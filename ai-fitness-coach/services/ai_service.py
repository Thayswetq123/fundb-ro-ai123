import random


def analyze_fitness(age, weight, height, goal):

    bmi = weight / ((height / 100) ** 2)

    quotes = [
        "Disziplin schlägt Motivation.",
        "Jeder Fortschritt zählt.",
        "Konstanz gewinnt.",
        "Bleib fokussiert."
    ]

    quote = random.choice(quotes)

    if bmi < 20:
        body = "schlank"
    elif bmi < 26:
        body = "athletisch"
    else:
        body = "kräftig"

    return f"""
📊 BMI: {bmi:.1f}

👤 Körpertyp:
{body}

🎯 Ziel:
{goal}

🔥 Empfehlung:
Trainiere konstant 4-5x pro Woche.

💡 Motivation:
{quote}
"""
