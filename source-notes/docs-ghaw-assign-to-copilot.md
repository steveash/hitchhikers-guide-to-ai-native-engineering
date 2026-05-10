---
source_url: https://github.github.com/gh-aw/reference/assign-to-copilot
source_type: docs
title: "GitHub Agentic Workflows: Assign to Copilot Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#357"
---

# GitHub Agentic Workflows: Assign to Copilot Reference

> The authoritative reference for the `assign-to-agent` safe output — documents how to
> programmatically assign the Copilot coding agent to existing issues or pull requests,
> including the full parameter schema (target resolution modes, cross-repository PR creation,
> model selection), the fine-grained PAT authentication requirement, and the two-pattern
> design that separates new-issue assignment (`assignees: copilot` in `create-issue`)
> from existing-issue assignment (`assign-to-agent`).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/assign-to-copilot` page —
  in the "Reference" section, distinct from the `patterns/` practitioner pages and
  the `introduction/` conceptual pages. Reference pages document platform behavior
  precisely; this one specifies the complete `assign-to-agent` safe output schema.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team behind Peli de Halleux's "Agent Factory"
  blog series and the `gh aw` CLI). Reference-section claims about parameter defaults,
  authentication requirements, and target resolution behavior are settled platform facts,
  not practitioner recommendations.
- **Scope**: The complete `assign-to-agent` safe output schema — all configuration
  parameters (name, model, custom-agent, custom-instructions, allowed, max, target,
  target-repo, pull-request-repo, allowed-pull-request-repos, base-branch, github-token),
  target resolution semantics ("triggering" / "*" / numeric), cross-repository PR creation
  support, and authentication requirements (fine-grained PAT). Does NOT cover: the
  general Safe Outputs architecture and security invariants (see `docs-ghaw-safe-outputs-
  specification.md`), the IssueOps trigger pattern (see `docs-ghaw-issueops.md`), model
  selection governance at the organization level (see `docs-github-copilot-agent-model-
  selection.md`), or the related `create-issue` safe output's `assignees: copilot` field.

## Extracted Claims

### Claim 1: `assign-to-agent` is the programmatic safe output for assigning the Copilot coding agent to existing issues or pull requests

- **Evidence**: The page opens with this direct statement and provides the full parameter
  schema for the safe output. The mechanism routes through the Safe Outputs MCP Gateway
  infrastructure rather than direct GitHub API writes.
- **Confidence**: settled (first-party reference documentation; this is the normative
  definition of the `assign-to-agent` operation type)
- **Quote**: "This page describes how to programmatically assign the GitHub Copilot coding
  agent to issues or pull requests using the `assign-to-agent` safe output."
- **Our assessment**: `assign-to-agent` is the assignment mechanism for workflows that need
  to assign Copilot to issues/PRs that already exist — created by a prior workflow step, by
  a human, or by an upstream event. It follows the same Safe Outputs privilege-separation
  model as all other write operations on the gh-aw platform: the AI job declares the
  assignment intent; the Safe Output Processor executes it with the write credentials the
  AI job does not hold. For Ch04 (Agent Patterns / Orchestration): document `assign-to-agent`
  as the mechanism for closing the loop from issue discovery/creation to agent dispatch —
  a workflow can create an issue and immediately route it to Copilot in two safe-output
  steps.

### Claim 2: Two distinct patterns handle Copilot assignment depending on whether the issue is new or pre-existing — `assignees: copilot` in `create-issue` for new issues, `assign-to-agent` for existing ones

- **Evidence**: The page explicitly separates the two patterns. For new issues that need
  immediate assignment, the recommendation is to use `assignees: copilot` in `create-issue`
  configuration rather than `assign-to-agent`. The `assign-to-agent` safe output handles
  the case where the issue already exists in GitHub.
- **Confidence**: settled (first-party; the two-pattern distinction is stated directly
  as guidance for when to use each)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This two-pattern design is architecturally clean: the `create-issue`
  safe output handles new-issue creation with optional immediate Copilot assignment as a
  single atomic operation; `assign-to-agent` handles the separate concern of routing
  pre-existing issues. Practitioners should choose based on whether the issue already
  exists at workflow execution time. The IssueOps pattern (`docs-ghaw-issueops.md` Claim 7)
  documents `assignees: copilot` in the sub-issue creation context; this reference page
  documents the other side of the assignment surface. For Ch04: present both patterns
  in the same section — "Copilot assignment" has two forms; the choice depends on whether
  the target issue pre-exists.

### Claim 3: The `target` parameter controls assignment destination with three resolution modes: event-bound ("triggering"), agent-output-bound ("*"), or fixed (numeric issue/PR number)

- **Evidence**: The page documents three distinct behaviors for the `target` field:
  `"triggering"` automatically resolves to the issue or PR from the workflow trigger
  context; `"*"` requires the agent to explicitly output `issue_number` or `pull_number`
  values; a numeric value always targets that specific issue or PR number.
- **Confidence**: settled (first-party reference documentation; the three-mode semantics
  are explicitly defined)
- **Quote**: "The `target` parameter determines which issue or PR to assign the agent to"
- **Our assessment**: The three target modes serve different workflow architectures.
  `"triggering"` is the IssueOps-idiomatic choice (mirrors `target: "triggering"` in
  `add-comment`, documented in `docs-ghaw-issueops.md` Claim 2) — the workflow responds to
  whatever triggered it. `"*"` enables dynamic dispatch: the AI agent analyzes context
  and determines which issue to assign Copilot to, outputting the number for the platform
  to resolve. The numeric mode is for fixed-target workflows (e.g., a DailyOps workflow
  that always routes to the same tracking issue). For Ch04: `target: "*"` is the pattern
  for AI-driven issue routing — the agent decides WHERE to dispatch, not just whether to
  dispatch. This is the mechanism underlying Issue Monster-style workflows
  (`blog-ghaw-issue-pr-mgmt.md` Claim 2).

### Claim 4: The `model` parameter selects the AI model for the assigned Copilot task, defaulting to "auto"

- **Evidence**: The `model` parameter is listed with a default of `"auto"`, indicating the
  platform selects the model automatically when no explicit model is specified. The parameter
  accepts model identifiers consistent with those documented in GitHub Copilot model
  selection (Claude Sonnet/Opus variants, Codex variants).
- **Confidence**: settled (parameter name and default stated in first-party reference
  documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `model` parameter extends model selection to the assignment level —
  the workflow author can control which AI model handles the assigned task, not just which
  agent receives the assignment. The `"auto"` default defers to platform heuristics. This
  connects directly to `docs-github-copilot-agent-model-selection.md` Claim 1 (model
  selection as a per-task control), but operates at the safe-output level rather than the
  github.com task-initiation UI level. For Ch04: note that `assign-to-agent` exposes model
  selection as a workflow configuration parameter — teams can specify model tier in workflow
  YAML rather than relying on UI-level selection or platform defaults.

### Claim 5: The `max` parameter defaults to 1, restricting a single workflow run to at most one Copilot assignment

- **Evidence**: The `max` parameter is listed with a default of 1. Like all Safe Outputs
  `max` settings, this follows the all-or-nothing semantics documented in
  `docs-ghaw-safe-outputs-specification.md` Claim 6: exceeding `max` rejects all
  operations of that type, not just the excess.
- **Confidence**: settled (parameter default stated in first-party reference documentation;
  max semantics are normative per the Safe Outputs spec)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A `max: 1` default is appropriate for most assignment workflows —
  assigning Copilot to multiple issues in a single run risks saturating the agent queue
  and is typically not the intent. Teams implementing bulk-assignment workflows (e.g.,
  routing a backlog of issues to Copilot in one pass) must explicitly raise `max`. The
  all-or-nothing semantics mean setting `max: 5` but having the agent attempt 6 assignments
  results in zero assignments — practitioners must calibrate `max` carefully for bulk
  operations. For Ch04: warn that `max` on `assign-to-agent` is especially consequential
  because each assignment potentially launches an autonomous Copilot task. Unbounded or
  overly generous `max` values could saturate the Copilot agent queue.

### Claim 6: Cross-repository PR creation is supported via `pull-request-repo`, enabling centralized issue tracking with distributed codebases

- **Evidence**: The `pull-request-repo` parameter allows specifying a different repository
  for PR creation than the one where the issue resides. The `target-repo` parameter
  specifies the repository for cross-repository issue lookup, while `allowed-pull-request-
  repos` restricts which repositories are valid PR targets.
- **Confidence**: settled (first-party reference documentation; parameters are explicitly
  listed)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Cross-repository assignment is the `assign-to-agent` counterpart to
  the multi-repo coordination patterns in `docs-ghaw-multi-repo-ops.md`. A common
  architecture: a central issue-tracking repository captures work items; `assign-to-agent`
  routes those issues to Copilot with `pull-request-repo` pointing to the target service
  repository where the code lives. The resulting PR appears in the service repo while the
  tracking issue lives in the ops repo. The `allowed-pull-request-repos` allowlist
  constrains cross-repo writes to pre-approved targets — consistent with the Safe Outputs
  cross-repository containment invariant SP6 (`docs-ghaw-safe-outputs-specification.md`
  Claim 5). For Ch04: this parameter combination (target-repo + pull-request-repo) is the
  concrete mechanism for centralized-issue / distributed-code architectural patterns.

### Claim 7: Authentication requires a fine-grained Personal Access Token (PAT); the default GITHUB_TOKEN lacks the necessary permissions, and GitHub App tokens are explicitly not supported

- **Evidence**: The page states directly that the default GITHUB_TOKEN lacks necessary
  permissions and that this safe output requires a fine-grained PAT. The page notes that
  GitHub App tokens are not supported, with the system falling back to the explicit
  `github-token` parameter or the `GH_AW_AGENT_TOKEN` magic secret.
- **Confidence**: settled (stated directly as an authentication requirement in first-party
  reference documentation)
- **Quote**: "This safe output requires a fine-grained PAT to authenticate the agent
  assignment operation. The default `GITHUB_TOKEN` lacks the necessary permissions."
- **Our assessment**: This is the most operationally significant constraint in the reference.
  Unlike most GitHub Actions workflows that rely on the automatic `GITHUB_TOKEN`, `assign-
  to-agent` requires a separately provisioned fine-grained PAT with repository-scope
  permissions (Actions, Contents, Issues, and Pull Requests at Write level). Teams adopting
  this safe output must plan for PAT lifecycle management: creation, rotation, secure
  storage in GitHub Secrets, and scope governance. The GitHub App token exclusion is notable
  — organizations that standardize on GitHub App tokens for workflow authentication must
  make an exception here and provision a PAT. For Ch04: document the PAT requirement as
  a deployment prerequisite for any workflow using `assign-to-agent`. For Ch05 (Team
  Adoption): PAT provisioning is an administrative step that may require coordination with
  GitHub organization admins, adding lead time to initial deployment.

### Claim 8: `GH_AW_AGENT_TOKEN` is a platform-recognized magic secret that the system uses as the authentication fallback when no explicit `github-token` is configured

- **Evidence**: The page documents that the system falls back to the `GH_AW_AGENT_TOKEN`
  secret when no explicit `github-token` is provided in the safe-output configuration.
  This allows teams to configure a single organization-level or repository-level secret
  once, rather than specifying `github-token` in every workflow that uses `assign-to-agent`.
- **Confidence**: emerging (sourced from WebFetch summary; exact parameter wording
  not directly quotable — the term "magic secret" is from the WebFetch summary, not
  a verbatim page quote)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `GH_AW_AGENT_TOKEN` convention is a platform-level pattern for
  centralized PAT management — a single secret provisioned once supports all `assign-to-agent`
  usages across an organization's workflows. This reduces the per-workflow secret management
  burden while still providing a path for per-workflow override via explicit `github-token`.
  For Ch04: recommend setting `GH_AW_AGENT_TOKEN` at the repository or organization level
  as the standard deployment pattern; reserve per-workflow `github-token` for cases where
  the assignment target requires different permissions. The naming convention (`GH_AW_*`)
  suggests this may be used across multiple gh-aw safe outputs that require elevated
  permissions beyond `GITHUB_TOKEN`.

### Claim 9: The `allowed` parameter restricts assignment to a specific list of agents, while `custom-agent` and `custom-instructions` enable non-default agent configurations

- **Evidence**: The parameter list documents: `allowed` as a list restricting which agents
  can be assigned (with the default agent being "copilot"); `custom-agent` as an optional
  custom agent identifier; `custom-instructions` as optional default instructions passed to
  the assigned agent.
- **Confidence**: emerging (parameter names and descriptions from WebFetch summary; exact
  semantic definitions not directly quotable)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `allowed` parameter provides a categorical guard: a workflow can
  declare that only specific agents (e.g., just "copilot", not custom agents) can be
  assigned, preventing prompt-injection or misconfiguration from routing issues to unexpected
  agents. The `custom-agent` and `custom-instructions` parameters reveal that the safe output
  is not hardwired to the built-in Copilot agent — it can dispatch to custom agents with
  bespoke instructions. `custom-instructions` is particularly notable: it provides a per-
  assignment default system prompt, allowing different workflows to assign the same agent
  with different behavioral contexts. For Ch04: `custom-instructions` is the assignment-time
  complement to repository-level CLAUDE.md or agent harness configuration — it provides a
  per-dispatch instruction layer without requiring the agent to read from repository files.

### Claim 10: The `base-branch` parameter allows specifying the target branch for the PR created by the assigned Copilot agent

- **Evidence**: The `base-branch` parameter is listed as an optional configuration for
  specifying which branch the Copilot-created PR should target.
- **Confidence**: settled (parameter listed in first-party reference documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `base-branch` enables multi-branch workflows where Copilot-generated
  PRs should target a release branch, a feature branch, or any non-default branch. This is
  important for release engineering workflows (consistent with `blog-gh-aw-operations-release-
  workflows.md`) where work for a specific release must land on a release branch rather than
  `main`. Omitting `base-branch` defaults to the repository's default branch. For Ch04:
  document `base-branch` as the assignment-level mechanism for directing Copilot's output
  to non-default branches — relevant for any workflow that manages parallel release lines.

## Concrete Artifacts

### `assign-to-agent` Safe Output — Complete Parameter Reference

```yaml
# assign-to-agent safe output — full parameter schema
# Source: github.github.com/gh-aw/reference/assign-to-copilot

