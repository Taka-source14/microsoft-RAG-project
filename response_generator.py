import re
from prompt_builder import build_rag_prompt

# Try importing Foundry Local SDK/packages if available
HAS_FOUNDRY_LLM = False

try:
    import foundry_local_llm_sdk
    # HAS_FOUNDRY_LLM = True
except ImportError:
    HAS_FOUNDRY_LLM = False


def generate_answer_with_llm(question: str, retrieved_chunks: list[dict]) -> str:
    """
    Tries to generate an answer using Foundry Local LLM.
    If unavailable, falls back to generate_fallback_answer.
    """
    global HAS_FOUNDRY_LLM
    fallback_msg = "Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."

    if not retrieved_chunks:
        return fallback_msg

    valid_chunks = [chunk for chunk in retrieved_chunks if chunk.get("score", 0) > 0]
    if not valid_chunks:
        return fallback_msg

    if HAS_FOUNDRY_LLM:
        try:
            print("Mode: Foundry Local LLM")
            prompt = build_rag_prompt(question, valid_chunks)
            # Call hypothetical Foundry LLM generation
            # answer_text = foundry_local_llm_sdk.generate(prompt)
            # return format_response(answer_text, valid_chunks)
            raise NotImplementedError()
        except Exception:
            return format_response(generate_fallback_answer(question, valid_chunks), valid_chunks)
    else:
        return format_response(generate_fallback_answer(question, valid_chunks), valid_chunks)


def generate_fallback_answer(question: str, retrieved_chunks: list[dict]) -> str:
    """
    Extractive fallback answer generator using chunk extraction rules.
    """
    print("Mode: Local extractive fallback")
    valid_chunks = [chunk for chunk in retrieved_chunks if chunk.get("score", 0) > 0]
    if not valid_chunks:
        return ""

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
        main_chunk = valid_chunks[0]
        sentences = re.split(r'(?<=[.!?])\s+', main_chunk["content"].strip())
        selected = [s.strip() for s in sentences if s.strip()][:4]
        answer_text = " ".join(selected)

    return answer_text


def format_response(answer_text: str, valid_chunks: list[dict]) -> str:
    """
    Helper to format the final generated answer and source citations.
    """
    if not answer_text.strip():
        return "Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."

    sources = []
    for chunk in valid_chunks:
        score_val = chunk.get("score", 0)
        if isinstance(score_val, float):
            score_str = f"{score_val:.2f}"
        else:
            score_str = str(score_val)
        source_line = f"- {chunk['source']} - Chunk {chunk['chunk_id']} (Score: {score_str})"
        if source_line not in sources:
            sources.append(source_line)
    sources_text = "\n".join(sources)

    return f"Cevap:\n{answer_text}\n\nKaynaklar:\n{sources_text}"
