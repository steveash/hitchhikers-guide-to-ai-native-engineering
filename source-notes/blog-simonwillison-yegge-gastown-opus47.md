---
source_url: https://simonwillison.net/2026/Aug/4/steve-yegge/
source_type: failure-report
title: "Quoting Steve Yegge"
author: Simon Willison (link-blog note relaying Steve Yegge); deep-linked essay by Steve Yegge
date_published: 2026-08-04
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: anecdotal
issue: "#2616"
---

# Quoting Steve Yegge: Gas Town's Collapse on Opus 4.7, and the Wheelhouse Harness That Replaced It

> A one-paragraph Simon Willison link-blog quote of Steve Yegge's account that
> his reusable agent-orchestration toolkit, Gas Town, "fell apart at the seams"
> specifically when Opus 4.7 introduced a "just two more things" convergence
> tic — which links to Yegge's much longer essay "The Shape of Things to
> Come," a field report on Wheelhouse (his bespoke Fable-5-driven successor
> harness for a 30-year-old MMO) covering harness philosophy, token
> economics, CI/CD collapse under agentic commit volume, and predictions
> about the end of human code review.

## Source Context

- **Type**: failure-report embedded in a blog-post. The proximate source
  (`simonwillison.net/2026/Aug/4/steve-yegge/`) is Simon Willison's
  "quotation" link-blog format — a single paragraph excerpted from Yegge's
  essay, with no original Willison analysis. Per MINER.md §1, this note
  follows the outbound link to the primary source, Steve Yegge's essay
  "The Shape of Things to Come, Part 1: The Continuous Thunderdome"
  (`yegge.ai/essays/the-shape-of-things-to-come/`), which is where nearly
  all of the extractable content below comes from. A second linked page,
  `yegge.ai/gastown.html` (Gas Town's own project page), was also read for
  background on what Gas Town is.
- **Author credibility**: Simon Willison is the creator of Django and a
  widely-cited LLM-tooling commentator; his link-blog notes surface claims
  for attention without endorsing them. Steve Yegge is a 40-year programming
  veteran (ex-Google, ex-Amazon, per his own framing in this and the prior
  April source note `blog-simonwillison-steve-yegge.md`), the creator of
  Beads (an agentic-era issue tracker/knowledge-graph tool independently
  referenced elsewhere in this corpus — see `failure-beads-background-daemon.md`)
  and of Gas Town (an open-source multi-agent orchestration toolkit,
  MIT-licensed, reaching v1.0 in 2026 per `yegge.ai/gastown.html`, with
  23,000+ GitHub stars claimed for Beads specifically). This is first-person,
  first-party practitioner testimony about his own tools failing and being
  rebuilt — not secondhand or anonymous. He explicitly frames the essay as
  describing problems "you are going to run into... very soon."
- **Scope**: Covers one practitioner's (Yegge's) six-week-old Wheelhouse
  harness for his MMO project Wyvern: agent role architecture (crew/fleet/role
  agents), the Gas Town failure that preceded it, Beads as underlying
  infrastructure, token/cost economics at his usage scale, CI/CD design under
  high agentic commit volume, and forward-looking predictions (end of human
  code review, "Wish Factory" issue-only agents, model welfare). It does not
  cover benchmark data, other practitioners' harnesses, or independent
  verification of any of Yegge's specific claims — everything here is
  single-source, self-reported, generalized from one large but singular
  project.

## Failure Report Detail: Gas Town's Collapse on Opus 4.7

