from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

prompts = ChatPromptTemplate.from_messages([
    ("system", "You are a translator and translate input into {language}"),
    ("user", "{query}")
])

final_prompts = prompts.format_messages(
    language="Hinglish",
    query="I love Germany"
)

res = llm.invoke(final_prompts)
print(res.content)