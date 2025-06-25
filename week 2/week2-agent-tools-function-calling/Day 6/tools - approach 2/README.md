# Week 2 – GPT-4o Agent with Tools + Function Calling

## Day 6

- Built a LangChain `initialize_agent()` powered by GPT-4o.
- Wrapped custom Python functions (math, datetime) as LangChain tools.
- GPT-4o selects tools via OpenAI function calling automatically.

## Files Overview

| File | Purpose |
|------|---------|
| `tools/utils.py` | Custom tool functions (e.g. multiply, get year) |
| `build_tools.py` | Converts Python functions into LangChain tools |
| `run_agent.py` | Runs the GPT-4o agent and selects tools based on query |

## Example Query
> “What is the current year and what is 45 * 11?”
