import os
import subprocess
import streamlit as st
import ffmpeg
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="ApnaAwaaz.Ai", page_icon=":studio_microphone:",layout="wide")

# side-bar 
st.sidebar.header(("About ApnaAwaaz.Ai"))
st.sidebar.markdown((
    """
    **Empower your voice, samplify your potential** \n 
    ApnaAwaaz.Ai is a revolutionary web app designed to put the power of voice in your hands. We're building an AI that learns your unique voice and empowers you.
    """
))

st.sidebar.header(("Features (Glimpse into the Future)"))
st.sidebar.markdown((
    """
**ApnaAwaaz.Ai is packed with exciting features waiting to be unveiled:**
- **Clone Your Voice in Videos:** Imagine making funny video dubs using your own voice!
- **Speak Your Mind:** Type any text, and ApniAwaaz.Ai will bring it to life using your simulated voice 
- **Train Your AI Voice:** Teach ApnaAwaaz.Ai to recognize and replicate your unique voice 
"""
))

def list_voice_models(model_folder):
    return [f for f in os.listdir(model_folder) if f.endswith('.pth')]

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottieurl("https://lottie.host/5e950871-987c-4103-a146-d4e69c6bbff3/XNSagokzkU.json")
lottie_coding2 = load_lottieurl("https://lottie.host/b66c0c8d-0a20-4e5d-b612-373d749f31fe/XxXLfbiv5A.json")

with st.container():
  left_column, right_column = st.columns(2)
  with left_column:
    st.title(":studio_microphone:" + ":notes:" + " :rainbow[ApnaAwaaz.Ai]")
    st.header("Select a voice:")

    # Voice Selection (Placeholder)
    voice_options = list_voice_models(model_folder="./voice_models")  
    selected_voice = st.selectbox("Pick one from below", voice_options)

    st.header("Upload an audio sample:")

    def uploaded_audio_mime(audio_type):
        # Function to get audio MIME type from file type string
        mime_types = {
            "audio/wav": [".wav"],
            "audio/mp3": [".mp3"],
            # Add more audio formats as needed
        }
        for mimetype, extensions in mime_types.items():
            if any(ext in audio_type for ext in extensions):
                return mimetype
        return "Unknown"  # Handle unsupported formats

    uploaded_audio_file = st.file_uploader("Audio sample can be dialogues, songs, or your own voice", type=["wav", "mp3"])
    if uploaded_audio_file is not None:
        # Check if a file was uploaded
        filename = uploaded_audio_file.name
        filetype = uploaded_audio_mime(uploaded_audio_file.type)
        
        # Process and play the uploaded audio
        bytes_data = uploaded_audio_file.read()

        model_folder = './voice_models'  # Path to the folder containing voice models
        output_folder = './output_files'  # Path to the folder to save output files
        os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

        # Get the path of the audio file
        audio_file_path = os.path.join(output_folder, filename)
        with open(audio_file_path, "wb") as f:
            f.write(bytes_data)

        # Perform voice conversion
        def perform_voice_conversion(audio_file_path, model_path, output_path):
            command = f"python -m rvc_python -i {audio_file_path} -mp {model_path} -o {output_path} --device cuda:0"
            st.write("Running voice conversion...")
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    # st.write(f"Voice conversion completed. Output saved to {output_path}")
                    st.header("Woohoo! Your audio is generated. Give it a listen!")
                    with open(output_path, "rb") as output:
                        st.audio(output.read())
                    st_lottie(lottie_coding2, height=100, key="coding2")
                else:
                    st.write("An error occurred during voice conversion.")
                    st.write(result.stderr)
            except Exception as e:
                st.write(f"An error occurred: {e}")

        model_path = os.path.join(model_folder, selected_voice)
        output_file_path = os.path.join(output_folder, f"converted_{filename}")
        perform_voice_conversion(audio_file_path, model_path, output_file_path)
    
  with right_column:
    st_lottie(lottie_coding1, height=500, key="coding1")
