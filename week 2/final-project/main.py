from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent_graph import run_agent
from langchain_core.messages import AIMessage

class ChatRequest(BaseModel):
    query: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/chat")
async def chat(request: ChatRequest):
    result = run_agent(request.query)
    content = result["messages"][-1].content
    return {"response": content}
