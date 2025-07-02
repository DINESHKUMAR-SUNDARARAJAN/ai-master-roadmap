from langchain_core.tools import tool
from utilities.search_docs import search_documents

@tool
def tool_search_docs(query: str) -> dict:
    """Search the indexed engineering handbook PDF and return relevant text chunks for a given user query."""
    result = search_documents(query)
    print(f"search_documents returned: {result}, type: {type(result)}")
    return {"Result": result}

# List of LangChain tool objects
TOOLS = [tool_search_docs]

# Function to convert tools into OpenAI-compatible schema
def tool_to_openai_schema(tool_obj):
    return {
        "name": tool_obj.name,
        "description": tool_obj.description,
        "parameters": tool_obj.args_schema.model_json_schema() if tool_obj.args_schema else {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

OPENAI_FUNCTION_SCHEMAS = [tool_to_openai_schema(tool) for tool in TOOLS]
