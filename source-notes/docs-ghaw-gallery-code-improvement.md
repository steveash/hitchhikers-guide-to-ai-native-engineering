---
source_url: https://github.github.com/gh-aw/gallery/code-improvement
source_type: docs
title: "GitHub Agentic Workflows Gallery: Automated Code Improvement"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3032"
---

# GitHub Agentic Workflows Gallery: Automated Code Improvement

> A short gallery page presenting the "Code Simplifier" daily-schedule
> workflow as the platform's worked example for agent-driven, behavior-
> preserving code simplification — draft-PR-only, gated on the repo's own
> formatter/tests/linter/build. The gallery page itself is thin (one YAML
> snippet, three short paragraphs), but its "portable adaptation of the
> Code Simplifier workflow" links directly to the full source workflow in
> `githubnext/agentics`, which contains substantially richer safety
> configuration and prompt engineering than the gallery page shows —
> and which the platform's own wizard corpus data (`docs-ghaw-wizard.md`)
> names as a specific anti-pattern for its archetype.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Gallery" section — a
  worked-example page one level more concrete than the `examples/` pages,
  per the framing already established in `docs-ghaw-multi-repo-feature-sync.md`'s
  Source Context). The page links out to the full, non-portable source
  workflow it adapts, hosted in a separate GitHub Next repository
  (`githubnext/agentics`).
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team and doc set behind every other `docs-ghaw-*` note in this
  corpus. The gallery YAML and the linked `agentics/code-simplifier.md`
  source file are both authoritative, shipped platform artifacts, not
  third-party commentary.
- **Scope**: Covers exactly one worked example — a daily-scheduled agent
  that reviews the last 24 hours of production code changes and opens a
  draft PR with a single, focused, behavior-preserving simplification. Does
  NOT cover: the Safe Outputs specification in depth (see
  `docs-ghaw-safe-outputs-specification.md`), the static protected-files
  threat-detection layer in depth (see `docs-ghaw-threat-detection.md`), or
  the network egress/sandbox model in depth (see `docs-ghaw-network-reference.md`).
  The gallery page's own frontmatter snippet is deliberately minimal (three
  fields: `on`, `permissions`, `safe-outputs`); the full operational
  configuration lives only in the linked source workflow, which this note
  also extracts (see Extraction Notes).

## Extracted Claims

### Claim 1: The workflow's task is framed as reviewing all production code changed in the last 24 hours for one clear, behavior-preserving simplification opportunity, triggered on a daily schedule
- **Evidence**: The gallery page's opening summary and the reproduced workflow prompt both state this framing; the frontmatter's `on:` block sets `schedule: daily`.
- **Confidence**: settled (first-party description of a shipped starter workflow, corroborated by the reproduced YAML)
- **Quote**: "Automated code improvement with GitHub Agentic Workflows means reviewing recent production-code changes for unnecessary complexity and proposing a small, behavior-preserving simplification."
- **Our assessment**: The "one clear opportunity" framing (echoed in the workflow prompt itself: "Look for one clear opportunity to remove needless branching, duplication, dead local abstractions, or confusing naming") is a deliberate scope limiter — the agent is not asked to refactor broadly, only to find a single, defensible improvement per run. This is a narrower mandate than a general "code review" or "linter" agent, and maps to the same scope-control instinct already documented for trigger filtering in `docs-ghaw-deterministic-agentic-patterns.md` (narrow the agent's job to reduce risk and review burden), applied here to task scope rather than trigger scope.

### Claim 2: The workflow opens a draft pull request rather than committing directly to the default branch, keeping the human in the loop before any simplification lands
- **Evidence**: The frontmatter's `safe-outputs.create-pull-request.draft: true` field, plus explicit prose stating the design intent.
- **Confidence**: settled (shown directly in the reproduced YAML and stated in prose)
- **Quote**: "The workflow opens a draft pull request rather than changing the default branch directly."
- **Our assessment**: This corroborates the draft-PR-as-trust-dial pattern already documented in `docs-ghaw-multi-repo-feature-sync.md` Claim 4 (push-triggered, higher-frequency sync workflows default to `draft: true`; only the rarer, well-defined `release`-triggered variant uses `draft: false`). A daily-scheduled, autonomously-triggered code-modification workflow is exactly the higher-frequency, more-judgment-required case that pattern predicts should default to draft — this page is a second, independent confirmation of that trust-dial logic for a different safe-output use case (code changes, not cross-repo sync).

### Claim 3: The agent is required to run the repository's own formatter, test suite, linter, and build before it may open the pull request, and must describe which checks passed in the PR body
- **Evidence**: The gallery page's prose states this validation gate; the underlying source workflow's "Phase 3: Validate Changes" section spells out the same four checks with adaptive shell commands per language/build system (see Concrete Artifacts).
- **Confidence**: settled (stated directly on the gallery page and elaborated in the linked source workflow)
- **Quote**: "Run the repository's formatter, tests, linter, and build. Open a draft pull request describing why the result is simpler and which checks passed."
- **Our assessment**: This is a concrete instance of self-validation before a write-adjacent safe output — the agent doesn't just propose a diff, it exercises the project's own quality gates first and reports the outcome as evidence in the PR description. The underlying source workflow (Concrete Artifacts, "Phase 4.1: Determine If PR Is Needed") makes this a hard gate: a PR is only created if tests pass, linting is clean, and the build succeeds (or none of those exist) — not merely "recommended." No existing source note documents an agent running its own target repo's full build/test/lint pipeline as a precondition for a safe-output PR; this is closer to a CI-gate-before-safe-output pattern than anything in `docs-ghaw-automated-pr-review.md` (which reviews a diff but does not itself run the target repo's build).

