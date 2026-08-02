---
source_url: https://cognition.com/blog/making-fable-cheaper-than-opus
source_type: blog-post
title: "Making Fable Cheaper Than Opus"
author: Joon Hee Lee (Cognition)
date_published: 2026-07-13
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2430"
---

# Making Fable Cheaper Than Opus

> Cognition parses every LLM call across 3,000 FrontierCode 1.1 evaluation
> sessions to show that, in their Devin Fusion lead+sidekick harness, Fable 5
> costs less per run than Opus 4.8 ($1.86 vs $2.04) and scores higher (60.7
> vs 54.6) despite costing 2x more per token — because Fable delegates early
> with tightly-specified briefs and rarely touches code itself (81% of runs),
> while Opus explores expensively before delegating late and then
> re-does much of the sidekick's work at lead prices.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, byline "Joon Hee
  Lee," published "07.13.26" per the page's own byline format — the same
  MM.DD.YY convention used across this corpus's other Cognition posts, e.g.
  `blog-cognition-devin-fusion.md`'s "06.29.26"). Joon Hee Lee also appears
  in the "FrontierCode 1.1" methodology post's byline
  (`blog-cognition-frontiercode.md` Source Context), so this is a named
  research-team author with direct involvement in the benchmark this post
  uses, not an anonymous corporate byline.
- **Author credibility**: First-party vendor content from Cognition, the
  company that builds and sells Devin, and a direct technical follow-up to
  Cognition's own "Devin Fusion" product launch
  (`blog-cognition-devin-fusion.md`) — this post explicitly frames itself as
  building on that launch: "When we introduced Devin Fusion, we showed a way
  out: keep a frontier model in charge, let it delegate to a cheaper and
  faster sidekick, and you get frontier-level performance at 35% lower
  cost." Cognition has a direct commercial interest in Fable 5 (Anthropic's
  model) appearing cost-effective inside its own Fusion harness, though the
  post also discloses a negative case (a task category where delegation
  "fails," see Claim 9) rather than reporting only favorable results. The
  evidence base is described as "we parsed every LLM call across all 3,000
  sessions" from FrontierCode 1.1 (Cognition's own benchmark, see
  `blog-cognition-frontiercode.md`), plus three named worked task examples
  with before/after detail. No independent (non-Cognition) verification of
  these figures was found.
- **Scope**: Covers a run-level and per-turn cost/quality comparison between
  Fable-5-led and Opus-4.8-led Fusion configurations paired with "the same
  cheap sidekick," a breakdown of where each lead's dollars go (its own
  turns vs. the sidekick's), the qualitative "manager vs. micromanager"
  behavioral difference driving that cost split, three worked task examples
  (an OIDC SSO exploration task, a hashing task with an O(1) constraint, and
  a changeset-migration over-engineering example), post-handoff review
  behavior (how often each lead re-pulls the sidekick's files into its own
  context and re-edits them), and an explicit disclosed failure mode for the
  delegation strategy (short/serial-debugging tasks). Does **not** cover:
  the sidekick model's identity (never named — only "a much cheaper model" /
  "the same cheap sidekick"), the definition of a "turn," the score's units
  (no percentage sign or "out of 100" denominator is given for the 60.7/54.6
  figures), sample sizes for the specific examples beyond the aggregate
  3,000-session count, or any comparison to Fusion configurations that don't
  involve Fable 5 or Opus 4.8 as the lead.

## Extracted Claims

### Claim 1: Despite Fable 5 costing roughly 2x more per token than Opus 4.8, Fable 5 paired with a cheaper sidekick in Cognition's Fusion harness costs less per run than Opus 4.8 paired with the same sidekick, while scoring higher on FrontierCode 1.1
- **Evidence**: Headline finding stated in the post's introduction, with the
  underlying per-token price gap named explicitly as the counterintuitive
  premise the rest of the post explains.
