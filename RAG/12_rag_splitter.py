from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/speech.txt", encoding="utf-8")
texts = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)

text_chunk = splitter.split_documents(texts)
len(text_chunk)

print(text_chunk)


