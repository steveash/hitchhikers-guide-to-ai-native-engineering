---
source_url: https://openai.com/index/managing-ai-investments-in-agentic-era
source_type: blog-post
title: "How to manage AI investments in the agentic era"
author: OpenAI
date_published: 2026-07-14
date_extracted: 2026-07-28
last_checked: 2026-07-28
status: current
confidence_overall: anecdotal
issue: "#2273"
---

# How to Manage AI Investments in the Agentic Era

> OpenAI's five-point executive framework for AI investment governance in the
> agentic era: shift measurement from token price to "useful work per dollar,"
> evaluate models by cost-per-accepted-outcome rather than price-per-token,
> treat governance as the operating layer that gates which workflows can
> scale, fund AI work as a three-tier portfolio (broad access / function-specific
> / strategic bets), and match product/capacity to proven demand rather than
> letting every team rebuild its own infrastructure. The post is prescriptive
> vendor guidance, not a measured study — every recommendation doubles as a
> pointer to a paid OpenAI enterprise product that implements it.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`, published
  July 14, 2026; a five-section prescriptive framework piece, unsigned/house-authored,
  auto-discovered via the `openai-news` trusted RSS feed). Structured as one
  short framing intro followed by five numbered "ways to invest with
  confidence," each pairing a strategic principle with a specific OpenAI
  product capability that implements it.
- **Author credibility**: First-party OpenAI vendor content, unsigned (no
  named individual author). Every one of the five sections links to a paid
  OpenAI enterprise product or program (ChatGPT Work, Admin Console spend
  controls, AI Deployment Engineers, Zero Data Retention, OpenAI Frontier /
  Deployment Company) — this is investment-strategy framing written to
  justify and cross-sell OpenAI's own enterprise product line, not
  independent research or a customer case study. No customer names, no
  quantified outcomes, and no methodology are given anywhere in the post;
  every claim is prescriptive advice or a product-capability description,
  not a measured finding.
- **Scope**: Covers five investment/governance principles (usage visibility,
  outcome-based model evaluation, pre-scale governance, portfolio-style
  funding, demand-matched capacity) and the specific product features that
  back each one (Admin Console analytics, `evals that reflect real tasks`,
  ChatGPT Work's centralized access/spend controls, AI Deployment Engineers,
  Zero Data Retention, OpenAI Frontier, Deployment Company). Does NOT cover:
  any named customer's actual investment outcome or ROI number, a
  quantified cost-governance failure case (contrast with the Uber/Meta/Microsoft
  budget-shock material already in the corpus), pricing figures for any of
  the named products, or a technical description of how "cost per accepted
  outcome" should actually be computed.

## Extracted Claims

### Claim 1: From GPT‑4 to GPT‑5.4, OpenAI's price per million tokens fell 97%, and GPT‑5.6 continues that trend, delivering better performance on the Artificial Analysis Coding Agent Index while using 54% fewer output tokens and 57% less time per task
- **Evidence**: OpenAI's own stated pricing/benchmark trend, presented as the article's opening context before the "but token price alone does not show value" pivot.
- **Confidence**: anecdotal (first-party vendor claim; no link to a pricing table or the underlying Artificial Analysis benchmark run is given in this post, and the 97% and 54%/57% figures are asserted, not sourced, within the article itself)
- **Quote**: "OpenAI's goal is to make AI more accessible, capable and affordable over time. From GPT‑4 to GPT‑5.4, the price per million tokens fell 97%. GPT‑5.6 continues that progress, delivering better performance in the Artificial Analysis Coding Agent Index with 54% fewer output tokens and 57% less time per task."
- **Our assessment**: The 54%-fewer-output-tokens framing measures GPT‑5.6 against OpenAI's own prior models over time (self-comparison), which is a different comparison from `blog-openai-gpt56-ga-announcement.md` Claim 5's figure (GPT‑5.6 Sol using "less than half the output tokens... and costing about one-third less" specifically **relative to Claude Fable 5** on the same Artificial Analysis Coding Agent Index). Both cite the same benchmark index and are directionally consistent (GPT‑5.6 is token-efficient), but they answer different questions — "cheaper than our own last model" vs. "cheaper than a named competitor" — and should not be conflated as the same statistic if both are cited in the guide.

### Claim 2: Token price alone does not indicate whether AI is creating value; leaders should instead measure "useful work per dollar" — tasks completed, time saved, decisions improved, and workflows ready to scale
- **Evidence**: The article's central thesis statement, presented as the pivot from the price-trend context (Claim 1) into the five-point framework that follows.
- **Confidence**: anecdotal (prescriptive framing claim; no worked example or formula for "useful work per dollar" is given anywhere in the post)
- **Quote**: "But token price alone does not show whether AI is creating value. Leaders should look at useful work per dollar: tasks completed, time saved, decisions improved, and workflows ready to scale."
- **Our assessment**: This is the article's headline reframing and the Prospector's triage question directly targets it. It is consistent in spirit with `blog-anthropic-admin-analytics-cost-controls.md` Claim 2's Claude Code "Value tab" (which estimates productivity lift and cost per commit with visible, adjustable formulas) — both vendors are pushing customers away from a raw per-token price comparison and toward an outcome-denominated metric. Neither vendor, however, specifies how "decisions improved" or "workflows ready to scale" would actually be measured; this remains an aspirational metric name, not a methodology, in both sources.

### Claim 3: Enterprise leaders need a plain view of who is using AI, which products/models they use, how much capacity they consume, and what kind of work that usage supports — without that visibility, a growing bill could reflect waste, productive experimentation, or an emerging business-critical workflow, and these three cannot be distinguished from spend alone
- **Evidence**: Section 1 ("Sharpen visibility into usage and spend"), describing the Admin Console's updated usage analytics and spend controls.
- **Confidence**: anecdotal (prescriptive framing plus a first-party product description; no data on how often rising spend actually falls into each of the three named categories)
- **Quote**: "Enterprise leaders need a plain view of AI usage: who is using it, which products or models they are using, how much capacity they are consuming, and what kind of work that usage supports. Without that visibility, a growing bill is hard to interpret. It could reflect waste, productive experimentation, or a workflow that is starting to become business-critical."
- **Our assessment**: This directly corroborates `blog-anthropic-admin-analytics-cost-controls.md` Claim 1 (Anthropic's admin dashboard breaking down usage/cost by group and user, filterable by SCIM groups) — both vendors are converging on the same claim that raw spend totals are uninterpretable without a workload/user breakdown. OpenAI adds a three-way interpretive framing (waste vs. experimentation vs. emerging-business-critical) that the Anthropic note does not state explicitly, though the underlying dashboards described in both posts serve the same diagnostic function.

### Claim 4: The lowest token price does not always produce the lowest total cost — a cheaper model may fail, retry, or require correction, while a more capable model may cost more per token but reach an acceptable result faster with fewer attempts and less review — so for priority workflows, organizations should track cost per accepted outcome, not cost per token
- **Evidence**: Section 2 ("Evaluate model efficiency by outcome ROI"), the article's most concrete methodological recommendation.
- **Confidence**: anecdotal (prescriptive recommendation; no worked example of a "cost per accepted outcome" calculation, no named customer, and no data on how often a pricier model actually wins on total cost)
- **Quote**: "For priority workflows, track cost per accepted outcome. In customer support, that might be a resolved case. In engineering, it might be a tested change that passes review."
- **Additional quote (same section, preceding paragraph)**: "The lowest token price does not always produce the lowest total cost. A cheaper model may fail, retry, or create work that needs correction. A more capable model may cost more per token but reach an acceptable result faster, with fewer attempts and less review."
- **Our assessment**: This is the article's most guide-relevant, falsifiable claim, and it stands in direct tension with the market-level evidence in `blog-vercel-ai-gateway-production-index-may2026.md` Claim 5 and Claim 6: Vercel's first-party gateway data shows teams *in practice* routing high volumes of coding-agent traffic to the cheapest available model (DeepSeek: 49% of coding-agent tokens at only 4% of cost) rather than uniformly following an outcome-cost calculation, and shows the market's blended average cost per token *rising* even as a much cheaper model entered at scale — i.e., frontier-model demand grew faster than cost-per-outcome optimization pulled spend down. This is not a MINER.md §4a contradiction (OpenAI is issuing normative advice about what organizations *should* measure; Vercel is reporting what organizations *actually* do in aggregate), but the guide should note the gap between the prescription and the observed market behavior when citing this claim.

### Claim 5: Enterprise leaders should treat governance as the operating layer that determines which AI work can scale — defining what context an agent can use, which tools it can access, what actions it can take, who approves higher-risk steps, and how additional capacity is granted as teams find valuable workflows
- **Evidence**: Section 3 ("Govern advanced workflows before they scale"), tied to ChatGPT Work's centralized admin controls and, for priority deployments, OpenAI's AI Deployment Engineers program.
- **Confidence**: anecdotal (prescriptive framing plus first-party product description; no data on adoption or effectiveness of this governance model at any named organization)
- **Quote**: "Enterprise leaders should treat governance as the operating layer that determines which AI work can scale. The practical work is to define what context ChatGPT can use, which tools it can access, what actions it can take, who approves higher-risk steps, and how additional capacity is granted when teams find valuable workflows."
- **Our assessment**: This "governance as the operating layer" framing directly corroborates and gives OpenAI's own name to the same argument made in `blog-thoughtworks-kamelman-token-crisis.md` Claim 13: "When the constraint is physical and compounding, you cannot optimize your way out of it at the billing layer. You have to move the decisions that generate the cost upstream, to where they can actually be governed." Kamelman's essay frames this as a hard-won lesson from budget-shock case studies (Uber, Microsoft); OpenAI's post presents the identical upstream-governance move as a proactive best practice with no crisis narrative attached — the same recommendation reaches the guide from two independent, non-overlapping sources (a consultancy synthesizing press coverage of AI budget failures vs. a lab's own product-positioning post), which strengthens the case for citing "govern upstream, not at the billing layer" as a cross-corroborated principle.

### Claim 6: Sensitive workflows need the right access controls, retention posture, compliance visibility, and approval paths before they scale, and OpenAI's enterprise privacy controls — including Zero Data Retention — can help customers deploy AI in high-trust environments
- **Evidence**: Section 3, continuing the governance discussion into a specific privacy/compliance product pointer.
- **Confidence**: anecdotal (product-capability pointer; no detail on what Zero Data Retention actually restricts, nor any named customer using it)
- **Quote**: "Privacy and governance should be part of that work from the start: sensitive workflows need the right access controls, retention posture, compliance visibility, and approval paths before they scale. Where applicable, OpenAI's enterprise privacy controls, including Zero Data Retention options, can help customers deploy AI in high-trust environments."
- **Our assessment**: This is a bare product pointer (a link to OpenAI's own API data-usage documentation) rather than a description of the feature's mechanics — no detail is given on what data is or isn't retained, for how long, or under what conditions ZDR applies. It corroborates the general principle (already present in the corpus via Anthropic's compliance/security material) that enterprise AI governance should include a data-retention dimension, but adds no new mechanism detail.

### Claim 7: Enterprise leaders should manage AI investments as a three-tier portfolio — broad access for everyday productivity, function-specific workflows that improve repeatable work, and a smaller number of strategic bets built around proprietary company context — funding each tier according to its maturity stage (exploration, validation, production), with shared capabilities (identity, trusted connectors, curated knowledge, evaluations, observability, model routing, reusable agent patterns) funded centrally so each new workflow becomes easier and safer to launch
- **Evidence**: Section 4 ("Fund workflows that can compound"), the article's most structurally elaborate recommendation.
- **Confidence**: anecdotal (an original portfolio-allocation framework proposed by OpenAI; not benchmarked against any named organization's actual budget allocation, and no data on what fraction of spend should go to each tier)
- **Quote**: "Enterprise leaders should manage AI investments as a portfolio:broad access for everyday productivity, function-specific workflows that improve repeatable work, and a smaller number of strategic bets built around proprietary company context. The strongest candidates are workflows that repeat at meaningful scale, have clear ownership, and can be measured for quality, risk, and business value."
- **Additional quote (same section, following paragraph)**: "Funding should follow maturity. Exploration should test whether the model can handle the task; validation should test representative cases against a clear quality bar; production funding should support the integrations, controls, reliability, and change management required to scale. Shared capabilities such as identity, trusted connectors, curated knowledge, evaluations, observability, model routing, and reusable agent patterns should be funded centrally so each new workflow becomes easier and safer to launch."
- **Our assessment**: This three-tier portfolio (broad access / function-specific / strategic bets) plus exploration/validation/production funding stages is structurally parallel to `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 4's build/run/maintenance three-part token budget, but the two frameworks operate at different altitudes: O'Mahony's framework is a per-feature, ticket-level budgeting gate ("should this specific feature exist, cost-wise"), while OpenAI's is an org-wide capital-allocation framework across an entire portfolio of AI initiatives ("how much of our total AI investment goes to each tier"). Both independently arrive at "funding should track a maturity/lifecycle stage" as the organizing principle, from a consultancy's practitioner-level lens and a lab's exec-level lens respectively — this convergence is worth noting, but the guide should not treat them as the same framework at different levels of detail; they answer different questions.

