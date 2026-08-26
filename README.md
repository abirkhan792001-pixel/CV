# CV — Prior Labs, Founder Associate

A one-page A4 CV, tailored to the
[Founder Associate](https://priorlabs.ai/careers?ashby_jid=95d8c3c1-8524-4ea4-83ec-273b0fefe534)
role at **Prior Labs** — the tabular-foundation-model lab behind TabPFN, now an
independent frontier AI lab inside SAP.

Adapted from the **trawa CV** (`Abir H. Khan_CV_Trawa.pdf`, built 22.08.2026). That
file is the E.ON-lineage CV with `(Germany)` dropped from the visa line; everything
else on it was carried over unchanged unless listed below.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> Abir_Hilal_Khan_CV.pdf, then finalise + audit
```

`npm run share` now runs three steps, not two: build, `scripts/finalise.py` (exact
A4 + document metadata), then `scripts/audit.py`, which is new on this branch. It
checks ATS parseability, layout, typography and
[provenance](#provenance-is-gated-too) — and it
[found a real defect](#the-audit-found-a-real-defect) on its first run.

Current state: **292.0 mm of 297 mm, one page, 5.0 mm headroom.** 524 selectable
words, 5 fonts embedded, photo at 655 DPI, 312 KB.

> One build note, environment-specific rather than a project setting: `package.json`
> asks for `playwright ^1.56.1`, which resolves to 1.62.1 — the version the committed
> `package-lock.json` records, matching the other branches in this repo. That release
> wants a newer Chromium than the one preinstalled in this build container, so the
> build here additionally pinned `playwright@1.56.1` with `--no-save`. That pin
> touched `node_modules` only and left the lockfile alone, so `npm install` on your
> own machine behaves exactly as it does on every other branch.

## What changed from the trawa CV

Five content edits and one structural fix. Nothing else on the page moved.

| | trawa CV | This CV |
|---|---|---|
| **Founder entry** | Stealth AI-Energy Startup — DACH whitespace, three-stage energy model, electricity-bill AI tool | **SQRlane** *(AI agents for freight forwarding)* — one shipped-product bullet plus two research findings |
| **Tagline** | "advised Fortune 500 leadership on turnaround strategy at A&M; sourced energy-transition deals in VC; now founding an AI-energy venture for German SMEs" | "**A&M** restructuring, **VC** diligence and **go-to-market** at an early-stage startup; now founding an **AI-agent venture** in logistics, built on **open-weight models**" |
| **Core skills** | Strategy Consulting, Financial Modelling, Commercial and Financial Due Diligence, Digital Transformation … | Go-to-Market Strategy, Sales Enablement, Process Automation, AI Agent Workflows, Generative AI … |
| **Technical** | Microsoft Excel, PowerPoint, Power BI, SQL, Python, Claude Code, LLMs | Python, SQL, Claude Code, LLMs, **Open-Weight Models**, Excel, PowerPoint — reordered so the AI terms lead |
| **Interests** | Distance running, swimming, hiking, baking | **cut** — see below |
| **Bullet rendering** | `position:absolute` glyph | normal-flow hanging indent |

### Where the page stands

The trawa CV sits at 296.8 mm of 297 — full. Four moves since, in order:

1. The SQRlane entry arrived with **four** bullets, paid for by cutting `Interests`
   (−4.9 mm: one line plus its grid gap) and trimming the Technical row back to one
   line (−4.2 mm, dropping `FastAPI` and `PowerPoint` to make room for
   `Open-Weight Models`). 296.8 → 296.1 mm.
2. The fourth bullet — the code/model-boundary finding — was **cut on request**,
   handing 4.2 mm back. 296.1 → 292.0 mm.
3. **`PowerPoint` was restored on request**, which re-wrapped the Technical row to
   two lines and spent exactly that 4.2 mm. 292.0 → 296.1 mm.
4. **`Power BI` was removed on request**, which took the Technical row back to one
   line and handed the 4.2 mm straight back. 296.1 → **292.0 mm, 5.0 mm headroom.**

`Interests` is the one thing still out, and at 5.0 mm of headroom against its
4.9 mm cost it is now — just — a free add. Left out rather than restored, because
nothing was asked for.

**One template addition came out of step 3.** With `PowerPoint` back the Technical
row wrapped mid-name and left `BI` orphaned on the second line, and the Core skills
row split `Market Sizing` the same way. Both got a `.nb` (`white-space:nowrap`)
span so each row breaks at a comma instead of through a term. Removing `Power BI`
in step 4 took its span with it, but the class stays: `Market Sizing` still needs
it, and the Core skills row is long enough that it always will.

Deliberately a CSS class and **not** `&nbsp;` — U+00A0 is one of the invisible
carriers `scripts/audit.py` refuses, so the entity would fail our own gate.

## The SQRlane entry

Three bullets: what was shipped, then two of the three research findings. The
third — the code/model boundary — was cut on request after the first pass; it is
kept in the table below, struck through, so the record shows why the page has two
rather than the three that were originally selected.

```
SQRlane (AI agents for freight forwarding)            Munich, Germany
Founder                                                 since 08.2026
```

| Bullet | What it is | Where it comes from |
|---|---|---|
| Shipped a working prototype: agents screen **42 live risk sources**, decide **reroute or hold** per booking, and draft the emails | The product | 42 free keyless sources across six families; Risk Monitor, Route Advisor and Comms Agent are the three that genuinely run |
| Cut inference cost **~10x** by sizing each model to its task (screening, judgement, drafting) against measured token counts | **Research — per-task model routing** | Measured 12,800 in / 3,700 out per cycle over 14 calls: $0.0034 against $0.0355 for a frontier model everywhere. 10.4x |
| ~~Split code from model: code computes routes, days and cost; the model only judges, so no customer-facing number is invented~~ | ~~the code/model boundary~~ — **cut on request** | Still true of the system: dates and sums never reach a model, and no probability is applied anywhere. Off the page, not off the record — worth having ready if it comes up |
| Designed for **EU-hosted open-weight inference**, with recorded reasoning and human approval before anything is sent | **Research — residency vs provenance** | Open-weight throughout so the host is a choice; data residency and model provenance kept as separate claims |

The two that remain map onto the posting's *What Makes You Special*: built
automations and agents that people used, and familiarity with open source and
foundation models. The cut bullet was the one carrying the technical-judgement
signal, so that now rests on the shipped-prototype bullet alone.

**"Designed for" in the fourth bullet is load-bearing and must stay.** The prototype
currently calls a US inference provider — it was built against a free tier for speed
of iteration, and the whitepaper says so in as many words. The architecture supports
EU-only operation and the provider layer is one file; the switch has not been made.
Do not upgrade that verb in an interview.

## What this CV is optimised for

The posting screens on a specific list. Each item is mapped to a place on the page:

| What Prior Labs asks for | Where it lands |
|---|---|
| Bachelor's or Master's in Business Administration, CS, **Data Science** or related | Education first — MSc Finance (Nova SBE), BMS Finance & Strategy |
| **1–2 years in consulting, venture capital, start-ups** | A&M (restructuring), Biome (VC), SCAILE (startup), SQRlane (founder) — named in that order in the tagline |
| **An AI-first way of working** | SQRlane's four bullets; SCAILE's AI agent workflows; `Claude Code` and `Large Language Models (LLMs)` in Technical |
| **You've built automations, agents, or internal tools that people actually used** | SCAILE: *"Automated weekly client KPI reporting with AI agent workflows, cutting manual effort by 60%"* — an internal tool with a measured saving |
| **High agency: you ship a v1 quickly** | *"Shipped a working prototype"* — deliberately the posting's own verb |
| **Familiarity with open source, foundation models** | Research 1 and 3; `Open-Weight Models` in Technical |
| Own the **inbound pipeline**, tracking and attribution | Biome: 3,000+ companies across a $170M pipeline; CAC/LTV unit economics |
| **Sales enablement** — decks, case studies, POCs | SCAILE go-to-market and >$100k ARR owned end to end; A&M creditor-negotiation presentations for client leadership |
| Cross-functional projects; **community building** | Hack-Nation: the TUM side of a 24-hour sprint, MIT and Stanford, 60+ countries |
| **Structured and reliable**, strong analytical skills | A&M turnaround workstream, $9.8M scenario models, board-level decisions |

Two things kept from the base deliberately:

- **Education before experience** — standard for a final-year Master's student, and
  the posting names the degree first among its essentials.
- **The visa line.** `No visa sponsorship required` stays: Prior Labs is a German
  employer, and it removes a question before it is asked.

## The audit found a real defect

`scripts/audit.py` is ported onto this branch from the Oliver Wyman CV and retargeted
to this page's entries and geometry. On its first run against the trawa lineage it
failed nine checks, and the cause was not cosmetic:

> ```
> FAIL  bullets stay with 'Nova School'   -- org line 6, bullet line 52
> FAIL  bullets stay with 'SQRlane'       -- org line 15, bullet line 68
> FAIL  no orphan bullet glyphs on their own line
> ```

The trawa CV styles `li` with `position:relative` and its `::before` glyph with
`position:absolute`. A positioned element paints in a later phase, so Chromium emits
**every bullet after the rest of the page** in the PDF's text stream. Copy the text
out of the trawa PDF and you get all nine entries first, then a wall of 20 orphaned
achievements, each trailed by a lone `•`. An ATS reading stream order sees nine
employers with nothing under them.

Fixed here the way the Oliver Wyman CV fixes it — a hanging indent built from normal
flow (`text-indent` plus an inline-block marker) that lands on exactly the same two
edges, glyph at 21.89 mm and text at 25.41 mm. Document order is preserved, the page
is pixel-identical, and all 21 bullets now sit with their employer.

**This is worth back-porting to every other CV in the repo** that still uses the
positioned marker.

## The template

Unchanged from the trawa CV and documented here for completeness. Formatting is
matched to `Abir_H._Khan_CV_Lio.pdf`, measured out of that PDF with PyMuPDF rather
than eyeballed.

| | |
|---|---|
| Type | **Liberation Serif** — metrically identical to Times New Roman, SIL OFL, vendored in `assets/fonts/` so builds are reproducible offline |
| Navy | `#0c447c` — measured rgb(12,68,124); top bar, name, section headers and rules |
| Link | `#0563c1` — measured rgb(5,99,193), underlined |
| Structure | Bold **organisation** left / bold **location** right, then italic *role* left / italic *dates* right, then bullets |
| Photo | `assets/photo.jpg`, **35 × 45 mm** (German *Bewerbungsfoto* standard), 900×1157 px = 655 DPI |
| Sizing | One size for everything except the name. `--fs-base: 9.35pt` is the largest that keeps every bullet on one line — don't raise it without re-running the build |

Left edges land exactly: text at 19.06 mm ×30, bullet glyph at 21.89 mm ×20,
bullet text at 25.41 mm ×20 (measured at character level), value column at
50.81 mm ×4.

Edit `cv.html` only — content and styling both live there. The tuning knobs are the
CSS variables at the top: `--fs-base`, `--lh`, `--pad-*`.

## Provenance is gated too

A CV is a document you send, so `scripts/audit.py` also asserts that the file names
nothing about what produced it. Seven checks: no XMP packet, no C2PA manifest,
Producer blank, no tool name in producer/creator/title/subject, no generator
fingerprint in the file bytes, no invisible or bidi carriers in the text, and no
EXIF/XMP/C2PA inside the embedded photo.

All seven pass, and they pass because the pipeline earns it rather than by luck:
Chromium renders hand-authored HTML, `finalise.py` overwrites the info dict and
blanks Producer, and Chromium re-encodes the photo on embed, which drops its EXIF.

Three notes on how these are written, because each is a way the check could have
been useless:

- **The metadata scan reads producer, creator, title and subject — not keywords.**
  Keywords are already required to appear in the visible text, so `Claude Code`
  there is a skill the candidate has, not a tool that touched the file. Scoping it
  this way is what lets that keyword be added without a false failure.
- **The byte-level fingerprint list is deliberately narrow, and excludes `Adobe`.**
  Every CID font carries `/Registry(Adobe)/Ordering(Identity)`, so matching it would
  fail on the five embedded Liberation Serif subsets rather than on a real leak.
- **The image check reads `xref_stream_raw`, not `extract_image`.** This one was a
  bug, caught by testing it: `extract_image()` re-encodes the picture and drops the
  APP1 segment the check is looking for, so the first version would have passed a
  photo whose EXIF was still sitting in the file. Splicing an `Exif` segment in
  proves it — raw sees it, extracted does not.

Each of the seven was verified by poisoning a copy of the PDF and confirming it
fails: a `Skia/PDF` Producer, an injected XMP packet, an embedded `c2pa`/`jumbf`
stub, a spliced `Exif` segment, and a `U+200B`/`U+200F` pair put through the real
build. A gate that cannot fail is not a gate.

The one thing none of this covers is a statistical or sampling-level watermark in
the *wording*, which is a different class of mark and needs a rewrite pass and a
detector, not a file check.

## Final audit

Run against the rendered PDF, not the source, so it reflects what a reader receives.
`npm run share` reports all of this; **all checks pass**.

| Check | Result |
|---|---|
| Pages | 1 |
| Exact A4 | 595.28 × 841.89 pt = 210.00 × 297.00 mm |
| Content height | 292.0 mm — 5.0 mm headroom |
| Bottom white | 16.10 mm |
| Text is text | 524 words selectable; 5 fonts, all embedded |
| Bullets with their employer | 9 of 9 entries |
| Bullets wrapping | 0 of 20 |
| Bullet text left edge | 25.41 mm, all 20 |
| Right-aligned column | 18 lines, 0.083 mm spread (italic side-bearing) |
| Rules | one span, 19.05–191.82 mm |
| Photo right edge | 191.82 mm — on the rules |
| Nothing crosses the right edge | widest line 191.96 mm |
| Metadata keywords visible on the page | 15 of 15 |
| Em / en dashes, placeholders | none |
| Non-ASCII | only `•`, `’`, `×` — all intentional |
| Dates | `MM.YYYY` throughout; every section in reverse chronological order |
| Compound terms split across a line break | none — `Market Sizing` held by `.nb` |
| Repeated bullet-opening verbs | none across all 20 |
| XMP packet / C2PA manifest | neither present |
| Producer / tool fingerprints | Producer blank; none of 11 byte markers; nothing in creator, title or subject |
| Invisible, bidi, variation-selector carriers | none of 23 |
| Embedded photo | no EXIF, XMP or C2PA in the raw stream |

## Before sending

1. **Confirm the SQRlane dates.** `since 08.2026` is carried straight from the base's
   founder entry and matches when the repository work starts. If the venture predates
   that, it is the one figure on the page taken on trust.
2. **The 12-month gap, 08.2024 to 07.2025, is still here.** The bachelor's ends
   07.2024 and the master's begins 08.2025, and this lineage of the CV has nothing
   covering between. The Oliver Wyman branch fills exactly that window with *Stealth
   Energy Venture (backed by Antler), Founder's Associate, 09.2024 – 06.2025*. If
   that entry is accurate, it belongs on this CV too — but it costs about 12 mm and
   there are 0.9 mm going spare, so something substantial has to come out for it.
   Worth deciding before you send: German-reading recruiters ask about gaps.
3. **German is B1.** Not a blocker — the posting asks for exceptional written and
   verbal communication *in English* — but Prior Labs is a German employer.
4. **`Founders Associate` at SCAILE and `Founder Associate` at Prior Labs are
   different jobs with near-identical titles.** That reads as a strength; just be
   ready to say plainly what the SCAILE one actually involved.
5. **Back-port the bullet fix** to the other CVs in this repo, per the section above.
