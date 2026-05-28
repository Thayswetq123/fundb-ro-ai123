import random


def vision_analysis(goal, weight, height):

    bmi = weight / ((height / 100) ** 2)

    # stabile Bewertung statt komplett random
    bodyfat_estimation = round(
        28 - (bmi * 0.8),
        1
    )

    if bodyfat_estimation < 8:
        bodyfat_estimation = 8
    if bodyfat_estimation > 35:
        bodyfat_estimation = 35

    muscle_balance = {
        "Brust": random.randint(1, 10),
        "Rücken": random.randint(1, 10),
        "Beine": random.randint(1, 10),
        "Schultern": random.randint(1, 10),
        "Core": random.randint(1, 10)
    }

    weakest = min(muscle_balance, key=muscle_balance.get)
    strongest = max(muscle_balance, key=muscle_balance.get)

    if goal == "Muskelaufbau":
        focus = "Kalorienüberschuss + schwere Grundübungen"
    elif goal == "Fett verlieren":
        focus = "Kaloriendefizit + mehr Cardio"
    else:
        focus = "Balance aus Kraft & Cardio"

    return f"""
📸 AI Körperanalyse

📊 BMI:
{bmi:.1f}

🔥 Geschätzter KFA:
{bodyfat_estimation}%

💪 Stärkste Muskelgruppe:
{strongest}

⚠️ Schwächste Muskelgruppe:
{weakest}

🎯 Empfehlung:
{focus}

💡 Coaching:
Trainiere {weakest} öfter (2–3x pro Woche Fokus).
"""
