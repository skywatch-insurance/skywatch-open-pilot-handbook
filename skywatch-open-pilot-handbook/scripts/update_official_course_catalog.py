#!/usr/bin/env python3
"""Build the link-only FAASTeam/AOPA official course catalog from FAA Safety.gov."""

from __future__ import annotations

import html
import json
import re
import urllib.request
from pathlib import Path


SOURCE_URL = "https://www.faasafety.gov/gslac/ALC/ajax_request_alc.aspx?ccatavl=0&view=otherCat&categoryId=15"
COURSE_URL = "https://www.faasafety.gov/gslac/ALC/course_content.aspx?pf=1&preview=true&cID={}"
OUTPUT = Path(__file__).resolve().parents[1] / "references" / "official-course-catalog.yaml"


def text(fragment: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(fragment))).strip()


def main() -> None:
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "SkyWatch-Open-Pilot-Handbook/1.0"})
    page = urllib.request.urlopen(request, timeout=30).read().decode("utf-8", "replace")
    blocks = re.findall(r'<div id="[^"]+_pnlRow".*?(?=<div id="[^"]+_pnlRow"|\Z)', page, re.S)
    records: dict[str, dict[str, str]] = {}
    for block in blocks:
        alc = re.search(r">(ALC-(\d+))</span>", block)
        title = re.search(r'_labelTitle"[^>]*>(.*?)</span>', block, re.S)
        author = re.search(r'_lblAuthor"[^>]*>(.*?)</span>', block, re.S)
        cost = re.search(r'_lblHasCost"[^>]*>(.*?)</span>', block, re.S)
        if not all((alc, title, author, cost)) or text(cost.group(1)).lower() != "free":
            continue
        presenter = text(author.group(1))
        institution = "FAA Safety Team" if "faasteam" in presenter.lower() else "AOPA Air Safety Institute" if "aopa" in presenter.lower() else ""
        if not institution:
            continue
        records[alc.group(1)] = {
            "id": alc.group(1),
            "title": text(title.group(1)),
            "institution": institution,
            "presented_by": presenter,
            "url": COURSE_URL.format(alc.group(2)),
        }

    ordered = sorted(records.values(), key=lambda item: (item["institution"], int(item["id"].split("-")[1])))
    lines = [
        "schema_version: 1",
        "checked_at: 2026-08-10",
        f"source_catalog: {SOURCE_URL}",
        "rights: link-only",
        "access_note: Free at time of review; FAA Safety.gov enrollment or sign-in may be required.",
        "scope_note: This is an institutional catalog, not a claim that every specialty course is part of the fixed-wing private-pilot core.",
        "counts:",
        f"  total: {len(ordered)}",
        f"  faa_safety_team: {sum(x['institution'] == 'FAA Safety Team' for x in ordered)}",
        f"  aopa_air_safety_institute: {sum(x['institution'] == 'AOPA Air Safety Institute' for x in ordered)}",
        "courses:",
    ]
    for item in ordered:
        lines.extend([
            f"  - id: {item['id']}",
            f"    title: {json.dumps(item['title'], ensure_ascii=False)}",
            f"    institution: {json.dumps(item['institution'])}",
            f"    presented_by: {json.dumps(item['presented_by'])}",
            "    access: free-at-review",
            "    kind: institutional-course",
            f"    url: {item['url']}",
        ])
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(ordered)} courses to {OUTPUT}")


if __name__ == "__main__":
    main()
