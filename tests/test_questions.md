# Test Soruları ve Manuel Kontrol Listesi

Bu dosya, yerel RAG asistanının (YBS Proje Takip Asistanı) doğruluğunu ve kısa cevap formatını doğrulamak için hazırlanan test soru listesidir.

---

## 1. DOCX / PDF Test Soruları (Kısa Cevap Doğrulaması)

Aşağıdaki sorular, `documents/` klasöründeki mixed (Türkçe-İngilizce karışık) `.docx` veya `.pdf` dokümanlarının (örneğin Titanic EDA ders planı veya proje yönetimi ek dokümanları) içeriğini test etmek için tasarlanmıştır.

### Test Soruları:
1. **Soru:** `Titanic EDA programı kaç haftalık?`
   * *Beklenen Cevap:* Programın 4 haftalık uzaktan bir eğitim olduğunu ve yaklaşık 20 günlük oturumdan oluştuğunu belirten kısa bir yanıt (maksimum 3-5 cümle).
2. **Soru:** `Phase 1 neyi kapsıyor?`
   * *Beklenen Cevap:* Phase 1 (1. Aşama) kapsamındaki konuları özetleyen kısa bir yanıt (maksimum 4 cümle).
3. **Soru:** `Day 5'te ne anlatılıyor?`
   * *Beklenen Cevap:* Day 5 (5. Gün) konusuna odaklanan kısa bir yanıt.
4. **Soru:** `Final presentations hangi gün yapılıyor?`
   * *Beklenen Cevap:* Final sunumlarının (presentations) yapılacağı günü/tarihi gösteren kısa bir yanıt.

---

## 2. TXT Test Soruları (Geriye Dönük Uyumluluk)

Aşağıdaki sorular, asistanın mevcut Türkçe metin (.txt) dosyalarıyla hâlâ doğru çalıştığını doğrulamak içindir.

### Test Soruları:
1. **Soru:** `Bu projenin amacı nedir?`
   * *Beklenen Kaynaklar:* `proje_amaci.txt` (Chunk 2) ve/veya `haftalik_plan.txt`
2. **Soru:** `RAG nedir?`
   * *Beklenen Kaynaklar:* `rag_aciklamasi.txt` (Chunk 1)

---

## 3. Cevaplanamaz / Alakasız Sorular (Güvenlik Kontrolü)

Aşağıdaki soru bilgi tabanında bulunmamaktadır. Asistan halüsinasyon görmemeli ve güvenli fallback mesajını vermelidir.

### Test Soruları:
1. **Soru:** `Bugün hava nasıl?`
   * *Beklenen Yanıt:*
     ```text
     Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.
     ```

---

## 4. Beklenen Çıktı Formatı

Cevaplar artık tüm paragrafı yazdırmak yerine, **en alakalı chunk'ın ilk 3-5 cümlesini** içerecek şekilde sınırlandırılmıştır. 

### Format Örneği:
```text
Cevap: Titanic EDA programı dört haftalık uzaktan bir Python ve Pandas veri bilimi programıdır. Program yaklaşık 20 günlük oturumdan oluşur.

Kaynaklar:
* titanic_eda_plan.docx - Chunk 1 (Score: 8)
```