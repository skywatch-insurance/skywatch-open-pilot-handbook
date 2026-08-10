#!/usr/bin/env python3
"""Transparent annual aircraft ownership cost estimator; not professional advice."""

from __future__ import annotations

import argparse
import json


def estimate(
    annual_hours: float,
    fuel_burn_gph: float,
    fuel_price: float,
    oil_hourly: float,
    maintenance_hourly: float,
    engine_reserve_hourly: float,
    prop_reserve_hourly: float,
    insurance_annual: float,
    storage_annual: float,
    annual_inspection_base: float,
    subscriptions_annual: float,
    financing_annual: float,
    other_fixed: float,
    contingency_pct: float,
) -> dict:
    values = locals()
    if any(v < 0 for v in values.values()):
        raise ValueError("Inputs cannot be negative")
    fuel = annual_hours * fuel_burn_gph * fuel_price
    variable_other = annual_hours * (oil_hourly + maintenance_hourly + engine_reserve_hourly + prop_reserve_hourly)
    variable = fuel + variable_other
    fixed = insurance_annual + storage_annual + annual_inspection_base + subscriptions_annual + financing_annual + other_fixed
    subtotal = variable + fixed
    contingency = subtotal * contingency_pct / 100
    total = subtotal + contingency
    return {
        "annual_hours": annual_hours,
        "fuel": round(fuel, 2),
        "other_variable_and_reserves": round(variable_other, 2),
        "total_variable": round(variable, 2),
        "total_fixed": round(fixed, 2),
        "contingency": round(contingency, 2),
        "estimated_annual_total": round(total, 2),
        "estimated_monthly_average": round(total / 12, 2),
        "estimated_per_flight_hour": round(total / annual_hours, 2) if annual_hours else None,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    for name, help_text in [
        ("annual-hours", "Expected flight hours"), ("fuel-burn-gph", "Fuel burn in gallons per hour"),
        ("fuel-price", "Price per gallon"), ("insurance-annual", "Current planning estimate, not a quote"),
        ("storage-annual", "Hangar or tie-down"), ("annual-inspection-base", "Base inspection only; discrepancies separate")]:
        p.add_argument(f"--{name}", type=float, required=True, help=help_text)
    p.add_argument("--oil-hourly", type=float, default=0)
    p.add_argument("--maintenance-hourly", type=float, default=0)
    p.add_argument("--engine-reserve-hourly", type=float, default=0)
    p.add_argument("--prop-reserve-hourly", type=float, default=0)
    p.add_argument("--subscriptions-annual", type=float, default=0)
    p.add_argument("--financing-annual", type=float, default=0, help="Annual interest/fees included in this planning view")
    p.add_argument("--other-fixed", type=float, default=0)
    p.add_argument("--contingency-pct", type=float, default=15)
    a = p.parse_args()
    result = estimate(**{k: v for k, v in vars(a).items()})
    result["warning"] = "Planning estimate only. It excludes acquisition cash, tax, depreciation, opportunity cost, upgrades, and any items not entered. Maintenance, financing, tax, and insurance require current professional inputs."
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
