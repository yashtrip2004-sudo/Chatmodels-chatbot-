from dotenv import load_dotenv
import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found in .env")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)
while True:
    prompt = input("YOU: ")
    response = model.invoke(prompt)
    print("bot: " + response.content)