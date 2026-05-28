import json
import os
import hashlib

FILE = "users.json"


# =========================
# INIT FILE
# =========================
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)


def load_users():
    with open(FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# HASH PASSWORD
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# REGISTER USER
# =========================
def register_user(username, password):

    users = load_users()

    if username in users:
        return False, "User existiert bereits"

    users[username] = {
        "password": hash_password(password)
    }

    save_users(users)

    return True, "Account erstellt"


# =========================
# LOGIN USER
# =========================
def login_user(username, password):

    users = load_users()

    if username not in users:
        return False, "User nicht gefunden"

    hashed = hash_password(password)

    if users[username]["password"] != hashed:
        return False, "Falsches Passwort"

    return True, "Login erfolgreich"
