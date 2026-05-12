---
source_url: https://github.github.com/gh-aw/guides/maintaining-repos
source_type: docs
title: "GitHub Agentic Workflows: Maintaining Repos (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#437"
---

# GitHub Agentic Workflows: Maintaining Repos (Guides)

> The practitioner guide for open-source repo maintainers running agentic
> workflows — uniquely frames repository maintenance safety as two coordinated
> mechanisms (safe-outputs controls what the agent *does*; integrity filtering
> controls what the agent *sees*), introduces Repo Assist as the recommended
> lightweight triage entry point for public repositories, documents a
> six-pattern failure table specific to maintaining-repo workflows, and
> establishes integrity filtering as a token-cost control — not just a
> security control.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/maintaining-repos`
  page — in the "Guides" section, which provides practitioner how-to guidance
  rather than architectural reference or pattern descriptions. The `guides/`
  section targets workflow authors solving concrete operational problems.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the `gh
  aw` platform. Claims about safe-output runtime enforcement, integrity filtering
  defaults, and rate limiting behavior are authoritative platform facts.
- **Scope**: Covers the specific challenges of running agentic workflows in
  public open-source repositories: the trust problem (anyone can open issues
  or PRs), the two-mechanism safety model (safe-outputs + integrity filtering),
  Repo Assist as a triage pattern, scaling strategies (token budgets, rate
  limiting, concurrency), and workflow debugging (AI-assisted + manual CLI
  commands + a six-failure-pattern reference table). Does NOT cover: the formal
  Safe Outputs MCP Gateway specification (see `docs-ghaw-safe-outputs-specification.md`),
  the full integrity filtering configuration reference (see
  `docs-ghaw-integrity-reference.md`), multi-repo orchestration patterns (see
  `docs-ghaw-central-repo-ops.md`), or the general five-layer security
  architecture (see `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: Repository maintenance safety requires two coordinated mechanisms — safe-outputs controls what the agent *does*, and integrity filtering controls what the agent *sees*

- **Evidence**: The page opens by naming both mechanisms in parallel and stating
  their roles explicitly: "Safe-outputs is the primary mechanism for controlling
  what a workflow can do." and "Integrity filtering is the primary mechanism for
  controlling what content the agent sees." The framing is that maintaining a
  public repo involves untrusted contributors who can open issues or PRs;
  both mechanisms are needed together to address different attack surfaces.
- **Confidence**: settled (first-party documentation; this dual-mechanism
  framing is a deliberate architectural statement, not incidental)
- **Quote**: "Safe-outputs is the primary mechanism for controlling what a
  workflow can do."
- **Our assessment**: This is the most important framing contribution of this
  page. Prior corpus sources (`docs-ghaw-how-they-work.md`,
  `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-integrity-reference.md`)
  document each mechanism independently. This guide is the first source to
  explicitly position them as a coordinated pair with complementary roles:
  safe-outputs as the *output boundary* (what the agent is permitted to write)
  and integrity filtering as the *input boundary* (what untrusted content the
  agent is permitted to see). For Ch03 (Safety and Verification): this dual-
  mechanism framing is the synthesis practitioners need. Neither mechanism alone
  is sufficient — an agent with no safe-outputs restriction can write arbitrary
  GitHub state even if its inputs are filtered; an agent with no integrity
  filtering might process a prompt-injection payload even if its outputs are
  controlled.

### Claim 2: Repo Assist is a named, recommended workflow pattern that runs on every new issue or PR and acts as a lightweight triage gateway for downstream code-modifying agents

- **Evidence**: The page describes Repo Assist explicitly: "Repo Assist is a
  workflow that runs on every new issue or PR, classifies the content, and
  routes work to the right place." The stated advantages of using it as the
  entry point for public repositories: it "Sees all incoming content (including
  from untrusted users)", "Applies lightweight, low-cost classification (labels,
  comments)", and "Acts as a gate that downstream code-modifying agents depend
  on."
- **Confidence**: emerging (first-party documentation; the pattern is named and
  its role is described, but no performance metrics or failure-rate data is
  provided)
- **Quote**: "Repo Assist is a workflow that runs on every new issue or PR,
  classifies the content, and routes work to the right place."
