from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader(web_path="https://chatgpt.com/work/?utm_source=google&utm_medium=paid_search&c_id=24187971532&c_agid=199508729213&c_crid=822392024321&c_kwid=kwd-1944766109507&c_ims=&c_pms=9061700&c_nw=g&c_dvc=c&gad_source=1&gad_campaignid=24187971532&gbraid=0AAAAA-I0E5dcrvWCIgzxoICHDbeKWBuVq&gclid=Cj0KCQjw5bjVBhCiARIsAJzMVnRQar34Wj3JIfvw5uJlsuw49-5vu8Upm-h0PNGfRTi1Z9hSxEMkfIoaAjaVEALw_wcB")

docs = loader.load()
len(docs)
print(docs[0].page_content)

#Web apge Loader by using Rag based system

