import streamlit as st


def chatbot_coach():

    st.markdown("# 🤖 Fitness Coach")

    question = st.text_input(
        "Stelle eine Fitness Frage"
    )

    if question:

        if "protein" in question.lower():
            st.write("Protein ist wichtig für Muskelaufbau.")

        elif "cardio" in question.lower():
            st.write("Cardio verbessert Ausdauer und Fettverbrennung.")

        else:
            st.write(
                "Bleib konstant und trainiere smart 💪"
            )
