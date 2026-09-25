---
source_url: https://github.blog/changelog/2026-09-23-local-sandboxing-in-the-github-copilot-app
source_type: docs
title: "Local sandboxing in the GitHub Copilot app"
author: GitHub (official changelog)
date_published: 2026-09-23
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: emerging
issue: "#3689"
---

# Local Sandboxing in the GitHub Copilot App

> GitHub's September 23, 2026 changelog adds per-project local sandboxing to the
> GitHub Copilot app — OS-level restriction of filesystem, network, and credential
> access for agent-run tools, off by default, fail-closed when the OS cannot
> enforce the requested policy, and explicitly separate from cloud/remote-host
> sandboxing and from Copilot CLI's own sandbox settings. A same-day cross-check of
> the enterprise `managed-settings.json` reference page confirms the `sandbox` key's
> "GitHub Copilot app" column now reads "Supported" and its prose now names the app
> explicitly — a change from the "Not supported" state the Sept 8, 2026 JetBrains
> enterprise-sandbox note recorded for that exact cell two weeks earlier.

## Source Context

- **Type**: docs (GitHub official product changelog, September 23, 2026; ~1-minute
  read, tagged `copilot`). One linked page was followed per MINER.md §1: "Configuring
  local sandboxing in the GitHub Copilot app"
  (resolved from the changelog's `https://gh.io/github-app-local-sandboxing` shortlink
  to `docs.github.com/en/copilot/how-tos/github-copilot-app/configure-local-sandboxing`),
  which supplied the full policy-configuration mechanics. A second page not linked from
  the changelog — the "Enterprise managed settings reference"
  (`docs.github.com/copilot/reference/enterprise-managed-settings-reference`), the same
  reference page relied on by five prior corpus notes in the enterprise-managed-settings
  family — was independently fetched to check whether the `sandbox` key's per-client
  support matrix reflects this changelog's claim, following the pattern established in
  `docs-github-copilot-app-opentelemetry.md` and
  `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`. All three pages
  were fetched as raw HTML/JSON (`curl` + parsing the docs pages' embedded
  `__NEXT_DATA__` payload) rather than via a summarizing WebFetch pass, per MINER.md §2a.
- **Author credibility**: GitHub engineering team announcing a production feature for
  the GitHub Copilot app client. Authoritative for: the existence and stated behavior of
  the per-project sandbox policy, the three configurable dimensions (filesystem, network,
  credentials), the off-by-default and fail-closed behavior, and the public-preview
  status. The linked configuration how-to and the enterprise reference page are the same
  first-party documentation family and are treated with equal authority for the
  additional mechanics they supply (bypass-prompt UX, OS-specific enforcement gaps, the
  managed-settings `sandbox` schema).
- **Scope**: The GitHub Copilot app's new per-project local sandbox feature — what it
  restricts, how to turn it on, the three configuration dimensions, the fail-closed
  enforcement guarantee, and its explicit non-coverage of cloud/remote sessions. The
  linked how-to page adds: default filesystem grants, denied-path precedence rules,
  OS-specific enforcement gaps (Windows, Linux), the `/sandbox on`/`/sandbox off`/
  `/restart-session` commands, and the "Run outside the sandbox?" bypass-prompt UX. The
  reference page adds: the full enterprise-managed `sandbox` key schema and confirms the
  app is now a supported client for that key. Does NOT cover: macOS Keychain/Seatbelt
  specifics for the app (the reference page's `userPolicy.seatbelt` sub-property is named
  but not elaborated for the app specifically), the "About cloud and local sandboxes for
  GitHub Copilot" concept page it links to for a cloud-vs-local overview (not fetched —
  see Extraction Notes), or any adoption/rollout data.

## Extracted Claims

### Claim 1: Local sandboxing in the GitHub Copilot app runs the tools an agent invokes inside an OS-level sandbox, reducing the potential impact of an unintended command by limiting access to files, network resources, and credentials

- **Evidence**: Changelog opening paragraph; restated near-verbatim in the linked
  "Configuring local sandboxing" how-to page's "About local sandboxing" section.
- **Confidence**: settled (stated identically across two first-party pages)
- **Quote (changelog)**: "Local sandboxing helps reduce the potential impact of unintended commands by limiting access to files, network resources, and credentials on your machine."
- **Quote (how-to page)**: "Local sandboxing runs the tools that an agent invokes on your behalf inside an operating-system sandbox. This reduces the potential impact of an unintended command by limiting access to files, network resources, and credentials on your machine."
- **Our assessment**: This is the headline threat-model claim: sandboxing targets the
  blast radius of an *unintended* command (whether from a bug, a misinterpreted
  instruction, or prompt injection), not just malicious input specifically. The how-to
  page's added framing — "the tools that an agent invokes on your behalf" — makes clear
  this wraps tool execution, not the model call itself. It directly answers the
  Prospector's triage question about concrete mechanisms: the three enforcement surfaces
  are filesystem, network, and credentials (elaborated in Claim 2), matching the
  "filesystem/network/credential isolation" framing the triage comment asked about.

### Claim 2: A project's sandbox policy is configured along three dimensions — filesystem (additional read/write, additional read-only, denied folder lists), network (outbound internet, local network), and credentials (Git HTTPS auth, GitHub CLI auth)

