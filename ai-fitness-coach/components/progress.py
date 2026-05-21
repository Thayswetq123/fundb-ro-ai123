import matplotlib.pyplot as plt
import streamlit as st


def show_progress_chart(weight):

    weights = [
        weight + 2,
        weight + 1,
        weight,
        weight - 1
    ]

    weeks = [1, 2, 3, 4]

    fig, ax = plt.subplots()

    ax.plot(weeks, weights)

    ax.set_xlabel("Woche")
    ax.set_ylabel("Gewicht")

    st.pyplot(fig)
