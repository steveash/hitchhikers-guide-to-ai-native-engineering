---
source_url: https://news.ycombinator.com/item?id=47573483
source_type: failure-report
platform: hn
title: "Ask HN: Is it actually possible to run multiple coding sessions in parallel?"
author: sukit
date_published: 2026-03-30
date_extracted: 2026-04-13
last_checked: 2026-04-13
status: current
confidence_overall: anecdotal
issue: "#57"
---

# Failure Report: Parallel Claude Code Sessions — Terminal Degradation, Cognitive Ceiling at 2, and the Demo Gap

> A practitioner who tried and failed to replicate Claude Code author demos of parallel
> multi-session workflows documents three distinct failure modes: terminal UX degradation
> that forced a tool switch, a hard cognitive ceiling of ~2 interactive parallel sessions
> before context-switching collapse, and a structural "demo gap" between tool-author
> workflows and average practitioner capability — with the thread's comments revealing
> that git worktrees + atomic tasks is the infrastructure bridge that closes (most of)
> that gap.

## Source Context

- **Platform**: Hacker News (Ask HN self-post), 11 points, 15 comments, 2026-03-30
- **Author credibility**: Working practitioner who used Claude Code from approximately
  June 2025, then Opencode, then Pi — three tools over roughly nine months. Not a
  researcher or tool author; a daily user who tried to level up to "high-efficiency"
  workflows and documented where they hit ceilings. The Ask HN format invites honest
  self-reporting over performance.
- **Community response**: Thread produced substantive workarounds. Multiple commenters
  confirmed parallel work is possible but requires worktree isolation. dontwannahearit
  reports a detailed 11-step workflow capped at 3 simultaneous threads. kevinsync
  describes a Claude + Codex multi-model strategy as an alternative to raw parallelism.
  No commenter disputed the OP's core failure modes; they offered techniques to work
  around them, which implicitly corroborates the underlying difficulties.

## What Was Attempted

- **Goal**: Scale from a single-session "ask, discuss, let agent write, review" workflow
  to the multi-session parallel pattern demonstrated publicly by Boris (identified by OP
  as "the Claude Code Author" — likely Boris Cherny, Claude Code's author; this is OP's
  attribution, not independently verified by this extraction).
- **Tool/approach**: Claude Code (starting ~June 2025). Switched to Opencode after
  terminal UX issues. Switched to Pi after additional issues with Opencode. Also attempted
  various "high-efficiency" workflows found on Twitter/X.
- **Setup**: Solo developer. Language and codebase unspecified.

## What Went Wrong

### Failure Mode 1: Claude Code Terminal UX Degradation

- **Symptoms**: "My terminal would constantly flicker, formatting was messy, and a single
  session could drag my whole machine down."
- **Severity**: Severe enough to force a tool switch — the author left Claude Code entirely
  for Opencode, then Pi.
- **Reproducibility**: Consistent enough for the author to switch tools after several months,
  implying this was not a one-off. No commenter contradicted this experience.

### Failure Mode 2: Cognitive Ceiling at ~2 Parallel Interactive Sessions

- **Symptoms**: "Two parallel sessions already feel like my limit. Once I go beyond that,
  my brain starts falling apart within minutes. Context switching is painful, I will lose
  myself in ten minutes."
- **Severity**: Practical productivity ceiling. Beyond 2 sessions, the overhead cost of
  context-switching appears to exceed the throughput gain from parallelism.
- **Reproducibility**: First-person account. Partially corroborated by dontwannahearit:
  "I can only keep 3 threads like this going at once." Both are upper bounds on interactive
  parallel sessions from independent practitioners.

### Failure Mode 3: Failed Demo Replication ("Demo Gap")

- **Symptoms**: "Around the end of last year I saw Boris, the Claude Code Author, share how
  he uses Claude Code. I was shocked. He runs multiple sessions in parallel. I tried to
  replicate that. It didn't work."
