# Test Soruları ve Beklenen Davranışlar

Bu dosya, yerel RAG asistanının (YBS Proje Takip Asistanı) doğruluğunu ve güvenliğini doğrulamak amacıyla oluşturulmuş test soru listesidir.

---

## 1. Cevaplanabilir Sorular (Dokümanlarda Bilgisi Olanlar)

Aşağıdaki soruların yanıtları `documents/` klasöründeki dosyalarda yer almaktadır. Sistem bu sorular sorulduğunda ilgili kaynak dokümanları ve Chunk ID'lerini doğru şekilde bulmalı ve yanıtı döndürmelidir.

### Test Soruları:
1. **Soru:** `Bu projenin amacı nedir?`
   * *Beklenen Kaynaklar:* `proje_amaci.txt` (Chunk 2 ve/veya 3), `haftalik_plan.txt`
2. **Soru:** `RAG nedir?`
   * *Beklenen Kaynaklar:* `rag_aciklamasi.txt` ve `proje_amaci.txt`
3. **Soru:** `Teslim kriterleri nelerdir?`
   * *Beklenen Kaynaklar:* `teslim_kriterleri.txt`
4. **Soru:** `Projede hangi riskler var?`
   * *Beklenen Kaynaklar:* `riskler.txt`
5. **Soru:** `3. haftada ne yapılacak?`
   * *Beklenen Kaynaklar:* `haftalik_plan.txt`
6. **Soru:** `Sunumda ne anlatmalıyım?`
   * *Beklenen Kaynaklar:* `sunum_notlari.txt`

---

## 2. Cevaplanamaz Sorular (Dokümanlarda Bilgisi Olmayanlar)

Aşağıdaki soruların yanıtları bilgi tabanında bulunmamaktadır. Sistem bu soruları aldığında halüsinasyon üretmemeli, kendi genel bilgisiyle cevap uydurmamalı ve güvenli şekilde aşağıdaki hata mesajını vermelidir.

**Beklenen Yanıt:**
```text
Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.
```

### Test Soruları:
1. **Soru:** `Bugün hava nasıl?`
2. **Soru:** `Bitcoin fiyatı nedir?`
3. **Soru:** `Türkiye'nin nüfusu kaçtır?`

---

## 3. Test Sonuçlarının Doğrulanması

Sistem CLI üzerinden çalıştırılarak (`python app.py`) veya test edilerek doğrulanmıştır. Her iki gruptaki tüm sorular yukarıda belirtilen beklenen davranışları tam olarak sergilemektedir.