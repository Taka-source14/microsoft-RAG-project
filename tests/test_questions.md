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

---

## 4. DOCX / PDF Desteği Manuel Test Kontrol Listesi

PDF ve DOCX dosyalarının başarıyla yüklenebildiğini ve sorgulanabildiğini manuel olarak test etmek için aşağıdaki adımları izleyin:

1. `documents/` klasörüne örnek bir `.docx` dosyası yerleştirin (örn: `ek_plan.docx`, içerik: "Sanal ortam kurulumu birinci aşamada tamamlanacaktır.")
2. `documents/` klasörüne metin tabanlı bir `.pdf` dosyası yerleştirin (örn: `ek_riskler.pdf`, içerik: "Bütçe aşımı riski projenin dördüncü haftasında kritik seviyeye ulaşabilir.")
3. Uygulamayı başlatın: `python app.py`
4. Yeni dosyaların başarıyla yüklendiğini teyit edin (Yüklenen doküman ve oluşturulan chunk sayısı artacaktır).
5. Şu soruyu sorun: `Kurulum hangi aşamada tamamlanacak?`
6. Cevabın `ek_plan.docx` kaynağını gösterdiğini doğrulayın.
7. Şu soruyu sorun: `Bütçe aşımı riski ne zaman kritik olacak?`
8. Cevabın `ek_riskler.pdf` kaynağını gösterdiğini doğrulayın.
9. Taranmış (yalnızca resim içeren) veya içi tamamen boş bir PDF/DOCX yerleştirerek uygulamanın hata vermeden çalıştığını, terminalde *"okunabilir metin bulunamadı. Dosya atlandı."* uyarısı vererek bu dosyayı güvenle atladığını doğrulayın.