def build_rag_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    """
    Builds a structured prompt for the LLM using the retrieved document context.
    """
    context_parts = []
    for chunk in retrieved_chunks:
        header = f"[Kaynak: {chunk['source']} - Chunk {chunk['chunk_id']}]"
        content = chunk["content"]
        context_parts.append(f"{header}\n{content}")

    context_text = "\n\n".join(context_parts)

    prompt = f"""Sen yerel dokümanlara göre cevap veren bir RAG asistanısın.

Kurallar:
- Sadece aşağıdaki bağlamı kullan.
- Bağlamda cevap yoksa bilgi uydurma.
- Cevap yoksa şunu yaz: Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.
- Kısa ve anlaşılır cevap ver.
- Cevabı Türkçe ver.

Bağlam:
{context_text}

Kullanıcı sorusu:
{question}
"""
    return prompt
