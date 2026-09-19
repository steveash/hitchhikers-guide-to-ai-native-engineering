---
source_url: https://openai.com/index/gpt-6-astra-next-generation-work
source_type: blog-post
title: "GPT‑6 Astra: The next generation in intelligence for work"
author: OpenAI (unsigned corporate voice)
date_published: 2026-09-09
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: emerging
issue: "#3561"
---

# GPT‑6 Astra: The next generation in intelligence for work

> OpenAI's own product-positioning post for GPT‑6 Astra in work contexts,
> published six days after launch: it frames Astra's core pitch as
> "no-prep" integration into existing, non-API-having applications, backs
> that with six enterprise customer testimonials (Cognition, Databricks,
> Hebbia, Box, Figma, Thomson Reuters Labs) and four coding/agentic
> testimonials (Datacurve, Basis, CodeRabbit, XTX Markets), restates the
> $10/$50-per-million-token pricing already documented elsewhere in this
> corpus, discloses a new quantified safety figure (89% fewer unintended
> outcomes than GPT‑5.6 Sol, 74.7% fewer than Claude Fable 5.1 on an
> internal "computer use safety benchmark"), and announces new enterprise
> admin controls and four named ChatGPT Desktop enterprise plugins (Oracle
> Analytics, Power BI, Navan, Avalara).

## Source Context

- **Type**: blog-post (official `openai.com/index/` product-announcement
  page, published September 9, 2026, unsigned/institutional byline
  "OpenAI"). Structured as four named sections ("The world's best model
  for complex work," "More useful work for every dollar," "More safety and
  control for consequential work," "Start using Astra today") with two
  embedded customer-testimonial carousels (six enterprise testimonials,
  four coding/agentic testimonials) and one video reference. Roughly
  1,000-1,100 words of body prose excluding testimonial carousels.
- **Author credibility**: First-party institutional statement from OpenAI
  about its own already-shipped, generally-available model, published six
  days after the September 3, 2026 launch (`blog-simonwillison-gpt6-astra-launch.md`,
  `blog-openai-astra-safety-overview.md`). As with every other first-party
  OpenAI post in this corpus, all comparative and quantified claims are
  self-measured and self-graded; the customer testimonials are OpenAI's own
  selection of quotes from named individuals at named companies, not an
  independent survey. Unlike the September 3 safety overview
  (`blog-openai-astra-safety-overview.md`), which foregrounded an unfavorable
  finding (decreased CoT monitorability) alongside favorable ones, this post
  is unambiguously promotional in framing — every customer quote and every
  headline metric in this post is favorable to Astra; no comparable
  self-critical disclosure appears here.
- **Scope**: Covers Astra's "no-prep" workflow-integration pitch, six
  enterprise-customer testimonials, an internal OpenAI dogfooding anecdote
  (video production, a Codex latency bug fix), pricing and cost-efficiency
  framing, four coding/agentic-customer testimonials, a new quantified
  computer-use safety-benchmark comparison against GPT‑5.6 Sol and Claude
  Fable 5.1, new enterprise admin controls, four named ChatGPT Desktop
  enterprise plugins, a restated Critical cybersecurity threshold
  disclosure, Zero Data Retention availability, and enterprise
  rollout/access mechanics. Does **not** cover: any benchmark methodology
  detail for OfficeQA Pro/Pro V2, DeepSWE v1.1, or the "computer use safety
  benchmark" (no named evaluation set, task count, or scoring rubric is
  given for any of these — only the headline percentages); Terminal Bench
  4.0 or Artificial Analysis Intelligence Index scores (named but not
  quantified in this post, unlike `blog-simonwillison-gpt6-astra-launch.md`,
  which gives Artificial Analysis Intelligence Index numbers directly); any
  detail on the CoT-monitorability regression already disclosed in
  `blog-openai-astra-safety-overview.md`; or a system-card-level citation
  for the "computer use safety benchmark" figures (this post presents them
  as a standalone paragraph, with no link to a supporting system-card
  sub-page in the archived version retrieved for this note).

## Extracted Claims

### Claim 1: GPT‑6 Astra, described as "the world's most intelligent and aligned model," is now available in ChatGPT Work, Codex, and the API, and is state-of-the-art on computer use, browsing, professional work, software engineering, cybersecurity, and science
- **Evidence**: Opening sentence of the post, framing the entire piece.
- **Confidence**: settled (a direct, first-party availability and positioning statement for an already-shipped model)
- **Quote**: "Last week we introduced GPT‑6 Astra, the world’s most intelligent and aligned model, now available in ChatGPT Work, Codex, and the API. Astra is state-of-the-art on computer use, browsing, professional work, software engineering, cybersecurity, and science, so teams can take on the most demanding professional work with unmatched speed, accuracy, and judgment."
- **Our assessment**: The "state-of-the-art" claim spans six distinct capability areas in one sentence with no supporting citation attached to any of them in this post specifically — the cybersecurity claim is separately substantiated by the Critical-threshold disclosure (Claim 9 below) and by `blog-simonwillison-gpt6-astra-launch.md` Claim 8's ExploitBench/ExploitGym/SRE-Bench figures, but the other five areas (computer use, browsing, professional work, software engineering, science) rest on this post's own testimonials and the benchmark names in Claims 4 and 6 rather than on independently reproduced scores. Treat as OpenAI's positioning framing, not as six independently verified capability claims.

