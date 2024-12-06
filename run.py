from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from src.graph_definition import graph

def main():
    # Konfiguration für den Thread (Session)
    config = {"configurable": {"thread_id": "1"}}

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Auf Wiedersehen!")
            break

        # State-Update durch den Graphen, "stream_mode=values" gibt uns die Events nach und nach
        events = graph.stream({"messages": [("user", user_input)]}, config, stream_mode="values")
        for event in events:
            # Wenn neue Nachrichten generiert wurden, geben wir die letzte AI-Nachricht aus
            if "messages" in event:
                ai_msg = event["messages"][-1]
                print("Assistant:", ai_msg.content)

if __name__ == "__main__":
    main()
