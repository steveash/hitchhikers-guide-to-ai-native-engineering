---
source_url: https://github.github.com/gh-aw/reference/safe-outputs-specification
source_type: docs
title: "GitHub Agentic Workflows: Safe Outputs MCP Gateway Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#432"
---

# GitHub Agentic Workflows: Safe Outputs MCP Gateway Specification

> The formal normative specification (Working Draft v1.19.0) for the Safe Outputs MCP Gateway —
> provides the authoritative technical architecture (three-component system, six security
> invariants, seven-stage validation pipeline, two conformance classes) that underlies the
> conceptual Safe Outputs pattern described in `docs-ghaw-how-they-work.md`; first corpus source
> to give practitioners the formal implementation requirements rather than the conceptual overview.

## Source Context

- **Type**: docs (formal normative specification — Working Draft v1.19.0, documenting
  gh-aw v1.8.0+. This is a W3C-style spec document using RFC 2119 requirement terminology
  (MUST, SHALL, SHOULD, MAY, REQUIRED), not a tutorial or conceptual overview. It is the
  authoritative implementation reference for the Safe Outputs mechanism.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same team
  behind Peli de Halleux's agent factory blog series and the `gh aw` platform. Claims about
  normative requirements, security invariants, validation pipeline, and conformance classes
  are authoritative for the Safe Outputs mechanism on this platform. The specification employs
  formal requirement language; this is the highest-confidence source type in the gh-aw corpus
  for implementation-level claims.
- **Scope**: The full normative architecture of the Safe Outputs MCP Gateway: system
  components (Workflow Compiler, MCP Gateway Server, Safe Output Processor), four foundational
  security principles, six security property invariants, seven-stage validation pipeline, NDJSON
  communication channel, configuration model (global + type-specific), operational features
  (staged mode, max limits, footers, content sanitization, domain filtering, cross-repository
  controls), and two conformance classes. Does NOT cover: individual safe output type schemas
  in depth (e.g., the full `create-issue` or `add-comment` parameter lists), the general gh-aw
  workflow compilation process (`docs-ghaw-compilation-process.md`), read-only MCP server
  configuration (`docs-ghaw-mcps.md`), or the conceptual "why" of Safe Outputs
  (`docs-ghaw-how-they-work.md` — that remains the conceptual entry point).

## Extracted Claims

### Claim 1: The Safe Outputs MCP Gateway is formally defined as "a security-centric translation layer enabling AI agents to declare intended GitHub operations through structured protocols while maintaining strict privilege separation"

- **Evidence**: The opening abstract of the specification provides this definition. The spec
  document is Working Draft v1.19.0, documenting gh-aw v1.8.0+, and uses RFC 2119 requirement
  terminology throughout.
- **Confidence**: settled (first-party formal specification; this is the normative definition
  for the entire mechanism)
- **Quote**: "This specification establishes normative requirements for the Safe Outputs Model
  Context Protocol (MCP) Gateway, a security-centric translation layer enabling AI agents to
  declare intended GitHub operations through structured protocols while maintaining strict
  privilege separation."
- **Our assessment**: The formal definition clarifies the architectural role of Safe Outputs
  more precisely than `docs-ghaw-how-they-work.md` Claim 5 ("Pre-approved actions the AI can
  request without write permissions"). The key additional precision: agents *declare intentions*
  (not execute operations), the declaration goes through *structured protocols* (NDJSON via
  the MCP Gateway), and the overall guarantee is *strict privilege separation*. For Ch03
  (Safety and Verification): this definition is the authoritative language for describing
  what Safe Outputs are in the guide. Prefer this wording over informal descriptions.

### Claim 2: The system comprises three distinct components in three operational phases: Workflow Compiler (pre-execution), MCP Gateway Server (agent runtime), and Safe Output Processor (post-execution)

- **Evidence**: The specification's component architecture section names three components:
  "Component C1: Workflow Compiler (Pre-execution phase)," "Component C2: MCP Gateway Server
  (Runtime agent phase)," and "Component C3: Safe Output Processor (Post-execution phase)."
  The Workflow Compiler parses configuration and generates JSON schemas; the MCP Gateway
  Server validates requests and records operations to NDJSON format; the Safe Output Processor
  validates and executes operations via the GitHub API.
- **Confidence**: settled (first-party formal specification; the three-component architecture
  is the core structural definition of the system)
- **Quote**: "The Safe Outputs MCP Gateway system comprises three distinct components operating
  in different phases: Component C1: Workflow Compiler (Pre-execution phase)... Component C2:
  MCP Gateway Server (Runtime agent phase)... Component C3: Safe Output Processor
  (Post-execution phase)"
- **Our assessment**: This three-phase model explains *when* security enforcement happens, which
  is architecturally important. The Workflow Compiler enforces at compile time (before the agent
  runs), the MCP Gateway enforces at agent runtime (as the agent attempts operations), and the
  Safe Output Processor enforces at post-execution (before GitHub API calls). Each phase catches
  a different class of violation. This is the implementation-level explanation for Layer 1
  (compilation-time validation) and Layer 5 (output sanitization) in `docs-ghaw-how-they-work.md`
  Claim 3's five-layer security model. For Ch02 (Harness Engineering): practitioners can now
  explain *which component* enforces each constraint — not just that constraints exist.

### Claim 3: Agents MUST execute without write permissions; agent-to-processor communication MUST use GitHub Actions artifact storage (NDJSON), not direct GitHub API calls

- **Evidence**: Two normative architectural requirements:
  - "Requirement AR1: Agent Isolation — Agents MUST execute without GitHub write permissions.
    Only read-level tokens SHALL be accessible to agent processes."
  - "Requirement AR2: Communication Channel Integrity — Agent-to-processor communication MUST
    occur through GitHub Actions artifact storage."
  The NDJSON format ("Newline-Delimited JSON: A text format where each line contains one
  complete, valid JSON object") is the artifact-storage communication format.
- **Confidence**: settled (normative MUST/SHALL requirements in the formal specification)
- **Quote**: "Agents MUST execute without GitHub write permissions. Only read-level tokens
  SHALL be accessible to agent processes."
- **Our assessment**: AR1 is the normative implementation of the "no write access by default"
  principle from `docs-ghaw-how-they-work.md` Claim 4. AR2 is architecturally significant and
  new to the corpus: the agent communicates its intended operations by writing to NDJSON in
  GitHub Actions artifact storage — not by calling the GitHub API directly. The Safe Output
  Processor then reads those artifacts and executes the operations. This NDJSON-based
  communication channel is the implementation mechanism that makes privilege separation possible:
  even if an agent were compromised, it cannot bypass the NDJSON pipeline to call the GitHub
  API directly, because it has no write tokens. For Ch03: AR1 + AR2 together are the
  concrete privilege-separation design — document them as the implementation mechanism, not
  just the design principle.

### Claim 4: Four foundational security principles govern the architecture: P1 (Architectural Separation), P2 (Declarative Over Imperative), P3 (Configurable Constraint Enforcement), P4 (Fail-Secure By Default)

- **Evidence**: Section 1.3 of the specification names four normative principles:
  - "P1: Security Through Architectural Separation — Write permissions MUST reside in separate
    execution contexts from AI reasoning."
  - "P2: Declarative Over Imperative — Operations are declared through schema-validated data
    structures, not imperative command execution."
  - "P3: Configurable Constraint Enforcement — Workflow authors explicitly configure permitted
    operations and constraints."
  - "P4: Fail-Secure By Default — Invalid inputs, constraint violations, or execution errors
    result in operation rejection, not degraded execution."
- **Confidence**: settled (normative principles stated in the formal specification)
- **Quote**: "Principle P4: Fail-Secure By Default — Invalid inputs, constraint violations, or
  execution errors result in operation rejection, not degraded execution."
- **Our assessment**: These four principles are the design rationale behind the entire
  architecture. P1 is the "why" behind separate execution contexts (Claim 3). P2 explains
  why NDJSON is used rather than function calls — operations are data structures, not
  executable code, enabling static analysis before execution. P3 explains the configuration
  model (workflow authors choose which operations are permitted, with what constraints). P4 is
  the "when in doubt, reject" safety posture. For Ch03: P4 (fail-secure) is the principle
  practitioners should name when justifying why max limits reject ALL operations on overflow
  rather than just the excess (Claim 6). P2 (declarative over imperative) is the reason
  Safe Outputs can be audited before execution — the operation is a JSON object, not a
  function call.

### Claim 5: Six security invariants are normatively required: SP1 Permission Separation, SP2 Validation Precedence, SP3 Limit Enforceability, SP4 Content Integrity, SP5 Provenance Traceability, SP6 Cross-Repository Containment

- **Evidence**: The specification defines six security properties as invariants:
  - SP1: "At all times during agent execution, the agent process SHALL NOT possess tokens or
    credentials permitting GitHub write operations."
  - SP2: "For all safe output operations, validation logic MUST execute before any GitHub API
    invocation. Invalid operations MUST be rejected without side effects."
  - SP3: "For all configured max limits, implementations MUST prevent exceeding the limit.
    Attempts to exceed limits SHALL result in operation rejection."
  - SP4: "All user-provided content MUST undergo sanitization. Sanitization MUST occur after
    agent output and before GitHub API invocation."
  - SP5: "All created GitHub resources MUST include provenance metadata identifying workflow
    source and run."
  - SP6: "For all cross-repository operations: target must be in type-specific allowlist OR
    global allowlist when defined."
- **Confidence**: settled (normative invariants using SHALL NOT / MUST language in the formal
  specification)
- **Quote**: "At all times during agent execution, the agent process SHALL NOT possess tokens
  or credentials permitting GitHub write operations."
- **Our assessment**: These six invariants are the security contract the Safe Outputs mechanism
  provides to practitioners. They are more specific than the five-layer model in
  `docs-ghaw-how-they-work.md` Claim 3: SP1 = Layer 3 (permission separation); SP2 = Layer 5
  (validation before API); SP4 = Layer 5 (output sanitization); SP6 = network containment
  at the output level. SP3 (limit enforceability, all-or-nothing) and SP5 (provenance
  traceability) are new guarantees not named in the conceptual model. For Ch03: these six
  invariants are the guarantee set — practitioners can evaluate whether a candidate
  implementation provides all six. An implementation missing SP5 (no provenance metadata)
  breaks the audit trail; an implementation missing SP4 (no content sanitization) is
  vulnerable to prompt injection reaching GitHub state.

### Claim 6: Max limit violation triggers all-or-nothing rejection — exceeding the configured `max` for an operation type rejects ALL operations of that type, not just the excess

- **Evidence**: The specification's normative requirement for limit enforcement: "When operation
  count for a type exceeds configured max, implementations MUST reject ALL operations of that
  type, not just excess operations." This is a MUST-level normative requirement, not a
  recommendation.
- **Confidence**: settled (normative MUST requirement in the formal specification)
- **Quote**: "When operation count for a type exceeds configured max, implementations MUST
  reject ALL operations of that type, not just excess operations."
- **Our assessment**: The all-or-nothing semantics of max limits are architecturally significant
  and not documented in any existing source note. The design choice follows from Principle P4
  (fail-secure): if the agent exceeds its operation budget, the safe behavior is to reject
  everything rather than allow partial execution that might leave state in an inconsistent
  condition. For practitioners: this means `max: 5` on `add-comment` means the workflow
  produces zero comments if the agent attempts 6 — not 5. This should inform how practitioners
  set max values. Setting max too low risks complete operation failure; setting it too high
  risks runaway writes. For Ch02: document the all-or-nothing semantics explicitly — this is a
  non-obvious design choice that practitioners must account for when tuning max values in
  DataOps and IssueOps workflows.

### Claim 7: Content sanitization (SP4) is a normative MUST that removes malicious URLs, command injection, and credential patterns from all user-provided content before GitHub API invocation

- **Evidence**: The specification requires sanitization via SP4 (Claim 5 above). The content
  sanitization section describes removing "potentially malicious patterns" including "malicious
  URLs, command injection, credential patterns" while "preserving legitimate content." The
  normative requirement is that sanitization MUST occur after agent output and before GitHub
  API invocation.
- **Confidence**: settled (normative requirement; the threat categories are named explicitly)
- **Quote**: (no single-sentence verbatim quote capturing the full threat list available;
  threat categories are listed as "malicious URLs, command injection, credential patterns")
- **Our assessment**: Content sanitization is the technical implementation of output sanitization
  (Layer 5 in `docs-ghaw-how-they-work.md` Claim 3). Its placement — after agent output, before
  GitHub API invocation — means it runs on the Safe Output Processor side (Component C3), not
  on the MCP Gateway Server side (Component C2). This is the mechanism that prevents prompt
  injection artifacts from reaching GitHub state: even if an attacker causes the agent to output
  a malicious URL or injection payload, sanitization intercepts it before the GitHub API call.
  For Ch03: name content sanitization as the prompt-injection defense layer within Safe Outputs.
  The three named threat vectors (malicious URLs, command injection, credential patterns) define
  what it defends against.

### Claim 8: All created GitHub resources MUST include provenance metadata (SP5) — workflow source, run URL, and optional triggering context

- **Evidence**: SP5: "All created GitHub resources MUST include provenance metadata identifying
  workflow source and run." The footer specification elaborates: footers include workflow name
  (as a clickable link), run URL, optional triggering context (issue/PR/discussion reference),
  and optional installation command with source path.
- **Confidence**: settled (normative MUST in the formal specification; footer contents described
  in the spec)
- **Quote**: "All created GitHub resources MUST include provenance metadata identifying workflow
  source and run."
- **Our assessment**: SP5 (provenance traceability) is the auditing guarantee. Any comment,
  issue, PR, or discussion created by Safe Outputs carries a footer identifying exactly which
  workflow created it and which run. This is important for two reasons: (1) operators can audit
  agent activity by examining footers; (2) the `close-older-discussions: true` mechanism in
  DataOps workflows (see `docs-ghaw-dataops.md` Claim 7) depends on provenance — the processor
  can identify "its own" prior discussions because they carry the workflow's footprint. For Ch03:
  SP5 is the spec-level guarantee behind the audit trail. Practitioners should design workflows
  expecting all Safe Output-created resources to carry footers — and should not strip or suppress
  them, as this breaks SP5 compliance.

### Claim 9: Staged Mode is a normatively defined preview execution mode where operations are simulated without permanent effects, indicated by emoji prefix in messages

- **Evidence**: "Staged Mode: A preview execution mode where operations are simulated and
  previewed without permanent effects. Indicated by emoji prefix in messages." The spec
  documents staged mode as a formal operational feature, not just a developer convenience.
- **Confidence**: settled (formally defined in the spec)
- **Quote**: "A preview execution mode where operations are simulated and previewed without
  permanent effects. Indicated by emoji prefix in messages."
- **Our assessment**: Staged mode is the Safe Outputs equivalent of a dry-run flag, but with
  a formal specification. The emoji-prefix convention makes staged outputs visually
  distinguishable from production outputs in GitHub UI — practitioners can enable staged mode
  on a production repository and have agents run without creating permanent state, using the
  emoji markers to distinguish preview from real output. The `staged-mode-reference`
  documentation (`docs-ghaw-staged-mode-reference.md`) likely provides the full operational
  details; this spec provides the formal definition. For Ch02: present staged mode as a
  first-class testing primitive for any Safe Outputs workflow — run in staged mode first to
  validate agent behavior before enabling production writes.

### Claim 10: Safe Outputs configuration uses a two-level hierarchy — global parameters affecting all output types, and type-specific blocks that can override global settings

- **Evidence**: "Safe output configuration employs a two-level hierarchy: global parameters
  affecting all types, and type-specific blocks customizing individual operation categories."
  Global parameters include: `footer`, `staged`, `allowed-domains`, `allowed-github-references`.
  Type-specific blocks allow per-operation customization with inheritance-override capability.
  Templatable fields: `max` and `footer` support GitHub Actions expressions.
- **Confidence**: settled (first-party specification; the configuration model is explicitly
  defined)
- **Quote**: "Safe output configuration employs a two-level hierarchy: global parameters
  affecting all types, and type-specific blocks customizing individual operation categories."
- **Our assessment**: The two-level configuration model explains how global security controls
  (domain allowlists, cross-repo restrictions) interact with per-type operational settings
  (max limits, footers). The global `allowed-domains` ("Specifies allowlist of domains
  permitted in URLs within safe output content") and `allowed-github-references` ("Specifies
  allowlist of GitHub repositories for cross-repository safe output operations") apply across
  all output types — they cannot be overridden at the type level. This hierarchy means
  security decisions (what domains are allowed, what repos are targets) are set globally and
  cannot be accidentally relaxed by a type-specific block. For Ch02: document the two-level
  hierarchy as the configuration model for Safe Outputs — help practitioners understand which
  settings belong at global vs. type-specific level.

### Claim 11: Two conformance classes exist — C1 (full conformance, all normative requirements) and C2 (partial conformance, security-critical requirements only, may omit some output types)

- **Evidence**:
  - "Class C1: Full Conformance — An implementation satisfying ALL normative requirements
    (MUST, SHALL, REQUIRED statements) in this document."
  - "Class C2: Partial Conformance — An implementation satisfying ALL security-critical
    normative requirements but omitting support for optional safe output types."
- **Confidence**: settled (formally defined in the specification)
- **Quote**: "Class C2: Partial Conformance — An implementation satisfying ALL security-critical
  normative requirements but omitting support for optional safe output types."
- **Our assessment**: The C1/C2 split clarifies that safe output type support is separable from
  security invariant compliance. A C2 implementation can skip some output types (e.g., not
  implementing `create-project-status-update`) while still maintaining all six security
  invariants (SP1-SP6). The security invariants are NOT optional in either class. For
  practitioners building Custom Safe Outputs or gh-aw forks: C2 is the minimum acceptable
  security posture — you can limit which output types you support, but you cannot relax any of
  the six security properties (SP1-SP6). For Ch03: document C1 vs C2 as the conformance
  guidance for anyone building Safe Outputs infrastructure.

### Claim 12: The seven-stage validation pipeline enforces ordering — schema validation and limit enforcement are REQUIRED; domain filtering, cross-repository validation, and dependency resolution are CONDITIONAL; API invocation is last

- **Evidence**: Section 3.3 of the specification names seven sequential stages:
  "Stage 1: Schema Validation (REQUIRED)... Stage 2: Limit Enforcement (REQUIRED)... Stage 3:
  Content Sanitization (REQUIRED)... Stage 4: Domain Filtering (CONDITIONAL)... Stage 5:
  Cross-Repository Validation (CONDITIONAL)... Stage 6: Dependency Resolution (CONDITIONAL)...
  Stage 7: GitHub API Invocation (EXECUTION)"
- **Confidence**: settled (normative sequence in the formal specification)
- **Quote**: "Stage 1: Schema Validation (REQUIRED)... Stage 2: Limit Enforcement (REQUIRED)...
  Stage 3: Content Sanitization (REQUIRED)... Stage 4: Domain Filtering (CONDITIONAL)...
  Stage 5: Cross-Repository Validation (CONDITIONAL)... Stage 6: Dependency Resolution
  (CONDITIONAL)... Stage 7: GitHub API Invocation (EXECUTION)"
- **Our assessment**: The pipeline ordering is normative — stages must execute in this sequence.
  Stages 1-3 (schema, limits, sanitization) are REQUIRED for every operation. Stages 4-6 are
  CONDITIONAL on configuration (domain filtering only applies when `allowed-domains` is set;
  cross-repository validation only applies when `allowed-github-references` is set). Stage 7
  (API invocation) is always last and only reached if all prior stages pass. This ordering
  implements SP2 (Validation Precedence Invariant) in concrete terms. For Ch03: the seven-stage
  pipeline is the implementation of output sanitization as a whole — it is more granular than
  the "output sanitization" label in the five-layer model. Practitioners can reason about which
  threats are caught at which stage: injection → Stage 3; domain exfiltration → Stage 4;
  unauthorized cross-repo writes → Stage 5.

## Concrete Artifacts

### Four Foundational Security Principles (verbatim from spec Section 1.3)

```
Principle P1: Security Through Architectural Separation
  "Write permissions MUST reside in separate execution contexts from AI reasoning."

Principle P2: Declarative Over Imperative
  "Operations are declared through schema-validated data structures, not imperative
  command execution."

Principle P3: Configurable Constraint Enforcement
  "Workflow authors explicitly configure permitted operations and constraints."

Principle P4: Fail-Secure By Default
  "Invalid inputs, constraint violations, or execution errors result in operation
  rejection, not degraded execution."
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0, Section 1.3 — Security Principles*

### Six Security Property Invariants (verbatim from spec)

```
SP1: Permission Separation Invariant
  "At all times during agent execution, the agent process SHALL NOT possess tokens or
  credentials permitting GitHub write operations."

SP2: Validation Precedence Invariant
  "For all safe output operations, validation logic MUST execute before any GitHub API
  invocation. Invalid operations MUST be rejected without side effects."

SP3: Limit Enforceability Invariant
  "For all configured max limits, implementations MUST prevent exceeding the limit.
  Attempts to exceed limits SHALL result in operation rejection."

SP4: Content Integrity Invariant
  "All user-provided content MUST undergo sanitization. Sanitization MUST occur after
  agent output and before GitHub API invocation."

SP5: Provenance Traceability Invariant
  "All created GitHub resources MUST include provenance metadata identifying workflow
  source and run."

SP6: Cross-Repository Containment
  "For all cross-repository operations: target must be in type-specific allowlist OR
  global allowlist when defined."
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0 — Security Properties section*

### Architectural Requirements (verbatim from spec)

```
AR1: Agent Isolation
  "Agents MUST execute without GitHub write permissions. Only read-level tokens SHALL
  be accessible to agent processes."

AR2: Communication Channel Integrity
  "Agent-to-processor communication MUST occur through GitHub Actions artifact storage."
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0 — Architectural Requirements section*

### Three-Component Architecture

```
Component C1: Workflow Compiler (Pre-execution phase)
  → Parses configuration, validates structure, generates JSON schemas
  → Enforces compile-time constraints (Layer 1 of the five-layer security model)

Component C2: MCP Gateway Server (Runtime agent phase)
  → Validates agent operation requests
  → Records operation declarations to NDJSON format (artifact storage per AR2)
  → Does NOT possess write credentials (enforces AR1/SP1)

Component C3: Safe Output Processor (Post-execution phase)
  → Reads NDJSON operation declarations from artifact storage
  → Runs seven-stage validation pipeline
  → Executes validated operations via GitHub API with write credentials
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0 — Component Architecture section*

### Seven-Stage Validation Pipeline

```
Stage 1: Schema Validation          (REQUIRED)
  → Validates operation structure against generated JSON schemas
Stage 2: Limit Enforcement          (REQUIRED)
  → Enforces max counts — all-or-nothing rejection on overflow
Stage 3: Content Sanitization       (REQUIRED)
  → Removes malicious URLs, command injection, credential patterns
Stage 4: Domain Filtering           (CONDITIONAL — requires allowed-domains config)
  → Validates URLs against domain allowlist
Stage 5: Cross-Repository Validation (CONDITIONAL — requires allowed-github-references)
  → Validates target repositories against allowlist
Stage 6: Dependency Resolution      (CONDITIONAL)
  → Resolves operation dependencies
Stage 7: GitHub API Invocation      (EXECUTION — only if stages 1-6 pass)
  → Executes validated operations via GitHub API with write credentials

Normative ordering: stages MUST execute in sequence; stage 7 MUST be last.
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0, Section 3.3 — Validation Pipeline*

### Configuration Model Structure

```
Two-level hierarchy:

Global parameters (apply to all output types):
  footer:                    — attribution metadata appended to all created resources
  staged:                    — enable preview mode across all operations
  allowed-domains:           — "Specifies allowlist of domains permitted in URLs within
                               safe output content"
  allowed-github-references: — "Specifies allowlist of GitHub repositories for
                               cross-repository safe output operations"

Type-specific blocks (per operation type, e.g., create-issue, add-comment):
  max:     — operation count limit (MUST override per-type; supports GH Actions expressions)
  footer:  — type-specific footer override (supports GH Actions expressions)
  (+ type-specific parameters such as project URL for update-project)

Inheritance: type-specific blocks inherit global settings; type-level max/footer
can override global values.
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0 — Configuration Model section*

### Conformance Classes

```
Class C1: Full Conformance
  "An implementation satisfying ALL normative requirements (MUST, SHALL, REQUIRED
  statements) in this document."

Class C2: Partial Conformance
  "An implementation satisfying ALL security-critical normative requirements but
  omitting support for optional safe output types."

Key distinction:
  Both C1 and C2 require full compliance with all six security invariants (SP1-SP6)
  and architectural requirements (AR1, AR2).
  C2 may omit implementation of specific safe output types (e.g., create-project-
  status-update) but CANNOT relax security properties.
```

*Source: Safe Outputs MCP Gateway Specification v1.19.0 — Conformance section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default): The spec's AR1
    ("Agents MUST execute without GitHub write permissions. Only read-level tokens SHALL be
    accessible to agent processes.") and SP1 ("At all times during agent execution, the agent
    process SHALL NOT possess tokens or credentials permitting GitHub write operations.") are
    the normative requirements that implement this design principle. Both sources fully
    consistent; this spec provides the formal MUST-level statement of what that note describes
    as a platform design principle.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as "pre-approved actions the AI can
    request without write permissions"): The spec provides the formal implementation of this
    pattern. The NDJSON pipeline (AR2), the seven-stage validation (Claim 12), and the six
    security invariants (Claim 5) are the technical apparatus behind the conceptual description.
  - `docs-ghaw-mcps.md` Claim 1 (custom MCP servers must be read-only; write operations go
    through Safe Outputs): The spec's AR1 and AR2 provide the normative enforcement: agents
    have no write tokens, and all writes go through the NDJSON pipeline → Safe Output Processor.
    MCP servers that perform writes bypass this pipeline entirely, which is why the MCP docs
    state the read-only policy. The spec explains *why* the policy exists.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth: compilation-time
    validation → runtime isolation → permission separation → network controls → output
    sanitization): The spec maps to these layers precisely. Component C1 (Workflow Compiler)
    = Layer 1; SP1/AR1 = Layer 3; SP4/Stage 3 + SP2/Stage 2 = Layer 5. The spec adds two
    elements not named in that note's five-layer model: SP5 (provenance traceability) and the
    all-or-nothing max limit semantics (Claim 6). Together, the two sources provide the
    complete picture: the five-layer model names the defense strategy; the spec provides the
    normative implementation requirements for each layer.
  - `docs-ghaw-dataops.md` Claim 7 (`safe-outputs: create-discussion` with `close-older-
    discussions: true` + `max: 1`): The spec explains the semantics of `max: 1` (all-or-
    nothing rejection — Claim 6) and why footers appear on Discussions created by DataOps
    workflows (SP5 requires provenance metadata — Claim 8). The DataOps note shows the
    configuration; this spec explains what the configuration normatively enforces.
  - `docs-ghaw-projectops.md` Claim 4 (dual-token layout for read/write project operations):
    The dual-token layout implements SP1 at the credential level — the read token (used by the
    MCP Gateway, Component C2) satisfies AR1; the write token (held only by the Safe Output
    Processor, Component C3) is isolated from the agent per the three-component architecture.
    ProjectOps applies the same principle to a domain-specific credential split.
  - `docs-ghaw-projectops.md` Claim 5 (four project-specific safe output commands:
    `update-project`, `create-project-status-update`, `create-project`, `add-comment`): The
    spec documents that 30+ output types exist. ProjectOps's four project-specific commands
    are named operation types within that larger catalog. The spec's conformance model (C2)
    explains how an implementation could support only the core types while omitting some of
    the project-specific ones.

- **Contradicts**: None. No existing source note makes claims that materially oppose any of
  the spec's security invariants, architectural requirements, conformance model, or pipeline
  stages. The five-layer model from `docs-ghaw-how-they-work.md` Claim 3 is consistent with
  the spec's component architecture and security properties — the spec provides more formal
  and more detailed requirements within the same overall design. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **AR2 (NDJSON artifact-storage communication channel)**: No prior corpus note documents
    that the agent communicates intended operations by writing NDJSON to GitHub Actions
    artifact storage, not by calling the GitHub API. This is the implementation mechanism
    that makes privilege separation possible and auditable. Prior notes describe Safe Outputs
    as a permission-separation mechanism without explaining the communication channel.
  - **All-or-nothing max limit semantics** (Claim 6): No prior note states that exceeding a
    `max` limit rejects ALL operations of that type, not just the excess. This is a
    non-obvious behavior with significant operational consequences for workflow tuning.
  - **Six security invariants as a formal guarantee set** (Claim 5): Prior notes describe the
    five-layer security model (conceptual); this spec provides six normative invariants that
    define what "compliant" means. SP3 (limit enforceability) and SP5 (provenance traceability)
    are new — not captured in any existing source note.
  - **Content sanitization threat taxonomy** (Claim 7): Prior notes mention "output
    sanitization" as Layer 5 of the security model but do not name what it sanitizes. The
    spec names three threat categories: malicious URLs, command injection, credential patterns.
  - **Conformance classes C1/C2** (Claim 11): No prior note documents that Safe Outputs
    implementations have two formally defined conformance classes, or that security invariants
    (SP1-SP6) are mandatory in both while output-type support is optional in C2. Relevant
    for teams building Custom Safe Outputs or gh-aw integrations.
  - **Seven-stage validation pipeline with CONDITIONAL stages** (Claim 12): Prior notes
    reference output sanitization as a layer; this spec names seven specific stages with their
    ordering and conditionality. The CONDITIONAL status of stages 4-6 explains why workflows
    without `allowed-domains` or `allowed-github-references` still have a valid pipeline.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add three-component architecture as the Safe Outputs implementation model** (Claim 2):
  When practitioners configure Safe Outputs in workflow frontmatter, they are instructing all
  three components: the Workflow Compiler (C1) validates configuration at compile time; the
  MCP Gateway Server (C2) intercepts and records agent operation declarations; the Safe Output
  Processor (C3) validates and executes. Practitioners who understand this model can debug
  Safe Outputs failures by identifying which component failed. Currently Ch02 likely describes
  Safe Outputs at the configuration level without explaining the runtime architecture.

- **Document all-or-nothing `max` semantics** (Claim 6): The guide should warn practitioners
  that `max: N` means "if the agent attempts more than N operations of this type, ALL N+
  operations are rejected." Setting `max: 1` on `add-comment` does not mean "post at most
  one comment" — it means "post exactly one comment OR fail entirely if the agent tries to
  post more than one." Practitioners tuning DataOps and IssueOps workflows must account for
  this. Pair with the DataOps `max: 1` on `create-discussion` (`docs-ghaw-dataops.md`
  Claim 7).

- **Document two-level configuration model** (Claim 10): Global parameters (`footer`,
  `staged`, `allowed-domains`, `allowed-github-references`) apply across all output types
  and define the security boundary. Type-specific blocks customize operational parameters
  (`max`, type-specific `footer`) within that boundary. Practitioners should know: security
  constraints (domains, cross-repo references) are global-only; operational limits (`max`)
  are per-type.

### Chapter 03: Safety and Verification

- **Establish SP1-SP6 as the Safe Outputs security contract** (Claim 5): Chapter 03 currently
  describes the five-layer security model. Add the six security invariants as the formal
  guarantee set for the Safe Outputs mechanism specifically. Practitioners can use SP1-SP6
  as an evaluation checklist: does this implementation maintain all six? SP5 (provenance)
  and SP3 (all-or-nothing limits) are not in the five-layer model and deserve explicit
  coverage.

- **Name content sanitization's three threat vectors** (Claim 7): Layer 5 (output sanitization)
  in the five-layer model should be described in terms of what it defends against: malicious
  URLs (preventing exfiltration links in comments/issues), command injection (preventing
  shell-executable payloads in GitHub content), and credential patterns (preventing accidental
  or deliberate credential leak via AI-generated content). These three vectors map to
  real prompt-injection attack patterns.

- **Cite NDJSON artifact-storage as the privilege-separation mechanism** (Claim 3, AR2):
  The reason agent compromise cannot lead to direct GitHub API writes is that the agent holds
  no write tokens AND communicates only via NDJSON artifact storage. An attacker who
  compromises an agent process can write arbitrary NDJSON, but that NDJSON still passes through
  the Safe Output Processor's seven-stage validation pipeline before any GitHub API call.
  This is the concrete implementation of "defense in depth" for Safe Outputs.

- **Document conformance classes for Custom Safe Outputs builders** (Claim 11): Teams
  implementing Custom Safe Outputs or gh-aw forks should target at minimum Class C2: all six
  security invariants (SP1-SP6) and architectural requirements (AR1, AR2) are non-negotiable;
  the output type catalog can be scoped to what the use case requires.

## Extraction Notes

1. **Source is a formal specification document**: The Safe Outputs MCP Gateway Specification
   v1.19.0 uses RFC 2119 requirement terminology throughout (MUST, SHALL, SHOULD, MAY,
   REQUIRED). The verbatim quotes for normative requirements are prefixed with their
   requirement strength — this is the appropriate citation format for spec documents.

2. **WebFetch returned AI-summarized content, not raw HTML**: The page is an Astro/Starlight
   SPA. Multiple targeted fetch requests were used to extract specific sections. The verbatim
   quotes in this note were obtained via targeted fetch requests asking for exact character-
   for-character reproduction of specific spec sections. Minor formatting variations in the
   YAML or prose are possible where the page uses complex layouts. Normative requirement
   statements (MUST, SHALL, etc.) are assessed as accurately captured given their critical
   role in this type of document.

3. **30+ safe output types exist but are not individually extracted**: The spec documents
   over 30 operation types (including `create-issue`, `add-comment`, `create-pull-request`,
   `update-project`, and others). Individual type schemas were not extracted — the focus was
   on the architectural properties, security model, and operational features that apply across
   all types. The `docs-ghaw-projectops.md` note covers four project-specific types in detail.

4. **No publication date**: The specification does not carry a publication date. `date_published`
   is left null. The spec identifies as Working Draft v1.19.0 targeting gh-aw v1.8.0+.

5. **No contradictions filed**: Reviewed all existing gh-aw source notes. No claims in this
   source materially oppose any existing note. The five-layer model in `docs-ghaw-how-they-work.md`
   and the spec's component architecture and invariants describe the same system at different
   levels of formality; they are complementary, not contradictory.

6. **Linked pages not followed**: The spec references individual safe output type reference
   pages (e.g., the full `create-issue` and `add-comment` parameter schemas). These were not
   followed — they cover per-type operational details beyond the scope of this structural note.
   If individual type schemas become relevant to the guide, they warrant separate source notes.
