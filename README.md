# 📄 LLM-Powered Document Q&A System (RAG)

This project is a **Retrieval-Augmented Generation (RAG)** based application that allows users to upload a PDF document and ask questions about its content. The system processes the document, stores embeddings in a vector database, and retrieves relevant context to generate accurate answers using an LLM.

---

## 🚀 Features

- 📂 Upload PDF documents
- ✂️ Intelligent text chunking
- 🧠 Embedding generation using HuggingFace
- 🗄️ Persistent vector storage using ChromaDB
- 🔍 Semantic search with retriever
- 🤖 LLM-powered question answering (Groq - LLaMA 3.1)
- 🌐 Interactive UI with Streamlit

---

## 🏗️ Project Structure

```
RAG-Q-A/
│── vector_store/          
│── app.py                 
│── document_ingestion.py  
│── rag_retrieval.py       
│── sample_context.pdf     
│── requirements.txt       
│── .env                   
│── README.md              
```

---

## ⚙️ How It Works

### 1. Document Ingestion (`document_ingestion.py`)
- Loads PDF using `UnstructuredPDFLoader`
- Splits text into chunks using `RecursiveCharacterTextSplitter`
- Generates embeddings using `HuggingFaceEmbeddings`
- Stores vectors in **ChromaDB**

### 2. Retrieval & QA (`rag_retrieval.py`)
- Loads stored embeddings
- Converts them into a retriever
- Uses `RetrievalQA` chain
- Queries LLM (`llama-3.1-8b-instant`) via Groq API

### 3. Frontend (`app.py`)
- Upload PDF
- Process document
- Ask questions via UI
- Display AI-generated answers

---

## 🧪 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/CoderVindra/RAG-Q-A.git
cd RAG-Q-A
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 Usage

1. Upload a PDF file
2. Wait for document processing
3. Ask questions related to the document
4. Get AI-generated answers instantly

---

## 🧠 Tech Stack

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM (LLaMA 3.1)
- Streamlit
- Python

---

## 🙌 Author

**Ravindra Pawar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
