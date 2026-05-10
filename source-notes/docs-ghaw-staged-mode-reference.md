---
source_url: https://github.github.com/gh-aw/reference/staged-mode
source_type: docs
title: "GitHub Agentic Workflows: Staged Mode Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#412"
---

# GitHub Agentic Workflows: Staged Mode Reference

> The authoritative YAML syntax and behavioral reference for gh-aw staged mode —
> the feature that runs workflows completely while replacing every write operation
> with a step-summary preview, enabling dry-run validation of safe outputs before
> production writes are enabled. Provides the configuration syntax that
> `docs-ghaw-safe-rollout.md` explicitly defers to.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, in the
  `reference/` section — the same section as `docs-ghaw-rate-limiting-controls.md`
  and `docs-ghaw-permissions-reference.md`; reference pages document platform
  feature syntax and behavior, not practitioner patterns or conceptual overviews)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  Agent Factory series and all `reference/` documentation). Claims about YAML
  syntax, environment variable contracts, and feature scope are authoritative for
  the `gh aw` platform. The recommended adoption pattern reflects practitioner
  guidance from the team running 183+ production workflows.
- **Scope**: Covers: enabling staged mode globally, per-output-type scoping,
  the step-summary preview format, all supported output types, custom safe output
  job integration via `GH_AW_SAFE_OUTPUTS_STAGED`, preview message customization
  via the `messages:` block, and the recommended adoption pattern. Does NOT cover:
  the conceptual distinction between staged mode and shadow evaluation (see
  `docs-ghaw-safe-rollout.md` Claims 3–4), the Safe Outputs permission model
  (see `docs-ghaw-how-they-work.md` Claim 5), or the full rollout ladder (see
  `docs-ghaw-safe-rollout.md`). This page is the syntax reference; safe-rollout
  is the governance lifecycle guide.

## Extracted Claims

### Claim 1: Staged mode runs the workflow completely while skipping every write operation, replacing each with a structured preview in the GitHub Actions step summary.

- **Evidence**: Core behavioral definition stated consistently across multiple
  fetches of the reference page; described as the defining property of the
  feature on the page.
