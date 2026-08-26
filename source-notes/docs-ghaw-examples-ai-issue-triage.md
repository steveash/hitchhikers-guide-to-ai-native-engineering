---
source_url: https://github.github.com/gh-aw/examples/ai-issue-triage
source_type: docs
title: "AI issue triage on GitHub"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: settled
issue: "#2972"
---

# AI issue triage on GitHub

> A short first-party recipe page showing the complete starter configuration for
> `githubnext/agentics/issue-triage`: an `on: issues: [opened, edited]` trigger, a
> `contents: read` / `issues: read` permission pair, and a two-part safe-outputs
> block (`add-labels` with an 8-label `allowed:` list and `max: 4`; `add-comment`
> with `max: 1`) — the first corpus source to show the exact allowlisted label set
> and per-label usage rules (`duplicate`, `needs-info`) for an issue-triage agent.

## Source Context

- **Type**: docs (a single "Examples" recipe page in the gh-aw documentation site —
  a narrow, prescriptive starter configuration with a complete workflow file, not a
  conceptual overview or full reference. Structurally identical in format to the
  sibling `examples/automated-pr-review` page already in the corpus
  (`docs-ghaw-automated-pr-review.md`): the site's pagination footer links this page
  directly to that one as "Next").
- **Author credibility**: First-party GitHub Next / Microsoft Research documentation
  for the `gh-aw` platform — the same team and doc set behind `docs-ghaw-issueops.md`,
  `docs-ghaw-labelops.md`, and `docs-ghaw-automated-pr-review.md`. Authoritative for
  the exact starter YAML, installation command, and label-management instructions;
  the page cites no external metrics or field-usage data.
- **Scope**: Covers exactly one starter workflow — issue triage on `issues:
  opened`/`edited` — and its safe-outputs configuration, agent instructions, and
  label-provisioning requirements. Does NOT cover: the general `on: issues:` trigger
  schema or two-job permission-separation architecture (that's `docs-ghaw-issueops.md`),
  the `label_command` trigger for label-driven re-runs (`docs-ghaw-labelops.md`), the
  formal Safe Outputs validation pipeline (`docs-ghaw-safe-outputs-specification.md`),
  or the Repo Assist triage-layer pattern for public repos
  (`docs-ghaw-examples-maintaining-repos.md`). The page is very short: two intro
  paragraphs, one YAML+markdown code block, two closing paragraphs, and a "Related
  pages" link list — no headings until "Related pages" (H2).

## Extracted Claims

### Claim 1: AI issue triage runs an agent on every new/edited issue to classify it, apply labels, detect likely duplicates, and request missing details, while staying read-only and writing exclusively through safe outputs

- **Evidence**: The page's opening paragraph frames the entire pattern this way
  before showing the concrete configuration.
- **Confidence**: settled (first-party description of a shipped starter workflow)
- **Quote**: "AI issue triage with gh-aw means running an agent whenever a new issue
  arrives so it can classify the report, set priority labels, detect likely
  duplicates, and ask for missing details. The workflow stays read-only during
  analysis, and gh-aw performs the resulting GitHub writes through safe outputs."
- **Our assessment**: This restates the general Safe Outputs permission model
  (`docs-ghaw-how-they-work.md` Claim 4: no write access by default; Claim 5: Safe
  Outputs as pre-approved operations) applied to the issue-triage use case — the same
  architectural pattern `docs-ghaw-automated-pr-review.md` Claim 1 documents for
  PR review. Nothing here is architecturally new, but it confirms triage is offered
  as an official packaged starter, not something practitioners must assemble
  themselves.

### Claim 2: The starter is installed with a single wizard command targeting a pinned workflow spec, `githubnext/agentics/issue-triage`, adapted from workflows published in the `githubnext/agentics` repository

- **Evidence**: The installation instruction is the page's second paragraph, a
  single command plus attribution to the source repository, with no additional
  setup steps described beyond it.
- **Confidence**: settled
- **Quote**: "Install the starter with `gh aw add-wizard githubnext/agentics/issue-triage`.
  The pattern is adapted from the workflows published in githubnext/agentics."
- **Our assessment**: Consistent with `docs-ghaw-automated-pr-review.md` Claim 2
  (`gh aw add-wizard githubnext/agentics/pr-review`) and `blog-ghaw-issue-pr-mgmt.md`
  Claim 7 (four orchestrator workflows installed the same way) — this is now the
  sixth documented instance of `add-wizard` + pinned spec URL as GitHub Next's
  standard distribution mechanism for official starter workflows, corroborating
  that the mechanism generalizes across issue-triage, PR-review, and
  orchestration use cases alike.

### Claim 3: The trigger fires on both `opened` and `edited` issue events (`on: issues: types: [opened, edited]`), with `contents: read` and `issues: read` as the only permissions on the AI job

- **Evidence**: The workflow frontmatter's `on:` and `permissions:` blocks, shown
  verbatim in the page's single code sample.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; YAML verbatim in Concrete Artifacts —
  `on: issues: types: [opened, edited]` / `permissions: contents: read, issues: read`)
