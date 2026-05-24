---
source_url: https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon
source_type: blog-post
title: "Meet the winners of our Built with Opus 4.6 Claude Code hackathon"
author: Anthropic (Claude team)
date_published: 2026-04-20
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#348"
---

# Meet the winners of our Built with Opus 4.6 Claude Code hackathon

> A five-project hackathon showcase that provides the strongest first-party
> evidence in the corpus that domain experts without programming backgrounds
> can ship production-grade AI systems with Claude Code — across law, medicine,
> music, and infrastructure engineering — and documents concrete patterns for
> document parsing agents, spec-driven development, and real-time AI at 15ms
> latency intervals.

## Source Context

- **Type**: blog-post (official claude.com blog, April 2026; post-hackathon
  winner announcement)
- **Author credibility**: Published on Anthropic's Claude blog. First-party
  Anthropic editorial post featuring five winning projects from a structured,
  judged competition (500 participants, $100,000 in prizes). Claims about what
  was built are grounded in specific GitHub repos and named individuals with
  verifiable backgrounds (a personal injury lawyer, a cardiologist, a musician).
  Evidence quality is concrete (named metrics, code stats, processing times),
  not marketing abstraction. Treat as high-credibility anecdotal evidence from
  a structured competition, not as a controlled study.
- **Scope**: Covers five winning projects: CrossBeam (1st, permit processing),
  Elisa (2nd, visual IDE for kids), PostVisit.ai (3rd, clinical AI), TARA
  (Keep Thinking prize, road infrastructure assessment), Conductr (Creative
  Exploration prize, real-time MIDI). The post includes direct quotes from each
  winner and specific technical metrics. Does NOT cover: architecture diagrams,
  model-level details (temperature, prompting strategy), cost, or failure cases
  encountered during development. The hackathon ran for one week with $500 in
  API credits per participant.

## Extracted Claims

### Claim 1: A non-developer (personal injury lawyer) won first place by building a production permit-processing system without writing any code

- **Evidence**: Named individual (Mike Brown, personal injury lawyer), named
  project (CrossBeam), named problem (California housing permit crisis), named
  outcome (first-place winner), direct quote on code involvement.
- **Confidence**: emerging (single verifiable anecdote from a structured
  competition with named participants and public judges)
- **Quote**: "It's crazy to me that I ended up winning this contest, and I
  didn't write a single line of code. I didn't even read a line of code."
- **Our assessment**: This is the strongest single evidence point in the corpus
  for the claim that Claude Code enables non-developers to ship production
  systems. The first-place win (not just participation) in a field of 500
  competitors elevates this above typical anecdote. Brown is a personal injury
  lawyer — his competitive advantage was domain knowledge of the permit system,
  not software skill. The mechanism is clear: Claude Code translated domain
  expertise into working software. For the guide, this is not merely an
  accessibility story — it is a pattern claim: domain expertise may substitute
  for programming skill when the development task maps cleanly to structured
  knowledge (document parsing, classification, action generation).

### Claim 2: AI document parsing for permit processing reduced turnaround from months to approximately 20 minutes

- **Evidence**: Named project (CrossBeam), named domain problem (California
  permit crisis), stated processing time reduction (months → ~20 minutes),
  described mechanism (parse blueprints and correction letters → generate
  action plans for builders).
- **Confidence**: anecdotal (single project report; reduction magnitude not
  independently verified)
- **Quote**: "Everyone thinks California has a housing crisis. We don't. We have
  a permit crisis."
- **Our assessment**: The months-to-20-minutes claim is plausible given the
  described mechanism (LLM-based document classification and action plan
  generation vs. manual review queues). The important pattern for the guide is
  not the specific time reduction — which is domain-specific — but the
  architectural form: structured document ingestion + AI extraction +
  action plan generation. This is the orchestrator-subagent pattern applied
  to civic tech. The non-developer winner using this architecture demonstrates
  that document-parsing agent pipelines are within reach for domain experts
  without engineering backgrounds.

