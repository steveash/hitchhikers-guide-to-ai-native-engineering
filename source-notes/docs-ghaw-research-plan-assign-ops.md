---
source_url: https://github.github.com/gh-aw/patterns/research-plan-assign-ops
source_type: docs
title: "GitHub Agentic Workflows: ResearchPlanAssignOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#351"
---

# GitHub Agentic Workflows: ResearchPlanAssignOps Pattern

> Named first-party pattern for a complete four-phase development harness
> (Research → Plan → Assign → Merge) that moves from automated codebase
> discovery to merged code while maintaining human decision gates at every
> phase transition — distinct from single-phase patterns in that it sequences
> scheduling, ChatOps, sub-issue orchestration, and human code review into one
> end-to-end workflow with a specific configuration vocabulary.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/research-plan-assign-ops`
  page — in the same `patterns/` section as `patterns/orchestration`,
  `patterns/agentic-ops`, `patterns/workqueue-ops`, and others. Patterns pages are
  practitioner implementation references, not conceptual overviews or API references.
  Note: `docs-ghaw-workqueue-ops.md` Claim 11 references this same pattern under the
  URL `/gh-aw/patterns/task-ops/` with the shortened name "TaskOps" — the two URLs
  may be aliases or the pattern may have been renamed; the content returned at
  `research-plan-assign-ops` is the authoritative extraction here.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` platform.
  YAML configurations and CLI behavior are authoritative for the `gh aw` platform.
  Claims about the end-to-end pattern design and applicability conditions represent
  first-party design intent. The `go-fan` reference implementation workflow is a named
  production example from the same team.
- **Scope**: Covers the ResearchPlanAssignOps design pattern — its four phases, the
  configuration vocabulary for each phase (cache-memory, safe-outputs grouping,
  assignees: copilot), the sub-issue formatting requirements for agent-consumable
  work items, the human decision gate model, and the applicability conditions. Does NOT
  cover: orchestration primitives in general (see `docs-ghaw-orchestration-patterns.md`),
  agentic monitoring patterns (see `docs-ghaw-agentic-ops.md`), queue-based backlog
  processing for the Assign phase (see `docs-ghaw-workqueue-ops.md`), or how individual
  Copilot agents produce their PRs.

## Extracted Claims

### Claim 1: ResearchPlanAssignOps is a named gh-aw pattern for a four-phase end-to-end development harness that moves from automated codebase discovery to merged code with human decision gates at every phase transition

- **Evidence**: Opening definition and phase structure of the page; the pattern is
  formally named, defined, and listed in the `patterns/` section alongside other named
  patterns (WorkQueueOps, AgenticOps, IssueOps, Orchestration).
- **Confidence**: settled (first-party documentation; the pattern name and four-phase
  structure are consistently extracted across multiple fetch passes)
- **Quote**: (no direct quote; two WebFetch calls returned different wordings of the
  opening description, so no single verbatim passage can be confirmed. See paraphrase
  in Our assessment.)
- **Our assessment**: This is a qualitatively different pattern from the single-phase
  patterns in the corpus (DailyOps, IssueOps, ChatOps, AgenticOps). Those patterns
  describe how to react to a trigger. ResearchPlanAssignOps describes a complete
  software development lifecycle managed through gh-aw, from "what should we work on?"
  (Research) to "is the work done?" (Merge). The explicit four-phase naming is
  significant: it formalizes a workflow that practitioners often implement ad-hoc into
  a named, configurable pattern with defined inputs, outputs, and transition triggers.
  For Ch02 (Harness Engineering) and Ch04 (Multi-Agent Orchestration): add as the
  canonical gh-aw pattern for research-driven development harnesses, positioned
  alongside WorkQueueOps (backlog processing) and AgenticOps (fleet monitoring) in
  the multi-phase pattern taxonomy.

### Claim 2: Phase 1 (Research) is a scheduled workflow that investigates the codebase from a specific angle and publishes its findings as a GitHub Discussion — the Discussion is the contract for subsequent phases

- **Evidence**: Phase 1 description consistently extracted across fetch passes; the
  go-fan workflow is named as the reference implementation.
