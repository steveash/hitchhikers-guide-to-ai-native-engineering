---
source_url: https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10
source_type: docs
title: "GitHub Copilot weekly releases — August 10"
author: GitHub (official changelog)
date_published: 2026-08-13
date_extracted: 2026-08-15
last_checked: 2026-08-15
status: current
confidence_overall: settled
issue: "#2712"
---

# GitHub Copilot Weekly Releases — August 10

> GitHub's August 13, 2026 weekly roundup covers five surfaces — general model rollouts,
> the standalone Copilot app, Copilot CLI, JetBrains, and VS Code 1.133 — and documents a
> near word-for-word repeat of the `/rewind` announcement from the August 3 digest, a new
> admin-controlled "enterprise managed settings" surface for JetBrains that parallels
> VS Code/CLI's existing managed-plugin governance, first-party Codex agent support inside
> JetBrains alongside Claude and native Copilot, and per-turn model switching between
> Claude BYOK and built-in models in VS Code. The linked JetBrains sub-changelog
> (August 11, 2026) was followed and supplies most of the substantive detail behind the
> weekly digest's two terse JetBrains bullets.

## Source Context

- **Type**: docs (GitHub official product changelog, August 13, 2026; "2 minute read" weekly
  roundup organized into five sections — GitHub Copilot general, GitHub Copilot app, GitHub
  Copilot CLI, GitHub Copilot for JetBrains, and VS Code 1.133 Release updates). One linked
  page was followed per MINER.md §1: the JetBrains sub-changelog "Copilot memory and Ollama
  in GitHub Copilot for JetBrains" (August 11, 2026), which is the "Read the full JetBrains
  update" link and is substantially longer and more detailed than the two bullets it is
  condensed from in the weekly digest. The VS Code 1.133 general release notes
  (`aka.ms/VSCode/133`) and the two "Try the Copilot app" / "Install the Copilot CLI"
  marketing links were not followed — consistent with the precedent in
  `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 2, where the general
  (non-Copilot-specific) VS Code release notes were judged out of scope for a Copilot-focused
  weekly digest.
- **Author credibility**: GitHub engineering team announcing production and rollout-in-progress
  features across five Copilot product surfaces. Authoritative for the existence of each
  feature, exact command/flag names (`/tasks`, `--mode autopilot`, `/rewind`, `/app`), and the
  behavioral descriptions given in the article and its linked JetBrains sub-changelog. Not a
  credible source for adoption metrics, comparative model quality (Kimi K3, MAI-Code-1.1-Flash),
  or effectiveness data for any UX change.
- **Scope**: A weekly digest covering the period since the prior weekly release (week of
  August 10, 2026), plus the full content of one linked JetBrains-specific changelog. Does NOT
  cover: Visual Studio (non-Code), Eclipse, Xcode, GitHub Mobile, or detailed configuration
  documentation for any listed feature beyond what the changelog and its one followed link
  state — this is an announcement-level summary, not a how-to guide. Per the Prospector's
  triage guidance, individual items summarized here may also exist as separate, more detailed
  standalone changelog entries and corpus source-notes (as already happened for Agent Plugins
  1.0 — see Claim 3).

## Extracted Claims

### Claim 1: Kimi K3 is rolling out to Copilot Pro, Pro+, Max, Business, and Enterprise plans
- **Evidence**: "GitHub Copilot, general" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Kimi K3 is rolling out to Copilot Pro, Pro+, Max, Business, and Enterprise plans."
- **Our assessment**: This is the first corpus documentation of Kimi K3 as a model integrated
  into GitHub Copilot specifically — prior corpus coverage of Kimi K3
  (`blog-thoughtworks-gall-kimi-k3-multi-model-era.md`,
  `blog-simonwillison-kimi-k3-pelican-benchmark.md`,
  `blog-latentspace-ainews-kimi-k3-wiki-memory.md`) evaluates the model on its own merits or
  via other vendors' tooling, not as a GitHub Copilot model-roster addition. Notably, the
  rollout spans individual tiers (Pro, Pro+, Max) and Business/Enterprise simultaneously,
  which contrasts with the individual-tier-first pattern documented for MAI-Code-1-Flash
  (`docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claim 2: Business/Enterprise listed
  as "not yet included" at that model's initial expansion). The source gives no rollout
  percentage, phasing detail, or reasoning for why this model shipped to all tiers at once.

### Claim 2: MAI-Code-1.1-Flash is rolling out in GitHub Copilot with native image understanding and improvements to coding quality, instruction following, tool use, and performance
- **Evidence**: "GitHub Copilot, general" section, second bullet.
- **Confidence**: emerging (a version-bump rollout announcement with no plan-tier or surface
  detail given, unlike the more detailed June 18 MAI-Code-1-Flash surface-expansion changelog)
- **Quote**: "MAI-Code-1.1-Flash is rolling out in GitHub Copilot with native image understanding and improvements to coding quality, instruction following, tool use, and performance."
- **Our assessment**: This extends `docs-github-copilot-mai-code-1-flash-more-surfaces.md`
  (June 18, 2026), which documented MAI-Code-1-Flash (no ".1") expanding to eight surfaces
  across Free-through-Max individual plans, with Business/Enterprise "listed as not yet
  included" (that note's Claim 2). This August 13 entry names a distinct, later version
  (MAI-Code-1.1-Flash) and adds "native image understanding" as a new capability not present
  in the June source's description — but gives no surface list or plan-tier detail, so it is
  not possible to confirm from this source alone whether 1.1 has reached the same eight
  surfaces or the same tier set as the June 1-Flash rollout. For a guide update: flag that a
  point-release of MAI-Code-1-Flash exists with multimodal (image) input support, without
  claiming parity in availability with the prior version until a more detailed changelog entry
  is found.

