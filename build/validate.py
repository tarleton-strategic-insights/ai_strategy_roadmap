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
              "capabilities_foundation", "framings"}
ID_RE = re.compile(r"^[A-I]\d+$")

def main():
    items = yaml.safe_load((DATA / "items.yaml").read_text())["items"]
    clusters = yaml.safe_load((DATA / "clusters.yaml").read_text())["clusters"]
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

    # 2. every item has a valid category (nothing dropped, nothing miscategorized)
    for it in items:
        if it.get("category") not in VALID_CATS:
            errors.append(f"{it['id']}: bad category {it.get('category')!r}")
        for s in it.get("spans", []):
            if s not in VALID_CATS:
                errors.append(f"{it['id']}: bad span {s!r}")

    # 3. cluster references resolve, and item.cluster agrees with clusters.yaml
    cluster_members = {}
    for cid, c in clusters.items():
        for iid in c["items"]:
            if iid not in seen:
                errors.append(f"cluster {cid} references missing item {iid}")
            cluster_members[iid] = cid
    for it in items:
        declared = it.get("cluster")
        actual = cluster_members.get(it["id"])
        if declared != actual:
            errors.append(f"{it['id']}: cluster mismatch (item says {declared}, clusters.yaml says {actual})")

    # 4. surface OPEN placement questions as warnings
    for it in items:
        if "(OPEN)" in (it.get("note") or ""):
            warnings.append(f"{it['id']}: OPEN placement — {it['note']}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(items)} items, {len(clusters)} clusters, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
