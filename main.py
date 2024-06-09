import os
import subprocess

# Function to list available voice models
def list_voice_models(model_folder):
    return [f for f in os.listdir(model_folder) if f.endswith('.pth')]

# Function to select a voice model
def select_voice_model(models):
    print("Available Voice Models:")
    for idx, model in enumerate(models):
        print(f"{idx + 1}. {model}")
    
    model_idx = int(input("Select a model by entering its number: ")) - 1
    return models[model_idx]

# Function to upload an audio file by entering its path
def get_audio_file_path():
    audio_file_path = input("Enter the path to the audio file: ")
    return audio_file_path

# Function to perform voice conversion
def perform_voice_conversion(audio_file_path, model_path, output_path):
    command = f"python -m rvc_python -i {audio_file_path} -mp {model_path} -o {output_path}"
    print("Running voice conversion...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Voice conversion completed. Output saved to {output_path}")
        else:
            print("An error occurred during voice conversion.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    model_folder = './voice_models'  # Path to the folder containing voice models
    output_folder = './output_files'  # Path to the folder to save output files
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist
    
    # List available voice models
    models = list_voice_models(model_folder)
    if not models:
        print("No voice models found in the specified folder.")
        return
    
    # Select a voice model
    selected_model = select_voice_model(models)
    model_path = os.path.join(model_folder, selected_model)
    
    # Get the path of the audio file
    audio_file_path = get_audio_file_path()
    if not audio_file_path or not os.path.exists(audio_file_path):
        print("Invalid audio file path.")
        return
    
    # Perform voice conversion
    output_file_path = os.path.join(output_folder, f"converted_{os.path.basename(audio_file_path)}")
    perform_voice_conversion(audio_file_path, model_path, output_file_path)

if __name__ == "__main__":
    main()