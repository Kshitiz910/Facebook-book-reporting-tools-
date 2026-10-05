import streamlit as st
from urllib.parse import urlparse
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# =========================================================
# BACKGROUND
# =========================================================

IMAGE_URL = (
    "https://i.postimg.cc/tCMXTHs3/"
    "ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"
)

# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
    <style>

    html, body,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .main,
    .block-container {{
        background: transparent !important;
    }}

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0,0,0,0.08),
                rgba(0,0,0,0.08)
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
       TITLE
       ===================================================== */

    .main-title {{
        text-align: center;
        color: #4169E1 !important;
        font-size: 40px;
        font-weight: 900;
        text-transform: uppercase;

        text-shadow:
            0 0 3px #fff,
            0 0 8px #4169E1,
            0 0 18px #4169E1,
            0 0 30px #1E40FF;

        animation: royalShine 2s ease-in-out infinite alternate;
        margin-bottom: 5px;
    }}

    @keyframes royalShine {{
        from {{
            text-shadow:
                0 0 3px #fff,
                0 0 8px #4169E1,
                0 0 18px #4169E1;
        }}

        to {{
            text-shadow:
                0 0 5px #fff,
                0 0 12px #4169E1,
                0 0 25px #4169E1,
                0 0 40px #1E40FF;
        }}
    }}

    /* =====================================================
       SUBTITLE
       ===================================================== */

    .sub-title {{
        text-align: center;
        color: white !important;
        font-size: 17px;
        font-weight: 900;
        text-transform: uppercase;
        text-shadow: 0 0 6px #000;
        margin-bottom: 25px;
    }}

    /* =====================================================
       HEADINGS
       ===================================================== */

    h1, h2, h3 {{
        color: #00E5FF !important;
        font-weight: 900 !important;
        text-transform: uppercase;

        text-shadow:
            0 0 3px #fff,
            0 0 8px #00E5FF,
            0 0 18px #00BFFF;

        animation: headingGlow 2.5s ease-in-out infinite alternate;
    }}

    @keyframes headingGlow {{
        from {{
            text-shadow:
                0 0 3px #fff,
                0 0 8px #00E5FF;
        }}

        to {{
            text-shadow:
                0 0 5px #fff,
                0 0 12px #00E5FF,
                0 0 25px #00BFFF;
        }}
    }}

    label {{
        color: white !important;
        font-weight: 900 !important;
        text-shadow: 0 0 5px #000;
    }}

    /* =====================================================
       INPUTS
       ===================================================== */

    div[data-testid="stTextInput"],
    div[data-testid="stTextInput"] > div,
    div[data-testid="stTextInput"] > div > div {{
        background: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextInput"]
    div[data-baseweb="input"] {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,.55) !important;
        border-radius: 12px !important;
    }}

    div[data-testid="stTextInput"] input {{
        background: transparent !important;
        color: white !important;
        font-weight: 900 !important;
    }}

    /* =====================================================
       SELECTBOX / MULTISELECT
       ===================================================== */

    div[data-testid="stSelectbox"] > div,
    div[data-testid="stMultiSelect"] > div {{
        background: transparent !important;
    }}

    div[data-baseweb="select"] > div {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,.55) !important;
        border-radius: 12px !important;
    }}

    div[data-testid="stMultiSelect"] span {{
        color: white !important;
        font-weight: 900 !important;
    }}

    div[data-baseweb="popover"],
    div[data-baseweb="menu"] {{
        background: rgba(15,15,20,.97) !important;
    }}

    div[data-baseweb="menu"] [role="option"] {{
        color: white !important;
        font-weight: 800 !important;
    }}

    /* =====================================================
       TEXTAREA
       ===================================================== */

    div[data-testid="stTextArea"],
    div[data-testid="stTextArea"] > div,
    div[data-testid="stTextArea"] > div > div {{
        background: transparent !important;
        box-shadow: none !important;
    }}

    div[data-testid="stTextArea"]
    div[data-baseweb="textarea"] {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,.55) !important;
        border-radius: 12px !important;
    }}

    div[data-testid="stTextArea"] textarea {{
        background: transparent !important;
        color: white !important;
        font-weight: 900 !important;
    }}

    input::placeholder,
    textarea::placeholder {{
        color: rgba(255,255,255,.9) !important;
        opacity: 1 !important;
        font-weight: 900 !important;
    }}

    /* =====================================================
       BUTTONS
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
            0 0 18px rgba(0,234,255,.55) !important;
    }}

    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow:
            0 0 30px rgba(0,234,255,.85) !important;
    }}

    div[data-testid="stLinkButton"] a {{
        width: 100% !important;
        border-radius: 12px !important;

        background: rgba(0,0,0,.25) !important;
        border: 1px solid rgba(255,255,255,.45) !important;

        color: white !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}

    /* =====================================================
       SUMMARY CARD
       ===================================================== */

    .summary-card {{
        padding: 18px;
        margin-top: 15px;
        border-radius: 15px;

        background: rgba(0,0,0,.30);

        border: 1px solid rgba(0,229,255,.45);

        box-shadow:
            0 0 18px rgba(0,229,255,.18);
    }}

    .summary-title {{
        color: #00E5FF;
        font-size: 20px;
        font-weight: 900;
        margin-bottom: 10px;
    }}

    .summary-label {{
        color: #fff;
        font-weight: 900;
    }}

    /* =====================================================
       FOOTER
       ===================================================== */

    .footer-text {{
        text-align: center;
        color: white !important;
        margin-top: 35px;
        font-weight: 900;
        text-shadow: 0 0 6px #000;
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
# SESSION STATE
# =========================================================

if "report_history" not in st.session_state:
    st.session_state.report_history = []

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
# TARGET
# =========================================================

st.markdown("### 🎯 TARGET FACEBOOK PROFILE / PAGE")

target_url = st.text_input(
    "FACEBOOK URL",
    placeholder="PASTE FACEBOOK PROFILE OR PAGE URL HERE"
)

# =========================================================
# REPORT REASONS
# =========================================================

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
        "INTELLECTUAL PROPERTY",
        "NUDITY OR SEXUAL CONTENT",
        "OTHER"
    ]
)

