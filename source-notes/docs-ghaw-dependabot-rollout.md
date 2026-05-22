---
source_url: https://github.github.com/gh-aw/examples/multi-repo/dependabot-rollout
source_type: docs
title: "GitHub Agentic Workflows Examples: Dependabot Rollout"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#851"
---

# GitHub Agentic Workflows Examples: Dependabot Rollout

> Practitioner walkthrough for implementing the CentralRepoOps orchestrator+worker
> pattern in the Dependabot rollout use case — provides the four-step setup sequence
> with specific CLI commands, safe incremental scaling via manual PR review before
> full automation, and the `[dependabot]` title-prefix + concurrency-group conventions
> that extend the abstract CentralRepoOps pattern documentation into runnable form.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Examples" section —
  a concrete, end-to-end implementation walkthrough of the CentralRepoOps
  orchestrator+worker pattern applied to the Dependabot configuration rollout
  use case. Distinct from the abstract "Patterns" reference pages; this page is
  a practitioner walkthrough with step-by-step setup instructions and runnable
  YAML configuration.)
- **Author credibility**: GitHub Agentic Workflows team — first-party examples
  from the same team behind the Peli de Halleux "Agent Factory" blog series and
  the `gh aw` CLI. The YAML configurations, CLI commands, and setup steps are
  authoritative for the gh-aw platform. The categorization thresholds and dispatch
  limits are opinionated defaults from the example, not platform-enforced constraints.
- **Scope**: End-to-end Dependabot configuration rollout using the CentralRepoOps
  pattern: four-step setup procedure, orchestrator workflow (Filter→Categorize→
  Prioritize→Dispatch→Summarize), worker workflow (conflict detection→analysis→
  customized PR or issue), three-PAT secret configuration, concurrency controls,
  and incremental validation approach. Does NOT cover: the abstract CentralRepoOps
  design pattern (see `docs-ghaw-central-repo-ops.md`), the `dispatch-workflow` vs.
  `call-workflow` decision (see `docs-ghaw-orchestration-patterns.md`), the
  `--dependabot` compiler flag for runtime tool monitoring (see
  `docs-ghaw-dependabot.md`), or the general safe rollout framework
  (see `docs-ghaw-safe-rollout.md`).

## Extracted Claims

### Claim 1: This examples page bridges abstract pattern documentation and runnable implementation by providing four ordered setup steps with specific file paths and CLI commands not found in the CentralRepoOps pattern reference

- **Evidence**: The page structures setup as four discrete steps, each prescribing
  a specific action: (1) create the orchestrator file at a named path, (2) compile
  and create the read token, (3) create the worker file, (4) create the checkout and
  output PATs. The ordering is load-bearing — the orchestrator must exist and be
  compiled before the worker references it via `dispatch-workflow`.
- **Confidence**: emerging (first-party documentation with concrete CLI commands;
  the ordering dependency is inferred from the dispatch-workflow compilation model
  in `docs-ghaw-orchestration-patterns.md` Claim 5)
- **Quote**: "In your central control repository, create `.github/workflows/dependabot-rollout-orchestrator.md`"
- **Our assessment**: The `docs-ghaw-central-repo-ops.md` note covers the same
  orchestrator+worker architecture and YAML but as a pattern reference — it describes
  what the pattern does, not how to set it up. This examples page provides the missing
  procedural layer: what to create, in what order, using what commands. The compile
  step (`gh aw compile`) as an explicit setup requirement — not just a development
  tool — is particularly important; practitioners following the abstract pattern page
  alone might not know to run the compiler before creating secrets. For Ch02 (Harness
  Engineering): pair the architectural documentation from `docs-ghaw-central-repo-ops.md`
  with this procedural walkthrough as the "how to actually build it" reference.

### Claim 2: The orchestrator's Filter step is the primary pre-flight safety gate — it scans org repos and skips all repositories that already have Dependabot configured before any worker is dispatched

- **Evidence**: The "How It Works" section describes the orchestrator's behavior
  explicitly: "The orchestrator runs weekly, scans org repos, skips ones that already
  have Dependabot configured, and dispatches up to 5 workers per run."