- **Severity**: Not a tool failure — the tool worked — but an expectation-gap failure. The
  workflow demonstrated publicly could not be reproduced by the practitioner.
- **Reproducibility**: The author raises this as a structural question: "Or is this kind of
  workflow only realistic for a small group of people, like those building the tools
  themselves?"

## Root Cause (if identified)

### Failure Mode 1 (Terminal Degradation)

- **Author's diagnosis**: Not explicitly diagnosed — described as an experience failure
  that caused the tool switch, not a root-caused technical failure.
- **Our assessment**: Likely a combination of Claude Code's rich terminal rendering (diff
  coloring, streaming output, interactive UI elements) and resource overhead of keeping
  a persistent agentic session running. Distinct from the session-content/context-loss
  failures documented in `failure-decker-4hr-session-loss.md` and
  `failure-claudemd-ignored-compaction.md` — this is a UX/system-resource failure, not
  an in-session context failure.
- **Category**: tool-limitation (terminal renderer design choice)

### Failure Mode 2 (Cognitive Ceiling)

- **Author's diagnosis**: Human cognitive limits — context switching between simultaneously
  active sessions overwhelms working memory within minutes. "Context switching is painful,
  I will lose myself in ten minutes."
- **Our assessment**: The ceiling is real but is a human-attention constraint, not a tool
  constraint per se. The thread's comments reveal this is addressable via worktree isolation
  (see Recovery Path): if sessions are logically isolated and scoped to atomic tasks, the
  practitioner's own reply shows the ceiling can be pushed to 5-10. The ceiling of 2
  applies to *interactively attended* parallel sessions where the practitioner's attention
  must actively track multiple in-flight tasks.
- **Category**: expectation-mismatch + workflow design (not a tool bug)

### Failure Mode 3 (Demo Gap)

- **Author's diagnosis**: Implicit — the workflow may only be realistic for "those building
  the tools themselves."
- **Our assessment**: Partially correct. Tool authors have deep configuration knowledge,
  custom tooling, and practice with the specific workflow patterns they demonstrate. However,
  the thread reveals that worktrees + atomic task scoping closes most of the gap for
  motivated practitioners. The "demo gap" is real but is also a configuration-and-practice
  gap, not an intrinsic capability gap.
- **Category**: expectation-mismatch

## Recovery Path

- **What they switched to**: Opencode (after Claude Code terminal issues), then Pi (still
  using at time of posting). The switch resolved the terminal UX failure mode but the
  author's workflow "hasn't really changed" — still single-session, primitive.

- **Workaround (discovered via thread)**:
  - sukit's own reply, after reflecting on worktree usage: "Yes if you operate with
    worktrees, its actually possible to operate up to 5-10 at least I've succeeded with
    that multiple times. I think whats important is, that you keep atomical small tasks
    and increments, and whenever possible merge things."
  - dontwannahearit's 11-step workflow using 3 simultaneous git worktrees (feature A,
    feature B, refactoring branch) with ticket-driven task definitions, per-worktree
    Claude instances, linter/test gates, and peer-review within the workflow.
  - kevinsync's multi-model strategy: use Claude for plan generation + implementation,
    Codex for co-validation + PR review — avoids the scaling problem of many simultaneous
    Claudes by routing different task types to different models.
  - the_robvb: "When I work with multiple parallel sessions I take the time to plan
    things out first, and then run everything. This takes a bit off the cognitive load."

- **Unresolved**: The OP's core question — whether the high-efficiency parallel workflow
  is accessible to average practitioners — is answered conditionally by the thread:
  yes, with worktrees + atomic tasks + upfront planning. But whether this is worth
  the setup overhead for a solo developer is left open.

## Extracted Lessons

### Lesson 1: Claude Code terminal UX degraded under real-world use — flickering, formatting noise, machine-wide slowdown

- **Evidence**: Direct quote from sukit: "My terminal would constantly flicker, formatting
  was messy, and a single session could drag my whole machine down." (Verbatim from OP,
  confirmed via direct source fetch.)
