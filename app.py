import streamlit as st
from ai_model import predict
from auth import create_table, register_user, login_user
from database import create_items_table, add_item, search_items
from PIL import Image
import datetime

# Tabellen erstellen
create_table()
create_items_table()

st.set_page_config(page_title="Fundbüro KI System", layout="wide")
st.title("🏛 Fundbüro KI System (Smartphone-ready)")

# --- Login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Login / Registrierung")
    username = st.text_input("Username")
    password = st.text_input("Passwort", type="password")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login erfolgreich!")
            else:
                st.error("Login fehlgeschlagen")
    with col2:
        if st.button("Registrieren"):
            if register_user(username, password):
                st.success("Registrierung erfolgreich!")
            else:
                st.error("Username existiert bereits")
else:
    st.subheader("🔐 Fundbüro")

    # --- Bild Upload + Kamera ---
    st.info("📤 Lade ein Bild hoch oder benutze die Kamera")
    uploaded_file = st.file_uploader("Bild hochladen", type=["jpg","jpeg","png"])
    camera_file = st.camera_input("📷 Kamera aufnehmen")

    image = None
    if uploaded_file:
        image = Image.open(uploaded_file)
    elif camera_file:
        image = Image.open(camera_file)

    if image:
        st.image(image, caption="Bild ausgewählt")
        predicted_class, confidence = predict(image)
        st.success(f"Vorhersage: {predicted_class} ({confidence*100:.2f}%)")
        
        # Datum
        date = st.date_input("Funddatum", datetime.date.today())
        add_item(predicted_class, uploaded_file.name if uploaded_file else "camera_photo", str(date))

    # --- Suche in der Datenbank ---
    st.subheader("🔍 Suche in der Funddatenbank")
    query = st.text_input("Suche nach Gegenständen")
    if query:
        results = search_items(query)
        for r in results:
            st.write(f"{r[0]} | {r[1]} | {r[3]}")
