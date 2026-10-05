import streamlit as st
from urllib.parse import urlparse

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# ==============================
# BACKGROUND IMAGE
# ==============================
IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# ==============================
# CUSTOM DESIGN / CSS
# ==============================
st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(rgba(0,0,0,0.50), rgba(0,0,0,0.70)),
        url('{IMAGE_URL}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.stApp,
.stApp p,
.stApp label,
.stApp div {{
    font-weight: 700 !important;
}}

.main-title {{
    text-align: center;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 2.8rem;
    font-weight: 900 !important;
    text-transform: uppercase;
    color: #00f2fe !important;
    text-shadow:
        0 0 15px rgba(0,242,254,0.95),
        2px 2px 10px #000000;
    margin-top: 10px;
    margin-bottom: 5px;
}}

.sub-title {{
    text-align: center;
    font-size: 1.1rem;
    font-weight: 800 !important;
    text-transform: uppercase;
    color: #ffffff !important;
    text-shadow: 2px 2px 6px #000000;
    margin-bottom: 25px;
}}

.stApp h3 {{
    color: #ffd700 !important;
    font-weight: 900 !important;
    text-transform: uppercase;
    text-shadow: 2px 2px 7px #000000;
}}

div[data-baseweb="input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] {{
    background-color: rgba(255,255,255,0.10) !important;
    border: 1px solid rgba(255,255,255,0.55) !important;
    border-radius: 10px !important;
    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.45) !important;
}}

input,
textarea,
[data-baseweb="select"] * {{
    color: #ffffff !important;
    font-weight: 900 !important;
    text-transform: uppercase !important;
    text-shadow: 1px 1px 4px #000000;
}}

input::placeholder,
textarea::placeholder {{
    color: rgba(255,255,255,0.90) !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
}}

.stTextInput label,
.stTextArea label,
.stMultiSelect label {{
    color: #ffffff !important;
    font-weight: 900 !important;
    text-transform: uppercase !important;
    text-shadow: 2px 2px 5px #000000;
}}

.stButton > button {{
    width: 100%;
    background: linear-gradient(
        135deg,
        #00f2fe 0%,
        #4facfe 100%
    ) !important;
    color: #000000 !important;
    font-weight: 900 !important;
    font-size: 1.15rem !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px !important;
    box-shadow: 0 4px 20px rgba(0,242,254,0.60);
}}

.stButton > button:hover {{
    transform: scale(1.02);
    box-shadow: 0 6px 25px rgba(0,242,254,0.90);
}}

.stAlert {{
    font-weight: 800 !important;
}}

hr {{
    border-color: rgba(255,255,255,0.25) !important;
}}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    "<h1 class='main-title'>⚡ Rajveer Facebook Reporting Tool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Advanced Facebook Analytics & Reporting Dashboard</p>",
    unsafe_allow_html=True
)

st.write("---")


# ==============================
# TARGET CONFIGURATION
# ==============================

st.subheader("🎯 Target Configuration")

target_url = st.text_input(
    "Target Facebook Profile / Post URL:",
    placeholder="https://www.facebook.com/..."
)


# ==============================
# ALL REPORT REASONS
# ==============================

st.subheader("📋 Report Reasons")

report_reasons = [
    "HARASSMENT OR BULLYING",
    "HATE SPEECH",
    "IMPERSONATION",
    "SCAM OR FRAUD",
    "VIOLENCE OR THREATS",
    "SPAM",
    "PRIVACY ISSUE",
    "OTHER"
]

selected_reasons = st.multiselect(
    "APPLICABLE REPORT REASONS:",
    report_reasons,
    default=report_reasons
)


# ==============================
# REPORT DETAILS
# ==============================

details = st.text_area(
    "REPORT DETAILS:",
    placeholder="PROBLEM KO SHORT MEIN EXPLAIN KAREIN."
)


# ==============================
# FACEBOOK URL VALIDATION
# ==============================

def valid_facebook_url(url):
    try:
        parsed = urlparse(url.strip())
        host = (parsed.hostname or "").lower()

        return (
            parsed.scheme in ("http", "https")
            and (
                host == "facebook.com"
                or host.endswith(".facebook.com")
            )
        )

    except Exception:
        return False


# ==============================
# PREPARE REPORT
# ==============================

if st.button("🚀 START REPORTING PROCESS"):

    if not target_url.strip():

        st.error(
            "⚠️ PLEASE ENTER A FACEBOOK PROFILE / POST URL."
        )

    elif not valid_facebook_url(target_url):

        st.error(
            "⚠️ PLEASE ENTER A VALID FACEBOOK URL."
        )

    else:

        st.success(
            "✅ REPORT INFORMATION PREPARED SUCCESSFULLY!"
        )

        st.info(
            "OPEN THE TARGET ON FACEBOOK AND USE FACEBOOK'S "
            "OFFICIAL REPORT OPTION TO SUBMIT THE REPORT."
        )

        st.write("### 📋 REPORT INFORMATION")

        reasons_text = "\n".join(
            f"- {reason}"
            for reason in selected_reasons
        )

        st.code(
            f"TARGET URL:\n{target_url.strip()}\n\n"
            f"REPORT REASONS:\n{reasons_text}\n\n"
            f"DETAILS:\n"
            f"{details.strip() or '(NO ADDITIONAL DETAILS)'}",
            language="text"
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/",
            use_container_width=True
        )


# ==============================
# FOOTER
# ==============================

st.write("---")

st.caption(
    "⚠️ THIS TOOL DOES NOT COLLECT FACEBOOK PASSWORDS, "
    "SESSION COOKIES OR LOGIN CREDENTIALS."
)
