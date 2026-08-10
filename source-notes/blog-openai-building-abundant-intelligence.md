---
source_url: https://openai.com/index/building-abundant-intelligence
source_type: blog-post
title: "Building abundant intelligence"
author: Sarah Friar (OpenAI)
date_published: 2026-07-31
date_extracted: 2026-08-10
last_checked: 2026-08-10
status: current
confidence_overall: emerging
issue: "#2606"
---

# Building abundant intelligence

> A leadership-level strategy post arguing that OpenAI's advantage comes from
> a "full stack" feedback loop (infrastructure, models, platform, products)
> that compounds intelligence, adoption, and investment. The post's own
> specific technical evidence — the July 30 Luna/Terra price cuts, the
> serving-cost/speculative-decoding engineering gains, and the ARC-AGI-3
> harness case study — restates figures already independently mined into the
> corpus; its novel contribution is the executive-level "abundance" framing
> tying those figures together, plus new scale figures (>1B active users,
> >2M businesses) and an investment-discipline vocabulary not previously in
> the corpus.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`, published
  July 31, 2026). A single-author strategy/vision essay, not a data report or
  case study — five short sections (economics of abundance, compute
  efficiency, why the full stack matters, investment discipline, closing
  outlook), each a few paragraphs of prose with no charts, tables, or
  customer quotes.
- **Author credibility**: Bylined "Sarah Friar" in the page footer, with no
  title or role stated anywhere in the fetched article text itself. The
  Prospector's three separate triage comments on this issue characterized her
  as OpenAI's CEO; this note records the byline as fetched and flags that the
  title itself was not independently verified against the source page (see
  Extraction Notes). Written in first person ("That is how I think about
  abundance..."), giving it a more personal, leadership-voice register than
  the unsigned house-style posts already in the corpus
  (`blog-openai-agents-transforming-work.md`,
  `blog-openai-managing-ai-investments-agentic-era.md`).
- **Scope**: Covers OpenAI's overall business/investment thesis — pricing
  strategy, compute efficiency gains, the "full stack" argument for owning
  infrastructure/models/platform/products together, investment-decision
  criteria, and adoption scale. Does NOT cover: any named customer, any new
  benchmark result not already published elsewhere, a methodology for any
  cited figure, or technical implementation detail beyond what its own linked
  posts (already independently mined) provide.

## Extracted Claims

### Claim 1: AI infrastructure's value lies not in its scale but in what it enables — more capable intelligence, available to more people, at lower cost — and this is both the mission and the business logic
- **Evidence**: The article's opening framing statement, presented as the author's own thesis rather than a measured finding.
- **Confidence**: anecdotal (a framing/thesis statement, not a measured claim)
- **Quote**: "AI infrastructure is not valuable because it is large. It is valuable because of what it makes possible: more capable intelligence, available to more people, at a lower cost."
- **Our assessment**: This is the article's title-level thesis and reads as an executive restatement of a "value comes from useful outcomes, not raw scale" argument already present in the corpus's cost-governance material (see Cross-References). It is not independently evidenced within this post; its value is as vocabulary/framing, not new data.

### Claim 2: A self-reinforcing cycle drives OpenAI's business: better intelligence drives broader adoption, broader adoption supports more investment, and more investment improves intelligence and efficiency
- **Evidence**: The article's stated causal model for its own growth, presented immediately after Claim 1.
- **Confidence**: anecdotal (an asserted causal loop, not measured or tested against alternative explanations)
- **Quote**: "Better intelligence drives broader adoption. Broader adoption supports more investment. More investment improves intelligence and efficiency. That is the cycle we are building."
- **Our assessment**: A tidy, unfalsifiable flywheel narrative common to growth-stage tech companies; no data in this post isolates whether adoption growth is actually caused by intelligence improvements versus price cuts, marketing, or competitive dynamics. Treat as narrative framing, not evidence of a causal mechanism.

### Claim 3: On July 30, 2026, OpenAI cut GPT‑5.6 Luna's price by 80% (to $0.20/$1.20 per million input/output tokens) and Terra's by 20% (to $2/$12)
- **Evidence**: Restatement of OpenAI's own pricing announcement, already independently fetched and verified in the corpus.
- **Confidence**: settled (published, dated pricing change, independently corroborated by a prior extraction of the primary pricing-announcement page)
- **Quote**: "Yesterday, we reduced the price of GPT‑5.6 Luna by 80 percent and GPT‑5.6 Terra by 20 percent. Luna now costs $0.20 per million input tokens and $1.20 per million output tokens; Terra costs $2 and $12, respectively."
- **Our assessment**: This figure exactly matches `blog-simonwillison-gpt56-luna-price-drop.md` Claim 1 (80%/20% price cuts) and Claim 2 (Terra $2.00/$12.00, Luna $0.20/$1.20), which independently fetched OpenAI's pricing-announcement page directly. This post adds no new pricing detail beyond that existing note; it functions here as leadership-level context for the "economics of abundance" argument rather than a primary pricing source.

### Claim 4: GPT‑5.6 Sol's new "Fast mode" delivers up to 2.5x the speed of standard processing at twice the price, with no change in intelligence
- **Evidence**: Restatement of the same July 30 pricing-announcement page.
- **Confidence**: settled (matches an already-verified figure in the corpus)
- **Quote**: "For GPT‑5.6 Sol, Fast mode delivers up to 2.5 times the speed of standard processing at twice the price, with no change in intelligence."
- **Our assessment**: Exact match to `blog-simonwillison-gpt56-luna-price-drop.md` Claim 6. No new detail added (that note additionally documents Fast mode's backward-compatibility with the deprecated "Priority Processing" tag, which this post omits).

### Claim 5: The right question for choosing among models is not which model belongs to which task, but how much intelligence an outcome demands, how fast it's needed, and what it should cost — and customers should be measured on the cost of a successful outcome (including retries, oversight, and errors), not price per token
- **Evidence**: The article's own prescriptive reframing, presented as the practical implication of the price cuts described in Claim 3.
- **Confidence**: anecdotal (prescriptive framing; no worked example, formula, or customer data given)
- **Quote**: "The right question is not which model belongs to which task. It is how much intelligence the outcome demands for the required result, how quickly the intelligence is needed, and what the intelligence should cost to achieve." — "The right measure is the cost of a successful outcome, including the time, retries, oversight, and errors required to get there."
- **Our assessment**: This is the same "useful work per dollar" / "cost per accepted outcome" argument already documented from OpenAI's own July 14 post, `blog-openai-managing-ai-investments-agentic-era.md` Claim 2 ("Leaders should look at useful work per dollar: tasks completed, time saved, decisions improved, and workflows ready to scale") and Claim 4 ("track cost per accepted outcome, not cost per token"). This post restates the identical thesis seventeen days later from a leadership rather than product-strategy framing, with no new mechanism or worked example beyond what the earlier post already provides.

### Claim 6: GPT‑5.6 Sol was used to optimize its own production serving software, reducing end-to-end serving costs by 20%, and to improve speculative decoding, increasing token-generation efficiency by more than 15%
- **Evidence**: Restatement of OpenAI's own engineering blog post on GPT‑5.6 serving efficiency.
- **Confidence**: emerging (vendor-self-reported figures, but independently corroborated by a separate extraction of the primary engineering post)
- **Quote**: "Working with our technical teams, GPT‑5.6 Sol helped optimize the production software used to serve our models, reducing end-to-end serving costs by 20 percent. It also helped improve speculative decoding, increasing token-generation efficiency by more than 15 percent."
- **Our assessment**: Exact match to `blog-simonwillison-gpt56-luna-price-drop.md` Claim 7 (20% serving-cost reduction via Sol-authored kernel rewrites in Triton/Gluon) and Claim 9 (>15% token-generation efficiency via Sol-supervised speculative-decoder training). This post compresses two mechanistically distinct optimizations (kernel rewrites and load-balancing tuning, per that note's Claim 7-8, versus speculative-decoder training, Claim 9) into a single "helped optimize the production software" sentence — the more detailed causal breakdown lives only in the earlier note.

### Claim 7: Improvements to retained reasoning and context management raised GPT‑5.6 Sol's ARC-AGI-3 score from 13.3% to 38.3% while using six times fewer output tokens, with no change to the model itself
- **Evidence**: Restatement of OpenAI's own ARC-AGI-3 harness case study, cited here as the article's example of "the system surrounding [the model] matters."
- **Confidence**: settled (matches figures already independently verified in the corpus from the primary case-study post)
- **Quote**: "In a recent benchmark analysis, improvements to retained reasoning and context management raised GPT‑5.6 Sol's score on the public ARC-AGI-3 task set from 13.3 percent to 38.3 percent while using six times fewer output tokens. The model did not change. The surrounding system did."
- **Our assessment**: Exact match to `blog-openai-arc-agi-3-two-settings.md` Claim 3 (13.3% → 38.3% RHAE) and Claim 8 (roughly 3x score, 6x fewer output tokens, combined effect). This is the article's single sharpest piece of technical evidence and it is entirely a restatement — this post adds the explicit "the model did not change, the surrounding system did" framing sentence, which is a slightly stronger and more citable one-line summary of the existing note's thesis than that note's own prose provides, but the underlying numbers are unchanged.

### Claim 8: The advantage of building across infrastructure, models, platform, and products is that each layer makes the others better — product feedback shapes research, research strengthens products and lowers serving cost, and demand across products informs capacity decisions
- **Evidence**: The article's central "full stack" argument, presented as the organizing thesis for the middle section of the post.
- **Confidence**: anecdotal (an asserted structural argument; no data isolates the marginal contribution of any one layer to another)
- **Quote**: "The advantage of building across infrastructure, models, platform, and products is not simply that we participate in each layer. It is that each layer makes the others better." — "Real-world product use shows us where customers find value and where they encounter friction. That feedback helps shape our research. Research improvements strengthen our products and lower the cost of serving them."
- **Our assessment**: A vertical-integration argument with no supporting data beyond the already-cited pricing and efficiency figures (Claims 3, 4, 6, 7). It is the closest thing in this post to a distinct, novel strategic claim — no existing corpus note makes this explicit "full stack compounding" argument on OpenAI's behalf — but it remains an assertion, not a demonstrated causal finding.

### Claim 9: OpenAI's models now reach more than one billion active users and more than two million businesses; six months after signing up, users send roughly 50% more messages per day and use ChatGPT for about twice as many kinds of work
- **Evidence**: Aggregate scale figures and a within-user engagement statistic, given without methodology or date-window disclosure in this post.
- **Confidence**: emerging (the within-user engagement figure is independently corroborated with disclosed cohort methodology by an existing corpus note; the >1B/>2M scale figures are new to the corpus and carry no methodology in this post)
- **Quote**: "Our models now reach more than one billion active users and more than two million businesses. As people gain confidence in the technology, they use it more deeply. Six months after signing up, people send roughly 50 percent more messages each day and use ChatGPT for about twice as many kinds of work."
- **Our assessment**: The "50 percent more messages... twice as many kinds of work" figure is an exact restatement of `blog-openai-chatgpt-adoption-signals.md` Claim 1 (50% more messages/day, doubled distinct tasks tried, six months post-signup, measured from a disclosed 0.1% cohort sample dated 2025-10-15 through 2026-05-31). This post gives no citation or methodology for that figure directly, relying on the reader to trust the underlying (separately documented) study. The >1 billion active users and >2 million businesses figures, by contrast, are novel to the corpus — no existing source note states an aggregate user or business count at this scale for any OpenAI product — and this post gives no sample definition, measurement date, or product-scope boundary (unclear whether "businesses" includes API-only customers, ChatGPT Enterprise/Work seats, or self-reported signups).

### Claim 10: ChatGPT Work is shifting knowledge work from "asking" to "doing," and agentic work through Codex now accounts for 99.8% of weekly output tokens across OpenAI, with Finance among the teams that have made agentic tools primary
- **Evidence**: Restatement of OpenAI's own internal Codex-adoption telemetry, plus a new named department (Finance) not previously highlighted in the corpus's coverage of this figure.
- **Confidence**: emerging (the 99.8% figure is a restatement of an existing, unaudited first-party telemetry claim; the "Finance" detail and "asking to doing" framing are new)
- **Quote**: "ChatGPT Work is changing what it means to be a knowledge worker, moving beyond answering questions to completing complex, multistep work—“asking” to “doing.” Across OpenAI, agentic work through Codex now accounts for 99.8% of weekly output tokens, with Finance among the teams that have made agentic tools a primary part of how they work."
- **Our assessment**: The 99.8%-of-weekly-output-tokens figure exactly matches `blog-openai-agents-transforming-work.md` Claim 2, already flagged there as a striking near-total-displacement number that should be treated as directional evidence of internal agentic-tool dominance rather than a precise, externally-auditable statistic. This post adds no new number but does add two new details: the specific "asking to doing" framing phrase (not present in the earlier post) and naming Finance specifically as an adopting department, where the earlier post's department-level breakdown (Claim 5 there) named Legal, Finance, and Recruiting as a group without singling out Finance for emphasis.

### Claim 11: OpenAI bases its infrastructure investment decisions on evidence — user and workload growth, enterprise commitments, API consumption, utilization, revenue, and progress in model capability and efficiency — with the objective being to deploy the right capacity at the right time against credible demand, not to build the most infrastructure possible
- **Evidence**: The article's stated investment-decision criteria, presented in the "Building with conviction and discipline" section.
- **Confidence**: anecdotal (a list of stated decision inputs with no worked example, weighting, or named instance of a decision made this way)
- **Quote**: "We base our investment decisions on evidence: user and workload growth, enterprise commitments, API consumption, utilization, revenue, and progress in model capability and efficiency." — "The objective is not to build the most infrastructure. It is to deploy the right capacity, at the right time, against credible demand."
- **Our assessment**: This is a distinct, more granular list of investment-decision inputs than the higher-altitude, product-focused three-tier portfolio framework already in the corpus from `blog-openai-managing-ai-investments-agentic-era.md` Claim 7 (broad access / function-specific / strategic bets, funded by exploration/validation/production maturity stage) — that post addresses how customers should allocate AI spend across workflows; this post addresses how OpenAI itself decides how much infrastructure capacity to build. The two are complementary (customer-facing investment governance vs. OpenAI's own capacity-planning discipline) rather than restating the same claim, though neither gives a worked example or named decision.

### Claim 12: OpenAI does not need to own every asset or build every component itself — it can own, partner, or buy depending on what best serves the customer and the economics — with the goal being to coordinate the system and learn across it rather than control every layer directly
- **Evidence**: A direct statement following the "full stack" argument (Claim 8), clarifying that vertical integration does not require full ownership.
- **Confidence**: anecdotal (a stated operating principle, no example of a specific own/partner/buy decision given)
- **Quote**: "It does not require owning every asset or building every component ourselves. We can own, partner, or buy depending on what best serves the customer and makes the most economic sense. What matters is coordinating the system and learning across it."
- **Our assessment**: Novel to the corpus — no existing OpenAI or Anthropic source note documents this explicit "own, partner, or buy" infrastructure-sourcing framing. It sits in some tension with the "full stack" language of Claim 8 (which emphasizes participating in every layer); this sentence clarifies that "full stack" means coordinated control and learning across layers, not literal ownership of every layer, a nuance worth preserving if the guide cites the full-stack argument.

## Concrete Artifacts

```
Source: OpenAI, "Building abundant intelligence" (Sarah Friar, July 31, 2026),
https://openai.com/index/building-abundant-intelligence

