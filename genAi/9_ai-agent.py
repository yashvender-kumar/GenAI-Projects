from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are agent and you can search anything from google",
    checkpointer= MemorySaver()
)

while True:
    quiz = input("You:")                           # is statement se sirf ans projntn HOGA  or isme khuchu text nahi hoga
    if quiz.lower() in ["exit","quit"]:
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": quiz}]},
        {"configurable": {"thread_id": "yash"}}
    )

     # sirf final answer nikal ke print karo, poora object nahi
    answer = (response["messages"][-1].content)
    print("Bot:", answer)

