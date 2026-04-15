import streamlit as st
import yt_dlp
import os

# پیج سیٹنگز
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# کسٹم ڈیزائن (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    .header-box {
        background-color: #1e3d59;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ہیڈر
st.markdown("""
    <div class="header-box">
        <h1>🚀 TOOLRY DOWNLOADER</h1>
        <p>BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA | WhatsApp: 00447704578383</p>
    </div>
    """, unsafe_allow_html=True)

# سیشن اسٹیٹ چیک کرنا (لنک مٹانے کے لیے)
if 'url_input' not in st.session_state:
    st.session_state.url_input = ""

# لنک ان پٹ باکس
url = st.text_input("🔗 Paste YouTube Link:", value=st.session_state.url_input, key="url_box")

# بٹنز کے کالمز
col1, col2, col3, col4 = st.columns(4)

with col4:
    if st.button("🔴 RESET"):
        # لنک مٹانے کے لیے سیشن اسٹیٹ کو خالی کرنا
        st.session_state.url_input = ""
        st.rerun()

# اگر لنک موجود ہو تو پروسیس کریں
if url:
    st.session_state.url_input = url # لنک کو یاد رکھنا
    try:
        st.info("⚡ Processing Video Connection...")
        
        # ڈاؤن لوڈ کے لیے فائل کا نام
        save_path = "download_file.mp4"

        # 403 ایرر سے بچنے کے لیے جدید ترین سیٹنگز
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'referer': 'https://www.google.com/',
        }

        with col1:
            if st.button("📥 DOWNLOAD"):
                with st.spinner("Downloading..."):
                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])
                        
                        if os.path.exists(save_path):
                            with open(save_path, "rb") as file:
                                st.download_button(
                                    label="💾 SAVE TO DEVICE",
                                    data=file,
                                    file_name="Toolry_Video.mp4",
                                    mime="video/mp4"
                                )
                            st.success("✅ Download Ready! Click 'Save to Device'.")
                            os.remove(save_path) # سرور سے فائل مٹانا
                    except Exception as e:
                        st.error(f"Error: {e}")

    except Exception as e:
        st.error(f"Unable to process link: {e}")

with col2:
    st.button("🔄 RESUME")
with col3:
    st.button("📁 FOLDER")

st.markdown("---")
st.caption("© 2026 Skill Up Academy | Powered by Shahid Mahmood Cheema")
