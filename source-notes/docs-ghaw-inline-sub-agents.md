---
source_url: https://github.github.com/gh-aw/reference/inline-sub-agents
source_type: docs
title: "GitHub Agentic Workflows: Inline Sub-Agents Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#522"
---

# GitHub Agentic Workflows: Inline Sub-Agents Reference

> First-party reference documentation for a single-file agent composition
> pattern that lets practitioners embed named worker-agent definitions directly
> inside a workflow markdown file using `## agent: \`name\`` headings — filling
> the gap between full cross-workflow dispatch (covered in
> `docs-ghaw-orchestration-patterns.md`) and standalone agent files in
> `.github/agents/`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/inline-sub-agents`
  page — in the `reference/` section alongside other gh-aw syntax and runtime
  behavior references. Reference pages document syntax and runtime contracts;
  they are distinct from the practitioner `guides/` section and conceptual
  `introduction/` pages.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that operates Peli de Halleux's agent factory. Claims about
  syntax, naming constraints, and runtime behavior are authoritative for the
  `gh aw` platform. The feature is production-documented and not marked as
  preview.
- **Scope**: Covers one specific composition mechanism: defining sub-agent
  blocks directly in workflow markdown files. Documents the `## agent: \`name\``
  syntax, name constraints, allowed frontmatter fields, the engine inheritance
  constraint, the `actions/setup` runtime extraction behavior, and multiple
  sub-agents in a single file. Does NOT cover: standalone agent files in
  `.github/agents/`, `dispatch-workflow` or `call-workflow` cross-file
  orchestration (see `docs-ghaw-orchestration-patterns.md`), or how
  sub-agents handle permissions (they inherit the parent workflow's permission
  set, but the page does not elaborate on this).

## Extracted Claims

### Claim 1: Inline sub-agents use a `## agent: \`name\`` level-2 heading to declare a named agent block directly within a workflow markdown file

- **Evidence**: The syntax is the primary content of the reference page; a
  complete workflow example demonstrates a parent workflow delegating to a
  named sub-agent defined in the same file.
- **Confidence**: settled (first-party reference documentation; the syntax is
  the stated normative form)
- **Quote**: (no direct quote; see the Concrete Artifacts section for the
  annotated example from the page)
- **Our assessment**: The level-2 heading delimiter is a natural choice: it
  is both human-readable in the `.md` source and parseable by the `actions/setup`
  runtime without a separate compilation step. The inline form means the entire
  workflow — orchestration logic and worker definitions — lives in a single
  version-controlled file. For Ch02 (Harness Engineering): this is the third
  composition pattern in the gh-aw ecosystem alongside separate `.github/agents/`
  files and cross-workflow dispatch. It closes the "same file, simpler case"
  gap in the composition spectrum.

### Claim 2: Sub-agent names must begin with a lowercase letter (a–z) and may contain only a–z, 0–9, underscores, and hyphens

- **Evidence**: The reference page specifies the naming constraints explicitly,
  with valid examples (`file-summarizer`, `code_reviewer`, `pr-analyst`) and
  a character-class rule.
- **Confidence**: settled (first-party reference documentation; constraint is
  formally stated, not inferred)
- **Quote**: (no direct quote; constraints were presented in a structured list
  with examples on the page)
- **Our assessment**: The naming rule is the same character class used for
  GitHub Actions job IDs and other CI/CD identifiers — a predictable
  convention for practitioners already familiar with the Actions ecosystem.
  The lowercase-start requirement prevents class-name-style names and implies
  the runtime treats agent names as identifiers, not display labels. For Ch02:
  document this alongside other gh-aw naming conventions when introducing the
  inline sub-agent feature.

### Claim 3: Each inline sub-agent block consists of optional YAML frontmatter wrapped in `---` delimiters, followed by natural language instructions

- **Evidence**: The page describes the block structure explicitly and the
  example workflow demonstrates it: frontmatter followed by an instruction
  body.
- **Confidence**: settled (first-party documentation)
- **Quote**: (no direct quote; the two-part structure was described in prose
  and demonstrated via example)
- **Our assessment**: The block structure is identical to the parent workflow's
  own two-component design (YAML frontmatter + natural language instructions
  per `docs-ghaw-how-they-work.md` Claim 1). This is a fractal application
  of the same pattern: the parent workflow is a two-component file; each
  inline sub-agent is a two-component block within that file. The design
  consistency is a practitioner-friendly choice — anyone who can write a
  workflow can write a sub-agent.

