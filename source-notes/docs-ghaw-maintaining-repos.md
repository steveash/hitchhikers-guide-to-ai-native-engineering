---
source_url: https://github.github.com/gh-aw/examples/maintaining-repos
source_type: docs
title: "GitHub Agentic Workflows Examples: Automated Repository Maintenance"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: emerging
issue: "#876"
---

# GitHub Agentic Workflows Examples: Automated Repository Maintenance

> Practitioner example integrating three gh-aw safety mechanisms — Repo Assist
> triage, safe-outputs output control, and integrity filtering input control —
> into a complete pattern for safely automating open-source repository maintenance
> at scale; notable for the 9× issue closure velocity claim and the explicit framing
> of integrity filtering as both a security control and a token-budget lever.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Examples" section — a
  concrete integration guide showing how to apply Repo Assist, safe-outputs, and
  integrity filtering together for open-source repo maintenance. Distinct from the
  "Reference" pages for each mechanism and from the abstract "Patterns" pages;
  this page is the worked synthesis that shows combination rather than individual
  mechanism design.)
- **Author credibility**: GitHub Agentic Workflows team — first-party documentation
  from the same team behind Peli de Halleux's agent factory blog series and the
  `gh aw` CLI. Claims about platform configuration (YAML field names, integrity
  levels, safe-output types) are authoritative. The 9× impact metric references
  "a study of 15 open-source repositories" — the study is first-party but the
  methodology is not described in detail on this page.
- **Scope**: Automated repository maintenance for public/open-source repositories
  using the combination of Repo Assist + safe-outputs + integrity filtering. Covers:
  the unique challenge of public-trigger agentic workflows, Repo Assist as triage
  layer, safe-outputs configuration for repo maintenance actions, integrity level
  selection, rate limiting, skip-author-associations, concurrency controls, repository
  scoping, and debugging. Does NOT cover: the individual mechanism references
  (see `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-integrity-reference.md`),
  the CentralRepoOps orchestrator+worker pattern for private org repos
  (see `docs-ghaw-central-repo-ops.md`), or the Dependabot Rollout example
  (see `docs-ghaw-maintaining-repos.md`).

## Extracted Claims

### Claim 1: Open-source repositories face a unique agentic security challenge — anyone can submit issues or PRs that trigger agent runs consuming compute and tokens, but contributors vary widely in trustworthiness

- **Evidence**: The page's opening statement and design rationale for the entire
  maintenance pattern. The challenge motivates both the Repo Assist triage layer and
  the integrity filtering input control, which together bound what content reaches
  the AI engine.
