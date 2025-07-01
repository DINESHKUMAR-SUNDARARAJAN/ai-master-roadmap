from pydantic import BaseModel
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, FunctionMessage
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from build_tools import TOOLS, OPENAI_FUNCTION_SCHEMAS
from dotenv import load_dotenv

import json

load_dotenv()

# Define state schema
class AgentState(BaseModel):
    messages: List[BaseMessage]

# LLM instance
llm = ChatOpenAI(model="gpt-4o")

# LLM node: calls GPT with function-calling enabled
def llm_node(state: AgentState) -> AgentState:
    messages = state.messages

    response = llm.invoke(  
        messages,
        functions=OPENAI_FUNCTION_SCHEMAS,  # convert @tool defs
        function_call="auto"
    )
    messages.append(response)
    return AgentState(messages=messages)

def func_exec_node(state: AgentState) -> AgentState:
    last = state.messages[-1]

    function_call = last.additional_kwargs.get("function_call")
    if function_call:
        name = function_call["name"]
        args_json = function_call.get("arguments", "{}")
        
        try:
            args = json.loads(args_json)
        except json.JSONDecodeError as e:
            args = {}
            print(f"Failed to parse function arguments: {e}")

        for tool in TOOLS:
            if tool.name == name:
                result = tool.invoke(args)

                # Always serialize to string
                try:
                    serialized = (
                        result if isinstance(result, str)
                        else json.dumps(result, ensure_ascii=False)
                    )
                except Exception as e:
                    serialized = f"Tool error: {e}"

                state.messages.append(
                    FunctionMessage(
                        name=name,
                        content=serialized
                    )
                )
                break

    return state



# Finish node: let GPT produce the final answer
def finish_node(state: AgentState) -> AgentState:
    messages = state.messages
    # ask GPT to wrap up now that tool output is in the stream
    summary = llm.invoke(messages)
    messages.append(summary)
    return AgentState(messages=messages)

def should_continue(state: AgentState) -> str:
    last_msg = state.messages[-1]
    if hasattr(last_msg, "function_call"):
        return "call_tool"
    return "finish"

# Build the graph
graph = StateGraph(state_schema=AgentState)
graph.add_node("llm", RunnableLambda(llm_node))
graph.add_node("exec", RunnableLambda(func_exec_node))
graph.add_node("finish", RunnableLambda(finish_node))

graph.set_entry_point("llm")

# Add a conditional edge (router)
graph.add_conditional_edges("exec", should_continue, {
    "call_tool": "llm",
    "finish": "finish"
})

# LLM always leads to exec
graph.add_edge("llm", "exec")

graph.set_finish_point("finish")

runnable = graph.compile()

# Interface
def run_agent(user_input: str):
    return runnable.invoke(AgentState(messages=[HumanMessage(content=user_input)]))
