---
source_url: https://github.github.com/gh-aw/patterns/task-ops
source_type: docs
title: "GitHub Agentic Workflows: TaskOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#354"
---

# GitHub Agentic Workflows: TaskOps Pattern

> Three-phase (Research → Plan → Assign) scaffolded pattern for systematic
> code improvement workflows where a developer gates each phase transition —
> the corpus's first named pattern where developer oversight is an explicit
> architectural requirement at multiple handoff points, not just a final review.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/task-ops` page —
  in the `patterns/` section alongside ExpertOps, DailyOps, Agentic Ops,
  Orchestration, and other named patterns. Patterns pages are practitioner
  implementation references, not conceptual overviews or API references.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's "Agent Factory" blog series and the
  `gh aw` CLI. The two documented examples (Static Analysis and Duplicate Code
  Detection) are described as concrete implementations rather than hypotheticals.
  Claims about the three-phase structure and customization axes are authoritative
  for the `gh aw` platform; generalizability beyond gh-aw is a design pattern
  claim that benefits from additional evidence.
- **Scope**: Covers the TaskOps design pattern — the three-phase Research →
  Plan → Assign structure, when to apply it, two concrete examples with specific
  tooling (zizmor/poutine/actionlint for static analysis; Serena MCP for
  semantic duplicate detection), the five customization axes, and limitations.
  Does NOT cover: the Safe Outputs permission model in general (see
  `docs-ghaw-how-they-work.md`), the IssueOps sub-issue hierarchy pattern for
  task decomposition (see `docs-ghaw-issueops.md`), the orchestration fan-out
  mechanisms (see `docs-ghaw-orchestration-patterns.md`), or fleet-level agent
  monitoring (see `docs-ghaw-agentic-ops.md`).

## Extracted Claims

### Claim 1: TaskOps is a three-phase Research → Plan → Assign pattern for systematic, developer-overseen code improvement workflows

- **Evidence**: The page defines the pattern through three named phases, each
  with a distinct agent role and a developer gate between phases. The developer
  reads the research report before invoking the planner, and reviews generated
  issues before assigning to Copilot. The pattern is formally named and listed
  in the `patterns/` section alongside other named gh-aw patterns.
- **Confidence**: settled (first-party documentation; the three-phase structure
  is explicit and named)
- **Quote**: (no single sentence spans all three phases; see Phase descriptions
  in Claims 2–4 and Concrete Artifacts)
- **Our assessment**: TaskOps is architecturally distinct from other gh-aw
  patterns because developer agency is not just a final gate (reviewing a PR
  before merge) but is embedded at two internal transitions: Research → Plan
  and Plan → Assign. This makes it a "human-in-the-loop at every phase"
  pattern rather than a "human reviews output" pattern. For Ch02 (Harness
  Engineering): position TaskOps in the harness trigger taxonomy as the
  "investigation-before-action" pattern — distinct from IssueOps (event-driven,
  largely automatic), DailyOps (scheduled, largely automatic), and ChatOps
  (human-initiated per session).

### Claim 2: The Research phase uses a scheduled agent to investigate the repository "under a specific angle" and generate a comprehensive report

- **Evidence**: Phase 1 description from the page, confirmed across multiple
  fetch passes.
- **Confidence**: settled (first-party documentation)
- **Quote**: "A research agent (typically scheduled daily or weekly) investigates
  the repository under a specific angle and generates a comprehensive report."
- **Our assessment**: The "specific angle" phrasing is architecturally significant:
  each TaskOps research agent is scoped to a single investigative focus (security,
  duplication, performance, etc.) rather than a general code review. This scoping
  makes the agent's output more predictable and the developer's review more tractable.
  The "typically scheduled daily or weekly" framing places this in the DailyOps
  scheduling category — the research agent runs on a cron, not on an event trigger.
  For Ch02: the research agent is a DailyOps-style scheduled workflow whose output
  is a human-readable artifact (report/discussion) rather than a direct code change.

### Claim 3: The Plan phase requires developer review of research findings before a planner agent converts them into specific, actionable issues

- **Evidence**: Phase 2 description from the page, confirmed across multiple
  fetch passes.
- **Confidence**: settled (first-party documentation)
- **Quote**: "The developer reviews the research report to determine if worthwhile
  improvements were identified. If the findings merit action, the developer invokes
  a planner agent to convert the research into specific, actionable issues."
- **Our assessment**: This is the first of two developer gates. The developer
  is not just reviewing AI output — they are making a binary decision (do these
  findings merit action?) and actively invoking the next agent if so. The
  "invokes a planner agent" language suggests a ChatOps-style `/plan` command
  (confirmed by the Static Analysis example). The planner agent's output is not
  code changes but structured GitHub issues — work items for the next phase.
  For Ch01 (Daily Workflows): document the developer's Phase 2 action as a
  specific workflow step: read the research discussion, then if findings are
  actionable, invoke the planner with a command such as `/plan`. This is a
  named human action, not just "review the output."

### Claim 4: The Assign phase gates on developer review of generated issues before approved issues are dispatched to Copilot for implementation (sequentially or in parallel)

- **Evidence**: Phase 3 description from the page, confirmed across multiple
  fetch passes.
- **Confidence**: settled (first-party documentation)
- **Quote**: "The developer reviews the generated issues and decides which ones
  to execute. Approved issues are assigned to Copilot for automated implementation
  and can be executed sequentially or in parallel depending on dependencies."
- **Our assessment**: This is the second developer gate. The developer curates
  the planner's output — not all generated issues must be executed. The
  "sequentially or in parallel depending on dependencies" framing is important:
  TaskOps does not prescribe execution order; practitioners must identify
  dependency relationships and configure accordingly. This is where the
  orchestration patterns from `docs-ghaw-orchestration-patterns.md` come in —
  parallel dispatch uses `dispatch-workflow` or sub-issue `assignees: copilot`.
  For Ch04 (Pattern Selection): TaskOps delegates execution coordination to
  the practitioner; the pattern provides gates and structure, not an execution
  engine.

### Claim 5: TaskOps applies when systematic investigation is required before action, when findings vary in priority, or when work needs structured decomposition for optimal agent execution

- **Evidence**: The "When to Use TaskOps" section, confirmed verbatim across
  multiple fetch passes.
- **Confidence**: settled (first-party; explicit applicability criteria)
- **Quote**: "Use this strategy when code improvements require systematic
  investigation before action, work needs to be broken down for optimal AI
  agent execution, or when research findings may vary in priority and require
  developer oversight at each phase."
- **Our assessment**: The three applicability conditions map to distinct
  scenarios: (1) "systematic investigation before action" — the improvement
  target is not self-evident; a research pass is needed to find it; (2) "broken
  down for optimal AI agent execution" — the work is too large or vague for a
  single agent; (3) "findings may vary in priority" — not all findings are worth
  acting on; human triage is needed. Condition 3 is the key differentiator from
  purely automated patterns: when the research output quality is unpredictable,
  TaskOps's human gates prevent low-quality findings from generating noise in
  the issue tracker. For Ch04: this three-condition rubric is the decision test
  for choosing TaskOps over automated alternatives (e.g., Agentic Ops for
  monitoring, DailyOps for routine automated actions).

### Claim 6: The Static Analysis example demonstrates a daily security scan using zizmor, poutine, and actionlint, publishing clustered findings to a GitHub Discussion with severity assessment and fix prompts

- **Evidence**: The "Example: Static Analysis → Plan → Fix" section, confirmed
  across multiple fetch passes.
- **Confidence**: settled (first-party; concrete example with named tools)
- **Quote**: "Runs daily to scan all agentic workflows with security tools
  (zizmor, poutine, actionlint), creating a comprehensive security discussion
  with clustered findings by tool and issue type, severity assessment, fix
  prompts, and historical trends."
- **Our assessment**: This example establishes that TaskOps's Research phase
  can invoke specialized static analysis tools — not just general AI reasoning.
  The research agent uses `static-analysis-report.md` and invokes external
  tools (zizmor for GitHub Actions-specific security, poutine for supply chain
  security, actionlint for Actions syntax) to generate structured findings.
  Publishing to a GitHub Discussion (not an issue) is notable: the Discussion is
  a durable, human-readable artifact that persists independently of action taken.
  The Plan phase is triggered by a developer `/plan` command. For Ch02: this
  is the cleanest example of a TaskOps harness: research workflow → Discussion
  artifact → developer `/plan` → issue generation → developer assigns to Copilot.

### Claim 7: The Duplicate Code Detection example uses Serena MCP for semantic code analysis, auto-assigning generated issues to Copilot via `assignees: copilot` in the workflow config

- **Evidence**: The "Example: Duplicate Code Detection → Plan → Refactor"
  section, confirmed across multiple fetch passes.
- **Confidence**: settled (first-party; concrete example with named MCP)
- **Quote**: "Runs daily using Serena MCP for semantic code analysis to identify
  exact, structural, and functional duplication. Creates one issue per distinct
  pattern (max 3 per run) that are assigned to Copilot (via `assignees: copilot`
  in workflow config)."
- **Our assessment**: Two findings in this example merit attention: (1) Serena
  MCP is used for semantic analysis — this is the first mention of Serena in a
  GHAW pattern page, confirming MCPs as a first-class capability for research
  agents that need domain-specific analysis tools beyond what GitHub's built-in
  toolset provides. (2) The `assignees: copilot` assignment is pre-configured in
  the workflow rather than applied by the developer after review — this is the
  "mixed" assignment mode from the Customization section. The `max 3 per run`
  cap prevents the issue queue from being flooded with duplication findings.
  For Ch02: note the `max:` pattern on issue creation as a volume-control
  mechanism parallel to `max:` on Safe Outputs comments.

### Claim 8: TaskOps has four documented limitations: longer cycle time than direct execution, false-positive findings, multi-phase coordination overhead, and specialized MCP dependencies for research agents

- **Evidence**: The "Limitations" section, confirmed verbatim across multiple
  fetch passes.
- **Confidence**: settled (first-party; explicit limitations listed)
- **Quote**: "The three-phase approach takes longer than direct execution and
  requires developers to review research reports and generated issues. Research
  agents may flag issues that don't require action (false positives), and multiple
  phases require workflow coordination and clear handoffs. Research agents often
  need specialized MCPs (Serena, Tavily, etc.)."
- **Our assessment**: The four limitations form a coherent adoption cost picture:
  (1) Time cost: three phases with human reviews is slower than a single automated
  pass. (2) False positive cost: the developer must filter noise from the research
  output — this is the core value-add of the Plan phase gate, but also its overhead.
  (3) Coordination cost: multi-phase workflows require clear naming conventions,
  handoff artifacts, and trigger mechanisms between phases. (4) Tooling cost:
  high-quality research (especially semantic analysis) requires MCPs like Serena
  that may not be available out of the box. For Ch04: these four limitations are
  the selection criteria for NOT using TaskOps — when speed matters, when research
  quality is uniformly high, or when no specialized MCPs are available, simpler
  automated patterns (Agentic Ops, DailyOps) may be more appropriate.

### Claim 9: TaskOps offers a five-axis customization space: research focus, frequency, report format, planning approach, and assignment method

- **Evidence**: The "Customization" section, confirmed verbatim across multiple
  fetch passes.
- **Confidence**: settled (first-party; five axes explicitly enumerated)
- **Quote**: "Adapt the TaskOps strategy by customizing the research focus
  (static analysis, performance metrics, documentation quality, security, code
  duplication, test coverage), frequency (daily, weekly, on-demand), report
  format (discussions vs issues), planning approach (automatic vs manual), and
  assignment method (pre-assign via `assignees: copilot` in workflow config,
  manual assignment through GitHub UI, or mixed)."
- **Our assessment**: The five customization axes define the configuration space
  for TaskOps deployments. Most axes are straightforward, but the assignment
  method axis is notable: practitioners can fully automate the Assign phase (all
  issues auto-assign to Copilot), keep it manual (developer assigns via GitHub
  UI after review), or mix (some issue types auto-assign, others require manual
  selection). The "automatic vs manual" planning approach axis is less well-defined
  in the source — it likely refers to whether the planner agent runs automatically
  on discussion creation or requires a developer `/plan` command. For Ch04:
  this customization matrix is a design aid for adapting TaskOps to different
  team risk tolerances and automation preferences.

### Claim 10: TaskOps is positioned among three related strategies: Orchestration (multiple TaskOps cycles toward shared goals), Threat Detection (continuous monitoring without planning phase), and Custom Safe Outputs (custom actions for the plan phase)

- **Evidence**: The "Related Strategies" section from the page.
- **Confidence**: emerging (strategy names are listed without detailed descriptions
  of their relationships)
- **Quote**: (no single verbatim sentence covers all three; the section names
  "Orchestration," "Threat Detection," and "Custom Safe Outputs" with brief
  descriptions)
- **Our assessment**: The "Threat Detection" related strategy is architecturally
  significant — it is described as "continuous monitoring without planning phase,"
  suggesting a variant of TaskOps that removes the human Plan gate and runs the
  research-to-action pipeline automatically for security-critical findings.
  This is not currently documented in the corpus as a named pattern. The
  "Orchestration" connection suggests that multiple TaskOps research cycles can
  feed a shared goal via the orchestrator/worker pattern. For Ch04: note that
  TaskOps and Threat Detection are variants of the same research-based architecture
  distinguished by whether a human gate exists between research and action.

## Concrete Artifacts

### Three-Phase Pattern Structure

```
TaskOps Pattern — Three Phases (from patterns/task-ops page)

