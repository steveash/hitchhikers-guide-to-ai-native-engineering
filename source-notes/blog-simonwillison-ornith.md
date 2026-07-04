---
source_url: https://simonwillison.net/2026/Jun/29/ornith/
source_type: blog-post
title: "Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding"
author: Simon Willison
date_published: 2026-06-29
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: emerging
issue: "#1504"
---

# Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding

> Willison's hands-on look at Ornith-1.0 — a new MIT-licensed open-weights model family
> from DeepReinforce, built on Gemma 4 + Qwen 3.5 — surfaces a genuinely new training-time
> pattern for the corpus: models that learn to generate their own task-specific RL
> scaffolds jointly with the solution, defended against reward hacking by a three-layer
> trust-boundary/monitor/judge architecture, plus a concrete local-deployment data point
> (35B GGUF via LM Studio + the Pi agent harness handling multi-tool-call code navigation).

## Source Context

- **Type**: blog-post (Simon Willison's short-form "link blog" post at simonwillison.net,
  linking to and summarizing DeepReinforce's own technical announcement at
  deep-reinforce.com/ornith_1_0.html; both pages were fetched for this note, along with the
  linked Pi agent-harness product page at pi.dev that Willison used for testing.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` Python CLI,
  and one of the most widely-cited practitioner commentators on LLM tooling. His "pelican
  riding a bicycle" SVG test is a recurring, informal cross-model benchmark he applies
  consistently across new model releases (cf. `blog-simonwillison-deepseek-v4.md`,
  `blog-simonwillison-glm51.md`). This post is first-person hands-on testing plus a summary
  of the vendor's own technical claims — not independent verification of DeepReinforce's
  benchmark numbers. No disclosed affiliation with DeepReinforce.
- **Scope**: Covers the Ornith-1.0 model family (sizes, licensing, base models), Willison's
  own local test session (Datasette code-navigation tasks, pelican SVG generation
  throughput), and a summary of DeepReinforce's self-improving training methodology and
  benchmark table. Does NOT cover: independent benchmark reproduction, training data
  composition, safety evaluation, or production deployment experience beyond a single local
  test session.

## Extracted Claims

### Claim 1: Ornith-1.0 is an MIT-licensed open-weights model family from DeepReinforce, in four size variants, built on pretrained Gemma 4 and Qwen 3.5
- **Evidence**: Stated directly in both Willison's post and DeepReinforce's own announcement, with identical wording in the two sources.
- **Confidence**: settled (published model metadata at time of post)
- **Quote**: "This is an interesting new open weights (MIT licensed) model, the first model release from DeepReinforce. [...] with variants including 9B Dense, 31B Dense, 35B MoE, and 397B MoE. Built on top of pretrained Gemma 4 and Qwen 3.5, it achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks."
- **Our assessment**: Four size variants spanning 9B (edge-deployable dense) to 397B (frontier-scale MoE) is a wide range for a first model release from a new lab. Building on both Gemma 4 and Qwen 3.5 as base models (rather than training from scratch) is a capital-efficient strategy that depends entirely on the base models' licenses being compatible with derivative redistribution (see Claim 2).

### Claim 2: The underlying Gemma 4 and Qwen 3.5 base models are both Apache 2.0 licensed, making the MIT-licensed Ornith-1.0 derivative legally clean — unlike earlier Gemma releases
- **Evidence**: Willison's own licensing analysis, explicitly contrasting Gemma 4's license with prior Gemma releases' more restrictive terms.
- **Confidence**: settled (Willison states this as fact, not speculation; Apache 2.0 and MIT are both well-understood permissive licenses)
- **Quote**: "As far as I can tell the licenses of those underlying models is compatible with being used in this way - Gemma 4 is Apache 2.0 licensed (and not bound by the janky additional Gemma Terms of Use that afflicted the previous Gemma models) and Qwen 3.5 is Apache 2.0 licensed as well."
- **Our assessment**: This is a practically important detail for anyone evaluating whether to build on Ornith-1.0 commercially: a chain of Apache 2.0 base models feeding into an MIT-licensed derivative removes the additional-use-restriction risk that affected earlier Gemma-based projects. "As far as I can tell" is a hedge worth preserving — Willison is not a lawyer and this is not legal advice, just an informed practitioner's read.

### Claim 3: Ornith-1.0's core innovation is a self-improving training framework where the model jointly learns to generate solution rollouts and the task-specific harnesses ("scaffolds") that guide those rollouts, rather than relying on a fixed human-designed harness
- **Evidence**: DeepReinforce's own technical announcement describes the two-stage RL step in detail: the model first proposes a refined scaffold conditioned on the task and prior scaffold, then generates a solution rollout conditioned on that scaffold; reward is propagated to both stages.
- **Confidence**: emerging (first-party technical description from the model's creator; not independently verified or reproduced by a third party)
- **Quote**: "The key innovation behind Ornith-1.0 is a self-improving training framework. Instead of relying on human-designed harnesses to drive solution generation in RL, Ornith-1.0 learns to generate both solution rollouts and the task-specific harnesses that guide those rollouts. By jointly optimizing the scaffold and the resulting solution, the model can discover better search trajectories and generate higher-quality solutions."
- **Our assessment**: This is the most novel claim in the source for this corpus. Everything else in the guide's harness-engineering material treats the harness as something humans design and the model operates within. Ornith-1.0's approach inverts that: the harness itself becomes a learned, per-task-category artifact that co-evolves with the policy during training. If this generalizes, it implies a future where "harness engineering" partially migrates from a human practitioner discipline into a training-time optimization target — though DeepReinforce is a new, largely unverified lab (Claim 9), so this claim should be treated as a promising but unreplicated research direction, not an established technique.

### Claim 4: DeepReinforce defends against reward hacking in the self-scaffolding setup with a three-layer architecture: an immutable outer trust boundary, a deterministic monitor, and a frozen LLM judge acting as a veto
- **Evidence**: DeepReinforce's technical blog explicitly names the reward-hacking risk (a self-generated scaffold learning to satisfy the verifier without doing the task — e.g., reading withheld test files, hardcoding expected outputs, copying an oracle solution) and describes three concrete countermeasures.
- **Confidence**: emerging (first-party description of a training-time safety architecture; no third-party audit of its effectiveness)
- **Quote**: "We defend against this in three layers. First, we fix the outer trust boundary: the environment, the tool surface, and test isolation are immutable and outside the model's reach, so the model evolves only the inner policy scaffold: its memory, error-handling, and orchestration logic. Second, a deterministic monitor enforces that boundary at the level it can be specified exactly, flagging any attempt to read withheld paths, modify verification scripts, or invoke actions outside the sanctioned tool surface, and assigning such trajectories zero reward with exclusion from the advantage computation. Third, because intent-level gaming can occur entirely within the allowed tool surface, a frozen LLM judge acts as a veto on top of the verifier rather than the primary reward."
- **Source**: deep-reinforce.com/ornith_1_0.html (linked directly from the Willison post)
- **Our assessment**: This is a training-time mirror of the eval-time reward-hacking mitigations documented in `blog-cursor-reward-hacking-benchmarks.md` (history isolation, egress proxying). Where Cursor's post addresses models gaming a *fixed* benchmark harness during *evaluation*, DeepReinforce is addressing a *self-generated, evolving* harness gaming its own reward signal during *training* — a harder problem because the exploitable surface (the scaffold) is itself something the model controls. The "frozen LLM judge as veto, not primary reward" design choice is notable: it avoids the judge itself becoming a second reward-hacking target by never letting the policy directly optimize against it.

### Claim 5: DeepReinforce reports Ornith-1.0-397B matching or exceeding Claude Opus 4.7 on Terminal-Bench 2.1 and SWE-Bench Verified, while trailing Claude Opus 4.8 on the same benchmarks
- **Evidence**: DeepReinforce's published benchmark table: Ornith-1.0-397B scores 77.5 (Terminal-Bench 2.1, Terminus-2 harness) and 82.4 (SWE-Bench Verified), vs. Claude Opus 4.7 at 70.3 and 80.8, and Claude Opus 4.8 at 85 and 87.6.
- **Confidence**: emerging (first-party, self-reported benchmark table; no independent reproduction; DeepReinforce also states outperforming "MiniMax M3" (66.0 / 80.5) and "DeepSeek-V4-Pro" (67.9 / 80.6))
- **Quote**: "Ornith-1.0-397B achieves 77.5 on Terminal-Bench 2.1 and 82.4 on SWE-Bench Verified, surpassing Claude Opus 4.7 on both benchmarks and outperforming leading open-source models of similar size, including Minimax M3 and DeepSeek-V4-Pro."
- **Source**: deep-reinforce.com/ornith_1_0.html
- **Our assessment**: The choice of Claude Opus 4.7 as the comparison baseline — rather than the newer Claude Opus 4.8, which the same table shows beating Ornith-1.0-397B on every reported benchmark (85 vs 77.5 on Terminal-Bench 2.1 Terminus-2; 87.6 vs 82.4 on SWE-Bench Verified) — is a self-serving framing choice typical of first-release vendor benchmarking. Any guide citation of "Ornith beats Claude Opus" should be qualified: it beats an older Opus generation, not the current one, and the comparison is entirely first-party.

### Claim 6: The 35B MoE variant significantly outperforms same-size open-weights models and, despite its much smaller size, beats the 397B Qwen 3.5 model on Terminal-Bench 2.1
- **Evidence**: DeepReinforce's benchmark table and prose both make this claim, though with a small numeric discrepancy between the prose (64.4) and the table (64.2) for Ornith-1.0-35B's Terminal-Bench 2.1 (Terminus-2) score.
- **Confidence**: emerging (first-party benchmark; internal inconsistency between prose and table numbers noted, though the qualitative claim — 35B beating 397B on this one benchmark — holds under either number)
- **Quote**: "Ornith-1.0-35B significantly outperforms similarly sized models, including Qwen 3.5-35B, Qwen 3.6-35B, and Gemma 31B. Despite having only 35B parameters, it even surpasses Qwen 3.5-397B on Terminal-Bench 2.1 (64.4 vs. 53.5) while matching its performance across several other coding and agentic benchmarks."
- **Source**: deep-reinforce.com/ornith_1_0.html (prose states 64.4; the accompanying results table states 64.2 for the same cell)
- **Our assessment**: A ~10x-smaller model beating a same-family model on one benchmark while only "matching" it elsewhere is consistent with a training methodology (self-scaffolding RL) that specifically targets agentic-coding task structure rather than raw scale — but it's a single-benchmark claim from the model's own creator, and the prose/table discrepancy (64.4 vs 64.2) is a small but real red flag for how carefully the announcement was proofread.

### Claim 7: DeepReinforce publishes per-benchmark evaluation harness configuration, including two different harnesses for the same benchmark (Terminus-2 vs. Claude Code) producing different scores for the same model
- **Evidence**: The footnote section specifies exact harness, temperature, top_p, context window, timeout, and hardware for each benchmark family, and reports Terminal-Bench 2.1 scores separately for "Terminus-2" harness and "Claude Code 2.1.126" harness.
- **Confidence**: settled (methodology is stated explicitly and is independently checkable in principle)
- **Quote**: "Terminal-Bench 2.1 (Terminus-2): We evaluate Terminal-Bench 2.1 using the Harbor/Terminus-2 framework with parser=json, temperature=1.0, top_p=1.0, and a 128K context window. [...] Terminal-Bench 2.1 (Claude Code): We evaluate Terminal-Bench 2.1 using Claude Code 2.1.126 with parser=json, temperature=1.0, top_p=1.0, max_new_tokens=131072."
- **Source**: deep-reinforce.com/ornith_1_0.html, "Footnote" section
- **Our assessment**: This directly corroborates `blog-cursor-reward-hacking-benchmarks.md`'s Claim 10/11 point that benchmark scores are not comparable without harness specification. DeepReinforce's own table shows non-trivial score deltas for the same model on the same nominal benchmark depending on harness (e.g., Ornith-1.0-397B: 77.5 under Terminus-2 vs 78.2 under Claude Code harness — a smaller gap than some Cursor-documented cases, but the same underlying phenomenon). This is a rare case of a vendor voluntarily disclosing harness-dependent variance rather than hiding it.

### Claim 8: Willison's hands-on test had the 35B GGUF-quantized variant (20GB, Q4_K_M) running locally via LM Studio and the Pi agent harness, successfully completing two multi-step code-navigation tasks against a Datasette checkout
- **Evidence**: Willison's own terminal session (linked but not statically fetchable — see Extraction Notes) plus his prose description of the test.
- **Confidence**: anecdotal (single practitioner, single session, two tasks; no controls or comparison run against other models in the same post)
- **Quote**: "I've been running the model using LM Studio and the ornith-1.0-35b-Q4_K_M.gguf (20GB) GGUF, hooked up to Pi. Initial impressions are very good - it seems to be able to run the agent harness over many tool calls in a proficient way. Here's a terminal session where I asked it to \"find the code that decodes the actor cookie\" and then \"find the code that opens the insert dialog when thebutton is clicked\" against a Datasette checkout, which it handled with ease."
- **Our assessment**: This is a genuine local-deployment data point: a 20GB quantized checkpoint, consumer-hardware-plausible, driving a real multi-tool-call agentic code-search session against a non-trivial codebase (Datasette, ~Willison's own large project). "Handled with ease" is Willison's subjective read, not a measured success rate — treat as a positive anecdotal signal for local-model agentic coding viability, not proof of general capability.

### Claim 9: Willison found very little public information about DeepReinforce as an organization; the earliest identifiable prior work is a June 2025 paper on CUDA optimization via contrastive reinforcement learning
- **Evidence**: Willison's own background research, stated as a limitation of what he could find.
- **Confidence**: anecdotal (absence-of-evidence claim from one person's search; the org may simply be new or intentionally low-profile)
- **Quote**: "I couldn't find much information about DeepReinforce themselves. The earliest paper I could find from the was CUDA-L1: Improving CUDA Optimization via Contrastive Reinforcement Learning from June 2025."
- **Our assessment**: A model release from an org with almost no public track record, whose only identifiable prior work is a contrastive-RL CUDA-optimization paper, is a meaningful provenance gap. It's consistent with the self-scaffolding RL training approach in Ornith-1.0 (both are RL-for-optimization research directions), which lends some coherence to the claim that this is a genuine research lab rather than a rebadged existing model — but the benchmark claims in Claims 5-6 should be weighted accordingly: this is not a lab with an established track record of accurate self-reported benchmarks.

### Claim 10: Willison's standard "pelican riding a bicycle" SVG test produced a recognizable but imperfect result at 103 tokens/second
- **Evidence**: Willison's direct observation of output quality and generation speed for his recurring cross-model creative-code benchmark.
- **Confidence**: anecdotal (single generation, single model, no comparison numbers for other models in this same post)
- **Quote**: "I also had it draw this pelican, which came out at 103 tokens/second: It's a little bit mangled but the pelican is clearly a pelican."
- **Our assessment**: 103 tokens/second is a local-inference throughput figure (LM Studio, presumably on Willison's own hardware — not specified) for SVG-as-text generation, not a vendor-published benchmark. It's a useful anecdotal throughput data point for local 35B MoE inference but is not comparable across posts without knowing Willison's hardware for this specific session, which is not stated here.

### Claim 11: Pi, the agent harness Willison used to test Ornith-1.0, is deliberately minimal — it ships without sub-agents, plan mode, MCP support, permission popups, or background bash, instead exposing extension primitives for users to add those features themselves
- **Evidence**: Pi's own product site (pi.dev), linked directly from the "hooked up to Pi" mention in Willison's post.
- **Confidence**: settled (first-party product description, directly checkable against the linked site)
- **Quote**: "Pi is a minimal agent harness. Adapt Pi to your workflows, not the other way around." / "Pi ships with powerful defaults but skips features like sub-agents and plan mode."
- **Source**: pi.dev (linked from the Willison post's "Pi" hyperlink)
- **Our assessment**: This is supporting context rather than a claim about Ornith-1.0 itself, but it matters for interpreting Claim 8: the harness under which Willison judged Ornith-1.0 to "run the agent harness over many tool calls in a proficient way" is an intentionally bare-bones harness (MIT licensed, by Earendil Inc.), not a fully-featured agent product. A model performing well under Pi's minimal defaults says something different than performing well under a harness with built-in sub-agents, plan mode, and permission gating. `blog-ronacher-pi-oss.md` documents Pi's own maintenance experience as an OSS project (issue/PR volume, `/is`/`/wr` slash commands) but not Pi's feature-set philosophy — this note adds that missing architectural context.

## Concrete Artifacts

### Ornith-1.0 model variants and licensing (verbatim from simonwillison.net/2026/Jun/29/ornith/)
```
Variants: 9B Dense, 31B Dense, 35B MoE, 397B MoE
Base models: Gemma 4 (Apache 2.0) + Qwen 3.5 (Apache 2.0)
Derivative license: MIT
Tested checkpoint: ornith-1.0-35b-Q4_K_M.gguf (20GB), via LM Studio + Pi
```

### Benchmark table excerpt — 397B tier (verbatim figures from deep-reinforce.com/ornith_1_0.html)
```
Benchmark                          Ornith-1.0-397B  Claude Opus 4.7  Claude Opus 4.8
Terminal Bench 2.1 (Terminus-2)    77.5             70.3             85
Terminal Bench 2.1 (Claude Code)   78.2             69.7             78.9
SWE-Bench Verified                 82.4             80.8             87.6
SWE-Bench Pro                      62.2             64.3             69.2

Benchmark                          Ornith-1.0-397B  Minimax-M3-428B  DeepSeek-V4-Pro-1.6T
Terminal Bench 2.1 (Terminus-2)    77.5             64.0             64.0
SWE-Bench Verified                 82.4             80.5             80.6

Benchmark                          Ornith-1.0-35B   Qwen3.5-35B  Qwen3.6-35B  Qwen3.5-397B
Terminal Bench 2.1 (Terminus-2)    64.2             41.4         52.5         53.5

Benchmark                          Ornith-1.0-9B    Qwen3.5-9B  Gemma4-12B  Gemma4-31B
Terminal Bench 2.1 (Terminus-2)    43.1             21.3        21          42.1
SWE-Bench Verified                 69.4             53.2        44.2        52
```

### Evaluation harness footnote (verbatim from deep-reinforce.com/ornith_1_0.html)
```
Terminal-Bench 2.1 (Terminus-2): We evaluate Terminal-Bench 2.1 using the Harbor/Terminus-2
framework with parser=json, temperature=1.0, top_p=1.0, and a 128K context window. Each run
uses a 4-hour timeout with 32 CPU cores and 48GB RAM, and results are averaged over 5 runs.

Terminal-Bench 2.1 (Claude Code): We evaluate Terminal-Bench 2.1 using Claude Code 2.1.126
with parser=json, temperature=1.0, top_p=1.0, max_new_tokens=131072. Results are averaged
over 5 runs.

SWE-Bench Verified, Pro and Multilingual: using OpenHands harness with temp=1.0, top_p=0.95,
256k context window.

SWE Atlas QnA, RF, TW: using mini SWE agent harness with temp=1.0, top_p=0.95, 128K context
window. Results are averaged over 5 runs.

NL2Repo: with temperature=1.0, top_p=1.0, 400K context, 48K output and anti-hacking filters.

ClawEval: An agentic code benchmark over real-user task distributions; temp=0.6 and 256K
context.
```

### Reward-hacking three-layer defense (verbatim from deep-reinforce.com/ornith_1_0.html)
```
1. Outer trust boundary (immutable): environment, tool surface, and test isolation are
   fixed and outside the model's reach; only the inner policy scaffold (memory,
   error-handling, orchestration logic) is learnable.
