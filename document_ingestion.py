import os
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Get the path of the current folder where the script is located.
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))


def process_document_to_chromadb(file_name : str ) -> bool:
    try:
        # Initialize the loader
        loader = UnstructuredPDFLoader(file_path=f"{WORKING_DIR}/{file_name}")

        # Load documents
        documents = loader.load()

        # Initialize text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=5000,
            chunk_overlap=200
        )

        # convert documents into smaller chunnks
        text_chunks = text_splitter.split_documents(
            documents=documents
        )

        # Load vector embedding model
        embedding = HuggingFaceEmbeddings()

        # create vector store
        Chroma.from_documents(
            documents=text_chunks,
            embedding=embedding,
            persist_directory=f"{WORKING_DIR}/vector_store"
        )
    except Exception as e:
        print(f"Something went wrong during document ingestion process. Error details : {str(e)}")
        return False
    else:
        print("Document ingestion process successful!")
        return True
