"""Mock Test tab: 25 random questions mixed from every bank, timed, pass at 60%."""
import streamlit as st

from content.grammar import QUIZ
from content.questions import PRACTICE, SKILL_EASY, SKILL_HARD, SKILL_MEDIUM
from quiz_engine import run_quiz
from ui import heading

QUESTION_COUNT = 25
TIME_LIMIT_SECONDS = 25 * 60


def render():
    heading("🎓 Mock Test")
    st.info(f"{QUESTION_COUNT} random سوالات · {TIME_LIMIT_SECONDS // 60} منٹ · پاس کے لیے 60%")
    pool = PRACTICE + QUIZ + SKILL_EASY + SKILL_MEDIUM + SKILL_HARD
    run_quiz("mock", pool, "Mock Test", limit=QUESTION_COUNT,
             timer_seconds=TIME_LIMIT_SECONDS, pass_pct=60)
