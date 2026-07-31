---
source_url: https://openai.com/index/a-scorecard-for-the-ai-age
source_type: blog-post
title: "A scorecard for the AI age"
author: Sarah Friar
date_published: 2026-07-17
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: anecdotal
issue: "#2358"
---

# A Scorecard for the AI Age

> OpenAI post, bylined to Sarah Friar (no title stated on the page), proposing
> "Useful Intelligence per Dollar" as a named four-dimension scorecard for AI
> value (useful work done, cost per successful task, dependability, value at
> scale), including an explicit
> cost-per-successful-task formula and a three-outcome dependability
> taxonomy (ready to use / needs correction / needs escalation) — framing
> that formalizes, three days later, the "useful work per dollar" language
> OpenAI introduced in `blog-openai-managing-ai-investments-agentic-era.md`.
> Concrete evidence is thin: one benchmark comparison (DeepSWE v1.1: GPT‑5.6
> Sol 72.7% vs. Claude Fable 5's 69.9%, at 36.2% lower estimated API cost);
> everything else is unexemplified conceptual framework.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`, category
  "Company," published July 17, 2026; auto-discovered via the trusted
  `openai-news` RSS feed). A first-person executive op-ed structured as an
  intro plus four numbered sections, each answering one of the scorecard's
  four questions, closing with a "Compute sits at the center" argument tying
  the framework back to OpenAI's own infrastructure investment.
- **Author credibility**: Bylined to Sarah Friar (confirmed via the page's
  own "Author" byline field, extracted separately from the body text). The
  post's own text is explicitly written in her voice as OpenAI's finance
  contact point for enterprise customers — "The question I hear from CFOs
  everywhere is simple: how do we get more value from our AI spend?" — but
  no title or role is stated on the page itself; this note does not assert
  a title beyond what the source discloses. Whatever her role, the post is
  first-party OpenAI content: no named customer, no disclosed methodology
  for any formula or category, and one benchmark chart as the only
  quantified evidence. It reads as executive framing for OpenAI's own
  enterprise product line (GPT‑5.6 tiers, ChatGPT Work, ChatGPT Enterprise
  are all mentioned as the implementation of the framework), not as an
  independent or audited study.
- **Scope**: Covers a four-dimension value framework (useful work done, cost
  per successful task, dependability, value at scale), an explicit
  cost-per-successful-task calculation method, the GPT‑5.6 Sol/Terra/Luna
  tier lineup as a customer-facing embodiment of the cost/capability
  tradeoff, one named coding benchmark (DeepSWE v1.1), a three-outcome
  dependability taxonomy, and a closing compute/infrastructure argument.
  Does NOT cover: any named customer's measured ROI, a worked numeric
  example of the cost-per-successful-task formula, pricing figures for any
  product, or any detail on how "needs correction" vs. "needs escalation"
  would be logged or measured in a real system.

## Extracted Claims

### Claim 1: OpenAI proposes "Useful Intelligence per Dollar" as the ultimate AI-age scorecard, defined by four questions — whether AI is completing work that matters, what each successful task costs, whether people can depend on the result, and whether each AI dollar produces more value as usage grows
- **Evidence**: The article's central framing statement, positioned after the opening CFO-value question and before the four numbered sections that each answer one question.
- **Confidence**: anecdotal (a named framework proposed by the author with no worked numeric example anywhere in the post; the four questions are asserted, not derived from data)
- **Quote**: "The ultimate scorecard for the age of AI could be looked at as “Useful Intelligence per Dollar.” This metric answers four key questions:"
- **Our assessment**: This is the first source in the corpus to give the "measure outcomes, not token price" idea a specific, capitalized, brandable name ("Useful Intelligence per Dollar") with four named sub-dimensions. It reads as a formalization, three days later, of the looser "useful work per dollar" phrase already documented in `blog-openai-managing-ai-investments-agentic-era.md` Claim 2 — same company, same core idea, now packaged as a named scorecard rather than a single sentence of advice.

### Claim 2: What matters for AI value is the full cost of producing a successful outcome — not the price per token — because a cheaper model may need more attempts, time, or human review while a pricier model may complete the task in one pass
- **Evidence**: The article's pivot paragraph, immediately preceding the four-question framework in Claim 1.
- **Confidence**: anecdotal (prescriptive framing claim; no worked comparison of "full cost" vs. "token price" for any specific task is given)
- **Quote**: "What matters is the full cost of producing a successful outcome, measured against the value that outcome creates."
- **Our assessment**: Directly corroborates `blog-openai-managing-ai-investments-agentic-era.md` Claim 4 (lowest token price does not always produce the lowest total cost) — same argument, same company, three days earlier. The two posts are close enough in wording and timing that they likely share an internal source document; citing both together would be redundant unless the guide specifically wants to show the argument being restated and formalized across two consecutive OpenAI posts.

### Claim 3: The cost-per-successful-task calculation is a three-step formula — add the full cost of completing the work, count the tasks that met the required quality bar, and divide the total cost by the number of successful tasks
- **Evidence**: Explicit numbered/bulleted method, given directly under the "What does a successful task actually cost?" section heading.
- **Confidence**: anecdotal (a named formula with no worked numeric example — no sample cost figures, task counts, or quality-bar definition are given anywhere in the post to actually run the calculation)
- **Quote**: "The calculation is straightforward: Add the full cost of completing the work. Count the tasks that met the required quality bar. Divide the full cost by the number of successful tasks."
- **Our assessment**: This is the single most concrete, guide-usable artifact in the post, and it directly fills a gap flagged in `blog-openai-managing-ai-investments-agentic-era.md`'s own Source Context ("Does NOT cover: ... a technical description of how 'cost per accepted outcome' should actually be computed"). That July 14 post asserted the principle ("track cost per accepted outcome") without a method; this July 17 post supplies the actual three-step arithmetic, even though it still stops short of a worked numeric example. Worth citing as the more complete of the two OpenAI sources on this specific point.

### Claim 4: The lowest price per token does not always produce the lowest cost per outcome — a frontier model can deliver the best value even for a routine request if it produces the right answer in one pass, reducing retries, latency, review, and total compute
- **Evidence**: Direct restatement of the article's core economic argument, immediately following the cost formula in Claim 3.
- **Confidence**: anecdotal (prescriptive claim; no data on how often a pricier model actually wins on total cost is given)
- **Quote**: "This is why the lowest price per token does not always produce the lowest cost per outcome. A frontier model may deliver the best value even for a routine request if it produces the right answer in one pass, reducing retries, latency, review, and total compute."
- **Our assessment**: This sits in the same tension already flagged in `blog-openai-managing-ai-investments-agentic-era.md`'s Cross-References → Contradicts section: Vercel's production-index data (cited there, not re-verified in this extraction) shows aggregate coding-agent traffic still routing heavily to the cheapest available model. This note does not re-file that tension as a new contradiction — it is the same normative-vs-descriptive gap already surfaced against the July 14 post, now restated by the same company three days later with no new descriptive evidence attached.

### Claim 5: GPT‑5.6 ships as a three-tier family — Sol (flagship), Terra (balances performance and cost), and Luna (fastest, most affordable) — letting customers match model choice to a workflow's specific cost/capability economics rather than defaulting to one tier for everything
- **Evidence**: Direct product description in the "What does a successful task actually cost?" section, presented as the practical embodiment of the cost-per-outcome argument (Claims 3-4).
- **Confidence**: emerging (a factual, checkable product-lineup description, though the specific claim of which tier suits which workflow type is prescriptive guidance rather than a measured finding)
- **Quote**: "A tiered model family gives customers more ways to optimize this equation. GPT‑5.6, which we released last week, has three tiers: Sol is our flagship; Terra balances performance and cost; Luna is our fastest and most affordable model."
- **Our assessment**: Consistent with the GPT‑5.6 tier lineup already documented in `blog-openai-gpt56-ga-announcement.md` (whose Claim 5 names the same Sol/Terra/Luna tiers with efficiency multipliers against Claude Fable 5 and Opus 4.8). This post adds no new tier-level detail beyond what that note already covers; it restates the lineup as context for the cost-per-outcome argument rather than as new product information.

### Claim 6: On the Artificial Analysis Coding Agent Index, GPT‑5.6 Sol with max reasoning set a new state of the art while using 54% fewer output tokens than another (unnamed) leading model
- **Evidence**: Benchmark claim in the "What does a successful task actually cost?" section, immediately preceding the DeepSWE v1.1 chart caption (Claim 7).
- **Confidence**: emerging (a specific, quantified vendor-reported benchmark figure, though the competing model is not named in this source and the underlying benchmark run is not independently linked)
- **Quote**: "We trained GPT‑5.6 to get more useful work from every token. On the Artificial Analysis Coding Agent Index, GPT‑5.6 Sol with max reasoning set a new state of the art while using 54% fewer output tokens than another leading model."
- **Our assessment**: The unnamed "another leading model" and the 54%-fewer-output-tokens figure both exactly match the ambiguous statistic already flagged in `blog-openai-managing-ai-investments-agentic-era.md` Claim 1 (which cited "54% fewer output tokens" on the same index without specifying whether the comparison was against OpenAI's own prior models or a competitor, and rated that ambiguity as a reason for its own anecdotal confidence). Read alongside `blog-openai-gpt56-ga-announcement.md` Claim 5 — which explicitly names Claude Fable 5 and states GPT‑5.6 Sol on the same Artificial Analysis Coding Agent Index uses "less than half the output tokens" than Fable 5 — this suggests the 54% figure in both OpenAI posts is more likely the same Fable-5-relative statistic than a self-comparison against prior GPT generations. This note treats that as a plausible inference, not a settled fact, since "another leading model" is still unnamed here too; the guide should not cite this passage as confirmation of which model is being compared without flagging the ambiguity.

### Claim 7: On DeepSWE v1.1, a long-horizon engineering-tasks benchmark, GPT‑5.6 Sol reaches a new high of 72.7%, above Claude Fable 5's 69.9%, at 36.2% lower estimated API cost
- **Evidence**: A chart caption directly below the Artificial Analysis Coding Agent Index claim (Claim 6), the article's single most specific quantified data point.
- **Confidence**: emerging (a specific, named-benchmark, named-competitor figure with a precise percentage-point margin and cost delta, though it is vendor-reported and not independently reproduced, and the chart's underlying data table was not recoverable from the reader-proxy text extraction — only the caption)
- **Quote**: "DeepSWE v1.1: Long-horizon engineering tasks; GPT‑5.6 Sol reaches a new high of 72.7%, above Claude Fable 5’s 69.9%, at 36.2% lower estimated API cost."
- **Our assessment**: "DeepSWE v1.1" is new to the corpus — no existing source note names this benchmark. This is a third, independent coding-benchmark data point in the corpus's ongoing "benchmark choice determines the winner" pattern (alongside SWE-Bench Pro, where `blog-openai-gpt56-ga-announcement.md` Claim 4 shows Fable 5 winning 80% to Sol's 64.6%, and the Artificial Analysis Coding Agent Index, where that note's Claim 5 shows Sol winning). On DeepSWE v1.1, Sol wins by a narrower margin (2.8 points, 72.7 vs. 69.9) than its Artificial Analysis Index win (2.8 points there too, coincidentally the same margin size but a different score scale) — worth citing in Chapter 03 as a third concrete instance of the same-domain, different-benchmark, different-winner pattern already established for GPT‑5.6 vs. Fable 5 specifically on coding tasks.

### Claim 8: AI adoption deepens in stages — first drafting, then finding context and reasoning across tools and data, then taking action, handling exceptions, and completing workflows with human judgment and control — and dependability should be tracked as three concrete outcomes: ready to use, needs correction, or needs escalation
- **Evidence**: The "How often does AI get the work right?" section, describing both the staged-adoption model and the three-outcome tracking taxonomy.
- **Confidence**: anecdotal (a named staged-adoption model and a named three-outcome taxonomy, both asserted without data on how organizations currently distribute across the three outcomes, or how long each adoption stage typically takes)
- **Quote**: "AI adoption tends to deepen in stages. First, AI helps draft. Then it finds context and reasons across tools and data. Over time, it begins taking action, handling exceptions, and completing workflows, with people providing judgment and control where needed."
- **Additional quote (same section, following paragraphs)**: "Ready to use: The result met the quality bar as delivered. Needs correction: The result required another attempt or human edits. Needs escalation: A person needed to step in and finish the work."
- **Our assessment**: The three-outcome taxonomy is new to the corpus and is genuinely more operational than most of this post's other claims — it names a specific, small, loggable category set that a team could plausibly instrument (was this task's result used as-is, corrected, or escalated?). It is a different kind of artifact than `blog-thoughtworks-anand-agent-evaluation-framework.md`'s three-layer evaluation architecture (Claim 5's persona-based testing / Claim 6's functional unit evals / Claim 7's operational observability): that framework describes *pre-production testing layers*, while this taxonomy describes *production outcome categories* for tasks already shipped to users. The two are complementary altitudes (test-time evaluation vs. production outcome tracking), not competing frameworks, and a guide chapter on evaluation could present them side by side without conflict.

### Claim 9: Before AI moves from drafting to taking action, organizations should define what data the system can access, what systems it can use or change, and when a person should review or approve an action
- **Evidence**: Direct governance recommendation in the "How often does AI get the work right?" section, following the dependability taxonomy in Claim 8.
- **Confidence**: anecdotal (prescriptive governance checklist; no example of an organization applying these three boundary types, and no detail on how "review or approve" is implemented mechanically)
- **Quote**: "Dependability also requires clear boundaries. Before AI moves from drafting to taking action, organizations should define: What data the system can access. What systems it can use or change. When a person should review or approve an action."
- **Our assessment**: This three-part boundary checklist (data access / system access / approval gates) is structurally similar to, but less operationally detailed than, `blog-openai-managing-ai-investments-agentic-era.md` Claim 5's "governance as the operating layer" framing (context, tools, actions, approvals, capacity) — this post's list is a subset of that earlier post's five-part list, restated in the specific context of the drafting-to-action transition rather than as a general investment-governance principle. Treat as a restatement at a narrower scope, not new governance content.

### Claim 10: Value scales when completed work grows faster than total cost while quality holds or improves, and compute — training compute for future capability, inference compute for delivering today's work — sits at the center of realizing that scaling
- **Evidence**: The "Does each AI dollar buy more work as usage grows?" section, the article's fourth and final scorecard dimension.
- **Confidence**: anecdotal (a definitional claim about what "value at scale" means, plus an assertion that compute is central to it; no data on any organization's actual work-growth-vs-cost-growth ratio over time is given)
- **Quote**: "Track how many tasks met the quality bar, the total cost of completing them, and the cost per successful task. If completed work grows faster than total cost while quality holds or improves, each AI dollar is producing more value."
- **Our assessment**: This closes the loop on Claim 3's formula — the same three tracked quantities (tasks meeting quality bar, total cost, cost per successful task) are proposed both as a point-in-time cost calculation (Claim 3) and, tracked over time, as the scaling-value indicator (this claim). It is the most methodologically coherent part of the post: a single set of three numbers serves both purposes, at least in principle, even though no worked example of tracking them over time is given.

## Concrete Artifacts

### The "Useful Intelligence per Dollar" four-question framework (verbatim, from source)

```
A scorecard for the AI age — Sarah Friar, OpenAI, July 17, 2026
https://openai.com/index/a-scorecard-for-the-ai-age

"The ultimate scorecard for the age of AI could be looked at as “Useful
Intelligence per Dollar.” This metric answers four key questions:

1. Is AI completing work that matters?
2. What does each successful task cost?
3. Can people depend on the result?
4. Does each AI dollar produce more value as usage grows?"
```

### Cost-per-successful-task formula (verbatim, from source)

```
"The calculation is straightforward:
- Add the full cost of completing the work.
- Count the tasks that met the required quality bar.
- Divide the full cost by the number of successful tasks."
```

### Dependability boundary checklist (verbatim, from source)

```
"Before AI moves from drafting to taking action, organizations should
define:
- What data the system can access.
- What systems it can use or change.
- When a person should review or approve an action."
```

### DeepSWE v1.1 benchmark chart caption (verbatim, from source)

```
"DeepSWE v1.1: Long-horizon engineering tasks; GPT‑5.6 Sol reaches a new
high of 72.7%, above Claude Fable 5’s 69.9%, at 36.2% lower estimated API
cost."
```

## Cross-References

### Cross-reference verification notes
`blog-openai-managing-ai-investments-agentic-era.md`, `blog-openai-gpt56-ga-announcement.md`,
`blog-anthropic-admin-analytics-cost-controls.md`, `blog-cursor-cfo-council.md`,
and `blog-thoughtworks-anand-agent-evaluation-framework.md` were re-read
directly (MINER.md §4b) and the claim numbers cited above were confirmed
against each note's numbered `### Claim N:` headings in document order
before writing this section.

- **Corroborates**:
  - `blog-openai-managing-ai-investments-agentic-era.md` Claim 2 ("useful
    work per dollar" as the outcome metric leaders should track instead of
    token price): this source's Claim 1 ("Useful Intelligence per Dollar")
    and Claim 2 (full cost of a successful outcome, not token price) restate
    the identical argument from the same company three days later, now
    packaged as a named, four-dimension scorecard rather than a single
    recommendation sentence.
  - `blog-openai-managing-ai-investments-agentic-era.md` Claim 4 (lowest
    token price ≠ lowest total cost; a pricier model can win by succeeding
    in one pass): this source's Claim 4 restates the same argument nearly
    verbatim in different wording, three days later.
  - `blog-cursor-cfo-council.md` Claim 2 (McKinsey: 88% of organizations
    have deployed AI, but only 39% can trace it to EBIT impact): a
    different vendor (Cursor), writing to the same CFO audience in the same
    three-week window (July 6 vs. July 17, 2026), makes the same underlying
    argument this source opens with — that adoption metrics do not show
    value, and organizations need a work/outcome-based measure instead.
    This is independent cross-vendor corroboration of the "adoption ≠
    value" premise, from a company with no stake in OpenAI's own product
    positioning.
  - `blog-cursor-cfo-council.md` Claim 8 (cost per accepted line varied
    ~7x across model families in Cursor's own telemetry): this is
    independent, measured evidence for this source's Claim 4 (lowest token
    price does not produce lowest cost per outcome) — Cursor's figure comes
    from actual usage data across model families, which this OpenAI post
    does not provide for its own claim.

- **Contradicts**: None filed as a new MINER.md §4a contradiction. The
  tension between this source's Claim 4 (organizations should evaluate
  models by cost-per-outcome, not token price) and the market-routing
  behavior documented via Vercel's production-index data (cited in
  `blog-openai-managing-ai-investments-agentic-era.md`'s own
  Cross-References → Contradicts, not independently re-verified in this
  extraction) is the same normative-vs-descriptive gap already surfaced
  against that earlier post. This source adds no new descriptive evidence
  and restates the same normative claim, so no new contradiction issue was
  filed; the existing gap noted on the July 14 post's note applies equally
  here.

