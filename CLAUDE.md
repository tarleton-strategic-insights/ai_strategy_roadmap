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

- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/use_cases/` —
  structured source of truth. Edit these, not the generated docs.
  - `items.yaml` — every use-case idea as a record (provenance ID, source group, text,
    cluster, category, key personnel). IDs (A1–I4) trace to the original flip-chart photos.
  - `taxonomy.yaml` — the category scheme (use-cases / capabilities / framings), the
    three use-case types, their facet profiles, and key-personnel mapping.
  - `clusters.yaml` — de-duplication clusters (repeated ideas grouped across source groups).
  - `use_cases_analysis.md` / `.pdf` — build outputs. Never hand-edit; regenerate.
- `pac_retreat_sources/post_event_analysis/strategic_insights/cook/vision statements/` —
  vision-statement transcriptions (from retreat flip charts) and cross-statement synopsis.
- `pac_retreat_sources/post_event_analysis/strategic_insights/hutyra/` — authored
  documents (the four PAC docs; read-only reference).
- `build/` — `validate.py` (integrity checks) and `generate.py` (the generation
  pipeline: yaml -> md -> styled HTML -> PDF).
- `roadmap/` — `ai_infrastructure.md` (platform catalog + job roles/org units),
  `OPEN_DECISIONS.md` (adjudicated decisions and the open-decision log, ADR-style),
  `post_retreat_discussion.md`.

## Core conventions

1. **Data drives docs.** The categorization lives in the `use_cases/*.yaml` files under
   `pac_retreat_sources/.../cook/use_cases/`. Generated documents are built from it. If a
   category changes, change the YAML and rebuild — never patch a generated file by hand.
2. **Provenance is sacred.** Every item keeps its A1–I4 ID linking it to a source photo
   group. Never renumber these; they are the audit trail. Display/ordinal numbering
   (use-case 1/2/3) is separate and *may* change.
3. **Alignment with PAC docs is tracked, not assumed.** The executive PAC documents use a
   three-**bucket** framework. This repo's categories map to those buckets but are not
   identical. `roadmap/OPEN_DECISIONS.md` tracks every known divergence awaiting
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

See `use_cases/taxonomy.yaml` for the authoritative definition and `roadmap/OPEN_DECISIONS.md`
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
python build/generate.py            # regenerate use_cases_analysis.md/.pdf from use_cases/*.yaml
```

Requires `markdown` (pip) and `wkhtmltopdf` (system). See `build/generate.py` header.

## Current status

- Categorization: complete draft; 6 alignment/adjudication items open.
- Priority vote: not yet held (immediate next step per PAC exec brief).
- Owners for Buckets 1 & 3: unnamed.
- MLOps/DevOps hire (the last-mile gap): recommended, not yet approved.