- **Confidence**: settled (first-party documentation; consistently extracted)
- **Quote**: "A scheduled workflow investigates the codebase from a specific angle and
  publishes its findings as a GitHub discussion."
- **Our assessment**: The "specific angle" framing is architecturally significant —
  each research workflow has a defined domain of inquiry (Go dependencies, security
  patterns, performance regressions) rather than a general sweep. The Discussion as
  contract is the key design choice: rather than piping findings directly to an issue
  queue, the research phase creates a human-readable artifact that developers can read,
  evaluate, and selectively act on. The Discussion is shared with the team, enabling
  async awareness before any planning or implementation begins. For Ch02: document
  "publish research findings to GitHub Discussion" as the standard Research phase output
  pattern — this is the mechanism that enables human review before Plan.

### Claim 3: Phase 2 (Plan) is triggered by a developer's /plan command on the research Discussion, causing the plan workflow to read the Discussion, extract concrete work items, and create up to five sub-issues grouped under a parent tracking issue

- **Evidence**: Phase 2 description consistently extracted across fetch passes; the
  `/plan` ChatOps trigger is explicitly named.
- **Confidence**: settled (first-party documentation; consistently extracted)
- **Quote**: (no direct quote; WebFetch returned ellipsis-containing versions that
  cannot be confirmed as verbatim. See paraphrase in Our assessment.)
- **Our assessment**: The `/plan` command is the first human decision gate. The
  developer does not just acknowledge the research findings — they must actively invoke
  planning. This prevents automatic escalation of low-quality or irrelevant research
  runs into implementation work. The "up to five sub-issues" cap (visible in the
  `max: 5` YAML configuration) bounds the planning output, preventing a single research
  finding from spawning an unbounded backlog. The sub-issues are grouped under a parent
  tracking issue, providing a rollup view of all work items derived from a single
  research run. For Ch04: document the /plan command as the ChatOps trigger for the
  Research→Plan transition, using the `safe-outputs: create-issue: group: true` pattern
  to create the tracking hierarchy.

### Claim 4: Each sub-issue generated by the plan phase is formatted for coding agent consumption — with a clear objective, the files to touch, step-by-step implementation guidance, and acceptance criteria

- **Evidence**: Direct quote from the page appearing in identical form across multiple
  WebFetch calls.
- **Confidence**: settled (verbatim quote; consistent across fetches)
- **Quote**: "The planner formats each sub-issue for a coding agent: a clear objective,
  the files to touch, step-by-step implementation guidance, and acceptance criteria."
- **Our assessment**: This is the critical specification for agent-ready work items. The
  four-field format (objective, files, guidance, criteria) is a minimum viable
  specification for a coding agent to operate autonomously. Without explicit file targets,
  a coding agent may modify the wrong files; without acceptance criteria, it has no way
  to verify its own output. This extends the sub-issue hierarchy pattern from
  `docs-ghaw-issueops.md` Claim 6 with specific content requirements — IssueOps
  describes the structural format (temporary_id, parent); ResearchPlanAssignOps specifies
  the content requirements for AI-consumable issue bodies. For Ch01 (Specifications /
  context engineering): the four-field format is the minimal spec an AI agent needs to
  self-direct. For Ch02: recommend this format for any issue that will be assigned to
  an AI agent, not just in ResearchPlanAssignOps.

### Claim 5: Phase 3 (Assign) routes sub-issues to Copilot via GitHub's native UI or bulk orchestrator workflows, enabling parallel implementation — Copilot opens PRs and posts progress updates independently

- **Evidence**: Phase 3 description consistently extracted across fetch passes; the
  `assignees: copilot` configuration and the bulk orchestrator path are both named.
- **Confidence**: settled (first-party documentation)
- **Quote**: "With well-scoped issues in hand, the developer assigns them to Copilot
  for automated implementation. Copilot opens a pull request and posts progress updates
  as it works."
