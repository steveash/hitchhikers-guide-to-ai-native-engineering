---
source_url: https://github.blog/changelog/2026-06-23-copilot-cli-new-terminal-interface-is-generally-available
source_type: docs
title: "Copilot CLI: New terminal interface is generally available"
author: GitHub (official changelog)
date_published: 2026-06-23
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: settled
issue: "#1290"
---

# Copilot CLI: New Terminal Interface is Generally Available

> GitHub's June 23, 2026 changelog announces the GA promotion of the Copilot CLI terminal redesign — removing the `/experimental on` gate — and introduces new in-session tool configuration commands (`/mcp add`, `/mcp search`, `/skills`, `/plugin`) that eliminate the need to hand-edit configuration files.

## Source Context

- **Type**: docs (GitHub official product changelog, June 23, 2026; ~350 words)
- **Author credibility**: GitHub engineering team official product changelog. Authoritative for: GA status of the terminal, exact tab names and keyboard shortcuts, the new in-session tool configuration commands (`/mcp add`, `/mcp search`, `/skills`, `/plugin`), color modes, and accessibility behavior. Not a credible source for: plan-tier availability, whether `/experimental on` still works as a backward-compatible command, what happens if the CLI is run outside a GitHub repository for Issues/PR tabs, or how `/mcp add` interacts with existing MCP server configuration files.
- **Scope**: GA promotion of the experimental terminal redesign (tabbed interface, accessibility improvements) and new in-session tool configuration UX. Does NOT cover: the GA status of other experimental features from the June 2 source (prompt scheduling via `/every`/`/after` is not mentioned), rubber duck or voice input (already GA per June 2 source), plan-tier differences, or detailed documentation for `/skills` toggle versus the `gh skill` package manager CLI.

## Extracted Claims

### Claim 1: The redesigned terminal interface for Copilot CLI — previously requiring `/experimental on` — is now generally available to all users

- **Evidence**: Official GitHub product changelog explicitly declaring GA status. The Microsoft Build 2026 preview is named as the prior public introduction of the feature.
- **Confidence**: settled (GA status stated definitively in official changelog)
- **Quote**: "The redesigned terminal interface for GitHub Copilot CLI that we previewed at Microsoft Build 2026 is now generally available."
- **Our assessment**: The operational impact is immediate: team deployments that were holding off on the terminal redesign due to its experimental status can now recommend it without caveats. The `/experimental on` gate was required per `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 9); that requirement is now removed. Guide advice referring to experimental status of the terminal UI should be updated to reflect GA.

### Claim 2: The GA terminal introduces a tabbed interface — Session, Gists, Issues, and Pull requests — but the Issues and Pull requests tabs only appear when the CLI is run inside a GitHub repository

- **Evidence**: Official changelog documents the tab names and the repository-context condition for Issues/PR tabs.
- **Confidence**: settled (tab names and conditional behavior documented in official changelog)
- **Quote**: "Press Tab to move between the default **Session** tab and a **Gists** tab for your personal gists. When you run the CLI inside a GitHub repository, you also get **Issues** and **Pull requests** tabs for that repository."
- **Our assessment**: The repository-context condition is an important operational detail not captured in the earlier experimental announcement (`docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, Claim 7, which listed all four tabs without noting the repo requirement). Practitioners running the CLI in a non-repo directory will only see Session and Gists tabs — Issues and PR tabs are not universally available. For harness engineering: the Issues/PR tabs are not usable in directory-level agent sessions; practitioners must be inside a GitHub repository to access them.

### Claim 3: Pressing `c` on a highlighted issue or pull request drops a reference into the active prompt, enabling immediate Copilot invocation on that item

- **Evidence**: Official changelog documents the keyboard shortcut and its behavior.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Highlight an issue or pull request and press c to drop a reference to it into your prompt, then ask Copilot to investigate, fix, comment on, or review it."
- **Our assessment**: The `c` shortcut closes the round-trip that previously required copy-pasting issue numbers or URLs into prompts. The listed action verbs (investigate, fix, comment on, review) map directly to concrete Copilot CLI task types. For Ch01 (Daily Workflows): the pattern of "find issue in Issues tab → press `c` → dictate action" is a concrete new daily-workflow primitive that reduces context-switching between the browser and terminal.

