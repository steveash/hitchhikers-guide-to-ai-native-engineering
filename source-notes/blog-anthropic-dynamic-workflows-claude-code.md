---
source_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
source_type: blog-post
title: "Introducing dynamic workflows in Claude Code"
author: Anthropic (Claude team, no individual byline)
date_published: 2026-05-28
date_extracted: 2026-05-29
last_checked: 2026-05-29
status: current
confidence_overall: emerging
issue: "#988"
---

# Introducing dynamic workflows in Claude Code

> Official Anthropic product announcement (May 28, 2026) introducing dynamic
> workflows in Claude Code — a research-preview feature that lets Claude
> orchestrate tens to hundreds of parallel subagents, write its own orchestration
> scripts, and verify results before returning them, exemplified by Jarred Sumner's
> 750,000-line Bun Zig-to-Rust rewrite in eleven days.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com/blog,
  May 28, 2026; research preview feature announcement with one concrete case study)
- **Author credibility**: First-party Anthropic announcement — authoritative on what
  the platform provides, which access tiers carry the feature, and what the intended
  use cases are. The Bun case study (Jarred Sumner, creator of Bun) is a named
  practitioner with a verifiable public project, raising evidential weight above an
  anonymous customer example. No individual Anthropic author byline is listed.
- **Scope**: Covers the feature overview (what dynamic workflows do), two access
  methods (direct request and `ultracode` setting), three primary use case categories,
  the Bun Zig-to-Rust rewrite case study with concrete metrics, a token-consumption
  warning, and platform availability. Does NOT cover: SDK integration code, CLAUDE.md
  configuration for workflows, pricing, internal architectural details of how subagent
  orchestration works, or how verification is implemented. Available only as research
  preview — broader practitioner validation is pending.

## Extracted Claims

### Claim 1: Dynamic workflows compress work that "would normally plan in quarters" to days by orchestrating tens to hundreds of parallel subagents in a single session

- **Evidence**: First-party feature description with a concrete case study (Bun rewrite)
  and the headline productivity claim. No controlled A/B benchmark against baseline
  single-agent approach; the Bun rewrite provides the strongest supporting evidence.
- **Confidence**: emerging (vendor headline claim + one named case study; research
  preview means broad practitioner validation is not yet available)
- **Quote**: "Work you'd normally plan in quarters now finishes in days."
- **Quote (scale)**: "tens to hundreds of parallel subagents in a single session"
- **Our assessment**: The quarters-to-days compression is the boldest productivity
  claim in the corpus for a Claude Code feature. The Bun rewrite (eleven days, 750k
  lines Rust, 99.8% test pass) is the supporting evidence Anthropic cites — it is
  a large-scale, publicly verifiable migration, and Jarred Sumner is a named
  practitioner, which makes this more credible than an anonymous customer example.
  The "research preview" qualifier means the claim is vendor-asserted and
  practitioner-validated in one case, not broadly replicated. The corpus should
  treat this as a strong directional signal pending broader access.

### Claim 2: Dynamic workflows dynamically write orchestration scripts — Claude itself generates the coordination logic, not the user

- **Evidence**: First-party architectural description. The "dynamically writes
  orchestration scripts" language distinguishes this from static workflow definitions
  where the user specifies the coordination graph.
- **Confidence**: emerging (vendor architectural claim; mechanism not independently
  verified; research preview)
- **Quote**: "dynamically writes orchestration scripts"
- **Our assessment**: This is the most architecturally significant claim in the
  post. Claude is not executing a user-defined orchestration graph; it is generating
  the graph based on the task. This positions dynamic workflows as a different level
  of abstraction from the five coordination patterns in
  blog-anthropic-multi-agent-coordination-patterns.md — those patterns require the
  practitioner to choose the topology; dynamic workflows allow Claude to choose it.
  The practical implication: practitioners using dynamic workflows declare *what* to
  accomplish; the orchestration *how* is delegated to Claude.

### Claim 3: Dynamic workflows include a built-in verification-before-return step — Claude checks its work independently before results reach the user

- **Evidence**: First-party feature description. The verification is described as
  a built-in property of the workflow execution, not an optional step.
- **Confidence**: emerging (vendor architectural claim; mechanism not described in
  detail; research preview)
