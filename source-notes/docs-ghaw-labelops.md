---
source_url: https://github.github.com/gh-aw/patterns/label-ops/
source_type: docs
title: "GitHub Agentic Workflows: LabelOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#327"
---

# GitHub Agentic Workflows: LabelOps Pattern

> The authoritative reference for label-as-trigger mechanics in gh-aw — documents
> the `label_command` transient-command trigger (with auto-removal, `remove_label: false`
> persistent-state mode, multi-label syntax, and `${{ needs.activation.outputs.label_command }}`
> output for conditional branching), the `names:` filtering approach for persistent
> state monitoring, the design principle distinguishing command vs. state labels, and
> four named LabelOps patterns (Priority Escalation, Triage, Security, Release); the
> first corpus source to document these trigger mechanics at the YAML level.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Design Patterns >
  LabelOps" section — prescriptive pattern reference for label-driven workflow triggers,
  not API reference or conceptual overview. Patterns pages document proven interaction
  models for specific trigger types.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` platform.
  Claims about the `label_command` trigger schema, auto-removal behavior, `remove_label`
  semantics, and `names:` filtering are authoritative for this platform. Claims about
  generalizability of the command-vs-state design principle beyond gh-aw require
  additional evidence.
- **Scope**: The LabelOps pattern — `label_command` trigger configuration (all syntax
  forms), `remove_label` option, `${{ needs.activation.outputs.label_command }}` output,
  OR-combination with `slash_command`, `names:` filtering for `labeled`/`unlabeled`
  events, the comparison table, four named LabelOps workflow patterns, AI-powered label
  applications, and best practices. Does NOT cover: the five-layer security architecture
  (in `docs-ghaw-how-they-work.md`), the ChatOps `slash_command` trigger mechanics
  (`docs-ghaw-chatops.md`), IssueOps `on: issues:` trigger (`docs-ghaw-issueops.md`),
  DailyOps scheduling (`docs-ghaw-dailyops.md`), or MCP integration
  (`docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: `label_command` is a gh-aw trigger type that fires when a named label is applied to an issue, PR, or discussion, then automatically removes the label by default so the same label can be reapplied to re-trigger

- **Evidence**: Page core mechanics: "The `label_command` trigger treats a label
  application as a transient command. When activated, the workflow runs and the matched
  label is automatically removed by default, allowing it to be reapplied for
  re-triggering without manual cleanup."
- **Confidence**: settled (first-party documentation; the trigger type is live on the
  gh-aw platform and the auto-removal behavior is explicitly stated)
- **Quote**: "The `label_command` trigger treats a label application as a transient
  command. When activated, the workflow runs and the matched label is automatically
  removed by default, allowing it to be reapplied for re-triggering without manual
  cleanup."
- **Our assessment**: The auto-removal property is the defining characteristic. It makes
  `label_command` semantically different from any other GitHub label behavior — labels
  normally persist until manually removed. The platform consuming and removing the label
  means: (1) the trigger is stateless — label presence = current intent, never historical
  record; (2) no manual cleanup is needed to re-trigger; (3) the label event stream in
  GitHub still records every application and removal, providing a complete audit trail.
  For Ch02 (Harness Engineering): add `label_command` to the trigger taxonomy alongside
  `slash_command` (ChatOps) and `schedule` (DailyOps). This is the low-friction alternative
  to `workflow_dispatch` for human-initiated agentic actions — any user who can apply a
  label can trigger an agent, no CLI knowledge required. Extends `blog-ghaw-weekly-mar2026.md`
  Claim 3, which introduced the concept without YAML-level detail.

### Claim 2: `label_command` supports five distinct syntax forms — from a one-line shorthand to a map with event-type scoping and multiple label names

- **Evidence**: The page documents five supported configuration formats:
  ```yaml
  # Shorthand
  on: "label-command deploy"

  # Map with single label
  on:
    label_command: deploy

  # Restricted to specific event types
  on:
    label_command:
      name: deploy
      events: [issues, pull_request]

  # Multiple label names
  on:
    label_command:
      names: [deploy, redeploy]
      events: [pull_request]

  # Persistent state (no auto-removal)
  on:
    label_command:
      name: in-review
      remove_label: false
  ```
