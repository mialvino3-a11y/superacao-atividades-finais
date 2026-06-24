import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    layout="wide",
    page_title="Atividades Finais — SuperAção SP",
    page_icon="📊",
)

st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
    [data-testid="stRadio"] { position: fixed; top: 0; left: 0; right: 0; z-index: 999;
        background: #1C2F67; padding: 8px 20px; }
    [data-testid="stRadio"] label { color: #fff !important; font-weight: 600 !important;
        font-size: 0.88rem !important; }
    [data-testid="stRadio"] > div { flex-direction: row !important; gap: 8px; }
    [data-testid="stRadio"] > div > label {
        background: rgba(255,255,255,0.12); border-radius: 6px;
        padding: 5px 16px !important; cursor: pointer; }
    [data-testid="stRadio"] > div > label:has(input:checked) {
        background: #0891B2 !important; }
    div[data-testid="stVerticalBlock"] > div:first-child { margin-top: 48px; }
</style>
""", unsafe_allow_html=True)

secao = st.radio(
    "",
    ["📊 Atividades Finais por Agente", "📋 Monitor de Estratégia (22/06)"],
    horizontal=True,
    label_visibility="collapsed",
)

base = os.path.dirname(__file__)

if secao == "📊 Atividades Finais por Agente":
    html_path = os.path.join(base, "atividades_finais_agentes.html")
else:
    html_path = os.path.join(base, "monitor_estrategia.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)