- **Our assessment**: Repo Assist is a named architectural pattern for the
  "first-touch" agent in a public repository. Its design is deliberately
  asymmetric: it runs for *everyone* (including untrusted users) but performs
  only lightweight, low-cost operations (labels and comments — not code
  changes). Downstream agents with higher blast radius (code-modifying,
  PR-creating) can then depend on Repo Assist's classifications as a trust
  signal. This creates a two-tier architecture: wide-open triage at the
  perimeter, restricted execution in the interior. For Ch02 (Harness
  Engineering): Repo Assist is the named starting point for any team deploying
  agentic workflows on a public repository. It is the correct first workflow
  to build before deploying code-modifying agents. For Ch03: the gateway
  pattern is a practical application of defense-in-depth — the triage agent
  has minimal permissions and minimal blast radius; the code-modifying agents
  are only reached via the triage gate.

### Claim 3: Safe-outputs enforces output control by blocking any GitHub side-effect that is not explicitly declared in the `safe-outputs:` block — before the action reaches the API

- **Evidence**: The page states: "Every action that produces a side-effect on
  GitHub — labeling an issue, posting a comment, opening a pull request,
  merging — must be explicitly declared in the `safe-outputs:` block." The
  enforcement point: "If an action isn't listed, the runtime blocks it before
  it reaches the API."
- **Confidence**: settled (first-party documentation; this is the normative
  behavioral description of the mechanism, consistent with AR1 in
  `docs-ghaw-safe-outputs-specification.md`)
- **Quote**: "Every action that produces a side-effect on GitHub — labeling an
  issue, posting a comment, opening a pull request, merging — must be
  explicitly declared in the `safe-outputs:` block."
- **Our assessment**: The "before it reaches the API" enforcement point is
  architecturally important: it means there is no window in which an unlisted
  action can be attempted and then caught — the runtime validates the
  declaration and blocks non-compliant actions before any GitHub API call is
  made. This is consistent with SP2 (Validation Precedence Invariant) from
  `docs-ghaw-safe-outputs-specification.md` Claim 5, which requires "validation
  logic MUST execute before any GitHub API invocation." The guide also enumerates
  eight available safe-output types for maintaining repos (see Concrete
  Artifacts). For Ch03: "before it reaches the API" is the key phrase for
  practitioners who want to understand the enforcement boundary — the agent
  cannot "try" an unlisted operation and have it silently dropped; it is
  blocked at declaration time.

### Claim 4: Public repositories automatically receive `min-integrity: approved` protection as a baseline without any configuration required

- **Evidence**: The guide states directly: "Every public repository automatically
  applies `min-integrity: approved` as a baseline." The integrity levels table
  confirms that `approved` level covers owners, members, collaborators, non-fork
  PRs on public repos, and recognized bots; content from first-time or anonymous
  contributors would be filtered by default.
- **Confidence**: settled (first-party documentation; this corroborates Claim 4
  in `docs-ghaw-integrity-reference.md` exactly)
