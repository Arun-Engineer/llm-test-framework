import os, pytest
from dotenv import load_dotenv
from openai import OpenAI
from src.llm_client import LLMClient

load_dotenv()

def classify_sentiment(text: str) -> str:
    llm = LLMClient(OpenAI(api_key = os.getenv("OPENAI_API_KEY")))
    prompt = f"Classify the sentiment as only 'positive' or 'negative'. Text: {text}"
    return llm.ask(prompt).lower()

# the EVAL GRID: many (input, expected) cases
@pytest.mark.parametrize("text, expected",[
    ("I love this product!", "positive"),
    ("This is terrible and broken", "negative"),
    ("Best purchase ever", "positive"),
    ("Worst experience of my life", "negative"),
])
def test_sentiment_classification(text, expected):
    result = classify_sentiment(text)
    assert expected in result