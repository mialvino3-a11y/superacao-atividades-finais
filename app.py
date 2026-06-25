import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    layout="wide",
    page_title="SuperAcao SP | Paineis",
    page_icon="📊",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    footer { display: none !important; }
    [data-testid="stAppViewContainer"] { background: #F0F2F7; }
    [data-testid="stSidebar"] { background: #1C2F67; border-right: 1px solid rgba(255,255,255,.12); }
    [data-testid="stSidebar"] * { color: #fff; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] div { color: rgba(255,255,255,.72); }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 { color: #fff !important; letter-spacing: .01em; }
    [data-testid="stSidebar"] [role="radiogroup"] { gap: 8px; }
    [data-testid="stSidebar"] [role="radiogroup"] label {
        background: rgba(255,255,255,.08);
        border: 1px solid rgba(255,255,255,.13);
        border-radius: 6px;
        padding: 9px 10px !important;
        transition: all .15s ease;
    }
    [data-testid="stSidebar"] [role="radiogroup"] label:hover { background: rgba(255,255,255,.14); }
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background: #C8A951 !important;
        border-color: #C8A951 !important;
    }
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) * {
        color: #1C2F67 !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.14); margin: 16px 0; }
    iframe { display: block; background: #F0F2F7; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### SuperAcao SP")
    st.caption("Paineis de acompanhamento")
    st.divider()
    secao = st.radio(
        "Painel",
        ["Monitor de Estrategia", "Atividades Referencias por Agente"],
        label_visibility="collapsed",
    )
    st.divider()
    if secao == "Monitor de Estrategia":
        base_sel = st.selectbox(
            "Base de dados",
            ["25/06/2026 (atual)", "22/06/2026 (anterior)"],
        )
    else:
        base_sel = None

base = os.path.dirname(__file__)

if secao == "Monitor de Estrategia":
    if base_sel and "22/06" in base_sel:
        html_path = os.path.join(base, "monitor_estrategia_22062026.html")
    else:
        html_path = os.path.join(base, "monitor_estrategia_25062026.html")
else:
    html_path = os.path.join(base, "atividades_finais_agentes.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1450, scrolling=True)
