from langgraph.graph import StateGraph, START, END
from src.state import State
from src.chatbot_node import chatbot_node
from src.tools_node import BasicToolNode, tools
from langgraph.graph.message import add_messages
from langgraph.prebuilt import tools_condition
from langgraph.checkpoint.memory import MemorySaver

# Graph erstellen
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_node("tools", BasicToolNode(tools))

# Kondition: Wenn Tool-Calls existieren, gehe zum Tool-Knoten, sonst beenden.
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")

# Start/End
graph_builder.add_edge(START, "chatbot")

# Memory Saver für Persistenz (optional)
memory = MemorySaver()

# Graph kompilieren
graph = graph_builder.compile(checkpointer=memory)
