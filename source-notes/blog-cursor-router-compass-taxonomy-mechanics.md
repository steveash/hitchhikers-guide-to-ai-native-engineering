---
source_url: https://cursor.com/blog/how-cursor-router-works
source_type: blog-post
title: "How Cursor Router chooses the right model for the task"
author: Connor O'Keefe & Yuri Volkov
date_published: 2026-08-06
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: emerging
issue: "#2546"
---

# How Cursor Router chooses the right model for the task

> A named-author technical follow-up (15 days after Cursor Router's product
> launch) that discloses the actual routing mechanism: a two-stage system —
> Compass, a complexity predictor with a disclosed online accuracy figure
> (96% vs. 71%), and a taxonomy classifier (domains/tasks/modifiers) with a
> named per-model strength table and a formal 75%-uplift-threshold eligibility
> rule — plus a two-stage offline/online evaluation pipeline and updated,
> improved cost/quality figures since launch.

## Source Context

- **Type**: blog-post (Cursor official blog, "research" category — distinct
  from the original launch post's "product" category — published Aug 6,
  2026, 6-minute read, byline "Connor O'Keefe & Yuri Volkov," two named
  individual authors rather than the anonymous "Cursor Team" byline used on
  the July 22 launch post).
- **Author credibility**: First-party vendor engineering post from
  Cursor/Anysphere describing the internal mechanics of their own commercial
  routing feature. Named individual authors and a "research" framing suggest
  more technical ownership than the original marketing-flavored launch post,
  and this post does disclose materially more methodology (a routing
  formula, an explicit eligibility threshold, a two-stage offline/online eval
  pipeline, a named complexity-predictor accuracy figure). It remains
  unaudited: no error bars, no description of how the 96%/71% Compass
  accuracy figures were computed beyond "online," no description of dataset
  composition beyond "hundreds of thousands of turns," and all
  cost/satisfaction percentages are self-reported without independent
  verification. Same posture as `blog-cursor-router-model-classifier.md` —
  treat all percentages as first-party and self-selected — but with
  substantially more disclosed mechanism detail than that post.
- **Scope**: Covers the two-stage routing architecture (Compass complexity
  gate, then a taxonomy classifier for frontier-model selection), the
  training dataset's two outcome variables (Performance, Cost), Compass's
  online validation accuracy, the taxonomy's three dimensions and a
  per-model strength table (Grok, Sol, Opus, Fable), the routing/eligibility
  algorithm (a formula plus a 75% one-sided uplift threshold), the two-stage
  offline-then-online evaluation methodology, and updated cost/satisfaction
  figures as of Aug 6, 2026 (compared to the July 22 launch baseline). Does
  NOT cover: the classifier's underlying model architecture or training
  procedure in ML terms, any named enterprise customer or dollar
  cost-per-commit figure (unlike the original post), any misrouting example
  or failure case, or an expansion of the "AFC" acronym used in the original
  post (this post does not use the term "AFC" at all).

## Extracted Claims

