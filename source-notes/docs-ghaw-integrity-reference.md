---
source_url: https://github.github.com/gh-aw/reference/integrity
source_type: docs
title: "GitHub Agentic Workflows: Integrity Filtering Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#398"
---

# GitHub Agentic Workflows: Integrity Filtering Reference

> The authoritative configuration reference for gh-aw's `tools.github.min-integrity`
> mechanism — documents how trust-based content filtering restricts agent access to
> GitHub content before the AI engine processes it, the four-level hierarchy
> (`merged`, `approved`, `unapproved`, `none`), the six-step effective-integrity
> computation algorithm, per-item adjustment via blocked/trusted users and
> approval/refusal labels, reaction-based endorsement (v0.68.2+), centralized
> org-wide management via GitHub Variables, the pre-agent DIFC proxy, and the
> `gh aw logs --filtered-integrity` observability command.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/integrity` page — in
  the "Reference" section alongside `reference/permissions`, `reference/threat-detection`,
  `reference/tools`. Reference pages document platform configuration authoritatively.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI. Configuration
  field names, integrity level definitions, computation algorithm, and default behaviors
  are settled platform facts. The level selection guidance ("Choosing a Level") is
  architectural opinion from the platform team, with rationale.
- **Scope**: Complete reference for the `tools.github` integrity filtering sub-system
  — the eleven configuration fields, the integrity level hierarchy, repository scoping,
  per-item adjustment mechanisms, reaction-based endorsement, GitHub Actions expression
  support, effective integrity computation, centralized variable management, default
  behaviors by repo visibility, the pre-agent DIFC proxy and its disable option, level
  selection guidance, the complete example library, and DIFC_FILTERED log events and
  the `--filtered-integrity` log filter command. Does NOT cover: the broader threat
  detection pipeline (`reference/threat-detection`, see `docs-ghaw-threat-detection.md`),
  the Safe Outputs validation pipeline (`docs-ghaw-safe-outputs-specification.md`), or
  the permissions model (`docs-ghaw-permissions-reference.md`).

## Extracted Claims

### Claim 1: Integrity filtering manages agent access to GitHub content based on author trust rather than permissions — it restricts what reaches the AI engine, not what the agent is allowed to call

- **Evidence**: Opening description of the mechanism: "Integrity filtering (`tools.github.min-integrity`)
  manages which GitHub content an agent can access by filtering based on **trust** rather
  than permissions." The gateway removes low-integrity items from tool call results before
  the AI engine processes them — the agent receives a reduced result set, not an error.
- **Confidence**: settled (first-party documentation; this is the core architectural distinction
  of the feature)
- **Quote**: "Integrity filtering (`tools.github.min-integrity`) manages which GitHub content
  an agent can access by filtering based on **trust** rather than permissions."
- **Our assessment**: This is a fundamentally different security mechanism from the permissions
  model (`docs-ghaw-permissions-reference.md` Claim 1, which controls what GitHub API operations
  the agent can call). Integrity filtering is an *input* restriction: even if the agent is
  permitted to call `list_issues`, items from untrusted authors are silently removed from the
  returned list before the AI engine sees them. The threat model being addressed is prompt
  injection via untrusted content — an attacker cannot inject instructions via an issue comment
  if that comment never reaches the AI engine. This is the data-plane complement to the
  threat detection pipeline (which operates on agent *output*). For Ch03 (Safety and
  Verification): distinguish this from permissions as "trust-based input restriction" vs.
  "capability-based access control."

### Claim 2: The MCP gateway intercepts `tools.github` calls and removes items below the minimum integrity threshold before they reach the AI engine; filtered items are logged as `DIFC_FILTERED` events

- **Evidence**: Mechanism description from the page: "The MCP gateway intercepts tool calls to
  GitHub and applies integrity checks. When an item's integrity falls below the configured
  minimum, the gateway removes it before the AI engine processes it. This filtering is
  transparent—agents receive a reduced result set, and filtered items are logged as
  `DIFC_FILTERED` events."
- **Confidence**: settled (first-party documentation; the interception point, removal behavior,
  and logging mechanism are explicitly described)
- **Quote**: "This filtering is transparent—agents receive a reduced result set, and filtered
  items are logged as `DIFC_FILTERED` events."
- **Our assessment**: The transparency property (agents receive a reduced set, not an error) is
  a deliberate design choice — it avoids revealing the filtering boundary to potentially-malicious
  content. The `DIFC_FILTERED` event logging is the observability hook: security practitioners
  can inspect which items were filtered and why, even though the agent itself cannot see them.
  The term "DIFC" refers to Decentralized Information Flow Control, the underlying security
  model. For Ch02 (Harness Engineering): the transparency means agents do not need to handle
  errors from integrity filtering — the tool call succeeds with fewer results. For Ch03: DIFC_FILTERED
  events are the audit trail for trust-based filtering, analogous to how the Safe Outputs
  audit trail records write operations.

### Claim 3: Four configurable integrity levels form a strict hierarchy — `merged`, `approved`, `unapproved`, `none` — plus an unconditional `blocked` state that cannot be set as a threshold

- **Evidence**: "Integrity Levels Hierarchy" section from the reference page, listing from highest
  to lowest: `merged` (merged PRs, commits reachable from default branch), `approved` (OWNER,
  MEMBER, COLLABORATOR; non-fork PRs on public repos; private repo content; trusted bots; trusted-users),
  `unapproved` (CONTRIBUTOR or FIRST_TIME_CONTRIBUTOR), `none` (all objects including FIRST_TIMER).
  `blocked` is separately defined as "always denied, cannot be promoted."
- **Confidence**: settled (first-party documentation; the level names are explicitly defined and
  align with the names used in `blog-ghaw-weekly-2026-03-30.md` Claim 1 for integrity-aware cache
  storage)
- **Quote**: "The four configurable levels are cumulative and ordered restrictively. Setting
  `min-integrity: approved` means only `approved` or `merged` items reach the agent."
- **Our assessment**: This authoritatively resolves the inference in `blog-ghaw-weekly-2026-03-23.md`
  Concrete Artifacts, which provisionally used "low/medium/high/critical" as example level names
  and explicitly asked for verification. The actual names are `merged`, `approved`, `unapproved`,
  `none`. The `blocked` state is important: it is not a configurable threshold but an automatic,
  permanent denial for users listed in `blocked-users`. For Ch03: use these exact level names in
  the guide; do not use informal names like "high" or "strict."

### Claim 4: Public repositories automatically receive `min-integrity: approved` protection without any configuration; private and internal repositories have no default guard policy

- **Evidence**: "Default Behavior" section of the reference page: "For **public repositories**,
  if no `min-integrity` is configured, the runtime automatically applies `min-integrity: approved`,
  protecting public workflows without additional authentication. For **private and internal
  repositories**, no guard policy applies automatically."
- **Confidence**: settled (first-party documentation; the asymmetric default behavior between
  public and private repos is explicitly stated)
- **Quote**: "For **public repositories**, if no `min-integrity` is configured, the runtime
  automatically applies `min-integrity: approved`, protecting public workflows without additional
  authentication."
- **Our assessment**: This default-enabled protection for public repos is the "secure by default"
  design principle applied at the data layer. It means that public-facing workflows on GitHub
  get baseline protection against content from anonymous contributors without explicit configuration.
  The absence of a default guard for private repos reflects that private repos already have GitHub's
  own access controls — all contributors have been granted repository access. This aligns with the
  `blog-ghaw-weekly-2026-03-23.md` Claim 4 (MCP guard policy GA: "auto-configures access controls
  at runtime with no manual lockdown config") as the general-availability mechanism for this
  protection. For Ch03: note that public repo workflows have this protection automatically — teams
  deploying workflows on private repos must explicitly configure `min-integrity` if they want
  trust-based filtering.

### Claim 5: The effective integrity of each item is computed through a six-step algorithm that applies adjustments in precedence order: base → blocked-users → refusal-labels → trusted-users → approval-labels → base fallback

- **Evidence**: "Effective Integrity Computation" section describes the algorithm:
  1. Start with base integrity from GitHub metadata
  2. If author in `blocked-users`: effective integrity → `blocked`
  3. Else if item has a `refusal-labels` label: effective integrity → `none`
  4. Else if author in `trusted-users`: effective integrity → max(base, `approved`)
  5. Else if item has an `approval-labels` label: effective integrity → max(base, `approved`)
  6. Else: effective integrity → base
  "The `min-integrity` threshold is applied after this computation."
- **Confidence**: settled (first-party documentation; the step-by-step algorithm is explicitly
  specified in numbered order)
- **Quote**: (no direct quote; the algorithm is presented as a numbered list — see Concrete
  Artifacts)
- **Our assessment**: The precedence order is the critical implementation detail. `blocked-users`
  wins over everything: even if an item has an `approval-labels` label, a blocked author's content
  is still denied. Refusal overrides promotion: a `refusal-labels` label beats `trusted-users`
  and `approval-labels`. Trust elevation and label promotion are symmetric (`max(base, approved)`)
  — neither can demote integrity, only raise it. For Ch02: practitioners designing complex guard
  policies with overlapping rules need to understand this precedence to predict behavior. For
  Ch03: the precedence design implements defense-in-depth — the most restrictive controls
  (blocked-users, refusal-labels) are checked first and cannot be overridden by later steps.

### Claim 6: `blocked-users` unconditionally denies all content from listed usernames, overriding all other settings including trust elevation and label promotion

- **Evidence**: Configuration field description: "`blocked-users` unconditionally blocks content
  from listed usernames, overriding all other settings." Example showing use with `min-integrity: none`
  (permissive level but specific accounts blocked). The `blocked-users` step is Step 2 in the
  effective integrity computation — checked before any positive adjustment.
- **Confidence**: settled (first-party documentation; "unconditionally" and "overriding all other
  settings" are explicit)
- **Quote**: "`blocked-users` unconditionally blocks content from listed usernames, overriding
  all other settings"
- **Our assessment**: `blocked-users` is the absolute denial mechanism. Unlike `min-integrity`
  (which sets a floor for the general population), `blocked-users` is an allow-list exclusion —
  named accounts are always denied regardless of how permissive the general configuration is.
  This is the correct design for handling compromised accounts or known-bad actors: you don't
  need to lower your general `min-integrity` threshold, you just add specific accounts to
  `blocked-users`. For Ch03: recommend `blocked-users` as the targeted response to specific
  threat actors (compromised accounts, spam bots) while keeping general `min-integrity` at
  an appropriate level for the workflow.

### Claim 7: `trusted-users` elevates listed usernames to `approved` integrity regardless of GitHub author association, enabling external contractors and partner developers to be treated as trusted contributors

- **Evidence**: Configuration field description: "`trusted-users` elevates listed usernames to
  `approved` integrity regardless of GitHub's author association." Additional constraint: "Trust
  elevation only raises integrity—never lowers it. `blocked-users` takes precedence." Requirement:
  "`trusted-users` requires `min-integrity` to be set."
- **Confidence**: settled (first-party documentation; behavior and constraints are explicitly stated)
- **Quote**: "`trusted-users` requires `min-integrity` to be set."
- **Our assessment**: `trusted-users` is the mechanism for handling the contractor/partner pattern:
  someone who is not an OWNER, MEMBER, or COLLABORATOR on the repository but should be treated
  as trusted for agent input purposes. Without `trusted-users`, a contractor with FIRST_TIME_CONTRIBUTOR
  association would be at `unapproved` level; `trusted-users` raises them to `approved` regardless.
  The constraint that `min-integrity` must be set is important — `trusted-users` cannot be used
  on a public repo that has no explicit `min-integrity` (relying on the default `approved` auto-apply).
  For Ch02: document `trusted-users` as the standard integration point for non-member trusted parties.

### Claim 8: `approval-labels` and `refusal-labels` implement a human-review gate: labeled items are promoted to `approved` or demoted to `none` regardless of author integrity

- **Evidence**: `approval-labels`: "promotes items bearing listed labels to `approved` integrity,
  enabling human-review workflows." `refusal-labels`: "downgrades items bearing listed labels
  to `none` integrity, overriding promotion." The example uses `agent-approved` and `human-reviewed`
  as approval labels; `needs-security-review` and `do-not-automate` as refusal labels.
- **Confidence**: settled (first-party documentation; the promotion and demotion semantics are
  explicitly stated, with the interaction noted: "refusal overrides promotion but not blocked-user
  exclusion")
- **Quote**: "Promotion only raises integrity and respects blocked-user exclusion."
- **Our assessment**: `approval-labels` is the human-review gate for external contributions: a
  maintainer reviews an issue or PR from an external contributor and adds `agent-approved`, which
  promotes it to `approved` level so the agent can process it. `refusal-labels` is the suppression
  mechanism: a team can mark items with `do-not-automate` to prevent the agent from ever processing
  them regardless of who filed them. Together, these two mechanisms implement a lightweight
  human-in-the-loop workflow on top of the trust hierarchy without requiring `trusted-users` grants.
  For Ch03 (Safety): this is the "human vouches for this item" pattern — the label is the vouching
  mechanism, human-readable and visible in the GitHub UI.

### Claim 9: Reaction-based endorsement (available from v0.68.2) allows maintainers to adjust item integrity using GitHub reactions without adding labels, configured via `features.integrity-reactions: true`

- **Evidence**: Configuration section "Promoting and Demoting via Reactions" states reactions
  are "available from v0.68.2." `features.integrity-reactions: true` enables the feature. Default
  endorsement reactions: `THUMBS_UP`, `HEART`. Default disapproval reactions: `THUMBS_DOWN`, `CONFUSED`.
  The `endorser-min-integrity` field (default: `approved`) controls who can endorse.
- **Confidence**: emerging (first-party documentation; version gate established; the default
  reaction values and endorser integrity requirement are specified, but broad adoption is not
  yet documented)
- **Quote**: (no direct quote; the reactions feature is described across multiple configuration
  fields without a single introductory sentence to quote verbatim — see Concrete Artifacts)
- **Our assessment**: Reaction-based endorsement is a UX improvement over `approval-labels` for
  high-volume workflows. Adding a label requires label management (creating the label, granting
  permission to apply it); a reaction requires only clicking an emoji. The `endorser-min-integrity`
  field (who can endorse) prevents low-integrity actors from self-endorsing their content by
  reacting to it — the endorser must themselves be at `approved` level or higher by default.
  The `disapproval-integrity` field (default: `none`) allows even a single disapproval to make
  content inaccessible to the agent, which is a conservative default appropriate for security-
  sensitive workflows. For Ch02: recommend reactions as the lightweight alternative to approval-labels
  for teams where label management is a friction point.

### Claim 10: All list-type fields accept GitHub Actions expressions evaluated at runtime, enabling centralized management via repository or organization variables

- **Evidence**: "Using GitHub Actions Expressions" section shows all four list fields accepting
  expression syntax. "Centralized Management via GitHub Variables" section documents four
  corresponding variables (`GH_AW_GITHUB_BLOCKED_USERS`, `GH_AW_GITHUB_TRUSTED_USERS`,
  `GH_AW_GITHUB_APPROVAL_LABELS`, `GH_AW_GITHUB_REFUSAL_LABELS`) that are automatically
  unioned with per-workflow values. Variables split on commas and newlines, are trimmed and
  deduplicated.
- **Confidence**: settled (first-party documentation; the variable names, union behavior, and
  delimiter formats are explicitly specified)
- **Quote**: "The runtime unions per-workflow values with corresponding variables."
- **Our assessment**: The GitHub Variables integration enables the "define-once, apply-everywhere"
  pattern for blocked user lists and trusted user lists across an organization. An organization can
  maintain `GH_AW_GITHUB_BLOCKED_USERS` as an org-level variable that automatically applies to
  all workflows — individual workflows do not need to enumerate blocked users explicitly. This is
  the enterprise-scale management pattern: org-level security policy expressed once, applied
  uniformly. For Ch02: document this as the fleet-management pattern for integrity policy. For
  Ch03: org-level variables provide a single place to update blocked users across all workflows
  when an account is compromised.

### Claim 11: When a guard policy is configured, a DIFC proxy is automatically injected to filter pre-agent `gh` CLI calls in setup steps using the same MCP gateway container; this proxy can be disabled with `integrity-proxy: false`

- **Evidence**: "Pre-Agent Integrity Proxy" section: "When a guard policy is configured, the
  compiler injects a DIFC proxy filtering `gh` CLI calls in pre-agent setup steps." The proxy
  uses the same MCP gateway container, applies only static fields (`min-integrity` and
  `allowed-repos`), and does NOT apply `blocked-users`, `trusted-users`, `approval-labels`,
  or `refusal-labels` (resolved at runtime). The proxy "starts before custom steps and stops
  before MCP gateway starts to prevent double-filtering." Disabling: `integrity-proxy: false`.
- **Confidence**: settled (first-party documentation; the proxy behavior, limitations, and
  disable option are explicitly specified)
- **Quote**: "This opt-out is useful when pre-agent steps require unfiltered API access.
  Disabling only affects pre-agent `gh` calls—the agent itself always operates under the
  configured guard policy."
- **Our assessment**: The pre-agent proxy is an automatically-active safety extension that most
  practitioners will not need to configure. Its key limitation: it only applies static policy
  fields (those known at compile time). If a workflow relies on `trusted-users` or `approval-labels`
  in pre-agent steps, the proxy will not apply those — only the base `min-integrity` threshold.
  The `integrity-proxy: false` opt-out is specifically useful when a pre-agent setup step needs
  to read content that would be filtered (e.g., a step that processes all issues regardless of
  author trust). Disabling the proxy does not affect the agent's own filtering, which always
  operates under the full guard policy. For Ch02: document the proxy as automatic and explain
  the `integrity-proxy: false` escape hatch with its appropriate use case.

### Claim 12: The `gh aw logs --filtered-integrity` command downloads only runs with integrity-filtered content, enabling targeted investigation of filtering behavior and policy tuning

- **Evidence**: "Filtering Logs by Integrity Events" section: "This downloads only runs with
  integrity-filtered content, useful for investigating whether configuration filters expected
  content or when tuning levels after observing traffic patterns."
- **Confidence**: settled (first-party documentation; the command and use cases are explicitly
  stated)
- **Quote**: "This downloads only runs with integrity-filtered content, useful for investigating
  whether configuration filters expected content or when tuning levels after observing traffic
  patterns."
- **Our assessment**: The `--filtered-integrity` flag addresses a key operational need: when
  a workflow is behaving unexpectedly (not processing items that should be processed, or
  processing items that seem wrong), this command isolates the runs where filtering was active.
  Combined with the structured DIFC_FILTERED event fields (server, tool, user, reason, integrity
  tags, author association), practitioners can identify exactly what was filtered and why. For
  Ch02: document this command as the first diagnostic step when debugging unexpected agent
  behavior on content-filtered workflows. For Ch03: the DIFC_FILTERED event log is the audit
  trail for trust-based filtering — recommend enabling `gh aw logs --filtered-integrity`
  review as part of security observability workflows (this also connects to `docs-ghaw-dailyops.md`
  Claim 7: `daily-security-observability.md` uses "DIFC integrity-filtered event analysis").

## Concrete Artifacts

### Basic Configuration (from reference page)

```yaml
# Minimum integrity for all GitHub content:
tools:
  github:
    min-integrity: approved

