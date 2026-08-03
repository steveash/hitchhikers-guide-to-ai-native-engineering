---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/sakana-ai-fugu-is-this-where-model-routing-should-live
source_type: blog-post
title: "Sakana AI's Fugu: Is this where model routing should live?"
author: Ben O'Mahony (Principal AI Engineer, Thoughtworks)
date_published: 2026-07-23
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: emerging
issue: "#2449"
---

# Sakana AI's Fugu: Is This Where Model Routing Should Live?

> A Thoughtworks engineer evaluates Sakana AI's Fugu (a proprietary,
> multi-model routing API) and argues its benchmark gains are real but
> uneven, and that its core design flaw isn't accuracy — it's that routing
> decisions live in an opaque platform layer above the application instead
> of inside the application team's own observable, evaluable capability
> code.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI category; byline
  piece, not a research paper or vendor announcement)
- **Author credibility**: Ben O'Mahony, Principal AI Engineer at Thoughtworks
  — already established in this corpus as the author of
  `blog-thoughtworks-omahony-feature-token-budgets.md` (token-budget
  governance patterns across named enterprise customers). This piece is an
  opinionated technical critique/review of a third-party product (Sakana
  AI's Fugu), not first-party product documentation or an empirical study;
  the author explicitly frames it as commentary on "where routing should
  live" rather than a benchmark reproduction. He discloses direct
  "platform-team" experience as the basis for his critique of platform-layer
  routing.
- **Scope**: Covers Fugu's architecture (coordinator + frontier-model pool +
  role assignment), its benchmark performance (LiveCodeBench, SWE-bench
  Pro), its pricing model, its opacity around which model handled a given
  query, and the author's argument for where routing logic should live
  architecturally (the application/capability layer, not a platform
  abstraction). Does not cover: Fugu's training methodology in depth (points
  to two ICLR 2026 papers, TRINITY and the Conductor, without summarizing
  them), pricing at scale, or any first-hand production deployment data —
  this is a review/opinion piece based on Sakana's own published benchmark
  numbers and product FAQ, not the author's own production telemetry.

## Extracted Claims

