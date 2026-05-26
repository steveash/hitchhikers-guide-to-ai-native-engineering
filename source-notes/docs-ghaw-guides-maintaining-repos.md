---
source_url: https://github.github.com/gh-aw/guides/maintaining-repos
source_type: docs
title: "GitHub Agentic Workflows: Guides — Maintaining Repositories"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: emerging
issue: "#437"
---

# GitHub Agentic Workflows: Guides — Maintaining Repositories

> An integrated practitioner guide covering the defense-in-depth model for open-source
> repository automation — Repo Assist as triage layer, safe-outputs as output control,
> and integrity filtering as input control — with scaling strategies, a five-step debug
> workflow, and a six-category failure taxonomy for public-repository maintenance at scale.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guides page — now redirecting to
  `examples/maintaining-repos`; see Extraction Notes. Content is first-party from the
  same team behind the Peli de Halleux agent factory blog series and the `gh aw` CLI.)
- **Author credibility**: GitHub Next / Microsoft Research. Configuration field names,
  CLI commands, and behavior descriptions are authoritative for the `gh aw` platform.
  The page uses v0.72.0+ field naming conventions (`user-rate-limit`, `max-runs-per-window`)
  consistent with the breaking change documented in `blog-ghaw-weekly-2026-05-11.md` Claim 6.
- **Scope**: Practitioner guide for maintaining public repositories with agentic workflows.
  Covers: the trust-surface challenge for open-source repos, Repo Assist as a prerequisite
  triage layer, safe-outputs output control (eight types), integrity filtering input control
  (four levels plus reactions-as-trust-signals), four scaling mechanisms (rate limiting,
  pre-activation skips, concurrency, repository scoping), five-step iterative debug workflow
  with AI-assisted Copilot CLI, and six failure pattern categories with remediation guidance.
  Does NOT cover: the normative safe-outputs specification (`docs-ghaw-safe-outputs-specification.md`),
  the complete integrity filtering reference (`docs-ghaw-integrity-reference.md`), or the full
  eight-mechanism anti-runaway taxonomy (`docs-ghaw-rate-limiting-controls.md`).

## Extracted Claims

### Claim 1: Public repository agentic workflows face a trust-surface challenge — any authenticated user can trigger agent runs, requiring defense-in-depth as the architectural response

- **Evidence**: The page opens by stating the challenge directly: "anyone can open an
  issue or PR, triggering agent runs that consume compute and tokens — but not every
  contributor is equally trustworthy." It then presents the two-mechanism defense:
  "Together they form a defense-in-depth model: integrity filtering keeps untrusted
  content out of the agent's context, and safe-outputs ensure the agent can only
  produce authorized side-effects."
- **Confidence**: settled (first-party framing of the platform's public-repo threat
  model; the two-mechanism defense-in-depth claim is consistent with the formal
  specifications in `docs-ghaw-integrity-reference.md` and `docs-ghaw-safe-outputs-specification.md`)
- **Quote**: "Open-source maintainers face a unique challenge when running agentic
  workflows: anyone can open an issue or PR, triggering agent runs that consume
  compute and tokens — but not every contributor is equally trustworthy."
- **Our assessment**: This is the most direct statement in the corpus of why public-repo
  agentic workflows require special handling beyond what private-repo workflows need.
  The trust-surface problem is bidirectional: (1) untrusted input can manipulate agent
  behavior via prompt injection in issue or PR content; (2) untrusted triggers can exhaust
  resources by driving every opened issue through a full agent run. The two-mechanism
  defense addresses both: integrity filtering handles input restriction before context
  assembly; safe-outputs handles output scope enforcement before the GitHub API. For
  Ch03 (Safety and Verification): use this framing as the opening rationale for why
  public-repo workflows require the additional safety layers documented in this source.

### Claim 2: Repo Assist is the recommended starting point for any public repository — it classifies incoming issues and PRs and routes work, functioning as a triage layer that gates downstream code-modifying agents

