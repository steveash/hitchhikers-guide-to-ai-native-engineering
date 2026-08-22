---
source_url: https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack
source_type: docs
title: "The new GitHub Copilot experience in Slack"
author: GitHub (official changelog)
date_published: 2026-08-21
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: emerging
issue: "#2858"
---

# The New GitHub Copilot Experience in Slack

> GitHub's August 2026 changelog announces a public-preview Slack integration —
> published the same day as, and structurally near-identical to, its Microsoft
> Teams counterpart — that lets any conversation participant steer a Copilot
> cloud agent session via `@GitHub` mentions, spins up a dedicated **Slack
> Code** channel per task, captures the entire thread as agent context,
> attributes shared-context artifacts to the app identity rather than a person,
> and gates Teams/Slack-originated PRs behind an automatic extra ruleset
> approval — the same chat-native entry point onto GitHub's Copilot cloud
> agent / cloud sandbox substrate, with one Slack-specific addition (Slack
> Code) not present in the Teams integration.

## Source Context

- **Type**: docs (GitHub official changelog, `github.blog/changelog`, published
  August 21, 2026; a roughly 2-minute-read feature announcement). One linked
  GitHub Docs how-to page was followed in full per MINER.md §1 — "Integrating
  Copilot Cloud Agent with Slack" — since the changelog itself gives only a
  compressed summary of the security, identity, and configuration mechanics
  that the how-to doc documents in much greater detail. Both pages were
  fetched with WebFetch using multiple independently-worded prompts (a full
  reading-order reproduction pass, followed by targeted verbatim-quote
  checks for specific sentences); every `Quote` field below matches
  identically across at least two independent fetches, except where noted.
- **Author credibility**: First-party GitHub product changelog and official
  docs. Authoritative for feature existence, configuration steps, and the
  identity/permission/security model as designed. Not a source for adoption
  data, comparative UX quality against Teams or other Copilot surfaces, or
  how often teams actually use `@GitHub` in Slack versus other Copilot
  surfaces — no customer quotes, usage metrics, or case studies appear in
  either page.
- **Scope**: Covers the Slack-specific entry point for GitHub Copilot cloud
  agent (starting sessions via `@GitHub` mention, the dedicated "Slack Code"
  channel mechanic, thread-as-context capture, identity/permission model for
  DM vs. shared-context sessions, compliance approval gating, issue-creation
  workflow, default-repository configuration, availability/prerequisites).
  Does **not** cover: the Slack app's installation permission scopes in
  API/manifest terms, a rollout timeline to GA, independent security review
  of the integration, cloud-sandbox architecture or billing internals (that
  material lives in the sibling Teams source's Claims 9–11, sourced from a
  different linked concept page not re-fetched here since this changelog
  does not link to it), or a direct feature-parity comparison against
  Vercel's Chat SDK Slack adapter beyond what can be inferred by comparing
  the two sources' stated behavior.

## Extracted Claims

### Claim 1: The Slack integration brings both Copilot CLI's and the Copilot app's agentic capabilities into Slack as a public preview, via `@GitHub` mentions in DMs, channels, or threads

- **Evidence**: The changelog's lead sentence, corroborated by the how-to
  doc's introduction describing the same integration.
- **Confidence**: settled (first-party description of a shipping
  public-preview mechanism, consistent across both pages)
- **Quote**: "The GitHub integration in Slack now brings the agentic capabilities of GitHub Copilot CLI and the GitHub Copilot app into Slack in public preview."
- **Our assessment**: This frames the Slack integration as a repackaging of
  two existing Copilot surfaces (CLI and app) rather than a new agent
  implementation — consistent with the pattern already documented for Teams
  in `docs-github-copilot-teams-shared-agentic-work.md` Claim 2, where
  Teams-originated work is explicitly one entry point onto the same
  underlying cloud agent execution substrate. Both chat integrations appear
  to be thin, chat-native front ends onto one shared backend rather than
  independent agent stacks.

### Claim 2: GitHub is a launch partner for "Slack Code," described in the changelog as a new type of channel designed for agents

- **Evidence**: A standalone sentence in the changelog's opening paragraph,
  distinct from the `@GitHub`-mention feature description that precedes it.