safe-outputs:
  assign-to-agent:
    name: "copilot"              # Agent identifier (default: "copilot")
    model: "auto"                # AI model for the assigned task (default: "auto")
    custom-agent: null           # Optional: custom agent ID (overrides name)
    custom-instructions: null    # Optional: default instructions for the agent
    allowed: []                  # Optional: restrict to specific agents
    max: 1                       # Max assignments per run (default: 1)
    target: "triggering"         # "triggering" | "*" | <issue-number>
    target-repo: null            # Cross-repo: where the issue lives
    pull-request-repo: null      # Cross-repo: where the PR should be created
    allowed-pull-request-repos: []  # Additional allowed PR repositories
    base-branch: null            # Target branch for Copilot's PR (default: repo default)
    github-token: null           # Fine-grained PAT (falls back to GH_AW_AGENT_TOKEN)
```

*Parameter names, defaults, and types reconstructed from WebFetch summaries of the
reference page. Verify against source URL before production use, as defaults may change.*

### Target Resolution Decision Guide

```
target parameter value  | Resolution behavior
------------------------|------------------------------------------
"triggering"            | Resolves from workflow trigger context
                        | (the issue/PR that activated the workflow)
                        | Idiomatic for IssueOps and ChatOps workflows
                        |
"*"                     | Agent must output explicit issue_number or
                        | pull_number values in its response
                        | Used for AI-driven routing (agent picks target)
                        |
