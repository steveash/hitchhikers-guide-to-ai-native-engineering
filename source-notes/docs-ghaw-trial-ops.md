---
source_url: https://github.github.com/gh-aw/patterns/trial-ops
source_type: docs
title: "GitHub Agentic Workflows: TrialOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#355"
---

# GitHub Agentic Workflows: TrialOps Pattern

> The canonical reference for pre-deployment workflow testing in gh-aw — documents
> the `gh aw trial` command, four repository modes (Default, Direct, Logical, Clone),
> dry-run previewing, result interpretation via a structured JSON schema, and
> multi-workflow comparison as a pre-production evaluation technique; fills the
> development-time testing slot that staged mode and the safe rollout ladder do not cover.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, in the `patterns/`
  section — the same section as `patterns/orchestration` covered by
  `docs-ghaw-orchestration-patterns.md` and `patterns/monitoring` covered by
  `docs-ghaw-monitoring-patterns.md`. Patterns pages are practitioner implementation
  references, distinct from conceptual `introduction/` pages and practitioner `guides/`
  section.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub Next /
  Microsoft Research — the same team behind Peli de Halleux's agent factory series). CLI
  behavior and repository mode descriptions are authoritative for the `gh aw` platform.
  The TrialOps pattern reflects operational practice from running 183+ production workflows.
  Claims do not automatically generalize to other agentic workflow platforms without
  qualification.
- **Scope**: Covers the TrialOps pattern: the `gh aw trial` CLI command, four repository
  modes, dry-run mode, single and multiple workflow testing, repeated trials, custom trial
  repositories, advanced options (issue context, append instructions, cleanup), result
  interpretation (JSON schema, success indicators, common troubleshooting), and multi-workflow
  comparison. Does NOT cover: the Safe Outputs permission model in general (see
  `docs-ghaw-how-they-work.md`), the rollout ladder for production promotion (see
  `docs-ghaw-safe-rollout.md`), staged mode syntax (see `docs-ghaw-staged-mode-reference.md`),
  or the SideRepoOps or MultiRepoOps patterns referenced in the "Related Documentation"
  section.

## Extracted Claims

### Claim 1: TrialOps is the gh-aw pattern for pre-deployment workflow testing — it validates and iterates on workflows in isolated temporary repositories before they are deployed to target repositories

- **Evidence**: The opening description frames TrialOps explicitly as a pre-deployment
  safety mechanism — "before deployment to target repositories" — distinguishing it from
  in-production validation tools like staged mode, which applies after a workflow is already
  deployed.
- **Confidence**: emerging (first-party practitioner documentation; the pattern is named
  and documented, but no adoption metrics or external validation are provided)
- **Quote**: "TrialOps uses temporary trial repositories for safely validating and iterating
  on workflows before deployment to target repositories."
- **Our assessment**: TrialOps fills a gap not covered by any existing corpus note. The
  safe rollout ladder (`docs-ghaw-safe-rollout.md` Claim 2) begins with "start in
  report-only mode" — it assumes the workflow is already deployed. Staged mode
  (`docs-ghaw-staged-mode-reference.md` Claim 1) is an operating mode of a deployed
  workflow. TrialOps is the testing primitive that precedes both: you validate the workflow
  in isolation before it ever enters the production deployment pipeline. The "iterating"
  framing is significant — TrialOps is not just for one-time validation but for the
  development loop itself: build, trial, adjust, repeat. For Ch02 (Harness Engineering):
  position TrialOps as the first phase of the workflow lifecycle — testing before
  deployment — before staged mode and the safe rollout ladder take over.

### Claim 2: The `gh aw trial` CLI creates a temporary private repository, installs the workflow via `workflow_dispatch`, and stores results in three locations: local JSON, trial repository, and console output

- **Evidence**: The "How Trial Mode Works" section describes the three-location result
  storage as a platform behavior, not a practitioner choice. The default trial repository
  name (`gh-aw-trial`) is explicitly stated.
- **Confidence**: settled (first-party documentation; the CLI behavior and default name
  are stated explicitly)
