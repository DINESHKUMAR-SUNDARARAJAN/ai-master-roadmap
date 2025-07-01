# test_tools.py
from build_tools import tool_get_current_year, tool_search_docs, TOOLS, OPENAI_FUNCTION_SCHEMAS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, FunctionMessage
load_dotenv()

class AgentState(BaseModel):
    messages: List[BaseMessage]

llm = ChatOpenAI(model="gpt-4o")
def test_get_current_year():
    print("Testing tool_get_current_year:")
    result = tool_get_current_year.invoke({})
    print("Output:", result)

def test_search_docs():
    print("\nTesting tool_search_docs:")
    query = "deployment process"
    result = tool_search_docs.invoke({"query": query})
    print("Output:", result)

def verification(state: AgentState) -> AgentState:
    messages = state.messages
    result = llm.invoke(  
        messages,
        functions=OPENAI_FUNCTION_SCHEMAS,  # convert @tool defs
        function_call="auto"
    )
    print(result)

if __name__ == "__main__":
    verification(AgentState(messages=[HumanMessage(content="What are our engineering principles according to the handbook?")]))
