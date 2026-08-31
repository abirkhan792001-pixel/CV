# CV — Allianz Consulting (Allianz Services)

A one-page A4 CV, tailored to the **Consultant** opening at
[Allianz Consulting](https://careers.allianz.com/), the Allianz Group's internal
consulting unit, which partners with operating entities worldwide on digital,
sustainability and operational-excellence transformation.

Same template as the other tailored CVs in this repo. Work-experience copy is
lifted from those CVs and from `Abir_Hilal_Khan_CV_Prior_Labs.pdf`, which is
where the founder entry comes from.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> Abir_Hilal_Khan_CV.pdf, the file to actually send
```

`Abir Hilal Khan_CV_Allianz Consulting.pdf` is a copy of that share output under
the naming convention the other tailored CVs in this repo use. It is the file to
attach to this application.

`npm run share` builds, then runs `scripts/finalise.py` (needs `pymupdf`) to
produce the copy you hand to a recruiter. It differs from the build output in
three ways, none of which touch the layout:

- **Document metadata.** Playwright takes the title from `<title>` but exposes
  nothing else, so Chromium leaves Author, Subject and Keywords empty and stamps
  itself as Creator. Those fields are what a PDF viewer shows in its title bar,
  what an email client previews, and what some applicant-tracking systems index.
- **Exact A4.** Chromium snaps the page to whole device pixels and lands on
  210.23 × 297.35 mm. The finalise step trims the mediabox to a true
  595.276 × 841.890 pt. The rightmost text sits at 191.96 mm and the lowest at
  285.66 mm, so this removes blank margin only — it asserts the page is at least
  A4 before cropping, and asserts exact A4 after.
- **Verification.** It asserts one page and every font embedded, then reports
  photo DPI and selectable word count.

### On "high resolution"

A PDF's text and rules are vector, so they are resolution-independent — they
print as sharply as the device allows. The only raster element is the photo, at
**900 × 1157 px placed in a 35 × 45 mm frame = 655 DPI**, against a print
standard of 300. It is encoded at JPEG quality 95 with 4:4:4 chroma (no
subsampling), which is what removes the faint artefacts the earlier quality-90
4:2:0 encode left around the collar and hairline. All five fonts are embedded as
subsets, so the file renders identically on a machine that has never seen
Liberation Serif. 317 KB — comfortably emailable.

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

Allianz Consulting's posting screens on a short, specific list. Each one is
mapped to a place on the page:

| What Allianz asks for | Where it lands |
|---|---|
| **Expert knowledge of AI frameworks; leverage AI tools in everyday tasks; consult clients on AI adoption** | The founder entry (all three bullets), SCAILE's agent-workflow and KPI-automation bullets, and the first half of Core skills. This is the posting's loudest requirement and it gets the most page. |
| Minimum **1 year in operational business or management consulting** as an FTE | Work experience: Founder, SCAILE, A&M, Biome. See the caveat in **Before sending** — this is the one line the page does not clear outright. |
| **Analytical thinking**, affinity for solving problems | A&M scenario models, Biome's 3,000+ company screen and CDD build-ups, SCAILE's GEO market sizing |
| Responsibility for **deliverable quality and project milestones** | A&M's "full turnaround workstream", SCAILE's "owned North American clients end to end" |
| **Business development and client pitches** | SCAILE's >$100k ARR signed and onboarded end to end |
| **Excellent English**, used for presentations and reports | Languages row; A&M's creditor-negotiation presentations |
| **PowerPoint and Excel (complex functions)** | Technical row, deliberately placed first in it |
| **Curiosity for or knowledge of insurance and financial services** | FitSure (InsurTech), MSc Finance, A&M restructuring, Biome |
| **Project or change management** tools and techniques | A&M turnaround workstream; `Project and Change Management` in Core skills |
| International experience, German or other languages | Munich, Lisbon, Delhi, Hyderabad; North American clients; five languages |
| Affinity for **IT and GenAI** | Technical row (Claude Code, LLMs, open-weight models, Python, SQL) |
| Digital / sustainability / operational-excellence transformation | AI entries (digital), the Commission thesis (sustainability), SCAILE's 60% effort cut (operational excellence) |

Two deliberate choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  grads.
- **Photo included.** All the source CVs except DHL carry one, and this is a
  German employer, where the photo CV is still the convention.

## Where the work-experience copy comes from

Bullets are taken from the source CVs rather than rewritten, so the same claims
appear the same way everywhere. The tailoring moves for Allianz Consulting:

- **TCG / Trariti Consulting Group is out**, as briefed. It was on the older
  `Abir Hilal Khan_CV_Allianz Technology.pdf` but not on the current source;
  the audit below confirms it does not appear in the rendered PDF. Work
  experience is Stealth → SCAILE → A&M → Biome.
- **The founder entry is now the freight-forwarding venture**, replacing the
  AI-energy one, with the three bullets taken verbatim in substance from
  `Abir_Hilal_Khan_CV_Prior_Labs.pdf`. Two changes: the `~` on *~10x* is
  dropped, per the repo's no-tildes rule, and *EU-hosted* and *recorded
  reasoning* are bolded. That third bullet is the strongest line on the page
  for an insurer — EU-hosted inference, a recorded reasoning trail and a human
  in the loop before anything is sent is exactly the governance posture a
  regulated financial institution has to be able to evidence. The venture is
  named: **SQRlane**.
- **The first founder bullet names the three agents** rather than counting risk
  sources. *Screening reads live risk feeds, judgement calls reroute or hold,
  drafting writes the emails* says what was actually built; *42 live risk
  sources* only said how wide one input was. It also matches the second bullet,
  which already sizes a model per agent. Held to one line, which is this
  template's design rule.
- **FitSure is back in**, under Extracurricular & Leadership. It is the only
  insurance experience in the history, and the posting asks for curiosity for
  or knowledge of insurance. Its verb was changed from *Designed* to
  **Modelled**, because *Designed* already opens the third founder bullet.
- **Impact Consulting is out, United Nations Foundation is in**, on request.
  The two entries are the same height, so this is a straight swap and the page
  did not move. It trades a consulting title plus a fintech fundraising claim
  for the clearest *desire to make a difference* evidence in the history, which
  the posting asks for by name.
- **Biome leads with scale and drops its energy bullet.** *Evaluated 3,000+
  companies within a $70M pipeline* now goes first, because analytical volume
  is what this posting screens on. The energy-transition origination line came
  out: the Commission thesis already carries sustainability, with more weight
  behind it, so the bullet was paying rent twice.
- **A&M and SCAILE are unchanged.** Both already read the way this posting
  wants — client ownership, business development, presentations for leadership,
  a quantified automation result — so nothing was gained by touching them.
- **The tagline is rebuilt as four noun phrases** (*MSc Finance at Nova SBE
  (FT #6); Fortune 500 turnaround strategy at A&M; AI agent workflows and
  go-to-market at SCAILE; now founding an AI venture in freight forwarding*).
  The previous version opened its third clause with *advised*, which collided
  with the verb opening SCAILE's first bullet.

## The outcome pass

The first draft of this CV had nine bullets that ended without a result — they
named an activity, a topic or a volume and stopped. That is the single biggest
thing separating a good CV from a strong one, so five of the nine were closed
with facts supplied by the candidate:

| Bullet | Was | Now |
|---|---|---|
| Master's Thesis | the topic only | scaled to the EU's **€662B climate budget** — 34% of the 2021-2027 MFF plus NextGenerationEU, against a 30% target |
| SCAILE advisory | that he advised | positioning adopted, **80% MoM MRR growth** |
| Hack-Nation | that he coordinated | **120 TUM participants** |
| SQRlane | what was built | a **pilot blueprint** for a mid-market forwarder, plus **Y Combinator** and **a16z Speedrun** applications |
| Draycott PE Challenge | Team Lead, no placing | **cut** — the team did not place, so the bullet had no result to give. Its line paid for the SQRlane one. |

Four remain open, and each needs a fact only the candidate has: Biome's 3,000+
company screen and its due-diligence models (did anything get funded?), FitSure
(any users or pilot?), and SQRlane's governance bullet, which is design intent
rather than an outcome and is kept anyway because it is the strongest line on
the page for an insurer.

The **€662B** figure is the European Commission's own: the 2021-2027 MFF plus
NextGenerationEU is projected to contribute €662 billion to climate objectives,
34% of the envelope against a 30% mainstreaming target. It is the scale of the
thing the thesis studies, not a figure the candidate claims to have moved.

## Where the source CVs disagree

The six PDFs in this repo contradict each other in four places. This CV takes
the majority reading each time. Worth settling properly, because a recruiter
comparing two of your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova SBE FT rank** | FT #8 across the older CVs | **FT #6** — Nova SBE's International Master's in Finance placed 6th worldwide and 5th in Europe in the 2025 Financial Times ranking, up from 7th and 11th in the two years before. #8 was stale |
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

Written against the posting's own vocabulary rather than generic consulting
terms, because this posting is unusually specific about what it wants.

**Core skills** opens with `AI Adoption`, `Generative AI (GenAI)` and
`Agentic AI Workflows`. The posting names *AI frameworks*, *AI tools in
everyday tasks* and *consult clients on AI adoption* in a single bullet, and
separately calls GenAI a valuable asset — so the AI terms lead, and both the
spelled-out and abbreviated forms of GenAI are present because parsers match
them differently. `Digital Transformation` and `Operational Excellence` are
Allianz Consulting's own words for two of its three transformation pillars.
`Project and Change Management` is a literal match for *project or change
management tools and techniques*.

Three terms came out of the previous version of this row to keep it at two lines:
`Financial Modelling` (now inside the Technical row, where it qualifies Excel),
`Commercial and Financial Due Diligence` and `Market Sizing` (both demonstrated
by the Biome and SCAILE bullets), and `Business Case Development`. The rule
applied is the repo's existing one: a keyword row that restates what an entry
already proves is padding, and a reader who spots that discounts the rest.

**Technical leads with Excel and PowerPoint**, which is unusual placement for a
technical row and deliberate here — the posting asks for them by name and
specifies *can perform complex functions*, so the parenthetical says
`(financial modelling, complex functions)`. `Open-Weight Models` was added
alongside `Large Language Models (LLMs)` and `Claude Code`, since the founder
entry is evidence for it.

**No insurance keyword row was added.** FitSure, the MSc Finance, A&M and Biome
demonstrate the financial-services interest; asserting it again in a keyword row
would be the same padding the energy-transition row was cut for.

`scripts/finalise.py` stamps a matching keyword list into the PDF metadata,
which is what some applicant-tracking systems index.

## Final audit

Run against the rendered PDF, not the source, so it reflects what a reader sees.

| Check | Result |
|---|---|
| Pages | 1 |
| Content height | 296.8 mm of 297 mm — 0.2 mm headroom |
| TCG / Trariti | absent |
| Em / en dashes, stray quotes, tildes | none |
| Non-ASCII inventory | only `•` ×19, `’` ×2, `×` ×1, `€` ×1 — all intentional |
| Bullets wrapping | 0 of 19 |
| Repeated bullet-opening verbs | none — Ranked, Graduated, Shipped, Cut, Designed, Advised, Automated, Owned, Managed, Built, Prepared, Evaluated, Developed, Coordinated, Modelled, Created |
| Dates | `MM.YYYY` throughout |
| Verb tense | past for closed roles, present only for the live venture |
| Fonts | all 5 embedded as subsets |
| Page size | 595.28 × 841.89 pt = exact A4 |
| Photo | 900 × 1157 px in a 35 × 45 mm frame = 655 DPI |
| Selectable text | 539 words |
| Placeholders | none |

Three things deliberately left alone, carried over from the previous pass:

- **A 12-month gap, 08.2024 to 07.2025.** The bachelor's ends 07.2024 and the
  master's begins 08.2025; nothing on the page covers between. German recruiters
  read timelines closely and will ask. Not fixable here — it needs a fact only
  the candidate has.
- **"Specialization"** is US spelling among British forms (Modelling, Organiser).
  It is the degree title as awarded by Shiv Nadar University and all six source
  CVs write it that way. Degree titles are quoted, not restyled.
- **The `×` in "MIT Sloan AI Club × TUM"** (U+00D7). A naive ATS could mangle it,
  but the keywords either side survive independently.

## Before sending

1. **The one-year bar, and what the page now says about it.** The posting asks
   for a minimum of one year in operational business or management consulting
   **as a full-time employee**. By duration the page clears it: SQRlane 1 month,
   SCAILE 3, A&M 7, Biome 3 — **14 months**, or **19** counting the FitSure
   venture and netting its overlap with Biome. What the page no longer states is
   the employment basis. *Intern* was dropped from both titles on request, so
   A&M reads *North American Commercial Restructuring Team* and Biome reads
   *Venture Capital Analyst* — the latter is the title six of the source CVs
   already use, minus its *(Intern)* qualifier. Neither line claims full-time
   employment, and neither denies it; the dates carry the duration.
   **Do not assert full-time employment for A&M or Biome** on an application
   form or in interview. Both firms will confirm the actual basis on a reference
   check, and a stated claim that fails that check is a different problem from a
   title that simply omits a qualifier.
2. **German is B1.** The posting treats German as a bonus rather than a
   requirement, so B1 is not disqualifying — but do not inflate it.
3. **Allianz Consulting is not Allianz Technology.** This CV is for the
   consulting unit inside Allianz Services. `Abir Hilal Khan_CV_Allianz
   Technology.pdf` in this repo is an older, different application and still
   carries TCG, "top 15%", "since 06.2026" and "Eligible for visa sponsorship".
   Do not send that one by mistake.
4. **Back-port the corrections to the other five CVs.** Class rank is top 10%,
   SCAILE ended 08.2026, and the header line is now "No visa sponsorship
   required", with the country qualifier dropped.
5. **The founder entry names a live prototype.** Be ready to demo or describe
   the three agents, the model-sizing decision and the approval step in
   interview — an internal consultancy at an insurer will ask about the human-
   in-the-loop design specifically.
