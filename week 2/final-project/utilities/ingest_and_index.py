import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Load API key
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load and split PDF
loader = PyPDFLoader("engineering_handbook.pdf")
pages = loader.load()

splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=10)
docs = splitter.split_documents(pages)

# Create vector DB
embedding_model = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embedding=embedding_model, persist_directory="db")

print(f"Indexed {len(docs)} chunks.")
