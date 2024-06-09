import streamlit as st
import subprocess
import ffmpeg
import os

def download_video(video_url, output_path='downloaded_video.mp4'):
    ydl_command = [
        'yt-dlp',
        '-f', 'best',
        '-o', output_path,
        video_url
    ]
    try:
        result = subprocess.run(ydl_command, capture_output=True, text=True)
        if result.returncode == 0:
            return output_path
        else:
            st.error(f"Error downloading video: {result.stderr}")
            return None
    except Exception as e:
        st.error(f"Exception occurred: {e}")
        return None

def extract_audio(video_path, audio_path='extracted_audio.mp3', duration=60):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, t=duration, format='mp3')
            .run()
        )
        return audio_path
    except ffmpeg.Error as e:
        st.error(f"Error extracting audio: {e}")
        return None

def extract_thumbnail(video_path, thumbnail_path='thumbnail.jpg', timestamp='00:00:01'):
    try:
        (
            ffmpeg
            .input(video_path, ss=timestamp)
            .output(thumbnail_path, vframes=1)
            .run()
        )
        return thumbnail_path
    except ffmpeg.Error as e:
        st.error(f"Error extracting thumbnail: {e}")
        return None

st.title("YouTube Video & Thumbnail Extractor")

video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = video_url.split('v=')[-1]
    
    # Download the video
    video_path = download_video(video_url)
    
    if video_path:
        # Extract and display the thumbnail
        thumbnail_path = extract_thumbnail(video_path)
        
        if thumbnail_path:
            st.image(thumbnail_path, caption='Thumbnail')
        
        # Extract audio for 1 minute
        audio_path = extract_audio(video_path, duration=60)
        if audio_path:
            st.write("Audio extracted:")
            st.audio(audio_path, format='audio/mp3')
            os.remove(audio_path)  # Cleanup
        
        # Cleanup
        os.remove(video_path)
        os.remove(thumbnail_path)
    else:
        st.error("Failed to download video. Please check the URL and try again.")
