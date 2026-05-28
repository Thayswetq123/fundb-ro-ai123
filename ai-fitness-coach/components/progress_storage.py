import json
import os
from datetime import datetime

FILE = "progress.json"


# Datei erstellen falls nicht vorhanden
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)


def load_progress():
    with open(FILE, "r") as f:
        return json.load(f)


def save_progress_entry(username, weight, calories):

    data = load_progress()

    if username not in data:
        data[username] = []

    data[username].append({
        "date": str(datetime.now()),
        "weight": weight,
        "calories": calories
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
