def chunk_text(text: str, max_tokens: int = 400, overlap: int = 50):
    """
    Simple placeholder chunker. Replace with real token-based chunking.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + max_tokens
        chunks.append(" ".join(words[start:end]))
        start += max_tokens - overlap
    return chunks
