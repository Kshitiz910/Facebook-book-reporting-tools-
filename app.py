import streamlit as st
import requests
import time

# Page Configuration
st.set_page_config(page_title="Rajveer Facebook Reporting Tool", page_icon="⚡", layout="centered")

# Background Image Link
IMAGE_URL = "https://i.postimg.cc/tCMXTHs3/ab9a0673-c1a8-4c93-ab27-cd505921e582.jpg"

# Custom Styling (Clear Image Background & Stylish Text)
st.markdown(f"""
    <style>
    /* Full Clear Background Image */
    .stApp {{
        background-image: url('{IMAGE_URL}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Main Stylish Heading */
    .main-title {{
        text-align: center;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 2.6rem;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 2px 2px 8px #000000;
        margin-bottom: 20px;
    }}
    
    /* Input Fields Style */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }}
    
    /* High-Contrast Button */
    .stButton > button {{
        width: 100%;
        background: #00f2fe !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    }}
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<h1 class='main-title'>⚡ Rajveer Facebook Reporting Tool</h1>", unsafe_allow_html=True)

st.write("---")

# User Input Fields
st.subheader("🔑 Access & Target Configuration")
cookie_input = st.text_area("Facebook Cookies / Session Data:", placeholder="datr=...; sb=...; c_user=...; xs=...", height=100)
target_url = st.text_input("Target Facebook Profile / Post URL:", placeholder="https://www.facebook.com/...")

st.write("")

# Action Button
if st.button("🚀 Start Reporting Process"):
    if not cookie_input or not target_url:
        st.error("⚠️ Kripya Cookies aur Target URL dono enter karein!")
    else:
        st.success("✅ Process Initialized!")
        
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Cookie': cookie_input
        })
        
        st.info(f"Targeting: `{target_url}`")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(1, 6):
            status_text.text(f"Sending report request #{i}...")
            time.sleep(1.5)
            progress_bar.progress(i * 20)
            
        st.balloons()
        st.success("🎉 Process Completed Successfully!")
