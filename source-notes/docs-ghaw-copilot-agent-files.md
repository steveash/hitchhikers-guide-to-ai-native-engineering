---
source_url: https://github.github.com/gh-aw/reference/copilot-custom-agents
source_type: docs
title: "GitHub Agentic Workflows: Importing Copilot Agent Files"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#374"
---

# GitHub Agentic Workflows: Importing Copilot Agent Files

> Reference documentation for the `imports` field mechanism that brings external
> Copilot agent files into gh-aw workflows — covering the local vs. remote import
> formats, the `owner/repo/path@ref` version-pinning convention, commit SHA caching,
> agent file frontmatter fields, organization collection patterns, multi-component
> composition, and the engine-specific injection distinction (Copilot native vs.
> prompt injection for Claude and Codex).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows reference page — in the `reference/`
  section under "Imports (Copilot Agent Files)," positioned in the site navigation
  between "Imports (APM)" and "Inline Sub-Agents")
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team operating the gh-aw platform. Format specifications, constraint claims,
  caching behavior, and engine-specific handling are authoritative for the gh-aw
  platform. Claims about Copilot-native vs. prompt-injection behavior are first-party
  but reflect an implementation detail specific to this platform and are not externally
  verified.
- **Scope**: Covers the Copilot agent file format, the `imports` field for local and
  remote agent file references, the `owner/repo/path@ref` remote pinning convention,
  commit SHA caching, organization-level agent collections, combining agent file
  imports with tool/MCP/policy imports, and inline agent definition as an alternative.
  Does NOT cover: the full `imports` system (separate reference page), general
  frontmatter fields (separate reference), or the complete inline sub-agent syntax
  (explicitly deferred to the adjacent Inline Sub-Agents reference already mined as
  `docs-ghaw-inline-sub-agents.md`).

## Extracted Claims

### Claim 1: "Custom agents" is the Copilot term for specialized task-specific prompts stored as markdown files in `.github/agents/` — Copilot processes them natively while other engines (Claude, Codex) inject the markdown body as a plain prompt

- **Evidence**: Stated directly in the Overview section: "'Custom agents' is a term
  used in GitHub Copilot for specialized prompts for behaviors for specific tasks.
  They are markdown files stored in the `.github/agents/` directory and imported via
  the `imports` field. Copilot supports agent files natively, while other engines
  (Claude, Codex) inject the markdown body as a prompt."
- **Confidence**: settled (first-party documentation; the engine-specific handling is
  an explicit implementation detail stated in the introductory paragraph)
- **Quote**: "Copilot supports agent files natively, while other engines (Claude,
  Codex) inject the markdown body as a prompt."
- **Our assessment**: The engine-specific handling distinction has architectural
  implications for multi-engine teams: Copilot can interpret the agent file's
  frontmatter fields (`tools`, `mcp-servers`) natively; Claude and Codex receive
  only the markdown body as additional prompt context, with frontmatter fields
  ignored for agent-file-specific behavior. This extends `docs-ghaw-how-they-work.md`
  Claim 9 (multi-engine support with the same workflow structure) — the workflow
  *structure* is identical across engines but what each engine does with an agent
  file import differs. For Ch04 (Multi-Agent Orchestration): practitioners using
  Claude as the workflow engine should not expect Copilot-specific agent file
  features (e.g., native tool bindings via `tools` frontmatter) to be honored.

### Claim 2: Agent files are imported into workflows via the `imports` field in workflow frontmatter, with support for both local (same-repo) and remote (cross-repo) sources

- **Evidence**: "Import Copilot agent files in your workflow using the `imports`
  field. Agent files can be imported from local `.github/agents/` directories or
  from external repositories." Code examples are provided for both local and remote
  paths.
- **Confidence**: settled (first-party documentation; `imports` is a documented
  workflow frontmatter field with explicit code examples)
- **Quote**: "Import Copilot agent files in your workflow using the `imports` field.
  Agent files can be imported from local `.github/agents/` directories or from
  external repositories."