- **Evidence**: The page positions Repo Assist as "the recommended starting point for
  any public repository because it: Sees all incoming content (including from untrusted
  users), so nothing is silently ignored." It "runs on every new issue or PR, classifies
  the content, and routes work to the right place." A notable detail: Repo Assist
  "overrides this to `unapproved` so it can see issues from contributors and first-time
  contributors" — meaning the triage workflow relaxes integrity filtering to see all
  incoming content, while downstream code-modifying agents use stricter thresholds.
- **Confidence**: emerging (first-party prescriptive positioning; the triage-layer
  architectural rationale is editorial guidance, not a measured outcome)
- **Quote**: "Repo Assist is a workflow that runs on every new issue or PR, classifies
  the content, and routes work to the right place. It is the recommended starting point
  for any public repository because it:"
- **Our assessment**: The triage-layer pattern separates lightweight classification
  (Repo Assist: labels, comments, routing) from heavyweight code-modifying operations
  (downstream agents). This prevents runaway resource consumption where every opened
  issue triggers a full code-modifying agent — Repo Assist absorbs volume and escalates
  to expensive agents only when warranted by classification. The integrity-filtering
  override is architecturally significant: Repo Assist operates at `unapproved` to see
  everything; downstream agents use the stricter default (`approved` on public repos per
  `docs-ghaw-integrity-reference.md` Claim 4). For Ch02 (Harness Engineering): Repo
  Assist as triage layer should be the first workflow deployed on any public repository,
  with code-modifying agents added as downstream consumers of its routing decisions.
  Corroborates `docs-ghaw-examples-maintaining-repos.md` Claim 1.

### Claim 3: Safe-outputs is the primary output control mechanism — every GitHub side-effect must be explicitly declared in the `safe-outputs:` block or the runtime blocks it before reaching the API

- **Evidence**: The "Controlling Workflow Outputs with Safe-Outputs" section states:
  "Safe-outputs is the primary mechanism for controlling what a workflow can do. Every
  action that produces a side-effect on GitHub — labeling an issue, posting a comment,
  opening a pull request, merging — must be explicitly declared in the `safe-outputs:`
  block." The enforcement: "If an action isn't listed, the runtime blocks it before it
  reaches the API."
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-safe-outputs-specification.md` Claim 5, SP2 Validation Precedence:
  "validation logic MUST execute before any GitHub API invocation")
- **Quote**: "Safe-outputs is the primary mechanism for controlling what a workflow can
  do. Every action that produces a side-effect on GitHub — labeling an issue, posting a
  comment, opening a pull request, merging — must be explicitly declared in the
  `safe-outputs:` block."
- **Our assessment**: The "declare or be blocked" framing is the most accessible entry
  point for practitioners encountering safe-outputs for the first time. It translates the
  formal normative definition in `docs-ghaw-safe-outputs-specification.md` into an
  operational rule: enumerate what you need; anything not listed is automatically
  suppressed before reaching the GitHub API. The runtime enforcement ("blocks it before
  it reaches the API") means a misconfigured or misbehaving agent cannot cause undeclared
  side-effects regardless of what it attempts. For Ch02 and Ch03: use this framing
  alongside the specification's formal definition to give practitioners both the
  conceptual model and the normative requirements. Corroborates `docs-ghaw-examples-maintaining-repos.md`
  Claim 2.

### Claim 4: Eight safe-output types cover the complete write surface for repository maintenance: label-issue, comment-issue, comment-pull-request, create-pull-request, merge-pull-request, close-issue, create-issue, assign-issue

- **Evidence**: The page provides a complete table of safe-output types with their
  capabilities covering triage (label, comment), contribution handling (create-pr,
  close-issue), work assignment (assign-issue), and new work creation (create-issue).
  The `merge-pull-request` type is explicitly flagged as "experimental."
- **Confidence**: settled (first-party documentation; the type names are explicit in
  the table; "experimental" flag on `merge-pull-request` is stated)
- **Quote**: (no direct single-sentence quote; the eight types are presented as a table
  — see Concrete Artifacts)
- **Our assessment**: These eight types are the practitioner checklist for configuring
  repository maintenance safe-outputs blocks. The `merge-pull-request` "experimental"
  flag is important — teams should not rely on it for production maintenance workflows
  until it reaches stable status. For Ch02: use this enumeration as the reference
  checklist when documenting safe-outputs configuration for maintenance workflows.
  Corroborates `docs-ghaw-examples-maintaining-repos.md` Claim 3.

### Claim 5: Integrity filtering is the primary input control mechanism — it evaluates author trust and removes items below the threshold before the agent's context is assembled, complementing safe-outputs' output control

- **Evidence**: The "Controlling Workflow Inputs with Integrity Filtering" section:
  "Integrity filtering is the primary mechanism for controlling what content the agent
  sees. It evaluates the author of each issue, PR, or comment and removes items that
  don't meet the configured trust threshold — before the agent's context is assembled."
  The page also notes that Repo Assist overrides this to `unapproved` so it can see
  all incoming content.
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-integrity-reference.md` Claim 1's "filters based on trust rather than
  permissions" framing)
