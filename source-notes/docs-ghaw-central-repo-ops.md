---
source_url: https://github.github.com/gh-aw/patterns/central-repo-ops
source_type: docs
title: "GitHub Agentic Workflows: CentralRepoOps Pattern"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#321"
---

# GitHub Agentic Workflows: CentralRepoOps Pattern

> The CentralRepoOps pattern — a single private repository as a control plane for
> org-scale operations across hundreds of target repositories — is the most concrete
> multi-repo agent orchestration design in the GHAW corpus: it supplies extractable
> Orchestrator+Worker YAML, three-token permission architecture, bounded fan-out via
> `max`, and a phased rollout categorization scheme, all in one first-party reference.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns" section;
  not a blog post or practitioner account — first-party reference for the CentralRepoOps
  design pattern)
- **Author credibility**: GitHub Agentic Workflows team (the same team behind Peli de
  Halleux / Don Syme's agent factory series — see `blog-gh-aw-operations-release-workflows.md`
  for author background). First-party documentation for the `gh aw` platform. Claims about
  workflow structure, permission model, and fan-out behavior are settled for this platform;
  claims about general multi-agent orchestration should be treated as an implementation
  perspective, not a universal finding.
- **Scope**: The CentralRepoOps pattern in full — Orchestrator+Worker architecture,
  token/secrets configuration, fan-out control, trigger file vs. schedule trade-offs,
  cross-org deployment, phased rollout strategy, and best practices. Includes a complete
  worked example: a Dependabot Rollout orchestrator with categorization, prioritization,
  and bounded dispatch. Does NOT cover: single-repo operations (see companion pattern
  SideRepoOps), non-GHAW orchestration platforms, or general GitHub Actions primitives.

## Extracted Claims

### Claim 1: The Orchestrator+Worker split separates *where to operate* from *how to operate each repo*, making it a re-usable architectural pattern beyond gh-aw

- **Evidence**: The page explicitly states the two-role design: "Orchestrator Role:
  Decides where to roll out next. Filters and categorizes target repositories. Prioritizes
  rollout sequence. Dispatches workers with controlled fan-out. Worker Role: Executes how
  to configure each target repository. Receives target repository via `workflow_dispatch`
  input. Checks out target repository with appropriate credentials. Creates pull requests
  or issues in target repos." This is not just two workflows — it is a named architectural
  separation of policy from execution, applicable to any org-scale operation.
- **Confidence**: emerging (design-level claim; pattern is well-motivated and internally
  coherent, but real-world adoption at scale is not benchmarked in this documentation)
- **Quote**: "Orchestrator Role: Decides _where_ to roll out next … Worker Role:
  Executes _how_ to configure each target repository."
