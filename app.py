import streamlit as st
from urllib.parse import urlparse

# ==============================
# PAGE CONFIG
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
# CUSTOM CSS
# ==============================
st.markdown(
    f"""
    <style>

    /* MAIN BACKGROUND */
    .stApp {{
        background:
            linear-gradient(
                rgba(0, 0, 0, 0.45),
                rgba(0, 0, 0, 0.55)
            ),
            url("{IMAGE_URL}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* MAIN CONTENT */
    .block-container {{
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* TITLE */
    .main-title {{
        text-align: center;
        color: #00eaff;
        font-size: 42px;
        font-weight: 900;
        text-transform: uppercase;
        text-shadow:
            0 0 10px rgba(0, 234, 255, 0.8),
            0 0 25px rgba(0, 234, 255, 0.5);
        margin-bottom: 5px;
    }}

    /* SUBTITLE */
    .sub-title {{
        text-align: center;
        color: white;
        font-size: 18px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 30px;
    }}

    /* SECTION HEADINGS */
    h1, h2, h3 {{
        color: #ffd700 !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* LABELS */
    label {{
        color: white !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* ==============================
       TRANSPARENT TEXT BOXES
       ============================== */

    /* TEXT INPUT */
    div[data-baseweb="input"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.20);
    }}

    div[data-baseweb="input"] > div {{
        background: transparent !important;
    }}

    /* TEXTAREA */
    div[data-baseweb="textarea"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.20);
    }}

    div[data-baseweb="textarea"] > div {{
        background: transparent !important;
    }}

    /* INPUT + TEXTAREA TEXT */
    input,
    textarea {{
        background: transparent !important;
        color: white !important;
        font-weight: 900 !important;
        font-size: 15px !important;
    }}

    /* PLACEHOLDER */
    input::placeholder,
    textarea::placeholder {{
        color: rgba(255, 255, 255, 0.80) !important;
        font-weight: 800 !important;
        text-transform: uppercase;
    }}

    /* SELECT BOX */
    div[data-baseweb="select"] > div {{
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
    }}

    div[data-baseweb="select"] * {{
        color: white !important;
        font-weight: 800 !important;
    }}

    /* BUTTON */
    .stButton > button {{
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 13px 20px;
        background: linear-gradient(
            90deg,
            #00eaff,
            #0077ff
        );
        color: white;
        font-size: 17px;
        font-weight: 900;
        text-transform: uppercase;
        box-shadow:
            0 0 15px rgba(0, 234, 255, 0.45);
    }}

    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow:
            0 0 25px rgba(0, 234, 255, 0.70);
    }}

    /* INFO / SUCCESS BOXES */
    .stAlert {{
        background: rgba(0, 0, 0, 0.35) !important;
        backdrop-filter: blur(5px);
        border-radius: 12px;
    }}

    /* DIVIDER */
    hr {{
        border-color: rgba(255, 255, 255, 0.25) !important;
    }}

    /* FOOTER */
    .footer {{
        text-align: center;
        color: rgba(255, 255, 255, 0.75);
        font-size: 12px;
        margin-top: 30px;
        font-weight: 700;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# HEADER
# ==============================
st.markdown(
    '<div class="main-title">⚡ Rajveer Facebook Reporting Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Advanced Facebook Analytics & Reporting Dashboard</div>',
    unsafe_allow_html=True
)

st.divider()

# ==============================
# TARGET URL
# ==============================
st.markdown("### 🎯 Target Facebook Profile / Page")

target_url = st.text_input(
    "Facebook URL",
    placeholder="PASTE FACEBOOK PROFILE OR PAGE URL HERE"
)

# ==============================
# REPORT REASONS
# ==============================
st.markdown("### 🚨 Report Reasons")

report_reasons = st.multiselect(
    "SELECT REPORT REASONS",
    [
        "HARASSMENT OR BULLYING",
        "HATE SPEECH",
        "IMPERSONATION",
        "SCAM OR FRAUD",
        "VIOLENCE OR THREATS",
        "SPAM",
        "PRIVACY ISSUE",
        "OTHER"
    ],
    default=[
        "HARASSMENT OR BULLYING",
        "HATE SPEECH",
        "IMPERSONATION",
        "SCAM OR FRAUD",
        "VIOLENCE OR THREATS",
        "SPAM",
        "PRIVACY ISSUE",
        "OTHER"
    ]
)

# ==============================
# REPORT DETAILS
# ==============================
st.markdown("### 📝 Report Details")

details = st.text_area(
    "DESCRIBE THE ISSUE",
    placeholder="WRITE THE DETAILS OF THE ISSUE HERE...",
    height=160
)

# ==============================
# URL VALIDATION
# ==============================
def valid_facebook_url(url):
    try:
        parsed = urlparse(url)
        return (
            parsed.scheme in ["http", "https"]
            and (
                "facebook.com" in parsed.netloc.lower()
                or "fb.com" in parsed.netloc.lower()
            )
        )
    except Exception:
        return False


# ==============================
# REPORT BUTTON
# ==============================
st.markdown("###")

if st.button("🚀 START REPORTING PROCESS"):

    if not target_url.strip():
        st.error("PLEASE ENTER A FACEBOOK URL.")

    elif not valid_facebook_url(target_url.strip()):
        st.error("PLEASE ENTER A VALID FACEBOOK URL.")

    elif not report_reasons:
        st.error("PLEASE SELECT AT LEAST ONE REPORT REASON.")

    else:

        st.success("REPORT INFORMATION PREPARED SUCCESSFULLY.")

        st.markdown("### 📋 REPORT SUMMARY")

        st.write("**TARGET URL:**")
        st.code(target_url.strip())

        st.write("**SELECTED REASONS:**")

        for reason in report_reasons:
            st.write(f"• {reason}")

        if details.strip():
            st.write("**REPORT DETAILS:**")
            st.write(details)

        st.info(
            "OPEN THE TARGET PROFILE/PAGE ON FACEBOOK AND USE FACEBOOK'S "
            "OFFICIAL REPORT OPTION TO SUBMIT THE REPORT."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )

# ==============================
# FOOTER
# ==============================
st.markdown(
    """
    <div class="footer">
        RAJVEER FACEBOOK REPORTING TOOL<br>
        THIS TOOL DOES NOT COLLECT FACEBOOK PASSWORDS,
        SESSION COOKIES OR LOGIN CREDENTIALS.
    </div>
    """,
    unsafe_allow_html=True
)
