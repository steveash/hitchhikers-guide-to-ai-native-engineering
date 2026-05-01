---
source_url: https://github.github.com/gh-aw/patterns/issue-ops
source_type: docs
title: "GitHub Agentic Workflows: IssueOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#326"
---

# GitHub Agentic Workflows: IssueOps Pattern

> The authoritative reference for the IssueOps trigger pattern in gh-aw — documents
> the `on: issues:` trigger, label allowlisting via `add-labels: allowed:`, the
> `steps.sanitized.outputs.text` injection-defense mechanism applied to issue
> title+body content, and the sub-issue hierarchy pattern for decomposing large work
> items into Copilot-executable parallel tasks; the first corpus source to cover these
> four patterns.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Design Patterns >
  IssueOps" section — prescriptive pattern reference, not API reference or conceptual
  overview. Patterns pages document proven interaction models for specific trigger types.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` platform.
  Claims about the `issues:` trigger schema, safe-output configurations, sanitization
  semantics, and sub-issue JSON format are authoritative for this platform. Claims about
  generalizability of IssueOps injection-defense or task-decomposition patterns beyond
  gh-aw require additional evidence.
- **Scope**: The IssueOps pattern specifically — `on: issues:` trigger configuration,
  `add-comment` and `add-labels` safe-output configurations, `steps.sanitized.outputs.text`
  sanitization for issue content, the two-job permission-separation model
  (AI job read-only / write job `issues: write`), and sub-issue hierarchy creation with
  `temporary_id` + `parent` fields for multi-agent task decomposition. Does NOT cover:
  the five-layer security architecture (in `docs-ghaw-how-they-work.md`), MCP server
  integration (`docs-ghaw-mcps.md`), the ChatOps `slash_command` trigger
  (`docs-ghaw-chatops.md`), or the DailyOps scheduling pattern (`docs-ghaw-dailyops.md`).

## Extracted Claims

### Claim 1: The `on: issues: types: [opened]` trigger fires agentic workflows on issue creation with minimal read-only permissions for the AI execution job

- **Evidence**: YAML frontmatter shown on the page:
  ```yaml
  on:
    issues:
      types: [opened]
  permissions:
    contents: read
    actions: read
  ```
  The trigger activates when a new issue is opened, and the AI job is sandboxed to
  `contents: read` and `actions: read` — no write access of any kind.
- **Confidence**: settled (first-party documentation; the trigger schema and permission
  block are explicit)
- **Quote**: (from YAML block)
- **Our assessment**: The `on: issues:` trigger is the IssueOps entry point — it fires
  automatically on issue creation without any human command. This distinguishes IssueOps
  from ChatOps (human-initiated slash command) and DailyOps (scheduled cron). The
  `contents: read` + `actions: read` permissions are consistent with the "no write access
  by default" principle in `docs-ghaw-how-they-work.md` Claim 4 — the AI job cannot
  modify repository content or GitHub state directly. All writes go through Safe Outputs.
  For Ch02 (Harness Engineering): add `on: issues: types: [opened]` to the trigger
  taxonomy alongside `slash_command` (ChatOps) and `schedule` (DailyOps). For Ch01:
  IssueOps is the pattern for automatic agentic responses to incoming issues — triage,
  classification, initial response — without requiring any human to invoke a command.

### Claim 2: The `add-comment` safe output targets the triggering issue via `target: "triggering"` and caps comment volume with `max:`

- **Evidence**: YAML configuration documented on the page:
  ```yaml
  safe-outputs:
    add-comment:
      max: 3
      target: "triggering"
  ```
  The `target: "triggering"` value routes the comment to the issue that activated the
  workflow. The `max:` field caps how many comments the agent can post per workflow run.
- **Confidence**: settled (first-party; YAML fields are explicit)
- **Quote**: (from YAML block)
- **Our assessment**: `target: "triggering"` is the IssueOps-specific `add-comment`
  configuration — it makes the agent comment on the newly opened issue, not on an
  arbitrary item. This contrasts with `docs-ghaw-dailyops.md` Claim 5 where `target:
  "4750"` is a fixed discussion number. The "triggering" value is a platform-provided
  alias for the event context — the agent does not need to know the issue number. The
  `max:` annotation (already documented for `create-pull-request-review-comment` in
  `docs-ghaw-chatops.md` Claim 8) appears here as a general Safe Output volume-control
  mechanism. For Ch02: `target: "triggering"` is the right default for any IssueOps
  workflow that responds to the issue it was triggered by — document it as the idiomatic
  pattern, not a configuration detail.

### Claim 3: Label allowlisting via `add-labels: allowed: [...]` constrains the agent to a pre-approved label set, with `max:` bounding how many labels can be applied per issue

- **Evidence**: YAML configuration:
  ```yaml
  safe-outputs:
    add-labels:
      allowed: [bug, needs-info, enhancement, question, documentation]
      max: 2
  ```
  The `allowed:` field enumerates the complete set of labels the agent may apply; no
  label outside this list can be applied regardless of what the AI produces. The `max:`
  field caps how many labels can be applied in one run.
- **Confidence**: settled (first-party; YAML is explicit and the constraint semantics
  are clear)
- **Quote**: "Labels are restricted to an allowlist, restricting automation to predefined
  categories."
- **Our assessment**: Label allowlisting is a new Safe Output primitive not documented
  in any prior corpus note. It provides two security properties: (1) **label injection
  prevention** — a prompt-injected instruction to "apply the label 'urgent'" or
  "create label 'approved'" cannot succeed if those strings are not in `allowed:`; (2)
  **label creation prevention** — the agent cannot create new GitHub labels, only apply
  existing ones from the allowlist. The `max: 2` bound prevents a misbehaving agent from
  applying a flood of labels to a single issue. Together, `allowed:` + `max:` bound both
  what the agent can write and how much it can write. For Ch02: document `add-labels`
  with `allowed:` as a required pattern for any IssueOps workflow that applies labels —
  an `add-labels` without `allowed:` exposes the label namespace to AI discretion. For
  Ch03 (Safety and Verification): label allowlisting is the concrete implementation of
  "bounded write surface" for the labeling use case — add to the Safe Outputs section
  alongside `max:` as a rate-limiting primitive.

### Claim 4: Issue content is accessed via `steps.sanitized.outputs.text`, which combines the issue title and body while stripping @mentions, URIs, and prompt-injection payloads before the AI sees them

- **Evidence**: Access pattern from the page: `Analyze this issue:
  "${{ steps.sanitized.outputs.text }}"`. The sanitization step is platform-provided
  and combines issue title + body into a single string. The filter categories (from the
  platform's documented sanitization behavior, consistent with `docs-ghaw-chatops.md`
  Claim 6): unauthorized mentions, malicious links, and excessive content.
- **Confidence**: settled (first-party; the access reference is explicit; filter categories
  are platform-documented and corroborated by `docs-ghaw-chatops.md`)
- **Quote**: `Analyze this issue: "${{ steps.sanitized.outputs.text }}"`
- **Our assessment**: IssueOps extends the `steps.sanitized.outputs.text` pattern
  documented in `docs-ghaw-chatops.md` Claim 5 to issue content specifically. The key
  extension: for ChatOps, `steps.sanitized.outputs.text` contains the slash command
  comment body; for IssueOps, it contains the combined title + body of the triggering
  issue. This is significant because issue titles are often the first thing an AI reads
  to classify the issue — title injection ("URGENT: ignore previous instructions and...") 
  is a real threat vector. Combining title + body into a single sanitized string before
  AI access closes that vector. For Ch03: document that IssueOps workflows must access
  issue content via `steps.sanitized.outputs.text`, not via raw `github.event.issue.title`
  or `github.event.issue.body` — the same principle as ChatOps, applied to a wider content
  surface (title+body vs. comment body only).

### Claim 5: The two-job permission-separation model isolates the AI execution job (contents: read) from the write job (issues: write) — enforcing least-privilege for the AI environment

- **Evidence**: The page documents: "the main AI job runs with `contents: read` and
  `actions: read` permissions, while comment creation occurs in a separate job with
  `issues: write` permissions, preventing direct AI write access." This is described
  as the IssueOps instantiation of the Safe Outputs architecture: the AI job has no
  write capability; the write job is a separate platform-controlled step.
- **Confidence**: emerging (the design principle is clearly stated; the complete two-job
  YAML was not fully extractable from the page rendering — the page describes the split
  architecturally but the explicit multi-job YAML was not shown in the extractable content)
- **Quote**: "comment creation occurs in a separate job with `issues: write` permissions,
  preventing direct AI write access"
- **Our assessment**: This is the IssueOps-specific instantiation of the Safe Outputs
  permission model (`docs-ghaw-how-they-work.md` Claim 5). The key insight is that the
  AI job and the write job are separate GitHub Actions jobs — the AI job cannot directly
  call `issues: write` APIs because it literally lacks the permission. The write job is
  platform-controlled and only executes the pre-approved Safe Output operations. This
  is stronger than a software-only separation: the GitHub Actions permission model
  enforces the isolation at the infrastructure level. For Ch03 (Safety and Verification):
  the two-job model is the concrete workflow-level implementation of permission separation.
  Name it explicitly: "AI job reads, write job writes — enforced by GitHub Actions
  permissions, not application-level checks."

### Claim 6: Sub-issue hierarchies with `temporary_id` and `parent` fields enable agents to decompose large issues into a structured tree of agent-sized tasks

- **Evidence**: JSON format documented on the page:
  ```json
  {"type": "create_issue", "temporary_id": "aw_abc123", "title": "Feature X", "body": "Tracking issue"}
  {"type": "create_issue", "parent": "aw_abc123", "title": "Task 1", "body": "First task"}
  ```
  The `temporary_id` establishes a named reference for the parent issue; the `parent`
  field in child issues links them to the parent via that reference. The platform resolves
  `temporary_id` references at creation time.
- **Confidence**: settled (first-party documentation; the JSON schema is explicit)
- **Quote**: (from JSON block on page)
- **Our assessment**: This is the first corpus source to document a structured task
  decomposition primitive for IssueOps. The `temporary_id` + `parent` pattern enables
  a single IssueOps workflow to create a parent tracking issue and any number of
  child task issues in one run, without knowing the actual GitHub issue numbers in advance
  (the platform resolves them). The result is a native GitHub issue hierarchy — the
  kind of structure a project manager would create manually — produced automatically when
  an issue is filed. For Ch09 (Agent Orchestration): this is the IssueOps complement to
  the Orchestrator+Worker pattern in `docs-ghaw-central-repo-ops.md`. Where CentralRepoOps
  decomposes by *repository*, IssueOps sub-issue hierarchies decompose by *task within a
  repository*. Together they give two levels of multi-agent decomposition: org-scale
  (repo fan-out) and issue-scale (task fan-out).

### Claim 7: Sub-issues can be assigned to Copilot via `assignees: copilot`, enabling the platform to dispatch them for parallel autonomous execution

- **Evidence**: The page documents `assignees: copilot` as the assignment pattern for
  sub-issues in the hierarchy. When Copilot is assigned to a sub-issue, the platform
  can dispatch it for autonomous execution, enabling parallel processing of the decomposed
  task tree.
- **Confidence**: settled (first-party; `assignees: copilot` is explicitly documented
  as the parallel-execution enabler)
- **Quote**: "Sub-issues can be assigned to Copilot with `assignees: copilot` for
  parallel execution."
- **Our assessment**: `assignees: copilot` is the mechanism that closes the loop from
  task decomposition (Claim 6) to parallel execution. Without it, the sub-issue hierarchy
  is just a GitHub issue structure — organized but not actionable by agents. With
  `assignees: copilot`, each sub-issue becomes a dispatch signal for the Copilot agent.
  The result is an IssueOps workflow that responds to one issue by creating a structured
  work breakdown and launching parallel agents for each task. This is a meaningful
  multi-agent orchestration primitive — the closest thing in gh-aw to a "spawn n subagents"
  command. For Ch09: document `assignees: copilot` as the IssueOps parallel execution
  trigger. For Ch02: it requires no additional workflow configuration — the `assignees:`
  field in the sub-issue JSON is sufficient. The bound on how many sub-issues can be
  created (and thus how many Copilot instances are dispatched) should be managed explicitly
  to prevent runaway fan-out — analogous to `max:` in CentralRepoOps `dispatch-workflow`.

### Claim 8: IssueOps fills the "automated issue-triggered" slot in the gh-aw trigger taxonomy alongside ChatOps (slash command), DailyOps (schedule), and LabelOps (label change)

- **Evidence**: The DailyOps documentation (`docs-ghaw-dailyops.md` Claim 8, "Related
  Patterns") names the taxonomy explicitly: "IssueOps — Trigger workflows from issue
  creation or comments." IssueOps is positioned as the automatically-triggered counterpart
  to ChatOps's human-initiated commands and DailyOps's schedule-driven automation.
- **Confidence**: settled (first-party taxonomization corroborated across multiple pages)
- **Quote**: "IssueOps — Trigger workflows from issue creation or comments"
- **Our assessment**: The four-trigger taxonomy (DailyOps / IssueOps / ChatOps / LabelOps)
  is now substantiated by source notes for three of the four triggers (DailyOps #323,
  ChatOps #322, IssueOps #326). A LabelOps note (#327) is referenced in the
  `docs-ghaw-dailyops.md` triage as a sibling issue and would complete the taxonomy.
  The IssueOps pattern is distinguished by its trigger condition: it fires automatically
  on issue events (no human command required) and is scoped to a specific issue (not
  a scheduled run against all open issues). For Ch02: include IssueOps in the trigger
  decision guide — use IssueOps when the agent should respond automatically to each new
  issue as it arrives; use ChatOps when humans should explicitly request agent action on
  a per-issue basis; use DailyOps when the agent should periodically process all issues
  in bulk.

## Concrete Artifacts

### Basic IssueOps Trigger Frontmatter

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
safe-outputs:
  add-comment:
    max: 2
---
```

