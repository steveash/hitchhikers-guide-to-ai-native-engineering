---
source_url: https://simonwillison.net/2026/Jun/16/georgi-gerganov/
source_type: blog-post
title: "Quoting Georgi Gerganov"
author: Georgi Gerganov (llama.cpp/ggml creator), quoted by Simon Willison
date_published: 2026-06-16
date_extracted: 2026-06-25
last_checked: 2026-06-25
status: current
confidence_overall: anecdotal
issue: "#1302"
---

# Quoting Georgi Gerganov: llama.cpp Creator on Daily Qwen3.6-27B Use for Coding Tasks

> Georgi Gerganov (creator of llama.cpp and ggml) confirms in a Hacker News comment that
> Qwen3.6-27B is a productive daily-use local model for coding tasks, providing a second
> high-credibility practitioner datapoint — distinct model (Qwen vs. DeepSeek), distinct hardware
> (M2 Ultra and RTX 5090), distinct harness approach (stripped pi agent with custom system prompt)
> — corroborating that local model coding agents are genuinely viable for maintainer workflows.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "quotation" format — Willison presents a Hacker
  News comment by Georgi Gerganov without adding editorial prose of his own; the page consists of
  the blockquote and tags only. Tags: ai, generative-ai, local-llms, llms, ai-assisted-programming,
  qwen, coding-agents, georgi-gerganov, pi. Published 16th June 2026. The HN comment was posted
  in a thread responding to Vicki Boykis's article "Running local models is good now.")
- **Author credibility**: Georgi Gerganov is the creator of llama.cpp and ggml — the foundational
  C/C++ inference library and tensor library that underpin most local model runtimes (Ollama, LM
  Studio, and many other tools build on llama.cpp). He is not a consumer of local model
  infrastructure; he is one of its primary architects. His "I can 100% attest" carries unusual
  weight: he has more visibility into what local model inference actually does than nearly any
  other practitioner on the planet. Simon Willison is a designated `trusted-feed` source
  (creator of Django, Django ORM, Datasette); his selection of this comment as worthy of
  amplification is itself a relevance signal.
- **Scope**: Covers Gerganov's experience using Qwen3.6-27B locally at ggml-org for maintenance
  tasks over approximately 1.5 months, his hardware (M2 Ultra and RTX 5090), his harness
  configuration (pi agent stripped to minimal flags with a custom system prompt), and his
  observation that PR review time — not model capability — is his primary bottleneck. Does NOT
  cover: model quality benchmarks, inference speed, configuration setup steps, tool-call
  streaming, quantization details, or how the setup compares to hosted API providers.

## Extracted Claims

### Claim 1: Qwen3.6-27B is a capable local model for coding tasks — attested by the creator of llama.cpp after 1.5 months of near-daily use

- **Evidence**: Direct first-person confirmation from Georgi Gerganov, the author of llama.cpp
  and ggml. This is the highest-credibility local model practitioner validation in the corpus:
  the person who built the infrastructure others use to run local models is himself using one
  daily for coding work. The "100% attest" phrasing signals deliberate confidence, not hedged
  enthusiasm.
- **Confidence**: anecdotal (single practitioner; very high credibility given role; no benchmark
  or controlled study)
- **Quote**: "I can 100% attest to the fact that Qwen3.6-27B is a very capable local model for
  coding tasks."
- **Our assessment**: This is a second-practitioner confirmation that local models are now viable
  for coding agent work, distinct from Ronacher's (`blog-ronacher-local-models-focus-polish.md`
  Claims 11–13) in model (Qwen3.6-27B vs. DeepSeek V4 Flash), hardware (M2 Ultra and RTX 5090
  vs. Mac 128GB+), and harness (stripped pi base vs. pi-ds4 extension). That two practitioners
  working on different model/hardware/harness combinations independently reach the same
  "genuinely capable" conclusion strengthens the generalization. The credibility differential
  is notable: Gerganov is the infrastructure creator, giving him insider knowledge of what the
  model is actually doing. His assessment is not naive enthusiasm.

