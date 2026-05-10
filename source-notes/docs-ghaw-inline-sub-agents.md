---
source_url: https://github.github.com/gh-aw/reference/inline-sub-agents
source_type: docs
title: "GitHub Agentic Workflows: Inline Sub-Agents"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-04
last_checked: 2026-05-04
status: current
confidence_overall: emerging
issue: "#522"
---

# GitHub Agentic Workflows: Inline Sub-Agents

> First-party reference documentation for a specific gh-aw composition pattern:
> defining named agent blocks directly inside a workflow markdown file using
> `## agent: \`name\`` heading delimiters as an alternative to separate
> `.github/agents/` files — covering the syntax, the runtime extraction
> mechanism, the engine restriction, model inheritance, and natural-language
> invocation pattern.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows reference page — in the
  `reference/` section, positioned between "Imports (Copilot Agent Files)" and
  "Imports (Dependabot)" in the site navigation, indicating it documents a
  specific composition technique rather than a conceptual overview)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that operates the gh-aw platform. YAML syntax and runtime
  behavior claims are authoritative for the `gh aw` platform. The extraction
  mechanism (`actions/setup` → `.agents/agents/`) is a platform implementation
  detail specific to gh-aw and does not generalize to other agentic platforms.
- **Scope**: Covers the inline sub-agent definition syntax, frontmatter fields,
  name constraints, runtime extraction behavior, engine restriction,
  multiple-sub-agents-per-file support, and natural-language invocation. Does
  NOT cover: when to choose inline vs. separate agent files (no explicit
  guidance given), cost or performance trade-offs between inline and separate
  agents, how sub-agents interact with the parent's tool allowlist or
  permissions, or whether compiled `.lock.yml` files include the inline
  sub-agent blocks.

## Extracted Claims

### Claim 1: An inline sub-agent is a named agent definition embedded directly in a workflow markdown file rather than in a separate `.github/agents/` file — the `## agent: \`name\`` heading marks the start of each block

- **Evidence**: First-party documentation defining the feature: "An inline
  sub-agent is a named agent definition embedded directly in a workflow markdown
  file. Instead of creating a separate file in `.github/agents/`, you define
  the agent's frontmatter and instructions in a dedicated section of the same
  workflow file."
- **Confidence**: settled (first-party platform documentation; this is the
  canonical definition of the feature)
- **Quote**: "An inline sub-agent is a named agent definition embedded directly
  in a workflow markdown file. Instead of creating a separate file in
  `.github/agents/`, you define the agent's frontmatter and instructions in a
  dedicated section of the same workflow file."
- **Our assessment**: The key architectural implication is colocation — the agent
  and the workflow that uses it live in the same file. This trades the
  reusability of a separate file for the readability of seeing the agent
  definition alongside the workflow that invokes it. The page is positioned
  adjacent to "Imports (Copilot Agent Files)" in the gh-aw reference navigation,
  confirming that inline sub-agents and separately-authored agent files are
  parallel composition options. For Ch02 (Harness Engineering): inline
  sub-agents are a second composition path alongside the separate agent file
  approach documented in `docs-ghaw-agentic-authoring.md`.

### Claim 2: Sub-agent blocks are extracted by `actions/setup` at runtime and materialized as `.agents/agents/<name>.agent.md` files that the Copilot CLI discovers automatically

- **Evidence**: First-party documentation stating the runtime mechanism:
  "`actions/setup` extracts each inline sub-agent block and writes it to:
  `.agents/agents/<name>.agent.md`" and "The Copilot CLI finds
  `.agents/agents/file-summarizer.agent.md` and invokes it automatically."
- **Confidence**: settled (first-party documentation; specific mechanism and
  directory path are named)
- **Quote**: "`actions/setup` extracts each inline sub-agent block and writes
  it to: `.agents/agents/<name>.agent.md`"
- **Our assessment**: Extraction happens at runtime (not compile time), meaning
  inline sub-agents are defined in the `.md` source but their file-based
  representation is created at execution time. At the point the Copilot CLI
  processes them, they are indistinguishable from separately-authored agent
  files. The destination directory is `.agents/agents/` (runtime-generated),
  not `.github/agents/` (statically-authored). This distinction matters for
  practitioners debugging sub-agent invocation failures — they should look in
  `.agents/agents/` for the materialized form, not in source-controlled
  directories. For Ch02: this extraction mechanism is an important
  implementation detail that separates the authoring artifact (the inline block)
  from the execution artifact (the extracted `.agent.md` file).

