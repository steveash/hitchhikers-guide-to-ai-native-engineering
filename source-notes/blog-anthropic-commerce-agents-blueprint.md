---
source_url: https://claude.com/blog/claude-for-commerce-agents
source_type: blog-post
title: "Building commerce agents with Claude"
author: Anthropic (Claude team)
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: emerging
issue: "#3188"
---

# Building commerce agents with Claude

> Official Anthropic launch of a commerce-agent blueprint (shopping agent +
> merchant agent reference implementations, `anthropics/commerce-agents` on
> GitHub) paired with a companion engineering deep-dive,
> "[A guide to the anatomy of effective commerce agents](https://claude.com/blog/the-anatomy-of-effective-commerce-agents)"
> (same date), which supplies the concrete architecture, performance, and
> production-readiness guidance the announcement itself only gestures at.

## Source Context

- **Type**: blog-post (official claude.com/blog product announcement,
  September 2, 2026) plus a linked first-party engineering companion post
  (same date, same domain) that this note treats as part of the same source
  event per MINER.md §1's instruction to follow substantive linked pages.
- **Author credibility**: First-party Anthropic — house-authored product
  announcement and engineering post, not bylined to a named individual.
  Maximum authority on what Anthropic recommends and ships, but the headline
  metric (35% larger carts, 60% more purchase completion) is Anthropic's own
  aggregate characterization of unnamed "retailers running shopping agents on
  Claude," not an independently audited or per-customer study — treat as a
  vendor-reported directional figure. The nine customer testimonials
  (Shopify, Priceline, Visa, Accenture, Mastercard, Intuit, Klaviyo, Wix,
  Zomato, Fetch, Square) are named individuals with titles at named
  companies, which raises them above generic marketing pull-quotes, but they
  are still solicited praise quotes chosen by Anthropic for publication, not
  independently sourced interviews.
- **Scope**: Covers what the commerce blueprint provides (shopping agent +
  merchant agent reference implementations, deployment targets, guardrails),
  why enterprises are adopting it (nine testimonials), and — via the linked
  "anatomy" deep-dive — the specific architectural, performance, and
  production-readiness patterns behind it: skills-vs-subagents architecture,
  prompt-caching design, model selection method, safety enforcement for
  money-moving actions, memory storage, evaluation practice, and multi-team
  ownership. Does NOT cover: the actual code in the `anthropics/commerce-agents`
  repository (not fetched — GitHub source, out of scope for a text-source
  extraction), the vertical demo sites, or the referenced webinar content.
  The "anatomy" post's full prose could not be reproduced verbatim due to a
  copyright-reproduction guard in the fetch tool used (see Extraction Notes);
  quotes below for that post are short, individually verified verbatim
  fragments rather than full-paragraph excerpts.

## Extracted Claims

### Claim 1: Retailers running shopping agents on Claude have seen materially larger carts and higher purchase-completion rates
- **Evidence**: Headline statistic on the announcement post, presented without a named source study, sample size, or methodology — an aggregate vendor characterization of customer outcomes.
- **Confidence**: anecdotal
- **Quote**: "Retailers running shopping agents on Claude have seen carts up to 35% larger and shoppers 60% more likely to complete a purchase."
- **Our assessment**: Directionally plausible (multi-item planning and in-conversation checkout removing friction is a reasonable mechanism for both effects) but not verifiable from this source alone — no denominator, no named retailer, no comparison methodology (vs. no agent? vs. a worse agent?) is given. Use as a vendor-reported headline figure, not a benchmark.

### Claim 2: The commerce blueprint ships complete, working reference implementations of a shopping agent and a merchant agent, buildable via the Messages API, Agent SDK, or Claude Managed Agents (beta), and deployable via Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI
- **Evidence**: First-party description of the repository's contents and deployment surface.
- **Confidence**: settled
- **Quote**: "The code deploys where you already build with Claude, including the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI."
- **Our assessment**: Consistent with Anthropic's general platform-portability positioning elsewhere in the corpus (Managed Agents, Bedrock/Vertex support). The three build paths (raw Messages API, Agent SDK, Managed Agents beta) being offered simultaneously for one reference implementation is notable — it signals Anthropic wants the same blueprint to work whether a team hand-rolls its harness or buys the managed layer.

