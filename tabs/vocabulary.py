"""Vocabulary tab: 100 words with search + category filter."""
import html

import streamlit as st

from content.vocab import CATEGORIES, VOCAB
from ui import heading


def filter_words(query: str, category: str):
    q = query.strip().lower()
    return [
        w for w in VOCAB
        if (category == "All" or w[3] == category)
        and (not q or any(q in field.lower() for field in w))
    ]


def _table(words):
    rows = "".join(
        f"<tr><td class='ko'>{html.escape(ko)}</td><td class='ur'>{html.escape(ur)}</td>"
        f"<td class='pr'>{html.escape(pr)}</td><td>{html.escape(cat)}</td></tr>"
        for ko, ur, pr, cat in words
    )
    st.markdown(
        "<div class='vocab-wrap'><table class='vocab'><thead><tr><th>KOREAN</th><th>URDU</th>"
        f"<th>PRONUNCIATION</th><th>CATEGORY</th></tr></thead><tbody>{rows}</tbody></table></div>",
        unsafe_allow_html=True)


def render():
    heading("🔤 Vocabulary List")
    c1, c2 = st.columns([2, 1])
    query = c1.text_input("🔎 Search (Korean / Urdu / pronunciation):", key="vocab_search")
    category = c2.selectbox("Category:", ["All"] + CATEGORIES, key="vocab_cat")
    words = filter_words(query, category)
    st.caption(f"{len(words)} / {len(VOCAB)} words")
    if words:
        _table(words)
    else:
        st.warning("کوئی لفظ نہیں ملا۔ دوسرا search آزمائیں۔")
