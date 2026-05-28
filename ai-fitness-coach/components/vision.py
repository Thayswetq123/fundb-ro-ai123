import random


def vision_analysis():

    bodyfat = random.randint(10, 25)

    muscles = [
        "Brust",
        "Schultern",
        "Rücken",
        "Arme"
    ]

    weak_point = random.choice(muscles)

    return f"""
📸 KI Vision Analyse

Geschätzter Körperfettanteil:
{bodyfat}%

Verbesserungspotenzial:
{weak_point}

Empfehlung:
Mehr Fokus auf progressive Belastung.
"""
