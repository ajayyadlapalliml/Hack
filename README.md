
# 🛡️ Threat Tracer – AI-Powered Threat Detection

**Threat Tracer** is an end-to-end AI pipeline that analyzes YouTube videos (or other media URLs) for potential security threats by transcribing speech, translating it to English, summarizing key information, and detecting suspicious keywords.

## 🚀 Features:

- 🎙️ **Speech-to-Text Transcription** using OpenAI Whisper (via Hugging Face)
- 🌐 **Translation** to English with Google Translate
- 📝 **Summarization** using BART (facebook/bart-large-cnn)
- 🚨 **Keyword-Based Threat Analysis** with suspect keyword detection
- 📬 **Email Alerts** if potential threats are detected
- 💻 **Streamlit Frontend** for interactive analysis
- 🧾 **Text Output Files** for all stages (transcript, translation, summary, analysis)

---

## Pipeline Overview

1. 🔗 **Input**: Paste a YouTube URL or media link
2. 🧠 **Transcription**: Convert audio to text (Whisper)
3. 🌍 **Translation**: Non-English transcripts are translated to English
4. ✂️ **Summarization**: Condense the translated text
5. ⚠️ **Threat Analysis**: Detect critical keywords (e.g., bomb, terrorism, attack)
6. 📧 **Alert**: Send an email with the summary if suspect content is found
7. 🖥️ **Streamlit App**: Visual interface to walk through all steps

---

## 📂 Project Structure

```
Hack/
├── app.py                  # Streamlit frontend
├── transcribe.py           # Transcribes YouTube audio
├── translate.py            # Translates transcript to English
├── summarize.py            # Summarizes translated content
├── analyze.py              # Analyzes summary for threat keywords & sends alert
├── outputs/                # Stores all text output files
├── audio_files/            # Temporarily stores downloaded audio
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/ajayyadlapalliml/threat-tracer.git
cd threat-tracer

# Create virtual environment
python -m venv whisper-env
.\whisper-env\Scripts activate  # On Windows

```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Paste a link and walk through each stage interactively.

---

## 🔐 Email Alert Setup

> Configure `SENDER_EMAIL`, `APP_PASSWORD`, and `RECEIVER_EMAIL` inside `analyze.py`.  
> Use a Gmail App Password (not your actual Gmail password).

---

## 🛠️ Technologies Used

- Whisper (Hugging Face Transformers)
- Googletrans
- BART Summarizer
- Regex / NLP
- Streamlit
- yt-dlp + ffmpeg
- SMTP (for Gmail alerts)

---

## 🌟 Future Enhancements

- Support real-time YouTube/any Other live stream monitoring
- Visual keyword dashboards
- PDF report export
- Cloud deployment (Streamlit Cloud, Hugging Face Spaces)
- Secure .env file for credentials

---

## 👨‍💻 Contributors

- [Ajay Yadlapalli](https://github.com/ajayyadlapalliml)
- [Shiva Teja Beerelli](https://github.com/ShivaTeja25)
- [Madhuri Duvvuri](https://github.com/madhuriduvvuri15)
- [Udaya Chandrika Gummuluri](https://github.com/chandrika2707)

---

## 📄 License

MIT License. Free to use for educational and research purposes.
