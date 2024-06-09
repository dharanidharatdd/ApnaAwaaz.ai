import streamlit as st 

st.set_page_config(page_title="ApnaAwaaz.Ai", page_icon=":studio_microphone:")

st.title(":studio_microphone:" + ":notes:" + " :rainbow[ApnaAwaaz.Ai]")

# side-bar 
st.sidebar.header(("About ApnaAwaaz.Ai"))
st.sidebar.markdown((
    """
    **Empower your voice,amplify your potential** \n 
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

import streamlit as st

def uploaded_audio_mime(audio_type):
  # Function to get audio MIME type from file type string
  mime_types = {
      "audio/wav": [".wav"],
      "audio/mpeg": [".mp3"],
      # Add more audio formats as needed
  }
  for mimetype, extensions in mime_types.items():
    if any(ext in audio_type for ext in extensions):
      return mimetype
  return "Unknown"  # Handle unsupported formats


st.header("Select a voice:")
# Voice Selection (Placeholder)
voice_options = ["Your Voice (Coming Soon)", "Narendra Modi", "Voice 2 (Example)"]  
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


uploaded_audio_file = st.file_uploader("audio sample can be dialogues, songs or your own voice", type=["wav", "mpeg", "mp3"])

if uploaded_audio_file is not None:
  # Check if a file was uploaded
  filename = uploaded_audio_file.name
  filetype = uploaded_audio_mime(uploaded_audio_file.type)
  
  # Print file type for debugging
  print(f"Uploaded file type: {filetype}")

  # Process and play the uploaded audio
  bytes_data = uploaded_audio_file.read()
  st.header("Woohoo! Your audio is generated. Give it a listen!")
  st.audio(bytes_data)

  
