# AI Roadmap — Command Center

Working repository for Tarleton State University's AI initiative roadmap, owned by the
Strategic Insights (SI) group. This is the single source of truth for the use-case
portfolio, its categorization, the roadmap iterations, and the open decisions that
drive them.

## What this repo is for

The PAC (Presidential Advisory Committee) retreat produced 20+ AI use-case ideas. This
repo (1) holds those ideas as structured, traceable data, (2) maintains the
categorization framework leadership agreed to, (3) keeps that framework aligned with the
executive-facing PAC documents, and (4) tracks the open questions and decisions that
move the roadmap forward iteration by iteration.

## Layout

- `data/` — structured source of truth. Edit these, not the generated docs.
  - `items.yaml` — every use-case idea as a record (provenance ID, source group, text,
    cluster, category, key personnel). IDs (A1–I4) trace to the original flip-chart photos.
  - `taxonomy.yaml` — the category scheme (use-cases / capabilities / framings), the
    three use-case types, their facet profiles, and key-personnel mapping.
  - `clusters.yaml` — de-duplication clusters (repeated ideas grouped across source groups).
- `docs/source/` — authored documents (the four PAC docs; read-only reference).
- `docs/generated/` — build outputs (markdown + PDF). Never hand-edit; regenerate.
- `build/` — the generation pipeline (md -> styled HTML -> PDF).
- `roadmap/` — roadmap iterations, priority-vote results, 90-day milestone sets.
- `decisions/` — adjudicated decisions and the open-decision log (ADR-style).
- `hooks/` — parked ideas to develop later, one file each.

## Core conventions

1. **Data drives docs.** The categorization lives in `data/*.yaml`. Generated documents
   are built from it. If a category changes, change the YAML and rebuild — never patch a
   generated file by hand.
2. **Provenance is sacred.** Every item keeps its A1–I4 ID linking it to a source photo
   group. Never renumber these; they are the audit trail. Display/ordinal numbering
   (use-case 1/2/3) is separate and *may* change.
3. **Alignment with PAC docs is tracked, not assumed.** The executive PAC documents use a
   three-**bucket** framework. This repo's categories map to those buckets but are not
   identical. `decisions/OPEN_DECISIONS.md` tracks every known divergence awaiting
   adjudication. Do not silently "fix" a divergence — surface it.
4. **Nothing gets dropped.** Every source item lands in exactly one category. If an item
   fits nowhere, that is a signal to revisit the taxonomy, not to discard the item.

## The categorization framework (current state)

Items partition into three top-level kinds:

- **Use-cases** — resourceable work, split by the scarce *key personnel* each depends on:
  1. Workforce development — organizers (wide & deep coordination on structure)
  2. Curriculum integration — subject-matter experts (narrow & deep on content)
  3. AI solution delivery — AI engineers (narrow & deep on technical)
- **Capabilities / Foundation** — cross-cutting preconditions (governance, security,
  advisory board); not sorted by personnel.
- **Framings** — strategic lenses and models (Extend/Defend/Upend; the "AI Competitive
  Flywheel"); consume no resources.

See `data/taxonomy.yaml` for the authoritative definition and `decisions/OPEN_DECISIONS.md`
for unresolved framework questions (notably: use-case ordering vs. PAC bucket numbers,
and two contested item placements).

## Relationship to the PAC three-bucket framework

| This repo (use-case) | PAC document (bucket) | Owner |
|---|---|---|
| Workforce development | Bucket 1: Workforce Upskilling | Org lead (TBD); SI advises |
| AI solution delivery | Bucket 2: High-Technical Projects | **SI owns** |
| Curriculum integration | Bucket 3: Curriculum Integration | Academic Affairs (TBD); SI advises |
| Capabilities / Foundation | Cross-Cutting Foundations | rides along all buckets |
| Framings | (not represented in PAC docs) | — |

**Known ordering conflict:** this repo currently orders use-cases Workforce/Curriculum/
AI-solution (1/2/3); PAC buckets order Workforce/Technical/Curriculum (1/2/3). Slots 2 and
3 are transposed. Unresolved — see OPEN_DECISIONS.

## Build

```
python build/generate.py            # regenerate all docs/generated from data/
```

Requires `markdown` (pip) and `wkhtmltopdf` (system). See `build/generate.py` header.

## Current status

- Categorization: complete draft; 6 alignment/adjudication items open.
- Priority vote: not yet held (immediate next step per PAC exec brief).
- Owners for Buckets 1 & 3: unnamed.
- MLOps/DevOps hire (the last-mile gap): recommended, not yet approved.
