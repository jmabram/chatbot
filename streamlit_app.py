import streamlit as st
import os
import subprocess

# Title of the app
st.title("🎥 YouTube Video Transcriber")

# Instructions
st.write("Paste a YouTube video URL below to get started:")

# Input field for YouTube URL
youtube_url = st.text_input("YouTube Video URL", placeholder="https://youtu.be/example")

# Function to download YouTube video using yt-dlp
def download_video(youtube_url):
    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        
        # Run yt-dlp to download the video
        download_command = [
            "yt-dlp",
            youtube_url,
            "-f",
            "bestaudio",
            "-o",
            "downloads/video.%(ext)s"
        ]
        subprocess.run(download_command, check=True)

        downloaded_files = os.listdir("downloads")
        for file in downloaded_files:
            if file.startswith("video"):
                return os.path.join("downloads", file)
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e}"
    except Exception as e:
        return str(e)

# Download video when a valid URL is provided
if youtube_url:
    if st.button("Download Video"):
        with st.spinner("Downloading video... Please wait."):
            video_path = download_video(youtube_url)
        
        if os.path.exists(video_path):
            st.success(f"Video downloaded successfully: {video_path}")
        else:
            st.error("An error occurred while downloading the video.")