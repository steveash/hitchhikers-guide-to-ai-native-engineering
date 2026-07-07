---
source_url: https://mattwood.blog/essays/2026/07/the-cost-of-the-answer/
source_type: blog-post
title: "The Cost of the Answer"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-07-02
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1601"
---

# The Cost of the Answer

> Matt Wood (AWS Chief AI & Technology Officer) argues that AI work only
> compounds when the cost of *knowing whether the work improved* — not the
> cost of the work itself — falls; that the evaluator, not the generator, is
> where a loop's economics are decided; and that the durable organizational
> asset is the evaluator apparatus (rubrics, objection sets, worked examples),
> not any single artifact it improves, which depreciates the moment it ships.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; single-author, no citations infrastructure, no images or
  tables; ~1,700 words; five named sections: "The machinery and the
  economics," "The theory of value," "Making answers cheap, and keeping them
  honest," "The durable asset," plus an unnamed closing section).
- **Author credibility**: Matt Wood returned to AWS in 2026 as Chief AI &
  Technology Officer after nearly 15 years at AWS earlier in his career and,
  most recently, leading commercial technology and innovation at PwC (per the
  site's About page, cited in full in `blog-mattwood-field-and-frontier.md`
  Concrete Artifacts). He holds a PhD in machine learning and did a
  postdoctoral fellowship in NLP/bioinformatics at Weill Cornell Medicine.
  This is a `trusted-feed` source (per the triage issue) — the third essay
  discovered from this feed in the corpus — meaning it already passed an
  author-worth-listening-to bar. The essay itself is a conceptual/strategy
  argument with no cited data, named customer example, or benchmark; every
  claim is the author's own reasoning and metaphor, not a measured finding.
- **Scope**: Covers a checking-account/savings-account metaphor for
  compounding vs. one-off value; a definition of "loop" and "evaluator"; the
  claim that answer cost (not work cost) determines which work compounds;
  a worked explanation of why coding compounded first (cheap evaluator
  infrastructure, not self-writing tests); the claim that a strategy's final
  verdict can stay expensive while intermediate answers are cheap; four
  concrete techniques for making an answer cheap and trustworthy (bounded
  comparison, plateau-watching, evidence-requiring, twice-repeated pattern);
  a "durable asset" argument that the evaluator apparatus — not the
  artifact — is what compounds, illustrated with a four-pass strategy-memo
  example; and a closing argument that organizations under-invest in
  evaluator infrastructure because it looks like overhead while automation
  pays back immediately. Does NOT cover: specific tooling, a named
  organization's case study, metrics/benchmarks, code examples, or a
  rebuttal/counter-perspective (single-voice essay, no comments).

## Extracted Claims

### Claim 1: A checking account (proportional, capped return) and a savings account (compounding return) are the two shapes AI investment can take, and most teams are operating only the first
- **Evidence**: Author's opening framing metaphor, presented before any of the
  essay's other arguments.
- **Confidence**: anecdotal (interpretive metaphor, not a measured finding)
- **Quote**: "What separates the two accounts is not the money. It is whether anything in the system can turn this period's balance into next period's growth. AI has the same dividing line: it compounds only when the organization lowers the cost of knowing whether the work got better. The cost that matters is not the cost of the work but the cost of the answer."
- **Our assessment**: This is the essay's organizing device and its main
  contribution to the guide's vocabulary — a named distinction between
  proportional automation gains (checking account) and compounding judgment
  gains (savings account). It is asserted as metaphor, not demonstrated with
  data, but it reframes "is AI paying off" from a throughput question into an
  economics-of-evaluation question, which the rest of the essay operationalizes.

