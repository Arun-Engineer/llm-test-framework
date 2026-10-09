from unittest.mock import MagicMock
from src.llm_client import LLMClient

def test_ask_strips_whitespace():
    # build a FAKE response object shaped like OpenAI's
    fake_client = MagicMock()

    fake_client.chat.completions.create.return_value.choices[0].message.content = " Paris "

    llm = LLMClient(fake_client)

    result = llm.ask("Capital of France?")

    assert result == "Paris"