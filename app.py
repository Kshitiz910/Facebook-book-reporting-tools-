import streamlit as st
from urllib.parse import urlparse

# Page Configuration
st.set_page_config(
    page_title="Rajveer Facebook Reporting Tool",
    page_icon="⚡",
    layout="centered"
)

# Your original background image
IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# Custom CSS
st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.75)),
        url('{IMAGE_URL}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.stApp, .stApp p, .stApp label, .stApp div {{
    color: #ffffff !important;
}}

.main-title {{
    text-align: center;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: #00f2fe !important;
    text-shadow: 0 0 15px rgba(0,242,254,0.9),
                 2px 2px 10px #000000;
    margin-top: 10px;
    margin-bottom: 5px;
}}

.sub-title {{
    text-align: center;
    font-size: 1.1rem;
    color: #e0e0e0 !important;
    text-shadow: 1px 1px 5px #000000;
    margin-bottom: 25px;
}}

.stApp h3 {{
    color: #ffd700 !important;
    text-shadow: 1px 1px 6px #000000;
    font-weight: 700;
}}

div[data-baseweb="input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] {{
    background-color: rgba(0,0,0,0.75) !important;
    border: 1px solid rgba(0,242,254,0.6) !important;
    border-radius: 10px !important;
}}

textarea, input {{
    color: #ffffff !important;
    font-size: 1rem !important;
}}

.stButton > button {{
    width: 100%;
    background: linear-gradient(135deg,#00f2fe 0%,#4facfe 100%) !important;
    color: #000000 !important;
    font-weight: 800 !important;
    font-size: 1.2rem !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px !important;
}}

</style>
""", unsafe_allow_html=True)


# Original Heading
st.markdown(
    "<h1 class='main-title'>⚡ Rajveer Facebook Reporting Tool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Advanced Facebook Analytics & Reporting Dashboard</p>",
    unsafe_allow_html=True
)

st.write("---")


# Target Configuration
st.subheader("🎯 Target Configuration")

target_url = st.text_input(
    "Target Facebook Profile / Post URL:",
    placeholder="https://www.facebook.com/..."
)

reason = st.selectbox(
    "Report Reason:",
    [
        "Harassment or bullying",
        "Hate speech",
        "Impersonation",
        "Scam or fraud",
        "Violence or threats",
        "Spam",
        "Privacy issue",
        "Other"
    ]
)

details = st.text_area(
    "Report Details:",
    placeholder="Problem ko short mein explain karein."
)


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


if st.button("🚀 Start Reporting Process"):

    if not target_url.strip():
        st.error("⚠️ Please enter a Facebook Profile/Post URL.")

    elif not valid_facebook_url(target_url):
        st.error("⚠️ Please enter a valid Facebook URL.")

    else:
        st.success("✅ Report information prepared successfully!")

        st.info(
            "Facebook par target profile/post open karke "
            "Facebook ke official Report option se report submit karein."
        )

        st.write("### 📋 Report Information")

        st.code(
            f"Target URL: {target_url.strip()}\n"
            f"Reason: {reason}\n"
            f"Details: {details.strip() or '(No additional details)'}",
            language="text"
        )

        st.link_button(
            "🌐 Open Facebook",
            "https://www.facebook.com/",
            use_container_width=True
        )


st.write("---")

st.caption(
    "⚠️ This tool does not collect Facebook passwords, "
    "session cookies or login credentials."
)
