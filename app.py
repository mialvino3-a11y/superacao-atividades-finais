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
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.14); margin: 16px 0; }
    iframe { display: block; background: #F0F2F7; }
    .painel-ativo {
        background: #C8A951;
        border: 1px solid #C8A951;
        border-radius: 6px;
        padding: 9px 10px;
        color: #1C2F67 !important;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .painel-ativo .dot { width: 9px; height: 9px; border-radius: 50%; background: #1C2F67; flex-shrink: 0; }
    /* Setinha de recolher a sidebar: sempre visivel e com contraste alto */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        opacity: 1 !important;
        visibility: visible !important;
    }
    [data-testid="stSidebarCollapseButton"] button,
    [data-testid="collapsedControl"] button {
        background: #C8A951 !important;
        border-radius: 50% !important;
        box-shadow: 0 1px 4px rgba(0,0,0,.25);
    }
    [data-testid="stSidebarCollapseButton"] svg,
    [data-testid="collapsedControl"] svg {
        color: #1C2F67 !important;
        fill: #1C2F67 !important;
    }
    /* Selectbox "Base de dados": o fundo do campo e branco, entao o texto
       precisa ficar escuro (a regra generica acima deixa tudo branco,
       o que tornava o valor selecionado invisivel). */
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #fff !important;
        border: 1.5px solid #C8A951 !important;
        border-radius: 6px !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #1C2F67 !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### SuperAcao SP")
    st.caption("Paineis de acompanhamento")
    st.divider()
    st.markdown(
        '<div class="painel-ativo"><span class="dot"></span>Monitor de Estrategia</div>',
        unsafe_allow_html=True,
    )
    st.divider()
    base_sel = st.selectbox(
        "Base de dados",
        ["02/07/2026 (atual)", "29/06/2026 (anterior)", "26/06/2026", "25/06/2026", "22/06/2026"],
    )

base = os.path.dirname(__file__)

if base_sel and "22/06" in base_sel:
    html_path = os.path.join(base, "monitor_estrategia_22062026.html")
elif base_sel and "25/06" in base_sel:
    html_path = os.path.join(base, "monitor_estrategia_25062026.html")
elif base_sel and "26/06" in base_sel:
    html_path = os.path.join(base, "monitor_estrategia_26062026.html")
elif base_sel and "29/06" in base_sel:
    html_path = os.path.join(base, "monitor_estrategia_29062026.html")
else:
    html_path = os.path.join(base, "monitor_estrategia_02072026.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1450, scrolling=True)