- **Confidence**: settled (first-party reference documentation; this is a
  definitional claim about the feature's observable behavior)
- **Quote**: (no direct quote; wording varied slightly across fetches — the
  core claim is "workflows run completely but skip all write operations" per one
  fetch, "every write operation is skipped; instead, a detailed preview appears
  in the GitHub Actions step summary" per another; see Concrete Artifacts for
  preserved descriptions)
- **Our assessment**: The two-part behavior is the essential property: (a) the
  workflow *runs completely* — no early exit, no short-circuit, no reduced
  execution path; (b) each write is *replaced*, not silently dropped, with a
  step-summary preview. Together these guarantee complete visibility: the
  practitioner sees exactly what the workflow would do, with no missing steps
  and no silent failures. For Ch02 (Harness Engineering): staged mode is the
  standard gh-aw dry-run mechanism, and its "complete execution + visible
  preview" guarantee distinguishes it from simply disabling safe outputs.

### Claim 2: Staged mode is enabled by adding `staged: true` to the `safe-outputs:` block in workflow frontmatter; it defaults to `false`.

- **Evidence**: The YAML syntax appears consistently across multiple fetches; the
  default-false behavior is made explicit by per-type examples showing
  `staged: false` as the commented default value.
- **Confidence**: settled (first-party reference documentation with explicit
  YAML configuration examples)
- **Quote**: (no direct quote; see Concrete Artifacts for the full YAML examples)
- **Our assessment**: The placement within `safe-outputs:` is architecturally
  meaningful: staged mode is a *property of the safe-outputs configuration*, not
  a standalone workflow flag. This means staged mode is only relevant when safe
  outputs are configured — a workflow without safe outputs has nothing to stage.
  The default-false value also means production writes are the default starting
  state: teams must opt in to staged mode explicitly, and must remember to remove
  `staged: true` when promoting to production. For Ch02: the promotion step
  (removing `staged: true`) should be part of any deployment checklist for new
  gh-aw workflows.

### Claim 3: Staged mode can be scoped to individual output types, enabling granular previewing where some outputs preview while others execute normally in the same workflow run.

- **Evidence**: Per-type scoping YAML examples appear in multiple fetches,
  showing `create-pull-request: staged: true` alongside an `add-comment:` block
  that executes normally — both in the same workflow.
- **Confidence**: settled (first-party reference documentation with explicit YAML
  examples demonstrating the per-type control surface)
- **Quote**: (no direct quote for the surrounding prose; see Concrete Artifacts
  for the YAML examples)
- **Our assessment**: Per-type scoping is the most operationally useful staging
  configuration for production deployments. A workflow that has reached
  production-trust level for most output types but not for a newly added PR
  creation step can scope staged mode to just that type. This enables incremental
  trust promotion at the individual output-type level, rather than requiring
  the whole workflow to remain staged while one type is being validated. For
  Ch03 (Safe Outputs): per-type scoping provides a fine-grained control surface
  that aligns with the principle of least-privilege escalation — introduce
  production writes one output type at a time.

### Claim 4: The preview format displays in the step summary showing a structured description of what would happen if staged mode were disabled, with all output fields populated.

- **Evidence**: Multiple fetches describe the preview as appearing in the step
  summary with all fields (titles, bodies, labels, assignees). Fetch 3's
  `messages:` block template reveals the default preview format string.
- **Confidence**: settled (first-party reference documentation; the preview
  format is explicitly described)
- **Quote**: "The following {operation} would occur if staged mode was disabled:"
  (from the `staged-description` default in the `messages:` block, fetch 3 —
  this is the default preview description template)
- **Our assessment**: The step summary is the primary practitioner interface with
  staged mode — it is how teams decide whether a proposed write looks correct.
  The fact that all populated fields (titles, bodies, labels, assignees) are
  shown means practitioners get a complete view of the intended artifact.
  For Ch03: the step summary preview functions as an audit surface for proposed
  writes, not merely a debugging tool, and should be treated as a formal review
  artifact in any staged-mode workflow that feeds a promotion decision.

### Claim 5: Custom safe output jobs must implement their own staged-mode behavior by detecting the `GH_AW_SAFE_OUTPUTS_STAGED` environment variable, which is set to `"true"` when staged mode is active.

- **Evidence**: The environment variable name appears consistently across multiple
  fetches; described as the integration contract for custom jobs. Built-in safe
  output types handle staged mode automatically; custom jobs must opt in.
- **Confidence**: settled (first-party reference documentation; specific,
  testable API contract)
- **Quote**: (no direct quote for the surrounding explanation; the env var name
  `GH_AW_SAFE_OUTPUTS_STAGED` is verbatim from multiple fetches)
- **Our assessment**: This environment variable is the extensibility seam between
  the platform's staged-mode mechanism and user-defined safe outputs. The
  asymmetry matters: if a team adds a custom safe output job and forgets to check
  `GH_AW_SAFE_OUTPUTS_STAGED`, staged mode will have no effect on that job — it
  will execute normally even when `staged: true` is set globally. This is a
  potential footgun for teams that mix built-in and custom safe outputs. For
  Ch02: any custom safe output job implementation template should include
  `GH_AW_SAFE_OUTPUTS_STAGED` detection as a required pattern, not an optional
  enhancement.

### Claim 6: Preview message customization is available through a `messages:` block with `staged-title` and `staged-description` keys; the `{operation}` placeholder is replaced with the safe output operation name.

- **Evidence**: Fetch 3 provided verbatim YAML for the `messages:` block; the
  `{operation}` placeholder is explicitly documented with an example substitution.
- **Confidence**: settled (first-party reference with specific YAML schema and
  documented placeholder behavior)
- **Quote**: "The `{operation}` placeholder is replaced with the safe output
  operation name (for example, `issue creation`)."
- **Our assessment**: Preview message customization serves organizational
  consistency — teams that run staged workflows in shared repositories can
  brand or contextualize the preview format for their audience. The single
  `{operation}` placeholder means the same template is applied across all output
  types in the workflow; there is no per-type message customization documented
  on this page. For Ch02: the `messages:` block is a quality-of-life feature;
  its value increases when staged-mode previews are reviewed by stakeholders
  outside the team that wrote the workflow.

### Claim 7: The recommended adoption pattern is a 5-step iterative loop — enable staged mode, trigger on a real event, review the preview, adjust, repeat until stable, then remove `staged: true`.

- **Evidence**: Fetch 3 provided a verbatim 5-step description from the
  "Recommended Workflow" section of the page.
- **Confidence**: emerging (first-party practitioner recommendation from the
  team running the platform; the 5-step structure is explicit but "common" leaves
  room for variations)
- **Quote**: "A common adoption pattern is to start with staged mode and disable
  it once you're satisfied: 1. Enable `staged: true` and trigger the workflow on
  a real event. 2. Open the Actions run and review the preview. 3. Adjust the
  workflow prompt or configuration based on the preview. 4. Repeat until the
  output looks correct. 5. Remove `staged: true` to start creating real GitHub
  resources."
- **Our assessment**: This loop frames staged mode as a *development tool*,
  not a permanent production mode. The phrase "start creating real GitHub
  resources" in step 5 marks the promotion as a threshold event — the workflow
  graduates from previewing to acting. This is the operational implementation
  of rung 2 in `docs-ghaw-safe-rollout.md`'s rollout ladder (Claim 2): staged
  mode is not indefinite, it is a validation phase with a defined exit condition.
  For Ch02: present this 5-step loop as the standard harness iteration cycle for
  gh-aw practitioners, alongside the `gh aw compile --watch` / `gh aw run` dev
  loop from `docs-ghaw-how-they-work.md` Claim 11.

### Claim 8: The page recommends keeping staged mode enabled during prompt iteration and only disabling it once the workflow is stable, suggesting staged mode should be re-enabled after any prompt changes.

- **Evidence**: Fetch 3 extracted a callout box with this explicit recommendation,
  appearing as highlighted guidance rather than body text.
- **Confidence**: emerging (callout-box recommendation from first-party
  documentation; not a platform constraint, a practitioner guidance statement)
- **Quote**: "Keep staged mode enabled when iterating on prompt changes, and
  only remove it when the workflow is stable."
- **Our assessment**: This callout extends staged mode's role beyond initial
  development into ongoing prompt engineering. A team that modifies a workflow's
  natural language instructions should re-enable `staged: true` to verify the
  new behavior before returning to production writes. This implies staged mode
  is not a one-time gate that a workflow passes through once during initial
  deployment — it is a repeatable validation mode that should be used whenever
  the workflow's decision logic changes. For Ch02: recommend that any workflow
  prompt change trigger a staged-mode review cycle before the change is
  deployed to production.

### Claim 9: Staged mode supports all built-in safe output types, including issue operations, comments, labels, discussions, pull requests, projects, releases, release assets, workflow dispatch, agent assignment, and agent session creation.

- **Evidence**: Fetch 3 provided an explicit list of 23 output types; fetch 1
  described "all 24 built-in safe output types" — a count discrepancy exists
  between fetches. The explicit list from fetch 3 is used here.
- **Confidence**: emerging (the explicit type list is from one fetch; the count
  discrepancy creates uncertainty about completeness)
- **Quote**: (no direct quote for the count claim; see Concrete Artifacts for
  the explicit type list from fetch 3)
- **Our assessment**: The presence of `assign-to-agent` and `create-agent-session`
  in the supported types is notable: staged mode works for orchestration-level
  operations, not just content creation. A multi-agent workflow that uses
  `assign-to-agent` to dispatch work to sub-agents can preview those
  assignments before any agent is actually tasked. This extends staged mode's
  scope from "preview what gets written to GitHub" to "preview how the
  orchestration would fan out." For Ch09 (Agent Orchestration): staged mode
  should be recommended as a validation tool for multi-agent dispatch chains,
  not only for content-producing workflows.

## Concrete Artifacts

### Enabling Staged Mode Globally (from source, YAML)

```yaml
---
on: issues
safe-outputs:
  staged: true
  create-issue:
    title-prefix: "[ai] "
    labels: [automation]
---
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — enabling staged mode section*

### Per-Output-Type Scoping (from source, YAML)

```yaml
safe-outputs:
  staged: false         # default
  create-pull-request:
    staged: true        # PRs preview only
  add-comment:          # comments execute normally
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — scoping staged mode per output type section*

### Preview Message Customization (from source, YAML)

```yaml
---
safe-outputs:
  staged: true
  messages:
    staged-title: " Preview: {operation}"
    staged-description: "The following {operation} would occur if staged mode was disabled:"
  create-issue:
---
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — customizing preview messages section*

Note: The `{operation}` placeholder is replaced with the safe output operation name
(e.g., `issue creation`).

### Recommended Adoption Pattern (from source, verbatim 5-step list)

```
A common adoption pattern is to start with staged mode and disable it once
you're satisfied:

1. Enable `staged: true` and trigger the workflow on a real event.
2. Open the Actions run and review the preview.
3. Adjust the workflow prompt or configuration based on the preview.
4. Repeat until the output looks correct.
5. Remove `staged: true` to start creating real GitHub resources.
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — recommended workflow section*

### Callout Box (from source, verbatim)

```
Keep staged mode enabled when iterating on prompt changes, and only remove
it when the workflow is stable.
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — callout box*

### Supported Output Types (from source, explicit list — fetch 3)

```
create-issue, update-issue, close-issue
add-comment
add-labels, remove-labels
create-discussion, update-discussion, close-discussion
create-pull-request, update-pull-request, close-pull-request
create-pull-request-review-comment
push-to-pull-request-branch
create-project, update-project, create-project-status-update
update-release, upload-asset
dispatch-workflow
assign-to-agent, assign-to-user
create-agent-session
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — supported output types section*
*Note: fetch 1 described "24 built-in safe output types"; fetch 3 lists 23 explicitly. Count discrepancy noted.*

### Custom Safe Output Job Integration

```
Environment variable: GH_AW_SAFE_OUTPUTS_STAGED
Value when staged mode is active: "true"
Required behavior: skip real operation; display preview instead
Note: built-in safe output types handle this automatically;
      custom jobs must implement the check explicitly
```
*Source: https://github.github.com/gh-aw/reference/staged-mode — staged mode for custom safe output jobs section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-safe-rollout.md` Claim 2 (the four-rung rollout ladder with staged
    mode as rung 2): this reference page's recommended 5-step adoption loop (Claim 7)
    is the operational implementation of that rung. The ladder says "enable staged
    behavior when proposed writes need to be previewed"; this page provides the
    syntax and loop for doing so. The two notes together form a complete picture:
    safe-rollout gives the when and why, this page gives the how and what.
  - `docs-ghaw-safe-rollout.md` Claim 3 (staged mode answers "what would the
    workflow do?" vs. shadow evaluation's "does the real write path behave correctly?"):
    this page's behavioral description (Claim 1 — complete execution, all writes
    replaced with previews) confirms why staged mode answers the first question
    but not the second. Because the workflow executes completely but no resources
    are created, practitioners see the proposed decisions but not the actual
    write-path execution.
  - `docs-ghaw-safe-rollout.md` Claim 4 (staged mode sufficient when main risk
    is decision quality): the complete-execution-with-preview model (Claim 1)
    is exactly the mechanism that makes staged mode sufficient for that risk
    class. The preview shows all fields the AI decided on; that is decision
    quality in observable form.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as pre-approved operations
    without write permissions): staged mode is an *operating mode* of Safe Outputs —
    it modifies the behavior of safe-output execution (replacing write with preview)
    rather than bypassing the permission model. The `staged: true` key lives inside
    `safe-outputs:` precisely because it governs how those outputs behave.

