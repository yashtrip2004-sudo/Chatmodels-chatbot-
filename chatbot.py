from dotenv import load_dotenv
import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage ,SystemMessage, HumanMessage 
load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found in .env")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=token,
)
print("choose the way you want to chat with the bot:")
print("press 1 for a funny chatbot")
print("press 2 for a sad chatbot"
      )
print("press 3 for a sarcastic chatbot")
mode = input("Enter your choice (1, 2, or 3): ")
if mode == '1': 
    messages=[
        SystemMessage(content="You are a funny ai agent.")
    ]
elif mode == '2':
    messages=[
        SystemMessage(content="You are a sad ai agent.")
    ]
elif mode == '3':
    messages=[
        SystemMessage(content="You are a sarcastic ai agent.")
    ]


model = ChatHuggingFace(llm=llm)
print("Chatbot is ready. Type your message and press Enter (type 'exit' to quit).")
while True:
    prompt = input("YOU: ")
    if prompt.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    messages.append( HumanMessage(content=prompt))
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("bot: " + response.content)

    