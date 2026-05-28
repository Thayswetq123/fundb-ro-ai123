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


# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# LOGIN SYSTEM
def login_section():

    st.sidebar.title("🔐 Account")

    users = load_users()

    # WENN EINGELOGGT
    if st.session_state.logged_in:

        st.sidebar.success(
            f"Eingeloggt als {st.session_state.username}"
        )

        if st.sidebar.button("Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()

        return True


    option = st.sidebar.selectbox(
        "Option",
        [
            "Login",
            "Registrieren"
        ]
    )

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

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.rerun()

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