- **Contradicts**: None. This reference page is the authoritative YAML syntax
  documentation for staged mode. `docs-ghaw-safe-rollout.md` explicitly defers
  to this page ("see the Staged Mode reference linked from this page") for syntax
  details; there are no conflicting claims in the corpus. The count discrepancy
  between fetches (23 vs 24 supported types) is a rendering ambiguity, not a
  substantive contradiction.

- **Extends**:
  - `docs-ghaw-safe-rollout.md`: that source characterized staged mode
    conceptually (what question it answers, when to use it, its position in the
    rollout ladder). This reference page provides the syntax and configuration
    details that safe-rollout deferred to. Together they are the complete staged
    mode resource: safe-rollout for governance rationale, this page for
    implementation syntax.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as the permission-separation
    pattern): this page extends the base Safe Outputs model with staged mode as
    an operating configuration. The base model describes what safe outputs are
    and how they work; this page describes how to run them in preview mode.
  - `docs-ghaw-how-they-work.md` Claim 11 (recommended dev loop: compile →
    watch → run → review): this page's 5-step adoption loop (Claim 7) is the
    staged-mode-specific extension of that dev loop. The two loops compose:
    the how-they-work dev loop handles structural validation (`gh aw compile`),
    while this page's loop handles behavioral validation (staged → preview →
    adjust → repeat → disable).

