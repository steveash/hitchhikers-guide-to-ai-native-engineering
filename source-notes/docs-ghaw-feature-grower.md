---
source_url: https://github.github.com/gh-aw/patterns/feature-grower
source_type: docs
title: "GitHub Agentic Workflows: Feature Grower Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3110"
---

# GitHub Agentic Workflows: Feature Grower Pattern

> Named gh-aw pattern for growing a long-lived feature one implementation-ready
> sub-issue at a time, using a "crop and cookie" label pair and an open-child
> gate as backpressure against waterfall planning — the first corpus entry to
> name and mechanize "avoid waterfall planning" as a concrete harness pattern.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/feature-grower`
  page — in the `patterns/` design-patterns section alongside `MonitorOps`
  (previous in nav) and `MultiRepoOps` (next in nav), and listed with
  `WorkQueueOps` and `ResearchPlanAssignOps` as the pattern's named
  alternatives. Patterns pages are practitioner implementation references,
  not conceptual overviews.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind the `gh aw` CLI,
  Peli de Halleux's "Agent Factory" series, and every other `patterns/` page
  already in the corpus). The workflow frontmatter shown is a reference
  implementation, not a hypothetical example.
- **Scope**: Covers the Feature Grower pattern in full — the core concept and
  its rationale (avoiding waterfall planning), the crop/cookie label model and
  its open-child backpressure gate, the assessment sources the agent should
  consult, a complete reference workflow frontmatter, the agent instructions
  for the workflow body, scheduling/cadence guidance (including a link to a
  separate "All You Can Eat" pattern definition), and explicit applicability
  conditions with named alternatives. Does NOT cover: the internals of native
  GitHub sub-issues beyond the `parent` field, the `create-issue` safe output
  schema in full (see `docs-ghaw-safe-outputs-specification.md`), or the
  `gh-proxy` GitHub tools transport mode in detail (see
  `docs-ghaw-github-tools.md`).

## Extracted Claims

### Claim 1: Feature Grower advances a long-lived feature in small, reviewable increments by having a scheduled agent create only the next useful chunk of work, explicitly to avoid waterfall planning

- **Evidence**: The page's opening definition, extracted verbatim from the
  static page HTML (confirmed by direct inspection of the rendered article
  text, not just an AI-summarized fetch).
- **Confidence**: settled (first-party documentation; this is the pattern's
  own stated purpose, not an inference)
- **Quote**: "Feature Grower is a pattern for advancing a long-lived feature
  in small, reviewable increments. A scheduled agent reads the feature plan,
  assesses the current implementation, and creates only the next useful chunk
  of work. The next run reassesses the feature after that chunk has been
  completed." / "This avoids waterfall planning, where a large task tree is
  created before the implementation has produced feedback."
- **Our assessment**: This is the corpus's first pattern to name "waterfall
  planning" as the specific failure mode it exists to prevent, and to define
  avoidance mechanically (reassess-then-create-one-chunk) rather than as
  general advice. The design is a closed loop, not a one-shot planner: "plan
  states the direction; repository files, completed work, and optional memory
  show the current position" — the plan is treated as intent, not as an
  exhaustive backlog. For Ch02 and Ch04: this gives practitioners a concrete,
  implementable answer to "how do we avoid over-planning a multi-week
  feature?" — reassess from ground truth every run, emit exactly one chunk.

### Claim 2: The pattern uses two GitHub issue labels — `crop` for the open parent issue holding the feature plan, and `cookie` for an implementation-ready child issue sized for one pull request

- **Evidence**: Definition under "The crop and cookie model" heading, verified
  against the raw page HTML.
- **Confidence**: settled (first-party naming; the two labels are the
  pattern's central mechanism)
- **Quote**: "A `crop` labels an open parent issue containing the feature
  plan. A `cookie` labels an implementation-ready child issue sized for one
  pull request."
- **Our assessment**: The metaphor (crop → grows → cookie, i.e., harvested
  and ready to consume) is memorable but the mechanical content is what
  matters: `crop` is a durable, long-lived label on a tracking issue; `cookie`
  is a short-lived label on a PR-sized child. Sizing a `cookie` to "one pull
  request" is the pattern's operational definition of "chunk" — it ties the
  planning unit directly to the review unit. For Ch02: name `crop`/`cookie`
  as gh-aw's label vocabulary for this pattern, alongside the `plan`/
  `ai-generated` labels already documented in `docs-ghaw-research-plan-assign-ops.md`
  Claim 9 for a related but distinct pattern.

### Claim 3: An open-child gate — "a crop with an open cookie child is left alone" — provides backpressure that prevents the agent from producing new work faster than implementation can validate it

- **Evidence**: Stated directly under "The crop and cookie model," with the
  mechanism restated in operational terms: "Each scheduled run scans open
  crops. A crop with an open cookie child is left alone. ... The next run is
  skipped while that cookie remains open."
- **Confidence**: settled (first-party documentation; this is the pattern's
  named safety property)
- **Quote**: "A crop with an open cookie child is left alone." / "The
  open-child gate provides backpressure. It prevents the planner from
  producing work faster than implementation can validate its assumptions and
  keeps each crop focused on one active increment."
- **Our assessment**: This is the specific mechanism behind Claim 1's
  waterfall-avoidance goal — it is not just "create one chunk," it is "create
  one chunk, then structurally cannot create another until the first is
  closed." This is architecturally the same shape as the `skip-if-match`
  open-item gate in the "All You Can Eat" pattern (see Concrete Artifacts and
  Claim 8 below) applied to a parent/child issue relationship instead of a
  single-workflow-output relationship. For Ch02: name "open-child gate" as a
  second backpressure primitive alongside `skip-if-match`, for cases where the
  thing being rate-limited is a child issue under a longer-lived parent rather
  than the workflow's own last output.

### Claim 4: Assessment must prioritize the feature issue as the durable statement of intent and repository files as the source of truth for implementation status, with closed children/merged PRs for history and cache/repo memory as optional between-run observations that must not override current state

- **Evidence**: Full paragraph under "Assessment sources," extracted verbatim
  from the page.
- **Confidence**: settled (first-party documentation; this is a prescriptive
  assessment-priority ordering)
- **Quote**: "Use the feature issue as the durable statement of intent and
  repository files as the source of truth for implementation status. Closed
  children and merged pull requests provide a history of completed
  increments. Cache or repository memory can preserve brief observations
  between runs, but stale memory must not override current code or issue
  state."
- **Our assessment**: The explicit subordination of memory to ground truth
  ("stale memory must not override current code or issue state") is a
  guardrail against a specific failure mode: an agent that trusts its own
  cached summary of "what's done" over what the repository actually shows,
  and re-proposes already-completed work or misses completed work. This
  extends `docs-ghaw-cache-memory-reference.md`'s treatment of cache-memory as
  a capacity-bounded, LRU-evicted store (Claim 1) with a correctness rule:
  memory is advisory, not authoritative. For Ch03 (Safety and Verification):
  document "memory is advisory; repository state is authoritative" as a
  named rule for any pattern that combines cross-run memory with live
  repository inspection.

### Claim 5: The next chunk must be the smallest coherent change that materially advances the feature, with a clear objective, relevant implementation context, explicit non-goals, and testable acceptance criteria — and the agent should not decompose the entire remaining plan unless the current increment requires it

- **Evidence**: Second paragraph under "Assessment sources," extracted
  verbatim.
- **Confidence**: settled (first-party documentation; this is the pattern's
  explicit sizing and content rule for the generated issue)
- **Quote**: "The next chunk should be the smallest coherent change that
  materially advances the feature. It needs a clear objective, relevant
  implementation context, explicit non-goals, and testable acceptance
  criteria. Do not decompose the entire remaining plan unless the current
  increment requires that analysis."
- **Our assessment**: The four required components (objective, context,
  non-goals, acceptance criteria) are a minimal spec template for an
  agent-consumable issue, structurally similar to the sub-issue formatting
  requirements in `docs-ghaw-research-plan-assign-ops.md` Claim 4 (objective,
  files to touch, implementation guidance, acceptance criteria) — but Feature
  Grower's rule explicitly forbids upfront decomposition of the whole plan,
  where ResearchPlanAssignOps's Plan phase explicitly produces up to five
  sub-issues in one pass (Claim 3 in that note). The two patterns encode
  opposite defaults for the same problem (how much to plan ahead), and the
  Feature Grower page itself resolves this as a conditioning choice, not a
  disagreement — see Cross-References below.

### Claim 6: The reference workflow frontmatter uses `on.skip-if-match` as a bare query string sibling to `schedule` and `workflow_dispatch` (not nested inside either), matching an existing open `cookie` issue on a stable hidden marker

- **Evidence**: Reconstructed from the rendered code block's per-line
  indentation data (`--ecIndent` CSS custom properties in the page's
  Expressive Code markup), confirming `schedule`, `workflow_dispatch`, and
  `skip-if-match` sit at the same indentation depth under `on:` — i.e.
  `skip-if-match` is a top-level `on.*` field used here in its bare-string
  shorthand form, consistent with the `on.skip-if-match.query` field
  documented in `docs-ghaw-frontmatter-full-reference.md` Claim 3.
- **Confidence**: settled (verified against raw HTML/CSS indentation data,
  not the AI-summarized fetch, which had reconstructed this block
  inconsistently across passes — see Extraction Notes)
- **Quote**: `skip-if-match: 'is:issue is:open "gh-aw-workflow-id:
  feature-grower" in:body'`