### Claim 2: A loop is defined narrowly as a system that does work, evaluates it, and feeds the evaluation back into the next round — anything that doesn't close that circuit is a single pass repeated, however fast or automated
- **Evidence**: Author's own definitional framing.
- **Confidence**: anecdotal (definitional claim)
- **Quote**: "Anything that closes that circuit is a loop. Anything that doesn't, no matter how fast or how automated, is a single pass repeated."
- **Our assessment**: This tightens the corpus's existing "loop" vocabulary
  (e.g. `blog-anthropic-getting-started-with-loops.md` Claim 1's "agents
  repeating cycles of work until a stop condition is met") by adding a
  necessary condition: the evaluation of round N must feed into round N+1,
  not just repeat. A fast, automated pipeline with no evaluation feedback is,
  by this definition, not a loop at all — a distinction the Anthropic
  four-type taxonomy does not make explicit.

### Claim 3: Agents have made the generation half of a loop nearly free, which means the evaluator — not the generator — now decides a loop's economics
- **Evidence**: Author's own economic argument, framed as the essay's central
  mechanism.
- **Confidence**: anecdotal (interpretive economic claim, no cost data cited)
- **Quote**: "Agents have made the first half nearly free. The work itself, the drafting, the coding, the generating, now costs so little that it is no longer where the economics of the loop are decided; the evaluator is."
- **Our assessment**: This directly corroborates
  `blog-anthropic-harness-long-running.md` Claim 2 (the GAN-inspired
  generator/evaluator split "outperforms prompting a single agent to
  self-critique") and Claim 10 (the evaluator's value is task-relative) —
  both sources independently converge on the evaluator as the load-bearing
  component of a working loop. Wood's essay supplies the economic argument
  for *why* (generation cost has collapsed, shifting scarcity to judgment)
  where the Anthropic post supplies the architectural mechanism.

### Claim 4: An unvalidated loop can reinforce a mistake as easily as fix one and get progressively wronger every round while still looking like progress
- **Evidence**: Author's own argument, following directly from Claim 3.
- **Confidence**: anecdotal (asserted failure mode, no measured example)
- **Quote**: "An unvalidated loop can reinforce a mistake as easily as fix one, and it can get wronger every round, which is worse than never looping at all, because it looks like progress the whole way down."
- **Our assessment**: This is a sharp articulation of a risk documented more
  concretely elsewhere in the corpus. `blog-ronacher-the-coming-loop.md`
  Claim 5 describes the mechanism this claim predicts in the wild: harness
  loops amplify models' defensive-code tendency so "the system slowly
  becomes less understandable while appearing more robust." Wood's claim is
  the general theoretical statement ("looks like progress the whole way
  down"); Ronacher's is the specific observed instance (accumulating
  defensive code that passes tests while degrading comprehensibility). The
  two corroborate at different levels of abstraction.

### Claim 5: Coding compounded first not because tests write themselves, but because software engineering spent decades building cheap evaluator infrastructure — tests, builds, linters, type systems, benchmarks, CI
- **Evidence**: Author's own historical argument, explicitly rejecting the
  "tempting" alternative explanation (free self-running tests) before stating
  this one.
- **Confidence**: anecdotal (historical/causal claim, no citation of when or
  how much this infrastructure investment cost)
- **Quote**: "Coding compounded first because software engineering spent decades building cheap evaluators: tests, builds, linters, type systems, benchmarks, continuous integration. Fields compound when they invest in answer infrastructure."
- **Our assessment**: This reframes a claim already present in the corpus in
  a different causal direction. `blog-addyosmani-code-agent-orchestra.md`
  Claim 5 (per `blog-langchain-human-judgment-improvement-loop.md`
  Cross-References) argues "the bottleneck is no longer generation. It's
  verification" as a present-tense diagnosis; Wood's claim is a historical
  explanation for why coding was the *first* domain to compound at all — the
  verification infrastructure predates the AI-agent era by decades. This is
  a useful corrective against implying that coding's compounding is somehow
  intrinsic to code as a medium; the essay argues it is intrinsic to the
  field's prior infrastructure investment instead.

### Claim 6: A strategy's final verdict can stay genuinely expensive (unknown for months) while it decomposes into cheap intermediate answers — clarity, explicit assumptions, addressed objections, survival against plausible futures — that a loop can run on
- **Evidence**: Author's own argument extending the coding/writing/strategy
  comparison into a prescription for what a loop can and cannot cheaply know.
- **Confidence**: anecdotal (conceptual claim, no measured example of a
  strategy loop in practice)
- **Quote**: "AI cannot know the final truth cheaply, and it does not need to: it can lower the cost of the intermediate answers that make the final judgment better, and those are the answers a loop runs on. The verdict stays with whoever owns the call; the loop hands them better material to make it with."
- **Our assessment**: This is the essay's answer to an obvious objection
  ("if strategy's outcome takes months to verify, how can it loop at all?").
  The decomposition into cheap intermediate proxies is the load-bearing
  move — it explains how judgment-heavy work can compound without requiring
  the loop to solve the actual hard problem (was the strategy right).
  This is conceptually close to `blog-langchain-human-judgment-improvement-loop.md`
  Claim 9 (borderline evaluator scores flag calibration issues, very negative
  scores flag agent problems) in spirit — both treat the evaluator's signal
  as a proxy to be interpreted, not a final verdict — but Wood's claim is
  about proxy *design* (what cheap questions substitute for an expensive one)
  while LangChain's is about proxy *diagnosis* (what a given score means).

### Claim 7: You lower the cost of an answer by asking a bounded, comparative question ("does this beat the last one?") instead of an unbounded absolute one ("is this good?")
- **Evidence**: Author's own prescriptive technique, the first of four
  cost/trust techniques offered in the essay's fourth section.
- **Confidence**: anecdotal (prescriptive technique, no comparative data on
  bounded vs. unbounded evaluation cost)
- **Quote**: "Judging whether a draft is good in any absolute sense is slow and expensive. Judging whether this version beats the last one is cheaper, and it is usually all the loop needs. Comparison can still be hard when dimensions conflict, one version clearer, the other bolder, but the question stays bounded: two candidates, one call, no need to define good in the abstract."
- **Our assessment**: This is a concrete, actionable design principle for
  evaluator prompts, distinct from anything named in
  `blog-anthropic-harness-long-running.md` (which documents "sprint
  contracts" — negotiating what "done" looks like in advance — but not the
  narrower comparative-vs-absolute question framing). It is a small but
  specific addition to the corpus's evaluator-design toolkit: prefer
  pairwise/relative judgments over absolute quality judgments where possible.

### Claim 8: You lower cost further by watching for a plateau (shrinking round-to-round changes, or the same fix recurring) as a free trend signal, instead of waiting for a defined finish line
- **Evidence**: Author's own prescriptive technique, the second of four.
- **Confidence**: anecdotal (prescriptive technique, no example of this
  plateau-detection heuristic implemented in a real system)
- **Quote**: "Watch the size of the changes each round: when they shrink toward nothing, or the same fix keeps recurring, you have a signal, not a verdict, and it cost nothing but attention to a trend you were already tracking."
- **Our assessment**: This names an evaluation-free stopping heuristic — you
  do not need an evaluator to tell you "done," only to notice the loop has
  stopped producing new information. It is a lighter-weight complement to
  `blog-anthropic-getting-started-with-loops.md` Claim 3's `/goal` mechanism
  (a separate evaluator model checks a defined success condition after every
  turn) — Wood's plateau heuristic could serve as a stop condition even when
  no explicit success criterion has been defined, which is exactly the case
  (open-ended strategy work) the essay is arguing loops need to handle.

### Claim 9: You raise an answer's trustworthiness by requiring evidence for any claimed win (the specific change, the specific result) and by requiring a pattern to repeat once before trusting it as a lesson
- **Evidence**: Author's own prescriptive technique, the third and fourth of
  four, presented together as the "keeping them honest" half of the section.
- **Confidence**: anecdotal (prescriptive technique, no measured comparison of
  loops with vs. without these two checks)
- **Quote**: "A loop with no free answer can talk itself into progress that is not there, so make it show its work: the specific change, the specific result. This does not make any single check faster. It makes the check honest, which is what keeps you from compounding on a false gain."
- **Additional quote**: "Waiting for it to show up twice costs one extra round and buys an answer that is harder to fool."
- **Our assessment**: This directly corroborates
  `blog-anthropic-harness-long-running.md` Claim 6 (out-of-the-box evaluators
  "identify legitimate issues, then talk itself into deciding they weren't a
  big deal" — the rationalization/sycophancy failure mode) and Claim 14
  (criteria wording shapes generator behavior in unexpected ways). Wood's
  "show its work" and "wait for it to show up twice" are concrete, generic
  mitigations for the same rationalization risk Rajasekaran documents
  empirically in a specific harness; this essay generalizes it into a
  named discipline (evidence-requiring, pattern-repetition) applicable to any
  evaluator design, not just the QA-agent case Rajasekaran describes.

### Claim 10: The artifact a loop improves was never the durable asset — it depreciates the day it ships; the evaluator apparatus (rubrics, objection sets, worked examples, recorded failures) is what can persist and compound
- **Evidence**: Author's own central argument in the "durable asset" section,
  illustrated with a four-pass strategy-memo example (rubric holds the
  draft → recurring objection gets flagged → objection gets written into the
  standing rubric → next unrelated memo inherits the fix).
- **Confidence**: anecdotal (conceptual argument with an illustrative,
  non-empirical example)
- **Quote**: "The artifact was never the asset. It ships, it leaves, and it starts depreciating the day it is done. The evaluator can stay."
- **Additional quote**: "Run this for a year and the company has not merely produced better memos. It has accumulated better strategic taste, held somewhere that does not walk out the door."
- **Our assessment**: This is the essay's headline contribution and the one
  the Prospector's triage comment specifically flagged for extraction. It
  extends `blog-anthropic-harness-long-running.md` Claim 9 ("every component
  in a harness encodes an assumption... those assumptions are worth stress
  testing," components pruned as models improve) with a complementary but
  distinct claim: where Rajasekaran's post is about pruning stale harness
  *components*, Wood's claim is about which harness *component category*
  (the evaluator specifically, not the generator or the artifact) is worth
  investing in for long-term compounding. It also extends
  `blog-langchain-human-judgment-improvement-loop.md` Claim 13 (golden
  datasets as a regression-prevention baseline curated by SMEs) — Wood's
  "standing rubric that inherits every recurring objection" is a more
  general version of the same accumulation pattern LangChain describes
  specifically for golden datasets: both describe an evaluator asset that
  is deliberately built up over time and outlives any single work product.

### Claim 11: Durable evaluator assets are not maintenance-free — rubrics can ossify into bureaucracy, objection sets can overfit to the last failure, and accumulated taste can quietly become accumulated caution
- **Evidence**: Author's own qualification of the "durable asset" argument,
  immediately following the strategy-memo example.
- **Confidence**: anecdotal (qualifying claim, no example of an ossified
  evaluator or how the author detected/fixed one)
- **Quote**: "They can also ossify: a rubric can harden into bureaucracy, an objection set can overfit to the last failure, accumulated taste can quietly become accumulated caution. The asset needs maintenance, new evidence, new counterexamples, an occasional reset."
- **Our assessment**: This is an important counterweight to Claim 10 that
  keeps the essay from reading as unconditional evaluator-investment
  advocacy. No existing corpus source names evaluator ossification as a
  distinct risk category (the closest is
  `blog-anthropic-harness-long-running.md` Claim 9's harness-component
  pruning, which addresses components going *stale relative to model
  capability*, not a rubric hardening into institutional caution). The guide
  should treat this as a maintenance requirement paired with any
  "build a durable evaluator" recommendation, not an isolated caveat.

### Claim 12: Organizations under-invest in evaluator infrastructure because automation pays back in throughput within the first week while an evaluator looks like pure overhead until it becomes the asset, so budget keeps flowing to "what can I automate" instead
- **Evidence**: Author's own closing argument, framed as an explanation for
  why most teams remain in the "checking account" pattern from Claim 1
  despite the compounding case made in Claims 3-11.
- **Confidence**: anecdotal (organizational-behavior claim, no survey or
  budget-allocation data cited)
- **Quote**: "Automation pays back in throughput, and throughput shows up in the first week; an evaluator looks like overhead right up until it becomes the asset. So the natural question, what work can I automate, keeps winning the budget, and it leads to checking accounts every time: you speed up the work, pocket the gain, and the next gain costs another deposit."
- **Our assessment**: This is the essay's explanation for a pattern
  `blog-mattwood-field-and-frontier.md` (same author) documents from a
  different angle: that note's Claim 5 cites Forrester's estimate that genAI
  orchestrates less than 1% of core business processes despite broad
  experimentation. Read together, the two essays argue the same
  under-investment from different mechanisms — the field-and-frontier essay
  attributes it to organizations being over-indexed on frontier exploration
  and under-indexed on field deployment; this essay attributes it to a
  budget-visibility asymmetry (throughput is visible in week one, evaluator
  value is invisible until it compounds). Both are the author's own
  interpretive frameworks, not competing empirical claims, so this is a
  complementary explanation rather than a corroboration of a shared fact.

### Claim 13: The prescriptive reframe for where to invest is "where is the cost of the answer too high to loop?" rather than "what can I automate?" — and those high-cost-of-answer places are the map of where lasting value sits, not a failure of AI
- **Evidence**: Author's closing synthesis, the essay's final argument.
- **Confidence**: anecdotal (prescriptive framing, closes the essay without
  new evidence)
- **Quote**: "The better question is: where is the cost of the answer too high to loop? Those places are not failures of AI; they are the map of where to invest. Lower the cost of the answer and the work starts compounding."
- **Our assessment**: This is the essay's most directly actionable line and
  restates Claim 1's checking-account/savings-account framing as a concrete
  diagnostic question a team can ask about its own portfolio of AI
  investments. It is the natural pairing for Claim 12: Claim 12 explains why
  teams default to the wrong question, and Claim 13 supplies the replacement
  question.

## Concrete Artifacts

### The checking-account / savings-account metaphor (as stated in prose)

```
Source: Matt Wood, "The Cost of the Answer," mattwood.blog, 2026-07-02
(https://mattwood.blog/essays/2026/07/the-cost-of-the-answer/)

CHECKING ACCOUNT (most teams' current AI investment)
  - Gain proportional to deposit (design effort in)
  - Real value, but a ceiling
  - To gain again: deposit more effort

SAVINGS ACCOUNT (where compounding value lives)
  - Balance itself put to work; interest earns interest
  - Requires: something in the system turns this period's
    balance into next period's growth
  - The dividing line: whether the cost of KNOWING the work
    got better (the cost of the answer) is falling
```

### Four techniques for a cheap AND trustworthy answer (as stated in prose)

```
Source: Matt Wood, "The Cost of the Answer," mattwood.blog, 2026-07-02

LOWER COST
  1. Ask a bounded, comparative question ("does this beat the
     last one?") instead of an unbounded absolute one ("is this good?")
  2. Watch the plateau (shrinking round-to-round changes, or a
     recurring fix) as a free trend signal instead of waiting
     for a defined finish line

RAISE TRUSTWORTHINESS
  3. Require evidence before counting a win: "the specific
     change, the specific result" — makes the check honest,
     not faster
  4. Require a pattern to repeat once before trusting it as a
     lesson — costs one extra round, "buys an answer that is
     harder to fool"
```

### The four-pass strategy-memo example (durable evaluator asset)

```
Source: Matt Wood, "The Cost of the Answer," mattwood.blog, 2026-07-02

Pass 1: Agent drafts the strategy memo.
Pass 2: Evaluator holds draft against a rubric (assumptions
        explicit, options distinct, tradeoffs named).
Pass 3: Evaluator notices the same objection (e.g. weak
        customer evidence) recurring across rounds; starts
        demanding it earlier.
Pass 4: That objection gets written into the STANDING RUBRIC —
        so the next memo, on an unrelated question, faces it
        from the first draft.

Result after a year: "the company has not merely produced
better memos. It has accumulated better strategic taste, held
somewhere that does not walk out the door."
Risk: the standing rubric can ossify (bureaucracy, overfitting
to the last failure, caution disguised as taste) and needs
maintenance — new evidence, new counterexamples, an occasional
reset.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harness-long-running.md` Claim 2 (generator/evaluator
    split "outperforms prompting a single agent to self-critique") and
    Claim 10 (evaluator value is task-relative — worth the cost only where
    the task exceeds solo model capability): this essay's Claim 3 supplies
    the economic mechanism (generation cost collapsed, so evaluator cost is
    now what decides loop economics) for why the generator/evaluator split
    is the right architecture, a claim that post demonstrates empirically
    but does not explain in cost terms.
  - `blog-anthropic-harness-long-running.md` Claim 6 (out-of-the-box
    evaluators rationalize away legitimate issues) and Claim 14 (criteria
    wording steers generator behavior unexpectedly): this essay's Claim 9
    ("show its work," "wait for it to show up twice") generalizes the same
    rationalization risk that post documents empirically in one harness into
    a portable evaluator-design discipline.
  - `blog-ronacher-the-coming-loop.md` Claim 5 (harness loops amplify
    defensive-code accumulation so "the system slowly becomes less
    understandable while appearing more robust"): this essay's Claim 4
    ("an unvalidated loop... can get wronger every round... because it
    looks like progress the whole way down") is the general theoretical
    statement of the exact failure mode Ronacher observed concretely.
  - `blog-langchain-human-judgment-improvement-loop.md` Claim 5 ("teams get
    more leverage when humans help design and calibrate automated
    evaluators, rather than manually reviewing large volumes of agent
    outputs") and Claim 13 (golden datasets as a curated regression
    baseline): both corroborate this essay's Claim 10 that the durable,
    compounding asset is the evaluator/curated-judgment layer, not any
    single agent output.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus source argues that the artifact (rather than the
  evaluator/judgment layer) is the durable compounding asset, or that
  unvalidated loops are safe to run without evaluation — the corpus sources
  reviewed for this note (harness-long-running, the-coming-loop,
  human-judgment-improvement-loop, getting-started-with-loops) are
  consistent with this essay's central claims at varying levels of
  abstraction. No contradiction issue filed.

- **Extends**:
  - `blog-mattwood-field-and-frontier.md` (same author, 2026-06-23): that
    essay's Claim 6 ("the model is a component, and the system is the work")
    argues competitive advantage has moved off the model and onto
    surrounding infrastructure; this essay names *which part* of that
    surrounding infrastructure specifically compounds (the evaluator, not
    routing or orchestration generally) and gives the economic mechanism
    (cost of the answer) for why. Claim 12 here also complements that
    essay's Claim 5 (Forrester: genAI orchestrates <1% of core business
    processes) with a different explanatory mechanism for the same
    under-investment pattern — see Claim 12's "Our assessment" for why this
    is a complementary explanation, not a duplicate claim.
  - `blog-anthropic-getting-started-with-loops.md` Claim 3 (`/goal`'s
    evaluator model checks a user-defined success condition after every
    turn): this essay's Claim 8 (watch the plateau instead of waiting for a
    defined finish line) adds a stop-condition technique for exactly the
    case `/goal` does not cover — open-ended work where no explicit success
    criterion can be defined in advance.
  - `blog-anthropic-harness-long-running.md` Claim 9 (harness components
    encode assumptions that go stale as models improve, and should be pruned
    at each upgrade): this essay's Claim 10 extends that pruning discipline
    with a complementary claim about what to *keep investing in regardless
    of model version* — the evaluator apparatus, as distinct from the
    generator components that pruning targets.

- **Novel**:
  - The "cost of the answer" as the named central economic quantity that
    determines whether AI work compounds or merely accelerates (Claims 1,
    3, 5, 13) — no existing corpus source names this specific quantity as
    the deciding variable, as distinct from cost of compute, cost of tokens,
    or cost of engineering time.
  - The checking-account / savings-account metaphor for compounding vs.
    proportional AI investment (Claim 1) — new framing device for the corpus.
  - The four concrete techniques for making an evaluator answer cheap and
    trustworthy at the same time — bounded comparison, plateau-watching,
    evidence-requiring, twice-repeated-pattern trust (Claims 7-9) — are new,
    portable, non-tool-specific evaluator-design techniques not documented
    elsewhere in the corpus (the corpus's existing evaluator-design guidance,
    e.g. sprint contracts in `blog-anthropic-harness-long-running.md`, is
    tool/task-specific by comparison).
  - Evaluator ossification as a named maintenance risk (Claim 11) — no
    existing source names bureaucratic hardening, overfitting to the last
    failure, or caution-disguised-as-taste as risks specific to a durable
    evaluator asset.
  - The claim that organizations under-invest in evaluators specifically
    because of a budget-visibility asymmetry (throughput visible in week
    one; evaluator value invisible until it compounds) (Claim 12) is a novel
    organizational-behavior explanation not present in the corpus.

## Guide Impact

- **Chapter 01 (Concepts)**: Add "cost of the answer" as core vocabulary
  for what determines whether a loop compounds (Claims 1, 3) — a sharper,
  economics-first framing than the corpus's current definitional coverage
  of loops (`blog-anthropic-getting-started-with-loops.md`), which classifies
  loops by trigger/stop/primitive but does not name the evaluator-cost
  variable as the thing that decides compounding. Pair with Claim 2's
  tightened loop definition (evaluation must feed back into the next round,
  or it is a single pass repeated, however automated).

- **Chapter 02/03 (Harness Engineering / Operationalization)**: Add the four
  cost-lowering/trust-raising evaluator techniques (Claims 7-9: bounded
  comparison, plateau-watching, evidence-requiring, twice-repeated-pattern
  trust) as concrete, portable guidance for designing evaluator prompts,
  alongside the existing sprint-contract and evaluator-tuning guidance from
  `blog-anthropic-harness-long-running.md`. These are lighter-weight and
  more broadly applicable (not tied to a specific SDK or task domain) than
  that post's evaluator-tuning workflow.

- **Chapter 04 (Organizational Patterns)**: Add the "durable evaluator
  asset" framing (Claim 10: the artifact depreciates on ship, the evaluator
  apparatus compounds) as a named argument for why evaluator infrastructure
  investment should be budgeted as a capital asset, not overhead — paired
  with Claim 12's explanation for why organizations currently under-invest
  in it (throughput's payback is visible in week one; the evaluator's is
  not) and Claim 11's maintenance requirement (evaluators need refreshing or
  they ossify into bureaucracy or false caution). This complements
  `blog-mattwood-field-and-frontier.md`'s existing "field vs. frontier"
  organizational-investment framing already flagged for Ch04 with a
  narrower, more specific investment target: not "invest more in the field"
  generally, but "invest specifically in the evaluator/judgment layer."

## Extraction Notes

1. The full article was fetched via WebFetch, which in this case returned
   what appeared to be a complete reproduction of the essay text. Per
   MINER.md §2a, every `Quote` field in this note was independently
   re-verified against a second, separately-parsed source: the raw HTML was
   retrieved directly via `curl` (browser user-agent, HTTP 200) and stripped
   of script/style/markup tags to plain text, then each planned quote was
   located and confirmed character-for-character in that plain text before
   being included in this note.
2. The article contains no outbound hyperlinks and no named data sources,
   statistics, or citations to verify independently — every claim in this
   essay is the author's own conceptual argument or illustrative example,
   which is why every claim here is rated `anecdotal` rather than `emerging`
   or `settled`.
3. No sub-pages were followed beyond the essay itself. The author's About
   page (`https://mattwood.blog/about/`) was not re-fetched for this note
   since it is already fully captured, with direct quotes, in
   `blog-mattwood-field-and-frontier.md` Concrete Artifacts — this note
   cites that existing extraction rather than duplicating it.
4. No contradiction issues filed. See Cross-References → Contradicts for
   the reasoning: this essay's claims corroborate and extend existing
   corpus sources at varying levels of abstraction, and no existing note
   was found to argue the opposite of any claim extracted here.
5. Cross-references to `blog-anthropic-harness-long-running.md`,
   `blog-ronacher-the-coming-loop.md`,
   `blog-langchain-human-judgment-improvement-loop.md`,
   `blog-anthropic-getting-started-with-loops.md`, and
   `blog-mattwood-field-and-frontier.md` were all verified by reading the
   cited claim numbers in the actual source-note files before writing this
   note, per MINER.md §4b.
