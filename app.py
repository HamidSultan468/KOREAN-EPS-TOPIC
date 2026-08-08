import streamlit as st
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="KR KOREAN EPS-TOPIK PRO",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED HIGH-CONTRAST & URDU STYLING CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

    /* Global Background & High Contrast Text */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #150a21 0%, #050508 100%) !important;
        color: #ffffff !important;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Urdu Text Global Style */
    div, p, label, span, h1, h2, h3, h4, h5, h6 {
        font-family: 'Noto Nastaliq Urdu', 'Rajdhani', sans-serif !important;
    }

    /* Vibrant Gold 3D Title */
    .golden-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
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
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.95rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-shadow: 0 0 12px rgba(0, 242, 254, 0.8);
    }

    /* Navigation Buttons Grid Fix */
    div[data-testid="column"] {
        padding: 0px 4px !important;
    }

    div.stButton {
        width: 100% !important;
    }

    /* RGB Glow Animation */
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
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 2px 5px !important;
    }

    div.stButton > button:hover {
        transform: scale(1.04) translateY(-2px) !important;
        background: rgba(20, 30, 55, 1) !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.8) !important;
    }

    /* Main Container Box */
    .neon-container {
        background: rgba(10, 14, 23, 0.9);
        border: 1.5px solid #00f2fe;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        margin-top: 25px;
    }

    /* FIX FOR INFO BOX / PATTI WHITE TEXT */
    div.stAlert {
        background-color: rgba(0, 242, 254, 0.2) !important;
        border: 1.5px solid #00f2fe !important;
        border-radius: 10px !important;
    }

    div.stAlert p, div.stAlert div, div.stAlert span {
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: bold !important;
        line-height: 2.2rem !important;
        text-shadow: 0 0 4px rgba(0, 0, 0, 0.8) !important;
    }

    /* File Uploader Styling */
    div[data-testid="stFileUploader"] {
        background-color: #0f172a !important;
        border: 2px dashed #00f2fe !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }

    div[data-testid="stFileUploader"] section {
        background-color: #0f172a !important;
    }

    div[data-testid="stFileUploader"] span, 
    div[data-testid="stFileUploader"] small,
    div[data-testid="stFileUploader"] label {
        color: #ffffff !important;
        font-size: 1.05rem !important;
    }

    div[data-testid="stFileUploader"] button {
        background: #00f2fe !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }

    /* Clean Styled Table for Vocabulary */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 1.1rem;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15);
    }
    .styled-table thead tr {
        background-color: #00f2fe;
        color: #050508;
        text-align: left;
        font-weight: bold;
    }
    .styled-table th, .styled-table td {
        padding: 12px 15px;
        border-bottom: 1px solid rgba(0, 242, 254, 0.2);
    }
    .styled-table tbody tr {
        background-color: rgba(15, 23, 42, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Helper Function to Display PDF File
def display_pdf(file_bytes):
    base64_pdf = base64.b64encode(file_bytes).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf" style="border-radius: 10px; border: 2px solid #00f2fe;">'
    st.markdown(pdf_display, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="golden-title">KR KOREAN EPS-TOPIK PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Next-Gen Language Learning Hub</div>', unsafe_allow_html=True)

# Session State Initializations
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "EPS Topik Books"

if 'book_sub_action' not in st.session_state:
    st.session_state.book_sub_action = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "안녕하세요! (سلام) میں آپ کا EPS-TOPIK AI اسسٹنٹ ہوں۔ کورین زبان سے متعلق کچھ بھی پوچھیں!"}
    ]

# --- LINE 1: NAVIGATION BUTTONS ---
c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
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

# --- LINE 2: NAVIGATION BUTTONS ---
c6, c7, c8, c9, c10 = st.columns([1, 1, 1, 1, 1])
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

# --- DYNAMIC CONTENT CONTAINER ---
st.markdown('<div class="neon-container">', unsafe_allow_html=True)

# 1. EPS TOPIK BOOKS SECTION
if st.session_state.active_tab == "EPS Topik Books":
    st.markdown('<h3 style="color: #00f2fe;">📚 EPS Topik Books Manager</h3>', unsafe_allow_html=True)
    
    sub1, sub2, sub3 = st.columns([1, 1, 1])
    with sub1:
        if st.button("📤 Upload PDF", key="sub_up_btn"):
            st.session_state.book_sub_action = "upload"
    with sub2:
        if st.button("📥 Download PDF", key="sub_down_btn"):
            st.session_state.book_sub_action = "download"
    with sub3:
        if st.button("✏️ Edit Text / Lesson", key="sub_edit_btn"):
            st.session_state.book_sub_action = "edit"
        
    st.write("---")
    
    # Sub Actions Functional Views
    if st.session_state.book_sub_action == "upload":
        st.markdown("<h4 style='color: #ffd700;'>📤 نئی بک اپلوڈ کریں (Upload PDF)</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("پی ڈی ایف فائل کا انتخاب کریں:", type=["pdf"])
        
        if uploaded_file is not None:
            st.success(f"فائل '{uploaded_file.name}' کامیابی سے اپلوڈ ہو گئی ہے!")
            st.markdown("<h4 style='color: #00f2fe; margin-top: 15px;'>📖 آپ کی اپلوڈ کردہ پی ڈی ایف (PDF Viewer):</h4>", unsafe_allow_html=True)
            # Read bytes & render PDF
            bytes_data = uploaded_file.getvalue()
            display_pdf(bytes_data)

    elif st.session_state.book_sub_action == "download":
        st.markdown("<h4 style='color: #ffd700;'>📥 کتابیں ڈاؤنلوڈ کریں (Download PDF)</h4>", unsafe_allow_html=True)
        st.write("دستیاب کتابوں کی فہرست:")
        st.download_button(
            label="📄 EPS Topik Book 1 (Urdu Version) ڈاؤنلوڈ کریں",
            data=b"Sample PDF Content",
            file_name="EPS_Topik_Book_1.pdf",
            mime="application/pdf"
        )

    elif st.session_state.book_sub_action == "edit":
        st.markdown("<h4 style='color: #ffd700;'>✏️ سبق میں ترمیم کریں (Edit Text / Lesson)</h4>", unsafe_allow_html=True)
        lesson_num = st.selectbox("سبق کا نمبر منتخب کریں:", [f"Lesson {i}" for i in range(1, 61)])
        edited_text = st.text_area(f"{lesson_num} کے مواد میں ترمیم کریں:", height=150)
        if st.button("تبدیلیاں محفوظ کریں (Save Changes)"):
            st.success(f"{lesson_num} کی معلومات محفوظ کر لی گئی ہیں!")
            
    else:
        st.info("اوپر دیے گئے بٹنوں (Upload, Download, Edit) پر کلک کر کے سبق اپلوڈ یا دیکھیں۔")

# 2. READING SECTION
elif st.session_state.active_tab == "Reading":
    st.markdown('<h3 style="color: #00f2fe;">📖 Reading Section</h3>', unsafe_allow_html=True)
    st.write("ریڈنگ پریکٹس مٹیریل:")
    st.markdown("> **سوال 1:** 다음 그림을 보고 맞는 단어나 문장을 고르십시오.")
    st.radio("صحیح جواب منتخب کریں:", ["1. 가방", "2. 안경", "3. 모자", "4. 구두"])

# 3. LISTENING SECTION
elif st.session_state.active_tab == "Listening":
    st.markdown('<h3 style="color: #00f2fe;">🎧 Listening Section</h3>', unsafe_allow_html=True)
    st.write("آڈیو سنیں اور جواب دیں:")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 4. GRAMMAR SECTION
elif st.session_state.active_tab == "Grammar":
    st.markdown('<h3 style="color: #00f2fe;">📘 Korean Grammar Rules</h3>', unsafe_allow_html=True)
    st.markdown("""
    * **입니다 / 입니까?:** اسم (Noun) کے ساتھ 'ہے' یا 'کیا ہے؟' کے لیے استعمال ہوتا ہے۔
    * **은 / 는:** جملے کے مرکزی موضوع (Topic Marker) کی نشاندہی کرتا ہے۔
    * **이 / 가:** سبجیکٹ مارکر (Subject Marker) ہے۔
    """)

# 5. PRACTICE QUIZ SECTION
elif st.session_state.active_tab == "Practice Quiz":
    st.markdown('<h3 style="color: #00f2fe;">📝 Practice Quiz Settings</h3>', unsafe_allow_html=True)
    
    col_q, col_t = st.columns(2)
    with col_q:
        num_questions = st.number_input("سوالات کی تعداد (Number of Questions):", min_value=1, max_value=100, value=20)
    with col_t:
        time_per_q = st.number_input("ہر سوال کے لیے وقت (سیکنڈز میں):", min_value=5, max_value=300, value=30)
        
    st.write("<br>", unsafe_allow_html=True)
    if st.button("🚀 Start Custom Quiz", key="start_quiz_btn"):
        st.success(f"ٹیسٹ شروع ہو گیا! کل سوالات: {num_questions} | ٹائمر: {time_per_q} سیکنڈز فی سوال۔")

# 6. CHATBOT SECTION
elif st.session_state.active_tab == "Chatbot":
    st.markdown('<h3 style="color: #00f2fe;">🤖 EPS-TOPIK Korean Assistant</h3>', unsafe_allow_html=True)
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("کورین زبان، گرامر یا الفاظ سے متعلق سوال لکھیں..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        response = f"آپ نے پوچھا: '{user_input}'۔ EPS-TOPIK اسسٹنٹ آپ کی مکمل رہنمائی کے لیے فعال ہے!"
        
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

# 7. TRANSLATION SECTION
elif st.session_state.active_tab == "Translation":
    st.markdown('<h3 style="color: #00f2fe;">🌐 Instant Korean Translator</h3>', unsafe_allow_html=True)
    source_text = st.text_area("ترجمہ کرنے کے لیے اردو یا انگریزی متن درج کریں:", height=100)
    if st.button("Translate Text", key="trans_action_btn"):
        if source_text:
            st.info(f"**ترجمہ (Korean):** 안녕하세요, '{source_text}' 에 대한 번역입니다.")

# 8. SKILL TEST SECTION
elif st.session_state.active_tab == "Skill Test":
    st.markdown('<h3 style="color: #00f2fe;">🛠️ Skill Test Preparation</h3>', unsafe_allow_html=True)
    st.write("اسکل ٹیسٹ کے بنیادی مرحلے:")
    st.checkbox("1. 핀뽑기 (Pin Selection Test)")
    st.checkbox("2. 나사 조이기 (Bolt & Nut Assembly)")
    st.checkbox("3. 체력 검사 (Physical Fitness Test)")

# 9. VOCABULARY SECTION
elif st.session_state.active_tab == "Vocabulary":
    st.markdown('<h3 style="color: #00f2fe;">🔤 Vocabulary List</h3>', unsafe_allow_html=True)
    
    vocab_html = """
    <table class="styled-table">
        <thead>
            <tr>
                <th>Words (Korean)</th>
                <th>Meaning in Urdu</th>
                <th>Meaning in English</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>안녕하세요</td>
                <td>سلام / آپ کیسے ہیں؟</td>
                <td>Hello / How are you?</td>
            </tr>
            <tr>
                <td>감사합니다</td>
                <td>شکریہ</td>
                <td>Thank you</td>
            </tr>
            <tr>
                <td>선생님</td>
                <td>استاد</td>
                <td>Teacher</td>
            </tr>
            <tr>
                <td>학생</td>
                <td>طالب علم</td>
                <td>Student</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(vocab_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)