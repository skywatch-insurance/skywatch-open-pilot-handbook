#!/usr/bin/env python3
"""Build the credited free-learning catalog from original publisher pages."""

from __future__ import annotations

import json
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "references" / "free-learning-catalog.yaml"

VIDEO_COLLECTIONS = [
    {
        "id": "free-pilot-training-instrument",
        "url": "https://www.youtube.com/playlist?list=PLKGcDgymP_oZ618l5ebEnDIpqOrrTwboI",
        "creator": "Free Pilot Training",
        "creator_url": "https://www.youtube.com/@FreePilotTraining",
        "jurisdiction": "US-FAA",
        "role": "instrument-rating-supplement",
        "credibility": "Established aviation-training creator; verify consequential claims against current FAA sources.",
    },
    {
        "id": "king-schools-free-private-pilot",
        "url": "https://www.youtube.com/playlist?list=PLQTup63Foj4Si57jzEUT-KGtbaAsjkbAE",
        "creator": "King Schools",
        "creator_url": "https://www.youtube.com/@KingSchools",
        "jurisdiction": "US-FAA",
        "role": "private-pilot-supplement",
        "credibility": "Long-established US flight-training publisher; videos are supplemental and the current FAA authority controls.",
    },
    {
        "id": "free-pilot-ground-school-channel",
        "url": "https://www.youtube.com/@freepilotgroundschool2326/videos",
        "creator": "Free Pilot Ground School",
        "creator_url": "https://www.youtube.com/@freepilotgroundschool2326",
        "jurisdiction": "mixed-or-unspecified",
        "role": "topic-explanation-supplement",
        "credibility": "Structured aviation ground-school library; confirm jurisdiction and verify against FAA sources before US operational use.",
    },
]

INSTITUTIONAL_HUBS = [
    {
        "id": "faa-pilot-training",
        "title": "Pilot Training and Study Materials",
        "creator": "Federal Aviation Administration",
        "url": "https://www.faa.gov/pilots/training",
        "creator_url": "https://www.faa.gov/",
        "kind": "official-learning-hub",
        "jurisdiction": "US-FAA",
    },
    {
        "id": "faa-faasteam-wings",
        "title": "FAASTeam Courses and WINGS Pilot Proficiency Program",
        "creator": "Federal Aviation Administration Safety Team",
        "url": "https://www.faa.gov/faasteam",
        "creator_url": "https://www.faa.gov/faasteam",
        "kind": "official-course-hub",
        "jurisdiction": "US-FAA",
    },
    {
        "id": "faa-airman-education",
        "title": "Airman Education Programs",
        "creator": "Federal Aviation Administration",
        "url": "https://www.faa.gov/pilots/training/airman_education",
        "creator_url": "https://www.faa.gov/",
        "kind": "official-course-hub",
        "jurisdiction": "US-FAA",
    },
    {
        "id": "aopa-asi-online-learning",
        "title": "Air Safety Institute Online Learning",
        "creator": "AOPA Air Safety Institute",
        "url": "https://www.aopa.org/training-and-safety/online-learning",
        "creator_url": "https://www.aopa.org/training-and-safety/air-safety-institute",
        "kind": "institutional-learning-hub",
        "jurisdiction": "US-focused",
    },
    {
        "id": "aopa-asi-safety-centers",
        "title": "Air Safety Institute Safety Centers",
        "creator": "AOPA Air Safety Institute",
        "url": "https://www.aopa.org/training-and-safety/air-safety-institute/safety-centers",
        "creator_url": "https://www.aopa.org/training-and-safety/air-safety-institute",
        "kind": "institutional-learning-hub",
        "jurisdiction": "US-focused",
    },
    {
        "id": "eaa-proficiency-education",
        "title": "Pilot Proficiency and Education Programs",
        "creator": "Experimental Aircraft Association",
        "url": "https://www.eaa.org/eaa/pilots/eaa-pilot-proficiency/proficiency-and-education-programs",
        "creator_url": "https://www.eaa.org/",
        "kind": "institutional-learning-hub",
        "jurisdiction": "US-focused",
    },
    {
        "id": "ntsb-general-aviation-safety",
        "title": "General Aviation Safety Resources",
        "creator": "National Transportation Safety Board",
        "url": "https://www.ntsb.gov/Advocacy/safety-alerts/Pages/default.aspx",
        "creator_url": "https://www.ntsb.gov/",
        "kind": "official-safety-learning-hub",
        "jurisdiction": "US",
    },
    {
        "id": "noaa-jetstream",
        "title": "JetStream Online School for Weather",
        "creator": "NOAA National Weather Service",
        "url": "https://www.noaa.gov/jetstream",
        "creator_url": "https://www.noaa.gov/",
        "kind": "official-weather-learning-hub",
        "jurisdiction": "US",
    },
    {
        "id": "nasa-beginners-guide-aeronautics",
        "title": "Beginner's Guide to Aeronautics",
        "creator": "NASA Glenn Research Center",
        "url": "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/",
        "creator_url": "https://www.nasa.gov/glenn/",
        "kind": "official-aeronautics-learning-hub",
        "jurisdiction": "general-science",
    },
]


