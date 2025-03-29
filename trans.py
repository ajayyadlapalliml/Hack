import os
import librosa
import torch
from transformers import pipeline
import yt_dlp

def transcribe_youtube(url):
    audio_folder = "audio_files"
    os.makedirs(audio_folder, exist_ok=True)

    # Download audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(audio_folder, 'audio.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    audio_file = os.path.join(audio_folder, 'audio.wav')

    # Load audio
    audio_data, _ = librosa.load(audio_file, sr=16000)

    device = 0 if torch.cuda.is_available() else "cpu"
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base",
                           device=device, chunk_length_s=30, stride_length_s=5)

    result = transcriber(audio_data, generate_kwargs={"task": "transcribe"})

    transcript_file = os.path.join("outputs", "transcription_result.txt")
    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(result['text'])

    return transcript_file