### Claim 8: Once a workflow proves its value, leaders should match the specific product, capacity, and support model to its demand rather than having every team rebuild its own infrastructure — ChatGPT Work provides ready-made capabilities (chat, coding, agentic workflows, connectors, plugins, Computer Use, administration) that companies can extend with proprietary data and workflow logic, while larger strategic deployments can use OpenAI Frontier and Deployment Company to build and manage "AI coworkers" across enterprise systems
- **Evidence**: Section 5 ("Match capacity to proven demand"), the article's closing recommendation and product pointer.
- **Confidence**: anecdotal (prescriptive recommendation plus product-capability description; no named customer example of this "match capacity to demand" transition, and no criteria given for what counts as "proven" demand)
- **Quote**: "Once a workflow proves its value, leaders should match the product, capacity, and support model to its demand.ChatGPT Work provides ready-made capabilities for chat, coding, agentic workflows, connectors, plugins, Computer Use, and administration. Companies can extend that foundation with proprietary data, permissions, evaluations, and workflow logic where those elements create differentiated value."
- **Additional quote (same section, following paragraph)**: "This approach lets leaders scale proven work with the right product, capacity, and support model instead of making each workflow rebuild its own infrastructure."
- **Our assessment**: The "don't make each workflow rebuild its own infrastructure" argument is the closing rationale for Claim 7's "fund shared capabilities centrally" recommendation — both point toward centralizing platform investment (identity, connectors, knowledge, evaluations) so individual workflows only need to add their differentiated logic on top. This is consistent with, but less operationally detailed than, the shared-infrastructure arguments already in the corpus (e.g., `blog-anthropic-building-enterprise-agents.md` Claim 2's "encoding institutional knowledge into systems that compound," which is similarly aspirational and unmechanized). Notably, this section is also OpenAI's most direct pointer toward its own paid products (ChatGPT Work, OpenAI Frontier, Deployment Company) as the literal implementation of "match capacity to demand," underscoring the post's dual function as strategy advice and product cross-sell.