### Claim 3: The shopping agent is designed to handle multi-item, natural-language requests end-to-end — search, comparison, cart assembly, and in-conversation customer service — inside the retailer's own app or site, with payment left to the retailer's existing checkout or an agentic-payments provider
- **Evidence**: First-party functional description with a concrete example query.
- **Confidence**: settled
- **Quote**: "A customer can say 'I need a tent, sleeping bag, and stove for a weekend trip with two kids,' and the agent can take it from there."
- **Our assessment**: The explicit choice to leave payment integration to the retailer (rather than bundling a payments product into the blueprint) is a meaningful scoping decision — it keeps the blueprint payment-rail-agnostic and defers a hard, regulation-heavy problem to specialized providers. Folding customer-service Q&A (order status, returns, refund policy) into the same conversation rather than deflecting to a support page is the concrete instance of the "tightly coupled session across multiple intents" argument made in Claim 6 below.

### Claim 4: The shopping agent's guardrails constrain prices and products to actual catalog data and are explicitly designed to avoid manipulative upsell patterns
- **Evidence**: First-party guardrail description, stated as a design property of the reference implementation rather than an optional add-on.
- **Confidence**: settled
- **Quote**: "The agent features guardrails designed to constrain prices and products to actual catalog data, and avoids manipulative upsell patterns."
- **Our assessment**: This is a trust/safety claim specific to commerce (hallucinated prices or invented products would be directly financially harmful to both retailer and customer, and manipulative upsell is a reputational and possibly regulatory risk). The post gives no mechanism detail here (e.g., whether this is prompt-level instruction, tool-level catalog-lookup enforcement, or an eval gate) — the "anatomy" post's safety-enforcement claim (Claim 10 below) is the more mechanistic companion to this claim, but it addresses money-moving/business-changing actions specifically, not upsell-pattern avoidance, so this remains a claim of intent without a documented enforcement mechanism.

### Claim 5: The merchant agent requires human approval before any of its proactively suggested changes go live
- **Evidence**: First-party description of the merchant agent's human-in-the-loop design.
- **Confidence**: settled
- **Quote**: "When the agent proactively suggests a change, a person approves it before anything goes live, meaning users get the final say while their agent watches the store."
- **Our assessment**: This is the announcement-post-level statement of the same principle the "anatomy" post states more mechanistically in Claim 10 ("no model tool call moves money or changes the business... changes are staged for approval"). Consistent, two-layer confirmation (marketing framing + engineering mechanism) from the same source event increases confidence this is a real design constraint, not just messaging.

