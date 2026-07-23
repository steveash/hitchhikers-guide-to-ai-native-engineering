---
source_url: https://cursor.com/blog/router
source_type: blog-post
title: "Introducing Cursor Router"
author: Cursor Team
date_published: 2026-07-22
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2165"
---

# Introducing Cursor Router

> Cursor's product announcement for a learned routing classifier — trained on
> 600k+ live requests and evaluated across millions of live requests via
> online A/B testing rather than offline evals — that assigns each coding
> request to a cost-tier model based on query, context, task complexity, and
> domain, reporting 30–50% cost savings in enterprise early access and 60%
> savings in A/B tests versus an all-frontier-model baseline, with named
> cache-miss-aware training/evaluation and two production quality signals
> (user satisfaction and code "keep rate").

## Source Context

- **Type**: blog-post (Cursor official blog, "product" category, published
  July 22, 2026, 8-minute read, byline "Cursor Team" — no named individual
  author)
- **Author credibility**: First-party vendor product announcement from
  Cursor/Anysphere about Cursor's own commercial routing feature, now
  generally available for Teams and Enterprise plans. Cursor has a direct
  commercial incentive to present favorable results (this is a paid-tier
  feature launch, not a research disclosure), and no methodology section
  discloses how the A/B test was randomized, what the control arm actually
  was beyond "priced entirely at Opus 4.8 API rates," or how "user
  satisfaction (AFC)" is computed beyond the two behavioral proxies named
  (moving to the next feature vs. correcting the agent). No customer names,
  no external audit, no error bars or confidence intervals on any reported
  percentage. Treat all percentage figures as first-party, self-selected,
  and unaudited — same posture as `blog-cursor-agent-swarm-model-economics.md`
  and other first-party Cursor engineering/product posts in the corpus, but
  with less methodological disclosure than that post (which described its
  controlled experiment design, anti-cheating checks, and public code
  artifact in detail; this post discloses none of that for its routing
  classifier or A/B test).
- **Scope**: Covers the product rationale for Cursor Router (developers
  defaulting to one "daily driver" model at frontier prices for routine
  work), the classifier's training/evaluation methodology at a high level
  (600k+ live requests, online A/B across millions of requests, cache-miss
  awareness), the three user-facing modes (Intelligence/Balance/Cost) with
  cost-vs-satisfaction comparisons against Fable, Opus 4.8, and GPT-5.6 Sol,
  early-access enterprise cost-savings figures (including cost-per-commit),
  admin rollout controls, and a forward-looking mention of "dynamic tool
  calling" as a related token-efficiency effort. Does NOT cover: the
  classifier's model architecture, feature engineering, training procedure,
  or evaluation rubric in any technical depth; the actual AFC acronym
  expansion; named enterprise customers; per-mode error/failure-rate data;
  or any case where routing selected a worse model.

## Extracted Claims

