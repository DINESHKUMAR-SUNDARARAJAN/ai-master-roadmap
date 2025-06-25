# Week 1 – GPT-4o Playground & Core Engineering

## Days Covered: 1 to 3

### Day 1: GPT-4o API Setup
- Created a secure `.env`-based project to call GPT-4o.
- Tested `openai.ChatCompletion.create()` with system + user prompts.

### Day 2: CLI Prompt + Function Calling
- Created `cli_gpt_assistant.py` to send user input dynamically.
- Built `function_call_gpt.py` with OpenAI function calling.
- Parsed JSON function output for structured responses.

### Day 3: Prompt Chaining + Token Tracking
- Implemented multi-step GPT logic: clean → summarize → analyze.
- Added cost tracking and token monitoring.
- Logged estimates for GPT-4o usage.

## Files Overview

| File | Purpose |
|------|---------|
| `test_gpt4o.py` | Basic GPT API call |
| `cli_gpt_assistant.py` | CLI prompt handler |
| `function_call_gpt.py` | Simulated tool usage with function calling |
| `prompt_chain.py` | Chains multiple GPT tasks |
| `cost_tracker.py` | Logs token usage and cost |