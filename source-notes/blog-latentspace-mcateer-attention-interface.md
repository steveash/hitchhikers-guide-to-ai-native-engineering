---
source_url: https://www.latent.space/p/attention-interface
source_type: blog-post
title: "The Evolution of the Agent Harness"
author: Dan McAteer (guest contributor, Latent Space)
date_published: 2026-08-22
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3328"
---

# The Evolution of the Agent Harness

> Dan McAteer's macro-history and predictive framework for agent-harness
> evolution: a three-stage "Bolt-On Era → Co-Training Era → Attention Era"
> progression, backed by a quantified "gap" model of harness effectiveness,
> the Harness-Bench 23.8-point same-model spread, OpenAI's ARC-AGI-3 tripling,
> and Anthropic's 80% Claude Code system-prompt deletion — concluding that as
> models absorb harness capability into their weights, the harness's
> remaining job becomes managing human attention rather than model capability.

## Source Context

- **Type**: blog-post (guest essay on Latent Space, Shawn "swyx" Wang's
  publication; a `trusted-feed` source per this repo's scanning
  configuration). Published 2026-08-22T07:30:52Z per the page's embedded
  `datePublished` metadata.
- **Author credibility**: Dan McAteer is a guest contributor to Latent Space,
  not a Latent Space staff writer. His own contributor bio, pulled directly
  from the page: "AI writer and agentic engineer. I write Attention Heads,
  exploring what's worth paying attention to as intelligence becomes
  abundant and human attention grows scarce. Contributor @ Latent.Space."
  He is not a named engineer at Anthropic, OpenAI, or any harness vendor —
  this is an outside analyst's synthesis essay, not first-party engineering
  testimony. Its evidentiary strength comes from the specific, checkable
  data points it cites from named primary sources (Harness-Bench, OpenAI's
  ARC-AGI-3 post, Thariq Shihipar's system-prompt figure, a named podcast
  quote from Lukasz Kaiser) rather than from the author's own authority.
  Being carried on a `trusted-feed` publication means it passed the
  "is this worth listening to" bar at triage, not that its claims are
  first-party verified.
