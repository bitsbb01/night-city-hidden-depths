#!/usr/bin/env python3
"""Validate authored location definitions; this is a content check, not game runtime code."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCATION_DIR = ROOT / "content" / "locations"


def validate_location(data: dict[str, Any], source: str = "<memory>") -> list[str]:
    errors: list[str] = []
    where = f"{source}: "

    required = ("location_id", "title", "creator", "target_playtime_minutes",
                "layout", "quest", "loot", "save_keys")
    for key in required:
        if key not in data:
            errors.append(f"{where}missing required field {key!r}")
    if errors:
        return errors

    if data["creator"] != "Bitsbb01":
        errors.append(f"{where}creator must remain 'Bitsbb01'")

    layout = data["layout"]
    zones = layout.get("zones", [])
    zone_ids = [zone.get("id") for zone in zones]
    if len(zone_ids) != len(set(zone_ids)):
        errors.append(f"{where}zone ids must be unique")
    if sum(zone.get("minutes", 0) for zone in zones) < data["target_playtime_minutes"]:
        errors.append(f"{where}zone pacing estimates are shorter than target playtime")

    entrances = layout.get("entrances", [])
    destinations = {entry.get("destination") for entry in entrances}
    if len(entrances) < 2:
        errors.append(f"{where}at least two entrances are required")
    if "safehouse" not in destinations:
        errors.append(f"{where}one entrance must lead to the safehouse")
    if not destinations.intersection(zone_ids) - {"safehouse"}:
        errors.append(f"{where}one entrance must lead to a playable hostile area")
    if layout.get("generation_mode") != "select_authored_variant":
        errors.append(f"{where}locations must select from authored layouts")
    if layout.get("procedural_geometry") is not False:
        errors.append(f"{where}procedural geometry is not supported by this content format")

    quest = data["quest"]
    chance = quest.get("hostage_event_chance")
    if not isinstance(chance, (int, float)) or not 0 <= chance <= 1:
        errors.append(f"{where}hostage_event_chance must be between 0 and 1")
    if chance != 0.05:
        errors.append(f"{where}hostage_event_chance must be 0.05 (5%)")
    for captive in ("civilian", "captured_ncpd_officer", "vehicle_painter"):
        if captive not in quest.get("hostage_types", []):
            errors.append(f"{where}missing hostage type {captive!r}")
    if quest.get("special_hostage_once_per_save") is not True:
        errors.append(f"{where}the special hostage must be one-time per save")

    if "badge_roulette" not in data["loot"].get("unique_once_per_save", []):
        errors.append(f"{where}Badge Roulette must be in the once-per-save reward list")
    if data["loot"].get("enemy_custom_weapon_loadouts_require_player_discovery") is not True:
        errors.append(f"{where}enemy custom weapons must require prior player discovery")

    keys = data["save_keys"]
    if len(keys) != len(set(keys)):
        errors.append(f"{where}save keys must be unique")
    for key in ("quiet_track.hostage_roll", "quiet_track.badge_roulette_awarded",
                "quiet_track.painter_rescued"):
        if key not in keys:
            errors.append(f"{where}missing persistent save key {key!r}")

    return errors


def main() -> int:
    files = sorted(LOCATION_DIR.glob("*.json"))
    if not files:
        print(f"ERROR: no location definitions found in {LOCATION_DIR}", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: cannot read JSON: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: top level must be a JSON object")
            continue
        errors.extend(validate_location(data, str(path.relative_to(ROOT))))

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} authored location definition(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
