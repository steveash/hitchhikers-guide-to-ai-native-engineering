---
source_url: https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case
source_type: blog-post
title: "Claude models explained: choosing the best model for your use case"
author: Anthropic
date_published: 2026-07-24
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: settled
issue: "#2219"
---

# Claude models explained: choosing the best model for your use case

> Anthropic's first-party framework for choosing among Claude model classes
> (Mythos/Fable, Opus, Sonnet, Haiku): default to the most intelligent
> available model and tune with effort level, because cost-per-task is
> often lower for capable models even at a higher price-per-token; a
> four-question checklist (task difficulty, latency, access constraints,
> unit economics); and the "advisor strategy" pattern, with one concrete
> benchmark figure (Sonnet 5 + Fable 5 advisor within 10% of Fable 5's
> SWE-bench Pro score at 63% of the price).

## Source Context

- **Type**: blog-post (official Anthropic product blog, claude.com/blog,
  "Enterprise AI / Agents / Claude Code" categories; published July 24,
  2026; ~5 minute read time)
- **Author credibility**: First-party Anthropic house post, not bylined to
  an individual — same publication pattern as other `blog-anthropic-*`
  product-advice posts in this corpus. Anthropic is the model vendor, so
  claims about its own model class positioning and pricing tradeoffs are
  a first-party, settled description of shipping products, but the
  comparative framing (e.g., "start with the most intelligent model") is
  also vendor guidance that steers usage toward higher-margin model
  classes — worth reading with that incentive in mind even where the
  underlying mechanics (fewer turns, less thinking time) are plausible.
- **Scope**: Covers the four current Claude model classes (Mythos/Fable,
  Opus, Sonnet, Haiku), a four-question model-selection framework, the
  "advisor strategy" pattern, and evals-vs-benchmarks guidance for
  choosing a model. Does NOT cover: specific pricing tables, the "Choosing
  a Claude model and effort level in Claude Code" companion doc it links
  to (not followed — it is Claude Code-specific product documentation
  rather than the general vendor framework this article documents), or
  any named customer case study. The article includes two illustrative
  (non-benchmark-plotted) curves for the effort-level/quality/cost
  tradeoff; the curves' data points could not be extracted from the
  fetched text and are not reproduced here.

## Extracted Claims

### Claim 1: Anthropic's default recommendation is to start with the most intelligent generally available model and use effort level, not model class, as the first lever to tune cost and performance
- **Evidence**: Stated directly as the article's opening thesis, immediately after framing model selection as "the most frequent questions we hear."
- **Confidence**: settled (explicit, unambiguous first-party recommendation)
- **Quote**: "But to put aside the nuance for a moment, our default recommendation is to start with the most intelligent generally available model and use effort level to dial in performance and cost."
- **Our assessment**: This reframes "which model class" and "which effort level" as two separate, ordered decisions rather than one combined choice — pick the smartest available class first, then use effort level (not a cheaper class) as the primary dial. This is a specific, actionable default that a guide chapter on model selection can state as Anthropic's official starting position, distinct from the "start cheap and move up" alternative the same article also endorses (Claim 3).

