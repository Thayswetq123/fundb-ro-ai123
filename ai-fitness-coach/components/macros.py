def calculate_macros(calories, goal):

    if goal == "Muskelaufbau":

        protein = calories * 0.30 / 4
        carbs = calories * 0.45 / 4
        fats = calories * 0.25 / 9

    elif goal == "Fett verlieren":

        protein = calories * 0.40 / 4
        carbs = calories * 0.30 / 4
        fats = calories * 0.30 / 9

    else:

        protein = calories * 0.35 / 4
        carbs = calories * 0.35 / 4
        fats = calories * 0.30 / 9

    return {
        "Protein": int(protein),
        "Carbs": int(carbs),
        "Fats": int(fats)
    }
