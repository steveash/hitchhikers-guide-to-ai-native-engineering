---
source_url: https://github.github.com/gh-aw/examples/maintaining-repos
source_type: docs
title: "GitHub Agentic Workflows: Automated Repository Maintenance (Examples)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#876"
---

# GitHub Agentic Workflows: Automated Repository Maintenance (Examples)

> A practical worked guide integrating three GHAW patterns — Repo Assist as
> triage layer, safe-outputs output control, and integrity filtering for input
> validation — into a concrete application of automated repository maintenance at
> scale in public repositories, with extractable YAML configurations, CLI command
> sequences, and a taxonomy of six common failure modes.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `examples/maintaining-repos`
  page — in the `examples/` section, which provides integrated worked guides as
  distinct from `patterns/` pages that document individual design patterns and
  `reference/` pages that document field schemas. This is the examples counterpart
  to the guides page at `guides/maintaining-repos` (issue #437, not yet mined),
  intended to provide runnable configurations rather than narrative explanation.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw`
  CLI. Configuration field names, CLI commands, and behavior descriptions are
  authoritative for the `gh aw` platform. The page uses current (v0.72.0+) field
  naming conventions (`user-rate-limit`, `max-runs-per-window`) consistent with
  the breaking change documented in `blog-ghaw-weekly-2026-05-11.md` Claim 6.
- **Scope**: How to apply safe-outputs, integrity filtering, and Repo Assist
  together for public repository maintenance at scale. Covers: Repo Assist as
  triage layer, safe-outputs block declaration and available output types,
  integrity filtering levels and reactions-as-trust-signals, scaling strategies
  (token budget, rate limiting, pre-activation association skips, concurrency,
  repository scoping), debugging workflows (AI-assisted and CLI-based), and a
  six-category common failure patterns taxonomy. Does NOT cover: the formal
  normative safe-outputs specification (`docs-ghaw-safe-outputs-specification.md`),
  the complete integrity filtering reference (`docs-ghaw-integrity-reference.md`),
  or the full eight-mechanism anti-runaway taxonomy
  (`docs-ghaw-rate-limiting-controls.md`). This page is the practical integration
  guide; the reference pages provide the formal specifications.

## Extracted Claims

### Claim 1: Repo Assist is the recommended entry point for any public repository — it classifies incoming issues and PRs and gates downstream code-modifying agents

- **Evidence**: The page positions Repo Assist explicitly as "the recommended
  starting point for any public repository" in its opening section. The pattern
  runs on every new issue or PR, classifies the content, routes work, and functions
  as a prerequisite that other code-modifying agents depend on.
- **Confidence**: emerging (first-party recommendation; the prescriptive
  positioning as "recommended starting point" is editorial guidance, not a
  measured outcome)
- **Quote**: "Repo Assist is a workflow that runs on every new issue or PR,
  classifies the content, and routes work to the right place."
- **Our assessment**: The Repo Assist triage layer pattern is the most novel
  architectural claim in this source. The design separates lightweight
  classification (Repo Assist: labels, comments, routing) from heavyweight
  code-modifying operations (downstream agents). This prevents runaway resource
  consumption from every opened issue triggering a full code-modifying agent.
  Repo Assist absorbs the volume of incoming contributions and only escalates
  to expensive agents when warranted by classification. For Ch02 (Harness
  Engineering): document the triage-layer pattern explicitly — for any public
  repository receiving untrusted contributions, Repo Assist should be the first
  workflow deployed, with code-modifying agents added as downstream consumers of
  its routing decisions. For Ch03 (Safety and Verification): the triage layer is
  the architectural response to the threat of high-volume untrusted input on
  public repositories.

### Claim 2: Safe-outputs is the primary mechanism for controlling what a workflow can do — every side-effectful GitHub operation must be explicitly declared in the `safe-outputs:` block or the runtime blocks it

- **Evidence**: The page's "Controlling Workflow Outputs with Safe-Outputs" section
  establishes this as the output control mechanism: every action producing a side
  effect must be declared, or "the system rejects it before reaching the API."
  Eight output types are enumerated covering the full spectrum of repository
  maintenance operations.
- **Confidence**: settled (first-party documentation; consistent with the formal
  normative definition in `docs-ghaw-safe-outputs-specification.md` Claim 1)
- **Quote**: "Safe-outputs is the primary mechanism for controlling what a workflow
  can do. Every action that produces a side-effect on GitHub — labeling an issue,
  posting a comment, opening a pull request, merging — must be explicitly declared
  in the `safe-outputs:` block."
- **Our assessment**: This practical framing of safe-outputs as "declare what you
  need or it's blocked" is clearer for practitioners than the formal normative
  definition. The enumeration of eight specific output types relevant to
  maintenance workflows gives practitioners a concrete allowlist to work from.
  Corroborates `docs-ghaw-safe-outputs-specification.md` Claim 1 (formal normative
  definition) and Claim 4 (P3: Configurable Constraint Enforcement — "Workflow
  authors explicitly configure permitted operations and constraints"). For Ch02:
  use this framing alongside the specification's formal definition to give
  practitioners both the conceptual model and the normative requirements.

### Claim 3: Eight safe-output types cover the full spectrum of repository maintenance actions: label-issue, comment-issue, comment-pull-request, create-pull-request, merge-pull-request, close-issue, create-issue, assign-issue

- **Evidence**: The page provides a complete table of safe-output types with their
  capabilities. All eight types are enumerated. The table maps each type to a
  specific maintenance operation.
- **Confidence**: settled (first-party documentation; the type names are explicit
  in the table; `merge-pull-request` is flagged as "experimental")
- **Quote**: (no single-sentence quote; the table maps type names to capabilities
  — see Concrete Artifacts)
- **Our assessment**: This enumeration is the practitioner's checklist for
  configuring repository maintenance safe-outputs blocks. The `merge-pull-request`
  "experimental" flag is important — teams should not rely on it for production
  repository maintenance workflows until it reaches stable status. The eight types
  represent a complete write surface for repository maintenance operations: triage
  (label, comment), contribution handling (create-pr, close-issue), work assignment
  (assign-issue), and new work creation (create-issue). For Ch02: use this
  enumeration when documenting the safe-outputs configuration pattern for
  maintenance workflows.

### Claim 4: Integrity filtering is the primary mechanism for controlling what content the agent sees — it evaluates author trust and removes items below the threshold before the agent's context is assembled

- **Evidence**: The page's "Controlling Workflow Inputs with Integrity Filtering"
  section establishes this as the input control mechanism: the system "evaluates
  the author of each issue, PR, or comment and removes items that don't meet the
  configured trust threshold — before the agent's context is assembled."
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-integrity-reference.md` Claim 1)
- **Quote**: "Integrity filtering is the primary mechanism for controlling what
  content the agent sees. It evaluates the author of each issue, PR, or comment
  and removes items that don't meet the configured trust threshold — before the
  agent's context is assembled."