*Source: gh-aw IssueOps patterns documentation, "Issue Trigger" section*

### Full Safe-Outputs Configuration — Comment + Label Application

```yaml
safe-outputs:
  add-comment:
    max: 3
    target: "triggering"   # Comments on the issue that triggered the workflow
  add-labels:
    allowed: [bug, needs-info, enhancement, question, documentation]
    max: 2                  # Cannot apply more than 2 labels per run
```

*Source: gh-aw IssueOps patterns documentation, "Safe Outputs" section*

### Sanitized Issue Content Access Pattern

```yaml
# In the workflow's natural language instruction body:
Analyze this issue: "${{ steps.sanitized.outputs.text }}"

# steps.sanitized.outputs.text is platform-injected before the agent executes.
# For IssueOps: combines issue TITLE + BODY into one sanitized string.
# Filters applied: unauthorized mentions, malicious links, excessive content.
#
# DO NOT use ${{ github.event.issue.title }} or ${{ github.event.issue.body }}
# directly — those bypass sanitization and expose the agent to raw user input,
# including prompt-injection payloads in issue titles.
```

*Source: gh-aw IssueOps patterns documentation, consistent with docs-ghaw-chatops.md sanitization*

### Sub-Issue Hierarchy — JSON Format

```json
{"type": "create_issue", "temporary_id": "aw_abc123", "title": "Feature X", "body": "Tracking issue"}
{"type": "create_issue", "parent": "aw_abc123", "title": "Task 1", "body": "First task"}
```