### Claim 2: Astra's core differentiator, per OpenAI's own framing, is that it does not require businesses to prepare data, redesign workflows, or build custom integrations before delivering value — it can write code and operate through the same applications people already use, including ones with no API, letting businesses use it within existing workflows "from day one"
- **Evidence**: Second paragraph of the post's first named section, "The world's best model for complex work."
- **Confidence**: settled (a direct, specific positioning claim, though the "no extensive preparation" framing is itself an OpenAI marketing characterization, not an independently measured integration-time reduction)
- **Quote**: "Most AI systems require businesses to prepare their data, redesign workflows, and build custom integrations before they can deliver value. Astra changes that. In ChatGPT Work and Codex, it can write code and work through the same applications people use every day—even when those applications don’t have an API. That means businesses can put AI to work within their existing workflows from day one, without extensive preparation or engineering work."
- **Our assessment**: This is the post's central thesis and the reason its title emphasizes "work" specifically — it is a computer-use/agentic-interoperability claim (operating through applications lacking an API) rather than a raw-intelligence claim. It directly extends the Computer Use and browser-based application access already announced for ChatGPT Work in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 12 (Computer Use "operate[s] the user's computer in the background — clicking, typing, and moving files across apps, tools, and the browser"), now reframed as Astra's specific, named contribution to that existing product surface rather than a new capability being introduced for the first time.