### Claim 4: Keeping project-specific build and test commands in `AGENTS.md` is the documented interface that lets the agent validate its own proposed changes using the repository's normal contribution process
- **Evidence**: The gallery page's closing guidance sentence.
- **Confidence**: settled (explicit first-party recommendation)
- **Quote**: "Keep project-specific build and test commands in AGENTS.md so the agent can validate its proposal using the repository's normal contribution process."
- **Our assessment**: This gives `AGENTS.md` a specific, load-bearing role beyond general behavioral guidance: it is the documented lookup point for *how to validate a change*, not just *how to behave*. This is a narrower and more mechanical claim than the general "contribution guidelines" framing in the underlying source workflow's own instructions ("Check for style guides, coding conventions, or contribution guidelines... Look for language-specific conventions (e.g., STYLE.md, CONTRIBUTING.md, README.md)") — the gallery page specifically names `AGENTS.md` as the build/test command source, while the source workflow's own prompt text (Concrete Artifacts) never mentions `AGENTS.md` by name and instead falls back to generic per-language command guesses (`make test`, `npm test`, `pytest`, etc.). This is a discrepancy worth flagging: the gallery page's stated best practice (put commands in `AGENTS.md`) is not actually wired into the agent prompt it links to as its source (see Claim 6 and Extraction Notes).

