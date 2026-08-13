---
source_url: https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app
source_type: docs
title: "Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot app"
author: GitHub (official changelog)
date_published: 2026-08-12
date_extracted: 2026-08-13
last_checked: 2026-08-13
status: current
confidence_overall: settled
issue: "#2668"
---

# Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot App

> GitHub's August 12, 2026 changelog documents general availability of Agent Plugins 1.0
> — a cross-vendor open standard (co-published with AWS, Anysphere, Microsoft, OpenAI,
> Vercel, and Google) that packages agent skills and MCP servers into one installable
> plugin governed independently of any single vendor. VS Code's implementation notably
> recognizes both GitHub Copilot's and Anthropic's Claude plugin manifest formats
> alongside the new standard, and existing enterprise governance controls
> (`enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces` in
> `managed-settings.json`) extend to the new standard without a separate policy.

## Source Context

- **Type**: docs (GitHub official product changelog, August 12, 2026; ~2-minute read,
  tagged `copilot`). Three linked documentation pages were followed per MINER.md §1,
  fetched as raw HTML via `curl` (not through AI-summarizing WebFetch, to keep quotes
  verbatim — see Extraction Notes): the VS Code docs page "Agent plugins in VS Code"
  (`code.visualstudio.com/docs/agent-customization/agent-plugins`), the GitHub Docs page
  "About GitHub Copilot plugins" (`docs.github.com/copilot/concepts/agents/about-plugins`),
  and the spec-authoring guide "Build an Agent Plugin"
  (`agent-plugins.org/plugin-authors`). Two further linked pages (the raw spec markdown on
  GitHub, and the team-specific-overrides doc subsection already covered by
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`) were not
  fetched — see Extraction Notes.
- **Author credibility**: GitHub engineering team announcing a production, generally
  available (not preview) cross-vendor standard, in collaboration with named co-publishers
  (AWS, Anysphere — maker of Cursor — Microsoft, OpenAI, Vercel) and Google as a core
  maintainer. Authoritative for: the standard's existence, GA status, supported clients,
  manifest/schema mechanics, and the enterprise governance integration. The VS Code and
  GitHub Docs pages are first-party product documentation for their respective clients and
  are authoritative for client-specific behavior (format auto-detection, capability
  matrices, default marketplaces). The `agent-plugins.org` page is the standard's own
  authoring guide and is authoritative for the portable spec mechanics, but is not a
  GitHub source — it defines the vendor-neutral floor that GitHub's clients implement.
  None of these sources provide independent/critical evaluation (e.g., security review of
  the plugin execution model, adoption data, or comparison of migration friction against
  vendor claims) — this is vendor self-reporting of a feature launch, not a third-party
  assessment.
- **Scope**: Covers the Agent Plugins 1.0 standard's launch, the manifest-migration path
  for existing plugin authors, the portable vs. client-specific capability split, VS
  Code's multi-format auto-detection (Agent Plugins 1.0, Copilot, Claude, legacy
  OpenPlugin), the minimal plugin package structure and discovery process, and how
  existing enterprise managed-settings controls extend to the new standard. Does NOT
  cover: adoption numbers, how conflicts between multiple installed plugins claiming the
  same skill/agent name are resolved, the full JSON Schema for `plugin.json` beyond the
  fields shown in examples, independent security analysis of plugin-bundled MCP servers
  or hooks (the VS Code doc's caution note is the only security framing given), or
  Copilot CLI/cloud-agent-specific UI for plugin management (only VS Code's UI is
  documented in the sources fetched).

## Extracted Claims

### Claim 1: Agent Plugins 1.0 is a cross-vendor open standard published August 6, 2026, with AWS, Anysphere, Microsoft, OpenAI, and Vercel, and Google joined the same day as a core maintainer
- **Evidence**: Stated directly in the changelog body as a factual announcement, naming the co-publishing companies.
- **Confidence**: settled
- **Quote**: "We published Agent Plugins 1.0 on August 6 with AWS, Anysphere, Microsoft, OpenAI, and Vercel. Google also joined as a core maintainer on the same day."
- **Our assessment**: The specific, named multi-vendor list (including Anysphere, maker of the competing Cursor editor, and Google as a "core maintainer" rather than just a co-signer) is the most notable fact in this source — it signals plugin packaging is being treated as neutral infrastructure rather than a GitHub-owned lock-in mechanism. This is a stronger interoperability claim than typical single-vendor "open format" announcements and is corroborated by VS Code's own docs recognizing Anthropic's Claude plugin format (Claim 6).

### Claim 2: Agent Plugins 1.0 packages agent skills and MCP servers into one installable plugin, governed independently of any single vendor
- **Evidence**: Direct definitional quote from the changelog's overview section.
- **Confidence**: settled
- **Quote**: "Agent Plugins 1.0 is an open standard that packages agent skills and MCP servers into one installable plugin that is governed independently of any single vendor."
- **Our assessment**: This is the standard's own self-description of scope: it standardizes exactly two component types (skills, MCP servers) and explicitly leaves everything else (agents, hooks, slash commands) as client-specific extensions (Claim 8). That's a narrower "portable core" than a full plugin system — a deliberate design choice, not an oversight, per the authoring guide's "Client-managed installation, distribution, enablement, updates, and user interface are outside the portable specification."

### Claim 3: Support for Agent Plugins 1.0 is generally available (not preview) across VS Code, Copilot CLI, the GitHub Copilot SDK, and the GitHub Copilot app, on all Copilot plans
- **Evidence**: Direct statement in the changelog.
- **Confidence**: settled
- **Quote**: "Support is generally available in VS Code, Copilot CLI, the GitHub Copilot SDK, and the GitHub Copilot app, on all Copilot plans."
- **Our assessment**: Notable that this shipped as GA rather than preview/experimental — contrasts with several prior enterprise plugin-governance features in this corpus that launched as public preview (e.g. `docs-github-copilot-enterprise-managed-plugins-vscode.md`, `docs-github-copilot-enterprise-strict-known-marketplaces.md`). The underlying enterprise distribution mechanism had already been through two months of preview iteration before the cross-vendor standard itself went GA on day one, which is a reasonable de-risking sequence.

### Claim 4: Migrating an existing plugin to the 1.0 spec is described as "mostly manifest work" — three concrete file/directory changes
- **Evidence**: Changelog's "Building or migrating a plugin" section lists the specific manifest changes required.
- **Confidence**: settled
- **Quote**: "If you maintain a plugin, adopting the spec is mostly manifest work: Add $schema to plugin.json[;] Keep skills under skills/ and MCP configuration in mcp.json[;] Move Copilot-specific files into the com.github.copilot/ directory, which other clients ignore"
- **Our assessment**: Low-friction migration path is plausible given the changes are additive (new namespaced directory) rather than restructuring. The `com.github.copilot/` reverse-domain namespace directory is the mechanism that lets one package serve both the portable standard and Copilot-specific extras (custom agents, commands, rules, hooks, canvases) without breaking non-Copilot clients — other clients are documented to simply ignore directories they don't recognize (Claim 8's "VS Code currently ignores client extension data and directories in Agent Plugins 1.0 packages").

### Claim 5: Existing GitHub Copilot plugins that don't target Agent Plugins 1.0 remain supported, with no required migration
- **Evidence**: Explicit backward-compatibility statement in the changelog's "What you can do" section.
- **Confidence**: settled
- **Quote**: "Keep your existing plugins. Existing GitHub Copilot plugins that don't target Agent Plugins 1.0 remain supported, with no migration required."
- **Our assessment**: Standard vendor practice for a format transition — avoids stranding existing plugin authors. Consistent with VS Code's docs (Claim 6), which show the client auto-detecting four distinct manifest formats simultaneously (Agent Plugins 1.0, Copilot, Claude, legacy OpenPlugin) rather than requiring a hard cutover.

### Claim 6: VS Code auto-detects and supports four distinct plugin manifest formats by manifest file location, including Anthropic's Claude plugin format
- **Evidence**: VS Code's own documentation table listing format-detection rules by manifest path.
- **Confidence**: settled
- **Quote**: "Through its existing Copilot and Claude plugin formats, VS Code also supports client-specific plugin capabilities, including slash commands, custom agents, and hooks."
- **Our assessment**: This is the single most novel fact in the source relative to our corpus: VS Code's plugin loader treats `.claude-plugin/plugin.json` (Claude's format) as a first-class, directly supported manifest location alongside GitHub's own `plugin.json` and the new Agent Plugins 1.0 root `plugin.json`, plus a "Legacy OpenPlugin" format at `.plugin/plugin.json`. No existing note in this corpus documents cross-vendor plugin-format recognition inside a single client; this is direct evidence that at least one major IDE (VS Code, via GitHub Copilot's extension) is voluntarily reading a competing/adjacent vendor's plugin manifest format rather than requiring authors to publish separately for each client.

### Claim 7: Agent Plugins 1.0 defines only skills and MCP servers as portable component types; agents, hooks, and slash commands are client-specific via reverse-domain "client extension namespaces"
- **Evidence**: VS Code documentation's capability table, distinguishing "Standard" (portable) vs. "Client-specific" columns for five capability types.
- **Confidence**: settled
- **Quote**: "Agent Plugins 1.0 defines skills and MCP servers as portable component types. Other capabilities are client-specific and can use the standard's reverse-domain client extension namespaces. VS Code currently ignores client extension data and directories in Agent Plugins 1.0 packages."
- **Our assessment**: This confirms the "portable core, extensible edges" design read from Claim 2 and Claim 4. It also flags a real limitation: a plugin's custom agents, hooks, and slash commands do NOT travel across clients today even under the 1.0 standard — only skills and MCP servers do. A plugin author targeting VS Code, Copilot CLI, and a third client (e.g., Claude Code) for agent/hook behavior specifically would still need per-client namespaced directories, not a single portable definition.

### Claim 8: A minimal Agent Plugin requires only a root `plugin.json` with `$schema` and `name`, plus an optional `skills/<skill>/SKILL.md`; discovery walks immediate children of `skills/` and validates each against the Agent Skills spec
- **Evidence**: The standard's own authoring guide (`agent-plugins.org/plugin-authors`), showing the minimal file tree and manifest JSON.
- **Confidence**: settled
- **Quote**: "A skills-capable client loads plugin.json, discovers the immediate children of skills/, and validates each SKILL.md against the Agent Skills specification."
- **Our assessment**: This ties Agent Plugins 1.0 explicitly to the pre-existing Agent Skills spec as a dependency rather than reinventing skill packaging — plugins are a distribution wrapper around already-standardized skills plus a new MCP-server bundling convention. Consistent with the "packages agent skills and MCP servers" framing in Claim 2.

### Claim 9: The portable spec enforces a package-boundary security constraint — plugin-declared file paths must resolve within the plugin root, and symlinks may not escape the package
- **Evidence**: Direct constraint text from the authoring guide's "Package boundaries" section.
- **Confidence**: settled
- **Quote**: "Files supplied by the package must resolve within the plugin root. Configuration fields defined as plugin-relative paths begin with ./; symlinks and equivalent filesystem mechanisms must not be used to escape the package."
- **Our assessment**: This is a genuine, spec-level supply-chain safeguard against a plausible attack (a malicious or compromised plugin using `../` traversal or a symlink to read/write files outside its own directory when installed by a client). It's a narrow guarantee, though: it constrains what paths a *conformant* manifest can declare, not what a plugin's bundled MCP server or hook script can do once it executes — the VS Code docs' separate caution note (Claim 10) makes clear that runtime code execution risk remains a user-review responsibility, not something the spec closes off.

### Claim 10: VS Code explicitly warns that plugins can include hooks and MCP servers that run code on the user's machine, and recommends reviewing plugin contents and publisher before installing, especially from community marketplaces
- **Evidence**: A dedicated "Caution" callout in the VS Code documentation.
- **Confidence**: settled
- **Quote**: "Plugins can include hooks and MCP servers that run code on your machine. Review the plugin contents and publisher before installing, especially for plugins from community marketplaces."
- **Our assessment**: This is GitHub/Microsoft's own acknowledgment that the plugin trust model is currently "review before install," not sandboxed-by-default execution — the same class of supply-chain risk documented for MCP servers generally in `docs-github-copilot-mcp-allowlists-enterprise.md`. It directly motivates why enterprise `strictKnownMarketplaces`/`enabledPlugins` governance (Claim 11) matters for organizations that can't rely on individual developers doing this review consistently.

### Claim 11: Enterprise `managed-settings.json` governance (`enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`) applies uniformly to Agent Plugins 1.0 across VS Code, Copilot CLI, the Copilot app, and Copilot cloud agent, with no separate policy required
- **Evidence**: Changelog's "Govern plugins with the settings you already use" section, stating the existing enterprise mechanism extends automatically.
- **Confidence**: settled
- **Quote**: "If you already manage these plugin settings for supported Copilot clients, they also apply to Agent Plugins 1.0. No separate Agent Plugins policy is required."
- **Our assessment**: This is a meaningful governance claim: it means organizations that already configured plugin allowlisting via the settings documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md` (June 5), `docs-github-copilot-enterprise-strict-known-marketplaces.md` (June 25), and the `overridable` team-specific model in `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (August 3) get Agent Plugins 1.0 coverage automatically at the format's GA launch, rather than needing a new policy rollout. This is consistent, incremental extension of one governance system rather than a parallel one — a positive signal for reducing enterprise admin overhead, though it also means any gaps or bugs in that existing system (not evaluated by this source) now apply to the new standard too.

### Claim 12: The changelog explicitly directs pairing plugin governance with MCP allowlists, since plugins can carry MCP server configurations
- **Evidence**: Direct cross-reference sentence in the changelog's governance section.
- **Confidence**: settled
- **Quote**: "Plugins can also carry MCP server configurations, so pair this with MCP allowlists, which approve or block individual servers by URL, command, or name."
- **Our assessment**: This confirms plugin-level allowlisting (which plugins can install) and server-level allowlisting (which MCP servers can run, regardless of source) are separate, complementary controls — a plugin passing `enabledPlugins`/`strictKnownMarketplaces` governance does not automatically mean its bundled MCP server passes `allowedMcpServers`/`deniedMcpServers` governance from `docs-github-copilot-mcp-allowlists-enterprise.md`. Organizations relying on only one of the two controls would have a gap.

### Claim 13: GitHub Copilot's own (non-standard) plugin format supports five component types with specific file/directory conventions that differ in several respects from the Agent Plugins 1.0 layout
- **Evidence**: GitHub Docs "About GitHub Copilot plugins" page, listing component types and their file locations.
- **Confidence**: settled
- **Quote**: "Custom agents — Specialized AI assistants (*.agent.md files in agents/)[;] Skills — Discrete callable capabilities (skills subdirectories in skills/, containing a SKILL.md file)[;] Hooks — Event handlers that intercept agent behavior (a hooks.json file in the plugin root, or in hooks/)[;] MCP server configurations — Model Context Protocol integrations (a .mcp.json file in the plugin root, or an mcp.json file in .github/)[;] LSP server configurations — Language Server Protocol integrations (an lsp.json file in the plugin root, or in .github/)"
- **Our assessment**: Note the naming/location mismatch this creates in practice: the portable Agent Plugins 1.0 standard uses `mcp.json` at the plugin root (Claim 8), while GitHub's own native Copilot plugin format uses `.mcp.json` (leading dot) at the root or `mcp.json` under `.github/`. This is exactly the kind of divergence the `com.github.copilot/` namespace directory (Claim 4) and per-client format auto-detection (Claim 6) exist to paper over — but it also means a plugin author reading only one of the two doc sets could easily use the wrong filename for their target client.

### Claim 14: VS Code's default plugin marketplaces are `copilot-plugins` and `awesome-copilot`, configurable via the `chat.plugins.marketplaces` setting, with plugin support togglable via `chat.plugins.enabled`
- **Evidence**: VS Code documentation's marketplace/configuration section.
- **Confidence**: settled
- **Quote**: "Enable or disable support for agent plugins with the chat.plugins.enabled setting."
- **Our assessment**: Confirms the "Awesome Copilot marketplace" referenced in the changelog (Claim 3's "Install spec plugins from a marketplace... available by default in VS Code, Copilot CLI, and the Copilot app") is a specific, named default repository rather than a generic description, and that marketplace membership itself is configurable — relevant to the `extraKnownMarketplaces`/`strictKnownMarketplaces` enterprise controls (Claim 11), which act on exactly this configuration surface.

## Concrete Artifacts

Minimal `plugin.json` manifest for Agent Plugins 1.0 (from `agent-plugins.org/plugin-authors`, the standard's authoring guide):
```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "hello-plugin"
}
```

Minimal skill file `skills/greet/SKILL.md` (from the same authoring guide):
```markdown
---
name: greet
description: Greet the user and offer help.
---