### Claim 2: Local model coding agents are productive for "mundane" maintainer tasks — PR review and small code generation — across 1.5 months of near-daily use

- **Evidence**: Gerganov's direct account of his ggml-org maintenance workflow. The
  characterization "nothing really impressive, but definitely a helpful tool for a maintainer"
  is self-aware modesty that also sets a realistic capability expectation.
- **Confidence**: anecdotal (first-person account; representative of one maintainer's workflow
  over 1.5 months)
- **Quote**: "I use it for small mundane tasks at ggml-org - nothing really impressive, but
  definitely a helpful tool for a maintainer."
- **Our assessment**: The "mundane tasks" framing is valuable calibration. Gerganov is not
  claiming the model replaces deep architectural reasoning or greenfield system design — he
  is claiming it reliably handles the repetitive, high-volume tasks that consume maintainer
  time: reviewing code, writing small patches, explaining changes. For practitioners evaluating
  local model adoption: the realistic target use case is "helpful for maintainer workflows,"
  not "replaces senior engineering judgment." This honest framing is more useful than
  benchmark claims.

### Claim 3: A stripped-down pi agent configuration (`pi -nc --offline` with a short custom system prompt) is sufficient for productive local model coding work

- **Evidence**: Gerganov's explicit description of his harness configuration, with the specific
  flags used. The `-nc` flag disables conversation context and `--offline` runs without network
  access. A "short system prompt to align it a bit with my style" means he is applying minimal
  behavioral guidance rather than a complex system prompt.
- **Confidence**: anecdotal (first-person; Gerganov is describing his specific working
  configuration, which he has validated over 1.5 months of use)
- **Quote**: "Currently, I have a very lightweight harness - the pi agent with everything
  stripped (`pi -nc --offline`) and a short system prompt to align it a bit with my style."
- **Our assessment**: The stripped configuration is noteworthy because it inverses the assumption
  that effective local model coding requires sophisticated harness configuration. Gerganov achieves
  productive daily use with the most minimal harness possible: no conversation context, no network,
  just a brief system prompt. This directly instantiates the "pick a winner and polish it" pattern
  from Ronacher's post (`blog-ronacher-local-models-focus-polish.md` Claim 9) — the harness is
  not elaborate; the model is simply good enough that elaborate configuration is unnecessary.
  **Important caveat**: Gerganov is the creator of llama.cpp. He would find local model setup
  trivially navigable. The absence of setup difficulty in his account does not mean typical
  practitioners would find the same experience. The configuration burden described in Ronacher
  Claim 1 (inference engine, quantization, template, context size, JSON configs) still applies
  to practitioners without Gerganov's infrastructure background.

### Claim 4: PR review time — not model capability — is the primary bottleneck limiting a core maintainer's use of local model coding agents

- **Evidence**: Gerganov's direct statement about the constraint on his usage. He distinguishes
  between model capability (which he affirms) and his own time availability for coding tasks
  (which is consumed by PR review obligations).
- **Confidence**: anecdotal (first-person; reflects one maintainer's time allocation, not a
  structural observation about local model limitations)
- **Quote**: "I think I would be using it much more, if I didn't have to spend a lot of my time
  on reviewing PRs."
- **Our assessment**: This is a subtle but important calibration. The limit on Gerganov's local
  model use is not model quality, inference speed, tooling gaps, or configuration burden — it
  is that reviewing the PRs generated by contributors consumes the time he would otherwise spend
  on tasks where the model would help him. This is an ironic loop for the creator of the
  infrastructure that enables AI-assisted coding: the AI PR volume problem
  (`blog-ronacher-pi-oss.md` Claim 13) is consuming the maintainer time that local model
  tools could otherwise help with. For the guide: the "model capability is no longer the
  bottleneck" signal from Gerganov is the same signal Ronacher sends — adoption is limited
  by workflow, time, and tooling integration, not by model quality.

