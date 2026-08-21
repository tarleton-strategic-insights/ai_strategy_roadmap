## Introduction

This working draft of AI strategy \& roadmap for Tarleton State builds upon [pac_report.md](pac_report.md) and [survey_analysis.md](survey_analysis.md) — moving from "what we learned in the retreat and followup survey" to "how we act on it."

**Status: working draft**, not a final proposal. Sections vary in maturity — some (Use
Cases, Gap Analysis, Infrastructure) are fleshed out; others (Milestones, Resourcing
and Budget) are still placeholders awaiting input from other stakeholders. Intended to
guide further conversation, not to be read as a complete package.

## Synthesized vision statement 
from [pac_report.md](pac_report.md) and [vision_statements_analysis.md](pac_retreat/analysis/vision_statements_analysis.md)

> Tarleton State University will responsibly harness AI to amplify student success, workforce readiness, and institutional impact — empowering our students, faculty, staff, and community to lead with integrity, privacy, and trust in an AI-enabled world.

## Use Cases
In [pac_report.md](pac_report.md) and [use_cases_analysis.md](pac_retreat/analysis/use_cases_analysis.md), all 51 use cases suggested in the PAC retreat were analyzed to create two types of categorization: by outcome and by resource. 

### By Outcome
- Ensure AI Literacy for All Tarleton Graduates
- Accelerate Student Retention and Success
- Enhance Service and Operations Through AI

### By Resource
- Ensure AI Literacy for All Tarleton Graduates
- Equip our faculty and staff to use AI effectively and responsibly
- Provide guidance and guardrails to keep our data and systems safe
- AI Solutions Delivery

We now add details such as key roles and responsibilities. This is work in-progress. It is incomplete and intended as a starting point for future discussions.

Since technical AI expertise is a limited and expensive resource, we estimate the level necessary for each role.

#### Ensure AI Literacy for All Tarleton Graduates

- Curriculum integration and microcredential programs
- Leaders
    - Provost, deans, department heads
        - Establish academic structure and process (ex: stand-alone AI courses vs. embed AI in all courses vs. embed into capstones)
        - AI expertise: low
- Doers
    - Instructors
        - Design & implement most effective ways to integrate AI within their specific subject
        - AI expertise: varies by field

This objective naturally lives within Academic Affairs which has already begun to plan and pursue it.

#### Equip our faculty and staff to use AI effectively and responsibly

- Workforce development
- Leaders
    - Coordinator
        - Organize & support training for all staff AND faculty (and possibly alumni, community partners, etc)
        - AI expertise: low
- Doers
    - Trainers
        - Teach AI to a broad range of people
        - AI expertise: medium

This is a big job that needs a leader with a clear vision and strong organizational skills to make it consistent and effective. Unlike the other pieces, this does not have an obvious home nor align naturally with existing jobs.

It presents organizational challenges because it spans both faculty and staff. Here are a few examples (over-simplified for brevity)
- Uses: faculty need AI for teaching/learning and research; staff need AI for business functions
- Trainers: CEE trains faculty; HR trains staff
- Incentives: faculty are incentivized by tenure/promotion; staff are incentivized by performance evaluations

This incomplete list already highlights the 1st big issue - workforce development does not fit naturally into our organizational structure.

Thus, figuring out where this fits must be one of our top priorities.

#### Provide guidance and guardrails to keep our data and systems safe

- Oversee AI governance, ethics, security, etc
- Leaders
    - TBD
- Doers
    - TBD

AI Council has provided some degree of oversight, but it does not have a clear mandate or sufficient resourcing to do it properly. We could choose to beef-up and refocus AI Council for this job or find/create another group.

This carries at least 2 responsibilities - creating guidance AND communicating/implementing/enforcing it. AI Council can create all necessary the rules and proceedures, but it must have broad leadership support to disseminate and enforce them.

#### AI Solutions Delivery
Many of the high-priority applications of AI (dropout early-warning, course planning & advising, streamline business processes, etc) are technically complex to create and maintain. Like most IHE AI strategies reviewed, we propose creating a team with advanced AI skills to tackle these challenging tasks.

- Create, deploy, and support complex AI tools & solutions
- Leaders
    - Chief engineer
        - Develop, architect, and guide multiple complex AI projects
        - Evaluate & support 3rd-party AI products
        - AI expertise: high
    - Project manager
        - Intake, prioritize, coordinate, and monitor all projects
        - Client-facing point of contact
        - AI expertise: low
- Doers
    - Engineer
        - Execute complex AI projects
        - AI expertise: high
    - Operations
        - Deploy, monitor, and support completed projects
        - AI expertise: high
    - Product support
        - Help users effectively leverage 3rd party AI tools (ex: Copilot, AI Builder)
        - AI expertise: medium

There are already several pockets of such activity to build upon.

## Organizational Structure

While "Ensure AI Literacy for All Tarleton Graduates" lives wholly within Academic Affairs, the other resource categories span multiple divisions wrt function and personnel. For example, "AI Solutions Delivery" will serve the entire university and likely involve personnel from Business \& Finance, University Strategy, Academic Affairs, and potentially other divisions. As discussed above, "Workforce development" does not have a natural home and therefore might only span multiple divisions.

