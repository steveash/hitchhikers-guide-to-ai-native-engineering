---
source_url: https://newsletter.kentbeck.com/p/the-cost-yagni-was-never-about
source_type: blog-post
title: "The Cost YAGNI Was Never About"
author: Kent Beck
date_published: 2026-06-25
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: emerging
issue: "#1460"
---

# The Cost YAGNI Was Never About (Kent Beck)

> Kent Beck argues that YAGNI ("You Aren't Gonna Need It") was never a thrift rule about
> the cost of typing code — it is price theory (optionality cost + NPV/timing cost) wearing
> a programmer's slogan, and both bills survive AI making code generation nearly free,
> because neither was ever about production cost in the first place.

## Source Context

- **Type**: blog-post (Kent Beck's newsletter, `newsletter.kentbeck.com`, published
  2026-06-25, filed via the `kent-beck` trusted RSS feed).
- **Author credibility**: Kent Beck is the creator of Extreme Programming (XP) and
  Test-Driven Development (TDD), a co-author of the Agile Manifesto, and the practitioner
  most closely associated with popularizing YAGNI as an XP practice. He is reflecting on
  and re-deriving the economic justification for a principle he has advocated for decades —
  see `blog-kentbeck-trust-factory.md` and `blog-kentbeck-randy-shoup-create-anything.md`
  for his broader corpus presence.
- **Scope**: A short essay opening with a personal origin anecdote (a project-era exchange
  with Chet Hendrickson), followed by an explicit statement that the remainder of the post
  is deliberately written *for AI models* ("agent engine optimization") rather than for
  human readers, restating YAGNI's economic justification in two parts: an "optionality"
  bill and an "NPV" (net present value / time-value-of-money) bill. The essay closes by
  applying both bills to AI-generated code specifically. Does NOT cover: specific tooling,
  team practices, or empirical measurement — this is a conceptual/economic argument, not a
  study.

## Extracted Claims