### Claim 3: Spec-driven development with AI code generation produced 39,000+ lines of code in 30 hours — with 1,500+ tests

- **Evidence**: Named project (Elisa, a visual IDE for middle-school
  programmers), named developer (Jon McBee, software engineer), specific
  quantified outputs: 39,000+ lines of code, 1,500+ tests, 76 commits, 30
  hours of work over 6 days. Named real-world validation: daughter used it
  for a 7th-grade science fair project.
- **Confidence**: emerging (specific metrics from a named individual in a
  verifiable competition; developer is a software engineer, so output quality
  is harder to attribute solely to Claude Code)
- **Quote**: "I know systems architecture. I know how to integrate hardware.
  I know how to define and test software. Claude Code helped me turn all that
  knowledge into a shippable product in only six days."
- **Our assessment**: The McBee quote is the clearest articulation in the
  corpus of how domain knowledge (systems architecture, hardware integration,
  software testing) functions as the input that Claude Code amplifies. McBee
  is a professional software engineer — so unlike Brown, he could have built
  this without Claude Code. The claim is about velocity, not feasibility. The
  spec-driven workflow described (users design via visual primitives, Claude
  Code generates corresponding code) is a form of visual-specification-to-code
  translation. The 1,500+ test count suggests the development was test-first
  or test-alongside — consistent with spec-driven approaches where the spec
  defines expected behavior before implementation. 39,000 lines in 30 hours
  is roughly 1,300 lines/hour, which is not credible without significant
  AI-assisted generation.

### Claim 4: Real-time AI music generation with 15ms decision intervals achieves perceptually invisible latency

- **Evidence**: Named project (Conductr), named developer (Asep Bagja
  Priandana, electronic musician), specific metrics: 4,800 lines of JavaScript
  and WebAssembly, note generation every 15 milliseconds. Direct quote on
  latency perception.
- **Confidence**: emerging (specific technical metrics from a named individual;
  the 15ms figure is specific and technically plausible for WebAssembly-based
  audio generation)
- **Quote**: Latency is "musically invisible."
- **Our assessment**: 15ms is below the 20ms threshold typically cited for
  perceptible audio latency — making the "musically invisible" claim
  technically credible. The use of WebAssembly (rather than pure JavaScript)
  for the latency-critical path is the architecturally notable detail: it
  suggests the builder (a musician, not a systems programmer) was guided to
  WebAssembly by Claude Code for the performance-critical path. This is the
  only project in the hackathon that demonstrates real-time AI with hard
  latency constraints. The pattern — AI-generated content at sub-human
  reaction-time intervals — is novel in the corpus and relevant to any
  application where AI must operate in a time-synchronous rather than
  request-response mode.

### Claim 5: Vision-based infrastructure assessment reduced dashcam footage analysis from weeks to 5 hours

- **Evidence**: Named project (TARA), named developer (Kyeyune Kazibwe),
  specific output structure (condition assessment + economic analysis + equity
  findings + sensitivity interpretation in one PDF), specific processing time
  reduction (weeks → 5 hours). Direct quote from developer.
- **Confidence**: anecdotal (single project report; reduction not independently
  verified)
- **Quote**: "One click generates a complete PDF report: condition assessment,
  economic analysis, equity findings, sensitivity interpretation, all in one
  document. This process used to take weeks. TARA does it in five hours."
- **Our assessment**: TARA's architecture is a multi-stage pipeline:
  vision model analyzing dashcam footage → surface condition classification →
  distress pattern identification → economic analysis computation → PDF report
  generation. Each stage feeds the next. The "one click" framing is UX
  design, not architecture; the architectural claim is that this pipeline can
  be built by a non-developer and reduce expert labor from weeks to hours. The
  equity findings component is notable — it suggests the pipeline includes a
  judgment layer (which roads are in underserved areas?) beyond pure computer
  vision. This is the most technically complex project in the hackathon and the
  one most directly analogous to an agent orchestration pattern.