- **Quote**: "Every public repository automatically applies `min-integrity:
  approved` as a baseline."
- **Our assessment**: This default makes integrity filtering the secure-by-default
  posture for public repos without any configuration. In the maintaining-repos
  context, this means that a maintainer can deploy a Repo Assist workflow on a
  public repository and immediately benefit from filtering: issues and PRs from
  first-time contributors, external accounts, and users with no prior association
  will not reach the AI engine's context unless the maintainer explicitly lowers
  the threshold. The guide positions this as "protecting public workflows without
  additional authentication" — a zero-configuration security baseline. For Ch02:
  document this default explicitly so maintainers know the out-of-the-box
  protection level; teams that want to process content from first-time
  contributors must explicitly lower to `min-integrity: unapproved` or use
  `approval-labels` as a human-review gate.

### Claim 5: Integrity filtering is also a token-cost control — filtering untrusted content prevents it from appearing in agent context windows, directly reducing token consumption

- **Evidence**: The "Token Budget Awareness" subsection of the scaling strategies
  section states that integrity filtering reduces token consumption by preventing
  filtered items from appearing in agent context windows. The practical guidance:
  "Use `gh aw logs --format markdown --count 20` to track token trends over time."
- **Confidence**: emerging (first-party framing; the token reduction benefit is
  stated without quantification)
- **Quote**: (no direct quote capturing the full token-cost framing; see paraphrase
  in Our assessment)
- **Our assessment**: This reframes integrity filtering from a security mechanism
  (keep untrusted content out of the AI engine) to a cost mechanism (reduce the
  token volume processed per run). On a high-traffic open-source repository,
  filtering first-time contributors reduces the number of items the agent
  processes per workflow run — which directly reduces token consumption,
  especially for triage workflows that enumerate many issues or PRs. The
  practical implication: `min-integrity` level selection is not just a security
  decision; it is also a cost optimization. Tightening `min-integrity` on a
  noisy public repo can significantly reduce token expenditure. The `gh aw logs
  --format markdown --count 20` command is the recommended tool for monitoring
  token trends over time. For Ch02: add this cost-control framing when
  introducing integrity filtering — it is the "why bother for small repos"
  motivation beyond security. Corroborates `docs-ghaw-how-they-work.md` Claim
  11 (the best practice workflow includes `gh aw logs` for cost monitoring).

### Claim 6: The `user-rate-limit` frontmatter key prevents workflow execution floods by capping runs per user per sliding window

- **Evidence**: The "Rate Limiting" subsection states: "The `user-rate-limit`
  frontmatter key caps how many times a workflow can run in a sliding window."
  The documented configuration shows `max-runs-per-window: 5` and `window: 60`
  as example values.
- **Confidence**: emerging (first-party documentation; the field name
  `user-rate-limit` differs from the `rate-limit` field name documented in
  `docs-ghaw-rate-limiting-controls.md` — see Extraction Notes)
- **Quote**: "The `user-rate-limit` frontmatter key caps how many times a
  workflow can run in a sliding window."
- **Our assessment**: Per-user rate limiting is the direct defense against
  the open-source repo threat model described in the page's introduction: any
  user can open issues or PRs, consuming workflow execution and token budget.
  Without a rate limit, a coordinated flood of issues can exhaust the team's AI
  quota. The maintaining-repos context highlights this risk more clearly than
  the rate-limiting reference (which describes the mechanism without the
  open-source motivation). The `user-rate-limit` field name diverges from the
  `rate-limit` field documented in `docs-ghaw-rate-limiting-controls.md` — see
  Extraction Notes for the discrepancy. For Ch03: document rate limiting as the
  flood-prevention primitive specifically in the open-source context, not just
  as a generic runaway control. The "any user can trigger" threat is specific to
  public repositories.

### Claim 7: Workflows can increase concurrency for high-throughput triage using `max-parallel` under the `concurrency:` key

- **Evidence**: The "Concurrency Controls" subsection states: "Workflows
  automatically use dual concurrency control (per-workflow and per-engine)."
  For repo-assist workflows, the page documents that higher concurrency enables
  parallel triage, with the example key `concurrency: max-parallel: 3`.
- **Confidence**: settled (first-party documentation; the dual concurrency model
  is consistent with `docs-ghaw-rate-limiting-controls.md` Claim 3; `max-parallel`
  is documented as a supported override)
- **Quote**: "Workflows automatically use dual concurrency control (per-workflow
  and per-engine)."
- **Our assessment**: The insight here is the context-specific recommendation:
  for *triage workflows* like Repo Assist (which are lightweight and process
  many items), increasing `max-parallel` improves throughput without significant
  blast-radius risk (triage only labels and comments, not modifies code). For
  *code-modifying workflows*, higher concurrency increases risk. The per-engine
  singleton prevents AI resource over-consumption even if `max-parallel` is high.
  For Ch02: the `max-parallel` tuning decision should be presented as risk-
  proportional: lightweight triage workflows can handle higher parallelism;
  code-modifying workflows should stay at the conservative default.

### Claim 8: The `allowed-repos` configuration scopes cross-repository reads to prevent agents from accessing repositories outside their intended scope

- **Evidence**: The "Scoping Repository Access" subsection documents:
  ```
  tools:
    github:
      allowed-repos: "myorg/*"
      min-integrity: approved
  ```
  The `allowed-repos` key restricts cross-repository reads to a pattern.
- **Confidence**: settled (first-party documentation; `allowed-repos` is
  consistent with the configuration field documented in `docs-ghaw-integrity-reference.md`)
- **Quote**: (no direct prose quote; the YAML block is the evidence — see
  Concrete Artifacts)
- **Our assessment**: The combination of `allowed-repos` scoping and `min-integrity`
  in the same `tools.github:` block is the practical security configuration for
  multi-repo maintaining-repo workflows. In the maintaining-repos context, a
  Repo Assist workflow might read content from related repositories (e.g., to
  detect duplicate issues across repos) — `allowed-repos` ensures the agent
  cannot read beyond the organization's own repos. This is distinct from the
  Safe Outputs cross-repository restriction (which controls where the agent can
  *write*). For Ch02: document `allowed-repos` as the read-scoping complement
  to `safe-outputs.target-repo` write-scoping — both are needed for full
  cross-repo access control.

### Claim 9: A six-pattern failure table provides the specific symptoms, causes, and fixes for the most common maintaining-repo workflow failures

- **Evidence**: The debugging section documents a six-row failure reference
  table with columns for failure type, symptom/cause, and recommended fixes.
  The table covers: Missing tool calls, Authentication failures, Integrity
  filtering blocking, Safe-output validation failures, Token budget exhaustion,
  and Network blocks. For safe-output validation failures, it specifically
  references checking `safe_outputs.jsonl` in artifacts — a debugging artifact
  not documented in other source notes.
- **Confidence**: emerging (first-party documentation; the patterns are
  prescriptive; failure frequency data is not provided)
- **Quote**: (no single prose quote; the table is the evidence — see Concrete
  Artifacts)
- **Our assessment**: The `safe_outputs.jsonl` artifact reference is the most
  novel debugging detail in this table — it is not mentioned in
  `docs-ghaw-troubleshooting-debugging.md` or `docs-ghaw-safe-outputs-specification.md`.
  If a workflow's safe-output operations are not executing as expected, the
  `safe_outputs.jsonl` file in the run's artifacts contains the structured
  record of what the agent attempted to write. The Token budget exhaustion row
  is also notable: it lists four mitigations in priority order (raise
  `min-integrity`, add `cache-memory:`, simplify prompt, tighten
  `user-rate-limit`) — framing `min-integrity` as the most direct cost control.
  For Ch05 (Observability): include this table as the first-response reference
  for maintaining-repo workflow debugging. The `safe_outputs.jsonl` artifact
  reference warrants a separate call-out.

### Claim 10: The recommended debugging cycle for maintaining-repo workflows is a five-step iterative loop: check summary → audit run → AI-assist for complex issues → recompile → compare baseline

- **Evidence**: The page documents a numbered five-step process: (1) check
  workflow run summary in GitHub Actions UI, (2) execute `gh aw audit RUN_ID`
  for structured breakdown, (3) use `/agent agentic-workflows` in Copilot Chat
  for complex issues, (4) edit `.md` file → run `gh aw compile` for validation
  → trigger new run, (5) compare new run against baseline using
  `gh aw audit BASELINE_ID NEW_ID`. The AI-assisted step explicitly positions
  Copilot as the escalation for issues that don't resolve via structured CLI
  output alone.
- **Confidence**: emerging (first-party prescriptive guidance; no data on what
  fraction of issues each step resolves)
- **Quote**: (no single prose quote; the procedure is a numbered list — see
  Concrete Artifacts)
- **Our assessment**: This five-step cycle is the maintaining-repos specific
  integration of the debugging tools documented independently in
  `docs-ghaw-troubleshooting-debugging.md`. The ordering matters: start with
  the structured output (audit CLI), escalate to AI assistance for complex
  cases, then recompile and compare — the AI assistant step is positioned as a
  middle tier between structured CLI tools and starting from scratch. The
  baseline comparison step (step 5) is particularly valuable for maintaining-
  repo workflows that run repeatedly: comparing two runs of the same workflow
  detects behavioral regressions introduced by a workflow change. For Ch05:
  add this as the maintaining-repo debugging workflow. Cross-reference
  `docs-ghaw-troubleshooting-debugging.md` for the full audit command reference.

## Concrete Artifacts

### Two-Mechanism Safety Overview (from source page)

```
Mechanism 1: Safe-outputs
  Role: Controls what the agent can DO
  Quote: "Safe-outputs is the primary mechanism for controlling what a
          workflow can do."
  How: "Every action that produces a side-effect on GitHub — labeling an
        issue, posting a comment, opening a pull request, merging — must be
        explicitly declared in the safe-outputs: block."
  Enforcement: "If an action isn't listed, the runtime blocks it before it
                reaches the API."