### Claim 1: Most Cursor users default to a single "daily driver" model for all tasks, which the company frames as a cost/quality mismatch — routine work is completed at frontier prices even though it doesn't need frontier capability
- **Evidence**: Stated usage-pattern figure with a causal claim about spend growth outpacing output quality.
- **Confidence**: anecdotal (self-reported usage statistic, no methodology for how "daily driver" was defined or measured)
- **Quote**: "Roughly 60% of developers using Cursor pick a single model as their daily driver. This results in routine work being completed at frontier prices, and AI spend growing much faster than output quality."
- **Our assessment**: This is the stated problem motivating the product, not independent evidence of the problem's severity — no baseline is given for what "normal" AI spend growth vs. output quality growth would look like. It is nonetheless a plausible framing consistent with GitHub Copilot's own routing announcements (`docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 1), which independently observe that pre-routing model selection left cost/quality on the table.

### Claim 2: Cursor Router is a classifier trained on 600k+ live requests and evaluated via online A/B testing across millions of live requests, optimizing for a "user satisfaction (AFC)" reward signal rather than an offline eval rubric
- **Evidence**: Direct methodology statement; the acronym "AFC" is used but never expanded or defined anywhere in the post.
- **Confidence**: emerging (specific first-party scale figures for a production system; not independently verifiable, no expansion of AFC, no train/test split or holdout methodology disclosed)
- **Quote**: "At its core, Cursor Router is a classifier that routes users to the best model option based on their query. We trained Cursor Router on 600k+ live requests and evaluated performance in an online A/B test across millions of live requests directed by Cursor Router, optimizing for user satisfaction (AFC) as a reward."
- **Our assessment**: The choice to optimize a classifier against a proxy reward ("user satisfaction (AFC)") rather than ground-truth task success is exactly the setup `blog-cursor-reward-hacking-benchmarks.md` warns is vulnerable to gaming when the proxy and the true objective diverge (Claim 11 there: "the benchmark measures what it claims to measure" — construct validity). This post gives no discussion of how AFC as a reward signal might be gamed by model outputs optimized to *feel* satisfying (e.g., agreeable behavior, premature "done" claims) rather than being genuinely correct — a gap worth flagging rather than a claim we can independently verify either way.

### Claim 3: The classifier routes on four signals — query, context, task complexity, and domain — combined with learned per-model behavior, sending simple work to price-efficient models, UI work to models with "best taste," and complex/long-horizon work to frontier reasoning models
- **Evidence**: Direct description of routing inputs and three example routing outcomes.
- **Confidence**: anecdotal (description of routing logic; no feature importance data, no accuracy/precision figures for the classifier itself, no examples of misrouted requests)
- **Quote**: "Cursor Router analyzes each request on query, context, task complexity, and domain, combined with what we know about each model's behavior. We learn what each model is best at, and route to the most effective option. Simple work goes to the most price-efficient models, UI updates go to the model with the best taste, and more complex, long-horizon problems go to frontier reasoning models."
- **Our assessment**: This is a learned, production-data-trained classifier rather than a rule-based heuristic, which is the key methodological difference from GitHub Copilot's routing. `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 2 names four *fixed* task dimensions (reasoning, code generation complexity, bug diagnosis difficulty, tool orchestration needs) evaluated by an unspecified (likely rule- or prompt-based) mechanism, and `docs-github-copilot-cca-cost-efficient-models.md` Claim 3 is an explicit human-authored heuristic ("use smaller/cheaper models for simple tasks, capable models for complex work"). Cursor's approach — a classifier trained on hundreds of thousands of live requests against a satisfaction reward — is a materially different (and more data-intensive) architecture for the same underlying goal. Neither approach's actual accuracy is independently benchmarked in either corpus, so we cannot say which routes better; we can only say they are different architectures.

### Claim 4: The routing classifier is deliberately designed to be easy to update as new models ship, rather than requiring rearchitecture
- **Evidence**: Direct design-rationale statement.
- **Confidence**: anecdotal (stated design intent; no evidence of how quickly a new model is actually incorporated, e.g. time-to-support for a newly released model)
- **Quote**: "We designed our routing classifier for a world in which updated models get shipped early and often. This way as newer and more powerful models are released, we can easily update Cursor Router, so the experience keeps improving."
- **Our assessment**: This is an unverified design claim (no example given of a new model being added post-launch), but it is consistent with the "model neutrality" positioning stated elsewhere in the post and is the kind of design goal that model-swap-friction sources in the corpus (e.g. the GPT-5.6 Sol prompt-tuning friction documented in `blog-cursor-agent-swarm-model-economics.md` Claim 17) suggest is genuinely hard to achieve in practice — worth treating as an aspiration stated at launch, not a demonstrated capability.

### Claim 5: Cursor Router is cache-aware in both training and evaluation — it is trained on a dataset where routing decisions cause cache misses, and its reported cost savings already include the cost of those cache misses
- **Evidence**: Direct methodology statement distinguishing this from offline-eval limitations.
- **Confidence**: emerging (specific, falsifiable-in-principle methodological claim about what the reported savings figures include, though not independently auditable)
- **Quote**: "Cursor Router is cache-aware in both how it is trained and evaluated. It is trained on a dataset where routing results in cache misses, and evaluated in production where our reported cost savings include the cost of cache misses in routing decisions." / "Offline evals also omit the extra cache-miss cost that comes from switching models. Real routing happens across a conversation: which model to pick, and when to switch."
- **Our assessment**: This is a specific, technically substantive methodological detail — cache-miss cost from switching models mid-conversation is a real and easy-to-hide cost that a naive offline eval (which typically scores single-turn requests in isolation) would miss. Naming this as a design constraint on both training data and evaluation is more concrete than most vendor cost-savings claims in the corpus, which rarely address whether the "savings" figure accounts for switching overhead at all.

### Claim 6: Cursor chose large-scale online A/B testing over offline evals because offline evals are small, distant from real-world usage, and hard to reduce to a rubric
- **Evidence**: Direct methodological justification, contrasting online A/B with offline eval limitations.
- **Confidence**: anecdotal (stated rationale, not a comparison showing offline evals actually failed to predict online results for this specific classifier)
- **Quote**: "We chose to measure the efficacy of our router using large online A/B tests instead of offline evals. While offline evals are useful proxies for quality, they're limited by their small size, their distance from real-world usage, and the difficulty of reducing success to a rubric."
- **Our assessment**: This is a defensible general critique of offline evals, but it also means Cursor Router's headline percentages come with no offline benchmark to cross-check against — the reader has only Cursor's own online A/B numbers and no alternative measurement to compare them to. This is not a red flag on its own (online A/B is a legitimate methodology) but it does mean the claim is unfalsifiable by an outside party without access to Cursor's traffic.

### Claim 7: Two production signals evaluate router quality — "user satisfaction," based on behavioral proxies (moving to the next feature is positive, correcting the agent is negative), and "keep rate," how much agent-generated code remains in the codebase over time — and these same two metrics have been used to evaluate every model launch and harness improvement for the past nine months
- **Evidence**: Direct definition of both metrics plus a claim about their prior usage history.
- **Confidence**: anecdotal (metric definitions given, but no accuracy/reliability data for the behavioral-proxy classifier itself, e.g. false-positive rate for "moving to next feature" as a satisfaction signal)
- **Quote**: "User satisfaction, classifying agent success based on user responses. Moving on to the next feature is a strong positive signal, while correcting the agent is a strong negative one." / "Keep rate, or how much of the agent-generated code remains in the codebase over time." / "We have relied on these metrics to evaluate every model launch and harness improvement in the past nine months."
- **Our assessment**: "Keep rate" (code retention) as an evaluation metric is a genuinely useful outcome-based proxy — it measures whether generated code survives contact with a real codebase rather than just whether it initially compiles or passes a benchmark. It is a narrower, single-vendor version of the "verification over generation" emphasis found elsewhere in the corpus (e.g. `blog-cursor-agent-swarm-model-economics.md` Claim 10 on review as high-return compute), applied here as a measurement tool rather than a harness technique. The claim that these are the metrics behind "every model launch and harness improvement in the past nine months" is asserted without supporting detail and cannot be checked against any other corpus source.

### Claim 8: Auto Intelligence mode matches Fable's user satisfaction at about 60% lower cost, and beats Opus 4.8's satisfaction by about 15% at nearly the same cost; Auto Balance beats Opus 4.8's satisfaction at about 36% lower cost, and matches GPT-5.6 Sol's satisfaction at lower spend
- **Evidence**: Direct comparative percentage claims against three named competing models/tiers (Fable, Opus 4.8, GPT-5.6 Sol).
- **Confidence**: emerging (specific first-party comparative figures against named models, though the underlying satisfaction-scoring methodology is not independently audited and no confidence intervals are given)
- **Quote**: "We found that Auto Intelligence mode lands near Fable on user satisfaction of output at about 60% lower cost for teams, while also lifting satisfaction about 15% over Opus 4.8 at nearly the same cost." / "Similarly, Auto Balance lands above Opus 4.8 on user satisfaction with the results at about 36% lower cost. Against GPT-5.6 Sol, Auto Balance delivers comparable satisfaction at a lower spend rate."
- **Our assessment**: These are the headline quality-vs-cost claims for the two named modes, but they are stated in relative terms only (percentages) without absolute satisfaction scores, so the reader cannot judge whether the underlying satisfaction differences are large or small in absolute terms — "15% over Opus 4.8" could describe a small or large real-world quality gap depending on the scale of the underlying metric, which is not disclosed.

### Claim 9: In early access, three high-volume enterprise accounts (thousands of users each) saved 30–50% on Auto-routed requests versus routing everything to Opus 4.8, with no decrease in quality; cost-per-commit was $6.76 for Intelligence mode and $4.63 for Balance, versus $12.69 for Fable 5 and $7.34 for Opus 4.8, with GPT-5.6 Sol matching Intelligence's cost but at lower user satisfaction
- **Evidence**: Named comparison metric (cost-per-commit, not just cost-per-request) across an early-access cohort of three specific accounts, with a baseline of "priced entirely at Opus 4.8 API rates."
- **Confidence**: emerging (specific dollar figures with a stated comparison baseline; small sample — three accounts — and no customer names, no description of what tasks generated these commits, no disclosure of how "no decrease in quality" was measured beyond the satisfaction/keep-rate metrics described elsewhere)
- **Quote**: "In early access, three high-volume accounts with thousands of users saved 30%–50% on Auto-routed requests versus routing everything to Opus 4.8, with no decrease in quality." / "For a single commit, we observed Cursor Router had a lower cost per commit of $6.76 for Intelligence mode and $4.63 for Balance." / "GPT-5.6 Sol matched the cost of Intelligence but had lower user satisfaction with the output. Meanwhile, Fable 5 and Opus 4.8 produced commits at a cost premium to Cursor Router at $12.69 and $7.34 respectively."
- **Our assessment**: Cost-per-commit is a more outcome-oriented unit than cost-per-request (a request could be cheap but unproductive), which strengthens this claim relative to a pure per-request cost comparison. But the sample is explicitly three accounts, and "with no decrease in quality" is asserted rather than shown with a specific quality delta for this early-access cohort (the mode-level satisfaction percentages in Claim 8 are a separate, larger-scale measurement). This is the single most concrete, guide-citable cost figure in the source: a $12.69-to-$4.63 per-commit spread (roughly 2.7x) between an all-Fable-5 baseline and Cursor Router's Balance mode.

### Claim 10: Cursor Router offers three user-selectable modes on a cost-intelligence Pareto frontier — Intelligence (frontier quality, matching the most expensive models), Balance (matching the frontier models "most people like to daily drive"), and Cost (good quality, optimizing token spend) — and admins control rollout per team/group, including which modes are selectable, the default, and per-model allow/block lists
- **Evidence**: Direct mode definitions plus admin-control feature description.
- **Confidence**: settled (directly observable product feature description, not a performance claim)
- **Quote**: "Intelligence: Frontier quality, with performance matching the most expensive and powerful models that might be out of reach for daily use. Balance: Strong quality, with performance matching the frontier models that most people like to daily drive. Cost: Good quality, reaching the highest available intelligence while optimizing token spend." / "Admins can decide how Cursor Router rolls out across teams. You can enable it per team or group, choose which modes members can select, set the default, and allow or block specific models."
- **Our assessment**: This is a factual product-feature description (what the modes are and how admins configure them), not a claim requiring evidentiary weighing — the "settled" confidence here reflects that it's describing the shipped product surface, not an empirical result. It is the concrete implementation detail a guide section on team-scale model routing infrastructure would need: routing here is not just automatic but bounded by admin policy (allow/block lists, per-team defaults), which is the same governance shape GitHub Copilot's `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 4 describes ("Auto honors all model policies set by administrators").

### Claim 11: Cursor frames model-choice routing as only one piece of overall token efficiency; a second named effort, "dynamic tool calling," lazily loads native tool descriptions into the prompt only on first use (mirroring the existing MCP pattern) rather than loading all tool descriptions into every prompt
- **Evidence**: Forward-looking product description in the "What's next" section.
- **Confidence**: anecdotal (described as an example of ongoing work; no metric given for how much prompt/context space this saves)
- **Quote**: "Dynamic tool calling is another clear example where most native tool descriptions are no longer loaded into every prompt. The model looks them up the first time it needs them, following the same pattern we already use for MCPs. This keeps common tools like read and edit hot while less commonly used tools only enter the prompt when the agent actually calls them."
- **Our assessment**: This is a distinct, concrete context-engineering technique — lazy tool-description loading — that is separate from the model-routing claims that are this post's main subject, but it is novel to the corpus as a named Cursor technique and belongs in a context-engineering discussion of prompt/context budget management rather than in a model-selection discussion. No quantification is given (no token count or percentage reduction), which caps this at anecdotal despite being a specific, plausible mechanism.

## Concrete Artifacts

```
Source: "Introducing Cursor Router," Cursor Team, cursor.com/blog/router, July 22, 2026

HEADLINE COST/QUALITY FIGURES (verbatim from post):
  Early access (dozens of enterprises): ~30-50% lower cost at frontier performance
  Online A/B test (millions of requests): frontier-quality performance at 60% savings
  Auto Intelligence vs. Fable: near-equal satisfaction, ~60% lower cost
  Auto Intelligence vs. Opus 4.8: +~15% satisfaction, ~same cost
  Auto Balance vs. Opus 4.8: above Opus 4.8 satisfaction, ~36% lower cost
  Auto Balance vs. GPT-5.6 Sol: comparable satisfaction, lower spend

COST PER COMMIT (three high-volume early-access accounts, thousands of users each,
vs. all-traffic-at-Opus-4.8-API-rates baseline):
  Cursor Router Intelligence mode:  $6.76
  Cursor Router Balance mode:       $4.63
  Opus 4.8 (baseline):              $7.34
  Fable 5:                          $12.69
  GPT-5.6 Sol:                      matched Intelligence's $ cost, lower satisfaction

THREE MODES:
  Intelligence — "Frontier quality, with performance matching the most
    expensive and powerful models that might be out of reach for daily use."
  Balance — "Strong quality, with performance matching the frontier models
    that most people like to daily drive."
  Cost — "Good quality, reaching the highest available intelligence while
    optimizing token spend."

TRAINING/EVAL METHODOLOGY (as disclosed):
  Training set: 600k+ live requests
  Eval: online A/B test across millions of live requests
  Reward signal: "user satisfaction (AFC)" — acronym not expanded in source
  Cache-aware: trained on data where routing causes cache misses; reported
    savings figures include cache-miss cost
  Routing inputs: query, context, task complexity, domain + per-model
    behavior knowledge

QUALITY METRICS USED (per source, "relied on... for every model launch and
harness improvement in the past nine months"):
  1. User satisfaction — behavioral proxy: next-feature progression = positive
     signal, agent correction = negative signal
  2. Keep rate — proportion of agent-generated code remaining in the
     codebase over time

AVAILABILITY: Teams and Enterprise plans; desktop, web, iOS, CLI, SDK.
ADMIN CONTROLS: per-team/group enablement, selectable-mode restriction,
  default mode, per-model allow/block list.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below,
`docs-github-copilot-cli-auto-model-selection-task-based-routing.md`,
`docs-github-copilot-cca-cost-efficient-models.md`,
`blog-cursor-reward-hacking-benchmarks.md`, and
`blog-cursor-agent-swarm-model-economics.md` were re-read directly
(MINER.md §4b) and every claim number cited below was confirmed against
those notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
    Claim 9 ("GitHub's internal evaluations show gains in token efficiency
    from auto routing with no quality regression"): both this source's
    Claim 9 (30-50% enterprise savings "with no decrease in quality") and
    GitHub's Claim 9 make the same shape of assertion — automatic routing
    saves cost without sacrificing quality — from two independent
    commercial vendors, though neither discloses a methodology strong
    enough to treat the specific percentages as directly comparable to
    each other.
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
    Claim 4 ("Auto honors all model policies set by administrators"): this
    source's Claim 10 (admin-controlled per-team/group rollout, selectable
    modes, allow/block lists) describes the same governance requirement —
    automatic routing at the team/enterprise level needs an admin policy
    layer — independently arrived at by both vendors.
  - `blog-cursor-agent-swarm-model-economics.md` Claim 15 (a ~7.9x total-cost
    spread across model-mix configurations for "similar quality" in
    multi-agent swarm work): this source's Claim 9 (a roughly 2.7x
    cost-per-commit spread between Fable 5 at $12.69 and Cursor Router
    Balance at $4.63) is a smaller but directionally consistent finding —
    both posts, published two days apart by the same company, argue that
    large cost differentials exist between model choices at equivalent
    output quality, though they measure this in structurally different
    contexts (single-request classification-based routing here vs.
    planner/worker role assignment there).

- **Contradicts**: None found. No existing source note makes a claim about
  production-signal-trained routing classifiers that this source's claims
  materially oppose.

- **Extends**:
  - `docs-github-copilot-cca-cost-efficient-models.md` Claim 3 ("use
    smaller/cheaper models for simple tasks, capable models for complex
    work" — a human-authored heuristic): this source's Claim 3 describes a
    materially different mechanism for the same goal — a classifier learned
    from 600k+ live requests rather than a hand-written task-complexity
    rule — extending the corpus's routing coverage from rule-based to
    learned/data-driven routing.
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
    Claim 2 (four fixed task dimensions evaluated by an unspecified
    mechanism): this source's Claim 3 names a comparable but distinct
    input set (query, context, task complexity, domain) and, unlike the
    GitHub source, discloses that the mechanism is a classifier trained on
    production traffic rather than a static rubric — a level of mechanism
    detail the GitHub note does not provide.
  - `blog-cursor-reward-hacking-benchmarks.md` Claim 11 ("the goal of eval
    design is construct validity, not answer correctness"): this source's
    Claim 2 (optimizing a classifier against a "user satisfaction (AFC)"
    reward with no disclosed anti-gaming methodology) is a case where the
    construct-validity concern that source raises for benchmark eval design
    applies equally to a production reward signal used to train a routing
    classifier — this source does not address whether AFC itself is
    resistant to being gamed by model behavior optimized to appear
    satisfying rather than to be correct.

- **Novel**:
  - **Cache-miss-aware classifier training and evaluation** (Claim 5): no
    other corpus source describes training a routing system on a dataset
    where routing itself causes a cost (cache misses from model-switching),
    or explicitly folding that cost into reported savings figures. This is
    a specific methodological detail not present in either GitHub Copilot
    routing note.
  - **"Keep rate" as a named, cross-model, longitudinal evaluation metric**
    (Claim 7): while "verification over generation" and code-survival-style
    concerns appear elsewhere in the corpus (e.g.
    `blog-cursor-agent-swarm-model-economics.md` Claim 10's review-lens
    discussion), no other source names a specific metric ("keep rate") for
    tracking what fraction of agent-generated code persists in a codebase
    over time, or claims it has been used continuously "for every model
    launch and harness improvement" for a specific duration (nine months).
  - **Dynamic tool calling / lazy tool-description loading** (Claim 11):
    novel to the corpus as a named technique — no other source describes
    deferring native tool description loading until first use, distinct
    from (but analogous to) the existing MCP lazy-loading pattern the post
    references.

## Guide Impact

- **Chapter 04 (Model Selection & Tradeoffs)**: Add Cursor Router as a
  second data point (alongside GitHub Copilot's auto model selection,
  `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` and
  `docs-github-copilot-cca-cost-efficient-models.md`) that team-scale model
  routing is moving from static, human-authored heuristics (task dimensions,
  simple/complex tiering) toward classifiers trained directly on production
  traffic and satisfaction signals. Flag explicitly that this source
  provides no comparative accuracy data against the rule-based approach —
  the guide should present both as coexisting strategies, not claim the
  learned classifier is proven superior, since neither corpus source
  benchmarks routing accuracy against a common baseline.

- **Chapter 05 (Cost & Economics)**: Add the cost-per-commit comparison
  ($4.63-$12.69 spread across Balance/Fable 5, roughly 2.7x) as a concrete,
  citable figure for team-scale model-cost-optimization discussions,
  alongside the existing swarm-economics figures from
  `blog-cursor-agent-swarm-model-economics.md` Claim 15. Note for readers
  that both figures are first-party Cursor numbers from the same one-week
  publication window (July 20-22, 2026) and should be treated as
  directionally consistent evidence for "large cost spreads exist between
  model choices at similar quality," not as independently corroborated
  numbers.

- **Chapter 07 (Production Observability)**: Add "keep rate" (code
  retention over time) as a named example of an outcome-based quality
  metric for agent-generated code, distinct from task-completion or
  benchmark-pass metrics, citing this source as the origin. Flag the
  construct-validity gap identified in Cross-References — the guide should
  note that optimizing a routing classifier against a satisfaction/reward
  proxy carries the same gaming risk that
  `blog-cursor-reward-hacking-benchmarks.md` documents for benchmark
  optimization, and this source does not address whether AFC is
  gaming-resistant.

- **Chapter 04 (Context Engineering, if applicable) / Harness Engineering**:
  Add "dynamic tool calling" (lazy-loading native tool descriptions on
  first use, mirroring MCP's existing lazy-load pattern) as a named,
  unquantified technique for reducing per-request prompt/context overhead
  in tool-heavy agent harnesses.

## Extraction Notes

- WebFetch's default AI-summarization pass returned a condensed,
  paraphrased summary of this article rather than verbatim text (same
  limitation documented in `blog-cursor-agent-swarm-model-economics.md`'s
  Extraction Notes and `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`).
  To get quote-accurate text, the article's raw HTML was fetched directly
  via `curl` with a standard browser user agent (HTTP 200), and the full
  article body (all section headings, all body paragraphs, and the author
  byline) was extracted by stripping HTML tags with a Python script that
  preserved block-level line breaks. The page rendered the article body
  twice in the raw HTML (once inside a hidden/duplicate DOM node, likely
  for hydration or SEO purposes) — both copies were identical, confirming
  no truncation or partial rendering. All quotes above were copied
  character-for-character from that extracted text.
- The source is a single, self-contained blog post with no sub-pages beyond
  a "Related posts" list (not followed — unrelated titles: "Build from
  anywhere with Cursor for iOS," "Introducing organizations for Cursor
  Enterprise," "Improvements to Teams Pricing") and references to "our docs
  and changelog" (not linked with a specific URL in the extracted text, so
  not followed).
- The acronym "AFC" (used as the reward signal name, "user satisfaction
  (AFC)") is never expanded anywhere in the source. This is flagged
  explicitly in Claim 2 and the frontmatter confidence rating rather than
  guessed at.
- No customer names are given for the "three high-volume accounts" in
  Claim 9 — only "thousands of users" per account. This caps how
  specifically the guide can cite this figure (no company-level case study
  exists to cross-check).
- No contradiction issue was filed. No existing source note makes a claim
  about production-trained routing classifiers, offline-vs-online eval
  methodology, or cache-miss-aware routing that this source materially
  opposes — the overlaps found are corroborating or extending, not
  contradicting (see Cross-References).
