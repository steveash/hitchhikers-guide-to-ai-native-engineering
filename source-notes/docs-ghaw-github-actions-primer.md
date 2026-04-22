---
source_url: https://github.github.com/gh-aw/guides/github-actions-primer
source_type: docs
title: "GitHub Agentic Workflows: GitHub Actions Primer"
author: GitHub Agentic Workflows team (official guides documentation)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#296"
---

# GitHub Agentic Workflows: GitHub Actions Primer

> The side-by-side comparison reference for how agentic workflows differ from
> traditional GitHub Actions — establishes the concrete architectural divergences
> (compilation model, permission model, network access, execution environment,
> auditability) and the 20-minute agent execution step timeout as the key
> practitioner constraint.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guide, "Guides > GitHub Actions
  Primer" — conceptual background for engineers coming from traditional GitHub Actions;
  not API reference or practitioner case study)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (the same
  team behind the "Peli's Agent Factory" blog series and `docs-ghaw-how-they-work.md`).
  This page is the primer for practitioners familiar with standard GitHub Actions who are
  learning how gh-aw diverges. Claims about compilation model, execution environment, and
  permission model are authoritative for the gh-aw platform.
- **Scope**: Introduces GitHub Actions fundamentals (YAML, jobs, steps, triggers) in the
  context of agentic workflows, then documents where gh-aw diverges from standard Actions.
  The comparison table is the central artifact. Does NOT cover: the full compilation
  workflow (that is `docs-ghaw-how-they-work.md`), the five-layer security architecture
  (same), specific workflow examples (blog series), or the authoring lifecycle
  (`docs-ghaw-agentic-authoring.md`). This page is the "how is this different from Actions
  I already know?" answer.

## Extracted Claims

### Claim 1: Agentic workflows compile from natural-language markdown into secure GitHub Actions YAML, adding AI-driven decision-making on top of deterministic Actions infrastructure

- **Evidence**: The page documents the compilation model and comparison: "agentic workflows
  compile from markdown into secure GitHub Actions YAML while adding AI-driven
  decision-making capabilities." Comparison table: Definition: "YAML" (traditional) vs.
  "Markdown" (agentic).
- **Confidence**: settled (first-party documentation; consistent with the compilation
  model in `docs-ghaw-how-they-work.md`)
- **Quote**: "agentic workflows compile from markdown into secure GitHub Actions YAML
  while adding AI-driven decision-making capabilities"
- **Our assessment**: This is the clearest one-sentence description of the gh-aw
  compilation model. The primer states it as a definition, not as an explanation of a
  design decision. For Ch02 (Harness Engineering): use as the opening framing — "agentic
  workflows are markdown that compiles to GitHub Actions YAML." The "secure" qualifier
  matters: this is not a simple transpilation but a security-hardening step. Corroborates
  `docs-ghaw-how-they-work.md` Claim 7 (the compilation model from canonical documentation),
  which provides more technical detail.

### Claim 2: The agent execution step in agentic workflows defaults to a 20-minute timeout — 18× shorter than the 360-minute default for standard GitHub Actions jobs

- **Evidence**: Explicitly documented: "Default timeout is 360 minutes for standard GitHub
  Actions jobs; the agent execution step in agentic workflows defaults to 20 minutes."
- **Confidence**: settled (first-party documentation; specific numeric values)
- **Quote**: "Default timeout is 360 minutes for standard GitHub Actions jobs; the agent
  execution step in agentic workflows defaults to 20 minutes."
- **Our assessment**: This is the most actionable practitioner constraint in this source
  and is entirely new to the corpus. At 18× tighter than the standard GitHub Actions
  timeout, the 20-minute ceiling is a hard design constraint for harness engineers.
  Workflows that iterate through large file sets, call external services with latency, or
  wait for slow CI systems will hit this limit. For Ch02: document as a hard constraint
  that must inform agentic task scoping — if a task requires more than ~15 minutes of
  active agent execution time, it needs to be decomposed into shorter steps or use
  checkpointing.

### Claim 3: Write permissions are not used explicitly in agentic workflows — all GitHub API write operations are declared through safe outputs, which validate, constrain, and sanitize GitHub API interactions

