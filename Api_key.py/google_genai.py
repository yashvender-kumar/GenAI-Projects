
''' Google genai api key'''


from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

while True:
    query = input("Aadi: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye 👋")
        break

    res = llm.invoke(query)
    print("Ai: ",res.content, "/n")
