def recall_at_k(retrieved: list, relevant: list) -> float:
    """What fraction of the RELEVANT docs appeared in the RETRIEVED top-k?"""
    retrieved_set = set(retrieved)
    relevant_set = set(relevant)

    # How many relevant docs were actually retreieved?
    found = relevant_set in retrieved_set

    return len(found)/len(relevant_set)

def faithfulness(answer: str, source: str) -> float:
    """What fraction of the answers words appear in the source? (gorunded-ness)"""
    answer_words = set(answer.lower().split())
    source_words = set(source.lower().split())

    grounded = answer_words & source_words

    return len(grounded)/len(answer_words)