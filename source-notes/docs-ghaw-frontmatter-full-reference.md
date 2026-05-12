---
source_url: https://github.github.com/gh-aw/reference/frontmatter-full
source_type: docs
title: "GitHub Agentic Workflows: Full Frontmatter Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#429"
---

# GitHub Agentic Workflows: Full Frontmatter Reference

> The complete schema-level catalog of all gh-aw frontmatter fields — trigger
> taxonomy (slash commands, label commands, schedule, GitHub events), conditional
> skip gate system, execution lifecycle hooks, extensible engine configuration
> (including custom providers with OAuth), A/B experiment support, and tracker-id
> tagging — the ground truth for what is configurable before a single line of
> markdown instruction is written.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/frontmatter-full`
  page — in the "Reference" section. The page explicitly states it is
  "automatically generated from JSON Schema for validating agentic workflow
  frontmatter configuration." This makes it the authoritative machine-readable
  spec, not an editorial document. Distinct from individual reference pages
  (`reference/permissions`, `reference/sandbox`, `reference/network`,
  `reference/tools`) that cover single sections in depth — this page catalogs
  all fields in one place.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the
  `gh aw` CLI. Because the content is generated from JSON Schema rather than
  written by hand, field names, types, defaults, and valid values are authoritative
  platform facts. The schema itself is the contract — not a practitioner's
  summary of what works.
- **Scope**: Complete field catalog for the YAML frontmatter section of gh-aw
  workflow files: workflow identity fields, imports, trigger configuration (all
  trigger types and their sub-fields), conditional skip options, permissions,
  execution configuration, features/experiments, engine configuration (including
  custom provider/runtime definitions), sandbox, network, tools, workflow step
  lifecycle hooks, container/service configuration, and concurrency. Does NOT
  cover: individual field *behavior* in depth (see the dedicated reference pages:
  `docs-ghaw-permissions-reference.md`, `docs-ghaw-sandbox-reference.md`,
  `docs-ghaw-network-reference.md`, `docs-ghaw-tools-reference.md`,
  `docs-ghaw-concurrency-reference.md`); markdown body syntax and templating
  (see `docs-ghaw-templating-reference.md`); workflow file anatomy (see
  `docs-ghaw-workflow-structure-reference.md` in PR #688).

## Extracted Claims

### Claim 1: The frontmatter-full reference is automatically generated from JSON Schema — it is the machine-readable contract for what fields are valid, not an editorial summary

- **Evidence**: The page states it provides "JSON Schema for validating agentic
  workflow frontmatter configuration." The field list and type annotations are
  derived from the schema itself, not from human-written documentation.
- **Confidence**: settled (first-party documentation; the schema-generated
  status is explicitly stated on the page)
- **Quote**: (no direct quote available; see paraphrase in Our assessment)
- **Our assessment**: The "generated from JSON Schema" provenance means this
  page is the closest thing to a grammar spec for workflow frontmatter. If a
  field exists here, it is valid. If it does not, it is not. This matters for
  practitioners who want to know the complete configuration surface without
  reading multiple individual reference pages. For Ch02 (Harness Engineering):
  point practitioners to this page as the authoritative field index when
  debugging or designing a new workflow. The individual reference pages
  (`permissions`, `sandbox`, etc.) remain better for understanding *why* a
  field exists and what it means — this page is the index.

### Claim 2: There are five trigger categories (slash_command, label_command, schedule, standard GitHub events, workflow_run/dispatch) with 50+ configurable sub-fields collectively

- **Evidence**: The page enumerates `on.slash_command`, `on.label_command`,
  `on.schedule`, `on.push`, `on.pull_request`, `on.issues`, `on.issue_comment`,
  `on.discussion`, `on.discussion_comment`, `on.workflow_dispatch`,
  `on.workflow_run`, plus numerous GitHub API event types (release,
  deployment_status, check_run, merge_group, etc.). Each has between 2 and 9
  named sub-fields.
- **Confidence**: settled (first-party reference; field list is schema-derived)
- **Quote**: "Workflow triggers defining when agentic workflow should run"
  (description of the `on` field)
- **Our assessment**: The trigger taxonomy spans two paradigms: *agentic*
  triggers (`slash_command`, `label_command`) that are specific to human/agent
  interaction patterns and *GitHub Actions* triggers (`push`, `pull_request`,
  `issues`) that map directly to GitHub's event model. Practitioners need to
  pick the right trigger class: slash commands for human-invoked workflows,
  label commands for label-gated workflows, schedule for periodic maintenance,
  and standard events for reactive automation. The `workflow_run` trigger
  enables workflow orchestration — one workflow completing triggers another.
  For Ch02: document the trigger taxonomy as the first design decision in
  workflow authoring — who or what activates this agent, and under what
  circumstances?

### Claim 3: Six conditional skip options form a precondition gate system that runs before the AI engine is invoked — enabling cost-saving short-circuits based on search queries, CI status, user roles, and bot identity

- **Evidence**: The page documents: `on.skip-if-match` (skip if GitHub search
  query has matches), `on.skip-if-no-match` (skip if query has no matches),
  `on.skip-if-check-failing` (skip if CI checks failing/pending on target
  branch), `on.skip-roles` (skip for users with specific repo roles),
  `on.skip-bots` (skip for specific GitHub usernames/bots), and `on.roles`
  (require specific repo roles to trigger). Each has sub-fields for
  configuration (e.g., `query`, `max`, `scope`, `include`, `exclude`,
  `allow-pending`, `branch`).
- **Confidence**: settled (first-party reference; schema-derived field list)
- **Quote**: "Skip workflow if GitHub search query has matches" (description
  of `on.skip-if-match`)
- **Our assessment**: The skip options are a cost-control and correctness
  mechanism. Before the AI engine runs (and incurs token costs), the workflow
  can check whether running makes sense: is there already an open PR for this
  issue? Are CI checks green? Is the triggering user a maintainer? Each check
  is a declarative precondition, not logic in the AI instructions. This is
  architecturally significant: it keeps guard logic out of the AI prompt
  (where it is harder to reason about and may not be followed reliably) and
  puts it in the frontmatter (where it is validated at compile time and
  executed deterministically). For Ch02 (Harness Engineering): the skip
  conditions are the first line of cost control. For Ch03 (Safety): role-based
  access control via `on.roles` and `on.skip-roles` is the frontmatter-level
  authorization layer.

### Claim 4: on.manual-approval enables environment-gated human pre-approval before the AI engine runs — workflow-level HITL, not just action-level

- **Evidence**: The field `on.manual-approval` is described as "Environment
  name requiring manual approval before workflow runs." It uses GitHub's
  environment protection rules mechanism (the same system used for deployment
  approvals in standard GitHub Actions).
- **Confidence**: settled (first-party reference; field is schema-derived)
- **Quote**: "Environment name requiring manual approval before workflow runs"
  (field description)
- **Our assessment**: This is distinct from action-level human approval (the
  `critical actions can require human approval` capability from
  `docs-ghaw-how-they-work.md` Claim 10, which gates individual Safe Outputs
  operations). `on.manual-approval` gates the *entire workflow* before it
  starts — the AI engine does not run at all until a human approves. This
  is the correct mechanism for high-stakes workflows (e.g., a workflow that
  modifies production configuration) where you want a human to explicitly
  greenlight each run rather than reviewing outputs after the fact. For Ch03:
  there are now two HITL points in the gh-aw architecture — pre-workflow
  (`on.manual-approval`) and per-action (critical Safe Outputs approval).
  Practitioners should understand both and choose the right granularity.

### Claim 5: engine configuration supports fully custom provider/runtime definitions with OAuth 2.0 authentication — workflows are not limited to the four named engines (claude, copilot, codex, gemini)

- **Evidence**: The page documents `engine.runtime.id` (accepts named adapters:
  codex, claude, copilot, gemini, crush), `engine.provider.id` (accepts:
  openai, anthropic, github, google), `engine.provider.auth` with
  `strategy: 'api-key'` or `strategy: 'oauth-client-credentials'`, and
  OAuth-specific fields (`token-url`, `client-id`, `client-secret`,
  `token-field`). Also documents `engine.provider.request` with
  `path-template`, `query`, and `body-inject` for non-standard API endpoints.
- **Confidence**: settled (first-party reference; schema-derived field list)
- **Quote**: "Provider identifier (openai, anthropic, github, google)" (field
  description for `engine.provider.id`)
- **Our assessment**: The inline engine definition capability (via
  `engine.runtime` + `engine.provider`) means gh-aw is extensible to any
  inference API, not just the four named built-ins. This is significant for
  enterprises running private model deployments (GHEC, GHES, or custom) —
  they can configure OAuth-authenticated access to internal model endpoints.
  The `engine.api-target` field explicitly names "GHEC, GHES, custom" as
  valid targets. For Ch02: document that engine configuration is a three-tier
  choice — (1) named engine shorthand (e.g., `engine: claude`), (2) named
  engine with model override (`engine.model`), (3) fully custom
  runtime/provider definition for non-standard endpoints.

### Claim 6: engine.max-turns limits AI chat iterations per run — the explicit anti-runaway-loop mechanism for agentic workflows

- **Evidence**: The field `engine.max-turns` is described as "Maximum chat
  iterations per run (prevents runaway loops)." The field description uses
  the phrase "prevents runaway loops" explicitly, naming the safety purpose.
- **Confidence**: settled (first-party reference; the anti-runaway intent is
  explicitly stated in the field description)
- **Quote**: "Maximum chat iterations per run (prevents runaway loops)"
  (field description for `engine.max-turns`)
- **Our assessment**: This is the frontmatter-level turn limit, distinct from
  the token cost runaway detection via `gh aw logs` described in
  `docs-ghaw-how-they-work.md` Claim 11. `max-turns` is a hard structural
  limit (the workflow stops after N turns regardless of what the AI wants
  to do); `gh aw logs` is observability after the fact. Together they form
  two layers of runaway protection. For Ch02: recommend setting `max-turns`
  as a default discipline for agentic workflows — pick a number that fits
  the task complexity (e.g., 5 for simple label operations, 20 for multi-step
  analysis) rather than leaving it unlimited.

### Claim 7: engine.bare mode disables auto-loading of context/custom instructions — for workflows that need full control over the AI context window

- **Evidence**: The field `engine.bare` is described as "Disable auto-loading
  of context/custom instructions." It is a boolean field.
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "Disable auto-loading of context/custom instructions" (field
  description for `engine.bare`)
- **Our assessment**: In normal mode, gh-aw automatically injects context
  (repository CLAUDE.md or equivalent, custom instructions, etc.) into the
  AI's context window before the workflow markdown. `engine.bare` disables
  this, giving the workflow author full control over what the AI sees. This
  matters for specialized workflows where the default context injection might
  confuse the AI or pollute results — e.g., a security audit workflow where
  CLAUDE.md's permissive guidance shouldn't apply. For Ch04 (Context
  Engineering): `engine.bare` is the escape hatch when default context
  injection is a problem. Recommend using it deliberately, with the tradeoff
  documented: you gain full context control but lose the automatic context
  sharing that custom instructions provide.

### Claim 8: The experiments field supports A/B testing with variants and configurable storage — enabling statistical workflow iteration with 'cache' (ephemeral) or 'repo' (persistent) storage

- **Evidence**: The page documents an `experiments` object with
  `experiments.storage` described as "'cache' or 'repo' (default); 'repo'
  persists to git branch." The parent `experiments` field description says
  "A/B testing experiments with variants and metadata."
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "'cache' or 'repo' (default); 'repo' persists to git branch"
  (description of `experiments.storage`)
- **Our assessment**: The experiments capability suggests gh-aw supports
  statistical workflow evaluation natively — you can define workflow variants,
  run them against incoming triggers, and persist results either ephemerally
  (cache, for quick iteration) or permanently (git branch, for long-term
  analysis). This is relevant for teams that want to measure whether a new
  version of an agent workflow performs better than the old version on real
  traffic. For Ch02: `experiments` is the platform's built-in A/B testing
  mechanism for workflow improvement loops. The `storage: 'repo'` option is
  particularly interesting because it stores experiment state in git history,
  making results auditable and reproducible.

### Claim 9: The tracker-id field tags all workflow-created assets with a durable identifier — enabling lifecycle management of agent-created artifacts

- **Evidence**: The field `tracker-id` is described as "Optional identifier
  to tag created assets; 8+ alphanumeric chars, hyphens, underscores."
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "Optional identifier to tag created assets; 8+ alphanumeric
  chars, hyphens, underscores" (field description for `tracker-id`)
- **Our assessment**: `tracker-id` is an asset provenance mechanism — all
  GitHub objects (issues, PRs, comments, labels) created by a workflow run
  carrying a `tracker-id` get tagged with that identifier. This enables
  lifecycle operations like "find and close all issues created by
  workflow X," "delete all PRs from the last test run," or "audit all
  assets created by agent Y." It's the complement to the Safe Outputs
  audit trail: Safe Outputs records *that* something was created; tracker-id
  records *by whom* (which workflow). For Ch02: recommend setting `tracker-id`
  for any workflow that creates GitHub objects at scale — it's the difference
  between "agent created 50 issues" and "agent created 50 issues that can
  be retrieved and cleaned up later."

### Claim 10: Minimum schedule interval is 5 minutes — platform-enforced minimum for periodic agentic workflows

- **Evidence**: The page states: "Minimum interval is 5 minutes" in the
  context of the `on.schedule` field. The schedule field supports both
  natural language ("daily", "weekly", "hourly", "every 2h") and cron syntax.
- **Confidence**: settled (first-party reference; explicitly stated constraint)
- **Quote**: "Minimum interval is 5 minutes" (scheduling constraint)
- **Our assessment**: The 5-minute minimum prevents runaway schedule storms
  and aligns with GitHub Actions' own scheduling constraints. The natural
  language schedule options ("daily", "weekly", "hourly") are a UX convenience
  on top of the underlying cron semantics. For Ch01 (Daily Workflows): when
  designing maintenance workflows (daily doc freshness checks, weekly
  dependency audits), the schedule trigger is the right mechanism — document
  that the minimum granularity is 5 minutes and that natural language is
  acceptable syntax.

### Claim 11: on.lock-for-agent in issues and issue_comment triggers prevents concurrent agent modifications — an issue-level mutex pattern

- **Evidence**: The field `on.issues.lock-for-agent` is described as "Lock
  issue for agent when workflow runs; prevents concurrent modifications."
  Similarly, `on.issue_comment.lock-for-agent` is "Lock parent issue for
  agent to prevent concurrent modifications."
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "Lock issue for agent when workflow runs; prevents concurrent
  modifications" (description of `on.issues.lock-for-agent`)
- **Our assessment**: `lock-for-agent` is a frontend-level concurrency
  primitive for GitHub issue operations. Without it, two concurrent workflow
  runs triggered by different events on the same issue could create race
  conditions (e.g., two agents adding conflicting comments, or one agent
  reading stale issue state after another has modified it). With it, the
  platform serializes access to the issue. This is complementary to the
  workflow-level concurrency groups in `docs-ghaw-concurrency-reference.md`
  — concurrency groups prevent two instances of the *same workflow* from
  running simultaneously; `lock-for-agent` prevents two *different workflows*
  from touching the same issue concurrently. For Ch03: recommend enabling
  `lock-for-agent` for any issue-processing workflow that reads then writes
  issue state — the correctness property it provides is worth the serialization
  cost.

### Claim 12: Execution lifecycle has four injection points — pre-steps (before checkout), steps (after built-in checks), pre-agent-steps (after init, before AI), and post-steps (after AI) — enabling structured workflow composition

- **Evidence**: The page documents four step injection fields:
  `pre-steps` ("Steps at beginning before checkout; for token minting/setup"),
  `steps` ("Custom workflow steps"),
  `pre-agent-steps` ("Steps before AI execution after initialization"),
  `post-steps` ("Steps after AI execution"). Additionally, `on.steps`
  provides "Steps injected into pre-activation job after built-in checks."
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "Steps before AI execution after initialization" (description
  of `pre-agent-steps`)
- **Our assessment**: The four-point lifecycle structure enables precise
  injection of custom logic around the AI execution. The most important
  distinction is `pre-steps` (runs before checkout — for secrets setup,
  custom token minting, environment bootstrapping) vs. `pre-agent-steps`
  (runs after checkout and init — for custom context preparation, data
  fetching, tool setup that needs the repo present). `post-steps` enables
  cleanup, notification, or result processing after the AI finishes.
  For Ch02: document these four lifecycle hooks as the composability model
  for gh-aw harnesses. A workflow is not just "frontmatter + markdown" —
  the step hooks are where custom harness logic lives when it cannot be
  expressed declaratively.

### Claim 13: inlined-imports boolean at compile time materializes all imported workflow specs into the lock.yml — trading flexibility for full portability

- **Evidence**: The field `inlined-imports` is described as "If true, inline
  all imports at compilation time in generated lock.yml."
- **Confidence**: settled (first-party reference; schema-derived)
- **Quote**: "If true, inline all imports at compilation time in generated
  lock.yml" (field description)
- **Our assessment**: Without `inlined-imports`, imported shared workflow
  specs are referenced by path or cross-repo coordinate — the lock.yml
  contains a pointer that is resolved at runtime. With `inlined-imports:
  true`, all imports are resolved at compile time and embedded in the
  lock.yml, making the compiled artifact self-contained. This tradeoff:
  without inlining, updates to shared imports propagate automatically; with
  inlining, the workflow is frozen at compile-time versions but is fully
  portable and auditable without remote dependencies. For Ch02: `inlined-imports`
  is the "snapshot vs. live reference" choice for shared component libraries.
  Recommend inlining for production workflows (reproducibility) and live
  references for development (easier iteration on shared components).

## Concrete Artifacts

### Complete Trigger Field Reference (abridged from schema)

```yaml
on:
  # Slash command — invoked via /command in comments
  slash_command:
    name: string | array      # command name(s) without /; default: filename
    events: string | array    # where active; default: '*' (all comment events)

  # Label command — fires when label added to issue/PR/discussion
  label_command:
    name: string | array      # label name(s) that trigger the workflow
    events: string | array    # item types: issues, pull_request, discussion
    remove_label: boolean     # auto-remove triggering label; default: true

  # Standard GitHub events (each with sub-filters)
  push:
    branches: array           # branches to include
    paths: array              # paths to include

  pull_request:
    types: array              # event types (opened, synchronize, closed, etc.)
    draft: boolean            # filter by draft state
    forks: string | array     # allow fork patterns: '*', 'org/*', 'org/repo'

  issues:
    types: array
    lock-for-agent: boolean   # lock issue for agent; prevents concurrent mods

  issue_comment:
    types: array
    lock-for-agent: boolean   # lock parent issue

  schedule: string | array    # 'daily', 'weekly', 'hourly', cron; min 5 min

  workflow_dispatch:          # manual trigger with optional inputs
    inputs: object

  workflow_run:               # triggered when another workflow completes
    workflows: array
    types: array

  # Conditional skip gate system (all run before AI engine):
  skip-if-match:
    query: string             # GitHub search query; skip if matches found
    max: integer | string     # default 1
    scope: string             # 'none' for org-wide queries

  skip-if-no-match:
    query: string             # skip if no matches
    min: integer              # default 1

  skip-if-check-failing:
    include: array            # check names to evaluate
    exclude: array
    branch: string            # defaults to PR base or current ref
    allow-pending: boolean    # pending checks not treated as failing

  skip-roles: string | array  # skip for users with these roles
  skip-bots: string | array   # skip for these bot usernames
  roles: string | array       # required roles; default: admin, maintainer, write
  bots: array                 # bot allow-list despite role requirements

  # Human approval gate (entire workflow)
  manual-approval: string     # GitHub environment name requiring approval
