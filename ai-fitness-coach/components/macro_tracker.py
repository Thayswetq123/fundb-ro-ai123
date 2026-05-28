import streamlit as st


def macro_tracker():

    st.markdown("# 🍽 Tages Makros")

    protein = st.slider("Protein", 0, 300, 120)
    carbs = st.slider("Carbs", 0, 500, 250)
    fats = st.slider("Fette", 0, 150, 60)

    st.success(
        f"Protein: {protein}g | Carbs: {carbs}g | Fette: {fats}g"
    )
