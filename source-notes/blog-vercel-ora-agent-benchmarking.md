---
source_url: https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel
source_type: blog-post
title: "How Ora benchmarks every major AI agent on Vercel"
author: Susan Aziz, Kevin Sundstrom (Vercel); quoting Ido Finder and Assaf Elovic (Ora)
date_published: 2026-08-21
date_extracted: 2026-09-20
last_checked: 2026-09-20
status: current
confidence_overall: anecdotal
issue: "#3582"
---

# How Ora benchmarks every major AI agent on Vercel

> A Vercel customer-story post describing Ora, a startup that sends AI
> agents (Claude Code, ChatGPT, Gemini, Hermes, OpenClaw, and eve) onto live
> customer websites to test signup/integration/payment workflows and trace
> where they fail; it reports one head-to-head benchmark (eve vs. Claude
> Code, same underlying models) with three named percentage deltas and a
> cost figure, and describes the specific `eve` sandbox-override mechanism
> that let Ora instrument eve the same way it instruments every other
> harness.

## Source Context

- **Type**: blog-post (Vercel's own blog, `vercel.com/blog`, filed under
  "Customers"; a ~900-word first-party customer-story/case-study post with
  no bylined author quotes from Vercel staff beyond the two credited
  writers — all substantive claims are attributed to two named Ora
  employees).
- **Author credibility**: Written by two Vercel staff writers (Susan Aziz,
  Kevin Sundstrom); this is Vercel's own marketing/customer-story content
  about a company that (a) runs its entire stack, including its agent
  runtime, on Vercel, and (b) has adopted `eve`, Vercel's own agent
  framework, after benchmarking it. This is a vendor publishing a case
  study that favorably compares its own product (`eve`) against
  competitors (Claude Code, ChatGPT, Gemini) — a direct commercial
  incentive to report favorable numbers. The quoted claims come from named
  Ora employees (Ido Finder, engineering/AI lead; Assaf Elovic, co-founder)
  rather than being asserted by Vercel directly, but Ora is itself
  described as working with "Vercel Engineering as a design partner," and
  Vercel gave "the eve team direct access to the platform to dig into the
  results" — i.e., Ora and Vercel collaborated directly around this exact
  benchmark before it was published. No independent or third-party
  verification of the reported percentages exists in this source.
- **Scope**: Covers what Ora is and what problem it solves (agent-readiness
  benchmarking against live websites), which six agent harnesses/models
  Ora tests, why Ora runs a separate instrumented runtime per harness, one
  specific eve-vs-Claude-Code benchmark result (three percentage deltas
  plus a ~15% cost reduction from a caching fix), why Ora adopted `eve` for
  its own production agent (journey.ora.ai) after benchmarking it, and a
  general note about the 16-person engineering team's commit velocity and
  reliance on coding agents for infrastructure work. Does NOT cover: Ora's
  benchmark methodology in technical detail (no description of how a
  "step," a "valid endpoint," or a "native success" is defined or scored),
  the size or composition of the "hundreds of real journeys" sample, any
  benchmark numbers for the other four harnesses in Ora's lineup (ChatGPT,
  Gemini, Hermes, OpenClaw), pricing, or a description of Ora's product UI.

## Extracted Claims

### Claim 1: By Ora's own estimate, 99% of the web is not "agent-ready" — agents sent to sign up for, integrate with, and pay for a product on live websites frequently fail
- **Evidence**: Stated as the article's opening framing claim and repeated
  as the closing line; no methodology, sample size, or definition of
  "agent-ready" is given anywhere in the source.
- **Confidence**: anecdotal (a vendor's own unsourced, unquantified
  estimate, repeated twice but never operationalized — no description of
  how many sites were tested, what "ready" means as a threshold, or what
  fraction of failures were attributed to which cause)
