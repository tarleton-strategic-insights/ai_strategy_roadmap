#!/usr/bin/env python3
"""
Regenerate use_cases_analysis.md from raw_items.yaml, unique_items.yaml, resources.yaml,
and outcomes.yaml. Also regenerates pac_report.md (Introduction + Vision Statement +
Use Cases, the latter re-deriving the outcome/resource breakdown from those same
files) plus vision_synthesis.yaml.

PDFs are off by default — this repo is pushed to GitHub, which renders markdown
natively, so committed PDFs would just be stale duplicates. Pass --pdf to also render
use_cases_analysis.pdf (styled) and a plain-styled PDF for every other .md in
pac_retreat/ and supporting_materials/other/, e.g. for sharing outside GitHub.

Deps: pip install pyyaml markdown  ;  system: wkhtmltopdf (only needed with --pdf)
Usage: python supporting_materials/code/generate.py [--pdf]

Produces:
  supporting_materials/pac_retreat/analysis/use_cases_analysis.md
  pac_report.md                              (repo top level)
  supporting_materials/pac_retreat/analysis/use_cases_analysis.pdf (only with --pdf; styled)
  <other .md>.pdf                            (only with --pdf; plain default styling)
"""
import sys, subprocess, datetime
from pathlib import Path
import yaml

SUPPORTING = Path(__file__).resolve().parent.parent
ROOT = SUPPORTING.parent
COOK = SUPPORTING / "pac_retreat/analysis/strategic_insights/cook"
DATA = COOK / "use_cases"
ANALYSIS = SUPPORTING / "pac_retreat/analysis"
OUT = ROOT
OTHER = SUPPORTING / "other"
TITLE = "PAC AI Use Case Brainstorm 2026-07-27"
SUBTITLE = ("Source: `pac_retreat/sources/event_artifacts/images/use_cases/` "
            "(9 flip-chart photos from a Gartner-facilitated workshop, breakout "
            "group notes, sent by Drew Doolin, 2026-07-30). "
            "Categorization framework adjudicated — see ADR-8 and ADR-9 in "
            "[resolved_decisions.md](../../other/decisions/resolved_decisions.md).")

def load():
    items = yaml.safe_load((DATA / "raw_items.yaml").read_text())["items"]
    resources = yaml.safe_load((DATA / "resources.yaml").read_text())["resources"]
    outcomes = yaml.safe_load((DATA / "outcomes.yaml").read_text())["outcomes"]
    uniques = yaml.safe_load((DATA / "unique_items.yaml").read_text())["unique_items"]
    return items, resources, outcomes, uniques

def by_group(items):
    groups = {}
    for it in items:
        groups.setdefault(it["group"], []).append(it)
    return groups

def emit_part1(items):
    out = ["## Part 1 — Direct Extraction (enumerated)\n",
           "Defined in "
           "[raw_items.yaml](strategic_insights/cook/use_cases/raw_items.yaml).\n"]
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
           "[unique_items.yaml](strategic_insights/cook/use_cases/unique_items.yaml).\n"]
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

def emit_part3b_resources(resources, uniques):
    out = ["### By Resources\n",
           "Categorize items based on the resources it requires - highlights *HOW* we "
           "do it and informs resource allocation and planning decisions.\n"]
    for rname, rdef in resources.items():
        out.append(f"#### {rdef['label']}\n")
        out.extend(emit_uniques_list(rdef["items"], uniques))
        out.append("")
    return "\n".join(out)

def emit_part3(items, resources, outcomes, uniques):
    out = ["## Part 3 - Categorize\n"
           "We now categorize unique use cases from PAC retreat in two distinct ways "
           "that reveal "
           "important patterns: by outcome and by resources.\n",
           "Defined in "
           "[outcomes.yaml](strategic_insights/cook/use_cases/outcomes.yaml) "
           "and "
           "[resources.yaml](strategic_insights/cook/use_cases/resources.yaml) "
           "using deduplicated (unique) items.\n",
           emit_part3a_outcomes(uniques, outcomes),
           "",
           emit_part3b_resources(resources, uniques)]
    return "\n".join(out)

def build_md(items, resources, outcomes, uniques):
    parts = [f"# {TITLE}", SUBTITLE, "", "---", "",
             emit_part1(items), "---", "",
             emit_part2(items, uniques), "---", "",
             emit_part3(items, resources, outcomes, uniques)]
    return "\n".join(parts) + "\n"

VISION_STATEMENT_COUNT = 7  # distinct statements documented in vision_statements_analysis.md

def emit_report_intro():
    return ("## Introduction\n\n"
            "This report synthesizes the outcomes of Tarleton State's PAC AI strategy "
            "retreat (2026-07-27) into a single reference: our working vision for AI "
            "at the university, and the concrete use cases surfaced at the retreat, "
            "organized by the strategic outcome each serves and the resources needed "
            "to deliver it.\n\n"
            "This report was created by a human+AI team.\n")

def emit_report_vision():
    synthesis = yaml.safe_load((COOK / "vision_synthesis.yaml").read_text())["working_synthesis"]
    return (f"## Vision Statement\n\n> {synthesis}\n\n"
            "See "
            "[vision_statements_analysis.md](supporting_materials/pac_retreat/analysis/vision_statements_analysis.md) for details.\n")

def emit_report_use_cases(items, resources, outcomes, uniques):
    out = ["## Use Cases\n",
           "We analyze all use cases suggested during the PAC retreat by combining "
           "duplicate items then categorizing them in two distinct ways that "
           "reveal important patterns: by outcome and by resources.\n",
           "Note - this section does NOT judge the value/priority of use cases NOR "
           "add missing items ... that will happen later. This section analyzes "
           "only suggestions made during the PAC retreat giving them all equal "
           "weight.\n",
           "See "
           "[use_cases_analysis.md](supporting_materials/pac_retreat/analysis/use_cases_analysis.md) for details.\n",
           emit_part3a_outcomes(uniques, outcomes),
           "",
           emit_part3b_resources(resources, uniques)]
    return "\n".join(out)

def build_report_md(items, resources, outcomes, uniques):
    parts = [emit_report_intro(), "---", "",
             emit_report_vision(), "---", "",
             emit_report_use_cases(items, resources, outcomes, uniques)]
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
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    items, resources, outcomes, uniques = load()
    md = build_md(items, resources, outcomes, uniques)
    md_path = ANALYSIS / "use_cases_analysis.md"
    md_path.write_text(md)
    print(f"wrote {md_path.relative_to(ROOT)}  ({len(items)} items)")

    report_md = build_report_md(items, resources, outcomes, uniques)
    report_path = OUT / "pac_report.md"
    report_path.write_text(report_md)
    print(f"wrote {report_path.relative_to(ROOT)}")

    if "--pdf" in sys.argv:
        pdf_path = md_path.with_suffix(".pdf")
        to_pdf(md_path, pdf_path)
        print(f"wrote {pdf_path.relative_to(ROOT)}")

        other_mds = [report_path]
        other_mds += sorted(p for p in (SUPPORTING / "pac_retreat").rglob("*.md")
                             if p.name != "use_cases_analysis.md")
        other_mds += sorted(OTHER.rglob("*.md"))
        for other_md in other_mds:
            other_pdf = other_md.with_suffix(".pdf")
            to_pdf(other_md, other_pdf, css=PLAIN_CSS)
            print(f"wrote {other_pdf.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