- **Our assessment**: The policy/execution separation is a strong architectural principle
  for multi-repo operations. The orchestrator holds the organizational view (which repos,
  in what priority order, under what constraints); the worker holds the repo-local view
  (what does this repo's structure require). This prevents the orchestrator from becoming
  a giant switch statement of per-repo special cases. The pattern directly implements
  Anthropic's orchestrator-subagent design (see `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 7 — the recommended default for multi-agent systems) in a concrete org-scale
  context. For Ch02 (Harness Engineering): name this split explicitly when recommending
  multi-repo agent architecture. For Ch04 (Multi-Agent Architecture): this is the
  orchestrator-subagent pattern instantiated at org scale, with concrete workflow YAML.

### Claim 2: Controlled fan-out via `max: 5` in `safe-outputs.dispatch-workflow` is the documented safety primitive for preventing runaway blast radius in org-scale operations

- **Evidence**: The orchestrator workflow frontmatter explicitly sets:
  ```yaml
  safe-outputs:
    dispatch-workflow:
      workflows: [dependabot-rollout]
      max: 5
  ```
  The page explains: "This configuration dispatches `dependabot-rollout` worker for every
  prioritized repository while limiting concurrent workers to 5. The `max` parameter
  prevents overwhelming the organization with simultaneous changes." Workers independently
  set `max: 1` for PR/issue creation, creating a two-level blast-radius cap.
- **Confidence**: settled (first-party documentation; this is a platform-enforced
  parameter, not a recommendation)
- **Quote**: "The `max` parameter prevents overwhelming the organization with simultaneous
  changes."
- **Our assessment**: The `max` parameter is not optional decoration — it is the mechanism
  that separates "controlled fan-out" from "uncontrolled blast". Without it, an orchestrator
  that dispatches workers for every repo in the organization can saturate GitHub API rate
  limits, flood review queues, or trigger accidental mass merges. The two-level cap (5
  concurrent workers, 1 PR/issue per worker) is a practical safety design: total PR
  creation rate ≤ 5 per orchestrator run. For Ch02: `max` in `dispatch-workflow` is a
  required field for any org-scale orchestrator harness, not an optional optimization.
  For Ch05 (Team Adoption): the `max` value is the knob for phased pilots — start with
  `max: 1` to validate the worker on one repo before scaling.

### Claim 3: The pattern requires three distinct fine-grained PATs, each with the minimum required permissions for its specific role

- **Evidence**: Three PATs are documented with explicit permission scopes:
  1. `GH_AW_READ_ORG_TOKEN` (orchestrator read access) — Contents: Read-only. Purpose:
     scan organization for candidate repositories.
  2. `ORG_REPO_CHECKOUT_TOKEN` (worker checkout) — Contents: Read & write, Actions:
     Read & write. Purpose: check out target repositories.
  3. `REPO_SAFE_OUTPUTS_TOKEN` (worker output delivery) — Contents: Write, Issues: Write,
     Pull Requests: Write. Purpose: create PRs and issues in target repositories.
- **Confidence**: settled (first-party documentation; token scope requirements are
  deterministic for the described operations)
- **Quote**: "Three fine-grained PATs enable the orchestrator-worker pattern"
- **Our assessment**: The three-token model is a concrete, opinionated implementation of
  least-privilege for multi-repo agent operations. The separation matters: if the orchestrator
  read token were also used for PR creation, a compromised orchestrator run could directly
  write to all target repos without the worker intermediary. By separating checkout
  credentials from output delivery credentials, the attack surface for each credential is
  minimized. From `docs-ghaw-how-they-work.md` (Claim 4), we know gh-aw defaults to no
  write access — this three-token model is how that principle is operationalized at the
  cross-repo level. For Ch03 (Safety and Verification): the three-token model is the
  reference architecture for any agentic system that operates across repository boundaries.
  Map token → role → minimum permission; do not share tokens between roles.

### Claim 4: The orchestrator creates a complete decision trail without ever pushing `main`-branch changes to individual target repositories

- **Evidence**: Best practice 1 in the page: "Keep orchestrator permissions narrow; delegate
  repo-specific writes to workers." The Prospector triage notes: "the control plane
  (orchestrator) never pushes main changes to individual repos — the audit log stays in one
  place." All target-repo changes are delivered via pull requests created by the worker,
  not direct pushes. The orchestrator's `GH_AW_READ_ORG_TOKEN` is read-only.
- **Confidence**: emerging (design intent documented; whether all organizations enforce
  this is not independently verified)
- **Quote**: "complete decision trail without pushing main changes to individual target
  repositories"
- **Our assessment**: The "no main-branch push from orchestrator" constraint is a
  significant governance guarantee. For security and compliance-conscious organizations,
  the ability to say "the automation system never directly modified a production branch —
  all changes went through PRs" is a meaningful audit point. The corollary is that
  rejecting a worker PR is the only human intervention point required — reviewers don't
  need to monitor CI logs or approve orchestrator dispatches, just review PRs in their
  own repo. For Ch05 (Team Adoption): this design is the key enabler for org-scale
  adoption. Teams accept the orchestrator's output by reviewing PRs in their own
  workflows, not by granting the orchestrator direct access.

### Claim 5: The trigger file architecture — a stable `.yml` referencing the `.lock.yml` via `workflow_call` — decouples trigger definition from agentic logic and enables trigger changes without recompilation

- **Evidence**: The page describes and illustrates two files: (1) the agentic orchestrator
  source (`.md` → compiled to `.lock.yml`), and (2) a stable trigger file
  (`.github/workflows/central-ops-trigger.yml`) that references the lock file via
  `workflow_call`. The trade-off table: Schedule Only requires a single file but only
  supports cron triggers and breaks on recompile; Trigger File + `workflow_call` requires
  two files but supports any GitHub event and survives recompilation (the trigger file
  references the compiled lock by name, which is stable).
- **Confidence**: settled (first-party documentation with explicit trade-off table)
- **Quote**: "Recompiling the orchestrator regenerates the lock file; the trigger file
  remains stable."
- **Our assessment**: This is a direct extension of the compilation model documented in
  `docs-ghaw-how-they-work.md` (Claim 7 — `.md` → `.lock.yml` separation). The trigger
  file pattern adds a third artifact: a stable `.yml` that references the lock file but
  is not itself recompiled. The practical impact: teams can wire up multiple trigger events
  (label applied, push to main, `workflow_dispatch`, scheduled) without touching the
  agentic logic, and the trigger definition can be modified independently. For Ch02:
  recommend the trigger file pattern as default for orchestrators that need event-driven
  scheduling, not just cron. The two-file overhead is worth the flexibility.

### Claim 6: Cross-repository trigger files enable application repos to invoke platform orchestrators without cross-org checkout by having `secrets: inherit` forward caller secrets

- **Evidence**: The page documents the cross-repository trigger pattern with a concrete
  example: a `platform-relay.yml` in an application repo calling `platform-gateway.lock.yml`
  in a platform repo via `uses:` with `secrets: inherit`. Requirements: platform repo must
  be accessible from the caller's organization (Settings → Actions → General → "Accessible
  from repositories in the organization"); caller must configure `COPILOT_GITHUB_TOKEN`;
  billing for premium Copilot requests goes to the caller's token.
- **Confidence**: emerging (design described; billing implications and visibility
  requirements may change with platform updates)
- **Quote**: "Caller repository must configure `COPILOT_GITHUB_TOKEN`. Premium Copilot
  requests bill to the caller's token, not the platform's."
- **Our assessment**: The cross-repo trigger pattern is notable for the billing model:
  the platform operator does not absorb the cost of agents invoked from application repos —
  each caller is billed for their own agent runs. This is a practical enabler for
  platform team adoption: a central platform can offer orchestration capabilities without
  absorbing unbounded AI costs from consumer repos. The `secrets: inherit` behavior means
  callers transparently provide their own credentials, including billing tokens, through
  the call chain. For Ch05 (Team Adoption): document the billing model explicitly so
  platform teams understand that they can provide the orchestration infrastructure without
  carrying the operational cost.

### Claim 7: Cross-organization deployments require `inlined-imports: true` to embed all shared resources at compile time, eliminating cross-org checkout at runtime

- **Evidence**: The page states: "When platform and caller repos span different
  organizations, use `inlined-imports: true`." This embeds all imported content into the
  `.lock.yml` at compile time. Trade-off explicitly documented: "any change to imported
  files requires recompilation." The `inlined-imports` frontmatter block causes the
  compiler to resolve all `imports:` references and embed them verbatim, making the lock
  file self-contained.
- **Confidence**: settled (first-party documentation; the trade-off is clearly stated)
- **Quote**: "This embeds all imported content into the `.lock.yml` at compile time,
  eliminating cross-organization checkout requirements. Trade-off: any change to imported
  files requires recompilation."
- **Our assessment**: The inlined-imports trade-off (self-contained lock file vs. staleness
  on imported resource change) is architecturally important for platform teams. Without
  inlining, a cross-org workflow must check out shared resources from the platform repo at
  runtime — requiring appropriate cross-org permissions that may not exist. Inlining solves
  this by front-loading the dependency resolution at compile time, converting a runtime
  permission requirement into a compile-time one (which is manageable by the platform
  team, not the caller). The cost: platform teams must recompile and re-publish the lock
  file when any imported resource changes. For Ch02 (Harness Engineering): `inlined-imports`
  is the correct choice for cross-org shared library distribution; same-org deployments
  can rely on runtime checkout.

### Claim 8: The phased rollout categorization strategy — simple → security → complex → conflicting — provides a concrete governance template for prioritizing org-scale operations

- **Evidence**: The Dependabot Rollout orchestrator implements a four-category
  classification scheme: Simple (single package.json, <50 deps, standard structure);
  Complex (multiple package.json, >100 deps, or multiple ecosystems); Conflicting (has
  Renovate config or custom update scripts); Security (open security alerts or public
  with dependencies). Prioritization order: simple → security → complex → conflicting.
  The page describes this as the orchestrator's "Categorize" and "Prioritize" steps.
- **Confidence**: anecdotal (this specific scheme is the worked example; it is not a
  universal formula — other organizations will have different complexity signals)
- **Quote**: "Prioritize — Order repos by rollout preference: simple → security →
  complex → conflicting"
- **Our assessment**: The ordering is instructive as a template: start with the easiest
  repos (lowest risk, highest success rate) to validate the worker before tackling the
  hard cases. Security repos get elevated priority despite complexity because the benefit
  (closing security gaps) outweighs the operational risk. Conflicting repos (those with
  competing tooling) are deferred because they require human judgment to resolve conflicts
  — the agent can detect the conflict but cannot safely resolve it. This is a concrete
  instantiation of the "pilot wave" approach mentioned in the page's best practices:
  "Phased rollout (pilot waves), security-aware prioritization, central governance
  patterns." For Ch05: the categorize → prioritize → dispatch loop is a reusable
  governance template for any org-scale agent operation, not just Dependabot rollout.
  Adapt the category definitions to the domain.

### Claim 9: Workers should explain their reasoning in PR/issue bodies rather than applying generic templates, because the AI's value is in analysis not template instantiation

- **Evidence**: The Dependabot Rollout worker includes explicit instructions in its prompt:
  "Key: Explain Your Reasoning. In the PR/issue body, explain why you chose this specific
  configuration (not a generic template)." Best practice 6 in the page: "Explain worker
  reasoning in pull request/issue bodies rather than applying generic templates." The
  worker analyzes repository structure (dependency count, ecosystem type, monorepo
  detection, security alert status) before generating a configuration.
- **Confidence**: anecdotal (design guidance from the platform team; no metric comparing
  PR acceptance rates for templated vs. explained PRs)
- **Quote**: "Based on your analysis, create an appropriate config" and "explain why you
  chose this specific configuration (not a generic template)"
- **Our assessment**: This claim is the most directly applicable to Ch01 (Daily Workflows).
  The argument is that an agent adding a Dependabot config should analyze *this* repo and
  explain *this* repo's configuration choices — not clone a generic template. This
  produces PRs reviewers can actually evaluate (does the reasoning match what I know about
  this repo?). Without explanation, the PR is opaque: reviewers cannot verify whether the
  agent made a good choice or just applied a one-size-fits-all template. This is consistent
  with `blog-gh-aw-operations-release-workflows.md` Claim 2 (release automation works
  because it has unambiguous success criteria — the PR body is where those criteria are
  surfaced to reviewers). For Ch02 (Harness Engineering): instruct workers to include
  analysis rationale in their outputs, not just the output artifact.

### Claim 10: Conflict detection before overwriting is a mandatory worker safety gate — workers must check for existing tooling (Renovate, custom scripts) before applying changes

- **Evidence**: The worker workflow includes an explicit conflict detection step: "Check
  for conflicts: Does `.github/dependabot.yml` already exist? → Stop, create issue
  explaining it exists. Does `.github/renovate.json` or `renovate.json` exist? → Create
  issue about migrating from Renovate. Are there custom dependency update scripts? →
  Create issue suggesting Dependabot alternative." Workers create issues instead of PRs
  when conflicts are detected.
- **Confidence**: emerging (design described in the worked example; generalizes to any
  org-scale operation that touches existing configurations)
- **Quote**: "Does `.github/renovate.json` or `renovate.json` exist? → Create issue
  about migrating from Renovate"
- **Our assessment**: Conflict detection before overwriting is the primary safety gate
  that makes the CentralRepoOps pattern safe at scale. Without it, the orchestrator would
  dispatch workers that overwrite Renovate configurations with Dependabot configurations
  — destroying existing dependency management setups in potentially hundreds of repos.
  The issue-instead-of-PR output is the correct behavior for conflicts: it flags the
  problem for human resolution without making any changes. This is consistent with the
  "no main branch push" principle (Claim 4) — even the fallback path (creating an issue)
  does not modify code. For Ch03 (Safety and Verification): any org-scale worker that
  modifies existing configurations must include a conflict detection gate as its first
  step. Define "conflict" explicitly in the worker prompt — don't rely on the agent to
  infer what constitutes a collision.

## Concrete Artifacts

### Complete Orchestrator Workflow Frontmatter (Dependabot Rollout)

From the CentralRepoOps documentation. Exact YAML structure is as documented; verify
against current gh-aw documentation before using in production.

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

### Complete Worker Workflow Frontmatter (Dependabot Rollout)

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

### Three-Token Permission Model for Cross-Repo Operations

```
Token 1: GH_AW_READ_ORG_TOKEN
  Scope: Organization owner, all repositories
  Permission: Contents: Read-only
  Used by: Orchestrator (scanning for candidate repos)

Token 2: ORG_REPO_CHECKOUT_TOKEN
  Scope: Organization owner, all repositories
  Permissions: Contents: Read & write, Actions: Read & write
  Used by: Worker (checking out target repositories)

Token 3: REPO_SAFE_OUTPUTS_TOKEN (GH_AW_CROSS_REPO_PAT)
  Scope: Organization owner, all repositories
  Permissions: Contents: Write, Issues: Write, Pull Requests: Write
  Used by: Worker safe-outputs (creating PRs and issues in target repos)

Design principle: Each token corresponds to exactly one role.
No token grants capabilities beyond its role's minimum requirement.
```

### Trigger File Architecture (Two-File Pattern)

```yaml
# File 1: .github/workflows/dependabot-rollout-orchestrator.md (source)
#          compiled to: dependabot-rollout-orchestrator.lock.yml
# (Agentic logic lives here; recompiled when logic changes)

# File 2: .github/workflows/central-ops-trigger.yml (STABLE — never recompiled)
name: Central Ops Trigger
on:
  issues:
    types: [labeled]
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      reason:
        description: "Reason for manual trigger"
        required: false
        default: "manual"

jobs:
  trigger:
    uses: ./.github/workflows/dependabot-rollout-orchestrator.lock.yml
    with:
      reason: ${{ github.event_name }}
    secrets: inherit

# The trigger file references the LOCK FILE (stable name), enabling trigger
# definition changes without recompilation. Adding a new event trigger = edit
# this file only. Changing agent logic = edit the .md source and recompile.
```

### Cross-Organization Deployment via `inlined-imports`

```markdown
---
on:
  workflow_call:

engine: copilot
inlined-imports: true     # Embeds all imports into .lock.yml at compile time

imports:
  - shared/common-tools.md
  - shared/security-setup.md
---
# Platform Gateway Workflow
# (all imports are embedded; no cross-org checkout required at runtime)
```

### Schedule vs. Trigger File Trade-off Table

```
Aspect                        | Schedule Only      | Trigger File + workflow_call
------------------------------|--------------------|---------------------------------
Setup                         | Single file        | Two files (orchestrator + trigger)
Trigger flexibility           | Cron/schedule only | Any GitHub event
Change without recompile      | No                 | Yes (edit trigger file only)
Pass event context to agent   | No                 | Yes via workflow_call inputs
Stability across recompiles   | Breaks on recompile| Fixed (references lock file name)
When to use                   | Simple recurring   | Event-driven or flexible scheduling
```

### Conflict Detection Decision Tree (Worker Safety Gate)

```
On entry, worker checks:
  1. Does .github/dependabot.yml exist?
     → YES: Stop. Create issue: "dependabot.yml already exists."
  2. Does .github/renovate.json or renovate.json exist?
     → YES: Create issue: "Renovate config found — migration required."
  3. Are there custom dependency update scripts?
     → YES: Create issue: "Custom scripts found — review before automating."
  4. No conflicts found → Proceed to analysis and PR creation.

Output for conflicts: ISSUE (not PR). No code changes made.
Output for clean repos: PR with customized config + reasoning in body.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default") and Claim 5
    (Safe Outputs as permission-separation primitive): The three-token model and worker
    `safe-outputs.create-pull-request` configuration are the concrete multi-repo
    implementation of the Safe Outputs and no-write-by-default principles that
    `docs-ghaw-how-they-work.md` describes at the conceptual level. Together: conceptual
    principle (how-they-work) + org-scale implementation (this note).
  - `docs-ghaw-how-they-work.md` Claim 7 (compilation model — `.md` → `.lock.yml`):
    The trigger file pattern here extends that model with a third artifact (the stable
    `.yml` trigger file referencing the lock file). `docs-ghaw-how-they-work.md`
    documents the two-file model (source + lock); this note documents the three-file
    model (source + lock + stable trigger) as the production pattern for event-driven
    orchestrators.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 (orchestrator-subagent
    as the recommended default for multi-agent systems) and Claim 2 (context-centric
    decomposition): The CentralRepoOps Orchestrator+Worker split is a concrete
    implementation of the orchestrator-subagent pattern, instantiated at org scale
    with bounded fan-out. The three-token permission model is consistent with
    context-centric decomposition — each agent role has exactly the context (credentials,
    permissions, target scope) it needs, no more.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` / lock file
    separation): The Changeset Generator's compilation model is the same mechanism used
    here. This note is the multi-repo extension of what that blog post established for
    single-repo release workflows.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: That note covers the GHAW conceptual architecture
    (Safe Outputs, five-layer security, compilation model). This note covers the
    CentralRepoOps pattern — a concrete multi-repo architecture that applies those
    conceptual primitives. Together they form the complete reference: conceptual
    foundations (how-they-work) + org-scale application (this note).
  - `blog-gh-aw-operations-release-workflows.md`: That note covers single-repo
    orchestration for release workflows. This note extends to multi-repo fan-out —
    the orchestrator concept introduced for one repo is applied to an organization.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 12 (start simple,
    evolve based on observed failure modes): The CentralRepoOps pattern provides the
    implementation that practitioners can start from — a complete, working orchestrator-
    subagent design for a real class of problems. The Anthropic taxonomy describes
    the pattern topology; this note provides the working instantiation.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 7 (cross-repo workflow reliability improvements
    in v0.65.x): The reliability improvements noted in that release directly support the
    CentralRepoOps use case. Per-tool-call metrics (`gh aw logs`) would surface which
    dispatch calls fail; MCP keepalive configuration ensures long-running orchestrators
    don't lose tool connectivity.

