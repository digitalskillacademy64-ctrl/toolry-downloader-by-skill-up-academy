import streamlit as st
import yt_dlp
import os

# 1. پیج کی بنیادی سیٹنگز
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# 2. خوبصورت ڈیزائن (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        color: white;
    }
    .header-box {
        background-color: #1e3d59;
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ہیڈر سیکشن
st.markdown("""
    <div class="header-box">
        <h1>🚀 TOOLRY DOWNLOADER</h1>
        <p style='font-size: 1.2em; margin-bottom: 5px;'>BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA</p>
        <p style='font-size: 1.1em;'>WhatsApp: 00447704578383</p>
    </div>
    """, unsafe_allow_html=True)

# 4. لنک مٹانے (Clear Link) کی لاجک
if 'video_url' not in st.session_state:
    st.session_state.video_url = ""

def clear_url():
    st.session_state.video_url = ""

# 5. لنک ان پٹ باکس
url = st.text_input("🔗 Paste YouTube or TikTok Link Here:", value=st.session_state.video_url, key="url_box")

# 6. کنٹرول بٹنز
col1, col2, col3, col4 = st.columns(4)

with col1:
    download_btn = st.button("📥 DOWNLOAD")

with col2:
    # Reset کی جگہ Clear Link بٹن
    if st.button("🗑️ CLEAR LINK"):
        clear_url()
        st.rerun()

with col3:
    st.button("🔄 RESUME")

with col4:
    st.button("📁 FOLDER")

# 7. ڈاؤن لوڈنگ کا عمل
if url:
    st.session_state.video_url = url
    if download_btn:
        with st.spinner("⚡ پروسیسنگ ہو رہی ہے، براہ کرم انتظار کریں..."):
            save_path = "toolry_video.mp4"
            
            # یوٹیوب اور کوکیز کے لیے ایڈوانس آپشنز
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': save_path,
                'cookiefile': 'cookies.txt',  # کوکیز فائل کا استعمال
                'noplaylist': True,           # پلے لسٹ کو نظر انداز کرے گا
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists(save_path):
                    with open(save_path, "rb") as file:
                        st.download_button(
                            label="💾 CLICK TO SAVE VIDEO",
                            data=file,
                            file_name="Toolry_Video.mp4",
                            mime="video/mp4"
                        )
                    st.success("✅ ویڈیو تیار ہے! اوپر والے بٹن سے محفوظ کریں۔")
                    os.remove(save_path) # عارضی فائل ڈیلیٹ کرنا
            
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("مشورہ: اگر ایرر آئے تو چیک کریں کہ لنک پلے لسٹ کا نہ ہو اور cookies.txt فائل اپ ڈیٹ ہو۔")

# فوٹر
st.markdown("---")
st.caption("© 2026 Skill Up Digital Academy | Shahid Mahmood Cheema")
