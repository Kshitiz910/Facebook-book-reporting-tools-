import streamlit as st
from urllib.parse import urlparse

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# ==========================================
# BACKGROUND IMAGE
# ==========================================
IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown(
    f"""
    <style>

    /* ======================================
       FULL BACKGROUND
       ====================================== */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.12),
                rgba(0, 0, 0, 0.12)
            ),
            url("{IMAGE_URL}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* REMOVE STREAMLIT DEFAULT BACKGROUND */
    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    [data-testid="stToolbar"] {{
        background: transparent !important;
    }}

    .main {{
        background: transparent !important;
    }}

    .block-container {{
        background: transparent !important;
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* ======================================
       TITLE
       ====================================== */

    .main-title {{
        text-align: center;
        color: #00eaff;
        font-size: 42px;
        font-weight: 900;
        text-transform: uppercase;

        text-shadow:
            0 0 8px #000,
            0 0 15px rgba(0, 234, 255, 0.8);

        margin-bottom: 5px;
    }}

    .sub-title {{
        text-align: center;
        color: white;
        font-size: 18px;
        font-weight: 900;
        text-transform: uppercase;

        text-shadow:
            0 0 5px #000,
            0 0 10px #000;

        margin-bottom: 30px;
    }}

    /* ======================================
       HEADINGS
       ====================================== */

    h1, h2, h3 {{
        color: #ffd700 !important;
        font-weight: 900 !important;
        text-transform: uppercase;

        text-shadow:
            0 0 5px #000,
            0 0 10px #000;
    }}

    /* ======================================
       LABELS
       ====================================== */

    label {{
        color: white !important;
        font-weight: 900 !important;
        text-shadow:
            0 0 5px #000;
    }}

    /* ======================================
       TEXT INPUT - COMPLETELY TRANSPARENT
       ====================================== */

    div[data-testid="stTextInput"] {{
        background: transparent !important;
    }}

    div[data-testid="stTextInput"] > div {{
        background: transparent !important;
    }}

    div[data-testid="stTextInput"] div[data-baseweb="input"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.45) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"] div[data-baseweb="input"] > div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"] input {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;
        font-weight: 900 !important;
        font-size: 15px !important;

        box-shadow: none !important;
    }}

    /* ======================================
       TEXTAREA - COMPLETELY TRANSPARENT
       ====================================== */

    div[data-testid="stTextArea"] {{
        background: transparent !important;
    }}

    div[data-testid="stTextArea"] > div {{
        background: transparent !important;
    }}

    div[data-testid="stTextArea"] div[data-baseweb="textarea"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.45) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"] div[data-baseweb="textarea"] > div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"] textarea {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;
        font-weight: 900 !important;
        font-size: 15px !important;

        box-shadow: none !important;
    }}

    /* ======================================
       PLACEHOLDER TEXT
       ====================================== */

    input::placeholder,
    textarea::placeholder {{
        color: rgba(255,255,255,0.88) !important;
        opacity: 1 !important;

        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* ======================================
       SELECT / DROPDOWN
       ====================================== */

    div[data-testid="stMultiSelect"] {{
        background: transparent !important;
    }}

    div[data-testid="stMultiSelect"] > div {{
        background: transparent !important;
    }}

    div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.45) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stMultiSelect"] input {{
        background: transparent !important;
        color: white !important;
    }}

    div[data-testid="stMultiSelect"] span {{
        color: white !important;
        font-weight: 900 !important;
    }}

    /* ======================================
       DROPDOWN POPUP
       ====================================== */

    div[data-baseweb="popover"] {{
        background: rgba(15,15,20,0.92) !important;
        border-radius: 12px !important;
    }}

    div[data-baseweb="menu"] {{
        background: rgba(15,15,20,0.92) !important;
    }}

    div[role="option"] {{
        color: white !important;
        font-weight: 800 !important;
    }}

    /* ======================================
       BUTTON
       ====================================== */

    .stButton > button {{
        width: 100%;

        border-radius: 12px;
        border: none;

        padding: 13px 20px;

        background:
            linear-gradient(
                90deg,
                #00eaff,
                #0077ff
            );

        color: white;

        font-size: 17px;
        font-weight: 900;

        text-transform: uppercase;

        box-shadow:
            0 0 15px rgba(0,234,255,0.5);
    }}

    .stButton > button:hover {{
        transform: scale(1.02);

        box-shadow:
            0 0 25px rgba(0,234,255,0.8);
    }}

    /* ======================================
       LINK BUTTON
       ====================================== */

    .stLinkButton > a {{
        width: 100%;
        border-radius: 12px !important;

        background:
            linear-gradient(
                90deg,
                #00eaff,
                #0077ff
            ) !important;

        color: white !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* ======================================
       ALERTS
       ====================================== */

    div[data-testid="stAlert"] {{
        background: rgba(0,0,0,0.30) !important;

        border-radius: 12px !important;

        backdrop-filter: blur(2px);
    }}

    /* ======================================
       DIVIDER
       ====================================== */

    hr {{
        border-color: rgba(255,255,255,0.30) !important;
    }}

    /* ======================================
       FOOTER
       ====================================== */

    .footer {{
        text-align: center;

        color: rgba(255,255,255,0.85);

        font-size: 12px;

        margin-top: 30px;

        font-weight: 800;

        text-shadow:
            0 0 5px #000;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">⚡ Rajveer Facebook Reporting Tool</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Advanced Facebook Analytics & Reporting Dashboard</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# TARGET FACEBOOK
# ==========================================

st.markdown("### 🎯 TARGET FACEBOOK PROFILE / PAGE")

target_url = st.text_input(
    "FACEBOOK URL",
    placeholder="PASTE FACEBOOK PROFILE OR PAGE URL HERE"
)

# ==========================================
# REPORT REASONS
# ==========================================

st.markdown("### 🚨 REPORT REASONS")

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
    ]
)

# ==========================================
# REPORT DETAILS
# ==========================================

st.markdown("### 📝 REPORT DETAILS")

details = st.text_area(
    "DESCRIBE THE ISSUE",
    placeholder="WRITE THE DETAILS OF THE ISSUE HERE...",
    height=160
)

# ==========================================
# URL VALIDATION
# ==========================================

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


# ==========================================
# REPORT BUTTON
# ==========================================

st.markdown("###")

if st.button("🚀 START REPORTING PROCESS"):

    if not target_url.strip():

        st.error("PLEASE ENTER A FACEBOOK URL.")

    elif not valid_facebook_url(target_url.strip()):

        st.error("PLEASE ENTER A VALID FACEBOOK URL.")

    elif not report_reasons:

        st.error("PLEASE SELECT AT LEAST ONE REPORT REASON.")

    else:

        st.success(
            "REPORT INFORMATION PREPARED SUCCESSFULLY."
        )

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
            "OPEN THE TARGET PROFILE/PAGE ON FACEBOOK "
            "AND USE FACEBOOK'S OFFICIAL REPORT OPTION "
            "TO SUBMIT THE REPORT."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )

# ==========================================
# FOOTER
# ==========================================

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