- **Confidence**: settled (first-party statement naming a specific Slack
  platform feature and GitHub's launch-partner role in it)
- **Quote**: "GitHub is also a launch partner for Slack Code, a new type of channel designed for agents."
- **Our assessment**: This is the most structurally novel claim in the
  source relative to the corpus: it positions "Slack Code" as a
  **Slack-platform-level** feature (a new channel type, with other launch
  partners implied beyond GitHub) rather than something GitHub built
  unilaterally, the way Vercel's Chat SDK Slack adapter
  (`blog-vercel-chat-sdk-slack-agent-support.md`) wraps Slack's existing
  "agent messaging experience" APIs. No other source in the corpus documents
  Slack itself shipping a dedicated agent-native channel primitive. This
  changelog does not name any other launch partner or describe "Slack Code"
  as a platform capability independent of GitHub's use of it — that would
  need to be corroborated by a Slack-authored source, which is not currently
  in the corpus.

### Claim 3: Mentioning `@GitHub` in a DM, channel, or thread starts an agent session that can answer questions, triage and create/label issues, investigate failures and implement changes validated in a secure cloud sandbox, and open a pull request linked back to the conversation

- **Evidence**: The changelog's "What you can now do with @GitHub" bulleted
  list.
- **Confidence**: settled (first-party enumeration of shipping capabilities)
- **Quote**: "Answer questions about your code and GitHub activity." / "Triage bug reports, update existing issues, or create and label new issues." / "Investigate failures, implement changes, and validate its work in a secure cloud sandbox." / "Open a pull request and provide a link to the conversation for review."
- **Our assessment**: This four-item capability list is close in substance
  (though not identical wording) to Claim 1's changelog framing for Teams in
  `docs-github-copilot-teams-shared-agentic-work.md` ("Turn a Microsoft
  Teams discussion into a collaborative agent session everyone can see and
  help direct"), and to the how-to doc's own opening line for Slack (see
  Claim 5 below) — GitHub is describing the same underlying capability set
  across both chat surfaces, phrased slightly differently per platform.

### Claim 4: Copilot continues working asynchronously in Slack while the user is away (in a meeting, commuting, or otherwise occupied), and the session can be steered from Slack and later continued from the terminal, the GitHub Copilot app, or an IDE

- **Evidence**: The changelog's async-continuation sentence, corroborated by
  the how-to doc's "Secure Cloud Sandboxes" section describing the same
  cross-surface continuation.
- **Confidence**: settled (first-party description of a named, cross-surface
  continuation mechanism)
- **Quote**: "GitHub Copilot continues working asynchronously while you're in a meeting, commuting, or focused on something else." (changelog) / "When Copilot cloud agent starts work on a task from Slack, Copilot continues working asynchronously in a secure cloud sandbox, and posts the result when it's ready. You can keep steering from Slack or continue the work on the agent-generated artifacts in GitHub, the terminal, or your preferred code editor." (how-to doc)
- **Our assessment**: This is the identical device-independent session model
  already documented for Teams (`docs-github-copilot-teams-shared-agentic-work.md`
  Claim 2 and Claim 10) and for CLI remote control
  (`docs-github-copilot-cli-remote-control-ga.md`) — a session's state lives
  in GitHub-hosted infrastructure, not on whichever client started it, so
  "started in Slack, continued in an IDE" is a consequence of the shared
  cloud-agent session substrate rather than a Slack-specific bridging
  feature. This corroborates the corpus's growing picture of one session
  model surfaced through CLI, VS Code, JetBrains, issues/projects, Teams,
  and now Slack.

### Claim 5: Copilot cloud agent creates a dedicated "Slack Code" channel per task, which the user (and optionally teammates) uses to collaborate with Copilot, and which must be used exclusively once established; the channel can later be archived and reopened

- **Evidence**: The how-to doc's "Slack Code" subsection, corroborated by
  the changelog's shorter "Slack Code and GitHub Copilot" section describing
  the same mechanic.
- **Confidence**: settled (first-party description of a specific, named UI
  mechanism with an explicit one-channel-per-task rule and a documented
  archive/reopen lifecycle)
- **Quote**: "When you ask Copilot to perform a task, Copilot cloud agent will create a dedicated code channel, called Slack Code. This is where you, and optionally your teammates, can collaborate with Copilot on a task. Once a code channel is established, steer the session exclusively through that channel." / "Copilot manages the code channel and displays details about the session, such as the working repository, branch, issue or pull request link, status, and model in use. Code channels are intended for one session at a time: one channel per task. When the session is finished, you are asked whether you want to archive the channel. After archiving, the channel and its history remain viewable and searchable, and you can reopen the channel if needed." (how-to doc) / "GitHub Copilot can also create a dedicated code channel that keeps the task focused without adding noise to the original conversation." (changelog)
- **Our assessment**: This is the single feature in this source with no
  documented counterpart in the Teams integration
  (`docs-github-copilot-teams-shared-agentic-work.md` describes no
  equivalent per-task dedicated-channel mechanic — Teams sessions appear to
  stay in the originating thread). The "steer the session exclusively
  through that channel" instruction, combined with "one channel per task"
  and an explicit archive/reopen lifecycle, makes Slack Code a more
  structured, longer-lived collaboration surface than a thread-scoped
  conversation — closer in spirit to a per-task workspace than a chat
  reply. Whether this difference reflects a genuine platform capability gap
  (Teams lacking an equivalent channel-spawning primitive) or simply a
  choice GitHub made for the Slack integration specifically is not
  something either page states.

### Claim 6: Agent sessions in Slack are shared by design, so a team collaborates on the work where the request began rather than one person working privately with an agent — anyone can join the code channel from the originating thread to inspect diffs, review output previews, add context, redirect the approach, or stop the session

- **Evidence**: The changelog's "The power of multiplayer" section.
- **Confidence**: settled (first-party framing of the integration's
  collaboration model as a deliberate design choice, not an incidental
  side effect)
- **Quote**: "Agent sessions in Slack are shared, so your team can collaborate on the work where the request began instead of one person working privately with an agent." / "Inside the code channel, your team can follow the plan, inspect the diffs, review output previews like HTML artifacts, and iterate with Copilot."
- **Our assessment**: This "multiplayer by default" framing is thematically
  close to Shopify River's Lehrwerkstatt design philosophy documented in
  `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` (Claims 1–4): both
  describe agent work deliberately kept visible and joinable in a shared
  chat surface rather than defaulting to a private 1:1 session. The
  mechanisms differ materially, though — River's design is coercive (it
  *refuses* DMs entirely to force visibility, per that note's Claim 1),
  while GitHub's Slack integration supports both DM sessions (personal
  identity, private) and shared-context sessions (app identity, joinable
  code channel) as parallel options, leaving the choice of visibility to the
  user rather than enforcing it architecturally. This is a conditioning
  variable, not a contradiction: the two sources describe different design
  points on the same visibility-vs-privacy spectrum for chat-native coding
  agents, worth naming explicitly if the guide contrasts "opt-in
  multiplayer" (GitHub Slack/Teams) against "mandatory multiplayer" (River)
  as two adoption strategies.