- **Our assessment**: The two assignment paths (native UI vs. bulk orchestrator) serve
  different scales. A developer manually assigning a handful of sub-issues uses the
  native GitHub UI. A team assigning dozens of sub-issues at once uses a bulk
  orchestrator workflow — presumably using the `dispatch-workflow` or `call-workflow`
  patterns from `docs-ghaw-orchestration-patterns.md`. The progress updates (PR
  description, comments) provide visibility without requiring the developer to actively
  poll each Copilot instance. Parallel execution is the efficiency mechanism — multiple
  Copilot agents work on different sub-issues simultaneously, with each contributing
  its own PR. For Ch04: document the dual-path assignment mechanism (UI for small
  batches, orchestrator for large ones) and the parallel PR-per-sub-issue execution
  model.

### Claim 6: Phase 4 (Merge) requires human maintainer review before merging — maintainers check correctness and test compliance, and tracking issues auto-close when all sub-issues resolve

- **Evidence**: Phase 4 description consistently extracted across fetch passes;
  auto-close behavior for the tracking issue is explicitly stated.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Copilot's pull request is reviewed by a human maintainer. The maintainer
  checks correctness, runs tests, and merges."
- **Our assessment**: The merge gate is the final human decision point — no AI-generated
  code merges without maintainer approval. This distinguishes the pattern from fully
  autonomous coding agents: every PR still requires a human reviewer. The auto-close
  behavior for the tracking issue when all sub-issues resolve provides automatic
  housekeeping without requiring the developer to manually close the parent issue. For
  Ch04: the Merge phase is where the pattern reconnects to standard pull request review
  workflows — there is no special gh-aw configuration for the merge gate itself; it is
  the absence of autonomous merge that defines this phase.

### Claim 7: The pattern is explicitly designed for three specific use cases: when work scope is unknown until analysis runs, when human prioritization is needed before implementation, or when research quality varies across runs

- **Evidence**: "When to use" section of the pattern page, extracted via WebFetch
  across multiple fetch passes.
- **Confidence**: settled (first-party; stated as explicit applicability conditions)
- **Quote**: "the scope of work is unknown until analysis runs" / "issues need human
  prioritization before implementation" / "research findings vary in quality"
- **Our assessment**: The three conditions define the target class for this pattern.
  They are complementary but independent — any one of them justifies using
  ResearchPlanAssignOps. The "quality varies" condition is the most subtle: it
  acknowledges that AI-generated research findings are not uniformly actionable, and
  human judgment is the quality filter between research and planning. This is honest
  about the current state of AI-generated code analysis: a research workflow may
  identify real issues on one run and false positives on the next, so automation
  without human review would create noise. For Ch02 and Ch05 (Team Adoption): use
  these three conditions as the adoption decision criteria — teams that do NOT have
  all three can likely use a simpler pattern (DailyOps for direct incremental
  improvement, WorkQueueOps for pre-defined backlogs).

### Claim 8: The research phase uses `cache-memory: true` for cross-run persistence, enabling the scheduled research workflow to accumulate context and findings across multiple executions

- **Evidence**: Configuration example from the page showing `tools: cache-memory: true`
  as a research workflow option.
- **Confidence**: settled (YAML configuration block; consistent with cache-memory
  semantics documented in `docs-ghaw-audit-with-agents.md` Claim 5)
- **Quote**: (no direct quote; see Concrete Artifacts section for YAML block)
- **Our assessment**: Cache-memory makes the research phase stateful — the go-fan
  workflow tracking Go dependencies can remember which dependencies it already examined,
  which suggestions it already surfaced, and what the baseline state was. Without
  cache-memory, each research run would be independent and potentially repeat the same
  findings. With cache-memory, the research workflow can track changes over time and
  only surface new or worsening conditions. This is consistent with `docs-ghaw-audit-with-agents.md`
  Claim 5 (cache-memory for rolling baselines) but applied to the research discovery
  phase rather than post-run audit consumption.

### Claim 9: The planning phase uses `safe-outputs: create-issue: group: true, max: 5, labels: [plan, ai-generated]` — grouping sub-issues under a parent tracking issue with a five-issue cap and AI-provenance labels

- **Evidence**: Planning configuration block from the page showing the `group: true`
  field alongside `max: 5` and labels.
