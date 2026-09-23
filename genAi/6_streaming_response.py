from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", streaming = True)

while True:
    quiz = input("aadi:")

    if quiz.lower() in ["exit", "quit", "bye"]:
        print("Good bye")

    print("Ai: ",end="")
    response = llm.stream(quiz)
    for chunk in response:
        print(chunk.content,end="",flush=True)
        print()  # naya line, taki agla input clean line se shuru ho






    
