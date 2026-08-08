import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="KR KOREAN EPS-TOPIK PRO",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STRICT CSS FOR EXACT EQUAL BUTTONS & GRID ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600;700&display=swap');

    /* Global Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #150a21 0%, #050508 100%) !important;
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Vibrant Gold Title */
    .golden-title {
        font-family: 'Orbitron', sans-serif;
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
        font-family: 'Orbitron', sans-serif;
        font-size: 0.95rem;
        letter-spacing: 2px;
        margin-bottom: 25px;
        text-shadow: 0 0 12px rgba(0, 242, 254, 0.8);
    }

    /* Keyframes for Soft RGB Animated Glow */
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

    /* Target ALL Streamlit Buttons to Force EXACT GRID SIZING */
    div[data-testid="column"] {
        padding: 0px 4px !important; /* کالمز کے بیچ برابر فاصلہ */
    }

    div.stButton {
        width: 100% !important;
    }

    div.stButton > button {
        width: 100% !important;
        height: 55px !important;                  /* بالکل فکسڈ اونچائی */
        background: rgba(10, 15, 30, 0.85) !important;
        border-radius: 30px !important;             /* اوول / کیپسول شیپ */
        border: 2px solid #00f2fe !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 0.78rem !important;             /* یکساں فاؤنٹ سائز */
        font-weight: 700 !important;
        text-align: center !important;
        animation: rgbGlow 6s infinite ease-in-out !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 2px 5px !important;
        box-sizing: border-box !important;
    }

    div.stButton > button:hover {
        transform: scale(1.04) translateY(-2px) !important;
        background: rgba(20, 30, 55, 0.95) !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.8) !important;
    }

    /* Content Box */
    .neon-container {
        background: rgba(10, 14, 23, 0.8);
        border: 1.5px solid #00f2fe;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        margin-top: 25px;
    }

    /* Clean Styled Table for Vocabulary */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 1rem;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.15);
    }
    .styled-table thead tr {
        background-color: #00f2fe;
        color: #050508;
        text-align: left;
        font-weight: bold;
        font-family: 'Orbitron', sans-serif;
    }
    .styled-table th, .styled-table td {
        padding: 12px 15px;
        border-bottom: 1px solid rgba(0, 242, 254, 0.2);
    }
    .styled-table tbody tr {
        background-color: rgba(15, 23, 42, 0.6);
    }
    .styled-table tbody tr:hover {
        background-color: rgba(0, 242, 254, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="golden-title">KR KOREAN EPS-TOPIK PRO</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Next-Gen Language Learning Hub</div>', unsafe_allow_html=True)

# Active State Tracker
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "EPS Topik Books"

# --- LINE 1: EXACT EQUAL 5 COLUMNS ---
c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
with c1:
    if st.button("EPS Topik Books", key="btn1"): st.session_state.active_tab = "EPS Topik Books"
with c2:
    if st.button("Reading", key="btn2"): st.session_state.active_tab = "Reading"
with c3:
    if st.button("Listening", key="btn3"): st.session_state.active_tab = "Listening"
with c4:
    if st.button("Grammar", key="btn4"): st.session_state.active_tab = "Grammar"
with c5:
    if st.button("Practice Quiz", key="btn5"): st.session_state.active_tab = "Practice Quiz"

st.markdown("<div style='margin-top: 8px;'></div>", unsafe_allow_html=True)

# --- LINE 2: EXACT EQUAL 5 COLUMNS ---
c6, c7, c8, c9, c10 = st.columns([1, 1, 1, 1, 1])
with c6:
    if st.button("Chatbot", key="btn6"): st.session_state.active_tab = "Chatbot"
with c7:
    if st.button("Translation", key="btn7"): st.session_state.active_tab = "Translation"
with c8:
    if st.button("Skill Test", key="btn8"): st.session_state.active_tab = "Skill Test"
with c9:
    if st.button("Vocabulary", key="btn9"): st.session_state.active_tab = "Vocabulary"
with c10:
    st.button("Empty 10", key="btn10", disabled=True)

# --- DYNAMIC CONTENT AREA ---
st.markdown('<div class="neon-container">', unsafe_allow_html=True)

# 1. EPS TOPIK BOOKS SECTION
if st.session_state.active_tab == "EPS Topik Books":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📚 EPS Topik Books Manager</h3>', unsafe_allow_html=True)
    
    sub1, sub2, sub3 = st.columns([1, 1, 1])
    with sub1:
        st.button("📤 Upload PDF", key="sub_up")
    with sub2:
        st.button("📥 Download PDF", key="sub_down")
    with sub3:
        st.button("✏️ Edit Text / Lesson", key="sub_edit")
        
    st.write("---")
    st.info("یہاں آپ اپنی تمام پی ڈی ایف بکس اور اسباق کا انتظام کر سکتے ہیں۔")

# 2. READING SECTION
elif st.session_state.active_tab == "Reading":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📖 Reading Section</h3>', unsafe_allow_html=True)
    st.write("ریڈنگ مٹیریل اور پیراگراف یہاں ظاہر ہوں گے۔")

# 3. LISTENING SECTION
elif st.session_state.active_tab == "Listening":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🎧 Listening Section</h3>', unsafe_allow_html=True)
    st.write("آڈیو ٹریکس اور لسولنگ پریکٹس یہاں سے ہوگی۔")

# 4. GRAMMAR SECTION
elif st.session_state.active_tab == "Grammar":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📘 Grammar Center</h3>', unsafe_allow_html=True)
    st.write("کورین گرامر کے تمام قوانین اور تفصیلی وضاحتیں یہاں موجود ہیں۔")

# 5. PRACTICE QUIZ SECTION
elif st.session_state.active_tab == "Practice Quiz":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">📝 Practice Quiz Settings</h3>', unsafe_allow_html=True)
    
    col_q, col_t = st.columns(2)
    with col_q:
        num_questions = st.number_input("سوالات کی تعداد (Number of Questions):", min_value=1, max_value=100, value=20)
    with col_t:
        time_per_q = st.number_input("ہر سوال کے لیے وقت (سیکنڈز میں):", min_value=5, max_value=300, value=30)
        
    st.write("<br>", unsafe_allow_html=True)
    if st.button("🚀 Start Custom Quiz", key="start_q"):
        st.success(f"ٹیسٹ شروع ہو رہا ہے: {num_questions} سوالات | فی سوال {time_per_q} سیکنڈ کا ٹائمر!")

# 6. CHATBOT SECTION
elif st.session_state.active_tab == "Chatbot":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🤖 AI Korean Chatbot</h3>', unsafe_allow_html=True)
    st.write("کورین زبان کی رہنمائی کے لیے اپنے سوالات پوچھیں۔")

# 7. TRANSLATION SECTION
elif st.session_state.active_tab == "Translation":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🌐 Translation Tool</h3>', unsafe_allow_html=True)
    st.text_area("متن درج کریں...", height=120)
    st.button("Translate Text", key="trans_btn")

# 8. SKILL TEST SECTION
elif st.session_state.active_tab == "Skill Test":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🛠️ Skill Test Module</h3>', unsafe_allow_html=True)
    st.write("اسکل ٹیسٹ کی تیاری کے لیے مواد اور ویڈیوز۔")

# 9. VOCABULARY SECTION
elif st.session_state.active_tab == "Vocabulary":
    st.markdown('<h3 style="color: #00f2fe; font-family: Orbitron;">🔤 Vocabulary Table</h3>', unsafe_allow_html=True)
    
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