"""Shared neon UI helpers (same look as the main app)."""
import streamlit as st

EXTRA_CSS = """
<style>
    /* ---- Shared neon styling for all tab content ---- */
    div[data-testid="stRadio"] label p, div[data-testid="stCheckbox"] label p {
        color: #ffffff !important; font-size: 1.05rem !important;
    }
    div[data-testid="stRadio"] > div[role="radiogroup"] > label {
        background: rgba(0, 242, 254, 0.07); border: 1px solid rgba(0, 242, 254, 0.35);
        border-radius: 12px; padding: 8px 14px; margin-bottom: 6px;
    }
    div[data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
        border-color: #ffd700; box-shadow: 0 0 10px rgba(255, 215, 0, 0.35);
    }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div, textarea, input {
        background-color: #0f172a !important; color: #ffffff !important;
        border: 1.5px solid #00f2fe !important; border-radius: 10px !important;
    }
    div[data-testid="stExpander"] {
        background: rgba(10, 14, 23, 0.9); border: 1.5px solid rgba(0, 242, 254, 0.6) !important;
        border-radius: 12px; margin-bottom: 8px;
    }
    div[data-testid="stExpander"] summary p { color: #ffd700 !important; font-weight: bold; }
    div[data-testid="stMetric"] {
        background: rgba(0, 242, 254, 0.08); border: 1.5px solid #00f2fe;
        border-radius: 14px; padding: 12px 16px; box-shadow: 0 0 14px rgba(0, 242, 254, 0.25);
    }
    div[data-testid="stMetricValue"] { color: #ffd700 !important; font-family: 'Orbitron', sans-serif !important; }
    div[data-testid="stMetricLabel"] p { color: #00f2fe !important; }
    div[data-testid="stProgress"] > div > div > div > div { background: linear-gradient(90deg, #00f2fe, #a855f7, #ffd700) !important; }
    div[data-testid="stAudio"] audio, audio { width: 100%; filter: hue-rotate(160deg); }
    div[data-testid="stChatMessage"] {
        background: rgba(10, 14, 23, 0.85); border: 1px solid rgba(0, 242, 254, 0.45); border-radius: 14px;
    }
    div[data-testid="stChatMessage"] p { color: #ffffff !important; }

    .q-card {
        background: rgba(15, 23, 42, 0.95); border: 1.5px solid #a855f7; border-radius: 14px;
        padding: 16px 20px; margin: 10px 0; font-size: 1.25rem; color: #ffffff;
        box-shadow: 0 0 16px rgba(168, 85, 247, 0.3);
    }
    .timer-box {
        display: inline-block; font-family: 'Orbitron', sans-serif !important; font-size: 1.4rem;
        color: #ffd700; border: 2px solid #ffd700; border-radius: 30px; padding: 6px 22px;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.8); box-shadow: 0 0 14px rgba(255, 215, 0, 0.35);
    }
    .ok-box { border: 1.5px solid #22c55e; background: rgba(34,197,94,0.15); border-radius: 10px; padding: 10px 14px; color: #bbf7d0; }
    .bad-box { border: 1.5px solid #ef4444; background: rgba(239,68,68,0.15); border-radius: 10px; padding: 10px 14px; color: #fecaca; }
    .result-pass { color: #22c55e; font-family: 'Orbitron', sans-serif !important; font-size: 2rem; text-align: center; text-shadow: 0 0 18px rgba(34,197,94,0.8); }
    .result-fail { color: #ef4444; font-family: 'Orbitron', sans-serif !important; font-size: 2rem; text-align: center; text-shadow: 0 0 18px rgba(239,68,68,0.8); }
    .vocab-wrap { max-height: 560px; overflow-y: auto; border: 1.5px solid #00f2fe; border-radius: 12px; }
    table.vocab { width: 100%; border-collapse: collapse; color: #ffffff; }
    table.vocab th { position: sticky; top: 0; background: #0f172a; color: #ffd700; padding: 10px; border-bottom: 2px solid #00f2fe; font-family: 'Orbitron', sans-serif !important; font-size: 0.8rem; }
    table.vocab td { padding: 8px 12px; border-bottom: 1px solid rgba(0, 242, 254, 0.2); text-align: center; }
    table.vocab tr:hover td { background: rgba(0, 242, 254, 0.1); }
    td.ko { color: #00f2fe; font-size: 1.2rem; font-weight: bold; }
    td.ur { color: #ffea79; font-size: 1.1rem; direction: rtl; }
    td.pr { color: #c084fc; }
    .rule-pattern { color: #00f2fe; font-family: 'Orbitron', sans-serif !important; font-size: 0.9rem; }
    .rule-ko { color: #ffd700; font-size: 1.2rem; }
    .rule-ur { direction: rtl; text-align: right; color: #ffffff; line-height: 2; }
</style>
"""


def inject_extra_css():
    st.markdown(EXTRA_CSS, unsafe_allow_html=True)


def heading(text: str):
    """Cyan section heading used by every tab."""
    st.markdown(f'<h3 style="color: #00f2fe;">{text}</h3>', unsafe_allow_html=True)


def subheading(text: str):
    """Gold sub-heading used inside tabs."""
    st.markdown(f"<h4 style='color: #ffd700;'>{text}</h4>", unsafe_allow_html=True)
