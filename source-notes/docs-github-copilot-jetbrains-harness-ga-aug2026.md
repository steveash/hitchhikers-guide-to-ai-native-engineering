---
source_url: https://github.blog/changelog/2026-08-24-copilot-harness-generally-available-in-copilot-for-jetbrains
source_type: docs
title: "Copilot harness generally available in Copilot for JetBrains"
author: GitHub (official changelog)
date_published: 2026-08-24
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3050"
---

# Copilot Harness Generally Available in Copilot for JetBrains

> GitHub's August 24, 2026 JetBrains changelog promotes "Copilot harness" — a
> capitalized, agent-picker-selectable entity, not previously documented under
> this name anywhere in the corpus — to general availability, alongside a
> public-preview built-in JetBrains MCP server, a post-update "What's New" tab,
> and Copilot harness `/review` integrations inside the IDE. The changelog does
> not define what distinguishes "Copilot harness" architecturally from the
> "Agent" mode, Claude agent provider, or Copilot CLI provider already
> documented in this corpus's JetBrains family — it names the GA milestone and
> a screenshot caption ("Agent picker drop down selecting Copilot harness")
> without further explanation.

## Source Context

- **Type**: docs (GitHub official product changelog, August 24, 2026; self-tagged
  "Release," "2 minute read," roughly 300 words across four sections: "What's new,"
  "User experience enhancements," "Quality improvements," and "Try it out and share
  your feedback")
- **Author credibility**: GitHub engineering team announcing a GA promotion and three
  smaller features for the JetBrains Copilot plugin. Authoritative for: the fact that
  "Copilot harness" reached GA on this date, that it is selectable from an agent
  picker dropdown (per the screenshot alt text), and the stated behavior of the other
  three "What's new" items. Not authoritative for: what "Copilot harness" actually is
  as a distinct execution mode (no definition, architecture description, or migration
  note is given anywhere in the source), whether it replaces or sits alongside the
  "Agent" mode documented in `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
  (Claim 1), or what "faster feature delivery and better code quality" means
  mechanistically.
- **Scope**: Four "What's new" items (Copilot harness GA, built-in JetBrains MCP
  server support in public preview, a post-update "What's New" tab, and Copilot
  harness `/review` integrations), four "User experience enhancements" bullets
  (model management, debug workflows, chat ergonomics, multi-root customization
  discovery), and one "Quality improvements" paragraph naming several reliability
  fixes. Does NOT cover: a definition or architecture description of "Copilot
  harness," a settings path or prerequisite for enabling it, an admin policy gate
  (no "Editor preview features" policy is mentioned for the GA item, unlike several
  prior preview-stage JetBrains changelogs in this corpus), or a JetBrains plugin
  version floor.

## Extracted Claims

### Claim 1: "Copilot harness" — a capitalized, agent-picker-selectable entity — is now generally available in Copilot for JetBrains, described only as providing "faster feature delivery and better code quality"

- **Evidence**: Official changelog "What's new" section, "Copilot harness generally
  available" heading, plus the section's screenshot alt text: "Agent picker drop down
  selecting Copilot harness."
- **Confidence**: settled (the GA status itself is stated definitively) — but see
  Our assessment for why the *substance* of the claim is thin
- **Quote**: "Copilot harness is now generally available, providing faster feature
  delivery and better code quality."
- **Our assessment**: This is a genuine terminology gap in the corpus, not just a new
  feature. No prior JetBrains source note in this family uses "Copilot harness" as a
  capitalized, selectable product name. Two prior corpus sources use "harness" only as
  a lowercase, generic noun: `docs-github-copilot-vscode-july-2026.md` (Claim 1) quotes
  VS Code's Agents window copy verbatim — "Use worktrees with any harness: Start
  Copilot, Claude, or Codex sessions in a Git worktree" — using "harness" to mean *any*
  of several interchangeable agent backends (Copilot, Claude, Codex), not a specific
  GitHub-branded mode. `docs-github-copilot-jetbrains-otel-model-management-july2026.md`
  (Concrete Artifacts, User Experience Enhancements) similarly uses "harness" generically
  in two UX bullets from the July 27, 2026 JetBrains changelog: "show a todo list in
  the harness" and "URL rendering in Copilot CLI harness." In both of those prior
  sources, "harness" describes the CLI agent's own runtime/session container — a common
  noun, not a proper one. This August 24 source is the first to capitalize "Copilot
  harness" and present it as a named option in the agent picker dropdown (per the
  screenshot alt text), on par with "Agent," "Ask," "Custom agents," and "Plan" from
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 1) and "Claude"
  from `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 1). One
  plausible reading — not stated by the source and not to be presented in the guide as
  confirmed — is that "Copilot harness" is a rebrand of the "Agent" mode / native
  Copilot CLI agent (whose phased promotion to JetBrains default was already announced
  in `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 11) into a
  distinct, GitHub-branded name that disambiguates it from third-party agent providers
  (Claude) now sharing the same picker. The source gives no evidence to confirm or rule
  this out. For the guide: flag this naming collision explicitly, since Chapter 02 of
  this guide is itself titled "Harness Engineering" and uses "harness" as the generic
  industry term for an agent's execution environment — GitHub has now productized the
  same word as a specific, capitalized, selectable mode name in JetBrains, which risks
  confusing readers if the guide doesn't distinguish the two usages.

### Claim 2: Built-in JetBrains MCP server support is now in public preview, making it easier to expose IDE capabilities through MCP-driven agent workflows without relying only on external server setup

- **Evidence**: Official changelog "What's new" section, "Built-in JetBrains MCP
  server support" heading, with a screenshot captioned "Agent customization page
  showing the built-in JetBrains MCP server."
- **Confidence**: emerging (explicitly public preview; no admin policy gate stated)
- **Quote**: "The built-in JetBrains MCP server support is now in public preview. This
  makes it easier to expose IDE capabilities through MCP-driven agent workflows
  without relying only on external server setup."
- **Our assessment**: This is a different MCP capability from every prior MCP item
  documented in this JetBrains family. `docs-github-copilot-jetbrains-otel-model-management-july2026.md`
  (Claim 3) documented MCP servers becoming usable *inside Claude agent flows* — i.e.,
  connecting to *external* MCP servers from a Claude-backed session.
  `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md` (Claim 3)
  documented enterprise-wide *allowlisting/denylisting* of which external MCP servers
  developers may connect to. This claim is different in kind: JetBrains itself now
  *exposes* IDE capabilities (presumably things like code navigation, refactoring, or
  project introspection already native to the IDE) *as* an MCP server, "without relying
  only on external server setup" — meaning the IDE becomes an MCP server an agent can
  call into, not merely an MCP client connecting outward. The changelog gives no detail
  on which IDE capabilities are exposed, what tools the built-in server offers, or how a
  practitioner enables/discovers it beyond the linked screenshot showing it on an "Agent
  customization page." For Ch02 (Harness Engineering — MCP Configuration): document
  this as a new MCP *server* role for JetBrains (IDE-as-MCP-server), distinct from the
  MCP *client* allowlisting and Claude-flow MCP access already documented; flag the
  missing tool inventory as an open question pending a dedicated docs page.

### Claim 3: After a JetBrains Copilot plugin update, a "What's New" tab now opens automatically so practitioners can immediately see what changed

- **Evidence**: Official changelog "What's new" section, "Better post-update release
  discovery" heading, with a screenshot captioned "What's new tab showing latest
  release notes."
- **Confidence**: settled (product fact stated definitively; no preview qualifier)
- **Quote**: "After you update the Copilot for JetBrains plugin, a What's New tab will
  open so you can immediately see what changed. This helps you adopt new capabilities
  faster and reduces guesswork after each upgrade."
- **Our assessment**: No prior source note in this corpus documents an in-IDE,
  auto-opening changelog surface for the JetBrains plugin. This is a small but
  practically relevant discoverability fix: given how frequently this JetBrains family
  of changelogs ships (roughly monthly since May 2026, per the eight prior source notes
  cross-referenced here), practitioners who don't proactively read github.blog have had
  no in-product signal of what changed after each plugin update until now. For Ch01
  (Daily Workflows): note the auto-opening "What's New" tab as a low-friction way for
  practitioners to stay current on JetBrains Copilot capabilities without external
  changelog-tracking effort — directly relevant to a guide that itself has been mining
  a new JetBrains changelog roughly monthly.

### Claim 4: Copilot harness `/review` integrations can now be used directly within JetBrains, reducing context switching when practitioners want review guidance during development

- **Evidence**: Official changelog "What's new" section, "Expanded Copilot harness
  integrations" heading.
- **Confidence**: settled (product fact stated definitively; no preview qualifier) —
  though it inherits the same "Copilot harness" definitional gap as Claim 1
- **Quote**: "You can use Copilot harness /review integrations directly in JetBrains,
  reducing context switching when you want review guidance during development."
- **Our assessment**: This ties the undefined "Copilot harness" entity (Claim 1) to
  `/review`, a command this corpus has previously only documented in the context of
  Copilot code review features (e.g., `docs-github-copilot-code-review-*` family, not
  independently re-verified in this extraction). The phrase "Copilot harness /review
  integrations" reads as: whatever code-review capability `/review` invokes elsewhere
  in Copilot's surfaces is now reachable as a JetBrains-embedded command, framed under
  the "Copilot harness" umbrella. This further supports Claim 1's inference that
  "Copilot harness" functions as a branded umbrella for GitHub's own (non-Claude)
  agentic capabilities in JetBrains, spanning both coding-agent execution and code
  review — but the source does not state this explicitly. For Ch02: note `/review`
  as newly available inside JetBrains under the Copilot harness umbrella; flag for a
  follow-up source once GitHub documents `/review`'s JetBrains-specific behavior (scope
  of review — file, PR, session diff — is not stated here).

### Claim 5: JetBrains Copilot's language model management table now has improved search behavior, clarified search actions, and resizable columns

- **Evidence**: Official changelog "User experience enhancements" section, "Model
  management" bullet.
- **Confidence**: settled (UX polish item stated definitively)
- **Quote**: "Model management: Improved search behavior, clarified search actions,
  and enabled resizable columns in the language model table."
- **Our assessment**: A minor usability fix to the model picker/management surface
  documented across this family (e.g., the `/models` command and recently-used models
  section in `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, Claim
  6). Resizable columns imply the "language model table" has grown wide enough
  (multiple providers × multiple metadata fields, plausibly including BYOK custom
  endpoints per `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`, Claim 1)
  that a fixed-width layout was no longer sufficient — a side-effect indicator of how
  much the JetBrains model-selection surface has grown since May 2026. Not
  independently significant enough for a dedicated guide callout beyond a passing
  mention in a UX-polish list.