```
*Source: github.github.com/gh-aw/reference/frontmatter-full — schema-generated field catalog*

### Engine Configuration — Three Tiers

```yaml
# Tier 1: Named engine shorthand
engine: claude

# Tier 2: Named engine with model and turn limit override
engine:
  id: claude
  model: claude-3-5-sonnet-20241022
  max-turns: 10          # prevents runaway loops
  bare: false            # set true to disable auto-loading context/custom instructions

# Tier 3: Custom provider with OAuth 2.0 (for GHEC, GHES, private deployments)
engine:
  runtime:
    id: claude           # adapter: codex | claude | copilot | gemini | crush
  provider:
    id: anthropic        # openai | anthropic | github | google
    model: claude-3-5-sonnet-20241022
    auth:
      strategy: oauth-client-credentials   # or: api-key
      token-url: ${{ secrets.TOKEN_URL }}
      client-id: OAUTH_CLIENT_ID           # secret name
      client-secret: OAUTH_CLIENT_SECRET
    request:
      path-template: /v1/messages/{model}  # for non-standard endpoints
  api-target: https://my-ghes.example.com  # GHEC, GHES, or custom
```
*Source: github.github.com/gh-aw/reference/frontmatter-full — schema-generated field catalog*

### Execution Lifecycle Hooks

```yaml
# Pre-steps: before checkout (token minting, environment setup)
pre-steps:
  - uses: my-org/setup-secrets@v1
    with:
      secret-name: MY_API_KEY

