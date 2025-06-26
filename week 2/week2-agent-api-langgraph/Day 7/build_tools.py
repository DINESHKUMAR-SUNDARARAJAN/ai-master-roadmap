from langchain_core.tools import tool
from tools.utils import get_current_year, multiply_numbers
from tools.search_docs import search_documents

@tool
def tool_get_current_year() -> dict:
    """Returns the current year."""
    return get_current_year()

@tool
def tool_multiply(x: float, y: float) -> dict:
    """Multiplies two numbers."""
    return multiply_numbers(x, y)

@tool
def tool_search_docs(query: str) -> dict:
    """Returns context from the document based on the query."""
    return search_documents(query)

TOOLS = [tool_get_current_year, tool_multiply, tool_search_docs]