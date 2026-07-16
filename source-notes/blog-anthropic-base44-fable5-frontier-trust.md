---
source_url: https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work
source_type: blog-post
title: "Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work"
author: Anthropic (case study featuring Yoav Orlev, Head of Product, Base44)
date_published: 2026-07-15
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: anecdotal
issue: "#1918"
---

# Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work

> Anthropic case study, built around quotes from Base44's Head of Product Yoav
> Orlev, arguing that Claude Fable 5 is the first model Base44 has trusted
> with platform-core work previously reserved for its most senior engineers
> (a system-prompt rebuild and native-mobile infrastructure) — evidenced by
> self-reported completion percentages/timings for two specific tasks and a
> named failure mode of prior models ("naive" next-step decisions, getting
> stuck instead of searching the codebase for an existing fix) that Fable 5
> avoids.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, claude.com, published
  2026-07-15; part of the "Working at the frontier" corporate case-study
  series; no individual Anthropic byline; ~5 min read per the post's own
  reading-time label)
- **Author credibility**: Published by Anthropic on claude.com — marketing
  framing, hosted to position Claude Fable 5 favorably — but the substantive
  claims are attributed throughout to Yoav Orlev, Head of Product at Base44,
  described as the company's first employee. Base44 is characterized as "a
  vibe-coding platform that allows anyone, regardless of technical ability,
  to build full stack applications and websites," with customers "from small
  businesses with no developers to companies using it to build full SaaS
  products." Orlev's team has "build[t] on every Claude model since Sonnet
  4," giving him direct, comparative exposure to prior Claude generations in
  the same production harness (Base44's app-generation engine, live since
  early 2025). No independent/non-Anthropic-hosted account of these claims
  exists in this source; treat as a single-practitioner account amplified by
  a vendor channel. No code, eval methodology detail, screenshots, or
  third-party verification is included.
