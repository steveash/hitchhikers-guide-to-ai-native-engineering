---
source_url: https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
source_type: docs
title: "Updates to GitHub Copilot for Slack and Microsoft Teams"
author: GitHub (official changelog)
date_published: 2026-09-25
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: emerging
issue: "#3721"
---

# Updates to GitHub Copilot for Slack and Microsoft Teams

> GitHub's September 25, 2026 changelog documents a maturity pass on its
> August 2026 Slack/Teams Copilot cloud agent integrations — richer
> conversation context (Slack attachments/message links; Teams inline
> images, forwarded messages, channel-thread history), mid-conversation
> model switching, Slack default owners/repositories, duplicate-issue
> checking with conversation-traceable links, and a named list of
> platform-specific reliability fixes, including one with real security
> weight: Slack repository switching was made "safer so superseded
> sessions cannot continue acting in the old repository."

## Source Context

- **Type**: docs (GitHub official changelog, `github.blog/changelog`,
  published September 25, 2026, tagged "Improvement," "collaboration
  tools," and "copilot"; a roughly 2-minute-read feature/maintenance
  update to integrations first announced August 21, 2026). Fetched via
  `curl` with a browser user-agent against the page's `<article>` element
  directly, not through a summarizing WebFetch pass — an initial WebFetch
  pass was run first for orientation and then discarded once the raw HTML
  extraction surfaced multiple material wording differences (see
  Extraction Notes item 1). The two pages this changelog links to for
  setup — "Integrating Copilot cloud agent with Slack" and "Integrating
  GitHub Copilot cloud agent with Microsoft Teams" — are the same how-to
  docs already fully mined in `docs-github-copilot-slack-shared-agentic-work.md`
  and `docs-github-copilot-teams-shared-agentic-work.md`; both were
  re-fetched (via their embedded Next.js `renderedPage` JSON, the same
  extraction method those sibling notes used) specifically to check
  whether they had been updated to reflect this changelog's new features
  — they had not, as of this extraction (see Claim 9).
- **Author credibility**: First-party GitHub product changelog.
  Authoritative for feature existence and stated behavior. Not a source
  for adoption data, independent verification of the reliability fixes,
  or user-experienced before/after comparison — no customer quotes, usage
  metrics, or case studies appear in the page.
- **Scope**: Covers incremental context, control, and reliability updates
  to the Slack and Teams Copilot cloud agent integrations documented at
  launch in the two August 21, 2026 sibling sources. Does NOT cover: the
  underlying identity/permission model, the "Slack Code" channel
  mechanic, cloud-sandbox architecture or billing, or the issue-creation
  workflow — none of that changed in this update and none of it is
  restated here (it remains sourced from the two sibling notes). Also
  does not name specific model versions available for the new
  mid-conversation model-switching control.

## Extracted Claims

### Claim 1: Slack conversations can now supply supported files, attachments, and message links as agent context, while Teams conversations can supply inline images, forwarded-message context, and channel/thread history

- **Evidence**: The changelog's "Better context for the work you're
  already doing" section, its first sentence.
- **Confidence**: settled (first-party description of a shipping context
  expansion, stated per-platform)
- **Quote**: "You can now use supported Slack files, attachments, and message links as context. In Teams, Copilot can work with inline images, forwarded-message context, and channel and thread history."
- **Our assessment**: This is a genuine platform-specific split, not a
  single feature applied identically to both integrations: Slack gains
  file/attachment/message-link context, while Teams specifically gains
  inline-image and forwarded-message handling plus (re-affirmed)
  channel/thread history. Neither sibling note (`docs-github-copilot-slack-shared-agentic-work.md`,
  `docs-github-copilot-teams-shared-agentic-work.md`) documents
  attachments, files, message links, or forwarded messages as usable
  context inputs — both describe only "the entire thread" as the capture
  unit. This extends, rather than corrects, that picture: the *capture
  scope* (entire thread) is unchanged, but the *content types* Copilot
  can now parse within that thread have grown.

### Claim 2: Copilot now checks for similar existing issues before creating a new one, includes direct links to the resulting work, and keeps a link back to the originating conversation so context stays traceable

- **Evidence**: The changelog's "Better context for the work you're
  already doing" section, second sentence.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Copilot also checks for similar issues before creating a new one, includes direct links to the resulting work, and keeps a link back to the originating conversation so the context remains easy to trace."
