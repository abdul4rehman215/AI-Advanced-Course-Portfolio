import os
import re
import tempfile
from datetime import datetime

import speech_recognition as sr
import streamlit as st
from gtts import gTTS


st.set_page_config(
    page_title="Assignment 07 - Urdu Voice Chatbot",
    page_icon="🎙️",
    layout="centered",
)


# -----------------------------
# Helper functions
# -----------------------------
def normalize_text(text: str) -> str:
    """Normalize Urdu/English mixed input for simple rule-based handling."""
    if not text:
        return ""
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def transcribe_urdu_audio(audio_bytes: bytes) -> str:
    """Transcribe recorded audio using Google Speech Recognition with Urdu locale."""
    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_bytes)
        temp_audio_path = tmp_file.name

    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ur-PK")
        return text
    finally:
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)



def generate_urdu_response(user_text: str) -> str:
    """Simple rule-based Urdu chatbot response generator."""
    text = normalize_text(user_text)

    rules = [
        (["السلام علیکم", "اسلام علیکم", "assalam", "salam", "سلام"],
         "وعلیکم السلام۔ آپ کا خیر مقدم ہے۔ میں آپ کی کس معاملے میں مدد کر سکتا ہوں؟"),
        (["آپ کیسے ہیں", "کیسے ہو", "how are you"],
         "میں بالکل ٹھیک ہوں۔ شکریہ۔ آپ بتائیں، میں آپ کی کیسے مدد کروں؟"),
        (["آپ کا نام", "تمہارا نام", "your name"],
         "میرا نام اردو وائس چیٹ بوٹ ہے۔ میں آپ کی آواز کو متن میں بدل کر جواب دے سکتا ہوں۔"),
        (["ai", "اے آئی", "artificial intelligence", "مصنوعی ذہانت"],
         "مصنوعی ذہانت ایسے سسٹمز بنانے کا شعبہ ہے جو سیکھ سکیں، فیصلہ کر سکیں، اور مختلف کام خودکار انداز میں انجام دے سکیں۔"),
        (["رگ", "rag", "retrieval augmented generation"],
         "ریٹریول آگمینٹڈ جنریشن ایک ایسا طریقہ ہے جس میں ماڈل جواب دینے سے پہلے متعلقہ معلومات بازیافت کرتا ہے تاکہ جواب زیادہ درست اور سیاق کے مطابق ہو۔"),
        (["چیٹ بوٹ", "chatbot", "بوٹ"],
         "چیٹ بوٹ ایک ایسا سافٹ ویئر ہوتا ہے جو متن یا آواز کے ذریعے صارف سے گفتگو کرتا ہے اور سوالات کے جواب دیتا ہے۔"),
        (["وقت", "time"],
         f"اس وقت تاریخ اور وقت یہ ہے: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"),
        (["شکریہ", "thanks", "thank you"],
         "آپ کا شکریہ۔ اگر آپ چاہیں تو مزید سوال بھی پوچھ سکتے ہیں۔"),
        (["خدا حافظ", "الوداع", "bye"],
         "خدا حافظ۔ امید ہے آپ کو یہ ایپ مفید لگی ہوگی۔"),
    ]

    for keywords, response in rules:
        if any(keyword in text for keyword in keywords):
            return response

    if not text:
        return "مجھے کوئی واضح ان پٹ موصول نہیں ہوا۔ براہِ کرم دوبارہ کوشش کریں۔"

    return (
        "میں نے آپ کی بات یہ سمجھی: \n\n"
        f"\"{user_text}\"\n\n"
        "اس کے جواب میں میرا سادہ اردو ردِعمل یہ ہے: "
        "آپ نے ایک اہم نکتہ اٹھایا ہے۔ اگر آپ چاہیں تو میں اسی موضوع پر مزید وضاحت بھی دے سکتا ہوں۔"
    )



