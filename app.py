import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages easily.")

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN"
}

if "history" not in st.session_state:
    st.session_state.history = []

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"

text = st.text_area("Enter Text", height=150)

st.caption(f"Characters: {len(text)}")

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=list(languages.keys()).index(st.session_state.source_lang)
    )

with col3:
    target_lang = st.selectbox(
        "Target Language",
        [lang for lang in languages.keys() if lang != "Auto Detect"],
        index=[lang for lang in languages.keys() if lang != "Auto Detect"].index(st.session_state.target_lang)
    )

with col2:
    st.write("")
    st.write("")
    if st.button("🔄 Swap"):
        if source_lang != "Auto Detect":
            st.session_state.source_lang = target_lang
            st.session_state.target_lang = source_lang
            st.rerun()
        else:
            st.warning("Auto Detect cannot be swapped.")
if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.subheader("Translated Text")
            st.success(translated)

            st.session_state.history.append({
                "from": source_lang,
                "to": target_lang,
                "original": text,
                "translated": translated
            })

            st.download_button(
                label="📥 Download Translation",
                data=translated,
                file_name="translation.txt",
                mime="text/plain"
            )

            try:
                tts = gTTS(translated, lang=languages[target_lang])
                tts.save("translated.mp3")

                with open("translated.mp3", "rb") as audio_file:
                    st.audio(audio_file.read(), format="audio/mp3")

                os.remove("translated.mp3")

            except:
                st.info("Audio is not available for this language.")

        except Exception as e:
            st.error("Translation failed. Try another language pair.")

    else:
        st.warning("Please enter some text.")

if st.session_state.history:
    st.subheader("📜 Translation History")

    for item in reversed(st.session_state.history[-5:]):
        with st.expander(f"{item['from']} → {item['to']}"):
            st.write("Original:")
            st.info(item["original"])
            st.write("Translated:")
            st.success(item["translated"])