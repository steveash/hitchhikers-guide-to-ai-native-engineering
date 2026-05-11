---
source_url: https://github.github.com/gh-aw/reference/custom-agent-for-aw
source_type: docs
title: "GitHub Agentic Workflows: Copilot Agent Files Support (Custom Agent)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#377"
---

# GitHub Agentic Workflows: Copilot Agent Files Support (Custom Agent)

> Reference documentation for the `agentic-workflows` custom agent — a Copilot
> Agent File installed by `gh aw init` that equips Copilot Chat, Copilot CLI, and
> VSCode Agent Mode with five gh-aw-specific authoring capabilities (create,
> update, upgrade, import, debug), plus three alternative approaches for
> non-Copilot environments.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows reference page, in the
  `reference/` section, positioned between "Imports (Copilot Agent Files)" and
  "Inline Sub-Agents" in the site navigation — documenting a specific agent that
  helps users author and manage agentic workflows, not an overview or conceptual
  guide)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that operates the gh-aw platform. Claims about agent capabilities,
  command syntax, and file locations are authoritative for this platform. Claims
  about generalizability of the meta-pattern (using Copilot Agent Files to build
  platform tooling) are interpretive and assessed separately.
- **Scope**: The `agentic-workflows` custom agent — what it is, how to install it,
  its five specific capabilities, and three alternative approaches for environments
  without the agent installed. Does NOT cover: the Copilot Agent Files import
  mechanism (see `docs-ghaw-copilot-agent-files.md`), the broader authoring
  lifecycle beyond this specific agent (see `docs-ghaw-agentic-authoring.md`), or
  the compilation model, security architecture, or orchestration patterns.

## Extracted Claims

### Claim 1: The `agentic-workflows` custom agent is a Copilot Agent File (`.github/agents/agentic-workflows.agent.md`) that extends Copilot Chat, CLI, and VSCode Agent Mode with gh-aw-specific workflow authoring capabilities

- **Evidence**: The page overview states: "GitHub Agentic Workflows offers
  custom agents—specialized prompts for Copilot, Copilot CLI, and VSCode Agent
  Mode—to facilitate creation, modification, and debugging of agentic workflows."
  The Installation section confirms the file created: "`gh aw init` creates
  `.github/agents/agentic-workflows.agent.md`, registering the
  `/agent agentic-workflows` command in Copilot Chat."
- **Confidence**: settled (first-party documentation; the file path and command
  are explicitly stated)
- **Quote**: "GitHub Agentic Workflows offers custom agents—specialized prompts
  for Copilot, Copilot CLI, and VSCode Agent Mode—to facilitate creation,
  modification, and debugging of agentic workflows."
- **Our assessment**: The `agentic-workflows` agent is itself a Copilot Agent File
  — the same format documented in `docs-ghaw-copilot-agent-files.md` for importing
  agent instructions into workflows. The gh-aw platform uses its own Copilot Agent
  Files format for its primary authoring interface. This is a self-referential
  meta-pattern: the tooling that helps practitioners build Copilot Agent File-based
  workflows is itself a Copilot Agent File. For Ch02 (Harness Engineering): the
  `agentic-workflows.agent.md` is a concrete example of the Copilot Agent Files
  format serving a platform-level purpose, distinct from agent files imported as
  workflow components.

### Claim 2: Three installation paths create the custom agent — the GitHub Agents tab, VSCode Agent Mode initiation, and the `gh aw init` CLI — all producing `.github/agents/agentic-workflows.agent.md`

- **Evidence**: The Installation section explicitly lists three entry points:
  "Users initialize repositories by navigating to the Agents tab on GitHub,
  starting VSCode Agent Mode, or running: `gh aw init`." All three result in
  creation of `.github/agents/agentic-workflows.agent.md`.
- **Confidence**: settled (first-party documentation; the three paths are
  enumerated alongside the output file)
- **Quote**: (no single prose quote covering all three paths; the three paths
  appear as an enumeration in the installation section)
- **Our assessment**: The three installation paths reflect three distinct practitioner
  contexts: browser-based (Agents tab), editor-based (VSCode Agent Mode), and
  CLI-based (`gh aw init`). All converge on the same artifact. The `docs-ghaw-agentic-authoring.md`
  Claim 1 documents only the CLI path (`gh aw init`) and does not name the Agents
  tab or VSCode Agent Mode as equivalent installation triggers. This reference page
  is the authoritative source for the complete installation surface. For Ch02: the
  three-path equivalence means practitioners do not need the CLI to set up the
  authoring agent — opening the Agents tab in the browser or initiating VSCode Agent
  Mode are sufficient.

