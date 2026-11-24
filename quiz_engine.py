"""Reusable quiz engine: next/previous, optional timer, instant check, score + result screen.

Used by Listening, Grammar quiz, Practice Quiz, Skill Test and Mock Test.
Each quiz keeps its own state in st.session_state under its `key` prefix.
"""
import io
import math
import random
import struct
import time
import wave
from pathlib import Path

import streamlit as st

from ui import subheading

AUDIO_DIR = Path(__file__).parent / "data" / "audio"


# ---------- state helpers ----------
def _k(key: str, name: str) -> str:
    return f"{key}__{name}"


def reset_quiz(key: str):
    """Forget everything about a quiz so it starts fresh (also drops its radio widgets)."""
    s = st.session_state
    for k in [k for k in list(s.keys()) if str(k).startswith(f"{key}__")]:
        del s[k]


def prepare_questions(raw, limit=None, seed=None):
    """Turn (q, options, answer, explain[, transcript]) tuples into dicts with shuffled options."""
    rng = random.Random(seed)
    items = list(raw)
    if limit:
        items = rng.sample(items, min(limit, len(items)))
    out = []
    for item in items:
        q, options, ans, explain = item[:4]
        transcript = item[4] if len(item) > 4 else None
        order = list(range(len(options)))
        rng.shuffle(order)
        out.append({
            "q": q,
            "options": [options[i] for i in order],
            "answer": order.index(ans),
            "explain": explain,
            "transcript": transcript,
        })
    return out


def _init(key, raw, limit, timer_seconds):
    s = st.session_state
    if _k(key, "qs") not in s:
        s[_k(key, "qs")] = prepare_questions(raw, limit=limit)
        s[_k(key, "idx")] = 0
        s[_k(key, "answers")] = {}
        s[_k(key, "checked")] = set()
        s[_k(key, "done")] = False
        s[_k(key, "start")] = time.time()


# ---------- audio placeholder ----------
def make_beep_wav(seconds=1.2, freq=660, rate=16000) -> bytes:
    """Tiny generated WAV so the audio player is real and playable."""
    n = int(seconds * rate)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        frames = b"".join(
            struct.pack("<h", int(9000 * math.sin(2 * math.pi * freq * t / rate) * (1 - t / n)))
            for t in range(n)
        )
        w.writeframes(frames)
    return buf.getvalue()


def audio_player(key: str, idx: int, transcript: str | None):
    """Plays data/audio/<key>_<n>.mp3|wav if present, otherwise a placeholder beep."""
    real = next((p for ext in ("mp3", "wav", "ogg") if (p := AUDIO_DIR / f"{key}_{idx + 1}.{ext}").exists()), None)
    if real:
        st.audio(real.read_bytes())
    else:
        st.audio(make_beep_wav(), format="audio/wav")
        st.caption(f"🔊 Placeholder audio — asli recording ke liye file rakhein: data/audio/{key}_{idx + 1}.mp3")
    if transcript:
        with st.expander("📜 Transcript (آڈیو اسکرپٹ)"):
            st.markdown(f"<div class='rule-ko'>{transcript}</div>", unsafe_allow_html=True)


# ---------- callbacks ----------
def _save_answer(key, idx):
    s = st.session_state
    s[_k(key, "answers")][idx] = s[_k(key, f"radio{idx}")]


def _go(key, delta):
    st.session_state[_k(key, "idx")] += delta


def _finish(key):
    st.session_state[_k(key, "done")] = True


def _check(key, idx):
    st.session_state[_k(key, "checked")].add(idx)


# ---------- timer ----------
def _timer(key, seconds):
    @st.fragment(run_every=1)
    def tick():
        s = st.session_state
        if s.get(_k(key, "done")) or _k(key, "start") not in s:
            return
        remaining = int(s[_k(key, "start")] + seconds - time.time())
        if remaining <= 0:
            s[_k(key, "done")] = True
            st.rerun()
        m, sec = divmod(remaining, 60)
        st.markdown(f"<div class='timer-box'>⏱ {m:02d}:{sec:02d}</div>", unsafe_allow_html=True)

    tick()


