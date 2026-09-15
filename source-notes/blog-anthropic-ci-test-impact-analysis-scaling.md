---
source_url: https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
source_type: blog-post
title: "Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic"
author: Sachin Malhotra (Anthropic Continuous Integration team)
date_published: 2026-09-14
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: anecdotal
issue: "#3448"
---

# Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic

> First-person account by the same Anthropic CI engineer behind
> `blog-anthropic-claude-oncall-cicd.md` describing how a single-writer,
> in-memory test-impact-analysis (test-selection) service withstood three
> successive capacity patches — each buying less runway than the last (70
> days, 29 days, <1 day) — before being redesigned into stateless listener
> workers writing to a database-backed journal, and the "always plan for the
> exponential" lesson the author draws from the experience.

## Source Context

- **Type**: blog-post (official claude.com/blog, "Claude Code / Enterprise
  AI" category, published September 14, 2026, ~5 minute read, bylined to a
  single named engineer)
- **Author credibility**: Sachin Malhotra is named in the byline as the sole
  author, identified elsewhere in the corpus (`blog-anthropic-claude-oncall-cicd.md`)
  as "an engineer on our Continuous Integration team." This is first-hand
  practitioner testimony about a system he personally operated through three
  incident cycles and then redesigned — comparable in evidentiary weight to
  his earlier on-call post. The architectural narrative (patch sequence,
  root causes, redesign shape) is credible first-hand reporting; the
  headline scaling figures (25x CI jobs, 8x code shipped, 80% Claude-authored,
  10x test growth, patch runway durations, "three weeks vs. a quarter" for
  the redesign) are self-reported internal metrics with no disclosed
  methodology, sample window, or measurement definition.
