import os
from dotenv import load_dotenv

load_dotenv()

# Importations
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser

# Local HuggingFace Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# ===== VECTOR STORE CACHING SETUP  =====
PERSIST_DIR = "./chroma_db"

if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
    print("Local database se Chroma store load ho raha hai...")
    vector_store = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )
else:
    print("PDF parse ho rahi hai aur new vector store ban raha hai...")
    loader = PyPDFLoader("data/cookbook.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
    splitted_data = splitter.split_documents(docs)

    vector_store = Chroma.from_documents(
        documents=splitted_data, 
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
# ============================================================

# Retriever function
def get_context(query: str):
    data = vector_store.similarity_search(query=query, k=4)
    
    context = ""
    for doc in data:
        context += doc.page_content + "\n"
    
    return {"context": context, "question": query}


# Prompt template
prompt = PromptTemplate.from_template("""
    You are a helpful cooking assistant that answers questions about recipes, 
    ingredients, cooking instructions, and food storage tips based on the 
    "Be a Food Hero" cookbook.
    
    Use only the given context to answer the question. If the answer is not 
    available in the context, simply say 'I don't know.' Do not make up 
    information that is not present in the context.

    Context:
    {context}

    Question:
    {question}
""")

# Model initialization
llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)

# RAG Chain Setup
rag_chain = RunnableLambda(get_context) | prompt | llm | StrOutputParser()

# Interactive Loop
while True:
    query = input("User: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye Have A Nice Day!")
        break

    res = rag_chain.invoke(query)
    print("AI:", res, "\n")

