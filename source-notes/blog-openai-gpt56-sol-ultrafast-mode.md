---
source_url: https://openai.com/index/previewing-ultrafast
source_type: blog-post
title: "Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed"
author: OpenAI
date_published: 2026-08-13
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: emerging
issue: "#2885"
---

# Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed

> OpenAI previews Ultrafast, a new limited-preview API service tier that runs
> GPT‑5.6 Sol up to 14× faster than Standard processing (up to 750 output
> tokens/second), powered by a Cerebras hardware partnership. Four named
> early-access customers (Jane Street, Podium, Basis, Rogo) and internal
> OpenAI teams describe production use cases, but the source discloses no
> pricing, no general-availability date, and no mention of the existing
> Sol "Fast mode" (2.5×/2× price) — leaving the relationship between the
> two speed tiers unstated.

## Source Context

- **Type**: blog-post (OpenAI `openai.com/index/` "Product" news vertical,
  published August 13, 2026 — a short (~750-word) product-preview page with
  a customer-testimonial carousel, an embedded before/after demo video
  caption, and no benchmark table or technical/engineering deep-dive,
  unlike the companion engineering post OpenAI published alongside the
  July 30, 2026 Terra/Luna price cut).
- **Author credibility**: House-authored OpenAI product announcement, no
  named individual author. Contains four named external customer quotes
  (Jane Street, Podium, Basis, Rogo), attributed by name and title, all
  OpenAI-selected and OpenAI-published — standard vendor-testimonial
  credibility caveats apply. The core performance figures (14×, 750
  output tokens/second) are OpenAI's own unaudited, self-reported numbers;
  no independent benchmark (e.g., Artificial Analysis) is cited or linked.
- **Scope**: Covers the existence and headline performance claim of
  Ultrafast mode for GPT‑5.6 Sol, five illustrative target use cases,
  four customer testimonials, two internal-OpenAI usage examples
  (incident response, research), the Cerebras hardware partnership
  framing, and limited-preview availability status. Does NOT cover:
  pricing, a committed general-availability date, independent
  benchmarking of the 14×/750 tok/s figures, any technical explanation of
  *how* Cerebras achieves the speedup, or the relationship (if any) to
  the existing Sol "Fast mode" tier (2.5× speed / 2× price, documented in
  `blog-simonwillison-gpt56-luna-price-drop.md` Claim 6) — the word "Fast
  mode" does not appear anywhere in this source.

## Extracted Claims

### Claim 1: Ultrafast is a new API service tier for GPT‑5.6 Sol, up to 14× faster than Standard processing, powered by Cerebras, delivering up to 750 output tokens per second

- **Evidence**: The article's opening statement of the product itself —
  the headline claim the entire post is built around.
- **Confidence**: emerging (a specific, vendor-self-reported speed
  multiplier and throughput figure; no independent benchmark is cited)
- **Quote**: "Today, we’re sharing an early look at Ultrafast, a new
  service tier that runs GPT‑5.6 Sol up to 14× faster than Standard
  processing, launching first in the OpenAI API. Powered by Cerebras,
  Ultrafast generates up to 750 output tokens per second, bringing our
  most intelligent model to products and workflows where every second
  matters."
- **Our assessment**: 14× is a materially larger multiplier than any
  other OpenAI or Anthropic speed tier already in the corpus: OpenAI's
  own Sol "Fast mode" is up to 2.5× (`blog-simonwillison-gpt56-luna-price-drop.md`
  Claim 6), and Anthropic's Opus 4.8 fast mode is up to 2.5× OTPS
  (`blog-simonwillison-llm-anthropic-0251.md` Claim 4). The jump from
  ~2.5× (software/infra-tuned speed tiers) to 14× (a dedicated third-party
  inference-hardware partner) suggests a different mechanism class
  entirely, not an incremental extension of the same optimization work
  documented for Fast mode — see Claim 8 for what the source does and
  does not say about that mechanism.

