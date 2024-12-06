from langchain_anthropic import ChatAnthropic
from typing import Dict
from src.state import State

# Ersetze das Modell und Key nach Bedarf
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

def chatbot_node(state: State) -> Dict:
    """Nimmt den aktuellen State mit user-/system-/AI-Nachrichten
    und ruft das Modell an, um eine neue AI-Message zurückzubekommen."""
    new_message = llm.invoke(state["messages"])
    # Rückgabeformat: Dict mit State-Updates
    return {"messages": [new_message]}