### Claim 6: Debug-log exploration in JetBrains Copilot now has improved event-time sorting, token-usage filtering, and layout behavior

- **Evidence**: Official changelog "User experience enhancements" section, "Debug
  workflows" bullet.
- **Confidence**: settled (UX polish item stated definitively)
- **Quote**: "Debug workflows: Improved event-time sorting, token-usage filtering, and
  layout behavior in debug-log exploration."
- **Our assessment**: This directly extends the Agent Debug Panel first documented in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 5: "a
  chronological event log of agent interactions during a Copilot CLI session") and
  enhanced with a logs summary view in
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 5). "Token-
  usage filtering" is new to the corpus for this panel specifically — no prior source
  documents the debug panel surfacing token consumption as a filterable dimension,
  though per-turn AI credit visibility was separately documented as an inline session
  indicator in the same June 22 note (Claim 7). This is the first evidence the debug
  panel and the cost-visibility feature are converging (token usage now filterable
  within the same debugging surface that shows the chronological event log). For Ch04
  (Agentic Workflows — Debugging): note that the Agent Debug Panel can now be filtered
  by token usage, letting practitioners identify which events in a session consumed
  disproportionate tokens — useful for diagnosing runaway or inefficient agent turns.

### Claim 7: JetBrains Copilot chat now supports improved scrolling for long tool outputs and added keyboard shortcuts for send options

