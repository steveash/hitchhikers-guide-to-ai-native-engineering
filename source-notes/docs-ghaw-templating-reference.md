---
source_url: https://github.github.com/gh-aw/reference/templating
source_type: docs
title: "GitHub Agentic Workflows: Templating Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#413"
---

# GitHub Agentic Workflows: Templating Reference

> The authoritative reference for gh-aw's four dynamic content mechanisms —
> GitHub Actions expression restrictions in markdown (vs. permissive frontmatter),
> the `{{#if}}` conditional block syntax, the deprecated activation outputs form,
> and runtime imports for injecting file and URL content into prompt text at
> execution time, with security controls (path restriction, expression rejection,
> YAML/comment stripping) that prevent prompt injection via imported content.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/templating` page —
  in the "Reference" section, alongside `reference/imports`, `reference/sandbox`,
  `reference/network`. Reference pages document platform behavior authoritatively.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind the `gh aw` CLI and Peli de Halleux's agent factory blog series.
  Expression allowlists, runtime import security behavior, and deprecation warnings
  are authoritative for the `gh aw` platform. Claims about security rationale are
  documented but design intent is partly interpretive.
- **Scope**: Four templating mechanisms for dynamic content in gh-aw workflow files:
  (1) GitHub Actions expression restrictions in markdown body, (2) activation outputs
  (current and deprecated forms), (3) conditional markdown via `{{#if}}`, and
  (4) runtime imports for file/URL injection at execution time. Does NOT cover:
  compile-time frontmatter imports via the `imports:` field (that is the separate
  `reference/imports` page, mined separately); trigger configuration; or the
  broader compilation model (see `docs-ghaw-compilation-process.md`).

## Extracted Claims

### Claim 1: GitHub Actions expressions in workflow markdown are restricted to a safe subset — secrets, environment variables, and complex functions are prohibited to prevent sensitive data exposure to the LLM

- **Evidence**: The page documents an explicit allowlist/denylist for expressions
  in workflow markdown (as distinct from YAML frontmatter, which has no such
  restriction). Permitted in markdown: event properties (`github.event.*`),
  repository context (`github.actor`, `github.repository`), run metadata
  (`github.run_id`, `github.job`), and pattern expressions (`steps.*`, `needs.*`).
  Prohibited: "All other expressions are disallowed, including `secrets.*`, `env.*`,
  `vars.*`, and complex functions."
- **Confidence**: settled (first-party reference documentation; the allowlist and
  denylist are explicitly named as platform constraints)
- **Quote**: "All other expressions are disallowed, including `secrets.*`, `env.*`,
  `vars.*`, and complex functions"
- **Our assessment**: The restriction asymmetry — frontmatter can use full GitHub
  Actions expressions; markdown cannot — reflects the security boundary between the
  configuration layer (frontmatter: safe, machine-readable YAML) and the instruction
  layer (markdown: sent to the LLM as prompt text). If secrets were permitted in
  markdown, they would become part of the prompt context visible to the LLM, with
  all the exfiltration risk that implies. This is a concrete instance of the
  "YAML constrains, markdown instructs" separation in `docs-ghaw-how-they-work.md`
  Claim 1 — the frontmatter holds sensitive configuration; the markdown holds
  task instructions. For Ch02 (Harness Engineering): document that expression
  restrictions in markdown are a security feature, not a limitation — the allowed
  subset (event metadata, actor, run ID) is sufficient for context-injection use
  cases without exposing secrets.

### Claim 2: Activation outputs have a deprecated form (`needs.activation.outputs.*`) and a current form (`steps.sanitized.outputs.text/title/body`) — the deprecated form still works but generates compilation warnings

- **Evidence**: The page documents that using `${{ needs.activation.outputs.* }}`
  in workflow markdown "is deprecated. These expressions still work but produce a
  deprecation warning during compilation." The recommended replacement is
  `${{ steps.sanitized.outputs.text }}` and related outputs (`title`, `body`)
  accessed directly via the `steps.sanitized` step outputs.
- **Confidence**: settled (first-party documentation; deprecation warning behavior
  at compile time is an explicit platform specification)
- **Quote**: "in workflow markdown is **deprecated**. These expressions still work
  but produce a deprecation warning during compilation."
- **Our assessment**: The rename from `needs.activation.outputs.*` to
  `steps.sanitized.outputs.*` reflects an architectural change in how gh-aw
  exposes sanitized event content — moving from a job-level output reference to
  a step-level output reference. The "sanitized" naming is significant: it signals
  that the content has been processed through the output sanitization layer (Layer 5
  of the security pipeline in `docs-ghaw-how-they-work.md` Claim 3) before being
  made available to the workflow prompt. For Ch02: any existing workflow examples
  that reference `needs.activation.outputs.*` should be updated to
  `steps.sanitized.outputs.text/title/body`. This is a migration that will not
  break immediately but will produce compilation noise until updated.

### Claim 3: Conditional markdown blocks (`{{#if expression}}...{{/if}}`) include or exclude prompt sections at compile time based on GitHub Actions boolean expressions — no nesting, `else` clauses, or loops are supported

- **Evidence**: The page documents the conditional syntax with an example:
  `{{#if github.event.issue.number}}` wrapping an issue-specific analysis section.
  "The compiler automatically wraps expressions with `${{ }}` for GitHub Actions
  evaluation." Falsy values listed: "`false`, `0`, `null`, `undefined`,
  `""` (empty string)." Limitations stated: no nesting, no else clauses, no loops.
- **Confidence**: settled (first-party documentation; the syntax, falsy values, and
  limitations are explicitly stated)
- **Quote**: "The compiler automatically wraps expressions with `${{ }}` for
  GitHub Actions evaluation."
- **Our assessment**: Conditional markdown is the mechanism for making prompt
  content event-adaptive without duplicating workflow files. An issue-triggered
  workflow can include issue-specific prompt sections only when an issue number is
  present; a PR-triggered workflow can include PR-specific sections when the PR
  context exists. The no-nesting / no-else limitation is notable — it forces
  simple, flat conditionals rather than complex branching logic in the prompt body.
  This is consistent with the "what, not how" philosophy in `docs-ghaw-agentic-
  authoring.md` Claim 8: the prompt author specifies what the agent should do in
  a given context; the LLM handles the logic of how. Complex conditional branching
  belongs in the agent's reasoning, not in the template. For Ch02 (Harness
  Engineering): introduce `{{#if}}` as the mechanism for event-adaptive prompt
  sections. Note that `docs-ghaw-dispatch-ops.md` Claim 4 documents the more
  specific `{{#if (eq ...)}}` variant for `workflow_dispatch` input-driven
  branching — that is a specialization of the general `{{#if}}` documented here.

### Claim 4: Runtime imports inject file or URL content directly into the workflow prompt at execution time — not at compile time — using `{{#runtime-import filepath}}` or `{{#runtime-import? filepath}}` syntax

- **Evidence**: The page distinguishes runtime imports from compile-time imports:
  runtime imports "include content from files and URLs in workflow prompts at
  runtime." The required form (`{{#runtime-import filepath}}`) fails if the file
  is missing; the optional form (`{{#runtime-import? filepath}}`) silently skips
  missing files. Line range extraction is supported:
  `{{#runtime-import docs/auth.go:45-52}}`.
- **Confidence**: settled (first-party documentation; the two syntactic forms,
  line range capability, and required vs optional behavior are explicitly specified)
- **Quote**: (no direct prose quote for this specific claim; see Concrete Artifacts
  for verbatim syntax forms)
- **Our assessment**: The compile-time vs. runtime distinction is architecturally
  significant: compile-time imports (via the `imports:` frontmatter field) are
  processed by `gh aw compile` and embedded in the `.lock.yml`; runtime imports
  are resolved when the workflow runs. This means runtime imports can reference
  content that changes between runs (e.g., a living documentation file, a
  configuration file updated by another process). The line range extraction feature
  (`file:line-start-line-end`) enables surgical injection of specific code sections
  — e.g., injecting the implementation of a specific function into the prompt for
  a code review workflow. For Ch02 (Harness Engineering): document runtime imports
  as the dynamic content injection mechanism for gh-aw workflows, distinct from the
  static composition of compile-time imports. Both serve different use cases:
  compile-time imports for stable shared components; runtime imports for
  content that varies between executions.

### Claim 5: Runtime imports enforce three security controls to prevent prompt injection — path traversal is rejected, all file paths are bounded to the `.github` folder, and GitHub Actions expressions in imported content are rejected with an error

- **Evidence**: The page documents security restrictions on runtime imports:
  "All file paths are resolved within the `.github` folder" (bounding the import
  scope); path traversal attempts are rejected; "GitHub Actions expressions
  (`${{ ... }}`) are **rejected with error**" in imported content (preventing
  template injection through attacker-controlled files).