### Claim 7: Before an `@GitHub` mention in Slack, Copilot cloud agent will capture the entire thread as context for the request, and that captured context is stored in the artifacts the agent generates — a user who wants to limit context should send a direct message instead

- **Evidence**: A dedicated "Security Considerations" callout in the how-to
  doc, placed as its own section immediately after the introduction and
  before the identity/permissions section — verified verbatim across two
  independent WebFetch passes.
- **Confidence**: settled (first-party, explicitly labeled as a security
  consideration rather than a passing feature description)
- **Quote**: "Before you @mention GitHub in Slack, consider that Copilot cloud agent will capture the entire thread as context for your request, understanding and implementing solutions based on the discussion. This context is stored in the artifacts the agent generates. If you want to limit the context, you can send a direct message to the GitHub app for Slack instead."
- **Our assessment**: This is word-for-word identical in structure and
  near-identical in wording to the Teams how-to doc's own "Security
  considerations" callout, documented in
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 3 (which quotes:
  "Before you @mention GitHub in Teams, consider that Copilot cloud agent
  will capture the entire thread as context for your request..." — the only
  textual difference is "Teams"/"the GitHub app for Teams" swapped for
  "Slack"/"the GitHub app for Slack"). This is strong evidence GitHub
  authored both integrations' documentation from a shared template, and
  that the same operational risk applies identically to both: any
  `@GitHub`-in-a-channel session is an implicit broad data-capture event,
  and the only documented mitigation (switching to a DM) is an environment
  choice, not a scoping control, in both integrations.

### Claim 8: The identity Copilot uses for created artifacts depends on conversation type — in a direct message it acts using the requester's personal GitHub permissions; in a shared context (group thread or channel) it creates artifacts such as pull requests under its app identity rather than the individual's personal account

