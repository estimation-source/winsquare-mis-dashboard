import streamlit as st

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Winsquare MIS Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# INJECT CLEAN STYLES (NO PLAIN TEXT BREAKAGE)
# ============================================================
css_code = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: #f8fafc !important;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

/* Compact Banner */
.hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: 10px;
    padding: 18px 24px;
    color: #ffffff;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
    margin-bottom: 20px;
}

.hero-title {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0;
}

.hero-subtitle {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 2px;
}

/* Compact Module Card */
.module-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}

.module-card:hover {
    border-color: #2563eb;
    box-shadow: 0 6px 12px -2px rgba(37, 99, 235, 0.1);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.badge {
    font-size: 9.5px;
    font-weight: 700;
    text-transform: uppercase;
    padding: 2px 7px;
    border-radius: 4px;
}

.badge-blue { background: #eff6ff; color: #2563eb; border: 1px solid #bfdbfe; }
.badge-green { background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }
.badge-purple { background: #faf5ff; color: #9333ea; border: 1px solid #e9d5ff; }

.module-title {
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
}

.module-desc {
    font-size: 12px;
    color: #64748b;
    line-height: 1.4;
}

.web-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12.5px;
    font-weight: 600;
    color: #2563eb;
    text-decoration: none !important;
}
</style>
"""

st.markdown(css_code, unsafe_allow_html=True)

# ============================================================
# MODULE LIVE LINKS SETUP
# ============================================================
REQUIREMENT_ENGINE_URL = "https://your-requirement-engine.streamlit.app"
WINDOW_DETAILS_URL = "https://your-window-details.streamlit.app"
GLASS_PI_VERIFY_URL = "https://glass-pi-verification.streamlit.app/"

# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-title">
            <i class="fa-solid fa-chart-line" style="font-size: 18px; color: #38bdf8;"></i> Winsquare MIS DASHBOARD
        </div>
        <div class="hero-subtitle">Central Gateway for Processing, BOQ Extraction & Project Management Modules</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 3-COLUMN COMPACT LAYOUT
# ============================================================
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.markdown(
        f"""
        <div class="module-card">
            <div>
                <div class="card-header">
                    <span class="badge badge-blue">BOQ Processing</span>
                    <i class="fa-solid fa-file-invoice-dollar" style="color:#2563eb; font-size: 14px;"></i>
                </div>
                <div class="module-title">Requirement Sheet Engine</div>
                <div class="module-desc">Multi-sheet BOQ Excel processing, non-frosted glass extraction & SQFT auto-calculation.</div>
            </div>
            <div>
                <hr style="border:0; border-top: 1px solid #f1f5f9; margin: 8px 0;">
                <a href="{REQUIREMENT_ENGINE_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right" style="font-size: 11px;"></i>
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
                <div class="card-header">
                    <span class="badge badge-green">Specifications</span>
                    <i class="fa-solid fa-border-all" style="color:#16a34a; font-size: 14px;"></i>
                </div>
                <div class="module-title">Window Details</div>
                <div class="module-desc">Window codes directory, profile specs, hardware details, and component breakdowns.</div>
            </div>
            <div>
                <hr style="border:0; border-top: 1px solid #f1f5f9; margin: 8px 0;">
                <a href="{WINDOW_DETAILS_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right" style="font-size: 11px;"></i>
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
                <div class="card-header">
                    <span class="badge badge-purple">Analytics / MIS</span>
                    <i class="fa-solid fa-chart-pie" style="color:#9333ea; font-size: 14px;"></i>
                </div>
                <div class="module-title">GLASS PI VERIFICATION</div>
                <div class="module-desc">Glass Proforma Invoice verification, quantity cross-checks, and rate validation system.</div>
            </div>
            <div>
                <hr style="border:0; border-top: 1px solid #f1f5f9; margin: 8px 0;">
                <a href="{GLASS_PI_VERIFY_URL}" target="_blank" class="web-link">
                    Launch Module <i class="fa-solid fa-arrow-right" style="font-size: 11px;"></i>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
