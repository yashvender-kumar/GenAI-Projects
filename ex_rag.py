from dotenv import load_dotenv
load_dotenv()

# Imports
from langchain_community.document_loaders import PyPDFLoader                             # For load Pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter                      # For Text Spliter
from langchain_google_genai import GoogleGenerativeAI     # For Api Key
from langchain_chroma import Chroma                                                      # For vector database in which store embeding(number)
from langchain_core.prompts import PromptTemplate                                        # Prompt banane ke liye template (with variables)
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# ---------------- PDF LOADING ----------------

loader = PyPDFLoader("data/cookbook.pdf")
docs = loader.load()

print("PDF Pages:", len(docs))


# ---------------- TEXT SPLITTING ----------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=500
)

splitted_data = splitter.split_documents(docs)

print("Chunks:", len(splitted_data))


# ---------------- EMBEDDINGS + VECTOR STORE ----------------

embeddings = GoogleGenAIEmbeddings(
    model="text-embedding-004"
)

vector_store = Chroma.from_documents(
    documents=splitted_data,
    embedding=embeddings
)


# ---------------- RETRIEVAL ----------------

def get_context(query: str):

    data = vector_store.similarity_search(
        query=query,
        k=4
    )

    context = ""

    for doc in data:
        context += doc.page_content + "\n"

    return {
        "context": context,
        "question": query
    }


# ---------------- LLM ----------------

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash"
)


# ---------------- PROMPT ----------------

prompt = PromptTemplate.from_template("""
You are a helpful cooking assistant that answers questions about recipes,
ingredients, cooking instructions, and food storage tips based on the
"Be a Food Hero" cookbook.

Use only the given context to answer the question.

If the answer is not available in the context, simply say:
"I don't know."

Do not make up information that is not present in the context.

Context:
{context}

Question:
{question}
""")


# ---------------- RAG CHAIN ----------------

rag_chain = (
    RunnableLambda(get_context)
    | prompt
    | llm
)


# ---------------- CHAT LOOP ----------------

while True:

    query = input("User: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye! Have A Nice Day!")
        break

    res = rag_chain.invoke(query)

    print("AI:", res, "\n")