- **Confidence**: emerging (specific, quantified, first-party comparison on
  Cognition's own benchmark and harness; no independent replication)
- **Quote**: "Fable 5 costs 2x more per token than Opus 4.8, so a Fable-led agent should cost more."
- **Quote (headline result)**: "Fable + Sidekick costs less than Opus + Sidekick ($1.86 vs. $2.04), while scoring higher (60.7 vs 54.6)."
- **Our assessment**: This is a specific, falsifiable, counterintuitive claim
  — the kind of result worth flagging prominently in a guide chapter on
  model-selection economics, since it directly contradicts a naive
  "cheaper-per-token model = cheaper system" heuristic. The claim is scoped
  narrowly (Cognition's own Fusion harness, FrontierCode 1.1, one specific
  sidekick pairing) and should not be generalized to "Fable 5 is always
  cheaper than Opus 4.8" outside a delegation architecture — the post's own
  framing is that the *architecture* (who delegates, when, and how) is the
  primary cost driver, not the per-token price alone.

### Claim 2: The cost gap is driven by allocation, not just total spend — Fable spends more on its sidekick but far less on itself, while Opus spends more on itself and less on its sidekick, even though Fable's per-token rate is higher throughout
- **Evidence**: A stated cost breakdown splitting each run's total into lead
  spend and sidekick spend.
- **Confidence**: emerging (specific first-party dollar breakdown, same
  evidentiary basis as Claim 1)
- **Quote**: "Fable + Sidekick": lead cost and sidekick cost sum to "$1.86 vs. $2.04" per the headline figure (exact per-component dollar quote not directly captured in this extraction; component figures $1.28 lead + $0.58 sidekick for Fable, $1.73 lead + $0.31 sidekick for Opus, were confirmed via a structured cost-breakdown table in the post, not a prose sentence — see Concrete Artifacts)
- **Our assessment**: This is the mechanistic core of Claim 1 — it shows the
  cost win isn't simply "Fable is cheaper," it's that Fable's *lead* spend
  drops enough (by delegating more successfully) to more than offset both
  Fable's higher per-token rate and its higher sidekick spend. This is a
  transferable diagnostic for any team evaluating a lead+sidekick harness:
  look at the lead/sidekick cost split, not just the aggregate run cost, to
  understand whether a cost improvement comes from cheaper delegation or
  from the lead simply doing less total work.

### Claim 3: Fable's lead takes far fewer turns and processes far less cumulative context per run than Opus's lead — 11.5 turns and 545k input tokens versus 26.5 turns and 1,679k input tokens
- **Evidence**: A stated per-run turn count and input-token figure for each
  configuration, framed as the mechanical explanation for Claim 2's cost
  split.
- **Confidence**: emerging (specific, first-party quantified metric from the
  same 3,000-session analysis)
- **Quote**: "Fable's lead takes 11.5 turns per run to Opus's 26.5"
- **Our assessment**: A ~2.3x turn-count gap and a ~3.1x input-token gap
  (545k vs. 1,679k) is a large, specific, and falsifiable difference — it
  gives a concrete mechanism (fewer turns, less re-read context) for why
  Fable's lead spend is lower despite its higher per-token rate. This
  corroborates and quantifies `blog-cognition-devin-fusion.md` Claim 2's
  more general design rule that "the main agent should take minimal
  actions, and only read what is absolutely necessary" — this post supplies
  the first per-run turn/token measurement in this corpus showing one
  frontier model (Fable 5) actually following that design rule
  substantially more than another (Opus 4.8) inside the identical harness.

### Claim 4: The post frames the behavioral difference as "a manager with a capable engineer" (Fable) versus "a micromanager with an intern" (Opus) — Fable delegates early with a detailed brief, while Opus performs extensive solo exploration, design, and implementation (20-45 turns) before delegating late
- **Evidence**: A direct analogy statement plus a quantified range for
  Opus's pre-delegation solo-work turn count.
- **Confidence**: emerging (a named, specific behavioral pattern with a
  quantified range, drawn from the same 3,000-session trajectory analysis)
- **Quote**: "Opus behaves like a micromanager with an intern; Fable is a manager with a capable engineer"
- **Quote (Opus's solo-exploration range)**: "A typical Opus-led run goes through 20–45 turns of solo exploration, design, and implementation."
- **Our assessment**: This is the post's central qualitative finding and the
  one most useful for a guide chapter on delegation design: the cost
  advantage isn't just "delegate more," it's "delegate *earlier*, before
  paying for exploration and design work the sidekick could have absorbed
  as part of a well-specified brief." A team building a similar harness
  should treat "how many turns before the first delegation" as a concrete,
  measurable lever distinct from "how often does the lead delegate at all"
  (see Claim 8, where both leads delegate about equally often).

### Claim 5: In 81% of Fable-led runs, the lead model never makes a single code edit itself, versus only 24% of Opus-led runs
- **Evidence**: A specific aggregate percentage comparison from the
  3,000-session trajectory analysis.
- **Confidence**: emerging (specific, quantified, first-party comparative
  statistic)
- **Quote**: "in 81% of Fable-led runs, the lead never makes a single code edit"
- **Our assessment**: This is the single most citable statistic in the post
  for a guide chapter on delegation architecture — it operationalizes
  "delegates effectively" as a concrete, measurable behavior (does the lead
  ever touch code at all) rather than a vague qualitative impression. Read
  alongside Claim 8 (both leads delegate ~3 times per run), the 81%-vs-24%
  gap shows the difference is not delegation *frequency* but whether the
  lead's own edits, on top of delegated work, are needed at all — Opus
  apparently uses delegation as a supplement to its own editing rather than
  a substitute for it.

### Claim 6: Fable's handoff briefs emphasize constraints, edge cases, and a definition of "done" rather than implementation detail, illustrated by a hashing-task example where Fable's brief specified an O(1) performance constraint the sidekick honored (scoring 94), while Opus's brief omitted the constraint and the sidekick's resulting linear-time implementation scored only 25
- **Evidence**: A direct quote characterizing Fable's handoff style, plus a
  named worked example with a quoted constraint and two scores.
- **Confidence**: emerging (one specific, quantified worked example plus a
  general characterization; a single example illustrating a general claim,
  not a systematic count of how often this pattern occurs across all 3,000
  sessions)
- **Quote (general framing)**: "Fable's handoffs enumerated constraints, edge cases, and a definition of 'done'"
- **Quote (O(1) constraint, from Fable's brief)**: "operator() must be O(1) in pointer length: NO full token scan"
- **Quote (outcome)**: "shipped a linear-time implementation, which scored 25... score of 94"
- **Our assessment**: This is the clearest concrete illustration in the post
  of *what* a good delegation brief looks like versus a bad one — stating a
  hard performance constraint up front (O(1), not "make it fast") is a
  specific, transferable authoring pattern for anyone writing handoff briefs
  to a cheaper sidekick model. The 25-vs-94 score gap on what is otherwise
  the same task is a striking illustration of how much a brief's
  specificity can matter independent of the underlying sidekick's raw
  capability, since both configurations used "the same cheap sidekick."

### Claim 7: An OIDC SSO exploration task illustrates the delegation-timing difference directly — Fable delegated the repo exploration immediately, while Opus re-read files the sidekick had already summarized rather than trusting the summary
- **Evidence**: A named worked example task with a described divergence in
  each lead's handling of the same exploratory sub-task.
- **Confidence**: anecdotal (a single named worked example illustrating the
  general Claim 4 pattern; not a systematic count of how often this
  redundant-re-reading behavior occurs)
- **Quote**: "Explore the repo to map out how OIDC SSO is implemented"
- **Our assessment**: This is a single task-level illustration of the same
  underlying mechanism as Claim 3's aggregate token-count gap (545k vs.
  1,679k input tokens) — Opus's higher token consumption is at least
  partly explained by re-reading context the sidekick had already condensed
  into a summary, rather than treating the sidekick's output as
  trustworthy. This is a specific, transferable failure mode: a lead model
  that doesn't trust its own sidekick's summaries pays for the sidekick's
  work and then pays again to redo the reading itself.

### Claim 8: After the handoff, Opus pulls the sidekick's files back into its own (expensive) context roughly twice as often as Fable does, and makes roughly four times as many corrective edits at lead-model prices; both leads delegate to the sidekick about the same number of times per run (roughly 3 handoffs)
- **Evidence**: A direct quantified comparison of post-handoff review
  behavior, plus a separate statement establishing that delegation
  *frequency* itself is not the differentiator.
- **Confidence**: emerging (specific, quantified, first-party comparative
  statistics from the same trajectory analysis)
- **Quote (post-handoff behavior)**: "Opus...pulls the sidekick's files back into its own context 2x more often and makes 4x more corrective edits at lead prices."
- **Quote (delegation frequency parity)**: "both leads delegate the same number of times, about 3 handoffs per run"
- **Our assessment**: This is the claim that most precisely isolates the
  mechanism behind Claim 1-3's cost gap: since both leads delegate about
  equally often, the difference is entirely in what happens *after* the
  handoff — Opus spends lead-priced tokens re-reviewing and re-editing
  sidekick work it apparently doesn't trust, while Fable is more likely to
  accept the sidekick's output or, per Claim 9's changeset-migration
  example, issue a second cheap handoff rather than fixing it itself at
  lead prices.

### Claim 9: A changeset-migration example is described where both leads identified the same over-engineering problem in the sidekick's diff, but Opus reverted and reimplemented it directly at lead-model prices, while Fable issued a second, cheap handoff back to the sidekick with a more specific instruction to try simpler alternatives in order
- **Evidence**: A named worked example contrasting each lead's remediation
  choice for the same identified problem.
- **Confidence**: anecdotal (a single named worked example; the exact
  prose wording could not be verified verbatim during this extraction — see
  Extraction Notes)
- **Quote**: (no direct quote; see paraphrase above and in Our assessment — the fetched text for this example returned bracketed editorial paraphrase rather than a clean verbatim excerpt, so no quote is asserted here per MINER.md §2a Rule 5)
- **Our assessment**: If accurately characterized, this is a specific
  illustration of Claim 8's "4x more corrective edits at lead prices"
  statistic in action — the choice point is not "does the lead notice the
  problem" (both leads did) but "how does the lead fix it" (re-delegate
  cheaply with a sharper instruction, vs. take it over directly at lead
  cost). Because the exact source wording for this example was not
  independently verified character-for-character, a future note or the
  Assayer should re-verify this specific example against the source before
  it is cited with a direct quote in the guide.

### Claim 10: Fable's delegation strategy is explicitly described as not universally useful — it fails specifically on short tasks and on serial debugging tasks where the root-cause investigation is one long, non-decomposable chain of judgment calls, because those tasks lack delegable components
- **Evidence**: A direct disclosed-limitation statement under a dedicated
  "When delegation doesn't help" section.
- **Confidence**: emerging (a first-party, explicitly disclosed negative
  case, named specifically rather than a generic hedge)
- **Quote**: "Fable's delegation strategy is not universally useful; it fails when the task does not have delegable components"
- **Quote (specific failure category)**: "Serial debugging tasks where the root-cause hunt is one long chain of judgments"
- **Our assessment**: This is a disclosed limitation, not just a marketing
  highlight reel, which strengthens the credibility of the post's other
  claims — Cognition names a specific task shape (short, or a single
  non-decomposable judgment chain) where the entire cost-saving mechanism
  described in Claims 1-8 simply does not apply, rather than implying
  delegation helps universally. A guide citing this post's cost results
  should carry this caveat: the savings are conditional on task
  decomposability, not a property of Fable 5 or the Fusion harness alone.

### Claim 11: The post closes by arguing that as cheaper sidekicks absorb more implementation work, what remains worth frontier-model prices shifts from doing the work to exercising judgment — deciding what to build, what to constrain, and who should do the writing
- **Evidence**: A direct closing statement summarizing the post's overall
  argument.
- **Confidence**: anecdotal (a stated framing/prediction about where
  frontier-model value accrues, not itself a new measured result — it
  synthesizes Claims 1-10 rather than adding new evidence)
- **Quote**: "What will remain worth frontier prices is judgment: what to build, what to constrain, and who should write it"
- **Our assessment**: This closing framing is consistent with — and gives a
  specific, quotable articulation of — the same shift toward
  judgment-over-implementation already argued in
  `blog-cognition-devin-fusion.md` Claim 2 (the frontier lead should "take
  minimal actions" and reserve itself for "the plan, the interpretation of
  ambiguity, the final review"). This post adds the specific evidence (the
  81%-vs-24% code-edit-avoidance gap, the O(1)-constraint example) that the
  earlier, more architectural post did not have, since that post's focus
  was announcing the Fusion harness rather than analyzing a full session
  corpus.

## Concrete Artifacts

### Cost/score/turn comparison table
```
Source: cognition.com/blog/making-fable-cheaper-than-opus, from the
"Cost of an agent" section (WebFetch-assisted extraction; component dollar
figures and token counts were returned as structured summary data, not
verified against raw HTML — see Extraction Notes)

Configuration          Score   Cost/run   Turns   Input tokens
Fable + Sidekick        60.7    $1.86      11.5    545k
Opus + Sidekick         54.6    $2.04      26.5    1,679k

Cost breakdown:
Fable + Sidekick: $1.28 lead + $0.58 sidekick = $1.86
Opus + Sidekick:  $1.73 lead + $0.31 sidekick = $2.04
```

### Worked task examples (from "A micromanager with an intern vs a manager with an engineer")
```
Source: cognition.com/blog/making-fable-cheaper-than-opus

1. OIDC SSO exploration task
   Brief given to sidekick: "Explore the repo to map out how OIDC SSO is
   implemented"
   Fable: delegated the exploration immediately.
   Opus: re-read files the sidekick had already summarized rather than
   trusting the summary (per WebFetch-assisted summary; not independently
   verified verbatim — see Extraction Notes).

2. Hashing task with an O(1) performance constraint
   Fable's brief specified: "operator() must be O(1) in pointer length: NO
   full token scan"
   Opus's brief omitted this constraint.
   Result: sidekick under Opus "shipped a linear-time implementation,
   which scored 25"; sidekick under Fable's constrained brief scored 94.

3. Changeset-migration over-engineering example (see Claim 9 — exact
   wording not independently verified; both leads identified the same
   over-engineering problem in the sidekick's diff, but chose different
   remediations: Opus reportedly reverted and reimplemented directly at
   lead prices, Fable reportedly issued a second, more specific cheap
   handoff back to the sidekick).
```

### Aggregate behavioral statistics
```
Source: cognition.com/blog/making-fable-cheaper-than-opus

- Lead never edits code: Fable 81% of runs, Opus 24% of runs
- Handoffs per run: ~3 for both leads (delegation frequency is not the
  differentiator)
- Opus pulls sidekick's files back into its own context: 2x more often
  than Fable
- Opus makes corrective edits at lead-model prices: 4x more often than
  Fable
- Opus's typical solo pre-delegation exploration: 20-45 turns
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-devin-fusion.md` Claim 2 (the Fusion lead model "should
    take minimal actions, and only read what is absolutely necessary. By
    default it should delegate and monitor, while making the significant
    decisions: the plan, the interpretation of ambiguity, the final
    review"): this post's Claims 3, 4, and 5 supply the first per-session
    quantified measurement in this corpus of one specific frontier model
    (Fable 5) actually following that design rule substantially more than
    another (Opus 4.8) inside the identical harness — turning that
    earlier post's general architectural prescription into a measured,
    model-specific behavioral gap (11.5 vs. 26.5 turns; 81% vs. 24%
    code-edit avoidance).
  - `blog-cognition-multi-agents-working.md` Claim 9 (Smart Friend's named
    failure mode: an under-informed consulted model defaults to fabricating
    an answer rather than requesting more information, and the mitigation
    of sharing full context and giving specific instructions rather than
    vague ones) and Claim 8 (Smart Friend as a reactive escalation pattern
    predating the parallel-agent Fusion/sidekick architecture): this post's
    Claim 6 (specific, constraint-laden briefs like the O(1) example
    outperform vague ones) is a Fusion-architecture-specific instance of
    the same underlying principle that earlier Cognition post established
    for the Smart Friend consult pattern — specificity of instruction to a
    cheaper/weaker model materially changes outcome quality, independent of
    which specific multi-model architecture is used.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 9 (Fable 5
    "stated the invariants it would hold itself to, then executed against
    them" on a migration task that had tripped up earlier models, in
    Cognition's Devin harness): this post's Claim 6 (Fable's briefs state
    explicit constraints and a definition of "done") is a structurally
    similar behavior pattern — stating explicit constraints/invariants
    before or during execution — reported independently by two different
    Cognition sources, in two different roles (Fable 5 stating its own
    invariants in the trust-focused post; Fable 5, as a lead, specifying
    invariants *for a sidekick* in this post).

- **Contradicts**: None filed as a formal contradiction issue. One
  near-miss was evaluated: this post's Fusion score/cost figures (Fable +
  Sidekick: 60.7 score / $1.86, on "FrontierCode 1.1 Extended") differ from
  `blog-cognition-devin-fusion.md` Claim 9's chart (Fusion + Fable 5: 57.6
  score / $3.00, on "FrontierCode Extended," measured on "an internal
  version of Devin Fusion" before Fable 5 access was suspended on June 12,
  2026) and from `blog-cognition-frontiercode.md` Claim 10's live Main
  leaderboard (solo Fable 5, no sidekick: 53.5%; solo Opus 4.8: 46.5%).
  None of these three figures are directly comparable: they differ in
  benchmark subset (Extended vs. Main), harness configuration (paired
  lead+sidekick vs. solo model), and point in time (this post is dated
  2026-07-13, after Fable 5 access was restored per
  `blog-vercel-ai-gateway-fable-5-restored.md`'s July 1, 2026 date, so it
  likely reflects a later, tuned Fusion build than the June 29 Devin
  Fusion launch post's pre-suspension figures). This does not meet the
  `agents/MINER.md` §4a bar for a filed contradiction — the differences are
  explained by named conditioning variables (subset, configuration, harness
  revision, and measurement date), not an opposed claim about the same
  measurement. Flagged here as an unresolved figure-comparability caveat
  rather than filed as a contradiction.

- **Extends**:
  - `blog-cognition-devin-fusion.md`: that post announced the Fusion
    lead+sidekick architecture and its headline 35%/41% cost-reduction
    results; this post is an explicit, self-referenced deep-dive follow-up
    ("When we introduced Devin Fusion, we showed a way out...") that parses
    every LLM call across 3,000 evaluation sessions to explain, at the
    mechanism level, *why* one specific lead model (Fable 5) achieves a
    larger cost win than another (Opus 4.8) inside that same architecture —
    something the launch post's aggregate results did not isolate by lead
    model.
  - `blog-cognition-frontiercode.md`: this post's entire evaluation is
    conducted on FrontierCode 1.1 (3,000 sessions), the benchmark that
    source documents in full methodological detail (six-axis grading,
    reverse-classical tests, scope enforcement, the internet-use
    anti-cheating revision) — this post supplies a new, lead-model-specific
    analysis on top of that benchmark's infrastructure without describing
    the benchmark's own mechanics.

- **Novel**:
  - The specific per-run cost/turn/token breakdown comparing two named
    frontier models as leads in an identical multi-agent harness paired
    with an identical sidekick (Claims 1-3) is new to this corpus — prior
    sources report aggregate harness-level cost savings
    (`blog-cognition-devin-fusion.md`) or solo-model benchmark scores
    (`blog-cognition-frontiercode.md`), but not a controlled, same-sidekick,
    lead-model-vs-lead-model comparison.
  - The 81%-vs-24% "lead never edits code" statistic (Claim 5) and the
    2x-more-context-pulls / 4x-more-corrective-edits post-handoff statistics
    (Claim 8) are new, specific, measurable operationalizations of "trusts
    its delegate" that no prior corpus source quantifies at this
    granularity.
  - The explicit finding that delegation *frequency* is equal (~3 handoffs
    per run for both leads) while delegation *outcome* differs sharply is a
    new and specific refinement of this corpus's general "delegate more"
    guidance — the differentiator identified here is delegation timing and
    brief quality, not delegation frequency.

## Guide Impact

- **Chapter 04 (Cost & Reliability) / Chapter 06 (Model Selection &
  Routing)**: Add Claim 1 as a concrete, named counterexample to the
  heuristic "a cheaper-per-token model always produces a cheaper agentic
  system" — cite the mechanism (Claims 2-3: fewer turns, less re-read
  context, higher code-edit avoidance) rather than the headline dollar
  figures alone, since the headline figures are scoped to one specific
  harness/benchmark/model pairing.

- **Chapter 04 (Cost & Reliability)**: Add Claim 4's "manager with an
  engineer" vs. "micromanager with an intern" framing, plus Claim 6's O(1)
  constraint example, as a concrete authoring guideline for delegation
  briefs in any lead+sidekick harness: specify hard constraints and a
  definition of "done" up front, rather than delegating implementation
  details and leaving performance/behavioral requirements implicit —
  supported by this post's own before/after score example (25 vs. 94 on
  the same task).

