# Test Soruları ve Manuel Kontrol Listesi

Bu dosya, yerel RAG asistanının (YBS Proje Takip Asistanı) doğruluğunu ve RAG pipeline işlevlerini doğrulamak için hazırlanan test soru listesidir.

---

## 1. Doküman Odaklı Test Soruları (Semantik Arama ve Kısa Cevap)

Aşağıdaki sorular, `documents/` klasöründeki dokümanların içeriğini test etmek için tasarlanmıştır.

### Test Soruları:
1. **Soru:** `RAG nedir?`
   * *Beklenen Yanıt:* RAG kavramının kısa açıklaması.
2. **Soru:** `Bu projenin amacı nedir?`
   * *Beklenen Yanıt:* Proje amacını (dokümanlara erişilebilirlik ve cevap üretme) gösteren kısa bir yanıt.
3. **Soru:** `Foundry Local nedir?`
   * *Beklenen Yanıt:* Microsoft Foundry Local ile ilgili yerel dokümanlarda yer alan açıklama.
4. **Soru:** `Embedding ne işe yarar?`
   * *Beklenen Yanıt:* Metin parçalarının sayısal vektörlere dönüştürülmesi ile ilgili kısa açıklama.
5. **Soru:** `Vector search ne işe yarar?`
   * *Beklenen Yanıt:* Cosine similarity benzerlik aramaları ve SQLite entegrasyonu ile ilgili kısa açıklama.
6. **Soru:** `Bu sistem hangi dosya türlerini destekliyor?`
   * *Beklenen Yanıt:* Desteklenen dosya uzantılarını (.txt, .docx, .pdf) içeren açıklama.

---

## 2. Cevaplanamaz / Alakasız Sorular (Güvenlik Kontrolü)

Aşağıdaki sorular bilgi tabanında bulunmamaktadır. Asistan bilgi uydurmamalı (halüsinasyon görmemeli) ve güvenli fallback mesajını vermelidir.

### Test Soruları:
1. **Soru:** `Bugün hava nasıl?`
   * *Beklenen Yanıt:* `Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.`
2. **Soru:** `Bitcoin fiyatı kaç?`
   * *Beklenen Yanıt:* `Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.`

---

## 3. Beklenen Çıktı Formatı

Cevaplar yerel SQLite veritabanındaki (`rag.db`) chunk'lardan semantik benzerlik skorları hesaplanarak oluşturulur.

### Format Örneği:
```text
Cevap:
[Cevap metni]

Kaynaklar:
- file_name.ext - Chunk X (Score: Y)
```