- **Our assessment**: Duplicate-issue checking is new to the corpus for
  this integration — neither sibling source's "Creating Issues with
  Copilot" documentation (`docs-github-copilot-slack-shared-agentic-work.md`
  Claim 12) mentions any deduplication step; that note's extracted
  example prompts show issue creation as a direct, unconditional action.
  The bidirectional linking (work → conversation, conversation → work)
  is also new: the sibling notes document that a PR or issue gets created
  "with a link to the conversation for review" (one direction) but not
  that the link is now maintained back from the conversation side as a
  standing traceability feature.

### Claim 3: Users can switch models for the next message in a Slack or Teams Copilot conversation, and Copilot keeps that choice for the rest of the conversation

- **Evidence**: The changelog's "More control over how you work" section,
  first sentence.
- **Confidence**: settled (first-party feature description)
- **Quote**: "You can switch models for the next message and keep that choice throughout the conversation."
- **Our assessment**: This is a chat-native instance of the model-tier
  selection pattern already documented for GitHub's cloud coding agents
  on github.com in `docs-github-copilot-agent-model-selection.md` (that
  source's Claim 1: "you can now select a model when kicking off a
  task"). The two differ in trigger point: github.com's cloud-agent model
  selection happens at task *kickoff*, while this Slack/Teams control lets
  a user change models *mid-conversation*, with the new choice persisting
  going forward rather than applying just once. Neither sibling Slack/
  Teams source documents any model-selection capability at all — this is
  the first mention of model choice for either chat integration.
  Separately, the same-day GitHub Copilot weekly digest
  (`docs-github-copilot-weekly-releases-sept21-2026.md` Claim 3) describes
  this identical feature with different wording ("Switch models
  mid-conversation, and Copilot keeps your choice for the rest of the
  thread") — see Cross-References for why this is treated as a wording
  variant, not a contradiction.

### Claim 4: In Slack, users can additionally set default owners and repositories, making it easier to keep work moving across repositories and shared conversations

- **Evidence**: The changelog's "More control over how you work" section,
  second and third sentences.
- **Confidence**: settled (first-party feature description, explicitly
  scoped to Slack only)
- **Quote**: "In Slack, you can also set default owners and repositories. This makes it easier to keep work moving across repositories and shared conversations."
- **Our assessment**: This extends, rather than replaces, the existing
  default-repository mechanism documented in
  `docs-github-copilot-slack-shared-agentic-work.md` Claim 11 (a channel
  can have a default repository, set via `@GitHub settings`, that is
  otherwise implicitly set by the first session in that channel). "Default
  owners" is a new configuration axis not present in that Claim 11's
  description or in the current how-to doc text (see Claim 9 below) — it
  is unclear from this changelog alone whether "owner" here means a
  default GitHub org/user namespace distinct from a specific default
  repository, since the how-to doc has not yet been updated to explain
  the mechanic.

### Claim 5: Copilot's handling of longer-running tasks has been improved with clearer implementation-plan status, better handling of interrupted or stale replies, and more predictable reconnection behavior when a conversation goes idle, applying across both Slack and Teams

- **Evidence**: The changelog's "Bug fixes and reliability improvements"
  section, first sentence — the only sentence in that section stated as a
  cross-platform improvement rather than scoped to one integration.
- **Confidence**: settled (first-party description of a shipped
  reliability improvement)
- **Quote**: "We've improved how Copilot handles longer-running tasks, including clearer implementation-plan status, better handling of interrupted or stale replies, and more predictable reconnection behavior when a conversation goes idle."
- **Our assessment**: This is a maturity signal for the async,
  cross-surface session-continuation model documented in both sibling
  notes (`docs-github-copilot-slack-shared-agentic-work.md` Claim 4,
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 2): a session
  that runs asynchronously while the user is away is exactly the kind of
  session that can go idle, get interrupted, or receive a stale reply —
  this update is direct evidence that the August 2026 launch version of
  that async model had rough edges serious enough to warrant a named fix
  a month later.

### Claim 6: In Microsoft Teams specifically, Copilot now more reliably retains channel-thread history, avoids duplicate answers, correctly handles Teams-converted images, and works more consistently with user-owned repositories and large channels

- **Evidence**: The changelog's "Bug fixes and reliability improvements"
  section, second sentence, explicitly scoped to "In Microsoft Teams."
- **Confidence**: settled (first-party enumeration of platform-specific
  bug fixes)
- **Quote**: "In Microsoft Teams, Copilot now more reliably retains channel-thread history, avoids duplicate answers, correctly handles Teams-converted images, and works more consistently with user-owned repositories and large channels."
- **Our assessment**: Each item here names a concrete prior failure mode
  that was not disclosed in the August 21 Teams launch source
  (`docs-github-copilot-teams-shared-agentic-work.md`): thread history
  being dropped, duplicate answers being sent, Teams' own image-conversion
  pipeline confusing the agent, and degraded behavior specifically with
  user-owned (as opposed to org-owned) repositories and large channels.
  None of these are named anywhere in the prior corpus — this is the
  first evidence in the guide's Copilot-Teams coverage that the public
  preview shipped with specific, now-named reliability gaps around scale
  (large channels) and repository ownership type (user-owned repos).

### Claim 7: In Slack specifically, Copilot improved implementation-plan recovery, fixed repository picker and code-channel issues, and made repository switching safer so that superseded sessions cannot continue acting in the old repository

- **Evidence**: The changelog's "Bug fixes and reliability improvements"
  section, third sentence, explicitly scoped to "In Slack."
- **Confidence**: settled (first-party enumeration of platform-specific
  bug fixes, one of which is a security-relevant correctness fix)
- **Quote**: "In Slack, we improved implementation-plan recovery, fixed repository picker and code-channel issues, and made repository switching safer so superseded sessions cannot continue acting in the old repository."
- **Our assessment**: This is the most operationally significant single
  sentence in the source. "Made repository switching safer so superseded
  sessions cannot continue acting in the old repository" is a direct
  admission that, prior to this fix, a Slack Copilot session that had been
  superseded (e.g., by a user changing the default repository or starting
  a new session) could continue taking action against the *previous*
  repository — a stale-session-writes-to-wrong-repo failure mode. This
  sharpens the "Slack Code" channel-lifecycle picture in
  `docs-github-copilot-slack-shared-agentic-work.md` Claim 5 (one channel
  per task, steer exclusively through that channel): the existence of a
  fix implies that, at launch, exclusivity was not fully enforced at the
  execution layer, only at the UI/instruction layer. For Ch03/Ch06: this
  is a concrete, named example of a chat-native agent's session-isolation
  guarantee failing in practice (not hypothetically) — worth citing when
  the guide discusses why "the agent says it's steering session A" is not
  the same guarantee as "the agent cannot act on behalf of a stale session
  B."

### Claim 8: Across both experiences, Copilot now provides more accurate messages when a task stalls, a connection is interrupted, or access settings prevent work from continuing

- **Evidence**: The changelog's "Bug fixes and reliability improvements"
  section, closing sentence.
- **Confidence**: settled (first-party statement of improved error/status
  messaging)
- **Quote**: "Across both experiences, Copilot now provides more accurate messages when a task stalls, a connection is interrupted, or access settings prevent work from continuing."
- **Our assessment**: This closes the loop on Claim 5's async-reliability
  improvements with a user-facing observability angle: better internal
  handling of stalls/interruptions/access-denial is only useful to a
  practitioner if the failure is legible in the chat, rather than a silent
  hang. This is a small but concrete "fail loudly and specifically" fix
  worth noting for Ch01/Ch03 alongside general guidance that chat-native
  agent surfaces should surface access-denied and stall conditions
  explicitly rather than leaving a thread hanging with no status update.

### Claim 9: As of this extraction, neither the Slack nor the Teams how-to documentation pages linked from this changelog describe any of the new features it announces (context expansion, model switching, default owners, duplicate-issue checking, or the named bug fixes)

- **Evidence**: Direct re-fetch of both linked how-to docs' `renderedPage`
  content (same extraction method as the sibling notes) on 2026-09-26,
  the day after this changelog published. Neither page's text contains
  "model," "switch," "owner," "duplicate," "similar issue," "attachment,"
  "message link," "forwarded," or "inline image" anywhere.
- **Confidence**: settled (direct textual absence, verified by re-reading
  both full pages, not inferred)
- **Quote**: (no direct quote — this is an absence, not a statement; the
  how-to docs' full current text is unchanged from what is already quoted
  verbatim in `docs-github-copilot-slack-shared-agentic-work.md` and
  `docs-github-copilot-teams-shared-agentic-work.md`)
- **Our assessment**: This is a documentation-lag finding, not a product
  claim: GitHub shipped and announced these features in the dedicated
  changelog before updating the reference how-to docs the changelog
  itself links to for "setup details and supported workflows." A
  practitioner reading only the how-to docs (rather than the changelog)
  would not learn about model switching, default owners, or the new
  context types at all. Worth flagging for the Smith: any guide text that
  cites the Slack/Teams how-to docs as the canonical reference should be
  paired with a pointer to this changelog (and future changelogs) for
  the more current feature set, since the two page types are not kept in
  sync in real time.

### Claim 10: The public preview remains available only to organizations on GitHub Copilot Business and Enterprise plans, with usage counted against existing Copilot entitlements and existing Copilot cloud agent budgets, and some capabilities rolling out gradually

- **Evidence**: The changelog's "Availability" section.
- **Confidence**: settled (first-party statement of plan eligibility and
  billing/rollout mechanics, unchanged from launch)
- **Quote**: "The public preview is available to organizations on GitHub Copilot Business and GitHub Copilot Enterprise plans. Usage counts against your existing Copilot entitlements and can be managed with existing Copilot cloud agent budgets. Some capabilities are rolling out gradually and may not yet be available in every workspace."
- **Our assessment**: This restates, rather than changes, the plan-tier
  gating already documented in both sibling notes' Claim 13/Claim 7 —
  included here for completeness since it confirms the integration is
  still public preview five weeks after launch, with no GA date
  announced, and that the new features in this update are subject to the
  same gradual-rollout caveat as the original launch.

## Concrete Artifacts

### Get started in Slack — updated steps (verbatim, from the changelog)

```
1. Make sure an administrator has enabled the Copilot cloud agent policy for your organization.
2. Install or upgrade the GitHub app for Slack.
3. Link your GitHub account and mention @GitHub in a conversation.

For setup details and supported workflows, see how to use Copilot coding agent with Slack.
(link: https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-slack)

Source: https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
```

### Get started in Microsoft Teams — updated steps (verbatim, from the changelog)

```
1. Make sure an administrator has enabled GitHub Copilot cloud agent and cloud sandboxes.
2. Install or upgrade the GitHub app for Microsoft Teams.
3. In Teams, mention @GitHub and follow the prompts to connect your GitHub account.

For setup details and supported workflows, see how to integrate GitHub Copilot cloud agent with Microsoft Teams.
(link: https://docs.github.com/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams)

Source: https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
```

### Full "Bug fixes and reliability improvements" section (verbatim, from the changelog)

```
We've improved how Copilot handles longer-running tasks, including clearer
implementation-plan status, better handling of interrupted or stale replies,
and more predictable reconnection behavior when a conversation goes idle. In
Microsoft Teams, Copilot now more reliably retains channel-thread history,
avoids duplicate answers, correctly handles Teams-converted images, and works
more consistently with user-owned repositories and large channels. In Slack,
we improved implementation-plan recovery, fixed repository picker and
code-channel issues, and made repository switching safer so superseded
sessions cannot continue acting in the old repository. Across both
experiences, Copilot now provides more accurate messages when a task stalls,
a connection is interrupted, or access settings prevent work from continuing.

Source: https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
```

## Cross-References

### Cross-reference verification notes

`docs-github-copilot-slack-shared-agentic-work.md`,
`docs-github-copilot-teams-shared-agentic-work.md`,
`docs-github-copilot-agent-model-selection.md`, and
`docs-github-copilot-weekly-releases-sept21-2026.md` were each re-read in
full during this extraction per MINER.md §4b, and every claim number
cited above was located and confirmed against that note's own numbered
`### Claim N:` headings in document order before writing this section.

- **Corroborates**:
  - `docs-github-copilot-weekly-releases-sept21-2026.md` Claim 3 — the
    same-day GitHub Copilot weekly digest describes the identical set of
    updates (model switching, duplicate-issue prevention, plan-status
    reliability, Slack context sharing) in compressed, differently-worded
    bullets. The digest text: "Choose the best model for each task.
    Switch models mid-conversation, and Copilot keeps your choice for the
    rest of the thread. In Slack, you can also set channel defaults." /
    "Avoid duplicate issues since Copilot now checks for similar existing
    issues before creating a new one." — describes the same two features
    as this source's Claims 3 and 2, respectively, but the digest's own
    text does not mention Teams' inline-image/forwarded-message context
    expansion, the conversation-traceable linking half of Claim 2, or any
    of the platform-specific bug fixes in Claims 6–7 at all. This
    confirms the established pattern (already noted in that digest note's
    own Source Context) that the weekly digest is a compressed pointer to
    a fuller dedicated changelog — except here the digest links only to
    the generic how-to docs, not to this dedicated changelog, so a reader
    following only the digest's links would never reach this source's
    additional detail.
  - `docs-github-copilot-agent-model-selection.md` Claim 1 — corroborates
    the general pattern of GitHub exposing model-tier choice as an
    operator-facing control across its hosted-agent surfaces; this source
    extends that pattern to chat-native mid-conversation switching (see
    Claim 3's assessment for the distinction).

- **Contradicts**: None identified as a MINER.md §4a contradiction. One
  wording-level tension was evaluated and is documented as an
  extraction-accuracy note rather than filed: this changelog states model
  choice can be switched "for the next message" and is then kept
  "throughout the conversation" (Claim 3), while the same-day weekly
  digest describes switching "mid-conversation" with the choice kept "for
  the rest of the thread." Both describe the same net behavior (a
  mid-conversation switch that persists going forward) using different
  granularity of phrasing — "for the next message" specifies the switch
  applies starting from the immediately following message, which the
  digest's shorter phrasing omits but does not contradict. This does not
  meet the "materially opposes... both claims would lead to different
  guide advice" bar in MINER.md §4a — both sources agree on the
  operationally relevant fact (the new model choice is not a one-off, it
  persists), so no contradiction issue filed.

- **Extends**:
  - `docs-github-copilot-slack-shared-agentic-work.md` — adds file/
    attachment/message-link context support (Claim 1), duplicate-issue
    checking and bidirectional conversation linking (Claim 2), mid-
    conversation model switching (Claim 3), default owners as a new
    configuration axis alongside the existing default-repository
    mechanic (Claim 4), and — most significantly — discloses that the
    launch-version "steer exclusively through that channel" guarantee
    (that note's Claim 5) was not fully enforced at the execution layer
    until this update's repository-switching safety fix (Claim 7 here).
  - `docs-github-copilot-teams-shared-agentic-work.md` — adds inline-
    image and forwarded-message context support (Claim 1) and discloses
    four previously-undocumented Teams reliability gaps: dropped
    thread history, duplicate answers, mishandled Teams-converted images,
    and degraded behavior with user-owned repositories and large channels
    (Claim 6) — none of which appear in that note's launch-day coverage.
  - `docs-github-copilot-agent-model-selection.md` — extends the
    corpus's coverage of GitHub-hosted model-tier selection from a
    task-kickoff control (github.com cloud agents) to a mid-conversation,
    persistent-choice control (Slack/Teams chat sessions) — see Claim 3.

- **Novel** (what this note adds that no prior source covers):
  - **A named, disclosed prior security/correctness gap in session
    isolation**: "superseded sessions cannot continue acting in the old
    repository" (Claim 7) is the first source in the corpus to document
    that a chat-native coding agent's session-exclusivity guarantee had a
    real execution-layer gap, not just a UI-level instruction, and that
    the gap has now been closed. No other Copilot chat-integration source
    discusses a stale-session-writes-to-wrong-target failure mode.
  - **Documentation lag between a dedicated changelog and its own linked
    how-to docs** (Claim 9): a directly-verified, dated example of
    first-party GitHub documentation being out of sync with itself —
    useful as a general caution for how the guide should treat
    "changelog announces, how-to doc doesn't yet reflect it" as an
    expected transient state for public-preview features, not an error to
    be second-guessed.
  - **Platform-specific content-type context expansion** (Claim 1):
    Slack and Teams gaining *different* new context input types
    (files/attachments/message-links vs. inline-images/forwarded-
    messages) rather than a single feature ported identically to both, is
    new to the corpus's picture of how GitHub evolves these two sibling
    integrations independently despite their shared underlying template
    (documented in both sibling notes' Cross-References sections).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Update the existing Slack/Teams
  `@GitHub`-mention coverage (sourced from the two sibling notes) to
  note the expanded context inputs (Claim 1: Slack files/attachments/
  message links, Teams inline images/forwarded messages), the new
  duplicate-issue check before creating an issue (Claim 2), and
  mid-conversation model switching (Claim 3) as current-state behavior,
  not just the August 2026 launch feature set. Flag "default owners" in
  Slack (Claim 4) as an under-documented configuration option — the
  how-to doc does not yet explain it (Claim 9), so any guide text should
  say "check `@GitHub settings` in-product" rather than asserting a
  specific mechanic.

- **Chapter 03 (Safety and Verification) / Chapter 06 (Security Threat
  Model)**: Add Claim 7's disclosed repository-switching fix as a
  concrete, named example that a chat-native agent's stated
  session-exclusivity guarantee ("steer exclusively through that
  channel," per `docs-github-copilot-slack-shared-agentic-work.md` Claim
  5) is a design intent, not an execution-layer guarantee, until proven
  otherwise — teams relying on Copilot's chat integrations for
  multi-repository work should not assume old-session isolation is
  airtight for integrations that are still in public preview.

- **Chapter 04 (Agentic Workflows)**: Add mid-conversation model
  switching in Slack/Teams (Claim 3) alongside the github.com cloud-agent,
  task-kickoff model selection already documented via
  `docs-github-copilot-agent-model-selection.md`, as a second, distinct
  point in the guide's growing coverage of GitHub surfacing model-tier
  choice as an explicit operator control rather than a hidden default.

- **Chapter 05 (Team Adoption)**: Note that this integration remains
  public preview with no GA date five weeks after its August 21, 2026
  launch (Claim 10), and that GitHub is actively iterating on named
  reliability gaps (Claims 5–8) rather than treating the initial public
  preview as feature-complete — relevant context for teams deciding
  whether to pilot the Slack/Teams integration now versus waiting for a
  more mature release.

## Extraction Notes

1. **Raw HTML extraction used instead of a summarizing WebFetch pass, and
   the difference mattered.** An initial WebFetch pass on the changelog
   URL returned a paraphrased summary (e.g., rendering Claim 3's actual
   text — "You can switch models for the next message and keep that
   choice throughout the conversation" — as "Users can switch AI models
   mid-conversation while maintaining that selection throughout the
   discussion," and rendering Claim 7's "made repository switching safer
   so superseded sessions cannot continue acting in the old repository"
   as the much vaguer "safer repository switching," dropping the specific
   superseded-session detail entirely). The WebFetch pass was discarded
   once `curl` with a browser user-agent successfully retrieved the raw
   `<article>` HTML; every `Quote` field above was copied from that raw
   HTML, not from the discarded WebFetch summary.
2. **Both linked how-to docs re-fetched to check for updates, per
   MINER.md §1, and found unchanged.** Both pages were retrieved via
   their embedded Next.js `renderedPage` JSON (same method used in the
   sibling notes) specifically to check whether they now documented any
   of this changelog's new features. Neither did (Claim 9) — this
   negative result is itself extracted as a claim since it is directly
   useful to the Smith.
3. **The same-day weekly digest was read in full, not just grepped.**
   `docs-github-copilot-weekly-releases-sept21-2026.md`'s own Claim 3 was
   read together with the underlying raw HTML of its source page
   (independently re-fetched via `curl` at
   `github.blog/changelog/2026-09-25-github-copilot-weekly-releases-september-21`
   during this extraction, to confirm the digest's exact wording rather
   than trusting the sibling note's quote alone) to verify the digest
   links to the generic how-to docs, not to this dedicated changelog —
   confirming the two GitHub pages are independent write-ups of the same
   underlying product change, not one linking to the other.
4. **No customer or adoption evidence in the page.** This is first-party
   GitHub product documentation describing incremental changes to a
   public-preview feature; no named customer, usage metric, or
   independent review appears. Overall confidence is rated "emerging"
   rather than "settled," consistent with both sibling notes' rationale:
   the integration remains public preview with no GA date, and no
   independent verification of any claim (especially the disclosed
   repository-switching fix in Claim 7) exists outside GitHub's own
   documentation.
5. **No contradiction with any existing corpus note was found requiring a
   filed issue.** Reviewed `docs-github-copilot-slack-shared-agentic-work.md`,
   `docs-github-copilot-teams-shared-agentic-work.md`,
   `docs-github-copilot-agent-model-selection.md`, and
   `docs-github-copilot-weekly-releases-sept21-2026.md` in full. The one
   wording-level tension found (Claim 3's Cross-References entry) was
   evaluated against the MINER.md §4a bar and judged not to meet it. No
   contradiction issue filed.
6. **Prospector's triage comments (three separate passes on this issue)
   ranged from "low novelty, incremental update" to "worth mining for
   adoption/workflow insight."** Having read the changelog's raw HTML in
   full, the "low novelty" framing undersells one specific item: Claim
   7's disclosed session-isolation fix is a genuinely new, security-
   relevant data point not present in either August 21 launch source.
   The rest of the update (context expansion, model switching, bug fixes)
   is legitimately incremental relative to the sibling notes' comprehensive
   launch-day coverage, consistent with the "medium/low novelty" framing
   for those portions.
