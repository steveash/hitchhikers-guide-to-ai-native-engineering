---
source_url: https://developers.googleblog.com/building-scalable-ai-agents-with-modular-prompt-transpilation/
source_type: blog-post
title: "Building scalable AI agents with modular prompt transpilation"
author: Simerus Mahesh (Site Reliability Engineer, Google)
date_published: 2026-07-16
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1962"
---

# Building scalable AI agents with modular prompt transpilation

> A first-party Google Developers Blog post proposing that production system
> prompts be treated as build artifacts rather than static text: modular
> "skill file" templates (Jinja2-style `include`/`if`/`macro` syntax) are
> resolved by a transpiler that performs build-time validation (missing
> imports, undefined variables, circular dependencies) and CI/CD drift
> checking (golden-file regeneration and diff), with progressive-disclosure
> runtime skill loading and agent-authored PRs as the resulting capabilities.

## Source Context

- **Type**: blog-post (developers.googleblog.com, the official Google
  Developers Blog; published July 16, 2026 — the same day this source was
  discovered via the `google-developers` trusted feed).
- **Author credibility**: Simerus Mahesh is credited as a "Site Reliability
  Engineer" at Google. The article's `Article` JSON-LD metadata confirms
  this byline and the July 16, 2026 publish date. This is a first-party
  Google engineering account, but it is an individual practitioner post
  (SRE, not a named team like "Claude Code" or "GitHub Next"), and the post
  presents an architectural pattern and a single worked example rather than
  production usage statistics, adoption figures, or before/after
  measurements from a specific Google product. No quantitative evidence
  (error rates prevented, teams using this pattern, scale of "at production
  scale") is given anywhere in the post — every claim is presented as
  architectural reasoning and a single illustrative code example, not as a
  measured outcome.
- **Scope**: Covers one architectural pattern — modular prompt templates
  compiled by a transpiler — end to end: authoring (Jinja2-style skill
  files), compilation (import resolution, transpiled artifact), build-time
  validation (dependency graphs, circular-import detection), CI/CD drift
  checking (golden-file comparison), runtime skill loading (progressive
  disclosure), and agent-authored updates (PR-gated self-modification). Does
  NOT cover: a named tool, library, or product that implements this pipeline
  (no `transpiler` package, ADK feature, or Vertex AI capability is named or
  linked); benchmark or production evidence that the pattern improves
  reliability or reduces incidents; how the transpiler's variable/dependency
  validation is actually implemented (e.g., what "treat each prompt fragment
  as a node in a directed graph" looks like in code); or how this pattern
  interacts with existing prompt-versioning or eval tooling.

## Extracted Claims

### Claim 1: Three specific failure modes emerge once system prompts scale beyond a single file — obscured blast radius, copy-paste drift, and deferred runtime errors

- **Evidence**: Named and explained as a three-item list, each with its own
  explanatory sentence, following a stated general principle that this is
  "a classic software engineering scaling problem."
- **Confidence**: anecdotal (an SRE's architectural reasoning and pattern
  naming from a single blog post; no incident data, benchmark, or named
  production system is cited as evidence that these three modes are the
  dominant ones, or that they occur in the stated order of severity)
- **Quote**: "System prompt diffs are harder though. Adding a sentence could
  have unintended side effects across the entire agent, which is often hard
  to predict or test." ... "This leads to copy-pasting or multiple versions
  of the same functionality leading to inconsistencies." ... "While this
  helps with authoring, it pushes error detection to runtime. You might
  deploy a prompt that only fails when a specific, rarely-used workflow is
  triggered because of a missing variable or an invalid import path."
- **Our assessment**: The three failure modes are a plausible, well-named
  taxonomy — "obscured blast radius" and "deferred runtime errors" in
  particular give practitioners vocabulary for problems many teams have
  likely experienced without naming them this precisely. The "deferred
  runtime errors" failure mode is the most concrete and verifiable claim of
  the three: a prompt with a templating bug (missing variable, bad import)
  that only manifests when a rare code path is hit is a real and checkable
  category of bug, distinct from the other two which are more diffuse
  ("harder to predict or test," "leading to inconsistencies"). We buy the
  taxonomy as a useful framing but note it is asserted, not measured.

### Claim 2: The proposed fix is to treat prompts as build artifacts, authored as modular "skill files" that reduce scope and encapsulate a single behavior

- **Evidence**: Stated as the article's core architectural recommendation,
  directly following the failure-mode taxonomy, with an explicit contrast to
  "just static text."
- **Confidence**: emerging (a named architectural pattern with a worked code
  example, but presented as a recommendation rather than a documented
  production practice at Google or elsewhere)
- **Quote**: "The solution here is to treat prompts like build artifacts as
  opposed to just static text." ... "Instead of maintaining one monolithic
  prompt file, you can author modular skill files. This allows you to
  reduce the scope of each file and encapsulate a specific behavior, which
  allows teams to separate concerns and iterate on components individually."
- **Our assessment**: "Skill files" here is architecturally distinct from
  Claude Code's "Skills" (see Cross-References) — this post's skill files
  are Jinja2-style *prompt template fragments* resolved at compile time,
  not folders containing scripts/assets/data that Claude discovers and
  invokes at runtime. The convergent naming ("skill") across two different
  mechanisms (Anthropic's runtime-discoverable folders vs. this post's
  compile-time template includes) is worth flagging for the guide so the
  two are not conflated.

### Claim 3: The templating layer uses Jinja2-style syntax — `{% include %}`, `{% if %}/{% else %}`, and `{% macro %}` — to compose shared instructions and inject environment-specific values into a prompt template file

- **Evidence**: A full worked code example (`agents/sre_agent.prompt.md`)
  showing two `{% include %}` directives pulling in shared safety and
  tool-usage prompt fragments, an `{% if allow_remediation %}/{% else %}`
  conditional gating remediation-recommendation language, and a
  `{% macro bullet_section(title, items) %}` macro that renders a titled
  bullet list, called once with a "Required investigation steps" list.
- **Confidence**: emerging (a concrete, complete code example — the most
  verifiable claim in the post — but a single illustrative snippet, not
  evidence of a real deployed template library)
- **Quote**: (no single prose quote covers the whole example; the code block
  itself is the evidence — see Concrete Artifacts for the verbatim template)
- **Our assessment**: This is the most concrete and independently checkable
  artifact in the post. The syntax shown is literally Jinja2 (Python's
  templating library) — `{% include %}`, `{% if %}/{% else %}/{% endif %}`,
  `{% macro %}/{% endmacro %}`, and `{{ variable }}` interpolation are all
  standard Jinja2 constructs, not a bespoke DSL invented for this post. This
  means teams could plausibly implement the described transpiler as a thin
  wrapper around an existing, mature templating engine rather than building
  template parsing from scratch — a practical implementation detail the
  post itself does not state explicitly.

### Claim 4: A transpiler resolves the template's imports and variables to produce a fully rendered, deterministic prompt artifact that can be tested, audited, and diffed before it reaches the model

- **Evidence**: A before/after pair — the template from Claim 3 with
  `environment = "production"` and `allow_remediation = true` — is shown
  transpiling to a specific rendered text artifact with the conditional
  branch resolved, the macro expanded into a rendered `## Required
  investigation steps` bullet list, and the includes presumably inlined
  (though the transpiled example shown omits the included
  `shared/safety.prompt.md` and `shared/tool_usage.prompt.md` content).
- **Confidence**: emerging (a worked example with a specific
  before/after; but the transpiled example doesn't actually show the
  `{% include %}` fragments resolved, only the `{% if %}` and `{% macro %}`
  constructs — see Our assessment)
- **Quote**: "The result is a deterministic, fully rendered artifact that
  you can test, audit, and diff before it ever reaches the model. We can
  then use a transpiler to resolve the template imports to generate a file
  that is ready to be ingested by an agent."
- **Our assessment**: Worth flagging a gap in the worked example for the
  Assayer and any downstream reader: the "transpiled artifact" shown in the
  post never displays the resolved content of the two `{% include %}`
  directives (`shared/safety.prompt.md`, `shared/tool_usage.prompt.md`) —
  the output jumps straight to the SRE-agent-specific text. This doesn't
  invalidate the claim (the includes may simply have been omitted from the
  illustrative output for brevity), but it means the post's own example
  doesn't fully demonstrate "every include is a dependency" being resolved
  end to end.

### Claim 5: A production-grade transpiler must perform build-time validation for missing imports, undefined variables, and circular dependencies, treating each prompt fragment as a node in a directed graph

- **Evidence**: Stated as a requirement ("should be running validation
  checks") with a specific mechanism named (dependency graph, prompt
  fragments as graph nodes) and a specific failure mode it prevents
  (recursive imports causing silent production failure).
- **Confidence**: anecdotal (an architectural requirement asserted by the
  author; no implementation, tool, or specific validation algorithm is
  named beyond "directed graph," and no example of a caught error — e.g., an
  actual circular-import case — is shown)
- **Quote**: "We should be running validation checks for missing imports,
  undefined variables, and circular dependencies during the build process."
  ... "If you treat each prompt fragment as a node in a directed graph, you
  can easily catch recursive imports that would otherwise cause a silent
  failure in production."
- **Our assessment**: This directly parallels a documented, working
  implementation of the same idea in a different corpus source: gh-aw's
  compiler resolves `imports:` via "a deterministic breadth-first traversal"
  with explicit cycle detection during Phase 1 (parsing/validation) of its
  five-phase compilation pipeline (`docs-ghaw-compilation-process.md`
  Claim 2). Where this Google post asserts the requirement in the abstract
  ("treat each prompt fragment as a node in a directed graph"), the gh-aw
  reference documents a working, named algorithm (BFS with cycle detection)
  that does exactly this for markdown prompt imports in a shipped tool. The
  guide should prefer citing the gh-aw implementation as the concrete
  existence proof and this post as the generalized architectural rationale
  for why the check matters.

### Claim 6: CI pipelines should regenerate the transpiled prompt from source (the "golden file") and fail the build if it differs from the currently committed artifact, ensuring the repo always matches what's running in production

- **Evidence**: Stated as a named technique ("drift checking") with the
  specific mechanism (regenerate from source, compare to committed
  artifact, fail build on diff) and the stated purpose (close the gap
  between source files and deployed artifacts).
- **Confidence**: anecdotal (a named CI pattern description; no CI
  configuration, tool, or specific pipeline example is shown, unlike the
  templating code example in Claim 3)
- **Quote**: "This also enables drift checking. You can set your CI
  pipelines to be able to regenerate the transpiled prompt from source
  (referred to as the golden file) and compare it against the currently
  committed artifact. If the outputs differ, the build fails. This ensures
  that the code in your repo is exactly what's running in production,
  eliminating the gap between source files and deployed artifacts."
- **Our assessment**: "Golden file" testing is a well-established software
  pattern (used for snapshot testing, generated-code verification, etc.)
  applied here specifically to compiled prompts. The practical value is
  catching the specific failure mode where someone hand-edits a deployed
  prompt artifact directly (bypassing the source template) — the next CI
  run would regenerate from source, diff against the hand-edit, and fail,
  forcing the edit back into the templated source of truth. This is a
  reusable, low-effort CI check any team with a compiled-prompt pipeline
  could adopt regardless of whether they build a full transpiler.

### Claim 7: Progressive disclosure — a compiled, stable base prompt for non-negotiable behaviors plus runtime, on-demand retrieval of task-specific skill modules — reduces context exhaustion and keeps the agent focused

- **Evidence**: Stated as "a better architectural pattern" with an explicit
  mechanism: the compiled base prompt enforces "identity and safety
  boundaries," while the agent "can use a tool to dynamically retrieve only
  the specific skill modules required for the task at hand."
- **Confidence**: anecdotal (an architectural recommendation with a named
  benefit but no measurement of the context savings, no example tool
  definition for the retrieval mechanism, and no worked example of which
  skill modules get loaded for which task)
- **Quote**: "A better architectural pattern would be to leverage
  progressive disclosure. This is where we separate the stable control
  plane from task-specific context. The compiled base prompt should enforce
  non-negotiable behaviors like identity and safety boundaries. Then, at
  runtime, the agent can use a tool to dynamically retrieve only the
  specific skill modules required for the task at hand; this reduces
  context exhaustion and helps to keep the agent focused on its task."
- **Our assessment**: This is architecturally identical to Anthropic's
  documented "progressive disclosure" design for Claude Code Skills: "You
  should think of the entire file system as a form of context engineering
  and progressive disclosure" (`blog-anthropic-claude-code-skills-lessons.md`
  Claim 5). Both sources converge on the same two-tier design — a small,
  always-loaded control layer plus larger, on-demand content loaded only
  when needed — but from opposite directions: Anthropic's skills are
  runtime-discovered folders (no compile step at all), while this post's
  "skill modules" are compile-time template fragments that get selectively
  *retrieved* at runtime via a tool call after being compiled. The
  convergent architecture, independently arrived at by two different
  organizations describing two structurally different mechanisms, is a
  meaningful corroboration of progressive disclosure as a general principle
  — see Cross-References.

### Claim 8: Once prompts are modular, agents can propose updates to their own instruction layer via pull requests — drafting a new skill module and its imports rather than mutating instructions in real time — subject to the same transpiler validation and human review as any other code change

- **Evidence**: Stated as an emergent capability of the modular system
  ("Once you have this modular system, you unlock a powerful workflow"),
  with a specific scenario (an agent resolving a new incident type drafts a
  new skill module, updates imports, opens a PR) and an explicit statement
  distinguishing this from real-time self-modification.
- **Confidence**: anecdotal (a described workflow and its governance
  properties, not a demonstrated instance — no example PR, no named agent,
  no evidence this has actually happened is given)
- **Quote**: "When an agent resolves a new type of incident, it could
  theoretically draft a new skill module, update the relevant imports, and
  open a pull request." ... "The agent isn't mutating its own instructions
  in real-time; it's proposing a code change. The transpiler then subjects
  that proposal to the same validation and review rigors as any other code
  change. A human reviewer can inspect the PR, run the evals, and merge the
  change."
- **Our assessment**: The word "theoretically" in the source is worth
  flagging explicitly — the author frames this as a capability the
  architecture *unlocks*, not one that has been observed in production.
  The governance structure described (PR-gated, transpiler-validated,
  human-reviewed, evals run before merge) is the load-bearing safety
  property of the whole claim: it is architecturally indistinguishable from
  "an agent can propose a normal code change to a repo it has write access
  to," with the only novelty being that the changed file happens to be a
  prompt fragment rather than application code. The claim is really about
  *how modular prompts + transpilation make self-improvement safe to allow*
  (by routing it through existing code-review machinery) rather than a new
  capability specific to prompts.

### Claim 9: The article's overall framing is that a production prompt transpiler "reframes prompt engineering as a build-system problem," with prompts needing to be "built, validated, versioned, and deployed" rather than just edited

- **Evidence**: Stated as the article's conclusion, generalizing from the
  specific mechanisms described (templating, transpilation, validation,
  drift checking, progressive disclosure, PR-gated updates) to a single
  framing claim about how prompt engineering should be categorized as a
  discipline.
- **Confidence**: emerging (a framing/positioning claim; not independently
  falsifiable in the way the technical claims above are, but consistent
  with and summarizing everything else demonstrated in the post)
- **Quote**: "A production prompt transpiler reframes prompt engineering as
  a build-system problem." ... "As AI agents become deeply integrated into
  critical workflows, their instruction layers need the same reliability
  standards we demand of our software. Prompts shouldn't just be edited,
  they should be built, validated, versioned, and deployed."
- **Our assessment**: This framing claim is the post's real thesis, and it
  is corroborated — independently and with more implementation depth — by
  the gh-aw compilation model already in the corpus: gh-aw treats agentic
  workflow markdown as source that is compiled (`gh aw compile`) into a
  deployable artifact (`.lock.yml`) with validation, dependency resolution,
  and a documented runtime/compile-time boundary
  (`docs-ghaw-compilation-process.md` Claims 1, 7). The "prompts as build
  artifacts" framing is not unique to this post; it is an emerging
  cross-organization pattern (Google SRE blog post + GitHub Next's shipped
  gh-aw compiler) for treating agent instructions as compiled software
  rather than static text.

## Concrete Artifacts

### Top-level agent prompt template (Jinja2-style, verbatim)

```
# agents/sre_agent.prompt.md (prompt template file)

{% include "shared/safety.prompt.md" %}
{% include "shared/tool_usage.prompt.md" %}

You are an SRE triage agent operating in the {{ environment }} environment.

{% if allow_remediation %}
You may recommend remediation steps, but destructive actions require human approval.
{% else %}
You may inspect, summarize, and explain the issue, but do not recommend remediation actions.
{% endif %}

{% macro bullet_section(title, items) %}
## {{ title.rstrip() }}
{% for item in items %}
- {{ item.rstrip() }}
{% endfor %}
{% endmacro %}

{{ bullet_section("Required investigation steps", [
"Inspect recent deployment events",
"Check service metrics for latency or error-rate changes",
"Review logs for repeated failure patterns"
]) }}
```
*Source: developers.googleblog.com/building-scalable-ai-agents-with-modular-prompt-transpilation/, fetched directly via curl, decoded from HTML entities (`&quot;` → `"`, `&#x27;` → `'`).*

### Transpiled output (environment="production", allow_remediation=true)

```
You are an SRE triage agent operating in the production environment.

You may recommend remediation steps, but destructive actions require human approval.

## Required investigation steps

- Inspect recent deployment events
- Check service metrics for latency or error-rate changes
- Review logs for repeated failure patterns
```
*Source: same article. Note: this rendered example does not show the
resolved content of the two `{% include %}` directives — see Claim 4's
Our assessment.*

### Three named failure modes of monolithic prompts (verbatim section headings + explanatory text)

```
Obscured blast radius:
"System prompt diffs are harder though. Adding a sentence could have
unintended side effects across the entire agent, which is often hard to
predict or test."

Copy-paste drift:
"This leads to copy-pasting or multiple versions of the same functionality
leading to inconsistencies."

Deferred runtime errors:
"While this helps with authoring, it pushes error detection to runtime.
You might deploy a prompt that only fails when a specific, rarely-used
workflow is triggered because of a missing variable or an invalid import
path."
```
*Source: same article, "Why monolithic prompts break down" section.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 1 (five-phase compilation
    pipeline: parse → construct → resolve → pin → generate) and Claim 7
    (only frontmatter changes require recompilation; markdown body is
    loaded at runtime): both sources treat agent instruction text as
    compiled source that produces a deterministic deployable artifact. This
    Google post states the general architectural rationale ("prompts should
    be built, validated, versioned, and deployed"); gh-aw's compilation
    reference is the working implementation of the same idea for GitHub
    Agentic Workflows, with a named, shipped `gh aw compile` command instead
    of a hypothetical "transpiler."
  - `docs-ghaw-compilation-process.md` Claim 2 (deterministic BFS import
    resolution with cycle detection): this post's Claim 5 (treat each
    prompt fragment as a directed-graph node to catch recursive imports) is
    the same requirement stated abstractly; gh-aw's BFS-with-cycle-detection
    is a concrete, named algorithm doing exactly this for a real compiler.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 5 ("You should
    think of the entire file system as a form of context engineering and
    progressive disclosure"): this post's Claim 7 (compiled base prompt +
    runtime-retrieved skill modules) independently arrives at the same
    progressive-disclosure principle, applied to a structurally different
    mechanism (compile-time template fragments vs. runtime-discovered skill
    folders). See Claim 7's Our assessment for the distinction.
  - `blog-anthropic-large-codebase-best-practices.md` Claim 6 ("lean and
    layered CLAUDE.md," loaded additively): the same "small stable core +
    larger on-demand detail" shape recurs a third time here, applied to a
    third mechanism (CLAUDE.md directory hierarchy). Three independent
    sources (this post, Claude Code skills, CLAUDE.md layering) converge on
    the same context-budget shape via three different implementations.

- **Contradicts**: None identified. This post's claims about modular prompt
  architecture do not conflict with any existing corpus source. The paper
  `paper-gloaguen-agentsmd-effectiveness.md` studies a related but distinct
  question — whether AI-*generated* AGENTS.md context files help task
  success (finding: they mostly don't, and increase cost 20–23%) — which is
  not the same claim as this post's (that *manually authored*, modular,
  compiler-validated prompt *templates* reduce engineering failure modes
  like drift and deferred errors). The two sources address different
  layers of the problem (context-file content usefulness vs. prompt-authoring
  infrastructure) and are not in tension; flagging this explicitly so a
  future miner or the Smith doesn't mistake the topical overlap ("prompts,"
  "context files") for a contradiction. No contradiction issue filed.

- **Extends**: `docs-ghaw-templating-reference.md` (conditional markdown
  `{{#if}}...{{/if}}` and runtime `{{#runtime-import}}` mechanisms): gh-aw's
  templating reference documents a working, shipped templating system for
  agentic workflow prompts with its own conditional and import syntax
  (Handlebars-flavored, not Jinja2) and explicit security controls (path
  restriction, expression rejection) that this Google post's Jinja2-style
  example does not address at all — the post never discusses what happens
  if included/imported prompt content is untrusted or attacker-influenced.
  This is a gap worth noting: gh-aw's templating reference treats "what if
  imported content contains a malicious expression" as a first-class
  security question (Claim 5 of that note); this post treats template
  composition purely as a maintainability mechanism with no security
  framing.

- **Novel**:
  - **"Transpiler" as the specific term for a prompt-template compiler**: no
    existing corpus source uses this term for prompt/instruction
    compilation. gh-aw uses "compile"/"compiler"; this is the first use of
    "transpiler" specifically for prompt template resolution.
  - **The concrete Jinja2-syntax worked example** (Claim 3, Concrete
    Artifacts): no existing corpus source shows a complete, syntactically
    valid Jinja2 prompt template with `include`, `if/else`, and `macro`
    used together, nor a paired before/after transpiled-output example.
  - **"Golden file" terminology applied to compiled prompts** (Claim 6): no
    existing corpus source names the CI drift-check pattern for prompts
    specifically as a "golden file" comparison, though the underlying
    concept (regenerate-and-diff) is structurally similar to gh-aw's
    frontmatter/lock-file compilation model.
  - **Agent-authored prompt updates framed explicitly as "not real-time
    mutation, but a proposed code change"** (Claim 8): while other corpus
    sources describe agents proposing code changes generally, this is the
    first source to state this principle specifically for an agent's *own
    instruction layer*, with the explicit contrast to real-time
    self-modification as the safety property.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Prompt Composition and Templating**:
  The guide currently documents CLAUDE.md layering (root + subdirectory,
  additive loading) and Claude Code skill folders (runtime-discovered,
  progressive disclosure) as the two primary context-modularity mechanisms.
  This source adds a third, distinct pattern — compile-time prompt
  templates resolved by a transpiler with build-time validation — that is
  not yet represented in the corpus. Recommend adding a "Prompt Templates as
  Build Artifacts" subsection introducing the three failure modes (Claim 1)
  as the motivating problem and the transpiler pipeline (Claims 2–4) as one
  answer, explicitly cross-referenced against gh-aw's shipped compilation
  model (`docs-ghaw-compilation-process.md`) as the more concrete,
  production-verified version of the same idea. Caveat prominently: this
  source describes an architectural pattern with one illustrative example,
  not a named tool or measured production outcome — weight it accordingly
  relative to the gh-aw reference notes, which document a shipped compiler.

- **Chapter 02 (Harness Engineering) — CI/CD for Prompts**: Add "golden
  file" drift checking (Claim 6) as a low-effort, adoptable CI pattern for
  any team with a templated or generated prompt pipeline, independent of
  whether they build a full transpiler: regenerate the compiled prompt from
  source in CI and fail the build if it differs from the committed
  artifact. This is a simpler, standalone recommendation extractable from
  the larger architecture.

- **Chapter 02 (Harness Engineering) — Progressive Disclosure as a Named
  Cross-Mechanism Principle**: The guide should name progressive disclosure
  (small stable core + on-demand detail) as a general context-engineering
  principle that recurs across at least three different mechanisms in the
  corpus: CLAUDE.md layering, Claude Code skill folders, and this post's
  compiled-base-prompt-plus-retrieved-skill-modules pattern. Citing all
  three sources together strengthens the principle's standing beyond any
  single implementation.

- **Chapter 03 (Verification) — Agent-Authored Instruction Changes**: Add
  Claim 8's governance pattern (agent proposes a PR to its own instruction
  layer; transpiler validates; human reviews and runs evals before merge)
  as a named safety pattern for any team considering allowing agents to
  modify their own prompts/skills. Frame explicitly as "the safety property
  is not that self-modification doesn't happen, but that it never bypasses
  the same review gate as any other code change" — and note that this
  source frames it as a theoretical capability the architecture unlocks,
  not a demonstrated production practice.