- **Evidence**: The how-to doc's "Understanding Collaborative Sessions,
  Permissions, Code Channels and Sandboxes" section, stating the
  distinction directly as a two-item list.
- **Confidence**: settled (first-party statement of the platform's
  identity-attribution model, stated as a clear binary rule keyed on
  conversation type)
- **Quote**: "The identity Copilot uses depends on whether you interact with it in a direct message or a shared context." / "When you use Copilot in a direct message, it can take actions for you, such as creating pull requests or issues, as well as answer questions. It uses the permissions of your linked GitHub personal account to take these actions." / "When you use Copilot in a shared context, such as a group thread or channel, Copilot creates artifacts, such as pull requests, under its app identity rather than your personal account."
- **Our assessment**: This is the identical conversation-type-conditional
  identity model already documented for Teams in
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 4, confirming
  that GitHub's identity-attribution rule for Copilot cloud agent is a
  platform-agnostic policy applied consistently across both chat
  integrations, not a Teams-specific or Slack-specific design choice.

### Claim 9: Because shared-context pull requests are attributed to the app identity rather than a person, repository rulesets automatically require one additional approval beyond whatever a repo already requires, enabled by default, as long as the repository already requires at least one approval

- **Evidence**: The how-to doc's paragraph immediately following the
  identity/permissions explanation.
- **Confidence**: settled (first-party statement of a specific, automatic
  ruleset behavior)
- **Quote**: "Pull requests created in a shared context by Copilot use the app's identity. If you use repository rulesets, because these pull requests aren't attributed to a person, one more approval is required before merging, as long as the repository already requires at least one approval. This is enabled by default."
- **Our assessment**: This sentence is verbatim-identical to the
  corresponding sentence in the Teams how-to doc, quoted in
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 5 — further
  confirmation that this ruleset-approval-escalation mechanism is a single,
  shared compliance control applied uniformly to any chat-integration
  session that produces an app-identity-attributed PR, not something
  configured per chat platform. Note also that the changelog itself frames
  this as something "[r]epository administrators can require," a subtly
  different framing (opt-in admin control) from the how-to doc's "enabled
  by default" — the same tension already identified and evaluated (and not
  filed as a contradiction) for the Teams source's Claim 5; the same
  reasoning applies here without needing separate re-evaluation.

### Claim 10: Only users with write access to a repository can trigger Copilot to make changes, but any conversation participant can provide input; guest members of a workspace and outside collaborators to repositories cannot start or steer a session with Copilot in Slack at all

- **Evidence**: A direct exclusion statement in the how-to doc's permissions
  section.
- **Confidence**: settled (first-party statement of an access exclusion)
- **Quote**: "Only users with write access to a repository can trigger Copilot to make changes, but any conversation participant can provide input. Guest members of a workspace, and outside collaborators to repositories are not able to start or steer a session with Copilot in Slack."
- **Our assessment**: Again verbatim-identical in structure to the Teams
  how-to doc's exclusion statement (`docs-github-copilot-teams-shared-agentic-work.md`
  Claim 6, substituting "Teams" for "Slack"). The changelog itself does not
  mention this exclusion for Slack either, exactly as the Teams changelog
  omitted it — the Assayer/Smith should treat both changelog entries as
  incomplete permission specifications and rely on the respective how-to
  docs as the authoritative source for this exclusion.

### Claim 11: A Slack channel can have a default repository (set via `@GitHub settings`), which provides the context Copilot uses when responding and is where Copilot-created issues/PRs are opened unless a repository is specified in the prompt; if a channel has no default repository, Copilot sets whatever repository is used in the channel's first session as its default; direct messages cannot have a default repository at all

- **Evidence**: The how-to doc's "Connecting the GitHub App to Your GitHub
  Account" and "Setting a Default Repository for a Channel" sections.
- **Confidence**: settled (first-party description of a configuration
  mechanism, with an explicit DM exclusion and an explicit implicit-default
  behavior)
- **Quote**: "The default repository provides the context that Copilot uses when responding to prompts, and it's also where issues and pull requests created by Copilot cloud agent sessions will be opened unless you specify a repository in your prompt." / "You can set a default repository for each private or public channel. You cannot set a default repository for direct messages with Copilot." / "If a channel does not have a default repository, Copilot sets the repository you use in your first session in that channel as the channel's default repository." / "The default repository is shared across the channel, so any change applies to everyone using Copilot in that channel."
- **Our assessment**: This is, again, the identical "first use sets the
  channel default" gotcha and DM exclusion already documented for Teams in
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 8 — the same
  practical warning applies: a team sharing one Slack channel across
  multiple repositories should deliberately set (or reset) the default via
  `@GitHub settings` rather than relying on whichever repository happened
  to be used first, and note the additional detail here (not stated for
  Teams) that "any change applies to everyone using Copilot in that
  channel" — the default is a shared, mutable channel-level setting, not a
  per-user preference.