### Claim 1: Cursor Router is explicitly a two-stage system — Compass decides whether a turn needs a frontier model at all, and only if so does a second-stage taxonomy classifier pick which frontier model — built on the premise that model selection should be learned from real developer work rather than benchmark scores
- **Evidence**: Direct architectural description with explicit two-stage framing.
- **Confidence**: emerging (specific architectural claim from the system's own engineers, not independently verifiable, but concrete and falsifiable in principle)
- **Quote**: "Cursor Router is built around the idea that model selection should be learned from how models perform on real developer work, rather than inferred from benchmark scores." / "First, we need to decide whether a turn is simple enough for a price-efficient model. Compass, our complexity predictor, makes this decision. Second, if the turn is more demanding, we need to decide which frontier model is most likely to perform well on that kind of work."
- **Our assessment**: This is the specific mechanism the original launch post (`blog-cursor-router-model-classifier.md` Claim 3) described only at the level of four input signals ("query, context, task complexity, and domain"). This post names the two-stage decomposition explicitly and gives each stage a name (Compass, taxonomy classifier), which is a genuine architectural disclosure the original post lacked.

### Claim 2: The training dataset is built from live Cursor traffic (hundreds of thousands of turns) and captures two outcome variables per turn — Performance (inferred from the user's next action) and Cost (from API pricing and token usage, explicitly including cache-miss costs from model switching)
- **Evidence**: Direct dataset-construction and outcome-variable description.
- **Confidence**: emerging (specific scale and variable definitions from the source; not independently auditable, no description of sampling method beyond "live Cursor traffic")
- **Quote**: "The dataset contains hundreds of thousands of turns sampled across a range of models." / "Performance. We infer performance from what the user does next. Moving on to the next task is a strong positive signal, while correcting the agent is a strong negative one." / "Cost. We calculate cost from API pricing and token usage for that turn. Because the data comes from live traffic, it also captures costs that benchmarks often miss, including cache misses caused by switching models."
- **Our assessment**: "Hundreds of thousands of turns" is consistent with the original post's "600k+ live requests" (Claim 2 in `blog-cursor-router-model-classifier.md`) — not a contradiction, just a rounder restatement. The Performance-signal definition (next-action inference) is verbatim-equivalent to the original post's "user satisfaction" behavioral-proxy definition, but this post never uses the term "AFC" that the original post used for the same concept — see Cross-References.

### Claim 3: Compass was validated online with a disclosed accuracy figure: turns it rated most likely to succeed got a positive performance signal 96% of the time, versus 71% for turns it rated least likely to succeed
- **Evidence**: Specific quantified online validation result for the complexity predictor.
- **Confidence**: emerging (a specific, falsifiable-in-principle number, but first-party and unaudited — no sample size, no confidence interval, no definition of "most likely" / "least likely" bucket boundaries)
- **Quote**: "We evaluated Compass online and confirmed that its scores are strong predictors of user satisfaction. Turns that Compass rated as most likely to succeed received a positive performance signal 96% of the time, while turns it rated as least likely to succeed received one 71% of the time."
- **Our assessment**: This is the single most concrete classifier-accuracy figure disclosed anywhere in the corpus's routing-classifier coverage — neither the original Cursor Router post nor GitHub Copilot's auto-routing docs (`docs-github-copilot-cli-auto-model-selection-task-based-routing.md`) disclose any accuracy number for their routing mechanism. Still, a 96%-vs-71% gap describes relative separation between two score buckets, not a precision/recall figure for the routing decision itself, so it should be cited as "Compass's score correlates with outcome" rather than "Compass is 96% accurate."

### Claim 4: Compass outputs a continuous complexity score between 0 and 1, and the "mode" difference between Auto Balance and Auto Intelligence is implemented as different threshold/budget settings on the same underlying scoring system, not different models or logic
- **Evidence**: Direct mechanism description tying score threshold to mode behavior.
- **Confidence**: settled (a factual description of the shipped mechanism, not a performance claim)
- **Quote**: "In practice, Compass assigns each turn a continuous complexity score between 0 and 1. We set a threshold within that range to determine which turns stay on a price-efficient model and which are upgraded to a frontier model. Lower thresholds keep more traffic on the price-efficient model, while higher thresholds upgrade more often." / "Auto Balance keeps more traffic on the price-efficient path and gives the task router a smaller budget. Auto Intelligence gives the task router more room to select frontier models when the expected performance gain justifies the cost."
- **Our assessment**: This is a specific, guide-citable mechanism detail: the three user-facing modes described in the original post (Claim 10 there) are not three separately trained systems but three parameter settings (threshold + cost budget) applied to one continuous scoring pipeline — a materially more concrete architectural fact than the original post's mode descriptions, which were framed only in outcome terms ("frontier quality" vs. "strong quality" vs. "good quality").

### Claim 5: The taxonomy classifier scores each turn across three learned dimensions — domains (backend, database schemas, frontend), tasks (fixing bugs, running commands, writing tests), and modifiers (bounded edits, product questions, visual-heavy changes)
- **Evidence**: Direct taxonomy definition with named example categories per dimension.
- **Confidence**: emerging (specific structural claim; the post gives only 2-3 examples per dimension, not the full category list, so we can't assess how granular the true taxonomy is)
- **Quote**: "Domains identify where the work happens: backend, database schemas, frontend" / "Tasks identify what the developer wants done: fixing bugs, running commands, writing tests" / "Modifiers capture characteristics that cut across domains and tasks, but may change which model performs best: bounded edits, product questions, visual-heavy changes"
- **Our assessment**: This extends the original post's four-signal description ("query, context, task complexity, and domain," Claim 3 in `blog-cursor-router-model-classifier.md`) into a concrete three-dimensional label taxonomy. Structurally similar in spirit to GitHub Copilot's four fixed task dimensions (`docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 2: reasoning, code generation complexity, bug diagnosis difficulty, tool orchestration needs), but Cursor's dimensions are explicitly framed as "learned from real developer traffic" rather than human-authored a priori categories.

### Claim 6: No single model dominates every task category — Cursor found each of four named frontier/routine models has distinct strengths: Grok on low-cost routine work (Git commands, general database operations), Sol on planning and codebase comprehension (plus strong, cheaper results on several implementation tasks), Opus on execution-heavy work (devops, database queries, performance optimization), and Fable on debugging and visual implementation (justifying its higher cost on complex tasks)
- **Evidence**: Direct per-model comparative findings across the taxonomy's categories.
- **Confidence**: anecdotal (qualitative strength claims per model; no quantified per-category win-rate or score is given for any of the four models)
- **Quote**: "We found that no model dominates every kind of work, and each has categories where it outperforms" / "Grok offers strong value across broad, routine work. Its low inference cost made it especially effective for categories such as Git commands and general database operations." / "Sol performs especially well on planning and codebase comprehension." / "Opus performs well on execution-heavy work. It showed particular strengths in devops, database queries, and performance optimization." / "Fable excels at debugging and visual implementation. Its quality gains were most valuable on complex tasks where they justified its higher cost."
- **Our assessment**: This is novel to the corpus — no other source names which specific frontier model is empirically best at which task category from a vendor's own production routing data. It is qualitative (no numbers per model/category), so it should be cited in the guide as "Cursor observed distinct per-model strength profiles" rather than as ranked, quantified performance data.

### Claim 7: A candidate frontier model becomes eligible for a task category only if it clears a one-sided 75% uplift threshold against the price-efficient baseline model (roughly 75% confidence the improvement is real); the optimizer then picks the traffic-weighted mix of eligible models that maximizes performance within the mode's cost budget
- **Evidence**: Direct algorithmic description of the eligibility rule and the subsequent optimization step, plus an explicit routing formula.
- **Confidence**: emerging (a specific, technically substantive decision rule; not independently auditable, no description of how "observed performance" is estimated per task label — sample size per label, statistical test used, etc.)
- **Quote**: "Only route when performance is clearly better. A candidate model becomes eligible only when its observed performance on that task label clears a one-sided 75% uplift threshold against the price-efficient model. Roughly, this means we need 75% confidence that the improvement is real." / "Choose the best mix within the budget. From the eligible candidates, the optimizer chooses the traffic-weighted combination expected to deliver the largest performance gain while keeping the average cost per turn within the mode's budget."
- **Our assessment**: This is the most concrete decision-rule disclosure in the corpus's model-routing coverage — a named statistical threshold (75% one-sided uplift) plus a named optimization objective (traffic-weighted mix under a cost budget), versus the original post's and GitHub Copilot's routing notes, both of which describe routing only in terms of input signals, not the decision rule applied to those signals.

### Claim 8: Cursor evaluates routing policies in two stages — offline cross-validation and a held-out test set to screen candidates before deployment, then online live-traffic testing as the final validation — because offline evaluation cannot capture production-only effects like caching and model-switching costs
- **Evidence**: Direct description of the evaluation pipeline's two stages and the stated rationale for the second (online) stage.
- **Confidence**: settled (a factual methodology description, consistent with and more detailed than the original post's methodology statement)
- **Quote**: "We evaluated our routing policies in two stages. First, we used cross-validation to tune the Compass thresholds and optimization budgets without overfitting to a particular split. We then evaluated the selected policies on a held-out test set that had not been used during training." / "But offline analysis still cannot fully capture how a policy will behave in production, and benchmarks are limited for the same reason. Live developer traffic remains the most representative test." / "We then tested the policies on live traffic, where we could measure user satisfaction and the actual cost of each turn under production conditions. This captures effects that are difficult to model offline, including token usage, caching, and the cost of switching between models."
- **Our assessment**: This directly answers the Prospector's triage question about "decision trees" and methodology beyond the original announcement. The original post (`blog-cursor-router-model-classifier.md` Claim 6) stated only that Cursor "chose" online A/B over offline evals; this post clarifies that offline evaluation is still used, but only as a pre-deployment screening step feeding into online validation, not as a replacement for it — a more complete and more defensible methodology than the original post implied.

### Claim 9: As of Aug 6, 2026, Auto Intelligence delivers above-Fable-level satisfaction at 68% lower cost (an 18% further reduction since the July 22 launch), and Auto Balance outperforms Opus 4.8 at 41% lower cost (an 8% further reduction) while further increasing satisfaction by 3% over the same period
- **Evidence**: Updated headline cost/satisfaction figures, explicitly framed as improvements over the launch-time baseline.
- **Confidence**: emerging (specific first-party comparative figures, framed as deltas from an earlier first-party figure; no absolute satisfaction scores or sample sizes given, same limitation as the original post's Claim 8)
- **Quote**: "Today, Auto Intelligence delivers above Fable-level user satisfaction at 68% lower cost, a further 18% reduction since its launch. Auto Balance outperforms Opus 4.8 at 41% lower cost, a further 8% reduction over the same period, while further increasing user satisfaction by 3%."
- **Our assessment**: These figures update, and are directionally consistent with, the original post's launch-time figures (Auto Intelligence ~60% lower cost vs. Fable; Auto Balance ~36% lower cost vs. Opus 4.8 — `blog-cursor-router-model-classifier.md` Claim 8). Framed as "a further X% reduction," the numbers describe continued improvement rather than a one-time launch result, which is the specific piece of evidence the Prospector's triage question asked for. See Cross-References for why this is treated as an update, not a contradiction.

### Claim 10: Since launch, Cursor added Opus 5 to the routing pool and improved Compass's predictions; the stated long-term goal is a router that predicts each model's expected quality and cost, learns continuously from production outcomes, and updates without a discrete retraining cycle
- **Evidence**: Direct statement of post-launch changes and forward-looking design goal.
- **Confidence**: anecdotal (stated intent and one concrete example — adding Opus 5 — but no metric for how quickly it was incorporated or what "continuously updating" means operationally)
- **Quote**: "Since launching Cursor Router, we've added Opus 5 to the routing mix and improved Compass's predictions." / "Over time, we want the router to become more adaptive by predicting each model's expected quality and cost, learning from production outcomes, and updating continuously."
- **Our assessment**: This is direct evidence for the original post's Claim 4 design intent ("designed our routing classifier for a world in which updated models get shipped early and often") — Opus 5 being added within roughly two weeks of launch is the first concrete example in the corpus of that stated design goal being exercised, though still without a disclosed time-to-support metric.

## Concrete Artifacts

```
Source: "How Cursor Router chooses the right model for the task,"
Connor O'Keefe & Yuri Volkov, cursor.com/blog/how-cursor-router-works,
Aug 6, 2026 (research category; ~2 weeks after the July 22, 2026 launch post)

ROUTING FORMULA (as rendered in source):
  route(x) = price-efficient model,  if Compass(x) < threshold
             task router,            if Compass(x) >= threshold

EVALUATION PIPELINE (two stages, as disclosed):
  1. Offline: cross-validation to tune Compass thresholds + optimization
     budgets, then a held-out test set (not used in training) for
     candidate screening
  2. Online: live-traffic A/B testing for final validation — measures
     user satisfaction and actual cost under production conditions,
     including caching and model-switching costs offline eval misses

TAXONOMY (three dimensions, examples as given — not exhaustive):
  Domains:    backend, database schemas, frontend
  Tasks:      fixing bugs, running commands, writing tests
  Modifiers:  bounded edits, product questions, visual-heavy changes

MODEL ELIGIBILITY RULE:
  A candidate frontier model is eligible for a task label only if its
  observed performance clears a one-sided 75% uplift threshold against
  the price-efficient baseline ("~75% confidence the improvement is real").
  Optimizer then picks the traffic-weighted mix of eligible models that
  maximizes performance within the mode's cost budget.

PER-MODEL STRENGTHS (qualitative, no per-category scores given):
  Grok  — routine, low-cost work; Git commands, general DB operations
  Sol   — planning, codebase comprehension; strong + cheaper on several
          implementation tasks
  Opus  — execution-heavy work; devops, DB queries, performance
          optimization
  Fable — debugging, visual implementation; higher cost justified on
          complex tasks

COMPASS VALIDATION:
  Positive performance signal rate for turns Compass rated "most likely
  to succeed": 96%
  Positive performance signal rate for turns Compass rated "least likely
  to succeed": 71%

HEADLINE FIGURES, LAUNCH (Jul 22, 2026) vs. TODAY (Aug 6, 2026):
                          Launch (per original post)   Today (per this post)
  Auto Intelligence vs.
    Fable, cost delta:    ~60% lower                   68% lower (+18% further)
  Auto Balance vs.
    Opus 4.8, cost delta: ~36% lower                   41% lower (+8% further)
  Auto Balance vs.
    Opus 4.8, satisfaction: "above" (unquantified)      +3% further increase

POST-LAUNCH CHANGES: added Opus 5 to routing pool; improved Compass
  predictions. Stated long-term goal: router that predicts per-model
  quality/cost, learns from production outcomes, updates continuously.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-cursor-router-model-classifier.md`,
`docs-github-copilot-cli-auto-model-selection-task-based-routing.md`, and
`docs-github-copilot-cca-cost-efficient-models.md` were re-read directly
(MINER.md §4b) and every claim number cited below was confirmed against
those notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-cursor-router-model-classifier.md` Claim 5 (cache-aware training
    and evaluation, including cache-miss costs in reported savings): this
    source's Claim 2 independently restates the same design point ("it also
    captures costs that benchmarks often miss, including cache misses
    caused by switching models") as part of the dataset's Cost outcome
    variable, and Claim 8 restates it again as a reason live-traffic
    testing is necessary. Same underlying claim, told from the data-pipeline
    side rather than the results side.
  - `blog-cursor-router-model-classifier.md` Claim 7 (behavioral-proxy
    "user satisfaction" definition: next-feature progression is positive,
    correction is negative): this source's Claim 2 gives a verbatim-
    equivalent definition under the name "Performance" instead of "user
    satisfaction (AFC)."
  - `blog-cursor-router-model-classifier.md` Claim 9 (30-50% enterprise
    cost savings "with no decrease in quality"): this source's Claim 9
    (68%/41% cost reductions with satisfaction gains) is a later, larger
    figure in the same direction, from the same underlying system.

- **Contradicts**: None found, but flagging one point for the Assayer to
  weigh: the original post used the term "user satisfaction (AFC)" for its
  reward signal (Claim 2 in `blog-cursor-router-model-classifier.md`); this
  post never uses "AFC" and instead names the same behaviorally-defined
  metric "Performance." The definitions given for the two terms are
  identical (next-action progression = positive, correction = negative), so
  this reads as a terminology change/simplification between the two posts
  rather than a substantive disagreement — not filed as a contradiction
  issue. Similarly, the improved cost/satisfaction percentages in Claim 9
  (68%/41% vs. the original ~60%/36%) are explicitly framed by the source
  itself as "a further X% reduction since launch," i.e. an acknowledged
  update over time on the same metric, not two different first-party
  figures for the same point in time — also not a contradiction.

- **Extends**:
  - `blog-cursor-router-model-classifier.md` Claim 3 (four input signals:
    query, context, task complexity, domain): this source's Claim 1 and
    Claim 5 name the actual two-stage architecture (Compass, then a
    taxonomy classifier) and the taxonomy's three concrete dimensions
    (domains, tasks, modifiers) that operationalize those signals — the
    mechanism the original post described only abstractly.
  - `blog-cursor-router-model-classifier.md` Claim 6 (stated preference for
    online A/B over offline evals, because offline evals are "limited by
    their small size, their distance from real-world usage, and the
    difficulty of reducing success to a rubric"): this source's Claim 8
    clarifies that offline evaluation (cross-validation + held-out test) is
    still used as a pre-deployment screening stage feeding into online
    validation, not bypassed entirely as the original post's phrasing could
    imply.
  - `blog-cursor-router-model-classifier.md` Claim 10 (three modes described
    only in outcome terms: "frontier quality," "strong quality," "good
    quality"): this source's Claim 4 discloses the actual mechanism behind
    the modes — a shared continuous 0-1 Compass score with a per-mode
    threshold and cost budget, not three separately built systems.
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
    Claim 2 (four fixed, human-named task dimensions evaluated by an
    unspecified mechanism): this source's Claim 5 names a comparable but
    distinct three-dimension taxonomy (domains, tasks, modifiers)
    explicitly described as "learned from real developer traffic" rather
    than human-authored, and Claim 7 discloses an actual decision rule (75%
    uplift threshold + budget-constrained optimizer) that the GitHub note
    does not disclose for its own routing mechanism.

- **Novel**:
  - **Compass as a named, separately-evaluated complexity predictor with a
    disclosed online accuracy figure** (Claim 3): no other source in the
    corpus names a specific sub-component of a routing system or discloses
    a quantified accuracy figure (96% vs. 71%) for it.
  - **Named per-model task-category strength findings** (Claim 6): no other
    corpus source states which specific frontier model (Grok, Sol, Opus,
    Fable) is empirically strongest at which task category, based on a
    vendor's own production routing data.
  - **A disclosed statistical eligibility rule for routing** (Claim 7): the
    "one-sided 75% uplift threshold" and traffic-weighted, budget-
    constrained optimizer is the most concrete routing decision rule
    disclosed anywhere in the corpus's model-routing coverage.
  - **Two-stage offline/online evaluation pipeline, explicitly sequenced**
    (Claim 8): novel level of methodological detail — cross-validation and
    a held-out test set as a pre-screening stage before online A/B testing,
    rather than either method alone.
  - **A concrete post-launch improvement trajectory on the same metrics**
    (Claim 9, Claim 10): this is the first source in the corpus to show a
    vendor's routing-classifier cost/quality figures measured twice, two
    weeks apart, with an explicit account of what changed in between (added
    Opus 5, improved Compass) — direct evidence that a production routing
    classifier is iterated on rather than shipped once and left static.

## Guide Impact

- **`guide/02-harness-engineering.md`**: The two-stage routing architecture
  (Compass complexity gate → taxonomy classifier for frontier-model
  selection), the disclosed 75% one-sided uplift eligibility rule, and the
  two-stage offline/online evaluation pipeline (Claims 1, 7, 8) are
  concrete enough to cite as a worked example of production model-routing
  mechanics, alongside the existing `blog-cursor-router-model-classifier.md`
  citation. Recommend adding this as the "how it actually works" companion
  to that note's "what it does" framing — the guide should distinguish the
  product-level description (modes, cost savings) from the mechanism-level
  description (score threshold + eligibility rule) this source adds.

- **`guide/04-context-engineering.md`**: If the guide discusses model
  selection as a category of context/resource-management decision, the
  named per-model strength table (Claim 6: Grok for routine/low-cost, Sol
  for planning/comprehension, Opus for execution-heavy work, Fable for
  debugging/visual work) is a citable, if qualitative, example of
  task-to-model matching heuristics observed in production — with the
  explicit caveat that "no model dominates every kind of work" and no
  per-category win-rate is disclosed.

- **Cost/economics discussion (wherever the guide covers it, e.g. within
  `02-harness-engineering.md` or `05-team-adoption.md`)**: Update any
  citation of the original post's launch-time cost figures (~60% lower cost
  for Auto Intelligence, ~36% for Auto Balance) with this source's Aug 6,
  2026 figures (68% and 41% respectively, both explicitly framed as further
  improvements since launch — Claim 9). Recommend citing both figures
  together as evidence of a continuous-improvement trajectory, not just the
  more recent number in isolation, since that trajectory (not just the
  endpoint) is the more guide-relevant fact.

## Extraction Notes

- WebFetch's default AI-summarization pass returned a condensed,
  paraphrased, and in places inaccurate summary of this article (it
  invented section names and figures not present in the source, e.g. citing
  "41% reduced expense while increasing satisfaction by 3%" as if it were a
  static result rather than a "further reduction since launch," and never
  named "Compass" clearly as the complexity predictor's actual name). Same
  limitation previously documented in `blog-cursor-router-model-classifier.md`'s
  Extraction Notes. To get quote-accurate text, the article's raw HTML was
  fetched directly via `curl` with a standard browser user agent (HTTP 200),
  and the article body was extracted by stripping HTML tags while
  preserving block-level line breaks. The page rendered the article body
  twice in the raw HTML (duplicate DOM nodes, likely for hydration/SEO) —
  both copies were identical, confirming no truncation. All quotes above
  were copied character-for-character from that extracted text.
- The source is a single self-contained blog post. It links to "our docs"
  (no specific URL given in the extracted text, so not followed) and lists
  three "Related posts" — `blog-cursor-agent-swarm-model-economics.md`'s
  source (already in the corpus), `blog-cursor-cloud-agent-dev-environments.md`
  or a close variant (already in the corpus, "How we set up our cloud agent
  environment"), and a "Grok 4.5 Model Card" 1-minute post not followed
  because it is a model-card summary unlikely to add routing-specific
  detail relevant to this issue's triage question.
- The routing formula in the source is rendered as a LaTeX-style piecewise
  function in the page; it has been transcribed in the Concrete Artifacts
  section using its literal branch conditions (Compass(x) < threshold vs.
  >= threshold) rather than reproducing the source's raw LaTeX markup,
  which did not render cleanly through HTML-stripping.
- No customer names, dollar figures, or per-account cost-per-commit data
  appear in this post (unlike the original launch post's three-account,
  $/commit figures) — this post is about mechanism and aggregate
  cost/satisfaction percentages only.
- A contradiction issue was considered but not filed: the "AFC" →
  "Performance" naming change and the 60%/36% → 68%/41% figure updates are
  both addressed directly in Cross-References as non-contradictory
  (terminology simplification and an explicitly-framed metric update over
  time, respectively). Neither one is two first-party sources disagreeing
  about the same point in time.