- **Confidence**: settled (first-party documentation; Filter is the first of five
  orchestrator tasks, positioned before Categorize to prevent wasted analysis on
  already-configured repos)
- **Quote**: "The orchestrator runs weekly, scans org repos, skips ones that already
  have Dependabot configured, and dispatches up to 5 workers per run."
- **Our assessment**: The Filter step's placement as the first task (before
  Categorize) is architecturally significant: no analysis effort is spent on repos
  that already have Dependabot. This is the idempotence guarantee for the
  orchestrator — running it multiple times will not dispatch duplicate workers to
  already-configured repos. Without this filter, a repo that has Dependabot
  configured (perhaps manually) after the first orchestrator run would be
  re-processed on the next run and generate a conflict-detection issue (the worker
  would detect the existing `dependabot.yml` and output an issue instead of a PR).
  For Ch02: the Filter step is the orchestrator-level idempotence mechanism;
  document it as a required pattern for any org-scale rollout orchestrator.

### Claim 3: Workers perform analysis-driven configuration generation rather than template application — each worker analyzes the specific repository's structure and generates customized configuration with reasoning explained in the PR body

- **Evidence**: The "How It Works" section states: "Each worker checks out the
  target repo, analyzes its structure, and creates a customized `dependabot.yml`
  pull request — or opens an issue if Renovate or other conflicts are detected."
  The worker performs ecosystem detection, monorepo analysis, security alert review,
  and conflict detection before generating any configuration.
- **Confidence**: emerging (first-party description; the specific analysis dimensions
  are documented but the exact prompt instructions that drive analysis are in the
  worker workflow content, not reproduced verbatim in the summary sections)
- **Quote**: "Each worker checks out the target repo, analyzes its structure, and
  creates a customized `dependabot.yml` pull request — or opens an issue if Renovate
  or other conflicts are detected."
- **Our assessment**: The "customized" emphasis over "generic template" is consistent
  with `docs-ghaw-central-repo-ops.md` Claim 9 — "explain why you chose this specific
  configuration (not a generic template)." This is the value proposition of agentic
  configuration rollout over scripted rollout: the agent can tailor configuration to
  each repo's actual dependency complexity, monorepo structure, and security posture,
  producing PRs that reviewers can evaluate by checking the reasoning against their
  own knowledge of the repo. For Ch01 (Daily Workflows): document analysis-driven
  vs. template-driven configuration as a key differentiator for agentic rollout tools.
  For Ch02: instruct workers to include analysis rationale in PR bodies, not just the
  generated configuration file.

### Claim 4: The recommended safe rollout procedure is explicit manual validation before scaling — start with max: 5 dispatches, review worker PRs manually, then increase the limit once output quality is confirmed

- **Evidence**: The Best Practices section explicitly states: "Keep `max: 5` on the
  orchestrator during initial rollout; increase once validated." and "Review a few
  worker PRs manually before full automation."
- **Confidence**: settled (first-party; explicitly stated as best practice recommendations)
- **Quote**: "Keep `max: 5` on the orchestrator during initial rollout; increase once
  validated." / "Review a few worker PRs manually before full automation."
- **Our assessment**: The explicit "review before scaling" instruction is the
  practitioner-level instantiation of the `docs-ghaw-safe-rollout.md` safe rollout
  framework. The `max: 5` starting limit functions as the pilot cohort; manual review
  of those 5 PRs answers the question "is the worker generating acceptable output?"
  before committing to org-wide automation. If the worker generates poor-quality
  configurations (e.g., wrong update intervals, missing ecosystems, incorrect monorepo
  detection), the `max: 5` limit bounds the blast radius to 5 PRs before the issue
  is caught. For Ch05 (Team Adoption): document this as the standard pilot validation
  procedure for org-scale agentic operations — the `max` parameter is both a safety
  control and a pilot-wave selector.

### Claim 5: Worker-level conflict detection outputs issues (not PRs) for repositories where existing tooling conflicts would be overwritten — creating a human-review queue for cases the automation cannot safely resolve