# With repository scoping:
tools:
  github:
    allowed-repos: "myorg/*"
    min-integrity: approved
```

*Source: gh-aw reference/integrity, "Configuration" section*

### Configuration Reference Table (from reference page)

```
Field                     Type              Req  Default                     Description
---                       ---               ---  ---                         ---
min-integrity             string            Yes* approved (public); none      Minimum level: merged/approved/unapproved/none
                                                 (private)
allowed-repos             string/array      No   "all"                       Scope: "all", "public", or patterns
blocked-users             array/expression  No   []                          Unconditional denial
trusted-users             array/expression  No   []                          Elevated to approved (requires min-integrity)
approval-labels           array/expression  No   []                          Labels promoting items to approved
refusal-labels            array/expression  No   []                          Labels downgrading to none
integrity-proxy           boolean           No   true                        Enable DIFC proxy for pre-agent gh CLI calls
endorsement-reactions     array             No   ["THUMBS_UP", "HEART"]      Reactions promoting to approved (v0.68.2+)
disapproval-reactions     array             No   ["THUMBS_DOWN", "CONFUSED"] Reactions demoting integrity
endorser-min-integrity    string            No   approved                    Minimum integrity of endorser
disapproval-integrity     string            No   none                        Integrity level when disapproval applied

* Required when guard policy used. Note: `repos` is deprecated; use `allowed-repos`.
```

*Source: gh-aw reference/integrity, "Configuration Reference Table"*

### Integrity Levels Hierarchy (from reference page)

```
LEVEL        WHAT IT COVERS
merged       Pull requests merged into target branch; commits reachable from
             default branch (any author). Strictest configurable level.

