# Conversational-RAG-with-PDF-uploads-and-Chat-History

🧠 Conversational RAG with PDF Uploads & Chat History
A powerful Conversational Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and interact with their content through natural language questions. This system leverages LangChain, Groq LLMs, HuggingFace Embeddings, and Streamlit to create a seamless and intelligent PDF-based Q&A interface — with memory!

🚀 Features
🔍 Conversational PDF Q&A — Ask questions about one or multiple uploaded PDFs.

🧠 Context-Aware Retrieval — Understands chat history to give contextually relevant answers.

📚 Chat Memory — Maintains and shows chat history for each session.

🧾 Multi-File Upload Support — Upload multiple PDFs at once.

⚡ Groq LLM Support — Fast inference with Llama3 models via Groq API.

🧠 MiniLM Embeddings — Efficient semantic similarity using HuggingFace all-MiniLM-L6-v2.

🏗️ Tech Stack
Technology	Usage
Streamlit	Frontend for UI and interaction
LangChain	Core RAG chain and chat management
Groq	LLM backend using Llama3-8b-8192
HuggingFace	For document embedding via all-MiniLM-L6-v2
Chroma	Vector database for storing document chunks
LangChain-Chroma	Retriever interface between vector DB and LangChain
dotenv	Securely handle API keys and tokens
PyPDFLoader	Load PDF content and convert to text chunks

📁 Folder Structure
bash
Copy
Edit
.
├── main.py                    # Streamlit app (this file)
├── .env                       # Stores private API tokens
├── requirements.txt           # Python dependencies
🔑 Setup & Usage
✅ 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/conversational-pdf-rag.git
cd conversational-pdf-rag
✅ 2. Create and Activate a Virtual Environment (Optional)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
✅ 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ 4. Add Environment Variables
Create a .env file in the root directory:

env
Copy
Edit
HF_TOKEN=your_huggingface_token_here
✅ 5. Run the App
bash
Copy
Edit
streamlit run main.py
🧪 How to Use the App
Enter your GROQ API Key: Required to access the Llama3 model.

Enter a Session ID: Identifies the specific chat session for message history.

Upload PDF(s): Choose one or more PDF files to analyze.

Ask Questions: Interact with your PDFs conversationally.

See Chat History: Your conversation history will persist as long as the session remains.

🧠 Chain Architecture
text
Copy
Edit
User Input
   ↓
Contextualization Prompt (if needed)
   ↓
History-Aware Retriever
   ↓
Relevant Chunks Retrieved from Vector Store
   ↓
Stuff Chain (Prompt + Answer LLM)
   ↓
Response Generated
   ↓
Chat History Stored and Displayed
Retriever: Uses Chroma and HuggingFaceEmbeddings.

LLM: Groq-hosted Llama3 8B model via API.

Chains:

create_history_aware_retriever: Reformulates questions based on context.

create_stuff_documents_chain: Combines document chunks to answer questions.

RunnableWithMessageHistory: Links message history to RAG pipeline.

📦 Dependencies
Create a requirements.txt with:

txt
Copy
Edit
streamlit
langchain
langchain-core
langchain-community
langchain-chroma
langchain-groq
langchain-huggingface
chromadb
python-dotenv
PyPDF2
🛡️ Security Notes
Make sure never to upload .env to public repositories.

The GROQ API Key and HuggingFace token are sensitive — store securely.

✍️ Author
Your Name — @yourhandle

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🧠 Coming Soon / Ideas
Support for other document types (DOCX, TXT)

Multi-turn memory persistence across reloads

Upload history tracker

UI enhancements with session switching
