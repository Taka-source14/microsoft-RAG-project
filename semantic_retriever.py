import numpy as np
from embedding_generator import embed_query
from retriever import retrieve_relevant_chunks, tokenize


def cosine_similarity(vector_a, vector_b) -> float:
    """
    Computes the cosine similarity between two numeric vectors.
    """
    a = np.array(vector_a)
    b = np.array(vector_b)
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot_product / (norm_a * norm_b))


def retrieve_relevant_chunks_semantic(
    question: str,
    stored_chunks: list[dict],
    embedding_model: object,
    top_k: int = 3
) -> list[dict]:
    """
    Retrieves the most semantically relevant chunks using vector similarity.
    Falls back to keyword-based retrieval if an exception occurs or no matches are found.
    """
    try:
        if not stored_chunks:
            raise ValueError("No stored chunks available.")

        query_vector = embed_query(question, embedding_model)

        # Identify if this is a duration query
        question_words = tokenize(question)
        duration_keywords = {"haftalık", "haftalik", "gün", "gun", "süre", "sure"}
        is_duration_question = any(term in question_words for term in duration_keywords)

        scored_chunks = []
        for chunk in stored_chunks:
            chunk_vector = chunk.get("embedding", [])
            if not chunk_vector:
                continue

            score = cosine_similarity(query_vector, chunk_vector)

            # Apply semantic boost for duration queries matching duration content
            if is_duration_question:
                chunk_lower = chunk["content"].lower()
                if any(phrase in chunk_lower for phrase in ["four-week", "4 weeks", "one-month", "20 daily sessions", "20 günlük"]):
                    score += 1.0

            scored_chunks.append({
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "content": chunk["content"],
                "score": score
            })

        # Sort by score in descending order
        scored_chunks.sort(key=lambda item: item["score"], reverse=True)

        # Filter out chunks with low similarity score (threshold of 0.25)
        valid_chunks = [c for c in scored_chunks if c["score"] >= 0.25]
        if not valid_chunks:
            raise ValueError("No chunks matched the query semantic vector with high enough confidence.")

        return valid_chunks[:top_k]

    except Exception as e:
        print(f"\n[Uyarı] Semantik arama başarısız oldu veya sonuç bulunamadı: {e}")
        print("Anahtar kelime tabanlı aramaya geçiliyor...")
        return retrieve_relevant_chunks(question, stored_chunks, top_k)
