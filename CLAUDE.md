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
  - `raw_items.yaml` — every use-case idea as a record (provenance ID, source group,
    text). IDs (A1–I4) trace to the original flip-chart photos. Carries no category or
    dedup field — those live solely in categories.yaml/unique_items.yaml, so there is
    nothing here that can fall out of sync with them.
  - `categories.yaml` — sole authoritative category scheme AND membership (use-cases /
    capabilities), the three use-case types, their facet profiles, key-personnel
    mapping, and each category's `items:` list of unique_items IDs (not raw item IDs).
    Every unique_items entry belongs to exactly one category — no spanning.
  - `unique_items.yaml` — sole authoritative deduplication: every raw item appears in
    exactly one entry's `items:` list (multi-item entries are duplicates of the same
    idea; single-item entries are singletons, `label:` = the item's own text). Keys are
    arbitrary sequential slugs (X1, X2, ...), decoupled from content. categories.yaml
    categorizes at this level, not the raw-item level.
- `pac_retreat_sources/post_event_analysis/strategic_insights/hutyra/` — authored
  documents (the four PAC docs; read-only reference).
- `build/` — `validate.py` (integrity checks) and `generate.py` (yaml -> md, always;
  optionally md -> styled HTML -> PDF for every `.md` in `roadmap/` with `--pdf`).
  PDFs are gitignored — this repo is pushed to GitHub, which renders markdown natively,
  so committed PDFs would just be stale duplicates.
- `roadmap/` — `ai_strategy_develop.md` (platform catalog + job roles/org units),
  `open_decisions.md` (what needs adjudication), `resolved_decisions.md` (adjudicated
  decisions, ADR-style), `post_retreat_discussion.md`, `vision_statements_analysis.md`
  (vision-statement transcriptions + synopsis), and `use_cases_analysis.md` (build
  output from the `use_cases/*.yaml` above — never hand-edit; regenerate).

## Core conventions

1. **Data drives docs.** The categorization lives in the `use_cases/*.yaml` files under
   `pac_retreat_sources/.../cook/use_cases/`. Generated documents are built from it. If a
   category changes, change the YAML and rebuild — never patch a generated file by hand.
2. **Provenance is sacred.** Every item keeps its A1–I4 ID linking it to a source photo
   group. Never renumber these; they are the audit trail. Display/ordinal numbering
   (use-case 1/2/3) is separate and *may* change.
3. **Alignment with PAC docs is tracked, not assumed.** The executive PAC documents use a
   three-**bucket** framework. This repo's categories map to those buckets but are not
   identical. `roadmap/open_decisions.md` tracks every known divergence awaiting
   adjudication. Do not silently "fix" a divergence — surface it.
4. **Nothing gets dropped.** Every source item lands in exactly one category. If an item
   fits nowhere, that is a signal to revisit the taxonomy, not to discard the item.

## The categorization framework (current state)

Categorization applies at the **unique_items** (deduplicated) level, not the raw-item
level — every unique_items entry belongs to exactly one category. Where an entry's
member raw items previously disagreed (e.g. a duplicate group mixing a curriculum item
with a workforce item), a single category was chosen by explicit adjudication rather
than split across categories.

Unique items partition into two top-level kinds:

- **Use-cases** — resourceable work, split by the scarce *key personnel* each depends on:
  1. Curriculum integration — subject-matter experts (narrow & deep on content)
  2. Workforce development — organizers (wide & deep coordination on structure)
  3. AI solution delivery — AI engineers (narrow & deep on technical)
- **Capabilities / Foundation** — cross-cutting preconditions (governance, security,
  advisory board); not sorted by personnel.

(A former third top-level kind, **Framings** — strategic lenses/models that consumed no
resources — was removed 2026-08-11: once categorization moved to the unique_items level,
every framings-flavored raw item turned out to be the minority member of a duplicate
group whose majority belonged elsewhere, leaving the category permanently empty.)

See `use_cases/categories.yaml` for the authoritative definition and `roadmap/open_decisions.md`
for unresolved framework questions (notably a lingering ordering divergence vs. PAC bucket
numbers, and two contested item placements).

## Relationship to the PAC three-bucket framework

| This repo (use-case) | PAC document (bucket) | Owner |
|---|---|---|
| Curriculum integration | Bucket 3: Curriculum Integration | Academic Affairs (TBD); SI advises |
| Workforce development | Bucket 1: Workforce Upskilling | Org lead (TBD); SI advises |
| AI solution delivery | Bucket 2: High-Technical Projects | **SI owns** |
| Capabilities / Foundation | Cross-Cutting Foundations | rides along all buckets |

**Ordering vs. PAC buckets:** this repo currently orders use-cases Curriculum/Workforce/
AI-solution (1/2/3); PAC buckets order Workforce/AI-solution/Curriculum (1/2/3) — every
slot differs. This is adjudicated, not an oversight (OD-1, resolved): the repo
deliberately keeps its own internal ordering rather than matching PAC's, and that
internal ordering has itself been revised twice (ADR-1, then ADR-9 in
`roadmap/resolved_decisions.md`) for internal-readability and ownership-signaling reasons
unrelated to PAC alignment. See `roadmap/resolved_decisions.md` for the full history.

## Build

```
python build/generate.py            # regenerate roadmap/use_cases_analysis.md from use_cases/*.yaml
python build/generate.py --pdf      # also render PDFs (gitignored; GitHub renders md natively)
```

`--pdf` requires `markdown` (pip) and `wkhtmltopdf` (system). See `build/generate.py` header.

## Current status

- Categorization: complete draft; 6 alignment/adjudication items open (see `roadmap/open_decisions.md`).
- Priority vote: not yet held (immediate next step per PAC exec brief).
- Owners: Curriculum Integration — Denise Martinez. AI Solution Delivery — Scott Cook.
  Workforce Development still unnamed — see OD-8 in `roadmap/open_decisions.md`.
- MLOps/DevOps hire (the last-mile gap): recommended, not yet approved.
