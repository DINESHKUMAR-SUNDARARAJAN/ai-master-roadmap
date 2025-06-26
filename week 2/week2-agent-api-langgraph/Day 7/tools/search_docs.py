from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def search_documents(query: str, k: int = 3) -> dict:
    db = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings())
    results = db.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in results])
    return {"context": context}
