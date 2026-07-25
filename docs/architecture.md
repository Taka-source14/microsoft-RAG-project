# YBS Proje Takip Asistanı — Proje Haritası ve UML Diagramları

## 1. Proje Haritası

**Proje Adı:** YBS Proje Takip Asistanı
**İngilizce Adı:** Local RAG Project Management Assistant
**Ana Teknoloji:** Microsoft Foundry Local + RAG
**Amaç:** YBS proje dokümanlarından bilgi çekerek proje süreciyle ilgili sorulara cevap veren yerel bir yapay zekâ asistanı geliştirmek.

---

## 2. Projenin Temel Amacı

Bu proje, proje yönetimi sürecinde kullanılan dokümanları daha erişilebilir hale getirmeyi amaçlar.

Kullanıcı; proje amacı, haftalık plan, görev listesi, teslim kriterleri, riskler ve sunum notları gibi dokümanlar hakkında doğal dilde soru sorabilir. Sistem, önce ilgili doküman parçalarını bulur, ardından bu bilgileri kullanarak cevap üretir.

Örnek sorular:

```text
Bu projenin amacı nedir?
Bu hafta hangi görevleri yapmalıyım?
Teslim kriterleri nelerdir?
Projedeki riskler nelerdir?
Sunumda projeyi nasıl anlatmalıyım?
RAG bu projede nasıl kullanılıyor?
```

---

## 3. Proje Bileşenleri

| Bileşen           | Açıklama                                                   |
| ----------------- | ---------------------------------------------------------- |
| Kullanıcı Arayüzü | Kullanıcının soru sorduğu CLI veya Streamlit ekranı        |
| Doküman Yükleyici | `documents/` klasöründeki proje dokümanlarını okur         |
| Chunking Modülü   | Uzun metinleri küçük parçalara böler                       |
| Embedding Modülü  | Metin parçalarını sayısal vektörlere dönüştürür            |
| Retrieval Modülü  | Kullanıcı sorusuna en yakın doküman parçalarını bulur      |
| Prompt Builder    | Bulunan bilgileri modele verilecek context haline getirir  |
| Foundry Local LLM | Yerel çalışan model ile cevap üretir                       |
| Kaynak Gösterme   | Cevabın hangi dokümandan üretildiğini gösterir             |
| Test Modülü       | Cevaplanabilir ve cevaplanamaz sorularla sistemi test eder |

---

## 4. Genel Sistem Haritası

```mermaid
flowchart TD
    A[Kullanıcı] --> B[Arayüz: CLI veya Streamlit]
    B --> C[Kullanıcı Sorusu]
    C --> D[Soru Embedding İşlemi]
    D --> E[Retrieval Modülü]
    E --> F[Doküman Chunkları]
    F --> G[En Alakalı Chunkları Seç]
    G --> H[Prompt Builder]
    H --> I[Foundry Local LLM]
    I --> J[Cevap Üretimi]
    J --> K[Kaynak Bilgisi Ekle]
    K --> L[Kullanıcıya Cevap Göster]
```

---

## 5. RAG Akış Haritası

```mermaid
flowchart LR
    A[Local Project Documents] --> B[Document Loader]
    B --> C[Text Chunking]
    C --> D[Embedding Generation]
    D --> E[Vector Store / SQLite]
    F[User Question] --> G[Question Embedding]
    G --> H[Similarity Search]
    E --> H
    H --> I[Top Relevant Chunks]
    I --> J[Augmented Prompt]
    J --> K[Foundry Local LLM]
    K --> L[Grounded Answer]
```

---

## 6. UML Use Case Diagram

```mermaid
flowchart LR
    User((Kullanıcı))

    UC1[Proje hakkında soru sor]
    UC2[Haftalık görevleri öğren]
    UC3[Teslim kriterlerini sorgula]
    UC4[Proje risklerini görüntüle]
    UC5[Sunum notlarını öğren]
    UC6[Kaynaklı cevap al]
    UC7[Dokümanda olmayan soruya güvenli cevap al]

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
```

---

## 7. UML Activity Diagram