### Claim 3: Within the first few days of rollout, OpenAI states customers were already using Astra for GPU optimization, spotting discrepancies in financial statements, and producing more on-brand presentation decks
- **Evidence**: Third paragraph of the "world's best model" section, a brief, unattributed usage-pattern summary preceding the named testimonials.
- **Confidence**: anecdotal (unattributed, unquantified — no customer name, task count, or outcome metric attached to any of the three named use cases)
- **Quote**: "Within the first few days of rollout, we’re already seeing customers put Astra to work, from optimizing GPUs to spotting discrepancies in financial statements to producing more on-brand decks."
- **Our assessment**: This sentence is a summary preview of the named testimonials that follow (GPU optimization maps to no specific named testimonial in this post; financial-statement discrepancy-spotting maps loosely to Hebbia's Claim 5 testimonial; on-brand decks maps directly to both Hebbia's and the post's later "better at following a company's voice, templates, and design standards" claim, Claim 8 below) rather than three independent data points — treat as scene-setting, not as three additional customer examples beyond the six named testimonials in Claim 4.

### Claim 4: Six named enterprise customers gave positive testimonials about GPT‑6 Astra: Cognition (Devin harness integration, computer use/writing/codebase understanding), Databricks (OfficeQA Pro/Pro V2 state-of-the-art, better cost per task than GPT‑5.6 Sol), Hebbia (best decks tested, 17% more faithful to brief, 19% more accurate document sourcing), Box (>10% less likely to make confidently incorrect assertions), Figma (design-vision understanding), and Thomson Reuters Labs (writing quality and intent-understanding for legal work)
- **Evidence**: Six separate testimonial quotes in a carousel, each attributed to a named individual, title, and company.
- **Confidence**: anecdotal (named, attributed customer quotes — stronger than an unattributed marketing claim, but OpenAI's own selection of favorable quotes, not an independent or randomly-sampled customer survey)
- **Quote**: "We’re integrating GPT‑6 Astra into Devin’s harness on launch day, where it delivers state-of-the-art performance on our internal testing benchmark. Its excellent computer use, writing, and codebase understanding improved testing right out of the box: videos are noticeably easier to follow, and reports are clearer and more concise" — Silas Alberti, SVP Research, Cognition
- **Our assessment**: The Databricks quote (Ivan Zhou) is the most technically specific of the six: "GPT‑6 Astra claims the new state of the art on our OfficeQA Pro & Pro V2 benchmarks, using our Genie harness. It also offers significantly better cost per task than GPT‑5.6 Sol." Both "OfficeQA Pro/Pro V2" and "Genie harness" are named here for the first time in this corpus, with no score attached — a candidate for a future Miner pass on Databricks' own benchmark documentation if it exists as a separate source. The Hebbia quote (George Sivulka) gives the sharpest quantified figures of the six: "followed the brief 17% more faithfully than the next-best model, while sourcing its claims to the right document 19% more often." The Box quote (Yashodha Bhavnani) is notable for framing "judgement" specifically as *declining to assert* unsupported conclusions (">10% less likely to make confidently incorrect assertions") — a calibration/hallucination-avoidance claim distinct from the other five testimonials' raw-capability framing.

### Claim 5: OpenAI itself rolled out Astra internally weeks before public launch; its developer/marketing teams used Astra and Codex to convert three hours of multicamera footage into a promotional video that garnered over 550,000 views in four days, and its engineering team used Astra to find and fix a memory-allocation bottleneck causing slow Codex sessions in a test environment, achieving 25x lower turn latency at roughly 30% higher peak memory use by switching allocators
- **Evidence**: Fourth paragraph of the "world's best model" section, an internal-dogfooding anecdote with two named use cases and specific quantified outcomes for the second.
- **Confidence**: emerging (a specific, quantified internal case study — 25x latency reduction, 30% memory increase, 550k views in 4 days — but self-reported with no external verification of either figure, and no detail on what "switching allocators" specifically involved)
- **Quote**: "At OpenAI, Astra was rolled out internally weeks before launch, so we saw first hand how bleeding-edge capabilities like computer use could change the way we work. Our developer and marketing teams used Astra and Codex to turn three hours of multicamera footage into our GPT‑6 Astra Developer First Impressions video … which has already garnered over 550k views in just 4 days. Our engineering team used Astra to uncover and resolve a memory-allocation bottleneck that was causing slow Codex sessions in a test environment. By switching allocators, they were able to produce 25× lower turn latency with roughly 30% higher peak memory use." (the ellipsis marks a screen-reader-only "(opens in a new window)" link label the source inserts between "video" and "which," omitted per MINER.md §2a.3)
- **Our assessment**: The 25x-latency-for-30%-more-memory tradeoff is a concrete, checkable-in-principle engineering result (a classic latency/memory tradeoff from an allocator change) — notable both as a specific technical claim and as evidence that OpenAI is using Astra/Codex on its own infrastructure debugging, not just customer-facing content generation. This is a distinct internal-dogfooding data point not previously documented in this corpus's Astra coverage; it complements rather than duplicates the internal cross-team adoption figures (sales discovery-to-PoC compressed from weeks to 24 hours, finance month-end close from days to hours) already recorded in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 for the earlier, GPT‑5.6-powered ChatGPT Work.

### Claim 6: Astra is also better than its predecessors at following a company's voice, templates, and design standards, producing first results closer to something a team can use directly
- **Evidence**: Closing sentence of the "world's best model" section, following the internal-dogfooding anecdote and preceding a "Gaia presentation/Spreadsheet/Document styling" visual example (not independently reproducible from this note's text-only extraction).
- **Confidence**: anecdotal (an unquantified, comparative style/template-adherence claim, with no named benchmark or scoring)
- **Quote**: "Astra is also better at following a company’s voice, templates, and design standards, so the first result is closer to something a team can put to use."
- **Our assessment**: This directly echoes and specifically extends the original ChatGPT Work launch post's framing that GPT‑5.6 is "state of the art at reasoning through multi-step tasks and creating materials that follow your templates and reference files" (`blog-openai-chatgpt-work-ambitious-partner.md` Claim 3) — this post asserts the successor model (Astra) improves specifically on that same template/style-adherence dimension, though neither post gives a scoring methodology for the claim.

### Claim 7: Astra was trained to complete tasks in fewer tokens with fewer retries, meaning less rework and lower cost per task; OpenAI claims it occupies "the majority of the cost-efficiency frontier" on professional-work and coding evaluations including Terminal Bench 4.0 and the Artificial Analysis Intelligence Index; API pricing starts at $10 per million input tokens and $50 per million output tokens
- **Evidence**: Full paragraph of the "More useful work for every dollar" section.
- **Confidence**: emerging for the cost-efficiency-frontier claim (named benchmarks, but no score, percentile, or chart given in this post itself); settled for the pricing figure (a specific, checkable, previously-corroborated number)
- **Quote**: "Astra continues our commitment to providing extremely efficient models that deliver more useful work per dollar to our customers. It's been trained to complete tasks in fewer tokens with fewer retries, which means less rework and lower cost per task. With Astra, OpenAI occupies the majority of the cost-efficiency frontier on professional work and coding evaluations, including Terminal Bench 4.0 and Artificial Analysis Intelligence Index. Pricing starts at $10 per million input tokens and $50 per million output tokens."
- **Our assessment**: The $10/$50 pricing figure corroborates `blog-simonwillison-gpt6-astra-launch.md` Claim 3 and `blog-simonwillison-astra-pelican-comparison-grid.md` Claim 3 (first-person-confirmed) exactly — this post is now a third, first-party-sourced confirmation of that price point. The "majority of the cost-efficiency frontier" framing is vaguer than the Artificial Analysis Intelligence Index score (61, tied with Sol, trailing both Fable 5.1 and Muse Spark 1.3) already documented in `blog-simonwillison-gpt6-astra-launch.md` Claim 4 — this post cites the same named index but gives no score, so it should not be read as contradicting that lower relative standing; "cost-efficiency frontier" is a cost-vs-capability framing (matching Claim 5's "less than half the cost of Claude Fable 5, for the same score" from the launch post), not a claim about topping the raw intelligence index itself.

### Claim 8: Four named coding/agentic customers gave testimonials: Datacurve (new DeepSWE v1.1 record at 74%, fewer steps and greater token efficiency on long-horizon tasks), Basis (proactive-agent pass rate on 5+ hour end-to-end workflows improved 20%, with fewer inference calls and less scaffolding needed), CodeRabbit (~20% more bugs caught overall, more than double the catch rate on cross-file pull requests requiring extensive reasoning), and XTX Markets (general commentary on accelerating AI mathematical-research capability)
- **Evidence**: Four separate testimonial quotes in a second carousel, each attributed to a named individual, title, and company.
- **Confidence**: anecdotal for the XTX Markets quote (general commentary, no figure); emerging for the other three (specific, quantified, named-benchmark or named-metric claims, but self-reported customer testimonials, not independently audited)
- **Quote**: "Astra sets a new record on DeepSWE v1.1 at 74%. It did so with fewer steps and greater token efficiency than has ever been achieved by frontier models, especially on complex, long horizon tasks. Certainly, this model will have a noticeable impact on high quality, real-world software engineering." — Serena Ge, Co-Founder & CEO, Datacurve
- **Our assessment**: The CodeRabbit quote (David Loker) is the most operationally specific of the four: "Compared with our baseline, Astra caught ~20% more bugs. On pull requests that require extensive cross-file reasoning to detect subtle issues, it more than doubled the catch rate. In code review, it connects a change's intent to its consequences: it reasons across files to catch interface-contract drift and authorization bugs the baseline missed, and it backs findings with concrete verification steps." This is a concrete, mechanism-level claim (cross-file reasoning connecting change intent to consequence) rather than a bare percentage, and is the first corpus mention of "interface-contract drift" as a named class of bug a coding agent is claimed to catch. The Basis quote's "remove scaffolding and accelerate performance" framing is notable as a claim that improved model decision-making reduces the amount of harness-side scaffolding needed — relevant to any guide discussion of the harness-vs-model-capability tradeoff already explored elsewhere in this corpus (e.g. `blog-ronacher-the-coming-loop.md`).

### Claim 9: On OpenAI's internal "computer use safety benchmark" — testing models against hard business scenarios like exposing confidential information, sharing a dashboard too broadly, or deleting data — Astra produced unintended outcomes 89% less often than GPT‑5.6 Sol and 74.7% less often than Claude Fable 5.1
- **Evidence**: First two sentences of the "More safety and control for consequential work" section, a single named-but-undescribed internal benchmark with two comparative percentage figures.
- **Confidence**: emerging (a specific, quantified, named-benchmark comparative claim against two competitor models, but self-reported with no described task count, methodology, or scoring rubric, and no third-party audit)
- **Quote**: "During training, we tested Astra on our internal computer use safety benchmark which tests models against the hardest business scenarios such as exposing confidential information, sharing a dashboard too broadly, or deleting data. In this evaluation, Astra produced unintended outcomes 89% less often than GPT‑5.6 Sol and 74.7% less often than Claude Fable 5.1. Additional confirmation and automated review further improved performance for GPT‑6 Astra and GPT‑5.6 Sol."
- **Our assessment**: This is the first corpus source to name a "computer use safety benchmark" or give any cross-vendor (OpenAI vs. Anthropic) comparative figure for unintended/unsafe agentic-action rates specifically. It is a materially different kind of claim from the Critical cybersecurity threshold disclosure (Claim 10 below): that disclosure is about offensive capability (can the model find and exploit vulnerabilities), while this benchmark is about defensive/accidental-harm avoidance (does the model itself take unintended harmful actions during ordinary business use of computer-use/agentic features) — a guide citing one should not imply it substantiates the other. No benchmark name, task count, or scoring methodology is given, and the "89%"/"74.7%" figures have no stated denominator (percent of what base rate, over how many trials) — this should be flagged clearly as a headline vendor figure pending independent reproduction.

### Claim 10: New enterprise admin controls let organizations restrict Astra to approved websites and desktop applications, manage uploads and downloads, and control browsing history; ChatGPT Work and Codex include confirmation policies requiring approval before consequential actions and automated review of potentially unsafe or unauthorized tool calls, letting teams start with a limited configuration and expand access over time
- **Evidence**: Second paragraph of the "More safety and control for consequential work" section.
- **Confidence**: settled (a direct, specific, itemized list of first-party product/admin controls tied to a named product surface)
- **Quote**: "Organizations can also decide how broadly to deploy Astra. New enterprise admin controls let them restrict access to approved websites and desktop applications, manage uploads and downloads, and control browsing history. ChatGPT Work and Codex also include safeguards such as confirmation policies, which can require approval before consequential actions, and automated review of potentially unsafe or unauthorized tool calls. These controls allow teams to start with a limited configuration and expand access over time."
- **Our assessment**: This extends the enterprise-admin control surface already documented in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13 (a Compliance API for visibility into ChatGPT Work conversations/actions, and an "Auto-review" feature reviewing important connected-tool actions before they happen). The new elements here — approved-website/desktop-application allowlisting, upload/download management, and browsing-history control — are website/desktop-scoped controls not named in that July post, consistent with Astra's expanded computer-use/browsing emphasis (Claim 1). "Confirmation policies" requiring approval before consequential actions appears functionally similar to that earlier post's "Auto-review," though this post does not explicitly state whether it is the same feature renamed or a distinct, additional one.

### Claim 11: Alongside Astra, OpenAI is launching new enterprise plugins in ChatGPT Desktop — from Oracle Analytics, Power BI (described as "a Microsoft Fabric service"), Navan, and Avalara — powered by "the latest browser use capabilities," to make familiar enterprise applications easier to access
- **Evidence**: Third paragraph of the "More safety and control for consequential work" section.
- **Confidence**: settled (a direct, specific, named-vendor product announcement)
- **Quote**: "To further access, alongside Astra, we’re also launching new enterprise plugins in ChatGPT Desktop. Powered by the latest browser use capabilities, plugins from Oracle Analytics, Power BI (a Microsoft Fabric service), Navan, and Avalara make it easier to access familiar enterprise applications."
- **Our assessment**: This is the first corpus mention of ChatGPT Desktop "enterprise plugins" as a distinct product category, and the first naming of Oracle Analytics, Navan, or Avalara as OpenAI enterprise integration partners. Notably, OpenAI describes these plugins as "powered by the latest browser use capabilities" — i.e., framed as an application of Astra's computer-use/browsing strength (Claim 1, Claim 2) rather than as traditional API-based connectors, consistent with the post's central "works through applications without an API" thesis.

### Claim 12: GPT‑6 Astra is confirmed as the first OpenAI model to reach the Critical cybersecurity capability threshold under the Preparedness Framework; OpenAI states it has strengthened protections against both misuse and the model taking unauthorized actions, including training Astra to respect safety/security boundaries, improving resistance to safeguard-bypass attempts, and deploying automated checks to block harmful responses; Zero Data Retention is available for eligible API customers on supported endpoints, subject to approval
- **Evidence**: Fourth paragraph of the "More safety and control for consequential work" section plus a standalone closing sentence.
- **Confidence**: settled (a direct restatement of an already-confirmed capability-tier classification, plus a specific, checkable product-availability statement)
- **Quote**: "Astra … is also the first model to reach the Critical cybersecurity capability threshold under our Preparedness Framework. With that increased capability, we’ve strengthened protections … against both misuse and the model taking unauthorized actions including training Astra to respect safety and security boundaries, improving its resistance to attempts to bypass safeguards, and deploying automated checks designed to block harmful responses." … "Zero Data Retention is available for eligible API customers on supported endpoints, subject to approval." (the first two ellipses each mark a screen-reader-only "(opens in a new window)" link label the source inserts — immediately after "Astra" and after "protections," respectively — omitted per MINER.md §2a.3; the final ellipsis joins two non-adjacent sentences from different paragraphs of the same post, per the same section)
- **Our assessment**: This restates, without new detail, the Critical-threshold confirmation already fully documented in `blog-openai-astra-safety-overview.md` Claim 1 (the Sept 3 launch-day safety post) — this Sept 9 "work" post adds no new figure, mechanism, or evaluation detail beyond that earlier disclosure, and should not be cited as an independent corroboration beyond confirming OpenAI continues to state the same classification six days later. The Zero Data Retention availability detail is new to this corpus's Astra coverage specifically, though ZDR itself is an existing OpenAI enterprise/API feature, not something introduced with Astra.

## Concrete Artifacts

```
Source: OpenAI, "GPT-6 Astra: The next generation in intelligence for
work," https://openai.com/index/gpt-6-astra-next-generation-work
(published September 9, 2026; retrieved via Internet Archive Wayback
Machine snapshot dated 2026-09-10 — see Extraction Notes)

Pricing (restated, matches prior corpus figures):
  Input:  $10 / million tokens
  Output: $50 / million tokens

Internal OpenAI dogfooding case study:
  - Developer/marketing teams: 3 hours of multicamera footage -> "GPT-6
    Astra Developer First Impressions" video, 550k+ views in 4 days
  - Engineering team: fixed a memory-allocation bottleneck causing slow
    Codex sessions in a test environment by switching allocators ->
    25x lower turn latency, ~30% higher peak memory use

Computer use safety benchmark (OpenAI internal, unnamed task set):
  Astra vs. GPT-5.6 Sol:        89% fewer unintended outcomes
  Astra vs. Claude Fable 5.1:   74.7% fewer unintended outcomes
  (scenario types named: exposing confidential information, sharing a
  dashboard too broadly, deleting data)

New enterprise admin controls (Astra-specific, additive to
`blog-openai-chatgpt-work-ambitious-partner.md` Claim 13's Compliance
API / Auto-review):
  - Restrict access to approved websites and desktop applications
  - Manage uploads and downloads
  - Control browsing history
  - Confirmation policies requiring approval before consequential actions
  - Automated review of potentially unsafe or unauthorized tool calls

New ChatGPT Desktop enterprise plugins (four named vendors):
  - Oracle Analytics
  - Power BI (described as "a Microsoft Fabric service")
  - Navan
  - Avalara

Six enterprise-workflow testimonials (company, named individual, title):
  - Cognition       — Silas Alberti, SVP Research
  - Databricks      — Ivan Zhou, Staff Research Engineer & Tech Lead Manager
  - Hebbia          — George Sivulka, Founder & CEO
  - Box             — Yashodha Bhavnani, VP of AI Products
  - Figma           — Loredana Crisan, Chief Design Officer
  - Thomson Reuters Labs — Omar Bari, VP Applied Research

Four coding/agentic testimonials (company, named individual, title):
  - Datacurve   — Serena Ge, Co-Founder & CEO (DeepSWE v1.1: 74%, new record)
  - Basis       — Mitch Troyanovsky, Co-founder (+20% pass rate, 5+ hour workflows)
  - CodeRabbit  — David Loker, VP of AI (~20% more bugs caught overall;
                  >2x catch rate on cross-file PRs)
  - XTX Markets — Alex Gerko, CEO (qualitative, no figure)

Named-but-unscored benchmarks in this post: Terminal Bench 4.0,
Artificial Analysis Intelligence Index, OfficeQA Pro & Pro V2 (Databricks'
own "Genie harness"), DeepSWE v1.1.
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-gpt6-astra-launch.md`, `blog-openai-astra-safety-overview.md`,
`blog-openai-astra-critical-cyber-capabilities.md`,
`blog-simonwillison-astra-pelican-comparison-grid.md`,
`blog-ronacher-astra-why.md`, and `blog-openai-chatgpt-work-ambitious-partner.md`
were each re-read in full before writing this section, and every `Claim N`
cited below was located and confirmed by number and content against that
note's own text before use, per MINER.md §4b.

- **Corroborates**:
  - `blog-simonwillison-gpt6-astra-launch.md` Claim 3 and
    `blog-simonwillison-astra-pelican-comparison-grid.md` Claim 3 (both
    documenting $10/$50 per-million-token API pricing for Astra): this
    post's Claim 7 restates the identical figure as a third, first-party
    OpenAI source, now six days post-launch.
  - `blog-openai-astra-safety-overview.md` Claim 1 (Astra confirmed,
    unhedged, as OpenAI's first model to reach the Critical cybersecurity
    threshold): this post's Claim 12 restates the same confirmed
    classification without adding new detail.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 12 (Computer Use
    lets ChatGPT Work "operate the user's computer in the background —
    clicking, typing, and moving files across apps, tools, and the
    browser") and Claim 3 (GPT‑5.6 "creating materials that follow your
    templates and reference files"): this post's Claims 2 and 6 restate
    both capabilities as Astra-specific improvements to the same existing
    product surface, not new capabilities introduced for the first time.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  One point of framing tension is worth flagging rather than silently
  smoothing over: this post's Claim 7 states Astra "occupies the majority
  of the cost-efficiency frontier on professional work and coding
  evaluations, including... Artificial Analysis Intelligence Index," which,
  read in isolation, could suggest Astra leads that index outright. But
  `blog-simonwillison-gpt6-astra-launch.md` Claim 4 gives the actual score
  (61, tied with GPT‑5.6 Sol, five points behind Claude Fable 5.1, and
  behind Meta's Muse Spark 1.3) — Astra does *not* top the raw Intelligence
  Index. These are not contradictory: this post's claim is specifically
  about the *cost-efficiency frontier* (a cost-vs-capability framing,
  consistent with the launch post's Claim 5 "less than half the cost of
  Claude Fable 5, for the same [Coding Agent Index] score"), not about
  topping the raw index score. A guide passage citing this post's
  "cost-efficiency frontier" language must not imply Astra leads the
  Intelligence Index itself — it does not, per the launch post's own
  numbers. No contradiction issue filed (MINER.md §4a "When NOT to file":
  the two claims measure different things — cost-efficiency vs. raw
  score — not opposing claims about the same fact).

- **Extends**:
  - `blog-openai-chatgpt-work-ambitious-partner.md`: that July 9, 2026 post
    launched ChatGPT Work on GPT‑5.6 with four enterprise testimonials
    (Zapier, RingCentral, Virgin Atlantic, NVIDIA) and a Compliance
    API/Auto-review admin control set. This post is the direct successor
    announcement — same product (ChatGPT Work), new underlying model
    (Astra), six new enterprise testimonials, and an expanded admin-control
    surface (website/desktop allowlisting, upload/download management,
    browsing-history control) layered on top of the original Compliance
    API/Auto-review controls.
  - `blog-openai-astra-safety-overview.md` and
    `blog-openai-astra-critical-cyber-capabilities.md`: this post's Claim 9
    (the "computer use safety benchmark," 89%/74.7% fewer unintended
    outcomes than Sol/Fable 5.1) is the first corpus figure quantifying
    Astra's *defensive*/accidental-harm-avoidance performance during
    ordinary computer-use tasks, distinct from the *offensive*
    cyber-capability figures (ExploitBench, ExploitGym, SRE-Bench) already
    documented in `blog-simonwillison-gpt6-astra-launch.md` Claim 8 and the
    Critical-threshold classification in the two cited safety posts. All
    four sources concern Astra's safety profile but measure different
    things — a guide passage should not conflate offensive-capability
    figures with this post's defensive/unintended-action figures.
  - `blog-simonwillison-astra-pelican-comparison-grid.md` Claim 6 (Astra
    does not support a "none"/no-reasoning level, unlike Sol/Terra/Luna):
    this post's emphasis on Astra "trained to complete tasks in fewer
    tokens with fewer retries" (Claim 7) is a plausible, though not
    explicitly connected, complementary framing — Astra's token efficiency
    is claimed to come from training rather than from a low-reasoning
    mode it does not offer.

- **Contrasts** (not contradictions — flagged per MINER.md's "high value"
  guidance for tensions, no issue filed):
  - `blog-ronacher-astra-why.md` Claim 9 (a named practitioner's verdict
    that, even at a low failure rate, he does "not manage to trust this
    model much" for professional software engineering, given observed
    code-quality problems from a 35-hour unattended run) sits in direct
    tension with this post's uniformly favorable coding testimonials
    (Claim 8: Datacurve, Basis, CodeRabbit) and its "no-prep" workflow
    thesis (Claim 2). This is not a factual contradiction — the two
    sources describe different tasks under different conditions (Ronacher:
    a single, unbounded, 35-hour, fully unattended greenfield C/Python
    interpreter project; this post's testimonials: bounded coding-agent
    evaluations like DeepSWE v1.1 and cross-file PR review) — but a guide
    passage should present both: OpenAI's own vendor-selected customer
    testimonials are uniformly favorable, while at least one independent,
    named, hands-on practitioner report in this same corpus found
    committed-code quality and trustworthiness problems significant enough
    to withhold professional trust in Astra even at a stated low failure
    rate. No contradiction issue filed (MINER.md §4a "When NOT to file":
    conditioning-variable difference — bounded/evaluated tasks vs.
    unbounded/unattended real-world use — not opposing claims about the
    same fact).

- **Novel**:
  - First corpus source to name a "computer use safety benchmark" and to
    give a cross-vendor (OpenAI vs. Anthropic) comparative unintended-
    outcome-rate figure (Claim 9).
  - First corpus source to name "OfficeQA Pro & Pro V2" and Databricks'
    "Genie harness" (within the Databricks testimonial, Claim 4) and
    "DeepSWE v1.1" with a specific score (74%, within the Datacurve
    testimonial, Claim 8).
  - First corpus source to name ChatGPT Desktop "enterprise plugins" as a
    distinct product category and to name Oracle Analytics, Navan, and
    Avalara as OpenAI enterprise integration partners (Claim 11).
  - First corpus source to disclose OpenAI's own internal engineering use
    of Astra to diagnose and fix a Codex session-latency bug, with a
    specific 25x-latency/30%-memory tradeoff figure (Claim 5).
  - First corpus source to name "interface-contract drift" as a class of
    bug a coding agent is claimed to catch (within the CodeRabbit
    testimonial, Claim 8).

## Guide Impact

- **Chapter 02/03 (Model Selection — Cost Economics)**: This post adds a
  third first-party confirmation of the $10/$50 pricing (Claim 7) — no new
  guide action needed beyond what `blog-simonwillison-gpt6-astra-launch.md`
  and `blog-simonwillison-astra-pelican-comparison-grid.md` already
  recommend, except to note that OpenAI's own "cost-efficiency frontier"
  framing (Claim 7) must be presented alongside the actual Intelligence
  Index score (61, tied with Sol, trailing Fable 5.1 and Muse Spark 1.3)
  from the launch post, so a guide passage does not imply Astra leads that
  index outright — see Cross-References → Contradicts.

- **Chapter on Security & Threat Model**: Add Claim 9's "computer use
  safety benchmark" figures (89% fewer unintended outcomes vs. Sol, 74.7%
  fewer vs. Claude Fable 5.1) as a new, distinct data point from Astra's
  offensive-capability figures already in the guide's coverage — explicitly
  label it as measuring accidental/unintended-harm avoidance during
  ordinary agentic computer-use tasks, not offensive cyber capability, and
  flag it as a self-reported, unaudited vendor figure with no disclosed
  methodology or task count.

- **Chapter on Harness Engineering / Enterprise Deployment**: Add Claim 10's
  new admin controls (approved-website/desktop-application allowlisting,
  upload/download management, browsing-history control, confirmation
  policies, automated tool-call review) and Claim 11's four named ChatGPT
  Desktop enterprise plugins (Oracle Analytics, Power BI, Navan, Avalara)
  as concrete examples of the access-control surface available to
  organizations deploying computer-use-capable agents — pair with
  `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13's Compliance
  API/Auto-review as the fuller admin-control picture across both posts.

- **Do not cite this post's coding/agentic testimonials (Claim 8) as
  representative of typical real-world outcomes without also citing
  `blog-ronacher-astra-why.md`'s independent, hands-on practitioner
  report**: per the Contrasts entry above, this post's testimonials are
  OpenAI's own selection of favorable, bounded-task customer quotes: a
  guide section on Astra's coding reliability should present both the
  vendor testimonials here and the independent 35-hour unattended-run
  findings together, not the favorable testimonials alone.

## Extraction Notes

- **Fetch method**: The live URL returned HTTP 403 with a Cloudflare bot
  challenge (`cf-mitigated: challenge`), consistent with the access pattern
  already documented for other `openai.com/index/` posts in this corpus.
  An Internet Archive Wayback Machine snapshot was located via the
  `archive.org/wayback/available` API
  (`web.archive.org/web/20260910185345/https://openai.com/index/gpt-6-astra-next-generation-work/`)
  and fetched directly with `curl` (HTTP 200). The raw HTML was isolated to
  its `<main>` tag, stripped of scripts/styles/comments, and linearized to
  plain text locally with a small Python script (headings/paragraphs/list
  items converted to newlines, tags stripped, HTML entities unescaped). All
  `Quote` fields in this note were copied character-for-character from that
  linearized text (including its curly apostrophes, en-dash hyphenation in
  "GPT‑6," and the multiplication sign in "25×"), with invisible
  screen-reader/word-joiner artifacts (`⁠` characters preceding
  "(opens in a new window)" labels) omitted as non-content formatting
  noise, per MINER.md §2a.3 — consistent with how
  `blog-openai-astra-critical-cyber-capabilities.md`'s Extraction Notes
  document the same footer-link-label artifact for this same `openai.com`
  page template.
- **Testimonial carousel parsing**: the two testimonial carousels (six
  enterprise quotes, four coding/agentic quotes) render in the linearized
  text as a single run-on paragraph per carousel, with each quote delimited
  by curly quotation marks and each attribution following an em dash. These
  were parsed with a regex isolating each `"quote" — Name, Title, Company`
  unit rather than read as continuous prose; every quote and attribution
  pairing was checked against the raw HTML's visual carousel-slide
  structure (company logo list immediately following each carousel,
  matching quote order) before being assigned in this note.
- **No sub-pages followed**: the post's only outbound content link is to
  the "GPT‑6 Astra Developer First Impressions" video (referenced, not
  embedded transcript) cited in Claim 5; this was not independently
  fetched, since the post's own prose gives the specific, checkable claims
  (three hours of footage, 550k+ views in 4 days) this note extracts. No
  benchmark-methodology sub-pages (for OfficeQA Pro/Pro V2, DeepSWE v1.1,
  or the computer use safety benchmark) are linked from this post itself,
  unlike the safety-overview post's linked system-card sub-pages
  (`blog-openai-astra-safety-overview.md` Extraction Notes) — this post is
  a self-contained single page with no deeper source to follow for its
  benchmark names.
- **Overall confidence rated `emerging`**: the post contains several
  settled, checkable first-party statements (pricing, the Critical-threshold
  restatement, the admin-control and plugin lists), but its central
  evidentiary content — six enterprise testimonials, four coding
  testimonials, the "cost-efficiency frontier" framing, and the "computer
  use safety benchmark" figures — is either unaudited vendor-selected
  customer quotation or a self-reported comparative benchmark with no
  disclosed methodology. This is consistent with this post's promotional
  framing (see Source Context) rather than a technical or safety-disclosure
  register.
- **One contrast flagged, no contradiction issue filed**: see
  Cross-References → Contrasts. This post's uniformly favorable coding
  testimonials sit in tension with `blog-ronacher-astra-why.md`'s
  independent negative practitioner verdict, but the two describe
  different task conditions (bounded evaluations vs. unbounded unattended
  use), so this was judged a conditioning-variable case per MINER.md §4a
  "When NOT to file," not a genuine contradiction. No contradiction issue
  was filed.
- **Single Prospector triage comment set used**: three duplicate triage
  comments were posted to the source issue (all 2026-09-19, within seconds
  of each other), recommending overlapping chapter targets (Ch02/Ch03;
  Ch02/Ch03; Ch02/Ch03/Ch04/Ch07). This note's Guide Impact section targets
  Model Selection/Cost Economics, Security & Threat Model, and Harness
  Engineering/Enterprise Deployment as the strongest, most specific matches
  across all three comments' overlapping intent.
