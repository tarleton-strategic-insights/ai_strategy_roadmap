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

- `docs/` — `README.md` (quick start, this layout section) and `CLAUDE.md` (this
  file). Moved out of the repo top level so a visitor landing on the GitHub repo page
  isn't confused by internal working docs; the top-level `README.md` is a short stub
  pointing here.
- `pac_report.md` (repo top level) — build output: Introduction + Vision Statement +
  Use Cases (the latter re-deriving the outcome/resource breakdown from
  `use_cases/*.yaml`). Never hand-edit; regenerate. Lives at top level (not under
  `pac_retreat/`) because it's the primary PAC-facing deliverable.
- `AI_strategy_and_roadmap.md` (repo top level) — hand-authored sequel to
  `pac_report.md`, moving from "what was surfaced" to "how we act on it":
  prioritization, org structure, staffing (including the Champions/Leaders/Doers
  role detail per resource category — no longer generated, lives here natively),
  milestones, budget, governance. Not generated; edit directly, never regenerate.
- `followup_message.md` (repo top level) — PAC-facing follow-up survey draft.
- `pac_retreat/sources/` — raw retreat materials (flip-chart photos, slides, pre-event
  case-study research). Read-only reference; never edited.
- `pac_retreat/analysis/` — structured source of truth and its generated/hand-authored
  analysis docs.
  - `use_cases_analysis.md` — build output (Parts 1–3 of use-case extraction,
    dedup, and categorization). Never hand-edit; regenerate.
  - `vision_statements_analysis.md` — vision-statement transcriptions + synopsis,
    hand-maintained except the Synthesized Vision Statement quote.
  - `strategic_insights/cook/use_cases/` — structured source of truth. Edit these,
    not the generated docs.
    - `raw_items.yaml` — every use-case idea as a record (provenance ID, source
      group, text). IDs (A1–I4) trace to the original flip-chart photos. Carries no
      resource, outcome, or dedup field — those live solely in
      resources.yaml/outcomes.yaml/unique_items.yaml, so there is nothing here that
      can fall out of sync with them.
    - `unique_items.yaml` — sole authoritative deduplication: every raw item appears
      in exactly one entry's `items:` list (multi-item entries are duplicates of the
      same idea; single-item entries are singletons, `label:` = the item's own
      text). Keys are arbitrary sequential slugs (X1, X2, ...), decoupled from
      content. Both resources.yaml and outcomes.yaml categorize at this level, not
      the raw-item level.
    - `resources.yaml` — sole authoritative **resource** scheme AND membership: the
      four resource categories (label + `items:` list of unique_items IDs, not raw
      item IDs) each unique_items entry needs to be delivered. Every unique_items
      entry belongs to exactly one resource category — no spanning. Answers "what
      does this work need?" — drives hiring/promoting/organizing decisions. Plain
      label+items shape, same as outcomes.yaml — the Champions/Leaders/Doers role
      detail this file used to carry (as `personnel.yaml`) now lives as
      hand-authored prose in `AI_strategy_and_roadmap.md` instead, not generated.
    - `outcomes.yaml` — sole authoritative **outcome** scheme AND membership: which
      strategic objective each unique_items entry serves. Independent axis from
      resource — the two don't have to agree and aren't derived from each other.
      Every unique_items entry belongs to exactly one outcome. Set mirrors
      `followup_message.md`'s three PAC-facing priorities plus a Foundations
      catch-all.
  - `strategic_insights/cook/vision_synthesis.yaml` — sole authoritative source for
    the official vision statement (adjudicated 2026-08-12, ADR-11) quoted in
    `pac_report.md`'s Vision Statement section and (by hand) in
    `vision_statements_analysis.md`'s "Synthesized Vision Statement" section.
  - `strategic_insights/hutyra/` — authored documents (the four PAC docs; read-only
    reference).
- `build/` — `validate.py` (integrity checks) and `generate.py` (yaml -> md, always;
  optionally md -> styled HTML -> PDF for every `.md` in `pac_retreat/` and `roadmap/`
  with `--pdf`). PDFs are gitignored — this repo is pushed to GitHub, which renders
  markdown natively, so committed PDFs would just be stale duplicates.
- `roadmap/` — hand-authored roadmap docs:
  `decisions/open_decisions.md` (what needs adjudication) and
  `decisions/resolved_decisions.md` (adjudicated decisions, ADR-style);
  `resources/infrastructure.md` (AI platform catalog),
  `resources/support_organizations.md` (support roles/org units), and
  `resources/post_retreat_discussion.md`. Job roles (Curriculum Integration Lead,
  Workforce Development Lead, AI Solution Delivery Lead, etc.) are no longer tracked
  separately here — see `AI_strategy_and_roadmap.md` for current role definitions.

## Core conventions

1. **Data drives docs.** The categorization lives in the `use_cases/*.yaml` files under
   `pac_retreat/analysis/.../cook/use_cases/`. Generated documents are built from it.
   If a resource category or outcome changes, change the YAML and rebuild — never patch
   a generated file by hand. (Exception: `AI_strategy_and_roadmap.md` is hand-authored,
   not generated — see Layout above.)
2. **Provenance is sacred.** Every item keeps its A1–I4 ID linking it to a source photo
   group. Never renumber these; they are the audit trail. Display/ordinal numbering
   (use-case 1/2/3) is separate and *may* change.
