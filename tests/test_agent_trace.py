from unittest.mock import MagicMock

def run_agent(tools):
    """A simple agent: searches, THEN summarizes(the correct order)."""
    search_result = tools.search("python testing")
    summary = tools.summarize(search_result)
    return summary

def test_agent_calls_tools_in_correct_order():
    # mock the tools so we can RECORD what the agent calls
    mock_tools = MagicMock()
    mock_tools.search.return_value = "search data"
    mock_tools.summarize.return_value = "final summary"

    result = run_agent(mock_tools)

    # TRACE VERIFICATION: check the STEPS, not just the answer.
    mock_tools.search.assert_called_once()
    mock_tools.summarize.assert_called_once_with("search data")
    assert result == "final summary"