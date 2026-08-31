# CV — Hilti, International Finance Career / CFO Track

A one-page A4 CV, tailored to Hilti's finance entry routes after a referral
conversation with Timur (Hilti, CFO track), who offered to recommend the
candidate internally and asked for three things to forward to HR: the target
roles, the CV, and a short introduction message stating availability.

The page is tuned for the two postings that fit the profile:

- **Controller (m/f/d) – International Finance Career / CFO Track**, Kaufering
  (job 16066-en) — FP&A for the Central Europe hub: closings, rolling
  forecasts, cost controlling, business partnering; screens for a
  finance/controlling degree and internships or up to 3 years in corporate
  finance, audit or consulting; explicitly built to develop toward Group
  CFO-level roles via international assignments.
- **Outperformer – Global Management Development Program, Finance Track**,
  Germany-wide (job 19572-de) — 24-month rotational graduate program
  (12 months as Account Manager, finance projects at home and abroad, a
  Controlling & Reporting rotation in Kaufering); screens for a recent
  master's, 6–30 months of initial experience, ≥6 months international
  experience, fluent English plus another language, and global mobility.

Posting details were compiled from search results and Stepstone on
31.08.2026 — careers.hilti.group itself was unreachable from the build
environment — so **verify the live postings before sending**. The companion
`Hilti_Roles_Tracker.xlsx` in this repo carries the full role research, a
criterion-by-criterion fit map, and the caveats; it is a draft until the
candidate's own role list is pasted in.

