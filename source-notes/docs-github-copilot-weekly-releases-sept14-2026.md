---
source_url: https://github.blog/changelog/2026-09-18-github-copilot-weekly-releases-september-14
source_type: docs
title: "GitHub Copilot weekly releases — September 14"
author: GitHub (official changelog)
date_published: 2026-09-18
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: emerging
issue: "#3559"
---

# GitHub Copilot Weekly Releases — September 14

> GitHub's September 18, 2026 weekly digest covers four sections — GitHub
> Copilot core, GitHub Copilot Business/Enterprise admin features, the
> Copilot app, and VS Code 1.138 — and restates, without new detail, two
> announcements already covered by dedicated source notes: the September 14
> auto-model-selection tiers (issue #3447) and the September 18 code review
> "improved review experience" changelog (issue #3560). The novel material is
> a VS Code Agents-window usage-metrics GA, Copilot-suggested values for
> repository custom properties (public preview), a GA budget-increase-request
> workflow for usage-based billing plans, a new Sentry canvas in the Copilot
> app, and three VS Code 1.138 Agents-window features (local Dev Containers,
> automatic session cleanup, and pull request creation from Agent Host
> sessions). Unlike the September 7 digest, this entry links to no dedicated
> deep-dive blog post for any single feature — only to the Copilot app
> download page and the general (non-Copilot-specific) VS Code 1.138 release
> notes at `aka.ms/VSCode/138`, neither of which was fetched, consistent with
> this family's established scope.

## Source Context

- **Type**: docs (GitHub official product changelog, September 18, 2026;
  self-tagged "Release," "2 minute read"; four sections — "GitHub Copilot,"
  "GitHub Copilot Business and Enterprise users," "GitHub Copilot app," and
  "VS Code 1.138 release updates"). Fetched via `curl` with a browser
  user-agent (rather than relying solely on WebFetch AI summarization),
  following the precedent set in `docs-github-copilot-weekly-releases-aug31-2026.md`
  Extraction Note 1 and reused throughout this note family, which found
  WebFetch prone to inventing headings not present in the source (confirmed
  again here: WebFetch's own summary of this page fabricated a "Main
  Features" / "Business and Enterprise Features" heading structure and
  incorrectly labeled the intro section "GitHub Copilot Core Updates" — none
  of which appear in the actual changelog HTML). No linked deep-dive post
  was fetched this week because none of the outbound links point to a
  dedicated single-feature announcement (see Extraction Notes).
- **Author credibility**: GitHub engineering team (official product
  changelog). Authoritative for: the existence of each named feature, its
  stated availability tier (GA, public preview, or "rolling out"), and which
  plans/surfaces it applies to. Not authoritative for: independent
  verification of any feature's real-world behavior, UI screenshots or exact
  menu paths (none included), or quantitative before/after data (none given
  for any item in this entry, unlike the HydraFusion post mined for the
  September 7 digest).
- **Scope**: A weekly digest covering the period since the prior weekly
  release (week of September 14, 2026). Does NOT cover: Visual Studio,
  Eclipse, Xcode, GitHub Mobile, JetBrains, or Copilot CLI-specific feature
  detail beyond the one cross-surface auto-model-selection-tiers mention.
  Does not link to or describe any Jira-, HydraFusion-, or JetBrains-related
  follow-up to the prior digest.

## Extracted Claims

### Claim 1: Copilot code review now resolves comments it judges addressed in subsequent reviews (leaving outstanding feedback open), suggests commit messages when suggestions are applied, can use shell tools to validate changes, and combines findings from multiple agents for Lite reviews

- **Evidence**: "GitHub Copilot" section, first bullet, changelog.
- **Confidence**: settled (this is a same-topic restatement of a dedicated
  changelog published the same day; see Cross-References)
- **Quote**: "Copilot code review now resolves addressed comments during subsequent reviews, leaving outstanding feedback open. It also suggests commit messages when you apply its code suggestions. Reviews can use shell tools to validate changes, and Lite reviews now combine findings from multiple agents."
- **Our assessment**: This paragraph is a condensed restatement of the
  identical announcements already mined in full depth in
  `docs-github-copilot-code-review-progress-tracking-smart-commits.md`
  (issue #3560, source-dated the same day, September 18, 2026). That note's
  Claims cover the overview-comment restructuring, auto-resolution
  mechanics, resolution-reason tagging, smart-commit-message generation
  (both single-suggestion and batch), broadened shell-tool access for
  review validation, and the ensemble-of-agents architecture for Lite
  reviews — this digest paragraph adds no detail beyond what that dedicated
  note already extracted. No independent guide action follows from this
  claim beyond corroboration.

### Claim 2: Auto model selection now offers efficiency, balance, and intelligence tiers — all drawing from the same available models — rolling out in VS Code, Copilot CLI, and the Copilot app

- **Evidence**: "GitHub Copilot" section, second bullet, changelog.
- **Confidence**: settled (restatement of a dedicated changelog published
  four days earlier; see Cross-References)
- **Quote**: "Choose how Copilot weighs cost, quality, and response time with the new efficiency, balance, and intelligence tiers in auto model selection. All three tiers select from the same available models. This update is rolling out in VS Code, Copilot CLI, and the Copilot app."
- **Our assessment**: This is a verbatim-equivalent restatement of
  `docs-github-copilot-auto-model-selection-tiers.md` (issue #3447,
  September 14, 2026 dedicated changelog), which already extracted the
  three tiers, their per-tier optimization targets, the "same models, only
  routing weighting changes" scoping detail, the three-surface availability
  limit, and the unchanged 10%-discount billing mechanics in full depth. No
  new detail here; the phrase "rolling out" (rather than the dedicated
  note's "currently rolling out") is the only wording variance, not a
  status change.

### Claim 3: VS Code Agents-window usage metrics are now generally available for Enterprise and organization reports, tracking daily active users, session counts, and user message totals separately from editor-window metrics

- **Evidence**: "GitHub Copilot Business and Enterprise users" section,
  first bullet, changelog.
- **Confidence**: settled (GA feature, stated directly by the vendor; no
  quantitative baseline given for what "editor-window metrics" report by
  contrast)
- **Quote**: "Measure adoption and activity in the dedicated VS Code Agents window with new usage metrics that are now generally available. Enterprise and organization reports include daily active users, session counts, and user message totals, alongside user-level activity data. These metrics are separate from the editor-window metrics."
- **Our assessment**: This is the first corpus documentation of usage
  metrics scoped specifically to the VS Code Agents window (the
  session-based, multi-agent UI documented across
  `docs-github-copilot-vscode-july-2026.md`,
  `docs-github-copilot-vscode-august-2026.md`, and this family's prior
  weekly entries) as distinct from prior Copilot usage-metrics sources,
  which report at the org/enterprise/team/repo aggregate level
  (`docs-github-copilot-team-level-usage-metrics.md`,
  `docs-github-copilot-app-usage-metrics-report-rollups.md`,
  `docs-github-copilot-repository-level-usage-metrics.md`) without
  distinguishing Agents-window sessions from editor-window (inline
  completion / chat) activity. The explicit statement that these are
  "separate from the editor-window metrics" is the operationally important
  detail: an admin reading an aggregate Copilot usage report cannot
  currently infer Agents-window adoption from it and must consult this new,
  separate reporting surface. For Ch05 (Team Adoption): document this as a
  new, narrower-scoped metrics surface for teams specifically trying to
  measure agentic-session adoption (as opposed to overall Copilot usage) in
  VS Code.

### Claim 4: Copilot can now suggest allowed values for repository custom property definitions (public preview), with organization/enterprise owners able to toggle the suggestions via a Copilot policy

- **Evidence**: "GitHub Copilot Business and Enterprise users" section,
  second bullet, changelog.
- **Confidence**: emerging (explicitly public preview)
- **Quote**: "Get help choosing values for repository custom properties with Copilot suggestions, now in public preview. For example, when you create an internet-facing property, Copilot can suggest yes and no as allowed values. Organization and enterprise owners can turn suggestions on or off through a Copilot policy."
- **Our assessment**: This is distinct from `docs-github-copilot-cca-custom-properties.md`
  (issue #172), which documents using custom properties as a gate to
  selectively *enable Copilot cloud agent* per-repository — a
  configuration-as-access-control pattern. This claim is the reverse
  direction: Copilot *assisting with defining* the custom property values
  themselves (e.g., suggesting "yes"/"no" for a boolean-shaped property),
  a documentation/authoring aid rather than an access-control mechanism.
  The two features share the "custom properties" GitHub primitive but serve
  unrelated purposes and should not be conflated in the guide. The
  policy-gated on/off toggle is consistent with GitHub's general pattern
  (seen elsewhere in the corpus) of giving org/enterprise owners a Copilot
  policy lever for any new suggestion-generating feature.

### Claim 5: Organizations and enterprises on usage-based billing can now request a higher Copilot budget when they hit their AI credit limit, with owners/billing managers able to approve, adjust, or deny the request in settings — GA for Copilot Business and Enterprise, excluding enterprises with managed users

- **Evidence**: "GitHub Copilot Business and Enterprise users" section,
  third bullet, changelog.
- **Confidence**: settled (GA feature, stated directly by the vendor,
  including an explicit exclusion)
- **Quote**: "Request a higher Copilot budget from your organization or enterprise when you reach your AI credit limit. Owners and billing managers can approve, adjust, or deny requests in settings. Approval restores access to AI credits. This is now generally available for Copilot Business and Copilot Enterprise plans with usage-based billing. This feature is not available for enterprises with managed users."
- **Our assessment**: This is a new self-service escalation workflow for
  the AI-credit-limit friction point that the guide should treat as
  operationally significant: previously, hitting a credit limit under
  usage-based billing presumably required an out-of-band admin request
  (not itself documented in this corpus); this formalizes an in-product
  request/approve/deny loop. The "not available for enterprises with
  managed users" exclusion is a real scope limit worth flagging — teams
  under the managed-users model (which the corpus elsewhere associates with
  stricter admin-controlled environments, e.g.
  `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`) do not get
  this self-service path and must rely on whatever the managed-user
  provisioning process already prescribes. No prior corpus source documents
  an in-product budget-increase-request workflow; this is novel.

### Claim 6: The Copilot app now includes a Sentry canvas that lets developers move from a Sentry crash report to a code fix by reviewing errors and stack traces, then working with Copilot to investigate, validate a fix, and prepare a pull request

- **Evidence**: "GitHub Copilot app" section, sole bullet, changelog.
- **Confidence**: emerging (no explicit GA/preview tier stated in the
  digest text itself, unlike most other items in this digest)
- **Quote**: "Fix production crashes from Sentry reports. Move from crash report to code fix with the new Sentry canvas in the GitHub Copilot app. Review errors, stack traces, and related context, then work with Copilot to investigate the cause, validate a fix, and prepare a pull request."
- **Our assessment**: This is the first corpus documentation of a
  third-party error-monitoring (Sentry) integration inside the standalone
  Copilot app, joining the September 7 digest's Jira "canvas" integration
  (documented in `docs-github-copilot-weekly-releases-sept7-2026.md` Claim
  1) as a second instance of the Copilot app's "shared canvas" pattern being
  extended to a specific third-party tool. As with the Jira integration, the
  digest gives no mechanism detail (how Sentry projects connect to the
  canvas, whether it requires a Sentry-side app install or API token, or
  which Copilot plans include it) and states no availability tier. The
  workflow described — investigate root cause, validate fix, prepare PR —
  matches the guide's general "human triages, agent investigates and
  drafts, human reviews PR" pattern already documented for other
  triage-to-PR flows in this corpus. For Ch05 (Team Adoption): flag as
  relevant for organizations using Sentry for production error monitoring,
  but treat plan-tier and configuration requirements as unconfirmed pending
  a dedicated changelog entry, consistent with how this note family treated
  the undocumented Jira integration status in the prior digest.

### Claim 7: VS Code's Agents window can now run agents inside the project's own local Dev Container (tools and dependencies included), rolling out gradually and requiring both Docker and a supported Dev Container configuration

- **Evidence**: "VS Code 1.138 release updates" section, first bullet,
  changelog.
- **Confidence**: emerging (explicitly a gradual rollout, not stated as
  full GA or preview using this family's usual tier vocabulary)
- **Quote**: "Run agents with your project's tools and dependencies using local Dev Containers in the Agents window. Support is rolling out gradually and requires both Docker and a supported Dev Container configuration."
- **Our assessment**: This is a distinct, more specific capability from the
  passing Dev Containers mention in `docs-github-copilot-vscode-june-2026.md`
  Claim 6, which documents the integrated *browser* proxying HTTP(S)
  traffic through a remote workspace connection (SSH remotes, Dev
  Containers, or Codespaces used only as examples of "remote workspace"
  types) — that claim is about browser network routing, not about running
  the agent itself inside a container. This claim is the first corpus
  documentation of the Agents window executing an agent session *inside*
  a project-defined Dev Container, giving the agent the exact toolchain and
  dependency versions the container specifies rather than whatever is on
  the host machine. The two explicit prerequisites (Docker installed,
  supported Dev Container configuration present in the repo) mean this is
  not available by default even once rolled out — repos without an existing
  `.devcontainer` config get no benefit. For Ch02 (Harness Engineering —
  Environment Parity): document as a mechanism for eliminating
  host-vs-agent toolchain drift, conditional on the repo already having
  Dev Container support and the practitioner's machine having Docker.

### Claim 8: VS Code 1.138 adds opt-in, preview automatic session cleanup — marking inactive Agents-window sessions Done once all their pull requests merge, with optional deletion after a separate grace period

- **Evidence**: "VS Code 1.138 release updates" section, second bullet,
  changelog.
- **Confidence**: emerging (explicitly opt-in and in preview)
- **Quote**: "Automatically mark inactive sessions as Done once all their pull requests merge, with optional deletion after a separate grace period. Automatic cleanup is opt-in and now in preview."
- **Our assessment**: This addresses session-list hygiene for practitioners
  running many parallel Agents-window sessions — a workflow this corpus has
  documented growing more common (worktree-isolated parallel sessions,
  multi-chat sessions; see `docs-github-copilot-vscode-july-2026.md` Claim
  1, `docs-github-copilot-vscode-august-2026.md` Claim 1). Two independent
  timers are implied: one for marking a session "Done" (triggered by all
  its PRs merging) and a separate, optional grace period before deletion —
  the digest does not state either timer's default or configurable length.
  Being opt-in and preview means teams should not assume old sessions
  vanish automatically without deliberately enabling this. For Ch02
  (Harness Engineering — Session Management): note as a forthcoming
  mitigation for Agents-window session-list clutter in high-parallelism
  workflows, with the caveat that the cleanup timers' exact durations are
  not yet documented.

### Claim 9: VS Code 1.138 lets practitioners create a pull request directly from an Agent Host session without leaving the Agents window — reviewing the generated title and description, choosing draft status, and creating it directly or delegating creation to the agent

- **Evidence**: "VS Code 1.138 release updates" section, third bullet,
  changelog.
- **Confidence**: settled (product fact stated directly in the official
  changelog, naming "Agent Host sessions" as the mechanism)
- **Quote**: "Create pull requests from Agent Host sessions without leaving the Agents window. Review the generated title and description, choose draft status, and create the pull request directly or ask your agent to do it."
- **Our assessment**: This extends the Agent Host concept first named as a
  concrete product feature in `docs-github-copilot-vscode-august-2026.md`
  Claim 6 (connecting multiple VS Code windows to one running agent
  session) with a new capability built on the same underlying session type:
  PR creation without a context switch to a terminal, GitHub.com, or a
  separate PR-creation dialog. The "review generated title/description,
  choose draft status" detail implies Copilot drafts PR metadata from the
  session's own changes, with an explicit human-approval step before
  creation (or the option to delegate that step back to the agent) —
  consistent with the guide's general verify-before-execute framing. For
  Ch01 (Daily Workflows): document as a workflow-friction reduction for the
  common "agent session produces changes → open a PR" step, now completable
  without leaving the Agents window.

## Concrete Artifacts

### Full weekly digest — September 14, 2026 (published September 18, 2026), verbatim transcript

Extracted from raw HTML via `curl` with a browser user-agent (not WebFetch
summarization alone), per MINER.md §2a and this family's established
precedent.

```
GitHub Copilot weekly releases — September 14
Source: github.blog/changelog, published 2026-09-18, retrieved 2026-09-19
Release, 2 minute read

INTRO
  This week, GitHub Copilot adds new model selection options, code review
  updates, and Sentry integration in the Copilot app. There are also
  updates for admins, plus new agent features in VS Code.

GITHUB COPILOT
  [Claim 1]
  Copilot code review now resolves addressed comments during subsequent
  reviews, leaving outstanding feedback open. It also suggests commit
  messages when you apply its code suggestions. Reviews can use shell
  tools to validate changes, and Lite reviews now combine findings from
  multiple agents.

  [Claim 2]
  Choose how Copilot weighs cost, quality, and response time with the new
  efficiency, balance, and intelligence tiers in auto model selection. All
  three tiers select from the same available models. This update is
  rolling out in VS Code, Copilot CLI, and the Copilot app.

GITHUB COPILOT BUSINESS AND ENTERPRISE USERS
  [Claim 3]
  Measure adoption and activity in the dedicated VS Code Agents window
  with new usage metrics that are now generally available. Enterprise and
  organization reports include daily active users, session counts, and
  user message totals, alongside user-level activity data. These metrics
  are separate from the editor-window metrics.

  [Claim 4]
  Get help choosing values for repository custom properties with Copilot
  suggestions, now in public preview. For example, when you create an
  internet-facing property, Copilot can suggest yes and no as allowed
  values. Organization and enterprise owners can turn suggestions on or
  off through a Copilot policy.

  [Claim 5]
  Request a higher Copilot budget from your organization or enterprise
  when you reach your AI credit limit. Owners and billing managers can
  approve, adjust, or deny requests in settings. Approval restores access
  to AI credits. This is now generally available for Copilot Business and
  Copilot Enterprise plans with usage-based billing. This feature is not
  available for enterprises with managed users.

GITHUB COPILOT APP
  [Claim 6]
  Fix production crashes from Sentry reports. Move from crash report to
  code fix with the new Sentry canvas in the GitHub Copilot app. Review
  errors, stack traces, and related context, then work with Copilot to
  investigate the cause, validate a fix, and prepare a pull request.
  (Link: "Download the Copilot app" — github.com/features/ai/github-app)

VS CODE 1.138 RELEASE UPDATES
  [Claim 7]
  Run agents with your project's tools and dependencies using local Dev
  Containers in the Agents window. Support is rolling out gradually and
  requires both Docker and a supported Dev Container configuration.

  [Claim 8]
  Automatically mark inactive sessions as Done once all their pull
  requests merge, with optional deletion after a separate grace period.
  Automatic cleanup is opt-in and now in preview.

  [Claim 9]
  Create pull requests from Agent Host sessions without leaving the
  Agents window. Review the generated title and description, choose
  draft status, and create the pull request directly or ask your agent to
  do it.
  (Link: "full release notes" — aka.ms/VSCode/138, not fetched, general
   non-Copilot-specific release notes)
```

*Source: raw HTML of
https://github.blog/changelog/2026-09-18-github-copilot-weekly-releases-september-14,
fetched directly via `curl` with a browser user-agent on 2026-09-19,
block-level tags converted to line breaks, remaining markup stripped. All
`Quote` fields above were checked by exact substring match against this
transcript, including confirming the curly apostrophe in "project's tools
and dependencies," normalized to a straight ASCII apostrophe per this
family's established convention (see Extraction Notes).*

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-code-review-progress-tracking-smart-commits.md`,
`docs-github-copilot-auto-model-selection-tiers.md`,
`docs-github-copilot-cca-custom-properties.md`,
`docs-github-copilot-vscode-june-2026.md`,
`docs-github-copilot-vscode-august-2026.md`,
`docs-github-copilot-vscode-july-2026.md`, and
`docs-github-copilot-weekly-releases-sept7-2026.md` were re-read directly in
those notes (via `### Claim N:` headings, counted top-to-bottom in document
order) before citing, per MINER.md §4b.

- **Corroborates** `docs-github-copilot-code-review-progress-tracking-smart-commits.md`
  (issue #3560, same-day September 18, 2026 dedicated changelog): Claim 1 of
  this note restates that entry's overview-comment restructuring,
  auto-resolution, smart-commit-message, shell-tool-validation, and
  Lite-review-ensemble announcements in condensed form, with no new detail.

- **Corroborates** `docs-github-copilot-auto-model-selection-tiers.md`
  (issue #3447, Claim 1, four days earlier on September 14, 2026): Claim 2
  of this note restates the efficiency/balance/intelligence tier
  announcement, with no new detail beyond what that dedicated note already
  extracted (per-tier targets, same-model-pool scoping, three-surface
  availability limit, unchanged 10% discount).

- **Distinct from** `docs-github-copilot-cca-custom-properties.md` (issue
  #172, using custom properties to selectively enable Copilot cloud agent
  per-repository): Claim 4 of this note (Copilot suggesting *values* for
  custom property definitions) is a documentation-authoring aid, not an
  access-control mechanism — both features use the same GitHub "custom
  properties" primitive but for unrelated purposes.

- **Extends** `docs-github-copilot-vscode-august-2026.md` (Claim 6, the
  Agent Host connecting multiple VS Code windows to one running agent
  session): Claim 9 of this note documents a new capability on the same
  Agent Host session type — creating a pull request without leaving the
  Agents window.

- **Distinct from** `docs-github-copilot-vscode-june-2026.md` (Claim 6, the
  integrated browser proxying traffic through a remote workspace connection,
  which mentions Dev Containers only as one example remote-workspace type):
  Claim 7 of this note is a different capability — running the agent's own
  execution environment inside a project's Dev Container — not browser
  network routing.

- **Extends** `docs-github-copilot-team-level-usage-metrics.md` and
  `docs-github-copilot-app-usage-metrics-report-rollups.md` (org/team/repo
  aggregate Copilot usage reporting via API): Claim 3 of this note adds a
  narrower-scoped, VS Code Agents-window-specific usage metrics surface,
  explicitly stated as separate from editor-window metrics — the corpus's
  first documentation of Agents-window-scoped adoption measurement as
  distinct from overall Copilot usage.

- **Extends** `docs-github-copilot-weekly-releases-sept7-2026.md` (Claim 1,
  the Jira "shared canvas" integration in the Copilot app): Claim 6 of this
  note documents a second third-party-tool canvas integration (Sentry) in
  the same app, following the same "canvas" naming and
  investigate-fix-validate-PR workflow shape, with the same lack of stated
  availability tier or configuration detail as the Jira integration.

- **Contradicts**: None identified. This digest is additive relative to the
  existing corpus; no claim here revises a prior source note's claim.

- **Novel**:
  - First corpus documentation of VS Code Agents-window-specific usage
    metrics (DAU, session counts, message totals), separate from
    editor-window and org-aggregate Copilot usage metrics (Claim 3).
  - First corpus documentation of Copilot suggesting values for repository
    custom property definitions (Claim 4).
  - First corpus documentation of an in-product Copilot budget-increase-
    request/approval workflow for usage-based billing plans, with an
    explicit managed-users exclusion (Claim 5).
  - First corpus documentation of a Sentry integration ("canvas") in the
    standalone Copilot app (Claim 6).
  - First corpus documentation of the VS Code Agents window running agents
    inside a project's own local Dev Container (Claim 7).
  - First corpus documentation of opt-in automatic Agents-window session
    cleanup tied to pull request merge state (Claim 8).
  - First corpus documentation of creating a pull request directly from an
    Agent Host session without leaving the Agents window (Claim 9).

## Guide Impact

### Chapter 05: Team Adoption

- **New Agents-window-specific usage metrics**: Document Claim 3 as a
  narrower reporting surface than existing org/team/repo aggregate Copilot
  usage metrics — teams specifically trying to measure agentic-session
  (not just overall Copilot) adoption in VS Code should look at this new
  GA metrics surface rather than assuming aggregate usage reports cover it.
- **Budget-increase self-service workflow**: Document Claim 5's
  request/approve/deny loop as the first in-product path for AI-credit-limit
  escalation under usage-based billing, with the caveat that it is
  unavailable for enterprises with managed users, who should be told to use
  whatever their existing managed-user provisioning process prescribes.
- **Sentry canvas as a second third-party-tool integration pattern**: Add
  Claim 6 alongside the September 7 digest's Jira integration as a second
  instance of the Copilot app's canvas-based, investigate-fix-validate-PR
  pattern for third-party tool data — flag both as unconfirmed for
  plan-tier/configuration requirements pending dedicated changelogs.
- **Custom properties as a documentation aid, not access control**: When
  citing `docs-github-copilot-cca-custom-properties.md` for the
  access-control use of custom properties, note Claim 4's distinct
  value-suggestion feature to avoid conflating the two custom-properties
  capabilities.

### Chapter 02: Harness Engineering

- **Local Dev Containers for Agents-window execution**: Document Claim 7 as
  a mechanism for eliminating host-vs-agent toolchain drift, conditional on
  the repository already having a supported Dev Container configuration and
  the practitioner's machine having Docker installed — neither is automatic
  even once the gradual rollout reaches a given user.
- **Opt-in automatic session cleanup**: Document Claim 8 as a forthcoming
  mitigation for Agents-window session-list clutter under high-parallelism
  workflows (worktree-isolated and multi-chat sessions already documented
  elsewhere in this corpus), noting it must be explicitly enabled and that
  neither cleanup timer's default duration is documented yet.

### Chapter 01: Daily Workflows

- **PR creation without leaving the Agents window**: Document Claim 9 as a
  workflow-friction reduction for the "agent session produces changes → PR"
  step, with an explicit human review point (title/description, draft
  status) before creation, or the option to delegate that step to the
  agent.

## Extraction Notes

1. **No dedicated deep-dive post to follow this week**: Unlike
   `docs-github-copilot-weekly-releases-sept7-2026.md` (which followed the
   linked HydraFusion announcement post per MINER.md §1), this digest's only
   outbound links are to the Copilot app download page (not a feature
   description) and the general, non-Copilot-specific VS Code 1.138 release
   notes at `aka.ms/VSCode/138` — the latter deliberately not fetched,
   consistent with this family's established treatment of general VS Code
   release notes as out of scope (e.g.
   `docs-github-copilot-weekly-releases-aug31-2026.md` Extraction Note 2).
2. **Raw HTML fetched via `curl`, not WebFetch summarization**: Fetched
   directly with a browser user-agent and parsed by stripping markup from
   the `<article>` content region, per the precedent in
   `docs-github-copilot-weekly-releases-aug31-2026.md` Extraction Note 1.
   An initial WebFetch call on the same URL (made before the `curl` fetch,
   to triage the source) fabricated section headings ("Main Features,"
   "Business and Enterprise Features," "GitHub Copilot Core Updates,"
   "Copilot App Integration") not present anywhere in the actual page, and
   regrouped bullets under those invented headings differently from the
   page's real four sections ("GitHub Copilot," "GitHub Copilot Business
   and Enterprise users," "GitHub Copilot app," "VS Code 1.138 release
   updates") — this discrepancy is noted as further confirmation of the
   established WebFetch-unreliability finding for this source family, not
   used as a basis for any claim above. The per-item tier language in the
   WebFetch summary happened to match the raw HTML in this instance; the
   heading fabrication is the reproducible failure mode.
3. **Restated items (Claims 1-2) still extracted as full claims**: Following
   the precedent set by `docs-github-copilot-weekly-releases-sept7-2026.md`
   Claim 12 (the JetBrains sandbox restatement), the code-review and
   auto-model-tier paragraphs are extracted as claims with explicit
   restatement framing rather than omitted, so a reader of this note alone
   sees the full digest content and is pointed to the dedicated notes for
   depth.
4. **No availability tier stated for the Sentry canvas (Claim 6)**: As with
   the September 7 digest's Jira integration, this is reported as a genuine
   gap in the source rather than inferred — most other items in this digest
   explicitly state "public preview," "GA," "rolling out," or "opt-in...
   preview," but the Sentry canvas bullet states none of these.
5. **Cross-reference verification performed**: All `Claim N` citations above
   were checked against each cited note's actual claim numbering by
   re-reading the note in full before citing, per MINER.md §4b.
6. **Apostrophe normalization**: The source HTML uses a typographic curly
   apostrophe in "your project's tools and dependencies." Consistent with
   existing notes in this corpus, the quote above is normalized to a
   straight ASCII apostrophe — a typographic substitution only, no wording,
   word order, or punctuation altered.