- **Quote**: "Integrity filtering is the primary mechanism for controlling what content
  the agent sees. It evaluates the author of each issue, PR, or comment and removes
  items that don't meet the configured trust threshold — before the agent's context is
  assembled."
- **Our assessment**: The pre-context-assembly timing is architecturally significant —
  integrity filtering acts before the agent runs; filtered content never enters the AI
  engine's context at all. This contrasts with threat detection (which analyzes agent
  output after the fact) and with safe-outputs (which gates agent-requested write
  operations). Together: integrity filtering is the input layer; safe-outputs is the
  output layer. Both are required for a complete defense-in-depth harness for public
  repositories. For Ch03: document integrity filtering as the input restriction layer;
  safe-outputs as the output enforcement layer; Repo Assist as the triage layer that
  orchestrates the other two. Corroborates `docs-ghaw-examples-maintaining-repos.md`
  Claim 4 and `docs-ghaw-integrity-reference.md` Claim 1.

### Claim 6: Integrity filtering directly reduces token consumption as a dual security-and-cost mechanism — filtered items never appear in the agent's context window

- **Evidence**: The scaling strategies section states: "Integrity filtering directly
  reduces token consumption: items filtered by the gateway never appear in the agent's
  context window."
- **Confidence**: emerging (first-party claim; the connection is structurally correct
  given the filtering-before-context-assembly design, but no quantification is provided)
- **Quote**: "Integrity filtering directly reduces token consumption: items filtered by
  the gateway never appear in the agent's context window."
- **Our assessment**: The dual security + cost framing is new to the corpus relative to
  `docs-ghaw-integrity-reference.md`, which treats integrity filtering as a security
  mechanism. This source adds the cost optimization angle: for high-volume public repos
  where many low-integrity contributions arrive continuously, setting `min-integrity: approved`
  filters most noise before it reaches the AI engine — reducing both security risk and
  token spend. For Ch02: document integrity filtering as having dual purpose. For Ch05
  (Organization/Teams): use this framing when justifying integrity filtering adoption to
  cost-conscious stakeholders. Corroborates `docs-ghaw-examples-maintaining-repos.md`
  Claim 5.

### Claim 7: Reactions serve as trust signals to promote or demote content integrity without label management — enabled by `features.integrity-reactions: true`

- **Evidence**: The "Reactions as Trust Signals" subsection states: "Maintainers can use
  GitHub reactions to promote content past the integrity filter without modifying labels."
  This requires `integrity-reactions: true` in the workflow configuration.
- **Confidence**: emerging (first-party documentation; consistent with
  `docs-ghaw-integrity-reference.md` Claim 9, which documents the same feature as
  requiring v0.68.2+)
