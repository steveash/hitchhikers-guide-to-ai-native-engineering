---
source_url: https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31
source_type: docs
title: "GitHub Copilot weekly releases — August 31"
author: GitHub (official changelog)
date_published: 2026-09-04
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: settled
issue: "#3249"
---

# GitHub Copilot Weekly Releases — August 31

> GitHub's September 4, 2026 weekly roundup covers four surfaces — general model
> rollouts, the Copilot app and CLI, GitHub Copilot for JetBrains, and VS Code
> 1.136 — and is the first corpus documentation of Claude Fable 5.1 arriving
> inside GitHub Copilot, of "Agent Merge" (a public-preview feature that resolves
> review feedback, failed checks, and merge conflicts to get a PR ready to
> merge), and of content exclusions reaching the standalone Copilot app and CLI
> (previously documented only for Copilot code review). It also restates, without
> new detail, two already-documented items: Gemini 3.8 Flash's Copilot debut
> (`docs-github-copilot-gemini38flash-availability.md`, one day earlier) and the
> JetBrains "Copilot harness" GA promotion
> (`docs-github-copilot-jetbrains-harness-ga-aug2026.md`, eleven days earlier).

## Source Context

- **Type**: docs (GitHub official product changelog, September 4, 2026; self-tagged
  "Release," "1 minute read"; roughly 130 words of primary content across four
  sections — "GitHub Copilot, general," "GitHub Copilot app and Copilot CLI,"
  "GitHub Copilot in JetBrains," and "VS Code 1.136 release updates." Confirmed via
  direct raw-HTML fetch with `curl`, not solely a WebFetch AI summary — an initial
  WebFetch pass paraphrased several bullets (e.g., rendering "Copilot app and CLI
  now honor content exclusions" as an invented "Content Exclusions Feature" heading
  not present in the source), consistent with the AI-summarization risk already
  flagged in prior notes in this family (see Extraction Note 1).
- **Author credibility**: GitHub engineering team announcing production and
  public-preview/experimental features across four Copilot product surfaces.
  Authoritative for: the existence of each feature, the named plan tiers for the
  two model rollouts, and the one-line behavioral description given for each VS
  Code 1.136 item. Not authoritative for: adoption metrics, how "Agent Merge"
  resolves conflicts mechanistically, whether Claude Fable 5.1 is covered by
  GitHub's data retention agreement (the source is silent on this, unlike the
  exclusion criteria documented for "Claude Fable 5" in
  `docs-github-copilot-global-model-policy-ga.md`), or performance/quality
  comparisons for either newly-listed model.