### Claim 3: The custom agent generates complete, configured workflow files (frontmatter, prompts, tools, permissions) from natural language goal descriptions

- **Evidence**: The "Creating Workflows" capability is described: "Users invoke
  natural language prompts like 'create a workflow that triages issues' to generate
  configured workflow files with frontmatter, prompts, tools, and permissions."
- **Confidence**: settled (first-party; the capability is stated with an example
  prompt and an enumeration of what the generated file contains)
- **Quote**: "create a workflow that triages issues"
- **Our assessment**: The agent does not require the practitioner to know the
  workflow file format — it translates a goal description into a complete, properly
  structured workflow file with all required components. This is the primary value
  proposition of the authoring agent: abstracting YAML/frontmatter authoring behind
  a natural language interface. The agent handles the structural plumbing (frontmatter,
  tool declarations, permission blocks) while the practitioner focuses on the goal.
  For Ch02: document this as the entry-level workflow creation path; contrast with
  manual authoring (requiring knowledge of the full schema) and the `create.md`
  URL-addressable prompt documented in `docs-ghaw-setup-creating-workflows.md`.

### Claim 4: Existing workflows are modified through conversational natural language instructions addressed to the agent — no direct YAML editing required

- **Evidence**: "Commands such as 'update the issue-triage workflow to add
  web-fetch tool' modify workflows through conversational instructions."
- **Confidence**: settled (first-party documentation; the command form is explicitly
  demonstrated)
- **Quote**: "update the issue-triage workflow to add web-fetch tool"
- **Our assessment**: Conversational modification treats the workflow file as a
  mutable object that the agent reads and rewrites based on instructions. The
  practitioner names the workflow and describes the change; the agent handles
  locating the file, making the appropriate schema-level edit, and writing the
  result. This is a significant ergonomic improvement over direct YAML editing,
  particularly for practitioners unfamiliar with the full frontmatter schema. For
  Ch02: document conversational modification as the primary workflow maintenance
  path for practitioners using Copilot Chat; contrast with direct file editing
  for practitioners who prefer explicit schema control.

### Claim 5: The custom agent maintains workflow version compatibility by upgrading workflow format to the current platform version

- **Evidence**: "The agent maintains compatibility by upgrading 'all workflows to
  latest version.'"
- **Confidence**: settled (first-party; the upgrade capability and example command
  are stated)
- **Quote**: "all workflows to latest version"
- **Our assessment**: Workflow upgrade is a maintenance operation that suggests
  the gh-aw platform evolves its workflow format over time — the agent abstracts
  migration from one format version to another. Practitioners who have existing
  workflows written against an earlier format can use the agent to update them
  without manually auditing the schema diff between versions. For Ch02: document
  upgrade as a maintenance operation; note that the agent handles version-to-version
  migration automatically, reducing the burden of format changes on practitioners.

### Claim 6: The custom agent imports workflows from external repositories with optional customizations including engine selection

- **Evidence**: "Users import workflows from external repositories with optional
  customizations like engine selection."
- **Confidence**: settled (first-party; the capability is stated with an example
  customization type)
- **Quote**: (no direct quote; the capability appears as a paraphrase in the source)
- **Our assessment**: Agent-mediated import adds a customization layer over raw
  workflow file copying — the agent can adapt the imported workflow's configuration
  (such as engine selection) for the target repository. This differs from
  `create-agentic-agent` (documented in `docs-ghaw-agentic-authoring.md` Claim 3),
  which performs AI-assisted migration with dependency analysis. The import
  capability described here appears to be lighter-weight: importing and configuring
  a workflow with specific overrides rather than doing a full AI-assisted adaptation.
  For Ch02: clarify the distinction between agent-mediated import (this claim) and
  `create-agentic-agent` migration (Claim 3 in `docs-ghaw-agentic-authoring.md`) —
  both involve cross-repository workflow reuse but with different levels of AI-driven
  adaptation.