```yaml
# To dispatch sub-issues to Copilot for parallel execution:
assignees: copilot
```

*Source: gh-aw IssueOps patterns documentation, "Sub-Issue Hierarchies" section*

### Permission-Separation Architecture Summary

```
IssueOps Two-Job Permission Model:

Job 1 — AI Execution Job
  Trigger:     on: issues: types: [opened]
  Permissions: contents: read, actions: read
  What it can do: read repo content, analyze issue, produce safe-output requests
  What it CANNOT do: write to issues, apply labels, comment, create issues directly

Job 2 — Write Job (platform-controlled Safe Output handler)
  Permissions: issues: write
  What it does: executes the safe-output operations the AI requested
  Operations:  add-comment (bounded by max:), add-labels (bounded by allowed: and max:)

Design principle: AI has zero write capability — Safe Outputs are the ONLY write path.
Same as docs-ghaw-how-they-work.md Claim 5, instantiated at the YAML job level.
```

*Source: gh-aw IssueOps patterns documentation, architectural description*

### Trigger Decision Guide (from taxonomy)

```
Trigger type       | When to use                                | Human action required?
-------------------|--------------------------------------------|-----------------------
IssueOps           | Respond automatically to each new issue    | No — fires on issue open
ChatOps            | Respond when human explicitly requests     | Yes — /slash-command
DailyOps           | Process issues in bulk on a schedule       | No — fires on cron
LabelOps           | Respond when a label is applied/removed    | No (or label = human action)
```