approved     Objects authored by OWNER, MEMBER, or COLLABORATOR; non-fork PRs
             on public repos; all items in private repos; trusted platform bots;
             users in trusted-users list.

unapproved   Objects from CONTRIBUTOR or FIRST_TIME_CONTRIBUTOR.

none         All objects, including FIRST_TIMER and users with no association.

blocked      Items from users in blocked-users — always denied, cannot be promoted.
             (Not a configurable threshold — automatic and permanent.)
```

*Source: gh-aw reference/integrity, "Integrity Levels Hierarchy" section*

### Effective Integrity Computation (from reference page)

```
Algorithm (applied to each item, in order):

  1. Start with base integrity from GitHub metadata
  2. If author in blocked-users:
       → effective integrity = blocked
  3. Else if item has a refusal-labels label:
       → effective integrity = none
  4. Else if author in trusted-users:
       → effective integrity = max(base, approved)
  5. Else if item has an approval-labels label:
       → effective integrity = max(base, approved)
  6. Else:
       → effective integrity = base

  Then: apply min-integrity threshold (filter items below threshold)
```

*Source: gh-aw reference/integrity, "Effective Integrity Computation" section*

### Level Selection Guidance (from reference page)

```
Workflow intent                                    Recommended level
---                                               ---
Code review automation / applying changes         merged or approved (trusted content only)
Responding to maintainers and contributors        approved (common, safe default)
Community triage or planning                      unapproved (allow contributors but not
                                                  anonymous/first-time interactions)
