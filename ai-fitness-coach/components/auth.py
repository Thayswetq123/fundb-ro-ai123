import streamlit as st
from components.user_db import register_user, login_user


def login_section():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:

        st.title("💪 AI Fitness Coach")

        tab1, tab2 = st.tabs(["🔑 Login", "🆕 Register"])

        # =========================
        # LOGIN
        # =========================
        with tab1:

            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")

            if st.button("Login"):

                success, msg = login_user(username, password)

                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

        # =========================
        # REGISTER
        # =========================
        with tab2:

            new_user = st.text_input("New Username", key="reg_user")
            new_pass = st.text_input("New Password", type="password", key="reg_pass")

            if st.button("Create Account"):

                success, msg = register_user(new_user, new_pass)

                if success:
                    st.success(msg)
                else:
                    st.error(msg)

    else:

        st.sidebar.success(f"👤 {st.session_state.username}")

        if st.sidebar.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()
