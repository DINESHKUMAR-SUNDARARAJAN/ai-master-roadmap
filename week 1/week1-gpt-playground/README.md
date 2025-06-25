# GPT-4o API Test – Day 1

This project tests GPT-4o API access using Python on a Windows machine.

## Setup

1. Clone the repo
2. Create `.env` and add:
OPENAI_API_KEY=your_openai_key
3. Create and activate virtual env:
python -m venv venv
venv\Scripts\activate
4. Install requirements:
pip install -r requirements.txt
5. Run it:
python test_gpt4o.py [To check the default prompt present in the file]
6. Run it:
python cli_gpt_assistant.py {#promt_to_be_sent} [To check the prompt sent in the terminal]
7. Run it:
python function_call_gpt.py [To check if the default prompt is displayed in the place of summerize_text]

## Output

The script prints GPT-4o's response to a custom user prompt.