Mechanism 2: Integrity filtering
  Role: Controls what the agent can SEE
  Quote: "Integrity filtering is the primary mechanism for controlling what
          content the agent sees."
  How: "It evaluates the author of each issue, PR, or comment and removes
        items that don't meet the configured trust threshold."
  Default: "Every public repository automatically applies min-integrity:
             approved as a baseline."
```

*Source: gh-aw guides/maintaining-repos, opening section*

### Safe-Output Types Available for Maintaining-Repos Workflows (from source)

```
Safe-output              | What it allows
------------------------ | ----------------------------------------
label-issue              | Apply or remove labels on an issue
comment-issue            | Post a comment on an issue
comment-pull-request     | Post a comment on a pull request
create-pull-request      | Open a new pull request
merge-pull-request       | Merge a pull request (experimental)
close-issue              | Close an issue
create-issue             | Open a new issue
assign-issue             | Assign an issue to a user or team
```

*Source: gh-aw guides/maintaining-repos, "Controlling Workflow Outputs with
Safe-Outputs" section*

### Integrity Levels for Maintaining-Repos Context (from source)

```
Level      | Who qualifies
---------- | ---------------------------------------------------------------
merged     | PRs merged into the default branch; commits reachable from main
approved   | Owners, members, collaborators; non-fork PRs on public repos;
           | recognized bots
