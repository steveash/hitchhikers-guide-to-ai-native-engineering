---
source_url: https://www.deeplearning.ai/the-batch/issue-354
source_type: blog-post
title: "The Batch Issue 354: Hermes vs. OpenClaw, Cybersecurity Alarms Ring, More-Interactive Conversations, Can Agents Do Human Work?"
author: DeepLearning.AI / Andrew Ng (editorial)
date_published: 2026-05-22
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: emerging
issue: "#875"
---

# The Batch Issue 354: Hermes Agent Memory/Skill Architecture, TML Real-Time Multimodal, AISI Cybersecurity Escalation, Agent Benchmark Distribution Gap

> Four high-signal stories from May 22, 2026: (1) Hermes Agent's automatic
> skill-building and dual-file memory architecture as a concrete open-source
> pattern for stateful agents; (2) TML-Interaction-Small's encoder-free early
> fusion enabling 0.40s conversational latency with 276B parameters; (3) AISI
> reporting Claude Mythos Preview and GPT-5.5 now execute attacks taking
> humans 3 hours, with token scaling increasing attack depth; (4) CMU/Stanford
> quantifying that agent benchmarks are skewed 2.7× toward computer/math vs.
> the economic weight of admin/office support occupations.

## Source Context

- **Type**: blog-post (weekly news digest; DeepLearning.AI's flagship newsletter,
  Issue 354, May 22, 2026; 16-minute read)
- **Author credibility**: The Batch is Andrew Ng's weekly AI industry roundup.
  This issue reports on announced products and third-party research — Nous Research
  (Hermes Agent), Thinking Machines Lab (TML-Interaction-Small), Google security
  researchers, and a Carnegie Mellon/Stanford study. Andrew Ng's opening letter on
  Harvard grade policy is not extracted (no engineering-practice signal). Treat
  as reliable secondary reporting on primary sources, not first-party engineering
  documentation. Four stories cover distinct topics; each requires independent
  confidence calibration.
- **Scope**: Covers four engineering-relevant stories: Hermes Agent vs. OpenClaw
  (agent architecture and self-improvement), TML-Interaction-Small (real-time
  multimodal with foreground/background model split), cybersecurity threats from
  LLMs (Google report + AISI update), and agent benchmark distribution gaps
  (CMU/Stanford). The Andrew Ng Harvard grade editorial is not extracted per
  Prospector guidance.

## Extracted Claims

### Claim 1: Hermes Agent overtook OpenClaw in daily token consumption on OpenRouter despite complaints about token inefficiency, signaling that capability (automatic skill creation) outweighs token economy for users

- **Evidence**: Reported fact from Nous Research's open-source launch; OpenRouter
  leaderboard is a third-party platform tracking real usage. The leaderboard
  criterion (daily token consumption) is a proxy for user demand.
- **Confidence**: emerging (leaderboard snapshot at time of publication; token
  consumption can shift rapidly)
- **Quote**: "Hermes Agent, an open-source agent launched in February by the
  New York-based AI lab Nous Research, recently moved ahead of OpenClaw on a
  leaderboard that tracks the number of tokens agents consume daily, as tallied
  by the AI-model platform OpenRouter. Some users have complained that Hermes
  Agent is less token-efficient, but its ability to define and sharpen new skills
  (specialized instructions, workflows, and/or domain knowledge) calls attention
  to self-improvement as a core agentic capability."
- **Our assessment**: The OpenRouter leaderboard is a coarse but real signal —
  it reflects actual usage, not vendor claims. The caveat about token
  inefficiency is significant: users accept higher cost for self-improvement
  capability. This inverts the usual assumption that token efficiency is the
  primary selection criterion. For harness engineers: if skill accumulation and
  memory provide measurable task improvement, users may tolerate higher
  per-interaction cost, which changes how to evaluate agent ROI.

### Claim 2: Hermes Agent creates new skills automatically upon task completion using SKILL.md format, and a Curator system manages lifecycle by archiving unused skills (90+ days) and merging similar ones

- **Evidence**: Architectural description from the source, describing Hermes
  Agent's design in concrete mechanism terms. SKILL.md is a named file format
  for skills as instruction files.
- **Confidence**: emerging (vendor description of open-source architecture;
  the SKILL.md format and Curator mechanism are verifiable in the published
  codebase)
- **Quote**: "it also creates new skills automatically. When Hermes Agent works
  on a problem for a long time or fixes an error and decides it has completed
  the task successfully, it calls a tool to create a skill. To prevent
  agent-generated skills from growing out of hand, an additional background
  system called Curator (i) archives every skill that has not been used in over
  90 days by moving it to a separate folder, and (ii) uses an LLM determine
  whether each skill should be kept as is, merged with other skills, or archived."