- **Our assessment**: This claim positions integrity filtering as the input
  complement to safe-outputs' output control. Together they form the complete
  "what the agent sees" + "what the agent can do" boundary. The pre-assembly
  timing ("before the agent's context is assembled") is architecturally significant:
  unlike threat detection (which analyzes agent output), integrity filtering acts
  before the agent runs — the filtered content never enters the AI engine's context
  at all. This is consistent with `docs-ghaw-integrity-reference.md` Claim 1's
  "filters based on trust rather than permissions" framing. For Ch03 (Safety and
  Verification): integrity filtering is the input restriction layer; safe-outputs
  is the output enforcement layer. Both are required for a complete defense-in-depth
  harness for public repositories.

### Claim 5: Integrity filtering directly reduces token consumption because filtered items never appear in the agent's context window — making it both a security control and a cost optimization

- **Evidence**: The page's scaling strategies section explicitly links integrity
  filtering to token budget: "Integrity filtering directly reduces token consumption:
  items filtered by the gateway never appear in the agent's context window." Users
  should monitor trends with `gh aw logs --format markdown --count 20`.
- **Confidence**: emerging (first-party claim; the connection between filtering and
  token consumption is structurally correct given the filtering-before-context-assembly
  design, but no quantification is provided)
- **Quote**: "Integrity filtering directly reduces token consumption: items filtered
  by the gateway never appear in the agent's context window."
