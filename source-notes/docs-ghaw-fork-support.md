---
source_url: https://github.github.com/gh-aw/reference/fork-support
source_type: docs
title: "GitHub Agentic Workflows: Fork Support Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#394"
---

# GitHub Agentic Workflows: Fork Support Reference

> The authoritative reference for gh-aw's fork behavior — distinguishes two
> separate fork scenarios (execution inside a fork vs. inbound PRs from a fork),
> documents the deny-by-default safety model for both, and specifies the `forks:`
> configuration field for selectively permitting PR-triggered execution from
> trusted fork patterns.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/fork-support` page
  — in the "Reference" section, not the conceptual `introduction/` pages or
  practitioner `guides/`. Reference pages document platform behavior authoritatively;
  this one specifies the complete fork support model.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Configuration field names, default behaviors, and security rationales are settled
  platform facts.
- **Scope**: Fork behavior only — how gh-aw handles two distinct fork scenarios:
  (1) workflows running inside forked repositories (always skipped via compile-time
  condition); (2) inbound pull requests from forked repositories (blocked by default,
  configurable via `forks:`). Does NOT cover: the general permissions model (see
  `docs-ghaw-permissions-reference.md`), the compilation pipeline in detail (see
  `docs-ghaw-compilation-process.md`), or the Safe Outputs mechanism (see
  `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: GHAW explicitly distinguishes two separate fork scenarios with different operational models — execution inside a forked repo (always skipped) versus inbound PRs from a fork (deny-by-default, configurable)

- **Evidence**: The page opens by establishing this as a two-scenario taxonomy:
  "GitHub Agentic Workflows distinguishes between two fork situations with different
  operational modes: workflows running within forked repositories versus inbound
  pull requests originating from forks." The two scenarios receive separate
  documentation sections with separate policies and separate configuration mechanisms.
- **Confidence**: settled (first-party documentation; the two-scenario model is
  the organizing principle of the entire page)
- **Quote**: "GitHub Agentic Workflows distinguishes between two fork situations
  with different operational modes: workflows running within forked repositories
  versus inbound pull requests originating from forks."
- **Our assessment**: The two-scenario framing is the central insight of this page.
  Many practitioners conflate "my workflow runs on a fork" with "someone opened a
  PR from a fork" — these are entirely different situations with different risk
  profiles and different configuration levers. Execution inside a fork is an all-or-
  nothing compile-time bypass; PR-from-fork access is configurable per-pattern at
  the trigger level. For Ch02 (Harness Engineering): present fork handling as a
  two-axis decision matrix, not a single "fork policy" toggle.

### Claim 2: Agentic workflows do not execute inside forked repositories — all jobs are automatically skipped via a compile-time condition

- **Evidence**: Stated unambiguously: "Agentic workflows intentionally do not
  execute in forked repositories. The system automatically skips all jobs using a
  compile-time condition." The specific jobs affected are enumerated: agent jobs,
  self-update tasks, and maintenance tasks.
- **Confidence**: settled (first-party documentation; the compile-time condition is
  a platform-enforced behavior, not a configuration option)
- **Quote**: "Agentic workflows intentionally do not execute in forked repositories.
  The system automatically skips all jobs using a compile-time condition."
- **Our assessment**: The word "intentionally" signals this is a deliberate design
  choice, not an implementation limitation. The compile-time condition means this
  protection is baked into the generated `.lock.yml` — it cannot be accidentally
  overridden at runtime. This is an application of the compilation-time validation
  principle from `docs-ghaw-how-they-work.md` Claim 3 (Layer 1: compile-time
  validation as the first security layer). For Ch02: deploy operators should
  understand that gh-aw workflows require no special fork configuration to remain
  safe in fork scenarios — the skip is automatic and unconditional.

### Claim 3: The rationale for fork execution suppression is that forks lack both the necessary secrets and contextual information for secure, reliable agent operation

- **Evidence**: The page provides a direct rationale statement: "The rationale is
  straightforward: forks lack the necessary secrets and contextual information for
  agents to function securely and reliably." The specific consequences are
  enumerated: agent jobs are bypassed entirely, self-update and maintenance tasks
  don't run, and secrets from the upstream repository remain unavailable.
