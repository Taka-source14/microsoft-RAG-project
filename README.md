# YBS Proje Takip Asistanı (Local RAG Project Management Assistant)

YBS Proje Takip Asistanı, Yönetim Bilişim Sistemleri (YBS) proje yönetimi dokümanlarını okuyup, kullanıcının proje süreciyle ilgili sorularına kaynak göstererek güvenilir cevaplar veren yerel bir **RAG (Retrieval-Augmented Generation)** uygulamasıdır.

Bu proje, harici bulut servislerine veya ücretli API'lere bağımlı olmadan tamamen çevrimdışı (offline) ve yerel çalışacak şekilde tasarlanmış bir MVP (Minimum Viable Product) sürümüdür.

---

## Projenin Temel Amacı ve Geliştirilme Nedeni

Proje yönetimi süreçlerinde hedefler, haftalık planlar, riskler ve görevler genellikle farklı dokümanlarda veya notlarda dağınık şekilde tutulur. Kullanıcılar aradıkları bilgiyi bulmak için bu dosyalar arasında manuel arama yapmak zorunda kalır. 

Bu asistan:
* Proje dokümanlarını merkezi hale getirir.
* Doğal dildeki soruları analiz ederek ilgili paragrafları hızlıca bulur.
* Tamamen yerel dokümanlardaki bilgilere sadık kalarak (halüsinasyon üretmeden) yanıt verir.
* Yanıtların hangi doküman ve hangi bölümden (Chunk ID) alındığını şeffaf bir şekilde listeler.

---

## RAG (Retrieval-Augmented Generation) Nedir?

RAG, yapay zeka modelinin bir soruya cevap vermeden önce harici bir bilgi tabanından (bu projede yerel `.txt`, `.docx` ve `.pdf` dosyaları) ilgili bilgileri sorgulayıp getirmesi ve bu bilgileri kullanarak cevap üretmesi yöntemidir.

Süreç temel olarak 3 adımdan oluşur:
1. **Retrieval (Bilgi Getirme):** Kullanıcının sorusuyla en alakalı doküman parçaları (chunklar) bulunur.
2. **Augmentation (Zenginleştirme):** Bulunan bilgiler prompt içerisine bağlam (context) olarak yerleştirilir.
3. **Generation (Cevap Üretme):** Model/sistem sadece bu bağlama dayanarak cevabı oluşturur.

---

## Proje Yapısı

```text
Local RAG Project Management Assistant/
│
├── app.py                  # CLI uygulamasının giriş noktası ve Q&A döngüsü
├── document_loader.py      # Doküman yükleme ve hata kontrolü modülü
├── text_chunker.py         # Metinleri paragraflara (chunk) bölme modülü
├── retriever.py            # Türkçe NLP tabanlı anahtar kelime arama modülü
├── response_generator.py   # Grounded (bağlama dayalı) cevap oluşturma modülü
│
├── documents/              # Bilgi tabanını oluşturan yerel dosyalar
│   ├── proje_amaci.txt
│   ├── haftalik_plan.txt
│   ├── gorev_listesi.txt
│   ├── teslim_kriterleri.txt
│   ├── riskler.txt
│   ├── sunum_notlari.txt
│   └── rag_aciklamasi.txt
│
├── docs/                   # Proje mimari ve tasarım dokümantasyonu
│   ├── architecture.md
│   └── project_roadmap.md
│
├── tests/                  # Test planı ve örnek sorular
│   └── test_questions.md
│
├── requirements.txt        # Proje bağımlılıkları (python-docx, pypdf)
└── .gitignore              # Git tarafından takip edilmeyecek dosyalar
```

---

## Nasıl Çalışır?

1. **Doküman Yükleme:** `documents/` klasöründeki tüm `.txt` (UTF-8), `.docx` (Word) ve `.pdf` (metin tabanlı PDF) dosyaları yüklenir. Okunamayan boş veya taranmış resim-tabanlı dosyalar atlanır.
2. **Parçalara Bölme (Chunking):** Dokümanlar, anlam bütünlüğünü korumak adına çift satır boşluklarından (`\n\n`) bölünerek paragraflara ayrılır. Her parçaya özgün bir `chunk_id` verilir.
3. **Türkçe Tokenizasyon:** Kullanıcı sorusu ve doküman parçaları Türkçe karakter duyarlılığıyla (büyük/küçük harf dönüşümleri: `İ` -> `i`, `I` -> `ı` vb.) temizlenir ve kelimelerine ayrılır.
4. **Stopwords (Dolgu Kelimeleri) Filtreleme:** Türkçe dilindeki etkisiz kelimeler (`ve`, `veya`, `ile`, `için`, `bu`, `şu`, `bir`, `de`, `da`, `ne`, `nedir`, `nasıl`, `hangi`, `nelerdir`, `mı`, `mi`, `mu`, `mü`) elenerek sadece anlamlı kelimeler tutulur.
5. **Skorlama ve Arama:** Soru kelimeleri ile doküman parçaları arasındaki kelime çakışması (keyword overlap) hesaplanır. En yüksek skora sahip ilk 3 parça seçilir.
6. **Kaynaklı Cevap Üretimi:** Seçilen parçaların içerikleri birleştirilerek cevap oluşturulur ve en sona ilgili kaynak dosyalar ile Chunk ID bilgileri eklenir. Eğer hiçbir kelime çakışması yoksa, sistem güvenli bir şekilde bilgi bulunamadığını belirtir.