- **Scope**: Covers one specific service (Anthropic's internal test-impact-
  analysis / test-selection service) end to end: its original
  listener/selector architecture, three sequential capacity patches and why
  each was insufficient, the redesigned stateless-worker/journal
  architecture, and forward-looking advice for other teams. Does NOT cover:
  the selection algorithm itself (how "past performance and package
  relevance" map to a specific test subset), the database/store technology
  chosen, false-negative rates for skipped tests, cost of the new
  architecture in absolute terms (only "more expensive... but easier to
  scale" is stated), or the on-call/incident-response tooling covered in the
  author's companion post (linked at the end of this article and already in
  the corpus).

## Extracted Claims

### Claim 1: CI job volume at Anthropic grew 25x over six months, driven by 8x more code shipped per engineer per quarter, 80% of that code authored by Claude, 10x growth in the codebase's test count, and only a nominal increase in engineer headcount
- **Evidence**: Author's own summary framing, stated as the article's premise
  before any architectural detail follows.
- **Confidence**: anecdotal (specific, named figures, but self-reported with
  no disclosed methodology, baseline definition, or measurement window
  beyond "2021-2025" as the comparison period for the 8x figure)
- **Quote**: "Anthropic engineers on average ship 8x as much code per quarter
  as they did from 2021-2025. Claude authors 80% of that code and it also
  plays a large role in reviewing and approving PRs as well... On top of
  that, the amount of tests across our codebase grew 10x and we added a
  nominal amount of engineers. This all led to a 25x increase in CI jobs
  over a six month period."
- **Our assessment**: The 8x code-shipped figure and the "Claude authors most
  of it" framing match the same author's companion post almost exactly
  (`blog-anthropic-claude-oncall-cicd.md` Claim 16: "8x as much code per
  quarter as they did from 2021 to 2025"), which is internal-consistency
  corroboration from the same team rather than independent verification. The
  80%-Claude-authored and 10x-test-growth figures are new to this post. The
  25x CI-job figure is presented as a downstream multiplication of the other
  factors ("not every test runs on every PR," the author notes), not a
  directly measured single metric.

### Claim 2: Before the redesign, three sequential capacity patches were applied, each buying dramatically less runway than the last: a doubled-core machine bought ~70 days, package-level sharding bought 29 days, and daily restarts bought less than a day
- **Evidence**: Sequential incident narrative with the author naming the
  fix, the date it was applied, and how long it lasted before the next
  crisis.
- **Confidence**: settled (a specific, ordered, first-hand incident history
  with named durations — the kind of claim a team's own incident timeline
  could directly confirm or refute, even though it isn't independently
  audited here)
- **Quote**: "getting there was a bumpy path that started with three quick
  fixes, which lasted 70 days, then 29 days, and then less than a day
  respectively."
- **Our assessment**: The shrinking-runway pattern (70 → 29 → <1 days) is the
  article's strongest piece of evidence for its "always plan for the
  exponential" thesis: it's a concrete, monotonic demonstration that
  capacity patches degrade in effectiveness under compounding exponential
  load, not just an assertion that they eventually stop working.

### Claim 3: The original service's architecture required a single writer per test to keep an in-memory result history consistent, which structurally prevented horizontal sharding
- **Evidence**: Direct architectural root-cause description explaining why
  the "bigger machine" patch (Claim 2) was the only available first option.
- **Confidence**: settled (specific, first-hand description of the exact
  design constraint that caused the scaling failure)
- **Quote**: "All of this ran as a single process because keeping a running
  history per test meant a single writer needed to apply the results. This
  v0 design prevented us from being able to horizontally shard."
- **Our assessment**: This is the precise mechanism, not just the symptom —
  useful for practitioners diagnosing similar "why can't we just add more
  instances" scaling walls: the constraint was state-consistency ownership
  (one writer per mutable history), not raw compute.

### Claim 4: A 20-minute lag in the listener component could translate into tens of thousands of unapplied test-result updates, with three concrete downstream failure modes: undetected bad merges causing repeated investigations, flaky dependencies blocking merges, and newly fixed or added tests not running (risking regressions)
- **Evidence**: Direct enumeration of specific failure scenarios tied to a
  stated lag magnitude.
- **Confidence**: settled (specific, named failure taxonomy from the
  system's operator, describing mechanism rather than asserting an
  unqualified metric)
- **Quote**: "For an AI-native SDLC, a small lag can have a big impact. For
  example, 20 minutes of listener lag can translate into tens of thousands
  of test updates not being applied to the selector."
- **Quote** (failure modes): "If a bad change gets merged, then a test will
  start failing for everyone else causing multiple unnecessary
  investigations. If a dependency starts flaking, then flaky reds start
  blocking merges. If a test gets fixed or a new one gets added, it won't
  run until the listener catches up risking a regression."
- **Our assessment**: This quantifies why the listener's staleness is not a
  cosmetic problem — at agent-driven PR volume, a short absolute lag
  compounds into a large number of stale decisions, each with a distinct,
  named downstream cost. This is the clearest evidence in the post for why
  "eventually consistent, slightly stale" was not an acceptable tradeoff at
  this scale.

### Claim 5: The redesigned service replaced the singleton with stateless listener workers that append results to a database-backed journal, plus a separate consumer process that rolls the journal into per-test history every few seconds
- **Evidence**: Direct architectural description of the solution, framed
  explicitly as Claude's suggested fix that the team had previously
  deferred.
- **Confidence**: settled (specific, first-hand description of a shipped
  architecture, including the roll-up mechanism and its stated cadence)
- **Quote**: "we gave the test selection service a database, or an in-memory
  data store to be exact... Now, any listener worker can process any
  result, append it to a journal in the in-memory store, and move on
  without holding anything in memory - stateless and hence, horizontally
  scalable. A small separate consumer process rolls the journal up into
  per-test history every few seconds, and the selector can look up relevant
  result history quickly."
- **Our assessment**: This is a textbook single-writer-singleton →
  stateless-workers-plus-append-only-journal migration: state ownership
  moves from in-process memory to an external store, and horizontal scaling
  becomes possible because no worker needs to coordinate with any other to
  stay correct. This is the same underlying pattern documented at the
  protocol level in `blog-google-mcp-stateless-scaling.md` and at the agent-
  infrastructure level in `blog-anthropic-scaling-managed-agents.md` (see
  Cross-References) — this post is a third, independent instance of the
  pattern applied to CI tooling specifically.

### Claim 6: The redesign was more expensive to run than the singleton but far easier to scale and memory-profile, and it took three weeks for a single engineer with Claude's help versus an estimated quarter a year earlier
- **Evidence**: Direct cost/tradeoff statement plus a before/after time
  estimate for the same class of project.
- **Confidence**: anecdotal (the "a year ago it would have been closer to a
  quarter" figure is a retrospective estimate, not a measured prior project;
  no team size, engineer-hours, or infrastructure-cost breakdown is given)
- **Quote**: "This distributed architecture is more expensive to run, but it
  is much easier to scale and memory profile than a shaky singleton. This
  project took three weeks for a single engineer. A year ago it would have
  been closer to a quarter."
- **Our assessment**: This is the article's central economic argument for
  why "redesign now" beats "patch again": the claimed ~4x reduction in
  redesign time (quarter → three weeks) is what makes a full architectural
  overhaul competitive with — and ultimately cheaper than — another
  short-lived patch, reversing the traditional cost calculus where a full
  rewrite is the expensive, avoided option. The comparison baseline (a
  hypothetical "a year ago" project) is not a measured prior instance,
  so this should be read as the author's informed estimate rather than an
  A/B comparison.

### Claim 7: The author ran a long-lived, dedicated Claude Tag session monitoring the service for months, which paged him whenever listener lag exceeded 50,000 jobs and consistently argued for a full overhaul while the team kept choosing patches instead
- **Evidence**: First-hand description of an operational practice, with a
  concrete trigger threshold and an explicit statement of the human-vs-agent
  disagreement over strategy.
- **Confidence**: anecdotal (a single engineer's personal operational
  practice and characterization of "usually," not a documented decision log)
- **Quote**: "I started a long-running session in an internal version of
  Claude Tag dedicated to monitoring the service. Anytime the listener lag
  would get more than 50,000 jobs behind, Claude would ping me and resume
  our conversation on next steps. This would go on for months, and it was
  helpful not having to constantly remind it of past efforts or context.
  Claude often argued for an overhaul, but we usually settled on another
  patch."
- **Our assessment**: This is a concrete instance of a standing,
  threshold-triggered monitoring agent with persistent context across
  months — structurally similar to the on-call monitoring role described in
  the author's companion post (`blog-anthropic-claude-oncall-cicd.md`, Claim
  1), but notable here for a detail that post doesn't include: the agent's
  own architectural recommendation (overhaul) was repeatedly overruled by
  the humans in favor of a smaller patch, until the patches stopped working.
  This is a specific, self-critical data point about organizational
  inertia outlasting a correct agent recommendation — worth preserving
  distinctly from the more triumphant "Claude fixed it" framing elsewhere
  in the post.

### Claim 8: Three quick-fix attempts at the memory-limit crisis (Patch 3) — bug-hunting, swapping the memory allocator, and avoiding profiling the loaded singleton — all failed to solve the underlying problem, and restarting only bought less than a day and caused further data loss
- **Evidence**: Enumerated list of attempted fixes and their outcomes,
  followed by a description of the restart patch's own failure mode.
- **Confidence**: settled (specific, first-hand enumeration of attempted
  fixes and their concrete, stated results)
- **Quote**: "We only found four bugs. Swapping the memory allocator as a
  quick-hack did nothing. We were trying to optimize garbage collection but
  that wasn't really the solution. We didn't want to risk memory profiling
  a singleton already under a heavy load... Restarting bought us less than a
  day."
- **Quote** (restart's own failure mode): "We also discovered daily restarts
  were resulting in the service gradually falling further behind. When it
  fell behind for more than an hour, which happened several times, a ton of
  job results weren't recorded by the listener... this translated into us
  running tests that were already super flaky or widespread-failing across
  the board."
- **Our assessment**: This is a useful negative result: standard
  single-process performance-tuning moves (bug fixes, allocator swap, GC
  tuning) did not touch the actual bottleneck, because the bottleneck was
  architectural (single-writer state ownership, per Claim 3), not a code-
  level inefficiency. The restart patch's specific failure mode — falling
  behind after restart caused stale data that *increased* flaky-test noise
  rather than just delaying detection — is a concrete illustration that a
  workaround can quietly degrade the very signal (test selection accuracy)
  the service exists to produce.

### Claim 9: A test-selection service, rather than running every test on every change, is necessary specifically because agents (unlike humans) need a curated, valid set of tests to self-verify and iterate effectively, and running everything on every PR doesn't scale
- **Evidence**: Direct statement of the design rationale for the service's
  existence, made before any of the scaling-crisis narrative.
- **Confidence**: emerging (a stated design rationale from the system's
  builder; the human-vs-agent test-triage comparison is asserted, not
  measured with a false-positive/negative comparison)
- **Quote**: "Many of my peers work at organizations where every test is
  still run on every change. This works up to a point, but doesn't scale:
  CI gates get increasingly long, expensive, and untrustworthy. Additionally,
  humans are great at determining which test failures don't apply to them
  while agents will require more context and direction. When they get a
  specific set of valid tests, they can self-verify and iterate more
  effectively."
- **Our assessment**: This gives a specific, agent-shaped reason to prefer
  test *selection* over test *exhaustiveness* as agent-authored PR volume
  rises: the claim isn't just "running everything is slow," it's that a
  noisy, irrelevant-failure-laden test gate is harder for an agent to
  interpret and self-correct against than a curated one. This is a directly
  relevant data point against the "run more, slower tests" recommendation
  in `blog-pragmaticengineer-erez-cicd.md` Claim 10 — see Cross-References.

### Claim 10: Claude prefers authoring smaller, more granular PRs, which independently increases CI job count beyond what larger PRs would generate, and the agentic activity floor is raised (agents push overnight and on weekends) while remaining bursty because humans still drive and approve a significant share of PRs
- **Evidence**: Direct statement in the "what I would do differently"
  section, offered as part of the explanation for why CI load grew the way
  it did.
- **Confidence**: anecdotal (a stated observation with no PR-size
  distribution data, before/after counts, or weekend/weekday job-volume
  breakdown given)
- **Quote**: "This has changed the shape of PRs over time at Anthropic as
  Claude prefers smaller, more granular PRs (another good reason not to run
  every test against every PR). This has translated into more CI jobs in a
  given day. Also, the activity level floor is raised as agents push
  overnight and on weekends, but it remains bursty as human engineers still
  drive and approve a significant amount of PRs."
- **Our assessment**: This separates two distinct load-growth mechanisms
  that are easy to conflate: (1) more code volume, and (2) the same code
  volume split into more, smaller units, each of which triggers its own CI
  run — the second mechanism means CI load can outpace code-volume growth
  even proportionally. The "raised floor, still bursty" characterization of
  the daily traffic shape is a specific, transferable detail for anyone
  capacity-planning CI infrastructure for agent-authored work.

### Claim 11: The author's forward-looking advice for other teams is to plan for a 25x load increase within two quarters, treat over-engineering as less costly than before, instrument services so Claude can act as "eyes and ears" for incremental hill-climbing, keep state out of processes from the start, and avoid running any critical service as a single instance unless it can be measured with canaries
- **Evidence**: Explicit, itemized advice section closing the article,
  generalizing from the specific incident history just described.
- **Confidence**: emerging (specific, actionable advice, but framed as the
  author's own retrospective judgment ("what I would do differently") rather
  than a validated practice adopted elsewhere)
- **Quote**: "My advice to engineering teams is, whether you build or buy,
  assume your architecture will be at a 25x load within two quarters.
  Over-engineering as a concept is starting to slightly fade away, or at
  least the bar is moving much higher. You can now start to account for
  10-20x the perceived scale in your v0 designs as long your budget allows
  for it. Instrument your services to act as Claude's eyes and ears. It
  allows Claude to hill-climb and fix problems incrementally much better and
  faster than we could manually... Keep state out of the process from the
  start. I'd also avoid running any critical service as a single instance
  unless you can measure it and any canary changes."
- **Our assessment**: This is the article's most directly reusable
  prescriptive checklist, distinct from the specific incident narrative: a
  numeric planning target (10-20x v0 headroom, 25x within two quarters), an
  explicit reversal of the traditional anti-over-engineering norm, an
  instrumentation requirement framed around enabling Claude specifically
  (not just human observability), and a state-management default
  ("stateless unless measured"). Note this reframes "over-engineering" as
  conditional on budget, not unconditionally endorsed.

### Claim 12: This test-impact-analysis service is a distinct system from the on-call/incident-response Claude Tag deployment the same author previously documented, though both are part of the same team's broader CI/CD-scaling response to agentic code volume
- **Evidence**: The article's closing line links directly to the author's
  earlier post as a related but separate system.
- **Confidence**: settled (a direct, explicit link between two systems built
  by the same named author and team)
- **Quote**: "I've also written how we accelerated CI on call using Claude
  Tag (beta)."
- **Our assessment**: This confirms the two posts describe complementary,
  not overlapping, systems on the same team: the on-call post
  (`blog-anthropic-claude-oncall-cicd.md`) covers incident *detection and
  response* for CI/CD failures broadly, while this post covers the *test
  selection* pipeline specifically — one component among the several the
  on-call agent would investigate if it failed. Both cite the same "8x more
  code per quarter" framing independently, which is useful corroboration
  that the figure is a stable, team-level talking point rather than a
  one-off number invented for either post.

## Concrete Artifacts

### Patch sequence and runway (verbatim figures)
```
Source: claude.com/blog, "The bumpy road to redesign" section, Sep 14, 2026

Patch 1 (~October, prior year): doubled cores on the machine   -> ~70 days
Patch 2 (February): package-level sharding, one worker/package -> 29 days
Patch 3 (March): daily restarts                                 -> <1 day
Redesign (following): stateless workers + database journal      -> stable
  since cutover
```

### Listener/selector architecture (before and after)
```
Source: claude.com/blog, "The test impact analysis architecture" and
"The redesign" sections, Sep 14, 2026

BEFORE (v0, singleton):
  - "Listener": records test results from every CI run
  - "Selector": reads test result history, decides which tests run on
    which opened PRs
  - Constraint: single writer required per test to keep in-memory
    history consistent -> prevented horizontal sharding
  - Failure mode: 20 min of listener lag -> tens of thousands of
    unapplied test-result updates

AFTER (redesigned):
  - Any listener worker can process any result
  - Each worker appends the result to a journal in a database-backed
    (in-memory) data store -> stateless, holds nothing in memory
  - A separate consumer process rolls the journal into per-test
    history every few seconds
  - Selector looks up result history from the rolled-up store
  - Tradeoff stated: "more expensive to run, but much easier to scale
    and memory profile than a shaky singleton"
  - Build time: 3 weeks, single engineer (author's estimate: ~1
    quarter a year earlier for a comparable project)
```

### Scaling headline figures (verbatim)
```
Source: claude.com/blog, opening section, Sep 14, 2026

- CI job volume: 25x increase over 6 months
- Code shipped per engineer per quarter: 8x (current vs. 2021-2025 avg)
- Share of code authored by Claude: 80%
- Test count across codebase: 10x growth
- Engineer headcount: "nominal" increase
```

### "What I would do differently" checklist (verbatim, condensed)
```
Source: claude.com/blog, closing section, Sep 14, 2026

1. Account for the AI exponential: plan for 25x load within two
   quarters; v0 designs can budget for 10-20x perceived scale.
2. Instrument services to act as "Claude's eyes and ears" so it can
   hill-climb fixes incrementally; ensure job counts in equal job
   counts out.
3. Keep state out of the process from the start.
4. Avoid running any critical service as a single instance unless you
   can measure it and any canary changes.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-oncall-cicd.md` (same author, same team; Claim 16
    — "8x as much code per quarter as they did from 2021 to 2025"): this
    post's Claim 1 restates the identical 8x figure independently, which is
    internal-consistency corroboration (same team, two posts, consistent
    number) rather than third-party verification. Claim 12 above makes the
    relationship between the two posts explicit — complementary systems
    (incident response vs. test selection), not overlapping claims about
    the same system.
  - `blog-anthropic-scaling-managed-agents.md` (Claims 3-5 — the "pets vs.
    cattle" framing: a coupled, stateful design is a "pet" that fails hard
    and requires manual recovery, while a decoupled, stateless harness is
    "cattle," recoverable via `wake(sessionId)` re-reading an event log, and
    measured a 60%/90% p50/p95 TTFT improvement from the stateless
    redesign): this post's Claim 5 (the singleton → stateless-workers-plus-
    journal redesign) is a second, independent Anthropic engineering team
    arriving at the identical architectural pattern — replace an in-process
    stateful singleton with stateless workers that recover state from a
    durable, append-only log — for a completely different subsystem (CI
    test selection vs. agent session/harness infrastructure). Two
    independent teams converging on the same pattern for different problems
    is stronger evidence that "stateless workers + durable log" is a general
    scaling response to agent-driven load, not a one-off fix.
  - `blog-google-mcp-stateless-scaling.md` (Claim 1 — a stateful
    session-handshake model pins clients to specific server instances and
    breaks horizontal scaling; Claim 3 — statelessness enables plain
    round-robin load balancing and transparent failover): this post's Claim
    3 (single-writer-per-test-history singleton preventing horizontal
    sharding) is a third, industry-independent instance of the same root
    cause (state pinned to one process/instance blocks horizontal scaling)
    and the same fix (remove the state dependency, make workers
    interchangeable) — this time for CI infrastructure rather than an
    agent-tooling protocol, corroborating that this is a general
    distributed-systems pattern being rediscovered across agent-adjacent
    infrastructure, not specific to any one domain.

- **Contradicts**: Not filed as a new contradiction. Claim 9 here (test
  *selection* — running a curated, minimal set of valid tests per PR — is
  necessary because exhaustive per-PR test runs "don't scale" and are
  harder for agents to self-verify against) sits in real tension with
  `blog-pragmaticengineer-erez-cicd.md` Claim 10 (as agents write most code,
  CI's optimization target will shift toward running "extra, more thorough
  tests – and also even slower ones," because agents don't suffer the
  human context-switch cost of a slow pipeline). This exact tension —
  Erez's "more and slower tests" prediction versus evidence pointing the
  other direction — is already tracked under closed issue **#1510**
  ("CI/CD rigor under AI-generated code: rising verification investment
  (predicted) vs. falling human review (observed)"), whose Side A is this
  same Erez claim. Per MINER.md §4a, a contradiction already filed on the
  same topic should not be re-filed; this note instead adds a third data
  point to that existing thread: Anthropic's own CI-scaling response was to
  invest in smarter test *selection* (fewer, targeted tests per PR) rather
  than to run more or slower tests uniformly, which reads as independent
  evidence against Erez's specific "more and slower" prediction, though
  Erez's proposed mechanism (agents don't context-switch on a slow pipeline)
  and this post's mechanism (agents need curated, low-noise test signal)
  are not strictly incompatible — a future resolution of #1510 should weigh
  this post's evidence alongside the existing two sides.

- **Extends**:
  - `blog-anthropic-claude-oncall-cicd.md` (Claim 2 — the four-part on-call
    agent requirements taxonomy: memory, connections/access, schedules,
    instructions): this post's Claim 7 (a long-running Claude Tag session
    dedicated to monitoring a single service, paging the author at a
    50,000-job lag threshold) is a second, narrower instance of a
    standing, memory-and-schedule-driven monitoring agent — but unlike the
    on-call post, this one includes a specific, self-critical detail that
    post omits: the agent's own recommendation (overhaul) was repeatedly
    overruled by humans in favor of patches, for months, until the patches
    stopped working. This is a concrete illustration of organizational
    inertia outlasting a correct agent recommendation, worth adding to any
    guide discussion of trust/autonomy that currently only shows agents
    being followed.
  - `blog-pragmaticengineer-erez-cicd.md` (Claim 10, discussed above under
    Contradicts): extends the CI/CD-under-agentic-load discussion with a
    concrete, named counter-example to weigh against Erez's prediction.

