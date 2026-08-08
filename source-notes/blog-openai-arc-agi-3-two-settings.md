---
source_url: https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores
source_type: blog-post
title: "How enabling two settings tripled our scores on the ARC-AGI-3 benchmark"
author: OpenAI
date_published: 2026-07-29
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: emerging
issue: "#2569"
---

# How enabling two settings tripled our scores on the ARC-AGI-3 benchmark

> OpenAI's first-party case study showing that GPT‑5.6 Sol's low ARC-AGI-3
> score (7.8%) was largely a harness artifact, not a capability ceiling:
> enabling two Responses API settings — retained reasoning and compaction —
> tripled its score (13.3% → 38.3% RHAE) and cut output tokens 6x, with no
> change to the model itself.

## Source Context

- **Type**: blog-post (OpenAI house engineering write-up, `openai.com/index/`,
  no named individual author).
- **Author credibility**: First-party account of OpenAI's own investigation
  into its own model's benchmark performance, describing an internal
  re-implementation of the ARC-AGI-3 harness using OpenAI's own Responses
  API. This is direct engineering testimony with specific before/after
  numbers and a stated mechanism, not a third-party audit — the standard
  vendor-self-report caveat applies (no independent reproduction of the
  13.3%/38.3% figures by ARC or any outside party is cited in the piece).
  The post explicitly credits ARC Prize's own team for "their analysis that
  inspired us to take a closer look," suggesting the investigation began
  from an external observation, which lends some outside grounding to the
  motivation even though the numbers themselves are OpenAI-measured.
- **Scope**: Covers GPT‑5.6 Sol's performance on the ARC-AGI-3 public task
  set under the official (generic) harness versus a Responses-API
  reimplementation with retained reasoning and compaction enabled, the two
  root causes identified in the official harness (reasoning discarded each
  turn; rolling truncation at 175,000 characters), and OpenAI's resulting
  recommendation for API developers and benchmark runners. Does NOT cover:
  a task-by-task or level-by-level score breakdown, how other model
  families perform under the same modified harness, independent
  verification of the RHAE numbers by ARC Prize or a third party, or
  detailed ablation isolating the contribution of retained reasoning alone
  versus compaction alone (the two settings are reported only in
  combination, plus the deprecated legacy-harness baseline).

## Extracted Claims

### Claim 1: GPT‑5.6 Sol's official ARC-AGI-3 score (7.8%) was strikingly low relative to its other demonstrated capabilities, and GPT‑5.5 scored barely above zero (0.4%)
- **Evidence**: Direct contrast between GPT‑5.6 Sol's headline capabilities (solving the cycle double cover conjecture, beating Pokémon FireRed) and its ARC-AGI-3 score, stated as the article's opening puzzle.
- **Confidence**: settled (directly reported scores, not in dispute)
- **Quote**: "But on ARC-AGI-3, a benchmark of 2D puzzle games, GPT‑5.6 Sol scored just 7.8%, and GPT‑5.5 could barely play the games at all, scoring a paltry 0.4%."
- **Our assessment**: This framing — a flagship model scoring near zero on a benchmark while otherwise demonstrating strong general capability — is the article's setup for arguing the gap is a harness problem, not a capability problem. Worth noting this specific 7.8% figure is the same number reported in the vendor benchmark table analyzed in `blog-openai-gpt56-ga-announcement.md` (see Cross-References); this article is effectively a retraction-by-explanation of that table's ARC-AGI-3 row.

