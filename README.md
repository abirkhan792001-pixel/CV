# CV and cover letter — Oliver Wyman, Consultant (entry level), Dubai / Doha

A one-page A4 CV, tailored to Oliver Wyman's entry-level consulting intake for
its **Dubai / Doha** offices. The posting screens for structured problem
solving, research and interviews, client-ready deliverables, extracurricular
substance, and fluent English (Arabic an advantage). It explicitly does *not*
screen for a particular academic major, so this pass trades coursework detail
for consulting evidence.

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

```bash
npm run letter       # -> Abir Hilal Khan_Cover Letter_Oliver Wyman.pdf
```

`npm run share` builds, runs `scripts/finalise.py` (needs `pymupdf`), then runs
`scripts/audit.py`. It writes two identical PDFs: `Abir_Hilal_Khan_CV.pdf` and
`Abir Hilal Khan_CV_Oliver Wyman.pdf`, the latter following this repo's naming
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
  Every keyword stamped there also appears on the page — and that is now
  **enforced by the audit**, see *Metadata says only what the page says* below.
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

Current state: **294.6 mm of 297 mm, one page, 2.4 mm headroom**. Still short of a line, which is 4.23 mm
at this size, so anything added to the body has to be traded against something
already there.

## The cover letter

Oliver Wyman asks for a CV, a cover letter and transcripts. `cover-letter.html`
is the second of those, built by the same pipeline: `npm run letter` renders it,
checks it fits one page, counts unfilled placeholders, then stamps metadata and
writes `Abir Hilal Khan_Cover Letter_Oliver Wyman.pdf`.

It shares the CV's letterhead, so the two documents read as one application:
same navy, same top bar, same margins, same face. Body type is **10.5 pt, not
the CV's 9.35 pt** — the CV is squeezed by its one-line-per-bullet rule, and
running prose at 9.35 pt reads cramped. It has no photograph, and it now lands at
**295.8 mm of 297 mm**: the letter used to have room to spare and no longer does.

### Written against Clay's AI writing policy

Drafted to the policy at `clay.com/blog/ai-writing-policy`, whose four
principles are: **stand behind every sentence** (you cannot disown a line by
saying an AI wrote it), **writing is thinking**, **a document should take longer
to write than to read**, and **length is no virtue**. What that changed:

| Principle | What it did to the draft |
|---|---|
| Length is no virtue | **494 words**, excluding placeholders. Every opener that says nothing is gone: no *"I am writing to express my strong interest"*, no *"I believe my skills align"*, no *"I would welcome the opportunity to discuss"*. One summary sentence was cut in drafting because it only restated the paragraph above it |
| Respect the reader's time | A subject line (*Application: Consultant, Dubai / Doha*) so the reader knows what this is in one glance. Four short paragraphs, one claim each, each carrying a figure |
| Stand behind every sentence | Every factual claim traces to the CV, which traces to the source CVs. Nothing about motivation is asserted on the candidate's behalf |
| Writing is thinking | The two things only the candidate can think — why the Gulf, why this firm — are **left as placeholders**, not guessed at |

The house style follows the CV's: **no em or en dashes**, no *delve*, *leverage*,
*robust*, *landscape*, *passionate*, *resonate*, *thrilled*; no paragraph opening
with *Moreover*, *Furthermore* or *Additionally*.

The letter was then rewritten once end to end, on request, under the
`remove-ai-marks` skill's Layer B paraphrase brief: change wording at the token
level, reorder clauses, vary sentence boundaries, and keep every fact, figure
and name. The second draft shares **59% of its vocabulary** with the first and
introduces 47 words the first did not use; all eighteen figures and proper nouns
were checked to survive. Two caveats are recorded rather than glossed:

- **Layer A never ran.** The skill's cleaning service was unreachable in that
  environment, and the skill forbids falling back to local cleaning, so no
  invisible-Unicode or metadata pass was performed. Nothing here should be read
  as a claim that the file has been scanned or cleared.