- **Evidence**: Official changelog "User experience enhancements" section, "Chat
  ergonomics" bullet.
- **Confidence**: settled (UX polish item stated definitively)
- **Quote**: "Chat ergonomics: Improved long tool-output scrolling and added shortcuts
  for send options."
- **Our assessment**: A narrow usability fix with no strong cross-reference in this
  corpus. "Long tool-output scrolling" implies practitioners were previously hitting
  friction reviewing large tool call results (e.g., long file reads, large diffs,
  verbose command output) inline in chat — a plausible pain point for JetBrains
  sessions given the CLI agent's growing tool surface documented across this family,
  but the changelog does not name a specific prior failure mode. Not significant enough
  for a dedicated guide section; worth a passing mention alongside Claim 6 as evidence
  of continued chat-surface polish.

### Claim 8: JetBrains Copilot now discovers customizations across all folders in a multi-root workspace and honors client-provided customization locations

- **Evidence**: Official changelog "User experience enhancements" section, "Multi-root
  customization discovery" bullet.
- **Confidence**: settled (product fact stated definitively)
- **Quote**: "Multi-root customization discovery: Improved customization handling by
  discovering customizations across all folders and honoring client-provided
  customization locations."
- **Our assessment**: This addresses a gap not explicitly covered by any prior source
  in this family: all previous JetBrains customization documentation
  (`docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 8, global `.agent.md` at
  `~/.copilot/agents`; `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
  Claim 8, the Agent Customizations editor's workspace/personal scope split) describes
  customization discovery in terms of a single project or a two-tier
  workspace/personal scope, not explicitly a *multi-root* workspace (multiple
  independent folders open in one JetBrains window). "Honoring client-provided
  customization locations" is notable but underspecified — the changelog does not
  define what a "client-provided" location is (a JetBrains-specific project setting?
  an IDE-level override?) or how it relates to the existing `.github/agents/` /
  `~/.copilot/agents` path model. For Ch02 (Harness Engineering — Agent Configuration):
  flag multi-root customization discovery as a fix relevant to practitioners working in
  monorepo-adjacent, multi-folder JetBrains workspaces, where previously customizations
  in non-primary folders may not have been discovered; flag "client-provided
  customization locations" as an open question pending further documentation.

### Claim 9: This release improves reliability for account detection and sign-in flows, MCP schema and tool-state handling, BYOK and model-refresh behavior, and Copilot agent session continuity after resume

- **Evidence**: Official changelog "Quality improvements" section, opening sentence.
- **Confidence**: settled (reliability fixes stated definitively, no further detail
  given per item)
- **Quote**: "This release improves reliability for account detection and sign-in
  flows, MCP schema and tool-state handling, BYOK and model-refresh behavior, and
  Copilot agent session continuity after resume."
- **Our assessment**: A bundled reliability paragraph naming four fix areas without
  individual detail, consistent with the terse "Quality improvements" style seen
  across this family (e.g., the single-sentence Quality improvements section in
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md`). "MCP schema and
  tool-state handling" is plausibly related to the new built-in MCP server support
  (Claim 2) shipping in the same release — a new MCP surface would exercise schema
  and tool-state handling more heavily and could surface bugs the release also fixes —
  but this connection is not stated by the source and should not be presented as
  confirmed. "Session continuity after resume" extends prior corpus documentation of
  session persistence (e.g., `docs-github-copilot-jetbrains-cli-agent-sessions.md`'s
  unified sessions view) without new specifics. For Ch03 (Verification — Environment
  Reliability): log as a general reliability improvement; none of the four fix areas
  carry enough independent detail for a dedicated guide callout.

### Claim 10: This release also fixes editor and rendering defects, restores file and folder `#` references in Copilot, Claude, and Codex chat inputs, and resolves worktree session startup failures for projects opened from WSL

- **Evidence**: Official changelog "Quality improvements" section, second sentence,
  naming two specific regressions and their fixes.
- **Confidence**: settled (specific bug fixes stated definitively)
- **Quote**: "It also fixes editor and rendering defects, restores file and folder #
  references in Copilot, Claude, and Codex chat inputs, and resolves worktree session
  startup failures for projects opened from WSL."
- **Our assessment**: Two concrete, previously-undocumented regressions are named here.
  First, the `#` file/folder reference syntax — a common in-chat mention mechanism —
  had regressed across *three* named chat surfaces simultaneously: "Copilot, Claude,
  and Codex chat inputs." This is the first corpus source to name Codex as a chat input
  surface inside JetBrains Copilot at all (prior JetBrains sources in this family name
  only Copilot's native agent, the Copilot CLI agent, and Claude as agent providers —
  see `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1; Codex
  is not mentioned in any of the six other reviewed notes in this family). Its
  appearance here, in a bug-fix sentence rather than a feature announcement, implies
  Codex became available as a JetBrains chat/agent surface at some point *before*
  this changelog, without a dedicated "What's new" announcement being mined into this
  corpus — a gap worth flagging for the Prospector to check for a missed intermediate
  changelog. Second, "worktree session startup failures for projects opened from WSL"
  is a concrete regression in the worktree isolation mode first documented in
  `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 2), specific to Windows
  Subsystem for Linux project setups — the first WSL-specific reliability note in this
  family. For Ch02 (Harness Engineering) and Ch03 (Verification): (1) flag Codex as an
  apparently-already-available JetBrains chat surface that this corpus has not yet
  independently documented — a candidate gap for a follow-up source search; (2) note
  the WSL worktree-startup fix as relevant to Windows-based practitioners using
  worktree isolation mode, who may have hit session-startup failures prior to this
  release.

## Concrete Artifacts

### Full "What's New" section (verbatim, raw-HTML-extracted)

```
Copilot harness generally available
"Copilot harness is now generally available, providing faster feature
delivery and better code quality."
[Screenshot alt text: "Agent picker drop down selecting Copilot harness"]

Built-in JetBrains MCP server support
"The built-in JetBrains MCP server support is now in public preview.
This makes it easier to expose IDE capabilities through MCP-driven
agent workflows without relying only on external server setup."
[Screenshot alt text: "Agent customization page showing the built-in
JetBrains MCP server"]

Better post-update release discovery
"After you update the Copilot for JetBrains plugin, a What's New tab
will open so you can immediately see what changed. This helps you
adopt new capabilities faster and reduces guesswork after each
upgrade."
[Screenshot alt text: "What's new tab showing latest release notes"]

Expanded Copilot harness integrations
"You can use Copilot harness /review integrations directly in
JetBrains, reducing context switching when you want review guidance
during development."
```
*Source: "Copilot harness generally available in Copilot for JetBrains," GitHub
changelog, August 24, 2026 (raw HTML fetched via `curl`, tags stripped, entities
decoded).*

### User Experience Enhancements and Quality Improvements (verbatim)

```
User experience enhancements:
"This release improves daily interaction quality across model
controls, debug workflows, long outputs, and workspace
customizations."

- Model management: "Improved search behavior, clarified search
  actions, and enabled resizable columns in the language model
  table."
- Debug workflows: "Improved event-time sorting, token-usage
  filtering, and layout behavior in debug-log exploration."
- Chat ergonomics: "Improved long tool-output scrolling and added
  shortcuts for send options."
- Multi-root customization discovery: "Improved customization
  handling by discovering customizations across all folders and
  honoring client-provided customization locations."

Quality improvements:
"This release improves reliability for account detection and sign-in
flows, MCP schema and tool-state handling, BYOK and model-refresh
behavior, and Copilot agent session continuity after resume. It also
fixes editor and rendering defects, restores file and folder #
references in Copilot, Claude, and Codex chat inputs, and resolves
worktree session startup failures for projects opened from WSL."
```
*Source: "Copilot harness generally available in Copilot for JetBrains," GitHub
changelog, August 24, 2026.*

### Page section structure (as fetched)

```
Copilot harness generally available in Copilot for JetBrains
(Release, August 24, 2026, 2 minute read)
├── What's new
│   ├── Copilot harness generally available
│   ├── Built-in JetBrains MCP server support
│   ├── Better post-update release discovery
│   └── Expanded Copilot harness integrations
├── User experience enhancements (4 bullets)
├── Quality improvements (2 sentences)
└── Try it out and share your feedback
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 5) and
    `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 5): both
    documented the Agent Debug Panel's chronological event log and its summary-view
    enhancement. Claim 6 here corroborates the panel's continued development with
    event-time sorting and token-usage filtering.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 2): worktree isolation
    mode is corroborated as a live, maintained feature by Claim 10's WSL startup-failure
    fix — a feature that receives bug fixes is a feature still actively used and
    supported.

