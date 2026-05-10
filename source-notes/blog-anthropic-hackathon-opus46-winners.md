---
source_url: https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon
source_type: blog-post
title: "Meet the winners of our Built with Opus 4.6 Claude Code hackathon"
author: Anthropic
date_published: 2026-04-20
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#348"
---

# Meet the winners of our Built with Opus 4.6 Claude Code hackathon

> A five-project showcase from Anthropic's first Claude Code hackathon — 500
> participants, one week, $500 in API credits each — demonstrating that
> domain experts with zero software development background can build and
> deploy production-grade AI systems using Claude Code; four of the five
> primary winners were non-professional developers.

## Source Context

- **Type**: blog-post (Anthropic claude.com, April 20, 2026; ~5 minute read)
- **Author credibility**: First-party Anthropic blog post. This is a curated
  showcase of selected hackathon winners — not an independent study or a
  representative sample of Claude Code usage. Anthropic partnered with
  Cerebral Valley to select 500 participants; six winners shared $100,000 in
  Claude API credits. Claims about participant backgrounds, build metrics, and
  technical implementations come from the participants' own descriptions and
  Anthropic's editorial framing. The metrics (lines of code, hours, latency,
  processing time reduction) are unaudited self-reports. Treat as high-quality
  anecdote, not controlled measurement.
- **Scope**: Five winning projects covering: multi-agent document processing
  (CrossBeam), visual-spec-to-code IDE (Elisa), post-appointment clinical AI
  (PostVisit.ai), vision-based infrastructure assessment (TARA), and real-time
  AI music collaboration (Conductr). Does NOT cover: the full participant pool,
  failure cases, or representative usage — only the five winners Anthropic
  selected as exemplary. The article does not describe the CLAUDE.md contents,
  API configurations, or harness architectures in technical depth.

## Extracted Claims

### Claim 1: Four of five primary hackathon winners were non-professional developers — a personal injury lawyer, a cardiologist, a roads and infrastructure specialist, and an electronic musician

- **Evidence**: Explicit Anthropic characterization of the winner demographics.
  The article names the backgrounds directly: Mike Brown (personal injury
  lawyer), Michał Nedoszytko (Brussels cardiologist, 20 years in healthcare
  software), Kyeyune Kazibwe (formerly at Uganda's Ministry of Works and
  Transport), and Asep Bagja Priandana (electronic musician). Jon McBee is
  the fifth winner; the article implies he is the one professional software
  engineer.
- **Confidence**: settled (Anthropic's own characterization of its hackathon
  winners; backgrounds are named and specific)
- **Quote**: "The winners of our Opus 4.6 hackathon, our first in this series,
  included a personal injury lawyer, a cardiologist, a roads and infrastructure
  specialist, an electronic musician, and one professional software engineer...
  And four out of five winners were not professional developers."
- **Our assessment**: This is the most striking single finding in the article.
  The claim is not that non-developers can produce toy projects — all five
  winners were delivering systems with real production intent (one is being
  explored by a city government, one is built by a practicing cardiologist for
  real patient use). This directly challenges the assumption in the
  `survey-pragmaticengineer-ai-tooling-2026.md` corpus picture (Claim 3 there:
  staff+ engineers are the heaviest agent users at 63.5%) — that sample
  measures engineers, but the domain-expert population may be a larger and
  faster-growing agent user cohort that survey misses entirely.

### Claim 2: A personal injury lawyer built a multi-agent permit processing system without writing or reading a single line of code

- **Evidence**: Direct participant quote. Mike Brown (CrossBeam, first place)
  is a practicing personal injury lawyer in California who built a production
  AI system using Claude Code as the sole implementation mechanism.
- **Confidence**: settled (verbatim participant quote)
- **Quote**: "It's crazy to me that I ended up winning this contest, and I
  didn't write a single line of code. I didn't even read a line of code."
- **Our assessment**: This is the most extreme data point in the corpus for
  the "non-developer using Claude Code" pattern. Brown's contribution was
  entirely domain knowledge (California permit law, the specific failure modes
  of first-submission applications) — the implementation was entirely
  Claude Code's. This demonstrates that the interface for building complex
  multi-agent systems is increasingly natural language and domain expertise,
  not programming skill. The implication for the guide: tool selection and
  interface design for non-developer practitioners is a real design space, not
  a theoretical one.

