---
source_url: https://cognition.com/blog/devin-can-now-manage-devins
source_type: blog-post
title: "Devin Can Now Manage Devins"
author: The Cognition Team
date_published: 2026-03-19
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: anecdotal
issue: "#2073"
---

# Devin Can Now Manage Devins

> Cognition product announcement: Devin can now decompose a large task and
> delegate pieces to a team of "managed Devins" — full agent instances, each
> in its own isolated VM with its own shell/browser/test runner, coordinated
> by a parent Devin that scopes work, monitors progress, resolves conflicts,
> and reads full child trajectories to improve future decomposition. Short,
> thin-evidence post; concrete value is in the mechanics named and the five
> verbatim example task-decomposition prompts, not in any measured outcome.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  03.19.26 per the page's byline, i.e. 2026-03-19; byline "By The Cognition
  Team," no individual author named)
- **Author credibility**: Published directly by Cognition, the company that
  builds and sells Devin. This is a first-party product-announcement post,
  the same authorship pattern as `blog-cognition-devin-in-windsurf.md` and
  `blog-cognition-auto-triage.md` (also "By The Cognition Team"). No named
  individual, no customer quote, no metric of any kind, and no incident or
  worked example appears anywhere in the post. This is a thinner-evidence
  post than `blog-cognition-verifying-agentic-development.md` (which has a
  named author and detailed mechanism disclosure) or
  `blog-cognition-devin-productivity-estimation.md` (which discloses
  statistical validation) — it sits at the same evidentiary tier as
  `blog-cognition-devin-in-windsurf.md`: a product-philosophy/feature
  announcement with concrete shipped mechanics but zero adoption, accuracy,
  or outcome data.
- **Scope**: Covers what "managed Devins" are (full Devin instances in
  isolated VMs), the coordinator's role (scope, assign, monitor, resolve
  conflicts, compile), the stated rationale (context accumulation degrades
  single-session quality), a named feedback mechanism (parent reads child
  trajectories to improve future decomposition), a bulleted capability list
  (spin up, message, monitor ACU, sleep/terminate, schedule self-messages),
  and five example task-decomposition prompts from a "Try it now" section.
  Does NOT cover: how many managed Devins can run in parallel, any
  reliability/success-rate figure, cost data beyond the undefined "ACU"
  unit, how conflicts between managed Devins are actually resolved
  (mechanism not described, only stated as a coordinator responsibility),
  how the trajectory-reading feedback loop concretely changes future
  decomposition, or any named customer/practitioner using the feature.

## Extracted Claims

### Claim 1: Devin can now break a large task into scoped pieces and delegate each piece to a separate "managed Devin" session that runs in parallel
- **Evidence**: Direct feature-announcement statement opening the post.
- **Confidence**: emerging (vendor description of a shipped, generally
  available feature — not a single anecdote — but no example task or
  outcome is walked through)
- **Quote**: "Starting today, Devin can break down large tasks and delegate them to a team of managed Devins that work in parallel."
- **Our assessment**: This is the headline capability claim and the post's
  only forward-looking commitment ("starting today," i.e. generally
  available, not a beta or waitlist). It names the core mechanism —
  decomposition followed by parallel delegation — that the rest of the post
  elaborates on. As with `blog-cognition-auto-triage.md` Claim 1, treat this
  as an existence claim for a shipped feature, not evidence of
  decomposition quality or delegation accuracy at any particular rate.

### Claim 2: Each managed Devin is a full Devin instance running in its own isolated virtual machine, with its own terminal, browser, development environment, session link, and the ability to independently run shell commands, execute tests, and verify its own changes before reporting back
- **Evidence**: Direct architectural description enumerating per-instance
  resources and per-instance capabilities.
- **Confidence**: emerging (specific architectural claim for a shipped
  feature — isolated VM per child, not a shared sandbox — but no detail on
  how VM provisioning time, resource limits, or per-VM cost work)
