from document_loader import load_documents


def main():
    print("YBS Proje Takip Asistanı başlatılıyor...\n")

    documents = load_documents("documents")

    print(f"{len(documents)} doküman başarıyla yüklendi.\n")

    for index, document in enumerate(documents, start=1):
        source = document["source"]
        content = document["content"]

        preview = content[:120].replace("\n", " ")

        print(f"{index}. {source}")
        print(f"   Önizleme: {preview}...\n")


if __name__ == "__main__":
    main()