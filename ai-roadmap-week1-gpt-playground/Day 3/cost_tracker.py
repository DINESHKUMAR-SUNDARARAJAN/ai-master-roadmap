import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Summarize GPT-4o’s main strengths in 3 points."}
    ]
)

tokens_used = response['usage']['total_tokens']
cost = tokens_used * 0.000005  # GPT-4o input+output = $0.005 per 1K tokens

print(f"🔢 Tokens used: {tokens_used}")
print(f"💵 Estimated cost: ${cost:.6f}")
print("🧠 GPT Response:")
print(response['choices'][0]['message']['content'])
