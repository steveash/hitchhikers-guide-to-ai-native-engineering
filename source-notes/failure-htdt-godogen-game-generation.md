---
source_url: https://github.com/htdt/godogen
source_type: failure-report
platform: hn
title: "Show HN: Claude Code skills that build complete Godot games (four rewrites, three engineering bottlenecks)"
author: Alex Ermolov (htdt)
date_published: 2026-03-16
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: anecdotal
issue: "#69"
---

# Failure Report: Four Rewrites to Make LLMs Generate Playable Godot 4 Games

> A year-long, four-rewrite engineering narrative: building an LLM pipeline to
> generate complete playable Godot 4 games from a text prompt required solving
> three concrete bottlenecks — GDScript training-data scarcity (solved by
> lazy-loading a custom API reference corpus), build-time vs. runtime state
> confusion (solved by careful phase-aware prompting and headless scene
> serialization), and agent self-bias in evaluation (solved by a separate
> vision-model QA loop) — while the generated-code target language was replaced
> from GDScript to C# mid-project to eliminate ~28 documented type-system
> failure modes. The source is a GitHub repo + Show HN narrative.

## Source Context

- **Platform**: GitHub repo (https://github.com/htdt/godogen, 2,806 stars,
  267 forks, MIT licensed, Python + C#/.NET 9) + Show HN discussion
  (https://news.ycombinator.com/item?id=47400868, 337 points, 206 comments,
  2026-03-16). The engineering narrative is distributed across the README, a
  dedicated `gdscript-vs-csharp.md` comparison document, `CONTRIBUTING.md`,
  and the HN discussion itself.
- **Author credibility**: Alex Ermolov (htdt) is the solo creator who spent
  approximately one year on this project across four major rewrites. The repo
  has active maintenance (27 commits through April 15, 2026), public MIT
  licensing, structured contribution guidelines requiring pre-approved issues,
  and a formal `gdscript-vs-csharp.md` design document — signals of
  engineering discipline, not a weekend experiment. The HN engagement (337
  pts / 206 comments) indicates strong practitioner interest and community
  validation. The author explicitly promised a follow-up blog post "with the
  full story (all the wrong turns)" not yet published as of extraction date.
- **Community response**: Largely enthusiastic with focused technical
  questioning. Key skeptical threads concerned: (1) whether LLM-generated
  games can achieve "passion," (2) output polish and gameplay depth, (3)
  physics implementation challenges. The author was transparent about
  limitations. No commenters disputed the technical claims about GDScript
  training-data scarcity or the context-window lazy-loading architecture.

## What Was Attempted

- **Goal**: Build a fully automated pipeline that takes a natural language
  text prompt and outputs a complete, playable Godot 4 game project — including
  architecture design, 2D/3D asset generation, GDScript/C# code generation,
  and visual testing.
- **Tool/approach**: Claude Code (godogen pipeline) + Google Gemini Flash
  (visual QA and 2D assets) + xAI Grok (textures, video generation for
  animated sprites) + Tripo3D (2D→3D model conversion) + BiRefNet
  (background removal). LLM orchestration via Claude inside a 1M-token
  context window.
- **Setup**: Solo developer, ~1 year, four major rewrites. Target runtime:
  Godot 4 (.NET build), Python 3.10+, .NET 9 SDK, xvfb (headless display),
  vulkan-tools, ffmpeg, ImageMagick. Cost per generated game: $5–8 all-in
  (LLM API ~$1–3, visual assets ~$3–5).

## What Went Wrong

### Failure Mode 1: GDScript Training-Data Scarcity

- **Symptoms**: LLMs "barely know GDScript." The language has approximately
  850 classes with Python-like syntax; models confidently hallucinate Python
  idioms that do not exist in GDScript or that produce silent type failures.
  The Variant return type from functions like `instantiate()`, math operations
  (`abs`, `clamp`, `lerp`), and array/dictionary access creates diffuse,
  hard-to-predict type-related failures throughout generated code.
- **Severity**: Total failure of naive generation. Code that looks syntactically
  plausible compiles but exhibits runtime type errors or hallucinated API calls.
- **Reproducibility**: Consistent — any model generating GDScript without
  augmentation will hit this. The ~850-class surface area of the Godot API
  is simply not adequately represented in standard LLM training corpora.

### Failure Mode 2: Build-Time vs. Runtime State Confusion

- **Symptoms**: Scenes are generated via headless scripts that build the node
  graph in memory and serialize to `.tscn` files. However, `@onready`
  variables and signal connections only exist at runtime, not at build time
  when the generation scripts run. Generated code that references these at
  build time compiles but produces silent failures at runtime. Additionally:
  "every node needs its owner set correctly or it silently vanishes on save"
  — a Godot-specific engine behavior that is not in the docs but must be
  correctly handled.
- **Severity**: Silent failure — code compiles, scenes serialize, but the
  resulting game project is broken in ways that only manifest at runtime.
- **Reproducibility**: Consistent. Any LLM generating Godot scene construction
  code without phase-aware prompting will encounter this.

### Failure Mode 3: Agent Self-Bias in Output Evaluation

- **Symptoms**: A coding agent evaluating its own generated game code is
  inherently biased toward declaring success. "Code compiles fine but assets
  are floating, paths lead nowhere, layouts are garbage" — the agent that
  wrote the code cannot reliably detect these visual failures through code
  review alone.
- **Severity**: Degraded quality to total failure depending on how bad the
  visual bugs are. Generated games that pass the agent's own review may
  exhibit z-fighting, floating objects, physics explosions, and grid-like
  placements that should be organic.
- **Reproducibility**: Consistent for visual/spatial quality. Text-only code
  review systematically misses spatial and visual correctness issues.

### Failure Mode 4: GDScript Type System — ~28 Documented Failure Modes

- **Symptoms** (from `gdscript-vs-csharp.md`): The GDScript type system
  creates diffuse, hard-to-contain failure modes:
  - Type inference with `:=` operator creates silent failures
  - `Variant` returns from `instantiate()`, math operations, array/dictionary
    access make type errors unpredictable
  - Approximately 28 documented GDScript type-related gotchas with no
    systematic containment
- **Severity**: Progressive quality degradation across the full range of
  generated code.
- **Reproducibility**: Consistent. The failure modes are structural to GDScript's
  type system, not edge cases.

### Failure Mode 5: Context Window Overflow from Full API Injection

- **Symptoms**: GDScript has ~850 classes. Injecting the full Godot API
  reference into the context window to address Failure Mode 1 blows up the
  context budget.
- **Severity**: Infeasible — full API injection is not a viable solution to
  the training-data scarcity problem.
- **Reproducibility**: Constant — a 1M-token window cannot hold the full
  Godot API corpus for all 850 classes in working form.

## Root Cause (if identified)

- **Author's diagnosis**: Three discrete engineering bottlenecks requiring
  distinct solutions:
  1. Training data scarcity for GDScript — requires external reference injection
  2. Build-time vs. runtime state complexity — requires phase-aware prompting
  3. Coding agent self-bias in evaluation — requires an external evaluator

  Additionally, GDScript's type system creates a combinatorial failure surface
  that is not solvable by prompting alone.

- **Our assessment**: The diagnosis is specific and credible. The GDScript
  training-data scarcity claim is directly verifiable: GDScript is a niche
  language with a Python-like but incompatible syntax, and the LLM training
  corpus does not have adequate GDScript coverage. The build-time vs. runtime
  distinction is a real Godot architectural property, not an LLM failure — the
  failure is the LLM not knowing about it. The self-bias evaluation problem is
  a general limitation of self-referential code review, well-documented in
  the multi-agent and verification literature. The C# migration as resolution
  to Failure Mode 4 is well-supported by the formal comparison document.

- **Category**: tool-limitation (LLM training data coverage) + expectation-mismatch
  (build-time vs. runtime state) + architectural-design (self-referential evaluation)

## Recovery Path

### Recovery 1: Custom API Reference Corpus with Lazy-Loading

The author built a three-part reference system:
1. A hand-written GDScript language specification documenting quirks
2. Full Godot API documentation converted from Godot's XML source
3. A "quirks database for engine behaviors you can't learn from docs alone"

Critically, the API reference is **lazy-loaded** — the agent retrieves only
the specific class APIs it needs at runtime, rather than injecting the full
corpus upfront. This sidesteps the context-window overflow (Failure Mode 5)
while addressing training-data scarcity (Failure Mode 1).

```
Architecture: "godot-api" runs as an isolated skill context
  → Agent queries it on demand for needed class APIs
  → Only relevant API documentation enters the main context window
  → Context budget preserved for generation and reasoning
```

*Source: godogen README + HN discussion, htdt, 2026-03-16*

### Recovery 2: Phase-Aware Scene Serialization

Scenes are constructed via headless Python scripts that build the Godot node
graph in memory and serialize to `.tscn` files directly. This avoids
hand-editing Godot's serialization format. The prompting teaches the model:
- Which APIs are available at which execution phase (build vs. runtime)
- That every node must have its owner set correctly or it silently vanishes on save
- That `@onready` and signal connections cannot be used in build-time scripts

The author notes: "it took careful prompting but paid off."

### Recovery 3: Separate Vision-Model QA Loop

A dedicated Gemini Flash vision model runs as a separate, isolated skill context.
It receives only screenshots from the running game (no code) and evaluates
them against generated reference images. Crucially, the evaluator has no
access to the generated code — this eliminates self-bias.

> "Godogen closes that loop: after writing code, it captures screenshots from
> the running engine and a vision model evaluates them. That's the difference
> between 'compiles but broken' and 'actually playable.'"

*Source: htdt, HN discussion, 2026-03-16*

Bug categories caught by the visual loop that code review misses:
- Z-fighting (geometry at identical depth)
- Floating objects
- Physics explosions (rigid bodies flying apart)
- Grid-like placements that should be organic

### Recovery 4: C# Migration (replaces GDScript)

In April 2026 the generated code target was migrated from GDScript to C#.
The formal comparison document (`gdscript-vs-csharp.md`) lists:

**GDScript eliminated ~28 type-related failure modes.** The key ones:
- `:=` type inference with silent failures
- `Variant` returns from `instantiate()`, math ops, array/dict access

**C# advantages for code generation:**
- Generics and proper type inference eliminate the Variant failure class
- "Trades diffuse type-system complexity for a small number of well-documented,
  well-contained sharp edges"
- More correct generated code on the first attempt

**C# well-documented sharp edges (retained):**
- `SetScript()` disposes the C# managed wrapper → requires "temp parent" pattern
  to re-obtain root nodes (12 lines of documented example code)
- Requires `.csproj` files, `dotnet build` compilation step, `partial` class
  declarations
- Signal delegate naming conventions must end in `EventHandler`

### Recovery 5: Single-Context Architecture with Isolated Skill Contexts

The system abandoned a multi-context agent approach and converged on:
- **One main orchestrator context** running the full pipeline in a 1M-token
  window with stage-specific instructions loaded progressively
- **Isolated skill contexts** for support functions (API lookup, visual QA,
  asset generation) — these run separately to preserve the main pipeline's
  focus and context budget

Document-based state persistence across any compaction or failure:
- `STRUCTURE.md` — Architecture documentation
- `PLAN.md` — Pipeline execution plan
- `ASSETS.md` — Asset list and specifications
- `MEMORY.md` — Persistent state

### Recovery 6: Risk-First Feature Decomposition

Rather than decomposing all game features equally:
1. System identifies genuinely risky features (procedural generation, custom
   physics, complex shaders)
2. Risky features are isolated for separate verification
3. Routine features are assembled in a single pass to minimize integration
   overhead

## Extracted Lessons

### Lesson 1: For niche or low-training-data languages, LLMs require injected external reference — not just better prompting

- **Evidence**: GDScript has ~850 classes and Python-like syntax that LLMs
  confidently hallucinate against. The author's solution was a custom three-part
  reference corpus (language spec, API docs converted from XML, quirks
  database). Prompting alone could not compensate for training data absence.
- **Confidence**: anecdotal (single project, one language) but the mechanism
  is generalizable
- **Actionable as**: When targeting code generation for any language or framework
  with thin training data representation, plan for a reference injection layer.
  The injection must be lazy-loaded to avoid context window overflow. Any niche
  framework, domain-specific language, or rapidly-evolving API is at risk of
  this failure mode.

### Lesson 2: Lazy-loading large API reference corpora is necessary for context-window-constrained code generation

- **Evidence**: 850 GDScript classes cannot all be injected upfront even in a
  1M-token window when combined with generation output. The author built a
  dedicated "godot-api" skill context queried on demand. Only needed APIs
  enter the main context window.
- **Confidence**: emerging (the architecture is documented and the reason is
  given; the alternative — full injection — is ruled out explicitly)
- **Actionable as**: Design large-API code generation pipelines with lazy
  retrieval of documentation, not upfront injection. RAG-style retrieval
  (or a dedicated skill context that answers API queries) is the pattern.
  This applies to any library with more API surface than fits in the working
  context budget alongside the actual code being generated.

### Lesson 3: LLMs need explicit phase-aware prompting for runtime-vs-build-time distinction in engine/framework targets

- **Evidence**: Godot's `@onready` variables and signal connections only exist
  at runtime, not during headless scene construction. The model does not know
  this distinction without being explicitly taught. Silent runtime failures
  result. The "owner must be set correctly or node silently vanishes on save"
  is a similar undocumented engine behavior that required the quirks database.
- **Confidence**: anecdotal (single engine, single pipeline)
- **Actionable as**: When generating code for runtime environments with
  lifecycle phases (game engines, reactive frameworks, server-side rendering,
  initialization sequences), catalog the phase-specific API availability
  constraints and include them in the reference corpus. Do not assume the
  model infers these from the language docs.

### Lesson 4: A coding agent cannot reliably evaluate the visual/spatial correctness of its own output — external evaluator is required

- **Evidence**: The author states "code compiles fine but assets are floating,
  paths lead nowhere, layouts are garbage" as the pre-QA state. A separate
  Gemini Flash vision model evaluating screenshots (not code) catches bugs
  that the code-generating agent systematically misses. The visual QA agent
  has no code access — only rendered screenshots from the running engine.
- **Confidence**: anecdotal (single pipeline) but aligns with general
  multi-agent verification literature
- **Actionable as**: For any pipeline where output correctness has a visual,
  spatial, or behavioral dimension that can be checked via screenshot or
  execution trace, add a separate evaluator that does NOT have access to the
  generated code. The evaluator must be grounded in the actual output, not
  the code that was supposed to produce it.

### Lesson 5: Type-system choice for code generation targets has a multiplicative effect on generated-code quality

- **Evidence**: The formal `gdscript-vs-csharp.md` document enumerates
  ~28 GDScript type-system failure modes that C# eliminates. The migration
  was a deliberate engineering decision, not a preference change. C# "trades
  diffuse type-system complexity for a small number of well-documented,
  well-contained sharp edges."
- **Confidence**: anecdotal (single project, documented formally)
- **Actionable as**: When selecting a code generation target language, explicitly
  evaluate type system properties from the LLM's perspective. A language with
  diffuse, implicit type failures (variants, dynamic typing, overloaded
  inference) will produce more hard-to-detect failures than one with explicit,
  containable type contracts. Favor static typing with clear error surfaces
  when the choice exists.

### Lesson 6: Document-based state persistence is a prerequisite for multi-stage LLM pipelines that need to survive context compaction

- **Evidence**: Godogen persists pipeline state as structured markdown
  documents (STRUCTURE.md, PLAN.md, ASSETS.md, MEMORY.md) that survive any
  context compaction or failure. The pipeline can be resumed from any failure
  point. The design explicitly parallels the "specs as compressed context"
  pattern documented elsewhere in our corpus.
- **Confidence**: emerging (convergent with multiple other sources)
- **Actionable as**: Multi-stage LLM pipelines should write state to durable
  files at every stage boundary, not rely on conversation context to carry
  forward. This is the pipeline equivalent of the individual-session pattern
  from blog-sankalp-claude-code-20 and failure-decker-4hr-session-loss.

### Lesson 7: Four major rewrites are required to converge a novel LLM pipeline — plan for iteration, not first-pass success

- **Evidence**: The author states explicitly: "I've been working on this for
  about a year through four major rewrites." The known abandoned approaches:
  GDScript as code target, multi-context agent architecture, earlier background
  removal implementation, initial animation pipeline. The full story of wrong
  turns has not yet been published as of extraction date.
- **Confidence**: anecdotal (single practitioner)
- **Actionable as**: Budget for multi-iteration cycles when building novel
  LLM pipelines. The "four rewrites" number is a useful calibration point:
  even a sophisticated practitioner building in a well-understood domain
  required four major architectural revisions to converge. Do not treat an
  initial working implementation as a production architecture.

### Lesson 8: Multi-model composition (not single-model) is the production pattern for AI-native pipelines requiring diverse modalities

- **Evidence**: Godogen uses Claude for code generation, Gemini for 2D assets
  and visual QA, Grok for textures and video-based animated sprites, Tripo3D
  for 2D→3D model conversion, BiRefNet for background removal. No single
  model handles all modalities. The system was designed multi-provider from
  the start.
- **Confidence**: anecdotal (single pipeline architecture)
- **Actionable as**: Do not assume the best general-purpose LLM is best at
  all pipeline tasks. Design pipelines with model selection per task type.
  This trades orchestration complexity for quality per task and avoids
  single-vendor dependency.

## Concrete Artifacts

### The three-bottleneck framing (direct quote, HN)

```
"Getting LLMs to reliably generate functional games required solving three
specific engineering bottlenecks:

1. The Training Data Scarcity: LLMs barely know GDScript. It has ~850 classes
   and a Python-like syntax that will happily hallucinate Python idioms that
   fail to compile.

2. Build-Time vs Runtime State: Scenes are generated via headless scripts that
   build the node graph in memory and serialize it to .tscn files. Every node
   needs its owner set correctly or it silently vanishes on save. @onready and
   signal connections don't exist at build time. It took careful prompting but
   paid off.

3. The Evaluation Loop: A coding agent is inherently biased toward validating
   its own output. Godogen closes that loop: after writing code, it captures
   screenshots from the running engine and a vision model evaluates them.
   That's the difference between 'compiles but broken' and 'actually playable.'"
```

*Source: htdt, HN discussion item 47400868, 2026-03-16*

### C# type-safety migration summary (from gdscript-vs-csharp.md)

```
GDScript failure modes eliminated by C# migration:
  - := type inference with silent failures
  - Variant return from instantiate(), abs/clamp/lerp, array[], dict[]
  - ~28 type-related gotchas documented in gdscript-vs-csharp.md
  
C# sharp edges retained (well-documented):
  - SetScript() disposes C# managed wrapper
    → requires "temp parent" pattern to re-obtain root nodes (~12 lines)
  - Requires .csproj, dotnet build, partial class declarations
  - Signal delegates must end in EventHandler convention

Design principle (author): "Trades diffuse type-system complexity for a
small number of well-documented, well-contained sharp edges"
```

*Source: gdscript-vs-csharp.md, htdt, 2026-04*

### Pipeline skill contexts and isolation structure

```
godogen pipeline (Claude, 1M-token main context):
  - Stage-specific instructions loaded progressively
  - Document persistence: STRUCTURE.md, PLAN.md, ASSETS.md, MEMORY.md

Isolated skill contexts (separate from main pipeline):
  - godot-api: Godot class API lookup (lazy-loaded on demand)
  - visual-qa:  Gemini Flash visual QA (screenshot evaluation, no code access)

Asset providers:
  - Google Gemini: character references, visual designs, 2D assets
  - xAI Grok:     textures, simple objects, video-based animated sprites
  - Tripo3D:      2D image-to-3D model conversion
  - BiRefNet:     background removal (multi-signal matting)
```

*Source: godogen README, AGENTS.md, 2026-04*

### Economics (from HN discussion)

```
Per-game generation cost (all-in):
  - LLM API (Claude code generation): ~$1–3
  - Visual assets (Gemini + Tripo3D):  ~$3–5
  - Total:                             $5–8 per game
```

*Source: htdt, HN discussion item 47400868, 2026-03-16*

### Demo prompts (from demo_prompts.md)

```
CartoRally:             Top-down racing, terrain with visible contour lines
Amsterdam Cyclist:      2D side-scrolling bike, four lanes, parallax scrolling
3D Alpine Snowboard:    Downhill simulator, carved turns, speed-dependent snow spray
Ultra Realistic Nature: Riverbank, procedural shaders, animated grass, modeled tree
```

*Source: demo_prompts.md, htdt, 2026*

### Contribution philosophy (from CONTRIBUTING.md)

```
"The agent is a highly capable LLM — handholding only pollutes the context.
We do not give obvious guidance."

Contribution focus: improvements to autonomous game generation only.
Closed without review: unnecessary features, config options lacking good
defaults, large refactors without demonstrated problems.
```

*Source: CONTRIBUTING.md, htdt, 2026*

## Cross-References

- **Corroborates**: `research-wasnotwas-context-compaction.md` — Godogen's
  document-based persistence (STRUCTURE.md, PLAN.md, ASSETS.md, MEMORY.md)
  is the pipeline-scale implementation of the "durable state that survives
  compaction" pattern. The wasnotwas research documented compaction destroying
  in-context state; Godogen's architecture assumes compaction will occur and
  writes state externally at every stage boundary.

- **Corroborates**: `failure-decker-4hr-session-loss.md` — The "write
  architectural rationale to a file immediately" lesson from the decker failure
  is operationalized at pipeline scale in Godogen's PLAN.md and STRUCTURE.md.
  Both sources point to the same root cause: in-context state is ephemeral,
  durable files are the only reliable persistence medium.

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's
  multi-agent orchestration model predicts exactly the Godogen architecture:
  separate specialized agents for coding, asset generation, and evaluation,
  with an orchestrator managing state. Godogen is a practitioner validation
  of Osmani's theoretical model in a demanding real-world domain.

- **Corroborates**: `discussion-hn-ttal-multiagent-factory.md` — TTal's
  external state pattern (avoiding in-context state for multi-agent workflows)
  converges with Godogen's markdown persistence approach. Both reached the
  same architectural conclusion independently.

- **Corroborates**: `blog-french-owen-coding-agents-feb-2026` — French-Owen's
  multi-model orchestration principle is directly validated. Godogen uses five
  distinct model providers (Claude, Gemini, Grok, Tripo3D, BiRefNet) because
  no single model excels at all modalities. This is the strongest practitioner
  evidence in our corpus for the multi-model composition pattern.

- **Extends**: `failure-claudemd-ignored-compaction.md` — The Godogen
  architecture is an implicit workaround for CLAUDE.md unreliability: by
  encoding the pipeline state in markdown files (not CLAUDE.md instructions),
  the system avoids depending on the model to remember what stage it's in.
  The "compaction destroys guidelines" failure mode is sidestepped by making
  guidelines unnecessary — the state documents carry the context instead.

- **Novel**: This is the first source note in our corpus covering:
  - **Low-training-data language code generation** as a first-class engineering
    problem requiring dedicated reference injection infrastructure
  - **Lazy-loading API corpora** as a context-window management technique for
    large-API code generation
  - **Cross-modal visual QA** (screenshot-based evaluation separate from code
    review) as a verification technique for generated game/visual output
  - **Type system selection** as a code-generation quality lever (not just
    a developer-experience choice)
  - **Four-rewrite iteration cycle** as calibration data for novel LLM pipeline
    development
  - **Per-game economics** ($5–8 all-in) as a concrete cost benchmark for
    complex multi-modal generation pipelines

## Guide Impact

- **Chapter 04 (Context Engineering)**: This source provides the strongest
  practitioner evidence for the lazy-loading API reference pattern. Add a
  section: "Injecting reference corpora for low-coverage languages and
  frameworks." The Godogen architecture (custom language spec + API docs
  converted from source XML + quirks database, all lazy-loaded via isolated
  skill context) is the reference implementation. Every AI-native project
  targeting a niche or rapidly-evolving framework faces a version of this
  problem.