<numeric-value>         | Always targets that specific issue or PR number
                        | Used for fixed-target workflows (e.g., DailyOps
                        | that routes to the same tracking issue)
```

### Authentication Requirements

```
assign-to-agent authentication:

DEFAULT GITHUB_TOKEN:  ❌ Insufficient — lacks required write permissions
GITHUB APP TOKEN:      ❌ Not supported
FINE-GRAINED PAT:      ✅ Required (must have Write access to Actions, Contents,
                           Issues, and Pull Requests for target repository)

Token lookup order:
  1. Explicit github-token parameter in the safe-output configuration
  2. GH_AW_AGENT_TOKEN secret (repository or organization level)

Recommended deployment pattern:
  → Set GH_AW_AGENT_TOKEN at repository or org level (once)
  → Override with explicit github-token only when target requires different scope
```

### Two-Pattern Assignment Summary

```
Copilot assignment — two safe-output patterns:

Pattern A: Create issue + immediately assign (new issues)
  Use: create-issue safe output with assignees: copilot
  When: The issue does not yet exist; creation and assignment are one atomic step

Pattern B: Assign to existing issue/PR (pre-existing)
  Use: assign-to-agent safe output
  When: The issue already exists (created by human, prior workflow, or upstream event)

Cross-reference:
  Pattern A is documented in docs-ghaw-issueops.md (Claim 7: sub-issue + assignees: copilot)
  Pattern B is this reference page (assign-to-agent)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-issueops.md` Claim 7 (`assignees: copilot` for parallel execution of
    sub-issues): Both sources document Copilot assignment patterns; they address
    complementary cases. IssueOps Claim 7 covers assignment at creation time in sub-issue
    hierarchies; this reference page covers assignment to pre-existing issues via a dedicated
    safe output. The distinction — new-issue vs. existing-issue — is made explicit in this
    reference page (Claim 2 above).
  - `blog-ghaw-issue-pr-mgmt.md` Claim 2 (Issue Monster as serialized Copilot dispatcher):
    Issue Monster is the production workflow that assigns issues to Copilot one at a time.
    This reference page documents the `assign-to-agent` safe output that Issue Monster likely
    uses as its write mechanism. The `max: 1` default (Claim 5) matches Issue Monster's
    deliberate one-at-a-time serialization design.
  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (AR1 — Agents MUST execute without
    write permissions): The fine-grained PAT authentication requirement (Claim 7) is the
    implementation of AR1 for the assignment use case — the AI job cannot call the Copilot
    assignment API directly because it holds no write credentials. The PAT lives with the
    Safe Output Processor, not the AI job. The spec's SP6 (Cross-Repository Containment
    invariant) maps to the `allowed-pull-request-repos` parameter (Claim 6) that restricts
    cross-repo PR targets to an allowlist.
  - `docs-github-copilot-agent-model-selection.md` Claim 1 (GitHub now exposes per-task
    model selection): The `model` parameter in `assign-to-agent` (Claim 4) is the workflow-
    YAML-level expression of the model selection capability documented in that changelog.
    The changelog describes UI-level model selection when kicking off tasks; this reference
    page documents the same control available as a YAML parameter in automated workflows.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md` (Safe Outputs MCP Gateway Specification):
    That note documents the overall Safe Outputs architecture including 30+ operation types.
    `assign-to-agent` is one of those types; this reference page provides the type-specific
    schema (parameters, authentication requirements, target semantics) that the spec
    deliberately does not cover per its scope statement.
  - `docs-ghaw-multi-repo-ops.md` (MultiRepoOps Pattern): That note covers cross-repository
    workflow dispatch. The `target-repo` + `pull-request-repo` + `allowed-pull-request-repos`
    parameter combination in `assign-to-agent` (Claim 6) provides cross-repository support
    at the safe-output level — assignment can span repositories in the same way multi-repo
    dispatch spans repositories for workflow execution.
  - `docs-github-copilot-agent-model-selection.md` Claims 5–6 (two-layer governance model —
    org admin enables policy; repo owner enables agent): The PAT requirement (Claim 7) adds
    a third credential layer to that model — beyond org policy enablement and repo settings
    enablement, teams must also provision and manage a fine-grained PAT with the correct
    permissions. Together, the three layers define the full prerequisites for Copilot
    assignment in a workflow.