- **Confidence**: settled (first-party documentation; the three restrictions are
  explicit platform specifications, not implementation details)
- **Quote**: "GitHub Actions expressions (`${{ ... }}`) are **rejected with error**"
- **Our assessment**: The three controls together address three distinct attack
  surfaces. Path restriction (`.github` folder only) prevents imports from reading
  arbitrary repository content (e.g., `.env` files, `.ssh/`, secrets). Path
  traversal rejection (`../` sequences) prevents escape from the bounded folder.
  GitHub Actions expression rejection in imported content prevents a scenario where
  an attacker modifies an imported file to inject `${{ secrets.API_KEY }}` into
  the prompt — which would surface the secret to the LLM. This last control is
  the most subtle: the templating system strips expressions from imported content
  so that even if an attacker controls an imported file, they cannot use the
  import mechanism as a side channel for secret exfiltration. For Ch03 (Safety
  and Verification): the expression-rejection control in runtime imports is a
  concrete implementation of defense against prompt injection via included content.
  Worth noting as a design pattern for any system that injects external content
  into AI prompts.

### Claim 6: URL-based runtime imports are supported with a 1-hour per-run cache, and imported content has YAML frontmatter and HTML/XML comments automatically stripped before injection

- **Evidence**: The page states URL imports "support HTTP/HTTPS" and are "cached
  for 1 hour per workflow run." Imported content is processed before injection:
  "YAML front matter and HTML/XML comments are automatically stripped." Error
  handling for URL fetch failures is included in the documented error cases.
