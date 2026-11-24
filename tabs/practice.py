"""Practice Quiz tab: 20 MCQs, 20-minute timer, next/previous, result screen."""
from content.questions import PRACTICE
from quiz_engine import run_quiz
from ui import heading

TIME_LIMIT_SECONDS = 20 * 60


def render():
    heading("📝 Practice Quiz")
    run_quiz("practice", PRACTICE, "Practice Quiz", timer_seconds=TIME_LIMIT_SECONDS, pass_pct=60)
