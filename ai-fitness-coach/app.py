import streamlit as st

from services.ai_service import analyze_fitness
from components.progress_dashboard import show_progress_dashboard
from components.nutrition import calculate_calories
from components.workout import generate_workout
from components.progress import show_progress_chart
from components.ai_progress_coach import ai_progress_coach
from components.macros import calculate_macros
from components.water import calculate_water
from components.sleep import sleep_recommendation
from components.image_compare import show_image_comparison

from components.auth import login_section
from components.progress_storage import save_progress_entry
from components.vision import vision_analysis
from components.macro_tracker import macro_tracker
from components.videos import show_workout_video
from components.chatbot import chatbot_coach


# PAGE CONFIG
st.set_page_config(
    page_title="AI Fitness Coach",
    layout="wide"
)


# LOGIN
login_section()

if not st.session_state.logged_in:
    st.warning("Bitte einloggen")
    st.stop()


# TITLE
st.title("💪 AI Fitness Coach")

st.markdown(
    f"## Willkommen {st.session_state.username}"
)

st.markdown(
    "### Deine persönliche Fitness Analyse"
)


# LAYOUT
col1, col2 = st.columns(2)


# LEFT SIDE
with col1:

    age = st.number_input(
        "Alter",
        16,
        100,
        25
    )

    weight = st.number_input(
        "Gewicht (kg)",
        40,
        200,
        80
    )

    height = st.number_input(
        "Größe (cm)",
        140,
        220,
        180
    )

    goal = st.selectbox(
        "Ziel",
        [
            "Muskelaufbau",
            "Fett verlieren",
            "Body Recomp"
        ]
    )


# RIGHT SIDE
with col2:

    image = st.file_uploader(
        "📸 Körperbild hochladen",
        type=["png", "jpg", "jpeg"]
    )

    if image:

        st.image(
            image,
            caption="Hochgeladenes Bild",
            use_container_width=True
        )

    before_image = st.file_uploader(
        "Vorher Bild",
        type=["png", "jpg", "jpeg"]
    )

    after_image = st.file_uploader(
        "Nachher Bild",
        type=["png", "jpg", "jpeg"]
    )


# SESSION STATES
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = ""

if "vision_result" not in st.session_state:
    st.session_state.vision_result = ""

if "calories" not in st.session_state:
    st.session_state.calories = 0

if "macros" not in st.session_state:
    st.session_state.macros = {}

if "water" not in st.session_state:
    st.session_state.water = 0

if "sleep" not in st.session_state:
    st.session_state.sleep = ""

if "workout" not in st.session_state:
    st.session_state.workout = ""


# BUTTON
if st.button("🚀 Analyse starten"):

    st.session_state.analysis_done = True

    # AI ANALYSE
    st.session_state.analysis_result = analyze_fitness(
        age,
        weight,
        height,
        goal
    )

    # VISION ANALYSE
    st.session_state.vision_result = vision_analysis()

    # KALORIEN
    st.session_state.calories = calculate_calories(
        weight,
        height,
        age,
        goal
    )

    # MAKROS
    st.session_state.macros = calculate_macros(
        st.session_state.calories,
        goal
    )

    # WASSER
    st.session_state.water = calculate_water(weight)

    # SCHLAF
    st.session_state.sleep = sleep_recommendation(goal)

    # WORKOUT
    st.session_state.workout = generate_workout(goal)

    # SAVE PROGRESS
    save_progress_entry(
    st.session_state.username,
    weight,
    st.session_state.calories
)


# DAUERHAFTE AUSGABE
if st.session_state.analysis_done:

    # ANALYSE
    st.markdown("# 🧠 Analyse")

    st.write(
        st.session_state.analysis_result
    )


    # VISION
    st.markdown("# 📸 Vision Analyse")

    st.write(
        st.session_state.vision_result
    )


    # ERNÄHRUNG
    st.markdown("# 🍽 Ernährung")

    st.success(
        f"Empfohlene Kalorien: {st.session_state.calories} kcal"
    )


    # MAKROS
    st.markdown("# 🍗 Makros")

    st.write(
        st.session_state.macros
    )


    # MAKRO TRACKER
    macro_tracker()


    # WASSER
    st.markdown("# 💧 Wasser")

    st.success(
        f"Empfohlene Wassermenge: {st.session_state.water} Liter"
    )


    # SCHLAF
    st.markdown("# 💤 Schlaf")

    st.info(
        st.session_state.sleep
    )


    # WORKOUT
    st.markdown("# 💪 Workout Plan")

    st.write(
        st.session_state.workout
    )


    # CHART
    st.markdown("# 📈 Fortschritt")

    show_progress_chart(weight)


    # BILD VERGLEICH
    if before_image and after_image:

        st.markdown("# 📸 Vorher / Nachher")

        show_image_comparison(
            before_image,
            after_image
        )


    # VIDEO
    show_workout_video()


    # CHATBOT
    chatbot_coach()
st.markdown("---")

show_progress_dashboard(st.session_state.username)
st.markdown("---")

st.markdown("## 🧠 AI Progress Coach")

if st.session_state.analysis_done:

    coach_result = ai_progress_coach(st.session_state.username)

    st.write(coach_result)