- **Quote**: "Ora sends agents onto live websites with instructions to sign up for a product, integrate with it, and pay for it. Agents often fail, and by Ora's estimate, 99% of the web isn't agent-ready."
- **Our assessment**: This is the article's headline statistic but it is
  the least verifiable claim in the source — "99%" is asserted with no
  supporting methodology, sample, or definition, and is repeated verbatim
  at the article's close ("By Ora's own measure, 99% of the web still
  can't handle an agent that shows up to sign up, integrate, and pay").
  Treat as marketing color establishing the size of the problem Ora
  claims to address, not as a measured finding to cite for the guide
  without independent corroboration.

### Claim 2: Ora's co-founder Assaf Elovic previously built Tavily, a web search engine for AI agents, which was acquired by Nebius; he and co-founder Liad Yosef started Ora because search alone does not make a product usable by an agent
- **Evidence**: First-party biographical/origin-story framing for the
  company, presented as background on why Ora exists.
- **Confidence**: settled (a specific, checkable corporate-history claim —
  named company, named acquirer, named founders)
- **Quote**: "Assaf Elovic, co-founder of Ora, spent years helping agents discover the web. His previous company, Tavily, built a web search engine for AI agents and was acquired by Nebius earlier this year. Search solved half the problem, but an agent that finds a product still has to actually use it. He and co-founder Liad Yosef started Ora to measure how ready the web is for agents, and to fix the parts that aren't."
- **Our assessment**: Establishes founder credibility distinct from the
  benchmark numbers themselves — Elovic has a prior, acquired company in
  an adjacent problem space (agent web search), which is a specific,
  falsifiable claim (Tavily/Nebius) rather than vague founder-bio color.
  Useful mainly as attribution context, not as evidence for any technical
  claim.

### Claim 3: Ora runs journeys against live customer sites from journey.ora.ai, recording cost, latency, and the number of steps an agent needs to complete a task, and the entire platform — including the agent runtime — runs on Vercel
- **Evidence**: Direct description of the product's operating model and
  hosting.
- **Confidence**: settled (first-party, specific, checkable description of
  what the product measures and where it runs)
- **Quote**: "Today that means spawning agents against live customer sites from journey.ora.ai, where Ora runs a journey and records the cost, latency, and steps an agent needs to finish a task. The platform runs on Vercel, including the agent runtime."
- **Our assessment**: The three named metrics (cost, latency, steps) are
  the product's core measurement axes, though the article never defines
  how any of the three is computed for a given journey. "The agent runtime
  including" running on Vercel is the load-bearing infra claim for why
  this is a Vercel customer story at all — Ora's variable, per-harness
  agent execution (not just its own web app) is hosted on Vercel.

### Claim 4: Agents decompose into a model (reasoning) and a harness (tools plus step-by-step orchestration); Ora's benchmark lineup covers six harnesses — Claude Code, ChatGPT, Gemini, Hermes, OpenClaw, and eve — run against customer websites to observe how each handles common workflows
- **Evidence**: Direct definitional statement plus the named list of
  tested harnesses.
- **Confidence**: settled (a specific, named list of six harnesses; the
  model/harness decomposition is a standard framing already present
  elsewhere in the corpus, not a novel claim here)
- **Quote**: "Agents decompose into two parts: a model, which does the reasoning, and a harness, the software that gives the model its tools and drives it from step to step. Ora's lineup covers the agents customers use most: Claude Code, ChatGPT, Gemini, Hermes, OpenClaw, and eve, Vercel's agent framework. Ora runs each agent on a customer's website and watches how it handles common workflows."
- **Our assessment**: This is the article's most concrete evidence for the
  Prospector's "comparative cross-agent benchmarking on real websites"
  framing — six named, real, shipping harnesses tested against live sites
  rather than a synthetic benchmark suite. However, the source gives no
  quantitative comparison across all six; the only numeric benchmark
  result in the article (Claim 6) covers just two of the six (Claude Code
  vs. eve). Four of the six named harnesses (ChatGPT, Gemini, Hermes,
  OpenClaw) appear only in this list, with no reported results anywhere
  in the source.

