import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Clean the input text
step1 = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You clean and normalize messy text."},
        {"role": "user", "content": "  HeLLo   ThIs iS   WriTtEn   oDdlY... and i am MaNNGOO! "}
    ]
)
cleaned_text = step1.choices[0].message.content.strip()

# Step 2: Summarize the cleaned text
step2 = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You summarize text in one sentence."},
        {"role": "user", "content": f"Summarize this: {cleaned_text}"}
    ]
)

# step 3: Generate a tweet from the summary
step3 = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You summarize text in one sentence."},
        {"role": "user", "content": f"Generate tweet from this: {cleaned_text}"}
    ]
)
summary = step2.choices[0].message.content.strip()
tweet = step3.choices[0].message.content.strip()
print("\nFinal Summary:")
print(summary)
print("\nTweet: ")
print(tweet)