- **Confidence**: settled (first-party; all five YAML forms are explicitly shown on the page)
- **Quote**: (from YAML blocks on page)
- **Our assessment**: The five forms cover a progression from the simplest case (one
  label, any event type) to the most specific (multiple labels, specific event type,
  no removal). The `events:` field mirrors the scoping concept in the `slash_command`
  trigger (`docs-ghaw-chatops.md` Claim 2) — gh-aw provides event-type filtering as
  a first-class configuration rather than requiring manual filtering logic in the workflow.
  For Ch02: document the shorthand form for simple deployments and the full map form
  for production configurations that need event-type scoping. The `names:` plural form
  (multiple labels) enables a single workflow to handle related label commands (e.g.,
  `deploy` and `redeploy`) without duplicating workflow definitions.

### Claim 3: `remove_label: false` converts `label_command` from a transient command into a persistent state marker — the workflow fires but the label remains attached

- **Evidence**: Directly documented: "This boolean field (default: `true`) controls
  whether the matched label persists after workflow activation. Setting it to `false`
  designates the label as representing ongoing state rather than a consumable command —
  useful for marking items currently under processing."
- **Confidence**: settled (first-party; the option and its semantic are explicitly stated)
- **Quote**: "Setting it to `false` designates the label as representing ongoing state
  rather than a consumable command — useful for marking items currently under processing."
- **Our assessment**: `remove_label: false` is the bridge between `label_command` and
  `names:` filtering. A label with `remove_label: false` fires the workflow AND stays
  attached — making it simultaneously a trigger and a state indicator. The "currently
  under processing" example is the canonical use case: when a workflow is actively
  working on an item, the persistent label visually signals that to humans browsing the
  issue or PR. Without `remove_label: false`, the label disappears as soon as the
  workflow starts, giving no visible indication that work is in progress. For Ch02: name
  this as the "processing indicator" pattern — apply a `label_command` with
  `remove_label: false` to mark work as in-flight; have the workflow remove the label
  itself (via a safe-output) when it completes.

### Claim 4: The triggering label name is exposed via `${{ needs.activation.outputs.label_command }}`, enabling a single workflow to branch on which of multiple labels fired it

- **Evidence**: Page documents the output variable: "`${{ needs.activation.outputs.label_command }}`
  — This supports workflows handling multiple label commands that need conditional
  branching logic."
- **Confidence**: settled (first-party; the output variable path is explicitly stated)
- **Quote**: "This supports workflows handling multiple label commands that need
  conditional branching logic."
- **Our assessment**: When a workflow is configured to respond to multiple labels (e.g.,
  `names: [deploy, redeploy, rollback]`), the agent needs to know which label actually
  fired to take the appropriate action. The `label_command` output provides that
  information. This is analogous to `${{ github.event.inputs.* }}` in `workflow_dispatch`
  — the platform injects the trigger context so the agent doesn't have to reverse-engineer
  it. For Ch02: document this output variable alongside the `names:` multi-label syntax
  as a required pair — if you configure multiple label names, you need `label_command`
  output to branch on them. Without it, the workflow cannot distinguish which label fired.

### Claim 5: `label_command` and `slash_command` can coexist in the same workflow definition using OR logic, unifying agent behavior across label-triggered and comment-triggered invocations

- **Evidence**: Page states: "`label_command` and `slash_command:` can coexist in the
  same workflow definition using OR logic. The workflow activates when either trigger
  condition is satisfied, enabling unified agent logic across multiple invocation methods."
- **Confidence**: settled (first-party; the OR combination is explicitly documented)
- **Quote**: "enabling unified agent logic across multiple invocation methods"
- **Our assessment**: This is the most powerful harness ergonomic in the LabelOps page.
  Rather than maintaining two parallel workflows (one label-triggered, one slash-command-
  triggered) that implement the same agent logic, a single workflow can respond to either
  trigger. The practical impact: a team can offer both a label-based UI (for users who
  prefer labels) and a slash-command UI (for users who prefer commands) without any
  additional workflow maintenance. For Ch02: name this as the "multi-path trigger"
  pattern — combine `label_command` + `slash_command` in one workflow to support
  both interaction styles simultaneously. Extends `docs-ghaw-chatops.md` Claim 1
  (`slash_command` mechanics) and `docs-ghaw-issueops.md` Claim 8 (trigger taxonomy)
  by adding the OR-composition capability.