### Claim 2: OpenAI frames Ultrafast as decoupling speed from model size — "more useful work per second" rather than the historical tradeoff of choosing a smaller or more specialized model for real-time speed

- **Evidence**: Direct positioning statement in the article.
- **Confidence**: emerging (vendor framing/positioning language, not a
  checkable technical fact)
- **Quote**: "Until now, getting real-time speed typically meant choosing
  a smaller or more specialized model. Ultrafast points to progress in a
  new direction: more useful work per second."
- **Our assessment**: This is a marketing framing device, not a
  benchmark claim, but it is a useful practitioner-facing heuristic if
  it holds up: historically, latency-sensitive products had to trade
  down to a smaller/cheaper model (e.g., Luna instead of Sol) to hit a
  real-time latency budget. If Ultrafast genuinely offers flagship-tier
  intelligence at 14× the throughput, it removes that tradeoff for
  Ultrafast-eligible workloads — but this is asserted, not demonstrated
  with a controlled quality comparison (see Claim 10 for the closest
  thing to supporting evidence, a single demo video).

### Claim 3: OpenAI names five target use-case categories for Ultrafast, each tied to a specific real-time workflow description: incident response and reliability, financial research and security, customer support and voice, commerce, and live research and experimentation

- **Evidence**: A bulleted list of scenarios in the article, each with a
  one-to-two-sentence description of the underlying workflow.
- **Confidence**: emerging (illustrative vendor-authored scenarios, not
  documented production deployments beyond the four testimonials in
  Claim 5)
- **Quote**: "Incident response and reliability: When a critical system
  fails, analyze application logs, recent code changes, and engineer
  reports to identify the likely cause and help prepare a fix while the
  outage is still unfolding." … "Financial research and security:
  Analyze market signals, assess transactions, and identify suspicious
  activity while conditions are still changing." … "Customer support and
  voice: Resolve complex customer issues in real time without
  interrupting the conversation, even when finding the answer requires
  multiple steps or systems." … "Commerce: Answer product questions,
  check inventory, personalize recommendations, and resolve checkout
  issues while the shopper is still deciding, before hesitation becomes
  an abandoned cart." … "Live research and experimentation: Turn
  research that previously took an overnight run into an interactive
  working session, letting teams test an idea, examine the results,
  adjust their approach, and run another experiment without breaking
  their flow."
- **Our assessment**: These five categories share a common shape: work
  where the model needs to reason over changing, time-sensitive state
  (an unfolding outage, moving market conditions, a live conversation, a
  shopper mid-decision, an interactive research loop) rather than
  batch-processing static input. This is a coherent product thesis —
  Ultrafast is being positioned for "keep pace with a changing situation"
  workloads, not simply "make existing batch jobs finish faster."

### Claim 4: OpenAI is running Ultrafast as a limited preview restricted to a select group of customers, with access "expanding as capacity grows," and discloses no pricing or general-availability date

- **Evidence**: The Availability section, the closing paragraph, and
  the "What early customers are experiencing" section framing.
- **Confidence**: settled (a directly stated, checkable rollout-status
  fact — the absence of pricing/GA-date information is independently
  verifiable by reading the full page, which this Miner did)
- **Quote**: "GPT‑5.6 Sol on Ultrafast mode is available in a limited
  preview today to a select group of customers. We’ll expand access as
  capacity grows." … "We’ve been testing GPT‑5.6 Sol on Ultrafast mode
  with an initial group of companies across coding, commerce, financial
  research, support, and other interactive applications."
- **Our assessment**: This directly answers (in the negative) the
  Prospector's triage question about "cost/throughput tradeoffs" and
  "pricing implications": there are none disclosed in this source. No
  price-per-token figure, multiplier over Standard pricing, or GA
  timeline appears anywhere in the article — a notable contrast with the
  July 30, 2026 Fast mode announcement, which gave an exact price
  multiplier (2× Standard) alongside its speed multiplier
  (`blog-simonwillison-gpt56-luna-price-drop.md` Claim 6). Any guide
  content citing Ultrafast should flag pricing and general availability
  as unknown/pending, not infer a price from the Fast mode precedent.

