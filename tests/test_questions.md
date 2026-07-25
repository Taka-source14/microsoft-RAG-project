# Test Soruları ve Manuel Kontrol Listesi

Bu dosya, yerel RAG asistanının (YBS Proje Takip Asistanı) doğruluğunu ve RAG pipeline işlevlerini doğrulamak için hazırlanan test soru listesidir.

---

## 1. Doküman Odaklı Test Soruları (Semantik Arama ve Kısa Cevap)

Aşağıdaki sorular, `documents/` klasöründeki mixed `.docx` veya `.pdf` dokümanlarının (örneğin Titanic EDA planı veya proje yönetimi ek dokümanları) içeriğini test etmek için tasarlanmıştır.

### Test Soruları:
1. **Soru:** `RAG nedir?`
   * *Beklenen Yanıt:* RAG kavramının ve asistanın yerel proje yönetiminde nasıl kullanıldığının kısa açıklaması.
2. **Soru:** `Bu projenin amacı nedir?`
   * *Beklenen Yanıt:* Proje amacını gösteren kısa bir yanıt.
3. **Soru:** `Titanic EDA programı kaç haftalık?`
   * *Beklenen Yanıt:* Programın 4 haftalık uzaktan bir eğitim olduğunu belirten kısa bir yanıt.
4. **Soru:** `Day 5'te ne anlatılıyor?`
   * *Beklenen Yanıt:* 5. Günün ana konusuna odaklanan kısa bir yanıt.

---

## 2. RAG ve Teknik Kavramlar (Bilgi Tabanına Bağlı Olarak)

1. **Soru:** `Foundry Local nedir?`
   * *Beklenen Yanıt:* Eğer dokümanlarda mevcutsa ilgili açıklama, yoksa fallback mesajı.
2. **Soru:** `Embedding ne işe yarar?`
   * *Beklenen Yanıt:* Metinlerin sayısal vektörlere çevrilmesi ile ilgili kısa bir açıklama veya fallback mesajı.
3. **Soru:** `Vector search ne işe yarar?`
   * *Beklenen Yanıt:* Benzerlik eşleştirmesi ile ilgili kısa bir açıklama veya fallback mesajı.

---

## 3. Cevaplanamaz / Alakasız Sorular (Güvenlik Kontrolü)

Aşağıdaki sorular bilgi tabanında bulunmamaktadır. Asistan bilgi uydurmamalı (halüsinasyon görmemeli) ve güvenli fallback mesajını vermelidir.

### Test Soruları:
1. **Soru:** `Bugün hava nasıl?`
   * *Beklenen Yanıt:* `Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.`
2. **Soru:** `Bitcoin fiyatı kaç?`
   * *Beklenen Yanıt:* `Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.`

---

## 4. Beklenen Çıktı Formatı

Cevaplar yerel SQLite veritabanındaki (`rag.db`) chunk'lardan semantik benzerlik skorları hesaplanarak oluşturulur.

### Format Örneği:
```text
Cevap:
[Cevap metni]

Kaynaklar:
- file_name.ext - Chunk X (Score: Y)
```