---
source_url: https://cognition.com/blog/local-fusion
source_type: blog-post
title: "Introducing Fusion in Devin Desktop & CLI"
author: The Cognition Team
date_published: 2026-09-11
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: emerging
issue: "#3408"
---

# Introducing Fusion in Devin Desktop & CLI

> Cognition brings its "Fusion" lead/sidekick multi-model harness (previously
> cloud-only, see `blog-cognition-devin-fusion.md`) to Devin Desktop and CLI,
> pairing newer models — Fable 5.1 or GPT-6 Astra as lead, Cognition's own
> SWE-2 as sidekick — and, for the first time, backs its cost-savings claims
> with third-party benchmarking (Artificial Analysis, Vals AI) rather than
> only its own FrontierCode numbers. Reports up to 39% lower cost than a
> single-model harness at near-frontier scores, and adds concrete, per-pairing
> harness-tuning guidance (brief detail level, sidekick pushback permission,
> exploration-delegation boundaries) not present in the June launch post.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com/blog/local-fusion,
  anonymous corporate byline consistent with this corpus's other Cognition
  product-announcement posts, e.g. `blog-cognition-devin-fusion.md`,
  `blog-cognition-devin-desktop.md`). Byline date rendered "09.11.26" in the
  page's own MM.DD.YY convention. This is a product-availability announcement
  (Fusion moving from Devin Cloud preview to local Desktop/CLI), not a
  practitioner essay.
- **Author credibility**: First-party vendor content from Cognition, maker of
  Devin, with a direct commercial interest in Fusion appearing efficient and
  high-quality. Unlike the June launch post (which benchmarked Fusion only on
  its own FrontierCode benchmark), this post states it "partnered with
  Artificial Analysis and Vals AI to evaluate Fusion" across five named
  benchmarks (DeepSWE 1.1, Terminal-Bench 4, SWE-Atlas QnA, Vals Code
  Migration, FrontierCode 1.1 Extended) — third-party-run evaluation, though
  the post itself doesn't disclose the third parties' methodology, sample
  sizes, or whether Cognition had any input into the task selection.