- **Extends**:
  - `blog-openai-managing-ai-investments-agentic-era.md` Claim 4: that
    post asserted "track cost per accepted outcome" as a principle but its
    own Source Context explicitly flags that it gives "no technical
    description of how 'cost per accepted outcome' should actually be
    computed." This source's Claim 3 supplies the missing three-step
    formula (add full cost, count successful tasks, divide) — still without
    a worked numeric example, but a more complete methodological statement
    than the earlier post gave.
  - `blog-openai-gpt56-ga-announcement.md` Claim 4 (SWE-Bench Pro: Fable 5
    wins, 80% vs. Sol's 64.6%) and Claim 5 (Artificial Analysis Coding
    Agent Index: Sol wins over Fable 5, using less than half the output
    tokens and about one-third less cost): this source's Claim 7 (DeepSWE
    v1.1: Sol wins over Fable 5, 72.7% vs. 69.9%, at 36.2% lower cost) adds
    a third, independent coding benchmark to the same "benchmark choice
    determines the winner" evidence set already established for GPT‑5.6 vs.
    Fable 5 specifically.
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 2 (Claude
    Code's Value tab, with visible/adjustable formulas for productivity
    lift and cost per commit): this source's Claim 3 (explicit
    cost-per-successful-task arithmetic) gives OpenAI's own equivalent
    formula-transparency move, though as prose guidance rather than a
    shipped, adjustable product feature the way Anthropic's Value tab is.