- **Our assessment**: The `imports` field is a multipurpose composition mechanism —
  the same field handles agent file imports, tool configuration imports, MCP server
  imports, and security policy imports (see Claim 7). The agent file is one category
  of importable component in the gh-aw composition model. This is consistent with
  `docs-ghaw-how-they-work.md` Claim 1's two-component structure: the `imports`
  field is a YAML frontmatter capability that extends the workflow's effective tool
  and instruction surface before execution. For Ch02 (Harness Engineering): the
  `imports` field is the primary harness composition mechanism; practitioners should
  understand that agent files, tools, MCPs, and policies all flow through the same
  field.

### Claim 3: Local agent file imports use a repository-relative path (`imports: - .github/agents/my-agent.md`) and create no external versioning dependency

- **Evidence**: The "Local Agent File Import" section provides a code example
  showing the local import syntax in workflow frontmatter. The path format
  (`.github/agents/my-agent.md`) and the constraint that the file must be in
  `.github/agents/` are consistent with the Agent File Requirements section.
- **Confidence**: settled (first-party documentation with a code example)
- **Quote**: (no direct prose quote; code example shows `imports: - .github/agents/my-agent.md`)
- **Our assessment**: Local imports are the simplest composition form — no external
  dependency, no versioning required, the agent file evolves with the repository.
  The path must be within `.github/agents/` per the Agent File Requirements (Claim 5).
  For Ch02: use local imports when the agent is repository-specific; use remote
  imports (Claim 4) when the agent should be shared across repositories as an
  organizational standard.

### Claim 4: Remote agent file imports use the `owner/repo/path@ref` format, and the `@ref` must be a tag or commit reference — floating branch references are not supported

- **Evidence**: The "Remote Agent File Import" section documents the format with the
  example `acme-org/shared-agents/.github/agents/code-reviewer.md@v1.0.0`. The
  Agent File Requirements section states: "Remote imports require explicit versioning
  via tags or commit references."
- **Confidence**: settled (first-party documentation; format is specified with a
  concrete example and the versioning requirement is stated explicitly)
- **Quote**: (no single prose quote; format appears in code example as
  `acme-org/shared-agents/.github/agents/code-reviewer.md@v1.0.0` and requirement
  states "Remote imports require explicit versioning via tags or commit references")
- **Our assessment**: The `@ref` versioning requirement enforces reproducibility
  for cross-repository agent composition — workflows cannot float against a moving
  branch HEAD. This aligns with the gh-aw lock file model in
  `docs-ghaw-how-they-work.md` Claim 7: pinning remote imports by tag or commit SHA
  is the import-level equivalent of the lock file's compile-time reproducibility
  guarantee. For Ch02: recommend that teams maintaining shared agent file libraries
  create version tags (e.g., `v1.0.0`, `v2.0.0`) to enable stable `@ref` pinning
  across all consumer workflows. Untagged repositories force consumers to use commit
  SHAs, which is brittle for humans to maintain.

### Claim 5: Remote agent files are cached by commit SHA in `.github/aw/imports/`, enabling reproducible re-execution without network round-trips

- **Evidence**: Listed explicitly in the Agent File Requirements section: "Caching:
  Remote agent files are cached by commit SHA in `.github/aw/imports/`"
- **Confidence**: settled (first-party documentation; the cache path is specifically
  stated)
- **Quote**: "Remote agent files are cached by commit SHA in `.github/aw/imports/`"
- **Our assessment**: Commit SHA caching means remote imports are resolved once and
  served from a local cache for subsequent runs. The cache captures exactly which
  version of the agent file was used, ensuring two runs of the same workflow use
  identical agent instructions. It also means `.github/aw/imports/` is a
  platform-managed directory that accumulates cached files over time. Practitioners
  should not manually edit files in this directory and should understand that it is
  part of the platform's import resolution infrastructure. For Ch02: document
  `.github/aw/imports/` as a platform-managed cache directory alongside
  `.github/aw/` (compiled lock files) in any harness file structure reference.

### Claim 6: The imported agent file's instructions are merged with the workflow prompt — the agent file contributes additively to the effective prompt the engine receives

