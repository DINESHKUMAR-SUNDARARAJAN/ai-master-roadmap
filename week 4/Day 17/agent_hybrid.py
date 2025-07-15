import os
from dotenv import load_dotenv
from version import check_versions
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from google import genai

load_dotenv()
check_versions()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = SystemMessage(content="You are Jarvis, a helpful and intelligent AI assistant.")

gpt = ChatOpenAI(model="gpt-4o")

def run_gemini(user_id: str, query: str, memory: list[str]) -> str:
    contents = [SYSTEM_PROMPT.content] + memory + [query]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )
    return response.text

def run_gpt(user_id: str, query: str, memory: list[HumanMessage]) -> str:
    msgs = [SYSTEM_PROMPT] + memory + [HumanMessage(content=query)]
    resp = gpt.invoke(msgs)
    return resp.content

def run_hybrid(user_id: str, query: str, memory: list) -> str:
    lower = query.lower()
    if any(kw in lower for kw in ["calculate", "code", "divide", "search", "tool", "function"]):
        return run_gpt(user_id, query, memory)
    return run_gemini(user_id, query, memory)
