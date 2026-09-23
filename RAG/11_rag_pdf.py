from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("data/Resume.pdf")
docs = loader.load()
len(docs)
print(docs[0].page_content)