- **Scope**: Covers the full essay from introduction through conclusion — a
  single continuous argument with five named sections ("What a Harness
  Actually Is," "Harness 1.0: The Past, 'The Bolt-On Era,'" "Harness 2.0: The
  Present, 'The Co-Training Era,'" "Harness 3.0: The Future, 'The Attention
  Era,'" "The Attention-Interface"). Does NOT cover: any original research,
  benchmark, or data collection by the author — every specific number in
  the piece (Harness-Bench spread, ARC-AGI-3 tripling, Claude Code's 80%
  system-prompt cut, Answer.AI's Devin test, the compounding-reliability
  arithmetic) is either a citation of someone else's reported result or the
  author's own back-of-envelope calculation, not new measurement. No images
  in the piece carry alt text or captions with additional data beyond the
  prose (checked directly in the fetched HTML).

## Extracted Claims

### Claim 1: An agent harness is defined as everything besides the model weights that makes the agent work — environment, tools, context, and guardrails — without which the model is confined to its training data and the prompt it's given
- **Evidence**: The article's own definitional framing, stated early and used as the organizing concept for the rest of the essay; illustrated by the "brain in a vat" image applied to original (November 2022) ChatGPT.
- **Confidence**: settled (a definitional framing broadly consistent with how the rest of this corpus already uses the term)
- **Quote**: "An agent harness is everything besides the model weights that makes the agent work. The environment, tools, context and guardrails that surround the model. Without the harness the model is a brain in a vat."
- **Our assessment**: This definition is materially narrower in wording but functionally equivalent to Lilian Weng's more clinical framing in `blog-lilianweng-harness-engineering-rsi.md` Claim 1 ("the system surrounding a base model that orchestrates execution and decides how the model thinks and plans, calls tools and acts, perceives and manages context, stores artifacts, and evaluates results") — both exclude the model weights themselves and include tools/context/guardrails as the harness's substance. McAteer's version is written for a practitioner audience and pairs the definition with a body metaphor ("the harness gave the brain a body") that recurs through the rest of the essay as its central image.

### Claim 2: The tangible jump in agent usefulness around Christmas 2025 was the confluence of the model-capability curve and the harness-capability curve improving together and crossing at the right moment — not a discrete model release or a discrete harness release alone
- **Evidence**: The article's central thesis statement, immediately following the framing question ("why did agents start working around Christmas 2025?").
- **Confidence**: emerging (an explicit interpretive thesis argued through the rest of the piece via supporting data points, not itself a single measured finding)
- **Quote**: "What I'll argue in this post is that it was the confluence of the last two. The model and the harness improving together and then their curves of improvement crossing at the right moment."
- **Our assessment**: This is the load-bearing interpretive claim the rest of the essay's historical narrative (Claims 4-8) and quantified evidence (Claims 9-10) are marshaled to support. It is explicitly corroborated by a named, quoted third party (Claim 3, Lukasz Kaiser) rather than resting on the author's authority alone.

### Claim 3: Lukasz Kaiser (a co-inventor of the Transformer) stated on the "Unsupervised Learning" podcast in June 2026 that the "big jump" in agent capability last Christmas is hard to attribute to any single cause — harness changes, post-training changes, and new pre-trained models all arrived around the same time
- **Evidence**: A direct quote attributed by name to a named individual on a named podcast, used by the author as external corroboration for Claim 2.
- **Confidence**: anecdotal (a single named individual's recollection on a podcast, relayed secondhand by this essay rather than independently verified by this Miner against the original podcast episode)
- **Quote**: "The change last winter, last Christmas — it's a little hard to pin down. I mean, the harness changed and a little post-training changed and then new pre-trained models came… but it felt like a big jump which is not that easy to pin down what did it."
- **Our assessment**: This quote is doing real evidentiary work in the essay — it is the only named-individual, on-record testimony (as opposed to author argument or vendor benchmark) supporting the "confluence, not a single cause" thesis. Its confidence should be read as "one credible person's recollection," not as an independently measured event; this Miner did not independently verify the quote against the original "Unsupervised Learning" episode.

### Claim 4: The Bolt-On Era's first three stages (ReAct, AutoGPT/BabyAGI, Cursor/Copilot) trace a gap between "what the harness asks of the model" and "what the model can deliver" that starts near zero, widens catastrophically, then gets pulled back down by retreating to human-in-the-loop design
- **Evidence**: A three-part historical narrative with named systems, dates, and a stated causal mechanism for each stage's design choice.
- **Confidence**: emerging (a historical narrative organized around named, real releases and dates, but the "gap" framing itself is the author's own interpretive model, not a measured quantity)
- **Quote**: "ReAct...defines the idea of an 'agent loop' where a model reasons -> acts -> observes -> repeats...Prompting is the only reasoning method that exists at this time and no one calls it a 'harness.'" / "With AutoGPT/BabyAGI, the harness curve sprints ahead of the model capability curve...A loop doesn't add capability to a model. A loop amplifies the capability a model has, and below some threshold the loop amplifies errors rather than reliability." / "The first AI-powered IDEs recognize the failure-mode of giving the model too much autonomy. They close the gap by pulling the harness curve down below the model curve."
- **Our assessment**: The specific dates given (ReAct, October 2022; AutoGPT/BabyAGI, Spring 2023; Cursor/Copilot, 2023-2024) are checkable against public release history and are consistent with the well-known timeline of these tools; this Miner did not independently re-verify each date against primary sources. The "gap" framing (harness demand vs. model capability, and the effectiveness of an agent as the size of the gap) is the essay's own conceptual device and is not attributed to any external source — it should be treated as McAteer's synthesis, not a cited finding.

### Claim 5: A 95%-per-step reliability rate compounded over a 20-step task yields roughly a 36% average success rate, illustrating why handing an unreliable model full autonomy (as AutoGPT/BabyAGI did) amplifies errors rather than producing reliable task completion
- **Evidence**: A stated arithmetic illustration (0.95^20 ≈ 0.358) offered as the mechanism explanation for why "premature autonomy" failed in Spring 2023.
- **Confidence**: settled (a straightforward, independently checkable calculation: 0.95^20 = 0.3585..., consistent with the "~36%" figure given)
- **Quote**: "Consider the power of compounding in the negative: 95% reliability per-step over a 20-step task results in a ~36% average success rate."
- **Our assessment**: This is a clean, verifiable illustration of compounding-error math applied specifically to agent loop reliability, and it is a useful, quotable mental model for why per-step reliability matters disproportionately in long-horizon agentic tasks — a small per-step error rate that looks acceptable in isolation becomes catastrophic at 15-20+ steps. Novel to the corpus as a named illustration (see Cross-References).

### Claim 6: A test from the Answer.AI team found the first version of Devin succeeded at roughly a 15% rate when given full autonomy, corroborating that the industry's mid-2023–2024 retreat to human-in-the-loop tooling (Cursor, Copilot) was the technically correct move rather than excessive caution
- **Evidence**: A specific, named third-party test result cited as evidence that full-autonomy coding agents were not yet viable at that capability level.
- **Confidence**: anecdotal (a specific numeric figure attributed to a named organization's test, but relayed without a link to, or further methodology detail from, the original Answer.AI test in the recovered article text; not independently verified by this Miner)
- **Quote**: "The first version of Devin tries to hand the autonomy back to the model. A test from the team at Answer.AI shows that is still premature, with a ~15% success rate. It's evidence that the move from the IDEs to retreat from full autonomy is not cowardly, but the correct move."
- **Our assessment**: This is a specific, falsifiable claim (a named team, a named product, an approximate percentage) but this Miner could not locate the original Answer.AI test to verify the ~15% figure or its task set/methodology from the article text alone — treat as an unverified secondhand citation pending independent confirmation, similar in evidentiary weight to other secondhand benchmark citations flagged elsewhere in this corpus (e.g., the Terminal Bench 2.0 ranking-swing citation flagged in `blog-humanlayer-skill-issue-harness-engineering.md` Claim 10).

### Claim 7: Claude Code (February 2025) was the first coding agent to succeed at full model autonomy not because it was first to attempt it, but because it launched at the crossover point where the model had become reliable enough to be handed the loop — and grew to roughly $1B ARR within six months
- **Evidence**: Direct narrative claim tying Claude Code's specific design choices (terminal instead of IDE, bash/file access, permission rules instead of per-change approval) to a timing argument, with a named revenue figure as the outcome measure.
- **Confidence**: emerging (the $1B ARR figure and the "built with the next model's capabilities in mind" framing are specific and checkable claims, though this article does not cite an external source for either — they read as the author's own synthesis of public reporting, not a footnoted citation)
- **Quote**: "It abandons the IDE for the terminal, gives the model bash and file read/write access, and replaces the need for human approval on every change with permission rules...Boris Cherny and team build Claude Code with the next model's capabilities in mind, not the current one...Claude Code grows to roughly $1B ARR within six months, all because Anthropic seized the opportunity available when the curves begin to meet."
- **Our assessment**: The design-choice description (terminal over IDE, bash/file access, permission rules) is consistent with widely reported Claude Code architecture already documented elsewhere in this corpus (e.g. `blog-anthropic-agent-view-claude-code.md`). The "~$1B ARR within six months" figure and the "built for the next model" framing are presented without an inline citation in the source article itself; this Miner did not find independent corroboration for the exact ARR figure elsewhere in the corpus and flags it as an unverified secondhand claim.

### Claim 8: Harness-Bench ran the same model across the same 106 tasks under different harness configurations and observed scores ranging from 52.4 to 76.2 — a 23.8-point spread attributable entirely to harness changes with zero change to the model
- **Evidence**: A specific, named benchmark with a specific task count and a specific score range, offered as the article's primary quantified evidence that "the harness matters, and in a way we can measure."
- **Confidence**: emerging (a specific, checkable benchmark result attributed by name, but this Miner could not locate independent documentation of "Harness-Bench" elsewhere in this corpus or verify its methodology beyond what this article states; treat as a single-source citation)
- **Quote**: "Harness-Bench ran the same model over the same 106 tasks in different harnesses, and scores ranged from 52.4 to 76.2: a 23.8-point spread with zero change to the model. Half the agent is the harness."
- **Our assessment**: This is the single most load-bearing quantified data point in the essay — a same-model, same-task, harness-only score swing of nearly 24 points is a dramatic illustration of harness-as-performance-lever. It is directionally identical to, and of comparable or larger magnitude than, the corpus's existing best quantified example of this same phenomenon: `blog-openai-arc-agi-3-two-settings.md` Claim 2 (same GPT-5.6 Sol model weights, two Responses API settings changed, score roughly tripled from 13.3% to 38.3% RHAE). Harness-Bench itself is novel to this corpus and was not independently verified by this Miner (no benchmark leaderboard, paper, or methodology page for "Harness-Bench" was located during this extraction) — cite it as reported, not as independently confirmed.

### Claim 9: OpenAI achieved a comparable harness-only result on ARC-AGI-3: enabling retained reasoning and compaction (with no model change) tripled GPT-5.6 Sol's score from 13.3% to 38.3%
- **Evidence**: A specific, named result attributed to OpenAI, offered immediately after the Harness-Bench citation as a second, corroborating quantified example of harness-driven performance gains.
- **Confidence**: settled (this specific claim is independently, directly corroborated by a primary source already in this corpus — see Cross-References)
- **Quote**: "OpenAI achieved a similar result on ARC-AGI-3 with harness changes. Adding only retained reasoning and compaction, GPT-5.6 Sol's ARC-AGI-3 score tripled from 13.3% to 38.3%."
- **Our assessment**: Unlike Harness-Bench (Claim 8), this specific claim is independently verifiable and is in fact already documented first-party in this corpus: `blog-openai-arc-agi-3-two-settings.md` Claim 3 gives the identical figures ("With the official harness, GPT‑5.6 Sol scored 13.3% on the ARC-AGI-3 public set. With retained reasoning and compaction, it scored 38.3%.") from OpenAI's own engineering write-up. This is the strongest-evidenced individual data point in McAteer's essay because it is checkable against a primary source, not merely cited secondhand.

### Claim 10: Reinforcement learning has moved inside the harness — OpenAI's own codex-1 release announcement (May 2025) states the model "was trained using reinforcement learning on real-world coding tasks in a variety of environments," which the author reads as Toolformer's 2023 vision (tool use trained in, not prompted) finally manifesting in production
- **Evidence**: A direct quote attributed to OpenAI's codex-1 release announcement, paired with the author's own interpretive framing linking it back to the earlier Toolformer reference (Claim 4).
- **Confidence**: emerging (the quote is attributed to a specific, named vendor announcement; this Miner did not independently locate and re-verify the original codex-1 announcement text, so the quote is reproduced as relayed by this essay, not independently confirmed character-for-character against OpenAI's own page)
- **Quote**: "codex-1 was trained using reinforcement learning on real-world coding tasks in a variety of environments."
- **Our assessment**: This is a specific, named claim about training methodology (RL inside the harness's own task distribution, not prompted-in tool use) that is structurally consistent with, though not identical to, the broader "harness-code as an optimizable/trainable object" theme documented at much greater technical depth in `blog-lilianweng-harness-engineering-rsi.md` (e.g. Claim 2's five-stage optimization-target progression, which places "harness code" and "optimizer code" as later stages beyond prompts/context/workflow). McAteer's essay treats this as evidence that the model/harness boundary is dissolving; Weng's essay treats the same underlying phenomenon as a research literature with named papers and named authors. The two sources corroborate the same directional trend from different vantage points (practitioner-essay synthesis vs. research-literature review).

### Claim 11: Once a model absorbs a harness capability into its weights through training, the harness sheds the now-redundant scaffolding — Anthropic's Thariq Shihipar reported the team recently deleted 80% of Claude Code's system prompt, and the author frames the pace of this deletion as the actual measure of harness-evolution progress ("production by reduction")
- **Evidence**: A specific, named percentage attributed to a specific, named Anthropic engineer, paired with the author's own framing of deletion velocity as the field's real progress metric.
- **Confidence**: settled (the underlying 80% figure is independently, directly corroborated by a primary transcript source already in this corpus — see Cross-References; the "production by reduction" framing itself is the author's own synthesis)
- **Quote**: "GPT-5.1-Codex-Max launch: 'The first model natively trained to operate across multiple context windows through compaction.' Once the models absorb the harness capabilities, the harness can shed the scaffold. It's production by reduction. Thariq Shihipar from Anthropic said that the team recently deleted 80% of Claude Code's system prompt. The measure of the pace of agent harness evolution is how much of the harness you get to delete, while retaining the same capability level."
- **Our assessment**: The 80% figure is independently corroborated, with substantially more precision and qualification, by `blog-simonwillison-cat-thariq-fireside-chat.md` Claim 2 (Thariq Shihipar's direct, on-record statement: "the Claude Code system prompt was reduced by 80% for frontier models, chiefly by removing examples") and Claim 4 (the reduction applies only to the most frontier models — older/cheaper models still get the full prompt; "It's only our most frontier models that have this 80% token decrease — the older models still have the full system prompt"). McAteer's essay states the 80% figure without that per-model-tier qualifier, which is a simplification but not a misstatement — the underlying fact is directly verified. The "production by reduction" framing (deletion-while-retaining-capability as the real progress metric) is a distinct, memorable heuristic not present in the fireside-chat note, and is a genuinely useful addition to the corpus's harness-pruning material alongside `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 ("What can I stop doing?").

### Claim 12: The model/harness co-evolution loop is: train inside the harness → absorb the harness's capability into the weights → shed the now-redundant harness scaffolding → repeat, with each cycle the model climbing to the next capability it doesn't yet have
- **Evidence**: The author's own stated summary of the mechanism argued through Claims 9-11, offered as the essay's explanation for why the "jump last Winter" (Claim 3, Kaiser's quote) is hard to pin down to a single event.
- **Confidence**: emerging (a synthesizing framework built on the specific data points in Claims 8-11, not itself an independently measured or cited finding)
- **Quote**: "This, then, is the loop of model / harness evolution: train -> absorb -> shed -> repeat. The model climbs to the next thing it can't do yet." / "The jump that Kaiser pointed out is hard to pin down because it's not a discrete event...it happened in the space between the model and harness working together."
- **Our assessment**: This is the essay's central organizing mechanism, synthesizing the preceding evidence into a named repeatable cycle. It is a genuinely novel framing for this corpus's harness-engineering material — the "train → absorb → shed → repeat" loop names the process by which harness components go stale (already documented via `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 and `blog-anthropic-harness-long-running.md` Claim 9) as a *cause and effect cycle* rather than a static pruning checklist.

### Claim 13: As models absorb the computer-facing capabilities of the harness (multi-agent orchestration, tool selection, memory), what remains un-absorbable is the human-centric layer — permissions, identity, trust, and legibility — and the author argues absorption does not end the harness but inverts it: the harness becomes the agent's interface to the human who operates it, not the human's interface to the model
- **Evidence**: The article's central forward-looking thesis for the "Attention Era" section, stated as a direct claim with no external citation (this is explicitly the author's own prediction, not a reported finding).
- **Confidence**: anecdotal (an explicit, self-identified prediction by the author — "I predict" appears in the following section — not a measured or cited finding; the underlying premise that permissions/identity/trust "cannot be absorbed" is asserted, not demonstrated)
- **Quote**: "What's left at the end of this deletion and absorption process are the human-centric agent capabilities. Things like permissions, identity, trust and legibility. A model that absorbs permissions into itself has dissolved permissions. Absorption doesn't end the harness. Absorption inverts the harness. The harness becomes the agent's interface to the human that operates it."
- **Our assessment**: This is the essay's most speculative and most novel claim, and the one with the least direct evidentiary support of any claim extracted from this source — it is explicitly forward-looking rather than a report of something already observed. It is, however, thematically well-aligned with concrete permission/identity architecture already documented first-party in this corpus: `blog-anthropic-agent-identity-access-model.md` (Anthropic's own agent-identity access model for Claude Tag, replacing "what can this user do?" with "what can this agent do?" — that note's Claim 4) is a live, shipped example of exactly the kind of human-centric, non-absorbable harness layer McAteer's essay predicts will remain load-bearing. The guide should present this claim as a plausible, well-reasoned but unproven forecast, not as an established fact.

### Claim 14: The author predicts that within a year, every company building agentic AI will ship a human "attention policy surface" — an "attention-interface" analogous to how every agentic AI company shipped an AGENTS.md — governing when an agent may interrupt a human, when it should keep working, and which decisions it can make alone versus needing approval
- **Evidence**: An explicit, self-identified prediction (the article's closing thesis), drawing an analogy to the AGENTS.md convention already widespread across coding-agent products.
- **Confidence**: anecdotal (an explicit, hedged forecast by the author with a specific one-year time horizon; not a report of an already-shipped pattern, though the author cites two named examples as early "sparks")
- **Quote**: "I predict that within a year, every company building agentic AI will ship a human attention policy surface in the way that every agentic AI company shipped AGENTS.md. AGENTS.md tells the agent how to work with your codebase. The attention-interface will tell the agent how to work with you. It will govern when it's allowed to interrupt you, when it should keep working, which decisions it can make alone and which decisions need your approval."
- **Our assessment**: This is a specific, falsifiable, dated prediction (checkable in approximately one year from the August 2026 publication date) rather than a description of current practice — the guide should flag it explicitly as a forecast, not cite it as an established pattern. The author's own supporting evidence for "sparks of this already" is thin in the source text itself — a single unelaborated sentence naming "Anthropic's long-running agent progress files and agentic approval queues" with no further detail, benchmark, or citation. This Miner did not find a corpus source note documenting either of those two named examples in enough depth to treat them as independent corroboration; they are noted here as the author's own (unverified) supporting evidence, not as separately confirmed facts.

### Claim 15: Ryan Lopopolo stated on the "Extreme Harness Engineering for Token Billionaires" episode of Latent Space that "the only fundamentally scarce thing is the synchronous human attention of my team," which the author uses to argue that as tokens became abundant and reliable, human attention remained the true bottleneck
- **Evidence**: A direct quote attributed to a named individual on a named podcast episode, used as supporting testimony for the essay's closing "scarce resource" framing.
- **Confidence**: anecdotal (a single named individual's quoted opinion on a podcast, relayed secondhand by this essay; this Miner did not independently verify the quote against the original episode)
- **Quote**: "The only fundamentally scarce thing is the synchronous human attention of my team."
- **Our assessment**: This quote supplies the essay's title concept and its closing image ("The interface to the one true scarce resource: human attention") — it functions as the rhetorical anchor for Claims 13-14 rather than as independent evidence for them. Worth flagging for the guide as a quotable framing rather than as a data point.

## Concrete Artifacts

### The three-stage harness-evolution model, as named and dated in the article

```
Source: Dan McAteer, "The Evolution of the Agent Harness," Latent Space,
published 2026-08-22 (https://www.latent.space/p/attention-interface)

Harness 1.0 — "The Bolt-On Era" (the past):
  ReAct, "The Harness on Paper"        (October 2022)
  AutoGPT/BabyAGI, "Premature Autonomy" (Spring 2023)
  Cursor/Copilot, "Retreat to Human in the Loop" (2023-2024)
  Claude Code, "The Curves Cross"       (February 2025)

Harness 2.0 — "The Co-Training Era" (the present):
  RL moves inside the harness; models absorb harness capabilities into
  weights; harness sheds redundant scaffolding ("production by reduction").
  Loop: train -> absorb -> shed -> repeat.

Harness 3.0 — "The Attention Era" (the predicted future):
  Human-centric capabilities (permissions, identity, trust, legibility)
  are what remains un-absorbable. The harness inverts from "human's
  interface to the model" to "model's interface to human attention" —
  the "attention-interface."
```

### Quantified evidence cited in the article

```
Source: Dan McAteer, "The Evolution of the Agent Harness," Latent Space,
2026-08-22

Compounding reliability math (author's own illustration):
  95% reliability/step over 20 steps -> ~36% average success rate
  (0.95^20 ≈ 0.3585, independently verifiable)

Answer.AI test of first-version Devin (full autonomy): ~15% success rate
  (secondhand citation; original test not independently located by this
  Miner)

Claude Code: ~$1B ARR within six months of February 2025 launch
  (stated without inline citation in the source article)

Harness-Bench: same model, same 106 tasks, different harnesses
  Score range: 52.4 to 76.2 (a 23.8-point spread, zero model change)
  (novel to this corpus; not independently located/verified by this Miner)

OpenAI ARC-AGI-3 (GPT-5.6 Sol), harness-only change (retained reasoning +
compaction, no model change):
  13.3% -> 38.3% ("tripled")
  (independently corroborated first-party — see Cross-References)

Claude Code system prompt reduction (attributed to Thariq Shihipar,
Anthropic): 80% size reduction
  (independently corroborated first-party, with the added qualifier that
  this applies only to frontier-tier models — see Cross-References)
```

### Key quotes attributed to named third parties

```
Source: Dan McAteer, "The Evolution of the Agent Harness," Latent Space,
2026-08-22

Lukasz Kaiser (Transformer co-inventor), "Unsupervised Learning" podcast,
June 2026:
  "The change last winter, last Christmas — it's a little hard to pin
  down. I mean, the harness changed and a little post-training changed
  and then new pre-trained models came… but it felt like a big jump
  which is not that easy to pin down what did it."

OpenAI, codex-1 release announcement, May 2025:
  "codex-1 was trained using reinforcement learning on real-world coding
  tasks in a variety of environments."

OpenAI, GPT-5.1-Codex-Max launch:
  "The first model natively trained to operate across multiple context
  windows through compaction."

Ryan Lopopolo, "Extreme Harness Engineering for Token Billionaires"
episode, Latent Space:
  "The only fundamentally scarce thing is the synchronous human attention
  of my team."
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `blog-openai-arc-agi-3-two-settings.md` Claim 3 (13.3% -> 38.3% RHAE
    on ARC-AGI-3 via retained reasoning + compaction, zero model change) —
    this is a direct, primary-source confirmation of Claim 9 here. The
    figures match exactly, giving this specific claim in McAteer's essay
    the strongest evidentiary backing of any single data point extracted
    from this source.
  - `blog-simonwillison-cat-thariq-fireside-chat.md` Claim 2 (Thariq
    Shihipar's on-record statement that the Claude Code system prompt was
    reduced 80% for frontier models, chiefly by removing examples) and
    Claim 4 (the 80% reduction applies only to the most frontier
    model tier; older models retain the full prompt) — this directly
    corroborates and adds precision to Claim 11 here. McAteer's essay
    states the 80% figure without the per-model-tier qualifier that the
    fireside-chat transcript makes explicit.
  - `blog-lilianweng-harness-engineering-rsi.md` Claim 1 (harness defined
    as the orchestration layer distinct from model weights) and Claim 5
    (the near-term path to model/harness convergence is unlikely to be a
    model directly rewriting its own weights; instead the object being
    optimized migrates up a level of abstraction, using the
    prompt-engineering-didn't-disappear-it-moved-up analogy) — Claim 1
    here (McAteer's harness definition) is functionally consistent with
    Weng's more technical framing, and Claim 12 here (the
    train->absorb->shed->repeat loop) is a third, independently-arrived-at
    position in the same "will models absorb their own harnesses" debate
    that Weng's Claim 5 and `blog-langchain-harness-memory.md` Claim 2
    (Harrison Chase: an agent, by definition, always needs a surrounding
    system) already stake out two other positions on. McAteer's version
    is the most concrete of the three: it names a specific repeatable
    mechanism (train, absorb, shed) rather than arguing from definition
    (Chase) or analogy alone (Weng).
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 ("What can
    I stop doing?" as the review heuristic at each model upgrade, with the
    context-anxiety-resets-become-dead-weight example) — corroborates the
    same underlying pruning phenomenon that Claim 11 here names
    "production by reduction." McAteer's framing adds a specific measure
    (how much you can delete while retaining capability = the actual pace
    metric of harness evolution) that is a sharper, more quotable version
    of the same idea.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1 ("coding
    agent = AI model(s) + harness," most failures attributed to the model
    are actually harness/configuration problems) — corroborates the
    general "harness matters as much as the model" thesis underlying
    Claim 8 here (Harness-Bench's 23.8-point same-model spread).
  - `blog-anthropic-agent-identity-access-model.md` Claim 4 (Anthropic's
    shipped agent-identity model for Claude Tag replaces "what can this
    user do?" with "what can this agent do?") — a concrete, already-shipped
    example of the human-centric, non-absorbable harness layer (permissions
    and identity specifically) that Claim 13 here predicts will remain the
    harness's job after computer-facing capabilities are absorbed into the
    model.

- **Contradicts**: None identified. No claim in this source was found to
  materially oppose an existing corpus source note on the same specific
  question. Per MINER.md §4a, no contradiction issue was filed. (Note: this
  essay's "middle-tier models benefit most from harness-improvement effort"
  is NOT a claim McAteer makes — that finding belongs to
  `blog-lilianweng-harness-engineering-rsi.md` Claim 9 alone — so there is
  no tension to flag between the two sources on that specific point.)

- **Extends**:
  - `blog-anthropic-harness-long-running.md` Claim 9 (harness components
    encode assumptions about model limitations that go stale and should be
    pruned at each model upgrade) — Claim 12 here supplies a causal
    mechanism (train inside the harness -> absorb capability -> shed
    scaffolding) for *why* components go stale, rather than only
    documenting *that* they do.
  - `blog-latentspace-ainews-harness-drift-quantization.md` Claim 1 (stale
    `agents.md` instructions as "self-inflicted prompt injection") — both
    sources are concerned with harness content/scaffolding outliving its
    usefulness, but at different layers: that note is about instruction
    *content* becoming actively misleading, while this essay (Claims 11-12)
    is about harness *code/scaffolding* becoming redundant once the model
    absorbs the underlying capability. Complementary, not overlapping.

- **Novel**:
  - The three-stage "Bolt-On Era / Co-Training Era / Attention Era"
    naming and periodization (Claims 4, 8-14) is new vocabulary and a new
    organizing timeline for this corpus — no existing source note names
    or dates these three stages as a sequence.
  - The "gap" model of agent effectiveness (Claim 4: effectiveness = the
    gap between what the harness asks of the model and what the model can
    deliver, and the historical narrative of that gap widening then
    narrowing then inverting) is a novel explanatory framework.
  - Harness-Bench's specific 23.8-point same-model spread (Claim 8) is new
    to the corpus by name, though directionally corroborated by the
    independently-verified ARC-AGI-3 case (Claim 9).
  - The compounding-reliability arithmetic applied specifically to
    agent-loop autonomy timing (Claim 5) is a new, quotable illustration.
  - The "attention-interface" concept and the specific prediction that
    every agentic AI company will ship a human attention-policy surface
    within a year, by analogy to AGENTS.md (Claim 14), is entirely new to
    the corpus — no existing source note discusses a dedicated
    human-attention/interruption-policy artifact as a harness component.
  - The "production by reduction" framing — measuring harness-evolution
    progress by how much scaffolding can be deleted while capability is
    retained (Claim 11) — is a new, sharper name for a phenomenon the
    corpus already documents with less memorable framing.

## Guide Impact

- **Chapter 02 (Harness Engineering) / Chapter 04 (Model-Harness
  Co-evolution)**: Add the three-stage periodization (Bolt-On Era /
  Co-Training Era / Attention Era, Concrete Artifacts) as a narrative
  spine for a "how did we get here" section, anchored by the two
  independently-verified quantified data points (Claim 9's ARC-AGI-3
  tripling and Claim 11's Claude Code 80% system-prompt cut) rather than
  the unverified ones (Harness-Bench, the Answer.AI Devin test, the $1B
  ARR figure) — the guide should distinguish claims this Miner could
  verify against a primary source already in the corpus from claims
  relayed only secondhand by this essay.
- **Chapter 02 (Harness Engineering — pruning heuristics)**: Add Claim 11's
  "production by reduction" framing (measure harness-evolution pace by how
  much you can delete while retaining capability) alongside the existing
  "What can I stop doing?" heuristic from
  `blog-anthropic-harnessing-claude-intelligence.md` Claim 15 — these are
  two independently-phrased versions of the same practitioner discipline
  and pairing them strengthens the guide's pruning-as-practice section.
  Add Claim 12's train->absorb->shed->repeat loop as the causal
  explanation for why that pruning becomes necessary and recurring.
- **Chapter 05 (Team Adoption) / Chapter 06 (Security and Governance, if
  the guide has a permissions/trust section)**: Add Claims 13-14 (the
  "Attention Era" prediction and the specific "attention-interface"
  forecast) as a clearly-labeled speculative forecast, not established
  practice — paired with the concrete, already-shipped example in
  `blog-anthropic-agent-identity-access-model.md` (agent identity for
  Claude Tag) as evidence the underlying human-centric-permissions trend
  is real even though McAteer's specific "every company ships this within
  a year" prediction is unproven. Flag the one-year prediction as
  checkable and worth revisiting in a future mining pass (~August 2027).
- **Chapter 04 (Context Engineering)**: Add Claim 9 (ARC-AGI-3 tripling)
  as an additional citation pointing readers to the fuller primary-source
  treatment in `blog-openai-arc-agi-3-two-settings.md`, since this essay's
  framing (harness settings as a lever comparable in magnitude to model
  choice) is a useful practitioner-facing summary of that more detailed
  technical source.

## Extraction Notes

- **Fetch method**: The first `WebFetch` call against this URL returned
  only a short AI-generated summary and explicitly refused a follow-up
  request to reproduce the article verbatim, citing copyright concerns —
  the same limitation documented in this corpus's other Latent
  Space/Lil'Log extractions (e.g. `blog-lilianweng-harness-engineering-rsi.md`,
  `blog-latentspace-nathan-chatgpt-work-harness.md`). This post is not
  paywalled, so the full raw HTML was fetched directly via `curl` with a
  browser user-agent, the `<div class="body markup">` article body was
  isolated from the surrounding page chrome, and its HTML tags were
  stripped and entities decoded to plain text locally. All `Quote` fields
  above were copied character-for-character from that locally-extracted
  plain text.
- **Full article read in full**: The entire essay (introduction through
  the closing "attention-interface" paragraph) was read in full for this
  extraction, not sampled. No linked sub-pages were followed — the article
  references named external sources (the "Unsupervised Learning" podcast,
  OpenAI's codex-1 announcement, the "Extreme Harness Engineering for
  Token Billionaires" Latent Space episode, Harness-Bench, the Answer.AI
  Devin test) but does not hyperlink most of them inline in the fetched
  HTML, and this Miner did not independently search out and fetch each
  named external source separately — quotes and figures attributed to
  those sources are relayed as this essay states them, with confidence
  grades adjusted downward (anecdotal/emerging rather than settled) to
  reflect that lack of independent verification, per MINER.md's guidance
  to flag rather than silently resolve unverified secondhand citations.
  Two of this essay's cited figures (Claim 9, the ARC-AGI-3 tripling; and
  Claim 11, the Claude Code 80% system-prompt figure) happened to already
  have independent, first-party primary-source documentation elsewhere in
  this corpus, and those were re-verified directly against the cited
  source notes (not against the original OpenAI/Anthropic sources
  themselves, which those existing notes already verified).
- **No images carry additional text data**: checked the fetched HTML
  directly for `alt` attributes and `<figcaption>` elements within the
  article body; none were present, so no chart/diagram data was missed by
  extracting prose only.
- **Confidence-overall set to `emerging`**: this is an outside analyst's
  synthesis essay (not first-party engineering testimony) built from a mix
  of independently-verifiable claims (2 of the numeric claims are directly
  corroborated by primary sources already in this corpus), unverified
  secondhand citations (Harness-Bench, the Answer.AI test, the codex-1 and
  GPT-5.1-Codex-Max quotes, the Kaiser and Lopopolo podcast quotes), and
  explicit, self-labeled speculation about the future (the Attention Era
  and attention-interface predictions). The overall grade reflects that
  mixture rather than treating the essay as uniformly reliable or
  uniformly speculative.
- No contradiction with an existing source note was identified during
  cross-referencing; see Cross-References → Contradicts. No contradiction
  issue was filed per MINER.md §4a.
