from langchain_core.tools import Tool
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_core.tools import StructuredTool
from utilities.search_user_docs import search_documents
from pydantic import BaseModel

class SearchArgs(BaseModel):
    query: str
    user_id: str

tool_search_user_docs = StructuredTool.from_function(
    func=search_documents,
    name="tool_search_user_docs",
    description="Search user vector DB using query and user_id.",
    args_schema=SearchArgs
)
# Export tool list
TOOLS = [tool_search_user_docs]

# Convert to OpenAI-compatible function schemas
OPENAI_FUNCTION_SCHEMAS = [convert_to_openai_function(tool) for tool in TOOLS]



