import streamlit as st
import yt_dlp
import os

# 1. پیج سیٹنگز
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# 2. کسٹم ڈیزائن (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
        background-color: #f0f2f6;
    }
    .header-box {
        background-color: #1e3d59;
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ہیڈر (آپ کی برانڈنگ)
st.markdown("""
    <div class="header-box">
        <h1>🚀 TOOLRY DOWNLOADER</h1>
        <p style='font-size: 1.1em;'>BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA</p>
        <p>WhatsApp: 00447704578383</p>
    </div>
    """, unsafe_allow_html=True)

# 4. سیشن اسٹیٹ (ری سیٹ بٹن کے لیے)
if 'video_url' not in st.session_state:
    st.session_state.video_url = ""

# 5. لنک ان پٹ باکس
url = st.text_input("🔗 Paste YouTube Link:", value=st.session_state.video_url, key="url_box")

col1, col2, col3, col4 = st.columns(4)

with col1:
    download_btn = st.button("📥 DOWNLOAD")

with col2:
    st.button("🔄 RESUME")

with col3:
    st.button("📁 FOLDER")

with col4:
    if st.button("🔴 RESET"):
        st.session_state.video_url = ""
        st.rerun()

# 6. ڈاؤن لوڈنگ لاجک
if url:
    st.session_state.video_url = url
    if download_btn:
        with st.spinner("⚡ پروسیسنگ جاری ہے، براہ کرم انتظار کریں..."):
            save_path = "toolry_video.mp4"
            
            # کوکیز کے ساتھ جدید سیٹنگز
            ydl_opts = {
                'format': 'best',
                'outtmpl': save_path,
                'cookiefile': 'cookies.txt',  # جو فائل آپ نے ابھی اپ لوڈ کی ہے
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists(save_path):
                    with open(save_path, "rb") as file:
                        st.download_button(
                            label="💾 SAVE TO DEVICE (محفوظ کریں)",
                            data=file,
                            file_name="Toolry_Video.mp4",
                            mime="video/mp4"
                        )
                    st.success("✅ ویڈیو تیار ہے! اب 'SAVE TO DEVICE' بٹن پر کلک کریں۔")
                    os.remove(save_path) # عارضی فائل صاف کرنا
            
            except Exception as e:
                st.error(f"Error: {e}")
                st.warning("اگر ایرر برقرار ہے تو چیک کریں کہ cookies.txt فائل صحیح طرح اپ لوڈ ہوئی ہے۔")

# فوٹر
st.markdown("---")
st.caption("© 2026 Skill Up Academy | Powered by Shahid Mahmood Cheema")