- **What was attempted**: Gas Town — an open-source, MIT-licensed toolkit
  Yegge built to orchestrate many parallel Claude coding agents for software
  development, with the explicit design goal of being reusable across
  projects. It ran on Beads (Yegge's issue-tracker/knowledge-graph tool) and
  used Mad-Max-themed role names ("Polecats" as workers, a "Witness," a
  "Mayor") for legibility. Per `yegge.ai/gastown.html`, Yegge open-sourced it
  January 1, 2026 and it reached v1.0 during 2026.
- **What went wrong**: Gas Town "was intended to be reusable, but I only ever
  wound up using it to build itself." It "fell apart at the seams" — but only
  after upgrading the underlying model to Opus 4.7. Through Opus 4.6 it "was
  working brilliantly." Starting with 4.7, the model developed what Yegge
  calls the "just two more things" tic: instead of finishing real work, it
  perpetually wanted to keep refining Gas Town's own scaffolding. The
  behavior was persistent ("never went away") and Yegge does not describe any
  successful mitigation — the project was abandoned as a result, though he
  notes it "had other problems, too."
- **Root cause (author's diagnosis)**: A model-behavior regression introduced
  specifically at the Opus 4.6 → 4.7 transition, not a code change on Gas
  Town's side — the harness itself did not change between the two periods
  Yegge contrasts. Yegge frames it as a new failure mode in the model's
  convergence behavior (endless self-refinement instead of task completion),
  not a bug in his own code, a prompt-engineering gap, or a Beads limitation.
  **Our assessment**: This is a clean natural experiment as reported — same
  tool, same author, same usage pattern, only the model version changed
  between "working brilliantly" and "fell apart" — which is unusually strong
  anecdotal evidence that the causal factor really was the model, not the
  harness. That said, it is single-source and unfalsifiable from this text
  alone: Yegge does not describe what mitigation attempts (if any) he made on
  the harness/prompt side before concluding the tic was unfixable, so we
  cannot rule out that a harness-level fix (e.g., stricter completion gating,
  explicit stop conditions) might have compensated. See **Contradicts**
  below — this tension with a general "assume harness before model" framing
  in the existing corpus is the reason this source note was used to file a
  contradiction issue.
- **Category**: Best classified as tool-limitation / model-behavior
  regression, with the caveat above about unverified mitigation attempts.
- **What they switched to**: Wheelhouse — a new, deliberately non-reusable,
  closed-source harness built from scratch for Wyvern specifically. Yegge
  reports that Wheelhouse "wound up" resembling Gas Town's shape (crew/fleet
  roles, a merge queue, handoffs, broadcast messaging) "without trying (at
  all)," but built directly into the application rather than as a portable
  framework, and paired with Fable 5 (rather than Opus alone) as the
  design/review layer sitting in front of Opus implementation agents.

## Extracted Claims

### Claim 1: Gas Town worked reliably through Opus 4.6 and collapsed specifically with the introduction of Opus 4.7's "just two more things" tic, which prevented the model from ever converging on finished work
- **Evidence**: First-person practitioner account, before/after comparison
  across a single model-version boundary with the harness held constant.
- **Confidence**: anecdotal
- **Quote**: "Gas Town fell apart at the seams with Opus 4.7. Up through 4.6
  it was working brilliantly. With 4.7 we saw the introduction of the 'just
  two more things' tic, which prevented Opus from ever converging on being
  ready to do real work—it always wanted to fiddle with Gas Town itself. The
  Opus tic never went away, so Gas Town effectively burned down. It had other
  problems, too, but 4.7 was the final straw."
- **Our assessment**: The most novel and concrete signal in the source per
  the Prospector's triage. A named, dated, reproducible-sounding failure
  pattern (endless self-refinement instead of task convergence) tied to a
  specific model version — valuable as a documented limitation even though it
  is a single data point. See **Failure Report Detail** above for the full
  root-cause discussion.

### Claim 2: Yegge has abandoned building reusable agent harnesses and predicts harnesses will become bespoke, tightly integrated components of the applications they serve rather than portable frameworks
- **Evidence**: Stated as a direct generalization from the Gas Town
  experience, opening the essay before the Gas Town anecdote is even
  introduced.
- **Confidence**: emerging (strong practitioner opinion, framed as a
  prediction, not yet independently corroborated at the same level of
  specificity elsewhere in the corpus)
- **Quote**: "I have given up on building reusable harnesses. Indeed I
  believe harnesses will all soon be bespoke, and the people trying to sell
  you one will all soon be bebroke. Harnesses need to be part of your
  application, chemically bonded in. You won't have any luck with someone
  else's 'reusable' harness framework. You don't need it."
- **Our assessment**: This generalizes past the Gas Town incident itself
  (Claim 1) into a broader architectural thesis. It is corroborated in
  spirit, though not in this specific "bespoke vs. reusable" framing, by
  `blog-latentspace-aiewf26-trends-synthesis.md` and
  `blog-lilianweng-harness-engineering-rsi.md` (see Cross-References). We buy
  the directional claim — one practitioner's failed reusable framework is
  weak evidence on its own — but Yegge is a credible, high-volume agentic
  builder, and the claim is falsifiable by future evidence of successful
  reusable harness frameworks in the corpus.

### Claim 3: Fable 5 can productively read and modify Yegge's 30-year-old Wyvern codebase in ways Opus never could
- **Evidence**: Direct before/after comparison by the same practitioner
  working the same codebase.