Greet the user and offer help.
```

Minimal portable plugin directory layout (from `agent-plugins.org/plugin-authors`):
```
hello-plugin/
├── plugin.json
└── skills/
    └── greet/
        └── SKILL.md
```

Example VS Code plugin layout mixing portable and client-specific components (from `code.visualstudio.com/docs/agent-customization/agent-plugins`):
```
my-testing-plugin/
  plugin.json              # Plugin metadata and configuration
  skills/
    test-runner/
      SKILL.md              # Testing skill instructions
      run-tests.sh           # Supporting script
  agents/
    test-reviewer.agent.md  # Code review agent
  hooks/
    hooks.json               # Hook configuration
    scripts/
      validate-tests.sh      # Hook script
  .mcp.json                  # MCP server definitions
```

Example GitHub Copilot native plugin layout (from `docs.github.com/copilot/concepts/agents/about-plugins`):
```
my-plugin/
├── plugin.json           # Required manifest
├── agents/               # Custom agents (optional)
│   └── helper.agent.md
├── skills/               # Skills (optional)
│   └── deploy/
│       └── SKILL.md
├── hooks.json            # Hook configuration (optional)
├── .mcp.json             # MCP server config (optional)
└── lsp.json              # LSP server config (optional)
```

Sample richer `plugin.json` with optional metadata fields (from the VS Code documentation):
```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "my-dev-tools",
  "description": "React development utilities",
  "version": "1.2.0"
}
```

VS Code's plugin-format auto-detection rules, by manifest location (from `code.visualstudio.com/docs/agent-customization/agent-plugins`):
- Agent Plugins 1.0: root `plugin.json` with canonical `$schema`
- Copilot: standard `plugin.json`
- Claude: `.claude-plugin/plugin.json`
- Legacy OpenPlugin: `.plugin/plugin.json`

## Cross-References

- **Corroborates**: `docs-github-copilot-mcp-allowlists-enterprise.md` — this source's "pair this with MCP allowlists" instruction (Claim 12) directly reinforces that note's claim that MCP server governance is a distinct, fail-closed control layered on top of (not replaced by) plugin/marketplace governance.
- **Contradicts**: None identified. No existing corpus note claims plugin formats are single-vendor-locked or that portable cross-client packaging was unavailable before this launch, so there is no direct conflict — this source instead fills a documented gap (see Novel, below).
- **Extends**: `docs-github-copilot-enterprise-managed-plugins-vscode.md` (June 5, 2026 — the original enterprise-managed plugin distribution preview for VS Code, predating the open standard) and `docs-github-copilot-enterprise-strict-known-marketplaces.md` (June 25, 2026 — introduced `strictKnownMarketplaces`) are both extended: this source confirms (Claim 11) that the governance surface those notes describe now covers Agent Plugins 1.0 packages automatically. `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (August 3, 2026 — `overridable` team-level settings) is likewise extended, since plugin/marketplace keys are named examples of the additive-override model that note documents. `docs-github-copilot-mcp-allowlists-enterprise.md` (August 6, 2026 — same day as the Agent Plugins 1.0 spec publication) is extended by the explicit plugin-vs-MCP-allowlist pairing in Claim 12.
- **Novel**: The cross-vendor co-publication itself (Claim 1: AWS, Anysphere, Microsoft, OpenAI, Vercel, Google) is new to this corpus — prior source notes in this family document GitHub-only enterprise plugin governance, not an industry-wide packaging standard. Most notably, VS Code's direct recognition of Anthropic's Claude plugin manifest format (`.claude-plugin/plugin.json`) alongside GitHub's own and the new standard (Claim 6) is the first documented instance in this corpus of one vendor's IDE client natively reading another vendor's agent-plugin format. The package-boundary path-traversal/symlink constraint (Claim 9) and the "portable core is only skills + MCP servers, everything else is client-specific" design split (Claim 7) are also new specifics not covered by the earlier enterprise-governance notes, which focused on distribution/allowlisting rather than the plugin package format itself.