Phase 1: Research
  Agent type: scheduled research agent (DailyOps-style)
  Trigger:    cron schedule (daily or weekly)
  Output:     comprehensive report (GitHub Discussion or issue)
  Human gate: developer reads report; decides if findings merit action
  Quote:      "A research agent (typically scheduled daily or weekly)
               investigates the repository under a specific angle and
               generates a comprehensive report."

Phase 2: Plan
  Agent type: planner agent (invoked on demand)
  Trigger:    developer invokes (e.g., /plan ChatOps command)
  Output:     specific, actionable GitHub issues with clear objectives
               and acceptance criteria
  Human gate: developer reviews generated issues; selects which to execute
  Quote:      "If the findings merit action, the developer invokes a planner
               agent to convert the research into specific, actionable issues."

Phase 3: Assign
  Agent type: Copilot (implementation)
  Trigger:    developer assigns approved issues to Copilot
  Output:     pull requests implementing the approved issues
  Options:    sequential or parallel execution depending on dependencies
  Quote:      "Approved issues are assigned to Copilot for automated
               implementation and can be executed sequentially or in
               parallel depending on dependencies."
```

*Source: GitHub Agentic Workflows `patterns/task-ops` page, "How TaskOps Works" section*

### Example 1: Static Analysis → Plan → Fix

```
Example: Static Analysis Security Workflow

