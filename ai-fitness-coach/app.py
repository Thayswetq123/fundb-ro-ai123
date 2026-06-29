import streamlit as st

from services.ai_service import analyze_fitness

from components.progress_dashboard import show_progress_dashboard
from components.ai_progress_coach import ai_progress_coach
from components.adaptive_coach import adaptive_training_plan
from components.vision import vision_analysis
from components.chatbot import chatbot_coach
from components.auth import login_section


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Fitness Coach",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# 🎨 LEVEL 4 UI DESIGN
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #111827, #0b0f19);
    color: white;
    font-family: 'Inter', sans-serif;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1f2937;
}

/* BUTTONS */
div.stButton > button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    padding: 12px 18px;
    border: none;
    font-weight: 600;
}

div.stButton > button:hover {
    transform: scale(1.02);
    opacity: 0.9;
}

/* CARDS */
.card {
    background: rgba(17, 24, 39, 0.7);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 12px;
}

/* METRICS */
[data-testid="stMetric"] {
    background-color: rgba(17, 24, 39, 0.7);
    padding: 16px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* HEADINGS */
h1, h2, h3 {
    color: #f9fafb;
    letter-spacing: -0.5px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# 🔐 LOGIN
# =========================
login_section()

if not st.session_state.logged_in:
    st.stop()


# =========================
# 🧭 SIDEBAR NAVIGATION
# =========================
st.sidebar.title("💪 AI Fitness")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "🧠 Coach", "📸 Vision", "🤖 Chat"]
)

st.sidebar.markdown("---")

st.sidebar.success(f"👤 {st.session_state.username}")


# =========================
# 📊 DASHBOARD
# =========================
if page == "📊 Dashboard":

    st.markdown("""
    <div class="card">
        <h2>🔥 Welcome back</h2>
        <p>Dein AI Coach analysiert deinen Fortschritt in Echtzeit</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔥 Form", "Strong", "+2%")

    with col2:
        st.metric("📈 Progress", "Good", "+1.2kg")

    with col3:
        st.metric("⚡ Streak", "5 days", "+1")

    st.markdown("---")

    show_progress_dashboard(st.session_state.username)

    st.markdown("---")

    st.markdown("## 🧠 AI Coach Feedback")

    st.info(
        ai_progress_coach(st.session_state.username)
    )

    st.markdown("## 🔥 Adaptiver Trainingsplan")

    st.write(
        adaptive_training_plan(
            st.session_state.username,
            "Muskelaufbau"
        )
    )


# =========================
# 🧠 COACH
# =========================
elif page == "🧠 Coach":

    st.title("🧠 AI Coach")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Alter", 16, 100, 25)

    with col2:
        weight = st.number_input("Gewicht", 40, 200, 80)

    with col3:
        height = st.number_input("Größe", 140, 220, 180)

    goal = st.selectbox(
        "Ziel",
        ["Muskelaufbau", "Fett verlieren", "Body Recomp"]
    )

    if st.button("🚀 Analyse starten"):

        with st.spinner("AI denkt nach... 🧠"):

            result = analyze_fitness(age, weight, height, goal)

        st.markdown("## 🧠 Ergebnis")

        st.markdown(f"""
        <div class="card">
        {result}
        </div>
        """, unsafe_allow_html=True)


# =========================
# 📸 VISION
# =========================
elif page == "📸 Vision":

    st.title("📸 Körperanalyse")

    image = st.file_uploader(
        "Bild hochladen",
        type=["png", "jpg", "jpeg"]
    )

    if image:

        with st.spinner("Analysiere Körper..."):

            result = vision_analysis(
                "Muskelaufbau",
                80,
                180
            )

        st.markdown("## 🧠 Ergebnis")

        st.markdown(f"""
        <div class="card">
        {result}
        </div>
        """, unsafe_allow_html=True)


# =========================
# 🤖 CHAT
# =========================
elif page == "🤖 Chat":

    st.title("🤖 AI Chat Coach")

    chatbot_coach()
