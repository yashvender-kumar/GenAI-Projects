# LLM
# TOOL -----Google Search Tool
# Agent
# Memory
# Streming
# Web Interface


from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash",streaming =True)
search = GoogleSerperAPIWrapper()
tools = [search.run]
memory = MemorySaver()

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []

agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="You are my personal agent"
)

print(st.session_state.memory)

#### Builiding Web Interface..

st.subheader("Hello User")
for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask me ?")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})

    response = agent.stream(
        {"messages":[{"role": "user", "content":query}]},
        {"configurable": {"thread_id": "1"}},
        stream_mode = "messages"
    )

    ai_container = st.chat_message("assistant")
    with ai_container:
        space = st.empty()
    message = ""
    for chunk in response:
        content = chunk[0].content

        if isinstance(content, list):
            text = "".join(
                block.get("text", "") if isinstance(block, dict) else str(block)
                for block in content
            )
        else:
            text = content

        message = message + text
        space.write(message)

    st.session_state.history.append({"role": "assistant", "content": message})




  




    
''' 

streamlit run Projects_Ai_agents/project.py


'''