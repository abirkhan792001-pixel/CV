#!/usr/bin/env python3
"""Audit the share-ready PDF: ATS parseability first, then layout.

Run after `npm run share`. Everything here is measured out of the rendered
PDF rather than the source, so it reflects what a reader -- and a parser --
actually receives.
"""
import pymupdf, pathlib, re, sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDF  = ROOT / "Abir_Hilal_Khan_CV.pdf"
PT   = 25.4 / 72

doc  = pymupdf.open(PDF)
page = doc[0]
text = page.get_text()                       # stream order: what a naive ATS reads
lines = [l for l in text.split("\n") if l.strip()]

fails = []
def check(ok, label, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}{('  -- ' + detail) if detail else ''}")
    if not ok:
        fails.append(label)

print("\nATS")
check(doc.page_count == 1, "single page", f"{doc.page_count}")
check(len(text.split()) > 400, "text is real text, not an image", f"{len(text.split())} words selectable")
check(all(f[1] for f in page.get_fonts(full=True)), "all fonts embedded",
      f"{len(page.get_fonts())} fonts")

# Contact block: a parser must find each field as plain text.
check(bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text)), "email present as text")
check(bool(re.search(r"\+\d[\d ]{8,}", text)), "phone present as text")
check("linkedin.com/in/" in text, "LinkedIn profile spelled out, not hidden behind anchor text")
check(lines[0].strip().upper() == lines[0].strip() and len(lines[0].split()) >= 2,
      "name is the first line of the stream", lines[0])

# Section headers: parsers segment the document on these.
for h in ("EDUCATION", "WORK EXPERIENCE", "EXTRACURRICULAR", "SKILLS"):
    check(any(l.strip().startswith(h) for l in lines), f"section header {h!r} found in stream")

# Reading order: every bullet must follow its own employer, not pile up at the
# end of the document. This is what `position:relative` on li used to break.
def idx(pred):
    return next((i for i, l in enumerate(lines) if pred(l)), -1)
pairs = [
    ("Nova School",            "Top 10% of the class"),
    ("SCAILE Technologies",    "Owned North American clients"),
    ("Stealth Energy Venture", "Led digital transformation"),
    ("Alvarez & Marsal",       "Prepared creditor-negotiation"),
    ("Biome Venture Studio",   "Evaluated 3,000+ companies"),
    ("Trariti Consulting",     "Led 90+ stakeholder interviews"),
    ("Impact Consulting",      "Created competitive benchmarking"),
]
for org, bullet in pairs:
    i, j = idx(lambda l: l.startswith(org)), idx(lambda l: bullet in l)
    nxt = min([k for o, _ in pairs[pairs.index((org, bullet)) + 1:]
               for k in [idx(lambda l, o=o: l.startswith(o))] if k > i] or [len(lines)])
    check(i != -1 and i < j < nxt, f"bullets stay with {org!r}", f"org line {i}, bullet line {j}")

check(not any(l.strip() == "•" for l in lines), "no orphan bullet glyphs on their own line")
check(all(l.lstrip().startswith("•") for l in lines if "Top 10% of the class" in l),
      "bullet glyph sits on the same line as its text")

print("\nLAYOUT")
spans = [(ln["bbox"], "".join(s["text"] for s in ln["spans"]))
         for b in page.get_text("dict")["blocks"] if b["type"] == 0 for ln in b["lines"]]
left = Counter(round(b[0] * PT, 2) for b, _ in spans)
check(left.most_common(1)[0][0] == 19.06, "text left edge", str(left.most_common(4)))
check(round(max(b[3] for b, _ in spans) * PT, 2) < 297 - 8, "bottom white",
      f"{297 - max(b[3] for b, _ in spans) * PT:.2f} mm")

rules = [d["rect"] for d in page.get_drawings()
         if d["rect"].width > 100 and d["rect"].height < 3]
spanset = {(round(r.x0 * PT, 2), round(r.x1 * PT, 2)) for r in rules}
check(len(spanset) <= 2, "section rules share one span", str(sorted(spanset)))

photo = page.get_image_rects(page.get_images(full=True)[0][0])[0]
check(abs(photo.x1 * PT - max(r.x1 * PT for r in rules)) < 0.1,
      "photo right edge sits on the rules", f"{photo.x1 * PT:.2f} mm")

# The repo rule is that metadata may only name things the reader can see on the
# page. Checked here rather than by hand: a keyword a candidate cannot see on
# their own CV is one they cannot be asked about in an interview.
flat = " ".join(text.split()).lower()
# A hyphenated compound can take the line break at its own hyphen, leaving
# "creditor- negotiation" in the stream for a word the reader sees whole.
rejoined = flat.replace("- ", "-")
missing = [k.strip() for k in doc.metadata.get("keywords", "").split(",")
           if k.strip() and k.strip().lower() not in flat
           and k.strip().lower() not in rejoined]
check(not missing, "every metadata keyword also appears in the visible text",
      "missing: " + ", ".join(missing) if missing else
      f"{len(doc.metadata.get('keywords', '').split(','))} keywords, all on the page")

print("\nTYPOGRAPHY")
# Placeholders own the guillemets, so they are reported here by name rather than
# surfacing downstream as an unexplained non-ASCII failure.
holes = re.findall(r"\u00ab[^\u00bb]*\u00bb", " ".join(text.split()))
check(not holes, "no unfilled placeholders",
      "; ".join(holes) if holes else "none")
bad = {c for c in text if ord(c) > 127} - set("\u2022\u2019\u00d7\u00ab\u00bb")
check(not bad, "non-ASCII limited to bullet, curly apostrophe, times",
      "unexpected: " + repr(bad) if bad else "")
check("—" not in text and "–" not in text, "no em or en dashes")
check(not re.search(r"\d\d\.\d\d\.\d{4}|\b\d{4}-\d{2}\b", text), "dates are MM.YYYY throughout")

# The bullet glyph and its text share one run now, so the 25.41 mm text edge has
# to be read at character level rather than from line boxes.
starts, wrapped = [], []
for b in page.get_text("rawdict")["blocks"]:
    if b["type"] != 0:
        continue
    for ln in b["lines"]:
        chars = [c for sp in ln["spans"] for c in sp["chars"]]
        if chars and chars[0]["c"] == "\u2022":
            starts.append(round([c for c in chars[1:] if c["c"].strip()][0]["bbox"][0] * PT, 2))
        elif abs(ln["bbox"][0] * PT - 25.41) < 0.6:
            wrapped.append(ln)
check(set(starts) == {25.41}, "bullet text starts at 25.41 mm",
      f"{len(starts)} bullets, x = {sorted(set(starts))}")
check(not wrapped, "no bullet wraps to a second line", f"{len(wrapped)} wrapped")

# Nothing may cross the text right edge, and the right-aligned locations and
# dates must all land on it. Long bullets legitimately stop short of it.
EDGE = 191.84
rights = [round(b[2] * PT, 2) for b, t in spans]
check(max(rights) <= EDGE + 0.01, "nothing crosses the text right edge",
      f"widest line ends at {max(rights):.2f} mm")
flush = [r for r in rights if abs(r - EDGE) < 0.05]
# 10 entries x 2 rows (organisation/location, then role/dates). An exact count
# rather than a floor, so a silently dropped entry fails here too.
check(len(flush) == 20, "right-aligned column flush",
      f"{len(flush)} location/date lines on {EDGE} mm")

print(f"\n{'ALL CHECKS PASS' if not fails else str(len(fails)) + ' FAILED: ' + ', '.join(fails)}\n")
sys.exit(1 if fails else 0)