unapproved | Contributors who have had a PR merged before; first-time
           | contributors
none       | All content including users with no prior relationship
```

*Source: gh-aw guides/maintaining-repos, "Controlling Workflow Inputs with
Integrity Filtering" section*

### Scaling Configuration Examples (from source)

```yaml
# Token budget monitoring:
# "Use `gh aw logs --format markdown --count 20` to track token trends over time."

# Rate limiting (flood prevention):
user-rate-limit:
  max-runs-per-window: 5
  window: 60

# Concurrency (higher parallelism for triage):
concurrency:
  max-parallel: 3

# Repository access scoping (cross-repo read restriction):
tools:
  github:
    allowed-repos: "myorg/*"
    min-integrity: approved

# Reaction-based trust endorsement:
features:
  integrity-reactions: true
tools:
  github:
    min-integrity: approved
```

*Source: gh-aw guides/maintaining-repos, "Scaling Strategies" section*

### Six-Pattern Failure Reference Table (from source)

```
Failure                      | Symptom/Cause                              | Fixes
---------------------------- | ------------------------------------------ | ---------------------------------------------
Missing tool calls           | Tool not configured or incorrectly named   | Add to tools: block; fix safeoutputs prefix;
                             |                                            | check MCP connectivity
Authentication failures      | Insufficient token permissions or missing  | Review permissions: block; ensure secrets
                             | API keys                                   | configured; check Auth Reference
Integrity filtering blocking | Author association below min-integrity     | Adjust min-integrity; add author to
                             | threshold                                  | trusted-users; use approval-labels
Safe-output validation       | Agent attempted undeclared GitHub action   | Review safe-outputs:; check safe_outputs.jsonl
failures                     |                                            | in artifacts
Token budget exhaustion      | Run hit token limit before completion      | Raise min-integrity; add cache-memory:;
                             |                                            | simplify prompt; tighten user-rate-limit
Network blocks               | Required domain blocked by firewall        | Check firewall section of audit; add domain
                             |                                            | to network.allowed
```

*Source: gh-aw guides/maintaining-repos, "Common Failure Patterns" section*

### AI-Assisted Debugging Commands (from source)

```bash
# Copilot CLI (local):
copilot
# Inside CLI:
/agent agentic-workflows
Debug this run: https://github.com/OWNER/REPO/actions/runs/RUN_ID

