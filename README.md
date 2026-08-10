# SkyWatch Open Pilot Handbook

**From first lesson to first year of ownership.**

The Open Pilot Handbook is an open-source, source-first aviation knowledge project and portable AI skill for US general aviation. It helps prospective pilots, students, certificated pilots, renters, instructors, buyers, and first-year owners learn concepts, plan decisions, use practical tools, and find the current authority that controls.

> **Important:** This project is educational. It is not a substitute for current regulations, NOTAMs, weather products, approved aircraft documents, a CFI/CFII, DPE, AME, A&P/IA, attorney, CPA, lender, title/escrow professional, or licensed insurance representative. It does not make go/no-go, airworthiness, medical, legal, tax, or coverage decisions.

## What is here

- [`skywatch-open-pilot-handbook/SKILL.md`](skywatch-open-pilot-handbook/SKILL.md): the portable agent skill.
- [`skywatch-open-pilot-handbook/references/curriculum.md`](skywatch-open-pilot-handbook/references/curriculum.md): 12-module private-pilot syllabus.
- [`skywatch-open-pilot-handbook/references/free-pilot-training-map.yaml`](skywatch-open-pilot-handbook/references/free-pilot-training-map.yaml): all 64 Free Pilot Training lessons mapped into the syllabus.
- [`skywatch-open-pilot-handbook/references/playlists.yaml`](skywatch-open-pilot-handbook/references/playlists.yaml): additional free curriculum, safety, weather, and ownership playlists.
- [`skywatch-open-pilot-handbook/references/free-learning-catalog.yaml`](skywatch-open-pilot-handbook/references/free-learning-catalog.yaml): 199 credited free video lessons and institutional learning hubs, each linked to its original publisher.
- [`CREDITS.md`](CREDITS.md): human-readable creator and institutional attribution.
- [`skywatch-open-pilot-handbook/references/pilot-journeys.md`](skywatch-open-pilot-handbook/references/pilot-journeys.md): discovery flight through post-checkride proficiency.
- [`skywatch-open-pilot-handbook/references/ownership-journey.md`](skywatch-open-pilot-handbook/references/ownership-journey.md): rent/club/own through the first year.
- [`skywatch-open-pilot-handbook/assets/templates`](skywatch-open-pilot-handbook/assets/templates): reusable checklists and worksheets.
- [`skywatch-open-pilot-handbook/scripts`](skywatch-open-pilot-handbook/scripts): transparent planning calculators and validators.

## Install

Copy the `skywatch-open-pilot-handbook` folder into the skills directory used by your agent. The skill intentionally keeps detailed material in `references/` so agents load only what a question requires.

Generic installation:

```bash
cp -R skywatch-open-pilot-handbook /path/to/your/skills/
```

Then ask:

```text
Use $skywatch-open-pilot-handbook to build a realistic six-month private-pilot training plan.
Use $skywatch-open-pilot-handbook to compare renting, a flying club, and ownership for my mission.
Use $skywatch-open-pilot-handbook to create questions for an A&P before a pre-buy inspection.
```

## Current scope

- Jurisdiction: United States / FAA.
- Certificate foundation: private pilot airplane.
- Ownership focus: common light general-aviation aircraft.
- Status: `v0.1-layout`; educational framework and tools are usable, but individual curriculum lessons remain open for expert-authored expansion and review.

## Content and transcript rights

Free Pilot Training and other creator videos are used as syllabus inputs, links, and discovery sources. Their transcripts and videos are not redistributed here. Publicly viewable content is not automatically open-licensed. Any future transcript-derived publication requires documented permission or a compatible license in the rights ledger.

## Contribute

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Safety-critical changes require a domain reviewer and maintainer. Every consequential claim needs a current source, jurisdiction, checked date, and content classification.

## Maintainer and attribution

Created and maintained by [SkyWatch](https://www.skywatch.ai/) with community contributors. SkyWatch is an aviation insurance provider and has a commercial interest in serving pilots and aircraft owners. Educational content must remain vendor-neutral; commercial links must be optional and clearly labeled.

## License

Original repository text, code, and templates are licensed under Apache-2.0 unless a file says otherwise. Third-party names, videos, transcripts, images, approved aircraft documents, and linked material remain the property of their respective owners.
