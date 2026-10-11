def normalize(text: str) -> str:
    """Strip formatting tricks so obfuscated leaks cant hide."""
    text = text.lower()
    for char in [" ", "-", ".", "_", "*"]:
        text = text.replace(char, "")
    return text

def secret_leaked(output: str, secret: str) -> bool:
    """The ORACLE: did the secret leak, even if obfuscated."""
    clean_output = normalize(output)
    clean_secret = normalize(secret)

    return clean_secret in clean_output