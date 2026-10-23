#!/usr/bin/env python3
"""Validate authored quest flow graphs; this is a content check, not game runtime code."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUEST_DIR = ROOT / "content" / "quests"


def validate_quest_flow(data: dict[str, Any], source: str = "<memory>") -> list[str]:
    errors: list[str] = []
    where = f"{source}: "

    for key in ("quest_id", "title", "creator", "start_node", "terminal_nodes", "nodes", "save_facts"):
        if key not in data:
            errors.append(f"{where}missing required field {key!r}")
    if errors:
        return errors

    if data["creator"] != "Bitsbb01":
        errors.append(f"{where}creator must remain 'Bitsbb01'")

    nodes = data["nodes"]
    if not isinstance(nodes, list) or not nodes:
        return errors + [f"{where}nodes must be a non-empty list"]

    node_ids = [node.get("id") for node in nodes if isinstance(node, dict)]
    if len(node_ids) != len(nodes):
        errors.append(f"{where}each node must be an object with an id")
        return errors
    if any(not isinstance(node_id, str) or not node_id for node_id in node_ids):
        errors.append(f"{where}node ids must be non-empty strings")
        return errors
    if len(node_ids) != len(set(node_ids)):
        errors.append(f"{where}node ids must be unique")

    by_id = {node["id"]: node for node in nodes}
    start = data["start_node"]
    terminals = data["terminal_nodes"]
    if start not in by_id:
        errors.append(f"{where}start_node must name an existing node")
        return errors
    if by_id[start].get("type") != "start":
        errors.append(f"{where}start_node must have type 'start'")
    if not isinstance(terminals, list) or not terminals:
        errors.append(f"{where}at least one terminal node is required")
        return errors

    for terminal in terminals:
        if terminal not in by_id:
            errors.append(f"{where}terminal node {terminal!r} does not exist")
        elif by_id[terminal].get("type") != "terminal":
            errors.append(f"{where}terminal node {terminal!r} must have type 'terminal'")

    for node in nodes:
        edges = node.get("next")
        if not isinstance(edges, list):
            errors.append(f"{where}node {node['id']!r} next must be a list")
            continue
        for target in edges:
            if target not in by_id:
                errors.append(f"{where}node {node['id']!r} points to missing node {target!r}")
        if node.get("type") == "terminal" and edges:
            errors.append(f"{where}terminal node {node['id']!r} must not have outgoing edges")

    if any(error.startswith(where) and "missing node" in error for error in errors):
        return errors

    reachable: set[str] = set()
    pending = [start]
    while pending:
        current = pending.pop()
        if current in reachable or current not in by_id:
            continue
        reachable.add(current)
        pending.extend(by_id[current].get("next", []))
    unreachable = set(node_ids) - reachable
    if unreachable:
        errors.append(f"{where}all quest nodes must be reachable; unreachable: {', '.join(sorted(unreachable))}")

    facts = data["save_facts"]
    if not isinstance(facts, list) or not all(isinstance(fact, str) and fact for fact in facts):
        errors.append(f"{where}save_facts must be a list of non-empty strings")
    elif len(facts) != len(set(facts)):
        errors.append(f"{where}save facts must be unique")

    return errors


def main() -> int:
    files = sorted(QUEST_DIR.glob("*.json"))
    if not files:
        print(f"ERROR: no quest flow definitions found in {QUEST_DIR}", file=sys.stderr)
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
        errors.extend(validate_quest_flow(data, str(path.relative_to(ROOT))))

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(files)} authored quest flow definition(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
