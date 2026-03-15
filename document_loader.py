import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader

def load_documents(docs_path="docs"):
    print(f"Loading documents from {docs_path}...")

    if not os.path.exists(docs_path):
        print(f"Directory {docs_path} does not exist.")
        return []

    loader = DirectoryLoader(
        docs_path,
        recursive=True,
        show_progress=True,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    documents = loader.load()

    if len(documents) == 0:
        print(f"No documents found in {docs_path}.")
        return []
    
    for i, doc in enumerate(documents[:3]):
        print(f"Document {i+1}:")
        print(f"  Source: {doc.metadata['source']}")
        print(f"  Content length: {len(doc.page_content)}")
        print(f"  content preview: {doc.page_content[:100]}...")
        print(f"  metadata: {doc.metadata}")
        print("\n")

    return documents