# Steps: injected after built-in pre-activation checks
steps:
  - name: custom-validation
    run: echo "custom gate check"

# Pre-agent-steps: after init, before AI execution (context prep, data fetch)
pre-agent-steps:
  - name: fetch-project-context
    run: gh api /repos/${{ github.repository }}/projects > /tmp/projects.json

# Post-steps: after AI execution (cleanup, notification, result processing)
post-steps:
  - name: notify-team
    run: gh issue comment ${{ github.event.issue.number }} --body "Agent run complete"
```
*Source: github.github.com/gh-aw/reference/frontmatter-full — schema-generated field catalog*

### Workflow Identity and Metadata Fields

```yaml
name: My Workflow Name           # appears in GitHub Actions interface
description: Optional description rendered as comment in generated YAML
source: owner/repo/path@ref      # where workflow was added from (provenance)
redirect: new/path/workflow.md   # for add/update redirects
tracker-id: my-workflow-v1       # 8+ chars; tags all created assets
labels: [maintenance, scheduled]
metadata:
  team: platform                 # custom key-value (64-char keys, 1024-char values)
  version: "1.2"

inlined-imports: false           # true: embed all imports in lock.yml at compile time
```
*Source: github.github.com/gh-aw/reference/frontmatter-full — schema-generated field catalog*

### Experiments / A/B Testing Configuration

```yaml
experiments:
  storage: repo          # 'cache' (ephemeral) or 'repo' (persists to git branch)
  # variant and metadata configuration not fully rendered in source
