# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # only needed for --pdf: system wkhtmltopdf too
python build/validate.py           # integrity checks
python build/generate.py           # rebuild roadmap/use_cases_analysis.md (markdown only)
python build/generate.py --pdf     # also render PDFs (not committed; repo is pushed to
                                    # GitHub, which renders markdown natively)
```

## Where things live
- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/` —
  structured source of truth (`raw_items.yaml`, `unique_items.yaml`, `personnel.yaml`,
  `outcomes.yaml`). Edit these; the generated doc lives in `roadmap/`, not here.
- `pac_retreat_sources/post_event_analysis/strategic_insights/hutyra/` — the authored PAC
  documents (reference).
- `roadmap/` — `open_decisions.md` (what needs adjudication), `resolved_decisions.md`
  (adjudicated decisions, ADR-style), `ai_strategy_develop.md` (platform catalog + job
  roles), `post_retreat_discussion.md`, `vision_statements_analysis.md`
  (vision-statement transcriptions + synopsis), and `use_cases_analysis.md` (build
  output — do not hand-edit). PDFs are gitignored, generated on demand only.