- **Evidence**: Stated in the "Remote Agent File Import" section: "The agent
  instructions are merged with the workflow prompt, customizing the AI engine's
  behavior for specific tasks."
- **Confidence**: settled (first-party documentation; merge behavior explicitly
  described)
- **Quote**: "The agent instructions are merged with the workflow prompt,
  customizing the AI engine's behavior for specific tasks."
- **Our assessment**: The merge model means an agent file is additive, not
  substitutive. The agent file contributes a "role" or "persona" layer; the
  workflow's own instruction section contributes the specific task. Overlap
  between agent file contents and workflow instructions results in redundant
  prompt content. For Ch02: practitioners designing agent file contents should
  put role definitions, behavioral constraints, and general expertise scope in
  the agent file, and task-specific instructions in the workflow's markdown body.
  The merge model favors specialization of each layer.

### Claim 7: The `imports` field supports mixing agent file imports with tool configurations, MCP servers, and security policies in a single workflow frontmatter — enabling modular, multi-layer harness assembly

- **Evidence**: The "Combining Copilot Agent Files with Other Imports" section
  provides a code example that mixes four types of imports: a custom agent file
  (`security-auditor.md@v2.0.0`), tool configurations (`github-standard.md@v1.0.0`),
  MCP servers (`database.md@v1.0.0`), and security policies (`security-policies.md@v1.0.0`),
  all within a single `imports` field.
- **Confidence**: settled (first-party documentation with a complete code example)
- **Quote**: "You can mix custom agent file imports with tool configurations and
  shared components"
- **Our assessment**: Multi-component imports enable a layered harness: the agent's
  role comes from a shared agent library, its tools from a shared tool library, its
  MCP connections from a shared MCP library, and security constraints from a shared
  policy library. Each layer can be versioned and maintained independently by
  different teams. This is the gh-aw pattern for enterprise-grade harness engineering.
  For Ch02: document the multi-layer `imports` model as the organizational deployment
  pattern for gh-aw, distinct from the single-repo local-import model. Each layer
  type deserves its own versioned repository when shared across many workflows.

### Claim 8: Organizations can create centralized agent file libraries — versioned repositories containing multiple specialized agent files — that teams import with explicit `@ref` pins for cross-repository reuse

- **Evidence**: The "Copilot Agent File Collections" section states: "Organizations
  can create libraries of specialized custom agent files" and provides a directory
  structure example showing one repository (`acme-org/ai-agents`) containing five
  specialized agent files for different tasks.
- **Confidence**: settled (first-party documentation with a code example of the
  directory layout and an import example using version-pinned imports)
- **Quote**: "Organizations can create libraries of specialized custom agent files"
- **Our assessment**: This is the gh-aw pattern for organizational agent
  standardization. Rather than each repository defining its own code-reviewer or
  security-auditor agent instructions from scratch, a central team maintains a
  versioned library that all repositories import. Version-pinned imports
  (`@v2.0.0`) mean consuming repositories explicitly opt into agent updates.
  This extends `docs-ghaw-agentic-authoring.md` Claim 3 (migration vs.
  synchronization): organization agent file collections are the synchronization
  path specifically for agent instructions. For Ch04 (Multi-Agent Orchestration):
  organization-level libraries enable teams to compose multi-specialist workflows
  from a shared catalogue rather than building each specialist from scratch.

### Claim 9: Copilot agent file frontmatter supports `name`, `description`, `tools`, and `mcp-servers` fields — but the page does not document how `tools` and `mcp-servers` interact with the importing workflow's own tool and MCP configuration

- **Evidence**: The "Agent File Requirements" section states: "Frontmatter: Can
  include `name`, `description`, `tools`, and `mcp-servers`." The Overview code
  example (`my-agent.md`) only shows `name` and `description` in use. The page
  does not explain the merge semantics for `tools` and `mcp-servers`.
- **Confidence**: emerging (`name` and `description` are demonstrated; `tools` and
  `mcp-servers` are listed as supported but not demonstrated or explained)