- **Contradicts**: None. No existing source note makes claims that materially oppose the
  Orchestrator+Worker split, the three-token model, the fan-out `max` primitive, or the
  trigger file architecture described here. The single-repo orchestration in
  `blog-gh-aw-operations-release-workflows.md` is a simpler version of the same pattern,
  not a contradiction. No contradiction issue needs to be filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Multi-repo Orchestrator+Worker as a named architectural pattern with YAML**: No
    prior corpus source provides complete orchestrator and worker workflow YAML for a
    multi-repo agent operation. The conceptual pattern (orchestrator dispatches workers)
    existed in `blog-anthropic-multi-agent-coordination-patterns.md` and
    `docs-ghaw-how-they-work.md`, but the concrete implementation was absent.
  - **Three-token permission model for cross-repo operations**: No prior source in the
    corpus specifies a role-based token architecture for multi-repo agent operations.
    The `docs-ghaw-how-they-work.md` Safe Outputs principle is the conceptual foundation;
    this is the concrete permission design.
  - **Bounded fan-out via `max` in `dispatch-workflow`**: The `max` parameter as a
    blast-radius control mechanism in multi-agent dispatch is documented here for the
    first time. The weekly notes reference fan-out improvements but don't document
    this specific primitive.
  - **Trigger file as a third compilation artifact**: The stable `.yml` trigger file
    pattern (distinct from both `.md` source and `.lock.yml` executable) is new to the
    corpus.
  - **Phased rollout categorization scheme**: Simple → security → complex → conflicting
    as an explicit governance-aware prioritization template for org-scale operations.
  - **`inlined-imports: true` for cross-org deployments**: Compile-time import embedding
    as the solution for cross-organization shared resource distribution is not described
    in any prior source note.
  - **Conflict detection gate as a mandatory worker safety pattern**: The check-before-
    write pattern (detect Renovate, existing configs, custom scripts; create issue instead
    of PR on conflict) is new to the corpus as an explicit safety gate.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add Orchestrator+Worker split as a named multi-repo harness pattern** (Claim 1): The
  guide currently covers single-agent and basic orchestration. Add this as the canonical
  reference for multi-repo agent architecture: policy in the orchestrator, execution in
  workers. Reference this note's YAML artifacts as the starting template. Cross-reference
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 for the foundational pattern.
- **Add `max` in `dispatch-workflow` as a required field for multi-repo orchestrators**
  (Claim 2): Frame as a safety requirement, not an optimization. Document the two-level cap
  (orchestrator `max: 5`, worker `max: 1` per PR/issue). Recommend starting with `max: 1`
  for pilot validation before scaling.
