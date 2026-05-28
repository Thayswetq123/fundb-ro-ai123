import streamlit as st

from services.ai_service import analyze_fitness

from components.progress_dashboard import show_progress_dashboard
from components.ai_progress_coach import ai_progress_coach
from components.adaptive_coach import adaptive_training_plan
from components.vision import vision_analysis
from components.chatbot import chatbot_coach
from components.macro_tracker import macro_tracker


st.set_page_config(
    page_title="AI Fitness Coach",
    layout="wide"
)


# =========================
# 🔐 LOGIN
# =========================
from components.auth import login_section

login_section()

if not st.session_state.logged_in:
    st.stop()


# =========================
# 🧭 SIDEBAR NAVIGATION
# =========================

st.sidebar.title("💪 Navigation")

page = st.sidebar.radio(
    "Menü",
    [
        "📊 Dashboard",
        "🧠 AI Coach",
        "📸 Vision",
        "🤖 Chatbot"
    ]
)


st.sidebar.markdown("---")
st.sidebar.write(f"👤 {st.session_state.username}")


# =========================
# 📊 DASHBOARD
# =========================

if page == "📊 Dashboard":

    st.title("📊 Dein Dashboard")

    show_progress_dashboard(st.session_state.username)

    st.markdown("---")

    adaptive_training_plan(
        st.session_state.username,
        "Muskelaufbau"
    )


# =========================
# 🧠 AI COACH
# =========================

elif page == "🧠 AI Coach":

    st.title("🧠 AI Personal Coach")

    age = st.number_input("Alter", 16, 100, 25)
    weight = st.number_input("Gewicht", 40, 200, 80)
    height = st.number_input("Größe", 140, 220, 180)

    goal = st.selectbox(
        "Ziel",
        ["Muskelaufbau", "Fett verlieren", "Body Recomp"]
    )

    if st.button("🚀 Analyse starten"):

        result = analyze_fitness(age, weight, height, goal)

        st.markdown("## 🧠 Ergebnis")
        st.write(result)


# =========================
# 📸 VISION
# =========================

elif page == "📸 Vision":

    st.title("📸 Körperanalyse")

    image = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg"])

    if image:

        result = vision_analysis(
            "Muskelaufbau",
            80,
            180
        )

        st.markdown("## 🧠 Analyse")
        st.write(result)


# =========================
# 🤖 CHATBOT
# =========================

elif page == "🤖 Chatbot":

    st.title("🤖 AI Chat Coach")

    chatbot_coach()
