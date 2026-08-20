import base64
import os
import streamlit as st

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Winsquare MIS Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# HELPER: LOAD LOGO AS BASE64 FOR HTML EMBEDDING
# ============================================================
logo_html = ""
logo_path = "logo.png"

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    logo_html = f'<img src="data:image/png;base64,{encoded_string}" class="hero-logo" alt="Winsquare Logo">'


# ============================================================
# ENTERPRISE UI STYLING & ICONS (CLEANED & FIXED)
# ============================================================
st.markdown(
    """
    <!-- FontAwesome Vector Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .main .block-container {
        padding-top: 3rem !important;
        padding-bottom: 4rem !important;
        max-width: 1200px !important;
    }

    /* Top Hero Banner with Logo Integration */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 16px;
        padding: 32px 40px;
        color: #ffffff;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.12);
        margin-bottom: 32px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .hero-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .hero-subtitle {
        font-size: 14px;
        color: #94a3b8;
        margin-top: 6px;
        font-weight: 500;
    }

    .hero-logo {
        height: 60px;
        width: auto;
        max-width: 180px;
        object-fit: contain;
        background: rgba(255, 255, 255, 0.95);
        padding: 6px 12px;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    /* Executive Module Card */
    .module-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 26px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.25s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }

    .module-card:hover {
        border-color: #2563eb;
        transform: translateY(-3px);
        box-shadow: 0 12px 20px -4px rgba(37, 99, 235, 0.08);
    }

    /* Icon Container */
    .icon-box {
        width: 44px;
        height: 44px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-bottom: 16px;
    }

    .icon-engine {
        background-color: #eff6ff;
        color: #2563eb;
    }

    .icon-window {
        background-color: #f0fdf4;
        color: #16a34a;
    }

    .icon-glass {
        background-color: #faf5ff;
        color: #9333ea;
    }

    .module-title {
        font-size: 19px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .module-desc {
        font-size: 13.5px;
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* Professional Website Link */
    .web-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
        font-weight: 600;
        color: #2563eb;
        text-decoration: none !important;
        transition: all 0.2s ease;
    }

    .web-link:hover {
        color: #1d4ed8;
        gap: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# MODULE LIVE LINKS SETUP
# ============================================================
REQUIREMENT_ENGINE_URL = "https://requirement-sheet-engine.streamlit.app/"
WINDOW_DETAILS_URL = "https://your-window-details.streamlit.app"
GLASS_PI_VERIFICATION_URL = "https://glass-pi-verification.streamlit.app/"

# ============================================================
# HEADER WITH INTEGRATED LOGO
# ============================================================
st.markdown(
    f"""
    <div class="hero-banner">
        <div>
            <div class="hero-title">
                <i class="fa-solid fa-chart-line"></i> Winsquare MIS DASHBOARD
            </div>
            <div class="hero-subtitle">Central Gateway for Processing, BOQ Extraction & Project Management Modules</div>
        </div>
        {logo_html}
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 3-COLUMN LAYOUT WITH VECTOR ICONS & LINKS
# ============================================================
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(
        f"""
        <div class="module-card">
            <div>
                <div class="icon-box icon-engine">
                    <i class="fa-solid fa-file-invoice-dollar"></i>
                </div>
                <div class="module-title">Requirement Sheet Engine</div>
                <div class="module-desc">
                    Multi-sheet BOQ Excel processing, automatic non-frosted glass extraction, SQFT auto-calculation, and official requirement sheet generation.
                </div>
            </div>
            <div>
                <hr style="border: 0; border-top: 1px solid #f1f5f9; margin-bottom: 16px;">
                <a href="{REQUIREMENT_ENGINE_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right-long"></i>
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
                <div class="icon-box icon-window">
                    <i class="fa-solid fa-border-all"></i>
                </div>
                <div class="module-title">Window Details</div>
                <div class="module-desc">
                    Comprehensive window codes directory, profile specifications, hardware details, and component level breakdowns.
                </div>
            </div>
            <div>
                <hr style="border: 0; border-top: 1px solid #f1f5f9; margin-bottom: 16px;">
                <a href="{WINDOW_DETAILS_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right-long"></i>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="module-card">
            <div>
                <div class="icon-box icon-glass">
                    <i class="fa-solid fa-chart-pie"></i>
                </div>
                <div class="module-title">Glass & PI Verification</div>
                <div class="module-desc">
                    Glass Proforma Invoice verification, quantity cross-checks, rate validation system, and automated mismatch detection.
                </div>
            </div>
            <div>
                <hr style="border: 0; border-top: 1px solid #f1f5f9; margin-bottom: 16px;">
                <a href="{GLASS_PI_VERIFICATION_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right-long"></i>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