- **Our assessment**: This is a concrete example of the bare-string shorthand
  for `skip-if-match` (a plain query string, no `query:`/`max:`/`scope:`
  sub-fields) — the "All You Can Eat" pattern's own documentation (Concrete
  Artifacts, below) confirms this shorthand implies `max: 1`. Combined with
  the `gh-aw-workflow-id: feature-grower` marker, the config skips activation
  whenever an open issue carries that hidden identity marker in its body —
  i.e., whenever an unconsumed `cookie` still exists. For Ch02: add this as a
  second worked example of `skip-if-match`'s string-shorthand form alongside
  the one in `docs-ghaw-cost-management.md` (`'label:duplicate OR
  label:wont-fix'`).

### Claim 7: The workflow body instructs the agent to skip crops with an open `cookie` child, set the new cookie's `parent` field to the existing crop's issue number (not a `temporary_id`), and emit `noop` when there is no useful next increment

- **Evidence**: Agent-instruction prose following the YAML frontmatter block,
  extracted verbatim from the page.
- **Confidence**: settled (first-party documentation; this is the literal
  instruction text shown as the reference implementation)
- **Quote**: "Find open issues labeled `crop`. Skip every crop that has an
  open child issue labeled `cookie`. For each eligible crop, assess the plan
  against completed children, memory, and current repository files. Create
  one implementation-ready `cookie` issue with its `parent` set to the crop
  issue number. Use `noop` when there is no useful next increment."
