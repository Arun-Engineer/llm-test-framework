import os
from dotenv import load_dotenv
from openai import OpenAI
from src.llm_client import LLMClient

load_dotenv()

def test_capital_answer_contains_paris():
    llm = LLMClient(OpenAI(api_key = os.getenv("OpenAI_API_KEY")))
    answer = llm.ask("what is the capital of France?")

    # PROPERTY check - not exact match! The model might say add
    #"Paris", "The capital is Paris.", "Paris is the capital." - all valid
    assert "paris" in answer.lower()