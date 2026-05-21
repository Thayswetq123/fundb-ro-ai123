from components.macros import calculate_macros
from components.water import calculate_water
from components.sleep import sleep_recommendation
from components.image_compare import show_image_comparison
import streamlit as st
from services.ai_service import analyze_fitness
from components.nutrition import calculate_calories
from components.workout import generate_workout
from components.progress import show_progress_chart

st.set_page_config(
    page_title="AI Fitness Coach",
    layout="wide"
)

st.title("💪 AI Fitness Coach")

st.markdown("## Deine persönliche Fitness Analyse")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input("Alter", 16, 100, 25)

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

with col2:

    image = st.file_uploader(
        "📸 Körperbild hochladen",
        type=["png", "jpg", "jpeg"]
    )

    if image:
        st.image(image)

if st.button("🚀 Analyse starten"):

    result = analyze_fitness(
        age,
        weight,
        height,
        goal
    )

    st.markdown("# 🧠 Analyse")
    st.write(result)

    show_progress_chart(weight)
