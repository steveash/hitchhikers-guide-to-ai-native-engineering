---
source_url: https://github.github.com/gh-aw/patterns/task-ops
source_type: docs
title: "GitHub Agentic Workflows: TaskOps / ResearchPlanAssignOps Pattern (URL alias)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#354"
---

# GitHub Agentic Workflows: TaskOps / ResearchPlanAssignOps Pattern (URL alias)

> Confirms the TaskOps URL (`patterns/task-ops`) is a permanent redirect to
> `patterns/research-plan-assign-ops`, resolving the naming ambiguity noted in
> `docs-ghaw-workqueue-ops.md` and `docs-ghaw-research-plan-assign-ops.md`;
> extracts the full YAML configuration for the three safe-output phases (create-
> discussion with `expires`/`category`/`close-older-discussions`, plan create-issue
> with `expires`/`title-prefix`, assign create-issue with `title-prefix`) and the
> negative selection criteria not captured in the primary extraction.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/task-ops` page — URL
  in the same `patterns/` section as `patterns/research-plan-assign-ops`,
  `patterns/workqueue-ops`, and others. The page redirects permanently to
  `patterns/research-plan-assign-ops/`, confirming the two URLs reference the same
  pattern. This note exists to close the naming discrepancy and to capture
  incremental YAML configuration and selection criteria not in the primary
  extraction at `docs-ghaw-research-plan-assign-ops.md`.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw`
  CLI. YAML configuration fields and pattern selection criteria are authoritative
  for the `gh aw` platform.
- **Scope**: Covers the URL alias relationship (task-ops = research-plan-assign-ops),
  the complete set of phase-specific safe-output YAML configurations (including
  `expires`, `title-prefix`, `category`, `close-older-discussions` fields not
  captured in the primary extraction), the negative selection criteria for when NOT
  to use the pattern, and the Related Patterns section. Does NOT re-extract the
  four-phase structure, human gate model, sub-issue content requirements, or
  go-fan reference details — those are fully covered in
  `docs-ghaw-research-plan-assign-ops.md`.

## Extracted Claims

### Claim 1: The `patterns/task-ops` URL is a permanent redirect to `patterns/research-plan-assign-ops`, confirming TaskOps and ResearchPlanAssignOps are the same named pattern

- **Evidence**: Direct WebFetch of `https://github.github.com/gh-aw/patterns/task-ops`
  returns only a redirect notice with no substantive content of its own.
- **Confidence**: settled (redirect is explicit and deterministic; confirmed across
  multiple fetch attempts)
- **Quote**: "Redirecting from `/gh-aw/patterns/task-ops/` to `/gh-aw/patterns/research-plan-assign-ops/`"
- **Our assessment**: This closes the naming ambiguity logged as a question in two
  existing source notes. `docs-ghaw-workqueue-ops.md` Claim 11 cited the URL
  `patterns/task-ops` with the description "Research → Plan → Assign pattern";
  `docs-ghaw-research-plan-assign-ops.md` Extraction Note 2 suspected the two URLs
  might be aliases. The redirect confirms they are the same pattern. The
  WorkQueueOps note's characterization of the pattern as three phases
  (Research → Plan → Assign) reflects the prior name; the current page names four
  phases (Research → Plan → Assign → Merge). TaskOps is the legacy name; the
  canonical current name is ResearchPlanAssignOps.

### Claim 2: The Research phase uses `create-discussion` with `expires: 1d`, `category: "research"`, `max: 1`, and `close-older-discussions: true` — limiting the live artifact to one current discussion per research cycle

- **Evidence**: YAML configuration block from the current research-plan-assign-ops
  page, consistently extracted across multiple fetch passes.
- **Confidence**: settled (first-party YAML config block; consistent with
  `expires:`/`close-older-discussions:` semantics documented in
  `docs-ghaw-ephemerals.md` Claim 3 and `docs-ghaw-dataops.md` Claim 7)
