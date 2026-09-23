from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

promts = [
    {"role":"user", "content": "Hello, my name is aadi"},
    {"role":"ai", "content": "Hello,  aadi! How can I assist you t..."},
    {"role":"user", "content":"What is My name ?"}
]


# History list - yehi memory ka kaam karega
history = []

print("Chat shuru! Exit karne ke liye 'exit', 'quit' ya 'bye' likho.\n")

while True:
    query = input("User: ")

    if query.lower() in  ["exit", "quit", "bye"]:
        print("Goodbye")
        break

       # User ka message history mein add karo
    history.append({"role": "user", "content": query})
    print("User: ", query)

       # Poori history LLM ko bhejo (isse purana context yaad rehta hai)
    res = llm.invoke(history)

        # Yaha content clean kar rahe hain - agar list hai toh sirf text nikalo
    if isinstance(res.content,list):
        text = res.content[0]["text"]
    else:
         text = res.content


        # AI ka response bhi history mein add karo
    history.append({"role": "ai", "content": res.content})
    print("Ai: ", res.content,"\n")

