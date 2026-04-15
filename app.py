import streamlit as st
import yt_dlp
import os
import re

# --- Page Config ---
st.set_page_config(page_title="Toolry Downloader", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-box {
        background: #1e3799; color: white; padding: 25px;
        text-align: center; border-radius: 12px;
    }
    .brand-sub {
        text-align: center; font-weight: bold; margin: 15px 0;
        color: #1e3799; border-bottom: 2px solid #1e3799; padding-bottom: 10px;
        font-size: 1.2em;
    }
    .done-text {
        color: #2ecc71; font-size: 60px; font-weight: bold;
        text-align: center; margin-top: 30px;
    }
    .stButton>button {
        background-color: #1e3799; color: white; border-radius: 8px;
        height: 3.5em; width: 100%; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

DOWNLOAD_PATH = os.path.join(os.getcwd(), "downloads")

# --- Branding ---
st.markdown('<div class="header-box"><h1>🚀 TOOLRY DOWNLOADER</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">BY SKILL UP ACADEMY | CEO SHAHID MAHMOOD CHEEMA | WhatsApp: 00447704578383</div>', unsafe_allow_html=True)

url = st.text_input("🔗 Paste YouTube Link:", placeholder="Paste link and it will only download the single video...")

col1, col2, col3, col4 = st.columns(4)
with col1: download_btn = st.button("📥 DOWNLOAD")
with col2: resume_btn = st.button("🔄 RESUME")
with col3: 
    if st.button("📂 FOLDER"):
        if not os.path.exists(DOWNLOAD_PATH): os.makedirs(DOWNLOAD_PATH)
        os.startfile(DOWNLOAD_PATH)
with col4:
    if st.button("🧹 RESET"): 
        st.cache_data.clear()
        st.rerun()

st.write("---")

p_bar = st.progress(0)
status_msg = st.empty()
final_done = st.empty()

def clean_ansi(text): return re.sub(r'\x1b\[[0-9;]*[mGKF]', '', str(text))

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = clean_ansi(d.get('_percent_str', '0%')).replace('%','').strip()
        speed = clean_ansi(d.get('_speed_str', 'Fast...'))
        total = clean_ansi(d.get('_total_bytes_str', d.get('_total_bytes_estimate_str', '...')))
        
        try:
            p_val = float(percent)
            p_bar.progress(p_val / 100)
            status_msg.markdown(f"### 📥 Downloading: `{percent}%` | ⚡ Speed: `{speed}` | 📦 Size: `{total}`")
        except: pass
        
    if d['status'] == 'finished':
        p_bar.progress(1.0)
        status_msg.empty()
        final_done.markdown('<p class="done-text">✅ DONE</p>', unsafe_allow_html=True)

def start_download():
    if not url:
        st.error("Link paste kren!")
        return
    
    final_done.empty()
    status_msg.info("⚡ Processing Single Video Connection...")
    
    try:
        if not os.path.exists(DOWNLOAD_PATH): os.makedirs(DOWNLOAD_PATH)
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'continuedl': True,
            'noprogress': True,
            'quiet': True,
            # اہم ترین تبدیلی: پلے لسٹ کو روکنے کے لیے
            'noplaylist': True, 
            'concurrent_fragment_downloads': 64,
            'youtube_include_dash_manifest': False,
            'cachedir': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
    except Exception as e:
        st.error(f"Error: {str(e)}")

if download_btn or resume_btn:
    start_download()