### Claim 6: `names:` filtering on `labeled`/`unlabeled` events provides a distinct label-trigger mechanism where labels remain attached — suited to state monitoring rather than transient commands

- **Evidence**: Page documents the `names:` filtering approach:
  ```yaml
  on:
    issues:
      types: [labeled]
      names: [bug, critical, security]
  ```
  "This approach suits monitoring label state where labels should remain attached after
  workflow execution." The page notes it is compiled into conditional `if` expressions
  in the final YAML.
- **Confidence**: settled (first-party; the syntax and semantic are explicitly stated)
- **Quote**: "This approach suits monitoring label state where labels should remain
  attached after workflow execution."
- **Our assessment**: The `names:` approach is the correct choice when a label represents
  ongoing status (e.g., "bug" labels that should remain visible on the issue) rather than
  a one-shot action. It also supports `unlabeled` events — workflows can trigger when a
  label is removed, useful for escalation/de-escalation patterns (e.g., when a
  "reviewed" label is removed, flag for re-review). The compilation into `if` expressions
  means the underlying GitHub Actions YAML is still standard `labeled` event logic; gh-aw
  provides the ergonomic `names:` abstraction on top. For Ch02: add `names:` filtering
  to the trigger taxonomy. It shares the `on: issues:` or `on: pull_request:` base event
  type with IssueOps but differs in its label-scoping semantics.

### Claim 7: The design principle for choosing between `label_command` and `names:` filtering is explicit — use `label_command` when the label means "do this now" (transient command), use `names:` when the label represents an ongoing property (persistent state)

- **Evidence**: Comparison table from the page:
  | Aspect | label_command | names: filtering |
  |--------|---------------|-----------------|
  | **Label lifecycle** | Auto-removed after trigger | Remains persistent |
  | **Re-triggering** | Reapply the label | Only on next labeled event |
  | **Typical use case** | Transient "do this now" commands | State-based routing and monitoring |
  | **Supported item types** | Issues, PRs, discussions | Issues, pull requests |
- **Confidence**: settled (first-party; the table and framing are explicitly stated in
  the documentation)