- **Novel**:
  - **Complete YAML syntax for staged mode** (Claims 2–3, Concrete Artifacts):
    No existing source note documents the `staged: true` key, per-type scoping
    syntax, or the `messages:` block. `docs-ghaw-safe-rollout.md` references
    the syntax but explicitly defers to this page; `docs-ghaw-how-they-work.md`
    mentions Safe Outputs conceptually but not the staged-mode configuration.
    This page is the corpus's first documentation of these YAML specifics.
  - **`GH_AW_SAFE_OUTPUTS_STAGED` environment variable** (Claim 5): The
    integration contract for custom safe output jobs has not appeared in any
    existing source note. This is new to the corpus and is the only mechanism
    by which custom jobs can participate in staged mode.
  - **`messages:` block for preview customization** (Claim 6): No existing
    source note mentions the `staged-title`, `staged-description`, or
    `{operation}` placeholder. This is entirely new.
  - **Per-type scoping as an incremental trust mechanism** (Claim 3): While
    `docs-ghaw-safe-rollout.md` describes the rollout ladder at the workflow
    level, per-type scoping allows sub-workflow-level trust promotion (one output
    type at a time). This granularity level is not described in any existing note.
  - **Orchestration output types in staged mode** (`assign-to-agent`,
    `create-agent-session` in Claim 9): The presence of orchestration-level
    operations in the staged-mode surface is not noted in any existing source.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: `docs-ghaw-safe-rollout.md` introduced
  staged mode as a rollout concept but had no YAML syntax. Add the `staged: true`
  configuration pattern from this page as the harness implementation reference.
  Add the per-type scoping YAML as the recommended pattern for incremental
  trust promotion within a single workflow. Add the `messages:` block as an
  optional harness configuration for teams that share staged-mode previews with
  non-authors. Add the recommendation to re-enable `staged: true` after prompt
  changes (Claim 8) as a harness maintenance rule.

