---
source_url: https://openai.com/index/cars24
source_type: blog-post
title: "How Cars24 scales conversations and builds faster with OpenAI"
author: OpenAI (customer case study; named quotes from Vikram Chopra, Builder, Cars24, and Jayesh Gupta, Builder—AI & Innovation, Cars24)
date_published: 2026-07-16
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: anecdotal
issue: "#2323"
---

# How Cars24 scales conversations and builds faster with OpenAI

> An OpenAI customer case study on Cars24, an India-based used-car marketplace, describing OpenAI-built voice/chat agents that handle a multi-week, multi-channel buy/sell funnel (1M+ conversation-minutes/month, 12% lost-seller-lead recovery), plus a second, distinct thread on embedding Codex into the software development lifecycle via Linear and spreading agentic workflows to ~600 non-engineering employees (85-90% daily active usage).

## Source Context

- **Type**: blog-post (OpenAI "Customer Stories" case study, `openai.com/index/cars24`, published July 16, 2026; ~650 words, auto-discovered via the `openai-news` trusted feed). Structured with a company metadata block (Company size: Enterprise, Region: Asia-Pacific & Oceania, Industry: Technology, Products: API, ChatGPT, Codex) and a four-metric "Results at a glance" stat box, consistent with the template already documented for BBVA (`blog-openai-bbva-banking-transformation.md`), Endava (`blog-openai-endava-frontiers.md`), Notion (`blog-openai-notion-codex-case-study.md`), and Samsung (`blog-openai-samsung-chatgpt-codex-deployment.md`).
- **Author credibility**: House-authored OpenAI promotional copy — OpenAI has a direct commercial incentive to present its APIs and Codex favorably. Two named individuals are quoted, both with the internal Cars24 title "Builder": Vikram Chopra ("Builder, Cars24" — a co-founder title dressed as a role name rather than a conventional executive title like CEO/CTO) and Jayesh Gupta ("Builder—AI & Innovation, Cars24"). No third-party verification of the headline metrics (1M+ conversation minutes, 50% support-resolution increase, 80% turnaround reduction, 12% lead recovery) is given anywhere in the piece — no methodology, baseline, or measurement window is disclosed for any of the four stat-box figures.
- **Scope**: Covers (1) a customer-facing voice/chat agent workflow spanning the full car buying and selling journey (discovery, financing, test-drive scheduling, follow-up, after-sales), (2) Codex embedded into the software development lifecycle via Linear ticket creation/grooming and GitHub work summarization, (3) Codex spreading beyond engineering into finance, legal, marketing, and operations, including two named finance workflows and informally-built "chief of staff" agents, and (4) an aggregate internal-adoption figure (~600 employees, 85-90% daily active usage). Does NOT cover: any technical detail of the voice/chat agent architecture (model used, latency, escalation-to-human logic, language/dialect handling for the Indian market), the size of the engineering team or overall company headcount, a rollout timeline, cost/pricing, or any account from a Cars24 customer (buyer or seller) describing their own experience with the agent.

## Extracted Claims

### Claim 1: Car buying and selling in India is a multi-week, multi-channel process (calls, document checks, follow-ups) rather than a single e-commerce session, which OpenAI frames as the core scaling challenge Cars24's agents were built to solve
- **Evidence**: Narrator (OpenAI-authored) framing statement describing the market context before introducing the agent workflow.
- **Confidence**: anecdotal (unattributed narrator claim about market structure; not sourced to any external market-research citation)
- **Quote**: "Unlike traditional e-commerce, car buying and selling in India rarely happens in a single session. Much of the process happens outside the app, across calls, document checks, and follow-ups that can take days or weeks."
- **Our assessment**: This is a plausible and specific framing of why a conversation-heavy, long-horizon agent (rather than a single-turn chatbot) was the chosen solution shape — the claim ties the technical design (persistent, multi-touchpoint agents that follow up over days) directly to a named structural feature of the market (fragmented, multi-session, partially offline transactions). It is scene-setting rather than an evaluable metric, but it is more specific than typical "AI transforms X industry" framing because it names the mechanism (process spans calls + documents + follow-ups over days/weeks) that makes single-session automation insufficient.