- **Confidence**: settled (YAML configuration block from the page)
- **Quote**: (no direct quote; see Concrete Artifacts section for YAML block)
- **Our assessment**: `group: true` is a previously undocumented `safe-outputs:
  create-issue:` field. It controls the parent-sub-issue relationship structure:
  with `group: true`, the plan workflow creates one parent tracking issue and up to
  `max: 5` child sub-issues in a single safe-output operation. The `labels: [plan,
  ai-generated]` serve two functions: searchability (find all planned items from
  research) and AI-provenance transparency (flag that these issues were generated by
  the plan workflow). For Ch02: document `group: true` as the sub-issue grouping
  primitive for safe-outputs, distinct from the `temporary_id` + `parent` JSON format
  in `docs-ghaw-issueops.md` Claim 6.

### Claim 10: Direct assignment uses `safe-outputs: create-issue: assignees: copilot` — automatically routing newly created sub-issues to Copilot at creation time, eliminating a separate manual assignment step

- **Evidence**: Direct assignment configuration block from the page.
- **Confidence**: settled (YAML configuration block)
- **Quote**: (no direct quote; see Concrete Artifacts section for YAML block)
- **Our assessment**: Embedding `assignees: copilot` in the plan workflow's
  `create-issue` safe-output closes the Plan→Assign transition automatically. Rather
  than the developer manually assigning each sub-issue after planning, the plan workflow
  itself creates issues that are already assigned to Copilot. This compresses two
  steps (create + assign) into one, suitable for teams that have established trust in
  the research and planning quality and want less manual intervention. The tradeoff is
  that the developer loses the Plan→Assign review gate — sub-issues go directly from
  planning to Copilot without human triage of individual items. For Ch02: document
  `assignees: copilot` in `create-issue` as the auto-assign variant of the pattern,
  contrasted with the two-step (plan then manually assign) variant.

### Claim 11: The go-fan workflow is named as a concrete reference implementation of the Research phase — it runs on weekdays, examines Go dependencies, and creates categorized discussions with improvement suggestions

- **Evidence**: Phase 1 description names go-fan explicitly as the exemplar research
  workflow with its specific domain (Go dependencies) and schedule (weekdays).
- **Confidence**: anecdotal (single named workflow; no metrics or additional
  corroboration from other sources)