- **A rewrite by the same model family as the draft is not what Layer B
  prescribes** (it calls for a model other than the suspected origin), so this
  is an editorial rewrite, not an anti-detection result.

Three things the rewrite itself got wrong were then fixed, on a read-back of the
result rather than of the brief:

- **SCAILE Technologies was missing from the letter entirely.** It ran *"since
  2022"* and then jumped to A&M in 01.2024, leaving the most recent entry on the
  CV unmentioned and dropping the one credential that speaks to Oliver Wyman's
  AI and digital work. It now has two sentences, placed **after** the earlier
  roles rather than in strict reverse chronology: A&M leads because it is the
  strongest evidence, and closing the evidence on *most recently* runs forward
  into *this year* (Draycott) and then into the January start date.
- ***"Trariti Consulting Group had me advising VC and PE firms"*** made the
  employer the subject and the candidate the object. The first draft's
  *"I advised"* was stronger and is back. Churning wording for its own sake
  costs something, and this is where it cost the most.
- ***"The front half of that pattern I learned earlier"*** mis-described its own
  evidence: at Trariti he ran the interviews **and** turned them into
  recommendations, which is the whole pattern, not its front half. The sentence
  is gone, and the paragraph now opens on a plain *"Earlier, at ..."*, which is
  also nine words shorter.

### The placeholders, and what filled them

The letter shipped with three `«...»` placeholders, counted by `build.mjs` and
reported as *"not ready to send"*. All three are now filled, from three earlier
cover letters the candidate wrote himself (Hilti Outperformer, E.ON Inhouse
Consulting, DHL Consulting). The rule stayed the same as for the CV: **claims
come from the sources, not from the drafter.**

- **Why Dubai or Doha.** The mobility half is his own: the four countries and
  the New York / Chicago collaboration are in the Hilti and E.ON letters and on
  the CV. The regional half was, for several drafts, **the one unsourced claim in
  either document** — none of the three earlier letters mentions the Gulf, the
  Middle East, Dubai or Doha once, so the sentence there argued from a general
  proposition about regional diversification that nothing backed.

  It is now sourced twice over. **He is building a freight-forwarding venture that
  reads supply-chain risk early and automates the response with AI agents**, and the
  markets where that is worth most are the volatile ones — which is a commercial
  reason for the region rather than a romantic one, and it is his. It is also not a
  new enthusiasm: the DHL letter, written in 05.2025, opens *"Somewhere between the
  pandemic freight crisis and the war in Ukraine, I stopped seeing supply chains as a
  background function and started seeing them as the actual architecture of global
  business."* The same paragraph then names **Ignacio, a senior consultant in the
  Dubai office**, as the conversation that turned the interest into an application —
  checkable, and the same move the E.ON letter made by naming Isabel, Sindhuja and
  Florian.

  **One thing to weigh before sending.** Telling a consulting firm you are actively
  building a company cuts both ways. Oliver Wyman's posting asks for *initiative,
  intuition, and creativity*, and a venture in the exact domain they would consult on
  is strong evidence of all three. It also invites the question of whether you would
  leave. The letter frames it as the origin of a regional interest rather than as a
  competing commitment, which is the honest framing and the least exposed one, but
  the judgement is the candidate's.

- **Why Oliver Wyman.** Argued from the posting's own distinctive offer — the
  choice to *"specialize early or explore different areas before choosing a
  path"* — against a record that is deliberately cross-domain. The opening,
  *"My interest in Oliver Wyman is specific"*, is his own construction from the
  DHL letter.
- **The date.** Set to the build date.

One further change came out of reading the sources. **Biome's bullet was
volume; now it is initiative.** It read *"took 3,000+ companies through a $170M
pipeline, judging each on market size, competition and how far it could scale"*.
The DHL letter carries a far better version of the same job: given a sector
brief, he argued the fund's thesis was underweight on decarbonisation, rebuilt
the evaluation framework, and took a revised case to the VP. Oliver Wyman screens
explicitly for *initiative, intuition, and creativity*, and that is the best
evidence of it in any of the source documents.