- **Confidence**: settled (first-party documentation; the challenge is the stated
  design motivation for the platform's public-repo protections)
- **Quote**: "Open-source maintainers face a unique challenge when running agentic
  workflows: anyone can open an issue or PR, triggering agent runs that consume
  compute and tokens — but not every contributor is equally trustworthy."
- **Our assessment**: This frames the core tension in public-repo agentic automation:
  open platforms require permitting broad triggering (to be useful to contributors)
  but broad triggering is the attack surface. The solution documented on this page
  is layered: filter inputs by trust (integrity filtering), constrain outputs by
  declaration (safe-outputs), and route via a lightweight triage layer (Repo Assist)
  rather than directly executing heavy actions. For Ch03 (Safety and Verification):
  this challenge statement belongs in any guide section on public-facing agentic
  workflows. The distinction from private org workflows is important — private repos
  have GitHub's own access controls as a pre-filter; public repos do not.

### Claim 2: Repo Assist is the recommended triage layer for public repositories — it runs on every new issue or PR, classifies content, and routes work rather than executing heavy actions directly

- **Evidence**: The page's "Repo Assist as Your Triage Layer" section describes the
  pattern explicitly. The guidance recommends it as the entry point for public repos
  because it sees all incoming content while applying only lightweight classification
  actions rather than heavy code-modifying operations.
- **Confidence**: settled (first-party recommendation; the lightweight-before-heavy
  pattern is the explicit design rationale)
- **Quote**: "Repo Assist is a workflow that runs on every new issue or PR, classifies
  the content, and routes work to the right place."
- **Our assessment**: Repo Assist as a triage gate is the public-repo analogue of
  the orchestrator-before-worker pattern from `docs-ghaw-central-repo-ops.md` Claim 1
  — but lighter. Rather than dispatching workers via `dispatch-workflow`, Repo Assist
  applies labels, adds comments, and gates downstream code-modifying agents. This
  is the correct design for high-volume public repos where every issue or PR triggers
  a run: a cheap triage that filters intent before committing expensive analysis.
  For Ch02 (Harness Engineering): recommend Repo Assist as the standard entry point
  for any gh-aw deployment on a public repository. The "classify and route, don't
  modify" principle is the key operational property.

### Claim 3: Safe-outputs is the primary output control mechanism — every action that produces a side-effect on GitHub must be explicitly declared in the `safe-outputs:` block or it is blocked at runtime

- **Evidence**: The page's Safe-Outputs section describes this as the controlling
  mechanism for all write operations. The YAML table of available safe-outputs for
  repo maintenance includes: `label-issue`, `comment-issue`, `comment-pull-request`,
  `create-pull-request`, `merge-pull-request` (experimental), `close-issue`,
  `create-issue`, `assign-issue`.
- **Confidence**: settled (first-party documentation; consistent with the formal
  specification in `docs-ghaw-safe-outputs-specification.md`)
- **Quote**: "Every action that produces a side-effect on GitHub — labeling an issue,
  posting a comment, opening a pull request, merging — must be explicitly declared."
- **Our assessment**: This is the practical statement of `docs-ghaw-safe-outputs-specification.md`
  Claim 1's formal definition — "security-centric translation layer" — expressed
  in practitioner terms. The operative word is "declared": the workflow's frontmatter
  is a static permission manifest, and any mutation not in that manifest cannot be
  executed regardless of what the agent requests. The `merge-pull-request` type
  labeled "experimental" is notable — it suggests automated merging is a controlled
  capability still under development, reinforcing that the safe-outputs surface is
  deliberately gated and evolving. For Ch02: the safe-outputs block for a repo
  maintenance workflow is the complete list of mutations the agent is permitted to
  make; treat it as a security contract, not an optional config.

### Claim 4: Integrity filtering is the primary input control mechanism — it removes items below the minimum trust level from tool-call results before the AI engine sees them, preventing untrusted content from reaching the agent

- **Evidence**: The page describes integrity filtering as the complement to safe-outputs:
  safe-outputs controls what the agent *does*, while integrity filtering controls what
  the agent *sees*. The four integrity levels shown: `merged` (PRs merged into default
  branch), `approved` (owners, members, collaborators), `unapproved` (contributors with
  merged PRs or first-time contributors), `none` (all content).
- **Confidence**: settled (first-party documentation; consistent with the detailed
  reference in `docs-ghaw-integrity-reference.md`)
- **Quote**: (no direct quote on input-control definition; see paraphrase in Our assessment)
- **Our assessment**: The page presents the two mechanisms (safe-outputs, integrity
  filtering) as complementary layers: safe-outputs prevents unauthorized writes,
  integrity filtering prevents untrusted content from influencing the AI's reasoning.
  Together they form the layered defense the page advocates for public-repo maintenance.
  The integrity level taxonomy matches `docs-ghaw-integrity-reference.md` Claim 3's
  authoritative definitions exactly (`merged`, `approved`, `unapproved`, `none`). For
  Ch03: document the two-layer model as the standard safety architecture for public-repo
  agentic workflows. The input/output framing is the clearest way to explain both
  mechanisms without overlap.

### Claim 5: A study of 15 open-source repositories using this combined approach achieved a 9× median increase in issue closure and PR merge velocity, reducing open issue counts in every repository

- **Evidence**: The page's "Real-World Impact" section cites a specific study with a
  specific metric ("9×") and scope ("15 open-source repositories"). The outcome is
  described as improved in all repositories in the study, not just the median.
- **Confidence**: emerging (first-party claim; the study is cited but its methodology
  is not described — no details on repository sizes, issue types, baseline periods,
  or whether the study was independently reviewed)
- **Quote**: "A study of 15 open-source repositories found this approach achieved a
  9× median increase in issue closure and PR merge velocity, reducing open issue counts
  in every repository."
- **Our assessment**: The 9× figure is the most concrete outcome metric in the gh-aw
  corpus for repository maintenance automation. The "median" qualifier and "every
  repository" qualification suggest the study was not dominated by outliers, which
  increases credibility. However, without methodology details (study duration, what
  "closure velocity" means exactly, whether repositories had comparable baselines),
  this remains emerging confidence. The metric references "a link to a separate impact
  report" not followed here. For Ch05 (Team Adoption): cite as a first-party impact
  claim with the caveat that methodology details are from an unfollowed linked report.
  Do not present as independently verified.

### Claim 6: Integrity filtering provides a dual benefit — security (preventing untrusted content from reaching the AI engine) and token-budget reduction (filtered items never appear in the context window)

- **Evidence**: The page's "Token Budget Awareness" section explicitly frames integrity
  filtering as both a security control and a cost control. The mechanism is the same
  for both effects: items removed by the gateway cannot consume context window tokens.
- **Confidence**: settled (first-party; the dual benefit is explicitly stated as a
  design property)
- **Quote**: "Integrity filtering directly reduces token consumption: items filtered by
  the gateway never appear in the agent's context window."
- **Our assessment**: This claim is novel in the corpus: no existing source note frames
  integrity filtering as a token-budget lever, only as a security mechanism. The
  implication is that teams running high-integrity workflows (e.g., `min-integrity: approved`)
  on active public repos with many first-time contributor issues will see significantly
  smaller context windows than teams running `min-integrity: none`. This is both a
  security benefit (fewer potential injection vectors) and an economic benefit (lower
  token costs per run). For Ch02: document integrity level selection as having cost
  implications in addition to security implications. The choice of `approved` vs.
  `unapproved` is not just a trust decision — it also affects run cost on active
  public repos. For Ch05 (Team Adoption): this dual framing helps justify integrity
  filtering investment to cost-conscious teams.

### Claim 7: Rate limiting via `user-rate-limit` prevents any single user from flooding the system with triggered runs — configured with `max-runs-per-window` and `window` (in seconds)

- **Evidence**: The page's "Scaling Strategies" section includes a rate limiting
  configuration example showing `max-runs-per-window: 5` and `window: 60`, meaning
  a single user can trigger at most 5 runs per 60-second window.
- **Confidence**: settled (first-party documentation; the YAML fields are platform
  features with specific semantics)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: Rate limiting is the primary anti-flood protection for
  public-trigger workflows. Without it, a user who creates 50 issues in rapid succession
  would trigger 50 concurrent agent runs — consuming compute, tokens, and potentially
  hitting GitHub API rate limits. The `user-rate-limit` control bounds per-user burst
  rate without blocking legitimate users who file a moderate number of issues over time.
  This is distinct from the `max-parallel` concurrency control (which limits concurrent
  runs globally, not per user). For Ch02: rate limiting should be a standard element of
  any public-repo workflow configuration, not an optimization added after observing
  abuse.

### Claim 8: `skip-author-associations` enables early run termination for trusted author classes — skipping the workflow's agentic phase entirely for owners, members, and collaborators who do not need automated triage

- **Evidence**: The page shows a `skip-author-associations` configuration on
  `issue_comment: [owner, member, collaborator]`. This skips the workflow's agentic
  processing for comments from those author association classes, meaning the agent is
  not invoked at all for their interactions.
- **Confidence**: settled (first-party documentation; the YAML syntax and association
  names are consistent with GitHub's author association taxonomy)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: `skip-author-associations` is an optimization that also serves
  as a token-budget lever: if the workflow's purpose is triaging external contributions,
  there is no need to run the agent on comments from the repo's own maintainers who
  presumably know the project's standards. Skipping these associations reduces total
  agent invocations and token consumption for trusted classes without affecting the
  triage function for external contributors. For Ch02: document as a standard
  optimization for any workflow whose purpose is classifying external input. The
  combination of `skip-author-associations` + `min-integrity: approved` creates a
  two-layer pre-filter: skip trusted maintainers entirely (before agent), filter
  untrusted content from context (during agent).

### Claim 9: Concurrency controls via `max-parallel` limit how many agent runs execute simultaneously — separate from per-user rate limiting

- **Evidence**: The page's scaling section shows `concurrency: max-parallel: 3` as a
  global concurrency control distinct from `user-rate-limit`. The two controls address
  different dimensions: rate limiting bounds triggering burst per user, concurrency
  bounds simultaneous execution globally.
- **Confidence**: settled (first-party; the two fields are shown as separate configuration
  blocks for distinct purposes)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: The separation of rate limiting (per-user burst) from concurrency
  (global parallelism) is architecturally important. A repository could receive moderate
  traffic from many users simultaneously — each within their rate limit — while still
  exceeding the desired parallel execution count. `max-parallel` is the global cap
  that prevents context-window and API rate-limit exhaustion from concurrent runs.
  For Ch02: document both controls as part of the standard public-repo workflow
  configuration. They are complementary: rate limiting prevents individual user floods,
  concurrency prevents aggregate execution floods.

### Claim 10: Repository access scoping via `tools.github.allowed-repos` limits the set of repositories the agent can read — reducing blast radius if the agent is compromised or misbehaves

- **Evidence**: The page shows a `tools.github.allowed-repos: "myorg/*"` configuration
  combined with `min-integrity: approved`, restricting the agent's `github` toolset
  reads to repositories in the org. This is presented as a scaling and safety control.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-integrity-reference.md`
  Concrete Artifacts → "Basic Configuration" showing `allowed-repos` in the integrity
  config)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: Repository scoping is an underemphasized security control in the
  corpus. Even if an agent has only read access, the set of repositories it can read
  determines its reconnaissance surface. An agent maintaining repos in `myorg/*` has
  no legitimate need to read repos outside the org; `allowed-repos: "myorg/*"` enforces
  that constraint at the gateway level. For Ch03: recommend `allowed-repos` scoping as
  a default practice for any workflow that doesn't need cross-org access. The default
  (`"all"`) is permissive; the correct posture is to scope to the minimum necessary
  repository set.

### Claim 11: Six failure patterns cover the common failure modes in public-repo maintenance workflows — each with specific symptoms and targeted fixes involving specific audit commands and YAML adjustments

- **Evidence**: The page's troubleshooting section presents a complete six-row table
  of failure patterns: missing tool calls, authentication failures, integrity filtering
  blocking content, safe-output validation failures, token budget exhaustion, and
  network blocks. Each row includes symptom, cause, and specific remediation steps.
- **Confidence**: settled (first-party; the six patterns are explicitly structured
  with `DIFC_FILTERED` events, `safe_outputs.jsonl` artifacts, and specific CLI
  commands for each failure type)
- **Quote**: (no direct single quote; see Concrete Artifacts for full table)
- **Our assessment**: The six failure patterns constitute the definitive diagnostic
  taxonomy for public-repo maintenance workflows. Each pattern maps to a specific
  mechanism: missing tool calls → workflow frontmatter configuration; auth failures →
  permissions/secrets; integrity filtering blocks → guard policy misconfiguration
  (surfaced via `DIFC_FILTERED` events); safe-output failures → undeclared mutations;
  token exhaustion → context budget; network blocks → domain allowlist. This taxonomy
  is more comprehensive than any existing corpus note on debugging. For Ch02: the
  troubleshooting table is the field diagnostic guide for any practitioner with a
  misbehaving repo maintenance workflow.

### Claim 12: `gh aw audit RUN_ID` provides structured analysis of a specific run's behavior, with `--json` and `--parse` flags for machine-readable output; comparative audit via `gh aw audit BASELINE_ID CURRENT_ID` enables regression detection

- **Evidence**: The page's debugging section lists specific CLI commands for audit,
  including the standard `gh aw audit RUN_ID` invocation, flag variants, and the
  two-argument form for comparing a baseline run against a current run.
- **Confidence**: settled (first-party; the CLI commands are listed verbatim on the page)
- **Quote**: (no direct prose quote; see Concrete Artifacts for CLI commands)
- **Our assessment**: The comparative audit command (`gh aw audit BASELINE_ID CURRENT_ID`)
  is novel in the corpus — no existing source note documents this regression detection
  mode. The typical workflow for debugging a regression would be to compare a known-good
  run (baseline) against the failing run (current), and this command enables that
  directly. For Ch02: document the comparative audit as the primary tool for debugging
  behavioral regressions in workflows — useful when a workflow that previously worked
  correctly starts misbehaving after a configuration or prompt change.

## Concrete Artifacts

### Safe-Outputs Available for Repository Maintenance

From the page's Safe-Outputs section:

```
Safe-output          | What it allows
---------------------|-------------------------------------------
label-issue          | Apply or remove labels on an issue
comment-issue        | Post a comment on an issue
comment-pull-request | Post a comment on a pull request
create-pull-request  | Open a new pull request
merge-pull-request   | Merge a pull request (experimental)
close-issue          | Close an issue
create-issue         | Open a new issue
assign-issue         | Assign an issue to a user or team
```

*Source: gh-aw examples/maintaining-repos, "Safe-Outputs Configuration" section*

### Rate Limiting Configuration

```yaml
user-rate-limit:
  max-runs-per-window: 5
  window: 60
```

*Source: gh-aw examples/maintaining-repos, "Rate Limiting" section*

### Skip Author Associations

```yaml
on:
  issue_comment:
    types: [created]
  skip-author-associations:
    issue_comment: [owner, member, collaborator]
```

*Source: gh-aw examples/maintaining-repos, "Skip Author Associations" section*

### Concurrency Control

```yaml
concurrency:
  max-parallel: 3
```

*Source: gh-aw examples/maintaining-repos, "Concurrency" section*

### Repository Scoping with Integrity Filtering

```yaml
tools:
  github:
    allowed-repos: "myorg/*"
    min-integrity: approved
```

*Source: gh-aw examples/maintaining-repos, "Repository Scoping" section*

### Integrity Reactions Configuration

```yaml
features:
  integrity-reactions: true
tools:
  github:
    min-integrity: approved
```

*Source: gh-aw examples/maintaining-repos, "Integrity Reactions Configuration" section*

### Debugging CLI Commands

```
gh aw audit RUN_ID
gh aw audit RUN_ID --json
gh aw audit RUN_ID --parse
gh aw logs my-workflow
gh aw logs my-workflow --format markdown --count 10
gh aw logs --filtered-integrity
gh aw audit BASELINE_ID CURRENT_ID
```

*Source: gh-aw examples/maintaining-repos, "Debugging Commands" section*

### Troubleshooting Failure Patterns

```
Failure                        | Symptom / Cause                                            | Fixes
-------------------------------|------------------------------------------------------------|-----------
Missing tool calls             | Tool not configured or wrong name. Check `missing_tools`  | Add to `tools:` in frontmatter; fix any `safeoutputs-` prefix;
                               | in audit.                                                  | check MCP connectivity.
Authentication failures        | Token permissions too narrow or API key missing.           | Review `permissions:` block; ensure secrets are set.
Integrity filtering blocking   | Author's association below `min-integrity`. `DIFC_FILTERED`| Adjust `min-integrity`; add author to `trusted-users`;
content                        | events in audit show details.                              | use `approval-labels`; check logs.
Safe-output validation         | Agent attempted undeclared GitHub action. Safe-outputs      | Review `safe-outputs:`; check `safe_outputs.jsonl` in
failures                       | blocks anything not listed.                                | audit artifacts.
Token budget exhaustion        | Run hit token limit before completing.                     | Raise `min-integrity` to reduce context; add `cache-memory:`;
                               |                                                            | simplify prompt; tighten `user-rate-limit`.
Network blocks                 | Required domain blocked by firewall.                       | Check firewall section of audit; add domain to
                               |                                                            | `network.allowed`.
```

*Source: gh-aw examples/maintaining-repos, "Common Failure Patterns Table"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-integrity-reference.md` Claim 1 ("Integrity filtering manages which GitHub
    content an agent can access by filtering based on trust rather than permissions"):
    This examples page confirms integrity filtering as the input control layer in the
    public-repo maintenance pattern — the same mechanism the reference page documents
    authoritatively. The level definitions (`merged`, `approved`, `unapproved`, `none`)
    match `docs-ghaw-integrity-reference.md` Claim 3 exactly.
  - `docs-ghaw-integrity-reference.md` Claim 12 (`gh aw logs --filtered-integrity` for
    investigating filtering behavior): The debugging CLI commands on this page include
    `gh aw logs --filtered-integrity`, corroborating that command as the diagnostic tool
    for integrity-related failures.
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (Safe Outputs as "security-centric
    translation layer enabling AI agents to declare intended GitHub operations"): Claim 3
    here ("every action that produces a side-effect must be explicitly declared") is the
    practitioner-language version of the same principle. The formal spec and this example
    page are fully consistent.
  - `docs-ghaw-safe-outputs-specification.md` Claim 7 (content sanitization via SP4 as
    a prompt-injection defense): This page's two-mechanism framing (safe-outputs for output,
    integrity filtering for input) is consistent with the spec's defense-in-depth model —
    input restriction (integrity filtering) plus output sanitization (safe-outputs SP4)
    together bound the injection attack surface.

- **Extends**:
  - `docs-ghaw-integrity-reference.md`: That reference documents the full eleven-field
    integrity configuration surface. This examples page applies a subset (primarily
    `min-integrity`, `allowed-repos`, `user-rate-limit`, and `skip-author-associations`)
    in a concrete maintenance workflow context. Together they form the complete reference
    (configuration surface) + practical application (this note).
  - `docs-ghaw-safe-outputs-specification.md`: The formal spec defines what safe-outputs
    are and how they work architecturally. This examples page shows which specific output
    types are used for repo maintenance (`label-issue`, `comment-issue`, `close-issue`,
    etc.) and how they fit into the broader layered safety pattern. The spec provides
    the "what" and "why"; this page provides the "which types to use and in what context."
  - `docs-ghaw-central-repo-ops.md` Claim 1 (Orchestrator+Worker split as the
    recommended multi-repo architecture): This examples page covers a simpler, single-
    workflow architecture (Repo Assist triage → lightweight actions) appropriate for
    open-source public repos where the priority is lightweight triage, not org-scale
    rollout. CentralRepoOps is the heavier pattern for private org rollouts; this page
    is the lighter pattern for ongoing public-repo maintenance.

- **Contradicts**: None identified. The integrity level names, safe-output semantics,
  and debugging commands are consistent with all existing source notes.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Integrity filtering as token-budget lever** (Claim 6): No prior source note frames
    integrity filtering as a cost control mechanism. The quote "items filtered by the
    gateway never appear in the agent's context window" establishes a direct connection
    between `min-integrity` level selection and per-run token cost. This is new guidance
    for practitioners choosing integrity levels.
  - **9× issue closure velocity impact metric** (Claim 5): No existing source note
    documents a quantitative outcome metric for the combined Repo Assist + safe-outputs
    + integrity filtering pattern. This is the only cited operational impact measurement
    in the corpus for this pattern combination.
  - **Repo Assist as triage layer framing** (Claim 2): While Repo Assist is mentioned
    in passing in other notes, this page's explicit framing of it as the recommended
    first layer before heavier code-modifying agents is new. The "classify and route,
    don't modify" principle is not stated this directly in any existing note.
  - **`skip-author-associations` optimization pattern** (Claim 8): No existing source
    note documents `skip-author-associations` as an agent invocation optimization for
    trusted author classes. The combination of this field with integrity filtering as
    a two-layer pre-filter is novel.
  - **Comparative audit for regression detection** (Claim 12): `gh aw audit BASELINE_ID
    CURRENT_ID` as a regression comparison tool is not documented in any existing source
    note.
  - **Safe-outputs type catalog for repo maintenance** (Claim 3): The specific eight
    output types for repo maintenance (`label-issue`, `comment-issue`, `comment-pull-request`,
    `create-pull-request`, `merge-pull-request` [experimental], `close-issue`, `create-issue`,
    `assign-issue`) as a named subset for this use case are not listed as a group in any
    existing source note.
  - **Six-pattern troubleshooting taxonomy with artifact references** (Claim 11): While
    individual debugging commands appear in other notes, this is the first source note
    with a complete failure-pattern table linking each failure type to its artifact
    (`DIFC_FILTERED`, `safe_outputs.jsonl`) and specific remediation steps.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add Repo Assist as the standard entry point for public-repo workflows** (Claim 2):
  The guide should recommend Repo Assist as the default first-layer workflow for any
  public repository, positioned before heavier code-modifying agents. The "classify
  and route" design principle — lightweight triage rather than direct modification —
  should be named explicitly. Cross-reference CentralRepoOps (`docs-ghaw-central-repo-ops.md`)
  as the complementary pattern for private org rollouts.

- **Add `skip-author-associations` + `user-rate-limit` + `max-parallel` as the
  standard scaling configuration for public-repo workflows** (Claims 7–9): Document
  these three controls as a set: rate limiting (per-user burst), concurrency (global
  parallelism), and association skipping (trusted author pre-filter). They address
  different dimensions of the scaling problem and should all be present in any
  high-traffic public-repo workflow configuration.

- **Document `tools.github.allowed-repos` scoping as a default security practice**
  (Claim 10): Recommend repository scoping as the default, with `"all"` as a
  conscious opt-out requiring justification. Document alongside `min-integrity` as
  part of the standard `tools.github` security configuration.

- **Add six-failure-pattern troubleshooting table as the diagnostic reference**
  (Claim 11): The table provides the complete field guide for debugging gh-aw
  maintenance workflows. Pair with `gh aw audit RUN_ID` (standard) and
  `gh aw audit BASELINE_ID CURRENT_ID` (regression) as the primary debugging tools.

### Chapter 03: Safety and Verification

- **Frame the safe-outputs + integrity filtering combination as the layered defense
  model for public-repo workflows** (Claims 3–4): Chapter 03 should describe the
  two-layer model explicitly: safe-outputs blocks unauthorized mutations (output layer);
  integrity filtering blocks untrusted content from reaching the AI engine (input layer).
  Neither alone is sufficient — an agent with write access but no input filtering is
  vulnerable to prompt injection from issues; an agent with input filtering but no
  output control can still take unauthorized actions on trusted inputs.

- **Add public-repo challenge framing to the safety coverage** (Claim 1): The
  open-source challenge — anyone can trigger agent runs, varying trustworthiness —
  is the motivating design context for the input/output safety layer combination.
  Document it as the adversarial model that integrity filtering + safe-outputs
  address together.

### Chapter 05: Team Adoption

- **Cite 9× issue closure velocity as the first-party impact metric for this pattern**
  (Claim 5): When making the case for agentic repo maintenance, this is the most
  concrete quantitative claim in the corpus. Present with appropriate caveats: 15
  repositories, methodology details in a linked report not deeply examined.

- **Frame integrity level selection as both a security and cost decision** (Claim 6):
  Teams evaluating integrity filtering often frame it purely as security overhead.
  The token-budget framing changes the calculus: higher integrity (stricter filtering)
  can reduce per-run costs on active public repos with many low-integrity issues.
  Present the dual benefit when discussing adoption of integrity filtering.

## Extraction Notes

1. **WebFetch used; no raw HTML access**: The page is a JavaScript-rendered SPA
   (Astro/Starlight). Content was extracted via three WebFetch passes with different
   prompts to maximize verbatim coverage. The verbatim quotes captured here have been
   confirmed across multiple passes; they are assessed as accurate to the source page.
   YAML blocks were confirmed in two passes.

2. **No complete Repo Assist workflow YAML present**: The page does not reproduce a
   complete Repo Assist workflow frontmatter — only configuration fragments for specific
   features. Practitioners implementing Repo Assist should consult the Repo Assist
   pattern documentation (not fetched for this note).

3. **`merge-pull-request` labeled experimental**: The safe-outputs table lists
   `merge-pull-request` with "(experimental)" notation. This capability should not
   be relied upon for production workflows without consulting current platform status.

4. **9× metric methodology not examined**: The impact claim references "a separate
   impact report" via a link not followed in this extraction. The study scope (15
   repositories) and outcome (9× median velocity, improvement in all repos) are taken
   from the page text. Full methodology assessment would require following the linked
   report.

5. **No sub-pages followed**: The page links to the Safe Outputs Reference, Integrity
   Filtering Reference, Rate Limiting Reference, and Audit Reference as related
   documentation. These are covered by existing source notes
   (`docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-integrity-reference.md`,
   etc.). The debugging commands page and network configuration guide were not fetched.

6. **No publication date**: The page does not carry an explicit date. Content is
   consistent with gh-aw platform behavior as of 2026-05-23.

7. **No contradictions filed**: Reviewed all existing source notes with gh-aw, integrity
   filtering, safe-outputs, and Repo Assist coverage. No claims in this source materially
   oppose any existing source note. The integrity level names, safe-output semantics, and
   platform behavior are fully consistent with `docs-ghaw-integrity-reference.md` and
   `docs-ghaw-safe-outputs-specification.md`. No contradiction issue required.