- **Confidence**: settled (first-party documentation; cache TTL and stripping
  behavior are explicit platform specifications)
- **Quote**: "YAML front matter and HTML/XML comments are automatically stripped."
- **Our assessment**: The automatic stripping behavior is a practical affordance:
  practitioners can import markdown documentation files (which may have YAML
  frontmatter) or HTML-commented source files into workflow prompts without the
  frontmatter or comments polluting the injected text. The LLM receives clean
  content. The 1-hour cache is relevant for rate-limiting: frequently-triggered
  workflows that import the same URL will not re-fetch on every run within the
  hour — important for URLs that have per-request rate limits. For Ch02: when
  designing workflows that import URL content, practitioners can rely on the cache
  for frequently-triggered workflows. For Ch03: URL import fetch failures are
  handled with descriptive error messages rather than silent failures — consistent
  with the "fail loudly" pattern in agentic harness design.

### Claim 7: The body-level `{{#import}}` shorthand is deprecated and normalizes to runtime imports — it produces warnings during compilation

- **Evidence**: The page notes that `{{#import}}` is a "body-level shorthand"
  that "normalizes to runtime imports but produces warnings." This is the
  deprecated form; the explicit `{{#runtime-import}}` syntax is the current form.
- **Confidence**: settled (first-party documentation; deprecated form behavior
  is an explicit platform specification)
- **Quote**: (no direct prose quote; described as a "body-level shorthand" that
  "normalizes to runtime imports but produces warnings")
