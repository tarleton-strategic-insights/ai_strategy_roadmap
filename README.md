# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # only needed for --pdf: system wkhtmltopdf too
python build/validate.py           # integrity checks
python build/generate.py           # rebuild pac_retreat/use_cases_analysis.md + pac_report.md (markdown only)
python build/generate.py --pdf     # also render PDFs (not committed; repo is pushed to
                                    # GitHub, which renders markdown natively)
```

## Where things live
- `pac_retreat/sources/` — raw retreat materials (photos, slides, case studies).
  Read-only.
- `pac_retreat/analysis/strategic_insights/cook/use_cases/` — structured source of
  truth (`raw_items.yaml`, `unique_items.yaml`, `personnel.yaml`, `outcomes.yaml`).
  Edit these; the generated docs live at `pac_retreat/` top level, not here.
- `pac_retreat/analysis/strategic_insights/cook/vision_synthesis.yaml` — source of
  truth for the official vision statement quoted in `pac_report.md`.
- `pac_retreat/analysis/strategic_insights/hutyra/` — the authored PAC documents
  (reference).
- `pac_retreat/` (top level) — `pac_report.md` / `use_cases_analysis.md` (build
  output — do not hand-edit) and `vision_statements_analysis.md`
  (vision-statement transcriptions + synopsis).
- `roadmap/` — `open_decisions.md` (what needs adjudication), `resolved_decisions.md`
  (adjudicated decisions, ADR-style), `infrastructure.md` (AI platform catalog),
  `support_organizations.md` (support roles/org units), `post_retreat_discussion.md`,
  `survey.md`. PDFs are gitignored, generated on demand only.
