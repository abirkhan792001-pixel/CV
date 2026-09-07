# CV — Allianz Technology, AI Transformation Analyst

A one-page A4 CV, tailored to the **AI Transformation Analyst (m/f/d)** opening
(Job ID 104521) on the IF&IS AI & Automation team at
[Allianz Technology SE](https://careers.allianz.com/), Unterföhring, near
Munich. The role sits between business and engineering: mapping IF&IS
processes (network, workplace, data center, security), turning AI
opportunities into functional requirements, use cases and business cases, and
carrying those through stakeholder engagement and change management.

Same template as the other tailored CVs in this repo; only the content
changed, retargeted from the previous application on file
(`Abir Hilal Khan_CV_Orizon.pdf`, a Lean/process-optimization role). That
target already leaned on the same underlying evidence — stakeholder
interviews, process root-cause analysis, an AI agent workflow — so this pass
is a re-emphasis toward this posting's specific vocabulary (functional
requirements, use cases, business cases, AI-enabled redesign), not a rewrite.
No new facts were added.

## Build

```bash
npm install          # installs playwright
npm run build        # -> Abir_Khan_CV.pdf, with a one-page check
npm run preview      # also writes preview.png for visual QA
npm run share        # -> Abir_Hilal_Khan_CV.pdf, the file to actually send
```

`Abir Hilal Khan_CV_Allianz Technology.pdf` is a copy of that share output
under the naming convention the other tailored CVs in this repo use. It is
the file to attach to this application, and it **replaces** the older PDF of
the same name — see "Superseded" below.

`npm run share` builds, then runs `scripts/finalise.py` (needs `pymupdf`) to
produce the copy you hand to a recruiter: it stamps document metadata (title,
author, ATS keywords) that Playwright leaves empty, and trims the page to
exact A4 (Chromium otherwise snaps to 210.23 × 297.35 mm). `build.mjs`
measures rendered content height against the A4 box and exits non-zero if the
CV spills onto a second page, so the one-page requirement is enforced rather
than eyeballed. It also counts unfilled `«placeholders»`.

Edit `cv.html` only — content and styling both live there. The tuning knobs
for fitting content are the CSS variables at the top: `--fs-base`, `--lh`,
`--margin-x`, `--margin-y`.

Current state: **296.8 mm of 297 mm, one page, 0.2 mm headroom** — unchanged
from the previous target, since every edit in this pass was matched
line-for-line against what it replaced so nothing reflowed.

## The template

Formatting, fonts, colours and measurements are unchanged from prior targets
and, further back, matched to `Abir_H._Khan_CV_Lio.pdf`, measured out of that
PDF with PyMuPDF. See earlier commits for the full measured-vs-source table —
nothing in that layer changed here, only the words.

| | |
|---|---|
| Type | **Liberation Serif** — metrically identical to Times New Roman, SIL OFL, vendored in `assets/fonts/` |
| Navy | `#0c447c` — top bar, name, section headers and rules |
| Link | `#0563c1`, underlined |
| Photo | `assets/photo.jpg`, 35 × 45 mm, the German *Bewerbungsfoto* standard |
| Structure | Bold **organisation** left / bold **location** right, then italic *role* left / italic *dates* right, then bullets, one line each |

## What this CV is optimised for

The posting's own language is specific — it names *functional requirements*,
*use cases, epics and user stories*, *business cases*, *as-is process
mapping*, *AI-enabled redesign* and *stakeholder engagement* as the actual
job, not just nice-to-haves. Each is mapped to a place on the page:

| What the posting asks for | Where it lands |
|---|---|
| **Identify, assess and prioritize AI & Automation opportunities** | SQRlane's three-stage AI workflow and inference-cost bullet, SCAILE's AI-enabled redesign bullet, Core skills leading with AI Adoption / GenAI |
| **Interview process owners; map as-is processes; identify AI-enabled redesign opportunities** | TCG: *"Led 90+ interviews with process owners across departments, translating findings into structured, actionable requirements"* — the closest single match in the whole work history; A&M's root-cause-analysis bullet |
| **Translate business needs into functional requirements, use cases, epics, user stories** | TCG's interview bullet (now ending in *requirements*, not *recommendations*); SQRlane's three-stage workflow design; `Requirements Definition` and `Business Analysis` in Core skills |
| **Build and maintain business cases (value, effort, adoption)** | SQRlane: *"Scoped a pilot blueprint and business case…"*; A&M: *"Built scenario models to support the business case for a $9.8M…plan"*; `Business Case Development` in Core skills |
| **Maintain visibility of the AI use-case portfolio** | SQRlane's multi-stage AI workflow spans three named use cases (screening, judgement, drafting) under one roadmap |
| **Stakeholder engagement across Regional Heads, Chapter Leads, Tribe Leads, Group AI stakeholders** | A&M's stakeholder-relations bullet (client leadership and creditors), SCAILE's cross-functional-stakeholder bullet, `Stakeholder Management` in Core skills |
| **Change management for AI-enabled ways of working** | SQRlane's human-approval design (adoption/governance), `Change Management` in Core skills |
| **Applied understanding of GenAI, LLMs, predictive models, automation** | SQRlane's model-sizing bullet, Technical row leading with `Large Language Models (LLMs), Predictive Models` |
| **Bridge between business and IT/AI technical teams** | SCAILE (advising founders while owning delivery), SQRlane (building and shipping the system personally) |
| **Analytical mindset, structured problem-solving, value creation** | A&M scenario models, Biome's 3,000+ company screen, TCG's funding-lever models |
| **Bachelor's/Master's in a related field; up to 5 years' experience** | MSc Finance (Nova SBE) + BMS Finance & Strategy (Shiv Nadar); work history is well inside the posting's ceiling, consistent with an entry-level opening |
| **Fluent English; German a plus** | Languages row: English (Fluent), German (B1, improving) |

