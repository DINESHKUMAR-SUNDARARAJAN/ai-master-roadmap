from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, FunctionMessage
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from memory_store import get_memory, add_to_memory
from build_tools import TOOLS, OPENAI_FUNCTION_SCHEMAS
import json

load_dotenv()

# 1. Define agent state schema
class AgentState(BaseModel):
    messages: List[BaseMessage]
    user_id: str


# 2. LLM node (GPT-4o with function-calling)
llm = ChatOpenAI(model="gpt-4o")

def llm_node(state: AgentState) -> AgentState:
    print(f"\nLLM_NODE for user '{state.user_id}': {[m.content for m in state.messages]}")
    response = llm.invoke(
        state.messages,
        functions=OPENAI_FUNCTION_SCHEMAS,
        function_call="auto"
    )
    add_to_memory(state.user_id, response)
    return AgentState(messages=state.messages + [response], user_id=state.user_id)


# 3. Function execution node
def func_exec_node(state: AgentState) -> AgentState:
    print("\nState Messages: "+str(state.messages))
    last = state.messages[-1]
    print("\nLast: "+str(last))
    print("Has attribute: "+str(hasattr(last, "additional_kwargs.function_call")))

    if hasattr(last, "additional_kwargs"):
        print(type(last.additional_kwargs))
        function_call_values = last.additional_kwargs["function_call"]
        print("\nFunction Call: " + str(function_call_values))
        name = function_call_values["name"]
        args_str = function_call_values["arguments"]
        args = {}
        try:
            args = json.loads(args_str)
        except Exception:
            args = {}
    
        args["user_id"] = state.user_id
        
        print("Arguments sent: " + str(args))

        for tool in TOOLS:
            if tool.name == name:
                print(f"Calling tool: {tool.name} with args: {args}")
                result = tool.invoke(args)
                try:
                    result_str = result if isinstance(result, str) else json.dumps(result)
                except Exception:
                    result_str = str(result)

                state.messages.append(FunctionMessage(name=name, content=result_str))
                break

        print("\nState: "+str(state))
        print(f"GPT requested tool: {name} with args: {args}")
        
    print(f"Tool returned: {result}")
    return state


# 4. Router
def router(state: AgentState) -> str:
    last = state.messages[-1]
    return "call_tool" if hasattr(last.additional_kwargs, "function_call") else "end"


# 5. Final LLM call after tools
def finish_node(state: AgentState) -> AgentState:
    print("FINISH_NODE")
    final_reply = llm.invoke(state.messages)
    return AgentState(messages=state.messages + [final_reply], user_id=state.user_id)


# 6. Build LangGraph
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


# 7. Entry point for API
def run_agent(user_id: str, query: str) -> str:
    memory = get_memory(user_id)
    input_msg = HumanMessage(content=query)
    add_to_memory(user_id, input_msg)

    state = AgentState(messages=memory + [input_msg], user_id=user_id)
    final = runnable.invoke(state)

    print("\nFinal LangGraph Messages:")
    for msg in final["messages"]:
        print(f" - {type(msg).__name__}: {msg.content}")

    ai_response = next(
        (m.content for m in reversed(final["messages"]) if isinstance(m, AIMessage)),
        None
    )
    return ai_response or "I wasn't able to generate a response."
