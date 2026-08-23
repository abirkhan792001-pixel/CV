# CV — Deloitte Luxembourg, Analyst: Financial Risk Management

A one-page A4 CV, tailored to Deloitte Luxembourg's **Analyst — Financial Risk
Management**, posted 20.08.2026. The role sits in Deloitte's Risk & Regulatory
practice, which delivers risk and capital management services to banks and
(alternative) investment funds: risk modelling and model validation, CRR/CRD IV
and IFRS 9 compliance work, and regulatory reporting (COREP, FINREP). Seniority
is Junior; the posting asks for a *first* experience in financial risk
management and modelling.

Built on the same template as the other tailored CVs in this repo.
Work-experience copy is lifted from those CVs rather than rewritten, so the same
claims appear the same way everywhere.

> **Two must-haves are not on the page: French and VBA.** Both are listed by
> Deloitte under *Must have*, and neither is evidenced by any of the six source
> CVs, so neither was invented here. See *Before sending* — these are the first
> two things to fix if the candidate actually has them.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> the files to actually send, then audits them
```

`npm run share` builds, runs `scripts/finalise.py` (needs `pymupdf`), then runs
`scripts/audit.py`. It writes two identical PDFs: `Abir_Hilal_Khan_CV.pdf` and
`Abir Hilal Khan_CV_Deloitte Luxembourg.pdf`, the latter following this repo's
naming convention for a tailored copy.

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
  Every keyword stamped there also appears on the page — now enforced, see
  *Metadata says only what the page says* below.
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

## This pass: from fund reporting to bank risk modelling

The previous target was KPMG's *Risk Reporting for Investment Funds*. Deloitte's
posting is a different animal in the same practice area, and the difference
drove every edit here:

|  | KPMG (last pass) | Deloitte (this pass) |
|---|---|---|
| Client base | investment funds and asset managers | **banks** and investment funds |
| Core activity | preparing and reviewing risk reports | **modelling and validating risk models** |
| Named risks | portfolio risk, VaR, derivatives | **credit, liquidity, market, climate, IRRBB** |
| Named regulation | UCITS/AIFMD-adjacent, general EU | **CRR/CRD IV, IFRS 9, COREP, FINREP** |
| Named languages | English; German/French an advantage | **French *and* English fluent — must have** |

**No structural change was made.** The entries, their order, the photo and the
section layout are as they were; the page was already the right shape for a
junior risk role. What changed is vocabulary and emphasis, at a constant line
count — the page is still 295.5 mm.

### The eight edits

| # | Where | Change | Why |
|---|---|---|---|
| 1 | Tagline | *"scenario and sensitivity modelling … fund diligence across a $170M pipeline"* → *"**credit and liquidity** scenario modelling … **>$100M** in distressed debt exposure"* | The posting names credit and liquidity first. The fund-pipeline claim is still on the page, in the Biome entry |
| 2 | A&M bullet 2 | *"across liquidity and supplier scenarios to test operational resilience"* → *"across **liquidity** and supplier **stress scenarios** to test resilience"* | Puts *stress* on the page, where the underlying work is stress testing in substance. Two words traded out to hold the one-line rule |
| 3 | A&M bullet 4 | *creditor-negotiation* set in bold | The only occurrence of "credit" in the work section; bold makes it survive a six-second skim |
| 4 | Biome bullet 1 | *"Evaluated 3,000+ companies"* → *"**Screened** 3,000+ companies"* | Deloitte asks for *"excellent data mining skills"*. Screening 3,000 companies is data mining; evaluating them is not, quite |
| 5 | Core skills | *Data Analysis* → **Data Mining and Analysis**; *Financial Modelling* → **Financial and Risk Modelling**; **Stress Testing** added; *Commercial Due Diligence* removed | Three of the posting's own terms in, one corporate-finance term out |
| 6 | Focus areas | Rebuilt: **Credit Risk, Liquidity Risk, Market Risk**, VaR, Regulatory Reporting, **Banking and** Investment Funds, EU Financial Regulation, **Climate and Sustainable Finance** | *Risk Management*, *Derivatives*, *Portfolio Risk Monitoring* and *Asset Management* were the fund-monitoring set; the four named risk types replace them |
| 7 | Technical | **Word** added | Named explicitly in the posting's must-have tooling line |
| 8 | `finalise.py` | Keyword field rebuilt around the new terms | Metadata tracks the page |

**Dropping *Commercial Due Diligence* from the skills row costs nothing.** The
phrase still appears verbatim in the Biome bullet — *"Built commercial due
diligence models…"* — so an ATS searching for it still matches. The skills row
is the scarce space; the bullet is not.

### The line arithmetic

Every row had to stay at its existing line count, because there is no fourth
line available anywhere:

| Row | Before | After | Lines | Slack left |
|---|---|---|---|---|
| Tagline | 168 ch | 170 ch | 2, unchanged | — |
| Core skills | 168 ch | 184 ch | 2, unchanged | 18.4 mm (~13 ch) |
| Focus areas | 161 ch | 171 ch | 2, unchanged | 38.2 mm (~27 ch) |
| Languages | 94 ch | 94 ch | 1, unchanged | 14.5 mm (~10 ch) |
| Technical | 89 ch | 96 ch | 1, unchanged | **5.3 mm (~4 ch)** |

Technical is the tight one: adding *Word* leaves 5.3 mm, about four characters.
Anything further on that row wraps it and costs a line the page does not have —
which is exactly what happens if you add VBA naively. See *Before sending*, where
each remaining edit is given as a **tested swap** rather than an estimate.

## What this CV is optimised for

Deloitte's posting screens on a list. Each item is mapped to a place on the page:

| What the posting asks for | Where it lands |
|---|---|
| **Master's in business administration, quantitative finance, engineering, econometrics** | Education first, MSc Finance to 12.2026; BMS Finance & Strategy |
| **First experience in financial risk management and modelling (credit, liquidity, IRRBB)** | A&M: scenario models for a $9.8M risk-mitigation plan, EBITDA sensitivity across liquidity stress scenarios, >$100M in debt under Chapter 11 |
| **Excellent analytical and logical problem-solving** | Top 3 of 15,000 nationally; Magna Cum Laude; top 10% at Nova |
| **Rigorous, quality driven, result-oriented, excellent data mining** | Biome's 3,000+ company screen; `Data Mining and Analysis` |
| **Strong interpersonal and communication skills** | *"Led 90+ stakeholder interviews"*; *"Owned North American clients as their first point of contact"*; A&M's creditor-negotiation materials |
| **Report writing, analysis and presentation of results to clients** | A&M's presentations for client leadership; SCAILE's weekly client reporting and KPI dashboards; `Client Reporting` |
| **Modelling and independent review of risk models** | A&M scenario models; Trariti data-driven models; Biome's commercial due diligence models |
| **Regulatory Reporting (COREP, FINREP)** | `Regulatory Reporting` in Focus areas — see the honesty note below |
| **Climate risk** | European Commission thesis on EU renewable-energy funding; `Climate and Sustainable Finance` |
| **Strong command of Excel, Word, PowerPoint** | `Advanced Microsoft Excel` leads the Technical row, with PowerPoint and Word |
| **Coding skills (Python, SQL, SAS, R) — an asset** | Python, SQL, Power BI; *Introduction to Python* in Nova coursework |
| **Banking industry knowledge — a plus** | A&M restructuring (creditors, distressed debt, Chapter 11); `Banking and Investment Funds` |
| **German — an asset** | Languages row, German (B1, improving) |
| **Fluent French and English — must have** | **English only.** See *Before sending* |
| **VBA — must have** | **Not claimed.** See *Before sending* |

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
| Financial and Risk Modelling | A&M scenario models for a risk-mitigation plan; Biome build-ups; Trariti models |
| Scenario and Sensitivity Analysis | A&M: scenario models, EBITDA sensitivity |
| Stress Testing | A&M: liquidity and supplier stress scenarios, tested for resilience |
| Data Mining and Analysis | Biome's 3,000+ company screen; SCAILE KPI reporting |
| Client Reporting | SCAILE's weekly client reporting and dashboards; A&M's presentations for client leadership |
| Process Automation | SCAILE's AI agent workflows, 60% manual effort cut |
| Stakeholder Management | Trariti's 90+ stakeholder interviews |
| Problem Solving | Top 3 of 15,000 nationally; Draycott Team Lead |

`Focus areas` are the target domain — Credit Risk, Liquidity Risk, Market Risk,
Value at Risk (VaR), Regulatory Reporting, Banking and Investment Funds, EU
Financial Regulation, Climate and Sustainable Finance. Labelling them *focus
areas* rather than *skills* is deliberate and is the source CVs' own label: VaR
and market risk are coursework, EU regulation and the climate line are the
thesis, and the banking exposure is A&M rather than a bank. It is the honest
register for a Junior posting that asks for a *first* experience.

**What is deliberately not claimed:** CRR/CRD IV, IFRS 9, COREP, FINREP, IRRBB,
Basel, model validation, VBA, SAS, R and French. Deloitte names CRR/CRD IV and
IFRS 9 under *Nice to have* and VBA and French under *Must have*; nothing in any
source CV evidences any of them. Asserting *Model Validation* was specifically
rejected — the posting means formal independent validation of a bank's risk
models, and no entry on the page is that. See *Before sending*.

## Written for the ATS

Deloitte Luxembourg recruits through an applicant-tracking system, so the parse
is the first round. `scripts/audit.py` checks the claims below against the
**rendered PDF**, not the source, and exits non-zero on any failure.

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

| Extraction mode | Reading order | Bullets with employer | Email | Phone | LinkedIn |
|---|---|---|---|---|---|
| PyMuPDF `get_text()` — stream order | OK | OK | ✓ | ✓ | ✓ |
| PyMuPDF `get_text(sort=True)` | OK | OK | ✓ | ✓ | ✓ |
| pypdf `extract_text()` | OK | OK | ✓ | ✓ | ✓ |
| pdfminer.six, default layout analysis | OK | OK | ✓ | ✓ | ✓ |
| pdfminer.six, `laparams=None` | OK | OK | ✓ | ✓ | ✓ |

Stream order is the mode that matters most: Apache PDFBox, which underpins Tika
and a lot of enterprise résumé parsing, has `sortByPosition` **off** by default.

### The rest of the ATS checklist

| Check | Result |
|---|---|
| Text is real text, not an image | 543 words selectable |
| Reading order | every bullet follows its own employer, verified for 5 entries |
| Orphan bullet glyphs | none |
| Name | first line of the stream |
| Email, phone | present as plain text, regex-matchable |
| LinkedIn | spelled out as `linkedin.com/in/khan-abir`, not hidden behind anchor text |
| Section headers | `EDUCATION`, `WORK EXPERIENCE`, `EXTRACURRICULAR & LEADERSHIP`, `SKILLS & ADDITIONAL INFORMATION` all found |
| Metadata keywords | all 25 also appear in the visible text |
| Fonts | all 5 embedded as subsets |
| Pages | 1 |
| Dates | `MM.YYYY` throughout |

### Metadata says only what the page says

The rule was stated last pass but nothing enforced it, and this pass it caught
three violations on the first run: the keyword field carried `Financial Risk
Management`, `Scenario Analysis` and `Advanced Excel`, none of which appear
verbatim on the page — which reads as *Risk Management*, *Scenario and
Sensitivity Analysis* and *Advanced Microsoft Excel*. All three were corrected to
the page's own wording.

`scripts/audit.py` now asserts it: **every comma-separated term in the PDF's
keyword field must appear in the visible text**, and the audit fails if one does
not. An ATS that indexes both finds the same words twice either way, and a
candidate who cannot see a term on their own CV cannot be asked about it in an
interview.

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
| **A&M's plan** | *"$9.8M risk-mitigation plan"* (five of six) vs *"cost and risk-mitigation plan"* (Accenture Strategy) | **"risk-mitigation plan"** — the majority reading, and the one that matters for a risk role |
| **A&M's creditor work** | *"prepared"* (three of four) vs *"advised C-level leadership on strategy"* | **"prepared"** — preparing material for leadership and advising leadership are different claims |

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
| Metadata keywords visible on the page | 25 of 25 |
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

The first two items are Deloitte *must-haves* that this CV cannot satisfy from
the source material. They are ordered by how much they change the application.

Each of the first three was **built and measured**, not estimated. The page has
1.5 mm of headroom, so a naive insertion wraps a row and pushes the CV to two
pages: adding `French (B2)` and `VBA` as straight additions takes it to 303.8 mm.
The swaps below were tested and all hold the page at **295.5 mm**.

1. **French — the one that decides the application.** The posting says *"Be
   fluent in French and English"* under **Must have**, and Luxembourg means it:
   French is a working language of the country and of Deloitte's local client
   base. **No source CV mentions French at all**, so none was invented here.
   If there is a real level, make this swap in the Languages row — drop
   `Portuguese (Basic)`, which is the least useful entry for a Luxembourg role:

   ```
   English (Fluent), French (B2), German (B1, improving), Hindi (Fluent), Bengali (Fluent)
   ```

   Tested: 295.5 mm, one line, still fits. If there is genuinely no French, this
   application is a stretch on a stated must-have — better to say so directly in
   the cover letter than to let the CV imply otherwise.
2. **VBA.** Named in the same must-have line as Excel, Word and PowerPoint, and
   not claimed because nothing evidences it. Adding it alone wraps the Technical
   row, which has only ~4 characters of slack. Trade `Data Analytics` for it —
   a generic umbrella term for a named must-have:

   ```
   Advanced Microsoft Excel, VBA, PowerPoint, Word, Power BI, SQL, Python, Generative AI
   ```

   Tested: 295.5 mm, one line, still fits.
3. **CRR/CRD IV and IFRS 9.** Named under *Nice to have*. These are the one edit
   that needs **no** trade — `Focus areas` has 38 mm of slack on its second line:

   ```
   Credit Risk, Liquidity Risk, Market Risk, CRR/CRD IV, IFRS 9, Value at Risk (VaR), ...
   ```

   Tested: 295.5 mm, still two lines, 5.8 mm to spare. Add either or both only if
   they were genuinely covered in the Nova Risk Management course.
4. **SAS and R.** Also *nice to have*. Python and SQL are on the page and cover
   the posting's *"or other data analytics tools"* intent; add SAS or R only if
   real, and note the Technical row is the tightest line on the page — each needs
   a trade like VBA's.
5. **Confirm the work-authorisation line.** The header carries *"No visa
   sponsorship required"*, written originally for Germany with the country
   deliberately dropped. **Luxembourg is a different jurisdiction**, and a German
   or Portuguese residence permit does not by itself carry the right to work
   there. If it does not hold for Luxembourg, change or remove the line before
   sending — this is the one claim on the page a recruiter can check on day one.
6. **`Open to relocation to Luxembourg`** is implied by applying and removes the
   obvious objection to a Munich address. Remove it only if the intention is to
   ask about remote or Munich-based work.
7. **The 12-month gap will come up.** 08.2024 to 07.2025. Have the answer ready.
8. **Back-port the corrections to the other five CVs.** Class rank is top 10%,
   SCAILE ended 08.2026, and Trariti's location is Mumbai; the Allianz and
   Accenture CVs still disagree on the first two. They also still carry "Eligible
   for visa sponsorship" rather than "No visa sponsorship required", and all of
   them still have the bullet paint-order defect described above.
