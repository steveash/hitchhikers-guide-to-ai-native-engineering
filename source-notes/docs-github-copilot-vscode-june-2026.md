---
source_url: https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases
source_type: docs
title: "GitHub Copilot in Visual Studio Code, June 2026 releases"
author: GitHub (official changelog)
date_published: 2026-07-08
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: settled
issue: "#1719"
---

# GitHub Copilot in Visual Studio Code, June 2026 Releases

> GitHub's July 8, 2026 VS Code roundup (v1.123–v1.127, covering June and early July)
> documents GA browser-agent tooling with a detailed private-tabs/isolated-sessions
> trust model, per-subagent cost visibility, Marketplace-based model provider discovery,
> an explicitly named "Autopilot" permission level, and three new enterprise/security
> hardening features (native device-management settings delivery, MCP OAuth client-secret
> storage, and a two-hour extension auto-update delay).

## Source Context

- **Type**: docs (GitHub official product changelog, July 8, 2026; roundup covering
  VS Code releases v1.123 through v1.127 from June and early July 2026; the primary
  article is short — five theme sections plus an "Also new" list of ten one-line
  items). A linked companion changelog (July 1, 2026, "Browser tools for GitHub
  Copilot in VS Code are generally available") was followed as a substantive sub-page
  per MINER.md §1 and provided most of the security/trust-model detail used below.
- **Author credibility**: GitHub engineering team announcing production features in
  VS Code Copilot. Authoritative for the existence of each feature, exact setting
  names (`workbench.browser.enableChatTools`, `chat.agent.allowedNetworkDomains`,
  `chat.agent.deniedNetworkDomains`, `chat.agent.networkFilter`), and behavioral
  descriptions given in both articles. Not a credible source for: adoption metrics,
  whether "Autopilot" task-completion detection is measurably better, how the
  Marketplace model-provider vetting process works, or any effectiveness data for
  the two-hour extension delay as a supply-chain mitigation.
- **Scope**: Roundup of all VS Code Copilot updates released June–early July 2026,
  organized into five clusters (integrated browser, parallel sessions/chats, cost
  visibility, Marketplace model providers, Autopilot) plus a ten-item "Also new"
  list. The companion GA article covers only the browser-tools feature in depth.
  Does NOT cover: CLI-specific features, Visual Studio (non-Code) features, or
  JetBrains/Eclipse equivalents — those have separate changelogs and separate
  corpus notes (e.g. `docs-github-copilot-vs-may-2026.md`,
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`). Does not enumerate
  a JSON schema for the new file-based managed settings, does not name which model
  providers are available via Marketplace at launch, and does not describe the
  device-management (MDM) configuration schema.

## Extracted Claims

### Claim 1: Agentic browser tools reached general availability in VS Code and are enabled by default

- **Evidence**: Both the July 8 roundup and the July 1 companion changelog state GA
  status and default-on behavior explicitly.
- **Confidence**: settled (product fact — stated in two official changelog entries)
- **Quote**: "Agentic browser tools are now generally available: This is enabled by
  default, allowing agents to navigate pages, inspect content, capture screenshots,
  and validate web apps directly in VS Code." (July 8 roundup)
- **Our assessment**: This confirms the browser-agent capability (previewed earlier
  in 2026) is now default-on infrastructure rather than an opt-in experiment. The
  companion article adds the framing: "Agents can now drive a real browser, navigate
  live web apps, and feed what they find back into the chat." For Ch02: document
  browser-driving as a default agent capability practitioners should assume is
  active in VS Code 1.123+ unless explicitly disabled by policy (see Claim 5).

### Claim 2: Agent access to a user's own browser tabs is private by default and requires an explicit, revocable "Share with Agent" grant per tab

- **Evidence**: The July 1 companion changelog states this under "You stay in
  control" as the first of three trust-model guarantees.
- **Confidence**: settled (product guarantee — stated in official changelog)
- **Quote**: "Your tabs are private by default: The agent can’t read or interact
  with a page you opened until you select Share with Agent, and you can revoke
  that access at any time."
- **Our assessment**: This is the first documented explicit consent gate for
  agent access to a user's *existing* browser tabs (as opposed to tabs the agent
  opens itself, covered separately in Claim 3). The per-tab, revocable-at-any-time
  design means a practitioner can have an agent open a browser session for testing
  while keeping their personal browsing (email, dashboards, other tickets) invisible
  to the agent by default. For Ch02: document "Share with Agent" as the required
  consent action before an agent can read a user-opened tab — practitioners should
  not assume browser-driving agents can see whatever is open unless they explicitly
  shared it.

### Claim 3: Tabs the agent opens itself run in fresh, isolated sessions with no access to the user's cookies or storage, and parallel agents keep their tabs private from one another

- **Evidence**: July 1 companion changelog, second trust-model guarantee.
- **Confidence**: settled (product guarantee — stated in official changelog)
- **Quote**: "The agent’s tabs are isolated: Pages the agent opens itself run in
  fresh sessions with no access to the cookies or storage from your everyday
  browsing. Agents running in parallel in the Agents window each keep their
  browser tabs private from one another."
- **Our assessment**: This is a session-isolation guarantee with two layers: (1)
  agent-opened tabs cannot read the user's authenticated browsing state (no
  session hijacking of the developer's logged-in accounts), and (2) concurrent
  agent sessions (documented in Claim 7, the Parallel Sessions cluster) do not
  leak browser state between each other. For Ch04 (Agentic Workflows — Multi-Session):
  this is a concrete isolation property practitioners running multiple parallel
  agent sessions with browser tools should rely on — one agent's browser-driven
  testing session cannot read or interfere with another's. For Ch05/Ch06/Ch07
  (Security): document this alongside terminal credential isolation
  (`docs-github-copilot-vscode-may-2026.md` Claim 11) as a second documented
  agent/human boundary in VS Code — that note covers terminal-entered credentials
  not reaching the LLM; this covers browser session state not leaking between the
  human's browsing and the agent's, or between concurrent agents.

### Claim 4: Sensitive browser permissions (camera, microphone, location, notifications, clipboard reads) are never granted automatically to agents; only low-risk actions like sanitized clipboard writes are allowed by default

- **Evidence**: July 1 companion changelog, third trust-model guarantee, with an
  explicit enumeration of gated permission types.
- **Confidence**: settled (product guarantee — stated in official changelog with
  explicit enumeration)
- **Quote**: "Sensitive permissions stay under your control: Capabilities like the
  camera, microphone, location, notifications, and clipboard reads are never
  granted automatically. Each one needs your explicit approval for a site, and
  agents can’t approve them on your behalf. Only low-risk actions, such as
  sanitized clipboard writes, are allowed by default."
- **Our assessment**: The explicit statement that "agents can’t approve them on
  your behalf" closes a specific self-approval loophole — an agent instructed
  (or prompt-injected) to grant itself camera/microphone/location access cannot
  do so; only the human can approve per-site. The "sanitized clipboard writes"
  carve-out is notable: writes are allowed by default but implied to be filtered
  ("sanitized") — the mechanism for sanitization is not described. For Ch02:
  document this permission model as the default browser-tool security posture,
  parallel to the terminal credential-isolation guarantee from the May 2026
  roundup. For Ch05/Ch07 (Enterprise Governance/Security): this is a concrete
  answer to the "can a browser-driving agent silently turn on my camera or read
  my clipboard" concern that teams evaluating agentic browser tools will raise.

### Claim 5: Enterprise admins can centrally disable browser tools and restrict which network domains agents and the integrated browser can reach

- **Evidence**: July 1 companion changelog, "Enterprise controls" section, naming
  a dedicated setting and reusing an existing network-filter mechanism.
- **Confidence**: settled (setting names stated in official changelog)
- **Quote**: "A new dedicated on/off switch (workbench.browser.enableChatTools)"
  and "Existing agent network domain controls (chat.agent.allowedNetworkDomains
  and chat.agent.deniedNetworkDomains, enabled with chat.agent.networkFilter)
  that restrict which sites agents and the integrated browser can reach. Denied
  domains take precedence, and both lists support wildcards (e.g., *.example.com)."
- **Our assessment**: Two distinct governance levers: a binary kill switch
  (`workbench.browser.enableChatTools`) and an allow/deny domain filter that now
  *also* governs the integrated browser, not just agent network calls generically
  — implying `chat.agent.allowedNetworkDomains`/`deniedNetworkDomains` predates this
  release and is being extended in scope. The "denied domains take precedence"
  rule is a specific conflict-resolution detail worth documenting for teams writing
  allow/deny lists. For Ch02 (Harness Engineering — Enterprise Configuration): add
  these three settings to the VS Code enterprise configuration surface, alongside
  the `.github-private/.github/copilot/settings.json` mechanism documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` — note that these are
  VS Code *workspace/user settings* (`workbench.*`, `chat.agent.*`), a different
  configuration surface from the enterprise-managed settings.json system, and teams
  should decide which layer to use for browser-tool governance.

### Claim 6: The integrated browser can now proxy HTTP(S) traffic through a remote connection when opened in a remote workspace (public preview)

- **Evidence**: July 8 roundup, "Integrated browser updates" section.
- **Confidence**: emerging (stated as a public preview feature in the official
  changelog)
- **Quote**: "Browse from remote workspaces: When the integrated browser is opened
  in a remote workspace, HTTP(S) web traffic can now be proxied through the remote
  connection. This feature is in public preview."
- **Our assessment**: This extends browser-agent tooling to remote-development
  workflows (SSH remotes, Dev Containers, Codespaces) — without this, an agent
  testing a web app running only on a remote host would have no way to reach it
  from the local integrated browser. For Ch02: document remote workspace browsing
  as a preview-status prerequisite for teams that want browser-driven agent testing
  in remote/containerized dev environments; the public preview status means
  behavior may still change.

### Claim 7: The Agents window now supports running multiple sessions side by side and multiple chats within a single session, with drag-and-drop session organization

- **Evidence**: July 8 roundup, "Parallel sessions and chats" section, three
  bullet points.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "Run sessions side by side: Keep separate agent tasks visible and
  active at the same time." / "Use multiple chats in one session: Break a larger
  change into focused workstreams, so you can keep implementation, review,
  testing, and docs separate while still managing the overall task in one place."
  / "Agent session organization: Tidy up your Agents window by grouping related
  sessions or dragging and dropping your sessions to rearrange them."
- **Our assessment**: The "multiple chats in one session" capability is a new
  substructure not previously documented: a single agent *session* (presumably
  one branch/workspace context) can now contain several distinct *chats*
  (implementation, review, testing, docs) rather than one session mapping to one
  linear conversation. This differs from the May 2026 roundup's Claim 7 ("multiple
  agent sessions can run concurrently side-by-side"), which documented
  session-level parallelism only. For Ch04 (Agentic Workflows — Multi-Session):
  document this as a second, finer-grained level of parallelism inside a single
  session — practitioners can now separate concerns (implement vs. review vs.
  test vs. document) as distinct chats without spinning up entirely separate
  sessions for a single logical task.

### Claim 8: Practitioners can now see total credit cost across a full agent session and inspect credit usage for individual subagents when work is delegated

- **Evidence**: July 8 roundup, "Cost visibility and improvements" section.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "See total session cost: Understand credit usage across the full
  chat, not just one request." / "Inspect subagent usage: See credit usage for
  individual subagent sections when work is delegated."
- **Our assessment**: Per-subagent credit visibility is the first documented
  instance in this corpus of cost attribution *within* a single delegated agent
  workflow, rather than only at the request or session level. This matters for
  practitioners using orchestration/delegation patterns (a primary agent farming
  out subtasks to subagents) — they can now see which subagent consumed the
  budget, not just an aggregate total. For Ch04 (Cost Management): add
  per-subagent cost inspection as a debugging/optimization tool for multi-agent
  workflows — teams whose credit consumption is dominated by one expensive
  subagent step can now identify and target it directly rather than guessing
  from the aggregate session cost.

### Claim 9: Model provider extensions can now be discovered and installed directly from the VS Code Marketplace via the Language Models editor, with context size and reasoning effort adjustable from a unified picker

- **Evidence**: July 8 roundup, "Model providers from the Marketplace" section.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "Discover providers from one place: Use the Language Models editor
  to find model provider extensions." / "Install from Marketplace: Open filtered
  Marketplace results for extensions that contribute models." / "Customize models
  faster: Adjust context size and reasoning effort from a unified picker."
- **Our assessment**: This turns model-provider onboarding into an in-editor,
  Marketplace-native discovery flow rather than requiring practitioners to know
  in advance which extension to install for a given provider. Combined with the
  reasoning-effort controls already documented in
  `docs-github-copilot-vscode-may-2026.md` (Claim 10) and the 1M context window
  from `docs-github-copilot-1m-context-reasoning-levels.md`, the "unified picker"
  framing suggests GitHub has consolidated context-size and reasoning-effort
  configuration into a single UI surface rather than separate controls. For Ch02:
  document the Language Models editor + filtered Marketplace results as the
  recommended discovery path for adding non-default model providers, superseding
  any guidance that assumed manual extension search.

### Claim 10: GitHub now names the "act without checking in at every step" permission level "Autopilot," and has shipped smarter task-completion detection plus more independent agent progress for it

- **Evidence**: July 8 roundup, "Autopilot improvements" section, explicitly
  defining the term.
- **Confidence**: settled (naming and feature description stated in official
  changelog)
- **Quote**: "Autopilot, the permission level that lets agents act without
  checking in at every step, is now more hands-off and better at seeing tasks
  through." / "Better task completion: Agents are smarter about determining when
  the requested work is actually finished." / "More independent progress: Agents
  can continue working through steps with less manual steering."
- **Our assessment**: This is the first *first-party, named* documentation of
  "Autopilot" as a specific VS Code permission level in this corpus. The term had
  previously surfaced only anecdotally: `docs-github-copilot-enterprise-auto-model-default.md`
  (Claim 10) quoted a GitHub staff engineer's forum reply describing
  `disableBypassPermissionsMode` as controlling "auto-pilot" behavior, and framed
  it as informally synonymous with "bypass permissions mode" /
  `disableBypassPermissionsMode` from `docs-github-copilot-enterprise-bypass-permissions.md`.
  This July 8 changelog is the first source that names and describes Autopilot
  as a product-level permission tier in its own right, rather than a side
  reference in a forum thread. This is not a contradiction — the two sources are
  consistent (Autopilot is the user-facing name for the permission level the
  enterprise `disableBypassPermissionsMode` setting controls) — but it is a
  terminology clarification worth flagging for the guide. For Ch02 (Harness
  Engineering — Permission Levels): document "Autopilot" as the named VS Code
  permission tier for hands-off agent execution, and cross-link it explicitly
  to `disableBypassPermissionsMode` as the enterprise-side control that can
  disable it. For Ch05 (Enterprise Governance): teams that previously found
  "auto-pilot" only in a community-forum answer now have an authoritative,
  named product description to cite.

### Claim 11: A new "Gutter feedback" capability lets practitioners leave comments directly on an agent's changes from the editor gutter

- **Evidence**: July 8 roundup, "More agent workflow wins" list.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "Gutter feedback: Leave comments on an agent’s changes directly from
  the editor gutter."
- **Our assessment**: This is a distinct review surface from GitHub's existing
  Copilot code review comment UX (`docs-github-copilot-code-review-comment-ux.md`),
  which covers severity-labeled comments on *pull request* diffs from the
  automated review agent. Gutter feedback instead applies to an agent's changes
  during an active editing session, in the editor itself, before a PR necessarily
  exists. For Ch01 (Daily Workflows): document gutter feedback as the
  in-session review mechanism — distinct from and prior to PR-level review —
  for practitioners who want to comment on or flag specific agent-authored lines
  as they are produced, rather than waiting until the change reaches a pull
  request.

### Claim 12: Sessions can now generate a pull request with title and description automatically produced from the session's context ("smarter pull request creation")

- **Evidence**: July 8 roundup, "More agent workflow wins" list.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "Smarter pull request creation: Create a pull request from a session
  with the title and description generated from session context."
- **Our assessment**: This is complementary to, not the same as, the PR chat
  richer-context work documented in `docs-github-copilot-chat-pr-richer-context.md`
  — that source covers interactive chat *within* an already-open PR; this feature
  covers PR *creation* directly from a VS Code Agents-window session, using the
  session's own history (not the diff alone) as the source for the generated
  title/description. For Ch01 (Daily Workflows): document this as the default
  PR-creation path from an agent session — practitioners should review the
  generated title/description against the session's actual scope before merging,
  since accuracy of session-derived summaries is not evaluated in this source.

### Claim 13: Enterprise-managed Copilot settings can now be delivered via native OS device management on Windows and macOS, or via a JSON file for machines not enrolled in device management

- **Evidence**: July 8 roundup, "More agent workflow wins" list, two adjacent
  bullet points.
- **Confidence**: settled (product fact — stated in official changelog); emerging
  for how this interacts with the existing settings.json mechanism, which is not
  addressed in this source
- **Quote**: "Managed Copilot settings: Deliver Copilot configuration through
  native device management on Windows and macOS." / "File-based managed settings:
  Apply managed Copilot settings from a JSON file for machines that are not
  enrolled in device management."
- **Our assessment**: This adds two new delivery mechanisms to the enterprise
  Copilot governance stack documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` (the
  `.github-private/.github/copilot/settings.json` repository-based mechanism) and
  `docs-github-copilot-enterprise-strict-known-marketplaces.md` (which notes a
  "new preferred path" `copilot/managed-settings.json`). This source does not
  state whether native device-management delivery and the file-based JSON path
  use the same schema as `.github-private`/`copilot/managed-settings.json`, or
  are a parallel, MDM-specific configuration system. This is a documentation gap:
  enterprises now potentially have *three* distinct delivery paths for the same
  class of settings (source-controlled settings.json, native MDM push, local
  unenrolled-machine JSON file), and this source does not clarify precedence or
  overlap between them. For Ch02/Ch05 (Enterprise Configuration): flag this gap
  explicitly — document all three mechanisms side by side and recommend teams
  verify with GitHub's enterprise documentation which one is authoritative when
  more than one could apply to the same machine.

### Claim 14: MCP OAuth credentials can now be configured with preregistered OAuth client IDs, with client secrets held in VS Code's secret storage rather than in project or user configuration files

- **Evidence**: July 8 roundup, "More agent workflow wins" list.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "MCP OAuth credentials: Configure preregistered OAuth client IDs and
  keep client secrets in VS Code secret storage."
- **Our assessment**: This is the first documented MCP-specific credential-handling
  mechanism for GitHub Copilot in this corpus, though it corroborates the general
  MCP-as-auth-boundary thesis from `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`
  (Claim 2: MCP can enable "a trust boundary where harness code does not handle
  credentials at all"). Storing client secrets in VS Code's OS-level secret
  storage, rather than in a settings file or `.vscode/mcp.json`-style config,
  keeps the secret out of any file that might be committed, synced, or read by
  an agent's file-reading tools. For Ch02 (Harness Engineering — MCP
  Configuration): document VS Code secret storage as the recommended location
  for MCP OAuth client secrets, and flag "preregistered client IDs" as implying
  admins or developers must register the OAuth client with the MCP server's
  identity provider ahead of time — the specific registration flow is not
  described in this source.

### Claim 15: VS Code now applies a two-hour delay before automatically installing newly published extension versions, and Workspace Trust now lets users browse a new folder safely before deciding whether to trust it

- **Evidence**: July 8 roundup, "More agent workflow wins" list, final two items.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "Extension auto-update delay: A two-hour delay is applied before
  automatically installing newly published extension versions, giving teams a
  safety buffer." / "Workspace Trust improvements: Browse new folders safely
  first, then trust the folder when ready."
- **Our assessment**: Both are supply-chain/trust hardening measures. The
  two-hour extension delay is a specific, quantified mitigation against
  just-published (potentially compromised or buggy) extension versions reaching
  users instantly — it gives GitHub/Microsoft or the community a narrow window to
  catch and pull a bad release before broad auto-update rollout. The Workspace
  Trust change lowers the friction of the existing trust-then-browse model to a
  browse-then-trust model, letting a developer inspect an unfamiliar folder
  (e.g., a cloned repository of unknown provenance) before granting it the
  elevated permissions that trusted-workspace status confers. Neither mechanism
  is evaluated for effectiveness in this source. For Ch07 (Security): add the
  two-hour extension delay as a concrete, named supply-chain control comparable
  to `strictKnownMarketplaces` (`docs-github-copilot-enterprise-strict-known-marketplaces.md`)
  — both restrict what untrusted code can reach a developer's environment,
  one for Copilot plugin marketplaces, one for all VS Code extensions generally.
  Document the Workspace Trust browse-first change as a lower-friction path to
  safely evaluating unfamiliar repositories before an agent (or the editor itself)
  is granted trusted-workspace capabilities.

## Concrete Artifacts

### Browser Tools Trust Model (VS Code, GA as of July 1, 2026)

```
GitHub Copilot Integrated Browser — Trust and Isolation Model

USER-OPENED TABS:
  Default:     Private — agent cannot read or interact
  Grant:       "Share with Agent" (explicit, per-tab)
  Revocation:  "at any time"

AGENT-OPENED TABS:
  Session:     Fresh session, no cookies/storage from user's regular browsing
  Concurrency: Parallel agents (Agents window) keep tabs private from each other

SENSITIVE PERMISSIONS (never auto-granted):
  - Camera
  - Microphone
  - Location
  - Notifications
  - Clipboard reads
  Each requires explicit per-site human approval; agents cannot self-approve.

LOW-RISK DEFAULT-ALLOWED:
  - Sanitized clipboard writes (mechanism for "sanitized" not specified)

ENTERPRISE CONTROLS:
  workbench.browser.enableChatTools       — dedicated on/off switch
  chat.agent.allowedNetworkDomains        — allow-list (wildcards supported)
  chat.agent.deniedNetworkDomains         — deny-list (wildcards supported,
                                             takes precedence over allow-list)
  chat.agent.networkFilter                — enables the above filters
  Workspace Trust and approval prompts    — still apply on top of the above
```

Source: github.blog changelogs, July 1 and July 8, 2026, both retrieved 2026-07-10.

### June–July 2026 "Also New" Feature List (VS Code v1.123–v1.127)

```
GitHub Copilot in VS Code — "More agent workflow wins" (July 8, 2026 roundup)

Session sync and chronicle    — sync sessions to GitHub account; cross-machine
                                 coding history search (corroborates May 2026
                                 roundup Claims 5–6)
Gutter feedback                — comment on agent's changes from editor gutter
Smarter pull request creation  — PR title/description generated from session context
1M context windows              — compatible Anthropic and OpenAI models
Model hover cards               — quick model descriptor + jump to configuration
Official Ollama extension       — replaces built-in Ollama provider
Managed Copilot settings        — native device management (Windows/macOS)
File-based managed settings     — JSON file for non-device-managed machines
MCP OAuth credentials           — preregistered client IDs; secrets in VS Code
                                   secret storage
Extension auto-update delay     — 2-hour delay before auto-installing new
                                   extension versions
Workspace Trust improvements     — browse new folder safely, then trust
```

Source: github.blog changelog, July 8, 2026, retrieved 2026-07-10.

## Cross-References

- **Corroborates** `docs-github-copilot-vscode-may-2026.md` (Claims 5–6): That
  source documented session sync to GitHub account and Chronicle
  (`/chronicle` commands for standup reports and productivity tips) as May 2026
  features. This July source's "Session sync and chronicle" bullet confirms both
  capabilities remain current and are still part of the "More agent workflow
  wins" feature set two months later — no material change described.

- **Corroborates** `docs-github-copilot-1m-context-reasoning-levels.md` (Claim 1):
  That source documented 1M-token context windows landing in VS Code, the Copilot
  CLI, and the GitHub Copilot app on June 4, 2026. This July 8 source's "1M
  context windows" bullet ("Work with compatible Anthropic and OpenAI models
  using much larger context windows for bigger codebases and longer
  conversations") reconfirms the VS Code availability; no new surfaces or model
  names are added here.

- **Extends** `docs-github-copilot-vscode-may-2026.md` (Claim 11, terminal
  credential isolation) and adds a second, browser-side instance of the same
  agent/human data-isolation pattern: Claims 2–4 of this note establish that
  browser tab access and sensitive browser permissions are likewise gated from
  the agent by default, extending the "credentials/sensitive data isolated from
  the LLM by design" pattern from the terminal into the browser surface.

- **Extends** `docs-github-copilot-vscode-may-2026.md` (Claim 7, concurrent
  sessions) with Claim 7 of this note: May 2026 documented session-level
  parallelism ("Open more than one agent session at the same time"); this source
  adds a finer-grained layer — multiple *chats* within a single session — that
  did not exist in the May feature set.

- **Extends** `docs-github-copilot-enterprise-managed-plugins-vscode.md` and
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`: those sources
  documented the `.github-private/.github/copilot/settings.json` /
  `copilot/managed-settings.json` enterprise-managed settings system with plugin
  distribution, hooks/MCP governance, bypass-permission controls, and marketplace
  restriction. Claim 13 of this note adds two more delivery mechanisms (native
  OS device management; file-based JSON for non-enrolled machines) to the same
  governance space, without clarifying how they relate to the existing
  settings.json path — flagged as an open documentation gap.

- **Extends** `docs-github-copilot-enterprise-bypass-permissions.md` and
  `docs-github-copilot-enterprise-auto-model-default.md` (Claim 10): those
  sources documented `disableBypassPermissionsMode` and a single anecdotal forum
  reference to "auto-pilot" behavior. Claim 10 of this note is the first
  official, named, first-party description of "Autopilot" as a VS Code
  permission level — clarifying (not contradicting) the terminology those two
  enterprise-settings notes used informally.

- **Extends** `docs-github-copilot-code-review-comment-ux.md`: that source
  documented severity-labeled, grouped comments on Copilot's own automated PR
  code review. Claim 11 of this note (gutter feedback) documents a distinct
  review surface — human comments on agent-authored changes during an editing
  session, before a PR exists.

- **Complements** `docs-github-copilot-chat-pr-richer-context.md`: that source
  documented interactive Copilot chat inside an already-open PR (GA as of June
  4). Claim 12 of this note (smarter PR creation) documents the preceding step —
  generating the PR itself, with title/description drawn from session context.

- **Corroborates** `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` (Claim 2):
  that source's thesis that MCP's core value is isolating auth flows so "harness
  code does not handle credentials at all." Claim 14 of this note (MCP OAuth
  client secrets held in VS Code secret storage, not in config files) is a
  concrete GitHub Copilot implementation of that same auth-isolation principle.

- **Extends** `docs-github-copilot-enterprise-strict-known-marketplaces.md`
  (supply-chain framing): that source framed `strictKnownMarketplaces` as
  operating "prior to tool execution" to prevent installation of untrusted
  Copilot plugins. Claim 15 of this note (two-hour extension auto-update delay)
  is a parallel supply-chain control at the general VS Code extension level
  rather than the Copilot-plugin-marketplace level.

- **Novel**:
  - First official, named documentation of "Autopilot" as a VS Code Copilot
    permission level (Claim 10) — previously only referenced anecdotally via a
    GitHub staff forum reply in `docs-github-copilot-enterprise-auto-model-default.md`.
  - First documented per-subagent credit-usage inspection within a delegated
    agent workflow (Claim 8) — prior cost-visibility notes covered session- or
    request-level cost only.
  - First documented explicit browser tab trust model for a GitHub Copilot
    surface: private-by-default user tabs with revocable per-tab sharing, and
    isolated fresh-session tabs for agent-initiated browsing (Claims 2–3).
  - First documented MCP OAuth credential mechanism specific to GitHub Copilot,
    with client secrets stored in VS Code's OS-level secret storage (Claim 14).
  - First documented quantified extension supply-chain delay (two hours) for
    VS Code generally, distinct from the Copilot-specific `strictKnownMarketplaces`
    control (Claim 15).
  - First documentation of "multiple chats in one session" as a sub-session
    parallelism layer, distinct from the session-level parallelism already
    documented in May 2026 (Claim 7).

## Guide Impact

### Chapter 02: Harness Engineering — IDE Configuration and Safety

- **Browser-agent trust model**: Add the private-by-default / Share-with-Agent /
  isolated-agent-tabs model (Claims 1–4) as the documented default security
  posture for VS Code's now-GA browser tools. Pair with the existing terminal
  credential-isolation guarantee (`docs-github-copilot-vscode-may-2026.md` Claim
  11) as the guide's two concrete "what the agent cannot see by default" examples.
- **Enterprise browser governance**: Document `workbench.browser.enableChatTools`
  and the `chat.agent.*NetworkDomains`/`networkFilter` settings (Claim 5) as VS
  Code workspace/user-setting-level controls, distinct from the
  `.github-private`-based enterprise-managed settings system.
- **"Autopilot" naming**: Update any guide text that referred to the hands-off
  permission level only via `disableBypassPermissionsMode` or informal
  "auto-pilot" forum language — this changelog is now the authoritative,
  citable name and description (Claim 10).
- **MCP OAuth credential handling**: Document VS Code secret storage as the
  recommended location for MCP OAuth client secrets (Claim 14), reinforcing the
  broader "credentials should live outside agent-readable files" principle.
- **Enterprise settings delivery gap**: Flag the three parallel delivery
  mechanisms for enterprise Copilot settings (repository settings.json, native
  device management, file-based JSON for unenrolled machines — Claim 13) as an
  open question for teams to resolve with GitHub's own documentation before
  guide language asserts a single canonical mechanism.

### Chapter 04: Agentic Workflows — Multi-Session and Cost Optimization

- **Sub-session parallelism**: Document "multiple chats in one session" (Claim
  7) as a finer-grained parallelism layer beneath session-level parallelism,
  useful for splitting implementation/review/testing/docs within one logical
  task.
- **Per-subagent cost inspection**: Add subagent-level credit visibility (Claim
  8) as a debugging tool for multi-agent delegation workflows — teams can now
  identify which subagent step is driving cost rather than relying on aggregate
  session totals.
- **PR-creation-from-session**: Document "smarter pull request creation" (Claim
  12) as the default PR-generation path from an Agents-window session, with the
  caveat that generated titles/descriptions should be reviewed against actual
  session scope.

### Chapter 05: Team Adoption — Enterprise Governance and Safety

- **Browser tools kill switch and domain filtering**: Recommend
  `workbench.browser.enableChatTools` and the network domain allow/deny lists
  (Claim 5) as the concrete controls for teams evaluating whether to enable
  agentic browser tools org-wide.
- **Two governance-delivery mechanisms need reconciling**: Advise teams
  evaluating enterprise Copilot governance to check which of the three delivery
  paths (Claim 13) their organization's admins are actually using before
  assuming a single settings.json is authoritative.

### Chapter 07: Security

- **Extension supply-chain delay**: Add the two-hour extension auto-update
  delay (Claim 15) as a general VS Code supply-chain control, alongside the
  Copilot-specific `strictKnownMarketplaces` allowlist
  (`docs-github-copilot-enterprise-strict-known-marketplaces.md`).
- **Workspace Trust browse-first**: Document the browse-then-trust flow (Claim
  15) as a lower-friction way to safely inspect unfamiliar repositories before
  granting trusted-workspace capabilities to the editor or its agents.

## Extraction Notes

1. **Two sources fetched, one raw-HTML-verified**: The primary source
   (July 8 roundup) was retrieved twice — once via WebFetch (AI-summarized) and
   once via direct `curl` of the raw HTML, which was then parsed to plain text.
   All quotes in this note are taken from the raw-HTML-derived plain text
   (`article_text.txt`), not from the WebFetch summary, to guarantee
   character-for-character accuracy. The July 1 companion GA changelog
   (linked from the roundup's "Agentic browser tools are now generally
   available" bullet) was likewise fetched via raw `curl` and parsed the same
   way, per MINER.md §1's instruction to follow substantive linked pages.

2. **WebFetch summary discarded in favor of raw HTML**: An initial WebFetch call
   to the roundup URL returned a summarized version with some paraphrased
   headings (e.g., "Enhanced Workspace Trust browsing" vs. the source's actual
   "Workspace Trust improvements: Browse new folders safely first, then trust
   the folder when ready"). All claims and quotes in this note were rewritten
   against the verbatim raw-HTML text to avoid citing paraphrased wording as a
   direct quote, per MINER.md §2a.

3. **"Also new" list — ten items, six extracted as full claims**: Of the ten
   one-line "More agent workflow wins" items, four (session sync/chronicle, 1M
   context windows, model hover cards, Official Ollama extension) were judged to
   have minimal independent guide impact beyond what existing corpus notes
   already cover, or too little source detail to extract meaningfully beyond a
   one-line mention (model hover cards, Ollama extension). These four are listed
   in the Concrete Artifacts feature list for corpus completeness but were not
   given dedicated Claim entries. The remaining six (gutter feedback, PR
   creation, managed settings delivery, MCP OAuth, extension delay, Workspace
   Trust) received full claims because each introduces a new, guide-relevant
   configuration surface or governance mechanism.

4. **No contradictions identified**: Cross-referencing against the May 2026 VS
   Code roundup, the enterprise-managed-settings notes, the 1M-context note, the
   PR-chat note, the code-review comment-UX note, and the MCP auth-gateway note
   found no claims in this source that oppose an existing corpus position. The
   "Autopilot" naming (Claim 10) clarifies rather than contradicts the informal
   "auto-pilot" forum reference in `docs-github-copilot-enterprise-auto-model-default.md`
   — both describe the same underlying permission level from different vantage
   points (product naming vs. a support-forum troubleshooting reply). No
   contradiction issue filed.

5. **Documentation gap flagged, not resolved**: Claim 13 identifies a real gap —
   this source does not state whether native device-management delivery and the
   file-based JSON path share a schema with the existing
   `.github-private`/`copilot/managed-settings.json` mechanism, or how conflicts
   between multiple applicable delivery mechanisms are resolved. This was
   deliberately left as an open question in Guide Impact rather than resolved
   with speculation, since no source in the corpus (including this one) answers
   it.

6. **Sub-pages beyond the browser GA article were not followed**: The roundup
   links to five VS Code version release-notes pages (1.123–1.127) at the very
   end ("For the full details, browse the complete release notes across these
   versions"). These were not fetched — they are full version release notes
   (typically thousands of lines covering all VS Code changes, not just
   Copilot), and the roundup plus the one substantive Copilot-specific linked
   article (browser tools GA) were judged sufficient to cover the Copilot-relevant
   content per the Prospector's triage guidance. This is noted per MINER.md's
   "follow up to 5 linked pages that seem substantive" — the version release
   notes were judged not substantive specifically for Copilot extraction
   purposes, as distinct from the browser GA page which was Copilot-specific
   and directly expanded on a claim in the primary source.
