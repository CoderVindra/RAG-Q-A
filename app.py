import os
import streamlit as st
from document_ingestion import process_document_to_chromadb
from rag_retrieval import rag_retriever


# Get current working directory path
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# Display a title on the webpage.
st.title("LLM-Powered Document Q&A System")

# Create file upload widget
uploaded_file = st.file_uploader("Upload a pdf file", type=["pdf"])

if uploaded_file is not None:
    # create full path to save file
    save_path = os.path.join(WORKING_DIR, uploaded_file.name)

    # open file in write-binary mode
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Ingest this pdf file
    processed_document = process_document_to_chromadb(file_name=uploaded_file.name)

    if processed_document:
        st.success("Document processed sucessfully!")
    else:
        st.error("Something went wrong during processing of document! Try again later!")
    
# Text widget to get user input
user_ques = st.text_area("Ask your question about the document here!")

if st.button("Answer"):
    ans = rag_retriever(user_query=user_ques)
    st.markdown("### RAG Response")
    st.markdown(ans)
    