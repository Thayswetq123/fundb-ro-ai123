import streamlit as st
from database import init_db, save_item, get_items
from auth import register_user, login_user
from ai_model import predict
from PIL import Image
import io

init_db()
st.set_page_config(page_title="Fundbüro KI System")

st.title("Fundbüro KI System")

if "user" not in st.session_state:
    st.session_state.user = None

# LOGIN / REGISTER
if st.session_state.user is None:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.user = username
                st.success("Login erfolgreich!")
                st.experimental_rerun()
            else:
                st.error("Falscher Username oder Passwort")

    with tab2:
        new_user = st.text_input("Neuer Username")
        new_pass = st.text_input("Neues Passwort", type="password")
        if st.button("Registrieren"):
            if register_user(new_user, new_pass):
                st.success("Account erstellt!")
            else:
                st.error("Username existiert bereits")
    st.stop()

# Tabs: Upload / Kamera / Datenbank
tab1, tab2, tab3 = st.tabs(["Upload", "Kamera", "Datenbank"])

with tab1:
    uploaded = st.file_uploader("Bild hochladen", type=["jpg","jpeg","png","bmp","webp"])
    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        label = predict(image)
        st.image(image, width=300)
        st.success(label)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        save_item(st.session_state.user, buffer.getvalue(), label)

with tab2:
    cam = st.camera_input("Foto aufnehmen")
    if cam:
        image = Image.open(cam).convert("RGB")
        label = predict(image)
        st.image(image, width=300)
        st.success(label)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        save_item(st.session_state.user, buffer.getvalue(), label)

with tab3:
    search = st.text_input("Suche Gegenstand")
    date = st.text_input("Datum YYYY-MM-DD")
    rows = get_items()
    for r in rows:
        user, img, label, d = r
        if search and search.lower() not in label.lower():
            continue
        if date and date != str(d):
            continue
        st.image(img, width=200)
        st.write(label)
        st.write(d)
