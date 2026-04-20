---
source_url: https://claude.com/blog/seeing-like-an-agent
source_type: blog-post
title: "Seeing like an agent: how we design tools in Claude Code"
author: Thariq Shihipar (Anthropic, Claude Code team)
date_published: 2026-04-10
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#250"
---

# Seeing like an agent: how we design tools in Claude Code

> First-party Anthropic post by a Claude Code engineer documenting the iteration history
> behind three specific tool design decisions — AskUserQuestion, TodoWrite→Task, and
> RAG→Grep→progressive disclosure — as evidence for the "see like an agent" design principle:
> match tool granularity to model ability, not to human intuition.

## Source Context

- **Type**: blog-post (claude.com/blog, April 2026)
- **Author credibility**: Thariq Shihipar is a member of technical staff at Anthropic working
  on Claude Code. This is a first-party account from inside the build team, not a practitioner
  write-up. Claims about why tool designs failed or succeeded reflect direct observation of
  model behavior during development, not external inference. Highest-credibility source for
  Claude Code tool design intent.
- **Scope**: Three concrete case studies of iterative tool design within Claude Code, plus
  the "see like an agent" meta-principle. Covers: the three failed/revised attempts at
  AskUserQuestion elicitation, the TodoWrite→Task capability-driven evolution, and the
  RAG→Grep→progressive disclosure search evolution. Does NOT cover tool pricing, CLAUDE.md
  authoring, safety/permission design, or multi-agent safety. The ~20-tool count is mentioned
  as the current stable plateau, not a hard limit. Article is ~5 minutes reading time.

## Extracted Claims

### Claim 1: Adding a questions parameter to an existing tool (ExitPlanTool) failed because it sent conflicting signals — the model couldn't determine whether to produce a plan, ask questions, or both simultaneously

- **Evidence**: Direct observation by the author during Claude Code development. The model
  received a tool call contract that said "provide a plan AND optionally provide questions about
  that plan in the same call." The ambiguity about whether to call the tool twice (once for
  questions, once for the plan) was the observable failure mode.
- **Confidence**: settled (first-party author observation with specific failure mechanism named)
- **Quote**: (paraphrased from article) Claude received conflicting signals — asked simultaneously
  for both a plan and questions about that plan. Raised ambiguity about whether Claude needed to
  call the tool twice.
- **Our assessment**: This documents a named failure mode for tool parameter overloading: when a
  single tool is asked to produce structurally different kinds of output in the same call, the
  model doesn't reliably know which path to take. The failure was not about capability — Claude
  could understand both instructions — but about disambiguation. The signal was noisy.

### Claim 2: Asking the model to produce a custom markdown output format (bullet-point questions with bracketed alternatives) also failed — the model appended extra sentences, dropped options, or abandoned the structure entirely

- **Evidence**: Author's direct observation during Claude Code development. The format was
  intended to be parsed programmatically into a UI. Failure modes were: extra narrative text
  appended after the structured block, options within the format dropped, the structure abandoned
  partway through the response.
- **Confidence**: settled (first-party observation; specific failure modes named)
- **Quote**: (paraphrased) Claude didn't reliably produce this format — it appended extra
  sentences, dropped options, or abandoned the structure entirely.
- **Our assessment**: This is the standard "format instruction in system prompt is unreliable for
  structured elicitation" finding. Attempting to get structured output from natural language
  instructions produces brittle results, especially when the model has learned to write prose and
  must fight that tendency to stay in format. This failure is widely documented in practitioner
  experience; this source adds first-party confirmation of the failure mode from the team that
  builds Claude.

### Claim 3: A dedicated AskUserQuestion tool — one the model calls at any point, which triggers a modal blocking the agent loop until the user answers — succeeded where the previous two approaches failed

- **Evidence**: Described as the successful third iteration. The mechanism: calling the tool
  blocks the agent loop and opens a modal UI. The model learned to call it reliably because the
  tool had a single, unambiguous purpose. The author notes "Claude seemed to like calling this
  tool" as a positive signal that the tool design matched how the model wanted to operate.
