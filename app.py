import streamlit as st

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="Live YouTube Dashboard",
    page_icon="📺",
    layout="wide"
)

# ---------------------------
# Sidebar (similar style to your car price app)
# ---------------------------
st.sidebar.title("📊 Dashboard Controls")
st.sidebar.markdown("**Live Financial & Data Streams**")

st.sidebar.info(
    """
    This dashboard continuously plays
    **live YouTube streams**.

    Designed for:
    - Finance
    - Data Science
    - Markets
    - Education
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
st.title("📺 Live YouTube Stream Dashboard")
st.markdown(
    """
    This Streamlit dashboard embeds **live YouTube video streams**  
    and keeps them running directly inside the app.
    """
)

# ---------------------------
# Video section
# ---------------------------
st.subheader("🔴 Live Stream")

st.video(
    "https://www.youtube.com/live/xLqt2p6Dowo"
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
    st.metric(label="App Framework", value="Streamlit")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption(
    "Built with Streamlit • Optimized for mobile & desktop • iOS Safari compatible"
)
