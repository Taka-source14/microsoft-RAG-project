def generate_answer(question: str, relevant_chunks: list[dict]) -> str:
    """
    Generates a simple grounded answer using only retrieved chunk contents.
    If no relevant chunks are found, returns a standard message.
    """
    if not relevant_chunks:
        return "Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."

    # Filter out chunks with 0 or negative score (just in case)
    valid_chunks = [chunk for chunk in relevant_chunks if chunk.get("score", 0) > 0]

    if not valid_chunks:
        return "Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."

    # Format the short answer by concatenating contents of valid chunks
    # We join them with a double newline to separate paragraphs.
    answer_paragraphs = []
    sources = []

    for chunk in valid_chunks:
        content = chunk["content"].strip()
        if content not in answer_paragraphs:
            answer_paragraphs.append(content)
        
        source_info = f"- {chunk['source']} (Chunk {chunk['chunk_id']})"
        if source_info not in sources:
            sources.append(source_info)

    answer_text = "\n\n".join(answer_paragraphs)
    sources_text = "\n".join(sources)

    full_response = f"{answer_text}\n\nKaynaklar:\n{sources_text}"
    return full_response