- **Evidence**: Changelog's bulleted "sandbox settings" list; the how-to page repeats
  and elaborates each dimension in its own subsection.
- **Confidence**: settled (identical three-dimension structure in both pages)
- **Quote**: "Filesystem: Additional read/write, additional read-only, and denied folder lists. Network: Outbound internet and local network settings. Credentials: Git credentials for authenticated HTTPS git operations, and GitHub CLI credentials for GitHub CLI authentication."
- **Our assessment**: This three-dimension model — filesystem, network, credentials —
  is structurally the same shape as the AWF sandbox model documented in
  `docs-ghaw-sandbox-reference.md` (Claims 4 and 7: a three-tier filesystem model plus
  environment-variable/credential handling) and the Copilot CLI `/sandbox` interface
  documented in `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`
  (Concrete Artifacts: General/Auth/Filesystem/Network tabs). Different products, same
  three-axis threat model: what files can be touched, what network can be reached, what
  identity can be assumed. This is corroborating evidence that "filesystem + network +
  credentials" is GitHub's (and, more broadly, the industry's) standard decomposition
  for agent sandbox policy, not an app-specific design choice.

### Claim 3: Local sandboxing is off by default; enabling it for a project is done via app settings → select project → toggle "Sandbox new sessions" under "Sandbox," and the change applies only to new sessions, not ones already running

- **Evidence**: Changelog "Get started" section; how-to page "Enabling local sandboxing
  in a project" section, word-for-word consistent.
- **Confidence**: settled (identical instructions on both pages)
- **Quote**: "Local sandboxing is off by default. Open the app settings, select your project, and turn on Sandbox new sessions under "Sandbox". This applies to new sessions in the project, not sessions already running."
- **Our assessment**: The opt-in default is notable given the fail-closed guarantee in
  Claim 6 — GitHub is not shipping this sandboxed-by-default, but once enabled, the
  enforcement is strict (fail rather than silently degrade). The how-to page adds a
  practical recommendation not in the changelog: "For most projects, start with the
  default policy. It allows common development tasks such as installing dependencies,
  connecting to a local development server, pushing a branch, and creating a pull
  request. Add restrictions when the project is next to sensitive folders, does not need
  network access, or should not use your credentials." This is concrete, actionable
  guidance for a harness engineer deciding when to layer on restrictions beyond the
  default policy.

### Claim 4: Sandboxing can be toggled for an already-active local session via the `/sandbox on` (or `/sandbox off`) slash command, which creates a session-scoped override without changing the project's default

- **Evidence**: Changelog "Get started" section; how-to page "Changing sandboxing for a
  session" section, which adds the `/sandbox off` counterpart and override semantics not
  in the changelog.
- **Confidence**: settled (changelog states `/sandbox on`; how-to page corroborates and
  extends with `/sandbox off` and override scoping)
- **Quote (changelog)**: "To enable sandboxing for an active local session, enter /sandbox on. This changes that session without changing the project default."
- **Quote (how-to page)**: "During an active local session, the command creates a persistent override for that session and applies it immediately. The override does not change the project default for other sessions. If you enter either command before a session starts, the command changes the project default inherited by new sessions."
- **Our assessment**: The distinction between a session-scoped override (mid-session)
  and a project-default change (pre-session) is a precise, practically important
  behavior the changelog alone does not fully specify — the how-to page is required to
  understand that the *same* `/sandbox on`/`off` command has different scope depending on
  when it's issued. A harness engineer scripting or documenting sandbox usage needs this
  timing distinction to predict what a given command will actually do.

### Claim 5: Local sandboxing does not apply to cloud sandbox sessions or sessions running on a remote host, and the GitHub Copilot app's sandbox settings are configured separately from Copilot CLI's sandbox settings

- **Evidence**: Changelog closing paragraph before the public-preview note; how-to page
  "About local sandboxing" section states the same scope limit and adds the
  working-tree-vs-sandbox distinction.
- **Confidence**: settled (stated identically in both pages)
- **Quote (changelog)**: "Local sandboxing does not apply to cloud sandbox sessions or sessions running on a remote host. GitHub Copilot app and Copilot CLI sandbox settings are configured separately."
- **Quote (how-to page)**: "A working tree keeps the branches and files for concurrent sessions separate, but it does not restrict what a command can access elsewhere on your machine. Local sandboxing provides that additional protection."
- **Our assessment**: This is an important scope caveat for the guide: "local" is doing
  real work in the feature name — it is specifically the *local* repository/working-tree
  session mode that gets this OS-level protection, not cloud-hosted or remote-host agent
  sessions, which presumably have their own (different) isolation model. The explicit
  "configured separately" from Copilot CLI confirms these are two independent policy
  surfaces even though (per Claim 2) they share the same three-dimension structure — a
  practitioner who configures CLI sandboxing does not thereby configure app sandboxing,
  and vice versa. The working-tree clarification is a useful corrective: a git worktree's
  file/branch isolation is not a security boundary, only a workspace-organization one;
  sandboxing is the actual access-control layer.

### Claim 6: If the operating system cannot enforce the requested sandbox policy, the sandboxed shell fails with an error rather than running the command without a sandbox — the app does not silently degrade to unsandboxed execution

