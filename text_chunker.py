import re


def split_text_into_chunks(text: str, max_chars: int = 800) -> list[str]:
    """
    Splits a text into smaller chunks.
    First splits by double newlines (\n\n).
    If a chunk exceeds max_chars, it splits it further by sentences or line breaks.
    """
    raw_chunks = text.split("\n\n")
    chunks = []

    for chunk in raw_chunks:
        clean_chunk = chunk.strip()
        if not clean_chunk:
            continue

        if len(clean_chunk) <= max_chars:
            chunks.append(clean_chunk)
        else:
            # Split further by line breaks first
            lines = clean_chunk.split("\n")
            current_sub_chunk = []
            current_len = 0

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if len(line) > max_chars:
                    # If a single line is too long, split it by sentence endings
                    sentences = re.split(r'(?<=[.!?])\s+', line)
                    for sent in sentences:
                        sent = sent.strip()
                        if not sent:
                            continue
                        if current_len + len(sent) + 1 > max_chars:
                            if current_sub_chunk:
                                chunks.append(" ".join(current_sub_chunk))
                                current_sub_chunk = []
                                current_len = 0
                            # If a single sentence is still larger, just append it directly
                            chunks.append(sent)
                        else:
                            current_sub_chunk.append(sent)
                            current_len += len(sent) + 1
                else:
                    if current_len + len(line) + 1 > max_chars:
                        if current_sub_chunk:
                            chunks.append("\n".join(current_sub_chunk))
                            current_sub_chunk = []
                            current_len = 0
                        current_sub_chunk.append(line)
                        current_len = len(line)
                    else:
                        current_sub_chunk.append(line)
                        current_len += len(line) + 1

            if current_sub_chunk:
                chunks.append("\n".join(current_sub_chunk))

    return chunks


def chunk_documents(documents: list[dict]) -> list[dict]:
    """
    Converts loaded documents into smaller text chunks.

    Each chunk contains:
    - source: original file name
    - chunk_id: order of the chunk inside the source document
    - content: chunk text
    """
    all_chunks = []

    for document in documents:
        source = document["source"]
        content = document["content"]

        chunks = split_text_into_chunks(content)

        for index, chunk in enumerate(chunks, start=1):
            all_chunks.append({
                "source": source,
                "chunk_id": index,
                "content": chunk
            })

    return all_chunks