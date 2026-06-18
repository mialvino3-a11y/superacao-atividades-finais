import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    layout="wide",
    page_title="Atividades Finais — SuperAção SP",
    page_icon="📊",
)

# Remove padding do Streamlit para o HTML ocupar toda a tela
st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
</style>
""", unsafe_allow_html=True)

html_path = os.path.join(os.path.dirname(__file__), "atividades_finais_agentes.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1100, scrolling=True)
