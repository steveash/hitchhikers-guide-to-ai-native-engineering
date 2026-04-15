---
source_url: https://pieterma.es/syntopic-reading-claude/
source_type: blog-post
title: "Syntopic Reading with Claude Code"
author: Pieter Maes (pmaze)
date_published: 2026-01-10
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: anecdotal
issue: "#78"
---

# Syntopic Reading with Claude Code

> A practitioner writeup on using Claude Code with custom CLI tools to mine
> 100 non-fiction books for thematic connections — notable for its concrete
> staged-pipeline failure mode ("insights baked into the prompts"), the mental
> model shift from prompt engineering to tool design, and the recursive
> agent-proposes-then-implements-its-own-tools loop.

## Source Context

- **Type**: blog-post (practitioner writeup; ~1,500 words with live demo at
  trails.pieterma.es)
- **Author credibility**: Pieter Maes (pmaze) is an independent developer who
  built and shipped the project described. Claims are first-person and
  verifiable through the live demo. Not a researcher, not a vendor. The HN
  submission drew 524 points and 146 comments (Jan 2026), suggesting broad
  practitioner recognition. Strength is specificity and working system;
  weakness is N=1 (single project, single author, no controlled comparison).
- **Scope**: Single-project report on using Claude Code for a non-coding,
  exploratory/creative task (cross-book thematic analysis). Covers: staged
  pipeline failure mode, the agentic replacement, tool design philosophy,
  the agent self-improvement loop, CLI output format design, cost data, and
  novelty as an optimization signal. Does NOT cover team adoption, CLAUDE.md
  design, hooks, or session management. The system uses Claude Code as
  an orchestrator of custom CLI tools, not for code generation.

## Extracted Claims

### Claim 1: Staged LLM pipelines return the insights already baked into their prompts

- **Evidence**: Author's direct experience building a multi-stage LLM pipeline
  with hand-assembled contexts for cross-book analysis. Observed that the
  pipeline outputs reflected prompt structure rather than genuine discovery.
- **Confidence**: anecdotal
- **Quote**: "I was mainly getting back the insight that I was baking into the
  prompts, and the results weren't particularly surprising."
- **Our assessment**: This is a well-named failure mode. The mechanism is
  clear: a pipeline with fixed stages and explicit context assembly constrains
  the output to the shape of the prompt. A stage designed to "find connections
  between X and Y" finds connections between X and Y; no surprises. This is
  the pipeline equivalent of the sycophancy problem — you get back your own
  assumptions reflected. Distinct from the sycophancy literature (which is
  about a model agreeing with the user in dialogue) but analogous in structure.
  Not yet named in our corpus; worth naming as "prompt amplification" or
  "pipeline echo."

### Claim 2: A minimal agentic prompt outperformed a hand-tuned staged pipeline

- **Evidence**: Author switched from the multi-stage pipeline to giving Claude
  access to CLI debugging tools with a minimal prompt ("find something
  interesting") and observed a qualitative improvement.
- **Confidence**: anecdotal
- **Quote**: "On a whim, I gave CC access to my debug CLI tools and found that
  it immediately did a better job at pulling in what it needed than the
  pipeline I was trying to tune by hand, while requiring much less
  orchestration."
- **Our assessment**: Credible and important for the corpus. The key variable
  is not just "agentic vs. pipeline" but the combination of two things: (1)
  the agent can decide which tool to call and in what sequence, and (2) the
  prompt is deliberately underconstrained ("find something interesting"
  vs. "find connections between X and Y"). The underconstrained prompt is what
  enables genuine discovery. The practical lesson is counterintuitive: when
  the goal is open-ended exploration, less prompt engineering, not more, may
  produce better results. This claim needs further corroboration from other
  practitioners — single data point for now.

### Claim 3: Tool design is a higher-leverage abstraction than prompt engineering for agentic tasks

- **Evidence**: Author's stated mental model shift after the pipeline failure.
  The switch to agentic approach prompted a reframing of where effort should
  go.
- **Confidence**: anecdotal
- **Quote**: "I started spending my time implementing better tools for Claude
  to use, moving up a rung on the abstraction ladder."
- **Our assessment**: This is the central claim of the post and the highest
  value for the guide. The "rung on the abstraction ladder" framing is clean
  and quotable. It aligns with Osmani's orchestra post (harness engineering as
  the skill that matters) but is more pointed: don't tune the prompt, change
  what the agent can do. The mechanism is that better tools expand the agent's
  action space while better prompts only direct it within a fixed action space.
  Corroborates existing Ch02 harness engineering evidence and extends it with
  a concrete case study of what "better tools" looks like in practice.