- **Scope**: Covers the CLI/Desktop rollout of Fusion, a joint benchmark
  comparison against Claude Code and Codex on the Artificial Analysis Coding
  Agent Index and four other benchmarks, a restatement of the underlying
  two-agent architecture (lead + sidekick, persistent independent contexts,
  brief/result/feedback-only exchange), FrontierCode turn-phase distribution
  data, a "price per task, not per token" cost-efficiency argument with a
  Fable-5-vs-Opus-4.8-as-lead comparison and a sidekick-model cost/quality
  coupling table, and three concrete per-pairing harness-tuning levers. Does
  **not** cover: the classifier or routing logic from the original Fusion
  post (this post doesn't mention dynamic mid-session routing at all), the
  5-minute prompt-cache TTL constraint disclosed in the June post, sample
  sizes/methodology for the Artificial Analysis/Vals AI benchmarks, or how
  "up to 39%" was chosen as the headline number when the benchmark table
  shows the FrontierCode Extended savings for Astra+SWE-2 at only −11%.

## Extracted Claims

### Claim 1: Fusion is Cognition's efficiency headline claim for the local rollout — "up to 39% more efficient" than single-model harnesses on major coding benchmarks, backed by an Artificial Analysis Coding Agent Index v1.5 comparison against Claude Code and Codex
- **Evidence**: Opening paragraph and hero chart with named data points for
  each configuration's score and cost.
- **Confidence**: emerging (specific, quantified vendor claim, benchmarked on
  a named third-party index; the "up to" framing picks the single best
  number from a range that varies by benchmark — see Claim 3)
- **Quote**: "Fusion is the most efficient frontier harness for Fable and Astra, up to 39% more efficient compared to other model harnesses across major coding benchmarks. Today, we're making it available in Devin Desktop and CLI."
- **Our assessment**: This is the direct answer to the first and third triage
  comments' key question about updated model pairings and cost benchmarks:
  the headline number (39%) comes specifically from the Astra+SWE-2 vs.
  Codex comparison, not from Fable 5.1+SWE-2 vs. Claude Code (36%) — the
  post picks the larger of its two headline figures to lead with, which is
  ordinary marketing framing but worth flagging so the guide doesn't cite
  "39%" as if it applied uniformly across both model pairings.

### Claim 2: For best results, Cognition recommends pairing Fable 5.1 as the lead with SWE-2 as the sidekick
- **Evidence**: Direct recommendation immediately following the
  lead/sidekick role explanation.
- **Confidence**: emerging (a direct vendor recommendation, not independently
  validated, though consistent with the benchmark table's generally stronger
  Fable-5.1-paired results)
- **Quote**: "When selecting Fusion, you pick two models instead of one. Pick a frontier model for planning and review (the "lead"), and a cost-effective model for execution (the "sidekick"). For best results, we recommend pairing Fable 5.1 with SWE-2."
- **Our assessment**: This is new, actionable guidance absent from the June
  post (which didn't name a specific recommended pairing, since Fable 5 was
  under a since-lifted access suspension at the time — see
  `blog-cognition-devin-fusion.md` Claim 10). SWE-2 itself (Cognition's own
  sidekick model) is not otherwise documented anywhere in this corpus; this
  post is the first source establishing it as Cognition's current
  recommended default sidekick.

### Claim 3: A five-benchmark, third-party-partnered comparison (Artificial Analysis, Vals AI) of Fusion vs. single-model baselines shows cost reductions ranging from −11% to −46% with scores usually close to, and sometimes exceeding, the single-model baseline
- **Evidence**: A results table with five benchmarks, each showing baseline
  model score/cost and Fusion-pair score/cost with percentage cost delta.
- **Confidence**: emerging (specific, third-party-partnered, per-benchmark
  quantified data — a meaningfully more rigorous evidentiary base than the
  June post's FrontierCode-only, self-benchmarked headline numbers)
- **Quote**: "We partnered with Artificial Analysis and Vals AI to evaluate Fusion with Fable 5.1 and GPT-6 Astra with SWE-2 as the sidekick across several coding agent benchmarks. Devin Fusion saves significant costs across the board while maintaining frontier performance."
- **Our assessment**: The range is wide and pairing-dependent — Astra+SWE-2
  on FrontierCode 1.1 Extended saves only 11% (63.1 vs 63.4 score, almost a
  wash) versus 46% on DeepSWE 1.1 for Fable 5.1+SWE-2 — which undercuts the
  "up to 39%" headline as a representative figure and argues the guide
  should present this as "cost savings vary substantially by benchmark and
  pairing, from roughly 11% to 46%" rather than citing a single number.
  Notably this is the first Cognition Fusion post to use independent
  third-party benchmark operators rather than exclusively its own
  FrontierCode, partially addressing this corpus's standing "no independent
  replication" caveat on `blog-cognition-devin-fusion.md`'s claims — though
  only partially, since the post still doesn't disclose the third parties'
  methodology or whether Cognition had any role in task/prompt selection.

### Claim 4: Model routing is framed as insufficient because the initial prompt doesn't reveal task difficulty, and switching models mid-task breaks the prompt cache — incurring cost and defeating the purpose of routing
- **Evidence**: Direct explanatory passage under "Model routing is not
  enough," paired with FrontierCode turn-phase distribution data showing
  agents spend most turns on Setup (34%) and Plan (32%), not Implementation
  (only 5%).
- **Confidence**: emerging (a stated engineering rationale, illustrated with
  specific first-party turn-distribution data, not independently verified)
- **Quote**: "But the initial prompt isn't enough to know the difficulty of the task. "Fix xyz bug" could be a one-line edge case or could require rearchitecting your entire product; you can't know until you've actually investigated the code. Additionally, you break prompt caches by switching models mid-task, incurring $$$ for frontier models and defeating the purpose of routing."
- **Our assessment**: This restates and sharpens the cache-miss argument
  already present in the June post's Claim 3 (routing/consult-tool patterns
  like Smart Friend and Anthropic's Advisor pay a cache-miss cost per query)
  but generalizes it specifically to *any* mid-task model switch, not just
  per-call consult tools — a stronger, more general claim: this post
  implies that even a well-designed router that swaps models based on
  observed difficulty (not just a consult call) still pays the cache-miss
  tax, which is the specific problem Fusion's parallel-persistent-context
  design is built to avoid entirely by never switching the model mid-task
  for either agent.

### Claim 5: The Fusion architecture runs two parallel agents (lead + sidekick) that maintain separate persistent contexts and exchange only briefs, results, and feedback — not full conversation histories — so each agent independently maximizes prompt caching
- **Evidence**: Direct architecture description under "The Fusion
  architecture," restating the June post's core design with the same
  terminology (lead/sidekick, replacing June's "main agent"/"sidekick").
- **Confidence**: emerging (restated first-party architecture description;
  no new mechanism detail beyond the June post)
- **Quote**: "Instead of passing entire conversations between models, the lead and sidekick only exchange briefs, results, and feedback. The sidekick doesn't need the lead's entire history to implement a change, and the lead doesn't need every intermediate tool result to review the work. Each agent builds its own persistent context, taking full advantage of prompt caching."
- **Our assessment**: This is a corroborating restatement, not new
  information, of `blog-cognition-devin-fusion.md` Claim 2's architecture
  description — worth recording because it confirms the architecture is
  unchanged between the cloud-preview (June) and local (September) releases,
  which is itself useful: the cost/benchmark improvements in this post come
  from model-pairing and tuning changes, not an architecture revision.

### Claim 6: The lead model always stays in charge — it reviews the sidekick's work, identifies problems, and can take back control when the sidekick is out of its depth — and the user always interfaces with the frontier-tier lead model rather than the cheaper sidekick
- **Evidence**: Direct statement under "The Fusion architecture," giving the
  rationale for keeping a frontier model in the user-facing role.
- **Confidence**: emerging (first-party design rationale, not independently
  tested)
- **Quote**: "The Fusion architecture ensures that frontier intelligence is always in charge. We don't assign tasks to a cheaper model hoping that the routing decision was correct. The lead always reviews the work, identifies problems, and can take control back when the sidekick is out of its depth." / "Additionally, since the lead model is in charge of the session, the user always interfaces with frontier intelligence for the best user experience. Many smaller models are becoming more capable, but are still less polished as user-facing agents."
- **Our assessment**: This is a specific, transferable design rule for
  cost-optimized multi-model harnesses: reserve the frontier model for the
  user-facing surface and final quality gate, even when most execution work
  is delegated — the guide should distinguish this from routing patterns
  where a cheap model may be the one the user directly sees and interacts
  with for "easy" tasks.

### Claim 7: Cost and model intelligence are described as coupled rather than independent — more expensive models can make the whole system cheaper, because frontier models are increasingly token-efficient and create less back-and-forth; Cognition argues 2026-era model/harness combos should be evaluated on price per task, not price per token
- **Evidence**: Direct argument under "More expensive models can make Fusion
  cheaper," illustrated with a specific Fable-5-vs-Opus-4.8-as-lead
  comparison and a sidekick cost table (Claim 8).
- **Confidence**: emerging (a specific, named comparative result plus a
  general framing argument; single comparison, not a systematic study)
- **Quote**: "One of our key findings is that using more expensive models can make the entire system cheaper. This applies to both the lead and the sidekick. Price per token is only part of the equation, because frontier models are increasingly more token efficient, and also more efficient in how much back-and-forth work the lead and the sidekick create for each other. In 2026, models (and model-harness combos) should be evaluated on price per task rather than price per token."
- **Quote (lead comparison)**: "We saw this when we replaced Opus 4.8 with Fable 5 as the lead. Fable nominally costs twice as much per token. But with the same sidekick, Fable-led sessions cost 9% less on average, while scoring higher on FrontierCode. Fable delegated earlier and gave better briefs, while Opus micromanaged the sidekick and redid much of its work."
- **Our assessment**: This is a specific, transferable finding — a leaner
  articulation of the same "cost-per-task, not cost-per-token" argument
  already present in `blog-anthropic-choosing-claude-model.md` Claim 2, now
  applied specifically to the *lead* role in a two-agent harness rather than
  to single-model selection: a lead model's *delegation quality* (giving
  better upfront briefs, needing fewer correction rounds) is framed as the
  mechanism by which a pricier lead lowers total system cost, not merely
  raw per-token efficiency.

### Claim 8: Sidekick model choice shows the same cost/intelligence coupling — a stronger, pricier sidekick (SWE-2, $0.75/Mtok) barely raises overall session cost versus a much cheaper one (GPT-5.6 Luna, $0.20/Mtok, a 275% price gap) because it needs fewer attempts and creates less review/correction work for the lead
- **Evidence**: A named sidekick-comparison table (Astra-high lead, both
  sidekicks, on FrontierCode) plus explanatory bullets.
- **Confidence**: emerging (a single named comparison table; no disclosed
  sample size or task count underlying the two data points)
- **Quote**: "The same principle applies to the sidekick. Using a stronger model like SWE-2 instead of a smaller model like GPT-5.6 Luna doesn't substantially increase overall cost." / "Stronger sidekicks tend to be more turn and token efficient. A lower price per token is less useful if the model needs more attempts to get the implementation right." / "A stronger sidekick also makes the lead cheaper. Its work needs less review and correction rounds. Every mistake a stronger sidekick avoids can save the frontier model rounds of reasoning."
- **Our assessment**: The table result is striking: despite SWE-2 costing
  275% more per token than GPT-5.6 Luna, the Astra-led Fusion session with
  SWE-2 actually scored higher (63.4 vs 62.0) *and* cost slightly less
  ($2.34 vs $2.39, a 2% decrease) than the Luna-sidekick session — a
  concrete, quantified counterexample to picking a sidekick purely on
  per-token price. This is a novel, specific data point extending Claim 7's
  general argument to the sidekick side of the pairing, which the June post
  did not address at all (it discussed only lead-model cost/intelligence
  tradeoffs).

### Claim 9: Harness tuning must vary by model pairing along at least three named axes: how much detail the lead's brief should contain, whether the sidekick is permitted to push back on instructions, and how much exploratory work is delegated to the sidekick — with the last one still an active area of research
- **Evidence**: Three enumerated, explicitly reasoned tuning questions under
  "Tuning the harness for different model pairings."
- **Confidence**: emerging (specific, named tuning levers with stated
  rationale; framed as ongoing practice/research, not a settled
  methodology)
- **Quote**: "How much detail should the lead provide? Paired with a weaker sidekick, Fable 5.1 needs to provide more prescriptive briefs. We incur more lead tokens upfront, but avoid extra review rounds later. With SWE-2 as the sidekick, Fable can leave more implementation details for the sidekick to figure out." / "Should the sidekick be allowed to push back? ...With stronger sidekicks, encouraging pushback can help catch mistakes in the lead's plan. Allowing weaker sidekicks to be opinionated ends up hurting overall performance and cost." / "What exploration should be delegated? We find that exploration needed for planning should not be delegated to a weaker sidekick, as it shapes the lead's plan... Tuning this boundary remains an active area of our research."
- **Our assessment**: This is the most operationally concrete, novel content
  in the post — the June launch post described the architecture and
  aggregate results but gave no guidance on *how* to configure a
  lead/sidekick pairing differently depending on sidekick strength. This
  directly answers the second and third triage comments' request for
  "model pairing tuning" specifics: a team adopting a similar pattern should
  expect to re-tune brief verbosity, pushback permissions, and exploration
  scope for each new model pairing rather than assuming one harness
  configuration works uniformly.

### Claim 10: Fusion is now available to try locally via a single-command Devin CLI install, extending a pattern Cognition says has performed well on Devin Cloud "over the past few months"
- **Evidence**: Direct installation instructions and closing framing.
- **Confidence**: settled (a verifiable, concrete distribution fact — the
  install command itself — combined with an anecdotal, undisclosed-metric
  claim about Devin Cloud performance)
- **Quote**: "You can try it for yourself by installing Devin CLI: `curl -fsSL https://cli.devin.ai/install.sh | bash`" / "We have seen great results with Fusion on Devin Cloud over the past few months, and we are excited to bring it to your machine."
- **Our assessment**: This is the operational core of the "local" framing in
  this post's title and URL slug: Fusion was previously available only via
  the Devin Cloud web preview described in `blog-cognition-devin-fusion.md`;
  this post's primary news, beyond the new model pairings and benchmarks, is
  that the same harness now ships in Devin CLI and Desktop. The "great
  results... over the past few months" claim is undisclosed-metric and
  should be treated as marketing framing rather than evidence.

## Concrete Artifacts

### Headline Artificial Analysis Coding Agent Index v1.5 comparison
```
Source: cognition.com/blog/local-fusion, hero chart

Claude Code, Fable 5.1 (max):        score 62.2, cost $12.36
Devin Fusion, Fable 5.1 + SWE-2:     score 61.7, cost $7.90   (36% lower cost than Claude Code)
Codex, Astra (max):                  score 61.6, cost $7.47
Devin Fusion, Astra + SWE-2:         score 58.9, cost $4.54   (39% lower cost than Codex)
Claude Code, Opus 5 (max):           score 60.0
Muse Code, Muse Spark 1.3 (max):     score 54.0
Opencode, GLM-5.3:                   score 54.0
Kimi Code CLI, Kimi K3:              score 52.0
Grok Build, Grok 4.6 (xhigh):        score 47.0
Claude Code, Qwen3.8 Max:            score 43.0
Codex, DeepSeek V4:                  score 43.0
Antigravity SDK, Gemini 3.8 Flash:   score 42.0
```

### Five-benchmark third-party-partnered comparison table
```
Source: cognition.com/blog/local-fusion, "Savings across benchmarks"
(partnered with Artificial Analysis and Vals AI); format is score @ cost,
with Fusion columns showing % cost change vs. the matching single-model column

Benchmark                    | Fable 5.1        | Fusion (Fable 5.1+SWE-2) | Astra           | Fusion (Astra+SWE-2)
DeepSWE 1.1                  | 64.3 @ $14.63     | 63.1 @ $7.88  (-46%)      | 67.6 @ $7.88     | 67.3 @ $4.69  (-40%)
Terminal-Bench 4             | 57.6 @ $17.46     | 56.1 @ $13.37 (-23%)      | 55.6 @ $10.08    | 50.0 @ $6.06  (-40%)
SWE-Atlas QnA                | 64.8 @ $7.57      | 65.9 @ $5.00  (-34%)      | 61.8 @ $5.72     | 59.4 @ $3.59  (-37%)
Vals Code Migration          | 54.6 @ $70.97     | 57.3 @ $42.00 (-41%)      | 67.7 @ $44.36    | 61.3 @ $35.51 (-20%)
FrontierCode 1.1 (Extended)  | 63.6 @ $2.68      | 63.5 @ $1.67  (-38%)      | 63.1 @ $2.62     | 63.4 @ $2.34  (-11%)
```

### FrontierCode turn-phase distribution ("Where an agent spends its turns")
```
Source: cognition.com/blog/local-fusion, "Model routing is not enough"

Plan:           32%
Setup:          34%
Implementation:  5%
Debug:          17%
Validate:        9%
(Closeout: remaining, unlabeled percentage in source)
```

### Sidekick cost/quality coupling table
```
Source: cognition.com/blog/local-fusion, "More expensive models can make
Fusion cheaper" (Astra "high" as lead, FrontierCode)

Sidekick             | List price      | Astra (high) Fusion, FrontierCode
GPT-5.6 Luna (high)  | $0.20/Mtok      | 62.0 @ $2.39
SWE-2 (medium)       | $0.75/Mtok (+275%) | 63.4 @ $2.34 (-2%)
```

### Local install command
```
Source: cognition.com/blog/local-fusion

curl -fsSL https://cli.devin.ai/install.sh | bash
```

## Cross-References

- **Extends**:
  - `blog-cognition-devin-fusion.md` (the June 29, 2026 Fusion launch,
    cloud-preview-only): this post is the direct sequel, bringing the same
    lead/sidekick architecture (Claim 5, restating that source's Claim 2) to
    Devin CLI and Desktop (Claim 10), with newer model pairings (Fable 5.1
    and GPT-6 Astra in place of Fable 5/Opus 4.8/GPT-5.5) and, notably, a
    shift from FrontierCode-only self-benchmarking to a joint evaluation
    with Artificial Analysis and Vals AI (Claim 3) — directly answering the
    second and third triage comments' question about whether this post adds
    genuinely new evidence versus restating the June post. It does not
    mention the June post's dynamic mid-session routing mechanism (that
    source's Claim 6) or its disclosed 5-minute prompt-cache TTL constraint
    (that source's Claim 11) at all — this post is narrower in scope,
    focused on availability, model pairings, and per-pairing tuning rather
    than the full architecture.
  - `blog-anthropic-choosing-claude-model.md` Claim 2 ("cost-per-task is
    often lower for more intelligent models even when price-per-token is
    higher... starting with a smaller model makes it harder to tell model
    failures apart from setup failures"): this source's Claim 7 (Fable 5 as
    lead costs 9% less overall than Opus 4.8 despite costing 2x per token)
    and Claim 8 (SWE-2 sidekick costs less overall than cheaper GPT-5.6 Luna
    despite a 275% per-token premium) are two concrete, quantified instances
    of the same general principle, applied specifically to each role in a
    two-agent harness rather than to single-model selection.

- **Corroborates**:
  - `blog-cognition-multi-agents-working.md` Claims 8-11 (the "Smart
    Friend" pattern's per-call cache-miss problem, motivating a shift toward
    persistent-context multi-agent designs): this post's Claim 4 restates
    and generalizes the cache-miss argument (any mid-task model switch,
    routing included, pays the cache-miss cost) that `blog-cognition-devin-fusion.md`
    Claim 3 first drew from the Smart Friend/Advisor comparison.
  - `blog-simonwillison-gpt6-astra-launch.md` Claim 5 (per Artificial
    Analysis, GPT-6 Astra costs about the same as GPT-5.6 Sol on the Coding
    Agent Index while scoring 2 points higher, and costs less than half of
    Claude Fable 5 for the same score): corroborates this post's framing of
    Astra as a cost-efficient choice on the same Artificial Analysis Coding
    Agent Index this post uses for its headline chart (Claim 1) — both
    sources independently point to Astra's cost-efficiency profile on that
    specific index.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 9 (multi-model routing
    improves cost and quality by routing planning to cheaper models and
    implementation to capable models): this post's lead/sidekick split
    (frontier model plans and reviews, cheaper model implements) inverts
    which role gets the cheaper model relative to Osmani's specific framing
    (Osmani: cheap model for planning, capable model for implementation;
    Fusion: capable model for planning/review, cheap model for
    implementation) — worth flagging as a difference in which task
    dimension each source assigns to the frontier vs. cheap model, though
    not a direct contradiction since Osmani's claim is a general
    orchestration heuristic, not evaluated against Fusion's specific
    architecture or benchmarked head-to-head.

- **Contradicts**: Evaluated one candidate tension, not filed. This post's
  Claim 1/3 present GPT-6 Astra (paired with SWE-2 in Fusion) as achieving
  near-frontier, cost-efficient benchmark scores on short, graded coding
  tasks. `blog-ronacher-astra-why.md` (an independent, hands-on 35-hour
  unattended run of the same GPT-6 Astra model, outside any Fusion-style
  review harness) documents the model committing low-quality "slop" code —
  code-golfed scripts leaking into production files, unexplained hardcoded
  constants, style inconsistent with the surrounding codebase — and
  concludes the author does not yet trust Astra for professional software
  engineering (that source's Claims 1-6, 9). This does not meet the
  `agents/MINER.md` §4a filing bar as a hard contradiction: the two sources
  evaluate materially different conditions — this post measures short,
  discrete, benchmark-graded tasks with a frontier lead (potentially Astra
  itself, or Fable 5.1) reviewing and correcting sidekick output before
  scoring, while Ronacher's report is a single 35-hour unattended run with
  no analogous review/correction loop and an open-ended, ambiguous goal.
  Both could be true simultaneously (Astra performs well on short, graded,
  reviewed tasks; Astra's code-quality discipline degrades over long,
  unsupervised, open-ended horizons) as a conditioning-variable case rather
  than a factual disagreement about the same measurement. Flagged here as a
  tension worth watching rather than filed as a contradiction — if a future
  source benchmarks Astra's *unattended, unreviewed* code quality against
  Fable 5.1's under matched conditions and finds a `Fusion`-relevant
  discrepancy, that would meet the filing bar and this note's "Contradicts"
  section should be revisited.

- **Novel**:
  - The joint third-party benchmarking partnership (Artificial Analysis,
    Vals AI) as evaluators of Fusion, rather than Cognition's own
    FrontierCode benchmark exclusively — a meaningful evidentiary upgrade
    over the June post, though still not fully independent (methodology and
    task-selection process undisclosed).
  - SWE-2, Cognition's currently recommended default sidekick model — not
    documented anywhere else in this corpus prior to this note.
  - The sidekick-side cost/intelligence coupling data (Claim 8): a stronger,
    much pricier sidekick (SWE-2 vs. GPT-5.6 Luna, +275% per-token) that
    nets out *cheaper and higher-scoring* overall — the June post only
    discussed this coupling for the lead role.
  - The three explicit, per-pairing harness-tuning levers (brief detail
    level, sidekick pushback permission, exploration-delegation boundary) —
    concrete operational guidance absent from the June architecture post.
  - CLI/Desktop local availability itself, via a documented one-line
    install command — the June post was cloud-preview-only
    (app.devin.ai/signup).

## Guide Impact

- **Chapter 04 (Cost & Reliability) / Chapter 06 (Model Selection &
  Routing)**: When citing Fusion-style lead/sidekick cost savings, use this
  post's per-benchmark range (roughly −11% to −46%, Concrete Artifacts) and
  explicitly note the range rather than repeating "up to 39%" as if it were
  representative — the 39% figure is the single best-case data point (Astra
  vs. Codex on the Artificial Analysis index), not a typical result across
  benchmarks.

- **Chapter 06 (Model Selection & Routing)**: Add Claim 8's sidekick-side
  finding as a specific instance of "evaluate on price-per-task, not
  price-per-token" (already sourced from `blog-anthropic-choosing-claude-model.md`
  Claim 2): a 275%-pricier sidekick model can still lower total system cost
  if it reduces the lead's review/correction burden enough. Pair this with
  Claim 7's lead-side version (Fable 5 vs. Opus 4.8 as lead, 9% cheaper
  overall despite 2x token price) as two worked examples of the same
  principle applied to each role in a two-agent harness.

- **Chapter 02 (Harness Engineering)**: Add Claim 9's three tuning levers
  (brief verbosity, sidekick pushback permission, exploration-delegation
  scope) as a checklist for teams building or adopting a similar
  lead/sidekick harness: expect to re-tune each lever per model pairing
  rather than assuming one harness configuration transfers across model
  swaps.

- **Chapter 04 (Cost & Reliability)**: Note Claim 4's generalized cache-miss
  argument (any mid-task model switch, not just consult-tool routing, pays a
  cache-invalidation cost) as sharpening the existing guidance from
  `blog-cognition-devin-fusion.md` Claim 3 — useful as a general caution
  against naive difficulty-based model routing, independent of whether a
  team adopts the specific Fusion architecture.

## Extraction Notes

- WebFetch's summarizing pass on this URL returned an accurate, reasonably
  complete summary. To extract verbatim quotes and confirm the exact
  benchmark table figures, the page was additionally fetched via `curl` with
  a browser user-agent and converted to plain text with `html2text` (Python
  library, installed for this extraction). All quotes above were located and
  verified character-for-character against that raw-text extraction (saved
  locally during extraction) before inclusion in this note; the chart data
  (Concrete Artifacts) was read directly from the chart's underlying text
  labels as they appear in the extracted plain text, not re-derived from a
  visual reading of the rendered chart image.
- The Closeout percentage in the "Where an agent spends its turns" chart is
  not stated as a number in the extracted text (the source lists "Closeout"
  as a labeled category alongside Plan/Setup/Implementation/Debug/Validate,
  but only five numeric percentages — 32%, 34%, 5%, 17%, 9%, summing to
  97% — appear in the extracted text). This is left unstated in Concrete
  Artifacts rather than guessed (the implied ~3% would put Closeout as the
  smallest category, consistent with it being a wrap-up phase, but this is
  inference, not something the source states).
- No sub-pages were followed. The post contains only an install-script link
  (cli.devin.ai/install.sh, not a content page) and image assets; no other
  substantive linked pages were present to follow per `agents/MINER.md` §1.
- Cross-references verified before writing: re-read
  `blog-cognition-devin-fusion.md` in full and confirmed Claims 2, 3, 6, 10,
  11 by number and content; re-read `blog-cognition-multi-agents-working.md`
  and confirmed Claims 8-11 by number and content; re-read
  `blog-anthropic-choosing-claude-model.md` and confirmed Claim 2 by number
  and content; re-read `blog-addyosmani-code-agent-orchestra.md` and
  confirmed Claim 9 by number and content; re-read
  `blog-simonwillison-gpt6-astra-launch.md` and confirmed Claim 5 by number
  and content; re-read `blog-ronacher-astra-why.md` in full and confirmed
  Claims 1-6 and 9 by number and content before evaluating (and declining to
  file) the Astra-trustworthiness tension described in Cross-References →
  Contradicts. No claim number was guessed or approximated.
- The prior triage comments on this issue disagreed with each other on
  specific figures (36-39% vs. 39% vs. 35-41%, and "SWE-2" vs. "GPT-6
  Astra" as the paired model in different comments) — these were treated as
  untrusted, unverified triage notes per this task's instructions, not as
  source facts. All figures and model names in this note were independently
  verified against the raw fetched source text rather than copied from any
  triage comment.
- Confidence rated `emerging` overall: this is a first-party vendor
  announcement with specific, quantified claims now partly corroborated by
  named third-party benchmark operators (Artificial Analysis, Vals AI) — a
  step up in rigor from the June post's self-benchmarked-only claims — but
  it still lacks disclosed methodology/sample sizes for the third-party
  benchmarks, doesn't address the June post's unresolved cache-TTL
  constraint, and the "up to 39%" headline is a best-case rather than
  representative figure (Claim 3's "Our assessment"). Not rated `settled`
  because no figure here is independently replicated outside this single
  joint evaluation.
