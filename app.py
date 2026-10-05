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
       BACKGROUND
       ====================================== */

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

    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .main,
    .block-container {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    .block-container {{
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
            0 0 18px rgba(0,234,255,0.8);
    }}

    .sub-title {{
        text-align: center;
        color: white;
        font-size: 18px;
        font-weight: 900;
        text-transform: uppercase;
        text-shadow: 0 0 8px #000;
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
        text-shadow: 0 0 5px #000;
    }}

    /* ==================================================
       FACEBOOK URL BOX
       FULLY TRANSPARENT
       ================================================== */

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
        box-shadow: none !important;

        border: 1px solid rgba(255,255,255,0.40) !important;
        border-radius: 12px !important;
    }}

    [data-testid="stTextInput"] [data-baseweb="input"] > div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    [data-testid="stTextInput"] [data-baseweb="input"] div {{
        background-color: transparent !important;
    }}

    [data-testid="stTextInput"] input {{
        background: transparent !important;
        background-color: transparent !important;
        color: white !important;

        font-size: 15px !important;
        font-weight: 900 !important;

        box-shadow: none !important;
        outline: none !important;
    }}

    /* ==================================================
       REPORT REASONS DROPDOWN
       FULLY TRANSPARENT
       ================================================== */

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
        box-shadow: none !important;

        border: 1px solid rgba(255,255,255,0.40) !important;
        border-radius: 12px !important;
    }}

    [data-testid="stMultiSelect"] [data-baseweb="select"] div {{
        background-color: transparent !important;
    }}

    [data-testid="stMultiSelect"] input {{
        background: transparent !important;
        background-color: transparent !important;
        color: white !important;
    }}

    [data-testid="stMultiSelect"] span {{
        color: white !important;
        font-weight: 900 !important;
    }}

    /* CHOOSE OPTIONS TEXT */
    [data-testid="stMultiSelect"] [data-baseweb="select"] {{
        color: white !important;
    }}

    /* ==================================================
       REPORT DETAILS TEXTAREA
       FULLY TRANSPARENT
       ================================================== */

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
        box-shadow: none !important;

        border: 1px solid rgba(255,255,255,0.40) !important;
        border-radius: 12px !important;
    }}

    [data-testid="stTextArea"] [data-baseweb="textarea"] > div {{
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }}

    [data-testid="stTextArea"] [data-baseweb="textarea"] div {{
        background-color: transparent !important;
    }}

    [data-testid="stTextArea"] textarea {{
        background: transparent !important;
        background-color: transparent !important;

        color: white !important;

        font-size: 15px !important;
        font-weight: 900 !important;

        box-shadow: none !important;
        outline: none !important;
    }}

    /* ======================================
       PLACEHOLDER
       ====================================== */

    input::placeholder,
    textarea::placeholder {{
        color: rgba(255,255,255,0.90) !important;
        opacity: 1 !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* ======================================
       DROPDOWN POPUP
       ====================================== */

    [data-baseweb="popover"] {{
        background: rgba(15,15,20,0.95) !important;
        border-radius: 12px !important;
    }}

    [data-baseweb="menu"] {{
        background: rgba(15,15,20,0.95) !important;
    }}

    [role="option"] {{
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

        background: linear-gradient(
            90deg,
            #00eaff,
            #0077ff
        ) !important;

        color: white !important;
        font-size: 17px;
        font-weight: 900;
        text-transform: uppercase;

        box-shadow:
            0 0 15px rgba(0,234,255,0.5);
    }}

    .stButton > button:hover {{
        transform: scale(1.02);
    }}

    /* ======================================
       ALERT
       ====================================== */

    [data-testid="stAlert"] {{
        background: rgba(0,0,0,0.25) !important;
        border-radius: 12px !important;
    }}

    /* ======================================
       FOOTER
       ====================================== */

    .footer {{
        text-align: center;
        margin-top: 40px;
        padding: 20px 10px;

        color: white;
        font-weight: 800;

        text-shadow: 0 0 6px #000;
    }}

    .footer-name {{
        font-size: 16px;
        margin-bottom: 8px;
    }}

    .footer-fire {{
        font-size: 15px;
        margin-bottom: 18px;
    }}

    .whatsapp-link {{
        display: inline-block;

        padding: 11px 22px;

        border-radius: 25px;

        background: rgba(0,0,0,0.25);

        border: 1px solid rgba(255,255,255,0.35);

        color: white !important;

        text-decoration: none !important;

        font-size: 15px;
        font-weight: 900;

        backdrop-filter: blur(2px);
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
# TARGET FACEBOOK PROFILE
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
    <footer class="footer">

        <p class="footer-name">
            © 2026 CODED BY :- 𝐑𝐀𝐉𝐕𝐄𝐄𝐑
        </p>

        <p class="footer-fire">
            𝐀𝐋𝐖𝐀𝐘𝐒 𝐎𝐍 𝐅𝐈𝐑𝐄 ‹
        </p>

        <div>
            <a
                href="https://wa.me/"
                target="_blank"
                class="whatsapp-link"
            >
                ☘ CHAT ON WHATSAPP
            </a>
        </div>

    </footer>
    """,
    unsafe_allow_html=True
)