### Claim 4: Inline sub-agents support exactly two optional frontmatter fields — `model` and `description` — with `model` defaulting to the parent workflow's model if omitted

- **Evidence**: The reference page's frontmatter field table lists two fields:
  `model` (optional, "AI model to use (e.g. `claude-haiku-4.5`). Defaults to
  the parent workflow's model.") and `description` (optional, brief purpose
  statement). Both are marked as not required.
- **Confidence**: settled (first-party reference table; the two-field constraint
  is explicit)
- **Quote**: "AI model to use (e.g. `claude-haiku-4.5`). Defaults to the parent
  workflow's model."
- **Our assessment**: The two-field limit is significant by what it excludes:
  no `permissions`, no `tools`, no `on` trigger, and — critically — no `engine`
  field (Claim 5). Sub-agents are intentionally minimal: they receive a model
  and a description, and nothing else configurable at the sub-agent level. The
  model default-to-parent behavior means the simplest inline sub-agent has zero
  frontmatter — just the heading and instructions. For Ch02 and Ch04: the
  model override on a per-sub-agent basis is the primary configuration lever
  practitioners have. All other constraints (engine, permissions, tools) come
  from the parent workflow.

### Claim 5: Inline sub-agents cannot specify an `engine` field; they always run within the parent workflow's engine

- **Evidence**: The page explicitly states this as a noted constraint.
- **Confidence**: settled (first-party documentation; stated as a hard rule)
- **Quote**: "Sub-agents do **not** accept an `engine` field. They run within
  the parent workflow's engine."
- **Our assessment**: This constraint has two implications. First, engine
  selection is a workflow-level concern, not a task-level concern — the
  practitioner chooses Copilot vs. Claude vs. Codex at the parent level, and
  all sub-agents inherit that choice. Second, you cannot use inline sub-agents
  to mix engines within one workflow run. If different sub-tasks need different
  engines (e.g., one task requires Copilot, another requires Claude), the
  correct pattern is separate workflow files with `call-workflow` or
  `dispatch-workflow` dispatch, not inline sub-agents. For Ch04: document this
  as the key limitation that distinguishes inline sub-agents from cross-workflow
  dispatch. The engine constraint makes inline sub-agents the right pattern for
  same-engine, same-permission task delegation; dispatch patterns are the right
  choice when engine or permission variation is needed across workers.

### Claim 6: At runtime, `actions/setup` extracts inline sub-agent blocks and writes them to `.agents/agents/<name>.agent.md`; the Copilot CLI discovers and invokes agents from this path by name

- **Evidence**: Runtime behavior described in the reference page: the
  `actions/setup` action performs the extraction; the Copilot CLI uses
  automatic discovery from the `.agents/agents/` directory. Parent workflow
  instructions reference the sub-agent by name; the CLI resolves it from
  the extracted file.
- **Confidence**: settled (first-party reference documentation; the extraction
  path is explicitly stated)
- **Quote**: (no direct quote; runtime behavior was described in a dedicated
  section of the page)
- **Our assessment**: This is a runtime extraction mechanism, distinct from the
  `gh aw compile` step that produces `.lock.yml` files. The inline sub-agents
  remain embedded in the workflow source (`.md` and `.lock.yml`) and are
  materialized into the agent discovery directory only at execution time by
  `actions/setup`. For Ch02: note that this means inline sub-agent changes
  take effect at the next workflow run without a separate compile step for
  the sub-agent definitions themselves. For practitioners debugging agent
  behavior: the extracted `.agents/agents/<name>.agent.md` file is the
  live definition being executed, and is where debugging should start.

### Claim 7: A single workflow file can contain multiple inline sub-agent blocks, each with its own name, model, and instruction set

- **Evidence**: The reference page's multiple sub-agents example shows two
  sub-agent blocks in one file (`summarizer` using `claude-haiku-4.5`,
  `reviewer` using `claude-sonnet-4.5`), each with distinct frontmatter and
  instructions.
- **Confidence**: settled (first-party documentation; example demonstrates the
  feature)
- **Quote**: (no direct quote; the multi-sub-agent capability was shown through
  a code example)
- **Our assessment**: Multiple sub-agents in one file enables deliberate model
  tier selection per task. The pattern from the example — haiku for a
  summarization task, sonnet for a code review task — is a cost-optimization
  strategy: route low-complexity work to less expensive models and reserve
  higher-tier models for tasks that require more reasoning. This is the same
  principle as Cursor's inter-request model switching (blog-cursor-fast-regex-search)
  applied within a single gh-aw workflow file. For Ch02 (Harness Engineering)
  and Ch04 (Multi-Agent Orchestration): name per-sub-agent model selection as
  the primary cost-control lever for inline sub-agent workflows.