### Claim 3: Agent Plugins 1.0 — a build-once, cross-tool plugin standard — is reiterated as generally available in VS Code, Copilot CLI, the GitHub Copilot SDK, and the GitHub Copilot app
- **Evidence**: "GitHub Copilot, general" section, third bullet.
- **Confidence**: settled (restates a GA fact already established in the corpus)
- **Quote**: "Build a plugin once and use it across compatible agent tools with Agent Plugins 1.0, now generally available in VS Code, Copilot CLI, the GitHub Copilot SDK, and the GitHub Copilot app."
- **Our assessment**: This is a corroborating restatement, not new information — the GA launch
  itself was already documented in `docs-github-copilot-agent-plugins-1-0.md` (August 12, 2026,
  issue #2668), whose Claim 3 states the identical fact ("Support is generally available in VS
  Code, Copilot CLI, the GitHub Copilot SDK, and the GitHub Copilot app, on all Copilot plans").
  The one-day gap between the dedicated Agent Plugins 1.0 changelog (August 12) and this weekly
  digest (August 13) confirms GitHub's weekly-roundup format re-surfaces major standalone
  announcements from the same week rather than omitting them — the same pattern seen for
  `/rewind` in Claim 9 below, and worth noting as an editorial characteristic of this digest
  series (a Miner or Prospector reviewing a weekly digest should expect some bullets to be
  restatements of separately-filed changelog entries, not exclusively new material).

### Claim 4: The GitHub Copilot app's plugin management now shows each installed plugin's current version and supports updating plugins individually or all at once, from Customize or Settings
- **Evidence**: "GitHub Copilot app" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Installed plugins are now easier to manage. See each plugin’s current version, update plugins individually, or update them all at once from Customize or Settings."
- **Our assessment**: `docs-github-copilot-agent-plugins-1-0.md`'s Scope section explicitly
  flagged that its three fetched sources documented "only VS Code's UI... for plugin
  management" and did not cover "Copilot CLI/cloud-agent-specific UI for plugin management."
  This claim fills part of that gap by documenting the standalone Copilot app's plugin-update
  UI specifically: per-plugin version visibility plus a choice between individual and batch
  updates, accessible from two named entry points (Customize, Settings). The source does not
  say whether this predates or postdates the Agent Plugins 1.0 GA launch (Claim 3), or whether
  it applies to Agent Plugins 1.0 packages, GitHub's native Copilot plugin format, or both.

### Claim 5: The GitHub Copilot app lets users open an agent's own clarifying question in a side chat to talk it through, while the original question keeps waiting for a response
- **Evidence**: "GitHub Copilot app" section, second bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Talk through an agent’s question before answering by opening it in a side chat while the original question waits for your response."
- **Our assessment**: This is mechanically distinct from the app's `/side` command documented
  in `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 2 ("use /side to explore a
  parallel question without disrupting your main task") — `/side` is for the *user* to raise
  an unrelated parallel question, whereas this feature is specifically for discussing the
  *agent's own* clarifying question (an ask-user prompt) before committing to an answer, with
  the original prompt explicitly described as still "waiting." It is conceptually adjacent to
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` Claim 6, which documented
  session ask-user prompts being rendered as Markdown with attention notifications in
  JetBrains — that source improved the *visibility* of an agent's question; this one adds a
  *deliberation* mechanism before answering it, on a different surface (the standalone app).
  Neither source states whether the two are related implementations.

### Claim 6: Copilot CLI adds `/tasks` for managing all of a session's subagents and their tasks in one place
- **Evidence**: "GitHub Copilot CLI" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Manage all your subagents and their tasks in /tasks."
- **Our assessment**: No prior corpus source documents a dedicated Copilot CLI command for
  managing subagent tasks specifically. This is distinct from the Sessions sidebar documented
  in `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 8, which manages multiple
  concurrent top-level *sessions* within one terminal — `/tasks` instead appears scoped to
  subagents spawned *within* a session. The source gives no detail on what "managing" a task
  covers (viewing status, canceling, reprioritizing) beyond the one-line description, so this
  should be treated as a thin but novel data point pending a more detailed changelog entry.

### Claim 7: Copilot CLI now lets a practitioner queue prompts, shell commands, and supported slash commands while an agent turn is actively running
- **Evidence**: "GitHub Copilot CLI" section, second bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Queue prompts, shell commands, and supported slash commands while an agent turn is running."
- **Our assessment**: This names three distinct queueable input types (prompts, shell commands,
  slash commands) — broader than what a practitioner might assume from "queue prompts" alone.
  It is a standalone-CLI parallel to
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 4, which documented
  JetBrains' Claude-provider CLI integration supporting in-flight message queuing with three
  distinct interrupt modes (Add to Queue, Steer with Message, Stop and Send) back in June 2026.
  This August source does not specify whether the standalone Copilot CLI offers the same three
  interrupt semantics or a simpler single queue — the two features share the "don't wait for
  the current turn to finish before giving the agent more input" goal but are documented with
  different levels of granularity on different surfaces (JetBrains-embedded vs. standalone
  CLI), so this is noted as a parallel capability, not confirmed as the same mechanism.

### Claim 8: Copilot CLI's headless mode (`-p`) can now combine `--plan` and `--mode autopilot` so the agent produces a plan and then implements it without further prompting
- **Evidence**: "GitHub Copilot CLI" section, third bullet.
- **Confidence**: settled (product fact stated directly in official changelog, including the
  stated purpose)
- **Quote**: "Combine --plan and --mode autopilot in headless mode (-p) to have the agent produce a plan and then implement it."
- **Our assessment**: No prior corpus source documents Copilot CLI's headless/`-p` mode at all,
  so this is the first corpus data point for it. The "autopilot" naming is notable: it matches
  the permission-level name GitHub gave its VS Code Agents window "act without checking in at
  every step" mode, documented in `docs-github-copilot-vscode-june-2026.md` Claim 10 ("GitHub
  now names the 'act without checking in at every step' permission level 'Autopilot'"). This
  is a second data point for "autopilot" as a converging cross-surface term for
  unattended/unsupervised agent execution within the Copilot product line specifically (as
  opposed to the cross-*vendor* `/rewind` convergence documented in the August 3 digest). The
  source does not describe what happens if `--plan` output requires a decision the agent
  cannot resolve on its own mid-autopilot-execution.

### Claim 9: Copilot CLI's `/rewind` restores Copilot's own changes without requiring Git and without discarding the user's own subsequent edits
- **Evidence**: "GitHub Copilot CLI" section, fourth bullet.
- **Confidence**: settled (product fact restated from a prior changelog in near-identical
  wording)
- **Quote**: "Use /rewind to restore Copilot changes without requiring git or discarding user edits."
- **Our assessment**: This is functionally the same claim as
  `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 10 ("Use /rewind without Git to
  restore the conversation and files Copilot changed while preserving subsequent edits"),
  published one week earlier — both state Git-independence and preservation of the user's own
  post-rewind edits. The wording differs slightly ("discarding user edits" here vs. "preserving
  subsequent edits" there; this entry drops the earlier "restore the conversation" phrase and
  says only "restore Copilot changes"), but neither source explains whether that's a
  meaningful behavioral narrowing (conversation state no longer restored, only files) or just
  looser summary language reused across two consecutive weekly digests. Given the Claim 3
  pattern of this digest re-surfacing recent standalone announcements, and that no separate
  `/rewind`-specific changelog entry has been found in the corpus, this is most likely
  repeated/reinforced messaging rather than a second, distinct product change — but the
  wording delta is flagged here rather than silently resolved, since a future source (or the
  Assayer) may find that "restore the conversation" actually was dropped as a real scope
  change.

### Claim 10: The Copilot CLI `/app` command now preserves session and folder context when opening the Copilot app
- **Evidence**: "GitHub Copilot CLI" section, fifth bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "/app command now preserves session and folder context when opening the Copilot app."
- **Our assessment**: This is the first corpus mention of a Copilot CLI `/app` command at all —
  its purpose (bridging from the CLI into the standalone Copilot app) is inferable from the
  name and this one-line description, but the source does not state what "preserves... context"
  concretely carries over (the conversation history itself, just the working directory, or
  both). Notable as a cross-surface continuity mechanism alongside `/tasks` (Claim 6) and
  queueing (Claim 7) — this week's CLI bullets collectively deepen session continuity and
  multi-surface handoff rather than adding net-new agent capabilities.

### Claim 11: GitHub Copilot for JetBrains gains cross-session Copilot memory, letting the agent recall project details and preferences across separate chat sessions instead of requiring them to be repeated
- **Evidence**: Weekly digest "GitHub Copilot for JetBrains" section, first bullet; expanded in
  the linked JetBrains sub-changelog's "Copilot memory across chat sessions" section.
- **Confidence**: settled (product fact stated directly in both the digest and the linked
  changelog, with matching description)
- **Quote**: "Keep useful context across agent chat sessions with Copilot memory, so you don’t have to repeat the same project details or preferences." (digest); "Copilot memory can now retain and recall useful information across agent chat sessions. This helps you maintain context between conversations instead of repeatedly providing the same project details or preferences. You can manage the feature with the Copilot Memory toggle in the Copilot settings portal." (linked JetBrains sub-changelog)
- **Our assessment**: This extends `docs-github-copilot-memory-user-preferences.md` (May 15,
  2026), which documented Copilot Memory's user-level scope (cross-repository, cross-agent,
  "stated or inferred" preferences) as an early-access capability for Copilot Pro/Pro+ that
  note's Claim 5 said GitHub intended to "bring... to more plans in the future." This August 11
  entry is best read as that memory feature arriving on a new *surface* (the JetBrains IDE
  plugin, alongside whatever surfaces it already supported) rather than a new feature — the
  "Copilot Memory toggle in the Copilot settings portal" management path matches the May
  source's Claim 4 (reviewable/deletable via personal Copilot Memory settings). Neither this
  source nor the May source states whether JetBrains' arrival also lifts the Pro/Pro+-only
  gating from the May announcement; this source does not mention plan tier at all. Also
  extends `docs-github-copilot-memory-deletion-scope-cli.md` only insofar as both concern
  Copilot Memory's cross-surface rollout — the deletion-scope note was not re-read for this
  claim beyond its title, and no specific claim from it is cited here.

### Claim 12: GitHub Copilot for JetBrains adds Ollama as a BYOK provider, with provider configuration and model selection supported throughout the JetBrains experience
- **Evidence**: Weekly digest "GitHub Copilot for JetBrains" section, second bullet; expanded
  in the linked JetBrains sub-changelog's "Ollama as a BYOK provider" section.
- **Confidence**: settled (product fact stated directly in both the digest and the linked
  changelog)
- **Quote**: "Use local Ollama models in JetBrains with new support for Ollama as a BYOK (bring your own key) provider." (digest); "You can now use Ollama as a BYOK provider in GitHub Copilot for JetBrains. The integration supports provider configuration and model selection throughout the JetBrains experience, giving you another way to work with models that fit your development environment." (linked JetBrains sub-changelog)
- **Our assessment**: This extends, but is distinct from, two prior JetBrains BYOK sources.
  `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` Claim 1 (July 14, 2026) documented
  JetBrains BYOK expanding to "custom, OpenAI-compatible endpoints with API keys, not just named
  providers" — Ollama specifically was not named as a supported provider in that source. This
  August 11 entry is the first corpus documentation of Ollama by name as a JetBrains BYOK
  provider. It also parallels `docs-github-copilot-byok-vscode.md` Claim 2, which named Ollama
  as one of VS Code BYOK's supported local runtimes back in April 2026 — Ollama support is now
  documented on both the VS Code and JetBrains Copilot BYOK surfaces, roughly four months
  apart. Per the VS Code BYOK note's Claim 7, local-runtime BYOK models there "still require the
  Copilot service" and internet connectivity even though the model itself runs locally; this
  JetBrains source does not state whether the same constraint applies to its Ollama
  integration.

### Claim 13: GitHub Copilot for JetBrains adds enterprise "managed settings" — admin server-based controls covering plugin availability, MCP server access, permission bypass behavior, and OpenTelemetry settings
- **Evidence**: Linked JetBrains sub-changelog's "Enterprise managed settings" section (not
  present in the weekly digest itself, which only lists memory and Ollama for JetBrains).
