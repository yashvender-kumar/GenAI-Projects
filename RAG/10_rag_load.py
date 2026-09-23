from dotenv import  load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
loader = TextLoader("data/speech.txt", encoding="utf-8")
text = loader.load()
len(text)
print(text[0].page_content)


# Text Document Loader in Rag Pipeline  