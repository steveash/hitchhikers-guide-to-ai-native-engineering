---
source_url: https://github.github.com/gh-aw/guides/agentic-authoring
source_type: docs
title: "GitHub Agentic Workflows: Agentic Authoring"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-04-21
last_checked: 2026-04-21
status: current
confidence_overall: emerging
issue: "#293"
---

# GitHub Agentic Workflows: Agentic Authoring

> Practitioner-facing authoring lifecycle guide for gh-aw — covers the four
> concrete activities absent from existing notes: repository initialization via
> a self-contained `install.md` prompt, AI-assisted cross-repo workflow migration
> (`create-agentic-agent`), Copilot-native debugging via `/agent agentic-workflows
> debug <run-url>`, and the generalizable meta-pattern of URL-addressable
> self-contained prompt files that any AI assistant can fetch and execute.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guide page, "Guides > Agentic
  Authoring" — practitioner how-to for the authoring lifecycle, not API reference
  or conceptual overview)
- **Author credibility**: First-party from GitHub Next / Microsoft Research (the same
  team behind the "Peli's Agent Factory" blog series and `docs-ghaw-how-they-work.md`).
  This page documents the authoring UX of a production platform the team operates
  internally. Claims about CLI commands, agent behaviors, and prompt patterns are
  first-party and production-verified. Claims about generalizability beyond gh-aw
  are interpretive.
- **Scope**: The authoring lifecycle — initialization, web-UI creation, cross-repo
  migration, debugging, and auxiliary prompt patterns (Planner, Dictation). Does NOT
  cover: the compilation model (in `docs-ghaw-how-they-work.md`), the security
  architecture (same), specific workflow examples (in the blog series), or cost
  benchmarking. This page is the "how to author"; the "how they work" page is the
  "how they execute."

## Extracted Claims

### Claim 1: `gh aw init` bootstraps a repository for agentic authoring by fetching and executing a self-contained `install.md` prompt

- **Evidence**: The page describes two equivalent initialization paths: (1) running
  the `gh aw init` CLI command, or (2) pasting the prompt "Initialize this repository
  for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/install.md"
  into any AI assistant. Both routes produce the same result: the repository is
  configured with the files needed for the agentic authoring experience. After init,
  the user commits and pushes the created files.
- **Confidence**: settled (first-party documentation; CLI command exists and is
  version-tracked at `github.github.com/gh-aw`)
- **Quote**: "In order to enable the agentic authoring experience, you will need to
  configure your repository with a few files. Run this prompt or the init command."
- **Our assessment**: The key architectural detail is that `gh aw init` and the
  `install.md` prompt are equivalent — the CLI is a convenience wrapper around a
  prompt-driven initialization. This means the init protocol is AI-assistant-agnostic:
  a practitioner without the `gh aw` CLI can still bootstrap a repository by sharing
  the `install.md` URL with any coding agent. For Ch02 (Harness Engineering): `gh aw
  init` is the zero-to-harness entry point; it should precede the compile → watch →
  run loop documented in `docs-ghaw-how-they-work.md` Claim 11.

### Claim 2: On first run in a new repository, the authoring agent detects missing secrets and opens an issue with setup instructions — turning a configuration failure into a guided onboarding step

- **Evidence**: Documented in a Tip callout on the page: "On the first run in a new
  repository, the workflow will surely fail because the secrets are not configured.
  The agentic workflow should detect the missing tokens and create an issue with
  instructions on how to configure them."
- **Confidence**: emerging (stated in first-party documentation; behavior is
  "should detect," not a hard guarantee)
- **Quote**: "The agentic workflow should detect the missing tokens and create an
  issue with instructions on how to configure them."
- **Our assessment**: This is an example of graceful failure-as-onboarding: instead
  of producing an opaque error message, the agent converts a configuration failure
  into a structured, actionable issue that guides the user to resolution. The pattern
  is more broadly applicable — any agentic workflow can be designed to detect
  first-run precondition failures and open setup-guidance issues rather than silently
  failing or producing cryptic logs. For Ch02: worth naming as a harness design
  pattern for first-run UX. For Ch03: relates to the "critical actions require human
  approval" model — here, the agent's first "action" on a mis-configured repo is
  to escalate to the human via an issue rather than attempting to proceed.

