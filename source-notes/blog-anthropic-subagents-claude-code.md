---
source_url: https://claude.com/blog/subagents-in-claude-code
source_type: blog-post
title: "How and When to Use Subagents in Claude Code"
author: Anthropic
date_published: 2026-04-07
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#204"
---

# How and When to Use Subagents in Claude Code

> Anthropic's first-party guide to subagent delegation in Claude Code —
> establishing the official quantitative thresholds (10+ files, 3+ independent
> tasks), the five-category use-case taxonomy, the full layered invocation model
> (conversational → custom agents → CLAUDE.md → skills → hooks), the `.claude/agents/`
> markdown schema with routing-critical `description` field guidance, and five
> explicit "when NOT to use" conditions — the authoritative complement to
> practitioner-derived subagent patterns in the existing corpus.

## Source Context

- **Type**: blog-post (Anthropic official blog, first-party vendor documentation
  of a shipping production feature)
- **Author credibility**: Anthropic. This is the definitive first-party account
  of subagent delegation in Claude Code — not reverse engineering, not practitioner
  synthesis. Claims about configuration schema, routing behavior, and use-case
  thresholds are authoritative for the Claude Code product as described. The post
  is noteworthy for including explicit "when NOT to use" conditions (same-file
  conflicts, small-task overhead, delegation-routing degradation from too many
  specialists) alongside the positive use-case taxonomy — a level of honesty that
  increases credibility beyond typical vendor marketing.
- **Scope**: Covers the full subagent delegation surface in Claude Code: what
  subagents are architecturally, the five-category use-case taxonomy with a
  quantitative trigger threshold, four invocation layers (conversational,
  `.claude/agents/` custom agents, CLAUDE.md policy, skills, hooks), the custom
  subagent markdown schema, routing behavior driven by the `description` field,
  UX primitives (Ctrl+B, `/tasks`), five conditions under which subagents should
  NOT be used, and practical workflow patterns. Does NOT cover: subagent cost or
  token budget details (no numbers), Agent Teams
  (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) as a separate feature, performance
  benchmarks for the built-in agent types (general-purpose, Plan, Explore), or
  the security/trust boundary model for multi-agent handoffs (covered separately
  in `blog-anthropic-claude-code-auto-mode.md`).

## Extracted Claims

### Claim 1: Subagents are isolated Claude instances with fresh context windows that return synthesized results to the main conversation — their primary engineering value is managing token accumulation in long sessions

- **Evidence**: Post architectural description: "Subagents operate as
  self-contained agents that work independently to read files, explore code, or
  make changes. They start with fresh context, unencumbered by conversation
  history." The stated benefit is "synthesized findings instead of raw content"
  and managing "token costs and context accumulation in long Claude Code sessions."
- **Confidence**: settled (first-party architectural description of shipping feature)
- **Quote**: "Subagents are isolated Claude instances with independent context
  windows that handle specific tasks and return results to the main conversation.
  They help manage token costs and context accumulation in long Claude Code sessions."
- **Our assessment**: This frames subagents primarily as a context management
  tool, not merely a parallelism primitive. The distinction matters for when to
  reach for them: the appropriate trigger is not just "can this be parallelized?"
  but also "will doing this in the main session create context bloat that degrades
  subsequent interactions?" The fresh-context benefit is that synthesis happens
  inside the subagent (which starts clean), so only the result — not the entire
  context accumulated during research — pollutes the main session. This aligns
  with the ccunpacked note's finding that the system prompt is assembled from
  CLAUDE.md + tool definitions + context + memory on every turn (Step 4 of the
  agent loop): anything that accumulates in the main session grows the input to
  every subsequent API call.

### Claim 2: The official quantitative threshold for subagent delegation is 10+ files to explore or 3+ independent tasks

- **Evidence**: Direct Anthropic recommendation with explicit numbers: "When a
  task requires exploring ten or more files, or involves three or more independent
  pieces of work, that's a strong signal to direct Claude toward subagents."
- **Confidence**: emerging (first-party recommendation; no controlled study cited
  for these specific thresholds)
- **Quote**: "When a task requires exploring ten or more files, or involves three
  or more independent pieces of work, that's a strong signal to direct Claude
  toward subagents."