## Guide Impact

- **Chapter on harness/IDE extensibility (Ch02 per triage)**: Add Agent Plugins 1.0 as a concrete example of cross-vendor standardization of agent tooling packaging — specifically the "portable core (skills + MCP servers) vs. client-specific extension namespace" design pattern (Claim 7), which is a reusable architectural lesson for anyone designing a plugin/extension system that needs to span multiple AI coding tools. Cite the VS Code multi-format auto-detection (Claim 6) as evidence that IDE vendors are willing to read competitors' manifest formats when the cost of doing so is low (a JSON file at a known path) — useful context for any recommendation about betting on a single vendor's extension format vs. a portable one.
- **Chapter on agentic workflows / plugin ecosystem (Ch04 per triage)**: The manifest-migration mechanics (Claim 4: add `$schema`, move vendor-specific files to a namespaced directory) are a concrete, low-friction example of an additive migration path that keeps one package working across multiple clients — worth citing if the guide discusses how to structure a shareable skill/tool package that needs to serve more than one agent runtime.
- **Chapter on governance / team adoption of third-party agent plugins (Ch05 per triage)**: Two things worth adding: (1) the explicit, vendor-stated caution that plugins can execute arbitrary code via hooks and MCP servers with only a "review before install" trust model (Claim 10) — this belongs in any discussion of supply-chain risk for AI-agent extensibility; (2) the fact that existing enterprise `managed-settings.json` governance now covers the new standard automatically (Claim 11), which is a positive example of a governance mechanism designed to extend rather than require reconfiguration for new capability launches — useful if the guide recommends how organizations should structure their own AI-tooling governance to anticipate future format changes.