### Claim 3: CrossBeam demonstrates that multi-agent parallelization can compress a 6-month permit workflow to 20 minutes

- **Evidence**: Participant-reported outcome. CrossBeam deploys parallel
  sub-agents to parse California housing permit blueprints and correction
  letters simultaneously, identifying required fixes and generating action
  plans. The framing: "generate action plans within 20 minutes." Buena Park
  (which permitted only 120 of 8,900 required housing units in 2024) is
  "exploring adoption."
- **Confidence**: emerging (single participant report, unaudited; "within 20
  minutes" is an outcome claim without a controlled baseline)
- **Quote**: "Everyone thinks California has a housing crisis. We don't. We
  have a permit crisis."
- **Our assessment**: The specific architecture is the key artifact — multiple
  sub-agents running in parallel to independently process the blueprint and
  the correction letter simultaneously, then synthesizing into a single action
  plan. This is a concrete real-world instance of the orchestrator-subagent
  pattern from `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7:
  orchestrator-subagent handles "the widest range of problems with the least
  coordination overhead"). The outcome data (6-month delay costing $30,000 per
  homeowner; 90%+ first-submission rejection rate; Buena Park's 120/8,900
  gap) grounds the pattern in a specific high-value domain.

### Claim 4: Systems architecture knowledge without coding ability can become a shippable product in six days using Claude Code

- **Evidence**: Participant quote from Jon McBee (Elisa, second place), who
  built a 39,000+ line, 1,500+ test block-based visual IDE in 30 hours over
  six days using Claude Code. McBee's self-description: knows systems
  architecture, hardware integration, and how to define and test software,
  but relied on Claude Code for implementation.
- **Confidence**: emerging (single participant report; metrics unaudited)
- **Quote**: "I know systems architecture. I know how to integrate hardware.
  I know how to define and test software. Claude Code helped me turn all that
  knowledge into a shippable product in only six days."
- **Our assessment**: The 30 hours / 76 commits / 39,000+ lines / 1,500+
  tests metric is the highest productivity density claim in our corpus for a
  single practitioner using Claude Code. It should not be extrapolated as
  typical — McBee is a high-skill systems thinker even if not a coder —
  but it sets an upper bound on what is achievable when domain knowledge and
  implementation delegation are well-matched. The quote captures the
  mechanism: the practitioner contributes architectural knowledge and
  requirement definition; Claude Code contributes implementation.

### Claim 5: A visual spec-to-code pipeline where users assemble primitives rather than writing code is viable for youth (including a 12-year-old) to deploy production-grade systems

- **Evidence**: Elisa project description. McBee built a block-based visual
  IDE where users snap together primitives (goals, requirements, agents,
  skills, rules, portals, deployments) and AI generates backend code. His
  12-year-old daughter used it to flash microcontroller firmware without
  writing code. McBee named the project after her.
- **Confidence**: anecdotal (single use case; "12-year-old flashed firmware"
  is a product showcase claim, not a usability study)
- **Quote**: "I named this project after my daughter, because she's exactly
  who it's for."
- **Our assessment**: The named primitives — goals, requirements, agents,
  skills, rules, portals, deployments — map closely to the Claude Code mental
  model (CLAUDE.md as goal/rule specification, agents.toml for agent
  configuration, skills for capability definition). The Elisa approach
  makes this architecture visual and composable for non-coders. The firmware
  flashing use case demonstrates that the visual-spec-to-code pipeline
  generalizes beyond software to embedded systems. This is a novel extension
  of the spec-driven development pattern.

### Claim 6: Vision-based infrastructure assessment can compress weeks-long reporting workflows to five hours using Opus 4.6's vision capabilities

- **Evidence**: Participant quote and product description. TARA (Kyeyune
  Kazibwe, formerly Uganda Ministry of Works and Transport) converts dashcam
  footage into road investment appraisals. Opus 4.6's vision capabilities
  analyze surface conditions, distress patterns, and roadside activity; the
  system segments roads by condition, auto-populates costs, and generates
  economic analyses with NPV projections and equity scores.
- **Confidence**: emerging (single participant report; "weeks to five hours"
  is a before/after claim without methodological detail)
- **Quote**: "One click generates a complete PDF report: condition assessment,
  economic analysis, equity findings, sensitivity interpretation, all in one
  document. This process used to take weeks. TARA does it in five hours."
- **Our assessment**: The domain expert background is critical here — Kazibwe's
  government infrastructure experience means the output format (NPV projections,
  equity scores, sensitivity interpretation) is genuine domain-standard, not
  an AI-generated approximation of what such a report might look like. This
  distinguishes TARA from a generic document-generation use case: the
  infrastructure specialist knew exactly what a credible investment appraisal
  required and directed the system to produce it. The vision-to-structured-
  document pipeline (dashcam footage → PDF with economic analysis) is a novel
  workflow pattern for our corpus.

### Claim 7: Real-time AI systems can achieve sub-15ms decision intervals via C compiled to WebAssembly, making latency "musically invisible"

- **Evidence**: Technical description of Conductr (Asep Bagja Priandana,
  Creative Exploration Prize). A C engine compiled to WebAssembly generates
  notes every 15 milliseconds. Total implementation: approximately 4,800 lines
  of JavaScript and WebAssembly.
- **Confidence**: emerging (participant-reported architecture; no independent
  verification of the 15ms figure or whether this achieves subjective
  "invisibility" across music contexts and hardware)
- **Quote**: "musically invisible" (Priandana's description of the latency)
- **Our assessment**: The WebAssembly compilation approach is a concrete
  engineering decision that addresses the specific latency constraint: browser-
  based JavaScript cannot reliably hit 15ms audio-processing intervals, but
  compiled C via WASM can. This is the first source in our corpus documenting
  a latency-critical AI application with specific interval requirements (15ms)
  and a concrete implementation strategy (C → WASM) for meeting them. The
  "make it funky" command interface — users reshape arrangements mid-performance
  via natural language — demonstrates that real-time AI responsiveness and
  natural-language interaction are compatible in the same system.

### Claim 8: Clinical AI built by a domain expert (cardiologist) achieves evidence integration + privacy compliance + patient-controlled data in one week

- **Evidence**: Product description and participant quote. Michał Nedoszytko,
  a Brussels cardiologist with 20 years in healthcare software, built
  PostVisit.ai during a road trip from Brussels to San Francisco. The system
  explains diagnoses in plain language, analyzes visit transcripts, and
  surfaces clinical evidence while maintaining "privacy, security, and clinical
  best practices."
- **Confidence**: anecdotal (single participant, hackathon context; compliance
  claims are not audited or certified)
- **Quote**: "Medicine is based on evidence. And now, by combining health
  records, evidence, and visit data, the patient has complete control and
  understanding of what happens after the visit."
- **Our assessment**: The cardiologist background is load-bearing for the
  privacy and clinical claims — Nedoszytko knows what "clinical best practices"
  means concretely in a way a software engineer building a health app would
  not. The "patient has complete control" framing addresses the privacy
  constraint by design: the architecture flows through patient control rather
  than around it. This represents a different design philosophy from most
  healthcare AI, which typically flows through provider systems. The "built
  during a road trip" detail is relevant: the system required no specialized
  development environment — Claude Code operated on a standard laptop in
  transit.

### Claim 9: Domain experts who can define requirements and tests can substitute Claude Code for implementation skills entirely

- **Evidence**: Synthesis across multiple winner descriptions. The common
  pattern: participants contributed domain knowledge (permit law, cardiology,
  infrastructure assessment, music theory) and specification ability; Claude
  Code contributed implementation. Brown explicitly "didn't write or read a
  line of code." McBee describes converting "knowledge into a shippable
  product."
- **Confidence**: emerging (consistent across 4 of 5 winners; hackathon
  context selects for motivated domain experts, so not representative of
  typical domain-expert-with-Claude-Code outcomes)
- **Quote**: (no single direct quote captures this synthesis; see individual
  claims above)
- **Our assessment**: The pattern across all four non-developer winners is
  consistent: domain knowledge + requirement definition + test specification
  can substitute for coding ability when Claude Code acts as the implementation
  layer. This is not "vibe-coding" (generating code without understanding what
  it should do) — McBee explicitly cites architecture, hardware integration,
  and test definition knowledge. The skill set that becomes load-bearing is
  **knowing what correct behavior looks like**, not knowing how to produce it.
  This reframes the guide's practitioner profile: "who uses Claude Code" is
  not "engineers" but anyone who can specify correct behavior.

### Claim 10: The hackathon metric of 39,000+ lines and 1,500+ tests in 30 hours represents an extreme upper bound for Claude Code productivity under ideal conditions

- **Evidence**: Jon McBee's reported Elisa build statistics: 30 hours, 76
  commits, 39,000+ lines of code, 1,500+ tests. Context: McBee had domain
  knowledge (systems architecture, hardware integration), a well-defined
  problem (visual IDE for youth programming), and was in competition mode
  (motivated, focused, no competing responsibilities).
- **Confidence**: anecdotal (single participant, unaudited, competition
  context; the conditions — domain clarity, focus, motivation — are not
  typical of production software work)
- **Quote**: "30 hours, making 76 commits with more than 39,000 lines of code
  and more than 1,500 tests"
- **Our assessment**: This should be used as an upper-bound data point, not
  a representative productivity claim. The conditions that enabled this rate
  (well-specified domain, no organizational friction, competition motivation)
  rarely co-occur in enterprise software contexts. The more important
  operational lesson is the ratio: 1,500+ tests alongside 39,000+ lines
  suggests the test suite scaled with the codebase, not as an afterthought.
  McBee's explicit claim to "know how to define and test software" is the
  mechanism — tests were part of the specification process, not added post-hoc.

## Concrete Artifacts

### CrossBeam Architecture (from article description)

```
CrossBeam — Multi-Agent Housing Permit Processing
Source: Anthropic hackathon winner profile, April 20, 2026
Builder: Mike Brown (personal injury lawyer, no code written)

Problem domain:
  - California housing permits: 90%+ first-submission rejection rate
  - Average six-month delay costs homeowners $30,000
  - Buena Park: 8,900 units required by 2029; 120 permitted in 2024

Agent architecture:
  - Input: blueprints + correction letters (document pair)
  - Parallel sub-agents: independently analyze blueprint requirements
    and correction letter specifications
  - Output: action plan identifying required fixes, generated within 20 minutes
  - Pattern: orchestrator-subagent with parallel sub-agent document processing

Deployment status: Buena Park (CA) "exploring adoption"
```

### Elisa Build Metrics (from article)

```
Elisa — Visual IDE for Youth Programming
Source: Anthropic hackathon winner profile, April 20, 2026
Builder: Jon McBee (systems architect background)

Build statistics:
  - Total time:   30 hours
  - Duration:     6 days
  - Commits:      76
  - Lines of code: 39,000+
  - Tests:         1,500+

Visual primitives (user-facing building blocks):
  goals, requirements, agents, skills, rules, portals, deployments

Notable demo: builder's 12-year-old daughter flashed microcontroller
firmware without writing code
```

### Conductr Technical Implementation (from article)

```
Conductr — Real-Time AI Music Collaboration
Source: Anthropic hackathon winner profile, April 20, 2026
Builder: Asep Bagja Priandana (electronic musician)

Technical stack:
  - Browser-based MIDI instrument
  - Core engine: C compiled to WebAssembly
  - Total implementation: ~4,800 lines (JavaScript + WebAssembly)
  - Note generation interval: every 15 milliseconds
  - Latency characterization: "musically invisible"

User interface:
  - User plays chord → Claude generates drums, bass, melody, harmony tracks
  - Natural language commands reshape arrangements mid-performance
  - Example command: "make it funky"
```

### TARA Processing Pipeline (from article)

```
TARA — Road Infrastructure Investment Assessment
Source: Anthropic hackathon winner profile, April 20, 2026
Builder: Kyeyune Kazibwe (former Uganda Ministry of Works and Transport)

Input → Output pipeline:
  1. Dashcam footage captured while driving road segment
  2. Opus 4.6 vision analyzes: surface conditions, distress patterns,
     roadside activity
  3. System segments roads by condition category
  4. Auto-populates cost estimates
  5. Generates economic analysis: NPV projections, equity scores,
     sensitivity interpretation

Output: Complete PDF report — condition assessment + economic analysis
        + equity findings + sensitivity interpretation

Processing time: 5 hours (vs. weeks for traditional manual assessment)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 ("For most
    use cases, we recommend starting with orchestrator-subagent. It handles
    the widest range of problems with the least coordination overhead.") —
    CrossBeam's architecture is a direct real-world deployment of this pattern:
    an orchestrator receiving a permit-processing job, dispatching parallel
    sub-agents to handle blueprints and correction letters independently, then
    synthesizing into an action plan. This is the most concrete production
    deployment of orchestrator-subagent in our corpus.
  - `blog-french-owen-coding-agents-feb-2026.md` Claim 6 ("Opus has been
    trained to work across context windows extremely efficiently... You'll
    notice Opus frequently spinning up multiple sub-agents simultaneously") —
    CrossBeam demonstrates this parallel sub-agent delegation in a production
    context, with a specific domain application and business outcome (20-minute
    permit analysis, city government exploration).
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 6 ("With Opus
    4.6, using subagents improved BrowseComp results by 2.8% over single-agent
    runs") — CrossBeam operationalizes the parallel subagent pattern at
    production scale for document processing, extending the benchmark evidence
    with a field deployment.

- **Contradicts**: None filed. The survey finding that staff+ engineers are
  the heaviest agent users at 63.5% (`survey-pragmaticengineer-ai-tooling-2026.md`
  Claim 3) is not contradicted by this source — the survey measured engineers,
  and this source measures a different population (domain experts in a
  competitive hackathon). These are different contexts, not competing claims
  about the same population.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` — CrossBeam extends
    the orchestrator-subagent pattern description with a real production
    deployment showing concrete input types (permit documents), parallel
    sub-agent roles (blueprint analyzer + correction letter analyzer), and
    outcome metrics (20 minutes, potential city adoption). The multi-agent
    coordination patterns source provides the taxonomy; this source provides
    a production instance.
  - `survey-pragmaticengineer-ai-tooling-2026.md` — The hackathon results
    extend the practitioner picture beyond engineers entirely: four domain
    experts (lawyer, cardiologist, infrastructure specialist, musician) built
    production systems, a population the engineer-focused survey does not
    capture. The guide's target audience definition should incorporate this
    extension.
  - `blog-anthropic-harnessing-claude-intelligence.md` — TARA extends the
    vision capability discussion (that source focuses on coding and browsing
    benchmarks) with a production deployment of Opus 4.6 vision for physical
    infrastructure assessment — a domain where vision analysis has direct
    economic stakes (infrastructure investment decisions).

- **Novel**:
  - **Non-developer domain experts as production Claude Code users**: No prior
    corpus source documents a lawyer, cardiologist, or infrastructure official
    building and deploying production AI systems with Claude Code. The
    practitioner notes in our corpus (`practitioner-dadlerj-tin.md`,
    `practitioner-nikolays-postgres-dba.md`, etc.) are all technically
    sophisticated practitioners. This source introduces a qualitatively
    different user population.
  - **"Didn't write or read a single line of code" as a documented production
    outcome**: Brown's complete delegation of implementation to Claude Code —
    with no code inspection — is the most extreme zero-code-involvement claim
    in the corpus. It is not "low-code"; it is zero-code-involvement by a
    practitioner who won a production-system competition.
  - **15ms real-time AI decision interval via C → WebAssembly**: No prior
    corpus source documents latency-critical AI systems with sub-15ms
    requirements and a WASM-based implementation strategy. Conductr is the
    first corpus entry demonstrating real-time AI in a latency-critical domain
    (music generation requires sub-perceptual-threshold response times).
  - **Vision-to-structured-investment-appraisal pipeline**: TARA's dashcam →
    PDF-with-NPV-projections pipeline is a novel vision application pattern not
    documented elsewhere in the corpus. It combines multimodal vision analysis
    with domain-standard economic modeling in a single automated workflow.
  - **Domain knowledge substitution for coding ability**: The explicit
    mechanism — "I know systems architecture...Claude Code helped me turn all
    that knowledge into a shippable product" — articulates a novel practitioner
    posture. Prior corpus sources discuss Claude Code as a productivity
    multiplier for developers; this source documents it as an implementation
    layer for non-developers who can specify but not implement.
  - **Test-driven specification by non-developers**: McBee's 1,500+ tests
    alongside 39,000+ lines, produced by a systems thinker who "knows how to
    define and test software," suggests that test specification is a portable
    skill that transfers to Claude Code context — even without coding ability.

## Guide Impact

- **Chapter 02 (Interaction Patterns / Multi-Agent Orchestration)**: Add
  CrossBeam as the primary production example of orchestrator-subagent
  parallelization. It is the most concrete deployment of the pattern in the
  corpus: a non-developer built it, it is being evaluated for city-level
  deployment, and the domain (regulatory document processing) is generalizable.
  The specific sub-agent roles (blueprint analyzer + correction letter analyzer)
  illustrate how to decompose a document-processing workflow into parallel
  bounded subtasks, operationalizing the context-centric decomposition
  principle from `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 13.

- **Chapter 03 (Agentic Complexity / Real-Time Systems)**: Add Conductr's
  15ms WASM architecture as the corpus's first documented approach to
  latency-critical AI. Current corpus coverage for latency is mostly about
  API response times; Conductr documents a harder constraint (15ms for
  real-time music generation) and a concrete implementation strategy (C →
  WASM). This should anchor any section on latency-critical AI system design.

- **Chapter 04 (Patterns / Practitioner Profiles)**: Add TARA as the
  primary vision-integration pattern example (dashcam footage → structured
  investment appraisals). The pattern — domain-standard output format +
  domain expert directing the AI to produce it — is distinct from generic
  document generation and more useful as a guide example. Add the non-developer
  winner demographic as evidence that the guide's target audience extends
  beyond software engineers to domain experts who can specify correct behavior.

- **Chapter 04 (Patterns / Spec-Driven Development)**: Elisa's visual-
  primitive approach (goals, requirements, agents, skills, rules, portals,
  deployments as snap-together building blocks) is a visual instantiation of
  spec-driven development. McBee's explicit "I know how to define and test
  software" combined with the 1,500+ test count supports a recommendation
  that spec-driven development with Claude Code requires test-specification
  skill more than coding skill. Update any section that implies spec-driven
  development requires software engineering background.

- **Chapter 02 or new chapter on Practitioner Types**: The four non-developer
  winners represent a user posture the guide does not currently address:
  domain experts who can specify requirements and validate outputs but cannot
  implement. A dedicated section on "Claude Code for domain experts" (or
  "non-developer practitioners") would cover: how to frame requirements in
  natural language, how to validate outputs without reading code, how to
  structure parallel agent workflows without programming them. CrossBeam,
  TARA, and PostVisit.ai are three distinct domain applications that could
  each serve as worked examples.

## Extraction Notes

- **Source is a curated showcase, not a representative sample**: All five
  projects were selected by Anthropic and Cerebral Valley as exemplary
  winners. The source provides evidence that these patterns are *achievable*,
  not that they are *typical*. Framing in the guide should reflect this:
  "demonstrated possible" rather than "expected outcome."
- **Metrics are participant self-reports**: Lines of code, hours, processing
  times, and before/after comparisons come from the winners' own descriptions
  in video/demo presentations; none are independently audited. The 39,000+
  lines / 30 hours and "weeks → 5 hours" claims should be cited with this
  proviso.
- **No linked GitHub repos were fetched**: The Prospector's triage mentioned
  "5 GitHub repos" as part of the evidence. These were not fetched for this
  extraction; the claims here come from the article narrative only. A
  follow-up extraction of the GitHub repos (if public) could yield concrete
  CLAUDE.md contents, hook configurations, and architectural code that would
  substantially enrich claims 3, 7, and 9.
- **"One professional software engineer" ambiguity**: The article says McBee
  is the one professional software engineer among the winners, but his quote
  ("I know systems architecture. I know how to integrate hardware...") is
  consistent with a hardware/embedded engineer rather than a software developer
  in the traditional sense. The distinction matters for the guide's practitioner
  profile claims but cannot be resolved from the article alone.
- **PostVisit.ai compliance claims are unaudited**: Nedoszytko's claims about
  "privacy, security, and clinical best practices" are architectural intentions
  from a domain expert, not certifications. The guide should note this if citing
  PostVisit.ai in any context related to healthcare AI compliance.