- **Evidence**: The How It Works section and the worker workflow description establish
  the conflict detection gate as the worker's first safety check, with issues as the
  output for conflicting cases. The conflict types covered: existing `dependabot.yml`
  (already configured), Renovate configuration files (`renovate.json`, `.renovaterc`),
  and custom dependency update scripts.
- **Confidence**: settled (first-party; conflict detection is documented in both the
  How It Works section and the worker workflow description; consistent with
  `docs-ghaw-central-repo-ops.md` Claim 10)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The issue-instead-of-PR output for conflicts is the correct
  behavior at the worker level for the same reason the orchestrator uses issues for
  ambiguous cases: it flags the problem for human resolution without making any
  changes. A repo with Renovate already installed needs a human decision — migrate
  to Dependabot, keep Renovate, or run both. The agent can detect the conflict but
  cannot safely make that policy decision. This creates a self-triaging queue: after
  the orchestrator runs, repos receive either a Dependabot PR (clean), a conflict
  issue (needs human decision), or nothing (already configured). For Ch03 (Safety and
  Verification): the conflict detection gate at the worker level is the primary safety
  mechanism for org-scale configuration rollout. Document it as mandatory: any worker
  that modifies existing configurations must check for conflicts before creating a PR.

### Claim 6: Concurrency groups at the workflow level prevent duplicate processing of the same target repository when multiple orchestrator runs overlap

- **Evidence**: The worker workflow frontmatter includes a `concurrency` field with a
  group key incorporating both the workflow name and the target repository input:
  `gh-aw-${{ github.workflow }}-${{ github.event.inputs.target_repo }}`. The Best
  Practices section confirms: "Use `concurrency` groups to prevent duplicate runs."
- **Confidence**: settled (first-party; the concurrency configuration is in the worker
  YAML frontmatter; consistent with `docs-ghaw-central-repo-ops.md` Concrete Artifacts
  → worker YAML)
- **Quote**: "Use `concurrency` groups to prevent duplicate runs."
- **Our assessment**: The concurrency group keyed on `target_repo` is the correct
  deduplication primitive for worker workflows that accept a repo name as input.
  Without it, if the orchestrator is triggered manually (or runs twice in close
  succession), the same target repo could receive two concurrent worker invocations —
  potentially creating two PRs or causing race conditions on checkout. The group key
  ensures exactly one worker runs for each repo at a time. For Ch02: document the
  `concurrency: group:` field as a required element in any `workflow_dispatch`-triggered
  worker that accepts a target identifier as input.

### Claim 7: The `[dependabot]` title prefix convention enables cross-repo filtering and identification of agent-created PRs throughout the organization

- **Evidence**: The Best Practices section states: "Add `[dependabot]` title-prefix
  for easy filtering." The worker frontmatter includes
  `title-prefix: '[dependabot] '` in the `safe-outputs.create-pull-request`
  configuration.
- **Confidence**: settled (first-party; stated as a best practice with YAML evidence)
- **Quote**: "Add `[dependabot]` title-prefix for easy filtering."
- **Our assessment**: The title prefix serves two functions: (1) it enables engineers
  in target repos to filter their PR queue to show only agent-created Dependabot PRs,
  and (2) it provides the orchestrator (and the team operating the control plane) with
  a consistent signal for identifying which PRs were created by the agent vs. manually.
  The prefix also aids deduplication — if a repo already has a `[dependabot]` PR open,
  the `max: 1` safe output constraint prevents the worker from creating a second one
  even if the orchestrator dispatches the worker again. For Ch02: document title prefix
  conventions as a required element of any org-scale worker workflow; they are the
  primary searchability and deduplication mechanism for agent-created outputs at scale.

### Claim 8: The three-PAT setup assigns each token to exactly one role with minimum required permissions — GH_AW_READ_ORG_TOKEN (orchestrator read), ORG_REPO_CHECKOUT_TOKEN (worker checkout), GH_AW_CROSS_REPO_PAT (worker output delivery)