# =========================================================
# EVIDENCE
# =========================================================

st.markdown("### 📎 EVIDENCE / REPORT DETAILS")

details = st.text_area(
    "DESCRIBE THE ISSUE",
    placeholder=(
        "CLEARLY DESCRIBE WHAT HAPPENED, "
        "WHY YOU BELIEVE IT VIOLATES FACEBOOK'S RULES, "
        "AND INCLUDE RELEVANT EVIDENCE..."
    ),
    height=180
)

# =========================================================
# REVIEW / APPEAL
# =========================================================

st.markdown("### ⏳ REVIEW / APPEAL REQUEST")

review_type = st.selectbox(
    "SELECT REQUEST TYPE",
    [
        "ACCOUNT REVIEW REQUEST",
        "SUSPENSION APPEAL",
        "DISABLED ACCOUNT REVIEW",
        "CONTENT REVIEW REQUEST",
        "OTHER"
    ]
)

review_details = st.text_area(
    "REVIEW / APPEAL DETAILS",
    placeholder=(
        "WRITE THE REASON FOR YOUR REVIEW OR APPEAL "
        "REQUEST HERE..."
    ),
    height=150
)

# =========================================================
# URL VALIDATION
# =========================================================

def valid_facebook_url(url):

    try:
        parsed = urlparse(url)

        hostname = parsed.netloc.lower().split(":")[0]

        return (
            parsed.scheme in ["http", "https"]
            and (
                hostname == "facebook.com"
                or hostname.endswith(".facebook.com")
                or hostname == "fb.com"
                or hostname.endswith(".fb.com")
            )
        )

    except Exception:
        return False


# =========================================================
# PREPARE REPORT
# =========================================================

st.markdown("###")

if st.button("🚀 PREPARE REPORT"):

    if not target_url.strip():

        st.error("PLEASE ENTER A FACEBOOK URL.")

    elif not valid_facebook_url(target_url.strip()):

        st.error("PLEASE ENTER A VALID FACEBOOK URL.")

    elif not report_reasons:

        st.error("PLEASE SELECT AT LEAST ONE REPORT REASON.")

    elif not details.strip():

        st.error("PLEASE DESCRIBE THE ISSUE.")

    else:

        report = {
            "time": datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            ),
            "url": target_url.strip(),
            "reasons": report_reasons,
            "details": details.strip()
        }

        st.session_state.report_history.append(report)

        st.success(
            "REPORT PREPARED SUCCESSFULLY."
        )

        st.markdown(
            f"""
            <div class="summary-card">

            <div class="summary-title">
            📋 REPORT SUMMARY
            </div>

            <div class="summary-label">
            TARGET:
            </div>

            {target_url.strip()}

            <br><br>

            <div class="summary-label">
            REASONS:
            </div>

            {"<br>".join(report_reasons)}

            <br><br>

            <div class="summary-label">
            DETAILS:
            </div>

            {details.strip()}

            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "YOUR REPORT IS PREPARED. "
            "OPEN FACEBOOK AND USE ITS OFFICIAL "
            "REPORTING OPTION TO SUBMIT IT."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )

# =========================================================
# PREPARE REVIEW REQUEST
# =========================================================

if st.button("⏳ PREPARE REVIEW / APPEAL REQUEST"):

    if not target_url.strip():

        st.error("PLEASE ENTER A FACEBOOK URL.")

    elif not valid_facebook_url(target_url.strip()):

        st.error("PLEASE ENTER A VALID FACEBOOK URL.")

    elif not review_details.strip():

        st.error(
            "PLEASE ENTER REVIEW / APPEAL DETAILS."
        )

    else:

        st.success(
            "REVIEW / APPEAL REQUEST PREPARED."
        )

        st.markdown(
            f"""
            <div class="summary-card">

            <div class="summary-title">
            📄 REVIEW REQUEST SUMMARY
            </div>

            <div class="summary-label">
            TARGET:
            </div>

            {target_url.strip()}

            <br><br>

            <div class="summary-label">
            REQUEST TYPE:
            </div>

            {review_type}

            <br><br>

            <div class="summary-label">
            DETAILS:
            </div>

            {review_details.strip()}

            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "THIS TOOL PREPARES YOUR REVIEW REQUEST. "
            "IT DOES NOT AUTOMATICALLY SUSPEND AN ACCOUNT "
            "OR GUARANTEE A 180-DAY REVIEW. "
            "FACEBOOK MAKES THE FINAL DECISION."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )

# =========================================================
# HISTORY
# =========================================================

if st.session_state.report_history:

    st.markdown("### 📊 REPORT HISTORY")

    for index, item in enumerate(
        reversed(st.session_state.report_history),
        start=1
    ):

        with st.expander(
            f"REPORT #{index} — {item['time']}"
        ):

            st.write(
                "**TARGET URL:**",
                item["url"]
            )

            st.write(
                "**REASONS:**"
            )

            for reason in item["reasons"]:
                st.write(f"• {reason}")

            st.write(
                "**DETAILS:**"
            )

            st.write(item["details"])

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