- **Quote**: "The CLI creates a temporary private repository (default: `gh-aw-trial`),
  installs and executes the workflow via `workflow_dispatch`."
- **Our assessment**: The three-location result storage is a practical design: local JSON
  files for programmatic comparison and analysis, the trial repository for inspecting
  actual GitHub artifacts (issues, PRs, comments) as they would appear in production,
  and console output for immediate human review. The `workflow_dispatch` installation
  mechanism mirrors how gh-aw workflows run in production — the trial execution path is
  identical to production execution, just in an isolated repository. This makes TrialOps
  a high-fidelity simulation: the workflow sees the same execution environment, the same
  trigger mechanism, and the same platform APIs — only the repository is temporary. For
  Ch02: TrialOps should be described as a production-fidelity testing primitive, not a
  mock or simulation.

### Claim 3: Four repository modes control the level of isolation and repository context available during a trial — Default, Direct, Logical, and Clone each answer a different testing question

- **Evidence**: The "Repository Modes" section lists four distinct modes, each with a
  different `--flag` syntax and a different trade-off between isolation and authenticity.
  The modes are mutually exclusive (one is selected per trial run).
- **Confidence**: settled (first-party documentation; modes and flags are enumerated
  explicitly)
- **Quote**: (no direct quote spanning all four modes; individual mode descriptions below)
- **Our assessment**: The four modes form a spectrum from most isolated to most authentic:
  Default (outputs go to trial repo, safest) → Logical (simulates against real repo context
  while keeping outputs in trial) → Clone (reads real repo contents for code analysis) →
  Direct (creates real artifacts in a specified repo, least isolated). Each mode answers a
  different question: Default: "does this workflow produce correct safe outputs?"; Logical:
  "does this workflow behave correctly when it thinks it's running against my real repo?";
  Clone: "does this workflow correctly analyze my actual codebase?"; Direct: "does this
  workflow create the right artifacts in a real repository?". The progression from Default
  to Direct mirrors the trust-building logic in `docs-ghaw-safe-rollout.md` — start with
  the most isolated mode and work toward higher-fidelity testing as confidence grows. For
  Ch02: present the four modes as a testing escalation ladder, with Default as the
  recommended starting mode.

### Claim 4: Default mode routes `github.repository` to the developer's repository while sending all outputs to the trial repository — the safest testing configuration

- **Evidence**: Default mode description is stated as: repository context points to the
  developer's actual repo (enabling the workflow to reason about that repo), but all
  written outputs land in the trial repository (not the production repo).
- **Confidence**: settled (first-party documentation; the mode behavior is stated explicitly)
- **Quote**: "github.repository points to your repo; outputs go to trial repo"
- **Our assessment**: Default mode is the recommended starting point for TrialOps because
  it combines real repository context (the workflow has accurate metadata about the actual
  repo) with complete output isolation (nothing is written to the production repo). This
  is appropriate for the common case: testing whether a workflow produces the right kind
  of safe outputs (correct labels, titles, bodies) without risking polluting the production
  repo with test artifacts. For Ch03 (Safety and Verification): Default mode is the
  zero-risk testing configuration — it validates workflow decision quality without
  production side effects.

### Claim 5: Clone mode enables workflows that analyze code to run against actual repository contents during the trial — the highest-fidelity testing mode for code-analysis workflows

- **Evidence**: Clone mode is described as cloning the repository's contents into the
  trial environment so that workflows which need to read and analyze actual code can do so
  during the trial.
- **Confidence**: settled (first-party documentation; the clone behavior is stated)
- **Quote**: "Clones repo contents so workflows can analyze actual code"
- **Our assessment**: Clone mode addresses the specific case where a workflow's behavior
  depends on the actual content of the repository — for example, a code review workflow
  that reads source files, or a dependency audit workflow that reads package manifests.
  Without Clone mode, such workflows would either fail or produce misleading results
  (analyzing an empty or default trial repository rather than the real codebase). Clone
  mode is the highest-fidelity TrialOps configuration for content-dependent workflows,
  at the cost of the most setup complexity. For Ch02: recommend Clone mode specifically
  for workflows that use the `gh aw` code-analysis toolsets.

