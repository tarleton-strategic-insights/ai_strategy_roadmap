#!/usr/bin/env python3
"""
Integrity checks on the use-case data. Run before committing or building.
Usage: python build/validate.py   (exit 0 = clean, 1 = problems)
"""
import sys, re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "pac_retreat/analysis/strategic_insights/cook/use_cases"
VALID_PERSONNEL_CATEGORIES = {"workforce_development", "curriculum_integration", "ai_solution_delivery",
                              "capabilities_foundation"}
ID_RE = re.compile(r"^[A-I]\d+$")

def check_axis(axis_name, axis_defs, uniques, errors):
    """Every unique_items entry must belong to exactly one group in this axis."""
    seen = {}
    for gname, gdef in axis_defs.items():
        for uid in gdef["items"]:
            if uid not in uniques:
                errors.append(f"{axis_name} {gname} references missing unique_items entry {uid}")
            elif uid in seen:
                errors.append(f"unique_items {uid}: appears in both {seen[uid]!r} and {gname!r} in {axis_name}")
            else:
                seen[uid] = gname
    for uid in uniques:
        if uid not in seen:
            errors.append(f"unique_items {uid}: not listed in any {axis_name} group")

def main():
    items = yaml.safe_load((DATA / "raw_items.yaml").read_text())["items"]
    uniques = yaml.safe_load((DATA / "unique_items.yaml").read_text())["unique_items"]
    personnel = yaml.safe_load((DATA / "personnel.yaml").read_text())
    outcomes = yaml.safe_load((DATA / "outcomes.yaml").read_text())["outcomes"]
    errors, warnings = [], []

    # 1. unique, well-formed IDs
    seen = {}
    for it in items:
        iid = it.get("id", "")
        if not ID_RE.match(iid):
            errors.append(f"malformed id: {iid!r}")
        if iid in seen:
            errors.append(f"duplicate id: {iid}")
        seen[iid] = it

    # 2. unique_items.yaml references resolve, and every raw item lands in exactly
    #    one entry (multi-item entries are duplicates; single-item entries are
    #    singletons — nothing is dropped, nothing double-counted).
    dedup_seen = {}
    for uid, u in uniques.items():
        for iid in u["items"]:
            if iid not in seen:
                errors.append(f"unique_items entry {uid} references missing item {iid}")
            elif iid in dedup_seen:
                errors.append(f"{iid}: appears in both {dedup_seen[iid]} and {uid}")
            else:
                dedup_seen[iid] = uid
    for iid in seen:
        if iid not in dedup_seen:
            errors.append(f"{iid}: not listed in any unique_items entry")

    # 3. personnel.yaml is well-formed and every unique_items entry belongs to
    #    exactly one personnel category (nothing dropped, nothing double-assigned).
    #    personnel.yaml is authoritative; raw_items.yaml carries no personnel field.
    pers_defs = dict(personnel["kinds"]["use_cases"]["types"])
    pers_defs["capabilities_foundation"] = personnel["kinds"]["capabilities_foundation"]
    if set(pers_defs) != VALID_PERSONNEL_CATEGORIES:
        errors.append(f"personnel.yaml kinds {set(pers_defs)} != VALID_PERSONNEL_CATEGORIES {VALID_PERSONNEL_CATEGORIES}")
    check_axis("personnel", pers_defs, uniques, errors)

    # 4. outcomes.yaml is well-formed and every unique_items entry belongs to exactly
    #    one outcome (independent axis from personnel — see outcomes.yaml header).
    check_axis("outcome", outcomes, uniques, errors)

    # 5. surface OPEN placement questions as warnings
    for it in items:
        if "(OPEN)" in (it.get("note") or ""):
            warnings.append(f"{it['id']}: OPEN placement — {it['note']}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(items)} items, {len(uniques)} unique_items entries, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