- **Chapter 04 (Document-based state persistence)**: Godogen's STRUCTURE.md /
  PLAN.md / ASSETS.md / MEMORY.md pattern should be added alongside the
  decker backup script and the Sankalp handoff pattern as the third canonical
  approach to surviving context compaction: externalize all pipeline state at
  every stage boundary, assume in-context state will be lost.

- **Chapter 02 (Harness Engineering)**: The skill context isolation pattern
  (godot-api and visual-qa as isolated contexts, not inline function calls)
  is worth adding as an architectural recommendation. Support functions that
  consume large context budgets (API reference lookup, visual evaluation)
  should run in isolated skill contexts to preserve the main pipeline's focus
  and token budget.

- **Chapter 03 (Safety and Verification)**: The visual QA loop is the first
  source in our corpus documenting cross-modal verification: using a
  vision model to evaluate screenshots from running code. Add as a
  verification pattern for any pipeline whose output has a visual or
  behavioral dimension. Key design rule: the evaluator must not have access
  to the code that produced the output — only to the actual output.

- **Chapter 03 (Safety and Verification / Self-bias warning)**: Add a
  "coding agent self-bias" caveat to any section recommending agent
  self-review. The Godogen case study is the clearest formulation: "A coding
  agent is inherently biased toward validating its own output." Self-review
  can catch syntactic and logical errors; it cannot reliably detect visual,
  spatial, or behavioral failures in the execution output.

