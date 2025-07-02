from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def search_documents(query: str, k=3) -> dict:
    print(f"Searching docs for query: {query}")

    # Retrieve pdf content from DB
    db = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings())
    results = db.similarity_search(query, k=k)

    if not results:
        print("No results found.")
        return {"context": "No relevant content found in the document."}
    
    # Joining the obtained contents as chunks
    context = "\n\n".join([doc.page_content for doc in results])
    print(f"Retrieved {len(results)} chunks.")
    return {"context": context}
