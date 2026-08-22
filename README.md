# CV — RWE Consulting Careers Day, October 2026

A one-page A4 CV, tailored to the **RWE Consulting Careers Day** on 29 October
2026 in Essen (recruitment code 92869, applications close **11.09.2026**,
invitations go out by 25 September). RWE Consulting is the RWE Group's in-house
consultancy, working alongside Corporate Strategy and Sustainability.

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
`Abir Hilal Khan_CV_RWE Consulting.pdf`, the latter following this repo's naming
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

Current state: **296.8 mm of 297 mm, one page, 0.2 mm headroom.** The page is
full. Anything added from here has to be traded against something already on it.

## Written for the ATS

RWE recruits through SAP SuccessFactors, and the posting asks only for a CV with
full contact details, so the parse is the whole first round. `scripts/audit.py`
checks the claims below against the **rendered PDF**, not the source, and exits
non-zero on any failure.

### The bullets used to detach from their employers

The biggest find in this pass, and it was invisible on the page. The old CSS gave
every `li` a `position:relative` so the bullet glyph could be absolutely
positioned. Positioned elements paint in a later phase than normal-flow content,
so Chromium emitted **every bullet after the rest of the page** in the PDF's text
stream. A parser that reads that stream in order saw this:

```
...
Interests
Distance running, swimming, hiking, baking
Ranked top 10% of the class
•
Master's Thesis in partnership with the European Commission ...
•
```

Every achievement orphaned at the end of the document, detached from the employer
it belongs to, each followed by a stray `•` on its own line. Nothing could be
attributed to A&M, to Biome, or to any date range.

Which parsers this actually hit, measured on the old file and the new one:

| Extraction mode | Old file | New file |
|---|---|---|
| PyMuPDF `get_text()` — stream order | **broken**, 0/4 entries intact | OK |
| pypdf `extract_text()` | **broken**, 0/4 | OK |
| PyMuPDF `get_text(sort=True)` | OK | OK |
| pdfminer.six, default layout analysis | OK | OK |
| pdfminer.six, `laparams=None` | OK | OK |

So it was not universal: parsers that sort by position recovered, parsers that
trust stream order did not. That is not a safe bet to take — Apache PDFBox, which
underpins Tika and a lot of enterprise résumé parsing, has `sortByPosition` **off**
by default, which is exactly the broken mode.

The fix is a hanging indent built from normal flow — `text-indent` plus an
inline-block `::before` marker — instead of a positioned one. Document order is
preserved, so all five modes above now agree, and the geometry is unchanged: the
glyph still sits at 21.89 mm and the bullet text still starts at **exactly
25.41 mm** on all 20 bullets, verified at character level.

### The rest of the ATS checklist

| Check | Result |
|---|---|
| Text is real text, not an image | 518 words selectable |
| Reading order | every bullet follows its own employer, verified for 4 entries |
| Orphan bullet glyphs | none |
| Name | first line of the stream |
| Email, phone | present as plain text, regex-matchable |
| LinkedIn | **spelled out as `linkedin.com/in/khan-abir`** — see below |
| Section headers | `EDUCATION`, `WORK EXPERIENCE`, `SKILLS …` all found |
| Fonts | all 5 embedded as subsets |
| Pages | 1 |
| Dates | `MM.YYYY` throughout |

Two smaller changes came out of the same review:

- **The LinkedIn link now shows its URL.** It used to be an anchor reading
  "LinkedIn" — a parser captures visible text, not the `href`, so the profile was
  being dropped. Spelling it out ran the contact line 0.39 mm past the text
  column, paid for by narrowing the header's photo gap from 8 mm to 6.5 mm. That
  gap is not one of the template's measured values; the `.sep` margin is, so it
  was left alone.
- **`ADDITIONAL INFORMATION` is now `SKILLS & ADDITIONAL INFORMATION`.** Parsers
  segment a document on recognised headers and populate a skills field from a
  section named for it. The old header carried a `Core skills` label inside the
  section but nothing in the header itself. Costs nothing.

The layout was already sound in the other respects: the photo is a separate
element an ATS skips, and the two-column header is the same one the other five
CVs use.

## Rebuilding this repo produces a taller page than it used to

Worth knowing before you touch the content. The previously shipped PDF renders
text about **4.7% narrower than Liberation Serif's actual metrics**. Measured on
one line, `Ranked top 10% of the class`:

| | Width at 9.345 pt |
|---|---|
| Liberation Serif metrics (computed from the vendored woff2) | 109.265 pt |
| Rebuild here | 109.214 pt |
| Previously shipped `Abir_Hilal_Khan_CV.pdf` | 104.135 pt |