### Claim 6: Dry-run mode previews trial behavior without executing the workflow or creating any repositories — the zero-cost validation step for checking configuration before a real trial

- **Evidence**: Dry-run mode is described as a preview mechanism that avoids any execution
  side effects: no trial repository is created, no workflow runs.
- **Confidence**: settled (first-party documentation; the dry-run option and its behavior
  are stated explicitly)
- **Quote**: "Preview what would happen without executing workflows or creating repositories"
- **Our assessment**: Dry-run mode fills the role of a pre-flight check: before committing
  to a full trial run (which creates a temporary repository and dispatches a workflow),
  practitioners can verify that the trial command is correctly configured. This is
  particularly useful when setting up a TrialOps run for the first time — checking that
  the workflow reference is correct, the flags are properly formed, and the intended mode
  is active. For Ch02: recommend dry-run as the mandatory first step in any TrialOps
  workflow. The cost of a dry-run is zero; the cost of a misconfigured full trial run
  (wasted run minutes, orphaned trial repositories) is real.

### Claim 7: Trial results are stored in a structured JSON schema with four top-level fields — workflow_name, run_id, safe_outputs, and agentic_run_info — enabling programmatic analysis and multi-run comparison

- **Evidence**: The "Understanding Trial Results" section describes the JSON schema
  used in `trials/*.json` files, with `safe_outputs` containing artifacts like
  `issues_created` and `agentic_run_info` containing performance metrics including
  `duration_seconds` and `token_usage`.
- **Confidence**: settled (first-party documentation; the JSON schema is enumerated)
- **Quote**: "Results are saved in `trials/*.json` with workflow runs, issues, PRs, and
  comments viewable in the trial repository's Actions and Issues tabs."
- **Our assessment**: The structured result schema is the foundation for TrialOps'
  multi-workflow comparison capability. Because every trial run produces a consistent
  JSON structure, practitioners can use standard tooling (e.g., `jq`) to compare runs
  across workflow versions, measure token usage trends, and track whether safe output
  quantities are within expected ranges. The inclusion of `token_usage` in `agentic_run_info`
  is notable: TrialOps produces cost telemetry for pre-deployment runs, enabling
  practitioners to estimate production costs before deploying a workflow. For Ch07
  (Cost Management): pre-deployment cost estimation via TrialOps `agentic_run_info`
  should be recommended as a standard practice before deploying any new workflow.

### Claim 8: Success indicators for a trial run are: a green checkmark, expected outputs present in the trial repository, and no errors in logs

- **Evidence**: The "Understanding Trial Results" section lists three explicit success
  indicators, stated as a summary of what "success looks like" for a trial run.
- **Confidence**: settled (first-party documentation; the indicators are enumerated)
- **Quote**: "Green checkmark, expected outputs created, no errors in logs."
- **Our assessment**: The three-indicator success definition maps to three distinct
  concerns: (1) the green checkmark confirms the workflow run itself completed without
  infrastructure failure; (2) expected outputs present confirms the workflow produced the
  intended safe outputs (issues, PRs, comments); (3) no errors in logs confirms the
  workflow's internal logic ran cleanly. A workflow can pass (1) while failing (2) —
  for example, if the workflow's conditional logic prevented any safe outputs from being
  created when they should have been. A workflow can pass (1) and (2) while failing (3) —
  if it produced outputs but logged recoverable errors that might become failures at scale.
  All three indicators must be positive for a trial to constitute a successful validation.
  For Ch03: frame these three indicators as the minimum passing bar for a TrialOps trial.

### Claim 9: The `--append` flag enables testing a workflow's response to additional constraints or instructions without modifying the source workflow file

- **Evidence**: The "Append Instructions" advanced pattern describes `--append` as a
  mechanism for injecting additional instructions into the workflow execution during the
  trial, separate from the workflow's base instructions.