- **Quote**: (from comparison table; the "transient command" vs. "state-based routing and
  monitoring" framing is the key design distinction)
- **Our assessment**: This is the most actionable finding in the source. A concrete
  trigger-design heuristic: if the label represents an action to take right now (deploy,
  review, approve), use `label_command` and let the platform remove it. If the label
  represents an ongoing property of the issue or PR (bug, blocked, in-review), use
  `names:` filtering and let the label persist. The distinction is load-bearing for
  designing human-in-the-loop controls — the wrong choice produces a label that either
  disappears when you expect it to stay, or accumulates when you expect it to be cleared.
  For Ch02: include this heuristic explicitly in the trigger decision guide alongside the
  existing IssueOps / ChatOps / DailyOps guidance.

### Claim 8: The page names four concrete LabelOps workflow patterns — Priority Escalation, Label-Based Triage, Security Automation, and Release Management

- **Evidence**: "Common LabelOps Patterns" section: "Priority Escalation: Apply `P0`,
  `critical`, or `urgent` labels; agent analyzes severity and provides SLA guidance.
  Label-Based Triage: Use `needs-triage` or `triaged` labels to suggest categorization,
  priority assignments, and affected components. Security Automation: Security-designated
  labels trigger disclosure risk checks and review process initiation. Release Management:
  Release labels activate analysis of timelines, blocker identification, and release notes
  drafting."
- **Confidence**: anecdotal (first-party named patterns; no metrics or success rates
  provided for any of the four)
- **Quote**: "Priority Escalation: Apply P0, critical, or urgent labels; agent analyzes
  severity and provides SLA guidance."
- **Our assessment**: The four patterns share a common structure: a human (or automation)
  applies a meaningful label → a gh-aw workflow reads the label as a trigger → the agent
  executes a specific task suited to that label's semantics. This is LabelOps as a
  human-readable dispatch system — label names are the API. The Security Automation
  pattern is particularly notable: security-designated labels can trigger automated
  disclosure risk checks without requiring any developer to invoke a command, creating
  a continuous security layer triggered by human triage decisions. For Ch01 (Daily
  Workflows): these four patterns are good starting points for teams building their first
  LabelOps workflows. The Release Management pattern complements `blog-gh-aw-operations-
  release-workflows.md`'s Changeset Generator — labels could trigger the release
  workflow rather than requiring a manual `gh aw run`.

### Claim 9: AI-powered LabelOps supports three automated label management applications — Automatic Label Suggestions, Component Auto-Labeling, and Label Consolidation Audits

- **Evidence**: "AI-Powered LabelOps Applications" section: "Automatic Label Suggestions:
  Analyze items and apply labels for type, priority, and component using
  `safe-outputs.add-labels.allowed` for security restrictions. Component Auto-Labeling:
  Extract affected components from file paths and system references, then apply matching
  labels. Label Consolidation Audits: Scheduled workflows identify duplicate, unused, or
  inconsistently named labels."
- **Confidence**: anecdotal (first-party named applications; no metrics or examples
  provided)
- **Quote**: "Automatic Label Suggestions: Analyze items and apply labels for type,
  priority, and component using `safe-outputs.add-labels.allowed` for security
  restrictions."
- **Our assessment**: The Label Consolidation Audit is the most novel of the three —
  using a scheduled gh-aw workflow (DailyOps-style) to audit the label namespace itself
  for hygiene issues. Label sprawl (dozens of near-duplicate labels like "bug", "Bug",
  "BUGS", "defect") is a real problem in mature repositories, and automated consolidation
  audits address it without developer intervention. The reference to `safe-outputs.
  add-labels.allowed` for Automatic Label Suggestions is notable — it confirms that even
  AI-generated label suggestions must go through the Safe Outputs allowlist, not
  unrestricted label creation. For Ch01: Label Consolidation Audits are a concrete
  example of DailyOps applied to repository hygiene rather than code quality.

### Claim 10: LabelOps best practices include specific hyphenated label names, semantic documentation in LABELS.md or GitHub label descriptions, opt-in automation labels, and Safe Outputs for all write operations

- **Evidence**: Best practices section: "Employ specific, hyphenated label names
  (`ready-for-review` rather than `ready`) to minimize unintended triggers. Document
  label semantics in repository files like LABELS.md or GitHub's label description field.
  Restrict automation scope using opt-in labels such as `automation-enabled`. Employ safe
  outputs for all write operations to maintain security posture."
- **Confidence**: emerging (first-party opinions; these are design recommendations, not
  platform-enforced constraints)
- **Quote**: "Employ specific, hyphenated label names (ready-for-review rather than
  ready) to minimize unintended triggers."
- **Our assessment**: The "minimize unintended triggers" rationale for specific names is
  important — a generic label like "ready" might be applied in contexts unrelated to the
  target workflow, causing spurious activations. The opt-in label pattern (`automation-
  enabled`) is a conservative default for new LabelOps deployments: only items that have
  been explicitly opted in will receive automated label handling. This prevents automated
  workflows from processing legacy items or items that maintainers want to handle manually.
  For Ch02: include the opt-in label pattern as a recommended rollout strategy for new
  LabelOps workflows — deploy automation conservatively before expanding scope.

## Concrete Artifacts

### `label_command` Configuration — All Supported Syntax Forms

```yaml
# Shorthand (simplest — single label, any event type)
on: "label-command deploy"

# Map with single label (explicit)
on:
  label_command: deploy

# Restricted to specific event types
on:
  label_command:
    name: deploy
    events: [issues, pull_request]

# Multiple label names (requires label_command output for branching)
on:
  label_command:
    names: [deploy, redeploy]
    events: [pull_request]

# Persistent state marker (label remains after workflow fires)
on:
  label_command:
    name: in-review
    remove_label: false
```