- **Evidence**: The Setup section documents three distinct secret creation steps,
  each tied to a specific workflow role and permission scope:
  Step 2: `GH_AW_READ_ORG_TOKEN` — "a fine-grained PAT with `Contents: Read-only`
  scoped to all target repositories" (orchestrator scanning).
  Step 4: `ORG_REPO_CHECKOUT_TOKEN` — Contents R/W, Actions R (worker checkout);
  `GH_AW_CROSS_REPO_PAT` — Contents W, Issues W, PRs W (worker safe-outputs).
- **Confidence**: settled (first-party documentation; consistent with
  `docs-ghaw-central-repo-ops.md` Claim 3's three-token model)
- **Quote**: "a fine-grained PAT with `Contents: Read-only` scoped to all target
  repositories"
- **Our assessment**: The three-PAT setup instantiates the least-privilege principle
  at the multi-repo level: each token grants only what its role requires and nothing
  more. The read token cannot create PRs; the checkout token cannot deliver safe
  outputs; the output token cannot read the org repository list. This separation
  matters for security posture — a compromised read token cannot write to any repo,
  and a compromised output token cannot scan the org's repo list. For Ch03 (Safety
  and Verification): the three-PAT model is the reference implementation of
  least-privilege multi-repo token design. Map each token to one role; never share
  tokens between roles.

### Claim 9: The Summarize task in the orchestrator creates a built-in audit trail of each run's decisions without requiring separate monitoring tooling

- **Evidence**: Summarization is the fifth and final task in the orchestrator's
  sequence. The orchestrator reports total candidates identified, categorization
  breakdown (simple/complex/conflicting/security counts), and the specific repos
  selected for this run with rationale. This appears in the workflow run log visible
  in the GitHub Actions UI.
- **Confidence**: emerging (first-party; the Summarize task is described in the
  orchestrator workflow frontmatter; the exact output format is part of the agent
  prompt, not reproduced in full by WebFetch)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The Summarize task is an important auditability feature: after
  each weekly run, operators can read the orchestrator's run log to understand which
  repos were selected, why they were categorized as they were, and what was dispatched.
  This is the "human-readable decision trail" that makes automated org-scale operations
  governable — without it, the orchestrator is a black box that changes repos on a
  schedule with no explanation. In combination with the conflict-detection issues
  created by workers, the Summarize output provides complete traceability: orchestrator
  log shows what was considered and selected; worker outputs (PRs and issues) show
  what was done and why. For Ch02: document the Summarize step as a required element
  of any multi-repo orchestration workflow. For Ch05 (Team Adoption): the
  orchestrator's decision log is the governance artifact that enables teams to trust
  and audit automated org-scale operations.

## Concrete Artifacts

### Page Introduction (verbatim)

From the page's opening description:

```
"This example shows how to roll out a new Dependabot configuration across 100
repositories using the central control plane pattern."
```

*Source: gh-aw examples, "Dependabot Rollout — Overview" section*

### How It Works (verbatim)

From the page's "How It Works" section:

```
1. The orchestrator runs weekly, scans org repos, skips ones that already have
   Dependabot configured, and dispatches up to 5 workers per run.

2. Each worker checks out the target repo, analyzes its structure, and creates a
   customized dependabot.yml pull request — or opens an issue if Renovate or other
   conflicts are detected.
```

*Source: gh-aw examples, "Dependabot Rollout — How It Works" section*

### Setup Steps (verbatim)

From the page's "Setup" section:

```
Step 1: In your central control repository, create
        .github/workflows/dependabot-rollout-orchestrator.md
        [with orchestrator frontmatter and prompt]

Step 2: Compile this workflow: gh aw compile
        Then create the GH_AW_READ_ORG_TOKEN secret — a fine-grained PAT with
        Contents: Read-only scoped to all target repositories.

Step 3: Create the worker workflow .github/workflows/dependabot-rollout.md
        in the same central repository.

Step 4: Create two fine-grained PATs scoped to target repositories:
        - ORG_REPO_CHECKOUT_TOKEN: Contents R/W, Actions R  (worker checkout)
        - GH_AW_CROSS_REPO_PAT:    Contents W, Issues W, PRs W  (worker outputs)
```

