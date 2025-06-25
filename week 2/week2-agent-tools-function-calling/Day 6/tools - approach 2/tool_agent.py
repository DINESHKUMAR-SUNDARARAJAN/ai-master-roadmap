import os
from dotenv import load_dotenv
from openai import OpenAI
from tools.search_docs import get_relevant_chunks

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Define system prompt
def get_response_from_agent(user_input: str) -> str:
    context = get_relevant_chunks(user_input)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a retrieval-augmented assistant. Use the provided context to answer."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{user_input}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_query = input("Ask your assistant: ")
    answer = get_response_from_agent(user_query)
    print("\nGPT-4o Agent says:\n")
    print(answer)
