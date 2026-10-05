import streamlit as st
from urllib.parse import urlparse

st.set_page_config(
    page_title="Facebook Report Assistant",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Facebook Report Assistant")
st.caption("Safe reporting helper — Facebook login/cookies ki zarurat nahi.")

st.warning(
    "Facebook password, c_user, xs ya koi bhi session cookie yahan enter na karein."
)

st.subheader("1. Facebook URL")
target_url = st.text_input(
    "Profile/Post URL",
    placeholder="https://www.facebook.com/..."
)

st.subheader("2. Report Reason")
reason = st.selectbox(
    "Reason select karein",
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
    "Details",
    placeholder="Problem ko short mein explain karein."
)

def valid_facebook_url(url):
    try:
        p = urlparse(url.strip())
        host = (p.hostname or "").lower()

        return (
            p.scheme in ("http", "https")
            and (
                host == "facebook.com"
                or host.endswith(".facebook.com")
            )
        )
    except:
        return False


if st.button("🚀 Prepare Report", use_container_width=True):

    if not target_url.strip():
        st.error("Facebook URL enter karein.")

    elif not valid_facebook_url(target_url):
        st.error("Valid Facebook URL enter karein.")

    else:
        st.success("Report information ready hai.")

        st.write("### Next Step")
        st.write(
            "Facebook par target profile/post open karein, "
            "Report option select karein aur appropriate reason choose karke submit karein."
        )

        st.code(
            f"Target: {target_url.strip()}\n"
            f"Reason: {reason}\n"
            f"Details: {details.strip() or '(none)'}",
            language="text"
        )

        st.link_button(
            "Open Facebook",
            "https://www.facebook.com/",
            use_container_width=True
        )

st.divider()

st.caption(
    "This tool does not collect Facebook passwords/session cookies "
    "or automate mass reporting."
)
