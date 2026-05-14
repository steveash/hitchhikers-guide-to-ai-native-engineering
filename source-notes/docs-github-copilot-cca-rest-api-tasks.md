---
source_url: https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api
source_type: docs
title: "Start Copilot cloud agent tasks via the REST API"
author: GitHub (official changelog)
date_published: 2026-05-13
date_extracted: 2026-05-14
last_checked: 2026-05-14
status: current
confidence_overall: settled
issue: "#734"
---

# Start Copilot Cloud Agent Tasks via the REST API

> GitHub's May 2026 announcement of the Agent tasks REST API (public preview) adds
> a direct programmatic invocation path for Copilot cloud agent tasks — distinct from
> the existing UI/issue-assignment and GitHub Actions workflow triggers — enabling
> batch scripting, portal integration, and time-based automation without requiring
> GitHub Actions infrastructure, while exposing the same GitHub App token exclusion
> already present in the Safe Outputs-based `assign-to-agent` mechanism.

## Source Context

- **Type**: docs (GitHub official product changelog, May 13, 2026, ~150 words)
- **Author credibility**: GitHub engineering team announcing a production feature in
  public preview. Authoritative for the existence of the API, the stated use cases,
  authentication support, and access-tier eligibility. Not a credible source for API
  performance characteristics, rate limits, task success rates, or comparative
  effectiveness of programmatic vs. UI-triggered invocation. The source is
  deliberately brief; it links to the API reference documentation at
  `https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task`
  for the full technical schema.
- **Scope**: The existence and basic capabilities of the Agent tasks REST API, three
  illustrative use cases (fan-out scripting, portal integration, automated release
  prep), progress-tracking availability, authentication support, and subscription-tier
  eligibility. Does NOT cover: specific API endpoint paths or request/response schemas
  (those are in the linked documentation), model selection parameters, rate limits,
  billing implications, task cancellation, error handling, webhook or callback
  patterns (only polling is implied), or how the REST API interacts with CCA's
  existing GitHub Actions-based execution environment.

## Extracted Claims

### Claim 1: GitHub's Agent tasks REST API enables Copilot Business and Enterprise users to programmatically start CCA tasks, in public preview as of May 2026

- **Evidence**: Official GitHub product changelog announcing the feature. The "public
  preview" qualifier signals the API surface may change before GA; the Copilot
  Business/Enterprise restriction is explicit.
- **Confidence**: settled (product fact — the API exists and is documented)
- **Quote**: "Copilot Business and Copilot Enterprise users can programmatically start
  Copilot cloud agent tasks with the new Agent tasks REST API, available in public
  preview."
- **Our assessment**: This is the primary announcement — a third invocation path for
  CCA tasks, joining (a) UI-based assignment (issue assignment, Agents tab, @copilot
  in a PR comment) and (b) GitHub Actions workflow Safe Outputs (`assign-to-agent`).
  Unlike those paths, the REST API requires no GitHub Actions infrastructure and can
  be called from any HTTP client. For Ch02 (Harness Engineering): document this as
  the third member of the CCA invocation taxonomy. The "public preview" caveat means
  practitioners integrating the REST API into production tooling should pin to
  `apiVersion=2026-03-10` and monitor for deprecation or breaking changes before GA.
  Cross-reference: `docs-github-copilot-cca-startup-custom-images.md` Claim 4
  enumerates the prior two invocation paths (issue assign, Agents tab, @copilot in PR);
  the REST API is a fourth path not listed there (the changelog was published April 27,
  before this May 13 announcement).

### Claim 2: CCA executes in an isolated cloud development environment, making and validating code changes before opening a pull request

- **Evidence**: Official description in the changelog. This is the operational model
  for all CCA tasks, restated in the context of the REST API announcement.
- **Confidence**: settled (product fact, consistent with prior CCA documentation)
- **Quote**: "Copilot cloud agent works in the background in its own development
  environment, where it can make and validate code changes, then open a pull request."
- **Our assessment**: This sentence describes the CCA execution model as it applies
  to REST-API-triggered tasks. The key operational implication: REST-API-initiated
  tasks are not synchronous — the API call starts the task, and the agent then does
  its work asynchronously in the background. The "validate code changes" step is
  consistent with `docs-github-copilot-cca-validation-parallel.md`, which documents
  that CCA's validation tools run 20% faster via parallelization. The "then open a
  pull request" output is the standard CCA artifact — the REST API adds a new trigger
  path but does not change the output format. For Ch02: practitioners calling the
  REST API must design for asynchronous completion — fire-and-poll, not
  request-response.

### Claim 3: The REST API enables batch fan-out scripting — running refactors or migrations across many repositories from a single script

