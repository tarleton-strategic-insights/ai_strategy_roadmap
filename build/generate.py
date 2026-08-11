#!/usr/bin/env python3
"""
Regenerate use_cases_analysis.md from raw_items.yaml, categories.yaml, unique_items.yaml.

PDFs are off by default — this repo is pushed to GitHub, which renders markdown
natively, so committed PDFs would just be stale duplicates. Pass --pdf to also render
use_cases_analysis.pdf (styled) and a plain-styled PDF for every other .md in roadmap/,
e.g. for sharing outside GitHub.

Deps: pip install pyyaml markdown  ;  system: wkhtmltopdf (only needed with --pdf)
Usage: python build/generate.py [--pdf]

Produces:
  roadmap/use_cases_analysis.md
  roadmap/use_cases_analysis.pdf        (only with --pdf; styled)
  roadmap/<other .md>.pdf               (only with --pdf; plain default styling)
"""
import sys, subprocess, datetime
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases"
OUT = ROOT / "roadmap"
TITLE = "PAC AI Use Case Brainstorm 2026-07-27"
SUBTITLE = ("Source: 9 flip-chart photos from a Gartner-facilitated workshop "
            "(breakout group notes), sent by Drew Doolin, 2026-07-30.")

def load():
    items = yaml.safe_load((DATA / "raw_items.yaml").read_text())["items"]
    cats = yaml.safe_load((DATA / "categories.yaml").read_text())
    uniques = yaml.safe_load((DATA / "unique_items.yaml").read_text())["unique_items"]
    return items, cats, uniques

def by_group(items):
    groups = {}
    for it in items:
        groups.setdefault(it["group"], []).append(it)
    return groups

def emit_part1(items):
    out = ["## Part 1 — Direct Extraction (enumerated)\n"]
    for g, its in sorted(by_group(items).items()):
        out.append(f"### Group {g}")
        for i, it in enumerate(its, 1):
            out.append(f"{i}. {it['id']}: {it['text']}")
        out.append("")
    return "\n".join(out)

def emit_part2(items, uniques):
    out = ["## Part 2 — Deduplicated (nothing removed; every item lands in exactly "
           "one entry below)\n"]
    by_id = {it["id"]: it for it in items}
    for uid, u in uniques.items():
        out.append(f"### {u['label']}")
        for iid in u["items"]:
            out.append(f"- {iid}: {by_id[iid]['text']}")
        out.append("")
    return "\n".join(out)

def emit_part3(items, cats, uniques):
    out = ["## Part 3 — Categorization\n",
           "Generated from the use_cases yaml. Membership is defined in categories.yaml "
           "at the deduplicated (unique_items) level — every unique_items entry belongs "
           "to exactly one category.\n"]
    types = cats["kinds"]["use_cases"]["types"]
    ordered = sorted(types.items(), key=lambda kv: kv[1]["ordinal"])

    def emit_uniques_in(cat_def):
        for uid in cat_def["items"]:
            u = uniques[uid]
            n = len(u["items"])
            out.append(f"- {u['label']} ({n} raw item{'s' if n != 1 else ''})")

    out.append("### Use-cases\n")
    for tname, t in ordered:
        pretty = tname.replace("_", " ").capitalize().replace("Ai ", "AI ")
        out.append(f"#### {t['ordinal']}. {pretty}")
        out.append(f"- Key personnel — {t['key_personnel']}")
        for facet in ("structure", "content", "technical"):
            label = f"***{facet.capitalize()}***" if facet == t["load_bearing_facet"] else facet.capitalize()
            out.append(f"- {label}: {t['facets'][facet]}")
        out.append("\nItems:")
        emit_uniques_in(t)
        out.append("")

    out.append("### Capabilities / Foundation")
    emit_uniques_in(cats["kinds"]["capabilities_foundation"])
    out.append("")
    return "\n".join(out)

def build_md(items, cats, uniques):
    parts = [f"# {TITLE}", SUBTITLE, "", "---", "",
             emit_part1(items), "---", "",
             emit_part2(items, uniques), "---", "",
             emit_part3(items, cats, uniques)]
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
    items, cats, uniques = load()
    md = build_md(items, cats, uniques)
    md_path = OUT / "use_cases_analysis.md"
    md_path.write_text(md)
    print(f"wrote {md_path.relative_to(ROOT)}  ({len(items)} items)")
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