The rebuild matches the font. The old file does not, so whatever rendered it was
laying text out narrow. The content had been tuned against that narrow rendering,
which is why a clean rebuild of the committed HTML came out at **309.3 mm** — 12.3 mm
over A4, with the tagline, two bullets and the skills row all wrapping a line further
than intended.

That was fixed by trimming copy, not by shrinking type: `--fs-base` is still
9.35 pt. The page now fits at correct font metrics, so it will render the same
anywhere.

## What this CV is optimised for

RWE's posting screens on a short list. Each item is mapped to a place on the page:

| What RWE asks for | Where it lands |
|---|---|
| **Registered Master/MBA/PhD student or graduate** | Education first, MSc Finance to 12.2026 |
| **Interested in renewable energy and sustainability** | Commission thesis (lead bullet), founder venture, Biome's energy-transition thesis, tagline |
| **Enthusiastic about solving complex problems** | Top 3 of 15,000 in a national case challenge, Draycott Team Lead, A&M scenario modelling |
| **…in a motivated and diverse team** | Hack-Nation across 60+ countries, UN Foundation, four countries of study and work |
| **Business fluent in English** | First row of Skills, in the posting's own words |
| Consulting fit (the day is a case study) | A&M, Impact Consulting, SCAILE advisory, Biome diligence |
| Based in Germany, no relocation friction | Munich in the contact line, "No visa sponsorship required" |

Two choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  graduates, and RWE gates on being a registered student or recent graduate.
- **Photo included.** All the source CVs except DHL carry one, and RWE is a German
  employer, where the photo CV is still the convention.

## The tailoring moves, from the E.ON version

- **The tagline leads with the Commission thesis.** It used to open on A&M and
  turnaround strategy. RWE's first screen is interest in renewable energy, so the
  strongest renewables evidence on the page goes into the first sentence a
  recruiter reads. `Fortune 500 restructuring at A&M` keeps the consulting
  credential in the same two lines.
- **The Master's Thesis is now Nova's first bullet**, ahead of class rank. Same
  reasoning: it is the one item on the page that is both energy-specific and work
  only this candidate did. It was also shortened from *"in partnership with the
  European Commission"* to *"with the European Commission"* to hold one line.
- **`Energy Transition`, `Renewable Energy` and `Sustainability` are in Core
  skills.** The E.ON version deliberately cut a keyword row on the grounds that it
  asserted what the entries already demonstrated. That reasoning held for a row of
  four unevidenced terms; it does not hold here, because RWE's posting screens on
  these exact words and each one is backed by an entry on the page — the thesis,
  the founder venture's German energy regulation work, and Biome's
  energy-transition thesis.
- **`Data Analysis`, `Problem Solving`, `Project Management` and `Stakeholder
  Management` are all present.** These four are RWE Consulting's own published
  vocabulary. `Data Analysis` had been cut for E.ON to hold the row at two lines;
  it is back.
- **`Commercial and Financial Due Diligence`, `Business Case Development` and
  `Digital Transformation` came out** to pay for the above. The row is a fixed
  two-line budget and the RWE-specific terms outrank them. Diligence is still
  demonstrated in the Biome entry.
- **`Generative AI` moved to the Technical row**, keeping the keyword without
  spending a Core-skills line. `Claude Code` came out of that row — it was the
  least load-bearing term and the only one forcing a second line.
- **English is now "Business Fluent"**, matching the posting's phrasing. German
  stays at B1: this posting does not ask for German, unlike E.ON's.
- **The founder's third bullet dropped "applying to Antler"** to hold one line.
  Still present tense (*"Building…"*, *"in early talks with…"*), which is accurate
  for a venture still in research.

Everything else is unchanged: TCG is out, Impact Consulting is in, Biome's ESG
line leads its entry, and the coursework list stays replaced by the thesis.

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
| Bottom margin | `--pad-b: 10.5mm`, reduced from 12 mm to fit the third founder bullet. Not a matched value — the sources' ~14.5 mm of bottom white is a consequence of their shorter content, not a template parameter |
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
| Name top | 22.58 mm | 22.42 mm — CSS box top; the glyph top measures 25.32 mm in both |
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

`Abir H. Khan_CV_Strategy Consulting.pdf` is the same template as Lio — every text
metric agrees within 0.03 mm — and **its rules sit exactly on its own text edges**,
which is what confirms Lio's 0.46 mm offset is slop rather than intent.

One trap worth knowing: `h2` needs an explicit `font-size:1em`. Without it the
browser's default 1.5em heading size applies and the section headers render half
again too big — wrong for this template, where headers are body size.

### No photo, if you'd rather

Delete the `<img class="photo">` line in `cv.html`. Everything else reflows — the
header is a flex row and the left column already sets its own width.