- **Confidence**: settled (product fact stated directly in the linked official changelog)
- **Quote**: "Administrators have more server-based controls for managing GitHub Copilot across their organizations. These enterprise managed settings cover plugin availability, MCP server access, permission bypass behavior, and OpenTelemetry settings."
- **Our assessment**: This is a genuinely new surface, not present in the two-bullet weekly
  digest summary — only reachable by following the "Read the full JetBrains update" link, which
  is exactly the kind of substantive linked sub-page MINER.md §1 requires following. It
  parallels `docs-github-copilot-enterprise-managed-plugins-vscode.md`, whose Claim 2 states the
  VS Code/CLI enterprise plugin baseline "applies uniformly to every user's Copilot CLI and VS
  Code clients" — JetBrains was not named as a covered client in that June 5, 2026 source. This
  entry is the first corpus documentation of an equivalent admin-managed-settings surface
  reaching JetBrains specifically. It also extends
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` Claim 1, which documented
  JetBrains OpenTelemetry configuration as something an individual *practitioner* sets under
  Settings > Tools > GitHub Copilot > Chat — this August source adds OpenTelemetry as one of
  four things an *administrator* can now control server-side instead, a meaningfully different
  governance model (individual opt-in configuration vs. centrally enforced policy) for the
  same underlying capability. The source names four governed categories but does not describe
  the configuration mechanism (e.g., whether it mirrors VS Code/CLI's
  `.github-private/.github/copilot/settings.json` path from the enterprise-managed-plugins
  note, or a JetBrains-specific equivalent), only linking to a separate
  `aka.ms/jetbrains-copilot-enterprise-managed-settings` page that was not fetched for this
  note.

### Claim 14: GitHub Copilot for JetBrains expands Codex agent support — Codex sessions are now visible in agent debug logs, and Codex workflows support updated permission modes and customizations via instructions and skills
- **Evidence**: Linked JetBrains sub-changelog's "Expanded Codex workflows" section (not
  present in the weekly digest itself).
- **Confidence**: settled (product fact stated directly in the linked official changelog)
- **Quote**: "Codex sessions are now visible in agent debug logs. Codex workflows also support updated permission modes and customizations through instructions and skills, helping you adapt agent behavior to your project."
- **Our assessment**: This is the first corpus mention of Codex (OpenAI's coding agent) as a
  supported agent provider inside GitHub Copilot for JetBrains. It extends
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, whose Claim 1 (June 22,
  2026) established Claude as JetBrains' first non-native selectable agent provider in public
  preview and whose summary described JetBrains becoming "a multi-provider agent platform" —
  this source shows that multi-provider framing extending to a third agent vendor (Copilot
  native, Claude, now Codex) rather than being a Claude-specific integration. The word
  "Expanded" in the section heading implies Codex support already existed in some form before
  this entry, but no prior corpus source documents an initial Codex integration in JetBrains to
  confirm what "expanded" is relative to — this is a gap worth flagging for a future source
  note if GitHub's own docs cover Codex-in-JetBrains directly. The phrase "customizations
  through instructions and skills" suggests Codex workflows in JetBrains can be configured with
  the same instructions/skills mechanism used for Copilot's own agent, but the source does not
  confirm file-format compatibility.

### Claim 15: GitHub Copilot for JetBrains can now automatically install Copilot CLI from its integrated terminals on macOS, Linux, and Windows
- **Evidence**: Linked JetBrains sub-changelog's "Easier Copilot CLI setup" section (not
  present in the weekly digest itself).
- **Confidence**: settled (product fact stated directly in the linked official changelog)
- **Quote**: "GitHub Copilot for JetBrains can now automatically install Copilot CLI from integrated terminals on macOS, Linux, and Windows. This reduces setup steps and makes it easier to start using terminal-based agent workflows directly from your IDE."
- **Our assessment**: A straightforward onboarding-friction reduction: previously a
  practitioner using JetBrains would need to separately install Copilot CLI (e.g., via the
  "Install the Copilot CLI" path referenced elsewhere in this digest) before it was usable from
  a JetBrains-integrated terminal. All three major desktop OS families are named explicitly,
  suggesting this is not a partial/platform-limited rollout. No prior corpus source documents
  auto-installation of Copilot CLI from any IDE's integrated terminal.

### Claim 16: VS Code 1.133 lets a practitioner switch between Claude BYOK and built-in Copilot models on a per-turn basis without leaving the active Claude session
- **Evidence**: "VS Code 1.133 Release updates" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog, including the
  "for each new turn" granularity)
- **Quote**: "Switch models without leaving your Claude session by choosing between Claude BYOK and built-in Copilot models for each new turn."
- **Our assessment**: The "for each new turn" detail is the operationally significant part —
  this is not a session-level, restart-required switch but a per-message choice within one
  continuous session. It extends `docs-github-copilot-byok-vscode.md`, which established that
  BYOK models are usable "anywhere in VS Code Chat, including the built-in plan agent and
  custom agents" (that note's Claim 3) but did not describe mid-session, per-turn switching
  between a BYOK model and a built-in one specifically for a *Claude* session. It is also
  conceptually adjacent to JetBrains' multi-provider agent selection
  (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1), though that
  source describes selecting Claude as the agent provider at setup, not switching turn-by-turn
  within a session — VS Code's version is finer-grained. The source does not state whether
  switching models mid-session preserves conversation context/cache the way `/btw`'s side chat
  does (`docs-github-copilot-weekly-releases-aug3-2026.md` Claim 4).

### Claim 17: VS Code 1.133 adds a pinned-prompt feature that keeps the relevant prompt visible while scrolling through long chats
- **Evidence**: "VS Code 1.133 Release updates" section, second bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Stay oriented in long chats by keeping the relevant prompt pinned as you scroll."
- **Our assessment**: A UX/navigation improvement with a clearly stated purpose (staying
  oriented in long conversations) but no further mechanism detail — the source does not say
  whether pinning is automatic (always the most recent prompt) or user-selectable (pin any
  prior prompt), nor whether it applies to the primary chat only or also to side-chat surfaces
  like `/btw` (`docs-github-copilot-weekly-releases-aug3-2026.md` Claim 4). No prior corpus
  source documents a pinned-prompt affordance for any Copilot chat surface.

### Claim 18: VS Code 1.133's integrated browser now reflects HTML changes immediately without requiring a manual refresh
- **Evidence**: "VS Code 1.133 Release updates" section, third bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "See HTML changes immediately without manually refreshing the integrated browser."
- **Our assessment**: This extends the integrated browser's feature line documented in
  `docs-github-copilot-vscode-june-2026.md` (Claim 1: agentic browser tools reached GA and are
  enabled by default) and
  `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 5 (element-level annotation feedback,
  August 3). Prior corpus coverage of the integrated browser focused on agent-facing
  capabilities (tool access, permissions, feedback annotation); this is the first corpus
  mention of a live-reload property specifically for the practitioner's own viewing experience
  of the rendered page — previously, presumably, the practitioner had to manually refresh the
  embedded browser to see the effect of an agent's HTML edit. The source does not state whether
  this applies to CSS/JS changes as well or only literal HTML content.

