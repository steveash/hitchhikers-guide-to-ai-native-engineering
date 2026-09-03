---
source_url: https://newsletter.kentbeck.com/p/reject-change-sometimes
source_type: blog-post
title: "Reject Change, Sometimes"
author: Kent Beck
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: emerging
issue: "#3197"
---

# Reject Change, Sometimes (Kent Beck)

> Kent Beck uses Shannon's Demon — a portfolio-rebalancing strategy that
> outperforms both an all-safe and an all-risky strategy on the same
> symmetric bet — to argue that the *correct* strategy for accepting or
> rejecting change is not fixed but depends on the payoff structure of the
> bet on offer, then maps three different payoff structures (symmetric,
> asymmetric, three-outcome-with-death) onto his existing 3X product phases:
> Extract runs Shannon's Demon (rebalance/protect), Explore runs pure
> "Reckless" (go all-in on a big-asymmetric-upside bet), and Expand runs a
> third strategy focused on reducing the probability of death rather than
> optimizing the payoff directly.

## Source Context

- **Type**: blog-post (Kent Beck's newsletter, `newsletter.kentbeck.com`,
  published 2026-09-02, filed via the `kent-beck` trusted RSS feed).
- **Author credibility**: Kent Beck is the creator of Extreme Programming
  (XP) and Test-Driven Development (TDD), and a co-author of the Agile
  Manifesto — see `blog-kentbeck-trust-factory.md`,
  `blog-kentbeck-yagni-economics.md`, and
  `blog-kentbeck-3x-explore-expand-extract.md` for his broader corpus
  presence. This post is Beck applying a metaphor introduced to him by a
  named third party (Kunal Bhalla) to his own existing 3X framework, not a
  third-party report about Beck.
- **Scope**: A short essay in three named parts: (1) an intuition-building
  narrative and worked arithmetic example for Shannon's Demon (a
  rebalancing strategy that beats both a risk-averse strategy and an
  all-in-risky strategy on the same repeated symmetric double-or-half bet),
  under the heading "What?"; (2) a direct mapping of that intuition onto
  each of the three 3X phases (Extract, Explore, Expand), each under its
  own heading; and (3) an appendix containing a runnable JavaScript
  simulator Beck wrote to build his own intuition, plus a short
  acknowledgment to Kunal Bhalla. Does NOT cover: AI, AI agents, or
  AI-assisted development in any form — like `blog-kentbeck-3x-explore-expand-extract.md`,
  this piece is entirely conceptual/theoretical and contains no company
  examples, case studies, or real-world numeric metrics (the only numbers
  are the worked coin-flip arithmetic and simulator code). A block
  soliciting "custom talks and advisory engagements" for Beck's own
  consulting practice appears after the article's content, in the same
  structural position (after the appendix, no divider) as similar
  promotional blocks flagged in other Beck notes — see Extraction Notes.

## Extracted Claims

### Claim 1: Shannon's Demon (SD) — a strategy that rebalances 50/50 between a safe asset and a symmetric double-or-half bet after every round — grows over time, even though an all-safe strategy stays flat and an all-in-risky strategy on the same bet ends up "usually... around flat"
- **Evidence**: Beck's own opening narrative (the "ancient exchange" of three traders — Prudence, Reckless, and SD) plus the worked two-day arithmetic example that follows it.
- **Confidence**: settled (Shannon's Demon / volatility harvesting via periodic rebalancing is an established result in portfolio theory and control theory, independent of this essay; Beck's presentation of it is accurate to the standard result)
- **Quote**: "After a while a curious thing happened. Prudence's stack of coins stayed exactly the same. Reckless' stack grew & shrank & grew & shrank, half the time up, half the time down. But SD's stack grew over time. Same investments. Different outcomes. What's going on?"
- **Our assessment**: This is the essay's foundational intuition, and it is genuinely correct as stated — rebalancing into a symmetric-multiplicative bet converts a zero-drift gamble into positive expected growth by systematically "banking" gains before subsequent losses shrink a smaller base. The claim is sound on its own mathematical terms; the interesting (and less settled) part of the essay is the analogy applied afterward, not this base result.