- **Our assessment**: The deprecation path (`{{#import}}` → `{{#runtime-import}}`)
  is a breaking-change-free migration: existing workflows using the old shorthand
  continue to work but generate compilation warnings, giving teams time to migrate.
  The explicit `{{#runtime-import}}` naming is more self-documenting — it makes
  clear that the import happens at runtime, not compile time, which matters for
  reasoning about content freshness and cache behavior. For Ch02: workflows
  using `{{#import}}` body-level syntax should be updated to `{{#runtime-import}}`
  or `{{#runtime-import?}}` to silence compilation warnings.

## Concrete Artifacts

### Expression Restrictions in Workflow Markdown

```
PERMITTED in workflow markdown (sent to LLM as prompt text):
  Event properties:    ${{ github.event.issue.number }}
                       ${{ github.event.pull_request.title }}
  Repository context:  ${{ github.actor }}
                       ${{ github.repository }}
  Run metadata:        ${{ github.run_id }}
                       ${{ github.job }}
  Pattern expressions: ${{ steps.<id>.outputs.<name> }}
                       ${{ needs.<job>.outputs.<name> }}

PROHIBITED in workflow markdown:
  Secrets:             ${{ secrets.* }}
  Environment vars:    ${{ env.* }}
  Repository vars:     ${{ vars.* }}
  Complex functions:   ${{ toJson(...) }}  and similar

NOTE: Frontmatter (YAML between --- delimiters) has NO such restriction —
      full GitHub Actions expressions including secrets.* are permitted there.
```

*Source: Templating reference page, "GitHub Actions Expressions" section*

### Activation Outputs — Current vs. Deprecated Forms

```yaml
# CURRENT form (recommended):
${{ steps.sanitized.outputs.text }}    # sanitized event body text
${{ steps.sanitized.outputs.title }}   # sanitized event title
${{ steps.sanitized.outputs.body }}    # sanitized event body

# DEPRECATED form (still works; produces deprecation warning at compile time):
${{ needs.activation.outputs.text }}
${{ needs.activation.outputs.title }}
${{ needs.activation.outputs.body }}
```

*Source: Templating reference page, "Activation Outputs" section*

### Conditional Markdown Syntax

```markdown
{{#if github.event.issue.number}}
## Issue-Specific Analysis
You are analyzing issue #${{ github.event.issue.number }}.
{{/if}}
```

Falsy values: `false`, `0`, `null`, `undefined`, `""` (empty string)

Limitations: No nesting, no `{{else}}` clauses, no loops.

The compiler automatically wraps the expression with `${{ }}` for GitHub Actions
evaluation — the author writes `{{#if github.event.issue.number}}`, not
`{{#if ${{ github.event.issue.number }}}}`.

*Source: Templating reference page, "Conditional Markdown" section*

### Runtime Import Syntax Forms

```
# Required import (fails if file not found):
{{#runtime-import .github/shared/context.md}}

# Optional import (silently skipped if file not found):
{{#runtime-import? .github/shared/optional-context.md}}

# Line range extraction (inject lines 45-52 only):
{{#runtime-import docs/auth.go:45-52}}

# URL import (HTTP/HTTPS, cached 1 hour per workflow run):
{{#runtime-import https://example.com/context.md}}

# Deprecated body-level shorthand (still works; produces warnings):
{{#import .github/shared/context.md}}
```

*Source: Templating reference page, "Runtime Imports" section*

### Runtime Import Security Controls

```
Control 1: Path restriction
  - All file paths resolved within .github folder
  - Prevents reading arbitrary repository content (.env, .ssh/, etc.)

Control 2: Path traversal rejection
  - Sequences like ../ are rejected
  - Prevents escape from the .github folder boundary

Control 3: GitHub Actions expression rejection
  - ${{ ... }} expressions in imported content → rejected with error
  - Prevents attacker-controlled files from injecting secrets into prompts
  - Applies to both file and URL imports

Automatic content processing (before injection into prompt):
  - YAML frontmatter stripped
  - HTML/XML comments stripped
  - Clean content delivered to LLM
```