- **Quote**: "Maintainers can use GitHub reactions to promote content past the integrity
  filter without modifying labels."
- **Our assessment**: Reactions-as-trust-signals is the lowest-friction human-in-the-loop
  option for repo maintenance workflows processing untrusted contributions. Maintainers
  can use thumbs-up reactions to approve content for agent processing without managing a
  label system, which is lower operational overhead than `approval-labels` for high-volume
  public repos. For Ch02: recommend reactions-as-trust-signals as the lightweight HITL
  option for maintenance workflows processing untrusted contributions. Corroborates
  `docs-ghaw-examples-maintaining-repos.md` Claim 6 and `docs-ghaw-integrity-reference.md`
  Claim 9.

### Claim 8: Four scaling mechanisms enable high-volume public repository maintenance: per-user rate limiting (user-rate-limit), pre-activation skips (skip-author-associations), concurrency controls (max-parallel), and repository scoping (allowed-repos)

- **Evidence**: The "Scaling Strategies" section documents all four mechanisms: `user-rate-limit`
  with `max-runs-per-window` and `window` fields throttles per-user trigger frequency;
  `skip-author-associations` prevents workflow runs from starting for specified author
  associations before any agent infrastructure activates; `max-parallel` in the `concurrency:`
  block adjusts parallel processing; `tools.github.allowed-repos` restricts cross-repository
  reads. The page also includes guidance: "Match your production rate to your available
  review bandwidth."
- **Confidence**: emerging (first-party documentation; field behaviors are shown in YAML
  and consistent with `docs-ghaw-rate-limiting-controls.md`)
- **Quote**: "Match your production rate to your available review bandwidth."
- **Our assessment**: The four mechanisms operate at different cost and scope layers:
  (1) `skip-author-associations` prevents run activation entirely (zero infrastructure
  cost for filtered triggers); (2) `user-rate-limit` limits per-user frequency (reduces
  abuse patterns); (3) `max-parallel` caps concurrent processing (controls simultaneous
  AI inference costs); (4) `allowed-repos` scopes tool access (security + cost control).
  The `user-rate-limit` field uses v0.72.0+ naming conventions (`max-runs-per-window`
  rather than the deprecated `max-runs` from `docs-ghaw-rate-limiting-controls.md` Claim 8).
  For Ch02: document all four mechanisms as the scaling toolkit for high-volume repositories
  with their YAML syntax. Corroborates `docs-ghaw-examples-maintaining-repos.md` Claims 7, 8, 9.

### Claim 9: AI-assisted debugging via the Copilot CLI is the fastest root-cause path for failing maintenance workflows; the audit report covers failure summary, tool usage, MCP server health, firewall analysis, token metrics, and missing tools

- **Evidence**: The "Debugging Failed Workflows" section positions Copilot CLI as the
  primary debugging tool: "The fastest path to a root cause is to hand the failing run
  URL to the Copilot CLI." The audit report content: "The audit report covers: failure
  summary, tool usage, MCP server health, firewall analysis, token metrics, and missing
  tools."
- **Confidence**: emerging (first-party recommendation; the relative speed vs. manual
  audit is asserted, not benchmarked)
- **Quote**: "The fastest path to a root cause is to hand the failing run URL to the
  Copilot CLI."
- **Our assessment**: This is consistent with `docs-ghaw-troubleshooting-debugging.md`
  Claims 1 and 2, which document the same AI-assisted debugging pattern as the primary
  workflow for any agentic workflow failure. The five-step iterative debug loop
  (check UI → gh aw audit → Copilot CLI → modify+compile → comparative audit) gives
  practitioners a structured diagnostic sequence. The comparative audit step
  (`gh aw audit BASELINE_ID CURRENT_ID`) is especially useful for identifying which
  configuration change caused a regression. For Ch02: document the five-step workflow
  as standard operating procedure for any failing maintenance workflow. Corroborates
  `docs-ghaw-examples-maintaining-repos.md` Claim 10.