---

## Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/Taka-source14/microsoft-RAG-project.git
cd "Local RAG Project Management Assistant"
```

### 2. Sanal Ortam Oluşturun ve Aktive Edin
**Windows için:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux için:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
*(Yeni eklenen DOCX ve PDF desteği için python-docx ve pypdf kütüphaneleri venv içerisine kurulur)*
```bash
pip install -r requirements.txt
```

### 4. CLI Uygulamasını Çalıştırın
```bash
python app.py
```

---

## Örnek Sorular

Uygulama çalıştıktan sonra aşağıdaki örnek soruları yöneltebilirsiniz:
* **Soru:** `Bu projenin amacı nedir?`
* **Soru:** `RAG nedir?`
* **Soru:** `Teslim kriterleri nelerdir?`
* **Soru:** `Projede hangi riskler var?`
* **Soru:** `3. haftada ne yapılacak?`
* **Soru:** `Sunumda ne anlatmalıyım?`

### Alakasız Sorular (Bilgi Bulunamayan Durumlar)
Eğer dokümanlarda bulunmayan alakasız bir soru sorulursa sistem halüsinasyon üretmez:
* **Soru:** `Bugün hava nasıl?`
* **Cevap:** `Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.`

---

## Mevcut Durum (MVP Sürümü)

* [x] Yerel dokümanlar (.txt, .docx, .pdf) başarıyla yükleniyor.
* [x] Okunamayan taranmış (resim tabanlı) PDF'ler güvenle atlanarak sistemin çökmesi önleniyor.
* [x] Dokümanlar paragraf tabanlı mantıklı parçalara (chunk) bölünüyor.
* [x] Türkçe karakter uyumlu tokenizasyon ve stopwords temizleme yapılıyor.
* [x] Anahtar kelime eşleşmesi baz alınarak en alakalı bölümler puanlanıp getiriliyor.
* [x] Cevaplar sadece yerel doküman içeriğine dayandırılıyor (Sıfır Halüsinasyon).
* [x] Kullanılan kaynak dosyaları ve Chunk ID'leri şeffaf bir şekilde listeleniyor.
* [x] Alakasız sorular güvenli hata mesajıyla karşılanıyor.

---

## Gelecek Geliştirmeler

* **Foundry Local ve LLM Entegrasyonu:** Cevapların sadece ham paragraf birleştirmesi yerine yerel çalışan hafif bir LLM (Foundry Local veya yerel Llama/Mistral) ile daha akıcı ve özetlenmiş hale getirilmesi.
* **Embedding Tabanlı Semantik Arama:** Anahtar kelime eşleşmesi yerine vektör benzerliği (Cosine Similarity) kullanılarak eşanlamlı kelimeler içeren soruların da bulunabilmesi.
* **SQLite Vektör Depolama:** Chunk ve vektör verilerinin RAM yerine yerel SQLite veritabanında saklanarak hızlandırılması.
* **Streamlit Web Arayüzü:** CLI yerine kullanıcı dostu modern bir Streamlit arayüzünün sunulması.
* **PDF ve DOCX Desteği:** Sadece `.txt` değil, `.pdf` ve `.docx` formatındaki dokümanların da okunabilmesi (Tamamlandı).
* **OCR Entegrasyonu:** Taranmış (scanned) veya resim tabanlı PDF'lerden metin okuyabilmek için Tesseract OCR entegrasyonunun yapılması.

---

## Demo Videosu Açıklaması

MVP sürümünün terminal arayüzündeki çalışma performansını gösteren demo ekran kaydı ileride hazırlanarak proje klasörüne eklenecektir. Uygulamanın terminal çıktılarındaki soru-cevap doğruluğu test aşamasında tam puanla doğrulanmıştır.
