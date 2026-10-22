import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str) -> list[float]:

    """Convert text into a vector (embedding)"""
    response = client.embeddings.create(model = "text-embedding-3-small", input = text)
    return response.data[0].embedding

def cosine_similarity(a: list[float], b: list[float]) -> float:
    """How close in MEANING are two vector? 1=same, 0= unrelated."""

    a,b = np.array(a), np.array(b)
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))

def semantic_faitfullness(answer: str, source: str) -> float:
    """Faithfullness by MEANING, not word overlap."""
    answer_vec = get_embedding(answer)
    source_vec = get_embedding(source)
    return cosine_similarity(answer_vec, source_vec)

if __name__ == "__main__":
    # The exact case wrod-overlap FAILED on:
    answer = "The CEO resigned"
    source = "The chief executive stepped down"
    print("Semantic faithfullness:", semantic_faitfullness(answer, source))