```mermaid
flowchart TD
    A([Başla]) --> B[Kullanıcı soru girer]
    B --> C{Soru boş mu?}

    C -- Evet --> D[Uyarı ver: Lütfen soru girin]
    D --> B

    C -- Hayır --> E[Soruyu embedding'e çevir]
    E --> F[Doküman chunkları ile benzerlik hesapla]
    F --> G[En alakalı chunkları seç]
    G --> H{Yeterli context bulundu mu?}

    H -- Hayır --> I[Dokümanlarda yeterli bilgi bulunamadı cevabı ver]
    I --> Z([Bitir])

    H -- Evet --> J[Context ile prompt oluştur]
    J --> K[Foundry Local modeline gönder]
    K --> L[Cevabı üret]
    L --> M[Kaynak dosyaları ekle]
    M --> N[Kullanıcıya cevabı göster]
    N --> Z([Bitir])
```

---

## 8. UML Sequence Diagram

```mermaid
sequenceDiagram
    actor User as Kullanıcı
    participant UI as Arayüz
    participant RAG as RAG Pipeline
    participant Embed as Embedding Servisi
    participant Store as Vector Store / SQLite
    participant Prompt as Prompt Builder
    participant LLM as Foundry Local LLM

    User->>UI: Soru girer
    UI->>RAG: ask_question(question)
    RAG->>Embed: Soru embedding'i oluştur
    Embed-->>RAG: Question vector
    RAG->>Store: En benzer doküman chunklarını ara
    Store-->>RAG: Top-K ilgili chunklar
    RAG->>Prompt: Context + soru ile prompt oluştur
    Prompt-->>RAG: Augmented prompt
    RAG->>LLM: Prompt gönder
    LLM-->>RAG: Cevap üret
    RAG-->>UI: Cevap + kaynak bilgisi
    UI-->>User: Sonucu göster
```

---

## 9. UML Class Diagram

```mermaid
classDiagram
    class App {
        +run()
        +display_answer()
    }

    class DocumentLoader {
        +load_documents(folder_path)
        +read_text_file(file_path)
    }

    class TextChunker {
        +split_text(text)
        +create_chunks(documents)
    }

    class EmbeddingService {
        +generate_embedding(text)
        +generate_batch_embeddings(chunks)
    }

    class VectorStore {
        +save_chunk(chunk, embedding, source)
        +get_all_chunks()
        +search_similar(query_embedding, top_k)
    }

    class RAGPipeline {
        +ask_question(question)
        +retrieve_context(question)
        +generate_answer(question, context)
    }

    class PromptBuilder {
        +build_prompt(question, context)
    }

    class FoundryLocalClient {
        +load_model()
        +generate_response(prompt)
    }

    class Source {
        +file_name
        +chunk_id
        +content
    }

    App --> RAGPipeline
    RAGPipeline --> EmbeddingService
    RAGPipeline --> VectorStore
    RAGPipeline --> PromptBuilder
    RAGPipeline --> FoundryLocalClient
    DocumentLoader --> TextChunker
    TextChunker --> EmbeddingService
    VectorStore --> Source
```

---

## 10. UML Component Diagram

```mermaid
flowchart TD
    subgraph UI[User Interface Layer]
        A[CLI / Streamlit App]
    end

    subgraph AppLayer[Application Layer]
        B[RAG Pipeline]
        C[Prompt Builder]
        D[Source Formatter]
    end

    subgraph DataLayer[Data Layer]
        E[Documents Folder]
        F[SQLite / Vector Store]
    end

    subgraph AILayer[AI Layer]
        G[Embedding Model]
        H[Foundry Local LLM]
    end

    A --> B
    B --> C
    B --> D
    B --> G
    B --> F
    E --> B
    C --> H
    H --> D
    D --> A
```

---

## 11. Veri Modeli

İlk MVP sürümünde veriler RAM üzerinde tutulabilir. Daha gelişmiş sürümde SQLite kullanılabilir.

### Önerilen SQLite Tablosu

```mermaid
erDiagram
    DOCUMENT_CHUNKS {
        int id
        string source_file
        int chunk_index
        text content
        text embedding_json
        datetime created_at
    }

    QUESTIONS {
        int id
        text question
        text answer
        text used_sources
        datetime asked_at
    }

    DOCUMENT_CHUNKS ||--o{ QUESTIONS : "used_as_context"
```

---

## 12. Modül Sorumlulukları