### Claim 3: `create-agentic-agent` performs AI-assisted one-time cross-repo workflow migration, distinct from `gh aw add` which provides ongoing synchronized reuse

- **Evidence**: The page explicitly distinguishes two patterns:
  - `create-agentic-agent`: "AI-assisted migration. The agent analyzes the source
    workflow, identifies dependencies, adapts configuration for your repository, and
    validates the result. This is useful for forking workflows as starting points or
    one-time migrations requiring substantial changes."
  - `gh aw add` (via "Reusing Workflows"): for "synchronized updates across
    repositories."
  The page gives an example migration prompt: "Migrate the release.md workflow from
  github/gh-aw to this repository. Adapt permissions and repository-specific
  references for our structure."
- **Confidence**: settled (first-party; the two mechanisms are explicitly named and
  distinguished)
- **Quote**: "This is useful for forking workflows as starting points or one-time
  migrations requiring substantial changes. For synchronized updates across
  repositories, use Reusing Workflows with `gh aw add` instead."
- **Our assessment**: The migration vs. synchronization distinction is important
  for workflow lifecycle management. `gh aw add` is like a package dependency — the
  workflow stays in sync with the upstream version. `create-agentic-agent` is like
  a fork — the agent adapts the workflow once, and the adopting repo owns it from
  that point. The choice depends on whether the team wants to track upstream changes
  (use `gh aw add`) or needs substantial customization that would conflict with
  upstream updates (use `create-agentic-agent`). For Ch02 (Harness Engineering):
  add this as a workflow reuse decision: "Will you track upstream? Use `gh aw add`.
  Are you forking as a starting point? Use `create-agentic-agent`." Extends Claim 4
  in `blog-gh-aw-operations-release-workflows.md` (the `gh aw add-wizard` install
  pattern), which covers only the synchronization path.

### Claim 4: The GitHub Web Interface enables non-interactive workflow creation via Copilot, useful for quickly turning an idea into a working workflow without a local coding agent

- **Evidence**: The page states: "If you have access to GitHub Copilot, you can
  create and edit Agentic Workflows directly from the web interface. While
  non-interactive, it's useful for quickly turning an idea into a working workflow."
  A video demonstration is embedded (not extractable via WebFetch) showing web-based
  workflow creation.
- **Confidence**: settled (first-party; feature is live for Copilot subscribers)
- **Quote**: "While non-interactive, it's useful for quickly turning an idea into a
  working workflow."
- **Our assessment**: The web interface is a low-friction entry point — no CLI, no
  local dev environment. The trade-off is interactivity: it creates a workflow in
  one shot, but lacks the conversational back-and-forth of a local coding agent.
  For Ch05 (Team Adoption): this is a relevant adoption path for teams who want to
  trial gh-aw without committing to CLI setup. The "non-interactive" caveat is worth
  surfacing — it works well for simple workflows but may fall short for workflows
  requiring iterative refinement of the agent's instructions.

### Claim 5: `/agent agentic-workflows debug <run-url>` is a Copilot-native command that diagnoses failing workflow runs by identifying root cause (missing tools, permission errors, network blocks) and suggesting targeted fixes

- **Evidence**: Documented directly: "If your repository is configured for agentic
  authoring, use the agentic-workflows agent in Copilot Chat: `/agent
  agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID`. The
  agent audits the run, identifies the root cause (missing tools, permission errors,
  network blocks), and suggests targeted fixes."
- **Confidence**: settled (first-party; the command format and root cause categories
  are explicitly stated)
- **Quote**: "The agent audits the run, identifies the root cause (missing tools,
  permission errors, network blocks), and suggests targeted fixes."