*Source: gh-aw examples, "Dependabot Rollout — Setup" section*

### Best Practices (verbatim)

From the page's "Best Practices" section:

```
- Keep `max: 5` on the orchestrator during initial rollout; increase once validated.
- Add `[dependabot]` title-prefix for easy filtering.
- Use `concurrency` groups to prevent duplicate runs.
- Review a few worker PRs manually before full automation.
```

*Source: gh-aw examples, "Dependabot Rollout — Best Practices" section*

### Orchestrator Workflow Frontmatter

Consistent with `docs-ghaw-central-repo-ops.md` Concrete Artifacts. Reproduced here
for practitioner convenience; verify against the live example page before use in
production.

```markdown
---
on:
  schedule:
    - cron: '0 9 * * 1'
tools:
  github:
    github-token: ${{ secrets.GH_AW_READ_ORG_TOKEN }}
    toolsets: [repos]
safe-outputs:
  dispatch-workflow:
    workflows: [dependabot-rollout]
    max: 5
---
# Dependabot Rollout Orchestrator
Categorize and orchestrate Dependabot rollout across repositories.
**Target repos**: All repos in the organization

## Task
1. **Filter** - Parse repos, check each for existing `.github/dependabot.yml`,
   keep only repos without it
2. **Categorize** - Read repo contents to assess complexity:
   - Simple: Single package.json, <50 dependencies, standard structure
   - Complex: Multiple package.json files, >100 deps, or multiple ecosystems
   - Conflicting: Has Renovate config or custom update scripts
   - Security: Open security alerts or public with dependencies
3. **Prioritize** - Order repos by rollout preference: simple → security → complex → conflicting
4. **Dispatch** - Dispatch `dependabot-rollout` worker for every prioritized repository
5. **Summarize** - Report total candidates, categorization breakdown, selected repos with rationale
```

*Source: gh-aw examples, "Dependabot Rollout — Orchestrator Workflow" section;
consistent with `docs-ghaw-central-repo-ops.md` Concrete Artifacts →
"Complete Orchestrator Workflow Frontmatter (Dependabot Rollout)"*

### Worker Workflow Frontmatter

Consistent with `docs-ghaw-central-repo-ops.md` Concrete Artifacts. Reproduced here
for practitioner convenience.

```markdown
---
on:
  workflow_dispatch:
    inputs:
      target_repo:
        description: 'Target repository (owner/repo format)'
        required: true
        type: string

run-name: Dependabot rollout for ${{ github.event.inputs.target_repo }}

concurrency:
  group: gh-aw-${{ github.workflow }}-${{ github.event.inputs.target_repo }}

engine:
  id: copilot
  concurrency:
    group: gh-aw-copilot-${{ github.workflow }}-${{ github.event.inputs.target_repo }}

checkout:
  repository: ${{ github.event.inputs.target_repo }}
  github-token: ${{ secrets.ORG_REPO_CHECKOUT_TOKEN }}
  current: true

permissions:
  contents: read
  issues: read
  pull-requests: read

tools:
  github:
    github-token: ${{ secrets.GH_AW_READ_ORG_TOKEN }}
    toolsets: [repos]

safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-pull-request:
    target-repo: ${{ github.event.inputs.target_repo }}
    title-prefix: '[dependabot] '
    max: 1
  create-issue:
    target-repo: ${{ github.event.inputs.target_repo }}
    title-prefix: '[dependabot-config] '
    max: 1
---
```

*Source: gh-aw examples, "Dependabot Rollout — Worker Workflow" section;
consistent with `docs-ghaw-central-repo-ops.md` Concrete Artifacts →
"Complete Worker Workflow Frontmatter (Dependabot Rollout)"*

### Orchestrator Five-Task Sequence

