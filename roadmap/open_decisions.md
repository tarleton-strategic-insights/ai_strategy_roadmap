# Open Decisions Log

Unresolved framework and placement questions. Each carries a recommendation and stays
open until Scott adjudicates. When resolved, move the entry to `resolved_decisions.md`
as a dated ADR entry and update the relevant `use_cases/*.yaml`.

## Framework-level

### OD-8 — Workforce development ownership
No owner currently assigned for the Workforce development use-case. Strategic Insights owns AI solution delivery; Academic Affairs owns Curriculum integration.
**Decision needed:** Who owns Workforce development?
**Status: OPEN.**

### OD-10 — Name for the central AI solutions team
"AI solution delivery" names the *use-case category* (the work), not a team. If/when a
central team forms to own that work, it needs its own name, distinct from the category.
Candidates surfaced 2026-08-11 (see chat, no doc yet): **AI Center of Excellence**
(dominant industry/enterprise term — IBM, Microsoft, Oracle, SAP all use this pattern),
**AI Enablement Team** (real, less formal, emphasizes helping others use AI over building
for them — may undersell a build-for-others scope), **AI Solutions Team** (plain,
low-jargon, keeps preferred word "Solutions"). Scott's stated preference: likes
"Solutions," lukewarm on "Delivery" as the closing word — but this only applies to a
future team name, not the existing "AI solution delivery" use-case category label, which
stays as-is (see ADR-2 in `resolved_decisions.md`).
**Decision needed:** Pick a name once/if a central team is formally stood up (linked to ADR-10 in `resolved_decisions.md`).
**Status: OPEN.**

### OD-11 — Single organization over all three use-cases + Capabilities/Foundation?
Should Curriculum integration, Workforce development, AI solution delivery, and
Capabilities/Foundation all live under one umbrella organization (e.g. an "AI Council"),
rather than being owned/coordinated separately as today (see OD-8, ADR-4 in
`resolved_decisions.md` on the current per-category ownership split)? Distinct from
ADR-10 in `resolved_decisions.md`, which resolved centralized vs. distributed *build*
capacity specifically within AI solution delivery — this is about governance/
organizational structure across all four categories.
**Decision needed:** Single umbrella org (e.g. AI Council) vs. keep separate ownership per category.
**Status: OPEN.**

### OD-12 — Tarleton's position on the AI maturity spectrum
Slide 3 of `pac_retreat_sources/event_artifacts/slides/Richardson_AI_landscape.pdf`
("Organizations Are Picking Their Pace") lays out a six-stage AI maturity spectrum:
**Not AI-enabled** (no AI use) → **AI-assisted** (basic AI support in isolated areas) →
**AI-augmented** (AI enhances, but not central) → **AI-integrated** (AI integrated into
core processes) → **AI-centric** (AI is central to most areas) → **AI-native** (business
fundamentally built on AI). Where does Tarleton currently sit on this spectrum?
**Decision needed:** Pick Tarleton's current stage (and optionally a target stage/timeline).
**Status: OPEN.**

### OD-13 — PAC should prioritize AI solution delivery items
Proposal: when PAC holds the not-yet-held priority vote (see `CLAUDE.md` "Current
status" and `roadmap/post_retreat_discussion.md`'s milestone table), it should
specifically prioritize items within the AI solution delivery use-case category —
i.e. weight/sequence the vote toward that backlog rather than treating all three
use-case categories as equally urgent.
**Decision needed:** Confirm PAC's priority vote should weight AI solution delivery
items first/most heavily, vs. an even-handed vote across all three use-case categories.
**Status: OPEN.**

### OD-14 — AI Solution Delivery: reporting structure vs. logical/matrixed unit
Many of the roles in `use_cases/personnel.yaml`'s "Solutions Delivery" category (Chief
AI Officer, Project manager, Engineer, Operations, Product support) are probably not
full-time jobs and could be filled by existing staff (Scott has
candidate names in mind) — but a role can't simply be stacked on top of someone's
current job; some of their existing duties would need to be realigned to someone else.
This raises a structural question, related to but more concrete than ADR-10 (in
`resolved_decisions.md`) and OD-11: should
AI Solution Delivery be a genuine organizational reporting structure (its own reporting
line, staff formally moved/reassigned into it), or a logical/matrixed unit composed of
individuals who keep their existing reporting lines in different units (e.g. Strategic
Insights, ITS, Academic Affairs) but contribute part-time to AI solution delivery work?
**Decision needed:** Real reporting structure vs. logical/matrixed cross-unit team —
and if matrixed, how each person's existing duties get realigned to make room.
**Status: OPEN.**

## Item-level placement

_(none currently open — see `resolved_decisions.md` for resolved item-level placements)_