### Claim 6: A cardiologist built privacy-aware clinical AI integrating patient records with clinical evidence without a software development background

- **Evidence**: Named project (PostVisit.ai), named developer (Michał
  Nedoszytko, Brussels-based cardiologist), described functionality (explains
  diagnoses in plain language, analyzes visit notes, integrates patient records
  with clinical evidence, patient understanding between appointments). Direct
  quote on the clinical AI's purpose.
- **Confidence**: anecdotal (single practitioner report from a competition
  setting)
- **Quote**: "Medicine is based on evidence. And now, by combining health
  records, evidence, and visit data, the patient has complete control and
  understanding of what happens after the visit."
- **Our assessment**: PostVisit.ai operates in a privacy-sensitive domain
  (patient health records) and was built by a domain expert (cardiologist)
  without software development background. The system integrates multiple
  data sources (health records, clinical evidence, visit data) and generates
  patient-facing explanations — a non-trivial context assembly and output
  generation task. The fact that a cardiologist built this in a one-week
  hackathon suggests that domain experts in regulated industries can now
  prototype clinical AI tools without engineering teams, which has implications
  for both the speed of clinical AI prototyping and the risks (a non-developer
  cardiologist may not implement proper privacy controls).

### Claim 7: Four of five main hackathon winners were non-professional developers

- **Evidence**: Explicit statement in the source about winner demographics.
  Winners: Brown (personal injury lawyer), McBee (software engineer),
  Nedoszytko (cardiologist), Kazibwe (background not specified), Priandana
  (electronic musician). Only McBee is a professional software developer.
- **Confidence**: settled (stated explicitly by Anthropic as a notable
  pattern from the competition; verifiable from winner descriptions)
- **Quote**: (no direct quote; stated as a notable finding in the post's
  framing)
- **Our assessment**: This is the most important structural finding from the
  hackathon for the guide. A 500-person competition selecting for best projects
  produced first-place results from domain experts outside software engineering.
  This is not an accessibility anecdote — it is a competitive result. The
  pattern across winners is consistent: lawyers, doctors, musicians, and
  infrastructure analysts translated deep domain knowledge into working software
  because Claude Code handled the translation. The implication for the guide's
  framing of Claude Code: it is not primarily a developer productivity tool
  but a domain-expertise-to-software translator with developer productivity as
  one application.

### Claim 8: The competitive hackathon structure (500 participants, $100,000 prize pool, one week) produced production-quality systems across five unrelated domains

- **Evidence**: Stated competition parameters: 500 participants, $500 in API
  credits each, $100,000 total prize pool, one-week duration. Five winners
  span: civic tech (permit processing), education (visual IDE), healthcare
  (clinical AI), infrastructure (road assessment), music (MIDI generation).
- **Confidence**: settled (competition parameters stated by Anthropic; winner
  domains observable from project descriptions)
- **Quote**: (no direct quote; structural observation from competition setup
  and winner selection)
- **Our assessment**: The diversity of winning domains in a single one-week
  competition provides evidence that Claude Code's domain generality is not
  narrowly bounded. The $500 API credit limit constrains what could be built —
  the winning projects had to be cost-efficient. The one-week constraint filters
  for approaches that move fast, which inherently favors AI-assisted development.
  These constraints make the competition results informative: the patterns that
  won are the patterns that work quickly and cheaply, which is exactly the
  profile relevant to practitioners building with Claude Code.

### Claim 9: Domain experts translate professional knowledge — not just task descriptions — into shippable products using Claude Code

- **Evidence**: Pattern across all five winners. Brown (law: permit
  regulations + document classification), McBee (systems architecture + test
  design), Nedoszytko (medical evidence + clinical record structure),
  Kazibwe (infrastructure engineering + economic analysis frameworks),
  Priandana (music theory + MIDI protocol + audio latency requirements).