Built on the same template as the other tailored CVs in this repo.
Work-experience copy is lifted from those CVs rather than rewritten, so the
same claims appear the same way everywhere.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> the files to actually send, then audits them
```

`npm run share` builds, runs `scripts/finalise.py` (needs `pymupdf`), then runs
`scripts/audit.py`. It writes two identical PDFs: `Abir_Hilal_Khan_CV.pdf` and
`Abir Hilal Khan_CV_Hilti.pdf`, the latter following this repo's naming
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

## This pass: risk reporting out, FP&A and mobility in

The previous pass targeted KPMG Luxembourg's risk-reporting practice. Every
entry, bullet and date is unchanged from it — the experience section already
carries exactly what a controlling track screens on — so this retune touched
only the four places where the page states its own target, and the line count
is untouched: the page still measures 295.5 mm.

| Change | Was (KPMG) | Is (Hilti) |
|---|---|---|
| Tagline, third clause | *fund diligence across a $170M pipeline* | *owned client KPI reporting and >$100k ARR at a Munich tech startup* |
| Tagline, first clause | *…, coursework in Risk Management* | coursework claim moved out; the Education bullet still carries it |
| Header status line | *Open to relocation to Luxembourg* | ***Internationally mobile*** — global mobility is a stated screen for both roles |
| Coursework bullet | leads with **Risk Management** | leads with **Corporate Finance**, same four courses reordered |
| Core skills | *Client Reporting* | *KPI Reporting* — the same SCAILE evidence, in the controlling register |
| Focus areas | VaR, Derivatives, Regulatory Reporting, Investment Funds, EU Financial Regulation… | FP&A, Controlling and Reporting, Forecasting, Cost Controlling, Business Partnering, Performance Management, International Finance |

`No visa sponsorship required` stays: it was written for Germany (the country
was deliberately dropped from the line two passes ago), and both target roles
are with Hilti Deutschland AG. If the target ever becomes HQ Schaan
(Liechtenstein), the line needs re-checking — that is a different jurisdiction.

## What this CV is optimised for

Each screening item from the two postings is mapped to a place on the page:

| What the postings ask for | Where it lands |
|---|---|
| **Business/econ degree, finance-controlling focus** | Education first; MSc Finance to 12.2026; bachelor's in Finance & Strategy |
| **Internships / up to 3 yrs (Controller); 6–30 months (Outperformer)** | ~19 months across A&M (7), Trariti (6), Biome (3), SCAILE (3) — inside both windows |
| **Corporate finance / audit / consulting background** | A&M restructuring (Fortune 500, U.S. Chapter 11); Trariti boutique strategy consulting |
| **Closings, rolling forecasts, cost controlling** | A&M scenario models and **EBITDA sensitivity analysis**; `Forecasting`, `Cost Controlling` in Focus areas |
| **Business partnering** | *"informing board-level decisions"*; creditor-negotiation presentations for client leadership; `Business Partnering` in Focus areas |
| **Reporting and performance management** | *"Automated weekly client KPI reporting … 60%"*; KPI dashboards; `KPI Reporting`, `Performance Management` |
| **Stakeholder management, conceptual strength** | *"Led 90+ stakeholder interviews"*; scenario models for a $9.8M plan |
| **≥6 months international experience (Outperformer)** | India → Portugal → Germany across the page; European Commission thesis |
| **Global mobility** | *Internationally mobile* in the header |
| **Fluent English + one other language (Outperformer)** | English, Hindi, Bengali fluent; German B1; Portuguese basic |
| **Customer-facing year as Account Manager (Outperformer)** | *"Owned North American clients as their first point of contact, signing and onboarding >$100k ARR"* |
| **Leadership potential** | Team Lead, Draycott PE Challenge; hackathon organiser; UN Foundation |
| **Analytics tooling** | Advanced Excel leads Technical; Power BI, SQL, Python, Generative AI |

Two choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students, and both
  postings gate on the degree.
- **Photo included.** Normal practice for a German employer (35 × 45 mm
  Bewerbungsfoto). It is a separate element a parser skips — the five-parser
  check below runs against the file as shipped, photo and all. To remove it,
  delete the `<img class="photo">` line; everything reflows.

## Where the FP&A vocabulary comes from

The rule is the repo's existing one: **a keyword goes on the page only if
something on the page backs it.** The skills grid stays split in two.

`Core skills` are demonstrated by an entry above them:

| Term | Backed by |
|---|---|
| Financial Modelling | A&M scenario models, Biome build-ups, Trariti models |
| Scenario and Sensitivity Analysis | A&M: scenario models, EBITDA sensitivity |
| Data Analysis | Biome's 3,000+ company screen, SCAILE KPI reporting |
| Commercial Due Diligence | Biome |
| KPI Reporting | SCAILE's weekly client KPI reporting and dashboards |
| Process Automation | SCAILE's AI agent workflows, 60% manual effort cut |
| Stakeholder Management | Trariti's 90+ stakeholder interviews |
| Problem Solving | Top 3 of 15,000 nationally; Draycott Team Lead |

`Focus areas` are the target domain, in the postings' own words — FP&A,
Controlling and Reporting, Forecasting, Cost Controlling, Business Partnering,
Performance Management, International Finance. Labelling them *focus areas*
rather than *skills* is deliberate and is the source CVs' own register: the
scenario and sensitivity work (A&M), the KPI reporting and dashboards (SCAILE)
and the board-level and client-leadership exposure are real evidence of the
domain, but a 7-month restructuring internship is not a controlling job, and
the honest label keeps every interview answer safe.

**What is deliberately not claimed:** SAP (the ERP a Hilti controller will
live in), IFRS/HGB accounting standards, VBA, and any German level above B1.
Nothing in any source CV evidences them. See *Before sending* — SAP and German
are the two highest-value edits available if the facts support them.

## Written for the ATS

Hilti recruits through an applicant-tracking system (SmartRecruiters-family
careers site), so the parse is the first round. `scripts/audit.py` checks the
claims below against the **rendered PDF**, not the source, and exits non-zero
on any failure.

### The bullets used to detach from their employers

The biggest find in this repo's ATS work, and it was invisible on the page. The
old CSS gave every `li` a `position:relative` so the bullet glyph could be
absolutely positioned. Positioned elements paint in a later phase than
normal-flow content, so Chromium emitted **every bullet after the rest of the
page** in the PDF's text stream. A parser that reads that stream in order saw
every achievement orphaned at the end of the document, detached from the
employer it belongs to. The fix is a hanging indent built from normal flow —
`text-indent` plus an inline-block `::before` marker. Document order is
preserved and the geometry is unchanged: glyph at 21.89 mm, bullet text at
**exactly 25.41 mm** on all 20 bullets, verified at character level.

### Five parsers, re-run on this version

Extraction was re-run on the shipped Hilti file. The check asserts the eight
organisations appear in page order, that the email, phone and LinkedIn fields
extract as plain text, and that a leading bullet from each of five entries
falls between its own employer and the next one.

| Extraction mode | Reading order | Email | Phone | LinkedIn | Bullets attached |
|---|---|---|---|---|---|
| PyMuPDF `get_text()` — stream order | OK | ✓ | ✓ | ✓ | ✓ |
| PyMuPDF `get_text(sort=True)` | OK | ✓ | ✓ | ✓ | ✓ |
| pypdf `extract_text()` | OK | ✓ | ✓ | ✓ | ✓ |
| pdfminer.six, default layout analysis | OK | ✓ | ✓ | ✓ | ✓ |
| pdfminer.six, `laparams=None` | OK | ✓ | ✓ | ✓ | ✓ |

Stream order is the mode that matters most: Apache PDFBox, which underpins Tika
and a lot of enterprise résumé parsing, has `sortByPosition` **off** by default.

### The rest of the ATS checklist

| Check | Result |
|---|---|
| Text is real text, not an image | 532 words selectable |
| Reading order | every bullet follows its own employer, verified for 5 entries |
| Orphan bullet glyphs | none |
| Name | first line of the stream |
| Email, phone | present as plain text, regex-matchable |
| LinkedIn | spelled out as `linkedin.com/in/khan-abir`, not hidden behind anchor text |
| Section headers | `EDUCATION`, `WORK EXPERIENCE`, `EXTRACURRICULAR & LEADERSHIP`, `SKILLS & ADDITIONAL INFORMATION` all found |
| Fonts | all 5 embedded as subsets |
| Pages | 1 |
| Dates | `MM.YYYY` throughout |

### Metadata says only what the page says

**Every term in the metadata also appears in the visible text** — the keyword
field now carries the FP&A vocabulary (Financial Planning & Analysis, FP&A,
Controlling, Forecasting, Cost Controlling, Business Partnering, Performance
Management, KPI Reporting, …) and each term is on the page. An ATS that indexes
both finds the same words twice either way, and a candidate who cannot see a
term on their own CV cannot be asked about it in an interview.

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
| Body size | 9.48 pt | 9.35 pt — the largest size that keeps every bullet on one line, the source's own design rule |

One trap worth knowing: `h2` needs an explicit `font-size:1em`. Without it the
browser's default heading size applies and the section headers render half
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

Also worth knowing: `Abir H. Khan_CV_Siemens Advanta.pdf` and
`Abir H. Khan_CV_Strategy Consulting.pdf` are **byte-identical** — two
filenames, one document.

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
- **"Specialization"** is US spelling among British forms. It is the degree
  title as awarded by Shiv Nadar University and all six source CVs write it
  that way. Degree titles are quoted, not restyled.
- **The `×` in "MIT Sloan AI Club × TUM"** (U+00D7). A naive ATS could mangle
  it, but the keywords either side survive independently.

## Before sending

1. **Verify both live postings.** Every posting detail in this README and in
   `Hilti_Roles_Tracker.xlsx` came from search results and Stepstone on
   31.08.2026 because careers.hilti.group was unreachable from the build
   environment. Job IDs, titles and requirements must be confirmed on the live
   site — or with Timur — first.
2. **Confirm which route Timur means by "CFO track"** — the Kaufering
   Controller entry role or the Outperformer Finance Track — and let his answer
   set the order of the roles list he forwards.
3. **Pin down availability before the intro message is drafted.** The MSc runs
   to 12.2026, so full-time availability is presumably 01.2027 — confirm the
   exact date, whether the thesis allows an earlier start, and note that the
   Outperformer intake dates are fixed (check the next intake).
4. **If you have SAP exposure, say so.** A Hilti controller lives in SAP and
   no source CV evidences it. One term in the Technical row is the
   highest-value keyword edit available — the page has 1.5 mm of headroom, so
   something must come out to make room.
5. **If your German is now better than B1, update the Languages row.** German
   is the working language around the DACH business the Controller role
   partners with, and the Outperformer sales year is customer-facing in German.
6. **The 12-month gap will come up.** Have the answer ready.
7. **Back-port the corrections to the other five CVs.** Class rank is top 10%,
   SCAILE ended 08.2026, and Trariti's location is Mumbai; the Allianz and
   Accenture CVs still disagree on the first two. They also still carry
   "Eligible for visa sponsorship" rather than "No visa sponsorship required",
   and all of them still have the bullet paint-order defect described above.
