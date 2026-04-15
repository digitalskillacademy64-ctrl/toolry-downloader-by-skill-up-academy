import streamlit as st
import yt_dlp
import os

# 1. پیج کی بنیادی سیٹنگز
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# 2. کسٹم ڈیزائن (CSS) - جیسا آپ کی تصویر میں تھا
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
    }
    .header-box {
        background-color: #1e3d59;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 10px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #1e3d59;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ہیڈر اور برانڈنگ
st.markdown("""
    <div class="header-box">
        <h1>🚀 TOOLRY DOWNLOADER</h1>
        <p>BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA | WhatsApp: 00447704578383</p>
    </div>
    """, unsafe_allow_html=True)

# 4. سیشن اسٹیٹ (لنک کو ری سیٹ کرنے کے لیے)
if 'url_input' not in st.session_state:
    st.session_state.url_input = ""

# 5. لنک ان پٹ باکس
url = st.text_input("🔗 Paste YouTube Link:", value=st.session_state.url_input, key="url_box", placeholder="یہاں لنک پیسٹ کریں...")

# 6. بٹنز کے کالمز
col1, col2, col3, col4 = st.columns(4)

with col1:
    download_btn = st.button("📥 DOWNLOAD")

with col2:
    st.button("🔄 RESUME")

with col3:
    st.button("📁 FOLDER")

with col4:
    if st.button("🔴 RESET"):
        # لنک مٹانے کے لیے سیشن اسٹیٹ خالی کرنا
        st.session_state.url_input = ""
        st.rerun()

# 7. ڈاؤن لوڈنگ کی مین لاجک
if url:
    # صارف کا ڈالا ہوا لنک سیشن میں محفوظ کرنا
    st.session_state.url_input = url
    
    if download_btn:
        with st.spinner("⚡ Connecting to Server using Cookies..."):
            save_path = "toolry_download.mp4"
            
            # یوٹیوب کی پابندیوں سے بچنے کے لیے فائنل سیٹنگز
            ydl_opts = {
                'format': 'best',
                'outtmpl': save_path,
                'cookiefile': 'cookies.txt',  # یہ فائل آپ نے گٹ ہب پر اپ لوڈ کر دی ہے
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                'referer': 'https://www.google.com/',
            }

            try:
                # ڈاؤن لوڈ کا عمل
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # اگر فائل ڈاؤن لوڈ ہو گئی تو صارف کو بٹن دکھائیں
                if os.path.exists(save_path):
                    with open(save_path, "rb") as file:
                        st.download_button(
                            label="💾 SAVE TO DEVICE (فائل محفوظ کریں)",
                            data=file,
                            file_name="Toolry_Video.mp4",
                            mime="video/mp4"
                        )
                    st.success("✅ ڈاؤن لوڈ مکمل! اب اوپر والے بٹن پر کلک کر کے موبائل یا پی سی میں سیو کریں۔")
                    os.remove(save_path) # سرور سے فائل مٹانا تاکہ جگہ بھر نہ جائے
            
            except Exception as e:
                st.error(f"Error: {e}")
                st.warning("اگر 403 ایرر آ رہا ہے تو اپنی cookies.txt فائل دوبارہ اپ لوڈ کریں۔")

# فوٹر
st.markdown("---")
st.caption("© 2026 Skill Up Academy | Powered by Shahid Mahmood Cheema")