- **Evidence**: Explicit use case listed in the changelog. This is the most
  architecturally novel use case relative to existing invocation paths.
- **Confidence**: emerging (the use case is articulated by the vendor; no empirical
  evidence of how well batch-scripted CCA tasks perform at scale, what rate limits
  apply, or whether the quality degrades at higher task volumes)
- **Quote**: "Fan out refactors or migrations across many repositories from a simple
  script."
- **Our assessment**: This is the distinguishing capability relative to prior invocation
  paths. UI-based assignment requires a human for each repo; workflow-based assignment
  via `assign-to-agent` requires a GitHub Actions trigger for each repo. A script can
  iterate over a repository list, POST to the Agent tasks API for each, and track
  progress asynchronously — enabling org-wide or cross-org refactors without manual
  UI interaction per repository. The changelog provides no information on rate limits
  or concurrency constraints; practitioners implementing batch scripts should consult
  the API documentation and test with small batches before scaling. For Ch02: add
  "fan-out refactor via REST API" as a concrete harness pattern for large-scale
  codebase migrations.

### Claim 4: The REST API enables one-click integration with internal developer portals for automated repository setup

- **Evidence**: Explicit use case listed in the changelog. Positions the REST API
  as an integration point for DevEx tooling.
- **Confidence**: emerging (the use case is articulated; no implementation examples
  or integration patterns are provided in the changelog)
- **Quote**: "Set up new repositories in one click from your company's internal
  developer portal."
