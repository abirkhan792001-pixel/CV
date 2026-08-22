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

Current state: **293.1 mm of 297 mm, one page, 3.9 mm headroom.** That margin is
thin on purpose — the page is full. Adding a bullet means taking one out, or
dropping `--fs-base`.

## The template

Matched to the source CVs (Accenture / Allianz / Siemens), which are set in
Times New Roman:

| | |
|---|---|
| Type | **Liberation Serif** — metrically identical to Times New Roman, SIL OFL, subset and vendored in `assets/fonts/` so builds are reproducible offline |
| Accent | `--navy: #1f4e79` — top rule, name, section headers and their underlines |
| Structure | Bold **organisation** left / bold **location** right, then italic *role* left / italic *dates* right, then bullets |
| Photo | `assets/photo.jpg`, top-right at 28 × 36 mm — extracted from the Accenture Strategy PDF, kept at its native 237:304 ratio so it isn't stretched |

There is a wrapping cliff between 10.0 pt and 10.2 pt: at 10.2 several bullets
tip onto a second line and the page jumps from 293 mm to 315 mm. `--fs-base` is
set at **10 pt** for that reason. Don't nudge it up without re-running the build.

### No photo, if you'd rather

Delete the `<img class="photo">` line in `cv.html`. Everything else reflows —
the header is a flex row and the left column already sets its own width.

## What this CV is optimised for

E.ON's own posting for the Academy screens on a short, specific list. Each one
is mapped to a place on the page:

| What E.ON asks for | Where it lands |
|---|---|
| Enrolled Master's in final year / PhD / recent grad, **outstanding academic record** | Education placed **first**, class rank on its own bullet |
| **Initial hands-on experience in consulting and/or the energy industry** | A&M restructuring, plus energy-transition deal sourcing at Biome |
| **Fluent English *and* German** | First row of Additional Information — see the caveat below |
| **Highly communicative within a team** | Hack-Nation (MIT × TUM), FitSure, Impact Consulting |
| Curiosity, "ready to transform the energy industry" | Tagline, Net-Zero coursework, Biome's lead bullet |
| International experience | MIT × TUM, London, Lisbon, Delhi |

Two deliberate choices carried over from the source CVs:

- **Education before experience.** Standard for final-year students and recent
  grads, and E.ON gates explicitly on academic record.
- **Photo included.** All the source CVs except DHL carry one, and E.ON Inhouse
  Consulting is a German employer, where the photo CV is still the convention.

## Where the work-experience copy comes from

Bullets are taken from the source CVs rather than rewritten, so the same claims
appear the same way everywhere. Two tailoring moves for E.ON:

- **TCG / Trariti Consulting Group is out**, as briefed. Work experience is
  SCAILE → A&M → Biome.
- **Biome's ESG line leads its entry.** "Sourced ESG-focused deals ... to
  support the fund's energy-transition thesis" is the single strongest genuine
  energy signal in the history, so it goes first rather than third.

Elsewhere on the page:

- **Net-Zero coursework** is pulled to the front of the Nova bullet. It is real —
  it appears in the DHL CV's coursework list.
- **The M&A competition line** (2nd place, St. Stephen's College, Delhi
  University, 2022) also comes from the DHL CV.
- **Hack-Nation** was added on brief. Scale figures — 24-hour sprint, MIT /
  Harvard / Stanford, 60+ countries — are from public sources (hack-nation.ai,
  MIT RAISE), not invented.

## Where the source CVs disagree

The six PDFs in this repo contradict each other in four places. This CV takes
the majority reading each time. Worth settling properly, because a recruiter
comparing two of your CVs will see the difference:

| | Says | This CV uses |
|---|---|---|
| **Nova class rank** | top 15% (Allianz, both Accenture) vs top 10% (Siemens) | **top 15%** |
| **Nova end date** | 12.2026 (four CVs) vs 01.2027 (DHL) | **12.2026** |
| **German** | B1 (Allianz, both Accenture) vs Intermediate (Siemens) vs Basic (DHL) | **B1** |
| **SCAILE** | since 06.2026 (Allianz, both Accenture) vs 06.2026 – 08.2026 (Siemens) | **since 06.2026** |

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

## Before sending

1. **German is B1.** E.ON's posting asks for *fluent English and German*. The CV
   states B1 honestly — do not inflate it, since ECON interviews partly in
   German. Worth addressing directly in the cover letter.
2. **Confirm the class rank** (15% vs 10%) and fix it across all six CVs, not
   just this one.
3. **Confirm SCAILE is still current.** This CV says "since 06.2026"; the
   Siemens CV has it ending 08.2026.
