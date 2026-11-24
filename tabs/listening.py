"""Listening tab: 10 questions, audio player, answer check, score."""
from content.questions import LISTENING
from quiz_engine import run_quiz
from ui import heading


def render():
    heading("🎧 Listening Section")
    run_quiz("listening", LISTENING, "Listening Test", instant_feedback=True,
             with_audio=True, pass_pct=60)
