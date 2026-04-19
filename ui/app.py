import streamlit as st
st.set_page_config(page_title="JST Engine", layout="wide")
st.title("🗜️ Joke-Space Transform v1.0")
st.sidebar.markdown("### Settings")
mode = st.sidebar.selectbox("Mode", ["Mapping", "Generation", "Analytics"])

col1, col2 = st.columns(2)
with col1:
    concept = st.text_area("Literal Concept", "The 2026 Housing Market")
with col2:
    joke = st.text_area("Joke Representation", "A 1200-sq-ft hostage situation.")

tension = st.slider("Structural Tension", 0.0, 1.0, 0.85)

if st.button("Anchor to Joke-Space"):
    st.balloons()
    st.success("Vector committed to latent space.")
