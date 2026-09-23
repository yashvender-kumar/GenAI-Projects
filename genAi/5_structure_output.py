from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

# Discuss the problem first

text = "Hello my name is aadi,"
"email is bla bla and age is la la"

res = llm.invoke(f"please only gave me name, email and age from this text: {text}")

print(res.content)
