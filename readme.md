# Whisper Transcription Pipeline for Large Audio Files

This is a simple Python pipeline to transcribe **large audio files** (like `.wav` or `.mp3`) using [OpenAI Whisper](https://github.com/openai/whisper). It handles long files by:

1. Splitting them into chunks (e.g. every 10 minutes)
2. Transcribing each chunk with Whisper
3. Combining all transcriptions into a single `.txt` file

---

## 🔧 Requirements

- Python 3.8+
- FFmpeg (installed and in your system PATH)
- Whisper + Torch

---

## 📦 Installation

1. Clone this repo or copy the script files.
2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure FFmpeg is installed:

- **macOS**: `brew install ffmpeg`
- **Ubuntu**: `sudo apt install ffmpeg`
- **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html), and add it to your PATH.

---

## ▶️ Usage

1. Replace the `AUDIO_FILE` variable in `transcribe_pipeline.py` with your audio filename:

```python
AUDIO_FILE = "my_audio.wav"  # or .mp3, .m4a, etc.
```

2. Run the pipeline:

```bash
python transcribe_pipeline.py
```

3. Output:

- Chunked audio in `chunks/`
- Final transcript in `final_transcription.txt`

---

## 🧠 Model Options

You can change the Whisper model in the script:

```python
MODEL_NAME = "base"  # Options: tiny, base, small, medium, large
```

Larger models are slower but more accurate.

---

## 📂 File Structure

```
.
├── transcribe_pipeline.py
├── requirements.txt
├── README.md
├── chunks/                   # Automatically created
└── final_transcription.txt   # Output transcript
```

---

## 📝 To-Do / Optional Enhancements

- [ ] Add timestamps to the transcript
- [ ] Support subtitle formats (`.srt`, `.vtt`)
- [ ] Optional translation to English

---

## 🧡 Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
