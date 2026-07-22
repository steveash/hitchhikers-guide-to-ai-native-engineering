---
source_url: https://cognition.com/blog/multi-agents-working
source_type: blog-post
title: "Multi-Agents: What's Actually Working"
author: Walden Yan (Cognition)
date_published: 2026-04-22
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: emerging
issue: "#2139"
---

# Multi-Agents: What's Actually Working

> Cognition's Walden Yan revisits his own earlier "Don't Build Multi-Agents"
> post with ~10 months of production deployment experience across Devin and
> Windsurf, arguing multi-agent systems now work in a narrower form than the
> failed parallel-writer swarms he originally warned against: setups where
> "multiple agents contribute intelligence to a task while writes stay
> single-threaded" — demonstrated through a clean-context code-review loop, a
> "Smart Friend" small/large model pairing, and manager-child task delegation.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, byline "By Walden
  Yan," published "04.22.26" per the page's own byline format — the same
  MM.DD.YY convention used across this corpus's other Cognition posts, e.g.
  `blog-cognition-devin-schedule-devins.md`'s "03.20.26"). Walden Yan is named
  directly (not the anonymous "Cognition Team" byline used on several other
  posts in this corpus), and the post is an explicit first-person sequel: "10
  months ago, I wrote Don't Build Multi-Agents."
