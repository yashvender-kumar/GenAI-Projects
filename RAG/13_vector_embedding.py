from dotenv import load_dotenv
load_dotenv()

Document = [
    "Hello Aadi how are you",
    "Hello yash how are you",
    "Hell0 pranav how are you"
]

from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

vector = embedding.embed_documents(Document)

print(len(vector[0]))