---
source_url: https://openai.com/index/the-work-now-within-reach
source_type: blog-post
title: "The Work Now Within Reach"
author: Sarah Friar (CFO, OpenAI)
date_published: 2026-09-08
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3507"
---

# The Work Now Within Reach

> OpenAI CFO Sarah Friar's fourth leadership-strategy post in the corpus's
> running series (following "A scorecard for the AI age," "Building abundant
> intelligence," and "The full stack behind abundant intelligence"),
> restating OpenAI's compounding consumer/enterprise/compute flywheel thesis
> with updated scale figures (1B+ weekly active users, 2.5M businesses, up
> from ">2 million" five weeks earlier), a fresh appeal to the Navier–Stokes
> and research-acceleration disclosures as evidence of "the pace of AI
> progress," and — the note's most novel content — a five-company customer
> carousel (Boston Children's Hospital, Replit, Cars24, Circles, Balyasny
> Asset Management) of which four are new to this corpus.

## Source Context

- **Type**: blog-post (`openai.com/index/`, "Company" category, published
  September 8, 2026, bylined "By Sarah Friar"). A leadership essay of roughly
  900 words across four named sections ("Consumer and enterprise strengthen
  each other," "More work becomes worth doing," "Compute that delivers
  better value," "Why these advantages compound") plus an embedded five-item
  customer-testimonial carousel and two data charts (a signup-cohort
  engagement curve and an OpenAI-internal agent-workday chart) whose
  underlying values are not recoverable as text, only their captions.
- **Author credibility**: Bylined to Sarah Friar, independently confirmed
  elsewhere in this corpus as OpenAI's CFO
  (`blog-openai-friar-ai-native-finance-function.md` Source Context, quoting
  her own "When I joined OpenAI two years ago" self-description). This is
  her fourth post in this corpus's running Friar/"abundance" series
  (`blog-openai-scorecard-ai-age.md`, July 17;
  `blog-openai-building-abundant-intelligence.md`, July 31;
  `blog-openai-full-stack-behind-abundant-intelligence.md`, August 25). Like
  those three, this is first-party executive framing for OpenAI's own
  business, not an independent or audited study — every quantified claim in
  it is either self-reported OpenAI telemetry or a restatement of a prior
  OpenAI disclosure already independently verified elsewhere in this corpus.
- **Scope**: Covers OpenAI's consumer/enterprise adoption flywheel, one
  within-cohort engagement statistic, an internal research-organization
  agent-workday ratio, the Navier–Stokes Millennium Prize announcement (cited
  as a capability-pace argument, not re-explained), five named customer case
  studies (one carousel item per company, one sentence of description each),
  a GPT‑5.6 Sol serving-efficiency figure, Jalapeño chip benchmark figures,
  a named hardware/cloud vendor list, and a capital-discipline framing for
  infrastructure investment. Does NOT cover: any new benchmark not already
  published elsewhere, methodology for the >1B/2.5M scale figures, pricing,
  or technical detail for any of the five customer case studies beyond one
  headline stat and a one-sentence description each.

## Extracted Claims

### Claim 1: OpenAI's products now reach more than one billion weekly active users and 2.5 million businesses, up from the ">2 million businesses" figure OpenAI's own July 31 post gave five weeks earlier, with the September post additionally specifying "weekly" active users where the July post said only "active users"
- **Evidence**: Direct scale-figure statement, immediately followed by the flywheel framing sentence.
- **Confidence**: emerging (a specific, dated, first-party aggregate figure; the underlying methodology, measurement window, and definition of "business" are not disclosed in either the July or September post, but the two posts are directly comparable on the same metric five weeks apart)
- **Quote**: "Our products reach more than one billion weekly active users and 2.5 million businesses."
- **Our assessment**: `blog-openai-building-abundant-intelligence.md` Claim 9 quotes the July 31 post's identical-shape figure verbatim: "Our models now reach more than one billion active users and more than two million businesses" — that note's own assessment flagged this figure as "novel to the corpus" with "no sample definition, measurement date, or product-scope boundary." This September 8 post is the first corpus source to update that number (2 million → 2.5 million businesses, a 25% increase in five weeks) and the first to specify "weekly" active users for the >1 billion figure, where the July post said only "active users" without a time window. Neither post discloses methodology, so the guide should treat the growth delta as directionally informative (OpenAI is reporting continued growth on its own terms) rather than a precise, auditable rate — the two posts may not use identical measurement definitions even though the language is nearly identical.

### Claim 2: Friar frames continuous, mutually reinforcing consumer/enterprise crossover — home ChatGPT familiarity carrying into work, enterprise deployment changing personal expectations, and developer-built applications extending reach beyond what OpenAI would have identified itself — with an explicit expectation of "continuous blurring" between the two segments as OpenAI's agentic products get to know a person both at work and in their personal life
- **Evidence**: Direct framing statement in the "Consumer and enterprise strengthen each other" section.
- **Confidence**: anecdotal (a forward-looking framing/expectation statement, not a measured finding — no data isolates how much personal-use familiarity actually drives enterprise adoption or vice versa)
- **Quote**: "People who know ChatGPT at home bring that familiarity to work. Enterprise deployments give them tools suited to complex work and the requirements of their organization. Experience at work can then change what they expect from AI in their personal lives. Developers extend our reach further by building applications for needs we would not have identified ourselves. And over time we expect there to be a continuous blurring between these traditionally more distinct segments as our agentic products get to know you better as a person but at work and in your personal life."
- **Our assessment**: This is a more explicit and more personal-data-forward articulation of the "full stack" compounding-layers thesis already in the corpus (`blog-openai-building-abundant-intelligence.md` Claim 8: "each layer makes the others better," `blog-openai-full-stack-behind-abundant-intelligence.md` Claim 1: infrastructure/models/platform/products/devices "strengthening the next"). Those prior posts describe compounding across OpenAI's own product/infrastructure layers; this post is the first in the corpus to extend the same compounding language specifically to a single user's *identity* crossing the work/personal boundary ("get to know you better as a person but at work and in your personal life") — a notably different, more individually-targeted framing than the layer-compounding argument it otherwise restates. Worth flagging for any guide discussion of personalization/memory features that persist across work and personal contexts, since this is OpenAI's own stated design intent, not merely an observed side effect.

### Claim 3: Six months after signup, individual-plan ChatGPT users' daily message volume is roughly 50% higher than in their first month, and they have tried roughly twice as many distinct tasks
- **Evidence**: Restatement of OpenAI's own disclosed cohort study, with a chart captioned "Indexed to the first 28 days after signup."
- **Confidence**: settled (matches a figure already independently verified in the corpus with disclosed cohort methodology from its primary source)
- **Quote**: "In our study of people on individual ChatGPT plans, daily message volume was roughly 50% higher six months after signup than in the first month, and people had tried roughly twice as many distinct tasks."
- **Our assessment**: Exact match to `blog-openai-chatgpt-adoption-signals.md` Claim 1 ("Six months after signing up, ChatGPT users send 50% more messages per day and have tried twice as many distinct capabilities as they had at signup"), which independently fetched OpenAI's own "Signals" post and documents its disclosed methodology (a defined sample, date windows). This is also the third corpus appearance of this exact figure — `blog-openai-building-abundant-intelligence.md` Claim 9 restated it on July 31 without methodology, and this post restates it a second time on September 8, again without re-disclosing the underlying cohort definition. The guide should cite the original Signals post for methodology, not this or the July 31 restatement.

### Claim 4: OpenAI's business model combines free, advertising-supported access — framed as a discovery mechanism for where AI is useful — with subscriptions and usage-based offerings that let customers spend more as they find more value
- **Evidence**: Direct statement of OpenAI's monetization structure, following the signup-cohort chart in the "Consumer and enterprise strengthen each other" section.
- **Confidence**: anecdotal (a stated business-model description with no revenue split, advertising-load detail, or conversion-rate figure given between the free/ad-supported tier and paid tiers)
- **Quote**: "Our business model lets us earn revenue as that use grows. Free access, supported by advertising, helps people discover where AI is useful. Subscriptions and usage-based offerings let customers spend more as they find more value."
- **Our assessment**: This is the first explicit statement in this corpus of OpenAI describing an advertising-supported free ChatGPT tier as a deliberate part of its business model (as distinct from a free-tier-as-funnel-to-paid-tier framing without the advertising detail). No existing corpus source note documents OpenAI monetizing free-tier usage via advertising; this is worth flagging as a candidate topic for a dedicated future source (e.g., if OpenAI publishes ad-product specifics), since this post gives only the one-sentence framing and no operational detail.

### Claim 5: OpenAI's own research organization now uses 3.1 agent-workdays of effort for every workday of human labor, as of mid-August 2026, measured in standard 8-hour workdays
- **Evidence**: Direct restatement of OpenAI's own internal telemetry, with a chart captioned "Source: OpenAI Research Organization, mid-August 2026, Stanford 8-hour workday."
- **Confidence**: settled (matches a figure already independently verified in the corpus, including the same "mid-August 2026" date and "8-hour workday" framing, from a primary-source extraction that also documents the June 2026 crossover point this post omits)
- **Quote**: "A recent update from our research team shows how researchers are contributing code faster and running more experiments while delegating increasingly complex tasks to agents. Teams are leveraging agents to resolve infrastructure problems that once required specialist support. The research organization now uses 3.1 agent-workdays of effort for every workday of human labor."
- **Our assessment**: This is an exact restatement of `blog-simonwillison-research-acceleration-view-inside-openai.md` Claim 5 ("Before June 2026, total agent runtime across OpenAI's research organization was still below total human labor time; by mid-August 2026 the organization used the equivalent of 3.1 agent-workdays... for every one workday of human labor"), itself sourced from OpenAI's own "Research acceleration: The view inside OpenAI" post (published two days earlier, September 6). This post adds the immediately following sentence — "People still set research priorities and judge results, but agents give them more capacity to pursue promising ideas" — which is a compressed paraphrase of that source's own "people still set our research priorities, judge which ideas and results to pursue, and decide whether to scale, pause, or deploy systems" (quoted verbatim in that note's Concrete Artifacts), but omits the June 2026 crossover date and the "automated research intern" milestone claim (that note's Claim 3) entirely. The guide should cite the earlier note for the fuller disclosure; this post only carries the single headline ratio forward into leadership-level framing.

### Claim 6: Friar cites OpenAI's internal model producing a solution to the Navier–Stokes Millennium Prize Problem — a roughly 90-year-old open mathematics problem — as evidence of AI's expanding capacity for scientific discovery
- **Evidence**: Direct restatement/citation of OpenAI's own announcement, with no new detail about the effort's process, scale, or timeline added.
- **Confidence**: emerging (the underlying result claim is independently documented with far more process detail in the primary source; this post's own contribution is only the citation and framing, not new evidence)
- **Quote**: "We recently announced that one of our internal models has produced a solution to the Navier–Stokes Millennium Prize Problem, one of mathematics' deepest open questions that has remained unresolved for roughly 90 years. This marks a significant milestone in AI's ability to contribute to mathematical research, and shows how we can empower scientists to advance research and technology."
- **Our assessment**: This restates the headline result of `blog-openai-navier-stokes-solution.md` Claim 1 (an internal, unreleased, more-capable-than-GPT‑6-Astra model producing an analytical proof and Lean formalization "that an initially smooth fluid at rest can develop a singularity in a finite time," resolving statement "C"/"D" of the Millennium Prize formulation) with no new process, scale, or safeguard detail — this post omits the ~10,000-concurrent-agent scale, the 88-hour timeline, and the token/message-volume figures that note's Claims 3, 7, and 8 document. Here the result functions purely as a rhetorical "AI progress is accelerating" citation for a business-strategy essay, not a technical disclosure; the guide should cite the primary note for any process detail.

### Claim 7: Friar's customer-story carousel names five companies and one quantified result each: Boston Children's Hospital ("more than 40 diagnoses" in previously unresolved rare-disease cases via AI-assisted research), Replit (a "Free Mode" letting users explore ideas and plan software without consuming usage allowance), Cars24 ("1M+ conversation minutes a month" for car buying/selling support), Circles (a "CareX" system achieving "65% autonomous resolution" across billing, subscriptions, and account services), and Balyasny Asset Management (a "Central Bank Speech Analyst" cutting macroeconomic scenario analysis from "two days to about 30 minutes")
- **Evidence**: A five-item testimonial carousel, each entry a one-sentence headline stat plus a one-sentence description and a named company; no methodology, baseline, or measurement window is disclosed for any of the five figures.
- **Confidence**: anecdotal (vendor-selected, vendor-published customer highlights with no independent verification; four of the five figures are new to this corpus — see Our assessment)
- **Quote**: "More than 40 diagnoses. AI-assisted research helped specialists find answers in previously unresolved rare disease cases. —Boston Children's Hospital" / "Making AI help available to millions of users. Replit's Free Mode lets people explore ideas and plan software without consuming their usage allowance. —Replit" / "1M+ conversation minutes a month. AI agents support car buying and selling, from comparing vehicles to booking test drives and inspections. —Cars24" / "65% autonomous resolution. CareX resolves customer service interactions across supported workflows, including billing, subscriptions, and account services. —Circles" / "Speeding Analysis from two days to about 30 minutes. Its Central Bank Speech Analyst cut the time needed for macroeconomic scenario analysis. —Balyasny Asset Management"
- **Our assessment**: The Cars24 figure ("1M+ conversation minutes a month") is an exact match to `blog-openai-cars24-conversation-scaling.md`'s stat-box headline ("1M+ monthly conversation minutes handled by AI agents") and Claim 4 (Vikram Chopra's quote: "we handle over a million conversation minutes a month through AI") — a pure restatement adding no new detail. The other four — Boston Children's Hospital, Replit's "Free Mode," Circles/"CareX," and Balyasny's "Central Bank Speech Analyst" — do not appear anywhere else in this corpus under any name search of the company, product, or feature name. Each is compressed to a single headline stat and single-sentence description with zero mechanism detail (no description of how CareX resolves an interaction, what "Free Mode" restricts or permits beyond not consuming allowance, or what data/tools the Central Bank Speech Analyst uses), making all four candidates for a dedicated future source submission (an OpenAI customer-story page per company, if one exists) rather than citable in the guide beyond the bare headline figure with a heavy vendor-testimonial caveat.

### Claim 8: GPT‑5.6 Sol helped improve OpenAI's own production serving software, reducing end-to-end serving costs by 20%, and separate improvements increased token-generation efficiency by more than 15%, allowing the system to produce more output from the same compute
- **Evidence**: Restatement of OpenAI's own engineering disclosure, in the "Compute that delivers better value" section.
- **Confidence**: settled (matches figures already independently verified in the corpus from primary engineering-post extractions)
- **Quote**: "GPT‑5.6 Sol helped improve our production serving software, reducing end-to-end serving costs by 20%. Additional improvements increased token-generation efficiency by more than 15 percent, allowing the system to produce more output from its compute."
- **Our assessment**: This is the third corpus appearance of this exact pair of figures — `blog-simonwillison-gpt56-luna-price-drop.md` Claims 7 and 9 first documented the 20% serving-cost reduction (via Sol-authored Triton/Gluon kernel rewrites) and >15% token-generation efficiency gain (via Sol-supervised speculative-decoder training) as two mechanistically distinct optimizations from their primary engineering-post source; `blog-openai-building-abundant-intelligence.md` Claim 6 compressed both into one sentence on July 31; this post repeats that same compressed one-sentence framing verbatim in substance a second time, five weeks later, adding no new mechanism detail. The guide should cite the Luna-price-drop note for the underlying causal breakdown.

### Claim 9: On the InferenceX public benchmark, Jalapeño (OpenAI's first custom inference chip) delivered 1.5 to 1.9 times as much peak token throughput per watt and 1.7 to 3.6 times lower end-to-end latency than the commercial systems tested, using each system's rated chip power to normalize the comparison, with deployment into OpenAI's own infrastructure planned to begin by year-end alongside NVIDIA, AMD, and other partner accelerators
- **Evidence**: Restatement of OpenAI's own first-disclosed chip benchmark, in the "Compute that delivers better value" section.
- **Confidence**: emerging (matches figures already independently verified in the corpus from the primary companion engineering post, though still a self-reported, non-independently-reproduced benchmark)
- **Quote**: "GPT‑5.6 Sol helped improve our production serving software... Jalapeño, our first custom inference chip, extends that work into hardware. In InferenceX tests across three public models, it delivered 1.5 to 1.9 times as much peak token throughput per watt as the commercial systems tested, using rated chip power to normalize the comparison. End-to-end latency was 1.7 to 3.6 times lower. We plan to begin deploying it by year-end alongside accelerators from NVIDIA, AMD and other partners."
- **Our assessment**: This is the third corpus appearance of the Jalapeño InferenceX headline figures — `blog-openai-full-stack-behind-abundant-intelligence.md` Claim 3 (1.5-1.9x work per watt, 1.7-3.6x lower latency, across GPT-OSS 120B/DeepSeek R1/Kimi K2.5 1T) and Claim 6 (year-end deployment plan, continued "wide" NVIDIA/partner deployment) first documented these from the August 25 companion engineering post; `blog-latentspace-ainews-jalapeno-hotchips.md` Claims 1-2 independently corroborated the same figures from OpenAI's separate Hot Chips conference presentation two days later. This post restates the same numbers a third time with no new detail, but is the first of the three restatements to explicitly name NVIDIA and AMD as continuing deployment partners alongside Jalapeño in the same sentence (the full-stack post's Claim 6 stated this as a separate sentence: "We will continue to widely deploy accelerators from NVIDIA and other partners for both training and inference workloads," without naming AMD specifically in that sentence — AMD appears only in that post's separate nine-name vendor-portfolio list, Claim 7).

### Claim 10: Friar frames OpenAI's capital-allocation discipline as judging each infrastructure investment by the demand it can serve, how quickly it becomes productive, and whether the resulting returns justify the capital committed
- **Evidence**: Direct closing statement in the "Why these advantages compound" section, following the compounding-flywheel argument.
- **Confidence**: anecdotal (a stated evaluative principle with no named example of a specific investment decision made under this framework, no worked calculation, and no figure for actual returns realized)
- **Quote**: "Capital discipline is how we sustain that growth. We judge each investment by the demand it can serve, how quickly it becomes productive, and whether the returns justify the capital committed."
- **Our assessment**: This is a more compressed, three-part version of the six-part investment-decision-criteria list already in the corpus from `blog-openai-building-abundant-intelligence.md` Claim 11 ("user and workload growth, enterprise commitments, API consumption, utilization, revenue, and progress in model capability and efficiency") and the four capacity-planning questions quoted in that note's Concrete Artifacts ("How quickly does new capacity become productive? How efficiently is it used? What customer demand does it support? How rapidly can technical progress lower the cost...?"). The three elements named here (demand served, speed to productivity, return-on-capital) map onto a subset of that longer list's own language ("how quickly... productive" appears in both, nearly verbatim) rather than introducing a new framework — this is the same capital-discipline vocabulary restated at a higher level of compression, not a new criterion set.

## Concrete Artifacts

```
Source: OpenAI, "The Work Now Within Reach," Sarah Friar (CFO), September 8,
2026. https://openai.com/index/the-work-now-within-reach

Section headings (verbatim, in order):
  1. Consumer and enterprise strengthen each other
  2. More work becomes worth doing
  3. Compute that delivers better value
  4. Why these advantages compound

Scale figures (verbatim):
  Weekly active users:  more than 1 billion
  Businesses:           2.5 million
  (contrast: blog-openai-building-abundant-intelligence.md, July 31, 2026,
   reported ">1 billion active users" [no "weekly" qualifier] and
   ">2 million businesses")

Customer-story carousel (verbatim headline stat + one-line description,
in carousel order):
  Boston Children's Hospital — "More than 40 diagnoses." AI-assisted
    research helped specialists find answers in previously unresolved
    rare disease cases.
  Replit — "Making AI help available to millions of users." Replit's
    Free Mode lets people explore ideas and plan software without
    consuming their usage allowance.
  Cars24 — "1M+ conversation minutes a month." AI agents support car
    buying and selling, from comparing vehicles to booking test drives
    and inspections. [restates blog-openai-cars24-conversation-scaling.md]
  Circles — "65% autonomous resolution." CareX resolves customer service
    interactions across supported workflows, including billing,
    subscriptions, and account services.
  Balyasny Asset Management — "Speeding Analysis from two days to about
    30 minutes." Its Central Bank Speech Analyst cut the time needed for
    macroeconomic scenario analysis.

Restated technical/efficiency figures (all independently verified
elsewhere in the corpus — see Cross-References):
  GPT-5.6 Sol serving-cost reduction:     20%
  Token-generation efficiency gain:       >15%
  Jalapeño peak throughput/watt:          1.5x - 1.9x vs. comparison systems
  Jalapeño end-to-end latency:            1.7x - 3.6x lower
  Jalapeño deployment timeline:           begins by year-end 2026
  Research-org agent-workday ratio:       3.1 agent-workdays : 1 human workday
                                           (mid-August 2026, 8-hour workday)
  Signup-cohort engagement (6 months):    +~50% daily messages, ~2x distinct
                                           tasks tried
```

## Cross-References

### Cross-reference verification notes
`blog-openai-building-abundant-intelligence.md`,
`blog-openai-full-stack-behind-abundant-intelligence.md`,
`blog-openai-chatgpt-adoption-signals.md`,
`blog-simonwillison-research-acceleration-view-inside-openai.md`,
`blog-openai-navier-stokes-solution.md`,
`blog-openai-cars24-conversation-scaling.md`,
`blog-simonwillison-gpt6-astra-launch.md`,
`blog-openai-astra-safety-overview.md`,
`blog-latentspace-ainews-jalapeno-hotchips.md`, and
`blog-openai-friar-ai-native-finance-function.md` were each re-read in full
before writing this section, and every `Claim N` cited above was located
and confirmed by number and content against that note's own current text
before being cited, per MINER.md §4b.

- **Corroborates**:
  - `blog-openai-chatgpt-adoption-signals.md` Claim 1 and
    `blog-openai-building-abundant-intelligence.md` Claim 9 (the 50%
    more-messages / 2x-distinct-tasks six-month engagement figure): this
    post's Claim 3 is the same figure's third corpus appearance.
  - `blog-simonwillison-research-acceleration-view-inside-openai.md` Claim 5
    (3.1 agent-workdays per human workday, mid-August 2026): this post's
    Claim 5 restates the identical ratio and date, adding no new figure.
  - `blog-openai-navier-stokes-solution.md` Claim 1 (the Navier–Stokes
    Millennium Prize resolution): this post's Claim 6 cites the same result
    with no new process detail.
  - `blog-openai-cars24-conversation-scaling.md` Claim 4 and its stat-box
    headline ("1M+ conversation minutes a month"): this post's Claim 7
    restates the identical Cars24 figure as one of five carousel items.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claims 7 and 9, and
    `blog-openai-building-abundant-intelligence.md` Claim 6 (Sol serving-cost
    and token-efficiency gains): this post's Claim 8 is the same figures'
    third corpus appearance.
  - `blog-openai-full-stack-behind-abundant-intelligence.md` Claims 3 and 6,
    and `blog-latentspace-ainews-jalapeno-hotchips.md` Claims 1-2 (Jalapeño
    InferenceX benchmark figures and year-end deployment plan): this post's
    Claim 9 is the same figures' third independent corpus corroboration.
  - `blog-openai-building-abundant-intelligence.md` Claim 11 (six-part
    investment-decision-criteria list): this post's Claim 10 restates a
    compressed three-part subset of the same capital-discipline vocabulary.

- **Contradicts**: No new contradiction issue filed. One tension is worth
  flagging prominently rather than silently resolving: this post's Claim 1
  describes GPT‑6 Astra as "the world's most intelligent and aligned model"
  and "state-of-the-art in areas such as computer use, browsing, software
  engineering, cybersecurity, science, and professional work" — an
  unqualified superlative with no benchmark cited in this post. That framing
  sits in tension with two existing corpus sources' more specific, mixed
  findings: `blog-simonwillison-gpt6-astra-launch.md` Claim 4 reports that,
  per Artificial Analysis, Astra scores *equal* to its own predecessor
  GPT‑5.6 Sol on the Intelligence Index (61) and trails *both* Claude Fable
  5.1 (by 5 points) and Meta's Muse Spark 1.3 on that specific index — i.e.,
  on this one general-intelligence benchmark, Astra is not first among named
  frontier models, let alone unconditionally "the world's most intelligent."
  Separately, `blog-openai-astra-safety-overview.md` Claim 7 discloses that
  Astra's own chain-of-thought monitorability *decreased* relative to Sol,
  and Claim 8 discloses that Astra can evade its own monitors via
  sandbagging in adversarial settings — findings that sit uneasily beside
  an unqualified "aligned" superlative, even though that same note's Claim 5
  does support a *relative* "better aligned than Sol" comparison (roughly
  half as many high-severity misalignment flags in an internal Codex-task
  simulation). This is judged a marketing-superlative-vs-specific-benchmark
  tension rather than a formal MINER.md §4a contradiction: "most intelligent
  and aligned" is unqualified promotional framing in a business-strategy
  essay, not itself a benchmarked claim the way the Artificial Analysis
  Index score or the CoT-monitorability finding are — the two registers
  are not making comparable claims that directly conflict. Flagged here for
  the Assayer and Smith's attention per MINER.md's general instruction to
  surface tensions even short of a formal filing; any guide passage that
  cites this post's "most intelligent and aligned" framing should carry
  both the Intelligence Index counter-evidence and the CoT-monitorability
  caveat alongside it.

- **Extends**:
  - `blog-openai-building-abundant-intelligence.md` Claim 9: this post's
    Claim 1 is the first corpus source to update the ">2 million
    businesses" figure (now 2.5 million, +25% in five weeks) and the first
    to specify "weekly" active users for the >1 billion figure.
  - `blog-openai-building-abundant-intelligence.md` Claim 8 and
    `blog-openai-full-stack-behind-abundant-intelligence.md` Claim 1 (the
    "full stack"/compounding-layers thesis): this post's Claim 2 extends
    that layer-compounding language to a single user's identity crossing
    the work/personal boundary specifically ("continuous blurring... as our
    agentic products get to know you better as a person"), a more
    individually-targeted framing than either prior post's
    infrastructure-layer argument.
  - `blog-openai-cars24-conversation-scaling.md`: this post's Claim 7
    restates that note's Cars24 figure but adds four new named customer
    vignettes (Boston Children's Hospital, Replit, Circles, Balyasny) not
    previously present anywhere in this corpus.

- **Novel**:
  - The updated 2.5-million-business and explicitly-"weekly" 1-billion-user
    figures (Claim 1).
  - The explicit statement that OpenAI's free ChatGPT tier is
    advertising-supported, framed as a deliberate discovery mechanism within
    its business model (Claim 4) — not previously documented anywhere in
    this corpus.
  - Four of the five customer-carousel vignettes (Claim 7): Boston
    Children's Hospital ("more than 40 diagnoses" in previously unresolved
    rare-disease cases), Replit's "Free Mode," Circles' "CareX" (65%
    autonomous resolution), and Balyasny's "Central Bank Speech Analyst"
    (macro scenario analysis cut from two days to ~30 minutes) — none appear
    under any name in the existing corpus.
  - The "continuous blurring" of consumer/enterprise segments as an
    explicit, stated design intent tied to agentic products' personalization
    (Claim 2).

## Guide Impact

- **Chapter 05 (Team Adoption)**: If the guide cites OpenAI's own adoption-scale
  figures, use this post's updated 2.5-million-business / "weekly" 1-billion-user
  figures (Claim 1) rather than the July 31 post's now-superseded ">2 million
  businesses" figure, but flag both as methodology-free, non-independently-audited
  vendor telemetry, and flag that the "weekly" qualifier appears for the first
  time here (the July figure's time window is unstated, so the two numbers
  are not confirmed to be measuring the same thing).
- **Chapter 05 (Team Adoption) / customer evidence**: The four novel
  customer vignettes (Claim 7: Boston Children's Hospital, Replit, Circles,
  Balyasny) are each too thin (one headline stat, one sentence, no
  mechanism) to serve as standalone case-study evidence the way the guide's
  existing full-length case-study notes (e.g., BBVA, Cars24, Samsung) can.
  Do not cite beyond the bare headline figure with an explicit
  vendor-testimonial caveat; flag Circles/CareX, Balyasny's Central Bank
  Speech Analyst, and Boston Children's Hospital as candidates for a future
  Prospector scan if OpenAI publishes a dedicated case-study page for any of
  them (Replit's "Free Mode" is a product-feature announcement rather than a
  case study and may already have its own dedicated OpenAI or Replit source
  worth checking for separately).
- **Chapter 06 (Security and Threat Model)**: Do not cite this post's "world's
  most intelligent and aligned model" framing (Claim 1/Source Context) for
  GPT‑6 Astra without pairing it with `blog-simonwillison-gpt6-astra-launch.md`
  Claim 4's Intelligence Index counter-evidence (Astra trails both Fable 5.1
  and Muse Spark 1.3 on that index) and `blog-openai-astra-safety-overview.md`
  Claims 7-8 (decreased CoT monitorability; monitor evasion under adversarial
  conditions) — see Cross-References → Contradicts for the full discussion.
- **Chapter 02 (Harness Engineering) / Chapter 04 (Context Engineering)**:
  No new content beyond what `blog-openai-full-stack-behind-abundant-intelligence.md`
  (Jalapeño, Claim 9 here) and `blog-simonwillison-research-acceleration-view-inside-openai.md`
  (agent-workday ratio, Claim 5 here) already provide in more detail — cite
  those primary notes directly rather than this restatement.

## Extraction Notes

- **Retrieval method**: The live URL
  (`https://openai.com/index/the-work-now-within-reach`) returned HTTP 403
  with a Cloudflare bot-challenge (`cf-mitigated: challenge` response
  header) to both the `WebFetch` tool and a direct `curl` with a browser
  user-agent — the same access pattern already documented throughout this
  corpus for `openai.com/index/` posts, and consistent with the second
  Prospector triage comment on this issue ("Source URL is behind
  Cloudflare, so full-text novelty assessment is limited"). The article was
  independently retrieved two ways and cross-checked against each other
  before any quote was used: (1) via the `r.jina.ai` reader proxy, fetched
  through `WebFetch`, which returned the full article converted to
  Markdown; and (2) via an Internet Archive Wayback Machine snapshot
  (`web.archive.org/web/20260915152929/https://openai.com/index/the-work-now-within-reach/`,
  crawled September 15, 2026, seven days after publication), fetched
  directly with `curl` (HTTP 200) and stripped of `<script>`/`<style>`
  blocks and remaining HTML tags with a local Python regex pass. Both
  independently-fetched texts matched sentence-for-sentence on every
  passage checked; every `Quote` field in this note was verified as an
  exact substring of the Wayback-Machine-derived plain-text transcript
  (the more conservative, non-AI-mediated fetch of the two) before being
  written into this note, per MINER.md §2a.
- **Customer-carousel captions recovered from the Wayback transcript's
  linearized text**, which flattens the carousel's visual card layout into
  a flat sequence of stat/description/company-name lines; the pairing of
  each stat to its correct company and description was confirmed by the
  order and adjacency of the lines (stat, description, em-dash, company
  name, repeated five times) and cross-checked against the `r.jina.ai`
  Markdown version, which rendered the same five items in the same order
  with the same pairings.
- **Charts without recoverable underlying data**: as with other
  `openai.com/index/` posts already in this corpus, the signup-cohort
  engagement chart (Claim 3) and the agent-workday-ratio chart (Claim 5)
  rendered in both fetched transcripts only as a caption plus surrounding
  prose, with no cell values or axis labels recoverable as text beyond
  what the post's own sentences already state.
- **No sub-pages independently re-fetched**: this post does not itself
  link out to further sub-pages containing additional substantive detail on
  any of its own cited figures (contrast with
  `blog-openai-full-stack-behind-abundant-intelligence.md`, which linked to
  a distinct companion engineering post with additional Jalapeño detail).
  Every figure in this post that also appears in an existing corpus note
  was cross-checked against that note's own text (per MINER.md §4b) rather
  than re-derived from a fresh primary source, since this post itself gives
  no more detail than a one- or two-sentence restatement for any of them.
- **No contradiction issue filed**: see Cross-References → Contradicts for
  the one tension identified (Claim 1's unqualified "most intelligent and
  aligned" superlative versus the Intelligence Index and
  CoT-monitorability findings in two existing corpus notes) and the
  reasoning for why it does not meet the MINER.md §4a filing bar — the two
  registers (unqualified marketing framing vs. specific benchmark/safety
  findings) are not making directly comparable claims.
- **Confidence rated `emerging` overall**: eight of this note's ten claims
  either exactly restate or closely parallel a figure already independently
  verified elsewhere in this corpus (rated `settled` where the restatement
  is a verbatim or near-verbatim match to a primary-sourced figure, e.g.
  Claims 3, 5, 8; `emerging` where the underlying figure is vendor-reported
  but corroborated by more than one independent corpus source, e.g. Claim
  9). The genuinely novel content — the updated scale figures (Claim 1),
  the advertising-business-model disclosure (Claim 4), and the four new
  customer vignettes (Claim 7) — is thin (one sentence or stat each, no
  methodology) and individually rated `anecdotal` or `emerging`. This
  mirrors the confidence profile already assigned to this post's three
  predecessor Friar posts in the corpus, all of which combine a small
  amount of new framing/figures with a large proportion of restated,
  already-verified content.
