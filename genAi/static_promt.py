# Google Genai

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

prompts = [
    ("system", "You are python developer"),
    ("user", "How to become a GenAi Engineer in future")
]

res = llm.invoke(prompts)
print(res.content)