### Reviewed against the finished CV, and two fixes

Once the Antler entry went onto the CV, the letter had a hole in it.

- **The venture was missing entirely.** The letter opens *"Since 2022 my work has
  run to one pattern"* and then covers Trariti (2022), Biome (2023), A&M (2024)
  and *"most recently"* SCAILE (2026) — leaving **09.2024 to 06.2025 unaccounted
  for in the letter's own chronology**, the exact stretch the CV had just been
  fixed to explain. A reader holding both documents sees the letter skip a
  ten-month, second-most-recent role. It now has its own paragraph, placed after
  the earlier roles so the tail runs forward: Antler (2024–25), SCAILE (2026),
  Draycott (this year), start date.
- **The closing argument read as indecision.** It ended *"I have not yet met the
  one I want to spend a decade on"*, which to someone ranking candidates says *I
  do not know what I want* — and it sat in flat contradiction with the letter's
  own opening claim of *one pattern*. It now names the tension and resolves it:
  five different jobs, **one method, which is the pattern I opened with**, and the
  breadth was deliberate. The Antler paragraph is what earns *energy* a place in
  that list.

Both fixes overflowed the page by 9 mm, which `build.mjs` caught. Three things
paid for them, in order of honesty:

1. **A redundant clause, cut.** The close read *"I would move to either city and
   can start once Nova finishes"* — the third time the letter claimed willingness
   to move, after the opening names both cities and the mobility paragraph says
   moving is not the hard part. That is a real cut, not a space-saving one.
2. **Line height 1.42 to 1.36.** 1.42 was an arbitrary choice for this document;
   Word's default at 10.5 pt lands nearer 1.2, so 1.36 is still generous.
3. **Bottom margin 14 mm to 12 mm.** A normal letter margin either way.

The letter is now **494 words with 3.2 mm of headroom**. It is full: anything
added has to be traded, exactly like the CV.

Three smaller findings from the same review were then fixed too:

- ***"I worked on multibillion-dollar…"*** was the vaguest verb in the letter and
  it opened the letter's strongest paragraph, every other sentence of which uses
  *ran, built, traced, wrote*. Leading with the strong verb instead also sharpens
  the point the sentence exists to make: *"I ran a turnaround workstream for
  Fortune 500 clients **in** multibillion-dollar U.S. Chapter 11 restructurings,
  covering more than $100M"* puts his workstream inside the engagement rather
  than alongside it.
- ***"this year led my team at the Draycott…"*** would go stale exactly as the
  hardcoded date would have. Both results are now dated — *"In 2021 I placed in
  the top three of 15,000 … in 2026 I led my team at the Draycott"* — which also
  stops the undated case result reading as recent when it is five years old.
- ***"I don't just relocate; I integrate"*** is his own line, carried over from
  the Hilti letter, and it is gone. The sentence before it already proves
  mobility with four countries and the New York / Chicago work; the slogan only
  asserted the same thing again, and in the Hilti letter it sat in a bulleted
  *Global Mobility* section where that register fitted. In flowing prose it read
  as a boast. If an integration claim is wanted, the evidence to use is the
  German going A1 (Hilti, 01.2026) to B1 (the CV) — but that needs the timeline
  confirmed before it goes on a page.

### What the three letters disagree about

The candidate has confirmed that **everything in all three letters is true**, so
these are not errors to pick between; they are the same facts measured
differently, and the fix is to say which measurement is which.