- **Scope**: A weekly digest covering the period since the prior weekly release
  (week of August 31, 2026). No linked sub-pages were followed — unlike several
  prior weekly digests in this family (e.g.,
  `docs-github-copilot-weekly-releases-aug10-2026.md`, which followed a JetBrains
  sub-changelog), this entry contains no "Read the full [surface] update" links,
  only the general VS Code 1.136 release notes link (`aka.ms/VSCode/136`, not
  Copilot-specific, and consistent with the precedent in
  `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 2 of treating
  general VS Code release notes as out of scope for a Copilot-focused digest) and
  the "our list of all supported models" documentation link (general reference
  page, not fetched, consistent with
  `docs-github-copilot-gemini38flash-availability.md` Extraction Note 2's treatment
  of the same page). Does NOT cover: Visual Studio, Eclipse, Xcode, GitHub Mobile,
  or configuration detail for any listed feature beyond the one-line changelog
  description — this is an announcement-level summary, not a how-to guide.

## Extracted Claims

### Claim 1: Claude Fable 5.1 is now available in GitHub Copilot, accessible to Copilot Pro+, Max, Business, and Enterprise users

- **Evidence**: "GitHub Copilot, general" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Claude Fable 5.1 is available to Copilot Pro+, Max, Business, and Enterprise users."
- **Our assessment**: This is the first corpus documentation of Claude Fable 5.1
  by name as a GitHub Copilot model-roster addition — no prior
  `docs-github-copilot-*` note names this specific version. It raises an
  unresolved open question rather than a confirmed contradiction:
  `docs-github-copilot-global-model-policy-ga.md` (Claim 5, corroborated by
  Claim 8's more complete list from the linked docs page) documents that "models
  not covered by GitHub's data retention agreement (e.g., Fable 5)" — named there
  specifically as "Claude Fable 5," not "5.1" — are excluded from *default*
  enablement regardless of an enterprise's policy setting, requiring explicit
  admin opt-in. This source states Fable 5.1 is "available" to Business and
  Enterprise users but says nothing about data-retention coverage or
  default-enablement status for this specific version. Two readings are both
  consistent with the text: (a) Fable 5.1 is a newer point release that has since
  been brought under GitHub's data retention agreement, making it eligible for
  the normal enabled-by-default treatment documented in
  `docs-github-copilot-gemini38flash-availability.md` Claim 6 for Gemini 3.8
  Flash; or (b) Fable 5.1 remains excluded from default enablement like its
  predecessor, and "available" here means selectable-if-explicitly-enabled, not
  on-by-default. This source does not disambiguate the two, and unlike the
  Gemini 3.8 Flash notice, it includes no "Enabling access" section describing
  admin-policy interaction at all. For Ch05 (Team Adoption — Enterprise
  Governance): flag this explicitly as an open question for admins rather than
  assuming Fable 5.1 will appear automatically for Business/Enterprise users the
  way Gemini 3.8 Flash was confirmed to.

### Claim 2: Gemini 3.8 Flash is rolling out to Copilot Pro, Pro+, Max, Business, and Enterprise users

- **Evidence**: "GitHub Copilot, general" section, second bullet.
- **Confidence**: settled (product fact restated from a prior, more detailed
  changelog published one day earlier)
- **Quote**: "Gemini 3.8 Flash is rolling out to Copilot Pro, Pro+, Max, Business, and Enterprise users."
- **Our assessment**: This is a one-day-later restatement of
  `docs-github-copilot-gemini38flash-availability.md` Claim 4, which documents
  the identical five-tier list ("Gemini 3.8 Flash will be available to Copilot
  Pro, Pro+, Max, Business, and Enterprise users") from the dedicated September
  3, 2026 changelog. This weekly digest adds no new surface, pricing, or
  admin-policy detail beyond what that dedicated note already covers in depth
  (eight named surfaces, introductory pricing through December 31 2026, gradual
  rollout, default-enablement confirmation) — consistent with the pattern
  documented in `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 3 and
  its "Our assessment," where this same weekly-digest series re-surfaces major
  standalone announcements from the same week rather than omitting them. No
  guide update needed beyond what the dedicated Gemini 3.8 Flash note already
  recommends.

### Claim 3: The GitHub Copilot app and Copilot CLI now honor content exclusions, keeping sensitive code out of context across agentic workflows

- **Evidence**: "GitHub Copilot app and Copilot CLI" section, sole bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Copilot app and CLI now honor content exclusions, keeping sensitive code out of context across agentic workflows."
- **Our assessment**: This extends content exclusion support beyond the surface
  documented in `docs-github-copilot-code-review-config-controls.md` Claim 4,
  which established content exclusion at repository/organization/enterprise
  levels specifically for Copilot code review (June 12, 2026). This is the first
  corpus documentation of content exclusions applying to the standalone Copilot
  app and Copilot CLI's general agentic workflows, not just the code-review
  agent — a materially broader scope, since app/CLI sessions can read and act on
  arbitrary repository content during a coding task, not only during a review
  pass. The source gives no mechanism detail (same path-based rule format as
  code review? a new configuration surface for app/CLI specifically?) and does
  not state whether this is a new capability or a pre-existing repo/org/enterprise
  content-exclusion policy simply now being *respected* by these two surfaces
  where it previously was not. For Ch05 (Team Adoption — Enterprise Governance):
  update the content-exclusion deployment checklist (from the June 12 note) to
  note that, as of September 4 2026, the same exclusion policy that gates
  Copilot code review's file access now also gates the standalone Copilot app and
  CLI — organizations that configured content exclusions expecting them to apply
  only to code review should re-verify scope now covers agentic app/CLI sessions
  too.

### Claim 4: GitHub Copilot's harness for JetBrains is now generally available, providing "faster feature delivery and better code quality"

- **Evidence**: "GitHub Copilot in JetBrains" section, sole bullet.
- **Confidence**: settled (product fact restated from a prior changelog in
  near-identical wording)
- **Quote**: "The GitHub Copilot harness is now generally available in Copilot for JetBrains, providing faster feature delivery and better code quality."
- **Our assessment**: This is a corroborating restatement of
  `docs-github-copilot-jetbrains-harness-ga-aug2026.md` Claim 1 ("Copilot harness
  is now generally available, providing faster feature delivery and better code
  quality"), published eleven days earlier (August 24, 2026), with identical
  substantive wording. This weekly digest even links directly back to that
  original changelog entry ("see our previous changelog about the release"),
  making the restatement explicit rather than incidental — unlike the Gemini 3.8
  Flash and MAI-Code-1.1-Flash restatement patterns documented elsewhere in this
  family, which did not self-link to their source announcement. No new
  information; the definitional gap flagged in the original note (what "Copilot
  harness" is architecturally, and whether it replaces or coexists with "Agent"
  mode) remains unresolved by this source.

### Claim 5: VS Code 1.136 introduces "Agent Merge," a public-preview feature that gets a pull request ready to merge by resolving review feedback, failed checks, and merge conflicts

- **Evidence**: "VS Code 1.136 release updates" section, first bullet.
- **Confidence**: emerging (explicitly public preview; no detail on the
  resolution mechanism)
- **Quote**: "Agent Merge is now in public preview and gets your pull request ready to merge by resolving review feedback, failed checks, and merge conflicts."
- **Our assessment**: This is the first corpus documentation of "Agent Merge" as
  a named feature, and it is notable for bundling three previously separate,
  individually-documented CCA capabilities into one merge-readiness agent:
  (1) applying review feedback, documented as its own dedicated feature in
  `docs-github-copilot-cca-apply-review-feedback.md` Claim 1 ("Fix with Copilot"
  dialog, May 19, 2026); (2) fixing failing checks, documented in
  `docs-github-copilot-cca-fix-failing-actions.md` Claim 1 ("Fix with Copilot"
  button on failing Actions runs, May 18, 2026); and (3) resolving merge
  conflicts, which no prior corpus source documents as an automated Copilot
  capability at all — the corpus's only merge-conflict-resolution automation to
  date is `blog-cursor-agent-swarm-model-economics.md` Claim 7, a third-party
  (Cursor) swarm-orchestration pattern using a dedicated reconciler agent, not a
  GitHub Copilot feature. The changelog does not state whether Agent Merge
  invokes the same underlying "Fix with Copilot" / cloud-agent mechanisms as the
  two May features or is a new, integrated implementation, nor does it describe
  what happens when review feedback, failing checks, and merge conflicts must
  all be resolved together and one resolution invalidates another (e.g., a
  conflict-resolution edit that reintroduces a lint failure). For Ch02 (Harness
  Engineering) and Ch04 (Agentic Workflows): document Agent Merge as the first
  "PR merge-readiness" agent in the corpus that unifies review-response,
  CI-failure-fixing, and conflict-resolution into a single invocation, and flag
  the interaction-ordering question as an open item pending a dedicated
  changelog entry.

### Claim 6: VS Code 1.136 adds experimental multi-root workspace support, bringing Copilot and Claude agent sessions to every folder in a workspace

- **Evidence**: "VS Code 1.136 release updates" section, second bullet.
- **Confidence**: emerging (explicitly experimental; no detail on session
  isolation or cross-folder coordination)
- **Quote**: "Multi-root workspaces are now experimental and bring Copilot and Claude agent sessions to every folder in your workspace."
- **Our assessment**: This is a different capability from the two other
  multi-root/multi-window features already in the corpus. It is distinct from
  `docs-github-copilot-jetbrains-harness-ga-aug2026.md` Claim 8 (JetBrains
  multi-root *customization discovery* — finding `.github/agents`-style
  configuration files across folders), which concerns configuration lookup, not
  session placement. It is also distinct from `docs-github-copilot-vscode-august-2026.md`
  Claim 6 (the Agent Host connecting *multiple VS Code windows* to *one shared
  running session*) — this VS Code 1.136 feature instead brings a session to
  *each folder* within a single multi-root workspace, the inverse topology
  (one-session-many-windows vs. many-folders-each-with-sessions). No prior
  corpus source documents Copilot or Claude agent sessions scoped per-folder
  within one multi-root VS Code workspace. The source does not state whether
  each folder's session is independent (separate context, separate history) or
  shares any state, nor whether this applies to VS Code's built-in Copilot
  agent, the Claude BYOK provider (`docs-github-copilot-byok-vscode.md`), or
  both equally — though naming both "Copilot and Claude" explicitly suggests
  parity across providers. For Ch02 (Harness Engineering — Workspace
  Management): document as a new experimental option for practitioners working
  in monorepo-adjacent or multi-project VS Code workspaces who want independent
  agent sessions per folder rather than one session scoped to the whole
  workspace.

### Claim 7: VS Code 1.136 adds experimental chat backgrounds, letting practitioners personalize the Agents window with built-in patterns or their own images

- **Evidence**: "VS Code 1.136 release updates" section, third bullet.
- **Confidence**: emerging (explicitly experimental; cosmetic feature)
- **Quote**: "Chat backgrounds are now experimental and let you personalize the Agents window with built-in patterns or custom images."
- **Our assessment**: A purely cosmetic personalization feature with no
  functional bearing on agentic workflows. No prior corpus source documents
  visual customization of the VS Code Agents window beyond functional UI
  changes (chat backgrounds pinning, side-by-side layouts in
  `docs-github-copilot-vscode-august-2026.md` Claim 1). Not significant enough
  for a dedicated guide callout; noted here for corpus completeness per
  MINER.md's instruction to extract every interesting claim rather than
  pre-filter for guide relevance.

### Claim 8: VS Code 1.136 adds chat sessions that organize related conversations into a hierarchy and show which ones need the practitioner's attention

- **Evidence**: "VS Code 1.136 release updates" section, fourth bullet.
- **Confidence**: settled (product fact stated directly; no preview qualifier,
  unlike Claims 5–7)
- **Quote**: "Chat sessions organize related chats into a hierarchy and show which ones need your attention."
- **Our assessment**: This extends, rather than duplicates, two prior
  session-organization features in the corpus. `docs-github-copilot-weekly-releases-aug3-2026.md`
  Claim 8 documented Copilot CLI's Sessions sidebar for managing multiple
  *concurrent, flat* sessions (open/close/switch via keyboard shortcuts) — no
  hierarchy or attention-indicator concept. `docs-github-copilot-chat-agent-sessions.md`
  Claim 1 documented Copilot Chat becoming a surface for *querying and
  searching* past sessions (by topic, title, recency) — a retrieval interface,
  not an organizational hierarchy. This VS Code 1.136 feature is the first
  corpus documentation of (a) a *hierarchical* (parent/child or grouped, not
  flat-list) session structure, and (b) an explicit "needs your attention"
  indicator surfaced at the session-list level rather than within an individual
  conversation. The source does not define what "related" means for grouping
  purposes (same repository? same PR? explicitly linked by the practitioner?)
  or what triggers the attention indicator (an agent's pending question, per
  the ask-user-prompt pattern in
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` Claim 6, or
  a completed session awaiting review?). For Ch01 (Daily Workflows) and Ch04
  (Agentic Workflows — Multi-Session): document this as VS Code's answer to
  the "too many concurrent sessions" problem, distinct from the CLI's flat
  sidebar and Copilot Chat's search-based retrieval — VS Code instead
  organizes by relationship and surfaces urgency directly in the list.

## Concrete Artifacts

### Full weekly digest — August 31, 2026 (published September 4, 2026), verbatim transcript

Extracted from raw HTML (not AI-summarized WebFetch output) to guarantee verbatim
quotes, per MINER.md §2a and the precedent set in this family's prior notes.

```
GitHub Copilot weekly releases — August 31
Source: github.blog/changelog, published 2026-09-04, retrieved 2026-09-05
Release, 1 minute read

INTRO
  This week, GitHub Copilot expands model choice and content protections,
  while VS Code adds new ways to manage agent sessions and get pull
  requests merge-ready.

GITHUB COPILOT, GENERAL
  [Claim 1]
  - Claude Fable 5.1 is available to Copilot Pro+, Max, Business, and
    Enterprise users.
  [Claim 2]
  - Gemini 3.8 Flash is rolling out to Copilot Pro, Pro+, Max, Business,
    and Enterprise users.
  (For more information, see our list of all supported models.
   Link: docs.github.com/copilot/reference/ai-models/supported-models
   — not fetched, general reference page.)

GITHUB COPILOT APP AND COPILOT CLI
  [Claim 3]
  - Copilot app and CLI now honor content exclusions, keeping sensitive
    code out of context across agentic workflows.

GITHUB COPILOT IN JETBRAINS
  [Claim 4]
  - The GitHub Copilot harness is now generally available in Copilot for
    JetBrains, providing faster feature delivery and better code quality.
  (Links to the August 24, 2026 changelog entry: "see our previous
   changelog about the release" —
   github.blog/changelog/2026-08-24-copilot-harness-generally-available-in-copilot-for-jetbrains
   — already fully mined as docs-github-copilot-jetbrains-harness-ga-aug2026.md.)

VS CODE 1.136 RELEASE UPDATES
  [Claim 5]
  - Agent Merge is now in public preview and gets your pull request
    ready to merge by resolving review feedback, failed checks, and
    merge conflicts.
  [Claim 6]
  - Multi-root workspaces are now experimental and bring Copilot and
    Claude agent sessions to every folder in your workspace.
  [Claim 7]
  - Chat backgrounds are now experimental and let you personalize the
    Agents window with built-in patterns or your own images.
  [Claim 8]
  - Chat sessions organize related chats into a hierarchy and show which
    ones need your attention.
  (Links to full VS Code 1.136 release notes: aka.ms/VSCode/136 — not
   fetched, general non-Copilot-specific release notes.)
```

*Source: raw HTML of
https://github.blog/changelog/2026-09-04-github-copilot-weekly-releases-august-31,
fetched directly via `curl` with a browser user-agent (not WebFetch
summarization alone) on 2026-09-05, then isolated to the `<article>` element,
block-level tags converted to line breaks, and remaining markup stripped. All
`Quote` fields above were checked by exact substring match against this
transcript.*

### Weekly digest restatement pattern (this note vs. prior family members)

```
Item                     This digest's framing              Already documented in
────────────────────────────────────────────────────────────────────────────────────────
Gemini 3.8 Flash         "rolling out" (Claim 2)             docs-github-copilot-gemini38flash-availability.md
                                                              (Sept 3, 2026 — 1 day earlier, far more detail)
Copilot harness GA       restated verbatim, self-linked      docs-github-copilot-jetbrains-harness-ga-aug2026.md
(JetBrains)              (Claim 4)                           (Aug 24, 2026 — 11 days earlier)
Claude Fable 5.1         first appearance (Claim 1)           none — novel to corpus
Content exclusions       first appearance for app/CLI         docs-github-copilot-code-review-config-controls.md
(app + CLI)              (Claim 3)                           documents it for code review only (June 12, 2026)
Agent Merge              first appearance (Claim 5)           none — novel; unifies capabilities from
                                                              docs-github-copilot-cca-apply-review-feedback.md
                                                              and docs-github-copilot-cca-fix-failing-actions.md
Multi-root workspaces    first appearance (Claim 6)           none — novel
Chat backgrounds         first appearance (Claim 7)           none — novel (cosmetic)
Chat sessions hierarchy  first appearance (Claim 8)           none — novel; distinct from CLI Sessions
                                                              sidebar and Copilot Chat session search
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-global-model-policy-ga.md`,
`docs-github-copilot-gemini38flash-availability.md`,
`docs-github-copilot-code-review-config-controls.md`,
`docs-github-copilot-jetbrains-harness-ga-aug2026.md`,
`docs-github-copilot-cca-apply-review-feedback.md`,
`docs-github-copilot-cca-fix-failing-actions.md`,
`docs-github-copilot-vscode-august-2026.md`,
`docs-github-copilot-weekly-releases-aug10-2026.md`,
`docs-github-copilot-weekly-releases-aug3-2026.md`,
`docs-github-copilot-chat-agent-sessions.md`,
`docs-github-copilot-jetbrains-otel-model-management-july2026.md`, and
`blog-cursor-agent-swarm-model-economics.md` were re-read directly in those
notes (via `### Claim N:` headings) before citing, per MINER.md §4b; claim
numbers are counted top-to-bottom in document order as they appear in each
cited note.

- **Corroborates** `docs-github-copilot-gemini38flash-availability.md` (Claim 4,
  Gemini 3.8 Flash's five-tier plan eligibility): Claim 2 of this note restates
  the identical tier list one day later with no new detail.

- **Corroborates** `docs-github-copilot-jetbrains-harness-ga-aug2026.md` (Claim
  1, Copilot harness GA): Claim 4 of this note restates the identical GA fact
  eleven days later, with an explicit self-link back to the original changelog
  entry.

- **Extends** `docs-github-copilot-global-model-policy-ga.md` (Claim 5 and Claim
  8, "Claude Fable 5" excluded from default enablement as a model not covered by
  GitHub's data retention agreement): Claim 1 of this note documents a newer
  named version, "Claude Fable 5.1," reaching general availability in Copilot,
  without stating whether the data-retention exclusion still applies to this
  version — flagged as an open governance question, not resolved as a
  contradiction, since the two sources describe different model version strings
  and this source is silent on data-retention status either way.

- **Extends** `docs-github-copilot-code-review-config-controls.md` (Claim 4,
  content exclusion for Copilot code review at repo/org/enterprise levels):
  Claim 3 of this note documents the same content-exclusion mechanism now also
  gating the standalone Copilot app and Copilot CLI's general agentic
  workflows, a broader scope than code-review-only enforcement.

- **Extends** `docs-github-copilot-cca-apply-review-feedback.md` (Claim 1, "Fix
  with Copilot" dialog for applying review feedback) and
  `docs-github-copilot-cca-fix-failing-actions.md` (Claim 1, one-click fix for
  failing Actions runs): Claim 5 of this note (Agent Merge) bundles both
  capabilities — review-feedback resolution and failing-check fixes — together
  with merge-conflict resolution (novel) into a single named, public-preview
  feature. The source does not confirm whether Agent Merge reuses these two
  prior mechanisms internally or is a new implementation.

- **Extends and contrasts with** `blog-cursor-agent-swarm-model-economics.md`
  (Claim 7, a dedicated third-party reconciler agent for merge-conflict
  resolution between colliding worker agents): Claim 5 of this note is the
  first corpus documentation of GitHub Copilot itself offering automated
  merge-conflict resolution as part of a PR-readiness feature, distinct from
  Cursor's swarm-specific worker-collision use case.

- **Extends and contrasts with** `docs-github-copilot-jetbrains-harness-ga-aug2026.md`
  (Claim 8, JetBrains multi-root *customization discovery*) and
  `docs-github-copilot-vscode-august-2026.md` (Claim 6, the Agent Host sharing
  *one session* across *multiple windows*): Claim 6 of this note (VS Code
  multi-root workspaces bringing a session to *every folder*) is a third,
  distinct multi-root/multi-window topology — configuration lookup vs.
  session-sharing vs. per-folder session placement, respectively.

- **Extends** `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 8, CLI
  Sessions sidebar — flat, concurrent session list) and
  `docs-github-copilot-chat-agent-sessions.md` (Claim 1, Copilot Chat as a
  session search/query surface): Claim 8 of this note (VS Code chat sessions
  hierarchy with attention indicators) is a third, distinct session-management
  paradigm — hierarchical grouping with urgency signaling, on a third surface
  (VS Code chat, as opposed to CLI or web/IDE chat query tools).

- **Contradicts**: None filed as a contradiction issue. The Claude Fable 5.1 /
  "Claude Fable 5" data-retention-exclusion question (see "Extends" above,
  Claim 1) is the one point flagged as materially significant for enterprise
  governance advice, but it does not meet MINER.md §4a's bar for filing: the
  two sources name different model version strings, and this source makes no
  claim about data-retention coverage one way or the other — there is no
  direct assertion in this source that opposes the global-model-policy note's
  claim about "Claude Fable 5" specifically. This is a genuine corpus gap
  (an open question for a future source to resolve), not two sources making
  opposing claims about the same fact.

- **Novel**:
  - First corpus documentation of "Claude Fable 5.1" by name in any GitHub
    Copilot context (Claim 1).
  - First corpus documentation of content exclusions applying to the
    standalone Copilot app and Copilot CLI, beyond the previously-documented
    code-review-only scope (Claim 3).
  - First corpus documentation of "Agent Merge," a named feature unifying
    review-feedback resolution, failing-check fixes, and (novel) automated
    merge-conflict resolution into one PR-readiness agent (Claim 5).
  - First corpus documentation of per-folder agent session placement across a
    multi-root VS Code workspace (Claim 6).
  - First corpus documentation of visual/cosmetic personalization (chat
    backgrounds) for any Copilot chat surface (Claim 7).
  - First corpus documentation of hierarchical (non-flat) chat session
    organization with an attention/urgency indicator (Claim 8).

## Guide Impact

### Chapter 01: Daily Workflows

- **Chat sessions hierarchy with attention indicators**: Document VS Code's new
  hierarchical chat-session organization (Claim 8) as a way for practitioners
  running many concurrent or related sessions to see at a glance which ones
  need a response, contrasted with the CLI's flat Sessions sidebar and Copilot
  Chat's search-based retrieval.

### Chapter 02: Harness Engineering

- **Agent Merge as a unified PR-readiness agent**: Document Agent Merge (Claim
  5, public preview) as the first Copilot feature to combine review-feedback
  application, CI-failure fixing, and merge-conflict resolution into a single
  invocation — note the open question of how it sequences these three
  resolution types when they interact.
- **Multi-root workspace agent sessions**: Add VS Code's experimental
  per-folder session placement in multi-root workspaces (Claim 6) to the
  guide's workspace-management coverage, distinguishing it from JetBrains'
  multi-root *customization* discovery.
- **Content exclusions now cover the Copilot app and CLI**: Update the content
  exclusion documentation (previously scoped to code review per the June 12,
  2026 source) to note it also gates standalone app/CLI agentic workflows as of
  September 4, 2026 (Claim 3).

### Chapter 04: Agentic Workflows — Multi-Session Management

- **Three distinct session-organization paradigms now documented**: Add VS
  Code's hierarchical/attention-indicator model (Claim 8) as a third pattern
  alongside the CLI's flat Sessions sidebar
  (`docs-github-copilot-weekly-releases-aug3-2026.md` Claim 8) and Copilot
  Chat's NL search/retrieval (`docs-github-copilot-chat-agent-sessions.md`
  Claim 1) — practitioners should pick a primary surface based on whether they
  need quick switching (CLI), historical recall (Chat), or relationship-aware
  triage (VS Code).

### Chapter 05: Team Adoption — Enterprise Governance

- **Claude Fable 5.1 default-enablement status is unconfirmed**: Flag for
  enterprise admins that this source does not state whether Claude Fable 5.1
  is subject to the same data-retention-based exclusion from default
  enablement documented for "Claude Fable 5" in
  `docs-github-copilot-global-model-policy-ga.md`. Admins should verify in
  their own Copilot model policy settings rather than assume either outcome
  (Claim 1).
- **Content-exclusion scope expansion**: Organizations that configured content
  exclusions expecting them to gate only Copilot code review should re-verify
  that the same policy now also applies to the standalone Copilot app and CLI
  (Claim 3), which is a meaningfully larger practical scope since those
  surfaces perform general agentic coding work, not just review.

## Extraction Notes

1. **WebFetch discarded in favor of raw HTML, per established corpus
   precedent**: An initial WebFetch pass on the source URL returned a
   plausible-looking but paraphrased and partly-invented rendering — notably
   inventing a "Content Exclusions Feature" subheading not present in the
   actual page (the real page has no such heading; "Copilot app and Copilot
   CLI" is the section heading and the content-exclusion sentence is a plain
   bullet under it) and paraphrasing "The GitHub Copilot harness is now
   generally available" as "GitHub Copilot Harness: Now generally available."
   Per MINER.md §2a and the precedent in
   `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 1 and
   `docs-github-copilot-jetbrains-harness-ga-aug2026.md` Extraction Note 1, the
   page was instead fetched directly via `curl` with a browser user-agent, the
   `<article>` element isolated, block-level tags converted to line breaks, and
   remaining markup stripped programmatically to produce a verbatim transcript.
   Every `Quote` field above was checked by exact substring match against that
   transcript.
2. **No sub-pages followed**: Unlike several prior weekly digests in this
   family, this entry contains no "Read the full [surface] update" links to a
   more detailed sub-changelog. The two outbound links present (general VS
   Code 1.136 release notes at `aka.ms/VSCode/136`; general supported-models
   documentation) are both non-Copilot-specific or general-reference pages
   already judged out of scope by precedent in
   `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 2 and
   `docs-github-copilot-gemini38flash-availability.md` Extraction Note 2,
   respectively. The one link that *would* have led to Copilot-specific
   sub-page detail — the JetBrains harness GA link — points to an already-mined
   source note (`docs-github-copilot-jetbrains-harness-ga-aug2026.md`) rather
   than new material, so it was not re-fetched.
3. **Source is short by design (~130 words)**: All eight bullets in the digest
   are represented as individual claims above; no bullet was thin enough to be
   folded into a general "not independently claimed" bucket the way some prior
   notes in this family handled bare UX-polish bullets, because this digest
   contains no such bundled polish paragraph — every bullet names a distinct,
   nameable feature.
4. **Fable 5 / Fable 5.1 data-retention question not filed as a contradiction**:
   See Cross-References → Contradicts. This is flagged prominently in Claim 1
   and the Guide Impact section as an open question for a future source (a
   dedicated Fable 5.1 availability changelog, in the style of
   `docs-github-copilot-gemini38flash-availability.md`, or an updated
   data-retention exclusion list) to resolve, not adopted into the guide as a
   settled fact in either direction.
5. **Cross-reference verification performed**: All `Claim N` citations above
   were checked against each cited note's actual claim numbering by re-reading
   the note in full before citing; none were guessed, per MINER.md §4b.