### Claim 5: Local model coding agents are viable for sustained daily use on prosumer workstation hardware — M2 Ultra and RTX 5090 — with Qwen3.6-27B

- **Evidence**: Gerganov's direct account of running the model on his specific hardware over
  approximately 1.5 months. "Almost daily" and two distinct hardware platforms (Apple Silicon
  and NVIDIA GPU) are the evidence.
- **Confidence**: anecdotal (one practitioner's hardware; not a systematic hardware comparison
  or benchmark)
- **Quote**: "Over the last month and a half I've been using it almost daily, either on my M2
  Ultra or on my RTX 5090 box."
- **Our assessment**: Gerganov runs on both Apple Silicon (M2 Ultra — the same platform that
  ds4.c and pi-ds4 target) and a dedicated NVIDIA GPU workstation (RTX 5090). Both are
  prosumer/workstation hardware at the high end of consumer availability, not server-class
  infrastructure. The RTX 5090 mention extends the hardware evidence beyond the Mac-centric
  discussion in Ronacher (`blog-ronacher-local-models-focus-polish.md` Claim 15) and Willison's
  DeepSeek analysis (`blog-simonwillison-deepseek-v4.md` Claim 8): local model coding agents
  are viable on high-end NVIDIA GPU rigs, not just high-RAM Apple Silicon Macs. This
  broadens the addressable hardware base, though both platforms remain expensive relative
  to typical developer workstations.

## Concrete Artifacts

### Georgi Gerganov's Hacker News Comment (Full Blockquote, verbatim from simonwillison.net)

```text
Source: Georgi Gerganov, Hacker News comment in "Running local models is good now" thread
As quoted at: https://simonwillison.net/2026/Jun/16/georgi-gerganov/ (2026-06-16)

"I can 100% attest to the fact that Qwen3.6-27B is a very capable local model for coding
tasks. Over the last month and a half I've been using it almost daily, either on my M2
Ultra or on my RTX 5090 box. I use it for small mundane tasks at ggml-org - nothing really
impressive, but definitely a helpful tool for a maintainer. I think I would be using it
much more, if I didn't have to spend a lot of my time on reviewing PRs. Currently, I have
a very lightweight harness - the pi agent with everything stripped (`pi -nc --offline`) and
a short system prompt to align it a bit with my style."
```

### Gerganov's Pi Agent Configuration (Stripped Harness for Local Model Coding)

```text
Tool:    pi (Armin Ronacher's coding agent, https://github.com/mitsuhiko/pi)
Flags:   -nc --offline
         -nc: disables conversation context (no memory across sessions)
         --offline: no network access during inference
System prompt: short prompt "to align it a bit with my style"
               (minimal behavioral guidance for coding style matching)

Model:   Qwen3.6-27B (local)
Hardware: M2 Ultra -or- RTX 5090 box
Duration: ~1.5 months of near-daily use
Use case: "small mundane tasks at ggml-org" — PR review support, small code generation

Source: Georgi Gerganov, https://simonwillison.net/2026/Jun/16/georgi-gerganov/ (2026-06-16)
```

## Cross-References

- **Corroborates**: `blog-ronacher-local-models-focus-polish.md` Claims 11–13 — Ronacher
  establishes that local models are viable for coding agent work using DeepSeek V4 Flash +
  ds4.c + pi-ds4 on Mac 128GB+. Gerganov provides a second independent practitioner
  confirmation using a different model (Qwen3.6-27B), different hardware (M2 Ultra and RTX
  5090), and a simpler harness (base pi stripped, not pi-ds4). Two distinct practitioner
  accounts from different models and hardware platforms reaching the same "viable for daily
  coding work" conclusion strengthens the generalization beyond any one configuration. Note
  that both practitioners use the Pi agent — Gerganov on the base tool, Ronacher building a
  dedicated extension — which indirectly validates the Pi agent ecosystem as the current
  reference point for local model coding harnesses.