- **Our assessment**: This is a concrete variant on the IssueOps trigger pattern
  documented in `docs-ghaw-issueops.md` Claim 1, which shows `types: [opened]` only
  with `contents: read` + `actions: read` permissions. This page's triage workflow
  differs on both axes: it adds `edited` to the trigger types (so an issue that gets
  more detail added after creation is re-triaged) and swaps `actions: read` for
  `issues: read` (needed to read existing/recently-closed issues for duplicate
  detection — `actions: read` would not grant that). Neither difference is a
  contradiction; they are two different, purpose-fit configurations of the same
  `on: issues:` trigger family. This is the first corpus source to show `edited`
  included in an IssueOps-style trigger, and the first to show `issues: read` (vs.
  `actions: read`) as the companion permission.

### Claim 4: `add-labels` is scoped to an 8-value `allowed:` list (`bug`, `feature`, `question`, `needs-info`, `priority/p0`, `priority/p1`, `priority/p2`, `duplicate`) capped at `max: 4` labels per run; `add-comment` is capped at `max: 1`

- **Evidence**: The `safe-outputs:` block in the frontmatter, shown verbatim in the
  code sample.
- **Confidence**: settled (shown directly in the code sample)
- **Quote**: (no direct prose quote; YAML verbatim in Concrete Artifacts)
- **Our assessment**: This is a concrete instantiation of the `add-labels: allowed:`
  categorical-bounding primitive documented in `docs-ghaw-issueops.md` Claim 3 (which
  showed a 5-value allowlist: `bug, needs-info, enhancement, question, documentation`
  with `max: 2`). This page's allowlist is a superset/variant tuned for triage
  specifically: it adds a three-tier priority ladder (`priority/p0`–`p2`) and a
  `duplicate` label not present in the IssueOps example, and raises `max:` to 4 to
  accommodate applying both a type label and a priority label (plus possibly
  `needs-info` or `duplicate`) in one run. `add-comment: max: 1` matches the
  IssueOps note's Claim 2 pattern of capping comment volume, though this page's
  `add-comment` omits an explicit `target: "triggering"` field (default targeting
  behavior is presumably used, but the page does not state this).

### Claim 5: The agent's instructions direct it to do exactly three things per issue — classify and label, identify duplicates from open and recently-closed issues, and ask clarifying questions in one comment when details are missing

- **Evidence**: The markdown instruction body following the frontmatter in the code
  sample, phrased as a numbered three-item list.
- **Confidence**: settled (verbatim instruction text)
- **Quote**: "Review the triggering issue and do three things: 1. Classify the issue
  by type and priority, then add the matching labels. 2. Identify likely duplicates
  from existing open and recent closed issues. 3. If required details are missing,
  ask concise clarifying questions in one comment."
- **Our assessment**: This is a concrete, minimal three-task prompt template for
  triage agents: classify+label, duplicate-check, and gap-fill — bounded to
  "recent closed issues" (not the full closed-issue history) for duplicate
  detection, which limits the search surface an agent needs to reason over. The
  "one comment" constraint for clarifying questions reinforces the `add-comment:
  max: 1` cap in Claim 4 — the prompt and the safe-outputs bound are mutually
  consistent, not just independently specified.

