---
source_url: https://github.github.com/gh-aw/guides/editing-workflows
source_type: docs
title: "GitHub Agentic Workflows: Editing Workflows (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#435"
---

# GitHub Agentic Workflows: Editing Workflows (Guides)

> The practitioner-facing guide to the hot-edit vs. recompile boundary in
> gh-aw workflows — defines exactly which elements of the markdown body are
> freely editable at runtime, enumerates all 12 frontmatter field categories
> that require recompilation, and documents expression safety rules for
> GitHub context variables in markdown.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/editing-workflows`
  page — the "Guides" section, which provides practitioner how-to guidance as
  distinct from the "Reference" section's technical specification pages. The
  `guides/` section targets workflow authors making iterative changes to
  existing workflows, not readers learning the compilation model from scratch.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory and all gh-aw
  documentation. Claims about what requires or does not require recompilation
  are authoritative platform facts for the `gh aw` platform.
- **Scope**: The editing lifecycle for existing gh-aw workflows — what can be
  changed without recompiling (markdown body elements), what requires
  recompilation (all 12 frontmatter field categories), concrete before/after
  editing examples, and expression safety in markdown. Does NOT cover: the
  internal mechanics of what `gh aw compile` does (see
  `docs-ghaw-compilation-process.md`), the conceptual "why" of the compilation
  model (see `docs-ghaw-how-they-work.md`), creating new workflows from scratch
  (see `docs-ghaw-setup-creating-workflows.md`), or the full frontmatter field
  catalog (see `docs-ghaw-frontmatter-full-reference.md`).

## Extracted Claims

### Claim 1: The two-part workflow architecture distinguishes YAML frontmatter (compiled; recompilation required for changes) from markdown body (runtime-loaded; changes take effect immediately)

- **Evidence**: The page opens with an explicit two-part framing: "Agentic
  workflows consist of two parts: the **YAML frontmatter** (compiled into the
  lock file; changes require recompilation) and the **markdown body** (loaded
  at runtime; changes take effect immediately)." This is the practitioner's
  entry point for understanding what they can safely edit between runs.
- **Confidence**: settled (first-party documentation; this is the page's
  foundational architectural claim)
- **Quote**: "Agentic workflows consist of two parts: the **YAML frontmatter**
  (compiled into the lock file; changes require recompilation) and the
  **markdown body** (loaded at runtime; changes take effect immediately)."
- **Our assessment**: This framing is the practitioner-facing version of the
  architectural fact documented in `docs-ghaw-compilation-process.md` Claim 7
  and `docs-ghaw-how-they-work.md` Claim 7. What's distinct here is the
  emphasis on *editing consequences* — not "how does compilation work" but
  "what happens when I change this." The two-part framing gives workflow
  authors a decision rule: before editing, identify which part you are
  modifying, and you immediately know whether you need to recompile. For Ch02
  (Harness Engineering): this two-part mental model should be the first thing
  workflow authors internalize. The editing boundary is the most consequential
  daily-use property of the gh-aw compilation model.

### Claim 2: The markdown body is hot-editable without recompilation — five named element types can be freely changed between runs

- **Evidence**: The page names five hot-editable element types: "You can freely
  edit task instructions, output templates, conditional logic ('If X, then do
  Y'), context explanations, and examples." These are all natural-language
  constructs within the markdown body; none are YAML fields.
- **Confidence**: settled (first-party documentation; the list is explicitly
  enumerated)
- **Quote**: "The markdown body is loaded at runtime from the original `.md`
  file. You can freely edit task instructions, output templates, conditional
  logic ('If X, then do Y'), context explanations, and examples."
- **Our assessment**: The five-item list is more specific than prior corpus
  entries that simply say "the markdown body is editable." The categories
  cover the full range of what workflow authors typically want to change:
  what the agent does (task instructions), how it formats output (output
  templates), what decisions it makes (conditional logic), what context it
  has (context explanations), and how it learns from patterns (examples).
  Notably, conditional logic ("If X, then do Y") is listed as hot-editable —
  this means branching instruction changes do not require recompilation, only
  tool, permission, or trigger changes do. For Ch02: this list is the "safe
  to iterate" whitelist for practitioners in a rapid-feedback development loop.

### Claim 3: All YAML frontmatter changes always require recompilation because they are security-sensitive configuration options — 12 named field categories constitute the recompile boundary

- **Evidence**: The page states: "Changes to the **YAML frontmatter** always
  require recompilation. These are security-sensitive configuration options."
  It then enumerates 12 field categories that require recompilation: Triggers
  (`on:`), Permissions (`permissions:`), Tools (`tools:`), Network (`network:`),
  Safe outputs (`safe-outputs:`), MCP Scripts (`mcp-scripts:`), Runtimes
  (`runtimes:`), Imports (`imports:`), Custom jobs (`jobs:`), Engine (`engine:`),
  Timeout (`timeout-minutes:`), and Roles (`roles:`).
- **Confidence**: settled (first-party documentation; the list is explicit and
  the rationale — security-sensitive — is directly stated)
- **Quote**: "Changes to the **YAML frontmatter** always require recompilation.
  These are security-sensitive configuration options."
- **Our assessment**: The 12-field enumeration is the most complete compile-
  required field list in the corpus. Prior notes (`docs-ghaw-compilation-process.md`
  Claim 7) stated the principle ("frontmatter changes require recompilation")
  but did not name all 12 field categories. The security rationale ("security-
  sensitive configuration options") explains why there are no exceptions: any
  change to permissions, tools, network, or safe-output definitions changes the
  security posture of the workflow. Even seemingly innocuous frontmatter changes
  (e.g., a timeout adjustment) go through compilation to ensure the full security
  validation pipeline is re-run. For Ch02: practitioners should bookmark the
  12-field list as the authoritative "must recompile" checklist.

### Claim 4: The hot-edit workflow is editor-agnostic — markdown body changes can be made directly on GitHub.com without a local development environment

- **Evidence**: The page explicitly states: "You can edit the **markdown body**
  directly on GitHub.com or in any editor without recompiling. Changes take
  effect on the next workflow run."
- **Confidence**: settled (first-party documentation; the GitHub.com in-browser
  edit path is specifically named)
- **Quote**: "You can edit the **markdown body** directly on GitHub.com or in
  any editor without recompiling. Changes take effect on the next workflow run."
- **Our assessment**: The explicit mention of GitHub.com editing is significant
  for adoption: non-technical stakeholders or operators who understand the
  workflow's intent can refine agent instructions directly in the browser
  without needing a local clone, Go toolchain, or understanding of `gh aw
  compile`. This lowers the barrier to iterating on AI instructions compared
  to editing a compiled artifact. For Ch01 (Daily Workflows) and Ch05 (Team
  Adoption): the browser-edit path for instruction iteration is a feature for
  teams where the workflow author and the instruction refiner are different
  people — a PM can adjust labeling criteria for a triage agent without
  needing a developer's compile environment.

### Claim 5: Adding labeling criteria to the markdown body of an issue-triage workflow takes effect on the next run without recompilation — the canonical hot-edit example

- **Evidence**: The page's "Example: Adding Instructions" section shows a
  before/after where the workflow's markdown body gains a "## Labeling Criteria"
  section with four label definitions (`bug`, `enhancement`, `question`,
  `documentation`) and three priority-tier definitions (`high-priority`,
  `medium-priority`, `low-priority`) — all added directly to the markdown body
  with no frontmatter change required.
- **Confidence**: settled (first-party worked example from the documentation)
- **Quote**: (no single-sentence direct quote; the example is a before/after
  code block — see Concrete Artifacts for verbatim example)
- **Our assessment**: The worked example establishes a canonical pattern for
  the most common instruction-tuning operation: adding criteria or rules to
  guide the agent's decision-making. The before workflow routes issues and adds
  generic labels; the after workflow adds explicit rules for label selection
  and priority tiers. This is hot-editable because the decision rules are in
  the markdown body as natural language, not in a `tools:` or `permissions:`
  block. For Ch01/Ch02: use this as the reference example when teaching
  practitioners how to iterate on agent behavior. The pattern — "add an
  instruction section, re-run, observe" — is the fastest feedback cycle in
  gh-aw development.

### Claim 6: Adding a `tools:` block to a workflow requires recompilation — tool capability additions are never hot-editable

- **Evidence**: The page's "Example: Adding a Tool (Requires Recompilation)"
  section shows a before/after where a `tools:` block is added to frontmatter
  (specifically `github: toolsets: [issues]`), with the notation that this
  "must recompile." The tool addition happens in the YAML frontmatter section
  (between `---` markers), not in the markdown body.
- **Confidence**: settled (first-party worked example; `tools:` is one of the
  12 named recompile-required field categories from Claim 3)
- **Quote**: (no single-sentence direct quote; see Concrete Artifacts for
  verbatim before/after)
- **Our assessment**: This is the canonical counter-example to Claim 5 — the
  two worked examples together define the boundary precisely. Labeling criteria
  → markdown body → hot-editable. GitHub Issues tool access → frontmatter →
  recompile required. The distinction matters when practitioners are debugging
  why a workflow can't see certain GitHub data: if the tool that reads that
  data isn't in the frontmatter, editing the markdown won't fix it — a
  frontmatter change plus recompile is needed. For Ch02: document this
  pair of examples as the primary illustration of the hot-edit vs. recompile
  boundary in workflow development.

### Claim 7: Runtime expression safety in the markdown body permits specific GitHub context expressions but blocks arbitrary unsanitized user input — `steps.sanitized.outputs.text` is the documented safe path for user-provided content

- **Evidence**: The page's "Expressions and Environment Variables" section
  defines two categories. Allowed: `${{ github.event.issue.number }}`,
  `${{ github.repository }}`, `${{ github.event.issue.title }}`,
  `${{ steps.sanitized.outputs.text }}`, `${{ github.actor }}`. Prohibited
  (with note "Arbitrary expressions are blocked for security. This will fail
  at runtime"): `${{ github.event.comment.body }}`.
- **Confidence**: settled (first-party documentation; both categories are
  explicitly enumerated with examples)
- **Quote**: "Arbitrary expressions are blocked for security. This will fail
  at runtime"
- **Our assessment**: The expression safety boundary is important because
  markdown body expressions are a potential prompt injection vector — if a
  workflow agent receives direct user comment content via `${{ github.event.comment.body }}`,
  an attacker could craft a comment that hijacks the agent's instructions.
  The prohibition on arbitrary expressions and the `steps.sanitized.outputs.text`
  safe path are gh-aw's solution: run a sanitization step and use only its
  cleaned output. This connects to the five-layer security model in
  `docs-ghaw-how-they-work.md` Claim 3, where output sanitization (Layer 5)
  defends against prompt injection. For Ch03 (Safety and Verification) and Ch02
  (Harness Engineering): document the expression safety rule as the canonical
  pattern for safe user input handling in gh-aw markdown. The rule is:
  `steps.sanitized.outputs.text`, never `${{ github.event.*.body }}` or
  `${{ github.event.*.comment }}` directly.

## Concrete Artifacts

### Hot-Edit vs. Recompile Decision Rule (from page structure)

```
Two-part workflow architecture:
  YAML frontmatter (between --- markers):
    → Compiled into .lock.yml at gh aw compile time
    → Changes require recompilation
    → Security-sensitive

  Markdown body (below the second --- marker):
    → Loaded at runtime from the original .md file
    → Changes take effect on next workflow run
    → No recompilation needed

