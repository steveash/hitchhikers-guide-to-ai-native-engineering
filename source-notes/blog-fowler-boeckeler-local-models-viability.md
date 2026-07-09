---
source_url: https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-factors.html
source_type: blog-post
title: "Viability of local models for coding"
author: Birgitta Böckeler (Distinguished Engineer, Thoughtworks)
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: anecdotal
issue: "#1670"
---

# Viability of local models for coding

> Böckeler's two-part martinfowler.com memo (factors + experiences) is a
> four-week, hands-on evaluation of running local models for *agentic* coding
> (not just autocomplete) on two Apple Silicon Macs. It supplies a concrete
> factor taxonomy (RAM, quantization, MoE architecture, reasoning, context
> window, harness overhead), a landed-on model (Qwen3.6 35B MoE), and — most
> valuably — a documented divergence between manual and automated evaluation
> of the *same* models on the *same* tasks, plus an unexplained hardware-
> dependent quality difference on the *same* model and settings.

## Source Context

- **Type**: blog-post, two-part series on martinfowler.com's "Exploring Gen AI"
  memo series (Thoughtworks technologists' gen-AI explorations). Part 1,
  "Viability of local models for coding" (2026-07-07), is the primary source
  named in the issue; Part 2, "Experiences with local models for coding"
  (2026-07-08, `martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-experiences.html`),
  is the explicitly-promised follow-up ("Coming up... In my next memo, I will
  dive more deeply into the types of tasks I gave the models") and was
  published the day after Part 1 and before this note's extraction — both were
  read in full per MINER.md §1's instruction to follow substantive linked
  pages, since Part 2 contains the concrete task-level evidence that Part 1's
  factor taxonomy only summarizes.
- **Author credibility**: Birgitta Böckeler is a Distinguished Engineer and
  AI-assisted delivery expert at Thoughtworks with over 20 years of experience
  as a developer, architect, and technical lead. This is first-person,
  hands-on practitioner testing (her own two Macs, her own tasks, her own
  vibe-coded automated eval harness) — not a vendor announcement or an
  independently reproduced benchmark. She is explicit about the limits of her
  own method ("unstructured type of evaluation," "still quite messy and hard
  to evaluate").
- **Scope**: Covers *agentic* local-model coding specifically (not
  autocomplete), on two machines (M3 Max 48GB, M5 Pro 64GB), using LM Studio
  as the runtime and OpenCode/Pi as harnesses, testing Qwen3.6 and Gemma 4
  variants at Q4/4BIT quantization. Does not cover: non-Apple-Silicon
  hardware, quantization levels other than Q4/4BIT, QAT variants, code
  *quality* (only functional correctness was assessed), or non-JS/TS/Python
  tech stacks in the systematic comparison.

## Extracted Claims

### Claim 1: RAM is the core constraint on whether a local model can run at all for agentic coding, and Böckeler's viable working range was 15-25GB models with up to 64K context, in harnesses with no Skills/MCP servers active
- **Evidence**: Direct summary statement from Part 1's factor overview, plus a first-person account of a runtime crash on a 48GB-weight model.
- **Confidence**: anecdotal (two machines, own hardware, own model set)
- **Quote**: "Runnability: RAM is the core constraint. I used models between 15-25GB, context windows of maximum 64K, harnesses OpenCode and Pi with zero Skills and MCP servers active"
- **Our assessment**: This is a concrete, actionable RAM budget for practitioners scoping local-hardware requirements: 15-25GB of *model* weight is "comfortable," 30GB "stretches it a lot," and 48GB weights ran initially but "quickly crashed." Notably the budget assumes a bare harness (no Skills, no MCP servers) — any additional harness overhead eats directly into this same RAM ceiling via the context window (Claim 8).

### Claim 2: Tool calling was tricky and often failed, but the models could usually self-recover; small models are meaningfully more viable for autocomplete than for agentic use
- **Evidence**: Direct first-person summary plus a concrete example of the failure mode (wrong parameter names).
- **Confidence**: anecdotal
- **Quote**: "Tool calling was tricky still, the models often failed, but can usually self-recover from their failures. This is a key component of agentic coding specifically. Without it, you can still go the old-fashioned way of copying and pasting from a chat window of course. And small models are definitely a lot more viable for auto complete than agentic use."
- **Our assessment**: The self-recovery detail matters more than the failure rate itself — a model that fails tool calls but reliably retries with corrected syntax is still usable in an agentic loop, whereas one that fails silently is not. The example given elsewhere in the source (`file.path` instead of `filePath`) is a schema-naming error, not a reasoning error, which ties directly to Claim 7's harness-schema-fragmentation point: the same model may fail tool calls against one harness's naming convention and succeed against another's.

### Claim 3: All models tested had reasoning enabled by default and often looped unproductively ("Wait, ...", "Actually, ..."); running the same automated eval with reasoning off was both faster and equal-to-slightly-better in quality
- **Evidence**: Direct first-person observation plus a controlled-ish comparison (same automated setup, reasoning toggled off).
- **Confidence**: anecdotal (small number of automated eval runs, not a large-sample study)
- **Quote**: "I also did a few runs of my automated setup with reasoning off - and lo and behold, it's not only faster (which was to be expected), but also performed the same to slightly better! A good reminder that reasoning is not always necessary, and can sometimes even be counterproductive."
- **Our assessment**: This directly contradicts the intuitive assumption that reasoning tokens are a pure quality lever with only a speed cost. For small local models specifically, unproductive reasoning loops appear to be a real failure mode, not just a latency tax — worth flagging as a first knob to try disabling when a small local model's agentic output is disappointing, before concluding the model itself is inadequate. This claim is scoped to Böckeler's own small automated-eval sample; she does not claim this generalizes to larger models or cloud models.

### Claim 4: The Qwen3.6 35B-A3B MoE model gave the best balance of parameter count, RAM footprint, speed, and quality of any model tested, and became Böckeler's go-to local model after the four-week evaluation
- **Evidence**: Direct first-person conclusion stated in both Part 1 and Part 2, plus the final "default setup" configuration Böckeler settled on.
- **Confidence**: anecdotal (single practitioner, small model set: Qwen3.6 35B MoE, Qwen3.6 Coder Next 80B MoE, Gemma 4 12B, Gemma 4 26B, Gemma 4 31B)
- **Quote**: "The Qwen3.6 35B MoE model was by far giving me the best balance between number of parameters and RAM usage, and therefore runnability and quality of outcomes." / "However, based on this experience I do have a go-to model that I'm using locally now, which is Qwen3.6 35B MoE. It offered the best balance of capability, speed and RAM footprint among what I tried."
- **Our assessment**: This is the single most citable "if you're going to try one local model for agentic coding right now" recommendation in the source, backed by roughly four weeks of mixed manual/automated/day-to-day use rather than a one-off test. It should be cited with the caveat that the comparison set is small (five model variants, two labs: Qwen and Gemma) and JS/TS-and-Python-heavy in the systematic tasks.

### Claim 5: The exact same model (Qwen 35B MoE) and settings produced a large, unexplained quality difference between the 48GB and 64GB machines in automated evaluation — 5/7 task failures on the 48GB machine vs. 1/7 on the 64GB machine
- **Evidence**: Direct first-person automated-eval result comparison across the two machines for Task 2 (country bar chart), plus a similar unexplained pattern noted for Task 1 (better coding ability on the 64GB machine).
- **Confidence**: anecdotal (7-run automated eval per machine; single task pair; author explicitly says she cannot explain it)
- **Quote**: "In the automated setup, I ran this task with Qwen 35B MoE 7 times, and it failed to properly solve it 5 out of those 7 times... Here is where it gets interesting though: I then ran the evals again on the M5 machine with 64GB, and it failed only once! Which was really surprising to me, because I was expecting the two machines to deliver different speeds, but I did not expect this vast difference in quality of output with the same model settings. This remains a mystery to me."
- **Our assessment**: This is the most surprising and highest-value finding in the source for a corpus focused on rigor and evaluation methodology: identical model, identical settings, identical task, different only in host hardware, produced a 5/7-fail vs. 1/7-fail split. Böckeler explicitly does not have an explanation (she speculates about MoE expert-loading differences in Part 1 but flags it as an unverified hypothesis: "I'm not sure if that's true, but it's the only sensible hypothesis I have so far"). This should be flagged in the guide as a caution against generalizing local-model quality results across even nominally-identical hardware tiers without re-testing on the target machine.

### Claim 6: Manual evaluation and automated evaluation of the identical model on the identical task produced contradictory results — Gemma 4 26B was "the most successful" manually but failed 3/3 times in the automated setup
- **Evidence**: Direct first-person comparison across Böckeler's own Phase 1 (manual) and Phase 2 (automated) evaluation of Task 1 (bar chart cumulation).
- **Confidence**: anecdotal (single task, small sample sizes in both phases)
- **Quote**: "Gemma 4 26B was the most successful here. It did implement the full set of things I asked for." (Phase 1) followed by, in Phase 2: "Frustratingly, the automated setup did not confirm the manual experience. Gemma 4 26B failed to deliver a functionally correct solution 3/3 times, wheras Qwen3 35B MoE succeeded 2/2. The failure was always that it didn't properly implement the x-axis labels I asked for."
- **Our assessment**: This is a methodologically important finding independent of local models specifically: manual, conversational, back-and-forth evaluation and automated one-shot evaluation of the *same model on the same task* can disagree entirely about which model "wins." Böckeler's own explanation is that the automated setup expects the agent to "one-shot" the problem with only a browser as a self-correction sensor, which is "not fully realistic" — manual evaluation implicitly allows conversational correction that automated one-shot evaluation does not. This generalizes as a caution for any team building automated model-comparison evals: a one-shot automated harness measures something different from real conversational usage, and the two can rank models differently.

### Claim 7: Coding harnesses use different tool-call parameter naming schemas for the same operation (file editing), and this schema fragmentation compounds the small-model tool-calling reliability problem
- **Evidence**: Direct enumeration of three harnesses' edit-tool parameter names.
- **Confidence**: settled (directly checkable against each harness's own tool schema; Böckeler links to Pi's and OpenCode's schema docs and states Claude Code's naming is what Claude Code itself reported when asked)
- **Quote**: "I mentioned above that small models still struggle with tool calling - and it probably doesn't help that each harness has slightly different schemas for the basic tools." The three schema names themselves are extracted verbatim in Concrete Artifacts, below.
- **Our assessment**: This is a concrete, harness-engineering-relevant data point: three coding harnesses (Pi, OpenCode, Claude Code) all implement "edit a file" with a two-string old/new parameter pair, but use three different naming conventions (`old_text`/`new_text`, `oldString`/`newString`, `old_string`/`new_string`) for functionally identical semantics. For large frontier models this variance is presumably absorbed without issue, but Böckeler frames it as a contributing factor to small local models' tool-calling failures — a model fine-tuned or more heavily trained against one schema convention may be more failure-prone against another. This is the kind of harness-portability cost that's invisible until you try to run the same task across multiple harnesses with a weaker model.

### Claim 8: Runtimes' default context window size is far too small for agentic coding; Böckeler found 32K a workable minimum and 64K a more reliable default, but even 64K stretched available RAM on both test machines
- **Evidence**: Direct first-person statement plus the explicit RAM-vs-context-window tradeoff.
- **Confidence**: anecdotal
- **Quote**: "The default size configured in the runtimes is far too small for agentic coding, it has to be set to at least 32K, if not 64K." followed by "For small tasks I could sometimes work with 32K, but often I had to increase to 64K, so that seems to be a good default minimum. As the models themselves were already pushing the boundaries of my available RAM, I'm not sure how how much more I could still increase it, even on the 64GB machine..."
- **Our assessment**: A concrete, actionable configuration default for anyone setting up a local model for agentic coding: don't trust the runtime's out-of-the-box context window setting, and budget for 32-64K minimum on top of model weight RAM. This is a specific number the guide does not currently have for local-model context sizing, and it directly interacts with Claim 1's RAM budget — context window and model size compete for the same finite RAM pool.

### Claim 9: The choice of task is the single biggest factor determining whether a small local model is viable, more so than any hardware or model-configuration factor — with four concrete sub-dimensions: need for code research, number of files to edit, specificity of instructions, and tech stack
- **Evidence**: Direct first-person reflection after running both systematic (JS/TS) and less-systematic (Bash/Python) tasks across the four-week evaluation.
- **Confidence**: anecdotal (small, non-representative task set — two systematic web-frontend tasks plus informal Bash/Python scripting)
- **Quote**: "As the tasks are so important, I'm giving you some details here for two of them, to help inform your interpretation of my results. The choice of task is ultimately one of the biggest factors that determines viability of small, locally run models - it's all about expectations." Sub-dimensions, verbatim: "Will it require code research, or can the prompt point at the specific files to change?" / "How many files might it have to edit?" / "How specific are the instructions?" / "What is the tech stack?"
- **Our assessment**: This reframes "is model X viable for local agentic coding" as an underspecified question — viability is a function of (model, hardware, task) jointly, not model alone. The practical implication for practitioners: when scoping which of their own team's tasks are candidates for local-model delegation, evaluate against these four dimensions (does the task require discovery/search, how many files, how vague can the prompt be, what language) rather than relying on a general "is this model good enough" verdict from someone else's benchmark.

### Claim 10: In day-to-day use, Böckeler's most successful local-model workflow was planning with a large cloud model (Claude Sonnet) and delegating only the coding execution to the local model, for small, well-defined, pre-scoped tasks
- **Evidence**: Direct first-person account of her day-to-day task mix and its outcomes, including one task (building a game from scratch) that "started well, but fell apart for more complex logic."
- **Confidence**: anecdotal
- **Quote**: "Building a game from scratch (planning with Claude Sonnet, then delegating coding execution to the local model) - started well, but fell apart for more complex logic." Her summarized default workflow, stated separately: "I reach for it when I have small, straightforward tasks, often pre-planned by a bigger model"
- **Our assessment**: This is a concrete instance of a large/small model division of labor (planning on a frontier cloud model, execution on a local model), scoped explicitly to tasks that are small and well-defined enough for the weaker model's context and reasoning ceiling. It is the local-model-specific version of a "model mixing across orchestration tiers" pattern, with the local model's failure mode ("fell apart for more complex logic") providing the concrete boundary condition for when to route back to a bigger model.

### Claim 11: A colleague (Jigar Jani) does "almost all" of his coding on a real-world Python/React codebase with the same local model (Qwen 35B MoE, 4BIT) on a 48GB MacBook, using harness skills for code search/understanding, and stresses that code review remains essential
- **Evidence**: Second-hand but named, attributed account from a specific colleague's regular (not one-off) usage.
- **Confidence**: anecdotal (single named second-hand practitioner account, relayed by the author, not independently verified by the Miner)
- **Quote**: "My colleague Jigar Jani works with Qwen 35B MoE (4BIT) regularly on a 48GB Macbook, and does almost all of his coding with it, on a \"real world\" Python and React codebase. He is continuously enhancing his harness with skills, and has found Graphify and Understand Anything to be particularly useful to help the models with code search and understanding. Jigar finds it quite useful and sees improvements as he improves the harness, but he also stresses that code review is super important."
- **Our assessment**: This is a second, independent (if less rigorously documented) corroboration of Claim 4 — the same model, same quantization, on a smaller 48GB machine, sustaining "almost all" coding for one practitioner on a real production-style codebase, not just isolated test tasks. The emphasis on augmenting the harness with code-search/understanding skills echoes Claim 7's point that harness composition (not just the raw model) determines local-model viability, and the explicit "code review is super important" caveat is consistent with the source's overall finding that quality is uneven and needs verification.

### Claim 12: Böckeler's overall verdict is that local models for agentic coding are "still not ready for a simple 'plug and play' experience," frustrating and hard to evaluate, and remain "very far away" from the capability of current frontier cloud models — while still being worth incorporating selectively into a workflow
- **Evidence**: Direct closing statement synthesizing the four-week evaluation.
- **Confidence**: anecdotal
- **Quote**: "It has been a frustrating experience with sometimes confusing results, I therefore find that it's definitely not a plug-and-play type of experience yet. [...] Overall though, the agentic coding capabilities are definitely very far away from what I've now become used to with bigger models."
- **Our assessment**: This is the source's own explicit bottom line, and it should be preserved verbatim rather than summarized more optimistically or more pessimistically than the author intended: not unusable, not ready-to-recommend-broadly, but selectively useful (Claims 4, 10, 11) for small, well-scoped, often pre-planned tasks, given hands-on setup effort and active monitoring.

## Concrete Artifacts

### Hardware and runtime setup (verbatim/paraphrased from Part 1)
```
Machines:       Apple M3 Max, 48GB RAM  |  Apple M5 Pro, 64GB RAM
Runtime:        LM Studio (author's stated preference, for UX)
Harnesses:      OpenCode, Pi (Claude Code deliberately avoided locally —
                "it apparently would burden the context window quite a bit")
Quantization:   All models tested at Q4 / 4BIT (no QAT variants tried)
Context window: Runtime defaults are "far too small"; 32K workable minimum,
                64K more reliable, but stretches RAM on both machines

Source: Birgitta Böckeler, martinfowler.com, "Viability of local models for
coding" (2026-07-07)
```

### Models tested (verbatim list, Part 1)
```
Qwen3
  Qwen3.6 35B-A3B MoE Q4 GGUF          (22 GB)
  Qwen3.6 Coder Next 80B MoE GGUF      (45 GB)

Gemma 4
  Gemma 4 12B Q4 GGUF                  (7.5 GB)
  Gemma 4 26B 4BIT MLX                 (15.6 GB)
  Gemma 4 31B 4BIT MLX                 (29 GB)

Final default setup (Part 2, "at the time of publishing"):
  Model:          qwen/qwen3.6-35b-a3b, Q_4_KM quantization, GGUF
  Reasoning:      off (LM Studio: Inference > Settings > Custom Fields >
                  Enable Thinking > disable)
  Context window: max (LM Studio: Load > Context and Offload > Context
                  Length > drag slider to max)
  Harnesses:      OpenCode or Pi
  Use case:       small, straightforward tasks, often pre-planned by a
                  bigger model

Source: Birgitta Böckeler, martinfowler.com, Parts 1 and 2 (2026-07-07/08)
```

### Harness tool-call schema naming for "edit a file" (verbatim, Part 1)
```
Pi:          old_text / new_text
OpenCode:    oldString / newString
Claude Code: old_string / new_string (per the harness's own self-report)

Source: Birgitta Böckeler, martinfowler.com, "Viability of local models for
coding" (2026-07-07)
```

### Manual vs. automated evaluation divergence, Task 1 (bar chart cumulation) — verbatim, Part 2
```
Phase 1 (manual, conversational):
  "Gemma 4 26B was the most successful here. It did implement the full
  set of things I asked for."

Phase 2 (automated, one-shot):
  "Gemma 4 26B failed to deliver a functionally correct solution 3/3
  times, wheras Qwen3 35B MoE succeeded 2/2. The failure was always that
  it didn't properly implement the x-axis labels I asked for."

Source: Birgitta Böckeler, martinfowler.com, "Experiences with local models
for coding" (2026-07-08)
```

### Same-model, cross-machine quality divergence, Task 2 (country bar chart) — verbatim, Part 2
```
M3 Max 48GB, Qwen 35B MoE, 7 automated runs: failed 5/7
M5 Pro 64GB, Qwen 35B MoE, same settings, re-run: failed 1/7

"I was expecting the two machines to deliver different speeds, but I did
not expect this vast difference in quality of output with the same model
settings. This remains a mystery to me."

Source: Birgitta Böckeler, martinfowler.com, "Experiences with local models
for coding" (2026-07-08)
```

## Cross-References

- **Corroborates**: `blog-ronacher-local-models-focus-polish.md` — Both
  sources independently converge on: (1) local model setup/configuration is
  materially harder than hosted APIs (Ronacher's engine/quantization/template/
  context-size/JSON-config enumeration vs. Böckeler's own multi-week
  evaluation effort); (2) tool-calling reliability is the key open problem for
  *agentic* (not autocomplete) local coding — Ronacher's tool-parameter-
  streaming gap and Böckeler's Claim 2/7 tool-call failure-and-schema
  observations are two distinct facets of the same underlying immaturity; (3)
  the "not plug-and-play yet" verdict (Böckeler's Claim 12 vs. Ronacher's
  "runnable ≠ finished" framing) — both practitioners land on the same
  overall assessment via different evaluation methods (Ronacher: infrastructure
  audit; Böckeler: hands-on task testing).
- **Extends**: `blog-simonwillison-ornith.md` (Claim 8) — Willison's single
  positive anecdote (35B GGUF via LM Studio + Pi "handled with ease" on two
  Datasette code-navigation tasks) is a much smaller and more favorable data
  point than Böckeler's four-week, multi-task, multi-phase evaluation of a
  similarly-sized model class on the same LM Studio/Pi combination. Böckeler's
  Claims 5 and 6 (manual/automated divergence, cross-machine quality variance)
  supply the methodological texture that a single anecdotal session cannot:
  the same model/harness pairing that "handles" simple code-navigation tasks
  "with ease" can still fail the majority of a slightly more involved
  file-editing task depending on evaluation method and host machine.
- **Extends**: `blog-google-gemma-4-12b-laptop-ai-edge.md` — that note
  documents Google's own first-party tooling (Google AI Edge Gallery/Eloquent,
  `litert-lm serve`) for running Gemma 4 12B locally as an OpenAI-compatible
  endpoint. Böckeler independently tested Gemma 4 12B/26B/31B (Concrete
  Artifacts, above) via LM Studio/GGUF/MLX rather than Google's own tooling,
  and found Gemma 4 26B to be "the most successful" in one manual test (Claim
  6) but unreliable in the corresponding automated re-test — an independent,
  vendor-neutral data point on Gemma 4's real-world local-coding viability
  that complements Google's own product-announcement framing.
- **Contrasts** (not a contradiction): `blog-latentspace-glm52-open-frontier-parity.md`
  Claim 8 (a Reddit commenter's claim that large local models become
  impractical at 50K+ context due to prompt-processing/generation throughput,
  distinct from simply not fitting in memory) — Böckeler's own experience
  (Claim 8: 32-64K context already "pushing the boundaries" of available RAM
  on both her machines) is a smaller-model, RAM-bound version of the same
  underlying distinction: even before throughput becomes the bottleneck,
  RAM competition between model weights and KV cache limits usable context.
  Not a contradiction — the two sources describe the same tradeoff at
  different model-size tiers (Böckeler: 15-30GB models; the Reddit thread:
  hundreds-of-GB models).
- **Novel**: The manual-vs-automated evaluation divergence for the identical
  model and task (Claim 6) and the identical-model/identical-settings
  cross-machine quality divergence (Claim 5) are both new to this corpus — no
  existing source note documents either an evaluation-methodology-dependent
  ranking flip or an unexplained hardware-dependent quality (not just speed)
  difference for the same model. The four-dimension task-viability framework
  (Claim 9), the harness tool-schema naming comparison across three specific
  harnesses (Claim 7), and the concrete 32-64K context-window sizing
  recommendation (Claim 8) are also new specifics not previously documented
  in the corpus's local-model material.

## Guide Impact

- **Chapter 01 (Daily Workflows) — "Multi-Model Cooperation" / "Model mixing
  across orchestration tiers"**: Add local models as a further orchestration
  tier below existing cloud-model tiering, using Claim 10's concrete pattern
  (plan with a frontier cloud model, delegate execution of small/well-defined/
  pre-scoped tasks to a local model) and its documented failure boundary
  ("fell apart for more complex logic"). Claim 9's four task-viability
  dimensions (research needed, file count, instruction specificity, tech
  stack) give practitioners a checklist for deciding which tasks are
  candidates for this tier.
- **Chapter 02 (Harness Engineering) — tool-call schema section**: Add
  Claim 7's concrete three-harness comparison (Pi's `old_text`/`new_text`,
  OpenCode's `oldString`/`newString`, Claude Code's `old_string`/`new_string`)
  as a specific illustration of harness-schema fragmentation, framed as a
  contributing factor to weaker models' tool-calling failures — relevant to
  any team building or choosing a harness with local-model compatibility in
  mind.
- **Chapter 03 (Verification) — evaluation methodology**: Add Claim 6 (manual
  vs. automated evaluation ranking flip for the identical model/task) as a
  caution for teams building automated model-comparison evals: a one-shot
  automated harness measures something different from conversational,
  self-correcting usage, and the two can disagree about which model is
  better. Pair with Claim 5 (unexplained cross-machine quality variance for
  identical settings) as a reminder to re-validate local-model evaluation
  results on the actual target hardware rather than assuming portability
  across nominally similar machines.
- **Chapter 04 (Context Engineering) — context window sizing**: Add the
  concrete 32K-minimum/64K-practical-default local-model context-window
  recommendation (Claim 8), noting that runtime defaults are "far too small"
  out of the box and that this budget competes directly with model-weight RAM
  (Claim 1).

## Extraction Notes

- Both parts of the series were fetched by raw `curl` (HTTP 200 for both) and
  hand-parsed (HTML tags stripped, entities decoded) rather than via a
  summarizing fetch tool, so all quotes in this note are verbatim from that
  parsed plain text, not paraphrased.
- Part 2 was fetched and read in full even though the issue and Prospector
  triage comments named only Part 1, because Part 1 explicitly promises it
  as an imminent follow-up ("Coming up... In my next memo...") and it was
  already published (2026-07-08) by the time of extraction (2026-07-09);
  MINER.md §1 directs following up to 5 substantive linked pages, and Part 2
  is the primary source of the task-level evidence (Claims 5, 6, 9-12) that
  Part 1's factor taxonomy only summarizes at a high level. `source_url` in
  the frontmatter points to Part 1 (matching the issue), with Part 2 cited
  throughout as `martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-experiences.html`.
  No other linked sub-pages (e.g., the ds4/pi-ds4-style external tool links)
  were present in either article beyond internal martinfowler.com navigation.
- The typo "wheras" (Claim 6 quote) and the double "how how" (Claim 8 quote)
  appear verbatim in the source and are preserved as-is.
- **No contradiction issue filed.** The one candidate tension considered —
  Böckeler's overall mixed/frustrating four-week verdict vs. Willison's
  single positive "handled with ease" anecdote for a similarly-sized local
  model (`blog-simonwillison-ornith.md`) — does not meet the MINER.md §4a bar
  for a filed contradiction: the two sources test different specific models,
  different specific tasks, and different evaluation depths (one session vs.
  four weeks across three phases), so this is a conditioning-variable
  difference (task/session scope), not two claims that materially oppose each
  other on the same question. It is recorded under Cross-References →
  Extends instead.
- Confidence rated anecdotal overall: every claim originates from a single
  practitioner's first-person testing (plus one second-hand colleague
  account, Claim 11) over roughly four weeks, with a small, non-representative
  model and task set (five model variants, two labs, mostly JS/TS/Python
  tasks). Several individual claims (e.g., Claim 7's harness schema naming)
  are independently checkable/settled as facts, but the source's overall
  evaluative conclusions are practitioner anecdote, not a controlled study.
