---
source_url: https://openai.com/index/gpt-5-6
source_type: blog-post
title: "GPT‑5.6: Frontier intelligence that scales with your ambition"
author: OpenAI
date_published: 2026-07-09
date_extracted: 2026-07-27
last_checked: 2026-07-27
status: current
confidence_overall: emerging
issue: "#2257"
---

# GPT‑5.6: Frontier intelligence that scales with your ambition

> OpenAI's own general-availability announcement for the GPT‑5.6 family
> (Sol/Terra/Luna) — the primary source that Simon Willison quoted from in
> `blog-simonwillison-gpt56-ga-launch.md`. Beyond the two benchmarks
> Willison covered, this page adds a much larger vendor-reported benchmark
> table (11 domains, up to 10 comparison models), a new `ultra` parallel
> multi-agent capability setting, detailed cybersecurity capability numbers
> and a layered-safeguard architecture description, an individual-level
> "Trusted Access for Cyber" identity-verification requirement, internal
> OpenAI research-acceleration metrics, and eleven new model-level customer
> testimonials distinct from the ChatGPT Work product testimonials already
> mined in `blog-openai-chatgpt-work-ambitious-partner.md`.

## Source Context

- **Type**: blog-post (OpenAI "Product"/"Release" news vertical,
  `openai.com/index/`, published July 9, 2026 — the same day as
  `blog-openai-chatgpt-work-ambitious-partner.md`; a long-form
  benchmark-heavy model-release page with an interactive chart carousel,
  an 11-testimonial customer carousel, a large tabbed benchmark-table
  section, and a dedicated safety section).
- **Author credibility**: House-authored OpenAI product/research
  announcement, no named individual author. Contains eleven named external
  customer/partner quotes (Cursor, Qodo, Notion, Cognition, Rogo, Ramp,
  Shopify, Cisco, Clio, Balyasny Asset Management, Basis) attributed by
  name and title, all OpenAI-selected and OpenAI-published. All benchmark
  comparisons against Claude and Gemini models are self-reported by OpenAI,
  run on OpenAI's own harnesses (e.g., footnote 2: "All models are
  evaluated using the ExploitBench API harness with 5 seeds and reasoning
  continuity") — standard vendor-benchmark and vendor-testimonial
  credibility caveats apply throughout.
- **Scope**: Covers the GPT‑5.6 Sol/Terra/Luna GA launch, the new `ultra`
  parallel-multi-agent capability setting, Programmatic Tool Calling, a
  large benchmark table spanning professional/coding/science-health/
  computer-use/cybersecurity/self-improvement/multimodal/academic/
  tool-use/long-context/abstract-reasoning categories, cybersecurity
  capability claims and safeguard architecture, an individual "Trusted
  Access for Cyber" identity-verification requirement, internal OpenAI
  research-acceleration metrics, design/computer-use capability claims,
  eleven customer testimonials, and pricing/availability by plan tier.
  Does NOT cover: independent (non-OpenAI) verification of any benchmark
  number, the ChatGPT Work product surface itself (covered separately in
  `blog-openai-chatgpt-work-ambitious-partner.md`), or methodology detail
  beyond the numbered footnotes.

## Extracted Claims

### Claim 1: GPT‑5.6 launches for general availability as a three-tier family — Sol (flagship), Terra (balanced/everyday), and Luna (most cost-efficient) — following the limited preview
- **Evidence**: Direct product-launch statement in the post's opening paragraph; this is the primary source Willison quoted in `blog-simonwillison-gpt56-ga-launch.md` and `blog-simonwillison-gpt56-sol-launch.md`.
- **Confidence**: settled (unambiguous, dated GA launch announcement from the vendor itself; naming/tiering is a fact, not a performance claim)
- **Quote**: "We're launching the GPT‑5.6 family of models for general availability following our limited preview: our new flagship, Sol, alongside Terra, a balanced model for everyday work, and Luna, our most cost-efficient model."
- **Our assessment**: This confirms, from the primary source rather than a secondhand quote, the same July 9, 2026 GA date and Sol/Terra/Luna naming already independently documented in `blog-simonwillison-gpt56-ga-launch.md` Claim 1 and `blog-openai-chatgpt-work-ambitious-partner.md` Claim 3. No new information here beyond confirming the corpus's existing GA-date evidence now traces directly to the vendor's own page (this Miner successfully fetched it via the Wayback Machine after the live URL returned an HTTP 403 Cloudflare bot-challenge — see Extraction Notes).

### Claim 2: `ultra` is GPT‑5.6's highest-capability setting, coordinating four agents in parallel by default (up to 16 in some published evaluations) to trade higher token use for stronger results and faster time-to-result on demanding tasks
- **Evidence**: Direct feature description plus three named benchmark comparisons (BrowseComp, SEC-Bench Pro, Terminal-Bench 2.1) showing ultra's score-latency frontier versus a one-agent baseline.
- **Confidence**: emerging (a specific, named capability with vendor-reported benchmark support, not independently reproduced elsewhere in the corpus)
- **Quote**: "ultra is our highest-capability setting, coordinating multiple agents across parallel workstreams to finish complex tasks faster." ... "ultra goes further by coordinating four agents in parallel by default, trading higher token use for stronger results and faster time-to-result on demanding tasks. The charts below compare ultra's default four-agent setup with a one-agent baseline across BrowseComp, SEC-Bench Pro, and Terminal-Bench 2.1; BrowseComp and SEC-Bench Pro also show 16-agent configurations. Across all three evaluations, adding parallel agents shifts the score-latency frontier upward and to the left, reaching stronger results in less time. In the API, developers can build ultra-like experiences using the multi-agent beta in the Responses API."
- **Our assessment**: This substantially extends `blog-simonwillison-gpt56-ga-launch.md` Claim 9, which only had Willison's one-sentence secondhand paraphrase of the Multi-agent API ("spin up subagents for parallel, focused work") to go on, with the Multi-agent docs page itself unreachable during that extraction. Here the primary source gives concrete mechanics (4 agents by default, up to 16 in evaluations) and three named benchmarks showing the parallel-agent approach actually shifting the score-latency frontier rather than just adding cost. `ultra`-as-a-product-setting (available to ChatGPT Work Pro/Enterprise and Codex Plus+ users, per Claim 12) and the underlying Multi-agent API beta are presented as two surfaces of the same capability — a product-level packaging of native multi-agent orchestration that was previously only documented in this corpus as an API primitive.

