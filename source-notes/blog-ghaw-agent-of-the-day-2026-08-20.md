---
source_url: https://github.github.com/gh-aw/blog/2026-08-20-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – August 20, 2026: The Gardener"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-08-20
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2835"
---

# Agent of the Day – August 20, 2026: The Gardener

> Seventh entry in the "Agent of the Day" series — profiles Issue Arborist
> ("The Gardener"), a daily-scheduled issue-triage agent that scans the 100
> most recent parentless issues, links orphan clusters and symptom/root-cause
> pairs as sub-issues with an explicit, published citation for every link
> made, and — distinctively — publishes explicit reasoning for links it
> deliberately declined to make. Establishes conservative, reasoning-transparent
> issue linking as a named write-enabled agent archetype, and gives the
> corpus's first documented use of matching failed-run IDs across issues as
> a triage signal.

## Source Context

- **Type**: blog-post (seventh "Agent of the Day" entry from the official
  GitHub Agentic Workflows blog; bylined "Copilot" per the on-page author
  card, the same recurring gh-aw convention for AI-authored posts documented
  in prior entries in this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-08-18.md`. Each post profiles one
  production agent with concrete run data. This entry profiles a
  write-enabled issue-triage agent, distinct from the read-only audits in
  the May 20 Architecture Guardian and August 18 Notary entries, and from
  the event-driven, write-enabled AI Moderator of May 15.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post links a specific,
  independently verifiable GitHub Actions run
  (`https://github.com/github/gh-aw/actions/runs/31997474928`) for its
  August 17 run, and cites fourteen distinct, specific issue numbers
  (#53268–#53270, #53049, #52723, #52652, #52657, #53263, #53245, #53235,
  #53262, #53193, #53071–#53075, #52858) each linked directly to
  `github/gh-aw` issues. High credibility for first-party platform claims;
  the 5-run aggregate metrics (Claim 6 below) are stated in prose without an
  individually linked run URL for each of the five runs, so only the
  August 17 run is independently spot-checkable via its linked Actions run.
- **Scope**: Profiles Issue Arborist's August 17, 2026 run in detail (seven
  links made, five links deliberately withheld, each with stated reasoning)
  and summarizes aggregate reliability over a five-run window (~August
  11–17). Does NOT cover: the workflow's YAML frontmatter or `experiments:`
  A/B-test configuration (documented separately in
  `blog-ghaw-weekly-2026-08-17.md` Claim 11); GitHub API call counts per run
  (unlike the three-run snapshot in `blog-ghaw-weekly-2026-08-17.md` Claim
  10, this post gives no API-call figure); the discussion-report content
  itself (only the post's own summary of it); or what happens after a link
  is made (whether maintainers ever override or unlink a decision).

## Extracted Claims

### Claim 1: Issue Arborist is a scheduled `gh-aw` workflow that scans the 100 most recent open issues without a parent, looks for orphan clusters and symptom/root-cause pairs, and either links them as sub-issues or creates a new parent issue when a cluster is big enough to deserve one

- **Evidence**: Direct first-party description of the agent's mission and
  scanning scope in the second paragraph of the post.
- **Confidence**: settled (explicit, first-party mission description)
- **Quote**: "We're calling this workflow's persona **The Gardener**, and the
  name fits **Issue Arborist**, a scheduled `gh-aw` workflow that scans the
  100 most recent open issues without a parent, looks for orphan clusters
  and symptom/root-cause pairs, and either links them as sub-issues or
  creates a new parent when a cluster is big enough to deserve one."
- **Our assessment**: This restates and refines the workflow's purpose as
  first documented in `blog-ghaw-issue-pr-mgmt.md` Claim 1 ("an
  organizational workflow that has created 77 discussion reports ... and 18
  parent issues" by "linking related issues as sub-issues"), now with a
  precise scan boundary (100 most recent parentless issues) not stated in
  the January post. For Ch02 (Harness Engineering): "scan the N most recent
  unparented items, then link-or-create" is a concrete, reusable scoping
  pattern for any scheduled triage agent working against a growing,
  unbounded backlog — bounding the scan avoids unbounded per-run cost as the
  tracker grows.

### Claim 2: In its August 17 run, Issue Arborist reviewed 100 open issues and found seven confident matches, each with an explicit citation for why the link was safe to make

- **Evidence**: Direct statement introducing the linked run and the count of
  confident matches, immediately followed by the five bulleted examples
  (Claim 3).
- **Confidence**: settled (specific count tied to a linked, independently
  verifiable Actions run)
- **Quote**: "In its [August 17 run](https://github.com/github/gh-aw/actions/runs/31997474928),
  it reviewed 100 open issues and found seven confident matches, each with
  an explicit citation for why the link was safe to make"
- **Our assessment**: "Explicit citation for why the link was safe" is the
  operative design principle — the agent isn't just producing a link
  decision, it's producing a link decision plus the specific textual
  evidence that justified it. This is the same "reasoning transparency"
  value seen in `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4
  (Architecture Guardian's `safeoutputs.noop` called with a human-readable
  skip message), but applied to a write action (creating a link) rather
  than a skip. For Ch03 (Safety and Verification): any agent action that
  mutates shared state (here, issue hierarchy) should be paired with a
  human-legible justification string, not just the mutation itself.

### Claim 3: Two of the seven August 17 links were made because a symptom issue and a root-cause issue cited the exact same failed GitHub Actions run IDs — a concrete, checkable triage signal distinct from topical/textual similarity

- **Evidence**: Two of the five bulleted linking examples explicitly cite
  matching run IDs as the link justification: #53245/#53235 under #53263,
  and #53193 under #53262.
- **Confidence**: settled (explicit reasoning quoted directly from the post
  for both examples)
- **Quote**: "[#53245](https://github.com/github/gh-aw/issues/53245) and
  [#53235](https://github.com/github/gh-aw/issues/53235) linked under
  [#53263](https://github.com/github/gh-aw/issues/53263) — a root-cause
  issue about `safe_outputs` hard-failing entire batches — because both
  symptom issues cited the exact same failed run IDs the root cause called
  out. [#53193](https://github.com/github/gh-aw/issues/53193) linked under
  [#53262](https://github.com/github/gh-aw/issues/53262) for the same
  reason: matching run IDs across a root-cause and a symptom report."
- **Our assessment**: This is a genuinely specific, checkable triage
  heuristic — not "these issues seem related" but "these issues cite the
  identical run ID, therefore they describe the same underlying failure."
  It is a stronger evidentiary bar than semantic similarity, and it directly
  operationalizes the problem framing in the post's opening paragraph ("A
  workflow-failure symptom issue never gets tied back to the root cause that
  explains it"). For Ch02 (Harness Engineering): document "shared run-ID (or
  other unique execution identifier) citation" as a concrete, high-precision
  linking signal for any issue-triage agent operating on a codebase that
  generates CI/Actions run IDs — a stronger signal than free-text similarity
  because it is nearly unambiguous.

### Claim 4: The remaining three of the seven links were justified by explicit backlog self-description or existing cross-reference, not run-ID matching: two child issues that described themselves as slices of a named parent's backlog, one issue already referenced by name in its target parent, and one issue matched to an existing named tracker

- **Evidence**: Three of the five bulleted examples, each citing a distinct
  justification.
- **Confidence**: settled (explicit reasoning quoted directly from the post
  for all three examples)
- **Quote**: "[#53269](https://github.com/github/gh-aw/issues/53269) and
  [#53270](https://github.com/github/gh-aw/issues/53270) linked under
  [#53268](https://github.com/github/gh-aw/issues/53268) (`lint-monster:
  function-length refactoring`) — both child issues explicitly described
  themselves as slices of that parent's backlog. [#52723](https://github.com/github/gh-aw/issues/52723)
  linked under [#53049](https://github.com/github/gh-aw/issues/53049), a
  safe-outputs reliability parent that already referenced it by name.
  [#52652](https://github.com/github/gh-aw/issues/52652) linked under
  [#52657](https://github.com/github/gh-aw/issues/52657), a container CVE
  burn-down tracker."
- **Our assessment**: Combined with Claim 3, this shows Issue Arborist uses
  at least three distinct, named evidence types to justify a link: (a)
  shared run-ID citation, (b) self-description as a backlog slice, and (c)
  existing named cross-reference in the target parent. None of the seven
  confident links in this run rest on unexplained semantic similarity alone
  — every one cites a specific textual artifact. For Ch02: a reusable
  taxonomy of "acceptable evidence types" for automated issue-linking —
  practitioners building a similar agent can use this three-type list
  (shared identifier, self-declared membership, existing named reference)
  as a starting checklist for what counts as a safe-to-link citation.

### Claim 5: The same run flagged five additional issues as probably related but declined to link them, because the agent was not confident it understood the maintainers' intended organizational structure

- **Evidence**: Direct statement following the confident-match list,
  covering four container-scan issues and one additional issue withheld for
  a distinct reason.
- **Confidence**: settled (explicit reasoning quoted directly from the post)
- **Quote**: "Just as telling is what it _didn't_ link. The same run flagged
  four newer container-scan issues ([#53071](https://github.com/github/gh-aw/issues/53071),
  [#53072](https://github.com/github/gh-aw/issues/53072),
  [#53073](https://github.com/github/gh-aw/issues/53073),
  [#53075](https://github.com/github/gh-aw/issues/53075)) and one more
  ([#52858](https://github.com/github/gh-aw/issues/52858)) as _probably_
  related to the CVE burn-down parent — but held back because it wasn't
  confident whether maintainers wanted one rolling child per image or a
  daily detail issue per scan. It also noted #53263 might belong under the
  broader safe-outputs backlog #53049, but again declined to guess."
- **Our assessment**: This is the standout design property of the post: the
  agent distinguishes "probably related" from "confidently linkable," and
  the stated reason for withholding is not evidentiary weakness (it does
  believe the issues are related) but structural ambiguity about
  organizational intent ("one rolling child per image or a daily detail
  issue per scan"). This is a higher bar than Architecture Guardian's binary
  skip decision (`blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4) — here
  the agent makes seven positive decisions and five negative decisions in
  the same run, and explains each negative decision individually rather
  than emitting one aggregate "nothing more to report" message. For Ch02:
  when a linking/mutation decision depends on unstated maintainer intent
  (not just observable evidence), the agent should default to declining and
  surfacing the ambiguity rather than guessing — and should state *what*
  the ambiguity is (here: rolling-child-per-image vs. daily-detail-issue),
  giving maintainers the specific question to resolve rather than just a
  raised flag.

### Claim 6: Every linking decision made and every decision skipped is published as a public daily discussion report, giving maintainers visibility into the agent's reasoning rather than just its output

- **Evidence**: Direct closing statement of the "what it didn't link"
  paragraph.
- **Confidence**: settled (explicit design statement)
- **Quote**: "Every decision — made and skipped — gets published as a public
  daily discussion report, so maintainers can see the reasoning, not just
  the result."
- **Our assessment**: Publishing *declined* actions, not only completed
  ones, is the auditability property that most distinguishes this agent
  from prior corpus entries. `blog-ghaw-agent-of-the-day-2026-05-20.md`
  Claim 4 documents Architecture Guardian's noop-with-message pattern as
  auditable, but that is a single binary "skip today" decision per run. Here
  the discussion report is a structured accounting of a whole set of
  micro-decisions (7 made, 5 skipped in the profiled run), which is a
  materially larger and more granular disclosure surface. For Ch03 (Safety
  and Verification): for any agent that makes several independent mutation
  decisions per run, publish the full decision set — including near-misses
  that were deliberately not acted on — not just a summary of actions
  taken. The near-misses are often the most useful signal for a maintainer
  auditing whether the agent's judgment is trustworthy.

### Claim 7: Across its last five tracked runs (roughly August 11–17), Issue Arborist recorded five successful runs, zero errors, zero warnings, averaging around 8 minutes of runtime and 6–8 safe-output items per run, classified in the post as normal, uneventful automation

- **Evidence**: Aggregate operational summary in the post's fourth
  paragraph, covering a window described as "roughly August 11–17."
- **Confidence**: anecdotal (aggregate figures stated in prose; unlike the
  August 17 run in Claims 2–5, no individual Actions run URL is linked for
  any of the five runs, so the aggregate cannot be independently
  spot-checked run-by-run)
- **Quote**: "Across its last five tracked runs (roughly August 11–17),
  Issue Arborist has been remarkably consistent: five successful runs, zero
  errors, zero warnings, averaging around 8 minutes of runtime and creating
  6–8 safe-output items each time, all classified as normal, uneventful
  automation."
- **Our assessment**: This figure sits alongside, but does not simply
  restate, the three-run snapshot in `blog-ghaw-weekly-2026-08-17.md` Claim
  10 (published three days earlier from the same underlying agent): that
  note reports "under 11 minutes" runtime, "around 15" GitHub API calls, and
  "8–14" safe-output items per run across three runs. This post reports "~8
  minutes" runtime and "6–8" safe-output items across five runs, with no API
  call figure given. The two windows likely overlap (the weekly post covers
  runs up to 2026-08-17; this post's window is "roughly August 11–17") but
  are not stated as the same runs, and the safe-output-count ranges (8–14 vs.
  6–8) do not fully overlap. We read this as two different, non-identical
  measurement windows over the same continuously-running agent rather than a
  contradiction — the underlying claim ("Issue Arborist runs reliably with
  single-digit-minutes runtime and single-digit-to-low-teens safe-output
  counts per run") is consistent across both, but practitioners citing exact
  figures should note which post and which window they are drawing from.
  This does not meet the MINER.md §4a contradiction-filing bar: both figures
  describe the same agent behaving consistently, just measured over
  different (and only partially specified) windows — not two sources
  materially disagreeing about what the agent does or how well it works.

### Claim 8: No orphan cluster in the five-run window was large enough to justify creating a brand-new parent issue from scratch, which the post frames as a signal that the existing issue hierarchy is holding up reasonably well

- **Evidence**: Direct statement immediately following the five-run
  aggregate metrics.
- **Confidence**: anecdotal (author's interpretive framing of an absence —
  zero new-parent-issue creations in the window — as a positive structural
  signal, not an independently measured claim about hierarchy health)
- **Quote**: "No orphan cluster in that window was ever large enough to
  justify spinning up a brand-new parent issue from scratch — which is
  itself a useful signal that gh-aw's existing issue hierarchy is holding up
  reasonably well."
- **Our assessment**: This is a plausible but soft inference: "the agent
  didn't need to create a new parent" is consistent with "the hierarchy is
  healthy," but it is equally consistent with "clusters below the
  new-parent threshold happened not to occur this week" or "the threshold
  for creating a new parent is set conservatively enough that it rarely
  fires." The post does not state what triggers new-parent creation (e.g.,
  a minimum cluster size) or how often it has fired historically — contrast
  with `blog-ghaw-issue-pr-mgmt.md` Claim 1, which reports 18 parent issues
  created cumulatively since deployment, meaning the mechanism does fire
  over a long enough window. For Ch04 (Operations): "zero occurrences of an
  agent's most disruptive action type in a monitoring window" is a weak
  standalone health signal on its own — it should be paired with a
  known base rate (as `blog-ghaw-issue-pr-mgmt.md`'s 18-parent-issue
  cumulative figure provides) before treating it as evidence of tracker
  health rather than just low recent cluster volume.

## Concrete Artifacts

### Issue Arborist: August 17, 2026 Run — Links Made and Withheld

```
Run: https://github.com/github/gh-aw/actions/runs/31997474928
Issues reviewed: 100 (most recent open, parentless)
Confident links made: 7

Links made:
  #53269, #53270 -> under #53268 (lint-monster: function-length refactoring)
    reason: both children self-described as slices of that parent's backlog
  #52723 -> under #53049 (safe-outputs reliability parent)
    reason: parent already referenced #52723 by name
  #52652 -> under #52657 (container CVE burn-down tracker)
    reason: (topical match to named tracker; no further detail given)
  #53245, #53235 -> under #53263 (root cause: safe_outputs hard-failing batches)
    reason: symptom issues cited the exact same failed run IDs as the root cause
  #53193 -> under #53262
    reason: matching run IDs across root-cause and symptom report

Links withheld (5):
  #53071, #53072, #53073, #53075 -> probably related to CVE burn-down parent
    reason withheld: uncertain whether maintainers want one rolling child
    per image or a daily detail issue per scan
  #52858 -> probably related to CVE burn-down parent (same reason)
  #53263 -> possibly belongs under broader safe-outputs backlog #53049
    reason withheld: declined to guess

Disclosure: every decision (made and skipped) published as a public daily
discussion report.
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 20, 2026"*

### Issue Arborist: Five-Run Aggregate (roughly August 11–17, 2026, as stated in this post)

```
Runs tracked:     5
Successful runs:  5
Errors:           0
Warnings:         0
Avg runtime:      ~8 minutes
Safe-output items per run: 6-8
New parent issues created in window: 0
Classification:   "normal, uneventful automation"
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 20, 2026"*

Compare against the three-run snapshot in `blog-ghaw-weekly-2026-08-17.md`
Claim 10 (Concrete Artifacts): under-11-minute runtime, ~15 GitHub API
calls, 8–14 safe-output items per run, zero errors — a different,
only-partially-overlapping measurement window over the same agent; see
Claim 7's Our assessment for discussion of the discrepancy.

## Cross-References

- **Corroborates**:
  - `blog-ghaw-issue-pr-mgmt.md` Claim 1 (Issue Arborist described as "an
    organizational workflow that has created 77 discussion reports ... and
    18 parent issues" by "linking related issues as sub-issues," building
    "a dependency tree we'd never maintain manually"): Claim 1 here restates
    the same core mechanism (scan open issues, link related ones as
    sub-issues, create parents for large clusters) roughly seven months
    later, with a precise scan boundary (100 most recent parentless issues)
    that the January post did not state.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 10 (Agent of the Week spotlight,
    three-run snapshot: sub-11-minute runtime, ~15 API calls, 8–14
    safe-output items, zero errors): Claim 7 here corroborates the general
    shape of the claim (reliable, single-digit-minutes runtime, no errors,
    single-digit-to-low-teens safe-output volume) with a five-run window
    three days later, though the specific numeric ranges do not fully
    overlap — see Claim 7's Our assessment for why this is treated as two
    measurement windows rather than a contradiction.
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4 (Architecture
    Guardian's `safeoutputs.noop` called with an explicit, human-readable
    skip message rather than a silent skip): Claim 6 here corroborates the
    underlying principle — auditable agents should state *why* they didn't
    act, not just what they did act on — and extends it from a single
    binary per-run skip decision to a per-decision disclosure across
    multiple independent linking calls in the same run.

- **Contradicts**: None filed. Reviewed `CONTRADICTIONS.md` (no entries on
  issue-linking, issue-triage agents, or Issue Arborist) and the two
  existing Issue Arborist source notes (`blog-ghaw-issue-pr-mgmt.md`,
  `blog-ghaw-weekly-2026-08-17.md`). The numeric difference between this
  post's five-run aggregate (Claim 7) and the weekly post's three-run
  snapshot does not meet the MINER.md §4a bar: both describe the same
  continuously-running agent behaving consistently well, over different,
  only-partially-specified windows — not two sources making opposing
  claims about what the agent does or how it performs.

- **Extends**:
  - `blog-ghaw-weekly-2026-08-17.md` Claim 11 (Issue Arborist's
    `experiments.prompt_style` A/B test comparing "concise" vs. "detailed"
    instruction variants against a `links_created` metric, with a
    zero-tolerance `empty_output_rate` guardrail): that note documents the
    experiment's existence in the workflow's YAML frontmatter but not any
    result. This post's August 17 run (Claims 2–5) shows the agent
    producing seven well-justified links and zero empty-output runs in the
    five-run window (Claim 7) — consistent with, but not confirming,
    healthy behavior under whichever prompt variant was active for these
    runs. Neither post states which variant (`concise` or `detailed`) was
    used for the profiled runs.
  - `blog-ghaw-issue-pr-mgmt.md` Claim 1 (cumulative 18 parent issues
    created since deployment): Claim 8 here (zero new parents in the
    5-run window) is a short-window data point that, read against the
    cumulative 18-parent figure, indicates new-parent creation is
    infrequent relative to linking — consistent with the January post's
    implicit ratio (77 discussion reports to 18 parent issues, i.e., most
    runs report analysis without creating a new parent).

- **Novel**:
  - **Matching failed-run IDs across issues as a specific, high-precision
    linking signal** (Claim 3): No prior corpus source documents an agent
    using a shared unique execution identifier (a GitHub Actions run ID) as
    linking evidence between a symptom report and its root cause. This is a
    stronger, more checkable signal than the semantic/topical similarity
    implied elsewhere in the corpus's triage-agent coverage.
  - **Publishing declined-action reasoning alongside completed-action
    reasoning, at per-decision granularity within a single run** (Claim 6):
    prior corpus auditability patterns (Architecture Guardian's
    noop-with-message) cover a single per-run binary decision. This post
    documents an agent that discloses reasoning for each of several
    independent negative decisions (5 withheld links) alongside each of
    several independent positive decisions (7 made links) in the same run
    — a materially finer-grained disclosure model.
  - **A named taxonomy of acceptable link-justification evidence types**
    (Claim 4, read together with Claim 3): shared identifier citation,
    self-declared backlog membership, and existing named cross-reference
    are three distinct evidence types the agent cites across its seven
    confident links in one run — not previously enumerated in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "scan the N most recent
  unparented/unprocessed items, then link-or-create" (Claim 1) as a named
  scoping pattern for scheduled triage agents operating against unbounded,
  growing backlogs. Add "shared unique execution identifier as a
  high-precision linking signal" (Claim 3) to the toolkit of concrete
  evidence types an issue/artifact-linking agent can use, alongside
  semantic similarity — cite the run-ID-matching example as the
  worked case. Add the three-type evidence taxonomy from Claim 4 (shared
  identifier, self-declared membership, existing named reference) as a
  starting checklist for practitioners designing a similar linking agent's
  "is this link safe to make automatically" logic.

- **Chapter 03 (Safety and Verification)**: Update auditability guidance to
  cover multi-decision runs (Claim 6): when an agent makes several
  independent mutation decisions in one run, the audit trail should include
  every decision — made and declined — with its individual justification,
  not an aggregate summary. Pair with the existing
  `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4 guidance
  (noop-with-message for single binary skip decisions) to cover both the
  single-decision and multi-decision disclosure cases. Add "decline and
  surface the specific open question" (Claim 5) as the recommended behavior
  when a mutation decision depends on unstated human intent rather than
  observable evidence — the agent should name the actual ambiguity (e.g.,
  "one rolling child per image or a daily detail issue per scan"), not just
  flag uncertainty generically.

- **Chapter 04 (Operations)**: Caution practitioners citing Issue Arborist's
  operational metrics that at least two different measurement windows exist
  in the corpus with non-identical numbers (Claim 7: this post's five-run
  ~8-minute/6–8-safe-output window vs. `blog-ghaw-weekly-2026-08-17.md`'s
  three-run under-11-minute/8–14-safe-output window) — cite the specific
  source and window rather than treating either figure as a settled,
  permanent baseline. Note the weak-signal caution from Claim 8: "zero
  occurrences of an agent's most disruptive action in a short monitoring
  window" should be paired with a known longer-term base rate (e.g.,
  `blog-ghaw-issue-pr-mgmt.md`'s cumulative 18-parent-issue figure) before
  being read as evidence of system health.

## Extraction Notes

1. **Full post fetched via `curl` and read from raw HTML, not only
   WebFetch summary**: An initial WebFetch pass returned a structured
   summary with several numbers (e.g., "3.88 vs 3.5" — not applicable here,
   but generally WebFetch's small-model summarization risks rounding or
   restating figures). To obtain verbatim quotes per MINER.md §2a, the page
   was re-fetched directly via `curl` and the article body located inside
   `<div class="sl-markdown-content">`, then read as raw HTML/text. All
   quotes above are copied character-for-character from that raw fetch, not
   reconstructed from the WebFetch summary. The post is short (approximately
   500 words) and was captured in full in one fetch; no pagination or
   truncation was observed.

2. **Linked issue and Actions-run URLs not individually followed**: The
   post links directly to fourteen `github/gh-aw` issues and one Actions
   run. These are cited as primary-source evidence within the blog post's
   own text (the post already quotes the specific reasoning for each), not
   as substantive sub-pages carrying additional content the post omits, so
   they were not separately fetched per MINER.md §1's "up to 5 linked
   pages" guidance — the reasoning text in the blog post itself is the
   claim being extracted, and it is already verbatim-quotable from the post.
   One prior note in this series (`blog-ghaw-weekly-2026-08-17.md`) did
   fetch the underlying `issue-arborist.md` workflow file directly; that
   file's content (YAML frontmatter, `experiments:` block) is reused here
   only by cross-reference (see Extends), not re-fetched, since it is
   unrelated to this post's own text and was already captured in that note.

3. **Three existing source notes reviewed in full before writing
   Cross-References**: `blog-ghaw-issue-pr-mgmt.md`,
   `blog-ghaw-weekly-2026-08-17.md`, and
   `blog-ghaw-agent-of-the-day-2026-05-20.md` were read in full (not
   skimmed) to verify claim numbers and quote text before citing them
   above. All `Claim N` citations were checked against the actual numbered
   claims in those notes at the time of writing.

4. **No contradictions filed**: See Cross-References → Contradicts. The
   only tension found (differing five-run vs. three-run metric snapshots
   for the same agent) is treated as a measurement-window discrepancy, not
   a contradiction meeting the MINER.md §4a bar, and is documented in
   Claim 7's Our assessment and in the Guide Impact caution instead.

5. **Duplicate-triage note**: Three separate Prospector triage comments are
   present on issue #2835, apparently from repeated/parallel triage passes
   on the same auto-filed source. All three agree on novelty (high/medium),
   relevant chapters (Ch02, Ch04, and one adds Ch03/Ch06), and the core
   extraction guidance; this note follows the union of their guidance
   (conservative linking with reasoning, run-ID pairing, operational
   metrics, issue-triage as a distinct archetype) rather than picking one
   comment over the others.