- **Novel**:
  - **A monotonically shrinking patch-runway sequence (70 → 29 → <1 days)**
    (Claim 2) as concrete evidence that repeated capacity patches degrade
    in effectiveness under compounding exponential load — a specific,
    numbers-attached illustration of "patches buy less time each round,"
    not previously documented this concretely in the corpus.
  - **A named economic reversal**: a full architectural redesign (3 weeks)
    now costing less engineering time than a previous-generation estimate
    for the same class of project (~1 quarter), which the author uses to
    argue for redesigning early rather than patching (Claim 6) — new to the
    corpus as a specific "the math on rewrite-vs-patch has flipped" data
    point, distinct from the general "Claude accelerates migrations" claims
    already documented elsewhere (e.g., the Bun Zig→Rust rewrite in
    `blog-anthropic-dynamic-workflows-claude-code.md`).
  - **A specific state-ownership root-cause diagnosis** (Claim 3:
    single-writer-per-test-history as the structural blocker to horizontal
    sharding) as a transferable diagnostic pattern for "why can't we just
    add more instances" scaling failures.
  - **A quantified example of stale-data harm from a workaround itself**
    (Claim 8: daily restarts causing lag that increased flaky-test noise
    rather than merely delaying detection) — a concrete illustration that a
    patch can quietly worsen the exact signal quality a service exists to
    protect.

