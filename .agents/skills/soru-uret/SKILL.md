---
name: soru-uret
description: >-
  Örgütsel Davranış ders notlarından yeni bir vize deneme seti (25 farklı çoktan seçmeli soru)
  üretir, docs/data/vN.json olarak kaydeder ve manifest'e ekler. Kullanıcı "soruları üret",
  "yeni soru seti", "25 soru daha" gibi bir şey istediğinde kullan.
---

# Yeni soru seti üretme

Her "soruları üret" isteğinde **önceki setlerde olmayan 25 yeni soru** içeren yeni bir sürüm oluştur.

## Adımlar

1. **Kaynakları oku**
   - Ders notlarının düz metni `notes_text/*.txt` içinde. Yoksa ya da slaytlar değiştiyse yeniden çıkar:
     `python3 tools/extract_text.py`
   - Yalnızca notlarda geçen bilgilerden soru üret; notlarda olmayan "dış bilgi" ile doğru cevap kurma.

2. **Mevcut setleri incele** – `docs/data/manifest.json` ve tüm `docs/data/v*.json` dosyalarını oku.
   - Önceki setlerde sorulmuş kavramları/senaryoları **tekrarlama**. Aynı kavram tekrar sorulacaksa
     farklı bir açıdan (ör. tanım yerine senaryo, "hangisi değildir" vb.) ve farklı kökle sor.
   - Henüz sorulmamış konulara öncelik ver (her setin `topic` alanlarına bak).

3. **Yeni sürüm numarasını belirle** – manifest'teki en büyük N + 1 → `vN`.

4. **25 soru yaz** – kurallar:
   - Dil: Türkçe, MBA vize seviyesi. Tanım soruları ile senaryo/uygulama sorularını karıştır
     (yaklaşık en az %40 senaryo). Sorular birbirine yakın kavramlar arasında ikilem yaratacak, analitik ve çeldiricisi güçlü MBA düzeyinde hazırlanmalıdır.
   - **Şıklarda parantez içi ipucu yasaktır:** Şıklarda parantez içinde İngilizce karşılık, kısaltma veya ek açıklama (örn. "(Turnover)", "(EBM)", "(ÖVD)", "(Voice)" vb.) kesinlikle kullanılmamalıdır; akademik Türkçe terim yalın olarak verilmelidir.
   - Her soruda **tam 5 şık** (A–E), tek doğru cevap; çeldiriciler aynı bölümden makul kavramlar olsun.
   - **Cevap dağılımı dengeli:** her harf (A, B, C, D, E) tam 5 kez doğru cevap olsun.
   - Bölüm dağılımı: Vize kapsamındaki 5 bölümün hepsinden eşit soru (Bölüm 1'den 5'e kadar her birinden 5'er soru).
   - Zorluk karışımı: yaklaşık 3 kolay, 15 orta, 7 zor.
   - "Hepsi / hiçbiri" şıklarından kaçın. Olumsuz köklerde "DEĞİLDİR / YER ALMAZ" büyük harfle yazılsın.
   - Her soruya notlara dayanan kısa bir `explanation` ve slayt/başlık bilgisi içeren `source` ekle.

5. **Dosyayı yaz** – `docs/data/vN.json`, şema:

   ```json
   {
     "id": "vN", "version": N, "title": "Vize Deneme Seti N",
     "course": "Örgütsel Davranış", "createdAt": "YYYY-MM-DD",
     "description": "…",
     "questions": [
       {
         "id": "vN-q01", "chapter": 1, "topic": "…", "difficulty": "kolay|orta|zor",
         "question": "…", "options": ["…","…","…","…","…"],
         "answer": 0,
         "explanation": "…", "source": "…"
       }
     ]
   }
   ```
   `answer` = doğru şıkkın 0 tabanlı indeksi (0=A … 4=E). Bölüm numaraları manifest'teki `chapters` ile eşleşmeli.

6. **Manifest'e ekle** – `docs/data/manifest.json` → `versions` dizisinin sonuna:
   `{ "id": "vN", "file": "vN.json", "title": "Vize Deneme Seti N", "createdAt": "YYYY-MM-DD", "questionCount": 25 }`

7. **Doğrula** – `python3 tools/validate_questions.py` çalıştır; HATA YOK ve dengeli dağılım görene kadar düzelt.
   Benzerlik uyarısı (⚠) çıkarsa ilgili soruyu yeniden yaz.

8. **JS Paketini Güncelle** – `python3 tools/build_js_bundle.py` çalıştır; böylece yeni eklenen set `docs/questions-data.js` içine gömülür ve çift tıklayarak (file://) doğrudan çalışmaya devam eder.

9. Kullanıcıya kısaca hangi sürümün eklendiğini, bölüm dağılımını ve platformun nasıl açılacağını bildir:
   `docs/index.html` dosyasını doğrudan tarayıcıda açabilir veya `python3 -m http.server 8000 --directory docs` ile çalıştırabilir.
