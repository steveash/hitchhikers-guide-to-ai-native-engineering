---
source_url: https://addyosmani.com/blog/agentic-autonomy-levels/
source_type: blog-post
title: "Agentic Autonomy Levels"
author: Addy Osmani
date_published: 2026-07-02
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: emerging
issue: "#1642"
---

# Agentic Autonomy Levels

> Addy Osmani proposes a two-axis autonomy framework (agency × orchestration) that
> replaces single-axis autonomy ladders, defines six concrete levels grouped into three
> eras, ties verification requirements and named failure modes to each level, and
> prescribes an explicit "contract" agents should run under plus metrics, four
> anti-patterns, and a one-axis-at-a-time climbing discipline.

## Source Context

- **Type**: blog-post (long-form practitioner framework piece, published on Osmani's
  personal blog, ~2,400 words)
- **Author credibility**: Addy Osmani is a Director of Engineering at Google Chrome and
  a prolific, already-corroborated corpus source (five prior source notes:
  `blog-addyosmani-code-agent-orchestra.md`, `blog-addyosmani-agentic-code-review.md`,
  `blog-addyosmani-intent-debt.md`, `blog-addyosmani-loop-engineering.md`,
  `blog-addyosmani-new-software-lifecycle.md`, plus `blog-osmani-good-spec.md`). He is a
  practitioner-synthesizer: he cites named research (an Anthropic study of ~400K Claude
  Code sessions, an unnamed earlier Anthropic study on clarification/interrupt rates,
  OpenAI's Symphony spec) and enumerates specific product features (Claude Code, Codex)
  as implementations of his framework, but the six-level taxonomy, the contract fields,
  the anti-pattern names, and the metrics list are his own synthesis/prescription, not
  independently benchmarked.
- **Scope**: Covers a mental model for classifying and governing agent autonomy across
  both single-agent depth (how far one agent goes without check-in) and multi-agent
  breadth (how many agents run and who coordinates them). Does NOT cover implementation
  code, specific classifier architectures, or controlled before/after metrics for the
  framework itself — the "metrics" section lists what to measure, not measured results.
  Does not name a specific model or vendor tool as the reference implementation for
  Level 5 orchestration; the design is left to the reader.

## Extracted Claims

### Claim 1: Autonomy debates conflate two separate axes — how far a single agent goes, and how well multiple agents are coordinated — that should be measured separately
- **Evidence**: Structural argument contrasting Steve Yegge's single-axis ladder
  (referenced as covered in "Welcome to Gas Town" and The Pragmatic Engineer) with the
  proposed two-axis model.
- **Confidence**: emerging
- **Quote**: "almost every autonomy debate I've seen conflates two questions that should be separated: how far away from yourself are we letting this single agent go, and what is our skill at coordinating many agents? To capture these two dimensions separately, we'll use two axes: agency and orchestration."
- **Our assessment**: This is the article's central structural claim and it holds up logically — a team can be highly skilled at running one agent unattended (high agency) while still coordinating agents one at a time (low orchestration), or vice versa (many agents, each individually low-agency and closely supervised). The two-axis split is a genuinely useful organizing device for guide content that currently discusses "autonomy" as a single spectrum.

### Claim 2: The six autonomy levels collapse into three eras — assisted, agent-led, and orchestration — because orchestration only becomes relevant near the top of the stack
- **Evidence**: Structural description of how the two axes recombine into a single climbable ladder in practice.
- **Confidence**: emerging
- **Quote**: "First, you're in the driver's seat, and an agent mostly just helps, waiting for you to steer it. Second, the agent takes charge of a bounded task or goal, but you're still around to steer it and verify what it does. And third, in the era of orchestration, the system is capable of running the show, dispatching work across many agents, and you mostly need to step in when things go wrong: 'management by exception.'"
- **Our assessment**: The three-era framing is a practical simplification of the two-axis model for readers who want a single ladder rather than a 2D grid — useful for guide sections that need one linear progression to recommend to a team just starting out. The author is explicit that this simplification works "because orchestration only kicks in near the top," which is a testable claim about how practitioners actually adopt these tools (single-agent maturity before multi-agent adoption), not derived from data in this article.

### Claim 3: At Level 1 (Supervised action), the dominant failure mode is approval fatigue, where all approvals feel the same regardless of actual risk
- **Evidence**: Named failure mode plus a cited fix (Codex's "Auto-review" feature delegating boundary approvals to a separate reviewer agent).
- **Confidence**: emerging
- **Quote**: "Failure mode is approval fatigue; all approvals feel the same regardless of what they're approving. You might solve this by squinting at the diff, following some heuristics, checking in with another person before approving, or just agreeing to let the agent be responsible. Codex Auto-review solves this problem by delegating the final approval of boundary conditions to a separate reviewer agent."
- **Our assessment**: Strongly corroborated elsewhere in the corpus (see Cross-References). Note for the Assayer/Smith: "Codex Auto-review" here is OpenAI Codex's feature, a distinct product from Cursor's own "Auto-review" feature covered in `blog-cursor-agent-autonomy-auto-review.md` — same feature name, different vendor, different (though architecturally similar) implementation. Do not conflate the two when citing.

### Claim 4: At Level 2 (Scoped task delegation), verification shifts from human judgment to agent-produced evidence such as passing tests, types, lint, screenshots, and repro steps
- **Evidence**: Description of the level's operating mode and what "verification" means at this tier.
- **Confidence**: emerging
- **Quote**: "Verification is shifting away from you (you may need to rest and sleep) towards evidence that the agent can produce: passing automated tests, proper types, lint suggestions, screenshots, repro steps, provenance by example, etc."
- **Our assessment**: This is a specific, actionable definition of what "evidence-based verification" concretely consists of at this autonomy tier, going beyond the generic "tests should pass" framing common elsewhere in the corpus. Useful as a checklist for what an agent's evidence packet should contain before a human at Level 2 trusts the work without full manual review.

### Claim 5: At Level 3 (Goal-driven autonomy), the stopping condition must be measurable and automatable, or the level fails — vague goals like "improve UX" are explicitly named as unusable
- **Evidence**: Prescriptive guidance with concrete good/bad examples.
- **Confidence**: emerging
- **Quote**: "Don't ask your agent to help with vague, wooly goals like 'improving user experience in general' or 'make the codebase more testable.' Pick something specific, measurable, and automated: find bugs in production that elude static analysis, reduce load time, ensure that we have a strict TypeScript build with no explicit anys, triage all dependencies to keep just those that we understand and which pass our tests, etc."
- **Our assessment**: This is a directly actionable rule for spec-writing at higher autonomy tiers, and it corroborates the corpus's existing "specification imperative" thread (see Cross-References) without repeating it verbatim — this article's contribution is naming *measurability of the stopping condition* specifically, rather than spec quality in general.

### Claim 6: At Level 4 (Parallel delegation), the primary bottleneck is decomposition, and the named failure mode is "false parallelism" — running many agents against overlapping slices, which produces merge conflicts instead of more work
- **Evidence**: Described alongside an "orchestration tax" cost claim.
- **Confidence**: emerging
- **Quote**: "The biggest bottleneck at this level is decomposition: defining the right slices to delegate. [...] Failure mode is false parallelism: running many agents against overlapping slices at once, so instead of more work you get merge conflicts and duplicated decisions. [...] each agent incurs a cost - in terms of tokens consumed - proportional to the number of agents running at the same time. On the human side, orchestration tax makes the marginal cost of adding an agent go up after a few."
- **Our assessment**: The "orchestration tax" framing (marginal review/coordination cost rising with agent count, distinct from raw token cost) is a useful economic argument for WIP-limit-style guidance, and it is compatible with but not identical to `blog-addyosmani-code-agent-orchestra.md` Claim 8's "3-5 agents" heuristic — this article gives the *mechanism* (decomposition difficulty plus rising marginal coordination cost) rather than a specific number.

### Claim 7: At Level 5 (Managed-by-exception orchestration), independent verification — separate implementers, reviewers, test runners, security checks, and acceptance gates — becomes increasingly important as agent-factory scale grows
- **Evidence**: Description of the manager-agent factory model, with OpenAI's proposed Symphony spec (Linear-board-centered, per-issue agent workspace, spec-file-driven progress tracking) cited as one design for the "operating system" layer.
- **Confidence**: emerging
- **Quote**: "At this point in the climb, it becomes increasingly important to have independent verification: separate implementers and reviewers, separate test runners and QA, separate security checks, separate process gates for acceptance."
- **Our assessment**: This is a specific, non-obvious claim: as autonomy and scale increase, the fix is not "more human review" but "more separation of verification roles between different automated actors." This is consistent with the corpus's existing two-agent (implement/review) pattern but extends it to a five-role separation at fleet scale. The OpenAI Symphony reference is secondhand (a "proposed spec," not something the author used directly) and should be weighted as such if cited further.

### Claim 8: Whether an agent is genuinely operating at "high autonomy" should be judged by three questions about speed of error detection, reversibility, and evidence of correctness — not by the agent's own summary
- **Evidence**: Named diagnostic framework presented as the litmus test for autonomy level.
- **Confidence**: emerging
- **Quote**: "If we want to determine whether a large AI system is operating with high autonomy, the three questions we should be asking are: How quickly will we know we're wrong about what it's doing? How cleanly can we undo what it's doing? What would prove we're right about what it's doing? If the answer to all three is: not quickly, at great difficulty, and trusting the summary, it's not high autonomy."
- **Our assessment**: This is one of the most immediately reusable ideas in the article — a compact three-question test that a team can apply to any proposed autonomy escalation before granting it. The explicit naming of "trusting the summary" as a failing answer directly foreshadows the article's own "summary substitution" anti-pattern (Claim 11), making this internally consistent.

### Claim 9: Every agent run should be preceded by an explicit contract covering goal, scope, non-goals, tools/permissions, stopping condition, evidence, escalation, and budget
- **Evidence**: Prescriptive framework with each field defined individually.
- **Confidence**: emerging
- **Quote**: "Every run of an agent should be preceded by a contract that defines what it's trying to do. The goal: what we're trying to achieve (not an activity, not the technique, but an outcome). The scope: what domain we're operating in, and what techniques are allowed. Non-goals: what isn't part of the objective. Tools and permissions: how the agent can interoperate with the world. Stopping condition: when to stop; ideally, a measurable variable. Evidence: specific tests, screenshots, logs, database records or other indicators that can be used to confirm something has been done (independent of the agent). Escalation: who gets involved in what circumstances (including who runs the agent). And budget: a limit on how much time, effort and tokens are to be devoted to the task."
- **Our assessment**: This eight-field contract is more granular than the corpus's existing spec-writing guidance (the three-tier Always/Ask First/Never boundary system from `blog-osmani-good-spec.md`, referenced via `blog-addyosmani-code-agent-orchestra.md` Linked Source 4). The contract format is complementary rather than duplicative: the three-tier system defines *what the agent may touch*, while this contract defines *what a specific run is authorized to accomplish and when it must stop* — a per-task governance artifact rather than a standing repo-level policy document.

### Claim 10: An Anthropic analysis of roughly 400,000 Claude Code sessions from roughly 235,000 users (October 2025–April 2026) found that people make about 70% of planning decisions while Claude executes about 80% of the work
- **Evidence**: Cited third-party research finding, presented as supporting the claim that high autonomy is about shifting *which* decisions humans make, not removing humans from the loop.
- **Confidence**: anecdotal (as reported secondhand in this article; the underlying Anthropic study itself is not in our corpus and was not independently verified during this extraction)
- **Quote**: "They looked at ~400K sessions from ~235K people between October 2025 and April 2026. From each session they could figure out the decisions someone makes like how many actions they ask for in each prompt, which of these they choose to auto-approve, how often they interrupt etc. People make ~70% of the planning decisions, but Claude does ~80% of the execution."
- **Our assessment**: If accurate, this is a striking and citable split (humans retain the planning majority, agents take the execution majority) that supports a "supervised execution, human-led planning" default posture rather than either full delegation or full manual control. However, this is a secondhand citation of an unnamed/unlinked Anthropic study within Osmani's post — the original study should be located and mined directly before this statistic is treated as settled in the guide. Flagging as a follow-up source to enqueue.

### Claim 11: Autonomy systems tend to fail through four specific anti-patterns — autonomy as status, permission laundering, summary substitution, and fleet cosplay — each with a named fix
- **Evidence**: Four named patterns with one-line definitions and fixes.
- **Confidence**: emerging
- **Quote**: "Autonomy as status - an agent's autonomy rating becomes a meaningless badge of status. Higher autonomy is treated as proof of capability, not of safety, and agents are run hotter than verification supports. [...] Permission laundering - the tyranny of approval fatigue leads us to grant AI agents and tools wildly broader access than necessary. [...] Summary substitution - the agent's work summary substitutes for review, assuming the summary is sufficient. [...] Fleet cosplay - dozens of agents run in parallel, but a human persists in orchestrating every dependency manually."
- **Our assessment**: These four anti-patterns are specific and diagnostic — each names a distinct organizational failure mode rather than a generic warning against "overtrusting AI." "Fleet cosplay" in particular is a novel, precise name for a failure the corpus has not previously named explicitly: running many agents in parallel while a human still manually tracks every dependency between them, which negates the coordination benefit of orchestration. "Permission laundering" directly corroborates the corpus's existing approval-fatigue findings (see Cross-References) with a memorable, citable name.

### Claim 12: Safe scaling of autonomy requires moving up one axis at a time — starting from a single supervised, scoped agent and expanding into parallel read-heavy work, then parallel write work with worktree ownership rules, before adding recurring automation or full orchestration
- **Evidence**: Prescriptive sequencing with named new failure modes introduced at each step.
- **Confidence**: emerging
- **Quote**: "Move up one axis at a time. Start with a single supervised agent to do a single scoped task that produces defensible evidence of success (an autonomy level 1, if tidy enough). Then gradually expand in the three orthogonal directions. Parallelize read-heavy exploration tasks (autonomy level 4). Add write agents acting on separate worktrees with constrained file ownership rules (autonomy level 4). Add recurring automations, then agent-led orchestration based on issues, voice, etc."
- **Our assessment**: This is the article's most operational, directly-guide-usable recommendation: a concrete adoption sequence rather than an abstract principle. It matches the general shape of adoption-curve guidance elsewhere in the corpus (start narrow, expand as trust accumulates) but ties each expansion step to a specific axis (agency vs. orchestration) and a specific new failure mode to watch for (drift/context rot for longer single-agent runs; stale assumptions for background work; merge conflicts for parallel work; silent token spend for recurring automation; alert fatigue for managed-by-exception).

## Concrete Artifacts

### The Six-Level Autonomy Stack (verbatim level names and one-line summaries)

```
Source: https://addyosmani.com/blog/agentic-autonomy-levels/ ("The six levels in detail")

Level 0: Assist
  "The agent makes suggestions that are mostly good and often perfect, but you
  will always decide whether they're good enough to act on."
  Use for: costly errors, tiny changes, forming your own judgment.
  Verification: mostly local.

Level 1: Supervised action
  "The agent edits or runs commands on your behalf, asking you before executing
  anything consequential."
  Default posture for most people. Failure mode: approval fatigue.

Level 2: Scoped task delegation
  "Hand off a bounded task to the agent."
  Verification: automated tests, types, lint, screenshots, repro steps.

Level 3: Goal-driven autonomy
  "The agent does whatever it takes to achieve a goal, stopping only when some
  condition is met."
  Requires: measurable, automatable stopping condition.

Level 4: Parallel delegation
  "Work across many agents in parallel."
  Bottleneck: decomposition. Failure mode: false parallelism (overlapping
  slices -> merge conflicts). Cost: orchestration tax rises with agent count.

Level 5: Managed-by-exception orchestration
  "Define what success looks like, and which policies should apply."
  Manager agent wakes on trigger, dispatches workers, monitors, verifies,
  retries, escalates, aggregates, returns work products + evidence.
```

### Three Eras Mapping (verbatim)

```
Source: https://addyosmani.com/blog/agentic-autonomy-levels/ ("The climb: three eras and a single stack")

Era 1 (Assisted):      "you're in the driver's seat, and an agent mostly just
                        helps, waiting for you to steer it."
Era 2 (Agent-led):     "the agent takes charge of a bounded task or goal, but
                        you're still around to steer it and verify what it does."
Era 3 (Orchestration): "the system is capable of running the show, dispatching
                        work across many agents, and you mostly need to step in
                        when things go wrong: 'management by exception.'"
```

### Agent Contract Fields (verbatim, condensed)

```
Source: https://addyosmani.com/blog/agentic-autonomy-levels/ ("Every run of an agent should be preceded by a contract...")

Goal:                what we're trying to achieve (outcome, not activity/technique)
Scope:                what domain, what techniques are allowed
Non-goals:            what isn't part of the objective
Tools and permissions: how the agent can interoperate with the world
Stopping condition:   when to stop; ideally a measurable variable
Evidence:             tests, screenshots, logs, DB records (independent of the agent)
Escalation:           who gets involved in what circumstances
Budget:               time/effort/token limit, retry limit, parallelism limit
```

### Metrics List (verbatim, "Metrics make autonomy just a little more reliable")

```
Mean time between interventions
Longest successful unattended run with accepted work
Share of actions run in the sandbox vs escalated
Percentage of actions auto-approved vs rejected
Mean number of agent actions per human instruction
Clarification request rate
Interrupt request rate
Review time per accepted change
Rework rate on each level of confidence
Defect escape rate on each level of confidence
Token cost per accepted change
```

### Four Anti-Patterns (verbatim names + fixes)

```
Autonomy as status
  Fix: "Praise and reward those who settle on the correct level of autonomy
  and relentlessly avoid overstepping."

Permission laundering
  Fix: "Better boundaries are always a fix, such as sandbox profiles, scoped
  writable roots, allowlisted commands, hooks, and Auto-review."

Summary substitution
  Fix: "Bundle the same evidence packet as with fully manual reviews (a diff,
  tests, logs, screenshots, reviewer findings, risks, gaps, etc.) while
  avoiding cognitive surrender."

Fleet cosplay
  Fix: "Shared state, ownership rules, and better dependency tracking
  gradually reduce the need to coordinate manually."
```

### Tool/Feature References (verbatim list)

```
Claude Code: /plan, /goal, /loop, /background, /batch, /code-review,
  /security-review modes, subagents, hooks, checkpointing, agent delegation
  and management practices, background sessions, agent-team patterns,
  /schedule arguments

Codex: local/cloud threads, Goal mode, worktrees, Automations, subagents,
  review panes, GitHub code review, hooks, sandboxing, Auto-review, and rerun
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-auto-mode.md` Claim 1 ("Users approve 93% of
    permission prompts in manual mode — making manual review effectively theater")
    directly corroborates this article's Claim 3 (approval fatigue as the dominant
    Level 1 failure mode). Anthropic's own telemetry gives the approval-fatigue claim
    a settled quantitative backing that this article states only anecdotally.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("The bottleneck has shifted
    from code generation to verification") corroborates this article's closing thesis,
    "Verification will always be the bottleneck," from the same author across two
    different posts four months apart — a consistent through-line in Osmani's writing.
  - `blog-cursor-agent-autonomy-auto-review.md` Claims 1 and 6 (autonomy as "a dial,
    not a switch"; block-and-explain to the parent agent rather than the user) describe
    a production system that is a concrete implementation of this article's Claim 3
    fix for approval fatigue (delegating boundary approval to a separate reviewer
    agent). Note the naming collision flagged in Claim 3's assessment: Cursor's
    "Auto-review" and Codex's "Auto-review" are different vendors' features with the
    same name; this article cites the Codex one.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 10 (the "specification imperative"
    — vague thinking multiplies errors across agent fleets) corroborates this article's
    Claim 5 (Level 3 stopping conditions must be measurable, not "wooly").

- **Contradicts**: None identified. No existing source note stakes out a position that
  autonomy should be judged by a single axis, that approval-based (non-classifier)
  gating scales well, or that agent work summaries are sufficient for review — all of
  which this article argues against. No contradiction issue filed.

- **Extends**:
  - Steve Yegge's single-axis autonomy ladder, which this article explicitly names as
    the framework it is extending ("Steve Yegge's single-axis ladder mentioned in
    'Welcome to Gas Town' and in The Pragmatic Engineer"). **Important distinction for
    the Assayer**: this is *not* the same Yegge artifact covered by the corpus's
    existing `blog-simonwillison-steve-yegge.md` note, which covers a different Yegge
    topic entirely (the 20/20/60 industry AI-adoption-curve claim and the Google/
    Osmani/Hassabis Twitter dispute) — that note contains no autonomy-level ladder.
    The single-axis ladder this article extends appears to be the same "8-level
    framework" referenced in `blog-addyosmani-code-agent-orchestra.md` Claim 1
    ("Steve Yegge's 8-level framework where levels 5-8 require fundamentally different
    set of skills"), which that note's own "Additional Sources to Enqueue" section
    flagged as still unmined in our corpus. Recommend enqueueing Yegge's original
    ladder post/thread as a distinct source.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits of 3-5 concurrent
    agents) — this article's Claim 6 (orchestration tax, false parallelism) supplies
    the mechanism behind why WIP limits exist, without repeating the specific number.
  - `blog-osmani-good-spec.md` (via `blog-addyosmani-code-agent-orchestra.md` Linked
    Source 4's three-tier Always/Ask First/Never boundary system) — this article's
    Claim 9 (eight-field agent contract) is a complementary, per-run governance
    artifact alongside that standing repo-level policy document.

- **Novel**:
  - The two-axis agency/orchestration framework itself (Claim 1) — no existing corpus
    source separates "how far one agent goes" from "how many agents are coordinated"
    as independent, separately-measurable dimensions.
  - The three risk/reversibility/evidence questions as a portable litmus test for
    whether autonomy is genuinely "high" (Claim 8).
  - The eight-field agent contract format (Claim 9) as a per-task governance document,
    distinct from repo-level CLAUDE.md/AGENTS.md policy.
  - "Fleet cosplay" and "autonomy as status" as named anti-patterns — no prior corpus
    source names either failure mode explicitly, though "permission laundering" and
    "summary substitution" overlap conceptually with approval-fatigue and evidence-
    packet findings already in the corpus.
  - The orchestration-tax framing for why marginal agent-coordination cost rises with
    fleet size, independent of raw token cost (Claim 6).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the eight-field agent contract (Claim 9) as
  a recommended per-task governance template, positioned as complementary to — not a
  replacement for — the existing CLAUDE.md/AGENTS.md boundary guidance. Specifically
  recommend it for any workflow operating at Level 3+ (goal-driven or higher), where a
  measurable stopping condition and a budget cap are load-bearing safety mechanisms
  that repo-level policy files don't capture per-run.

- **Chapter 03 (Verification/Safety)**: Add the three risk/reversibility/evidence
  questions (Claim 8) as a concrete pre-flight checklist for deciding whether a
  proposed autonomy escalation is defensible. Add the "summary substitution"
  anti-pattern (Claim 11) as a named failure mode alongside the existing evidence-
  packet guidance already sourced from `blog-addyosmani-code-agent-orchestra.md` — this
  article's phrasing ("trusting the summary" as a failing answer to "what would prove
  we're right?") gives that existing guidance a sharper, more citable framing.

- **Chapter 03/05 boundary (Approval fatigue)**: Cite this article's Claim 3 alongside
  `blog-anthropic-claude-code-auto-mode.md` Claim 1 (93% blanket approval) and
  `blog-cursor-agent-autonomy-auto-review.md` Claims 6 and 9 (40%→7% interruption
  reduction) as three independent, converging sources — from Anthropic, Cursor, and
  Osmani's synthesis of Codex — that approval-gate-first designs fail at scale and that
  delegating boundary decisions to a separate reviewer agent (whichever vendor calls it
  "Auto-review") is the emerging production answer.

- **Chapter 04 (Orchestration, if/when it exists as a distinct section)**: Add the
  two-axis agency/orchestration framework (Claim 1) as the organizing model for
  distinguishing single-agent depth guidance from multi-agent coordination guidance,
  replacing any single-axis "autonomy level" framing currently implied elsewhere in the
  guide. Add the false-parallelism and orchestration-tax failure modes (Claim 6) to any
  section recommending parallel/fleet agent use, and the one-axis-at-a-time climbing
  sequence (Claim 12) as the recommended adoption path for teams scaling beyond a
  single supervised agent.

## Extraction Notes

- Read the full article directly (fetched raw HTML and stripped markup for verbatim
  quote verification, since the WebFetch tool's summarization pass paraphrased some
  wording on a first pass). All quotes in this note were checked character-for-character
  against the raw extracted text.
- No sub-pages were followed: the article links only to a Pangram human-authorship
  verification page (not substantive content) and does not link out to the Anthropic
  study, the earlier Anthropic study on clarification/interrupt rates, or the OpenAI
  Symphony spec with enough specificity to locate and fetch those as standalone sources
  in this pass. All three should be enqueued as follow-up sources (see below) rather
  than treated as verified in this note.
- Follow-up sources to enqueue: (1) the Anthropic study of ~400K Claude Code sessions
  (Oct 2025–Apr 2026) cited in Claim 10 — currently only available to us secondhand
  through this article; (2) the earlier, unnamed Anthropic study on clarification/
  interrupt rates for "hardest tasks" mentioned in the article's "Risk and reversibility
  set the ceiling" section but not extracted as a numbered claim here because no
  specific figures beyond "asked for clarification more than twice as often as users
  interrupted" were given; (3) Steve Yegge's original single-axis/8-level autonomy
  ladder post, referenced by both this article and `blog-addyosmani-code-agent-
  orchestra.md` but not yet mined as its own source note.
- The three triage comments on the source issue all converge on the same guidance
  (extract the two-axis framework, six levels, and anti-patterns); this note follows
  that guidance and additionally flags the Yegge-source-note mismatch (see
  Cross-References → Extends) since the triage comments assumed
  `blog-simonwillison-steve-yegge.md` was the relevant existing Yegge note, which on
  inspection it is not.