- **Confidence**: settled (first-party description of a shipped Claude Code feature)
- **Quote**: "Claude seemed to like calling this tool" (cited as a practitioner evaluation signal)
- **Our assessment**: "Claude seemed to like calling this tool" is the key evaluative heuristic
  from this case study. It is not a rigorous metric, but it is an observable signal: when tool
  call rate increases without explicit prompting, that is evidence the tool design matches the
  model's mental model of when to use it. This is a practitioner technique worth naming: monitor
  voluntary tool call frequency as a signal of tool-model fit.

### Claim 4: A structured dedicated tool outperforms format instructions for elicitation because the tool call contract provides an unambiguous, typed channel for structured output

- **Evidence**: The three-attempt AskUserQuestion story is the evidence. The first two attempts
  used in-band mechanisms (parameters, format instructions); the third used an out-of-band typed
  tool call. Only the third worked reliably.
- **Confidence**: settled (three-attempt iteration story with first-party authorship)
- **Quote**: (implied by the three-attempt story) The dedicated tool provides a clear, unambiguous
  signal to the model about when and how to ask questions.
- **Our assessment**: The principle generalizes beyond question-asking: any time the harness needs
  the model to produce a specific structured output on demand, a dedicated tool call with typed
  arguments is more reliable than format instructions in the prompt. The mechanism is that tool
  call contracts are harder to violate than prose format instructions — the model either calls the
  tool with conforming arguments or it does not call it. There is no partial compliance.

### Claim 5: System reminders injected every 5 turns to keep the model on track with a todo list caused Opus 4.5 to treat the list as a rigid constraint rather than a flexible guide

- **Evidence**: Author's direct observation during Claude Code development with the TodoWrite
  tool. The 5-turn system reminder frequency is specific. The failure mode: as Claude's
  capabilities improved, the reminders led it to stick to the original list even when
  circumstances changed and plan modification was appropriate.
- **Confidence**: settled (first-party observation with specific mechanism named: 5-turn
  reminder cadence, and specific failure mode: treating list as constraint)
- **Quote**: (paraphrased) System reminders every 5 turns made Claude think it had to stick
  rigidly to the list instead of modifying it when circumstances changed.
- **Our assessment**: This is a named anti-pattern: over-scaffolding a capable model. The
  5-turn system reminder was a harness component designed for weaker models that needed
  frequent goal re-anchoring. Applied to Opus 4.5, it became a constraint that suppressed
  adaptive behavior. The meta-lesson is that scaffolding designed for a less capable model
  can actively degrade performance of a more capable one by narrowing its action space.

### Claim 6: TodoWrite was replaced with a Task tool that includes dependencies, shares updates across subagents, and can be altered or deleted — shifting the design goal from "keeping the model on track" to "agent communication"

- **Evidence**: Direct description of the migration from the author. The Task tool is
  described as enabling inter-agent coordination — multiple subagents can read and update
  shared tasks — which the todo list did not support.
- **Confidence**: settled (first-party description of a shipped Claude Code change)
- **Quote**: (paraphrased) Replaced TodoWrite with Task tool. Tasks include dependencies,
  share updates across subagents, and can be altered/deleted. Shifted focus from "keeping
  model on track" to "agent communication."
- **Our assessment**: The reframing from "model tracking" to "agent communication" is the
  conceptual shift. A todo list is a memory aid for a single model. A Task tool is a shared
  state primitive for a multi-agent system. The same surface area now serves a fundamentally
  different function. This maps directly to the ccunpacked architecture note's documentation
  of the Task tool taxonomy — this source provides the design rationale for why Task exists
  in its current form.

### Claim 7: As model capabilities improved, tools designed to compensate for earlier limitations became constraints that actively reduced performance — capability-driven tool retirement is a first-class design practice

- **Evidence**: The TodoWrite→Task migration is the concrete case. The 5-turn system reminder
  was designed for a model that needed external goal-anchoring; Opus 4.5 didn't need this
  and was harmed by it.
- **Confidence**: settled (documented through the TodoWrite→Task case study with named model
  version and specific failure mechanism)
- **Quote**: (implied by the case study) As the model became more capable, todos became
  constraining.
