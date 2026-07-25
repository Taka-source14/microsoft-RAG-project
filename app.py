from document_loader import load_documents
from text_chunker import chunk_documents
from retriever import retrieve_relevant_chunks
from response_generator import generate_answer


def main():
    print("==================================================")
    print("   YBS Proje Takip Asistanı (Local RAG MVP)       ")
    print("==================================================")
    print("Supported file types: .txt, .docx, .pdf")
    print("Uygulama başlatılıyor...\n")

    try:
        documents = load_documents("documents")
        print(f"-> {len(documents)} doküman başarıyla yüklendi.")
    except Exception as e:
        print(f"Hata: Dokümanlar yüklenemedi: {e}")
        return

    chunks = chunk_documents(documents)
    print(f"-> {len(chunks)} chunk başarıyla oluşturuldu.\n")

    print("Soru sorabilirsiniz. Çıkmak için 'q', 'quit', 'exit' veya 'çıkış' yazın.\n")

    while True:
        try:
            question = input("Soru: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nUygulama kapatılıyor...")
            break

        if question.lower() in ["q", "quit", "exit", "çıkış"]:
            print("Uygulama kapatılıyor...")
            break

        if not question:
            print("Lütfen bir soru girin.\n")
            continue

        # Retrieve top 3 relevant chunks
        relevant_chunks = retrieve_relevant_chunks(question, chunks, top_k=3)

        # Generate grounded answer
        answer = generate_answer(question, relevant_chunks)

        print(f"\n{answer}")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()