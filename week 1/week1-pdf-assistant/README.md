# Week 1 – PDF Q&A Assistant (RAG Lite)

## Day 4

- Used `PyPDF2` to extract text from PDFs.
- Injected sliced PDF content into GPT-4o for document-specific Q&A.
- Validated GPT-4o's ability to reason only with local context.

## Files Overview

| File | Purpose |
|------|---------|
| `pdf_reader.py` | Extracts raw text from PDF |
| `pdf_qa_gpt.py` | Passes content + question to GPT-4o |
| `sample.pdf` | Source document used in QA test |