## Guide Impact

- **Chapter 03 (System Design / Orchestration at Scale)**: Add the
  singleton-to-stateless-workers-plus-journal redesign (Claim 5) as a named,
  concrete case study of the general "stateless workers + durable
  append-only log" scaling pattern already documented from two other angles
  in `blog-anthropic-scaling-managed-agents.md` and
  `blog-google-mcp-stateless-scaling.md` — this is now a three-source
  corroborated pattern specific enough to state as a default recommendation
  for any service that needs to scale under agent-driven load: identify the
  single-writer state dependency first (Claim 3), then externalize it to a
  store workers can share.

- **Chapter 05 (Testing and CI/CD at Scale)**: Add this as the guide's first
  detailed, numbers-attached case study of CI infrastructure strain from
  agentic coding specifically: the 25x/8x/80%/10x scaling figures (Claim 1),
  the shrinking patch-runway sequence (Claim 2), the 20-minute-lag failure
  taxonomy (Claim 4), and the "curated test selection over run-everything"
  rationale (Claim 9) as a directly relevant counter-data-point to weigh
  against the "more, slower tests" prediction already in the corpus via
  `blog-pragmaticengineer-erez-cicd.md` (tracked under contradiction #1510
  — do not present either position as settled).

- **Chapter 03 or 06 (Capacity Planning / Org Practices)**: Add the closing
  advice checklist (Claim 11) as a specific, numeric planning heuristic —
  budget v0 designs for 10-20x perceived scale, plan for 25x within two
  quarters, instrument for Claude-driven incremental hill-climbing, default
  to stateless unless measured — distinct from generic "build for scale"
  advice because it names concrete multipliers and ties them explicitly to
  agent-driven (not just user-driven) load growth.