- **Our assessment**: This dual-purpose framing (security + cost) is new to the
  corpus. The `docs-ghaw-integrity-reference.md` note covers integrity filtering
  as a security mechanism exclusively; this page adds the cost optimization angle.
  For high-volume public repositories where many low-integrity contributions arrive
  continuously (e.g., first-time contributor spam), setting `min-integrity: approved`
  filters most of the noise before it reaches the AI engine — reducing both
  security risk and token spend. For Ch02: document integrity filtering as having
  a dual purpose: security (preventing prompt injection via untrusted content) and
  cost optimization (reducing context window size). For Ch05 (Organization/Teams):
  use this framing when justifying integrity filtering adoption to cost-conscious
  stakeholders.

### Claim 6: Reactions can serve as trust signals to promote or demote content integrity without label management — enabled by `features.integrity-reactions: true` with `tools.github.min-integrity`

- **Evidence**: The page's "Reactions as Trust Signals" subsection under Integrity
  Filtering documents this feature: maintainers "can use GitHub reactions to
  promote or demote content past the integrity threshold without modifying labels,
  when `features.integrity-reactions: true` is enabled."
- **Confidence**: emerging (first-party documentation; consistent with
  `docs-ghaw-integrity-reference.md` Claim 9 which documents the same feature
  as requiring v0.68.2+)
- **Quote**: (no direct single-sentence verbatim quote for the combined feature
  description; see YAML in Concrete Artifacts)
- **Our assessment**: Corroborates `docs-ghaw-integrity-reference.md` Claim 9
  (reaction-based endorsement from v0.68.2+). This page's contribution is placing
  reactions-as-trust-signals in the repo maintenance workflow context — maintainers
  reviewing incoming contributions can use thumbs-up/thumbs-down reactions to
  approve or flag content for agent processing, without needing to manage a label
  system. This is lower friction than `approval-labels` for high-volume public
  repos. For Ch02: recommend reactions-as-trust-signals as the lightweight
  human-in-the-loop option for repo maintenance workflows that process untrusted
  contributions.

### Claim 7: `user-rate-limit` with `max-runs-per-window` and `window` fields throttles per-user trigger frequency — these are the v0.72.0+ names for what was previously called `rate-limit` and `max-runs`

- **Evidence**: The page shows the YAML configuration using `user-rate-limit:` with
  `max-runs-per-window: 5` and `window: 60`. The v0.72.0 breaking change renaming
  these fields from `rate-limit` and `max-runs` is documented in
  `blog-ghaw-weekly-2026-05-11.md` Claim 6 (PR #31390: `rate-limit` →
  `user-rate-limit`; `max-runs` → `max-runs-per-window`).
- **Confidence**: emerging (first-party example; the field behavior is consistent
  with `docs-ghaw-rate-limiting-controls.md` Claim 8; the renaming is confirmed
  by `blog-ghaw-weekly-2026-05-11.md` Claim 6)
- **Quote**: (no direct prose quote; field names appear in YAML — see Concrete
  Artifacts)
- **Our assessment**: This examples page implicitly confirms that the v0.72.0+
  naming is the current standard for rate limiting configuration in the GHAW
  platform. Practitioners reading the `docs-ghaw-rate-limiting-controls.md`
  source note (which uses the pre-v0.72.0 names `rate-limit` and `max-runs`)
  should update their harness configurations to use `user-rate-limit` and
  `max-runs-per-window`. The field semantics are unchanged — only the names
  differ. For Ch02 (Harness Engineering): all harness template examples should
  use the v0.72.0+ field names. Recommend practitioners update any existing
  configurations that use the deprecated names.

