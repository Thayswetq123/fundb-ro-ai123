import streamlit as st


def login_section():

    # =========================
    # SESSION STATE SAFE INIT
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
        <div style='text-align:center; padding:30px'>
            <h1>💪 AI Fitness Coach</h1>
            <p style='color:gray'>Login oder Account erstellen</p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("🚀 Login / Register"):

            if username.strip() != "":

                st.session_state.logged_in = True
                st.session_state.username = username.strip()

                st.success("Login erfolgreich 🚀")

                st.rerun()

            else:
                st.error("Bitte Username eingeben")

    # =========================
    # LOGGED IN STATE
    # =========================
    else:

        st.sidebar.markdown("### 👤 Account")

        st.sidebar.success(f"{st.session_state.username}")

        if st.sidebar.button("🚪 Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()
