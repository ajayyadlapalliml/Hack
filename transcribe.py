from transformers import pipeline
import librosa
import torch

audio_file = r"C:\Users\shiva\Hack\Russian News for language students 03.06.19 [DQtX1wZiSAo].wav"


# Load audio at 16 kHz
audio_data, _ = librosa.load(audio_file, sr=16000)

# Whisper pipeline setup
device = 0 if torch.cuda.is_available() else "cpu"
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base",
    device=device,
    chunk_length_s=30,
    stride_length_s=5
)

result = transcriber(audio_data, generate_kwargs={"task": "transcribe"})

# Save transcription result to text file
with open("transcription_result.txt", "w", encoding="utf-8") as f:
    f.write(result['text'])

print("✅ Transcription saved to transcription_result.txt")
