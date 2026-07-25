# YBS Proje Takip Asistanı (Local RAG Project Management Assistant)

YBS Proje Takip Asistanı, Yönetim Bilişim Sistemleri (YBS) proje yönetimi dokümanlarını okuyup, kullanıcının proje süreciyle ilgili sorularına kaynak göstererek güvenilir ve kısa cevaplar veren yerel bir **RAG (Retrieval-Augmented Generation) MVP** uygulamasıdır.

Bu proje, harici bulut servislerine, ücretli API'lere veya harici LLM kurulumlarına bağımlı olmadan tamamen çevrimdışı (offline) ve yerel çalışacak şekilde tasarlanmış bir terminal (CLI) uygulamasıdır.

---

## Projenin Temel Özellikleri ve Yetenekleri

* **Çoklu Belge Desteği:** Belge klasöründeki `.txt` (UTF-8), Word `.docx` ve metin tabanlı `.pdf` dokümanlarını otomatik okuyup bilgi tabanına dahil eder.
* **Akıllı Paragraf Bölme (Chunking):** Dokümanları çift satır boşluklarına (`\n\n`) göre paragraflara böler. Karakter limiti (maksimum 800 karakter) aşan uzun paragrafları cümle sonlarından bölerek cevapların çok uzun ve karmaşık olmasını engeller.
* **Türkçe ve İngilizce Karışık Arama Desteği (Keyword Expansion):** Türkçe karakter duyarlı aramayı (büyük/küçük harf dönüşümleri: `İ` -> `i`, `I` -> `ı` vb.) ve dolgu sözcük (stopword) filtrelemesini yapar. Ayrıca Türkçe-İngilizce eşleştirme haritası ile "haftalık" kelimesini "weeks", "gün" kelimesini "day", "aşama" kelimesini "phase" ile ilişkilendirerek mixed (karışık dilli) dokümanlarda doğru eşleşme puanları hesaplar.
* **Kısa ve Grounded (Kaynak Kanıtlı) Cevap Üretimi:** En alakalı doküman parçasının ilk 3-5 cümlesini çekerek kısa ve net yanıtlar üretir. Her cevabın altına hangi dosyadan ve hangi chunk numarasından (puanıyla birlikte) alındığını listeler.
* **Sıfır Halüsinasyon:** Dokümanlarda bulunmayan alakasız sorulara cevap uydurmak yerine doğrudan *"Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."* yanıtını verir.

---

## Nasıl Çalışır?

1. **Doküman Yükleme:** `documents/` klasöründeki `.txt`, `.docx` ve `.pdf` uzantılı dosyalar taranır. Metin içermeyen boş veya taranmış (resim tabanlı) dosyalar terminalde uyarı verilerek güvenle atlanır.
2. **Chunking (Karakter Sınırlı):** Yüklenen belgeler paragraf sınırlarına göre bölünür. 800 karakter sınırını aşan büyük bloklar cümle bazlı alt chunklara ayrılır.
3. **Puanlama (Retrieval):** Kullanıcının sorusu temizlenip anahtar kelimelere ayrılır. Soru kelimeleri ve bunların Türkçe-İngilizce karşılıkları, doküman chunklarındaki kelimelerle eşleştirilerek overlap skoru hesaplanır. En yüksek puanlı 3 chunk seçilir.
4. **Cevap Formatlama:** En yüksek skora sahip en alakalı chunk seçilerek ilk 4 anlamlı cümlesi alınır ve kaynak detaylarıyla (ve hesaplanan eşleşme skoruyla) terminale basılır.

---

## Proje Yapısı

```text
Local RAG Project Management Assistant/
│
├── app.py                  # CLI uygulamasının giriş noktası ve kullanıcı döngüsü
├── document_loader.py      # TXT, DOCX ve PDF yükleme modülü
├── text_chunker.py         # Metinleri karakter limitli (800) chunklara bölme modülü
├── retriever.py            # Türkçe/İngilizce anahtar kelime arama ve puanlama modülü
├── response_generator.py   # Grounded ve kısa cevap oluşturma modülü
│
├── documents/              # Bilgi tabanını oluşturan yerel dosyalar (.txt, .docx, .pdf)
├── docs/                   # Proje mimari ve tasarım dokümantasyonu
├── tests/                  # Test planı ve örnek sorular
├── requirements.txt        # Proje bağımlılıkları (python-docx ve pypdf)
└── .gitignore              # Git tarafından takip edilmeyecek dosyalar
```

---

## Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/Taka-source14/microsoft-RAG-project.git
cd "Local RAG Project Management Assistant"
```

### 2. Sanal Ortam Oluşturun ve Aktive Edin
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. CLI Uygulamasını Çalıştırın
```bash
python app.py
```

---

## Örnek Sorular ve Beklenen Davranışlar

Uygulama çalıştıktan sonra sorabileceğiniz örnek sorular:
* `Titanic EDA programı kaç haftalık?` (DOCX veya PDF dosyasından kısa süre bilgisi çeker)
* `Phase 1 neyi kapsıyor?` (Karışık dilli dokümanlarda Phase 1 içeriğini getirir)
* `Day 5'te ne anlatılıyor?` (İlgili günün ders detayını getirir)
* `Bu projenin amacı nedir?` (RAG proje amacını getirir)
* `Bugün hava nasıl?` (Bilgi bulunamadı uyarısı döner)

---

## Sınırlamalar ve Gelecek Geliştirmeler

Bu proje basit, offline çalışan anahtar kelime tabanlı bir MVP prototipidir. Aşağıdaki gelişmiş özellikler şu anki sürümde **mevcut değildir** ve gelecek iyileştirmeler olarak planlanmıştır:
* **Uzak/Yerel LLM Entegrasyonu (Foundry Local):** Şu anki sürümde cevaplar doğrudan ilgili paragraftan kırpılarak oluşturulmaktadır. Gelecekte Foundry Local veya yerel Llama/Mistral entegrasyonu ile cevapların akıcı bir şekilde özetlenmesi sağlanacaktır.
* **Vektör Embedding Tabanlı Arama:** Anahtar kelime eşleşmesi yerine Cosine Similarity ile semantik arama yapılması.
* **SQLite Vektör Deposu:** Chunkların yerel bir veri tabanında saklanması.
* **Tesseract OCR Desteği:** Taranmış (resim tabanlı) PDF dosyalarının taranarak okunabilmesi.
* **Web Arayüzü (Streamlit):** Web tarayıcısı üzerinden etkileşim.
