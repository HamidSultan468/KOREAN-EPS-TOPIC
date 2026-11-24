"""Translation tab: Korean <-> Urdu / English using deep-translator (Python, no JS)."""
import streamlit as st

from ui import heading, subheading

DIRECTIONS = {
    "Korean → Urdu (کورین سے اردو)": ("ko", "ur"),
    "Urdu → Korean (اردو سے کورین)": ("ur", "ko"),
    "Korean → English": ("ko", "en"),
    "English → Korean": ("en", "ko"),
}
MAX_CHARS = 4500


MYMEMORY_CODES = {"ko": "ko-KR", "ur": "ur-PK", "en": "en-GB"}
MYMEMORY_MAX_CHARS = 450


def _google(text: str, source: str, target: str) -> str:
    from deep_translator import GoogleTranslator
    return GoogleTranslator(source=source, target=target).translate(text)


def _mymemory(text: str, source: str, target: str) -> str:
    from deep_translator import MyMemoryTranslator
    if len(text) > MYMEMORY_MAX_CHARS:
        raise ValueError("fallback limit")
    return MyMemoryTranslator(source=MYMEMORY_CODES[source], target=MYMEMORY_CODES[target]).translate(text)


def translate_text(text: str, source: str, target: str) -> str:
    """Translate with Google (deep-translator), falling back to MyMemory.

    Raises ValueError for bad input and RuntimeError (friendly Urdu/Roman message) if every provider fails.
    """
    text = text.strip()
    if not text:
        raise ValueError("empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"Text {MAX_CHARS} حروف سے چھوٹا رکھیں۔")
    try:
        import deep_translator  # noqa: F401
    except ImportError as exc:
        raise RuntimeError("deep-translator install nahi hai: pip install deep-translator") from exc

    errors = []
    for provider in (_google, _mymemory):
        try:
            result = provider(text, source, target)
            if result and result.strip():
                return result
        except Exception as exc:  # network, rate-limit, unsupported pair, too long
            errors.append(str(exc))
    detail = errors[0] if errors else "unknown error"
    if "too many requests" in detail.lower():
        raise RuntimeError("Google ne abhi requests rok di hain (rate limit). Thori der baad dobara try karein.")
    raise RuntimeError(f"Translation nahi ho saki — internet check karein aur dobara try karein. ({detail[:120]})")


def render():
    heading("🌐 Instant Korean Translator")
    label = st.selectbox("Direction:", list(DIRECTIONS), key="tr_dir")
    source, target = DIRECTIONS[label]
    text = st.text_area("متن لکھیں:", height=130, key="tr_input", placeholder="안녕하세요, 저는 공장에서 일합니다.")
    if st.button("🌐 Translate", key="tr_go"):
        try:
            st.session_state.tr_result = translate_text(text, source, target)
        except ValueError as exc:
            st.session_state.tr_result = None
            if str(exc) != "empty":
                st.warning(str(exc))
            else:
                st.warning("پہلے کچھ متن لکھیں۔")
        except RuntimeError as exc:
            st.session_state.tr_result = None
            st.error(str(exc))
    result = st.session_state.get("tr_result")
    if result:
        subheading("ترجمہ (Translation)")
        st.markdown(
            f"<div class='q-card' style='direction:{'rtl' if target == 'ur' else 'ltr'}'>{result}</div>",
            unsafe_allow_html=True)