### Claim 8: `skip-author-associations` is a pre-activation guard that uses trigger event payload fields to skip workflow runs before agent execution begins, reducing cost from unnecessary activations

- **Evidence**: The page's "Pre-Activation Association Skips" subsection under
  Scaling Strategies states: "The `on.skip-author-associations` setting enables
  job-level guards using event payload fields to skip runs before agent execution
  begins." The YAML shows this nested under the `on:` trigger configuration,
  e.g., `skip-author-associations.issue_comment: [owner, member, collaborator]`
  to skip runs triggered by owners, members, or collaborators on issue_comment events.
- **Confidence**: emerging (first-party documentation; the field is named and
  demonstrated in YAML; no existing corpus source documents this field)
- **Quote**: (no direct single-sentence verbatim quote; the mechanism is described
  in prose and YAML — see Concrete Artifacts)
- **Our assessment**: `skip-author-associations` is novel to the corpus — no
  existing source note documents this field. The pre-activation timing (before
  agent execution) is important: unlike integrity filtering (which removes specific
  items from agent context) and safe-outputs (which blocks specific write operations),
  `skip-author-associations` prevents the workflow from running at all when the
  triggering author has a specified association. This is a coarser but cheaper
  control: if you know that issues opened by collaborators never need automated
  triage (because collaborators use an internal process), skipping those runs
  entirely saves the activation cost. For Ch02 (Harness Engineering): document
  `skip-author-associations` as the zero-cost scaling mechanism — it gates on
  event metadata without running any agent infrastructure. For Ch05: this is the
  cost-reduction primitive for high-volume repositories where a significant
  fraction of triggers come from trusted internal contributors.

### Claim 9: Concurrency controls for maintenance workflows use dual enforcement (per-workflow and per-engine); `max-parallel` adjusts concurrent processing of issues

