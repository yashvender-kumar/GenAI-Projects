from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

res = llm.invoke("what is python?")
print(res.content)