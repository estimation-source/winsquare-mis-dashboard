import streamlit as st

st.set_page_config(page_title="Winsquare MIS Dashboard", layout="wide", page_icon="🪟")

# Custom Title Styling
st.markdown("<h1 style='text-align: center; color: #1e293b;'>Winsquare MIS DASHBOARD</h1>", unsafe_allow_html=True)
st.markdown("---")

# Module Navigation Selection
st.sidebar.title("📌 Modules Navigation")
page = st.sidebar.radio("मॉड्युल निवडा:", ["🏠 Home Dashboard", "⚡ Requirement Sheet Engine", "🪟 Window Details"])

if page == "🏠 Home Dashboard":
    st.subheader("Welcome to Winsquare MIS System")
    st.write("खालीलपैकी तुम्हाला हव्या असलेल्या मॉड्युलवर क्लिक करा:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### ⚡ Requirement Sheet Engine")
        st.write("BOQ फाईल्स मर्ज करा आणि Glass Requirement Sheet तयार करा.")
        # युझरने बटण दाबल्यावर पेज बदलेल
        if st.button("Requirement Sheet वर जा"):
            st.session_state["page"] = "Requirement Sheet Engine"
            
    with col2:
        st.success("### 🪟 Window Details")
        st.write("विंडो कोडनुसार स्पेसिफिकेशन्स आणि इतर डिटेल्स पहा.")
        if st.button("Window Details वर जा"):
            st.session_state["page"] = "Window Details"

elif page == "⚡ Requirement Sheet Engine":
    # इथे तुमचा Requirement Sheet Engine चा संपूर्ण कोड येईल
    st.title("Requirement Sheet Engine")
    st.write("तुमचा असलेला requirement engine कोड इथे रन करा.")

elif page == "🪟 Window Details":
    # इथे विंडो डिटेल्सचा कोड येईल
    st.title("Window Details Module")
    st.write("विंडो डिटेल्स मॉड्युलची माहिती इथे दाखवा.")