- **Quote**: (no direct quote; derived from Phase 1 description which described go-fan
  as a research workflow that "runs on weekdays, examines Go dependencies, and creates
  categorized discussions with improvement suggestions")
- **Our assessment**: The go-fan workflow provides concrete evidence that the pattern
  is in production use at the team that authored it. The "categorized discussions"
  framing suggests go-fan creates structured Discussion posts rather than free-form
  analysis — likely with categories like "security updates," "major version upgrades,"
  "deprecated dependencies." The weekday-only schedule reflects cost management (no
  weekend runs for non-urgent dependency monitoring). For Ch02: use go-fan as the
  canonical example when illustrating the Research phase — it shows the pattern in a
  real domain (Go dependency management) with specific outputs (categorized discussions).

## Concrete Artifacts

### Research Phase Configuration (with cache-memory)

```yaml
# Research workflow frontmatter (representative)
tools:
  cache-memory: true
```

- Enables cross-run state for the research workflow
- Research findings accumulate across multiple scheduled executions
- Consistent with cache-memory semantics in docs-ghaw-audit-with-agents.md Claim 5

*Source: `patterns/research-plan-assign-ops` — Research phase configuration section*

### Planning Phase Configuration (with grouping)

```yaml
# Plan workflow frontmatter (representative)
safe-outputs:
  create-issue:
    group: true
    max: 5
    labels: [plan, ai-generated]
```

- `group: true`: creates one parent tracking issue with sub-issues
- `max: 5`: caps sub-issue output per planning run
- Labels provide searchability and AI-provenance transparency

*Source: `patterns/research-plan-assign-ops` — Plan phase configuration section*

### Direct Assignment Configuration

```yaml
# Assignment configuration (representative)
safe-outputs:
  create-issue:
    assignees: copilot
```

- Automatically routes created sub-issues to Copilot at creation time
- Collapses Plan→Assign into a single safe-output operation
- Suitable for teams with established trust in research and planning quality

*Source: `patterns/research-plan-assign-ops` — Assignment configuration section*

### Four-Phase Workflow Summary

```
ResearchPlanAssignOps: Research → Plan → Assign → Merge

Phase 1: Research
  Trigger:  Scheduled (weekdays)
  Action:   Investigate codebase from a specific angle
  Output:   GitHub Discussion with findings and recommendations
  Config:   cache-memory: true (cross-run persistence)
  Example:  go-fan (Go dependency monitoring)

Phase 2: Plan
  Trigger:  Developer issues /plan command on research Discussion
  Action:   Extract work items, create up to 5 grouped sub-issues
  Output:   Parent tracking issue + ≤5 sub-issues
  Config:   safe-outputs: create-issue: group: true, max: 5,
                                        labels: [plan, ai-generated]
  Sub-issue format: objective + files to touch + implementation
                    guidance + acceptance criteria

Phase 3: Assign
  Trigger:  Developer assigns sub-issues via UI or bulk orchestrator
  Action:   Copilot implements each sub-issue in parallel
  Output:   One PR per sub-issue, progress updates posted
  Config:   safe-outputs: create-issue: assignees: copilot (auto-assign)
            OR manual UI assignment + optional bulk orchestrator

Phase 4: Merge
  Trigger:  Copilot opens PR; developer reviews
  Action:   Human maintainer checks correctness and tests, then merges
  Output:   Merged code; tracking issue auto-closes when all sub-issues resolve
  Config:   Standard GitHub PR review (no gh-aw-specific config)

Human decision gates:
  After Research → developer reads Discussion and issues /plan (or ignores it)
  After Plan      → developer reviews sub-issues and assigns (or batches with orchestrator)
  After Assign    → maintainer reviews each PR and merges (or requests changes)
```

*Source: `patterns/research-plan-assign-ops` — full page synthesis*

### Applicability Conditions

```
Use ResearchPlanAssignOps when:
  1. "the scope of work is unknown until analysis runs"
     (the codebase must be analyzed before knowing what to implement)

  2. "issues need human prioritization before implementation"
     (not all research findings are worth acting on — human filter is essential)

  3. "research findings vary in quality"
     (AI-generated analysis is not uniformly actionable — humans select what to plan)

Do NOT use when:
  - Work scope is already known (use WorkQueueOps for pre-defined backlogs)
  - All findings should be automatically actioned (use DailyOps for direct improvement)
  - A single-phase trigger-response model suffices (use IssueOps or ChatOps)
```

*Source: `patterns/research-plan-assign-ops` — "Use Cases" / "When to Use" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-issueops.md` Claim 6 (sub-issue hierarchies with `temporary_id` and
    `parent` fields for agent-sized task decomposition): The Plan phase creates sub-issues
    grouped under a parent tracking issue — the same structural model. The difference is
    the trigger: IssueOps creates hierarchies in response to issue-open events; ResearchPlanAssignOps
    creates them in response to a /plan command on a research Discussion. Both confirm
    sub-issue hierarchies as the standard multi-task decomposition primitive in gh-aw.
  - `docs-ghaw-issueops.md` Claim 7 (`assignees: copilot` for parallel autonomous
    execution): The direct assignment configuration uses `assignees: copilot` in
    `create-issue`, consistent with IssueOps Claim 7. This source adds the creation-time
    variant (embedded in the plan output) alongside IssueOps's post-creation variant.
  - `docs-ghaw-agentic-ops.md` Claim 4 (two-level escalation: Discussion for durable
    record, Issue for actionable findings): The Research phase publishes to Discussions
    for team-wide visibility before any issues are created — same escalation model, applied
    to research findings instead of monitoring alerts.
  - `docs-ghaw-workqueue-ops.md` Claim 11 (TaskOps named as "Research → Plan → Assign
    pattern"): The WorkQueueOps note references `patterns/task-ops` with the description
    "Research → Plan → Assign pattern." This aligns with the four-phase structure of
    the `research-plan-assign-ops` pattern — either the page is available at both URLs
    or one is an older alias. The Assign-phase sub-issue queue is the primary interface
    between ResearchPlanAssignOps and WorkQueueOps.

- **Extends**:
  - `docs-ghaw-orchestration-patterns.md`: The orchestration primitives (`dispatch-workflow`
    for bulk worker fan-out) are the underlying mechanism for "bulk orchestrator workflows"
    in the Assign phase. ResearchPlanAssignOps does not define new orchestration primitives;
    it uses existing ones within a named four-phase harness. The novelty is the end-to-end
    pattern, not the individual orchestration mechanisms.
  - `docs-ghaw-issueops.md`: The sub-issue hierarchy (Claim 6) and `assignees: copilot`
    (Claim 7) primitives from IssueOps are repurposed in the Plan and Assign phases of
    ResearchPlanAssignOps. This pattern extends IssueOps by placing sub-issue creation
    in the context of a research-driven, discussion-gated workflow rather than an automatic
    issue-event response.
  - `docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory` for rolling baseline persistence):
    The Research phase uses `cache-memory: true` in the same way — cross-run state
    accumulation without external infrastructure. ResearchPlanAssignOps extends the
    cache-memory pattern from audit-consumer workflows to research-discovery workflows.
  - `docs-ghaw-agentic-ops.md`: The publication-to-Discussion mechanic in the Research
    phase is the same design as Agentic Ops's durable report destination. ResearchPlanAssignOps
    extends it by making the Discussion an actionable input for the Plan phase (/plan command),
    rather than just a monitoring record.

- **Contradicts**: None. The four-phase design, sub-issue patterns, cache-memory usage,
  and assignees:copilot mechanism are all consistent with existing corpus source notes.
  No contradiction issue required.

- **Novel**:
  - **Complete four-phase end-to-end development harness as a named pattern** (Claim 1):
    No existing corpus note describes a multi-phase development lifecycle pattern that
    sequences Research, Plan, Assign, and Merge as distinct operational phases with
    defined transitions. Single-phase patterns (DailyOps, IssueOps, ChatOps) are covered;
    this multi-phase harness is new.
  - **Human decision gates at every phase transition** (Claims 2-6): The explicit design
    requirement that humans review and approve each phase transition (via /plan, via
    assignment, via PR review) is a distinct architectural stance — not fully autonomous
    and not fully manual. No existing note formalizes this three-gate human oversight
    model for a multi-phase workflow.
  - **`group: true` in `safe-outputs: create-issue:`** (Claim 9): The `group: true` field
    is not documented in any existing corpus source note. It is the first description of
    a safe-output option that automatically creates a parent-child issue hierarchy in a
    single operation.
  - **Sub-issue content requirements for AI agent consumption** (Claim 4): The four-field
    format (objective, files to touch, implementation guidance, acceptance criteria) as
    the minimum specification for a coding-agent-consumable work item is not stated in
    any existing note. IssueOps covers sub-issue structure; this pattern specifies sub-issue
    *content requirements*.
  - **The /plan command as a ChatOps trigger for Discussion→Issue workflow transition**
    (Claim 3): No existing note documents a ChatOps command that reads a Discussion and
    produces structured sub-issues. The /plan command is a new interaction pattern — a
    human-in-the-loop trigger that bridges a research artifact (Discussion) to a work
    artifact (sub-issues).
  - **Auto-close of tracking issue when all sub-issues resolve** (Claim 6): Automatic
    tracking issue closure based on sub-issue resolution state is not documented in any
    existing corpus note.
  - **go-fan as a named production reference implementation of a research workflow**
    (Claim 11): The first named production workflow in the corpus that exemplifies the
    Research phase — Go dependency monitoring as a concrete domain.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add ResearchPlanAssignOps as the canonical pattern for research-driven development
  harnesses** (Claims 1, 7): Position it in the multi-phase pattern taxonomy alongside
  WorkQueueOps (backlog processing), AgenticOps (fleet monitoring), and single-phase
  patterns (DailyOps, IssueOps). The selection criterion: use when scope is unknown
  until analysis, human prioritization is needed, or research quality is variable.
- **Add `group: true` in `safe-outputs: create-issue:` as the parent-sub-issue creation
  primitive** (Claim 9): Currently undocumented. The idiomatic plan-phase configuration
  is `group: true, max: 5, labels: [plan, ai-generated]` — add to the safe-outputs
  vocabulary.
- **Document the four-field sub-issue format as the standard for agent-ready work items**
  (Claim 4): Any issue that will be assigned to a coding agent should specify: clear
  objective, files to touch, step-by-step guidance, acceptance criteria. Frame this
  as the "agent-readable spec" requirement, distinct from human-readable issue descriptions.
- **Add the dual-path assignment mechanism** (Claim 5): Document both the manual UI path
  (few sub-issues) and the bulk orchestrator path (many sub-issues) as alternative Assign
  phase approaches. Cross-reference `docs-ghaw-orchestration-patterns.md` for the
  dispatch-workflow primitives used in bulk assignment.

### Chapter 04: Multi-Agent Orchestration

- **Add the human-in-the-loop gate model as a distinct design stance** (Claims 1-6):
  ResearchPlanAssignOps demonstrates that multi-agent workflows do not have to choose
  between fully autonomous and fully manual. Three human gates (plan trigger, assignment,
  merge review) with parallel autonomous execution in between is a concrete middle path.
  Contrast with fully autonomous pipelines (continuous deployment agents) and fully
  manual workflows (human-assisted coding without AI agents).
- **Document the Research→Discussion→Plan transition as a harness design pattern**
  (Claims 2-3): The Discussion-as-contract pattern (research publishes to Discussion,
  humans /plan to trigger issue creation) is reusable beyond ResearchPlanAssignOps.
  Any workflow where humans need to evaluate AI-generated findings before spawning
  work items can use this pattern.

### Chapter 01: Daily Workflows / Practitioner Adoption

- **Add go-fan as a concrete example of research workflow scoping** (Claim 11): Teams
  designing their first research workflow should define a specific domain of inquiry
  (like "Go dependencies") rather than a general codebase analysis. The go-fan model —
  scheduled, domain-specific, categorized Discussion output — is the reference.
- **Add the four-field sub-issue format as a checklist for issue quality** (Claim 4):
  Before assigning any issue to an AI agent, verify it specifies: (1) clear objective,
  (2) files to touch, (3) step-by-step guidance, (4) acceptance criteria. Without all
  four, the agent is likely to undershoot or overshoot the intended scope.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The `WebFetch` tool processes page content
   through an AI model before returning results. Three independent WebFetch calls were
   made to this page with different prompt framings. The opening description returned
   in two different forms across calls (Fetch 1: "four-phase workflow pattern that
   automates discovery while maintaining human oversight"; Fetch 2: "four-phase
   development pattern that moves from automated discovery to merged code with human
   control at every decision point"), confirming that the tool does not return verbatim
   text reliably. Only one passage appeared in identical form across multiple fetches
   and is cited as a direct quote: "The planner formats each sub-issue for a coding
   agent: a clear objective, the files to touch, step-by-step implementation guidance,
   and acceptance criteria." The use-case conditions (three quoted strings in Claim 7)
   appeared consistently in Fetch 2 and are cited as quotes with that caveat.

2. **URL / TaskOps naming discrepancy**: The `docs-ghaw-workqueue-ops.md` source note
   (Claim 11) references a related pattern at `/gh-aw/patterns/task-ops/` with the
   description "Research → Plan → Assign pattern." The page extracted here is at
   `patterns/research-plan-assign-ops` and covers four phases (Research → Plan → Assign
   → Merge). These may be the same page available at two URLs, or the TaskOps URL may
   be a stub pointing to this page, or the pattern was renamed from TaskOps. This
   extraction is based on the `research-plan-assign-ops` URL specified in issue #351.

3. **YAML configuration blocks**: The three YAML blocks (research, planning, assignment)
   were consistently returned across fetch passes and match the gh-aw configuration
   conventions documented in other corpus notes. They are presented as representative
   configurations, not complete workflow specs — the full frontmatter (schedule, permissions,
   etc.) was not extractable from the pattern page.

4. **go-fan workflow not separately fetched**: The go-fan reference implementation is
   named in the Phase 1 description but no separate URL was provided for it. It was not
   independently fetched. Claims about go-fan are based solely on the description on
   the pattern page.

5. **No date on the page**: Like other gh-aw documentation pages, this page does not
   carry an explicit publication date. `date_published` is set to null.

6. **No contradictions filed**: All claims are consistent with or extend existing corpus
   source notes. No existing note makes claims that materially oppose the four-phase
   pattern, sub-issue formatting requirements, or configuration vocabulary described here.