- **Confidence**: anecdotal (single practitioner's sustained experience over several months,
  sufficient to drive a tool switch)
- **Actionable as**: Claude Code's terminal UX overhead is a real adoption friction. The
  guide should not treat Claude Code as universally frictionless for terminal users.
  Acknowledge terminal renderer resource cost as a factor for resource-constrained
  machines.

### Lesson 2: The interactive parallel session ceiling is ~2 sessions without worktree isolation

- **Evidence**: Direct quote from sukit: "Two parallel sessions already feel like my limit.
  Once I go beyond that, my brain starts falling apart within minutes. Context switching
  is painful, I will lose myself in ten minutes." (Verbatim from OP, confirmed via direct
  source fetch.) Corroborated independently by dontwannahearit: "I can only keep 3 threads
  like this going at once." (Verbatim from comment thread.)
- **Confidence**: anecdotal (two independent practitioners)
- **Actionable as**: For practitioners without worktree isolation, set realistic expectations:
  1-2 interactively attended parallel sessions is a reasonable ceiling. Beyond that, the
  cognitive overhead of context-switching may negate throughput gains. The guide should
  frame higher parallelism as requiring infrastructure (worktrees) and practice, not just
  opening more terminals.

### Lesson 3: Git worktrees + atomic task scoping appear to extend the parallel ceiling to 3-10

- **Evidence**: Direct quote from sukit's own reply: "Yes if you operate with worktrees,
  its actually possible to operate up to 5-10 at least I've succeeded with that multiple
  times. I think whats important is, that you keep atomical small tasks and increments,
  and whenever possible merge things." (Verbatim from thread comment.) dontwannahearit
  runs 3 worktrees simultaneously with an 11-step workflow and ticket-based task scoping.
  nojs: "Yes, worktrees with workmux. I expected this to become less necessary over time
  as models got faster, but the opposite has happened. It feels like Claude has actually
  gotten slower (but in fairness does more per prompt), meaning worktrees are even more
  essential now." (Verbatim.)
- **Confidence**: anecdotal (three independent confirmations from the same thread)
- **Actionable as**: Git worktrees are the primary infrastructure pattern for scaling beyond
  2 parallel sessions. The guide should introduce worktrees as the default recommendation
  for any practitioner targeting more than 2 concurrent agent tasks. The "atomic tasks"
  constraint is as important as the worktree isolation itself.

### Lesson 4: The "demo gap" is real but is a configuration-and-practice gap, not an intrinsic capability gap

- **Evidence**: sukit describes seeing Boris demonstrate parallel sessions and failing to
  replicate them: "He runs multiple sessions in parallel. I tried to replicate that.
  It didn't work." (Verbatim.) The thread's responses demonstrate that multiple practitioners
  DO successfully run parallel workflows — but with infrastructure (worktrees, ticket
  systems, planning-first disciplines) the OP had not set up.
- **Confidence**: anecdotal
- **Actionable as**: The guide should explicitly address the demo gap in the daily-workflows
  chapter: public demos of high-efficiency agentic workflows typically embed infrastructure
  (worktrees, tool-specific configurations, planning disciplines) that is not visible in
  the demo. Show the required infrastructure alongside any aspirational workflow description.
  Set realistic expectations: replicating a tool-author demo takes configuration investment.

### Lesson 5: Multi-model cooperation (Claude + Codex) is an alternative scaling strategy to raw Claude parallelism

- **Evidence**: kevinsync (verbatim from thread): "Lately I've had a lot more success having
  Claude generate a plan, send the plan to Codex for co-validation/amendments, have Claude
  implement the plan, then have Codex PR review the commit." And: "I haven't yet found a
  scenario where many Claudes and many Codexes running simultaneously on 35 concurrent
  features makes any sense, but I'd definitely encourage people to try multi-model
  cooperation since they all seem to have different sensibilities."