*Source: gh-aw DailyOps and IssueOps documentation, cross-referenced*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claims 4–5 (no write access by default; Safe Outputs
    as permission-separated state mutation): IssueOps is a direct application of both
    principles. The AI job's `contents: read` permissions implement "no write by default";
    `add-comment` and `add-labels` in `safe-outputs:` implement the Safe Outputs write
    channel. Both sources are fully consistent; this note provides the IssueOps-specific
    instantiation.
  - `docs-ghaw-chatops.md` Claims 5–6 (`steps.sanitized.outputs.text` as safe input
    channel; filter categories — unauthorized mentions, malicious links, excessive content):
    IssueOps applies the identical sanitization mechanism to issue title+body content.
    ChatOps documents it for comment body; IssueOps extends it to issue content. Both
    sources agree on the mechanism, filter categories, and the imperative to use
    `steps.sanitized.outputs.text` rather than raw event payload fields.
  - `docs-ghaw-chatops.md` Claim 7 ("treat user-provided content as untrusted"): IssueOps
    inherits the same security mandate. Issue titles and bodies are user-provided, external
    content subject to the same prompt-injection risks as comment bodies.
  - `docs-ghaw-chatops.md` Claim 8 (agent read-only + Safe Outputs for writes, `max:`
    as volume control): IssueOps follows the same architectural pattern. The `max:`
    annotation on `add-comment` and `add-labels` is the IssueOps instantiation of the
    volume-limiting pattern first documented in the ChatOps note.
  - `docs-ghaw-dailyops.md` Claim 8 (trigger taxonomy: DailyOps / IssueOps / ChatOps /
    LabelOps): IssueOps fills the slot that DailyOps names but does not detail. Both
    sources are consistent on IssueOps = "trigger from issue creation."

