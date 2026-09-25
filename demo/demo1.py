
''' Google genai api key'''


from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
                        # FOR AGENTs module 
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.utilities import GoogleSerperAPIWrapper


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
Memory = MemorySaver()                                                                    #Modle
search = GoogleSerperAPIWrapper

agent = create_agent(
    model=llm,
    tools=[search.run],
    checkpointer=MemorySaver(),
    system_prompt="You are my agent"
)

while True:
    query = input("Aadi: ")

    if query.lower() in ["exit", "quit", "bye"]:                                   
        print("Good Bye 👋")                                
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "aadu"}}
    )

    response = llm.invoke(query)
    print("Ai: ",response.content, "/n")