- **Evidence**: The "Concurrency Controls" subsection states: "Workflows
  automatically use dual concurrency control (per-workflow and per-engine)" with
  optional `max-parallel` adjustment for parallel processing. The YAML shows
  `concurrency: max-parallel: 3`.
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-rate-limiting-controls.md` Claim 3 and the full concurrency reference)
- **Quote**: (no direct verbatim quote; dual concurrency control and `max-parallel`
  are described in prose and YAML — see Concrete Artifacts)
- **Our assessment**: Corroborates `docs-ghaw-rate-limiting-controls.md` Claim 3
  (dual concurrency control: per-workflow and per-engine). This page adds the
  `max-parallel` configuration for maintenance workflows where concurrent
  processing of multiple issues is desirable — e.g., a repository receiving 50
  issues per day might set `max-parallel: 3` to process three simultaneously rather
  than serially. For Ch02: document `max-parallel` as the throughput tuning knob
  for maintenance workflows with steady-state issue volume. Higher `max-parallel`
  increases throughput but also increases concurrent AI inference cost.

### Claim 10: The five-step iterative debug workflow for failed maintenance workflows is: check GitHub Actions UI → run `gh aw audit RUN_ID` → consult AI assistance (`copilot /agent agentic-workflows`) → modify config and compile → compare runs with `gh aw audit BASELINE_ID NEW_ID`

- **Evidence**: The "Iterative Debug Workflow" section documents five steps as the
  recommended debugging sequence. The "Quick Start" subsection identifies AI-assisted
  debugging as "the fastest path to a root cause."
- **Confidence**: emerging (first-party guidance; the five-step sequence is
  prescriptive but its relative effectiveness vs. other approaches is not measured)
- **Quote**: "The fastest path to a root cause is to hand the failing run URL to
  the Copilot CLI."
- **Our assessment**: The AI-assisted debugging entry point (`copilot /agent
  agentic-workflows` with a run URL) is novel to the corpus — no existing source
  note documents this specific debugging workflow. The comparative audit command
  (`gh aw audit BASELINE_ID CURRENT_ID`) is valuable for distinguishing regressions
  from pre-existing issues. The five-step structure (observe → diagnose → consult
  → modify → compare) is a generalizable debugging loop that applies beyond
  maintenance workflows. For Ch02: document the iterative debug workflow as the
  standard operating procedure for any failing gh-aw workflow. The comparative
  audit step is especially important for identifying which configuration change
  caused a regression.

### Claim 11: Six categories of common failure patterns exist for maintenance workflows: missing tool calls, authentication failures, integrity filtering blocks, safe-output validation failures, token budget exhaustion, and network blocks

- **Evidence**: The "Common Failure Patterns" section names all six categories:
  "missing tool calls, authentication failures, integrity filtering blocks,
  safe-output validation failures, token budget exhaustion, and network blocks —
  each with diagnostic indicators and remediation steps."
- **Confidence**: emerging (first-party taxonomy; the six categories are presented
  as a complete classification but are derived from practical experience rather
  than formal analysis)
- **Quote**: (no direct single-sentence verbatim quote; the six categories are
  listed as a named set with per-category diagnostic indicators)
- **Our assessment**: The six-category failure taxonomy is new to the corpus as
  a named, complete classification. Individual failure types appear across multiple
  corpus notes (e.g., integrity filtering blocks are covered in
  `docs-ghaw-integrity-reference.md` Claim 12, token budget exhaustion in
  `docs-ghaw-rate-limiting-controls.md` Claim 4, network blocks in
  `docs-ghaw-network-reference.md`), but this is the first source to enumerate
  all six as a coordinated diagnostic taxonomy specifically for maintenance
  workflows. For Ch02: document the six categories as the diagnostic checklist
  for troubleshooting any maintenance workflow failure. Pair each category with
  its diagnostic command: `gh aw logs --filtered-integrity` for Category 3;
  `gh aw audit RUN_ID` for Categories 1, 4, 5, and 6.

## Concrete Artifacts

### Repo Maintenance YAML Configurations (from source)

```yaml
# Reactions as trust signals for public repo maintenance:
features:
  integrity-reactions: true
tools:
  github:
    min-integrity: approved
```

```yaml
# Per-user rate limiting (v0.72.0+ field names):
user-rate-limit:
  max-runs-per-window: 5
  window: 60
```

```yaml
# Pre-activation association skips:
on:
  issue_comment:
    types: [created]
  skip-author-associations:
    issue_comment: [owner, member, collaborator]
```

```yaml
# Concurrency controls for parallel issue processing:
concurrency:
  max-parallel: 3
```

```yaml
# Repository access scoping for monorepo / multi-repo:
tools:
  github:
    allowed-repos: "myorg/*"
    min-integrity: approved
```

*Source: gh-aw examples/maintaining-repos, YAML configuration sections*

### Safe-Outputs Type Table (from source)

```
Safe-output             | Capability
----------------------- | -----------------------------------------------
label-issue             | Apply or remove labels on an issue
comment-issue           | Post a comment on an issue
comment-pull-request    | Post a comment on a pull request
create-pull-request     | Open a new pull request
merge-pull-request      | Merge a pull request (EXPERIMENTAL)
close-issue             | Close an issue
create-issue            | Open a new issue
assign-issue            | Assign an issue to a user or team
```

*Source: gh-aw examples/maintaining-repos, "Controlling Workflow Outputs with
Safe-Outputs" section*

### Integrity Filtering Levels (from source)

```
Level       | What it covers
----------- | -----------------------------------------------------------
merged      | PRs merged into default branch; commits reachable from main
approved    | Owners, members, collaborators; non-fork PRs on public repos;
            | recognized platform bots
