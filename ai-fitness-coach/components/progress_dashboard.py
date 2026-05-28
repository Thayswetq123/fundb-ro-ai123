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

    st.markdown("## 📊 Dein Dashboard")

    if not data:
        st.info("Noch keine Daten vorhanden.")
        return

    weights = [x["weight"] for x in data]
    calories = [x["calories"] for x in data]

    # =========================
    # 📌 KPI CARDS (MODERN UI)
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ⚖️ Aktuelles Gewicht")
        st.metric("kg", weights[-1], f"{weights[-1] - weights[0]:.1f}")

    with col2:
        st.markdown("### 🔥 Kalorien Ziel")
        st.metric("kcal", calories[-1])

    with col3:
        trend = weights[-1] - weights[0]
        st.markdown("### 📈 Trend")

        if trend < 0:
            st.success(f"-{abs(trend):.1f} kg 🔥")
        else:
            st.warning(f"+{trend:.1f} kg 💪")

    st.markdown("---")

    # =========================
    # 📈 CHART (MODERN)
    # =========================

    st.markdown("## 📈 Gewicht Verlauf")

    fig, ax = plt.subplots()

    ax.plot(weights, marker="o", linewidth=3)

    ax.set_xlabel("Messung")
    ax.set_ylabel("Gewicht (kg)")
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)

    st.markdown("---")

    # =========================
    # 📜 HISTORY CARDS
    # =========================

    st.markdown("## 📜 Verlauf")

    for entry in reversed(data):

        st.markdown(f"""
        <div style="
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 12px;
            background-color: #111;
            color: white;
            border: 1px solid #333;
        ">
            📅 <b>{entry['date'][:10]}</b><br>
            ⚖️ Gewicht: <b>{entry['weight']} kg</b><br>
            🔥 Kalorien: <b>{entry['calories']}</b>
        </div>
        """, unsafe_allow_html=True)