### Claim 3: Sub-agents do not accept an `engine` field and always run within the parent workflow's engine — engine selection is a parent-level decision only

- **Evidence**: Documented as an explicit callout note: "Sub-agents do **not**
  accept an `engine` field. They run within the parent workflow's engine."
- **Confidence**: settled (first-party documentation; stated as a constraint in
  a callout box, indicating an important practitioner warning)
- **Quote**: "Sub-agents do **not** accept an `engine` field. They run within
  the parent workflow's engine."
- **Our assessment**: This constraint has a significant architectural implication:
  if a task requires a specific engine (e.g., Claude vs. Copilot), that decision
  cannot be made at the sub-agent level. Engine is a single, parent-workflow-level
  choice shared by all inline sub-agents in that file. This is different from the
  `model` field (Claim 4), which CAN be set per sub-agent. The practical trade-off:
  practitioners can mix models within a single workflow (parent on Sonnet,
  sub-agent on Haiku) but not engines. If different tasks require different
  engines, the appropriate composition mechanism is separate workflows connected
  via `call-workflow` or `dispatch-workflow` (per `docs-ghaw-orchestration-patterns.md`
  Claims 2–4), not inline sub-agents. For Ch02 and Ch04: name this as the
  scope boundary between inline sub-agents (same engine, potentially different
  model) and cross-workflow orchestration (potentially different engine).

### Claim 4: Inline sub-agents support two optional frontmatter fields — `model` (defaulting to parent's model) and `description` — and no other frontmatter fields

- **Evidence**: Frontmatter fields table from the documentation, which lists
  exactly two fields:
  - `model` (not required): "AI model to use (e.g. `claude-haiku-4.5`).
    Defaults to parent workflow's model."
  - `description` (not required): "Short description of the sub-agent's
    purpose."
  No other fields are listed in the table.
- **Confidence**: settled (first-party documentation; the table explicitly lists
  all supported fields as an exhaustive reference)
- **Quote**: "AI model to use (e.g. `claude-haiku-4.5`). Defaults to parent
  workflow's model."
