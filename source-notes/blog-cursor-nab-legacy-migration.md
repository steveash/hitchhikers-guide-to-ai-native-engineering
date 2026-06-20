---
source_url: https://cursor.com/blog/nab
source_type: blog-post
title: "National Australia Bank accelerates legacy migrations with Cursor"
author: "Cursor (vendor case study; named practitioners: Chris De Lorenzo, Andrew Vaughan, Coby Paterson, Harjot Singh, Caroline Trang — all NAB)"
date_published: 2026-04-23
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#350"
---

# National Australia Bank Accelerates Legacy Migrations with Cursor

> A named-practitioner enterprise case study at Fortune-500 scale (6,000 developers, scaling to 10,000+) documenting three distinct use cases — monolith-to-microservices migration, Assembly mainframe migration previously blocked by expertise scarcity, and a greenfield mobile app built without prior language experience — establishing that AI coding tools enable categorically impossible work, not only faster existing work, and providing the first corpus evidence on enterprise tool evaluation criteria (Amazon Q vs. GitHub Copilot vs. Cursor) and intentional enablement strategy.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's blog, April 2026; ~1,000 words; four named sections with attributed quotes from five NAB practitioners)
- **Author credibility**: Five named NAB practitioners (Chris De Lorenzo — Principal Engineer; Andrew Vaughan — Distinguished Engineer; Coby Paterson — Principal Engineer; Harjot Singh — Engineering Manager; Caroline Trang — Head of AI Tooling & Delivery). NAB is a major Australian bank (Fortune-500 scale). Published on Cursor's commercial blog — this is vendor marketing. The named engineers, specific project timelines, concrete velocity numbers, and multiple attributed quotes across different roles are consistent with genuine practitioner evidence. Treat as vendor-sourced practitioner evidence: emerging confidence for specific metrics, anecdotal confidence for individual quotes.
- **Scope**: Covers tool evaluation (Amazon Q vs. GitHub Copilot vs. Cursor), enterprise rollout and enablement strategy, three named migration/greenfield projects, and near-term roadmap. Does NOT cover: cost of Cursor licensing, how NAB CEL library is implemented technically, COBOL-specific capabilities (mentioned in tech stack but not the focus of described projects), how the Assembly migration flowcharts were generated (specific prompting approach), failure modes, or what evaluation criteria Amazon Q and GitHub Copilot failed on specifically.

## Extracted Claims

### Claim 1: NAB selected Cursor over Amazon Q and GitHub Copilot for enterprise standardization based on three criteria: model flexibility, codebase understanding across heterogeneous stacks, and extensibility/control

- **Evidence**: Named evaluation process: "NAB initially relied on Amazon Q and GitHub Copilot before conducting a comprehensive evaluation" and selected Cursor for three explicit reasons. All three criteria are named and described in the article with specific context.
- **Confidence**: emerging (vendor case study; the three criteria are described by a named engineer, Chris De Lorenzo; no independent validation of the evaluation methodology)
- **Quote**: "Using plugin-based coding assistants is like trying to bolt AI onto your workflow from the outside. With Cursor, the agent understands our codebase and works the way NAB works." — Chris De Lorenzo, Principal Engineer
- **Our assessment**: This is the first corpus source to document an explicit enterprise AI coding tool evaluation involving Amazon Q, GitHub Copilot, and Cursor with named selection criteria. The "plugin-based coding assistants" characterization is a specific architectural critique: tools that bolt onto existing IDEs without native context integration underperform tools designed around codebase understanding. For the guide: the three criteria (model flexibility, codebase understanding across heterogeneous stacks, extensibility for internal customization) constitute an enterprise evaluation framework practitioners can adapt.

### Claim 2: Task-appropriate model selection — cheaper models for routine tasks, advanced models for architecture — is a first-class enterprise evaluation criterion for AI coding tools

