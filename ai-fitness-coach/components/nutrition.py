def calculate_calories(weight, height, age, goal):

    maintenance = 10 * weight + 6.25 * height - 5 * age + 5

    if goal == "Muskelaufbau":
        return int(maintenance + 300)

    elif goal == "Fett verlieren":
        return int(maintenance - 400)

    return int(maintenance)