- **Novel**:
  - **"Useful Intelligence per Dollar" as a named, capitalized, branded
    four-dimension scorecard** (Claim 1): more formalized than the
    generic "useful work per dollar" phrasing already in the corpus via the
    July 14 OpenAI post.
  - **The explicit three-step cost-per-successful-task formula** (Claim 3):
    the first source in the corpus to state actual calculation steps for an
    "outcome cost" metric, rather than only the principle that such a
    metric should be tracked.
  - **The three-outcome dependability taxonomy** (ready to use / needs
    correction / needs escalation) (Claim 8): a new, potentially
    instrumentable production-metrics category set, distinct from the
    pre-production evaluation layers already documented via the Thoughtworks
    agent-evaluation-framework note.
  - **DeepSWE v1.1 as a named benchmark** (Claim 7): first corpus mention
    of this specific benchmark name.
  - **Sarah Friar as a named, individually bylined OpenAI author** (Source
    Context): the existing `blog-openai-managing-ai-investments-agentic-era.md`
    note on the closely related July 14 post is unsigned/house-authored;
    this is the first corpus source attributing OpenAI's cost-governance
    messaging to a specific named individual.

## Guide Impact

- **Chapter 05 (Team Adoption / ROI framing)**: Add "Useful Intelligence per
  Dollar" (Claim 1) and the explicit cost-per-successful-task formula
  (Claim 3) as OpenAI's most complete public statement of its
  outcome-over-token-price argument — present alongside the July 14 post's
  looser "useful work per dollar" phrasing (already in the guide via
  `blog-openai-managing-ai-investments-agentic-era.md`) and Anthropic's
  Value-tab feature (`blog-anthropic-admin-analytics-cost-controls.md`
  Claim 2) as three vendors converging on the same measurement philosophy,
  with this source providing the most explicit (if still unexemplified)
  arithmetic of the three.
