#!/usr/bin/env python3
"""Transparent private-pilot training budget estimator; not a quote."""

from __future__ import annotations

import argparse
import json


def estimate(
    flight_hours: float,
    aircraft_hourly: float,
    dual_hours: float,
    instructor_hourly: float,
    ground_hours: float,
    supplies: float,
    exams: float,
    contingency_pct: float,
) -> dict:
    values = locals()
    if any(v < 0 for v in values.values()):
        raise ValueError("Inputs cannot be negative")
    if dual_hours > flight_hours:
        raise ValueError("Dual hours cannot exceed total flight hours")
    aircraft = flight_hours * aircraft_hourly
    instruction = (dual_hours + ground_hours) * instructor_hourly
    subtotal = aircraft + instruction + supplies + exams
    contingency = subtotal * contingency_pct / 100
    total = subtotal + contingency
    return {
        "aircraft": round(aircraft, 2),
        "instruction": round(instruction, 2),
        "supplies_and_equipment": round(supplies, 2),
        "exams_and_fees": round(exams, 2),
        "subtotal": round(subtotal, 2),
        "contingency": round(contingency, 2),
        "estimated_total": round(total, 2),
        "estimated_cost_per_flight_hour": round(total / flight_hours, 2) if flight_hours else None,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--flight-hours", type=float, required=True)
    p.add_argument("--aircraft-hourly", type=float, required=True, help="Wet or dry rate as applicable; add fuel separately if dry")
    p.add_argument("--dual-hours", type=float, required=True)
    p.add_argument("--instructor-hourly", type=float, required=True)
    p.add_argument("--ground-hours", type=float, default=10)
    p.add_argument("--supplies", type=float, default=1000)
    p.add_argument("--exams", type=float, default=1000)
    p.add_argument("--contingency-pct", type=float, default=15)
    a = p.parse_args()
    result = estimate(a.flight_hours, a.aircraft_hourly, a.dual_hours, a.instructor_hourly, a.ground_hours, a.supplies, a.exams, a.contingency_pct)
    result["warning"] = "Planning estimate only. Verify current school, aircraft, instructor, fuel, tax, equipment, medical, exam, and retest costs. FAA minimum experience is not a typical completion guarantee."
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
