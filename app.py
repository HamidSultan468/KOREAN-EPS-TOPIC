import streamlit as st
import time

# پیج سیٹنگز
st.set_page_config(page_title="EPS-TOPIK Korean Master", page_icon="🇰🇷", layout="centered")

# CSS ڈیزائننگ
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; color: #38bdf8; text-align: center; font-weight: bold; margin-bottom: 20px; }
    .sub-card { background-color: #0d1117; padding: 20px; border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Session States
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# ٹیسٹ ڈیٹا بیس (4 آپشنز)
listening_questions = [
    {
        "audio": "https://www.w3schools.com/html/horse.mp3",
        "options": ["1. 의사 (ڈاکٹر)", "2. 학생 (طالب علم)", "3. 경찰관 (پولیس)", "4. 요리사 (شیف)"],
        "correct": "2. 학생 (طالب علم)"
    },
    {
        "audio": "https://www.w3schools.com/html/horse.mp3",
        "options": ["1. 선생님 (استاد)", "2. 회사원 (ملازم)", "3. 의사 (ڈاکٹر)", "4. 학생 (طالب علم)"],
        "correct": "1. 선생님 (استاد)"
    }
]

reading_questions = [
    {
        "question": "다음 단어와 관계있는 것은 무엇입니까? [ 사과 , 바나나 , 수박 ]",
        "options": ["1. 과일 (پھل)", "2. 가구 (فرنیچر)", "3. 옷 (کپڑے)", "4. 직업 (پیشہ)"],
        "correct": "1. 과일 (پھل)"
    },
    {
        "question": "다음 반대되는 단어를 고르십시오. [ 크다 (بڑا ہونا) ]",
        "options": ["1. 많다 (زیادہ)", "2. 작다 (چھوٹا)", "3. 길다 (لمبا)", "4. 무겁다 (بھاری)"],
        "correct": "2. 작다 (چھوٹا)"
    }
]

# سائڈبار نیویگیشن
st.sidebar.title("📌 Main Menu")
menu = st.sidebar.radio("کوئی ایک ماڈیول منتخب کریں:", ["Home", "Textbooks", "Listening Test", "Reading Test", "Vocabulary"])

st.markdown('<div class="main-header">🇰🇷 EPS-TOPIK Learning Platform</div>', unsafe_allow_html=True)

# ------------------- TEXTBOOKS MODULE -------------------
if menu == "Textbooks":
    st.header("📚 EPS-TOPIK Official Textbooks")
    st.write("نصابی کتاب کے تمام بنیادی فیچرز اور فائلز نیچے سے حاصل کریں:")

    # ذیلی بٹنز (Tabs)
    tab_read, tab_listen, tab_down, tab_up = st.tabs([
        "📖 Reading Material", 
        "🎧 Listening Audio", 
        "⬇️ Download Books", 
        "📤 Upload Custom Files"
    ])

    with tab_read:
        st.subheader("📖 Read Textbooks Online")
        st.info("کتاب 1 یا کتاب 2 کا مطالعہ یہاں سے کریں۔")
        book_sel = st.selectbox("کتاب منتخب کریں:", ["Book 1 (Lesson 1-30)", "Book 2 (Lesson 31-60)"])
        st.write(f"آپ اس وقت **{book_sel}** کھولی ہوئی ہے۔")
        st.text_area("کتاب کا اہم پیراگراف یا سبق درج کریں:", "안녕하세요. 저는 پاکستان 사람입니다.", height=100)

    with tab_listen:
        st.subheader("🎧 Textbook Audio Tracks")
        st.write("سبق کے مطابق آڈیو سنیں:")
        track = st.selectbox("ٹریک نمبر منتخب کریں:", [f"Track {i}" for i in range(1, 11)])
        st.audio("https://www.w3schools.com/html/horse.mp3")

    with tab_down:
        st.subheader("⬇️ Download PDF Textbooks")
        st.write("سرکاری پی ڈی ایف بکس ڈاؤن لوڈ کریں:")
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📖 Download Book 1 PDF", data="Book 1 Content Placeholder", file_name="EPS_Book_1.pdf")
        with col2:
            st.download_button("📖 Download Book 2 PDF", data="Book 2 Content Placeholder", file_name="EPS_Book_2.pdf")

    with tab_up:
        st.subheader("📤 Upload Custom Materials")
        st.write("اپنی نوٹس یا آڈیو فائلز ہوسٹ/اپلوڈ کریں:")
        uploaded_file = st.file_uploader("فائل منتخب کریں (PDF, MP3, PNG):", type=["pdf", "mp3", "png", "jpg"])
        if uploaded_file is not None:
            st.success(f"فائل '{uploaded_file.name}' کامیابی سے اپلوڈ ہو گئی۔")

# ------------------- TEST MODULE (LISTENING & READING) -------------------
elif menu in ["Listening Test", "Reading Test"]:
    st.header(f"📝 EPS-TOPIK {menu}")
    
    if not st.session_state.quiz_started:
        st.markdown('<div class="sub-card">', unsafe_allow_html=True)
        st.subheader("⚙️ Test Settings (انسٹرکٹر سیٹ اپ)")
        
        # مینوئل ٹائم ان پٹ (1 سے 600 سیکنڈ)
        timer_setting = st.number_input("فی سوال مینوئل وقت درج کریں (سیکنڈز):", min_value=1, max_value=600, value=30)
        
        if st.button("🚀 ٹیسٹ شروع کریں"):
            st.session_state.quiz_started = True
            st.session_state.test_timer = timer_setting
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        questions = listening_questions if menu == "Listening Test" else reading_questions
        q_idx = st.session_state.current_q

        if q_idx < len(questions):
            q = questions[q_idx]
            st.subheader(f"سوال {q_idx + 1} / {len(questions)}")
            st.caption(f"⏱️ اس سوال کے لیے وقت: {st.session_state.test_timer} سیکنڈز")

            if "audio" in q:
                st.audio(q["audio"])
            else:
                st.write(f"### {q['question']}")

            # 4 آپشنز
            user_choice = st.radio("درست جواب پر ٹک کریں:", q["options"], index=None, key=f"q_{q_idx}_{menu}")

            if st.button("Submit Answer / اگلا سوال"):
                if user_choice:
                    if user_choice == q["correct"]:
                        st.success("✔ درست جواب!")
                        st.session_state.score += 1
                    else:
                        st.error(f"✖ غلط جواب! درست جواب تھا: {q['correct']}")
                    time.sleep(1.5)
                    st.session_state.current_q += 1
                    st.rerun()
                else:
                    st.warning("براہ کرم کسی ایک آپشن پر ٹک کریں!")

        else:
            # Automatic Final Result Screen
            st.balloons()
            st.header("📊 آٹومیٹک رزلٹ کارڈ")
            total = len(questions)
            percentage = round((st.session_state.score / total) * 100)

            st.metric(label="حاصل کردہ نمبر (Score)", value=f"{percentage}%")
            st.write(f"کل سوالات: **{total}** | درست جوابات: **{st.session_state.score}** | غلط / وقت ختم: **{total - st.session_state.score}**")

            if st.button("🔄 دوبارہ ٹیسٹ شروع کریں"):
                st.session_state.quiz_started = False
                st.rerun()

# ------------------- OTHER MODULES -------------------
elif menu == "Vocabulary":
    st.header("🔤 Korean Vocabulary")
    st.write("1. 안녕하세요 - سلام")
    st.write("2. 감사합니다 - شکریہ")

else:
    st.header("Welcome!")
    st.write("سائڈبار سے اپنی پسند کا سیکشن منتخب کریں۔")