### Claim 7: The custom agent debugs failing workflow runs by accepting run URLs or natural language failure descriptions and returning root cause analysis with targeted fixes for permission errors, missing tools, and network issues

- **Evidence**: "By providing run URLs or describing failures, the agent audits
  logs, identifies root causes, and suggests fixes for permission errors, missing
  tools, and network issues."
- **Confidence**: settled (first-party; the two input modes and the three root
  cause categories are explicitly named)
- **Quote**: (no direct verbatim quote isolated; the capability description appears
  as integrated prose in the source)
- **Our assessment**: The debugging capability accepts two input modalities — a
  structured run URL (when the practitioner knows the run ID) and a natural language
  failure description (when the practitioner is debugging from memory or Copilot Chat
  context). The three root cause categories (permission errors, missing tools, network
  issues) are the same as those documented in `docs-ghaw-agentic-authoring.md` Claim 5,
  confirming that the root cause taxonomy is consistent between the guides and reference
  documentation. The natural language description input mode is not mentioned in the
  guides page, which only documents the run URL path — this source adds the alternative
  conversational debugging path. For Ch01 (Daily Workflows): document both input modes
  for the debugging capability.

### Claim 8: Three alternative non-Copilot approaches cover the same authoring and debugging tasks for practitioners without the custom agent installed

- **Evidence**: "For repositories without the agent installed or alternative AI
  assistants, a standalone debugging prompt at `debug.md` offers self-contained
  instructions. Additionally, `agentic-chat.md` assists with AI chatbot-based
  workflow authoring, while `DICTATION.md` corrects speech-to-text terminology
  issues."
- **Confidence**: settled (first-party; the three alternatives are named alongside
  their purposes)
- **Quote**: "For repositories without the agent installed or alternative AI
  assistants, a standalone debugging prompt at `debug.md` offers self-contained
  instructions."
- **Our assessment**: The three alternatives map directly to three of the five custom
  agent capabilities: `debug.md` → debugging (Claim 7), `agentic-chat.md` → creating
  workflows (Claim 3), `DICTATION.md` → assistive input pre-processing (not a
  standalone capability equivalent). Notably, there are NO stated alternatives for
  updating (Claim 4), upgrading (Claim 5), or importing (Claim 6) — suggesting these
  capabilities are only available through the installed custom agent. For Ch02: document
  that the custom agent is required for the update, upgrade, and import operations;
  the alternatives cover only creation and debugging.

### Claim 9: The gh-aw platform uses its own Copilot Agent Files format for its primary authoring interface — the `agentic-workflows.agent.md` agent is a platform-level Copilot Agent File that users of the platform work *with*, not one they import *into* workflows

- **Evidence**: The `agentic-workflows.agent.md` file lives in `.github/agents/`
  (the Copilot Agent Files standard location per `docs-ghaw-copilot-agent-files.md`
  Claim 1) and registers as a Copilot Chat command (`/agent agentic-workflows`).
  It is created by the same platform (`gh aw init`) that enables importing Copilot
  Agent Files into workflows via the `imports` field.
- **Confidence**: emerging (the meta-pattern is an interpretive claim based on
  observing that both the platform tooling and workflow components use the same
  file format and directory; not explicitly stated in the source)
- **Quote**: (no direct quote; this is an observational claim synthesized from
  multiple source details)
- **Our assessment**: The same `.github/agents/` format and directory serve two
  distinct roles in the gh-aw ecosystem: (1) platform-level tooling — the
  `agentic-workflows.agent.md` agent that practitioners use to author and manage
  workflows; and (2) workflow components — agent files imported via the `imports`
  field to define roles within specific workflows. This dual use has an important
  practical implication: a `.github/agents/` file is not necessarily a workflow
  component — it might be platform meta-tooling. For Ch02: when documenting the
  `.github/agents/` directory, note that it serves both roles and that not all
  files in it are workflow-composition components.

## Concrete Artifacts

### Installation — Three Equivalent Paths

```bash
# Path 1: CLI (most common)
gh aw init
# → Creates .github/agents/agentic-workflows.agent.md
# → Registers /agent agentic-workflows in Copilot Chat

# Path 2: GitHub Web Interface
# Navigate to: GitHub repository → Agents tab

# Path 3: VSCode
# Start VSCode Agent Mode (triggers agent setup)
```

*Source: custom-agent-for-aw reference page — "Installation" section*