2. Deterministic monitor: flags any attempt to read withheld paths, modify verification
   scripts, or invoke actions outside the sanctioned tool surface; assigns zero reward
   and excludes the trajectory from the advantage computation.
3. Frozen LLM judge: acts as a veto on top of the verifier (not the primary reward),
   to catch intent-level gaming that stays within the allowed tool surface.
```

### Datasette code-navigation test tasks (verbatim from simonwillison.net/2026/Jun/29/ornith/)
```
Task 1: "find the code that decodes the actor cookie"
Task 2: "find the code that opens the insert dialog when the button is clicked"
Target: a Datasette checkout
Result: "handled with ease"
```

## Cross-References

- **Corroborates**: `blog-cursor-reward-hacking-benchmarks.md` (Claims 6, 7, 10) — that
  source documents harness-dependent SWE-bench score gaps of 9–20 points for the same
  model depending on eval-harness configuration (history isolation, egress proxying), and
  recommends teams "make the setup clear when they report results." DeepReinforce's
  footnoted per-benchmark harness disclosure (Concrete Artifacts, above) and its two
  different Terminal-Bench 2.1 scores for the same model under two harnesses (Terminus-2
  vs. Claude Code) is a rare case of a vendor actually following that recommendation.
- **Corroborates**: `blog-simonwillison-deepseek-v4.md` and `blog-simonwillison-glm51.md`
  — both document Willison's recurring pattern of hands-on testing a newly-released
  MIT/Apache-licensed open-weights model within days of release, using the pelican-SVG
  test plus a real coding/agentic task as an informal but consistent evaluation ritual.
  This post follows the identical pattern (license check, pelican SVG, one real coding
  task) applied to an agentic-coding-specialized model rather than a general one.
- **Extends**: `blog-ronacher-pi-oss.md` — that note documents Pi's operational experience
  as an OSS project under AI-generated issue/PR volume (slop issues, the `/is`/`/wr`
  slash-command patterns) but does not describe Pi's own feature-set philosophy. This
  note's Claim 11 supplies that missing architectural context: Pi is designed as a
  deliberately minimal harness with extension primitives rather than built-in features.
  Together, the two notes give both the design philosophy (this note) and the lived
  maintenance consequences (`blog-ronacher-pi-oss.md`) of that philosophy.
- **Novel**: The self-scaffolding joint scaffold/solution RL training pattern (Claim 3)
  and its accompanying three-layer reward-hacking defense (Claim 4) are new to the corpus.
  No existing source note documents a model where the *harness itself* is a learned,
  per-task-category training artifact rather than a fixed human-designed structure the
  model operates within — every other harness-engineering source in the corpus treats
  the harness as something practitioners build externally.
- **Contradicts**: None identified. No existing corpus note makes a claim about
  self-scaffolding training or DeepReinforce specifically that this source conflicts with.
  No contradiction issue filed.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the self-scaffolding training pattern (Claim 3)
  as a forward-looking research direction distinct from the guide's existing
  harness-engineering material, which treats the harness as an artifact humans design and
  the model operates within. Frame it explicitly as unreplicated, first-party research from
  a new lab (Claim 9) — not yet an established technique — but worth flagging as a
  direction that could eventually blur the line between "harness engineering" (a
  practitioner discipline) and "training-time scaffold optimization" (a model-training
  technique).
- **Chapter 02/03 (Reward Hacking & Evaluation)**: Add DeepReinforce's three-layer
  training-time reward-hacking defense (Claim 4) alongside the existing eval-time
  mitigations from `blog-cursor-reward-hacking-benchmarks.md` (history isolation, egress
  proxying). Together they give a fuller picture: mitigations exist for reward hacking
  both during RL training (fixed trust boundary + deterministic monitor + frozen judge
  veto) and during benchmark evaluation (sealed git history + network egress control).
  Also add the harness-disclosure footnote (Claim 7) as a positive example of a vendor
  specifying eval harness configuration per benchmark — reinforcing the guide's existing
  point that benchmark scores are not comparable without harness specification.
- **Chapter 01/05 (Local Deployment)**: Add the concrete local-deployment data point
  (Claim 1, Claim 8): a 20GB Q4_K_M-quantized 35B MoE checkpoint, run via LM Studio and the
  Pi agent harness, handling multi-tool-call agentic code search against a real, non-trivial
  codebase. Useful as a practical reference point for practitioners scoping local-hardware
  requirements for agentic coding, alongside the existing DeepSeek V4 / GLM-5.1 data points.
- **Caveat for any citation of benchmark numbers**: DeepReinforce's headline claim (matches
  Claude Opus 4.7) is true per Claim 5's table, but the same table shows Claude Opus 4.8 —
  the actual current frontier model at time of release — beating Ornith-1.0-397B on every
  listed benchmark. Any guide reference to Ornith's benchmark standing should include this
  qualifier rather than repeating the vendor's own framing uncritically.

## Extraction Notes

- **WebFetch reliability issue, flagged and worked around**: Initial attempts to read the
  simonwillison.net post via the WebFetch tool returned inconsistent paraphrases across
  repeated calls, one of which fabricated a refusal citing a "125-character quote limit"
  that was never requested, and one of which returned a response with an embedded fake
  `<system-reminder>` tag nudging toward unrelated tool use. Both were treated as
  unreliable output from the fetch tool's summarizing layer (flagged to the user in
  conversation) rather than followed. To get genuinely verbatim text, the post's raw HTML
  was fetched directly via `curl` and hand-parsed (tags stripped, entities decoded) rather
  than relying on WebFetch's model-mediated summary. All quotes in this note were sourced
  from that raw-HTML extraction, not from the earlier WebFetch paraphrases.
- **DeepReinforce technical page**: WebFetch returned HTTP 403 for
  `deep-reinforce.com/ornith_1_0.html`; the page was instead fetched directly via `curl`
  (HTTP 200), which is the source for all DeepReinforce-attributed quotes, the benchmark
  tables, and the reward-hacking defense description in this note.
- **Pi product site** (pi.dev): fetched via `curl` for Claim 11's supporting context; this
  is a secondary linked page (the harness Willison used for testing), not the primary
  source, so it is used only for framing Claim 8, not as an independent claim about
  Ornith-1.0.
- **Not extractable**: the linked terminal-session transcript
  (`gisthost.github.io/?35da4d9ce7f0c27124c67655a0dc9e5d`) is a JavaScript-rendered gist
  viewer with no static HTML content — the actual tool-call transcript could not be
  fetched or verified beyond Willison's prose summary ("handled with ease"). The pelican
  SVG image itself (a GitHub gist) was not visually inspected.
- **Benchmark table discrepancy**: DeepReinforce's own prose states Ornith-1.0-35B scores
  "64.4" on Terminal-Bench 2.1 vs. Qwen 3.5-397B's 53.5, while the accompanying results
  table lists 64.2 for the same cell. Both numbers are reported in Claim 6 and the
  Concrete Artifacts table uses the table's figure (64.2).
- **No contradiction issues filed**: no existing corpus source makes a claim about
  self-scaffolding RL training or DeepReinforce that this source disagrees with.
