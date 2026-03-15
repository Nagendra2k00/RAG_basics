from dotenv import load_dotenv
from langchain_chroma import Chroma
from generation_embedding import _get_embedding_model

load_dotenv()

persist_directory = "db/chroma_db"

embedding_model = _get_embedding_model()


db = Chroma(
    persist_directory=persist_directory, 
    embedding_function=embedding_model, 
    collection_metadata={"hnsw:space": "cosine"}
)

query = "\n\nHow many different types of dogs are there?"

# retriever = db.as_retriever(search_kwargs={"k": 5})

retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 3,
        "score_threshold": 0.3
    }
)

related_docs = retriever.invoke(query)

print(f"query: {query}")

for i, doc in enumerate(related_docs, 1):
    print(f"\nDocument {i}:")
    print(f"\n{doc.page_content}\n")