- **Confidence**: settled (first-party documentation; the flag and its purpose are stated
  explicitly)
- **Quote**: "Test workflow responses to additional constraints without modifying the source"
- **Our assessment**: The `--append` flag is a testing affordance for prompt engineering
  iteration: practitioners can test how a workflow responds to additional instructions
  (e.g., "Focus on security issues" or "Only process issues labeled 'critical'") without
  editing the workflow file itself. This enables A/B testing of instruction additions
  against the same base workflow, which is particularly valuable when considering whether
  to add a constraint to a production workflow. The "without modifying the source"
  property preserves the base workflow's state during experimentation. For Ch02: recommend
  `--append` as the standard mechanism for testing instruction changes before committing
  them to the workflow file — use it to validate the addition is an improvement before
  modifying the source.

### Claim 10: Multiple workflows can be run side-by-side in a single trial command for quality, performance, and consistency comparison — with combined results stored in a `combined-results` JSON file

- **Evidence**: The "Multiple Workflows" basic usage example shows passing multiple
  workflow references in a single `gh aw trial` command. The "Comparing Multiple Workflows"
  section documents that results include both individual result files per workflow and
  a combined results file. The `--repeat` flag enables statistical reliability through
  repeated runs.
- **Confidence**: settled (first-party documentation; the multi-workflow syntax and
  combined results file are documented with examples)
- **Quote**: (no direct quote for the combined-results mechanism; see Concrete Artifacts
  for the CLI commands and `jq` query pattern)
- **Our assessment**: Multi-workflow comparison is TrialOps' most operationally
  significant capability for teams iterating on workflow quality. Rather than testing one
  version at a time and comparing mentally, practitioners can run multiple versions
  simultaneously against the same context and compare outputs programmatically via the
  combined results file. The `--repeat N` flag adds statistical reliability: comparing
  workflows across N runs each controls for non-determinism in AI outputs. For Ch04
  (Production Patterns): multi-workflow TrialOps comparison is the recommended approach
  for evaluating workflow variants before selecting one for production deployment — it
  applies the same "compare alternatives" discipline that staged mode applies to individual
  workflow runs.

### Claim 11: Common troubleshooting for trial failures covers four named scenarios — missing `workflow_dispatch` trigger, missing safe outputs configuration, permission errors, and timeouts — each with a specific remedy

- **Evidence**: The "Understanding Trial Results" troubleshooting section lists four
  scenario-specific remedies, indicating that these are the most common failure modes
  encountered in practice.
- **Confidence**: emerging (practitioner knowledge from running trials; the scenarios
  are named but no frequency data is provided)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The four scenarios reveal where TrialOps most commonly breaks
  down: (1) Workflow dispatch failures require adding the `workflow_dispatch` trigger —
  this is a configuration requirement for any workflow run via TrialOps, distinct from
  the triggers used in production. (2) Missing safe outputs indicate the workflow's
  configuration needs to declare which safe output types it will use. (3) Permission
  errors (verifying API keys) reflect that TrialOps runs with real GitHub credentials —
  a misconfigured secret will fail in trial just as it would in production. (4) Timeouts
  can be addressed using `--timeout <minutes>` — indicating TrialOps runs have a default
  timeout that may need adjustment for long-running workflows. For Ch02: include these
  four troubleshooting scenarios in any TrialOps guide as the first-stop diagnostic
  reference.

### Claim 12: The `--trigger-context` flag provides issue or event context to workflows designed to be triggered by specific GitHub events, enabling accurate testing of event-driven workflows

- **Evidence**: The "Issue Context" advanced pattern describes `--trigger-context` as
  taking a GitHub issue URL to provide the workflow with the same event context it would
  receive if triggered by that issue in production.
- **Confidence**: settled (first-party documentation; the flag syntax and purpose are
  stated)