- **Our assessment**: This is a meta-level agent capability: an agent debugging
  another agent's execution. The three named root cause categories (missing tools,
  permission errors, network blocks) are diagnostic primitives for the five-layer
  security architecture in `docs-ghaw-how-they-work.md` — each category maps to a
  specific security layer (Layer 1: tool allowlists, Layer 3: permission separation,
  Layer 4: network controls). For Ch01 (Daily Workflows): document this command as
  the primary debugging tool for gh-aw practitioners. For Ch02: the named root cause
  categories (tools, permissions, network) are a useful diagnostic framework for any
  agentic harness — not just gh-aw.

### Claim 6: `debug.md` is a self-contained, URL-addressable prompt that any AI assistant can fetch to diagnose and fix a failing workflow run — no Copilot subscription required

- **Evidence**: The page documents two debugging paths — Copilot Chat (Claim 5) and
  the self-contained URL path: "For any AI assistant or coding agent, share the URL
  to the standalone debugging prompt: `Debug this workflow run using
  https://raw.githubusercontent.com/github/gh-aw/main/debug.md`." The page explains
  the behavior: "The `debug.md` file is a self-contained prompt. The agent fetches
  it and follows the instructions to install the `gh aw` CLI, analyze logs, apply
  fixes, and open a pull request with the changes."
- **Confidence**: settled (first-party; `debug.md` exists at the documented URL and
  the behavior is explicitly described)
- **Quote**: "The `debug.md` file is a self-contained prompt. The agent fetches it
  and follows the instructions to install the `gh aw` CLI, analyze logs, apply fixes,
  and open a pull request with the changes."
- **Our assessment**: This is the most generalizable finding in the source. The
  pattern — a plain text file hosted at a public URL that functions as a complete,
  self-executing prompt — decouples agent instructions from any specific AI assistant.
  A practitioner can share the URL with Claude, GPT-4, a local Ollama model, or any
  other assistant, and the assistant will fetch and follow the instructions without
  any platform-specific configuration. The prompt IS the interface. This is a
  portable harness design pattern: instead of encoding agent instructions in a
  platform-specific format (Copilot instructions, OpenAI system prompt, etc.), encode
  them in a URL-addressable markdown file. For Ch02 (Harness Engineering): name this
  as the "URL-addressable prompt" pattern — a technique for distributing agent
  instructions that are AI-assistant-agnostic and human-readable.

### Claim 7: The URL-addressable self-contained prompt pattern generalizes beyond debugging — `install.md` follows the same pattern for repository initialization

- **Evidence**: Claim 1 documents the init path: "Initialize this repository for
  GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/install.md
  or `gh aw init`." This establishes that gh-aw uses the URL-addressable prompt
  pattern for at least two distinct lifecycle operations: initialization (`install.md`)
  and debugging (`debug.md`). The CLI commands (`gh aw init`, `/agent agentic-workflows
  debug`) are thin wrappers that invoke the same underlying self-contained prompts.
- **Confidence**: emerging (both URLs are documented; the generalization — that this
  is a deliberate design pattern — is interpretive)
- **Quote**: (implicit in the parallel structure of both init and debug paths)
- **Our assessment**: The fact that gh-aw uses URL-addressable prompts for both
  initialization and debugging suggests a deliberate architectural choice: the
  team distributes agent behavior as fetchable text files, not as platform-specific
  configurations. This makes the prompts versionable (they live in the gh-aw git
  repo), auditable (anyone can read them), and portable (any AI assistant can use
  them). Teams building their own agentic toolchains can adopt this pattern: host
  key prompts (CLAUDE.md, debugging guides, onboarding checklists) at stable URLs
  and reference them by URL rather than by copy-pasting into system prompts. For
  Ch02: this is a harness distribution and versioning technique worth naming.

### Claim 8: The `agentic-chat` Planner produces "what, not how" task specifications wrapped in 5 backticks, optimized for consumption by coding agents rather than human readers

- **Evidence**: "Copy the instructions, paste into your AI chat, then describe your
  workflow goal. The assistant asks clarifying questions and generates a structured
  task description (wrapped in 5 backticks) ready to use in your workflow. It focuses
  on what needs to be done rather than how, making it ideal for creating specifications
  that coding agents can execute."
- **Confidence**: anecdotal (the 5-backtick convention and "what not how" framing are
  documented; whether this produces better downstream agent performance is not measured)