- **Add three-token model as the cross-repo permission reference** (Claim 3): Pair with
  `docs-ghaw-how-they-work.md`'s Safe Outputs discussion. The model is: one token per
  role, each scoped to minimum permissions. Generalize beyond GHAW — any multi-repo
  agent operation should define an explicit token architecture before implementation.
- **Add trigger file pattern as default for event-driven orchestrators** (Claim 5): The
  two-file pattern (`.md` source + stable `.yml` trigger) should be the standard
  recommendation over schedule-only for orchestrators that need flexibility. The
  trade-off table (Concrete Artifacts) is the decision aid.
- **Add conflict detection gate as a required worker pattern** (Claim 10): Document the
  check-before-write pattern as a harness safety requirement for any worker that modifies
  existing configurations. Define the conflict types relevant to the operation; output
  issues not PRs on detection.

### Chapter 04: Multi-Agent Architecture

- **Use CentralRepoOps as the worked example for orchestrator-subagent at org scale**
  (Claims 1, 2, 8): The Dependabot Rollout example is the most concrete orchestrator-
  subagent implementation in the corpus with real workflow YAML. It demonstrates:
  categorization as orchestrator policy, bounded dispatch as fan-out control, and
  per-repo execution as stateless worker design. Pair with `blog-anthropic-multi-agent-
  coordination-patterns.md`'s taxonomy.