- **Contradicts**: None. No existing source note makes claims that materially oppose any
  parameter definition, authentication requirement, or target resolution semantic documented
  here. The IssueOps note's `assignees: copilot` and this note's `assign-to-agent` are
  explicitly complementary patterns for different scenarios, not conflicting claims.
  No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **`assign-to-agent` as a distinct named safe output type** (Claim 1): No prior corpus
    note documents `assign-to-agent` as a specific operation type with its own parameter
    schema. Prior notes reference Copilot assignment via `assignees: copilot` in issue
    creation or the Issue Monster dispatch pattern, but none documents the dedicated
    assignment-only safe output.
  - **Two-pattern split for Copilot assignment** (Claim 2): The explicit separation between
    new-issue assignment (`assignees: copilot` in `create-issue`) and existing-issue
    assignment (`assign-to-agent`) is not documented elsewhere in the corpus. Practitioners
    choosing between these two patterns had no guidance; this reference page provides it.
  - **`target: "*"` with agent-output resolution** (Claim 3): No prior corpus note
    documents the `"*"` target mode requiring the agent to output `issue_number` or
    `pull_number`. This is the mechanism for AI-driven issue routing — the agent decides
    the target — and is entirely new to the corpus.
  - **`custom-instructions` as per-assignment agent context** (Claim 9): The ability to
    pass default instructions to Copilot at assignment time, rather than relying on
    repository-level configuration, is not documented elsewhere. This is a per-dispatch
    instruction layer above CLAUDE.md or harness-level configuration.
  - **`GH_AW_AGENT_TOKEN` magic secret** (Claim 8): The platform-level fallback secret
    convention is not documented in any prior corpus note. It suggests a broader gh-aw
    pattern for centralized elevated-permission token management across safe outputs that
    require permissions beyond `GITHUB_TOKEN`.
  - **GitHub App token exclusion** (Claim 7): No prior corpus note documents that GitHub
    App tokens are specifically excluded from a gh-aw safe output's authentication options.
    For organizations that standardize on App token authentication for workflow automation,
    this is a deployment-blocking constraint requiring an explicit PAT exception.

