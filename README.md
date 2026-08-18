# SkyWatch Open Pilot Handbook

## Give your AI an aviation learning system

SkyWatch Co-Pilot is an open-source skill that turns ChatGPT, Claude, Cursor, or another compatible AI agent into a better aviation learning partner, grounded in FAA sources and built for pilots from their first lesson through aircraft ownership.

## See what the skill changes

These prompts are designed to test what the skill uniquely changes. Run the identical prompt with the skill disabled and enabled, using the same model on the same day.

### 1. Turn “study more” into the right next four weeks

```text
I'm a 28-hour private-pilot student. I can perform the basic maneuvers and land consistently, but I struggle with VFR cross-country planning and radio confidence. Build my next four weeks of study and flight preparation using only free resources. Give me exact links, readiness gates, and what I should deliberately postpone.
```

**Without the skill — representative answer:**

> Review navigation, weather, regulations, and radio procedures. Use a free online ground-school course, practice radio calls, and plan a cross-country with your instructor. Fly regularly and adjust the plan based on your progress.

**With SkyWatch Co-Pilot — representative answer:**

> **Week 1: Build and explain a paper nav log**
>
> Study [Free Pilot Training Lesson 47: Cross-Country Navigation Log with Calculations](https://www.youtube.com/watch?v=Ydvev6B7IaY). Build one route, then explain every heading, time, fuel, and checkpoint entry to your CFI.
>
> **Readiness gate:** complete a second nav log without prompts and reconcile it with your instructor.
>
> **Week 2: Make the calculations fluent**
>
> Study [Lesson 48: Guide to the E6B Flight Computer](https://www.youtube.com/watch?v=L8ORGN6zZog), then calculate wind correction, groundspeed, time, and fuel for the same route.
>
> **Readiness gate:** independently reproduce the calculations and identify any implausible result.
>
> **Week 3: Connect planning to FAA decision-making**
>
> Complete [FAASTeam ALC-481: Student Pilot VFR Navigation Planning](https://www.faasafety.gov/gslac/ALC/course_content.aspx?pf=1&preview=true&cID=481). Chair-fly the route and rehearse the radio calls with your CFI.
>
> **Week 4:** fly the scenario with your instructor and debrief against the plan.
>
> **Postpone for now:** unrelated ownership and advanced-instrument material. Your bottleneck is cross-country planning and radio workload.

### 2. Replace plausible recommendations with exact resources

```text
Give me the exact free video lessons and free FAA courses that cover VFR cross-country nav-log construction. Links, not descriptions.
```

**Without the skill — representative answer:**

> Try a free private-pilot ground-school playlist on YouTube and review the FAA Pilot's Handbook of Aeronautical Knowledge chapters on navigation and flight planning.

**With SkyWatch Co-Pilot — representative answer:**

> Here is the shortest relevant sequence from the handbook's verified catalog:
>
> 1. [Lesson 47: Cross-Country Navigation Log with Calculations](https://www.youtube.com/watch?v=Ydvev6B7IaY) — Free Pilot Training
> 2. [Lesson 48: Guide to the E6B Flight Computer](https://www.youtube.com/watch?v=L8ORGN6zZog) — Free Pilot Training
> 3. [Lesson 49: Electronic Alternatives to the E6B](https://www.youtube.com/watch?v=QXz9sMUdbZ0) — Free Pilot Training
> 4. [Lesson 50: Flying a Cross-Country with a Navigation Log](https://www.youtube.com/watch?v=2tIYJyRldzM) — Free Pilot Training
> 5. [ALC-481: Student Pilot VFR Navigation Planning](https://www.faasafety.gov/gslac/ALC/course_content.aspx?pf=1&preview=true&cID=481) — FAA Safety Team
>
> I selected only resources mapped to nav-log construction and credited each original publisher.

### 3. Make calculations auditable

```text
Front seats 340 lb at arm 37, rear seats 170 lb at 73, baggage 60 lb at 95, fuel 40 gal, and empty weight 1,480 lb at 39.5. Show the complete weight-and-balance calculation with every station, moment, total, CG, units, and assumptions. Then tell me exactly what aircraft-specific documents I must verify before using the result.
```

**Without the skill — representative answer:**

> Your total weight is 2,290 lb. Add each moment and divide by total weight to find the CG, then compare it with the aircraft's approved envelope.

**With SkyWatch Co-Pilot — representative answer:**

> **I cannot complete this calculation safely yet: the fuel arm is missing.** I will not assume an aircraft-specific value.
>
> Known subtotal before fuel: **2,050 lb** and **89,150 lb-in**. Fuel weight is **240 lb** using the stated 40 US gal and the teaching assumption of 6 lb/gal, but its moment and the final CG require the fuel arm.
>
> Retrieve the fuel arm from this aircraft's current approved weight-and-balance records or applicable POH/AFM. Also verify the current empty weight and moment, station arms, loading limits, fuel density used, and the applicable CG envelope. Once supplied, I can run the included calculator and return an auditable station-by-station table. A CFI or appropriately qualified person should verify the result before operational use.

That is the difference: not a larger aviation encyclopedia dump, but a staged learning plan, exact credited resources, auditable tools, and clear boundaries when required information is missing.

## How the skill creates the difference

The handbook gives the assistant a source policy, a structured curriculum, verified free resources, practical tools, stage-based sequencing, and aviation-specific safety boundaries. The result is an answer that is easier to verify and act on.

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
