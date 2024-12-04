from crewai import crew, task, agent
from crewai_tools import SerperDevTools
from langchain_ibm import WatsonxLLM
import os

os.environment["antrophic_api_key"] = ""
os.environ["SERPER_API_KEY"] = "e732b7720321deebef189e59177ff902c3fa4088"