## Guide Impact

### Chapter 04: Agent Patterns / Orchestration

- **Add `assign-to-agent` to the Copilot assignment pattern taxonomy** (Claims 1–2):
  The guide should document both assignment patterns side by side. When to use each:
  (a) `assignees: copilot` in `create-issue` — when creating a new issue and immediately
  routing it to Copilot in one atomic step; (b) `assign-to-agent` safe output — when the
  target issue already exists and assignment is a separate workflow step. The two-pattern
  split is a practitioner decision point that currently has no explicit guidance in the
  corpus.

- **Document `target: "*"` as the AI-driven routing mechanism** (Claim 3): When a workflow
  needs to let the agent decide which issue to dispatch to Copilot, `target: "*"` with agent-
  output `issue_number`/`pull_number` is the mechanism. This is the "dynamic dispatch" pattern
  — the equivalent of a human triager choosing which issues to hand off, but automated.
  Document it alongside the `"triggering"` (event-bound) and numeric (fixed-target) modes
  as a three-option target taxonomy.

- **Document `custom-instructions` as the per-dispatch context layer** (Claim 9): Position
  `custom-instructions` in the configuration hierarchy: below repository CLAUDE.md (which
  sets persistent behavioral context) and above per-issue comments (which provide task-
  specific context). A workflow can use `custom-instructions` to provide role-specific
  framing (e.g., "This is a security fix. Prioritize correctness over refactoring.") for
  different issue categories, without modifying repository-level configuration.

