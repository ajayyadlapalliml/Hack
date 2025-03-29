import os
from googletrans import Translator

def translate_to_english(transcript_path):
    translator = Translator()

    with open(transcript_path, "r", encoding="utf-8") as f:
        original_text = f.read()

    translation = translator.translate(original_text, dest='en')

    translation_file = os.path.join("outputs", "translated_result.txt")
    with open(translation_file, "w", encoding="utf-8") as f:
        f.write(translation.text)

    return translation_file
