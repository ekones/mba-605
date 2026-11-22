#!/usr/bin/env python3
"""Ders notlarından (pptx / ppt) düz metin çıkarır -> notes_text/ klasörü."""
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "notes_text"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def pptx_text(path: Path) -> str:
    out = []
    with zipfile.ZipFile(path) as z:
        slides = [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        slides.sort(key=lambda n: int(re.findall(r"\d+", n)[-1]))
        for i, name in enumerate(slides, 1):
            root = ET.fromstring(z.read(name))
            paras = []
            for p in root.iter(f"{{{NS['a']}}}p"):
                t = "".join(r.text or "" for r in p.iter(f"{{{NS['a']}}}t")).strip()
                if t:
                    paras.append(t)
            # speaker notes
            notes_name = f"ppt/notesSlides/notesSlide{re.findall(r'\d+', name)[-1]}.xml"
            notes = []
            if notes_name in z.namelist():
                nroot = ET.fromstring(z.read(notes_name))
                for p in nroot.iter(f"{{{NS['a']}}}p"):
                    t = "".join(r.text or "" for r in p.iter(f"{{{NS['a']}}}t")).strip()
                    if t and not t.isdigit():
                        notes.append(t)
            out.append(f"--- Slayt {i} ---")
            out.extend(paras)
            if notes:
                out.append("[Notlar] " + " ".join(notes))
    return "\n".join(out)


def ppt_text(path: Path) -> str:
    """Eski binary .ppt: TextCharsAtom (UTF-16LE, type 0x0FA0) ve TextBytesAtom (0x0FA8)."""
    data = path.read_bytes()
    out = []
    i = 0
    n = len(data)
    while i < n - 8:
        rec_type = int.from_bytes(data[i + 2:i + 4], "little")
        if rec_type in (0x0FA0, 0x0FA8):
            ver_inst = int.from_bytes(data[i:i + 2], "little")
            length = int.from_bytes(data[i + 4:i + 8], "little")
            if (ver_inst & 0x000F) == 0 and 0 < length < 20000 and i + 8 + length <= n:
                raw = data[i + 8:i + 8 + length]
                try:
                    txt = raw.decode("utf-16-le") if rec_type == 0x0FA0 else raw.decode("cp1254")
                except UnicodeDecodeError:
                    txt = None
                if txt and sum(c.isprintable() or c in "\r\n\t\x0b" for c in txt) / len(txt) > 0.95:
                    txt = txt.replace("\r", "\n").replace("\x0b", "\n").strip()
                    if txt:
                        out.append(txt)
                    i += 8 + length
                    continue
        i += 1
    # tekrarları sırayı koruyarak at
    seen, uniq = set(), []
    for t in out:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return "\n".join(uniq)


def main():
    OUT.mkdir(exist_ok=True)
    for f in sorted(ROOT.iterdir()):
        if f.suffix.lower() == ".pptx":
            txt = pptx_text(f)
        elif f.suffix.lower() == ".ppt":
            txt = ppt_text(f)
        else:
            continue
        dest = OUT / (f.stem + ".txt")
        dest.write_text(txt, encoding="utf-8")
        print(f"{f.name}: {len(txt)} karakter -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