- **Our assessment**: The per-sub-agent `model` field is the primary economic
  optimization lever for inline sub-agents. A parent workflow running on an
  expensive model (e.g., Claude Opus) can delegate bounded, focused tasks (e.g.,
  file summarization) to a cheaper model (e.g., Claude Haiku). This is a
  concrete application of the model-selection-for-cost principle at the
  intra-workflow level. The `description` field serves documentation purposes
  — it helps practitioners (and the parent workflow's AI) understand what the
  sub-agent does, similar to a function docstring. For Ch02: the `model` field
  is the primary knob for cost management with inline sub-agents; recommend
  explicitly setting it when the sub-agent's task is simpler than the parent's.

### Claim 5: A single workflow file may contain multiple inline sub-agent blocks, each delimited by its own `## agent: \`name\`` heading through the next `##` heading or EOF

- **Evidence**: First-party documentation: "A single workflow file may contain
  more than one sub-agent block. Each block starts with its own
  `## agent: \`name\`` heading and ends at the next `##` heading or EOF."
- **Confidence**: settled (first-party documentation)
- **Quote**: "A single workflow file may contain more than one sub-agent block.
  Each block starts with its own `## agent: \`name\`` heading and ends at the
  next `##` heading or EOF."
- **Our assessment**: Multiple sub-agents per file enable a single workflow to
  define its entire specialist agent team inline. A workflow that decomposes a
  task into three roles (e.g., a triage agent, a summarizer, and a labeler)
  can define all three in the same file. The heading-based delimiter means any
  `##`-level heading terminates the previous sub-agent block — workflow authors
  must be careful about heading structure to avoid accidentally closing a
  sub-agent block mid-definition. For Ch02 and Ch04: multiple inline sub-agents
  per file is the gh-aw pattern for single-file multi-role workflows.

### Claim 6: Parent workflows invoke sub-agents by name in natural language prompt text — the invocation is part of the workflow's instructions, not a structured code call

- **Evidence**: The documentation provides an example invocation in the parent
  workflow's instruction section: "Use the `file-summarizer` sub-agent to
  summarize the file `.github/workflows/smoke-copilot.md`. Verify the sub-agent
  returns a brief summary (2–4 sentences)." The Copilot CLI discovers the
  materialized agent file and dispatches to it based on this instruction.
- **Confidence**: settled (first-party example showing the invocation pattern)
- **Quote**: (no direct standalone quote; the invocation example appears as: "Use
  the `file-summarizer` sub-agent to summarize the file
  `.github/workflows/smoke-copilot.md`. Verify the sub-agent returns a brief
  summary (2–4 sentences).")
- **Our assessment**: Natural-language invocation aligns with the broader gh-aw
  philosophy of "markdown instructs, YAML constrains" (from
  `docs-ghaw-how-they-work.md` Claim 1) — the invocation lives in the
  instruction layer, not the configuration layer. The parent workflow tells the
  agent "use sub-agent X to do Y," and the Copilot CLI handles the dispatch to
  the materialized `.agent.md` file. This contrasts with `call-workflow`
  (per `docs-ghaw-orchestration-patterns.md` Claim 3), where the compiler
  generates a typed MCP tool for each worker — a structured tool call rather
  than a natural-language instruction. For Ch04: inline sub-agent invocation
  (natural language) vs. `call-workflow` invocation (typed MCP tool) is a
  design-level distinction between the two intra-run delegation mechanisms.

### Claim 7: Sub-agent name constraints are strict: must start with a lowercase letter (a–z) and contain only a–z, 0–9, underscores, and hyphens — with examples following a role-indicating naming convention

- **Evidence**: First-party documentation: "Must start with a lowercase letter
  (`a–z`), May contain only `a–z`, `0–9`, `_`, and `-`" with three examples:
  `file-summarizer`, `code_reviewer`, `pr-analyst`.
- **Confidence**: settled (first-party syntax specification)
- **Quote**: "Must start with a lowercase letter (`a–z`), May contain only
  `a–z`, `0–9`, `_`, and `-`"
- **Our assessment**: The naming constraints ensure the derived `.agent.md`
  filename is valid on the filesystem and unambiguous. The three provided
  examples (`file-summarizer`, `code_reviewer`, `pr-analyst`) establish an
  implicit naming convention: descriptive role-indicators using a verb-noun or
  role pattern. This aligns with the "what, not how" principle in
  `docs-ghaw-agentic-authoring.md` Claim 8 — the sub-agent name should describe
  its role (what it does), not its implementation (how it does it). For Ch02:
  document name constraints as a syntax requirement; recommend role-indicating
  names as a convention.

## Concrete Artifacts

### Inline Sub-Agent Syntax — Complete Example

```markdown
## agent: `file-summarizer`
---
model: claude-haiku-4.5
description: Summarizes the content of a file in a few concise sentences
---
You are a file summarization assistant. When given a file path, read the file
and return a brief summary (2–4 sentences) describing its purpose and key
contents. Be concise and factual.
```

*Source: Inline Sub-Agents reference page — code example section*

### Frontmatter Fields Table

| Field | Required | Description |
|-------|----------|-------------|
| `model` | No | AI model to use (e.g. `claude-haiku-4.5`). Defaults to parent workflow's model. |
| `description` | No | Short description of the sub-agent's purpose. |

*Source: Inline Sub-Agents reference page — frontmatter fields table*

### Runtime Extraction Path

```
Workflow source (.md):
  Contains ## agent: `name` blocks inline

  ↓ actions/setup (at runtime — not compile time)

.agents/agents/<name>.agent.md
  → Copilot CLI discovers and invokes automatically

Parent workflow instructions (natural language):
  "Use the `file-summarizer` sub-agent to summarize the file ..."
  → Copilot CLI dispatches to .agents/agents/file-summarizer.agent.md
```

*Source: Inline Sub-Agents reference page — "Runtime Behavior" section*

### Parent Workflow Invocation Pattern

```markdown
<!-- In the parent workflow's instruction section: -->
Use the `file-summarizer` sub-agent to summarize the file
`.github/workflows/smoke-copilot.md`. Verify the sub-agent returns
a brief summary (2–4 sentences).
```

*Source: Inline Sub-Agents reference page — invocation example*

### Name Constraint Examples

```
Valid names:
  file-summarizer   ✓ (lowercase, hyphens allowed)
  code_reviewer     ✓ (lowercase, underscores allowed)
  pr-analyst        ✓ (lowercase, hyphens allowed)

Pattern: Must start with a–z; may contain a–z, 0–9, _, -
```

*Source: Inline Sub-Agents reference page — name constraints section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 1 (workflow structure: YAML frontmatter
    + markdown instructions): Inline sub-agents follow the same two-component
    structure as parent workflows — optional YAML frontmatter between `---`
    delimiters followed by natural language instructions. The pattern is applied
    recursively within the workflow file.
  - `blog-simonwillison-muse-spark.md` Claim 3 (`subagents.spawn_agent` as a
    first-class tool in meta.ai's commercial product validates sub-agent
    delegation as a standard primitive): Inline sub-agents are another
    first-party platform's validation that defining and invoking named specialist
    agents is becoming a standard composition primitive across AI platforms.

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` (agent authoring lifecycle): That note
    documents the general gh-aw authoring workflow and references `.github/agents/`
    files as the standard agent location. This source adds the inline alternative —
    defining agents within the workflow file itself. Together they give two
    composition paths: separate-file (reusable across workflows) vs. inline
    (colocated with the workflow that uses them). The choice is not made explicit
    in either source; that gap is a guide-writing opportunity.
  - `docs-ghaw-orchestration-patterns.md` Claims 2–4 (`dispatch-workflow` vs.
    `call-workflow` decision framework): Those claims document inter-workflow
    delegation (orchestrator calling separate worker workflows). This source adds
    an intra-file delegation scope (parent workflow invoking inline sub-agents).
    Together they give a spectrum of gh-aw composition scopes: inline sub-agents
    (one file, one run) → `call-workflow` (multiple files, one run) →
    `dispatch-workflow` (multiple files, multiple runs). The spectrum is not
    articulated in any single existing note.
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation
    model): The compilation model converts `.md` source to an executable
    `.lock.yml` at compile time. This source adds a runtime-phase step:
    `actions/setup` extracts inline sub-agent blocks to `.agents/agents/` at
    execution time. This is a third derived artifact from `.md` source — after
    the compiled `.lock.yml` and per-worker MCP tools (per
    `docs-ghaw-orchestration-patterns.md` Claim 3) — adding a runtime-materialized
    agent file as an additional execution artifact.

- **Contradicts**: None. The inline sub-agent pattern is consistent with the
  workflow structure, compilation model, and engine-selection architecture
  documented in existing corpus notes. The engine restriction (no `engine` field
  per sub-agent) is new information that adds specificity to the engine-as-
  parent-frontmatter-decision described in `docs-ghaw-how-they-work.md` Claim 9,
  without contradicting it. No contradiction issue required.

- **Novel**:
  - **Inline sub-agent syntax** (Claims 1, 7): The `## agent: \`name\`` heading
    delimiter as a composition mechanism for defining named agents within a single
    workflow file is not documented in any existing corpus note. This is the first
    coverage of this specific syntax.
  - **`actions/setup` extraction mechanism** (Claim 2): The runtime extraction
    path (inline block in `.md` → `actions/setup` → `.agents/agents/<name>.agent.md`
    → Copilot CLI invocation) is new to the corpus. No existing note documents
    how inline sub-agents are materialized for execution.
  - **Engine-level constraint at sub-agent scope** (Claim 3): The explicit `engine`
    field restriction — sub-agents always run in the parent's engine, not a
    separately configured engine — is a new architectural boundary not described
    in existing notes.
  - **Intra-file composition scope** (Claims 1, 5, 6): The spectrum of gh-aw
    composition scopes (inline → `call-workflow` → `dispatch-workflow`) is not
    explicitly articulated in any existing note. This source fills the narrowest
    scope: agents defined and used within a single workflow file.
  - **Per-sub-agent model selection** (Claim 4): While general model selection
    at the workflow level is documented in `docs-ghaw-how-they-work.md` Claim 9,
    the sub-agent-level `model` field for intra-workflow model mixing (parent on
    Sonnet, sub-agent on Haiku) is new to the corpus and has specific cost
    implications.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add inline sub-agents as a composition pattern alongside separate agent files**
  (Claims 1, 2): When a workflow needs to delegate bounded subtasks to specialist
  agents, inline sub-agents provide a single-file composition path. Present
  alongside the `.github/agents/` separate-file approach as a second option.
  The guide should supply the decision criterion (not in the source): use inline
  when the agent is specific to one workflow and colocation aids readability;
  use separate files when the agent must be reused across multiple workflows.

- **Document the `actions/setup` extraction mechanism** (Claim 2): Practitioners
  debugging sub-agent invocation failures need to know that the `.agents/agents/`
  directory (created at runtime) is where materialized sub-agents live. This is
  distinct from `.github/agents/` (statically-authored agent files) and from
  the compiled `.lock.yml` (the parent workflow's executable). Confusing these
  paths is a likely source of debugging friction.

- **Per-sub-agent model selection as a cost lever** (Claim 4): When the parent
  workflow runs on an expensive model, using the `model` field in inline
  sub-agent frontmatter to assign cheaper models to bounded subtasks is a
  concrete cost optimization. Add to any cost management discussion in Ch02.

- **Name the engine restriction as a composition scope boundary** (Claim 3):
  Document that engine selection is always parent-level — if tasks in the same
  workflow require different engines, inline sub-agents cannot address this. The
  alternative is separate workflows connected via `call-workflow` or
  `dispatch-workflow`. This gives practitioners a decision rule for when to
  escalate from inline sub-agents to cross-workflow orchestration.

### Chapter 04: Multi-Agent Orchestration Patterns

- **Add intra-file delegation to the composition spectrum** (Claims 1, 5, 6):
  The guide should articulate the three-tier composition spectrum in gh-aw:
  inline sub-agents (one file, one run, natural-language invocation) →
  `call-workflow` (multiple files, one run, compiler-generated MCP tool
  invocation) → `dispatch-workflow` (multiple files, multiple async runs, API
  call invocation). Cite `docs-ghaw-orchestration-patterns.md` Claims 2–4 for
  the outer two tiers; cite this note for the innermost scope. No single
  existing source articulates the full spectrum.

- **Contrast invocation mechanisms** (Claim 6 vs. `docs-ghaw-orchestration-patterns.md`
  Claim 3): Inline sub-agents are invoked via natural language instructions in
  the parent prompt; `call-workflow` workers are invoked via compiler-generated
  typed MCP tools. For practitioners designing delegation: inline is more
  flexible (any natural language instruction) but less structured (no schema
  validation); `call-workflow` is more structured (typed MCP tool from worker
  inputs) but less flexible. Document this trade-off explicitly.

## Extraction Notes

1. **Page is compact and self-contained**: The Inline Sub-Agents reference page
   is a focused short reference — roughly 300–400 words, one code example, one
   table, and one callout. All content was read; claims were fully exhausted in
   7 extractions.

2. **No linked sub-pages were followed**: The navigation lists related reference
   pages (Copilot Agent Files, Workflow Structure, Frontmatter, Markdown) that
   are general references, not specific to inline sub-agents. The inline
   sub-agents page is self-contained. The "Imports (Copilot Agent Files)" page
   was identified as the most relevant adjacent reference but was not followed,
   as the Prospector's scope was specifically this reference page.

3. **No publication date**: Like other gh-aw documentation pages, this page does
   not carry an explicit publication date. `date_published` is left null.

4. **Engine restriction is stated as a callout**: The "no `engine` field"
   constraint appears in a Note callout box — the documentation explicitly
   flags it as an important practitioner warning, not buried prose.

5. **No contradictions to file**: Reviewed all existing source notes against all
   extracted claims. The inline sub-agent pattern is new to the corpus but
   consistent with the broader gh-aw architecture. The engine restriction adds
   specificity to existing engine-selection documentation without opposing any
   existing claim. No contradiction issue required.
