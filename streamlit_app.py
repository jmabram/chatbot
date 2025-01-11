import streamlit as st

# Title of the app
st.title("🎥 YouTube Video Transcriber")

# Instructions
st.write("Paste a YouTube video URL below to get started:")

# Input field for YouTube URL
youtube_url = st.text_input("YouTube Video URL", placeholder="https://youtu.be/example")

# Placeholder for the output (transcript area)
if youtube_url:
    st.info("Transcript will appear here once processing is added.", icon="💬")
else:
    st.warning("Please enter a valid YouTube URL to proceed.", icon="⚠️")