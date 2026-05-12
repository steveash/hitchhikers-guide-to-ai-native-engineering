---
source_url: https://github.github.com/gh-aw/reference/workflow-structure
source_type: docs
title: "GitHub Agentic Workflows: Workflow Structure Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#419"
---

# GitHub Agentic Workflows: Workflow Structure Reference

> The authoritative reference specification for gh-aw workflow file anatomy —
> documents the concrete minimal workflow example (with `on:` and `tools:` frontmatter
> fields), the critical runtime/compile-time editability boundary (markdown body editable
> on GitHub.com without recompile; only frontmatter changes require recompile), the
> lock file header format (`gh-aw-metadata` JSON + secrets manifest + action checksums),
> inline sub-agent block syntax, and the naming/commit conventions that make compiled
> workflows auditable.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/workflow-structure` page
  — in the "Reference" section of the documentation. Reference pages document the
  workflow file format authoritatively, as distinguished from the conceptual
  `introduction/` pages and practitioner `guides/`. This page is the schema-level
  specification the conceptual overview in `docs-ghaw-how-they-work.md` points toward.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  File naming conventions, lock file header format, and frontmatter field names
  are authoritative for the `gh aw` platform. Claims do not generalize automatically
  to other agentic CI systems.
- **Scope**: The concrete structure of a gh-aw workflow file — the two-component
  anatomy (YAML frontmatter + markdown body), the `.github/workflows/` file
  organization convention, lock file header format and machine-readable metadata,
  the runtime/compile-time editability boundary, inline sub-agent block syntax, and
  best practices for file naming and version control. Does NOT cover: the full
  frontmatter schema in detail (see `docs-ghaw-permissions-reference.md`,
  `docs-ghaw-tools-reference.md`, `docs-ghaw-sandbox-reference.md`), the compilation
  pipeline internals (see `docs-ghaw-compilation-process.md`), safe outputs
  configuration (see `docs-ghaw-safe-outputs-specification.md`), or inline sub-agent
  frontmatter fields and constraints (see `docs-ghaw-inline-sub-agents.md`).

## Extracted Claims

### Claim 1: The minimal viable workflow consists of `on:` (trigger events) and `tools:` (capability binding) in YAML frontmatter, with a natural language markdown body for agent instructions

- **Evidence**: A concrete code example on the reference page shows the complete
  minimal structure: frontmatter with `on: issues: types: [opened]` and `tools:
  github: toolsets: [issues]`, followed by a markdown instruction reading the issue
  by number and adding a comment.
- **Confidence**: settled (first-party reference documentation; this is the canonical
  minimal example from the official spec page)
- **Quote**: "Each workflow consists of: (1) YAML Frontmatter: Configuration options
  wrapped in `---`. (2) Markdown: Natural language instructions for the AI."
- **Our assessment**: The minimal example makes the two-component structure concrete
  in a way the conceptual overview does not. The `on:` key maps to GitHub Actions
  event syntax directly (same as traditional `.github/workflows/*.yml`), while
  `tools:` is a gh-aw-specific binding that declares which GitHub API toolsets the
  agent may access. The example shows event-driven triggering and capability-scoped
  tool access as the two canonical frontmatter responsibilities. For Ch02 (Harness
  Engineering): the `on:` + `tools:` scaffold is the minimal harness skeleton — any
  workflow that triggers on a GitHub event and needs to read/write GitHub objects
  will start from this pattern.

### Claim 2: The markdown body is loaded at runtime and can be edited directly on GitHub.com without recompilation — only frontmatter changes require running `gh aw compile`

- **Evidence**: The page states the editability rule in a dedicated "Editing
  Workflows" section, explicitly drawing the boundary between what requires
  recompilation and what does not.
- **Confidence**: settled (first-party reference documentation; this is an explicit
  platform behavior, not an opinion)
- **Quote**: "The markdown body is loaded at runtime and can be edited directly on
  GitHub.com without recompilation. Only frontmatter changes require recompilation."
- **Our assessment**: This is one of the most operationally significant properties
  of the gh-aw format. The separation of compile-time constraints (frontmatter) from
  runtime instructions (markdown) means that practitioners can iterate on agent
  prompts — rewording instructions, adding examples, adjusting tone — without
  touching the compiled `.lock.yml`. Only structural changes (adding a trigger,
  changing permissions, adding a tool) require the `gh aw compile` cycle. This
  dramatically lowers the iteration cost for prompt engineering within an existing
  workflow. For Ch02: emphasize that the "edit on GitHub.com" path is safe and
  intended for markdown-only changes, and that the compile cycle is reserved for
  frontmatter changes that alter the security boundary. This is the natural boundary
  between content owners (who can edit markdown) and security reviewers (who must
  approve frontmatter and recompile).

### Claim 3: Compiled lock files begin with a machine-readable `gh-aw-metadata` JSON header encoding `schema_version`, `frontmatter_hash`, `strict` mode, and `agent_id`, followed by sections documenting secrets used and custom actions with version checksums

- **Evidence**: The lock file header example on the page shows the exact format:
  `# gh-aw-metadata: {"schema_version":"v3","frontmatter_hash":"...","strict":true,"agent_id":"copilot"}`
  followed by sections for "Secrets used" (e.g., COPILOT_GITHUB_TOKEN, GITHUB_TOKEN)
  and "Custom actions used" with version tags and commit SHA checksums.
- **Confidence**: settled (first-party reference documentation; the header format is
  the authoritative specification)
- **Quote**: "# gh-aw-metadata: {\"schema_version\":\"v3\",\"frontmatter_hash\":\"...\",\"strict\":true,\"agent_id\":\"copilot\"}"
- **Our assessment**: The lock file header serves as a machine-readable manifest that
  enables reliable parsing by external tooling. Three elements are notable:
  (1) `frontmatter_hash` — a cryptographic link between the compiled artifact and
  the exact frontmatter that produced it, enabling tamper detection; if the `.md`
  frontmatter is modified without recompiling, the hash will not match the compiled
  lock. (2) `strict: true` — a compilation mode flag indicating that the lock file
  enforces all validated constraints. (3) The secrets manifest — documenting which
  tokens the workflow requires makes it auditable by security teams without reading
  all the workflow logic. This corroborates `blog-ghaw-weekly-2026-03-23.md`
  Claim 7 (gh-aw-metadata v3 embedding agent ID and model), which was described
  from a changelog perspective; this reference page documents the same format as
  the authoritative specification. For Ch02: the lock file header is not just a
  generated artifact — it is an audit manifest. Teams operating gh-aw workflows can
  parse it to verify which agent ID, model, and secrets a given compiled workflow
  uses without executing it.

### Claim 4: The `frontmatter_hash` in the lock file header is a cryptographic integrity mechanism linking the compiled artifact to the exact frontmatter configuration it was generated from

- **Evidence**: The lock file header example shows `"frontmatter_hash":"..."` as a
  field in the `gh-aw-metadata` JSON. The page describes the lock file as enabling
  "reliable parsing" — the hash makes it possible to detect whether frontmatter was
  modified after compilation without rerunning the compiler.
- **Confidence**: emerging (the hash field is documented; the exact hashing algorithm
  and tamper-detection behavior are not specified on this reference page)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `frontmatter_hash` bridges the two-file model to integrity
  verification: if an adversary modifies the `.md` frontmatter to change permissions
  or toolsets without recompiling, the hash in the existing `.lock.yml` will not match.
  This is the compile-time validation layer of the five-layer security model described
  in `docs-ghaw-how-they-work.md` Claim 3. In practice, the integrity check
  complements the `strict: true` flag — together they enforce that the lock file was
  generated from the exact frontmatter that the hash encodes. For Ch03 (Safety and
  Verification): recommend that CI pipelines validate `frontmatter_hash` against the
  current `.md` frontmatter as a supply-chain integrity check on the lock file.

### Claim 5: Workflow files are stored in `.github/workflows/` as `<name>.md` and compile to `<name>.lock.yml` in the same directory — both files should be committed for transparency

- **Evidence**: The page shows the canonical file tree:
  `.github/└── workflows/  ├── ci-doctor.md # Agentic Workflow  └── ci-doctor.lock.yml # Compiled GitHub Actions Workflow`
  Best practices state: commit source `.md` files and commit generated `.lock.yml`
  files for transparency.
- **Confidence**: settled (first-party; the directory and naming convention are
  explicitly shown as the canonical organization)
- **Quote**: "Always commit `.md` files" and ".lock.yml files for transparency"
- **Our assessment**: The side-by-side commit requirement is architecturally important:
  the `.md` is what humans read and review; the `.lock.yml` is what GitHub Actions
  executes. Committing both creates an auditable trail where any difference between
  the compiled artifact and the source (detectable via `frontmatter_hash` — Claim 4)
  is visible in git history. The "for transparency" rationale means reviewers can see
  both what the agent is instructed to do (markdown) and exactly what GitHub Actions
  will execute (YAML). For Ch02: the commit-both-files practice is a harness
  engineering discipline recommendation — it is not optional if auditability is a
  requirement.

### Claim 6: Workflow filenames should follow kebab-case naming with descriptive names reflecting function (e.g., `issue-responder.md`, `pr-reviewer.md`, `weekly-summary.md`), with no spaces or special characters

- **Evidence**: The best practices section on the page explicitly names the naming
  convention and provides three concrete examples. "Avoid spaces and special
  characters" is listed as a distinct best practice.
- **Confidence**: settled (first-party; the examples and prohibition are explicit)
- **Quote**: (no single verbatim quote captures the full convention; the examples
  appear as a bullet list — see Concrete Artifacts)
- **Our assessment**: Kebab-case naming mirrors the GitHub Actions convention for
  workflow file names, keeping gh-aw source files consistent with their compiled
  counterparts. The function-descriptive naming pattern (`issue-responder`,
  `pr-reviewer`) also makes the agent factory's workflow inventory self-documenting
  — a directory listing of `.github/workflows/*.md` is a readable manifest of what
  agents exist in a repository. For Ch02: adopt the kebab-case naming convention
  as a harness engineering standard. The compiled file inherits the same name
  (`issue-responder.lock.yml`), so the naming choice propagates to the GitHub Actions
  workflow list visible in the repository's Actions tab.

### Claim 7: Inline sub-agent blocks begin with `## agent: \`name\`` headings and are extracted at runtime to `.agents/agents/.agent.md` files

- **Evidence**: The page describes inline sub-agent blocks in a dedicated section,
  showing a concrete example with `## agent: \`file-summarizer\`` syntax,
  frontmatter specifying `model: claude-haiku-4.5` and `description:`, and natural
  language body text. The extraction destination is documented as `.agents/agents/`
  at runtime.
- **Confidence**: settled (first-party; this is a reference page description of the
  syntax and runtime behavior)
- **Quote**: "extracted at runtime to `.agents/agents/.agent.md`."
- **Our assessment**: This page provides the brief reference description of inline
  sub-agents; `docs-ghaw-inline-sub-agents.md` provides the full specification
  including constraints (no `engine` field, only `model` and `description` frontmatter
  fields, Copilot-engine restriction). The reference/workflow-structure page is the
  structural context — inline sub-agent blocks are part of the workflow file structure,
  defined after the main body. The runtime extraction mechanism means the workflow file
  is the source of truth for both the main workflow and any sub-agents it defines. For
  Ch02: readers should be directed to `docs-ghaw-inline-sub-agents.md` for the full
  sub-agent specification; this page establishes only that they exist and where they
  appear in the file structure.

## Concrete Artifacts

### Minimal Workflow Example (from source)

```markdown
---
on:
  issues:
    types: [opened]
tools:
  github:
    toolsets: [issues]
---
# Workflow Description
Read the issue #${{ github.event.issue.number }}. Add a comment to the issue listing useful resources and links.
```

*Source: reference/workflow-structure page, main code example*

### File Organization (from source)

```
.github/
└── workflows/
    ├── ci-doctor.md          # Agentic Workflow (source, edited by humans)
    └── ci-doctor.lock.yml    # Compiled GitHub Actions Workflow (generated by gh aw compile)
```

*Source: reference/workflow-structure, "File Organization" section*

### Lock File Header Format (from source)

```
# gh-aw-metadata: {"schema_version":"v3","frontmatter_hash":"...","strict":true,"agent_id":"copilot"}
#    ___ ...
# This file was automatically generated by gh-aw. DO NOT EDIT.
# ...
# Secrets used:
#   - COPILOT_GITHUB_TOKEN
#   - GITHUB_TOKEN
#
# Custom actions used:
#   - actions/checkout@de0fac2e... # v6.0.2
#   - actions/upload-artifact@bbbca2... # v4
```

*Source: reference/workflow-structure, "Lock File Header" section*

### Lock File Metadata Fields

```
schema_version  — schema version identifier (current: "v3")
frontmatter_hash — cryptographic hash of the frontmatter that produced this lock file
strict          — boolean; when true, enforces all validated constraints
agent_id        — AI agent identifier (e.g., "copilot")
```

*Source: reference/workflow-structure, "Lock File Header" section (field list derived from metadata JSON example)*

### Inline Sub-Agent Block Example (from source)

```markdown
## agent: `file-summarizer`
---
model: claude-haiku-4.5
description: Summarizes a file in a few sentences
---
You are a file summarization assistant. Return a brief summary of the given file.
```

*Source: reference/workflow-structure, "Inline Sub-Agent Blocks" section*

### Best Practices Summary

```
Naming:
  - Use descriptive, kebab-case names: issue-responder.md, pr-reviewer.md, weekly-summary.md
  - Avoid spaces and special characters

Version control:
  - Always commit .md files (the editable source of truth)
  - Always commit .lock.yml files (for transparency and auditability)

Compilation trigger:
  - Markdown-only edits: no recompilation needed (edit directly on GitHub.com)
  - Frontmatter changes: always recompile with gh aw compile
```

*Source: reference/workflow-structure, "Best Practices" and "Editing Workflows" sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 1 ("The two-component workflow structure
    (YAML frontmatter + natural language markdown) enables reliable, secure agentic
    programming via capability sandboxing"): This reference page is the concrete
    schema-level specification that the conceptual note describes. The `on:` +
    `tools:` minimal example here makes Claim 1 concrete.
  - `docs-ghaw-how-they-work.md` Claim 7 ("The compilation model separates the
    editable workflow source (`.md`) from the hardened executable (`.lock.yml`)
    produced by `gh aw compile`"): The file organization diagram and commit-both
    convention here corroborate that claim with the canonical reference description.
  - `blog-ghaw-weekly-2026-03-23.md` Claim 7 ("Lock files can now embed the
    configured agent ID and model for reproducibility and auditability"): The lock
    file header format described here (with `agent_id` in `gh-aw-metadata v3`) is
    the reference specification that Claim 7 in the weekly note described from a
    changelog perspective. This reference page is the authoritative definition of
    the v3 metadata format.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 1 (the `gh aw compile` five-phase
    pipeline): This reference page documents what the compiled artifact looks like
    from the author's perspective (the lock file header format, the file naming
    convention). The compilation process note documents how the artifact is produced
    internally. Together they give the complete picture: this reference page shows
    the inputs and outputs a practitioner works with; that note shows the phases
    that transform one into the other.
  - `docs-ghaw-inline-sub-agents.md` Claim 1 ("An inline sub-agent is a named
    agent definition embedded directly in a workflow markdown file"): This reference
    page provides the brief structural mention (placement in the file, runtime
    extraction destination); the inline sub-agents note provides the full
    specification of frontmatter fields, engine constraints, and invocation.
  - `docs-ghaw-permissions-reference.md` Claim 1 (read-only permissions model in
    `permissions:` frontmatter): The minimal workflow example on this page omits
    `permissions:` and `safe-outputs:` for simplicity. The permissions reference
    note extends this skeleton with the full permission configuration.

- **Contradicts**: None identified. The runtime/compile-time editability boundary
  (Claim 2) and lock file header format (Claim 3) are new to the corpus and do not
  conflict with any existing source notes. The file organization and naming
  conventions are consistent with all prior gh-aw documentation notes. No
  contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Lock file header anatomy as an audit manifest** (Claim 3): The full
    `gh-aw-metadata` JSON header format (four named fields), the secrets manifest
    section, and the action checksum section are not documented in any existing
    source note. The weekly note (`blog-ghaw-weekly-2026-03-23.md` Claim 7) mentioned
    v3 metadata in a changelog context; this is the first corpus note documenting
    it as a reference specification.
  - **`frontmatter_hash` as a cryptographic integrity mechanism** (Claim 4): No
    existing source note identifies the `frontmatter_hash` field or its role in
    tamper detection. The compilation process note documents SHA pinning for
    actions; this is the parallel integrity mechanism for frontmatter.
  - **Runtime/compile-time editability boundary as an operational rule** (Claim 2):
    The specific rule — "markdown body editable on GitHub.com without recompile;
    only frontmatter changes require recompile" — is not stated in any existing
    source note. `docs-ghaw-how-they-work.md` describes the two components but does
    not state this operational distinction explicitly.
  - **Minimal `on:` + `tools:` frontmatter scaffold** (Claim 1): A concrete
    working example with specific field names is not provided in any existing corpus
    note. `docs-ghaw-how-they-work.md` describes frontmatter generically; this page
    provides the minimal concrete example.
  - **File naming conventions** (Claim 6): The kebab-case naming requirement with
    specific examples (`issue-responder.md`, `pr-reviewer.md`, `weekly-summary.md`)
    is not documented in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the `on:` + `tools:` scaffold as the canonical minimal workflow skeleton**
  (Claim 1, Concrete Artifacts): The guide should provide the minimal viable workflow
  example from this reference page as the starting template for Ch02's harness design
  section. Pair with `docs-ghaw-permissions-reference.md` Claim 1 to add the
  `permissions:` + `safe-outputs:` pattern once the agent needs to write state.

- **Document the runtime/compile-time editability boundary** (Claim 2): Add as an
  explicit operational rule: "markdown body — edit on GitHub.com anytime; frontmatter
  — always recompile." This boundary determines which workflow changes require a
  security review cycle (frontmatter changes, which alter the sandbox) vs. which
  can be iterated freely (prompt/instruction changes in the markdown body). This
  is directly relevant to team workflows: content owners and security reviewers
  have different approval requirements for different parts of the file.

- **Add kebab-case naming as a harness engineering standard** (Claim 6): The naming
  convention has practical consequences — the compiled `.lock.yml` inherits the name,
  and the Actions tab shows workflow names derived from file names. Descriptive
  function-based names make agent factories self-documenting.

- **Add the commit-both-files discipline** (Claim 5): The guide should recommend
  committing both `.md` and `.lock.yml` as a discipline analogous to committing
  both source and generated lock files in dependency management. Cite the
  "transparency" rationale from this reference page.

### Chapter 03: Safety and Verification

- **Add `frontmatter_hash` verification as a supply-chain integrity check** (Claim 4):
  The guide should recommend that CI pipelines validate the `frontmatter_hash` in
  `.lock.yml` against the current `.md` frontmatter as a defense against unauthorized
  frontmatter modification without recompilation. This extends the five-layer security
  model from `docs-ghaw-how-they-work.md` Claim 3 with a concrete verification step.

- **Add the lock file header as an audit manifest** (Claim 3): The secrets and action
  checksum sections of the lock file header are first-class security artifacts. Security
  reviewers auditing a workflow can read the header to see exactly which tokens are
  required and which external actions (with which SHAs) are used — without executing
  the workflow. Add this to Ch03's observability and audit section.

### Chapter 06: Observability

- **Add lock file header parsing as a workflow inventory tool** (Claim 3): The
  machine-readable `gh-aw-metadata` format enables automated tooling that reads lock
  file headers across a repository (or organization) to build a workflow inventory:
  which workflows use which agent IDs, which secrets, which external actions. This
  is a form of static observability — understanding the agent factory's configuration
  without running it.

## Extraction Notes

1. **Source is brief but authoritative**: The reference/workflow-structure page is
   relatively concise — it provides the structural overview and canonical examples
   without deep explanations. Deeper explanations live in companion reference pages
   (permissions, tools, sandbox, safe-outputs) and in the conceptual introduction
   pages. The note accurately reflects the brevity of the source while extracting
   all substantive claims.

2. **WebFetch returned summaries across three fetches**: The page is rendered by an
   Astro/Starlight SPA. Three separate WebFetch calls were made with different
   prompts to maximize extraction coverage. The lock file header format and inline
   sub-agent example were captured from the third fetch. All quoted text appears
   verbatim in at least one fetch response; no quotes were reconstructed.

3. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   gh-aw-metadata v3, which shipped in v0.62.3 (from `blog-ghaw-weekly-2026-03-23.md`
   Claim 7).

4. **Inline sub-agents — not deep-extracted**: The `## agent:` block syntax is noted
   here as structural context. Full sub-agent specification is in
   `docs-ghaw-inline-sub-agents.md`; this note does not duplicate that extraction.

5. **No contradictions filed**: Reviewed all relevant existing source notes. No claims
   here oppose existing notes. The runtime/compile-time editability rule and lock file
   header format are new to the corpus, not contradictions of existing claims.
