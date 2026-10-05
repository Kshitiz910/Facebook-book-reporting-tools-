import streamlit as st
from urllib.parse import urlparse

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# =========================================================
# BACKGROUND IMAGE
# =========================================================

IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       BACKGROUND
       ===================================================== */

    html,
    body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .main,
    .block-container {{
        background-color: transparent !important;
    }}

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.08),
                rgba(0, 0, 0, 0.08)
            ),
            url("{IMAGE_URL}") !important;

        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    .block-container {{
        max-width: 900px !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }}


    /* =====================================================
       MAIN TITLE - ROYAL BLUE SHINE
       ===================================================== */

    .main-title {{
        text-align: center;

        color: #4169E1 !important;

        font-size: 40px;
        font-weight: 900;

        text-transform: uppercase;

        text-shadow:
            0 0 3px #ffffff,
            0 0 8px #4169E1,
            0 0 18px #4169E1,
            0 0 30px #1E40FF;

        animation: royalShine 2s ease-in-out infinite alternate;

        margin-bottom: 5px;
    }}

    @keyframes royalShine {{

        from {{
            text-shadow:
                0 0 3px #ffffff,
                0 0 8px #4169E1,
                0 0 18px #4169E1,
                0 0 25px #1E40FF;
        }}

        to {{
            text-shadow:
                0 0 5px #ffffff,
                0 0 12px #4169E1,
                0 0 25px #4169E1,
                0 0 40px #1E40FF;
        }}
    }}


    /* =====================================================
       SUB TITLE
       ===================================================== */

    .sub-title {{
        text-align: center;

        color: white !important;

        font-size: 17px;
        font-weight: 900;

        text-transform: uppercase;

        text-shadow: 0 0 6px #000000;

        margin-bottom: 25px;
    }}


    /* =====================================================
       SECTION HEADINGS - CYAN GLOW
       ===================================================== */

    h1,
    h2,
    h3 {{
        color: #00E5FF !important;

        font-weight: 900 !important;

        text-transform: uppercase;

        text-shadow:
            0 0 3px #FFFFFF,
            0 0 8px #00E5FF,
            0 0 18px #00BFFF,
            0 0 30px rgba(0,229,255,0.75);

        animation: headingGlow 2.5s ease-in-out infinite alternate;
    }}

    @keyframes headingGlow {{

        from {{
            text-shadow:
                0 0 3px #FFFFFF,
                0 0 8px #00E5FF,
                0 0 18px #00BFFF;
        }}

        to {{
            text-shadow:
                0 0 5px #FFFFFF,
                0 0 12px #00E5FF,
                0 0 25px #00BFFF,
                0 0 35px rgba(0,229,255,0.8);
        }}
    }}


    /* =====================================================
       LABELS
       ===================================================== */

    label {{
        color: white !important;
        font-weight: 900 !important;

        text-shadow:
            0 0 5px #000000;
    }}


    /* =====================================================
       FACEBOOK URL BOX - TRANSPARENT
       ===================================================== */

    div[data-testid="stTextInput"],
    div[data-testid="stTextInput"] > div,
    div[data-testid="stTextInput"] > div > div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"]
    div[data-baseweb="input"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;

        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"]
    div[data-baseweb="input"] > div,
    div[data-testid="stTextInput"]
    div[data-baseweb="input"] div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"] input {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;

        font-size: 15px !important;
        font-weight: 900 !important;

        box-shadow: none !important;
        outline: none !important;
    }}


    /* =====================================================
       REPORT REASONS - TRANSPARENT
       ===================================================== */

    div[data-testid="stMultiSelect"],
    div[data-testid="stMultiSelect"] > div,
    div[data-testid="stMultiSelect"] > div > div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    div[data-testid="stMultiSelect"]
    div[data-baseweb="select"] {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    div[data-testid="stMultiSelect"]
    div[data-baseweb="select"] > div {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;

        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stMultiSelect"]
    div[data-baseweb="select"] > div > div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    div[data-testid="stMultiSelect"]
    div[data-baseweb="select"] div {{
        background-color: transparent !important;
    }}

    div[data-testid="stMultiSelect"] input {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;
    }}

    div[data-testid="stMultiSelect"] span {{
        color: white !important;
        font-weight: 900 !important;
    }}


    /* =====================================================
       DROPDOWN OPTIONS
       ===================================================== */

    div[data-baseweb="popover"] {{
        background: rgba(15,15,20,0.96) !important;
        border-radius: 12px !important;
    }}

    div[data-baseweb="menu"] {{
        background: rgba(15,15,20,0.96) !important;
    }}

    div[data-baseweb="menu"] [role="option"] {{
        background: transparent !important;
        color: white !important;
        font-weight: 800 !important;
    }}

    div[data-baseweb="menu"] [role="option"]:hover {{
        background: rgba(0,229,255,0.15) !important;
    }}


    /* =====================================================
       REPORT DETAILS - TRANSPARENT
       ===================================================== */

    div[data-testid="stTextArea"],
    div[data-testid="stTextArea"] > div,
    div[data-testid="stTextArea"] > div > div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"]
    div[data-baseweb="textarea"] {{
        background: transparent !important;
        background-color: transparent !important;

        border: 1px solid rgba(255,255,255,0.55) !important;

        border-radius: 12px !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"]
    div[data-baseweb="textarea"] > div,
    div[data-testid="stTextArea"]
    div[data-baseweb="textarea"] div {{
        background: transparent !important;
        background-color: transparent !important;

        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"] textarea {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;

        font-size: 15px !important;
        font-weight: 900 !important;

        box-shadow: none !important;
        outline: none !important;
    }}


    /* =====================================================
       PLACEHOLDER
       ===================================================== */

    input::placeholder,
    textarea::placeholder {{
        color: rgba(255,255,255,0.90) !important;
        opacity: 1 !important;

        font-weight: 900 !important;
        text-transform: uppercase;
    }}


    /* =====================================================
       MAIN BUTTON
       ===================================================== */

    .stButton > button {{
        width: 100% !important;

        min-height: 58px !important;

        border: none !important;

        border-radius: 14px !important;

        background:
            linear-gradient(
                90deg,
                #00eaff,
                #0077ff
            ) !important;

        color: white !important;

        font-size: 17px !important;

        font-weight: 900 !important;

        text-transform: uppercase;

        box-shadow:
            0 0 18px rgba(0,234,255,0.55) !important;
    }}

    .stButton > button:hover {{
        transform: scale(1.02);

        box-shadow:
            0 0 28px rgba(0,234,255,0.80) !important;
    }}


    /* =====================================================
       LINK BUTTON
       ===================================================== */

    div[data-testid="stLinkButton"] a {{
        width: 100% !important;

        border-radius: 12px !important;

        background:
            rgba(0,0,0,0.25) !important;

        border:
            1px solid rgba(255,255,255,0.45) !important;

        color: white !important;

        font-weight: 900 !important;

        text-transform: uppercase;

        box-shadow: none !important;
    }}


    /* =====================================================
       ALERTS
       ===================================================== */

    [data-testid="stAlert"] {{
        background:
            rgba(0,0,0,0.22) !important;

        border-radius: 12px !important;
    }}


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer-text {{
        text-align: center;

        color: white !important;

        margin-top: 35px;

        font-weight: 900;

        text-shadow:
            0 0 6px #000000;
    }}

    .footer-name {{
        font-size: 16px;
        margin-bottom: 7px;
    }}

    .footer-fire {{
        font-size: 15px;
        margin-bottom: 15px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">'
    '⚡ RAJVEER FACEBOOK REPORTING TOOL'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'ADVANCED FACEBOOK ANALYTICS & REPORTING DASHBOARD'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# TARGET FACEBOOK PROFILE / PAGE
# =========================================================

st.markdown(
    "### 🎯 TARGET FACEBOOK PROFILE / PAGE"
)

target_url = st.text_input(
    "FACEBOOK URL",
    placeholder="PASTE FACEBOOK PROFILE OR PAGE URL HERE"
)


# =========================================================
# REPORT REASONS
# =========================================================

st.markdown(
    "### 🚨 REPORT REASONS"
)

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


# =========================================================
# REPORT DETAILS
# =========================================================

st.markdown(
    "### 📝 REPORT DETAILS"
)

details = st.text_area(
    "DESCRIBE THE ISSUE",
    placeholder="WRITE THE DETAILS OF THE ISSUE HERE...",
    height=160
)


# =========================================================
# FACEBOOK URL VALIDATION
# =========================================================

def valid_facebook_url(url):

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ["http", "https"]
            and
            (
                "facebook.com" in parsed.netloc.lower()
                or
                "fb.com" in parsed.netloc.lower()
            )
        )

    except Exception:
        return False


# =========================================================
# START REPORTING PROCESS
# =========================================================

st.markdown("###")

if st.button("🚀 START REPORTING PROCESS"):

    if not target_url.strip():

        st.error(
            "PLEASE ENTER A FACEBOOK URL."
        )

    elif not valid_facebook_url(
        target_url.strip()
    ):

        st.error(
            "PLEASE ENTER A VALID FACEBOOK URL."
        )

    elif not report_reasons:

        st.error(
            "PLEASE SELECT AT LEAST ONE REPORT REASON."
        )

    else:

        st.success(
            "REPORT INFORMATION PREPARED SUCCESSFULLY."
        )

        st.markdown(
            "### 📋 REPORT SUMMARY"
        )

        st.write(
            "**TARGET URL:**"
        )

        st.code(
            target_url.strip()
        )

        st.write(
            "**SELECTED REASONS:**"
        )

        for reason in report_reasons:

            st.write(
                f"• {reason}"
            )

        if details.strip():

            st.write(
                "**REPORT DETAILS:**"
            )

            st.write(
                details
            )

        st.info(
            "OPEN THE TARGET PROFILE OR PAGE "
            "ON FACEBOOK AND USE FACEBOOK'S "
            "OFFICIAL REPORT OPTION TO SUBMIT "
            "THE REPORT."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer-text">'
    '<div class="footer-name">'
    '© 2026 CODED BY :- 𝐑𝐀𝐉𝐕𝐄𝐄𝐑'
    '</div>'
    '<div class="footer-fire">'
    '𝐀𝐋𝐖𝐀𝐘𝐒 𝐎𝐍 𝐅𝐈𝐑𝐄 ‹'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# WHATSAPP
# =========================================================

st.link_button(
    "☘ CHAT ON WHATSAPP",
    "https://wa.me/91XXXXXXXXXX"
)