- **Quote**: "Provide issue context for issue-triggered workflows"
- **Our assessment**: `--trigger-context` solves a specific test fidelity problem: a
  workflow triggered by issue events reads `github.event.issue.*` — but in a trial
  environment, no real issue triggered the run. By providing a real issue URL,
  practitioners can test how the workflow processes a specific issue's content, labels,
  and metadata. This is essential for testing triage workflows, issue classification
  agents, and any workflow whose behavior depends on the triggering issue's content.
  Without `--trigger-context`, such workflows would either fail or produce outputs that
  don't reflect real-world behavior. For Ch02: recommend `--trigger-context` as mandatory
  for testing any workflow with `on: issues` or `on: issue_comment` triggers.

## Concrete Artifacts

### Basic TrialOps CLI Usage

```bash
# Single workflow from GitHub
gh aw trial githubnext/agentics/weekly-research

# Single workflow from local file
gh aw trial ./my-workflow.md

# Dry-run (no execution, no repositories created)
gh aw trial ./my-workflow.md --dry-run

# Multiple workflows for side-by-side comparison
gh aw trial githubnext/agentics/daily-plan githubnext/agentics/weekly-research

# Repeated trials for statistical reliability
gh aw trial githubnext/agentics/my-workflow --repeat 3
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Basic Usage" section*

### Repository Modes

```bash
# Default mode: github.repository → your repo; outputs → trial repo
gh aw trial ./my-workflow.md

# Direct mode: creates real issues/PRs in the specified repo
gh aw trial ./my-workflow.md --repo myorg/test-repo

# Logical mode: simulates against specified repo; outputs in trial repo
gh aw trial ./my-workflow.md --logical-repo myorg/target-repo

# Clone mode: clones repo contents so workflows can analyze actual code
gh aw trial ./my-workflow.md --clone-repo myorg/real-repo
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Repository Modes" section*

### Advanced Options

```bash
# Issue context for event-triggered workflows
gh aw trial githubnext/agentics/triage-workflow \
  --trigger-context "https://github.com/myorg/repo/issues/123"

# Append additional constraints without modifying the source
gh aw trial githubnext/agentics/my-workflow \
  --append "Focus on security issues and create detailed reports."

# Cleanup options
gh aw trial ./my-workflow.md --delete-host-repo-after
gh aw trial ./my-workflow.md --force-delete-host-repo-before

# Custom trial repository
gh aw trial githubnext/agentics/my-workflow --host-repo my-custom-trial

# Use current repo as trial host
gh aw trial ./my-workflow.md --host-repo .

# Timeout configuration (in minutes)
gh aw trial ./my-workflow.md --timeout 60
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Advanced Patterns" section*

### Trial Results JSON Schema

```
trials/<workflow-name>.<DATETIME>-<ID>.json

{
  "workflow_name": "<workflow identifier>",
  "run_id":        "<execution identifier>",
  "safe_outputs": {
    "issues_created": [...]   // issues, PRs, comments created in trial repo
  },
  "agentic_run_info": {
    "duration_seconds": <float>,
    "token_usage":      <integer>
  }
}

Storage locations:
  1. Local:           trials/<workflow-name>.<DATETIME>-<ID>.json
  2. Trial repository: GitHub Actions run + Issues/PRs tabs
  3. Console:          Summary output at end of run

Multiple workflows: also produces trials/combined-results.<DATETIME>-<ID>.json
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Understanding Trial Results" section*

### Multi-Workflow Comparison and Analysis

```bash
# Run three workflow versions twice each for comparison
gh aw trial v1.md v2.md v3.md --repeat 2

# Analyze combined results with jq — count issues created per workflow
cat trials/combined-results.*.json | \
  jq '.results[] | {workflow: .workflow_name, issues: .safe_outputs.issues_created | length}'
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Comparing Multiple Workflows" section*

### Success Indicators and Troubleshooting Reference

```
Success indicators (all three required):
  ✓ Green checkmark (run completed without infrastructure failure)
  ✓ Expected outputs created in trial repository
  ✓ No errors in run logs

