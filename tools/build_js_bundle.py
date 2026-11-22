#!/usr/bin/env python3
"""docs/data/manifest.json ve docs/data/v*.json dosyalarını okur,
docs/questions-data.js dosyasına window.QUIZ_DATA olarak yazar.
Böylece platform `file://` protokolüyle (çift tıklayarak) de doğrudan çalışabilir.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "docs" / "data"
OUT_FILE = ROOT / "docs" / "questions-data.js"


def build():
    manifest_path = DATA_DIR / "manifest.json"
    if not manifest_path.exists():
        print(f"Hata: {manifest_path} bulunamadı.")
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    versions_data = {}

    for v in manifest.get("versions", []):
        v_file = DATA_DIR / v["file"]
        if v_file.exists():
            v_json = json.loads(v_file.read_text(encoding="utf-8"))
            versions_data[v["id"]] = v_json
        else:
            print(f"Uyarı: {v_file} bulunamadı.")

    bundle = {
        "manifest": manifest,
        "versions": versions_data
    }

    content = f"// Bu dosya otomatik üretilmiştir. (tools/build_js_bundle.py)\nwindow.QUIZ_DATA = {json.dumps(bundle, ensure_ascii=False, indent=2)};\n"
    OUT_FILE.write_text(content, encoding="utf-8")
    print(f"Başarılı: {len(versions_data)} sürüm {OUT_FILE.relative_to(ROOT)} içine gömüldü.")


if __name__ == "__main__":
    build()