- **Confidence**: anecdotal (single practitioner's account)
- **Actionable as**: Multi-model workflows (plan with one, implement with another, review
  with a third) can achieve quality and throughput gains without requiring the practitioner
  to manage many parallel interactive sessions. This is an underrepresented alternative
  to the parallel-same-model pattern.

## Concrete Artifacts

### dontwannahearit's 11-Step Worktree Workflow

The most concrete parallel-session workflow in the thread. Reproduced verbatim:

```
1. Add ticket in gitlab describing bug or feature in as much detail as possible 
   along with acceptance criteria like expected unit tests or browser based tests.
2. In a work tree create a branch based on the id of that ticket in gitlab.
3. Start Claude, tell it to use a skill to pull that ticket, research and make a plan.
4. Review the plan, ask questions, refine.
5. Approve plan and let claude cook.
6. Have Claude run a set of linters/tests/code quality checks and ground until done.
7. Start a new Claude instance, ask it to review changes made. Provide feedback to 
   first Claude instance for changes.
8. Commit and push, creating a draft mr/pr in gitlab.
9. Review the actual code changes myself using gitlab. Comment on things not right.
10. Get Claude to use another skill to pull comments and work to resolve them. 
    Also feed back any CI failures.
11. Manually close comments and push again. Repeat until done and ready for 
    co-worker review.
```

Key constraint: "I can only keep 3 threads like this going at once. Sometimes it's only
1 or 2, depending on complexity. Smaller is better. Try to stay atomic and avoid feature
creep in each mr."

### Cognitive Ceiling Data Points

Two independent practitioners on upper limits of interactive parallel sessions (verbatim):

- sukit: "Two parallel sessions already feel like my limit. Once I go beyond that, my
  brain starts falling apart within minutes. Context switching is painful, I will lose
  myself in ten minutes."
- dontwannahearit: "I can only keep 3 threads like this going at once."

Together these bracket the cognitive ceiling at 2-3 interactive parallel sessions for
practitioners not using background-autonomous patterns.

### Worktree Scale Claim

sukit's own resolution (verbatim, later reply in same thread):

> "Yes if you operate with worktrees, its actually possible to operate up to 5-10 at
> least I've succeeded with that multiple times. I think whats important is, that you
> keep atomical small tasks and increments, and whenever possible merge things. to many
> hanging worktrees can quickly also become a nightmare managing"

Note: OP answered their own question — the 5-10 ceiling requires worktrees AND atomic
task discipline, not just opening more terminals.

## Cross-References

- **Corroborates** `failure-decker-4hr-session-loss.md`: Both document Claude Code
  reliability failures severe enough to change workflows. However, the failure axes are
  distinct: decker's failure is session-context loss (compaction destroying architectural
  rationale); sukit's failure mode 1 is terminal UX degradation (flickering, formatting,
  resource consumption). Together they cover two independent failure axes that together
  make the case for Claude Code requiring significant mitigation investment.

- **Corroborates** `failure-hooks-enforcement-2k.md`: Both document the overhead required
  to use Claude Code reliably. meloncafe built a 14-hook enforcement system; sukit simply
  switched tools. The response to friction differs but the underlying friction (Claude Code
  requires substantial engineering or practice to work reliably) is the same.

- **Corroborates** `failure-claudemd-ignored-compaction.md`: Adds to the pattern of
  multiple independent practitioners abandoning or building workarounds for Claude Code.
  The aggregate across these three notes forms a consistent picture: Claude Code's
  out-of-the-box experience requires significant mitigation for reliable use.

- **Extends/qualifies** `blog-addyosmani-code-agent-orchestra.md`: Osmani (Claim 8)
  recommends "3-5 concurrent agents as the WIP limit," noting Boris Cherny reportedly
  runs 15+. This source adds the practitioner-side evidence: without worktree isolation,
  the interactive cognitive ceiling is 2 sessions (sukit) to 3 sessions (dontwannahearit).
  The resolution: Osmani's 3-5 figure and Boris's 15+ apply to background-autonomous
  (isolated worktree) modalities; sukit and dontwannahearit are describing interactively
  attended sessions. The guide should make this distinction explicit.

