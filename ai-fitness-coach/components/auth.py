import streamlit as st
import json
import os


USERS_FILE = "users.json"


# DATEI ERSTELLEN
if not os.path.exists(USERS_FILE):

    with open(USERS_FILE, "w") as f:
        json.dump({}, f)


# USER LADEN
def load_users():

    with open(USERS_FILE, "r") as f:
        return json.load(f)


# USER SPEICHERN
def save_users(users):

    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


# LOGIN SYSTEM
def login_section():

    st.sidebar.title("🔐 Account")

    option = st.sidebar.selectbox(
        "Option",
        [
            "Login",
            "Registrieren"
        ]
    )

    users = load_users()

    username = st.sidebar.text_input("Username")

    password = st.sidebar.text_input(
        "Password",
        type="password"
    )


    # LOGIN
    if option == "Login":

        if st.sidebar.button("Einloggen"):

            if username in users:

                if users[username] == password:

                    st.sidebar.success(
                        f"Willkommen {username}"
                    )

                    return True

                else:
                    st.sidebar.error(
                        "Falsches Passwort"
                    )

            else:
                st.sidebar.error(
                    "User existiert nicht"
                )


    # REGISTER
    if option == "Registrieren":

        if st.sidebar.button("Account erstellen"):

            if username in users:

                st.sidebar.error(
                    "Username existiert bereits"
                )

            else:

                users[username] = password

                save_users(users)

                st.sidebar.success(
                    "Account erstellt!"
                )

    return False
