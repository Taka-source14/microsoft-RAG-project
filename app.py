from document_loader import load_documents
from text_chunker import chunk_documents
from embedding_generator import build_embeddings
import embedding_generator
from vector_store import rebuild_vector_store, load_chunks
from semantic_retriever import retrieve_relevant_chunks_semantic
from response_generator import generate_answer_with_llm


def main():
    print("==================================================")
    print("   YBS Proje Takip Asistanı (Local RAG Pipeline)  ")
    print("==================================================")
    print("Supported file types: .txt, .docx, .pdf")
    print("Uygulama başlatılıyor...\n")

    try:
        documents = load_documents("documents")
        print(f"Documents loaded: {len(documents)}")
    except Exception as e:
        print(f"Hata: Dokümanlar yüklenemedi: {e}")
        return

    # Chunking
    chunks = chunk_documents(documents)
    print(f"Chunks created: {len(chunks)}")

    # Embeddings
    embedded_chunks, embedding_model = build_embeddings(chunks)
    embedding_mode = "Foundry Local" if embedding_generator.USE_FOUNDRY else "TF-IDF fallback"
    print(f"Embedding mode: {embedding_mode}")

    # Vector store save
    db_name = "rag.db"
    rebuild_vector_store(embedded_chunks, embedding_model, db_path=db_name)
    print(f"Vector store: {db_name}")
    print("RAG pipeline ready.\n")

    # Load back from database to verify SQLite persistence
    stored_chunks = load_chunks(db_path=db_name)

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

        # Retrieve semantically (which falls back internally to keyword search on failure)
        relevant_chunks = retrieve_relevant_chunks_semantic(question, stored_chunks, embedding_model, top_k=3)

        # Generate answer (with LLM or fallback extractive method)
        answer = generate_answer_with_llm(question, relevant_chunks)

        print(f"\n{answer}")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()