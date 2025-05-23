import streamlit as st
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
import chromadb
import tempfile

from dotenv import load_dotenv
load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

st.title("Conversational RAG with PDF Uploads")
st.write("Upload PDFs and chat with their content")

api_key = st.text_input("Enter your GROQ API key", type="password")

if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192")

    # Chat Interface 
    session_id = st.text_input("Session ID", value="default_session")
    
    # Managing Chat History
    if "store" not in st.session_state:
        st.session_state.store = {}

    uploaded_files = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=True)

    # Process the uploaded files
    documents = []
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Use temporary file instead of fixed name
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.getvalue())
                temp_pdf_path = temp_file.name
            
            loader = PyPDFLoader(temp_pdf_path)
            docs = loader.load()
            documents.extend(docs)
            
            # Clean up temporary file
            os.unlink(temp_pdf_path)

        # Splitting and making embeddings
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=600)
        splits = text_splitter.split_documents(documents)
        
        # Alternative fix: Use FAISS instead of ChromaDB to avoid tenant issues
        from langchain_community.vectorstores import FAISS
        
        # Create FAISS vectorstore (no tenant issues)
        vectorstore = FAISS.from_documents(splits, embeddings)
        retriever = vectorstore.as_retriever()   

        contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a stand alone question which can be understood "
            "without a chat history. Do Not answer the question, "
            "just reformulate it if needed and otherwise return as it is with an apt response to the user. "
            "Do not give a blank response to the User."
        )
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}")
            ]
        )

        history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

        ## Answer question prompt
        system_prompt = (
            "You are an assistant for question answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you don't know. "
            "Use seven to eight sentences maximum and keep the answer concise. "
            "\n\n"
            "{context}"
        )
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}")
            ]
        )

        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        def get_session_history(session_id):
            if session_id not in st.session_state.store:
                st.session_state.store[session_id] = ChatMessageHistory()
            return st.session_state.store[session_id]

        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain, 
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )   

        user_input = st.text_input("Type your question here")
        if user_input:
            response = conversational_rag_chain.invoke(
                {"input": user_input},
                config={
                    "configurable": {"session_id": session_id}
                }
            )

            st.write("Assistant:", response['answer'])
            
            # Display chat history
            session_history = get_session_history(session_id)
            st.write("Chat History:")
            for msg in session_history.messages:
                st.write(f"{msg.type}: {msg.content}")
else:
    st.warning("Please enter your Groq API Key")