```
*Source: github.github.com/gh-aw/reference/frontmatter-full — schema-generated field catalog*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 1 (YAML frontmatter + markdown
    two-component structure): this page is the exhaustive catalog of what
    goes in the YAML frontmatter half. That note describes the *concept*;
    this note provides the *complete field inventory*.
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default —
    permissions): the `permissions:` field catalog here (19 named scopes,
    all default to read) is consistent with that claim.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require
    human approval): this note's Claim 4 (`on.manual-approval`) extends
    the human approval point upstream — not just for critical actions, but
    for the entire workflow run.
  - `docs-ghaw-concurrency-reference.md` (concurrency groups): the
    `concurrency` and `engine.concurrency` fields here align with that
    reference's documented group format expressions.
  - `docs-ghaw-permissions-reference.md` (permissions model): the
    `permissions` field catalog here lists the same 19 scopes covered in
    depth there, including the anomalous `id-token` and `models` scopes.
  - `docs-ghaw-sandbox-reference.md` (sandbox configuration): the
    `sandbox` field here (AWF type, mounts, memory, filesystem config,
    MCP gateway) matches that reference's deeper coverage.
  - `docs-ghaw-network-reference.md` (network controls): the `network`
    field here (allowed/blocked domains and ecosystems) matches that
    reference's network egress model.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 11 (development workflow: compile →
    watch → run → review): this page adds the `engine.max-turns` and
    `on.manual-approval` fields as configurable safety gates that belong
    in the workflow-design checklist alongside the compile step.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support): Claim 5
    in this note extends the four named engines to include fully custom
    provider definitions via `engine.runtime` + `engine.provider`, making
    the engine model extensible beyond the four documented engines.
  - `docs-ghaw-compilation-process.md` (compilation model): `inlined-imports`
    here (Claim 13) extends the `.md` → `.lock.yml` model with a compile-time
    option to fully materialize imports, adding a snapshot-vs-live-reference
    design choice to the compilation step.

- **Contradicts**: None. All claims in this source are consistent with
  existing source notes. This source is broader in scope (complete field
  catalog) but does not oppose any claim in the existing corpus.

- **Novel**:
  - **Conditional skip gate system** (Claim 3): The full six-field skip
    system (`skip-if-match`, `skip-if-no-match`, `skip-if-check-failing`,
    `skip-roles`, `skip-bots`, `roles`) as a pre-execution gate layer is
    not documented in any other source note. Individual skip patterns appear
    in workflow examples but the taxonomy as a whole is new.
  - **workflow-entry human approval** (Claim 4): `on.manual-approval` as
    a pre-workflow-start gate (vs. per-action approval) is not documented
    elsewhere in the corpus.
  - **Custom provider/OAuth engine** (Claim 5): The fully inline engine
    definition with OAuth 2.0 (`engine.runtime` + `engine.provider` +
    `engine.provider.auth`) is not documented elsewhere.
  - **engine.bare mode** (Claim 7): Auto-context-injection and its opt-out
    mechanism are not documented in any other source note.
  - **A/B experiments** (Claim 8): The `experiments` field with storage
    persistence options is not documented anywhere else in the corpus.
  - **tracker-id asset tagging** (Claim 9): The `tracker-id` field as a
    lifecycle management mechanism for agent-created GitHub objects is not
    described elsewhere.
  - **Execution lifecycle hooks** (Claim 12): The four-point injection
    model (pre-steps, steps, pre-agent-steps, post-steps) is not described
    as a unified pattern in any other source note.
  - **inlined-imports** (Claim 13): The compile-time import materialization
    option is not mentioned in any other source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add: Trigger taxonomy as the first harness design decision** (Claim 2):
  The guide should present the five trigger categories as a taxonomy that
  shapes the rest of the workflow design. The question "who or what activates
  this agent?" determines the trigger class; that choice constrains available
  sub-fields and determines the interaction model.

- **Add: Conditional skip gates as cost-control patterns** (Claim 3):
  Document the six skip options as declarative precondition checks that
  short-circuit before AI invocation. Specifically, `skip-if-match` (for
  idempotency — don't re-run if work is already done), `skip-if-check-failing`
  (for correctness — don't run on a broken branch), and `on.roles` (for
  access control — don't run for unauthorized users) are the three most
  commonly needed. Keeping these in frontmatter rather than in prompt
  instructions is a correctness property.

- **Add: engine configuration tier model** (Claim 5): Document the
  three-tier engine configuration (shorthand → model override → custom
  provider/OAuth) as a progressive complexity ladder. Most workflows need
  Tier 1 or 2. Tier 3 is for enterprise custom deployments only.

- **Add: max-turns as default discipline** (Claim 6): Recommend setting
  `engine.max-turns` as a default practice for all agentic workflows.
  Pair with `gh aw logs` for monitoring (from `docs-ghaw-how-they-work.md`
  Claim 11). These two mechanisms — one structural, one observational —
  form the complete anti-runaway strategy.

- **Add: execution lifecycle hooks** (Claim 12): Add the four-point
  lifecycle model (pre-steps, pre-agent-steps, post-steps, steps) as the
  composability mechanism for custom harness logic. These are where secrets
  setup, context enrichment, and result processing live.

- **Add: tracker-id for agent-created artifact management** (Claim 9):
  Recommend setting `tracker-id` for any workflow that creates GitHub
  objects at scale. It enables lifecycle queries and cleanup operations
  after agent runs.

- **Add: inlined-imports for production workflows** (Claim 13): Recommend
  `inlined-imports: true` for production workflows (reproducibility) and
  live references for development workflows (easier iteration).

### Chapter 03: Safety and Verification

- **Add: workflow-entry human approval gate** (Claim 4): The
  `on.manual-approval` field is the upstream HITL point before any AI
  execution. Pair with Safe Outputs per-action approval (from
  `docs-ghaw-how-they-work.md` Claim 10) to give practitioners a
  two-level HITL model — one at the workflow level and one at the action
  level.

- **Add: lock-for-agent as issue-level mutex** (Claim 11): Document
  `on.lock-for-agent` as a correctness mechanism for issue-processing
  workflows. Concurrent modification of the same issue by two agents is
  a class of race condition that `lock-for-agent` prevents. Recommend
  it as default for issue-triggered workflows that read then write.

### Chapter 04: Context Engineering

- **Add: engine.bare for full context control** (Claim 7): The
  `engine.bare` flag is the frontmatter-level override for teams that
  need full control over the AI context window. Document when to use it
  (specialized audit workflows, security-sensitive analysis) and the
  tradeoff (lose auto-injected context, gain full control).

## Extraction Notes

1. **Source is schema-generated and comprehensive**: The page is documented
   as "automatically generated from JSON Schema." This is the broadest single
   reference in the gh-aw documentation and the definitive field inventory.
   The full field count is approximately 200+ named sub-fields across all
   sections.

2. **Page truncation**: The WebFetch tool returned truncated content for the
   full page (the page is very long due to the exhaustive field catalog).
   Safe-outputs frontmatter fields (the `safe-outputs:` top-level section)
   and some tools sub-fields were not returned in the fetch responses.
   The safe-outputs configuration is covered in depth in
   `docs-ghaw-safe-outputs-specification.md`. The tools section is covered
   in `docs-ghaw-tools-reference.md`. Claims in this note are based on
   the fields that were returned.

3. **No direct publication date**: Like other gh-aw reference pages, this
   page carries no explicit publication date. Content is consistent with
   gh-aw v0.62.x+ based on the engine provider/runtime structure
   (which appeared in the same era as MCP gateway support).

4. **Deliberate scope**: This note focuses on fields NOT already deeply
   covered in dedicated reference page notes. Fields like `permissions`,
   `sandbox`, `network`, `tools`, and `concurrency` appear here in the
   field catalog but their behavior is documented in the respective dedicated
   notes. The novel claims in this note are about fields with no other
   coverage in the corpus.

5. **No contradictions filed**: All fields documented here are consistent
   with existing source notes. The five-layer security model, Safe Outputs
   permission separation, and compilation model from `docs-ghaw-how-they-work.md`
   are corroborated by this source, not contradicted.
