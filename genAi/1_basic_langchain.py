#  Load Env Variable 


from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_groq import ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile")

res = llm.invoke("what is python?")
print(res.content)

