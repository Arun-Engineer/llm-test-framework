from openai import OpenAI

class LLMClient:
    def __init__(self, client: OpenAI, model: str = "gpt-4o-mini"):
        # The OpenAI client is PASSED IN (so tests can inject a mock)
        self.client = client
        self.model = model

    def ask(self, prompt: str) -> str:
        """Send a prompt to the model, return the text answer."""
        response= self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "user", "content": prompt}],
        )
        # extract just the text from the response object
        return response.choices[0].message.content.strip()
    