- **Confidence**: settled (first-party architectural rationale; the two specific
  failure modes — missing secrets, missing context — are named)
- **Quote**: "forks lack the necessary secrets and contextual information for agents
  to function securely and reliably."
- **Our assessment**: The dual-failure rationale (secrets AND context) is worth
  unpacking. The secrets problem is obvious: a fork doesn't inherit GITHUB_TOKEN
  or repository secrets from the upstream. The "contextual information" problem is
  subtler: a fork may not have the repository-specific configuration, GitHub Project
  boards, issue labels, or workflow state that the agent depends on to function
  correctly. Skipping on forks prevents both silent failures (agent runs but
  produces wrong output due to missing context) and security failures (agent runs
  with reduced capabilities but still exposes partial system state). For Ch03
  (Safety and Verification): this dual-failure rationale is a useful framing for
  any agentic deployment where the execution environment may be missing expected
  configuration — prefer failing closed (skip) over failing open (attempt and
  produce incorrect outputs).

### Claim 4: Practitioners who want to run agentic workflows in a forked repo can do so by configuring their own secrets on the fork — at which point GitHub Actions no longer classifies it as a fork

- **Evidence**: The page provides a workaround: "To run agentic workflows in your
  own repository, fork the upstream project and configure your own secrets. Once
  you own the repository directly, it's no longer classified as a fork from GitHub
  Actions' perspective."
- **Confidence**: settled (first-party documentation; describes a property of how
  GitHub Actions handles fork classification)
- **Quote**: "Once you own the repository directly, it's no longer classified as a
  fork from GitHub Actions' perspective."
- **Our assessment**: This workaround reveals that the fork skip is not about
  ownership topology but about the GitHub Actions runtime fork classification.
  A repository forked from another is classified as a fork only if GitHub Actions
  identifies it as such at trigger time. By configuring your own secrets and
  treating the repository as your primary workspace (not as a temporary fork for
  upstream contribution), you exit the fork classification. This matters for teams
  building on top of gh-aw starter templates: the recommended path is fork once
  to start, then configure secrets to move into the "owned repository" operational
  mode. For Ch02: document this as the standard onboarding path for new gh-aw
  deployments based on upstream templates.

### Claim 5: By default, the `pull_request` trigger blocks workflow execution for PRs submitted from forked repositories via repository ID verification — fork PR access is deny-by-default

- **Evidence**: The page states: "By default, workflows block execution for pull
  requests submitted from forked repositories. The system includes a repository ID
  verification within the `pull_request` trigger."
- **Confidence**: settled (first-party documentation; the default behavior is
  explicitly stated)
- **Quote**: "By default, workflows block execution for pull requests submitted
  from forked repositories."
- **Our assessment**: The deny-by-default for fork PRs aligns with the broader
  gh-aw security posture of "zero capability by default" from
  `docs-ghaw-permissions-reference.md` Claim 1 (read-only by default, writes via
  safe outputs only). The `pull_request` trigger's repository ID verification is
  the enforcement mechanism — the system checks whether the PR's source repository
  matches the target repository's ID before proceeding. This prevents a class of
  supply-chain-style attacks where an external fork opens a PR specifically to
  trigger agent execution (e.g., to exploit a prompt-injection vulnerability via PR
  content). For Ch03 (Autonomy & Control / Safety): the deny-by-default for fork
  PRs should be the recommended default for any organization deploying gh-aw in
  a repository that accepts external contributions.

### Claim 6: The `forks:` configuration field in the `pull_request` trigger frontmatter provides explicit allowlisting of fork patterns for PR-triggered workflow execution

- **Evidence**: The page documents the mechanism: "To permit workflows for PRs
  from specific forks, use the `forks:` configuration field" with a YAML example
  showing `forks: ["trusted-org/*"]` under `on.pull_request`. The field allows
  pattern-based allowlisting rather than per-fork enumeration.
- **Confidence**: settled (first-party documentation; the field name and syntax
  are shown with a concrete example)
- **Quote**: "To permit workflows for PRs from specific forks, use the `forks:`
  configuration field"