unapproved  | Contributors with merged PRs; first-time contributors
none        | All content including users with no prior relationship
```

*Source: gh-aw examples/maintaining-repos, "Controlling Workflow Inputs with
Integrity Filtering" section*

### CLI Commands for Debugging (from source)

```bash
# Single-run diagnosis:
gh aw audit RUN_ID
gh aw audit RUN_ID --json
gh aw audit RUN_ID --parse

# Multi-run trend analysis:
gh aw logs my-workflow
gh aw logs my-workflow --format markdown --count 10

# Integrity filtering diagnostics:
gh aw logs --filtered-integrity

# Regression comparison between runs:
gh aw audit BASELINE_ID CURRENT_ID

# Recompile after configuration changes:
gh aw compile
```

*Source: gh-aw examples/maintaining-repos, "Debugging Failed Workflows" section*

### Five-Step Iterative Debug Workflow (from source)

```
1. Review workflow run summary in GitHub Actions UI
2. Execute `gh aw audit RUN_ID` for structured analysis
3. For complex issues: invoke `copilot /agent agentic-workflows`
   with the failing run URL for AI-assisted root cause analysis
4. Modify configuration → validate with `gh aw compile` → trigger new run
5. Compare runs using `gh aw audit BASELINE_ID NEW_ID`
```

*Source: gh-aw examples/maintaining-repos, "Debugging Failed Workflows —
Iterative Debug Workflow" section*

### Six Common Failure Pattern Categories (from source)

```
1. Missing tool calls         — agent has no access to required tools
2. Authentication failures    — token scope or credential configuration errors
3. Integrity filtering blocks — items removed before agent context assembly
4. Safe-output validation     — declared output type blocked or schema mismatch
   failures
