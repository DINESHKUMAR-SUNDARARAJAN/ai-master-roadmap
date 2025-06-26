# Week 2 – Day 7: GPT-4o Tool Agent API with LangGraph + FastAPI

This project refactors the GPT-4o agent into a **LangGraph-based architecture** and serves it via a **FastAPI** backend.

---

## What This Project Does

- Builds a GPT-4o-powered agent using **LangGraph**
- Supports **OpenAI function calling** for tools
- Includes a **ChromaDB-powered document search tool**
- Includes custom tools like `multiply_numbers()` and `get_current_year()`
- Serves the agent via a **FastAPI `/chat` endpoint**

---

## Core Technologies

| Tool | Purpose |
|------|---------|
| `LangGraph` | Orchestrates GPT tool-using agent logic |
| `LangChain + OpenAI` | Manages GPT-4o calls with tool calling |
| `ChromaDB` | Vector store to power document retrieval |
| `FastAPI` | Web API to expose the agent |
| `pydantic` | Defines the agent’s state schema |
| `uvicorn` | ASGI server to run FastAPI |