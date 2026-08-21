## Introduction

This working draft of AI strategy \& roadmap for Tarleton State builds upon [pac_report.md](pac_report.md) and [survey_analysis.md](survey_analysis.md) — moving from "what we learned in the retreat and followup survey" to "how we act on it."

**Status: working draft**, not a final proposal. Sections vary in maturity — some (Use
Cases, Gap Analysis, Infrastructure) are fleshed out; others are still open. See "Open
Questions" at the end for the specific decision points this draft still needs resolved.
Intended to guide further conversation, not to be read as a complete package.

## Synthesized vision statement 
from [pac_report.md](pac_report.md) and [vision_statements_analysis.md](supporting_materials/pac_retreat/analysis/vision_statements_analysis.md)

> Tarleton State University will responsibly harness AI to amplify student success, workforce readiness, and institutional impact — empowering our students, faculty, staff, and community to lead with integrity, privacy, and trust in an AI-enabled world.

## Use Cases
In [pac_report.md](pac_report.md) and [use_cases_analysis.md](supporting_materials/pac_retreat/analysis/use_cases_analysis.md), all 51 use cases suggested in the PAC retreat were analyzed to create two types of categorization: by outcome and by resource. 

### By Outcome
- Ensure AI Literacy for All Tarleton Graduates
- Accelerate Student Retention and Success
- Enhance Service and Operations Through AI

### By Resource
- Ensure AI Literacy for All Tarleton Graduates
- Equip our faculty and staff to use AI effectively and responsibly
- Provide guidance and guardrails to keep our data and systems safe
- AI Solutions Delivery

We begin filling in details such as key roles and responsibilities below. This is work in-progress, intended as a jumping-off point for future discussions.

#### Ensure AI Literacy for All Tarleton Graduates

- Outcome:
    - Curriculum integration
    - Microcredential programs
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

- Outcome:
    - Workforce development
- Leaders
    - Coordinator
        - Organize & support training for all staff AND faculty (and possibly alumni, community partners, etc)
        - AI expertise: low
- Doers
    - Trainers
        - Teach AI to a broad range of people
        - AI expertise: medium
    - ITS

This is a big job that needs a leader with a clear vision and strong organizational skills to make it consistent and effective. Unlike the other pieces, this does not have an obvious home nor align naturally with existing units. Therefore, figuring out where this fits must be one of our top priorities.

#### Provide guidance and guardrails to keep our data and systems safe

- Outcome:
    - Oversee AI governance, ethics, security, etc
- Leaders
    - TBD
- Doers
    - TBD

AI Council has provided some degree of oversight, but it does not have a clear mandate or sufficient resourcing to do it properly. We could choose to beef-up AI Council for this job or find/create another group.

This carries at least 2 responsibilities
- creating guidance AND
- communicating, implementing, and enforcing it

We can create guidance, but there must be broad leadership support and clear communication channels to disseminate and enforce them.

#### AI Solutions Delivery
Many of the AI applications prioritized highly in the survey (dropout early-warning, course planning & advising, streamline business processes, etc) are technically complex to create and maintain. Like many IHE AI strategies, we propose creating a team with advanced AI skills to tackle these challenging tasks.

- Outcome:
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

While "Ensure AI Literacy for All Tarleton Graduates" lives wholly within Academic Affairs, the other resource categories span multiple divisions wrt function and personnel. For example, "AI Solutions Delivery" will serve the entire university and likely involve personnel from Business \& Finance, University Strategy, Academic Affairs, and potentially other divisions. As discussed above, "Workforce development" does not have a natural home and therefore might also span multiple divisions.

Many of the roles above are not full time jobs. It is likely that they will be incorporated into existing positions across different departments/divisions.

These raise questions about coordination, oversight, and evaluation that commonly occur with cross-functional teams. These questions can be effectively answered and potential problem avoided through careful upfront discussion and planning.

## Build vs Buy

In constrast to most new technologies, everyone can use AI without needing advanced technical skills. AI empowers "build-your-own" approaches to problems that previously required specialized skills and materials. However, some problems remain too complex, specialized, or costly for DIY and should be outsourced or purchased.

"AI Solutions Delivery" could contain dedicated "build" and "buy" teams. While the build team creates and maintains in-house AI solutions, the buy team evaluates 3rd party tools and provides training and support for them to faculty \& staff.

## Embedded AI partners

University-wide AI training will equip everyone with enough basic AI knowledge to make meaningful low-complexity improvements to their own workflow while the AI Solutions team will create high-complexity AI tools to solve high-impact problems.

Question: Should there be something in-between?

Idea: Offer additional AI training to self-selected "AI partners" embedded in functional areas who will serve as local AI faciliators to
1. Encourage AI adoption \& self-service
2. Create medium-complexity AI solutions tailored to their unit which require more AI knowledge but are not well-suited for the main AI Solutions teams

## Gap Analysis
Below is a partial list of known AI-related gaps not covered above
1. Solution support - ongoing monitoring and maintenance of previously created AI solutions
1. Technical staff augmentation - short-term consultant support for specialities we lack in-house or demand beyond internal capacity
1. Intake & client coordination - structured process to receive, prioritize & track projects and communicate progress back to requestor
1. User-support for AI Builder, Copilot, and other enterprise-wide AI platforms
1. Technical User Community of Practice - AI power users share lessons learned and seek advice
1. Stable platform
    - AI Builder has usuage limits and teething-problems
    - Copilot has added cost (for pro) and many folks like ChatGPT/Gemini/Claude more
    - ChatGPT/Gemini/Claude are not secure/private
    - The AI landscape changes rapidly, creating new demand and undermining established solutions. While we can not control it, we must (to the best of our ability) plan how to mitigate disruptive effects.

## Open Questions

Decision points raised in this document, collected here so the next meeting can work
through them directly rather than finding them scattered across sections. See also
[open_decisions.md](supporting_materials/other/decisions/open_decisions.md) for decisions tracked
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


## Footnotes
Information that connects to the AI roadmap but is not core to the narrative

### Infrastructure

Current and planned AI infrastructure available to the University.
#### University-wide

| Platform | Cost | Availability | Notes |
|----------|------|--------------|-------|
| AI Builder | Free | Now | $10/day cap |
| Copilot Chat | Free | Now | |
| Copilot Pro | $18/month | Now | |
| TAICCI | TBD | >1 year out | Texas AI Compute Cooperative Initiative |
| VISION Superpod | Free | Now | High technical barrier to entry |
| Secure ChatGPT/Gemini/Claude | TBD | Early proposal | Getting quotes from OpenAI, Google, Anthropic |
| Microsoft Azure | TBD | Now | pay-as-you-go |

#### Limited-access

| Platform | Cost | Availability | Notes |
|----------|------|--------------|-------|
| TAI01 research server | — | Now | Donated by Troy Thorne |
| NVIDIA DGX Spark | — | Now | |
| Individual "edge" devices | variable | ongoing | |