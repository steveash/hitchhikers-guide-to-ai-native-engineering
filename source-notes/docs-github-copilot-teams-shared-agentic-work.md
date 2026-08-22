---
source_url: https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams
source_type: docs
title: "Shared agentic work with GitHub Copilot in Microsoft Teams"
author: GitHub (official changelog)
date_published: 2026-08-21
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: emerging
issue: "#2857"
---

# Shared Agentic Work with GitHub Copilot in Microsoft Teams

> GitHub's August 2026 changelog announces a public-preview Teams integration
> that lets any conversation participant steer a Copilot cloud agent session
> via `@GitHub` mentions, captures the entire thread as agent context, creates
> artifacts under the app's identity (not a personal account) in shared
> threads, and lets repository admins require an extra PR approval for
> Teams-originated Copilot work — a new chat-native entry point onto the same
> Copilot cloud agent / cloud sandbox substrate already documented elsewhere
> in this corpus via CLI, VS Code, issues, and projects surfaces.

## Source Context

- **Type**: docs (GitHub official changelog, `github.blog/changelog`,
  published August 21, 2026; approximately 2-minute read, tagged
  "collaboration tools" and "copilot"). Two linked GitHub Docs pages were
  followed in full per MINER.md §1, since the changelog entry itself gives
  only a compressed summary of the underlying mechanics: "Integrating
  Copilot cloud agent with Teams" (the how-to reference, fetched via its
  embedded Next.js `__NEXT_DATA__` JSON payload, not a summarizing fetch)
  and "Cloud and local sandboxes for GitHub Copilot" (the sandboxing concept
  page, same extraction method).
- **Author credibility**: First-party GitHub product changelog and official
  docs. Authoritative for feature existence, configuration steps, identity/
  permission semantics, and billing mechanics. Not a source for adoption
  data, comparative UX quality against other Copilot surfaces, or how often
  teams actually use this integration versus IDE/CLI/web surfaces — no
  customer quotes, metrics, or case studies appear in any of the three pages.
- **Scope**: Covers the Teams-specific entry point for GitHub Copilot cloud
  agent (starting sessions via `@GitHub` mention, thread-as-context capture,
  identity/permission model for DM vs. shared-context sessions, compliance
  approval gating, availability/billing) plus the general cloud-sandboxing
  mechanism that underlies it (session lifecycle, isolation model, billing
  meters). Does NOT cover: the Teams app's installation permission scopes in
  API/manifest terms, a rollout timeline to GA, independent security review
  of the Teams integration specifically, or how this compares in practice to
  Vercel's Chat SDK / Slack agent adapter (`blog-vercel-chat-sdk-slack-agent-support.md`)
  beyond what can be inferred by comparing the two sources' stated behavior.

## Extracted Claims

### Claim 1: Any Teams conversation participant can start a Copilot cloud agent session by mentioning `@GitHub` in a channel, thread, or direct message, and can supply context or help steer the session, but only participants with write access to the target repository can trigger Copilot to make changes

- **Evidence**: The changelog's lead description under "Turn meeting decisions
  into ready work," corroborated by the how-to doc's more explicit permission
  statement.
- **Confidence**: settled (first-party feature description of a shipping
  public-preview mechanism, consistent across both the changelog and the
  how-to doc)
- **Quote**: "Turn a Microsoft Teams discussion into a collaborative agent session everyone can see and help direct. Mention @GitHub in a channel, thread, or direct message to start a GitHub Copilot cloud agent session. Anyone in the conversation can ask questions, add context, and help plan or steer the work. Participants with write access to the repository can trigger Copilot to make changes."
- **Our assessment**: This is a two-tier participation model: any participant
  can shape the request (ask questions, add context, steer), but only write-
  access holders can authorize Copilot to actually act on the repository. The
  how-to doc states this identically but adds an explicit exclusion — see
  Claim 6 — that the changelog itself does not mention. For Ch01 (Daily
  Workflows) and Ch05 (Team Adoption): this is a concrete "who can do what"
  permission split for a chat-native agent surface, directly comparable to
  the "workspace-level boundaries, not per-item sharing" and role-roster
  guidance already documented for Anthropic's Claude Tag in
  `blog-anthropic-human-agent-teams.md` Claims 2 and 5 — see Cross-References.

### Claim 2: Work started in Teams continues asynchronously in a secure cloud sandbox, and can be picked up afterward from a terminal, the GitHub Copilot app, or a preferred IDE — not only from within Teams

- **Evidence**: The changelog's "Continue work across GitHub Copilot surfaces"
  section, corroborated by the how-to doc's "Secure cloud sandboxes" section.
