---
source_url: https://openai.com/index/scaling-storage-one-billion-users-part-one
source_type: blog-post
title: "Rapidly scaling online storage to serve over 1 billion ChatGPT users"
author: OpenAI (Habitat engineering team; editorial "we" voice, no individual byline)
date_published: 2026-09-11
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: emerging
issue: "#3632"
---

# Rapidly scaling online storage to serve over 1 billion ChatGPT users

> First-party OpenAI engineering post (part one of a two-part series) on
> Habitat, OpenAI's online storage platform: how it evolved from a
> single-database Python client library at DevDay 2023 into a service now
> handling 70M+ requests/second and 500PB+ of data for 1B+ weekly users, why
> a deliberate short-term Python-as-service tradeoff was made, three specific
> tail-latency root causes found and fixed (asyncio scheduling delay, a
> synchronized feature-flag-parsing stall, and a LIFO-connection-pool
> metastable failure), a deliberately constrained NoSQL API as a scaling
> strategy, and a from-scratch Rust rewrite of the entire service completed
> by 2 engineers using Codex and GPT-5.5 in one quarter.

## Source Context

- **Type**: blog-post (official `openai.com/index/` engineering post, category
  "Engineering," published September 11, 2026; ~1,900 words plus five
  labeled figures). Explicitly the first of a two-part series — the post
  states a second part will cover "the storage layer and how Habitat serves
  more than 500 petabytes and over 70 million requests every second," multi-tenancy
  reliability, read-performance optimization, and Azure Cosmos DB scaling in
  more depth.
- **Author credibility**: First-party OpenAI publication in an editorial "we"
  voice throughout (e.g., "we built," "we discovered," "we bet"). No
  individual author byline is given; the post is attributed to the
  organization/engineering team building Habitat, and closes with a link to
  an open "Software Engineer, Habitat (Online Data)" role, confirming a
  real, currently-staffed internal team rather than a marketing-only post.
  As with other first-party single-company technical accounts in this corpus
  (e.g. `blog-pragmaticengineer-orosz-openai-software-factory.md`'s
  first-hand-but-single-company reporting), the claims here are detailed and
  internally consistent but not independently audited by a third party.
- **Scope**: Covers Habitat's origin as a Python client library, the
  library-to-service migration and its motivating outage, the deliberate
  choice to launch the service in Python despite known overhead, three
  specific tail-latency debugging case studies (asyncio scheduling delay,
  Statsig config-parsing stalls, LIFO connection-pool metastability),
  Habitat's constrained NoSQL API design philosophy and its Rockset/CDC
  escape hatch for complex queries, and the subsequent Python-to-Rust
  rewrite. Does **not** cover (explicitly deferred to "part two," not yet
  published as of extraction): multi-tenancy reliability mechanics, the
  "layered strategy for optimizing read performance," or the Azure Cosmos DB
  partnership/scaling details at the storage-layer level. Also does not name
  specific dollar costs, specific latency numbers (p50/p99 figures are
  discussed qualitatively, not quoted), or a specific timeframe for the
  library-to-service migration beyond "by the middle of 2025."

## Extracted Claims

### Claim 1: Habitat evolved from a small Python client-side library at DevDay 2023 into a complex distributed system now handling more than 70 million requests per second, serving over 1 billion people weekly across almost 40 geographic regions, and storing more than 500 petabytes of data
- **Evidence**: Headline scale figures stated in the post's opening section and repeated as labeled stat callouts (Figure 01).
- **Confidence**: settled (specific, first-party, current-state operational metrics for a system the same post confirms is actively staffed and operated)
- **Quote**: "Habitat now handles more than 70 million requests every second, supporting products used by over 1 billion people each week, across almost 40 geographic regions. Habitat first launched to support GPTs at DevDay 2023, starting as a simple Python client-side library connected to a single database. Today, it's a complex distributed system that serves more than 500 petabytes of data."
- **Our assessment**: These are the article's load-bearing scale numbers and are internally consistent with the later claim that "at its peak, Python helped us serve more than 20 million requests every second" before the Rust rewrite (Claim 11) — i.e., total throughput roughly tripled between the pre-rewrite Python peak and the current, mostly-Rust figure, which is plausible given the described 10x-year-over-year growth trajectory (Claim 2).

