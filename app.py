import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="KR KOREAN EPS-TOPIK PRO",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED RGB ANIMATED & BRIGHT GOLD CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600;700&display=swap');

    /* Global Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #150a21 0%, #050508 100%) !important;
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Ultra Bright Vibrant Gold 3D Title */
    .golden-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 3px;
        background: linear-gradient(180deg, #ffffff 0%, #fff700 35%, #ffd700 70%, #ffaa00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 
            0 0 15px rgba(255, 247, 0, 0.8),
            0 0 30px rgba(255, 215, 0, 0.6),
            0 3px 0 #b7791f,
            0 6px 0 #744210,
            0 9px 15px rgba(0, 0, 0, 0.9);
        margin-bottom: 2px;
    }

    .sub-title {
        text-align: center;
        color: #00f2fe;
        font-family: 'Orbitron', sans-serif;
        font-size: 1rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-shadow: 0 0 12px rgba(0, 242, 254, 0.8);
    }

    /* Stat Glow Cards */
    .stat-card {
        background: rgba(13, 17, 23, 0.7);
        border: 1.5px solid #00f2fe;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.25);
        transition: all 0.3s ease;
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

    /* Animated RGB Soft Glow Keyframes for Buttons */
    @keyframes rgbGlow {
        0% {
            border-color: #00f2fe;
            box-shadow: 0 0 12px rgba(0, 242, 254, 0.4), inset 0 0 8px rgba(0, 242, 254, 0.2);
            color: #00f2fe;
        }
        33% {
            border-color: #a855f7;
            box-shadow: 0 0 12px rgba(168, 85, 247, 0.4), inset 0 0 8px rgba(168, 85, 247, 0.2);
            color: #c084fc;
        }
        66% {
            border-color: #ffd700;
            box-shadow: 0 0 12px rgba(255, 215, 0, 0.4), inset 0 0 8px rgba(255, 215, 0, 0.2);
            color: #ffea79;
        }
        100% {
            border-color: #00f2fe;
            box-shadow: 0 0 12px rgba(0, 242, 254, 0.4), inset 0 0 8px rgba(0, 242, 254, 0.2);
            color: #00f2fe;
        }
    }

    /* Uniform & Equal Sized Neon Animated Buttons */
    div.stButton > button {
        width: 100% !important;
        height: 48px !important;
        background: rgba(10, 15, 30, 0.85) !important;
        border-radius: 25px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.88rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        animation: rgbGlow 6s infinite ease-in-out !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    div.stButton > button:hover {
        transform: scale(1.03) translateY(-2px) !important;
        background: rgba(20, 30, 55, 0.95) !important;
        box-shadow: 0 0 22px rgba(255, 255, 255, 0.6) !important;
    }

    /* Main Container Box */
    .neon-container {
        background: rgba(10, 14, 23, 0.8);
        border: 1.5px solid #00f2fe;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        margin-top: 20px;
    }

    .stTextArea textarea {
        background-color: #080d1a !important;
        color: #00f2fe !important;
        border: 1px solid #00f2fe !important;
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

# --- BRIGHT GOLD HEADER ---
st.markdown('<div class="golden-title">KR KOREAN EPS-TOPIK PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Next-Gen Language Learning Hub</div>', unsafe_allow_html=True)

# --- STATS ROW (3 Cards) ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="stat-card"><div class="stat-num">12</div><div class="stat-label">Total Books</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="stat-num">1,500+</div><div class="stat-label">Vocabulary</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="stat-num">60+</div><div class="stat-label">Lessons</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN NAVIGATION BUTTONS (Equal Width 4 Columns) ---
nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    btn_textbooks = st.button("Textbooks")
with nav2:
    btn_vocab = st.button("Vocabulary")
with nav3:
    btn_grammar = st.button("Grammar")
with nav4:
    btn_quiz = st.button("Practice Quiz")

# Navigation State Management
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Textbooks"

if btn_textbooks: st.session_state.active_tab = "Textbooks"
if btn_vocab: st.session_state.active_tab = "Vocabulary"
if btn_grammar: st.session_state.active_tab = "Grammar"
if btn_quiz: st.session_state.active_tab = "Practice Quiz"

# --- CONTENT AREA ---
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
    st.markdown('<h4 style="color: #00f2fe;">📄 Quick Paragraph Translator</h4>', unsafe_allow_html=True)
    ko_text = st.text_area("کورین متن درج کریں...", height=100)
    
    tb1, tb2 = st.columns([1, 3])
    with tb1:
        if st.button("Translate"):
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
    st.button("Start Online Test")

st.markdown('</div>', unsafe_allow_html=True)