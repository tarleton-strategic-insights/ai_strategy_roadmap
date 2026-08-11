#!/usr/bin/env python3
"""
Integrity checks on the use-case data. Run before committing or building.
Usage: python build/validate.py   (exit 0 = clean, 1 = problems)
"""
import sys, re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases"
VALID_CATS = {"workforce_development", "curriculum_integration", "ai_solution_delivery",
              "capabilities_foundation"}
ID_RE = re.compile(r"^[A-I]\d+$")

def main():
    items = yaml.safe_load((DATA / "raw_items.yaml").read_text())["items"]
    uniques = yaml.safe_load((DATA / "unique_items.yaml").read_text())["unique_items"]
    cats = yaml.safe_load((DATA / "categories.yaml").read_text())
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

    # 3. categories.yaml is well-formed and every unique_items entry belongs to
    #    exactly one category (nothing dropped, nothing double-categorized).
    #    categories.yaml is authoritative; raw_items.yaml carries no category field.
    cat_defs = dict(cats["kinds"]["use_cases"]["types"])
    cat_defs["capabilities_foundation"] = cats["kinds"]["capabilities_foundation"]
    if set(cat_defs) != VALID_CATS:
        errors.append(f"categories.yaml kinds {set(cat_defs)} != VALID_CATS {VALID_CATS}")
    cat_seen = {}
    for cname, cdef in cat_defs.items():
        for uid in cdef["items"]:
            if uid not in uniques:
                errors.append(f"category {cname} references missing unique_items entry {uid}")
            elif uid in cat_seen:
                errors.append(f"unique_items {uid}: appears in both {cat_seen[uid]} and {cname}")
            else:
                cat_seen[uid] = cname
    for uid in uniques:
        if uid not in cat_seen:
            errors.append(f"unique_items {uid}: not listed in any category")

    # 4. surface OPEN placement questions as warnings
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