Common troubleshooting scenarios:
  Symptom: Workflow dispatch failures
  Remedy:  Add `workflow_dispatch` trigger to the workflow

  Symptom: Missing safe outputs in results
  Remedy:  Verify safe outputs are configured in workflow frontmatter

  Symptom: Permission errors
  Remedy:  Verify API keys and token scopes

  Symptom: Trial run times out
  Remedy:  Use --timeout <minutes> to extend the timeout
```

*Source: https://github.github.com/gh-aw/patterns/trial-ops — "Understanding Trial Results" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-safe-rollout.md` Claim 1 (safe rollout is a trust-promotion framework for
    increasing autonomy incrementally): TrialOps is the pre-deployment testing primitive
    that feeds the trust-promotion process documented in `docs-ghaw-safe-rollout.md`. The
    safe rollout ladder assumes the workflow is already deployed to a production or staging
    repository; TrialOps is the isolation test that validates behavior before that first
    deployment. Together they form a complete lifecycle: TrialOps → report-only → staged →
    shadow evaluation → production writes.
  - `docs-ghaw-staged-mode-reference.md` Claim 7 (5-step iterative adoption loop: enable
    staged, trigger, review, adjust, repeat, remove staged): TrialOps is a complementary
    pre-deployment iteration loop. The staged-mode loop operates on a deployed workflow;
    the TrialOps loop operates in isolated repositories. Both share the "adjust and repeat"
    iteration philosophy. A practitioner could use TrialOps to reach a stable workflow
    configuration, then enter the staged-mode loop once deployed.

- **Contradicts**: None identified. No existing source note documents the `gh aw trial`
  command, the TrialOps pattern, or the four repository modes. No claims in this source
  materially oppose existing notes. The relationship between TrialOps and staged mode is
  complementary — they operate at different lifecycle stages and answer different questions —
  not contradictory. No contradiction issue required.

- **Extends**:
  - `docs-ghaw-safe-rollout.md`: That source documents the safe rollout ladder starting
    from "report-only mode" in a deployed workflow. This source extends the pre-deployment
    phase that precedes the ladder: before a workflow reaches report-only mode in a
    production repository, practitioners can validate its behavior using TrialOps in
    isolated trial repositories. Read together, the complete workflow lifecycle is:
    develop → trial (TrialOps) → deploy to report-only → staged → shadow evaluation →
    production writes.
  - `docs-ghaw-staged-mode-reference.md` Claim 1 (staged mode runs the workflow completely
    while replacing every write operation with a step-summary preview): TrialOps and staged
    mode are two distinct isolation strategies. Staged mode replaces writes with previews
    while running in the target repository; TrialOps executes the workflow completely
    (real writes happen) but routes everything to a temporary trial repository. The two can
    compose: TrialOps first (does the workflow produce correct outputs in isolation?), then
    staged mode after deployment (does the proposed behavior look right in the real
    repository?).
  - `docs-ghaw-monitoring-patterns.md` Claim 1 (`update-project` safe output for audit
    trails): The TrialOps result JSON (`safe_outputs.issues_created`) provides equivalent
    audit trail data for pre-production trial runs. The monitoring patterns note covers
    production observability; TrialOps provides the equivalent observability surface for
    pre-deployment runs. Together they cover the full workflow lifecycle from testing
    through production monitoring.

