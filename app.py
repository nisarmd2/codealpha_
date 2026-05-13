import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")
languages = {
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
    "Chinese": "zh-cn",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Thai": "th"
}

text = st.text_area("Enter Text")

source_lang = st.selectbox("Source Language", list(languages.keys()))
target_lang = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.subheader("Translated Text")
        st.success(translated)

        # Copy button
        if st.button("Copy Text"):
            pyperclip.copy(translated)
            st.success("Copied to clipboard!")

        # Text to Speech
        tts = gTTS(translated)
        tts.save("translated.mp3")

        audio_file = open("translated.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

    else:
        st.warning("Please enter some text.")