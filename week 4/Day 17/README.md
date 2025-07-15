# 🤖 Week 4 – Day 1: Hybrid AI Agent (GPT-4o + Gemini 2.5)

In this module, I built a hybrid AI agent that dynamically selects between **OpenAI GPT-4o** and **Gemini 2.5 Flash**, depending on the type of query provided by the user.

---

## 🔍 Objective

- Build a production-ready hybrid AI system that can:
  - Use **GPT-4o** for function-heavy, math, and tool-based queries
  - Use **Gemini 2.5** for contextual, creative, or natural conversation
- Learn how to dynamically route prompts based on their content
- Integrate real-time version control awareness

---

## ⚙️ Technologies Used

| Component     | Version   | Role                                     |
|---------------|-----------|------------------------------------------|
| GPT-4o        | June 2025 | Handles structured reasoning & tools     |
| Gemini 2.5    | July 2025 | Handles conversational and creative tasks|
| LangChain     | v0.2.x    | Used for GPT message management          |
| Google GenAI  | v1.25.0   | New SDK for Gemini API (no `configure()`)|
| FastAPI       | Ready  | (optional for serving as API layer)      |

---

## 🧠 How It Works

- User sends a query via `run_hybrid(user_id, query, memory)`
- If the query contains keywords like `calculate`, `code`, or `divide` → **GPT-4o** is used
- Otherwise, it routes to **Gemini 2.5 Flash**
- Memory and context are handled dynamically between models
- Gemini client is securely initialized using `google-genai` SDK (v1.25+)

---

## 📄 Sample Usage

```python
from agent_hybrid import run_hybrid

print(run_hybrid("dinesh", "What is 12 divided by 4?"))  # uses GPT-4o
print(run_hybrid("dinesh", "Summarize our onboarding principles"))  # uses Gemini 2.5