- **Our assessment**: This principle extends and concretizes the "what can I stop doing?"
  heuristic from `blog-anthropic-harnessing-claude-intelligence.md`. Where that post frames
  it as a general review heuristic, this source provides the specific mechanism: system
  reminders that were designed to anchor attention become attention-narrowing constraints
  when the model no longer needs anchoring. Tool retirement is not just a cleanup task —
  it is a correctness requirement as capability rises.

### Claim 8: Pre-indexing code with RAG gave Claude context it didn't choose — replacing it with a Grep tool let Claude build its own context through active search, which produced better results

- **Evidence**: Author's account of the search evolution within Claude Code. The RAG approach
  was fragile across different environments and required upfront indexing. The Grep tool let
  Claude choose what to search for rather than receiving pre-retrieved context.
- **Confidence**: settled (first-party account of shipped evolution in Claude Code)
- **Quote**: (paraphrased) RAG required indexing and setup; was fragile across different
  environments; most critically, Claude received pre-indexed context rather than finding it
  itself.
- **Our assessment**: The key insight is that letting the model build its own context via
  search outperforms pre-retrieved context at sufficient capability levels. RAG optimizes
  for retrieving the right chunks; the Grep approach relies on the model knowing what to
  search for. The latter requires stronger model capability but produces better-fit context
  because the model selects exactly what it needs. This aligns with the BrowseComp code-
  execution filtering finding in `blog-anthropic-harnessing-claude-intelligence.md`
  (Claim 3): letting Claude write filtering logic rather than routing all tool outputs
  through context improves accuracy.

### Claim 9: Agent Skills created a progressive disclosure mechanism — skill files reference other files recursively, letting Claude discover relevant context incrementally through exploration rather than receiving a pre-loaded context dump

- **Evidence**: Author's account of the evolution from Grep to Agent Skills. Within a year,
  Claude evolved from unable to build context to performing nested multi-layer file searches
  finding exact context needed.
- **Confidence**: settled (first-party account of shipped Claude Code feature)
- **Quote**: (paraphrased) With Agent Skills, Claude could read skill files that reference
  other files recursively, discovering context incrementally through exploration. Within a
  year, Claude evolved from unable to build context to performing nested multi-layer file
  searches finding exact context needed.
- **Our assessment**: The explicit timeline ("within a year") documents the pace of capability
  advancement that made progressive disclosure viable. The recursive skill-file reference
  pattern is the implementation of progressive disclosure: the model reads a summary, decides
  which linked documents are relevant, reads those, and continues until it has sufficient
  context. This is pull-on-demand at the skill layer, corroborating Claim 4 in
  `blog-anthropic-harnessing-claude-intelligence.md` (skills as progressive disclosure with
  YAML frontmatter summaries).

### Claim 10: The Claude Code Guide subagent handles documentation lookup by searching its own context in isolation — this adds a 21st capability without adding a 21st tool to the main agent's tool list

- **Evidence**: Direct description of the Claude Code Guide subagent architecture. When users
  ask about Claude Code itself, the main agent calls a dedicated subagent that searches
  documentation within its own context following detailed extraction instructions, then returns
  only the answer to the main agent.
- **Confidence**: settled (first-party description of a shipped Claude Code feature)
- **Quote**: (paraphrased) A subagent Claude calls when users ask about Claude Code itself.
  The subagent searches documentation within its own context following detailed extraction
  instructions, returning only the answer. This keeps the main agent's context clean without
  adding a new tool.
- **Our assessment**: This is the canonical example of subagent-as-context-isolation. The main
  agent's context is not polluted with documentation search results; those results are
  filtered and distilled before re-entering context as a clean answer. The key architectural
  choice is that context isolation is achieved by routing to a subagent rather than by adding
  tools to the main agent. The consequence: capability expands without tool count growing.
  This directly implements the "progressive disclosure over tool proliferation" principle.

### Claim 11: Claude Code has approximately 20 tools, and the bar to add new tools is high because each additional tool adds decision overhead — progressive disclosure via subagents and skills is the preferred expansion mechanism

- **Evidence**: Author's direct statement about the current Claude Code tool count (~20) and
  the design philosophy behind it. The Claude Code Guide subagent example is presented as
  evidence of the preferred expansion path.