- **Quote**: (no direct quote; see Concrete Artifacts → Research Phase Configuration)
- **Our assessment**: The combination of `max: 1` and `close-older-discussions: true`
  implements a "single live research Discussion" discipline — each new research run
  automatically closes the prior one, preventing accumulation of stale findings.
  The `expires: 1d` adds a time-bound: if the research Discussion is not acted on
  within one day, it closes automatically. The `category: "research"` namespaces
  the Discussion under the repository's research category, enabling filtered views
  of research artifacts separately from other Discussion types. This configuration
  trio (`max: 1` + `close-older-discussions: true` + `expires: 1d`) is the
  production-hardened variant of the "living report" pattern documented in
  `docs-ghaw-dataops.md` Claim 7 — applied to research findings rather than
  data reports. For Ch02: document this as the canonical Research-phase Discussion
  configuration for any scheduled research workflow.

### Claim 3: The Plan phase `create-issue` safe-output includes `expires: 2d` and `title-prefix: "[plan] "` alongside the previously documented `group: true`, `max: 5`, `labels: [plan, ai-generated]`

- **Evidence**: YAML configuration block from the current research-plan-assign-ops
  page.
- **Confidence**: settled (first-party YAML config block)
- **Quote**: (no direct quote; see Concrete Artifacts → Plan Phase Configuration)
- **Our assessment**: The `expires: 2d` field means planned issues that are not
  acted on within two days auto-close — preventing accumulation of stale planning
  artifacts if the developer does not proceed to the Assign phase. The
  `title-prefix: "[plan] "` makes plan-phase issues visually distinct in the issue
  tracker and searchable independently. Combined with `labels: [plan, ai-generated]`,
  the plan output carries three independent traceability signals: title prefix
  (visual), labels (filterable), and issue-hierarchy (via `group: true` parent).
  The `expires: 2d` is notably shorter than the `expires: 7` (7-day) example in
  `docs-ghaw-ephemerals.md` Claim 3 — it enforces a tight human-decision window
  between planning and assignment. For Ch02: add `expires: 2d` to the Plan phase
  configuration as a default time-bound for planning artifacts.

### Claim 4: The Assign phase `create-issue` safe-output includes `title-prefix: "[fix] "` and `labels: [ai-generated]` with `assignees: copilot`, completing a three-tier title-prefix chain from research to implementation

- **Evidence**: YAML configuration block from the current research-plan-assign-ops
  page.
- **Confidence**: settled (first-party YAML config block)
- **Quote**: (no direct quote; see Concrete Artifacts → Assign Phase Configuration)
- **Our assessment**: The three title prefixes — `[go-fan]` (research Discussion),
  `[plan]` (planning issue), `[fix]` (implementation issue) — form a chain that
  tracks the provenance of every artifact back to its research origin. A developer
  looking at a `[fix]` PR can trace it to its `[plan]` issue and from there to the
  `[go-fan]` research Discussion. This is a naming-convention approach to
  cross-artifact traceability, complementing the structural link provided by
  `group: true` in the Plan phase. The `labels: [ai-generated]` on assign-phase
  issues (distinct from `[plan, ai-generated]` on plan-phase issues) allows
  filtering specifically for implementation-ready AI-generated work items.
  For Ch02: recommend the title-prefix chain as a traceability convention for
  multi-phase workflows — even teams not using ResearchPlanAssignOps can apply
  the same pattern to any workflow that produces artifacts across multiple phases.

### Claim 5: The pattern's negative selection criteria name three alternatives: IssueOps when work is already defined, the `assignees: copilot` shortcut when issues can bypass review, and MultiRepoOps when work spans multiple repositories

- **Evidence**: "When NOT to use" section from the current page, extracted
  verbatim across fetch passes.
- **Confidence**: settled (first-party; explicit negative criteria with named
  alternatives)