*Source: Templating reference page, "Runtime Imports" and "Error Handling" sections*

### Runtime Import Error Types

```
Error type            | Trigger condition
----------------------|------------------------------------------
File not found        | Required import (non-?) references missing file
Invalid line range    | Line numbers out of bounds or malformed range
Path traversal        | Import path contains ../ or other traversal
GitHub Actions macros | ${{ ... }} expression found in imported content
URL fetch failure     | HTTP/HTTPS fetch failed (timeout, 4xx, 5xx)
```

*Source: Templating reference page, "Error Handling" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 1 (YAML constrains, markdown instructs):
    The expression restriction asymmetry (frontmatter: unrestricted; markdown:
    allowlisted) is a concrete enforcement mechanism for the "YAML constrains,
    markdown instructs" architectural principle. This source gives the exact
    enforcement boundary; that source names the principle.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security pipeline): The
    markdown expression restriction is a compilation-time validation (Layer 1) —
    the compiler rejects prohibited expressions before the workflow runs.
    The runtime import controls (path restriction, expression rejection) operate
    at runtime (Layer 2/5). This templating reference fills in concrete
    implementation details for two of the five layers.
  - `docs-ghaw-dispatch-ops.md` Claim 4 (Handlebars conditionals `{{#if (eq ...)}}`
    for input-driven behavior): The dispatch-ops note documents `{{#if (eq ...)}}` as
    a specialization using comparison functions; the templating reference documents
    the general `{{#if expression}}` form for any boolean expression. The two
    together give the complete conditional markdown picture: simple boolean
    conditions (this source) and value-comparison conditions (dispatch-ops).
  - `docs-ghaw-agentic-authoring.md` Claim 6 (`debug.md` as a URL-addressable
    prompt): URL-based runtime imports and URL-addressable self-contained prompts
    share the same design philosophy — content hosted at stable URLs can be
    dynamically fetched and injected into agent context. Runtime imports formalize
    this for workflow prompts; the URL-addressable pattern generalizes it.

- **Extends**:
  - `docs-ghaw-compilation-process.md` (five-phase compilation pipeline): The
    "resolve" phase in the compilation pipeline is where template expression
    resolution and conditional markdown evaluation occur. The templating reference
    documents what is resolved; the compilation process note documents when and
    how. Together they give the full picture of template processing in gh-aw.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated
    state mutation): Runtime imports are the complement — they bring external
    content INTO the prompt, while Safe Outputs send agent-generated content OUT
    to GitHub state. Both operate with security controls. The templating reference
    adds the "input-side" security model (what can be injected) alongside the
    existing "output-side" model.

- **Contradicts**: None identified. The expression restriction model, conditional
  markdown, and runtime import security controls are consistent with the broader
  security architecture documented in existing corpus notes.

- **Novel**:
  - **Expression restriction asymmetry (frontmatter vs. markdown)** (Claim 1):
    No existing source note documents that frontmatter and markdown have different
    expression allowlists in gh-aw. The explicit prohibition of `secrets.*`,
    `env.*`, `vars.*` in markdown — while permitting them in frontmatter — is
    new to the corpus.
  - **Activation outputs deprecation** (Claim 2): The migration from
    `needs.activation.outputs.*` to `steps.sanitized.outputs.*` is not documented
    in any existing source note. Existing workflows and documentation that reference
    the deprecated form will generate compilation warnings.
  - **Runtime imports as a distinct mechanism** (Claims 4, 6): While compile-time
    `imports:` frontmatter is referenced in multiple notes, runtime imports
    (`{{#runtime-import}}`) as a separate mechanism for execution-time content
    injection are new to the corpus. The line range extraction feature is particularly
    novel — no existing note documents code-fragment injection by line range.
  - **Triple security control for runtime imports** (Claim 5): The combination of
    path restriction + path traversal rejection + expression rejection as a prompt
    injection defense for imported content is new to the corpus. The expression-
    rejection control (preventing `${{ secrets.API_KEY }}` in imported files from
    surfacing secrets to the LLM) is the most subtle and most security-significant
    finding in this source.
  - **Deprecated `{{#import}}` shorthand** (Claim 7): The deprecation of the
    body-level `{{#import}}` shorthand in favor of explicit `{{#runtime-import}}`
    is not documented in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Document the expression restriction boundary** (Claim 1): When writing workflow
  markdown (the instruction section), practitioners can use event metadata, actor,
  run ID, and step/job output references. Secrets, env vars, and vars are prohibited.
  This is not a limitation to work around — it is the security model. Guide should
  present the allowlist positively as "what you can use" rather than framing as
  restrictions. Cite `docs-ghaw-how-they-work.md` Claim 1 for the architectural
  rationale.

