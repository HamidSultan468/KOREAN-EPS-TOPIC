"""EPS Topik Books tab: real PDF upload/save, download, preview, and 60-lesson editor (JSON)."""
import base64
import json
import re
from pathlib import Path

import streamlit as st

from ui import subheading

ROOT = Path(__file__).resolve().parent.parent
UPLOADS_DIR = ROOT / "uploads"
LESSONS_FILE = ROOT / "data" / "lessons.json"
LESSON_COUNT = 60
MAX_PREVIEW_PAGES = 100


# ---------- storage ----------
def safe_filename(name: str) -> str:
    """Strip any path and unsafe characters from an uploaded filename."""
    base = Path(name).name
    cleaned = re.sub(r"[^\w.\- ()가-힣\u0600-\u06FF]", "_", base).strip(" .")
    return cleaned or "book.pdf"


def save_upload(name: str, data: bytes, directory: Path = UPLOADS_DIR) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / safe_filename(name)
    if not target.suffix.lower() == ".pdf":
        target = target.with_suffix(".pdf")
    target.write_bytes(data)
    return target


def list_books(directory: Path = UPLOADS_DIR):
    return sorted(directory.glob("*.pdf")) if directory.exists() else []


def default_lessons():
    return {f"Lesson {i}": "" for i in range(1, LESSON_COUNT + 1)}


def load_lessons(path: Path = LESSONS_FILE) -> dict:
    lessons = default_lessons()
    if path.exists():
        try:
            lessons.update(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            st.warning("lessons.json پڑھنے میں مسئلہ آیا؛ خالی سبق دکھائے جا رہے ہیں۔")
    return lessons


def save_lessons(lessons: dict, path: Path = LESSONS_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(lessons, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------- preview ----------
def preview_pdf(data: bytes):
    """Render pages as images (works in every browser); fall back to st.pdf / iframe."""
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    if pymupdf:
        try:
            doc = pymupdf.open(stream=data, filetype="pdf")
        except Exception:
            st.error("یہ PDF کھل نہیں سکی۔ فائل خراب ہو سکتی ہے۔")
            return
        total = min(len(doc), MAX_PREVIEW_PAGES)
        page_no = st.number_input("Page", 1, max(total, 1), 1, key="pdf_page") if total > 1 else 1
        pix = doc[int(page_no) - 1].get_pixmap(dpi=110)
        caption = f"Page {int(page_no)} / {len(doc)}"
        try:
            st.image(pix.tobytes("png"), caption=caption, width="stretch")
        except TypeError:  # older Streamlit without width="stretch"
            st.image(pix.tobytes("png"), caption=caption, use_container_width=True)
        return
    if hasattr(st, "pdf"):
        try:
            st.pdf(data, height=650)
            return
        except Exception:
            pass
    b64 = base64.b64encode(data).decode()
    st.markdown(f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="650"></iframe>',
                unsafe_allow_html=True)


# ---------- sections ----------
def _upload_section():
    subheading("📤 نئی بک اپلوڈ کریں (Upload PDF)")
    uploaded = st.file_uploader("پی ڈی ایف فائل کا انتخاب کریں:", type=["pdf"], key="book_uploader")
    if uploaded is None:
        return
    data = uploaded.getvalue()
    if not data.startswith(b"%PDF"):
        st.error("یہ درست PDF فائل نہیں ہے۔")
        return
    saved_key = f"saved_{uploaded.name}_{len(data)}"
    if saved_key not in st.session_state:
        st.session_state[saved_key] = str(save_upload(uploaded.name, data))
    st.session_state.last_book = st.session_state[saved_key]
    st.success(f"فائل '{uploaded.name}' کامیابی سے اپلوڈ اور محفوظ ہو گئی ہے! (uploads/)")
    preview_pdf(data)


def _download_section():
    subheading("📥 کتابیں ڈاؤنلوڈ کریں (Download PDF)")
    books = list_books()
    if not books:
        st.info("ابھی کوئی کتاب اپلوڈ نہیں ہوئی۔ پہلے 'Upload PDF' سے کتاب شامل کریں۔")
        return
    names = [b.name for b in books]
    default = Path(st.session_state.get("last_book", "")).name
    choice = st.selectbox("کتاب منتخب کریں:", names, index=names.index(default) if default in names else 0,
                          key="book_choice")
    path = UPLOADS_DIR / choice
    st.download_button(f"📄 {choice} ڈاؤنلوڈ کریں", data=path.read_bytes(), file_name=choice,
                       mime="application/pdf", key="book_download")
    with st.expander("👁 Preview"):
        preview_pdf(path.read_bytes())


def _edit_section():
    subheading("✏️ سبق میں ترمیم کریں (Edit Text / Lesson)")
    lessons = load_lessons()
    lesson_num = st.selectbox("سبق کا نمبر منتخب کریں:", [f"Lesson {i}" for i in range(1, LESSON_COUNT + 1)],
                              key="lesson_choice")
    edited_text = st.text_area(f"{lesson_num} کے مواد میں ترمیم کریں:", value=lessons[lesson_num],
                               height=150, key=f"lesson_text_{lesson_num}")
    if st.button("محفوظ کریں", key="lesson_save"):
        lessons[lesson_num] = edited_text
        save_lessons(lessons)
        st.success(f"{lesson_num} محفوظ کر لیا گیا ہے! (data/lessons.json)")
    filled = sum(1 for v in lessons.values() if v.strip())
    st.caption(f"محفوظ شدہ اسباق: {filled} / {LESSON_COUNT}")


def render():
    st.markdown('<h3 style="color: #00f2fe;">📚 EPS Topik Books Manager</h3>', unsafe_allow_html=True)
    sub1, sub2, sub3 = st.columns(3)
    with sub1:
        if st.button("Upload PDF", key="sub_up_btn"):
            st.session_state.book_sub_action = "upload"
    with sub2:
        if st.button("Download PDF", key="sub_down_btn"):
            st.session_state.book_sub_action = "download"
    with sub3:
        if st.button("Edit Text / Lesson", key="sub_edit_btn"):
            st.session_state.book_sub_action = "edit"
    st.write("---")
    action = st.session_state.book_sub_action
    if action == "upload":
        _upload_section()
    elif action == "download":
        _download_section()
    elif action == "edit":
        _edit_section()
    else:
        st.info("اوپر دیے گئے بٹنوں (Upload, Download, Edit) پر کلک کر کے سبق اپلوڈ یا دیکھیں۔")
