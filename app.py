from document_loader import load_documents
from text_chunker import chunk_documents
from retriever import retrieve_relevant_chunks


def main():
    print("YBS Proje Takip Asistanı başlatılıyor...\n")

    documents = load_documents("documents")
    print(f"{len(documents)} doküman başarıyla yüklendi.")

    chunks = chunk_documents(documents)
    print(f"{len(chunks)} chunk başarıyla oluşturuldu.\n")

    print("Soru sorabilirsiniz. Çıkmak için 'q' yazın.\n")

    while True:
        question = input("Soru: ").strip()

        if question.lower() in ["q", "quit", "exit", "çıkış"]:
            print("Uygulama kapatılıyor...")
            break

        if not question:
            print("Lütfen bir soru girin.\n")
            continue

        relevant_chunks = retrieve_relevant_chunks(question, chunks, top_k=3)

        if not relevant_chunks:
            print("\nBu soruyla ilgili dokümanlarda yeterli bilgi bulunamadı.\n")
            continue

        print("\nEn alakalı doküman parçaları:\n")

        for index, chunk in enumerate(relevant_chunks, start=1):
            print(f"{index}. Kaynak: {chunk['source']} - Chunk {chunk['chunk_id']}")
            print(f"   Skor: {chunk['score']}")
            print(f"   İçerik: {chunk['content']}\n")


if __name__ == "__main__":
    main()