- **Extends**:
  - `docs-ghaw-how-they-work.md`: That note covers Safe Outputs at the conceptual level
    ("pre-approved actions the AI can request without write permissions"). This note
    extends it with the IssueOps-specific safe-output configurations: `add-comment`
    with `target: "triggering"`, and `add-labels` with `allowed:` + `max:`. Specifically,
    `add-labels: allowed:` is a Safe Output primitive not described in `docs-ghaw-how-they-work.md`.
  - `docs-ghaw-chatops.md`: That note documents `steps.sanitized.outputs.text` for ChatOps
    slash command content. This note extends the same mechanism to IssueOps issue content —
    specifically combining title + body into one sanitized string, which ChatOps does not
    need (command body is the only input surface). The `target: "triggering"` pattern
    in `add-comment` is also an IssueOps-specific extension not covered in the ChatOps note.
  - `docs-ghaw-central-repo-ops.md` (Orchestrator+Worker multi-agent pattern): The sub-issue
    hierarchy with `temporary_id` + `parent` + `assignees: copilot` extends the Orchestrator+
    Worker concept from repo-level fan-out (CentralRepoOps) to task-level fan-out within a
    single repository. CentralRepoOps dispatches workers per repo; IssueOps sub-issues
    dispatch agents per task. Together they give two tiers of multi-agent decomposition.
  - `docs-ghaw-dailyops.md` Claim 3 (three-phase approach with approval gates): IssueOps
    sub-issue hierarchies can implement a similar multi-phase decomposition — the parent
    issue tracks the overall goal; sub-issues are the phased work items. Unlike DailyOps,
    IssueOps sub-issues are triggered by an event (issue open) rather than a schedule.