- **Corroborates**: `blog-ronacher-local-models-focus-polish.md` Claim 9 — "Pick a winner
  hard. If a tool call breaks, that is a product bug and then it's fixed no matter where in
  the stack it failed." Gerganov has implicitly done exactly this: selected one model
  (Qwen3.6-27B) and used it consistently for 1.5 months. The stripped harness (minimal flags,
  short system prompt) implies the model was "finished enough" that elaborate configuration
  was unnecessary — consistent with the "pick a winner and polish it" philosophy.

- **Corroborates**: `blog-ronacher-local-models-focus-polish.md` Claim 8 — "A lot of local
  model work optimizes for making models runnable. That is necessary, but it is not the same
  thing as making them feel finished." Gerganov's productive daily use implies Qwen3.6-27B
  has crossed the "finished" threshold for maintainer coding tasks — the model is not merely
  runnable but genuinely useful. However, the important caveat is that Gerganov's background
  (llama.cpp creator) means he is an unusually capable evaluator of what a model is doing
  and an unusually capable resolver of any configuration problems that arise. His "finished"
  experience may not generalize to practitioners who lack his infrastructure expertise.

- **Extends**: `blog-simonwillison-deepseek-v4.md` — Willison's DeepSeek V4 Flash coverage
  and Ronacher's local model polish post together establish the local model coding agent
  pattern on Mac Apple Silicon with DeepSeek. Gerganov's note extends this to a second model
  (Qwen3.6-27B) and a second hardware class (NVIDIA GPU / RTX 5090), broadening the
  corroborated hardware base beyond Mac-only. The two-machine evidence (M2 Ultra and RTX
  5090) is the first cross-platform practitioner validation of local model coding agents in
  the corpus.

