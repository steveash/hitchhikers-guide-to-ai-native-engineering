---
source_url: https://www.deeplearning.ai/the-batch/issue-346/
source_type: blog-post
title: "The Batch Issue 346: Nvidia's Open Salvo, OpenAI's Amazon Deal, Grok Cuts Video Prices, Recursive Language Models"
author: DeepLearning.AI / Andrew Ng (editorial)
date_published: 2026-03-27
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#182"
---

# The Batch Issue 346: Nvidia Nemotron Super, OpenAI/AWS Agent Infrastructure, RLMs

> Weekly AI industry news roundup with two engineering-relevant sections: Nvidia Nemotron 3
> Super 120B's performance on PinchBench agentic tasks (442 tok/s, 85.6% agentic accuracy
> under permissive open weights) and the OpenAI/Amazon stateful agent runtime deal — the
> first major cloud-native managed agent state infrastructure announcement.

## Source Context

- **Type**: blog-post (weekly news digest; DeepLearning.AI's flagship newsletter)
- **Author credibility**: The Batch is Andrew Ng's weekly AI industry roundup. This issue
  contains factual reporting on announced products and business deals, not practitioner
  analysis. The Nemotron section is based on Nvidia's official benchmarks and published
  model specs; the OpenAI/AWS section is based on public announcements. Treat as reliable
  secondary reporting on primary sources, not first-party engineering documentation.
  Novelty is low per Prospector triage — this is a news digest, not a practitioner
  deep-dive.
- **Scope**: Covers five stories: (1) Nvidia Nemotron 3 Super 120B open-weights agentic
  model, (2) OpenAI/Amazon AWS stateful agent infrastructure deal, (3) xAI Grok Imagine
  1.0 video generator (primarily pricing/business, limited engineering signal), (4) MIT
  Recursive Language Models for long-context processing, (5) Andrew Ng editorial on AI
  policy (no engineering signal, not extracted). Extraction focuses on sections 1, 2,
  and 4 per Prospector guidance.

## Extracted Claims

### Claim 1: Nemotron 3 Super 120B achieves 442 output tokens/second — fastest in the 100B+ open-weights class

- **Evidence**: Nvidia's published benchmark comparison: gpt-oss-120b 278 tok/s, Google
  Gemini 3.1 Flash-Lite 266 tok/s, Nemotron 3 Super 442 tok/s. All measured at comparable
  serving configurations (third-party infrastructure; NVFP4 on Blackwell GPUs for Nemotron).
- **Confidence**: emerging (Nvidia first-party claim; independent infrastructure benchmarks
  can vary significantly by serving setup and hardware)
- **Quote**: "442 output tokens per second" (Nvidia's advertised throughput for this model
  at the Blackwell GPU native format)
- **Our assessment**: 442 tok/s is meaningful for agentic workloads where latency compounds
  across multi-step chains. A model running 1.6× faster than the nearest comparable open-
  weights alternative reduces wall-clock time for long-horizon agentic tasks proportionally.
  The caveat: these numbers assume Blackwell GPU access (Nvidia's newest generation). Teams
  without Blackwell hardware will see different figures. The training on NVFP4 (native to
  Blackwell) makes this model hardware-tied in a way that portable open-weights models
  typically are not.

### Claim 2: Nemotron 3 Super 120B scores 85.6% on PinchBench agentic tasks, outperforming Kimi K2.5 (84.8%) and GLM-5 (84.1%)

- **Evidence**: PinchBench is Nvidia's agentic evaluation benchmark. The comparison
  cohort (Kimi K2.5, GLM-5) is real — these are published frontier open-weights models.
  Numbers are from Nvidia's model card / announcement.
- **Confidence**: emerging (first-party benchmark on vendor's own eval; PinchBench is not
  widely reproduced by independent parties as of this writing)
- **Quote**: "PinchBench (agentic tasks): 85.6% outperforming Kimi K2.5 (84.8%) and
  GLM-5 (84.1%)"
- **Our assessment**: PinchBench is Nvidia's benchmark, so treat these numbers as
  promotional rather than independently validated. The margin over competitors is small
  (0.8–1.5 points), well within noise for model evals without confidence intervals.
  More informative than the leaderboard position: the Nemotron 3 Super page explicitly
  targets agentic workloads (tool calling, structured outputs, reasoning modes), which
  is the first time a major open-weights release in this size class has shipped with
  native agentic primitives as headline features rather as afterthoughts. This is a
  positioning signal about where the open-source model ecosystem is heading.

### Claim 3: Nemotron 3 Super uses a hybrid mamba-2/transformer/MoE architecture with 120B total parameters and only 12B active per token

- **Evidence**: Model card from Nvidia. The 120B total / 12B active split is the
  mixture-of-experts routing behavior. Multi-token prediction layers and latent MoE
  compression (1/4 size reduction) are also documented.
- **Confidence**: settled (model architecture is published factual metadata)
- **Quote**: "Hybrid mamba-2/transformer/mixture-of-experts design; 120 billion total
  parameters, 12 billion active per token"
- **Our assessment**: The 12B active parameter count is what matters for inference cost
  and latency — the model runs with the compute footprint of a 12B model while having
  the capacity of 120B. This is the MoE value proposition. The mamba-2 component
  (state-space sequence model) contributes to the throughput advantage: unlike pure
  attention, mamba layers have linear (not quadratic) inference cost with sequence length,
  which explains why this model also leads on long-context benchmarks.

### Claim 4: Nemotron 3 Super achieves 91.75% on RULER long-context benchmark at 1M tokens — significantly outperforming gpt-oss-120b (22.30%)

- **Evidence**: RULER is a published long-context benchmark. The gpt-oss-120b comparison
  number (22.30%) is stark — it suggests that model's 1M-token context window is largely
  non-functional at long ranges. Qwen3.5-122B scores 91.33% (comparable to Nemotron).
- **Confidence**: emerging (benchmark results are published; RULER independently validated
  as a long-context eval; the 22.30% number for gpt-oss-120b is striking enough to
  warrant confirmation)
- **Quote**: "RULER long-context (1M tokens): 91.75% accuracy vs. Qwen3.5-122B 91.33%,
  gpt-oss-120b 22.30%"
- **Our assessment**: If the gpt-oss-120b RULER number holds up under independent
  verification, it would mean that model's 1M token advertised context is effectively
  broken at real-world long-range retrieval tasks. This is a meaningful data point
  for teams choosing open-weights models for agentic workloads where long context windows
  are needed (e.g., codebase-wide reasoning, multi-document agents). Nemotron's mamba-2
  component likely drives this advantage — SSMs handle long-range dependencies more
  uniformly than pure transformer attention, which degrades at range.

### Claim 5: Nemotron 3 Super ships with native tool calling, structured outputs, and three reasoning modes (off, low, regular)

- **Evidence**: Listed as first-class supported capabilities in Nvidia's announcement.
  Seven languages (Chinese, English, French, German, Italian, Japanese, Spanish), 43
  programming languages, 25T training tokens.
- **Confidence**: settled (capability list is Nvidia's own product documentation)
- **Quote**: (no direct quote; described as capabilities: "Tool calling and structured
  outputs; Reasoning modes (off, low, regular)")
- **Our assessment**: Native tool calling in a 12B-active-parameter model is a
  meaningful capability milestone for local/self-hosted agentic deployments. Previously
  teams building open-source agent harnesses had to rely on fine-tuned tool-use models
  or prompt engineering workarounds for structured output. Reasoning mode control
  (off/low/regular) enables cost/latency tradeoffs at the model level — teams can
  disable reasoning for fast tool routing calls and enable it for complex planning steps.

### Claim 6: Nemotron 3 Super weights are free for commercial use, with rights terminating only if safety guardrails are removed or users file patent litigation against Nvidia

- **Evidence**: License terms stated in the announcement. Available for free via Nvidia
  and OpenRouter. API pricing via third parties: ~$0.30/$0.80 per million input/output
  tokens.
- **Confidence**: settled (license terms are published)
- **Quote**: "Free weights/datasets download (license permits commercial use; rights
  terminate if safety guardrails removed or user files patent litigation against Nvidia)"
- **Our assessment**: This is more permissive than Llama's license (which restricts
  use above 700M monthly active users) but includes a guardrail-removal restriction
  that could complicate deployments that customize safety layers. The OpenRouter
  availability makes evaluation frictionless. At $0.30/$0.80 per million tokens via
  API, it is substantially cheaper than closed-weights models at comparable capability
  levels — relevant for teams comparing self-hosted vs. API cost for agentic workloads.

### Claim 7: Nvidia plans a $26 billion investment over five years in open-weights models — a strategic commitment to the open ecosystem

- **Evidence**: Stated in the "Behind the News" section; sourced from Nvidia's public
  announcements.
- **Confidence**: emerging (corporate investment announcements are often reshaped;
  verifiable in principle but not yet executed)
- **Quote**: "Nvidia plans $26 billion investment over five years in open-weights models"
- **Our assessment**: The strategic context: Chinese AI labs (Alibaba, Moonshot, Z.ai
  building GLM-5) are developing high-capability models specifically optimized for
  non-Nvidia hardware. Nvidia's open-weights investment is partly defensive — it
  maintains ecosystem lock-in through training-hardware dependency (NVFP4 on Blackwell)
  even while releasing weights freely. For teams evaluating model selection strategy:
  the open-weights model landscape is moving fast enough that hardware-agnostic models
  (Qwen, Llama) and hardware-tied models (Nemotron on Blackwell) are diverging in
  their TCO profiles.

### Claim 8: OpenAI's AWS deal is structured around a stateful runtime environment — distinct from stateless API calls — enabling managed agent state, memory, tool connections, and permissions

- **Evidence**: Technical framing from the OpenAI/AWS announcement. The stateful/stateless
  distinction is the legal and architectural mechanism that allowed AWS access while
  preserving Microsoft Azure's exclusive stateless API hosting rights.
- **Confidence**: emerging (based on public announcement framing; the technical
  architecture of the stateful runtime is not described in detail in this news digest)
- **Quote**: "Stateful runtime environment handles agent memory, tool connections, and
  user permissions — distinguishing from stateless API calls where 'each request is
  independent.'"
- **Our assessment**: The stateful/stateless split is architecturally significant for
  agent harness design. A stateful runtime that manages memory persistence, tool
  connections, and permission context server-side removes those concerns from the
  harness author — but also introduces vendor lock-in at the agent session level.
  The integration with Amazon Bedrock AgentCore means teams building on AWS have a
  path to managed agent infrastructure without building their own session management
  layer. The thin technical detail in this news digest limits extraction — this is
  a "watch this space" claim rather than an actionable engineering pattern.

### Claim 9: The OpenAI/AWS stateful deal was structured to preserve Microsoft Azure's exclusive stateless API hosting rights (2019–2024 agreement)

- **Evidence**: Business deal structure from public reporting. Microsoft held exclusive
  cloud hosting rights; the October 2025 restructuring removed right of first refusal
  and enabled AWS and other partnerships. The legal distinction (stateful vs. stateless)
  is explicitly the mechanism.
- **Confidence**: emerging (business structure is publicly reported; the legal distinction
  is the reported mechanism, not confirmed via primary legal documents)
- **Quote**: "Legal distinction preserves Microsoft Azure's exclusive stateless API hosting
  while enabling AWS agent infrastructure."
- **Our assessment**: For teams making cloud infrastructure decisions: OpenAI's agentic
  products may route to different cloud providers depending on stateful vs. stateless
  usage patterns. Bedrock AgentCore is the AWS integration point; Azure remains the
  stateless API provider. Teams with existing AWS or Azure vendor relationships may
  find their OpenAI API access is implicitly routing to different infrastructure depending
  on whether they use session-based agent APIs vs. one-shot completion calls.

### Claim 10: MIT Recursive Language Models (RLMs) treat prompts as external Python variables, enabling processing of documents that exceed model context windows

- **Evidence**: Benchmark results on BrowseComp+ (a long-context research benchmark):
  RLM-GPT-5 achieves 91.3% (stock GPT-5 hit context limits and could not respond);
  RLM-Qwen3-Coder-480B achieves 44.7% vs. Qwen with summary agent 38.0%;
  RLM-Qwen3-8B achieves 14% vs. baseline 0%.
- **Confidence**: emerging (published research results; independent replication pending)
- **Quote**: "Researchers developed systems treating prompts as external Python variables
  rather than feeding them directly into models, enabling processing of documents
  exceeding context windows."
- **Our assessment**: RLMs are relevant to agentic harness design for the specific class
  of tasks that require processing very large documents (codebase-wide analysis, lengthy
  legal/technical documents). The BrowseComp+ results are striking — the 91.3% for
  RLM-GPT-5 vs. stock GPT-5's inability to respond suggests that recursive decomposition
  is solving a real retrieval/reasoning problem, not just a mechanical context-stuffing
  problem. The OOLONG-PAIRS result (~50% maintained accuracy at 1M tokens vs. stock
  GPT-5 at ~0%) is the more compelling data point. For harness engineers building
  context management strategies: recursive task decomposition over large corpora may
  outperform retrieval-augmented approaches for tasks requiring full-document coherence.

## Concrete Artifacts

### Nemotron 3 Super 120B: Key Specs

```
Nvidia Nemotron 3 Super 120B-A12B (announced March 2026)

Architecture:    Hybrid mamba-2 / transformer / MoE
Parameters:      120B total; 12B active per token
Training data:   25 trillion tokens
Languages:       20 human languages (7 main), 43 programming languages
Context window:  Up to 1,000,000 tokens (input and output)
Training format: NVFP4 (native to Nvidia Blackwell GPUs)

Native capabilities:
  - Tool calling
  - Structured outputs
  - Reasoning modes: off / low / regular

Benchmark performance:
  Throughput (442 tok/s) vs:
    gpt-oss-120b:             278 tok/s
    Gemini 3.1 Flash-Lite:    266 tok/s

  PinchBench (agentic tasks):
    Nemotron 3 Super:         85.6%
    Kimi K2.5:                84.8%
    GLM-5:                    84.1%

  RULER 1M-token long-context:
    Nemotron 3 Super:         91.75%
    Qwen3.5-122B:             91.33%
    gpt-oss-120b:             22.30%

  Artificial Analysis Intelligence Index:
    Qwen3.5-122B:             42
    Nemotron 3 Super:         36
    gpt-oss-120b:             33

Availability:
  Weights: Free download (Hugging Face, Nvidia)
  API:     OpenRouter, Nvidia API (~$0.30/$0.80 per M tokens)
  License: Commercial use permitted; rights terminate on:
             (a) removal of safety guardrails, OR
             (b) filing patent litigation against Nvidia
```

### OpenAI/AWS Stateful Agent Infrastructure: Deal Structure

```
OpenAI + Amazon AWS Agent Infrastructure Deal (announced ~March 2026)

DEAL STRUCTURE
  Amazon investment:         $15B committed + $35B conditional
                             (on undisclosed milestones or OpenAI IPO before 2029)
  AWS agreement:             $100B expansion of prior $38B deal (8-year term)
  Compute commitment:        OpenAI consumes 2 GW of Amazon Trainium processing

ARCHITECTURAL SPLIT (preserving prior Microsoft Azure rights)
  Azure (Microsoft):         Stateless API calls (each request independent)
  AWS (Amazon):              Stateful runtime environment (agent sessions)

STATEFUL RUNTIME HANDLES:
  - Agent memory persistence
  - Tool connections
  - User permissions across session

AWS INTEGRATION:
  Platform:   Amazon Bedrock AgentCore
  Deployment: Customer environments
  Routing:    OpenAI Frontier (agent platform) customers via Amazon → Bedrock
              Direct OpenAI customers → Azure (stateless)

CONTEXT
  Microsoft 2019–2024 exclusive cloud rights expired; October 2025 restructuring
  removed Microsoft's right of first refusal, enabling AWS and other cloud partnerships.
  Microsoft retains 27% ownership and 20% revenue share from 2025 restructuring.
```

### MIT RLM Benchmark Results

```
MIT Recursive Language Models (RLMs) — March 2026 publication

Approach: Treat prompts as external Python variables (not in-context);
          recursively decompose tasks to process documents exceeding context windows

BrowseComp+ benchmark results:
  RLM-GPT-5:               91.3%  (stock GPT-5: could not respond — context limit)
  RLM-Qwen3-Coder-480B:   44.7%  (vs. Qwen with summary agent: 38.0%)
  RLM-Qwen3-8B:            14%   (vs. baseline: 0%)

OOLONG-PAIRS benchmark (1M-token context):
  RLM-GPT-5:               ~50% accuracy maintained across million-token contexts
  Stock GPT-5:              ~0% (context limit failure)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-glm51.md` — That note documents GLM-5.1 (Z.ai,
  754B MIT-licensed model) as another recent frontier open-weights release. The Batch 346
  "Behind the News" section explicitly names Z.ai among Chinese competitors building models
  for non-Nvidia hardware. Nemotron 3 Super and GLM-5.1 are contemporaneous open-weights
  options at different points on the parameter/capability curve — both offer MIT-or-similar
  permissive licenses and OpenRouter access. PinchBench shows GLM-5 at 84.1% vs. Nemotron
  at 85.6%, giving a direct head-to-head data point.

- **Corroborates**: `blog-cursor-cursorbench.md` — That note documents CursorBench's
  argument that public benchmarks fail to differentiate models at the frontier. Nemotron's
  PinchBench score (Nvidia's proprietary agentic benchmark) raises the same concern: PinchBench
  is a first-party eval, not independently validated. The CursorBench note's warning about
  vendor-designed benchmarks is directly applicable here — PinchBench margins (85.6% vs.
  84.8%) are within noise without published confidence intervals.

- **Corroborates**: `blog-anthropic-harness-long-running.md` — The OpenAI/AWS stateful
  agent infrastructure deal (managed memory, tool connections, user permissions) is a
  cloud-native implementation of the session and state management concerns that the
  Anthropic long-running harness post addresses at the SDK level. Both sources identify
  stateful session management as a core challenge for production agents; they represent
  different solution tiers (DIY harness via SDK vs. managed cloud service via Bedrock AgentCore).

- **Extends**: `blog-simonwillison-glm51.md` — Adds PinchBench comparative data giving
  GLM-5 a reference score (84.1%) against which Nemotron 3 Super can be calibrated.
  The Batch 346 is a more current snapshot of the open-weights model landscape than
  the GLM-5.1 note, adding throughput and long-context benchmarks as selection criteria
  alongside general capability.

- **Novel**: 
  - **PinchBench** as an agentic benchmark is not previously mentioned in the corpus.
    This note introduces it as a data point, with the CursorBench-documented caveat
    that vendor benchmarks should be treated as promotional until independently validated.
  - **Stateful vs. stateless API split** as an architectural mechanism for cloud provider
    routing in agentic deployments is new to the corpus. This is a practical infrastructure
    concern for teams using OpenAI APIs on AWS vs. Azure.
  - **MIT Recursive Language Models** as a long-context processing approach is not
    addressed in any other corpus source. The BrowseComp+ results (91.3% RLM-GPT-5 vs.
    stock GPT-5 unable to respond) are the strongest data point in the corpus on
    recursive decomposition for very long documents.

## Guide Impact

- **Chapter on Model Selection**: Nemotron 3 Super 120B should be added as a reference
  data point when the guide discusses open-weights model options for agentic workloads.
  The 12B active parameter / 442 tok/s profile makes it the current throughput leader
  for self-hosted agents. The RULER 1M-token results (91.75%) are relevant to any
  discussion of long-context agent capabilities. Flag PinchBench as vendor-only
  benchmark and advise independent validation.

- **Chapter on Agent Infrastructure / Deployment**: The OpenAI/AWS stateful runtime deal
  is the first major cloud-native managed agent state infrastructure announcement.
  When discussing cloud deployment options for production agents, note the AWS Bedrock
  AgentCore integration as a managed alternative to building session management in
  custom harnesses. The stateful/stateless architectural split is worth documenting as
  a pattern: stateless (each request independent, Azure) vs. stateful (session persistence,
  AWS) may become a meaningful deployment-architecture choice for teams.

- **Chapter on Context Engineering / Long-Context Patterns**: MIT RLMs provide the
  strongest benchmark evidence in the corpus that recursive task decomposition over
  external-variable prompts can dramatically outperform in-context approaches for
  documents exceeding model context windows. The BrowseComp+ and OOLONG-PAIRS results
  should inform any guide section comparing retrieval-augmented generation (RAG) vs.
  recursive decomposition for long-document tasks.

## Extraction Notes

- Source is a weekly news digest, not a practitioner deep-dive. Technical details are
  secondary reporting on Nvidia and OpenAI announcements, not primary engineering
  documentation. All claims should be verified against primary sources before being
  cited as authoritative.
- Prospector triage flagged novelty as "low" and identified exactly two sections for
  extraction (Nemotron, OpenAI/AWS). RLMs section added here because it has clear
  engineering signal (recursive decomposition for long-context) not found elsewhere
  in the corpus. Grok Imagine 1.0 video section and Andrew Ng editorial omitted per
  Prospector guidance (pricing/business news and AI policy opinion respectively).
- PinchBench is Nvidia's proprietary agentic benchmark. No independent replication
  found. Treat scores as directional signal, not validated ground truth.
- OpenAI/AWS stateful runtime architecture is thinly described in this news digest.
  The Bedrock AgentCore integration and stateful/stateless split are the most specific
  engineering details available. More technical depth would require reading primary
  Amazon Bedrock AgentCore documentation.
- The MIT RLM research is described in a paragraph-length summary. The BrowseComp+
  and OOLONG-PAIRS results are the most extractable claims; full methodology would
  require reading the primary research paper.