Research agent:  static-analysis-report.md
Schedule:        daily
Tools:           zizmor, poutine, actionlint (security scanning tools)
Output:          GitHub Discussion with:
                   - findings clustered by tool and issue type
                   - severity assessment
                   - fix prompts
                   - historical trends

Plan trigger:    developer reviews discussion, invokes /plan command
Plan output:     specific issues for each actionable finding

Assign:          developer selects issues to assign to Copilot
Implementation:  Copilot opens PRs for each assigned fix
```

*Source: GitHub Agentic Workflows `patterns/task-ops` page,
"Example: Static Analysis → Plan → Fix" section*

### Example 2: Duplicate Code Detection → Plan → Refactor

```
Example: Semantic Duplicate Code Detection Workflow

Research agent:  duplicate-code-detector.md
Schedule:        daily
Tools:           Serena MCP (semantic code analysis)
Detection types: exact duplication, structural duplication, functional duplication
Output:          GitHub Issues (max 3 per run, one per distinct pattern)
Assignment:      pre-assigned to Copilot via `assignees: copilot` in workflow config

Plan trigger:    (implicit — issues created directly by research agent)
Assign:          automatic via workflow config (mixed mode)
Implementation:  Copilot opens PRs for refactoring each identified pattern
```

*Source: GitHub Agentic Workflows `patterns/task-ops` page,
"Example: Duplicate Code Detection → Plan → Refactor" section*

### Customization Matrix

```
Customization axis | Options
-------------------|--------------------------------------------------------
Research focus     | static analysis, performance metrics, documentation
                   | quality, security, code duplication, test coverage
