from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=800, chunk_overlap=0):

    print(f"Splitting {len(documents)} documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""], # split on paragraph, line, sentence, space, and character
    )
    chunks = text_splitter.split_documents(documents)
    
    if chunks:
        for i, chunk in enumerate(chunks[:2]):
            print(f"Chunk {i+1}:")
            print(f"  Source: {chunk.metadata['source']}")
            print(f"  Content length: {len(chunk.page_content)}")
            print(f"  content preview: {chunk.page_content}")
            print("-" * 50)

        if len(chunks) > 1:
            print(f"Showing only the first 2 chunks. Total chunks: {len(chunks)}")

    return chunks