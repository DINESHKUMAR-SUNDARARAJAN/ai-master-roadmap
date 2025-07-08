# 📚 Week 3 – Day 2: User-Specific GPT Agent with File Uploads & Memory

## Objective
Build a personalized AI assistant that:
- Accepts user-specific file uploads (PDFs)
- Stores those documents in per-user vector databases
- Lets GPT answer queries using tool calling + LangGraph
- Tracks chat memory per user
- Exposes everything via FastAPI `/chat` and `/upload/{user_id}`

---

## Features Built

### File Uploads
- POST `/upload/{user_id}`
- Accepts PDF files
- Stores in `uploads/{user_id}/filename.pdf`
- Chunks + indexes using `Chroma.from_documents(..., persist_directory=db/{user_id})`

### Tools
- `tool_search_user_docs(query: str, user_id: str)` — uses `StructuredTool`

### LangGraph Agent Flow
- Tracks `messages` and `user_id` using `AgentState`
- Loops: GPT → Function Call → Execution → GPT again → Final response
- Built using `llm_node`, `exec_node`, `router`, and `finish_node`

### Memory Store
- Per-user chat memory
- Retrieved before agent execution
- Updated with every new message or tool result

---

## API Endpoints

### Upload PDF
```http
POST /upload/dinesh
Body: form-data
File: engineering_handbook.pdf
