import json
import streamlit as st
import matplotlib.pyplot as plt

FILE = "progress.json"


def load_data(username):

    try:
        with open(FILE, "r") as f:
            data = json.load(f)

        return data.get(username, [])

    except:
        return []


def show_progress_dashboard(username):

    data = load_data(username)

    st.markdown("## 📊 Dein Fortschritt")

    if not data:
        st.info("Noch keine Daten vorhanden.")
        return

    weights = [entry["weight"] for entry in data]
    dates = [entry["date"] for entry in data]

    # 📈 GRAPH
    fig, ax = plt.subplots()

    ax.plot(weights, marker="o")

    ax.set_title("Gewichtsverlauf")
    ax.set_xlabel("Messung")
    ax.set_ylabel("Gewicht (kg)")

    st.pyplot(fig)

    # 📋 VERLAUF
    st.markdown("## 📜 Verlauf")

    for entry in reversed(data):

        st.write(
            f"📅 {entry['date'][:10]} | ⚖️ {entry['weight']} kg | 🔥 {entry['calories']} kcal"
        )

    # 🧠 INSIGHT
    st.markdown("## 🧠 Analyse")

    diff = weights[-1] - weights[0]

    if diff < 0:
        st.success(f"Du hast {abs(diff):.1f} kg verloren 🔥")
    elif diff > 0:
        st.warning(f"Du hast {diff:.1f} kg zugenommen 💪")
    else:
        st.info("Kein Gewichtsunterschied")
