from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("🤖Ask Anything-Ai Qna Bot")
st.markdown("Made by Aadi☺️ help of langchain tool")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = llm.invoke(query)

    if isinstance(res.content, list):
        text = res.content[0]["text"]
    else:
        text = res.content

    st.chat_message("ai").markdown(text)
    st.session_state.messages.append({"role": "ai", "content": text})


''' 

streamlit run apps/1_QNA.py  


'''