- **Our assessment**: This is a variant use of the `parent` field documented
  in `docs-ghaw-issueops.md` Claim 6. That note's JSON example links a newly
  created child to a newly created parent via `temporary_id` (both issues
  created in the same run); here, `parent` is set directly to an
  **already-existing** crop issue number, since the crop long predates any
  individual cookie run. This is a second, simpler `parent`-linking mode not
  previously documented in the corpus: link to a pre-existing issue by number
  rather than to a same-run `temporary_id` reference. For Ch02: document both
  modes of the `parent` field side by side — same-run linking via
  `temporary_id`, and cross-run linking via a literal issue number.

### Claim 8: The page explicitly warns against `create-issue.group: true` for this pattern, because grouping creates a workflow-owned parent instead of attaching the new issue to the existing crop

- **Evidence**: Explicit prohibition stated immediately after the workflow
  instructions, extracted verbatim.
- **Confidence**: settled (first-party documentation; stated as a direct
  "do not" instruction with its rationale)
- **Quote**: "Do not use `create-issue.group: true`: grouping creates a
  workflow-owned parent instead of attaching the new issue to the existing
  crop."
- **Our assessment**: This is a specific, easy-to-make configuration mistake:
  `group: true` is the mechanism `docs-ghaw-research-plan-assign-ops.md`
  Claim 9 documents for the Plan phase (grouping up to five new sub-issues
  under a new parent tracking issue created in the same run). Applying that
  same option to Feature Grower would silently create a second, redundant
  parent issue instead of attaching the cookie to the pre-existing crop —
  the two patterns need mutually exclusive `create-issue` configurations for
  superficially similar sub-issue-creation goals. For Ch02: flag this as a
  configuration trap when documenting `create-issue.group` — its correctness
  depends on whether the parent already exists (Feature Grower: use `parent:
  <existing-number>`) or is being created in this run (ResearchPlanAssignOps:
  use `group: true`).

