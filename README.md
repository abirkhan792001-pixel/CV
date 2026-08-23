# CV — KPMG Luxembourg, Adviser: Risk Reporting for Investment Funds

A one-page A4 CV, tailored to KPMG Luxembourg's **Adviser — Risk Reporting for
Investment Funds (m/f/d)**, posted 30.06.2026. The role sits in KPMG's Risk
Advisory practice, which delivers risk monitoring and regulatory reporting to
funds and asset managers, and screens for 0–3 years in the financial sector.

Built on the same template as the other tailored CVs in this repo. Work-experience
copy is lifted from those CVs rather than rewritten, so the same claims appear the
same way everywhere.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> the files to actually send, then audits them
```

`npm run share` builds, runs `scripts/finalise.py` (needs `pymupdf`), then runs
`scripts/audit.py`. It writes two identical PDFs: `Abir_Hilal_Khan_CV.pdf` and
`Abir Hilal Khan_CV_KPMG Luxembourg.pdf`, the latter following this repo's naming
convention for a tailored copy.

If Playwright cannot download its pinned Chromium (sandboxes, offline CI), point
the build at one already on the machine:

```bash
CHROMIUM_PATH=/opt/pw-browsers/chromium npm run share
```

The finalise step differs from the raw build output in three ways, none of which
touch the layout:

- **Document metadata.** Playwright takes the title from `<title>` but exposes
  nothing else, so Chromium leaves Author, Subject and Keywords empty and stamps
  itself as Creator. Those fields are what a PDF viewer shows in its title bar,
  what an email client previews, and what some applicant-tracking systems index.
  Every keyword stamped there also appears on the page — see *Metadata says only
  what the page says* below.
- **Exact A4.** Chromium snaps the page to whole device pixels and lands on
  210.23 × 297.35 mm. The finalise step trims the mediabox to a true
  595.276 × 841.890 pt — blank margin only; it asserts the page is at least A4
  before cropping and exactly A4 after.
- **Verification.** It asserts one page and every font embedded, then reports
  photo DPI and selectable word count.

`build.mjs` measures the rendered content height against the A4 box and **exits
non-zero if the CV spills onto a second page**, so the one-page requirement is
enforced rather than eyeballed. It also counts unfilled `«placeholders»`.

Edit `cv.html` only — content and styling both live there. The tuning knobs for
fitting content are the CSS variables at the top: `--fs-base`, `--lh`,
`--margin-x`, `--margin-y`.

Current state: **295.5 mm of 297 mm, one page, 1.5 mm headroom.** Not enough for
another line; anything added has to be traded against something already there.

## This pass: the founder venture out, Trariti back in

The brief was to drop the stealth founder entry and restore the consulting
internship the earlier passes had cut. Both were done, and the rest of the page
was retuned for a risk-reporting role rather than an energy one.

### The two swaps

- **Out: Stealth AI-Energy Startup, Founder (since 08.2026).** Three bullets on
  DACH competitor mapping, a three-stage energy business model and an AI tool for
  German electricity bills. All of it was evidence for renewable energy, which is
  what the previous target screened on and this one does not.
- **In: Trariti Consulting Group (TCG), Summer Consultant, Mumbai, 03.2022 –
  08.2022.** Three bullets, taken verbatim from the source CVs: data-driven models
  for VC/PE firms, funding levers and investment viability across $100M+ in deal
  value, and 90+ stakeholder interviews.

The two entries cost the same height, so the swap alone was height-neutral.

Restoring this entry also **closes an open item the last audit raised**: nothing
on the page demonstrated stakeholder management, and the evidence for it —
*"Led 90+ stakeholder interviews…"* — lived in exactly the entry that had been
cut. It is back on the page, so the term in the skills row is now earned.

**The organisation is named in full.** Five source CVs write it as
*"TCG (boutique strategy consulting firm)"*; the DHL CV writes *"Trariti
Consulting Group"*. This CV uses **Trariti Consulting Group** with *(TCG, boutique
strategy consulting firm)* as the italic note, so a parser indexes a real company
name rather than a three-letter string, and a reader still learns what it is.

### What the rest of the page traded

The founder-for-Trariti swap was free, but the risk-reporting retune wanted four
lines the page did not have. Where they came from:

| Change | Lines |
|---|---|
| A new `Focus areas` row in the skills grid | −2 |
| Nova's relevant coursework restored as a bullet (Risk Management, Python) | −1 |
| A&M regains its creditor-negotiation bullet | −1 |
| Nova's class rank and Draycott merged onto one bullet | **+1** |
| **Impact Consulting dropped** from Extracurricular | **+3** |
| **Net** | **0 lines**, plus 1.3 mm recovered from one fewer entry margin and grid gap |

Which is why the page came down only from 296.8 mm to 295.5 mm: the line count is
unchanged, and the 1.3 mm is the whitespace between entries, not text.

**Impact Consulting was the entry to cut.** With Trariti restored, the page
already carries a consulting entry doing market and investment analysis, and
Impact's single bullet — competitive benchmarking and market-entry proposals for
a B2C fintech — was the weakest fit for a risk-reporting role and the closest
duplicate of work shown better elsewhere. Its three lines bought back the A&M
creditor-negotiation bullet, which carries the only hard value figure in that
entry ($2.5M preserved) and is the page's clearest evidence of preparing
material for client leadership.

## What this CV is optimised for

KPMG's posting screens on a list. Each item is mapped to a place on the page:

| What the posting asks for | Where it lands |
|---|---|
| **Master's in Finance / Quantitative Finance / related** | Education first, MSc Finance to 12.2026 |
| **0–3 years in the financial sector** | A&M restructuring, Biome VC, Trariti — all internships, none over 7 months |
| **Prepare and review risk and regulatory reports** | SCAILE's weekly client KPI reporting and dashboards; `Client Reporting` in Core skills |
| **Primary point of contact for client inquiries** | *"Owned North American clients as their first point of contact"*; *"Led 90+ stakeholder interviews"*; A&M's creditor-negotiation materials |
| **Gather and analyse client data for insights** | Biome's 3,000+ company screen; A&M scenario models |
| **Automate workflows, streamline processes** | *"Automated weekly client KPI reporting … cutting manual effort by 60%"*; `Process Automation` |
| **Contribute to internal reporting technologies** | SCAILE's KPI dashboards; Power BI, SQL, Python in Technical |
| **Interest in VaR and sensitivity analysis** | A&M's **EBITDA sensitivity analysis** bullet; Risk Management coursework; `Focus areas` row |
| **Highly proficient in Excel** | `Advanced Microsoft Excel` leads the Technical row |
| **Understanding of the investment funds industry** | Biome (VC, $170M pipeline), Trariti (VC/PE clients), Draycott PE Challenge |
| **VBA, Python, MATLAB or other data analytics** | Python, SQL, Power BI, `Data Analytics` |
| **European regulatory frameworks** | European Commission thesis; `EU Financial Regulation` |
| **Fluent English; German/French an advantage** | Languages row leads with English (Fluent), German (B1) |

Two choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  graduates, and this posting gates on the Master's.
- **Photo included.** All the source CVs except DHL carry one, and it is normal
  practice in Luxembourg. It is a separate element that a parser skips — the
  five-parser check below runs against the file as shipped, photo and all. To
  remove it, delete the `<img class="photo">` line; everything reflows.

## Where the risk vocabulary comes from

The posting is full of terms it would be easy to simply assert. The rule applied
here is the repo's existing one: **a keyword goes on the page only if something
on the page backs it.** So the skills grid is split in two.

`Core skills` are demonstrated by an entry above them:

| Term | Backed by |
|---|---|
| Financial Modelling | A&M scenario models, Biome build-ups, Trariti models |
| Scenario and Sensitivity Analysis | A&M: scenario models, EBITDA sensitivity |
| Data Analysis | Biome's 3,000+ company screen, SCAILE KPI reporting |
| Commercial Due Diligence | Biome |
| Client Reporting | SCAILE's weekly client reporting and dashboards |
| Process Automation | SCAILE's AI agent workflows, 60% manual effort cut |
| Stakeholder Management | Trariti's 90+ stakeholder interviews |
| Problem Solving | Top 3 of 15,000 nationally; Draycott Team Lead |

`Focus areas` are the target domain — Risk Management, Value at Risk (VaR),
Derivatives, Regulatory Reporting, Portfolio Risk Monitoring, Investment Funds and
Asset Management, EU Financial Regulation. Labelling them *focus areas* rather
than *skills* is deliberate: Risk Management is coursework, EU regulation is the
thesis, and the fund exposure is Biome and Trariti. It is the honest register for
a 0–3 years posting that asks for *interest* in these topics, and it is the source
CVs' own label.

**What is deliberately not claimed:** CRR, Solvency II, PRIIPs, UCITS, AIFMD,
VBA and MATLAB. The posting lists the first three as an asset and the last two as
a plus, and nothing in any source CV evidences any of them. See *Before sending*
— this is the single highest-value edit available if the candidate has in fact
studied them.

## Written for the ATS

KPMG Luxembourg recruits through an applicant-tracking system, so the parse is
the first round. `scripts/audit.py` checks the claims below against the **rendered
PDF**, not the source, and exits non-zero on any failure.

### The bullets used to detach from their employers

The biggest find in this repo's ATS work, and it was invisible on the page. The
old CSS gave every `li` a `position:relative` so the bullet glyph could be
absolutely positioned. Positioned elements paint in a later phase than normal-flow
content, so Chromium emitted **every bullet after the rest of the page** in the
PDF's text stream. A parser that reads that stream in order saw every achievement
orphaned at the end of the document, detached from the employer it belongs to,
each followed by a stray `•` on its own line. Nothing could be attributed to A&M,
to Biome, or to any date range.

The fix is a hanging indent built from normal flow — `text-indent` plus an
inline-block `::before` marker — instead of a positioned one. Document order is
preserved, and the geometry is unchanged: the glyph still sits at 21.89 mm and the
bullet text still starts at **exactly 25.41 mm** on all 20 bullets, verified at
character level.

### Five parsers, re-run on this version

Extraction was re-run on the shipped file after this pass. The check is stricter
than a text dump: it asserts the eight organisations appear in page order, and
that each of five leading bullets falls between its own employer and the next one.

| Extraction mode | Reading order | Email | Phone | LinkedIn |
|---|---|---|---|---|
| PyMuPDF `get_text()` — stream order | OK | ✓ | ✓ | ✓ |
| PyMuPDF `get_text(sort=True)` | OK | ✓ | ✓ | ✓ |
| pypdf `extract_text()` | OK | ✓ | ✓ | ✓ |
| pdfminer.six, default layout analysis | OK | ✓ | ✓ | ✓ |
| pdfminer.six, `laparams=None` | OK | ✓ | ✓ | ✓ |

Stream order is the mode that matters most: Apache PDFBox, which underpins Tika
and a lot of enterprise résumé parsing, has `sortByPosition` **off** by default.

### The rest of the ATS checklist

| Check | Result |
|---|---|
| Text is real text, not an image | 536 words selectable |
| Reading order | every bullet follows its own employer, verified for 5 entries |
| Orphan bullet glyphs | none |
| Name | first line of the stream |
| Email, phone | present as plain text, regex-matchable |
| LinkedIn | spelled out as `linkedin.com/in/khan-abir`, not hidden behind anchor text |
| Section headers | `EDUCATION`, `WORK EXPERIENCE`, `EXTRACURRICULAR & LEADERSHIP`, `SKILLS & ADDITIONAL INFORMATION` all found |
| Fonts | all 5 embedded as subsets |
| Pages | 1 |
| Dates | `MM.YYYY` throughout |

`EXTRACURRICULAR` was added to the audit's list of required headers this pass; it
was rendering correctly but was not being checked.

### Metadata says only what the page says

The keyword field stamped by `scripts/finalise.py` used to carry `RWE Consulting`,
a term present nowhere on the page — flagged as an open item last pass, and fixed
here. **Every term in the metadata now also appears in the visible text.** An ATS
that indexes both finds the same words twice either way, and a candidate who
cannot see a term on their own CV cannot be asked about it in an interview.

## Rebuilding this repo produces a taller page than it used to

Worth knowing before you touch the content. The previously shipped PDFs render
text about **4.7% narrower than Liberation Serif's actual metrics** — whatever
laid them out was setting text narrow, and content tuned against that rendering
overflows when rebuilt here. That was fixed by trimming copy, not by shrinking
type: `--fs-base` is still 9.35 pt, so the page renders the same anywhere.

## The template

Formatting is matched to `Abir_H._Khan_CV_Lio.pdf`, measured out of that PDF with
PyMuPDF rather than eyeballed. Every value in `cv.html` carrying a mm or pt figure
is a number taken from it.

| | |
|---|---|
| Type | **Liberation Serif** — metrically identical to Times New Roman (what the source uses), SIL OFL, vendored in `assets/fonts/` so builds are reproducible offline |
| Navy | `#0c447c` — measured rgb(12,68,124); top bar, name, section headers and rules |
| Link | `#0563c1` — measured rgb(5,99,193), underlined |
| Structure | Bold **organisation** left / bold **location** right, then italic *role* left / italic *dates* right, then bullets |
| Bottom margin | `--pad-b: 10.5mm`. Not a matched value — the sources' ~14.5 mm of bottom white is a consequence of their shorter content, not a template parameter |
| Photo | `assets/photo.jpg`, **35 × 45 mm**, 900×1157 px (655 dpi at that size) |
| Sizing | One size for everything except the name |

