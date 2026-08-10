#!/usr/bin/env python3
"""
Regenerate docs/generated/ from data/*.yaml.

Deps: pip install pyyaml markdown  ;  system: wkhtmltopdf
Usage: python build/generate.py [--no-pdf]

Produces:
  docs/generated/PAC_AI_use_cases_grouped.md
  docs/generated/PAC_AI_use_cases_grouped.pdf   (unless --no-pdf)
"""
import sys, subprocess, datetime
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "generated"
TITLE = "PAC AI Use Case Brainstorm 2026-07-27"
SUBTITLE = ("Source: 9 flip-chart photos from a Gartner-facilitated workshop "
            "(breakout group notes), sent by Drew Doolin, 2026-07-30.")

def load():
    items = yaml.safe_load((DATA / "items.yaml").read_text())["items"]
    tax = yaml.safe_load((DATA / "taxonomy.yaml").read_text())
    clusters = yaml.safe_load((DATA / "clusters.yaml").read_text())["clusters"]
    return items, tax, clusters

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

def emit_part2(items, clusters):
    out = ["## Part 2 — Grouped by Duplication (nothing removed)\n"]
    by_id = {it["id"]: it for it in items}
    for cid, c in clusters.items():
        out.append(f"### {c['label']}")
        for iid in c["items"]:
            out.append(f"- {iid}: {by_id[iid]['text']}")
        out.append("")
    clustered = {iid for c in clusters.values() for iid in c["items"]}
    out.append("### Ungrouped (no duplication cluster)")
    for it in items:
        if it["id"] not in clustered:
            out.append(f"- {it['id']}: {it['text']}")
    out.append("")
    return "\n".join(out)

def emit_part3(items, tax, clusters):
    by_id = {it["id"]: it for it in items}
    out = ["## Part 3 — Categorization\n",
           "Generated from data/. Every item lands in exactly one category "
           "(items with `spans` are cross-listed).\n"]
    types = tax["kinds"]["use_cases"]["types"]
    ordered = sorted(types.items(), key=lambda kv: kv[1]["ordinal"])

    def items_in(cat):
        return [it for it in items if it["category"] == cat or cat in it.get("spans", [])]

    out.append("### Use-cases\n")
    for tname, t in ordered:
        pretty = tname.replace("_", " ").capitalize()
        out.append(f"#### {t['ordinal']}. {pretty}")
        out.append(f"- Key personnel — {t['key_personnel']}")
        for facet in ("structure", "content", "technical"):
            label = f"***{facet.capitalize()}***" if facet == t["load_bearing_facet"] else facet.capitalize()
            out.append(f"- {label}: {t['facets'][facet]}")
        out.append("\nItems:")
        for it in items_in(tname):
            tag = "  *(spans)*" if it.get("spans") else ""
            out.append(f"- {it['id']}: {it['text']}{tag}")
        out.append("")

    for cat, header in (("capabilities_foundation", "Capabilities / Foundation"),
                        ("framings", "Framings")):
        out.append(f"### {header}")
        for it in items_in(cat):
            out.append(f"- {it['id']}: {it['text']}")
        out.append("")
    return "\n".join(out)

def build_md(items, tax, clusters):
    parts = [f"# {TITLE}", SUBTITLE, "", "---", "",
             emit_part1(items), "---", "",
             emit_part2(items, clusters), "---", "",
             emit_part3(items, tax, clusters)]
    return "\n".join(parts) + "\n"

def to_pdf(md_path, pdf_path):
    import markdown
    css = """
    @page { size: letter; margin: 0.9in 0.85in; }
    body { font-family: 'DejaVu Sans', sans-serif; font-size: 10.5pt; line-height: 1.45; }
    h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 4px; }
    h2 { font-size: 15pt; border-bottom: 1px solid #bbb; padding-bottom: 3px; margin-top: 20px; }
    h3 { font-size: 12.5pt; margin-top: 16px; }
    h4 { font-size: 11pt; margin-top: 12px; }
    li { margin-bottom: 2px; } strong, em { color: #000; }
    """
    body = markdown.markdown(md_path.read_text(), extensions=["extra", "sane_lists"])
    html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
    tmp = OUT / "_render.html"
    tmp.write_text(html)
    subprocess.run(["wkhtmltopdf", "--enable-local-file-access", "--encoding", "utf-8",
                    str(tmp), str(pdf_path)], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    tmp.unlink()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    items, tax, clusters = load()
    md = build_md(items, tax, clusters)
    md_path = OUT / "PAC_AI_use_cases_grouped.md"
    md_path.write_text(md)
    print(f"wrote {md_path.relative_to(ROOT)}  ({len(items)} items)")
    if "--no-pdf" not in sys.argv:
        pdf_path = OUT / "PAC_AI_use_cases_grouped.pdf"
        to_pdf(md_path, pdf_path)
        print(f"wrote {pdf_path.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