Decision: Which part am I editing?
  Frontmatter → must run gh aw compile before changes take effect
  Markdown body → edit and re-run, no compile step needed
```

### Complete Recompile-Required Field List (12 categories, verbatim from page)

```
Changes to the YAML frontmatter always require recompilation.
These are security-sensitive configuration options.

Requires recompilation:
  - Triggers       (on:):              Event types, filters, schedules
  - Permissions    (permissions:):     Repository access levels
  - Tools          (tools:):           Tool configurations, MCP servers, allowed tools
  - Network        (network:):         Allowed domains, firewall rules
  - Safe outputs   (safe-outputs:):    Output types, threat detection
  - MCP Scripts    (mcp-scripts:):     Custom MCP tools defined inline
  - Runtimes       (runtimes:):        Node, Python, Go version overrides
  - Imports        (imports:):         Shared configuration files
  - Custom jobs    (jobs:):            Additional workflow jobs
  - Engine         (engine:):          AI engine selection (copilot, claude, codex)
  - Timeout        (timeout-minutes:): Maximum execution time
  - Roles          (roles:):           Permission requirements for actors
```

### Hot-Editable Markdown Body Element Types (verbatim from page)

```
You can freely edit (no recompilation needed):
  - Task instructions
  - Output templates
  - Conditional logic ("If X, then do Y")
  - Context explanations
  - Examples