*Source: gh-aw LabelOps patterns documentation, "Label Command Trigger" section*

### Accessing the Triggering Label in a Multi-Label Workflow

```yaml
# In the workflow's natural language instruction body:
# Use ${{ needs.activation.outputs.label_command }} to know which label fired.

# Example branching logic (expressed in natural language):
# "If the triggering label is 'deploy', build and deploy a preview environment.
#  If the triggering label is 'redeploy', run only the deployment step.
#  Post the deployment URL as a comment when complete."
```

*Source: gh-aw LabelOps patterns documentation, "Accessing Matched Labels" section*

### `label_command` OR `slash_command` — Unified Trigger Definition

```yaml
# Workflow activated by EITHER a label application OR a slash command:
on:
  label_command: deploy
  slash_command: deploy
permissions:
  contents: read
safe-outputs:
  add-comment:
    max: 1
```

*Source: gh-aw LabelOps patterns documentation, "Integration with Slash Commands" section*

### `names:` Label Filtering — State Monitoring (Label Persists)

```yaml
on:
  issues:
    types: [labeled]
    names: [bug, critical, security]
```

*Source: gh-aw LabelOps patterns documentation, "Label Filtering via `names:`" section*

### Design Choice Comparison Table

```
Aspect              | label_command              | names: filtering
--------------------|----------------------------|----------------------------------
Label lifecycle     | Auto-removed after trigger | Remains persistent (attached)
Re-triggering       | Reapply the label          | Only on next labeled event
Typical use case    | "Do this now" commands     | State-based routing / monitoring
Supported items     | Issues, PRs, discussions   | Issues, pull requests
Design principle    | Transient command          | Persistent state marker
```

*Source: gh-aw LabelOps patterns documentation, "Comparison" section*

### Complete Workflow Example (Deploy Preview)

```yaml
---
on:
  label_command: deploy
permissions:
  contents: read
safe-outputs:
  add-comment:
    max: 1
---
# Deploy Preview
A `deploy` label triggers this workflow. Build and deploy a preview environment,
then post the resulting URL as a comment.
```

After activation, the label is automatically removed, allowing reapplication without
intervention.

*Source: gh-aw LabelOps patterns documentation, "Workflow Example" section*

### LabelOps Best Practices Reference

```
1. Name specificity:  Use hyphenated names ("ready-for-review" not "ready") to avoid
                      spurious triggers from label reuse in unrelated contexts.

2. Semantic docs:     Document label meanings in LABELS.md or GitHub label descriptions.
                      LabelOps effectiveness depends on humans applying labels with
                      consistent intent.

3. Opt-in scope:      Use an "automation-enabled" opt-in label to restrict which items
                      receive automated label handling. Conservative default for rollout.

4. Safe outputs:      All write operations (applying labels, posting comments) must use
                      safe-outputs. LabelOps workflows are not exempt from the "no direct
                      write access" model.
```