- **Our assessment**: The Curator's lifecycle management (90-day usage threshold,
  LLM-driven merge/archive decisions) is the most concrete skill-management
  architecture in the corpus. Skills Hub (Hermes's crowd-sourced skill library)
  is currently much smaller than OpenClaw's library — automatic skill generation
  is partly compensating for the community library gap. The "merge with other
  skills" operation is particularly notable: the agent maintains a non-redundant
  skill inventory rather than accumulating duplicates. This is skill-space
  compaction, analogous to context compaction in long conversations.

### Claim 3: Hermes Agent maintains two persistent memory files — user preferences and workflows/lessons learned — with LLM-driven deduplication and merge-on-overflow before writing new entries

- **Evidence**: Architectural description specifying the two-file design, with
  named decision logic for when and whether to write memory.
- **Confidence**: emerging (first-party open-source design description; mechanism
  is concrete and verifiable)
- **Quote**: "Hermes Agent maintains two general memory files that it adds to the
  prompt. One details user preferences, and the other includes information about
  workflows and lessons learned. It calls a built-in memory tool to add to these
  files. When it decides to add a memory, it checks the memory to see if it's
  worth adding and which of the two files to add it to. (For example, it does not
  add the memory if a similar memory already exists or the memory is too vague.)
  When it determines that adding the memory would exceed a preset file length, it
  examines the relevant memory file and merges related entries."
- **Our assessment**: The two-file separation (preferences vs. workflows/lessons)
  is a clean semantic partition: preferences are about the user, workflows are
  about the task domain. The merge-on-overflow pattern — rewriting the file to
  consolidate related entries before adding new ones — prevents unbounded growth
  while preserving information density. The vagueness check ("does not add the
  memory if... the memory is too vague") is a quality gate that rejects
  low-signal observations. This mirrors the approach of Anthropic's Managed
  Agents memory (`blog-anthropic-claude-managed-agents-memory.md` Claim 2), which
  also uses file-based storage for agent memory — but Hermes implements the
  merge-and-deduplication logic at the prompt-assembly level rather than relying
  on a platform memory layer.

### Claim 4: Hermes Agent uses a judge model to evaluate whether a persistent user goal has been achieved, continuing the agentic loop until the goal is satisfied or a maximum turn count is reached

- **Evidence**: Explicit architectural description. Anthropic Claude Code,
  OpenAI Codex, and OpenClaw (via plugin) are cited as offering similar capability.
- **Confidence**: emerging (design description; the judge model evaluation is
  a named architectural component)
- **Quote**: "Users can specify a goal in a message. Once the agent finishes its
  response, it will call a judge model to evaluate whether the goal was completed.
  If not, it continues working. This loop continues until the goal is judged to
  have been completed or the agent reaches a maximum number of turns. Anthropic
  Claude Code, OpenAI Codex, and OpenClaw (via a plugin) offer a similar capability."
- **Our assessment**: The judge-model pattern for goal evaluation is notable
  because it externalizes goal completion assessment from the agent's own
  generation: the acting model does not decide if it's done — a separate judge
  model makes that call. This separation of actor from evaluator is a reliability
  pattern: the acting model may be motivated (via training) to declare success,
  while the judge model can apply a distinct rubric. The max-turn safety rail
  prevents infinite loops. The three named counterparts (Claude Code, Codex,
  OpenClaw) confirm this is converging as an industry-standard agentic loop
  feature, not a Hermes-specific novelty.

### Claim 5: Hermes Agent's agentic loop context-summarizes old conversation history when the assembled prompt would exceed the LLM's input limit

- **Evidence**: Architectural description of the agentic loop's four steps, with
  context management as an explicit named step.
- **Confidence**: settled (described as a concrete mechanism; context length
  management is a well-understood engineering necessity)
- **Quote**: "(ii) If the prompt exceeds the input limit of the associated LLM,
  it asks the LLM to summarize old messages in the conversation history to reduce
  the size."
- **Our assessment**: Summarization-on-overflow is a simpler but lower-fidelity
  approach than research-wasnotwas-context-compaction.md's context compaction
  pattern, which preserves information more carefully. The Hermes design trades
  fidelity for simplicity: asking the LLM to summarize on demand is easy to
  implement but loses detail. For practitioners: this is the "good enough" long
  context solution for general-purpose agents; systems where historical task
  detail is critical (multi-week projects, accumulated debugging context) may
  need more sophisticated compaction.

### Claim 6: Hermes Agent signals a shift "from stateless AI assistants to agents that accumulate experience, adapt to users, and automate ongoing work beyond isolated tasks"

- **Evidence**: Editorial framing from The Batch's "Why it matters" section,
  characterizing the significance of Hermes Agent's design direction.
- **Confidence**: anecdotal (editorial assessment; directionally consistent with
  the architecture described in Claims 1–5)
- **Quote**: "It points toward a shift from stateless AI assistants to agents
  that accumulate experience, adapt to users, and automate ongoing work beyond
  isolated tasks."
- **Our assessment**: This is the clearest articulation in the corpus of the
  stateless → stateful agent transition as a named design evolution. The three
  components — accumulate experience (memory), adapt to users (user preference
  file), and automate ongoing work (persistent goal tracking) — map directly to
  the three mechanisms described in Claims 3, 3, and 4 respectively. For the
  guide: this framing is useful as a vocabulary anchor for the agent design
  chapter. "Stateful agents" is a better term than "agentic memory" for
  describing this cluster of patterns.

### Claim 7: TML-Interaction-Small processes audio, video, and text via 200ms "micro-turns" of interleaved input/output using encoder-free early fusion — trained from scratch without pretrained encoders for audio or images

- **Evidence**: Architectural description from Thinking Machines Lab's announcement
  and The Batch reporting. The technical design is detailed enough (200ms chunks,
  hierarchical multilayer perceptron for image patches, flow-matching decoder,
  jointly trained transformer) to constitute a concrete architectural claim.
- **Confidence**: emerging (vendor architectural description; mechanism is specific
  and technically coherent)
- **Quote**: "The interaction model interleaves 200-millisecond chunks of input
  processing and output generation, which Thinking Machines Lab calls micro-turns,
  rather than alternating between typical turns of input and output. It processes
  audio, video, and text as parallel streams, eliminating the perceived boundary
  between the end of an input and generation of an output."
- **Quote** (encoder-free): "Thinking Machines Lab calls this approach
  _encoder-free early fusion_ because it skips large pretrained encoders that
  many multimodal systems require (like OpenAI Whisper uses for audio and vision
  transformers use for images). The team trained the transformer, perceptron,
  and decoder together from scratch."
- **Our assessment**: Encoder-free early fusion is architecturally significant:
  most multimodal systems bolt pretrained encoders (Whisper for audio, ViT for
  images) onto a language model backbone. Training the full multimodal stack
  from scratch allows the architecture to learn joint representations optimized
  for interactivity rather than inherited from single-modality pretraining.
  The 200ms micro-turn is the key latency mechanism — it is below human
  perceptual thresholds for conversational delay (~300ms), enabling true
  interruptibility. The cost of this design is the 276B total parameter count
  required to maintain quality without pretrained encoder quality guarantees.

### Claim 8: TML-Interaction-Small achieves 0.40s conversational latency on FD-bench V1 and 77.8 average quality on FD-bench V1.5 (interruption handling), substantially outperforming GPT-Realtime-2 and Gemini-3.1-flash-live-preview on interactivity benchmarks

- **Evidence**: Thinking Machines Lab's own benchmarks, with competitor scores
  on the same benchmarks. Three models compared directly; scores are specific
  and quantitative.
- **Confidence**: emerging (vendor-reported benchmarks on own model; competitor
  scores reported at specific settings which affects comparability)
- **Quote**: "On FD-bench V1, which measures audio latency in conversational
  turns, TML-Interaction-Small responded in 0.40 seconds, significantly faster
  than Gemini-3.1-flash-live-preview set to minimal reasoning (0.57) and
  GPT-Realtime-2 set to minimal reasoning (1.18 seconds)."
- **Quote** (interruption): "On FD-bench V1.5, which gauges a model's ability
  to manage interruptions, interjections such as 'uh huh,' and foreground versus
  background speech, TML-Interaction-Small achieved 77.8 average quality, well
  above GPT-Realtime-2 set to xhigh reasoning (47.8 average quality) and
  Gemini-3.1-flash-live-preview set to high reasoning (45.5 average quality)."
- **Our assessment**: The FD-bench V1 gap is significant: TML at 0.40s is 3×
  faster than GPT-Realtime-2 at 1.18s. The FD-bench V1.5 gap is even more
  striking — 77.8 vs 47.8 is a 63% margin on interruption handling. These are
  the interactivity-specific benchmarks; TML trails on intelligence benchmarks
  (Claim 9). The competitor settings matter: GPT-Realtime-2 at "xhigh reasoning"
  is prioritizing intelligence over latency, which is the appropriate operating
  point for reasoning tasks. FD-bench V1.5 at 47.8 for GPT-Realtime-2 at xhigh
  suggests a latency/interactivity tradeoff, not just an architectural limitation.

### Claim 9: TML-Interaction-Small leads other voice models on interactivity benchmarks but trails GPT-Realtime-2's strongest reasoning mode on intelligence benchmarks

- **Evidence**: Benchmark results on three evaluations: Audio MultiChallenge
  (TML 43.4% APR, GPT-Realtime-2 48.5%, Gemini 36.1%) and BigBench Audio
  (TML 96.5%, GPT-Realtime-2 and Gemini tied 96.6%) show TML trailing or tied
  on intelligence; FD-bench V1/V1.5 show TML leading on interactivity (Claims 8).
- **Confidence**: emerging (vendor-reported; specific numeric results on named
  benchmarks; the benchmark selection may favor TML's architectural strengths)
- **Quote**: "In Thinking Machines Lab's tests, TML-Interaction-Small outperformed
  other voice models on benchmarks that evaluate interactivity but trailed
  GPT-Realtime-2's strongest reasoning mode on tests of intelligence."
- **Our assessment**: The tradeoff is explicit and honest: optimize for
  interactivity and you pay in intelligence. TML's architecture (foreground
  fast model + background asynchronous reasoner) is a design choice that
  prioritizes perceived responsiveness over per-turn reasoning depth. The
  background model can compensate, but only asynchronously. For real-time
  coaching, translation, or monitoring use cases (surgery, athletics per the
  article), the interactivity priority is correct. For multi-step complex
  reasoning, GPT-Realtime-2 at xhigh would be preferred.

### Claim 10: TML-Interaction-Small pairs a real-time interaction model with an asynchronous background reasoning model that shares the same context, with the interaction model weaving background outputs into conversation when appropriate

- **Evidence**: Architectural description with specific design motivation
  stated. The foreground/background split is named as distinct from orchestration
  approaches like Vocal Bridge.
- **Confidence**: emerging (vendor architectural description; the design
  rationale is explicitly articulated)
- **Quote**: "TML-Interaction-Small pairs two components: a fast interaction
  model that processes conversations in real time, and an asynchronous
  background model that performs reasoning. [...] The interaction model
  delegates reasoning, web browsing, and tool calls to the background model,
  which runs asynchronously. Both share the same context. The interaction model
  weaves the background model's output into the conversation when appropriate."
- **Our assessment**: The shared context between foreground and background is
  the key architectural property that distinguishes jointly-trained TML from
  orchestration systems like Vocal Bridge (where any real-time model can pair
  with any reasoner, but handoffs are managed externally). Shared context means
  the background model has full conversation history without explicit handoff;
  orchestration means context must be explicitly passed. The article explicitly
  names the trade-offs: TML's approach requires joint training but gains
  learned (rather than orchestrated) handoffs; Vocal Bridge gains flexibility
  but is "fundamentally turn-based, and handoffs between foreground and
  background are orchestrated rather than learned."

### Claim 11: Google researchers identified four new LLM-enabled cyberattack patterns: morphing malware that rewrites itself to evade detection, logical flaw identification invisible to traditional scanners, AI-powered obfuscation networks, and attacks targeting insecure AI infrastructure itself

- **Evidence**: Google security researchers' published report, as reported in
  The Batch. The four categories are explicitly named and mechanically described.
- **Confidence**: emerging (secondary reporting on a research report; the
  categories are attributed to Google's security team; the 2FA exploit discovery
  is described as a specific real-world incident)
- **Quote**: "LLMs can generate malware that evades detection by changing elements
  of its code. Such programs include a so-called mutation engine that, every time
  they replicate or infect a new system, rewrite their own decryption routines,
  swap commands for alternatives that accomplish the same results, add
  nonfunctional subroutines, and so on without changing their functions."
- **Quote** (logical flaws): "Unlike tools typically used by cybersecurity
  professionals to find bugs in code, which often work by finding known patterns
  or bombarding it with random data until it breaks, LLMs can reason about what
  code is intended to do and apply that reasoning to identify logical flaws."
- **Our assessment**: The four categories represent a qualitative shift from
  pattern-matching attacks (which rule-based defenses can handle) to
  reasoning-driven attacks that understand intent and context. "Reasoning about
  what code is intended to do" is the same capability that makes LLMs useful
  for code review — applied adversarially. The AI infrastructure targeting
  category is the most novel: attackers increasingly target AI tools, models,
  and accessory software as network entry points. This creates a recursive
  security problem: the AI systems being used to find vulnerabilities are
  themselves becoming high-value attack targets.

### Claim 12: AISI reported that Claude Mythos Preview and GPT-5.5 can execute attacks expected to take humans 3 hours — escalating from AISI's previous 1-hour forecast and Claude Opus 4.6's debut capability of 30-minute attacks — with performance increasing further when token limits are expanded

- **Evidence**: AISI (UK AI Safety Institute) evaluation report, as reported in
  The Batch. Historical comparison (Opus 4.6 debut = 30 minutes; previous AISI
  forecast = 1 hour; current = 3 hours) provides a timeline of capability growth.
  Additionally, Calif researchers used Claude Mythos Preview to penetrate Apple's
  security system (patch in progress).
- **Confidence**: emerging (AISI is an independent third-party evaluator with
  established methodology; test environments may not fully represent hardened
  production infrastructure)
- **Quote**: "Researchers at the cybersecurity firm Calif used that model to
  penetrate Apple's famously sturdy security. Calif brought the exploit to Apple,
  which is working on a patch. Meanwhile, the United Kingdom-backed AI Security
  Institute (AISI) reported that Claude Mythos Preview and OpenAI's GPT-5.5
  could reliably execute attacks that would be expected to take humans 3 hours —
  substantially longer than their previous forecast of 1 hour. (At its debut,
  Claude Opus 4.6 was able to execute attacks that take people 30 minutes.)"
- **Our assessment**: The progression — 30 minutes (Opus 4.6) → 1 hour (AISI
  prior forecast) → 3 hours (Mythos + GPT-5.5) — is the clearest attack-
  capability timeline in the corpus. Each generation roughly doubles the attack
  depth. The token-scaling finding (longer attacks when more tokens allowed) is
  consistent with `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 4,
  which documents no saturation at 100M tokens on the TLO benchmark. The Apple
  security breach (Calif using Mythos) is the first in-corpus documented case
  of an AI-assisted attack on a major consumer technology platform's security
  systems. It corroborates `blog-thebatch-ng-pm-bottleneck.md` Claim 6 (Mythos
  finding thousands of OS vulnerabilities) and extends it: Mythos is now
  documented both as a vulnerability discovery tool and as an active exploitation
  tool (the Calif Apple case).

### Claim 13: CMU/Stanford researchers mapped 10,000+ examples from 43 agent benchmarks to O*NET work activities, finding that benchmarks are skewed toward computer/math occupations relative to the U.S. economic distribution of labor

- **Evidence**: Zora Z. Wang et al. study using Claude 3.5 Sonnet to map 10,000+
  examples from 43 benchmarks (including SWE-bench and WebArena) to O*NET
  occupational taxonomy. Results quantified across employment count and wages.
- **Confidence**: emerging (peer-reviewed-quality methodology using established
  government data (O*NET); Claude 3.5 Sonnet used as the mapping tool introduces
  potential LLM-classification bias; sampling methodology described in detail)
- **Quote**: "The benchmarks focus much more on 'computer and mathematical'
  occupations (8,622 examples) than 'office and administrative support' (3,186
  examples) and 'management' (676 examples). In comparison, the U.S. employs
  significantly fewer employees in 'computer and mathematical' professions
  (5.2 million employees) than 'office and administrative support' (18.2 million)
  and 'management' (11 million). Similarly, U.S. employers pay 'computer and
  mathematical' professionals a total of 563.6 billion dollars a year, hundreds
  of billions of dollars less than 'office and administrative support' ($869.8
  billion) and 'management' ($1326.3 billion).'"
- **Our assessment**: The benchmark-to-labor gap is striking when expressed in
  capital terms: computer/math ($563.6B) vs. management ($1326.3B) means
  benchmarks are optimizing for a sector with less than half the wage capital
  of the most underrepresented occupation class. The "management" category at
  only 676 examples across 43 benchmarks — vs. 11 million US employees and
  $1.3T annual wages — represents the largest opportunity gap in absolute
  economic terms. The methodology (using Claude 3.5 Sonnet for mapping) is
  worth noting as a meta-point: the same AI being benchmarked is being used to
  analyze the benchmarks' coverage.

### Claim 14: Each individual agent benchmark covers less than 50% of O*NET work activities and less than 60% of skills; the best single benchmark (GDPval) covers only 47.8% of work activities and 58.5% of skills; all 43 benchmarks combined cover 56.5% of work activities and 85.4% of skill categories

- **Evidence**: Direct quantitative results from Zora Z. Wang et al.'s mapping
  study, using O*NET taxonomy as the ground truth for work activity and skill
  coverage.
- **Confidence**: emerging (quantitative output of a systematic methodology;
  coverage is bounded by O*NET taxonomy completeness and LLM classification
  accuracy)
- **Quote**: "Each benchmark covered less than 50 percent of all work activities
  and less than 60 percent of all skills. The benchmark that best covered both
  categories is GDPval, which encompassed 47.8 percent of work activities and
  58.5 percent of skills. All benchmarks put together covered 56.5 percent of
  work activities, though they covered 85.4 percent of the authors' 41 skill
  categories."
- **Our assessment**: The 56.5% work activity coverage across all 43 benchmarks
  combined is the most important number in this section. Even when combining
  every available benchmark, nearly half of human work activities are unmeasured.
  The gap between work activity coverage (56.5%) and skill category coverage
  (85.4%) reveals that skills are more coarsely defined than activities — there
  are fewer skills (41) but more activities (5,806 computer-based activities in
  O*NET). The 14.6% skill gap means that even at the coarser skill level, 6 of
  41 relevant skills are completely absent from all 43 benchmarks. This directly
  corroborates `blog-cursor-cursorbench.md` Claim 1's misalignment thesis (public
  benchmarks misalign with actual developer usage patterns) but quantifies it at
  economy-wide scale rather than the Cursor-specific task distribution.

## Concrete Artifacts

### Hermes Agent Agentic Loop Architecture

```
Hermes Agent Agentic Loop (Nous Research, February 2026)
Source: The Batch Issue 354

Steps:
(i)   Assemble prompt: personality + instructions + tools + skills +
      memory + user knowledge + conversation history (most recent message)
(ii)  If prompt exceeds LLM input limit → ask LLM to summarize old
      conversation history to reduce size
(iii) Send assembled prompt to LLM → agent either:
        - calls a tool
        - calls a skill
        - responds to the user
(iv)  If tool/skill call → execute call → which also outputs a tool call,
      skill call, or user response → cycle repeats
      until model generates a response for the user

Goal evaluation (persistent goals):
  - User specifies goal in a message
  - After each response, judge model evaluates: was goal completed?
  - If not → continue loop
  - Termination: goal achieved OR max turns reached

Context management:
  - Memory: two general files (user preferences; workflows + lessons learned)
  - Conversation database: searchable separately via tool
  - External memory providers: supports Honcho (identity/preference analysis)

Skill lifecycle (Curator):
  - Skills created automatically when Hermes completes a task
  - Curator archives skills unused for 90+ days
  - Curator uses LLM to decide: keep as-is / merge / archive
  - Format: SKILL.md instruction files
```

### TML-Interaction-Small Architecture and Performance

```
TML-Interaction-Small (Thinking Machines Lab, May 2026)
Source: The Batch Issue 354

ARCHITECTURE
  Total parameters:       276 billion (mixture-of-experts)
  Active per token:       12 billion
  Background model:       separate reasoning model (architecture undisclosed)
  Shared context:         interaction + background models share same context
  Input modalities:       audio (discretized tokens), video (40×40 px patches
                          via hierarchical MLP), text
  Output:                 audio (flow-matching decoder), text
  Turn mechanism:         200ms micro-turns (interleaved input + output)
  Fusion approach:        encoder-free early fusion — no Whisper, no ViT;
                          transformer + perceptron + decoder trained from scratch

PERFORMANCE (Thinking Machines Lab benchmarks)
  FD-bench V1 (audio latency):
    TML-Interaction-Small:              0.40s
    Gemini-3.1-flash-live (min reason): 0.57s
    GPT-Realtime-2 (min reason):        1.18s

  FD-bench V1.5 (interruption handling):
    TML-Interaction-Small:              77.8 avg quality
    GPT-Realtime-2 (xhigh reason):      47.8 avg quality
    Gemini-3.1-flash-live (high reason):45.5 avg quality

  Audio MultiChallenge (reasoning, multi-turn):
    GPT-Realtime-2 (xhigh reason):      48.5% APR
    TML-Interaction-Small:              43.4% APR
    Gemini-3.1-flash-live (high reason):36.1% APR

  BigBench Audio (audio reasoning):
    GPT-Realtime-2 + Gemini (high):     96.6% (tied)
    TML-Interaction-Small (background): 96.5%

AVAILABILITY: Closed research preview (months); wider release later 2026
UNDISCLOSED: Training data/methods, knowledge cutoff, context window,
             pricing, background model architecture

vs. Vocal Bridge (orchestration approach):
  TML: jointly trained foreground+background → learned handoffs, no turn boundary
  Vocal Bridge: orchestrated → any real-time + any reasoner, but turn-based
                and handoffs are managed (not learned)
```

### CMU/Stanford Benchmark Coverage Data

```
Agent Benchmark Labor Distribution (Zora Z. Wang et al., CMU/Stanford, 2026)
Source: The Batch Issue 354

METHODOLOGY
  Benchmarks analyzed:   43 (including SWE-bench, WebArena)
  Examples collected:    10,000+
  Sampling: batches of 5 examples per benchmark until <0.1% marginal coverage gain
            (<300 examples → include all; most others → ~300 sampled)
  Mapping tool:          Claude 3.5 Sonnet → O*NET work activities + skills
  O*NET taxonomy:        5,806 computer-based work activities; 41 related skills

BENCHMARK EXAMPLE DISTRIBUTION (by occupation)
  Category                       | Examples | U.S. Employees | Annual Wages
  -------------------------------|----------|----------------|------------------
  Computer & mathematical        | 8,622    | 5.2M           | $563.6B
  Office & admin support         | 3,186    | 18.2M          | $869.8B
  Management                     | 676      | 11M            | $1,326.3B

COVERAGE RESULTS
  Each individual benchmark:     < 50% of work activities; < 60% of skills
  Best single benchmark (GDPval):  47.8% work activities; 58.5% skills
  All 43 benchmarks combined:    56.5% work activities; 85.4% skill categories

AISI CAPABILITY ESCALATION TIMELINE
  Claude Opus 4.6 at debut:      attacks taking humans ~30 minutes
  AISI prior forecast:           attacks taking humans ~1 hour
  Current (Mythos + GPT-5.5):    attacks taking humans ~3 hours
  Token scaling:                 more tokens → longer-duration attacks achievable
  Real-world test:               Calif researchers used Mythos to breach Apple security
                                 (Apple working on patch at time of publication)
```

## Cross-References

- **Corroborates** `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 2
  (Mythos completed 3/10 TLO 32-step corporate network attack simulations) and
  Claim 4 (no saturation at 100M tokens): the AISI 3-hour-attack finding (Claim 12
  here) is a different benchmark scenario than the TLO 32-step attack, but both
  document the same capability trajectory — frontier models executing multi-step
  attacks that humans would require hours to complete, with performance scaling
  with token budget. Together the two notes establish that AI offensive capability
  is advancing on multiple independent evaluation tracks.

- **Corroborates** `blog-thebatch-ng-pm-bottleneck.md` Claim 6 (Claude Mythos
  found thousands of OS vulnerabilities with 99% unpatched): the Apple breach
  (Claim 12 here) extends the Mythos findings from "found vulnerabilities" to
  "exploited a real system." The Calif/Apple case is the first in-corpus
  documented active exploitation of a major platform using frontier AI, elevating
  the threat signal from potential to realized.

- **Corroborates** `blog-anthropic-opus-cybersecurity-partners.md` Claim 3
  (Wiz Red Agent uses Opus to "reason like a human pentester" to find "logic-
  driven flaws traditional scanners miss"): Claim 11 here provides the adversarial
  framing of the same capability — LLMs identifying logical flaws because "they
  can reason about what code is intended to do." The Wiz deployment is the
  defensive application; the Google report documents the same LLM reasoning
  capability applied offensively. Both notes together establish that logical-flaw
  identification via LLM reasoning is now a viable capability on both sides of
  the security equation.

- **Corroborates** `blog-anthropic-claude-managed-agents-memory.md` Claim 2
  (Managed Agents memory uses filesystem-based storage accessed via bash/code
  capabilities): Claim 3 here (Hermes Agent's two-file memory with LLM-driven
  deduplication) is an independent implementation of the same broad pattern
  (agent memory as structured files) in an open-source non-Anthropic system.
  The convergence of Anthropic's Managed Agents and Nous Research's Hermes Agent
  on file-based memory (vs. vector databases) is notable — two independent teams
  reached similar designs. Hermes adds merge-on-overflow and vagueness filtering
  that are not described in the Managed Agents note.

- **Corroborates** `blog-cursor-cursorbench.md` Claim 1 (public agent benchmarks
  suffer from misalignment — "Most SWE benchmarks focus on bug-fixing tasks...
  These misalign with actual developer agent usage patterns"): the CMU/Stanford
  study (Claims 13–14) quantifies the same misalignment at economy-wide scale
  rather than developer-task scale. Both sources reach the same conclusion through
  different methods — Cursor from internal production data, Wang et al. from
  O*NET mapping. Together they make the misalignment case at both the developer
  (Cursor) and the societal-labor (Wang et al.) levels.

- **Extends** `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 6 (Kimi K2.6
  multi-agent swarm with 300 parallel subagents, coordinator reassignment on
  failure): the Hermes Agent story (Claims 1–6) extends the open-source agent
  competition story. Kimi K2.6's claw groups and Hermes Agent's OpenRouter
  overtaking of OpenClaw represent two distinct competitive threads in the open-
  source agent ecosystem: Kimi emphasizes scale (300 subagents, fault-tolerant
  coordination), while Hermes emphasizes self-improvement (automatic skill
  creation, stateful memory). Neither is in tension with the other.

- **Extends** `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 1 (the
  proof-of-work equilibrium: defenders must spend more tokens finding exploits
  than attackers will spend exploiting): the four Google-catalogued attack
  categories (Claim 11) are the adversarial side of the same token-economy.
  Morphing malware and obfuscation networks reduce detection probability per
  attacker token; AI-assisted logical flaw identification increases exploit
  discovery per attacker token. These increase the attacker's effective token
  efficiency — meaning defenders must increase spending to maintain the
  equilibrium. The Google report is the evidence base for why the proof-of-work
  equilibrium is dynamic, not static.

- **Novel** (new to corpus):
  - **Hermes Agent's Curator skill lifecycle system**: the 90-day usage threshold,
    LLM-driven merge/archive decisions, and SKILL.md format are the first
    documented automated skill lifecycle management system in the corpus.
    Prior notes cover agent memory but not agent skill libraries with automated
    curation.
  - **TML-Interaction-Small encoder-free early fusion**: no prior corpus note
    documents encoder-free jointly-trained multimodal architectures for real-time
    interaction, or the foreground/background split for latency/reasoning tradeoff
    at this scale (276B total parameters).
  - **The foreground/background vs. orchestration architectural tradeoff** (Claim 10):
    the explicit comparison between jointly-trained (TML) and orchestrated
    (Vocal Bridge) multimodal real-time systems is new to the corpus.
  - **AISI attack capability timeline** (Claim 12): the specific progression
    (30 min → 1 hour → 3 hours) across model generations and AISI forecasts is
    the first explicit capability escalation timeline in the corpus for AI-enabled
    attacks. Prior notes provided point-in-time capability data; this source
    provides the trajectory.
  - **Benchmark coverage quantified at economy-wide scale** (Claims 13–14):
    the O*NET mapping study is the first in-corpus analysis that quantifies
    benchmark coverage gaps in economic terms (dollars, employment count) rather
    than task-distribution terms. The management sector gap ($1.3T wages, 676
    examples) is new and highly actionable for guide chapters on agent opportunity
    beyond software engineering.
  - **Logical flaw identification as an adversarial LLM capability category**
    (Claim 11): prior corpus notes document LLM-assisted security scanning as a
    defensive tool; this is the first note to document logical flaw identification
    explicitly as an offensive capability category.

## Guide Impact

- **Chapter 04 (Multi-Agent Orchestration) — Stateful Agent Architecture**: Add
  the Hermes Agent pattern (automatic skill creation + lifecycle management +
  two-file memory + judge-model goal evaluation) as a reference implementation
  for open-source stateful agents. Currently the corpus covers Anthropic's
  Managed Agents memory (`blog-anthropic-claude-managed-agents-memory.md`) and
  Kimi K2.6 swarm coordination (`blog-thebatch-gpt55-hallucination-kimi-k26.md`);
  Hermes is the first non-Anthropic, non-Moonshot stateful agent architecture
  in depth. The "stateless to stateful" vocabulary (Claim 6) should anchor the
  section intro.

- **Chapter 04 (Multi-Agent Orchestration) — Skill Management**: The Curator
  lifecycle system (Claim 2) introduces a pattern not previously in the corpus:
  automated skill pruning and consolidation. Add a design note: agents with
  growing skill libraries require lifecycle management (archive unused, merge
  similar) to prevent quality degradation as the library grows. The 90-day
  usage threshold and LLM-driven merge decision are specific enough to serve as
  a reference design.

- **Chapter 03 (Real-Time Agent UX) — Interaction Architecture**: Add TML-
  Interaction-Small's foreground/background split as the jointly-trained
  alternative to orchestration-based real-time agents (Claims 7, 10). The
  latency benchmarks (0.40s, FD-bench V1) and the interruption quality gap
  (77.8 vs 47.8) should anchor any section discussing real-time audio/video
  agent design. The explicit trade-off comparison (Claim 10: TML jointly trained
  vs. Vocal Bridge orchestrated) should be presented as a design decision the
  guide's reader must make, not a settled recommendation.

- **Chapter 06 (Safety & Security) — AI Attack Capability Timeline**: Claim 12's
  attack-duration progression (30 min → 1 hr → 3 hr across model generations)
  is the most concise capability timeline for AI-enabled attacks in the corpus.
  Add it as a named escalation sequence in the security chapter, paired with the
  AISI token-scaling finding and the Apple exploit case. The four attack categories
  from the Google report (Claim 11) should structure the threat landscape overview.

- **Chapter 06 (Safety & Security) — AI Infrastructure as Attack Target**: Claim
  11's "insecure AI infrastructure" category is a new threat class not addressed
  elsewhere in the guide. Recommend adding a section: AI tools, models, and
  accessory software are themselves becoming high-value attack entry points.
  Teams deploying AI-native systems must include the AI stack (model weights,
  API endpoints, agent harnesses, memory stores) in their threat model, not just
  the applications the AI touches.

- **Chapter 05 (Team Adoption / Agent Opportunity) — Beyond Software Engineering**:
  The CMU/Stanford study (Claims 13–14) provides the strongest quantitative case
  in the corpus for agent expansion into non-engineering domains. The management
  sector ($1.3T wages, 676 benchmark examples) and admin/office support ($869.8B
  wages, 3,186 examples) should anchor a guide section on where to direct agent
  investment for maximum economic impact. Current benchmarks mislead teams into
  optimizing for software engineering tasks because that is where the benchmarks
  are — the study provides the corrective framing.

## Extraction Notes

- Source is a weekly news digest (16 minutes); all four engineering-relevant
  stories were read and extracted in full. The Andrew Ng Harvard grade editorial
  was not extracted (educational philosophy, no engineering-practice signal) per
  Prospector guidance.
- TML-Interaction-Small is in closed research preview; benchmark data is from
  Thinking Machines Lab's own tests. The competitor settings (GPT-Realtime-2 at
  xhigh reasoning vs. minimal reasoning) affect direct comparison; claims
  reference the settings in context.
- The CMU/Stanford study uses Claude 3.5 Sonnet for O*NET mapping — the same
  class of AI being evaluated is used as the evaluation instrument. This
  introduces potential systematic bias (the mapping model may be better at
  recognizing software engineering tasks, which could inflate the measured
  skew). The methodology is otherwise transparent and the raw occupational
  employment data (O*NET, BLS) is independently verifiable.
- No contradictions identified that require filing: the AISI 3-hour attack
  finding (Claim 12) is a different evaluation scenario from the TLO 32-step
  attack (blog-simonwillison Claim 2; 20-hour human estimate) — different
  attack complexity classes, not conflicting data. The capability trajectory
  is consistent across both evaluations.
- No sub-pages followed; all four stories were self-contained on the single
  Issue 354 URL.
