# SkyWatch Open Pilot Handbook

## Open-source aviation knowledge to turbocharge AI assistants

Turn ChatGPT, Claude, Cursor, or another compatible AI agent into a better aviation learning co-pilot, grounded in FAA sources and built for pilots from their first lesson through aircraft ownership.

The handbook does not try to make an AI sound like an aviation encyclopedia. It gives the assistant a source policy, a structured curriculum, verified free resources, practical tools, stage-based sequencing, and aviation-specific safety boundaries. The result is an answer that is easier to verify and act on.

## See the difference

These prompts are designed to test what the skill uniquely changes. Run the identical prompt with the skill disabled and enabled, using the same model on the same day.

### 1. Turn “study more” into the right next four weeks

```text
I'm a 28-hour private-pilot student. I can perform the basic maneuvers and land consistently, but I struggle with VFR cross-country planning and radio confidence. Build my next four weeks of study and flight preparation using only free resources. Give me exact links, readiness gates, and what I should deliberately postpone.
```

**Without the skill:** expect a broad ground-school checklist covering many subjects, generic resource suggestions, and no clear exit criteria.

**With SkyWatch Co-Pilot:** expect a stage-specific sequence, only the relevant curriculum modules, credited lesson links, instructor-review points, measurable readiness gates, and lower-priority subjects explicitly deferred.

### 2. Replace plausible recommendations with exact resources

```text
Give me the exact free video lessons and free FAA courses that cover VFR cross-country nav-log construction. Links, not descriptions.
```

**Without the skill:** an assistant may suggest a general playlist, broad FAA handbooks, or plausible-looking resources that still need manual verification.

**With SkyWatch Co-Pilot:** it can retrieve the mapped Free Pilot Training cross-country lessons and the FAASTeam “Student Pilot VFR Navigation Planning” course, identify the original publishers, and provide the cataloged links instead of guessing from memory.

### 3. Make calculations auditable

```text
Front seats 340 lb at arm 37, rear seats 170 lb at 73, baggage 60 lb at 95, fuel 40 gal, and empty weight 1,480 lb at 39.5. Show the complete weight-and-balance calculation with every station, moment, total, CG, units, and assumptions. Then tell me exactly what aircraft-specific documents I must verify before using the result.
```

**Without the skill:** expect prose arithmetic and a conclusion that may blur a teaching calculation with an aircraft-specific determination.

**With SkyWatch Co-Pilot:** expect the included calculator's auditable station-by-station output, visible units and assumptions, and a precise verification step using that aircraft's current approved records.

More demo guidance and ready-to-record scripts are in [DEMO_PROMPTS.md](DEMO_PROMPTS.md).

> **Important:** This project is educational. It is not a substitute for current regulations, NOTAMs, weather products, approved aircraft documents, a CFI/CFII, DPE, AME, A&P/IA, attorney, CPA, lender, title/escrow professional, or licensed insurance representative. It does not make go/no-go, airworthiness, medical, legal, tax, or coverage decisions.

## What is here

- [`skywatch-open-pilot-handbook/SKILL.md`](skywatch-open-pilot-handbook/SKILL.md): the portable agent skill.
- [`skywatch-open-pilot-handbook/references/curriculum.md`](skywatch-open-pilot-handbook/references/curriculum.md): 12-module private-pilot syllabus.
- [`skywatch-open-pilot-handbook/references/free-pilot-training-map.yaml`](skywatch-open-pilot-handbook/references/free-pilot-training-map.yaml): all 64 Free Pilot Training lessons mapped into the syllabus.
- [`skywatch-open-pilot-handbook/references/official-course-catalog.yaml`](skywatch-open-pilot-handbook/references/official-course-catalog.yaml): 113 free FAA Safety Team and AOPA Air Safety Institute courses, credited and linked to their FAA catalog pages.
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

The public website is maintained in Webflow. See [WEBFLOW_MAINTENANCE.md](WEBFLOW_MAINTENANCE.md) for the page location, editing model, and staging-first publishing workflow.

## Maintainer and attribution

Created and maintained by [SkyWatch](https://www.skywatch.ai/) with community contributors. SkyWatch is an aviation insurance provider and has a commercial interest in serving pilots and aircraft owners. Educational content must remain vendor-neutral; commercial links must be optional and clearly labeled.

## License

Original repository text, code, and templates are licensed under Apache-2.0 unless a file says otherwise. Third-party names, videos, transcripts, images, approved aircraft documents, and linked material remain the property of their respective owners.
