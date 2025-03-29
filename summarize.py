import os
from transformers import pipeline

def summarize_translation(translation_path):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    with open(translation_path, "r", encoding="utf-8") as f:
        translated_text = f.read()

    # Hugging Face summarizer may have a token limit (~1024 tokens).
    # Split if your text is too long, or just summarize shorter text.

    summary = summarizer(translated_text, max_length=300, min_length=75, do_sample=False)

    summary_file = os.path.join("outputs", "summary_result.txt")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary[0]['summary_text'])

    return summary_file