- **Confidence**: settled (first-party tool count with rationale)
- **Quote**: (paraphrased from article) Claude Code has ~20 tools. The bar to add a new tool
  is high because each option adds cognitive load.
- **Our assessment**: The ~20-tool count is a concrete calibration point for harness builders.
  More tools means more tool-selection decisions per turn, which increases model uncertainty
  and response latency. The preferred expansion mechanism (route to subagent/skill rather
  than add a tool) is a direct consequence of this design pressure. Note that this contradicts
  the ccunpacked tool taxonomy note which documents 53+ tools — but ccunpacked was documenting
  all tools including internal, feature-gated, and system tools, while this post refers to
  the user-facing tool surface. The counts are consistent once this distinction is understood.

### Claim 12: "You learn to see like an agent" — the core design heuristic is to shape tools to the model's actual abilities and cognitive patterns, not to human intuitions about what a tool should look like

- **Evidence**: Stated directly by the author as the overarching principle derived from the
  three case studies. The math analogy: a person solving a math problem needs tools suited to
  their abilities (paper, calculator, or computer), and the right tool depends on the problem
  and the solver's capabilities.
- **Confidence**: settled (explicitly stated design principle from a first-party Anthropic author)
- **Quote**: "You want to give it tools that are shaped to its own abilities"; "You learn to
  see like an agent"; "Designing the tools for your models is as much an art as it is a science"
- **Our assessment**: "See like an agent" is a named, actionable design heuristic new to our
  corpus. It operationalizes as: before finalizing a tool design, ask "how does the model
  perceive the options this tool presents?" not "does this tool do what I want it to do?" The
  three case studies are its evidence base. This complements the reversibility/observability
  criteria from `blog-anthropic-harnessing-claude-intelligence.md` (Claim 14): that post tells
  you when to promote an action to a dedicated tool; this post tells you how to design the
  tool once you've decided to promote it.

## Concrete Artifacts

### AskUserQuestion Three-Attempt Design Log

```
# AskUserQuestion tool design iteration (Claude Code, Anthropic, 2026)
# Source: "Seeing like an agent", Thariq Shihipar

Attempt 1 — ExitPlanTool parameter modification (FAILED):
  Approach: Added a `questions` parameter to the existing ExitPlanTool
            alongside the plan parameter.
  Failure:  Claude received conflicting signals — asked simultaneously for
            both a plan and questions about that plan.
            Raised ambiguity about whether to call the tool twice.
  Root cause: Parameter overloading created disambiguation failure.

Attempt 2 — Custom markdown output format (FAILED):
  Approach: Updated output instructions to produce structured markdown with
            bullet-point questions and bracketed alternatives for UI parsing.
  Failure:  Claude appended extra sentences, dropped options, or abandoned
            the structure entirely. Format was not reliably produced.
  Root cause: Prose format instructions for structured output are brittle;
              model fights against its own language generation tendencies.

Attempt 3 — Dedicated AskUserQuestion tool (SUCCEEDED):
  Approach: Created a dedicated tool callable at any point during plan mode.
            Triggers a UI modal blocking the agent loop until user answers.
  Result:   Claude reliably called the tool; structured output worked.
  Signal:   "Claude seemed to like calling this tool" — voluntary call rate
            increased, indicating tool-model fit.
  Principle: A dedicated typed tool provides an unambiguous channel for
             structured elicitation that format instructions cannot match.
```

### TodoWrite → Task Migration

```
# TodoWrite to Task tool migration (Claude Code, Anthropic)
# Source: "Seeing like an agent", Thariq Shihipar

TodoWrite era:
  Mechanism: Model writes todo list; system reminders injected every 5 turns
             to re-anchor model on goals.
  Problem with capable models: System reminders caused Opus 4.5 to treat
  the list as a rigid constraint. Model would not modify plan even when
  circumstances changed and modification was appropriate.
  Root cause: Scaffolding designed for goal-anchoring in weaker models
              becomes plan-constraining in stronger models.

Task tool replacement:
  Mechanism: Task objects with dependencies; shared state across subagents;
             tasks can be altered or deleted by any agent.
  Design goal shift: From "keeping the model on track" → "agent communication"
  Key difference: Multi-agent shared state vs. single-model memory aid.
```