- **Chapter 04 (Cost & Reliability)**: Add Claim 8's post-handoff review
  statistics (2x more context pulls, 4x more corrective edits at lead
  prices for the less-effective delegator) as a measurable pattern teams
  can watch for in their own multi-model harness logs: repeatedly pulling a
  sub-agent's output back into the lead's own context and re-doing the work
  at lead prices is a specific, loggable signal that delegation briefs are
  under-specified, distinct from simply measuring aggregate cost.

- **Chapter 04 (Cost & Reliability)**: Add Claim 10's disclosed limitation
  (delegation savings are conditional on task decomposability; short tasks
  and single-chain serial-debugging tasks do not benefit) as a caveat
  alongside any citation of this post's headline cost figures, so the guide
  does not imply the savings generalize to all task types.

## Extraction Notes

- WebFetch's default fetch of this URL declined to reproduce long verbatim
  passages, citing IP/copyright concerns, when asked directly for
  section-by-section verbatim text. This is consistent with the general
  pattern of WebFetch applying reproduction-length limits observed
  elsewhere in this corpus (e.g. `blog-cognition-multi-agents-working.md`
  and `blog-cognition-devin-fusion.md` Extraction Notes, where the miner
  worked around this via `curl` + HTML tag-stripping). No `curl`/raw-HTML
  fallback was available in this extraction environment, so this note was
  built from multiple targeted WebFetch passes, each requesting a small
  number of short (under-125-character) direct quotes tied to a specific
  claim, rather than a single full-article dump. Each quote above under
  125 characters was returned by WebFetch inside quotation marks and
  attributed to a named section; these are treated as verbatim per
  WebFetch's own citation format, but — unlike the `curl`-based extractions
  in sibling Cognition notes — could not be independently cross-checked
  against raw HTML by this miner. This is a materially weaker verification
  standard than those sibling notes, and is disclosed here explicitly.