- **Chapter 03 (Safe Outputs & Staged Rollout)**: This page is the authoritative
  reference for staged mode syntax. Ch03 should cite this page for any YAML
  examples of staged mode. The custom job integration via `GH_AW_SAFE_OUTPUTS_STAGED`
  (Claim 5) should be added as a required implementation detail for any guidance
  on building custom safe outputs — the environment variable check must be
  documented as mandatory, not optional, since forgetting it causes staged mode
  to silently not apply to that job. The callout (Claim 8 — keep staged during
  prompt iteration) should be added as a best practice box.

- **Chapter 09 (Agent Orchestration)**: The presence of `assign-to-agent` and
  `create-agent-session` in staged mode's supported types (Claim 9) means
  staged mode can preview multi-agent dispatch chains, not just content writes.
  Ch09 should recommend staged mode as a validation tool for orchestrator
  workflows before promoting agent-assignment logic to production. This
  extends the safe rollout guidance (currently focused on content-producing
  workflows) to orchestration workflows.

## Extraction Notes

1. **WebFetch rendering variability**: The page was fetched three times with
   different prompts. Minor wording discrepancies appeared between fetches,
   particularly in the emoji used for the step summary indicator (🔍 in fetch 1,
   🎭 in fetch 2) and in the count of supported output types (24 in fetch 1,
   23 explicitly listed in fetch 3). All quotes marked as uncertain use
   `(no direct quote; see paraphrase in Our assessment)` per MINER.md §2a.
   Concrete YAML artifacts are consistent across fetches and are included
   verbatim as extracted by the tool.

2. **Count discrepancy**: Fetch 1 said "All 24 built-in safe output types";
   fetch 3 listed 23 types explicitly. The explicit list from fetch 3 is
   preserved in Concrete Artifacts. The guide should not assert a specific
   count pending re-verification against the live page.

3. **No linked sub-pages followed**: The reference page links to Safe Outputs
   Overview and the compilation process reference as related pages. Both are
   already covered in `docs-ghaw-how-they-work.md` and `docs-ghaw-compilation-process.md`.
   No additional sub-pages were fetched.

4. **No contradictions filed**: Reviewed existing source notes. No claims in
   this source materially oppose existing notes. The primary overlap is with
   `docs-ghaw-safe-rollout.md`, which characterizes staged mode conceptually;
   this page provides compatible syntax details that deepen rather than contradict
   that characterization.
