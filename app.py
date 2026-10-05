import streamlit as st
from urllib.parse import urlparse
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# =========================
# BACKGROUND IMAGE
# =========================
IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# =========================
# CSS
# =========================
st.markdown(f"""
<style>

.stApp {{
    background:
        linear-gradient(rgba(0,0,0,0.28), rgba(0,0,0,0.28)),
        url("{IMAGE_URL}") center center / cover fixed no-repeat;
}}

.block-container {{
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}}

.main-title {{
    text-align: center;
    color: #4169E1;
    font-size: 38px;
    font-weight: 900;
    letter-spacing: 1px;
    text-transform: uppercase;
    animation: titleGlow 2s infinite alternate;
    text-shadow:
        0 0 5px #ffffff,
        0 0 12px #4169E1,
        0 0 25px #4169E1;
}}

.subtitle {{
    text-align: center;
    color: white;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 25px;
}}

.section-title {{
    color: #00E5FF;
    font-size: 22px;
    font-weight: 900;
    text-transform: uppercase;
    animation: cyanGlow 2s infinite alternate;
    text-shadow:
        0 0 5px #00E5FF,
        0 0 15px #00E5FF;
    margin-top: 20px;
}}

@keyframes titleGlow {{
    from {{
        text-shadow:
            0 0 5px #ffffff,
            0 0 10px #4169E1;
    }}
    to {{
        text-shadow:
            0 0 8px #ffffff,
            0 0 20px #4169E1,
            0 0 35px #4169E1;
    }}
}}

@keyframes cyanGlow {{
    from {{
        text-shadow:
            0 0 5px #00E5FF;
    }}
    to {{
        text-shadow:
            0 0 10px #00E5FF,
            0 0 25px #00E5FF;
    }}
}}

/* Text input */
.stTextInput input {{
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1px solid rgba(0,229,255,0.7) !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}}

/* Text area */
.stTextArea textarea {{
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1px solid rgba(0,229,255,0.7) !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}}

/* Multiselect main box */
div[data-baseweb="select"] > div {{
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(0,229,255,0.7) !important;
    border-radius: 12px !important;
    color: white !important;
}}

/* Multiselect selected text */
div[data-baseweb="select"] span {{
    color: white !important;
    font-weight: 700 !important;
}}

/* Dropdown popup */
div[role="listbox"] {{
    background: #111827 !important;
}}

div[role="option"] {{
    color: white !important;
    background: #111827 !important;
}}

div[role="option"]:hover {{
    background: #1f2937 !important;
}}

/* Buttons */
.stButton > button {{
    width: 100%;
    background: linear-gradient(90deg, #00bfff, #4169E1);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 17px;
    font-weight: 900;
    box-shadow:
        0 0 10px #00E5FF,
        0 0 25px rgba(0,229,255,0.5);
    transition: 0.3s;
}}

.stButton > button:hover {{
    transform: scale(1.02);
    box-shadow:
        0 0 15px #00E5FF,
        0 0 35px rgba(0,229,255,0.8);
}}

/* Link button */
.stLinkButton > a {{
    width: 100%;
    text-align: center;
    background: #128C7E !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 900 !important;
    box-shadow: 0 0 15px rgba(18,140,126,0.7);
}}

/* Summary card */
.summary-card {{
    background: rgba(0,0,0,0.65);
    border: 1px solid #00E5FF;
    border-radius: 15px;
    padding: 18px;
    margin-top: 15px;
    color: white;
    box-shadow: 0 0 15px rgba(0,229,255,0.35);
}}

.footer-text {{
    text-align: center;
    margin-top: 35px;
    color: white;
    font-weight: 800;
}}

.footer-name {{
    font-size: 15px;
}}

.footer-fire {{
    margin-top: 7px;
    font-size: 17px;
    color: #00E5FF;
    text-shadow: 0 0 10px #00E5FF;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "report_history" not in st.session_state:
    st.session_state.report_history = []

# =========================
# HEADER
# =========================
st.markdown(
    '<div class="main-title">⚡ RAJVEER FACEBOOK REPORTING TOOL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ADVANCED FACEBOOK ANALYTICS & REPORTING DASHBOARD</div>',
    unsafe_allow_html=True
)

# =========================
# FACEBOOK URL
# =========================
st.markdown(
    '<div class="section-title">🔗 FACEBOOK URL</div>',
    unsafe_allow_html=True
)

target_url = st.text_input(
    "Facebook URL",
    placeholder="https://www.facebook.com/profile-or-page",
    label_visibility="collapsed"
)

# =========================
# REPORT REASONS
# =========================
st.markdown(
    '<div class="section-title">⚠ REPORT REASONS</div>',
    unsafe_allow_html=True
)

report_reasons = [
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

selected_reasons = st.multiselect(
    "Report Reasons",
    report_reasons,
    placeholder="Select genuine report reason(s)",
    label_visibility="collapsed"
)

# =========================
# REPORT DETAILS
# =========================
st.markdown(
    '<div class="section-title">📝 REPORT DETAILS</div>',
    unsafe_allow_html=True
)

report_details = st.text_area(
    "Report Details",
    placeholder="Explain the genuine issue clearly. Add relevant evidence or details here.",
    height=150,
    label_visibility="collapsed"
)

# =========================
# VALIDATE FACEBOOK URL
# =========================
def valid_facebook_url(url):
    try:
        parsed = urlparse(url.strip())
        host = parsed.netloc.lower().split(":")[0]

        return (
            parsed.scheme in ["http", "https"]
            and (
                host == "facebook.com"
                or host.endswith(".facebook.com")
                or host == "fb.com"
                or host.endswith(".fb.com")
            )
        )
    except Exception:
        return False


# =========================
# PREPARE REPORT
# =========================
if st.button("🚀 PREPARE REPORT"):

    if not target_url.strip():
        st.error("Please enter a Facebook URL.")

    elif not valid_facebook_url(target_url):
        st.error("Please enter a valid Facebook or FB URL.")

    elif not selected_reasons:
        st.error("Please select at least one genuine report reason.")

    elif not report_details.strip():
        st.error("Please enter report details.")

    else:

        report = {
            "time": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"),
            "target": target_url.strip(),
            "reasons": selected_reasons,
            "details": report_details.strip()
        }

        st.session_state.report_history.append(report)

        st.success("✅ Report request prepared successfully.")

        st.markdown(
            f"""
            <div class="summary-card">
                <b>🎯 TARGET</b><br>
                {target_url}<br><br>

                <b>⚠ REASONS</b><br>
                {", ".join(selected_reasons)}<br><br>

                <b>📝 DETAILS</b><br>
                {report_details}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(
            "The tool prepares your report information. "
            "It does not automatically submit mass reports or force Facebook to suspend an account."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )


# =========================
# REVIEW / APPEAL
# =========================
st.markdown(
    '<div class="section-title">🔎 REVIEW / APPEAL REQUEST</div>',
    unsafe_allow_html=True
)

request_type = st.selectbox(
    "Request Type",
    [
        "ACCOUNT REVIEW REQUEST",
        "SUSPENSION APPEAL",
        "DISABLED ACCOUNT REVIEW",
        "CONTENT REVIEW REQUEST",
        "OTHER"
    ]
)

review_details = st.text_area(
    "Review / Appeal Details",
    placeholder="Explain why you believe the account or content should be reviewed.",
    height=130
)

if st.button("⏳ PREPARE REVIEW / APPEAL REQUEST"):

    if not target_url.strip():
        st.error("Please enter the Facebook URL above.")

    elif not valid_facebook_url(target_url):
        st.error("Please enter a valid Facebook or FB URL.")

    elif not review_details.strip():
        st.error("Please enter review/appeal details.")

    else:

        st.success("✅ Review / appeal request prepared.")

        st.markdown(
            f"""
            <div class="summary-card">
                <b>📌 REQUEST TYPE</b><br>
                {request_type}<br><br>

                <b>🎯 TARGET</b><br>
                {target_url}<br><br>

                <b>📝 DETAILS</b><br>
                {review_details}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.warning(
            "Facebook makes the final decision. "
            "This tool cannot force a suspension or guarantee a 180-day review."
        )

        st.link_button(
            "🌐 OPEN FACEBOOK",
            "https://www.facebook.com/"
        )


# =========================
# REPORT HISTORY
# =========================
if st.session_state.report_history:

    st.markdown(
        '<div class="section-title">📚 REPORT HISTORY</div>',
        unsafe_allow_html=True
    )

    for i, item in enumerate(
        reversed(st.session_state.report_history),
        start=1
    ):

        with st.expander(
            f"Report #{i} — {item['time']}"
        ):

            st.write("🎯 Target:", item["target"])
            st.write("⚠ Reasons:", ", ".join(item["reasons"]))
            st.write("📝 Details:", item["details"])


# =========================
# WHATSAPP
# =========================
st.markdown("<br>", unsafe_allow_html=True)

st.link_button(
    "☘ CHAT ON WHATSAPP",
    "https://wa.me/91XXXXXXXXXX"
)

# Replace 91XXXXXXXXXX above with your WhatsApp number.


# =========================
# FOOTER
# =========================
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
