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

## Document lineage

Every document in this repo traces back to raw retreat/survey material through a chain
of synthesis. Starting from the culminating document and working backward:

1. **[`AI_strategy_and_roadmap.md`](../AI_strategy_and_roadmap.md)** — the culminating
   document. Hand-authored strategy and roadmap: org structure, staffing, gap
   analysis, infrastructure, open questions. Builds on both documents below.
2. **[`pac_report.md`](../pac_report.md)** and **[`survey_analysis.md`](../survey_analysis.md)**
   — the immediately preceding documents.
   - `pac_report.md` synthesizes `use_cases_analysis.md` and
     `vision_statements_analysis.md` (below) into a single PAC-facing reference.
   - `survey_analysis.md` analyzes `prioritization/survey_results.csv`, the raw
     responses to the follow-up survey drafted in `prioritization/survey_message.md`.
3. **`pac_retreat/analysis/use_cases_analysis.md`** and
   **`pac_retreat/analysis/vision_statements_analysis.md`** — generated/hand-maintained
   analysis one level further back.
   - `use_cases_analysis.md` is generated from the YAML source of truth in
     `strategic_insights/cook/use_cases/`: `raw_items.yaml` (every retreat idea) →
     `unique_items.yaml` (deduplicated) → `resources.yaml` / `outcomes.yaml` (the two
     categorization axes).
   - `vision_statements_analysis.md` transcribes the vision-statement photos and
     records the adjudicated synthesis, sourced from
     `strategic_insights/cook/vision_synthesis.yaml`.
4. **`pac_retreat/sources/`** — the raw retreat materials this whole chain ultimately
   derives from: flip-chart photos, workshop slides, and pre-event case-study
   research. Read-only; never edited.

## Where things live
- `pac_report.md` (repo top level) — build output (Introduction, Vision Statement,
  Use Cases). Do not hand-edit.
- `AI_strategy_and_roadmap.md` (repo top level) — hand-authored sequel to
  `pac_report.md`: org structure, staffing (including the Champions/Leaders/Doers
  role detail, no longer generated), gap analysis, infrastructure, and an "Open
  Questions" section. Working draft; not generated; edit directly.
- `survey_analysis.md` (repo top level) — hand-authored analysis of the follow-up
  survey responses, not generated.
- `prioritization/` — `survey_message.md` (PAC-facing follow-up survey draft) and
  `survey_results.csv` (raw export).
- `pac_retreat/sources/` — raw retreat materials (photos, slides, case studies).
  Read-only.
- `pac_retreat/analysis/` — `use_cases_analysis.md` (build output — do not
  hand-edit) and `vision_statements_analysis.md` (vision-statement transcriptions +
  synopsis).
  - `strategic_insights/cook/use_cases/` — structured source of truth
    (`raw_items.yaml`, `unique_items.yaml`, `resources.yaml`, `outcomes.yaml`).
    Edit these; the generated docs live one level up, not here.
  - `strategic_insights/cook/vision_synthesis.yaml` — source of truth for the
    official vision statement quoted in `pac_report.md`.
  - `strategic_insights/hutyra/` — the authored PAC documents (reference).
- `roadmap/` — `decisions/open_decisions.md` (what needs adjudication) and
  `decisions/resolved_decisions.md` (adjudicated decisions, ADR-style);
  `resources/infrastructure.md` (AI platform catalog),
  `resources/support_organizations.md` (support roles/org units), and
  `resources/post_retreat_discussion.md`. PDFs are gitignored, generated on demand only.