| | Says | Resolution |
|---|---|---|
| **A&M deal scale** | *"multibillion-dollar restructuring deals"* (E.ON) vs *"over $100M in debt and lease obligations"* (Hilti, DHL) | **Both, and now both are on the page.** They measure different things: the size of the engagement, and the size of his own workstream. The letter now reads *"worked on multibillion-dollar U.S. Chapter 11 restructurings for Fortune 500 clients, running a turnaround workstream across more than $100M of debt and lease obligations"* — which is stronger than either figure alone and cannot be read as inflating one into the other |
| **Nova FT rank** | **#5** (DHL, 05.2025) vs **#8** (CV) | A time series, not a contradiction. The CV keeps **#8** as the later figure. Do not quote #5 again |
| **German** | **A1** (Hilti, 01.2026) vs **B1** (CV) | Seven months apart; progression. B1 stands |
| **Consulting Club** | *"Associate Secretary of the Consulting Club"* (Hilti) | **Now on the CV.** See below |
| **Biome's name** | *"my VC Fellowship"* (Hilti) vs *"Biome Venture Studio, Venture Capital Intern"* (CV) | Left alone. The Hilti sentence reads *"my VC Fellowship **and** work at Trariti"*, which may name a third role rather than Biome. Not assumed either way |

### The Consulting Club office is now on the CV

*Associate Secretary, Consulting Club* appears in the Hilti letter and on no
version of this CV. For a consulting application it is a directly relevant
office, so it went onto the Nova entry's second bullet, which had 53.7 mm of
slack on its line.

It did not fit as written. The bullet ran to **190.69 mm against a 191.84 mm
edge, 1.15 mm from wrapping** — the same fragility the `Focus areas` row had
before it was trimmed, and a wrap costs 4.23 mm against 3.6 mm of headroom, so
it would have pushed the CV to two pages. Dropping the redundant *"Ranked"* from
*"Ranked top 10% of the class"* bought back 11.2 mm. `audit.py` keyed its Nova
reading-order marker to that exact phrase, so both markers were retargeted to
*"Top 10% of the class"*; the second one is a bare `all()` over matching lines,
which would have passed **vacuously** on an empty match set rather than failing.

### The 12-month gap is closed

The E.ON letter, dated 28.09.2025, said: *"I supported an energy startup as a
Founder's Associate, leading digital transformation and customer-centric
innovation in the sector."* That could not be SCAILE, which began 06.2026, so it
described a role held before September 2025 — inside the unexplained **08.2024
to 07.2025** window this CV had carried through every pass as unfixable without
a fact only the candidate had.

He has now supplied it: **Stealth Energy Venture (backed by Antler), Founder's
Associate, Munich, 09.2024 - 06.2025.** It sits between SCAILE and A&M in Work
Experience. Naming the backer is the point — a bare *"stealth"* entry asks the
reader to take an unverifiable claim on trust, while Antler is a recognisable
early-stage investor, so the entry carries its own credibility. The Munich
location also explains the header address, which until now had no entry behind it
earlier than 06.2026.

**What the twelve-month gap actually was: ten months, plus a month either side.**

| | |
|---|---|
| Shiv Nadar, BMS | 08.2020 - 07.2024 |
| *gap* | **1 month** |
| Stealth Energy Venture | 09.2024 - 06.2025 |
| *gap* | **1 month** |
| Nova SBE, MSc | 08.2025 - 12.2026 |

Two single months between a degree and a job, and a job and a degree. Nothing a
recruiter asks about.

This is also why the dates were left as a placeholder rather than inferred. The
gap ran 08.2024 to 07.2025 and it would have been tempting to fill the entry with
exactly that range — it would have plugged the hole perfectly and been **wrong at
both ends**, on a CV where every other date is right and where an interviewer can
check.

### What the Antler entry cost, and what buying UN Foundation back cost

The Antler entry needed 3 lines and an entry margin, **14.66 mm**, against 3.6 mm
of headroom. It was first paid for by dropping the **United Nations Foundation**
entry, which costs exactly the same — the page did not move.

That trade has since been reversed on request: **UN Foundation is back**, and
both entries are now on the page. Paying for it a second time took three cuts:

| Out | Lines |
|---|---|
| SCAILE: *"Automated weekly client KPI reporting … cutting manual effort by 60%"* | −1 |
| Trariti: *"Quantified critical funding levers and investment viability across $100M+ in deal value"* | −1 |
| The whole `Interests` row (*distance running, swimming, hiking, baking*) | −1, plus a 0.7 mm grid gap |
| **In: United Nations Foundation** | **+3**, plus an entry margin |

