import io
import os
import tempfile
from pathlib import Path
from typing import List, Tuple

import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS
import speech_recognition as sr

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

APP_TITLE = "Urdu Voice Chatbot with LangChain RAG"
DEFAULT_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"


st.set_page_config(page_title=APP_TITLE, page_icon="🎙️", layout="wide")


def init_state() -> None:
    defaults = {
        "vectorstore": None,
        "indexed_files": [],
        "retriever_k": 4,
        "chat_history": [],
        "last_transcript": "",
        "last_answer": "",
        "last_audio_bytes": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()


def save_uploaded_pdfs(uploaded_files) -> List[str]:
    temp_dir = tempfile.mkdtemp(prefix="urdu_rag_pdfs_")
    saved_paths: List[str] = []
    for uploaded_file in uploaded_files:
        output_path = os.path.join(temp_dir, uploaded_file.name)
        with open(output_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        saved_paths.append(output_path)
    return saved_paths



def load_pdf_documents(pdf_paths: List[str]):
    docs = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        file_docs = loader.load()
        for doc in file_docs:
            doc.metadata["source_name"] = Path(path).name
        docs.extend(file_docs)
    return docs



def build_vectorstore(pdf_paths: List[str], google_api_key: str, chunk_size: int, chunk_overlap: int):
    raw_docs = load_pdf_documents(pdf_paths)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    split_docs = splitter.split_documents(raw_docs)
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=google_api_key,
    )
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore, split_docs



def transcribe_urdu_audio(audio_bytes: bytes) -> str:
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_path = temp_audio.name

    try:
        with sr.AudioFile(temp_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ur-PK")
        return text.strip()
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass



def format_sources(source_docs) -> List[str]:
    seen = set()
    formatted = []
    for doc in source_docs:
        source_name = doc.metadata.get("source_name") or Path(str(doc.metadata.get("source", "Unknown"))).name
        page_number = doc.metadata.get("page")
        label = f"{source_name}"
        if page_number is not None:
            label += f" — page {page_number + 1}"
        if label not in seen:
            seen.add(label)
            formatted.append(label)
    return formatted



def generate_urdu_answer(
    query: str,
    google_api_key: str,
    temperature: float,
    model_name: str,
    retriever_k: int,
) -> Tuple[str, List[str], List]:
    retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": retriever_k})
    retrieved_docs = retriever.invoke(query)
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    source_labels = format_sources(retrieved_docs)

    system_prompt = (
        "آپ ایک مددگار اردو RAG چیٹ بوٹ ہیں۔ "
        "صرف فراہم کردہ context کی بنیاد پر جواب دیں۔ "
        "جواب مکمل اردو میں دیں۔ "
        "اگر context میں جواب واضح نہ ہو تو صاف بتائیں کہ دی گئی PDF فائلوں میں کافی معلومات نہیں ملیں۔ "
        "غیر ضروری بات نہ کریں۔"
    )

    user_prompt = f"""
Context:
{context}

User question:
{query}

Please answer in Urdu only.
"""

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=google_api_key,
        temperature=temperature,
    )
    response = llm.invoke([
        ("system", system_prompt),
        ("human", user_prompt),
    ])
    answer = response.content if hasattr(response, "content") else str(response)
    return answer.strip(), source_labels, retrieved_docs



def text_to_urdu_speech(text: str) -> bytes:
    tts = gTTS(text=text, lang="ur")
    buffer = io.BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)
    return buffer.read()


with st.sidebar:
    st.header("Configuration")
    google_api_key = st.text_input(
        "Google Gemini API Key",
        type="password",
        value=st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY", "")),
        help="Use a Google AI Studio Gemini API key for the LangChain chat and embeddings steps.",
    )
    model_name = st.selectbox(
        "Gemini model",
        ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"],
        index=0,
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.1)
    chunk_size = st.slider("Chunk size", 300, 2000, 1000, 100)
    chunk_overlap = st.slider("Chunk overlap", 0, 400, 200, 20)
    retriever_k = st.slider("Top-k retrieved chunks", 1, 8, 4, 1)
    st.session_state.retriever_k = retriever_k

    st.markdown("---")
    uploaded_pdfs = st.file_uploader(
        "Upload PDF files for the RAG knowledge base",
        type=["pdf"],
        accept_multiple_files=True,
        help="This assignment uses PDF files only, matching the course brief.",
    )

    build_clicked = st.button("Build / Refresh knowledge base", use_container_width=True)
    clear_chat_clicked = st.button("Clear chat history", use_container_width=True)

    if clear_chat_clicked:
        st.session_state.chat_history = []
        st.session_state.last_transcript = ""
        st.session_state.last_answer = ""
        st.session_state.last_audio_bytes = None
        st.success("Chat history cleared.")

    if build_clicked:
        if not google_api_key:
            st.error("Please provide your Google Gemini API key first.")
        elif not uploaded_pdfs:
            st.error("Please upload at least one PDF file.")
        else:
            with st.spinner("Loading PDFs, splitting content, creating embeddings, and building the vector store..."):
                try:
                    pdf_paths = save_uploaded_pdfs(uploaded_pdfs)
                    vectorstore, split_docs = build_vectorstore(
                        pdf_paths=pdf_paths,
                        google_api_key=google_api_key,
                        chunk_size=chunk_size,
                        chunk_overlap=chunk_overlap,
                    )
                    st.session_state.vectorstore = vectorstore
                    st.session_state.indexed_files = [file.name for file in uploaded_pdfs]
                    st.success(f"Knowledge base ready. Indexed {len(uploaded_pdfs)} PDF file(s) into {len(split_docs)} chunks.")
                except Exception as e:
                    st.exception(e)

