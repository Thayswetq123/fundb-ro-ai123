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
# 🎨 LEVEL 5 UI DESIGN
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
    width: 100%;
    height: 55px;
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
    background: rgba(17,24,39,0.9);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}

/* HEADINGS */
h1, h2, h3 {
    color: #f9fafb;
    letter-spacing: -0.5px;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
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
    <div style="
    padding:35px;
    border-radius:25px;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    margin-bottom:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.3);
    ">
    <h1 style="color:white;margin:0;">
    💪 Willkommen zurück
    </h1>

    <p style="
    color:white;
    font-size:18px;
    margin-top:10px;
    ">
    Verfolge deinen Fortschritt, verbessere dein Training
    und erreiche deine Ziele mit KI.
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "⚖️ Gewicht",
            "80 kg",
            "-1.2 kg"
        )

    with col2:
        st.metric(
            "🔥 Kalorien",
            "2400",
            "-200"
        )

    with col3:
        st.metric(
            "💪 Workouts",
            "18",
            "+3"
        )

    with col4:
        st.metric(
            "⚡ Streak",
            "7 Tage",
            "+1"
        )

    st.markdown("## 🚀 Schnellzugriffe")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "📸 Neue Analyse",
            use_container_width=True
        )

    with c2:
        st.button(
            "💪 Trainingsplan",
            use_container_width=True
        )

    with c3:
        st.button(
            "🍽 Ernährung",
            use_container_width=True
        )

    st.markdown("---")

    st.markdown("""
    ## 📈 Fortschritt

    Verfolge deine Entwicklung über Zeit.
    """)

    show_progress_dashboard(
        st.session_state.username
    )

    st.markdown("---")

    coach_text = ai_progress_coach(
        st.session_state.username
    )

    st.markdown(f"""
    <div style="
    padding:20px;
    border-radius:18px;
    background:#111827;
    border:1px solid #374151;
    margin-top:20px;
    margin-bottom:20px;
    ">
    <h3>🧠 AI Coach Feedback</h3>
    <p>{coach_text}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🔥 Adaptiver Trainingsplan")

    plan = adaptive_training_plan(
        st.session_state.username,
        "Muskelaufbau"
    )

    st.markdown(f"""
    <div style="
    padding:20px;
    border-radius:18px;
    background:#111827;
    border:1px solid #374151;
    ">
    {plan}
    </div>
    """, unsafe_allow_html=True)


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

            result = analyze_fitness(
                age,
                weight,
                height,
                goal
            )

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