- **Quote**: "Each managed Devin is a full Devin, running in its own isolated virtual machine with its own terminal, browser, and development environment. Each one can independently run shell commands, execute tests, and verify its own changes before reporting back. Each has its own session link, so you can inspect its work or message it directly."
- **Our assessment**: The specific architectural choice — full VM isolation
  per child, rather than, e.g., separate processes or containers sharing a
  host — is the concrete infrastructure claim underlying the rest of the
  post's benefits (clean context, independent test runners). It is the same
  isolation principle already documented for individual Devin sessions in
  `blog-cognition-verifying-agentic-development.md` (computer-use testing
  runs "in the cloud," observed at "10 to 20 Devins in parallel, each with
  its own dev server" — Claim 3 there), extended here to apply per-child
  within a single coordinated task rather than per-independent-session
  across unrelated tasks. No detail is given on whether managed-Devin VMs
  are billed/provisioned differently from top-level Devin sessions.

### Claim 3: The parent Devin session acts as a coordinator — it scopes the work, assigns each piece to a managed Devin, monitors progress, resolves conflicts, and compiles the results
- **Evidence**: Direct role-definition statement for the top-level session.
- **Confidence**: anecdotal (names five coordinator responsibilities as a
  list with no mechanism description for any of them — "resolves any
  conflicts" in particular is asserted with zero detail on what a conflict
  looks like or how resolution is decided)
- **Quote**: "The main Devin session acts as a coordinator: it scopes the work, assigns each piece to a managed Devin, monitors progress, resolves any conflicts, and compiles the results."
- **Our assessment**: This is a named orchestrator role with a five-item
  responsibility list, but "resolves any conflicts" is the single least
  substantiated phrase in the entire post — no example of what a conflict
  between managed Devins looks like (competing file edits? contradictory
  test results? overlapping scope?) or how the coordinator adjudicates it is
  given anywhere in the source. This maps onto the named
  "orchestrator-subagent" pattern in
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 (Anthropic's
  recommended default multi-agent topology), but that source's Claim 3
  explicitly names "information bottleneck" as orchestrator-subagent's core
  failure mode when subagents discover cross-cutting insights — this post
  asserts conflict resolution as a solved coordinator capability without
  addressing whether or how it avoids that named failure mode.

### Claim 4: The stated rationale for decomposition is that a single agent session handling too many things accumulates context, degrading focus and per-subtask quality; each managed Devin instead gets a clean slate, a narrow focus, its own shell, and its own test runner
- **Evidence**: Direct causal claim (context accumulation → degraded focus →
  degraded subtask quality) followed by the stated design response (clean
  slate + narrow focus + isolated tooling per child).
- **Confidence**: anecdotal (asserted causal mechanism with no supporting
  data — no before/after quality comparison between single-session and
  managed-Devin decomposition for the same task)
- **Quote**: "This matters because when one agent tries to handle too many things in a single session, context accumulates, focus degrades, and the quality of each subtask suffers. Each managed Devin gets a clean slate, a narrow focus, its own shell, and its own test runner."
- **Our assessment**: This restates, without new evidence, the "context
  overload" ceiling already established in this corpus as Claim 2 of
  `blog-addyosmani-code-agent-orchestra.md` ("Single-agent interaction has a
  hard ceiling from three constraints: context overload, lack of
  specialization, and no coordination") and as Claim 8 of
  `blog-anthropic-multi-agent-coordination-patterns.md` (context-duration as
  the decision criterion between orchestrator-subagent and agent teams).
  What this source adds is not a new argument for context isolation as a
  design principle — that is already well-corroborated in the corpus — but
  a concrete, named product instantiation of it: "clean slate, narrow focus,
  its own shell, and its own test runner" as the specific four-part bundle
  each managed Devin receives.

### Claim 5: Devin can read the full execution trajectories of its managed Devins to understand what worked, what didn't, and where they got stuck, and use that to improve how it breaks down the next task — described as a compounding effect where each managed Devin makes the next one more effective
- **Evidence**: Direct feedback-loop description with an explicit
  compounding claim.
- **Confidence**: anecdotal (asserted improvement mechanism with no
  measurement — no data on how much decomposition quality actually improves,
  how many trajectories are needed before improvement is observed, or
  whether this happens within a single coordinator session or persists
  across sessions)
- **Quote**: "Devin can also read the full trajectories of its managed Devins to understand what worked, what didn't, and where they got stuck, and use that to improve how it breaks down the next task. Over time, each managed Devin makes the next one more effective."
- **Our assessment**: This is the single most novel mechanism claim in the
  post and the one the Prospector's triage flagged as the key differentiator
  from prior corpus material — it is a concrete feedback loop for
  orchestration quality that reads the *process* record (full child
  trajectories: actions taken, dead ends, recoveries) rather than just the
  *output* (final diff or test result). This is conceptually adjacent to
  but distinct from the deterministic-skill-extraction loop in
  `blog-cognition-verifying-agentic-development.md` Claim 7 (Devin proposing
  a newly-learned setup step as a reusable skill via a one-click PR): that
  mechanism captures a specific, reusable procedural fact (how to log in);
  this mechanism is vaguer and broader — "understand what worked" and
  "improve how it breaks down the next task" — with no named artifact (no
  skill file, no PR, no explicit "lesson" object) produced from the
  trajectory review. Whether this improvement happens through in-context
  reasoning within the same coordinator session, or persists as a durable
  artifact across sessions, is not stated; the post gives no mechanism for
  *how* trajectory-reading translates into better decomposition, only that
  it does. Treat this as an unverified capability claim, not a documented
  technique — it lacks the specific mechanism detail
  (`blog-cognition-verifying-agentic-development.md` Claims 5-6, e.g., which
  disclose a named root cause and a specific TDD-style debiasing
  explanation) that would make it independently reusable guidance.

### Claim 6: The coordinator can message managed Devins mid-task to send instructions, context, or corrections to any child session
- **Evidence**: Bulleted capability-list item under "What Devin can do."
- **Confidence**: anecdotal (capability listed with zero example of a
  correction message or its effect)
- **Quote**: "Message child sessions: send instructions, context, or corrections to any managed Devin mid-task"
- **Our assessment**: This is a specific human-parity capability — the
  coordinator (itself an agent) can intervene in a running child session the
  same way a human supervisor could message a running Devin session
  directly (per the "own session link" detail in Claim 2). It is a concrete
  instance of agent-to-agent steering mid-execution, distinct from the more
  common "spawn and wait for the final report" pattern documented elsewhere
  in this corpus's subagent material (e.g.
  `blog-addyosmani-code-agent-orchestra.md` Claim 3, parent spawns subagents
  in parallel and waits for their reports) — here the parent can actively
  redirect a child while it is still running, not just consume its final
  output.

### Claim 7: The coordinator can monitor ACU (a Cognition-internal compute-consumption unit) consumption per child session
- **Evidence**: Bulleted capability-list item.
- **Confidence**: anecdotal (named but undefined unit — "ACU" is not
  expanded or defined anywhere in the post)
- **Quote**: "Monitor ACU consumption: track how much compute each child session is using"
- **Our assessment**: "ACU" is used without definition in this post (the
  Prospector's triage comment independently flagged "ACU monitoring" as a
  concrete product detail worth noting). This note cannot resolve what ACU
  stands for or how it is priced from this source alone — it should be
  cited only as "Cognition names a per-child compute-consumption metric
  (ACU) that the coordinator can monitor," not as a specific cost or pricing
  claim, since no conversion rate, dollar figure, or definition is given in
  this article.

### Claim 8: The coordinator can put child sessions to sleep or terminate them — pausing or stopping any managed Devin that is done or going off track
- **Evidence**: Bulleted capability-list item naming two distinct lifecycle
  actions (pause vs. stop) and two named triggers (done vs. off-track).
- **Confidence**: anecdotal (capability named with no detail on how
  "off track" is detected — automatically by the coordinator, or only on
  human instruction relayed through the coordinator)
- **Quote**: "Put child sessions to sleep or terminate them: pause or stop any managed Devin that's done or going off track"
- **Our assessment**: This is a concrete kill-switch/pause mechanism at the
  child-session level, directly analogous to the "kill stuck agents after
  3+ iterations on the same error" heuristic already in this corpus
  (`blog-addyosmani-code-agent-orchestra.md` Claim 12) — but this source
  does not state whether the *coordinator agent itself* decides when a child
  is "going off track" (an autonomous kill decision) or whether this is a
  human-facing control surface the coordinator merely exposes. This
  ambiguity matters for the guide: an autonomous parent-kills-child decision
  is a different (and less externally auditable) safety property than a
  human-in-the-loop kill switch, and the post does not disambiguate which
  one this is.

### Claim 9: The coordinator can schedule messages to itself, setting up follow-ups and checkpoints so it stays on top of progress
- **Evidence**: Bulleted capability-list item.
- **Confidence**: anecdotal (capability named with no example checkpoint
  schedule or cadence given, unlike the specific "15-minute cadence" rule
  already documented elsewhere in this corpus)
- **Quote**: "Schedule messages to itself: set up follow-ups and checkpoints so the coordinator stays on top of progress"
- **Our assessment**: This is a self-scheduling capability for the
  coordinator's own check-in cadence, distinct from but thematically related
  to the fixed "15-minute cadence" heuristic from
  `blog-addyosmani-code-agent-orchestra.md` (Linked Source 5, Coding Agents
  Manager post) already cited in the guide's Multi-Agent Orchestration
  section (`guide/01-daily-workflows.md`, "The 15-minute cadence"). That
  prior source names a specific cadence number as human-facing management
  guidance; this source describes a product feature letting the coordinator
  *agent itself* set its own checkpoint schedule, with no stated default or
  recommended interval — a mechanism for the pattern, not a validated
  cadence.

## Concrete Artifacts

### Five verbatim example task-decomposition prompts, from the "Try it now" section

These are the most concrete, reusable artifacts in the source — each names
a task category and shows the actual prompt language used to trigger
managed-Devin decomposition. Retrieved via a targeted follow-up fetch after
the initial page fetch truncated them; confirmed as the full, untruncated
text.

```
Source: cognition.com/blog/devin-can-now-manage-devins, "Try it now" section

1. QA your application in parallel:
"QA all pages in our application for the new light mode. Break this down
by page and spin up a managed Devin for each one. Each should navigate to
its page, test the components, take screenshots, and report back. Compile
a summary of what passed and what failed in an .md file. Use a 2-column
(side by side) image layout."

2. Run a large-scale migration:
"Migrate our frontend codebase from one icon library to another. Create a
reusable instruction for each independent piece of the migration, then
spin up managed Devins to execute each part in parallel. Each should
verify its changes by running tests before reporting back."

3. Run a security and dependency audit:
"Run a security and dependency audit across our codebase. Spin up one
session per service or package (10 at a time) to check for
vulnerabilities, outdated deps, and license issues, then compile the
results into a single report."

4. Refactor across your codebase:
"Refactor all class components in our codebase to functional components
with hooks. Break this into independent batches, spin up a managed Devin
for each batch, and compile the results into a set of PRs."

5. Test recently shipped features:
"Find 10 features that were recently touched based on merged PRs, and
spin up a session for each one to test it end-to-end. Attach a test
report from each session and summarize the overall results."
```

### Bulleted capability list, verbatim

```
Source: cognition.com/blog/devin-can-now-manage-devins, "What Devin can do" section

- Spin up managed Devins: Devin breaks a task into scoped pieces and
  delegates each to a separate session
- Message child sessions: send instructions, context, or corrections to
  any managed Devin mid-task
- Monitor ACU consumption: track how much compute each child session is
  using
- Put child sessions to sleep or terminate them: pause or stop any
  managed Devin that's done or going off track
- Schedule messages to itself: set up follow-ups and checkpoints so the
  coordinator stays on top of progress
```

### Section structure

```
Section structure of the source article (headings, in order):
1. Devin Can Now Manage a Team of Devins (intro, unheaded body)
2. What Devin can do
3. Try it now
Source: cognition.com/blog/devin-can-now-manage-devins, "By The Cognition Team," 03.19.26
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-code-agent-orchestra.md` Claim 2 ("Single-agent
    interaction has a hard ceiling from three constraints: context
    overload, lack of specialization, and no coordination") — this source's
    Claim 4 (context accumulation degrades single-session subtask quality;
    managed Devins get a clean slate and narrow focus) is a concrete, named
    product response to exactly the context-overload constraint Osmani
    states structurally. Both sources treat context isolation as the primary
    justification for decomposing work across multiple agent instances
    rather than handling it in one long-running session.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 (Anthropic's
    recommended default pattern is orchestrator-subagent, "the widest range
    of problems with the least coordination overhead") and Claim 8 (context
    duration determines orchestrator-subagent vs. agent teams: short,
    focused, single-invocation subtasks favor orchestrator-subagent) — this
    source's coordinator/managed-Devin architecture (Claims 1-3) is a
    concrete, shipped product instantiation of exactly the
    orchestrator-subagent pattern Anthropic names and recommends as the
    default topology, from an independent vendor (Cognition rather than
    Anthropic). The bounded, scoped-piece delegation described here (Claim 1:
    "break down large tasks and delegate them... that work in parallel")
    matches Anthropic's stated criterion for orchestrator-subagent over
    agent teams — subtasks that "produce clear outputs within a single
    invocation" — rather than the sustained, familiarity-accumulating
    engagement Anthropic reserves for agent teams.
  - `blog-cognition-verifying-agentic-development.md` Claim 3 (engineers
    observed running "10 to 20 Devins in parallel, each with its own dev
    server," described as "something you simply can't do on a single
    laptop") — this source's Claim 2 (each managed Devin runs in its own
    isolated VM with its own terminal, browser, and environment) is the same
    per-instance cloud-VM isolation principle, now applied specifically to
    children spawned *within* a single coordinated task rather than to
    independent top-level sessions a human runs directly.
  - `blog-cognition-auto-triage.md` Claim 3 ("Devin can inspect the
    codebase, check observability tools, look through related tickets or
    threads, ask for missing context, and spin up sub-Devins to investigate
    in parallel") — this is the same self-spawning sub-Devin mechanism
    named here, applied in that source to incident investigation rather
    than general task decomposition; together the two sources show
    Cognition applying the same "spin up sub-Devins" primitive to at least
    two distinct product surfaces (Auto-Triage and general task management),
    which supports reading "managed Devins" as underlying platform
    infrastructure rather than a feature built for one narrow use case.
  - `blog-cognition-devin-in-windsurf.md` Claim 4 (Cognition's own
    retrospective naming "managing teams of sub-agents in parallel" as one
    of four milestones in Devin's progression toward operating without a
    human in the loop) — this source is the dedicated, detailed product
    announcement for exactly that named milestone; the Windsurf post's
    Claim 4 lists it only as a one-line item in a four-item retrospective
    with no elaboration, while this source supplies the mechanics
    (isolated VMs, coordinator responsibilities, capability list, example
    prompts) that milestone item lacked.

- **Contradicts**: None filed. This source's Claim 3 ("resolves any
  conflicts") sits in unaddressed tension with
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3
  (orchestrator-subagent's core failure mode is an information bottleneck
  when subagents discover cross-cutting insights the orchestrator does not
  see) — but this does not meet the MINER.md §4a bar for filing a
  contradiction issue: Anthropic's claim names a failure mode that can
  occur under the orchestrator-subagent pattern, while this source merely
  asserts a coordinator responsibility without providing a mechanism to
  evaluate against that failure mode. The two claims are not making opposing
  factual assertions under matching conditions (one is a named risk, the
  other is an unsubstantiated capability claim); it is a gap in evidentiary
  depth on Cognition's side, not a direct conflict. Worth flagging in Guide
  Impact as an open question rather than escalating to a contradiction
  issue.

- **Extends**:
  - `guide/01-daily-workflows.md` "Multi-Agent Orchestration" section
    (currently anchored by `blog-addyosmani-code-agent-orchestra.md`) — this
    source adds a second, independent vendor's shipped self-spawning
    orchestration product (Devin managing Devins) alongside the guide's
    existing Claude-Code-centric coverage (subagents via the Task tool,
    agent teams via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). Where the
    existing guide content documents *how a human* orchestrates multiple
    agents, this source documents a product where *an agent itself* is the
    orchestrator/coordinator of other agent instances — a pool-based,
    self-spawning variant not previously covered under that section.
  - `blog-anthropic-multi-agent-coordination-patterns.md` — extends
    Anthropic's abstract five-pattern taxonomy with a concrete, named,
    shipped product implementation of the orchestrator-subagent pattern from
    a different vendor, including a specific value proposition (context
    isolation per subtask) and reusable example prompts that Anthropic's
    more abstract framework document does not supply.

- **Novel**: The trajectory-reading feedback loop (Claim 5: parent Devin
  reads full child execution histories to improve future task decomposition,
  described as making "each managed Devin more effective" over time) is new
  to this corpus at the level of a named, if underspecified, mechanism — no
  existing source note describes a coordinator agent reading complete
  subagent execution traces (not just final outputs) specifically to improve
  its own future decomposition strategy. The five verbatim example
  decomposition prompts (Concrete Artifacts) are also novel: no existing
  source note in this corpus provides ready-to-adapt prompt templates for
  parallel QA, migration, security-audit, refactor, and feature-testing
  task decomposition across multiple agent instances.

## Guide Impact

- **Chapter 01 (Daily Workflows), "Multi-Agent Orchestration" section**: Add
  this source as a second, independent-vendor example of the
  orchestrator-subagent pattern already anchored by
  `blog-addyosmani-code-agent-orchestra.md` and formalized in
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7. Specifically
  cite Claim 4 (context isolation per subtask: clean slate, narrow focus,
  own shell, own test runner) as a second corroborating source for the
  context-overload rationale already in that section, and cite the five
  example prompts (Concrete Artifacts) as reusable prompt templates readers
  can adapt for QA, migration, audit, refactor, and feature-testing
  decomposition tasks. Flag clearly that this is a vendor feature
  announcement with zero adoption, accuracy, or outcome data — cite for the
  pattern and the prompt templates, not as evidence the pattern works
  reliably.
- **Chapter 01 (Daily Workflows), "Multi-Agent Orchestration" section**: The
  post's unsubstantiated "resolves any conflicts" claim (Claim 3) is worth
  flagging as an open question rather than a documented technique: the
  guide should not present "the coordinator resolves conflicts" as a solved
  problem on this source's authority alone, since no mechanism is given and
  it sits unaddressed against the named orchestrator-subagent information-
  bottleneck failure mode in `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 3.
- **Chapter 02 (Harness Engineering)**: If the guide adds content on
  compounding operational knowledge across agent sessions, note that Claim 5
  (trajectory-reading feedback loop) is a *weaker*, less-specified sibling
  of the shipped, concrete mechanism already documented in
  `blog-cognition-verifying-agentic-development.md` Claim 7 (Devin proposing
  a newly-learned setup step as a named "testing skill" via a one-click PR)
  — this source should not be cited as adding a new, independently
  actionable compounding-knowledge technique; it should be cited only as a
  second data point that Cognition is pursuing this general direction across
  more than one product surface.

## Extraction Notes

- The article is very short (~200 words across an intro, a five-item
  bulleted capability list, and a "Try it now" section with five example
  prompts). Fetched via WebFetch, which on the first pass returned the
  article body reasonably completely but only listed the five example
  prompts as short paraphrased labels rather than their full text — this is
  the same truncation behavior already documented as a WebFetch limitation
  in several other Cognition source notes in this corpus (e.g.
  `blog-cognition-devin-productivity-estimation.md`,
  `blog-cognition-devin-in-windsurf.md` Extraction Notes). A second,
  targeted follow-up fetch specifically requesting the full, untruncated
  text of each example prompt was used to obtain the Concrete Artifacts
  block above; a third fetch cross-checked visual elements and outbound
  links (all of which were either related-post thumbnails, the Devin
  platform link, or standard footer/social links — none substantive enough
  to follow per MINER.md §1).
- No sub-pages were followed as substantive linked sources: the outbound
  links found (via a dedicated visual-elements/links fetch) are eight
  related-blog-post thumbnails (titles only, no elaboration), a link to
  `devin.ai`, the five `app.devin.ai/?prompt=...` deep links (which
  duplicate the example-prompt text already captured verbatim above, not
  new content), and standard LinkedIn/X/legal footer links. None met the
  "substantive" bar for following per MINER.md §1.
- Confidence is rated `anecdotal` overall, one tier below the `emerging`
  rating given to the evidentially similar `blog-cognition-devin-in-windsurf.md`
  and `blog-cognition-auto-triage.md`: this source has no named customer
  quote (unlike Auto-Triage's Modal quote) and its most novel claim (Claim 5,
  the trajectory-reading feedback loop) is asserted with less mechanism
  detail than either of those posts' comparably-tiered claims — "understand
  what worked... and use that to improve" has no named artifact, no example,
  and no stated persistence mechanism, whereas the comparably-anecdotal
  claims in the other two Cognition posts at least name a specific
  mechanism (e.g. Auto-Triage's three-tier outcome routing, Windsurf's
  named single-click handoff).
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts for the one candidate considered (tension
  between this source's unsubstantiated "resolves any conflicts" claim and
  Anthropic's named orchestrator-subagent information-bottleneck failure
  mode) and rejected as an evidentiary gap rather than a same-claim
  conflict. No contradiction issue filed.
- Cross-references verified before writing: re-read
  `blog-addyosmani-code-agent-orchestra.md` in full and confirmed Claims 2,
  3, 8, and 12 by number and content; re-read
  `blog-anthropic-multi-agent-coordination-patterns.md` in full and
  confirmed Claims 3, 7, and 8 by number and content; re-read
  `blog-cognition-verifying-agentic-development.md` in full and confirmed
  Claim 3 and Claim 7 by number and content; re-read
  `blog-cognition-auto-triage.md` in full and confirmed Claim 3 by number
  and content; re-read `blog-cognition-devin-in-windsurf.md` in full and
  confirmed Claim 4 by number and content. No claim number was guessed or
  approximated. The `guide/01-daily-workflows.md` "Multi-Agent
  Orchestration" section was read directly (not from a triage comment's
  chapter numbering) to confirm both the section's existence and its
  current source anchoring before writing Guide Impact.
