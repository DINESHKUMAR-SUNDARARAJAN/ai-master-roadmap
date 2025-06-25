# Week 2 – GPT-4o + ChromaDB RAG System

## Day 5

- Built a vector-based document retrieval pipeline (RAG).
- Embedded PDF chunks with `OpenAIEmbeddings`.
- Stored chunks in `ChromaDB` and queried top matches by similarity.
- GPT-4o answered questions using matched chunks only.

## Files Overview

| File | Purpose |
|------|---------|
| `ingest_and_index.py` | Splits PDF → embeds → stores to Chroma |
| `query_rag.py` | Retrieves top-k chunks → asks GPT-4o |
| `sample.pdf` | Source for embeddings |
| `db/` | Vector store created by Chroma |