### Claim 8: Parent workflow instructions reference inline sub-agents by name, and the Copilot CLI's automatic discovery mechanism handles the invocation without explicit tool call syntax

- **Evidence**: The single-file example shows the parent instructions referencing
  a sub-agent by name ("Use the `file-summarizer` sub-agent to summarize
  `README.md`...") with no explicit tool call API; the Copilot CLI resolves the
  named agent via the extracted `.agents/agents/` directory.
- **Confidence**: settled (first-party documentation; the invocation pattern is
  demonstrated in the example)
- **Quote**: (no direct quote; the invocation pattern is implicit in the example
  workflow)
- **Our assessment**: The name-based invocation means the parent workflow's
  instruction section reads like a natural language delegation: "use the
  file-summarizer sub-agent to do X." This is consistent with the gh-aw
  design philosophy that workflow instruction bodies are natural language task
  specifications (cf. `docs-ghaw-agentic-authoring.md` Claim 8: "what, not how"
  principle for instruction sections). Practitioners do not need to understand
  the underlying `actions/setup` extraction or `.agents/agents/` discovery
  mechanism to author workflows — the abstraction leaks only when debugging.

## Concrete Artifacts

### Single Inline Sub-Agent Example

The reference page provides a complete workflow demonstrating inline sub-agent
definition and invocation:

```markdown
---
on:
  workflow_dispatch:
engine: copilot
---
# File Summary Task

Use the `file-summarizer` sub-agent to summarize `README.md` and add a comment
to the current pull request with the result.

## agent: `file-summarizer`
---
model: claude-haiku-4.5
description: Summarizes the content of a file in a few concise sentences
---
You are a file summarization assistant. When given a file path, read the file
and return a brief summary (2–4 sentences) describing its purpose and key
contents. Be concise and factual.
```

*Source: `reference/inline-sub-agents` — single sub-agent example*

Note: WebFetch converts HTML to markdown; exact whitespace and line breaks in
the original may differ slightly from the above representation.

### Multiple Inline Sub-Agents Example

The reference page demonstrates multiple sub-agents in a single file with
different model configurations:

```markdown
## agent: `summarizer`
---
model: claude-haiku-4.5
description: Summarizes files concisely
---
Summarize the given file in 2–4 sentences.

## agent: `reviewer`
---
model: claude-sonnet-4.5
description: Reviews code for quality issues
---
Review the given code for bugs, style issues, and potential improvements.
```

*Source: `reference/inline-sub-agents` — multiple sub-agents example*

### Inline Sub-Agent Frontmatter Fields Reference

| Field | Required | Description |
|-------|----------|-------------|
| `model` | No | AI model to use (e.g. `claude-haiku-4.5`). Defaults to the parent workflow's model. |
| `description` | No | Short description of the sub-agent's purpose |
| `engine` | **Not accepted** | Sub-agents do NOT accept an engine field — they run within the parent workflow's engine |

*Source: `reference/inline-sub-agents` — Frontmatter Fields section*

### Naming Constraints

```
Sub-agent name requirements:
  - Must begin with a lowercase letter (a–z)
  - May contain: a–z, 0–9, underscore (_), hyphen (-)
  - Valid examples: file-summarizer, code_reviewer, pr-analyst
```

*Source: `reference/inline-sub-agents` — Name Constraints section*

### Runtime Extraction Path

```
Build / author time:  inline sub-agent defined in workflow .md source
  ↓  (gh aw compile)
Committed artifact:   .lock.yml (workflow executable)
  ↓  (workflow run triggered)
Execution time:       actions/setup extracts ## agent: blocks
  ↓  (writes to filesystem)
Agent discovery dir:  .agents/agents/<name>.agent.md
  ↓  (Copilot CLI auto-discovery)
Invocation:           parent instructions reference sub-agent by name
```

*Source: `reference/inline-sub-agents` — Runtime Behavior section (structure
reconstructed from prose description; not a literal code block from the page)*

### Composition Pattern Spectrum in gh-aw

```
Single-file inline sub-agents (this source):
  - All definitions in one .md file
  - Sub-agents inherit parent's engine and permissions
  - Runtime extraction via actions/setup
  - Per-sub-agent model selection (via model frontmatter field)
  - No API call overhead; no cross-workflow dispatch

call-workflow (docs-ghaw-orchestration-patterns.md):
  - Workers in separate workflow files
  - Compile-time fan-out; typed MCP tool per worker
  - Preserves github.actor and billing attribution
  - Workers finish before orchestrator concludes
  - Zero API call overhead at runtime

dispatch-workflow (docs-ghaw-orchestration-patterns.md):
  - Workers in separate workflow files
  - Runtime API call to workflow_dispatch
  - Workers run async; can outlive parent
  - Max 10 concurrent workers
```

*Source: synthesized from this note and docs-ghaw-orchestration-patterns.md;
not a literal artifact from the inline-sub-agents page*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 1 (the two-component workflow structure:
    YAML frontmatter + natural language markdown): Inline sub-agent blocks follow
    the identical two-component pattern — each block has optional YAML frontmatter
    (model, description) followed by natural language instructions. The fractal
    application of this pattern from workflow-level down to sub-agent block level
    is consistent with the design philosophy documented in Claim 1.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support: engine field in
    frontmatter selects Copilot/Claude/Codex/Gemini): Claim 5 here confirms the
    engine field is parent-workflow-only. The two sources together establish that
    engine selection is a workflow-level concern, and `engine` is the only
    frontmatter field that sub-agents cannot override.
  - `docs-ghaw-agentic-authoring.md` Claim 8 ("what, not how" for instruction
    sections): The sub-agent instruction body follows the same principle — natural
    language goals and constraints, not implementation steps. The Planner described
    in that note's Claim 8 could be used to draft inline sub-agent instruction
    bodies using the same "what, not how" methodology.