### Five Core Capabilities — Natural Language Invocation Patterns

```
Capability       Example invocation
─────────────────────────────────────────────────────────────────
Create           /agent agentic-workflows create a workflow that triages issues
Update           /agent agentic-workflows update the issue-triage workflow
                 to add web-fetch tool
Upgrade          /agent agentic-workflows upgrade all workflows to latest version
Import           /agent agentic-workflows import workflow from [external-repo-url]
Debug (URL)      /agent agentic-workflows debug [run-url]
Debug (natural)  /agent agentic-workflows [describe the failure in plain language]
```

*Source: custom-agent-for-aw reference page — "Key Capabilities" section*

### Three Alternative Approaches (Non-Copilot)

```
Task              Alternative                   When to use
─────────────────────────────────────────────────────────────────
Debugging         debug.md (standalone URL)     No Copilot, any AI assistant,
                                                or no agent installed
Workflow creation agentic-chat.md instructions  AI chatbot-based specification
Speech input      DICTATION.md prompt           Speech-to-text pre-processing
                                                (terminology correction)

NOTE: No stated alternatives for Update, Upgrade, or Import capabilities —
      these require the installed custom agent.
```

*Source: custom-agent-for-aw reference page — "Alternative Approaches" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` bootstraps the
    repository with the authoring agent): this reference page confirms the
    specific file created by `gh aw init` is `.github/agents/agentic-workflows.agent.md`.
    The guides page says "configure your repository with a few files" without naming
    them; this reference page names the file explicitly.
  - `docs-ghaw-agentic-authoring.md` Claim 5 (`/agent agentic-workflows debug`
    diagnoses failing runs with root cause categories including missing tools,
    permission errors, network blocks): both sources agree on the three root
    cause categories. This reference page adds that natural language descriptions
    (not just run URLs) are an accepted input mode for the debugging capability.
  - `docs-ghaw-agentic-authoring.md` Claim 6 (`debug.md` as a self-contained
    URL-addressable debugging prompt): this source confirms `debug.md` as the
    non-Copilot alternative for debugging, consistent with the guides page.
  - `docs-ghaw-agentic-authoring.md` Claims 8 and 9 (`agentic-chat.md` for
    chatbot-based workflow specification and `DICTATION.md` for speech-to-text
    correction): this reference page confirms both as alternatives, using the
    same file names. No new information beyond what the guides page documents
    for these two alternatives.

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` initialization): this
    source extends the guides page by adding two additional installation paths
    (GitHub Agents tab and VSCode Agent Mode) not mentioned there, and by naming
    the specific Copilot Agent File created.
  - `docs-ghaw-agentic-authoring.md` Claim 5 (debugging): adds the natural
    language description input mode alongside the run URL input mode documented
    in the guides page.
  - `docs-ghaw-copilot-agent-files.md` (Copilot Agent Files as importable workflow
    components): this source adds the complementary picture — Copilot Agent Files
    as platform-level tooling. Together they show the two uses of the `.github/agents/`
    format: components imported into workflows vs. platform tools that help build
    workflows. The distinction between these two uses is not explicitly drawn in either
    source but is important for practitioners who work with both simultaneously.

- **Contradicts**: None identified. The five-capability taxonomy, installation paths,
  and alternative approaches are consistent with existing corpus notes. The addition
  of VSCode Agent Mode as an installation path does not contradict the CLI-only
  description in `docs-ghaw-agentic-authoring.md` — the guides page omits paths
  rather than contradicting them.

- **Novel**:
  - **Three installation paths** (Claim 2): The GitHub Agents tab and VSCode Agent
    Mode as installation triggers for the authoring agent are not documented in any
    existing corpus note. `docs-ghaw-agentic-authoring.md` documents only `gh aw init`.
  - **`.github/agents/agentic-workflows.agent.md` as the explicit file created**
    (Claim 1): Existing notes describe `gh aw init` as bootstrapping the authoring
    experience but do not name the specific Copilot Agent File created. This source
    names it explicitly.
  - **Natural language description as debugging input mode** (Claim 7): The guides
    page documents run URL as the input to the debug command; this reference page
    adds natural language failure descriptions as an alternative input.
  - **Coverage gap for non-Copilot alternatives** (Claim 8): The absence of stated
    alternatives for Update, Upgrade, and Import is a new corpus finding — these
    three capabilities require the installed custom agent with no documented fallback.
  - **Dual-use `.github/agents/` directory** (Claim 9): The observation that
    `.github/agents/` serves both platform-level tooling and workflow-component
    roles is new to the corpus, though it is an interpretive claim synthesized
    from the two relevant source pages.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add three installation paths for the authoring agent** (Claim 2): The guide
  currently documents `gh aw init` as the initialization step. Extend to note that
  the GitHub Agents tab and VSCode Agent Mode also trigger agent setup, enabling
  practitioners without the CLI to get started via the browser or editor. The output
  is the same (`.github/agents/agentic-workflows.agent.md`) regardless of path.