### RAG → Grep → Progressive Disclosure Search Evolution

```
# Search context evolution in Claude Code
# Source: "Seeing like an agent", Thariq Shihipar

Phase 1 — RAG:
  Mechanism: Pre-indexed code retrieval. Claude received pre-selected context.
  Problems:  Fragile across environments; required indexing setup; most
             critically, Claude received context it didn't choose.

Phase 2 — Grep tool:
  Mechanism: Claude searches files on demand, builds its own context.
  Improvement: Claude selects what to search for; context matches its needs.

Phase 3 — Agent Skills (progressive disclosure):
  Mechanism: Skill files reference other files recursively. Claude reads a
             skill summary, decides which linked documents to follow, reads
             those, continues until it has sufficient context.
  Result:    Within one year, Claude went from unable to build context to
             performing nested multi-layer file searches finding exact context.

Claude Code Guide subagent (current):
  Problem solved: Documentation lookup would add a 21st tool to main agent.
  Solution: Route to a dedicated subagent that searches docs in its own
            context, returns only the distilled answer.
  Benefit:  Main agent context stays clean; capability expands without
            tool count growing.
```

### Tool Design Decision Heuristics (from article)

```
# Practitioner heuristics extracted from "Seeing like an agent"
# Source: Thariq Shihipar, Anthropic Claude Code team

Tool-model fit signal:
  "Claude seemed to like calling this tool" — voluntary call rate above
  baseline indicates the tool's interface matches the model's action model.
  Monitor involuntary vs. prompted call frequency during development.

Dedicated tool vs. format instruction:
  Use a dedicated typed tool whenever structured output is required on
  demand. Format instructions in prompts are unreliable for structured
  elicitation; typed tool call contracts are not.

When to retire a tool:
  If a tool component was designed to compensate for a model limitation,
  test whether the current model still has that limitation at each upgrade.
  Scaffolding that was load-bearing becomes a constraint when the limitation
  is eliminated.

Progressive disclosure over tool proliferation:
  ~20 tools is already a high count for decision overhead. Prefer routing
  to subagents or skills over adding tools to the main agent's tool list.
  Capability expansion via isolation beats capability expansion via enumeration.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harnessing-claude-intelligence.md` — Claim 4 there (skills as progressive
    disclosure with YAML frontmatter summaries in context, full body pulled on demand) is now
    backed by the specific design rationale here. The harnessing-intelligence post described
    the mechanism; this post explains the iterative history that produced it (RAG → Grep →
    Skills). Claim 15 there ("what can I stop doing?" at each model upgrade) is corroborated
    by the TodoWrite→Task case study here: the 5-turn system reminder was a case where the
    team asked exactly that question and removed the component.
  - `blog-ccunpacked-claude-code-architecture.md` — The tool taxonomy note documents the
    AskUserQuestion, TodoWrite, and Task tools as existing tools. This note provides the
    first-party design rationale and iteration history behind why AskUserQuestion is a
    dedicated tool and why Task replaced TodoWrite. The ccunpacked note maps *what* tools
    exist; this note explains *why* they are designed the way they are.
  - `blog-anthropic-harness-long-running.md` — Claim 9 there ("every harness component
    encodes an assumption about model limitations") is the identical meta-principle to
    Claim 7 here. Both are first-party Anthropic posts from the same week arriving at the
    same principle through different case studies: that post traces sprint decomposition
    becoming unnecessary on Opus 4.6; this post traces the 5-turn system reminder becoming
    constraining on Opus 4.5.

- **Contradicts**:
  - None identified. The ~20-tool count here vs. 53+ tools in `blog-ccunpacked-claude-code-
    architecture.md` is a scope difference (user-facing vs. all internal/gated tools), not a
    contradiction.

- **Extends**:
  - `blog-anthropic-harnessing-claude-intelligence.md` — Adds the concrete iteration history
    (three AskUserQuestion attempts, RAG→Grep→Skills evolution) behind principles that post
    states at a higher level. Together: the harnessing-intelligence post is the design
    principles; this post is the evidence base.
  - `blog-anthropic-harness-long-running.md` — Adds the specific mechanism by which a
    scaffolding component becomes a constraint (5-turn system reminder causing Opus 4.5 to
    treat a todo list as rigid) to that post's higher-level "harness components become dead
    weight" principle.
  - `blog-ccunpacked-claude-code-architecture.md` — Adds first-party design intent to that
    post's reverse-engineered architecture map. The ccunpacked note documented the Tool
    taxonomy from source maps; this post explains the design choices behind three of those
    tools.

- **Novel**:
  - **"See like an agent" as a named design heuristic**: The explicit principle — shape tools
    to the model's actual cognitive patterns, not to human intuitions — is named here for the
    first time in our corpus. Previous sources describe patterns that implement this principle
    without naming it.
  - **Three-attempt AskUserQuestion iteration log**: The specific sequence (ExitPlanTool
    parameter → custom markdown format → dedicated tool) with the specific failure mode of
    each attempt is not documented anywhere else. This is the canonical reference for why a
    dedicated elicitation tool beats format instructions.
  - **"Claude seemed to like calling this tool" as an evaluation signal**: Voluntary tool
    call frequency as a measure of tool-model fit is a practitioner technique not documented
    elsewhere in the corpus.
  - **5-turn system reminder as a named anti-pattern**: The specific mechanism by which
    over-scaffolding produces plan-rigidity in capable models is documented here for the
    first time.
  - **Capability-gated tool retirement**: Tools designed to compensate for model limitations
    should be retired as those limitations are eliminated — stated explicitly as a design
    practice for the first time in this post.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "See like an agent" as the named design heuristic
  for tool design, citing this source. The AskUserQuestion three-attempt story should be the
  canonical illustration of why dedicated typed tools outperform format instructions. The
  "Claude seemed to like calling this tool" heuristic should be listed as a practitioner
  evaluation technique alongside unit-testable metrics.

- **Chapter 02 (Harness Engineering)**: Add "capability-gated tool retirement" as an explicit
  practice: at each model upgrade, review tools built to compensate for limitations and test
  whether those limitations persist. Cite this source (5-turn system reminder case) alongside
  `blog-anthropic-harness-long-running.md` (sprint decomposition case) as two concrete instances
  of the same practice from first-party Anthropic authors.

- **Chapter 04 (Tool Design)**: The three-attempt AskUserQuestion log should anchor the
  "structured elicitation" section. Current corpus has the principle ("dedicated tools beat
  format instructions") from multiple sources; this post adds the failure taxonomy (conflicting
  signals from parameter overloading, format brittleness from prose instructions) with
  first-party authority.

- **Chapter 04 (Tool Design)** / **Chapter 06 (Multi-Agent Patterns)**: The TodoWrite→Task
  migration should be cited as the canonical example of "single-model scaffolding vs. multi-
  agent communication primitive." The design goal shift from "keeping model on track" to
  "agent communication" is the key concept for harness builders choosing between a memory aid
  and a coordination primitive.

- **Chapter 06 (Multi-Agent Patterns)**: The Claude Code Guide subagent pattern — route
  documentation lookup to a dedicated subagent rather than adding a new tool — should be
  extracted as a reusable pattern template for any capability that can be isolated to its own
  context window. The principle: prefer context isolation via subagent over tool proliferation
  in the main agent.

## Extraction Notes

- The article is available at claude.com/blog (not anthropic.com/engineering). Despite the
  different domain, Thariq Shihipar's Anthropic affiliation and the first-party description
  of internal development decisions confirm this is first-party Anthropic engineering content.
- Two WebFetch passes were performed: the first returned a high-level summary; the second
  retrieved specific quotes, iteration details, and mechanisms. Both passes were consistent.
  No direct verbatim quotes are available from WebFetch; quotes marked "(paraphrased)" above
  are faithful paraphrases of the described content.
- The article does not contain code examples or configuration snippets — the concrete
  artifacts are process descriptions, not technical implementations.
- This is a companion post to `blog-anthropic-harnessing-claude-intelligence.md` from the
  same week: that post is about harness-level design (context management, tool selection
  strategy, caching); this post is about tool-level design (iteration methodology, capability-
  driven retirement, progressive disclosure). Both are first-party Anthropic, both are April
  2026, and together they form the most complete first-party account of Claude Code design
  philosophy in the corpus.
