# Conversational-RAG-with-PDF-uploads-and-Chat-History

# Conversational RAG with PDF Uploads & Chat History

This project is a **Streamlit-based Conversational Retrieval-Augmented Generation (RAG) system** that allows users to:
- Upload PDF documents
- Interact with them via a conversational chatbot
- Maintain context-aware chat history across multiple sessions

It uses **LangChain**, **Groq Llama3**, **HuggingFace embeddings**, and **Chroma vector store** under the hood.

---

## 🧠 Features

- 🔍 **PDF Uploads**: Upload multiple PDF files for question-answering.
- 🧠 **Conversational RAG**: Queries are reformulated with chat context awareness.
- 📜 **Session-Based Chat History**: Each session maintains its own memory.
- 🧠 **LLM-Driven QA**: Powered by LLaMA3-8B from Groq.
- 🔎 **Semantic Search**: Uses `all-MiniLM-L6-v2` HuggingFace embeddings for document retrieval.

---

## 📦 Tech Stack

- `Streamlit` for frontend interface
- `LangChain` for orchestration
- `Groq LLaMA3` as LLM backend
- `HuggingFace Embeddings`
- `Chroma` as vector DB
- `dotenv` for environment variables

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/conversational-rag-pdf-chat.git
cd conversational-rag-pdf-chat


Multi-turn memory persistence across reloads

Upload history tracker

UI enhancements with session switching
