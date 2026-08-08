import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Next-Gen Korean EPS-TOPIK Hub",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CUSTOM CSS FOR UI ---
st.markdown("""
<style>
    /* Global Dark Theme Background */
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid rgba(56, 189, 248, 0.2);
    }
    
    /* Neon Header Cards */
    .header-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid rgba(56, 189, 248, 0.4);
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }
    
    /* Custom Neon Buttons */
    .stButton > button {
        background-color: #0d1117 !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px !important;
        padding: 8px 18px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #38bdf8 !important;
        color: #0d1117 !important;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.6) !important;
    }
    
    /* Sub-tabs Box */
    .sub-box {
        background-color: #161b22;
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 10px;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- JS INJECTION ---
try:
    with open("script.js", "r", encoding="utf-8") as f:
        js_code = f.read()
    components.html(f"<script>{js_code}</script>", height=0)
except Exception as e:
    pass

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🌐 Learning Hub")
menu = st.sidebar.radio(
    "نیویگیشن منتخب کریں:",
    ["📚 Textbooks", "🔤 Vocabulary", "📖 Grammar", "🎧 Listening Test", "📝 Reading Test", "🤖 AI Chatbot"]
)

# --- MAIN CONTENT LAYOUT ---
st.markdown('<div class="header-card"><h1 style="color: #38bdf8; margin:0;">🚀 Next-Gen Language Learning Hub</h1><p style="color: #94a3b8; margin-top: 5px;">EPS-TOPIK Official Korean Learning Platform</p></div>', unsafe_allow_html=True)

# 1. TEXTBOOKS MODULE
if menu == "📚 Textbooks":
    st.markdown("""
    <div class="sub-box">
        <h2 style="color: #38bdf8;">📗 EPS-TOPIK Official Textbooks</h2>
        <p style="color: #cbd5e1;">سرکاری نصابی بکس ڈاؤن لوڈ کریں یا آن لائن مطالعہ کریں:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("📖 Read Online")
    with col2:
        st.button("🎧 Listening Tracks")
    with col3:
        st.button("⬇️ Download PDFs")
    with col4:
        st.button("📤 Upload Custom")
        
    st.markdown("---")
    st.markdown("### 📄 Quick Korean Paragraph Translator")
    ko_text = st.text_area("کتاب کا کوئی بھی کورین متن یا جملہ یہاں لکھیں/پیسٹ کریں...", height=100)
    if st.button("Translate / ترجمہ کریں"):
        if ko_text:
            st.info(f"ترجمہ: {ko_text} (Processing Translation...)")
        else:
            st.warning("براہِ کرم پہلے کوئی متن درج کریں۔")

# 2. VOCABULARY MODULE
elif menu == "🔤 Vocabulary":
    st.markdown("""
    <div class="sub-box">
        <h2 style="color: #38bdf8;">🔤 Korean Vocabulary Database</h2>
        <p style="color: #cbd5e1;">اہم کورین الفاظ اور ان کے اردو تراجم:</p>
    </div>
    """, unsafe_allow_html=True)
    
    vocab_data = [
        {"Korean": "안녕하세요", "Meaning": "سلام / آپ کیسے ہیں؟"},
        {"Korean": "감사합니다", "Meaning": "شکریہ"},
        {"Korean": "선생님", "Meaning": "استاد / ٹیچر"},
        {"Korean": "학생", "Meaning": "طالب علم"},
        {"Korean": "회사원", "Meaning": "دفتر کا ملازم"},
        {"Korean": "의사", "Meaning": "ڈاکٹر"},
    ]
    st.table(vocab_data)

# 3. GRAMMAR MODULE
elif menu == "📖 Grammar":
    st.markdown("""
    <div class="sub-box">
        <h2 style="color: #38bdf8;">📖 Essential Grammar Rules</h2>
        <p style="color: #cbd5e1;">بنیادی کورین گرامر کے اصول اور مثالیں:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    * **입니다 (Imnida):** یہ "ہے۔" کے لیے استعمال ہوتا ہے (Formal Present Tense)۔
    * **입니까? (Imnika?):** سوال پوچھنے کے لیے استعمال ہوتا ہے (Is/Are?)۔
    * **은 / 는 (Eun / Neun):** جملے کے بنیادی موضوع (Topic Marker) کی نشاندہی کرتا ہے۔
    """)

# 4. TESTS MODULES
elif menu in ["🎧 Listening Test", "📝 Reading Test"]:
    st.markdown(f"""
    <div class="sub-box">
        <h2 style="color: #38bdf8;">{menu} Setup</h2>
        <p style="color: #cbd5e1;">ٹیسٹ شروع کرنے کے لیے فی سوال وقت (سیکنڈز میں) درج کریں:</p>
    </div>
    """, unsafe_allow_html=True)
    
    timer_val = st.number_input("Time per Question (Seconds):", min_value=5, max_value=300, value=30)
    if st.button("🚀 Start Test"):
        st.success(f"{menu} شروع ہو رہا ہے! فی سوال وقت: {timer_val} سیکنڈز")

# 5. CHATBOT MODULE
elif menu == "🤖 AI Chatbot":
    st.markdown("""
    <div class="sub-box">
        <h2 style="color: #38bdf8;">🤖 EPS Korean AI Assistant</h2>
        <p style="color: #cbd5e1;">کورین زبان یا ٹیسٹ سے متعلق کوئی بھی سوال پوچھیں:</p>
    </div>
    """, unsafe_allow_html=True)
    
    user_msg = st.text_input("اپنا سوال ٹائپ کریں...")
    if st.button("پوچھیں"):
        if user_msg:
            st.write(f"**You:** {user_msg}")
            st.write("**AI:** کورین ٹیسٹ میں بہتر نتائج کے لیے روزانہ Vocabulary اور Grammar کی مشق کریں۔")