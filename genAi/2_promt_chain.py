from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

prompts = [
    {"role":"system","content":"You are a  translator and translate input into franch"},
        {"role":"system","content":"You are a  translator and translate input into spanish"},
            {"role":"system","content":"You are a  translator and translate input into italian"},
    {"role":"user","content":"I love Germany"}
]

res = llm.invoke(prompts)
print(res.content)
