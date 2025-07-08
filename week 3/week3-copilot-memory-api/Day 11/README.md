# Week 3 – Day 11: LangGraph Multi-Tool Agent with Sequential Reasoning

## Objective
Enhance your GPT-4o agent to intelligently chain together multiple tool calls in response to a single query — just like a human would break down a problem and take actions step by step.

---

## Features Added

### Sequential Tool Execution
- Agent can now call multiple tools in one response loop
- GPT → tool → GPT → tool → final answer

### Router Logic
- Dynamically checks if GPT wants to call another function
- Loops until no more tool calls requested

## Files Updated

- `agent_graph.py` — supports multiple tool calls
- `build_tools.py` — verified tool names and structure
- `memory_store.py` — stores per-user messages
- `run_agent()` — now handles complex flow transparently

## Test Cases

| Prompt | Expected Behavior |
|--------|-------------------|
| "What is our onboarding process and what year is it?" | 2 tool calls → single GPT summary |
| "Give me the current year" | Calls only year tool |
| "What does our handbook say about deployment?" | Only search_docs tool |