### Measured against the source

| | Lio PDF | This CV |
|---|---|---|
| Text left edge | 19.06 mm | 19.06 mm |
| Bullet glyph | 21.89 mm | 21.89 mm |
| Bullet text | 25.41 mm | 25.41 mm |
| Additional-info value column | 50.81 mm | 50.81 mm |
| Name size / width | 17.04 pt / 60.14 mm | 17.04 pt / 60.07 mm |
| Photo top | 16.02 mm | 15.60 mm |
| Top bar | y 13.38 mm, 1.57 mm | y 13.23 mm, 1.59 mm |
| Body size | 9.48 pt | 9.35 pt — see below |

### Four deliberate differences

1. **Body type is 9.35 pt, not the source's 9.48 pt.** The source's design rule is
   one line per bullet. Our bullets are longer than its, and 9.35 pt is the
   largest size that preserves the rule. Don't raise it without re-running the
   build.
2. **The rules start at the text edge.** In the source they begin 0.46 mm to the
   left of the text — Word slop. Here all four section rules span exactly
   19.05–191.82 mm.
3. **The photo is flush right.** In the source it stops 3.44 mm short of the right
   text edge. Here its right edge sits on 191.82 mm with the rules and the
   right-aligned location/date column.
4. **The photo is 35 × 45 mm**, which is neither source's size — the two disagree
   (Lio 30.2 × 38.6, Strategy Consulting 37.7 × 47.1). 35 × 45 is the German
   *Bewerbungsfoto* standard, and its aspect (0.7778) is within 0.2% of the
   image's native 237/304 = 0.7796, so it crops clean.

