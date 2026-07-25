import re
from collections import Counter


TURKISH_STOPWORDS = {
    "ve", "veya", "ile", "için", "bu", "şu", "o", "bir", "de", "da",
    "ne", "nedir", "nasıl", "hangi", "nelerdir", "mi", "mı", "mu", "mü",
    "olarak", "olan", "olur", "var", "yok", "kaç", "kac", "kadar",
    "mıdır", "midir", "mudur", "müdür", "mıyız", "miyiz", "ise", "ki",
    "en", "daha", "çok", "cok", "gibi", "şey", "sey"
}

# Turkish-English keyword normalization and expansion map
KEYWORD_EXPANSION = {
    "haftalık": ["hafta", "week", "weeks", "four", "month", "session", "sessions"],
    "haftalik": ["hafta", "week", "weeks", "four", "month", "session", "sessions"],
    "hafta": ["haftalık", "week", "weeks", "four", "month", "session", "sessions"],
    "gün": ["day", "days"],
    "gun": ["day", "days"],
    "günde": ["day", "days"],
    "gunde": ["day", "days"],
    "günü": ["day", "days"],
    "gunu": ["day", "days"],
    "aşama": ["phase", "phases"],
    "asama": ["phase", "phases"],
    "aşaması": ["phase", "phases"],
    "asamasi": ["phase", "phases"],
    "program": ["course", "curriculum"],
    "programı": ["course", "curriculum"],
    "programi": ["course", "curriculum"],
    "sunum": ["presentation", "presentations", "presenting"],
    "sunumu": ["presentation", "presentations", "presenting"],
    "test": ["testing", "tests"],
    "doküman": ["document", "documents"],
    "dokuman": ["document", "documents"],
    "dokümanı": ["document", "documents"],
    "dokumani": ["document", "documents"]
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
    Keeps words longer than 1 character or digits (like 1, 5, 3).
    """
    text = turkish_lower(text)
    text = re.sub(r"[^a-zA-Zçğıöşü0-9\s]", " ", text)

    words = text.split()

    meaningful_words = [
        word for word in words
        if word not in TURKISH_STOPWORDS and (len(word) > 1 or word.isdigit())
    ]

    return meaningful_words


def calculate_keyword_score(question: str, chunk_content: str) -> int:
    """
    Calculates a simple keyword-based similarity score
    between the user question and a document chunk.
    Includes keyword expansion and duration search boosting.
    """
    question_words = tokenize(question)
    chunk_words = tokenize(chunk_content)

    chunk_word_counts = Counter(chunk_words)

    score = 0

    for word in question_words:
        # Check original word match
        word_score = chunk_word_counts.get(word, 0)

        # Check expanded words match
        if word in KEYWORD_EXPANSION:
            for alias in KEYWORD_EXPANSION[word]:
                word_score += chunk_word_counts.get(alias, 0)

        score += word_score

    # Apply score boost for duration questions matching duration content
    # Use question_words list to check exact matching tokens instead of substring in raw text
    duration_keywords = {"haftalık", "haftalik", "gün", "gun", "süre", "sure"}
    is_duration_question = any(term in question_words for term in duration_keywords)
    if is_duration_question:
        chunk_lower = chunk_content.lower()
        if any(phrase in chunk_lower for phrase in ["four-week", "4 weeks", "one-month", "20 daily sessions", "20 günlük"]):
            score += 15

    return score


def retrieve_relevant_chunks(question: str, chunks: list[dict], top_k: int = 3) -> list[dict]:
    """
    Retrieves the most relevant chunks for a given question.
    """
    scored_chunks = []
    question_words = tokenize(question)
    min_required_matches = 2 if len(question_words) >= 2 else 1

    for chunk in chunks:
        score = calculate_keyword_score(question, chunk["content"])

        if score >= min_required_matches:
            scored_chunks.append({
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "content": chunk["content"],
                "score": score
            })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]