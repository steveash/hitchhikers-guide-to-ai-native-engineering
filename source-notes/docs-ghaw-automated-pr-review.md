---
source_url: https://github.github.com/gh-aw/guides/automated-pr-review
source_type: docs
title: "Automated AI pull request review on GitHub"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2331"
---

# Automated AI pull request review on GitHub

> A short first-party recipe page showing the complete starter configuration
> for an automated PR-review agent: `pull_request` trigger, read-only
> permissions, and a three-part safe-outputs block (`add-comment`,
> `create-pull-request-review-comment`, `submit-pull-request-review`) —
> the first source note to document `submit-pull-request-review`'s
> `allowed-events` constraint.

## Source Context

- **Type**: docs (a single "Guides" recipe page — a narrow, prescriptive
  starter configuration, not a conceptual overview or full reference).
- **Author credibility**: First-party GitHub Next / Microsoft Research
  documentation for the `gh-aw` platform — the same team and doc set behind
  `docs-ghaw-chatops.md` and `docs-ghaw-how-they-work.md`. Authoritative for
  the exact starter YAML and installation command; the page does not cite
  external metrics or field usage data.
- **Scope**: Covers exactly one starter workflow — automated review on
  `pull_request` open/synchronize — and its safe-outputs configuration. Does
  NOT cover: the `slash_command`/ChatOps-triggered `/review` variant (that's
  `docs-ghaw-chatops.md`), the full Safe Outputs specification's validation
  pipeline (`docs-ghaw-safe-outputs-specification.md`), or engine selection
  (`docs-ghaw-engines-reference.md`). The page is very short: three
  paragraphs, one YAML/markdown code block, and a "Related pages" link list.

## Extracted Claims

### Claim 1: The automated-PR-review pattern runs an agent on every PR update to inspect the diff and return feedback through GitHub-native review surfaces, while keeping the agent itself read-only
- **Evidence**: The page's opening description frames the entire pattern this
  way, before showing the concrete configuration.
- **Confidence**: settled (first-party description of a shipped starter
  workflow)
- **Quote**: "Automated AI pull request review with gh-aw means running an
  agent on each pull request update so it can inspect the diff, identify
  likely defects, and return review feedback in GitHub-native review
  surfaces. The workflow keeps the agent read-only and uses safe outputs for
  the review summary and inline comments."
- **Our assessment**: This restates the general Safe Outputs permission
  model (`docs-ghaw-how-they-work.md` Claim 4: no write access by default;
  Claim 5: Safe Outputs as pre-approved operations) applied specifically to
  the code-review use case. Nothing here is architecturally new — it's the
  same read-agent/write-via-safe-outputs split already documented — but it
  confirms the pattern is offered as an official, packaged starter rather
  than something practitioners must assemble themselves.

### Claim 2: The starter workflow is installed with a single wizard command targeting a pinned workflow spec, `githubnext/agentics/pr-review`
- **Evidence**: The installation instruction is the page's second paragraph,
  a single command with no additional setup steps described.
