import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from build_tools import TOOLS

load_dotenv()
llm = ChatOpenAI(model="gpt-4o")

agent = initialize_agent(
    tools=TOOLS,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Ask the agent to decide
query = "What is the current year, and what is 45 * 11?"
response = agent.invoke(query)
print("Agent Response:\n", response)
