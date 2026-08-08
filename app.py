import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="KR KOREAN EPS-TOPIK PRO",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CYBERPUNK & GOLDEN 3D CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Rajdhani:wght@600;700&display=swap');

    /* Global Background */
    .stApp {
        background: radial-gradient(circle at 80% 20%, #150a21 0%, #08070c 100%) !important;
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* 3D Gold Embossed Main Title */
    .golden-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #ffe066 0%, #f59e0b 50%, #b45309 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 
            0 2px 0 #78350f,
            0 4px 0 #451a03,
            0 6px 10px rgba(0, 0, 0, 0.8),
            0 0 20px rgba(245, 158, 11, 0.4);
        margin-bottom: 2px;
    }

    .sub-title {
        text-align: center;
        color: #38bdf8;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.95rem;
        letter-spacing: 1px;
        margin-bottom: 25px;
        text-shadow: 0 0 8px rgba(56, 189, 248, 0.6);
    }

    /* Stat Glow Cards */
    .stat-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1.5px solid #00f2fe;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.25), inset 0 0 10px rgba(0, 242, 254, 0.1);
        transition: all 0.3s ease;
    }
    .stat-card:hover {
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.5), inset 0 0 15px rgba(0, 242, 254, 0.2);
        transform: translateY(-2px);
    }
    .stat-num {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: #00f2fe;
        text-shadow: 0 0 10px #00f2fe;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #94a3b8;
        font-weight: 600;
    }

    /* Neon Container Box */
    .neon-container {
        background: rgba(13, 17, 23, 0.75);
        border: 1.5px solid #38bdf8;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        margin-top: 20px;
    }

    /* Streamlit Custom Neon Buttons */
    div.stButton > button {
        width: 100% !important;
        background: rgba(15, 23, 42, 0.8) !important;
        color: #38bdf8 !important;
        border: 1.5px solid #38bdf8 !important;
        border-radius: 20px !important;
        padding: 10px 20px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #090d16 !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.8), 0 0 30px rgba(56, 189, 248, 0.5) !important;
        transform: scale(1.02);
    }

    /* Text Area Styling */
    .stTextArea textarea {
        background-color: #0f172a !important;
        color: #00f2fe !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- JS INJECTION ---
try:
    with open("script.js", "r", encoding="utf-8") as f:
        js_code = f.read()
    components.html(f"<script>{js_code}</script>", height=0)
except Exception:
    pass

# --- 3D GOLD HEADER ---
st.markdown('<div class="golden-title">KR KOREAN EPS-TOPIK PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Next-Gen Language Learning Hub</div>', unsafe_allow_html=True)

# --- STATS ROW (3 Neon Cards) ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="stat-card"><div class="stat-num">12</div><div class="stat-label">Total Books</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="stat-num">1,500+</div><div class="stat-label">Vocabulary</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="stat-num">60+</div><div class="stat-label">Lessons</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN NAVIGATION BUTTONS ROW ---
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    btn_textbooks = st.button("Textbooks")
with nav2:
    btn_vocab = st.button("Vocabulary")
with nav3:
    btn_grammar = st.button("Grammar")
with nav4:
    btn_quiz = st.button("Practice Quiz")

# State Management for Navigation
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Textbooks"

if btn_textbooks: st.session_state.active_tab = "Textbooks"
if btn_vocab: st.session_state.active_tab = "Vocabulary"
if btn_grammar: st.session_state.active_tab = "Grammar"
if btn_quiz: st.session_state.active_tab = "Practice Quiz"

# --- MAIN CONTENT AREA (NEON CONTAINER) ---
st.markdown('<div class="neon-container">', unsafe_allow_html=True)

if st.session_state.active_tab == "Textbooks":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📚 EPS-Topik Official Textbooks</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8;">Download official books directly:</p>', unsafe_allow_html=True)
    
    b1, b2, b3 = st.columns(3)
    with b1:
        st.button("Download Book 1")
    with b2:
        st.button("Download Book 2")
    with b3:
        st.button("Listening Tracks")
        
    st.markdown("---")
    st.markdown('<h4 style="color: #38bdf8;">📄 Quick Paragraph Translator</h4>', unsafe_allow_html=True)
    ko_text = st.text_area("کورین متن درج کریں...", height=100)
    if st.button("Translate / ترجمہ کریں"):
        if ko_text:
            st.info(f"ترجمہ: {ko_text}")

elif st.session_state.active_tab == "Vocabulary":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🔤 Vocabulary Database</h3>', unsafe_allow_html=True)
    vocab_data = [
        {"Korean": "안녕하세요", "Meaning": "سلام / آپ کیسے ہیں؟"},
        {"Korean": "감사합니다", "Meaning": "شکریہ"},
        {"Korean": "선생님", "Meaning": "استاد"},
        {"Korean": "학생", "Meaning": "طالب علم"}
    ]
    st.table(vocab_data)

elif st.session_state.active_tab == "Grammar":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📖 Grammar Rules</h3>', unsafe_allow_html=True)
    st.markdown("* **입니다 (Imnida):** یہ (Is/Am/Are) کے لیے استعمال ہوتا ہے۔")

elif st.session_state.active_tab == "Practice Quiz":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📝 Practice Quiz Engine</h3>', unsafe_allow_html=True)
    st.button("🚀 Start Online Test")

st.markdown('</div>', unsafe_allow_html=True)