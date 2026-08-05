---
source_url: https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude
source_type: blog-post
title: "A Guide to Cost Visibility and Control in Claude"
author: Anthropic
date_published: 2026-08-04
date_extracted: 2026-08-05
last_checked: 2026-08-05
status: current
confidence_overall: settled
issue: "#2500"
---

# A Guide to Cost Visibility and Control in Claude

> Anthropic's first-party strategic guide to Claude cost management: leads
> with a "measure cost-per-outcome, not token consumption" framing and a
> model-to-task-difficulty matching principle, then walks through Claude
> Enterprise admin controls (access gating, model controls, hard spend
> caps, usage observability) and Claude Platform/API cost levers (Workspaces,
> prompt caching at 10% of input rate, batch processing at half price, the
> effort parameter, and the advisor strategy) as a single practitioner
> toolkit.

## Source Context

- **Type**: blog-post (official Claude/Anthropic product blog, claude.com,
  "Enterprise AI" category; published August 4, 2026; ~5 minute read time)
- **Author credibility**: First-party Anthropic house post, not bylined to
  an individual — same publication pattern as other `blog-anthropic-*`
  product-guidance posts in this corpus. Feature descriptions (what each
  control does, what it costs) are settled first-party statements about
  shipping Claude Enterprise/Platform capabilities. The strategic framing
  ("measure cost-per-outcome") is vendor guidance, but it is stated as a
  principle rather than backed by an audited case study or benchmark, so
  it is graded settled-as-stated-recommendation rather than settled-as-
  measured-fact.
- **Scope**: Covers cost-per-outcome framing, model-to-task matching, the
  four Claude model classes at a task-type level, Claude Enterprise admin
  controls (access gating, model controls, hard spend caps, usage
  analytics, Analytics API, analytics chat), and Claude Platform/API cost
  levers (Workspaces, prompt caching, batch processing, effort parameter,
  advisor strategy). Does NOT cover: pricing tables, the underlying
  token-accounting implementation, whether any of this differs by plan
  tier below Enterprise, or a quantified figure for the closing "cut cost
  ... substantially" claim. Links out to product documentation for each
  named lever (effort, advisor tool, prompt caching, batch processing,
  Analytics API, Workspaces docs, access gating/model controls/spend cap
  support articles) — these were not followed as separate pages per
  MINER.md's "substantive linked pages" bar; they are reference-doc links
  for features this article already describes at the level of detail
  needed for extraction, not additional argument to mine.

## Extracted Claims

### Claim 1: The primary cost metric should be cost-per-outcome, not token consumption, assessed via two questions — the counterfactual cost of the work without AI, and whether the task is judgment-heavy or high-volume-and-straightforward
- **Evidence**: Stated as the article's opening strategic principle, in the "Useful Ways to Think About Cost" section.
- **Confidence**: settled (explicit, unambiguous first-party recommendation, though not backed by a measured example in this article)
- **Quote**: "It's helpful to measure AI's cost-per-outcome instead of token consumption as the primary metric of value." Plus the two diagnostic questions: "What would this work have cost without AI, whether in resources, time, or never attempting the project at all?" and "Is a model completing a task that is hard and requires judgment and reasoning, or is it just large, meaning a high volume of straightforward work?"
- **Our assessment**: This is a strategic framing claim rather than a specific tactic — it tells practitioners what to measure (outcome value relative to a without-AI counterfactual) rather than how to reduce a number. It sets up the rest of the article's tactics (model matching, caching, batching, effort, advisor) as tools in service of that outcome-per-dollar goal, not as ends in themselves. No prior corpus source frames Claude cost management with this specific two-question diagnostic.