- **Confidence**: emerging (consistent pattern across five independent projects
  in a single competition; not generalizable beyond competition context without
  additional evidence)
- **Quote**: "I know systems architecture. I know how to integrate hardware.
  I know how to define and test software. Claude Code helped me turn all that
  knowledge into a shippable product in only six days." (McBee)
- **Our assessment**: McBee's quote articulates the pattern that applies across
  all five winners: each brought a domain knowledge layer that Claude Code
  could not substitute (what does a permit correction letter mean? what
  constitutes clinically sound patient communication? what is musically
  invisible latency?) and Claude Code contributed the software translation layer
  (how do you parse a PDF? how do you generate a WebAssembly audio buffer?
  how do you structure a REST API?). The guide's current framing of Claude
  Code as a developer productivity tool needs to be extended: it is a
  domain-expertise amplifier whose output is software.

## Concrete Artifacts

### Winner Summary Table

```
Built with Opus 4.6 Claude Code Hackathon — Winner Summary
(Anthropic, April 2026; 500 participants, $100k prize pool, 1 week)

Prize              | Builder          | Background        | Project     | Domain
-------------------|-----------------|-------------------|-------------|------------------
1st Place          | Mike Brown       | Personal injury   | CrossBeam   | Permit processing
                   |                 | lawyer            |             | (months → ~20 min)
2nd Place          | Jon McBee        | Software engineer | Elisa       | Visual IDE for kids
                   |                 |                   |             | (39k lines, 1500 tests, 30h)
3rd Place          | Michał           | Cardiologist      | PostVisit   | Clinical AI
                   | Nedoszytko      |                   |             | (patient records + evidence)
Keep Thinking      | Kyeyune Kazibwe  | (unspecified)     | TARA        | Road infrastructure
                   |                 |                   |             | (dashcam → 5h vs. weeks)
Creative           | Asep Bagja       | Electronic        | Conductr    | Real-time MIDI
Exploration        | Priandana        | musician          |             | (15ms intervals)
```

### Elisa Development Metrics

```
Elisa (visual IDE for middle-school programmers)
Builder: Jon McBee (software engineer)
Development window: 6 days / 30 hours

Output metrics:
  Lines of code:  39,000+
  Tests:          1,500+
  Commits:        76
  Time-to-ship:   30 hours total

Development pattern:
  - Block-based visual IDE: user designs via visual primitives
  - Claude Code generates code corresponding to visual design
  - Test-alongside development (1,500 tests across ~39,000 lines ≈ 3.8% test density)
  - Validated by daughter using it for 7th-grade science fair project

Source: Anthropic hackathon post, April 2026
```

### Conductr Technical Specs

```
Conductr (browser-based MIDI instrument with AI accompaniment)
Builder: Asep Bagja Priandana (electronic musician)

Technical parameters:
  Total code:       ~4,800 lines (JavaScript + WebAssembly)
  Note generation:  every 15 milliseconds
  Latency target:   "musically invisible" (< ~20ms perceptual threshold)

Architecture pattern:
  - WebAssembly for latency-critical note generation path
  - AI generates musical accompaniment in real-time from user input
  - Browser-based (no local install)

Source: Anthropic hackathon post, April 2026
```

### TARA Pipeline Description

```
TARA (dashcam footage → road infrastructure investment appraisal)
Builder: Kyeyune Kazibwe

Pipeline stages (inferred from description):
  1. Dashcam footage ingestion
  2. Surface condition classification (road distress patterns)
  3. Economic analysis (investment cost / benefit)
  4. Equity analysis (geographic/demographic context)
  5. Sensitivity interpretation
  6. PDF report generation (one click)

Metrics:
  Before: weeks of expert analysis
  After:  5 hours end-to-end

Output format: "condition assessment, economic analysis, equity findings,
  sensitivity interpretation, all in one document"

Source: Direct quote from Kyeyune Kazibwe, Anthropic hackathon post, April 2026
```