- **Chapter 02 or 06 (Trust and Autonomy)**: Add Claim 7 (Claude's standing
  monitoring session repeatedly recommended the overhaul the team eventually
  needed, but was overruled for months in favor of patches) as a concrete,
  self-critical counter-example to any guide narrative that assumes teams
  promptly act on correct agent recommendations — useful alongside
  `blog-anthropic-claude-oncall-cicd.md`'s more successful on-call framing
  to show the same author-team relationship producing both outcomes.

## Extraction Notes

- **Fetch method**: The page is a JS-rendered Webflow site; WebFetch's
  AI-summarized rendering was not used as the source of truth. Instead the
  raw HTML was fetched via `curl` with a browser user agent, script/style
  blocks stripped, then all remaining HTML tags stripped to flat text. The
  full article body (byline through the closing "Additional CI resources"
  link) was present in that flat-text extraction and was read in full. Every
  `Quote` field above was verified character-for-character against that
  flat-text extraction (including matching literal `&#x27;` HTML entities
  back to apostrophes where the source markup used them).
- **Images/captions not extracted as data**: The post includes three inline
  images with captions ("Conversation recreated. Based on real events.";
  "Verbatim conversation on an internal version of Claude Tag with some
  redactions."; a chart captioned "Queued, unprocessed job-result events,
  hourly max. Before: a backlog built up most days and grew week over week.
  After cutover and tuning: flat."). The captions are quoted verbatim in
  Concrete Artifacts context where relevant, but the images themselves
  (a recreated Claude Tag conversation screenshot, a real redacted Claude
  Tag conversation screenshot, and a line chart) were not fetched or
  transcribed — no claim above depends on image content beyond what the
  surrounding prose and captions state in text.
- **One external link followed**: The post's closing line links to the
  author's earlier post, already in the corpus as
  `blog-anthropic-claude-oncall-cicd.md`; that note was re-read in full (not
  just its frontmatter) before writing Claim 12 and the Corroborates/Extends
  entries above, and every `Claim N` reference to it was confirmed against
  its actual numbered claims.
- **Cross-references verified**: `blog-anthropic-claude-oncall-cicd.md`,
  `blog-anthropic-scaling-managed-agents.md`,
  `blog-google-mcp-stateless-scaling.md`, and
  `blog-pragmaticengineer-erez-cicd.md` were each read in full (or, for the
  longest note, checked claim-by-claim via heading search) before citing;
  every `Claim N` reference above was located and confirmed against that
  note's actual numbered claims, not guessed.
- **Contradiction check performed, not filed**: Before writing the
  Contradicts section, `CONTRADICTIONS.md` and the repository's open and
  closed `contradiction`-labeled issues were both searched. Issue #1510
  already covers the exact Erez "more and slower tests" claim this source's
  Claim 9 bears on; per MINER.md §4a that existing thread was cited instead
  of filing a duplicate contradiction issue. No CONTRADICTIONS.md entry
  currently exists for #1510 despite the issue being closed — that is a
  pre-existing gap in the ledger, not something introduced by this
  extraction, and is noted here only so the Assayer/Smith are aware the
  referenced issue's resolution is not yet recorded in the ledger.
- **Confidence rationale**: Overall confidence is set to `anecdotal` because
  every claim rests on one named engineer's first-person account of a
  system he personally operated and redesigned, with no independent audit,
  third-party validation, or disclosed measurement methodology for any of
  the quantitative figures (25x/8x/80%/10x, the 70/29/<1-day patch
  runways, or the "three weeks vs. a quarter" redesign-time comparison).
  Individual claims are marked `settled` where the underlying mechanism or
  sequence of events is a specific, internally consistent first-hand
  description (e.g., the architectural root cause in Claim 3, the patch
  sequence in Claim 2) and `anecdotal` or `emerging` where the claim is a
  self-reported metric, a retrospective estimate, or a single illustrative
  characterization without a stated sample or baseline.