### Claim 9: Reducing wasted AI spend is not only a matter of model choice — clear instructions, focused tools, reusable context, and explicit stopping conditions can reduce loops and wasted spend, and the goal should be to match the model and workflow to the task, using smaller/faster models when they meet the quality bar and reserving frontier intelligence for complex, ambiguous, or high-stakes work
- **Evidence**: Closing paragraph of Section 2 ("Evaluate model efficiency by outcome ROI").
- **Confidence**: anecdotal (prescriptive engineering advice; no data on how much loop-reduction or spend-reduction these levers produce)
- **Quote**: "Model choice is only part of the equation. Clear instructions, focused tools, reusable context, and explicit stopping conditions can reduce loops and wasted spend. The goal is to match the model and workflow to the task: use smaller or faster models when they meet the quality bar, and reserve frontier intelligence for complex, ambiguous, or high-stakes work."
- **Our assessment**: The "explicit stopping conditions... reduce loops" recommendation directly corroborates `blog-thoughtworks-kamelman-token-crisis.md` Claim 8's engineering diagnosis of token waste ("retry instructions without hard boundaries create expensive loops that are invisible to standard infrastructure monitoring"), and the "match model to task, reserve frontier intelligence for high-stakes work" recommendation restates the tiered-model-routing pattern already well-documented via `blog-vercel-ai-gateway-production-index-may2026.md` Claim 5 (the coding-agent use case's observed DeepSeek/Anthropic volume split) and `docs-ghaw-cost-management.md`'s model-selection cost strategy. This claim adds no new mechanism beyond what's already in the corpus, but it is a third independent source (lab vendor, this time) converging on the same "route cheap work to cheap models, and bound agent loops explicitly" advice.

