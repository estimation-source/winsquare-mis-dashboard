import streamlit as st

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Winsquare MIS Dashboard",
    page_icon="🪟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# Custom CSS for Modern Card UI
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }

    /* Main Container Padding */
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
    }

    /* Dashboard Title Card */
    .dashboard-header {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 30px;
    }

    .dashboard-title {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .dashboard-subtitle {
        font-size: 14px;
        color: #64748b;
        margin-top: 6px;
        font-weight: 500;
    }

    /* Module Links Cards */
    .module-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    .module-card:hover {
        border-color: #2563eb;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.1);
    }

    .module-title {
        font-size: 18px;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .module-desc {
        font-size: 13px;
        color: #64748b;
        margin-bottom: 16px;
        line-height: 1.5;
    }

    /* Action Link Button */
    .link-btn {
        display: inline-block;
        background-color: #2563eb;
        color: #ffffff !important;
        font-weight: 600;
        font-size: 14px;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none !important;
        transition: background-color 0.2s ease;
    }

    .link-btn:hover {
        background-color: #1d4ed8;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DASHBOARD HEADER
# ============================================================
st.markdown(
    """
    <div class="dashboard-header">
        <div class="dashboard-title">Winsquare MIS DASHBOARD</div>
        <div class="dashboard-subtitle">Central Gateway for Processing & Project Management Modules</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# MODULE LINKS SECTION
# ============================================================

# 🔴 टीप: खालील URLs मध्ये तुमच्या अचूक Live Links टाका
REQUIREMENT_ENGINE_URL = "https://your-requirement-engine.streamlit.app"
WINDOW_DETAILS_URL = "https://your-window-details.streamlit.app"

# Module 1: Requirement Sheet Engine
st.markdown(
    f"""
    <div class="module-card">
        <div class="module-title">⚡ Requirement Sheet Engine</div>
        <div class="module-desc">
            Multi-sheet BOQ Excel processing, non-frosted glass extraction, SQFT auto-calculation & official requirement sheet generation.
        </div>
        <a href="{REQUIREMENT_ENGINE_URL}" target="_blank" class="link-btn">
            Open Module 🔗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Module 2: Window Details
st.markdown(
    f"""
    <div class="module-card">
        <div class="module-title">🪟 Window Details</div>
        <div class="module-desc">
            Window codes, profile specs, hardware details, and individual window level breakdown view.
        </div>
        <a href="{WINDOW_DETAILS_URL}" target="_blank" class="link-btn">
            Open Module 🔗
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
