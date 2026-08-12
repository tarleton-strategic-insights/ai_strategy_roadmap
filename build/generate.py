#!/usr/bin/env python3
"""
Regenerate use_cases_analysis.md from raw_items.yaml, unique_items.yaml, personnel.yaml,
and outcomes.yaml. Also regenerates pac_report.md (Introduction + Vision Statement +
Use Cases, the latter re-deriving the outcome/personnel breakdown from those same
files) plus vision_synthesis.yaml.

PDFs are off by default — this repo is pushed to GitHub, which renders markdown
natively, so committed PDFs would just be stale duplicates. Pass --pdf to also render
use_cases_analysis.pdf (styled) and a plain-styled PDF for every other .md in roadmap/,
e.g. for sharing outside GitHub.

Deps: pip install pyyaml markdown  ;  system: wkhtmltopdf (only needed with --pdf)
Usage: python build/generate.py [--pdf]

Produces:
  roadmap/use_cases_analysis.md
  roadmap/pac_report.md
  roadmap/use_cases_analysis.pdf        (only with --pdf; styled)
  roadmap/<other .md>.pdf               (only with --pdf; plain default styling)
"""
import sys, subprocess, datetime
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
COOK = ROOT / "pac_retreat_sources/post_event_analysis/strategic_insights/cook"
DATA = COOK / "use_cases"
OUT = ROOT / "roadmap"
TITLE = "PAC AI Use Case Brainstorm 2026-07-27"
SUBTITLE = ("Source: `pac_retreat_sources/event_artifacts/images/use_cases/` "
            "(9 flip-chart photos from a Gartner-facilitated workshop, breakout "
            "group notes, sent by Drew Doolin, 2026-07-30). "
            "Categorization framework adjudicated — see ADR-8 and ADR-9 in "
            "[resolved_decisions.md](resolved_decisions.md).")

def load():
    items = yaml.safe_load((DATA / "raw_items.yaml").read_text())["items"]
    personnel = yaml.safe_load((DATA / "personnel.yaml").read_text())
    outcomes = yaml.safe_load((DATA / "outcomes.yaml").read_text())["outcomes"]
    uniques = yaml.safe_load((DATA / "unique_items.yaml").read_text())["unique_items"]
    return items, personnel, outcomes, uniques

def by_group(items):
    groups = {}
    for it in items:
        groups.setdefault(it["group"], []).append(it)
    return groups

def emit_part1(items):
    out = ["## Part 1 — Direct Extraction (enumerated)\n",
           "Defined in "
           "[raw_items.yaml](../pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/raw_items.yaml).\n"]
    for g, its in sorted(by_group(items).items()):
        out.append(f"### Group {g}")
        for i, it in enumerate(its, 1):
            out.append(f"{i}. {it['id']}: {it['text']}")
        out.append("")
    return "\n".join(out)

def emit_part2(items, uniques):
    out = ["## Part 2 — Deduplicated (nothing removed; every item lands in exactly "
           "one entry below)\n",
           "Defined in "
           "[unique_items.yaml](../pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/unique_items.yaml).\n"]
    by_id = {it["id"]: it for it in items}
    for uid, u in uniques.items():
        out.append(f"### {u['label']}")
        for iid in u["items"]:
            out.append(f"- {iid}: {by_id[iid]['text']}")
        out.append("")
    return "\n".join(out)

def emit_uniques_list(items_list, uniques):
    out = []
    for uid in items_list:
        u = uniques[uid]
        n = len(u["items"])
        out.append(f"- {u['label']} ({n} raw item{'s' if n != 1 else ''})")
    return out

def emit_part3a_outcomes(uniques, outcomes):
    out = ["### By Outcomes\n",
           "Categorize items based on the outcome it serves - highlights *WHY* we do "
           "it and connects to the broader Tarleton strategic plan.\n"]
    for oname, odef in outcomes.items():
        out.append(f"#### {odef['label']}\n")
        out.extend(emit_uniques_list(odef["items"], uniques))
        out.append("")
    return "\n".join(out)

def emit_roles(role_list):
    out = []
    for role in role_list:
        out.append(f"    - {role['title']}")
        for desc in role.get("descriptions", []):
            out.append(f"        - {desc}")
        if "ai_expertise" in role:
            out.append(f"        - AI expertise: {role['ai_expertise']}")
    return out

def emit_personnel_category(label, cat_def, uniques):
    out = [f"#### {label}", ""]
    if "champions" in cat_def:
        out.append("- Champions")
        for name in cat_def["champions"]:
            out.append(f"    - {name}")
    out.append("- Leaders")
    out.extend(emit_roles(cat_def["leaders"]))
    out.append("- Doers")
    out.extend(emit_roles(cat_def["doers"]))
    out.append("- Items")
    for uid in cat_def["items"]:
        u = uniques[uid]
        n = len(u["items"])
        out.append(f"    - {u['label']} ({n} raw item{'s' if n != 1 else ''})")
    return out

def emit_part3b_personnel(personnel, uniques):
    out = ["### By Personnel\n",
           "Categorize items based on the personnel it requires - highlights *HOW* we "
           "do it and informs resource allocation and planning decisions.\n"]
    types = personnel["kinds"]["use_cases"]["types"]
    ordered = sorted(types.items(), key=lambda kv: kv[1]["ordinal"])

    for tname, t in ordered:
        out.extend(emit_personnel_category(t["label"], t, uniques))
        out.append("")

    foundation = personnel["kinds"]["capabilities_foundation"]
    out.extend(emit_personnel_category(foundation["label"], foundation, uniques))
    return "\n".join(out)