## Concrete Artifacts

### The five-point investment framework (verbatim structure, from source)

```
How to manage AI investments in the agentic era — OpenAI, July 14, 2026
https://openai.com/index/managing-ai-investments-in-agentic-era

1. Sharpen visibility into usage and spend
   -> Admin Console: usage analytics + spend controls, filterable at
      workspace / team-and-user / product-and-model "altitudes"

2. Evaluate model efficiency by outcome ROI
   -> track "cost per accepted outcome," not cost per token
   -> pair cost with business value (time saved, cycle time, revenue
      protected, risk avoided, capacity created)

3. Govern advanced workflows before they scale
   -> ChatGPT Work: centralized controls for context, tools, actions,
      approvals, spend
   -> AI Deployment Engineers (for priority deployments): evals,
      architecture, latency, reliability, workflow design
   -> Zero Data Retention (privacy/compliance)

4. Fund workflows that can compound
   -> Portfolio: broad access / function-specific workflows / strategic bets
   -> Funding follows maturity: exploration -> validation -> production
   -> Shared capabilities (identity, connectors, knowledge, evals,
      observability, model routing, agent patterns) funded centrally

5. Match capacity to proven demand
   -> ChatGPT Work (ready-made capabilities) for proven workflows
   -> OpenAI Frontier + Deployment Company for larger strategic deployments
```