- **Evidence**: Permission model section: "With GitHub Agentic Workflows, write permissions
  are not used explicitly. Instead much more restricted capabilities to write to GitHub are
  declared through safe outputs, which validate, constrain and sanitize all GitHub API
  interactions."
- **Confidence**: settled (first-party documentation; explicit design statement)
- **Quote**: "With GitHub Agentic Workflows, write permissions are not used explicitly.
  Instead much more restricted capabilities to write to GitHub are declared through safe
  outputs, which validate, constrain and sanitize all GitHub API interactions."
- **Our assessment**: This is a more explicit statement of the Safe Outputs security design
  than any other source in the corpus. `docs-ghaw-how-they-work.md` Claim 4 states "no
  write access by default" — the primer goes further: write permissions are "not used
  explicitly" at all. Safe outputs are the *only* write path, and they perform three
  distinct functions: validation (is the requested operation well-formed?), constraint (is
  it in the permitted set?), and sanitization (is the output clean before it reaches the
  GitHub API?). The three-function description adds specificity not present in the
  how-they-work docs. For Ch03 (Safety and Verification): this phrasing — "write
  permissions are not used explicitly" — is the clearest argument for why gh-aw's
  permission model is more restrictive than standard GITHUB_TOKEN least-privilege.

### Claim 4: The execution environment for agentic workflows is an enhanced sandbox with MCP isolation, not the standard runner VM used by traditional GitHub Actions

- **Evidence**: Comparison table: Execution environment: "Standard runner VM" (traditional)
  vs. "Enhanced sandbox with MCP isolation" (agentic).
- **Confidence**: emerging (first-party documentation; the specific implementation of
  "MCP isolation" within the sandbox is not detailed on this page)
- **Quote**: "Enhanced sandbox with MCP isolation" (comparison table entry)
- **Our assessment**: The "MCP isolation" qualifier adds a term not used in the five-layer
  security model of `docs-ghaw-how-they-work.md`. That note's Layer 2 is "Runtime
  isolation" — the primer specifies that this isolation includes MCP-layer hardening
  specifically. The implication: the sandbox is designed not just to prevent the agent
  process from accessing host resources, but to contain threats arriving through MCP tool
  responses (prompt injection via tool output, rogue MCP server responses). This is a
  meaningful distinction for practitioners evaluating the trust surface of their agentic
  workflows.

### Claim 5: Traditional GitHub Actions have unrestricted network access; agentic workflows restrict to allowlisted domains only

- **Evidence**: Comparison table: Network access: "Unrestricted" (traditional) vs.
  "Allowlisted domains only" (agentic).
- **Confidence**: settled (first-party documentation; explicit comparison)
- **Quote**: (from comparison table) Network access: "Unrestricted" vs. "Allowlisted
  domains only"
- **Our assessment**: The allowlist is the concrete mechanism behind Layer 4 (Network
  controls) of the five-layer security model in `docs-ghaw-how-they-work.md`. The primer
  makes the contrast explicit: practitioners migrating from traditional GitHub Actions
  workflows that make unrestricted external API calls will need to configure domain
  allowlists. This is a breaking change for any workflow that calls external services not
  on the allowlist. For Ch02: document domain allowlist configuration as a required
  harness engineering step for any gh-aw workflow that calls external tools or APIs.

### Claim 6: Agentic workflows provide enhanced auditability through agent reasoning logs, beyond standard GitHub Actions workflow logging

- **Evidence**: Comparison table: Auditability: "Standard workflow logging" (traditional)
  vs. "Enhanced with agent reasoning logs" (agentic).
- **Confidence**: emerging (comparison table entry; what "agent reasoning logs" contain
  and how to access them is not detailed on this page — see `blog-ghaw-agent-observability.md`
  for the observability architecture)
- **Quote**: "Enhanced with agent reasoning logs"
- **Our assessment**: Standard GitHub Actions logs capture what happened (step output, exit
  codes). Agent reasoning logs capture the agent's decision process — the why behind its
  actions. This is the observability primitive that enables audit of agentic behavior, not
  just output. For Ch03: reasoning logs are the primary post-hoc audit tool for agentic
  workflows. The primer introduces the concept; `blog-ghaw-agent-observability.md` provides
  the full architecture for consuming them.