Public-data or spam detection workflows           none (see all activity, ensure outputs
                                                  not applied without review)

WARNING: Setting min-integrity: none on public repositories disables automatic
protection — use only when designed for untrusted input.
```

*Source: gh-aw reference/integrity, "Choosing a Level" section*

### Centralized Management via GitHub Variables (from reference page)

```
Workflow field          GitHub Variable
---                     ---
blocked-users           GH_AW_GITHUB_BLOCKED_USERS
trusted-users           GH_AW_GITHUB_TRUSTED_USERS
approval-labels         GH_AW_GITHUB_APPROVAL_LABELS
refusal-labels          GH_AW_GITHUB_REFUSAL_LABELS

Runtime behavior:
  - Workflow values are UNIONED with corresponding variable values
  - Variables split on commas and newlines; trimmed; deduplicated
  - Set at: Settings → Secrets and variables → Actions → Variables
  - Set at org level for enterprise-wide application
```

*Source: gh-aw reference/integrity, "Centralized Management via GitHub Variables" section*

### DIFC_FILTERED Log Event Fields (from reference page)

```
When an item is filtered, a DIFC_FILTERED event is recorded in gateway.jsonl:

  Server           — MCP server returning filtered content
  Tool             — Tool call producing it (e.g., list_issues, get_pull_request)
  User             — Content author's login
  Reason           — e.g., "Resource has lower integrity than agent requires"
  Integrity tags   — Tags assigned to filtered item
  Author association — GitHub author association classification