### Claim 2: Enabling two Responses API settings — retained reasoning and compaction — tripled GPT‑5.6 Sol's ARC-AGI-3 score and cut its output tokens by 6x on the public task set
- **Evidence**: Stated as the article's central finding, following a description of the investigation into why the model was scoring low.
- **Confidence**: settled (the article's core, directly measured claim)
- **Quote**: "In the case of ARC-AGI-3, we discovered that turning on two API settings we use in ChatGPT and Codex—retained reasoning and compaction—tripled scores and cut output tokens by 6x on the public task set."
- **Our assessment**: A precise, falsifiable engineering claim: same model weights, two configuration changes, 3x score and 6x token efficiency. This is the sharpest single data point in the corpus for the "harness configuration, not raw model capability, often explains benchmark performance" thesis (see Cross-References to `blog-humanlayer-skill-issue-harness-engineering.md`).

### Claim 3: Under the official harness GPT‑5.6 Sol scored 13.3% RHAE on the ARC-AGI-3 public set; with retained reasoning and compaction it scored 38.3%; the estimated average human tester scores 48%, and models cannot see their own score or the scoring metric during play
- **Evidence**: A captioned chart figure giving both scores plus the human-baseline estimate and a note on what the model can/cannot observe during play.
- **Confidence**: settled (specific reported figures with methodology reference)
- **Quote**: "With the official harness, GPT‑5.6 Sol scored 13.3% on the ARC-AGI-3 public set. With retained reasoning and compaction, it scored 38.3%." ... "we estimate the average human tester scored 48%. Models are not told how they will be scored, and cannot see their score throughout—actions only return a text representation of each frame and what level they are on."
- **Our assessment**: 13.3% → 38.3% is roughly 2.9x, consistent with the "tripled" framing in Claim 2. Even at 38.3%, GPT‑5.6 Sol with the improved harness still trails the ~48% estimated human baseline — the two-settings fix closes most but not all of the human/model gap on this benchmark, a nuance worth preserving alongside the headline "tripled" claim.

### Claim 4: Root cause #1 — the official ARC-AGI-3 harness discarded all private reasoning after each action, forcing the model to re-derive its understanding of the game from scratch every turn, retaining only a log of past moves and brief notes (not the reasoning that produced them)
- **Evidence**: Direct engineering diagnosis presented as the first of two identified harness defects.
- **Confidence**: settled (a specific, mechanistic diagnosis stated as fact by the investigating team)
- **Quote**: "First, we noticed that after each game action, all private reasoning was discarded. This meant that with each action, GPT‑5.6 Sol was asked to figure out the game anew, unable to remember its past thinking. The model could still see a record of past moves and brief accompanying notes, but it could not see the plans, insights, or thoughts that led to them."
- **Our assessment**: This is a specific, concrete failure mode — discarding chain-of-thought/reasoning state between turns — distinct from generic "context window fills up" framing found elsewhere in the corpus. It is the mechanism, not just the symptom.

### Claim 5: Root cause #2 — the official harness used a rolling truncation window (dropping the oldest messages once the conversation context exceeded 175,000 characters), causing older actions to become invisible as history grew, compounding the loss of the model's past reasoning
- **Evidence**: Direct engineering diagnosis presented as the second identified harness defect, with the exact truncation threshold given later in the article.
- **Confidence**: settled (a specific, checkable threshold value stated by the authors)
- **Quote**: "Second, we saw that the harness used a rolling truncation window, causing older actions to become invisible as the history grew." ... "The ARC-AGI-3 harness addresses context limits with rolling truncation. When the conversation context exceeds 175,000 characters, the oldest messages are discarded."
- **Our assessment**: Combined with Claim 4, this means the official harness was compounding two separate memory losses: no reasoning ever survives a turn, and even the surviving action log eventually falls out of the window. Together these explain why the model "was struggling to learn over time" (the article's own summary phrase for the combined effect).

### Claim 6: Retaining reasoning across turns (via the Responses API's `previous_response_id` mechanism) made GPT‑5.6 Sol spend less time thinking per action, because it no longer had to reinterpret the game from scratch each turn, and made it markedly better at learning over time and employing coherent multi-turn strategies
- **Evidence**: Direct before/after behavioral observation following the switch to reasoning retention.
- **Confidence**: settled (stated as a direct observation by the investigating team, though qualitative rather than separately quantified from the compaction effect)
- **Quote**: "With reasoning retained, we noticed two big changes. First, GPT‑5.6 Sol spent less time thinking before each action, because it no longer had to interpret the game from scratch every turn. Second, when it was able to remember its past thoughts, GPT‑5.6 Sol was much better at learning over time and employing coherent strategies."
- **Our assessment**: This isolates retained reasoning's contribution qualitatively (faster per-action thinking, better multi-turn strategy) even though the headline 13.3%→38.3% number is reported only for the combined retained-reasoning-plus-compaction condition — the article does not give a retained-reasoning-only intermediate score.

### Claim 7: Replacing rolling truncation with compaction let GPT‑5.6 Sol preserve what it had learned about each game across longer runs and achieve a higher score with fewer output tokens; rolling truncation both discards earlier observations and forces the model to operate with a persistently fuller context window, which the authors say can slightly impair performance
- **Evidence**: Direct mechanism description contrasting compaction against the rolling-truncation baseline, following the harness-defect diagnosis.
- **Confidence**: emerging (the outcome — higher score, fewer tokens — is directly measured; the specific causal claim that "a fuller context window... can slightly impair performance" is asserted without a separate isolated measurement distinguishing it from the token-count effect)
- **Quote**: "Rolling truncation has two drawbacks. First, the model loses earlier observations and actions. Second, it spends much of the tasks operating with a fuller context window, which can slightly impair performance." ... "When we enabled compaction on ARC-AGI-3, GPT‑5.6 Sol was better able to preserve what it had learned about each game across longer runs, and achieved a higher score with fewer output tokens."
- **Our assessment**: The two named drawbacks of rolling truncation (data loss vs. long-context performance impairment) are conceptually distinct and map onto two separate corpus themes — context loss (already well-covered, e.g. `research-wasnotwas-context-compaction.md`) and long-context degradation independent of information loss (covered by Chroma's context-rot research as cited secondhand in `blog-humanlayer-skill-issue-harness-engineering.md` Claim 13). This article treats both as contributing to the same fix (compaction) without separating their individual contribution.

### Claim 8: Combined, retaining reasoning and enabling compaction let GPT‑5.6 Sol (max) achieve roughly 3x the ARC-AGI-3 score using 6x fewer output tokens
- **Evidence**: Summary statement following the description of both changes and an accompanying animation of context-window usage under each harness.
- **Confidence**: settled (restates the article's headline finding with the specific "(max)" reasoning-effort qualifier)
- **Quote**: "Together, retaining reasoning and compaction allow GPT‑5.6 Sol (max) to achieve roughly 3x the score with 6x fewer output tokens."
- **Our assessment**: The "(max)" qualifier is notable and easy to miss — this specific 3x/6x figure is scoped to the highest reasoning-effort setting, not necessarily representative of GPT‑5.6 Sol at lower effort levels, which the article does not separately report.

### Claim 9: OpenAI frames this as a recurring pattern, not a one-off: evals rarely measure models in isolation because they also measure a bundle of API-setting, harness-design, and prompting choices, and OpenAI states this is not the first time a low public-benchmark score traced back to a generic eval harness dropping reasoning messages
- **Evidence**: Stated directly in the article's conclusion, immediately preceding the developer recommendations.
- **Confidence**: emerging for the general framing (directly stated by the authors); anecdotal for the "not the first time" claim specifically, since no other named prior instance is given anywhere in the article
- **Quote**: "We hope these experiments serve as a reminder that evals rarely measure models in isolation—they also measure a bundle of less visible choices about API settings, harness design, and prompting. This isn’t the first time we’ve been surprised by low scores on a public benchmark and then discovered that the eval runner was using a generic harness that dropped reasoning messages."
- **Our assessment**: The general framing is well-supported by the ARC-AGI-3 case study itself. The "not the first time" line is a bare assertion with zero supporting detail (no benchmark named, no date, no numbers) — treat it as an unverifiable aside rather than a second data point.

### Claim 10: OpenAI's stated recommendation for developers maximizing API performance is to use the Responses API (not the legacy Chat Completions API), retain reasoning, and use compaction; the same recommendation is extended to anyone comparing models via evals
- **Evidence**: A direct, itemized recommendation list closing the article.
- **Confidence**: settled (a direct, unambiguous vendor recommendation)
- **Quote**: "If you’re an API developer trying to maximize performance, we recommend using the same settings that we deploy in our own products: Use our Responses API, not our legacy Chat Completions API; Retain reasoning; Use compaction. And if you’re comparing models, we recommend relying on evals that use the settings above, which best match real-world use in ChatGPT and Codex."
- **Our assessment**: This is a direct, actionable configuration recommendation from the vendor, corroborated mechanistically by Claims 4-8 in this same article. It is also self-interested — OpenAI is recommending its own current-generation API surface (Responses, not the API it explicitly calls "legacy") — which does not make the recommendation wrong, but the "trust but verify" framing should note the vendor has an adoption incentive alongside the technical rationale.

### Claim 11 (secondary source — Responses API blog): The Responses API's defining architectural difference from Chat Completions is that it preserves the model's reasoning state across turns via `previous_response_id`, while Chat Completions drops reasoning between calls; OpenAI reports GPT‑5 via Responses scores 5% better on TAUBench than via Chat Completions "purely by taking advantage of preserved reasoning"
- **Evidence**: Direct architecture description with a named benchmark figure, from OpenAI's separate "Why we built the Responses API" post (linked from the ARC-AGI-3 article as the mechanism behind "retained reasoning").
- **Confidence**: emerging (a specific vendor-reported benchmark delta for a general architectural claim, not independently reproduced)
- **Quote**: "And here’s where reasoning models really shine: Responses preserves the model’s _reasoning state_ across those turns. In Chat Completions, reasoning is dropped between calls, like the detective forgetting the clues every time they leave the room." ... "GPT-5 integrated via Responses scores 5% better on TAUBench compared to Chat Completions, purely by taking advantage of preserved reasoning."
- **Our assessment**: This gives an independent (from a different OpenAI post, published earlier) prior data point for the general "retained reasoning improves multi-turn benchmark performance" mechanism the ARC-AGI-3 article demonstrates at much larger magnitude (2.9x combined effect vs. a 5% TAUBench delta here) — consistent direction, very different scale, which is plausible given ARC-AGI-3's harness had reasoning fully discarded (a total loss) rather than TAUBench's presumed baseline Chat Completions configuration.

### Claim 12 (secondary source — Responses API blog): OpenAI preserves reasoning internally in encrypted form, hidden from the client, rather than exposing raw chain-of-thought — citing risks of hallucinated CoT, harmful content generation, and competitive exposure — with continuation handled via `previous_response_id` or reasoning items
- **Evidence**: Direct product-design rationale, including a quoted internal justification from OpenAI's Chief Scientist at the time of o1-preview's release.
- **Confidence**: settled (a direct, specific product-design description)
- **Quote**: "Responses addresses this by: Preserving reasoning internally, encrypted and hidden from the client. Allowing safe continuation via `previous_response_id` or reasoning items, without exposing raw CoT."
- **Our assessment**: Relevant context for why "retained reasoning" in the ARC-AGI-3 article is a specific API mechanism (an opaque, server-managed continuation token) rather than something a developer could replicate by simply logging and replaying the model's visible chain-of-thought text — the reasoning content itself is never exposed to the harness/caller in the first place.

### Claim 13 (secondary source — Compaction guide): Server-side compaction is enabled by setting `context_management` with a `compact_threshold` on a Responses `create` call; when the rendered token count crosses that threshold, the server runs a compaction pass and emits an opaque, encrypted compaction item that carries forward prior state and reasoning using fewer tokens — this is the specific mechanism the ARC-AGI-3 harness swap used in place of rolling truncation
- **Evidence**: Direct API documentation for the `compaction` feature named in the ARC-AGI-3 article, including a Python code example.
- **Confidence**: settled (documented API mechanism, not a performance claim)
- **Quote**: "You can enable server-side compaction in a Responses create request (`POST /responses` or `client.responses.create`) by setting `context_management` with `compact_threshold`." ... "The returned compaction item carries forward key prior state and reasoning into the next run using fewer tokens. It is opaque and not intended to be human-interpretable."
- **Our assessment**: This is a materially different compaction mechanism than the LLM-summarization pattern used by 6 of 7 coding-agent harnesses documented in `research-wasnotwas-context-compaction.md` Claim 3 — an opaque, server-generated, non-human-readable state blob rather than a text summary re-injected into the prompt. Worth distinguishing in the guide: "compaction" is not one technique but a family, and OpenAI's Responses API implementation is closer to a proprietary state checkpoint than a summarization pass.

### Claim 14 (secondary source — ARC-AGI-3 methodology docs): RHAE (Relative Human Action Efficiency) scores AI systems on completion and per-action efficiency against a human baseline defined as the upper-median first-time human player (by fewest actions) per level; per-level score is capped at 1.15x the human baseline, and per-game score is a weighted average that overweights later, harder levels
- **Evidence**: Direct scoring-methodology documentation from ARC Prize (the benchmark's own docs, linked from the ARC-AGI-3 article's score-comparison caption).
- **Confidence**: settled (documented, specific scoring methodology from the benchmark's own maintainers)
- **Quote**: "ARC-AGI-3 uses **Relative Human Action Efficiency** (RHAE, pronounced “ray”) to score AI systems. RHAE measures per-level action efficiency compared to a human baseline, normalized per game, across all games." ... "The maximum score per level is capped at **1.15x** human baseline."
- **Our assessment**: This confirms RHAE is not a simple completion-rate percentage — it is explicitly efficiency-normalized against human play, capped to avoid single-level runaway scores, and weighted toward harder levels. That context matters for interpreting the 13.3%/38.3%/48% figures in Claim 3: a score of 38.3% does not mean "solved 38.3% of levels," it means a blended completion-and-efficiency figure relative to human performance.

## Concrete Artifacts

```
Source: OpenAI, "How enabling two settings tripled our scores on the
ARC-AGI-3 benchmark," https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores
(published 2026-07-29)

Score comparison (ARC-AGI-3 public task set, RHAE metric):
  Official harness (reasoning discarded + rolling truncation):  13.3%
  Retained reasoning + compaction (Responses API):               38.3%
  Estimated average human tester baseline:                       48%
  Headline vendor benchmark table score (GPT-5.6 Sol, "official"
    harness, per blog-openai-gpt56-ga-announcement.md):           7.78%

Combined effect at max reasoning effort: ~3x score, 6x fewer output tokens.

Rolling truncation threshold (official harness): 175,000 characters —
oldest messages discarded once exceeded.

Recommended developer settings (verbatim list):
  - Use our Responses API, not our legacy Chat Completions API
  - Retain reasoning
  - Use compaction
```

```
Source: OpenAI Developers, "Compaction" guide,
https://developers.openai.com/api/docs/guides/compaction — the mechanism
named as "compaction" in the ARC-AGI-3 article. Python example, trimmed:

conversation = [
    {"type": "message", "role": "user", "content": "Let's begin a long coding task."}
]

while keep_going:
    response = client.responses.create(
        model="gpt-5.3-codex",
        input=conversation,
        store=False,
        context_management=[{"type": "compaction", "compact_threshold": 200000}],
    )
    conversation.extend(response.output)
    conversation.append({"type": "message", "role": "user", "content": get_next_user_input()})
```

```
Source: ARC-AGI-3 Docs, "ARC-AGI-3 Scoring Methodology,"
https://docs.arcprize.org/methodology

Per-level scoring examples (human baseline = 10 actions):
  AI takes 10 actions  -> level score 1.0  (100%)
  AI takes 20 actions  -> level score 0.25 (25%)
  AI takes 100 actions -> level score 0.01 (1%)
Per-level score capped at 1.15x human baseline.
Per-game score: weighted average of per-level scores, weighted by
  1-indexed level number (later/harder levels count more).
Total score: average of all game scores.
```

## Cross-References

- **Corroborates**:
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1
    ("coding agent = AI model(s) + harness," most failures attributed to
    the model are actually harness/configuration problems) — this article
    is a sharply quantified, vendor-side example of exactly this thesis: a
    3x score swing on the same model weights, driven entirely by two API
    configuration settings. It also corroborates that note's Claim 10 (a
    28-position benchmark ranking swing for the same model across
    harnesses, attributed secondhand to "Viv"/Terminal Bench 2.0 and
    flagged there as unverified) with an independently-sourced, directly
    quoted, first-party number — this article is stronger evidence for the
    same underlying "harness configuration can dominate benchmark outcomes"
    claim than the secondhand citation that note had to flag as unverified.
  - `research-wasnotwas-context-compaction.md` Claim 3 (six of seven
    open-source coding-agent harnesses use lossy LLM-summary compaction)
    and Claim 6 (OpenHands' reversible event-store as a counterexample
    showing lossy compaction is a design choice, not a technical
    necessity) — this article's compaction mechanism (Claim 13: an opaque,
    encrypted, server-generated state item, not an LLM-written text
    summary) is a third distinct compaction architecture beyond the two
    that note catalogs, reinforcing that note's point that "compaction" is
    not one algorithm.
- **Contradicts**: None identified. No existing source note claims that
  discarding reasoning between turns or rolling truncation is beneficial or
  neutral for agent/benchmark performance; this article's claims are
  consistent in direction with the corpus's existing "recent context and
  reasoning state are load-bearing" theme (e.g.
  `research-wasnotwas-context-compaction.md` Claim 5 on Claude Code
  re-injecting recently-read files after compaction). No contradiction
  issue filed per MINER.md §4a.
- **Extends**: `blog-openai-gpt56-ga-announcement.md` — that note's Claim 4
  and Concrete Artifacts (ABSTRACT REASONING table) report GPT‑5.6 Sol at
  7.78% on ARC-AGI-3 under OpenAI's standard vendor benchmark table, with
  no methodology detail beyond a footnote. This article is, in effect, an
  explanation of that very number: OpenAI's own account is that the
  "official harness" (used for the 7.8%/13.3%-class score reported in
  Claim 1 and Claim 3 here) discards reasoning and truncates context, and
  the same model reaches roughly 3x that score with two Responses API
  settings changed. Any future citation of that note's ARC-AGI-3 table row
  should carry the caveat that the figure reflects a specific (harness-
  limited) configuration, not GPT‑5.6 Sol's demonstrated ceiling on this
  benchmark.
- **Novel**: The specific, quantified case study of reasoning-discarding
  plus rolling truncation cutting a flagship model's benchmark score by
  roughly two-thirds (Claims 1-8) is new to the corpus — no existing note
  isolates and measures this exact failure mode with before/after numbers
  on a named public benchmark. Also novel: the RHAE scoring methodology
  detail (Claim 14) and the specific mechanics of Responses API server-side
  compaction as an opaque encrypted continuation token (Claim 13), neither
  previously documented in the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering — harness settings as a first-class
  performance lever)**: Add Claims 2-3 and 8 (13.3% → 38.3% RHAE, 3x score,
  6x fewer output tokens, from two configuration settings alone) as the
  corpus's sharpest quantified example that context/reasoning retention
  settings can matter more than anything about the model itself. Pair with
  `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1 as the
  practitioner framing this vendor case study substantiates.
- **Chapter 04 (Compaction mechanisms — not one algorithm)**: Add Claim 13
  (Responses API's opaque, encrypted, server-generated compaction item) as
  a named, distinct compaction architecture alongside the LLM-summarization
  pattern documented in `research-wasnotwas-context-compaction.md` — the
  guide should not describe "compaction" as a single technique without
  noting vendors implement it differently (summarize-and-replace vs.
  opaque state checkpoint).
- **Chapter 03 (Model Selection — Benchmark Interpretation)**: Add a caveat
  to any citation of `blog-openai-gpt56-ga-announcement.md`'s ARC-AGI-3
  table row (Sol 7.78%): per this article, that figure reflects a specific
  harness configuration (reasoning discarded, rolling truncation) that
  OpenAI itself later showed suppresses the same model's score by roughly
  a factor of 3. This sharpens the existing "no single benchmark score
  is model-only" guidance (already present via the GPT‑5.6 GA note's
  Cross-References) with a documented, quantified mechanism rather than a
  general caution.
- **Chapter 04 (Reasoning retention across turns)**: Add Claim 6 (retained
  reasoning reduces per-action thinking time and improves multi-turn
  strategic coherence) and Claim 11 (Responses vs. Chat Completions,
  +5% TAUBench from reasoning retention alone) as concrete evidence for
  preferring stateful/reasoning-preserving API configurations in
  long-horizon agentic tasks, distinct from the compaction-specific
  guidance above.

## Extraction Notes

- **Primary URL blocked; retrieved via reader proxy.** The live URL
  (`https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores`)
  returned HTTP 403 to both `WebFetch` and a direct `curl` with a browser
  user-agent — the same `openai.com/index/` access pattern already
  documented in this corpus's Extraction Notes for
  `blog-openai-gpt56-ga-announcement.md` and
  `blog-openai-chatgpt-work-ambitious-partner.md`. Unlike those notes, this
  extraction did not use the Wayback Machine (that tool returned an
  explicit "unable to fetch from web.archive.org" error in this session);
  instead the article was retrieved successfully (HTTP 200) via the
  `r.jina.ai` reader proxy, which returns a linearized Markdown transcript
  of the rendered page. The full article is short (roughly 700 words); it
  was read in its entirety, and all quotes above were checked against that
  transcript verbatim, with embedded "(opens in a new window)" link-
  affordance annotations (an artifact of the reader proxy's link handling,
  not part of the source's visible text) stripped from quoted passages.
- **Followed 3 linked sub-pages**, all fetched successfully via the same
  reader proxy: the "Why we built the Responses API" developer blog post
  (source of Claims 11-12, the mechanism behind "retained reasoning"), the
  "Compaction" API guide (source of Claim 13, the mechanism behind
  "compaction"), and the ARC-AGI-3 scoring methodology docs (source of
  Claim 14, the definition of the RHAE metric used throughout the primary
  article's score comparisons). Not followed: the cycle-double-cover-
  conjecture PDF (an unrelated math-proof artifact, no relevance to the
  harness/settings claims being extracted), the embedded Ethan Mollick
  X/Twitter post (a social-media embed, not a substantive linked page), and
  the Hugging Face gameplay-logs dataset link (raw data, not prose to
  extract claims from).
- **No ablation of the two settings individually.** The article reports
  the 13.3%→38.3% and 3x/6x figures only for the combined
  retained-reasoning-plus-compaction condition (plus qualitative,
  non-numeric before/after observations for reasoning retention alone in
  Claim 6). No isolated "compaction only" or "retained reasoning only"
  intermediate score is given anywhere in the source; this is noted
  explicitly in Claim 6's and Claim 7's assessments rather than inferred.
- **Confidence-overall set to `emerging`**: a first-party engineering
  account with precise, specific before/after numbers and a clearly stated
  mechanism, but self-reported by the same lab whose product is being
  evaluated, on a single model family and benchmark, with no independent
  third-party reproduction of the RHAE figures found during this
  extraction.
- No contradiction with an existing source note was identified; see
  Cross-References → Contradicts.
