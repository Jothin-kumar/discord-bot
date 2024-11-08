from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage

model = OllamaLLM(model="gemma2:2b")
with open("chatbot-data.txt", "r") as f:
    data = f.read().split("\n")
with open("chatbot-query-template.txt", "r") as f:
    query_template = f.read()

def get_response(prev_bot_msg, query):
    return model.invoke([
        HumanMessage(data),
        SystemMessage(prev_bot_msg),
        HumanMessage(f"{query_template.format(query)}")
    ])