- **Warn about `max` semantics for assignment workflows** (Claim 5): The all-or-nothing
  `max` behavior (`docs-ghaw-safe-outputs-specification.md` Claim 6) is especially
  consequential for `assign-to-agent` because each assignment potentially launches an
  autonomous agent task. Setting `max` too low causes complete assignment failure; setting
  it too high risks saturating the Copilot agent queue. Recommend: start with `max: 1`
  (the default); increase only for explicitly designed bulk-assignment workflows with
  queue-depth monitoring in place.

### Chapter 02: Harness Engineering

- **Document the PAT authentication requirement as a deployment prerequisite** (Claim 7):
  Any workflow that uses `assign-to-agent` requires a fine-grained PAT with Write access
  to Actions, Contents, Issues, and Pull Requests. This is a non-trivial deployment
  dependency: the PAT must be created, scoped, stored as a secret, and rotated. Recommend
  the `GH_AW_AGENT_TOKEN` convention as the standard pattern (set once at repository or
  org level; falls back automatically). Document this in the harness configuration checklist
  so teams don't discover the GITHUB_TOKEN limitation at deployment time.

- **Add cross-repository assignment to the multi-repo pattern coverage** (Claim 6):
  The `target-repo` + `pull-request-repo` combination enables issue-in-one-repo,
  PR-in-another-repo workflows. This is the assignment-level expression of the cross-
  repository pattern. The `allowed-pull-request-repos` allowlist provides the SP6-compliant
  containment for cross-repo writes. Document this alongside `docs-ghaw-multi-repo-ops.md`
  patterns.