- **Quote**: "It focuses on what needs to be done rather than how, making it ideal
  for creating specifications that coding agents can execute."
- **Our assessment**: The Planner is a prompt-engineering intermediary: it converts
  a casual human description of a goal into a structured, agent-optimized task
  specification. The "what, not how" framing aligns with how AGENTS.md-style harness
  prompts work — the agent is given the goal and constraints, not the implementation
  steps. The 5-backtick convention is a practical artifact: it makes the task
  description visually delimited and parseable by the workflow's natural language
  instruction section. For Ch02: the "what, not how" principle is worth naming in
  the context of writing workflow instruction sections — the agent decides how to
  accomplish a task; the instruction specifies the desired outcome and constraints.

### Claim 9: Dictation instructions serve as a terminology correction and formalization pre-processing layer between speech-to-text output and workflow authoring

- **Evidence**: "When creating agentic workflows using speech-to-text, use the
  dictation instructions prompt to correct terminology mismatches and formatting
  issues. This prompt corrects terminology (e.g., 'ghaw' → 'gh-aw', 'work flow' →
  'workflow'), transforms casual speech into imperative task descriptions, removes
  filler words, and adds implicit context."
- **Confidence**: anecdotal (documented functionality; effectiveness not measured)
- **Quote**: "corrects terminology (e.g., 'ghaw' → 'gh-aw', 'work flow' →
  'workflow'), transforms casual speech into imperative task descriptions, removes
  filler words, and adds implicit context"
- **Our assessment**: Dictation instructions are the thinnest and most specialized
  finding in this source — a prompt-engineering utility for practitioners who
  dictate workflow specifications via speech-to-text. The generalizable principle is
  narrower than it appears: vocabulary correction and formalization is a recurring
  pre-processing need when AI-generated or voice-generated text feeds into structured
  authoring contexts. For Ch02: mention as an auxiliary pattern for practitioners
  using voice interfaces; not a first-class guide finding.

## Concrete Artifacts

### Repository Initialization — Two Equivalent Paths

```bash
# Path 1: CLI command
gh aw init

# Path 2: Self-contained prompt (works with any AI assistant)
# Paste into Copilot Chat, Claude, or any coding agent:
"Initialize this repository for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/install.md"

# After initialization, commit and push the created files
git add .github/ && git commit -m "chore: initialize gh-aw authoring agent" && git push
```

*Source: Agentic Authoring guide, "Configuring Your Repository" section*

### Cross-Repo Migration vs. Synchronized Reuse

```
Migration (one-time, with adaptation):
  Tool:    create-agentic-agent
  When:    Forking a workflow as a starting point OR one-time migration with
           substantial customization needed
  Example: "Migrate the release.md workflow from github/gh-aw to this repository.
            Adapt permissions and repository-specific references for our structure."
  Result:  Adopting repo OWNS the workflow; it diverges from upstream

Synchronized reuse (ongoing, tracked):
  Tool:    gh aw add  (previously: gh aw add-wizard for initial install)
  When:    You want to track and receive updates from the upstream workflow
  Result:  Adopting repo stays in sync with upstream version changes
```

*Source: Agentic Authoring guide, "Remixing Workflows Between Repositories" section*

### Debugging — Two Paths

```bash
# Path 1: Via Copilot Chat (requires repository configured for agentic authoring)
/agent agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID

# The agent:
# - Audits the run
# - Identifies root cause: missing tools | permission errors | network blocks
# - Suggests targeted fixes

# Path 2: Self-contained prompt URL (any AI assistant, no Copilot required)
"Debug this workflow run using https://raw.githubusercontent.com/github/gh-aw/main/debug.md
The failed workflow run is at https://github.com/OWNER/REPO/actions/runs/RUN_ID"

# The agent fetches debug.md and follows its instructions to:
# - Install the gh aw CLI
# - Analyze logs
# - Apply fixes
# - Open a pull request with the changes
```

*Source: Agentic Authoring guide, "Debugging Workflows" section*

