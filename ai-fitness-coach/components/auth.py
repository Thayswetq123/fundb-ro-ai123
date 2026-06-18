import streamlit as st
from components.user_db import register_user, login_user


def login_section():

    # =========================
    # SESSION STATE
    # =========================
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""

    # =========================
    # LOGIN SCREEN
    # =========================
    if not st.session_state.logged_in:

        st.markdown("""
        <style>

        .hero-box {
            text-align: center;
            padding: 20px;
            margin-bottom: 20px;
        }

        .hero-title {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            font-size: 18px;
            color: #9ca3af;
        }

        </style>
        """, unsafe_allow_html=True)

        # Hero Bild (optional)
        try:
            st.image(
                "assets/hero.jpg",
                use_container_width=True
            )
        except:
            pass

        st.markdown("""
        <div class="hero-box">
            <div class="hero-title">
                💪 AI Fitness Coach
            </div>

            <div class="hero-subtitle">
                Dein persönlicher KI Coach für Training,
                Ernährung und Fortschritt.
            </div>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs([
            "🔑 Login",
            "🆕 Registrieren"
        ])

        # =========================
        # LOGIN
        # =========================
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

            if st.button(
                "🚀 Login",
                use_container_width=True
            ):

                success, msg = login_user(
                    username,
                    password
                )

                if success:

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.success("Login erfolgreich 🚀")
                    st.rerun()

                else:
                    st.error(msg)

        # =========================
        # REGISTER
        # =========================
        with tab2:

            new_user = st.text_input(
                "Neuer Username",
                key="reg_user"
            )

            new_pass = st.text_input(
                "Neues Passwort",
                type="password",
                key="reg_pass"
            )

            if st.button(
                "✨ Account erstellen",
                use_container_width=True
            ):

                success, msg = register_user(
                    new_user,
                    new_pass
                )

                if success:
                    st.success("Account erstellt 🎉")
                else:
                    st.error(msg)

    # =========================
    # EINGELOGGT
    # =========================
    else:

        st.sidebar.markdown("### 👤 Account")
        st.sidebar.success(
            st.session_state.username
        )

        if st.sidebar.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()