### Claim 2: Mismatching model capability to task difficulty raises total cost in both directions — a cheap model on a hard reasoning task burns tokens on retries and needs more human correction, while a frontier model on basic document processing pays for unused capability
- **Evidence**: Direct causal explanation immediately following Claim 1's framing.
- **Confidence**: settled (stated as Anthropic's own reasoning, not backed by a specific measurement in this article)
- **Quote**: "Assigning a less expensive model complex reasoning often makes the finished task more expensive, because it burns tokens on retries and needs more human correction. Putting a frontier model on basic document processing pays for capabilities the task never uses."
- **Our assessment**: This is the same underlying mechanism as `blog-anthropic-choosing-claude-model.md` Claim 2 ("cost-per-task is often lower for more intelligent models... because more capable models often take fewer turns and less thinking time"), restated here as a two-sided risk (both under- and over-matching are expensive) rather than that note's one-sided "start with the strongest model" framing. Together the two sources give a fuller picture: undermatching costs via retries/correction (this claim), while that note's Claim 1 argues for starting strong specifically to avoid the model-failure-vs-setup-failure confound. Neither source quantifies the retry/correction cost.

### Claim 3: The four Claude model classes are positioned by task type — Fable for the hardest problems, Opus for long-horizon work and coding, Sonnet for everyday work and analysis, Haiku for high-volume and routine tasks — illustrated with a multi-model insurance-claims example
- **Evidence**: Direct bullet-list positioning plus a worked example, in the "Useful Ways to Think About Cost" section.
- **Confidence**: settled (first-party description of current product lineup)
- **Quote**: "**Fable** for the hardest problems... **Opus** for long-horizon work and coding... **Sonnet** for everyday work and analysis... **Haiku** for high-volume and routine tasks." And the example: "For example, an insurance company might put a frontier model helping an adjuster evaluate a complex commercial claim while Haiku tags and triages the documents feeding into it."
- **Our assessment**: **Corroborates** `blog-anthropic-choosing-claude-model.md` Claim 4's four-class positioning (Mythos/Fable frontier, Opus reasoning-intensive enterprise tasks, Sonnet versatile/high-volume sub-agents, Haiku lowest-cost/high-frequency), but this article's phrasing is terser and shifted — it drops that note's benchmark citations (GDPval-AA, Terminal-Bench 2.1 for Opus) and instead labels Opus "long-horizon work and coding" rather than "reasoning-intensive enterprise tasks." This is a difference in emphasis, not a contradiction — both position Opus above Sonnet on capability and below Fable. The insurance-adjuster/document-triage example is new to the corpus: it is the first concrete named-industry example of the "multiple models on one project" pattern the choosing-model note only described abstractly.

### Claim 4: Cost controls sit on two separate surfaces — Claude Enterprise product controls (admin-facing) and Claude Platform/API controls (engineer-facing) — and most large customers use both
- **Evidence**: Direct statement opening the "How to See and Control Your Spend" section.
- **Confidence**: settled (first-party framing of the product/platform split)
- **Quote**: "The controls you have access to depend on whether Claude is running as a product for your employees or as an API behind your applications. The first puts controls with the admin, and the second with the engineers who build on it, and most large customers use both."
- **Our assessment**: This is a structural claim that organizes the rest of the article (and this source note) into two halves. It is a useful frame for the guide: cost governance is not a single control surface but two, owned by different roles (IT/admin vs. engineering), and an org running both Claude Enterprise and API-backed applications needs both sets of controls, not one or the other.

### Claim 5: Anthropic recommends working through the three Claude Enterprise cost controls in a specific order — access gating, then model controls, then hard spend caps — because it is hard to set a sensible spend limit before observing a month of real usage
- **Evidence**: Direct sequencing recommendation opening the "Cost Controls for Claude Enterprise" subsection.
- **Confidence**: settled (explicit first-party sequencing advice)
- **Quote**: "We generally suggest working through these in order, since it's hard to set a sensible limit before you've seen a month of real usage."
- **Our assessment**: This is new to the corpus and not present in `blog-anthropic-admin-analytics-cost-controls.md`, which documents the same three control types (access/model/spend-cap features) but as a feature list, not as a recommended sequence with a stated rationale. The rationale — caps need a baseline of real usage data to be set sensibly — is a concrete, actionable planning heuristic: don't set hard spend caps on day one of a rollout; gate access first, observe model usage, and only then cap spend once a month of real data exists.

### Claim 6: Access gating should be rolled out team-by-team via groups and custom roles rather than switched on for the whole org at once
- **Evidence**: Direct feature description and rollout recommendation in the "Cost Controls for Claude Enterprise" subsection.
- **Confidence**: settled (first-party description of a shipping admin-console feature, with an explicit rollout recommendation)
- **Quote**: "**Access gating** lets an admin determine the groups and custom roles that can use products like Claude Code and Claude Cowork, rather than an all-at-once switch. Start with one team, watch the results, and expand department by department."
- **Our assessment**: This is a specific rollout methodology (start with one team, expand department by department) that goes beyond the mere existence of role-based access control already documented in `blog-anthropic-cowork-enterprise.md` Claim 1 (SCIM-based RBAC) — that source establishes SCIM groups as the access-control mechanism, while this article adds a phased-rollout recommendation for how to use that mechanism when adopting Claude Enterprise cost controls specifically.

### Claim 7: Model controls operate at two distinct levels — entitlements (which models a team can access at all) and defaults (which model a new conversation starts on) — letting admins reserve the most capable models for teams doing the hardest work while defaulting everyone else to Sonnet
- **Evidence**: Direct feature description in the "Cost Controls for Claude Enterprise" subsection.
- **Confidence**: settled (first-party description of a shipping feature)
- **Quote**: "**Model controls** work at two levels. Entitlements determine which models a team can access, while defaults set which model a new conversation starts on. Admins can entitle teams doing your hardest work to the most capable models, and default everyone else to Sonnet."
- **Our assessment**: **Corroborates and sharpens** `blog-anthropic-admin-analytics-cost-controls.md` Claim 6, which describes "model defaults and entitlements" as a single combined feature ("let admins set which Claude model new conversations start with... Admins control which models are available to specific roles"). This article names entitlements and defaults as two separate levers rather than one bundled feature — a distinction useful for a guide checklist (an admin can restrict access to a model class without changing what a conversation defaults to, or vice versa).

### Claim 8: Hard spend caps place ceilings that bind immediately, and can be set at the org-wide, individual-user, or group level (where a group cap gives every member the same limit), but should only be set after establishing a usage baseline
- **Evidence**: Direct feature description in the "Cost Controls for Claude Enterprise" subsection, following directly from Claim 5's sequencing rationale.
- **Confidence**: settled (first-party description of a shipping feature)
- **Quote**: "**Hard spend caps** place ceilings on usage. Set them once you know your baseline for the full organization, for individual users, or for a group, in which case each member gets the limit. Caps bind right away."
- **Our assessment**: The three cap scopes (org/individual/group) are not distinguished in `blog-anthropic-admin-analytics-cost-controls.md`, which documents spend-threshold alerts (75%/90% admin, 75%/95% user) at what appears to be an org-level limit without naming per-user or per-group cap scopes. This article adds the scope options; neither article says whether per-user/per-group caps also carry the graduated 75%/90%/95% alert thresholds that note documents for the org-level cap, which is a gap the guide should flag rather than assume carries over.

### Claim 9: The same three usage-observability features documented previously (usage analytics dashboard, Analytics API, and natural-language analytics chat) are reiterated here as the Claude Enterprise tools for understanding spend, with a new example analytics-chat question
- **Evidence**: Direct feature descriptions in the "Tools to Observe Claude Usage" subsection.
- **Confidence**: settled (first-party description of shipping features, consistent with the July 2 announcement)
- **Quote**: "**Usage analytics** break spend down by person, team, and model. Data exports closely match invoices so that you can better reconcile usage with a bill." And: "**The Analytics API** makes the same data available to the systems a team already uses. Connect it to business intelligence tools, finance systems, and internal dashboards, so Claude spend can be evaluated alongside other costs like budgeting and forecasting." And: "**Analysis with analytics chat** lets admins ask about usage in plain language."
- **Our assessment**: **Corroborates** `blog-anthropic-admin-analytics-cost-controls.md` Claims 1, 3, and 4 almost exactly — same three features, same general capabilities (per-person/team/model breakdown, invoice reconciliation, BI-tool integration, natural-language querying). The example analytics-chat question given here ("Who are our top spenders this month?" / "Which team's usage grew fastest this quarter?") differs from that note's examples ("Which teams doubled their Claude usage this month?" / "Where are we getting the most value per seat?"), suggesting these are illustrative rather than fixed example prompts. No new capability is introduced; this article positions the trio as one of two categories of Enterprise controls (observe vs. constrain) rather than detailing each feature's UI as the July source did.

### Claim 10: On the Claude Platform, Workspaces separate API usage by product, team, or environment and appear as their own line in cost and usage reporting
- **Evidence**: Direct feature description opening the "Controls for Building on the API" section.
- **Confidence**: settled (first-party description of a shipping Console feature)
- **Quote**: "Workspaces separate API usage by product, team, or environment, and it has its own line in your cost and usage reporting."
- **Our assessment**: This is novel to the corpus — no prior source note documents Claude Console Workspaces as a cost-segmentation mechanism. It is the API-side analog of Claim 6's Enterprise access-gating-by-team pattern and Claim 9's group-filterable usage dashboard: the same "segment spend by team/product" principle, implemented at the API/Console layer rather than the Enterprise admin-console layer.

### Claim 11: Prompt caching, when reused reference material is sent with every call, costs 10% of the normal input rate on cache hits
- **Evidence**: Direct feature description with a specific pricing figure, in the "Controls for Building on the API" section.
- **Confidence**: settled (matches Anthropic's published prompt-caching pricing; also independently corroborated by a practitioner measurement)
- **Quote**: "**Prompt caching** stores content that gets reused across requests, so the model doesn't reprocess it every time. Turn it on if you send the same reference material with every call, which can cost 10% of the normal input rate on cache hits."
- **Our assessment**: **Corroborates** `blog-bswen-mcp-token-cost.md` Claim 8 ("Cache read costs 0.1x compared to base input") — the same 10%/0.1x figure, here from a first-party source rather than a practitioner's stated economics. This is the first time in the corpus this exact figure appears in an official Anthropic guide aimed at cost governance specifically (rather than in a Claude Code engineering post like `blog-anthropic-prompt-caching-everything.md`, which explains caching mechanics but does not state this percentage).

### Claim 12: Batch processing runs jobs that don't need an immediate answer at half price, and batch discounts stack with prompt-caching discounts
- **Evidence**: Direct feature description with a specific pricing figure and a worked example, in the "Controls for Building on the API" section.
- **Confidence**: settled (first-party description of a shipping pricing feature)
- **Quote**: "**Batch processing** runs jobs that don't need an immediate answer at half price like an e-commerce company classifying its catalog overnight. Move anything that can wait; batch discounts stack with caching."
- **Our assessment**: Novel to the corpus — no prior source note documents Claude's batch-processing discount or the specific claim that it stacks with prompt-caching discounts. The stacking claim is the more consequential detail for a cost-optimization checklist: a workload that both caches shared context and defers to batch could combine two independent discounts rather than choosing one lever over the other. This article gives no combined numeric example (e.g., an effective combined discount rate), so the stacking claim should be presented as a qualitative lever-combination point, not a quantified one.

### Claim 13: Two further API-level cost levers — the effort parameter (dialed down for routing/extraction, up for a final recommendation, so peak rates are paid only where needed) and the advisor strategy (a smaller model like Sonnet calls a frontier model at key moments, such as evaluating work before it ships) — let a workload pay for peak capability only on the calls that need it
- **Evidence**: Direct feature descriptions in the "Controls for Building on the API" section.
- **Confidence**: settled as stated first-party guidance; consistent with, but less quantified than, prior corpus coverage of the same two levers
- **Quote**: "**The effort parameter** controls how much reasoning the model does on a given call. Dial it down for routing and extraction, but turn it up for the final recommendation, so you pay peak rates only on the calls that need them." And: "**The advisor strategy** has a smaller model like Sonnet call a frontier model at key moments, like evaluating work before it ships. Run most of a task on a smaller model and pay for the larger model only where its judgment is applied."
- **Our assessment**: **Corroborates** `blog-anthropic-choosing-claude-model.md` Claim 7 (effort level as an independent axis from model class) and Claim 8 (the advisor strategy, with the quantified SWE-bench Pro figure: Sonnet 5 + Fable 5 advisor within 10% of Fable 5's score at 63% of the price). This article restates both patterns in more concrete per-call-type language (routing/extraction vs. final recommendation for effort; "evaluating work before it ships" for the advisor's trigger moment) but drops the earlier article's quantified benchmark — a guide citing the advisor strategy's cost/quality tradeoff should still cite the choosing-claude-model note for the number, and this article for the "when to invoke it" framing.

## Concrete Artifacts

### Claude Enterprise cost controls, recommended order (from source, "Cost Controls for Claude Enterprise" section)
```
Recommended sequence (per the article):
1. Access gating   — group/role-based, phased rollout (one team -> department by department)
2. Model controls   — entitlements (which models a team can access)
                       + defaults (which model a new conversation starts on)
3. Hard spend caps  — org-wide, per-user, or per-group; bind immediately;
                       set only after a baseline month of real usage
Rationale (verbatim): "it's hard to set a sensible limit before you've seen
a month of real usage."
```
*Source: https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude*

### Claude Platform (API) cost levers (from source, "Controls for Building on the API" section)
```
Workspaces        - separate API usage by product/team/environment;
                     own line in cost & usage reporting
Prompt caching     - reused content cached; 10% of normal input rate on
                     cache hits
Batch processing   - jobs that can wait run at half price;
                     STACKS with prompt-caching discount
Effort parameter   - dial down for routing/extraction, up for final
                     recommendation/output
Advisor strategy   - smaller model (e.g. Sonnet) calls a frontier model
                     at key moments (e.g. evaluating work before it ships);
                     most of the task still runs on the smaller model
```
*Source: https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude*

### Model family task-type mapping (verbatim, from source)
```
Fable  - for the hardest problems
Opus   - for long-horizon work and coding
Sonnet - for everyday work and analysis
Haiku  - for high-volume and routine tasks

Worked example: "an insurance company might put a frontier model helping
an adjuster evaluate a complex commercial claim while Haiku tags and
triages the documents feeding into it."
```
*Source: "Useful Ways to Think About Cost" section, same URL*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 6 (model
    defaults & entitlements) — this article names the same two levers
    (entitlements, defaults) but as explicitly separate mechanisms rather
    than one bundled feature description (Claim 7 here).
  - `blog-anthropic-admin-analytics-cost-controls.md` Claims 1, 3, 4
    (usage analytics dashboard, analytics chat, Analytics API) — same
    three features, same core capabilities, reiterated with a different
    example analytics-chat query (Claim 9 here).
  - `blog-anthropic-cowork-enterprise.md` Claim 1 (SCIM-based group/role
    access control) — this article's access-gating rollout recommendation
    (Claim 6 here) builds on the same group/role mechanism.
  - `blog-anthropic-choosing-claude-model.md` Claim 4 (four Claude model
    classes positioned by capability/use case) — same four classes, terser
    task-type phrasing here (Claim 3 here).
  - `blog-anthropic-choosing-claude-model.md` Claim 7 (effort level as an
    independent cost/quality axis) and Claim 8 (the advisor strategy,
    with the SWE-bench Pro benchmark figure) — both levers restated here
    in per-call-type language without the earlier article's quantified
    benchmark (Claim 13 here).
  - `blog-bswen-mcp-token-cost.md` Claim 8 ("Cache read costs 0.1x
    compared to base input") — same figure (10% / 0.1x), now stated by a
    first-party source in a cost-governance-focused article rather than a
    practitioner's own stated economics (Claim 11 here).

- **Contradicts**: None identified. This article's Opus positioning
  ("long-horizon work and coding," Claim 3) is terser than, but not in
  tension with, `blog-anthropic-choosing-claude-model.md` Claim 4's
  ("reasoning-intensive enterprise tasks," with named benchmarks) — both
  place Opus above Sonnet and below Fable/Mythos on capability; neither
  claims a different relative ordering. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-admin-analytics-cost-controls.md` — this article adds
    a recommended sequencing (access gating -> model controls -> hard
    spend caps, Claim 5), a stated rationale for that order (need a month
    of baseline usage before setting caps), the team-by-team access-gating
    rollout method (Claim 6), and the three spend-cap scopes — org/
    individual/group (Claim 8) — none of which appear in that source.
  - `blog-anthropic-choosing-claude-model.md` — this article's Claim 2
    (mismatch cost runs in both directions: undermatching costs via
    retries, overmatching costs via unused capability) complements that
    note's Claim 1/Claim 2 (start with the strongest model to avoid the
    model-failure-vs-setup-failure confound); read together they cover
    both the "why start strong" and "why don't over-provision" sides of
    model selection.
  - `blog-anthropic-prompt-caching-everything.md` — that source explains
    caching mechanics (four-layer hierarchy, cache-breaking pitfalls,
    cache-safe compaction) in depth but does not state a specific
    cache-hit discount percentage; this article supplies that number
    (10% of normal input rate, Claim 11) in a governance context.

- **Novel**:
  - **The cost-per-outcome framing with its two-question diagnostic**
    (Claim 1) — no prior corpus source states this specific metric
    substitution (outcome value vs. token consumption) with this
    diagnostic pair.
  - **Batch processing at half price, stacking with prompt-caching
    discounts** (Claim 12) — first corpus source to document Claude's
    batch-processing discount at all, and the only one to claim it
    stacks with caching.
  - **Claude Console Workspaces as a cost-segmentation mechanism**
    (Claim 10) — first corpus source to document Workspaces.
  - **The recommended admin-control sequencing and its baseline-usage
    rationale** (Claim 5) — first corpus source to give an explicit order
    of operations for standing up Claude Enterprise cost controls.
  - **The insurance-adjuster/document-triage worked example** (Claim 3)
    — first concrete named-industry example in the corpus of the
    multiple-models-on-one-project pattern.

## Guide Impact

- **Chapter 05 (Team Adoption — enterprise cost governance)**: Add the
  recommended control sequencing (Claim 5: access gating -> model
  controls -> hard spend caps, with the "wait for a month of real usage"
  rationale) as a concrete rollout checklist, replacing any generic
  "set up cost controls" guidance with an explicit order and the reason
  for it. Add the three hard-spend-cap scopes (org/individual/group,
  Claim 8) and the team-by-team access-gating rollout method (Claim 6)
  as specifics currently missing from the chapter's coverage of
  `blog-anthropic-admin-analytics-cost-controls.md`.
- **Chapter 02/04 (Model Selection / Cost Optimization)**: Add Claim 1's
  cost-per-outcome framing and two-question diagnostic as the opening
  principle for a "how to think about AI cost" section, ahead of any
  tactical levers (caching, batching, effort, model choice). Add Claim 2
  (mismatch cost runs both directions) alongside the existing
  `blog-anthropic-choosing-claude-model.md` coverage to complete the
  "why model matching matters" argument with the overmatching side that
  note does not cover.
- **Chapter 04 (Cost Optimization — API levers)**: Add batch processing
  (Claim 12: half price, stacks with caching) as a new lever in the
  chapter's cost-lever toolbox — currently absent from the corpus. Add
  the specific 10% cache-hit-rate figure (Claim 11) as a citable number
  for the prompt-caching lever, corroborated independently by
  `blog-bswen-mcp-token-cost.md`. Add Workspaces (Claim 10) as the
  API-side complement to Enterprise access gating for cost segmentation
  by team/product/environment.

## Extraction Notes

- The article was fetched via WebFetch twice with different prompts: one
  broad full-text extraction pass, and one targeted verbatim-quote
  verification pass asking specifically for the 20 sentences/bullets used
  as quotes in this note. Both passes returned identical wording for
  every quoted passage, giving reasonable confidence the quotes are
  faithful to the source, though WebFetch processes HTML through an
  intermediate model rather than returning raw text — the Assayer should
  spot-check against the live URL per standard practice.
- The article is short (~5 minute read) and fully accessible, no paywall.
  It links out to product-documentation pages for each named lever
  (effort, advisor tool, prompt caching, batch processing, Analytics API,
  Workspaces, and three Enterprise support articles for access
  gating/model controls/spend caps). None of these were followed as
  additional sources: they are reference documentation for features this
  article already describes at a level of detail sufficient for
  extraction, not additional argument or evidence to mine. A future
  Miner pass on any of those individual doc pages (e.g., the effort or
  advisor-tool documentation) could add implementation-level detail this
  article does not cover.
- The closing claim ("these features can routinely cut the cost of a
  production workload substantially before anyone touches a budget line")
  is deliberately not extracted as its own numbered claim — it is a
  vague, unquantified summary sentence with no example or figure behind
  it, so it is folded into Claim 13's assessment rather than presented as
  independent evidence.
- No contradiction with any existing source note was found during
  cross-referencing; see Cross-References "Contradicts" above for the
  near-miss (Opus positioning) that was evaluated and judged not to be a
  real contradiction — a difference in phrasing terseness, not a
  disagreement about relative model capability.
