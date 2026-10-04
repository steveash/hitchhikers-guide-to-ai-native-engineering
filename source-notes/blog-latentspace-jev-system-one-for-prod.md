---
source_url: https://www.latent.space/p/jev
source_type: blog-post
title: "Jev: System One models for Prod, not God — with Diogo Almeida, CEO, TypeSafe AI"
author: Latent Space (swyx) interviewing Diogo Almeida (CEO, TypeSafe AI)
date_published: 2026-09-21
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: anecdotal
issue: "#3893"
---

# Jev: System One models for Prod, not God — with Diogo Almeida

> A 2h20m founder interview (full transcript read) in which Jev's creator explains the design rationale for a "System One" decision model, and gives concrete usage guidance (decompose into many small questions, structured state, thresholds and cascades, robustness over determinism) that is directly relevant to how we describe verification and agent decomposition, alongside a critique of function calling and KV-cache-bound coding agents.

## Source Context

- **Type**: blog-post (podcast episode with show notes and a full auto-generated transcript; transcript used for all quotes)
- **Author credibility**: Almeida describes himself in the episode as co-author of InstructGPT and a former OpenAI post-training researcher; the show notes say the same. He is now the CEO of the vendor whose product he discusses, and the host (swyx) is a friendly acquaintance who previewed the company before launch, so this is a primary but promotional source. All performance, reliability and "best in class" statements are unverified founder claims; the company publicly refuses to publish benchmarks.
- **Scope**: Why Jev exists (RLCD vs RLHF vs RLVR), refusals, benchmarks, model versioning, API primitives, how to build with Jev, use-case families, coding agents, and the founder's views on neo-labs. Not covered: RLCD technique details (the show notes call it "novel, unpublished"), any measured numbers, training data, or pricing. Show-notes links (cookbooks, the "Tyranny of the KV Cache" article, Jev coding-agent guide) were not followed.

## Extracted Claims

### Claim 1: Jev is a model class whose consumer is code, not a human, and the founder prefers "System 1" to "decision models" as the name
- **Evidence**: Founder's own definition; contrasts with pre-trained LLMs ("autocomplete of the internet"), RLHF chat models, and RLVR models.
- **Confidence**: emerging
- **Quote**: "I think these are-- is the class of models where the goal is for code to be the consumer."
- **Our assessment**: Useful framing for the guide's tool/agent chapters: a model optimized for in-process programmatic use is a different component from a chat model. Almeida explicitly warns that "decision models" is too narrow ("there's other types that are machine-native that are not decisions"), a mild pushback on Willison's preference for that term (see Cross-References).

### Claim 2: The three post-training "north stars" differ in what they optimize, and RLCD targets reliability for programmatic use
- **Evidence**: Assertion by the founder; RLCD is unpublished and no paper or ablation is offered.
- **Confidence**: anecdotal
- **Quote**: "RLCD is make it reliable for, programmatic use."
- **Our assessment**: The taxonomy (RLHF = please humans, RLVR = optimize programmatically verifiable benchmarks, RLCD = calibrated decisions) is a clean mental model, but the claim that RLCD works is untested outside the vendor. Treat as vendor positioning, not research finding.

