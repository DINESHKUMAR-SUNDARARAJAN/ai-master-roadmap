import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

# Load keys
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Setup LangChain Chroma
embedding_model = OpenAIEmbeddings()
db = Chroma(persist_directory="db", embedding_function=embedding_model)

# Query
query = "What can i acheve knowig the contents in the document?"
docs = db.similarity_search(query, k=1)
context = "\n\n".join([doc.page_content for doc in docs])

# OpenAI client (v1+ style)
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant answering based on document context."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
    ]
)

print("Response:\n")
print(response.choices[0].message.content)