5. Token budget exhaustion    — context window or token limit exceeded
6. Network blocks             — egress restriction or connectivity failures
```

*Source: gh-aw examples/maintaining-repos, "Common Failure Patterns" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-integrity-reference.md` Claim 1 ("Integrity filtering manages which
    GitHub content an agent can access by filtering based on trust rather than
    permissions"): this examples page applies the same mechanism with the same
    framing. Consistent on the pre-context-assembly timing and the trust-based
    filtering model.
  - `docs-ghaw-integrity-reference.md` Claim 3 (four integrity levels: merged,
    approved, unapproved, none): this examples page enumerates the same four levels
    in the same order with consistent definitions.
  - `docs-ghaw-integrity-reference.md` Claim 9 (reaction-based endorsement from
    v0.68.2+ via `features.integrity-reactions: true`): Claim 6 here corroborates
    the same feature in the context of repo maintenance workflows.
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (formal definition of Safe
    Outputs as a security-centric translation layer) and Claim 4 (P3: Configurable
    Constraint Enforcement): Claim 2 here provides the practical expression of these
    formal requirements — "declare what you need or it's blocked."
  - `docs-ghaw-rate-limiting-controls.md` Claim 3 (dual concurrency control:
    per-workflow and per-engine): Claim 9 here corroborates the dual enforcement
    model in the context of maintenance workflows.
  - `blog-ghaw-weekly-2026-05-11.md` Claim 6 (`rate-limit` → `user-rate-limit`;
    `max-runs` → `max-runs-per-window` breaking changes in v0.72.0, PR #31390):
    this examples page uses the v0.72.0+ field names, confirming the renaming is
    reflected in current platform documentation.

- **Extends**:
  - `docs-ghaw-integrity-reference.md`: that reference covers the complete
    `min-integrity` configuration surface (eleven fields, six-step algorithm,
    centralized variables, pre-agent proxy). This examples page adds the
    cost-optimization angle (Claim 5: filtering reduces token consumption) and
    places integrity filtering in the repo maintenance workflow context alongside
    safe-outputs and Repo Assist.
  - `docs-ghaw-rate-limiting-controls.md`: that reference documents eight
    anti-runaway mechanisms with the pre-v0.72.0 field names. This examples page
    shows current (v0.72.0+) field names in context and adds `skip-author-associations`
    as a pre-activation guard not covered in the rate-limiting reference.
  - `docs-ghaw-safe-outputs-specification.md`: the specification provides the
    formal normative architecture. This examples page provides the practitioner
    configuration checklist (eight named types) for maintenance workflows.
  - `docs-ghaw-central-repo-ops.md` Claims 2, 10 (conflict detection gate,
    `max` parameter for blast-radius control): the maintenance workflow patterns
    here complement the CentralRepoOps pattern with the public-repo safety
    controls (integrity filtering, user-rate-limit, skip-author-associations)
    that CentralRepoOps does not address.

- **Contradicts**: None identified.

  **Note on `user-rate-limit` vs `rate-limit`**: The `docs-ghaw-rate-limiting-controls.md`
  source note (extracted 2026-05-10) uses `rate-limit` and `max-runs` — the
  pre-v0.72.0 field names. This examples page uses `user-rate-limit` and
  `max-runs-per-window` — the v0.72.0+ names. This is not a contradiction:
  `blog-ghaw-weekly-2026-05-11.md` Claim 6 documents the v0.72.0 breaking change
  renaming these fields. The examples page uses the current API; the
  rate-limiting-controls source note uses the deprecated API. No contradiction
  issue filed; the guide should update its harness examples to use the current
  field names.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Repo Assist as triage layer for code-modifying agents** (Claim 1): No prior
    corpus source explicitly names the pattern of using Repo Assist as a
    prerequisite triage layer that gates downstream code-modifying agents. The
    Repo Assist workflow exists in `docs-ghaw-troubleshooting-debug-ghe.md`
    (mentioned as part of GHE setup) but the triage layer architectural role —
    "Repo Assist first, then code-modifying agents downstream" — is not stated
    elsewhere as a named pattern.
  - **`skip-author-associations` pre-activation guard** (Claim 8): No existing
    source note documents this configuration field. It is the pre-activation
    complement to integrity filtering's in-context filtering — it prevents run
    activation entirely based on trigger author association, before any agent
    infrastructure starts.
  - **Integrity filtering as cost optimization** (Claim 5): The dual security +
    cost framing is new. All existing integrity filtering corpus coverage treats
    it as a security mechanism. This page is the first to explicitly state the
    token consumption reduction benefit.
  - **AI-assisted debugging via `copilot /agent agentic-workflows`** (Claim 10):
    The specific debugging workflow using Copilot CLI as the first diagnostic
    tool for failing runs is not documented in any existing source note.
  - **Six-category failure pattern taxonomy** (Claim 11): While individual failure
    types appear across multiple corpus notes, this is the first source to present
    all six as a coordinated named taxonomy for maintenance workflow failures.
  - **v0.72.0+ field names in context** (Claim 7): This examples page is the
    corpus's first concrete demonstration of `user-rate-limit` and `max-runs-per-window`
    used in a workflow configuration, consistent with the v0.72.0 renaming
    documented in `blog-ghaw-weekly-2026-05-11.md` Claim 6.
  - **Integration pattern: safe-outputs + integrity filtering + Repo Assist**:
    No prior source shows all three mechanisms combined as a coherent defense-in-depth
    approach specifically for public repository maintenance. The `docs-ghaw-safe-outputs-specification.md`,
    `docs-ghaw-integrity-reference.md`, and `docs-ghaw-rate-limiting-controls.md`
    notes each cover one mechanism; this page is the first to show them integrated.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add Repo Assist as triage layer as the recommended public-repo entry point**
  (Claim 1): The guide should document the triage-layer pattern explicitly: deploy
  Repo Assist first, configure downstream code-modifying agents as consumers of
  its routing decisions. Frame this as the safety and cost model for public
  repository automation — Repo Assist absorbs volume, code-modifying agents operate
  on pre-classified, routed work.

- **Add `skip-author-associations` as the zero-cost pre-activation scaling
  mechanism** (Claim 8): Document the field with its YAML placement (`on:` block)
  and purpose: skip workflow activation entirely for specified author associations,
  reducing AI infrastructure activation costs for triggers that don't require
  agent processing.

- **Update rate-limiting field names to v0.72.0+ conventions** (Claim 7):
  All harness template examples should use `user-rate-limit` / `max-runs-per-window`
  rather than the deprecated `rate-limit` / `max-runs`. The `docs-ghaw-rate-limiting-controls.md`
  source note uses pre-v0.72.0 names; these should be updated in guide examples.

- **Document the five-step iterative debug workflow as standard operating procedure**
  (Claim 10): Add the `check UI → gh aw audit → copilot /agent agentic-workflows →
  modify+compile → comparative audit` loop as the canonical debugging sequence for
  failing gh-aw workflows.

- **Document the six failure pattern categories as a diagnostic checklist** (Claim 11):
  Present all six categories with their corresponding diagnostic commands, giving
  practitioners a structured triage approach for any maintenance workflow failure.

### Chapter 03: Safety and Verification

- **Add integrity filtering as the input layer in the defense-in-depth model**
  (Claim 4): Current corpus describes safe-outputs as the output enforcement layer.
  Add integrity filtering as the paired input restriction layer: together they form
  the complete "what the agent sees" + "what the agent can do" boundary for public
  repository workflows.

- **Frame dual-purpose benefit of integrity filtering: security + cost** (Claim 5):
  When recommending integrity filtering adoption, note both benefits: prevents
  prompt injection via untrusted content (security) and reduces context window size
  (cost). The dual framing is more persuasive for organizations evaluating adoption.

- **Add Repo Assist triage layer as the architectural response to untrusted input**
  (Claim 1): For public repositories, the defense against high-volume untrusted
  contributions is a two-layer architecture: Repo Assist handles triage and routing;
  code-modifying agents operate only on work that passes triage.

## Extraction Notes

1. **WebFetch returns AI-model-processed content**: The `examples/maintaining-repos`
   page is an Astro/Starlight SPA. Multiple targeted WebFetch requests were made
   with different prompts to triangulate verbatim wording for the quoted passages.
   Introductory paragraph quotes (Claims 1, 2, 4) and the token consumption quote
   (Claim 5) were returned in quoted form by the WebFetch model. The debugging
   quick-start quote (Claim 10) was similarly returned in quoted form. While these
   appear plausibly verbatim, minor wording variations from the source page are
   possible. The Assayer should spot-check these quotes against the source URL.

2. **v0.72.0+ field naming**: This examples page uses `user-rate-limit` and
   `max-runs-per-window` — the post-v0.72.0 field names documented in
   `blog-ghaw-weekly-2026-05-11.md` Claim 6. The `docs-ghaw-rate-limiting-controls.md`
   note uses the pre-v0.72.0 names. The examples page's naming is treated as
   current for extraction purposes.

3. **Related pages not followed**: The page links to eight reference documents
   (safe outputs, integrity filtering, rate limiting, cost management, audit commands,
   debugging, network configuration, GitHub tools). All are already covered by
   dedicated source notes in the corpus. No sub-pages were followed.

4. **`merge-pull-request` is flagged "experimental"**: The source explicitly marks
   this output type as experimental. Claims about maintenance workflow capabilities
   that require PR merging should note this status until the type reaches stable.

5. **Issue #437 (guides/maintaining-repos) not yet mined**: The Prospector's triage
   comment notes issue #437 as the guides counterpart to this examples page, covering
   the same conceptual patterns in narrative form. That page has not been mined as of
   this extraction. The guide impact recommendations here may overlap with what #437
   will contribute; the guide synthesis should consider both source notes together.

6. **No contradictions filed**: Reviewed all existing gh-aw source notes. The
   `user-rate-limit` / `rate-limit` naming difference is an API evolution (v0.72.0
   breaking change), not a substantive contradiction. No claim in this source
   materially opposes any existing source note on behavior, design, or recommendations.
   No contradiction issue required.
