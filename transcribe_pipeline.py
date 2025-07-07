import os
import subprocess
import whisper
from glob import glob
from pathlib import Path

AUDIO_FILE = "my_audio.wav"   
CHUNK_DIR = "chunks"
CHUNK_LENGTH_SEC = 600      
MODEL_NAME = "base"           
OUTPUT_FILE = "final_transcription.txt"

def split_audio(input_file, output_dir, chunk_length=600):
    os.makedirs(output_dir, exist_ok=True)
    ext = Path(input_file).suffix  
    command = [
        "ffmpeg",
        "-i", input_file,
        "-f", "segment",
        "-segment_time", str(chunk_length),
        "-c", "copy",
        f"{output_dir}/chunk_%03d{ext}"
    ]
    print(" Splitting audio with ffmpeg...")
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f" Audio split into chunks in '{output_dir}'")

def transcribe_chunks(model_name, chunk_dir):
    print(f" Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)
    transcripts = []

    chunk_files = sorted(glob(f"{chunk_dir}/chunk_*.*"))  
    for file in chunk_files:
        print(f" Transcribing: {file}")
        result = model.transcribe(file)
        transcripts.append(result["text"])

    return transcripts

def save_transcript(transcripts, output_file):
    print(f" Saving final transcript to: {output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(transcripts))
    print("Done!")

if __name__ == "__main__":
    if not Path(AUDIO_FILE).exists():
        print(f"[❌] Audio file not found: {AUDIO_FILE}")
    else:
        split_audio(AUDIO_FILE, CHUNK_DIR, CHUNK_LENGTH_SEC)
        transcripts = transcribe_chunks(MODEL_NAME, CHUNK_DIR)
        save_transcript(transcripts, OUTPUT_FILE)