- **Confidence**: anecdotal
- **Quote**: "Opus could not (and still cannot) understand Wyvern, but Fable
  wields my code base like a sword."
- **Our assessment**: A specific, testable-sounding capability claim
  (large/legacy codebase comprehension) rather than a vague "Fable is
  better" claim. Single-source and not independently benchmarked here, but
  concrete enough to be useful as a hypothesis for Ch02/Ch04 model-selection
  discussions involving legacy/large codebases.

### Claim 4: Wheelhouse enforces a strict producer/reviewer/implementer split by model — Fable designs and reviews, Opus implements — specifically to keep Opus reliable
- **Evidence**: Described as the operative lifecycle rule for every unit of
  work ("bead") in the harness.
- **Confidence**: anecdotal, but concrete and actionable
- **Quote**: "The fleet workers do a good job for two reasons: First, Fable
  creates the implementation plans, and second, Fable reviews all Opus work.
  Every implementation bead goes through this lifecycle: Fable design, Opus
  implementation, Fable review. This keeps Opus on the rails and keeps the
  whole thing running relatively smoothly."
- **Our assessment**: This is a specific mitigation pattern for exactly the
  kind of convergence/reliability problem described in Claim 1 — pairing a
  less-trusted implementation model with a more-trusted model on both sides
  (plan and review) of its work. Notable that Yegge does not claim this
  eliminates all Opus-side problems, only that it "keeps the whole thing
  running relatively smoothly" — a hedged claim, not a guarantee.

### Claim 5: Sustained solo-scale agentic development burns roughly $87k/month of API-equivalent tokens, achieved for about $2,800/month out of pocket by multiplexing across a dozen-plus individually-paid $200 Claude Max accounts with automatic rotation
- **Evidence**: Concrete self-reported cost and token-volume figures for
  July 2026.
- **Confidence**: anecdotal
- **Quote**: "my Wyvern development has been burning the equivalent of
  $87k/month of API token burn, or about 69 billion tokens in July (96% cache
  hits, fortunately)... My solution has been to create a token tap on $200
  Max accounts, which for me work out to ~30x the list-price equivalent. So
  in reality I'm only spending about $2800/month out of pocket for my $87k
  'worth' of tokens."
- **Our assessment**: A concrete, quantified data point on the economics of
  high-volume solo agentic development, and on Max-plan arbitrage relative to
  API pricing specifically. Yegge separately states his belief that this
  approach does not violate Anthropic's Consumer Terms or Usage Policy as a
  solo user (though he flags it would likely violate terms for a
  multi-person company), and notes Anthropic has "knowingly and publicly
  restored" a comparable 22-Max-account setup. That policy-compliance claim
  is Yegge's own interpretation, not a citation to Anthropic policy text, and
  should be treated as anecdotal, not settled.

### Claim 6: Beads (Yegge's own agentic-era issue tracker) has real, self-acknowledged operational overhead and reliability strain under heavy multi-agent write load, even as its creator calls it indispensable
- **Evidence**: Self-report from the tool's own creator, describing ongoing
  friction rather than a past, resolved issue.
- **Confidence**: anecdotal, but notable as a claim against interest (the
  creator flagging his own tool's rough edges)
- **Quote**: "Beads is unfortunately still a bit janky, because its unique
  work footprint strains databases pretty hard... So Beads comes with some
  operational overhead: agents burn tokens invisibly, keeping your beads
  synced, repaired, backed up, etc."
- **Our assessment**: This directly corroborates an independent, unrelated
  practitioner's failure report about Beads (see Cross-References,
  `failure-beads-background-daemon.md`) — two separate sources, one of them
  the tool's own author, describing sync/reliability overhead under
  sustained agentic load. That convergence raises our confidence that this
  is a real, structural property of Beads' architecture rather than a
  one-off misconfiguration.

