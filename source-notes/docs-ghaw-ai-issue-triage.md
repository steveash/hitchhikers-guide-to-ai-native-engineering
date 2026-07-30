---
source_url: https://github.github.com/gh-aw/guides/ai-issue-triage
source_type: docs
title: "AI issue triage on GitHub"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2330"
---

# AI issue triage on GitHub

> A short first-party gh-aw "Guides" walkthrough of a starter issue-triage workflow —
> triggers on `issues: types: [opened, edited]`, applies an 8-label allowlist (type +
> priority/p0-p2 + duplicate) capped at `max: 4`, posts at most one comment, and gives
> concrete natural-language thresholds for when to apply `duplicate` vs. `needs-info`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Guides" section —
  a task-oriented starter-workflow walkthrough, distinct from the "Patterns" reference
  page for IssueOps in general). The page is short (roughly 250 words plus one YAML/
  Markdown workflow listing).
- **Author credibility**: First-party from GitHub Next / Microsoft Research, the team
  behind the `gh aw` platform and the `githubnext/agentics` starter-workflow repository
  this guide installs from. Authoritative for the exact YAML shown and the install
  command; the page does not report any production usage data or metrics for this
  specific workflow (contrast with `blog-ghaw-issue-pr-mgmt.md`, which reports Issue
  Arborist production metrics for a related but different workflow).
- **Scope**: Covers a single starter workflow — `.github/workflows/issue-triage.md` —
  and its three natural-language tasks: classification/labeling, duplicate detection,
  and clarifying-question requests. Does NOT cover: the underlying two-job permission-
  separation architecture, `steps.sanitized.outputs.text` sanitization mechanics, or
  the general IssueOps trigger taxonomy (all covered in `docs-ghaw-issueops.md`); does
  not report any production metrics, false-positive rate, or duplicate-detection
  accuracy for this workflow.

## Extracted Claims

### Claim 1: AI issue triage in gh-aw means running an agent on every new issue to classify it, set priority labels, detect likely duplicates, and ask for missing details, while keeping the analysis read-only and routing all writes through safe outputs
- **Evidence**: The page's opening definitional paragraph, which frames the whole
  workflow before showing the YAML.
- **Confidence**: settled (first-party definitional statement, directly corroborated
  by the YAML and prompt body shown on the same page)
- **Quote**: "AI issue triage with gh-aw means running an agent whenever a new issue arrives so it can classify the report, set priority labels, detect likely duplicates, and ask for missing details. The workflow stays read-only during analysis, and gh-aw performs the resulting GitHub writes through safe outputs."
- **Our assessment**: This is a compact, four-part definition of what "AI issue triage"
  concretely means on this platform: classify, prioritize, dedupe, and request missing
  info — as opposed to a vaguer claim like "AI triages issues." The "stays read-only /
  writes via safe outputs" clause restates the general Safe Outputs security model
  already documented in `docs-ghaw-issueops.md` Claims 1 and 5, applied specifically to
  the triage use case.

### Claim 2: The starter workflow is installed with `gh aw add-wizard githubnext/agentics/issue-triage`, and is explicitly adapted from workflows published in `githubnext/agentics`
- **Evidence**: The install-instructions sentence immediately following the definition.
- **Confidence**: settled (first-party install command, explicit attribution to a
  named upstream repository)
- **Quote**: "Install the starter with `gh aw add-wizard githubnext/agentics/issue-triage`. The pattern is adapted from the workflows published in githubnext/agentics."
- **Our assessment**: This confirms `githubnext/agentics` as a maintained catalog of
  reference/starter workflows that gh-aw's own documentation draws from and points
  users to — the same repository referenced by name in other corpus notes (e.g.
  `docs-ghaw-dailyops.md`, `docs-ghaw-agentic-ops.md`) as a source of installable
  patterns. This guide is effectively a documentation-side pointer at one specific
  `agentics` workflow rather than a novel pattern invented on this page.

