import re
from collections import Counter


TURKISH_STOPWORDS = {
    "ve", "veya", "ile", "için", "bu", "şu", "o", "bir", "de", "da",
    "ne", "nedir", "nasıl", "hangi", "nelerdir", "mi", "mı", "mu", "mü",
    "olarak", "olan", "olur", "var", "yok"
}


def turkish_lower(text: str) -> str:
    """
    Converts Turkish characters to lowercase correctly.
    'İ' -> 'i', 'I' -> 'ı'
    """
    text = text.replace("İ", "i").replace("I", "ı")
    return text.lower()


def tokenize(text: str) -> list[str]:
    """
    Converts text into clean lowercase words.
    """
    text = turkish_lower(text)
    text = re.sub(r"[^a-zA-Zçğıöşü0-9\s]", " ", text)

    words = text.split()

    meaningful_words = [
        word for word in words
        if word not in TURKISH_STOPWORDS and len(word) > 1
    ]

    return meaningful_words


def calculate_keyword_score(question: str, chunk_content: str) -> int:
    """
    Calculates a simple keyword-based similarity score
    between the user question and a document chunk.
    """
    question_words = tokenize(question)
    chunk_words = tokenize(chunk_content)

    chunk_word_counts = Counter(chunk_words)

    score = 0

    for word in question_words:
        score += chunk_word_counts.get(word, 0)

    return score


def retrieve_relevant_chunks(question: str, chunks: list[dict], top_k: int = 3) -> list[dict]:
    """
    Retrieves the most relevant chunks for a given question.
    """
    scored_chunks = []

    for chunk in chunks:
        score = calculate_keyword_score(question, chunk["content"])

        if score > 0:
            scored_chunks.append({
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "content": chunk["content"],
                "score": score
            })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]