- **Quote**: "checking its work before anything reaches you"
- **Our assessment**: This is the safety-relevant claim in the announcement. The
  generator/evaluator split documented in blog-anthropic-harness-long-running.md
  (Claim 2: "outperforms prompting a single agent to self-critique") is implemented
  here as a platform-level primitive inside dynamic workflows. The post also
  mentions "independent verification" and "adversarial testing" as explicit use
  case properties. The phrase "before anything reaches you" implies a hold step
  where outputs are not surfaced until internal checks pass — a meaningful
  architectural commitment to verification quality. Detail on what the verification
  checks or how it signals failure is absent from the announcement.

### Claim 4: Three primary use cases for dynamic workflows are codebase-wide bug hunts and security audits, large migrations spanning thousands of files, and critical work requiring independent attempts and adversarial testing

- **Evidence**: First-party use case framing from the announcement. These three
  categories are the named applications, each with a distinct property (audit
  coverage, migration scale, verification rigor).
- **Confidence**: emerging (vendor framing; one of the three — large migrations —
  is supported by the Bun case study; the other two are stated without named
  examples)
- **Quote**: (no single verbatim quote; the three categories appear as a list in
  the announcement)
- **Our assessment**: The use case taxonomy is operationally useful for
  practitioners evaluating whether to use dynamic workflows vs. standard Claude
  Code sessions. The three categories share a common property: tasks too large or
  risky for a single-pass agent, where parallel decomposition and independent
  verification add value proportional to cost. The "thousands of files" scale
  anchor for migrations is concrete and actionable. The absence of named examples
  for bug hunts and security audits reduces confidence in those categories, though
  they are structurally plausible given the parallel-verification architecture.

### Claim 5: Dynamic workflows are triggered via two paths: a direct request to Claude, or the new `ultracode` setting (effort level "xhigh") that lets Claude autonomously decide when to deploy workflows

- **Evidence**: First-party feature description with named setting (`ultracode`) and
  its effect (sets effort to "xhigh").
- **Confidence**: settled (named setting with described behavior; shipping feature detail)
- **Quote**: `ultracode` (setting name); effort level "xhigh"
- **Our assessment**: The two-path access model is significant for practitioners.
  The direct-request path ("Create a workflow for X") gives explicit control;
  the `ultracode` setting delegates the decision of *when* to use workflows to
  Claude, which is appropriate for users who want maximum automation and are
  comfortable with higher token consumption. The "xhigh" effort level suggests
  `ultracode` is positioned above the existing effort hierarchy — it is not
  simply "high" effort with parallelism added, but a qualitatively different
  operating mode. This is worth monitoring: if users enable `ultracode` for all
  sessions, they may encounter unexpectedly high token costs on routine tasks.

### Claim 6: Jarred Sumner used dynamic workflows to port Bun from Zig to Rust, generating roughly 750,000 lines of Rust with 99.8% of the existing test suite passing in eleven days from first commit to merge

- **Evidence**: Named practitioner (Jarred Sumner, creator of Bun), specific metrics
  (750,000 lines, 99.8% tests, eleven days), and verifiable public project. This is
  the most concrete case study in the announcement.