```

### Example: Adding Instructions (Hot-Edit — no recompilation)

```markdown
# BEFORE (.github/workflows/issue-triage.md):
---
on:
  issues:
    types: [opened]
---
# Issue Triage
Read issue #${{ github.event.issue.number }} and add appropriate labels.

# AFTER (edited on GitHub.com — no compile needed):
---
on:
  issues:
    types: [opened]
---
# Issue Triage
Read issue #${{ github.event.issue.number }} and add appropriate labels.
## Labeling Criteria
Apply these labels based on content:
- `bug`: Issues describing incorrect behavior with reproduction steps
- `enhancement`: Feature requests or improvements
- `question`: Help requests or clarifications needed
- `documentation`: Documentation updates or corrections

For priority, consider:
- `high-priority`: Security issues, critical bugs, blocking issues
- `medium-priority`: Important features, non-critical bugs
- `low-priority`: Nice-to-have improvements, minor enhancements
```

*Source: `guides/editing-workflows` — "Example: Adding Instructions" section*

### Example: Adding a Tool (Requires Recompilation)

```yaml
# BEFORE:
---
on:
  issues:
    types: [opened]
---

# AFTER (must recompile — tools: is a frontmatter change):
---
on:
  issues:
    types: [opened]

tools:
  github:
    toolsets: [issues]
