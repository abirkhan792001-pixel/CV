# CV — E.ON Inhouse Consulting (ECON) eCON Academy

A one-page A4 CV, tailored to the [eCON Academy](https://www.eon.com/en/about-us/business-units/eon-inhouse-consulting/econ-academy.html)
recruiting event run by E.ON Inhouse Consulting.

Rebuilt on the **same template as the other tailored CVs in this repo**, rather
than the standalone design it used to carry. Work-experience copy is lifted from
those CVs.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
```

`build.mjs` measures the rendered content height against the A4 box and **exits
non-zero if the CV spills onto a second page**, so the one-page requirement is
enforced rather than eyeballed. It also counts unfilled `«placeholders»` and
flags the CV as not ready to send while any remain.

Edit `cv.html` only — content and styling both live there. The tuning knobs for
fitting content are the CSS variables at the top: `--fs-base`, `--lh`,
`--margin-x`, `--margin-y`.

Current state: **296.8 mm of 297 mm, one page, 0.2 mm headroom.** The page is
full. Anything added from here must be traded against something already on it,
and `--pad-b` has already been spent (see below).

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
| Bottom margin | `--pad-b: 10.5mm`, reduced from 12 mm to fit the third founder bullet. Not a matched value — the sources' ~14.5 mm of bottom white is a consequence of their shorter content, not a template parameter. Last text now ends at 285.9 mm, leaving 11.1 mm |
| Photo | `assets/photo.jpg`, **35 × 45 mm**, 700×900 px (~508 dpi at that size). Cropped from `assets/photo-source.png` by `scripts/` steps recorded in the commit — see below |
| Sizing | One size for everything except the name |

### Measured against the source

| | Lio PDF | This CV |
|---|---|---|
| Text left edge | 19.06 mm | 19.06 mm |
| Bullet glyph | 21.89 mm | 21.89 mm |
| Bullet text | 25.41 mm | 25.41 mm |
| Additional-info value column | 50.81 mm | 50.81 mm |
| Name size / width | 17.04 pt / 60.14 mm | 17.04 pt / 60.20 mm |
| Photo | 30.16 × 38.63 mm | 34.92 × 44.98 mm — see below |
| Photo top | 16.02 mm | 15.87 mm |
| Name top | 22.58 mm | 22.42 mm |
| Top bar | y 13.38 mm, 1.57 mm | y 13.23 mm, 1.59 mm |
| Contact separator gaps | 1.70 / 1.68 mm | 1.66 / 1.62 mm |
| Body size | 9.48 pt | 9.35 pt — see below |

Left edges land exactly: 19.06 mm ×31, 21.89 mm ×19, 25.41 mm ×19, 50.81 mm ×5.

### Four deliberate differences

1. **Body type is 9.35 pt, not the source's 9.48 pt.** The source's design rule is
   one line per bullet. Our bullets are longer than its, and there is a cliff
   between 9.35 and 9.40 pt: at 9.40 pt seven bullets wrap and the page jumps from
   278.6 mm to 308.7 mm. 9.35 pt is the largest size that preserves the rule.
   Don't raise it without re-running the build.
2. **The rules start at the text edge.** In the source they begin 0.46 mm to the
   left of the text — Word slop. Here all five rules span exactly 19.05–191.82 mm,
   the same edges as the text.
3. **The photo is flush right.** In the source it stops 3.44 mm short of the right
   text edge. Here its right edge sits on 191.82 mm with the rules and the
   right-aligned location/date column.
4. **The photo is 35 × 45 mm**, which is neither source's size. The two disagree —
   Lio uses 30.2 × 38.6, Strategy Consulting 37.7 × 47.1 — so there was no single
   value to copy. 35 × 45 is the German *Bewerbungsfoto* standard, and its aspect
   (0.7778) is within 0.2% of the image's native 237/304 = 0.7796, so it crops
   clean where Strategy's 0.800 would not.

### The Strategy Consulting CV settles the rule question

`Abir H. Khan_CV_Strategy Consulting.pdf` is the same template as Lio — every text
metric agrees within 0.03 mm (text left 19.09 vs 19.06, name width 60.14 vs 60.14,
bullet glyph 21.91 vs 21.89, bullet text 25.44 vs 25.41, value column 50.84 vs
50.81). It differs on one thing that matters: **its rules span 19.05–190.94, sitting
exactly on its own text edges.** That confirms Lio's 0.46 mm offset is Word slop and
not intent, which is the basis for difference 2 above. It is a LibreOffice export
rather than Word, which is also why its top bar is a 4.5 pt stroke rather than a
filled rectangle — the same 1.59 mm on the page.

One trap worth knowing: `h2` needs an explicit `font-size:1em`. Without it the
browser's default 1.5em heading size applies and the section headers render half
again too big — wrong for this template, where headers are body size.

### No photo, if you'd rather

Delete the `<img class="photo">` line in `cv.html`. Everything else reflows — the
header is a flex row and the left column already sets its own width.

## What this CV is optimised for

E.ON's own posting for the Academy screens on a short, specific list. Each one
is mapped to a place on the page:

| What E.ON asks for | Where it lands |
|---|---|
| Enrolled Master's in final year / PhD / recent grad, **outstanding academic record** | Education placed **first**, class rank on its own bullet |
| **Initial hands-on experience in consulting and/or the energy industry** | Founder entry (German energy regulation, flexibility), A&M restructuring, energy-transition deal sourcing at Biome, Impact Consulting |
| **Fluent English *and* German** | First row of Additional Information — see the caveat below |
| **Highly communicative within a team** | Hack-Nation (MIT × TUM), UN Foundation |
| Curiosity, "ready to transform the energy industry" | Tagline, the Commission thesis, the founder entry, Biome's lead bullet |
| International experience | MIT × TUM, Lisbon, Delhi, Hyderabad |

Two deliberate choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  grads, and E.ON gates explicitly on academic record.
- **Photo included.** All the source CVs except DHL carry one, and E.ON Inhouse
  Consulting is a German employer, where the photo CV is still the convention.

## Where the work-experience copy comes from

Bullets are taken from the source CVs rather than rewritten, so the same claims
appear the same way everywhere. The tailoring moves for E.ON:

- **TCG / Trariti Consulting Group is out**, as briefed. Work experience is
  Stealth → SCAILE → A&M → Biome.
- **Impact Consulting is back in**, under Extracurricular & Leadership, after
  being cut to make room for the founder entry. It costs 14.5 mm and there was
  17.3 mm going spare once the energy-skills row came out, so it fits without
  dropping anything else. Location is **London, United Kingdom** — three of the
  source CVs say *London, UK* and two say *United Kingdom*; this takes the city
  from the majority and spells the country out to match the rest of the page.
- **The founder entry now carries three bullets, in the candidate's own words.**
  The middle one went through four versions: an arrow chain that read as a slide,
  a prose revenue model, a *"Prototyped an AI audit…"* line that fixed the
  register but claimed a build that does not exist, and finally the supplied
  wording — *"Designed a three-stage model — audit, subscription software, then
  flexibility trading — grounded in German energy regulation"*. The third bullet
  is deliberately present-tense (*"Building…"*, *"applying to…"*, *"in early
  talks with…"*), which is accurate for a venture still in research.
  **No bold on that third bullet**: bolding *Antler* and *TUM Venture Labs*
  widened it past the single-line limit, and the wording matters more than the
  emphasis.

- **Biome's ESG line leads its entry.** "Sourced ESG-focused deals ... to
  support the fund's energy-transition thesis" is the single strongest genuine
  energy signal in the history, so it goes first rather than third.

Elsewhere on the page:

- **The coursework list is gone**, replaced by the Master's Thesis, run with
  the European Commission. Coursework titles are weak evidence — everyone on
  the programme took them. A Commission-partnered project on EU climate-finance
  allocation with a renewables focus is the strongest energy signal on the
  page, and it is work only this candidate did.
- **The M&A competition line** was cut, leaving only *Top 3 nationwide,
  National Case Study Challenge (out of 15,000 participants)*. The field size
  does more work than a second, smaller placing.
- **Hack-Nation** was added on brief. Scale figures — 24-hour sprint, MIT /
  Harvard / Stanford, 60+ countries — are from public sources (hack-nation.ai,
  MIT RAISE), not invented.

## Where the source CVs disagree

The six PDFs in this repo contradict each other in four places. This CV takes
the majority reading each time. Worth settling properly, because a recruiter
comparing two of your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova class rank** | top 15% (Allianz, both Accenture) vs top 10% (Siemens) | **top 10%** — confirmed |
| **Nova end date** | 12.2026 (four CVs) vs 01.2027 (DHL) | **12.2026** — confirmed |
| **German** | B1 (Allianz, both Accenture) vs Intermediate (Siemens) vs Basic (DHL) | **B1** |
| **SCAILE** | since 06.2026 (Allianz, both Accenture) vs 06.2026 – 08.2026 (Siemens) | **06.2026 – 08.2026** — confirmed |

Because SCAILE is a closed role now, its bullets are past tense ("Advised",
"Built and shipped"), matching how the Siemens CV — the other one that dates it
to 08.2026 — writes them.

One more, which is a wording difference rather than a fact:

- **The A&M creditor bullet.** Three CVs say *"Prepared creditor-negotiation
  presentations for client leadership"*; Accenture Strategy escalates it to
  *"Advised C-level client leadership on creditor-negotiation strategy"*. This
  CV uses the **"Prepared"** wording. Preparing materials for leadership and
  advising leadership are different claims, and the first one is what three of
  four CVs commit to.

Also worth knowing: `Abir H. Khan_CV_Siemens Advanta.pdf` and
`Abir H. Khan_CV_Strategy Consulting.pdf` are **byte-identical** — two
filenames, one document.

## The skills block is written for ATS

Checked against what E.ON Inhouse Consulting and RWE Consulting actually publish.
E.ON's own careers copy names *"shaping the digital energy ecosystem"*, *"unlocking
flexibility for millions of households"*, *"driving GenAI transformation"* and
*"smarter grids"*, and asks for outstanding academics in Business Administration,
Economics, Engineering or STEM plus internships in consulting and/or energy. RWE
Consulting — the RWE Group's in-house consultancy, working with Corporate Strategy
& Sustainability — names project management, stakeholder management, data analysis
and problem solving.

Two changes came out of that check:

- **`Commercial and Financial Due Diligence` is in Core skills**, replacing
  `Operating Model Design`. This reverses an earlier cut of `Commercial Due
  Diligence` on the grounds that CDD is transaction-side vocabulary in-house
  consultancies do not use. Reinstated on request, and defensible: the Biome
  entry is real diligence experience, and both E.ON and RWE run M&A and
  post-merger work. `Data Analysis` came out to keep the row at two lines.
- **Added `Digital Transformation` and `Generative AI`.** E.ON explicitly names
  GenAI transformation and the digital energy ecosystem as current work, and the
  SCAILE role is real evidence for both. `Generative AI` moved up from the
  Technical row, where it read as a tool rather than a capability.

**The `Energy transition` row is gone.** It listed Climate Finance, Renewable
Energy, Decarbonisation and Net Zero Strategy, but every one of those is asserted
rather than demonstrated — the page already proves the same interest with evidence
(the Commission thesis, the founder entry's German energy regulation, Biome's
energy-transition thesis). A keyword row restating what three entries already show
is padding, and a reader who spots that discounts the rest of the block.

**`Technical` now carries `Claude Code` and `Large Language Models (LLMs)`.** Both
are literal-match ATS terms, and E.ON names GenAI transformation as live work. The
long form is deliberate: parsers match "LLM", "LLMs" and the spelled-out phrase
differently, and writing it out catches all three.

**`Cost Reduction` was dropped from Core skills** as the least load-bearing term —
Business Case Development and Operating Model Design already cover that ground.
`Operating Model Transformation` shortened to `Operating Model Design`, which is
what brings the row to two lines while keeping all ten remaining terms; it is also
the more accurate claim at this level.

The layout parses cleanly: text is real text, the photo is a separate element an
ATS skips, and the two-column header is the same one the other five CVs use.

## Final audit

Run against the rendered PDF, not the source, so it reflects what a reader sees.

| Check | Result |
|---|---|
| Pages | 1 |
| Em / en dashes | none — the two em dashes in the three-stage bullet became parentheses |
| Stray quote characters | none |
| Apostrophes | all curly (`Master’s`, `team’s`, `fund’s`) — `Master’s` was straight |
| Bullets wrapping | 0 of 20 |
| Tagline | 2 lines |
| Left edges | 19.06 mm ×31, 21.89 mm ×20, 25.41 mm ×20, 50.81 mm ×5 — exact |
| Tilde characters | none — `~` removed from €600M, $170M and 60% |
| Right-aligned column | 15 lines at 191.90 mm, 3 within ±0.06 mm (italic side-bearing) |
| Rules | all 5 span 19.05–191.82 mm, identical |
| Photo right edge | 191.82 mm — on the rules |
| Date format | `MM.YYYY - MM.YYYY` throughout |
| Serial commas | none used, consistently |
| Placeholders | none |

Two things deliberately left alone:

- **"Specialization"** is US spelling on a page that otherwise uses British forms
  (Modelling, Organiser, Analysed). It is left as-is because it is part of the
  degree title as awarded by Shiv Nadar University, and all six source CVs write
  it that way. Degree titles are quoted, not restyled.
- **Two verbs repeat across adjacent entries** — *Managed* opens a SCAILE bullet
  and an A&M bullet; *Built* opens an A&M bullet and a Biome bullet. Within a
  single entry this would be worth fixing, as it was for Biome's three "S" verbs.
  Across entries it reads far less strongly, and with 0.2 mm of headroom any
  reword risks the one-line rule. Flagged rather than changed.

## Before sending

1. **German is B1.** E.ON's posting asks for *fluent English and German*. The CV
   states B1 honestly — do not inflate it, since ECON interviews partly in
   German. Worth addressing directly in the cover letter.
2. **Back-port the corrections to the other five CVs.** Class rank is top 10%
   and SCAILE ended 08.2026; the Allianz and Accenture CVs still say top 15%
   and "since 06.2026".
3. **The header now reads "No visa sponsorship required (Germany)"**, replacing
   "Eligible for visa sponsorship". The other five CVs still carry the old
   line — worth making consistent.