- **Our assessment**: The `forks:` field is a targeted override of the deny-by-
  default policy — it does not change the default behavior but provides a structured
  mechanism to permit trusted forks without opening access to all forks. The
  pattern-based approach (`"owner/*"` matching all forks from an org) is more
  maintainable than enumerating individual fork repositories. This belongs in the
  same configuration space as `permissions:` and `safe-outputs:` — all three are
  security-relevant frontmatter fields that practitioners must reason about
  explicitly. For Ch02: document `forks:` as a deliberate security opt-in that
  should be reviewed as part of any workflow's security posture.

### Claim 7: The `forks:` field supports three pattern types — `"*"` (all forks), `"owner/*"` (org-scoped), `"owner/repo"` (specific fork) — and accepts multiple patterns as a list

- **Evidence**: The page enumerates: "`"*"` — all forks (use cautiously)",
  "`"owner/*"` — all forks from a specific user/organization",
  "`"owner/repo"` — individual fork repositories". The parenthetical "use
  cautiously" on `"*"` signals official guidance against its casual use.
  "Multiple patterns are supported as a list."
- **Confidence**: settled (first-party documentation; pattern syntax is enumerated
  with descriptions)
- **Quote**: "`"*"` — all forks (use cautiously)"
- **Our assessment**: The three-tier pattern system mirrors standard glob patterns
  used elsewhere in GitHub Actions. The granularity progression (specific repo →
  org-wide → all) maps to a trust escalation scale: narrow (one known fork),
  intermediate (entire trusted org), broad (any fork). Most production deployments
  should use `"owner/*"` — granting access to a specific organization's forks —
  rather than `"*"`. The "use cautiously" annotation on `"*"` is the platform
  team's signal that the all-forks case requires explicit justification, not a
  default choice. For Ch02: recommend `"owner/*"` as the standard pattern for
  organizations with trusted external contributors, and document the escalation
  risk of `"*"`.

### Claim 8: Allowing all forks (`"*"`) enables any user who forks the repository to trigger agent execution — the source characterizes this as requiring careful review of workflow permissions

- **Evidence**: "Allowing all forks enables any user who forks your repository to
  trigger agent execution. Carefully review workflow permissions before enabling
  untrusted fork access." This is labeled as a "Critical Security Note" in the
  source.
- **Confidence**: settled (first-party warning; labeled Critical Security Note in
  the source)
- **Quote**: "Allowing all forks enables any user who forks your repository to
  trigger agent execution. Carefully review workflow permissions before enabling
  untrusted fork access."
- **Our assessment**: The threat model behind this warning: a malicious user forks
  the repository, opens a PR, and the PR content is used as agent input. If the
  agent has broad permissions or can be influenced by PR content (prompt injection),
  the attacker gains execution surface. The four-reason security rationale for safe
  outputs from `docs-ghaw-permissions-reference.md` Claim 2 applies here — blast
  radius limitation and prompt injection defense are the two most relevant concerns
  when fork PRs can reach the agent. The mitigation: review that the workflow's
  `permissions:` block and `safe-outputs:` declarations are appropriately scoped
  before setting `forks: ["*"]`. For Ch03: add this as the canonical fork security
  warning — the `forks: ["*"]` setting should trigger the same review checklist as
  granting write permissions.

## Concrete Artifacts

### Fork Support Configuration — Two-Scenario Reference

```yaml
# Scenario 1: Workflows running INSIDE a forked repository
# ─────────────────────────────────────────────────────────
# No configuration needed — automatic compile-time skip.
# All jobs (agent, self-update, maintenance) are bypassed.
# Rationale: forks lack upstream secrets and contextual information.
#
# Workaround to run in a fork:
#   1. Fork the upstream project
#   2. Configure your own secrets in the forked repository
#   3. The repo is no longer classified as a fork by GitHub Actions

# Scenario 2: INBOUND PRs from forked repositories
# ─────────────────────────────────────────────────
# Default behavior: blocked (deny-by-default via repo ID verification)
#
# To allow execution from trusted forks:
---
on:
  pull_request:
    types: [opened, synchronize]
    forks: ["trusted-org/*"]
---
```

*Source: fork-support reference page — "Workflows Running in Forked Repositories"
and "Inbound Pull Requests from Forks" sections*

### `forks:` Pattern Reference

```
Pattern          Scope                         When to use
──────────────── ───────────────────────────── ────────────────────────────────
"owner/repo"     Specific fork only            Single known trusted fork
"owner/*"        All forks from an org/user    Trusted external organization
"*"              All forks (use cautiously)    Open-source projects only;
                                               requires full permissions review

Multiple patterns are supported as a list:
  forks: ["trusted-org/*", "known-contributor/my-repo"]

Security note (from source):
  "Allowing all forks enables any user who forks your repository to trigger
   agent execution. Carefully review workflow permissions before enabling
   untrusted fork access."
```

*Source: fork-support reference page — "Pattern Matching Options" section and
"Critical Security Note"*

### Fork Execution Decision Tree

```
Is my workflow running inside a forked repo?
  YES → All jobs automatically skipped (compile-time condition)
        No action needed; no configuration available to override
        To run in a fork: configure own secrets → exits fork classification

Is a PR from a forked repo triggering my workflow?
  Default: BLOCKED (deny-by-default via pull_request repo ID verification)
  To allow: add forks: field to pull_request trigger:
    - Specific fork: forks: ["org/fork-repo"]
    - Org-scoped:    forks: ["org/*"]           ← recommended for trusted orgs
    - All forks:     forks: ["*"]               ← review permissions first
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth security
    pipeline, Layer 1: compilation-time validation): The fork execution skip is
    implemented as a compile-time condition — a concrete application of Layer 1
    security. The skip is baked into the generated `.lock.yml` at compile time
    and cannot be accidentally overridden at runtime. This source adds a named,
    specific use case for what compile-time conditions protect against.
  - `docs-ghaw-permissions-reference.md` Claim 1 ("read-only permissions by default,
    with write operations handled through safe outputs"): The fork PR deny-by-default
    follows the same zero-capability-by-default posture — access to fork-triggered
    execution must be explicitly granted, not inherited by default. The source
    corroborates that security defaults in gh-aw are consistently deny-first.
  - `docs-ghaw-permissions-reference.md` Claim 2 (four security purposes of the
    read/safe-outputs separation — audit trail, blast radius, compliance gates,
    prompt injection defense): Claims 5 and 8 here are specific applications of
    blast radius limitation and prompt injection defense. The `pull_request` trigger's
    fork block prevents prompt-injection via PR content from reaching the agent, and
    the `forks:` allowlist limits blast radius to trusted sources.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 1 (two-component workflow structure with YAML
    frontmatter defining triggers, permissions, and tools): This source adds the `forks:`
    field as a security-relevant trigger sub-configuration that practitioners must reason
    about alongside `permissions:` and `safe-outputs:`. Claim 6 here adds a new
    frontmatter field to the trigger configuration space not described in the how-they-work
    overview.
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` bootstraps a repository for
    agentic authoring): Claim 4 here (fork → configure own secrets → exits fork
    classification) is the recommended bootstrap path when starting from an upstream
    gh-aw template repository. The two claims together give the standard "I forked the
    starter, how do I begin?" onboarding sequence: fork upstream → configure secrets →
    use as own repo.
  - `docs-ghaw-compilation-process.md` Claim 3 (Plan-Level Trust: AI reasoning is
    read-only and structurally isolated from write operations via per-job permissions):
    Claim 2 here adds another compile-time trust guarantee — the fork execution skip is
    generated at compile time and is structurally immune to runtime overrides, just as
    job-level permission isolation is structurally immune to in-job overrides.

- **Contradicts**: None identified. No existing source note documents fork behavior in
  gh-aw. The compile-time skip and `forks:` field are entirely new to the corpus and do
  not oppose any existing claims. No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Two-scenario fork taxonomy** (Claim 1): No existing note distinguishes between
    "workflows running inside a fork" and "PRs from a fork" as separate operational
    modes with separate policies. The two-scenario framing is the key structuring insight.
  - **Compile-time fork execution skip** (Claim 2): The automatic skip of all jobs in
    forked repositories via a compile-time condition is not described in any existing
    corpus note. Prior notes describe compile-time validation as a security layer
    conceptually; this is the first specific instance of a compile-time security condition
    with a named function.
  - **Dual-failure rationale for fork skip** (Claim 3): The specific explanation — forks
    lack both secrets AND contextual information — is new. No existing note articulates
    why the skip exists beyond the general security posture.
  - **Fork-to-own-repo migration workaround** (Claim 4): The fork → configure secrets
    → classified-as-owned transition is not documented in any existing note.
  - **`forks:` trigger configuration field** (Claims 6, 7): The `forks:` field in the
    `pull_request` trigger, its three pattern types, and the list-based multi-pattern
    support are not documented in any existing corpus note.
  - **Fork PR as a prompt-injection attack surface** (Claim 8): No existing note
    explicitly names inbound fork PRs as a prompt-injection risk that requires permission
    review before granting `forks: ["*"]` access.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add fork support as a two-scenario deployment decision** (Claims 1, 2, 5): When
  documenting gh-aw deployment, introduce the two-scenario model explicitly. Scenario 1
  (workflows inside a fork): no configuration needed — skip is automatic. Scenario 2
  (PR from a fork): `forks:` field must be explicitly configured to grant access.
  Practitioners deploying to repositories that accept external contributions must
  reason about both scenarios.

- **Document the fork-to-owned-repo onboarding path** (Claim 4): For teams starting
  from an upstream gh-aw template, the correct bootstrap sequence is: fork upstream
  → configure own secrets → treat as owned repository. The `gh aw init` step in
  `docs-ghaw-agentic-authoring.md` Claim 1 comes after this classification shift. Add
  this as a prefatory step in the "New Repository Setup" section.

- **Add `forks:` to the trigger configuration reference** (Claims 6, 7): Document the
  `forks:` field alongside `types:` and other `pull_request` trigger sub-fields. Provide
  the pattern reference table from Concrete Artifacts and recommend `"owner/*"` as the
  standard pattern for organizations with trusted external contributors.

### Chapter 03: Autonomy & Control / Safety

- **Add fork PR as a prompt-injection attack surface** (Claim 8): When discussing
  trust boundaries for agent inputs, add fork PRs as a specific named threat vector.
  PR content (title, body, code changes) is agent input; a PR from an untrusted fork
  is attacker-controlled input that can carry prompt-injection payloads. The deny-by-
  default for fork PRs is the platform's first-line defense; `forks: ["*"]` removes
  this defense and requires compensating controls (permission scoping, safe outputs
  review).

- **Name the fork PR deny-by-default as a blast-radius control** (Claims 5, 8):
  Frame the `pull_request` fork block as the same class of control as the permissions
  deny-by-default in `docs-ghaw-permissions-reference.md` Claim 1. Both implement the
  principle "deny all, grant explicitly." The `forks:` field is the explicit-grant
  mechanism for fork PR access, just as `safe-outputs:` is the explicit-grant mechanism
  for write operations.

- **Flag `forks: ["*"]` as a required permissions-review trigger** (Claim 8): Add to
  the deployment security checklist: any workflow with `forks: ["*"]` in its trigger
  requires a full review of the `permissions:` block and `safe-outputs:` declarations
  before deployment. This mirrors the platform team's "Critical Security Note."

## Extraction Notes

1. **Source is compact but security-dense**: The fork-support reference page is shorter
   than most gh-aw documentation (roughly 250-300 words plus one YAML example and one
   pattern list). Every sentence carries security-relevant content. Claims were exhausted
   after eight extractions.

2. **`if: ${{ !github.event.repository.fork }}` not quoted**: The Prospector's triage
   comment mentions this specific compile-time expression. The source page itself
   describes the compile-time condition without quoting the `if:` expression. Per
   MINER.md §2a, the specific expression is not included as a verbatim quote because
   it does not appear in the source text returned by WebFetch.

3. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with the current gh-aw
   platform as of 2026-05-11.

4. **No contradictions to file**: Reviewed all existing corpus source notes. Fork
   behavior is entirely absent from prior notes. No claims here oppose any existing
   source note. No contradiction issue filed.