- **Quote**: "Can include `name`, `description`, `tools`, and `mcp-servers`"
- **Our assessment**: The `tools` and `mcp-servers` fields in agent file frontmatter
  are underspecified in this page — listed as allowed but their behavior when imported
  is not explained. Key unanswered questions: Does importing an agent file with
  `mcp-servers` add those servers to the workflow's MCP configuration or override it?
  Does an agent file's `tools` list merge with the workflow's tool allowlist? The
  interaction model matters for security (could importing an agent file expand the
  workflow's tool attack surface?) and debugging (why is an unexpected MCP server
  available?). For Ch02: practitioners should test the `tools` and `mcp-servers`
  merge behavior empirically and document the results. The main Imports reference
  (`/reference/imports/`) may clarify this.

### Claim 10: The page's Agent File Requirements state "only one agent file can be imported per workflow," but a code example on the same page shows two agent files imported in the same workflow — the constraint and the example directly contradict each other

- **Evidence**: Requirements section states: "One per workflow: Only one agent file
  can be imported per workflow." The "Copilot Agent File Collections" security review
  example shows:
  ```
  imports:
    - acme-org/ai-agents/.github/agents/security-auditor.md@v2.0.0
    - acme-org/ai-agents/.github/agents/code-reviewer.md@v1.5.0
  ```
  That is two agent file imports in the same workflow frontmatter.
- **Confidence**: anecdotal (requirement text and code example contradict each other
  within the same page; neither can be taken as authoritative without external
  confirmation)
- **Quote**: "Only one agent file can be imported per workflow"
- **Our assessment**: This is an internal documentation inconsistency. The
  requirements section says one agent file per workflow; the code example shows two.
  Possible interpretations: (a) the constraint applies to Copilot-native processing
  only (one agent "personality" processed natively) while multiple markdown bodies
  can be merged as prompts; (b) the requirement text is wrong and multiple agent
  files are supported; (c) the code example is wrong and only one is actually
  enforced. Practitioners should verify empirically before relying on either the
  constraint or the multi-file example as a design choice. See Extraction Notes for
  the internal contradiction flag.

## Concrete Artifacts

### Agent File Format — Minimal Example

```markdown
---
name: My Copilot Agent
description: Specialized prompt for code review tasks
---

# Agent Instructions
You are a specialized code review agent. Focus on:
- Code quality and best practices
- Security vulnerabilities
- Performance optimization
```

*Source: Importing Copilot Agent Files reference page — Overview section,
`.github/agents/my-agent.md` code example*

### Local Agent File Import — Workflow Frontmatter

```yaml
---
on: pull_request
engine: copilot
imports:
  - .github/agents/my-agent.md
---

Review the pull request and provide feedback.
```

*Source: Importing Copilot Agent Files reference page — "Local Agent File Import"
section*

### Remote Agent File Import — `owner/repo/path@ref` Format

```yaml
---
on: pull_request
engine: copilot
imports:
  - acme-org/shared-agents/.github/agents/code-reviewer.md@v1.0.0
---

Perform comprehensive code review using shared agent instructions.
```

*Source: Importing Copilot Agent Files reference page — "Remote Agent File Import"
section*

### Organization Agent File Library — Directory Layout

```
acme-org/ai-agents/
└── .github/
    └── agents/
        ├── code-reviewer.md         # General code review
        ├── security-auditor.md      # Security-focused analysis
        ├── performance-analyst.md   # Performance optimization
        ├── accessibility-checker.md # WCAG compliance
        └── documentation-writer.md  # Technical documentation
```

*Source: Importing Copilot Agent Files reference page — "Copilot Agent File
Collections" section*

### Multi-Layer Composition — Agent + Tools + MCP + Policies

```yaml
---
on: pull_request
engine: copilot
imports:
  # Import specialized custom agent file
  - acme-org/ai-agents/.github/agents/security-auditor.md@v2.0.0

  # Import tool configurations
  - acme-org/workflow-library/shared/tools/github-standard.md@v1.0.0

  # Import MCP servers
  - acme-org/workflow-library/shared/mcp/database.md@v1.0.0

  # Import security policies
  - acme-org/workflow-library/shared/config/security-policies.md@v1.0.0
permissions:
  contents: read
safe-outputs:
  create-pull-request-review-comment:
    max: 10
---

# Comprehensive Security Review
Perform detailed security analysis using specialized agent files and tools.
```