---
```

*Source: `guides/editing-workflows` — "Example: Adding a Tool (Requires Recompilation)" section*

### Expression Safety: Allowed vs. Prohibited (verbatim from page)

```
# Allowed expressions in markdown body:
${{ github.event.issue.number }}   — issue number (GitHub context, read-only)
${{ github.repository }}           — repository identifier
${{ github.event.issue.title }}    — issue title (static at event time)
${{ steps.sanitized.outputs.text }} — sanitized step output (safe path for user content)
${{ github.actor }}                — user who triggered the workflow

# Prohibited (blocked for security, will fail at runtime):
${{ github.event.comment.body }}   — raw user-provided content (unsanitized)

# Rule: arbitrary expressions are blocked for security.
# Safe path for user input: use steps.sanitized.outputs.text
# instead of direct ${{ github.event.*.body }} access.
```

*Source: `guides/editing-workflows` — "Expressions and Environment Variables" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 7 ("Only frontmatter changes
    require recompilation — the markdown body is loaded at runtime, enabling
    instruction edits without running `gh aw compile`"): that claim documents
    the same boundary from the technical reference page's perspective; this
    source page documents it from the practitioner guide's perspective with
    named element lists and worked examples. The two together give both the
    *principle* (compilation-process) and the *application* (this page).
    Quote verified from that note: "Compilation is only required when changing
    **frontmatter configuration**. The **markdown body** is loaded at runtime."
  - `docs-ghaw-how-they-work.md` Claim 7 (the compilation model separates
    editable `.md` source from compiled `.lock.yml`): that claim establishes
    the `.md` → `.lock.yml` model; this source page is its practitioner
    consequence — the `.md` is editable at any time; the `.lock.yml` only
    changes on recompile.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth
    security pipeline, with compile-time validation as Layer 1): the
    "security-sensitive configuration options" rationale for requiring
    recompilation on all frontmatter changes is the Layer 1 validation
    that Claim 3 names. Every frontmatter change triggers a fresh security
    validation pass; instruction-only changes do not.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 7 (frontmatter/markdown body
    boundary): this source extends that claim with (a) the specific named list
    of 12 frontmatter fields requiring recompilation, (b) the named list of
    5 hot-editable markdown body element types, and (c) concrete before/after
    examples. The compilation-process note states the principle; this note
    gives it operational specificity.
  - `docs-ghaw-how-they-work.md` Claim 3 (output sanitization as Layer 5 of
    the security pipeline): Claim 7 in this note (expression safety, prohibited
    `${{ github.event.comment.body }}`, `steps.sanitized.outputs.text` as the
    safe path) is the practical editing-time consequence of the output
    sanitization layer. The "how they work" note names the layer; this note
    names the specific expression pattern practitioners must follow.
  - `docs-ghaw-frontmatter-full-reference.md` (complete frontmatter field
    catalog): that note is the exhaustive 200+ field reference; this note's
    12-field recompile list is the practitioner-facing subset that matters
    most for editing workflows. Together they give both the comprehensive
    field inventory and the critical editing-consequence taxonomy.

- **Contradicts**: None identified. All claims in this source are consistent
  with existing source notes. The 12-field recompile-required list is
  consistent with `docs-ghaw-compilation-process.md`'s compilation model and
  `docs-ghaw-frontmatter-full-reference.md`'s field catalog. No contradiction
  issue required.

  *Note on `imports:`:* The compilation-process note's "Runtime vs Compile-Time
  Boundary" artifact lists "Adding/removing markdown imports" as not requiring
  recompilation. This likely refers to inline markdown-level include references
  within the markdown body, which is distinct from the `imports:` YAML frontmatter
  field that this source lists as requiring recompilation. The two are using
  "imports" in different senses (markdown body references vs. YAML frontmatter
  field). Not a contradiction; a naming ambiguity worth tracking.

- **Novel**:
  - **Named hot-editable markdown body element types** (Claim 2): No other
    source in the corpus enumerates the five categories of freely-editable
    markdown body elements (task instructions, output templates, conditional
    logic, context explanations, examples). Prior notes state the principle
    ("markdown body is editable") but not the categorized list.
  - **Complete 12-field recompile-required list** (Claim 3): Prior corpus
    entries describe the *principle* (frontmatter → recompile) but none
    enumerate all 12 named frontmatter field categories constituting the
    boundary. This is the first source to provide the complete enumeration.
  - **Before/after editing examples** (Claims 5, 6): The worked before/after
    examples (adding labeling criteria, adding a tool) are not documented in
    any other source note. They provide the clearest, most concrete illustration
    of the hot-edit vs. recompile boundary in the corpus.
  - **Expression safety: allowed vs. prohibited patterns** (Claim 7): The
    specific allowed/prohibited expression categories — including the
    `steps.sanitized.outputs.text` safe path and the prohibition on
    `${{ github.event.comment.body }}` — are not documented in any other
    source note. This is the first source to name the expression safety
    boundary at the editing level (prior notes covered output sanitization
    as an architecture layer, not as a concrete expression authoring rule).
  - **Browser-edit path for instruction iteration** (Claim 4): The explicit
    statement that markdown body changes can be made "directly on GitHub.com"
    without a local development environment is not highlighted in any other
    source note. This adoption-lowering fact is novel to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the two-part editing mental model** (Claim 1): The "frontmatter →
  recompile / markdown body → hot-edit" decision rule should be the first
  section in any harness workflow iteration guidance. Before any "how to
  edit" instructions, practitioners need this binary: which part am I
  changing? Cite this page as the reference; the introductory paragraph
  provides the canonical statement.

- **Add the 12-field recompile-required list** (Claim 3): Update the harness
  engineering chapter's compilation guidance to include the complete
  enumeration of frontmatter fields that trigger a recompile requirement.
  Currently the corpus states the principle but not the complete list. This
  list is the authoritative "must recompile" checklist practitioners can
  reference when evaluating a proposed edit.

- **Add the 5-element hot-editable list as the "safe to iterate" whitelist**
  (Claim 2): Pair with the 12-field recompile list as the positive complement
  — "these are the things you can always change without compiling." Task
  instructions, output templates, conditional logic, context explanations,
  and examples form the complete set of hot-editable elements.

- **Use the before/after examples as the canonical harness iteration
  illustration** (Claims 5, 6): The two worked examples (adding labeling
  criteria → hot-edit; adding a tools block → recompile required) are the
  clearest pedagogical artifact in the corpus for teaching the editing
  boundary. Include both in Ch02's iteration loop section.

### Chapter 03: Safety and Verification

- **Add expression safety rules for markdown body** (Claim 7): The prohibition
  on `${{ github.event.comment.body }}` and the `steps.sanitized.outputs.text`
  safe path should appear in Ch03's prompt injection defense section. This
  extends the five-layer security model (output sanitization, Layer 5 from
  `docs-ghaw-how-they-work.md`) with the concrete editing-time expression
  pattern that enforces it.

### Chapter 01: Daily Workflows

- **Highlight the browser-edit path for instruction iteration** (Claim 4):
  For teams where instruction refinement is done by non-developers (PMs,
  domain experts, tech writers), the ability to edit markdown body
  instructions directly on GitHub.com without a compile environment is
  adoption-relevant. Add to Ch01's daily workflow patterns as the
  "lightweight iteration" path for agent instruction tuning.

### Chapter 05: Team Adoption

- **Distinguish roles by editing boundary** (Claims 1–4): The hot-edit vs.
  recompile boundary maps naturally to team role separation: harness engineers
  own frontmatter changes (compile, test, deploy new configurations); domain
  experts own markdown body changes (refine instructions, update criteria,
  add examples). The browser-edit path enables the latter without requiring
  access to the harness engineering toolchain. This is a team structure
  recommendation worth adding to Ch05.

## Extraction Notes

1. **Page is in the `guides/` section, not `reference/`**: This is the first
   `guides/`-section page extracted in the corpus. The guides section is
   practitioner-oriented (how-to, worked examples) vs. the reference section's
   technical specification orientation. The page is relatively short and
   focused on editing mechanics rather than comprehensive coverage.

2. **Multiple WebFetch passes for verbatim accuracy**: The gh-aw documentation
   is an Astro/Starlight SPA. Three separate WebFetch passes were used to
   capture content: a general extraction, a verbatim-focused pass, and a
   detail-focused pass targeting the examples and expressions sections.
   Quotes marked as verbatim were confirmed consistent across at least two
   passes.

3. **Before/after code blocks confirmed verbatim**: The example code blocks
   (Adding Instructions, Adding a Tool) were returned consistently across
   WebFetch passes and are treated as accurate to the source.

4. **`imports:` naming ambiguity noted**: The compilation-process note's
   concrete artifact lists "Adding/removing markdown imports" as not requiring
   recompilation, while this source's frontmatter field list includes `imports:`
   (the YAML frontmatter field) as requiring recompilation. These likely refer
   to different mechanisms. Not filed as a contradiction; documented in
   Cross-References.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-12.

6. **No contradictions to file**: Reviewed all existing source notes and
   CONTRADICTIONS.md. No claims in this source materially oppose any existing
   source note at the MINER.md §4a filing threshold. The 12-field recompile
   list and hot-edit element types are additive specificity to the existing
   compilation model documentation; they do not contradict it.
