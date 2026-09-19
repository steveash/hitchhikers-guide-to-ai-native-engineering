---
source_url: https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience
source_type: docs
title: "Copilot code review: An improved review experience"
author: GitHub (official changelog)
date_published: 2026-09-18
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: settled
issue: "#3560"
---

# Copilot Code Review: An Improved Review Experience

> GitHub's September 18, 2026 changelog announcing a restructured overview comment
> (findings grouped into Open / Resolved since last review / Previously missed),
> finding-level titles, two enhancements to auto-resolution (honoring "leave open"
> replies, tagging resolution reasons), and smart commit messages extended to
> batches of accepted suggestions — all GA immediately. Read together with its
> directly linked September 11, 2026 predecessor changelog, which introduces the
> baseline auto-resolution and single-suggestion smart-commit-message features
> this entry enhances, plus two analysis-quality changes (broader shell-tool access,
> an ensemble-of-agents architecture for Lite reviews) with the corpus's first
> quantified before/after metrics for Copilot code review output quality and cost.

## Source Context

- **Type**: docs (GitHub official product changelog, ~230 words, September 18, 2026),
  plus its directly linked predecessor changelog dated September 11, 2026
  (`https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review/`,
  ~280 words), followed per MINER.md's linked-page-following guidance because the
  September 18 entry explicitly frames its auto-resolution section as an
  enhancement to a feature introduced the week before ("New auto-resolution
  capabilities... These capabilities have now been improved") and links directly
  to that entry's auto-resolution section.
- **Author credibility**: GitHub engineering team announcing production feature
  changes and, in the September 11 entry, internal experiment results. Authoritative
  for the fact that these features exist, their mechanics, and their GA/rollout
  status. The September 11 entry's quantitative claims ("47%... 31%... 11%...
  about 8%") are self-reported by GitHub from its own experiments, with no
  methodology, sample size, or experiment duration disclosed — authoritative that
  GitHub observed these numbers internally, not independently verifiable by a
  practitioner.
- **Scope**: Covers UI/UX changes to the Copilot code review overview comment and
  per-comment titles, auto-resolution behavior and resolution-reason tagging,
  smart commit message generation for both single suggestions and batches, and
  (via the linked September 11 entry) two behind-the-scenes analysis changes:
  broadened shell-tool access for the review agent and an ensemble-of-agents
  architecture specifically for Lite-tier reviews. Does NOT cover: how the
  ensemble approach is implemented (number of agents, how conflicting findings
  across agents are reconciled), the experiment's sample size or repos/languages
  tested, whether the shell-tool and ensemble changes apply to Balanced reviews
  as well as Lite, or a numeric AI-Credit/Actions-minute cost figure for the
  claimed "about 8%" cost reduction (percentage of what baseline is unstated).

## Extracted Claims

### Claim 1: The refreshed Copilot code review overview comment shows the PR's current assessment, the review effort level used, and a summary of findings grouped into three categories: Open, Resolved since last review, and Previously missed

- **Evidence**: Dedicated changelog section "🔍 Clearer review progress at a glance."
- **Confidence**: settled (shipped UI change, described directly in the official changelog)
- **Quote**: "The refreshed overview comment shows Copilot's current assessment of your pull request, the review effort level it used, and lists a summary of the findings it identified in its review. Findings are now grouped into:"
- **Our assessment**: This is the most substantive change in the source — a
  restructuring of the primary artifact practitioners read when triaging a
  Copilot review. It directly extends `docs-github-copilot-code-review-effort-levels-ga.md`
  Claim 7 (effort level labeling shown "in both timeline events and the pull
  request overview comment") by confirming the overview comment now also carries
  the effort-level label alongside the new finding-grouping structure, and
  `docs-github-copilot-code-review-analysis-depth-efficiency.md` Claim 7 (PR
  overview comments displaying tier attribution for Medium-depth reviews) — the
  overview comment has been a growing surface for review metadata across three
  separate changelog entries (analysis-depth-efficiency's tier attribution,
  effort-levels-ga's effort-level labeling, and now this grouped-findings
  restructuring).

### Claim 2: Findings in the overview comment are grouped as Open (not yet addressed, may carry a new-commit label), Resolved since last review (validated as fixed), and Previously missed (newly found in existing changes, not previously commented elsewhere on the PR)

- **Evidence**: The three category definitions given in the same changelog section.
- **Confidence**: settled (shipped feature, definitions stated directly)
- **Quote**: "Open: Issues that have not been addressed yet. These may have a new label, indicating that they were introduced by a new commit."
- **Quote**: "Resolved since last review: Copilot has validated that you've fixed those issues it found earlier."
- **Quote**: "Previously missed: Issues not introduced by a new commit, but newly found in your existing changes by Copilot's subsequent review. This section includes the exact details of those comments, as they are not commented anywhere else on your pull request."
- **Our assessment**: The "Previously missed" category is the most operationally
  important of the three: it is the overview comment's only surface for findings
  Copilot catches on a re-review pass over code that didn't change since the last
  review — because these findings aren't posted as new inline comments elsewhere
  on the PR, a practitioner who only reads inline comments (rather than the
  overview) would miss them entirely. This is a concrete example of Copilot code
  review's iterative, multi-pass nature surfacing gaps in its own prior passes —
  worth flagging for Ch01 as a reason to always check the overview comment, not
  just inline comments, on re-review.

### Claim 3: Each finding in the overview comment includes its severity and a link to the corresponding inline comment; the overview persists progress across pushes, and prior PR-level and per-file summaries remain available alongside it

- **Evidence**: Same changelog section, closing paragraph.
- **Confidence**: settled (shipped feature, stated directly)
- **Quote**: "Each finding includes its severity and a link to the corresponding inline comment, so you can quickly move from the overview to the relevant code."
- **Quote**: "As you push additional commits and request another review, the overview preserves your progress and logs Copilot's findings. The prior pull request summary and per-file summaries also remain available."
- **Our assessment**: Embedding severity directly in the overview-comment finding
  list (not only on the inline comment itself, per
  `docs-github-copilot-code-review-comment-ux.md` Claim 1) means a practitioner
  can now triage by severity from the single overview comment without opening
  each inline thread — a further reduction in the "read every comment to
  prioritize" friction that Claim 1 of the comment-ux note originally addressed
  at the individual-comment level.

### Claim 4: Copilot code review comments now carry a title concisely describing the finding, used both in the overview comment's issue list and as an at-a-glance descriptor on the comment itself

- **Evidence**: Dedicated changelog subsection "Comment titles."
- **Confidence**: settled (shipped feature, stated directly)
- **Quote**: "Each Copilot code review comment now contains a title concisely describing what was found. These titles are used in the aforementioned overview comment's issue list and as at-a-glance descriptors of Copilot findings. This way you can prioritize the findings you want to look into first."
- **Our assessment**: Titles are the missing scanning primitive for the new
  Open/Resolved/Previously-missed grouping (Claim 2): without a title, an
  overview-comment issue list would show only severity and a link, forcing a
  click-through to understand each finding. With titles, the three-category list
  becomes independently scannable. This is a corroborating, tighter integration
  point with the severity labels documented in
  `docs-github-copilot-code-review-comment-ux.md` Claim 1 — severity plus title
  together give a two-field triage signal without opening any comment.

### Claim 5: Auto-resolution now honors an explicit reviewer reply asking to leave a comment open, rather than resolving it regardless

- **Evidence**: Dedicated changelog subsection "Comments are now auto-resolved more intelligently," first bullet.
- **Confidence**: settled (shipped behavior change, stated directly)
- **Quote**: "When a Copilot code review comment gets a reply to leave the issue open, it honors that reply."
- **Our assessment**: This is a correction to a specific failure mode of the
  baseline auto-resolution feature (see Claim 9 below, from the linked September
  11 entry): auto-resolving on a later commit is useful when the commit actually
  addresses the feedback, but could previously override a reviewer's explicit
  "no, leave this open" intent if a later commit happened to touch the same
  lines. This closes that gap — reviewer intent now takes precedence over the
  heuristic.

### Claim 6: Auto-resolution now tags resolved comments with a resolution reason — either Won't Fix or Incorrect — based on the practitioner's subsequent commits

- **Evidence**: Same changelog subsection, second bullet.
- **Confidence**: settled (shipped behavior change, stated directly)
- **Quote**: "Copilot now resolves comments with a resolution reason, either Won't Fix or Incorrect, based on your subsequent commits."
- **Our assessment**: This adds an audit trail dimension to auto-resolution that
  the September 11 baseline (Claim 9 below) did not have: previously, a comment
  auto-resolved by a later commit had no distinction between "this was
  incorrect/not applicable" and "this was fixed as suggested" versus "this was
  deliberately declined." The two-value reason (Won't Fix / Incorrect) is coarser
  than a full explanation but gives reviewers scanning resolved threads a signal
  for why each was closed without re-reading the full thread.

### Claim 7: Smart commit messages, previously generated only for a single applied suggestion, now extend to an eligible, complete batch of suggestions — including batches that mix Copilot and non-Copilot comments

- **Evidence**: Dedicated changelog section "✍️ Smart commit messages for batch suggestions."
- **Confidence**: settled (shipped feature extension, stated directly)
- **Quote**: "When you commit an eligible, complete batch of Copilot code review suggestions, Copilot now generates a relevant commit title and an optional description based on the selected changes. Batches can also contain non-Copilot comments and will still receive smart commit messages."
- **Our assessment**: This is explicitly an extension of the September 11
  baseline (Claim 10 below), which generated smart commit messages only "when you
  apply a suggestion" (singular). The batch case is the common real-world usage
  pattern for larger PRs, where a practitioner accepts many suggestions before
  committing — the single-suggestion version would have left batch commits with
  generic auto-filled messages. The "mixed batch" detail (Copilot + non-Copilot
  comments still receiving a smart message) means the feature generates from the
  net diff of the batch, not solely from Copilot-attributed changes.

### Claim 8: All of the September 18 improvements (overview restructuring, comment titles, auto-resolution enhancements, batch smart commit messages) are generally available, not a preview

- **Evidence**: Closing sentence of the changelog's intro paragraph.
- **Confidence**: settled (explicit GA statement)
- **Quote**: "These updates are now generally available."
- **Our assessment**: Unlike the June 2 → August 7 preview-to-GA arc documented
  for effort levels (`docs-github-copilot-code-review-skills-mcp-tier.md` →
  `docs-github-copilot-code-review-effort-levels-ga.md`), this batch of UX and
  auto-resolution changes ships directly to GA with no stated preview period —
  practitioners should expect these behaviors immediately, not as an opt-in.

### Claim 9: The baseline auto-resolution capability — comments resolve automatically when a later commit addresses the underlying feedback during Copilot's rereview — shipped September 11, 2026, one week before the improvements in Claim 5 and Claim 6

- **Evidence**: "✅ Automatic resolution of addressed comments" section of the linked September 11, 2026 predecessor changelog, which the September 18 entry links to directly from its own auto-resolution subsection.
- **Confidence**: settled (shipped feature, stated directly in the linked changelog)
- **Quote**: "When you push a commit that addresses a Copilot code review comment, Copilot now resolves that comment during its rereview. Instead of manually resolving threads that are no longer relevant, you can now rely on the open comments to reflect only the feedback that still needs your attention."
- **Our assessment**: This establishes the correct chronology for the guide: auto-resolution
  as a capability is not new to September 18 — it launched September 11, and the
  September 18 entry (this source's primary subject) only adds the "honor leave-open
  replies" and "tag resolution reason" refinements on top of it. A guide passage
  that cited only the September 18 changelog would risk implying auto-resolution
  itself is brand new; it is one week old at the time of the improvements in
  Claims 5 and 6.

### Claim 10: The baseline smart-commit-message capability — generating a commit message when a single Copilot autofix suggestion is applied — also shipped September 11, 2026, and is the predecessor Claim 7 (above) extends to batches

- **Evidence**: "Smart commit messages on Copilot autofix suggestions" section of the linked September 11, 2026 changelog.
- **Confidence**: settled (shipped feature, stated directly)
- **Quote**: "When you apply a suggestion provided by a Copilot code review comment, instead of auto-filling the standard commit message, Copilot now generates a smart suggestion based on what it's changing."
- **Our assessment**: Same chronology point as Claim 9 — this is the single-suggestion
  baseline; Claim 7's batch capability is the September 18 extension of it, not
  an independent new feature.

### Claim 11: Copilot code review's analysis agent now uses the full set of shell tools from the Copilot SDK (running behind the Copilot agent firewall) to validate reviewed code — e.g., running build commands, running tests, executing targeted scripts, and retrieving information from available tools and APIs — building on the file-reading tools it already used

- **Evidence**: "Deeper analysis with shell tools" section of the linked September 11, 2026 changelog.
- **Confidence**: settled (shipped architecture change, stated directly)
- **Quote**: "Building on the file-reading tools already used during review, Copilot code review now uses the full set of shell tools from the Copilot SDK, running behind the Copilot agent firewall. This gives the review agent more ways to validate the code under review (e.g., running build commands, running tests, executing targeted scripts, and retrieving information from available tools and APIs)."
- **Our assessment**: This is a genuine architectural expansion — moving Copilot
  code review from a primarily static, file-reading analysis to one that can
  execute code and tests during review. It is novel to the corpus: no existing
  Copilot code review source note documents shell-tool or build/test-execution
  capability during automated review. The "behind the Copilot agent firewall"
  phrasing implies a sandboxing/permission boundary distinct from the reviewed
  repository's own CI, but the source does not describe that firewall's
  mechanics — worth flagging as an open question for Ch02 (Harness Engineering)
  around what a reviewed PR's untrusted code can and cannot do when Copilot
  executes it during review.

### Claim 12: GitHub's internal experiment on the shell-tools change found developers left more positive feedback on Copilot's comments, and that Copilot surfaced more high-severity findings and fewer nits — reported qualitatively, with no percentage or count given

- **Evidence**: Closing sentence of the "Deeper analysis with shell tools" section.
- **Confidence**: anecdotal (GitHub-reported experiment result; no quantification, methodology, or sample size disclosed)
- **Quote**: "Our experiments with this change showed that developers left more positive feedback on Copilot's comments, and Copilot surfaced more high severity findings and fewer nits."
- **Our assessment**: Directionally plausible — giving a review agent execution
  tools (running tests, builds) should reduce speculative low-value comments
  ("nits") in favor of findings validated against actual failures. But this is
  vendor-reported with no effect size, so it should be treated as a directional
  claim, not a metric a team could use to forecast their own results. Contrast
  with Claim 13/14 below, where the ensemble-of-agents change is given specific
  percentages — the shell-tools claim notably is not.

### Claim 13: Lite-effort-level reviews now use an ensemble of multiple agents, each contributing its own perspective on the code, combined by Copilot into a single review, rather than one agent working alone

- **Evidence**: "Ensemble of agents in Lite reviews" section of the linked September 11, 2026 changelog.
- **Confidence**: settled (shipped architecture change for a specific effort tier, stated directly)
- **Quote**: "The Lite effort level now uses an ensemble of agents to produce a review rather than one agent working alone. Each agent contributes its own perspective on the code, and Copilot combines their findings into a single review. This makes Lite reviews more thorough and accurate for the same or often lower cost."
- **Our assessment**: This refines `docs-github-copilot-code-review-effort-levels-ga.md`
  Claim 8's definition of Lite ("Standard review. Provides fast, targeted
  feedback on common issues such as bugs, security vulnerabilities, and style
  inconsistencies (default)") with an architectural detail that source did not
  have: Lite is not a single lighter-weight model pass, but a multi-agent
  ensemble specifically at this tier. This does not contradict the August 7
  source — it is a later, additive architecture change to the same named tier,
  not a disagreement about what Lite was on August 7. No contradiction issue
  filed (time-conditioned product change, per MINER.md §4a's "conditioning
  variable" guidance, same treatment the effort-levels-ga note applied to its own
  supersession of the June 2 note).

### Claim 14: GitHub's internal experimentation found the ensemble-of-agents change for Lite reviews increased the average number of addressed comments per review by 47% for high-severity findings, 31% for medium, and 11% for low, while reducing review cost by about 8%

- **Evidence**: Closing sentence of the "Ensemble of agents in Lite reviews" section — the corpus's first quantified before/after metrics for a Copilot code review quality or cost change.
- **Confidence**: emerging (specific percentages given, but self-reported by GitHub with no disclosed experiment design, baseline definition, sample size, or duration)
- **Quote**: "In our experimentation, the ensemble approach increased the average number of addressed comments per review by 47% for high severity findings, 31% for medium, and 11% for low, while reducing review cost by about 8%."
- **Our assessment**: This is the first source in the corpus to attach specific
  percentages to a Copilot code review architecture change — prior sources
  (effort levels, MCP/skills, comment UX) describe capabilities and configuration
  but no source note before this one cites a quantified quality or cost delta.
  "Addressed comments per review" is a proxy for finding relevance (a comment a
  practitioner acts on is presumably more valuable than one they dismiss), and
  the severity-graded breakdown (47/31/11%) is a meaningful signal that the
  ensemble approach disproportionately improves high-severity finding quality
  over low-severity nits — consistent with Claim 12's qualitative "more high
  severity findings and fewer nits" observation from the separate shell-tools
  change. But "about 8%" cost reduction lacks a baseline (8% of what — AI
  Credits, Actions minutes, wall-clock, or a blended figure is not stated), and
  no confidence interval or sample size is given for any of the four numbers.
  Treat as a directional, vendor-reported result, not a number a team can use to
  forecast their own environment's cost or quality delta.

## Concrete Artifacts

### September 18, 2026 changelog (verbatim, cleaned of markup)

```
Title: Copilot code review: An improved review experience
Published: September 18, 2026
Source: https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience

Copilot code review now gives you a clearer view of how a review changes over
time, more intelligently auto-resolves its own suggestions, and generates
useful commit messages when you accept eligible suggestions in a batch. These
updates help you focus on findings that still need attention and make the
resulting commits easier to understand. These updates are now generally
available.

--- SECTION: 🔍 Clearer review progress at a glance ---

The refreshed overview comment shows Copilot's current assessment of your
pull request, the review effort level it used, and lists a summary of the
findings it identified in its review. Findings are now grouped into:

  Open: Issues that have not been addressed yet. These may have a new label,
  indicating that they were introduced by a new commit.

  Resolved since last review: Copilot has validated that you've fixed those
  issues it found earlier. Each finding includes its severity and a link to
  the corresponding inline comment, so you can quickly move from the overview
  to the relevant code.

  Previously missed: Issues not introduced by a new commit, but newly found
  in your existing changes by Copilot's subsequent review. This section
  includes the exact details of those comments, as they are not commented
  anywhere else on your pull request.

As you push additional commits and request another review, the overview
preserves your progress and logs Copilot's findings. The prior pull request
summary and per-file summaries also remain available.

--- SUBSECTION: Comment titles ---

Each Copilot code review comment now contains a title concisely describing
what was found. These titles are used in the aforementioned overview
comment's issue list and as at-a-glance descriptors of Copilot findings. This
way you can prioritize the findings you want to look into first.

--- SUBSECTION: Comments are now auto-resolved more intelligently ---

New auto-resolution capabilities allow GitHub Copilot to resolve its own
comments based on whether they were addressed between reviews. These
capabilities have now been improved:

  - When a Copilot code review comment gets a reply to leave the issue open,
    it honors that reply.
  - Copilot now resolves comments with a resolution reason, either Won't Fix
    or Incorrect, based on your subsequent commits.

--- SECTION: ✍️ Smart commit messages for batch suggestions ---

When you commit an eligible, complete batch of Copilot code review
suggestions, Copilot now generates a relevant commit title and an optional
description based on the selected changes. Batches can also contain
non-Copilot comments and will still receive smart commit messages.
```

### September 11, 2026 linked predecessor changelog (verbatim, cleaned of markup)

```
Title: Auto-resolution and analysis updates in Copilot code review
Published: September 11, 2026
Source: https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review/
(followed from the September 18 entry's link on "New auto-resolution capabilities")

Copilot code review now resolves its own comments once you address them and
writes smart commit messages for you when you apply its code suggestions.
Behind the scenes, Copilot now uses a broader set of shell tools to validate
the code it reviews, and an ensemble of agents produce a more thorough review
within the Lite effort level. Together, these updates make it easier to focus
on the feedback that still matters and give Copilot more ways to check its
work.

--- SECTION: Review experience updates ---

✅ Automatic resolution of addressed comments

When you push a commit that addresses a Copilot code review comment, Copilot
now resolves that comment during its rereview. Instead of manually resolving
threads that are no longer relevant, you can now rely on the open comments to
reflect only the feedback that still needs your attention.

  - Comments are automatically resolved when a later commit addresses the
    underlying feedback.
  - Feedback that is still outstanding stays open, so nothing gets lost.

Smart commit messages on Copilot autofix suggestions

When you apply a suggestion provided by a Copilot code review comment,
instead of auto-filling the standard commit message, Copilot now generates a
smart suggestion based on what it's changing.

--- SECTION: 🔧 Analysis updates ---

The following changes only improve the quality of reviews you receive and do
not affect how you request or receive reviews.

Deeper analysis with shell tools

Building on the file-reading tools already used during review, Copilot code
review now uses the full set of shell tools from the Copilot SDK, running
behind the Copilot agent firewall. This gives the review agent more ways to
validate the code under review (e.g., running build commands, running tests,
executing targeted scripts, and retrieving information from available tools
and APIs).

Our experiments with this change showed that developers left more positive
feedback on Copilot's comments, and Copilot surfaced more high severity
findings and fewer nits.

Ensemble of agents in Lite reviews

The Lite effort level now uses an ensemble of agents to produce a review
rather than one agent working alone. Each agent contributes its own
perspective on the code, and Copilot combines their findings into a single
review. This makes Lite reviews more thorough and accurate for the same or
often lower cost.

In our experimentation, the ensemble approach increased the average number of
addressed comments per review by 47% for high severity findings, 31% for
medium, and 11% for low, while reducing review cost by about 8%.
```

## Cross-References

- **Corroborates** `docs-github-copilot-code-review-comment-ux.md` (issue #723):
  - Claim 1 of that note (per-comment severity labels, High/Medium/Low, top-right
    corner of each comment) is directly built upon by this source's Claim 3
    (severity now also surfaced per-finding in the overview comment) and Claim 4
    (comment titles as a second scannable field alongside severity). The
    triage-without-opening-each-comment pattern that note's Claim 1 introduced is
    extended here from the individual comment level to the whole-PR overview
    level.
  - That note's Claim 2 (comment grouping to reduce repetition) and this source's
    Claim 1-2 (finding grouping into Open/Resolved/Previously missed) are related
    but distinct grouping mechanisms: that note groups *duplicate/similar*
    comments across the PR; this source groups *all* comments by *review-cycle
    status*. Both reduce cognitive load but along different axes — worth noting
    in the guide as two independent grouping dimensions rather than the same
    feature restated.

- **Extends** `docs-github-copilot-code-review-effort-levels-ga.md` (issue #2585):
  - Claim 7 of that note (effort level labeled in PR timeline events and overview
    comment) is confirmed and extended by this source's Claim 1, which
    additionally specifies the overview comment now shows "Copilot's current
    assessment" and the grouped-findings structure alongside the effort-level
    label.
  - Claim 8 of that note (Lite defined as "Standard review. Provides fast,
    targeted feedback...") is refined by this source's Claim 13: Lite reviews now
    run an ensemble of multiple agents rather than a single model pass. This is a
    later architecture change to the same named tier, not a disagreement about
    what Lite meant on August 7 — treated as a time-conditioned product
    evolution per MINER.md §4a, consistent with how the effort-levels-ga note
    itself handled its own supersession of the June 2 preview note. No
    contradiction issue filed.

- **Extends** `docs-github-copilot-code-review-analysis-depth-efficiency.md` (issue not re-verified in this note; cited by section name only):
  - That note's Claim 7 (PR overview comments displaying "Medium" tier attribution
    for Medium-depth reviews) is the earliest corpus instance of the overview
    comment carrying review-metadata beyond findings themselves. This source's
    Claim 1 (overview comment now shows effort level plus a three-way finding
    grouping) is a further build-out of that same surface. This note does not
    cite a specific numbered claim beyond Claim 7, which was directly verified via
    grep against the cited note's text before writing this cross-reference.

- **Contradicts**: None found and none filed. The one point that could look like
  tension — this source's framing of auto-resolution and smart commit messages as
  "new" in the September 18 changelog's intro paragraph, when both capabilities
  actually launched September 11 per Claims 9-10 — is not a contradiction between
  sources; it is this note correcting a chronology ambiguity within a single
  vendor's own changelog series by reading the linked predecessor entry. The
  September 18 changelog itself is accurate on close reading (it says these
  capabilities "have now been improved," not "are new"), so no contradiction issue
  is warranted per MINER.md §4a.

- **Novel**:
  - First corpus source describing the Open / Resolved since last review /
    Previously missed finding-grouping structure in the overview comment
    (Claims 1-2).
  - First corpus source documenting per-comment finding titles as a UI element
    (Claim 4).
  - First corpus source documenting auto-resolution mechanics for Copilot code
    review at all — both the September 11 baseline (Claim 9) and the September 18
    refinements: honoring "leave open" replies (Claim 5) and resolution-reason
    tagging, Won't Fix / Incorrect (Claim 6).
  - First corpus source documenting smart commit message generation for Copilot
    code review suggestions, both single-suggestion (Claim 10) and batch
    (Claim 7).
  - First corpus source documenting shell-tool/build/test execution access for
    the Copilot code review agent, "running behind the Copilot agent firewall"
    (Claim 11).
  - First corpus source documenting a multi-agent ensemble architecture for any
    Copilot code review effort tier (Claim 13).
  - First corpus source with quantified before/after metrics for a Copilot code
    review architecture change — the 47%/31%/11% addressed-comment increases by
    severity and the ~8% cost reduction (Claim 14) — and the first with even a
    qualitative before/after quality claim tied to a specific architecture change
    (Claim 12).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Update the Copilot code review triage
  walkthrough to reflect the new overview-comment structure: practitioners
  should read the overview comment's Open / Resolved since last review /
  Previously missed grouping first, paying particular attention to "Previously
  missed" since those findings are not duplicated as new inline comments
  elsewhere on the PR (Claim 2). Add that comment titles (Claim 4) plus
  per-finding severity in the overview (Claim 3) now allow full PR-level triage
  from the overview comment alone, without opening individual threads. Note
  that auto-resolved comments may now carry a Won't Fix or Incorrect reason tag
  (Claim 6) — reviewers scanning resolved threads have a coarse "why" signal
  without re-reading.
- **Chapter 02 (Harness Engineering)**: Flag the shell-tool/build-execution
  capability (Claim 11) as a new consideration for what untrusted PR code can do
  during an automated review pass — the "Copilot agent firewall" phrase implies
  sandboxing, but this source does not document its boundary; teams with
  security-sensitive repos should investigate before assuming build/test
  execution during review is safely isolated from secrets or network access.
  Also update any existing Lite-tier description to note the ensemble-of-agents
  architecture (Claim 13), since Ch02 content describing effort levels currently
  draws on the effort-levels-ga note's single-agent-implied framing.
- **Chapter 05 (Team Adoption)**: The quantified metrics in Claim 14 (47%/31%/11%
  addressed-comment increases by severity, ~8% cost reduction from the ensemble
  change) are the first vendor-reported numbers in the corpus that could inform
  an ROI narrative for Copilot code review adoption — but flag clearly as
  vendor-self-reported with no disclosed methodology, consistent with this
  note's confidence grading (emerging, not settled). Do not present these
  percentages as independently verified benchmarks.

## Extraction Notes

1. **Two changelog pages read, not one**: The September 18 entry (this issue's
   nominal source) is thin on its own — five features, ~230 words. Its
   auto-resolution subsection explicitly links to and references a September 11
   predecessor entry as the baseline it improves on. Per MINER.md's guidance to
   follow substantive linked pages, that predecessor was fetched and is the
   source of Claims 9-14. Treating the September 18 entry in isolation would have
   misrepresented auto-resolution and smart commit messages as brand-new
   capabilities rather than one-week-old features receiving their first
   refinement, and would have missed the shell-tools and ensemble-of-agents
   architecture changes and their metrics entirely.
2. **No further links followed**: Both changelog pages' only other outbound links
   are same-page table-of-contents anchors and the general `github.blog/changelog`
   listing/label pages — neither substantive nor specific to this feature. No
   additional pages were followed beyond the one predecessor changelog.
3. **Verbatim extraction method**: Both pages were fetched via direct `curl`
   (not WebFetch's AI-summarization path) to `/tmp/source.html` and
   `/tmp/source2.html`, with the `<article>` element isolated, tags stripped,
   and HTML entities unescaped programmatically, preserving the source's exact
   punctuation (including its mixed use of curly apostrophes in most contractions
   and a straight apostrophe in "Won't Fix"). All quotes above were copied from
   that cleaned text, not reconstructed from a summary.
4. **No contradiction issue filed**: See the Cross-References "Contradicts" entry
   above — the apparent "is this new or not" tension resolves on close reading of
   both changelog entries together and is not a genuine disagreement between
   sources.