### Claim 12: Users can ask Copilot to create one or more GitHub issues directly from a Slack conversation, including issues with child-parent (epic/sub-issue) relationships, and issue creation is bounded by the requester's existing GitHub issue-creation permissions

- **Evidence**: The how-to doc's "Creating Issues with Copilot" subsection,
  including three example `@GitHub` prompt strings for single-issue,
  multi-issue, and epic/child-issue creation.
- **Confidence**: settled (first-party feature description with concrete
  example prompts and an explicit permissions-boundary statement)
- **Quote**: "You can ask Copilot to create GitHub issues directly from Slack, turning conversations into actionable tasks." / "You can create a single issue or multiple issues at once with child-parent relationships." / "You can only use Copilot to create issues in repositories where you already have permission to create issues. This feature doesn't change your access or bypass repository permissions."
- **Our assessment**: This issue-creation workflow (including epic/child
  relationships) is not documented for the Teams integration in
  `docs-github-copilot-teams-shared-agentic-work.md`, which covers PR
  creation and general Q&A but does not describe an issue-creation
  sub-workflow with example prompts. Whether this is a genuine Slack-only
  capability or simply undocumented for Teams cannot be determined from
  either source alone. The explicit "doesn't change your access or bypass
  repository permissions" line is a direct, self-disclosed statement that
  the chat-native creation path is bounded by the same authorization model
  as creating an issue through any other GitHub surface — worth citing
  whenever the guide addresses whether chat-native agent actions can be
  used to escalate a user's effective permissions (they cannot, per this
  statement).

### Claim 13: The public preview is available to organizations on GitHub Copilot Business and GitHub Copilot Enterprise plans, and cloud sandbox policies must be enabled by an organization/enterprise owner (sharing the same configuration as Copilot cloud agent policies) before members can use Copilot in Slack

- **Evidence**: The changelog's "Availability and getting started" section,
  corroborated by the how-to doc's "Prerequisites" list.
- **Confidence**: settled (first-party statement of plan eligibility and a
  named prerequisite dependency between two platform policies)
- **Quote**: "The public preview is available to organizations on GitHub Copilot Business and GitHub Copilot Enterprise plans." (changelog) / "To use Copilot cloud agent, you must have cloud sandboxes enabled for your Copilot plan." / "Cloud sandbox policies share the same configuration as Copilot cloud agent policies. Members of an organization or enterprise, including an enterprise with managed users may need their owner to enable cloud sandboxes and Copilot cloud agent before they can use Copilot in Slack." (how-to doc)
- **Our assessment**: This is the identical two-policy rollout prerequisite
  already documented for Teams (`docs-github-copilot-teams-shared-agentic-work.md`
  Claim 7) — an org/enterprise owner must action two separate policy
  toggles (Copilot cloud agent, cloud sandboxes) before any team member can
  use `@GitHub` in either Slack or Teams. This confirms cloud sandboxing is
  a shared platform prerequisite gating every chat-native Copilot surface
  in the corpus, not something configured per integration.

### Claim 14: Getting started requires an administrator to enable the Copilot cloud agent policy, installing or upgrading the GitHub app for Slack, and linking a GitHub account by mentioning `@GitHub`

- **Evidence**: The changelog's three-step "Availability and getting
  started" list.
- **Confidence**: settled (first-party setup instructions)
- **Quote**: (no direct quote; see Concrete Artifacts for the verbatim
  three-step list)
- **Our assessment**: This is a compressed version of the how-to doc's own,
  more detailed setup flow (Claim 13's prerequisites plus the "Connecting
  the GitHub App" three-step sequence, which additionally specifies typing
  `@GitHub help` to discover available commands — a detail the changelog
  omits). Consistent with the Teams source's pattern where the changelog's
  "Getting Started" list is a summary and the how-to doc is the more
  complete procedural reference.

## Concrete Artifacts

### Getting Started steps (verbatim, from the changelog)