### Claim 10: Six failure pattern categories constitute the complete diagnostic taxonomy for maintenance workflow failures: missing tool calls, authentication failures, integrity filtering blocks, safe-output validation failures, token budget exhaustion, and network blocks

- **Evidence**: The "Common Failure Patterns" section names all six categories, each
  with diagnostic indicators and remediation steps.
- **Confidence**: emerging (first-party taxonomy derived from practical experience;
  presented as a complete classification but sourced from operational observation)
- **Quote**: (no direct single-sentence verbatim quote enumerating all six; categories
  are presented as a named set with per-category diagnostic indicators)
- **Our assessment**: The six-category taxonomy is the diagnostic checklist for any
  maintenance workflow failure. While individual failure types appear across multiple
  corpus notes (integrity filtering blocks in `docs-ghaw-integrity-reference.md` Claim 12;
  authentication failures and network blocks in `docs-ghaw-troubleshooting-debugging.md`
  Claims 7 and 8), this source presents all six as a coordinated taxonomy. Pair each
  category with its diagnostic command: `gh aw logs --filtered-integrity` for
  Category 3; `gh aw audit RUN_ID` for Categories 1, 4, 5, and 6. For Ch02: document
  the six categories as the diagnostic checklist for troubleshooting any maintenance
  workflow failure. Corroborates `docs-ghaw-examples-maintaining-repos.md` Claim 11.

## Concrete Artifacts

### Defense-in-Depth Overview (from source)

```
Two-mechanism defense-in-depth for public repositories:

Integrity filtering (INPUT LAYER):
  "keeps untrusted content out of the agent's context"
  → Evaluates author trust before context assembly
  → Repo Assist overrides to `unapproved` to see all incoming content
  → Downstream code-modifying agents use stricter thresholds

Safe-outputs (OUTPUT LAYER):
  "ensure the agent can only produce authorized side-effects"
  → Every GitHub mutation must be declared in safe-outputs: block
  → Runtime blocks undeclared operations before GitHub API
  → Eight enumerated types cover the full maintenance write surface
```

*Source: gh-aw guides/maintaining-repos (redirects to examples/maintaining-repos), overview section*

### Safe-Output Types for Repository Maintenance (from source)

```
Safe-output type         | Capability
------------------------ | -------------------------------------------
label-issue              | Apply or remove labels on an issue
comment-issue            | Post a comment on an issue
comment-pull-request     | Post a comment on a pull request
create-pull-request      | Open a new pull request
merge-pull-request       | Merge a pull request (EXPERIMENTAL)
close-issue              | Close an issue
create-issue             | Open a new issue
assign-issue             | Assign an issue to a user or team
```

*Source: gh-aw guides/maintaining-repos, "Controlling Workflow Outputs with Safe-Outputs" section*

### Scaling Mechanism YAML Configurations (from source)

```yaml
# Reactions as trust signals:
features:
  integrity-reactions: true
tools:
  github:
    min-integrity: approved

# Per-user rate limiting (v0.72.0+ field names):
user-rate-limit:
  max-runs-per-window: 5
  window: 60

# Pre-activation association skips:
on:
  issue_comment:
    types: [created]
  skip-author-associations:
    issue_comment: [owner, member, collaborator]

# Concurrency controls for parallel issue processing:
concurrency:
  max-parallel: 3

# Repository access scoping for monorepo / multi-repo:
tools:
  github:
    allowed-repos: "myorg/*"
    min-integrity: approved
```

*Source: gh-aw guides/maintaining-repos, Scaling Strategies section*

### CLI Commands for Debugging (from source)

```bash
# Single-run diagnosis:
gh aw audit RUN_ID
gh aw audit RUN_ID --json

# Multi-run trend analysis:
gh aw logs my-workflow
gh aw logs my-workflow --format markdown --count 20

# Integrity filtering diagnostics:
gh aw logs --filtered-integrity

# Regression comparison between runs:
gh aw audit BASELINE_ID CURRENT_ID

# Recompile after configuration changes:
gh aw compile
```