## Concrete Artifacts

### Full weekly digest — August 10, 2026 (published August 13, 2026), verbatim transcript

Extracted from raw HTML (not AI-summarized WebFetch output) to guarantee verbatim quotes, per
MINER.md §2a and the precedent set in `docs-github-copilot-weekly-releases-aug3-2026.md`
Extraction Note 1.

```
GitHub Copilot weekly releases — August 10
Source: github.blog/changelog, published 2026-08-13, retrieved 2026-08-15
2 minute read

INTRO
  From new models and portable plugins to smoother agent workflows, this
  week's updates make GitHub Copilot more flexible across editors, the
  command line, and the Copilot app.

GITHUB COPILOT, GENERAL
  [Claim 1]
  - Kimi K3 is rolling out to Copilot Pro, Pro+, Max, Business, and
    Enterprise plans.
  [Claim 2]
  - MAI-Code-1.1-Flash is rolling out in GitHub Copilot with native image
    understanding and improvements to coding quality, instruction
    following, tool use, and performance.
  [Claim 3]
  - Build a plugin once and use it across compatible agent tools with
    Agent Plugins 1.0, now generally available in VS Code, Copilot CLI,
    the GitHub Copilot SDK, and the GitHub Copilot app.

GITHUB COPILOT APP
  [Claim 4]
  - Installed plugins are now easier to manage. See each plugin's
    current version, update plugins individually, or update them all at
    once from Customize or Settings.
  [Claim 5]
  - Talk through an agent's question before answering by opening it in a
    side chat while the original question waits for your response.

GITHUB COPILOT CLI
  [Claim 6]
  - Manage all your subagents and their tasks in /tasks.
  [Claim 7]
  - Queue prompts, shell commands, and supported slash commands while an
    agent turn is running.
  [Claim 8]
  - Combine --plan and --mode autopilot in headless mode (-p) to have
    the agent produce a plan and then implement it.
  [Claim 9]
  - Use /rewind to restore Copilot changes without requiring git or
    discarding user edits.
  [Claim 10]
  - /app command now preserves session and folder context when opening
    the Copilot app.

GITHUB COPILOT FOR JETBRAINS
  [Claim 11]
  - Keep useful context across agent chat sessions with Copilot memory,
    so you don't have to repeat the same project details or preferences.
  [Claim 12]
  - Use local Ollama models in JetBrains with new support for Ollama as
    a BYOK (bring your own key) provider.

VS CODE 1.133 RELEASE UPDATES
  [Claim 16]
  - Switch models without leaving your Claude session by choosing
    between Claude BYOK and built-in Copilot models for each new turn.
  [Claim 17]
  - Stay oriented in long chats by keeping the relevant prompt pinned as
    you scroll.
  [Claim 18]
  - See HTML changes immediately without manually refreshing the
    integrated browser.
```