Filtered events appear in a "DIFC Filtered Events" table in run summaries.
The summary line shows total filtered item count.
```

*Source: gh-aw reference/integrity, "In Logs and Reports" section*

### Reaction-based Endorsement (from reference page, v0.68.2+)

```yaml
# Enable reaction-based integrity adjustment:
features:
  integrity-reactions: true
tools:
  github:
    min-integrity: approved

# Custom reaction configuration:
tools:
  github:
    endorsement-reactions:
      - "THUMBS_UP"
      - "HEART"
    disapproval-reactions:
      - "THUMBS_DOWN"
    endorser-min-integrity: merged   # Override: only merged-level users can endorse
    disapproval-integrity: unapproved

# Valid reaction values:
# THUMBS_UP, THUMBS_DOWN, HEART, HOORAY, CONFUSED, ROCKET, EYES, LAUGH
```

*Source: gh-aw reference/integrity, "Promoting and Demoting via Reactions" section*

### Complete Example: Human-Review Gate with Fleet Management (from reference page)

```yaml
tools:
  github:
    allowed-repos: "all"
    min-integrity: approved
    blocked-users: ${{ vars.GH_AW_GITHUB_BLOCKED_USERS }}
    trusted-users: ${{ vars.GH_AW_GITHUB_TRUSTED_USERS }}
    approval-labels:
      - "agent-approved"
    refusal-labels:
      - "needs-security-review"