- **Contradicts**: None identified. No existing corpus source makes a claim that
  directly opposes any claim in this note. No contradiction issue filed. (Note: the
  "Copilot harness" terminology gap discussed in Claim 1 is a definitional ambiguity
  and a generic-vs-proper-noun usage shift, not a factual contradiction between two
  sources making opposing claims about the same fact — it does not meet the MINER.md
  §4a bar for filing a contradiction issue.)

- **Extends**:
  - `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (MCP servers
    usable in Claude agent flows, Claim 3) and
    `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md` (MCP server
    allowlist, Claim 3): both documented JetBrains as an MCP *client* surface. Claim 2
    here extends the corpus's MCP coverage to JetBrains-as-MCP-*server* — a new
    direction not previously documented for any IDE in this family.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 1, agent
    picker with Agent/Ask/Custom agents/Plan modes) and
    `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 1, Claude
    added to the same picker): Claim 1 here extends the agent-picker inventory with
    "Copilot harness" as an additional (or renamed) selectable entry, per the
    screenshot alt text — though the source does not clarify whether it replaces
    "Agent" mode or sits alongside it.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 2, worktree isolation):
    Claim 10's WSL worktree-startup-failure fix extends this corpus's coverage of
    worktree isolation reliability to a WSL-specific failure mode not previously
    documented.