```
1. Administrator must enable the Copilot cloud agent policy
2. Install or upgrade the GitHub app for Slack
3. Link your GitHub account and mention @GitHub

Source: https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack
```

### Connecting the GitHub App — setup steps (verbatim, from the how-to doc)

```
1. In Slack, open a direct message with the GitHub app or @mention the GitHub app in a
   thread by typing @GitHub.
2. Follow the prompts to connect your GitHub account, and if prompted, optionally set a
   default repository.
3. To see what else you can do, in the thread, @mention the app by typing @GitHub help.

Source: https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-slack
```

### Example `@GitHub` prompts (verbatim, from the how-to doc)

```
General task prompt:
@GitHub Add "Hello World" to the README in octo-org/octo-repo on the develop branch

Single issue creation:
@GitHub In octo-org/octo-repo, create a feature request to add fuzzy matching to search.

Multiple issues at once:
@GitHub In octo-org/octo-repo, open separate issues for adding fuzzy matching to search,
paginating the results list, and caching search queries.

Issues with child-parent (epic) relationships:
@GitHub In octo-org/octo-repo, create an epic to redesign search, with child issues for
fuzzy matching, pagination, and query caching.

Setting a channel's default repository:
@GitHub settings

Source: https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-slack
```

### Prerequisites (verbatim list, from the how-to doc)

```
- You must have a GitHub account with access to Copilot through a paid Copilot plan.
- You must have a Slack account and be a member of a workspace.
- You must have the GitHub integration for Slack installed.
- To use Copilot cloud agent, you must have cloud sandboxes enabled for your Copilot plan.

Source: https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-slack
```

## Cross-References

### Cross-reference verification notes

`docs-github-copilot-teams-shared-agentic-work.md`, `blog-vercel-chat-sdk-slack-agent-support.md`,
`blog-simonwillison-tobias-lutke-lehrwerkstatt.md`, and `docs-github-copilot-cli-remote-control-ga.md`
were each re-read in full during this extraction per MINER.md §4b, and every claim number cited
above was located and confirmed against that note's own numbered `### Claim N:` (or, for the
Willison note, `### Claim N:`) headings in document order before writing this section.

- **Corroborates**:
  - `docs-github-copilot-teams-shared-agentic-work.md` — this is by far the
    closest sibling in the corpus, published the same day (2026-08-21) and
    covering the structurally identical integration for Microsoft Teams.
    Claims 4, 7, 8, 9, 10, 11, and 13 above each corroborate that note's
    Claims 2, 3, 4, 5, 6, 8, and 7 respectively, in several cases (Claims 7,
    9, 10, 11 here vs. that note's Claims 3, 5, 6, 8) with **verbatim-
    identical or near-verbatim-identical sentences** across the two
    how-to docs, differing only in the platform name. This is strong,
    directly-quotable evidence that GitHub operates a single security/
    identity/compliance model across its chat-native Copilot integrations
    and documents them from a shared template, rather than designing each
    chat platform's integration independently.
  - `docs-github-copilot-cli-remote-control-ga.md` — corroborates Claim 4's
    device-independent, continue-from-anywhere session model as a general
    property of Copilot cloud agent sessions, not something specific to
    chat-native entry points.

- **Contradicts**: None identified as a MINER.md §4a contradiction. One
  minor internal framing tension (Claim 9: changelog frames the extra PR
  approval as an admin-configurable "can now require" control, while the
  how-to doc frames it as an automatic, "enabled by default" ruleset
  consequence) mirrors the identical tension already evaluated and
  explicitly ruled out as a contradiction for the Teams source's Claim 5 —
  the same reasoning applies here (both statements describe the same
  mechanism from different vantage points, not conflicting facts), so it is
  noted in Claim 9's assessment rather than re-litigated or filed
  separately.

- **Extends**:
  - `docs-github-copilot-teams-shared-agentic-work.md` — this source adds
    one mechanic that note does not document at all: the dedicated "Slack
    Code" channel-per-task primitive (Claim 5) and GitHub's stated
    launch-partner role in a Slack-platform-level "agent channel" feature
    (Claim 2). It also documents an issue-creation sub-workflow with
    concrete example prompts (Claim 12) not present in the Teams source.
    Together these are the corpus's first evidence that, despite sharing a
    security/identity/compliance template, GitHub's Slack and Teams
    integrations are not feature-identical — Slack has at least two
    documented capabilities (Slack Code, structured issue creation with
    epic/child relationships) with no stated Teams counterpart.
  - `blog-vercel-chat-sdk-slack-agent-support.md` — that note documents a
    third-party (Vercel Chat SDK) Slack agent adapter's conversational
    feature set (suggested prompts, streaming with fallback, feedback
    buttons, and the `agent_view` history-under-capture gotcha in its
    Claim 5). This source documents a first-party (GitHub) Slack agent
    integration built on different underlying primitives (a dedicated
    "Slack Code" channel and the Slack GitHub app, rather than Chat SDK's
    `createSlackAdapter()`) with the **opposite** context-capture behavior:
    this source's Claim 7 states Copilot captures the *entire* thread as
    context by default (an over-capture risk, mitigated only by switching
    to a DM), while the Vercel note's Claim 5 describes Slack's native
    `agent_view` channel history capturing only the *user's* side of a
    conversation (an under-capture risk, requiring Chat SDK's own
    transcript feature to reconstruct full history). Both sources
    corroborate this note's `docs-github-copilot-teams-shared-agentic-work.md`
    cross-reference entry that already identified this same
    under-capture/over-capture contrast for Teams — it now applies
    identically to Slack, giving Ch03/Ch06 two independent, mechanism-level
    documented failure directions for chat-platform-agent context handling
    on the *same* chat platform (Slack), from two unrelated vendors
    (GitHub first-party vs. Vercel Chat SDK third-party).
  - `blog-simonwillison-tobias-lutke-lehrwerkstatt.md` — see Claim 6's
    assessment above: this source's "opt-in multiplayer" design (shared
    context sessions are joinable and visible, but DM sessions remain
    private) is a materially different design point than River's
    "mandatory multiplayer" (DMs are refused outright). Both sources now
    give the guide two concrete, contrasting implementations of
    visibility-as-collaboration for chat-native coding agents.