- **Confidence**: settled (first-party description of a named, cross-surface
  continuation mechanism)
- **Quote**: "Start a task from Teams and let Copilot work asynchronously in a secure cloud sandbox. Follow progress in the channel thread, then continue working with the agent-generated artifacts from your terminal, the GitHub Copilot app, or your preferred IDE."
- **Our assessment**: This positions Teams as one entry point among several
  onto the same underlying Copilot cloud agent execution substrate, rather
  than a Teams-specific agent implementation. This corroborates and extends
  `docs-github-copilot-issues-projects-sessions.md` Claim 1, which documents
  GitHub issues/projects as another surface for "view and steer cloud agent
  sessions... without leaving your workflow" — Teams is a further such
  surface, now chat-native rather than web- or IDE-native. For Ch04
  (Agentic Workflows): document the growing set of Copilot cloud agent entry/
  monitoring points (CLI remote control, VS Code, JetBrains, issues/projects
  sidebar, and now Teams) as converging on one session substrate accessible
  from wherever a practitioner is already working.

### Claim 3: The how-to documentation states explicitly that mentioning `@GitHub` in a shared context causes Copilot to capture the entire thread as request context, and that a user who wants to limit that context should send a direct message instead

- **Evidence**: A dedicated "Security considerations" callout in the how-to
  doc, placed immediately before the identity/permissions section.
- **Confidence**: settled (first-party, explicitly labeled as a security
  consideration rather than a passing feature description)
- **Quote**: "Before you @mention GitHub in Teams, consider that Copilot cloud agent will capture the entire thread as context for your request, understanding and implementing solutions based on the discussion. This context is stored in the artifacts the agent generates. If you want to limit the context, you can send a direct message to the GitHub app for Teams instead."
- **Our assessment**: This is the single most operationally important claim
  in the source for a harness/security audience — it is a self-disclosed data-
  exposure surface, not a marketed capability. "This context is stored in the
  artifacts the agent generates" means an entire channel thread's contents
  (potentially including off-topic remarks, other participants' unrelated
  messages, or accidentally-shared sensitive detail) can be captured and
  persisted into an issue, PR description, or comment. This is worth
  contrasting directly with Vercel's Chat SDK Slack adapter behavior
  documented in `blog-vercel-chat-sdk-slack-agent-support.md` Claim 5, which
  describes the *opposite* data-completeness problem — there, a chat
  platform's native history under `agent_view` captures only the user's side
  of a conversation, requiring a separate transcript mechanism to reconstruct
  full context. Here, the concern runs the other way: Copilot in Teams
  captures *too much* (the entire thread) by default, and the documented
  mitigation is an environment change (switch to DM) rather than a scoping
  configuration. For Ch03 (Safety and Verification) and Ch06 (Security Threat
  Model): teams should treat any `@GitHub`-in-a-channel session as an implicit
  broad data-capture event and adopt discussion hygiene (or use DMs for
  sensitive planning) rather than assuming the agent reads only the directly-
  addressed message.

### Claim 4: The identity used for Copilot-created artifacts depends on the conversation type — in a direct message, Copilot acts using the requester's personal GitHub permissions; in a shared context (channel or group thread), artifacts such as pull requests are created under the app's identity rather than any individual's personal account

- **Evidence**: The how-to doc's "Understanding collaborative sessions,
  permissions, and sandboxes" section states this distinction directly, with
  a follow-on Note calling out the ruleset consequence.
- **Confidence**: settled (first-party statement of the platform's identity-
  attribution model, stated as a clear binary rule keyed on conversation type)