## Extraction Notes

- The primary changelog page and all three linked pages that were followed
  (`code.visualstudio.com/docs/agent-customization/agent-plugins`,
  `docs.github.com/copilot/concepts/agents/about-plugins`, and
  `agent-plugins.org/plugin-authors`) were fetched as raw HTML via `curl` with a
  browser user-agent and converted to plain text with a Python script that strips
  tags, rather than via AI-summarizing WebFetch. This was done specifically so every
  quoted passage above could be verified character-for-character against the actual
  page text, per MINER.md §2a. An initial WebFetch pass on the changelog page was
  also run for orientation, but its output was discarded in favor of the raw-HTML
  extraction once quote-verification concerns surfaced; none of its (summarized,
  non-verbatim) text was used in the Quote fields above.
- Two links visible in the changelog's raw HTML were not followed: the raw
  `agent-plugins-spec/blob/main/spec/1.0.0.md` file on GitHub (the full formal spec
  — out of scope for a changelog-level source note; would be a good candidate for
  its own future source-note issue if the guide needs spec-level detail), and the
  `docs.github.com/.../configure-enterprise-managed-settings#overriding-settings-for-specific-teams`
  anchor, which resolves to the same team-override mechanism already extracted in
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`.
  `docs.github.com/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing`
  (linked as "Finding and installing plugins in Copilot CLI guide") was also not
  fetched — the VS Code and general "About GitHub Copilot plugins" pages already
  supplied client-behavior detail, and CLI-specific installation UX did not seem
  load-bearing enough to justify a fifth fetch for this note's scope.
- The three Prospector triage comments on the source issue disagreed on which
  existing notes overlap with this one (one listed `docs-github-copilot-enterprise-managed-plugins-vscode.md`
  and `docs-github-copilot-vscode-june-2026.md`; a second listed `docs-ghaw-how-they-work.md`
  and `docs-github-copilot-cli-security-review.md`; a third said no overlapping notes
  exist at all). Independent review of the actual corpus (see Cross-References) found
  the first comment's `docs-github-copilot-enterprise-managed-plugins-vscode.md`
  suggestion correct and load-bearing, but `docs-github-copilot-vscode-june-2026.md`
  does not mention plugins and was not used. The second comment's two suggestions
  (`docs-ghaw-how-they-work.md`, about the unrelated GitHub Agentic Workflows /
  `gh aw` product, and `docs-github-copilot-cli-security-review.md`, about the
  `/security-review` slash command) do not overlap with plugin packaging/governance
  and were not used. Two additional genuinely overlapping notes not mentioned by any
  triage comment (`docs-github-copilot-enterprise-strict-known-marketplaces.md` and
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`) were found
  by searching the corpus directly for `managed-settings.json`-related notes.
