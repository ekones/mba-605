# Örgütsel Davranış – Vize Soru Platformu

```
├── *.pptx / *.ppt              # ders notları (kaynak)
├── notes_text/                 # slaytlardan çıkarılmış düz metin
├── docs/                       # statik soru çözme platformu (GitHub Pages uyumlu)
│   ├── index.html · style.css · app.js · questions-data.js
│   └── data/
│       ├── manifest.json       # tüm sürümlerin listesi
│       └── v1.json, v2.json …  # her biri 25 soruluk set
├── tools/
│   ├── extract_text.py         # pptx/ppt → notes_text/*.txt
│   ├── validate_questions.py   # soru bankası doğrulama
│   └── build_js_bundle.py      # questions-data.js paketleme
└── .agents/skills/soru-uret/   # "soruları üret" talimatı (yeni vN.json üretir)
```

## Çalıştırma

Platformu **2 farklı şekilde** kullanabilirsiniz:

1. **Doğrudan Çift Tıklayarak (Sunucusuz):**
   `docs/index.html` dosyasını tarayıcınızda çift tıklayarak doğrudan açabilirsiniz. Sorular `docs/questions-data.js` içerisine gömülü olduğu için herhangi bir yerel HTTP sunucusuna ihtiyaç duymaz.

2. **Yerel HTTP Sunucusu ile:**
   ```bash
   python3 -m http.server 8000 --directory docs
   # tarayıcıda: http://localhost:8000
   ```

## Yeni soru seti

Ajana **"soruları üret"** demeniz yeterli: önceki setlerle çakışmayan 25 yeni soru `docs/data/vN.json`
olarak eklenir ve `manifest.json` güncellenir. Kontrol için:

```bash
python3 tools/validate_questions.py
```
