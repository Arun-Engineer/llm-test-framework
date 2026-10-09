import os
from dotenv import load_dotenv
from openai import OpenAI
from src.llm_client import LLMClient

load_dotenv()

# create the real client using the key from the environment
real_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

llm = LLMClient(real_client)
answer = llm.ask("What is the capital of France? Answer in one word.")
print("Model said: ", answer)