- **Evidence**: Changelog's dedicated sentence, set apart from the feature description;
  the how-to page restates this as part of "Applying policy changes" with additional
  mechanism detail (the check happens at first-shell-start, not at settings-save time).
- **Confidence**: settled (identical guarantee stated in both pages, with the how-to page
  adding when the check occurs)
- **Quote (changelog)**: "If your operating system cannot enforce the requested policy, the sandboxed shell fails with an error rather than running without a sandbox."
- **Quote (how-to page)**: "The app accepts sandbox settings before checking whether your operating system can enforce them. Support is checked when the first sandboxed shell starts. If the host cannot enforce the requested policy, the shell fails with an unsupported-platform or unsupported-policy message and does not run unsandboxed."
- **Our assessment**: This is the single highest-value security claim in the source and
  directly addresses the Prospector's triage question ("explicit requirement that OS
  enforce policy or fail safe — no degraded sandbox"). Fail-closed-on-unenforceable-policy
  is the correct security posture: a weaker alternative design (silently run unsandboxed
  if the OS can't comply) would be a dangerous default because a practitioner who
  believes their policy is active would have no signal that it silently wasn't. The
  how-to page's addition — that settings are *accepted* before enforceability is
  *checked*, and the check happens lazily at first-shell-start — is an operational detail
  worth flagging: a practitioner can save an unenforceable policy without immediate
  feedback and only discover the failure when a sandboxed command actually runs. For
  Ch06 (Security Threat Model): this fail-closed guarantee is the concrete mechanism that
  answers "does the sandbox degrade gracefully or fail safely" — it fails safely, with the
  caveat that the failure is deferred to first use, not policy-save time.

### Claim 7: Local sandboxing in the GitHub Copilot app is in public preview and subject to change

- **Evidence**: Changelog's standalone closing sentence before the "Learn more" link;
  how-to page opens with an identical note.
- **Confidence**: emerging (explicitly labeled public preview by the source itself)
- **Quote**: "Local sandboxing is in public preview and subject to change."
- **Our assessment**: Consistent with the preview labeling pattern for every other
  sandboxing-related feature in this corpus family
  (`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` Claim 4,
  `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md` Claim 1) — GitHub
  has shipped local sandboxing to JetBrains, the app, and (implicitly, given the reference
  page's existing "Supported" mark) Copilot CLI, all under public-preview labeling before
  any of them reached GA. This is the reason `confidence_overall` for this note is set to
  `emerging` rather than `settled`: the underlying capability is real and consistently
  described, but the source itself flags it as not yet stable.

### Claim 8: By default, a sandboxed session has read/write access to its workspace and current working directory; administrators/users can grant additional read-only or read/write folders, or deny specific folders, and a more-specific denied folder remains denied even when a broader parent folder has read or write access

- **Evidence**: How-to page "Configuring filesystem access" section.
- **Confidence**: settled (first-party how-to documentation, direct quote)
- **Quote**: "By default, a sandboxed session has read/write access to its workspace and current working directory." / "A more-specific denied folder remains denied when a broader parent folder has read or write access."
- **Our assessment**: The denied-folder precedence rule is a specific, testable policy
  semantic not mentioned in the changelog at all — it only appears in the linked how-to
  page, which is why following that link (per MINER.md §1) was necessary rather than
  relying on the changelog alone. This "most restrictive wins" precedence for filesystem
  rules is the same direction of precedence GitHub uses for the enterprise `sandbox` key's
  `deniedPaths` sub-property (Claim 11: "a managed value adds to, rather than replaces, a
  user's denied paths") — denial is additive/sticky at both the per-project-policy layer
  and the enterprise-managed layer, a consistent "deny wins" design across the whole
  sandbox stack.

### Claim 9: OS-specific enforcement gaps exist and are handled by fail-closed behavior rather than silent policy weakening — on Windows, a denied path that the active sandbox capabilities cannot guarantee causes the sandboxed command to fail with an unsupported-policy message; on Linux, the sandbox cannot independently control local network access for spawned processes such as shell commands and local MCP/LSP servers, though it still applies to in-process operations like web requests and remote MCP connections

- **Evidence**: How-to page "Configuring filesystem access" section (Windows) and
  "Configuring network access" section (Linux).
- **Confidence**: settled (first-party how-to documentation, direct quotes)
- **Quote (Windows)**: "On Windows, you can save a denied path in the project settings. If the active Windows sandbox capabilities cannot guarantee the denial, a sandboxed command fails with an unsupported-policy message. The command does not run with the denied path accessible or without a sandbox."
- **Quote (Linux)**: "On Linux, the sandbox cannot control local network access independently for spawned processes, such as shell commands and local MCP or LSP servers. The setting still applies to in-process operations, such as web requests and remote MCP connections."
- **Our assessment**: These are the two most concrete, platform-specific limitations in
  the source and are exactly the kind of detail a harness engineer needs before trusting
  the sandbox for a specific OS. The Windows case is a direct instance of the general
  fail-closed guarantee from Claim 6 applied to a specific sub-policy (denied paths). The
  Linux case is different in kind: it is not a fail-closed situation but a *documented
  gap in enforcement scope* — local network access for spawned child processes (shell
  commands, local MCP/LSP servers) is not independently controllable on Linux, only
  in-process network calls are governed by the network setting. This means a Linux user
  who denies local network access and then runs a shell command that itself makes a local
  network call is not protected by this setting for that call — a materially different
  and weaker guarantee than the Windows filesystem case, and the guide should not
  conflate the two as equivalent "the sandbox enforces this" claims. This is the most
  important limitation for Ch06 to flag explicitly rather than generalize away.

### Claim 10: When a tool needs access the sandbox policy does not allow, the app can display a "Run outside the sandbox?" prompt offering three choices — cancel, run once outside the sandbox, or disable sandboxing for the rest of the session — and an enterprise owner can prevent users from running tools outside the sandbox at all

- **Evidence**: How-to page "Running a tool outside the sandbox" section.
- **Confidence**: settled (first-party how-to documentation, direct quote)
- **Quote**: "If a tool needs access that the sandbox policy does not allow, the app can display a Run outside the sandbox? prompt. Depending on the effective policy, you can: Cancel the operation. Run the operation once outside the sandbox. Disable sandboxing for the remainder of the current session and run the operation. ... An enterprise owner can prevent users from running tools outside the sandbox. For more information, see Enterprise managed settings."
- **Our assessment**: This bypass-prompt mechanism is the practitioner-facing analog of
  the enterprise `sandbox.allowBypass` sub-property confirmed in Claim 11's schema (a
  managed `false` value "prevents individual commands from running outside the sandbox
  and prevents users from disabling sandboxing... from an active sandbox-bypass
  permission prompt"). This is the same governance pattern documented for permission
  prompts generally in `docs-github-copilot-enterprise-bypass-permissions.md`
  (`disableBypassPermissionsMode`): a user-facing escape hatch exists by default, and
  enterprises can lock it. The three-option structure (cancel / run-once / disable-for-
  session) gives granular control — a user is not forced into an all-or-nothing choice
  when a single blocked operation is a false positive.

### Claim 11: The enterprise-managed `sandbox` settings key now explicitly names the GitHub Copilot app in its reference-page prose ("Enforces minimum local sandbox restrictions for Copilot CLI and the GitHub Copilot app") and the per-client support table's "GitHub Copilot app" column reads "Supported" as of this extraction — a change from "Not supported" recorded for that same cell two weeks earlier

- **Evidence**: `docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
  fetched as raw HTML/`__NEXT_DATA__` JSON on 2026-09-25 (two days after this
  changelog's publication). The "Supported keys" table's `sandbox` row shows: Copilot
  CLI = Supported, VS Code = Not supported, GitHub Copilot app = **Supported**, Copilot
  cloud agent = Not supported, JetBrains IDEs = Not supported. The `sandbox` key's prose
  subsection opens with the app named explicitly.
- **Confidence**: settled (first-party reference documentation; the specific table cell
  and prose sentence are read directly from the page's rendered HAST/HTML, not
  summarized)
- **Quote (prose)**: "Enforces minimum local sandbox restrictions for Copilot CLI and the GitHub Copilot app."
- **Quote (app-specific enforcement note)**: "In app sessions, the embedded runtime parses, combines, and enforces the complete managed sandbox object, including properties that are not available in the app's project settings. The app displays the user's project settings, not the complete effective managed policy, and does not show per-setting managed locks."
- **Our assessment**: This is a genuine, verifiable corroboration rather than a
  contradiction — and it stands in useful contrast to the two other sandbox/telemetry
  discrepancies already logged against this exact reference page
  (`docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`'s issue #3334
  for the JetBrains `sandbox` column, and `docs-github-copilot-app-opentelemetry.md`'s
  issue #3682 for the Copilot-app `telemetry` column). The Sept 8, 2026 JetBrains-sandbox
  note recorded, from a Sept 9 fetch of this identical table, "GitHub Copilot app" as
  **Not supported** for the `sandbox` key. As of this extraction's Sept 25 fetch (two
  days after this changelog's Sept 23 publication), that same cell reads **Supported**,
  and the prose section has been updated to name the app explicitly — the reference page
  caught up to a changelog announcement within the two-week window, which is exactly the
  documentation-lag pattern the two open contradiction issues hypothesize but had not yet
  observed resolving. This does not resolve #3334 or #3682 (those concern the JetBrains
  and Copilot-app *columns for different keys* — `sandbox`/JetBrains and
  `telemetry`/Copilot-app, respectively), but it is the first corpus evidence that the
  lag pattern does self-correct, which is worth noting for the Assayer/Smith as context
  when evaluating those still-open issues. The "app displays project settings, not the
  complete effective managed policy" sentence is also a notable governance/UX gap worth
  flagging on its own: an app user inspecting their project's sandbox settings screen
  cannot see the full effective policy if enterprise-managed properties not exposed in
  the project-settings UI are also in force.

### Claim 12: The enterprise-managed `sandbox` key's schema includes an `enabled` sub-property whose `true` value cannot be overridden by the app's project setting or the `/sandbox off` command, and a `failIfUnavailable` sub-property that, combined with `enabled: true`, blocks model and tool execution entirely rather than allowing commands to run unsandboxed if the sandbox backend cannot be validated

- **Evidence**: Reference page `sandbox` key sub-property list, fetched 2026-09-25.
- **Confidence**: settled (first-party reference documentation, direct quotes)
- **Quote (`enabled`)**: "enabled: true requires sandboxing by default. Users cannot disable it through their configuration. In Copilot CLI, the --no-sandbox command line option and /sandbox disable command cannot override it. In the GitHub Copilot app, the project setting and /sandbox off command cannot override it. If the effective policy permits bypass, a user can still explicitly disable sandboxing for the rest of the current session from an active sandbox-bypass permission prompt."
- **Quote (`failIfUnavailable`)**: "failIfUnavailable: true, combined with enabled: true, makes the managed sandbox mandatory. If Copilot cannot validate, compile, or enforce the sandbox policy with an available sandbox backend, it blocks model and tool execution instead of allowing commands to fail or run unsandboxed. This property does not enable sandboxing by itself."
- **Our assessment**: This is the enterprise-governed escalation of the project-level
  fail-closed guarantee in Claim 6. At the project-policy level, an unenforceable policy
  fails the *specific sandboxed shell* (a narrow, per-command failure). At the
  enterprise-managed level with `failIfUnavailable: true`, an unenforceable sandbox
  backend blocks *model and tool execution entirely* — a much broader failure mode that
  stops the agent session rather than just one command. This is a meaningful distinction
  for Ch06: the guide should describe two tiers of fail-closed behavior (per-command vs.
  whole-session) depending on whether the mandatory-sandbox enterprise property is set,
  not a single undifferentiated "fails safely" claim. The `enabled` sub-property's
  bypass-prompt carve-out ("a user can still explicitly disable sandboxing... from an
  active sandbox-bypass permission prompt" unless `allowBypass: false` is also set,
  per Claim 10) shows these two enterprise properties (`enabled`, `allowBypass`) compose
  — mandatory sandboxing and bypass-prevention are independently configurable, so an
  enterprise wanting a true no-escape-hatch policy must set both.

## Concrete Artifacts

### Full changelog body (verbatim, raw-HTML-extracted)

```
Local sandboxing in the GitHub Copilot app
September 23, 2026 · 1 minute read

Local sandboxing helps reduce the potential impact of unintended commands by
limiting access to files, network resources, and credentials on your machine.
In the GitHub Copilot app, you configure it per project for local repository
and working tree sessions.

The project's sandbox settings include:
- Filesystem: Additional read/write, additional read-only, and denied folder
  lists.
- Network: Outbound internet and local network settings.
- Credentials: Git credentials for authenticated HTTPS git operations, and
  GitHub CLI credentials for GitHub CLI authentication.

These project settings describe the policy that the app requests when a
sandboxed session starts. The effective policy can be more restrictive when
enterprise-managed settings apply.

If your operating system cannot enforce the requested policy, the sandboxed
shell fails with an error rather than running without a sandbox.

Get started
Local sandboxing is off by default. Open the app settings, select your
project, and turn on Sandbox new sessions under "Sandbox". This applies to
new sessions in the project, not sessions already running. Changes to
filesystem, network, and credential settings apply to new sessions or when
an existing session restarts.

To enable sandboxing for an active local session, enter /sandbox on. This
changes that session without changing the project default.

Local sandboxing does not apply to cloud sandbox sessions or sessions
running on a remote host. GitHub Copilot app and Copilot CLI sandbox
settings are configured separately.

Local sandboxing is in public preview and subject to change.

Learn more about configuring local sandboxing in the GitHub Copilot app
(https://gh.io/github-app-local-sandboxing).

Tag: copilot
```

*Source: `https://github.blog/changelog/2026-09-23-local-sandboxing-in-the-github-copilot-app`,
raw HTML fetched via `curl`, `<article>` element isolated, tags stripped, HTML
entities decoded.*

### Configuration how-to page: filesystem/network/credential mechanics (condensed, verbatim quotes preserved)

```
Title: "Configuring local sandboxing in the GitHub Copilot app"
Note: "Local sandboxes for GitHub Copilot are in public preview and subject
to change."

DEFAULT FILESYSTEM ACCESS:
"By default, a sandboxed session has read/write access to its workspace and
current working directory."
Three configurable lists: Additional read/write, Additional read-only,
Denied.
"A more-specific denied folder remains denied when a broader parent folder
has read or write access."
Windows: "If the active Windows sandbox capabilities cannot guarantee the
denial, a sandboxed command fails with an unsupported-policy message. The
command does not run with the denied path accessible or without a sandbox."

DEFAULT NETWORK ACCESS:
"By default, sandboxed sessions can connect to the internet and your local
network."
Two toggles: Outbound internet, Local network.
Linux: "the sandbox cannot control local network access independently for
spawned processes, such as shell commands and local MCP or LSP servers. The
setting still applies to in-process operations, such as web requests and
remote MCP connections."

DEFAULT CREDENTIAL ACCESS:
"By default, authenticated Git and GitHub CLI operations are available
inside the sandbox."
Two toggles: Git credentials, GitHub CLI credentials.
"Turning off credential access can prevent operations such as pushing a
branch or creating a pull request from inside the sandbox."

SESSION COMMANDS:
/sandbox on   — turn on local sandboxing for the active session
/sandbox off  — turn off local sandboxing for the active session
/restart-session — restart a session while keeping its history (needed to
  apply new project-default settings to a running session)

BYPASS PROMPT:
"Run outside the sandbox?" — Cancel / Run once outside the sandbox /
Disable sandboxing for the remainder of the session.
"An enterprise owner can prevent users from running tools outside the
sandbox. For more information, see Enterprise managed settings."
```

*Source: `docs.github.com/en/copilot/how-tos/github-copilot-app/configure-local-sandboxing`
(resolved from the changelog's `gh.io/github-app-local-sandboxing` shortlink), parsed
from the page's embedded `__NEXT_DATA__` JSON (`articleContext.renderedPage`), fetched
2026-09-25.*

### Enterprise `sandbox` managed-settings key: prose and schema (verbatim, confirms Copilot app support)

```
Prose (id="sandbox" section):
"Enforces minimum local sandbox restrictions for Copilot CLI and the GitHub
Copilot app. Managed sandbox settings impose restrictions rather than
defaults: [force-on / capability / path-list precedence rules]"

"In app sessions, the embedded runtime parses, combines, and enforces the
complete managed sandbox object, including properties that are not
available in the app's project settings. The app displays the user's
project settings, not the complete effective managed policy, and does not
show per-setting managed locks."

Sub-properties (verbatim descriptions):
enabled              — true requires sandboxing by default; users cannot
                        disable it (CLI: --no-sandbox / /sandbox disable
                        cannot override; App: project setting / /sandbox
                        off cannot override). Bypass-prompt override still
                        possible unless allowBypass: false.
failIfUnavailable    — combined with enabled: true, blocks model and tool
                        execution if the sandbox backend cannot be
                        validated/compiled/enforced, instead of allowing
                        unsandboxed execution.
allowBypass          — false prevents per-command bypass and prevents
                        session-wide bypass via the sandbox-bypass prompt;
                        in CLI, also blocks /sandbox disable.
addCurrentWorkingDirectory — false prevents auto-adding CWD to read/write
                        paths.
sandboxMcpServers    — true requires local MCP servers to run in the
                        sandbox (remote MCP servers unaffected).
sandboxLspServers    — true requires language servers to run in the
                        sandbox.
gitAuth              — false prevents injecting a GitHub token for
                        authenticated Git HTTPS ops in the sandbox.
ghAuth               — false prevents injecting a GitHub token for GitHub
                        CLI in the sandbox.
allowDevToolAccess   — false prevents automatic access to dev-tool config,
                        caches, registries, toolchains (can contain
                        registry credentials/tokens); can break package
                        restoration/builds that rely on shared caches.
userPolicy           — object configuring filesystem, network, and macOS
                        Seatbelt restrictions (sub-schemas below).

sandbox.userPolicy.filesystem:
  readwritePaths / readonlyPaths — exact-string-matched managed grant
    lists; an empty managed array removes all user-configured grants of
    that type (but not separately-assembled access like tmp dirs or CWD).
  deniedPaths — managed value ADDS to (does not replace) user denials.

sandbox.userPolicy.network:
  allowOutbound / allowLocalNetwork — false blocks the respective access.
  allowedHosts / blockedHosts — hostname/IP allow-deny lists; blocked
    takes precedence over allowed; blocking a domain blocks subdomains.
  proxy.url — routes sandboxed traffic through an upstream HTTP proxy;
    "Platform support and enforcement vary."

Supported-keys table row (as fetched 2026-09-25):
Key: sandbox
Purpose: "Enforces minimum local sandbox restrictions for command
          execution, filesystem and network access, credentials, and
          local MCP and LSP servers"
Copilot CLI:          Supported
VS Code:               Not supported
GitHub Copilot app:    Supported   <-- was "Not supported" as of 2026-09-09
                                        per docs-github-copilot-jetbrains-
                                        enterprise-managed-sandbox-sept2026.md
Copilot cloud agent:   Not supported
JetBrains IDEs:        Not supported  (still contested; see issue #3334)
```

*Source: `docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
`sandbox` key prose section and "Supported keys" table row, parsed from the page's
embedded `__NEXT_DATA__` JSON, icon `aria-label` attributes read directly from raw
HTML SVG markup, fetched 2026-09-25.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 4): that note's
    July 14, 2026 announcement of JetBrains local sandboxing (public preview) is the
    first instance of this "local sandboxing" feature family; this note documents its
    second client (the GitHub Copilot app), two months later, with an identical
    off-by-default / public-preview pattern.
  - `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md` (Claim 3 and
    the linked "Configuring local sandbox settings" artifact, which that note identified
    as Copilot-CLI-scoped): this note's Concrete Artifacts confirm the CLI-scoped
    `/sandbox` interface documented there (General/Auth/Filesystem/Network tabs,
    `(managed)` labeling for locked settings) shares its three-axis structure
    (filesystem/network/credentials-or-auth) with the app-scoped policy documented here,
    even though the two are "configured separately" per Claim 5.
  - `docs-ghaw-sandbox-reference.md` (Claims 4 and 5): a structurally different product
    (GitHub Agentic Workflows' AWF firewall) but the same design philosophy — named,
    explicit filesystem access tiers and a fail-closed posture for what the runtime
    cannot guarantee. Neither note documents the other's product, but together they show
    GitHub applying a consistent sandboxing philosophy (explicit tiers, deny-wins
    precedence, fail rather than silently degrade) across both its Actions-based agentic
    workflow product and its interactive Copilot clients.
  - `docs-github-copilot-enterprise-bypass-permissions.md` (Claim 1,
    `disableBypassPermissionsMode`): the "Run outside the sandbox?" bypass prompt (Claim
    10) and the enterprise `sandbox.allowBypass` sub-property (Claim 12) are a
    sandbox-specific instance of the same general pattern that note documents for
    permission prompts broadly — a user-facing escape hatch that exists by default and
    that enterprises can lock via managed settings.

- **Extends**:
  - `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`: that note's
    Concrete Artifacts recorded the `sandbox` key's "Supported keys" table as of a
    2026-09-09 fetch, with "GitHub Copilot app: Not supported." This note's Claim 11
    re-fetches the identical table two weeks later (2026-09-25) and finds "GitHub Copilot
    app: Supported" — the first cell in that table this corpus has observed change value
    over time. This does not resolve that note's filed issue #3334 (which concerns the
    *JetBrains* column, still "Not supported"), but it directly updates the "GitHub
    Copilot app" column that note recorded, and demonstrates the changelog-to-reference-
    doc lag those notes hypothesized does eventually close.
  - `docs-github-copilot-app-security-review.md`: that note documented `/security-review`
    reaching the GitHub Copilot app on July 14, 2026, as a chat-window slash command
    available to all plan tiers. This note documents a second, distinct security-relevant
    capability (execution isolation, not vulnerability scanning) reaching the same client
    over two months later. Together they show the app surface's security posture
    maturing along two independent axes: detecting vulnerabilities in code the agent
    writes (`/security-review`) and restricting what the agent's own tool calls can touch
    while it works (local sandboxing).
  - `docs-github-copilot-app-opentelemetry.md`: that note documented the `telemetry` key
    reaching the GitHub Copilot app on Sept 22, 2026 — one day before this changelog —
    but found the reference page's `telemetry` row still marked "Not supported" for the
    app as of a Sept 24 fetch (issue #3682, unresolved). This note's Claim 11 fetches the
    same reference page one day later (Sept 25) and finds the *`sandbox`* row (a
    different key) already reading "Supported" for the app. The two keys are on
    different update timelines on the same page as of this extraction — worth flagging to
    the Assayer as evidence that reference-page currency lag is per-key, not a single
    page-wide staleness, so issue #3682 should not be assumed to resolve just because a
    different key's cell updated.

- **Related** (different product, same threat pattern — not corroboration):
  - `failure-copilot-cowork-file-exfiltration.md`: this failure report documents
    Microsoft Copilot Cowork (a different Microsoft product family, not GitHub Copilot)
    enabling a complete file-exfiltration chain via unrestricted agent email-sending,
    external image rendering, and pre-authenticated OneDrive links. It is not the same
    product as this source and is not cited as corroboration or contradiction. It is
    flagged as motivating context: a credential- and network-scoped local sandbox of the
    kind this source documents (crediential toggles per Claim 2; network allow/deny per
    Claim 9) is a plausible mitigating control against a comparable exfiltration chain if
    GitHub Copilot agents were ever similarly able to send outbound communications
    without approval — the guide should not claim this sandbox feature *prevents* that
    class of attack (the sources do not test that scenario against each other), only that
    it addresses the same general attack-surface category (uncontrolled credential and
    network access from agent-run tools).

- **Contradicts**: None identified against existing source notes. This note's own
  cross-check (Claim 11) found the reference page's `sandbox` key now *agrees* with this
  changelog for the "GitHub Copilot app" column, unlike the pattern in issues #3334 and
  #3682. No contradiction issue filed.

- **Novel**:
  - **First corpus documentation of app-level (not CLI, not JetBrains) local sandboxing
    configuration** (Claims 1-10): the per-project settings UI path, the `/sandbox
    on`/`off` commands, `/restart-session`, and the "Run outside the sandbox?" bypass
    prompt are all new to the corpus for this specific client.
  - **Denied-folder precedence rule** (Claim 8) and **OS-specific enforcement gaps for
    Windows (fail-closed on unguaranteeable denial) and Linux (no independent local-
    network control for spawned processes)** (Claim 9): none of these platform-specific
    behaviors are documented in any prior corpus source for any Copilot client.
  - **A confirmed, dated instance of the reference-page documentation lag closing**
    (Claim 11): the corpus has two open contradiction issues (#3334, #3682) hypothesizing
    that a changelog's claim will eventually be reflected in the reference page's support
    matrix. This is the first confirmed instance of that actually happening, for a
    different key/client pair, within roughly two weeks of the original changelog.
  - **The `failIfUnavailable` enterprise sub-property's whole-session-blocking behavior**
    (Claim 12), distinct from the project-level per-command fail-closed behavior (Claim
    6): no prior source distinguishes these two tiers of fail-closed sandbox enforcement.

## Guide Impact

### Chapter 06: Security Threat Model

- **Add local sandboxing in the GitHub Copilot app as a concrete, practitioner-facing
  execution-isolation mechanism** (Claims 1-6): document the three-dimension policy model
  (filesystem/network/credentials), the off-by-default posture, and — most importantly —
  the fail-closed guarantee (Claim 6: unenforceable policy fails the shell rather than
  running unsandboxed). This is a strong, concrete example for the threat model's
  existing discussion of "actual egress scope and capability-based access" (per the
  Prospector's triage key question) — it gives named, current-product mechanics rather
  than an abstract principle.
- **Document the two-tier fail-closed model explicitly, not as a single claim**
  (Claims 6, 9, 12): (1) project-level: an unenforceable shell-level policy fails that
  specific sandboxed shell; (2) enterprise `failIfUnavailable: true`: blocks model and
  tool execution for the whole session if the sandbox backend can't be validated. The
  guide should not conflate these — they differ in blast radius of the failure.
  Additionally, flag the Linux local-network gap (Claim 9) as a specific, named exception
  to "the sandbox enforces network policy" — it does not, for spawned child processes,
  on that platform.
- **Add the enterprise `sandbox` managed-settings key's full sub-property schema**
  (Concrete Artifacts, Claims 11-12) to the guide's enterprise hardening reference
  material: `enabled`, `failIfUnavailable`, `allowBypass`, `addCurrentWorkingDirectory`,
  `sandboxMcpServers`, `sandboxLspServers`, `gitAuth`, `ghAuth`, `allowDevToolAccess`,
  `userPolicy.filesystem/network/seatbelt`. Note that as of this extraction, this key
  applies to Copilot CLI and the GitHub Copilot app, but not VS Code, Copilot cloud
  agent, or JetBrains IDEs — a client-support asymmetry worth stating explicitly so
  practitioners don't assume uniform enterprise sandbox governance across all Copilot
  surfaces.

### Chapter 02: Harness Engineering

- **Add the "Run outside the sandbox?" bypass-prompt UX and its enterprise lock**
  (Claim 10) as a concrete pattern for harness designers: a default escape hatch with
  three granularities (cancel / run-once / disable-for-session), lockable by
  administrators via `allowBypass: false`. This is a reusable design pattern independent
  of GitHub's specific implementation — harness engineers building their own sandboxed
  tool-execution layers should consider offering equivalent graduated bypass options
  rather than an all-or-nothing sandbox toggle.
- **Note the settings-visibility gap**: the reference page states the app "displays the
  user's project settings, not the complete effective managed policy" (Claim 11) when
  enterprise-managed properties are in force. Harness engineers building admin tooling
  should not assume a project-settings UI reflects the full effective policy when
  enterprise overlays exist — this is a specific, documented instance of a broader
  "displayed config ≠ effective config" gap worth generalizing in the guide.

## Extraction Notes

1. **WebFetch's AI-summarized pass was largely accurate but not verified verbatim**: an
   initial WebFetch call against the changelog URL returned a plausible, close paraphrase
   of the changelog. Per MINER.md §2a, this extraction re-fetched the raw HTML via `curl`,
   isolated the `<article>` element, stripped tags, and decoded entities before writing
   any `Quote` field — all quotes above are copied from that raw-HTML extraction, not the
   WebFetch summary.
2. **Linked how-to page resolved through a `gh.io` shortlink**: the changelog's "Learn
   more" link points to `https://gh.io/github-app-local-sandboxing`, which this
   extraction resolved via `curl -I` (following the 301/302 redirect chain) to
   `docs.github.com/en/copilot/how-tos/github-copilot-app/configure-local-sandboxing`
   before fetching it. This page was fetched as raw HTML and its content parsed from the
   embedded `__NEXT_DATA__` JSON payload (`articleContext.renderedPage`), the same method
   used by several prior notes in this corpus for `docs.github.com` React/Next.js pages.
3. **A third page — the enterprise managed-settings reference — was fetched beyond the
   two the changelog and how-to page link to**, specifically to test whether the
   platform's own `sandbox`-key support matrix corroborates this changelog, following the
   precedent in `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md` and
   `docs-github-copilot-app-opentelemetry.md` (both of which found contradictions this
   way). This time the cross-check found corroboration instead (Claim 11) — reported with
   the same rigor as a contradiction would have been, per MINER.md §4/§4a's instruction to
   cross-reference against the existing corpus rather than only against the source itself.
4. **One linked page not followed**: the how-to page links to "About cloud and local
   sandboxes for GitHub Copilot" for a cloud-vs-local conceptual overview. This was not
   fetched — the changelog and how-to page together already establish the local/cloud
   scope boundary (Claim 5) with a direct quote, and the conceptual-overview page was
   judged unlikely to add claims beyond what's already extracted for this note's scope
   (app-level local sandboxing specifically, not the cloud sandbox architecture). Flagged
   as a candidate for a future source note if cloud sandboxing needs its own dedicated
   extraction.
5. **No contradictions filed**: see Cross-References → Contradicts. This is the first
   note in the local-sandboxing/enterprise-managed-settings family in this corpus to
   cross-check the reference page and find agreement rather than a discrepancy.
6. **`confidence_overall` set to `emerging`, not `settled`**: every individual claim
   about what the sources state is settled (verbatim, first-party, mutually consistent
   across three pages). The overall rating is `emerging` because the underlying
   capability — local sandboxing in the GitHub Copilot app — is explicitly labeled public
   preview and subject to change by the source itself (Claim 7), consistent with how this
   corpus has rated the other preview-labeled sandboxing announcements
   (`docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`:
   `confidence_overall: emerging`).