### Claim 5: Four named early-access customers describe Ultrafast as enabling qualitatively new product experiences, not just faster versions of existing ones

- **Evidence**: Four attributed customer testimonials in a carousel
  section of the article.
- **Confidence**: anecdotal (vendor-selected, vendor-published customer
  quotes from four companies; standard testimonial-credibility caveats
  apply — no independent verification of any of these accounts)
- **Quote**: "The increase in speed brought by Cerebras is impressive. It
  enables different ways of using the models, and makes it practical for
  developers to work in a more focused and productive way alongside
  them." —John Crepezzi, AI Assistants, Jane Street. "For us the
  Ultrafast has been invaluable in our voice stack. The speed completely
  changes the call experience for the more complex work." —Courtland
  Lykins, Product Lead—Voice AI, Podium. "Ultrafast allows us to create
  synchronous experiences for users that were previously limited by
  intelligence. Oftentimes the barrier to truly fast products is not
  just tokens per second, but also model intelligence, and ultrafast
  combines both." —Mitch Troyanovsky, Co-Founder, Basis. "Speed doesn’t
  just make the product feel better. It changes what people can
  realistically use it for. Ultrafast makes complex financial research
  feel like a real-time interaction." —Alex Wang, Applied AI, Rogo.
- **Our assessment**: The Basis quote is the most conceptually specific:
  it explicitly separates "tokens per second" from "model intelligence"
  as two independent barriers to a "truly fast product," and claims
  Ultrafast is the first offering to relax both simultaneously (previously
  practitioners had to choose one or the other — a smaller/faster model,
  or a larger/slower one). Podium's voice-stack framing is the most
  concrete production-workload data point (real-time voice calls are
  among the least latency-tolerant agentic use cases in the corpus). As
  with all vendor-published testimonials, treat as directional adoption
  signal, not as reproducible evidence.

### Claim 6: OpenAI's own internal engineering teams use Ultrafast for incident response, reading logs, analyzing traces, and preparing fixes "in a fraction of the time," while stating engineers "remain responsible for judgment and deployment"

- **Evidence**: A dedicated "How OpenAI is using Ultrafast" section
  describing OpenAI's own internal dogfooding of the product.