One trap worth knowing: `h2` needs an explicit `font-size:1em`. Without it the
browser's default 1.5em heading size applies and the section headers render half
again too big — wrong for this template, where headers are body size.

## Where the source CVs disagree

The six PDFs in this repo contradict each other. This CV takes the majority
reading each time. Worth settling properly, because a recruiter comparing two of
your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova class rank** | top 15% (Allianz, both Accenture) vs top 10% (Siemens) | **top 10%** — confirmed |
| **Nova end date** | 12.2026 (four CVs) vs 01.2027 (DHL) | **12.2026** — confirmed |
| **German** | B1 (Allianz, both Accenture) vs Intermediate (Siemens) vs Basic (DHL) | **B1** |
| **SCAILE** | since 06.2026 (Allianz, both Accenture) vs 06.2026 – 08.2026 (Siemens) | **06.2026 – 08.2026** — confirmed |
| **Trariti location** | Mumbai (Siemens, Strategy, Allianz, DHL) vs Delhi (both Accenture) | **Mumbai** |
| **Trariti's third bullet** | *"a $10M+ revenue product"* (Allianz) vs *"$10M+ ARR product"* (both Accenture) vs *"$10M+ product"* (Siemens, Strategy) | **"$10M+ revenue product"** |

Two wording calls settled this pass:

