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
        # Ensure the downloads directory exists
        if not os.path.exists("downloads"):
            os.makedirs("downloads")
        
        # Prepare the download command
        download_command = [
            "yt-dlp",
            youtube_url,
            "-f",
            "bestaudio",
            "-o",
            "downloads/video.%(ext)s"
        ]
        
        # Run the command and capture the output
        result = subprocess.run(
            download_command,
            text=True,  # Ensure output is in string format
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error
        )

        # Check for success or failure
        if result.returncode == 0:
            # Success: Find the downloaded file
            downloaded_files = os.listdir("downloads")
            for file in downloaded_files:
                if file.startswith("video"):
                    return os.path.join("downloads", file)
        else:
            # If the return code indicates failure, raise an error with detailed logs
            raise RuntimeError(f"Download failed. Error details:\n{result.stderr}")
    except Exception as e:
        # Return the error message to be displayed in the Streamlit app
        return str(e)

# Download video when a valid URL is provided
if youtube_url:
    if st.button("Download Video"):
        with st.spinner("Downloading video... Please wait."):
            video_path = download_video(youtube_url)
        
        # Check if the function returned a valid path or an error message
        if os.path.exists(video_path):
            st.success(f"Video downloaded successfully: {video_path}")
        else:
            st.error(f"An error occurred while downloading the video:\n{video_path}")
else:
    st.warning("Please enter a valid YouTube URL to proceed.", icon="⚠️")