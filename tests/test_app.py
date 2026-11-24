"""Run with:  python tests/test_app.py   (or pytest tests/)"""
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from streamlit.testing.v1 import AppTest  # noqa: E402

from content.grammar import QUIZ, RULES  # noqa: E402
from content.questions import LISTENING, PRACTICE, SKILL_LEVELS  # noqa: E402
from content.vocab import VOCAB  # noqa: E402
from quiz_engine import prepare_questions  # noqa: E402
from tabs import books, chatbot, vocabulary  # noqa: E402

APP = str(ROOT / "app.py")


def _app():
    at = AppTest.from_file(APP, default_timeout=30)
    at.run()
    assert not at.exception, at.exception
    return at


def _open(tab_button_key):
    at = _app()
    at.button(key=tab_button_key).click().run()
    assert not at.exception, at.exception
    return at


# ---------- content ----------
def test_content_counts():
    assert len(VOCAB) == 100 and len({w[0] for w in VOCAB}) == 100
    assert len(RULES) == 20 and len(QUIZ) == 10
    assert len(LISTENING) == 10 and len(PRACTICE) == 20
    assert all(len(c["questions"]) == 10 for c in SKILL_LEVELS.values()) and len(SKILL_LEVELS) == 3


def test_shuffle_keeps_correct_answer():
    for raw in (LISTENING, PRACTICE, QUIZ, *[c["questions"] for c in SKILL_LEVELS.values()]):
        original = {r[0]: r[1][r[2]] for r in raw}
        for seed in range(5):
            for q in prepare_questions(raw, seed=seed):
                assert q["options"][q["answer"]] == original[q["q"]]
    positions = {q["answer"] for q in prepare_questions(PRACTICE, seed=1)}
    assert len(positions) > 1, "answers must not all sit in the same position"


# ---------- logic ----------
def test_vocab_filter():
    assert len(vocabulary.filter_words("", "All")) == 100
    assert vocabulary.filter_words("학교", "All")[0][2] == "hakgyo"
    assert all(w[3] == "Food" for w in vocabulary.filter_words("", "Food"))
    assert vocabulary.filter_words("zzzz", "All") == []


def test_chatbot_replies():
    assert "school" in chatbot.get_reply("meaning of 학교").lower() or "اسکول" in chatbot.get_reply("meaning of 학교")
    assert "에서" in chatbot.get_reply("explain 에서")
    assert "EPS-TOPIK" in chatbot.get_reply("EPS exam kya hai")
    assert chatbot.get_reply("qwertyuiop asdf") == chatbot.FALLBACK


def test_books_storage_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        p = books.save_upload("../../evil name.pdf", b"%PDF-1.4 test", tmp)
        assert p.parent == tmp and p.read_bytes() == b"%PDF-1.4 test"
        assert [b.name for b in books.list_books(tmp)] == [p.name]
        lessons = books.default_lessons()
        assert len(lessons) == 60
        lessons["Lesson 7"] = "안녕하세요 — سلام"
        books.save_lessons(lessons, tmp / "lessons.json")
        assert books.load_lessons(tmp / "lessons.json")["Lesson 7"] == "안녕하세요 — سلام"


# ---------- UI flows (headless) ----------
def test_nav_has_mock_test_and_no_empty_10():
    at = _app()
    labels = [b.label for b in at.button]
    assert "Mock Test" in labels and "Empty 10" not in labels


def test_every_tab_renders():
    for key in [f"nav_btn{i}" for i in range(1, 11)]:
        _open(key)


def test_listening_check_and_score():
    at = _open("nav_btn3")
    at.radio(key="listening__radio0").set_value(0).run()
    at.button(key="listening__chk0").click().run()
    assert not at.exception
    for _ in range(9):
        at.button(key="listening__next").click().run()
    at.button(key="listening__fin").click().run()
    assert not at.exception and any(m.label == "Score" for m in at.metric)


def test_practice_full_run_and_result():
    at = _open("nav_btn5")
    at.button(key="practice__fin").click().run()
    assert any(m.label == "Score" and m.value == "0 / 20" for m in at.metric)
    at.button(key="practice__again").click().run()
    assert any("Question 1 / 20" in m.value for m in at.markdown)


def test_skill_levels_pass_fail():
    at = _open("nav_btn8")
    for level in ("Easy", "Medium", "Hard"):
        at.radio(key="skill_level").set_value(level).run()
        assert any(f"Question 1 / 10" in m.value for m in at.markdown), level
    at.button(key="skill_hard__fin").click().run()
    assert any("FAIL" in m.value for m in at.markdown)


def test_mock_test_has_25_questions():
    at = _open("nav_btn10")
    assert any("Question 1 / 25" in m.value for m in at.markdown)


def test_grammar_rules_and_quiz():
    at = _open("nav_btn4")
    assert len(at.expander) == 20
    at.text_input(key="grammar_search").set_value("에서").run()
    assert 0 < len(at.expander) < 20
    at.radio(key="grammar_view").set_value("📝 Grammar Quiz (10)").run()
    assert any("Question 1 / 10" in m.value for m in at.markdown)


def test_vocabulary_tab_search_filter():
    at = _open("nav_btn9")
    assert any("100 / 100 words" in c.value for c in at.caption)
    at.selectbox(key="vocab_cat").set_value("Food").run()
    assert any("10 / 100 words" in c.value for c in at.caption)


def test_chatbot_tab_conversation():
    at = _open("nav_btn6")
    at.chat_input[0].set_value("meaning of 학교").run()
    assert not at.exception
    assert len(at.session_state.chat_history) == 3


def test_translation_tab_handles_empty_and_runs():
    at = _open("nav_btn7")
    at.button(key="tr_go").click().run()
    assert any("متن" in w.value for w in at.warning)


if __name__ == "__main__":
    failed = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS  {name}")
            except Exception as exc:  # report every failure
                failed += 1
                print(f"FAIL  {name}: {type(exc).__name__}: {exc}")
    sys.exit(1 if failed else 0)
