---
source_url: https://martinfowler.com/fragments/2026-09-01.html
source_type: blog-post
title: "Fragments: September 1"
author: Martin Fowler (curator); primary linked sources — NVIDIA (Terry Chen, Yeyin (Eva) Zhu, Zhifan Ye, Jean-Francois Puget, Humphrey Shi), Paul Stack (stack72.dev), Claus Wilke (Genes, Minds, Machines), Michał Brzozowski and Neo Christopher Chung (Samsung AI Center Warsaw / University of Warsaw)
date_published: 2026-09-01
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: emerging
issue: "#3161"
---

# Fragments: September 1 (Martin Fowler)

> Fowler's short-form "Fragments" entry links five substantive external pieces:
> Simon Willison's LLM-cliché highlighter and the Wikipedia AI-writing-detection
> page it cites (humans are near-chance at spotting LLM prose); NVIDIA's AVO
> architecture for long-horizon autonomous agents (persistent memory +
> supervisor, 100% on ARC-AGI-3); Paul Stack's "AI Broke the Assumptions Behind
> CI" and Fowler's own rebuttal that CI has always been a practice, not a
> server; Claus Wilke's rebuttal of AI-supervirus fears from a working
> computational biologist's perspective; and an arXiv paper documenting
> correlated, model-family-specific "ghost" author personas contaminating
> real scholarly infrastructure at scale.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" series, September 1, 2026 entry —
  a short-form, multi-topic link-blog post, six snowflake-divider-separated
  sections in the original, roughly 700 words of Fowler's own prose). As with
  prior entries in this series (e.g. `blog-fowler-fragments-2026-08-24.md`),
  most of the substantive content lives in the linked pages rather than in
  Fowler's own text. This note follows four of the six linked items directly
  — the NVIDIA AVO blog post, Paul Stack's CI article, Claus Wilke's biosecurity
  rebuttal, and the arXiv "ghost couple" paper — within MINER.md's "up to 5"
  linked-page guidance. The fifth section (Mickey Petersen's one-line quip) is
  extracted from Fowler's own page directly, since the linked X/Twitter post is
  not independently substantive beyond the quoted line.
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks,
  author of *Refactoring* and *Patterns of Enterprise Application
  Architecture*, and an original Agile Manifesto signatory; `martinfowler.com`
  is a designated `trusted-feed` source in this repository. For the linked
  material: NVIDIA's post is a first-party technical account from the research
  team that built AVO, with five named authors and specific benchmark data.
  Paul Stack writes "The View from the AI Frontier," a practitioner blog about
  his own company's ("Swamp") production CI/verification practices — first-party,
  named, with measured figures. Claus Wilke is a computational-biology
  researcher who states he has "actually computationally designed viruses and
  other biological systems" and works on AI protein/peptide design — a
  domain-expert rebuttal, though published as a Substack opinion piece, not a
  peer-reviewed rebuttal, and explicitly written without having read the full
  paywalled article it responds to. The arXiv paper (Brzozowski & Chung,
  Samsung AI Center Warsaw / University of Warsaw) is a preprint (arXiv:2606.02184v2,
  cs.DL) — not yet peer-reviewed at time of extraction, but with specific,
  independently-queryable data (Zenodo API, DataCite timestamps, ResearchGate).
- **Scope**: Covers six topics: (1) AI-writing detection and Willison's cliché
  highlighter; (2) NVIDIA's AVO long-horizon agent architecture; (3) a one-line
  quip on MCP; (4) Paul Stack's critique of CI-with-agents and Fowler's
  rebuttal; (5) Claus Wilke's rebuttal of AI-bioweapon fears; (6) the arXiv
  ghost-persona paper. Does NOT cover any topic in depth on Fowler's own page
  alone — each topic's substance is either a linked page (AVO, Stack, Wilke,
  ghost paper) or a very short aside (the cliché-highlighter framing, the
  Petersen quip).

## Extracted Claims

