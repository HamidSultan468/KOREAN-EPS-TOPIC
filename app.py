import streamlit as st
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="KR KOREAN EPS-TOPIK PRO",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING (KEEPING BEAUTIFUL DESIGN) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 10%, #150a21 0%, #050508 100%) !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif;
    }

    div, p, label, span, h1, h2, h3, h4, h5, h6 {
        font-family: 'Noto Nastaliq Urdu', 'Rajdhani', sans-serif !important;
    }

    .golden-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #ffffff 0%, #fff700 35%, #ffd700 70%, #ffaa00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 15px rgba(255, 247, 0, 0.8), 0 3px 0 #b7791f, 0 9px 15px rgba(0, 0, 0, 0.9);
        margin-bottom: 2px;
    }

    .sub-title {
        text-align: center;
        color: #00f2fe;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.95rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-shadow: 0 0 12px rgba(0, 242, 254, 0.8);
    }

    div[data-testid="column"] { padding: 0px 4px !important; }
    div.stButton { width: 100% !important; }

    @keyframes rgbGlow {
        0% { border-color: #00f2fe; box-shadow: 0 0 12px rgba(0, 242, 254, 0.4); color: #00f2fe; }
        33% { border-color: #a855f7; box-shadow: 0 0 12px rgba(168, 85, 247, 0.4); color: #c084fc; }
        66% { border-color: #ffd700; box-shadow: 0 0 12px rgba(255, 215, 0, 0.4); color: #ffea79; }
        100% { border-color: #00f2fe; box-shadow: 0 0 12px rgba(0, 242, 254, 0.4); color: #00f2fe; }
    }

    div.stButton > button {
        width: 100% !important;
        height: 55px !important;
        background: rgba(10, 15, 30, 0.9) !important;
        border-radius: 30px !important;
        border: 2px solid #00f2fe !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.80rem !important;
        font-weight: 700 !important;
        text-align: center !important;
        animation: rgbGlow 6s infinite ease-in-out !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .neon-container {
        background: rgba(10, 14, 23, 0.9);
        border: 1.5px solid #00f2fe;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        margin-top: 25px;
    }

    /* Info Bar & File Uploader Styling Fixes */
    div.stAlert {
        background-color: rgba(0, 242, 254, 0.2) !important;
        border: 1.5px solid #00f2fe !important;
        border-radius: 10px !important;
    }

    div.stAlert p, div.stAlert span {
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
    }

    div[data-testid="stFileUploader"] {
        background-color: #0f172a !important;
        border: 2px dashed #00f2fe !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] label {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="golden-title">KR KOREAN EPS-TOPIK PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Next-Gen Language Learning Hub</div>', unsafe_allow_html=True)

# --- SESSION STATE RESTORATION ---
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "EPS Topik Books"

if 'book_sub_action' not in st.session_state:
    st.session_state.book_sub_action = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "안녕하세요! (سلام) میں آپ کا EPS-TOPIK AI اسسٹنٹ ہوں۔"}
    ]

# --- NAVIGATION BUTTONS LINE 1 ---
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    if st.button("EPS Topik Books", key="nav_btn1"): 
        st.session_state.active_tab = "EPS Topik Books"
        st.session_state.book_sub_action = None
with c2:
    if st.button("Reading", key="nav_btn2"): st.session_state.active_tab = "Reading"
with c3:
    if st.button("Listening", key="nav_btn3"): st.session_state.active_tab = "Listening"
with c4:
    if st.button("Grammar", key="nav_btn4"): st.session_state.active_tab = "Grammar"
with c5:
    if st.button("Practice Quiz", key="nav_btn5"): st.session_state.active_tab = "Practice Quiz"

st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS LINE 2 ---
c6, c7, c8, c9, c10 = st.columns(5)
with c6:
    if st.button("Chatbot", key="nav_btn6"): st.session_state.active_tab = "Chatbot"
with c7:
    if st.button("Translation", key="nav_btn7"): st.session_state.active_tab = "Translation"
with c8:
    if st.button("Skill Test", key="nav_btn8"): st.session_state.active_tab = "Skill Test"
with c9:
    if st.button("Vocabulary", key="nav_btn9"): st.session_state.active_tab = "Vocabulary"
with c10:
    st.button("Empty 10", key="nav_btn10", disabled=True)

# --- MAIN CONTENT AREA ---
st.markdown('<div class="neon-container">', unsafe_allow_html=True)

# 1. EPS TOPIK BOOKS SECTION (RESTORED ORIGINAL STRUCTURE)
if st.session_state.active_tab == "EPS Topik Books":
    st.markdown('<h3 style="color: #00f2fe;">📚 EPS Topik Books Manager</h3>', unsafe_allow_html=True)
    
    sub1, sub2, sub3 = st.columns(3)
    with sub1:
        if st.button("Upload PDF", key="sub_up_btn"):
            st.session_state.book_sub_action = "upload"
    with sub2:
        if st.button("Download PDF", key="sub_down_btn"):
            st.session_state.book_sub_action = "download"
    with sub3:
        if st.button("Edit Text / Lesson", key="sub_edit_btn"):
            st.session_state.book_sub_action = "edit"
        
    st.write("---")
    
    if st.session_state.book_sub_action == "upload":
        st.markdown("<h4 style='color: #ffd700;'>📤 نئی بک اپلوڈ کریں (Upload PDF)</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("پی ڈی ایف فائل کا انتخاب کریں:", type=["pdf"])
        
        if uploaded_file is not None:
            st.success(f"فائل '{uploaded_file.name}' کامیابی سے اپلوڈ ہو گئی ہے!")
            
            # Standard Streamlit PDF Display iFrame
            base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="650" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    elif st.session_state.book_sub_action == "download":
        st.markdown("<h4 style='color: #ffd700;'>📥 کتابیں ڈاؤنلوڈ کریں (Download PDF)</h4>", unsafe_allow_html=True)
        st.download_button(
            label="📄 EPS Topik Book 1 ڈاؤنلوڈ کریں",
            data=b"Sample PDF Content",
            file_name="EPS_Topik_Book_1.pdf",
            mime="application/pdf"
        )

    elif st.session_state.book_sub_action == "edit":
        st.markdown("<h4 style='color: #ffd700;'>✏️ سبق میں ترمیم کریں (Edit Text / Lesson)</h4>", unsafe_allow_html=True)
        lesson_num = st.selectbox("سبق کا نمبر منتخب کریں:", [f"Lesson {i}" for i in range(1, 61)])
        edited_text = st.text_area(f"{lesson_num} کے مواد میں ترمیم کریں:", height=150)
        if st.button("محفوظ کریں"):
            st.success("معلومات محفوظ کر لی گئی ہیں!")
            
    else:
        st.info("اوپر دیے گئے بٹنوں (Upload, Download, Edit) پر کلک کر کے سبق اپلوڈ یا دیکھیں۔")

# 2. OTHER TABS (STABLE)
elif st.session_state.active_tab == "Reading":
    st.markdown('<h3 style="color: #00f2fe;">📖 Reading Section</h3>', unsafe_allow_html=True)
    st.radio("صحیح جواب منتخب کریں:", ["1. 가방", "2. 안경", "3. 모자", "4. 구두"])

elif st.session_state.active_tab == "Listening":
    st.markdown('<h3 style="color: #00f2fe;">🎧 Listening Section</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Grammar":
    st.markdown('<h3 style="color: #00f2fe;">📘 Korean Grammar Rules</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Practice Quiz":
    st.markdown('<h3 style="color: #00f2fe;">📝 Practice Quiz</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Chatbot":
    st.markdown('<h3 style="color: #00f2fe;">🤖 EPS-TOPIK Korean Assistant</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Translation":
    st.markdown('<h3 style="color: #00f2fe;">🌐 Instant Korean Translator</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Skill Test":
    st.markdown('<h3 style="color: #00f2fe;">🛠️ Skill Test Preparation</h3>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Vocabulary":
    st.markdown('<h3 style="color: #00f2fe;">🔤 Vocabulary List</h3>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)