### CrossBeam Pipeline Description

```
CrossBeam (California housing permit processing)
Builder: Mike Brown (personal injury lawyer)

Pipeline stages (inferred from description):
  1. Ingest permit documents (blueprints, correction letters)
  2. AI parsing of document content
  3. Action plan generation for builders and municipalities

Metrics:
  Before: months of permit processing time
  After:  approximately 20 minutes

Builder's involvement: "I didn't write a single line of code. I didn't even
  read a line of code."

Source: Anthropic hackathon post, April 2026
```

## Cross-References

- **Corroborates**: `blog-anthropic-multi-agent-coordination-patterns.md` —
  CrossBeam's permit document parsing pipeline (ingest documents → classify
  content → generate action plans) is consistent with the orchestrator-subagent
  pattern described in Claim 7 of that note ("the recommended default pattern").
  TARA's multi-stage vision-to-report pipeline maps to the same pattern. The
  hackathon results provide practitioner evidence that this pattern is accessible
  to non-developers, not just to engineers who study coordination topologies.

- **Corroborates**: `blog-anthropic-maccoss-developer-onboarding.md` — Claim 1
  in that note (developer onboarding analogy as the key mental model) is
  substantiated by McBee's quote: "I know systems architecture... Claude Code
  helped me turn all that knowledge into a shippable product." Both sources
  describe the same mechanism: the user's pre-existing domain knowledge is the
  input; Claude Code supplies the software translation. The maccoss note frames
  this from a 17-year developer's perspective; the hackathon provides evidence
  that the same mechanism works for non-developers in one week.

- **Extends**: `blog-anthropic-multi-agent-coordination-patterns.md` —
  That note covers coordination topology (how agents coordinate). This source
  covers domain application (what non-developers build with agents). Together
  they establish: (1) the architectural vocabulary for agentic systems, and
  (2) the accessibility of those architectures to domain experts who cannot
  name the patterns they are using. The hackathon's non-developer winners are
  using orchestrator-subagent patterns without knowing the term.

- **Extends**: `blog-anthropic-maccoss-developer-onboarding.md` — The
  developer-onboarding analogy in that note applies when a professional developer
  is building context for an experienced developer's workflow. The hackathon
  extends this: domain experts without developer background are the most
  interesting case — they bring domain knowledge but no software architecture
  instinct, making Claude Code's translation role more complete.

- **Novel**:
  - **Non-developer competitive wins at scale**: The corpus contains practitioner
    anecdotes of non-developers using Claude Code, but no prior source documents
    a structured competition where non-developers outcompeted in a field of 500.
    Four of five winners without software backgrounds is a structural finding,
    not an anecdote.
  - **Real-time AI at 15ms decision intervals**: Conductr is the only source
    in the corpus documenting AI-assisted generation with hard real-time latency
    constraints (sub-20ms musical timing). The use of WebAssembly for the
    latency-critical path is novel in the corpus.
  - **Vision-based civic infrastructure assessment pipeline**: TARA's
    dashcam-to-investment-appraisal pipeline is a multi-modal agent pipeline
    applied to civic infrastructure — unrepresented in the corpus.
  - **Domain-expertise-to-software translation as the primary value mechanism**:
    The consistent pattern across five winners (deep domain knowledge + Claude
    Code = working software) is named and documented for the first time in the
    corpus. Prior sources note this as a secondary benefit; here it is the
    primary competitive differentiator.
  - **Spec-driven visual-to-code development (Elisa)**: McBee's workflow of
    defining visual specifications and having Claude Code generate corresponding
    code, validated with 1,500+ tests, is the most specific spec-driven
    development pattern in the corpus.
  - **Clinical AI prototyping by non-developer physicians**: PostVisit.ai
    demonstrates that physicians can prototype patient-facing clinical AI
    without engineering support — a pattern with significant implications for
    both speed of clinical AI development and safety risks.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Domain Expert Accessibility**: The
  hackathon provides the guide's strongest evidence base for a non-developer
  audience. Currently Ch02 is written for software practitioners. Add a subsection
  "When the expert is not a developer" citing CrossBeam (law) and PostVisit.ai
  (medicine) as the anchor cases. The document parsing pipeline (CrossBeam) and
  the multi-stage vision pipeline (TARA) should each be documented as accessible
  patterns for domain experts, not just as engineering examples.