- **Our assessment**: These are the first author-from-Anthropic quantitative
  signals in our corpus for subagent delegation. The Osmani note provides practitioner
  WIP limits (3-5 concurrent agents) but not a trigger threshold. The 10-file
  threshold is plausible as a heuristic: reading 10 files in the main session means
  all their contents are in context, whereas a subagent synthesizes them and returns
  only the relevant findings. The 3-independent-tasks threshold reflects parallelism
  opportunity cost: below that, subagent overhead (spawning, context setup, result
  aggregation) likely outweighs the speed benefit. Both thresholds are vendor
  recommendations rather than empirically validated boundaries — treat them as
  calibrated starting points, not hard rules.

### Claim 3: Anthropic taxonomizes five distinct use cases for subagent delegation, each with a named signal and named benefit

- **Evidence**: Five categories explicitly named in the post with specific
  signal/benefit pairs:
  1. Research-heavy tasks (signal: gathering context requires reading dozens of
     files; benefit: synthesized findings instead of raw content)
  2. Multiple independent tasks (signal: sub-tasks have no dependencies; benefit:
     parallel execution)
  3. Fresh perspective (signal: verification without conversation history
     influencing analysis; benefit: cleaner, more objective feedback)
  4. Verification before committing (signal: second opinion warranted before
     finalizing; benefit: catches issues familiarity obscures)
  5. Pipeline workflows (signal: sequential stages with clear handoffs; benefit:
     each stage receives focused attention)
- **Confidence**: emerging (vendor taxonomy; no usage frequency or effectiveness
  data cited for the categories)
- **Quote**: Not a single verbatim quote; the taxonomy is presented as a structured
  section of the post with signal/benefit pairs for each category.
- **Our assessment**: The taxonomy is notable for including two separate
  verification-oriented categories (3 and 4) alongside the more commonly discussed
  parallelism categories (1 and 2). Category 3 ("fresh perspective") makes explicit
  the anchoring-bias problem in long sessions — the main session's accumulated
  reasoning influences its own verification, which a fresh-context subagent avoids.
  Category 5 (pipeline workflows) is the formal framing of what TTal implements
  as its worker plane lifecycle (task → research → design → implement → review
  → merge → cleanup). The signal/benefit framing is directly usable as a decision
  checklist in the guide.

### Claim 4: Custom subagents are defined as markdown files in `.claude/agents/` (project-level) or `~/.claude/agents/` (user-level) with a YAML frontmatter schema

- **Evidence**: Post feature description with explicit directory paths and an
  example configuration:
  ```
  ---
  name: security-reviewer
  description: Reviews code changes for security vulnerabilities, injection
               risks, auth issues, and sensitive data exposure.
  tools: Read, Grep, Glob
  model: sonnet
  ---
  ```
  The post states these work "when a specialist should be available for automatic
  delegation and the work benefits from tightly scoped system prompts."
- **Confidence**: settled (first-party schema documentation for shipping feature)
- **Quote**: "Custom Subagents: Live in `.claude/agents/` (project-level) or
  `~/.claude/agents/` (user-level) as markdown files."
- **Our assessment**: This is the most concrete artifact in the post and the one
  most absent from existing corpus notes. The Osmani note describes subagent
  patterns without documenting the configuration schema. The ccunpacked note
  identifies the `.claude/agents/` path exists in the source map but doesn't
  document the frontmatter fields. This source provides the authoritative
  schema. The four fields (`name`, `description`, `tools`, `model`) are minimal
  and composable: `name` is the identifier, `description` drives routing,
  `tools` enforces capability scope (a read-only reviewer has `Read, Grep, Glob`
  — not `Bash`), and `model` allows per-agent model selection. The file body
  below the frontmatter becomes the subagent's system prompt — meaning custom
  agents are fully configurable specialists in a flat markdown file.

### Claim 5: The `description` field in custom subagent frontmatter is the routing primitive — specificity of trigger conditions, not capability summary, determines delegation accuracy

- **Evidence**: Post explicit guidance: "be specific about trigger conditions,
  not just capability" with a before/after contrast: "security expert" (bad) vs.
  "reviews code for security issues before commits" (good). The `description` is
  described as "how Claude decides when to auto-delegate."
- **Confidence**: emerging (first-party guidance; no controlled study of routing
  accuracy vs. description specificity cited)