- **Name `.github/agents/agentic-workflows.agent.md` explicitly** (Claim 1): When
  describing what `gh aw init` creates, name this file. It is a Copilot Agent File
  in the same format that workflows use for imported agent components — which makes
  it a concrete example of the format in action. Citing this reference page alongside
  `docs-ghaw-copilot-agent-files.md` provides both the "how it's used" (platform
  tooling) and "how to use it" (workflow component) perspectives.

- **Document the five-capability scope of the authoring agent** (Claims 3–7): The
  guide should give practitioners a clear reference for what the authoring agent
  handles (create, update, upgrade, import, debug) vs. what requires other tools or
  manual authoring. The three capabilities without non-Copilot alternatives (update,
  upgrade, import) should be called out explicitly — practitioners in non-Copilot
  environments need to know these operations require the installed agent.

- **Note the dual-use of `.github/agents/`** (Claim 9): When documenting the
  repository structure for gh-aw, clarify that `.github/agents/` contains both
  platform-level tooling files (like `agentic-workflows.agent.md`, added by
  `gh aw init`) and workflow-component agent files (added by practitioners). Not
  all files in this directory are workflow components. Cite `docs-ghaw-copilot-agent-files.md`
  for the workflow-component use and this note for the platform-tooling use.

### Chapter 01: Daily Workflows

- **Add natural language failure description as a debugging input mode** (Claim 7):
  The guide's debugging workflow should document both the structured path (`/agent
  agentic-workflows debug <run-url>`) and the conversational path (describing the
  failure in natural language to the agent). The run URL path is more precise when
  the run ID is known; the natural language path is useful when diagnosing from
  Copilot Chat context without leaving the chat interface.

## Extraction Notes

1. **WebFetch returns summarized content**: The gh-aw documentation is an Astro/Starlight
   SPA; WebFetch returns rendered text with AI summarization, not raw page source. Two
   fetches were performed to maximize content fidelity. The core content was consistent
   across both fetches. Verbatim quotes were extracted only where both fetches returned
   the same specific phrasing or where the content was sufficiently distinctive to be
   low-risk for summarization artifacts. Claims where the specific wording could not be
   verified verbatim are marked "(no direct quote; see paraphrase in Our assessment)."

2. **Command examples may be truncated**: The second WebFetch returned partial command
   examples (`"/agent agentic-workflows create a workflow that triages"` without the
   complete sentence). The first fetch gave more complete descriptions. Command examples
   in the Concrete Artifacts section reflect the most complete forms returned across
   both fetches; minor variations in exact syntax are possible.

3. **No publication date**: The gh-aw documentation does not carry explicit publication
   dates. `date_published` is left null. Content is consistent with current gh-aw
   platform state as of 2026-05-11.

4. **Claim 9 is interpretive**: The dual-use observation about `.github/agents/` is not
   explicitly stated in the source — it is synthesized from comparing this page with
   `docs-ghaw-copilot-agent-files.md`. The Assayer should treat it as interpretive.

5. **Import capability ambiguity**: Claim 6 (importing from external repositories with
   customizations like engine selection) may overlap with `create-agentic-agent` from
   `docs-ghaw-agentic-authoring.md` Claim 3 or with `gh aw add` synchronization. The
   exact mechanics of the agent-mediated import described here are not specified in
   sufficient detail to resolve this question from the fetched content.

6. **No contradictions to file**: Reviewed all existing source notes referenced by the
   Prospector and related corpus notes. No claims in this source materially oppose
   existing notes. The addition of new installation paths and a natural language debugging
   input mode adds specificity without contradicting prior documentation.
