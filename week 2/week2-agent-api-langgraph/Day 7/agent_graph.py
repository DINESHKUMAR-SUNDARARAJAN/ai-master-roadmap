from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from build_tools import TOOLS
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from langchain_core.messages import BaseMessage


load_dotenv()

class AgentState(BaseModel):
    messages: List[BaseMessage]

# Define the system prompt
system_prompt = (
    "You are a helpful assistant. Use tools when needed to answer the user's query."
)

llm = ChatOpenAI(model="gpt-4o")

# Define agent node (LLM call)
def agent_node(state: dict) -> dict:
    messages = state.messages
    response = llm.invoke(messages)
    messages.append(response)
    return {"messages": messages}

# Set up LangGraph
graph = StateGraph(state_schema=AgentState)

graph.add_node("agent", RunnableLambda(agent_node))
graph.set_entry_point("agent")
graph.set_finish_point("agent")

runnable = graph.compile()

# Interface to call this
def run_agent(user_input: str):
    return runnable.invoke({
        "messages": [HumanMessage(content=user_input)]
    }, config=RunnableConfig())