### Claim 6: Duplicate labeling is gated on match strength and requires citing the matched issue number; `needs-info` is gated on three specific missing-detail categories

- **Evidence**: The sentence immediately following the numbered instruction list in
  the code sample.
- **Confidence**: settled (verbatim instruction text)
- **Quote**: "Use `duplicate` only when the match is strong and include the issue
  number in the comment. Use `needs-info` when reproduction steps, expected
  behavior, or environment details are missing."
- **Our assessment**: This is the most specific, actionable prompt-design guidance
  in the source and the clearest answer to the Prospector's "duplicate detection
  logic" question: the page does not describe an algorithmic similarity threshold
  (e.g., embedding cosine similarity or a numeric score) — duplicate detection is
  delegated entirely to the agent's judgment, constrained only by the qualitative
  instruction "only when the match is strong" plus the requirement to cite the
  specific issue number as evidence in the comment (so a human reviewer can verify
  the claim rather than trust it blindly). Similarly, `needs-info` is scoped to
  three named categories (repro steps, expected behavior, environment details)
  rather than being triggered by vague "insufficient information" judgment. Both
  rules are guardrails against a known LLM-agent failure mode: applying a
  high-consequence label (`duplicate` can cause a real issue to be prematurely
  closed) on weak evidence. No existing corpus source documents duplicate-detection
  prompt guidance at this level of specificity.

### Claim 7: `add-labels` and `add-comment` being safe outputs means the agent has no direct write access to issues; gh-aw validates label names and comment content before posting, which reduces the risk of prompt injection escalating into unrestricted writes

- **Evidence**: The first closing paragraph, stated as the safety rationale for the
  whole pattern.
- **Confidence**: settled (restates the platform's normative Safe Outputs guarantee,
  per `docs-ghaw-safe-outputs-specification.md` Claim 3: agents MUST execute without
  write permissions)
- **Quote**: "`add-labels` and `add-comment` matter for security because the agent
  does not receive direct write access to issues. gh-aw validates label names and
  comment output before posting, which reduces the risk of prompt injection turning
  repository analysis into unrestricted writes."