### The article's altitude-based visibility framing (verbatim)

```
"Insights at different altitudes help guide investment and enablement
decisions:
- Workspace: Are adoption and spend moving together?
- Team and user: Where is demand growing, and who may need more support?
- Product and model: Where is more expensive intelligence being used, and
  is that demand sustained?
Together, these views help admins decide where to invest, coach, or set
limits."

Source: https://openai.com/index/managing-ai-investments-in-agentic-era
```

## Cross-References

### Cross-reference verification notes
`blog-anthropic-admin-analytics-cost-controls.md`, `blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-thoughtworks-kamelman-token-crisis.md`, `blog-thoughtworks-omahony-feature-token-budgets.md`,
`blog-openai-gpt56-ga-announcement.md`, and `blog-anthropic-building-enterprise-agents.md`
were re-read directly (MINER.md §4b) and the claim numbers cited above were
confirmed against each note's numbered `### Claim N:` headings in document
order before writing this section.

- **Corroborates**:
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 1 (Anthropic's
    admin dashboard breaking down usage/cost by group and user) and Claim 2
    (Claude Code's Value tab, with visible/adjustable ROI formulas): this
    source's Claim 2 ("useful work per dollar") and Claim 3 (usage-visibility
    argument) show both major labs converging, within roughly a month of
    each other (Anthropic July 2, OpenAI July 14, 2026), on the same
    outcome-over-token-price framing for enterprise AI cost governance.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 13 ("move the
    decisions that generate the cost upstream, to where they can actually
    be governed" — you cannot optimize your way out of a physical/compounding
    constraint at the billing layer): this source's Claim 5 ("governance as
    the operating layer that determines which AI work can scale") is the
    identical upstream-governance argument, independently reached by a
    consultancy synthesizing budget-crisis press coverage and by a lab
    positioning its own enterprise product.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 8 (token waste caused
    by retry loops without hard boundaries, verbose context, generous
    retrieval): this source's Claim 9 ("explicit stopping conditions can
    reduce loops and wasted spend") names the same failure mode from the
    vendor side.

