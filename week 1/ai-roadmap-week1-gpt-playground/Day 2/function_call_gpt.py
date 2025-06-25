import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a sample function schema
functions = [
    {
        "name": "summarize_text",
        "description": "Summarizes user-provided text in 3 bullet points",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to summarize"},
            },
            "required": ["text"]
        }
    },
    {
        "name": "extract_keywords",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "some article here"},
            }
        }
    }
]

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Summarize this: GPT-4o enables fast reasoning with vision and voice"}
    ],
    functions=functions,
    function_call="auto"
)

print("\n🧠 Function Call Output:\n")
print(response['choices'][0]['message']['function_call'])