- **Our assessment**: Directly corroborates `docs-ghaw-how-they-work.md` Claim 5 and
  `docs-ghaw-automated-pr-review.md` Claim 8 — the same "safe outputs = no direct
  write access, validated before posting" framing, now applied specifically to the
  issue-triage threat model: an issue title or body is attacker-controlled content
  (per `docs-ghaw-issueops.md` Claim 4's title+body injection surface), so
  constraining the agent's only write paths to a validated label allowlist and a
  single comment is the concrete defense against a triage agent being manipulated
  into applying arbitrary labels or posting arbitrary content.

### Claim 8: Every label in the `allowed:` list must pre-exist in the target repository or applying it fails at runtime; only `bug`, `feature`, and `question` ship as GitHub defaults, so `needs-info` and the three `priority/pN` labels must be created manually before first use

- **Evidence**: The second closing paragraph, which enumerates which of the eight
  allowlisted labels are GitHub defaults and which are not, and gives two concrete
  provisioning methods.
- **Confidence**: settled (verbatim instruction, consistent with
  `docs-ghaw-issueops.md` Claim 3's general note that `allowed:` "enumerates the
  complete set of labels the agent may apply")
- **Quote**: "Every label listed under `allowed` must already exist in the target
  repository. `bug`, `feature`, and `question` ship as GitHub defaults, but labels
  such as `needs-info`, `priority/p0`, `priority/p1`, and `priority/p2` do not, and
  applying a missing label fails at runtime. Create them before the first run with
  `gh label create needs-info` (repeat per label) or from the repository's
  Settings > Labels page."
- **Our assessment**: This is a practical deployment gotcha not stated in
  `docs-ghaw-issueops.md`'s more abstract treatment of `add-labels: allowed:` —
  the allowlist is a *client-side* constraint on what the agent may request, but it
  does not create the labels; a missing label is a hard runtime failure, not a
  silent no-op or an auto-created label. For a team deploying this starter
  unmodified, five of the eight allowlisted labels (`needs-info`,
  `priority/p0`, `priority/p1`, `priority/p2`, and `duplicate` — GitHub does not
  ship a `duplicate` default either, though the page does not call this out
  explicitly alongside the other four) require manual provisioning before the
  workflow can succeed on a fresh repository.

## Concrete Artifacts

### Starter workflow — `.github/workflows/issue-triage.md` (as shown on the page)

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
comment. Use `needs-info` when reproduction steps, expected behavior, or
environment details are missing.
```

*Source: gh-aw docs, "AI issue triage on GitHub" — the page's single code sample,
reconstructed line-for-line from the raw page HTML (fetched directly via `curl`
and parsed by hand; see Extraction Notes on why WebFetch's rendering was
discarded). All keys, values, and prose lines are verbatim.*

### Installation command

```
gh aw add-wizard githubnext/agentics/issue-triage
```

*Source: gh-aw docs, "AI issue triage on GitHub"*

### Related pages linked from this guide (not fetched for this note)

```
- Run Claude Code in GitHub Actions with gh-aw          → /gh-aw/engines/claude/
- Run GitHub Copilot agents in GitHub Actions with gh-aw → /gh-aw/engines/copilot/
- IssueOps                                               → /gh-aw/patterns/issue-ops/
- Quick start                                            → /gh-aw/setup/quick-start/
```

*Source: gh-aw docs, "AI issue triage on GitHub", "Related pages" section — link
targets extracted from the page's anchor hrefs. The page's pagination footer also
shows this page sits directly between "Using at Scale in Organizations"
(previous) and "Automated PR Review" (next, `/gh-aw/examples/automated-pr-review/`)
in the Examples section's reading order.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claims 4–5 (no write access by default; Safe
    Outputs as the permission-separated write channel): Claims 1 and 7 in this
    note are a direct instantiation of both for the issue-triage use case.
  - `docs-ghaw-issueops.md` Claim 3 (`add-labels: allowed:` as a categorical
    write-surface bound, paired with `max:` as a quantitative bound): Claim 4 here
    shows a second, independently-configured instance of the identical primitive
    with a different (larger, triage-specific) label set and `max:` value —
    corroborating that `allowed:` + `max:` is the general pattern for any
    label-writing gh-aw workflow, not an IssueOps-specific one-off.
  - `docs-ghaw-issueops.md` Claim 4 (issue title+body is attacker-controlled input
    requiring sanitization): Claim 7 here restates the same threat model
    (prompt injection via issue content) as the rationale for constraining writes,
    though — see Extraction Notes — this page does not itself mention
    `steps.sanitized.outputs.text`, so it corroborates the threat model without
    corroborating the specific sanitization mechanism.
  - `docs-ghaw-automated-pr-review.md` Claims 1, 2, and 8 (same "install via
    wizard from a pinned `githubnext/agentics/*` spec," "read-only agent + safe
    outputs" pattern, applied to the sibling PR-review starter): this note's
    Claims 1, 2, and 7 show the identical pattern applied to issue triage,
    reinforcing that both starters share one house architecture.
  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents MUST execute
    without write permissions; writes go through validated Safe Outputs): the
    normative backing for what this page states informally in Claim 7.

- **Extends**:
  - `docs-ghaw-issueops.md`: that note documents the general `on: issues:`
    trigger and `add-labels`/`add-comment` safe-outputs pattern using a
    5-label, `types: [opened]`-only, `actions: read`-permissioned example. This
    note extends it with a concrete triage-specific variant: `types: [opened,
    edited]`, `issues: read` (not `actions: read`), an 8-label allowlist
    including a priority ladder and a `duplicate` label, and — new to the
    corpus — specific per-label usage rules (Claim 6) that the IssueOps
    reference page does not provide.
  - `blog-vercel-github-tools-eve.md` Claim 3: that note documents an
    `issue-triage` *preset* in an unrelated framework (Vercel's AI SDK GitHub
    tools) that scopes a toolset to the issue-triage role by name. This note
    shows the same conceptual role — "issue triage" as a distinct, named agent
    function — implemented independently in gh-aw via a full workflow (trigger +
    permissions + safe-outputs + prompt) rather than a tool preset. The two
    sources corroborate that issue-triage is treated as a first-class, distinct
    agent archetype across at least two unrelated platforms, though the
    implementations are architecturally different (a bounded workflow vs. a
    scoped toolset) and this is not the same underlying mechanism.
  - `docs-ghaw-labelops.md`: that note documents `label_command` — triggering
    a workflow *from* a label being applied by a human. This note's workflow
    goes the other direction: it *applies* labels as an output, triggered by
    issue creation/edit, not by a label event. The two patterns are
    complementary (label-as-trigger vs. label-as-output) rather than
    overlapping, and could compose (e.g., a `triage-requested` label triggering
    a re-run of this workflow via `label_command`), though the source page does
    not describe such a composition.

- **Contradicts**: None identified. This page is fully consistent with the Safe
  Outputs / read-only-agent architecture documented in
  `docs-ghaw-how-they-work.md`, `docs-ghaw-issueops.md`, and
  `docs-ghaw-safe-outputs-specification.md`. The trigger-type and permission
  differences from `docs-ghaw-issueops.md` (Claim 3) are workflow-specific
  configuration choices, not conflicting claims about how the platform behaves —
  no contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Concrete per-label usage rules for duplicate and needs-info labeling**
    (Claim 6): no existing source note documents qualitative gating criteria
    ("only when the match is strong," "include the issue number," the three
    named `needs-info` categories) for when an agent should apply a specific
    triage label. This is the first source to answer the Prospector's "duplicate
    detection logic" question, and the answer is a prompt-level judgment rule,
    not an algorithmic threshold.
  - **`edited` included alongside `opened` in an `on: issues:` trigger**
    (Claim 3): `docs-ghaw-issueops.md` only documents `types: [opened]`. This is
    the first corpus source showing `edited` in the same trigger list, so an
    issue can be re-triaged after the reporter adds detail.
  - **`issues: read` as the companion permission to `contents: read`**
    (Claim 3): `docs-ghaw-issueops.md` uses `actions: read` in the equivalent
    slot. No existing source explains why one workflow needs `actions: read`
    and another needs `issues: read`; this note infers the likely reason
    (duplicate detection requires reading existing issue content) but flags it
    as inference, not a stated platform rule.
  - **A concrete, triage-tuned `add-labels: allowed:` list with a priority
    ladder** (Claim 4): the specific 8-label set (type labels + 3-tier priority
    + `needs-info` + `duplicate`) is a reusable reference configuration not
    present elsewhere in the corpus.
  - **Explicit runtime-failure behavior for missing allowlisted labels**
    (Claim 8): no existing source states that applying an `allowed:`-listed
    label that doesn't exist in the repository fails at runtime (rather than,
    e.g., being silently skipped or auto-created).

## Guide Impact

### Chapter 02 (Harness Engineering)

- **Add this workflow as the concrete issue-triage reference configuration**
  (Claims 3–4): where the guide currently might cite `docs-ghaw-issueops.md`'s
  generic `on: issues:` example, add this triage-specific variant showing
  `types: [opened, edited]`, `issues: read`, and an 8-label `allowed:` list with
  a priority ladder — a directly reusable starter for teams building their own
  triage agent.
- **Add the duplicate/needs-info gating rules as a reusable prompt-design
  pattern** (Claim 6): "gate a high-consequence label on strong-match evidence
  plus a citable reference (the specific issue number)" and "gate an
  info-request label on named missing-detail categories, not vague
  insufficiency" are both generalizable beyond issue triage — any agent
  applying a label with real consequences (e.g., `duplicate`, `wontfix`,
  `invalid`) should follow the same evidence-citation discipline.
- **Flag the label-pre-existence deployment gotcha** (Claim 8): document that
  `add-labels: allowed:` labels must be created before first use or the
  workflow fails at runtime — a concrete checklist item ("run `gh label
  create <name>` for every non-default label in your allowlist before
  deploying") for anyone adopting this or a similar starter.

### Chapter 03 (Safety and Verification)

- **Add the duplicate-labeling evidence requirement as a safety pattern**
  (Claim 6): "include the issue number in the comment" when applying
  `duplicate` gives a human reviewer a citable, checkable claim rather than an
  opaque label — this is a specific, generalizable instance of "require the
  agent to show its work" for any high-consequence classification action,
  worth adding alongside the existing Safe Outputs write-surface-bounding
  guidance (`allowed:`/`max:`) already documented from `docs-ghaw-issueops.md`.

## Extraction Notes

1. **WebFetch fabricated section headings on first two attempts — discarded.**
   Two initial WebFetch calls against this URL each returned invented H2
   structure ("## Overview", "## Installation", "## Workflow Configuration",
   "## Security Model", "## Label Requirements" on one pass; "## Overview",
   "## Key Implementation Details", "## Related Resources" on a follow-up
   pass with a different prompt) and reworded/paraphrased prose that does not
   exist on the real page. This is the same failure mode already documented in
   `docs-ghaw-automated-pr-review.md` Extraction Note 1 for the sibling
   `examples/automated-pr-review` page — both pages are short, headingless
   (until "Related pages") Astro/Starlight recipe pages, and WebFetch's
   underlying model appears to reliably impose a templated heading structure
   on this specific page type rather than reporting the actual (much shorter)
   content. I discarded both WebFetch outputs entirely and re-extracted by
   downloading the raw HTML directly (`curl`) and parsing the
   `sl-markdown-content` container by hand. Every quote and the full code
   block in this note are copied character-for-character from that raw
   HTML extraction, not from either WebFetch summary. **Flagging for the
   Prospector/Assayer**: this appears to be a systematic WebFetch failure mode
   for `github.github.com/gh-aw/examples/*` and possibly `guides/*` pages
   specifically — future miners assigned pages in this section should
   fetch raw HTML directly rather than trusting WebFetch's rendered summary.
2. **Related pages not fetched.** The four "Related pages" links (Claude Code
   engine, Copilot engine, IssueOps, Quick start) point to general platform
   documentation already covered by `docs-ghaw-engines-reference.md` and
   `docs-ghaw-issueops.md`, or a general onboarding page unrelated to the
   triage recipe specifically. Given the source page itself is short and
   self-contained and the linked pages don't add triage-specific material, I
   did not follow them.
3. **Source is thin — 8 claims**, at the low end of the 5-15 target range,
   because the actual page (once fabricated WebFetch content was discarded) is
   two intro paragraphs, one code sample, and two closing paragraphs — shorter
   even than the already-thin sibling `docs-ghaw-automated-pr-review.md` (8
   claims from three paragraphs plus one code block). I did not pad with
   generic restatement to reach a higher count.
4. **No publication date.** The page carries no visible publication or
   last-updated date; `date_published` is left null, consistent with other
   gh-aw docs notes in this corpus.
5. **Minor naming inconsistency noted, not treated as a contradiction.**
   `docs-ghaw-examples-maintaining-repos.md`'s Concrete Artifacts safe-outputs
   table lists a type named `label-issue`, while this page (and
   `docs-ghaw-issueops.md`) both use `add-labels` for the same YAML key. This
   is very likely the maintaining-repos table using a descriptive/paraphrased
   name rather than the literal field name (that note's own claims are
   sourced from a table, not a code sample), not a genuine platform
   inconsistency — both this page's and the IssueOps page's YAML samples are
   unambiguous, literal `add-labels:` keys. Not filed as a contradiction per
   MINER.md §4a (weakly-supported side / not a claim about behavior).
6. **No contradictions filed.** Reviewed `docs-ghaw-how-they-work.md`,
   `docs-ghaw-issueops.md`, `docs-ghaw-labelops.md`,
   `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-automated-pr-review.md`,
   and `blog-vercel-github-tools-eve.md`. No claim here materially opposes any
   existing source note at the MINER.md §4a threshold — the trigger-type and
   permission differences from `docs-ghaw-issueops.md` (Claim 3) are
   configuration variation between two different example workflows, not a
   disagreement about platform behavior.