- **Contradicts**: None filed as a MINER.md §4a contradiction. One notable
  tension is flagged instead: this source's Claim 4 (organizations *should*
  track cost-per-accepted-outcome rather than cost-per-token when choosing
  models) sits in tension with `blog-vercel-ai-gateway-production-index-may2026.md`
  Claim 5 and Claim 6, which show that in aggregate, gateway traffic is
  heavily routed to the cheapest available model for high-volume coding-agent
  work (DeepSeek: 49% of tokens at 4% of cost) and that the market's blended
  per-token cost is *rising* despite that cheap-model entry, because frontier
  demand is growing even faster. This is not a MINER.md §4a contradiction
  because the two sources are not making an opposing claim about the same
  fact — OpenAI is issuing normative advice about what a cost-per-outcome
  discipline *should* look like; Vercel is reporting descriptive market-level
  routing behavior. No contradiction issue was filed, but the gap between
  the prescription and the observed aggregate behavior is worth surfacing
  wherever the guide cites this claim.

- **Extends**:
  - `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 4
    (build/run/maintenance token budget per feature, a ticket-level
    budgeting gate): this source's Claim 7 (three-tier investment portfolio
    funded by maturity stage — exploration/validation/production) is a
    structurally parallel maturity-staged funding argument at the
    org-wide capital-allocation altitude rather than the per-feature
    altitude — the two frameworks answer different questions ("should this
    specific feature exist, cost-wise" vs. "how should our total AI
    investment be allocated across initiatives") but share the same
    underlying "fund according to lifecycle stage" logic.
  - `blog-anthropic-building-enterprise-agents.md` Claim 2 ("encoding
    institutional knowledge into systems that compound over time" — an
    aspirational, unmechanized claim) and Claim 6 (revenue vs. cost
    reduction as distinct enterprise AI investment pathways, also
    described only abstractly there): this source's Claim 7 (fund shared
    capabilities centrally: identity, connectors, knowledge, evaluations,
    observability, model routing) gives a more concrete list of *what*
    "compounding" infrastructure actually consists of than either of the
    Anthropic post's abstract claims did — still no worked example, but a
    more specific inventory of shared components.
  - `blog-openai-gpt56-ga-announcement.md` Claim 5 (GPT‑5.6 Sol vs. Claude
    Fable 5 on the Artificial Analysis Coding Agent Index — competitor
    comparison): this source's Claim 1 cites the same benchmark index for a
    self-comparison (GPT‑5.6 vs. OpenAI's own GPT‑5.4/GPT‑4) rather than a
    competitor comparison — see Claim 1's "Our assessment" for why these
    should not be conflated as the same statistic.

- **Novel**:
  - **"Useful work per dollar" and "cost per accepted outcome" as named
    metrics** (Claims 2, 4): the specific phrasing is new to the corpus,
    though the underlying idea (measure outcomes, not token price) is
    already present via the Anthropic admin-analytics note.
  - **The three-tier investment portfolio (broad access / function-specific
    / strategic bets) funded by maturity stage** (Claim 7): the first
    corpus source proposing this specific org-wide capital-allocation
    taxonomy for AI investment, distinct from the existing per-feature
    (O'Mahony) and per-workflow (gh-aw) budgeting frameworks already
    documented.
  - **"Altitude"-based usage-visibility framing** (workspace / team-and-user
    / product-and-model, in Concrete Artifacts): a new organizing vocabulary
    for usage-dashboard granularity not present in the Anthropic
    admin-analytics note's equivalent (group/user) breakdown.
  - **AI Deployment Engineers and Deployment Company as named OpenAI
    enterprise programs** (Claims 5, 8): first corpus documentation of these
    two specific OpenAI professional-services offerings.

## Guide Impact

- **Chapter 05 (Team Adoption / ROI framing)**: Add Claim 2 ("useful work per
  dollar") and Claim 4 ("cost per accepted outcome," with the customer-support
  and engineering examples given) as OpenAI's specific vocabulary for the
  outcome-over-token-price argument, alongside the equivalent Anthropic
  Value-tab framing (`blog-anthropic-admin-analytics-cost-controls.md` Claim 2)
  — present both vendors' terms side by side as evidence the industry is
  converging on this framing, while flagging that neither vendor specifies
  a concrete measurement methodology.
- **Chapter 05 (Team Adoption / Investment strategy)**: Add Claim 7's
  three-tier portfolio (broad access / function-specific / strategic bets,
  funded by exploration/validation/production maturity) as a candidate
  org-wide capital-allocation framework for a section on how to prioritize
  AI investment across initiatives — explicitly flag it as an unvalidated
  vendor proposal (no named customer example, no data on actual tier
  allocation), and note its structural parallel to (but different altitude
  from) O'Mahony's build/run/maintenance per-feature budget already in the
  corpus.
- **Chapter 02 / Chapter 04 (Cost Governance)**: Add Claim 5's "governance as
  the operating layer" framing as a second, independent source (alongside
  Kamelman's Thoughtworks essay) for the "move cost-governance decisions
  upstream, not to the billing layer" principle — this cross-corroboration
  from an unrelated source (lab vendor vs. consultancy) strengthens the case
  for stating this as a recommended principle rather than a single source's
  opinion.
- **Chapter 04 (Cost Engineering at Scale)**: When citing Claim 4's
  cost-per-outcome recommendation, pair it with the Vercel production-index
  finding (`blog-vercel-ai-gateway-production-index-may2026.md` Claims 5-6)
  that aggregate market behavior does not yet show this discipline
  dominating in practice — present the OpenAI claim as prescriptive
  aspiration, not descriptive reality, to avoid overstating how settled this
  practice is.

## Extraction Notes

1. **WebFetch on the live OpenAI URL returned HTTP 403** (both
   `https://openai.com/index/managing-ai-investments-in-agentic-era` and a
   trailing-slash variant), and a direct `curl` with a standard browser
   user-agent from Bash also returned HTTP 403 — consistent with the
   Cloudflare bot-challenge behavior already documented for `openai.com/index/`
   posts in `blog-openai-agents-transforming-work.md` and
   `blog-openai-chatgpt-work-ambitious-partner.md`. The Internet Archive
   Wayback Machine's availability API returned no existing snapshot for this
   URL at extraction time. The article was instead retrieved via the
   `r.jina.ai` reader proxy, fetched directly with `curl` (not through
   WebFetch's own AI-summarization layer — an initial WebFetch pass through
   the same proxy URL returned a visibly paraphrased summary with headings
   like "Key Investment Principles" that do not appear in the source, and
   was discarded per MINER.md §2a). The direct `curl` fetch of the proxy
   returned the full page converted to Markdown, including all prose,
   headings, and bullet lists; every quote in this note was checked
   character-for-character against that fetched Markdown, which is saved at
   the time of writing and reproduced in full within this extraction's
   working notes. Two link-affordance artifacts were elided from quotes as
   formatting noise, consistent with the precedent set in
   `blog-openai-gpt56-ga-announcement.md`'s Extraction Notes: (a) a
   zero-width word-joiner character (U+2060) the site inserts after model
   names like "GPT‑5.6" to control line-wrapping, present throughout the
   fetched Markdown but invisible to a reader; (b) the literal
   "(opens in a new window)" accessibility text some external links carry
   (e.g., around "Deployment Engineers" and "Zero Data Retention"), which is
   link-affordance markup, not body prose. Neither elision changes the
   meaning of any quoted passage. Per MINER.md §2a point 3, no two
   non-adjacent sentences are spliced into a single quoted passage anywhere
   in this note — claims with evidence spanning more than one paragraph
   (Claims 4, 7, 8) instead carry two separately-labeled, independently
   contiguous `Quote` fields rather than an ellipsis-joined single quote.
   Two quotes (Claims 7 and 8) also reproduce a genuine source-side
   formatting quirk verbatim rather than silently correcting it: the
   fetched Markdown's bold-span markup closes directly against the next
   word with no intervening space ("...as a portfolio:broad access..." and
   "...to its demand.ChatGPT Work..."), preserved as-is rather than "fixed"
   with an inserted space.
