# Week 2 – GPT-4o Agent with Tools + Function Calling

## Day 6

- Utilized the db created in Day 5
- Wrapped custom Python functions (get_relevant_chunks) as LangChain tools.
- GPT-4o selects tools via OpenAI function calling automatically.

## Files Overview

| File | Purpose |
|------|---------|
| `tool_agent.py` | Runs the GPT-4o agent with all available tools |
| `tools/search_docs.py` | Wraps Chroma similarity search as a tool |