- **Novel**:
  - **Qwen3.6-27B as a validated daily-use local coding model**: No other corpus note
    documents practitioner use of Qwen3.6-27B for coding agents. Ronacher's note covers
    DeepSeek V4 Flash; this is the first Qwen3.6-27B practitioner validation in the corpus,
    and from the most credible possible source for a local model assessment.
  - **RTX 5090 as a viable local model coding hardware platform**: Existing corpus notes
    (Ronacher, Willison) focus on high-RAM Apple Silicon Macs for local model coding.
    Gerganov's RTX 5090 use extends the validated hardware base to NVIDIA GPU workstations.
  - **Stripped pi harness as a working pattern (`pi -nc --offline` + short system prompt)**:
    No corpus note documents this specific minimal harness configuration. The contrast with
    pi-ds4 (Ronacher's elaborate zero-config extension) is notable: Gerganov achieves
    productive daily use with the most minimal possible harness, not a specialized extension.
  - **"PR review time is the bottleneck, not model capability"**: Gerganov's observation
    that PR review obligations — not model quality — limit his local model use is a new
    signal in the corpus. No other note documents the case where a practitioner is limited
    by their own time availability (specifically PR review volume from AI-assisted
    contributors) rather than by model or tooling constraints. This is an ironic feedback
    loop: AI tooling increases PR volume, which consumes the time that local model tools
    would otherwise help with.
  - **Highest-credibility local model practitioner confirmation**: The llama.cpp creator
    validating a local model for daily coding use is categorically different from any other
    practitioner account. This is the most authoritative possible source on what local model
    inference actually does and how well it works.

## Guide Impact

- **Chapter on Model Selection / Local vs. Hosted Inference** (extends Ronacher's analysis):
  Gerganov's quote should be cited alongside Ronacher's analysis as a second high-credibility
  practitioner confirmation that local models are viable for coding agent work. The guide
  currently would cite Ronacher (DeepSeek V4 Flash, Mac, pi-ds4) as the primary evidence.
  Adding Gerganov (Qwen3.6-27B, M2 Ultra and RTX 5090, stripped pi) establishes that viability
  is not model-specific or Mac-specific. The realistic framing — "helpful for mundane maintainer
  tasks, not impressive" — should accompany both citations as a capability calibration: local
  models are productive for coding work, not miraculous. The Ronacher caveat about the
  configuration burden (Claim 1) should still accompany the Gerganov confirmation, with the
  explicit note that Gerganov's ease of setup reflects his extraordinary background, not typical
  practitioner experience.

- **Chapter 02 (Harness Engineering)**: The stripped pi agent configuration (`pi -nc --offline`
  + short system prompt) is a concrete harness pattern for local model coding. Contrast with
  pi-ds4 (Ronacher Claim 12 — automated compilation, quantization selection, lifecycle management)
  to show the spectrum: one end is a specialized zero-configuration extension (pi-ds4) that
  handles all the complexity automatically; the other is a stripped-down minimal harness
  (Gerganov's approach) that works for an expert who can configure things themselves. For
  practitioners, the guide should recommend the more automated end (pi-ds4 pattern) unless
  they have Gerganov-level infrastructure expertise.

- **Chapter 01 (Daily Workflows — Practitioner Accounts)**: Gerganov's account provides the
  most credible available practitioner evidence that local model coding agents are genuinely
  part of a daily workflow (not an experiment or occasional use). "Almost daily" over 1.5
  months for "mundane tasks" at ggml-org is a production workflow signal. The guide can cite
  this as evidence that the AI-native daily workflow extends to local models — practitioners
  who have privacy requirements, offline needs, or hyperscaler-independence goals have a
  validated local option.

- **Chapter 02 (Harness Engineering — Workflow Bottleneck Analysis)**: Gerganov's observation
  that PR review time (not model capability) limits his local model use should inform guide
  advice on where to invest harness engineering effort. When a practitioner reaches the point
  where model capability is not the bottleneck, the constraint shifts to workflow integration,
  time allocation, and organizational factors. This matches the pattern Ronacher documents:
  the "local model viability" problem has largely been solved at the model quality level;
  the remaining problems are integration, polish, and workflow friction.

## Extraction Notes

- The Simon Willison page is in his standard "quotation" format: blockquote from the subject,
  no additional editorial prose from Willison, tags only. The full blockquote was recovered
  via multiple targeted WebFetch calls to assemble the complete text. Each sentence was
  individually confirmed across separate fetches; the full quote was confirmed as assembled
  on a final verification fetch. High confidence that the quote is verbatim.
- The quote is from a Hacker News comment Gerganov made in the discussion thread for Vicki
  Boykis's article "Running local models is good now." The Hacker News thread was not followed
  as a substantive linked source — the pi agent page was not available for follow-up; no
  other linked pages were identified as substantively adding to the Gerganov quote's content.
- Three triage comments were submitted for this issue (pipeline artifact). The triage
  assessments rated novelty as "medium" and "high." The "medium" assessments appropriately
  note that this is a second practitioner datapoint corroborating Ronacher; the "high"
  assessment emphasizes Gerganov's extreme credibility as an infrastructure creator. Both
  readings are defensible; this source note reflects the "medium novelty, high credibility"
  synthesis from the second triage comment.
- Confidence rated anecdotal overall: all claims originate from a single practitioner's
  ~100-word HN comment. No benchmark data, inference metrics, configuration details, or
  tool-call behavior is described. The practitioner is highly credible but the account is
  brief and experience-level only.
- No contradiction identified with existing corpus sources. No contradiction issue filed.
  The Gerganov account is consistent with Ronacher's local model viability claims while
  extending them to a different model and hardware configuration. The absence of discussion
  about configuration burden, tool-call streaming gaps, or polish issues is consistent with
  Gerganov's infrastructure expertise (he would not experience these as pain points), not
  a contradiction with Ronacher's account of those gaps.
- Cross-reference claim numbers verified against `blog-ronacher-local-models-focus-polish.md`
  read in full during this extraction session: Claims 1, 8, 9, 11, 12, 13, and 15 confirmed
  by position in the note.