### Claim 2: Worked arithmetic shows SD ends a two-round win/loss sequence with 112.5 coins (from a 100-coin start) regardless of whether the win or the loss comes first, while Reckless ends with exactly 100 coins either way
- **Evidence**: Beck's own step-by-step calculation, given twice (once for win-then-lose, once for lose-then-win) to show the result is order-independent for SD but always flat for Reckless.
- **Confidence**: settled (a specific, checkable arithmetic example; the two computations in the source are internally consistent and correctly worked)
- **Quote**: "If Reckless is betting 100 coins, they will end up with 100 coins—(100 * 2 / 2). SD will end up with 50 + (50 * 2) = 150 after the first day and then 75 (the rebalance) + (75 / 2) = 112.5."
- **Our assessment**: This is the essay's only fully concrete, reproducible artifact in the "What?" section — useful for the guide if it ever wants to illustrate the rebalancing mechanism with numbers rather than just narrative, since the two-round case is small enough to verify by hand.

### Claim 3: Beck states that his prior "long volatility" framing implied always embracing change/volatility, and that a reader (Kunal Bhalla) pointed out the necessary exception — that there are conditions under which one should deliberately "go short volatility" instead
- **Evidence**: Beck's own direct statement, opening the "What?" section, naming the source of the correction.
- **Confidence**: settled (a first-party statement of the essay's own motivation and attribution, not a claim about the world requiring outside verification)
- **Quote**: "In discussing long-volatility software development, so far I've made it sound like we always want to be long volatility (\"embrace change\", anyone?) Alert reader & good friend Kunal Bhalla pointed out the exception, when & how to go short volatility. He also introduced me to a powerful metaphor for building intuition around volatility—Shannon's Demon."
- **Our assessment**: This is the direct sequel to the deferred thesis flagged in `blog-kentbeck-xp-long-volatility.md` (see Cross-References). That earlier post promised the "XP is long volatility" argument would be developed "over the course of roughly the next year" in the paid section; this post is a piece of that promised development, and it explicitly complicates the "always embrace change" framing that a naive reading of "long volatility" would suggest — change/volatility is sometimes worth rejecting, which is this note's title claim, though the phrase "reject change" itself does not otherwise recur in the article body.

### Claim 4: In the Extract phase, the payoff structure resembles the original symmetric double-or-half bet, so the SD (rebalancing) product strategy is the correct one: protect the revenue stream, take some growth bets, lower costs, and keep changes reversible as much as possible
- **Evidence**: Beck's own mapping, in the "3X: Extract" section, of the symmetric-bet math from the "What?" section onto the Extract phase of his existing 3X framework.
- **Confidence**: emerging (a direct, named application of a settled financial-math result to a specific business-strategy phase; the underlying math is settled, but the mapping of "symmetric payoff" onto "Extract phase" specifically is Beck's own asserted analogy, not independently validated)
- **Quote**: "In such an environment, the SD product strategy makes the most sense. Protect the revenue stream. Take some growth bets. Lower costs. Keep changes reversible as much as possible."
- **Our assessment**: This is the essay's most guide-actionable single line — a four-part tactical prescription (protect revenue, take some growth bets, lower costs, keep changes reversible) for the phase 3X already identifies as mature/profit-optimizing. It reads as a refinement of the Extract-phase tactics already captured in `blog-kentbeck-3x-explore-expand-extract.md` Claim 6 ("small, safe experiments; roll out successes; optimize costs") rather than a contradiction of them — "keep changes reversible" is new phrasing not present in that earlier note's Extract tactics.

### Claim 5: Changing the bet's payoff to be asymmetric (+300% on a win, −33% on a loss) flips the optimal strategy from rebalancing to going all-in on the risky option — this is the Explore-phase mapping, and Beck frames it as not an ROI/expected-value question but a "how should we play it" question
- **Evidence**: Beck's own worked reasoning in the "3X: Explore" section, contrasting pairs of outcomes (win-then-lose vs. lose-then-win) under the new payoff scheme against the original symmetric one.
- **Confidence**: emerging (the underlying point — that optimal strategy under repeated multiplicative bets depends on the specific payoff ratios, not just their sign — is a real and well-known result in Kelly-criterion-adjacent reasoning; Beck's specific claim that this is the correct model for an Explore-phase product bet is his own applied argument, not independently tested)
- **Quote**: "Note how we aren't making an ROI-based decision. Should we play this flipper/strongbox combination? Does it provide a positive expected value? That's the not the interesting question. The interesting question is how we should play it."
- **Quote (framing)**: "The +300%/-33% flipper looks like the Explore payoff (actual numbers chosen at your discretion). So in Explore we go all in on the flipper. Reckless may be reckless, but they aren't irrational."
- **Our assessment**: This is the essay's sharpest reframe: it explicitly rejects the standard "is the expected value positive" question in favor of "given that the payoff is positive, what allocation strategy is optimal" — a subtler and more specific claim than a generic "take big swings in Explore" heuristic. Worth flagging for the guide: Beck states the specific numbers (+300%/−33%) are illustrative ("chosen at your discretion"), not empirically derived from any real product data.

### Claim 6: The Expand phase requires a richer three-outcome model — succeed (win), die (an outcome that "erases all possible future gains"), or switch to Extract — and the corresponding strategy is neither pure rebalancing nor pure all-in risk-taking, but engineering and operational investment to reduce the probability of death
- **Evidence**: Beck's own model extension in the "3X: Expand" section, explicitly naming this as a departure from the two prior phases' simpler models.
- **Confidence**: emerging (a structural extension of the essay's own framework to a third, more complex payoff shape; internally consistent with Claims 4-5's logic, but not validated against any real Expand-phase case)
- **Quote**: "Expand is where the model needs to get richer. In Expand we have 3 outcomes each \"turn\": Succeed at overcoming the next growth bottleneck. (The winning outcome.) Die. Lose everything. (The losing outcome. It really costs you because it erases all possible future gains.) Switch to Extract. (This one is new.)"
- **Quote (strategy)**: "Where Explore is pure Reckless & Extract is pure Shannon's Demon, Expand offers a new strategy for creating value:—engineering & operational investment to reduce the probability of death. Could be performance tuning, securing future resources, even things like improving backup & recovery procedures."
- **Our assessment**: This is the essay's most novel structural move relative to `blog-kentbeck-3x-explore-expand-extract.md`, which described Expand's goal/risk/tactics in a single compact line ("Avoid fatal obstacles while scaling furiously" / "Throttle growth, discard non-essential features, good-enough-for-now scaling") without a formal payoff model. This essay supplies that missing model: Expand's "die" outcome is uniquely costly not because it is a large negative number but because it is irreversible and forecloses all future option value — an argument structurally parallel to (though not explicitly connected by Beck to) the "optionality bill" in `blog-kentbeck-yagni-economics.md` Claim 3.

### Claim 7: During Expand, pushing (aggressively pursuing demand-driven growth) increases risk, while reducing friction sustains growth longer — and the phase is characterized by operating inside a system "only vaguely seen & understood," with the implication that once the system's dynamics become legible, a rebalancing (Shannon's Demon) strategy becomes viable
- **Evidence**: Beck's own closing observation in the "3X: Expand" section.
- **Confidence**: anecdotal (a qualitative, unmeasured operational claim and forward-looking implication, stated without a worked example or specific criterion for when a system has become "legible enough")
- **Quote**: "During Expand demand is pulling customers/usage/revenue. Pushing increases risk. Reducing friction sustains growth longer. And all of this is taking place inside a system only vaguely seen & understood. Some day the dials & levers will come into focus. Then you can put Shannon's Demon in charge."
- **Our assessment**: This is the essay's implicit answer to "when does a product graduate from Expand to Extract" — not a fixed time or revenue threshold, but the point at which the system's cause-and-effect relationships become legible enough to support deliberate rebalancing. This is consistent with, but more specific than, the transition criterion this note's Claim 6 corroborates and `blog-kentbeck-3x-explore-expand-extract.md` Claim 5 already recorded ("the phase ends once cause-and-effect relationships become predictable").

### Claim 8: Beck built and shares a runnable JavaScript simulator (a 100-day repeated-bet simulation, run 1,000 times, reporting the median outcome for each of the three strategies) as his own method for gaining intuition about Shannon's Demon, rather than deriving the result analytically
- **Evidence**: The "Appendix: Simulator" section and the code block itself.
- **Confidence**: settled (a first-party statement of Beck's own working method, and the code is a directly inspectable, reproducible artifact — see Concrete Artifacts)
- **Quote**: "I'm a programmer. I understand the world so I can program. I program so I can understand the world. Here is a little simulator I created & played with to help me gain intuition about the message of Shannon's Demon."
- **Our assessment**: A small but notable methodological data point: Beck's own preferred way of verifying a probabilistic/economic claim before publishing it is to write and run a simulation, not to rely on the closed-form math alone — consistent with a "programmer's" epistemics generally, and a concrete, checkable artifact the guide could point to if it ever discusses verifying probabilistic claims by simulation rather than argument alone.

## Concrete Artifacts

### Shannon's Demon simulator (verbatim JavaScript)

```
Source: Kent Beck, "Reject Change, Sometimes", newsletter.kentbeck.com,
2026-09-02, "Appendix: Simulator" section

const trade = (strategy) => {
  let coins = 100;
  for (let day = 0; day < 100; day++)
    coins = strategy(coins, Math.random() < 0.5 ? 2 : 0.5);
  return coins;
};

const prudence = (coins, flip) => coins;                  // all in the box
const reckless = (coins, flip) => coins * flip;           // all in the flipper
const demon    = (coins, flip) => coins/2 + coins/2*flip; // half & half, re-split daily

const median = (strategy) => {
  const results = Array.from({length: 1000}, () => trade(strategy)).sort((a, b) => a - b);
  return results[500];
};

console.log(`Prudence  ${median(prudence).toFixed(0)}`);
console.log(`Reckless  ${median(reckless).toFixed(0)}`);
console.log(`Demon     ${median(demon).toFixed(0)}`);
```

### The three 3X phases mapped to bet strategies (verbatim, condensed)

```
Source: Kent Beck, "Reject Change, Sometimes", newsletter.kentbeck.com, 2026-09-02

Extract — symmetric bet (double or half) → SD / rebalancing strategy
  "Protect the revenue stream. Take some growth bets. Lower costs.
   Keep changes reversible as much as possible."

Explore — asymmetric bet (+300% / -33%) → pure Reckless strategy
  "So in Explore we go all in on the flipper. Reckless may be reckless,
   but they aren't irrational."

Expand — three-outcome bet (succeed / die / switch to Extract) → a third
strategy: reduce the probability of death
  "Engineering & operational investment to reduce the probability of
   death. Could be performance tuning, securing future resources, even
   things like improving backup & recovery procedures."
```

## Cross-References

- **Extends**: `blog-kentbeck-xp-long-volatility.md` Claim 6, which recorded
  Beck's explicit deferral of the "XP is long volatility" argument to
  future paid-section posts ("I'm going to be exploring... or rather
  expanding... this idea of long volatility... you can (very reasonably)
  wait the year it will take to refine the idea"). This post is a concrete
  installment of that promised development: Claim 3 above shows Beck
  directly building on the "long volatility" framing from that earlier
  post and explicitly complicating it (there are conditions for going
  *short* volatility too). That earlier note's caution — "any guide
  citation of 'XP is long volatility' as a developed argument would be
  citing content that does not yet exist in accessible form" — should be
  revisited now that at least one substantive follow-up post exists,
  though the argument is still evidently unfolding across multiple posts
  rather than complete in this one.
- **Extends**: `blog-kentbeck-3x-explore-expand-extract.md` Claims 4-6 (the
  goal/risk/tactics one-liners for Explore, Expand, and Extract). This
  essay supplies a formal payoff-structure justification for each of those
  three tactical one-liners that the earlier note explicitly flagged as
  absent: that note's Claim 3 called the phase-mismatch thesis "notably
  thin on evidence: no specific historical example... is given," and this
  essay (while still not a case study) at least supplies a worked
  mathematical mechanism for *why* each phase's tactics differ, rather
  than asserting the tactics as a bare list. Specifically: Extract's "keep
  changes reversible" (this note's Claim 4) refines that note's Extract
  tactics ("small, safe experiments; roll out successes; optimize costs");
  Explore's "go all in" (this note's Claim 5) is consistent with but more
  quantitatively specific than that note's Explore tactics ("tiny teams,
  no dependencies, quickly discard failures"); and Expand's three-outcome
  death model (this note's Claim 6) is an entirely new formal structure
  not present in that note's compact "avoid fatal obstacles while scaling
  furiously" line.
- **Extends**: `blog-kentbeck-yagni-economics.md` Claim 3 (the "optionality
  bill" — committing to structure forecloses the option to build correctly
  later, and this loss occurs even if the guess turns out correct). This
  essay's Claim 6 (Expand's "die" outcome "erases all possible future
  gains") is a structurally similar irreversibility argument applied one
  level up, at the level of a whole initiative's survival rather than a
  single structural decision — both treat irreversible foreclosure of
  future options as the thing that makes an outcome costly, independent of
  the raw payoff size. Beck does not explicitly connect the two essays
  himself.
- **Corroborates**: `blog-kentbeck-3x-explore-expand-extract.md` Claim 2
  (the S-curve is produced by two competing feedback loops, and phase
  transitions correspond to where control shifts between them) via this
  note's Claim 7, which independently describes the Expand-to-Extract
  transition as occurring once "the dials & levers... come into focus" —
  i.e., once the system's causal structure (which loop dominates) becomes
  legible enough to act on deliberately. Two separate posts, six weeks
  apart, describe the same transition criterion (system legibility/
  predictability) rather than a fixed time or revenue threshold.
- **Contradicts**: None identified. This source does not address AI-agent
  development at all — like `blog-kentbeck-3x-explore-expand-extract.md`,
  it operates purely at the level of general product-strategy payoff
  structures, a different, non-conflicting layer from the corpus's
  AI-specific claims (e.g., `blog-kentbeck-trust-factory.md`'s "single
  player" genie-erosion diagnosis).
- **Novel**:
  - **Shannon's Demon / volatility-harvesting rebalancing as an explicit
    strategy metaphor (Claims 1-2)**: not present anywhere else in the
    corpus; a distinct, mathematically well-grounded framework for why
    "sometimes reject change" (deliberately not taking every available
    positive-looking bet) can outperform "always accept change."
  - **A formal payoff-structure justification for each 3X phase's tactics
    (Claims 4-6)**: the earlier 3X note supplied *what* each phase's
    tactics are; this note supplies *why*, in terms of the specific bet
    structure (symmetric / asymmetric / three-outcome-with-death) each
    phase resembles.
  - **The "ROI question vs. allocation question" reframe (Claim 5)**: the
    explicit argument that, given a positive-EV bet, the interesting
    strategic question is not whether to take it but how much of your
    resources to commit to it — not present elsewhere in the corpus in
    this form.
  - **A runnable, inspectable simulation artifact for a probabilistic
    business-strategy claim (Claim 8)**: distinct from the corpus's other
    Beck code artifact (`blog-kentbeck-smalltalk-genie.md`'s shipped
    GitHub repo, which is a software-development demo, not a strategy
    simulation).

## Guide Impact

- **Chapter 05 (Team Adoption)**: Consolidate with the existing 3X guide
  recommendation already flagged in `blog-kentbeck-3x-explore-expand-extract.md`'s
  Guide Impact (which recommends introducing 3X in Chapter 05 as a
  structural check — "before recommending a specific AI-adoption practice
  ... first ask which of the three phases the team/initiative is actually
  in"). This post adds a concrete mechanism the Smith can cite alongside
  that check: Claim 4's Extract-phase prescription ("keep changes
  reversible as much as possible") is directly actionable guidance for
  AI-native teams whose products have reached a mature, revenue-protecting
  phase — it argues for treating an AI agent's proposed changes with the
  same rebalancing discipline (small, reversible, revenue-protecting) that
  Beck argues is mathematically optimal for a symmetric-payoff environment,
  rather than either blocking all agent-proposed changes (Prudence) or
  accepting all of them (Reckless).
- **Chapter 05 (Team Adoption)**: Claim 5's explicit "ROI question vs.
  allocation question" reframe is a citable caution against a common
  simplification in AI-adoption decisions: teams often ask "does this
  AI-agent bet have positive expected value?" when, per this framework,
  the more useful question in an Explore-phase context is "given that it
  does, how much should we commit to it?" Recommend citing this alongside
  the existing 3X phase-check guidance as a refinement, not a replacement.
- **Chapter 04 (Context Engineering) or wherever irreversibility/optionality
  guidance lives**: Claim 6's "die" outcome (irreversible, forecloses all
  future gains) is a second, independent source (alongside
  `blog-kentbeck-yagni-economics.md` Claim 3's optionality bill) for
  treating irreversibility itself — not raw downside magnitude — as the
  thing that should most constrain agent autonomy in Expand-like,
  high-stakes situations (e.g., destructive migrations, irreversible data
  operations). Recommend citing both sources together if the guide adds
  irreversibility-specific guardrail guidance.
- No other chapter has directly actionable content from this source at
  this time: like the earlier 3X post, this essay never mentions AI, AI
  agents, or AI-assisted development, so its applicability is entirely by
  extrapolation from a general product-strategy framework, not by the
  source's own stated scope.

## Extraction Notes

- An initial plan to use WebFetch was set aside in favor of a direct
  `curl` fetch with a browser user-agent, following the pattern already
  documented in `blog-kentbeck-xp-long-volatility.md` and
  `blog-kentbeck-yagni-economics.md`'s Extraction Notes (WebFetch's
  summarizer has previously declined to reproduce Kent Beck posts
  verbatim). The raw HTML was fetched successfully (200 status), the
  article body isolated via its `class="body markup"` container, HTML
  tags stripped, and entities decoded — all quotes in this note were
  copied from that raw text, not reconstructed from any summary.
- The full post is short and not paywalled; there is no "subscribe to
  read the rest" gate anywhere in the fetched HTML, and the content
  matches the structure (intuition-building → 3X phase mapping →
  simulator appendix) that the Prospector's third triage comment
  anticipated. No sub-pages or linked pages substantive enough to warrant
  following per MINER.md §1 were found in the article body (the only
  outbound links are to the Wikipedia "multi-armed bandit" article, an
  aside rather than a substantive linked source).
- A promotional block ("Most teams don't have a strategy problem. They
  have an adaptation problem... I help teams bend. Adapt to Thrive...
  Booking a handful of custom talks and advisory engagements now...")
  appears immediately after the simulator appendix, with no divider and
  no explicit "sponsored" label in the fetched HTML. Following the
  precedent in `blog-kentbeck-3x-explore-expand-extract.md`'s Extraction
  Notes (which flagged a similarly-positioned, similarly-unlabeled block
  rather than silently including or silently excluding it), this block
  was read but deliberately **not** extracted as a claim — it is not
  connected back to the Shannon's Demon/3X argument by Beck himself in the
  accessible text, and its structural position (immediately before a paid
  consulting solicitation) matches the disclosed-sponsored pattern from
  `blog-kentbeck-xp-long-volatility.md` closely enough to treat it as
  self-promotional rather than essay content.
- No contradiction issue was filed. This source does not materially
  oppose any existing corpus source note's claim — it extends and
  corroborates existing Kent Beck corpus content on 3X and YAGNI/optionality
  (see Cross-References) rather than opposing it.
- Confidence rated `emerging` overall: the foundational Shannon's Demon
  math (Claims 1-2) is `settled` on its own terms (an established result,
  correctly presented), but the essay's guide-relevant content is the
  *application* of that math to the 3X business-strategy phases (Claims
  4-7), which is Beck's own asserted analogy — internally consistent and
  building on a framework already refined over months per
  `blog-kentbeck-xp-long-volatility.md`'s account of 3X's own incubation,
  but not validated against any real product case study or empirical data
  in this piece. Not rated `settled` overall because the phase-mapping
  claims are the load-bearing, novel content and remain asserted rather
  than tested; not rated `anecdotal` because most claims are a structured,
  first-party theoretical extension of an established framework rather
  than a single unverified anecdote (Claim 7 is the one claim individually
  flagged `anecdotal`).
- Cross-reference claim numbers were verified by re-reading the cited
  notes directly before writing: `blog-kentbeck-xp-long-volatility.md`
  Claim 6 (the deferred "long volatility" thesis, confirmed at that note's
  Claim 6 heading); `blog-kentbeck-3x-explore-expand-extract.md` Claims
  2, 3, 4, 5, and 6 (the two-feedback-loop mechanism, phase-mismatch
  thesis, and Explore/Expand/Extract goal-risk-tactics breakdowns, all
  confirmed at their respective headings); `blog-kentbeck-yagni-economics.md`
  Claim 3 (the optionality bill, confirmed at that note's Claim 3
  heading).
