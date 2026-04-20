---
source_url: https://github.github.com/gh-aw/introduction/how-they-work
source_type: docs
title: "GitHub Agentic Workflows: How They Work"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#254"
---

# GitHub Agentic Workflows: How They Work

> The canonical conceptual reference for GitHub Agentic Workflows — explains
> the two-component workflow structure, the five-layer defense-in-depth security
> pipeline, Safe Outputs as a permission-separation primitive, the compilation
> model from `.md` source to `.lock.yml` executable, and the "Continuous AI"
> framing for systematic agentic software collaboration.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "How They
  Work" reference page; not a blog post or practitioner account)
- **Author credibility**: First-party documentation from the GitHub Agentic
  Workflows team (the same team behind the Peli de Halleux / Don Syme agent
  factory blog series). This is the authoritative conceptual reference for the
  `gh aw` platform, not a practitioner account or blog post. Claims about the
  platform architecture, security model, and compilation behavior are settled
  for this platform; they do not automatically generalize to other agentic
  systems.
- **Scope**: Conceptual overview of how gh-aw workflows operate — structure,
  security architecture, tool integration, compilation model, and "Continuous AI"
  patterns. Does NOT cover: the full architecture stack (that is the companion
  architecture page, issue #253), specific workflow examples (covered in the
  "Meet the Workflows" blog series), failure modes, cost benchmarking, or how
  to choose between engine providers. This page is the conceptual "what and why";
  the architecture page (issue #253) is the structural "how."

## Extracted Claims

### Claim 1: The two-component workflow structure (YAML frontmatter + natural language markdown) enables reliable, secure agentic programming via capability sandboxing

- **Evidence**: The page describes each workflow as containing: (1) frontmatter
  — YAML between `---` markers defining "triggers (when the workflow runs),
  permissions (what it can access), and tools (what capabilities the AI has)";
  (2) markdown instructions — natural language task descriptions that the AI
  interprets. The combination "enables reliable, secure agentic programming by
  sandboxing AI capabilities and triggering at the right moments."
- **Confidence**: settled (first-party documentation of the platform's design)
- **Quote**: "enables reliable, secure agentic programming by sandboxing AI
  capabilities and triggering at the right moments"
- **Our assessment**: The structural insight here is the separation of concerns:
  YAML frontmatter carries the *constraints* (what the agent can do, when it
  runs), while markdown carries the *intent* (what the agent should try to do).
  A human engineer writes both, but they serve different purposes. This is
  declarative harness design — the harness author specifies the sandbox, and
  the agent operates within it. For Ch02 (Harness Engineering): this is a
  concrete, production-proven architecture for harness design. The YAML
  constrains; the markdown instructs. Neither is sufficient alone.

### Claim 2: Agentic workflows make context-sensitive decisions rather than executing deterministic if/then logic, while still running on deterministic CI/CD infrastructure

- **Evidence**: The page draws an explicit contrast: "Traditional workflows:
  execute pre-programmed steps with fixed if/then logic" vs. "Agentic
  workflows: use AI to understand context, make decisions, and generate content
  by interpreting natural language instructions flexibly." The framing: they
  "combine deterministic GitHub Actions infrastructure with AI-driven
  decision-making."
- **Confidence**: emerging (architectural claim about the class of systems, not
  a measured outcome)
- **Quote**: "combine deterministic GitHub Actions infrastructure with AI-driven
  decision-making"
- **Our assessment**: The key architectural distinction is that the substrate
  (GitHub Actions scheduling, permissions, event triggers) is deterministic and
  auditable, while the agent's reasoning over content is not. This hybrid is
  important for practitioners: it means you can reason about *when* and *with
  what permissions* an agent runs (deterministic), but not *exactly what* it
  will produce on a given input (AI-driven). For Ch01 (Daily Workflows) and
  Ch02 (Harness Engineering): this framing is useful for explaining to teams
  what guarantees agentic automation provides and what it does not. The
  deterministic wrapper is the trust layer; the AI layer is the value layer.

### Claim 3: GitHub Agentic Workflows implements a five-layer defense-in-depth security pipeline: compilation-time validation → runtime isolation → permission separation → network controls → output sanitization

- **Evidence**: The page explicitly names five security layers and describes
  the pipeline as following the path: Input → Compile → Runtime → Isolation →
  Output → Actions. The architectural description: "Workflows run with minimal
  permissions (no write access by default), use tool allowlists, and process
  outputs through a safety layer before applying changes."
- **Confidence**: emerging (first-party documentation; the specific threat model
  each layer addresses is named but not detailed on this page)
- **Quote**: "Multi-layered defense-in-depth architecture" with layers:
  "1. Compilation-time validation, 2. Runtime isolation, 3. Permission
  separation, 4. Network controls, 5. Output sanitization"
- **Our assessment**: This five-layer model is the most actionable security
  architecture in our corpus for agentic workflows. The pipeline order matters:
  validate at compile time (before the agent runs), isolate at runtime (sandbox
  the process), separate permissions (least-privilege for the agent), control
  network (limit egress), sanitize output (clean before applying changes to
  GitHub state). Each layer catches different attack vectors. Compilation-time
  validation catches structural violations before execution; output sanitization
  catches prompt injection artifacts before they reach GitHub state. For Ch03
  (Safety and Verification): this is a named, structured reference architecture.
  The Prospector's guidance identifies that each layer defends against specific
  threats (prompt injection, rogue MCP servers, malicious agents); the full
  threat mapping is in the companion architecture page (issue #253).

### Claim 4: Workflows run with minimal permissions — no write access by default — using tool allowlists to constrain the agent's action surface

- **Evidence**: Directly stated: "Workflows run with minimal permissions (no
  write access by default), use tool allowlists, and process outputs through a
  safety layer before applying changes." Tool allowlists are defined in the
  workflow frontmatter.
- **Confidence**: settled (first-party documentation; this is a design principle
  of the platform, not a practitioner observation)
- **Quote**: "Workflows run with minimal permissions (no write access by
  default), use tool allowlists, and process outputs through a safety layer
  before applying changes."
- **Our assessment**: The "no write access by default" principle is the
  least-privilege guarantee that makes the Safe Outputs model (Claim 5) coherent.
  If agents had write access by default, Safe Outputs would be defensive
  decoration; with no write access by default, Safe Outputs is the *only* path
  for the agent to cause GitHub state changes. This inverts the typical
  automation model (grant write access, then restrict) in favor of zero-capability
  by default (grant no access, then explicitly permit). For Ch03: this is the
  design principle worth naming and recommending — "zero capability by default,
  explicit permit" — because it limits blast radius from a compromised or
  misbehaving agent.

### Claim 5: Safe Outputs are pre-approved GitHub operations the AI can request without write permissions, providing permission-separated state mutation

- **Evidence**: The page defines Safe Outputs as "Pre-approved actions the AI
  can request without write permissions." They are "validated GitHub operations
  requiring no additional permissions." MCP Scripts are distinguished as "custom
  inline tools defined in workflow frontmatter" — a different mechanism.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Pre-approved actions the AI can request without write permissions"
- **Our assessment**: Safe Outputs is a named permission-separation pattern:
  the AI has no write capability directly, but can request that a pre-vetted,
  trusted handler perform a specific GitHub operation on its behalf. This is
  functionally similar to capability-based security — the agent can only exercise
  capabilities that were explicitly granted in the workflow spec. The "safe" in
  "Safe Outputs" refers to the vetting process at compile time: the compiler
  validates that the requested operations match the pre-approved list before the
  lock file is generated. From `blog-ghaw-weekly-2026-03-23.md` (Claim 1), we
  know the `safe-outputs.actions` block also extends this to GitHub Actions as
  MCP tools — any Action in the Marketplace can be promoted to a safe output.
  For Ch03: Safe Outputs is the canonical pattern for "how to give an AI agent
  permission to change state without giving it write access."

### Claim 6: MCP Scripts allow custom tool definitions inline in workflow frontmatter without deploying a separate MCP server

- **Evidence**: The page identifies MCP Scripts as "custom MCP tools defined
  inline in workflow frontmatter." This is distinct from connecting to an
  external MCP server — the tool is defined in the workflow file itself.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Custom MCP tools defined inline in workflow frontmatter"
- **Our assessment**: MCP Scripts lower the barrier to tool integration
  significantly. A practitioner who wants a custom tool doesn't need to deploy
  and maintain a separate MCP server process — they write the tool definition
  in the workflow file, and the compiler handles it. This is especially relevant
  for small, workflow-specific tools (e.g., a script that reads from a custom
  internal API). For Ch02 (Harness Engineering): MCP Scripts and safe-outputs.
  actions (from `blog-ghaw-weekly-2026-03-23.md`) together give two lightweight
  paths for adding custom capabilities — inline scripts for novel tools, GitHub
  Actions for reusing existing CI/CD tooling. A full external MCP server is
  the right choice only when the tool needs to be shared across many workflows
  or requires complex logic that doesn't fit inline.

### Claim 7: The compilation model separates the editable workflow source (`.md`) from the hardened executable (`.lock.yml`) produced by `gh aw compile`

- **Evidence**: The page describes the compilation model: "`gh aw compile`
  generates `.lock.yml` files from `.md` source files." The `.md` is "the
  editable source of truth," while `.lock.yml` is "the compiled GitHub Actions
  workflow with security hardening." Both should be committed.
- **Confidence**: settled (first-party documentation; the CLI command is
  documented)
- **Quote**: "The `.md` file is the editable source of truth, while `.lock.yml`
  is the compiled GitHub Actions workflow with security hardening."
- **Our assessment**: This is the same compilation claim documented in
  `blog-gh-aw-operations-release-workflows.md` (Claim 4) and
  `blog-ghaw-agent-observability.md` (Claim 6) from blog posts, but here it
  is stated from the canonical documentation, which makes it the authoritative
  reference. The key architectural distinction: the `.md` source is what humans
  write and reason about; the `.lock.yml` is what GitHub Actions executes.
  The compilation step is where security hardening happens (Claim 3 — compile-time
  validation is the first security layer). From `blog-ghaw-weekly-2026-03-23.md`
  (Claim 7), we know that as of v0.62.3, lock files also embed agent ID and
  model identity (gh-aw-metadata v3), extending the artifact beyond workflow
  logic to include model provenance. For Ch02: the `.md` → `.lock.yml`
  compilation pattern is the canonical harness reproducibility model.

### Claim 8: "Continuous AI" is defined as the systematic, automated application of AI to software collaboration — covering documentation currency, code quality, triage, and code review

- **Evidence**: The page names "Continuous AI" as the overarching pattern
  enabled by GitHub Agentic Workflows, defined as "systematic, automated
  application of AI to software collaboration." The four named patterns:
  documentation currency maintenance, incremental code quality improvement,
  intelligent issue and PR triage, automated code review.
- **Confidence**: anecdotal (this is a marketing/branding framing from GitHub;
  it names an emergent pattern but the label itself has no third-party adoption
  record)
- **Quote**: "systematic, automated application of AI to software collaboration"
- **Our assessment**: "Continuous AI" is a useful vocabulary entry for the
  guide, analogous to "Continuous Integration" or "Continuous Deployment" —
  it frames agentic automation as a systematic organizational practice rather
  than ad hoc tooling. The four use cases (documentation, code quality, triage,
  code review) are a reasonable taxonomy of "always-on" agentic tasks that
  operate continuously on repository events. For Ch01 (Daily Workflows): the
  "Continuous AI" framing provides vocabulary for recommending teams treat
  agentic automation as an organizational practice, not a one-off experiment.
  The four listed use cases are good starting points for teams building their
  first agent factory. However, the label is GitHub's coinage — do not present
  it as an industry-standard term.

### Claim 9: Multi-engine support (GitHub Copilot, Claude by Anthropic, Codex, Gemini) is first-class — all use the same workflow structure and MCP-based tool protocol

- **Evidence**: The page lists supported AI engines: "GitHub Copilot (default),
  Claude by Anthropic, Codex, and Gemini by Google." Each engine "interprets
  natural language instructions and executes them using configured tools and
  permissions." MCP is described as "a standardized protocol for connecting AI
  agents to external tools and services."
- **Confidence**: settled (first-party documentation; feature exists)
- **Quote**: "Each engine interprets natural language instructions and executes
  them using configured tools and permissions."
- **Our assessment**: The multi-engine claim matters for two reasons: (1) the
  same `.md` workflow spec can be run against different AI engines by changing
  the frontmatter — portability of intent across engines; (2) the common MCP
  tool protocol means tool definitions are not engine-specific. This is relevant
  to `docs-github-copilot-agent-model-selection.md`, which covers per-task
  model selection at the GitHub.com level. Taken together: model selection
  exists at two levels — choosing the engine class (Copilot vs. Claude vs.
  Codex in the workflow frontmatter) and choosing the model tier within an
  engine class (Sonnet vs. Opus, per issue #171). For Ch02: harness authors
  should treat engine selection as a frontmatter configuration, not a code
  change. This preserves portability.

### Claim 10: Critical actions can require human approval as a configurable escalation point within the security architecture

- **Evidence**: Directly stated: "Critical actions can require human approval."
  This is presented as part of the security architecture, implying it is
  configured in the workflow frontmatter's permissions or tools section.
- **Confidence**: emerging (stated in documentation; the configuration mechanism
  is not detailed on this page)
- **Quote**: "Critical actions can require human approval."
- **Our assessment**: Human approval as a configurable escalation is significant
  because it means the "autonomous" agent model is not all-or-nothing.
  High-stakes operations (e.g., merging a PR, deploying to production, deleting
  a branch) can be gated on human sign-off while low-stakes operations (e.g.,
  labeling an issue, posting a comment) run unattended. For Ch03 (Safety and
  Verification): recommend that teams identify which operations in their
  workflows qualify as "critical" and gate them on human approval. This maps to
  the "human-in-the-loop" verification pattern. It also corroborates
  `blog-gh-aw-operations-release-workflows.md` Claim 6 — the 22% rejection
  rate on Changeset Generator PRs means humans are still reviewing before merge;
  that human gate is exactly what this claim describes as a design option.

### Claim 11: The best practice workflow is compile → watch → run → review, with `gh aw logs` for cost monitoring

- **Evidence**: Best practices listed: "Start simple with clear, specific
  instructions. Test using `gh aw compile --watch` and `gh aw run`. Monitor
  costs with `gh aw logs`. Review AI-generated content before merging. Use safe
  outputs for controlled creation."
- **Confidence**: settled (first-party recommendations; `gh aw logs` for cost
  monitoring is consistent with `blog-ghaw-weekly-2026-03-23.md` Claim 8 on
  cost runaway detection)
- **Quote**: "Monitor costs with `gh aw logs`"
- **Our assessment**: The recommended sequence (compile → watch → run → review)
  is important because `gh aw compile --watch` catches structural errors before
  the agent ever runs — the first of the five security layers (compilation-time
  validation) is also the first development step. The cost monitoring guidance
  (`gh aw logs`) is consistent with the corpus evidence on token cost variance
  (`blog-ghaw-weekly-2026-03-23.md` Claim 6: 1.55M token runaway). For Ch02:
  include this four-step workflow as the recommended development loop for
  gh-aw practitioners.

## Concrete Artifacts

### Workflow Structure — Two-Component Layout

```markdown
---
# YAML frontmatter (constraints)
triggers:
  on: [pull_request]
permissions:
  pull-requests: read
tools:
  - name: github-api
    # MCP tool definitions or safe-outputs block
---

# Natural language markdown (intent)
## Task
When a pull request is opened, review the changed files for...
```
*Source: described in documentation as "YAML frontmatter" + "markdown instructions";
schema is illustrative — exact frontmatter fields defined in gh-aw documentation.*

### Security Pipeline (as documented)

```
Pipeline order (Input → Compile → Runtime → Isolation → Output → Actions):

Layer 1: Compilation-time validation
  → Validates workflow spec structure and tool allowlists before execution
  → Catches structural violations before the agent runs

Layer 2: Runtime isolation
  → Sandboxes agent execution environment
  → Prevents agent from accessing host resources outside defined scope

Layer 3: Permission separation
  → No write access by default
  → Tool allowlists constrain what the agent can invoke
  → Agent can only call explicitly permitted tools

Layer 4: Network controls
  → Limits egress from agent runtime
  → Prevents exfiltration via unexpected network calls

Layer 5: Output sanitization
  → Processes agent outputs through a safety layer before applying to GitHub state
  → Catches prompt injection artifacts before they reach GitHub API calls

Base principle: "Workflows run with minimal permissions (no write access by
default), use tool allowlists, and process outputs through a safety layer
before applying changes."
```

### Safe Outputs vs. MCP Scripts — Distinction

```
Safe Outputs:
  Definition: "Pre-approved actions the AI can request without write permissions"
  Mechanism:  AI requests a named operation; a pre-vetted handler performs it
  Example:    Creating a PR comment, applying a label, opening an issue
  Key:        No direct write permission; capability-based — only listed operations
              are permitted; validated at compile time

MCP Scripts:
  Definition: "Custom MCP tools defined inline in workflow frontmatter"
  Mechanism:  Inline tool definition in YAML frontmatter; compiler processes it
  Use case:   Workflow-specific custom tools without deploying an MCP server
  Key:        Provides read/query capability; not a state-mutation mechanism
              (Safe Outputs handles mutations)

Combined pattern (from blog-ghaw-weekly-2026-03-23.md v0.62.3):
  safe-outputs.actions: any GitHub Action exposed as an MCP tool via compiler-
  assisted schema derivation from action.yml
```

### Compilation Model

```
Source file:   workflow-name.md   (editable source of truth — written by humans)
  ↓
  gh aw compile
  (also: gh aw compile --watch  for development iteration)
  ↓
Compiled file: workflow-name.lock.yml  (hardened GitHub Actions executable)
  Security hardening applied at compile time
  As of gh-aw-metadata v3 (v0.62.3): also embeds agent ID + model identity

Both .md and .lock.yml are committed to the repository.
```

### Continuous AI — Named Pattern and Use Cases

```
Definition:  "systematic, automated application of AI to software collaboration"
coined by:   GitHub Agentic Workflows team (gh-aw documentation)

Four canonical starting patterns:
  1. Documentation currency maintenance     — keep docs in sync with code changes
  2. Incremental code quality improvement   — continuous lint, style, coverage nudges
  3. Intelligent issue and PR triage        — label, route, summarize incoming work
  4. Automated code review                  — check PRs against standards/CONTRIBUTING

Relation to CI/CD framing:
  CI (Continuous Integration)   = automated build + test on every commit
  CD (Continuous Deployment)    = automated deploy on merge
  Continuous AI                 = systematic AI-driven collaboration on every event
```

### Development Workflow (Best Practices)

```bash
# 1. Write or edit the workflow spec
$EDITOR .github/workflows/my-agent.md

# 2. Compile and watch for structural errors (compile-time validation)
gh aw compile --watch

# 3. Run the workflow against a test case
gh aw run

# 4. Monitor costs and audit logs
gh aw logs

# 5. Review AI-generated output before merging
# (human approval gate — especially for critical actions)
```

## Cross-References

- **Corroborates**:
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` /
    lock file separation): that source documents the CLI artifact from a blog
    post practitioner perspective; this source is the canonical documentation
    for the same mechanism. Together they establish that the `.md` → `.lock.yml`
    compilation model is both the official design and the production practice.
  - `blog-ghaw-agent-observability.md` Claim 6 (`gh aw compile` declarative
    model): same corroboration — this page is the primary source for what Claim 6
    in that note documents via blog post.
  - `blog-ghaw-weekly-2026-03-23.md` Claim 4 (GitHub MCP guard policy GA, no
    write access by default): this page's "no write access by default" (Claim 4)
    is the base design that the guard policy GA generalizes. The guard policy is
    the runtime enforcement; this page describes the design principle.

- **Extends**:
  - `blog-ghaw-weekly-2026-03-23.md` Claim 7 (lock files embed agent ID/model,
    gh-aw-metadata v3): this page describes the base compilation model; that
    weekly note describes the v3 extension that adds model identity to lock
    files. The two together give the complete picture of what a compiled lock
    file contains as of v0.62.3.
  - `blog-ghaw-weekly-2026-03-23.md` Claim 1 (`safe-outputs.actions` for
    exposing GitHub Actions as MCP tools): this page introduces Safe Outputs
    as the base pattern (Claim 5); that weekly note extends it with the
    `safe-outputs.actions` block for GitHub Action promotion. Read together,
    Safe Outputs is both the permission-separation mechanism (this page) and
    an extensibility mechanism for CI/CD tooling (weekly update).
  - `docs-github-copilot-agent-model-selection.md`: that source covers model
    selection at the GitHub.com task-dispatch level; this source covers
    engine/model configuration at the workflow-spec level. Together they give
    a two-layer model-selection picture: frontmatter sets the engine class,
    GitHub.com UI allows tier selection within a class.

- **Contradicts**: None. No existing source note makes claims that contradict
  the five-layer security model, Safe Outputs design, or compilation model
  described here. The prior blog posts (`blog-gh-aw-operations-release-workflows.md`,
  `blog-ghaw-agent-observability.md`) cite the `gh aw compile` pattern
  consistently with this documentation.

- **Novel**:
  - **Five-layer security model as named architecture** (Claim 3): No other
    source in the corpus names and sequences the five security layers
    (compile → runtime → isolation → network → output). The weekly notes
    cover specific layers (integrity guard, output sanitization) but not the
    full model as a unified architecture.
  - **Safe Outputs as a permission-separation pattern** (Claim 5): The weekly
    update (`blog-ghaw-weekly-2026-03-23.md`) introduced `safe-outputs.actions`,
    but the base Safe Outputs concept — AI requests pre-approved operations
    without write permissions — is documented here for the first time as a
    first-principles pattern, not just a changelog entry.
  - **"Continuous AI" as a named practice** (Claim 8): No other source in the
    corpus uses this term or defines systematic AI-driven collaboration as a
    named practice analogous to CI/CD. The four use cases are a useful
    practitioner taxonomy.
  - **MCP Scripts (inline custom tools)** (Claim 6): The inline tool-definition
    capability — MCP-compatible tools defined directly in workflow frontmatter —
    is not described in any existing source note.
  - **Workflow structure as a harness design pattern** (Claim 1): While the
    `gh aw compile` CLI is documented in multiple blog posts, the deliberate
    architectural principle of YAML-constrains / markdown-instructs as a
    separation-of-concerns in harness design is stated explicitly only in this
    documentation page.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add "Continuous AI" as a framing concept**: The guide should offer vocabulary
  for treating agentic automation as an organizational practice rather than ad hoc
  tooling. "Continuous AI" (defined here as "systematic, automated application of
  AI to software collaboration") provides this. The four starting patterns
  (documentation currency, code quality, triage, code review) are good first
  targets for teams building their first always-on agent. Note that the term is
  GitHub's coinage — present it as a useful framing, not an industry standard.

- **Agentic vs. traditional workflow contrast** (Claim 2): The "deterministic
  infrastructure + AI-driven decisions" framing gives practitioners a mental
  model for what agentic automation guarantees (when/permissions/triggers) vs.
  what it does not (exact output on a given input). This sets correct expectations
  and is a pre-condition for the safety discussion in Ch03.

### Chapter 02: Harness Engineering

- **Declarative harness design principle** (Claim 1): Add "YAML constrains,
  markdown instructs" as a named harness design pattern. The frontmatter defines
  the sandbox (triggers, permissions, tools); the markdown carries the intent.
  This separation is what makes harnesses composable and auditable.

- **`.md` → `.lock.yml` compilation model** (Claim 7): This page is the
  canonical reference for the compilation pattern that `blog-gh-aw-operations-
  release-workflows.md` and `blog-ghaw-agent-observability.md` reference from
  practitioner experience. Cite this documentation as the primary source.
  Pair with `blog-ghaw-weekly-2026-03-23.md` Claim 7 to cover lock file model
  identity (gh-aw-metadata v3).

- **MCP Scripts for inline tool integration** (Claim 6): Add as a lightweight
  path for workflow-specific tools. The three-path tool integration model:
  (a) Safe Outputs for pre-approved GitHub state mutations; (b) MCP Scripts
  for custom inline read/query tools; (c) external MCP servers for shared,
  complex tools. Ch02 should help practitioners pick the right path.

- **Development workflow** (Claim 11): Add the compile → watch → run → review
  loop as the recommended workflow for gh-aw practitioners. Specifically,
  `gh aw compile --watch` as a real-time structural validation tool and
  `gh aw logs` for cost monitoring.

### Chapter 03: Safety and Verification

- **Five-layer security architecture** (Claim 3): This is the most complete
  security architecture in the corpus for agentic systems. Add it as the
  reference model for Ch03's defense-in-depth section. The pipeline order
  (compile → runtime → isolation → network → output) maps to specific attack
  vectors (structural manipulation, process escape, privilege escalation, data
  exfiltration, prompt injection). The companion architecture page (issue #253)
  likely provides the threat model; once that note is filed, cross-reference both.

- **"Zero capability by default" principle** (Claim 4): The "no write access
  by default" plus tool allowlists design is the concrete implementation of
  least-privilege for agentic systems. Recommend this as the design principle
  for any harness security layer — not just for gh-aw. The principle is:
  start with zero agent capability, explicitly permit what is needed.

- **Safe Outputs as a named pattern** (Claim 5): Add Safe Outputs to Ch03 as
  the permission-separation pattern for AI state mutation. The design: agent
  has no write access; agent can request pre-approved operations through a
  capability-based handler. This is the pattern that prevents a compromised
  or misbehaving agent from causing unbounded GitHub state changes.

- **Human approval gate** (Claim 10): Add as a recommended practice for
  "critical actions" in any agentic workflow. Teams should identify which
  operations qualify as critical (merges, deploys, deletions) and configure
  human approval gates for those. This corroborates Ch03's human-in-the-loop
  theme (evidenced by the 22% rejection rate in `blog-gh-aw-operations-release-
  workflows.md` Claim 6).

## Extraction Notes

1. **Source is the conceptual overview, not the full architecture**: Per
   Prospector guidance, issue #253 covers the companion architecture page,
   which likely contains the detailed threat model for each security layer and
   more granular runtime execution details. This note covers the conceptual
   "what and why"; the architecture note should cover "how." Cross-reference
   once #253 is mined.

2. **Rendering note**: The page is an Astro/Starlight-rendered SPA. WebFetch
   returns the rendered text without JavaScript execution, which may omit
   embedded diagrams or interactive content. The security pipeline visualization
   ("Input → Compile → Runtime → Isolation → Output → Actions") was captured
   from the rendered text; interactive architecture diagrams, if any, may not
   have been extracted.

3. **No direct publication date**: The documentation page does not carry an
   explicit publication date. `date_published` is left null. Content is
   consistent with gh-aw v0.45.5–v0.62.x based on compilation model description.

4. **Skipped per Prospector guidance**: Engine API reference pages, changelog
   entries, and release notes are out of scope for this note. The focus was on
   conceptual architecture (security model, compilation model, Safe Outputs) and
   vocabulary (Continuous AI, agentic vs. traditional workflows).

5. **No contradictions filed**: Reviewed all existing source notes. No claims
   in this source materially oppose existing source notes. The five-layer
   security model and Safe Outputs are new to the corpus; they do not contradict
   existing notes. The `lockdown: true` → `min-integrity` evolution documented
   in `blog-ghaw-weekly-2026-03-23.md` is a platform-level change, not a
   contradiction of this page's security architecture description (both
   describe the same system at different points in its evolution; the base
   principle — defense-in-depth with minimal permissions — is consistent).