- **Confidence**: emerging (first-party self-reported internal usage
  example; no quantified time-savings figure given, only "a fraction of
  the time")
- **Quote**: "Incident response is one example where our team is using
  Ultrafast. When an alert fires, engineers need to build an accurate
  picture while the system and the evidence are still changing. Teams
  use it to quickly read logs, analyze traces, synthesize conversations,
  identify the next checks, and help prepare or validate a fix—all in a
  fraction of the time with the intelligence of Sol. It reduces the
  delay between observing a signal, testing a hypothesis, and choosing
  the next action, while engineers remain responsible for judgment and
  deployment."
- **Our assessment**: The explicit "engineers remain responsible for
  judgment and deployment" qualifier is notable as an autonomy-boundary
  statement: OpenAI frames Ultrafast as accelerating the
  observe-analyze-diagnose loop of incident response, not as
  autonomously deploying fixes. This is a narrower autonomy claim than
  some other agentic-ops examples already in the corpus (e.g., the
  autonomous training-run supervision documented in
  `blog-simonwillison-gpt56-luna-price-drop.md` Claim 9) — worth
  contrasting if the guide discusses agent autonomy boundaries in
  operational/SRE contexts.

### Claim 7: OpenAI's internal research team uses Ultrafast to tighten its experiment-iteration loop from an overnight batch cadence to multiple iterations within a single workday

- **Evidence**: Same "How OpenAI is using Ultrafast" section, second
  internal example.
- **Confidence**: emerging (first-party self-reported internal usage
  example; qualitative "loop tightening" claim, no quantified iteration
  count or time figure given)
- **Quote**: "For research, our team uses Ultrafast to rapidly search
  knowledge sources, query data, and quickly gather, organize, and
  summarize information across connected tools. A common workflow in
  research is for our team members to launch a batch of experiments
  over night, and review the results in the morning. With Ultrafast, we
  see this loop tightening to support multiple iterations during the
  workday instead."
- **Our assessment**: This directly corroborates the "Live research and
  experimentation" use case listed in Claim 3 with a concrete internal
  example: the specific before/after pattern (overnight batch → same-day
  multiple iterations) is a legible, reusable heuristic for practitioners
  evaluating whether a research/analysis workload is a good Ultrafast
  candidate — the test is whether the workload is currently
  latency-bound by an overnight or long-running batch cycle rather than
  by compute cost.

### Claim 8: OpenAI frames Ultrafast as "the next step" in an existing partnership with Cerebras for "ultra-low-latency inference," but discloses no further technical detail about the mechanism behind the 14×/750 tok/s figures

- **Evidence**: The "Powered by Cerebras" section — the only passage in
  the article addressing the underlying mechanism.
- **Confidence**: emerging (a partnership-framing statement; no
  architectural, chip-generation, or serving-infrastructure detail is
  given anywhere in the source)
- **Quote**: "Ultrafast marks the next step in our partnership with
  Cerebras to bring ultra-low-latency inference to OpenAI’s platform.
  Now, with GPT‑5.6 Sol on Ultrafast mode, Cerebras is supporting
  OpenAI’s most intelligent model, delivering up to 750 output tokens
  per second, enabling businesses to build more responsive products,
  make faster decisions, and bring powerful AI directly into their most
  demanding workflows."
- **Our assessment**: This directly answers, in the negative, the
  Prospector's second-triage key question about "the technical mechanism
  behind ultrafast mode's 14x speed claim." There is none in this
  source — no discussion of Cerebras wafer-scale hardware specifics, no
  serving-architecture detail, and (unlike the July 29, 2026 companion
  engineering post behind the Luna/Terra price cut, which detailed
  kernel rewrites, load-balancing tuning, and speculative-decoding
  work — `blog-simonwillison-gpt56-luna-price-drop.md` Claims 7–9) no
  linked companion technical post accompanies this announcement. "The
  next step in our partnership" implies a pre-existing OpenAI-Cerebras
  relationship predating this launch, but that relationship's prior
  scope is not described here and no earlier corpus source documents it.
  Any guide content should flag the mechanism as effectively a black box
  in this source — "faster because of specialized Cerebras hardware" is
  the full extent of the explanation offered.

### Claim 9: The source contains no pricing information for Ultrafast mode and never mentions the existing Sol "Fast mode" tier, leaving the relationship between the two speed offerings unstated

- **Evidence**: Absence, verified by reading the complete article text
  (all sections: intro, use cases, customer testimonials, internal
  usage, Cerebras partnership, availability) — no dollar figure, price
  multiplier, or the string "Fast mode" appears anywhere on the page.
- **Confidence**: settled (a directly verifiable absence in the full
  text of the source, not an inference)
- **Quote**: (no direct quote; see paraphrase in Our assessment — this
  claim documents what the source does *not* say)
- **Our assessment**: This is the single most guide-relevant gap in the
  source. OpenAI already sells a Sol speed tier — "Fast mode," up to
  2.5× faster at 2× the price, announced July 30, 2026
  (`blog-simonwillison-gpt56-luna-price-drop.md` Claim 6) — and this
  August 13 announcement neither references it, clarifies whether
  Ultrafast supersedes it, nor explains how a customer would choose
  between the two once Ultrafast reaches general availability. This is
  not treated as a formal contradiction per MINER.md §4a: neither source
  makes a claim that conflicts with the other (Fast mode's July 30 claims
  remain accurate for their own scope; Ultrafast's August 13 claims are
  simply silent on Fast mode's continued existence) — it is an
  information gap, not a factual dispute, so no contradiction issue was
  filed. The guide should present Ultrafast and Fast mode as two
  distinct, currently-coexisting Sol speed tiers with an unstated
  relationship, and flag this as an open question to revisit once
  OpenAI publishes GA/pricing details or a source directly addresses the
  overlap.

### Claim 10: A demo video caption claims GPT‑5.6 Sol on Ultrafast and Standard modes each built "a working 3D warehouse simulator from the same text prompt," presented side by side, as an implicit capability-parity demonstration

- **Evidence**: A single embedded demo video with an attached caption;
  no benchmark data, scoring, or third-party evaluation accompanies it.
- **Confidence**: anecdotal (a single, vendor-selected demo with no
  quantified comparison — the closest thing in the source to evidence
  for Claim 2's "no capability tradeoff" framing, but far short of a
  controlled benchmark)
- **Quote**: "GPT‑5.6 Sol Ultrafast and standard build a working 3D
  warehouse simulator from the same text prompt, side by side."
- **Our assessment**: This is the only piece of the source that
  gestures at output-quality parity between Ultrafast and Standard
  processing rather than just asserting it (Claim 2). It is a single
  cherry-picked demo task with no independent judging, no failure-case
  disclosure, and no indication of how many attempts were needed to
  produce a comparably "working" result on each side — treat as
  illustrative marketing material, not evidence that Ultrafast carries
  no quality tradeoff in general.

## Concrete Artifacts

### Ultrafast headline spec (from OpenAI, August 13, 2026)

```
Model:            GPT-5.6 Sol
Tier name:        Ultrafast
Speed:             up to 14x faster than Standard processing
Throughput:        up to 750 output tokens/second
Hardware partner:  Cerebras
Launch surface:    OpenAI API (first)
Availability:      Limited preview, select customers only
Pricing:           Not disclosed
GA date:           Not disclosed ("as capacity grows")

Source: openai.com/index/previewing-ultrafast, August 13, 2026
(fetched via Wayback Machine snapshot 2026-08-15; live URL returned
HTTP 403 Cloudflare bot-challenge to direct curl)
```

### Target use cases (verbatim list, from OpenAI)

```
- Incident response and reliability: analyze application logs, recent
  code changes, and engineer reports to identify a likely cause and help
  prepare a fix while an outage is still unfolding.
- Financial research and security: analyze market signals, assess
  transactions, and identify suspicious activity while conditions are
  still changing.
- Customer support and voice: resolve complex customer issues in real
  time without interrupting the conversation, even across multiple
  steps/systems.
- Commerce: answer product questions, check inventory, personalize
  recommendations, and resolve checkout issues while the shopper is
  still deciding.
- Live research and experimentation: turn overnight-run research into
  an interactive working session with multiple iterate/adjust/re-run
  cycles.

Source: openai.com/index/previewing-ultrafast, August 13, 2026
```

### Customer testimonials (from OpenAI, August 13, 2026)

```
Jane Street — John Crepezzi, AI Assistants
  "The increase in speed brought by Cerebras is impressive. It enables
  different ways of using the models, and makes it practical for
  developers to work in a more focused and productive way alongside
  them."

Podium — Courtland Lykins, Product Lead—Voice AI
  "For us the Ultrafast has been invaluable in our voice stack. The
  speed completely changes the call experience for the more complex
  work."

Basis — Mitch Troyanovsky, Co-Founder
  "Ultrafast allows us to create synchronous experiences for users that
  were previously limited by intelligence. Oftentimes the barrier to
  truly fast products is not just tokens per second, but also model
  intelligence, and ultrafast combines both."

Rogo — Alex Wang, Applied AI
  "Speed doesn't just make the product feel better. It changes what
  people can realistically use it for. Ultrafast makes complex
  financial research feel like a real-time interaction."

Source: openai.com/index/previewing-ultrafast, August 13, 2026
```

### Internal OpenAI usage examples (from OpenAI, August 13, 2026)

```
Incident response:
  - Read logs, analyze traces, synthesize conversations, identify next
    checks, prepare/validate a fix — "all in a fraction of the time"
  - Explicit qualifier: "engineers remain responsible for judgment and
    deployment"

Research:
  - Rapid knowledge-source search, data query, gather/organize/summarize
    across connected tools
  - Before: batch of experiments launched overnight, reviewed next
    morning
  - After (with Ultrafast): "this loop tightening to support multiple
    iterations during the workday instead"

Source: openai.com/index/previewing-ultrafast, August 13, 2026
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-anthropic-0251.md` Claim 4 (Anthropic Opus
    4.8 fast mode: up to 2.5× OTPS at premium pricing) and
    `blog-simonwillison-gpt56-luna-price-drop.md` Claim 6 (OpenAI Sol
    "Fast mode": up to 2.5× speed at 2× Standard price): all three
    sources corroborate the broader pattern of frontier labs offering a
    paid speed dial on a flagship model as a distinct lever from price
    cuts. This source's 14× figure is corroborating evidence that speed
    is now being marketed as its own competitive axis, alongside price
    and capability — but see Cross-References → Novel for why the
    magnitude and mechanism differ from the other two.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 13 ("nearly nine
    times the speed" for Luna vs. year-old frontier-class models):
    another OpenAI-authored double-digit-adjacent speed claim from three
    weeks earlier, though for a smaller/cheaper model rather than a
    hardware-accelerated flagship-model tier — both sources show OpenAI
    leaning on large speed multipliers as a headline marketing figure
    across different product mechanisms.

- **Contradicts**: None filed as a formal contradiction issue. See
  Claim 9 for the identified information gap (this source's silence on
  the existing Sol "Fast mode" tier) — judged an absence, not a
  conflicting claim, per MINER.md §4a.

- **Extends**:
  - `blog-openai-gpt56-ga-announcement.md` Claim 1 and
    `blog-simonwillison-gpt56-sol-launch.md` Concrete Artifacts (Sol's
    baseline identity and $5/$30 per-million-token pricing): this source
    adds a new, still-unpriced speed tier atop that established Sol
    baseline without revising Sol's own price.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 6 (Fast mode:
    2.5×/2× price for Sol): Ultrafast is a second, much larger (14×)
    speed tier for the same underlying model, introduced roughly two
    weeks later, whose relationship to Fast mode is unaddressed by
    either source (see Claim 9).

- **Novel**:
  - First corpus documentation of Cerebras as a named OpenAI inference
    hardware partner, and of any inference speed multiplier in the
    double-digit range (14×) — all prior corpus speed-tier figures for
    OpenAI and Anthropic (Fast mode variants) top out at roughly 2.5×.
  - First corpus source describing a speed tier as achieved via a
    dedicated third-party inference-hardware partnership rather than
    in-house serving-infrastructure optimization (contrast with the
    kernel-rewrite/load-balancing/speculative-decoding work documented
    for OpenAI's own price-cut efficiency gains in
    `blog-simonwillison-gpt56-luna-price-drop.md` Claims 7–9).
  - First corpus customer testimonials specifically about a speed
    product (as opposed to testimonials about a price cut, a GA launch,
    or general model capability) — four new named companies (Jane
    Street, Podium, Basis, Rogo) not previously present in the corpus's
    GPT-5.6 customer-testimonial coverage.
  - First corpus example of an internal OpenAI incident-response
    workflow with an explicit "engineers remain responsible for judgment
    and deployment" autonomy-boundary statement tied to a specific
    product feature.

## Guide Impact

- **Chapter 02 (Harness Engineering) / model-selection sections**: Add
  Ultrafast as a third documented Sol speed option alongside Standard
  and Fast mode (2.5×/2× price). State clearly that, as of this source,
  Ultrafast is limited-preview only, has no disclosed pricing or GA
  date, and its relationship to Fast mode (replaces it? coexists with
  it? different eligibility?) is not addressed by either vendor source —
  do not present Ultrafast as generally available or as a documented
  Fast-mode replacement.

- **Chapter 04 (inference optimization / latency patterns)**: Document
  Cerebras-partnered hardware acceleration as a distinct optimization
  path from OpenAI's own software/infrastructure-level Fast mode work
  and Anthropic's fast mode — note explicitly that this source gives no
  mechanism-level detail (no kernel, chip, or serving-architecture
  specifics), unlike the companion engineering post OpenAI published for
  the July 30 Luna/Terra price cut. Add the five named use-case
  categories (Claim 3) and the internal "overnight batch → same-workday
  iteration" pattern (Claim 7) as illustrative heuristics for identifying
  workloads where a large speed multiplier — not a cost cut — is the
  binding constraint.

- **Chapter 05 (API capabilities / vendor speed-tier landscape)**: Add
  the customer testimonials (Claim 5), especially Podium's real-time
  voice-stack use case and Basis's "tokens per second is not the only
  barrier — model intelligence is the other" framing, as concrete
  practitioner-reported motivations for choosing a hardware-accelerated
  speed tier over a smaller/cheaper model for latency-bound production
  workloads.

- No chapter should cite the 14× or 750 output-tokens/second figures as
  independently verified — both are OpenAI's own unaudited numbers, with
  no third-party benchmark (e.g., Artificial Analysis) cited in this
  source or found elsewhere in the corpus for Ultrafast specifically.

## Extraction Notes

- **Live URL blocked**: `https://openai.com/index/previewing-ultrafast`
  returned HTTP 403 with a Cloudflare bot-challenge (`cf-mitigated:
  challenge` response header) to both the WebFetch tool and a direct
  `curl` with browser headers — consistent with the same access pattern
  already documented for `openai.com/index/` pages in
  `blog-openai-gpt56-ga-announcement.md` and
  `blog-simonwillison-gpt56-luna-price-drop.md`. The article was
  retrieved via an Internet Archive Wayback Machine snapshot dated
  2026-08-15 (`web.archive.org/web/20260815181741/`), stripped of
  HTML/scripts/styles, and hand-extracted. The RSS feed description
  (`openai.com/news/rss.xml`) was independently fetched and its summary
  text cross-checked against the article's opening paragraph — the two
  match.
- **Three outbound links followed, per MINER.md §1**: the article links
  to `openai.com/index/gpt-5-6-frontier-intelligence-efficiency/` and
  `openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/`
  — both already fully mined in
  `blog-simonwillison-gpt56-luna-price-drop.md` (Claims 7–11 and Claim 6
  respectively) and not re-extracted here. A third link,
  `openai.com/index/improving-gpt-5-6-sol-in-chatgpt/` (published August
  6, 2026), was fetched via Wayback Machine (snapshot 2026-08-16) and
  read in full: it is a ChatGPT consumer-product update (factual-accuracy
  improvements, a new response-length slider, and expanding GPT-5.6 Luna
  to free-tier users) unrelated to inference speed or Ultrafast mode —
  judged off-topic for this note and not extracted as claims. It is not
  yet present anywhere in the corpus and may be worth a separate source
  submission if the Prospector judges its factual-accuracy claims
  (reported ~62%/68% fewer factual errors for Luna/Sol vs. GPT-5.5
  Instant) independently novel.
- **No contradiction issue filed**: see Cross-References → Contradicts
  and Claim 9 — the source's silence on Fast mode is an information gap,
  not a conflicting claim, per MINER.md §4a's "when not to file"
  guidance.
- **Source is short and thin on mechanism**: at ~750 words with no
  benchmark table, no linked companion engineering post, and no pricing,
  this is one of the shorter and less technically detailed OpenAI
  product-announcement sources in the corpus. All ten claims above
  exhaust the substantive content of the page; there was no additional
  depth to extract beyond what is captured here.
