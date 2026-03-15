import os
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

# Optional providers: import only what is used to avoid errors when a provider isn't installed.
def _get_embedding_model() -> Embeddings:
    """
    Return the embedding model based on EMBEDDING_PROVIDER env var.
    Supported: 'ollama'
    """
    provider = (os.environ.get("EMBEDDING_PROVIDER") or "ollama").strip().lower()

    if provider == "ollama":
        from langchain_ollama import OllamaEmbeddings
        model = os.environ.get("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
        return OllamaEmbeddings(model=model)

    raise ValueError(f"Unknown EMBEDDING_PROVIDER='{provider}'.")


def create_vector_database(chunks, persist_directory="db/chroma_db"):
    print(f"Creating vector database in {persist_directory}...")

    embedding_model = _get_embedding_model()
    print(f"Embedding provider: {os.environ.get('EMBEDDING_PROVIDER', 'ollama')}")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"},
    )

    print(f"Vector store created in {persist_directory}.")
    return vector_store
