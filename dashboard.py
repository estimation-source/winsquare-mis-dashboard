import streamlit as st

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Winsquare MIS Dashboard",
    page_icon="🪟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# MODERN ENTERPRISE UI STYLING (CSS)
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #f8fafc;
        color: #0f172a;
    }

    /* Hide Streamlit Header Elements */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .main .block-container {
        padding-top: 2.5rem;
        padding-bottom: 4rem;
        max-width: 1100px;
    }

    /* Top Banner Header */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 20px;
        padding: 40px 45px;
        color: #ffffff;
        box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.15), 0 8px 10px -6px rgba(15, 23, 42, 0.1);
        margin-bottom: 35px;
        position: relative;
        overflow: hidden;
    }

    .hero-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin: 0;
        color: #ffffff;
    }

    .hero-subtitle {
        font-size: 15px;
        color: #94a3b8;
        margin-top: 8px;
        font-weight: 500;
    }

    /* Dashboard Grid System */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
        gap: 24px;
    }

    /* Executive Module Card */
    .module-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 28px;
        position: relative;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.02);
    }

    .module-card:hover {
        border-color: #3b82f6;
        transform: translateY(-4px);
        box-shadow: 0 12px 20px -4px rgba(59, 130, 246, 0.12), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }

    .card-top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }

    .module-badge {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        padding: 4px 10px;
        border-radius: 20px;
        background-color: #eff6ff;
        color: #2563eb;
        border: 1px solid #bfdbfe;
    }

    .module-badge.green {
        background-color: #f0fdf4;
        color: #16a34a;
        border: 1px solid #bbf7d0;
    }

    .module-title {
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .module-desc {
        font-size: 14px;
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 24px;
    }

    /* Website-style Hyperlink */
    .web-link {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 14px;
        font-weight: 700;
        color: #2563eb;
        text-decoration: none !important;
        transition: color 0.2s ease, gap 0.2s ease;
    }

    .web-link:hover {
        color: #1d4ed8;
        gap: 10px;
    }

    .web-link-icon {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# MODULE LIVE LINKS SETUP
# ============================================================
# 🔴 येथे तुमच्या मूळ Streamlit Cloud / Web App च्या URLs टाका:
REQUIREMENT_ENGINE_URL = "https://requirement-sheet-engine.streamlit.app/"
WINDOW_DETAILS_URL = "https://your-window-details.streamlit.app"

# ============================================================
# DASHBOARD HERO BANNER
# ============================================================
st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-title">Winsquare MIS DASHBOARD</div>
        <div class="hero-subtitle">Central Gateway for Processing, BOQ Extraction & Project Management Modules</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# WEBSITE CARDS & HYPERLINKS VIEW
# ============================================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        f"""
        <div class="module-card">
            <div>
                <div class="card-top-row">
                    <span class="module-badge">BOQ Processing</span>
                </div>
                <div class="module-title">⚡ Requirement Sheet Engine</div>
                <div class="module-desc">
                    Multi-sheet BOQ Excel processing, automatic non-frosted glass extraction, SQFT calculation, and official requirement sheet generation.
                </div>
            </div>
            <div>
                <hr style="border: 0; border-top: 1px solid #f1f5f9; margin-bottom: 16px;">
                <a href="{REQUIREMENT_ENGINE_URL}" target="_blank" class="web-link">
                    Launch Module <span class="web-link-icon">↗</span>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="module-card">
            <div>
                <div class="card-top-row">
                    <span class="module-badge green">Specifications</span>
                </div>
                <div class="module-title">🪟 Window Details</div>
                <div class="module-desc">
                    Comprehensive window codes directory, profile specifications, hardware details, and component level breakdowns.
                </div>
            </div>
            <div>
                <hr style="border: 0; border-top: 1px solid #f1f5f9; margin-bottom: 16px;">
                <a href="{WINDOW_DETAILS_URL}" target="_blank" class="web-link">
                    Launch Module <span class="web-link-icon">↗</span>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
