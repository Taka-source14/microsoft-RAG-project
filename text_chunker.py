def split_text_into_chunks(text: str) -> list[str]:
    """
    Splits a text into smaller chunks.

    For the first version, we split the text by blank lines.
    This keeps paragraphs and list sections together.
    """

    raw_chunks = text.split("\n\n")

    chunks = []

    for chunk in raw_chunks:
        clean_chunk = chunk.strip()

        if clean_chunk:
            chunks.append(clean_chunk)

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