- **Novel**:
  - **"Copilot harness" as a capitalized, agent-picker-selectable, GA product entity**
    (Claims 1, 4): First corpus documentation of this exact term used as a proper noun;
    prior corpus uses of "harness" are all generic/lowercase (see Claim 1's Our
    assessment for the two prior examples). This is a genuine terminology gap requiring
    editorial attention given the guide's own Ch02 title.
  - **JetBrains exposing its own IDE capabilities as a built-in MCP server** (Claim 2):
    First corpus documentation of an IDE acting as an MCP server (not just an MCP
    client) for GitHub Copilot.
  - **An in-IDE, auto-opening "What's New" tab after plugin updates** (Claim 3): First
    corpus documentation of an in-product changelog discovery mechanism for the
    JetBrains plugin.
  - **Codex named as a JetBrains chat input surface** (Claim 10): First appearance of
    "Codex" in this JetBrains source-note family, surfaced incidentally in a bug-fix
    sentence rather than a feature announcement — a likely gap in this corpus's
    JetBrains coverage.
  - **Token-usage filtering in the Agent Debug Panel** (Claim 6): First corpus source
    connecting the debug panel's event log to token-consumption filtering.

## Guide Impact

- **Chapter 02 (Harness Engineering — Terminology)**: Add an explicit editorial note
  distinguishing the guide's generic use of "harness" (an agent's execution
  environment — the sense used in `docs-github-copilot-vscode-july-2026.md`'s "any
  harness: Copilot, Claude, or Codex") from GitHub's new capitalized product name
  "Copilot harness" (Claim 1), which is a specific, GA, agent-picker-selectable entity
  in JetBrains as of August 24, 2026 whose internal distinction from "Agent" mode is
  undocumented. Do not conflate the two when citing this or prior JetBrains sources.