*Source: gh-aw guides/maintaining-repos, "Debugging Failed Workflows" section*

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

*Source: gh-aw guides/maintaining-repos, "Common Failure Patterns" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-examples-maintaining-repos.md` Claims 1–11 (same page content — the
    guides/maintaining-repos URL redirects to examples/maintaining-repos; all claims
    in this note directly corroborate the prior extraction from issue #876).
  - `docs-ghaw-integrity-reference.md` Claim 1 (integrity filtering manages access
    based on trust, not permissions): Claim 5 here corroborates the same filtering
    model and pre-context-assembly timing.
  - `docs-ghaw-integrity-reference.md` Claim 3 (four integrity levels: merged,
    approved, unapproved, none): Claim 5 enumerates the same four levels with
    consistent definitions.
  - `docs-ghaw-integrity-reference.md` Claim 4 (public repos auto-apply
    `min-integrity: approved`): consistent with Claim 2's note that downstream
    code-modifying agents use the default `approved` threshold.
  - `docs-ghaw-integrity-reference.md` Claim 9 (reaction-based endorsement from
    v0.68.2 via `features.integrity-reactions: true`): Claim 7 here corroborates
    the same feature in the repo maintenance context.
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (Safe Outputs MCP Gateway as
    "security-centric translation layer") and Claim 5 (SP2 Validation Precedence —
    validation before API invocation): Claim 3 here provides the practical
    "declare or be blocked" expression of these normative requirements.
  - `docs-ghaw-rate-limiting-controls.md` Claim 3 (dual concurrency control
    per-workflow and per-engine): Claim 8 here corroborates the dual enforcement
    model via the `max-parallel` configuration.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 1 (AI-assisted debugging via
    Copilot CLI as fastest path) and Claim 2 (three-step Copilot CLI workflow):
    Claim 9 here corroborates the same debugging recommendation in the repo-maintenance
    context.

- **Extends**:
  - `docs-ghaw-integrity-reference.md`: that reference covers integrity filtering as
    a security mechanism exclusively. Claim 6 here adds the dual cost-optimization
    framing — filtering reduces token consumption — which is not present in the
    reference note.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as pre-approved operations
    without write permissions): this note extends the base Safe Outputs model with
    the practical eight-type enumeration and the repo-maintenance operational context.
  - `docs-ghaw-rate-limiting-controls.md` Claim 8 (pre-v0.72.0 `rate-limit` field
    with `max` sub-key): this source uses v0.72.0+ field names (`user-rate-limit`,
    `max-runs-per-window`), confirming current naming conventions in platform
    documentation.

- **Contradicts**: None identified.

  **Note on field naming**: `docs-ghaw-rate-limiting-controls.md` uses pre-v0.72.0
  names (`rate-limit`, `max-runs`); this source uses v0.72.0+ names (`user-rate-limit`,
  `max-runs-per-window`). This is an API evolution documented in
  `blog-ghaw-weekly-2026-05-11.md` Claim 6 (PR #31390 breaking change), not a
  contradiction.

- **Novel**: All findings from this page that were novel to the corpus at the time
  of prior PR #705 are now documented in `docs-ghaw-examples-maintaining-repos.md`
  (issue #876, extracted 2026-05-25), which was mined from the redirect target. The
  guides/maintaining-repos URL now redirects to examples/maintaining-repos; the
  content is identical. No novel findings remain to add to the corpus from this
  source. The corpus-level novel contributions (Repo Assist triage layer, integrity
  filtering as cost optimization, `skip-author-associations`, AI-assisted debugging
  workflow, and six-category failure taxonomy) are all now in `docs-ghaw-examples-maintaining-repos.md`.

## Guide Impact

### Chapter 02: Harness Engineering

- **Repo Assist as triage layer** (Claim 2): Document the pattern — deploy Repo Assist
  first, configure downstream code-modifying agents as consumers of its routing decisions.
  Note the integrity filtering override: Repo Assist operates at `unapproved` to see all
  incoming content; downstream agents use the stricter `approved` default on public repos.

- **Scaling toolkit for high-volume public repositories** (Claim 8): Document all four
  mechanisms with their YAML syntax — `user-rate-limit`, `skip-author-associations`,
  `max-parallel`, `allowed-repos`. Frame these as a multi-layer scaling strategy
  operating at different cost points: pre-activation (zero cost) → per-user throttle
  → concurrency cap → tool scoping.

- **Update rate-limiting field names to v0.72.0+** (Claim 8): All harness template
  examples should use `user-rate-limit`/`max-runs-per-window` rather than the deprecated
  `rate-limit`/`max-runs`. The `docs-ghaw-rate-limiting-controls.md` source note uses
  pre-v0.72.0 names that should be updated in guide examples.

- **Document the five-step iterative debug workflow** (Claim 9): The `check UI →
  gh aw audit → copilot CLI → modify+compile → comparative audit` loop is standard
  operating procedure for any failing gh-aw workflow.

### Chapter 03: Safety and Verification

- **Defense-in-depth framing for public repositories** (Claim 1): Add the trust-surface
  challenge as the opening rationale for requiring the two-mechanism defense: integrity
  filtering (input layer) + safe-outputs (output layer). This is more specific than the
  general five-layer model in `docs-ghaw-how-they-work.md` — it names the concrete
  public-repo threat and the two mechanisms that address it.

- **Integrity filtering as dual security-and-cost mechanism** (Claim 6): When
  recommending integrity filtering, note both benefits: security (prevents prompt
  injection via untrusted content) and cost (reduces context window size). The dual
  framing is more persuasive for mixed security/cost audiences than security alone.

## Extraction Notes

1. **URL redirect discovered**: The source URL `https://github.github.com/gh-aw/guides/maintaining-repos`
   redirects (HTTP 301) to `https://github.github.com/gh-aw/examples/maintaining-repos`.
   The canonical content for this URL is at the examples path.

