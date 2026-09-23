from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

res = llm.invoke("Hey where is france and germany?")

# Sirf clean text nikalne ke liye:
if isinstance(res.content, list):
    text = "".join(part["text"] for part in res.content if part.get("type") == "text")
    print(text)
else:
    print(res.content)