3. **Alignment with PAC docs is tracked, not assumed.** The executive PAC documents use a
   three-**bucket** framework. This repo's resource categories map to those buckets but
   are not identical. `roadmap/decisions/open_decisions.md` tracks every known divergence awaiting
   adjudication. Do not silently "fix" a divergence — surface it.
4. **Nothing gets dropped.** Every unique_items entry lands in exactly one resource
   category AND exactly one outcome. If an item fits nowhere on either axis, that is a
   signal to revisit the taxonomy, not to discard the item.

## The categorization framework (current state)

Every unique_items entry is categorized along **two independent axes** — they don't have
to agree with each other and neither is derived from the other:

- **Resource** (`resources.yaml`) — what the work needs (four categories: Curriculum
  integration, Workforce development, AI solution delivery, Capabilities/Foundation).
  Drives hiring/promoting/organizing decisions. Which specific roles (Champions,
  Leaders, Doers) staff each category is hand-authored in `AI_strategy_and_roadmap.md`,
  not part of this YAML.
- **Outcome** (`outcomes.yaml`) — which strategic objective the work serves. Mirrors the
  PAC-facing priorities in `followup_message.md`.

Both axes apply at the **unique_items** (deduplicated) level, not the raw-item level —
every unique_items entry belongs to exactly one group on each axis. Where an entry's
member raw items previously disagreed on resource category (e.g. a duplicate group
mixing a curriculum item with a workforce item), a single category was chosen by
explicit adjudication rather than split across categories; same rule applies to outcome.

### Resource

Unique items partition into two top-level kinds:

- **Use-cases** — resourceable work, split by the scarce *key resource* each depends on:
  1. Curriculum integration — "Ensure AI Literacy for All Tarleton Graduates."
  2. Workforce development — "Equip our faculty and staff to use AI effectively and
     responsibly."
  3. AI solution delivery — "AI Solutions Delivery."
- **Capabilities / Foundation** — "Provide guidance and guardrails to keep our data and
  systems safe"; cross-cutting preconditions (governance, security, advisory board); not
  sorted by resource.

Simplified 2026-08-20: `resources.yaml` (replaces `personnel.yaml`) dropped the
Champions/Leaders/Doers role breakdown (title, description(s), `ai_expertise` rating)
that used to live in the YAML — that detail is now hand-authored prose in
`AI_strategy_and_roadmap.md`'s Roles and Staffing section instead of generated, since it
no longer needs to round-trip through `pac_report.md`. `resources.yaml` itself is now a
plain label+items mirror of `outcomes.yaml`.

(Restructured 2026-08-12, since superseded: an earlier version replaced a
structure/content/technical facet profile with the Leaders/Doers breakdown described
above. A former third top-level kind, **Framings** — strategic lenses/models that
consumed no resources — was removed 2026-08-11: once this axis moved to the
unique_items level, every framings-flavored raw item turned out to be the minority
member of a duplicate group whose majority belonged elsewhere, leaving the category
permanently empty.)

See `use_cases/resources.yaml` for the authoritative category/item definition,
`AI_strategy_and_roadmap.md` for role detail, and `roadmap/decisions/open_decisions.md`
for unresolved framework questions (notably a lingering ordering divergence vs. PAC
bucket numbers, and two contested item placements).

### Outcome

Four groups (added 2026-08-12), three mirroring `followup_message.md`'s PAC-facing
priorities plus a catch-all for entries none of the three cover:

1. Accelerate Student Retention and Success
2. Integrate AI Across the Curriculum and Create AI Certificates
3. Enhance Service and Operations Through AI
4. Foundations (catch-all — e.g. governance, research capacity)

See `use_cases/outcomes.yaml` for the authoritative definition.

## Relationship to the PAC three-bucket framework

| This repo (use-case) | PAC document (bucket) | Owner |
|---|---|---|
| Curriculum integration | Bucket 3: Curriculum Integration | Academic Affairs (TBD); SI advises |
| Workforce development | Bucket 1: Workforce Upskilling | Org lead (TBD); SI advises |
| AI solution delivery | Bucket 2: High-Technical Projects | **SI owns** |
| Foundations | Cross-Cutting Foundations | rides along all buckets |

**Ordering vs. PAC buckets:** this repo currently orders use-cases Curriculum/Workforce/
AI-solution (1/2/3); PAC buckets order Workforce/AI-solution/Curriculum (1/2/3) — every
slot differs. This is adjudicated, not an oversight (OD-1, resolved): the repo
deliberately keeps its own internal ordering rather than matching PAC's, and that
internal ordering has itself been revised twice (ADR-1, then ADR-9 in
`roadmap/decisions/resolved_decisions.md`) for internal-readability and ownership-signaling reasons
unrelated to PAC alignment. See `roadmap/decisions/resolved_decisions.md` for the full history.

## Build

```
python build/generate.py            # regenerate pac_retreat/analysis/use_cases_analysis.md and pac_report.md (top level) from use_cases/*.yaml
python build/generate.py --pdf      # also render PDFs (gitignored; GitHub renders md natively)
```

`--pdf` requires `markdown` (pip) and `wkhtmltopdf` (system). See `build/generate.py` header.