- **Contradicts**: None. The IssueOps page is fully consistent with:
  - The five-layer security model in `docs-ghaw-how-they-work.md` (IssueOps is a concrete
    instantiation of layers 3–5: permission separation, Safe Outputs, input sanitization).
  - The sanitization model in `docs-ghaw-chatops.md` (same mechanism, different content).
  - The trigger taxonomy in `docs-ghaw-dailyops.md` (IssueOps fills the named slot).
  No existing source note makes claims that conflict with the IssueOps patterns described here.
  No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **`on: issues: types: [opened]` trigger type** (Claim 1): No prior corpus source
    documents this trigger type for gh-aw. All existing trigger coverage is schedule-based
    (`docs-ghaw-dailyops.md`), human-initiated slash-command (`docs-ghaw-chatops.md`), or
    generic push/PR events. The `issues:` trigger is the first event-based, automatically-
    fired, issue-scoped trigger in the corpus.
  - **`add-labels: allowed:` for label allowlisting** (Claim 3): No prior source documents
    the `allowed:` field in Safe Outputs. This is a new write-surface bounding primitive —
    the agent cannot apply labels outside the enumerated set. Prior notes cover `max:` for
    volume limiting but not `allowed:` for categorical limiting.
  - **Sub-issue hierarchy with `temporary_id` + `parent`** (Claim 6): No prior corpus
    source documents this task-decomposition primitive. The JSON format, cross-reference
    semantics, and platform resolution behavior are entirely new to the corpus.
  - **`assignees: copilot` for parallel agent dispatch** (Claim 7): No prior source
    documents this as a mechanism for routing GitHub issues to Copilot agents. It is the
    IssueOps equivalent of `dispatch-workflow: max: 5` in CentralRepoOps — the fan-out
    trigger for parallel agent execution.
  - **`target: "triggering"` in `add-comment`** (Claim 2): Prior notes cover `target: "4750"`
    (fixed discussion number, DailyOps) but not `target: "triggering"` as an event-context
    alias. This is the IssueOps-idiomatic comment targeting pattern.
  - **Combined title+body sanitization in `steps.sanitized.outputs.text` for issue content**
    (Claim 4): ChatOps documents `steps.sanitized.outputs.text` for comment body only. The
    IssueOps extension — combining issue title AND body into one sanitized string — is new
    to the corpus. Title injection (malicious content in the issue title) is a distinct
    threat vector from comment injection; covering both in one sanitized output is a concrete
    security improvement.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add IssueOps as the "always-on triage" pattern** (Claim 8): Teams that want automatic
  issue classification, labeling, and response without human invocation should use IssueOps.
  The pitch: every issue gets an immediate AI triage response — labels applied, initial
  comment posted, sub-tasks created — within seconds of filing. Contrast with ChatOps
  (human must invoke `/triage`) and DailyOps (batch processing on a schedule). IssueOps
  is the real-time, per-event pattern.

### Chapter 02: Harness Engineering

- **Add `on: issues: types: [opened]` to the trigger taxonomy** (Claim 1): The guide's
  trigger taxonomy currently covers `slash_command` (ChatOps) and `schedule` (DailyOps).
  Add `issues: types: [opened]` as the third trigger category — automatic, event-driven,
  per-issue. The choice rule: event-driven per issue → IssueOps; human-initiated per
  comment → ChatOps; scheduled batch → DailyOps.
- **Document `add-labels: allowed:` as a required field for any label-writing IssueOps
  workflow** (Claim 3): An `add-labels` safe output without `allowed:` gives the agent
  discretion over the full label namespace, including label creation. `allowed:` is the
  mechanical constraint; always specify it. Pair with `max:` for volume control. The
  Concrete Artifacts block shows the idiomatic pattern.
- **Document `target: "triggering"` as the idiomatic `add-comment` target** (Claim 2):
  IssueOps workflows that need to respond to the triggering issue should use
  `target: "triggering"` rather than a hardcoded issue number. This makes the
  configuration portable and event-context-aware.
- **Add sub-issue hierarchy as a task-decomposition harness pattern** (Claims 6–7): For
  IssueOps workflows that manage complex requests (feature planning, bug triage with
  multiple components), the `temporary_id` + `parent` + `assignees: copilot` pattern
  enables agent-driven task breakdown. Document the JSON format and flag the need to
  bound fan-out (how many sub-issues can be created per run) analogously to CentralRepoOps
  `max:`.