- **Corroborates** `blog-sankalp-claude-code-20.md`: Sankalp's practitioner account also
  documents Claude Code rough edges and the gap between advertised and experienced
  capability. Both are honest first-person accounts from working developers, not vendor
  documentation.

- **Novel**: Terminal UX degradation (flickering, formatting, machine-wide slowdown) as a
  distinct failure axis is not captured by any other source note. All other failure notes
  focus on context/session/compliance failures; this is the only note documenting the
  terminal renderer itself as a failure point. The "demo gap" framing — tool-author demos
  embedding invisible infrastructure — is also new to this corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add an explicit "Scaling to Parallel Sessions" section
  that distinguishes between: (a) interactive parallel sessions (ceiling: 2-3 without
  worktrees), and (b) isolated worktree sessions (ceiling: 5-10 with atomic task
  discipline). Cite sukit's cognitive ceiling quote and the worktree breakthrough quote.
  Add the demo gap caveat: when guide content shows parallel session demos, explicitly
  list the required infrastructure alongside the workflow description.

- **Chapter 01 (Daily Workflows)**: Add multi-model cooperation (kevinsync's Claude plan +
  Codex validate + Claude implement + Codex review) as an alternative to parallel
  same-model sessions. This provides a quality/throughput gain without the cognitive
  overhead of managing many simultaneous interactive sessions.

- **Chapter 02 (Harness Engineering)**: Promote git worktrees from an optional technique
  to a recommended baseline for practitioners aiming for more than 2 concurrent tasks.
  dontwannahearit's 11-step workflow is the most concrete worktree workflow in the corpus
  and should be included as a reference pattern.

- **Chapter 05 (Team Adoption)**: The "demo gap" observation belongs in a "Setting
  Realistic Expectations" section. Guide authors should be explicit: the workflows shown
  in vendor demos and expert practitioner write-ups typically embed months of configuration
  and practice. The onboarding path to high-efficiency parallel workflows is measured in
  weeks to months, not hours.

## Extraction Notes

- The source URL was confirmed live and accessible via the Algolia HN API
  (https://hn.algolia.com/api/v1/items/47573483). All verbatim quotes in this note were
  extracted directly from the API response and cross-checked against the scanner preview
  in the issue body. The quote "My terminal would constantly flicker, formatting was messy,
  and a single session could drag my whole machine down" appears verbatim in both the issue
  body preview and the direct API fetch. Direct HN HTML fetch returned HTTP 429 (rate
  limited); Algolia API fetch succeeded.
- A previous Miner extraction (PR #82) was based on the Prospector's triage synthesis
  rather than a direct source read (WebFetch was denied in that environment). This
  extraction reads the source directly. As a result: (1) sukit's self-contradictory
  follow-up comment (OP raised the 2-session ceiling, then answered their own question
  with a worktree-enabled 5-10 ceiling) is now captured; (2) additional commenter detail
  from kevinsync, nojs, dontwannahearit, and the_robvb is included; (3) all quotes are
  attributed as verbatim from source.
- The thread's "Boris" identification comes from sukit calling him "the Claude Code Author."
  This is almost certainly Boris Cherny, who is publicly identified as Claude Code's
  author. Treated as sukit's attribution, not independently verified.
- The thread is anecdotal throughout — no code, no metrics, no controlled comparisons.
  All confidence grades are anecdotal accordingly. The value is the concrete cognitive
  ceiling numbers (2-3 interactive sessions), the worktree workaround confirmation, and
  the demo gap framing — specific observations that are absent from other sources.
- The 15-comment thread was read in full. sukit participates in several reply chains;
  their replies partially contradict and expand on the OP, which is the most novel
  finding in the thread (the author resolved their own problem mid-discussion via worktrees).