- **Our assessment**: This use case targets enterprise platform engineering teams
  (those building or operating internal developer portals, e.g., Backstage-based
  portals or custom self-service tooling). The REST API becomes the bridge between a
  self-service portal action ("create new repo") and a CCA task ("configure the repo
  with standard scaffolding"). Previously, this integration would require either a
  GitHub Actions workflow tied to repo creation events or manual UI interaction.
  For Ch05 (Team Adoption — Enterprise): this positions CCA as a building block for
  internal platform-as-a-service automation, not just a developer-facing AI coding
  tool. Teams building internal platforms should evaluate whether the Agent tasks API
  can replace or augment existing repo-bootstrapping workflows.

### Claim 5: The REST API enables time-based automated workflows — e.g., weekly release preparation including release notes generation

- **Evidence**: Explicit use case listed in the changelog. Extends CCA triggering
  beyond event-driven (issue assignment, PR mention) and workflow-driven (Actions)
  patterns to any scheduler that can make HTTP requests.
- **Confidence**: emerging (use case articulated; no data on task success rates for
  release-prep workflows or on release-notes quality from CCA)
- **Quote**: "Automatically prepare a new release each week, including release notes."
- **Our assessment**: The "automatically prepare a release each week" use case implies
  cron-triggered calls to the REST API — any system that can schedule an HTTP request
  (cron jobs, cloud schedulers, monitoring systems, CI/CD platforms other than GitHub
  Actions) can now initiate CCA tasks. This is a meaningful architectural expansion:
  CCA is no longer exclusively event-driven or workflow-driven. However, release
  preparation is among the most context-sensitive tasks a developer performs — the
  changelog provides no evidence that CCA achieves acceptable quality on release-prep
  tasks without human oversight. For Ch02: note that time-based CCA invocation is now
  technically possible; whether it is appropriate for release-critical workflows
  requires separate evaluation. The `blog-gh-aw-operations-release-workflows.md`
  (covering GitHub's Changeset Generator at 78% merge rate) is the closest existing
  corpus evidence on automated release workflows — those findings predate this API
  and use a different invocation mechanism.

### Claim 6: Task progress can be tracked through the REST API after initiation — the API is not fire-and-forget

- **Evidence**: Explicit feature description in the changelog. The availability of
  progress tracking implies at minimum a GET endpoint for task status.
- **Confidence**: settled (feature described directly in official changelog)
- **Quote**: "Once you've started a task, you can also track progress through the API."
- **Our assessment**: Progress tracking turns the REST API into a complete task
  lifecycle management interface, not just a trigger. This is operationally important
  for integration scenarios where the calling system needs to know when a CCA task
  completes (e.g., to gate a subsequent pipeline step, to report status back to a
  portal user, to trigger a notification). The "also" in the quote suggests the
  tracking capability was added alongside the task-start capability, not a pre-existing
  feature being extended. The changelog does not document the polling interval, task
  state machine (queued/in-progress/complete/failed), or timeout semantics — those
  are in the linked API documentation. For Ch02: practitioners building integrations
  must account for the asynchronous completion pattern; the API reference at
  `https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task`
  should be consulted for the full status schema.

### Claim 7: Authentication supports personal access tokens (classic and fine-grained) and OAuth tokens; GitHub App installation access tokens are not yet supported

- **Evidence**: Explicit authentication statement in the changelog, with a "coming soon"
  qualifier for App token support.
- **Confidence**: settled (current support list and coming-soon qualifier stated
  explicitly in official changelog)
- **Quote (supported)**: "The Agent tasks API supports authentication with personal
  access tokens (classic and fine-grained) and OAuth tokens."
- **Quote (coming soon)**: "Support for GitHub App installation access tokens, plus
  access for Copilot Pro and Pro+ users, is coming soon."
- **Our assessment**: The GitHub App installation access token exclusion is
  operationally significant for enterprise teams. Organizations that standardize on
  GitHub App tokens for CI/CD automation (a common enterprise pattern) will find
  they cannot use the Agent tasks REST API until App token support ships. Teams in
  this situation face a choice: (a) provision PATs specifically for CCA REST API
  calls — adding PAT lifecycle management overhead — or (b) wait for App token
  support. The PAT-only limitation mirrors the `assign-to-agent` safe output
  constraint documented in `docs-ghaw-assign-to-copilot.md` Claim 7, suggesting a
  platform-wide authentication constraint for programmatic CCA invocation rather
  than an API-specific gap. For Ch02: document the PAT requirement as a deployment
  prerequisite for any integration built on the Agent tasks API. The `GH_AW_AGENT_TOKEN`
  convention described for `assign-to-agent` (Claim 8 of that note) may provide a
  centralized PAT management pattern adaptable to this context.

### Claim 8: Access is currently limited to Copilot Business and Enterprise subscribers; Copilot Pro and Pro+ access is forthcoming

- **Evidence**: Stated in both the opening sentence (Business/Enterprise only) and the
  "coming soon" qualifier in the authentication paragraph.
- **Confidence**: settled (current access restriction and forthcoming expansion both
  explicitly stated)
- **Quote**: "Support for GitHub App installation access tokens, plus access for
  Copilot Pro and Pro+ users, is coming soon."
- **Our assessment**: The current Business/Enterprise restriction is consistent with
  the general CCA access tier pattern throughout the corpus
  (`docs-github-copilot-agent-model-selection.md` Claim 5: Copilot Business or
  Enterprise required for cloud agent features; `docs-github-copilot-cca-custom-properties.md`
  Claim 1: enterprise admin controls over CCA access). The forthcoming Pro/Pro+
  expansion signals GitHub's intent to make programmatic CCA access available to
  individual developers and smaller teams, not just enterprise customers. For Ch05:
  teams advising individual developers on CCA adoption should note the current
  Business/Enterprise restriction and the timeline uncertainty for Pro/Pro+ access.

## Concrete Artifacts

### Agent Tasks REST API — Key Facts (from changelog, May 13, 2026)

```
Title: Start Copilot cloud agent tasks via the REST API
Published: 2026-05-13 (public preview)

API Documentation:
  https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task
  API version: 2026-03-10

Access eligibility (as of May 2026):
  ✅  Copilot Business subscribers
  ✅  Copilot Enterprise subscribers
  🔜  Copilot Pro users (coming soon)
  🔜  Copilot Pro+ users (coming soon)

Authentication (as of May 2026):
  ✅  Personal access tokens — classic
  ✅  Personal access tokens — fine-grained
  ✅  OAuth tokens
  🔜  GitHub App installation access tokens (coming soon)

Capabilities:
  - Start a CCA task programmatically (fire-and-poll pattern)
  - Track task progress through the API after initiation

Stated use cases:
  1. Fan out refactors or migrations across many repos from a script
  2. One-click repo setup from internal developer portals
  3. Automated weekly release preparation including release notes

Execution model:
  - CCA runs in its own development environment (isolated, cloud-based)
  - Agent makes and validates code changes, then opens a pull request
  - Asynchronous — task runs in background after API call initiates it
```

### CCA Invocation Path Taxonomy (synthesized from corpus, current as of 2026-05-14)

```
CCA Task Invocation Paths (as of May 2026):

Path 1 — UI / Manual (event-bound)
  Trigger:     Assign issue to Copilot, start from Agents tab,
               or @copilot mention in a pull request
  Requires:    GitHub.com UI access
  Auth:        GitHub session (no additional token needed)
  Source:      docs-github-copilot-cca-startup-custom-images.md Claim 4

Path 2 — GitHub Actions workflow (event-driven automation)
  Trigger:     Workflow event (issue creation, label, schedule, dispatch, etc.)
  Mechanism:   assign-to-agent Safe Output via the gh-aw platform
  Requires:    GitHub Actions, fine-grained PAT (or GH_AW_AGENT_TOKEN)
               GitHub App tokens NOT supported
  Source:      docs-ghaw-assign-to-copilot.md

Path 3 — REST API (direct programmatic)
  Trigger:     Any HTTP client (script, cron, portal, CI system)
  Mechanism:   Agent tasks REST API (apiVersion=2026-03-10)
  Requires:    PAT (classic/fine-grained) or OAuth token
               GitHub App installation tokens NOT yet supported
               Copilot Business or Enterprise subscription
  Source:      THIS NOTE (docs-github-copilot-cca-rest-api-tasks.md)

Common output across all paths:
  Agent works in isolated cloud environment → opens a pull request
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-assign-to-copilot.md` Claim 7 (GitHub App installation access tokens
    not supported for programmatic CCA assignment): Both sources document the same
    GitHub App token exclusion for programmatic CCA invocation. The parallel
    restriction across the Safe Outputs-based `assign-to-agent` and the new direct
    REST API suggests this is a platform-wide authentication constraint for
    CCA operations, not an API-specific oversight. Teams that standardize on App
    tokens will find the exclusion in both available programmatic invocation paths.

- **Extends**:
  - `docs-github-copilot-cca-startup-custom-images.md` Claim 4 (three CCA invocation
    paths enumerated — issue assignment, Agents tab, @copilot in PR): The REST API is
    a fourth invocation path not present in that April 27, 2026 changelog. The
    taxonomy artifact above integrates both sources into a complete four-path
    invocation model. Note that the startup performance improvements documented in
    that note (custom Actions images) apply to all invocation paths, including
    REST-API-triggered tasks.
  - `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 8 (aggregate
    CCA active user counts via the metrics API): The REST API expands the potential
    task volume beyond what UI and workflow triggers alone can generate — batch
    scripting across hundreds of repos could produce task counts that significantly
    exceed typical human-driven usage. The aggregate metrics API documented in that
    note gains added relevance as a monitoring tool for programmatically-triggered
    task volumes. Teams using the REST API for batch operations should track CCA
    usage metrics to detect unexpected task saturation.
  - `docs-github-copilot-cca-custom-properties.md` Claim 7 (pilot-first progressive
    rollout as the prescribed CCA adoption pattern): The REST API creates a new
    rollout consideration — batch-scripted task invocations can reach many
    repositories simultaneously, making the pilot-first pattern more important,
    not less. A script that fans out to 200 repos is qualitatively different from
    manual issue assignment in terms of rollout risk. The governance API from that
    note (selectively enabling CCA per org) is the prerequisite for safely deploying
    REST-API-driven automation.
  - `docs-github-copilot-agent-model-selection.md` Claim 1 (model selection now
    exposed for cloud agent tasks): The Agent tasks API documentation referenced in
    this changelog (`apiVersion=2026-03-10`) may expose model selection as a
    parameter — the changelog does not mention it, but the linked REST API reference
    would be the definitive source. Teams that require specific model tiers for
    programmatic tasks (e.g., Opus for complex multi-repo refactors, Sonnet for
    routine scaffolding) should consult the API documentation to determine whether
    model selection is a supported parameter in the REST API.

- **Contradicts**: None identified. The authentication constraints (PAT required,
  GitHub App excluded) are consistent with `docs-ghaw-assign-to-copilot.md` Claim 7,
  not a contradiction. The subscription tier restriction (Business/Enterprise) is
  consistent across all CCA-related source notes. No contradiction issue filed.

- **Novel**:
  - **Direct REST API as a third CCA invocation path**: No prior corpus source
    documents programmatic API access to start CCA tasks from arbitrary HTTP clients
    (outside of GitHub Actions workflows). The two prior paths (UI and Safe Outputs
    via `assign-to-agent`) both require GitHub infrastructure; the REST API does not.
  - **Batch fan-out scripting as a CCA use case**: The "fan out refactors or
    migrations across many repositories from a simple script" pattern is new to the
    corpus. Prior notes cover CCA invocation one task at a time (one issue, one
    workflow trigger). Batch scripting changes the scale assumptions for CCA-driven
    workflows.
  - **Internal developer portal integration as a CCA invocation pattern**: No prior
    corpus source discusses integrating CCA with internal developer portals (Backstage,
    custom self-service platforms). The REST API makes this integration technically
    feasible for the first time.
  - **Time-based CCA invocation (cron-triggered without GitHub Actions)**: Prior
    sources cover event-driven (issue/PR events) and workflow-driven (Actions
    schedule trigger) CCA invocation. The REST API enables pure HTTP-based
    time-based invocation from any scheduler, without requiring GitHub Actions
    infrastructure.

## Guide Impact

- **Chapter 02 (Harness Engineering — CCA Integration Patterns)**:
  - Add a "CCA Invocation Taxonomy" section documenting all three invocation paths
    (UI, Safe Outputs/`assign-to-agent`, REST API). For each path, specify: trigger
    mechanism, infrastructure requirements, authentication requirements, and best-fit
    use cases. The REST API is the right choice when: (a) invoking from outside GitHub
    Actions, (b) batch-dispatching across many repos, (c) integrating with a portal or
    non-GitHub CI system. The Safe Outputs path is the right choice when: operating
    within a GitHub Actions workflow and needing the privilege-separation guarantees of
    the gh-aw Safe Outputs model. The UI path remains the right choice for ad-hoc,
    human-initiated tasks.
  - Add a "PAT management for programmatic CCA" note: both the REST API and the
    `assign-to-agent` safe output require fine-grained PATs (not GitHub App tokens).
    Teams building CCA automation should provision and rotate these PATs as a
    dedicated operational concern, separate from general Actions workflow tokens.
  - Add "fan-out scripting" as a concrete harness pattern for large-scale migrations:
    POST to the Agent tasks API per repository, poll for completion, aggregate results.
    Note that rate limits apply (consult API docs) and that the pilot-first rollout
    pattern from `docs-github-copilot-cca-custom-properties.md` applies — test the
    script on a small cohort before scaling.

- **Chapter 05 (Team Adoption — Enterprise Considerations)**:
  - Add the Agent tasks REST API as a building block for internal platform integration.
    Teams operating internal developer portals (Backstage or custom) can now trigger
    CCA tasks programmatically from portal actions (repo creation, onboarding flows,
    etc.). Document the authentication prerequisites (PAT, Copilot Business/Enterprise
    subscription) as deployment dependencies.
  - Note the Pro/Pro+ expansion as forthcoming — individual developer access to the
    REST API is coming but not yet available. Teams advising individuals on CCA
    adoption should set this expectation.

- **Chapter 07 (Enterprise Operations)**:
  - Add a note connecting the `docs-github-copilot-cca-custom-properties.md`
    governance API (which orgs have CCA enabled) with the REST API: enabling CCA
    for an org via the governance API is the prerequisite for REST-API-triggered
    tasks from that org's repositories. An automation script that fans out across
    org repositories should first verify CCA is enabled for the target org before
    dispatching tasks.

## Extraction Notes

1. **Very brief source (~150 words)**: The changelog is among the shorter entries in
   the corpus. All substantive claims are exhausted in 8 items. The primary technical
   substance (endpoint paths, request schemas, response formats, rate limits) lives in
   the linked API documentation at
   `https://docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task`,
   which was not separately fetched. A source note for that documentation page would
   be a high-value extraction — it would provide the complete technical schema needed
   for practitioners building integrations.

2. **Verbatim quote accuracy**: Two independent WebFetch calls were made to the source
   URL, returning consistent content. All quotes in this note are presented as verbatim
   extractions from those fetches. The Assayer should spot-check the core quotes
   (particularly Claim 1, 7, and the use-case bullets in Claims 3–5) against the live
   URL, as the WebFetch AI layer may introduce minor rendering artifacts. Any quote
   where the fetched content appeared inconsistent across the two calls is marked
   `(no direct quote; see paraphrase in Our assessment)` per MINER.md §2a.

3. **API documentation not fetched**: The linked REST API reference at
   `docs.github.com/rest/agent-tasks/agent-tasks?apiVersion=2026-03-10#start-a-task`
   was not fetched in this extraction. That page contains the endpoint path, HTTP
   method, request body schema, response codes, and parameter definitions (potentially
   including model selection) that this changelog intentionally omits. A separate
   source note for the API reference would be high-value for practitioners building
   integrations — it would fill in the concrete technical details that the changelog
   references but does not reproduce.

4. **No contradictions filed**: All claims are consistent with existing corpus notes.
   The PAT requirement (Claim 7) corroborates rather than contradicts
   `docs-ghaw-assign-to-copilot.md` Claim 7. The subscription tier requirement
   (Claim 8) is consistent across all CCA notes.

5. **Public preview status**: The API is in public preview as of May 13, 2026.
   Breaking changes before GA are possible. Any guide section citing specific
   parameter names or endpoint behavior derived from the API documentation should
   note the public preview status and recommend pinning to `apiVersion=2026-03-10`
   while monitoring the changelog for GA announcement.
