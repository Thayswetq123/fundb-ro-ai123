import json
from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

FILE = "progress.json"


def load_data(username):

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        return data.get(username, [])

    except:
        return []


def adaptive_training_plan(username, goal):

    data = load_data(username)

    if len(data) < 2:
        return "📊 Noch nicht genug Daten für Anpassung."

    weights = [x["weight"] for x in data[-5:]]

    trend = weights[-1] - weights[0]

    prompt = f"""
Du bist ein Elite Fitness Coach.

Ziel der Person: {goal}

Gewichtsverlauf:
{weights}

Trend: {trend} kg Veränderung

Erstelle:

1. Bewertung des aktuellen Trainingsplans
2. Ist der Plan zu leicht oder zu schwer?
3. Was muss geändert werden?
4. Neuer optimierter Trainingsplan (kurz)
5. Ernährung Anpassung
6. Motivation

Antworte klar, direkt, motivierend.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Fehler: {str(e)}"