### Linked JetBrains sub-changelog — "Copilot memory and Ollama in GitHub Copilot for JetBrains" (August 11, 2026), verbatim transcript of substantive sections

```
Source: github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains
Retrieved 2026-08-15 via raw HTML (not AI-summarized WebFetch)

INTRO
  This update brings persistent memory, local model access, and more
  enterprise controls to GitHub Copilot for JetBrains. It also improves
  everyday chat workflows and resolves reliability issues across MCP
  servers, terminals, customizations, and cloud agents.

WHAT'S NEW

  Enterprise managed settings [Claim 13]
    Administrators have more server-based controls for managing GitHub
    Copilot across their organizations. These enterprise managed
    settings cover plugin availability, MCP server access, permission
    bypass behavior, and OpenTelemetry settings.
    (links to aka.ms/jetbrains-copilot-enterprise-managed-settings —
    not fetched)

  Copilot memory across chat sessions [Claim 11]
    Copilot memory can now retain and recall useful information across
    agent chat sessions. This helps you maintain context between
    conversations instead of repeatedly providing the same project
    details or preferences.
    You can manage the feature with the Copilot Memory toggle in the
    Copilot settings portal.
    (links to docs.github.com/copilot/concepts/agents/copilot-memory —
    not fetched)

  Ollama as a BYOK provider [Claim 12]
    You can now use Ollama as a BYOK provider in GitHub Copilot for
    JetBrains. The integration supports provider configuration and
    model selection throughout the JetBrains experience, giving you
    another way to work with models that fit your development
    environment.

  Expanded Codex workflows [Claim 14]
    Codex sessions are now visible in agent debug logs. Codex workflows
    also support updated permission modes and customizations through
    instructions and skills, helping you adapt agent behavior to your
    project.

  Easier Copilot CLI setup [Claim 15]
    GitHub Copilot for JetBrains can now automatically install Copilot
    CLI from integrated terminals on macOS, Linux, and Windows. This
    reduces setup steps and makes it easier to start using
    terminal-based agent workflows directly from your IDE.

USER EXPERIENCE ENHANCEMENTS [not independently claimed — see
Extraction Note 3]
  - Account management: Improved account management flows by supporting
    account switch/removal and polishing account-deletion interactions.
  - Model and settings views: Improved model and settings usability by
    capping long model-name width in the model picker and refining
    model view/todo list panel behavior.
  - Chat references: Restored file and folder # references in Copilot,
    Claude, and Codex chat inputs.
  - Customization: Moved the customization button to the top of Copilot
    chat.
  - Agent debug logs: Moved the agent debug logs button to the Options
    dropdown at the top of Copilot chat.

QUALITY IMPROVEMENTS [not independently claimed — see Extraction Note 3]
  This release improves reliability for MCP execution and approvals,
  terminal output and auto-approval, customizations, cloud agents, and
  diff-based editing. It also fixes ANSI escape rendering and makes
  terminal scrollbars more predictable.

CHANGED [not independently claimed — see Extraction Note 3]
  User-facing product strings now use "Copilot" instead of "Copilot
  CLI."
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-weekly-releases-aug3-2026.md`,
`docs-github-copilot-agent-plugins-1-0.md`,
`docs-github-copilot-mai-code-1-flash-more-surfaces.md`,
`docs-github-copilot-byok-vscode.md`,
`docs-github-copilot-memory-user-preferences.md`,
`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`,
`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`,
`docs-github-copilot-jetbrains-otel-model-management-july2026.md`,
`docs-github-copilot-enterprise-managed-plugins-vscode.md`, and
`docs-github-copilot-vscode-june-2026.md` were re-read directly in those notes
(via `### Claim N:` headings) before citing, per MINER.md §4b; claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates** `docs-github-copilot-agent-plugins-1-0.md` (Claim 3, Agent Plugins 1.0 GA
  across VS Code/CLI/SDK/App): Claim 3 of this note is a one-day-later restatement of the same
  GA fact, with no new detail.