- **Scope**: Covers Base44's model-evaluation practice (app-type evals,
  latency/cost/build-error measurement, a Minecraft-clone stress test), a
  named prior-model failure mode ("naive" next-step reasoning, not searching
  the codebase for existing fixes), two specific Fable-5-delegated tasks
  (system-prompt rebuild; native mobile infrastructure) with self-reported
  completion percentages and elapsed time, a self-correcting eval gap Fable 5
  surfaced during the system-prompt task, a senior-vs-junior-engineer framing
  of what delegation to Fable 5 now requires, and a forward-looking claim
  about product managers/designers now building in previously off-limits
  areas. Does NOT cover: Base44's eval methodology in detail (no task counts,
  scoring rubric, or pass/fail thresholds disclosed), exact prior-model
  version(s) behind "earlier Claude models" (unspecified beyond "since Sonnet
  4"), pricing/token cost for either delegated task, headcount or team size,
  or any data beyond the two named task anecdotes (no aggregate/fleet-wide
  before/after metrics).

## Extracted Claims

### Claim 1: Base44 restricted any platform-core changes touching multiple interdependent parts — specifically a hundreds-of-permutations system prompt and native mobile infrastructure — to its most senior engineers, because earlier models could not be trusted with that work
- **Evidence**: Source narration (not a direct Orlev quote) establishing the
  organizational bottleneck the rest of the post argues Fable 5 removed.
- **Confidence**: anecdotal (single company's internal policy, no
  quantification of how many changes were gated this way or over what
  period)
- **Quote**: "But any changes to the platform's core that touch multiple
  interdependent parts could only be entrusted to the most senior
  engineers." / "One such bottleneck was Base44's system prompt and its
  hundreds of permutations, which vary by whether someone is on their first
  app or their fifth, a free user or a subscriber, and by the category and
  features of the app being built. Another was changing the native mobile
  infrastructure, which only engineers with mobile expertise could do."
- **Our assessment**: This is the load-bearing baseline for the rest of the
  post's "senior-engineer-gated work" claims (Claims 4, 8) — it names two
  concrete, non-trivial classes of work (a permutation-heavy system prompt,
  native mobile infra) rather than a vague "hard problems," which makes the
  before/after comparison in Claims 4 and 8 more specific than most
  vendor-hosted step-change narratives in this corpus.

### Claim 2: Earlier Claude models, when stuck on an error, kept working the same spot instead of recognizing that a fix probably already existed elsewhere in the codebase and searching for it — a pattern Orlev calls "a naive approach"
- **Evidence**: Source narration of the failure mode plus a direct Orlev
  quote characterizing it.
- **Confidence**: anecdotal (single practitioner's characterization, no
  named prior model version, no incident count)
- **Quote**: "When a model got stuck on an error, for example, it would keep
  working the spot in front of it instead of recognizing the fix probably
  already existed elsewhere in the code and searching for it." / "The
  decision on what to do next is a crucial one and most of the time [earlier]
  models would take, I would say, a naive approach," he says.
- **Our assessment**: "Naive" next-step decision-making is a sharper,
  process-level failure description than a generic "earlier models made
  mistakes" claim — it locates the failure specifically in *where to look
  next* rather than in code-generation quality itself, which is a distinct
  claim from most step-change narratives in this corpus that focus on raw
  output correctness.

### Claim 3: Claude Fable 5 was the first model Base44's team tested that could reason as if it had an understanding of how software is built
- **Evidence**: Direct attribution to Orlev, stated as the post's central
  thesis sentence bridging the "earlier models" section to the results
  section.
- **Confidence**: anecdotal (single practitioner's subjective assessment, no
  criteria given for what "understanding of how software is built" means
  operationally)
- **Quote**: "Claude Fable 5 was the first model the team tested that could
  reason as if it had an understanding of how software is built, Orlev
  says."
- **Our assessment**: This is the post's headline claim and the most likely
  to be over-cited if lifted out of context — it is a summary judgment, not
  itself evidence; the specific behavioral claims that back it up are
  Claims 6, 7, and 9 below, and the guide should cite those rather than this
  summary sentence alone.

### Claim 4: Base44 evaluates each new Claude model with app-type-specific evals measuring latency, cost, and build errors, plus a stress test that has the model build a Minecraft clone to assess game-physics/mechanics handling
- **Evidence**: Source narration describing Base44's internal model-
  evaluation practice, presented as an established process rather than a
  one-off for Fable 5.
- **Confidence**: anecdotal (no task counts, scoring thresholds, or
  pass/fail criteria disclosed; "Minecraft clone" described only as a
  concept, not a scored benchmark)
- **Quote**: "Base44 runs each new Claude model through evals across
  different app types, measuring latency, cost, and build errors. The team
  also runs tests like building a Minecraft clone to see how a model handles
  game physics and mechanics."
- **Our assessment**: This is one of the few concrete, transferable eval-
  design details in the post — "build a Minecraft clone" as a proxy task for
  stress-testing physics/mechanics handling is a specific, reusable idea for
  practitioners designing their own model-selection evals, distinct from the
  generic "we run evals" claims common elsewhere in this corpus. No
  methodology (sample size, scoring rubric, how "build errors" is counted)
  is disclosed, so it should be cited as a practice example, not a
  reproducible benchmark.

### Claim 5: With Claude Fable 5, Base44 observed two things stand out relative to prior models: tasks finished in far fewer turns, and apps were more complete from the first prompt, including edge cases earlier models skipped
- **Evidence**: Source narration summarizing the eval/dogfooding outcome
  that motivated delegating senior-engineer-only work to Fable 5.
- **Confidence**: anecdotal (qualitative "far fewer turns" and "more
  complete," no turn counts, no completeness metric, no sample size)
- **Quote**: "With Claude Fable 5, two things stood out: it finished tasks
  in far fewer turns, and it built more complete apps from the first prompt,
  including the edge cases that earlier models skipped."
- **Our assessment**: This is the direct causal bridge between the eval
  practice (Claim 4) and the decision to delegate the system-prompt and
  mobile-infra tasks (Claims 6, 8) — but it is stated as a qualitative
  before/after impression from the evals, not as a quantified eval result,
  so the guide should not cite "far fewer turns" as a measured multiplier.

### Claim 6: Tasked with rebuilding Base44's system prompt — after about an hour of back-and-forth questions, Claude Fable 5 ran autonomously for four hours and returned 90-95% of what the team needed, which they measured via A/B testing infrastructure and shipped the same afternoon
- **Evidence**: Source narration with specific elapsed-time figures (1hr
  dialogue + 4hr autonomous run) and a specific completion-percentage range
  (90-95%), plus a named verification mechanism (A/B testing infrastructure)
  and shipping timeline (same afternoon).
- **Confidence**: emerging (specific, dated figures for a single named task,
  from a credible source with direct comparative model exposure, but no
  reproduction count, no definition of how "90% to 95% of what they needed"
  was measured beyond "using its A/B testing infrastructure," and no
  independent verification)
- **Quote**: "So the team pointed it at a task they had previously reserved
  only for the most senior engineers: rebuilding the Base44 system prompt.
  After about an hour of back-and-forth questions, Claude Fable 5 ran on its
  own for four hours and returned 90% to 95% of what they needed. Using its
  A/B testing infrastructure, the team was then able to measure and ship
  these changes that afternoon."
- **Our assessment**: This is the post's most concrete, quantified single-
  task result — a specific task (system-prompt rebuild), specific timings
  (1hr + 4hr), a specific completion range (90-95%), and a specific
  verification path (A/B test infra) that shipped same-day. It should be
  cited as an existence proof of a senior-engineer-gated task being
  substantially completed autonomously within a single working day, not as
  a claim that 4-hour autonomous sessions reliably produce 90%+-complete
  results — this is one anecdote for one task type at one company.

### Claim 7: While working on the system-prompt task, Claude Fable 5 flagged a gap in Base44's own eval suite — that it wasn't testing for cache hits even though a prompt change can break the cache and drive up cost at millions-of-users scale — and corrected the blind spot
- **Evidence**: Source narration describing a specific self-identified gap
  during task execution, distinct from the task's primary deliverable.
- **Confidence**: anecdotal (single incident, no detail on how the model
  surfaced the gap or what "corrected it" involved concretely)
- **Quote**: "And while Claude Fable 5 worked, it even flagged a gap in
  Base44's own evals: the team wasn't testing for cache hits, even though a
  prompt change can break the cache, and at the scale of millions of users
  that drives up cost. The model raised a blind spot and corrected it."
- **Our assessment**: This is a distinct claim from the task-completion
  claim (Claim 6) — it describes the model proactively identifying a gap in
  the *evaluation infrastructure itself* (not just the deliverable), a
  meta-level catch (testing-the-tests) that is more specific than a generic
  "the model caught an edge case" claim. Cost-at-scale reasoning (cache
  hits, millions of users) tied to a specific mechanism (prompt changes
  breaking cache) is a concrete, transferable example of what "understanding
  how software is built" (Claim 3) cashes out to in practice.

### Claim 8: When Claude Fable 5 got stuck on a change to the harness behind Base44's in-app agent, it reasoned the same problem had probably been solved elsewhere in the codebase, investigated that part, and returned with the fix — a pattern Orlev says he hasn't seen as often in other models
- **Evidence**: Source narration of a specific incident plus a direct Orlev
  quote characterizing the reasoning pattern as distinctive.
- **Confidence**: anecdotal (single named incident, no reproduction count,
  no detail on what the harness change or the eventual fix was)
- **Quote**: "When Claude Fable 5 got stuck on a change to the harness
  behind Base44's in-app agent, it reasoned that the same problem had
  probably been solved elsewhere in the codebase, went to investigate that
  part, and came back with the fix." / "This reasoning of 'this probably has
  been solved somewhere else, so I should go there to investigate' is
  something we haven't seen so often in other models," Orlev says.
- **Our assessment**: This is the direct, positive-case mirror of the
  "naive approach" failure mode named in Claim 2 (earlier models kept
  working the same stuck spot instead of searching elsewhere) — the same
  behavioral axis (where to look next when stuck) described as a named
  weakness for earlier models and a named strength for Fable 5, which gives
  the pairing more internal consistency than an isolated praise-quote would
  have. The direct quote is the most citable single sentence in the post for
  a guide chapter on agent codebase-navigation/search behavior.

### Claim 9: Orlev frames working with Claude Fable 5 as comparable to working with a senior engineer — a junior engineer needs every step specified and constant checking, while a senior one only needs the goal and the why
- **Evidence**: Source narration paraphrasing Orlev's stated comparison; not
  presented inside quotation marks as his verbatim words.
- **Confidence**: anecdotal (subjective practitioner comparison, no
  operational definition of "senior" vs. "junior" engineer delegation style)
- **Quote**: "Orlev compares working with Claude Fable 5 to working with a
  senior engineer. While a junior engineer needs every step specified and
  constant checking, you only need to brief a senior one on the goal and the
  why."
- **Our assessment**: This is reported narration, not a direct quote — the
  sentence does not appear inside quotation marks in the source, so it
  should be attributed as the article's paraphrase of Orlev's view rather
  than his verbatim words if cited. The specific "goal and the why" framing
  (vs. step-by-step instruction) is a concrete, transferable delegation
  heuristic distinct from the more general "trust the model more" framing
  common elsewhere in this corpus.

### Claim 10: A Base44 product manager (not an engineer) used Claude Fable 5 to bring native mobile app building into the platform, producing a working environment about 90% of what was needed for production after roughly two and a half hours
- **Evidence**: Source narration of a second, distinct delegated task, with
  a specific elapsed-time figure (2.5 hours) and completion percentage
  (~90%), and explicit attribution to a non-engineer role (product manager).
- **Confidence**: anecdotal (single task, single practitioner role, no
  detail on what the remaining ~10% consisted of or how "90%" was assessed)
- **Quote**: "This type of work extends beyond the engineering team, too.
  When a product manager wanted to bring native mobile app building inside
  Base44, he pointed Claude Fable 5 at the job and after roughly two and a
  half hours had a working environment that was about 90% of what the team
  needed to move to production."
- **Our assessment**: This is a distinct, arguably higher-signal claim than
  Claim 6 — it is not an engineer delegating engineering work to Fable 5,
  but a product manager independently producing infrastructure-level work
  (native mobile build environment) that the post explicitly says had
  previously required Base44's "top three engineers or a specialist"
  (Claim 11). This is a concrete instance of role-boundary shift (non-
  engineer producing infra-adjacent output), not just task-completion speed.

### Claim 11: Before Claude Fable 5, native-mobile-infrastructure work had to wait for Base44's top three engineers or a specialist to free up; now the model executes the task while Orlev's team reviews, tests, and approves the code before shipping
- **Evidence**: Source narration contrasting the prior resourcing
  bottleneck with the current review-gated workflow.
- **Confidence**: anecdotal (no data on how often this bottleneck actually
  blocked work previously, or on review/reject rates for Fable-5-produced
  code post-change)
- **Quote**: "Before Claude Fable 5, this type of work had to wait for
  Base44's top three engineers or a specialist to free up. Now, the model
  executes tasks while Orlev's team reviews, tests, and approves the code
  before shipping it."
- **Our assessment**: Important for guide accuracy: the post explicitly
  preserves a human review/test/approve gate before shipping — this is not
  a claim of unsupervised production deployment. The guide should cite this
  as "delegation of execution with retained human review," not as evidence
  that Fable 5 output ships without human sign-off.

### Claim 12: Having seen Fable 5 handle complex delegated tasks, Orlev now encourages Base44 product managers and designers to build in parts of the platform they were previously unwilling to touch for fear of breaking something, framing this as increased confidence to "make bolder moves with the business"
- **Evidence**: Source narration plus a direct closing Orlev quote.
- **Confidence**: anecdotal (single practitioner's stated intent/policy
  going forward, not a measured behavior change yet — framed as what Orlev
  "now encourages," not what has already happened at scale)
- **Quote**: "Knowing that they can trust Fable 5 with complex tasks, Orlev
  now encourages product managers and designers to build in parts of the
  platform they were previously not willing to touch for fear of breaking
  anything." / "Fable has given us the confidence to make bolder moves with
  the business," Orlev says. "It's bringing the product to a whole new area
  and possibilities that before that we were, I would say, scared to do."
- **Our assessment**: This is a forward-looking organizational-behavior
  claim (widened scope of who is "allowed" to touch core platform surfaces)
  building on the two concrete anecdotes (Claims 6, 10) rather than a third
  measured instance — it should be cited as Orlev's stated go-forward
  policy/attitude, not as evidence that a broadened set of non-engineers has
  already shipped platform-core changes at volume.

## Concrete Artifacts

No code, config, prompt text, benchmark methodology, or terminal transcripts
are included in this source — it is a prose case study with no reproduced
technical artifacts. The two quantitative task anecdotes (system-prompt
rebuild: 1hr + 4hr, 90-95%; native mobile infra: 2.5hr, ~90%) are captured
above as Claims 6 and 10 rather than as a separable data table, since no
additional numeric detail (cost, token counts, task breakdown) is given in
the source beyond what is quoted in those claims.

```
Base44 model-evaluation practice, as described in the source
(claude.com/blog, 2026-07-15):

- App-type-specific evals measuring: latency, cost, build errors
- Stress test: "build a Minecraft clone" — assesses handling of game
  physics and mechanics
- No task counts, scoring rubric, or pass/fail thresholds disclosed
```

## Cross-References

- **Corroborates**: `blog-anthropic-cognition-fable5-frontier-trust.md`
  Claim 4 (Cognition: "Give an earlier model five ideas to weigh at once,
  and it would lose track and get confused. On one database migration, a
  prior Opus model technically finished the job but introduced a series of
  subtle bugs along the way") and Claim 5 (Cognition: earlier models "stayed
  at the surface of the logs instead of digging for the relevant line" and
  were "trained to give an answer no matter what"). This source's Claim 2
  (earlier models take "a naive approach" to what-to-do-next decisions,
  getting stuck instead of searching for existing fixes) describes the same
  general category of failure — earlier models handling complex,
  multi-step, or ambiguous situations shallowly — from an independent
  company and practitioner, strengthening the case that this is a
  cross-practitioner-observed characteristic of pre-Fable-5 models rather
  than a single anecdote. This source's Claim 8 (Fable 5 reasoning that a
  stuck problem had "probably been solved elsewhere in the codebase" and
  investigating) is a direct positive-case parallel to Cognition's Claim 9
  (Fable 5 "properly us[ing] Cognition's internal debugging tools" and
  "stat[ing] the invariants it would hold itself to" on a migration that had
  tripped up earlier models) — both describe Fable 5 replacing a shallow/
  stuck failure mode with active investigation of available context before
  acting, in two unrelated production harnesses (Base44's app-generation
  engine vs. Cognition's Devin).
- **Corroborates**: `blog-anthropic-fable-finding-unknowns.md` Claim 11
  (Thariq Shihipar: "Claude Fable is the first model where I find the
  quality of the work is bottlenecked by my ability to clarify its
  unknowns"). This source's Claim 9 (a senior engineer, unlike a junior one,
  only needs to be briefed on "the goal and the why," not given step-by-step
  instruction) describes the same shift from a different angle: both sources
  independently frame Fable 5 as requiring less procedural hand-holding and
  more upfront goal/context-setting from the human, with the practitioner's
  own framing effort (not the model's raw capability) becoming the binding
  constraint.
- **Contradicts**: None identified as a direct, same-claim conflict.
- **Extends**: `blog-anthropic-code-w-claude-london-2026.md` Claim 5 (which
  names Base44 as a customer session presenter at Code w/ Claude London
  2026 but states explicitly that "no session content details are provided
  in the blog post"). This source is the first deep-dive extraction of what
  Base44 actually does with Claude — the system-prompt rebuild, native
  mobile infrastructure delegation, and the app-type/Minecraft-clone eval
  practice were all previously undocumented in this corpus. Also loosely
  extends `blog-thoughtworks-anand-agent-evaluation-framework.md` (a
  three-layer conversational-agent evaluation architecture) — this source's
  Claim 4 (app-type evals plus a Minecraft-clone stress test) describes a
  different evaluation layer (pre-adoption model-selection evals for a
  code-generation product, not production conversational-agent evals) but
  is additional evidence, from a different domain, that practitioners are
  building bespoke, task-specific eval suites rather than relying on
  general-purpose benchmarks alone.
- **Novel**: The "reasoned that the same problem had probably been solved
  elsewhere in the codebase, went to investigate that part, and came back
  with the fix" pattern (Claim 8) is new to this corpus as a named, specific
  agent behavior (a targeted search grep across existing source notes for
  "elsewhere in the codebase," "search the codebase," "already solved," and
  "existing solution" found no prior match). The app-type-evals-plus-
  Minecraft-clone-stress-test eval design (Claim 4) is also new — no
  existing source note documents a game-physics stress test as a model-
  selection eval technique. The cache-hit eval gap Fable 5 self-identified
  (Claim 7) is a novel, concrete instance of a model catching a hole in its
  own evaluation infrastructure (not just a code-level edge case) that is
  not documented elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 04 (context-engineering)**:
  Add Claim 8 (Fable 5 investigating existing code elsewhere in the
  codebase when stuck, rather than repeating the same failed approach) as a
  named, practitioner-validated example of productive codebase-search
  behavior, paired with Claim 2's contrasting failure mode (earlier models'
  "naive approach" of continuing to work the same stuck spot). Currently
  the guide lacks a concrete before/after example of this specific
  reasoning pattern; this source names it precisely enough to quote.
- **Chapter 04 (Model Evaluation and Scaling)**: Add Claim 4 (app-type evals
  measuring latency/cost/build-errors, plus a Minecraft-clone stress test
  for game-physics handling) as a concrete example of a bespoke,
  product-specific model-selection eval suite, distinct from general-purpose
  benchmarks. Flag explicitly that no methodology (task counts, scoring
  rubric, thresholds) is disclosed — cite as a design-pattern example, not
  a reproducible benchmark.
- **Chapter 05 (Team Adoption)**: Add Claim 10 (a product manager, not an
  engineer, independently produced a near-production-ready native-mobile
  build environment in ~2.5 hours) and Claim 12 (Orlev now encourages PMs
  and designers to build in previously off-limits platform areas) as a
  concrete instance of AI-driven role-boundary widening — who is trusted to
  touch platform-core surfaces — alongside the existing corpus theme of
  senior-engineer-gatekept work being reassigned. Pair with Claim 11's
  caveat that human review/test/approve remains in the loop before shipping,
  so the guide does not overstate this as unsupervised delegation.
- **Chapter 01 (Why Now / Motivation for agents)**: Claim 3 (Fable 5 as
  "the first model...that could reason as if it had an understanding of how
  software is built") is a strong pull-quote for framing why this model
  generation specifically unlocked delegation of previously senior-only
  work, but should be paired with the specific behavioral evidence (Claims 2,
  6-9) rather than cited standalone, since it is itself a summary judgment.

## Extraction Notes

- WebFetch's summarization pass on this URL returned only a short, lossy
  summary despite an explicit verbatim-extraction prompt (the underlying
  fetch tool appears to run the page through a small summarizing model
  regardless of prompt wording). To get the actual article text, the page
  was fetched directly via `curl` with a browser user agent, and the article
  body was located and extracted from the raw HTML (a Webflow-hosted static
  page) using a Python script that stripped tags and HTML entities. The
  extracted text was cross-checked paragraph-by-paragraph against the raw
  HTML source (including verifying the "Sugeragents" vs. "Superagents"
  discrepancy noted below) rather than relied on as a single-pass summary.
- The source contains one internal typo: one sentence reads "...confidence
  to build more ambitious parts of their **Sugeragents** platform" while a
  later sentence in the same article correctly reads "Base44 **Superagents**,
  now public, run workflows around those apps." Both spellings were verified
  directly against the raw HTML (not a rendering artifact of extraction).
  Where this note quotes the mis-spelled sentence, it is reproduced exactly
  as it appears in the source per MINER.md's verbatim-quoting rule; the
  correct product name is "Superagents," confirmed by the second usage.
- The article is short (~5 min read per its own label, two named sections:
  "Trusting Fable 5 with the most complex product and engineering jobs" and
  "What's next"). No outbound links or sub-pages were present in the fetched
  article body that warranted following — it is a single-page case study
  with no linked footnotes, benchmark methodology page, or related-post
  links surfaced in the raw HTML.
- No numbered claim in any other source note was cited by number in this
  note without first re-reading that note to confirm the claim's number and
  content: `blog-anthropic-cognition-fable5-frontier-trust.md` Claims 4, 5,
  8, 9 and `blog-anthropic-fable-finding-unknowns.md` Claim 11 were each
  re-read before citation. `blog-anthropic-code-w-claude-london-2026.md`
  Claim 5 and `blog-thoughtworks-anand-agent-evaluation-framework.md` were
  cited by claim number / by note-level description respectively, both
  after re-reading.
- No contradiction meeting MINER.md §4a's filing bar was identified. This
  source's task-completion figures (90-95%, ~90%) are self-reported,
  single-anecdote, and not directly comparable to any existing source note's
  quantified claims (different tasks, different companies, no shared
  methodology) — a difference in scope/context, not a same-conditions
  conflict. No contradiction issue filed.
- Confidence is set to `anecdotal` overall: unlike
  `blog-anthropic-cognition-fable5-frontier-trust.md` (which contains one
  `emerging`-graded claim — a named internal benchmark with a specific
  before/after score comparison across model generations), this source's
  most quantified claims (Claims 6, 10) are self-reported completion
  percentages for two one-off tasks with no comparable benchmark, no
  reproduction count, and no disclosed measurement methodology beyond "using
  its A/B testing infrastructure." Claim 6 is individually graded `emerging`
  given its specificity (named task, named timings, named verification
  mechanism), but it alone does not raise the source's overall grade above
  `anecdotal`.