### Claim 6: For commerce agents, a single agent with skills consistently outperforms both a monolithic one-prompt design and a subagent (orchestrator/handoff) design on quality, because a commerce conversation is one tightly coupled session across many intents and turns
- **Evidence**: First-party architectural claim from the "anatomy" companion post, framed as a comparative finding from building the reference implementations, not a hypothesis.
- **Confidence**: emerging
- **Quote**: "a single agent with skills consistently has outperformed both the one-prompt-for-everything design and the subagent design on quality"
- **Our assessment**: This is a specific, falsifiable-sounding comparative claim ("consistently... outperformed"), but the post gives no eval numbers, sample size, or task breakdown to back the comparison — it reads as an internal finding stated without supporting data in the fetched text. It also lands in direct tension with `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7: orchestrator-subagent is the recommended default pattern for practitioners starting out), which is a different first-party Anthropic post with no stated carve-out for tightly-coupled conversational domains. We filed **[contradiction #3203](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3203)** for this — see Cross-References below. Do not resolve the tension in this note; the two claims may reconcile via a conditioning variable (tightly-coupled multi-turn conversation vs. decomposable/parallelizable workflow) but neither source states that boundary explicitly.

### Claim 7: Every handoff to a subagent is a state-lossy operation that degrades quality in tightly coupled conversational domains
- **Evidence**: First-party mechanistic explanation for why Claim 6's comparative finding holds — the stated failure mode of the subagent design specifically.
- **Confidence**: emerging
- **Quote**: "Every handoff to a subagent is a state-lossy operation, which often impacts the quality"
- **Our assessment**: This is a specific, named mechanism (state loss at handoff boundaries) rather than a vague preference — useful because it's testable in principle and gives a reason a reader could check against their own domain ("does my agent's work decompose into loosely-coupled subtasks, or is it one continuous multi-intent conversation?"). It corroborates the general shape of `blog-fowler-garg-orchestrator-tax.md`'s "cognitive locality" argument (subagents are justified by what they keep *out* of the orchestrator's context, not by raw task splitting) — both sources treat context/state preservation, not parallelism, as the deciding factor for whether to split into subagents. Garg's source is a single coding-refactor incident, though, not a production conversational system, so it's a corroborating data point at a different level of rigor, not a duplicate claim.

### Claim 8: Content needed on most turns belongs in the system prompt; the rest should be built as skills, with the frequency of need (roughly one-third or more of traffic) as the deciding threshold
- **Evidence**: First-party design heuristic from the "anatomy" post's architecture section, applied concretely to the shopping agent (product search in the prompt; search-discovery, purchase-research, planning-goals, customer-care, and memory-personalization as skills).
- **Confidence**: emerging
- **Quote**: "Anything the agent needs on most turns generally goes in the system prompt"
- **Our assessment**: This gives a concrete, numeric-ish rule of thumb (~1/3 of traffic) for a decision that's usually made by intuition — worth extracting precisely because most sources in the corpus discuss "system prompt vs. skills/tools" qualitatively without a frequency threshold. Should be paired with prompt-caching guidance (Claim 9) in the guide, since stuffing low-frequency content into the system prompt also inflates the cached prefix unnecessarily.

### Claim 9: Production commerce deployments should design for 90-99% prompt-cache hit rates; cached input token reads cost roughly a tenth of fresh ones, with a 1.25x write premium that pays for itself on the second use
- **Evidence**: First-party performance-optimization guidance from the "anatomy" post, stated as an observed range from real deployments plus specific unit-economics figures.
- **Confidence**: settled
- **Quote**: "Best commerce deployments we've seen run at 90–99% cache hit rates" / "Cached input token reads cost a tenth of fresh ones"
- **Our assessment**: This is consistent with and extends `blog-anthropic-prompt-caching-everything.md`'s framing of caching as foundational to feasible long-running agentic products — that note covers Claude Code's harness-level caching architecture (4-layer hierarchy, cache-safe compaction forking), while this claim gives a concrete target metric (90-99% hit rate) and unit cost ratio specific to commerce/conversational deployments. The two sources corroborate each other's core thesis (caching is not an optimization, it's a design constraint) from different domains — worth citing together in a harness-engineering chapter section on caching.

### Claim 10: Model and reasoning-effort selection should be decided by measurement (running the full eval suite across candidate models/effort levels, weighted by real query distribution), not by defaulting to a model tier
- **Evidence**: First-party methodology claim from the "anatomy" post's performance section, with a concrete named example of the trade-off it's meant to resolve.
- **Confidence**: emerging
- **Quote**: "You should choose both by measurement"
- **Our assessment**: The named example — "Opus 5's lift on cart-driving tasks justifies the cost difference over Sonnet, and sometimes it doesn't" (per the earlier summary pass; not independently re-verified verbatim, see Extraction Notes) — frames this as a per-task-type decision rather than a single account-wide model choice. This is a specific, actionable instantiation of a general "eval-driven model selection" principle that recurs informally across the corpus; this source ties it concretely to commerce task categories (cart-driving vs. other task types).

### Claim 11: No model tool call is permitted to directly move money or change the business; all such changes are staged for approval, use server-issued and tracked IDs, are subject to enforced transaction caps, and third-party content is sanitized before reaching the model
- **Evidence**: First-party safety-enforcement architecture from the "anatomy" post's production-readiness section — the mechanistic backbone behind the announcement post's "a person approves it before anything goes live" claim (Claim 5).
- **Confidence**: settled
- **Quote**: "No model tool call moves money or changes the business."
- **Our assessment**: This is a strong, unambiguous architectural boundary (not "the model is instructed not to," but "the tool call itself cannot") — the strongest guardrail-design claim in this source. It corroborates `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`'s "automated oversight" tier (financial constraints, contractual scanning, and failsafes enforced at the infrastructure layer, not as human-authored policy alone) — both sources converge on enforcing financial/business-changing boundaries in code/infrastructure rather than relying on model instruction-following. Different domains (commerce agent tool design vs. general enterprise agent legal/governance framework) converging on the same enforcement principle strengthens confidence in the underlying pattern.

### Claim 12: Long-term memory belongs in the surrounding systems (a typed database), not in the model's context window, and should be extracted asynchronously after conversations to avoid adding latency, with user-facing controls over what's retained and deletion capability
- **Evidence**: First-party memory-architecture guidance from the "anatomy" post's production-readiness section.
- **Confidence**: emerging
- **Quote**: "Memory belongs in your systems, not in the model"
- **Our assessment**: Corroborates `blog-anthropic-claude-managed-agents-memory.md` (Claim 2: memories stored as files mounted on a filesystem, accessed via bash/code execution — external to model context) — both sources agree memory should live outside the model's context and be system-managed, though the two describe different concrete mechanisms (typed DB with categories/retention here vs. filesystem-mounted files in Managed Agents memory). The asynchronous-extraction-to-avoid-latency detail and explicit user deletion rights are new specifics not covered in the Managed Agents memory note, which focuses more on cross-agent sharing and versioning than on latency or user control.

### Claim 13: Commerce-agent evaluation should use snapshot-state test construction (build the precondition state, then append the test message) rather than full multi-turn conversation simulation, and should pair positive cases with negative counterparts across core requests, context-dependent cases, safety scenarios, interface validation, and multi-capability requests
- **Evidence**: First-party evaluation-methodology guidance from the "anatomy" post's production-readiness section.
- **Confidence**: emerging
- **Quote**: "Constructing the test state, appending the test user message"
- **Our assessment**: The snapshot-over-full-simulation approach is a practical answer to a common eval-authoring pain point (multi-turn conversation simulations are expensive to write and brittle to maintain). The explicit inclusion of "negative cases alongside positive ones" and "safety scenarios" as a named eval category is the evaluation-side complement to Claim 11's tool-level guardrails — testing that the guardrail holds, not just that it exists.

### Claim 14: Multi-team commerce-agent development should assign single-owner teams to each skill/tool, run CI against relevant eval subsets on change, and treat the agent as one unified deployment unit rather than independently shippable components
- **Evidence**: First-party organizational/governance guidance from the "anatomy" post's production-readiness section.
- **Confidence**: emerging
- **Quote**: "Every skill and tool has a single owner team"
- **Our assessment**: This is an org-design claim (ownership + CI-on-subset + unified-deployment) rather than a technical one — it's the multi-team analog of Claim 8's "system prompt vs. skills" split: skills are the unit of both architectural decomposition and team ownership. Worth flagging for a chapter on scaling agent development across teams, since it gives a concrete governance pattern (owner-per-skill, CI-on-touched-subset) rather than just asserting "coordinate carefully."

## Concrete Artifacts

```
Headline metric (announcement post, unattributed aggregate):
"Retailers running shopping agents on Claude have seen carts up to 35%
larger and shoppers 60% more likely to complete a purchase."