st.title("🎙️ Urdu Voice Chatbot with LangChain RAG")
st.caption(
    "Assignment 09 • Streamlit + LangChain + PDF-only RAG + Urdu voice input + Urdu text/audio response"
)

st.markdown(
    """
This application demonstrates a practical Assignment 09 workflow:
- upload **PDF files only** as the knowledge base
- build a **LangChain RAG pipeline**
- ask questions in **Urdu** through voice or typed input
- receive the answer in **Urdu text** and **Urdu speech**
"""
)

with st.expander("Sample Urdu prompts for testing"):
    st.markdown(
        """
- اس پی ڈی ایف میں سب سے اہم بات کیا ہے؟
- اس دستاویز کا خلاصہ اردو میں بتائیں۔
- اس فائل میں RAG کے بارے میں کیا بتایا گیا ہے؟
- اس موضوع کی اہم تعریفیں اردو میں سمجھائیں۔
- اگر معلومات موجود ہوں تو اہم نکات نکال کر بتائیں۔
"""
    )

if st.session_state.indexed_files:
    st.info("Indexed PDFs: " + ", ".join(st.session_state.indexed_files))
else:
    st.warning("First upload PDF files from the sidebar and click 'Build / Refresh knowledge base'.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1) Record Urdu voice input")
    st.caption("Allow microphone permission in your browser, then record your question.")
    audio_value = st.audio_input("Record your Urdu question")

with col2:
    st.subheader("2) Or type your Urdu question")
    typed_query = st.text_area(
        "Typed Urdu input",
        value="",
        height=140,
        placeholder="مثال: اس پی ڈی ایف میں RAG کے بارے میں کیا بتایا گیا ہے؟",
    )

submit = st.button("Ask the chatbot", type="primary", use_container_width=True)

if submit:
    if st.session_state.vectorstore is None:
        st.error("Please build the knowledge base from PDF files first.")
    elif not google_api_key:
        st.error("Please enter your Google Gemini API key in the sidebar.")
    else:
        transcript = ""
        if audio_value is not None:
            try:
                transcript = transcribe_urdu_audio(audio_value.read())
            except sr.UnknownValueError:
                st.error("The speech could not be recognized clearly. Please try again or use typed text.")
            except sr.RequestError as e:
                st.error(f"Speech recognition service error: {e}")
            except Exception as e:
                st.error(f"Audio processing failed: {e}")

        user_query = transcript if transcript else typed_query.strip()

        if not user_query:
            st.error("Please record or type a question in Urdu.")
        else:
            st.session_state.last_transcript = user_query
            with st.spinner("Retrieving relevant PDF chunks and generating an Urdu response..."):
                try:
                    answer, source_labels, _ = generate_urdu_answer(
                        query=user_query,
                        google_api_key=google_api_key,
                        temperature=temperature,
                        model_name=model_name,
                        retriever_k=retriever_k,
                    )
                    audio_bytes = text_to_urdu_speech(answer)
                    st.session_state.last_answer = answer
                    st.session_state.last_audio_bytes = audio_bytes
                    st.session_state.chat_history.append({
                        "question": user_query,
                        "answer": answer,
                        "sources": source_labels,
                    })
                except Exception as e:
                    st.exception(e)

if st.session_state.last_transcript:
    st.markdown("---")
    st.subheader("Input Urdu text")
    st.text_area("Recognized / submitted query", value=st.session_state.last_transcript, height=120)

if st.session_state.last_answer:
    st.subheader("Generated Urdu response")
    st.text_area("Chatbot response", value=st.session_state.last_answer, height=220)

if st.session_state.chat_history:
    latest_sources = st.session_state.chat_history[-1]["sources"]
    if latest_sources:
        st.markdown("**Retrieved source references**")
        for src in latest_sources:
            st.markdown(f"- {src}")

if st.session_state.last_audio_bytes:
    st.subheader("Generated Urdu speech output")
    st.audio(st.session_state.last_audio_bytes, format="audio/mp3")
    st.download_button(
        label="Download response audio",
        data=st.session_state.last_audio_bytes,
        file_name="urdu_rag_chatbot_response.mp3",
        mime="audio/mpeg",
    )

if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("Conversation history")
    for i, item in enumerate(reversed(st.session_state.chat_history), start=1):
        with st.expander(f"Chat {i}"):
            st.markdown("**Question**")
            st.write(item["question"])
            st.markdown("**Answer**")
            st.write(item["answer"])
            if item["sources"]:
                st.markdown("**Sources used**")
                for src in item["sources"]:
                    st.markdown(f"- {src}")
