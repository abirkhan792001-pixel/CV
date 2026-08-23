#!/usr/bin/env python3
"""Stamp document metadata onto the built PDF and write a share-ready copy.

Playwright's page.pdf() takes the title from <title> but exposes no other
metadata, so Chromium leaves Author, Subject and Keywords empty and stamps
itself as Creator. Those fields are what a PDF viewer shows in its title
bar, what an email client previews, and what some applicant-tracking
systems index -- worth filling in on a document that gets sent to
recruiters.
"""
import pymupdf, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC  = ROOT / "Abir_Khan_CV.pdf"
OUT  = ROOT / "Abir_Hilal_Khan_CV.pdf"
# Repo convention for a tailored copy: "Abir Hilal Khan_CV_<target>.pdf".
NAMED = ROOT / "Abir Hilal Khan_CV_Oliver Wyman.pdf"

A4_W, A4_H = 595.276, 841.890          # exact A4 in points

doc = pymupdf.open(SRC)

# Chromium snaps the page to whole device pixels, so width comes out at
# 210.23mm rather than 210.00. The content's right edge sits at 191.82mm and
# its last text at 285.93mm, so trimming the mediabox to exact A4 removes
# blank margin only -- nothing on the page moves or is clipped.
for page in doc:
    r = page.rect
    assert r.width >= A4_W - 0.01 and r.height >= A4_H - 0.01, "page smaller than A4"
    page.set_mediabox(pymupdf.Rect(0, 0, A4_W, A4_H))
doc.set_metadata({
    "title":    "Abir Hilal Khan - CV",
    "author":   "Abir Hilal Khan",
    "subject":  "Curriculum Vitae",
    # Every term here also appears on the page. Metadata that names things a
    # reader cannot see is keyword stuffing, and an ATS that indexes both will
    # find the same words twice either way.
    "keywords": ("Management Consulting, Strategy Consulting, Structured Problem Solving, "
                 "Root-Cause Analysis, Market Sizing, Competitive Benchmarking, Market Entry, "
                 "Commercial Due Diligence, Financial Modelling, Scenario Models, "
                 "Stakeholder Interviews, Executive Communication, Growth Strategy, "
                 "Operating Model Transformation, Restructuring, Turnaround, "
                 "Venture Capital, Private Equity, "
                 "Advanced Microsoft Excel, PowerPoint, Power BI, SQL, Python, Data Analytics, "
                 "MSc Finance, Nova SBE, Dubai, Doha, Arabic"),
    "creator":  "Abir Hilal Khan",
    "producer": "",
})
# garbage=4 dedupes and drops unreferenced objects; deflate recompresses
# streams. Neither touches image data or vector geometry.
doc.save(OUT, garbage=4, deflate=True, clean=True)
doc.close()
NAMED.write_bytes(OUT.read_bytes())

chk = pymupdf.open(OUT)
p = chk[0]
assert chk.page_count == 1, "expected one page"
assert abs(p.rect.width - A4_W) < 0.01 and abs(p.rect.height - A4_H) < 0.01, "not exact A4"
assert all(f[1] for f in p.get_fonts(full=True)), "a font is not embedded"
print(f"  wrote {OUT.name}  {OUT.stat().st_size:,} bytes")
print(f"  title    {chk.metadata['title']}")
print(f"  author   {chk.metadata['author']}")
print(f"  pages    {chk.page_count}   fonts embedded: all {len(p.get_fonts())}")
print(f"  size     {p.rect.width:.2f} x {p.rect.height:.2f} pt = "
      f"{p.rect.width*25.4/72:.2f} x {p.rect.height*25.4/72:.2f} mm (exact A4)")
for im in p.get_images(full=True):
    info = chk.extract_image(im[0])
    for r in p.get_image_rects(im[0]):
        dpi = info['width'] / (r.width * 25.4 / 72 / 25.4)
        print(f"  photo    {info['width']}x{info['height']} -> {dpi:.0f} DPI at {r.width*25.4/72:.1f}mm")
print(f"  text     {len(p.get_text().split())} words selectable (ATS-readable)")
print(f"  copy     {NAMED.name}")
