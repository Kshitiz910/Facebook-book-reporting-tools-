import streamlit as st
from urllib.parse import urlparse

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# =====================================================
# BACKGROUND IMAGE
# =====================================================

IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    f"""
    <style>

    /* ==============================
       MAIN BACKGROUND
       ============================== */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.10),
                rgba(0, 0, 0, 0.10)
            ),
            url("{IMAGE_URL}") !important;

        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    .main {{
        background: transparent !important;
    }}

    .block-container {{
        background: transparent !important;
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    /* ==============================
       TITLE
       ============================== */

    .main-title {{
        text-align: center;
        color: #00eaff;
        font-size: 40px;
        font-weight: 900;
        text-transform: uppercase;

        text-shadow:
            0 0 7px #000000,
            0 0 15px rgba(0, 234, 255, 0.8);

        margin-bottom: 5px;
    }}

    .sub-title {{
        text-align: center;
        color: white;
        font-size: 17px;
        font-weight: 900;
        text-transform: uppercase;

        text-shadow:
            0 0 6px #000000;

        margin-bottom: 25px;
    }}

    /* ==============================
       HEADINGS
       ============================== */

    h1, h2, h3 {{
        color: #ffd700 !important;
        font-weight: 900 !important;
        text-transform: uppercase;

        text-shadow:
            0 0 5px #000000,
            0 0 10px #000000;
    }}

    /* ==============================
       LABELS
       ============================== */

    label {{
        color: white !important;
        font-weight: 900 !important;
        text-shadow: 0 0 5px #000000;
    }}

    /* =================================================
       FACEBOOK URL INPUT - TRANSPARENT
       ================================================= */

    [data-testid="stTextInput"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stTextInput"] > div {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stTextInput"] [data-baseweb="input"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    [data-testid="stTextInput"] [data-baseweb="input"] > div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    [data-testid="stTextInput"] input {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;
        font-weight: 900 !important;
        font-size: 15px !important;

        box-shadow: none !important;
    }}

    /* =================================================
       REPORT REASONS - TRANSPARENT
       ================================================= */

    [data-testid="stMultiSelect"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stMultiSelect"] > div {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stMultiSelect"] [data-baseweb="select"] {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    [data-testid="stMultiSelect"] [data-baseweb="select"] div {{
        background-color: transparent !important;
    }}

    [data-testid="stMultiSelect"] input {{
        background: transparent !important;
        color: white !important;
    }}

    [data-testid="stMultiSelect"] span {{
        color: white !important;
        font-weight: 900 !important;
    }}

    /* =================================================
       REPORT DETAILS TEXTAREA - TRANSPARENT
       ================================================= */

    [data-testid="stTextArea"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stTextArea"] > div {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    [data-testid="stTextArea"] [data-baseweb="textarea"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;
        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    [data-testid="stTextArea"] [data-baseweb="textarea"] > div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    [data-testid="stTextArea"] textarea {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;
        font-weight: 900 !important;
        font-size: 15px !important;

        box-shadow: none !important;
    }}

    /* ==============================
       PLACEHOLDER
       ============================== */

    input::placeholder,
    textarea::placeholder {{
        color: rgba(255,255,255,0.90) !important;
        opacity: 1 !important;

        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* ==============================
       DROPDOWN POPUP
       ============================== */

    [data-baseweb="popover"] {{
        background: rgba(15,15,20,0.96) !important;
        border-radius: 12px !important;
    }}

    [data-baseweb="menu"] {{
        background: rgba(15,15,20,0.96) !important;
    }}

    [role="option"] {{
        color: white !important;
        font-weight: 800 !important;
    }}

    /* ==============================
       MAIN BUTTON
       ============================== */

    .stButton > button {{
        width: 100%;

        border: none !important;
        border-radius: 12px !important;

        padding: 13px 20px;

        background: linear-gradient(
            90deg,
            #00eaff,
            #0077ff
        ) !important;

        color: white !important;

        font-size: 17px !important;
        font-weight: 900 !important;

        text-transform: uppercase;

        box-shadow:
            0 0 15px rgba(0,234,255,0.55);
    }}

    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow:
            0 0 25px rgba(0,234,255,0.80);
    }}

    /* ==============================
       WHATSAPP BUTTON
       ============================== */

    div[data-testid="stLinkButton"] a {{
        width: 100% !important;

        border-radius: 12px !important;

        background: rgba(0,0,0,0.25) !important;

        border: 1px solid rgba(255,255,255,0.45) !important;

        color: white !important;

        font-weight: 900 !important;

        text-transform: uppercase;

        box-shadow: none !important;
    }}

    /* ==============================
       ALERTS
       ============================== */

    [data-testid="stAlert"] {{
        background: rgba(0,0,0,0.25) !important;

        border-radius: 12px !important;

        backdrop-filter: blur(2px);
    }}

    /* ==============================
       FOOTER
       ============================== */

    .footer-text {{
        text-align: center;

        color: white;

        font-weight: 900;

        margin-top: 30px;

        text-shadow:
            0 0 6px #000000;
    }}

    .footer-name {{
        font-size: 16px;
        margin-bottom: 5px;
    }}

    .footer-fire {{
        font-size: 15px;
        margin-bottom: 10px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">⚡ RAJVEER FACEBOOK REPORTING TOOL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">ADVANCED FACEBOOK ANALYTICS & REPORTING DASHBOARD</div>',
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# TARGET FACEBOOK PROFILE / PAGE
# =====================================================

st.markdown("### 🎯 TARGET FACEBOOK PROFILE / PAGE")

target_url = st.text_input(
    "FACEBOOK URL",
    placeholder="PASTE FACEBOOK PROFILE OR PAGE URL HERE"
)

# =====================================================
# REPORT REASONS
# =====================================================

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

# =====================================================
# REPORT DETAILS
# =====================================================

st.markdown("### 📝 REPORT DETAILS")

details = st.text_area(
    "DESCRIBE THE ISSUE",
    placeholder="WRITE THE DETAILS OF THE ISSUE HERE...",
    height=160
)

# =====================================================
# FACEBOOK URL VALIDATION
# =====================================================

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


# =====================================================
# START REPORTING PROCESS
# =====================================================

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
            "OPEN THE TARGET PROFILE OR PAGE ON FACEBOOK "
            "AND USE FACEBOOK'S OFFICIAL REPORT OPTION "
            "TO SUBMIT THE REPORT."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    '<div class="footer-text">'
    '<div class="footer-name">© 2026 CODED BY :- 𝐑𝐀𝐉𝐕𝐄𝐄𝐑</div>'
    '<div class="footer-fire">𝐀𝐋𝐖𝐀𝐘𝐒 𝐎𝐍 𝐅𝐈𝐑𝐄 ‹</div>'
    '</div>',
    unsafe_allow_html=True
)

# =====================================================
# WHATSAPP
# =====================================================

st.link_button(
    "☘ CHAT ON WHATSAPP",
    "https://wa.me/91XXXXXXXXXX"
)
