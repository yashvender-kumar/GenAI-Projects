from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool


@tool
def add_numbers(a: int, b: int):
    """
    It will return the sum of two numbers

    Args:
        a = Number One
        b = Number Two
    """
    return a + b


@tool
def multiply_numbers(a: int, b: int):
    """
    It will return the product of two numbers

    Args:
        a = Number One
        b = Number Two
    """
    return a * b


result = add_numbers.invoke({"a": 12, "b": 1})
print("Direct tool test:", result)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

agent = create_agent(
    model=llm,
    tools=[add_numbers, multiply_numbers],
    system_prompt="You are my maths teacher and always use tools for calculation",
)

response = agent.invoke({"messages": [{"role": "user", "content": "what is 2 + 5 ?"}]})
print(response)