```

*Source: gh-aw reference/integrity, "Combined blocking, trusting, labeling, and refusing" example*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-03-23.md` Claim 4 (GitHub MCP guard policy reaches GA;
    "auto-configures access controls at runtime with no manual lockdown config"): Claim 4 here
    documents the concrete default behavior enabled by that GA designation — `min-integrity: approved`
    is automatically applied to public repos without configuration. The two sources together
    establish: GA guard exists (weekly note) + exactly what it configures by default (this
    reference page).
  - `blog-ghaw-weekly-2026-03-30.md` Claim 1 (integrity-aware cache-memory using git branches
    `merged`, `approved`, `unapproved`, `none`): That claim independently confirms the four
    integrity level names used by this reference page. The March 30 note documents those names
    in the context of cache storage isolation; this page documents them as the filtering threshold
    API. The two sources are consistent.
  - `docs-ghaw-permissions-reference.md` Claim 2 (four security rationales for the read/safe-outputs
    separation, including "prompt injection defense"): Integrity filtering is the concrete
    implementation of prompt-injection defense at the *input* layer — it prevents untrusted content
    from reaching the AI engine in the first place. The permissions note states prompt injection
    defense as a rationale for the write-separation architecture; this note documents the complementary
    input-restriction mechanism.
  - `docs-ghaw-dailyops.md` Claim 7 (`daily-security-observability.md` uses "DIFC integrity-filtered
    event analysis"): Claim 12 here documents exactly what DIFC_FILTERED events are and how to
    retrieve them with `gh aw logs --filtered-integrity`. The DailyOps note names the observability
    workflow; this reference page specifies the event data model it operates on.

- **Contradicts**: None identified. No existing source note makes claims that conflict with the
  integrity filtering mechanism, the four-level hierarchy, the effective integrity computation
  algorithm, or the default behavior for public vs. private repos.

  **Resolves provisional inference in `blog-ghaw-weekly-2026-03-23.md`**: The Concrete Artifacts
  section of that note used inferred level names "low, medium, high, critical" for `min-integrity`,
  explicitly flagged as "inferred from common patterns; the actual API values should be verified."
  This reference page is that verification — the actual level names are `merged`, `approved`,
  `unapproved`, `none`. No contradiction issue is required (the blog note already flagged its
  inference as provisional), but practitioners should use the names from this reference page.
  The `blog-ghaw-weekly-2026-03-30.md` Claim 1 had already confirmed these names in the context
  of cache storage.

- **Extends**:
  - `blog-ghaw-weekly-2026-03-23.md` Claim 3 (`lockdown: true` → `min-integrity` breaking change
    in v0.62.2): That note documented the breaking change but had no detailed documentation of the
    `min-integrity` API. This reference page is the comprehensive specification: the eleven
    configuration fields, the four integrity levels, the effective integrity computation algorithm,
    all per-item adjustment mechanisms, centralized variable management, the pre-agent proxy,
    and the log observability command. The blog note established the transition; this page documents
    the full surface.
  - `docs-ghaw-threat-detection.md` (threat detection as a separate pipeline stage between the
    agentic job and safe output jobs): Integrity filtering operates at a different layer — it
    restricts *inputs* to the agent (what GitHub content reaches the AI engine during a run).
    Threat detection analyzes agent *outputs* (what the agent wants to write to GitHub). Together
    with the safe outputs validation pipeline, the three mechanisms form a complete defense chain:
    integrity filtering (input restriction by trust) → threat detection (output analysis) → safe
    outputs validation (write operation enforcement).
  - `docs-ghaw-tools-reference.md` Claim 9 (`github:` tool provides GitHub API access with
    configurable toolsets): `min-integrity` is configured within `tools.github`, making integrity
    filtering a sub-configuration of the `github:` tool. The tools reference documents the existence
    of `github:` toolset configuration; this reference page documents the `min-integrity` sub-field
    in complete detail.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Complete `min-integrity` configuration reference**: No prior source note documents the
    full eleven-field configuration surface (`min-integrity`, `allowed-repos`, `blocked-users`,
    `trusted-users`, `approval-labels`, `refusal-labels`, `integrity-proxy`, `endorsement-reactions`,
    `disapproval-reactions`, `endorser-min-integrity`, `disapproval-integrity`). Prior notes mention
    only `min-integrity` in passing.
  - **Authoritative integrity level names**: `merged`, `approved`, `unapproved`, `none` as the
    exact API values, resolving the blog-ghaw-weekly-2026-03-23.md provisional inference.
  - **Six-step effective integrity computation algorithm** (Claim 5): The precedence order for
    per-item adjustments is not described in any existing source note.
  - **Public repo default protection** (Claim 4): The automatic `min-integrity: approved` for
    public repos without configuration is referenced in context in blog-ghaw-weekly-2026-03-23.md
    but not fully documented with its private-repo asymmetry.
  - **Pre-agent DIFC proxy** (Claim 11): No prior source note documents this automatic injection
    for pre-agent `gh` CLI calls, its compile-time limitation to static fields, or the
    `integrity-proxy: false` disable option.
  - **Reaction-based endorsement** (Claim 9): No existing source note mentions the
    `features.integrity-reactions` flag or reaction-based integrity adjustment (v0.68.2+).
  - **Centralized variable management** (Claim 10): The four `GH_AW_GITHUB_*` variables and
    their union-with-workflow-values behavior are not documented in any existing source note.
  - **`gh aw logs --filtered-integrity`** (Claim 12): No existing source note documents this
    specific observability command or the full DIFC_FILTERED event field set.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add integrity filtering as a first-class `tools.github` configuration pattern** (Claims 1–2):
  The guide currently documents permissions (read scopes) and safe outputs (write operations) as
  the two primary security configuration surfaces. Add `min-integrity` as the third: trust-based
  input restriction that complements permission control. The canonical harness pattern expands to
  `permissions: {read scopes} + safe-outputs: {write ops} + tools.github.min-integrity: {level}`.

- **Document the eleven configuration fields** (Claim 2, Concrete Artifacts): Add the full
  configuration table as the reference for integrity filtering. The `min-integrity`, `allowed-repos`,
  `blocked-users`, `trusted-users`, `approval-labels`, and `refusal-labels` fields cover the
  typical configuration surface; document reactions and `integrity-proxy` as advanced options.

- **Add centralized variable management as the enterprise fleet pattern** (Claim 10): For
  organizations running workflows across multiple repositories, the `GH_AW_GITHUB_*` org-level
  variables are the mechanism for consistent integrity policy without per-workflow configuration.
  Document as an advanced harness pattern.

- **Document `integrity-proxy: false` with its specific use case** (Claim 11): Practitioners
  who disable the pre-agent proxy should understand they are only affecting pre-agent `gh` CLI
  calls — the agent itself always runs under the full guard policy. Flag this as a targeted
  opt-out, not a global disable.

### Chapter 03: Safety and Verification

- **Distinguish integrity filtering from permissions and threat detection** (Claim 1):
  The guide needs a clear conceptual map of the three security layers: (1) integrity filtering
  (trust-based input restriction — what the agent sees), (2) threat detection (output analysis —
  what the agent produces), (3) safe outputs validation (write enforcement — what the agent
  writes). Current Ch03 coverage of the safe-outputs architecture is missing the input restriction
  layer.

- **Use the four integrity levels as vocabulary for trust-tier design** (Claim 3): When recommending
  integrity levels, always use the actual API names (`merged`, `approved`, `unapproved`, `none`).
  Provide level selection guidance aligned with the reference page's table. The `approved` level
  is the correct default for most workflows responding to maintainers and contributors.

- **Document the six-step effective integrity algorithm** (Claim 5): Practitioners designing
  complex guard policies (combining `blocked-users`, `trusted-users`, `approval-labels`, and
  `refusal-labels`) need to understand the precedence order to predict behavior. The critical
  insight: blocked > refusal > trust-elevation — the most restrictive controls always win.

- **Add `approval-labels` as the human-review gate pattern** (Claim 8): For workflows that
  process external contributions, the `approval-labels` pattern (maintainer adds a label to
  vouch for an item before the agent processes it) is the lightweight human-in-the-loop
  control for input trust, analogous to the `fallback-to-issue` policy in threat detection.

- **Recommend DIFC_FILTERED log review as security observability** (Claim 12): The
  `gh aw logs --filtered-integrity` command is a targeted tool for auditing which content
  was filtered and why. Recommend including it in regular security observability workflows
  alongside the `daily-security-observability.md` workflow pattern from `docs-ghaw-dailyops.md`.

## Extraction Notes

1. **Source rendered fully via WebFetch**: The `reference/integrity` page is a static
   Astro/Starlight SPA. Content was fully accessible via WebFetch and returned comprehensive
   structured content. No sub-pages were followed (the page links to the GitHub Tools Reference
   and MCP Gateway for related documentation; those are separate source notes).

2. **Provisional level names from March 23 weekly resolved**: The `blog-ghaw-weekly-2026-03-23.md`
   note inferred `min-integrity` levels as "low, medium, high, critical" and explicitly asked
   for verification. This reference page confirms the actual names: `merged`, `approved`,
   `unapproved`, `none`. No contradiction issue required since the inference was explicitly
   flagged as provisional. The `blog-ghaw-weekly-2026-03-30.md` Claim 1 had already confirmed
   these names in the cache storage context.

3. **`integrity-proxy` interaction with runtime-resolved fields**: The pre-agent DIFC proxy
   applies only static fields (`min-integrity`, `allowed-repos`) because `blocked-users`,
   `trusted-users`, `approval-labels`, and `refusal-labels` are resolved at runtime (they
   may contain GitHub Actions expressions referencing variables). This is an important
   limitation to document: the proxy provides a baseline protection level, not the full
   guard policy.

4. **Reaction-based endorsement version gate**: `features.integrity-reactions` requires v0.68.2+.
   Teams on earlier versions will not see this feature. The `blog-ghaw-weekly-2026-04-27.md`
   note covers changes around that period; practitioners should verify their platform version
   before relying on this feature.

5. **No publication date**: The documentation page does not carry an explicit publication date.
   Content reflects the current gh-aw platform state as of 2026-05-12.

6. **No contradictions filed**: Reviewed all existing source notes with integrity or DIFC
   references. No claims in this source materially oppose any existing note. The provisional
   level names in `blog-ghaw-weekly-2026-03-23.md` are resolved, not contradicted — that
   note explicitly flagged them for verification. No contradiction issue required.
