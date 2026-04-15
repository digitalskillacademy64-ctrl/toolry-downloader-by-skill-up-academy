import streamlit as st
import yt_dlp
import os

# Page Configuration
st.set_page_config(page_title="Toolry Downloader", page_icon="📥")

st.title("📥 All-in-One Video Downloader")
st.markdown("### Skill Up Academy - Toolry Project")

# URL Input
url = st.text_input("ویڈیو کا لنک یہاں پیسٹ کریں:")

if url:
    try:
        # Get video info first
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            video_title = info.get('title', 'video')
            st.write(f"**Video Title:** {video_title}")

        if st.button("Download Video"):
            st.info("فائل پروسیس ہو رہی ہے، براہ کرم انتظار کریں...")
            
            # Download options
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloaded_video.%(ext)s',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            # Show download button to user
            with open("downloaded_video.mp4", "rb") as file:
                st.download_button(
                    label="اپنے کمپیوٹر میں سیو کریں",
                    data=file,
                    file_name=f"{video_title}.mp4",
                    mime="video/mp4"
                )
            st.success("ڈاؤن لوڈ مکمل ہو گیا!")

    except Exception as e:
        st.error(f"Error: لنک درست نہیں ہے یا نیٹ ورک کا مسئلہ ہے۔")