- **Confidence**: settled
- **Quote**: "Install the starter with `gh aw add-wizard githubnext/agentics/pr-review`."
- **Our assessment**: Consistent with `blog-ghaw-issue-pr-mgmt.md` Claim 7
  (all four of that post's orchestrator workflows install via `gh aw
  add-wizard` from pinned spec URLs) — this is the same installation
  mechanism applied to a fifth, review-specific workflow. Corroborates that
  `add-wizard` + pinned spec URL is the standard distribution model for
  GitHub Next's official starter workflows, not something unique to
  issue/PR-management automation.

### Claim 3: The starter's trigger is scoped to `pull_request` events of type `opened` and `synchronize` only
- **Evidence**: The workflow frontmatter's `on:` block.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; see the YAML in Concrete Artifacts —
  `on: pull_request: types: [opened, synchronize]`)
- **Our assessment**: Scoping to `opened` and `synchronize` (not `reopened`,
  `edited`, `ready_for_review`, etc.) means the agent re-reviews on every new
  commit push to the PR but not on metadata-only changes (title/label edits).
  This is a sensible narrow default: it reviews code changes specifically,
  not PR bookkeeping. No existing source note documents this specific
  `types:` scoping choice for a review workflow.

### Claim 4: The starter workflow runs with read-only `contents` and `pull-requests` permissions — no write scope of any kind
- **Evidence**: The `permissions:` block in the frontmatter.
- **Confidence**: settled
- **Quote**: (from the code sample) `permissions: contents: read
  pull-requests: read`
- **Our assessment**: This is a direct instantiation of the "no write access
  by default" principle (`docs-ghaw-how-they-work.md` Claim 4) and matches
  the read-only permission pair already documented for the ChatOps `/review`
  slash command in `docs-ghaw-chatops.md` Claim 8 (`contents: read,
  pull-requests: read`). Corroborates that this exact permission pair is the
  house style for any PR-reading, comment-writing gh-aw workflow, regardless
  of whether it's event-triggered or slash-command-triggered.

### Claim 5: The starter configures three safe-outputs with per-type limits: `add-comment` capped at 1, `create-pull-request-review-comment` capped at 10, and `submit-pull-request-review` restricted to `COMMENT`-type events only
- **Evidence**: The `safe-outputs:` block in the frontmatter shows all three
  types with their constraints in the same workflow.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; see the YAML in Concrete Artifacts —
  `safe-outputs: add-comment: max: 1 create-pull-request-review-comment: max:
  10 submit-pull-request-review: allowed-events: [COMMENT]`)
- **Our assessment**: The `max: 1` / `max: 10` pairing caps the agent to one
  summary comment and at most ten inline findings per run — a concrete,
  numeric instance of the volume-limiting pattern already named in
  `docs-ghaw-chatops.md` Claim 8 (which used `max: 5` for the same output
  type in a different, slash-command-triggered example). The two examples
  together show `max:` values are workflow-author-tunable, not fixed by the
  platform. Per `docs-ghaw-safe-outputs-specification.md` Claim 6, exceeding
  either cap rejects ALL operations of that type for the run, not just the
  overflow — so a review that tries to post 11 inline comments would post
  zero, not ten.

### Claim 6: `submit-pull-request-review`'s `allowed-events: [COMMENT]` restricts the safe output to posting a review with COMMENT status, not APPROVE or REQUEST_CHANGES
- **Evidence**: The frontmatter's `submit-pull-request-review:` block sets
  `allowed-events: [COMMENT]` with no other events listed, alongside the
  page's framing that the agent "cannot write directly to the pull request."
- **Confidence**: emerging (the field's full set of legal values and their
  effect on GitHub's PR review API are not documented anywhere on this page;
  inferred from GitHub's own review-event vocabulary of COMMENT/APPROVE/
  REQUEST_CHANGES, which the page itself does not spell out)
- **Quote**: (no direct quote; see paraphrase above — the YAML value
  `allowed-events: [COMMENT]` is verbatim in Concrete Artifacts)
- **Our assessment**: If `allowed-events` indeed gates which GitHub review
  states the safe output may submit, this is a meaningful safety detail: an
  automated review agent can leave comments but is structurally prevented
  from auto-approving or auto-blocking a PR merge. That would be a
  materially stronger safety property than "read-only + safe outputs"
  alone, since without this restriction a compromised or over-eager agent
  could still approve its own or an attacker's PR via a safe output. No
  existing source note documents the `allowed-events` field for
  `submit-pull-request-review` — `docs-ghaw-cross-repository-reference.md`
  Claim 4 lists `submit-pull-request-review` only as one of five safe-output
  types that don't support `target-repo: "*"` dynamic targeting, and does
  not mention `allowed-events` at all. We flag this as emerging rather than
  settled because the page never states the consequence of the restriction
  in its own words — a full field reference (not fetched for this note)
  would be needed to confirm it precisely.

### Claim 7: The review instructions direct the agent to create inline comments only for specific problems, produce one severity-grouped summary comment, and explicitly avoid restating unchanged code or giving style-only feedback
- **Evidence**: The markdown instruction body following the frontmatter in
  the code sample.
- **Confidence**: settled (verbatim instruction text)
- **Quote**: "Create inline review comments only for specific problems or
  concrete improvements. Add one summary comment that groups findings by
  severity and notes anything that needs human follow-up. Do not restate
  unchanged code or provide style-only feedback."
- **Our assessment**: This is a concrete, actionable prompt-design pattern
  for review agents: constrain inline comments to genuine findings (not
  narration), consolidate feedback into a single summary rather than one
  comment per observation, and explicitly exclude style nitpicks. The
  explicit "do not restate unchanged code" instruction targets a known LLM
  review-agent failure mode (restating the diff back to the author instead
  of adding value) — this is new, specific guidance not present in
  `docs-ghaw-chatops.md`'s shorter `/review` instruction body, which asks
  the agent to "examine the diff for potential bugs, security
  vulnerabilities, performance implications, code style issues, and missing
  tests or documentation" without this anti-noise constraint.

### Claim 8: Both `add-comment` and `create-pull-request-review-comment` being safe outputs means the agent cannot write directly to the pull request; gh-aw validates the review payload before posting
- **Evidence**: The page's closing paragraph, stated as the safety rationale
  for the whole pattern.
- **Confidence**: settled (restates the platform's normative Safe Outputs
  guarantee, per `docs-ghaw-safe-outputs-specification.md` Claim 3: agents
  MUST execute without write permissions)
- **Quote**: "This pattern uses `add-comment` for the summary and
  `create-pull-request-review-comment` for inline findings. Both are safe
  outputs, so the agent cannot write directly to the pull request; gh-aw
  validates the review payload before posting it."
- **Our assessment**: Directly corroborates `docs-ghaw-how-they-work.md`
  Claim 5 and `docs-ghaw-safe-outputs-specification.md` Claim 3 — no new
  architectural claim here, but it is useful as a plain-language restatement
  aimed at practitioners installing this specific starter, rather than the
  formal spec language used elsewhere in the corpus.

## Concrete Artifacts

### Starter workflow — `.github/workflows/pr-review.md` (as shown on the page)

```yaml
---
on:
  pull_request:
    types: [opened, synchronize]

permissions:
  contents: read
  pull-requests: read

safe-outputs:
  add-comment:
    max: 1
  create-pull-request-review-comment:
    max: 10
  submit-pull-request-review:
    allowed-events: [COMMENT]
---
# Pull Request Review Assistant

Review the pull request diff for correctness, security, maintainability, and test coverage.
Create inline review comments only for specific problems or concrete improvements. Add one summary comment that groups findings by severity and notes anything that needs human follow-up. Do not restate unchanged code or provide style-only feedback.
```

*Source: gh-aw docs, "Automated AI pull request review on GitHub" — the
page's single code sample, reconstructed line-for-line from the rendered
page (blank-line spacing between YAML sections normalized; all keys,
values, and prose lines verbatim).*

### Installation command

```
gh aw add-wizard githubnext/agentics/pr-review
```

*Source: gh-aw docs, "Automated AI pull request review on GitHub"*

### Related pages linked from this guide (not fetched for this note)

```
- Run Claude Code in GitHub Actions with gh-aw  → /gh-aw/engines/claude/
- Run GitHub Copilot agents in GitHub Actions with gh-aw → /gh-aw/engines/copilot/
- ChatOps → /gh-aw/patterns/chat-ops/
- Quick start → /gh-aw/setup/quick-start/
```

*Source: gh-aw docs, "Automated AI pull request review on GitHub", "Related
pages" section — link targets extracted from the page's anchor hrefs.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default) and
    Claim 5 (Safe Outputs as pre-approved operations without write
    permissions): Claims 1, 4, and 8 in this note are a direct, concrete
    instantiation of both for the PR-review use case.
  - `docs-ghaw-chatops.md` Claim 8 (the `/review` slash-command example uses
    `contents: read, pull-requests: read` and a `max:` cap on
    `create-pull-request-review-comment`): Claim 4 in this note shows the
    identical read-only permission pair used for an event-triggered (rather
    than slash-command-triggered) review workflow, and Claim 5 shows the
    same `max:` volume-limiting mechanism with a different numeric value
    (`max: 10` here vs. `max: 5` in the ChatOps example) — corroborating
    that `max:` is author-tunable per workflow, not fixed.
  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents MUST execute
    without write permissions; communication via NDJSON artifacts) and
    Claim 6 (max-limit violations reject ALL operations of that type, not
    just the excess): both are the normative backing for what this page
    states informally in Claim 8 and implies in Claim 5.
  - `blog-ghaw-issue-pr-mgmt.md` Claim 7 (all four of that post's workflows
    install via `gh aw add-wizard` from pinned spec URLs): Claim 2 in this
    note shows the same installation mechanism for a fifth workflow
    (`githubnext/agentics/pr-review`), reinforcing `add-wizard` + pinned URL
    as GitHub Next's standard distribution model across its whole starter
    catalog, not just issue/PR-management workflows.

- **Extends**:
  - `docs-ghaw-cross-repository-reference.md` Claim 4 (which lists
    `submit-pull-request-review` only as one of five safe-output types
    lacking `target-repo: "*"` support): this note's Claim 6 adds the
    `allowed-events` field for that same safe-output type — a
    review-state restriction that Claim 4 in that note does not mention.
  - `docs-ghaw-chatops.md`'s `/review` instruction body (Concrete Artifacts,
    "Slash Command Trigger — Full `/review` Example"): this note's Claim 7
    documents a more specific instruction pattern (explicit anti-noise
    constraints: no restating unchanged code, no style-only feedback, one
    summary comment) than the shorter ChatOps instruction text, extending
    the corpus's coverage of review-agent prompt design.

- **Contradicts**: None found. This page is fully consistent with the Safe
  Outputs / read-only-agent architecture documented in
  `docs-ghaw-how-they-work.md` and `docs-ghaw-safe-outputs-specification.md`,
  and with the permission pattern in `docs-ghaw-chatops.md`.

- **Novel**:
  - **`submit-pull-request-review` with `allowed-events: [COMMENT]`**
    (Claim 6): the specific field restricting an automated review's
    submission to comment-only status (as opposed to approve/request-changes)
    is not documented in any existing source note — this is the first
    appearance of that safe-output type's `allowed-events` configuration in
    the corpus.
  - **Concrete numeric safe-output limits for an event-triggered (non-ChatOps)
    review workflow** (Claim 5): `add-comment: max: 1` /
    `create-pull-request-review-comment: max: 10` on the `pull_request`
    trigger, distinct from the slash-command example already in the corpus.
  - **The anti-noise review-instruction pattern** (Claim 7): explicit
    "do not restate unchanged code or provide style-only feedback" guidance
    is new — a specific prompt-design constraint aimed at a known review-agent
    failure mode.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `pull_request: types:
  [opened, synchronize]` trigger scoping (Claim 3) as a concrete example of
  narrowing an event trigger to the subset of event subtypes that matter
  (code changes, not PR metadata edits) — currently the guide's trigger
  coverage (per `docs-ghaw-how-they-work.md`) doesn't include a worked
  example of `types:` filtering. Also add the anti-noise instruction pattern
  from Claim 7 ("do not restate unchanged code," "no style-only feedback,"
  "one summary comment grouping findings by severity") as a specific,
  reusable prompt template fragment for any review-style agent, citing this
  source alongside the shorter ChatOps `/review` example already cited from
  `docs-ghaw-chatops.md`.
- **Chapter 03 (Safety and Verification)**: If Claim 6 is confirmed by a
  fuller field reference, recommend `submit-pull-request-review:
  allowed-events: [COMMENT]` as the safe default for any automated
  (non-human-triggered) review workflow — explicitly preventing an agent
  from auto-approving or auto-blocking a PR via a safe output, which is a
  stronger and more specific claim than the guide's current "no write access
  by default" framing. Flag this as needing verification against the full
  Safe Outputs field reference before stating it as settled guidance.

## Extraction Notes

1. **WebFetch produced a fabricated structure on first attempt.** An initial
   fetch via the WebFetch tool returned invented section headings ("##
   Overview", "## Installation", "## Workflow Configuration", "## Safety
   Implementation") and reworded prose that do not exist on the actual page.
   The real page has no such headings — just a title, three paragraphs, one
   code block, and a "Related pages" list. I discarded that fetch entirely
   and re-extracted by downloading the raw HTML directly (`curl`) and
   parsing the `sl-markdown-content` container by hand, then cross-checked
   every quote in this note against the raw `<p>`/`<pre>` tags. All quotes
   above are copied character-for-character from that raw extraction, not
   from the WebFetch summary.
2. **Related pages not fetched.** The four "Related pages" links (Claude
   Code engine, Copilot engine, ChatOps, Quick start) point to general
   platform documentation already covered in depth by
   `docs-ghaw-engines-reference.md` and `docs-ghaw-chatops.md`, and a
   general onboarding quick-start page unrelated to the PR-review recipe
   specifically. Given this source page itself is very short and
   self-contained, and the linked pages don't add PR-review-specific
   material, I did not follow them — logged here per MINER.md §1's
   instruction to note when sub-pages weren't followed and why.
3. **Source is thin.** The page yields 8 claims, at the low end of the
   5-15 target range, because it is a short recipe page (three short
   paragraphs plus one code sample) rather than a comprehensive guide. I
   did not pad with generic restatement to hit a higher count.
4. **No publication date.** The page carries no visible publication or
   last-updated date; `date_published` is left null, consistent with other
   gh-aw docs notes in this corpus.
5. **No contradictions filed.** Reviewed `docs-ghaw-how-they-work.md`,
   `docs-ghaw-chatops.md`, `docs-ghaw-safe-outputs-specification.md`, and
   `docs-ghaw-cross-repository-reference.md`. No claims here materially
   oppose any existing source note at the MINER.md §4a threshold — Claim 6
   extends rather than contradicts the cross-repository-reference note's
   partial coverage of `submit-pull-request-review`.
