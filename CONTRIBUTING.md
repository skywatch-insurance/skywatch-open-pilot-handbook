# Contributing

Contributions from pilots, instructors, mechanics, medical examiners, owners, attorneys, accountants, insurers, researchers, and learners are welcome.

## Good contributions

- Correct a factual error and cite the current primary source.
- Add an alternate explanation without copying a creator's work.
- Improve a checklist while preserving approved-document boundaries.
- Add calculator tests, unit checks, or edge cases.
- Map an authoritative or openly licensed resource.
- Report outdated, ambiguous, unsafe, or commercially biased language.

## Required metadata

Every knowledge contribution must state:

- jurisdiction;
- content type: regulation, official guidance, manufacturer data, education, common practice, or estimate;
- direct source URL and document revision/effective date when available;
- date checked;
- whether the change is safety-critical;
- reviewer role needed.

## Do not submit

- Copyrighted transcripts, book pages, charts, images, or course material without documented permission.
- Aircraft-specific limitations or procedures copied from non-public or unverified documents.
- Personal medical, certificate, policy, claim, logbook, or aircraft-identifying data.
- Hidden promotion, affiliate links, paid ranking, or an endorsement claim.
- Definitive medical, legal, tax, airworthiness, or insurance conclusions.

## Review

Safety-critical changes require approval from both a domain reviewer and maintainer. Appropriate domain reviewers include an active CFI/CFII, A&P/IA, AME, aviation attorney, aviation CPA, or licensed insurance professional. A maintainer may label content `needs-review` and keep it out of confident agent responses until review is complete.

Run before opening a pull request:

```bash
python3 skywatch-open-pilot-handbook/scripts/validate_skill.py
python3 -m unittest discover -s skywatch-open-pilot-handbook/tests
```