Net **+1.2 mm**: 293.4 mm to 294.6 mm, and headroom down from 3.6 mm to 2.4 mm.

**Why those three.** The two bullets were each the third of their entry and the
most redundant: SCAILE still claims strategy and client ownership, Trariti still
claims growth-strategy advice and 90+ interviews, and no term in the skills grid
or the metadata lost its backing. `Interests` was the softest line on the page,
and the argument for cutting it is that UN Foundation is a **better** version of
the same signal — Oliver Wyman asks for *"evidence of leading an interesting and
impactful life outside of your studies"*, and *"1,200+ women and children in
rural India"* answers that harder than four hobbies do.

**What was actually lost:** two figures, the **60%** manual-effort cut and
Trariti's **$100M+ in deal value**, and the personality hook a consulting
interviewer sometimes opens on. At 2.4 mm the page is now tight; anything else
added has to be traded.

`audit.py` moved with it: the SCAILE reading-order marker was keyed to the
deleted automation bullet and now points at *"Owned North American clients"*, and
the right-aligned column count went from 18 to **20**, ten entries at two rows
each.

## What this CV is optimised for

Oliver Wyman's posting screens on a list. Each item is mapped to a place on the page:

| What the posting asks for | Where it lands |
|---|---|
| **Bachelor's (and Master's) degree** | Education first: MSc Finance to 12.2026, BMS Magna Cum Laude |
| **Research, gathering data, running interviews** | *"Led 90+ stakeholder interviews"*; Biome's 3,000+ company screen; European Commission thesis; `Stakeholder Interviews` in Core skills |
| **Turning information into clear insights** | *"turning insights into recommendations for a $10M+ revenue product"* |
| **Analyse problems, identify patterns, test hypotheses** | A&M's **root-cause analysis** and **scenario models**; `Structured Problem Solving`, `Root-Cause Analysis` |
| **Structure recommendations that support client decisions** | *"informing board-level decisions on distressed M&A"*; *"to prioritise turnaround initiatives"* |
| **Client-ready deliverables and presentations** | *"Prepared creditor-negotiation presentations for client leadership"*; `Executive Communication`; PowerPoint in Technical |
| **Work across industries and capabilities** | Restructuring (A&M), venture capital (Biome), strategy (TCG), fintech (Impact), AI/go-to-market (SCAILE), public sector (EC thesis) |
| **Travel, home market and international** | **Not stated** — the availability line was removed. Six cities across four countries appear as entry locations, which implies mobility but does not claim it |
| **Structure your work, manage your priorities** | *"Managed a turnaround workstream"*; *"prioritise turnaround initiatives"* |
| **Initiative, intuition, creativity** | Hack-Nation organiser; *"Advised the founders…"*; *"Owned North American clients … >$100k ARR"* |
| **Strong problem solving and analytical mindset** | **Top 3 of 15,000** nationally — in the header *and* in Education; Draycott PE Challenge Team Lead |
| **Extracurriculars; an impactful life outside studies** | Three entries — Hack-Nation, Impact Consulting, UN Foundation — plus the `Interests` row |
| **Fluency in English** | `Languages` row leads with English (Fluent) |
| **Proficiency in Arabic (advantage)** | `Languages` row, second entry: **Arabic (Basic)** — stated at the level it is |
| **Office: Dubai / Doha** | **Not stated.** Neither city appears on the page; the contact line reads *Munich, Germany*. Belongs in the cover letter — see *Before sending* |

Two choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  graduates, and this posting gates on the degree.
- **Photo included.** All the source CVs except DHL carry one, and it is normal
  practice in the Gulf. It is a separate element that a parser skips — the
  five-parser check below runs against the file as shipped, photo and all. To
  remove it, delete the `<img class="photo">` line; everything reflows. Note
  that removing it also collapses the free header space the two extra header
  lines are living in.

## Where the consulting vocabulary comes from

The rule is the repo's existing one: **a keyword goes on the page only if
something on the page backs it.** The skills grid is split in two.

`Core skills` are demonstrated by an entry above them:

