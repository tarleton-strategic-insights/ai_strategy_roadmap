# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # system: wkhtmltopdf
python build/validate.py           # integrity checks
python build/generate.py           # rebuild roadmap/use_cases_analysis.md + PDFs for roadmap/*.md
```

## Where things live
- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/` —
  structured source of truth (`raw_items.yaml`, `categories.yaml`, `unique_items.yaml`).
  Edit these; the generated doc lives in `roadmap/`, not here.
- `pac_retreat_sources/post_event_analysis/strategic_insights/hutyra/` — the authored PAC
  documents (reference).
- `roadmap/` — `open_decisions.md` (what needs adjudication), `resolved_decisions.md`
  (adjudicated decisions, ADR-style), `ai_strategy_develop.md` (platform catalog + job
  roles), `post_retreat_discussion.md`, `vision_statements_analysis.md`
  (vision-statement transcriptions + synopsis), and `use_cases_analysis.md`/`.pdf` (build
  output — do not hand-edit). Every `.md` here gets a matching `.pdf` on build.