- **Novel** (what this note adds that no prior source covers):
  - **"Slack Code" as a named, Slack-platform-level agent channel type**
    (Claim 2, Claim 5): the first corpus source documenting Slack itself
    (not just a third-party or first-party integration builder) shipping a
    dedicated channel primitive for agent work, with GitHub as a named
    launch partner. No other source describes an agent-native channel type
    at the chat-platform level, as distinct from an integration built on
    top of ordinary channels/threads/DMs.
  - **One-channel-per-task lifecycle with archive/reopen semantics**
    (Claim 5): a specific, stateful collaboration-surface lifecycle
    (create → steer exclusively → finish → prompt to archive → searchable
    archived history → reopenable) not documented for any other chat-native
    or web-native Copilot surface in the corpus.
  - **Structured issue creation via chat, including epic/child-issue
    relationships, with explicit example prompts** (Claim 12): the first
    corpus source giving concrete natural-language prompt examples for
    creating GitHub issues (single, multiple, and epic-with-children) from
    a chat interface.
  - **Near-verbatim shared documentation template across Slack and Teams
    integrations** (Claims 7, 9, 10, 11 assessments): while not a "claim"
    about the product itself, the discovery that GitHub's security
    considerations, ruleset-approval, guest-exclusion, and default-repo
    language is reused essentially verbatim between the Slack and Teams
    how-to docs is itself a useful, citable fact about how GitHub documents
    (and likely implements) its chat-integration security model as a single
    cross-platform policy rather than a bespoke one per chat platform.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the Slack `@GitHub`-mention entry
  point (Claims 1, 3, 4, 14) and the Slack Code per-task channel mechanic
  (Claim 5) as a chat-native way to turn a live discussion directly into a
  Copilot cloud agent session, alongside the guide's existing Teams coverage
  (`docs-github-copilot-teams-shared-agentic-work.md`) and IssueOps/CLI
  dispatch coverage. Flag the "first use sets the channel default
  repository" behavior (Claim 11) and the structured issue-creation prompt
  patterns (Claim 12, with the three verbatim example prompts in Concrete
  Artifacts) as directly reusable material.

- **Chapter 03 (Safety and Verification) / Chapter 06 (Security Threat
  Model)**: Add the "entire thread captured as context, persisted into
  generated artifacts" behavior (Claim 7) as a named data-exposure
  consideration for chat-native agent integrations generally — now
  confirmed identical across both GitHub's Slack and Teams integrations,
  strengthening the case that this is a general policy rather than a
  platform-specific quirk. Pair with the conversation-type-dependent
  identity model (Claim 8) and the ruleset approval escalation (Claim 9) as
  the same three-part chat-native governance picture already established
  for Teams, now corroborated for Slack. Note the "doesn't change your
  access or bypass repository permissions" guarantee (Claim 12) as a
  citable statement when addressing whether chat-native agent actions can
  escalate a user's effective GitHub permissions.