- **Author credibility**: First-party Cognition practitioner post from a
  named author revisiting his own prior public position based on subsequent
  production deployment experience (Devin, Windsurf/Cascade, Devin Review).
  This is not a case study with named customers — no customer is quoted here
  — but it is more evidentially grounded than a pure product announcement: it
  reports a concrete internal metric (Devin Review catches ~2 bugs/PR, 58%
  severe), a concrete usage-growth figure (~8x enterprise usage over 6
  months), and an explicit admission of what did NOT work (SWE-1.5 was "not
  good enough" as a primary model in the Smart Friend pairing). Treat the
  metrics as first-party, unaudited, and without stated methodology; treat
  the architectural framing (single-threaded writes as the dividing line)
  as Cognition's own synthesized position, not an industry consensus.
- **Scope**: Covers three practitioner-tested multi-agent patterns (clean-
  context code review, small/large "Smart Friend" model pairing, and
  manager-child task delegation), the context-engineering principles carried
  over from the author's prior post, and an explicit rejection of
  "unstructured swarm" architectures. Does **not** cover: the actual
  prompting or scaffolding code for any of the three patterns; a benchmark or
  controlled comparison for any claimed metric; named customers or session
  counts; or technical detail on how the "internal MCP" used for manager-child
  coordination is implemented.

## Extracted Claims

### Claim 1: Cognition now reports multi-agent systems working in production when writes stay single-threaded and additional agents only contribute intelligence, not actions — a narrower, revised claim than the author's own prior "Don't Build Multi-Agents" position
- **Evidence**: Direct framing statement early in the post, explicitly
  contrasted with "parallel-writer swarms," which the author says still
  don't see meaningful adoption.
- **Confidence**: emerging (first-party revision of a public position, based
  on ~10 months of subsequent production deployment; not a controlled study)
- **Quote**: "we've found a narrower class of patterns that do [work]: setups where multiple agents contribute intelligence to a task while writes stay single-threaded." / "multi-agent systems work best today when writes stay single-threaded and the additional agents contribute intelligence rather than actions."
- **Our assessment**: This is the post's organizing thesis and the frame
  every other claim below serves as evidence for. It is a meaningfully
  different, narrower claim than "build multi-agent systems" — it draws a
  specific dividing line (does any agent besides the single primary writer
  make write actions?) rather than a general endorsement of multi-agent
  architectures. See Cross-References → Contradicts: this framing directly
  conflicts with `blog-cursor-agent-swarm-model-economics.md`'s description
  of Cursor's own actively-invested, concurrently-writing swarm harness — a
  contradiction filed as issue #2149. That issue was closed and labeled
  `rejected` by an automated pre-screen (which expects raw source URLs
  pasted into the issue body, and flagged that the template's internal
  source-note file references "does not contain actual web URLs to the
  sources being compared"); despite the closure an automated Assayer
  contradiction assessment was still posted on
  the issue, proposing verdict `debated` / a proposed C-009 entry not yet
  appended to CONTRADICTIONS.md. No verdict is picked in this note.

### Claim 2: Cognition's context-engineering principles from the prior post — share as much context as possible between agents, and remember that actions carry implicit decisions that can conflict across parallel writers — still hold and are described as the root cause of most multi-agent fragility
- **Evidence**: Direct restatement of two named principles from the author's
  earlier post, presented as the reason most multi-agent setups today remain
  limited to "readonly" subagents (web search, code search).
- **Confidence**: emerging (first-party restated framework; carried forward
  from an earlier post not separately mined in this corpus)
- **Quote**: "Actions carry implicit decisions. When one agent makes certain changes or edits, it might make implicit choices (style, code patterns, how certain edge cases should be handled) that might conflict with the implicit choices of other parallel agents." / "most multi-agent setups in the world are limited to 'readonly' subagents, like web search subagents and code search subagents."
- **Our assessment**: This is the mechanism-level justification for Claim
  1's single-threaded-write dividing line — it names *why* concurrent writes
  are fragile (implicit, uncoordinated style/edge-case decisions), not just
  that they are. The "readonly subagent" framing corroborates
  `blog-humanlayer-skill-issue-harness-engineering.md` Claim 6 (sub-agents
  work as a "context firewall" for isolating discrete tasks, but role-based
  write specialization does not work) from an independent vendor.

### Claim 3: A ~8x usage growth in Devin's largest, historically most cautious enterprise segment over six months has created both a "push" (users experimenting with more multi-agent setups as capability and volume grow) and a "pull" (rising costs motivating cheaper multi-agent architectures as a substitute for frontier-model-only usage) toward multi-agent systems
- **Evidence**: A cited usage figure for the "largest enterprises segment,"
  described as "traditionally... cautious toward adopting new technologies,"
  plus a stated causal narrative connecting usage growth to both experimental
  multi-agent adoption and cost-driven interest in multi-agent cost savings.
- **Confidence**: anecdotal (single first-party usage figure for one
  unnamed customer segment; no comparison cohort, no absolute session count,
  and the push/pull causal narrative is the author's own interpretation, not
  a measured driver analysis)
- **Quote**: "Even when we look at Devin usage in our largest enterprises segment, the segment that has traditionally been cautious toward adopting new technologies, we see an explosion over the last 6 months (~8x)." / "This explosion of usage has led to both a push and a pull to multi-agents."
- **Our assessment**: The 8x figure is offered as backdrop, not as
  supporting evidence for any specific multi-agent claim — it is used to
  motivate why multi-agent coordination overhead (management, planning,
  reviewing) became a bottleneck worth solving, and separately why cost
  pressure (referencing the upcoming "Mythos class" of larger models) makes
  cheaper multi-agent substitutes for frontier-only usage attractive. Both
  halves of the causal story are asserted, not measured.

### Claim 4: Cognition explicitly distinguishes its own multi-agent experiments from a wave of large-scale agent-swarm demos (a 200k-LOC browser, a 100k-LOC C compiler, a 10k+-iteration LLM training script optimization), on the grounds that those demos share a simple, verifiable success criterion that most real software lacks
- **Evidence**: Direct comparison naming three specific external demos by
  scale, followed by an explicit statement of what distinguishes "real
  software" from those demo tasks.
- **Confidence**: anecdotal (a stated distinction/framing, not a measured
  comparison; none of the three named demos is independently re-verified in
  this extraction)
- **Quote**: "These are exciting but they all share a property most real software doesn't: a simple, verifiable success criterion. Real software requires a system that scales human taste and decision-making, which is the context in which we set out to explore multi-agent systems."
- **Our assessment**: This is a specific, citable articulation of why
  large-agent-count demo results (a category this corpus already documents
  independently — the Cursor web-browser-building swarm is referenced in
  `blog-addyosmani-code-agent-orchestra.md`'s "Self-Improving Agents" source,
  and a related Cursor swarm is documented in depth in
  `blog-cursor-agent-swarm-model-economics.md`) may not transfer to
  "real software" work with subjective, taste-dependent success criteria.
  It functions as Cognition's stated rationale for testing multi-agent
  patterns against production engineering work rather than a benchmarkable
  demo task — worth flagging directly against the "objective-driven
  optimization" framing in `blog-cursor-multi-agent-kernels.md` Claim 10,
  which explicitly argues optimization tasks with continuous, verifiable
  metrics are architecturally distinct from tasks like these that require
  human taste.

### Claim 5: A code-review loop where a clean-context Devin Review agent reviews Devin's own PRs catches an average of 2 bugs per PR, roughly 58% of which are severe (logic errors, missing edge cases, security vulnerabilities), and Devin now iterates against Devin Review before a human ever opens the PR
- **Evidence**: Direct first-party metric with a named breakdown by
  severity category, plus a description of the iterate-before-human-review
  workflow this enables.
- **Confidence**: emerging (specific, first-party quantified metric; no
  stated sample size, measurement window, or methodology for how "severe"
  was classified)
- **Quote**: "even on PRs written by Devin, Devin Review catches an average of 2 bugs per PR, of which roughly 58% are severe (logic errors, missing edge cases, security vulnerabilities)." / "Today, we make Devin and Devin Review natively iterate against one another, so that most bugs are already resolved by the time a human opens the PR."
- **Our assessment**: This is a concrete instance of the generator-verifier
  coordination pattern already named and taxonomized in
  `blog-anthropic-multi-agent-coordination-patterns.md`. Unlike that post's
  named failure mode (Claim 2 there, the "early victory problem" — a
  verifier that rubber-stamps on vague criteria), this Cognition instance
  reports the verifier finding real, severe issues at meaningful volume,
  which — if the 58%-severe figure holds — would be a positive existence
  proof that a generator-verifier loop can avoid that failure mode in
  practice, at least for a code-review use case. No sample size is given,
  so the figure should be cited as a vendor-reported rate, not a benchmarked
  result.

### Claim 6: The counterintuitive design choice behind Claim 5's success is that the coding and review agents deliberately do NOT share context beforehand — a clean-context reviewer catches more because it is forced to reason backward from the implementation without the original spec, and because a shorter context avoids "context rot," a documented phenomenon where models make less intelligent decisions at longer context lengths
- **Evidence**: Direct architectural explanation, citing "Context Rot" by
  name with an external hyperlink (to trychroma.com/research/context-rot) as
  the underlying mechanism, plus a stated behavioral rationale (the review
  agent openly questions things the original agent overlooked, including
  cases where "a user telling the agent to implement an insecure pattern"
  went unchallenged).
- **Confidence**: emerging (a specific, named mechanism — context rot — cited
  from external research as the explanation for an internally observed
  effect; the causal link between "clean context" and "more bugs found" is
  Cognition's own interpretation, not independently isolated by an ablation)
  in this post)
- **Quote**: "we found this technique to work best when the coding and review agents do not share any context beforehand." / "[Context Rot](https://www.trychroma.com/research/context-rot) is a well-documented phenomenon that is a result of models making less intelligent decisions at longer and longer context lengths." / "The dedicated review agent gets to skip this extraneous context, only look at the diff, and re-discover any context it needs as it reads the code from scratch."
- **Our assessment**: This is the single most transferable, actionable
  finding in the post. It directly corroborates
  `blog-humanlayer-skill-issue-harness-engineering.md` Claim 6 (sub-agents
  as a context firewall) and Claim 13 (which independently cites the same
  Chroma context-rot research), and
  `blog-anthropic-session-management-1m-context.md` Claim 8 (context rot
  means "the model is at its least intelligent point when compacting"). Three
  independent vendor/practitioner sources now cite Chroma's context-rot
  research as the mechanism behind a design decision — clean context for a
  reviewer here, avoiding stale context at compaction there — giving this a
  stronger evidentiary base than a single anecdote. The specific example
  given (the review agent catching an insecure pattern the user explicitly
  asked for, which the coding agent complied with due to shared context/
  instruction-following bias) is a concrete, quotable illustration of why
  a verifier without the generator's priors can catch what the generator
  cannot.

### Claim 7: Making the clean-context review loop work in practice required a separate "communication bridge" — Devin must filter Devin Review's findings against its own broader context of user instructions and decisions to avoid disobeying the user, doing out-of-scope work, or looping indefinitely — and Cognition reports today's models can make "reasonable judgment calls" here with dedicated prompting
- **Evidence**: Direct description of a second, distinct engineering problem
  (beyond the clean-context design itself): synthesizing a context-free
  reviewer's output back into a context-rich coder's decision-making.
- **Confidence**: anecdotal (a described capability with no metric — "some
  dedicated prompting" and "reasonable judgment calls" are qualitative,
  unquantified claims)
- **Quote**: "does Devin properly use its broader context of user instructions, decisions, etc. to filter the bugs that come back from Devin Review? This is key to preventing looping, disobeying the user, doing work that is out of scope, and so on. We found that with some dedicated prompting, models today can make reasonable judgment calls here."
- **Our assessment**: This is the named failure mode this pattern must guard
  against, and it is structurally identical to
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3's
  "information bottleneck" failure mode for orchestrator-subagent systems
  (a subagent's findings must be routed back without the orchestrator losing
  or misapplying cross-cutting context) — here the roles are reversed
  (the context-free specialist is the *verifier*, and the context-rich
  *generator* must do the synthesis), but the underlying problem — routing
  findings between agents holding different slices of context without
  losing fidelity — is the same shape.

### Claim 8: "Smart Friend" pairs a smaller/faster primary model with a larger/more expensive model that the primary can consult, motivated by a described industry-wide shift back toward large, expensive frontier models (Sonnet-class to Opus-class) that will make frontier intelligence too costly for many day-to-day tasks
- **Evidence**: Direct architectural description plus a stated industry
  observation about a shift in "most popular models" from mid-sized to
  large, with a reference to an upcoming "Mythos class" of even larger
  models.
- **Confidence**: anecdotal (the "most popular models" trend claim is
  asserted without data; the architecture description itself is a concrete,
  first-party design pattern)
- **Quote**: "If you look at the most popular models over the last few months, you see a distinct shift from mid-sized models like Anthropic's Sonnet-class models to large models like Anthropic's Opus-class models for the sake of performance." / "let the primary/smaller model decide when a situation was tricky enough to be worth consulting the smarter/expensive model."
- **Our assessment**: This corroborates and gives production texture to
  `blog-addyosmani-code-agent-orchestra.md` Claim 9 (multi-model routing:
  route planning to cheaper models, implementation to capable models, review
  to security-focused models) — Smart Friend is a specific instance of
  cost-aware model routing, but distinguished by being *reactive*
  (the primary decides mid-task whether to escalate) rather than *static*
  (routing decided up front by task type).

### Claim 9: Two distinct, hard sub-problems make Smart Friend difficult to engineer: (a) the primary model must learn to recognize when it is at its own limits and knows what to ask, despite being the weaker model in the pair — the inverse of the more common smart-orchestrator/dumb-subagent setup — and (b) the smart friend must know how to respond usefully rather than fabricating an answer when the primary's shared context is insufficient, including proactively flagging guidance the primary didn't ask for
- **Evidence**: Two named sub-sections in the post ("The primary model needs
  to know how to talk to smart friend" and "The smart friend needs to know
  how to talk back to the primary model"), each with a described failure
  mode and mitigation approach (sharing a full context fork by default;
  instructing the primary to investigate a specific file rather than
  guessing; the smart friend proactively over-scoping its answer).
- **Confidence**: anecdotal (described design problems and mitigations;
  no measurement of how often each failure mode occurs or how much each
  mitigation improves outcomes)
- **Quote**: "The core trickiness of this setup comes from the problem of 'how does a dumber model know it's at its limits?'" / "the right answer from the smart model is not to make up some theories (which is often the default behavior), but to specifically instruct the primary model to investigate this file and ask again later." / "it's often also fruitful to ask the smart friend to look beyond the question the primary model is asking, and suggest any important guidance based on the agent trajectory, even if the primary model didn't ask for it."
- **Our assessment**: The explicit naming of "the smart model's default
  behavior is to make up some theories" when under-informed is a specific,
  transferable failure-mode warning for any escalation-based multi-agent
  design: a more capable consultant model asked an under-specified question
  will confabulate rather than push back, unless explicitly instructed to
  request more information instead. This is a concrete guardrail
  recommendation ("share a full context fork," not a curated subset) that
  the guide can state directly.

### Claim 10: In practice, Smart Friend did not work well pairing Cognition's own smaller model (SWE-1.5) as primary with Sonnet 4.5, because the intelligence gap between them was too wide specifically in the two skills the pattern depends on (knowing when to escalate, knowing what to ask); Cognition frames this as a training problem it expects future SWE model generations to address, and reports the pattern "starts to pay off" with the newer SWE-1.6 model, though still not fully
- **Evidence**: Explicit first-party negative result ("We should be upfront:
  SWE 1.5 was not good enough at being the primary model for this setup to
  really work"), with a named follow-up model (SWE-1.6, hyperlinked, said to
  achieve "Opus-4.5 level performance on SWE-bench") reported as narrowing
  but not closing the gap.
- **Confidence**: emerging (a specific, first-party admission of failure
  with a named cause and a named partial-improvement follow-up; SWE-bench
  performance for SWE-1.6 is cited but not independently re-verified here)
- **Quote**: "The gap between it and Sonnet 4.5 was too wide in exactly the places that mattered for this setup: knowing when to escalate, knowing what to ask. The cost and speed wins were real, but the quality ceiling was set by the primary, and the primary wasn't strong enough." / "SWE 1.6 ... is meaningfully better and closes enough of that gap that the pattern starts to pay off, but it's still not where we want it. We're reasonably confident this is a training problem, and future SWE models will be trained with this back-and-forth in mind."
- **Our assessment**: This is a rare, specific negative result disclosed by
  a vendor about its own product line, which raises the credibility of the
  post's other claims by contrast — Cognition is willing to say a pattern
  did not work with its own model rather than only reporting successes.
  The stated diagnosis — the primary needs specific *escalation-judgment*
  skill, not just general capability, and this may require dedicated
  training rather than prompting alone — is a concrete, falsifiable
  hypothesis a future source could test directly.

### Claim 11: Smart Friend worked well, in production, over a meaningful stretch of time, when both models paired were frontier-tier (Claude and GPT run together) — and the nature of the coordination problem changes at that tier: it is no longer a weaker model learning when to ask a stronger one, but routing to whichever model is best suited to the specific sub-task (debugging, visual reasoning, test-writing), turning the "delegation logic" into a capability router rather than a difficulty escalator
- **Evidence**: Direct first-party positive result for frontier-to-frontier
  pairing, with an explicit distinction drawn between the two regimes
  (small-to-large escalation vs. frontier-to-frontier routing).
- **Confidence**: anecdotal (a described, unquantified production result —
  "produced real gains in the trickiest scenarios" and "a meaningful
  stretch" have no attached metric, task count, or measurement window)
- **Quote**: "We've run Claude and GPT together in this setup in production for a meaningful stretch, and it produced real gains in the trickiest scenarios." / "Cross-frontier communication is less about a weaker model knowing when to ask a stronger one, and more about routing to whichever model is best at the specific sub-task. Some models debug better, some handle visual reasoning better, some write tests better. The delegation logic becomes a capability router rather than a difficulty escalator."
- **Our assessment**: This is a distinct, useful refinement of the model-
  routing literature already in this corpus (`blog-addyosmani-code-agent-
  orchestra.md` Claim 9's "route by task type") — it specifically argues
  that once both models in a pairing are frontier-tier, the routing
  question stops being about *capability tier* (who is smart enough to
  handle this) and becomes about *specialization* (which model is better at
  this particular sub-skill, independent of general intelligence tier). No
  vendor benchmark is cited to support which model is better at which
  sub-task; this should be read as Cognition's own internal operational
  finding.

### Claim 12: Manager-child delegation is live in Devin today — a manager Devin breaks a larger task (e.g., a feature spanning ten PRs, a multi-service migration, a week of work) into pieces, spawns child Devins to work on them, and coordinates progress through an internal MCP — but making this feel coherent required more context engineering than expected, due to three specific, named failure modes
- **Evidence**: Direct architectural description of a shipped capability,
  with three explicitly named recurring problems: managers trained on
  small-scoped delegation default to being overly prescriptive when they
  lack deep codebase context; agents wrongly assume they share state with
  their children; and cross-agent communication (a child surfacing a
  finding to be relayed to siblings) doesn't happen by default because
  models haven't been trained in environments requiring it.
- **Confidence**: emerging (first-party description of a shipped,
  currently-used feature, with three specific named failure modes reported
  as still being actively worked on — "we're still improving on all of
  them" — rather than solved)
- **Quote**: "A manager Devin can break a larger task into pieces, spawn child Devins to work on them, and coordinate their progress through an internal MCP." / "Managers trained on small-scoped delegation default to being overly prescriptive, which backfires when the manager lacks deep codebase context. Agents assume they share state with their children when they don't. Cross-agent communication, a sub-agent writing messages back to its manager to be passed to other agents in the agent team, doesn't happen by default, because models haven't been trained in environments where it needed to."
- **Our assessment**: This maps directly onto the persistent Manager plane +
  ephemeral Worker plane two-plane architecture already documented in
  `discussion-hn-ttal-multiagent-factory.md` Claim 2, and the three named
  failure modes here are concrete instances of problems that taxonomy left
  abstract: "overly prescriptive managers" is a specific version of the
  orchestrator-subagent "information bottleneck" failure mode in
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3 (here, the
  bottleneck runs the other direction — top-down over-specification rather
  than lost bottom-up findings); "cross-agent communication doesn't happen
  by default" is the same problem TTal's P2P mesh topology (Claim 6 there)
  was built to solve by letting workers alert the Manager directly when
  blocked, rather than only reporting up through a queue.

### Claim 13: Cognition explicitly rejects "unstructured swarms" (arbitrary networks of agents negotiating with each other) as "mostly a distraction," stating the practical shape that works is "map-reduce-and-manage": a manager splits work, children execute, and the manager synthesizes and reports back
- **Evidence**: Direct architectural verdict stated in a rhetorical-question
  section ("What about unstructured swarms?"), naming making this kind of
  system "feel as coherent as a single agent working on a single task" as a
  focus of Cognition's work in 2026.
- **Confidence**: anecdotal (a stated architectural opinion, not a
  benchmarked comparison between "unstructured swarm" and "map-reduce-and-
  manage" approaches on the same task)
- **Quote**: "We think the unstructured-swarm approach, arbitrary networks of agents negotiating with each other, is mostly a distraction. The practical shape is map-reduce-and-manage: a manager splits work, children execute, the manager synthesizes and reports back."
- **Our assessment**: This is Cognition's explicit, general-purpose
  architectural recommendation, and it aligns closely with the vendor
  recommendation in `blog-anthropic-multi-agent-coordination-patterns.md`
  Claim 7 (orchestrator-subagent as the default pattern, handling "the
  widest range of problems with the least coordination overhead") — two
  independent vendors converge on a hub-and-spoke/orchestrator shape over a
  peer-to-peer mesh as the practical default. However, this claim is in
  direct tension with the parallel-writer swarm architecture documented in
  `blog-cursor-agent-swarm-model-economics.md` (see Cross-References →
  Contradicts, issue #2149) — that source's swarm is *also* tree-shaped
  with planner/worker roles (not an arbitrary peer-to-peer mesh), so it is
  not the "unstructured swarm" this claim targets, but it does involve
  concurrent worker writes to a shared codebase, which is the axis Claim 1
  above draws the line on.

### Claim 14: The open problems across all three patterns are communication problems — how a weaker model learns when to escalate, how a child surfaces a discovery that should change its siblings' work, and how to transfer context between agents without overwhelming the receiver — and Cognition frames the trajectory as building toward intelligence injected at every SDLC stage as "a coordinated system that scales human taste," not "a swarm of autonomous actors"
- **Evidence**: Direct closing synthesis statement, plus two footnoted
  external references: Anthropic published a related multi-agent research
  system post the day after the author's original "Don't Build Multi-
  Agents" post, and Anthropic separately launched a beta "advisor strategy"
  letting smaller models call larger ones, which the author reads as
  independent movement toward the same "smart friend" communication problem.
- **Confidence**: anecdotal (a stated synthesis and an expectation about
  future model training — "we also expect the next generation of models...
  to start closing these gaps" — not a measured prediction)
- **Quote**: "The open problems are all communication problems. How does a weaker model learn when to escalate? How does a child agent surface a discovery that should change its siblings' work? How do you transfer context between agents without drowning the receiver?" / "We're building toward a world where intelligence is injected at every stage of the software development lifecycle — planning, coding, review, testing, and monitoring — not as a swarm of autonomous actors, but as a coordinated system that scales human taste."
- **Our assessment**: This is the post's meta-conclusion, unifying Claims
  5-13 under a single framing: every pattern that worked (clean-context
  review, Smart Friend, manager-child delegation) succeeded despite, not
  because of, easy agent-to-agent communication, and every named failure
  mode traces back to a communication gap. The footnoted convergence with
  Anthropic's multi-agent research system post (published the day after the
  author's original post) and Anthropic's "advisor strategy" beta is a
  citable instance of two frontier labs independently arriving at similar
  problem framings around the same time — worth flagging as corroboration
  by convergence rather than shared methodology.

## Concrete Artifacts

### Article section structure (headings, in order)
```
Source: cognition.com/blog/multi-agents-working, "By Walden Yan," 04.22.26

1. (intro, unheaded — revisiting "Don't Build Multi-Agents" 10 months later)
2. A Refresher on Context Engineering
3. What Changed in the Last 10 Months
4. Some Practical Multi-agent Experiments
   1) The Code-Review-Loop that's so stupid it shouldn't work
   2) Large, expensive models are back - introducing "Smart Friend"
5. Looking Ahead: Higher-Level Delegation
6. What We Know Today
[1] footnote: Anthropic's multi-agent research system post, published the
    day after the author's original "Don't Build Multi-Agents" post
[2] footnote: Anthropic's "advisor strategy" beta (smaller models calling
    larger ones)
```

### Named metrics and figures, verbatim
```
Source: cognition.com/blog/multi-agents-working

- Devin usage in largest enterprise segment: ~8x over the last 6 months
- Devin Review: catches an average of 2 bugs per PR; ~58% severe
  (logic errors, missing edge cases, security vulnerabilities)
- External demo scale references (not Cognition's own): a web browser
  (200k LOC), a C compiler (100k LOC), an LLM training script
  (10k+ iterations)
- SWE-1.5: 950 tok/sec sub-frontier model, launched October (per this post)
- SWE-1.6: described as achieving "Opus-4.5 level performance on SWE-bench"
```

### Two named engineering sub-problems for Smart Friend, verbatim headers
```
Source: cognition.com/blog/multi-agents-working, "Smart Friend" section

1. The primary model needs to know how to talk to smart friend.
2. The smart friend needs to know how to talk back to the primary model
```

### Three named failure modes for manager-child delegation, verbatim
```
Source: cognition.com/blog/multi-agents-working, "Looking Ahead" section

- "Managers trained on small-scoped delegation default to being overly
  prescriptive, which backfires when the manager lacks deep codebase
  context."
- "Agents assume they share state with their children when they don't."
- "Cross-agent communication, a sub-agent writing messages back to its
  manager to be passed to other agents in the agent team, doesn't happen
  by default, because models haven't been trained in environments where
  it needed to."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2 (the
    generator-verifier "early victory problem" — a verifier that rubber-
    stamps on vague criteria) and Claim 7 (orchestrator-subagent as the
    recommended default, "the widest range of problems with the least
    coordination overhead") — this source's Claim 5 (Devin Review catching
    real, severe bugs at a stated rate) is a concrete production instance
    of a generator-verifier loop that does NOT exhibit the early-victory
    problem, and Claim 13's "map-reduce-and-manage" verdict is an
    independent, second-vendor convergence on orchestrator-subagent/
    hub-and-spoke over peer-to-peer mesh as the practical default.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 6 (sub-agents
    work as a "context firewall," but role-based specialization does not)
    and Claim 13 (Chroma's context-rot research cited as empirical backing
    for degraded performance at longer context) — this source's Claim 6
    (clean-context reviewer performs better, explicitly citing the same
    Chroma context-rot research by name and link) is a third independent
    citation of the same external research as the mechanism behind a
    context-management design decision.
  - `blog-anthropic-session-management-1m-context.md` Claim 8 (context rot
    means "the model is at its least intelligent point when compacting") —
    corroborates the general context-rot mechanism this source's Claim 6
    invokes, applied to a different scenario (compaction timing vs.
    reviewer context design).
  - `discussion-hn-ttal-multiagent-factory.md` Claim 2 (two-plane
    Manager/Worker architecture) and Claim 6 (P2P mesh topology letting
    workers alert the Manager directly when blocked) — this source's
    Claim 12 (manager-child delegation via an internal MCP) is a second,
    independently-arrived-at instance of the same two-plane shape; the
    "cross-agent communication doesn't happen by default" failure mode
    named here is the same underlying problem TTal's P2P mesh was built to
    solve.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 9 (multi-model routing:
    cheaper models for planning, capable models for implementation,
    security-focused models for review) — this source's Claims 8-11 (Smart
    Friend) are a production-tested elaboration of the same idea, adding
    the specific distinction between escalation-based routing (weak-to-
    strong, Claim 9-10 here) and capability-based routing (frontier-to-
    frontier, Claim 11 here) that Osmani's source does not draw.
  - `blog-cursor-multi-agent-kernels.md` Claim 2 (a planner agent that
    dynamically rebalances work across autonomous workers based on live
    performance metrics) — corroborates this source's Claim 12
    (manager-child delegation, coordinating child progress) as a second,
    independent instance of manager-plane coordination logic, though that
    source's planner rebalances based on a continuous benchmark signal
    (SOL scores) while this source gives no detail on what signal a Devin
    manager uses to judge child progress.

- **Contradicts**:
  - `blog-cursor-agent-swarm-model-economics.md` (Claims 1, 2, 4, 12) — this
    source's Claim 1 (parallel-writer multi-agent swarms "still don't see
    meaningful adoption," with single-threaded writes as the practically
    validated dividing line) directly conflicts with that source's
    description of Cursor's own actively-invested, concurrently-writing
    planner/worker swarm harness, validated by a controlled experiment
    (100% of a held-out SQL test suite across four model configurations
    vs. 11%-77% under the prior harness) and a from-scratch version-control
    system built specifically to make concurrent agent writes tractable at
    scale. **Filed as contradiction issue #2149** — no verdict is picked in
    this note. The issue was closed and labeled `rejected` by an automated
    pre-screen that expects raw source URLs in the issue body and flagged
    the template's internal source-note file references
    (`source-notes/blog-cognition-multi-agents-working.md`,
    `source-notes/blog-cursor-agent-swarm-model-economics.md`) with the note
    that the body "does not contain actual web URLs to the sources being
    compared." Despite that closure, an automated Assayer
    contradiction assessment was still posted on the issue: it verified
    both sides against the live sources and proposed verdict **`debated`**
    with a proposed **C-009** resolution entry, on the reasoning that the
    two claims answer different questions (Cognition's is about *breadth of
    market adoption* for parallel-writer swarms and explicitly carves out
    simple-verifiable-success-criterion demo tasks — exactly Cursor's
    SQLite-from-manual benchmark shape — as a known exception, while
    Cursor's is a single-experiment *technical existence proof* achieved
    after heavy bespoke coordination infrastructure). That proposed C-009
    entry has **not** yet been appended to CONTRADICTIONS.md (last committed
    entry is C-008) and is awaiting human finalization; the conditioning
    variables the assessment surfaces (task verifiability, unstructured
    peer-negotiation swarm vs. tree-shaped manager/children delegation, and
    willingness to build custom VCS / reconciler agents / a shared "Field
    Guide") are the axis a resolver should weigh.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` — that post
    provides the formal five-pattern taxonomy (generator-verifier,
    orchestrator-subagent, agent teams, message bus, shared state) with
    decision criteria for choosing between them; this source provides three
    concrete, production-deployed instances that map onto two of those
    patterns (generator-verifier → Claim 5's code review loop;
    orchestrator-subagent → Claim 12's manager-child delegation), plus a
    reactive escalation-based routing pattern (Smart Friend, Claims 8-11)
    that does not map cleanly onto any of the five named patterns there —
    Smart Friend is closer to a generator that can *consult* a verifier-like
    peer mid-task than to a strict generator-verifier post-hoc review loop,
    suggesting the five-pattern taxonomy may need a sixth "consult" pattern
    or a note that Smart Friend is a hybrid.
  - `discussion-hn-ttal-multiagent-factory.md` — TTal's two-plane
    architecture and P2P mesh topology were derived from building a
    software-factory CLI tool; this source arrives at the same two-plane
    shape (Claim 12) and the same cross-agent-communication gap (also
    Claim 12) independently, from a different starting point (a shipped
    commercial coding-agent product, not a practitioner's personal tool),
    strengthening the case that these are structural properties of
    manager-child delegation generally, not artifacts of one specific
    implementation.

- **Novel**:
  - **Clean-context (no shared context) generator-verifier pairing as a
    deliberate, counterintuitive design choice, with a quantified bug-catch
    rate**: No prior corpus source documents deliberately withholding
    shared context between a coding agent and its reviewer as the reason
    the reviewer performs *better*, nor gives a quantified rate (2 bugs/PR,
    58% severe) for this specific pairing.
  - **"Smart Friend" as a named architecture, including the specific
    failure mode that a consulted stronger model will "make up some
    theories" rather than push back when under-informed**: This corpus's
    other model-routing sources (Osmani's multi-model routing) describe
    routing by task type, not a reactive small-model-initiated escalation
    pattern with a named default-failure-mode warning.
  - **The escalation-routing vs. capability-routing distinction at the
    frontier tier**: The claim that cross-frontier model pairing changes
    the coordination problem from "does the weak model know its limits" to
    "which frontier model is best at this sub-task" is new framing not
    present elsewhere in this corpus.
  - **A named, public admission that a vendor's own smaller model (SWE-1.5)
    failed to make a specific multi-agent pattern work, with a stated
    diagnosis (a training problem, not a prompting problem)**: This is a
    rare disclosed negative result from a vendor about its own product line
    in this corpus's multi-agent coverage.
  - **The explicit dividing test for what counts as "working" multi-agent
    architecture — writes single-threaded vs. writes distributed across
    multiple agents — as the organizing axis of an entire post**: Prior
    corpus taxonomies (Anthropic's five patterns, TTal's seven patterns)
    organize by coordination topology or mechanism; this source organizes
    by a single binary property (who writes) and argues it is the
    determining factor for production viability today.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 03 (Patterns and
  anti-patterns)**: Add Claim 1's single-threaded-write framing as a
  proposed heuristic for evaluating any multi-agent design: "before adding
  a second or third agent, ask whether it will write to shared state/code,
  or only contribute intelligence (review, consultation, delegated
  research) to a single writer." Pair with the existing five-pattern
  taxonomy (`blog-anthropic-multi-agent-coordination-patterns.md`) as an
  orthogonal lens — this source's axis (single-writer vs. multi-writer)
  cuts across that taxonomy's five patterns rather than replacing it.
  Flag the direct tension with `blog-cursor-agent-swarm-model-economics.md`
  (contradiction issue #2149) explicitly rather than silently adopting
  Cognition's framing as settled guide advice.

- **Chapter 02 (Harness Engineering)**: Add Claim 6 (clean-context reviewer
  outperforms a context-sharing reviewer, attributed to context rot) as a
  named, actionable generator-verifier design rule, alongside the existing
  context-rot corroboration already cited from
  `blog-humanlayer-skill-issue-harness-engineering.md` and
  `blog-anthropic-session-management-1m-context.md`. This is now a
  three-source-corroborated recommendation: give a review/verification
  agent a fresh context window rather than forking the generator's context.

- **Chapter 04 (Context Engineering)**: Add Claim 9's named Smart Friend
  failure mode — an under-informed consulted model defaults to fabricating
  an answer rather than requesting more context — as a specific guardrail:
  when designing an escalation-consult pattern, explicitly instruct the
  consulted model to ask for more information (e.g., "investigate file X
  and ask again") rather than answer under uncertainty, and default to
  sharing a full context fork rather than a curated subset.

- **Chapter 02 (Harness Engineering)**: Add Claim 12's three named
  manager-child delegation failure modes (over-prescriptive managers,
  false shared-state assumptions, cross-agent communication not happening
  by default) as concrete anti-patterns to design against, cross-referenced
  with TTal's independently-derived two-plane architecture and P2P mesh
  mitigation for the same communication gap.

- **Chapter 01 (Daily Workflows) or Chapter 00 (Principles)**: Add Claim 4's
  distinction between demo tasks with simple, verifiable success criteria
  (browser/compiler/training-script-optimization demos) and "real software"
  requiring human taste and decision-making, as a caveat readers should
  apply whenever a large-agent-count demo result is cited as evidence for
  general engineering viability.

## Extraction Notes

- WebFetch's summarizing pass returned only a condensed, paraphrased
  ~250-word summary of this article on first fetch, consistent with the
  same difficulty already recorded in this corpus's other Cognition source
  notes (e.g. `blog-cognition-devin-desktop.md`, `blog-cognition-codemaps.md`
  Extraction Notes). The full article (~2,400 words across 6 named sections
  plus two footnotes) was instead fetched via `curl` with a browser
  user-agent, the `<article>` element isolated, and HTML tags stripped with
  the `html2text` tool. All quotes above were taken from that raw-text
  extraction and cross-checked against the WebFetch summary paragraph by
  paragraph for consistency — no discrepancy was found between the two
  beyond the expected loss of direct quotes in the summary.
- The article links to the author's own prior post ("Don't Build
  Multi-Agents," cognition.ai/blog/dont-build-multi-agents) as the premise
  this post revises. That prior post has no source note in this corpus at
  time of writing (not found via search of `source-notes/`) — a candidate
  for a future, separate source submission if a fuller before/after
  comparison of the author's position is wanted. It was not fetched
  separately for this extraction; this note relies on this source's own
  first-person summary of that prior post's argument.
- Two footnoted external links (Anthropic's multi-agent research system
  post, and Anthropic's "advisor strategy" beta post) were not fetched
  separately — both are used in this source only as brief, dated
  convergence references (Claim 14), not as sources of additional claims,
  consistent with MINER.md's guidance to follow substantive linked pages
  only when they would add new information beyond a footnote-level mention.
  A prior corpus source, `blog-simonwillison-code-w-claude-2026.md`,
  already documents Anthropic's "Mythos" model class by name, and
  references to a similar advisor/consult mechanism should be checked
  against that note if a future source mines the "advisor strategy" post
  directly.
- A contradiction was identified during cross-referencing (Claim 1 and
  Claim 13's rejection of "unstructured swarms" and endorsement of
  single-threaded writes, versus `blog-cursor-agent-swarm-model-economics.md`'s
  documentation of Cursor's actively-invested, concurrently-writing
  planner/worker swarm harness with a controlled experiment behind it).
  This meets the MINER.md §4a bar: both sources make general, same-topic
  claims about the production viability of parallel-writer multi-agent
  architectures that point in opposite directions and would lead to
  different guide advice. Filed as **contradiction issue #2149** before
  writing this note; no verdict is picked here — see Cross-References →
  Contradicts and the issue itself. Status as of extraction: the issue was
  closed and labeled `rejected` by an automated pre-screen bot that flagged
  the contradiction template's internal source-note file references as
  lacking raw web URLs in the issue body — a probable pre-screen
  miscalibration for contradiction issues, which correctly cite internal
  source notes that themselves carry `source_url` frontmatter for both
  sides (https://cognition.com/blog/multi-agents-working and the Cursor
  post's URL). Notwithstanding the closure, an automated Assayer
  contradiction assessment was still posted on the issue proposing verdict
  `debated` / a proposed C-009 entry; that entry has not yet been appended
  to CONTRADICTIONS.md (last committed entry is C-008) and is awaiting human
  finalization. The tension is therefore documented and assessed but not
  formally resolved; this note does not re-file a duplicate issue, since a
  completed assessment already exists on #2149.
- Cross-references verified before writing: re-read
  `blog-anthropic-multi-agent-coordination-patterns.md` in full and
  confirmed Claims 2, 3, and 7 by number and content;
  re-read `blog-humanlayer-skill-issue-harness-engineering.md` in full and
  confirmed Claims 6 and 13 by number and content; re-read
  `blog-anthropic-session-management-1m-context.md` and confirmed Claim 8
  by number and content; re-read `discussion-hn-ttal-multiagent-factory.md`
  in full and confirmed Claims 2 and 6 by number and content; re-read
  `blog-addyosmani-code-agent-orchestra.md` in full and confirmed Claim 9 by
  number and content; re-read `blog-cursor-multi-agent-kernels.md` in full
  and confirmed Claim 2 and Claim 10 by number and content; re-read
  `blog-cursor-agent-swarm-model-economics.md` in full and confirmed
  Claims 1, 2, 4, and 12 by number and content before citing them in the
  Contradicts section and the filed contradiction issue. No claim number
  was guessed or approximated.
- Confidence is rated `emerging` overall: this source combines a named,
  first-person practitioner author with several concrete, quantified
  metrics (bug-catch rate, usage growth, a disclosed negative result for
  SWE-1.5) that exceed pure marketing/philosophy framing, but no metric has
  a stated sample size or measurement methodology, no named customer is
  quoted, and the central organizing claim (single-threaded writes as the
  dividing line for viability) is contradicted by another vendor's
  documented production system — so it does not reach `settled`.
