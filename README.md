# RAG Basics

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-FF6B35?logo=chainlink)](https://python.langchain.com/)
[![Chroma](https://img.shields.io/badge/Chroma-vector%20DB-green)](https://www.trychroma.com/)

A minimal **Retrieval-Augmented Generation (RAG)** pipeline: load docs, chunk them, embed with Ollama, store in Chroma, and run similarity search.

---

## Quick start

```bash
git clone https://github.com/Nagendra2k00/RAG_basics.git
cd RAG_basics
python -m venv venv && venv\Scripts\activate   # Windows
# source venv/bin/activate                      # macOS/Linux
pip install -r requirements.txt
mkdir -p docs && echo "Your content here." > docs/sample.txt
python ingestion.py
python retrieval_pipeline.py
```

Requires **Python 3.10+** and [Ollama](https://ollama.ai/) with an embedding model (e.g. `ollama pull nomic-embed-text`).

---

## What it does

| Step | Description |
| ---- | ----------- |
| **Load** | Reads all `.txt` files from `docs/` |
| **Chunk** | Splits into overlapping segments (recursive splitter) |
| **Embed** | Uses Ollama to generate embeddings, stores in Chroma |
| **Retrieve** | Queries the vector store for relevant chunks |

---

## Project layout

Plain ASCII tree so it renders the same everywhere:

```
RAG_basics/
  docs/                    <- put your .txt files here
  db/
    chroma_db/             <- vector DB (created by ingestion)
  document_loader.py       <- load from docs/
  chunking.py              <- split into chunks
  generation_embedding.py  <- embeddings + Chroma
  ingestion.py             <- full pipeline: load -> chunk -> embed -> save
  retrieval_pipeline.py    <- load DB and run a query
  requirements.txt
  .env.example
  README.md
```

---

## Setup (detailed)

**1. Virtual environment (recommended)**

- **Windows:** `python -m venv venv` then `venv\Scripts\activate`
- **macOS/Linux:** `python -m venv venv` then `source venv/bin/activate`

**2. Install**

```bash
pip install -r requirements.txt
```

**3. Documents**

Put `.txt` files in `docs/`. Create the folder if needed: `mkdir -p docs`

**4. Environment (optional)**

```bash
cp .env.example .env
```

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `EMBEDDING_PROVIDER` | `ollama` | Embedding provider |
| `OLLAMA_EMBEDDING_MODEL` | `nomic-embed-text` | Ollama embedding model |

Omit `.env` to use defaults.

---

## Run

**Build the vector store**

```bash
python ingestion.py
```

(Ollama must be running and the embedding model pulled.)

**Query it**

```bash
python retrieval_pipeline.py
```

Edit the query or retrieval options (e.g. `k`, `score_threshold`) in `retrieval_pipeline.py`.

---

## Configuration

| What | Where |
| ---- | ----- |
| Document path | `ingestion.py` -> `load_documents(docs_path="docs")` |
| Chunk size / overlap | `chunking.py` -> `chunk_size=800`, `chunk_overlap=0` |
| Vector store path | `generation_embedding.py` & `retrieval_pipeline.py` -> `persist_directory="db/chroma_db"` |
| Retrieval (k, threshold) | `retrieval_pipeline.py` -> `search_kwargs={"k": 3, "score_threshold": 0.3}` |

---

## Troubleshooting

| Issue | Fix |
| ----- | --- |
| No documents found | Create `docs/` and add at least one `.txt` file |
| Ollama errors | Run `ollama serve` and `ollama pull nomic-embed-text` |
| Module not found | Activate the same venv where you ran `pip install` |
| Poor or empty results | Re-run `python ingestion.py` after changing files in `docs/` |

---


## 👤 Author

**Nagendra Kumar K S**

- GitHub: [@Nagendra Kumar K S](https://github.com/Nagendra2k00)
- LinkedIn: [@Nagendra Kumar K S](https://linkedin.com/in/nagendrakumarks)

## License

Use and modify as needed.