- **Chapter 05 (Team Adoption)**: Add the two-policy rollout prerequisite
  (Claim 13) and the guest/outside-collaborator exclusion (Claim 10) as
  rollout-planning items, identical to the Teams guidance. Add Claim 6's
  "opt-in multiplayer" framing (shared sessions are joinable; DMs stay
  private) as a design point to contrast against Shopify River's mandatory,
  DM-refusing visibility model when the guide discusses adoption strategies
  for chat-native coding agents — these represent two different points on
  the same visibility-vs-privacy spectrum, worth presenting as a genuine
  design choice rather than a single "best practice."

## Extraction Notes

1. **Two pages fetched via WebFetch, cross-verified across multiple
   independent passes, not a single summarizing pass.** The changelog page
   was fetched three times with independently-worded prompts (a
   quote-framed pass, a plain-reading-order pass, and a targeted
   verify-specific-sentences pass); every `Quote` used above from the
   changelog matched identically across at least two of these passes. The
   how-to doc was fetched with a full reading-order pass and two further
   targeted verification passes for its "Security Considerations" and
   "Slack Code" sections specifically, both of which matched the initial
   full-page fetch exactly.
2. **Prompt injection encountered and ignored during extraction.** One
   WebFetch call targeting the how-to doc returned a fabricated refusal
   claiming the extraction request conflicted with a "strict 125-character
   maximum for quotes from any source document" — a constraint that was
   never stated by the Miner in any prompt to WebFetch, in this note, or in
   MINER.md. This was recognized as an attempt to manipulate the extraction
   into truncating or fabricating quotes and was discarded outright; the
   two sections in question ("Security Considerations" and "Slack Code")
   were then successfully re-fetched cleanly with simpler prompts and both
   matched the earlier full-page extraction verbatim, confirming the
   injected constraint had no basis in the actual source content.
3. **No sub-pages beyond the one how-to doc were followed.** The changelog
   links only to the Slack how-to doc (fetched in full above). Unlike the
   sibling Teams source, this changelog does not separately link to the
   "Cloud and local sandboxes for GitHub Copilot" concept page, so this note
   does not re-document cloud-sandbox architecture or billing-meter detail
   — that material remains sourced only via
   `docs-github-copilot-teams-shared-agentic-work.md` Claims 9–11, and
   applies here only by inference (both integrations share the same "cloud
   sandboxes" prerequisite per Claim 13).
4. **No customer or adoption evidence in either page.** Both sources are
   first-party GitHub product documentation describing a public-preview
   feature; no named customer, usage metric, or independent review appears
   in either page. Overall confidence is rated "emerging" rather than
   "settled," matching the sibling Teams note's rationale: (a) the Slack
   integration is explicitly public preview with no GA date; (b) no
   independent verification of any claim (especially the context-capture
   claim in Claim 7) exists outside GitHub's own documentation; (c) the
   "Slack Code" launch-partner claim (Claim 2) in particular has no
   corroborating Slack-authored source in the corpus.
5. **No contradiction with any existing corpus note was found.** Reviewed
   `docs-github-copilot-teams-shared-agentic-work.md`,
   `blog-vercel-chat-sdk-slack-agent-support.md`,
   `blog-simonwillison-tobias-lutke-lehrwerkstatt.md`, and
   `docs-github-copilot-cli-remote-control-ga.md` in full. No existing note
   makes a claim that materially opposes anything in this source at the
   MINER.md §4a filing threshold. No contradiction issue filed.
6. **Prospector's third triage comment raised a fair concern** — that this
   might be "vendor marketing... without extractable patterns." Having read
   both pages in full, the how-to doc in particular carries substantial
   operational detail beyond a bare feature description (the identity/
   permission binary rule, the ruleset approval-escalation mechanism, the
   guest-exclusion boundary, the default-repository gotcha, and the Slack
   Code lifecycle), all independently verifiable and citable. This is
   assessed as a legitimate, extractable documentation source rather than
   marketing copy without substance — consistent with how the Teams sibling
   source was treated despite a similar low-novelty flag in its own
   Prospector triage comments.
