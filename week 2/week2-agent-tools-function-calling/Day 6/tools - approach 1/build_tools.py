from langchain.tools import tool
from tools.utils import get_current_year, multiply_numbers

@tool
def tool_current_year() -> dict:
    """Returns the current year"""
    return get_current_year()

@tool
def tool_multiply(x: float, y: float) -> dict:
    """Multiplies two numbers and returns the result"""
    return multiply_numbers(x, y)

# Export tool list
TOOLS = [tool_current_year, tool_multiply]
