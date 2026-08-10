# Open Decisions Log

Unresolved framework and placement questions. Each carries a recommendation and stays
open until Scott adjudicates. When resolved, move to a dated ADR entry at the bottom and
update the relevant `data/*.yaml`.

## Framework-level

### OD-1 — Use-case ordering vs. PAC bucket numbers
This repo orders use-cases Workforce(1) / Curriculum(2) / AI-solution-delivery(3).
PAC buckets order Workforce(1) / High-Technical(2) / Curriculum(3). Slots 2 and 3 are
transposed, so "Bucket 2" points at different categories across documents.
**Recommendation:** reorder to match PAC (swap ordinals so ai_solution_delivery=2,
curriculum_integration=3) in `data/taxonomy.yaml`. **Status: OPEN.**

### OD-2 — Terminology conformance
Repo uses "use-case / AI solution delivery"; PAC uses "bucket / High-Technical Projects."
**Recommendation:** keep internal names in data; add a PAC-facing label field if docs
must circulate together. **Status: OPEN.**

### OD-3 — Framings section
The Extend/Defend/Upend lenses and the AI Competitive Flywheel (A1-A3, I1-I4) have no
place in the PAC executive documents. This repo keeps them as a Framings category.
**Recommendation:** keep internally (completeness); omit from exec-facing exports.
**Status: OPEN.**

### OD-4 — Ownership dimension
PAC docs assign owner + SI role per bucket; this repo's facet profile omits ownership.
**Recommendation:** add `owner` / `si_role` fields to taxonomy use-case types.
**Status: OPEN.**

## Item-level placement

### OD-5 — F1 Security gap analysis
Repo: capabilities_foundation. PAC Appendix A: Bucket 2. PAC prose: Cross-Cutting
Foundation. PAC contradicts itself; we chose the prose side.
**Recommendation:** keep in Foundation. **Status: OPEN.**

### OD-6 — F3 "teach me ___" learning augmentation
Repo: workforce_development. PAC: Bucket 2 (a tool to build).
**Recommendation:** move to ai_solution_delivery to match PAC's read.
**Status: OPEN.**

### OD-7 — B5 Centralized AI support
Repo: workforce_development. Conceptual tension with PAC end-state (embedded unit experts,
not a central help desk).
**Recommendation:** keep placement; flag phrasing when it reaches roadmap sequencing.
**Status: OPEN.**

---

## Resolved (ADR)

_(none yet)_