- **Evidence**: Article describes model flexibility as one of NAB's three selection criteria: "Cheaper models are used for routine, straightforward implementations like front-end UI changes while more expensive thinking models are used for complex, long-running tasks like architecture design."
- **Confidence**: emerging (vendor-reported evaluation criterion; the use-case split is technically coherent and consistent with `blog-cursor-better-models-ambitious-work.md` Claim 3's high-vs.-low complexity task distinction)
- **Quote**: "Cheaper models are used for routine, straightforward implementations like front-end UI changes while more expensive thinking models are used for complex, long-running tasks like architecture design."
- **Our assessment**: This is the most practically actionable evaluation criterion in the source. NAB's model split maps directly onto the Cursor-better-models study's finding that high-complexity tasks grew 68% vs. 22% for low-complexity when better models became available — enterprises want to apply cheaper inference to the 78% of routine tasks and save expensive inference for the 22% of architecture-level decisions. For the guide: any enterprise tool evaluation rubric should include per-task model routing as a criterion, not just headline capability on complex tasks.

### Claim 3: NAB built an internal context engineering library (NAB CEL) using Cursor primitives to centralize institutional knowledge and enforce development standards

- **Evidence**: Article describes NAB CEL as enabling "the organization to centralize institutional knowledge while enforcing development standards," built using "Cursor's primitives."
- **Confidence**: anecdotal (described at summary level; no implementation specifics given in the source)
- **Quote**: (no direct quote; described as part of the extensibility evaluation criterion)
- **Our assessment**: NAB CEL represents a specific enterprise customization pattern: rather than giving individual developers CLAUDE.md-style project context files, NAB built a shared library layer on top of the tool's extension primitives. This is the "shared firm infrastructure" pattern from `blog-anthropic-cowork-enterprise.md` Claim 7 instantiated for a coding tool: individual conventions become org-wide assets. The "enforcing development standards" function is significant for a regulated financial institution — NAB can bake compliance requirements into the context library rather than relying on individual engineer awareness. The guide should name this as an enterprise customization pattern: internal context library built on tool primitives, separating institutional knowledge management from individual tool configuration.

### Claim 4: Intentional enablement strategy — training sessions and sprint days on real production projects — is cited as key to successful enterprise rollout at scale

- **Evidence**: Named quote from Andrew Vaughan, Distinguished Engineer, describing NAB's rollout approach explicitly.
- **Confidence**: anecdotal (single practitioner's characterization of the strategy; no measurement of its ROI vs. self-directed adoption)
- **Quote**: "We were intentional about enablement from the start, setting up tailored training sessions and sprint days where developers use Cursor on real production projects." — Andrew Vaughan, Distinguished Engineer
- **Our assessment**: The "real production projects" qualifier is the load-bearing claim here — it contrasts with training on toy examples or demo codebases. Sprint days on production projects force the tool into NAB's actual tech stack (Java, React, COBOL, Assembly) with real constraints. This is consistent with `blog-cursor-better-models-ambitious-work.md` Claim 2's 4–6 week lag finding: teams that train on toy examples will hit the false plateau; teams that use AI on real production work from day one build genuine capability. For the guide: enterprise rollout should include structured practice on real production projects, not only documentation or demo exercises.

### Claim 5: AI coding tools reduced BizCalc monolith pre-development work from 2 months to 1 week by generating user stories and API specs via Ask Mode and Plan Mode

- **Evidence**: Named engineer (Coby Paterson, Principal Engineer) with specific timeline. "The first two months were going to be dedicated entirely to pre-development tasks." Paterson completed all pre-development in one week using Cursor's Ask and Plan modes. Full migration expected in 2 months vs. 6-month original estimate (3x improvement overall).
- **Confidence**: emerging (named engineer; specific timeline; vendor-sourced; no independent validation)
- **Quote**: "Within a week, Cursor produced better user stories and a more detailed API spec than we could have done manually after months of reverse engineering the system." — Coby Paterson, Principal Engineer
- **Our assessment**: The "better user stories and more detailed API spec" claim is qualitative but coming from the engineer who did the manual alternative. The mechanism is Ask Mode and Plan Mode applied to legacy code comprehension — the AI reads the existing system and generates structured artifacts (user stories, API specs) that traditionally require manual code archaeology. The 3x overall migration improvement (2 months vs. 6) is anchored in a specific named project with a specific engineer, making it more credible than a headline aggregated metric. For the guide: legacy system comprehension (generating structured documentation from existing code) is a high-value near-term use case that produces verifiable artifacts — the AI-generated spec can be reviewed before any migration work begins.

### Claim 6: Assembly mainframe migration was previously categorically impossible due to expertise scarcity; AI tools unblocked it by generating flowcharts and business logic summaries from machine code

- **Evidence**: Named engineer (Harjot Singh, Engineering Manager) describes a project that could not be staffed manually due to Assembly expertise constraints. After using Cursor, the team generates flowcharts and business summaries from Assembly code and progresses 3x faster than expected.
- **Confidence**: emerging (named engineer; specific constraint described; 3x figure is relative to "expected" pace not a baseline pre-AI measurement; vendor-sourced)
- **Quote**: "Before Cursor, we couldn't even think about moving away from Assembly. We just didn't have the expertise or time to tackle an enormous project like this manually." — Harjot Singh, Engineering Manager
- **Quote**: "Without Cursor, the time and cost of this migration would have been greater than the value we'd get from it." — Harjot Singh, Engineering Manager
- **Our assessment**: This is the most novel single claim in the source for the guide. The Harjot Singh quote is not a velocity claim — it is a viability claim. "We couldn't even think about moving away from Assembly" describes a project that was categorically not attempted due to expertise bottleneck, not one that was attempted but slow. AI tools changed the economic calculation by substituting scarce Assembly expertise with AI-generated comprehension artifacts (flowcharts, business summaries). This is distinct from "5-8x faster" claims; it is "moved from impossible to possible." For the guide: the Assembly case establishes a new category of AI value — expertise gap bridging for scarce-knowledge legacy systems — that is separate from velocity improvement on existing work.

### Claim 7: A greenfield Kotlin/Android payment app was completed in 3 weeks vs. 4-month original scope despite the team having no prior Kotlin/Android experience, representing a 5-8x velocity improvement

- **Evidence**: Named engineer (Chris De Lorenzo, Principal Engineer). Original scope: 4 months. Actual completion: less than 3 weeks. Team used Cursor's Composer and Opus models. Explicit statement that the team lacked prior Kotlin/Android experience.
- **Confidence**: emerging (named engineer; specific timeline; vendor-sourced; the "no prior experience" claim is critical because it's what makes this 5-8x plausible — the baseline includes the language ramp-up time AI eliminated)
- **Quote**: "We've seen a 5-8x improvement in development velocity. But the main thing is we wouldn't have even tried to build this app without Cursor." — Chris De Lorenzo, Principal Engineer
- **Our assessment**: The velocity claim (5-8x) is strong but the more interesting clause is "we wouldn't have even tried to build this app without Cursor." The team's lack of Kotlin/Android experience was the barrier — not project complexity, not team capacity. AI eliminated the language learning tax that previously would have disqualified the team from the project or required hiring. This is the same "expertise gap bridging" pattern as the Assembly case (Claim 6) applied to greenfield development: AI enables teams to work in unfamiliar tech stacks without the traditional ramp-up period. The Composer + Opus model pairing is the first named practitioner report in the corpus combining Cursor's agentic mode with Anthropic's Opus model for a greenfield mobile project.

### Claim 8: AI coding tools democratize development by bringing engineers, architects, product, and security into the same workflow — not just accelerating individual engineers

- **Evidence**: Named quote from Chris De Lorenzo, Principal Engineer.
- **Confidence**: anecdotal (single practitioner quote; a framing claim, not an operational measurement)
- **Quote**: "Cursor is the first agent platform I've seen that brings engineers, architects, product, and security into the same workflow." — Chris De Lorenzo, Principal Engineer
- **Our assessment**: This framing redefines the value proposition from "individual productivity tool" to "cross-role coordination platform." De Lorenzo's claim is that AI coding tools collapse the handoff boundaries between disciplines — architects don't write separate design docs that engineers then implement; product managers don't produce requirements that engineers then interpret; security reviews don't happen post-implementation. Whether this is an artifact of Cursor specifically or a general property of AI-augmented development is not clear from the source, but the claim is structurally consistent with the NAB CEL pattern (Claim 3): a shared context library can encode standards from all four disciplines (engineering, architecture, product, security) into the tool's behavior. For the guide: frame AI coding tool adoption as cross-discipline infrastructure, not an engineering-department productivity initiative.

### Claim 9: AI tool adoption at NAB expanded beyond 6,000 engineers to 10,000+ employees including product management, design, and leadership, with function-specific training paths

- **Evidence**: Article states "NAB is now bringing Cursor to over 10,000 employees across its technology organization," including expansion to "product management, design, and leadership roles with function-specific training paths."
- **Confidence**: emerging (stated as current/near-term rollout; no timeline given for the 10,000 completion; vendor-sourced)
- **Quote**: (no direct quote for this claim; described in the article as current rollout scope)
- **Our assessment**: The 10,000-employee figure represents a 67% expansion beyond the initial 6,000 engineering standardization, reaching non-engineering technology roles. "Function-specific training paths" implies NAB has differentiated the tool's use cases by role — product managers likely use different modes and context than engineers. This corroborates `blog-anthropic-cowork-enterprise.md` Claim 6 (non-engineering adoption of AI tools for "surrounding work"), but extends it to a coding-focused tool: at NAB, the coding tool is not just for engineers. For the guide: the 10,000 expansion with function-specific training is evidence that AI coding tools' value extends to product management, design, and leadership in technology organizations when onboarding is role-differentiated.

### Claim 10: NAB's near-term roadmap extends AI tools to code review, QA testing, and deployment — re-thinking engineering processes around agents rather than bolting AI onto existing processes

- **Evidence**: Named quote from Caroline Trang, Head of AI Tooling & Delivery, describing the forward roadmap.
- **Confidence**: anecdotal (stated intentions; not yet implemented)
- **Quote**: "We want to bring Cursor to code review, quality assurance testing, and deployment. Re-thinking our engineering processes around agents is a key area of investment for NAB." — Caroline Trang, Head of AI Tooling & Delivery
- **Our assessment**: The "re-thinking engineering processes around agents" framing is the most strategically significant future claim in the source. It explicitly rejects "bolt AI onto existing workflow" (De Lorenzo's critique of plugin-based tools in Claim 1) and commits to redesigning the SDLC around agents rather than using agents to accelerate existing steps. The roadmap (code review → QA testing → deployment) mirrors Amplitude's stated roadmap from `blog-cursor-amplitude-autonomous-pipeline.md` Claim 9, which is planning CI/CD and deployment automation from a similar current state (strong code generation, moving toward full pipeline automation). For the guide: the full SDLC automation roadmap (generation → review → QA → deployment) is now described independently by two named enterprise practitioners (Amplitude and NAB), increasing confidence that this is the standard enterprise AI adoption arc.

## Concrete Artifacts

### Enterprise Tool Evaluation Summary

```
NAB AI Coding Tool Evaluation (April 2026, Cursor blog)

Evaluated tools: Amazon Q, GitHub Copilot, Cursor
Selected: Cursor for 6,000-developer standardization (scaling to 10,000+)

Selection criteria:
  1. Model flexibility
     - Task-based model routing: cheaper models for routine front-end/UI work;
       advanced "thinking models" for architecture and complex long-running tasks
     - Enables cost optimization across the task spectrum

  2. Codebase understanding
     - NAB operates thousands of repositories across multiple GitHub accounts
     - Tech stack: Java, React, COBOL, Assembly
     - Cursor demonstrated superior performance in heterogeneous multi-repo environments
     - Characterization: "plugin-based coding assistants" vs. native codebase integration

  3. Extensibility and control
     - NAB built internal context engineering library (NAB CEL) on Cursor primitives
     - Centralizes institutional knowledge while enforcing development standards
     - Enables org-wide standard enforcement, not individual configuration

Eliminated competitors:
  - Amazon Q: not selected (exact failure criterion not described in source)
  - GitHub Copilot: not selected; characterized as "plugin-based" approach
```

### Three Named Project Outcomes

```
Project 1: BizCalc Monolith-to-Microservices Migration
  Lead:        Coby Paterson, Principal Engineer
  Modes used:  Ask Mode, Plan Mode
  Pre-dev work: 1 week (vs. 2-month original estimate) — 8x compression
  Full migration: 2 months expected (vs. 6-month original estimate) — 3x compression
  Mechanism:   AI-generated user stories + API specs from legacy code reverse engineering
  Quote:       "Within a week, Cursor produced better user stories and a more detailed
                API spec than we could have done manually after months of reverse
                engineering the system."

Project 2: Assembly Mainframe Migration (core banking)
  Lead:        Harjot Singh, Engineering Manager
  Speed:       3x faster than expected (no pre-AI baseline; project was previously
                categorically not attempted)
  Mechanism:   AI-generated flowcharts and business logic summaries from Assembly code
  Key insight: Expertise bottleneck removed — team lacked Assembly knowledge; AI
                bridged the gap
  Quote:       "Before Cursor, we couldn't even think about moving away from Assembly.
                We just didn't have the expertise or time to tackle an enormous project
                like this manually."
  Quote:       "Without Cursor, the time and cost of this migration would have been
                greater than the value we'd get from it."

Project 3: Hardware-Agnostic Payment App (greenfield Kotlin/Android)
  Lead:        Chris De Lorenzo, Principal Engineer
  Duration:    Less than 3 weeks (vs. 4-month original scope)
  Modes used:  Composer, Opus models
  Team context: No prior Kotlin/Android experience
  Velocity:    5-8x improvement in development velocity
  Key insight: "Wouldn't have even tried to build this app without Cursor" — expertise
                gap (unfamiliar language) was the barrier, not complexity
```

### Enablement Strategy Pattern

```
NAB Enterprise Enablement Strategy (attributed to Andrew Vaughan, Distinguished Engineer)

Approach:
  - Training sessions: tailored by role/function (not generic onboarding)
  - Sprint days: developers use Cursor on real production projects, not toy examples
  - Expansion: function-specific training paths for product, design, leadership

Scale:
  - Phase 1: 6,000 engineers standardized
  - Phase 2: 10,000+ across technology organization (ongoing)

Philosophy:
  - "Intentional about enablement from the start"
  - Training on real production projects (not demos/sandboxes)
  - Function-specific paths (product manager training ≠ engineer training)
```

### Full SDLC Roadmap

```
NAB AI Agent SDLC Roadmap (attributed to Caroline Trang, Head of AI Tooling & Delivery)

Current state (deployed):
  ✓ Code generation (all four projects)
  ✓ Legacy code comprehension (Ask Mode / Plan Mode)
  ✓ Agentic coding (Composer for greenfield work)

Near-term roadmap:
  → Code review (AI-assisted or AI-driven review)
  → Quality assurance testing (QA automation)
  → Deployment (agentic deployment workflows)

Strategic framing:
  "Re-thinking our engineering processes around agents is a key area of investment
   for NAB" — explicitly rejecting "bolt AI onto existing processes" approach
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-amplitude-autonomous-pipeline.md` Claim 9 (Amplitude's near-term roadmap includes CI/CD and deployment automation) — NAB and Amplitude independently describe the same full SDLC automation arc (generation → review → QA → deployment). Two named enterprises targeting the same roadmap increases confidence this is the standard enterprise AI adoption trajectory, not an edge case.
  - `blog-cursor-amplitude-autonomous-pipeline.md` Claim 5 (3x increase in production commits) — The 3x metric appears in both sources but measures different things: Amplitude's 3x is a weekly-commit-volume metric; NAB's 3x is a project-timeline compression metric on specific legacy migrations. Both use 3x as a headline figure, but NAB's is per-project and more easily verifiable against a named baseline. Neither metric is settled; both are emerging.
  - `blog-cursor-better-models-ambitious-work.md` Claim 2 and Claim 3 (4–6 week lag before developers use better models for complex tasks; high-complexity task growth at 68%) — NAB's model selection criterion (advanced models for architecture, cheap models for UI) is the enterprise policy implementation of the behavioral pattern that study observes: developers eventually migrate toward complex tasks with better models. NAB has formalized this as an evaluation requirement rather than waiting for organic discovery.
  - `blog-anthropic-cowork-enterprise.md` Claim 7 (skills built by individuals become shared org infrastructure) — NAB CEL (Claim 3 above) is the same pattern instantiated for a coding tool: individual engineers' accumulated conventions are codified into a shared library that enforces org-wide standards. Both sources independently arrive at the "shared infrastructure" framing for AI tool customization.

- **Extends**:
  - `blog-cursor-self-hosted-cloud-agents.md` Claim 1 (primary enterprise adoption blockers are data security and infrastructure access, not model quality) — NAB's evaluation evidence adds a third dimension: tech stack diversity. NAB's selection of Cursor was partly about superior codebase understanding across heterogeneous stacks (Java, React, COBOL, Assembly). Enterprise blockers include not only security/infrastructure but also multi-language legacy environment support. The self-hosted agents note frames the problem as "where does execution happen?"; this note frames part of the problem as "does the tool understand our codebase?"
  - `blog-anthropic-cowork-enterprise.md` Claim 6 ("surrounding work first" adoption pattern for non-engineering teams) — NAB expands AI coding tools to 10,000 employees including product management, design, and leadership. For a coding tool (not a general AI assistant), this represents a different expansion pattern: non-engineers using a developer tool for adjacent work rather than a productivity tool for peripheral tasks. This extends the adoption arc in a new direction.

- **Tension with**:
  - `blog-bvp-shopify-ai-playbook.md` Claim 1 (Shopify deliberately avoids standardizing on a single AI tool, using Cursor, Claude Code, GitHub Copilot, OpenAI Codex, and Gemini in parallel) — NAB standardized 6,000+ developers on Cursor as a single platform. These are materially different enterprise strategies: Shopify's multi-tool approach optimizes for flexibility and avoids vendor lock-in; NAB's single-tool approach optimizes for institutional knowledge consolidation (NAB CEL requires a single target platform) and consistent codebase understanding. This is not filed as a formal contradiction because the strategies are conditioned on organizational context: NAB's priority is deep COBOL/Assembly/multi-repo integration that requires a single coherent tool; Shopify's priority is developer autonomy and tool churn resilience. The guide should present both as valid strategies with different tradeoffs: single-tool standardization enables deeper institutional customization (NAB CEL pattern) at the cost of flexibility; multi-tool enables flexibility and model diversity at the cost of shared context management.

- **Novel**:
  - **Assembly mainframe expertise-gap bridging** (Claim 6): No prior corpus source documents AI tools enabling previously categorically impossible legacy migration due to expertise scarcity. Every other velocity claim in the corpus describes tasks that were attempted (but slow) before AI. "Couldn't even think about moving away from Assembly" introduces a new AI value category: unblocking work that was not attempted, not merely accelerating work in progress.
  - **Enterprise AI tool evaluation framework** (Claim 1): No prior corpus source documents an explicit multi-tool evaluation (Amazon Q vs. GitHub Copilot vs. Cursor) with named selection criteria. This is the first corpus evidence of how a Fortune-500 financial institution conducted and decided an AI coding tool evaluation.
  - **"Wouldn't have even tried" productivity framing** (Claims 6 and 7): The capability-enablement framing (AI makes previously impossible work viable) is distinct from velocity-improvement framing (3x, 5-8x). Both NAB claims (Assembly migration and Kotlin payment app) include both frames, but the "wouldn't have tried" clause is novel to this source. No other corpus source explicitly describes AI as enabling categorically different project scope choices.
  - **NAB CEL as internal context engineering library** (Claim 3): No prior corpus source documents an enterprise building a shared internal library on AI tool primitives to encode institutional standards. This extends beyond individual CLAUDE.md files or project-level rules to an org-wide, maintained code library.
  - **Function-specific training paths for non-engineering roles** (Claim 9): No prior corpus source documents differentiated AI tool onboarding tracks by job function (engineer vs. product manager vs. designer vs. leader). The function-specific path is a distinct enterprise enablement pattern.

## Guide Impact

- **Chapter on Enterprise AI Adoption (planned, or Ch04/Ch05)**: Add the NAB tool evaluation framework (Claim 1 + 2) as the first corpus evidence for an enterprise AI coding tool evaluation rubric. Three criteria: (1) model flexibility with per-task routing, (2) heterogeneous codebase understanding, (3) extensibility for internal customization. Contrast with Shopify's multi-tool approach (`blog-bvp-shopify-ai-playbook.md` Claim 1) as competing valid enterprise strategies. The guide should present both explicitly rather than recommending one over the other — the decision variable is whether institutional customization (NAB CEL pattern) requires single-tool standardization.

- **Chapter on Legacy Modernization / Technical Debt (planned or Ch05)**: Add the Assembly expertise-gap bridging pattern (Claim 6) as a new AI value category distinct from velocity claims. The framing: AI tools change the economic viability calculation for legacy migration by substituting scarce expertise with AI-generated comprehension artifacts (flowcharts, business summaries). A project that was economically unviable before AI (cost of expertise acquisition > value of migration) becomes viable after AI (AI eliminates the expertise acquisition cost). This is a qualitatively different claim from "3x faster" and deserves explicit naming in the guide.

- **Chapter on Legacy Modernization / Technical Debt (planned or Ch05)**: Add the BizCalc migration pre-development compression pattern (Claim 5) as a concrete use case for AI-assisted legacy code comprehension. Ask Mode and Plan Mode used for reverse engineering → user stories + API specs is a specific workflow the guide can describe. The output (structured artifacts) is reviewable before any migration work begins — this is a low-risk entry point for teams hesitant about AI for legacy work.

- **Chapter on Onboarding and Enablement (planned or Ch02)**: Add the intentional enablement pattern (Claim 4) — sprint days on real production projects with function-specific training — as a recommended enterprise rollout approach. The "real production projects" qualifier distinguishes from generic onboarding; the "function-specific training" distinguishes from one-size-fits-all developer training. Pair with `blog-cursor-better-models-ambitious-work.md` Claim 2's 4–6 week lag finding: enterprises that train on real projects from day one reduce the discovery lag.

- **Chapter on Enterprise Governance / Customization (planned or Ch02/Ch04)**: Add the NAB CEL pattern (Claim 3) as an enterprise evolution of individual CLAUDE.md-style context files. The pattern: identify conventions that should be org-wide → encode in a shared context engineering library built on tool primitives → enforce automatically. This is the engineering equivalent of a code style linter but for AI tool behavior. Pair with `blog-anthropic-cowork-enterprise.md` Claim 7's "skills-as-infrastructure" pattern — both show the same organizational maturity signal: individual AI customizations becoming shared infrastructure.

- **Chapter on Full SDLC Automation (planned or Ch03)**: The convergence of NAB (Claim 10) and Amplitude (`blog-cursor-amplitude-autonomous-pipeline.md` Claim 9) on the same full SDLC roadmap (generation → review → QA → deployment) is strong enough to include as a named pattern: the "AI SDLC extension arc." Any guide section on long-term AI adoption trajectory should cite both sources and present the arc as a validated multi-practitioner observation, not a vendor aspiration.

## Extraction Notes

- **Source is vendor marketing** (~1,000 words, published on Cursor's commercial blog). All claims are vendor-sourced. The five named practitioners and specific timelines provide credibility above typical vendor copy, but no independent validation exists. Treat all metrics as emerging confidence, not settled.
- **"Wouldn't have tried" claims are the most important** for the guide, but the hardest to calibrate. The Assembly migration and Kotlin app cases both include explicit statements that the projects were gated on expertise NAB didn't have. These are memorable and quotable, but they are retrospective practitioner assessments — we cannot verify that the projects truly would not have been attempted without AI, or that alternative approaches (consulting, hiring, outsourcing) were genuinely ruled out.
- **COBOL mentioned but not a focus**: The tech stack diversity claim (Java, React, COBOL, Assembly) includes COBOL, but the described projects focus on Assembly migration and Java/Kotlin work. COBOL-specific use cases are not documented in the source beyond appearing in the tech stack list.
- **Model flexibility quote** (Claim 2): The text "Cheaper models are used for routine, straightforward implementations like front-end UI changes while more expensive thinking models are used for complex, long-running tasks like architecture design" was presented with "As stated" framing in the WebFetch summary, suggesting it is a verbatim quote from the article. The Assayer should verify this quote against the source URL, as the WebFetch tool was used for extraction.
- **No sub-pages followed**: The article is self-contained with no linked sub-pages. No additional pages were fetched.
- **No contradictions filed**: The Shopify multi-tool vs. NAB single-tool tension (noted in Cross-References) does not rise to the level of a filed contradiction — both strategies are context-conditioned and would lead to different advice for different organizations, not materially opposite advice for the same situation. No other corpus source makes claims that directly oppose the claims extracted here.