### Claim 1: Fowler is skeptical of AI-generated prose but explicitly questions how accurate his own gut reaction to "LLM voice" is, framing it as comparable to generational reactions to unfamiliar writing tics
- **Evidence**: Fowler's own reflective framing, opening the fragment.
- **Confidence**: anecdotal (single practitioner's self-reported, self-questioning reaction)
- **Quote**: "Like many readers, I'm wary of AI generated prose." / "Not just do I find myself repelled by prose with an LLM-voice, I also wonder how accurate my reaction is. I'm old enough to see all sorts of new tic-phrases appear, and in the past would just chalk it up to youngsters or airport business books."
- **Our assessment**: This is a useful calibration note rather than a factual claim: even a practitioner who dislikes "AI voice" explicitly flags that his own detection instinct may not be reliable — which is directly borne out by Claim 2 below. This corroborates `blog-simonwillison-llm-cliche-highlighter.md`, which documents the tool Fowler links here but does not itself address detection-accuracy research; this fragment supplies that missing piece.

### Claim 2: Per a 2025 study cited on Wikipedia's "Signs of AI writing" page, human ability to distinguish LLM-generated text from human-written text is no better than random chance
- **Evidence**: A blockquote Fowler reproduces from the Wikipedia page he links (`en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing`), which itself cites a 2025 study. This is third-hand (study → Wikipedia → Fowler's fragment) and not independently verified against the underlying study in this note.
- **Confidence**: emerging (a specific, dated study result, but relayed through two layers of secondary summarization — this note did not fetch the underlying 2025 study or the live Wikipedia page directly)
- **Quote**: "Humans are notoriously bad at distinguishing human and LLM-generated text. While research on humans' abilities to detect AI-generated text is still limited, a 2025 study has shown that human ability to distinguish LLM text from human is no better than random chance."
- **Our assessment**: If accurate, this materially undercuts any guide recommendation that relies on human reviewers manually spotting "AI-sounding" text as a quality gate (e.g. skimming for LLM tells as in `blog-simonwillison-llm-cliche-highlighter.md`'s twelve-pattern checklist). The two approaches are complementary, not contradictory: a deterministic pattern-matcher can reliably flag known clichés (settled, per that note's Claims 5-9), while unaided human judgment cannot reliably distinguish AI from human prose in general (this claim). The guide should not conflate "flags known clichés" with "detects AI-generated text reliably."

### Claim 3: A separate 2025 study of German university theses found humans achieved only a 57% recognition rate for AI-generated text and 64% for human-generated text
- **Evidence**: Same Wikipedia blockquote Fowler reproduces, citing a second, more specific 2025 study.
- **Confidence**: emerging (specific, quantified figures from a named study population — German theses — but again relayed third-hand, not independently verified against the primary study)
- **Quote**: "Another 2025 study on German theses has shown that humans managed a "recognition rate of 57% for AI texts and 64% for human-generated texts"."
- **Our assessment**: These numbers (57%/64%, both close to a 50% chance baseline for a binary classification task) are consistent with Claim 2's "no better than random chance" framing and give it a concrete, if narrow, empirical anchor. Notably even human-generated text is only correctly recognized 64% of the time — the difficulty is symmetric, not just "humans can't catch AI," but "humans are unreliable classifiers of authorship in general" in this study population.

### Claim 4: NVIDIA's AVO ("Agentic Variation Operators") architecture sustains long-horizon autonomous agent work through two mechanisms — persistent memory (carrying forward implementations, evaluation results, and reasoning across the task) and a supervisor (an independent monitor that redirects the main agent when its search trajectory stagnates)
- **Evidence**: NVIDIA's own technical blog post (developer.nvidia.com), authored by five named NVIDIA researchers, describing the architecture used in a seven-day GPU-kernel-optimization run. Fowler reproduces the same two sentences verbatim in his fragment.
- **Confidence**: settled (first-party architectural description from the team that built the system, corroborated by the same exact text appearing in both the primary NVIDIA post and Fowler's fragment)
- **Quote**: "Persistent memory carries forward prior implementations, evaluation results, compiler and profiler outputs, and accumulated reasoning, allowing the agent to resume from the current state rather than repeatedly reconstructing the search." / "The supervisor monitors the broader trajectory for stagnation or repeated unproductive cycles and can redirect the main agent toward alternative strategies when needed."
- **Our assessment**: This is a concrete, named architectural pattern for exactly the "how do you keep an agent productive across a context window boundary and many hours of work" problem this corpus already covers from other angles (see Cross-References). The key distinction from `blog-anthropic-harness-long-running.md`'s approach is mechanism: that post's Opus 4.5 harness used *sprint decomposition with context resets* to manage long-horizon work, while AVO uses *persistent memory plus an independent supervisory process* that intervenes on stagnation — two different architectural answers to the same underlying problem (sustaining progress beyond what a single context window and a single undirected agent can achieve).

### Claim 5: In a seven-day continuous run on NVIDIA DGX B200 hardware, AVO (running Claude Opus 5) explored over 500 optimization directions, produced 40 committed kernel versions, and the resulting attention kernels outperformed cuDNN by up to 3.5% and FlashAttention-4 by up to 10.5%
- **Evidence**: NVIDIA's blog post, first-party benchmark data with named hardware and named comparison baselines (cuDNN, FlashAttention-4).
- **Confidence**: settled (specific, named, first-party benchmark figures; not independently replicated outside NVIDIA, and NVIDIA is both the architecture's builder and its evaluator)
- **Quote**: "In our attention-kernel study, AVO operated continuously for seven days, explored more than 500 optimization directions, and produced 40 committed kernel versions." / "the resulting multihead attention kernels outperformed cuDNN by up to 3.5% and FlashAttention-4 by up to 10.5% across the evaluated configurations."
- **Our assessment**: This is a concrete, quantified data point for what a well-architected long-horizon harness can achieve on a single hard task — seven days of continuous, largely unsupervised agent operation producing kernels that beat hand-tuned, widely-used baselines. It's a useful counterweight to this corpus's more common short-session (hours, not days) harness examples.

### Claim 6: The same underlying AVO architecture, adapted only by swapping the task-specific tools and interface, transferred from GPU-kernel optimization to the ARC-AGI-3 interactive reasoning benchmark, achieving a 100.00 RHAE score across all 25 public-set environments while using approximately 12% fewer environment actions than the VISTA system on the same underlying model — though NVIDIA explicitly cautions this is not a controlled ablation
- **Evidence**: NVIDIA's blog post, comparing AVO's action count (6,624) against VISTA's reported action count (7,542) for the same 183 public-set levels, both using Claude Opus 5.
- **Confidence**: emerging (a specific, named comparison with real numbers, but NVIDIA itself flags it as confounded — different agent backend, observation representation, memory system, and context management between AVO and VISTA)
- **Quote**: "AVO completed the full 25-environment public set with a 100.00 RHAE score, solving all 183 levels in 6,624 environment actions. For reference, VISTA reports 7,542 environment actions with Claude Opus 5 while completing the same 183 public-set levels." / "This should not be interpreted as a controlled ablation: the two systems differ in agent backend, observation representation, memory, context management, and other implementation details."
- **Our assessment**: The headline transfer result — the same architecture generalizing from GPU-kernel engineering to an unrelated interactive-reasoning benchmark — is the more load-bearing claim than the specific 12% efficiency number, which NVIDIA itself hedges heavily. The guide should cite the qualitative transfer result (system-level design, not model capability alone, drives long-horizon performance) as the stronger takeaway, and treat the 12%-fewer-actions figure as directional color, not a validated ablation result.

### Claim 7: Mickey Petersen characterizes MCP as "SOAP for Zoomers" in a one-line quip Fowler reproduces without further comment or elaboration
- **Evidence**: A single quoted line, sourced to an X/Twitter post, with no supporting argument given in Fowler's fragment.
- **Confidence**: anecdotal (an unelaborated one-line opinion from a single source, reproduced without independent commentary by Fowler)
- **Quote**: "MCP is SOAP for Zoomers."
- **Our assessment**: This is pure color — a pithy comparison of MCP to the enterprise-integration bureaucracy of SOAP-era web services, implying a critique of MCP's growing complexity or standardization overhead, but with zero supporting detail in the source. Not independently verifiable or actionable; recorded here for completeness but should not be cited in the guide as evidence of anything beyond "at least one commentator finds the comparison apt."

### Claim 8: Paul Stack argues that even with instant, high-capacity CI, agent-driven development has an architectural flaw: the agent only discovers its change doesn't work after crossing the PR boundary, so the feedback loop sits in the wrong place regardless of CI speed
- **Evidence**: Stack's own practitioner blog post (stack72.dev), describing his experience building CI/verification workflows for agent-generated code at his company ("Swamp"), plus CircleCI's 2026 State of Software Delivery report figures he cites (28 million workflows analyzed, throughput up 59% year over year, main-branch success rate down to 70.8%, a five-year low).
- **Confidence**: settled (a clearly articulated architectural argument from a named practitioner actively building the described alternative; the CircleCI figures he cites are attributed to a named report, not independently verified in this note)
- **Quote**: "An agent writes a change, opens a PR, and CI picks it up instantly. The compile fails, the agent pushes a fix, CI picks it up instantly again. A test fails, another fix, another instant run. Each iteration is fast, but the agent is still discovering that its change doesn't work only after it crosses the PR boundary. The feedback loop is in the wrong place regardless of how fast CI runs."
- **Our assessment**: This is a specific, well-reasoned framing of why agent-driven development volume strains CI differently than human-driven development did — the problem isn't throughput, it's where in the pipeline verification happens. This directly extends `blog-thoughtworks-gall-supervisory-engineering.md` Claim 6 (the "middle loop should be treated as a kind of filter stage... before anything touches your CI/CD pipeline") with a concrete implementation rationale for why that filter stage matters architecturally, not just organizationally.

### Claim 9: Stack's company ("Swamp") runs the agent's full verification cycle — linting, tests, compilation, agent-powered code review, and adversarial review — in an isolated local environment before any PR is opened, producing a structured "attestation" (a manifest recording the verified commit hash, config checksums, every step and its result, and the overall gate decision) that CI validates rather than re-executes
- **Evidence**: Stack's first-party description of his own company's production workflow architecture.
- **Confidence**: settled (specific, named architecture from a practitioner actively operating it, including the explicit trust-model caveat that an attestation proves config integrity but not execution integrity)
- **Quote**: "At Swamp, we're converting our CI process into Swamp workflows where the agent runs the full verification cycle in an isolated local environment before a PR is ever opened. Linting, tests, compilation, agent-powered code reviews, and adversarial reviews all run the same process CI would run, isolated from the authored code." / "When everything passes, the workflow produces an attestation: a structured manifest that records exactly what happened during verification. The commit hash that was verified, sha256 checksums of the config that governed it (review prompts, workflow definitions, CLAUDE.md), every step that ran with its result and duration, and the overall gate decision."
- **Our assessment**: This is a concrete, reusable pattern for the guide's CI/CD or verification chapter: separate "execution" (verification controls run somewhere, local or remote) from "coordination" (CI validates a structured record rather than re-running everything). Stack is explicit that the model has a real trust gap — "The attestation says the tests passed. It can't prove they ran" — and proposes config-integrity checksums plus environment isolation as partial mitigations, not a complete solution. The guide should present this as a promising but not fully trust-solved pattern.

### Claim 10: In a 35-PR shadow-validation test running both the pre-PR verification loop and traditional CI in parallel, Stack's team measured a "CI escape rate" (how often CI found a failure the verification loop missed) of zero
- **Evidence**: Stack's first-party account of an internal measurement at his company, explicitly framed as early/limited evidence.
- **Confidence**: emerging (a specific, named metric with a stated sample size, but the sample is small — 35 PRs — single-organization, and self-reported by the team that built the system being validated)
- **Quote**: "We're measuring what we call the CI escape rate: how often does traditional CI find a failure after the pre-PR verification loop declared the change ready? So far, across those 35 PRs, the escape rate is zero. CI hasn't found a single failure that the verification loop missed." / "35 PRs is early evidence thats this new flow is working for us. The shadow validation is how we'll know if it stops working, and it's how we'd recommend anyone migrate: run both systems, measure escapes, investigate every one, and only consider removing duplicated CI execution once the escape rate gives you confidence."
- **Our assessment**: The "escape rate" metric and the recommended migration methodology (run both systems in shadow, measure escapes, only remove duplicate CI execution once confidence is earned) is the single most actionable, reusable piece of guidance in Stack's post — a concrete way for any team to validate a "verify before PR" migration without betting production reliability on an unproven workflow change. The zero-escape-rate result itself should be cited as preliminary (Stack's own words: "early evidence"), not as a settled finding.

### Claim 11: Fowler rebuts Stack's framing, arguing that running full verification locally before pushing was always how disciplined Continuous Integration worked, and that CI's essential identity is a practice — not merely a server — that conflates two jobs (executing verification and coordinating merges) by design, because verification is a necessary precondition for a healthy mainline
- **Evidence**: Fowler's own argument, drawing on his established Continuous Integration and Continuous Delivery writing (linking to his own `continuousIntegration.html`, `DeploymentPipeline.html`, `ContinuousDelivery.html`, and `branching-patterns.html#mainline` articles).
- **Confidence**: settled (Fowler is a primary, original documenter of Continuous Integration practice; this is a direct restatement of long-held, widely-cited positions he has published elsewhere, applied here to the agent-CI question)
- **Quote**: "This is where I get to be the grumpy old guy, and point out that was always how Continuous Integration works. When I'm done with a change, first I pull (to get everyone else's change since I started), I build and test locally, and if all is well I push and let the CI server do its thing." / "Above all, Continuous Integration is a practice, not just the CI server. Yes, CI does conflate two jobs: executing verification and coordinating merges. But that's the point: verification is a necessary part of merging if we want to retain a healthy mainline."
- **Our assessment**: Fowler and Stack are not actually in strong disagreement — Fowler explicitly concedes "Stack is right that we should question how the deployment pipelines should work with agents in play" and "CI with humans relies on them being disciplined to run commit tests locally before pushing to the CI server - and that we can (and should) automate that when using agents." The substantive disagreement is narrower than the headline suggests: Stack frames "verify before PR" as breaking with how CI has worked; Fowler frames it as CI finally getting the discipline automated that human developers were supposed to (but often didn't) provide manually. Both agree agents should verify locally before opening a PR — this is corroboration dressed as rebuttal, not a contradiction, so no contradiction issue is filed.

### Claim 12: Computational design of biological systems remains extremely difficult even for domain experts and current state-of-the-art AI tools — PhD students in 2026 spend months or years designing simple peptide binders, and most designs fail, don't express, or are toxic — which Claus Wilke cites to argue that Noah Smith's "disgruntled teenager designs a civilization-ending AI supervirus" scenario is not realistic given the current gap between AI capability and what such a scenario requires
- **Evidence**: Wilke's own stated domain expertise ("my day job involves developing and evaluating AI systems for protein and peptide design") and first-hand observation of the state of the field.
- **Confidence**: emerging (a domain expert's first-hand professional assessment, but a single source, published as an opinion-blog rebuttal rather than a peer-reviewed risk assessment, and explicitly written without having read the full paywalled article it responds to)
- **Quote**: "Computational design of biological systems is unfathomably difficult. Experts who have dedicated their life to this topic routinely hit their head against the wall when nothing they try seems to work. PhD students in 2026 using state-of-the-art AI software are spending months or years trying to design simple peptide binders that inhibit some enzyme or pull down some protein, and the majority of their designs fail, or don't express, or are toxic. But in Smith's fictitious world a disgruntled teenager with no special training in biology can just solve a problem thousands of times more complicated than designing a peptide binder."
- **Our assessment**: This is tangential to the guide's core AI-native-engineering-practice focus (it's a biosecurity/AI-capability-calibration argument, not a harness, verification, or CI/CD claim), but it is a useful calibration data point for any guide discussion of AI capability hype: a domain expert directly contradicts a widely-circulated worst-case scenario using specific, checkable professional experience (PhD-student timelines, failure rates) rather than general skepticism. Low priority for guide inclusion given the topic mismatch with this corpus's subject matter.

### Claim 13: Large language models generating fictional experts do not merely default to individual high-probability names — they produce correlated "character ensembles" (recurring name pairs and trios whose co-occurrence rates far exceed chance), and these ensembles are model-family-specific (Claude: Elena Vasquez + Marcus Chen + Amara Okafor; Gemini: Aris Thorne + Lena Petrova; GPT: Elara Voss with no fixed partner)
- **Evidence**: A systematic probing methodology across accessible model checkpoints (two prompt sets of 30 prompts per checkpoint), reported in a preprint by Brzozowski and Chung (Samsung AI Center Warsaw / University of Warsaw).
- **Confidence**: emerging (a specific, methodologically described finding — repeated prompting across multiple checkpoints — but from a single, not-yet-peer-reviewed preprint; the underlying mechanism for *why* models produce correlated rather than independent name draws is not established, only observed)
- **Quote**: "These names do not exist. Elena Vasquez and Marcus Chen have appeared as volcano experts, astronauts, thriller protagonists, podcast hosts, and academic co-authors across hundreds of independently produced AI-generated documents, never having lived. We show that large language models do not merely default to high-probability individual names when generating fictional experts: they produce correlated character ensembles: pairs and trios whose co-occurrence rates far exceed chance and are consistent across independent generations."
- **Our assessment**: This is a novel, specific, and checkable finding for this corpus's LLM-reliability material. It's a different flavor of hallucination than the factual-wrongness rates documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md` (Claim 2: GPT-5.5 hallucinates on 85.53% of wrong AA-Omniscience answers vs. 36.18% for Claude Opus 4.7) — that note measures how often a model states something false; this paper measures a structural pattern in *what* a model fabricates when asked to invent a person, which turns out to be non-random and model-identifiable. The practical implication is significant: any pipeline that has an LLM generate example people, case studies, or "expert" personas (documentation examples, test fixtures, synthetic training data) risks silently reproducing the same handful of fictional names across unrelated outputs.

### Claim 14: These name priors are version-specific and are actively suppressed at model release boundaries — for example, the Claude "Elena Vasquez + Marcus Chen" pair co-occurred in 23% of pair-prompt responses on claude-sonnet-4-20250514, and that co-occurrence rate declined over subsequent checkpoints to full extinction in claude-sonnet-4-6, with only a residual 3% bump in claude-opus-4-7
- **Evidence**: The same preprint's checkpoint-by-checkpoint probing data (Table 2), which the authors present as evidence of active mitigation by the model developer at release boundaries rather than random drift.
- **Confidence**: emerging (a specific, quantified trend across named model checkpoints from a single not-yet-peer-reviewed source; the paper infers "active suppression" as the explanation but does not have direct access to Anthropic's training process to confirm intent)
- **Quote**: "The overall trend is downward: 23% → 3% → 0%, with a partial residual bump in haiku-4.5 and a near-zero tail in the 2026 models. The pair is fully extinct in claude-sonnet-4-6, claude-opus-4-7 shows a residual 3% consistent with incomplete suppression in the opus line."
- **Our assessment**: If the paper's inference is correct, this means fictional-name output patterns are a dateable behavioral fingerprint of a specific model checkpoint — useful for provenance/detection purposes (content bearing the "Elena Vasquez" signature can be roughly time-bounded to the checkpoints where that prior was strong), but also a reminder that this specific failure mode is checkpoint-dependent and not a permanent property of "LLMs" in general. Guide recommendations citing specific ghost names risk going stale as models are updated; the durable takeaway is the *pattern* (correlated ensembles, checkpoint-specific, suppressible), not the specific current names.

### Claim 15: This ghost-persona pattern has produced measurable, real-world contamination of scholarly infrastructure — the paper identifies 1,655 ghost-authored records on Zenodo (a CERN-operated repository minting real DataCite DOIs) claiming nonexistent journals, with server-side DataCite timestamps proving deliberate publication-date backdating, and 991 of those records registered in a single month
- **Evidence**: A direct Zenodo API query by the paper's authors (querying by two nonexistent journal names found in their ghost-author corpus), cross-checked against DataCite's server-assigned registration timestamps versus the user-controlled `publication_date` field.
- **Confidence**: settled (a specific, independently re-queryable dataset — the authors describe querying a public API and cite a verifiable discrepancy between two timestamp fields, one user-controlled and one server-assigned — though this note did not independently re-run the Zenodo/DataCite query to confirm the current record count)
- **Quote**: "On Zenodo, a CERN-operated repository that mints 10.5281/zenodo.* DOIs registered immediately with DataCite, we identify 1,655 ghost-authored records claiming nonexistent journals with fabricated publication dates. Server-side DataCite timestamps prove deliberate backdating; 991 records were registered in March 2026 alone." / "A baseline of one to two records per month through 2025 gives way to 991 uploads in March 2026 and 666 in April 2026, approximately 25 records per day for sixty consecutive days."
- **Our assessment**: This moves the ghost-persona finding from an interesting model-behavior curiosity to a concrete, at-scale infrastructure-integrity problem: real DOIs, registered with a real scholarly infrastructure provider (DataCite/Zenodo), citing fabricated venues and backdated to appear pre-LLM. This directly matters for any AI-native-engineering workflow that treats DOI-bearing records, Zenodo, ResearchGate, or similarly "verified-looking" identifiers as a trust signal when an agent is asked to research, cite, or ground claims in external sources (e.g. RAG pipelines pulling from academic databases) — the presence of a real, resolvable DOI is not sufficient evidence that a cited work or author is real.

## Concrete Artifacts

### AVO architecture summary (NVIDIA technical blog, developer.nvidia.com, Aug 21, 2026 — linked from Fowler's fragment, followed directly for this note)

```
System: AVO (Agentic Variation Operators), NVIDIA research
Model tested: Claude Opus 5 (primary); GPT-5.6 Sol (limited comparison)
Two sustaining mechanisms: persistent memory + supervisor

Task 1 — GPU-kernel optimization (attention kernels, NVIDIA DGX B200):
  Duration: 7 days continuous
  Directions explored: 500+
  Committed kernel versions: 40
  Result vs cuDNN: up to +3.5%
  Result vs FlashAttention-4: up to +10.5%
  Follow-up: adapted evolved kernel to grouped-query attention in ~30 min

Task 2 — ARC-AGI-3 (interactive reasoning benchmark):
  Metric: Relative Human Action Efficiency (RHAE)
  Result: 100.00 RHAE across all 25 public-set environments, 183/183 levels
  Actions used: 6,624 (AVO) vs 7,542 (VISTA, same model, same 183 levels)
  Caveat (NVIDIA's own words): "not a controlled ablation" — backend,
  observation representation, memory, and context management all differ
  between AVO and VISTA
  Reference baseline: ARC Prize reports ~30% for Claude Opus 5 (High
  reasoning) on the model alone, without an AVO-style harness
```

### Paul Stack's pre-PR verification / attestation model (stack72.dev, "AI Broke the Assumptions Behind CI," 26 Aug 2026 — linked from Fowler's fragment, followed directly for this note)

```
Company: Swamp (Stack's employer/product)
Old flow: agent writes change -> opens PR -> CI discovers failures ->
          agent fixes -> CI re-runs (repeat)
New flow: agent runs full verification cycle locally/isolated BEFORE PR:
          lint, tests, compile, agent-powered code review, adversarial
          review -> produces "attestation" -> PR opens already verified
          -> CI validates the attestation (fast) instead of re-executing

Attestation contents: verified commit hash, sha256 checksums of governing
  config (review prompts, workflow defs, CLAUDE.md), every step + result +
  duration, overall gate decision

Trust model (Stack's own caveat):
  - Config integrity: independently verifiable (CI re-hashes config at
    the claimed commit)
  - Result integrity ("tests actually ran"): NOT provable from the
    attestation alone — same limitation applies to CI runners themselves

Measured results (Swamp, self-reported):
  - PR cycle time: ~45 minutes open-to-shipped, ~half of that is
    acceptance tests
  - Pre-verification-loop CI failure rate: ~25% of PRs hit a CI failure
    needing a fix/round-trip
  - Shadow-validation test: 35 PRs run through both old CI and new
    verification loop in parallel; CI escape rate (CI catching a failure
    the loop missed) = 0 across all 35
```

### Ghost-persona findings (Brzozowski & Chung, "The Ghost Couple: Correlated LLM Name Priors and Their Haunting of the Web and Academic Publishing," arXiv:2606.02184v2 — linked from Fowler's fragment, followed directly for this note)

```
Model-family-specific default fictional-expert ensembles:
  Claude: Elena Vasquez + Marcus Chen (+ trio: Amara Okafor)
  Gemini:  Aris Thorne + Lena Petrova
  GPT:     Elara Voss (no fixed partner)

Claude checkpoint suppression curve (pair co-occurrence, 30 prompts/checkpoint):
  claude-sonnet-4-20250514:  23%
  ...(decaying across intermediate checkpoints)...
  claude-sonnet-4-6:          0% (fully extinct)
  claude-opus-4-7:            3% (residual)
  haiku-4.5:            partial residual bump noted

Prior-generation ghost (pre-Vasquez): Elena Rodriguez, first identified via
  Contrastive Decoding Diffing (CDD) on model weights (Brzozowski et al.
  2026); absent from all Claude checkpoints by October 2025 — the
  "generational handoff" from Rodriguez to Vasquez marks the version
  boundary between the two investigations.

Real-world contamination — Zenodo (CERN-operated, real DataCite DOIs):
  Query: two nonexistent journal names found in ghost-author corpus
  Records returned: 1,661 (1,655 with 10.5281/zenodo.* DOIs; 6 legitimate
    self-archived papers with real publisher DOIs, correctly excluded)
  Verifiable markers of all 1,655 ghost records:
    1. Nonexistent venue (no Crossref entry, no ISSN, no publisher)
    2. Fabricated publication_date (2020-2023 claimed) vs. server-assigned
       DataCite registration timestamp (99% registered March-April 2026)
    3. No publisher-DOI cross-reference in related_identifiers
  Upload timeline: baseline 1-2/month through 2025 -> 991 in March 2026,
    666 in April 2026 (~25/day for 60 consecutive days)
  Most frequent listed authors across all 1,655 records: Elena Vasquez
    (77 papers), Liam Chen (74), Sofia Jensen (48), Sofia Rodriguez (40),
    Julian Styles (39), plus a cluster of eight Italian-sounding names
    (Alessandro Bianchi, Giulia Esposito, Lorenzo Giardini, et al.) each
    appearing in exactly 17 papers
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-anthropic-harness-long-running.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-simonwillison-llm-cliche-highlighter.md`, and
`blog-thebatch-gpt55-hallucination-kimi-k26.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-simonwillison-llm-cliche-highlighter.md` (the tool Fowler links in
    Claim 1 of this note): that note's Claims 5-9 establish the tool is a
    deterministic, regex-based cliché detector, settled as "this is what the
    shipped code does." This note's Claims 2-3 add the piece that note does
    not cover — human detection accuracy in general (near-chance per one
    cited study, 57%/64% per another) — clarifying that the cliché tool
    catches *known, named patterns*, not AI-generated text in general, which
    unaided humans are shown to be unreliable at spotting.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 6 ("The middle
    loop should be treated as a kind of filter stage, one that needs to be
    passed before anything touches your CI/CD pipeline"): this note's Claims
    8-9 (Paul Stack's pre-PR verification loop and attestation model) are a
    concrete, named, production-operating implementation of exactly that
    filter-stage principle, with measured figures (Claim 10) that the Gall
    piece's purely conceptual framing lacks.

- **Contradicts**: None filed as a MINER.md §4a contradiction. Claim 11
  (Fowler's rebuttal of Stack) reads as a narrower disagreement than its
  framing suggests — both authors agree agents should verify locally before
  opening a PR; see the "Our assessment" note under Claim 11 for why this
  does not rise to a contradiction requiring a filed issue.

- **Extends**:
  - `blog-anthropic-harness-long-running.md` (Opus 4.5/4.6 harness evolution,
    sprint decomposition, "context anxiety"): this note's Claims 4-6 (AVO's
    persistent-memory-plus-supervisor architecture) describe a different
    architectural answer to the same underlying problem that source's Claims
    7-9 address — sustaining agent progress and coherence across a task that
    exceeds a single context window. That note's harness used context resets
    (sprint decomposition) as the Opus 4.5-era mitigation; AVO instead
    persists memory across the whole run and adds an independent supervisory
    process. Both sources converge on the meta-point that long-horizon agent
    capability is a property of the surrounding system, not the model alone —
    this note's NVIDIA material states that explicitly ("The model matters,
    but the model is not the entire agent"), directly paralleling that
    source's Claim 9 ("every component in a harness encodes an assumption
    about what the model can't do on its own").
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 2 (GPT-5.5
    hallucinates on 85.53% of wrong AA-Omniscience answers vs. 36.18% for
    Claude Opus 4.7): this note's Claims 13-14 (correlated, model-family- and
    checkpoint-specific fictional-persona generation) document a structurally
    different, non-overlapping hallucination phenomenon — not "how often does
    the model state something false," but "what specific, non-random content
    does the model fabricate when asked to invent a person, and is that
    pattern model-identifiable." Both sources independently support the
    broader point that hallucination behavior is measurable, model-specific,
    and version-dependent, but neither source's specific data extends the
    other's numbers.

- **Novel**:
  - **Correlated, model-family-specific "ghost" fictional-expert ensembles as
    a dateable behavioral fingerprint** (Claims 13-14): no existing corpus
    source documents this specific hallucination pattern — recurring,
    correlated fictional-person names rather than independent random
    fabrication, tied to specific model checkpoints and suppressed at release
    boundaries.
  - **Real-world scholarly-infrastructure contamination at measured scale**
    (Claim 15): the 1,655-record Zenodo finding, with a verifiable
    server-side-timestamp backdating proof, is the first corpus source
    documenting concrete, at-scale contamination of a real DOI-issuing
    infrastructure by LLM-generated fictional authorship.
  - **The "escape rate" metric and shadow-validation migration methodology**
    (Claim 10): no existing corpus source names this specific metric (how
    often does the system you're trying to replace catch a failure the new
    system missed) or this specific migration discipline (run both in
    parallel, measure escapes, only cut over once confidence is earned) for
    validating a CI/verification architecture change.
  - **AVO's persistent-memory-plus-independent-supervisor architecture**
    (Claim 4), and its demonstrated transfer across two unrelated task
    domains (Claim 6): a new, named, cross-domain-validated long-horizon
    agent architecture pattern not previously documented in this corpus.
  - **Third-party, study-cited data on human AI-text-detection accuracy**
    (Claims 2-3): no existing corpus source cites specific measured human
    detection-accuracy figures (near-chance; 57%/64%) for distinguishing
    AI-generated from human-generated text.

## Guide Impact

- **Chapter 02/03 (Harness Engineering / Long-Horizon Agents)**: Add AVO's
  persistent-memory-plus-supervisor architecture (Claims 4-6, Concrete
  Artifacts) as a second named reference architecture for long-horizon agent
  work, alongside the sprint-decomposition/context-reset pattern already
  cited from `blog-anthropic-harness-long-running.md`. Present both as
  different answers to the same problem — resuming/persisting state across a
  task that outlasts a single context window — rather than presenting one as
  superseding the other, since they were built for different task shapes
  (a single continuous 7-day run vs. discrete, checkpointed sprints).

- **Chapter 06 (Deployment & Ops / CI-CD)**: Add Paul Stack's pre-PR
  verification/attestation model (Claims 8-9, Concrete Artifacts) as a
  concrete pattern for restructuring CI around agent-driven development:
  move full verification (lint, test, compile, agent review, adversarial
  review) before the PR opens, and have CI validate a structured attestation
  rather than re-execute the work. Explicitly include the attestation
  trust-model caveat (config integrity is provable; result/execution
  integrity is not) so the guide doesn't overstate the pattern's maturity.
  Add the "escape rate" metric and shadow-validation migration methodology
  (Claim 10) as the recommended way to validate this kind of change before
  committing to it — run old and new systems in parallel, measure how often
  the old system catches something the new one missed, only cut over once
  that rate is near zero over a meaningful sample.
  Also add Fowler's rebuttal (Claim 11) as a grounding reminder: verifying
  locally before pushing is not a new invention for the agent era, it's
  automating a discipline CI has always depended on — this reframes "agents
  need a new CI model" as "agents make it finally practical to enforce the
  CI discipline that was always the point."

- **Chapter 03 (Verification) / Content-quality or RAG-grounding sections**:
  Add the human AI-text-detection-accuracy findings (Claims 2-3 — near-chance
  detection; 57%/64% recognition rates) as a caution against relying on
  manual "does this read like AI" review as a quality or authenticity gate.
  Pair with the existing cliché-highlighter coverage
  (`blog-simonwillison-llm-cliche-highlighter.md`) to make the distinction
  explicit: deterministic pattern-matching for *known* clichés is settled and
  useful; general human judgment about AI-vs-human authorship is not reliable.
  Separately, add the ghost-persona findings (Claims 13-15) as a concrete
  risk for any pipeline where an agent generates or cites people, "experts,"
  or sources — including a specific caution that a real, resolvable DOI is
  not sufficient evidence a cited work or author is genuine, given the
  documented Zenodo contamination at scale.

- **Not recommended for guide inclusion**: Claim 12 (Wilke's biosecurity
  rebuttal) and Claim 7 (the Petersen MCP quip) are outside this guide's
  AI-native-engineering-practice scope — recorded here for completeness per
  MINER.md's extraction depth requirement, but neither warrants a guide
  citation.

## Extraction Notes

- Fowler's fragment page returned full, clean text via a direct `curl` fetch
  (WebFetch was not needed as a fallback for this page). All quotes
  attributed to Fowler's own page were verified against the raw HTML source
  (`grep`-located and hand-checked for exact punctuation, including
  typographic apostrophes and curly quotes) rather than the tag-stripped
  plain-text rendering, to avoid any entity-decoding drift.
- Four linked pages were followed directly, within MINER.md's "up to 5"
  guidance: the NVIDIA AVO blog post (developer.nvidia.com, fetched via
  `curl`, HTML tags stripped), Paul Stack's CI article (stack72.dev, same
  method), Claus Wilke's biosecurity rebuttal (blog.genesmindsmachines.com,
  same method), and the arXiv ghost-persona paper (arxiv.org/pdf/2606.02184,
  fetched as PDF and extracted with `pdfminer.six`). The fifth and sixth
  linked items (Simon Willison's cliché-highlighter tool and the Wikipedia
  AI-writing page; Mickey Petersen's X/Twitter post) were not independently
  fetched — the cliché-highlighter tool already has its own dedicated source
  note in this corpus (`blog-simonwillison-llm-cliche-highlighter.md`), the
  Wikipedia page's relevant content is fully captured by Fowler's own
  blockquote of it (Claims 2-3), and Petersen's quip is a single line with no
  further substance to extract beyond what Fowler already reproduces.
- The arXiv PDF extraction via `pdfminer.six` initially interleaved a figure
  caption (Figure 4) into the middle of the "most frequent authors" sentence
  in the Zenodo section, splitting "Sofia Jensen" across a page/column break.
  This was resolved by reading the surrounding text on both sides of the
  interleaved caption before transcribing the author list into Concrete
  Artifacts, rather than guessing at or truncating the split name.
- No contradiction issues filed. The Stack/Fowler exchange (Claims 8-11)
  reads structurally like a disagreement but resolves, on close reading, into
  substantial agreement with a difference of framing/emphasis — documented
  in Claim 11's "Our assessment" rather than escalated to a filed
  contradiction, per MINER.md §4a's guidance that framing differences are not
  material contradictions.
- Confidence rated **emerging** overall: this note combines settled,
  first-party, directly-fetched claims with specific data (NVIDIA's benchmark
  figures, Stack's production metrics, the arXiv paper's Zenodo query
  results) alongside several claims resting on single, not-yet-peer-reviewed,
  or thirdhand sources (the arXiv preprint's checkpoint-suppression inference,
  the Wikipedia-relayed detection-accuracy studies, Wilke's un-peer-reviewed
  opinion-blog rebuttal). No claim in this note is corroborated by a second
  independent source outside its own originating publication.