- **Quote**: "Prefer a simpler pattern when: The work is already well-defined
  (use IssueOps), Issues can go directly to Copilot without review (use the
  assignees: copilot shortcut), Work spans multiple repositories (use MultiRepoOps)."
- **Our assessment**: The three negative criteria complete the selection decision
  for this pattern. The existing `docs-ghaw-research-plan-assign-ops.md`
  documents the positive conditions (unknown scope, human prioritization needed,
  variable quality); this note adds the negative conditions that explicitly redirect
  to alternative patterns. The "assignees: copilot shortcut" negative criterion is
  noteworthy: if the developer trusts the research quality enough to bypass the
  Plan phase entirely, the shortcut (`safe-outputs.create-issue.assignees: copilot`
  in the research workflow directly) is the recommended simplification — not a
  stripped-down version of ResearchPlanAssignOps. For Ch04: the three negative
  criteria should be presented alongside the positive conditions in the pattern
  selection guide, giving practitioners a complete decision rubric.

### Claim 6: ResearchPlanAssignOps applies additionally when "research findings vary in quality (some runs find nothing actionable)" and "multiple work items can be executed in parallel"

- **Evidence**: Extended "When to use" section from the current page, extracted
  across fetch passes. The primary extraction (issue #351) captured the core
  three conditions; the current page shows at least two additional conditions.
- **Confidence**: settled (first-party; stated as explicit applicability conditions)
- **Quote**: "Research findings vary in quality (some runs find nothing actionable)"
- **Our assessment**: The "some runs find nothing actionable" qualification is
  honest about the AI research quality problem: a well-designed research workflow
  does not always return significant findings, and the human Plan gate is the
  filter for those empty runs. The "multiple work items can be executed in
  parallel" condition clarifies that ResearchPlanAssignOps is not just for
  single-fix scenarios — the Assign phase is designed for parallel Copilot
  execution of multiple sub-issues. For Ch04: add these two conditions to the
  existing positive-criteria list in the pattern selection guide.

### Claim 7: The go-fan workflow illustrates both the `category: "research"` and `close-older-discussions: true` configuration in practice — creating a `[go-fan]` discussion under the `audits` category each weekday

- **Evidence**: Phase 1 description on the current page, consistently extracted.
- **Confidence**: settled (first-party; concrete named workflow with specific
  schedule and output category)
- **Quote**: "it runs each weekday, picks one Go dependency, compares current
  usage against upstream best practices, and creates a `[go-fan]` discussion
  under the `audits` category."
- **Our assessment**: The `audits` category in go-fan maps to the `category:
  "research"` config in the Research phase YAML (Claim 2). The `[go-fan]` title
  prefix on the Discussion is the research-phase equivalent of the `[plan]` and
  `[fix]` prefixes in subsequent phases — completing the three-tier naming chain.
  The "picks one Go dependency" scoping is consistent with the `max: 1` Discussion
  config — one dependency investigated, one Discussion created, older one closed.
  For Ch02: use the go-fan → `audits` category relationship as the concrete example
  of `category: "research"` configuration.

### Claim 8: The Related Patterns section names DispatchOps (manually triggered research), WorkQueueOps (sequential queue processing), Safe Outputs, and Assign to Copilot as the four complementary patterns

- **Evidence**: Related Patterns section extracted from the current page.
- **Confidence**: settled (first-party; explicitly listed)
- **Quote**: (no single verbatim sentence; derived from the listed pattern names
  and their descriptions: "DispatchOps — Manually triggered research and
  investigations", "WorkQueueOps — Sequential queue processing for backlogs",
  "Safe Outputs — Secure write operations", "Assign to Copilot — Assigning issues
  to GitHub Copilot")
- **Our assessment**: The DispatchOps relationship is architecturally significant.
  DispatchOps is described as "manually triggered research" in this section — the
  same research agent role as ResearchPlanAssignOps Phase 1, but dispatched by a
  developer on demand rather than on a schedule. This positions the two patterns as
  scheduled vs. on-demand variants of the same research-first architecture, with
  identical Plan and Assign phases. The WorkQueueOps relationship is the
  TaskOps → WorkQueueOps pipeline documented in `docs-ghaw-workqueue-ops.md` Claim
  11: ResearchPlanAssignOps generates sub-issues; WorkQueueOps provides the queue-
  consumption layer for processing them at scale. For Ch04: add DispatchOps as the
  "on-demand research" sibling of ResearchPlanAssignOps — use ResearchPlanAssignOps
  for recurring scheduled investigation and DispatchOps for ad-hoc investigations.

## Concrete Artifacts

### Research Phase Configuration (complete with all fields)

```yaml
# Research phase — safe-output for Discussion creation
safe-outputs:
  create-discussion:
    expires: 1d
    category: "research"
    max: 1
    close-older-discussions: true
```

- `expires: 1d`: Discussion auto-closes after 1 day if not acted on
- `category: "research"`: Namespaces the Discussion to the research category (go-fan uses `audits`)
- `max: 1`: Only one research Discussion exists at a time
- `close-older-discussions: true`: Previous research Discussion is closed on each run

*Source: `patterns/research-plan-assign-ops` (redirect destination of `patterns/task-ops`), Research phase configuration section*

### Plan Phase Configuration (complete with all fields)

```yaml
# Plan phase — safe-output for grouped issue creation
safe-outputs:
  create-issue:
    expires: 2d
    title-prefix: "[plan] "
    labels: [plan, ai-generated]
    max: 5
    group: true
```

- `expires: 2d`: Planned issues auto-close after 2 days if not assigned
- `title-prefix: "[plan] "`: Visual identifier for plan-phase issues in the tracker
- `labels: [plan, ai-generated]`: Dual-label for searchability and AI provenance
- `max: 5`: Cap on issues per planning run
- `group: true`: Creates one parent tracking issue with sub-issues

*Source: `patterns/research-plan-assign-ops`, Plan phase configuration section*

### Assign Phase Configuration (complete with all fields)

```yaml
# Assign phase — safe-output for implementation issue creation
safe-outputs:
  create-issue:
    title-prefix: "[fix] "
    labels: [ai-generated]
    assignees: copilot
```

- `title-prefix: "[fix] "`: Visual identifier for implementation-ready issues
- `labels: [ai-generated]`: AI provenance label (without `plan` label — distinct from plan phase)
- `assignees: copilot`: Routes issues to Copilot at creation time (auto-assign mode)

*Source: `patterns/research-plan-assign-ops`, Assign phase configuration section*

### Title-Prefix Chain — Cross-Phase Traceability Convention

```
Research phase:  [go-fan]  Discussion — research findings, category: "research" (or "audits")
Plan phase:      [plan]    Issue      — concrete work items, grouped under parent
Assign phase:    [fix]     Issue      — implementation-ready items, assigned to Copilot

Traceability chain:
  developer reads "[go-fan]" Discussion
    → invokes /plan → "[plan] " issues created (grouped under tracking issue)
    → developer assigns → "[fix] " issues created and routed to Copilot
    → Copilot opens PR → human maintainer reviews and merges

Each prefix is a searchable handle:
  gh issue list --label plan --label ai-generated    → all current plan items
  gh issue list --label ai-generated -S open         → all pending Copilot items
  gh search discussions --category research          → all research artifacts
```

*Source: `patterns/research-plan-assign-ops`, derived from phase-specific YAML blocks and go-fan description*

### Pattern Selection Decision (Positive + Negative Criteria)

```
USE ResearchPlanAssignOps when:
  ✓ The scope of work is unknown until analysis runs
  ✓ Issues need human prioritization before implementation
  ✓ Research findings vary in quality (some runs find nothing actionable)
  ✓ Multiple work items can be executed in parallel

PREFER A SIMPLER PATTERN when:
  ✗ Work is already well-defined → use IssueOps
  ✗ Issues can go directly to Copilot without review → use assignees: copilot shortcut
  ✗ Work spans multiple repositories → use MultiRepoOps

RELATED ALTERNATIVES:
  DispatchOps    — same research architecture, but manually triggered (on-demand)
  WorkQueueOps   — queue-based processing of the sub-issues generated by this pattern
```

*Source: `patterns/research-plan-assign-ops`, "When to Use" and "Prefer a simpler pattern when" sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-workqueue-ops.md` Claim 11 ("TaskOps — Research → Plan → Assign
    pattern" linked at `/gh-aw/patterns/task-ops/`): The redirect confirms this
    citation is correct; the pattern has since been renamed to ResearchPlanAssignOps
    and extended with an explicit Merge phase.
  - `docs-ghaw-ephemerals.md` Claim 3 (`expires:` for automatic closure of safe
    outputs): The Research and Plan phase configurations apply `expires: 1d` and
    `expires: 2d` respectively — consistent with the semantics documented there.
    This is the first corpus example of `expires:` applied specifically within a
    multi-phase research workflow.
  - `docs-ghaw-dataops.md` Claim 7 (`close-older-discussions: true` + `max: 1` +
    `title-prefix:` as "living report" pattern): The Research phase configuration
    uses the same three fields. The two notes confirm this configuration as a
    general-purpose pattern for maintaining a single current Discussion artifact
    across scheduled runs — not specific to DataOps.

- **Extends**:
  - `docs-ghaw-research-plan-assign-ops.md` (primary extraction, issue #351):
    This note adds the incremental YAML fields (`expires`, `title-prefix`,
    `category`, `close-older-discussions`) and the negative selection criteria
    not captured in the primary extraction. The two notes together constitute
    the complete extraction for `patterns/research-plan-assign-ops`.
  - `docs-ghaw-dispatch-ops.md` (DispatchOps Pattern): The Related Patterns
    section here positions DispatchOps as the "on-demand research" variant of
    ResearchPlanAssignOps. Together they define a two-mode research workflow
    taxonomy: scheduled (ResearchPlanAssignOps) vs. on-demand (DispatchOps).
  - `docs-ghaw-multi-repo-ops.md` (MultiRepoOps): The negative criterion
    "Work spans multiple repositories → use MultiRepoOps" is the first explicit
    handoff boundary between ResearchPlanAssignOps and MultiRepoOps in the corpus.

- **Contradicts**: None. The URL alias, YAML configurations, and selection
  criteria are consistent with all existing corpus source notes. The "TaskOps
  = 3-phase" characterization in `docs-ghaw-workqueue-ops.md` Claim 11 differs
  from the current 4-phase ResearchPlanAssignOps; this reflects a naming/version
  evolution, not a contradiction in pattern design.

- **Novel**:
  - **URL alias confirmed** (Claim 1): The task-ops → research-plan-assign-ops
    redirect resolves an open question in two existing source notes. No prior
    note had confirmed the alias relationship with direct evidence.
  - **Complete Research-phase `create-discussion` configuration** (Claim 2):
    The four-field combination (`expires: 1d`, `category: "research"`, `max: 1`,
    `close-older-discussions: true`) is not in the primary extraction (issue #351).
    This is the canonical research-phase Discussion config.
  - **`title-prefix:` chain across phases** (Claims 3–4, Concrete Artifacts):
    The three-tier `[go-fan]`/`[plan]`/`[fix]` title-prefix chain as a
    cross-phase traceability convention is not documented elsewhere in the corpus.
  - **Negative selection criteria with named alternatives** (Claim 5): The
    explicit handoffs (IssueOps, assignees shortcut, MultiRepoOps) as negative
    criteria for pattern selection are not in the primary extraction.
  - **DispatchOps as scheduled/on-demand twin** (Claim 8): Positioning
    DispatchOps explicitly as the on-demand research variant of
    ResearchPlanAssignOps is new to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Complete Research-phase `create-discussion` config** (Claim 2): The guide
  should document the canonical Discussion configuration for research workflows:
  `expires: 1d`, `category: "research"`, `max: 1`, `close-older-discussions: true`.
  This is the production-hardened recipe that prevents stale research artifact
  accumulation. Cite alongside `docs-ghaw-dataops.md` Claim 7 to establish this
  as a general pattern for living-report workflows, not just ResearchPlanAssignOps.

- **Plan phase `expires: 2d`** (Claim 3): Add the 2-day expiration as the
  recommended default for planning artifacts. This enforces a human-decision
  time window: if planned issues are not assigned within two days, they close
  automatically rather than accumulating as stale noise.

- **Title-prefix chain as traceability convention** (Claims 3–4): Document the
  three-tier convention (`[research]`/`[plan]`/`[fix]`) as a portable pattern
  for multi-phase workflow traceability — applicable beyond ResearchPlanAssignOps
  to any workflow that produces artifacts across multiple phases.

### Chapter 04: Pattern Selection and Implementation

- **Add negative selection criteria** (Claim 5): The existing guide coverage of
  ResearchPlanAssignOps (when to use) should be complemented by the negative
  criteria and explicit handoffs: IssueOps for well-defined work, the
  `assignees: copilot` shortcut when planning can be skipped, MultiRepoOps for
  cross-repository scope.

- **Add DispatchOps as on-demand twin** (Claim 8): When presenting
  ResearchPlanAssignOps, contrast it with DispatchOps: same research-first
  architecture, different trigger model. Teams that want periodic investigation
  use ResearchPlanAssignOps (scheduled); teams that want on-demand investigation
  use DispatchOps. The Plan and Assign phases are identical between the two.

## Extraction Notes

1. **Source URL is a redirect only**: The URL `https://github.github.com/gh-aw/patterns/task-ops`
   returns only a redirect notice with no substantive page content of its own.
   All substantive content was extracted from the redirect destination
   (`https://github.github.com/gh-aw/patterns/research-plan-assign-ops/`).

2. **Primary extraction already exists**: The redirect destination was
   previously extracted as `docs-ghaw-research-plan-assign-ops.md` (issue #351,
   extracted 2026-05-10). This note captures only the incremental content
   discovered in the current page state that was not in the primary extraction.
   Quotes in this note are from the current page (2026-05-24 fetch); consistency
   with the primary extraction confirms no major page changes between 2026-05-10
   and 2026-05-24.

3. **Prior mining attempt (PR #613)**: A previous miner PR (#613) created a
   `docs-ghaw-task-ops.md` note based on a different version of the page content
   (3-phase "TaskOps" with static analysis examples including zizmor, poutine,
   actionlint; Serena MCP duplicate detection; a Limitations section; and a
   5-axis customization matrix). That PR was closed for a technical pipeline
   reason (commit e8a8935 rate-limit fix), not due to content issues. The content
   it extracted is NOT verifiable against the current page state — the page no
   longer shows that version of the content, and those quotes cannot be confirmed
   verbatim. This note does not reproduce that earlier content; only claims that
   can be verified against the current page are included.

4. **No contradictions filed**: The URL alias confirmation and incremental
   configuration details are consistent with all existing corpus source notes.
   The "3-phase vs. 4-phase" difference between the prior PR's content and the
   current page reflects a page evolution (Merge phase made explicit), not a
   contradiction in pattern design.

5. **go-fan category**: The go-fan description says the discussion is created
   "under the `audits` category" while the YAML shows `category: "research"`.
   These are not contradictory — repositories can configure different category
   names; go-fan uses `audits` for its Discussion category while the generic
   configuration template uses `research`. The pattern supports any category
   name configured in the repository's Discussions settings.
