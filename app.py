from document_loader import load_documents
from text_chunker import chunk_documents


def main():
    print("YBS Proje Takip Asistanı başlatılıyor...\n")

    documents = load_documents("documents")

    print(f"{len(documents)} doküman başarıyla yüklendi.\n")

    chunks = chunk_documents(documents)

    print(f"{len(chunks)} chunk başarıyla oluşturuldu.\n")

    for index, chunk in enumerate(chunks, start=1):
        source = chunk["source"]
        chunk_id = chunk["chunk_id"]
        content = chunk["content"]

        preview = content[:120].replace("\n", " ")

        print(f"{index}. {source} - Chunk {chunk_id}")
        print(f"   Önizleme: {preview}...\n")


if __name__ == "__main__":
    main()