def text_to_speech_urdu(text: str) -> bytes:
    """Convert Urdu text to speech using gTTS and return MP3 bytes."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_mp3:
        temp_mp3_path = tmp_mp3.name

    try:
        tts = gTTS(text=text, lang="ur", slow=False)
        tts.save(temp_mp3_path)
        with open(temp_mp3_path, "rb") as f:
            audio_bytes = f.read()
        return audio_bytes
    finally:
        if os.path.exists(temp_mp3_path):
            os.remove(temp_mp3_path)


# -----------------------------
# Session state
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "last_response_audio" not in st.session_state:
    st.session_state.last_response_audio = None


# -----------------------------
# UI
# -----------------------------
st.title("🎙️ Urdu Voice Chatbot Application")
st.caption("Assignment 07 - Streamlit Voice Chatbot | Urdu Speech → Text → Response → Urdu Speech")

with st.sidebar:
    st.header("How to use")
    st.write(
        "1. Record your voice in Urdu using the browser microphone.\n"
        "2. Wait for transcription.\n"
        "3. Review the generated Urdu response.\n"
        "4. Play or download the response audio."
    )
    st.info(
        "This demo uses Google Speech Recognition for Urdu speech-to-text and gTTS for Urdu text-to-speech."
    )
    st.write("**Helpful fallback:** You can also type Urdu text manually if microphone input is not available.")

st.markdown(
    "This application demonstrates a complete Urdu voice chatbot workflow: "
    "audio input, speech-to-text conversion, Urdu response generation, and speech output."
)

sample_prompts = [
    "السلام علیکم",
    "آپ کا نام کیا ہے؟",
    "مصنوعی ذہانت کیا ہے؟",
    "RAG کیا ہوتا ہے؟",
    "آپ کیسے ہیں؟",
]
st.write("**Sample Urdu prompts for testing:**")
st.code("\n".join(sample_prompts), language="text")

st.subheader("1) Record Urdu voice input")
audio_value = st.audio_input("Click and record your Urdu voice")

st.subheader("2) Or test with manual Urdu text")
manual_text = st.text_area(
    "Type Urdu text here if you want to test without the microphone",
    placeholder="مثال: السلام علیکم، آپ کیسے ہیں؟",
    height=120,
)

col1, col2 = st.columns(2)
with col1:
    process_audio = st.button("Process Voice Input", use_container_width=True)
with col2:
    process_text = st.button("Process Typed Text", use_container_width=True)


# -----------------------------
# Main interaction logic
# -----------------------------
if process_audio:
    if audio_value is None:
        st.warning("Please record your Urdu voice first.")
    else:
        try:
            with st.spinner("Transcribing Urdu voice input..."):
                user_text = transcribe_urdu_audio(audio_value.getvalue())

            st.success("Voice input processed successfully.")
            st.write("**Recognized Urdu text:**")
            st.text_area("Transcription", value=user_text, height=120, disabled=True)

            with st.spinner("Generating Urdu response..."):
                response_text = generate_urdu_response(user_text)

            st.write("**Generated Urdu response:**")
            st.text_area("Chatbot Response", value=response_text, height=170, disabled=True)

            with st.spinner("Converting response to Urdu speech..."):
                response_audio = text_to_speech_urdu(response_text)
                st.session_state.last_response_audio = response_audio

            st.write("**Generated Urdu speech output:**")
            st.audio(response_audio, format="audio/mp3")
            st.download_button(
                label="Download response audio",
                data=response_audio,
                file_name="urdu_chatbot_response.mp3",
                mime="audio/mpeg",
            )

            st.session_state.history.append(
                {
                    "mode": "voice",
                    "user_text": user_text,
                    "response_text": response_text,
                }
            )

        except sr.UnknownValueError:
            st.error("Speech could not be understood clearly. Please try again with a clearer Urdu recording.")
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")
        except Exception as e:
            st.error(f"Unexpected error while processing voice input: {e}")


if process_text:
    if not manual_text.strip():
        st.warning("Please type some Urdu text first.")
    else:
        try:
            with st.spinner("Generating Urdu response..."):
                response_text = generate_urdu_response(manual_text)

            st.write("**Input Urdu text:**")
            st.text_area("Typed Input", value=manual_text, height=120, disabled=True)

            st.write("**Generated Urdu response:**")
            st.text_area("Chatbot Response", value=response_text, height=170, disabled=True)

            with st.spinner("Converting response to Urdu speech..."):
                response_audio = text_to_speech_urdu(response_text)
                st.session_state.last_response_audio = response_audio

            st.write("**Generated Urdu speech output:**")
            st.audio(response_audio, format="audio/mp3")
            st.download_button(
                label="Download response audio",
                data=response_audio,
                file_name="urdu_chatbot_response.mp3",
                mime="audio/mpeg",
            )

            st.session_state.history.append(
                {
                    "mode": "typed",
                    "user_text": manual_text,
                    "response_text": response_text,
                }
            )

        except Exception as e:
            st.error(f"Unexpected error while processing typed text: {e}")


# -----------------------------
# Conversation history
# -----------------------------
st.markdown("---")
st.subheader("Conversation History")

if not st.session_state.history:
    st.write("No conversation yet. Record or type something in Urdu to begin.")
else:
    for idx, item in enumerate(reversed(st.session_state.history), start=1):
        with st.expander(f"Interaction {idx} | Mode: {item['mode']}"):
            st.write("**User input:**")
            st.write(item["user_text"])
            st.write("**Chatbot response:**")
            st.write(item["response_text"])

st.markdown("---")
st.caption(
    "Practical note: This version is intentionally lightweight and beginner-friendly for assignment submission. "
    "It uses a rule-based response engine so it can run without any API key."
)