- **Corroborates** `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 10, `/rewind`):
  Claim 9 of this note restates the same `/rewind` capability (Git-independent restoration,
  preserves the user's own subsequent edits) one week later with slightly different wording,
  flagged in Claim 9's "Our assessment" as most likely repeated messaging rather than a
  distinct product change.

- **Extends** `docs-github-copilot-mai-code-1-flash-more-surfaces.md` (Claim 2, individual-tier
  rollout with Business/Enterprise pending): Claim 2 of this note documents a later point
  release (MAI-Code-1.1-Flash) adding native image understanding, without confirming whether
  Business/Enterprise availability has caught up.

- **Extends** `docs-github-copilot-agent-plugins-1-0.md` (Scope section's documented gap in
  Copilot-app/CLI plugin-management UI coverage): Claim 4 of this note documents the Copilot
  app's plugin version/update UI specifically, partially filling that gap.

- **Extends and contrasts with** `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 2,
  `/side`) and `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim 6,
  Markdown-rendered ask-user prompts): Claim 5 of this note is a related-but-distinct
  "side-conversation about the agent's own question" feature, contrasted against both in its
  "Our assessment."

- **Extends** `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 8, Sessions sidebar):
  Claim 6 of this note (`/tasks`) manages subagents within a session, distinct from the
  Sessions sidebar's cross-session management.

