from groq import Groq
import streamlit as st
import json

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

FILE = "progress.json"


def load_user_data(username):

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        return data.get(username, [])

    except:
        return []


def ai_progress_coach(username):

    data = load_user_data(username)

    if len(data) < 2:
        return "📊 Noch nicht genug Daten für eine KI-Analyse."

    weights = [str(x["weight"]) for x in data[-5:]]

    prompt = f"""
Du bist ein professioneller Fitness Coach.

Analysiere diesen Fortschritt:

Gewicht Verlauf (neueste Daten):
{weights}

Gib:
1. Trend Analyse
2. Ist die Person auf Kurs?
3. Fehler im Training oder Ernährung
4. Konkrete Anpassungen
5. Motivation

Antworte kurz, klar und motivierend.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Fehler: {str(e)}"