- **A&M's plan is a *"$9.8M risk-mitigation plan"***, not a *"cost and
  risk-mitigation plan"*. Five of six source CVs say the former; only Accenture
  Strategy adds "cost". The last version carried the minority reading and the
  audit flagged it. The majority reading is also the one that matters here — this
  application is about risk.
- **"Prepared" creditor-negotiation presentations**, not "Advised C-level
  leadership on creditor-negotiation strategy". Three of four CVs say "prepared";
  preparing materials for leadership and advising leadership are different claims.

Also worth knowing: `Abir H. Khan_CV_Siemens Advanta.pdf` and
`Abir H. Khan_CV_Strategy Consulting.pdf` are **byte-identical** — two filenames,
one document.

## Final audit

`python3 scripts/audit.py`, run against the rendered PDF. All checks pass.

| Check | Result |
|---|---|
| Pages | 1 |
| Bullets wrapping | 0 of 20 |
| Bullet text edge | 25.41 mm on all 20, at character level |
| Left edges | 19.06 mm ×30, 21.89 mm ×20, 50.81 mm ×7 — exact |
| Right-aligned column | 16 location/date lines flush on 191.84 mm |
| Nothing crosses the right edge | widest line ends at 191.84 mm |
| Rules | all 4 section rules span 19.05–191.82 mm, identical |
| Photo right edge | 191.82 mm — on the rules |
| Bottom white | 12.40 mm |
| Em / en dashes | none |
| Non-ASCII inventory | only `•`, `’`, `×` — all intentional |
| Dates | `MM.YYYY` throughout |
| Placeholders | none |