- **Quote**: "The identity Copilot uses depends on whether you interact with it in a direct message or a shared context. When you use Copilot in a direct message, it can take actions for you, such as creating pull requests or issues, as well as answer questions. It uses the permissions of your linked GitHub personal account to take these actions. When you use Copilot in a shared context, such as a group thread or channel, Copilot creates artifacts, such as pull requests, under its app identity rather than your personal account."
- **Our assessment**: This is architecturally significant: a PR opened from a
  1:1 Teams DM is attributed to the requesting human, but the identical
  request made in a team channel is attributed to a non-human app identity —
  the same underlying action produces differently-attributed artifacts purely
  based on where the conversation happened. This directly motivates Claim 5
  (the ruleset approval-count consequence) and is the concrete mechanism
  behind Claim 6 in `docs-github-copilot-teams` (compliance oversight). It
  also parallels — without being identical to — the app-identity-vs-personal-
  identity distinction Anthropic documents for Claude Tag's credential model
  in `blog-anthropic-agent-identity-access-model.md` Claim 8 ("the credential
  is stored independently and mapped to that channel's identity, then
  injected at the network boundary at request time"), whose credentials are
  never attached to individual user accounts per that note's own assessment.
  Anthropic's model always uses a non-personal, channel-scoped identity,
  whereas GitHub's model conditionally uses either the personal account (DM)
  or the app identity (shared context) depending on where the request
  originates — see Cross-References.

### Claim 5: Because Teams-originated pull requests from a shared context are attributed to the app identity rather than a person, repository rulesets automatically require one additional approval beyond whatever a repo already requires — enabled by default — since these PRs are not attributed to a person

- **Evidence**: A "Note" callout immediately following the identity/
  permissions explanation in the how-to doc, corroborated by the changelog's
  "Compliance Oversight" section describing the same mechanism from the
  admin-configuration side.
- **Confidence**: settled (first-party statement of a specific, automatic
  ruleset behavior, corroborated across two independently-worded first-party
  pages)
- **Quote**: "Pull requests created in a shared context by Copilot use the app's identity. If you use repository rulesets, because these pull requests aren't attributed to a person, one more approval is required before merging, as long as the repository already requires at least one approval. This is enabled by default. See Available rules for rulesets."
- **Quote** (changelog, admin framing): "Repository administrators can now require an additional approval for any pull request attributed to the Microsoft Teams Copilot integration identity before it can merge. If you require two approvals in a repository, with this enabled you will need three for Copilot-created pull requests."
- **Our assessment**: There is a subtle but important tension between the two
  first-party statements worth flagging for extraction accuracy, though not
  a MINER.md §4a contradiction (both describe the same underlying mechanism
  from different angles, not conflicting facts): the how-to doc says the
  extra approval is a consequence of ruleset logic "enabled by default"
  whenever a repo already requires at least one approval, while the
  changelog frames the same behavior as something administrators "can now
  require" — implying an opt-in control. Read together, the most consistent
  interpretation is that the *base* mechanism (unattributed-PR-needs-one-
  more-approval under rulesets) is a standing ruleset behavior, while the
  changelog additionally describes an explicit admin-facing setting to
  require this for the Teams Copilot identity specifically. Practitioners
  configuring this should verify the exact toggle in their own repository
  settings rather than assume either page's framing is complete on its own.
  For Ch05 (Team Adoption) and Ch06 (Security Threat Model): document this
  as a concrete "keep a human in the loop" compliance control specifically
  triggered by chat-originated, app-attributed agent work — worth contrasting
  with Vercel's admin-centralized-policy governance model
  (`blog-vercel-enterprise-apps-and-agents.md` Claim 3) as another vendor's
  parallel "policy set centrally, not per-builder" approach, though Vercel's
  is an access-gating control and GitHub's here is a merge-gating control.

### Claim 6: Guest members of a Teams workspace and outside collaborators to a repository cannot start or steer a Copilot session in Teams at all

- **Evidence**: A direct exclusion statement in the how-to doc's permissions
  section, not mentioned anywhere in the changelog itself.
- **Confidence**: settled (first-party statement of an access exclusion)
- **Quote**: "Only users with write access to a repository can trigger Copilot to make changes, but any conversation participant can provide input. Guest members of a workspace, and outside collaborators to repositories are not able to start or steer a session with Copilot in Teams."
- **Our assessment**: This sharpens Claim 1's "any conversation participant"
  framing — it is not literally *any* participant. Guests and outside
  collaborators are excluded from initiating or steering entirely, not merely
  restricted from triggering changes. This is a detail the changelog entry
  omits, and the Assayer/Smith should treat the changelog alone as an
  incomplete permission specification — the how-to doc is the authoritative
  source for this exclusion. For Ch05 (Team Adoption): flag this exclusion
  explicitly when documenting rollout to teams that include external/guest
  members (a common Teams configuration in cross-company collaborations).

### Claim 7: Setting up the integration requires an administrator to have enabled both GitHub Copilot cloud agent and cloud sandboxes for the organization, since cloud sandbox policies share the same configuration as cloud agent policies

- **Evidence**: The how-to doc's "Prerequisites" list and a corroborating
  Note in the same section; also present in compressed form in the
  changelog's "Getting Started" list.
- **Confidence**: settled (first-party statement of a prerequisite dependency
  between two named platform policies)
- **Quote**: "To use Copilot cloud agent, you must have cloud sandboxes enabled for your Copilot plan. See Cloud sandboxing for GitHub Copilot." / "Cloud sandbox policies share the same configuration as Copilot cloud agent policies. Members of an organization or enterprise, including an enterprise with managed users may need their owner to enable cloud sandboxes and Copilot cloud agent before they can use Copilot in Teams."
- **Our assessment**: This ties the Teams integration's availability directly
  to the general cloud-sandboxing policy documented in the "Cloud and local
  sandboxes for GitHub Copilot" concept page (Claim 9 below) — an
  organization that has not separately enabled cloud sandbox access (which
  the sandboxing doc states is "disabled by default" at the org level) cannot
  use Teams Copilot regardless of whether individual members have Copilot
  seats. For Ch05 (Team Adoption): add this as a rollout-blocking prerequisite
  — teams evaluating the Teams integration need an org/enterprise owner to
  action two separate policy toggles (cloud agent, cloud sandboxes) before
  any team member can use `@GitHub` in Teams.

### Claim 8: A Teams channel can have a default repository, which provides the context Copilot uses when responding and is where Copilot-created issues/PRs are opened unless a repository is specified in the prompt; direct messages do not use a default repository at all

- **Evidence**: The how-to doc's "Connecting the GitHub app to your GitHub
  account" and "Setting a default repository for a channel" sections;
  corroborated by the changelog's "Getting Started" step 4.
- **Confidence**: settled (first-party description of a configuration
  mechanism, with an explicit DM exclusion)
- **Quote**: "The default repository provides the context that Copilot uses when responding to prompts, and it's also where issues and pull requests created by Copilot cloud agent sessions will be opened unless you specify a repository in your prompt." / "You cannot set a default repository for direct messages with Copilot."
- **Our assessment**: The how-to doc also documents an implicit-default
  behavior not stated in the changelog: "If a channel does not have a default
  repository, Copilot sets the repository you use in your first session in
  that channel as the channel's default repository" — meaning the first
  `@GitHub` request in a channel silently establishes that channel's default
  going forward, which could surprise a team that intended to use the same
  channel across multiple repositories. For Ch01 (Daily Workflows): document
  this "first use sets the default" behavior explicitly as a gotcha — teams
  working across multiple repositories from one channel should set (or
  reset) the default deliberately via `@GitHub settings` rather than relying
  on whichever repository happened to be used first.

### Claim 9: Cloud sandboxing runs an entire Copilot CLI session remotely inside a fully isolated, ephemeral Linux environment hosted by GitHub, built on Azure Container Apps Sandboxes, with GitHub providing only the identity, policy, and billing layer on top

- **Evidence**: The "Cloud and local sandboxes for GitHub Copilot" concept
  page's "Cloud sandboxing" section, extracted from the page's embedded
  `renderedPage` JSON (not a summarizing fetch).
- **Confidence**: settled (first-party architectural description naming the
  specific underlying infrastructure provider and GitHub's role on top of it)
- **Quote**: "Cloud sandboxing lets you run Copilot CLI sessions inside fully isolated, ephemeral Linux environments hosted by GitHub. Each cloud sandbox session is isolated from your local environment and from other sessions." / "Cloud sandboxing is built on Azure Container Apps Sandboxes, with GitHub providing the identity, policy, and billing layer."
- **Our assessment**: This is the general cloud-sandbox mechanism that the
  Teams integration's "secure cloud sandbox" (Claim 2 above) is built on top
  of — the Teams changelog and how-to doc describe the sandbox only as
  "secure," while this concept page supplies the actual architecture (Azure
  Container Apps Sandboxes as the isolation substrate, GitHub as the control-
  plane operator). This is architecturally the same control-plane/data-plane
  vendor split pattern already documented for Vercel's BYOC-on-AWS
  (`blog-vercel-enterprise-apps-and-agents.md` Claim 9: "Vercel runs the
  control plane on top of it") and Anthropic's Claude Managed Agents
  self-hosted sandboxes (per that Vercel note's Cross-References) — though
  here GitHub is the vendor retaining the control plane on top of a *different*
  cloud vendor's (Microsoft Azure) infrastructure, rather than a customer's
  own account. For Ch02 (Harness Engineering): document this as a distinct,
  named cloud-sandbox architecture worth distinguishing from gh-aw's AWF
  sandbox (`docs-ghaw-sandbox-reference.md`) — the two are unrelated products
  from different GitHub-adjacent teams solving isolation for different agent
  execution contexts (Copilot CLI cloud sessions vs. GitHub Actions-based
  agentic workflows); using the term "sandbox" for both risks conflating two
  distinct security models with different underlying mechanisms (Azure
  Container Apps Sandboxes vs. AWF's OS-level firewall/MXC).

### Claim 10: Cloud sandbox sessions have three lifecycle states — active, stopped (state snapshotted and resumable), and deleted (unrecoverable) — and because sessions run in GitHub-hosted infrastructure, a stopped session can be resumed from any device regardless of where it was originally started

- **Evidence**: The concept page's "Session lifecycle" and "Continue sessions
  across devices" sections.
- **Confidence**: settled (first-party specification of session state
  semantics)
- **Quote**: "A cloud sandbox session has three main states: Active: The session is running, and you are interacting with it from Copilot CLI. Stopped: The session is not currently running, but its state is saved. When you resume it, your files, environment variables, and in-progress work are restored. Deleted: The session and its saved state are removed and cannot be recovered." / "Because cloud sandbox sessions run in GitHub-hosted infrastructure, you can pick up a Copilot session on any device, regardless of where the session was originally started."
- **Our assessment**: This device-independence property is the specific
  mechanism that makes Claim 2's "continue work... from your terminal, the
  GitHub Copilot app, or your preferred IDE" possible for Teams-originated
  sessions — the session's state lives in GitHub's infrastructure, not on
  whichever machine issued the original request, so "started in Teams,
  continued in an IDE" is a direct consequence of this lifecycle model rather
  than a Teams-specific bridging feature. For Ch04 (Agentic Workflows):
  document the three-state lifecycle (active/stopped/deleted) as the general
  session model underlying every cloud-agent surface in this corpus (Teams,
  issues/projects sidebar per `docs-github-copilot-issues-projects-sessions.md`,
  CLI remote control), since all of them are almost certainly views onto the
  same session state rather than independent execution contexts.

### Claim 11: Cloud sandboxing is billed on three usage meters — compute time, memory allocation, and snapshot storage for stopped sessions — each priced separately and distinct from the (unrelated) AI-credit billing for the cloud agent session itself

- **Evidence**: The concept page's "Billing" section, with an explicit
  three-row meter table; corroborated by the changelog's "Availability"
  section distinguishing AI-credit billing from cloud sandbox billing.
- **Confidence**: settled (first-party pricing/billing specification with
  named meters, units, and per-unit prices)
- **Quote**: "Cloud sandboxing is billed based on usage. GitHub measures cloud sandbox usage across three meters" (table: Compute — "Time that a cloud sandbox session is running." — Compute second — $0.000024; Memory — "Memory allocated to a cloud sandbox session while it is running." — GiB second — $0.000003; Storage — "Snapshot storage for stopped sessions." — GiB month — $0.005).
- **Quote** (changelog, distinguishing the two billing dimensions): "GitHub Copilot cloud agent sessions started in Microsoft Teams consume AI credits. For organizations, cloud agent AI credit usage is governed by usage-based billing budgets. Cloud sandbox usage is billed separately and can be controlled with a product-level or SKU-level budget."
- **Our assessment**: A Teams-originated Copilot session therefore has two
  independent cost dimensions that a practitioner or FinOps owner must
  budget for separately: (1) AI credits for the cloud agent's model usage,
  governed by the org's usage-based billing budgets, and (2) cloud sandbox
  compute/memory/storage meters for the isolated execution environment,
  controlled by a separate product- or SKU-level budget. The Storage meter
  (billed even for *stopped*, non-executing sessions, per GiB-month) means a
  team that starts many Teams sessions and lets them go idle without
  deleting them accrues ongoing storage cost independent of active compute —
  a concrete cost-governance gap for Ch04 (Cost Engineering at Scale) to flag
  explicitly: session cleanup/deletion policy, not just active-usage limits,
  is a real cost lever here.

## Concrete Artifacts

### Getting Started steps (verbatim, from the changelog)

```
1. Confirm administrators have enabled GitHub Copilot cloud agent and cloud sandboxes
2. Install the GitHub app for Microsoft Teams
3. Mention @GitHub and authenticate your GitHub account
4. Configure a default repository for public channels (not required for direct messages)
5. Reference @GitHub followed by your task, or use @GitHub help for available commands

Source: https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams
```

### Usage command examples (verbatim, from the how-to doc)

```
Starting a session:
@GitHub Create a pull request to...YOUR_PROMPT repo=OWNER/REPO_NAME branch=BRANCH_NAME

Connecting the app / seeing available commands:
@GitHub
@GitHub help

Changing channel settings (e.g. default repository):
@GitHub settings

Source: https://docs.github.com/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-teams
```

### Cloud sandbox billing meters (verbatim table, from the sandboxing concept page)

```
| Meter    | Description                                              | Unit             | Price (USD)  |
|----------|-----------------------------------------------------------|------------------|--------------|
| Compute  | Time that a cloud sandbox session is running.              | Compute second   | $0.000024    |
| Memory   | Memory allocated to a cloud sandbox session while running. | GiB second       | $0.000003    |
| Storage  | Snapshot storage for stopped sessions.                      | GiB month        | $0.005       |

Source: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes#cloud-sandboxing
```

### Cloud sandbox CLI invocation (verbatim, from the sandboxing concept page — general mechanism, not Teams-specific)

```bash
copilot ‑‑cloud ‑‑experimental
```

```
Note from source: "Cloud sandboxing is currently an experimental feature. To
use it, you must have experimental features enabled for Copilot CLI—for
example, by using the ‑‑experimental command line option when starting a CLI
session, as shown above." / "Cloud sandboxing is only available for
interactive Copilot CLI sessions. You can't run the CLI programmatically in
a cloud sandbox—that is, you can't combine the ‑‑cloud option with the -p or
-i options."

Source: https://docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes#cloud-sandboxing
```

## Cross-References

### Cross-reference verification notes
`docs-github-copilot-issues-projects-sessions.md`, `blog-anthropic-human-agent-teams.md`,
`blog-anthropic-agent-identity-access-model.md`, `blog-vercel-chat-sdk-slack-agent-support.md`,
`blog-vercel-enterprise-apps-and-agents.md`, and `docs-ghaw-sandbox-reference.md` were
re-read in full (or, for the two long Vercel/gh-aw notes, in full including all
numbered claims) during this extraction per MINER.md §4b, and every claim number
cited above was located and confirmed against that note's own numbered
`### Claim N:` headings in document order before writing this section.

- **Corroborates**:
  - `docs-github-copilot-issues-projects-sessions.md` Claim 1 ("view and steer
    cloud agent sessions... without leaving your workflow"): this source's
    Claim 2 (continue work across CLI/app/IDE from a Teams-originated session)
    confirms the same underlying design intent — cloud agent sessions are a
    single execution substrate viewable/steerable from wherever the
    practitioner already works — now extended to a chat platform (Teams) in
    addition to the issues/projects web surfaces that note documents.
  - `blog-anthropic-human-agent-teams.md` Claim 2 (multiplayer agents require
    "credentials not tied to humans, so they can operate within safe,
    predictable guardrails"): this source's Claim 4 (shared-context artifacts
    attributed to the app identity, not a personal account) is a concrete,
    named instance of exactly this principle on a different vendor's platform
    — GitHub's Teams integration and Anthropic's Claude Tag both move toward
    non-personal, agent-scoped identities for actions taken in shared/group
    contexts.
  - `blog-anthropic-agent-identity-access-model.md` Claim 8 ("the credential
    is stored independently and mapped to that channel's identity, then
    injected at the network boundary at request time"): corroborates the
    same architectural direction as Claim 4 here, though the two differ in
    trigger condition —
    Anthropic's model is always channel-identity-scoped, while GitHub's
    Teams integration conditionally uses either the personal account (DM) or
    the app identity (shared context) depending on conversation type, a
    finer and more conditional split than Anthropic's stated model.
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 3 ("admins set the
    policy centrally rather than relying on each builder to configure it
    correctly"): this source's Claim 5 (rulesets requiring an extra approval
    for app-attributed Copilot PRs, "enabled by default") is a comparable
    centralized-governance default, though scoped to merge-time approval
    gating rather than Vercel Passport's deployment-access gating.

- **Contradicts**: None identified as a MINER.md §4a contradiction. One
  internal tension was evaluated and is documented as an extraction-accuracy
  note rather than filed as a contradiction: the changelog's "Compliance
  Oversight" section frames the extra-approval requirement as something
  administrators "can now require," while the how-to doc frames the same
  underlying ruleset behavior as automatic and "enabled by default" whenever
  a repo already requires at least one approval (see Claim 5's "Our
  assessment"). Both statements describe the same mechanism from different
  vantage points (admin-facing feature framing vs. ruleset-consequence
  framing) rather than asserting conflicting facts about what happens, so
  this does not meet the "materially opposes... both claims would lead to
  different guide advice" bar in MINER.md §4a — no contradiction issue filed.
  A second potential tension — this source's "public preview" availability
  for the Teams integration (Claim 11 quote) versus the sandboxing concept
  page's "Cloud sandboxing is currently an experimental feature" label for
  the general `copilot --cloud --experimental` CLI mechanism (Concrete
  Artifacts) — was also evaluated and ruled out as a contradiction: these are
  two different product surfaces (a Teams-specific integration in public
  preview vs. the general-purpose CLI cloud-sandbox flag, separately marked
  experimental) using two different maturity labels for two different
  surfaces on the same underlying infrastructure, not conflicting maturity
  claims about the same feature.

- **Extends**:
  - `docs-github-copilot-issues-projects-sessions.md`: that note documents
    GitHub-web-native surfaces (issue header pill, sidebar, projects board)
    for cloud agent session visibility. This source extends the same
    underlying session substrate to a chat-native surface (Microsoft Teams),
    adding a new entry point that note does not cover, plus a new mechanic
    that note also does not cover: thread-based context capture and
    conversation-type-dependent artifact identity (Claims 3-4).
  - `docs-ghaw-sandbox-reference.md`: that note documents AWF, the sandbox
    used by GitHub Agentic Workflows (`gh-aw`) for GitHub Actions-based agent
    jobs — a three-tier filesystem model, Docker-socket hiding, and
    environment-variable bridging, all OS-level isolation on the Actions
    runner. This source documents an architecturally distinct sandbox
    product — Copilot's cloud sandbox, built on Azure Container Apps
    Sandboxes as a full remote execution environment for Copilot CLI
    sessions — extending the corpus's sandbox coverage to a second, unrelated
    isolation architecture that happens to share the word "sandbox" with AWF
    but not its mechanism (see Claim 9's "Our assessment" for the explicit
    distinction the guide should preserve).
  - `blog-vercel-chat-sdk-slack-agent-support.md`: that note documents a
    chat-platform agent adapter's context/history handling from the opposite
    failure direction — Slack's native channel history under `agent_view`
    captures only the user's half of a conversation (an under-capture
    problem, Claim 5 there). This source's Claim 3 (Teams captures the
    *entire* thread as context and persists it into generated artifacts)
    extends the corpus's coverage of chat-platform-agent context handling to
    the over-capture direction, giving Ch03/Ch06 material for both failure
    modes practitioners should check for when wiring any chat platform to an
    agent: does the platform's native history under-capture (Slack) or does
    the agent over-capture the full thread by default (Teams)?

- **Novel** (what this note adds that no prior source covers):
  - **Conversation-type-conditional artifact identity** (Claim 4): no prior
    corpus source documents an agent platform where the *same* underlying
    action (opening a PR) is attributed to different identities (personal
    account vs. app identity) purely based on whether the triggering
    conversation was a direct message or a shared/group context.
  - **Automatic ruleset approval-count escalation for unattributed,
    app-identity PRs** (Claim 5): the specific mechanism — one additional
    required approval, "enabled by default," triggered by a PR's app-identity
    (non-human) attribution — is new to the corpus as a named compliance
    control.
  - **Guest/outside-collaborator exclusion from steering chat-native agent
    sessions** (Claim 6): not documented for any other chat-native or
    web-native Copilot surface in the corpus.
  - **"First use sets the channel default" implicit repository binding**
    (Claim 8): a specific, easy-to-miss configuration behavior not documented
    for any other Copilot surface.
  - **Cloud sandbox three-meter billing model (compute/memory/storage) with
    per-unit prices** (Claim 11): the first corpus source to give concrete,
    priced billing meters for GitHub's cloud sandbox product, including the
    detail that storage cost accrues even for stopped, non-executing
    sessions.
  - **Azure Container Apps Sandboxes as the named underlying infrastructure**
    (Claim 9): the first corpus source to name the specific cloud
    infrastructure vendor and product underlying GitHub Copilot's cloud
    sandboxing, distinct from GitHub's own Actions-runner-based AWF sandbox.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the Teams `@GitHub`-mention entry
  point (Claims 1, 2, 8) as a chat-native way to turn a live discussion
  directly into a Copilot cloud agent session, alongside the guide's existing
  coverage of IssueOps and CLI-triggered dispatch. Flag the "first use sets
  the channel default repository" behavior (Claim 8) explicitly as a gotcha
  for teams that share one Teams channel across multiple repositories.

- **Chapter 03 (Safety and Verification) / Chapter 06 (Security Threat
  Model)**: Add the "entire thread captured as context, persisted into
  generated artifacts" behavior (Claim 3) as a named data-exposure
  consideration for any chat-native agent integration — the documented
  mitigation (switch to DM) is an environment choice, not a scoping control,
  so teams should adopt discussion hygiene in shared channels before
  `@GitHub`-mentioning Copilot on sensitive topics. Pair this with the
  conversation-type-dependent identity model (Claim 4) and the ruleset
  approval escalation (Claim 5) as a three-part chat-native governance
  picture: what gets captured, who gets credited, and what merge gate applies.

- **Chapter 04 (Agentic Workflows / Cost Engineering at Scale)**: Add the
  cloud sandbox session lifecycle (active/stopped/deleted, Claim 10) and the
  three-meter billing model (Claim 11) as concrete cost-governance material —
  specifically, that stopped (non-executing) sessions still accrue storage
  cost, making session cleanup a real budget lever distinct from active-usage
  limits. Note the two independent cost dimensions (AI credits for the agent,
  separate compute/memory/storage billing for the sandbox) that FinOps
  guidance should address separately.

- **Chapter 05 (Team Adoption)**: Add the two-policy rollout prerequisite
  (org/enterprise owner must enable both Copilot cloud agent and cloud
  sandboxes, Claim 7) and the guest/outside-collaborator exclusion (Claim 6)
  as rollout-planning items for teams considering the Teams integration,
  particularly organizations with external/guest members in their Teams
  workspace.

## Extraction Notes

1. **Primary source and two linked docs pages fetched via raw payload
   extraction, not summarizing WebFetch.** The changelog page's article text
   was extracted from its raw HTML via `curl` (stripping tags directly from
   the `<article>` element). The two linked GitHub Docs pages
   ("Integrating Copilot cloud agent with Teams" and "Cloud and local
   sandboxes for GitHub Copilot") are Next.js apps; their full article text
   was located inside the page's embedded `__NEXT_DATA__` JSON payload at
   `props.pageProps.articleContext.renderedPage` and extracted from that
   HTML fragment directly via `curl`, not through a summarizing fetch-tool
   pass. Every `Quote` field in this note was copied from that
   directly-extracted text. An initial summarizing WebFetch pass was run
   first for orientation and discarded once the raw-payload extraction
   confirmed several phrasing differences (e.g., the summarizing pass
   rendered Claim 1's quote as "Mention @GitHub in Microsoft Teams channels,
   threads, or direct messages to initiate a GitHub Copilot cloud agent
   session," which is a paraphrase, not the source's actual wording used
   above).
2. **Two substantive linked pages followed, per MINER.md §1.** The changelog
   links to the how-to integration doc and the cloud-sandboxing concept page;
   both were fetched in full since the changelog itself gives only a
   compressed two-paragraph summary of mechanics that the how-to doc and
   concept page document in much greater detail (permission/identity model,
   security considerations, session lifecycle, billing meters). No further
   links (e.g., the Microsoft Teams app-store install link, the
   usage-based-billing docs page, the budget-configuration docs page) were
   followed, as they are either non-substantive (an app-store redirect) or
   narrowly duplicate billing-mechanism detail already covered by the pages
   fetched.
3. **No customer or adoption evidence in any of the three pages.** All three
   sources are first-party GitHub product documentation describing a
   public-preview feature; no named customer, usage metric, or independent
   review appears anywhere in this source set. Overall confidence is rated
   "emerging" rather than "settled" despite most individual claims being
   rated "settled" (unambiguous first-party descriptions of a shipping
   mechanism), because: (a) the Teams integration itself is explicitly public
   preview with no GA date; (b) the underlying cloud-sandboxing CLI mechanism
   is separately labeled experimental; and (c) no independent verification of
   any claim (especially the security/data-capture claim in Claim 3) exists
   outside GitHub's own documentation.
4. **One internal tension documented, not filed as a contradiction.** See
   Cross-References → Contradicts for the changelog-vs-how-to-doc framing
   difference on the extra-approval requirement (admin-configurable feature
   vs. automatic ruleset consequence), and the "public preview" vs.
   "experimental" maturity-label distinction between the Teams integration
   and the underlying CLI cloud-sandbox flag. Both were evaluated against the
   MINER.md §4a filing bar and judged not to meet it — see reasoning inline.
5. **No contradiction with any existing corpus note was found.** Reviewed
   `docs-github-copilot-issues-projects-sessions.md`,
   `blog-anthropic-human-agent-teams.md`,
   `blog-anthropic-agent-identity-access-model.md`,
   `blog-vercel-chat-sdk-slack-agent-support.md`,
   `blog-vercel-enterprise-apps-and-agents.md`, and
   `docs-ghaw-sandbox-reference.md` in full. No existing note makes a claim
   that materially opposes anything in this source at the MINER.md §4a
   filing threshold. No contradiction issue filed.