### URL-Addressable Self-Contained Prompt Pattern (Generalizable)

```
Pattern: URL-Addressable Self-Contained Prompts

Principle: Host agent instructions as plain-text markdown files at stable,
           public URLs. Reference by URL rather than by copy-paste.

Examples in gh-aw:
  install.md  → https://raw.githubusercontent.com/github/gh-aw/main/install.md
                 (bootstraps a new repository for agentic authoring)
  debug.md    → https://raw.githubusercontent.com/github/gh-aw/main/debug.md
                 (diagnoses and fixes failing workflow runs)

Properties:
  - Versionable: lives in git; can be pinned to a tag or SHA
  - Auditable: anyone can read the prompt at the URL
  - AI-assistant-agnostic: works with Copilot, Claude, GPT-4, local models, etc.
  - CLI-equivalent: gh aw init == "fetch install.md and follow it"
  - Complete: the prompt includes all setup steps (CLI install, auth, analysis)

Usage:
  "Do X using https://raw.githubusercontent.com/OWNER/REPO/main/PROMPT.md"
```

*Source: Agentic Authoring guide, "Configuring Your Repository" and "Self-Contained
(with URL)" sections*

### Planner (agentic-chat) — Specification Format

```
Workflow:
  1. Copy the agentic-chat instructions from the gh-aw page
  2. Paste into any conversational AI assistant
  3. Describe your workflow goal in natural language
  4. Assistant asks clarifying questions
  5. Output: structured task description, wrapped in ``````` (5 backticks)
  6. Paste the 5-backtick block into the workflow's instruction section

Key principle: "what needs to be done, not how" — goal + constraints,
               not implementation steps. The coding agent decides how.

Example output format:
  `````
  When a new issue is opened, analyze its title and body...
  Classify it as one of: bug / feature / question / documentation...
  Apply the matching label and assign to the appropriate team member...
  `````
```

*Source: Agentic Authoring guide, "Advanced Techniques > Planner" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 11 (compile → watch → run → review as the
    recommended development loop): this note adds the missing first step — `gh aw
    init` — that precedes the compile loop. The two together give the complete
    development lifecycle: init → compile → watch → run → review.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security pipeline): the three
    root cause categories for the `/agent agentic-workflows debug` command (missing
    tools, permission errors, network blocks) map directly to Layers 1, 3, and 4 of
    the security pipeline. The debugging command is a diagnostic tool for the
    security architecture.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): Claim 2 in this note (secret detection → issue creation) is an
    instance of this escalation pattern — the agent's first action on a
    mis-configured repo is to open an issue for human resolution rather than
    attempting to proceed.

- **Extends**:
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw add-wizard` for
    installing pre-built workflows): this note adds the migration side of the
    workflow-reuse picture. That source documents `gh aw add-wizard` (synchronized
    reuse); this source documents `create-agentic-agent` (one-time migration with
    adaptation). Together they give the complete workflow reuse decision: fork vs.
    sync.
  - `docs-ghaw-how-they-work.md` Claim 11 (development workflow): this note extends
    the four-step loop with (1) the `gh aw init` prerequisite and (2) the
    `/agent agentic-workflows debug` step when runs fail.

- **Contradicts**: None identified. No existing source note makes claims that
  contradict the authoring lifecycle, migration pattern, or URL-addressable prompt
  mechanism described here. The `gh aw add` vs `create-agentic-agent` distinction
  extends Claim 4 in `blog-gh-aw-operations-release-workflows.md` without opposing it.