- **Chapter 01 or Ch02 (Setting expectations for novel LLM pipelines)**:
  The four-rewrite timeline (one year, four major architectural revisions)
  is a useful calibration data point for teams estimating new AI-native
  project scope. Add alongside the cost data ($5–8/game) as a concrete
  economics and iteration anchor.

## Extraction Notes

- The repo was read in depth: README, gdscript-vs-csharp.md, CONTRIBUTING.md,
  AGENTS.md, demo_prompts.md, setup.md, and project structure. The HN
  discussion (item 47400868, 337 points, 206 comments) was also analyzed.
- The author promised a follow-up blog post with "the full story (all the
  wrong turns)" that had not yet been published as of 2026-04-15. A future
  mining task should check for this post when it appears — it may document
  additional failure modes from the first three rewrites not yet captured.
- The GDScript→C# migration occurred in April 2026, concurrent with the
  extraction date. The `gdscript-vs-csharp.md` document is the primary
  artifact for the type-system analysis. The ~28 failure modes enumerated
  there are the author's own documentation, not a third-party audit.
- The animation pipeline was noted as incomplete at extraction time — sprite
  sheet and animation generation remained problematic, and the author was
  planning migration to video models (Grok video generation was already
  integrated for animated sprites). This is an active open problem, not a
  resolved one.
- The repo statistics (2,806 stars, 267 forks) represent the state at
  extraction time (April 15, 2026) and will grow. The high engagement confirms
  practitioner interest in the problem space beyond the HN discussion.
- No existing source note in our corpus covers Godot, GDScript, game
  generation, or low-training-data code generation. This note is the initial
  coverage of an entirely new problem space.
- The "obvious guidance pollutes the context" contribution philosophy quote
  from CONTRIBUTING.md is a pithy encapsulation of the broader principle that
  context budget should be spent on high-signal information. Worth citing in
  guide sections on CLAUDE.md/AGENTS.md content strategy.
