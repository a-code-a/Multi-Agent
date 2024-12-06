from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import ToolMessage
from typing import Dict
from src.state import State
import json

tool = TavilySearchResults(max_results=2)
tools = [tool]

class BasicToolNode:
    """Ein Beispiel-Tool-Knoten, der Tool-Calls ausführt."""

    def __init__(self, tools: list) -> None:
        self.tools_by_name = {t.name: t for t in tools}

    def __call__(self, inputs: State) -> Dict:
        if messages := inputs.get("messages", []):
            last_message = messages[-1]
        else:
            raise ValueError("Keine Messages im State vorhanden.")

        outputs = []
        if hasattr(last_message, "tool_calls"):
            for tool_call in last_message.tool_calls:
                result = self.tools_by_name[tool_call["name"]].invoke(tool_call["args"])
                outputs.append(
                    ToolMessage(
                        content=json.dumps(result),
                        name=tool_call["name"],
                        tool_call_id=tool_call["id"],
                    )
                )
        return {"messages": outputs}
