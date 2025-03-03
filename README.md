# Transcript Word Cloud Project

This project provides a method to extract audio from an online video, segment the audio by speaker using Whisper Diarize, and generate a word cloud from the transcript.

## Prerequisites

- Python packages as listed in `requirements.txt`

## Installation

Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Step 1: Extract Audio from Video

Use `yt-dlp` to download and extract audio from a YouTube video:

```sh
yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 "https://www.youtube.com/watch?v=kEOv4x_FIsc" --output "audio.mp3"
```

### Step 2: Segment Audio by Speaker

Use `whisperx` to segment the audio by speaker:

```sh
whisperx ./audio.mp3 \
    --compute_type float32 \
    --diarize \
    --hf_token <YOUR_HF_TOKEN> \
    --output_dir ./output
```

### Step 3: Generate Word Cloud

The transcript can then be attributed by name to the speaker and fed to `wordcloud_from_transcript.py` to create a word cloud masked the usa and ukrainian flags.

```
python wordcloud_from_transcript.py --input ./output/audio.txt
```