def emit_part3(items, personnel, outcomes, uniques):
    out = ["## Part 3 - Categorize\n"
           "We now categorize unique use cases from PAC retreat in two distinct ways "
           "that each reveal "
           "important patterns: by outcome and by personnel.\n",
           "Defined in "
           "[outcomes.yaml](../pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/outcomes.yaml) "
           "and "
           "[personnel.yaml](../pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/personnel.yaml) "
           "using deduplicated (unique) items.\n",
           emit_part3a_outcomes(uniques, outcomes),
           "",
           emit_part3b_personnel(personnel, uniques)]
    return "\n".join(out)

def build_md(items, personnel, outcomes, uniques):
    parts = [f"# {TITLE}", SUBTITLE, "", "---", "",
             emit_part1(items), "---", "",
             emit_part2(items, uniques), "---", "",
             emit_part3(items, personnel, outcomes, uniques)]
    return "\n".join(parts) + "\n"

VISION_STATEMENT_COUNT = 7  # distinct statements documented in vision_statements_analysis.md

def emit_roadmap_intro():
    return ("## Introduction\n\n"
            "This roadmap synthesizes the outcomes of Tarleton State's PAC AI strategy "
            "retreat (2026-07-27) into a single reference: our working vision for AI "
            "at the university, and the concrete use cases surfaced at the retreat, "
            "organized by the strategic outcome each serves and the personnel needed "
            "to deliver it.\n")

def emit_roadmap_vision():
    synthesis = yaml.safe_load((COOK / "vision_synthesis.yaml").read_text())["working_synthesis"]
    return (f"## Vision Statement\n\n> {synthesis}\n\n"
            f"This synthesis of the {VISION_STATEMENT_COUNT} original vision statements "
            "was created by a human+AI team. See "
            "[vision_statements_analysis.md](vision_statements_analysis.md) for details.\n")

def emit_roadmap_use_cases(items, personnel, outcomes, uniques):
    out = ["## Use Cases\n",
           "We analyze all use cases suggested during the PAC retreat by combining "
           "duplicate items then categorizing them in two distinct ways that each "
           "reveal important patterns: by outcome and by personnel.\n",
           f"This synthesis of the {len(items)} suggested use cases was created by a "
           "human+AI team. See "
           "[use_cases_analysis.md](use_cases_analysis.md) for details.\n",
           emit_part3a_outcomes(uniques, outcomes),
           "",
           emit_part3b_personnel(personnel, uniques)]
    return "\n".join(out)

def build_roadmap_md(items, personnel, outcomes, uniques):
    parts = [emit_roadmap_intro(), "---", "",
             emit_roadmap_vision(), "---", "",
             emit_roadmap_use_cases(items, personnel, outcomes, uniques)]
    return "\n".join(parts) + "\n"

STYLED_CSS = """
@page { size: letter; margin: 0.9in 0.85in; }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 10.5pt; line-height: 1.45; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
h2 { font-size: 15pt; border-bottom: 1px solid #bbb; padding-bottom: 3px; margin-top: 20px; }
h3 { font-size: 12.5pt; margin-top: 16px; }
h4 { font-size: 11pt; margin-top: 12px; }
li { margin-bottom: 2px; } strong, em { color: #000; }
"""

# Plain default styling (browser-default-ish) for markdown files that aren't
# generated docs — logs, tables, notes. No custom fonts/spacing/rules.
PLAIN_CSS = """
@page { size: letter; margin: 1in; }
body { font-family: sans-serif; font-size: 12pt; }
table { border-collapse: collapse; }
td, th { border: 1px solid #ccc; padding: 4px 8px; }
"""

def to_pdf(md_path, pdf_path, css=STYLED_CSS):
    import markdown
    body = markdown.markdown(md_path.read_text(), extensions=["extra", "sane_lists"])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
    tmp = OUT / "_render.html"
    tmp.write_text(html)
    import os
    local_bin = ROOT / ".venv/tools/extracted/usr/local/bin/wkhtmltopdf"
    wkhtmltopdf = os.environ.get("WKHTMLTOPDF") or (str(local_bin) if local_bin.exists() else "wkhtmltopdf")
    subprocess.run([wkhtmltopdf, "--enable-local-file-access", "--encoding", "utf-8",
                    str(tmp), str(pdf_path)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tmp.unlink()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items, personnel, outcomes, uniques = load()
    md = build_md(items, personnel, outcomes, uniques)
    md_path = OUT / "use_cases_analysis.md"
    md_path.write_text(md)
    print(f"wrote {md_path.relative_to(ROOT)}  ({len(items)} items)")

    roadmap_md = build_roadmap_md(items, personnel, outcomes, uniques)
    roadmap_path = OUT / "pac_report.md"
    roadmap_path.write_text(roadmap_md)
    print(f"wrote {roadmap_path.relative_to(ROOT)}")

    if "--pdf" in sys.argv:
        pdf_path = OUT / "use_cases_analysis.pdf"
        to_pdf(md_path, pdf_path)
        print(f"wrote {pdf_path.relative_to(ROOT)}")

        for other_md in sorted(OUT.glob("*.md")):
            if other_md.name == "use_cases_analysis.md":
                continue
            other_pdf = other_md.with_suffix(".pdf")
            to_pdf(other_md, other_pdf, css=PLAIN_CSS)
            print(f"wrote {other_pdf.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
