while True:
    query = input("User: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("Good Bye Have A Nice Day!")
        break

res = rag_chain.invoke(query)
print("AI:", res, "\n")  