- **Chapter 02 (Harness Engineering) — Real-Time AI Architecture**: Conductr's
  15ms latency with WebAssembly is currently unrepresented in Ch02's pattern
  library. Add a subsection on real-time AI — where AI must operate at
  sub-human reaction times in a time-synchronous mode rather than
  request-response. Conductr is the anchor case. The key design pattern is:
  AI generates content at fixed intervals rather than on demand; the
  architectural challenge is minimizing generation latency to below the
  perceptual threshold.

- **Chapter 04 (Context Engineering) — Domain Knowledge as Context**: The
  consistent winner pattern (domain knowledge + Claude Code = software) supports
  a framing of context engineering as knowledge externalization. Domain experts
  who cannot code can still provide high-quality context (what a permit
  correction letter means; what constitutes evidence-based clinical communication)
  that Claude Code uses to generate correct behavior. Add this framing to Ch04's
  "what makes good context" discussion: domain expertise encoded as context is
  as valuable as technical specification.

- **Chapter 03 (Safety and Verification) — Non-Developer Safety Risks**: The
  hackathon's accessibility finding has a safety shadow: a cardiologist building
  clinical AI in a week may not implement appropriate privacy controls, audit
  logging, or clinical validation requirements. Ch03 should note that Claude
  Code's accessibility to non-developers increases both the speed of beneficial
  AI development and the risk that safety requirements are skipped. The
  PostVisit.ai case is the anchor.

- **Chapter 05 (Team Adoption) — Domain Expert Adoption Path**: The hackathon
  provides the strongest evidence that Claude Code adoption should target domain
  experts, not just developers. Add to Ch05's adoption playbook: identify the
  highest-domain-expertise team members (lawyers, doctors, data scientists,
  field engineers) as early Claude Code adopters, not just the highest-engineering-
  skill developers.

## Extraction Notes

- The source was fetched twice to obtain both summary structure and verbatim
  quotes. The quotes extracted (Brown, McBee, Nedoszytko, Kazibwe, Priandana)
  are the direct quotes from the hackathon winners as reported in the article.
  Per MINER.md §2a, these are taken as verbatim from the source; the Assayer
  should verify them against the source URL.
- The first WebFetch extraction returned an intro quote referencing "Opus 4.7"
  rather than "Opus 4.6." The source URL explicitly contains "opus-4-6" and
  the issue title references Opus 4.6. The discrepancy may reflect a WebFetch
  model extraction error rather than the actual source text. This source note
  treats the competition as the "Built with Opus 4.6" hackathon, consistent
  with the URL and issue title. The Assayer should verify the intro text against
  the live source URL to resolve this discrepancy.
- The source mentions "4 of 5 main winners" as non-professional developers.
  An earlier WebFetch noted that "Only 5 of 6 winners detailed; 6th winner not
  identified in article" — this appears to be a WebFetch model error. The
  source documents exactly 5 prize categories and 5 named winners.
- No contradictions with existing source notes were identified. The accessibility
  and non-developer evidence here is novel in the corpus (no prior note
  documents competitive outcomes from non-professional developers at this scale)
  rather than opposing any existing claim.
- Confidence set to `emerging` rather than `settled` because: (1) the winner
  metrics (processing times, code volume) are self-reported in a competition
  context without independent verification; (2) a competition design selects for
  best-in-show, not for typical outcomes; (3) the non-developer accessibility
  finding, while striking, is from a single structured event.