- **Chapter 05 (Team Adoption / cross-vendor corroboration)**: Cite
  `blog-cursor-cfo-council.md` Claim 2 (McKinsey's 88%-deployed/39%-EBIT-traced
  gap) alongside this source's opening framing as independent, non-OpenAI
  confirmation that "adoption metrics don't show value" is a live concern
  among enterprise finance leaders in mid-2026, not just an OpenAI talking
  point.
- **Chapter 03 (Model Selection — Benchmark Interpretation)**: Add the
  DeepSWE v1.1 data point (Claim 7: Sol 72.7% vs. Fable 5 69.9%, 36.2%
  lower cost) as a third coding-benchmark comparison point in the existing
  "no single benchmark picks a winner" discussion already built around
  SWE-Bench Pro and the Artificial Analysis Coding Agent Index
  (`blog-openai-gpt56-ga-announcement.md` Claims 4-5) — three different
  named coding benchmarks now give three data points on the same
  Sol-vs-Fable-5 matchup, two in Sol's favor and one in Fable 5's favor.
- **Chapter 03 / Chapter 05 (Evaluation)**: Add the three-outcome
  dependability taxonomy (Claim 8: ready to use / needs correction / needs
  escalation) as a candidate production-metrics category set for teams
  instrumenting agent-task outcomes, positioned as complementary to (not a
  replacement for) the pre-production evaluation layers already documented
  via `blog-thoughtworks-anand-agent-evaluation-framework.md` — flag it
  explicitly as an unvalidated vendor proposal with no worked example of
  how the three categories would actually be logged or measured.

