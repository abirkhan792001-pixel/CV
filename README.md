# CV — E.ON Inhouse Consulting (ECON) eCON Academy

A one-page A4 CV, tailored to the [eCON Academy](https://www.eon.com/en/about-us/business-units/eon-inhouse-consulting/econ-academy.html)
recruiting event run by E.ON Inhouse Consulting.

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

## What this CV is optimised for

E.ON's own posting for the Academy screens on a short, specific list. Each one
is mapped to a place on the page:

| What E.ON asks for | Where it lands |
|---|---|
| Enrolled Master's in final year / PhD / recent grad, **outstanding academic record** | Education placed **first**, grade on its own line |
| **Initial hands-on experience in consulting and/or the energy industry** | Founders Associate at an energy SaaS startup, leading the experience section |
| **Fluent English *and* German** | First row of Skills & Languages, both bolded |
| **Highly communicative within a team** | Leadership & Initiative — HackNation (MIT × TUM) |
| Curiosity, "ready to transform the energy industry" | Profile line + the Energy domain skills row |
| International experience | MIT × TUM collaboration; exchange/thesis line under Education |

Format notes, all deliberate:

- **No photo.** The Academy is an international event (Malmö 2025, Essen 2026)
  and the application runs in English. A clean international format travels
  better than the classic German photo CV here.
- **Education before experience.** Standard for final-year students and recent
  grads, and E.ON gates explicitly on academic record.
- **Restrained red accent** (`--accent`) nods to E.ON's brand without being
  costumey. Change one variable to switch it — `#1f3a4d` (deep petrol) is a good
  neutral alternative.
- **Justified bullets with hyphenation**, to hold a tight right edge at this
  information density.

## Writing the bullets

The event's core is a live consulting case and structured-problem-solving
training, so bullets should read the way a consultant would want them to:

> **action verb → what you owned → the number that moved**

Concretely, prefer *"Built the tariff model behind a €2.4m flexibility pilot with
three municipal utilities"* over *"Responsible for financial modelling and
stakeholder management"*. Ownership and quantification beat scope statements.

Two more things worth biasing toward, given who reads this:

- **Energy-domain judgement.** ECON's public cases are e-mobility, heating
  systems, and flexibility in the energy system. Any bullet that shows you
  already reason about that market is worth more than a generic business bullet.
- **Client/stakeholder surface.** Anything where you had to persuade, align, or
  present to someone outside your own team.

## What changed from the source CVs

Built from the six tailored CVs in this repo (Accenture Strategy was the most
current source). Deltas for the E.ON version:

- **Trariti Consulting Group (TCG) removed**, as briefed. SCAILE takes its slot.
- **Hack-Nation added** under Leadership. Scale figures (24-hour sprint, MIT /
  Harvard / Stanford, 60+ countries) are from public sources — hack-nation.ai
  and MIT RAISE — not invented.
- **Biome's energy line promoted to its lead bullet.** "Sourced ESG and
  energy-transition deals" is the single strongest genuine energy signal in the
  history, so it leads rather than sitting third.
- **Net-Zero coursework pulled forward** in Education for the same reason.
- **Profile rewritten** against E.ON's screening criteria, closing on why ECON
  specifically rather than consulting generally.

## Two things to verify before sending

1. **German is B1.** E.ON's posting asks for *fluent English and German*. The CV
   states B1 honestly — do not inflate it, since ECON interviews partly in
   German. Consider addressing it directly in the cover letter.
2. **Nova SBE end date.** The Accenture CV says 12.2026; the DHL CV says
   01.2027. This version uses 12.2026. Pick one and make it consistent
   everywhere.

## Status

No placeholders remain — `npm run build` reports zero and confirms one page.
