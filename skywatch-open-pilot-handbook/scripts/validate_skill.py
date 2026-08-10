#!/usr/bin/env python3
"""Validate Open Pilot structure and high-value safety invariants without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, errors: list[str]) -> str:
    p = ROOT / path
    if not p.is_file():
        errors.append(f"missing file: {path}")
        return ""
    return p.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    skill = require("SKILL.md", errors)
    if not re.match(r"^---\nname: skywatch-open-pilot-handbook\ndescription: .+\n---\n", skill):
        errors.append("SKILL.md frontmatter must contain only name and single-line description")
    for phrase in ["Do not make a live go/no-go decision", "actual policy", "approved checklist/AFM/POH", "jurisdiction"]:
        if phrase.lower() not in skill.lower():
            errors.append(f"SKILL.md missing safety invariant: {phrase}")

    required_refs = [
        "references/curriculum.md", "references/free-pilot-training-map.yaml", "references/playlists.yaml",
        "references/source-policy.md", "references/sources.yaml", "references/safety-boundaries.md",
        "references/pilot-journeys.md", "references/ownership-journey.md", "references/tool-catalog.md",
    ]
    for path in required_refs:
        require(path, errors)

    mapping = require("references/free-pilot-training-map.yaml", errors)
    numbers = [int(n) for n in re.findall(r"- \{n: (\d+),", mapping)]
    ids = re.findall(r"- \{n: \d+, id: ([^,]+),", mapping)
    if numbers != list(range(1, 65)):
        errors.append("Free Pilot Training map must contain lessons 1–64 in order")
    if len(ids) != 64 or len(set(ids)) != 64:
        errors.append("Free Pilot Training map must contain 64 unique video IDs")

    playlists = require("references/playlists.yaml", errors)
    if len(re.findall(r"^  - id:", playlists, re.M)) < 10:
        errors.append("Playlist registry must contain at least 10 vetted playlists")
    if "rights:" not in playlists or "checked:" not in playlists:
        errors.append("Playlist registry needs rights and checked metadata")

    templates = list((ROOT / "assets" / "templates").glob("*.md"))
    if len(templates) < 10:
        errors.append("At least 10 reusable templates are required")

    boundary = require("references/safety-boundaries.md", errors).lower()
    for topic in ["medical", "legal", "tax", "insurance", "maintenance", "privacy", "emergency"]:
        if topic not in boundary:
            errors.append(f"Safety boundaries missing topic: {topic}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION PASSED: 64 mapped lessons, {len(templates)} templates, source and safety policies present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