### Claim 1: Fugu is a multi-agent, dynamic model-routing system delivered behind a single OpenAI-compatible API, using a lightweight learned coordinator that assigns pooled frontier models 'Thinker', 'Worker', and 'Verifier' roles across turns
- **Evidence**: Author's architectural description of the product, presumably drawn from Sakana's own documentation/announcement (not independently verified against Sakana's source).
- **Confidence**: emerging (a third-party author's characterization of a proprietary system's architecture, not verified against Sakana's own technical documentation in this extraction)
- **Quote**: "It consists of a lightweight learned coordinator sitting behind an OpenAI-compatible endpoint, which assembles a pool of frontier models, assigns them 'Thinker', 'Worker' and 'Verifier' roles, orchestrating them across turns."
- **Our assessment**: This is a clean, novel architectural description for the corpus — a named role-based (Thinker/Worker/Verifier) multi-model orchestration pattern, distinct from the "resilience-first" framing already documented in `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` Claim 6, which describes Fugu only as coordinating "across a pool of specialized models" without naming the role structure. Together the two notes give the corpus a fuller picture of the same product from two different Thoughtworks authors.

### Claim 2: Fugu's underlying research (named "TRINITY" and "the Conductor") was presented at ICLR 2026
- **Evidence**: Author's citation of named research artifacts and a named venue; no further detail on findings is given in this article.
- **Confidence**: anecdotal (a bare citation with no methodology or results summarized; not independently verified against ICLR 2026 proceedings in this extraction)
- **Quote**: "The research behind it (TRINITY and the Conductor, both presented at ICLR 2026) is genuinely interesting but there's a question that deserves consideration: is this where model routing should live?"
- **Our assessment**: This is a lead, not a claim the guide can act on — the article does not summarize what TRINITY or the Conductor actually show. Worth flagging as a possible future source (the ICLR 2026 papers themselves) rather than citing further here.

### Claim 3: Fugu Ultra scores 93.2 on LiveCodeBench against "high 80s" for the frontier models it routes between, and edges out Opus 4.8 on SWE-bench Pro — but the base Fugu model trails Opus by ten points on that same SWE-bench Pro benchmark
- **Evidence**: Benchmark scores, presumably drawn from Sakana's own published results (not independently reproduced by the author or by this extraction).
- **Confidence**: anecdotal for the benchmark numbers themselves (vendor-published, not independently reproduced); emerging for the pattern the author draws from them (routing gains are real but inconsistent across model tiers/domains)
- **Quote**: "Fugu Ultra posts 93.2 on LiveCodeBench against high 80s for the frontier models it routes between. It edges out Opus 4.8 on SWE-bench Pro. The base Fugu model, meanwhile, trails Opus by ten points on the same benchmark."
- **Our assessment**: This is the article's central empirical hook and its most guide-relevant data point: the same routing system beats a frontier model on one tier and loses to it by ten points on another, on the identical benchmark. That single fact substantiates the article's broader argument (Claim 5) far better than an aggregate "routing works" framing would.

### Claim 4: Benchmark gains from Fugu are not evenly distributed even within a single domain — short-horizon competitive coding routes well, but longer-horizon repository work is muddier
- **Evidence**: Author's own reading of the spread between benchmark subdomains; no specific sub-scores are quoted beyond the LiveCodeBench/SWE-bench Pro figures in Claim 3.
- **Confidence**: anecdotal (author's interpretive gloss on benchmark spread, not a separately cited figure)
- **Quote**: "Even within a single domain, subdomains diverge. Short-horizon competitive coding routes beautifully, but Longer-horizon repository work gets muddier."
- **Our assessment**: A useful caveat for the guide: "routing improves benchmark scores" claims should be read at the subdomain level, not the domain level — a router can look strong in aggregate while still failing on the specific subtask (e.g., long-horizon repo work) that matters most to a given team's workload.

### Claim 5: "Routing can improve performance" is a claim that carries no operational weight — routing can also hand a task to a worse model, and the only claim that matters is whether routing improves performance on *your* tasks, which only your own evals can establish
- **Evidence**: Author's own argument, illustrated via an analogy to economist Yoram Bauman's comedic critique of "trade can make everyone better off" (Mankiw's principles of economics), and grounded in the base-Fugu SWE-bench Pro shortfall from Claim 3.
- **Confidence**: emerging (a reasoned argument directly supported by the article's own benchmark evidence, not merely rhetorical)
- **Quote**: "Yes, routing can improve performance, but routing can also hand your repository refactor to a model that's ten points worse at it, which is exactly what their own SWE-bench Pro numbers show for base Fugu... The only claim that would mean anything is 'routing significantly improves performance on tasks like yours', and nobody can make that claim except you, with your evals, on your tasks."
- **Our assessment**: This is the article's sharpest, most portable line for the guide — a general epistemic warning against vendor "routing improves performance" claims that applies well beyond Fugu specifically, to any third-party routing/orchestration product whose benchmark numbers are presented in aggregate.

### Claim 6: Unlike most semantic-routing products, which frame routing as "you don't need that expensive model" (i.e., optimize for cost), Fugu optimizes for output quality and charges a single blended rate based on the most expensive model in the pool rather than stacking per-model fees
- **Evidence**: Author's own comparative assessment of Fugu's design against the category norm, plus a description of Fugu's pricing model.
- **Confidence**: emerging (a specific, checkable design/pricing claim about a named product, though not independently verified against Sakana's pricing page in this extraction)
- **Quote**: "There's one particular thing Sakana got right. Fugu optimizes for quality, not cost... The pricing model is sensible too. There are no stacked fees, just a single blended rate based on the top model in your pool."
- **Our assessment**: This is presented by the author as the one design choice worth crediting, and it's a genuinely distinct positioning from cost-first routing products like Cursor Router (`blog-cursor-router-model-classifier.md`), which explicitly optimizes for cost reduction at matched or better quality (Claims 8-9 of that note). The corpus now has two named routing products with opposite optimization targets — useful for a guide section contrasting routing philosophies.

### Claim 7: Fugu's routing decision sits architecturally above the application, in a layer the application team neither controls nor observes — but the application team, not the platform, holds the domain context needed to route well (which actions are destructive, which subtasks tolerate a fast model, where a hard-coded answer beats any model call)
- **Evidence**: Author's own architectural argument, explicitly grounded in his stated first-hand platform-team experience ("I say this as someone with the platform-team scars to prove it").
- **Confidence**: anecdotal (an argument from professional experience and general software-architecture reasoning, not an empirical study)
- **Quote**: "Fugu moves routing above the application, into a layer the application team neither controls nor observes. The team building an agentic system holds the domain context. They know which actions are destructive, which subtasks tolerate a fast model, where a hard-coded answer beats any model call. A platform sitting one abstraction higher cannot know any of this."
- **Our assessment**: This is the article's central architectural thesis and the one the Prospector's triage comment specifically flagged as the key question to evaluate. It's a general platform-vs-application-layer argument (not Fugu-specific) that directly supports treating model routing as an application-owned "capability" rather than infrastructure — see Claim 9's Cursor Router cross-reference for a real product built on exactly this alternative principle.

### Claim 8: Fugu's own FAQ confirms that engineers cannot see which underlying model answered a given query — the routing decision is proprietary and withheld by design, and can silently change when a new frontier model is added to the pool
- **Evidence**: Author's direct citation of a specific FAQ entry in Fugu's own product documentation.
- **Confidence**: emerging (a specific, checkable claim about a named product's documented FAQ behavior — the strongest-sourced claim in the article, since it cites the vendor's own stated policy rather than the author's inference)
- **Quote**: "Can you see which underlying models Fugu used for a given query? No, you can't: the routing is proprietary and the information is withheld by design. Building on non-deterministic systems is already hard. Fugu adds a second non-deterministic layer, one you cannot inspect and governed by rules you cannot see, that can change underneath you when a new frontier model gets folded into the pool a fortnight after release."
- **Our assessment**: This is the single most guide-actionable finding in the article: a documented, vendor-confirmed opacity property (not just an inferred design flaw) of a named production routing product. For any guide section on evaluating third-party routing/orchestration vendors, "can you see and log which model handled this request, and can that change silently over time?" is now a concrete, citable due-diligence question.

### Claim 9: Modern agent frameworks (the author demonstrates Pydantic AI v2) let a team bundle model choice into the same "capability" object that holds instructions, tools, and hooks, keeping the routing decision inside the application's own trace so it can be logged, replayed, overridden, and evaluated
- **Evidence**: A working code example (~15 lines) showing a minimal capability-scoped router built with Pydantic AI v2 against local models via an OpenAI-compatible endpoint.
- **Confidence**: emerging (a concrete, runnable code example demonstrating the pattern, though the author explicitly calls his own example routing function "obviously a joke" — illustrative, not a production recommendation)
- **Quote**: "Pydantic AI v2 makes routing a property of the capability, the composable unit that bundles instructions, tools, hooks and model settings... Another advantage of this is that the decision is in your trace, which means you can log it, replay it, override it and eval it."
- **Our assessment**: This directly corroborates and extends `blog-cursor-router-model-classifier.md`, which documents a production instance of exactly this principle: Cursor Router is application/harness-layer routing (not a third-party platform sitting above the app) with two named observable quality signals ("user satisfaction," "keep rate" — Claim 7 of that note) that let the team log, evaluate, and iterate on routing decisions. Where this article argues in the abstract that routing should be observable and owned by the application layer, Cursor Router is a concrete, shipped example of that architecture at production scale — strong corroboration across two independently-authored sources.

### Claim 10: Fugu is a reasonable choice during the exploratory phase of a project (no evals yet, no clear sense of which model fits), but every serious agentic system eventually needs an orchestration layer it owns once it starts evaluating against real tasks
- **Evidence**: Author's own concluding recommendation, synthesizing the architectural critique (Claims 7-8) and the performance-variance evidence (Claims 3-5).
- **Confidence**: anecdotal (a prescriptive recommendation, not independently tested)
- **Quote**: "If you're in the exploratory phase without evals or a clear sense of which model fits, Fugu is a reasonable way to get strong answers through one endpoint. However, the moment you start evaluating a real system against real tasks, the calculus flips. Every serious agentic system ends up needing an orchestration layer it owns."
- **Our assessment**: This gives the guide a lifecycle-staged recommendation rather than a blanket "avoid third-party routing platforms" verdict — useful nuance: prototype-stage teams without eval infrastructure may reasonably reach for an opaque router like Fugu, but the article argues teams should plan to migrate routing in-house once they have evals and are optimizing a real workload.

## Concrete Artifacts

### Fugu benchmark figures (verbatim from article)
```
Fugu Ultra: 93.2 on LiveCodeBench (frontier models it routes between: "high 80s")
Fugu Ultra: edges out Opus 4.8 on SWE-bench Pro
Base Fugu: trails Opus [4.8] by ten points on SWE-bench Pro

Source: Thoughtworks Insights, "Sakana AI's Fugu: Is this where model
routing should live?", Ben O'Mahony, published July 23, 2026,
https://www.thoughtworks.com/insights/blog/generative-ai/sakana-ai-fugu-is-this-where-model-routing-should-live
```

### Minimal capability-scoped routing example (verbatim code block from article, Pydantic AI v2)
```python
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

provider = OpenAIProvider(base_url="http://localhost:1234/v1", api_key="lm-studio")
general_model = OpenAIChatModel("qwen/qwen3.6-35b-a3b", provider=provider)
coder_model = OpenAIChatModel("qwen2.5-coder-1.5b-instruct-mlx", provider=provider)

def bens_proprietary_routing_algorithm(task: str) -> OpenAIChatModel:
    return coder_model if "code" in task else general_model

agent = Agent(instructions="You are an AI assistant.")

def run(task: str) -> str:
    model_chosen = bens_proprietary_routing_algorithm(task)
    print(f"{model_chosen.model_name=}")
    return agent.run_sync(task, model=model_chosen).output

if __name__ == "__main__":
    print(run("Reply hello"))
    print(run("Explain this code: def add(x, y): return x + y"))
```
The author calls this router "obviously a joke" — it is illustrative of the
capability-scoped pattern (model choice bundled with the callable unit),
not a production routing algorithm.

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-kamelman-sovereign-ai-dependency.md`,
`blog-cursor-router-model-classifier.md`, and
`blog-thoughtworks-omahony-feature-token-budgets.md` were re-read directly
(MINER.md §4b) and the claim numbers cited above were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-cursor-router-model-classifier.md` Claims 1, 3, 7, and 9: this
    note's Claim 9 (routing as an application-owned, observable
    "capability") is directly corroborated by Cursor Router's real,
    production-scale implementation of application/harness-layer routing
    with named observability signals ("user satisfaction," "keep rate").
    Two independently-authored sources — one prescriptive, one a shipped
    product — now agree that routing decisions belong inside the
    application's own trace, not in an opaque platform layer.
  - `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` Claim 6: both
    notes independently describe Fugu as a multi-model orchestration
    product from Sakana AI; this note adds the role-based
    (Thinker/Worker/Verifier) architectural detail and the FAQ-documented
    opacity property (Claim 8) that the Kamelman note does not cover, while
    the Kamelman note covers resilience/sovereignty framing this note does
    not.

- **Contradicts**: None identified as a MINER.md §4a contradiction. This
  note's central thesis (routing should live in the application layer, not
  a platform layer — Claim 7) is in tension with the general premise of any
  routing-as-a-platform product, but no existing source note in this corpus
  stakes out the opposing position ("routing should live above the
  application") as a settled claim to be argued against — the closest
  candidate, `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` Claim
  6, treats Fugu as a credible resilience answer without taking a position
  on layering, so the two notes address different questions (resilience
  architecture vs. where routing logic should sit) rather than making
  opposing claims about the same fact.

- **Extends**:
  - `blog-thoughtworks-omahony-feature-token-budgets.md`: same author,
    different Thoughtworks piece; that note documents organizational
    token-budget governance responses to cost pressure, while this note
    extends the author's cost/routing thinking into an architectural
    critique of where model-selection logic should live. Claim 6 here (Fugu
    optimizes for quality, not cost, unlike most semantic-routing products)
    is a useful counterpoint to that note's cost-governance framing — not
    every routing product is cost-first.
  - `blog-cursor-router-model-classifier.md`: extends that note's
    documented production architecture with an independent, principled
    argument for *why* that architecture (app-owned, observable routing) is
    correct, and a contrasting cautionary example (Fugu's opacity, Claim 8)
    of what happens when routing is not app-owned.

- **Novel**:
  - **FAQ-documented model-selection opacity** (Claim 8): the first source
    in this corpus to cite a vendor's own documentation confirming that a
    routing product's model-selection decisions are unobservable by design
    and can change without notice as new models are added to the pool.
  - **Same-benchmark tier divergence** (Claim 3): the first source in this
    corpus to document a single routing product beating a frontier model on
    one benchmark and losing to it by ten points on the same benchmark,
    depending on model tier (Ultra vs. base) — concrete evidence that
    "routing improves benchmark scores" claims must be read at fine
    granularity.
  - **Quality-first (not cost-first) routing product positioning**
    (Claim 6): the corpus's first documented example of a named routing
    product explicitly optimizing for output quality rather than cost
    reduction.
  - **Capability-scoped routing code pattern** (Claim 9, Concrete
    Artifacts): a concrete, minimal code example of bundling model choice
    into an agent "capability" object (Pydantic AI v2), not previously
    present in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 7 and Claim 9 as guidance
  for where model-routing logic should live architecturally — as a
  capability the application/harness owns (with the routing decision
  visible in the trace, per Claim 9's Pydantic AI example), rather than
  delegated to an opaque third-party platform. Cite the Cursor Router
  cross-reference as a production example of this pattern already
  documented in the corpus.

- **Chapter 05 (Team Adoption)**: Add Claim 8 as a concrete due-diligence
  question teams should ask before adopting a third-party routing/model
  platform: "can we see and log which model answered a given request, and
  can that silently change over time?" Use Fugu's FAQ-confirmed "no" as the
  cautionary example.

- **Chapter 03/04 (if a benchmark-interpretation or model-evaluation
  section exists)**: Add Claim 3-5 as a caution against citing aggregate
  "routing improves performance" benchmark claims from routing-product
  vendors without checking tier/subdomain-level variance — the article's
  own SWE-bench Pro numbers (Fugu Ultra beats Opus 4.8, base Fugu trails by
  ten points) demonstrate why the aggregate framing can mislead.

## Extraction Notes

1. **Source fetched via direct HTTP, not WebFetch's AI-summarized output.**
   An initial WebFetch pass (per MINER.md §2a guidance to avoid
   paraphrased "quotes") returned only a bullet-point summary even when
   explicitly asked for verbatim text, consistent with the pattern noted in
   `blog-vercel-ai-gateway-production-index-may2026.md`'s Extraction Notes.
   This note instead retrieved the raw page HTML via a direct `curl`
   request, stripped markup with a Python script, and read the resulting
   plain text in full (`/tmp/fugu_article.txt`, 247 lines, article body
   lines 150-205). Every `Quote` field and the code block in this note are
   taken from that locally-parsed verbatim text.
2. **No sub-pages followed.** The article cites two ICLR 2026 papers by
   name (TRINITY, the Conductor) but provides no links to them, and three
   "related content" teasers at the end of the page link to unrelated
   Thoughtworks articles already out of scope for this issue. Nothing
   substantive to follow within the source itself.
3. **Benchmark figures are unverified vendor numbers.** LiveCodeBench and
   SWE-bench Pro scores are presented by the article as Sakana's own
   published results; neither the article's author nor this extraction
   independently reproduced them. This is reflected in the "anecdotal"
   evidence grade on Claim 3's benchmark-number component.
4. **No contradiction issues filed.** Cross-referenced against all
   model-routing and Fugu-related notes currently in the corpus (see
   Cross-References); found no claim here that materially opposes an
   existing note's settled claim on the same object in a way that would
   drive different guide advice — see Cross-References → Contradicts for
   the one near-miss considered and ruled out.
5. **Confidence calibration: emerging.** The article's strongest-sourced
   claim (Claim 8, the FAQ-documented opacity) and its most portable
   architectural argument (Claims 5, 7, 9) are well-grounded in either the
   vendor's own documented policy or sound general reasoning from stated
   professional experience. But the benchmark numbers underlying the
   argument (Claim 3) are unverified vendor-published figures, and several
   claims (Claims 2, 10) are bare citations or prescriptive opinion without
   independent empirical support — so the note is rated "emerging" rather
   than "settled" overall.
