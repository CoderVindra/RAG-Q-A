import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA


# Load env variables (For Groq API key)
load_dotenv()

# Get the working directory of the current file
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

def rag_retriever(user_query : str) -> str:
    # Initialize llm
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.0
    )

    # Load embedding model
    embedding = HuggingFaceEmbeddings()

    # load vector store
    vector_store = Chroma(
        persist_directory=f"{WORKING_DIR}/vector_store",
        embedding_function=embedding
    )

    # create retriever
    retriever = vector_store.as_retriever()

    # create QA chains from chain type
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    response = qa_chain.invoke({"query": user_query})
    
    return response["result"]