### Claim 4: Treating the agent as a coworker needing affordances, rather than a function to tune, produces better tool design

- **Evidence**: Author's explicit reframing of the design problem.
- **Confidence**: anecdotal
- **Quote**: "I spent my time thinking about the affordances that would make the
  workflow better, as if I were designing them for myself."
- **Our assessment**: This is the empathic mental model for tool design. It is
  a complement to the "prompt tuning" mental model, not a replacement. The
  practical operation is: put yourself in the agent's position and ask "what
  would I need to do this task well?" This tends to produce tools that provide
  context (not just answers), that expose structure (not just strings), and
  that support exploration (not just retrieval). Matches the Osmani
  "coworker" framing in the orchestra post. The author notes that the agent's
  reasoning "naturally aligned with human problem-solving approaches," which
  is the mechanism: if the tool is designed for how a human would work, and
  the agent reasons like a human, the tool works for the agent.

### Claim 5: Agents can identify their own capability gaps and propose new tools when asked for feedback

- **Evidence**: Author explicitly asked Claude to "provide feedback at the end
  and list the functionality it wished it had" and received actionable
  proposals.
- **Confidence**: anecdotal
- **Quote**: "Claude was excellent at proposing new commands and capabilities
  that would make the work more efficient."
- **Our assessment**: This is a reproducible, low-cost technique. Asking the
  agent "what tools do you wish you had?" at the end of a session is a
  structured way to surface gaps in the scaffolding. The author used this as
  an ongoing feedback loop rather than a one-time design exercise. This is
  novel in our corpus — no other source explicitly describes soliciting tool
  proposals from the agent. The quality of these proposals presumably depends
  on the agent having enough task experience to know what it's missing; this
  technique works better after several sessions, not on day one.

### Claim 6: Agents can implement the tools they propose, creating a recursive self-improvement loop

- **Evidence**: Author describes a three-step cycle: Claude proposes a new CLI
  capability → Claude implements the capability → Claude uses the new
  capability for the main task.
- **Confidence**: anecdotal
- **Quote**: "Claude suggested improvements, which Claude implemented, so
  Claude could do the work better."