### Claim 7: The default branch is the trust boundary for gh-aw workflows — all definitions must be on the default branch before activation, preventing privilege escalation from feature branches

- **Evidence**: "Workflows must be stored on the main or default branch to be active" and
  the workflow storage section explains this "ensures changes undergo code review, maintains
  an audit trail, prevents privilege escalation from feature branches, and treats the
  default branch as a trust boundary."
- **Confidence**: settled (first-party documentation; this is standard GitHub Actions
  behavior that gh-aw inherits and emphasizes)
- **Quote**: "ensures changes undergo code review, maintains an audit trail, prevents
  privilege escalation from feature branches, and treats the default branch as a trust
  boundary"
- **Our assessment**: The "trust boundary" framing is important for harness security. A PR
  that modifies a workflow definition cannot run that modified workflow until the PR is
  merged — preventing a compromised PR from activating a malicious workflow. For Ch03:
  the default branch as trust boundary is the access control model for workflow definitions
  themselves, distinct from the permission model for what a running workflow can do.
  Corroborates compilation-time validation (Layer 1) in `docs-ghaw-how-they-work.md` Claim
  3 — the trust boundary is enforced at the deployment gate, not just at compile time.

### Claim 8: workflow_dispatch enables manual execution from any branch, providing the development-time escape hatch for testing workflow changes before merging to the default branch

- **Evidence**: The page documents `workflow_dispatch` as enabling "manual workflow
  execution from any branch for development and testing." Separately: "The workflow
  definition must be merged to the main branch before it can be executed" — the two
  together describe that `workflow_dispatch` is the exception for pre-merge testing.
- **Confidence**: emerging (the interaction between the default-branch activation
  requirement and `workflow_dispatch`'s any-branch capability is documented but the
  exact mechanics are not detailed)
- **Quote**: "Enables manual workflow execution from any branch for development and
  testing"
- **Our assessment**: The `workflow_dispatch` testing pattern is the development-time
  escape hatch from the default-branch trust boundary. A practitioner can test a modified
  workflow on a feature branch before merging, but only via manual dispatch — it won't
  trigger automatically on push or PR events. For Ch02: document as the recommended
  iterative development pattern: author on a feature branch, test via `workflow_dispatch`,
  merge to default when ready. This complements `docs-ghaw-how-they-work.md` Claim 11's
  compile → watch → run → review loop and `docs-ghaw-agentic-authoring.md` Claim 1 (the
  init step that precedes the loop).

### Claim 9: Each job in GitHub Actions runs in a fresh VM with results shared between jobs via artifacts — the job isolation model that agentic workflows inherit

- **Evidence**: Core Concepts section: "Each job runs in a fresh VM, and results are
  shared between jobs using artifacts."
- **Confidence**: settled (standard GitHub Actions infrastructure documented here as
  context for practitioners new to Actions)
- **Quote**: "Each job runs in a fresh VM, and results are shared between jobs using
  artifacts."
- **Our assessment**: The fresh-VM-per-job model means no shared filesystem state between
  jobs by default — each job starts clean. For harness engineers: multi-job workflows must
  explicitly pass state via artifacts. This is the architectural reason why the
  `cache-memory` tool in `docs-ghaw-audit-with-agents.md` (Claim 5) exists — it is the
  platform-native solution to statelessness across runs.

## Concrete Artifacts

### Comparison Table: Traditional GitHub Actions vs. GitHub Agentic Workflows

```
| Aspect                | Traditional GitHub Actions     | GitHub Agentic Workflows         |
|-----------------------|-------------------------------|----------------------------------|
| Definition language   | YAML                          | Natural-language markdown        |
| Decision-making       | Fixed if-then logic           | AI-powered contextual            |
| Write operations      | Direct GitHub API (GITHUB_TOKEN) | Sanitized safe-outputs only   |
| Network access        | Unrestricted                  | Allowlisted domains only         |
| Execution environment | Standard runner VM            | Enhanced sandbox with MCP isolation |
| Auditability          | Standard workflow logging     | Enhanced with agent reasoning logs |
```
*Source: GitHub Actions Primer comparison table*

### Agent Execution Timeout Values