- **Chapter 02 (Harness Engineering — MCP Configuration)**: Add JetBrains's built-in
  MCP server (Claim 2, public preview) as a new MCP capability, distinct from the
  existing MCP-client allowlisting (`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`)
  and Claude-flow MCP access (`docs-github-copilot-jetbrains-otel-model-management-july2026.md`)
  already documented — flag the tool inventory as undocumented pending further sources.

- **Chapter 02 (Harness Engineering — Agent Configuration)**: Add multi-root
  customization discovery (Claim 8) to the guide's coverage of JetBrains customization
  discovery, alongside the existing personal/workspace scope model; flag "client-
  provided customization locations" as an open, undefined term.

- **Chapter 04 (Agentic Workflows — Debugging)**: Add token-usage filtering to the
  Agent Debug Panel documentation (Claim 6) as a refinement for diagnosing
  disproportionately expensive session events.

- **Chapter 01 (Daily Workflows)**: Note the auto-opening post-update "What's New" tab
  (Claim 3) as a low-friction in-product changelog discovery mechanism.

- **Prospector follow-up**: Flag "Codex" (Claim 10) as an apparently-available
  JetBrains chat input surface with no dedicated source note in this corpus family —
  worth a targeted search for the changelog entry that introduced it.

## Extraction Notes