# ---------- screens ----------
def _question_screen(key, title, timer_seconds, instant_feedback, with_audio):
    s = st.session_state
    qs, idx = s[_k(key, "qs")], s[_k(key, "idx")]
    answers = s[_k(key, "answers")]
    q = qs[idx]
    total = len(qs)

    top_l, top_r = st.columns([3, 1])
    with top_l:
        subheading(f"{title} — Question {idx + 1} / {total}")
    with top_r:
        if timer_seconds:
            _timer(key, timer_seconds)
    st.progress((idx + 1) / total, text=f"Answered: {len(answers)} / {total}")

    if with_audio:
        audio_player(key, idx, q["transcript"])

    st.markdown(f"<div class='q-card'>{q['q']}</div>", unsafe_allow_html=True)
    st.radio(
        "جواب منتخب کریں:", options=list(range(len(q["options"]))),
        format_func=lambda i: q["options"][i], index=answers.get(idx),
        key=_k(key, f"radio{idx}"), on_change=_save_answer, args=(key, idx),
    )

    if instant_feedback:
        st.button("✅ Check Answer", key=_k(key, f"chk{idx}"), on_click=_check, args=(key, idx),
                  disabled=idx not in answers)
        if idx in s[_k(key, "checked")]:
            if answers[idx] == q["answer"]:
                st.markdown("<div class='ok-box'>✔ صحیح جواب! Correct!</div>", unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<div class='bad-box'>✘ غلط۔ صحیح جواب: <b>{q['options'][q['answer']]}</b></div>",
                    unsafe_allow_html=True)
            st.caption(q["explain"])

    b1, b2, b3 = st.columns(3)
    with b1:
        st.button("⬅ Previous", key=_k(key, "prev"), on_click=_go, args=(key, -1), disabled=idx == 0)
    with b2:
        st.button("🏁 Finish", key=_k(key, "fin"), on_click=_finish, args=(key,))
    with b3:
        st.button("Next ➡", key=_k(key, "next"), on_click=_go, args=(key, 1), disabled=idx >= total - 1)


def compute_score(key):
    s = st.session_state
    qs, answers = s[_k(key, "qs")], s[_k(key, "answers")]
    correct = sum(1 for i, q in enumerate(qs) if answers.get(i) == q["answer"])
    return correct, len(qs)


def _result_screen(key, title, pass_pct):
    s = st.session_state
    qs, answers = s[_k(key, "qs")], s[_k(key, "answers")]
    correct, total = compute_score(key)
    pct = round(100 * correct / total)
    elapsed = int(time.time() - s[_k(key, "start")])

    subheading(f"🏆 {title} — Result")
    c1, c2, c3 = st.columns(3)
    c1.metric("Score", f"{correct} / {total}")
    c2.metric("Percentage", f"{pct}%")
    c3.metric("Time", f"{elapsed // 60:02d}:{elapsed % 60:02d}")

    if pass_pct is not None:
        if pct >= pass_pct:
            st.markdown(f"<div class='result-pass'>✔ PASS (کامیاب) — need {pass_pct}%</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-fail'>✘ FAIL (ناکام) — need {pass_pct}%</div>", unsafe_allow_html=True)
    elif pct >= 80:
        st.success("بہترین! Excellent work 🎉")
    elif pct >= 50:
        st.info("اچھی کوشش! مزید مشق کریں۔")
    else:
        st.warning("مزید تیاری کی ضرورت ہے۔")

    with st.expander(f"📋 Review answers ({total - correct} wrong / {total - len(answers)} skipped)"):
        for i, q in enumerate(qs):
            mine = answers.get(i)
            mark = "✔" if mine == q["answer"] else "✘"
            mine_txt = q["options"][mine] if mine is not None else "— (no answer)"
            st.markdown(
                f"**{mark} {i + 1}. {q['q']}**  \nYour answer: {mine_txt}  \n"
                f"Correct: **{q['options'][q['answer']]}** — {q['explain']}")

    st.button("🔄 Try Again", key=_k(key, "again"), on_click=reset_quiz, args=(key,))


# ---------- public API ----------
def run_quiz(key, raw_questions, title, *, limit=None, timer_seconds=None,
             pass_pct=None, instant_feedback=False, with_audio=False):
    """Render a full quiz. `key` must be unique per quiz."""
    _init(key, raw_questions, limit, timer_seconds)
    if st.session_state[_k(key, "done")]:
        _result_screen(key, title, pass_pct)
    else:
        _question_screen(key, title, timer_seconds, instant_feedback, with_audio)
