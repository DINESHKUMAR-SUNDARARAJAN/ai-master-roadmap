from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent_graph import run_agent

class ChatRequest(BaseModel):
    user_id: str
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
    response = run_agent(request.user_id, request.query)
    return {"response": response}