- **Extends**:
  - `docs-ghaw-orchestration-patterns.md` (Claims 1–7, the orchestrator/worker
    fan-out model with `dispatch-workflow` and `call-workflow`): That note covers
    two cross-workflow fan-out patterns. This source adds a third pattern —
    inline sub-agents — that operates within a single workflow file. Together,
    the three patterns form a complete composition spectrum for gh-aw practitioners:
    inline (same file) → `call-workflow` (compile-time cross-file) →
    `dispatch-workflow` (async cross-file). No existing note documented the
    same-file end of this spectrum.
  - `docs-ghaw-how-they-work.md` Claim 7 (the `.md` → `.lock.yml` compilation
    model): The inline sub-agent extraction is a runtime complement to the
    compile-time model. The compile step produces `.lock.yml`; the `actions/setup`
    step at runtime extracts inline sub-agents to `.agents/agents/`. This source
    adds the runtime artifact side of the workflow execution picture that Claim 7
    does not cover.
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts allow inline tool definitions
    in workflow frontmatter): MCP Scripts provide inline tool definitions in
    frontmatter; inline sub-agents provide inline agent definitions in the workflow
    body. Together, these two "inline" patterns constitute a co-location philosophy
    in gh-aw: a single `.md` file can bundle the orchestration logic, its tool
    definitions (via MCP Scripts), and its worker agents (via inline sub-agents),
    without any external files.

- **Contradicts**: None. The inline sub-agent pattern is additive to the
  existing gh-aw composition model documented in other notes. It does not
  oppose any existing claim about engine selection, permissions, or
  compilation behavior. No contradiction issue required.

- **Novel**:
  - **`## agent: \`name\`` syntax for inline agent definition**: No existing
    source note in the corpus documents this specific syntax or the inline
    sub-agent composition pattern. This is the first documentation of the
    single-file agent bundling mechanism.
  - **Per-sub-agent model selection within one file**: The ability to assign
    different model tiers (e.g., haiku for summarization, sonnet for review)
    within a single workflow file is not described in any existing note. This
    is a cost-optimization pattern with no equivalent in the cross-workflow
    dispatch patterns.
  - **Engine inheritance constraint**: The explicit prohibition on `engine`
    fields at the sub-agent level — sub-agents always run within the parent's
    engine — is not documented anywhere else in the corpus. It is the clearest
    statement of which configuration options belong at the workflow level vs.
    the task level in gh-aw.
  - **Runtime extraction via `actions/setup`**: The mechanism by which inline
    sub-agent definitions become `.agents/agents/<name>.agent.md` files at
    execution time is a second artifact-generation path not covered by the
    compile-time model documentation (`.md` → `.lock.yml`).
  - **Third composition tier**: Inline sub-agents fill the "same-file, simpler
    case" position in the composition spectrum below `call-workflow` and
    `dispatch-workflow`. No existing note established this tier existed.