def quoted(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def fetch_collection(collection: dict[str, str]) -> tuple[str, list[dict[str, str]]]:
    process = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--dump-single-json", collection["url"]],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(process.stdout)
    entries = []
    for entry in data.get("entries", []):
        video_id = entry.get("id")
        title = (entry.get("title") or "").strip()
        if not video_id or not title:
            continue
        entries.append({"id": video_id, "title": title, "url": f"https://www.youtube.com/watch?v={video_id}"})
    return data.get("title") or collection["id"], entries


def main() -> int:
    checked = date.today().isoformat()
    lines = [
        "schema_version: 1",
        f"checked: {checked}",
        "catalog_policy: Credited links and metadata only. Creator media and transcripts are not redistributed.",
        "authority_policy: Educational media supplements the 64-lesson syllabus; current primary sources control consequential claims.",
        "counting_policy: Counts individual free video lessons and institutional learning hubs, not 100 separate approved ground schools.",
        "collections:",
    ]
    resources: list[dict[str, str]] = []
    for collection in VIDEO_COLLECTIONS:
        title, entries = fetch_collection(collection)
        lines.extend(
            [
                f"  - id: {collection['id']}",
                f"    title: {quoted(title)}",
                f"    creator: {quoted(collection['creator'])}",
                f"    creator_url: {collection['creator_url']}",
                f"    collection_url: {collection['url']}",
                f"    jurisdiction: {collection['jurisdiction']}",
                f"    role: {collection['role']}",
                f"    credibility_note: {quoted(collection['credibility'])}",
                "    access: free-at-check",
                "    rights: link-only",
                f"    item_count: {len(entries)}",
            ]
        )
        for entry in entries:
            resources.append(
                {
                    **entry,
                    "collection_id": collection["id"],
                    "collection_title": title,
                    "collection_url": collection["url"],
                    "creator": collection["creator"],
                    "creator_url": collection["creator_url"],
                    "jurisdiction": collection["jurisdiction"],
                    "kind": "video-lesson",
                }
            )

    resources.extend(INSTITUTIONAL_HUBS)
    lines.extend([f"total_resources: {len(resources)}", "resources:"])
    for index, resource in enumerate(resources, start=1):
        resource_id = resource.get("id") or f"resource-{index}"
        lines.extend(
            [
                f"  - catalog_number: {index}",
                f"    id: {resource_id}",
                f"    title: {quoted(resource['title'])}",
                f"    creator: {quoted(resource['creator'])}",
                f"    creator_url: {resource['creator_url']}",
                f"    url: {resource['url']}",
                f"    kind: {resource['kind']}",
                f"    jurisdiction: {resource['jurisdiction']}",
                "    access: free-at-check",
                "    rights: link-only",
            ]
        )
        if "collection_id" in resource:
            lines.extend(
                [
                    f"    collection_id: {resource['collection_id']}",
                    f"    collection_title: {quoted(resource['collection_title'])}",
                    f"    collection_url: {resource['collection_url']}",
                ]
            )

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {OUTPUT}: {len(resources)} credited free resources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
