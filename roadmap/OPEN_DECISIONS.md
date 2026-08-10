# Open Decisions Log

Unresolved framework and placement questions. Each carries a recommendation and stays
open until Scott adjudicates. When resolved, move to a dated ADR entry at the bottom and
update the relevant `use_cases/*.yaml`.

## Framework-level

### OD-1 — Use-case ordering vs. PAC bucket numbers
**RESOLVED — see ADR below.**

### OD-2 — Terminology conformance
**RESOLVED — see ADR below.**

### OD-3 — Framings section
**RESOLVED — see ADR below.**

### OD-4 — Ownership dimension
**RESOLVED — see ADR below.**

### OD-8 — Workforce development ownership
No owner currently assigned for the Workforce development use-case. Strategic Insights owns AI solution delivery; Academic Affairs owns Curriculum integration.
**Decision needed:** Who owns Workforce development?
**Status: OPEN.**

### OD-9 — Central vs. distributed build teams
Conceptual tension between a centralized AI support/enablement function and embedded unit experts building their own solutions.
**Decision needed:** What is the target operating model—central team, distributed expertise, or hybrid?
**Status: OPEN.**

## Item-level placement

### OD-5 — F1 Security gap analysis
**RESOLVED — see ADR below.**

### OD-6 — F3 "teach me ___" learning augmentation
**RESOLVED — see ADR below.**

### OD-7 — B5 Centralized AI support
**RESOLVED — see ADR below.**

---

## Resolved (ADR)

### ADR-1 — Use-case ordering (2026-08-10, revised)
**Decision:** Reorder to: AI-solution-delivery(1) / Curriculum(2) / Workforce(3).
**Rationale:** Places owned use-cases first; un-owned Workforce last highlights the ownership gap.

### ADR-2 — Terminology (2026-08-10)
**Decision:** Keep repo terminology ("use-case," "AI solution delivery").
**Rationale:** Internal consistency; PAC-facing exports can translate as needed.

### ADR-3 — Framings section (2026-08-10)
**Decision:** Keep Extend/Defend/Upend lenses and AI Competitive Flywheel internally; omit from exec-facing exports.
**Rationale:** Useful for internal completeness; not relevant to PAC audience.

### ADR-4 — Ownership dimension (2026-08-10)
**Decision:** Add ownership to use-case taxonomy.
- AI solution delivery → **Strategic Insights**
- Curriculum integration → **Academic Affairs**
- Workforce development → **TBD** *(key decision needed)*

**Rationale:** Clarifies accountability; surfaces Workforce ownership gap as an open item.

### ADR-5 — F1 Security gap analysis placement (2026-08-10)
**Decision:** Keep in Foundation (not Bucket 2).
**Rationale:** PAC prose describes it as cross-cutting; Appendix A placement was inconsistent.

### ADR-6 — F3 "Teach me ___" placement (2026-08-10)
**Decision:** Keep in Workforce development.
**Rationale:** It's a training/learning tool, not a solution to build.

### ADR-7 — B5 Centralized AI support placement (2026-08-10)
**Decision:** Move to AI solution delivery.
**Rationale:** This is about building/delivering AI solutions, not workforce training.
**Open question surfaced:** Central vs. distributed build teams—key strategic decision TBD.
