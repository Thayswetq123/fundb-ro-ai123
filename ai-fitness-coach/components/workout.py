def generate_workout(goal):

    if goal == "Muskelaufbau":

        return """
Montag: Brust + Trizeps
Dienstag: Rücken + Bizeps
Mittwoch: Pause
Donnerstag: Beine
Freitag: Schultern
"""

    elif goal == "Fett verlieren":

        return """
Montag: HIIT
Dienstag: Oberkörper
Mittwoch: Cardio
Donnerstag: Unterkörper
Freitag: Ganzkörper
"""

    return """
Montag: Ganzkörper
Mittwoch: Cardio
Freitag: Krafttraining
"""