- **Extends** `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 4,
  in-flight message queuing with three interrupt modes): Claim 7 of this note documents a
  parallel queueing capability on the standalone Copilot CLI surface, with less granularity
  specified than the JetBrains-embedded version.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 10, "Autopilot" permission-level
  naming): Claim 8 of this note (`--mode autopilot` in CLI headless mode) is a second Copilot
  surface using the "Autopilot" name for unattended agent execution.

- **Extends** `docs-github-copilot-memory-user-preferences.md` (Claim 1 scope, Claim 4
  management interface, Claim 5 Pro/Pro+ early-access gating): Claim 11 of this note documents
  Copilot Memory reaching the JetBrains surface, with a matching management-toggle description
  but no statement on whether the Pro/Pro+ plan gating still applies.

- **Extends** `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 1, custom
  OpenAI-compatible BYOK endpoints) and **extends** `docs-github-copilot-byok-vscode.md`
  (Claim 2, Ollama named as a VS Code BYOK local runtime): Claim 12 of this note is the first
  corpus documentation of Ollama by name as a JetBrains BYOK provider, roughly four months
  after Ollama's VS Code BYOK debut.

- **Extends** `docs-github-copilot-enterprise-managed-plugins-vscode.md` (Claim 2, baseline
  applying to "every user's Copilot CLI and VS Code clients") and
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim 1,
  practitioner-configurable OpenTelemetry settings): Claim 13 of this note documents an
  admin-controlled managed-settings surface reaching JetBrains for the first time, and shifts
  OpenTelemetry configuration for JetBrains from individual opt-in to a category an
  administrator can also control centrally.

- **Extends** `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 1,
  Claude as JetBrains' first non-native agent provider, "multi-provider agent platform"
  framing): Claim 14 of this note shows that multi-provider framing extending to a third named
  agent vendor, Codex.

- **Extends** `docs-github-copilot-byok-vscode.md` (Claim 3, BYOK availability "anywhere in
  VS Code Chat") and **is conceptually adjacent to**
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 1, agent-provider
  selection at setup): Claim 16 of this note adds per-turn model switching within one Claude
  session, a finer granularity than either prior source describes.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 1, agentic browser tools GA) and
  `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 5, element-level browser feedback):
  Claim 18 of this note adds a live-reload property for the practitioner's own view of the
  rendered page, distinct from both sources' agent-facing browser capabilities.

