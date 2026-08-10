#!/usr/bin/env python3
"""Check registry URLs and report failures; no third-party packages required."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def urls() -> list[str]:
    found: list[str] = []
    for rel in ["references/sources.yaml", "references/playlists.yaml"]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        found.extend(re.findall(r"^\s+url: (https://\S+)\s*$", text, re.M))
    return list(dict.fromkeys(found))


def check(url: str, timeout: float) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "OpenPilotSourceCheck/0.1", "Range": "bytes=0-1024"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return 200 <= response.status < 400, str(response.status)
    except urllib.error.HTTPError as exc:
        # 401/403/429 can mean the source exists but blocks automation; flag separately.
        if exc.code in {401, 403, 429}:
            return True, f"reachable-but-automation-limited:{exc.code}"
        return False, f"http:{exc.code}"
    except Exception as exc:  # Network errors must be visible, not crash the whole check.
        return False, f"{type(exc).__name__}:{exc}"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--timeout", type=float, default=15)
    p.add_argument("--limit", type=int, default=0, help="Check only the first N URLs; 0 checks all")
    args = p.parse_args()
    targets = urls()[: args.limit or None]
    failures = 0
    for url in targets:
        ok, detail = check(url, args.timeout)
        print(("OK" if ok else "FAIL"), detail, url)
        failures += not ok
    print(f"Checked {len(targets)} URLs; failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