2. **No sub-pages followed.** The article links to several OpenAI product
   pages (ChatGPT Work, the Admin Console, an "evals drive next chapter of
   AI" post, the Deployment Engineers/Deployment Company sites, GPT‑5.6's
   own announcement, Zero Data Retention documentation) but none of these
   contain additional claims *about the investment framework itself* — they
   are the products the framework points to, already covered by MINER.md's
   guidance that a source's own outbound links are only followed when
   substantive to the claims being extracted. `blog-openai-gpt56-ga-announcement.md`
   and `blog-openai-chatgpt-work-ambitious-partner.md` already independently
   cover two of these linked pages in the corpus.
3. **No named customer, no quantified outcome, anywhere in the source.**
   Unlike `blog-openai-chatgpt-work-ambitious-partner.md`'s testimonial
   carousel or `blog-anthropic-admin-analytics-cost-controls.md`'s three
   customer quotes, this post contains zero named individuals, companies, or
   measured results — every claim is either a prescriptive recommendation or
   a first-party product-capability description. This is the primary driver
   of the "anecdotal" overall confidence rating: there is no empirical
   evidence in this source for any of its recommendations, only OpenAI's own
   assertion that they are sound practice.
4. **No contradiction issue filed.** The tension between this source's
   Claim 4 (prescriptive: track cost-per-outcome) and the Vercel production
   index's descriptive market data (aggregate routing still dominated by
   token-price differences, not measured outcome cost) was considered per
   MINER.md §4a but does not rise to a contradiction — the two sources
   answer different questions (normative vs. descriptive) about the same
   general topic rather than making opposing factual claims. See
   Cross-References → Contradicts for the full reasoning; the Assayer or
   Smith may weigh in if they read this differently.
5. **Confidence calibration: anecdotal.** Every individual claim in this
   note is itself rated anecdotal — the source is entirely prescriptive
   vendor framing and product-capability description, with no customer
   names, no measured results, and no disclosed methodology anywhere in the
   post. This is a notably lower confidence profile than the adjacent
   `blog-anthropic-admin-analytics-cost-controls.md` note (which at least
   includes three named-role customer quotes, even if the companies
   themselves are unnamed) or the `blog-openai-chatgpt-work-ambitious-partner.md`
   note (four fully-named customer testimonials). The overall "anecdotal"
   rating reflects that this source's value to the guide is as a strategic
   framing/vocabulary source, not as evidence for any specific practice.
