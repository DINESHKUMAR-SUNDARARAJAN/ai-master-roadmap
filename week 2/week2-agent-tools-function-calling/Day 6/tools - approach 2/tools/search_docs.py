from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def get_relevant_chunks(query, k=3):
    db = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings())
    matches = db.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in matches])