### Chapter 05: Team Adoption / Enterprise Governance

- **Flag PAT provisioning as an admin coordination dependency** (Claim 7): Unlike most
  GitHub Actions workflows that use the automatic `GITHUB_TOKEN`, `assign-to-agent` requires
  a separately provisioned PAT with specific write permissions. In organizations where PAT
  creation requires admin approval or follows a provisioning process, this adds lead time
  to initial `assign-to-agent` deployment. Teams should surface this dependency early in
  the adoption planning process, not discover it when a workflow fails with a permissions
  error.

## Extraction Notes

1. **Reference page, not conceptual or patterns page**: This is a `reference/` section page
   documenting the `assign-to-agent` safe output schema precisely. It does not include
   implementation rationale, worked examples from production, or comparison with alternative
   approaches. The guide impact section above reconstructs those implications from the
   parameter semantics.

2. **Verbatim quotes limited by WebFetch rendering**: The page is an Astro/Starlight SPA.
   Two WebFetch requests were made. The third request asking for full verbatim reproduction
   was declined by the WebFetch AI layer on copyright grounds. Three verbatim quotes were
   obtained from the first two fetches:
   - The overview sentence (Claim 1 quote)
   - The target parameter description (Claim 3 quote)
   - The PAT authentication requirement (Claim 7 quote)
   All other claims are marked `(no direct quote; see paraphrase in Our assessment)` per
   MINER.md §2a. The parameter names, defaults, and semantics are consistent across two
   independent fetch requests and are treated as settled platform facts.

3. **Parameter defaults from summary**: The concrete parameter defaults (`max: 1`,
   `model: "auto"`, `name: "copilot"`) were reported consistently in WebFetch summaries
   across two independent requests. They are treated as settled but should be verified
   against the live source URL before citing in the guide, as defaults may change with
   platform updates.

4. **No publication date**: The reference page does not carry an explicit publication date.
   `date_published` is left null. Content is consistent with gh-aw platform state as of
   2026-05-10.

5. **No contradictions filed**: Reviewed all existing source notes in the corpus. No
   existing note makes claims that materially oppose the `assign-to-agent` parameter
   schema, authentication requirements, or target semantics. The IssueOps note's
   `assignees: copilot` and this note's `assign-to-agent` are explicitly complementary
   patterns documented as such in this reference page.

6. **Related reference pages not followed**: The source page likely links to the `create-
   issue` safe output reference (documenting `assignees: copilot`) and potentially to the
   broader safe outputs catalog. These were not followed — the scope of this extraction
   is the `assign-to-agent` type specifically. The `create-issue` reference would warrant
   a separate source note if the guide needs deeper coverage of new-issue assignment.