## Extraction Notes

- The article was fetched twice: once via the WebFetch tool (which returned
  a paraphrased, lightly-reworded summary — noticeably not verbatim, e.g.
  "When initially constructing an AI agent..." vs. the source's actual
  "When you're first building an AI agent..."), and once via a direct
  `curl` request to the source URL, followed by stripping `<script>`/
  `<style>` tags and HTML markup with a Python regex to recover the raw
  visible page text. All quotes in this note were taken from the direct
  `curl` fetch and verified character-for-character (including HTML entity
  decoding for `&quot;`, `&#x27;`, and the curly apostrophe `’`) against
  that raw text, per MINER.md §2a — the WebFetch-only pass was discarded as
  a source for quotes since it paraphrased rather than reproduced the
  article verbatim.
- The page's embedded JSON-LD (`<script type="application/ld+json">`)
  confirmed the title, author name ("Simerus Mahesh"), and `datePublished`
  ("2026-07-16") independently of the visible page text.
- No sub-pages were followed. The article is a single self-contained post
  with no linked documentation, code repository, or companion piece; the
  "Related Posts" footer links are unrelated Google Developers Blog
  articles (ADK, Agent Development Kit announcements, a separate Grounding
  with Parallel Web Search post already in the corpus as
  `blog-google-parallel-web-search-grounding.md`), not extensions of this
  article's content.
- Confidence is set to `emerging` overall: the architectural reasoning is
  sound and independently corroborated by a more concrete, shipped
  implementation (`docs-ghaw-compilation-process.md`), but this specific
  source is a single practitioner's blog post with one illustrative code
  example and no named tool, benchmark, or production evidence of its own.
  Individual claims are graded `anecdotal` where no evidence beyond
  assertion is given (Claims 1, 5, 6, 7, 8) and `emerging` where a concrete
  worked example is present (Claims 2, 3, 4, 9).
- No contradiction was found requiring a filed issue; the topical overlap
  with `paper-gloaguen-agentsmd-effectiveness.md` is addressed explicitly
  under Cross-References → Contradicts to prevent it being mistaken for one
  later.