Two things carried over deliberately from the source CVs:

- **Education before experience.** Standard for a final-year Master's student.
- **Photo included.** German employer, photo-CV convention.

## Tailoring moves vs. the previous target (Orizon)

Every edit was matched in length against what it replaced, since the page had
0.2 mm of headroom before this pass and has the same after — nothing wraps to
a second line:

- **Tagline:** *"project and change management driving process improvement…
  now building AI-driven process automation at SQRlane"* → **"AI-enabled
  process transformation… now designing agentic AI use cases at SQRlane"** —
  leads with AI and use-case design, this posting's own terms, instead of the
  generic process-optimization framing the Orizon version used.
- **SQRlane, bullet 3:** *"…and feasibility case for a mid-market forwarder"*
  → **"…and business case for a mid-market forwarder"** — swaps in the
  posting's literal, recurring term.
- **SCAILE, bullet 1:** *"…a process-optimization initiative cutting manual
  effort by 60%"* → **"…an AI-enabled redesign cutting manual effort by 60%"**
  — this is the single closest match in the history to *"identify
  AI-enabled redesign opportunities"*, so it's named as one.
- **A&M, bullet 3:** *"…to validate a $9.8M cost and risk-mitigation plan
  against measured financial impact"* → **"…to support the business case for
  a $9.8M cost and risk-mitigation plan"** — same underlying work, framed in
  the posting's business-case language rather than generic validation.
- **TCG, bullet 1:** *"Led 90+ stakeholder interviews across departments,
  translating findings into structured, actionable recommendations"* →
  **"Led 90+ interviews with process owners across departments, translating
  findings into structured, actionable requirements"** — swaps in the
  posting's own nouns (*process owners*, *requirements*) for a bullet that
  was already, substantively, this exact activity.
- **Core skills** dropped `Process Optimization`, `Root-Cause & Risk
  Analysis`, `Data Analysis` and `AI Process Automation` (Orizon-specific
  framing) and added `AI Adoption`, `Generative AI (GenAI)`, `Business
  Analysis`, `Requirements Definition`, `Business Case Development` and
  `Process Redesign` — this posting's own recurring nouns, front-loaded.
- **Technical** reordered to lead with `Large Language Models (LLMs),
  Predictive Models` (the posting names both explicitly) ahead of the Excel/
  PowerPoint/Power BI/SQL/Python block, which is unchanged.
- Everything else — Education, SQRlane's workflow-design and inference-cost
  bullets, SCAILE's positioning and client-ownership bullets, A&M's turnaround
  and root-cause bullets, Biome, TCG's second bullet, Extracurricular &
  Leadership, Languages, Interests — is untouched, because it already reads
  the way this posting wants or isn't reachable without inventing a fact.
- **PDF metadata keywords** (`scripts/finalise.py`) were retargeted the same
  way: AI Transformation, Business Analysis, Requirements Definition, Use
  Cases, User Stories, Business Case Development, Process Design, IT
  Infrastructure, Information Security replace the previous keyword set.

## Final audit

Run against the rendered PDF.

| Check | Result |
|---|---|
| Pages | 1 |
| Content height | 296.8 mm of 297 mm — 0.2 mm headroom |
| Bullets wrapping | 0 |
| Fonts | all 5 embedded as subsets |
| Page size | 595.28 × 841.89 pt = exact A4 |
| Photo | 900 × 1157 px in a 35 × 45 mm frame = 655 DPI |
| Selectable text | 508 words |
| Placeholders | none |

## Superseded

`Abir Hilal Khan_CV_Allianz Technology.pdf` in this repo previously belonged
to an older, unrelated Allianz Technology application. That version still
carried TCG as a hidden/removed entry from an earlier draft, "top 15%" (now
top 10%), "since 06.2026" for SCAILE (now 06.2026 – 08.2026, closed-role past
tense) and "Eligible for visa sponsorship" (now "No visa sponsorship
required"). This build replaces it under the same filename with the current
facts and this posting's tailoring. If that older PDF was already sent to a
recruiter for a different Allianz Technology role, keep a copy before
overwriting further — this repository only tracks the current version.

## Before sending

1. **Fit is on business-analysis framing, not a security background.** The
   posting sits inside IT Infrastructure & Information Security, but the role
   itself is a business/AI bridge, not an infrastructure or security
   engineering position — nothing on the page claims network, workplace,
   data-center or security expertise, and nothing should be added to imply it
   at interview.
2. **German is B1.** The posting treats German as a plus, not a requirement.
   Don't inflate it.
3. **"Up to 5 years of experience"** is a ceiling, not a floor — consistent
   with an Entry Level posting. The page's roughly a year of relevant
   experience across SQRlane, SCAILE, A&M, Biome and TCG is proportionate to
   that, not a gap to explain.
4. **Be ready to discuss the SQRlane agent design in interview** — the
   three-stage workflow, the model-sizing rationale and the human-approval
   step are the strongest direct evidence of *AI use-case design* on the
   page, and this posting's interviewers will likely probe it specifically.
5. **The TCG interview bullet is now framed as requirements-gathering.** Be
   ready to describe that work the same way if asked — what departments, what
   the interviews fed into, and what "requirements" concretely meant there.
