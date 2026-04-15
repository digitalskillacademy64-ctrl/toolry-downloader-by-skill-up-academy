import streamlit as st
import yt_dlp
import os
import re

# Page Configuration
st.set_page_config(page_title="Toolry Downloader", page_icon="🚀", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 TOOLRY DOWNLOADER")
st.markdown("### BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA")
st.write("WhatsApp: 00447704578383")

# Initialize Session State for URL
if 'url_input' not in st.session_state:
    st.session_state.url_input = ""

def clear_text():
    st.session_state.url_input = ""

# Layout Columns
col1, col2 = st.columns([4, 1])

with col1:
    url = st.text_input("Paste YouTube Link (Supports Playlists):", key="url_input", placeholder="https://www.youtube.com/watch?v=...")

with col2:
    st.write("##") # Spacing
    st.button("CLEAR LINK", on_click=clear_text)

if url:
    if st.button("DOWNLOAD"):
        try:
            with st.spinner("Processing... Please wait."):
                save_path = "downloaded_video.mp4"
                
                # Playlist Friendly Settings
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': save_path,
                    'cookiefile': 'cookies.txt',
                    'noplaylist': False,  # پلے لسٹ سپورٹ آن کر دی گئی ہے
                    'playlist_items': '1', # پلے لسٹ میں سے صرف مطلوبہ ویڈیو لے گا
                    'nocheckcertificate': True,
                    'quiet': True,
                    'no_warnings': True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Provide Download Link
                if os.path.exists(save_path):
                    with open(save_path, "rb") as file:
                        st.video(file)
                        st.download_button(
                            label="📥 CLICK HERE TO SAVE TO DEVICE",
                            data=file,
                            file_name="Toolry_Video.mp4",
                            mime="video/mp4"
                        )
                    os.remove(save_path) # Cleanup
                else:
                    st.error("Error: Video file not found.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("فائل صحیح طرح اپ لوڈ ہونی چاہیے۔ اگر ایرر برقرار ہے تو cookies.txt چیک کریں۔")
