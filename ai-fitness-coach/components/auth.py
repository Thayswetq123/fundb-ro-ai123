import streamlit as st


def login_section():

    st.sidebar.title("🔐 Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input(
        "Password",
        type="password"
    )

    if st.sidebar.button("Login"):

        if username and password:
            st.sidebar.success(f"Willkommen {username}")
            return True

        st.sidebar.error("Ungültige Daten")

    return False