Three things deliberately left alone:

- **A 12-month gap, 08.2024 to 07.2025.** The bachelor's ends 07.2024 and the
  master's begins 08.2025; nothing on the page covers between. Recruiters read
  timelines closely and will ask. Not fixable here — it needs a fact only the
  candidate has.
- **"Specialization"** is US spelling among British forms (Modelling, Organiser,
  prioritisation). It is the degree title as awarded by Shiv Nadar University and
  all six source CVs write it that way. Degree titles are quoted, not restyled.
- **The `×` in "MIT Sloan AI Club × TUM"** (U+00D7). A naive ATS could mangle it,
  but the keywords either side survive independently.

## Before sending

1. **Confirm the work-authorisation line.** The header carries *"No visa
   sponsorship required"* verbatim from the last CV, where it was written for
   Germany with the country deliberately dropped. **Luxembourg is a different
   jurisdiction**, and a German or Portuguese residence permit does not by itself
   carry the right to work there. If it does not hold for Luxembourg, change or
   remove the line before sending — this is the one claim on the page that a
   recruiter can check on day one.
2. **`Open to relocation to Luxembourg` is new.** It is implied by applying, and
   it removes the obvious objection to a Munich address on a Luxembourg posting.
   Remove it if the intention is to ask about remote or Munich-based work.
3. **If you have studied CRR, Solvency II, PRIIPs, UCITS or AIFMD, say so.**
   The posting names the first three explicitly as an asset, and they are absent
   from the page because no source CV evidences them. Adding two or three to the
   `Focus areas` row is the highest-value keyword edit available. There is 1.5 mm
   of headroom, so a third line in that row does not fit — a term would have to
   come out to make room.
4. **Same for VBA and MATLAB.** Named in the posting as a plus. The page claims
   Python, SQL and Power BI, which cover *"or other data analytics tools"*.
5. **The 12-month gap will come up.** Have the answer ready.
6. **French is not on the page.** The posting treats German and/or French as an
   advantage; German (B1) is there. Add French only if there is a real level to
   state.
7. **Back-port the corrections to the other five CVs.** Class rank is top 10%,
   SCAILE ended 08.2026, and Trariti's location is Mumbai; the Allianz and
   Accenture CVs still disagree on the first two. They also still carry "Eligible
   for visa sponsorship" rather than "No visa sponsorship required", and all of
   them still have the bullet paint-order defect described above.