### Claim 2: Cars24 built voice and chat agents, using OpenAI's APIs, that carry a buyer through the full journey — budget/needs intake, car recommendation from the Cars24 catalog, test-drive booking, financing exploration, pre-visit confirmation and reschedule handling, post-visit follow-up, and post-purchase support (feedback, warranty, returns, after-sales)
- **Evidence**: Detailed narrator description of the buyer-side agent workflow, step by step, in the "Automating the full customer journey with AI agents" section.
- **Confidence**: anecdotal (narrator description of a workflow design; no metric attached to any individual step, no completion/conversion rate disclosed for the funnel as a whole)
- **Quote**: "When a buyer calls Cars24, an AI agent asks about their budget, family size, commute needs, and preferred car type. It recommends cars from the Cars24 catalog, books a test drive, and can help the customer explore financing. The agent then follows up before the test drive to confirm the visit, suggest alternative cars if preferences have changed, and collect additional details for financing. After the visit, an AI agent checks whether the customer wants to move forward, book another visit, or explore a different option."
- **Our assessment**: This is the most concretely described agent workflow in the piece — a single conversational agent (or agent family) persisting across a multi-day, multi-touchpoint sales funnel rather than handling one isolated task. The design detail worth flagging for the guide is the agent's role as a *stateful funnel operator*: it does not just answer a question once, it re-engages the same customer at multiple later points (pre-visit, post-visit, post-purchase) with context carried forward from earlier turns. No detail is given on how state is carried across these touchpoints (a CRM record, a persistent conversation thread, a scheduled re-invocation) — that implementation detail is a gap the guide should not assume is filled in.

### Claim 3: For seller leads that previously dropped out of the funnel after 10 days with no further contact, AI agents now re-engage the customer, re-qualify intent, and return them to the funnel when Cars24 can meet their price — recovering 12% of previously lost leads
- **Evidence**: Narrator description of the seller-side re-engagement workflow, paired with the headline "12%" stat-box figure.
- **Confidence**: emerging (a specific, named before-state — "used to drop out after 10 days" — a named mechanism, and a quantified recovery rate; still self-reported with no disclosed baseline volume or measurement window)
- **Quote**: "For leads that used to drop out after 10 days, AI agents now re-engage customers, qualify renewed intent, and return them to the funnel when Cars24 can serve the price they are looking for." (workflow description); "12% — previously lost seller leads recovered through AI-powered re-engagement" (stat box)
- **Our assessment**: This is the single most concrete, checkable claim in the source: it names a specific prior failure mode (hard 10-day cutoff with no further contact) and a specific recovery mechanism (re-engage, re-qualify, match on price) tied to a quantified outcome (12%). It is a genuinely novel pattern for the corpus — a marketplace-side "lost lead resurrection" agent gated on a price/intent match, rather than a generic customer-support or sales-conversion agent. The percentage is unaudited vendor telemetry with no disclosed lead volume, so the guide should cite the mechanism (structured re-engagement after a defined drop-out point, conditioned on renewed intent and price fit) as the reusable pattern, and treat "12%" as illustrative rather than benchmarkable against other companies' recovery rates.