### Claim 9: `skip-if-match` should be configured to run before activation, in the `pre_activation` job, matching a stable hidden marker rather than an editable title, and prefetching the crop/cookie relationship in a deterministic step (rather than via agent tool calls) makes the gate auditable and reduces tool calls

- **Evidence**: "Scheduling and backpressure" section plus the workflow-shape
  prose, extracted verbatim.
- **Confidence**: settled (first-party documentation; explicit operational
  guidance)
- **Quote**: "Always configure `skip-if-match` so an older output from the
  workflow blocks a new one while it remains open. Match the stable workflow
  marker rather than a title that a user can edit." / "Prefetching crops and
  their native sub-issue relationships in a deterministic step makes the gate
  auditable and reduces agent tool calls. Recheck the gate immediately before
  declaring the safe output to reduce duplicate work caused by concurrent
  human activity."
- **Our assessment**: Two distinct correctness rules are bundled here: (1)
  match on identity, not on mutable presentation (the same principle as the
  "All You Can Eat" pattern's own "match on stable identity" rule — see
  Concrete Artifacts); (2) recheck the gate condition twice — once
  deterministically before the agent runs (cheap, auditable), and once again
  immediately before the safe output is declared, specifically to close a
  race window where a human closes/reopens a cookie mid-run. This second
  "recheck immediately before declaring" step is a concurrency-safety pattern
  not previously documented in the corpus's treatment of `skip-if-match`
  (`docs-ghaw-cost-management.md` Claim 5, `docs-ghaw-frontmatter-full-reference.md`
  Claim 3) — those describe a single pre-activation check, not a
  belt-and-suspenders recheck against concurrent human edits. For Ch03: add
  "recheck idempotency gates immediately before the safe output, not only at
  activation" as a concurrency-safety pattern for any workflow whose gate
  condition can change during a long-running agent job.

### Claim 10: Cadence should be chosen by how quickly maintainers consume each increment — a frequent ("All You Can Eat") schedule around every 30 minutes when the next chunk should appear soon after consumption, or a daily/weekday schedule when slower growth is acceptable — always capping creation at one output per run with concurrency enabled

- **Evidence**: "Scheduling and backpressure" section's cadence guidance,
  extracted verbatim, plus the linked "All You Can Eat" pattern definition
  followed as a sub-page.
- **Confidence**: settled for the cadence-selection rule (first-party,
  explicit); the "All You Can Eat" pattern itself is settled first-party
  documentation from a companion reference file in the same `gh-aw` repository
- **Quote**: "Choose the cadence based on how quickly maintainers consume each
  increment: Use the All You Can Eat pattern with a frequent schedule,
  typically every 30 minutes, when the next chunk should appear soon after the
  previous issue closes or pull request merges. Use a daily or weekday
  schedule when slower growth is preferable and a delay before the next chunk
  is acceptable. In either case, cap creation at one output per run and keep
  concurrency enabled."
- **Our assessment**: Feature Grower does not itself define "All You Can Eat"
  — it links to a separate pattern-vocabulary file
  (`.github/aw/workflow-patterns.md` in the `github/gh-aw` repository, not the
  `patterns/` docs site) that defines it generically: "a scheduled workflow
  that keeps at most one *unconsumed* output alive at a time... content is
  served one plate at a time, on demand." Feature Grower is thus documented
  as a specific application of a more general open-item cadence pattern,
  applied to a parent/child issue relationship instead of a single workflow's
  own last output (see Claim 3). This is the first corpus source to name or
  define "All You Can Eat" explicitly. For Ch02: document "All You Can Eat"
  as the general cadence pattern, with Feature Grower's crop/cookie gate as a
  named specialization of it.

### Claim 11: Feature Grower is recommended when a feature has a stable direction but the best next step depends on implementation feedback — good for migrations, broad refactors, and multi-PR capabilities — with upfront planning, WorkQueueOps, or ResearchPlanAssignOps preferred when work is fully known or requires complete human-approved breakdown upfront

- **Evidence**: "When to use this pattern" section, extracted verbatim.
- **Confidence**: settled (first-party documentation; explicit applicability
  and alternative-pattern guidance)
- **Quote**: "Use Feature Grower when a feature has a stable direction but the
  best next step depends on implementation feedback. It works well for
  migrations, broad refactors, and capabilities that should land through a
  series of independently reviewable pull requests." / "Prefer upfront
  planning when work has fixed dependencies that must be approved as a whole.
  Prefer WorkQueueOps when all work items are already known, or
  ResearchPlanAssignOps when research should produce a complete,
  human-approved task breakdown before implementation."
