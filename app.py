import streamlit as st
import yt_dlp
import os

# Page Configuration
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 TOOLRY DOWNLOADER")
st.markdown("### BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA")
st.write("WhatsApp: 00447704578383")

# URL Input Handling
if 'url_input' not in st.session_state:
    st.session_state.url_input = ""

def clear_text():
    st.session_state.url_input = ""

col1, col2 = st.columns([4, 1])

with col1:
    url = st.text_input("Paste YouTube Link (Playlists Supported):", key="url_input", placeholder="https://www.youtube.com/watch?v=...")

with col2:
    st.write("##") # Spacing
    st.button("CLEAR LINK", on_click=clear_text)

if url:
    if st.button("DOWNLOAD"):
        try:
            with st.spinner("📥 Downloading the best quality... Please wait."):
                save_path = "downloaded_video.mp4"
                
                # Optimized ydl_opts for Playlists and High Quality
                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'outtmpl': save_path,
                    'cookiefile': 'cookies.txt',
                    'noplaylist': False,
                    'playlist_items': '1',
                    'nocheckcertificate': True,
                    'merge_output_format': 'mp4',
                    'quiet': True,
                    'no_warnings': True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Provide Download Link
                if os.path.exists(save_path):
                    with open(save_path, "rb") as file:
                        st.success("✅ Download Ready!")
                        st.video(file)
                        st.download_button(
                            label="📥 CLICK HERE TO SAVE TO DEVICE",
                            data=file,
                            file_name="Toolry_Video.mp4",
                            mime="video/mp4"
                        )
                    os.remove(save_path) # Cleanup server space
                else:
                    st.error("Error: Could not process the video.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("مشورہ: اگر ایرر برقرار ہے تو چیک کریں کہ GitHub پر 'packages.txt' فائل میں 'ffmpeg' لکھا ہوا ہے اور وہ اسی ریپوزٹری میں موجود ہے۔")

st.markdown("---")
st.caption("© 2026 Skill Up Digital Academy | Sadiqabad, Pakistan")