### Claim 5: The workflow exits without creating a pull request when no code changed in the last 24 hours or no worthwhile simplification exists — it does not force a PR on every scheduled run
- **Evidence**: The gallery page's Key Features list and prose; the underlying source workflow spells out explicit exit conditions and required status-message text for both no-op cases (see Concrete Artifacts).
- **Confidence**: settled (stated on the gallery page; elaborated with verbatim status messages in the linked source workflow)
- **Quote**: "Do nothing when no worthwhile simplification exists."
- **Our assessment**: This is a "silence is a valid, expected output" design — a scheduled agent workflow that produces no side effect on most runs, rather than being pressured to always find something to change. That matters for review fatigue: a daily code-improvement bot that always opens a PR (whether or not there's a real improvement) trains reviewers to ignore it. The source workflow's explicit "Exit Conditions" list (Concrete Artifacts) generalizes this beyond "nothing changed" to also cover "tests fail after changes," "build fails after changes," and "changes are too risky or complex" — i.e., the no-op path is also the fallback when the agent's own validation (Claim 3) fails, not just when there's nothing to simplify.

### Claim 6: The full, non-portable source workflow (`githubnext/agentics/code-simplifier.md`) that this gallery page adapts carries materially more safety and scoping configuration than the gallery page's own three-field frontmatter snippet shows — including a same-day PR expiry, a fallback-to-issue policy on protected files, deduplication against already-open code-simplifier PRs, and a network egress allowlist restricted to a fixed set of language-ecosystem ranges
- **Evidence**: `githubnext/agentics/code-simplifier.md` frontmatter (fetched directly, linked from the gallery page as "Code Simplifier source workflow"): `safe-outputs.create-pull-request.expires: 1d`; `safe-outputs.create-pull-request.protected-files: fallback-to-issue`; `on.skip-if-match: 'is:pr is:open in:title "[code-simplifier]"'`; `network.allowed: [defaults, dotnet, node, python, rust, java]`; `permissions: read-all`. None of these five fields appear in the gallery page's own reproduced YAML snippet, which shows only `on: schedule: daily`, three read-only `permissions` keys, and `safe-outputs.create-pull-request.title-prefix`/`draft`.
- **Confidence**: settled (verbatim frontmatter from the linked source file, directly fetched)
- **Quote**: (no direct prose quote from either page states this comparison; the frontmatter values themselves are verbatim — see Concrete Artifacts for both blocks side by side)
- **Our assessment**: This is a meaningful gap between the "recipe" shown to readers and the actual shipped configuration it claims to adapt. `expires: 1d` means an unmerged code-simplifier PR self-closes after one day — a stronger staleness control than the gallery page's silence on expiry would suggest. `protected-files: fallback-to-issue` (per `docs-ghaw-threat-detection.md` Claim 11, one of three named protection policies) means if the agent's simplification touches a supply-chain file (dependency manifest, CI workflow, or agent instruction file per that note's Claim 10), the platform routes it to a human-reviewed issue instead of blocking outright or allowing it through — a concrete, real-world usage example of that policy that the threat-detection reference note itself didn't have. `skip-if-match:` on an open code-simplifier PR title is the same dedup idiom named abstractly in `docs-ghaw-deterministic-agentic-patterns.md` Claim 8, applied here to prevent the daily schedule from piling up duplicate simplification PRs while one is still open. `permissions: read-all` is broader than the three explicit read scopes (`contents`, `issues`, `pull-requests`) the gallery page shows — readers copying only the gallery snippet get a narrower, arguably safer permission set than the "real" workflow uses, which is a reasonable simplification for a teaching example but should not be assumed equivalent for production adoption. For Ch03 (Safety and Verification): if the guide cites this gallery page, cite the fuller source-workflow configuration alongside it, since the safety-relevant fields live in the linked file, not the page readers land on first.

### Claim 7: The underlying source workflow's simplification prompt gives an explicit, named style rule against nested ternary operators, instructing the agent to prefer switch statements or if/else chains, and to choose explicit code over compact code
- **Evidence**: `githubnext/agentics/code-simplifier.md`, "2.2 Simplification Principles" → "2. Enhance Clarity" bullet list.
- **Confidence**: settled (verbatim instruction text from the linked source file)
- **Quote**: "**IMPORTANT**: Avoid nested ternary operators - prefer switch statements or if/else chains"
- **Our assessment**: This is a specific, actionable prompt-engineering rule not present anywhere in the corpus's existing coverage of code-quality or review-agent prompts (`docs-ghaw-automated-pr-review.md` Claim 7's anti-noise instructions cover review comments, not code-authoring style rules). It's notable as a rule the platform team apparently found necessary to call out explicitly ("IMPORTANT") rather than leave to the model's general judgment — a signal that unconstrained "simplify this code" prompts tend to produce nested-ternary-style compactions that the team considers a regression, not an improvement, even though a model might score such compactions as "simpler" by a naive line-count metric.

### Claim 8: The source workflow's prompt explicitly warns against over-simplification, naming six specific failure modes the agent must avoid even while simplifying
- **Evidence**: `githubnext/agentics/code-simplifier.md`, "2.2 Simplification Principles" → "4. Maintain Balance" section, which lists six named risks of over-simplification.
- **Confidence**: settled (verbatim instruction text from the linked source file)
- **Quote**: "Avoid over-simplification that could:\n- Reduce code clarity or maintainability\n- Create overly clever solutions that are hard to understand\n- Combine too many concerns into single functions\n- Remove helpful abstractions that improve code organization\n- Prioritize \"fewer lines\" over readability\n- Make the code harder to debug or extend"
- **Our assessment**: This is a direct, named countermeasure against a known LLM code-editing failure mode — over-aggressive compaction that reduces line count or apparent complexity while making the code harder to maintain. It pairs with Claim 7 (the anti-ternary rule) as evidence that the platform team iterated on this prompt specifically to correct for a tendency toward "clever but worse" simplifications, rather than trusting a generic "simplify this" instruction. This is new, specific content for the corpus's coverage of code-quality automation prompts — more concrete than the general "behavior-preserving" framing on the gallery page itself.

### Claim 9: The source workflow requires the agent to produce a structured PR description with named sections — a per-file changelist, a categorized improvements list, links back to the specific PRs/commits the changes were based on, and an explicit test/lint/build status checklist
- **Evidence**: `githubnext/agentics/code-simplifier.md`, "Phase 4.2: Generate PR Description", which specifies a markdown template with the sections "Files Simplified," "Improvements Made" (three named subcategories: Reduced Complexity, Enhanced Clarity, Applied Project Standards), "Changes Based On," "Testing," and "Review Focus."
- **Confidence**: settled (verbatim template from the linked source file — see Concrete Artifacts)
- **Quote**: "### Changes Based On\n\nRecent changes from:\n- #[PR_NUMBER] - [PR title]\n- Commit [SHORT_SHA] - [Commit message]"
- **Our assessment**: The "Changes Based On" section is a provenance mechanism distinct from `tracker-id` (per `docs-ghaw-frontmatter-full-reference.md` Claim 9, which tags created assets with a workflow identifier) — here the provenance links the *simplification PR* back to the *specific upstream PRs/commits* that introduced the code being simplified, giving a human reviewer a direct trail from "why does this file look different" back to "what changed here yesterday." This is a reusable PR-description template pattern for any agent whose job is to react to recent changes elsewhere in the repo, not just for code simplification specifically.

## Concrete Artifacts

### Gallery page's own reproduced workflow snippet — `.github/workflows/code-simplifier.md`

Reconstructed from the raw HTML of the gallery page (`<pre>` block under the "Code Simplifier" heading), preserving the source's line breaks and indentation exactly as rendered.

```yaml
---
on:
  schedule: daily

permissions:
  contents: read
  issues: read
  pull-requests: read

safe-outputs:
  create-pull-request:
    title-prefix: "[code-simplifier] "
    draft: true
---
# Code Simplifier
Review production code changed in the last 24 hours. Look for one clear opportunity to remove needless branching, duplication, dead local abstractions, or confusing naming while preserving behavior and public interfaces exactly.
Make only a focused change with a measurable readability or maintainability benefit. Run the repository's formatter, tests, linter, and build. Open a draft pull request describing why the result is simpler and which checks passed. Do nothing when no worthwhile simplification exists.
```

*Source: `github.github.com/gh-aw/gallery/code-improvement` (gallery page)*

### Linked source workflow's full frontmatter — `githubnext/agentics/workflows/code-simplifier.md`

Fetched directly via `raw.githubusercontent.com/githubnext/agentics/main/workflows/code-simplifier.md`; reproduced verbatim.

```yaml
---
name: Code Simplifier
description: Analyzes recently modified code and creates pull requests with simplifications that improve clarity, consistency, and maintainability while preserving functionality
on:
  schedule: daily
  skip-if-match: 'is:pr is:open in:title "[code-simplifier]"'

network:
  allowed:
  - defaults
  - dotnet
  - node
  - python
  - rust
  - java

permissions: read-all

tracker-id: code-simplifier

imports:
  - shared/formatting.md
  - shared/reporting.md

safe-outputs:
  create-pull-request:
    title-prefix: "[code-simplifier] "
    labels: [refactoring, code-quality, automation]
    expires: 1d
    protected-files: fallback-to-issue

tools:
  github:
    toolsets: [default]

timeout-minutes: 30
---
```

*Source: `githubnext/agentics/workflows/code-simplifier.md`, linked from the gallery page as "Code Simplifier source workflow" / "Code Simplifier workflow"*

### Anti-ternary and over-simplification guardrails (source workflow prompt body)

```markdown
#### 2. Enhance Clarity
- Reduce unnecessary complexity and nesting
- Eliminate redundant code and abstractions
- Improve readability through clear variable and function names
- Consolidate related logic
- Remove unnecessary comments that describe obvious code
- **IMPORTANT**: Avoid nested ternary operators - prefer switch statements or if/else chains
- Choose clarity over brevity - explicit code is often better than compact code

#### 4. Maintain Balance
Avoid over-simplification that could:
- Reduce code clarity or maintainability
- Create overly clever solutions that are hard to understand
- Combine too many concerns into single functions
- Remove helpful abstractions that improve code organization
- Prioritize "fewer lines" over readability
- Make the code harder to debug or extend
```

*Source: `githubnext/agentics/workflows/code-simplifier.md`, "Phase 2: Analyze and Simplify Code" → "2.2 Simplification Principles"*

### PR description template (source workflow prompt body)

```markdown
## Code Simplification - [Date]

This PR simplifies recently modified code to improve clarity, consistency, and maintainability while preserving all functionality.

### Files Simplified

- `path/to/file1.ext` - [Brief description of improvements]
- `path/to/file2.ext` - [Brief description of improvements]

### Improvements Made

1. **Reduced Complexity**
   - [Specific example]

2. **Enhanced Clarity**
   - [Specific example]

3. **Applied Project Standards**
   - [Specific example]

### Changes Based On

Recent changes from:
- #[PR_NUMBER] - [PR title]
- Commit [SHORT_SHA] - [Commit message]

### Testing

- ✅ All tests pass (or indicate if no tests exist)
- ✅ Linting passes (or indicate if no linter configured)
- ✅ Build succeeds (or indicate if no build step)
- ✅ No functional changes - behavior is identical

### Review Focus

Please verify:
- Functionality is preserved
- Simplifications improve code quality
- Changes align with project conventions
- No unintended side effects
```

*Source: `githubnext/agentics/workflows/code-simplifier.md`, "Phase 4: Create Pull Request" → "4.2 Generate PR Description"*

### Exit conditions and required status messages (source workflow prompt body)

```markdown
If **no files were changed in the last 24 hours**, exit gracefully without creating a PR:

✅ No code changes detected in the last 24 hours.
Code simplifier has nothing to process today.

If no improvements were made or changes broke tests, exit gracefully:

✅ Code analyzed from last 24 hours.
No simplifications needed - code already meets quality standards.

Exit gracefully without creating a PR if:
- No code was changed in the last 24 hours
- No simplifications are beneficial
- Tests fail after changes
- Build fails after changes
- Changes are too risky or complex
```

*Source: `githubnext/agentics/workflows/code-simplifier.md`, "Phase 1.3: Determine Scope" and "Important Guidelines → Exit Conditions"*

### The "Code Improvement" archetype's own anti-pattern list names this workflow by filename

Reproduced from `docs-ghaw-wizard.md` Claim 4's Concrete Artifacts (`patterns/archetypes/code-improvement.json` in `githubnext/gh-aw-wizard`), quoted verbatim from that source note (not re-fetched independently for this note):

```json
"anti_patterns": ["ci-doctor", "ci-doctor", "autofix-ci", "code-simplifier", "pr-fix"]
```

*Source: as cited in `docs-ghaw-wizard.md`, Claim 4 — see Cross-References below for why this is flagged as a contradiction rather than folded silently into the claims above.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-feature-sync.md` Claim 4 (`draft` as a per-pattern trust dial — push-triggered/frequent workflows default to `draft: true`, well-defined/rare triggers default to `draft: false`): Claim 2 above is a second, independent worked example of the same logic — a daily-scheduled, autonomously-triggered workflow defaults to draft.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 8 (`skip-if-match:` / `skip-if-no-match:` as the declarative dedup mechanism, producing skipped rather than failed runs): Claim 6 above's `skip-if-match: 'is:pr is:open in:title "[code-simplifier]"'` is a concrete, real-world instance of exactly this directive, previously only documented abstractly.
  - `docs-ghaw-threat-detection.md` Claim 11 (three protected-file policies: `blocked`, `allowed`, `fallback-to-issue`): Claim 6 above's `protected-files: fallback-to-issue` is the first corpus example of a real workflow actually configuring this specific policy value, rather than the reference page's abstract description of the three options.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 9 (`tracker-id` tags all workflow-created assets with a durable identifier for lifecycle management): the source workflow's `tracker-id: code-simplifier` (Concrete Artifacts) is a real usage example of this field.

- **Contradicts**:
  - **Filed as new issue #3084**: `docs-ghaw-wizard.md` Claims 3–4 report that the wizard's own empirical corpus (518 repos / 819 workflows) measures the "code-improvement" archetype at a 0.37 success rate (n=76) — one of the lower rates among archetypes with meaningful sample size — and that `patterns/archetypes/code-improvement.json`'s `anti_patterns` list names `code-simplifier` by filename, alongside `ci-doctor`, `autofix-ci`, and `pr-fix`, as a pattern the wizard's own data associates with low real-world success. This gallery page, from the same GitHub Next organization, presents the "Code Simplifier" workflow without qualification as the platform's official worked example for automated code improvement — no caveat about the archetype's measured 37% success rate or its own name appearing in the anti-pattern list. Both sources are first-party GitHub Next material and both bear directly on the same question — "should practitioners adopt the Code Simplifier pattern as shown?" — with opposing implications (adopt as a recommended example vs. treat as an empirically low-success anti-pattern to avoid cloning as-is). This is not a difference in scope or context (e.g., "good for small repos, bad for large ones") — it is the same workflow, evaluated by the same organization's own data, receiving opposite treatment in two different documentation surfaces. No verdict is picked in this note; see the filed contradiction issue for the full Side A/Side B writeup.

- **Extends**:
  - `docs-ghaw-network-reference.md` Claim 6 (unrecognized ecosystem identifiers in `network.allowed` trigger compile-time validation errors): the source workflow's `network.allowed: [defaults, dotnet, node, python, rust, java]` (Concrete Artifacts) is a concrete, real-world example of an ecosystem-identifier allowlist restricting a validation-heavy workflow (one that needs to run installs/builds across multiple language toolchains) to a fixed, named set of package-manager egress ranges rather than an unrestricted or single-ecosystem allowlist.
  - `docs-ghaw-automated-pr-review.md` Claim 7 (anti-noise review-instruction pattern: no restating unchanged code, no style-only feedback): Claims 7–8 above extend the corpus's coverage of "guardrail" prompt instructions from the review-comment domain into the code-authoring domain — explicit named rules (no nested ternaries, six over-simplification failure modes) constraining what an agent is allowed to produce, not just what it's allowed to say in review comments.
  - `docs-ghaw-github-tools.md` Claim 1 (GitHub Tools included by default via the five default toolsets): the source workflow's `tools.github.toolsets: [default]` (Concrete Artifacts) is a real usage example of relying on that default rather than enumerating specific toolsets.

- **Novel**:
  - The explicit anti-nested-ternary style rule and the six-item "Maintain Balance" over-simplification guardrail list (Claims 7–8) are new to the corpus — no existing source note documents specific code-style constraints embedded in an agent's code-authoring prompt.
  - The structured PR-description template with a "Changes Based On" provenance section linking a simplification PR back to the specific upstream PRs/commits that motivated it (Claim 9) is a new, reusable pattern not documented elsewhere.
  - The gap between what a gallery/teaching page shows (three-field frontmatter) and what the linked "real" source workflow actually configures (Claim 6: five additional safety/scoping fields) is a new observation for the corpus — prior gallery-page notes (`docs-ghaw-multi-repo-feature-sync.md`) flagged gaps in PAT scope guidance, but this is the first case of a gallery page's own reproduced YAML omitting fields present in the workflow it explicitly links to as its source.
  - The `AGENTS.md`-as-build/test-command-interface recommendation (Claim 4) is new, though see Claim 4's own assessment for why it isn't actually reflected in the linked source workflow's prompt text.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Cite Claim 3 (mandatory formatter/test/lint/build gate before PR creation) and Claim 5 (explicit no-op exit conditions including "tests fail after changes" and "changes are too risky or complex") as a concrete instance of a self-validating agent pattern — the agent doesn't just propose a change, it must exercise the target repo's own quality gates and only proceeds if they pass. Pair this with Claim 6's fuller safety configuration (`expires: 1d`, `protected-files: fallback-to-issue`, `skip-if-match` dedup) if the guide cites this example, since those fields are load-bearing but absent from the page's own reproduced snippet.
- **Chapter 03 (Safety and Verification) — contradiction flag**: Do not cite the Code Simplifier workflow as an unqualified "recommended pattern" without also surfacing the filed contradiction (measured 0.37 success rate and its own inclusion in the code-improvement archetype's anti-pattern list, per `docs-ghaw-wizard.md`). If the guide references this gallery page, the Smith should treat this as a **Debated** pairing per the contradiction-handling convention, not silently endorse the gallery framing.
- **Chapter 02 (Harness Engineering)**: Add the anti-nested-ternary rule and the six-item over-simplification guardrail list (Claims 7–8) as a concrete, reusable example of the kind of specific, named constraints that keep a "simplify this code" prompt from producing worse code — useful anywhere the guide discusses writing constraints into code-authoring agent prompts, not just for this specific workflow.
- **Chapter 02 (Harness Engineering)**: If the guide recommends `AGENTS.md` as a build/test command reference for agents (Claim 4), note the discrepancy documented in Claim 4's assessment — the gallery page states this practice, but the actual linked source workflow's prompt does not reference `AGENTS.md` and instead falls back to guessing per-language commands. The recommendation is sound advice but is not itself proof that the shipped example follows it.

## Extraction Notes

1. **WebFetch summary vs. raw HTML**: An initial WebFetch pass on the gallery page returned a plausible-looking summary with invented section headings ("## Overview", "## Workflow Configuration", "## Key Features") that do not appear on the actual page — the same failure mode already documented in `docs-ghaw-automated-pr-review.md`'s Extraction Notes for this documentation platform (an Astro/Starlight SPA). I discarded that summary and re-extracted by downloading the raw HTML directly (`curl`) and parsing the `sl-markdown-content` container and its `<pre>` code block by hand, preserving the exact line breaks and indentation of the reproduced YAML. All quotes in this note are copied from that raw extraction, not from the WebFetch summary.
2. **Followed the linked source workflow**: The gallery page names itself a "portable adaptation" of the "Code Simplifier workflow" and links twice to `https://github.com/githubnext/agentics/blob/main/workflows/code-simplifier.md`. Given MINER.md §1's instruction to follow up to 5 substantive linked pages, and that this link is the actual, non-adapted implementation the gallery page is teaching from, I fetched it directly via `raw.githubusercontent.com` and read it in full (308 lines). This is the source of Claims 6–9 and roughly half of this note's content — without following it, the note would only cover the gallery page's three short paragraphs and one minimal YAML snippet, which would fall well short of MINER.md's "read deeply" bar.
3. **Other linked pages not followed**: The gallery page's "Learn More" section also links to `/gh-aw/reference/safe-outputs-pull-requests/` and `/gh-aw/setup/creating-workflows/`. Both are general platform reference pages already covered by existing corpus notes (the safe-outputs pull-request mechanics are covered across `docs-ghaw-safe-outputs-specification.md` and `docs-ghaw-automated-pr-review.md`; workflow creation is covered by `docs-ghaw-setup-creating-workflows.md`) and are not specific to the code-improvement pattern, so they were not re-fetched for this note.
4. **Contradiction filed**: Per MINER.md §4a, I filed issue #3084 for the disagreement described in Cross-References → Contradicts (this gallery page's unqualified endorsement of the Code Simplifier pattern vs. `docs-ghaw-wizard.md`'s empirical data naming `code-simplifier` as a named anti-pattern with a 0.37 archetype success rate). No verdict is picked in this note.
5. **No publication date**: The gallery page carries no visible publication or last-updated date; `date_published` is left null, consistent with other `docs-ghaw-*` notes in this corpus. `confidence_overall` is set to `emerging` rather than `settled`: the configuration and prompt claims themselves are settled first-party facts, but the overall pattern's real-world effectiveness is actively contradicted by the platform's own corpus data (see Contradicts above), which keeps the note as a whole from being "settled" guidance.
