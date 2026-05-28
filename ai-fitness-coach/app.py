import streamlit as st

from services.ai_service import analyze_fitness

from components.nutrition import calculate_calories
from components.workout import generate_workout
from components.progress import show_progress_chart

from components.macros import calculate_macros
from components.water import calculate_water
from components.sleep import sleep_recommendation
from components.image_compare import show_image_comparison

from components.auth import login_section
from components.save_progress import save_progress
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


# ANALYSE BUTTON
if st.button("🚀 Analyse starten"):

    # AI ANALYSE
    result = analyze_fitness(
        age,
        weight,
        height,
        goal
    )

    st.markdown("# 🧠 Analyse")

    st.write(result)


    # VISION ANALYSE
    vision = vision_analysis()

    st.markdown("# 📸 Vision Analyse")

    st.write(vision)


    # ERNÄHRUNG
    st.markdown("# 🍽 Ernährung")

    calories = calculate_calories(
        weight,
        height,
        age,
        goal
    )

    st.success(
        f"Empfohlene Kalorien: {calories} kcal"
    )


    # FORTSCHRITT SPEICHERN
    save_progress(
        weight,
        calories
    )


    # MAKROS
    st.markdown("# 🍗 Makros")

    macros = calculate_macros(
        calories,
        goal
    )

    st.write(macros)


    # MAKRO TRACKER
    macro_tracker()


    # WASSER
    water = calculate_water(weight)

    st.markdown("# 💧 Wasser")

    st.success(
        f"Empfohlene Wassermenge: {water} Liter"
    )


    # SCHLAF
    sleep = sleep_recommendation(goal)

    st.markdown("# 💤 Schlaf")

    st.info(sleep)


    # WORKOUT
    st.markdown("# 💪 Workout Plan")

    workout = generate_workout(goal)

    st.write(workout)


    # CHART
    st.markdown("# 📈 Fortschritt")

    show_progress_chart(weight)


    # BILDER VERGLEICH
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
