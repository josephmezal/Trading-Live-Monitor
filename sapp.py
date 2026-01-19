import streamlit as st

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="Pixxian Capital. Monitoreo de Mercados Financieros",
    page_icon="🌐📊",
    layout="wide"
)

# ---------------------------
# Sidebar (similar st)
# ---------------------------
st.sidebar.title("⚙️ Menu de opciones")
st.sidebar.markdown("**Noticias Financieras Internacionales en Vivo & Data Streams**")

st.sidebar.info(
    """
     Esta aplicacion reproduce en vivo
    **live YouTube streams**.

    Cubrimos:
    - Finanzas internacionales 
    - Data Science
    - Marcados Financieros
    - Analisis Fundamental
    - Analisis Tecnico
    - Proximamente Intermediacion 
      Cripto-Financiera y Asesoria en 
      Derecho Fiscal internacional 
    """
)

# Optional selector (future extension)
stream_option = st.sidebar.selectbox(
    "Select live stream:",
    [
        "Live Stream 1 (Default)"
    ]
)

# ---------------------------
# Main dashboard
# ---------------------------
st.title("📺 Live Stream ")
st.markdown(
    """
     Este servicio se monitoreo de mercados es ofrecido por **Pixxian Capital, mercados por abrir**,  
      Mantiene las noticias reproduciendo en vivo directamente dentro de esta aplicacion.
    """
)

# ---------------------------
# Video section
# ---------------------------
st.subheader("🔴 Live Stream")

st.video(
    "https://www.youtube.com/watch?v=xLqt2p6Dowo"
)

# ---------------------------
# Dashboard-style layout
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Stream Status", value="LIVE")

with col2:
    st.metric(label="Platform", value="YouTube")

with col3:
    st.metric(label="AI", value="🚀")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption(
    "Pixxian Capital • Mercados por abrir  • Version de app para iOS Safari "
)
