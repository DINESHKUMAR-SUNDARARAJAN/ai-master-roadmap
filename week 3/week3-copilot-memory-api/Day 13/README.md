# Week 3 – Day 11: Streaming GPT Responses with LangGraph + FastAPI

---

## Goal

Today, we enabled **real-time GPT streaming** using:
- `LangGraph` `.stream()` API
- `FastAPI` + `StreamingResponse`
- A testable `run_agent_stream()` function
- Verified with `curl` and `requests`

---

## 🚀 Key Features

| Feature              | Description                                                |
|----------------------|------------------------------------------------------------|
| Streaming GPT      | GPT answers are streamed chunk-by-chunk (token-level UX)   |
| Updated Agent      | Agent emits only `AIMessage` chunks, cleanly streamed      |
| FastAPI Route      | `/chat/stream` supports streamed interaction               |
| Local Test Script  | `run_local.py` prints tokens as they arrive                |

---