Frequency          | daily, weekly, on-demand
Report format      | discussions (durable, async) vs. issues (actionable, tracked)
Planning approach  | automatic vs. manual (developer invokes planner)
Assignment method  | pre-assign (assignees: copilot in workflow config)
                   | manual (developer assigns via GitHub UI)
                   | mixed (some auto, some manual by issue type)
```

*Source: GitHub Agentic Workflows `patterns/task-ops` page, "Customization" section*

### Limitations Summary

```
Four documented limitations of the TaskOps pattern:

1. Longer cycle time
   "The three-phase approach takes longer than direct execution and
    requires developers to review research reports and generated issues."

2. False positives
   "Research agents may flag issues that don't require action (false positives)"
   Implication: human Plan gate is necessary to filter noise; without it,
   low-quality findings generate issue tracker noise.

3. Multi-phase coordination overhead
   "Multiple phases require workflow coordination and clear handoffs."
   Implication: naming conventions, trigger mechanisms, and artifact formats
   must be consistent across research → plan → assign workflows.

4. Specialized MCP dependencies
   "Research agents often need specialized MCPs (Serena, Tavily, etc.)"
   Implication: high-quality research requires tools beyond GitHub's built-in
   toolset; MCP setup is a prerequisite for some TaskOps deployments.
```

*Source: GitHub Agentic Workflows `patterns/task-ops` page, "Limitations" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): TaskOps is the most fully-realized instantiation of this principle
    in the corpus — not just one approval gate but two embedded developer gates
    (Plan: developer decides whether to invoke planner; Assign: developer decides
    which issues to execute). While Claim 10 names the pattern as a design option,
    TaskOps makes it structural to the pattern itself.
  - `docs-ghaw-issueops.md` Claim 7 (`assignees: copilot` for parallel execution):
    The Duplicate Code Detection example uses `assignees: copilot` in the same way
    IssueOps documents it — as the mechanism for routing GitHub issues to Copilot
    for automated execution. Both sources confirm `assignees: copilot` as a
    first-class dispatch mechanism, not just a convenience feature.
  - `docs-ghaw-how-they-work.md` Claim 8 ("Continuous AI" as systematic automated
    application of AI to software collaboration): TaskOps is a concrete implementation
    of two of the four Continuous AI use cases named there: "incremental code quality
    improvement" (via static analysis and duplicate detection) and "documentation
    currency maintenance" (documentation quality is listed as a research focus
    option in the Customization section).

- **Extends**:
  - `docs-ghaw-agentic-ops.md` (Agentic Ops monitors agent infrastructure via
    scheduled workflows + escalation): TaskOps applies a structurally similar
    scheduled-research-then-action model to code quality rather than agent fleet
    monitoring. Agentic Ops is observe-classify-report (no developer Plan gate);
    TaskOps is research-plan-fix (two developer gates). Together they show the
    same research-first architectural approach applied at different scopes:
    agent fleet health (Agentic Ops) vs. codebase quality (TaskOps).
  - `docs-ghaw-orchestration-patterns.md` Claims 2 and 4 (`dispatch-workflow`
    fan-out and decision framework): The TaskOps Assign phase — "executed
    sequentially or in parallel depending on dependencies" — delegates to the
    orchestration patterns for the parallel case. TaskOps adds the human planning
    gate before orchestration; the dispatch mechanism itself is documented in the
    orchestration patterns note.
  - `docs-ghaw-mcps.md` (MCP integration): Claim 7 here introduces Serena MCP
    as a concrete research tool for semantic code analysis. This is a specific
    example of domain-specialized MCP use not previously documented in the GHAW
    pattern corpus.

- **Contradicts**: None identified. No existing source note makes claims that
  materially oppose the three-phase structure, developer gate model, or tool
  usage described here. The IssueOps note (`docs-ghaw-issueops.md` Claim 7)
  uses `assignees: copilot` consistently with the Duplicate Code Detection
  example. No contradiction issue filed.

- **Novel**:
  - **Three-phase human-gated pattern (Research → Plan → Assign) as a named
    architectural type**: No existing source note documents a gh-aw pattern where
    developer oversight is required at two internal phase transitions, not just
    at final review. TaskOps is the first corpus entry where "human reviews
    findings and decides to proceed" is a structural requirement of the pattern,
    not just a best practice recommendation.
  - **Planner agent as an intermediate agent specialized for issue generation**:
    No prior corpus source describes an agent whose role is specifically to
    convert research findings into structured GitHub issues. The planner agent is
    a distinct agent type from research agents (which investigate and report) and
    implementation agents (which write code).
  - **Research agent publishing to GitHub Discussion as a human-readable handoff
    artifact**: While Agentic Ops and DailyOps publish to Discussions, TaskOps
    specifically uses the Discussion as the artifact that triggers the developer's
    Plan phase decision. The Discussion is not just a report but a structured
    decision surface.
  - **Serena MCP for semantic code analysis in a scheduled gh-aw workflow**
    (Claim 7): First corpus mention of Serena MCP in a patterns-page context.
    Confirms semantic code analysis tools as a viable research instrument for
    TaskOps.
  - **Threat Detection as a named TaskOps variant without the Plan gate**
    (Claim 10): The "Related Strategies" section names Threat Detection as
    "continuous monitoring without planning phase" — effectively an automated
    TaskOps where the developer Plan gate is removed for security-critical findings.
    This variant pattern is not documented elsewhere in the corpus.
  - **Five-axis customization matrix for research-based workflows** (Claim 9):
    The explicit enumeration of research focus, frequency, report format,
    planning approach, and assignment method as independent customization dimensions
    is a design space formalization not documented in any other GHAW pattern note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add TaskOps to the trigger taxonomy as the "investigation-before-action"
  pattern** (Claims 1–5): The guide's trigger taxonomy currently covers
  event-driven (IssueOps), human-initiated per-session (ChatOps), scheduled-automatic
  (DailyOps), and label-change (LabelOps) triggers. TaskOps adds a fifth type:
  scheduled-research with developer-gated progression. The key distinguishing
  property: the agent's first-phase output is a human-readable artifact (Discussion
  or issues) designed to inform a developer decision, not to directly execute a change.

- **Document the planner agent as a specialized intermediate agent type** (Claim 3):
  Ch02 covers research agents and implementation agents. The planner agent —
  converting research findings into structured GitHub issues — is a third agent
  role specific to multi-phase patterns. Practitioners implementing TaskOps must
  author both a research workflow and a planner workflow with complementary
  artifact formats (research output → planner input).

- **Document `assignees: copilot` at the workflow config level as distinct from
  developer-assigned dispatch** (Claim 7): In the Duplicate Code Detection example,
  `assignees: copilot` is set in the workflow configuration rather than applied by
  the developer. This is the "pre-assign" mode in the Customization section —
  issues are auto-assigned to Copilot on creation, bypassing the developer Assign
  gate. Practitioners should understand this is a configuration choice that trades
  control for automation speed.

### Chapter 04: Pattern Selection and Implementation

- **Add TaskOps to the pattern selection decision guide** (Claim 5): When does
  a team choose TaskOps over simpler automated patterns?
  - TaskOps: when research quality is unpredictable (findings vary in priority),
    when systematic investigation is needed before knowing what to fix, or when
    the work must be decomposed for optimal agent execution.
  - Agentic Ops / DailyOps: when research quality is reliable and automatic
    action is safe (monitoring with known thresholds, routine maintenance).
  The four limitations (Claim 8) are the selection cost — teams choosing TaskOps
  must accept longer cycle time, false-positive filtering overhead, coordination
  complexity, and potential MCP dependencies.

- **Document the TaskOps vs. Threat Detection trade-off** (Claim 10): TaskOps
  keeps the developer Plan gate for human oversight. Threat Detection (a named
  related strategy in the source) removes the Plan gate for security-critical
  findings that require immediate action. Teams should make an explicit choice:
  which research-to-action flows are safe to automate fully, and which require
  human triage?

- **Add the five-axis customization matrix as a design aid** (Claim 9): When
  implementing a TaskOps workflow, practitioners must make five design decisions
  (research focus, frequency, report format, planning approach, assignment method).
  The guide should present these as the configuration surface for adapting the
  pattern to team preferences and risk tolerances.

### Chapter 01: Daily Workflows

- **Document the developer's TaskOps workflow as three named touchpoints** (Claims
  2–4): In a TaskOps-enabled repository, the developer's daily workflow includes:
  (1) Read the research agent's report/discussion (Phase 2 gate: decide if findings
  merit action); (2) If yes, invoke the planner (e.g., `/plan`); (3) Review
  generated issues and assign approved ones to Copilot (Phase 3 gate). These are
  named developer actions, not passive reviews. The guide should frame TaskOps as
  a developer workflow pattern, not just an automation pattern.

## Extraction Notes

1. **Source is an Astro/Starlight-rendered SPA**: Like other gh-aw documentation
   pages, this page renders via JavaScript. WebFetch returns processed text rather
   than raw source. Four independent WebFetch calls were made across two sessions;
   consistent passages are cited as verbatim quotes. Passages that appeared in
   variant forms across calls are paraphrased in the Our Assessment sections, not
   cited as quotes.

2. **No YAML workflow examples on the pattern page**: Unlike some gh-aw patterns
   pages (e.g., ProjectOps, IssueOps), the TaskOps page does not appear to contain
   complete YAML frontmatter examples. The pattern descriptions reference specific
   workflow files (`static-analysis-report.md`, `duplicate-code-detector.md`) that
   are presumably in a reference implementation repository, but these were not
   linked from the extractable content. Claims about specific workflow configurations
   are based on the prose descriptions, not YAML artifacts.

3. **Reference implementation not located**: Unlike Agentic Ops (which links to
   `githubnext/agentic-ops`), the TaskOps page does not appear to provide a
   reference implementation repository link in the extractable content. The two
   example workflow files (`static-analysis-report.md`, `duplicate-code-detector.md`)
   may be in the `gh-aw` repository itself or in a separate reference repo; this
   could not be confirmed via WebFetch.

4. **"Planner agent" and the Plan phase trigger mechanism**: The Phase 2 description
   says the developer "invokes a planner agent" and the Static Analysis example
   mentions a `/plan` command, consistent with a ChatOps trigger. However, the
   Customization section lists "automatic vs manual" as a planning approach axis.
   Whether "automatic" means the planner agent fires on Discussion creation (DailyOps-
   style) or on issue creation, or via another trigger, is not specified in the
   extractable content. Claims about the planner trigger default to the manual
   (`/plan` command) case, which is the documented example.

5. **No contradictions filed**: Reviewed all existing source notes against the
   claims extracted here. No claims in this source materially oppose existing source
   notes at the MINER.md §4a threshold. The `assignees: copilot` usage is consistent
   with `docs-ghaw-issueops.md` Claim 7. The human approval gate pattern is consistent
   with `docs-ghaw-how-they-work.md` Claim 10. No contradiction issue filed.

6. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   gh-aw platform state as of 2026-05-10, based on tooling references (Serena MCP,
   zizmor, poutine, actionlint) matching current ecosystem tools.