- **Our assessment**: This is the highest-interest claim in the post for the
  guide. A coding agent that improves its own scaffolding is a qualitatively
  different thing from a coding agent that writes application code. The
  author's case is non-coding work (book analysis), which means Claude Code
  is doing both "scaffolding engineering" and "task execution" simultaneously.
  The loop is self-limiting (Claude can only propose tools it can imagine
  needing, not tools it hasn't thought of yet), but within that limit it
  appears to work. The Osmani self-improving agents post (linked source in
  blog-addyosmani-code-agent-orchestra) covers a similar concept at the
  workflow level (agent proposes PRD improvements); this post shows it at the
  tool/CLI level. The combination of both is the fuller picture.

### Claim 7: Semi-XML CLI output with nested related content helps the agent orient itself and discover adjacent exploration paths

- **Evidence**: Author describes the specific output format design decision and
  its rationale.
- **Confidence**: anecdotal
- **Quote**: N/A (described structurally rather than quoted)
- **Our assessment**: This is a concrete, extractable artifact for Ch04
  context engineering. The format is not just for readability — it is
  deliberately designed to surface related topics as side-effects of the
  primary query result, enabling the agent to discover what to explore next
  without a separate navigation step. This is "context for free" — packing
  the response with adjacent information reduces the number of tool calls
  needed to achieve situational awareness. Contrast with MCP server patterns
  that return minimal structured JSON: the pieterma approach trades token
  efficiency for exploration density.

### Claim 8: Novelty relative to existing content can substitute for an ill-defined "interestingness" quality metric

- **Evidence**: Author implemented two novelty mechanisms when "interestingness"
  proved too vague to optimize.
- **Confidence**: anecdotal
- **Quote**: N/A (described as design choice, not experimentally validated)
- **Our assessment**: The proxy-metric substitution is a genuinely useful
  design pattern for agentic tasks where the target quality is subjective or
  hard to measure. Novelty (embedding distance to existing output) is
  measurable; "interestingness" is not. This maps onto the broader principle
  that agentic systems need explicit optimization signals — if you can't define
  what you want, the agent can't optimize for it. The limitation is that
  novelty ≠ quality; a completely novel but incoherent connection scores
  highly by novelty but fails the human evaluation. The author combined
  algorithmic novelty with a prompt-level instruction ("avoid conceptual
  overlap"), which provides a rough quality floor.

### Claim 9: Cheap AI-assisted revision changes project economics — you commit to fewer suboptimal choices because undoing them is inexpensive

- **Evidence**: Author's observation about project decision-making under
  agentic assistance.
- **Confidence**: anecdotal
- **Quote**: "Revision is cheap, so I don't need to plow ahead with suboptimal
  choices just because it'd be too costly to undo them."
- **Our assessment**: This is the economics of reversibility under AI
  assistance. The traditional software engineering heuristic "make it hard to
  change irreversible decisions" is being relaxed: if revision is cheap
  enough, more decisions become reversible. The concrete case is design
  choices (excerpt length, trail structure) that would previously have locked
  in early because reworking them was expensive. With the agent, the author
  could hold those decisions open longer. This is a first-order economic
  argument for agentic systems, not just a quality argument.

### Claim 10: £10 / 60M input tokens is a viable cost profile for indexing 100 non-fiction books

- **Evidence**: Author's stated cost from running Gemini 2.5 Flash Lite for
  topic extraction (3-5 topics per chunk) across the full corpus.
- **Confidence**: anecdotal (no methodology details; single run)
- **Quote**: "Processing 100 books used ~60M input tokens, approximately £10
  total."
- **Our assessment**: A useful calibration data point, but limited in
  isolation. The model (Gemini Flash Lite), the task (topic extraction, not
  generation), and the chunk size (~500 words) are all specific to this
  project. The main guide implication is not the exact number but the order
  of magnitude: bulk preprocessing of a 100-book library costs less than a
  dinner. This makes large-scale knowledge base construction economically
  feasible for individual practitioners, not just organizations.

### Claim 11: A background server process for expensive model loading makes CLI tools viable for per-call agent tool use

- **Evidence**: Author's implementation choice: first CLI call transparently
  launches a server process holding expensive state (model weights); subsequent
  calls reuse the server via Python's `multiprocessing.connection`.
- **Confidence**: anecdotal
- **Quote**: N/A (described as implementation detail)
- **Our assessment**: This is a concrete, reusable pattern for building
  context-efficient CLI tools for agent consumption. Without this, each tool
  call would pay a cold-start penalty for model loading, making the tools
  impractically slow. The pattern is not unique to this project — similar
  server-per-session patterns exist in language server protocol (LSP)
  tooling — but applying it specifically to LLM-backed CLI tools for agent
  consumption is a novel framing. Relevant for Ch02 (harness engineering)
  and for anyone building custom CLI tools for Claude Code.

## Concrete Artifacts

### Semi-XML CLI Output Format

Attributed to the author's design; from the blog post:

```xml
<topics query="deception" count="1">
  <topic id="47193" books="7" score="0.0173" label="Deception">
    <chunk id="186" book="1">
      <topic id="47192" label="Business deal"/>
    </chunk>
  </topic>
</topics>
```

Design rationale: the nested structure shows (1) the primary result, (2) the
chunk context, and (3) related sibling topics in one response — enabling
the agent to discover adjacent exploration paths as a side-effect of a
primary query, without a separate navigation call.

### Four CLI Tool Capabilities Provided to the Agent

```
1. Find chunks associated with topics matching a query
2. Find adjacent topics within chunk windows (neighbourhood discovery)
3. Identify topics co-occurring across multiple books (cross-book analysis)
4. Browse sibling topics and chunks in the topic tree (hierarchical navigation)
```

### Three-Stage Agent Workflow

```
Stage 1 — Ideation:
  Scans library and existing trails
  Browses topic tree for unexplored areas
  Proposes novel trail concepts

Stage 2 — Research:
  Takes a specific trail idea
  Browses many chunks via CLI tools
  Extracts relevant excerpts
  Orders them to support the intended insight

Stage 3 — Polish:
  Adds highlights
  Adds connections between consecutive excerpts
```

### Technology Stack

```
Parsing:      selectolax (EPUB), wtpsplit/sat-6l-sm (sentence segmentation)
Storage:      SQLite + sqlite-vec (embeddings)
Topic graph:  igraph + Leiden partitioning (recursive, Surprise quality fn)
Models:       Gemini 2.5 Flash Lite (topic extraction)
              Claude Opus (prompt refinement)
              google/embeddinggemma-300m (embeddings)
              BAAI/bge-reranker-v2-m3 (reranking)
LLM calls:    DSPy (structured extraction, model experimentation)
CLI server:   Python multiprocessing.connection (lazy server launch)
```

### Cost Benchmark

```
Task:     Topic extraction for 100 non-fiction books
Model:    Gemini 2.5 Flash Lite
Tokens:   ~60M input tokens
Cost:     ~£10 total
Output:   ~100,000 extracted topics → ~1,000 top-level categories
```

### Agent Self-Improvement Loop (Concise)

```
1. Run agent on main task
2. At session end: ask "what functionality do you wish you had?"
3. Agent proposes new CLI commands/capabilities
4. Agent implements the proposed commands
5. Next session: agent uses new commands on main task
6. Repeat
```

## Cross-References

- **Corroborates**:
  - **blog-addyosmani-code-agent-orchestra**: The Osmani orchestra post's
    central thesis that harness engineering (designing the agent's environment)
    is the primary skill is corroborated here with a concrete non-coding case
    study. Osmani's "the bottleneck is no longer generation, it's verification"
    maps onto pieterma's "I moved from tuning prompts to implementing tools" —
    both shift effort from the language model's output to the environment it
    operates in. The self-improving agent concept in Osmani's linked source 3
    (Self-Improving Coding Agents) is at the workflow level; pieterma's is at
    the tool/CLI level.
  - **practitioner-dadlerj-tin**: tin's architecture (Claude Code with custom
    CLI commands as the primary interface) is structurally similar to the
    pieterma system. Both demonstrate that the agent's power comes from the
    tools it has access to, not from the model alone. tin's hook pattern
    (auto-commit on session end) is a different form of the same insight:
    invest in the scaffolding.
  - **practitioner-getsentry-sentry**: Sentry's skill-based decomposition
    (focused CLI commands per task type) is the production-scale analog of
    pieterma's four CLI tools. Both demonstrate the "explicit tool for each
    subtask" pattern rather than a generic search tool.

- **Contradicts**: None identified. The "tool design > prompt engineering"
  claim does not contradict existing notes — it extends and sharpens them.
  The staged pipeline failure mode is novel to the corpus (no existing note
  argues FOR staged pipelines for exploratory tasks).

- **Extends**:
  - **blog-addyosmani-code-agent-orchestra** (Claim 3 / harness engineering):
    pieterma provides a concrete non-coding case study of "invest in better
    tools, not better prompts." The orchestra post states the principle;
    this post shows the mechanism.
  - **blog-osmani-good-spec**: Both posts are fundamentally about designing
    the agent's working environment — the good-spec post from the
    specification angle, this post from the tool-affordance angle. Together
    they cover both static context (what the agent is told) and dynamic
    context (what the agent can do).

- **Novel**:
  - **The staged pipeline echo failure mode**: No existing source names or
    describes the specific failure where a multi-stage LLM pipeline returns
    the assumptions baked into its prompts rather than discovering new
    patterns. This is a concrete, nameable failure mode new to the corpus.
  - **Agent-proposes-then-implements-its-own-tools loop**: No existing source
    note describes this specific three-step recursive pattern (ask agent for
    tool proposals → agent implements proposals → agent uses them). The
    self-improving agents concept exists in Osmani, but at a different level
    of abstraction.
  - **Minimal prompt for exploratory tasks**: The claim that underconstrained
    prompts ("find something interesting") produce better results than
    carefully specified ones for open-ended exploration tasks is not covered
    by other source notes. Most of the guide's prompt advice runs in the
    opposite direction (more specificity = better results). This is a
    conditional claim (works for exploration; probably not for code generation)
    that deserves explicit treatment.
  - **Background server process pattern for CLI tools**: The
    multiprocessing.connection pattern for avoiding cold-start costs on
    LLM-backed CLI tools is not covered elsewhere.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the "tool design > prompt
  engineering" mental model shift as a named principle. The pieterma case
  study (staged pipeline → agentic with CLI tools) is the most concrete
  illustration in the corpus. Add the agent self-improvement loop (ask for
  tool proposals, implement them) as a technique for iterative harness
  refinement — this is a lightweight alternative to designing all tools
  upfront. Add the four CLI tool types (search, neighborhood, co-occurrence,
  tree navigation) as an example of what a non-coding agent's tool palette
  looks like.

- **Chapter 02 (Harness Engineering — tool output design)**: Add the
  semi-XML format as a positive example of designing CLI output for agent
  consumption: pack related context into every response to reduce follow-up
  tool calls. Contrast with minimal JSON formats that optimize for machine
  parsing but reduce the agent's situational awareness per call.

- **Chapter 02 (Harness Engineering — custom CLI patterns)**: Add the
  background server process (lazy launch via multiprocessing.connection) as
  the recommended implementation pattern for CLI tools that depend on
  expensive model loading or state initialization.

- **Chapter 04 (Context Engineering)**: The staged pipeline echo failure mode
  is a concrete illustration of "you get what you put in" — a context
  engineering failure, not a model failure. Add as a cautionary example for
  the "what NOT to put in context" section: pre-specifying the structure of
  the answer constrains the output to that structure.

- **Chapter 04 (Context Engineering)**: The novelty-as-proxy-metric pattern
  is relevant to the "signal vs. noise in context" discussion. Using
  embedding distance to existing outputs as an optimization signal is a
  concrete technique for any agent tasked with generating diverse, non-redundant
  content.

- **Chapter 00 (Principles)**: The "pipeline echo" failure (prompts amplify
  rather than discover) is worth a principle-level warning: "underconstrain
  your prompts for exploration tasks." This is a conditioned principle (NOT
  for code generation), so it must be positioned carefully — but it is a
  real and underrepresented caveat in the current harness-engineering-heavy
  corpus.

## Extraction Notes

- The issue was auto-filed from HN with the URL trails.pieterma.es (the live
  demo). The actual blog post is at pieterma.es/syntopic-reading-claude/.
  The Prospector's triage comment identified the correct URL. This note
  extracts from the blog post; the live demo was also inspected and showed
  40+ generated trails but no additional technical content beyond what the
  post describes.
- Author is a solo developer. All claims are N=1 (single project, single
  author). Confidence is consistently anecdotal; do not cite metrics (£10,
  60M tokens) as benchmarks without that caveat.
- The HN discussion (524 points, 146 comments) was not extracted. If the
  guide needs practitioner reaction to the claims, the HN thread is the
  source; it was not followed here as it would require a separate extraction.
- DSPy is used for structured LLM calls and model experimentation; the post
  does not elaborate on how DSPy was used beyond that characterization. If
  the guide ever covers DSPy specifically, a dedicated source note would be
  needed.
- The system is designed for a non-coding exploratory task. Claims about
  "minimal prompts working better than specific ones" should NOT be
  generalized to code generation tasks without additional evidence.