## Guide Impact

### Chapter 04: Multi-Agent Orchestration Patterns

- **Add inline sub-agents as the lightweight end of the gh-aw composition
  spectrum** (Claims 1, 6, 8): The three-tier composition decision for
  gh-aw practitioners:
  - **Inline sub-agents**: same engine, same permissions, same file, simple
    delegation — minimal overhead, definitions travel with the workflow
  - **`call-workflow`**: cross-file, compile-time fan-out, synchronous, typed
    MCP tools per worker, attribution preserved
  - **`dispatch-workflow`**: cross-file, async, runtime API call, workers
    outlive parent, max 10

  Cite this source for the inline end; cite `docs-ghaw-orchestration-patterns.md`
  for the cross-workflow end. The three tiers together are a complete decision
  framework for practitioners structuring multi-agent work in gh-aw.

- **Document the engine inheritance constraint as the key inline-vs-dispatch
  decision point** (Claim 5): If any worker task needs a different engine or
  different permissions, inline sub-agents are not the right pattern. Use
  `call-workflow` (engine same, permissions potentially different) or
  `dispatch-workflow` (engine can vary per worker file). Inline sub-agents
  are appropriate when all sub-tasks run well under the parent's engine.

### Chapter 02: Harness Engineering

- **Add per-sub-agent model selection as the cost optimization lever for
  inline sub-agents** (Claim 7): Teams using inline sub-agents can assign
  lightweight models to deterministic sub-tasks (summarization, classification,
  simple extraction → haiku) and reserve capable models for complex reasoning
  tasks (code review, analysis, synthesis → sonnet or opus). This is the
  inline-sub-agent equivalent of the model routing pattern; it operates at
  the workflow-file level rather than the API-call level.

- **Extend the co-location philosophy for single-file agents** (Claim 1,
  extending `docs-ghaw-how-they-work.md` Claims 1 and 6): A single gh-aw
  `.md` workflow file can bundle:
  - Orchestration logic (parent workflow body)
  - Custom tool definitions (via MCP Scripts in frontmatter)
  - Worker agent definitions (via inline sub-agents in the body)

  This single-file co-location pattern is a portable, self-contained unit.
  Combined with the URL-addressable prompt pattern
  (`docs-ghaw-agentic-authoring.md` Claim 6), teams can distribute complete
  multi-agent workflows as single fetchable files.

- **Document `.agents/agents/<name>.agent.md` as the debugging path** (Claim 6):
  When diagnosing unexpected inline sub-agent behavior, the extracted file at
  `.agents/agents/<name>.agent.md` is the live definition being executed.
  This is the first place to check when the sub-agent's behavior does not
  match the workflow source — since extraction happens at runtime, a stale
  checkout or a failed extraction can produce divergence between the `.md`
  source and the executed definition.

## Extraction Notes

1. **Source is concise**: The reference page is short — primarily syntax
   definitions, one or two code examples, a frontmatter field table, and
   notes on constraints and runtime behavior. The content is information-dense
   despite the brevity. All claims were fully extracted in 8 entries.

2. **WebFetch HTML→markdown conversion**: The page was fetched via WebFetch,
   which converts HTML to markdown via an AI model. Code blocks may not preserve
   exact whitespace or line breaks from the original. Code examples in the
   Concrete Artifacts section are labeled as potentially differing in formatting;
   the syntax and content are accurate per multiple consistent fetches of the page.

3. **Related reference links not followed**: The page references related
   documentation (Copilot Agent Files documentation, Markdown workflow body
   reference, Workflow structure organization, YAML frontmatter configuration).
   These links were not followed because the inline-sub-agents reference page
   is self-contained for this feature, and the related pages cover topics already
   documented in existing corpus notes (workflow body syntax:
   `docs-ghaw-how-they-work.md`; frontmatter: same). Following them would
   risk duplicate extraction, not novel content.

4. **No publication date**: Like other gh-aw documentation pages, this page
   does not carry an explicit publication date. `date_published` is left null.

5. **No contradictions to file**: Reviewed all existing source notes with
   relevant overlap (docs-ghaw-orchestration-patterns.md,
   docs-ghaw-how-they-work.md, docs-ghaw-agentic-authoring.md,
   blog-anthropic-claude-managed-agents.md, blog-simonwillison-muse-spark.md).
   No claim here materially opposes any existing source note. The engine
   inheritance constraint and the runtime extraction behavior are new to the
   corpus but do not contradict anything previously documented.
