# components/auth.py

import streamlit as st
from components.user_db import register_user, login_user

def login_section():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    if not st.session_state.logged_in:

        st.markdown("""
        <style>
        .login-box {
            max-width: 500px;
            margin: 50px auto;
            padding: 35px;
            border-radius: 20px;
            background: rgba(17,24,39,0.85);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
        }

        .hero-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            color: #9ca3af;
            margin-bottom: 25px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="login-box">
            <div class="hero-title">💪 AI Fitness Coach</div>
            <div class="hero-subtitle">
                Dein persönlicher KI Fitness Coach
            </div>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔑 Login", "🆕 Registrieren"])

        with tab1:

            username = st.text_input(
                "Username",
                key="login_user"
            )

            password = st.text_input(
                "Passwort",
                type="password",
                key="login_pass"
            )

            if st.button("🚀 Login", use_container_width=True):

                success, msg = login_user(
                    username,
                    password
                )

                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()

                st.error(msg)

        with tab2:

            username = st.text_input(
                "Neuer Username",
                key="reg_user"
            )

            password = st.text_input(
                "Neues Passwort",
                type="password",
                key="reg_pass"
            )

            if st.button(
                "✨ Account erstellen",
                use_container_width=True
            ):

                success, msg = register_user(
                    username,
                    password
                )

                if success:
                    st.success(msg)
                else:
                    st.error(msg)

    else:

        st.sidebar.success(
            f"👤 {st.session_state.username}"
        )

        if st.sidebar.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()
