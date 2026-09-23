''' 
groq api key
'''


from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

while True:
    query = input("Aadi: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye 👋")
        break

    res = llm.invoke(query)
    print("AI: ", res.content,"/n")