- **Add phased rollout categorization as a governance template** (Claim 8): The simple
  → security → complex → conflicting ordering is an exportable template. Teams can adapt
  the categorization dimensions (what counts as "complex" or "conflicting" for their
  domain) while preserving the ordering logic (de-risk first, handle conflicts last).

### Chapter 05: Team Adoption

- **Add decision-trail guarantee as an adoption enabler** (Claim 4): For org-scale agent
  adoption, the "no direct main-branch writes from the control plane" guarantee is a key
  trust mechanism. Teams that adopt CentralRepoOps can tell their stakeholders: all changes
  arrive as PRs in your repo's normal review workflow. Document this as the governance
  argument for centralized agent orchestration.
- **Document cross-repo billing model for platform teams** (Claim 6): If a platform team
  provides an orchestration service to application teams, clarify that billing follows
  the caller's token. Platform teams do not absorb unbounded AI costs from consumer adoption.
- **Add pilot wave methodology** (Claims 2, 8): Recommend starting with `max: 1` on a
  small cohort of simple repos before scaling. The categorization scheme provides the
  selection logic for the pilot cohort.

### Chapter 03: Safety and Verification

- **Three-token model as the cross-repo least-privilege reference** (Claim 3): Extend
  the `docs-ghaw-how-they-work.md` "zero capability by default" principle to the cross-repo
  case. Each credential has one role; no role shares credentials with another.