| Modül           | Dosya                     | Görev                                        |
| --------------- | ------------------------- | -------------------------------------------- |
| App             | `app.py`                  | Uygulamayı başlatır, kullanıcıdan soru alır  |
| Document Loader | `document_loader.py`      | Dokümanları okur                             |
| Chunker         | `text_chunker.py`         | Metinleri parçalara böler                    |
| Embedding       | `embedding_service.py`    | Metinleri embedding'e dönüştürür             |
| Vector Store    | `vector_store.py`         | Chunk ve embedding verilerini saklar         |
| RAG Pipeline    | `rag_pipeline.py`         | Retrieval ve generation sürecini yönetir     |
| Prompt Builder  | `prompt_builder.py`       | Model için context destekli prompt üretir    |
| Test            | `tests/test_questions.md` | Test sorularını ve beklenen cevapları içerir |

---

## 13. Proje Akışının Basit Özeti

```text
1. Proje dokümanları documents klasörüne eklenir.
2. Sistem dokümanları okur.
3. Dokümanları küçük parçalara böler.
4. Her parçanın embedding vektörü oluşturulur.
5. Kullanıcı soru sorar.
6. Soru embedding'e çevrilir.
7. En alakalı doküman parçaları bulunur.
8. Bulunan parçalar prompt içine eklenir.
9. Foundry Local modeli cevap üretir.
10. Cevap, kaynak doküman bilgisiyle kullanıcıya gösterilir.
```

---

## 14. Current Implemented Architecture

```text
Documents → Loader → Chunker → TF-IDF Embeddings → SQLite rag.db → Semantic Retriever → Prompt Builder → Local Extractive/Fallback Answer → Sources
```

Şu anda YBS Proje Takip Asistanı'nda tam olarak çalışan RAG mimarisi şu şekildedir:
- **Doküman Yükleme:** `documents/` altındaki `.txt`, `.docx`, ve metin tabanlı `.pdf` dosyalarını temiz bir şekilde yükler.
- **Parçalama (Chunking):** Paragraf sınırlarını koruyarak maksimum 800 karakter boyutunda parçalar oluşturur.
- **Embedding:** Yerel TF-IDF vektörleştirici (fallback) kullanarak metin parçalarını ve sorguları sayısal vektörlere çevirir (Microsoft Foundry Local entegrasyonu için yapı hazırlanmıştır).
- **Vektör Deposu (SQLite):** `rag.db` adında yerel bir veritabanı kurarak chunk metinlerini, kaynak yollarını ve embedding JSON dizelerini saklar.
- **Semantik Arama:** Cosine Similarity hesaplayarak en benzer 3 chunk'ı çeker. Arama hatasında anahtar kelime tabanlı fall-back mekanizmasını çalıştırır.
- **Prompt Builder:** İlgili context parçalarını ve kuralları birleştirerek Türkçe prompt hazırlar.
- **Cevap Üretimi:** Microsoft Foundry Local LLM API'sine bağlanmayı dener; bulunamazsa, yerel context içinden en alakalı cümleleri seçen akıllı fallback modunu çalıştırır.

---

## 15. Target Foundry Local Architecture

```text
Documents → Loader → Chunker → Foundry Local Embeddings → SQLite/Vector Store → Semantic Retriever → Prompt Builder → Foundry Local Chat Model → Grounded Answer with Sources
```

Gelecek aşamalarda hedeflenen tam Microsoft Foundry Local entegrasyonu:
- **Embedding:** Microsoft Foundry Local SDK üzerinden yerel çalışan yüksek başarımlı bir dense embedding modeli (örneğin BERT veya MiniLM tabanlı) ile metinleri vektörleştirme.
- **Vektör Deposu:** SQLite üzerinde JSON aramak yerine, pgvector benzeri bir yerel vektör eklentisi veya doğrudan SQLite-vss entegrasyonu ile hızlı ANN aramaları yapma.
- **Local LLM:** Yerel donanım üzerinde (CPU/GPU) barındırılan Llama-3 veya Mistral benzeri 7B parametreli bir Foundry Local LLM modeli (Chat Model) ile prompt'ları işleyip yüksek kaliteli, özetlenmiş, doğal dilde cevaplar üretme.
