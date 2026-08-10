# AI Roadmap — Command Center

SI's working repository for Tarleton's AI initiative roadmap. Read `CLAUDE.md` first.

## Quick start
```
pip install pyyaml markdown        # system: wkhtmltopdf
python build/validate.py           # integrity checks
python build/generate.py           # rebuild docs/generated from data/
```

## Where things live
- `data/` — structured source of truth (items, taxonomy, clusters). Edit here.
- `docs/source/` — the four authored PAC documents (reference).
- `docs/generated/` — build outputs. Do not hand-edit.
- `decisions/OPEN_DECISIONS.md` — what still needs adjudication.
- `roadmap/` — iterations, priority-vote results, milestones.
- `hooks/` — parked ideas.