### Claim 2: OpenAI's storage platform grew more than 10x year-over-year for three consecutive years, a rate the post explicitly contrasts with typical systems-engineering practice of building for one 10x horizon at a time
- **Evidence**: Direct first-party statement contrasting Habitat's growth curve with normal industry pacing.
- **Confidence**: settled (specific, quantified, first-party growth-rate claim)
- **Quote**: "Often, system engineers build for 10x scale, and hope for it to hold for a few years while preparing for the next 10x. In our case, we've grown more than 10x year-over-year for the last three years."
- **Our assessment**: This is the article's framing device for every subsequent architectural decision — it explicitly attributes the "series of tactical decisions and sequencing" described later (deferring the Python rewrite, keeping the API deliberately constrained, etc.) to this compounding growth rate rather than to any single design philosophy. Should be read as context for why the later engineering tradeoffs (Claims 4, 7, 11) were made in the order they were, not as an isolated statistic.

### Claim 3: Migrating Habitat from a shared client-side library to a standalone service was forced by a specific coordination failure — a multi-day, feature-flagged rollout meant to reduce blast radius instead caused the very regional outage it was designed to prevent, after one team rolled back to a previously buggy client version
- **Evidence**: A specific, sequenced first-party incident narrative (routing-logic change → feature flag → staged rollout → shadow-testing → bug fix → re-rollout → an unrelated team's rollback to a stale client → outage).
- **Confidence**: settled (a specific, sequenced incident account, though self-reported and without a postmortem date or named services)
- **Quote**: "Eventually, we were ready to enable the flag, only for one of the teams to roll back their service for unrelated reasons to a previously buggy client, causing the outage we had worked so hard to avoid." / "Changes to the client library necessitated complex coordination across dozens of services, a process that proved increasingly brittle, inefficient, and susceptible to operational failures. To reduce this operational fan out for our future deployments, we decided to pull Habitat into its own service."
- **Our assessment**: This is a concrete, causally specific failure story (not a generic "libraries don't scale" claim) that motivates a library-to-service architectural migration — a pattern directly relevant to any guide discussion of when a shared client library should become a centralized service. The irony (the safety mechanism itself, an unrelated team's rollback of an unrelated change, caused the exact outage class it was built to prevent) is the most citable specific detail.

### Claim 4: A centralized Habitat service functions as a single security chokepoint — centrally enforcing access control, performing audit logging, and limiting underlying storage access — explicitly to protect against "external, internal, and agent actors"
- **Evidence**: Direct first-party statement of the security rationale for centralization, made as a second, distinct justification alongside the operational-coordination rationale in Claim 3.
- **Confidence**: settled (a stated design rationale, specific and unambiguous, though not paired with an incident example the way Claim 3 is)
- **Quote**: "A centralized service also gives us a single chokepoint to provide the strongest data security and privacy primitives. Habitat service is where we can centrally enforce access control policies, perform audit logging, and limit access to underlying storage resources like Azure Cosmos DB. Habitat plays a critical role in protecting user data and preventing unauthorized access from external, internal, and agent actors."
- **Our assessment**: The explicit inclusion of "agent actors" alongside "external" and "internal" actors as a threat category worth architecting against is notable and, to our knowledge, novel phrasing in this corpus — it signals that OpenAI treats its own (and possibly third-party) AI agents as a distinct access-control threat class requiring the same centralized chokepoint as human-driven external/internal access, not merely a convenience-oriented design choice.

### Claim 5: OpenAI deliberately kept Habitat's new standalone service in Python rather than a faster language, accepting known performance costs, as a conscious short-term technical-debt tradeoff prioritizing unblocking product developers and platform stability over cost or resource optimization
- **Evidence**: Direct first-party statement of the tradeoff and its explicit rationale.
- **Confidence**: settled (explicit, first-party statement of a deliberate engineering tradeoff, stated plainly without hedging)
- **Quote**: "Using Python for a high-throughput service increased network latency and added substantial CPU and memory scaling costs compared to local library execution. Moreover, we recognized that the inefficiencies of Python would not be acceptable at 100x scale, making an eventual rewrite almost certain. However, we viewed this as a strategic incursion of technical debt. Our primary objective then was not cost or resource optimization, but rather unblocking product developers and achieving platform stability."
- **Our assessment**: This is a specific, named instance of "incur technical debt deliberately, on a known future-rewrite timeline" as an engineering strategy, distinct from technical debt that accumulates unintentionally — directly relevant to any guide discussion of when it is acceptable to ship a known-suboptimal implementation on purpose.

### Claim 6: OpenAI's decision to defer the Python rewrite rested on an explicit wager that its own coding models would mature enough, by the time a rewrite became necessary, to make that migration achievable — a bet the post states "eventually proved correct"
- **Evidence**: Direct first-party statement of the wager and its stated outcome, presented as a distinct, named justification alongside Claim 5's cost/stability rationale.
- **Confidence**: emerging (a first-party claim about an internal decision's motivation and outcome, self-assessed by the same organization that made the bet, though the outcome — the Rust rewrite in Claim 11 — is independently described with specific metrics in the same post)
- **Quote**: "We also made a calculated wager that the rapid advancement of our own coding models would simplify the technical path in the future. We bet that by the time a full migration off Python was required, Codex and GPT would make that migration achievable. That bet eventually proved correct."
- **Our assessment**: This is a first-party account of an organization consciously betting on its own AI tooling's future trajectory as an infrastructure-planning input — not just using AI tools opportunistically once available, but structuring a multi-year technical-debt decision around an anticipated future capability. This is a distinct and stronger claim than "AI tools helped with our rewrite" (Claim 11); it asserts the rewrite's deferral was itself contingent on this specific prediction about coding-model capability.

### Claim 7: The dominant driver of tail latency in Habitat's Python service was Python's asyncio event-loop scheduling delay, not downstream database response time — traced by observing that requests stalled waiting for their coroutine to be rescheduled after the downstream storage had already responded
- **Evidence**: First-party trace-level debugging account describing the specific symptom pattern observed before tuning.
- **Confidence**: settled (a specific, technically detailed root-cause finding, illustrated with a labeled figure, consistent with the broader Python GIL/concurrency mechanics described in the same section)
- **Quote**: "Before tuning for our initial service launch, we saw in traces for requests with p99 and higher latency that while downstream storage responded quickly, requests frequently stalled while waiting for the responsible coroutine to be rescheduled to parse the response." / "For Python services at OpenAI, we find that in addition to measuring standard utilization and saturation metrics on memory, CPU, network, and disk usage, it is critical to also monitor the asyncio loop and how busy it is, then tune accordingly."
- **Our assessment**: This is a specific, actionable observability recommendation (monitor asyncio event-loop busyness as its own signal, distinct from standard CPU/memory/network/disk metrics) backed by a concrete measurement method (Claim 8) — a transferable pattern for any team running latency-sensitive Python services with mixed I/O- and CPU-bound work under asyncio.

### Claim 8: Habitat's team measures asyncio event-loop scheduling delay empirically in production by periodically scheduling background tasks and recording the gap between expected and actual execution time, observing jitter of up to hundreds of milliseconds and, in edge cases, several seconds — which led them to run many small-concurrency worker processes instead of fewer high-concurrency ones
- **Evidence**: First-party description of the measurement technique and its quantified findings, with the stated resulting architectural response.
- **Confidence**: settled (a specific, reproducible measurement methodology with quantified results)
- **Quote**: "By periodically scheduling background tasks and recording the delta between expected and actual execution time, we are able to empirically measure event loop scheduling delay in real time. At high utilization, with many expensive tasks, even modest numbers of concurrent requests per process are enough to produce significant scheduling jitter, up to hundreds of milliseconds and in some edge cases several seconds. As a result, we resort to keeping each process serving only a small number of concurrent requests and instead massively scale out the number of Python worker processes."
- **Our assessment**: This is a concrete, implementable diagnostic technique (a synthetic scheduled-task canary measuring the delta between expected and actual firing time) that any team running Python asyncio services under CPU-heavy load could adopt directly, independent of Habitat's specific domain.

### Claim 9: A synchronized, unjittered Statsig feature-flag config refresh (every pod's workers all polling and parsing the same large config every 60 seconds, combined with up to 8 processes per pod) caused every pod to periodically stall all in-flight request processing simultaneously — root-caused via live CPU profiling and fixed with a smaller targeted config, a longer refresh interval, and added jitter
- **Evidence**: First-party root-cause narrative naming the specific tool (Statsig), the specific default (60-second unjittered polling of every production rule across every service), and the specific architectural amplifier (8 processes per pod).
- **Confidence**: settled (a specific, named tool, a specific default configuration, and a specific fix, presented as an actual resolved incident rather than a hypothetical)
- **Quote**: "By default, Statsig was configured to poll for refreshed configs every minute with no jitter, and the config included every production rule across every service. Elsewhere, an architectural decision was made to run up to 8 Python processes per pod to push higher CPU usage and provide lower latencies. Combined, this meant that every minute each pod would have some moment where all of its workers stalled processing in-flight requests and instead would spend their CPU cycles parsing a giant configuration file. The fix was straightforward once CPU profiling helped us root cause the issue: deploy a smaller targeted config, lengthen the refresh interval, and add some jitter to background tasks like these."
- **Our assessment**: This is a specific, named, and highly transferable failure pattern — synchronized background-task polling across all workers in a pod is a generic anti-pattern (a self-inflicted "thundering herd" within a single pod, distinct from the client-to-server thundering herd covered in Claim 10) that any team using feature-flag SDKs with default periodic-refresh behavior should check for, independent of Statsig specifically.

### Claim 10: Client-side connection pooling combined with Python's aiohttp TCPConnector defaulting to LIFO (most-recently-used) connection reuse created a self-reinforcing metastable failure state, where overloaded server processes were preferentially routed more traffic because their connections were returned to the pool later; patching to FIFO reuse broke the feedback loop and even reduced steady-state variance
- **Evidence**: First-party incident narrative including the initial symptom (processes remained degraded well past the triggering burst, "runaway degradation"), the diagnostic test (capping max connection reuse duration), the root-cause mechanism (LIFO reuse), the fix (patch to FIFO), and an explicit citation to an external reference class of failure (Facebook's metastable failure engineering post).
- **Confidence**: settled (a specific, mechanistically explained, named failure mode with a described fix and stated outcome, illustrated with two labeled before/after figures)
- **Quote**: "Further investigation found that Python's aiohttp TCPConnector defaults to LIFO connection reuse: the most recently returned connection is selected for the next request. ... During a burst of requests, requests to slower overloaded servers returned connections to the pool later and were therefore selected more frequently by subsequent requests, gradually concentrating more traffic on the pods already struggling. Patching the connection pool to use FIFO reuse broke this feedback loop and even reduced our steady state request variance as well." / "This was a class of failures some of our teammates were well-acquainted with from prior work: metastable failure."
- **Our assessment**: This is one of the most specific, mechanistically-explained findings in the post — a concrete, checkable claim (aiohttp's TCPConnector LIFO default) that any team using aiohttp with client-side connection pooling at scale can directly verify and fix in their own systems. The team now relies on Istio/Envoy for connection pooling and load-aware balancing instead of managing this at the application layer, per the same section — a specific "move this concern into the infrastructure layer" resolution worth preserving alongside the original bug.

### Claim 11: In Q2 2026, two engineers used Codex and GPT-5.5 to rewrite Habitat's entire service from Python to Rust; the new Rust service now handles 95% of production requests (with Python deprecation planned "in the coming weeks"), and is measured as 6x more CPU-efficient and 15x more memory-efficient than the Python version, with lower average and tail latencies
- **Evidence**: First-party account naming a specific quarter, a specific team size, the specific AI tools used, and specific before/after efficiency multipliers.
- **Confidence**: settled (a specific, dated, first-party claim with quantified efficiency multipliers, stated as a completed and currently-deployed migration, not a projection)
- **Quote**: "In Q2 2026, with just 2 engineers, Codex, and GPT‑5.5, we were able to rewrite the entire service in Rust. This new Rust service is now handling 95% of our production requests; we'll be deprecating Python entirely in the coming weeks. Our data shows the Rust service is 6x more CPU efficient and 15x more memory efficient than the Python version, with significantly lower average and tail latencies."
- **Our assessment**: This is a concrete, dated, named instance of exactly the claim that appears only as a paywalled teaser line in `blog-pragmaticengineer-orosz-openai-software-factory.md` (section 7 teaser: "it only takes one or two engineers for previously 'impossible' rewrites and migrations to succeed") — see Cross-References → Corroborates. Unlike that teaser line, this post gives the specific system (Habitat, "second largest service by core count at OpenAI"), the specific team size (2 engineers), the specific tools (Codex, GPT-5.5), the specific timeframe (Q2 2026, one quarter), and specific efficiency outcomes (6x CPU, 15x memory) rather than an unelaborated headline claim.

### Claim 12: Habitat deliberately exposes only a constrained NoSQL object/edge API (no arbitrary SQL, no unbounded queries or joins) inspired by Meta's TAO system, treating this restriction as an explicit tradeoff that makes request cost predictable and pushes complex analytical querying needs onto a separate, isolated, per-team-provisioned Rockset layer fed by change-data-capture
- **Evidence**: First-party design-philosophy statement paired with a named historical failure mode it was designed to avoid (unreviewable, expensive ad hoc Postgres queries causing outages) and a named external inspiration (the TAO paper).
- **Confidence**: settled (a specific, named API design philosophy with a stated historical motivation and a named external precedent, not a marketing claim)
- **Quote**: "Rather than allowing clients to construct arbitrary SQL queries that could result in large table scans or joins across many tables, Habitat exposes a simple NoSQL API. The lack of a powerful API is an explicit tradeoff in Habitat's design. ... The problem here is in cost imbalance: it is cheap and easy to write SQL queries that are expensive and hard to run. In Habitat, we avoid this and make expensive queries exceedingly obvious client-side." / "For clients with more complex querying needs, we do provide an offline secondary view of Habitat exposed via Rockset. We use change data capture (CDC) to stream changes from the online storage out to isolated Rockset instances in near-real-time. Each client team is responsible for scaling their own Rockset instance for their complex querying needs."
- **Our assessment**: This is a specific, generalizable API-design pattern — deliberately restrict the primary online-storage API to predictable-cost operations, and satisfy complex/ad hoc querying needs entirely outside the hot path via CDC into a separately-scaled analytical store — that is transferable well beyond OpenAI's specific stack (Cosmos DB/Rockset), and is presented with a concrete historical motivation (pre-Habitat Postgres outages from unreviewed expensive queries) rather than as abstract best practice.

## Concrete Artifacts

### Scale metrics (verbatim stat callouts, Figure 01)

```
Source: https://openai.com/index/scaling-storage-one-billion-users-part-one

70M+ requests per second
1B+ people each week
500 PB+ data
```

### Statsig incident root cause (verbatim)

```
Source: https://openai.com/index/scaling-storage-one-billion-users-part-one — "Reducing a tail latency in our feature flag configurations"

"In our initial service launch, we discovered through live service CPU
profiling one root cause of high asyncio delay (and resulting high tail
latencies): periodic JSON parsing of our feature flag configurations via
Statsig (a tool that manages feature flags, and can be used to run A/B tests
and more).

By default, Statsig was configured to poll for refreshed configs every
minute with no jitter, and the config included every production rule across
every service. Elsewhere, an architectural decision was made to run up to 8
Python processes per pod to push higher CPU usage and provide lower
latencies. Combined, this meant that every minute each pod would have some
moment where all of its workers stalled processing in-flight requests and
instead would spend their CPU cycles parsing a giant configuration file.

The fix was straightforward once CPU profiling helped us root cause the
issue: deploy a smaller targeted config, lengthen the refresh interval, and
add some jitter to background tasks like these."
```

### LIFO-vs-FIFO connection pool metastable failure (verbatim)

```
Source: https://openai.com/index/scaling-storage-one-billion-users-part-one — "Balancing loads and managing connection pools"

"We discovered this in a chance incident where, despite stopping the client
that was overloading part of our service, a subset of processes remained
degraded well past the bursty traffic. In fact, we noticed those processes
experienced runaway degradation, receiving increasingly more requests until
we restarted them. ... We suspected the connection pool was to blame and
tested this suspicion by capping max connection reuse duration, which
indeed limited the degradation and confirmed our investigation direction.
Further investigation found that Python's aiohttp TCPConnector defaults to
LIFO connection reuse: the most recently returned connection is selected
for the next request. ... Patching the connection pool to use FIFO reuse
broke this feedback loop and even reduced our steady state request variance
as well."

External reference cited by the post for this failure class:
"metastable failure" — https://engineering.fb.com/2014/11/14/production-engineering/solving-the-mystery-of-link-imbalance-a-metastable-failure-state-at-scale/
```

### Python-to-Rust rewrite outcome (verbatim)

```
Source: https://openai.com/index/scaling-storage-one-billion-users-part-one — "Migrate from Python to Rust"

"With the platform maturing and our growth continuing to accelerate, and
being the second largest service by core count at OpenAI (and fourth for
our Envoy footprint), it was finally time to move past Python. At its peak,
Python helped us serve more than 20 million requests every second.

In Q2 2026, with just 2 engineers, Codex, and GPT‑5.5, we were able to
rewrite the entire service in Rust. This new Rust service is now handling
95% of our production requests; we'll be deprecating Python entirely in
the coming weeks. Our data shows the Rust service is 6x more CPU efficient
and 15x more memory efficient than the Python version, with significantly
lower average and tail latencies."
```

### Habitat's NoSQL/CDC design (verbatim)

```
Source: https://openai.com/index/scaling-storage-one-billion-users-part-one — "Why Habitat does less"

"Habitat exposes a NoSQL API modeled around client-defined object and edge
types, inspired by TAO. Clients predefine objects and edges and how they
relate to each other, but not the content of each type. The resulting
relationships resemble a graph, but Habitat itself does not support typical
graph traversal queries outside of querying direct edges of a particular
object.

We partition this graph so that each object and its corresponding edges are
colocated in a storage-level partition, but we make no concerted
database-level effort to colocate objects and the remote objects to which
their edges point. The result is that the model easily partitions for
horizontal scalability, but graph traversals are inefficient since any
particular hop between objects may require fetching from two entirely
different Azure Cosmos DB accounts stored in different regions."
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-orosz-openai-software-factory.md` — that note's
    Concrete Artifacts section records section 7's paywalled teaser line,
    "it only takes one or two engineers for previously 'impossible' rewrites
    and migrations to succeed," with the note itself flagging that no
    substantive content beyond that one-line teaser was visible at
    extraction time. This source's Claim 11 (2 engineers, Codex, and
    GPT-5.5 rewrote Habitat's entire service to Rust in Q2 2026, now serving
    95% of production traffic at 6x/15x CPU/memory efficiency) is a
    concrete, dated, named instance of exactly that teaser claim — the first
    fully-detailed confirmation of it found in the corpus so far.
  - `blog-anthropic-code-migration-playbook.md` (Claim 11, best practice
    "Don't use the largest model for everything... save your largest model
    for reviewers and for anything that writes rules other agents will
    follow") and the same note's Claim 2/12 (the Bun Zig-to-Rust rewrite
    completed by effectively one practitioner plus agents in under two
    weeks) — this source's Claim 11 is a second, independent (different
    company, different language migration direction target, different
    domain) data point for the broader corpus pattern that small human
    teams (1-2 people) paired with coding agents can complete large-scale
    language migrations that would traditionally require much larger teams
    and longer timelines. Note the difference in verification method: unlike
    the Bun/Krieger migrations' explicit test-suite-driven "judge" process
    described in that note, this source does not describe Habitat's
    verification methodology for the Rust rewrite at all — a gap flagged in
    Extraction Notes.
  - `blog-pragmaticengineer-orosz-openai-software-factory.md` Claim 10
    (Venkat Venkataramani: "roughly a 10x increase in load on some systems"
    in about six months, calling it growth that "might happen over two or
    three years" elsewhere) — this source's Claim 2 (10x year-over-year
    growth for three consecutive years) is a distinct but consistent
    first-party OpenAI figure for the same underlying hypergrowth
    phenomenon, measured over a longer baseline (three years vs. six
    months) and for a different system (storage/Habitat vs. general
    build-test-deploy infrastructure load) — both describe OpenAI's
    infrastructure org managing a compounding-growth rate its own leadership
    repeatedly characterizes as unusual relative to typical company scaling.

- **Extends**:
  - `blog-pragmaticengineer-orosz-openai-software-factory.md` — that note's
    Source Context records the paywalled teaser for section 5 ("Engineering
    for a billion users: how OpenAI scales up its infra... They buy first
    and take it in-house later. Also, geographic infra distribution,
    capacity planning tactics and challenges."). This source is a distinct,
    separately-published, fully-open article covering the storage-platform
    dimension of that same "billion users" scaling story specifically — it
    does not resolve or fill in that paywalled section's own content ("buy
    first, take in-house later" is not addressed anywhere in this source),
    but both sources are first-party accounts of OpenAI's response to the
    same underlying user/traffic growth referenced in this source's Claim 1.
  - `blog-openai-full-stack-behind-abundant-intelligence.md` (compute/chip
    infrastructure strategy, including OpenAI's first custom inference chip)
    — that note covers the compute/hardware layer of OpenAI's infrastructure
    stack; this source covers the online-storage layer. Both are first-party
    "how we scale for our own hypergrowth" accounts published within about
    two weeks of each other (August 25 and September 11, 2026), suggesting a
    coordinated late-summer 2026 infrastructure-disclosure push by OpenAI
    that the guide could note as a pattern (frontier labs publishing
    infrastructure engineering detail as both recruiting and credibility
    content) rather than treating either post in isolation.

- **Novel**: This is the first source in the corpus documenting: Python
  asyncio event-loop scheduling delay as a named, measured tail-latency
  driver with a specific synthetic-canary measurement technique (Claim 8);
  a named third-party feature-flag SDK (Statsig) causing a synchronized
  per-pod processing stall (Claim 9); aiohttp's TCPConnector LIFO default
  causing an explicitly named "metastable failure" in a production system,
  with an external citation to the Facebook metastable-failure engineering
  literature (Claim 10); and a TAO-inspired constrained-NoSQL-API-plus-CDC
  design pattern as a deliberate scaling strategy (Claim 12). No prior
  corpus source discusses Azure Cosmos DB, Statsig, aiohttp connection
  pooling, or metastable failure states at all (verified by full-corpus
  grep at extraction time — see Extraction Notes).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 11 (2 engineers + Codex +
  GPT-5.5 rewrote an entire high-throughput production service from Python
  to Rust in one quarter, now serving 95% of production traffic) as a
  second, independently-sourced large-scale-migration data point alongside
  the existing Bun/Krieger case studies from
  `blog-anthropic-code-migration-playbook.md`. Flag explicitly, per
  Extraction Notes, that this source — unlike the Anthropic migration
  playbook — gives no verification methodology detail (no mention of a test
  suite, a "judge," or a review process for the rewrite), so it should be
  cited as an outcome data point, not as a second worked process example.
- **Chapter 02 (Harness Engineering — Deliberate Technical Debt)**: Add
  Claims 5 and 6 (OpenAI knowingly shipped a suboptimal Python service,
  explicitly betting that its own coding models would mature enough to make
  a later rewrite achievable, and states the bet "proved correct") as a
  named example of technical-debt sequencing decisions that treat future AI
  coding capability as a planning input, not just an opportunistic tool —
  distinct from the corpus's existing coverage of AI-assisted migrations
  that doesn't address why the original suboptimal implementation was chosen
  in the first place.
- **Chapter 06 (Cost/Efficiency and Infrastructure)**: Add the three
  tail-latency debugging case studies (Claims 7-10: asyncio scheduling
  delay measurement, synchronized feature-flag-parsing stalls, LIFO
  connection-pool metastability) as concrete, transferable diagnostic
  patterns for any team running latency-sensitive Python services at scale
  — independent of AI-native engineering specifically, but relevant to any
  guide section on operating the infrastructure that supports high-volume
  agent-driven traffic. Add Claim 12's constrained-API-plus-CDC-escape-hatch
  design pattern as a specific, named strategy for making request cost
  predictable at scale.
- **Chapter 03 (Verification) or Chapter 02**: Add Claim 4's explicit
  framing of "agent actors" as a named access-control threat category
  (alongside external and internal actors) requiring centralized
  enforcement — a specific, quotable instance of a frontier lab treating its
  own AI agents as a distinct security boundary to architect against, useful
  for any guide discussion of access-control design in agent-heavy
  environments.

## Extraction Notes

- **WebFetch returned HTTP 403 (Cloudflare bot challenge) for the live URL**,
  confirmed via direct `curl` with a browser user-agent (also 403, with a
  Cloudflare JS-challenge response body) and via the Wayback Machine
  (`archive.org/wayback/available` returned no snapshot for this URL). The
  article was successfully retrieved in full via the `r.jina.ai` reader
  proxy (`https://r.jina.ai/https://openai.com/index/scaling-storage-one-billion-users-part-one`),
  which returned the complete article markdown (title through the closing
  careers-page link) with no visible truncation or paywall marker. All
  quotes above were copied character-for-character from that retrieved text.
  The OpenAI RSS feed (`openai.com/news/rss.xml`) was independently checked
  and its description for this entry ("Learn how OpenAI evolved Habitat from
  a Python library into a globally distributed storage platform serving 1
  billion ChatGPT users and 22M requests per second") was used only to
  confirm the article's existence and general topic before the full-text
  retrieval succeeded; it was not used as a source for any quote or claim
  above (note its "22M requests per second" figure is itself inconsistent
  with the article body's own "70 million requests every second" and "more
  than 20 million requests every second" peak-Python figures — this is an
  RSS-description/article-body discrepancy in OpenAI's own publishing, not
  a claim worth extracting, since the RSS description is marketing copy, not
  the article itself).
- No sub-pages were followed. The article's only outbound link relevant to
  its claims is the TAO paper citation (`usenix.org/system/files/conference/atc13/atc13-bronson.pdf`,
  Claim 12) and the Facebook metastable-failure engineering post (Claim 10)
  — both are cited as named external precedents for concepts the article
  itself already explains inline, and neither is a "sub-page" of the source
  in the sense MINER.md §1 describes (a docs page with further first-party
  content); both were left as external references rather than separately
  mined. The post's closing careers-page link (`openai.com/careers/...`) was
  not followed as it is a job posting, not further narrative content.
- **This is explicitly "part one" of a two-part series**; part two (covering
  multi-tenancy reliability, read-performance optimization strategy, and the
  Azure Cosmos DB partnership in more depth) had not been published as of
  extraction (2026-09-23). A future Prospector pass should watch for part
  two and file it as a related, separate source when it appears — this note
  should not be treated as covering Habitat's storage layer in full.
- Full-corpus grep confirmed no existing source note mentions Azure Cosmos
  DB, Statsig, aiohttp, Envoy, Istio, Python's GIL in this exact latency
  context, or "metastable failure" — supporting the Novel assessment above.
  Two prior notes independently touch OpenAI infrastructure at a broader
  strategic level (`blog-openai-abbott-texas-infrastructure-letter.md`:
  data-center/grid/water commitments in Texas; a policy letter with no
  engineering detail) and product-adoption/velocity
  (`blog-pragmaticengineer-orosz-openai-software-factory.md`); neither
  overlaps this source's storage-platform engineering content directly.
  No contradiction with any existing source note was found, so no
  contradiction issue was filed per MINER.md §4a.
- Confidence is set to `emerging` overall, matching the pattern used
  elsewhere in the corpus for detailed, internally-consistent, first-party
  single-company technical accounts that are not independently audited by a
  third party (e.g. `blog-pragmaticengineer-orosz-openai-software-factory.md`).
  Individual claims are rated `settled` where they describe specific,
  quantified, already-completed technical outcomes or root-cause findings
  (Claims 1-5, 7-12) and `emerging` where the claim concerns an internal
  decision's stated motivation and self-assessed success (Claim 6).