*Source: gh-aw LabelOps patterns documentation, "Best Practices" section*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-mar2026.md` Claim 3 (Label Command Trigger as a workflow activation
    primitive — "Activate workflows by adding labels; automatically removed for
    reapplication"): that note introduced the concept at a changelog level. This note
    corroborates the conceptual claim and extends it with the complete YAML syntax, all
    configuration options, and the design principle framing. Both sources agree: auto-
    removal + reapplication is the defining property of `label_command`. Together they
    give the historical context (when it shipped, v0.59.0) and the design reference
    (how to configure it).
  - `docs-ghaw-how-they-work.md` Claims 4–5 (no write access by default; Safe Outputs
    as permission-separated state mutation): the LabelOps best practice "employ safe
    outputs for all write operations" is a direct instantiation of these principles.
    LabelOps AI-powered applications that apply labels must use `safe-outputs.add-labels.
    allowed` (Claim 9), consistent with `docs-ghaw-issueops.md` Claim 3 which documents
    the same `allowed:` field for IssueOps label application.
  - `docs-ghaw-chatops.md` Claim 1 (`slash_command` trigger mechanics): this note's
    Claim 5 (OR-combination of `label_command` + `slash_command`) builds directly on
    the `slash_command` trigger documented in the ChatOps note. Both trigger types can
    coexist in a single workflow — a fact neither note alone establishes without the other.
  - `docs-ghaw-issueops.md` Claim 8 (four-trigger taxonomy: DailyOps / IssueOps /
    ChatOps / LabelOps): that note names LabelOps as the fourth trigger category but
    provides no detail about its mechanics. This note fills that gap, completing the
    four-trigger taxonomy with the concrete YAML reference for LabelOps.

- **Extends**:
  - `blog-ghaw-weekly-mar2026.md` Claim 3 (Label Command Trigger introduced in v0.59.0):
    this note extends the changelog entry into a full pattern reference. The five YAML
    syntax forms, `remove_label: false`, multi-label naming, `label_command` output
    variable, and OR-combination with `slash_command` are all absent from the weekly
    update. This note adds everything needed for practitioners to actually implement
    `label_command` workflows.
  - `docs-ghaw-issueops.md` (IssueOps trigger taxonomy and Safe Outputs): the `names:`
    filtering approach (Claim 6) shares the `on: issues: types: [labeled]` event base
    with IssueOps but adds label-name scoping that IssueOps does not document. Together,
    `docs-ghaw-issueops.md` and this note give a complete picture of issue-triggered
    automation: open-event triggers (IssueOps) and label-event triggers (LabelOps).
  - `docs-ghaw-chatops.md` (ChatOps trigger): the OR-combination of `label_command` +
    `slash_command` (Claim 5) extends the ChatOps trigger by making it one of two paths
    into the same workflow, not a standalone trigger. The "multi-path trigger" pattern
    is new to the corpus.
  - `docs-ghaw-github-actions-primer.md` (trigger architecture): that note mentions
    triggers at the architectural level. This note adds a concrete new trigger type
    (`label_command`) that the primer does not document.

- **Contradicts**: None. No existing source note claims that flat (non-tiered) label
  triggers are preferable, or that labels should not be used as workflow activation
  signals. The `label_command` semantics (auto-removal) are consistent with how
  `blog-ghaw-weekly-mar2026.md` Claim 3 described the feature at introduction. No
  contradiction issue filed.

- **Novel** (what this note adds to the corpus):
  - **Complete `label_command` YAML syntax** (Claim 2): Five configuration forms,
    none documented in any prior corpus source at the YAML level. Prior coverage
    (`blog-ghaw-weekly-mar2026.md` Claim 3) was conceptual only.
  - **`remove_label: false` persistent-state mode** (Claim 3): Not documented in any
    existing source note. The "currently processing" marker pattern this enables is
    new to the corpus.
  - **`${{ needs.activation.outputs.label_command }}` output variable** (Claim 4):
    Not documented in any existing source note. Required for multi-label conditional
    branching; without it, multi-label `label_command` workflows cannot distinguish
    which label fired.
  - **`label_command` OR `slash_command` combination** (Claim 5): Not documented in
    any existing source note. The "multi-path trigger" pattern — same agent logic
    reachable by label or command — is new to the corpus.
  - **`names:` filtering for `labeled`/`unlabeled` events** (Claim 6): Not documented
    in any existing corpus source. The persistent-label monitoring approach is
    semantically distinct from `label_command` and fills the "state routing" use case.
  - **Command vs. state design principle** (Claim 7): The explicit heuristic — transient
    command → `label_command`, persistent state → `names:` filtering — is the first
    trigger-design principle in the corpus stated at this level of specificity for label
    triggers. Prior notes document when to use ChatOps vs. DailyOps vs. IssueOps, but
    not the intra-label trigger choice.
  - **Four named LabelOps patterns** (Claim 8): Priority Escalation, Label-Based Triage,
    Security Automation, Release Management — none of these named patterns appear in
    any existing source note.
  - **Label Consolidation Audit as a DailyOps application** (Claim 9): No prior source
    documents automated label hygiene as a scheduled agentic workflow.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Trigger Taxonomy**: Add `label_command` and
  `names:` filtering as the two LabelOps trigger mechanisms, completing the four-trigger
  taxonomy (DailyOps / IssueOps / ChatOps / LabelOps) with concrete YAML references
  for all four. Add the command-vs-state design heuristic (Claim 7) as the decision
  rule for choosing between the two. Current trigger guidance covers only `slash_command`
  and `schedule`; this note fills the label-trigger gap.

- **Chapter 02 (Harness Engineering) — Multi-Path Trigger Pattern**: Add the
  `label_command` OR `slash_command` combination as a named pattern for workflows that
  should be reachable via multiple interaction surfaces. Document the YAML form (Claim 5
  Concrete Artifact) and the benefit: one workflow definition, two invocation paths,
  zero duplication of agent logic.

- **Chapter 02 (Harness Engineering) — Processing Indicator Pattern**: Document
  `remove_label: false` as the pattern for marking work as in-flight during processing
  (Claim 3). The workflow applies a persistent label to signal "being processed," then
  removes it via a safe-output on completion. This gives humans visual feedback without
  manual state management.

- **Chapter 01 (Daily Workflows) — LabelOps Starter Patterns**: Cite the four named
  patterns (Claim 8) as concrete starting points for teams building their first LabelOps
  workflows: Priority Escalation for SLA enforcement, Label-Based Triage for issue
  management, Security Automation for disclosure workflows, Release Management for
  release coordination. Pair with `blog-gh-aw-operations-release-workflows.md` for the
  Release Management pattern — labels could activate the Changeset Generator workflow
  rather than requiring a manual command.

- **Chapter 03 (Safety and Verification) — LabelOps Safe Outputs Mandate**: Add the
  `safe-outputs.add-labels.allowed` requirement to the Safe Outputs section (Claim 9
  and best practices). LabelOps AI-powered label suggestions must go through the
  allowlist — the agent cannot create new labels or apply labels outside the enumerated
  set. Cross-reference with `docs-ghaw-issueops.md` Claim 3, which documents the same
  `allowed:` primitive for IssueOps.

- **Chapter 01 (Daily Workflows) — Label Hygiene**: Add Label Consolidation Audits as
  an example of DailyOps applied to repository hygiene (Claim 9). Scheduled workflows
  that audit the label namespace for duplicates and unused labels are a concrete always-on
  pattern with no code-change risk.

## Extraction Notes

1. **Source is a patterns page, not a comprehensive reference**: The LabelOps patterns
   page is prescriptive (configuration examples and design patterns) rather than
   exhaustive (complete API reference). Some configuration details (e.g., whether
   `names:` filtering supports `discussion` events) are not documented on the page.
   Practitioners should consult the gh-aw CLI reference for edge cases.

2. **Prospector-identified detail confirmed by source**: The Prospector's triage comment
   mentioned that the compiler generates a `workflow_dispatch` trigger with `item_number`
   input for manual testing. This was not directly present in the fetched page content
   and is therefore not extracted as a claim in this note. The compiler-generated test
   trigger is documented in the broader gh-aw compilation model
   (`docs-ghaw-how-they-work.md`); practitioners should rely on that source for
   compilation behavior.

3. **No publication date**: The documentation page does not carry an explicit publication
   date. Content is consistent with gh-aw platform state as of 2026-05-01, and with
   the `label_command` feature introduced in v0.59.0 (March 2026) as documented in
   `blog-ghaw-weekly-mar2026.md`.

4. **Rendering note**: The page is an Astro/Starlight-rendered SPA. WebFetch returns
   rendered text without JavaScript execution. The page content appears complete for
   the pattern configurations documented; no interactive diagrams or video content
   was present. The comparison table was captured from the rendered markdown.

5. **No contradictions filed**: Reviewed all existing source notes against the claims
   in this source. No claim in this source materially opposes any existing source note.
   The `label_command` semantics extend rather than contradict `blog-ghaw-weekly-mar2026.md`
   Claim 3. The `names:` filtering approach extends rather than contradicts the trigger
   taxonomy in `docs-ghaw-issueops.md` and `docs-ghaw-dailyops.md`.
