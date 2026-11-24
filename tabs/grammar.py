"""Grammar tab: 20 rules (Korean + Urdu) and a 10-question quiz."""
import html

import streamlit as st

from content.grammar import QUIZ, RULES
from quiz_engine import run_quiz
from ui import heading


def _rules():
    query = st.text_input("🔎 Rule تلاش کریں (Korean / Urdu / English):", key="grammar_search").strip().lower()
    shown = 0
    for i, (title, pattern, ko, ur, explain) in enumerate(RULES, 1):
        blob = " ".join((title, pattern, ko, ur, explain)).lower()
        if query and query not in blob:
            continue
        shown += 1
        with st.expander(f"{i}. {title}"):
            st.markdown(f"<div class='rule-pattern'>{html.escape(pattern)}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='rule-ur'>{explain}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='rule-ko'>▶ {ko}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='rule-ur'>{ur}</div>", unsafe_allow_html=True)
    st.caption(f"Showing {shown} / {len(RULES)} rules")


def render():
    heading("📘 Korean Grammar Rules")
    view = st.radio("Section:", ["📖 Rules (20)", "📝 Grammar Quiz (10)"], horizontal=True, key="grammar_view")
    if view.startswith("📖"):
        _rules()
    else:
        run_quiz("grammar_quiz", QUIZ, "Grammar Quiz", instant_feedback=True, pass_pct=60)