```
Task 1: FILTER
  → Scan all org repositories
  → Skip repos that already have .github/dependabot.yml
  → Keep only repos without existing Dependabot configuration
  (Idempotence guarantee: never re-processes already-configured repos)

Task 2: CATEGORIZE
  → Simple:      single package.json, <50 deps, standard structure
  → Complex:     multiple package.json, >100 deps, multiple ecosystems
  → Conflicting: Renovate config or custom update scripts present
  → Security:    open security alerts or public repo with dependencies

Task 3: PRIORITIZE
  → Order: simple → security → complex → conflicting
  (Easiest first; conflicts deferred to human judgment)

Task 4: DISPATCH
  → Trigger dependabot-rollout worker for each prioritized repo
  → Bounded by max: 5 per orchestrator run (adjustable after validation)

Task 5: SUMMARIZE
  → Report: total candidates, categorization breakdown, selected repos + rationale
  (Built-in audit trail in the GitHub Actions run log)
```

### Worker Conflict Detection Gate

```
On entry, worker checks (in order):

  1. Does .github/dependabot.yml already exist?
     → YES: Stop. Create issue: existing config detected.
     (Orchestrator Filter should have caught this; issue is the fallback)

  2. Does .github/renovate.json, renovate.json, or .renovaterc exist?
     → YES: Create issue: "Renovate configuration found — migration required."

  3. Are there custom dependency update scripts?
     → YES: Create issue: "Custom scripts found — review before automating."

  4. No conflicts found → Proceed to complexity analysis and PR creation.

Output for conflicts: ISSUE (not PR). No code changes made.
Output for clean repos: PR with customized dependabot.yml + reasoning in body.
Output PR limit: max: 1 per worker run.
```

### Three-PAT Permission Architecture