### Claim 4: Vikram Chopra (Builder, Cars24) frames the shift as moving from an experience that "depended on who picked up the phone" to one where AI gives "every customer a high-quality experience at any scale," citing over a million conversation-minutes handled by AI monthly
- **Evidence**: Direct named-executive quote.
- **Confidence**: anecdotal (single named individual's characterization; the "1M+ conversation minutes" figure is also the stat-box headline number, with no disclosed baseline or definition of what counts as a "conversation minute")
- **Quote**: "Buying a car in India is a journey, not a transaction. For years, the experience depended on who picked up the phone. AI changes that. Today, we handle over a million conversation minutes a month through AI, giving every customer a high-quality experience at any scale." —Vikram Chopra, Builder, Cars24
- **Our assessment**: The "depended on who picked up the phone" framing is a specific, quotable articulation of the consistency problem large conversation-driven service operations face (individual human performance variance), positioning AI agents as a consistency mechanism rather than purely a cost or speed mechanism. This is a distinct emphasis from the volume/speed framing common elsewhere in the corpus's customer-support case studies — worth noting as an alternative justification (uniformity of experience at scale) for agent deployment in high-touch service contexts.

### Claim 5: Cars24 embeds Codex directly into its software development lifecycle — product managers use it to create and refine Linear tickets, engineers tag it into bug reports for it to pick up, and it summarizes GitHub activity and posts team updates, reducing the number of standups needed
- **Evidence**: Direct narrator description in the "Embedding Codex into the software development lifecycle" section.
- **Confidence**: anecdotal (narrator description of workflow integration; no metric given for standup reduction, ticket volume, or bug-resolution rate)
- **Quote**: "Product managers use Codex to create and refine Linear tickets. Engineering teams tag Codex into bug reports so it can pick up defined tasks. Codex also summarizes work across GitHub and posts updates for teams, reducing the number of standups needed to keep work moving."
- **Our assessment**: The "tag Codex into a bug report so it can pick up defined tasks" pattern is a specific, checkable workflow-integration point — Codex participates directly in an existing bug-tracking mechanism (an @-mention or tag trigger) rather than being invoked through a separate interface. The "summarizes work across GitHub and posts updates... reducing standups" claim is notable as a distinct use case from code generation itself: an agent functioning as an automated status-reporting layer that substitutes for a synchronous meeting. No detail is given on what the summarization pipeline actually looks at (commits? PRs? both?) or how "reducing the number of standups" was measured (fewer meetings scheduled? shorter meetings? self-reported perception?).

### Claim 6: Cars24 reoriented its entire project-management workflow around Linear in a matter of weeks specifically to create a cleaner integration path for Codex
- **Evidence**: Direct narrator statement describing a deliberate tooling migration undertaken to support agent integration.
- **Confidence**: anecdotal (narrator claim; no detail on what tool(s) were replaced, migration mechanics, or headcount/team scope affected)
- **Quote**: "Cars24 reoriented its project management workflows around Linear in a matter of weeks, creating a cleaner path for Codex to support day-to-day work."
- **Our assessment**: This is a notable "adopt the agent-compatible tool, not just the agent" pattern — Cars24 changed its underlying project-management system (implicitly, from something else to Linear) as a prerequisite step for agent integration, rather than building a custom integration against whatever PM tool was already in place. This is a different adoption mechanism than the "living docs" or "agent speedruns" patterns documented in `blog-cursor-coinbase-agent-first-adoption.md` — it is a *tooling-standardization* move (pick the PM tool the agent ecosystem already integrates with cleanly) rather than a process-redesign or training move. The "in a matter of weeks" timeframe is asserted but not detailed (no description of what the migration itself required).

### Claim 7: Jayesh Gupta (Builder—AI & Innovation, Cars24) says Codex's spread beyond engineering — into product management, finance teams, and day-to-day workflows — changed his view from "Codex makes engineers faster" to "we changed how the entire company thinks about getting work done"
- **Evidence**: Direct named-executive quote.
- **Confidence**: anecdotal (single named individual's retrospective characterization; no data attached beyond the aggregate ~600-employee/85-90%-DAU figure elsewhere in the piece)
- **Quote**: "I thought Codex would make our engineers faster. What surprised me was how quickly it spread beyond engineering. Product managers, finance teams, and even day-to-day workflows started changing. That is when I realised we had not just changed how we write code but had changed how the entire company thinks about getting work done." —Jayesh Gupta, Builder—AI & Innovation, Cars24
- **Our assessment**: This is the case study's clearest first-person articulation of a coding-agent-turned-general-productivity-tool trajectory happening organically at a single company, distinct from OpenAI's own aggregate telemetry claim of the same trend (`blog-openai-codex-knowledge-work.md` Claim 2: knowledge workers are ~20% of Codex users and growing 3x faster than developers). Gupta's account is a named-practitioner, single-company instance of that broader vendor-reported pattern — it corroborates the direction but adds no independent measurement of its own.

### Claim 8: Cars24 finance teams use Codex to pull numbers from systems of record, run analysis, and prepare investor-reporting workflows without manually chasing inputs from multiple business heads
- **Evidence**: Narrator description of a named finance/investor-relations use case, in the "Extending agentic workflows to every team" section.
- **Confidence**: anecdotal (narrator description; no metric for time saved or reporting-cycle reduction)
- **Quote**: "In finance and investor relations, for instance, Cars24 teams use Codex to pull numbers from their systems of record, run analysis, and prepare investor reporting workflows without manually chasing inputs from multiple business heads."
- **Our assessment**: A specific, plausible non-engineering use case — an agent acting as a cross-system data-aggregation and drafting layer for a recurring, multi-stakeholder reporting process (investor reporting), where the described pain point (manually chasing inputs from multiple business heads) is a coordination/retrieval problem rather than an analysis problem per se. This is a concrete illustration of Codex used for what the OpenAI knowledge-work report calls "search" and "coordination" frictions (`blog-openai-codex-knowledge-work.md` Claim 7) in a finance-specific context not previously documented in the corpus.

### Claim 9: A separate finance workflow uses Codex to review purchase requests and purchase orders above a defined threshold — checking for anomalies, flagging concerns, and auto-approving requests where no issues are found
- **Evidence**: Narrator description of a named finance-approval automation workflow.
- **Confidence**: anecdotal (narrator description of an automated approval mechanism; no disclosure of the threshold value, anomaly-detection method, auto-approval rate, or any audit/override safeguard)
- **Quote**: "Another finance workflow uses Codex to review purchase requests and purchase orders above a defined threshold. The automation checks for anomalies, flags concerns, and auto-approves requests where no issues are found."
- **Our assessment**: This is the source's most operationally significant and least-scrutinized claim: an agent autonomously approving financial transactions above a threshold, not merely drafting or recommending. No detail is given on what happens when the agent is wrong (false-negative anomaly detection resulting in an improper auto-approval), what threshold triggers agent review versus fully manual review, or whether any human spot-checks approved-but-unreviewed transactions. The guide should flag this as a real-world instance of an agent operating with standing write/approval authority over financial workflows — a meaningfully higher-stakes autonomy pattern than the ticket-drafting or report-summarization claims elsewhere in this source — while noting that the case study gives no operational safeguards or failure-mode detail for it.

### Claim 10: Cars24 employees have built informal "chief of staff" agents connecting Slack, Gmail, WhatsApp, and other systems to manage communication, scheduling, hiring workflows, and follow-ups, illustrating a broader shift toward employees building their own tools rather than waiting for centralized engineering support
- **Evidence**: Narrator description in the "Extending agentic workflows to every team" section.
- **Confidence**: anecdotal (narrator claim describing an emergent, bottom-up pattern; no count of how many such agents exist, which teams built them, or any outcome measure)
- **Quote**: "Some teams have built \"chief of staff\" agents that connect Slack, Gmail, WhatsApp, and other systems to manage communication, scheduling, hiring workflows, and follow-ups."
- **Our assessment**: This is a distinct pattern from the finance and engineering workflows described elsewhere in the source — a personal-assistant-style, multi-system-integrated agent built by non-engineering employees themselves ("chief of staff"), rather than a centrally-built and -deployed tool. The framing sentence immediately preceding this quote ("employees are increasingly building the tools they need instead of waiting for centralized engineering support") makes explicit that this is presented as evidence of democratized, bottom-up tool-building rather than top-down IT deployment — a notable adoption-model claim, though entirely unquantified (no number of teams, agents, or employees involved is given).

### Claim 11: Cars24 has deployed ChatGPT Enterprise and Codex to about 600 employees across its central organization (engineering, finance, legal, marketing, operations), with 85% to 90% daily active usage
- **Evidence**: Direct narrator statement with specific headcount and usage-rate figures, in the "Building an AI-first operating model" closing section.
- **Confidence**: emerging (a specific, named headcount and a specific, named daily-active-usage percentage range; still self-reported with no definition of what "daily active usage" counts as — any tool interaction in a day? a specific feature used?)
- **Quote**: "Internally, Cars24 has deployed ChatGPT Enterprise and Codex to about 600 employees across its central organization, with 85% to 90% daily active usage."
- **Our assessment**: An 85-90% daily-active-usage rate among a ~600-employee deployed population is an unusually high sustained-engagement figure to cite without qualification — for comparison, the corpus's other OpenAI enterprise deployment case studies describe adoption by eligibility rule or total headcount (BBVA: 3,000 → ~100,000 employees; Samsung: all Korea + all global DX-division employees) but do not generally report a *daily* active-usage percentage this high for a comparable population size. The guide should treat this figure with the same self-reported-vendor-telemetry caveat applied elsewhere (no methodology, no time window, no distinction between light touch-and-go use and substantive daily work), but it is specific enough to be worth flagging as a notably strong internal-adoption figure if corroborated elsewhere.

## Concrete Artifacts

### Case study metadata and headline stat box (verbatim)

```
Source: https://openai.com/index/cars24 (July 16, 2026)

Company size: Enterprise
Region:       Asia-Pacific & Oceania
Industry:     Technology
Products:     API, ChatGPT, Codex

Results at a glance:
  1M+   monthly conversation minutes handled by AI agents
  50%   increase in customer support resolution rates
  80%   reduction in turnaround time across key service workflows
  12%   previously lost seller leads recovered through AI-powered re-engagement
```

### Named-practitioner quotes, verbatim, in order of appearance

```
Source: https://openai.com/index/cars24 (July 16, 2026)

1. Vikram Chopra, Builder, Cars24:
   "Buying a car in India is a journey, not a transaction. For years, the
   experience depended on who picked up the phone. AI changes that. Today,
   we handle over a million conversation minutes a month through AI, giving
   every customer a high-quality experience at any scale."

2. Jayesh Gupta, Builder—AI & Innovation, Cars24:
   "I thought Codex would make our engineers faster. What surprised me was
   how quickly it spread beyond engineering. Product managers, finance
   teams, and even day-to-day workflows started changing. That is when I
   realised we had not just changed how we write code but had changed how
   the entire company thinks about getting work done."
```

### Section headings (verbatim, in order)

```
Source: https://openai.com/index/cars24 (July 16, 2026)

1. Scaling a complex, conversation-driven marketplace
2. Automating the full customer journey with AI agents
3. Embedding Codex into the software development lifecycle
4. Extending agentic workflows to every team
5. Building an AI-first operating model
```

## Cross-References

- **Corroborates**:
  - `blog-openai-codex-knowledge-work.md` Claim 2 (knowledge workers now ~20% of Codex's user base, adopting it more than 3x faster than developers). Claim 7 in this note (Jayesh Gupta's account of Codex spreading unexpectedly from engineering into product, finance, and general workflows) is a named-practitioner, single-company illustration of that aggregate, self-reported OpenAI usage trend — a second data point (after `blog-openai-notion-codex-case-study.md`'s Claim 9, Notion engineers moving to parallel-task usage) of a named customer's account matching OpenAI's own telemetry-based narrative.
  - `blog-openai-codex-knowledge-work.md` Claim 7 (OpenAI's "three frictions" framing — search, coordination, approval/verification). This note's Claim 8 (Codex pulling numbers from systems of record and preparing investor-reporting workflows "without manually chasing inputs from multiple business heads") is a concrete, named-customer instance of the "coordination" friction that report describes abstractly.
  - `blog-openai-bbva-banking-transformation.md` and `blog-openai-samsung-chatgpt-codex-deployment.md` (both OpenAI-authored enterprise deployment case studies spanning multiple non-engineering functions). This note's Claim 11 (ChatGPT Enterprise + Codex to ~600 employees across engineering, finance, legal, marketing, operations) follows the same "central organization, cross-functional rollout" template as BBVA and Samsung, adding a specific daily-active-usage figure (85-90%) that neither of those two sources reports for a comparable population.

- **Contradicts**: None identified. No existing corpus source makes a claim about conversation-agent marketplace workflows, Codex-in-SDLC integration, or Cars24 specifically that this source disagrees with.

- **Extends**:
  - `blog-cursor-coinbase-agent-first-adoption.md` (Superbuilders role, living docs, agent speedruns as named organizational adoption mechanisms). This note's Claim 6 (Cars24 reoriented its entire PM tooling around Linear "in a matter of weeks" specifically to give Codex a cleaner integration path) adds a distinct adoption mechanism to that corpus's repertoire of named change-management tactics: *tooling standardization for agent compatibility*, rather than a process redesign (Coinbase's sprint-planning changes) or a training ritual (Coinbase's speedruns, BBVA's champions/wizards network).
  - `blog-openai-codex-knowledge-work.md` (Claim 8/9/10/11 customer vignettes — GroundVue, Proaction, a university professor, a personal accessibility-tool builder). This note's Claim 10 ("chief of staff" agents built by non-engineering Cars24 employees connecting Slack, Gmail, WhatsApp) is a structurally similar "employee builds their own tool without waiting for centralized engineering" vignette, but at a single named enterprise rather than independent small businesses/individuals, and for an internal productivity tool rather than a customer-facing or personal product.

- **Novel**:
  - **A quantified "lost lead resurrection" agent pattern gated on a defined drop-out point and a renewed-intent/price-match condition** (Claim 3: leads that "used to drop out after 10 days" are re-engaged and returned to the funnel "when Cars24 can serve the price they are looking for," recovering 12% of previously lost leads). No existing corpus source documents an agent workflow keyed to reviving specifically time-expired sales leads with a price-fit gating condition.
  - **An agent with standing auto-approval authority over financial purchase orders above a threshold** (Claim 9) — the corpus's other finance-automation examples (e.g., BBVA's credit-risk-analysis GPT) are described as analysis/recommendation tools reviewed by a human; this is the first source describing an agent that auto-approves transactions outright when no anomaly is flagged, with zero disclosed safeguard detail.
  - **Deliberate PM-tool standardization (migrating to Linear) specifically to enable clean agent integration** (Claim 6) as a distinct adoption-mechanism category from process redesign or training.
  - **A stateful, multi-touchpoint conversational agent persisting across a days/weeks-long transaction funnel** (Claim 2) rather than a single-session support or sales chatbot — the specific mechanism (re-invocation at pre-visit, post-visit, and post-purchase stages with carried-forward context) is more granular than the general "conversational AI handles customer support" pattern already common in the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add Claim 6 (Linear migration as a prerequisite for clean Codex integration) as a named example of tooling standardization as an adoption mechanism, alongside Coinbase's process-redesign and training-ritual mechanisms already cited from `blog-cursor-coinbase-agent-first-adoption.md`. Add Claim 11 (~600 employees, 85-90% daily active usage) as a specific internal-adoption figure to cite alongside BBVA's and Samsung's cross-functional deployment scale, with the same self-reported-telemetry caveat.
- **Chapter 03/04 (whichever covers agent autonomy and operational risk)**: Flag Claim 9 (Codex auto-approving purchase orders above a threshold with no disclosed safeguard) as a concrete, real-world example of an agent granted standing write/approval authority over a financial workflow — worth citing as a case where the guide should push readers to ask "what happens when the anomaly check is wrong?" since the source itself gives no answer.
- **Chapter 01 (Daily Workflows) or wherever the guide discusses non-engineering agent adoption**: Add Claim 10 ("chief of staff" agents connecting Slack, Gmail, WhatsApp, built by non-engineering employees) and Claim 8 (finance/investor-relations reporting workflow) as concrete, named-company illustrations of employee-built agentic tooling outside the engineering org, corroborating the "Codex for everyone" trend already documented from OpenAI's own telemetry in `blog-openai-codex-knowledge-work.md`.
- **Any chapter discussing conversational/customer-facing agent design**: Cite Claim 2 (stateful, multi-touchpoint funnel agent) and Claim 3 (time-gated lead re-engagement with a price-fit condition) as concrete workflow patterns for long-horizon, multi-session conversational agents in transaction-heavy marketplace contexts — a use case not previously represented in the corpus's mostly single-session customer-support or coding-agent case studies.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/cars24`) returned HTTP 403 to both the WebFetch tool and a direct `curl` with a browser user-agent — a Cloudflare challenge page, consistent with the OpenAI-domain bot-blocking behavior already documented in `blog-openai-notion-codex-case-study.md`, `blog-openai-samsung-chatgpt-codex-deployment.md`, and `blog-openai-codex-knowledge-work.md`'s Extraction Notes. The `WebFetch` tool additionally refused to fetch `web.archive.org` URLs directly in this environment (same restriction documented in those prior notes). The article was retrieved via a Wayback Machine snapshot (`http://web.archive.org/web/20260717113022/https://openai.com/index/cars24/`, crawled July 17, 2026, one day after publication), fetched with `curl` and parsed by stripping `<script>`/`<style>` blocks and all remaining HTML tags with a local Python script, rather than through an AI-summarization pass, specifically to guarantee the `Quote` fields above are copied character-for-character rather than paraphrased, per MINER.md §2a.
- The source is short (~650 words, as the Prospector's triage comment anticipated) with no linked sub-pages containing further substantive content about Cars24; the page's "Keep reading" footer links to three unrelated OpenAI posts (a teen AI-safety piece, a US AI-safety-policy piece, and a GPT-Red robustness research post), none of which concern Cars24 and were not followed.
- This is a single-source, two-named-practitioner, vendor-published case study. Every quantitative figure in it (1M+ conversation minutes, 50% support-resolution increase, 80% turnaround reduction, 12% lead recovery, ~600 employees, 85-90% daily active usage) is self-reported by OpenAI/Cars24 with no disclosed methodology, baseline, or measurement window — `confidence_overall` is set to anecdotal (rather than emerging) because, unlike BBVA's or Coinbase's case studies which pair headline figures with detailed named mechanisms and multiple named executives, several of this source's most load-bearing figures (the 50% and 80% stats in particular) are never explained or tied to a specific workflow anywhere in the body text — they appear only in the stat box with no supporting narrative, which is a thinner evidentiary link between metric and mechanism than other case studies in the corpus provide.
- No contradictions identified during extraction; nothing in this source disagrees with an existing corpus note (see Cross-References), so no contradiction issue was filed per MINER.md §4a.