- **Quote**: "The `description` field is how Claude decides when to auto-delegate
  — be specific about trigger conditions, not just capability."
- **Our assessment**: This is the most actionable design guidance in the post and
  the most novel claim relative to our corpus. The key insight: the `description`
  serves as a routing predicate, not an agent bio. "Security expert" describes
  what the agent is; "reviews code for security issues before commits" describes
  when Claude should invoke it. The mismatch explains why practitioners building
  custom agents report inconsistent auto-delegation: an agent described by capability
  ("database specialist") has no trigger signal — Claude doesn't know when to use
  it. An agent described by trigger ("reviews schema changes to ensure backwards
  compatibility") has a clear invocation condition. This principle has direct
  implications for any harness that uses `.claude/agents/`: every agent's
  description should answer "when should I be invoked?" not "what can I do?"

### Claim 6: CLAUDE.md defines delegation policies that apply to every interaction; skills are loaded on demand — they serve different structural roles and should not be conflated

- **Evidence**: Post explicit distinction: "CLAUDE.md Instructions: Defines rules
  for when Claude should delegate to specialists. Loaded at conversation start for
  consistent behavior." vs. "Skills: Reusable interfaces for complex multi-step
  workflows in `.claude/skills/`. Invoked with `/skill-name` or automatically when
  task matches description. Differs from CLAUDE.md: Skills load on demand; CLAUDE.md
  always applies."
- **Confidence**: settled (first-party definitional distinction for two shipping features)
- **Quote**: "Skills load on demand; CLAUDE.md shapes every interaction."
- **Our assessment**: This is a clarifying distinction that is missing or muddled
  in most practitioner accounts. The implication for harness design is concrete:
  CLAUDE.md is the standing policy document (always present, shapes every turn's
  system prompt per the ccunpacked agent loop Step 4); skills are on-demand procedure
  modules (loaded when invoked, not always in context). A delegation policy ("code
  reviews should always use read-only subagents") belongs in CLAUDE.md because it
  should govern every session. A multi-step research workflow belongs in a skill
  because it should be invoked explicitly rather than shaping all interactions.
  Misplacing these (a complex workflow in CLAUDE.md, a standing policy as a skill)
  degrades both context efficiency and policy reliability.

### Claim 7: Hooks are the most automated invocation layer — they execute at specific lifecycle points without conversational invocation or custom agent routing

- **Evidence**: Post description: "Hooks: User-defined shell commands, HTTP endpoints,
  or LLM prompts that execute at specific lifecycle points. Most automated approach
  for subagent orchestration." The stop hook example demonstrates a hook that blocks
  completion until tests pass.
- **Confidence**: settled (first-party description of shipping feature)
- **Quote**: "Hooks: User-defined shell commands, HTTP endpoints, or LLM prompts
  that execute at specific lifecycle points. Most automated approach for subagent
  orchestration."
- **Our assessment**: The positioning of hooks as the "most automated approach" is
  significant — it means the invocation model is explicitly layered by automation
  level: conversational (most manual) → custom agents (routing-triggered) →
  CLAUDE.md (policy-triggered) → skills (explicit invocation) → hooks (lifecycle-
  triggered, no invocation needed). The stop hook pattern is the most concrete
  example of hooks-as-quality-gates: by blocking the main agent's `Stop` lifecycle
  event until tests pass, a hook imposes a local CI gate without requiring
  the practitioner to remember to run tests manually. This maps to the meloncafe
  finding in `failure-hooks-enforcement-2k.md` that hooks provide reliable
  enforcement that CLAUDE.md prose cannot — here the enforcement is against
  session completion, not against individual tool calls.

### Claim 8: The stop hook pattern — blocking Claude's completion lifecycle event until tests pass — is a reusable quality gate for pre-commit verification

- **Evidence**: Post example: "Stop hook that blocks Claude from finishing until
  tests pass." This is presented as the concrete illustration of hooks as the
  most automated subagent orchestration approach.
- **Confidence**: emerging (first-party example; no configuration snippet published;
  no failure mode analysis)
- **Quote**: "Example: Stop hook that blocks Claude from finishing until tests
  pass." (described as a concrete use case for lifecycle hooks)
- **Our assessment**: The stop hook pattern is the first-party confirmation of the
  quality-gate hook pattern our corpus has documented from practitioner-side. The
  dadlerj tin profile (`practitioner-dadlerj-tin.md`) documents auto-commit hooks;
  the meloncafe note documents enforcement hooks. The stop hook adds a third
  pattern: completion-gate hooks that prevent session closure until a condition
  is met. The three patterns together cover the full lifecycle hook surface:
  pre-tool-call enforcement, post-session action, and pre-completion gate. The
  stop hook is also the formal implementation of the Ralph Loop's "validate before
  commit" step — the Osmani note describes this as a five-step cycle; this source
  shows the underlying hook mechanism that can enforce it automatically.

### Claim 9: Two subagents editing the same file creates conflicts — parallel subagents must be scoped to non-overlapping file sets

- **Evidence**: Post explicit "when NOT to use" condition: "Same-file edits: Two
  subagents editing one file creates conflicts."
- **Confidence**: settled (first-party caution for a concrete failure mode)
- **Quote**: "Same-file edits: Two subagents editing one file creates conflicts."
- **Our assessment**: This is a practical constraint that the Osmani note and the
  TTal note discuss at the architecture level (worktree isolation per agent) but
  neither states as a direct conflict-causing failure mode for subagents specifically.
  The implication for harness design: parallel subagent decomposition must be
  file-disjoint. This is achievable for tasks like "fix all the TypeScript errors
  across packages" (each subagent takes one package directory) but requires careful
  task decomposition for cross-cutting concerns. The TTal Worker plane's one-worktree-
  per-task design is the architectural solution to this constraint: if each worker
  has an isolated git worktree, there is no shared file system to conflict on.

### Claim 10: Too many specialist agents makes delegation less reliable — flooding Claude with options degrades routing performance

- **Evidence**: Post explicit "when NOT to use" condition: "Too many specialist
  agents: Flooding Claude with options makes delegation less reliable."
- **Confidence**: emerging (first-party caution; no measurement of degradation
  rate vs. agent count cited)
- **Quote**: "Too many specialist agents: Flooding Claude with options makes
  delegation less reliable."
- **Our assessment**: This is the inverse of the description-specificity claim
  (Claim 5): even well-described agents degrade routing quality if there are too
  many of them. The mechanism is plausible — with many specialist options, the
  routing decision itself becomes a harder problem (more candidates to evaluate),
  and the probability of a wrong delegation increases. This creates a practical
  design constraint: the `.claude/agents/` directory should contain focused,
  non-overlapping specialists with distinct trigger conditions, not a comprehensive
  library of every possible specialist. The "start with conversational prompts,
  build automation as patterns clarify" recommendation in the post is the correct
  mitigation: add a custom agent only when a pattern recurs enough to justify it,
  not preemptively for every conceivable specialization.

### Claim 11: Subagents report to the main conversation but cannot communicate with each other — tasks requiring peer coordination require agent teams instead

- **Evidence**: Post explicit "when NOT to use" condition: "Subagents need
  coordination: Subagents report to main conversation but can't communicate; use
  agent teams instead."
- **Confidence**: settled (first-party architectural description of a structural limitation)
- **Quote**: "Subagents need coordination: Subagents report to main conversation
  but can't communicate; use agent teams instead."
- **Our assessment**: This is the key architectural constraint that differentiates
  the subagent model from the Agent Teams model (which uses a shared task list for
  peer-to-peer coordination). The one-directional reporting model (subagent → main
  conversation, never subagent ↔ subagent) means parallel subagents can only be
  used for truly independent tasks. Tasks that require sequential handoffs (subagent
  A's output is subagent B's input) must either be serialized through the main
  conversation, or implemented as a pipeline where the main agent orchestrates the
  handoffs. The TTal architecture works around this via its Manager plane — the
  human-facing manager coordinates worker-to-worker handoffs because the workers
  cannot coordinate directly. This constraint also explains the 10-files / 3-tasks
  threshold: it is sized for independent tasks, not dependent ones.

### Claim 12: Built-in subagent types include general-purpose agents, Plan agents for strategic research, and Explore agents optimized for fast read-only search

- **Evidence**: Post lists three built-in types: "General-purpose agents for
  complex multi-step tasks, Plan agents that research codebases before presenting
  strategies, Explore agents optimized for fast, read-only code search."
- **Confidence**: settled (first-party enumeration of shipping feature types)
- **Quote**: "Built-in subagent types include: General-purpose agents for complex
  multi-step tasks, Plan agents that research codebases before presenting strategies,
  Explore agents optimized for fast, read-only code search."
- **Our assessment**: The three built-in types map cleanly to use cases 1, 2, and 3
  from the five-category taxonomy: Explore agents serve the research-heavy use case
  with fast read-only operations; Plan agents serve the fresh-perspective use case
  by focusing on strategy synthesis; general-purpose agents serve the multiple-
  independent-tasks and pipeline use cases. The ccunpacked note documented these
  types in the tool taxonomy (53+ tools, Agents & Tasks category) but did not
  describe their functional differentiation. This source adds the intended use case
  for each type, making the choice among built-in types clearer for practitioners.

### Claim 13: Effective conversational prompts for subagent delegation include explicit scope, explicit parallelization requests, and specified output format

- **Evidence**: Post lists natural language invocation patterns:
  - "Use a subagent to explore how authentication works"
  - "Have a separate agent review this code for security issues"
  - "Research this in parallel. Check the API routes, database models, and frontend
    components simultaneously"
  - "Spin up subagents to fix these TypeScript errors across packages"
  And prescribes: "Scope tasks clearly, request parallelization explicitly, specify
  output format (summaries vs. full contents)."
- **Confidence**: emerging (vendor best-practice recommendations; no A/B data on
  prompt patterns cited)
- **Quote**: "Scope tasks clearly, request parallelization explicitly, specify
  output format (summaries vs. full contents)."
- **Our assessment**: The three-part prescription (scope + parallelization request +
  output format) is more specific than any practitioner-derived invocation guidance
  in our corpus. The distinction between requesting "summaries" vs. "full contents"
  as output is the conversational analog of the context management benefit (Claim 1):
  asking for summaries explicitly keeps the main session clean of raw file contents.
  The four example prompts are directly copyable as invocation templates.

### Claim 14: Ctrl+B sends a running subagent to the background; `/tasks` shows all running background operations

- **Evidence**: Post as a "Pro-tip": "Ctrl+B sends subagents to background.
  `/tasks` command shows running operations."
- **Confidence**: settled (first-party UX documentation for shipping feature)
- **Quote**: "Pro-tip: Ctrl+B sends subagents to background. `/tasks` command
  shows running operations."
- **Our assessment**: These are the only two UX primitives documented in the post.
  Ctrl+B addresses the "attention management" problem in long-running subagent work:
  instead of waiting for a subagent to complete before continuing in the main
  session, the engineer can send it to the background and do other work. The
  `/tasks` command provides visibility into the running background state. Together
  they enable an asynchronous working mode: start multiple subagents, background
  them, continue in the main session, check `/tasks` periodically. This UX maps to
  the TTal "remote oversight" pattern (manage from a distance) but implemented
  natively within a single Claude Code session rather than via an external
  orchestration tool.

## Concrete Artifacts

### Custom Subagent Configuration Schema

From the post (official Anthropic schema for `.claude/agents/<name>.md`):

```markdown
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities, injection risks,
             auth issues, and sensitive data exposure.
tools: Read, Grep, Glob
model: sonnet
---

[System prompt body goes here — defines the subagent's behavior,
constraints, and output format as markdown prose]
```

**Field semantics:**
- `name`: Identifier used for direct invocation and logging
- `description`: Routing predicate — Claude reads this to decide when to auto-delegate;
  should answer "when should I be invoked?" not "what can I do?"
- `tools`: Capability scope — comma-separated list restricts which tools the
  subagent can use (e.g., a reviewer should have `Read, Grep, Glob` not `Bash` or `Edit`)
- `model`: Model selection for this agent (e.g., `sonnet`, `haiku`) — allows
  routing cheap tasks to cheaper models

**File locations:**
- Project-level: `.claude/agents/<name>.md`
- User-level: `~/.claude/agents/<name>.md`

### The Five-Layer Invocation Hierarchy

From the post's "How to Direct Subagent Usage" section — ordered from most manual to most automated:

```
Layer 1: Conversational Invocation (most manual)
  Trigger: Natural language in the prompt
  Example: "Use a subagent to explore how authentication works"
  Best for: Ad-hoc delegation; one-off tasks; exploring whether a pattern
            warrants a custom agent

Layer 2: Custom Subagents (.claude/agents/ or ~/.claude/agents/)
  Trigger: Automatic routing via `description` field match, or explicit invocation
  Best for: Recurring specialists; tasks that benefit from tightly scoped
            system prompts

Layer 3: CLAUDE.md Instructions
  Trigger: Loaded at conversation start; applies to every interaction
  Best for: Standing delegation policies ("code reviews should always use
            read-only subagents"); project-wide routing rules

Layer 4: Skills (.claude/skills/)
  Trigger: /skill-name or automatic when task description matches
  Best for: Reusable multi-step workflows (NOT standing policies — use CLAUDE.md
            for those); skills load on demand, not on every turn

Layer 5: Hooks (most automated)
  Trigger: Lifecycle events (pre-tool-call, post-sampling, stop)
  Best for: Quality gates; enforcement; automated subagent orchestration without
            conversational invocation
```

### When NOT to Use Subagents (Official Conditions)

From the post's explicit "When NOT to Use Subagents" section:

```
1. Sequential, dependent work
   Condition: Tasks form a chain where each step depends on the prior step's output
   Reason:    A single session handling the chain is cleaner than routing through
              the main conversation to coordinate dependencies

2. Same-file edits
   Condition: Two or more agents would need to modify the same file
   Reason:    Parallel edits to the same file create conflicts

3. Small tasks
   Condition: The task is simple and bounded
   Reason:    Subagent spawn overhead (context setup, result aggregation)
              outweighs the benefit for small tasks

4. Too many specialist agents in .claude/agents/
   Condition: The agents/ directory has accumulated many specialists
   Reason:    Flooding Claude with delegation options degrades routing reliability;
              maintain a focused set of non-overlapping specialists

5. Subagents need to coordinate with each other
   Condition: The work requires peer-to-peer communication between subagents
   Reason:    Subagents only report back to the main conversation — they cannot
              communicate directly; use Agent Teams for coordination-required work
```

### Five Use-Case Taxonomy with Thresholds

From the post (signal/benefit pairs plus quantitative threshold):

```
Use case          Signal                              Benefit
──────────────────────────────────────────────────────────────────────────
Research-heavy    Gathering context requires           Synthesized findings,
                  reading dozens of files              not raw file contents

Multiple          Sub-tasks have no dependencies       Parallel execution
independent       between them                         (faster completion)

Fresh perspective Verification needed without          Cleaner, unbiased
                  conversation history influence        feedback

Verification      Second opinion warranted before      Catches issues that
before commit     finalizing changes                   familiarity obscures

Pipeline          Sequential stages with clear         Each stage gets
workflows         handoffs                             focused attention

Quantitative threshold (official):
  "When a task requires exploring ten or more files, or involves three or
   more independent pieces of work, that's a strong signal to direct Claude
   toward subagents."
```

## Cross-References

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's
  post documents subagent patterns from a practitioner-synthesizer perspective
  (the Task tool, conductor → orchestrator shift, quality gates, WIP limits).
  This source is the authoritative vendor complement: same conceptual territory,
  with the concrete configuration schema and routing mechanics Osmani does not
  provide. The five-category use-case taxonomy maps directly onto Osmani's patterns:
  Research-heavy → Explore agents, Multiple independent → Task tool parallelism,
  Fresh perspective → Osmani's "two-agent review" pattern, Pipeline workflows →
  Osmani's Factory Model six-step production line. The Osmani note's WIP limit
  recommendation (3-5 concurrent agents) is directionally consistent with this
  source's "too many specialist agents degrades routing" caution.

- **Corroborates**: `blog-ccunpacked-claude-code-architecture.md` — The ccunpacked
  note documents the Agents & Tasks tool category (Agent, SendMessage, TaskCreate,
  etc.) from the leaked source map, and identifies the `.claude/agents/` path in
  the codebase. This source provides the user-facing schema for those paths and
  the intended use cases for each built-in subagent type (general-purpose, Plan,
  Explore) that ccunpacked lists in the tool taxonomy without functional description.
  Together: ccunpacked gives the internal architecture; this note gives the
  configuration surface.

- **Corroborates**: `blog-anthropic-claude-code-auto-mode.md` — The auto-mode
  note documents the security trust model for multi-agent handoffs (bidirectional
  handoff classification, outbound task review + inbound result review). This
  source is the companion piece: what subagents are and how to configure them. The
  two sources together constitute Anthropic's complete first-party guidance on
  subagent architecture: configure the delegation model here, secure the boundaries
  there. The auto-mode note's "subagents report to main conversation" architecture
  is confirmed by this source's explicit claim that "subagents can't communicate
  with each other."

- **Corroborates**: `discussion-hn-ttal-multiagent-factory.md` — TTal's two-plane
  architecture (persistent Manager + ephemeral Worker) is a practitioner solution
  to exactly the constraint this source documents: subagents cannot coordinate with
  each other, so a persistent orchestrator (the Manager plane) must handle all
  coordination. TTal's task lifecycle (task → research → design → implement →
  review → merge → cleanup) is a practitioner implementation of the Pipeline
  Workflow use case. The file-disjoint parallelism constraint (Claim 9) explains
  why TTal assigns each worker its own git worktree.

- **Corroborates**: `failure-hooks-enforcement-2k.md` — The meloncafe practitioner
  documented that lifecycle hooks provide reliable enforcement where CLAUDE.md prose
  cannot. This source's positioning of hooks as "the most automated approach for
  subagent orchestration" and the stop-hook pattern as a pre-completion quality gate
  independently validates that hooks are the correct enforcement primitive, not
  just a workaround. Both sources reach the same conclusion from different directions:
  hooks as enforcement (meloncafe) and hooks as orchestration automation (this source).

- **Extends**: `blog-addyosmani-code-agent-orchestra.md` — The Osmani note correctly
  identifies that custom agents and CLAUDE.md policy serve different purposes but
  does not clearly articulate the skills vs. CLAUDE.md distinction or the full
  five-layer invocation hierarchy. This source provides the complete hierarchy
  (conversational → custom agents → CLAUDE.md → skills → hooks) that Osmani
  describes only partially, and adds the critical structural distinction: CLAUDE.md
  always applies (standing policy); skills load on demand (invocable procedure).

- **Novel**:
  - **The five-layer invocation hierarchy** (conversational → custom agents →
    CLAUDE.md → skills → hooks, ordered by automation level) is not documented
    in any other corpus source. Existing notes describe individual layers but
    not the layered model as an architectural whole.
  - **The `description`-as-routing-predicate design principle** ("trigger conditions,
    not capability") is new to the corpus. No other source articulates this
    distinction explicitly, even though it is the key to reliable auto-delegation.
  - **The custom subagent frontmatter schema** (`name`, `description`, `tools`,
    `model` + system prompt body in `.claude/agents/<name>.md`) is documented here
    for the first time as a complete first-party schema. The ccunpacked note
    identified the directory; no prior note documents the field semantics.
  - **The explicit "when NOT to use" taxonomy** (5 conditions) is new. Osmani and
    TTal discuss failure modes implicitly; this source enumerates them explicitly
    with named conditions, making them actionable as a design checklist.
  - **The Ctrl+B / `/tasks` UX primitives** for background subagent management
    are documented here for the first time in the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the five-category use-case taxonomy as
  the decision framework for "should I use a subagent for this?" — with the
  quantitative threshold (10 files / 3 independent tasks) as the rule of thumb.
  The taxonomy's signal/benefit pairs are actionable as a checklist. Add a section
  on the "asynchronous working mode" enabled by Ctrl+B + `/tasks`: start parallel
  subagents, background them, continue in main session — this is the native
  Claude Code equivalent of TTal's remote oversight pattern.

- **Chapter 02 (Harness Engineering)**: The custom subagent schema (`.claude/agents/`
  markdown frontmatter) belongs as a concrete configuration artifact in the harness
  engineering chapter alongside CLAUDE.md and settings.json. The `description`-as-
  routing-predicate principle is the most actionable design rule for practitioners
  building custom agents: every agent description should answer "when should I be
  invoked?" Recommend adding a "description anti-pattern" callout: capability
  summaries ("database specialist") vs. trigger conditions ("reviews schema migrations
  for backwards compatibility before merging"). The "too many specialists degrades
  routing" caution should become a design constraint: maintain a focused agent
  registry, not an exhaustive one.

- **Chapter 02 (Harness Engineering)**: The five-layer invocation hierarchy
  (conversational → custom agents → CLAUDE.md → skills → hooks) provides the
  structural framework missing from current harness guidance. Current corpus
  covers CLAUDE.md, hooks, and skills individually but not as layers in an
  automation spectrum. The guide should present this as a progression: start
  conversational, formalize as custom agents when patterns repeat, elevate to
  CLAUDE.md when standing policy is needed, add skills for reusable workflows,
  add hooks for lifecycle enforcement.

- **Chapter 02 (Harness Engineering / CLAUDE.md Design)**: The skills vs. CLAUDE.md
  distinction (skills load on demand; CLAUDE.md always applies) resolves a gap in
  existing guidance. Current corpus treats both as "configuration files" without
  distinguishing structural roles. Update the harness chapter to frame CLAUDE.md
  as standing-policy-only (not a procedure library) and skills as on-demand
  procedure modules. Cross-reference with `blog-addyosmani-code-agent-orchestra.md`
  Claim 7 (LLM-generated AGENTS.md reduces success 3%, developer-written improves 4%):
  the same principle applies — CLAUDE.md should be a curated standing-policy document,
  not a dumping ground for procedures that should be in skills.

- **Chapter 03 (Safety and Verification)**: The stop hook pattern should be the
  canonical example of pre-completion quality gates. Frame it alongside the
  meloncafe enforcement-hook pattern as the two canonical lifecycle hook patterns:
  pre-tool-call enforcement (meloncafe) and pre-completion gate (this source). The
  "when NOT to use subagents" taxonomy should be extracted as a design checklist
  for multi-agent harness reviews — particularly the same-file conflict condition,
  which is the most common failure mode for practitioners who naively parallelize.

- **Chapter 04 (Context Engineering)**: The fresh-context benefit of subagents
  (Claim 1) belongs in the context engineering chapter as a concrete tool for
  managing token accumulation. The argument: if a research task accumulates 50K
  tokens of file contents in the main session, every subsequent turn pays 50K
  tokens. A subagent that synthesizes those files and returns a 2K-token summary
  keeps the main session clean. This is the context-budget argument for subagent
  delegation — separate from the parallelism argument — and gives practitioners
  a second reason to delegate that is independent of whether the tasks are
  parallelizable.

## Extraction Notes

- **Source depth**: This is a blog post (not a full technical reference or
  documentation page). Content is concise — roughly 1,500 words. The claim density
  is high for the word count, but practitioners seeking full configuration
  documentation (e.g., complete list of hook lifecycle events, full tool names
  valid in the `tools` field) will need to consult the official Claude Code
  documentation directly. The post is a high-quality introduction and decision
  guide, not an exhaustive reference.
- **No sub-pages followed**: The post does not link to substantive sub-pages.
  The Claude Code documentation (docs.anthropic.com/claude-code) is referenced
  implicitly but not linked within the post itself.
- **Vendor documentation editorial note**: Per guide editorial tenet #8, vendor
  documentation is authoritative on "what exists" and "how to configure it"
  but should be supplemented by practitioner evidence for "does it work as
  described in practice." The quantitative thresholds (10 files, 3 tasks),
  the `description` routing accuracy claims, and the routing degradation claim
  from too many agents are all vendor recommendations without independent
  practitioner validation in the current corpus. The schema fields and UX
  primitives are factual (the feature ships as described).
- **Relationship to auto-mode note**: The post does not discuss security,
  trust boundaries, or the safety model for subagent handoffs. Those are covered
  in `blog-anthropic-claude-code-auto-mode.md`. A Smith synthesizing Chapter 02
  should read both together: this note for the configuration and delegation model,
  the auto-mode note for the security architecture at subagent interfaces.
- **Prospector alignment**: The three Prospector triage comments identified
  partially overlapping extraction targets; this extraction synthesizes all three
  perspectives. The first triage's "official taxonomy" and "custom subagent schema"
  targets are fully extracted. The second triage's "when NOT to spawn" conditions
  and "fresh review pattern" are fully extracted. The third triage's "decision
  thresholds" and "routing logic" targets are fully extracted. All Prospector
  extraction targets were found in the source.
