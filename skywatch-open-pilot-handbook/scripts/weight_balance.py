#!/usr/bin/env python3
"""Teaching-only weight-and-balance arithmetic checker using user-supplied approved data."""

from __future__ import annotations

import argparse
import json


def calculate(stations: list[tuple[str, float, float]], max_weight: float | None = None, forward_cg: float | None = None, aft_cg: float | None = None) -> dict:
    if not stations:
        raise ValueError("At least one station is required")
    if any(weight < 0 for _, weight, _ in stations):
        raise ValueError("Station weights cannot be negative")
    total_weight = sum(weight for _, weight, _ in stations)
    total_moment = sum(weight * arm for _, weight, arm in stations)
    if total_weight <= 0:
        raise ValueError("Total weight must be greater than zero")
    cg = total_moment / total_weight
    checks = {
        "max_weight": None if max_weight is None else total_weight <= max_weight,
        "forward_cg": None if forward_cg is None else cg >= forward_cg,
        "aft_cg": None if aft_cg is None else cg <= aft_cg,
    }
    return {
        "stations": [{"name": n, "weight": w, "arm": a, "moment": round(w * a, 3)} for n, w, a in stations],
        "total_weight": round(total_weight, 3),
        "total_moment": round(total_moment, 3),
        "calculated_cg": round(cg, 3),
        "user_supplied_boundary_checks": checks,
    }


def parse_station(value: str) -> tuple[str, float, float]:
    try:
        name, weight, arm = value.split(",", 2)
        return name.strip(), float(weight), float(arm)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use NAME,WEIGHT,ARM") from exc


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--station", action="append", type=parse_station, required=True, help="Repeat NAME,WEIGHT,ARM; keep units consistent")
    p.add_argument("--max-weight", type=float)
    p.add_argument("--forward-cg", type=float)
    p.add_argument("--aft-cg", type=float)
    a = p.parse_args()
    result = calculate(a.station, a.max_weight, a.forward_cg, a.aft_cg)
    result["warning"] = "Teaching arithmetic only. Use the exact current aircraft weight-and-balance record, approved AFM/POH envelope (which may vary by weight/configuration), and independently verify before flight."
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
