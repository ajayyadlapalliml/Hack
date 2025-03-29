import trans
import translate
import summarize
import analyze

def main(youtube_url):
    print("Starting transcription...")
    transcript_path = trans.transcribe_youtube(youtube_url)
    print(f"✅ Transcription saved to {transcript_path}")

    print("Starting translation to English...")
    translation_path = translate.translate_to_english(transcript_path)
    print(f"✅ Translation saved to {translation_path}")

    print("🚩 Starting summarization...")
    summary_path = summarize.summarize_translation(translation_path)
    print(f"✅ Summary saved to {summary_path}")

    print("🚩 Running suspect word analysis...")
    analysis_path = analyze.analyze_summary(summary_path)
    print(f"✅ Analysis saved to {analysis_path}")

if __name__ == "__main__":
    youtube_url = input("🎬 Enter the YouTube URL: ")
    main(youtube_url)
