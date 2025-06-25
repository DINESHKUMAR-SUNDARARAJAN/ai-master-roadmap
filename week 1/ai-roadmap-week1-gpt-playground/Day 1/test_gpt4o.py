import openai
import os
import sys
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("Missing OPENAI_API_KEY in your .env file")

user_prompt = sys.argv[1]

if len(sys.argv) < 2:
    print("❌ Please provide a prompt as a command-line argument.")
    sys.exit(1)

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a brutally honest AI coach."},
        {"role": "user", "content": user_prompt}
    ]
)

print("\n🧠 GPT-4o Response:\n")
print(response['choices'][0]['message']['content'])
print("Token usage: "+str(response['usage']['total_tokens']))
print(response)