## Extraction Notes

1. **WebFetch on the live OpenAI URL returned HTTP 403**, and a direct
   `curl` with a browser user-agent from Bash also returned HTTP 403 —
   consistent with the Cloudflare bot-challenge behavior already documented
   for `openai.com/index/` posts in
   `blog-openai-managing-ai-investments-agentic-era.md` and
   `blog-openai-agents-transforming-work.md`. An initial `WebFetch` pass
   through the `r.jina.ai` reader proxy returned a visibly paraphrased,
   restructured summary (with an invented "Core Framework" heading and
   compressed bullet points not present in the source) and was discarded
   per MINER.md §2a. The article was instead retrieved with a direct `curl`
   to the `r.jina.ai` proxy (bypassing WebFetch's own summarization layer),
   which returned the full page converted to Markdown — every quote in this
   note was checked character-for-character against that fetched Markdown.
   A second `curl` fetch in plain-text mode (`X-Return-Format: text`) was
   used specifically to recover the page's navigation chrome and the
   "Author" byline field (which the Markdown-mode fetch omitted), confirming
   the author name "Sarah Friar" and the July 17, 2026 publish date shown
   next to the title.
2. **No title or role is given for the author on the page itself.** This
   note reports only "Sarah Friar" as extracted from the source's own
   byline field, consistent with MINER.md's instruction not to assert
   claims the source does not itself make; no role or title is stated in
   Source Context beyond what the fetched page discloses.
3. **No sub-pages followed.** The post does not link to any page containing
   additional claims about the scorecard framework itself; its outbound
   links (GPT‑5.6's own announcement, ChatGPT Work, ChatGPT Enterprise) are
   product pages already covered elsewhere in the corpus
   (`blog-openai-gpt56-ga-announcement.md`,
   `blog-openai-chatgpt-work-ambitious-partner.md`).
4. **One quote had markdown formatting markers elided.** The DeepSWE v1.1
   chart caption (Claim 7) rendered in the fetched Markdown as
   `**_DeepSWE v1.1_**_: Long-horizon engineering tasks...cost._` — bold and
   italic markup characters (`**`, `_`) interspersed within the caption
   text by the site's own chart-caption styling, not prose punctuation.
   These markup characters were stripped for the quote reproduced in this
   note; the underlying visible text (verified by regex-stripping `*`/`_`
   from the raw fetched line) is otherwise character-for-character
   identical to what is quoted above. No words were added, removed, or
   reordered.
5. **Chart data not recoverable beyond captions.** The DeepSWE v1.1 chart
   (Claim 7) and the Artificial Analysis Coding Agent Index reference
   (Claim 6) are both illustrated with embedded charts in the source; the
   reader-proxy Markdown conversion preserved the DeepSWE v1.1 caption as
   quotable prose but not any underlying chart data table, consistent with
   the same limitation already documented in
   `blog-openai-chatgpt-adoption-signals.md`'s Extraction Notes for a
   different OpenAI Signals post.
6. **No contradiction issue filed.** The only tension identified (Claim 4's
   cost-per-outcome prescription vs. observed market routing-to-cheapest-model
   behavior) is the same gap already surfaced against
   `blog-openai-managing-ai-investments-agentic-era.md`, restated by the
   same company three days later with no new descriptive evidence. Filing a
   second contradiction issue for the same underlying tension, re-triggered
   by a closely related follow-up post from the same source, was judged
   not to meet MINER.md §4a's bar ("the contradiction is already filed").
7. **Confidence calibration: anecdotal.** Seven of this note's ten claims are
   individually rated anecdotal — the post is almost entirely prescriptive
   framework and named-but-unexemplified formulas/taxonomies, with no named
   customer, no worked numeric example, and no disclosed methodology beyond
   the DeepSWE v1.1 chart (Claim 7, rated emerging), the Artificial Analysis
   Coding Agent Index figure (Claim 6, rated emerging as a specific
   quantified benchmark statistic), and the GPT‑5.6 tier description
   (Claim 5, rated emerging as a factual product description).
   This mirrors the confidence profile already assigned to
   `blog-openai-managing-ai-investments-agentic-era.md` (also entirely
   anecdotal at the individual-claim level) — the two posts share the same
   evidentiary thinness, consistent with both being executive framing
   pieces rather than measured studies.
