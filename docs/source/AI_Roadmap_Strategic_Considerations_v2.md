# AI Roadmap — Strategic Considerations and Open Questions

**INTERNAL — Strategic Insights working document. Not for distribution.**

This companion to the PAC executive report records open questions and emerging considerations that inform the roadmap but do not belong in the executive summary. Each item states why it matters and the suggested next step, so nothing identified during early planning is lost between roadmap iterations.

---

## 1. The service-delivery fork: self-service vs. service shop

**The question:** Is the university training people to solve their own problems with AI, or building a shop that solves their problems for them?

This is an early fork in the road for the entire roadmap, and it is larger than any single project. Document digitization illustrates it well: many departments need physical records digitized with genuine information extraction, not just scanning.

- **Path A — self-service:** standardize on user-friendly commercial platforms (Azure Document Intelligence, Databricks), fund licenses, and staff a teaching/enablement function so units can serve themselves.
- **Path B — service shop:** staff a small specialist team on expert-grade tooling (e.g., Tesseract) and operate an internal service bureau that departments submit work to.

The choice determines **hiring profiles, tooling standards, and budget shape**. A hybrid is possible (specialist tooling to clear backlogs now, platform standardization for shareability later), but the default posture should be decided deliberately, early, and revisited per domain.

**Next step:** frame this as an explicit decision point in the next roadmap iteration, with document digitization as the pilot case.

## 2. MLOps/DevOps talent market realities

The executive report's top hiring recommendation faces a market problem worth planning around before a job description is written:

- In industry, ML engineering sits at a **senior rung of the data-science career ladder**; the roles are high-paying and competitive, and university salary bands may not reach market rates.
- **Mitigations to evaluate:**
  - *Agentic MLOps tooling* — recent platform releases (notably Databricks) claim to automate portions of the deployment pipeline. If credible, the hire profile could shift from a senior ML engineer to a strong DevOps engineer supported by tooling.
  - *Internal transfer and upskilling* — some needs may be met by moving an existing capable employee onto the team ("new to the team," not "new to the university"), reducing both cost and ramp time.
  - *Phasing* — a first hire focused on deployment fundamentals, with the senior profile deferred until project volume justifies it.

**Next step:** a short market scan and tooling assessment before the recruitment request is finalized.

## 3. Document digitization / OCR pathway

- A Texas state agency precedent shows **Tesseract (open-source OCR)** performing at near-100% accuracy on dense tabular scans when configured correctly (DPI settings, chunking) — techniques now in hand that earlier internal attempts lacked.
- Early re-testing on our own transcripts looks substantially better than prior results. If accuracy holds on the hardest documents, the **existing transcript backlog can be processed immediately** at near-zero marginal cost — and the added historical data may meaningfully improve the AMP model.
- Tradeoffs to track: vision-language-model OCR is stronger on nuance (prompt-guided, preserves table structure) but carries per-token cost; certain foreign-developed models are off-limits regardless of quality; commercial platforms (Azure Document Intelligence, Databricks) remain the shareable, teachable route if the self-service path wins item 1.

**Next step:** validate Tesseract accuracy on a sample of the hardest documents; if it holds, begin the backlog while platform costing continues in parallel.

## 4. Course scheduling and room optimization

- The incumbent commercial scheduling product costs roughly **$500K per year** and cannot handle basic constraints (e.g., matching courses to rooms by amenities such as whiteboard coverage), let alone cross-campus travel-time feasibility.
- There is active energy at the provost level to build a replacement in-house, with early prototyping already under way. The opportunity is real: even a partial solution that beats the incumbent would deliver enterprise-wide improvement plus a hard-dollar savings story.
- Risks to manage: enterprise-scale scheduling is a genuinely hard optimization problem — constraint interactions multiply in ways toy-scale prototypes do not reveal. Expectations should target *better than the incumbent*, not perfection.
- Favorable property: output would likely flow to the registrar rather than to end users, meaning **low last-mile delivery burden** relative to other Bucket 2 projects.

**Next step:** a scoping session with the provost's office to inventory constraints and set realistic phase-one targets.

## 5. AI teammate system — architecture and dogfooding

- **Knowledge-base architecture:** the ingestion layer (chunking raw emails, transcripts, and documents with project labels and source metadata) is under way. The open question is whether a **second transformation layer** (vector embedding / distillation into retrieval-optimized form) is required, or whether the project expert can operate effectively on direct chunks. Intuition says the transformation matters; only empirical testing will settle it.
- **Dogfooding opportunity:** the roadmap reporting workflow itself — a central knowledge base generating multiple report levels for different audiences — is a natural first test-bed project for the system, once deadline pressure permits.
- **Known constraint:** stable backlinks to individual emails may not exist in the current mail platform; effort on that thread should stay bounded.

**Next step:** run comparative retrieval tests (direct chunks vs. transformed layer) on the existing corpus.

## 6. Micro-credentialing — placement and positioning

- The initiative does not fit cleanly into the three-bucket partition (it spans Buckets 1 and 3 and may ultimately warrant its own track). That ambiguity is acceptable for now; the positioning is what must not be lost:
  - The niche is **learners who want a physical person to learn from** — not a competition with large online-only providers.
  - Curriculum can build on industry-standard content (Coursera, Google, and similar); the value-add is human instruction and community.
  - It carries presidential sponsorship, which materially improves its odds of traction and funding.

## 7. Bucket 1 delivery model — embedded experts

- The mature structure for workforce upskilling is **AI-capable point people embedded in each unit** serving as the local first line of support, rather than all questions routing to a central office. This is a later-stage design goal, but it should shape the upskilling program's architecture from the start (train-the-trainer emphasis, unit-level champions).

## 8. Funding path and timing

- The resource request is expected to route to the **president's level rather than through the standard CFO channel**, which favors moving while leadership attention on AI is high.
- Little of this plausibly executes within the current fiscal year's budget; the request is for additional allocation, positioned as the recognized exception to current headcount constraints: new people, for new tasks, that reduce demand for people elsewhere.
- A secondary window worth noting: modest current-year funds may support early, small-dollar moves (tooling, pilot licenses) before year-end.

## 9. External landscape — watch list

- **Vendor diversification for AI development:** institutional frustration with the incumbent productivity vendor's AI offerings and support has triggered exploratory conversations with Google, Anthropic, and OpenAI on secure integrations against enterprise data. The core productivity stack (email, calendar) stays put; the AI development environment is in play. SI technical staff should join these conversations once they formalize.
- **TAICCI (A&M System AI compute cooperative):** an early-stage initiative to pool significant AI hardware across system schools, other Texas universities, and industry partners — industry pays for compute time, and proceeds fund tokens for students and researchers. It may not survive its early stages, but if it launches it could materially change Tarleton's compute economics. Monitor.
- **State DIR AI sandbox:** a legislatively mandated AI prototyping sandbox for Texas state agencies has gone quiet since January. Low priority, but worth an occasional check.
- **AI framework support liaison:** a dedicated customer-success contact now exists on the framework team; coordination and support requests should route through that channel rather than ad hoc email.
