"""Chatbot tab: rule-based EPS-TOPIK assistant. `ask_api` is the hook for a real LLM later."""
import os
import re

import streamlit as st

from content.grammar import RULES
from content.vocab import VOCAB
from ui import heading

# (keywords, answer) — first entry with the most keyword hits wins.
KNOWLEDGE = [
    (["eps", "topik", "exam", "امتحان", "ٹیسٹ", "test"],
     "EPS-TOPIK کوریا میں کام کے لیے کورین زبان کا امتحان ہے۔ اس میں Reading اور Listening کے سوالات ہوتے ہیں "
     "(کل 50 سوالات، 200 نمبر)۔ تازہ ترین تفصیل اور پاس سکور HRD Korea / اپنے ملک کی EPS ویب سائٹ سے ضرور چیک کریں۔"),
    (["hangul", "alphabet", "حروف", "الفبا", "한글"],
     "한글 (Hangul) میں 14 بنیادی حرفِ صحیح اور 10 حرفِ علت ہیں۔ پہلے ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ اور ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ سیکھیں، "
     "پھر انہیں جوڑ کر syllable بنائیں (مثال: ㅎ + ㅏ + ㄴ = 한)۔"),
    (["hello", "hi", "greet", "سلام", "안녕"],
     "안녕하세요! (annyeonghaseyo) = سلام۔ رسمی انداز میں 안녕하십니까؟ کہتے ہیں۔"),
    (["thank", "شکریہ", "감사"],
     "شکریہ = 감사합니다 (gamsahamnida)۔ جواب میں 천만에요 (cheonmaneyo) = کوئی بات نہیں۔"),
    (["sorry", "معذرت", "معاف", "죄송"],
     "معذرت = 죄송합니다 (joesonghamnida)۔ 'معاف کیجیے' کے لیے 실례합니다 بھی استعمال ہوتا ہے۔"),
    (["study", "tips", "prepare", "تیاری", "کیسے سیکھ", "learn"],
     "روزانہ کا منصوبہ: 1) 20 نئے الفاظ (Vocabulary tab)، 2) 2 گرامر rules (Grammar tab)، 3) 10 منٹ Listening، "
     "4) ہفتے میں ایک بار Mock Test۔ غلط جوابات کا review ضرور کریں۔"),
    (["number", "count", "گنتی", "عدد"],
     "دو نظام ہیں: خالص کورین (하나, 둘, 셋 ... 열) گھنٹے اور گنتی کے لیے، اور چینی-کوریائی (일, 이, 삼 ... 백, 천, 만) "
     "منٹ، پیسے اور تاریخ کے لیے۔ مثال: 세 시 삼십 분 = 3:30۔"),
    (["salary", "wage", "تنخواہ", "월급", "money", "پیسے"],
     "월급 = تنخواہ۔ 'میری تنخواہ کب ملے گی؟' = 월급은 언제 받아요؟ معاہدے (계약) میں تنخواہ اور اوور ٹائم (야근) لازمی دیکھیں۔"),
    (["visa", "ویزا", "비자"],
     "비자 = ویزا۔ ویزا اور کانٹریکٹ کی تازہ شرائط کے لیے صرف سرکاری ذرائع (HRD Korea / EPS) پر بھروسہ کریں۔"),
    (["safety", "danger", "fire", "accident", "حفاظت", "آگ", "حادثہ", "위험"],
     "حفاظت: 안전모 (ہیلمٹ) پہنیں، 위험 = خطرہ۔ آگ لگے تو 119 پر کال کریں، پولیس کے لیے 112۔ 조심하세요 = احتیاط کریں۔"),
    (["help", "مدد", "commands", "کیا کر"],
     "میں EPS-TOPIK کے سوالات، الفاظ کا مطلب ('meaning of 학교')، گرامر ('explain 에서') اور مفید جملوں میں مدد کر سکتا ہوں۔"),
]

FALLBACK = ("معذرت، میں یہ پوری طرح نہیں سمجھا۔ آپ یوں پوچھ سکتے ہیں: 'meaning of 학교'، 'explain 에서'، "
            "'EPS exam kya hai', 'study tips', 'numbers'۔")


def _tokens(text: str):
    return re.findall(r"[\w가-힣\u0600-\u06FF]+", text.lower())


def _lookup_word(text: str):
    """Match a vocab word typed as Korean, Urdu, or pronunciation."""
    lowered = text.lower()
    for ko, ur, pr, cat in VOCAB:
        if ko in text or pr in _tokens(lowered):
            return f"**{ko}** ({pr}) = {ur}  ·  Category: {cat}"
    return None


def _lookup_rule(text: str):
    """Return the rule whose particle/ending is the longest match in the text (에서 beats 에)."""
    best, best_len = None, 0
    for title, pattern, ko, ur, explain in RULES:
        marker = title.split(" — ")[0]
        for part in re.findall(r"[가-힣]+(?:/[가-힣]+)?", marker):
            for particle in part.split("/"):
                if particle in text and len(particle) > best_len:
                    best, best_len = (title, ko, ur, explain), len(particle)
    if best and len(text) < 40:
        title, ko, ur, explain = best
        return f"**{title}**\n\n{explain}\n\nمثال: {ko} — {ur}"
    return None


def ask_api(message: str, history: list) -> str | None:
    """Future hook: call an LLM here (set CHATBOT_API_KEY in .env). Return None to fall back to rules."""
    if not os.getenv("CHATBOT_API_KEY"):
        return None
    return None  # TODO: implement provider call


def get_reply(message: str, history: list | None = None) -> str:
    history = history or []
    api = ask_api(message, history)
    if api:
        return api
    lowered = message.lower()
    if any(w in lowered for w in ("meaning", "mean", "مطلب", "معنی", "کیا ہے")) or len(message.strip()) <= 12:
        word = _lookup_word(message)
        if word:
            return word
    wants_rule = any(w in lowered for w in ("explain", "grammar", "rule", "گرامر"))
    if wants_rule or (len(message.strip()) <= 8 and re.search(r"[은는이가을를에]", message)):
        rule = _lookup_rule(message)
        if rule:
            return rule
    tokens = set(_tokens(lowered))
    best, best_hits = None, 0
    for keywords, answer in KNOWLEDGE:
        hits = sum(1 for k in keywords if k in lowered or k in tokens)
        if hits > best_hits:
            best, best_hits = answer, hits
    if best:
        return best
    return _lookup_word(message) or FALLBACK


def render():
    heading("🤖 EPS-TOPIK Korean Assistant")
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    prompt = st.chat_input("اپنا سوال لکھیں... (e.g. meaning of 학교 / explain 에서 / study tips)")
    if prompt:
        reply = get_reply(prompt, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()
    if st.button("🗑 Clear chat", key="chat_clear"):
        st.session_state.chat_history = st.session_state.chat_history[:1]
        st.rerun()