- **Contradicts**: None identified. The `/rewind` wording delta noted under Claim 9 ("restore
  the conversation and files" in the August 3 source vs. "restore Copilot changes" here) is
  flagged as a possible scope narrowing but is not filed as a contradiction — both sources
  agree on the two load-bearing facts (Git-independence, preservation of the user's own
  subsequent edits) and lead to the same guide advice either way, consistent with the
  no-contradiction-filed precedent set for the analogous color-mode wording delta in
  `docs-github-copilot-cli-terminal-ga.md`.

- **Novel**:
  - First corpus documentation of Kimi K3 as a GitHub Copilot model-roster addition (Claim 1).
  - First corpus documentation of Copilot CLI's `/tasks` subagent-management command (Claim 6).
  - First corpus documentation of Copilot CLI's headless (`-p`) mode and its
    `--plan`/`--mode autopilot` combination (Claim 8).
  - First corpus documentation of a Copilot CLI `/app` command bridging to the standalone app
    with context preservation (Claim 10).
  - First corpus documentation of an enterprise "managed settings" admin-control surface
    reaching GitHub Copilot for JetBrains (Claim 13).
  - First corpus documentation of Codex (OpenAI's agent) as a supported provider inside GitHub
    Copilot for JetBrains (Claim 14).
  - First corpus documentation of IDE-integrated-terminal auto-installation of Copilot CLI
    (Claim 15).
  - First corpus documentation of per-turn (not per-session) model switching in VS Code Chat
    (Claim 16).
  - First corpus documentation of a pinned-prompt UX affordance in any Copilot chat surface
    (Claim 17).

## Guide Impact

### Chapter 01: Daily Workflows

- **Pinned prompts for long chats**: Document VS Code's pinned-prompt feature (Claim 17) as a
  navigation aid for practitioners running long-lived agent conversations.
- **Live integrated-browser reload**: Add the integrated browser's immediate HTML-change
  reflection (Claim 18) as a reason practitioners no longer need to manually refresh after an
  agent's front-end edit.
- **CLI `/app` and cross-surface continuity**: Document `/tasks` (Claim 6), CLI-active-turn
  queueing (Claim 7), and `/app` context preservation (Claim 10) together as this week's theme
  of deepening session continuity and multi-surface handoff within Copilot CLI, rather than as
  three unrelated features.

### Chapter 02: Harness Engineering

- **Headless CLI planning mode**: Document `--plan` + `--mode autopilot` in Copilot CLI's `-p`
  headless mode (Claim 8) as a scriptable "produce a plan, then implement it unattended"
  pattern, and note the "Autopilot" naming now spans both the VS Code Agents window permission
  level and Copilot CLI's headless mode.
- **Plugin management UI, Copilot app surface**: Add the Copilot app's per-plugin
  version/update UI (Claim 4) to the corpus's plugin-management coverage, alongside the
  existing VS Code-focused documentation in `docs-github-copilot-agent-plugins-1-0.md`.
- **JetBrains Ollama BYOK**: Add Ollama as a named JetBrains BYOK provider (Claim 12) to the
  guide's model-provider configuration options for JetBrains users.

### Chapter 04: Agentic Workflows — Multi-Session, Correction, and Provider Selection

- **Subagent task management (`/tasks`)**: Document Copilot CLI's `/tasks` command (Claim 6)
  as the within-session complement to the cross-session Sessions sidebar.
- **Per-turn model switching**: Add VS Code's Claude BYOK / built-in per-turn model switching
  (Claim 16) as the finest-grained model-selection mechanism documented so far in the corpus,
  distinct from session-start provider selection (JetBrains) or app/repo-level model auto
  selection.
- **`/rewind` repeated messaging**: Note in the guide's correction-patterns section that
  GitHub re-announced `/rewind` in back-to-back weekly digests (August 3 and August 10) with
  slightly different wording — treat this as reinforcement of the same capability documented
  from the August 3 source, not evidence of a second, distinct change, unless a future source
  clarifies the wording delta.
- **Multi-provider JetBrains platform now includes Codex**: Update the JetBrains
  multi-provider-agent guidance to include Codex (Claim 14) alongside native Copilot and
  Claude.

### Chapter 05: Team Adoption — Enterprise Governance

- **JetBrains enterprise managed settings**: Add JetBrains to the guide's enterprise
  Copilot-governance checklist (Claim 13) — administrators can now centrally control plugin
  availability, MCP server access, permission bypass behavior, and OpenTelemetry export for
  JetBrains specifically, shifting OpenTelemetry from an individual practitioner setting
  (per `docs-github-copilot-jetbrains-otel-model-management-july2026.md`) to an
  admin-governable one as well.
- **Kimi K3 model-roster addition**: Note Kimi K3's simultaneous rollout to individual and
  Business/Enterprise plans (Claim 1) for teams tracking which third-party models are
  available under their Copilot license tier.

## Extraction Notes

1. **WebFetch discarded in favor of raw HTML, per established corpus precedent**: Following
   the precedent in `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 1 (which
   found WebFetch fabricated an entire "Related Updates" list not present in the source) and
   `docs-github-copilot-agent-plugins-1-0.md` Extraction Notes, both the primary weekly-digest
   URL and the linked JetBrains sub-changelog URL were fetched as raw HTML via `curl` with a
   browser user-agent, then converted to plain text by isolating the `<article>` element,
   converting block-level tags to line breaks, and stripping remaining markup — producing a
   verbatim transcript of every heading and bullet in both articles. Every `Quote` field above
   was checked by exact substring match (whitespace-normalized only) against these transcripts,
   preserving original curly-quote punctuation (e.g., "plugin’s", "agent’s", "don’t").
   An initial WebFetch pass was also run on the primary digest URL for orientation; comparing
   its output against the raw-HTML transcript found it consistently paraphrased every bullet
   (e.g., "Subagent task management via /tasks command" for the actual "Manage all your
   subagents and their tasks in /tasks.") without inventing new content this time — but none of
   its paraphrased text was used in any Quote field, per MINER.md §2a.
2. **JetBrains sub-changelog followed as a substantive linked page**: Per MINER.md §1, the "Read
   the full JetBrains update" link was followed because the weekly digest condenses it to two
   bullets (memory, Ollama) while the linked page contains three additional substantive "What's
   new" sections (enterprise managed settings, Codex workflows, easier CLI setup) plus UX and
   quality-improvement notes — all extracted as Claims 11-15 above. No other linked page from
   either article was followed: the general VS Code 1.133 release notes (`aka.ms/VSCode/133`)
   are not Copilot-specific (same judgment call as the August 3 note's Extraction Note 2); the
   two "Try the Copilot app" / "Install the Copilot CLI" links are marketing/download pages, not
   documentation; and the JetBrains sub-changelog's own two outbound links
   (`aka.ms/jetbrains-copilot-enterprise-managed-settings` and
   `docs.github.com/copilot/concepts/agents/copilot-memory`) were not fetched — the changelog
   text itself provided enough detail for Claims 11 and 13, and following two further pages
   would have exceeded a reasonable scope for a weekly-digest-level source note without a
   specific signal (e.g., Prospector guidance) that deeper JetBrains-admin documentation was
   required.
3. **Several bullets not given dedicated claims**: The JetBrains sub-changelog's "User
   experience enhancements" section (five bullets: account management, model/settings views,
   chat references, customization button placement, agent debug logs button placement), its
   one-line "Quality improvements" summary, and its one-line "Changed" note (UI string rename
   from "Copilot CLI" to "Copilot") are all thin polish/reliability items with no measurable
   detail, mechanism, or novel capability — consistent with how
   `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 3 handled the Copilot
   app's bare "sessions start and switch more efficiently" bullet. All are preserved verbatim
   in Concrete Artifacts for corpus completeness rather than given individual Claim entries.
4. **No contradictions identified; one wording delta flagged but not filed**: Cross-referencing
   against ten existing source notes found no claim in this source that materially opposes an
   existing corpus position leading to different guide advice. The one wording difference
   worth flagging — `/rewind`'s "restore the conversation and files" (August 3 digest) vs.
   "restore Copilot changes" (this source, August 10 digest) — is discussed in Claim 9 and the
   Cross-References section but does not meet MINER.md §4a's bar for filing a contradiction
   issue, since both readings lead to identical guide advice (Git-independent restoration that
   preserves the user's own subsequent edits) and the delta is at least as plausibly loose
   restatement as an intentional scope change.
5. **Codex-in-JetBrains has no prior corpus baseline**: Claim 14's "Expanded Codex workflows"
   heading implies a pre-existing Codex integration in JetBrains, but no source note in this
   corpus documents an initial Codex-in-JetBrains launch to compare against. This is flagged as
   a genuine corpus gap rather than resolved by inference — a future source (a GitHub changelog
   entry or docs page specifically introducing Codex as a JetBrains agent provider) would let a
   subsequent Miner pass establish the "before" state this entry's "expanded" is relative to.