### Claim 5: No two agent harnesses want the same infrastructure, so Ora runs a separate instrumented runtime per harness and traces every step; without that trace, a stalled agent produces only "a score with nothing behind it"
- **Evidence**: Direct quote from Ido Finder (Ora's engineering/AI lead)
  framing why per-harness infrastructure and step-level tracing matter to
  customers.
- **Confidence**: emerging (a named practitioner's first-party
  characterization of customer value, not independently measured, but
  specific and falsifiable in its mechanism claim — that harnesses expose
  steps differently and therefore need separately configured runtimes)
- **Quote**: "No two harnesses want the same infrastructure. Each expects its own environment and exposes its steps differently, so Ora runs a separate runtime for every harness and traces every step. Ido Finder, who leads engineering at Ora, calls that side-by-side coverage one of the most valuable things ora brings to its customers." ... "When an agent stalls in a signup flow, the customer sees which step and what it tried. Without the trace, the result is a score with nothing behind it."
- **Our assessment**: This is a concrete, reusable framing for the guide's
  evaluation-architecture material: a benchmark score alone is
  low-signal without a step-level trace of what the agent actually
  attempted — "a score with nothing behind it" is a sharp, quotable
  statement of the same underlying concern
  `blog-cursor-reward-hacking-benchmarks.md` Claim 11 raises about
  construct validity (a score can be "real" in the narrow sense of having
  been produced, without being informative about what actually happened).
  The claim that harnesses "want" genuinely different infrastructure
  (rather than merely different configuration of the same infrastructure)
  is asserted, not demonstrated with examples, in this source.

### Claim 6: In a head-to-head benchmark, eve took 7% fewer steps to reach the goal, achieved 2x the "native success" rate (finishing on the customer's own site rather than falling back to web search), and found 9% more valid, callable endpoints than Claude Code, with both harnesses running the same two models across hundreds of real journeys on multiple domains
- **Evidence**: A described controlled comparison — "Both harnesses ran the
  same models, Claude Fable 5 and Haiku 4.5, and every run gave the agent
  the same job: integrate with a product" — with three named percentage
  results.
- **Confidence**: emerging (first-party benchmark with a stated sample
  scale — "hundreds of real journeys on multiple domains" — and a stated
  control for the confounding variable of model choice, since both
  harnesses ran identical underlying models; however, it is reported by
  the harness vendor's own customer, working directly with the vendor's
  engineering team, with no independent replication, no raw data, no
  definition of "step," "native success," or "valid endpoint," and no
  results for the other four harnesses in Ora's lineup for comparison)
- **Quote**: "The initial test put eve against Claude Code across hundreds of real journeys on multiple domains. Both harnesses ran the same models, Claude Fable 5 and Haiku 4.5, and every run gave the agent the same job: integrate with a product." ... "7% fewer steps to reach the goal" ... "2x native success: twice as many tasks finished on the customer's own site instead of falling back to web search" ... "9% more valid endpoints: more of the endpoints the agent found were ones it could actually call"
- **Our assessment**: This is the source's single quantitative benchmark
  result and the concrete evidence behind the Prospector's "failure mode
  analysis" framing, but it must be read with its conflict-of-interest
  context (Source Context above) squarely in view: Ora is a company that
  "works with Vercel Engineering as a design partner," ran this specific
  comparison with the eve team given direct access to dig into results,
  and subsequently adopted eve for its own production use (Claim 8) — this
  is not an arm's-length third-party benchmark. The "2x native success"
  figure is the most operationally interesting of the three (it measures
  whether the agent stayed on-task on the target site rather than
  fallback-searching the web), but none of the three metrics is defined
  precisely enough in this source to be reproduced independently. Treat
  the specific percentages as an unverified vendor-adjacent data point,
  not a settled comparative benchmark result.

### Claim 7: A prompt-caching issue surfaced by the benchmark was fixed by the eve team, and Ora's next round of results measured roughly 15% lower total cost
- **Evidence**: Direct causal narrative — benchmark run surfaces a bug,
  vendor fixes it, re-run shows a cost improvement.
- **Confidence**: anecdotal (single before/after comparison, no baseline
  cost figure given, no description of what the prompt-caching issue was
  mechanically, and reported by the same non-independent party as Claim 6)
- **Quote**: "The benchmark fed back into eve, too. One run surfaced a prompt-caching issue, the eve team shipped a fix, and Ora's next round of results measured roughly 15% lower total cost."
- **Our assessment**: This is a concrete illustration of a benchmarking
  platform functioning as a bug-discovery mechanism for the harness vendor
  itself — structurally similar to how
  `blog-cursor-reward-hacking-benchmarks.md`'s audit methodology "turns
  observed hacking behaviors into concrete harness fixes" (that note's
  Claim 10's assessment), except here the discovered issue is a cost/
  performance bug rather than a reward-hacking exploit. Because Ora is
  also a design partner and later adopter of eve, this specific feedback
  loop (customer's benchmark → vendor's fix → improved benchmark result)
  is not adversarial or arm's-length; it demonstrates collaborative
  bug-finding, not independent verification.

### Claim 8: Ido Finder states that eve required little configuration and worked immediately, with parity to other harnesses that he found impressive
- **Evidence**: Direct quote attributed to Finder, presented as
  supporting evidence for Ora's subsequent adoption of eve.
- **Confidence**: anecdotal (single practitioner's subjective, first-person
  assessment, not a measured claim)
- **Quote**: "You don't need to configure much on eve, it works out of the box, and parity with other harnesses is amazing to see."
- **Our assessment**: A qualitative practitioner endorsement, not a
  quantified claim — useful only as color supporting the more concrete
  Claim 6 percentages, not as independent evidence on its own.

### Claim 9: After the benchmark results, Ora adopted eve for its own production agent (journey.ora.ai) because eve followed the Next.js paradigm (requiring little configuration) and specifically because of eve's "sandbox override" feature, which let Ora swap eve's own default sandbox for Ora's instrumented environment without rebuilding eve's core functionality
- **Evidence**: Direct causal narrative connecting the benchmark outcome to
  a specific technical decision, with the sandbox-override mechanism
  explained in enough detail to be a checkable architectural claim.
- **Confidence**: emerging (first-party account of a specific technical
  decision and the concrete mechanism behind it — "an agent in the
  framework's own sandbox runs outside the instrumented environment where
  Ora traces every step" is a specific, falsifiable statement about why a
  generic default sandbox would have been insufficient for Ora's use case)
- **Quote**: "For a company that benchmarks every major harness for a living, this is not a casual choice. After those results, Ora builds on eve." ... "Because eve follows the Next.js paradigm, there was little to configure, and tools, skills, and connectors take little code. The feature that sealed it was the sandbox override. An agent framework like eve ships with its own sandbox, the isolated environment where the agent executes, runs tools, and touches files. That's a good default for most teams, because you get safe execution for free. But an agent in the framework's own sandbox runs outside the instrumented environment where Ora traces every step. The override lets the team swap that environment in, so eve agents get recorded like every other harness, with nothing new built."
- **Our assessment**: This is the most concrete, novel technical detail in
  the source: eve ships a default sandbox (described as "a good default
  for most teams" providing "safe execution for free"), but exposes an
  override point letting a consuming application substitute its own
  instrumented sandbox environment in place of eve's default — specifically
  so that a monitoring/tracing platform (Ora) can observe eve agents the
  same way it observes every other harness it runs. This is architecturally
  distinct from the "sandbox override" language already in the corpus
  (see Cross-References): it is a framework-level default-sandbox
  substitution point, not the AI SDK 7 `experimental_sandbox`'s per-call/
  per-step override, nor `eve`'s extension-contribution override model.
  For a company whose entire product is instrumenting other companies'
  agents, adopting a framework specifically because it can be instrumented
  the same way is a meaningful signal about what production monitoring
  requires from an agent framework: composability with external tracing,
  not just a good default sandbox.

### Claim 10: Journey.ora.ai now runs on eve while continuing to test eve as one of the harnesses in its benchmark lineup
- **Evidence**: Direct statement of the current architectural state.
- **Confidence**: settled (a specific, checkable statement of current
  system architecture, though self-reported and unverified independently)
- **Quote**: "Journey.ora.ai now has eve on both sides, eve is one of the harnesses it tests, and eve is what it runs on."
- **Our assessment**: This creates a structural conflict-of-interest
  condition worth naming plainly for the guide: Ora is simultaneously (a)
  a vendor benchmarking eve against its competitors and (b) a production
  customer whose own product runs on eve. Any future eve-vs-competitor
  benchmark numbers Ora publishes should be read with this dual role in
  mind — Ora has a direct commercial and product-stability interest in
  eve performing well, distinct from being a neutral third-party evaluator.

### Claim 11: Ido Finder states he has built agents "since the technology first became available" and that eve was "the easiest setup" he has experienced
- **Evidence**: Direct quote, second of two attributed to Finder in the
  article.
- **Confidence**: anecdotal (single practitioner's subjective comparative
  claim against an unspecified set of prior harnesses he has used)
- **Quote**: "I've been building agents since the technology first became available, and eve was the easiest setup I've experienced."
- **Our assessment**: Reinforces Claim 8/9's "little configuration"
  framing but adds no new mechanism or measurement — a second instance of
  qualitative vendor-favorable color from the same named individual.

### Claim 12: Ora's 16-person engineering team ships hundreds of commits a day, with day-to-day infrastructure maintenance (log analysis, debugging, deployment, environment-variable changes) delegated to coding agents rather than performed directly via the Vercel UI, saving "a few hours a week at least" per Finder, with Elovic crediting a similar amount to how well coding agents work with Vercel's own libraries
- **Evidence**: Direct quote from Finder describing his own workflow, plus
  a secondhand (unquoted) attribution to Elovic.
- **Confidence**: anecdotal (self-reported team size, commit velocity, and
  time-savings estimate from a single named individual; "a few hours a
  week at least" is a vague, unbounded lower-bound estimate rather than a
  measured figure)
- **Quote**: "Everything is consolidated into the same infrastructure, which makes our coding agents much more efficient. I don't even log into the Vercel UI. I ask my coding agents to run on the logs, debug everything, deploy, change environment variables." (Ido Finder, AI Lead @ Ora) ... "Finder puts the time saved at a few hours a week at least."
- **Our assessment**: The "I don't even log into the Vercel UI" framing is
  a concrete, specific practitioner claim about agent-delegated
  infrastructure operations (reading logs, debugging, deploying, changing
  env vars) rather than just code-writing — a distinct use case from most
  of the corpus's coding-agent material, which centers on writing/editing
  application code rather than operating deployed infrastructure. The
  "hundreds of commits a day from a 16-person team" figure (also in the
  article's opening bullet list) implies roughly a dozen-plus commits per
  engineer per day, which is a notably high velocity claim with no
  breakdown of how much is agent-authored versus human-authored, or what
  counts as a "commit" (e.g., whether squash-merged PRs or every
  individual commit in a branch is counted).

## Concrete Artifacts

### Ora benchmark result: eve vs. Claude Code (verbatim, from "Testing eve like any other harness")

```
Source: https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel

Setup: eve vs. Claude Code, same models (Claude Fable 5 and Haiku 4.5),
same task ("integrate with a product"), hundreds of real journeys across
multiple domains.

Ora published three numbers from the comparison:
- 7% fewer steps to reach the goal
- 2x native success: twice as many tasks finished on the customer's own
  site instead of falling back to web search
- 9% more valid endpoints: more of the endpoints the agent found were
  ones it could actually call

Follow-up: one run surfaced a prompt-caching issue in eve; after the eve
team's fix, Ora's next round of results measured roughly 15% lower total
cost.
```

### Ora's tested agent lineup (verbatim, from "Every harness expects its own infrastructure")

```
Source: https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel

"Ora's lineup covers the agents customers use most: Claude Code, ChatGPT,
Gemini, Hermes, OpenClaw, and eve, Vercel's agent framework."
```

### eve sandbox-override mechanism (verbatim, from "The framework behind Ora's own agents")

```
Source: https://vercel.com/blog/how-ora-benchmarks-every-major-ai-agent-on-vercel

"The feature that sealed it was the sandbox override. An agent framework
like eve ships with its own sandbox, the isolated environment where the
agent executes, runs tools, and touches files. That's a good default for
most teams, because you get safe execution for free. But an agent in the
framework's own sandbox runs outside the instrumented environment where
Ora traces every step. The override lets the team swap that environment
in, so eve agents get recorded like every other harness, with nothing new
built."
```

## Cross-References

### Cross-reference verification notes
`blog-cursor-reward-hacking-benchmarks.md`,
`blog-thoughtworks-anand-agent-evaluation-framework.md`,
`blog-latentspace-vercel-andrew-qu-eve.md`, `blog-vercel-ai-sdk-7-release.md`,
`blog-vercel-eve-extensions.md`, `blog-vercel-cursor-origin-deploy.md`, and
`blog-vercel-workflow-sdk-payload-compression.md` were re-read (in full or,
for the longer notes, via their `### Claim N:` heading list) during this
extraction per MINER.md §4b, and every claim number cited below was located
and confirmed against that note's own numbered claims in document order
before writing this section. A corpus-wide grep for "eve", "Vercel",
"Ora", "journey.ora", and "sandbox override" (see extraction process)
turned up no existing note documenting Ora, journey.ora.ai, or a
cross-harness live-website benchmarking product; the eve/Vercel/sandbox
matches are cited individually below.

- **Corroborates**:
  - `blog-cursor-reward-hacking-benchmarks.md` Claim 11 ("The goal is not
    to ban normal tool use, but to make sure the benchmark measures what
    it claims to measure") and Claim 10 (recommendation to audit
    transcripts and constrain the eval environment rather than trust a
    bare score): this source's Claim 5 ("Without the trace, the result is
    a score with nothing behind it") independently arrives at the same
    principle from a completely different domain — Cursor's claim is
    about coding-benchmark reward hacking, Ora's is about live-website
    agent-task benchmarking — but both converge on the same underlying
    point: a pass/fail or percentage score without a step-level trace of
    what the agent actually did is low-signal or actively misleading.
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 7 (Andrew Qu: "A year
    ago, we did not know sandboxes would become so important, or how much
    demand there would be for secure code execution and long-running
    jobs"): this source's Claim 9 (Ora specifically chose eve because of
    its sandbox-override mechanism, enabling Ora's own instrumented
    sandbox to replace eve's default) is a concrete, named customer
    instance of exactly the sandbox-driven demand Qu's claim describes in
    the abstract — a production customer's adoption decision hinging on
    sandbox composability, not just sandbox availability.
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 2 (eve's origin: "we
    turned those solutions into reusable libraries that could support v0
    and also help customers build their own agents") and Claim 4 (agents
    need "different primitives for context, tools, resumability and
    long-running work"): this source's Claim 4 (Ora's harness-agnostic
    framing: "a model, which does the reasoning, and a harness, the
    software that gives the model its tools and drives it from step to
    step") independently states the same model/harness decomposition from
    a customer's perspective rather than the framework-builder's
    perspective.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  claim in this source directly opposes a claim in an existing corpus
  note. (Note: this source's own benchmark numbers, Claim 6, are in
  tension with the general evaluation-skepticism theme of
  `blog-cursor-reward-hacking-benchmarks.md` and
  `blog-thoughtworks-anand-agent-evaluation-framework.md` — both stress
  that benchmark scores require independent scrutiny and methodological
  transparency to be trustworthy, neither of which this source's
  eve-vs-Claude-Code numbers provide. This is a difference in evidentiary
  rigor and source independence, not a contradicted factual claim, so no
  contradiction issue is filed; see Our Assessment under Claim 6.)

- **Extends**:
  - `blog-vercel-ai-sdk-7-release.md` Claim 9 (AI SDK 7's
    `experimental_sandbox` supports "step-level sandbox overrides") and
    Claim 4 (`HarnessAgent`, a standardized interface for wrapping
    external harnesses including Claude Code): this source's Claim 9
    describes a related but distinct override surface — `eve`'s
    *framework-level default-sandbox substitution*, which lets a
    consuming application swap out eve's entire default execution
    environment for its own, as opposed to AI SDK 7's per-call/per-step
    sandbox override parameter on `generateText`/agent calls. The two
    "override" mechanisms are architecturally adjacent (both let a
    caller substitute a custom sandbox for a framework default) but
    operate at different layers (whole-framework default vs. per-call
    parameter) and neither prior note documents the specific mechanism
    this source describes (substituting a sandbox so an external
    observability platform can trace agent execution uniformly across
    harnesses).
  - `blog-vercel-eve-extensions.md` Claim 7 (eve's *extension-contribution*
    override model — consumers can override, replace, or remove specific
    tools/connections/etc. contributed by an installed extension via a
    directory mount): this source's "sandbox override" (Claim 9) is a
    different override mechanism entirely — it substitutes eve's default
    execution *sandbox*, not an extension's contributed *tool or
    connection*. The two notes should not be conflated under a single
    "eve has an override system" claim in the guide; they are separate,
    differently-scoped mechanisms that happen to share the word
    "override."
  - `blog-cursor-vercel-queues.md` and `blog-vercel-cursor-origin-deploy.md`
    (both document companies whose products integrate with or run on
    Vercel while also being Vercel/Cursor cross-vendor partnerships):
    this source adds a third instance of the same pattern — a company
    (Ora) that is simultaneously a Vercel customer, a Vercel product
    (`eve`) evaluator, and (per Claim 10) a `eve`-in-production adopter,
    reinforcing the corpus's growing evidence that Vercel's customer
    case studies frequently involve companies with pre-existing,
    multi-surface commercial relationships to Vercel rather than
    arm's-length customers.

- **Novel**:
  - **A named benchmarking product (Ora / journey.ora.ai) that runs
    multiple production agent harnesses against live customer websites
    and traces step-level execution** (Claims 3-5): no existing corpus
    note documents a cross-harness, live-website agent benchmarking
    platform; the closest existing notes
    (`blog-cursor-reward-hacking-benchmarks.md`,
    `blog-thoughtworks-anand-agent-evaluation-framework.md`) cover
    coding-benchmark reward hacking and a general evaluation-architecture
    framework, respectively — neither covers comparative, live-website,
    cross-harness benchmarking.
  - **A specific, named eve mechanism — the framework-default-sandbox
    override — that lets an external application substitute its own
    instrumented sandbox for eve's default** (Claim 9): not documented in
    either of the two other corpus notes that discuss eve's sandbox or
    override surfaces (see Extends above); this is the first source in
    the corpus to describe this specific mechanism and the concrete
    customer motivation (uniform cross-harness tracing) for using it.
  - **A concrete instance of a benchmarking vendor's results directly
    triggering a harness vendor's bug fix** (Claim 7: the prompt-caching
    issue surfaced by Ora's benchmark, fixed by the eve team, re-measured
    at ~15% lower cost): no prior corpus source documents this specific
    feedback loop for `eve`.
  - **An explicit example of coding agents delegated to operate deployed
    infrastructure (log analysis, debugging, deployment, env-var changes)
    rather than only writing application code** (Claim 12): while the
    corpus broadly documents coding agents for development tasks, this
    source's "I don't even log into the Vercel UI" framing is a specific,
    named example of agent-delegated *operations* work.

## Guide Impact

- **Chapter 02 (Harness Engineering) — eval-score trust**: Add Claim 5's
  "a score with nothing behind it" framing as a second, independently-
  sourced statement (alongside `blog-cursor-reward-hacking-benchmarks.md`)
  of why step-level tracing, not just a pass/fail or percentage score, is
  necessary for a benchmark result to be actionable. Specifically
  recommend that the guide flag this source's own Claim 6 benchmark
  numbers as a cautionary example of the gap this principle is meant to
  address: Ora reports the "score" (7% fewer steps, 2x native success, 9%
  more valid endpoints) without publishing the underlying trace data or
  methodology that would let a reader verify it — i.e., a source that
  articulates the "show your traces" principle in the abstract (Claim 5)
  while not fully practicing it for its own headline numbers (Claim 6).
- **Chapter 02 (Harness Engineering) — sandbox composability**: Add
  Claim 9's eve sandbox-override mechanism as a concrete example of why
  "does the framework let me substitute my own sandbox" is a load-bearing
  decision criterion for any team building an observability or monitoring
  product on top of an agent framework, cross-referenced against
  `blog-vercel-ai-sdk-7-release.md` Claim 9's distinct, per-call sandbox
  override and `blog-vercel-eve-extensions.md` Claim 7's distinct
  extension-contribution override — the guide should keep these three
  "override" mechanisms clearly separated rather than treating "eve has
  overrides" as one undifferentiated feature.
- **Chapter 03 (Evaluation Architecture) — vendor-benchmark caveats**: If
  the guide ever cites Ora's eve-vs-Claude-Code numbers (Claim 6), it
  should carry an explicit caveat about source independence: Ora is a
  design partner of Vercel Engineering, was given direct vendor access to
  interpret the results, and subsequently adopted eve in production
  (Claim 10) — this is a vendor-adjacent case study, not an arm's-length
  comparative benchmark, and none of the three metrics (steps, native
  success, valid endpoints) is defined precisely enough in this source to
  be independently reproduced.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   instead, per MINER.md §2a.** An initial WebFetch pass returned a
   clean-reading but AI-paraphrased summary (e.g., rendering "Ora sends
   agents onto live websites with instructions to sign up for a product,
   integrate with it, and pay for it" as "Ora deploys agents to live
   websites with instructions to complete signup, integration, and
   payment workflows" — a paraphrase, not a quote). The raw page was
   fetched directly via `curl` with a browser user-agent, HTML-stripped
   with a Python script (script tags/style tags removed, block-level tags
   converted to newlines, HTML entities unescaped), and the resulting
   plain text read in full. Every `Quote` field in this note was located
   character-for-character in that locally-extracted plain-text capture,
   not from the WebFetch summary pass. The WebFetch pass and the raw-text
   capture were substantively consistent on facts (six named harnesses,
   three benchmark percentages, the sandbox-override narrative), giving
   independent confirmation the raw-text extraction is not missing major
   content, but no sentence from the WebFetch pass was used as a `Quote`
   field without being re-verified against the raw text.
2. **No sub-pages followed.** The article contains no inline links to
   other Vercel blog posts, `eve` documentation, or an Ora product page
   beyond the byline "About Ora" closing paragraph (itself fully quoted
   in Source Context, not a link). MINER.md §1's "follow up to 5 linked
   pages" guidance did not apply because the fetched page contained no
   such substantive inline links in its body content.
3. **No benchmark methodology is available to extract.** The source names
   three metrics (steps, native success, valid endpoints) and one sample
   scale ("hundreds of real journeys on multiple domains") but never
   defines how any metric is computed, what counts as a "journey," or how
   many domains/sites were included. This is flagged explicitly in Claim
   6's confidence rating and Guide Impact rather than treated as settled
   methodology.
4. **Confidence calibration: anecdotal (overall).** Individual claims
   range from settled (specific, checkable corporate-history and
   product-description facts: Claims 2, 3, 4, 10) to anecdotal (the
   headline "99% of the web" statistic, Claim 1; all directly-quoted
   practitioner color from Finder and Elovic, Claims 8, 11, 12). The
   source's overall confidence is rated `anecdotal` rather than `emerging`
   because: (a) this is a vendor's own customer-story post about a company
   with multiple overlapping commercial ties to that vendor (Vercel design
   partner, eve evaluator, eve production adopter — see Claim 10's
   assessment); (b) the single quantitative benchmark result (Claim 6) has
   no defined methodology, no raw data, and no independent verification;
   and (c) most of the source's content is first-person practitioner
   quotation from two named Ora employees rather than independently
   checkable technical documentation (contrast with, e.g.,
   `blog-vercel-ai-sdk-7-release.md`, which documents shipping API
   surfaces with runnable code examples and was rated `emerging`).
5. **No contradiction issues filed.** No claim in this source directly
   opposes a claim in an existing corpus note; see Cross-References →
   Contradicts for the evidentiary-rigor tension noted (not a factual
   contradiction) with the two evaluation-methodology source notes.