## Where the source CVs disagree

The six PDFs in this repo contradict each other in four places. This CV takes the
majority reading each time. Worth settling properly, because a recruiter comparing
two of your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova class rank** | top 15% (Allianz, both Accenture) vs top 10% (Siemens) | **top 10%** — confirmed |
| **Nova end date** | 12.2026 (four CVs) vs 01.2027 (DHL) | **12.2026** — confirmed |
| **German** | B1 (Allianz, both Accenture) vs Intermediate (Siemens) vs Basic (DHL) | **B1** |
| **SCAILE** | since 06.2026 (Allianz, both Accenture) vs 06.2026 – 08.2026 (Siemens) | **06.2026 – 08.2026** — confirmed |

Because SCAILE is a closed role now, its bullets are past tense ("Advised",
"Built and shipped"), matching how the Siemens CV — the other one that dates it to
08.2026 — writes them.

One more, a wording difference rather than a fact: three CVs say *"Prepared
creditor-negotiation presentations for client leadership"*; Accenture Strategy
escalates it to *"Advised C-level client leadership on creditor-negotiation
strategy"*. This CV uses **"Prepared"** — preparing materials for leadership and
advising leadership are different claims, and the first is what three of four CVs
commit to.

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
| Left edges | 19.06 mm ×31, 21.89 mm ×20, 50.81 mm ×5 — exact |
| Right-aligned column | 18 location/date lines flush on 191.84 mm |
| Nothing crosses the right edge | widest line ends at 191.84 mm |
| Rules | all 4 section rules span 19.05–191.82 mm, identical |
| Photo right edge | 191.82 mm — on the rules |
| Bottom white | 11.34 mm |
| Em / en dashes | none |
| Non-ASCII inventory | only `•`, `’`, `×`, `€` — all intentional |
| Dates | `MM.YYYY` throughout |
| Placeholders | none |

Three things deliberately left alone:

- **A 12-month gap, 08.2024 to 07.2025.** The bachelor's ends 07.2024 and the
  master's begins 08.2025; nothing on the page covers between. German recruiters
  read timelines closely and will ask. Not fixable here — it needs a fact only the
  candidate has.
- **"Specialization"** is US spelling among British forms (Modelling, Organiser).
  It is the degree title as awarded by Shiv Nadar University and all six source
  CVs write it that way. Degree titles are quoted, not restyled.
- **The `×` in "MIT Sloan AI Club × TUM"** (U+00D7). A naive ATS could mangle it,
  but the keywords either side survive independently.

## Open items the audit surfaced

Neither is a defect; both are judgement calls that belong to the candidate.

- **Nothing on the page demonstrates stakeholder management.** It is one of the
  four skills RWE Consulting publishes, and it currently appears only as a term in
  the Core skills row. The evidence exists — *"Led 90+ stakeholder interviews,
  turning insights into recommendations for a $10M+ revenue product"* is in all six
  source CVs — but it belongs to the TCG entry, which was cut on brief. Reinstating
  it costs about 14.6 mm on a page with 0.2 mm spare, so something else would have
  to come out.
- **The A&M scenario bullet takes a minority wording.** Five of six source CVs say
  *"a $9.8M risk-mitigation plan"*; only Accenture Strategy says *"a $9.8M cost and
  risk-mitigation plan"*, which is what this CV carries. The repo's rule elsewhere
  is to take the majority reading. Left as-is rather than changed silently, since
  both wordings are the candidate's own.

## Before sending

1. **"Full contact details" may mean a postal address.** The posting asks for a CV
   with full contact details; the header carries city, phone, email and LinkedIn
   but no street address. German applications often include one. Add it to the
   contact line if you want it there — it will need a line-fit check, since the
   line is currently 0.6 mm inside the column.
2. **The 12-month gap will come up.** Have the answer ready; it is the first thing
   a German recruiter will notice on the timeline.
3. **`RWE Consulting` sits in the PDF keyword metadata but nowhere on the page.**
   Harmless — it is an application to RWE — but it is a term present only for
   matching. Drop it from `scripts/finalise.py` if you would rather the metadata
   only restate what a reader can see.
4. **Deadline 11.09.2026, recruitment code 92869.** Invitations go out by
   25 September for the 29 October event in Essen. The code belongs in the portal,
   not on the CV.
5. **Back-port the corrections to the other five CVs.** Class rank is top 10% and
   SCAILE ended 08.2026; the Allianz and Accenture CVs still say top 15% and
   "since 06.2026". They also still carry "Eligible for visa sponsorship" rather
   than "No visa sponsorship required", and all of them still have the bullet
   paint-order defect described above.