- **Confidence**: emerging (named practitioner + publicly verifiable project + specific
  metrics; no independent replication of the metrics; the "99.8%" figure and "eleven
  days" appear to be self-reported by Sumner or relayed by Anthropic)
- **Quote**: "roughly 750,000 lines of Rust"
- **Quote**: "99.8% of the existing test suite passing"
- **Quote**: "eleven days from first commit to merge"
- **Our assessment**: This is the strongest piece of evidence in the corpus for
  large-scale AI-driven codebase migration. The Bun rewrite is a real, publicly
  tracked project (Bun is an open-source JavaScript runtime). The metrics are
  specific: 750k lines is a major production codebase by any measure; 99.8% test
  pass rate suggests the migration preserved correctness at scale; eleven days is
  dramatically faster than any comparable human-led rewrite at that scale. The
  prior corpus mention of this rewrite (blog-simonwillison-not-locked-in.md, Claim 5
  via Hashimoto's blockquote) referenced it as a reversibility example without
  the mechanism or metrics — THIS source is the first to document that dynamic
  workflows were the mechanism and to provide the concrete production metrics.

### Claim 7: Progress in dynamic workflows saves automatically, allowing interrupted jobs to resume

- **Evidence**: First-party feature description. No implementation details provided.
- **Confidence**: emerging (vendor capability claim; no mechanism described)
- **Quote**: (no direct verbatim quote; paraphrased from announcement description)
- **Our assessment**: Automatic progress saving addresses a key failure mode for
  long-running agentic work documented in the corpus (e.g., failure-decker-4hr-
  session-loss.md: four-hour session loss from context failure). If dynamic workflows
  checkpoint progress durably, practitioners can interrupt and resume without starting
  from scratch — a meaningful reliability property for jobs measured in hours or days.
  The mechanism (how progress is checkpointed, what counts as a resumable unit) is
  not described in the announcement.

### Claim 8: Dynamic workflows consume substantially more tokens than a typical Claude Code session, requiring careful budget monitoring

- **Evidence**: First-party warning in the announcement. No specific multiplier
  provided (e.g., "5x" or "10x").
- **Confidence**: settled (vendor-acknowledged property of the feature)
- **Quote**: "Dynamic workflows can consume substantially more tokens than a typical
  Claude Code session."
- **Our assessment**: This warning is the most practically actionable claim for
  practitioners starting to use dynamic workflows. "Substantially more" is vague,
  but the recommendation to "start with scoped tasks to understand usage patterns"
  before deploying on large codebases is sound guidance. The parallel-subagent
  architecture means token consumption scales with the number of simultaneous agents
  — "tens to hundreds" of parallel agents implies proportionally higher cost than
  a single-agent session. Practitioners should prototype with small, bounded tasks
  before applying workflows to production-scale migrations.

### Claim 9: Dynamic workflows are available in research preview on Max, Team, and Enterprise plans via Claude Code CLI, Desktop app, VS Code extension, and the Claude API (including Amazon Bedrock, Vertex AI, and Microsoft Foundry)

- **Evidence**: First-party availability matrix from the announcement.
- **Confidence**: settled (vendor-stated availability and access tier for a shipping
  research preview)
- **Quote**: (no single verbatim quote; availability details are stated factually
  in the announcement)
- **Our assessment**: The research preview designation is the key qualifier. Unlike
  general availability, research preview means access may be limited and the feature
  is not considered production-ready by Anthropic. The multi-surface availability
  (CLI, Desktop, VS Code, API, three cloud providers) signals this is intended as a
  broad capability, not a narrow experiment. The Multi-cloud API availability
  (Bedrock, Vertex AI, Microsoft Foundry) is notable: enterprise users on those
  platforms can access dynamic workflows without routing through the Claude API
  directly.

## Concrete Artifacts

### Feature Access Methods

```
# Dynamic workflows in Claude Code — access paths (research preview, 2026-05-28)
# Source: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

METHOD 1 — Direct request:
  Action:  Ask Claude to create a workflow explicitly
  Example: "Create a workflow to migrate these 3,000 files from Python 2 to Python 3"
  Control: User decides when to use workflows

METHOD 2 — ultracode setting:
  Action:  Enable ultracode via the effort menu
  Effect:  Sets effort level to "xhigh"
  Control: Claude autonomously decides when to deploy workflows
  Warning: Higher autonomous token consumption vs. explicit request

COST WARNING:
  "Dynamic workflows can consume substantially more tokens than a typical
  Claude Code session."
  Recommendation: Start with scoped tasks to understand usage before scaling.
```

### Bun Zig-to-Rust Migration Case Study

```
# Bun: Zig-to-Rust rewrite using dynamic workflows (May 2026)
# Source: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
# Practitioner: Jarred Sumner (creator of Bun)

Task:       Port Bun runtime from Zig to Rust
Output:     "roughly 750,000 lines of Rust"
Test pass:  "99.8% of the existing test suite passing"
Timeline:   "eleven days from first commit to merge"
Mechanism:  Dynamic workflows orchestrating parallel subagents

Context in corpus:
  Prior mention: blog-simonwillison-not-locked-in.md (Claim 5) cited
  the Bun Zig-to-Rust rewrite as a programming language lock-in example
  via a Hashimoto quote, but WITHOUT the mechanism or metrics.
  THIS source is the first corpus entry to document:
  (a) that dynamic workflows were the mechanism, and
  (b) the specific production metrics (750k lines, 99.8%, 11 days).
```

### Dynamic Workflows Use Case Matrix

```
# Primary use cases for dynamic workflows (from announcement, 2026-05-28)
# Source: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code

USE CASE 1: Codebase-wide bug hunts and security audits
  Property: Independent verification of coverage
  Scale:    Entire codebase in scope

USE CASE 2: Large migrations spanning thousands of files
  Property: File-scale parallelism
  Scale:    "thousands of files"
  Example:  Bun Zig-to-Rust (750k lines Rust, 99.8% tests, 11 days)

USE CASE 3: Critical work requiring independent attempts and adversarial testing
  Property: Independent verification before results surface
  Scale:    Task complexity (not necessarily file count)
  Pattern:  "checking its work before anything reaches you"

SHARED PROPERTIES across all three:
  - Too large or risky for single-pass agent
  - Parallel decomposition adds value
  - Built-in verification step
  - Substantially higher token cost vs. standard session
```

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-not-locked-in.md** (Claim 5): "Programming language and
    platform lock-in is structurally declining as AI coding agents reduce the cost
    of switching between technologies" — Claim 5 there cited the Bun Zig-to-Rust
    rewrite as a lock-in-declining example via Hashimoto's blockquote, without the
    mechanism or metrics. This source provides both: dynamic workflows were the
    specific mechanism, and the 750k-line/99.8%/11-day metrics are the concrete
    production evidence. This source strengthens Claim 5 of that note substantially.
  - **blog-anthropic-multi-agent-coordination-patterns.md** (Claim 7): "For most
    use cases, we recommend starting with orchestrator-subagent. It handles the
    widest range of problems with the least coordination overhead." Dynamic
    workflows implement the orchestrator-subagent pattern at production scale within
    Claude Code, providing a hosted path to the recommended default pattern without
    requiring practitioners to build their own multi-agent harness.
  - **blog-anthropic-harness-long-running.md** (Claim 2): The generator/evaluator
    split "outperforms prompting a single agent to self-critique." The verification-
    before-return step in dynamic workflows ("checking its work before anything
    reaches you") is the platform-level implementation of this principle — the
    workflow's internal verification is structurally separated from the generation,
    matching the architectural rationale in that note.

- **Extends**:
  - **blog-anthropic-managed-agents-dreaming-outcomes.md** (Claim 6): Managed
    Agents multiagent orchestration (public beta, May 6, 2026) and dynamic workflows
    in Claude Code are parallel mechanisms for multi-agent work on different product
    surfaces. Managed Agents multiagent orchestration is accessed via the Managed
    Agents API (lead agent + specialists, shared filesystem); dynamic workflows are
    accessed via Claude Code CLI/Desktop/SDK (Claude writes its own orchestration
    scripts). Together they represent two paths to production-scale parallel agent
    work. This source is the first to document dynamic workflows as the Claude Code
    surface equivalent.
  - **blog-anthropic-multi-agent-coordination-patterns.md** (Claim 3): The
    information bottleneck is the named failure mode of orchestrator-subagent — 
    "subagents completing bounded tasks may surface cross-cutting insights the
    orchestrator cannot route efficiently." Dynamic workflows address this by having
    Claude dynamically write and modify orchestration scripts, allowing routing
    adjustments mid-workflow. The verification-before-return step additionally
    prevents cross-cutting failures from surfacing to the user undetected.

- **Contradicts**: None filed. No existing corpus note makes claims about dynamic
  workflows that conflict with this source. The `ultracode` setting is new to the
  corpus; the Bun metrics add specificity to a previously evidence-free Hashimoto
  claim without contradicting it.

- **Novel**:
  - **Dynamic workflows as a named Claude Code feature**: No prior corpus source
    documents dynamic workflows as a feature of Claude Code with specific invocation
    methods. This is the first corpus entry for this capability.
  - **`ultracode` as a named Claude Code operating mode**: The `ultracode` setting
    and its "xhigh" effort level are novel to the corpus. The only prior corpus
    discussion of effort levels is in auto mode (blog-anthropic-claude-code-auto-mode.md),
    which covers the classifier-based permission tier; `ultracode` adds a new level
    above the existing effort hierarchy.
  - **Verification-before-return as a named architectural property of Claude Code
    workflows**: Prior sources discussed evaluation in the context of the
    generator/evaluator harness pattern (blog-anthropic-harness-long-running.md) or
    the Managed Agents outcomes feature (blog-anthropic-managed-agents-dreaming-outcomes.md
    Claim 4). This is the first source to name verification-before-return as a
    built-in property of Claude Code workflow execution — distinct from external
    evaluator harnesses.
  - **Bun case study with production metrics**: The first corpus entry documenting
    that a 750k-line production codebase migration (Zig to Rust) was completed in
    eleven days using dynamic workflows, with 99.8% test retention. Prior corpus
    sources mentioned the Bun rewrite conceptually (simonwillison-not-locked-in);
    none documented the mechanism or metrics.
  - **Research-preview large-scale refactoring via Claude Code**: Prior large-scale
    AI migration evidence in the corpus came from third-party tools (Cursor NAB,
    blog-cursor-nab-legacy-migration.md). This is the first first-party Anthropic
    evidence for a 750k-line migration using a Claude Code-native feature.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add `ultracode` as a named Claude Code setting
  for practitioners who want maximum automation. Document both access paths (direct
  request and `ultracode` setting). The "Work you'd normally plan in quarters now
  finishes in days" headline claim should be contextualized with the token cost
  warning — `ultracode` is not a drop-in replacement for standard sessions on
  routine tasks. The research-preview caveat should be noted.

- **Chapter 02 (Harness Engineering)**: Add dynamic workflows as a Claude Code-native
  alternative to DIY multi-agent harnesses for large-scale tasks. Practitioners who
  would otherwise build an orchestrator-subagent harness from scratch (per
  blog-anthropic-multi-agent-coordination-patterns.md Claim 7) now have a platform
  option: request a dynamic workflow or enable `ultracode`. Update the "Build vs. Buy"
  framing to include Claude Code dynamic workflows as a third option alongside
  self-managed harnesses and Claude Managed Agents.

- **Chapter 03 (Safety and Verification)**: The verification-before-return pattern
  ("checking its work before anything reaches you") should be documented as a
  built-in verification primitive for dynamic workflows. Connect to the
  generator/evaluator pattern in blog-anthropic-harness-long-running.md Claim 2 —
  dynamic workflows implement this at the platform level without requiring the
  practitioner to build a separate evaluator. Note the caveat: the verification
  mechanism's specifics are not documented in the announcement; practitioners
  should treat this as a helpful default, not an auditable safety guarantee.

- **Chapter 05 (Large-Scale Refactoring and Migrations)**: The Bun case study
  (Claim 6: 750k lines Rust, 99.8% tests, eleven days) is the most concrete
  large-scale AI migration evidence in the corpus and should anchor this chapter's
  "what is achievable" section. Pair with blog-cursor-nab-legacy-migration.md (NAB
  Assembly mainframe migration) and blog-simonwillison-not-locked-in.md (Claim 5,
  lock-in decline) to form a multi-source account of agent-driven large-scale
  rewrites. The Bun case uniquely provides: (a) the specific mechanism (Claude Code
  dynamic workflows), (b) the scale (750k lines), and (c) the quality metric (99.8%
  test retention).

- **Chapter 05 (Large-Scale Refactoring)** — update lock-in section: The Bun
  metrics in Claim 6 here should be added to the discussion of blog-simonwillison-
  not-locked-in.md Claim 5. That note mentioned the Bun rewrite via Hashimoto's
  blockquote without mechanism or metrics; adding the mechanism (dynamic workflows)
  and metrics (750k lines, 99.8%, 11 days) makes the lock-in-declining argument
  significantly more concrete.

## Extraction Notes

- Source fetched May 29, 2026. The WebFetch tool returned summaries rather than
  full verbatim text on both attempts; quotes in this note are drawn from the
  most consistent passages across two separate fetches. Verbatim quotes marked
  as confirmed appeared identically or very closely in both fetches. The headline
  quote ("Work you'd normally plan in quarters now finishes in days.") was
  explicitly surfaced as a direct quote by both fetch attempts.
- The blog post is described as a research-preview announcement with no implementation
  detail or SDK code. Sub-pages were not linked from the announcement; no
  documentation links were identified to follow.
- The Bun case study attributes the rewrite to Jarred Sumner specifically. The
  metrics (750k lines, 99.8%, eleven days) are credited to Sumner's use of
  dynamic workflows. Sumner is a high-credibility named source (public figure,
  open-source project creator), but the metrics are self-reported or vendor-relayed
  — not independently validated.
- The `ultracode` setting sets effort level to "xhigh." The relationship between
  `ultracode` and the existing effort levels in Claude Code (normal/high/etc.) was
  not described in detail in the announcement. The auto-mode architecture
  (blog-anthropic-claude-code-auto-mode.md) covers the classifier-based permission
  tier; `ultracode` appears to be a separate effort/complexity dimension rather
  than a permission tier.
- No pricing or specific token multiplier for dynamic workflows was mentioned.
  The "substantially more tokens" warning is qualitative.