Furthermore, many of the listed roles are not full time jobs. It is likely that they will be incorporated into existing positions across different departments/divisions.

These raise questions about coordination, oversight, and evaluation that always occur with cross-functional teams. These questions can be effectively answered and potential problem avoided through careful upfront discussion and planning.

## Build vs Buy

In constrast to most new technologies, everyone can use AI without needing advanced technical skills. AI empowers "build-your-own" approaches to problems that previously required specialized skills and materials. However, some problems remain too complex, specialized, or costly for DIY and should be outsourced or purchased.

"AI Solutions Delivery" could contain dedicated "build" and "buy" teams. While the build team creates and maintains in-house AI solutions, the buy team evaluates 3rd party tools and provides training and support for them to faculty \& staff.

## Embedded AI partners

The Workforce Development team will equip all faculty \& staff with enough basic AI knowledge to pick their own low-hanging fruit and make meaningful improvements to their own workflow. The AI Solutions team will create advanced AI tools to solve complex problems.

Question: Should there be something in-between?

Idea: Offer additional AI training beyond the baseline campus-wide training to self-selected "AI partners" embedded in functional areas to serve as local AI faciliators for their unit to
1. Encourage AI adoption \& self-service
2. Create intermediate-level AI solutions tailored to their unit which require AI knowledge beyond baseline and are not appropriate tasks for the main AI Solutions teams (eg: too narrow, competing priorities, etc)

The AI partner program could fall either under workforce development or AI solutions teams. My instinct leans toward AI solutions as that could bring a secondary benefit of creating direct relationships between AI partners and engineers with advanced AI skills.


## Gap Analysis
Below is a partial list of additional AI-related gaps I've heard which are not covered above
1. User-support for AI Builder, Copilot, and other enterprise-wide AI platforms
1. Technical Users Group where AI power users can share lessons learned and seek advice
1. Stable platform
    - AI Builder has usuage limits and teething-problems
    - Copilot has added cost (for pro) and many folks like ChatGPT/Gemini/Claude more
    - ChatGPT/Gemini/Claude are not secure/private
1. Technical staff augmentation - short-term consultant support for specialities we lack in-house or when tasks outstrip internal capacity
1. Intake & client coordination - structured process to receive, prioritize, and track project and communicate progress back to requestor
1. Solution support - ongoing monitoring and maintenance of previously created solutions

## Infrastructure

Current and planned AI infrastructure available to the University.
### University-wide

| Platform | Cost | Availability | Notes |
|----------|------|--------------|-------|
| AI Builder | Free | Now | $10/day cap |
| Copilot Chat | Free | Now | |
| Copilot Pro | $18/month | Now | |
| TAICCI | TBD | >1 year out | Texas AI Compute Cooperative Initiative |
| VISION Superpod | Free | Now | High technical barrier to entry |
| Secure ChatGPT/Gemini/Claude | TBD | Early proposal | Getting quotes from OpenAI, Google, Anthropic |

### Limited-access

| Platform | Cost | Availability | Notes |
|----------|------|--------------|-------|
| TAI01 research server | — | Now | Donated by Troy Thorne |
| NVIDIA DGX Spark | — | Now | |

-------- Everything below is AI-created boilerplate to be completed or removed later --------

---

## Roles and Staffing

TODO: how the Champions/Leaders/Doers roles in pac_report.md's "By Resources" section get
filled — hiring, reassignment, training.

---

## Milestones and Timeline

TODO: phased plan. See "Summary: Emerging Roadmap Milestones" in
[post_retreat_discussion.md](roadmap/resources/post_retreat_discussion.md) as a starting point.

---

## Resourcing and Budget

TODO: funding model. See OD-13 and
[infrastructure.md](roadmap/resources/infrastructure.md).

---

## Governance and Guardrails

TODO: policy, security, ethics oversight for the "Provide guidance and guardrails" category.

---

## Open Questions

Decision points raised in this document, collected here so the next meeting can work
through them directly rather than finding them scattered across sections. See also
[open_decisions.md](roadmap/decisions/open_decisions.md) for decisions tracked
independently of this roadmap.

1. **Where does Workforce Development live?** Flagged above as not fitting naturally
   into the existing organizational structure, spanning both faculty (CEE, tenure
   incentives) and staff (HR, performance-eval incentives) — this is one of the
   biggest structural risks in the whole roadmap and still has no proposed home.
2. **Who owns AI governance?** AI Council currently lacks a clear mandate and
   sufficient resourcing. Do we expand and refocus AI Council, or stand up a
   different group? This underpins the Build vs Buy split and the AI partners
   program below it, so resolving it unblocks both.
3. **AI partners: workforce extension or Solutions Delivery on-ramp?** Two different
   framings are floating in "Embedded AI partners" — an advanced extension of
   Workforce Development, or an introductory tier feeding into AI Solutions
   Delivery. Current lean is the latter, but neither framing is fully fleshed out;
   this may need its own dedicated discussion before it can be scoped.
4. **Budget and resourcing model** — not addressed anywhere in this draft yet. This
   document distills what PAC said it wants and needs; the funding conversation is
   a distinct next step for other stakeholders to own.