*Source: Importing Copilot Agent Files reference page — "Combining Copilot Agent
Files with Other Imports" section*

### Agent File Requirements Summary

```
Location:     Must be in .github/agents/ directory (local or remote)
Format:       Markdown with YAML frontmatter
Frontmatter:  Can include name, description, tools, mcp-servers
Count:        "Only one agent file can be imported per workflow"
              ⚠ Conflicts with multi-agent-file code example — see Claim 10
Caching:      Remote agent files cached by commit SHA in .github/aw/imports/
Versioning:   Remote imports require explicit versioning via tags or commit references
```

*Source: Importing Copilot Agent Files reference page — "Agent File Requirements"
section*

### Inline Agent Definition (Alternative — Deferred to Adjacent Reference)

```markdown
## agent: `code-reviewer`
---
model: claude-sonnet-4.5
description: Reviews code for quality and correctness
---
You are a code review agent. Analyze the provided code for bugs, style issues,
and potential improvements. Be specific and actionable.
```

*Source: Importing Copilot Agent Files reference page — "Defining Agents Inline"
section. Full specification in `docs-ghaw-inline-sub-agents.md`.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support: Copilot, Claude,
    Codex, Gemini all use the same workflow structure): Claim 1 here adds
    engine-specific nuance — the workflow *structure* is identical, but each engine's
    *runtime handling* of agent file imports differs. Copilot processes the agent
    file natively; Claude and Codex inject only the markdown body as a prompt.
  - `docs-ghaw-inline-sub-agents.md` Claim 1 (inline sub-agents are defined in the
    workflow file "instead of creating a separate file in `.github/agents/`"): This
    source explicitly presents inline agents as an alternative to separate `.github/agents/`
    files (the mechanism documented here). The two sources together cover both
    composition paths for agent definitions in gh-aw.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 1 (two-component workflow structure: YAML
    frontmatter + markdown instructions): This source extends the frontmatter
    component by documenting the `imports` field — the mechanism that assembles
    agent files, tools, MCP servers, and security policies into the workflow's
    capability surface at compile time.
  - `docs-ghaw-agentic-authoring.md` (general authoring lifecycle): That note
    documents the authoring workflow but does not cover the agent file import
    mechanism. This note fills the gap: local vs. remote import paths,
    `owner/repo/path@ref` format, organization collections, and multi-layer
    composition.
  - `docs-ghaw-inline-sub-agents.md` (inline sub-agent specification): This source
    covers the external agent file path; that source covers the inline path. Together
    they give the complete picture of gh-aw's two agent composition approaches.

- **Contradicts**: None identified with existing corpus notes.

- **Novel**:
  - **`imports` field as the agent file composition mechanism** (Claims 2, 3, 4):
    The specific `imports` field as the workflow frontmatter mechanism for agent
    file references (local and remote) is not documented in any existing corpus note.
  - **`owner/repo/path@ref` remote import format** (Claim 4): The cross-repository
    agent file import syntax with explicit version pinning is new to the corpus.
  - **Commit SHA caching in `.github/aw/imports/`** (Claim 5): The platform-managed
    cache location for remote agent files is new to the corpus.
  - **Agent instruction merge behavior** (Claim 6): The explicit statement that
    agent file instructions merge additively with workflow prompts is new.
  - **Organization agent file collections** (Claim 8): The pattern of centralized,
    versioned agent libraries for organizational reuse is new to the corpus.
  - **`tools` and `mcp-servers` in agent file frontmatter** (Claim 9): The existence
    of these fields (and the interaction uncertainty) is new to the corpus.
  - **Engine-specific agent file handling** (Claim 1): The explicit distinction
    between Copilot-native processing and prompt injection for Claude/Codex is new.

## Guide Impact

