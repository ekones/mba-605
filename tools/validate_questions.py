#!/usr/bin/env python3
"""Soru bankasını doğrular.

Kontroller:
  * manifest.json içindeki her sürüm dosyası mevcut ve geçerli JSON
  * her sürümde tam 25 soru, her soruda 5 benzersiz şık, geçerli cevap indeksi
  * soru id'leri benzersiz, bölüm numarası manifest'te tanımlı
  * sürümler arası tekrar eden / çok benzer soru kökü yok
  * manifest'te listelenmemiş vN.json dosyası yok

Kullanım:  python3 tools/validate_questions.py
"""
import difflib
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "docs" / "data"
QUESTIONS_PER_SET = 25
OPTIONS_PER_QUESTION = 5
SIMILARITY_LIMIT = 0.80
REQUIRED = ("id", "chapter", "topic", "difficulty", "question", "options", "answer", "explanation", "source")
DIFFICULTIES = {"kolay", "orta", "zor"}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.sub(r"[^\w]+", " ", text).strip()


def main() -> int:
    errors, warnings = [], []
    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    chapters = set(manifest["chapters"].keys())
    listed = set()
    all_stems = []  # (version, id, normalized stem)
    seen_ids = set()

    for v in manifest["versions"]:
        path = DATA / v["file"]
        listed.add(v["file"])
        if not path.exists():
            errors.append(f"{v['id']}: {v['file']} bulunamadı")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        qs = data.get("questions", [])
        if data.get("id") != v["id"]:
            errors.append(f"{v['file']}: id '{data.get('id')}' manifest ile uyuşmuyor ('{v['id']}')")
        if len(qs) != QUESTIONS_PER_SET:
            errors.append(f"{v['id']}: {len(qs)} soru var, {QUESTIONS_PER_SET} olmalı")
        if v.get("questionCount") != len(qs):
            errors.append(f"{v['id']}: manifest questionCount={v.get('questionCount')} ama dosyada {len(qs)} soru")

        answers = Counter()
        per_chapter = Counter()
        for q in qs:
            qid = q.get("id", "?")
            missing = [k for k in REQUIRED if k not in q]
            if missing:
                errors.append(f"{qid}: eksik alanlar {missing}")
                continue
            if qid in seen_ids:
                errors.append(f"{qid}: id tekrar ediyor")
            seen_ids.add(qid)
            if str(q["chapter"]) not in chapters:
                errors.append(f"{qid}: bölüm {q['chapter']} manifest'te yok")
            if q["difficulty"] not in DIFFICULTIES:
                errors.append(f"{qid}: zorluk '{q['difficulty']}' geçersiz")
            opts = q["options"]
            if len(opts) != OPTIONS_PER_QUESTION:
                errors.append(f"{qid}: {len(opts)} şık var, {OPTIONS_PER_QUESTION} olmalı")
            if len({norm(o) for o in opts}) != len(opts):
                errors.append(f"{qid}: tekrar eden şık var")
            if not (isinstance(q["answer"], int) and 0 <= q["answer"] < len(opts)):
                errors.append(f"{qid}: cevap indeksi geçersiz ({q['answer']})")
            answers["ABCDE"[q["answer"]] if isinstance(q["answer"], int) and 0 <= q["answer"] < 5 else "?"] += 1
            per_chapter[q["chapter"]] += 1
            all_stems.append((v["id"], qid, norm(q["question"])))

        dist = " ".join(f"{k}:{answers[k]}" for k in "ABCDE")
        chap = " ".join(f"B{c}:{n}" for c, n in sorted(per_chapter.items()))
        print(f"✔ {v['id']:<4} {len(qs)} soru | cevap dağılımı {dist} | {chap}")
        if max(answers.values(), default=0) - min((answers[k] for k in "ABCDE"), default=0) > 2:
            warnings.append(f"{v['id']}: cevap harfi dağılımı dengesiz ({dist})")

    # sürümler arası benzerlik
    for i in range(len(all_stems)):
        for j in range(i + 1, len(all_stems)):
            vi, qi, si = all_stems[i]
            vj, qj, sj = all_stems[j]
            r = difflib.SequenceMatcher(None, si, sj).ratio()
            if r >= SIMILARITY_LIMIT:
                (errors if r > 0.95 else warnings).append(f"{qi} ~ {qj}: soru kökleri çok benzer (%{r*100:.0f})")

    for f in DATA.glob("v*.json"):
        if f.name not in listed:
            warnings.append(f"{f.name} manifest'te listelenmemiş")

    for w in warnings:
        print("⚠", w)
    for e in errors:
        print("✘", e)
    print(f"\nToplam {len(all_stems)} soru, {len(manifest['versions'])} sürüm. "
          f"{'HATA YOK' if not errors else str(len(errors)) + ' HATA'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