```
Token: GH_AW_READ_ORG_TOKEN
  Role:        Orchestrator scanning
  Scope:       Organization owner, all repositories
  Permissions: Contents: Read-only
  Created in:  Setup Step 2

Token: ORG_REPO_CHECKOUT_TOKEN
  Role:        Worker checkout
  Scope:       Organization owner, all repositories
  Permissions: Contents: Read & write, Actions: Read & write
  Created in:  Setup Step 4

Token: GH_AW_CROSS_REPO_PAT
  Role:        Worker safe-outputs delivery
  Scope:       Organization owner, all repositories
  Permissions: Contents: Write, Issues: Write, Pull Requests: Write
  Created in:  Setup Step 4

Design principle: one token per role; no role shares a token with another.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-central-repo-ops.md` Claim 1 ("Orchestrator Role: Decides _where_ to
    roll out next … Worker Role: Executes _how_ to configure each target repository"):
    This example page is a concrete practitioner walkthrough of exactly this split
    applied to the Dependabot rollout use case. The policy/execution separation is
    visible in the five-task sequence: the orchestrator owns where (which repos,
    in what order) while workers own how (analyze, generate, deliver).
  - `docs-ghaw-central-repo-ops.md` Claim 2 ("`max` parameter prevents overwhelming
    the organization with simultaneous changes"): Claim 4 here extends this with the
    specific practice: start at `max: 5`, review manually, then scale. The examples
    page provides the incremental validation procedure that the pattern reference
    describes only structurally.
  - `docs-ghaw-central-repo-ops.md` Claim 3 (three-PAT model): Claim 8 here is a
    concrete instantiation of the same model with the setup steps mapped to CLI
    commands. The pattern reference documents the token architecture; this page
    documents when and how to create each token in the setup sequence.
  - `docs-ghaw-central-repo-ops.md` Claim 10 (conflict detection as a mandatory
    worker safety gate): Claim 5 here is the same gate described from the practitioner
    setup perspective. The pattern reference documents the gate abstractly; this page
    shows it embedded in the worker workflow and explains its place in the overall flow.
  - `docs-ghaw-orchestration-patterns.md` Claim 2 (`dispatch-workflow` fans out via
    GitHub's `workflow_dispatch` API — async, independent worker runs): The worker
    here is invoked via `dispatch-workflow`, confirming the async fan-out model. The
    orchestration patterns note establishes the mechanism; this example page applies it.

- **Extends**:
  - `docs-ghaw-central-repo-ops.md`: That note covers the CentralRepoOps pattern as
    a design reference (what the pattern does, why, and what YAML it requires). This
    examples page extends it into the procedural layer: how to set it up, in what
    order, using what CLI commands, with what validation steps. Together they form the
    complete reference for a practitioner implementing this pattern: architectural
    understanding (central-repo-ops) + implementation procedure (this note).
  - `docs-ghaw-safe-rollout.md` (safe rollout framework — four-rung autonomy-promotion
    ladder): The "review a few worker PRs manually before full automation" practice from
    this examples page is an instantiation of the safe rollout principle. The safe-rollout
    note documents the framework abstractly; this example shows the specific manual
    validation step for org-scale configuration rollout. `max: 5` + manual review
    corresponds to the pilot-wave phase on the rollout ladder.
  - `docs-ghaw-multi-repo-ops.md` Claim 4 (hub-and-spoke topology, each component
    workflow creates tracking issues in a central repo via `target-repo`): This example
    uses the inverse topology — the central control plane dispatches workers to component
    repos (top-down CentralRepoOps), not bottom-up hub-and-spoke. The multi-repo-ops
    note establishes the topology taxonomy; this example is the CentralRepoOps (top-down)
    instance that contrasts with hub-and-spoke (bottom-up).

- **Contradicts**: None identified. The setup procedure, token model, and best practices
  are consistent with `docs-ghaw-central-repo-ops.md`, `docs-ghaw-orchestration-patterns.md`,
  and `docs-ghaw-multi-repo-ops.md`. No contradiction issue filed.

- **Novel**:
  - **Four-step setup sequence with ordered CLI commands** (Claim 1): No existing source
    note documents the setup procedure for the CentralRepoOps Dependabot Rollout pattern.
    `docs-ghaw-central-repo-ops.md` documents the pattern architecture but not the setup
    sequence. The compile-before-create-worker ordering and the per-step secret creation
    instructions are new to the corpus.
  - **Filter step as orchestrator idempotence guarantee** (Claim 2): The explicit
    "skip repos that already have Dependabot configured" first-task placement is documented
    here for the first time as an idempotence mechanism. The `docs-ghaw-central-repo-ops.md`
    Claim 8 covers the categorization scheme but does not specifically highlight the Filter
    step as an idempotence guarantee.
  - **Incremental scaling procedure: max: 5 → manual review → increase** (Claim 4):
    The specific procedure of starting conservative and reviewing before scaling is not
    documented in any existing corpus note. `docs-ghaw-central-repo-ops.md` Claim 2
    covers the `max` parameter as a blast-radius control; this note adds the "how to
    scale it safely" operational practice.
  - **Concurrency group key pattern for `workflow_dispatch` workers** (Claim 6):
    The specific key format `gh-aw-${{ github.workflow }}-${{ github.event.inputs.target_repo }}`
    for deduplication of target-keyed workers is not documented in any existing source
    note. The `docs-ghaw-central-repo-ops.md` worker YAML includes the concurrency
    group but does not explain it as a deduplication primitive.
  - **`[dependabot]` title prefix as org-wide filtering convention** (Claim 7):
    While `docs-ghaw-central-repo-ops.md` includes `title-prefix: '[dependabot] '`
    in the worker YAML, it does not explain the purpose or recommend it as a best
    practice convention. This examples page explicitly calls it out as a filtering
    and identification mechanism.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add four-step setup sequence as the implementation procedure for CentralRepoOps**
  (Claim 1): Pair with `docs-ghaw-central-repo-ops.md` as complementary references —
  architecture/design (central-repo-ops) and implementation/procedure (this note).
  Note the compile-before-worker ordering dependency: the orchestrator must be compiled
  before the worker can reference it via `dispatch-workflow`. Cross-reference the
  compilation model in `docs-ghaw-orchestration-patterns.md` Claim 5.

- **Add concurrency group key pattern for `workflow_dispatch` workers** (Claim 6):
  Any worker workflow accepting a target identifier as input should include a
  concurrency group keyed on `${{ github.workflow }}-${{ github.event.inputs.<target_input> }}`.
  Without this, concurrent orchestrator invocations can dispatch duplicate workers
  for the same target. Document as a required element, not an optimization.

- **Add title prefix as the org-wide filtering convention** (Claim 7): Workers that
  create PRs or issues in target repos should use consistent `title-prefix` values
  per operation type. The `[dependabot]` prefix is the reference example. Document
  as a required convention for any org-scale worker that creates visible outputs
  in external repositories.

- **Add Filter step as the orchestrator idempotence pattern** (Claim 2): Any
  orchestrator that rolls out configuration to org repos must check whether the
  target repo already has that configuration before dispatching a worker. The Filter
  step is the idempotence mechanism — without it, already-configured repos are
  re-processed and generate spurious conflict issues. Document as a required pattern
  for org-scale orchestrators.

### Chapter 03: Safety and Verification

- **Add conflict detection → issue output as the mandatory worker safety gate for
  configuration rollout** (Claim 5): When a worker would overwrite or conflict with
  existing tooling, it must create an issue (not a PR) and stop. No code changes
  should be made in the conflicting case. The conflict detection gate is the primary
  safety mechanism that makes org-scale configuration rollout safe to run.

- **Add three-PAT setup procedure as the reference implementation of least-privilege
  multi-repo token design** (Claim 8): Pair with `docs-ghaw-central-repo-ops.md`
  Claim 3 for the architecture; use this note for the "how to actually create each
  token in setup" procedural guidance.

### Chapter 05: Team Adoption

- **Add the incremental scaling procedure as the standard org-scale validation
  protocol** (Claim 4): Start with `max: 5`, review the worker outputs manually, then
  increase once quality is validated. Frame `max` as both a safety control and a
  pilot-wave selector. Cross-reference with `docs-ghaw-safe-rollout.md`'s rollout
  ladder framework.

- **Document the Summarize task as the governance artifact for org-scale operations**
  (Claim 9): Teams that adopt org-scale agentic rollout can audit the orchestrator's
  decisions via the GitHub Actions run log. The built-in summarization (total candidates,
  categorization breakdown, selected repos with rationale) enables post-hoc review
  without additional monitoring infrastructure.

## Extraction Notes

1. **Examples page vs. patterns page**: This source is in the `examples/multi-repo/`
   section, not the `patterns/` section. It provides a practitioner walkthrough with
   concrete setup steps, complementing the abstract CentralRepoOps pattern reference
   (`docs-ghaw-central-repo-ops.md`). The two pages cover largely the same architecture
   but at different abstraction levels.

2. **YAML consistency with `docs-ghaw-central-repo-ops.md`**: Three WebFetch passes
   were performed. The YAML in the Concrete Artifacts section is consistent across
   passes and matches the YAML already extracted in `docs-ghaw-central-repo-ops.md`
   Concrete Artifacts (that note extracted from the CentralRepoOps pattern page which
   includes the same Dependabot Rollout worked example). Minor formatting variations
   may exist between the two pages; the `docs-ghaw-central-repo-ops.md` YAML is the
   more complete reference.

3. **Verbatim quotes**: The Introduction, How It Works, Setup Steps, and Best Practices
   prose was captured via WebFetch. Quotes in this note are from the WebFetch output
   and are presented as verbatim; however, as WebFetch uses a model to process content,
   minor transcription variations cannot be ruled out. All YAML blocks are consistent
   with multiple passes and with `docs-ghaw-central-repo-ops.md`.

4. **No publication date**: The page does not carry an explicit publication date.
   Content is consistent with gh-aw platform behavior as of 2026-05-22.

5. **Sub-pages not followed**: The page links to the `patterns/central-repo-ops`
   reference and the `patterns/orchestration` reference as related pages. These are
   already covered by `docs-ghaw-central-repo-ops.md` and
   `docs-ghaw-orchestration-patterns.md` respectively.

6. **No contradictions filed**: Reviewed all existing corpus source notes. No claims
   in this source materially oppose existing source notes. The setup sequence, token
   model, and best practices are consistent with all related notes. No contradiction
   issue filed.
