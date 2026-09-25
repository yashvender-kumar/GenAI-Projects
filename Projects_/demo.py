
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool

# 1. LLM Setup
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
memory = MemorySaver()

# 2. Fix Search Tool Declaration
search_wrapper = GoogleSerperAPIWrapper()
search_tool = Tool(
    name="google_search",
    description="Search Google for recent information, current time, news, and live updates.",
    func=search_wrapper.run
)

# 3. Create Agent
agent = create_agent(
    model=llm,
    tools=[search_tool],  # Directly pass the tool object
    checkpointer=memory,
    system_prompt="You are a helpful AI assistant."
)

while True:
    query = input("Aadi: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye 👋")
        break

    # Run agent and fetch latest message
    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "aadu"}}
    )

    # Clean response print
    ai_message = response["messages"][-1].content
    print("Ai:", ai_message, "\n")