| Term | Backed by |
|---|---|
| Structured Problem Solving | Top 3 of 15,000 nationally; A&M workstream; Draycott Team Lead |
| Root-Cause Analysis | A&M: *"Ran root-cause analysis of operating and cash-flow inefficiencies"* |
| Market Sizing | SCAILE: *"backed by a market sizing of AI search (GEO)"*; Biome's market-size screen |
| Competitive Benchmarking | Impact Consulting: *"Created competitive benchmarking…"* |
| Commercial Due Diligence | Biome: *"Built commercial due diligence models…"* |
| Financial Modelling | A&M scenario models; TCG market and investment models |
| Stakeholder Interviews | TCG: *"Led 90+ stakeholder interviews"* |
| Executive Communication | A&M: creditor-negotiation presentations for client leadership; board-level decisions |

`Focus areas` are the target domain — Growth Strategy, Market Entry, Operating
Model Transformation, Restructuring, Private Capital. Labelling them *focus
areas* rather than *skills* is deliberate and is the source CVs' own label:
Restructuring is one internship and Market Entry is one extracurricular
engagement. Each still has a line on the page behind it — Private Capital by
four (the TCG bullet, *Venture Capital Intern*, *commercial due diligence*, and
*Draycott Private Equity Challenge*).

**`Management Consulting` was on this row and came off.** It bought the ATS
phrase, but it was the least informative term of the five — it says the
candidate wants to work in management consulting, which is what applying already
says — and it cost the row its slack: the line ended at **190.67 mm against a
191.84 mm text edge, 1.17 mm from wrapping**. A wrap there is not cosmetic; the
page carries 3.6 mm of headroom against a 4.23 mm line, so one extra character
in that row would have pushed the CV onto a second page. The row now ends at
177.85 mm with 14 mm of slack, and the page still carries *consulting* three
times (*Trariti Consulting Group*, *boutique strategy consulting firm*, *Impact
Consulting*) and *Consultant* twice.

**What is deliberately not claimed:** any Middle East experience, workshop
facilitation, and survey design. The posting names workshops as part of the job;
nothing in any source CV evidences them. See *Before sending*.

**Arabic is on the page at Basic**, added on the candidate's instruction and
placed second in the `Languages` row, straight after English — it is the term
this posting names as an advantage, so it should be where a recruiter's eye
lands. The level is written next to it rather than left to inference: the
posting asks for *proficiency*, Basic is not proficiency, and a Gulf interview
tests it in the first minute.

## Written for the ATS

Oliver Wyman recruits through an applicant-tracking system, so the parse is the
first round. `scripts/audit.py` checks the claims below against the **rendered
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
bullet text still starts at **exactly 25.41 mm** on all 17 bullets, verified at
character level.

### Five parsers, re-run on this version

Extraction was re-run on the shipped file after this pass. The check is stricter
than a text dump: it asserts that **all nine organisations appear in page order**,
and that each of five leading bullets falls between its own employer and the next
one. Impact Consulting was added to both lists this pass, so the extracurricular
section — the one that grew — is now covered too.

| Extraction mode | Reading order | Bullet ownership | Email | Phone | LinkedIn |
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
| Text is real text, not an image | 511 words selectable |
| Reading order | every bullet follows its own employer, verified for 6 entries |
| Orphan bullet glyphs | none |
| Name | first line of the stream |
| Email, phone | present as plain text, regex-matchable |
| LinkedIn | spelled out as `linkedin.com/in/khan-abir`, not hidden behind anchor text |
| Section headers | `EDUCATION`, `WORK EXPERIENCE`, `EXTRACURRICULAR & LEADERSHIP`, `SKILLS & ADDITIONAL INFORMATION` all found |
| Fonts | all 5 embedded as subsets |
| Pages | 1 |
| Dates | `MM.YYYY` throughout |

### Metadata says only what the page says