# GitHub.com (with agentic authoring enabled):
/agent agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID
```

*Source: gh-aw guides/maintaining-repos, "Debugging: AI-Assisted" section*

### Manual Debugging CLI Commands (from source)

```bash
# Audit a specific run (structured breakdown):
gh aw audit RUN_ID
gh aw audit RUN_ID --json
gh aw audit RUN_ID --parse

# Compare two runs for behavioral regressions:
gh aw audit BASELINE_ID CURRENT_ID

# Analyze logs for a workflow:
gh aw logs my-workflow
gh aw logs my-workflow --format markdown --count 10

# Download only runs with integrity-filtered content:
gh aw logs --filtered-integrity
```

*Source: gh-aw guides/maintaining-repos, "Manual Debugging with CLI Commands"
section*

### Five-Step Iterative Debug Cycle (from source)

```
1. Check workflow run summary in GitHub Actions UI
2. Execute `gh aw audit RUN_ID` for structured breakdown
3. Use `/agent agentic-workflows` in Copilot Chat for complex issues
4. Edit .md file → run `gh aw compile` for validation → trigger new run
5. Compare new run against baseline: gh aw audit BASELINE_ID NEW_ID
```

*Source: gh-aw guides/maintaining-repos, "Iterative Debug Workflow" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as "pre-approved actions
    the AI can request without write permissions"): Claim 3 here is the
    practical guide-level restatement of the same mechanism, adding the
    key enforcement detail that unlisted actions are blocked "before it reaches
    the API" — matching SP2 (Validation Precedence Invariant) in
    `docs-ghaw-safe-outputs-specification.md` Claim 5.
  - `docs-ghaw-integrity-reference.md` Claim 1 (integrity filtering manages
    access based on trust, not permissions): Claim 1 and Claim 4 here corroborate
    the integrity reference. This page provides the public-repo maintainer context
    for *why* the distinction matters: in a public repo, the permissions model
    doesn't filter external contributors — integrity filtering does.
  - `docs-ghaw-integrity-reference.md` Claim 4 (public repos auto-apply
    `min-integrity: approved`): Claim 4 here states the identical default,
    providing the second primary-source confirmation. Both are first-party gh-aw
    documentation.
  - `docs-ghaw-integrity-reference.md` Claim 12 (`gh aw logs --filtered-integrity`
    for targeted investigation): Claim 5 here references the same command for
    token trend monitoring; together the two notes establish that this command
    serves both cost observability and security investigation purposes.
  - `docs-ghaw-rate-limiting-controls.md` Claim 3 (dual concurrency control:
    per-workflow and per-engine): Claim 7 here restates the same dual model,
    adding the `max-parallel` override for triage workflows as the
    maintaining-repos specific tuning recommendation.
  - `docs-ghaw-troubleshooting-debugging.md` Claims 1–2 (AI-assisted Copilot
    CLI debugging as primary recommended approach): Claim 10's five-step cycle
    positions the Copilot CLI as Step 3 (escalation for complex issues), which
    is consistent with the debugging guide positioning it as the "fastest path
    to a root cause." The maintaining-repos guide integrates it into a broader
    iterative cycle rather than presenting it as a standalone first-response.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 4 (`gh aw audit` for
    comprehensive run breakdown): the manual debugging commands here (Concrete
    Artifacts) reproduce the same `gh aw audit RUN_ID` variants, confirming
    consistency across both documentation pages.
  - `docs-ghaw-how-they-work.md` Claim 11 (best practice workflow includes
    `gh aw logs` for cost monitoring): Claim 5 here independently identifies
    `gh aw logs --format markdown --count 20` as the token-trend monitoring
    command for the maintaining-repos context. Both sources agree on `gh aw logs`
    as the cost observability tool.

- **Extends**:
  - `docs-ghaw-how-they-work.md` and `docs-ghaw-safe-outputs-specification.md`:
    those notes cover safe-outputs as a security and permission-separation
    mechanism. Claim 1 here extends the framing by explicitly positioning
    safe-outputs + integrity filtering as a *coordinated pair* — the first
    source in the corpus to state this pairing as an architectural design
    principle, not just two independently useful features.
  - `docs-ghaw-integrity-reference.md`: that reference covers the full
    eleven-field configuration surface. Claims 4 and 5 here extend by showing
    the *cost* rationale for integrity filtering — a framing absent from the
    reference page, which focuses on security and trust computation.
  - `docs-ghaw-troubleshooting-debugging.md`: that page covers the Copilot CLI
    debugging workflow and `gh aw audit` in full depth. This guide extends the
    debugging coverage with: (a) a six-failure-pattern table tailored to
    maintaining-repo workflows; (b) the `safe_outputs.jsonl` artifact reference
    for safe-output debugging (not in any other note); (c) the five-step
    iterative debug cycle as a structured workflow rather than a reference-style
    tool description.
  - `docs-ghaw-central-repo-ops.md` Claim 2 (Repo Assist as the triage layer):
    that note mentions Repo Assist in the context of a large-scale orchestration
    pattern. This guide is the first source to document Repo Assist as a named
    standalone entry-point pattern for any public repository, regardless of
    scale — available to small open-source projects, not just enterprise
    orchestration.

- **Contradicts**: None identified beyond the field-name discrepancy noted in
  Extraction Notes. No existing source note makes claims that oppose the
  dual-mechanism framing, the Repo Assist pattern, the integrity filtering
  defaults, or the debugging recommendations.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Dual-mechanism coordination framing** (Claim 1): No existing source note
    explicitly frames safe-outputs and integrity filtering as a coordinated pair
    with complementary roles (output boundary + input boundary). The existing
    notes cover each mechanism independently. This is the first source to name
    the pairing as the safety model for open-source repo maintenance.
  - **Repo Assist as a named standalone triage pattern** (Claim 2): While
    `docs-ghaw-central-repo-ops.md` mentions Repo Assist in passing, this is
    the first source to document it as a named, recommended starting pattern for
    any public repository — with its design rationale (sees all content, applies
    only lightweight actions, acts as a gate for downstream agents).
  - **Integrity filtering as token-cost control** (Claim 5): No other source in
    the corpus frames `min-integrity` level selection as a cost optimization. The
    integrity reference (`docs-ghaw-integrity-reference.md`) and the rate-limiting
    reference cover the security rationale; this page adds the cost-reduction
    rationale and names `gh aw logs --format markdown --count 20` as the
    monitoring command.
  - **`safe_outputs.jsonl` artifact for safe-output debugging** (Claim 9): This
    artifact reference does not appear in `docs-ghaw-troubleshooting-debugging.md`,
    `docs-ghaw-safe-outputs-specification.md`, or any other source note. It is
    the specific file to inspect when safe-output operations are not executing
    as expected.
  - **Six-pattern failure table for maintaining-repo workflows** (Claim 9):
    The combination of failure types, symptoms, and fixes presented as a
    structured table — with the maintaining-repo context (integrity blocking,
    token budget exhaustion, rate-limit consequences) — is new to the corpus.
    The token-exhaustion mitigations (raise `min-integrity` first, then
    `cache-memory:`, then prompt simplification, then `user-rate-limit`) provide
    a prioritized recovery path not documented elsewhere.
  - **Five-step iterative debug cycle** (Claim 10): The structured five-step
    cycle (check → audit → AI-assist → recompile → baseline-compare) as a
    workflow for maintaining-repos debugging is new. Prior notes document
    individual tools; this page sequences them into an iterative procedure.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add dual-mechanism pattern as the canonical safety model for public-facing
  workflows** (Claim 1): Ch02 currently covers safe-outputs and integrity
  filtering independently. Add a synthesis section that presents them as a
  coordinated pair: safe-outputs for output control + integrity filtering for
  input control. The framing: "what can the agent do?" (safe-outputs) and "what
  can the agent see?" (integrity filtering) — both must be configured for a
  complete public-repo safety posture.

- **Add Repo Assist as the recommended first workflow for public repositories**
  (Claim 2): Before recommending code-modifying workflows on public repos,
  recommend deploying a Repo Assist workflow first. The design rationale: it
  processes all incoming content (broad reach), applies only low-blast-radius
  actions (labels, comments), and creates the trust signals that downstream
  agents can consume. Document the two-tier architecture: wide-open triage at
  the perimeter, restricted execution in the interior.

- **Document `allowed-repos` + `min-integrity` as the cross-repo read scoping
  pair** (Claim 8): When introducing `tools.github:` configuration, document
  `allowed-repos` and `min-integrity` as the two access restrictions for the
  read path — separate from the write-path restrictions in `safe-outputs:`.

### Chapter 03: Safety and Verification

- **Frame the dual-mechanism model as the open-source safety architecture**
  (Claim 1): For public repositories, Ch03's safety architecture section should
  explain that two boundaries are needed: the output boundary (safe-outputs:
  agent requests declared operations through the safe-outputs gateway) and the
  input boundary (integrity filtering: untrusted content is removed before
  reaching the AI engine). Each boundary defends against different attacks:
  output boundary prevents unauthorized writes; input boundary prevents prompt
  injection via untrusted issues and PRs.

- **Document `user-rate-limit` (or `rate-limit`) as the flood-prevention
  control specifically for public repos** (Claim 6): The open-source threat
  model is explicit here: anyone can open issues, consuming workflow execution
  and AI token budget. Per-user rate limiting is the targeted defense.

### Chapter 05: Observability and Feedback Loops

- **Add the five-step debug cycle as the maintaining-repo debugging workflow**
  (Claim 10): check summary → audit (`gh aw audit`) → AI-escalate → recompile
  → baseline-compare. Include the specific Copilot CLI command for the
  AI-escalation step.

- **Add the six-pattern failure table as the first-response debugging
  reference** (Claim 9): Include the table from Concrete Artifacts. Highlight
  the `safe_outputs.jsonl` artifact path for safe-output debugging — this is
  not documented elsewhere in the corpus and is the correct artifact to inspect
  when safe-output operations fail silently.

- **Document integrity filtering's cost-monitoring benefit** (Claim 5): Frame
  `gh aw logs --format markdown --count 20` as the token-trend monitoring
  command for public-repo workflows, and explain that raising `min-integrity`
  is the highest-leverage cost reduction lever for high-traffic repositories.

## Extraction Notes

1. **Field name discrepancy: `user-rate-limit` vs. `rate-limit`**: The
   maintaining-repos page uses `user-rate-limit:` with sub-key
   `max-runs-per-window:`, while `docs-ghaw-rate-limiting-controls.md` documents
   a field named `rate-limit:` with sub-key `max:`. Both describe per-user
   sliding-window rate limiting, and both produce the same guide advice. The
   discrepancy may reflect different document versions, a field rename, or the
   same mechanism surfaced under different names in different doc sections. This
   is noted here for Assayer verification; no contradiction issue is filed
   because the guide impact is identical.

2. **`safe_outputs.jsonl` not in prior corpus notes**: The six-failure-pattern
   table references `safe_outputs.jsonl` in artifacts as the debugging artifact
   for safe-output validation failures. This file path does not appear in
   `docs-ghaw-troubleshooting-debugging.md`, `docs-ghaw-safe-outputs-specification.md`,
   or any other existing source note. It is treated as a first-occurrence claim
   (Novel section). Assayer should verify against the source URL.

3. **Source is an Astro/Starlight SPA**: WebFetch was used twice — once for
   comprehensive content extraction, once for verbatim quote extraction. The
   failure patterns table, safe-output types table, and integrity levels table
   were captured verbatim from the second fetch. CLI commands in the Concrete
   Artifacts section are reproduced character-for-character. Prose passages
   marked as quotes appear consistent across both fetches.

4. **Sub-pages not followed**: The page links to companion reference pages
   (Safe Outputs Reference, Integrity Filtering Reference, Rate Limiting
   Controls, Audit Commands, Debugging Workflows, Network Configuration Guide,
   GitHub Tools Reference). All of these are already covered in the corpus by
   dedicated source notes. No additional sub-pages were followed.

5. **No publication date**: The documentation does not carry an explicit
   publication date. `date_published` left null. Content is consistent with
   the current gh-aw platform state, including the `integrity-reactions` feature
   (v0.68.2+) documented in `docs-ghaw-integrity-reference.md` Claim 9.

6. **No contradictions filed**: Reviewed all existing source notes with
   overlapping coverage (safe-outputs, integrity filtering, rate limiting,
   debugging). No claims in this source materially oppose existing notes. The
   `user-rate-limit` vs. `rate-limit` discrepancy is flagged in Extraction
   Notes 1 above but does not meet the contradiction threshold (different
   guide advice required).