### Chapter 02: Harness Engineering

- **Document `imports` as the primary harness composition mechanism** (Claims 2, 7):
  The `imports` field is how gh-aw workflows assemble their capability surface — agent
  roles, tool allowlists, MCP connections, and security policies all flow through it.
  Ch02 should give `imports` top-level treatment alongside the frontmatter and
  markdown structure, not treat it as a footnote.

- **Add local vs. remote import decision guidance** (Claims 3, 4): Use local imports
  (`.github/agents/my-agent.md`) when the agent is specific to one repository; use
  remote imports (`owner/repo/path@ref`) when the agent encodes organizational
  standards that should be shared across repositories. Pair this with a recommendation
  to tag shared agent file releases to enable stable `@ref` pinning.

- **Add organization agent file collections as the primary harness sharing pattern**
  (Claim 8): Organizations needing consistent agent behaviors across many repositories
  should build versioned agent file libraries in a dedicated repository and import
  with explicit version pins. This is the synchronization path for agent instructions
  — the agent-file counterpart to `gh aw add` for workflow synchronization (from
  `docs-ghaw-agentic-authoring.md` Claim 3).

- **Flag the one-per-workflow ambiguity** (Claim 10): Until the documentation
  inconsistency is resolved, Ch02 should note that the maximum number of agent file
  imports per workflow is unconfirmed — the requirements say one, but a code example
  shows two. Practitioners should verify empirically before building multi-agent-file
  workflows.

### Chapter 04: Multi-Agent Orchestration Patterns

- **Engine-specific agent file behavior** (Claim 1): When the workflow engine is
  Claude or Codex, agent file imports provide only prompt injection (the markdown
  body), not native Copilot agent file processing. Teams building multi-engine
  workflows should design agent file contents to work as prompt text, not as
  Copilot-specific configurations.

- **Agent file collections as pre-composition** (Claim 8): Organization libraries
  let teams compose multi-specialist workflows from a catalogue of versioned,
  shared agent definitions — an organizational-level composition layer that sits
  below inline sub-agents in the composition spectrum. Cite alongside
  `docs-ghaw-inline-sub-agents.md` Claims 1, 5 for the full intra-file, then
  cross-file picture.

## Extraction Notes

1. **Internal documentation inconsistency (Claim 10)**: The page states "Only one
   agent file can be imported per workflow" in the requirements section, but its own
   code example under "Copilot Agent File Collections" imports two agent files in the
   same workflow. This is an internal self-contradiction within the source. The most
   plausible interpretation is that the requirement applies to Copilot-native agent
   file processing and the documentation was not consistently updated — but this is
   speculative. No contradiction issue was filed (the conflict is within a single
   source page and requires empirical testing to resolve, not editorial adjudication
   between competing claims). The inconsistency is prominently flagged in Claim 10.

2. **`tools` and `mcp-servers` frontmatter fields underspecified**: Agent file
   frontmatter supports `tools` and `mcp-servers` but the page explains neither the
   semantics of these fields nor how they interact with the importing workflow's own
   tool and MCP configuration. The main Imports reference page
   (`https://github.github.com/gh-aw/reference/imports/`) was not followed but may
   clarify this.

3. **Inline agent definition section not re-extracted**: The "Defining Agents Inline"
   section of this page covers the `## agent: \`name\`` heading mechanism, which is
   fully documented in the already-mined `docs-ghaw-inline-sub-agents.md` (issue #522).
   The page explicitly defers to the Inline Sub-Agents reference for the complete
   syntax specification. This content is not re-extracted here beyond a brief artifact
   capture.

4. **No publication date**: Like other gh-aw documentation pages, this page does not
   carry an explicit publication date. `date_published` is left null. Content is
   consistent with the gh-aw platform as of 2026-05-11.

5. **No contradictions with existing corpus**: Reviewed all existing source notes
   against extracted claims. No claims in this source materially oppose existing
   notes. The engine-specific agent file handling (Claim 1) adds new specificity to
   multi-engine support without contradicting `docs-ghaw-how-they-work.md` Claim 9.
