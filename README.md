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
- 🤖 **LLM-Driven QA**: Powered by LLaMA3-8B from Groq.
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
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Add your HuggingFace token:

```
HF_TOKEN=your_huggingface_token_here
```

> 💡 You can get a free HF token from https://huggingface.co/settings/tokens

### 5. Run the App

```bash
streamlit run main.py
```

---

## 🔑 How to Use

1. Enter your **GROQ API Key** when prompted in the app.  
2. Set a **Session ID** to start a new chat session.  
3. Upload one or more **PDF files**.  
4. Ask questions about the content.  
5. View answers with full conversational memory.  

---

## 💬 Example Prompts

- “Summarize the second chapter.”  
- “What is the definition of quantum entanglement?”  
- “What is the conclusion in the last section?”  
- “What did we discuss in the last message?”  

---

## 📁 Project Structure

```bash
.
├── main.py                  # Main Streamlit application
├── requirements.txt         # Required Python packages
├── .env                     # HuggingFace token (not pushed)
└── README.md                # This file
```

---

## 🧪 requirements.txt

```
streamlit
langchain
langchain-groq
langchain-community
langchain-chroma
langchain-core
langchain-huggingface
chromadb
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ✍️ Author

Developed by **Dushyant Atalkar**
