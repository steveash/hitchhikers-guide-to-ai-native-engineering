---
source_url: https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments
source_type: docs
title: "Trigger Copilot automations with comments"
author: GitHub (official changelog)
date_published: 2026-08-03
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: emerging
issue: "#2472"
---

# Trigger Copilot Automations with Comments

> GitHub's August 3, 2026 changelog announcing that Copilot cloud agent
> "automations" — previously triggerable only by schedule, issue-creation,
> or pull-request-open/sync events — can now also be triggered by an issue
> or pull request comment matching configured text. The feature is GA for
> Pro/Pro+/Max/Business/Enterprise, but the linked "About Copilot
> automations" reference documentation had not been updated to describe the
> new trigger type as of the extraction date, leaving the precise matching,
> filtering, and governance semantics unconfirmed.

## Source Context

- **Type**: docs (GitHub official product changelog, ~120 words, August 3,
  2026; one linked reference documentation page, "About Copilot
  automations," also examined)
- **Author credibility**: GitHub engineering team announcing a production
  feature as shipped (present-tense "You can now create..."). Authoritative
  for the feature's existence, the three named use cases, the entry point in
  the UI, and the subscription-tier availability. Not authoritative for
  mechanics the changelog does not state: exact comment-text matching rules
  (substring vs. exact vs. pattern), whether the trigger fires immediately,
  and whether the general automations write-access filter (documented for
  the four pre-existing trigger types) applies identically to comment
  triggers.
- **Scope**: Covers the existence of comment-triggered automations, three
  illustrative use cases, the configuration step (specify trigger comment
  text), the UI entry point (Agents tab → Automations), and tier
  availability/admin-policy requirement. Does NOT cover: comment-matching
  syntax or case sensitivity, per-trigger permission/role filtering specific
  to comments, whether comment triggers can be scoped to specific comment
  authors, interaction with the existing "ignore non-write-access users by
  default" rule, or any prompt-injection guidance for comment-derived
  automation prompts. The linked "About Copilot automations" doc — checked
  the same day — does not mention comment triggers at all; see Extraction
  Notes.

## Extracted Claims

### Claim 1: Copilot cloud agent automations can now be configured to run when an issue comment or a pull request comment is created

- **Evidence**: Direct statement in the changelog opening line, framed as a
  new, generally-available capability ("You can now create...").
- **Confidence**: settled (first-party changelog announcing a shipped
  feature)
- **Quote**: "You can now create Copilot cloud agent automations that run
  when an issue comment or pull request comment is created."
- **Our assessment**: This is a fifth trigger type added to Copilot cloud
  agent automations. The linked "About Copilot automations" doc (fetched
  2026-08-04) enumerates only four trigger types — on a schedule, when an
  issue is created, when a pull request is opened, when a pull request is
  synchronized — with no mention of comment triggers. That means the
  changelog is ahead of the reference documentation: the capability is
  live, but the canonical trigger-taxonomy page has not yet been updated to
  include it. For Ch02 (Harness Engineering): document this as a fifth
  automation trigger type, but flag the taxonomy gap so future updates can
  confirm the doc catches up.

### Claim 2: The changelog names three specific use cases for comment-triggered automations — generating documentation, investigating errors, and creating follow-up tasks

- **Evidence**: Three bulleted, labeled use cases in the changelog body,
  each pairing a comment context (PR vs. issue) with a distinct automation
  outcome.
- **Confidence**: settled (explicit first-party examples)
- **Quote**: "Generate documentation: Comment on a pull request to
  automatically generate or update documentation based on your code
  changes. Investigate errors: Comment on an issue to trigger an automation
  that investigates stack traces or error logs. Create follow-up tasks:
  Comment on a pull request to have an automation automatically create
  follow-up issues for refactoring or technical debt."
- **Our assessment**: The three use cases split cleanly along comment
  context: PR comments drive "generate documentation" and "create follow-up
  tasks" (both code-change-adjacent), while issue comments drive "investigate
  errors" (triage-adjacent). None of the three examples describes a
  conversational/interactive use case (e.g., "answer this question") — all
  three are one-shot generative or investigative tasks kicked off by a
  comment, not a back-and-forth chat. For Ch01 (Daily Workflows): frame this
  as "comment as a task-dispatch mechanism," distinct from Copilot Chat or
  @-mention conversational interactions.

### Claim 3: Configuring a comment trigger requires the automation author to specify the exact comment text that should activate it

- **Evidence**: Single explicit sentence describing the configuration step,
  with no further elaboration on matching semantics.
- **Confidence**: emerging (the requirement to specify trigger text is
  settled; the matching mechanics — substring, exact match, regex, case
  sensitivity — are not documented anywhere in the source or the linked doc)
- **Quote**: "When configuring an automation, specify the comment text that
  should trigger it."
- **Our assessment**: This is the single most operationally important
  sentence in the changelog, and it is also the least specific. Compare to
  gh-aw's `slash_command` trigger (`docs-ghaw-chatops.md` Claim 1), which
  has a fully documented schema — a `name:` field for the command string,
  an `events:` field for comment-context filtering, and a `roles:` field for
  caller authorization. GitHub's changelog gives none of that detail for
  Copilot automations: no confirmation of whether "comment text" means an
  exact match, a leading command-like token (e.g., `/docs`), or a
  free-text substring search. For Ch02: flag this as an open question for
  practitioners — until the doc catches up, teams should test the matching
  behavior empirically before relying on it for precise triggering (e.g.,
  confirm whether a comment containing the trigger text anywhere fires the
  automation, or only an exact match).

### Claim 4: The feature is accessed via the Agents tab in a repository, under an "Automations" sidebar entry

- **Evidence**: Explicit two-step navigation instruction in the changelog.
- **Confidence**: settled (first-party UI navigation instruction)
- **Quote**: "To get started, click through to the Agents tab in your
  repository, then pick Automations in the sidebar."
- **Our assessment**: This confirms automations (including the new comment
  trigger) are configured through the same "Agents" surface used for other
  Copilot cloud agent (CCA) invocation paths (issue assignment, Agents tab
  task start, @copilot mentions — see `docs-github-copilot-cca-fix-failing-actions.md`
  Claim 1's taxonomy). Automations are a distinct sub-feature within that
  surface, not a new top-level entry point. For Ch02: when documenting the
  CCA/Agents tab UI, note "Automations" as a persistent-configuration
  sibling to one-off task invocation, not a separate product surface.

### Claim 5: Automations are available to existing Copilot Pro, Pro+, Max, Business, and Enterprise subscribers, with Business/Enterprise additionally requiring administrator enablement of the Copilot cloud agent policy

- **Evidence**: Explicit tier list and administrator-gate statement in the
  changelog's closing paragraph.
- **Confidence**: settled (explicit first-party tier and prerequisite
  statement)
- **Quote**: "Automations are available for existing Copilot Pro, Pro+, Max,
  Business, and Enterprise users. Copilot Business and Copilot Enterprise
  users need the Copilot cloud agent policy enabled by an administrator."
- **Our assessment**: Unlike the "Fix with Copilot" workflow-failure feature
  (`docs-github-copilot-cca-fix-failing-actions.md` Claim 5, Business/
  Enterprise only), comment-triggered automations are available to
  individual Pro/Pro+/Max subscribers without an admin gate — only the
  Business/Enterprise tiers carry the administrator-enablement prerequisite.
  This is consistent with the general CCA automations feature (which the
  changelog frames as an existing capability being extended, not a brand
  new one) rather than an enterprise-only rollout. For Ch05 (Team Adoption):
  individual/Pro users can adopt comment-triggered automations without
  waiting on an admin; Business/Enterprise teams still need the
  cloud-agent-policy prerequisite already documented for other CCA features.

### Claim 6: Automations more broadly (the four pre-existing trigger types, per the linked reference doc) are private to their creator, are not stored in Git, are scoped to a single repository, cannot run in public repositories, and consume GitHub Actions minutes and AI Credits each time they run

- **Evidence**: These constraints are documented on the linked "About
  Copilot automations" reference page, not in the changelog itself. The
  changelog does not restate them for the comment trigger specifically, but
  they are stated as properties of "automations" as a whole, and the
  comment trigger is presented as an additional trigger option for the same
  feature, not a separate feature.
- **Confidence**: emerging (settled as a description of the pre-existing
  four trigger types; inferred, not explicitly confirmed by either source,
  that these constraints also govern the new comment trigger — see
  Extraction Notes)
- **Quote**: "An automation is private to the user who created it. Other
  people, including repository administrators, can't see your automations."
  / "They are not committed to Git, so they are not versioned alongside
  your code or managed through pull requests." / "An automation can only
  take action in the single repository it is scoped to." / "The repository
  must be private or internal. Automations are not available in public
  repositories." / "Each time an automation runs, it starts a Copilot cloud
  agent session that uses GitHub Actions minutes and GitHub AI Credits."
  (all from "About Copilot automations")
- **Our assessment**: The public-repository exclusion is the most
  significant constraint for guide purposes: if it extends to comment
  triggers (plausible but unconfirmed), the "generate documentation" and
  "create follow-up tasks" use cases from Claim 2 are unavailable to
  open-source maintainers using public GitHub repos — a meaningful
  limitation compared to gh-aw's `slash_command` trigger, which is
  explicitly designed for and documented with public-repository risk
  guidance (`docs-ghaw-chatops.md` Claim 4, "avoid `roles: all` in public
  repositories"). The "private to the creator, invisible to admins"
  property is also notable for governance: unlike gh-aw workflows (which
  are committed to the repo, visible to anyone with read access, and
  reviewable in a PR), a Copilot automation's configuration — including
  which comment text triggers it and what prompt it runs — is not
  discoverable by a repository admin without asking the creator. For Ch05
  (Team Adoption / Enterprise Governance): flag this visibility gap as a
  governance consideration — teams cannot audit which comment-triggered
  automations exist in a repository the way they can audit a `.github/workflows/`
  directory.

### Claim 7: The general automations permission rule — ignoring trigger events from users without write access to the repository by default, with an opt-in override — is documented for automations broadly but not confirmed for the comment trigger specifically

- **Evidence**: Stated on the linked "About Copilot automations" page as a
  property of automations' event handling, framed as a prompt-injection
  mitigation. The page was fetched and checked specifically for any
  comment-trigger-specific permission language; none was found.
- **Confidence**: anecdotal (the rule is settled for automations generally,
  but its applicability to the new comment trigger — announced one day
  before this note's extraction — is not confirmed by either source
  examined)
- **Quote**: "To reduce the risk of prompt injection, automations ignore
  events triggered by users who don't have write access to the repository
  by default... You can opt in to allowing these events if you need to."
- **Our assessment**: If this rule extends to comment triggers, it means a
  comment from a non-write-access user (e.g., an external contributor on a
  public... except automations don't run on public repos per Claim 6, so
  more precisely: an external collaborator without write access on a
  private/internal repo) would not fire the automation by default, closing
  off the most obvious abuse vector (a low-privilege user posting the
  trigger phrase to invoke an automation with elevated tool access). This
  is the single biggest open governance question the Prospector's triage
  flagged ("does this create new surface for accidental automation
  invocation?") and this source cannot answer it definitively for the new
  trigger type. For Ch03 (Safety and Verification): until GitHub's docs
  confirm the write-access filter applies to comment triggers, treat this
  as an unconfirmed-but-plausible mitigation, not a documented guarantee —
  practitioners configuring comment triggers should verify the effective
  permission behavior themselves rather than assume parity with the other
  four trigger types.

## Concrete Artifacts

### Verbatim Text of Source Changelog (August 3, 2026)

```
Title: Trigger Copilot automations with comments

You can now create Copilot cloud agent automations that run when an issue
comment or pull request comment is created.

Common use cases include:

Generate documentation: Comment on a pull request to automatically generate
or update documentation based on your code changes.

Investigate errors: Comment on an issue to trigger an automation that
investigates stack traces or error logs.

Create follow-up tasks: Comment on a pull request to have an automation
automatically create follow-up issues for refactoring or technical debt.

When configuring an automation, specify the comment text that should
trigger it. To get started, click through to the Agents tab in your
repository, then pick Automations in the sidebar.

Automations are available for existing Copilot Pro, Pro+, Max, Business,
and Enterprise users. Copilot Business and Copilot Enterprise users need
the Copilot cloud agent policy enabled by an administrator.

Learn more in "About Copilot automations" in the GitHub Docs.
```

Source: https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments
Retrieved: 2026-08-04 via `curl` (rendered HTML, tag-stripped) — text
cross-checked against an independent WebFetch summarization; content
consistent.

### Copilot Automations — Trigger Type Comparison (as of 2026-08-04)

```
Trigger type                    | Source
---------------------------------|----------------------------------------
On a schedule                    | "About Copilot automations" doc
When an issue is created         | "About Copilot automations" doc
When a PR is opened              | "About Copilot automations" doc
When a PR is synchronized        | "About Copilot automations" doc
When an issue/PR comment is      | THIS changelog (2026-08-03) — NOT YET
  created (NEW)                  |   reflected in the "About Copilot
                                  |   automations" doc as of 2026-08-04
```

### Automation Configuration Fields (from linked "About Copilot automations" doc; comment-trigger-specific fields not separately confirmed)

```
When you create an automation, you define:
  - A name to identify the automation
  - A prompt describing the task you want Copilot to perform
  - One or more triggers that determine when the automation runs
  - The model Copilot uses
  - The tools Copilot can use

Optional filters (documented for issue/PR triggers, not confirmed for
comment triggers):
  - Search query filter (issue-created trigger)
  - Search query filter + files-changed filter (PR-opened / PR-synchronized
    triggers)
```

Source: "About Copilot automations", https://docs.github.com/copilot/concepts/agents/cloud-agent/about-automations
Retrieved: 2026-08-04 via WebFetch (two independent fetches, targeted
specifically at locating any "comment" trigger mention; both fetches
confirmed no such mention is present on the page as currently published).

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cca-fix-failing-actions.md` Claim 1 (CCA invocation
    path taxonomy — issue assign, Agents tab, @copilot in PR, REST API,
    workflow-failure UI button): this source adds a sixth path/trigger
    conceptually, though it sits within the "Automations" sub-feature
    (persistent, author-configured) rather than the one-off task-invocation
    paths that note's taxonomy covers. Both sources corroborate that GitHub
    is steadily expanding the surface of events that can dispatch a Copilot
    cloud agent session without a human explicitly starting one each time.
  - `docs-ghaw-triggers-reference.md` Claim 10 (`issue_comment` events fire
    for both issue and PR comments; gh-aw provides explicit filtering to
    distinguish them): this changelog's phrasing — "an issue comment or
    pull request comment" as two distinct cases — suggests GitHub Copilot's
    automation platform also distinguishes issue vs. PR comment contexts,
    consistent with the same underlying GitHub Actions `issue_comment`
    event ambiguity that gh-aw documents and works around. Not confirmed
    directly, since the changelog doesn't describe the underlying event
    plumbing.

- **Contradicts**: None identified. No existing source note makes a claim
  this source materially opposes. No contradiction issue filed.

- **Extends**:
  - The linked "About Copilot automations" doc (not independently mined —
    no existing source note documents Copilot automations as a base
    feature prior to this note): this note is the first in the corpus to
    document Copilot cloud agent Automations at all, including both the
    four pre-existing trigger types (schedule, issue-created, PR-opened,
    PR-synchronized) captured secondhand via the linked doc, and the new
    comment trigger from the changelog itself.
  - `docs-ghaw-chatops.md` (the `slash_command` trigger for gh-aw): this
    note's Claim 3 draws a direct comparison — gh-aw's comment trigger has
    a fully specified schema (`name:`, `events:`, `roles:`) and documented
    sanitization/injection defenses (`docs-ghaw-chatops.md` Claims 5-7);
    GitHub Copilot's new comment trigger has none of that detail published
    yet. This note extends the corpus's comment-trigger comparison set with
    a second, less-specified implementation of the same general pattern
    (comment-as-dispatch-mechanism).
  - `docs-github-copilot-cca-fix-failing-actions.md` (CCA invocation
    taxonomy): extends that note's enumeration of ways a CCA session can
    start, adding "persistent, author-configured automation triggered by a
    matching comment" as a category distinct from the one-off/manual paths
    already catalogued there.

- **Novel**:
  - **Copilot cloud agent "Automations" as a base concept**: no prior
    source note in the corpus documents automations (scheduled or
    event-triggered persistent CCA configurations) at all. This note
    introduces the concept via the linked reference doc, then layers the
    new comment trigger on top.
  - **Comment-triggered automation as a fifth/newest trigger type,
    announced ahead of its own reference documentation**: the specific
    situation of a shipped GA feature whose canonical doc page has not yet
    been updated to list it is itself a notable, corpus-first data point
    about GitHub's own docs/changelog synchronization lag — relevant to how
    much practitioners should trust a "current" doc page as exhaustive on
    the day a related changelog ships.
  - **Explicit governance gap on private/undiscoverable automations**:
    Claim 6's finding that automations are invisible to repository admins
    (not just to other contributors) is new to the corpus and has direct
    Ch05 governance implications not previously captured for any CCA
    feature.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "Automations" as a distinct CCA
  configuration layer, separate from one-off task invocation (assign issue,
  Agents tab start, @copilot mention, REST API, "Fix with Copilot"). Within
  Automations, document five trigger types: schedule, issue-created,
  PR-opened, PR-synchronized, and (new) matching-comment-created. Flag the
  comment trigger's matching semantics (exact vs. substring vs. pattern) as
  unconfirmed pending doc updates — recommend practitioners test empirically
  before depending on precise trigger behavior.

- **Chapter 03 (Safety and Verification)**: Add the write-access-filter
  question as an open item: the general automations doc states non-write
  users are ignored by default with an opt-in override (Claim 7), but this
  is not confirmed for the comment trigger specifically. Until confirmed,
  recommend treating comment-triggered automations on repositories with
  external/lower-trust collaborators as needing manual verification of the
  effective permission behavior, by analogy to gh-aw's documented
  `roles:`-based access control (`docs-ghaw-chatops.md` Claims 3-4) which
  Copilot automations do not yet appear to expose as a configurable field.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Add the
  visibility/audit gap from Claim 6 — automations are private to their
  creator and invisible even to repository admins, and are not stored in
  Git or reviewable via pull request. Recommend this as a governance
  caveat: teams adopting Copilot automations (comment-triggered or
  otherwise) have no built-in mechanism to inventory what automations exist
  in a repository, unlike gh-aw workflows which are committed, visible
  files. Also note the tier/admin-gate split from Claim 5: Pro/Pro+/Max
  users can self-serve; Business/Enterprise requires the existing
  cloud-agent-policy administrator prerequisite already documented
  elsewhere in the corpus.

- **Chapter 01 (Daily Workflows)**: Add "comment as task dispatch" as a
  named interaction pattern for Copilot cloud agent, distinct from
  conversational @-mentions or manual task starts — citing the three use
  cases in Claim 2 (generate docs, investigate errors, create follow-up
  issues) as the vendor's own framing of where this pattern is expected to
  add value.

## Extraction Notes

1. **Changelog is thin (~120 words)**: consistent with other GitHub
   changelog entries in the corpus (e.g.,
   `docs-github-copilot-cca-fix-failing-actions.md`). All claims directly
   extractable from the changelog text are exhausted in Claims 1-5. Claims
   6-7 draw on the linked "About Copilot automations" reference page to
   provide governance and constraint context, following MINER.md §1's
   instruction to follow substantive linked pages.

2. **Documentation lag is itself a finding, not an extraction failure**: I
   fetched the linked "About Copilot automations" page twice, the second
   time with a prompt specifically instructing the model to search the
   entire page for any mention of "comment" triggers. Both fetches
   confirmed no comment-trigger content exists on that page as currently
   published (checked 2026-08-04, one day after the changelog). This means
   several operationally important questions the Prospector's triage
   explicitly asked about — exact comment-matching semantics, whether the
   general write-access permission filter applies to the comment trigger,
   whether comment triggers can be author-filtered — cannot be answered
   from currently available first-party sources. I have marked the
   relevant claims (3, 6, 7) as "emerging" or "anecdotal" rather than
   "settled" to reflect this, and the overall confidence as "emerging"
   rather than "settled" despite the source being an official GitHub
   changelog, because the changelog alone under-specifies the mechanics a
   practitioner would need to safely deploy this feature.

3. **Verbatim changelog text obtained via direct HTML fetch**: WebFetch's
   first pass on the changelog URL returned a reasonable paraphrase/summary
   rather than exact prose (typical of WebFetch's summarization behavior).
   To get verbatim text for the Quote fields and Concrete Artifacts section,
   I fetched the rendered HTML directly via `curl` (following the site's
   redirect) and stripped tags programmatically, then manually verified the
   resulting text against the WebFetch summary for consistency. All quotes
   in this note are taken from that verbatim extraction, not from the
   WebFetch paraphrase.

4. **Related same-day changelog entries not mined**: The changelog page
   links to two other August 2026 entries ("Customize the reasoning level
   for Copilot cloud agent," "Enterprise team specialization for managed
   settings") as adjacent releases. The latter already has a corpus note
   (`docs-github-copilot-enterprise-team-specialization-managed-settings.md`,
   per recent repo history). The reasoning-level entry was not followed —
   it is a separate feature not directly relevant to comment triggers and
   would warrant its own source issue if not already filed.

5. **No contradictions filed**: Reviewed existing source notes for
   conflicting claims about Copilot automations, CCA invocation paths, and
   comment-based triggers generally. No existing note makes a claim this
   source materially opposes — the corpus simply had no prior coverage of
   Copilot Automations as a concept. No contradiction issue filed per
   MINER.md §4a.
