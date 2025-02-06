import os #used for processes involving the operating system
import json #used for json operations on the result
import whisper #used for Text-to-Speech recognition
import argparse #used for providing command line inputs to the program
from pathlib import Path #used for directory traversal and searching files

def find_files(directory, extensions={'.mp3', '.wav', '.mp4', '.mkv', '.flac'}):
    """This function scans a directory and its subdirectories for media files with specified extensions."""
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                media_files.append(os.path.join(root, file))
    return media_files

def process_files(file_path, model):
    """This function Processes the given media file using the Whisper model."""
    try:
        result = model.transcribe(file_path)
        return result['text']
    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")
        return None

def save_result(file_path, text, output_dir):
    """This function saves the transcription as a text file and JSON file."""
    base_name = Path(file_path).stem
    text_path = os.path.join(output_dir, f"{base_name}.txt")
    json_path = os.path.join(output_dir, f"{base_name}.json")
    
    with open(text_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump({"file": file_path, "transcription": text}, json_file, ensure_ascii=False, indent=4)
    
    print(f"Saved transcription: {text_path} and {json_path}")

def main(input_folder, output_folder):
    """Main function to process media files in the input folder."""
    os.makedirs(output_folder, exist_ok=True)
    model = whisper.load_model("tiny")  # Smallest available model
    
    media_files = find_files(input_folder)
    print(f"Found {len(media_files)} media files.")
    
    for media_file in media_files:
        print(f"Processing: {media_file}") 
        transcription = process_files(media_file, model)
        if transcription:
            save_result(media_file, transcription, output_folder)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", type=str)
    parser.add_argument("output_folder", type=str)
    
    args = parser.parse_args()

    main(args.input_folder, args.output_folder)