The rule was previously enforced by hand and drifted twice — an earlier version
shipped `RWE Consulting` in the keyword field, a term present nowhere on the
page. **The audit now checks it.** Every comma-separated keyword stamped by
`scripts/finalise.py` must appear in the rendered page text, case-insensitively,
or the build fails.

It earned its keep immediately: it caught `Private Capital` still sitting in the
keyword list minutes after that term had been dropped from the `Focus areas`
row. Current state: **27 keywords, all of them on the page.**

The same assertion runs in `finalise.py`, so the cover letter is held to it too.
One bug surfaced there and is fixed: a hyphenated compound can take its line
break **at its own hyphen**, so the flattened text stream holds
*"creditor- negotiation"* for a word the reader sees whole, and a naive
substring check fails on layout rather than on content. Both checks now also
test the rejoined variant.

An ATS that indexes both fields finds the same words twice either way, and a
candidate who cannot see a term on their own CV cannot be asked about it in an
interview.

## Rebuilding this repo produces a taller page than it used to

Worth knowing before you touch the content. The previously shipped PDFs render
text about **4.7% narrower than Liberation Serif's actual metrics** — whatever
laid them out was setting text narrow, and content tuned against that rendering
overflows when rebuilt here. That was fixed by trimming copy, not by shrinking
type: `--fs-base` is still 9.35 pt, so the page renders the same anywhere.

## The template

Formatting is matched to `Abir_H._Khan_CV_Lio.pdf`, measured out of that PDF
with PyMuPDF rather than eyeballed. Every value in `cv.html` carrying a mm or pt
figure is a number taken from it.

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

The seven distinct CV documents in this repo -- eight files, two of them
byte-identical -- contradict each other. This CV takes the majority
reading each time. Worth settling properly, because a recruiter comparing two of
your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova class rank** | top 15% (Allianz, both Accenture) vs top 10% (Siemens, RWE) | **top 10%** — confirmed |
| **Nova end date** | 12.2026 (four CVs) vs 01.2027 (DHL) | **12.2026** — confirmed |
| **German** | B1 (Allianz, both Accenture) vs Intermediate (Siemens) vs Basic (DHL) | **B1** — the *"improving"* the source CVs append was dropped to fit Arabic on the line; the claim is unchanged |
| **SCAILE** | since 06.2026 (Allianz, both Accenture) vs 06.2026 – 08.2026 (Siemens, RWE) | **06.2026 – 08.2026** — confirmed |
| **TCG location** | Mumbai (Siemens, Strategy, Allianz, DHL) vs Delhi (both Accenture) | **Mumbai** |
| **TCG's third bullet** | *"a $10M+ revenue product"* (Allianz) vs *"$10M+ ARR product"* (both Accenture) vs *"$10M+ product"* (Siemens, Strategy) | **"$10M+ revenue product"** |
| **Impact Consulting location** | London, UK (Allianz, both Accenture, DHL) vs United Kingdom (Siemens/Strategy) vs London, United Kingdom (RWE) | **London, United Kingdom** |
| **Impact Consulting's verb** | *Created* (Allianz, both Accenture, RWE) vs *Built* (Siemens/Strategy, DHL) | **Created** — majority, and it varies the three *Built* bullets above it |

Two wording calls carried over from the last pass:

- **A&M's plan is a *"$9.8M risk-mitigation plan"***, not a *"cost and
  risk-mitigation plan"*. Five of six source CVs say the former.
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
| Bullets wrapping | 0 of 17 |
| Bullet text edge | 25.41 mm on all 17, at character level |
| Left edges | 19.06 mm ×32, 21.89 mm ×17, 167.68 mm ×8, 50.81 mm ×5 — exact |
| Right-aligned column | 20 location/date lines flush on 191.84 mm, an exact count |
| Nothing crosses the right edge | widest line ends at 191.84 mm |
| Rules | all 4 section rules span 19.05–191.82 mm, identical |
| Photo right edge | 191.82 mm — on the rules |
| Bottom white | 13.46 mm |
| Metadata keywords on the page | 30 of 30 |
| Em / en dashes | none |
| Non-ASCII inventory | only `•`, `’`, `×` — all intentional |
| Dates | `MM.YYYY` throughout |
| Placeholders | none |

