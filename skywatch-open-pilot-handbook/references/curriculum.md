# Private-pilot curriculum

## Contents

1. How to use the curriculum
2. Twelve modules
3. Checkride and proficiency loop
4. Lesson authoring template

## How to use the curriculum

This is a syllabus and retrieval map, not an FAA-approved ground school or graduation certificate. Align study with the current Private Pilot Airplane ACS, current FAA handbooks, regulations, and the user's instructor.

Free Pilot Training supplies the primary 64-lesson sequence. Its captions were reviewed as syllabus inputs on 2026-08-04. The repository does not reproduce transcripts. Use `free-pilot-training-map.yaml` to retrieve the exact lesson URL and module. Use `official-course-catalog.yaml` to find 83 free FAASTeam and 30 free AOPA safety courses, remembering that specialty courses are not automatically part of the fixed-wing core. Use `playlists.yaml` when the learner needs an alternate free explanation.

For each topic:

1. State the learning objective in original words.
2. Teach the stable concept at the learner's level.
3. Link the Free Pilot Training lesson and at least one primary source.
4. Add an alternate explanation only if it resolves a learning gap.
5. Ask two recall questions, one application scenario, and one risk-management question.
6. Identify what must be learned with a CFI or exact aircraft document.
7. Record unresolved questions for the instructor.

## Module 1 — Aerodynamics and aircraft control

**Free Pilot Training lessons:** 1–14.  
**Outcomes:** Explain lift and angle of attack; recognize stalls/spins as angle-of-attack and coordination problems; relate controls, stability, controllability, flaps, turns, load factor, V-speeds, left-turning tendencies, ground effect, and wake turbulence to risk.

**Primary anchors:** PHAK aerodynamics and flight controls; Airplane Flying Handbook; current ACS Areas I, VII, and IX as applicable.

**Practice:** draw force relationships; explain accelerated-stall risk; calculate a simple level-turn load factor with the provided assumptions; build a wake-turbulence avoidance scenario. Do not supply aircraft-specific speeds from memory.

## Module 2 — Airspace and operating environment

**Lessons:** 15–22.  
**Outcomes:** Identify Classes B–G, entry/equipment/communication concepts, special-use and other airspace, and the need to verify current chart, NOTAM, and regulatory information.

**Primary anchors:** current eCFR Title 14; AIM; Chart User's Guide; current charts. Never infer real-time authorization from a static lesson.

## Module 3 — Charts, time, and pilotage

**Lessons:** 23–27.  
**Outcomes:** Work with UTC/Zulu, latitude/longitude, sectional symbols, airport data, safe-altitude planning concepts, and pilotage/dead-reckoning orientation.

**Primary anchors:** Chart User's Guide, AIM, current sectional and Chart Supplement.

## Module 4 — Flight instruments

**Lessons:** 28–34.  
**Outcomes:** Explain gyroscopic/electronic attitude and direction displays, turn instruments, pitot-static system, altimeter errors, magnetic compass behavior, and electronic display training considerations.

**Primary anchors:** PHAK; exact aircraft AFM/POH and avionics manuals. Treat failure indications and procedures as aircraft/equipment-specific.

## Module 5 — Communications and navigation systems

**Lessons:** 35–39.  
**Outcomes:** Prepare standard communication, non-towered calls, ATIS use, VOR concepts, and GPS orientation while distinguishing teaching examples from current ATC instructions or database status.

**Primary anchors:** AIM; current chart data; approved avionics manuals.

## Module 6 — Weather and weather decisions

**Lessons:** 40–46.  
**Outcomes:** Explain atmosphere, reports/forecasts, winds aloft, charts, briefing sources, and major hazards; build a conservative briefing workflow and identify uncertainty.

**Primary anchors:** Aviation Weather Center, FAA aviation weather publications, Flight Service, current official products. Never turn cached knowledge into a go/no-go decision.

## Module 7 — Cross-country planning

**Lessons:** 47–50.  
**Outcomes:** Build and update a nav log, use manual/E6B and electronic calculations, track fuel/time/position, define diversion triggers, and compare plan with reality.

**Primary anchors:** PHAK, AFH, current charts/data, exact AFM/POH. Require instructor review for student cross-country planning.

## Module 8 — Weight, balance, and performance

**Lessons:** 51–52.  
**Outcomes:** Explain weight, moments, CG, envelope, density altitude, takeoff/landing/climb performance, and why interpolation/conditions/model-specific data matter.

**Primary anchors:** exact current aircraft weight-and-balance record and approved AFM/POH. Generic examples are for teaching only. Use `scripts/weight_balance.py` as a transparent arithmetic check, never as final authority.

## Module 9 — Regulations, documents, and maintenance responsibility

**Lessons:** 53–59.  
**Outcomes:** Locate required documents, orient to medical/BasicMed, privileges/limitations, right-of-way and restraint rules, owner/operator maintenance responsibility, NOTAMs, and Chart Supplement use.

**Primary anchors:** current eCFR, FAA medical/BasicMed resources, AIM, FAA Dynamic Regulatory System, exact records and maintenance data. Escalate factual edge cases.

## Module 10 — Aeromedical factors and risk management

**Lesson:** 60 plus safety playlists.  
**Outcomes:** Use IMSAFE, PAVE, 5P, personal minimums, external-pressure recognition, and conservative decision gates; recognize common physiological hazards without diagnosing.

**Primary anchors:** PHAK, ACS risk-management elements, FAASTeam, FAA/NTSB safety material. Personal minimums supplement—not replace—regulation, approved documents, and instructor judgment.

## Module 11 — Airport and aircraft operations

**Lessons:** 61–64.  
**Outcomes:** Orient to basic operation, airport markings/lights, traffic patterns, runway-incursion avoidance, and wind-aware taxi control concepts.

**Primary anchors:** AFH, AIM, current airport data, exact aircraft checklist/AFM/POH, local instructor procedures. Do not turn generic instruction into aircraft-specific operating procedure.

## Module 12 — ACS and practical-test readiness

**Inputs:** all lessons plus the current Private Pilot Airplane ACS.  
**Outcomes:** Map knowledge, risk management, and skills; diagnose gaps; prepare scenario-based oral practice; organize documents and endorsements with the instructor; create a conservative post-checkride proficiency plan.

Do not guarantee endorsement, eligibility, or a practical-test outcome.

## Checkride and proficiency loop

For each ACS task:

1. **Explain:** teach the core concept without notes.
2. **Locate:** find the current primary source.
3. **Apply:** solve a scenario using explicit assumptions.
4. **Manage risk:** identify hazards, mitigations, and decision gates.
5. **Demonstrate with a CFI:** connect knowledge to actual skill.
6. **Debrief:** record what changed and what still requires work.

## Lesson authoring template

```markdown
---
title: Topic
jurisdiction: US-FAA
acs_tasks: []
source_ids: []
video_ids: []
last_source_check: YYYY-MM-DD
review_interval_days: 180
safety_critical: true
reviewer_role: CFI
status: draft|reviewed|needs-review
---

## Learning objectives
## Concept
## Why pilots get this wrong
## Worked teaching example
## Risk-management scenario
## Verify before acting
## Questions for your instructor
## Sources
```
