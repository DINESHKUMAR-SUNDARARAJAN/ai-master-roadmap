import openai
import os
import sys
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Take prompt from command line
if len(sys.argv) < 2:
    print("Please provide a prompt as a command-line argument.")
    sys.exit(1)

system_role = sys.argv[1]
user_prompt = sys.argv[2]

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_role},
        {"role": "user", "content": user_prompt}
    ]
)

print("\nGPT-4o Response:\n")
print(response['choices'][0]['message']['content'])
print("Token usage: "+str(response['usage']['total_tokens']))
print(response)
