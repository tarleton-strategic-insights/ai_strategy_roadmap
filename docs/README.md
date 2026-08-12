# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # only needed for --pdf: system wkhtmltopdf too
python build/validate.py           # integrity checks
python build/generate.py           # rebuild pac_retreat/analysis/use_cases_analysis.md + pac_report.md (markdown only)
python build/generate.py --pdf     # also render PDFs (not committed; repo is pushed to
                                    # GitHub, which renders markdown natively)
```

## Where things live
- `pac_report.md` (repo top level) — build output (Introduction, Vision Statement,
  Use Cases). Do not hand-edit.
- `followup_message.md` (repo top level) — PAC-facing follow-up survey draft.
- `pac_retreat/sources/` — raw retreat materials (photos, slides, case studies).
  Read-only.
- `pac_retreat/analysis/` — `use_cases_analysis.md` (build output — do not
  hand-edit) and `vision_statements_analysis.md` (vision-statement transcriptions +
  synopsis).
  - `strategic_insights/cook/use_cases/` — structured source of truth
    (`raw_items.yaml`, `unique_items.yaml`, `personnel.yaml`, `outcomes.yaml`).
    Edit these; the generated docs live one level up, not here.
  - `strategic_insights/cook/vision_synthesis.yaml` — source of truth for the
    official vision statement quoted in `pac_report.md`.
  - `strategic_insights/hutyra/` — the authored PAC documents (reference).
- `roadmap/` — `decisions/open_decisions.md` (what needs adjudication) and
  `decisions/resolved_decisions.md` (adjudicated decisions, ADR-style);
  `resources/infrastructure.md` (AI platform catalog),
  `resources/support_organizations.md` (support roles/org units), and
  `resources/post_retreat_discussion.md`. PDFs are gitignored, generated on demand only.