```
Standard GitHub Actions job timeout:  360 minutes (6 hours)
Agent execution step (gh-aw) timeout: 20 minutes
Ratio:                                18× shorter than standard

Practitioner constraint: tasks requiring > ~15 minutes of active agent execution
must be decomposed into shorter steps or use checkpointing.
```
*Source: GitHub Actions Primer, timeout documentation*

### Safe Outputs Permission Model (Primer Description)

```
Traditional GitHub Actions:
  - Write permissions granted via GITHUB_TOKEN (write scope)
  - Workflows make direct GitHub API calls

GitHub Agentic Workflows:
  - Write permissions NOT used explicitly
  - All write operations → safe outputs
  - Safe outputs perform: validate + constrain + sanitize on GitHub API interactions
  - Effect: agent can only modify GitHub state through a pre-approved, sanitized
    capability handler — not through direct API access
```
*Source: GitHub Actions Primer, Permission Model section*

### Default Branch Trust Boundary

```
Activation requirement:
  Workflow definitions MUST be on the default/main branch before they are active.

Security properties:
  1. Changes undergo code review before activation
  2. Audit trail maintained for all workflow changes
  3. Privilege escalation from feature branches prevented
  4. Default branch = trust boundary for workflow definitions

Development escape hatch:
  workflow_dispatch → enables manual execution from any branch (for testing)
  (push/PR/schedule triggers still require default branch)
```
*Source: GitHub Actions Primer, Workflow Storage and Testing sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default"): this primer
    adds the explicit statement "write permissions are not used explicitly" — a stronger
    phrasing of the same design principle, plus the three-function (validate/constrain/
    sanitize) description of safe outputs that is more specific than the how-they-work docs.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security model): the primer's
    comparison table maps onto Layers 3 (permission separation / write operations row),
    4 (network controls / network access row), 2 (runtime isolation / execution environment
    row), and 5 (output sanitization / write operations row) respectively. The comparison
    table is a practitioner-facing summary of the underlying security architecture.
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation model): the
    primer states the compilation direction plainly ("compile from markdown into secure
    GitHub Actions YAML") as onboarding context; the how-they-work note provides the
    technical detail of the compiled artifact.
  - `docs-ghaw-how-they-work.md` Claim 2 (deterministic infrastructure + AI decisions):
    the comparison table's "Decision-making" row (Fixed if-then vs. AI-powered) and
    "Definition language" row (YAML vs. Markdown) give concrete form to this same
    architectural claim.

- **Extends**:
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` pattern):
    the primer provides the conceptual "why" for the compilation step (markdown → secure
    YAML) that the blog post documents as a practitioner CLI operation. The primer is the
    background; the blog post is the hands-on procedure.
  - `docs-ghaw-agentic-authoring.md`: that note covers the authoring lifecycle (init,
    create, debug); this primer is the prerequisite conceptual read that explains the
    underlying Actions architecture. Complete practitioner on-ramp = this primer first,
    then the authoring guide.
  - `docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory` for rolling baselines):
    the fresh-VM-per-job isolation model (Claim 9 here) is the architectural reason
    why cache-memory exists — stateless jobs require a platform mechanism to persist
    state across runs.

- **Contradicts**: None. The primer's "write permissions are not used explicitly" is a
  stronger phrasing than `docs-ghaw-how-they-work.md`'s "no write access by default"
  but is not a contradiction — both describe the same design from different angles (the
  how-they-work note describes the default capability state; the primer states that
  write permissions are architecturally absent from the model). No contradiction issue
  filed.

- **Novel**:
  - **20-minute agent execution step timeout** (Claim 2): The specific value (20 min vs.
    360 min for standard jobs) is not mentioned in any existing source note. This is a
    hard practitioner constraint that is entirely new to the corpus.
  - **"Write permissions are not used explicitly" phrasing** (Claim 3): While the Safe
    Outputs model is documented in `docs-ghaw-how-they-work.md`, the explicit statement
    that write permissions are "not used" (not just "off by default") plus the three-function
    (validate/constrain/sanitize) description adds specificity new to the corpus.
  - **"Enhanced sandbox with MCP isolation" as execution environment term** (Claim 4):
    The MCP-specific isolation qualifier is not named in the five-layer model. This primer
    introduces "MCP isolation" in the execution sandbox context.
  - **Agent reasoning logs as an explicit auditability primitive** (Claim 6): No existing
    source note names "agent reasoning logs" as a distinct, enhanced logging capability
    contrasted against standard Actions logging.
  - **Default branch as trust boundary framing** (Claim 7): The "trust boundary" label
    for the default branch requirement is a security framing not present in existing
    source notes.
  - **Comparison table as single-reference artifact** (Concrete Artifacts): The
    side-by-side comparison across six dimensions (definition, decision-making, write
    operations, network, environment, auditability) is the most concise architectural
    summary of gh-aw vs. traditional Actions in the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add 20-minute agent execution step timeout as a hard constraint** (Claim 2): Harness
  engineers must size agentic tasks to fit within 20 minutes of active agent execution.
  Tasks that may exceed this must be decomposed into shorter steps or use checkpointing.
  Add as a concrete constraint alongside the compile → watch → run → review loop from
  `docs-ghaw-how-they-work.md` Claim 11.
- **Add domain allowlist configuration as a required harness step** (Claim 5): Any gh-aw
  workflow calling external services must explicitly allowlist those domains. Warn
  practitioners migrating from traditional GitHub Actions — unrestricted network access
  is not available in gh-aw.
- **Add `workflow_dispatch` as the recommended development testing trigger** (Claim 8):
  Before merging to the default branch, test workflow changes via manual dispatch on a
  feature branch. Document as part of the complete development lifecycle: init → compile
  → `workflow_dispatch` (feature branch testing) → merge → production trigger.

### Chapter 03: Safety and Verification

- **Add "write permissions are not used explicitly" as the definitive safe outputs
  framing** (Claim 3): Use this primer's phrasing to explain why gh-aw's permission model
  is more restrictive than standard GITHUB_TOKEN least-privilege: write access is
  architecturally absent, not just set to a restrictive default.
- **Add default branch as trust boundary** (Claim 7): The trust boundary framing belongs
  in Ch03's access control section — it separates "what can a running workflow do?" (Safe
  Outputs model) from "who controls what runs?" (default branch gate as code-review
  requirement).
- **Add agent reasoning logs as the audit primitive** (Claim 6): When investigating
  unexpected agent behavior, reasoning logs are the primary post-hoc tool. Add a pointer
  to `blog-ghaw-agent-observability.md` for the full observability architecture.

### Chapter 01: Daily Workflows

- **Comparison table as practitioner onboarding reference** (Concrete Artifacts): The
  six-row comparison table is the fastest on-ramp for a developer familiar with GitHub
  Actions who needs to understand what changes with gh-aw. Add it (or a condensed form)
  to Ch01 as the "what's different" summary for practitioners evaluating adoption.

## Extraction Notes

1. **Two fetches required**: The first fetch returned the comparison table (4 visible
   rows) and core documentation. A second fetch with targeted prompting recovered the
   timeout values (360 min vs. 20 min), the "Enhanced sandbox with MCP isolation"
   execution environment entry, and the auditability row. Complete comparison table
   assembled from both fetches.

2. **Source is primer-level content, not a deep technical reference**: Per Prospector
   guidance, this page provides the conceptual foundation for gh-aw vs. traditional
   Actions. The detailed security architecture is in `docs-ghaw-how-they-work.md`; the
   authoring lifecycle is in `docs-ghaw-agentic-authoring.md`. This note focuses on
   what the primer adds that those notes do not cover — primarily the comparison table,
   the 20-minute timeout, and the "write permissions not used explicitly" phrasing.

3. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with the current gh-aw
   platform as of 2026-04-22.

4. **20-minute timeout elevated as a key finding**: The Prospector triage identified this
   as a "concrete constraint relevant to Ch02 harness design." It is not mentioned in any
   existing source note and is the most actionable novel claim in this source.

5. **No contradictions filed**: Reviewed `docs-ghaw-how-they-work.md`,
   `docs-ghaw-agentic-authoring.md`, `blog-gh-aw-operations-release-workflows.md`, and
   related source notes. The stronger "write permissions are not used explicitly" phrasing
   is a more direct statement of the same design principle as `docs-ghaw-how-they-work.md`
   Claim 4, not a contradiction.