- **`inlined-imports` for cross-org hardening** (Claim 7): When sharing agentic workflows
  across org boundaries, inline imports at compile time to eliminate runtime cross-org
  checkout. Document the recompile-on-change requirement as the trade-off.

## Extraction Notes

1. **Source is first-party official documentation**: This is not a blog post or practitioner
   account — it is the authoritative pattern reference from the GHAW team. Claims about
   platform mechanics (token scopes, `max` parameter, `inlined-imports`) are settled for
   this platform.
2. **Workflow YAML reconstructed from docs**: The orchestrator and worker YAML were
   reconstructed from the page's complete worked example. Minor formatting variations from
   production YAML are possible; verify against `gh aw` CLI documentation before use.
3. **No explicit publication date**: Content is consistent with gh-aw v0.45–v0.62.x era
   (post-Dec 2025) based on the `safe-outputs` API surface described. `date_published`
   left null.
4. **Related patterns noted but not extracted**: The page references MultiRepoOps,
   SideRepoOps, and Cross-Repository Operations as related patterns. These were not
   followed as they are likely covered by companion pattern pages (separate source
   submissions may be warranted).
5. **No contradictions filed**: Reviewed all corpus source notes. No existing claim
   materially opposes CentralRepoOps design decisions. The multi-repo extension of Safe
   Outputs and the orchestrator-subagent pattern are consistent with all prior corpus sources.