- One example (Claim 9, the changeset-migration remediation contrast) is
  reported without a verified verbatim quote: a WebFetch pass returned
  bracketed editorial paraphrase (e.g. "[reverts and reimplements at lead
  prices]") rather than clean source text for this specific example, which
  is a sign of AI-summarization rather than direct quotation. Per
  `agents/MINER.md` §2a Rule 5, no quote is asserted for this example; it
  is reported as a paraphrase and flagged for re-verification.
- The score units for the headline figures (60.7, 54.6, and the cost-table
  variants 60.8/55.4) are not stated in the source as retrieved — no
  percentage sign or "out of N" denominator was found in any WebFetch pass.
  This is disclosed as a gap in Source Context and should not be assumed to
  be directly comparable to the percentage-denominated FrontierCode Main/
  Extended scores in `blog-cognition-frontiercode.md` without further
  verification (see Cross-References → Contradicts for the fuller
  reasoning on why these are not treated as comparable here).
- The sidekick model's identity was not disclosed in any fetched pass — the
  post refers to it only as "a much cheaper model" / "the same cheap
  sidekick" throughout. This is noted in Source Context rather than
  guessed.
- Sub-pages: no linked sub-pages were identified as substantive beyond the
  post's own self-reference to the "Devin Fusion" launch post (already
  covered by `blog-cognition-devin-fusion.md` in this corpus) and implicit
  reliance on FrontierCode 1.1 (already covered by
  `blog-cognition-frontiercode.md`) — neither was re-fetched separately, per
  `agents/MINER.md` §1's guidance to follow linked pages only when they add
  information beyond what this corpus's existing notes already document.