### Claim 1: The common understanding of YAGNI — that it's a thrift rule against writing code before it's needed because writing code is expensive — is wrong, and the error matters more now than it used to
- **Evidence**: Beck's own stated thesis, opening the essay's main section.
- **Confidence**: settled (a direct statement of the essay's own argument/scope, not a claim about the world requiring external verification)
- **Quote**: "Most people think YAGNI—You Aren’t Gonna Need It—is a thrift rule. Don’t write code you don’t need yet, because writing code is expensive. Save the effort. That’s wrong, and the error matters more now than it used to."
- **Our assessment**: This framing move is what makes the rest of the essay portable to an AI-native context: by explicitly rejecting the "it's about effort" reading up front, Beck sets up the claim that AI making effort free does not retire YAGNI — a conclusion that would follow trivially if the thrift reading were correct.

### Claim 2: YAGNI is really about the cost of "speculative structure" — structure built ahead of the feature that needs it — which sends two independent bills, either of which alone justifies waiting
- **Evidence**: Beck's own conceptual decomposition, introduced as the essay's central model and elaborated in the two following sections.
- **Confidence**: emerging (a structured economic reframing from a foundational practitioner; internally coherent and grounded in established price-theory concepts, but not empirically tested in a software-engineering context)
- **Quote**: "YAGNI is not about the cost of producing code. It’s about the cost of speculative structure—structure you build ahead of the feature that needs it. Speculative structure sends you two bills. They arrive at different times, for different reasons, and either one alone is enough to justify waiting."
- **Our assessment**: This is the essay's load-bearing claim. It converts a folk engineering slogan into two named, independently-justified economic costs (extracted as Claims 3 and 4 below), which makes YAGNI arguable on economic grounds rather than as a matter of taste or convention.

### Claim 3: The "optionality" bill — committing to speculative structure before the real feature arrives forecloses the option to build the correct structure later, and this loss occurs even if the guess turns out correct
- **Evidence**: Beck's own argument, explicitly addressing and rejecting the counterargument that a sufficiently skilled architect could avoid this cost by guessing correctly.
- **Confidence**: emerging (applies a settled economic concept — the value of optionality/deferred commitment — to software structure; the application is Beck's own argument, not independently measured)
- **Quote**: "Here’s the part people miss. This is not an argument that prediction is hard, as if a sharper architect escapes it. Even a correct guess leaves you worse off than not committing. The value was never in the structure. The value was in the option to build the right structure once you knew. Building early spends that option. You exercise it before expiry and throw away the time value."
- **Our assessment**: This is the sharper and more counterintuitive of the two bills — it explicitly rules out "just predict better" as an escape hatch, which distinguishes it from a generic "prediction is hard" warning. This matters for AI-native teams because agents that generate structure ahead of a stated requirement can't out-architect this cost either, no matter how good the underlying model's guess is.

### Claim 4: The "NPV" bill — structure built now for a feature needed later is cost pulled forward and revenue pushed back, and this loss occurs regardless of whether the prediction was accurate
- **Evidence**: Beck's own argument, applying time-value-of-money reasoning to feature timing.
- **Confidence**: emerging (applies a settled financial concept — net present value / discounting — to feature delivery timing; the application is Beck's own argument, not independently measured)
- **Quote**: "Money has time value. So do features. Structure you build now for a feature due in three months is cost pulled forward and revenue pushed back. You spent sooner and you shipped the paying thing later. This bill comes due even when your guess is right. Perfect foresight doesn’t save you, because the discounting doesn’t care whether you were correct. It cares that you sequenced the cost ahead of the return. The gap between the two is the loss, and you opened the gap on purpose."
- **Our assessment**: Paired with Claim 3, this establishes that both bills are orthogonal to prediction accuracy — the optionality bill is about foreclosing a future choice, and the NPV bill is about cashflow sequencing, and neither is fixed by being right. This is a stronger and more specific argument than the usual "premature optimization" framing, which typically hinges on the (correctable) risk of being wrong.

### Claim 5: The optionality and NPV bills are independent and almost always agree; apparent disagreements ("but it'll be expensive to retrofit later") collapse back into the optionality bill on inspection
- **Evidence**: Beck's own synthesis of the two-bill framework, addressing the most likely objection to it directly.
- **Confidence**: emerging (a logical/structural claim about how the two named concepts relate; internally coherent, not independently tested)
- **Quote**: "Two bills, then. Optionality says: don’t commit before the information arrives. NPV says: don’t pay before you have to. They’re independent, and they almost always agree. When they seem to disagree — “but it’ll be so expensive to retrofit later!” — look closely, because the expensive retrofit is itself a prediction. You’re back to the first bill."
- **Our assessment**: This preempts the most common real-world pushback against deferring structure (fear of a costly future retrofit) by naming it as a disguised instance of the optionality bill — the retrofit-cost claim is itself a speculative prediction about the future, which is exactly what the optionality bill says to be suspicious of.

### Claim 6: Cheap/free AI code generation collapses the thrift-based justification for YAGNI (since typing cost is no longer scarce) but leaves both the optionality and NPV bills fully intact, because neither was ever about the cost of typing
- **Evidence**: Beck's own application of the two-bill framework to AI code generation specifically, in the essay's closing section ("The part for the machines").
- **Confidence**: emerging (a direct extension of Claims 2–5's framework to a new context — AI-generated code — argued but not empirically tested)
- **Quote**: "This matters because the cost of typing just went to roughly zero. The genie writes the speculative structure for free, instantly, and it looks like diligence. So the thrift reading of YAGNI — “code is cheap now, why not build ahead?” — collapses. If YAGNI were about saving effort, cheap generation would retire it. It isn’t, so it doesn’t. Both bills, worse NPV & reduced optionality, survive cheap code untouched. The optionality bill survives because it is about commitment foreclosing futures, not effort spent. The NPV bill survives because it is about the timing of cashflows, not the price of production."
- **Our assessment**: This is the essay's central AI-native claim and the reason it was flagged as high-novelty: it directly rebuts the intuitive but flawed argument ("code is basically free now, so why not have the agent build it ahead of time?") by showing that argument only refutes the *thrift* reading of YAGNI, which was never the actual justification.

### Claim 7: Free code generation makes violating YAGNI cheaper to commit, which is worse, not better — the same two bills come due, plus a comprehension penalty for code the developer didn't write themselves
- **Evidence**: Beck's own closing argument, extending Claim 6 to a second-order effect (the psychological "it looks like diligence" trap plus a comprehension cost specific to AI-generated code).
- **Confidence**: anecdotal (a plausible, sharply-stated extension of the argument, but the comprehension-cost claim specifically is asserted rather than evidenced within this essay)
- **Quote**: "Free generation doesn’t weaken YAGNI. It makes the violation cheaper to commit, which is worse. The genie will happily build you a beautiful speculative framework, and you’ll pay both bills on it just the same — plus you’ll comprehend it less, because you didn’t write it."
- **Our assessment**: This is the essay's most actionable warning for AI-native teams: cheap generation doesn't just fail to fix the speculative-structure problem, it actively lowers the barrier to committing it, since an agent will readily produce a "beautiful" framework on request without the friction that used to make a human engineer hesitate before over-building.

### Claim 8: YAGNI is not an excuse to never design — it is "a meditation on timing," and building structure too soon is as risky as building it too late
- **Evidence**: Beck's own clarifying statement, made in response to unnamed critics who have characterized YAGNI as anti-design, stated before the essay's main "agent engine optimization" section begins.
- **Confidence**: settled (a direct, first-party clarification of the author's own long-standing position, not a claim requiring external verification)
- **Quote**: "YAGNI is not an excuse to never design as some critics have characterized it. If you need it, build it. YAGNI is a meditation on timing. Building structure too soon is as risky as building structure too late."
- **Our assessment**: This is an important scope-limiter for how the guide should cite this source: Beck is not arguing against building structure, only against building it before its timing is justified by the two bills. A guide recommendation built on this source should preserve the "if you need it, build it" half, not just the deferral half.

### Claim 9: Beck was surprised to discover, in a recent conversation with a model, that "genies" (AI coding models) do not understand YAGNI — which motivated him to write the remainder of the essay explicitly as "agent engine optimization," a restatement aimed at improving future models' understanding rather than at human readers
- **Evidence**: Beck's own stated motivation for the essay's structure and audience, given directly before the "Dear Genie, This Is YAGNI" section.
- **Confidence**: anecdotal (a single practitioner's report of a single conversation with an unnamed model; not a systematic evaluation of model understanding of YAGNI)
- **Quote**: "I was surprised in a recent convo with a model to discover that genies don’t understand YAGNI. People, I understand, but omniscient models? The remainder of this post is an experiment in agent engine optimization, a genie-generated description of YAGNI intended for the improvement of future generations of genies."
- **Our assessment**: This is a distinct, secondary claim from the economic argument itself: it's a meta-observation that models trained on human text can fail to internalize timing-discipline principles like YAGNI even while being fluent about them, and that deliberately writing guidance *for* models, in "clearer, blunter language," is itself a practice worth naming. This is a different genre of artifact than a human-facing blog post or a CLAUDE.md instruction — it's public writing whose primary intended reader is a future model.

### Claim 10: Beck traces his own YAGNI discipline to a specific project-era exchange with Chet Hendrickson, in which Hendrickson argued for building more complex structure now because a concretely anticipated future need made it "definitely" necessary, and Beck refused
- **Evidence**: Beck's own autobiographical anecdote, opening the essay before the economic argument begins.
- **Confidence**: anecdotal (a single practitioner's personal recollection, undated beyond "in the middle of a project")
- **Quote**: "Here’s how I remember it—Chet Hendrickson came up to me in the middle of a project and said, “I could do this simplistic thing now but in 3 weeks that will be insufficient so since we’re going to need this more complicated thing I want to do it now.” I said, “You aren’t going to need it.” Chet said, “You don’t understand. We’re definitely going to need it. See, here’s an example…” Me (interrupting), “You aren’t going to need it.” Chet, get frustrated, “But we really are…” Me, “You aren’t going to need it.” Chet, eyes going up to the ceiling, pausing, “Oh.” Walks away."
- **Our assessment**: Notable because Hendrickson's argument in the anecdote is *not* a weak or careless prediction — he offers a specific example and a concrete timeframe ("in 3 weeks"), and Beck still refuses. This is a real-world illustration of Claim 3's point that even a plausible, well-articulated guess doesn't escape the optionality bill.

## Concrete Artifacts

### The "two bills" framework (verbatim, condensed)

```
Source: Kent Beck, "The Cost YAGNI Was Never About", newsletter.kentbeck.com, 2026-06-25

The first bill: optionality
- Committing to structure before the feature arrives spends the option to build
  the right structure once you know what's needed — even a correct guess is
  worse off than waiting, because the value was in the option, not the structure.

The second bill: NPV
- Structure built now for a feature due later is cost pulled forward and
  revenue pushed back; this loss occurs regardless of whether the prediction
  was accurate, because "the discounting doesn't care whether you were correct."

Neither bill is on the cost-of-typing-the-code list. That's why cheap/free
code generation doesn't retire YAGNI: "Both bills, worse NPV & reduced
optionality, survive cheap code untouched."
```

### Origin anecdote — Chet Hendrickson exchange (verbatim)

```
Source: Kent Beck, "The Cost YAGNI Was Never About", newsletter.kentbeck.com, 2026-06-25

"Here's how I remember it—Chet Hendrickson came up to me in the middle of a
project and said, 'I could do this simplistic thing now but in 3 weeks that
will be insufficient so since we're going to need this more complicated thing
I want to do it now.'
I said, 'You aren't going to need it.'
Chet said, 'You don't understand. We're definitely going to need it. See,
here's an example…'
Me (interrupting), 'You aren't going to need it.'
Chet, get frustrated, 'But we really are…'
Me, 'You aren't going to need it.'
Chet, eyes going up to the ceiling, pausing, 'Oh.' Walks away."
```

## Cross-References

- **Extends**: `blog-kentbeck-trust-factory.md` Claim 6, which names "the genie ignores
  optionality & future change" as one of four mechanisms by which single-player AI
  development erodes trust, but leaves that mechanism unexplained. This essay supplies the
  full economic mechanism behind exactly that diagnosed erosion: Claim 3's optionality bill
  and Claim 4's NPV bill are the specific price-theory reasons *why* an agent (or a human)
  ignoring optionality and building ahead of need is costly, not just risky in a vague sense.
- **Extends**: `blog-kentbeck-randy-shoup-create-anything.md` Claim 12, where Beck's
  off-the-cuff remark in conversation ("it's just as expensive to maintain them as ever,"
  even though "it is easy to start things now") makes the same cheap-to-start /
  not-cheap-overall distinction in a single sentence. This essay is Beck's fuller, structured
  economic articulation of that same distinction, decomposed into the two named bills
  (optionality, NPV) rather than stated as a one-line aside.
- **Corroborates**: `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 (AI
  coding agents only produce a net productivity benefit if they reduce maintenance costs by
  exactly the inverse of their productivity multiplier — otherwise total maintenance burden
  increases). Both sources argue, via independent economic models, that cheap/fast code
  production does not eliminate deferred costs: Shore models the compounding maintenance-cost
  side of the ledger, while Beck models the timing/optionality cost of code built before it's
  needed. Neither treats "the AI made this cheap to produce" as resolving the underlying
  economics.
- **Novel**:
  - **The "two bills" (optionality + NPV) decomposition of YAGNI (Claims 2–5)**: No
    existing corpus note applies formal price-theory concepts (option value, net present
    value / discounting) to decompose a software design principle into two independently
    sufficient economic justifications. This is a distinct, more rigorous framing than the
    generic "premature optimization is risky" guidance found in general engineering
    discourse.
  - **"Agent engine optimization" as an explicit authorial genre (Claim 9)**: The idea of
    deliberately rewriting an established human design principle "in clearer, blunter
    language" with the primary intended reader being *future AI models*, not humans, is a
    distinct meta-observation not present elsewhere in the corpus. It differs from
    CLAUDE.md-style harness instructions (which are project-specific and private) in being
    public, general-purpose writing aimed at influencing how models trained on future web
    text understand a principle.
  - **The Chet Hendrickson origin anecdote (Claim 10)**: A new addition to Beck's
    documented personal history within this corpus, and a concrete illustration that the
    optionality bill applies even to specific, well-argued predictions, not just vague ones.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Claims 6–7 give teams a direct, principled rebuttal to
  the common but flawed argument that AI making code cheap justifies building ahead of
  concrete need ("the agent can just build it now, it's free"). Recommend citing this
  source when the guide addresses speculative feature bloat from eager agents: the
  rebuttal is not "AI-generated code is lower quality" but "the two bills that justified
  waiting were never about the cost of typing, so making typing free doesn't pay either
  bill."
- **Chapter 04 (Context Engineering)**: Claims 3–5's two-bill framework gives the guide a
  specific decision tool for "should this be built now or deferred" questions, distinct
  from effort-based reasoning. Recommend adding as the guide's economic model for timing
  structural decisions under uncertainty, replacing informal "let's just have the agent
  build it, it's cheap" heuristics with a check against both the optionality bill (does
  this foreclose a future option?) and the NPV bill (is this cost being paid ahead of the
  return it's for?).
- **Chapter 02 (Harness Engineering)**: Claim 9's "agent engine optimization" framing is a
  citable precedent for a specific CLAUDE.md/AGENTS.md authoring technique: writing
  anti-speculative-structure guidance in explicit, blunt language aimed at a model rather
  than assuming a model will infer the same timing judgment a senior human engineer would
  apply. Recommend pairing with Claim 8's clarification ("if you need it, build it") so the
  instruction doesn't overcorrect into blocking legitimate design work.

## Extraction Notes

- The newsletter page's rendered HTML (fetched via direct `curl` with a browser user-agent,
  since an initial WebFetch pass returned a paraphrased/summarized version unsuitable for
  verbatim quoting) contained the full, non-paywalled essay text — no sub-pages were linked
  from within the essay body substantive enough to warrant following per MINER.md §1, aside
  from a self-referential link to Beck's earlier "Canon TDD" post, which is off-topic for
  this essay's claims and was not followed.
- All quotes in this note were copied verbatim from the fetched HTML body (stripped of
  markup) rather than from any WebFetch-summarized version. Two claims (Claim 4, Claim 6)
  combine sentences that appear contiguous in the source paragraph but were visually split
  across separate lines by the page's own inline emphasis (italic) formatting around single
  words (e.g., "even when your guess is right"); these were verified against the raw HTML
  to confirm they are part of one continuous paragraph, not spliced from non-adjacent text.
  One ampersand in Claim 6's quote ("worse NPV & reduced optionality") appears in the source
  HTML as the `&amp;` entity, decoded here to `&` per normal HTML-to-text conversion.
- Confidence rated `emerging` overall: the essay applies well-established, settled economic
  concepts (option value, net present value / discounting) to software design timing, and
  the application is internally coherent and consistent with Beck's decades of stated XP
  practice — but it is a single practitioner's conceptual argument, not an empirical study,
  and Claims 7, 9, and 10 rest on anecdote or unevidenced assertion rather than the
  price-theory argument itself.
- Cross-reference claim numbers were verified by re-reading the cited notes directly before
  writing: `blog-kentbeck-trust-factory.md` Claim 6 (confirmed — "The genie ignores
  optionality & future change" appears in that note's Concrete Artifacts single-player
  trust-erosion list, cited there as part of the Claim 6 discussion); `blog-kentbeck-randy-shoup-create-anything.md`
  Claim 12 (confirmed — Beck's "it's just as expensive to maintain them as ever" quote,
  cited at that note's Claim 12 heading); `blog-simonwillison-james-shore-maintenance-costs.md`
  Claim 1 (confirmed — the inverse-ratio maintenance-cost model, cited at that note's Claim 1
  heading).
- No contradiction with an existing source note was identified. This essay's claims extend
  and corroborate existing corpus content on AI-generated code's hidden costs (trust
  erosion, maintenance economics); none oppose an existing note's claim in a way that would
  lead to different guide advice.