- **Our assessment**: This section is the pattern's own decision framework
  and directly resolves the apparent tension with Claim 5: Feature Grower is
  for work whose shape is *not* fully knowable in advance (implementation
  feedback changes the next step); WorkQueueOps (`docs-ghaw-workqueue-ops.md`
  Claim 1: "processing a large backlog of work items" that are already
  enumerated) and ResearchPlanAssignOps
  (`docs-ghaw-research-plan-assign-ops.md` Claim 7: applicable "when human
  prioritization is needed before implementation") are for work that is
  either fully known or should be fully broken down before any
  implementation starts. All three patterns share the same underlying
  concern — how much to decompose before coding begins — and pick different
  points on that spectrum. For Ch05 (Team Adoption): present these three
  patterns as a single decision table keyed on "how well is the remaining
  work understood right now?"

## Concrete Artifacts

### Feature Grower Reference Workflow Frontmatter (from pattern page)

Reconstructed from the page's rendered code block, verified against the raw
per-line indentation data in the page HTML (not the summarized WebFetch
output, which mis-nested `skip-if-match` under `workflow_dispatch` in one
pass — see Extraction Notes):

```yaml
# .github/workflows/feature-grower.md
---
on:
  schedule: daily on weekdays
  workflow_dispatch:
  skip-if-match: 'is:issue is:open "gh-aw-workflow-id: feature-grower" in:body'
permissions:
  contents: read
  issues: read
tools:
  cache-memory:
    key: feature-grower
  github:
    mode: gh-proxy
    toolsets: [issues, repos]
safe-outputs:
  create-issue:
    labels: [cookie]
    max: 1
concurrency:
  group: feature-grower
  cancel-in-progress: false
---
```

*Source: `patterns/feature-grower`, "Workflow shape" section*

### Feature Grower Control Flow (mermaid flowchart, from pattern page)

```
plan[Feature plan] --> assess[Assess current state]
assess --> gate{Active chunk?}
gate -- yes --> wait[Wait]
gate -- no --> chunk[Create next sub-issue]
chunk --> implement[Implement and review]
implement --> assess
```

*Source: `patterns/feature-grower`, "Overview" section (mermaid diagram source,
extracted from the raw page markup)*

### "All You Can Eat" Pattern Definition (from linked sub-page, followed per MINER.md §1)

The Feature Grower page links "All You Can Eat pattern" to
`https://github.com/github/gh-aw/blob/main/.github/aw/workflow-patterns.md#all-you-can-eat-pattern`
— a shared pattern-vocabulary file in the `github/gh-aw` repository, distinct
from the `patterns/` docs site. Followed as a substantive linked page per
MINER.md §1:

```
All You Can Eat Pattern

Nickname for a scheduled workflow that keeps at most one *unconsumed* output
alive at a time. The workflow wakes up frequently (typically every 30
minutes), but activation is skipped while the previous output from that
workflow is still open. As soon as the user consumes the previous output
(closes the issue, merges or closes the pull request), the next scheduled
run produces the next item — content is served one plate at a time, on
demand, and runs proceed sequentially.

Rules:
- One open item at a time. Cap the safe output with `max: 1`. The string
  form of `skip-if-match` implies a threshold of `max: 1`, so any single
  open match skips activation; no extra field is needed.
- Match on stable identity. Prefer the hidden
  `gh-aw-workflow-id: <workflow-file-name-without-.md>` marker (`in:body`)
  over a title prefix, because humans rename titles.
- Do not starve. If the user never closes the item, the workflow never runs
  again. Set `expires:` on the safe output (or an equivalent auto-close) so
  an abandoned item eventually unblocks the schedule.
- Skipped runs are cheap. The check runs in the `pre_activation` job, so the
  agent never starts and no tokens are spent on a skipped tick.
```

*Source: `github/gh-aw` repository, `.github/aw/workflow-patterns.md`,
"All You Can Eat Pattern" section (raw file, quoted verbatim)*

### Related Documentation Links (from pattern page nav/footer)

```
Previous: MonitorOps
Next: MultiRepoOps
Named alternatives (from "When to use this pattern"): WorkQueueOps, ResearchPlanAssignOps
```

*Source: `patterns/feature-grower`, page navigation and "When to use this pattern" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` as the
    highest-ROI cost control, evaluated in the `pre_activation` job before
    any token spend): The "All You Can Eat" sub-page's "Skipped runs are
    cheap" rule and Feature Grower's own `skip-if-match` config both confirm
    this same pre-activation, zero-token-cost skip mechanism, applied here to
    an open-child (not open-output) condition.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 3 (six-field
    `on.skip-if-match` precondition system): Claim 6 here is a concrete,
    verified worked example of the bare-string shorthand form of
    `on.skip-if-match`.
  - `docs-ghaw-cache-memory-reference.md` Claim 4 (`key` option for named
    cache-memory stores): The reference frontmatter's `cache-memory: { key:
    feature-grower }` is a direct worked example of this field.
  - `docs-ghaw-github-tools.md` Claim 3 (`gh-proxy` transport mode): The
    reference frontmatter's `github: { mode: gh-proxy }` is a worked example
    of this transport mode, though Feature Grower does not use integrity
    reactions — here `gh-proxy` appears to be a plain performance choice, not
    a required dependency.
  - `docs-ghaw-workqueue-ops.md` Claim 9 (`concurrency.group` with
    `cancel-in-progress: false` to prevent race conditions): The reference
    frontmatter's `concurrency: { group: feature-grower, cancel-in-progress:
    false }` is a direct worked example of this same rule applied to a
    different pattern.

- **Contradicts**: None filed. Claim 5 (Feature Grower: create only the next
  chunk, do not decompose the whole plan) and
  `docs-ghaw-research-plan-assign-ops.md` Claim 3 (ResearchPlanAssignOps: the
  Plan phase creates up to five sub-issues in one pass) encode opposite
  planning-horizon defaults, but per MINER.md §4a this is a conditioning
  variable, not a contradiction — Claim 11 here shows the Feature Grower page
  itself names ResearchPlanAssignOps as the explicit alternative for when a
  complete upfront breakdown is wanted, and the two patterns' applicability
  conditions are disjoint (implementation-feedback-dependent vs.
  fully-plannable-upfront). No contradiction issue required.

- **Extends**:
  - `docs-ghaw-issueops.md` Claim 6 (`temporary_id` + `parent` sub-issue
    linking, both issues created in the same run): Claim 7 here documents a
    second `parent`-linking mode — linking a newly created child directly to
    an already-existing issue by number, with no `temporary_id` needed
    because the parent was not created in this run.
  - `docs-ghaw-research-plan-assign-ops.md` Claim 9 (`create-issue: group:
    true` for grouping new sub-issues under a new parent): Claim 8 here shows
    the same `group: true` option is actively harmful when the parent already
    exists, giving the corpus its first documented case where a safe-output
    option is correct for one named pattern and wrong for an adjacent one.
  - `docs-ghaw-cost-management.md` Claim 5 and
    `docs-ghaw-frontmatter-full-reference.md` Claim 3 (single pre-activation
    `skip-if-match` check): Claim 9 here adds a second check — rechecking the
    gate immediately before the safe output is declared — as a
    concurrency-safety refinement not previously documented for
    `skip-if-match`-gated workflows.
  - `docs-ghaw-workqueue-ops.md` Claim 1 and
    `docs-ghaw-research-plan-assign-ops.md` Claim 7 (applicability
    conditions for adjacent backlog/planning patterns): Claim 11 here
    completes a three-pattern applicability spectrum (Feature Grower /
    WorkQueueOps / ResearchPlanAssignOps) keyed on how well the remaining
    work is understood upfront.

- **Novel**:
  - **"Waterfall planning" named as the specific failure mode a pattern is
    designed to prevent** (Claim 1): No existing corpus source uses this term
    or frames a pattern's purpose this explicitly around avoiding upfront
    over-planning.
  - **The crop/cookie label pair and open-child gate** (Claims 2–3): Not
    documented in any existing note. This is a distinct backpressure
    mechanism from `skip-if-match`'s open-output gate — it rate-limits
    against an open *child* issue under a long-lived *parent*, not against
    the workflow's own last output.
  - **"All You Can Eat" as a named, defined cadence pattern** (Claim 10): No
    existing corpus source names or defines this pattern. It is defined in a
    companion pattern-vocabulary file in the `github/gh-aw` repository, not
    the docs site, and was not previously in the corpus's source list.
  - **Cross-run `parent`-by-existing-issue-number linking** (Claim 7): A
    second, previously undocumented mode of the `parent` field for sub-issue
    creation, distinct from the same-run `temporary_id` mode in
    `docs-ghaw-issueops.md`.
  - **Recheck-the-gate-before-declaring-output as a concurrency-safety
    pattern** (Claim 9): Not documented elsewhere in the corpus for any
    `skip-if-match`-style gate.
  - **A three-pattern applicability spectrum for planning horizon** (Claim
    11): The corpus has documented WorkQueueOps and ResearchPlanAssignOps
    individually; this is the first source to explicitly triangulate all
    three patterns against each other on a single axis.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add Feature Grower to the patterns taxonomy as the harness pattern for
    long-lived, direction-stable features whose next step depends on
    implementation feedback (Claim 1, Claim 11). Present its control loop
    (plan → assess → gate → create-one-chunk → implement → reassess) as a
    concrete, implementable alternative to upfront task-tree planning.
  - Document the open-child gate (crop/cookie) as a second named backpressure
    primitive alongside `skip-if-match`'s open-output gate (Claim 3), and the
    "All You Can Eat" pattern as the general cadence vocabulary both draw
    from (Claim 10).
  - Document the two `parent`-linking modes for sub-issue creation side by
    side: same-run via `temporary_id` (`docs-ghaw-issueops.md` Claim 6) vs.
    cross-run via an existing issue number (Claim 7 here) — and flag
    `create-issue.group: true` as correct only for the former (Claim 8).

- **Chapter 03 (Safety and Verification)**:
  - Add "memory is advisory, repository state is authoritative" as a named
    rule for any pattern combining cache/repo memory with live repository
    inspection (Claim 4).
  - Add "recheck idempotency gates immediately before declaring the safe
    output, not only at pre-activation" as a concurrency-safety refinement
    for long-running gated workflows (Claim 9).

- **Chapter 05 (Team Adoption)**:
  - Add a three-way decision table — Feature Grower vs. WorkQueueOps vs.
    ResearchPlanAssignOps — keyed on how well the remaining work is
    understood before implementation starts (Claim 11), cross-referencing
    `docs-ghaw-workqueue-ops.md` and `docs-ghaw-research-plan-assign-ops.md`.

## Extraction Notes

1. **The docs site (`github.github.com/gh-aw/...`) is a client-rendered
   Astro/Starlight site, but the article content is present in the static
   HTML.** Rather than rely solely on WebFetch's AI-summarized output — which
   reconstructed the reference YAML block with `skip-if-match` incorrectly
   nested inside `workflow_dispatch` in one of two independent passes — the
   raw page HTML was fetched directly with `curl`, tags were stripped to
   recover the flattened article text, and the Expressive Code code block's
   per-line `--ecIndent` CSS values were parsed directly to recover the
   YAML's true nesting (confirming `skip-if-match` is a top-level `on:`
   sibling, not nested under `workflow_dispatch`). All quotes in this note
   were verified against this raw-HTML extraction, not the summarized
   WebFetch output.

2. **One linked sub-page was followed**: the "All You Can Eat pattern" link
   resolves to `.github/aw/workflow-patterns.md` in the `github/gh-aw`
   repository (a raw Markdown file, not a `patterns/` docs page). This was
   fetched directly via `raw.githubusercontent.com` and quoted verbatim in
   Concrete Artifacts. No other sub-pages were followed — the four other
   linked pages (MonitorOps, MultiRepoOps, WorkQueueOps,
   ResearchPlanAssignOps) already have source notes in the corpus and were
   cross-referenced against those existing notes instead of re-fetched.

3. **No contradictions filed**: reviewed all existing GHAW corpus source
   notes for claims that materially oppose any claim here. The apparent
   tension between Feature Grower's "don't decompose the whole plan" (Claim
   5) and ResearchPlanAssignOps's "create up to five sub-issues per Plan run"
   is resolved by the source itself as a conditioning variable (Claim 11,
   the page's own "When to use this pattern" section) — not a genuine
   disagreement about the same conditions. No contradiction issue required
   per MINER.md §4a.

4. **No explicit publication date** on the pattern page, consistent with
   other `patterns/` pages in the corpus; `date_published` is left null.