- Cross-references verified before writing: re-read
  `blog-cognition-devin-fusion.md` in full and confirmed Claims 2 and 9 by
  number and content; re-read `blog-cognition-frontiercode.md` in full and
  confirmed Claim 10 by number and content; re-read
  `blog-cognition-multi-agents-working.md` in full and confirmed Claims 8
  and 9 by number and content; re-read
  `blog-anthropic-cognition-fable5-frontier-trust.md` in full and confirmed
  Claim 9 by number and content. No claim number was guessed or
  approximated.
- One contradiction candidate (this post's Fusion score/cost figures vs.
  the two prior Cognition source notes' differing figures) was evaluated
  against the `agents/MINER.md` §4a filing bar and did not meet it — see
  Cross-References → Contradicts for the full reasoning. No contradiction
  issue filed.
- Confidence is rated `emerging` overall: this is a first-party vendor
  follow-up analysis with several specific, quantified claims (a full
  cost/turn/token breakdown, an 81%-vs-24% behavioral statistic, named
  worked examples with before/after scores) drawn from a stated
  full-corpus analysis (parsing every LLM call across 3,000 sessions)
  rather than a handful of cherry-picked anecdotes, and it discloses at
  least one negative case (Claim 10's task-decomposability limitation)
  rather than reporting only favorable results. It does not reach
  `settled` because the analysis is entirely first-party (Cognition
  benchmarking its own harness on its own benchmark), no figure is
  independently replicated, the sidekick model's identity and the score
  units are undisclosed, and — per this extraction's own limitations —
  quotes in this note were not verified against raw HTML the way sibling
  Cognition notes in this corpus were.
