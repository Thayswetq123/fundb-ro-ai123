import streamlit as st
from PIL import Image


def show_image_comparison(before, after):

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Vorher")
        st.image(before)

    with col2:
        st.markdown("## Nachher")
        st.image(after)