### Claim 3: RLHF-style chat tuning rewards overconfidence and mode-dropping, which is why free-text models are poor decision-makers
- **Evidence**: Theoretical argument (mode-covering vs mode-dropping distributions, GAN analogy, LeCun's error-accumulation slide); no experiment shown.
- **Confidence**: anecdotal
- **Quote**: "You need to be hyper-confident in order to not go off the rails ‘cause the reward model will punish you so hard when that happens"
- **Our assessment**: Plausible and consistent with known sycophancy/overconfidence complaints, but presented as opinion. Relevant to the guide's treatment of LLM-as-judge: confidence from a chat-tuned model should not be trusted as calibrated.

### Claim 4: Refusals are a type error when a model is a software dependency
- **Evidence**: Argument by example (a refusal inside a background dependency randomly breaking downstream software); no incident data.
- **Confidence**: anecdotal
- **Quote**: "refusal is just, like, obviously a type error."
- **Our assessment**: A real engineering concern for unattended pipelines (a refusal is an unmodelled failure mode) even if we do not endorse removing safety training. He also states the opposing considerations are handled in code: ask many independent questions about refusal situations rather than "Should I refuse here?" (Claim 6).

### Claim 5: Prefer robustness (similar inputs, similar outputs) over bitwise determinism
- **Evidence**: Founder's design stance; describes a robustness test that inserts random IDs (UUIDs/"nonces") into the prompt and checks that outputs stay similar. No results given.
- **Confidence**: emerging
- **Quote**: "You want, given similar inputs, get similar outputs."
- **Our assessment**: A testable idea we can lift independent of Jev: perturb irrelevant tokens and measure output stability as an eval for any LLM-in-the-loop decision. He also says determinism costs money ("Determinism is something you can, like, trade off for better cost.") and Jev has no seed parameter, which is a real constraint for teams that rely on replayable tests.

### Claim 6: Decompose AI work into many small, independently measurable questions; fix failures by adding a question, a threshold and a test case
- **Evidence**: Practitioner advice from a founder who says he has queried the model more than anyone; refusal-handling example. Host notes that the same approach with small LLMs used to be slower, more expensive and worse.
- **Confidence**: emerging
- **Quote**: "Like, you fix the bug by adding that question in, adding the threshold, maybe remembering that as a test case, and now it is just solved forever."
- **Our assessment**: The strongest guide-relevant claim. It argues for replacing a monolithic prompt with an evaluable decision graph, where each branch is a regression test. The condition matters: it only pays off when the per-call cost and latency are near zero, which is what the vendor is selling. With ordinary LLM calls the host's own experiment ("It was slower, more expensive") points the other way.

### Claim 7: Big system messages are the wrong abstraction; pass structured state and ask parallel questions
- **Evidence**: Founder opinion tied to the Jev API (state, instructions and criteria as structured JSON).
- **Confidence**: anecdotal
- **Quote**: "System messages are, like, disgusting global variables where you just put everything in there"
- **Our assessment**: Colourful, and consistent with context-management advice elsewhere in the guide, but the argument is an analogy to programming practice, not evidence. His related claim that long instruction lists make models miss some instructions ("you hope that every single instruction gets nailed") is unquantified.

### Claim 8: Verify LLM calls by putting IDs on every message and asking one question per ID, paying for the shared state once
- **Evidence**: Usage tip given in the "verify everything" use-case family.
- **Confidence**: anecdotal
- **Quote**: "Put IDs on every, like, message, and then ask a question about each ID."
- **Our assessment**: A concrete observability/verification pattern (per-message classifiers over a long transcript) that depends on state caching or cheap prefix reuse. Specific to Jev's pricing model; we should not present it as a general technique.

### Claim 9: Use calibrated confidence for thresholds and escalation, optionally as a cascade to bigger models
- **Evidence**: Speculative design discussion; the host challenges "what if the calibration is wrong", and the founder replies "I didn't say that" (calibration is perfect) and concedes the model "will get many things wrong".
- **Confidence**: anecdotal
- **Quote**: "Like, if it’s super confident, then maybe it’s right. And if it’s in the middle, then you do the next bigger model, and you chain off from there."
- **Our assessment**: The cascade-by-confidence pattern is standard and sensible; what is unproven here is the calibration quality. The only user levers today are rewording, further decomposition, and threshold choice; fine-tuning is "in the cards" but explicitly "not a promise".

### Claim 10: Public benchmarks are rejected; teams should evaluate on their own workflow, and internal evals need discipline not to be gamed
- **Evidence**: Company policy; the founder says it hurt fundraising ("no one believed us"). Internal evals exist but are not published.
- **Confidence**: anecdotal
- **Quote**: "I believe that in the long run, it needs to be vibes and trust until you put it into a workflow and evaluate it for that workflow and measure it"
- **Our assessment**: The advice to evaluate on your own workflow is sound and consistent with the guide; the practical consequence is that none of the quality claims in this episode can be independently checked from this source. Another Jev-related note records that an outside benchmark and clones appeared within about a week (`blog-simonwillison-jev-decision-models.md` Claim 11), which is the likelier route to verification.

### Claim 11: Model versions will change quickly; long-term support is not promised
- **Evidence**: Direct statements about release policy, mentioning a possible temporary LTS of Jev 1.13.0.
- **Confidence**: settled (as a statement of the vendor's stated policy, not of outcomes)
- **Quote**: "we are not promising long-term support for the models because we think that there’s lots of improvements to have."
- **Our assessment**: Operationally important: pinning to a model version does not imply it will remain available, so decision thresholds tuned on one version may need re-validation. He also says versions are immutable once deployed ("We will not change our models when we deploy them.").

### Claim 12: Jev is a single-hop tool; quality drops as reasoning hops increase, and the System 1 / System 2 boundary is empirical
- **Evidence**: The host's own experiments on day one (not the founder's); the founder agrees the boundary is an empirical question.
- **Confidence**: anecdotal
- **Quote**: "Multi-hop is gonna. It starts to falls down."
- **Our assessment**: Consistent with Willison's "weak on numbers, dates and adversarial content" caveat. The speaker is the host, so the evidence is one practitioner's trial with no data shown.

### Claim 13: Coding agents' KV-cache coupling to one model makes routing, sub-agents and compaction hard; a multi-model agent could share state more cleverly
- **Evidence**: Speculation from an unpublished/forthcoming essay ("KV cache Rules Everything Around Me") and an internal design-patterns document; no implementation.
- **Confidence**: anecdotal
- **Quote**: "why routing is really hard, why sub-agents don’t seem to work, like, why compaction is such a hard problem"
- **Our assessment**: A fresh causal explanation for three recurring harness problems in the corpus: append-only, cache-friendly context locks agents into one model and makes state hand-off to cheaper sub-agents costly. His proposals (labelled sub-task trees, searchable history, read-only observer agents, an LLM arbitrating locks between parallel agents) are explicitly untested ("I have no guarantees that it’ll work").

### Claim 14: Established coding agents are built around a single-model world and open agents will adopt multi-model setups faster
- **Evidence**: Speculation; the founder says he does not "follow closely".
- **Confidence**: anecdotal
- **Quote**: "they’re built around a single model world"
- **Our assessment**: Interesting prediction but made by someone selling a second model type into harnesses. Flag as a conjecture, not market data.

### Claim 15: Function-calling interfaces are weak because developers cannot set per-action probabilities or thresholds, leaving "begging in a system message"
- **Evidence**: Anecdote from the founder's OpenAI tenure (he says he wanted a logit bias per function) plus the observation that coding agents are overfit to their built-in tools and use MCP/external tools poorly.
- **Confidence**: anecdotal
- **Quote**: "the solution is begging in a system message"
- **Our assessment**: Names a real gap: tool-selection steering is purely prompt-level in current harnesses. The claim that agents use external tools/MCP poorly because of overfitting is asserted, not measured; compare with the bash-vs-typed-tools result in the AINews digest note.

### Claim 16: Four use-case families: dark data, real-time intelligence in the loop, "verify everything", and smart software
- **Evidence**: The founder says the families were mapped "from first principles, like, long before release"; the near-term revenue volume is expected from dark data and coding agents. No customer data shown.
- **Confidence**: anecdotal
- **Quote**: "people hoarded big data, but they would not throw a LM at it ‘cause it was too expensive."
- **Our assessment**: Gives a buyer-side taxonomy for where cheap, fast classification matters. Founder admits he is "so out of touch" with the customer front line, so family rankings are a team hearsay.

### Claim 17: Pre-launch demand was weak; most trial users did not understand the product, then demand exploded and rate limits became the bottleneck
- **Evidence**: Founder recollection of launch week: waitlist sign-ups "don't matter", token volume passed a trillion tokens a day (host-framed milestone, not independently confirmed).
- **Confidence**: anecdotal
- **Quote**: "I would say, like, more than half the people we had play with it just did not get it."
- **Our assessment**: A failure-to-communicate data point about unfamiliar model shapes: the education burden (cookbooks, skills for coding agents) was a real cost. Traction numbers are self-reported.

### Claim 18: Optimize for intelligence per dollar on a Pareto frontier rather than raw capability, and accept being GPU constrained
- **Evidence**: Stated product strategy; no frontier plot is shown.
- **Confidence**: anecdotal
- **Quote**: "I don’t care how much smarter it is, it needs to be in the Pareto frontier."
- **Our assessment**: Useful for Ch02-style model-economics discussion as an articulation of the cost/quality objective, but the claim "while holding intelligence constant" is what the host calls load-bearing and what cannot be verified here.

## Concrete Artifacts

```
Primitive-to-control-flow mapping (Almeida, ~00:58:06-00:58:21 in transcript):
  choice  -> switch statement on an enum
  Noulli  -> if statement (a Bernoulli-style probability, "Bool-ish")
  score   -> sorting or thresholding (greater than / less than)
"there will be more types, and they will map into programming primitives."
```

```
Robustness test sketch (Almeida, ~00:42:31): insert random UUIDs ("nonces")
into otherwise identical prompts and require similar outputs from all of them.
Determinism (same input -> same output) is described as the wrong north star and
as tradable for cost.
```

```
Verify-everything usage tip (Almeida, ~01:37:09): assign an ID to every message in a
long state, then ask one question per ID, so the state is paid for once and many
questions run in parallel.
```

```
Show-notes pointers (not followed): Jev coding-agent guide and Jev skill,
"jev for linting", "compacting tool calls", essay "Tyranny of the KV Cache",
official patterns/cookbooks, Jev programming-language projects.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-jev-decision-models.md` Claim 4 (one state, many questions, evaluated in parallel) and Claim 6 (weak on numbers, dates, adversarial content) match the founder's description and the host's multi-hop observation (Claim 12 here). `blog-simonwillison-llm-typesafe-010a0.md` Claims 1-4 (yes/no returns a probability; choice and score modes) correspond to the primitives named in the Concrete Artifacts. `blog-latentspace-ainews-jev-system-one-model.md` Claim 6 (engineers link Jev to DSPy-style signatures and many small task-specific AI functions) fits the decomposition advice in Claim 6 here.
- **Contradicts**: None filed. Two soft tensions, neither a direct opposition so no contradiction issue was opened: (1) `blog-simonwillison-jev-decision-models.md` Claim 2 favours the name "decision models"; Almeida says the category is wider than decisions. This is a naming dispute, not a divergence in guide advice. (2) `blog-simonwillison-jev-decision-models.md` Claim 10 says evals matter more for decision models, while Almeida rejects public benchmarks; these agree once "own-workflow evals" is distinguished from "public benchmarks". `blog-latentspace-ainews-jev-system-one-model.md` Claim 7 (bash alone beat typed tool catalogs) is in contextual rather than direct tension with Claim 15 here.
- **Extends**: `blog-latentspace-ainews-jev-system-one-model.md` Claims 1, 2 and 5 (System One positioning, RLCD, not a general language model) with first-person rationale and API-design reasoning; `blog-simonwillison-jev-decision-models.md` Claim 9 (bias concerns) is not addressed by the founder, who instead argues the API should not police use.
- **Novel**: The refusal-as-type-error argument; the robustness-over-determinism test; the "fix a bug by adding a question, threshold and test case" workflow; explicit no-LTS model versioning policy; the KV-cache explanation for why routing, sub-agents and compaction are hard; the function-calling logit-bias critique.

## Guide Impact

- **Verification chapter (Ch03)**: Add the "decompose into many small, independently thresholded questions, and turn every failure into a new question plus test case" pattern (Claim 6) as a vendor-reported practice, labelled anecdotal, with the condition that it needs very cheap, fast calls. Add the perturbation (nonce/UUID) robustness test (Claim 5) as an eval idea that is usable with any model.
- **Model economics (Ch02)**: Cite Claim 11 for the operational point that model versions may not receive long-term support, so tuned thresholds need re-validation on each release; cite Claim 18 for the intelligence-per-dollar framing, flagged as unverified vendor positioning.
- **Tool design / agent patterns (Ch04)**: Cite Claims 13 and 15 as a hypothesis, not a finding, on why tool steering is prompt-only and why append-only context coupling makes sub-agent hand-off and compaction hard; recommend revisiting once the founder's essay is mined as its own source.
- **Do not**: use any capability or reliability number from this source in the guide; none are provided and the company declines to publish them.

## Extraction Notes

- Read the entire transcript (~182k characters; roughly 2h20m) plus the show notes. The post is not paywalled; the transcript was fetched directly from the page HTML. One stretch of the transcript (InstructGPT/OpenAI history and neo-lab commentary, ~01:55-02:05) was read for context but yields no extractable engineering claims, so none are extracted from it; the founder's disparagement of neo-labs and the "pace the frontier" safety discussion were judged out of scope for the guide.
- Quotes are copied from the transcript; speaker disfluencies and the transcript's punctuation were retained. Some quotes are fragments to avoid splicing non-adjacent sentences.
- Timestamps in Concrete Artifacts are the approximate transcript positions where the topic starts.
- Claims about OpenAI, Anthropic or other third parties made in the episode were not extracted as facts.
- Confidence is `anecdotal` overall: one founder, no data, and a vendor with a stated policy against publishing benchmarks.