Three things deliberately left alone:

- **A 12-month gap, 08.2024 to 07.2025.** The bachelor's ends 07.2024 and the
  master's begins 08.2025; nothing on the page covers between. Consulting
  recruiters read timelines closely and will ask, and a case interviewer may open
  with it. Not fixable here — it needs a fact only the candidate has.
- **"Specialization"** is US spelling among British forms (Modelling, Organiser,
  prioritise). It is the degree title as awarded by Shiv Nadar University and
  all seven source CVs write it that way. Degree titles are quoted, not restyled.
- **The `×` in "MIT Sloan AI Club × TUM"** (U+00D7). A naive ATS could mangle it,
  but the keywords either side survive independently.

## Before sending

1. **Arabic (Basic) is now on the page, and no source CV evidences it.** It was
   added on instruction, so the level stated has to be one you can defend: a
   Gulf interviewer may open in Arabic to see what *Basic* means. If it
   overstates where you actually are, say so and it comes off — the row has
   9 mm of slack and the page does not move either way. If it understates you,
   raise it: *proficiency* is what the posting asks for, and `Arabic
   (Conversational)` or a CEFR level would read stronger than `(Basic)`.
   Fitting it cost `German (B1, improving)` its last word — the row would have
   wrapped to a second line otherwise, and the page has only 3.6 mm of
   headroom against a 4.23 mm line.
2. **Decide whether the venture belongs on the CV too.** The letter names the
   freight-forwarding venture as the reason the Gulf is specific; the CV does not
   mention it. It is deliberately not there — the first instruction of this pass
   was to take a founder entry *off* the page — but it is current work in the
   domain the letter argues from, and leaving it off is now a choice rather than
   an omission. If you would also rather the CV carried the relocation signal,
   restoring *"Open to relocation to Dubai or Doha | Willing to travel
   internationally"* is one line in the header and costs the page nothing,
   because the photograph, not the text, sets the header height.
3. **Do not reinstate "No visa sponsorship required."** It was written for
   Germany and is false for the UAE and Qatar, where the employer sponsors
   every expatriate hire. If a nationality or current-residence line is wanted —
   some Gulf employers do expect one — add it as a fact, not as a claim about
   sponsorship.
4. **The 12-month gap will come up.** Have the answer ready; consulting
   interviews open on the CV.
5. **Consider swapping Impact Consulting for FitSure** if the entrepreneurial
   signal matters more to you than the consulting one. *FitSure (InsurTech
   venture, incubated at Shiv Nadar University), Co-Founder, 01.2023 – 08.2023 —
   "Defined the business model and pricing strategy for wearable-based dynamic
   health premiums in a 3-person team"* appears in five source CVs and is the
   same height, so the swap is free. Oliver Wyman's posting asks for *initiative,
   intuition and creativity* and for *evidence of leading an interesting and
   impactful life outside of your studies*, which FitSure speaks to directly.
   Impact Consulting was chosen because it backs `Market Entry` and `Competitive
   Benchmarking` in the skills grid — swap the entry and those two terms lose
   their evidence, so retune the row too.
6. **No industry line.** The page evidences pharmaceuticals, industrials and
   logistics (A&M), energy, SaaS and consumer tech (Biome) and fintech (Impact)
   in the *source* CVs, but none of those sectors is named on this page and
   there is no room for a row that names them. Entry-level consulting hiring does
   not screen on industry, so this is a deliberate omission rather than a gap.
7. **Workshops are not claimed.** The posting lists workshops among client-ready
   deliverables. Nothing in any source CV evidences facilitating one. If you have
   run one, it is worth a bullet.
8. **Back-port the corrections to the other six CVs.** Class rank is top 10%,
   SCAILE ended 08.2026, and TCG's location is Mumbai; the Allianz and Accenture
   CVs still disagree on the first two. They also still carry "Eligible for visa
   sponsorship" and all of them still have the bullet paint-order defect
   described above.
