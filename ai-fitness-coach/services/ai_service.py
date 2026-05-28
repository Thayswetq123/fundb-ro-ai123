from groq import Groq
import streamlit as st


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def analyze_fitness(
    age,
    weight,
    height,
    goal
):

    prompt = f"""
Du bist ein professioneller Fitness Coach.

Person:
- Alter: {age}
- Gewicht: {weight}kg
- Größe: {height}cm
- Ziel: {goal}

Erstelle:
1. Körperanalyse
2. Trainingsplan
3. Ernährung
4. Kalorien Empfehlung
5. Motivation

Antworte modern und motivierend.
"""

    try:

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Fehler: {str(e)}"