### Claim 3: Programmatic Tool Calling lets GPT‑5.6 write and run lightweight in-memory programs that coordinate tools, filter large volumes of intermediate data, and adapt their workflow — reducing token use, model round trips, and developer scripting effort — and is compatible with Zero Data Retention (ZDR)
- **Evidence**: Direct feature description, corroborated against `blog-simonwillison-gpt56-ga-launch.md` Claim 8's independent verification against OpenAI's Programmatic Tool Calling developer docs.
- **Confidence**: settled (a named, documented API feature; the ZDR-compatibility claim is a specific, checkable product detail)
- **Quote**: "GPT‑5.6 can write and run lightweight programs that coordinate tools, process intermediate results, monitor progress, and choose the next action as work unfolds. This lets tool-heavy tasks advance with fewer tokens, fewer model round trips, and less guidance. Instead of requiring developers to script every step or passing every tool response back through the model, Programmatic Tool Calling in the Responses API can filter large amounts of intermediate data, retain only what matters, and adapt its workflow along the way." ... "In the Responses API, Programmatic Tool Calling lets GPT‑5.6 write and run programs in-memory that coordinate tools and process intermediate results, making it Zero Data Retention (ZDR) compatible."
- **Our assessment**: Corroborates and slightly extends `blog-simonwillison-gpt56-ga-launch.md` Claim 8 (sandboxed V8 runtime, `allowed_callers` gating, verified against OpenAI's docs page) — this page adds the explicit "ZDR compatible" framing, which that note's Concrete Artifacts table lists as a docs-verified property but does not attribute to this specific launch page. No new architectural detail beyond what's already in the corpus for this feature.

### Claim 4: Across an 11-domain, vendor-run benchmark table comparing GPT‑5.6 (Sol/Sol Ultra/Terra/Luna) against GPT‑5.5, Claude Fable 5, Claude Opus 4.8, Claude Mythos 5, Claude Mythos Preview, Gemini 3.1 Pro Preview, and Gemini 3.5 Flash, no single model wins across every category — GPT‑5.6 Sol leads on SWE-Bench Pro's coding-agent-index framing while Claude Fable 5 leads SWE-Bench Pro itself, and results diverge further by domain (cybersecurity, science, computer use, long context)
- **Evidence**: A large published results table (reproduced in Concrete Artifacts below) spanning Professional, Coding, Science and health, Computer use, Cybersecurity, Self-improvement, Multimodal, Academic, Tool use, Long context, and Abstract reasoning categories.
- **Confidence**: emerging (extensive vendor-self-reported benchmark data, not independently reproduced; see Extraction Notes on table-transcription risk)
- **Quote**: (no single-sentence quote captures the table; see the Coding section row directly below and Concrete Artifacts for the full reproduced table)
- **Our assessment**: On the one row independently corroborated elsewhere in the corpus — SWE-Bench Pro, where the table shows GPT‑5.6 Sol at 64.6% against Claude Fable 5 at 80% — this table's Fable 5 figure matches `blog-simonwillison-gpt56-ga-launch.md` Claim 5 exactly (also 80%, quoted from this same source by Willison), which gives confidence the table was scraped correctly at least at that cell. The table also shows Claude Mythos 5 at 80.3% and Claude Mythos Preview at 77.8% on SWE-Bench Pro — two Claude variants not covered in either existing GPT‑5.6 note, since Willison's post only named Fable 5. This extends the corpus's "benchmark choice determines the winner" pattern (already established by `blog-simonwillison-gpt56-ga-launch.md` Claims 4-7) with many more comparison points across a much wider set of domains than the two benchmarks Willison covered.

### Claim 5: On the Artificial Analysis Coding Agent Index, GPT‑5.6 Sol with max reasoning sets a new state of the art at 80 — 2.8 points above Claude Fable 5 — while using less than half the output tokens, less than half the time, and about one-third less cost; the advantage extends down the tier ladder (Terra above Fable 5, Luna above Claude Opus 4.8)
- **Evidence**: Direct benchmark claim in the "Efficient by default" section, distinct from the SWE-Bench Pro figure in Claim 4.
- **Confidence**: emerging (vendor-reported index score and efficiency multipliers, not independently reproduced)
- **Quote**: "GPT‑5.6 Sol is our best coding model yet. On the Artificial Analysis Coding Agent Index, GPT‑5.6 Sol with max reasoning sets a new state of the art at 80, 2.8 points above Fable 5, while using less than half the output tokens, taking less than half the time, and costing about one-third less. That advantage extends across the family: Terra performs just above Fable 5, while Luna outperforms Opus 4.8; each does so in roughly one-third of the time, with about half as many output tokens, and at approximately one-quarter the estimated cost."
- **Our assessment**: This is a different, coding-agent-composite benchmark from SWE-Bench Pro (Claim 4/Willison's Claim 5), and on this index GPT‑5.6 Sol claims the win over Fable 5 rather than losing to it — reinforcing that "GPT‑5.6 beats Fable 5" and "Fable 5 beats GPT‑5.6" are both true depending on which coding benchmark is cited, a sharper illustration of the same benchmark-choice-determines-winner pattern already flagged for Ch03 guidance in the existing GPT‑5.6 notes.

### Claim 6: GPT‑5.6 is OpenAI's strongest cybersecurity model to date — scoring 73.5% on ExploitBench (vs. GPT‑5.5's 47.9%), reaching a 33.7% pass rate on ExploitGym under a six-hour cap (vs. GPT‑5.5's 15.1% two-hour-cap peak), and 71.2% on SEC-Bench Pro (vs. GPT‑5.5's 45.8%)
- **Evidence**: Three named benchmark results with methodology footnotes (ExploitBench evaluated via OpenAI's own API harness with 5 seeds and reasoning continuity; ExploitGym rescaled from an internal alpha API to match public-API latency).
- **Confidence**: emerging (specific, quantified vendor-reported cybersecurity capability numbers; cyber capabilities are explicitly evaluated "with reduced safeguards" per footnote 1, and no independent red-team source in the corpus reproduces these figures)
- **Quote**: "GPT‑5.6 is our strongest cybersecurity model yet, achieving frontier performance with significantly fewer tokens. On ExploitBench, which measures progress from reaching vulnerable code through arbitrary code execution, it scores 73.5% versus GPT‑5.5's 47.9% at a comparable output-token budget. On ExploitGym, which asks agents to turn real-world vulnerabilities into working exploits, it almost doubles GPT‑5.5's peak pass rate, from 15.1% to 24.9% under the two-hour cap; with six hours, it reaches 33.7%. On SEC-Bench Pro, which tests proof-of-concept generation on complex software, it scores 71.2% versus GPT‑5.5's 45.8% at an improved latency."
- **Our assessment**: A large, specific generational jump in offensive-capable cyber benchmarks (roughly 1.5x on ExploitBench, more than 2x on ExploitGym, 1.55x on SEC-Bench Pro) is the concrete evidence behind this post's separate safety claims (Claims 7-8) that GPT‑5.6 required a materially stronger safeguard system. Novel to the corpus — no existing source note has this level of specific offensive-cyber-benchmark detail for any OpenAI model generation.

### Claim 7: GPT‑5.6's safeguards are architecturally layered — protections trained into the model, combined with real-time checks, continuous monitoring, and account-level enforcement, plus a "reasoning monitor" that reviews conversations for potential harm, in contrast to systems relying only on classifier flags from lower-intelligence models
- **Evidence**: Direct architecture description in the "Scaling safety and security with capability" section.
- **Confidence**: emerging (a specific, named safety-architecture description from the vendor; no independent evaluation of the reasoning monitor's accuracy or false-positive/negative rate is given)
- **Quote**: "GPT‑5.6's safeguards are layered for greater accuracy and redundancy, and designed to adapt quickly as new attacks emerge. Protections trained into the model work alongside real-time checks, continuous monitoring, and account-level enforcement, to help the system remain safe even when a particular layer does not work as intended. In many systems, classifier flags alone decide what to block, relying on lower intelligence models that are harder to change in order to prevent harm. Our approach adds a reasoning monitor that reviews the conversation to determine if there is a potential for harm. This design is intended to enable defensive work while blocking serious misuse, with the most sensitive capabilities reserved for verified users through Trusted Access. Because some protections use test-time reasoning, we can rapidly update them to close gaps without retraining classifiers from scratch."
- **Our assessment**: A concrete, named architectural pattern — using a reasoning-capable model as a monitor layer instead of (or alongside) a separately-trained lower-intelligence classifier — that is directly relevant to any Ch03 discussion of automated safety/verification gates, structurally similar to the "Auto-review" pattern already documented for ChatGPT Work in `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13 (a model reviewing agent actions before execution), but applied here to safety/misuse detection rather than task-execution governance. The post explicitly frames "test-time reasoning" as enabling faster iteration than retraining a classifier — a maintainability argument for reasoning-based safety layers worth noting alongside the architectural claim itself.

### Claim 8: Compared with previous models, GPT‑5.6 Sol's cyber safeguards block roughly ten times more potentially harmful activity, and the model does not cross the "Critical" capability threshold in either biology or cybersecurity despite being more capable than earlier OpenAI models in both domains
- **Evidence**: Direct safety-evaluation claims in the same section, following the cybersecurity capability jump documented in Claim 6.
- **Confidence**: emerging (specific vendor-reported safety-filtering multiplier and a categorical threshold-crossing claim tied to OpenAI's own capability-threshold framework, not independently audited in this corpus)
- **Quote**: "The GPT‑5.6 models are more capable than our earlier models in both biology and cybersecurity but do not cross the Critical threshold in either category. In cybersecurity, our testing suggests GPT‑5.6 is better at finding and fixing vulnerabilities than at reliably carrying out autonomous, end-to-end attacks against hardened targets—giving defenders an opportunity to strengthen systems before weaknesses are exploited. In biology, our testing suggests GPT‑5.6 can support legitimate research but does not provide the end-to-end capability needed to create, engineer, or synthesize a highly dangerous novel threat." ... "Compared with previous models, our GPT‑5.6 Sol cyber safeguards block roughly ten times more potentially harmful activity. Because these measures can create friction for benign use, we provide an option in ChatGPT and Codex to easily retry prompts on lower-capability models, and we will continue reducing the impact of our safeguards on benign use while maintaining a high robustness bar."
- **Our assessment**: The "roughly ten times more potentially harmful activity" blocked figure is a specific, falsifiable-in-principle claim, but as with the capability benchmarks in Claim 6, it is self-measured and self-reported with no disclosed methodology for what counts as "potentially harmful activity" or how the 10x baseline comparison was constructed. The explicit acknowledgment that stronger safeguards "create friction for benign use" (with a documented mitigation — retry on a lower-capability model) is a useful concrete data point for any guide discussion of the safety/usability tradeoff in agentic cyber tooling.

### Claim 9: Before GA, OpenAI ran approximately 700,000 NVIDIA A100 Tensor Core GPU-equivalent hours of black-box automated red teaming against GPT‑5.6, alongside extensive human red teaming and external-expert safeguard testing
- **Evidence**: Direct, quantified safety-investment claim in the same section.
- **Confidence**: emerging (a specific, large compute-hours figure with no independent way to verify or contextualize against a prior generation's red-teaming investment, since no comparable prior-generation figure is given in this post or elsewhere in the corpus)
- **Quote**: "Before general availability, we ran our most intensive safety evaluations to date, including extensive red teaming, robust capability and safeguard testing with external experts, and approximately 700,000 NVIDIA A100 Tensor Core GPU-equivalent hours of black-box automated red teaming. This enabled us to systematically probe likely weak points, surface jailbreaks, and help us strengthen the system before launch."
- **Our assessment**: Novel to the corpus — no existing source note quantifies pre-release automated red-teaming investment in GPU-hours for any model generation from any vendor. Useful as a concrete (if unaudited and incomparable) data point if the guide ever discusses the scale of pre-release safety testing frontier labs report investing.

### Claim 10: Individuals seeking OpenAI Daybreak's "Trusted Access for Cyber" program must verify their identity, and members must enable Advanced Account Security with hardware-backed passkeys by September 1 (2026) to retain access to OpenAI's most cyber-capable frontier models — those who don't will revert to default (safeguarded) access; OpenAI is separately partnering with Yubico to offer preferred pricing on hardware keys
- **Evidence**: Direct program-requirement description immediately following the cybersecurity capability claims.
- **Confidence**: settled (a specific, dated, checkable access-control policy from the vendor)
- **Quote**: "Individuals can verify their identity and request trusted access, and organizations can apply for their teams. Individual members will need to enable Advanced Account Security with hardware-backed passkeys by September 1 to retain access to our most cyber-capable frontier models; those who do not will return to default access. Users who do not already have hardware-backed passkeys can receive preferred pricing from our partner, Yubico. We are also taking additional steps to restrict access to high-risk entities and in high-risk jurisdictions."
- **Our assessment**: This extends `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 4, which documented the Daybreak program's government-level "Trusted Access for Cyber" partnerships with nine named allied governments — this source adds the individual/organizational access tier of the same program, with a concrete enforcement mechanism (hardware-backed-passkey deadline, with automatic downgrade to default access on non-compliance) not previously documented in the corpus. The Yubico partnership for "preferred pricing" is a novel, specific vendor-security-hardware collaboration detail.

### Claim 11: Inside OpenAI, GPT‑5.6 accelerated internal AI research measurably — average daily output tokens per active researcher during internal testing were more than twice the highest level observed for GPT‑5.5, the share of research compute devoted to internal coding inference grew 100-fold over the past six months, and internal agentic token usage grew approximately 22-fold over the same period; on an internal "RSI Index" bundle of research-acceleration evaluations, GPT‑5.6 Sol scores a 16.2-point improvement over GPT‑5.5
- **Evidence**: Direct internal-adoption and internal-evaluation claims in the "GPT‑5.6 accelerates OpenAI" section.
- **Confidence**: anecdotal for the token-usage-growth figures (internal telemetry, no external verification possible) and emerging for the RSI Index score (a named internal benchmark, self-administered)
- **Quote**: "We already saw that acceleration and stronger adoption during the internal testing period of GPT‑5.6, as average daily output tokens per active researcher were more than twice the highest level observed for GPT‑5.5." ... "Over the past six months, the share of research compute devoted to internal coding inference grew 100-fold, while internal agentic token usage increased approximately 22-fold." ... "On a bundle of evaluations measuring progress towards recursive self-improvement, we observe GPT‑5.6 Sol to be a 16.2 point improvement over GPT‑5.5, accelerating internal research across the board."
- **Our assessment**: This corroborates the general "OpenAI's internal engineering org has moved to near-total agentic-coding adoption" thesis already documented in `blog-openai-agents-transforming-work.md` (Codex at 99.8% of weekly company-wide output tokens, ~June 25, 2026) and `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 ("nearly 100% of teams... use ChatGPT Work and Codex"), but adds a new, more research-specific angle: growth *rate* metrics (100x research-compute share, 22x agentic token usage over six months) rather than a snapshot adoption percentage. The post itself caveats that "these adoption metrics do not measure research progress on their own" — a self-aware limitation worth preserving alongside the headline multipliers.

### Claim 12: On GeneBench Pro, GPT‑5.6 Sol reaches 28.7% — the identical figure independently documented in `blog-openai-genebench-pro-case-studies.md` — and OpenAI states that Claude Fable 5 is excluded from this chart because it "does not answer" advanced biology questions and refuses the majority of questions in the eval
- **Evidence**: A chart caption/footnote accompanying the GeneBench Pro results, plus the benchmark table's numeric value for GPT‑5.6 Sol.
- **Confidence**: settled for the GPT‑5.6 Sol score (independently corroborated, character-for-character, by a dedicated OpenAI benchmark case-studies page mined separately) and anecdotal for the Fable-5-refusal claim (a vendor's characterization of a competitor model's behavior, with no disclosed refusal rate or example prompts)
- **Quote**: "GeneBench Pro: Long-horizon genomics and quantitative-biology analyses; GPT‑5.6 reaches stronger results with fewer tokens and less time. Claude Fable 5 is not included as it does not answer advanced biology questions and refuses the majority of questions in this eval."
- **Our assessment**: The 28.7% Sol figure matching `blog-openai-genebench-pro-case-studies.md` exactly (that note's Claim 8, sourced independently from OpenAI's dedicated GeneBench Pro announcement) is a strong internal-consistency check across two separate OpenAI publications. The Fable-5-refusal characterization should be treated with more skepticism than the score itself: it is OpenAI's unaudited explanation for a competitor's absence from its own comparison chart, with no refusal-rate number, no example prompts, and no way to distinguish "the model correctly declines unsafe dual-use biology requests" from "the model is miscalibrated toward over-refusal" from this source alone. Worth flagging for any Ch03 discussion of dual-use biology-benchmark refusal behavior as a claim requiring independent verification, not evidence in either direction on its own.

### Claim 13: GPT‑5.6 delivers "a step change in design judgment," using stronger computer-use capabilities to inspect and refine its own rendered output — not just generate underlying code or content — catching visual and functional issues before handing work back; on OSWorld 2.0 it sets a new state of the art at 62.6%, surpassing Claude Opus 4.8 while using 85% fewer output tokens
- **Evidence**: Direct capability description in the "A leap forward in design" section, plus a named computer-use benchmark result.
- **Confidence**: emerging (a specific, named benchmark score and efficiency multiplier; the qualitative "step change in design judgment" framing is unquantified vendor characterization)
- **Quote**: "GPT‑5.6 delivers a step change in design judgment. With only high-level direction, GPT‑5.6 creates tasteful, ergonomic, and functional interfaces. Its stronger computer-use capabilities let it inspect and refine the rendered result—not just generate the underlying code or content—so it can catch visual and functional issues and apply finishing touches before handing the work back." ... "GPT‑5.6 Sol sets new state-of-the-art results on BrowseComp at 92.2% and OSWorld 2.0 at 62.6%; on OSWorld, it surpasses Opus 4.8 while using 85% fewer output tokens."
- **Our assessment**: The "inspect and refine the rendered result, not just generate the code" framing is a specific mechanistic claim about closing the loop between generation and verification for UI/design output — conceptually adjacent to the guide's existing verification-loop material, but applied here to visual/design correctness rather than code correctness. The 85%-fewer-output-tokens efficiency figure on OSWorld 2.0, if accurate, is a notable efficiency gap for a task category (computer use) that is typically token-expensive.

### Claim 14: GPT‑5.6 access is tiered by product surface and plan — ChatGPT Chat gives Plus/Pro/Business/Enterprise users Sol at medium+ effort (Pro/Enterprise also get "Sol Pro"), ChatGPT Work and Codex give Free/Go users Terra only and paid tiers a choice of Sol/Terra/Luna with adjustable effort, `max` is available to all ChatGPT Work/Codex users with GPT‑5.6 access, and `ultra` is restricted to Pro/Enterprise in ChatGPT Work and Plus+ in Codex
- **Evidence**: Direct availability breakdown in the "Availability and pricing" section.
- **Confidence**: settled (a specific, dated, checkable product/plan access matrix from the vendor)
- **Quote**: "Chat: Plus, Pro, Business, and Enterprise users access GPT‑5.6 Sol through medium and higher effort settings. Pro and Enterprise users can also select GPT‑5.6 Sol Pro for the highest-quality results on complex tasks." ... "ChatGPT Work and Codex: Free and Go users access GPT‑5.6 Terra. Plus, Pro, Business, and Enterprise users can choose among GPT‑5.6 Sol, Terra, and Luna and set an effort level for each." ... "max is available to all users with access to GPT‑5.6 in ChatGPT Work and Codex and can be toggled on in settings. In ChatGPT Work, ultra is available to Pro and Enterprise users. In Codex, it is available to Plus and higher plans."
- **Our assessment**: This is more granular plan-by-plan access detail than either existing GPT‑5.6 note captures — `blog-simonwillison-gpt56-ga-launch.md` covers pricing and spec but not this plan-tier access matrix, and `blog-openai-chatgpt-work-ambitious-partner.md` covers ChatGPT Work's own rollout timeline but not which specific model/effort combinations each plan tier unlocks. Useful as a concrete reference for any Ch03 guidance comparing what capability level is actually reachable at each subscription tier, as distinct from the model's raw benchmark ceiling.

## Concrete Artifacts

```
Source: OpenAI, "GPT‑5.6: Frontier intelligence that scales with your
ambition," https://openai.com/index/gpt-5-6 (July 9, 2026), retrieved via
Wayback Machine snapshot dated 2026-07-25 (see Extraction Notes).

Pricing (per 1M tokens) — confirmed identical to preview-stage figures in
blog-simonwillison-gpt56-sol-launch.md and GA figures in
blog-simonwillison-gpt56-ga-launch.md:
  Sol    $5.00 input  / $30.00 output
  Terra  $2.50 input  / $15.00 output
  Luna   $1.00 input  / $6.00 output
Cache writes: 1.25x uncached input rate (GPT-5.6+ only). Cache reads: 90%
cached-input discount. Explicit cache breakpoints, 30-minute minimum
cache life (unchanged from preview/GA figures already in the corpus).

Customer testimonials (model-level; NOT the ChatGPT Work product
testimonials in blog-openai-chatgpt-work-ambitious-partner.md, which cite
Zapier/RingCentral/Virgin Atlantic/NVIDIA):
  Cursor      — Oskar Schulz, President
                "one of the strongest models we've tested on CursorBench"
  Qodo        — Itamar Friedman, Co-Founder & CEO
                strongest on agentic code-review tests; ~3x fewer tokens/PR,
                ~2x lower median latency vs GPT-5.5
  Notion      — Simon Last, Co-Founder
                "most tenacious problem-solver we've seen yet"; Terra/Luna
                match GPT-5.5 performance at half cost, 16% fewer tokens
  Cognition   — Scott Wu, Co-founder & CEO
                "top-tier model that combines strong coding-agent
                performance with very strong cost efficiency"
  Rogo        — Alex Wang, Applied AI
                Big Finance Benchmark: +6.2 rubric quality, +3.6% answer
                accuracy vs GPT-5.5; with Programmatic Tool Calling, 24%
                fewer output tokens, 28% faster
  Ramp        — Ian Tracey, Software Engineer, Applied AI
                "felt less like a chat assistant and more like an
                end-to-end technical operator"
  Shopify     — Shane Moran, Senior Applied AI/ML Engineer
                followed intent better than GPT-5.5 across a multi-stage
                Codex research/plan/implement workflow
  Cisco       — Arjun Sambamoorthy, VP/CTO, AI Software and Platform
                "stays focused through long-running tasks... little
                steering"
  Clio        — Angel Faus, VP of Engineering
                legal research/document workflows: 14% fewer tokens with
                improved quality; Programmatic Tool Calling cuts prompt
                tokens 38% on multi-step document analysis, no quality loss
  Balyasny Asset Management — Alberto Da Costa, Principal Engineer,
                Applied AI
                "1.72x more token-efficient" on financial research; 88% on
                multi-hop tasks
  Basis       — Tarrek Shaban, Head of Product
                "substantial improvements on reasoning, decision making and
                autonomy" for complex accounting work

Benchmark table (reproduced as scraped from a linearized Wayback Machine
HTML snapshot — see Extraction Notes on transcription-reliability caveats;
"—" denotes no reported figure for that model in that row):

PROFESSIONAL
  Eval                                Sol      Terra    Luna     GPT-5.5   Fable5    Opus4.8   Gem3.1ProPrev  Gem3.5Flash
  Agents' Last Exam                   52.7%    50.4%    50.3%    46.9%     40.5%     45.2%     32.1%          —
  GDPval-AA v2 (Elo)                  1747.8   1593     1591.8   1493.7    1759.6    1600.1    962.3          1348.8
  Management Consulting Tasks (Int.)  43.2%    37.2%    35.4%    31.3%     35.5%     31.6%     13.2%          —
  Big Finance Bench                   53%      51%      36%      49%       —         44%       —              —
  Artificial Analysis Intel. v4.1     58.9     55       51.2     54.8      59.9      55.7      46.5           50.2

CODING
  Eval                     Sol      SolUltra  Terra    Luna     GPT-5.5   Mythos5   MythosPrev  Fable5   Opus4.8  Gem3.1ProPrev
  AA Coding Agent Idx v1.1 80       —         77.4     74.6     76.4      —         —           77.2     72.5     42.7
  SWE-Bench Pro            64.6%    —         63.4%    62.7%    59.4%     80.3%     77.8%       80%      69.2%    54.2%
  DeepSWE v1.1              72.7%    —         69.6%    67.2%    67%       —         —           69.7%    59%      11.8%
  Terminal-Bench 2.1        88.8%    91.9%     87.4%    84.7%    85.6%     88%       —           83.1%    78.9%    70.7%

SCIENCE AND HEALTH
  Eval                     Sol      Terra    Luna     GPT-5.5   Fable5    Opus4.8   Gem3.1ProPrev  Gem3.5Flash
  GeneBench Pro            28.7%    23.3%    10.8%    12%       —         16%       3.1%           8.14%
  LifeSciBench             59.9%    56%      51.2%    50.4%     —         53.6%     —              —
  MedChemBench (Internal)  48.3%    35%      30.4%    35.5%     —         —         —              —
  HealthBench Professional 60.5%    57.7%    55.7%    49.5%     60.9%     53%       —              —

COMPUTER USE
  Eval             Sol      SolUltra  Terra    Luna     GPT-5.5   Mythos5   MythosPrev  Opus4.8  Gem3.1ProPrev
  OSWorld 2.0       62.6%    —         50.2%    45.6%    47.5%     —         —           54.8%    —
  BrowseComp        90.4%    92.2%     87.5%    83.3%    84.4%     88%       87.9%       84.3%    85.9%
  BenchCAD           70.6%    —         62.3%    63.1%    44.4%     38.4%     35.5%       27.3%    —
  BenchCAD (python) 83.4%    —         78.2%    73.9%    55.8%     65%       61%         51.8%    —

CYBERSECURITY (footnote 1: cyber capabilities evaluated with reduced safeguards)
  Eval                       Sol      SolUltra  Terra    Luna     GPT-5.5   Mythos5   MythosPrev  Opus4.8
  Capture-the-Flag Challenges 96.7%    —         91.8%    85.2%    88.1%     —         —           —
  SEC-Bench Pro                71.2%    74.3%     57.7%    48.9%    45.8%     —         —           —
  ExploitBench                  73.5%    —         52.9%    33.2%    47.9%     78%       74.2%       40%
  ExploitGym                    33.7%    —         23.2%    12.4%    15.1%     —         —           —

SELF-IMPROVEMENT
  Eval                              Sol     Terra   Luna    GPT-5.5
  Internal Research Debugging Eval  68.3%   67.8%   50.8%   50%
  KernelGen 1P                      61.1%   49.2%   22.4%   29.3%
  NanoGPT                           9.69%   14.5%   1.66%   2.65%
  PostTrainBench Lite               50.3%   51.5%   29.6%   38.8%
  RSI Index                         57.9%   56.3%   41.9%   41.7%

MULTIMODAL
  Eval                     Sol     Terra   Luna    GPT-5.5  Fable5  Opus4.8  Gem3.1ProPrev
  MMMU Pro (no tools)      83%     80.7%   78.4%   81.2%    —       —        80.5%
  MMMU Pro (with tools)    84.6%   82%     79.5%   83.2%    —       —        —
  gdp.pdf                  30.7%   24.7%   22.7%   26%      29.8%   22.5%    16.7%

ACADEMIC
  Eval                        Sol    Terra   Luna    GPT-5.5  Mythos5  MythosPrev  Fable5  Opus4.8  Gem3.1ProPrev
  GPQA Diamond                94.6%  92.9%   92.3%   93.6%    94.1%    94.6%       92.6%   92%      94.3%
  FrontierMath Tier 1-3 (v2)  89%    84.9%   78.6%   85.3%    —        —           87%     80%      59.6%
  FrontierMath Tier 4 (v2)    83%    68.3%   58.5%   72.5%    —        —           87.8%   56.1%    —

TOOL USE
  Eval           Sol     Terra   Luna    GPT-5.5  Mythos5  MythosPrev  Fable5  Opus4.8  Gem3.1ProPrev  Gem3.5Flash
  AutomationBench 18.1%   15.2%   14.9%   12.9%    —        —           17.4%   15.5%    —              14.5%
  Toolathlon       58%     53.1%   53.4%   55.6%    61.7%    61.1%       61.7%   59.9%    48.8%          —

LONG CONTEXT
  Eval                              Sol     Terra   Luna    GPT-5.5  Mythos5  MythosPrev  Opus4.8
  OpenAI MRCR v2 8-needle 256-512K  91.5%   89.6%   41.3%   81.5%    —        —           —
  OpenAI MRCR v2 8-needle 512K-1M   73.8%   72.5%   41.3%   74%      —        —           —
  GraphWalks BFS 256k f1            90.7%   76.9%   81.3%   73.7%    91.1%    85.7%       85.9%
  GraphWalks BFS 1mil f1            77.1%   71.2%   51.2%   45.4%    79.4%    74.3%       68.1%

ABSTRACT REASONING
  Eval          Sol     Terra   Luna    GPT-5.5  Opus4.8  Gem3.1ProPrev
  ARC-AGI-3     7.78%   0.8%    0.18%   0.43%    1.5%     0.42%
  (footnote 8: ARC-AGI-3 for Opus 4.8 run on "high," not "max," reasoning
  effort — the only published ARC-AGI-3 result for that model)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt56-ga-launch.md` Claims 1, 3, 4, 5, 8, 10 — this
    page is the primary source Willison quoted for the GA pricing, the
    Agents' Last Exam headline figure, the SWE-Bench Pro figure, and the
    Programmatic Tool Calling description; all match character-for-character
    where directly comparable (e.g., the Agents' Last Exam prose quote and
    the SWE-Bench Pro 64.6%/80% figures are identical across both notes).
  - `blog-simonwillison-gpt56-sol-launch.md` Claims 1-6 — GA pricing,
    prompt-cache mechanics (explicit breakpoints, 30-minute TTL, 1.25x
    write / 90% read discount) are unchanged from the June 26 preview this
    note documents.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 3 — both posts,
    published the same day, independently confirm the July 9, 2026 GPT‑5.6
    GA date and the "our latest frontier model" framing.
  - `blog-openai-genebench-pro-case-studies.md` Claim 8 — the 28.7%
    GeneBench Pro score for GPT‑5.6 Sol matches exactly across two
    separately-published OpenAI sources (see Claim 12).
  - `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 4 — this
    page's individual-level Trusted Access for Cyber requirements (Claim
    10) sit alongside that note's government-level Daybreak partnerships
    as two access tiers of the same named program.
  - `blog-openai-agents-transforming-work.md` and
    `blog-openai-chatgpt-work-ambitious-partner.md` Claim 8 — Claim 11's
    internal-research-acceleration figures corroborate the broader
    "OpenAI's own engineering org has moved to near-total agentic-coding
    adoption" thesis already established in both notes, from a
    research-specific angle.
- **Contradicts**: None identified. The internal tension between different
  benchmarks favoring different vendors (Claim 4/5 vs. SWE-Bench Pro) is a
  conditioning-variable/benchmark-choice nuance already captured as such in
  `blog-simonwillison-gpt56-ga-launch.md`'s Cross-References, not a factual
  dispute between sources — no new contradiction issue filed per MINER.md
  §4a.
- **Extends**:
  - `blog-simonwillison-gpt56-ga-launch.md` Claim 9 (Multi-agent API) — see
    Claim 2 above; this source adds the `ultra` product-level setting, its
    default 4-agent (up to 16-agent) configuration, and three named
    benchmarks showing the score-latency frontier shift.
  - `blog-openai-chatgpt-work-ambitious-partner.md` Claim 13 (Auto-review,
    a model reviewing agent actions before execution) — this source's
    Claim 7 (a "reasoning monitor" reviewing conversations for potential
    harm) is a structurally similar model-reviews-model pattern applied to
    safety/misuse detection rather than task-execution governance.
- **Novel**:
  - The full 11-domain benchmark table (Claim 4, Concrete Artifacts) — no
    existing GPT‑5.6 source note in the corpus has benchmark data beyond
    Agents' Last Exam and SWE-Bench Pro (Willison's two headline figures).
  - The cybersecurity capability figures (Claim 6: ExploitBench, ExploitGym,
    SEC-Bench Pro) and the layered-safeguard architecture description with
    a named "reasoning monitor" component (Claim 7) — the first
    corpus source with this level of technical detail on an OpenAI model's
    offensive-cyber capability testing and defensive safeguard design.
  - The 700,000 A100-GPU-equivalent-hour red-teaming figure (Claim 9) — the
    first corpus quantification of pre-release automated red-teaming scale
    for any model, from any vendor.
  - The individual "Trusted Access for Cyber" hardware-passkey requirement
    and Yubico partnership (Claim 10) — extends the corpus's existing
    Daybreak/government-partnership coverage with an individual/
    organizational access tier and enforcement mechanism.
  - The plan-by-plan model/effort access matrix (Claim 14) — more granular
    than any existing GPT‑5.6 availability documentation in the corpus.
  - Eleven model-level customer testimonials (Concrete Artifacts) distinct
    from the four ChatGPT-Work-product testimonials already mined.

## Guide Impact

- **Chapter 03 (Model Selection — Benchmark Interpretation)**: Claim 5 (GPT‑5.6
  Sol beats Fable 5 on the Artificial Analysis Coding Agent Index) directly
  paired against the already-sourced SWE-Bench Pro result (Fable 5 beats Sol)
  sharpens the existing "no single benchmark picks a winner" guidance with a
  same-domain (coding) example where both vendors can point to a different
  named coding benchmark in their favor — a stronger illustration than the
  cross-domain Agents'-Last-Exam-vs-SWE-Bench-Pro pairing already in the
  corpus. Add a caveat that Claim 12's GeneBench Pro chart caption
  characterizing Fable 5 as refusing "the majority" of biology questions is
  an unaudited, vendor-sourced characterization of a competitor's behavior
  and should not be cited as evidence of Claude's dual-use-refusal calibration
  without independent verification.
- **Chapter 03 (Model Selection — Multi-Agent/Parallel Capability)**: Add
  Claim 2 (`ultra`'s 4-agent default, up to 16 agents in evals, with
  score-latency frontier data across three benchmarks) as a concrete
  example of a major vendor productizing native multi-agent orchestration
  as a user-selectable capability tier, not just an API primitive — worth
  citing alongside any Ch04 discussion of parallel-subagent patterns for
  the mechanism (trading token spend for wall-clock speed and score) it
  documents with actual benchmark evidence.
- **Chapter 03 (Verification / Safety Architecture)**: Add Claim 7's
  "reasoning monitor" pattern (a reasoning-capable model reviewing
  conversations for harm potential, layered alongside trained-in
  protections and real-time checks, explicitly contrasted with
  classifier-only architectures) as a named, vendor-documented example of
  reasoning-based safety-gate design, worth citing alongside
  `blog-openai-chatgpt-work-ambitious-partner.md`'s Auto-review pattern as
  two applications (safety vs. task governance) of the same
  model-reviews-model architectural idea.
- **Chapter 05 (Tooling/API Capabilities)**: Add Claim 14's plan-by-plan
  access matrix as a concrete reference point distinguishing a model's
  benchmark ceiling from what capability level is actually reachable at a
  given subscription tier — relevant wherever the guide compares "what can
  this model do" against "what can I actually get access to."
- No chapter should cite the ~10x-harmful-activity-blocked figure (Claim 8)
  or the 700,000-GPU-hour red-teaming figure (Claim 9) as comparable,
  standardized safety-investment metrics against any other vendor's
  safety claims — both are self-reported, unaudited, and have no disclosed
  baseline methodology.

## Extraction Notes

- **Live URL returned HTTP 403**: `https://openai.com/index/gpt-5-6`
  returned an HTTP 403 with a Cloudflare bot-challenge response
  (`cf-mitigated: challenge` header, confirmed via direct `curl` with a
  browser user-agent) to both `WebFetch` and direct `curl` — the same
  access pattern already documented for other `openai.com/index/` posts in
  `blog-openai-chatgpt-work-ambitious-partner.md` and
  `blog-openai-agents-transforming-work.md`.
- **Retrieved via Internet Archive Wayback Machine**: A snapshot dated
  2026-07-25 (crawled 16 days after publication, 2 days before this
  extraction) was fetched successfully via direct `curl`
  (`web.archive.org/web/2026/https://openai.com/index/gpt-5-6`, HTTP 200),
  then stripped of HTML tags/scripts/styles locally to produce a linearized
  plain-text transcript. All prose quotes above were checked against that
  transcript and are verbatim, including the source's non-standard
  hyphen/quote characters ("GPT‑5.6" uses U+2011 non-breaking hyphen;
  curly apostrophes/quotes preserved as scraped).
- **Benchmark table transcription is lower-confidence than the prose
  quotes**: the source renders its benchmark tables as interactive
  chart/table components; the linearized HTML scrape recovers table
  headers and cell values as flat sequential text with the table structure
  (which header applies to which value) inferred by this Miner from column
  counts and header-block boundaries, not from preserved HTML table
  markup. One partial inconsistency was found and is flagged rather than
  silently resolved: the post's prose states "GPT‑5.6 Sol sets a new high
  of 53.6" on Agents' Last Exam (matching Willison's independently-quoted
  figure in `blog-simonwillison-gpt56-ga-launch.md`), while the
  Professional-category benchmark table reconstructed here shows Sol at
  52.7% on the same-named row — a ~0.9-point discrepancy this Miner did
  not resolve (possibly different reasoning-effort settings for the prose
  headline vs. the table's default row, or a scraping/alignment artifact).
  Where a table cell and a prose quote for the same metric could be
  cross-checked (SWE-Bench Pro's Fable 5 figure, GeneBench Pro's Sol
  figure), they matched independently-sourced figures elsewhere in the
  corpus exactly, which raises confidence in the table's general
  reliability — but the Assayer should spot-check the reconstructed table
  against a rendered view of the archived page
  (`web.archive.org/web/20260725.../https://openai.com/index/gpt-5-6`)
  before treating any individual cell not otherwise cross-referenced in
  this note as fully verified.
- **No sub-pages followed**: the linked "updated GPT‑5.6 system card" was
  not fetched — it is referenced only as a pointer for further safety
  detail, not quoted from, and following it was judged lower-value than
  fully extracting the launch page itself given the page's length. The
  Agents' Last Exam and Artificial Analysis Intelligence Index benchmark
  definition pages (external, non-OpenAI) were also not followed.
- **No contradiction filed**: see Cross-References → Contradicts.