- **Novel**:
  - **TrialOps as a named pre-deployment testing pattern** (Claim 1): No existing source
    note documents TrialOps, the `gh aw trial` command, or the concept of isolated
    temporary repositories as a pre-deployment testing primitive. This is entirely new
    to the corpus.
  - **Four repository modes** (Claims 3–5): The Default / Direct / Logical / Clone
    mode taxonomy is not described in any existing corpus note. The progression from
    most isolated to most authentic provides a testing escalation ladder not previously
    documented.
  - **Trial results JSON schema** (Claim 7): The structured result format
    (workflow_name, run_id, safe_outputs, agentic_run_info with token_usage) is not
    documented in any existing note. The inclusion of `token_usage` as a pre-deployment
    cost-estimation primitive is particularly notable.
  - **Multi-workflow side-by-side comparison** (Claim 10): The ability to run multiple
    workflow versions in a single trial command and compare combined results via `jq`
    is not described in any existing corpus note. This is the TrialOps-specific analog
    to A/B testing for workflow quality.
  - **`--append` flag for instruction testing** (Claim 9): Testing instruction additions
    without modifying the source workflow file is a prompt engineering primitive not
    documented elsewhere in the corpus.
  - **`--trigger-context` for event-driven workflow testing** (Claim 12): The mechanism
    for providing real GitHub issue context to workflows designed to respond to specific
    events is not documented in any existing note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: No existing chapter content covers pre-deployment
  workflow testing. Add TrialOps as the standard first phase of the gh-aw workflow
  lifecycle — before any workflow is deployed to a production repository, practitioners
  should validate it using `gh aw trial`. Recommend: (1) start with Default mode + dry-run;
  (2) use Clone mode for code-analysis workflows; (3) use `--trigger-context` for
  event-driven workflows; (4) check `agentic_run_info.token_usage` for cost estimation
  before production deployment.

- **Chapter 03 (Safety and Verification)**: Position TrialOps as the safety gate that
  precedes the safe rollout ladder. The complete safety lifecycle for a new workflow is:
  TrialOps in isolation → report-only deployment → staged mode validation → shadow
  evaluation → production writes. TrialOps Default mode is the zero-risk entry point:
  it validates workflow decision quality without any production side effects. Add the
  three-indicator success definition (green checkmark + expected outputs + no log errors)
  as the minimum passing bar before a workflow enters production deployment.

- **Chapter 04 (Production Patterns)**: Add multi-workflow TrialOps comparison (`gh aw
  trial v1.md v2.md --repeat N`) as the recommended approach for evaluating workflow
  variants. When teams need to choose between two approaches (e.g., different prompts,
  different safe output configurations), TrialOps provides a structured, programmatically
  analyzable comparison via the combined results JSON file. The `--repeat` flag adds
  the statistical reliability needed for non-deterministic AI outputs.

- **Chapter 07 (Cost Management)**: Add pre-deployment cost estimation via TrialOps as
  a standard practice. The `agentic_run_info.token_usage` field in the trial result JSON
  provides a cost proxy for each trial run. Comparing token usage across workflow versions
  (using the multi-workflow comparison feature) enables practitioners to identify
  cost-efficient variants before committing to production deployment.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The `gh aw` documentation site uses an
   Astro/Starlight SPA that WebFetch processes through an AI model before returning
   content. Three independent fetches were made with different prompts. Quotes used in
   this note appeared consistently across all three fetches; they are treated as verbatim.
   Where fetch results varied in wording, the claim is marked "(no direct quote; see
   paraphrase in Our assessment)" per MINER.md §2a.

2. **Related pages not followed**: The source's "Related Documentation" section references
   SideRepoOps, MultiRepoOps, Orchestration patterns, and Safe Outputs. SideRepoOps is
   partially documented in `docs-ghaw-ephemerals.md`; MultiRepoOps has no dedicated corpus
   note; Orchestration is covered by `docs-ghaw-orchestration-patterns.md`; Safe Outputs
   is covered by `docs-ghaw-how-they-work.md`. None were fetched as part of this
   extraction — they are either already in the corpus or outside this note's scope.

3. **No publication date**: Like other gh-aw `patterns/` pages, this page carries no
   explicit publication date. `date_published` is left null. Content is consistent with
   the current `gh aw` platform as of the extraction date (2026-05-11).

4. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose any existing note at the MINER.md §4a filing threshold.
   The TrialOps pattern is novel to the corpus — no existing note covers this territory
   to contradict it.

5. **Repository mode quotes**: The individual mode descriptions ("github.repository points
   to your repo; outputs go to trial repo" etc.) appeared consistently across all three
   fetches in the same phrasing. They are treated as verbatim but noted here as potentially
   rendered from table cells rather than running prose — the phrasing is terse in a way
   consistent with table content.
