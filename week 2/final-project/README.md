## AI Assistant Agent with Tool Calling & RAG (Week 2 Final Project)

This project demonstrates an AI assistant built using **LangGraph**, **LangChain tools**, and **OpenAI function calling**, capable of:

- Calling multiple tools like year lookup and PDF search
- Retrieving answers from a custom PDF using **ChromaDB + RAG**
- Iterating across multiple tools using LangGraph
- Deployable as a FastAPI backend for real-world use


---

## Features

| Feature                               | Supported |
|--------------------------------------|-----------|
| Tool calling (OpenAI Functions)   | ✅         |
| PDF vector search (RAG)           | ✅         |
| Multi-step LangGraph agent        | ✅         |
| Testable tool APIs                | ✅         |
| FastAPI backend server            | ✅         |
| Render-ready deployment structure | ✅         |

---

## Tools Implemented

| Tool Name              | Purpose                                      |
|------------------------|----------------------------------------------|
| `tool_get_current_year()` | Returns the current year                    |
| `tool_search_docs(query)` | Searches the PDF for query-relevant content |

All tools are defined in `build_tools.py` using `@tool` decorators.

---

## PDF Used

We use `engineering_handbook.pdf` as the source for document search.

It’s indexed using:

- `PyPDFLoader`
- `RecursiveCharacterTextSplitter`
- `OpenAIEmbeddings`
- `Chroma(persist_directory="db")`

---

## Example Query

```bash
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d "{\"query\": \"What is the current year and how do we handle deployments?\"}"

---

## Testing Individual Tools

python test_tools.py

---

## Run Locally

# Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-master-roadmap.git

# Go to final project
cd week\ 2/final-project/

# Install dependencies
pip install -r requirements.txt

# Set your .env
echo "OPENAI_API_KEY=sk-..." > .env

# Run locally
uvicorn main:app --reload





