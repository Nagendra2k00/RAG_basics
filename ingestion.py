import os
from dotenv import load_dotenv
from document_loader import load_documents
from chunking import split_documents
from generation_embedding import create_vector_database

load_dotenv()


def main():
    print("Starting ingestion...")

    # Load documents
    documents = load_documents(docs_path="docs")

    # Split documents into chunks
    chunks = split_documents(documents)
    
    # Create vector database
    vector_store = create_vector_database(chunks)

    print("Ingestion completed successfully.")

if __name__ == "__main__":
    main()