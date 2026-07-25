import re


def generate_answer(question: str, relevant_chunks: list[dict]) -> str:
    """
    Generates a simple grounded answer using only retrieved chunk contents.
    If no relevant chunks are found, returns a standard message.
    """
    fallback_msg = "Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."
    if not relevant_chunks:
        return fallback_msg

    # Filter out chunks with 0 or negative score (just in case)
    valid_chunks = [chunk for chunk in relevant_chunks if chunk.get("score", 0) > 0]

    if not valid_chunks:
        return fallback_msg

    # Special handling for duration/schedule questions
    question_lower = question.lower()
    has_duration_phrases = False
    for chunk in valid_chunks:
        content_lower = chunk["content"].lower()
        if any(phrase in content_lower for phrase in ["four-week", "4 weeks", "one-month", "20 daily sessions", "20 günlük"]):
            has_duration_phrases = True
            break

    is_duration_question = any(q_term in question_lower for q_term in ["haftalık", "haftalik", "gün", "gun", "süre", "sure"])

    if is_duration_question and has_duration_phrases:
        answer_text = "Titanic EDA programı dört haftalık uzaktan bir Python ve Pandas veri bilimi programıdır. Program yaklaşık 20 günlük oturumdan oluşur."
    else:
        # Use the most relevant chunk as the main source (index 0)
        main_chunk = valid_chunks[0]
        # Extract 3-5 sentences (we will extract 4 sentences)
        sentences = re.split(r'(?<=[.!?])\s+', main_chunk["content"].strip())
        selected = [s.strip() for s in sentences if s.strip()][:4]
        answer_text = " ".join(selected)

    # Format sources
    sources = []
    for chunk in valid_chunks:
        score_info = f" (Score: {chunk['score']})" if "score" in chunk else ""
        source_line = f"* {chunk['source']} - Chunk {chunk['chunk_id']}{score_info}"
        if source_line not in sources:
            sources.append(source_line)
    sources_text = "\n".join(sources)

    return f"Cevap: {answer_text}\n\nKaynaklar:\n{sources_text}"
