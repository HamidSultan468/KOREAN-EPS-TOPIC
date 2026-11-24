"""Skill Test tab: Easy / Medium / Hard, 10 questions each, pass/fail per level."""
import streamlit as st

from content.questions import SKILL_LEVELS
from quiz_engine import run_quiz
from ui import heading


def render():
    heading("🛠️ Skill Test Preparation")
    names = list(SKILL_LEVELS)
    level = st.radio(
        "Level منتخب کریں:", names, horizontal=True, key="skill_level",
        format_func=lambda n: f"{SKILL_LEVELS[n]['icon']} {n}  (pass {SKILL_LEVELS[n]['pass_pct']}%)",
    )
    cfg = SKILL_LEVELS[level]
    run_quiz(f"skill_{level.lower()}", cfg["questions"], f"Skill Test · {level}",
             pass_pct=cfg["pass_pct"], instant_feedback=True)
