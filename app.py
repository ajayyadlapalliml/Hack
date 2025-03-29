import streamlit as st
import trans
import translate
import summarize
import analyze

st.set_page_config(page_title="AI Threat Detection", layout="centered")

st.title("🛡️ Threat Tracer")
st.markdown("Enter a URL and analyze it for potential threats based on transcription, translation, and keyword detection.")

youtube_url = st.text_input("🔗 Enter URL")

if st.button("Analyze") and youtube_url:
    with st.spinner("Transcribing..."):
        transcript_path = trans.transcribe_youtube(youtube_url)
        st.success("✅ Transcription complete")

    with open(transcript_path, "r", encoding="utf-8") as f:
        st.text_area("📄 Transcription", f.read(), height=200)

    with st.spinner("Translating..."):
        translation_path = translate.translate_to_english(transcript_path)
        st.success("✅ Translation complete")

    with open(translation_path, "r", encoding="utf-8") as f:
        st.text_area("🌐 Translation", f.read(), height=200)

    with st.spinner("Summarizing..."):
        summary_path = summarize.summarize_translation(translation_path)
        st.success("✅ Summary complete")

    with open(summary_path, "r", encoding="utf-8") as f:
        summary_text = f.read()
        st.text_area("📝 Summary", summary_text, height=200)

    with st.spinner("Analyzing for threat keywords..."):
        analysis_path = analyze.analyze_summary(summary_path)
        st.success("✅ Analysis complete")

    with open(analysis_path, "r", encoding="utf-8") as f:
        analysis = f.read()

    if "Analysis Result: Suspect" in analysis:
        st.error("🚨 Threat Detected! Email alert sent.")
    else:
        st.success("✅ No threat detected.")
else:
    st.info("Paste a link above and click 'Analyze'.")