1. **Raw HTML extraction, not AI-summarized WebFetch**: An initial WebFetch call
   returned a plausible-looking but paraphrased/summarized reproduction of the page
   (e.g., rendering "Copilot harness is now generally available, providing faster
   feature delivery and better code quality" as an unquoted summary sentence, and
   compressing the four "What's new" items into prose). Per MINER.md §2a, this
   extraction instead fetched the changelog directly via `curl` and parsed the
   article body from the raw HTML (`<article>` → `.PostContent-main` →
   embedded pre-rendered HTML block). All quotes above were copied character-for-
   character from that raw-HTML extraction, not from the WebFetch summary.
2. **Source is short (~300 words)**: All ten claims above represent essentially the
   entire substantive content of the changelog. The "Try it out and share your
   feedback" section (plugin marketplace link, feedback channels) was not extracted
   as a claim — it is navigational/feedback-channel content, consistent with how
   this same section is treated across every other note in this family.
3. **No sub-pages followed**: unlike several prior notes in this family (e.g.,
   `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`, which
   followed two linked reference pages), this changelog entry contains no inline
   links to deeper documentation for "Copilot harness," the built-in MCP server, or
   any other item — only the two navigational feedback links at the bottom. There is
   no linked page to follow that would resolve the Claim 1 definitional gap.
4. **"Copilot harness" definitional gap is the central limitation of this source**:
   this extraction deliberately does not assert what "Copilot harness" is beyond
   what the source states (a GA, agent-picker-selectable entity associated with
   faster feature delivery, better code quality, and `/review` integrations). The
   plausible "this is the renamed Agent/CLI-agent mode" reading in Claim 1 is
   explicitly flagged as unconfirmed inference, not fact, and should not be adopted
   into the guide without a corroborating source that states it directly.
5. **No contradictions filed**: see Cross-References → Contradicts above.