### Claim 2: Cost-per-task is often lower for more intelligent models even when their price-per-token is higher, because capable models need fewer turns and less thinking time, and starting with a smaller model makes it harder to tell model failures apart from setup failures
- **Evidence**: Direct causal explanation given immediately after the opening recommendation.
- **Confidence**: settled (stated as Anthropic's own reasoning, not attributed to a specific measurement in this article — no cost table accompanies the claim)
- **Quote**: "Cost-per-task is often lower for more intelligent models, especially at lower effort levels, even if the price-per-token is higher. This is because more capable models often take fewer turns and less thinking time to get most tasks right. Starting with a smaller model can also make it harder to distinguish between model failures and setup failures."
- **Our assessment**: The "model failures vs. setup failures" point is the most guide-useful part of this claim and is not just a cost argument — it's a debugging-methodology argument: if you start with a weak model and the task fails, you cannot tell whether the model is incapable of the task or your harness/prompt/tools are misconfigured. Starting with the strongest available model removes that confound, then downgrading (Claim 3) is a controlled experiment against a known-working baseline. This complements rather than duplicates `blog-cursor-router-model-classifier.md` Claim 1, which frames the *opposite* failure mode (users over-defaulting to one frontier "daily driver" model for routine work) — the two sources are addressing different points in the same decision, not disagreeing: this article is about where to *start* debugging a new task, Cursor's is about where routine, already-understood tasks should *settle*.

### Claim 3: Some organizations instead start with the most cost-effective model and move up model classes until quality bar is met; Anthropic documents both directional approaches
- **Evidence**: Stated as an explicit alternative to the primary recommendation in Claim 1, in the same opening section.
- **Confidence**: settled (first-party acknowledgment that its own default advice is not universal)
- **Quote**: "Some organizations may also choose to start with the most cost effective model and move up classes until the quality bar is met. We include both directional approaches in our documentation on model selection."
- **Our assessment**: Notable that Anthropic explicitly validates the bottom-up approach as legitimate rather than treating Claim 1's top-down default as the only correct method — this gives a guide chapter room to present both as valid starting points conditioned on org context (e.g., whether the task is novel/unbounded vs. a well-understood high-volume workload), rather than picking one as universally correct.

### Claim 4: The four Claude model classes are positioned as: Mythos/Fable (frontier, dual-use-gated vs. public-safe split of the same underlying model), Opus (reasoning-intensive enterprise tasks, benchmarked on GDPval-AA and Terminal-Bench 2.1), Sonnet (versatile everyday/high-volume sub-agent work), and Haiku (lowest cost, fastest, high-frequency latency-sensitive workloads)
- **Evidence**: Direct class-by-class descriptions in "The Claude model family" section. Full verbatim text for all four classes is reproduced in Concrete Artifacts below (splicing the four subsections' wording into one Quote field here would misrepresent them as a single contiguous passage, so only the most guide-relevant sentence is quoted directly in this claim).
- **Confidence**: settled (first-party description of current product lineup)
- **Quote**: "Sonnet is our versatile model class for everyday tasks. Sonnet provides a balance of performance, cost, and speed for the widest set of general purpose use cases, including high-volume sub-agents in multi-agent orchestration setups."
- **Our assessment**: The explicit call-out that Sonnet is meant for "high-volume sub-agents in multi-agent orchestration setups" is a specific, citable first-party endorsement of the orchestrator-uses-a-stronger-model / sub-agents-use-a-cheaper-model pattern already documented elsewhere in the corpus (e.g., the advisor/executor split in `blog-anthropic-computer-use-best-practices.md` Claim 11, and Cursor's task-complexity routing in `blog-cursor-router-model-classifier.md` Claim 3). It corroborates that this is Anthropic's own recommended shape for multi-agent cost management, not just a third-party optimization.

### Claim 5: The rule of thumb for choosing between Opus and Fable is to run evals first — if Opus clears the quality bar, prefer it for speed/price; if it struggles, move to Fable, since larger models like Fable tend to show more "wisdom, creativity, and writing skills" than benchmark scores alone would suggest
- **Evidence**: Direct guidance in the "Opus" section, framed as resolving the apparent overlap between the two classes.
- **Confidence**: settled as a stated decision rule; the "wisdom, creativity" distinction is emerging/qualitative — no benchmark cited to back it
- **Quote**: "The general rule of thumb is if your evals or internal testing show Opus struggling on some tasks, then Fable is the answer. If Opus already clears the quality bar, then its speed and price profile may make it the better choice."
- **Our assessment**: This is an evals-first decision rule, not a static class ranking — it defers the Opus-vs-Fable choice to the org's own test results rather than asserting one is categorically better. It's consistent with Claim 8's broader point that Anthropic recommends custom evaluations over benchmark comparison specifically because Opus and Fable's benchmark scores can be close enough that benchmarks alone don't resolve the choice.

### Claim 6: The article's model-selection framework asks four questions — task difficulty, latency needs, access constraints, and unit economics — and ties access constraints specifically to a named gated program, "Project Glasswing," that restricts Mythos availability
- **Evidence**: Direct enumeration in "How to choose which Claude model is best for your workload."
- **Confidence**: settled (first-party framework; "Project Glasswing" is a specific named program, though the article gives no further detail on its enrollment criteria)
- **Quote**: "How hard is this task? If it typically takes a lot of time, involves multiple steps, or is previously unsolved then a more capable model class is appropriate. What are the latency needs? If the model is involved in high-frequency customer facing workloads, then Sonnet is often the best choice. What are the access constraints? Mythos is only available to organizations under Project Glasswing. Not all organizations make all model classes available to all roles. What are the unit economics? Higher volumes of production may be more appropriate for lower classes of models, particularly if evaluations show those tasks are completed satisfactorily. Models are priced differently per token and will have different price-per-task costs based on their capabilities and effort level."
- **Our assessment**: "Project Glasswing" as the named gate for Mythos access is a new, specific fact for the corpus — no prior source note names this program. The task-difficulty question ("takes a lot of time, involves multiple steps, or is previously unsolved") gives concrete, checkable criteria for routing a task to a stronger model class, which is more specific and actionable than a vague "hard tasks need better models" heuristic, and maps closely onto the complexity signal Cursor Router uses for automatic routing (`blog-cursor-router-model-classifier.md` Claim 3).

### Claim 7: Effort level is presented as a second, independent axis from model class — higher-class models at higher effort give the best possible performance, but higher-class models at *lower* effort can sometimes be more cost-efficient than a smaller model class altogether
- **Evidence**: Direct statement in the "unit economics" discussion, illustrated (but not data-labeled) by two curves the article says are "illustrative and not plotted from benchmark data."
- **Confidence**: emerging (the mechanism is stated plainly, but the accompanying curves are explicitly disclosed as illustrative rather than measured, and no quantified example is given for this specific claim — the quantified example in Claim 9 is a different comparison, a cross-class advisor pattern rather than same-class effort tuning)
- **Quote**: "Effort level also impacts the balance of quality, speed, and cost. Higher-class models at higher efforts offer the best possible performance, and higher-class models at lower efforts can sometimes be more efficient than smaller models."
- **Our assessment**: This is the mechanistic backing for Claim 1's headline recommendation ("use effort level to dial in performance and cost") — it explains *why* starting with a stronger model and tuning effort down can beat starting with a weaker model outright. The explicit disclosure that the accompanying curves are illustrative, not measured, is a notable transparency marker the Assayer should be aware of: this claim should not be cited in the guide as having a quantified benchmark behind it.

### Claim 8: The "advisor strategy" — a faster, lower-cost worker model calling a more intelligent model only to check its plan and evaluate its work — improves performance substantially, with Sonnet 5 plus a Fable 5 advisor scoring within 10% of Fable 5's own SWE-bench Pro score at 63% of Fable 5's full-task price
- **Evidence**: Named pattern description plus one concrete cited benchmark comparison (SWE-bench Pro).
- **Confidence**: emerging (a single benchmark figure on one evaluation suite, first-party, no methodology detail such as how often the advisor is invoked or what "63% of the price" is measured against beyond "using Fable 5 for the whole task")
- **Quote**: "The advisor strategy allows faster, lower-cost worker models to call more intelligent models to check their plan and evaluate their work, leading to improved performance. This method, where the executor model is coached only when needed, improves performance by a substantial amount. For example, on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of the price of using Fable 5 for the whole task."
- **Our assessment**: **Extends** `blog-anthropic-computer-use-best-practices.md` Claim 11, which documents the `advisor_20260301` tool (a beta feature letting a Sonnet-based computer-use agent call Opus-level reasoning for planning "without tools and without context management") — this article generalizes the same executor/advisor split beyond computer use into a named, general-purpose strategy ("advisor strategy") and, notably, upgrades the advisor from Opus-level to Fable-level reasoning while the executor stays at Sonnet. It also supplies the first quantified cost/quality tradeoff number for the pattern in this corpus (within 10% of quality at 63% of price on SWE-bench Pro) — the computer-use source had "no performance benchmarks published" per that note's own confidence rating. Read together, the two sources show the advisor pattern moving from a beta, domain-specific tool to a named, benchmarked, general strategy across roughly the same period.

### Claim 9: Anthropic recommends custom evaluations over standard benchmarks specifically when comparing powerful models like Opus and Fable, because those models can solve nearly all questions on a standard benchmark ("saturation"), making the benchmark unable to discriminate between them
- **Evidence**: Direct explanation in "How evals and benchmarks help with model choice."
- **Confidence**: settled (a general methodological point Anthropic states as its own recommendation, consistent with public discussion of benchmark saturation elsewhere)
- **Quote**: "Benchmarks are a set of pre-determined tasks or scenarios, often for a specific domain, with known solutions. These can be helpful directional guides for evaluating capabilities across model classes and providers. The challenge arises when evaluating powerful models, such as Opus and Fable, which can solve almost all of the questions on the test (often referred to as saturation). In these cases, we recommend organizations use the models on real workloads or test them with their own evaluations to make a decision on which model is the right choice. Typically, evaluations are a curated set of problems drawn from production — including difficult tasks where your current tools fall short, with success criteria your team defines."
- **Our assessment**: This directly names the mechanism (benchmark saturation among the strongest model classes) as the *reason* custom evals matter for top-tier model selection specifically, not just as general best practice. It gives a precise definition of what "custom evaluation" should mean in this context — production-drawn problems, deliberately including cases where current tooling already fails, with team-defined success criteria — which is more specific than a generic "build evals" recommendation and can anchor a guide's eval-construction checklist.

## Concrete Artifacts

### The four-question model-selection framework (verbatim, from source)
```
How hard is this task?
  -> takes a lot of time / multiple steps / previously unsolved => more capable class

What are the latency needs?
  -> high-frequency customer-facing workloads => Sonnet often best choice

What are the access constraints?
  -> Mythos: only orgs under "Project Glasswing"
  -> not all model classes are available to all roles/orgs

What are the unit economics?
  -> high production volume => lower model classes may be appropriate,
     if evals show tasks are completed satisfactorily
  -> price-per-token differs by class; price-per-task also depends on
     effort level
```
*Source: "How to choose which Claude model is best for your workload," https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case*

### Claude model class summary (verbatim descriptions, from source)
```
Mythos  - "most capable model class, with frontier capabilities across
           domains" - especially coding, long-running agents, previously
           unsolved problems. Ships as two packages of the same model:
           Mythos (trusted orgs, dual-use cyber/bio work) / Fable
           (public, additional safeguards). Both require limited data
           retention.
Opus    - "powerful model class for reasoning-intensive enterprise
           tasks." Benchmarks: GDPval-AA (knowledge work),
           Terminal-Bench 2.1 (agentic coding).
Sonnet  - "versatile model class for everyday tasks" - balance of
           performance/cost/speed; explicitly named for high-volume
           sub-agents in multi-agent orchestration.
Haiku   - "lowest cost and fastest model class" - high-frequency,
           latency-sensitive workloads.
```
*Source: "The Claude model family" section, same URL*

### Advisor strategy benchmark figure (verbatim, from source)
```
Pattern: worker/executor model (fast, low-cost) calls a more intelligent
model as an "advisor" to check its plan and evaluate its work; advisor
is invoked only when needed (not every turn).

Measured example (SWE-bench Pro):
  Sonnet 5 + Fable 5 advisor  -> within 10% of Fable 5's own score
                               -> at 63% of the price of using Fable 5
                                  for the whole task
```
*Source: "Combining models' strengths with the advisor strategy" section, same URL*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-computer-use-best-practices.md` Claim 11 (the beta
    `advisor_20260301` tool: a Sonnet-based computer-use agent calling
    Opus-level reasoning for planning only, without tools or screen
    access) — corroborates that Anthropic has been building toward a
    general executor/advisor split; this article shows it graduating
    from a single beta tool description to a named, cross-product
    strategy with a quantified benchmark result (Claim 8).
  - `blog-simonwillison-gpt56-ga-launch.md` Claim 2 (Willison's own
    observation that "price-per-million tokens doesn't tell us much now
    that the number of reasoning tokens can differ so much between
    models for the same task") — corroborates this article's Claim 2
    (cost-per-task can be lower for pricier-per-token models) from an
    independent, non-vendor source, though Willison's point is about
    reasoning-token volume specifically while this article's point is
    about turn count and thinking time more broadly; both converge on the
    same practical takeaway — sticker price-per-token is not a reliable
    cost proxy.
  - `blog-simonwillison-afraid-of-chinese-models.md` Claim 6 ("tokens are
    not a commodity" — Thompson's argument that a token from one model is
    not fungible with a token from another, so list price-per-token
    obscures how many tokens a model actually needs to reach a correct
    answer) — same underlying point as Claim 2 here, from a third,
    independent commentator.
  - `blog-cursor-router-model-classifier.md` Claim 3 (Cursor Router's
    classifier sends "Simple work... to the most price-efficient models"
    and "more complex, long-horizon problems... to frontier reasoning
    models") and `docs-github-copilot-cca-cost-efficient-models.md`
    Claim 3 (GitHub's
    explicit task-complexity-aware CCA model guidance) — both corroborate
    this article's Claim 6 "how hard is this task?" question as a
    convergent, cross-vendor pattern: task difficulty as the primary
    routing signal for model-class selection, not just an Anthropic-
    specific framework.

- **Contradicts**: None identified. This article's default ("start with
  the most intelligent model," Claim 1) and Cursor's framing of
  single-model defaulting as a cost/quality *mismatch*
  (`blog-cursor-router-model-classifier.md` Claim 1) could look like
  opposing advice at a glance, but they are not a real contradiction —
  see the "Our assessment" note under Claim 2: this article is about
  where to start on a *new, not-yet-understood* task (use the strongest
  model to remove the model-failure/setup-failure confound), while
  Cursor's point is about *routine, already-characterized* work
  defaulting unnecessarily to frontier pricing. No contradiction issue
  filed.

- **Extends**:
  - `blog-anthropic-computer-use-best-practices.md` Claim 11 — see
    Claim 8's "Our assessment" above for the detailed extension: beta
    tool -> named general strategy, plus a first quantified benchmark
    figure for the pattern.
  - `blog-cursor-router-model-classifier.md` and
    `docs-github-copilot-cca-cost-efficient-models.md` — this article
    supplies Anthropic's own first-party version of the task-complexity
    routing question both of those sources implement in product form
    (Cursor's classifier, GitHub's CCA decision matrix), giving the
    guide a vendor-neutral statement of the same principle to cite
    alongside the product-specific implementations.

- **Novel**:
  - **"Project Glasswing"** (Claim 6) as the named program gating Mythos
    access — first appearance of this specific program name in the
    corpus (prior sources referenced "trusted organizations" for
    dual-use access without a program name).
  - **The "advisor strategy" as a named, general pattern with a
    quantified cross-class benchmark figure** (Claim 8) — the specific
    number (within 10% of quality at 63% of price on SWE-bench Pro) is
    new to the corpus.
  - **Explicit vendor guidance that starting with the strongest model
    disambiguates "model failure" from "setup failure"** (Claim 2) — a
    debugging-methodology argument for model selection that no prior
    corpus source frames this way.
  - **The four-question selection checklist itself** (Claim 6) as a
    compact, citable framework — prior corpus sources describe
    individual selection criteria (cost, latency, task complexity) but
    none package all four (difficulty / latency / access / unit
    economics) into one named checklist.

## Guide Impact

- **Chapter 02 (Model Selection Strategy)**: Add the four-question
  framework (Claim 6) as the chapter's core selection checklist, and
  Claim 1's "start with the most intelligent model, tune with effort
  level" plus Claim 3's "or start cheap and move up" as the two named
  directional approaches — presented as a choice conditioned on whether
  the task is novel/unbounded (favor top-down) or routine/high-volume
  (favor bottom-up), per Claim 2's model-failure-vs-setup-failure
  reasoning.
- **Chapter 02 or 04 (Cost Optimization)**: Add the "advisor strategy"
  (Claim 8) as a named, benchmarked pattern for the guide's cost-lever
  toolbox, cross-referenced against `blog-anthropic-computer-use-best-
  practices.md` Claim 11 to show its evolution from a single beta tool
  to a general strategy. Cite the concrete figure (within 10% of quality
  at 63% of price) as the first quantified example of this pattern in
  the corpus.
- **Chapter 04 (Cost Optimization)**: Add Claim 2 and Claim 7 (cost-per-
  task vs. price-per-token; effort level as an independent axis from
  model class) as the mechanistic explanation for why sticker
  price-per-token is not a reliable cost proxy, reinforcing the same
  point already made independently by `blog-simonwillison-gpt56-ga-launch.md` and
  `blog-simonwillison-afraid-of-chinese-models.md` — three independent
  sources (one vendor, two practitioners) now converge on this.
- **Chapter 03 (Benchmark Interpretation) or eval-construction section**:
  Add Claim 9's benchmark-saturation rationale and its specific
  definition of a custom evaluation (production-drawn problems,
  deliberately including current-tool failure cases, team-defined
  success criteria) as a concrete construction checklist, citing
  Anthropic's own stated reason for needing it (saturation among Opus/
  Fable-tier models).

## Extraction Notes

- WebFetch's default summarization pass returned only a loose paraphrase
  of the article; to get verbatim text for quoting, the page was fetched
  directly via `curl` and HTML tags stripped locally, then cross-checked
  against a second WebFetch pass. Both methods agreed on all quoted
  sentences reproduced above.
- The article links out to a companion doc, "Choosing a Claude model and
  effort level in Claude Code," and to a general "model selection"
  documentation page (referenced in Claim 3) and a "custom agent
  evaluations" best-practices post (referenced under Claim 9). Per
  MINER.md's "follow up to 5 linked pages" guidance, these were
  considered but not fetched: they are Claude Code-specific product docs
  and a separate best-practices post respectively, not sub-pages of
  *this* article's argument, and pulling them in would extraction-creep
  this note past what issue #2219 asked the Miner to mine. Recommend
  filing them as separate source-submission candidates if not already in
  the queue.
- The article includes two effort-level/cost/quality curves explicitly
  labeled "illustrative and not plotted from benchmark data." No
  numeric values could be extracted from them via the text-extraction
  method used here (they are rendered as images/charts, not table data),
  and the caption's own disclaimer means they would carry no evidentiary
  weight even if extracted — flagged in Claim 7 rather than presented as
  a data artifact.
- No contradiction with any existing source note was found; see
  Cross-References "Contradicts" above for the near-miss that was
  evaluated and ruled not a real contradiction.