- **Introduce runtime imports as dynamic content injection** (Claim 4): For workflows
  that need to inject living documentation, configuration files, or code fragments
  into prompt context, `{{#runtime-import}}` is the mechanism. Distinguish from
  compile-time imports: runtime imports are for content that changes between runs;
  compile-time imports are for stable shared components. Document the line range
  extraction feature (`file:N-M`) as a code-review workflow building block.

- **Flag the activation outputs migration** (Claim 2): Any existing guide examples
  or practitioner templates that use `needs.activation.outputs.*` should be updated
  to `steps.sanitized.outputs.*`. Ch02 examples should use the current form only.

- **Present `{{#if}}` as the event-adaptive prompt pattern** (Claim 3): When a
  single workflow serves multiple trigger contexts (issue + PR, for example),
  conditional markdown allows event-specific prompt sections without duplicating
  workflow files. Note the flat-only limitation (no nesting, no else) and frame
  this as a constraint that keeps prompts readable.

### Chapter 03: Safety and Verification

- **Add runtime import expression rejection as a prompt injection defense** (Claim 5):
  Systems that inject external content into AI prompts must sanitize that content to
  prevent the injection of expressions or commands. gh-aw's approach — reject any
  `${{ ... }}` expression found in imported content with a compile error — is a
  concrete design pattern. Teams building custom harnesses that import external
  content into prompts should apply equivalent controls. This extends the defense-
  in-depth discussion beyond gh-aw to general harness design.

- **Document path restriction + traversal rejection as a file injection pattern**
  (Claim 5): Bounding file imports to a trusted directory (`.github`) and rejecting
  traversal sequences is the standard defense against directory traversal in content
  injection systems. Worth naming as a principle for any harness that lets agents
  or prompts reference files by path.

## Extraction Notes

1. **Compile-time imports not covered**: The `reference/imports` page (covering
   the `imports:` frontmatter field, parameterized imports, cross-repo imports,
   and `inlined-imports: true`) is a separate page linked from the templating
   reference but not the subject of this note. The imports reference was fetched
   to understand the boundary between compile-time and runtime imports but is not
   extracted here. A separate source note for the imports reference would be
   appropriate if nominated.

2. **No embedded code examples extracted verbatim**: The WebFetch tool's content
   extraction returns the page text but the model declined full verbatim
   reproduction. The code examples in Concrete Artifacts above are reconstructed
   from the described syntax, confirmed against two separate fetches of the page.
   Practitioners should verify against the live page at the source URL.

3. **No publication date**: Like other gh-aw documentation pages, this page does
   not carry an explicit publication date. `date_published` is left null.

4. **Dispatch-ops note cross-reference verified**: `docs-ghaw-dispatch-ops.md`
   Claim 4 was read and confirmed to document the `{{#if (eq ...)}}` specialization
   as a distinct (but related) conditional form. The general `{{#if expression}}`
   documented here and the value-comparison `{{#if (eq ...)}}` in dispatch-ops
   are complementary, not redundant.

5. **No contradictions filed**: Reviewed all existing source notes. No claims in
   this source materially oppose existing source notes. The expression restriction
   model and runtime import security controls are new to the corpus but consistent
   with the broader security architecture.