Named customer testimonials (announcement post), with company + role:
- Visa — Jack Forestell, Chief Product and Strategy Officer
- Mastercard — Sherri Haymond, EVP, Global Head of Digital Commercialization
- Accenture — Kath Gramling, Global Consumer Goods, Retail and Travel lead
  ("85% are now open to collaboration with an AI agent and nearly three in
  four would trust a personal AI agent more than their best friend to make
  a purchase on their behalf" — Accenture research cited within the quote,
  not independently sourced by this note)
- Priceline — Cobus Kok, VP AI Experiences (their assistant "Penny" runs on
  Claude)
- Intuit — Chris Kasten, Chief Architect and SVP of Engineering
- Shopify — Vanessa Lee, VP Product (building a reference storefront via
  Catalog, UCP, and Shop Sign-in)
- Klaviyo — Andrew Bialecki, Founder and Co-CEO
- Wix — Dror Zalika, Head of Commerce ("working commerce agent taking
  prompts within fifteen minutes")
- Zomato — Akhil Bansal, Senior Engineering Manager ("Our engineers had the
  blueprint running with no blockers; the setup worked exactly as
  documented. The practices it bakes in, from tool iteration limits to
  prompt caching, are the ones we recognized from building Zomato's own
  agent. Teams standing up their first agent on Claude will skip weeks of
  trial and error.")
- Fetch — Ashley Nader, Staff Product Manager ("Our engineers had both
  commerce agents from Anthropic's blueprint running locally in well under
  an hour, with live conversations working on the first attempt. We ran
  the Claude Code workflow twice and got two different architectures back,
  each designed to what we'd asked for. For a team starting from scratch,
  that turns days of agent scaffolding into hours.")
- Square — Willem Avé, Head of Product

Shopping agent capability list (announcement post, verbatim bullets):
- Search the catalog and assemble the right set of items, including
  multi-item requests.
- Remember the customer's preferences and tailor what it suggests.
- Show products, comparisons, and the cart right in the conversation, not
  just as text.
- Build the cart and hand it to checkout.
- Answer customer service questions in the same conversation, like where
  an order is, how to return or exchange an item, and what the refund
  policy says, instead of sending the customer to a support page.

Merchant agent capability list (announcement post, verbatim bullets):
- Answer questions about sales performance like what's selling and what
  isn't.
- Track inventory and proactively flag problems, like an item about to
  sell out before a promotion starts.
- Recommend pricing and promotions based on the store's own sales history.
- Draft marketing campaigns to move the products that need moving.

Getting-started steps (announcement post):
1. Fork the repository at github.com/anthropics/commerce-agents.
2. Read the engineering deep-dive at
   claude.com/blog/the-anatomy-of-effective-commerce-agents.
3. See the vertical demos and request a working session at
   claude.com/solutions/commerce.

"Anatomy" companion post — three-part structure (paraphrased section
headings; full prose not reproducible verbatim per fetch-tool copyright
guard, see Extraction Notes):
  Part 1: Architecture — skills over subagents; system-prompt-vs-skills
    frequency threshold; UI components implemented as tools.
  Part 2: Performance Optimization — latency reduction (fewer turns,
    faster tools, perceived-latency techniques); prompt caching
    (90-99% hit rate target, cache economics); model/effort selection by
    measurement.
  Part 3: Production Readiness — memory management (external, async,
    deletable); safety enforcement (no model tool call moves
    money/changes the business); evaluation practice (snapshot-state,
    positive+negative cases); multi-team ownership (single owner per
    skill/tool, CI on subsets).
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-prompt-caching-everything.md` — both sources treat
    prompt caching as a foundational architectural constraint rather than
    an optional optimization; this note adds a concrete commerce-specific
    target (90-99% cache hit rate) and unit-cost figures (10x cheaper
    cached reads, 1.25x write premium) that the caching-everything note
    (Claude Code harness-level) does not state.
  - `blog-anthropic-claude-managed-agents-memory.md` (Claim 2) — both agree
    memory should live outside model context and be system-managed
    (filesystem-mounted files there vs. a typed database here); this note
    adds asynchronous post-conversation extraction and explicit user
    deletion rights as specifics not covered there.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (Claim 5)
    — both converge on enforcing money-moving/business-changing actions at
    the infrastructure/code layer rather than via model instruction alone
    (Thoughtworks' "automated oversight" tier vs. this source's "no model
    tool call moves money" boundary), from unrelated domains (enterprise
    legal governance framework vs. commerce agent tool design).
  - `blog-fowler-garg-orchestrator-tax.md` — Garg's "cognitive locality"
    argument (subagents justified by context isolation, not task-splitting)
    is directionally consistent with this source's "state-lossy handoff"
    reasoning (Claim 7), though Garg's source is a single coding-refactor
    incident and this source is a production commerce architecture claim —
    different rigor levels, same underlying mechanism.

  - **Contradicts**: `blog-anthropic-multi-agent-coordination-patterns.md`
    (Claim 7: orchestrator-subagent is the recommended default pattern for
    practitioners starting multi-agent system design). This source's Claim
    6 states that for commerce/conversational agents, single-agent-with-skills
    "consistently outperformed... the subagent design on quality" — a
    direct architectural tension for any tightly-coupled conversational
    domain. Filed as
    **[contradiction #3203](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3203)**;
    no verdict is asserted here — see that issue and its eventual
    CONTRADICTIONS.md entry for resolution.

- **Extends**:
  - `blog-anthropic-claude-managed-agents.md` and
    `blog-anthropic-building-enterprise-agents.md` — both are prior
    first-party Anthropic posts on general enterprise agent
    infrastructure/strategy; this source is the first domain-specific
    (commerce) blueprint with concrete reference implementations,
    guardrails, and named production customers in this specific vertical.
  - `blog-bvp-shopify-ai-playbook.md` — that note covers Shopify's internal
    engineering-org AI rollout (LLM proxy, no autonomous merging, etc.);
    this source's Shopify testimonial is about a different, external-facing
    product (a customer-facing commerce agent reference storefront) — same
    company, unrelated context, not a corroboration or contradiction, just
    a second, distinct Shopify data point in the corpus.

- **Novel**:
  - First source-note-level documentation of a domain-specific (commerce)
    agent blueprint with paired shopping-agent/merchant-agent reference
    implementations and named enterprise validation across retail, travel,
    payments, and SaaS-for-commerce companies.
  - The frequency-based system-prompt-vs-skills threshold (~1/3 of traffic,
    Claim 8) and the snapshot-state eval-construction method (Claim 13) are
    both specific, actionable heuristics not previously captured elsewhere
    in the corpus in this concrete a form.
  - The "no model tool call moves money or changes the business" phrasing
    (Claim 11) is the most unambiguous single-sentence articulation of the
    money-movement guardrail principle found in the corpus to date.

## Guide Impact

- **Ch02/Ch03 (multi-agent architecture)**: Add Claim 6/7 (skills over
  subagents for tightly coupled conversational domains) as a named
  exception/conditioning case to the orchestrator-subagent-as-default
  guidance from `blog-anthropic-multi-agent-coordination-patterns.md`,
  once contradiction #3203 is resolved. Until resolved, do not assert
  either as the guide's blanket recommendation for conversational agents.
- **Ch02/Ch03 (tool/skill design)**: Add the frequency-based system-prompt-
  vs-skills threshold (Claim 8, ~1/3 of traffic) as a concrete decision
  rule, and the "UI components as tools, not generated markup" pattern
  (mentioned in Concrete Artifacts, Part 1) as a specific technique for
  agents with rich in-conversation UI.
- **Harness engineering / performance chapter**: Add the 90-99% cache-hit-
  rate target and cache economics (Claim 9) alongside the existing
  `blog-anthropic-prompt-caching-everything.md` material as commerce-domain
  confirmation that caching design is not optional at production scale.
- **Ch04 (guardrails and safety)**: Add "no model tool call moves money or
  changes the business" (Claim 11) as a named, quotable architectural
  boundary for any agent with financial or state-changing side effects,
  cross-referenced with the Thoughtworks scope-of-authority framework's
  automated-oversight tier.
- **Evaluation chapter (if planned)**: Add the snapshot-state eval
  construction method and the positive/negative-case pairing requirement
  (Claim 13) as a concrete alternative to full multi-turn conversation
  simulation for eval authoring.

## Extraction Notes

- **Two-post extraction**: This note combines the announcement post
  (`claude.com/blog/claude-for-commerce-agents`) and its linked engineering
  companion (`claude.com/blog/the-anatomy-of-effective-commerce-agents`,
  published the same day and explicitly pointed to by the announcement as
  "an engineering deep-dive on how it was built") per MINER.md's
  instruction to follow substantive linked pages. Claims are attributed to
  the specific post they came from in each claim's Evidence line.
- **Verbatim limitation on the "anatomy" post**: The fetch tool used to
  read the "anatomy" post refused full-paragraph verbatim reproduction,
  citing fair-use limits, and would only return short (under-125-character)
  verbatim fragments plus its own paraphrased summaries. Every `Quote` field
  drawn from that post above was independently requested and returned as a
  short, tool-confirmed verbatim fragment — not reconstructed from the
  paraphrase. Where a claim (Claim 10) relies on a detail that was only
  available from an earlier, unverified summarization pass (the Opus 5 vs.
  Sonnet cart-driving example), this is explicitly flagged in that claim's
  "Our assessment" as not independently re-verified verbatim, per MINER.md
  §2a's instruction to prefer an honest gap over a fabricated quote.
- **GitHub repository not fetched**: `anthropics/commerce-agents` (the
  actual blueprint code) was not fetched or extracted — this is a text-source
  (blog-post) extraction per the issue's `triaged:text` label, and the code
  repository is a separate artifact that a future source submission could
  target if deemed worth a dedicated extraction pass.
- **Contradiction filed before this note**: Per MINER.md §4a, contradiction
  #3203 (skills-vs-subagents default) was filed prior to writing this note;
  no verdict is asserted in Claim 6/7 or Cross-References — that is left to
  the resolver.
- **Testimonial quotes**: All nine named testimonials were reproduced by
  the fetch tool as full quoted paragraphs (not subject to the copyright
  guard that blocked the "anatomy" post's prose, likely because block-quote
  attributed testimonials aren't treated as "substantial" reproduction by
  the tool's own heuristic). The headline metric and two testimonial quotes
  used in claims above were independently re-fetched and confirmed
  character-for-character identical across two separate fetch calls.
