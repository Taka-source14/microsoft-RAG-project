# YBS Proje Takip Asistanı (Local RAG Project Management Assistant)

YBS Proje Takip Asistanı, Yönetim Bilişim Sistemleri (YBS) proje yönetimi dokümanlarını okuyup, kullanıcının proje süreciyle ilgili sorularına kaynak göstererek güvenilir ve kısa cevaplar veren yerel bir **RAG (Retrieval-Augmented Generation)** uygulamasıdır.

Bu proje, harici bulut servislerine, ücretli API'lere veya internet bağlantısına bağımlı olmadan tamamen çevrimdışı (offline) ve yerel çalışacak şekilde tasarlanmış bir terminal (CLI) uygulamasıdır.

---

## Current RAG Pipeline

Sistem aşağıdaki tam RAG boru hattı (pipeline) akışını takip eder:

```text
Documents → Loader → Chunker → Embeddings → SQLite Vector Store → Semantic Retriever → Prompt Builder → Local LLM/Fallback Generator → Source-based Answer
```

1. **Documents & Loader (`document_loader.py`):** `documents/` klasöründeki `.txt`, `.docx` ve `.pdf` dosyalarını yükler. Boş veya taranmış (resim tabanlı) dosyaları güvenle atlar.
2. **Chunker (`text_chunker.py`):** Dokümanları paragraf sınırlarına ve maksimum 800 karakter limitine göre anlamlı parçalara (chunk) böler.
3. **Embeddings (`embedding_generator.py`):** Microsoft Foundry Local SDK yüklüyse Foundry Local embedding modelini kullanır. Aksi halde yerel `scikit-learn` TF-IDF vektörleştirici ile çevrimdışı fallback embedding'ler üretir.
4. **SQLite Vector Store (`vector_store.py`):** Chunk metinlerini, kaynak yollarını ve embedding dizilerini `rag.db` adlı yerel SQLite veritabanına kaydeder.
5. **Semantic Retriever (`semantic_retriever.py`):** Kullanıcı sorusunu vektöre çevirir ve SQLite'taki chunk vektörleri ile **Cosine Similarity** (Kosinüs Benzerliği) hesaplayarak en yakın 3 chunk'ı çeker. Başarısızlık durumunda otomatik olarak anahtar kelime tabanlı aramaya geçer.
6. **Prompt Builder (`prompt_builder.py`):** Bulunan ilgili metin parçalarını, asistan kuralları ve kullanıcı sorusu ile birleştirerek grounded (dokümana dayalı) bir Türkçe prompt hazırlar.
7. **Local LLM/Fallback Generator (`response_generator.py`):** Microsoft Foundry Local LLM yüklüyse prompt'u yerel LLM'e göndererek cevap üretir. Aksi halde yerel context'ten en alakalı cümleleri seçen akıllı fallback modunu çalıştırır.

---

## Proje Yapısı

```text
Local RAG Project Management Assistant/
│
├── app.py                  # CLI uygulamasının giriş noktası ve RAG akışı
├── document_loader.py      # TXT, DOCX ve PDF yükleme modülü
├── text_chunker.py         # Metinleri karakter limitli (800) chunklara bölme modülü
├── embedding_generator.py  # Foundry Local / TF-IDF embedding modülü (Yeni)
├── vector_store.py         # SQLite veritabanı (rag.db) yönetim modülü (Yeni)
├── semantic_retriever.py   # Cosine similarity tabanlı semantik arama modülü (Yeni)
├── prompt_builder.py       # LLM için RAG prompt oluşturma modülü (Yeni)
├── retriever.py            # Anahtar kelime tabanlı yedek arama modülü
├── response_generator.py   # LLM ve fallback tabanlı cevap oluşturma modülü
│
├── documents/              # Bilgi tabanını oluşturan yerel dosyalar (.txt, .docx, .pdf)
├── docs/                   # Proje mimari ve tasarım dokümantasyonu (architecture.md)
├── tests/                  # Test planı ve örnek sorular (test_questions.md)
├── requirements.txt        # Proje bağımlılıkları
└── .gitignore              # rag.db ve sanal ortam dosyalarını hariç tutar
```

---

## Kurulum ve Çalıştırma

### 1. Sanal Ortamı Aktif Edin (Mevcutsa) veya Oluşturun
```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 3. CLI Uygulamasını Çalıştırın
```bash
python app.py
```

---

## Örnek Sorular

Uygulama çalıştıktan sonra sorabileceğiniz örnek sorular:
* `RAG nedir?`
* `Bu projenin amacı nedir?`
* `Titanic EDA programı kaç haftalık?`
* `Day 5'te ne anlatılıyor?`
* `Bugün hava nasıl?` (Alakasız soru fallback testi)
* `Bitcoin fiyatı kaç?` (Alakasız soru fallback testi)

---

## Limitations (Sınırlamalar)

* **Foundry Local Entegrasyonu:** Tam entegrasyon yerel sistemde Microsoft Foundry Local ortamının/paketlerinin kurulu olmasına bağlıdır. Bulunmadığında sistem otomatik ve güvenli şekilde yerel TF-IDF ve extractive fallback moduna geçer.
* **Fallback Modu Sınırları:** LLM bulunmadığında çalışan fallback modu, serbest üretim yapmak yerine doğrudan doküman cümlelerini seçerek cevap verir; bu nedenle tam bir LLM kadar akıcı özetleme yapamaz.
* **Taranmış PDF'ler:** OCR (Optik Karakter Tanıma) entegre edilmediği için sadece metin tabanlı PDF'ler desteklenir.
* **Optimizasyon:** Çok büyük doküman setleri için (1000+ sayfa) TF-IDF ve SQLite bellek içi aramalar yerine daha gelişmiş vektör veritabanları (FAISS, Chroma vb.) gerekebilir.