### Claim 3: The starter workflow triggers on both issue creation and issue edits (`types: [opened, edited]`), with the AI job restricted to `contents: read` and `issues: read`
- **Evidence**: YAML frontmatter shown verbatim on the page:
  ```yaml
  on:
    issues:
      types: [opened, edited]
  permissions:
    contents: read
    issues: read
  ```
- **Confidence**: settled (first-party YAML, explicit)
- **Quote**: (from YAML block, reproduced verbatim in Concrete Artifacts)
- **Our assessment**: This is the first corpus source to document `types: [opened,
  edited]` for the `on: issues:` trigger — `docs-ghaw-issueops.md` Claim 1 only shows
  `types: [opened]`. Including `edited` means the triage agent re-runs when an issue
  reporter updates the title or body after filing (e.g. adding reproduction steps in
  response to a `needs-info` comment), which is a meaningfully different re-triage
  behavior than a fire-once-on-creation workflow. The permission set (`contents: read`,
  `issues: read`) is narrower in one respect than the IssueOps note's example
  (`contents: read`, `actions: read`) — this workflow reads issue data (`issues: read`)
  rather than Actions metadata, consistent with a workflow whose job is to read and
  reason about issue content specifically.

### Claim 4: The workflow's label allowlist is `bug, feature, question, needs-info, priority/p0, priority/p1, priority/p2, duplicate`, capped at `max: 4` labels per run
- **Evidence**: YAML `safe-outputs.add-labels` block shown verbatim on the page:
  ```yaml
  safe-outputs:
    add-labels:
      allowed:
        - bug
        - feature
        - question
        - needs-info
        - priority/p0
        - priority/p1
        - priority/p2
        - duplicate
      max: 4
  ```
- **Confidence**: settled (first-party YAML, explicit)
- **Quote**: (from YAML block, reproduced verbatim in Concrete Artifacts)
- **Our assessment**: This allowlist is a concrete, triage-specific instantiation of
  the `add-labels: allowed:` primitive already documented generically in
  `docs-ghaw-issueops.md` Claim 3 (whose example list was `[bug, needs-info,
  enhancement, question, documentation]`). This page's list differs in a notable way:
  it adds a three-tier `priority/p0` / `priority/p1` / `priority/p2` namespace and a
  `duplicate` label, neither of which appear in the IssueOps note's example — this is
  the first corpus source to document a namespaced priority-label taxonomy for an
  agentic triage workflow. `max: 4` (vs. `max: 2` in the IssueOps example) reflects
  that a single triage pass may need to apply both a type label and a priority label
  simultaneously (e.g. `bug` + `priority/p1`), so the bound is set higher than a
  single-purpose labeling workflow would need.

### Claim 5: The workflow allows at most one comment per run (`add-comment: max: 1`)
- **Evidence**: YAML `safe-outputs.add-comment` block shown verbatim on the page:
  ```yaml
  add-comment:
    max: 1
  ```
- **Confidence**: settled (first-party YAML, explicit)
- **Quote**: (from YAML block, reproduced verbatim in Concrete Artifacts)
- **Our assessment**: `max: 1` is stricter than the `max: 3` shown in the IssueOps
  note's `add-comment` example (`docs-ghaw-issueops.md` Claim 2), and the prompt body
  (Claim 6) explains why: the workflow is designed to consolidate all clarifying
  questions into a single comment rather than posting multiple times. This is a
  concrete design choice worth naming explicitly: a triage agent that might otherwise
  comment once per missing field is constrained to batch its questions.

### Claim 6: The workflow's natural-language instructions define exactly three tasks — classify and label, identify likely duplicates among open and recently closed issues, and ask clarifying questions in one comment if required details are missing
- **Evidence**: The Markdown prompt body shown on the page, following the YAML
  frontmatter, under the heading "# Issue Triage Assistant."