### Chapter 03: Safety and Verification

- **Add label allowlisting as a Safe Outputs write-surface bound** (Claim 3): Extend
  the Ch03 Safe Outputs section with the `add-labels: allowed:` pattern. Present two
  complementary bounding mechanisms: `allowed:` (categorical — constrains *what* can be
  written) and `max:` (quantitative — constrains *how much* can be written). Both are
  required for a safe label-writing workflow in a public repository.
- **Extend the `steps.sanitized.outputs.text` mandate to issue content** (Claim 4): The
  ChatOps section should already recommend `steps.sanitized.outputs.text` over raw event
  payload fields. The IssueOps section must make the same recommendation and clarify:
  issue titles are included in the sanitized output — do not access `github.event.issue.title`
  directly. Title injection is a real attack surface for IssueOps workflows processing
  external-contributor issues.
- **Document the two-job permission-separation model as a workflow-level pattern** (Claim 5):
  The five-layer security architecture (`docs-ghaw-how-they-work.md` Claim 3) describes
  permission separation abstractly. The IssueOps two-job model is the concrete GitHub
  Actions implementation: AI job reads (no `issues: write`), write job writes (no agent
  code). Name this explicitly in Ch03 so practitioners understand it is enforced at the
  infrastructure level, not just the application level.

### Chapter 09: Agent Orchestration

- **Add sub-issue hierarchies as the task-level multi-agent decomposition pattern** (Claims 6–7):
  The corpus now has two multi-agent decomposition primitives: CentralRepoOps
  (`dispatch-workflow: max: N`) for repo-level fan-out, and IssueOps sub-issues
  (`temporary_id` + `parent` + `assignees: copilot`) for task-level fan-out. Present
  them as complementary tiers: when an issue represents a large project, IssueOps can
  break it into sub-issues and dispatch parallel agents for each task within a single
  repository, while CentralRepoOps handles cross-repository operations at org scale.

## Extraction Notes

1. **Source is a patterns page, not a comprehensive reference**: The IssueOps patterns
   page provides representative configurations and key guidance. The two-job YAML split
   (Claim 5) was described architecturally but not shown as a complete extractable YAML
   block — the page may render this via interactive diagrams or embedded components not
   captured by WebFetch. The design intent is clear; the exact YAML structure may require
   verification against the gh-aw CLI reference.

2. **Sanitization filter categories cross-validated from ChatOps note**: The
   `steps.sanitized.outputs.text` filter categories (unauthorized mentions, malicious links,
   excessive content) were corroborated from `docs-ghaw-chatops.md` Claim 6, which
   quotes the platform documentation directly. The IssueOps page references the same
   sanitization mechanism without repeating all filter details. Both sources describe
   the same platform-provided sanitization layer.

3. **Sub-issue `max:` not documented on this page**: The CentralRepoOps note documents
   `max:` for `dispatch-workflow` fan-out control. The IssueOps page does not explicitly
   document a `max:` bound on sub-issue creation or Copilot assignments. Practitioners
   should treat the absence of documented `max:` as a gap to investigate before deploying
   sub-issue workflows at scale — unbounded sub-issue creation could saturate the GitHub
   issue queue and trigger multiple simultaneous Copilot agent instances.

4. **Rendering note**: The page is an Astro/Starlight-rendered SPA. WebFetch returns
   rendered text without JavaScript execution. Two WebFetch calls were made to extract
   all YAML blocks; the content appears complete for the pattern configurations documented
   on the page. No interactive diagrams or video content is present on this page.

5. **No publication date**: The documentation page does not carry an explicit publication
   date. Content is consistent with gh-aw platform state as of 2026-05-01 (current with
   the ChatOps and DailyOps pattern pages extracted on the same date).

6. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose existing source notes at the MINER.md §4a threshold. The
   IssueOps patterns are fully consistent with the five-layer security model
   (`docs-ghaw-how-they-work.md`) and the sanitization model (`docs-ghaw-chatops.md`).
   The `add-labels: allowed:` primitive extends the Safe Outputs model without opposing it.
