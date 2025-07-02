from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from pydantic import BaseModel
from typing import List
from memory_store import get_memory, add_to_memory
from dotenv import load_dotenv
from build_tools import OPENAI_FUNCTION_SCHEMAS

load_dotenv()

# 1. State schema
class AgentState(BaseModel):
    messages: List[BaseMessage]
    user_id: str

llm = ChatOpenAI(model="gpt-4o")

# 2. LLM node
def llm_node(state: AgentState) -> AgentState:
    response = llm.invoke(state.messages, functions=OPENAI_FUNCTION_SCHEMAS, function_call='auto')
    add_to_memory(state.user_id, response)
    return AgentState(messages=state.messages + [response], user_id=state.user_id)

from langchain_core.messages import FunctionMessage
from build_tools import TOOLS
import json

def func_exec_node(state: AgentState) -> AgentState:
    last = state.messages[-1]

    if hasattr(last, "function_call"):
        name = last.function_call.name
        args_str = last.function_call.arguments
        try:
            args = json.loads(args_str)
        except Exception as e:
            args = {}

        for tool in TOOLS:
            if tool.name == name:
                result = tool.invoke(args)
                try:
                    result_str = result if isinstance(result, str) else json.dumps(result)
                except:
                    result_str = str(result)

                state.messages.append(
                    FunctionMessage(name=name, content=result_str)
                )
                break

    return state

def router(state: AgentState) -> str:
    last = state.messages[-1]
    if hasattr(last, "function_call"):
        return "call_tool"
    return "end"

def finish_node(state: AgentState) -> AgentState:
    final_reply = llm.invoke(state.messages)
    return AgentState(messages=state.messages + [final_reply], user_id=state.user_id)


graph = StateGraph(state_schema=AgentState)

graph.add_node("llm", RunnableLambda(llm_node))
graph.add_node("exec", RunnableLambda(func_exec_node))
graph.add_node("finish", RunnableLambda(finish_node))
graph.add_node("end", RunnableLambda(lambda s: s))

graph.set_entry_point("llm")
graph.add_edge("llm", "exec")
graph.add_conditional_edges("exec", router, {
    "call_tool": "llm",
    "end": "finish"
})
graph.set_finish_point("finish")

runnable = graph.compile()

def run_agent(user_id: str, query: str) -> str:
    memory = get_memory(user_id)
    input_msg = HumanMessage(content=query)
    add_to_memory(user_id, input_msg)

    state = AgentState(messages=memory + [input_msg], user_id=user_id)
    final = runnable.invoke(state)

    print("`Final LangGraph Output:")
    for msg in final["messages"]:
        print(f" - {type(msg).__name__}: {msg.content}")

    ai_response = next(
        (m.content for m in reversed(final["messages"]) if isinstance(m, AIMessage)),
        None
    )

    return ai_response or "I wasn't able to generate a response."


