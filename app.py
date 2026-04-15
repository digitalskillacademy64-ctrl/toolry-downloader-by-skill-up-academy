import streamlit as st
import yt_dlp
import os

# صفحے کی بنیادی سیٹنگز
st.set_page_config(page_title="Toolry Downloader", page_icon="📥", layout="wide")

# کسٹم ڈیزائن (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    .header-box {
        background-color: #1e3d59;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ہیڈر اور برانڈنگ
st.markdown(f"""
    <div class="header-box">
        <h1>BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA</h1>
        <p>WhatsApp: 00447704578383</p>
    </div>
    """, unsafe_allow_html=True)

st.title("📥 Toolry All-in-One Video Downloader")

# لنک ڈالنے کی جگہ
url = st.text_input("یوٹیوب یا کسی بھی ویڈیو کا لنک یہاں پیسٹ کریں:", placeholder="https://www.youtube.com/watch?v=...")

# بٹن لے آؤٹ
col1, col2, col3, col4 = st.columns(4)

if url:
    try:
        # ویڈیو کی معلومات حاصل کرنا
        ydl_opts_info = {
            'quiet': True,
            'no_warnings': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'video')
            thumbnail = info.get('thumbnail')

        if thumbnail:
            st.image(thumbnail, width=400)
        st.write(f"**ویڈیو کا عنوان:** {video_title}")

        with col1:
            if st.button("DOWNLOAD"):
                with st.spinner("پروسیسنگ شروع ہے..."):
                    save_path = "downloaded_video.mp4"
                    
                    # مین ڈاؤن لوڈ سیٹنگز (403 ایرر سے بچنے کے لیے)
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': save_path,
                        'quiet': True,
                        'no_warnings': True,
                        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                        'referer': 'https://www.google.com/',
                    }

                    try:
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])

                        if os.path.exists(save_path):
                            with open(save_path, "rb") as f:
                                st.download_button(
                                    label="فائل سیو کریں (Save File)",
                                    data=f,
                                    file_name=f"{video_title}.mp4",
                                    mime="video/mp4"
                                )
                            st.success("ڈاؤن لوڈنگ مکمل! اب اوپر والے بٹن سے سیو کریں۔")
                            os.remove(save_path) # سرور سے فائل صاف کرنا
                    except Exception as download_error:
                        st.error(f"ڈاؤن لوڈ میں مسئلہ آیا: {download_error}")

    except Exception as e:
        st.error(f"لنک پروسیس نہیں ہو سکا: {e}")

# باقی بٹن (ڈیزائن کے لیے)
with col2:
    st.button("RESUME")
with col3:
    st.button("FOLDER")
with col4:
    if st.button("RESET"):
        st.rerun()

st.markdown("---")
st.caption("© 2026 Skill Up by Kar e Kamal | Powered by Shahid Mahmood Cheema")