### Claim 4: The `o` key opens the highlighted item on GitHub in the browser; the `/` key on the Issues or Pull requests tab runs a GitHub search query

- **Evidence**: Official changelog documents both keyboard shortcuts.
- **Confidence**: settled (product facts in official changelog)
- **Quote**: "Press o to open the highlighted item on GitHub in your browser, or press / on the **Issues** or **Pull requests** tab to search GitHub with your own query."
- **Our assessment**: These two shortcuts complete the terminal-as-hub pattern: browse within CLI (default), escalate to browser when needed (`o`), and search with custom queries (`/`). The `/` search shortcut is particularly useful for practitioners who need to find items not visible in the default tab view. Together with `c` (Claim 3), the terminal now supports a full triage workflow without leaving the CLI session.

### Claim 5: The tab bar can be reordered, hidden, or turned off entirely from settings; mouse click also switches tabs

- **Evidence**: Official changelog states both customization and mouse support.
- **Confidence**: settled (product facts in official changelog)
- **Quote**: "You can also click a tab with your mouse to switch to it. From your settings, you can reorder, hide, or turn off the tab bar entirely."
- **Our assessment**: The ability to turn off the tab bar entirely is important for practitioners who prefer minimal UI — the terminal can be returned to a single-pane experience without the tabbed overhead. Reordering tabs reduces cognitive load for workflows that primarily use Issues or PRs. Mouse support reduces the learning curve for practitioners accustomed to GUI environments. For enterprise deployments: teams can standardize tab bar configuration via a shared settings file (a pattern documented in `docs-github-copilot-cli-settings-command.md`, Claim 8's Ctrl+E shortcut).

### Claim 6: MCP server setup is now a guided in-session experience — `/mcp add` presents an interactive form, `/mcp search` browses the GitHub MCP Registry and installs directly; new servers are immediately available without restarting the CLI

- **Evidence**: Official changelog documents both commands and the no-restart behavior.
- **Confidence**: settled (product facts in official changelog)
- **Quote**: "Run `/mcp add` to fill out an interactive form or `/mcp search` to browse the GitHub MCP Registry and install a server directly. New servers are available immediately, without restarting the CLI."
- **Our assessment**: This is the most novel capability in the GA release from a harness engineering perspective. Prior MCP configuration required hand-editing JSON or YAML configuration files outside the CLI session — a friction point that demanded the practitioner know the correct schema. The interactive `/mcp add` form eliminates schema knowledge as a prerequisite. The GitHub MCP Registry integration in `/mcp search` makes discoverability first-class. The immediate availability (no restart) removes a deployment barrier: practitioners can add an MCP server mid-session and use it in the same conversation. For Ch02 (Harness Engineering): this changes the recommended MCP server setup workflow from "edit config file, restart" to "/mcp add, available immediately."

### Claim 7: The `/skills` in-session command toggles individual skills on or off using arrow keys and spacebar

- **Evidence**: Official changelog documents the command and its interaction model.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Run `/skills` to toggle individual skills on or off with the arrow keys and the space bar."
- **Our assessment**: This is an in-session toggle UI distinct from the `gh skill` package manager (documented in `docs-github-copilot-agent-skills-cli.md`) — the `gh skill` CLI manages installation and distribution; `/skills` manages which installed skills are active in the current session. For practitioners who install many skills globally but want to enable only relevant ones per context: `/skills` provides session-scoped enable/disable without reinstallation. This is analogous to enabling/disabling browser extensions per tab — the capability is installed but activation is session-specific.

### Claim 8: The `/plugin` command browses and installs plugins from a marketplace, a repository, or a local path

- **Evidence**: Official changelog documents the command and its three installation sources.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Browse and install plugins from a marketplace, a repository, or a local path with the `/plugin` command."
- **Our assessment**: Plugins are distinct from skills and MCP servers in the Copilot CLI extensibility model — the changelog treats them separately. The three installation sources (marketplace, repository, local path) parallel package manager paradigms and support enterprise use cases: a marketplace for community plugins, a repository for org-shared plugins, and a local path for development-time or air-gapped installations. For Ch02: the plugin installation surface adds a third extensibility primitive alongside MCP servers and skills.

### Claim 9: The GA interface uses theme-aware semantic colors and responsive components; color modes `default`, `dim`, `high-contrast`, and `colorblind` are available via `/theme`

- **Evidence**: Official changelog names the color modes and the `/theme` command.
- **Confidence**: settled (product facts in official changelog)
- **Quote**: "The new interface uses theme-aware semantic colors and responsive components that adapt to narrow terminals without truncating what you need to read."
- **Our assessment**: The June 23 GA announcement lists four color modes via `/theme`: `default`, `dim`, `high-contrast`, `colorblind`. This differs from the June 2 experimental announcement (`docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, Claim 8) which listed five modes: `default`, `github`, `dim`, `high-contrast`, `colorblind`. The `github` mode present in the experimental version does not appear in the GA announcement. This may indicate the `github` mode was dropped during the experimental period, or the GA changelog omitted it. Note: `colorMode` is also a `/settings` key (per `docs-github-copilot-cli-settings-command.md`, Claim 7), making `/theme` a shorthand for `/settings colorMode <value>`. The responsive components adapting to narrow terminals is a new detail not in the June 2 source — the terminal now avoids truncating content on small displays.

### Claim 10: Screen reader support activates automatically when a screen reader is detected, with labeled icons and animations that disable themselves

- **Evidence**: Official changelog documents the automatic detection behavior and what adapts.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Rely on screen reader support that automatically turns on when a screen reader is detected, with labeled icons and animations that disable themselves."
- **Our assessment**: The automatic detection removes the configuration burden from users who rely on screen readers — no manual setting is required. The explicit disabling of animations under screen reader mode is a meaningful accessibility implementation: animations that convey state in visual modes are often disorienting or meaningless in screen reader contexts. For enterprise deployments with accessibility compliance requirements: the automatic screen reader detection and the `high-contrast`/`colorblind` modes together address multiple accessibility needs in a production GA release.

## Concrete Artifacts

### GA Terminal Tab Interface

```
Tabs (always available):
  - Session       (current agent session — default tab)
  - Gists         (personal gists)

Additional tabs (only when CLI runs inside a GitHub repository):
  - Issues        (repository Issues)
  - Pull requests (repository Pull Requests)

Tab keyboard shortcuts:
  Tab     — move between tabs
  c       — drop reference to highlighted issue/PR into prompt
  o       — open highlighted item on GitHub in browser
  /       — search GitHub (on Issues or Pull requests tab)
  [click] — mouse click to switch tabs

Tab bar customization (via settings):
  - Reorder tabs
  - Hide individual tabs
  - Turn off tab bar entirely
```

*Source: Copilot CLI changelog, June 23, 2026*

### In-Session Tool Configuration Commands (GA)

```
# MCP servers — no file editing, no restart required
/mcp add              — interactive form for MCP server setup
/mcp search           — browse GitHub MCP Registry, install directly
                        (new servers available immediately, no restart)

# Skills — toggle active skills per session
/skills               — toggle individual skills on/off with arrow keys + spacebar

# Plugins — install from multiple sources
/plugin               — browse and install from marketplace, repository, or local path

# Settings — view/change configuration inline
/settings             — open inline settings dialog (see docs-github-copilot-cli-settings-command.md)
```

*Source: Copilot CLI changelog, June 23, 2026*

### Accessibility and Color Configuration

```
# Color mode selection
/theme default        — default color scheme
/theme dim            — reduced brightness
/theme high-contrast  — high contrast mode
/theme colorblind     — colorblind-friendly palette

# (equivalent to: /settings colorMode <value>)

# Screen reader support
- Automatic: activates when screen reader is detected
- No manual configuration required
- Labeled icons, animations disabled under screen reader mode

# Responsive layout
- Components adapt to narrow terminals without truncating content
```

*Source: Copilot CLI changelog, June 23, 2026*

### Feature Availability Matrix (Updated from June 2 → June 23)

```
Feature                       June 2 Status    June 23 Status
────────────────────────────────────────────────────────────────────
Rubber duck (/rubber-duck)    GA               GA (unchanged)
Voice input                   GA               GA (unchanged)
Prompt scheduling (/every,    Experimental     Not mentioned
  /after)                     (/experimental)  (status unknown)
Terminal redesign             Experimental     GA ← STATUS CHANGE
                              (/experimental)  (no gate required)
/mcp add, /mcp search         Not documented   GA (new in this source)
/skills toggle UI             Not documented   GA (new in this source)
/plugin command               Not documented   GA (new in this source)
```

*Source comparison: June 2 changelog (issue #1067) vs. June 23 changelog (issue #1290)*

## Cross-References

- **Extends** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 9): That source documented the two-tier availability model — rubber duck and voice as GA, prompt scheduling and terminal as experimental requiring `/experimental on`. This source removes the `/experimental on` requirement for the terminal redesign, updating its status to GA. The terminal claims (Claims 7, 8) in that source are now superseded for availability status, though the feature descriptions remain accurate. Note: prompt scheduling's status is not addressed in this June 23 source.

- **Extends** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 7): That source described the experimental terminal tab navigation (Session, Issues, Pull requests, Gists) without specifying that Issues and Pull requests tabs require a GitHub repository context. This source clarifies that condition. For guide advice: the Issues/PR tab pattern should be qualified with "when running inside a GitHub repository."

- **Potential discrepancy with** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 8): That source lists five color modes for the experimental terminal: `default`, `github`, `dim`, `high-contrast`, `colorblind`. The June 23 GA announcement lists four modes: `default`, `dim`, `high-contrast`, `colorblind` — the `github` mode is absent. This may indicate the `github` mode was dropped between experimental and GA, or the GA changelog omitted it. Not filed as a contradiction because: (a) the missing mode leads to the same guide advice (use `/theme` to select a color mode), and (b) WebFetch summarization may have missed it. Assayer should verify against the source URL.

- **Extends** `docs-github-copilot-cli-settings-command.md` (Claim 7): That source documented `/settings` consolidating `/theme`, `/streamer-mode`, and `/experimental` with live-application for `colorMode`. This source confirms that `/theme` remains a first-class command in the GA terminal and is listed alongside `/settings` as a tool configuration entry point — the two coexist. The June 11 `/settings` note's guidance on configuring `colorMode` via `/settings` is consistent with this source.

- **Corroborates** `docs-github-copilot-cli-settings-command.md` (Claim 8): That source documented that the settings system has a canonical file representation accessible via Ctrl+E. This source adds tab bar customization (reorder, hide, turn off) as settings-governed behavior — consistent with the pattern that CLI visual preferences are stored in the settings file.

- **Extends** `docs-github-copilot-agent-skills-cli.md` (Claim 1): That source established the Copilot CLI as a primary surface for new GitHub agent feature development and documented `gh skill` as a package manager for skills distribution. This source introduces the `/skills` in-session toggle UI — a distinct, complementary skills management surface: `gh skill` manages installation/distribution; `/skills` manages activation per session. Together they define a two-layer skills management model: install-time management (gh skill) and session-time activation (/skills).

- **Novel**:
  - **In-session MCP server setup via `/mcp add` and `/mcp search` without file editing**: No prior corpus source documents a CLI-native guided MCP server registration flow that requires no file editing and takes effect immediately without restart. Prior MCP configuration guidance across all corpus sources involves config file editing.
  - **GitHub MCP Registry browser (`/mcp search`)**: No prior corpus source documents a browsable registry of MCP servers accessible directly from within a CLI session.
  - **In-session plugin management (`/plugin`)**: No prior corpus source documents a `/plugin` command as a distinct CLI extensibility surface, separate from MCP servers and skills.
  - **`c`/`o`/`/` tab keyboard shortcuts for issue/PR interaction**: No prior corpus source documents keyboard shortcuts for in-terminal GitHub entity interaction (reference in prompt, open in browser, search).
  - **Tab bar customization (reorder, hide, disable)**: No prior corpus source documents this level of terminal layout customization as a settings-governed feature.

## Guide Impact

### Chapter 01: Daily Workflows

- **Remove experimental caveat from terminal recommendations**: Guidance that directs practitioners to enable the terminal via `/experimental on` should be updated. The terminal is now available by default. Update to: run `copilot update` to ensure the latest CLI, then the tabbed interface is active without any gate.
- **Add the `c`/`o`/`/` shortcut workflow**: Document the triage-from-terminal pattern: open Issues tab, find the relevant issue, press `c` to reference it in the prompt, then dictate the action (investigate, fix, comment, review). This is a concrete daily-workflow improvement that reduces context-switching to the browser.
- **MCP server onboarding path**: Replace "edit your MCP config file" setup guidance with `/mcp search` (discover from GitHub MCP Registry) or `/mcp add` (interactive form). Note that new servers activate immediately — no session restart needed.

### Chapter 02: Harness Engineering

- **MCP server configuration via `/mcp add`**: Update the MCP setup workflow. The CLI now provides an interactive form-based path that eliminates schema knowledge as a prerequisite. For teams onboarding new members to a Copilot CLI harness, the command sequence is now: `/mcp search` (discover what's available) → install → immediately available. Document `/mcp add` as the recommended first-try path before resorting to manual config file editing.
- **Skills activation model**: Document the two-layer skills management model — `gh skill install` for distribution/installation (from `docs-github-copilot-agent-skills-cli.md`), `/skills` for per-session toggle. Harnesses that install many skills globally should guide practitioners to use `/skills` to enable only contextually-relevant skills, reducing prompt overhead per session.
- **Plugin surface**: Add `/plugin` as the third extensibility primitive alongside MCP servers and skills. Clarify the distinction: MCP servers extend what the agent can *do* (tools/resources); skills extend what the agent *knows* (context/instructions); plugins extend the CLI *application* (UI/workflow integrations).
- **Tab bar in terminal harness design**: Note that the Issues/PR tabs require a GitHub repository context — CLI sessions run in non-repo directories will not show these tabs. Harness configurations that target non-repo directories cannot rely on Issues/PR tab availability.

### Chapter 04: Agent Behaviors and Patterns

- **Update tabbed interface description**: The June 2 source (currently the primary citation for the tabbed terminal) described the tab layout without the repository-context condition. Update to: "Issues and Pull requests tabs appear only when the CLI is run inside a GitHub repository — they are not available in non-repository directories."

## Extraction Notes

1. **Source is a short changelog (~350 words)**: Four WebFetch calls were made to extract content with increasing specificity. The tool summarizes rather than reproducing content verbatim. Only quotes confirmed across multiple fetch passes are used as verbatim — the Assayer should verify all quotes against the source URL.
2. **`github` color mode discrepancy**: The June 2 experimental source listed `github` as a fifth color mode. The June 23 GA source lists only four modes. The discrepancy was explicitly tested in a targeted fetch asking specifically about the `github` mode; the result confirmed it was not present. This may be a real removal or a summarization artifact — see Cross-References section.
3. **Prompt scheduling status unaddressed**: The June 23 changelog does not mention prompt scheduling (`/every`, `/after`), which was documented as experimental in the June 2 source. Its current status (still experimental, GA, or discontinued) is not established by this source.
4. **`/skills` vs. `gh skill` distinction**: The `/skills` command documented here is an in-session activation toggle. The `gh skill` command in `docs-github-copilot-agent-skills-cli.md` is a separate GitHub CLI package manager for skill installation and distribution. These are two layers of the same skills ecosystem, not the same feature.
5. **No contradiction issues filed**: The color mode discrepancy (4 vs. 5 modes) does not lead to different guide advice and is not clearly attributable to the source versus WebFetch summarization. No contradiction issue filed.