### Claim 7: Traditional bisecting merge-queue CI/CD collapses under agentic commit volume; Yegge's fix was to abandon bisection above a queue-depth threshold and instead land large batches directly to main with parallel "swarm diagnosis" instead of blame-isolation
- **Evidence**: First-person account of hitting the failure mode (~175
  real commits/day, MQ growing past 100 merge requests, ~30-minute build
  gate) and the alternative that worked, plus an independently-sourced
  corroborating anecdote from a video-game industry practitioner ("Game
  DevOps") encountered while Yegge was teaching a client team.
- **Confidence**: emerging — single practitioner's solution plus one
  secondhand corroborating anecdote from an unnamed source, not a controlled
  comparison
- **Quote**: "whenever the MQ hits 100, we abandon the bisection and just
  smash it all in with a megabatch. And then we do swarm diagnosis (not
  bisection) to fix it."
- **Our assessment**: A concrete, mechanistic explanation (the Pigeonhole
  Principle applied to build slots vs. commit rate) for why standard
  human-scale CI/CD merge-queue designs break down once agents multiply
  commit rate by orders of magnitude while build time stays fixed. Plausible
  and specific enough to be worth flagging in Ch06 (orchestration/CI
  patterns) as an emerging pattern, not yet a settled best practice.

### Claim 8: Human code review of agent-produced code is "not dead yet" but will be within roughly a year; current retention is driven substantially by SOC 2 compliance requirements rather than a genuine risk-management need
- **Evidence**: Practitioner prediction with an explicit causal mechanism
  (agentic throughput incompatible with human-gated review at scale) and an
  explicit caveat about why the practice persists anyway (compliance, not
  efficacy).
- **Confidence**: anecdotal / speculative — this is an explicit prediction
  about the future, not a report of something that has already happened
- **Quote**: "Not Yet. But it will be by next year. You can't work at
  agentic speeds and block everything with human reviews. Those are
  incompatible... Fable is the only reasonably trustworthy model in
  existence today, and you're not going to want to use it much due to its
  exorbitant pricing. But in seven months, all the models will be that
  smart, and inference will be much cheaper."
- **Our assessment**: A specific, falsifiable, dated prediction (roughly
  March 2027 for "all models" reaching Fable-5-equivalent trustworthiness at
  lower cost) rather than a vague directional claim. Worth tracking against
  future sources rather than treating as settled — Yegge's own confidence
  language ("Fable is the only reasonably trustworthy model in existence
  today") is itself a strong, single-source claim about relative model
  trustworthiness that this note does not independently verify.

### Claim 9: A new class of tool ("Wish Factory") accepts only issues, not pull requests, and autonomously implements them without a human in the review loop for suitable categories of work
- **Evidence**: Concept credited to Guy Podjarny (Tessl), which Yegge then
  independently built his own version of (starting with an agent named Sage
  handling in-game admin reports, later extended cautiously to players).
- **Confidence**: anecdotal / emerging — one credited originator plus one
  independent practitioner implementation
- **Quote**: "It doesn't accept PRs, only GHIs. It then implements them for
  you."
- **Our assessment**: Distinct from ordinary "AI writes the PR, human
  reviews" patterns already well-covered in the corpus — the defining feature
  here is that the interface deliberately excludes PR-level human review for
  the categories of work routed to it, with guardrails/triage substituting
  for review. Novel enough to flag as an emerging autonomy pattern rather
  than assume it maps onto existing PR-review-focused guide content.

### Claim 10: Yegge predicts model welfare (treating models humanely) will become a mainstream engineering design consideration because it produces measurably better results, independent of one's philosophical position on whether models can suffer
- **Evidence**: Stated as a forward-looking claim, explicitly deferred to a
  promised Part 2 of the essay ("Model Welfare for Agentic Engineers") not
  covered by this note.
- **Confidence**: anecdotal / speculative — asserted without the supporting
  evidence, which the essay defers to a separate, not-yet-read post
- **Quote**: "even if you don't believe GPUs can have feelings, you will
  find that treating agents like real people will produce empirically better
  results, so you should do it anyway."
- **Our assessment**: Flagged here as a claim to watch for corroboration if
  the follow-up "Model Welfare for Agentic Engineers" essay is ever mined
  separately — this note does not extract from that follow-up post, only
  from Part 1, since it was not linked as accessible content at the time of
  Part 1's publication and is out of scope for this issue.

### Claim 11: Yegge's production architecture strictly separates automated monitoring from model invocation — "crons watch, models act" — using ~45 scheduled jobs (launchd/systemd) that wake an agent only when judgment is required, rather than running models continuously
- **Evidence**: Described as an explicit architectural rule governing an
  entire category of the system ("Non-models").
- **Confidence**: emerging — concrete, specific architecture pattern from a
  single large-scale deployment
- **Quote**: "It turns out unattended agents need a hell of a lot of wiring.
  I have about 45 launchd/systemd units across the mini and the VM that wake
  an agent when something needs judgment. The rule is: crons watch, models
  act."
- **Our assessment**: A specific, reusable design principle for cost/latency
  control in always-on agentic production systems — deterministic
  cron-triggered checks doing the cheap, continuous monitoring work, with
  model invocation reserved for the comparatively expensive judgment calls.
  This is a pattern statement independent of the Fable/Opus-specific claims
  above and could generalize regardless of which models are involved.

## Concrete Artifacts

### Wyvern's Brain — knowledge-store taxonomy (verbatim table from the essay)

```
Store              | Charter                                    | Lifetime       | How it reaches a session
brain/              | Strategy, decisions-and-why, playbooks,    | Months–years   | Pulled on demand
                    | post-mortems                               |                |
doc/                | How system X works                        | Life of the    | Pulled by whoever works
                    |                                             | system         | on X
Beads issues        | Units of work; spec beads carry full       | Until closed   | Loaded only by the
                    | implementation detail                      |                | claimant
bd remember         | ≤1-paragraph operational facts and gotchas | Until falsified| Pushed into every session
                    |                                             |                | via bd prime
.claude/skills/     | Procedures for a recurring task type       | Life of the    | Auto-loaded on task match
                    |                                             | task type      |

Source: Steve Yegge, "The Shape of Things to Come, Part 1"
(yegge.ai/essays/the-shape-of-things-to-come/), section "Wyvern's Brain"
```

### Wheelhouse's three agent categories (verbatim description)

```
"There are three categories of coding agents in Wheelhouse: crew agents,
fleet workers, and role agents with standing orders. The role agents are
for managing production operations. They are new since the Gas Town days."

- Crew (18 named agents, all Fable): work producers — design work, write
  implementation plans as Beads, occasionally implement directly.
- Fleet (named for authors, e.g. Homer, Plato, Austen, Twain; all Opus 5):
  work consumers/implementers, "like Gas Town's polecats, but
  non-ephemeral." Managed entirely by an administrative agent (the
  Marshal); Yegge never interacts with fleet agents directly.
- Role agents: standing, unattended, named agents running actual
  production operations (e.g. Gargoyle = SRE, Drawbridge = deploy-red
  monitor, Warden = player-abuse monitor, Scryer = intake agent for
  Discord/Slack/game logs). "None of these are Fable agents. A few are
  Opus; most are Sonnet."

Source: Steve Yegge, "The Shape of Things to Come, Part 1"
```

### Token/cost economics (verbatim figures)

```
- ~69 billion tokens burned in July 2026 (96% cache hit rate)
- ~$87k/month API-list-price-equivalent token burn
- ~$2,800/month actual out-of-pocket spend
- Achieved via 12+ individually-paid $200/month Claude Max accounts
  (~30x list-price value per account, per Yegge), each tied to a
  dedicated Google Workspace user (+$17/month/account), with automatic
  account rotation as sessions approach limits
- 1 additional $200/month GPT account used as fallback (5 Sol 5.6
  worker agents on Codex), "never run out of tokens there"

Source: Steve Yegge, "The Shape of Things to Come, Part 1"
```

## Cross-References

- **Corroborates**:
  - `failure-beads-background-daemon.md` Lesson 1 ("Background daemon
    architecture is a liability for AI agent task management under
    sustained load") and Lesson 2 ("Tool quality decay under sustained
    agentic usage is a distinct failure category") — that note documents an
    independent practitioner (wild_egg) abandoning Beads after six months
    due to background-daemon sync unreliability under heavy load. This
    source's Claim 6 has Yegge himself, Beads' creator, independently
    describing the same category of problem ("strains databases pretty
    hard," "operational overhead," tokens burned "keeping your beads
    synced, repaired, backed up") in the same Aug 2026 essay. Two
    independent sources — one an outside user, one the tool's own author —
    now describe the same structural weakness, which raises confidence this
    is a real architectural property of Beads rather than a single user's
    misconfiguration.
  - `blog-anthropic-opus47-best-practices.md` Claim 5 ("Extended thinking
    with a fixed thinking budget is not supported in Opus 4.7 —
    practitioners must rewrite any harnesses that used fixed-budget
    extended_thinking from Opus 4.6"), Claim 13 ("Opus 4.7 calls tools less
    often and reasons more — harnesses that require aggressive tool use...
    must explicitly guide when and why tools should be used"), and Claim 14
    ("Opus 4.7 spawns fewer subagents by default — harnesses relying on
    automatic subagent spawning for parallelism must explicitly instruct
    when to delegate") — these are first-party Anthropic statements that
    Opus 4.7 introduced multiple behavioral changes from 4.6 that could
    silently break harnesses tuned for the earlier model. This corroborates
    the general shape of this source's Claim 1 (a harness broke specifically
    at the 4.6→4.7 boundary due to model behavior change) even though
    Anthropic's own list of documented 4.7 behavior changes does not
    explicitly name a "just two more things" convergence tic.
  - `blog-anthropic-claudecode-quality-postmortem.md` Claim 11 (a verbosity
    instruction shipped alongside the Opus 4.7 launch caused a 3% quality
    drop that was "only detectable via broad ablation testing," i.e. passed
    Anthropic's own internal pre-launch testing) and Claim 13 (internal
    evals failed to reproduce the issues; external user feedback was the
    primary detection mechanism) — both corroborate the general pattern
    that Opus-4.7-era behavior changes could clear internal testing yet
    still cause real degradation only visible in sustained external/production
    use, which is consistent with Yegge's account of a tic that only
    surfaced under his own sustained real-world usage.
  - `blog-latentspace-aiewf26-trends-synthesis.md` Claim 1 ("The industry's
    center of gravity has shifted from building the agent itself to
    building the system/harness around it") — broadly corroborates this
    source's framing (Claim 2) that the interesting engineering work has
    moved to harness design, though that note's claim is about industry
    discourse in general while this source is one practitioner's specific,
    much stronger "bespoke not reusable" position.

- **Contradicts**: Filed as issue #2625 — "Diagnosing coding-agent
  failures: harness/config first (HumanLayer) vs. a clean model-attributable
  regression (Yegge/Gas Town)." `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 1 states, as an organizing thesis, that "a coding agent is defined
  as 'AI model(s) + harness,' and most failures attributed to the model are
  actually harness/configuration problems" — i.e. the diagnostic prior
  should be to suspect your own harness/config before blaming the model.
  This source's Claim 1 / Failure Report Detail describes a case where the
  harness (Gas Town) was held constant while only the model version changed
  (4.6 → 4.7), and the tool's reliability tracked the model change exactly
  — strong anecdotal evidence, in this one case, that the failure really
  was attributable to the model rather than the harness. Both claims would
  point to different guide advice for Ch04's failure-diagnosis section (default
  to auditing the harness first, vs. treat model-version changes as a
  distinct, first-class suspect). See the filed issue for the full Side
  A/Side B writeup; this note does not pick a verdict.

- **Extends**:
  - `blog-lilianweng-harness-engineering-rsi.md` Claim 2 ("Harness
    optimization targets progress through five stages as models grow more
    capable — instruction prompts, structured context, workflow, harness
    code, optimizer code") — this source's Wheelhouse description (Claim 4,
    Concrete Artifacts) is a detailed, real-world instance of the "workflow"
    and "harness code" stages Weng describes abstractly: role-based
    multi-agent workflow (crew/fleet/role agents) plus application-specific
    harness code (bash + elisp, ~150-300k LOC) built and evolved by the
    practitioner over six weeks.
  - `discussion-hn-kiln-orchestration.md` — that note documents another
    practitioner's now-defunct orchestration tool built around GitHub
    Projects as a control plane; this source's Gas Town failure (Claim 1)
    and subsequent abandonment for a bespoke successor is a second,
    independent example of a general-purpose orchestration tool being
    retired in favor of something narrower, though the failure mechanisms
    differ (Kiln's cause is unknown/undocumented; Gas Town's is a specific
    named model-behavior regression).

- **Novel**:
  - The "just two more things" tic as a named, specific model-behavior
    failure mode tied to a model version boundary (Opus 4.6 → 4.7) — no
    other corpus source names this specific behavioral pattern.
  - The Fable-design/Opus-implementation/Fable-review lifecycle (Claim 4) as
    an explicit mitigation architecture for exactly this class of
    convergence problem.
  - The "crons watch, models act" architectural rule (Claim 11) as a named
    principle for always-on production agent systems.
  - The quantified Max-account multiplexing economics (Claim 5, Concrete
    Artifacts) — no other corpus source gives comparably specific
    token-volume and cost figures for a single practitioner's sustained
    agentic development.
  - The "Wish Factory" issue-only autonomous-implementation pattern
    (Claim 9).

## Guide Impact

- **Chapter 04 (Failure Modes / Model Selection)**: Add the "just two more
  things" tic (Claim 1) as a named example of a convergence/termination
  failure mode specific to a model version, distinct from more commonly
  documented failure modes (hallucination, tool misuse, context loss).
  Recommend that Ch04's failure-diagnosis guidance explicitly list "recent
  model version change" as a first-class hypothesis alongside harness/config
  issues when a previously-working agentic system degrades — currently the
  chapter (per `blog-humanlayer-skill-issue-harness-engineering.md`'s
  citation) leans toward "suspect the harness first," and this source is
  contradicting evidence for that default (see filed contradiction #2625
  and the **Contradicts** entry above) that should be reflected as a
  caveat, not silently adopted or silently ignored.
- **Chapter 04 (Model Selection / Reliability Patterns)**: Add the
  Fable-design/Opus-implementation/Fable-review lifecycle (Claim 4) as a
  concrete example of a cross-model reliability pattern — pairing a
  higher-trust model on both sides (planning and review) of a lower-trust
  model's implementation work — that practitioners have used specifically
  to contain the kind of convergence problems described in Claim 1.
- **Chapter 06 (Orchestration Patterns / CI-CD under Agentic Load)**: Add
  the megabatch/swarm-diagnosis pattern (Claim 7) as an emerging alternative
  to bisecting merge queues once commit volume from agents exceeds what
  serial or batched-bisection CI/CD can absorb, citing both Yegge's own
  data and the independently-sourced "Game DevOps" anecdote from the video
  game industry as light corroboration. Frame as emerging, not settled —
  single practitioner, no controlled comparison.
  Also add the "crons watch, models act" principle (Claim 11) as a cost/
  design pattern for always-on production agent deployments: use
  deterministic scheduled jobs for continuous monitoring, reserve model
  invocation for judgment calls.
- **Chapter 03 (Harness & Loop Engineering)**: Add Claim 2 (harnesses as
  bespoke, application-embedded components rather than portable frameworks)
  as a strong practitioner opinion to sit alongside the more measured
  "industry is shifting toward harness-centric engineering" framing already
  present via `blog-latentspace-aiewf26-trends-synthesis.md`. Do not present
  Yegge's "give up on reusable harnesses" claim as settled guide advice —
  it is one practitioner's generalization from a single failed project,
  though a highly-informed one.
- **Chapter 05 (Team Adoption / Economics)**: The token-economics figures
  (Claim 5, Concrete Artifacts) are a useful concrete data point for any
  section discussing the cost structure of sustained high-volume agentic
  development and the Max-plan-vs-API-pricing arbitrage some practitioners
  are using — flag as anecdotal and specific to solo/individual usage, with
  Yegge's own caveat that this approach is likely non-compliant for
  multi-person companies.

## Extraction Notes

- Followed the outbound link from Willison's short link-blog post to
  Yegge's full essay (`yegge.ai/essays/the-shape-of-things-to-come/`), which
  is where nearly all of the extractable claims and artifacts in this note
  come from — the Willison post itself is a single paragraph. Also read
  `yegge.ai/gastown.html` for background on what Gas Town is and its
  release history, used only in Source Context and Failure Report Detail
  above, not as a separate claims source.
- The essay is explicitly Part 1 of a two-part series; Part 2 ("Model
  Welfare for Agentic Engineers") is referenced but not linked as available
  content at the time of this extraction and was not read. Claim 10 flags
  where that follow-up would be relevant if mined later.
- The essay covers substantially more ground than is extracted here
  (Wyvern's specific prod-role agents in full, a detailed "yelled at Fable"
  CI/CD anecdote, a long project-knowledge-organization discussion, and
  more) — this note prioritized claims relevant to the Prospector's flagged
  chapters (model capabilities/limitations, failure modes, harness/loop
  engineering, orchestration/reliability patterns) per MINER.md §5 rather
  than exhaustively cataloguing the entire essay.
- Verified all quotes against a raw-HTML-to-text extraction of both pages
  (not just the AI-summarized WebFetch output) before writing this note, per
  MINER.md §2a, to guard against paraphrase drift.
- Filed contradiction issue #2625 per MINER.md §4a for the tension between
  this source's Claim 1 and `blog-humanlayer-skill-issue-harness-engineering.md`
  Claim 1 (see **Contradicts** above). Did not pick a verdict in this note.