- **Confidence**: settled (first-party prompt text, explicit)
- **Quote**: "Review the triggering issue and do three things: 1. Classify the issue by type and priority, then add the matching labels. 2. Identify likely duplicates from existing open and recent closed issues. 3. If required details are missing, ask concise clarifying questions in one comment."
- **Our assessment**: This is the task decomposition for the whole workflow, and it
  maps directly onto the label allowlist (Claim 4): task 1 produces the type + priority
  labels, task 2 produces the `duplicate` label, task 3 produces at most the one
  allowed comment (Claim 5). Notably, duplicate detection here scans "existing open
  and recent closed issues" — i.e., closed issues are still candidates for a duplicate
  match, not just the open backlog. No detail is given on how far back "recent" closed
  issues extends, or what search mechanism (full-text, embeddings, issue search API)
  the agent uses to find candidates.

### Claim 7: The workflow instructs the agent to apply `duplicate` only on a strong match, and to name the matched issue number in the comment
- **Evidence**: Direct guidance sentence in the prompt body, immediately following the
  three-task list.
- **Confidence**: settled (first-party prompt instruction, explicit; no data on how
  often this threshold is met correctly in practice — this is instruction text, not a
  measured precision rate)
- **Quote**: "Use `duplicate` only when the match is strong and include the issue number in the comment."
- **Our assessment**: This is a concrete, actionable confidence threshold written
  directly into the agent's instructions rather than left to model discretion — "strong
  match" plus a mandatory citation of the specific duplicate issue number, which gives
  a human reviewer an immediate way to verify or reject the classification. This is a
  reusable prompt-engineering pattern for any agentic classification task with a
  binary, high-cost-if-wrong label: pair the label with a mandatory justification
  reference (here, an issue number) so the decision is auditable rather than opaque.

### Claim 8: The workflow instructs the agent to apply `needs-info` specifically when reproduction steps, expected behavior, or environment details are missing
- **Evidence**: Direct guidance sentence in the prompt body, immediately following the
  duplicate-detection guidance.
- **Confidence**: settled (first-party prompt instruction, explicit)
- **Quote**: "Use `needs-info` when reproduction steps, expected behavior, or environment details are missing."
- **Our assessment**: This names three specific, checkable fields (repro steps,
  expected behavior, environment) as the criteria for `needs-info`, rather than a vague
  "if the issue is unclear" instruction. This is a concrete bug-report completeness
  rubric baked into the agent prompt — the same three fields that a well-formed bug
  report template would ask a human to fill in — and gives the guide a ready-made
  "minimum viable bug report" checklist attributable to a first-party source.

### Claim 9: Safe outputs validate label names and comment content before posting because the agent has no direct write access to issues, which the page frames as reducing prompt-injection risk
- **Evidence**: The page's closing security-rationale sentence, following the workflow
  listing.
- **Confidence**: emerging (a stated design rationale, not a disclosed red-team result
  or exploit count — contrast with `blog-anthropic-how-contain-claude.md` Claim 11,
  which discloses a specific tested exfiltration-block rate)
- **Quote**: "`add-labels` and `add-comment` matter for security because the agent does not receive direct write access to issues. gh-aw validates label names and comment output before posting, which reduces the risk of prompt injection turning repository analysis into unrestricted writes."
- **Our assessment**: This restates, in triage-specific language, the general Safe
  Outputs permission-separation rationale already documented in `docs-ghaw-issueops.md`
  Claim 5 and `docs-ghaw-how-they-work.md`. The specific framing here — "prompt
  injection turning repository analysis into unrestricted writes" — makes the threat
  model explicit for the triage case: an issue body is attacker-controllable content
  (anyone can file an issue), so a triage agent that read issue text and then had raw
  write access would be a directly exploitable prompt-injection-to-write path. No new
  mitigation mechanism is introduced beyond what IssueOps already documents (label
  allowlisting via `allowed:`, `max:` volume caps); this page just states the rationale
  in the triage context rather than the general one.

## Concrete Artifacts

### Full starter workflow, `.github/workflows/issue-triage.md` (verbatim from page)

