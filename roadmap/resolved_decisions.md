# Resolved Decisions Log

Adjudicated framework and placement questions, ADR-style. See `open_decisions.md` for
unresolved questions. When an open decision is resolved, move its entry here as a dated
ADR and update the relevant `use_cases/*.yaml`.

## Framework-level

### OD-1 — Use-case ordering vs. PAC bucket numbers
**RESOLVED — see ADR-1, ADR-9 below.**

### OD-2 — Terminology conformance
**RESOLVED — see ADR-2 below.**

### OD-3 — Framings section
**RESOLVED — see ADR-3, ADR-8 below.**

### OD-4 — Ownership dimension
**RESOLVED — see ADR-4 below.**

## Item-level placement

### OD-5 — F1 Security gap analysis
**RESOLVED — see ADR-5 below.**

### OD-6 — F3 "teach me ___" learning augmentation
**RESOLVED — see ADR-6 below.**

### OD-7 — B5 Centralized AI support
**RESOLVED — see ADR-7 below.**

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
**Update:** Resolved by ADR-10 below (2026-08-11).

### ADR-8 — Remove Framings category (2026-08-11)
**Decision:** Remove the Framings kind entirely (supersedes ADR-3's "keep internally").
**Rationale:** Categorization was moved from the raw-item level to the deduplicated
(unique_items) level — every unique_items entry now belongs to exactly one category
instead of spanning several. Every entry that previously included a framings-flavored
raw item (the Extend/Defend/Upend framings and the "AI Competitive Flywheel" spokes) had
that item as the minority member of a duplicate group whose majority belonged to a real
use-case or Capabilities/Foundation category; adjudicating each entry to a single
category left Framings with zero members. An empty category serves no purpose, so it was
dropped rather than kept as a placeholder.

### ADR-9 — Use-case ordering, second revision (2026-08-11)
**Decision:** Reorder to: Curriculum(1) / Workforce(2) / AI-solution-delivery(3)
(supersedes ADR-1's AI-solution-delivery(1) / Curriculum(2) / Workforce(3)).
**Rationale:** Balances two goals that ADR-1's ordering no longer served once
categorization moved to the unique_items level: (1) readability — AI solution delivery
became the longest item list in Part 3 of the generated doc, and having the longest list
first pushed the shorter, easier-to-scan categories further down; (2) ADR-1's original
ownership signal — keeping the still-unowned Workforce development (see OD-8 in
`open_decisions.md`) out of the first position — is preserved by this ordering too, since
Workforce sits in the middle, not first.

### ADR-10 — Central vs. distributed build teams (2026-08-11)
**Decision: Both.** Stand up a central AI Solutions Delivery team to handle
high-complexity use-cases, **and** invest in AI training & literacy to empower
self-service on low-complexity ones. For medium-complexity work, consider an "AI
partner" model — similar to MarCom's partner program — with skilled partners embedded
in functional areas across the university.
**Rationale:** Resolves the tension surfaced in ADR-7 (central vs. distributed) by
matching operating model to use-case complexity rather than picking one model for
everything: a central team can't scale to every request, pure self-service can't handle
technically complex work, and an embedded-partner tier fills the middle ground —
distributing skilled capacity into functional areas without losing central
coordination entirely.
**Open question surfaced:** How the AI partner tier would actually be staffed/trained,
and how it interacts with the roles in `use_cases/personnel.yaml`'s "Solutions
Delivery" category — see OD-11 and OD-14 in `open_decisions.md`.

### ADR-11 — Official vision statement (2026-08-12)
**Decision:** Adopt the Working synthesis as Tarleton State's single official AI
vision statement: "Tarleton State University will responsibly use AI to improve
student success, workforce readiness, and institutional operations, while protecting
the integrity, privacy, and trust of our students, faculty, staff, and community."
**Rationale:** Synthesizes the 7 candidate statements transcribed from the retreat
flip charts (see `pac_retreat/vision_statements_analysis.md`) into one adjudicated
statement, closing out the "not yet adjudicated" status that section carried since
the retreat. Sole source of truth for the wording is
`pac_retreat/analysis/strategic_insights/cook/vision_synthesis.yaml`; `pac_report.md`'s
Vision Statement section is generated from it directly, and
`vision_statements_analysis.md`'s "Synthesized Vision Statement" section is kept in
sync by hand.
