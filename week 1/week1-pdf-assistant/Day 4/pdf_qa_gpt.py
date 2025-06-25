import openai
import os
from dotenv import load_dotenv
from pdf_reader import extract_text_from_pdf

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load and slice text
pdf_text = extract_text_from_pdf("sample.pdf")
context = pdf_text[:300]  # Keep under token limit

question = "What is the main purpose of this document?"

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a document assistant."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]
)

print("GPT-4o Answer:")
print(response['choices'][0]['message']['content'])
