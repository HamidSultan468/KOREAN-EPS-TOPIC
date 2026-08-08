import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="KR Korean EPS-Topik Pro Portal",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling: Neon Glow, Glassmorphism & High-End UI
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Poppins:wght@400;600&display=swap');

    .stApp {
        background: radial-gradient(circle at top, #0f172a 0%, #020617 100%);
        color: #e2e8f0;
        font-family: 'Poppins', sans-serif;
    }

    /* Glass Effect Containers */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
    }

    /* Neon Buttons */
    div.stButton > button {
        width: 100%;
        background: rgba(15, 23, 42, 0.8) !important;
        color: #38bdf8 !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 40px !important;
        padding: 12px 25px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.3) !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #0f172a !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important;
        transform: translateY(-2px);
    }
    
    .stat-text {
        font-family: 'Orbitron', sans-serif;
        color: #f8fafc;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/south-korea.png", width=60)
    st.title("EPS-Topik Hub")
    st.caption("Korean Language Pro Portal")
    
    st.markdown("---")
    
    menu = st.radio(
        "Main Navigation",
        ["Home", "Textbooks", "Vocabulary", "Grammar", "Listening", "Online Quiz"],
        index=0
    )
    
    st.markdown("---")
    st.subheader("Support")
    if st.button("Rate Us"):
        st.toast("Thank you for your feedback!", icon="⭐")
    if st.button("Share Portal"):
        st.toast("Link copied!", icon="🔗")

# ---------------------------------------------------------
# Header Section
# ---------------------------------------------------------
st.markdown("""
<div style="text-align: center;">
    <h1 style="font-family: 'Orbitron', sans-serif; color: #f8fafc;">KR KOREAN EPS-TOPIK PRO</h1>
    <p style="color: #94a3b8;">Master the Korean language with our advanced interactive portal.</p>
</div>
""", unsafe_allow_html=True)

# Metrics
c1, c2, c3 = st.columns(3)
with c1: st.markdown('<div class="glass-card" style="text-align:center;"><div class="stat-text">12</div><p>Total Books</p></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="glass-card" style="text-align:center;"><div class="stat-text">1,500+</div><p>Vocabulary</p></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="glass-card" style="text-align:center;"><div class="stat-text">60+</div><p>Lessons</p></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Dynamic Content
# ---------------------------------------------------------
if menu == "Home":
    st.markdown('<div class="glass-card"><h3>Welcome to the Dashboard</h3><p>Select a category from the sidebar to start your learning journey.</p></div>', unsafe_allow_html=True)

elif menu == "Textbooks":
    st.markdown('<div class="glass-card"><h3>Official Textbooks</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("Download Book 1")
    with col2:
        st.button("Download Book 2")

elif menu == "Vocabulary":
    st.markdown('<div class="glass-card"><h3>Vocabulary Search</h3></div>', unsafe_allow_html=True)
    st.text_input("Enter word to search...", placeholder="e.g. Doctor")

elif menu == "Online Quiz":
    st.markdown('<div class="glass-card"><h3>Practice Quiz</h3></div>', unsafe_allow_html=True)
    ans = st.radio("What is the Korean word for 'Teacher'?", ["의사", "선생님", "회사원"], index=None)
    if st.button("Submit Answer"):
        if ans == "선생님":
            st.success("Correct!")
        else:
            st.error("Try again!")