2. **Content already in corpus**: `docs-ghaw-examples-maintaining-repos.md` (issue #876,
   extracted 2026-05-25) provides a comprehensive prior extraction of the redirect target
   with 11 claims and extensive YAML artifacts. All novel findings from this page are
   already documented in the corpus. This note provides the formal source attribution for
   issue #437's URL and cross-reference coverage for the guides path.

3. **Previous PR #705 closed for technical reasons**: A prior Miner PR for this issue
   was closed on 2026-05-24 due to a GitHub dispatch-rate-limit pipeline issue (not a
   content problem). The Assayer had approved depth, accuracy, and completeness for that
   PR; the only rejection was one incorrect cross-reference: the Extends section cited
   `docs-ghaw-central-repo-ops.md` Claim 2 for "Repo Assist as the triage layer." That
   Claim 2 is actually about fan-out blast radius control via `max: 5` in
   `safe-outputs.dispatch-workflow` — unrelated to Repo Assist. This note corrects that
   error: the Extends section does not cite `docs-ghaw-central-repo-ops.md`. The Repo
   Assist triage-layer finding is documented in `docs-ghaw-examples-maintaining-repos.md`
   Claim 1 and corroborated in Claim 2 of this note.

4. **No contradictions filed**: Reviewed all existing gh-aw source notes. No claim in
   this source materially opposes any existing source note at the MINER.md §4a threshold.
   The `user-rate-limit`/`rate-limit` naming difference is an API evolution (v0.72.0
   breaking change), not a substantive contradiction. No contradiction issue required.

5. **Related pages not followed**: The page links to multiple reference documents
   (safe outputs, integrity filtering, rate limiting, debugging, network configuration).
   All are already covered by dedicated source notes in the corpus. No sub-pages followed.