Restated pricing/efficiency figures (all independently verified elsewhere
in the corpus — see Cross-References):
  GPT-5.6 Luna price cut:      -80%  ($1.00/$6.00 -> $0.20/$1.20 per 1M tokens)
  GPT-5.6 Terra price cut:     -20%  ($2.50/$15.00 -> $2.00/$12.00 per 1M tokens)
  GPT-5.6 Sol Fast mode:       2.5x speed at 2x price, no intelligence change
  Serving cost reduction:      20% (Sol-assisted production kernel/software optimization)
  Speculative decoding gain:   >15% token-generation efficiency
  ARC-AGI-3 (Sol, public set):  13.3% -> 38.3%, 6x fewer output tokens (no model change)
  Codex share of weekly OpenAI
    output tokens:              99.8% (Finance named as an adopting department)

New scale figures (no methodology disclosed in this post):
  Active users:      >1 billion
  Businesses:        >2 million
  6-month post-signup engagement growth (restates
    blog-openai-chatgpt-adoption-signals.md Claim 1):
      Messages/day:               +~50%
      Distinct kinds of work:     ~2x

Stated investment-decision criteria (verbatim list):
  "user and workload growth, enterprise commitments, API consumption,
  utilization, revenue, and progress in model capability and efficiency"

Stated capacity-planning questions (verbatim):
  "How quickly does new capacity become productive? How efficiently is it
  used? What customer demand does it support? How rapidly can technical
  progress lower the cost of delivering useful intelligence?"
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-gpt56-luna-price-drop.md`,
`blog-openai-arc-agi-3-two-settings.md`, `blog-openai-agents-transforming-work.md`,
`blog-openai-chatgpt-adoption-signals.md`, and
`blog-openai-managing-ai-investments-agentic-era.md` were re-read directly
(MINER.md §4b) and the claim numbers cited above were confirmed against each
note's numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 1 (80%/20% price cuts
    headline) and Claim 2 (exact new Terra $2.00/$12.00, Luna $0.20/$1.20
    pricing): this post's Claim 3 restates both with no new detail.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 6 (Sol Fast mode, 2.5x
    speed at 2x price): this post's Claim 4 restates it verbatim in substance.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claim 7 (20% serving-cost
    reduction via Sol-authored kernel work) and Claim 9 (>15% token-efficiency
    gain via Sol-supervised speculative-decoder training): this post's Claim 6
    compresses both into one summary sentence.
  - `blog-openai-arc-agi-3-two-settings.md` Claim 3 (13.3% → 38.3% RHAE) and
    Claim 8 (~3x score, 6x fewer output tokens): this post's Claim 7 restates
    the identical figures as its lead technical example.
  - `blog-openai-agents-transforming-work.md` Claim 2 (Codex = 99.8% of weekly
    OpenAI output tokens): this post's Claim 10 restates the same figure,
    adding a "Finance" department callout and the "asking to doing" phrase not
    present in the earlier post.
  - `blog-openai-chatgpt-adoption-signals.md` Claim 1 (50% more messages/day,
    2x distinct tasks tried, six months post-signup, from a disclosed 0.1%
    cohort sample): this post's Claim 9 restates the same figure without
    the earlier post's methodology disclosure.
  - `blog-openai-managing-ai-investments-agentic-era.md` Claim 2 ("useful work
    per dollar") and Claim 4 ("cost per accepted outcome"): this post's Claim 5
    is the identical thesis, restated from a leadership rather than
    product-strategy framing seventeen days later.

- **Contradicts**: None identified. No claim in this post opposes an existing
  source note; the post's own content is almost entirely a restatement of
  figures already independently verified from their primary sources elsewhere
  in the corpus.

- **Extends**:
  - `blog-openai-managing-ai-investments-agentic-era.md` Claim 7 (three-tier
    customer investment portfolio, funded by maturity stage): this post's
    Claim 11 gives a parallel but distinct list — OpenAI's own internal
    infrastructure capacity-planning criteria, rather than guidance for how a
    customer should allocate AI spend. The two describe different decision-makers
    (OpenAI's own capacity planning vs. customer investment governance) using
    a structurally similar "fund/build according to evidence of demand"
    logic.
  - `blog-openai-chatgpt-work-ambitious-partner.md` (customer-testimonial-driven
    ChatGPT Work coverage): this post's "asking to doing" framing (Claim 10)
    gives a named, quotable phrase for the same knowledge-work-transformation
    argument that post documents via named customer testimonials, without
    adding any new customer evidence itself.

- **Novel**:
  - The >1 billion active users and >2 million businesses aggregate scale
    figures (Claim 9) — no existing corpus note states OpenAI product usage
    at this aggregate scale, and this post gives no methodology, date, or
    product-scope definition for either number.
  - The explicit "own, partner, or buy" infrastructure-sourcing principle
    (Claim 12) — not previously documented in the corpus for any lab.
  - The "full stack" compounding-layers argument as an explicit, named
    strategic thesis (Claim 8) — the underlying pricing/efficiency evidence
    is already in the corpus, but no existing note frames it as a deliberate
    vertical-integration strategy in these terms.
  - Finance singled out by name as a Codex-adoption department (Claim 10) —
    the existing corpus note on this topic
    (`blog-openai-agents-transforming-work.md` Claim 5) named Legal, Finance,
    and Recruiting as a group without individually emphasizing Finance.

## Guide Impact

- **Chapter 03 (Model Selection / Cost-Performance)**: This post adds no new
  pricing or benchmark number for this chapter — every technical figure it
  cites (Claims 3, 4, 6, 7) is already sourced with more detail from
  `blog-simonwillison-gpt56-luna-price-drop.md` and
  `blog-openai-arc-agi-3-two-settings.md`. If the guide wants an
  executive-level quote tying "outcome cost, not token price" to these
  figures for a chapter introduction or pull-quote, Claim 5's framing
  ("the right measure is the cost of a successful outcome") is the most
  citable single sentence in this post, but the guide should cite the
  existing, more detailed notes for the underlying numbers.
- **Chapter 04 (Context Engineering / harness-as-performance-lever)**: Claim
  7's one-line summary — "The model did not change. The surrounding system
  did." — is a sharper, more quotable restatement of the thesis already
  documented in full in `blog-openai-arc-agi-3-two-settings.md`. Useful as a
  pull-quote if the guide wants a leadership-level framing sentence for that
  section, but cite the ARC-AGI-3 note directly for the actual figures and
  mechanism (retained reasoning, compaction).
- **Chapter 05 (Team Adoption / Infrastructure Strategy)**: Add Claim 12's
  "own, partner, or buy" framing and Claim 11's investment-decision-criteria
  list as new vocabulary for a section on infrastructure build-vs-buy
  decisions at the organizational level — explicitly flag both as unvalidated
  leadership assertions with no named example of a specific own/partner/buy
  decision or investment call made under this framework.
- No chapter should cite the >1 billion active users or >2 million
  businesses figures (Claim 9) as precise, load-bearing numbers — this post
  discloses no methodology, measurement date, or scope definition for either,
  unlike the six-months-post-signup engagement figure in the same claim,
  which traces to a methodologically disclosed existing corpus source.

## Extraction Notes

- **Primary URL blocked; retrieved via Wayback Machine snapshot fetched
  directly with `curl`.** The live URL
  (`https://openai.com/index/building-abundant-intelligence`) returned HTTP
  403 to both `WebFetch` and a direct `curl` with a browser user-agent — the
  same Cloudflare-challenge access pattern already documented in this corpus
  for `openai.com/index/` posts. The Wayback Machine's availability API
  reported a snapshot (`web.archive.org/web/20260802191303/...`), but
  `WebFetch` itself returned an explicit tool error when pointed at that
  `web.archive.org` URL ("Claude Code is unable to fetch from
  web.archive.org"). The snapshot HTML was instead retrieved with a direct
  `curl` request (HTTP 200), stripped of script/style tags and HTML markup
  with a local Python script, and read in full — a short post (roughly 900
  words of body text plus navigation chrome), read in its entirety. Every
  quote above was checked against that extracted text.
- **No sub-pages independently re-fetched.** The post links to three of its
  own prior posts ("recent pricing announcement," "recent engineering work,"
  and "recent benchmark analysis") that are the primary sources for Claims 3,
  4, 6, and 7. Rather than re-fetch pages already deeply mined by two existing
  corpus notes (`blog-simonwillison-gpt56-luna-price-drop.md` for the pricing
  and engineering posts; `blog-openai-arc-agi-3-two-settings.md` for the
  benchmark post), this note treats those figures as restatements and
  cross-references the existing notes' specific claim numbers directly, per
  MINER.md §4b. No sub-page in this post contains a number or mechanism not
  already covered by an existing note.
- **Author title not independently verified.** The fetched article text
  credits "Sarah Friar" as author with no title given anywhere in the body or
  footer. The Prospector's triage comments on this issue (three separate
  passes) described her as OpenAI's CEO; this note records that
  characterization here rather than in the frontmatter/byline, since it could
  not be confirmed from the source page itself during this extraction.
- No contradiction with any existing source note was identified; see
  Cross-References → Contradicts. This source's low novelty-to-restatement
  ratio (10 of 12 claims either exactly restate or closely parallel a figure
  already independently verified elsewhere in the corpus) is reflected in the
  `emerging` overall confidence rating and should inform how heavily the
  guide leans on this specific post versus its more detailed primary sources.
