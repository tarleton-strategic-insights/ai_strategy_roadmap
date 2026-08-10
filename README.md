# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # system: wkhtmltopdf
python build/validate.py           # integrity checks
python build/generate.py           # rebuild the grouped-use-cases doc
```

## Where things live
- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/` —
  structured source of truth (`items.yaml`, `taxonomy.yaml`, `clusters.yaml`) plus the
  generated `PAC_AI_use_cases_grouped.md`/`.pdf`. Edit the yaml; the md/pdf are build
  outputs — do not hand-edit.
- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/vision statements/` —
  vision-statement transcriptions and synopsis.
- `pac_retreat_sources/post_event_analysis/strategic_insights/hutyra/` — the authored PAC
  documents (reference).
- `roadmap/` — `OPEN_DECISIONS.md` (what needs adjudication), `ai_infrastructure.md`
  (platform catalog + job roles), `post_retreat_discussion.md`.