- **Novel**:
  - **URL-addressable self-contained prompt pattern** (Claims 6 and 7): No other
    source in the corpus documents the pattern of hosting agent instructions as
    fetchable markdown files at stable URLs that any AI assistant can execute. The
    `debug.md` and `install.md` examples are the first concrete instances of this
    pattern in the corpus.
  - **`create-agentic-agent` one-time migration** (Claim 3): The migration vs.
    synchronization distinction — fork with AI-assisted adaptation vs. tracked
    reuse — is new to the corpus. Prior notes covered only the `gh aw add` path.
  - **First-run secret detection and issue creation** (Claim 2): Graceful
    failure-as-onboarding via automated issue creation for missing secrets is not
    documented in any existing source note. This is a harness design pattern for
    first-run UX.
  - **`/agent agentic-workflows debug` root cause taxonomy** (Claim 5): The three
    named root cause categories (missing tools, permission errors, network blocks)
    as a diagnostic framework for agentic workflow failures are new to the corpus.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add `/agent agentic-workflows debug <run-url>` as a debugging workflow**: When
  a gh-aw workflow fails, the first diagnostic step is `/agent agentic-workflows
  debug <run-url>` in Copilot Chat (or `debug.md` via any AI assistant). Document
  the three root cause categories (missing tools, permission errors, network blocks)
  as a triage checklist. This closes the debugging gap in the current guide — the
  compile → watch → run loop from `docs-ghaw-how-they-work.md` Claim 11 covers
  development-time iteration, but not how to diagnose a live failure.

### Chapter 02: Harness Engineering

- **Add `gh aw init` as the repo initialization step** preceding the compile →
  watch → run → review loop. The complete development lifecycle for gh-aw is:
  init → compile → watch → run → review. Cite this note alongside
  `docs-ghaw-how-they-work.md` Claim 11.

- **Name the URL-addressable prompt pattern** (Claims 6 and 7): Introduce this as
  a harness distribution technique — host agent instructions as plain-text markdown
  at a stable URL; reference by URL rather than by inline copy. Properties: AI-
  assistant-agnostic, versionable in git, auditable, and complete (the prompt
  contains all setup steps). This is distinct from CLAUDE.md (which is repo-local)
  — URL-addressable prompts are designed for cross-repo and cross-assistant portability.

- **Document the workflow reuse decision** (Claim 3): When adopting a workflow from
  another repository, practitioners face a fork-vs-sync decision. Use
  `create-agentic-agent` for one-time migration with substantial adaptation; use
  `gh aw add` for ongoing synchronization with upstream. The guide should help
  practitioners make this choice explicitly rather than defaulting to one path.

- **First-run graceful failure pattern** (Claim 2): Add as a harness design
  recommendation: agentic workflows should detect first-run configuration failures
  (missing secrets, missing permissions) and open a setup-guidance issue rather
  than failing silently or producing cryptic logs. This converts an error into an
  onboarding step.

- **"What, not how" for instruction sections** (Claim 8): When writing the natural
  language instruction section of a workflow, specify what the agent should accomplish
  and the constraints it operates under — not how to accomplish it. The agentic-chat
  Planner formalizes this principle and can serve as a drafting aid.

## Extraction Notes

1. **Source is the authoring UX guide, not the conceptual reference**: Per Prospector
   guidance, the Miner skipped re-extraction of the security architecture, compilation
   model, and Safe Outputs patterns — those are fully documented in
   `docs-ghaw-how-they-work.md`. This note covers only the authoring lifecycle content
   that is absent from existing notes.

2. **Video content not extracted**: The "Using the GitHub Web Interface" section
   includes an embedded video demonstration of web-based workflow creation.
   WebFetch cannot extract video content. The claim (Claim 4) is documented from
   the surrounding text; visual details of the demo are not captured.

3. **`agentic-chat` and dictation instructions not fetched**: The page provides
   "Copy agentic-chat instructions" and "Copy dictation instructions" buttons that
   load the prompt text. These prompts are not directly accessible via static fetch.
   Claims 8 and 9 are based on the page's descriptions of these prompts, not on
   the prompt texts themselves.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the current gh-aw platform as of 2026-04-21.

5. **Planner and Dictation sections are thin**: Consistent with Prospector guidance
   to treat these sections as lower priority, Claims 8 and 9 are extracted but
   assessed as thinner findings. The more extractable content — init, migration,
   debugging, and the URL-addressable prompt pattern — received deeper treatment.

6. **No contradictions to file**: Reviewed all existing source notes. No claims in
   this source materially oppose existing source notes. The migration vs.
   synchronization distinction extends rather than contradicts `blog-gh-aw-
   operations-release-workflows.md` Claim 4.