```yaml
---
on:
  issues:
    types: [opened, edited]
permissions:
  contents: read
  issues: read
safe-outputs:
  add-labels:
    allowed:
      - bug
      - feature
      - question
      - needs-info
      - priority/p0
      - priority/p1
      - priority/p2
      - duplicate
    max: 4
  add-comment:
    max: 1
---
# Issue Triage Assistant

Review the triggering issue and do three things:
1. Classify the issue by type and priority, then add the matching labels.
2. Identify likely duplicates from existing open and recent closed issues.
3. If required details are missing, ask concise clarifying questions in one comment.

Use `duplicate` only when the match is strong and include the issue number in the
comment. Use `needs-info` when reproduction steps, expected behavior, or environment
details are missing.
```

*Source: https://github.github.com/gh-aw/guides/ai-issue-triage — reproduced verbatim
from the rendered code sample on the page.*

### Install command (from page)

```
gh aw add-wizard githubnext/agentics/issue-triage
```

*Source: gh-aw "AI issue triage on GitHub" guide.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-issueops.md` Claim 1 (`on: issues:` trigger with a read-only AI job)
    and Claim 5 (two-job permission-separation model, Safe Outputs as the only write
    path): this page's opening definition ("stays read-only during analysis... writes
    through safe outputs") and permission block (`contents: read`, `issues: read`) are
    a direct, consistent instantiation of both.
  - `docs-ghaw-issueops.md` Claim 3 (`add-labels: allowed:` bounds the label namespace;
    pair with `max:` for volume control): this page's `allowed:` list plus `max: 4` is
    a second, concrete example of the same primitive applied to a different label set.

- **Contradicts**: None identified. No claim here conflicts with an existing source
  note under matching conditions.

- **Extends**:
  - `docs-ghaw-issueops.md` Claim 1: extends the `on: issues:` trigger documentation
    with a second `types:` configuration — `[opened, edited]` rather than `[opened]`
    alone — showing that a triage workflow may deliberately re-trigger on issue edits
    (e.g. to re-evaluate after a reporter adds missing detail).
  - `docs-ghaw-issueops.md` Claim 3: extends the generic `add-labels: allowed:` /
    `max:` primitive with a concrete, triage-domain label taxonomy (type labels +
    three-tier `priority/p0-p2` namespace + `duplicate`) and a higher `max: 4` bound
    justified by the need to apply both a type and a priority label in one pass.
  - `blog-ghaw-issue-pr-mgmt.md` Claim 1 (Issue Arborist: links related issues into
    sub-issue hierarchies, with production metrics of 77 discussion reports / 18
    parent issues): this is a different workflow with a related but distinct goal.
    Issue Arborist groups related issues into a parent/child structure; this
    ai-issue-triage workflow's duplicate detection instead applies a single
    `duplicate` label pointing at one matched issue number, with no hierarchy created
    and no production metrics reported for this specific workflow. The two are
    complementary triage-adjacent patterns, not the same mechanism under different
    names.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **`types: [opened, edited]` trigger configuration** (Claim 3): no prior corpus
    source documents re-triggering an issue-triage agent on edits, only on creation.
  - **A concrete `priority/p0`–`priority/p2` namespaced label taxonomy** (Claim 4):
    prior label-allowlist examples in the corpus (`docs-ghaw-issueops.md`) use flat,
    unnamespaced labels (`bug, needs-info, enhancement, question, documentation`) with
    no priority dimension.
  - **Explicit natural-language confidence threshold and audit requirement for a
    binary classification label** (Claim 7 — "strong match" + mandatory issue-number
    citation for `duplicate`): no prior source documents this specific prompt-
    engineering pattern of pairing a label with a mandatory justification reference.
  - **A named three-field bug-report completeness rubric baked into an agent prompt**
    (Claim 8 — reproduction steps / expected behavior / environment): new to the
    corpus as an explicit, reusable checklist.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this workflow's YAML (Concrete Artifacts)
  as a complete, minimal worked example of an IssueOps-triggered triage harness — it
  is more concrete than the abstract IssueOps pattern page (`docs-ghaw-issueops.md`)
  because it shows a full, runnable frontmatter + prompt body for one specific task.
  Specifically add the `types: [opened, edited]` trigger option (Claim 3) alongside
  `types: [opened]` as a design choice: re-trigger on edits when the agent should
  re-evaluate after the reporter supplies more information.
- **Chapter 02/03 (Harness Engineering / Safety)**: Add the `priority/p0-p2` +
  `duplicate` label taxonomy (Claim 4) as a second worked example of `add-labels:
  allowed:` + `max:`, showing that the `max:` bound should scale with how many
  independent label dimensions (type, priority) a single triage pass may need to set
  simultaneously.
- **Chapter 03 (Safety and Verification) / prompt-engineering guidance**: Add Claims
  7 and 8 as concrete, reusable prompt patterns: (a) pair any binary/high-cost
  classification label with a mandatory justification reference so the decision is
  auditable (the `duplicate` + issue-number pattern), and (b) define completeness
  criteria for "needs more info" labels as a named checklist (reproduction steps,
  expected behavior, environment) rather than leaving "is this issue clear enough" to
  model discretion.
- **Chapter 05 (Team Adoption / Operations)**: Note the `gh aw add-wizard
  githubnext/agentics/issue-triage` install command (Claim 2) as a low-friction
  starting point for teams wanting to stand up issue triage, cross-referenced against
  the other `githubnext/agentics`-sourced starter workflows already cited elsewhere in
  the corpus (`docs-ghaw-dailyops.md`, `docs-ghaw-agentic-ops.md`).

## Extraction Notes

- The page is short (~250 words of prose plus one YAML/Markdown workflow listing and
  a "Related pages" link list). A first WebFetch pass returned only a summarized
  paraphrase; per MINER.md §2a, all quotes above were instead extracted via `curl` on
  the raw page HTML, parsing the rendered `<pre>`/`ec-line` code-block markup line by
  line to recover the exact YAML/Markdown text (the site is an Astro/Starlight-style
  SPA that syntax-highlights code samples into per-line `<div>` elements). The
  reconstructed workflow file matches the WebFetch paraphrase in substance and is used
  here as the verbatim, authoritative version.
- The page's "Related pages" section links to four other pages: "Run Claude Code in
  GitHub Actions with gh-aw," "Run GitHub Copilot agents in GitHub Actions with
  gh-aw," "IssueOps," and "Quick start." Of these, IssueOps is already covered in
  depth by `docs-ghaw-issueops.md`. The other three were not followed for this note —
  they are general platform-onboarding pages (engine setup, quick start) rather than
  triage-specific content, and following them would extend this note beyond the scope
  of the ai-issue-triage guide itself. If they are not already covered elsewhere in
  the corpus, they may be worth separate site-crawl discovery and their own source
  issues.
- No publication date is shown on the page (typical for this documentation site's
  "Guides" section, consistent with `docs-ghaw-issueops.md`'s Extraction Notes on the
  same point). Content is current as of 2026-07-30.
- `confidence_overall` is set to `emerging` rather than `settled`: while the YAML and
  prompt text are first-party and unambiguous (settled-grade evidence), the page
  reports no production usage, no accuracy/precision data for duplicate detection or
  classification, and no metrics comparable to `blog-ghaw-issue-pr-mgmt.md`'s Issue
  Arborist numbers — this is a documented starter pattern, not a validated-in-
  production workflow claim.
- Reviewed all `source-notes/` files matching `ghaw`, `cognition`, and `triage` before
  writing Cross-References; re-read `docs-ghaw-issueops.md` and `blog-ghaw-issue-pr-mgmt.md`
  in full and confirmed cited claim numbers by content, not by guessing.
- No contradiction meeting the MINER.md §4a filing bar was found. This source is
  consistent with the Safe Outputs / permission-separation model documented across the
  gh-aw corpus; no contradiction issue filed.
