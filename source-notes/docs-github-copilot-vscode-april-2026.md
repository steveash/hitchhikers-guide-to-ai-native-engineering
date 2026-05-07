---
source_url: https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases
source_type: docs
title: "GitHub Copilot in Visual Studio Code — April 2026 Releases"
author: GitHub (official changelog)
date_published: 2026-05-06
date_extracted: 2026-05-07
last_checked: 2026-05-07
status: current
confidence_overall: emerging
issue: "#548"
---

# GitHub Copilot in Visual Studio Code — April 2026 Releases

> The VS Code April 2026 Copilot changelog (releases v1.116–v1.119) introduces four
> high-signal patterns for AI-native engineering: universal semantic workspace search
> plus a new cross-org `githubTextSearch` tool; bring-your-own-key support that creates
> a new model-governance surface for enterprise teams; agent read/write access to live
> terminals and browser tabs; and remote CLI session orchestration from GitHub.com or
> mobile — extending VS Code into an asynchronous dispatch surface for Copilot CLI work.

## Source Context

- **Type**: docs (GitHub official product changelog, May 6, 2026, covering VS Code
  releases v1.116 through v1.119 shipped throughout April and early May 2026)
- **Author credibility**: GitHub engineering team announcing production features in
  Visual Studio Code. Authoritative for the fact that these capabilities exist, the
  specific setting names and commands, and the stated behavioral semantics. Not a
  credible source for adoption outcomes, task-quality effects of these features, or
  how often they are used in practice. No empirical data cited.
- **Scope**: Four feature groups — smarter context (semantic search, `/chronicle`,
  token reduction), agent experience (inline diffs, custom agent generation, BYOK,
  terminal access, browser integration), chat continuity (remote CLI monitoring,
  debug log persistence, background command notifications), and UX polish. Covers
  VS Code specifically; does NOT cover whether these features apply to JetBrains,
  Eclipse, or other Copilot-supported IDEs, or how they interact with the Visual
  Studio features documented in `docs-github-copilot-vs-april-2026.md`.

## Extracted Claims

### Claim 1: Semantic indexing for code search is now universally available across all VS Code workspaces — previously limited to certain workspace types

- **Evidence**: Official changelog statement under "Search across any codebase." No
  prior restriction documented; the announcement implies a prior limitation now removed.
- **Confidence**: settled (product fact; scoping change stated in official changelog)
- **Quote**: "Semantic indexing now works in all workspaces."
- **Our assessment**: The universalization of semantic search removes a class of
  workspace-type confusion for practitioners. Teams that had been unable to use
  Copilot's semantic search in monorepo or non-standard workspace configurations can
  now rely on it consistently. For Ch04 (context engineering): semantic indexing is
  now a baseline capability, not a conditional one — practitioners can assume it is
  available and design context-retrieval strategies around it without workspace-type
  caveats.

### Claim 2: A new `githubTextSearch` agentic tool enables grep-style search across remote GitHub repositories and organizations, extending agent code awareness beyond the local workspace

- **Evidence**: Official changelog under "Search across any codebase." The tool name
  is explicitly stated.
- **Confidence**: settled (product fact — tool named and described in official changelog)
- **Quote**: "Agents can also run grep-style searches across GitHub repos and orgs
  with the new `githubTextSearch` tool."
- **Our assessment**: This extends the agent's code-awareness surface from the
  local workspace to the entire GitHub organization. Previously, agent search was
  bounded by what was cloned locally; `githubTextSearch` allows agents to query
  the full org codebase without a local clone. For Ch04: this is a significant
  context-sourcing pattern — agents can now pull cross-repo evidence (e.g., how a
  pattern is used elsewhere in the org) as context for local work. Teams with large
  monorepos or multi-repo architectures should evaluate whether `githubTextSearch`
  reduces the "agent lacks cross-codebase context" failure mode documented in
  harness failure literature.

### Claim 3: The experimental `/chronicle` feature creates a local, queryable database of the developer's chat history — a persistent memory layer for workflow recall

- **Evidence**: Official changelog under "Query history with /chronicle (Experimental)."
  Setting name explicitly stated: `github.copilot.chat.localIndex.enabled`.
- **Confidence**: emerging (experimental; no data on recall quality, storage limits,
  or how well personalized workflow tips work in practice)
- **Quote**: "Chronicle tracks your chat interactions in a local database so you can
  search past sessions, recall recent work, and get personalized workflow tips."
- **Our assessment**: `/chronicle` is the first documented per-developer persistent
  memory layer in the GitHub Copilot VS Code ecosystem. Prior corpus sources document
  session-level context management (e.g., Cursor's self-summarization, Anthropic's
  1M-context session management); `/chronicle` extends this to cross-session recall.
  The "personalized workflow tips" claim is the least specific — no detail on how tips
  are generated or what they cover. The local-database approach means this data does
  not leave the developer's machine (privacy-preserving), but also means it cannot
  be shared across a team. For Ch04: document `/chronicle` as an emerging individual
  context-management primitive, distinct from shared project context (CLAUDE.md,
  AGENTS.md). Experimental status means teams should not build critical workflows
  around it yet.

### Claim 4: Smarter prompt caching, deferred tool loading, and purpose-built agentic tools reduce token usage on every agent request without changing agent behavior

- **Evidence**: Official changelog overview and "Lower token usage" section. No
  metrics or percentages cited for the reduction magnitude.
- **Confidence**: emerging (product claim with no quantitative evidence; "without
  changing agent behavior" is asserted but not demonstrated)
- **Quote**: "Smarter prompt caching, deferred tool loading, and new agentic tools
  reduce token usage on every request."
- **Our assessment**: Three separate mechanisms are bundled in this claim: (1) prompt
  caching (reuse of repeated prompt segments across requests), (2) deferred tool
  loading (tools not included in the prompt until needed), and (3) purpose-built
  agentic tools (presumably more efficient tool definitions). The behavioral-equivalence
  claim ("without changing agent behavior") is important but unverified — prompt
  caching and deferred loading can theoretically affect agent behavior if cache hits
  miss context that would have changed the response. For Ch02: this is noteworthy as
  a platform-level token-efficiency improvement that applies without any harness
  changes. Practitioners should monitor whether their agents' behavior changes
  noticeably after the VS Code update; the "no behavior change" claim should be
  treated as a starting assumption to verify.

### Claim 5: Code changes now appear as inline diffs directly in the chat thread, removing the need to switch views to review AI-proposed edits

- **Evidence**: Official changelog under "Review diffs in chat."
- **Confidence**: settled (UI feature stated in official changelog)
- **Quote**: "Code changes now appear as diffs directly in the chat thread."
- **Our assessment**: This is a workflow-friction reduction rather than a capability
  change. Previously, reviewing AI-proposed code changes required navigating to a
  separate diff view; now the developer sees the diff inline where the suggestion
  was made. For Ch01 (daily workflows): this reduces the cognitive switch cost
  between "chat with agent" and "review proposed change" — a small but meaningful
  improvement to the review-and-iterate loop.

### Claim 6: Custom agents, skills, and instructions can be generated from a natural language description, reducing the barrier to creating new agent tooling

- **Evidence**: Official changelog under "Generate agent customizations." No detail
  on what the output format is, how complete the generated definitions are, or what
  validation is performed.
- **Confidence**: emerging (feature announced without detail on output quality or
  completeness)
- **Quote**: "Draft custom agents, skills, and instructions from a natural language
  description."
- **Our assessment**: The feature mirrors the "generate configuration from description"
  pattern used in other tooling (e.g., GitHub Actions workflow generation). The
  practical question is whether the output is a usable starting point or requires
  substantial human refinement. The term "draft" in the source suggests the output
  is a starting point, not a finished artifact. For Ch02 (harness engineering): if
  the generated output is reasonably complete, this lowers the skill-authoring
  barrier for teams that are not already fluent in SKILL.md or agent instruction
  formats. The connection to the `gh skill` package manager
  (`docs-github-copilot-agent-skills-cli.md`) is worth tracking — if generated
  skills are `gh skill`-compatible, the creation-to-distribution pipeline is
  significantly shortened.

### Claim 7: Copilot Business and Enterprise users can link their own API keys from third-party model providers to use those models directly in VS Code, with admin governance via a named policy

- **Evidence**: Official changelog under "Bring your own model key." Both external
  provider keys (OpenRouter, Microsoft Foundry, Google, Anthropic, OpenAI) and local
  models (Ollama, Foundry Local) are listed. Admin policy name is stated explicitly.
- **Confidence**: settled (product fact; providers listed and admin policy named in
  official changelog)
- **Quote**: "Copilot Business and Enterprise users can link their own API keys
  (OpenRouter, Microsoft Foundry, Google, Anthropic, OpenAI, and others) to use
  those models directly in VS Code chat."
- **Our assessment**: BYOK is a materially different model-access pathway from what
  was previously documented in our corpus. Prior sources documented model selection
  from GitHub's curated roster (`docs-github-copilot-agent-model-selection.md`,
  Claim 1) or auto-routing within GitHub's infrastructure
  (`docs-github-copilot-cli-auto-model-selection.md`, Claim 1). BYOK bypasses
  GitHub's model hosting entirely — the model request goes to the external provider
  directly. This has cost implications (billed by the external provider, not against
  Copilot premium requests), privacy implications (conversation data goes to the
  external provider), and governance implications (the admin policy "Bring Your Own
  Language Model Key" is a new enterprise control surface separate from existing
  Copilot model policies). For Ch02: BYOK adds a third model-access tier:
  (1) GitHub-hosted models (Copilot plan), (2) model selection from GitHub's third-
  party agent roster (Business/Enterprise with admin policy), (3) direct API key
  access to any provider (Business/Enterprise, BYOK admin policy). Teams with
  existing Anthropic or OpenAI contracts may find BYOK allows reusing enterprise
  agreements for their VS Code Copilot sessions.

### Claim 8: The changelog ambiguously states that BYOK requires Business/Enterprise with admin policy in one sentence and is available for Free/Pro users in another — the per-tier access model is unclear

- **Evidence**: The second WebFetch of the source included both "Copilot Business
  and Enterprise users can link their own API keys... Admins control access via the
  Bring Your Own Language Model Key policy" and "BYOK is available for Copilot
  Free, Pro, and Pro users." These two statements are adjacent in the source and
  are not reconciled.
- **Confidence**: anecdotal (intra-source ambiguity; the source does not explain
  the discrepancy between the two tier statements)
- **Quote**: (no single verbatim quote captures the contradiction; see both
  statements cited in Evidence above)
- **Our assessment**: The most plausible reading is that Business/Enterprise users
  use an admin-governed BYOK pathway (controlled via the "Bring Your Own Language
  Model Key" policy), while Free/Pro users may have direct BYOK access without
  admin governance. An alternative reading is that "Free, Pro, and Pro users" is
  a rendering artifact for "Free, Pro, and Pro+ users" (the Pro+ tier may have
  individual BYOK without admin control). A third reading: local models (Ollama,
  Foundry Local) are available to all tiers, while external provider keys require
  Business/Enterprise. Practitioners relying on BYOK for compliance or cost
  management should verify the exact tier requirements against current GitHub
  documentation before building workflows around it. For Ch02: note the tier
  ambiguity and recommend documentation verification as of the time of implementation.

### Claim 9: Agents can read from and write to existing foreground terminals — including live REPLs and interactive scripts — giving agents persistent access to active execution contexts

- **Evidence**: Official changelog under "Agents can access any open terminal."
- **Confidence**: settled (capability stated in official changelog)
- **Quote**: "Agents can read from and write to existing foreground terminals,
  including running REPLs and interactive scripts."
- **Our assessment**: Terminal read/write is a significant capability expansion.
  Previously, agents in VS Code could execute terminal commands; this announcement
  extends access to *existing* terminals, meaning agents can interact with a
  session the developer already started (e.g., a running Python REPL, a test
  process, a database CLI). This is meaningfully different from spawning a new
  terminal for each command — the agent can observe and interact with ongoing
  state. For Ch03 (safety): terminal write access to an existing REPL or
  interactive script is a high-privilege capability — the agent can execute
  arbitrary code in a running process. Teams with security-sensitive workflows
  should review whether auto-approve is appropriate for terminal-write actions,
  or whether a human confirmation gate should be enforced for this capability.

### Claim 10: Browser tab sharing gives agents real-time visibility into live web content — agents can read page content, interact with elements, and validate changes in a live browser

- **Evidence**: Official changelog under "Integrated Browser."
- **Confidence**: settled (capability stated in official changelog)
- **Quote**: "Give agents visibility into your live browser by sharing tabs on
  demand as context. Agents can read content, interact with pages, and validate
  changes in real time."
- **Our assessment**: Browser integration closes a major context gap: agents
  previously had to rely on descriptions of web UI state; they can now observe
  the live state directly. "Interact with pages" implies the agent can take
  actions in the browser (clicks, form fills, navigation), not just read. This
  enables a class of automated validation workflows — e.g., "make this change
  and verify it renders correctly in the browser" — that previously required
  separate browser automation tooling. For Ch04 (context engineering): browser
  tab sharing is a new context source that makes live runtime state available to
  agents alongside static code context. Teams building full-stack features should
  consider whether browser-integrated Copilot sessions reduce the "agent doesn't
  know what the UI actually looks like" failure mode. For Ch03 (safety): browser
  interaction is a high-risk agent capability (could submit forms, click links,
  navigate to external sites) that should be used with explicit session-level
  boundaries.

### Claim 11: Copilot CLI sessions can be monitored and steered remotely from GitHub.com or the mobile app, enabling asynchronous delegation of CLI work from VS Code

- **Evidence**: Official changelog under "Continue Copilot CLI sessions across
  devices." Setting name (`github.copilot.chat.cli.remote.enabled`) and command
  (`/remote on`) explicitly stated. Marked experimental.
- **Confidence**: emerging (experimental feature; monitoring and steering
  semantics not fully defined in changelog)
- **Quote**: "run `/remote on` to monitor and steer ongoing Copilot CLI sessions
  started in VS Code from GitHub.com or the mobile app."
- **Our assessment**: This is the VS Code analogue of the "dispatch and continue"
  pattern documented in `docs-github-copilot-vs-april-2026.md` (Claim 7), where
  VS IDE became a dispatch surface for cloud agent work. Here, VS Code becomes
  the starting point for a Copilot CLI session that can then be monitored remotely
  — the developer can initiate CLI-based work, close VS Code, and continue
  steering the session from a phone or browser. "Steer" is noteworthy: the
  developer is not just observing but actively directing the running session. For
  Ch04: document this as an emerging "start locally, continue remotely" workflow
  pattern. Experimental status means it should not anchor production workflows yet.

### Claim 12: Agent debug logs now persist locally across VS Code sessions, enabling retrospective forensics on earlier agent runs

- **Evidence**: Official changelog under "Debug past agent sessions."
- **Confidence**: settled (feature stated in official changelog)
- **Quote**: "The Agent Debug Log panel now persists logs locally so you can
  retrace what happened in earlier runs."
- **Our assessment**: Persistent debug logs address a longstanding limitation:
  when an agent run produced unexpected output, diagnosing what happened required
  the session to still be open. Now developers can retrospectively examine what
  tools were called, what context was used, and what decisions the agent made.
  For Ch04: persistent debug logs are a key observability primitive for
  iterating on agent harness configuration. Teams can use these logs to identify
  which tool calls or context sources correlate with poor outputs and refine
  their harness accordingly. This is a weaker version of the structured
  observability frameworks described in `blog-ghaw-agent-observability.md` but
  requires no additional tooling — it is built into VS Code.

### Claim 13: Long-running terminal commands surface status notifications in chat, bridging asynchronous background work with the conversational interface

- **Evidence**: Official changelog under "Track background commands."
- **Confidence**: settled (feature stated in official changelog)
- **Quote**: "Long-running terminal commands inform you of their status with
  system notifications in chat."
- **Our assessment**: This is a UX integration between the terminal execution
  context and the chat context. Developers running a slow test suite or build
  can now receive a chat notification when it completes rather than switching
  windows to check. For Ch01 (daily workflows): note this as a workflow
  continuity feature — developers can remain in the conversational context while
  background work runs, reducing context switches.

## Concrete Artifacts

### VS Code April 2026 Copilot Feature Summary

```
Changelog scope: VS Code releases v1.116–v1.119
Publication date: May 6, 2026

SMARTER CONTEXT
  Semantic search: universally available in all workspaces (previously limited)
  githubTextSearch: grep-style search across GitHub repos and orgs (new tool)
  /chronicle (experimental): local queryable chat history database
    Setting: github.copilot.chat.localIndex.enabled
  Token reduction: prompt caching + deferred tool loading + new agentic tools

AGENT EXPERIENCE
  Inline diffs: code changes appear as diffs in chat thread
  Agent generation: draft custom agents/skills/instructions from natural language
  BYOK: Business/Enterprise can link external provider API keys
    Providers: OpenRouter, Microsoft Foundry, Google, Anthropic, OpenAI (+ others)
    Local models: Ollama, Foundry Local, and more
    Admin control: "Bring Your Own Language Model Key" policy on GitHub.com
    ⚠️ Tier ambiguity: source also states "BYOK is available for Copilot Free, Pro,
       and Pro users" without reconciling with the Business/Enterprise requirement
  Terminal access: agents can read/write existing foreground terminals (incl. REPLs)
  Browser integration: share tabs; agents read content, interact, validate in real time

CHAT CONTINUITY
  Remote CLI monitoring (experimental):
    Enable: github.copilot.chat.cli.remote.enabled
    Command: /remote on
    Monitor/steer from GitHub.com or mobile app
  Debug log persistence: Agent Debug Log panel persists logs across sessions
  Background command notifications: long-running commands → chat notifications

ALSO NEW
  Incremental chat rendering, sortable agent sessions, synced Copilot CLI session titles
  Markdown preview with toolbar (source/preview toggle)
```

### BYOK Configuration (VS Code, April 2026)

```
For Copilot Business/Enterprise (admin-governed):
  Admin enables: "Bring Your Own Language Model Key" policy on GitHub.com
  Users link: API key from supported provider in VS Code settings
  Supported providers: OpenRouter, Microsoft Foundry, Google, Anthropic, OpenAI

For local models (all tiers, per source):
  Ollama, Foundry Local, and others (no external API key required)

⚠️ Tier note: Source states both "Business and Enterprise users can link their
   own API keys" AND "BYOK is available for Copilot Free, Pro, and Pro users."
   Exact tier requirements should be verified against current GitHub docs before
   implementation.
```

### Remote CLI Session Configuration

```
1. Enable experimental remote CLI feature:
   Setting: github.copilot.chat.cli.remote.enabled → true

2. Start Copilot CLI session in VS Code

3. Activate remote monitoring:
   Command: /remote on

4. Monitor/steer from:
   - GitHub.com (browser)
   - Mobile app

Note: experimental as of May 2026. Not recommended for production workflows.
```

## Cross-References

- **Corroborates**:
  - **docs-github-copilot-vs-april-2026.md** (#475): That note covers the April 2026
    Visual Studio Copilot changelog. Both notes share the same release period and
    product family; each covers distinct features for different editors. Where VS
    introduced user-level agent definitions at `%USERPROFILE%/.github/agents/` and
    a debugger agent pipeline (that note, Claims 5 and 3), VS Code introduces BYOK,
    browser integration, and terminal write access. Together they show GitHub shipping
    distinct capability expansions to its two Microsoft IDE Copilot integrations in
    the same period — with VS Code receiving more agentic execution primitives
    (terminal, browser) and VS receiving more workflow management primitives
    (issue-from-debugger, user-level agents). Neither changelog overlaps the other's
    features, confirming these are product-distinct update streams.
  - **docs-github-copilot-vs-april-2026.md** Claim 7 ("dispatch and continue" pattern):
    The remote CLI session monitoring (Claim 11 here) is a VS Code instantiation of
    the same pattern: the IDE becomes a starting point for asynchronous agent work
    that the developer can continue monitoring remotely. The VS version uses a cloud
    agent on remote infrastructure; the VS Code version uses the Copilot CLI.
    Together, these two sources establish the "start in IDE, continue remotely" as
    an emerging pattern across both Microsoft IDEs.

- **Extends**:
  - **docs-github-copilot-agent-model-selection.md** (#171): That note documents
    model selection from GitHub's hosted model roster (Claude/Codex agents on
    github.com). Claim 7 here (BYOK) introduces a third model-access tier: rather
    than selecting from GitHub's offered models, teams can bypass GitHub's hosting
    entirely and route requests directly to an external provider via API key. The
    two sources together show three distinct model-access pathways in the Copilot
    ecosystem: (1) GitHub-hosted models, (2) GitHub-brokered third-party models,
    (3) user/team-owned direct provider keys (BYOK).
  - **docs-github-copilot-cli-auto-model-selection.md** (#203): That note covers
    the Copilot CLI's auto model routing and per-request model transparency. Claim 11
    here (remote CLI monitoring) adds VS Code as a remote orchestration surface for
    those same CLI sessions. The two sources together define the full Copilot CLI
    developer experience: auto model routing for cost-efficiency (that note),
    remotely monitored/steered sessions from VS Code (this note). A Copilot CLI
    harness that uses auto routing (for cost) and remote monitoring (for async work)
    is now fully documented between these two sources.
  - **docs-github-copilot-agent-skills-cli.md** (#189): That note documents the
    `gh skill` package manager for cross-agent skill distribution. Claim 6 here
    (natural language agent generation) complements it: `gh skill` provides the
    distribution mechanism; natural language generation provides an authoring
    shortcut. If generated agent/skill definitions are `gh skill`-compatible (not
    stated in this source), the creation-to-distribution pipeline is substantially
    shortened. Track whether GitHub documents the output format of the generation
    feature.

- **Contradicts**: None identified between this source and existing source notes.
  The BYOK tier ambiguity (Claim 8) is an intra-source inconsistency, not a
  contradiction with another note — no existing note claims that BYOK requires
  Business/Enterprise only or that it is available at all tiers. The terminal write
  access and browser interaction capabilities are novel additions with no opposing
  claims in the corpus.

- **Novel**:
  - **BYOK for VS Code inline chat**: No prior corpus source documents Copilot users
    bringing their own external provider API keys for VS Code inline chat. Prior model-
    access sources covered GitHub's hosted models (Claim 1 of #171) or auto routing
    within GitHub's infrastructure (#203). BYOK is a fundamentally different access
    pathway with distinct cost, privacy, and governance implications.
  - **Browser tab sharing as agent context source**: No prior corpus source documents
    live browser state as an agent context input. All prior context sources are
    code-based (files, repos, CLAUDE.md, skills) or structured tool output. Live
    browser content is the first real-time UI-state context source documented.
  - **Agent write access to live terminal sessions**: Prior sources documented agents
    executing terminal commands in new shells. Write access to existing foreground
    terminals (including live REPLs) is a new execution primitive not documented
    elsewhere in the corpus.
  - **`githubTextSearch` tool for cross-org grep**: No prior source documents a
    purpose-built agent tool for searching GitHub organizations programmatically.
    Prior search was local-workspace-bounded.
  - **`/chronicle` per-developer chat history database**: No prior source documents
    a persistent, queryable per-developer workflow memory layer in a Copilot context.
    This is the first local-database approach to chat history in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add BYOK as a third model-access tier in the Copilot model configuration taxonomy,
    distinct from GitHub-hosted models (auto routing, `docs-github-copilot-cli-auto-
    model-selection.md`) and GitHub-brokered third-party models (`docs-github-copilot-
    agent-model-selection.md`). Note the intra-source tier ambiguity (Claim 8) and
    recommend documentation verification before implementation. For teams with existing
    Anthropic/OpenAI contracts, document BYOK as a cost-consolidation option (use
    existing enterprise credits rather than Copilot premium requests).
  - Note the new admin governance surface: "Bring Your Own Language Model Key" policy
    is a new enterprise configuration scope not previously documented in the corpus.
    Enterprise Copilot governance checklists should include this policy alongside the
    CCA and model-selection admin policies from `docs-github-copilot-cca-custom-
    properties.md`.
  - Add `githubTextSearch` as a cross-org context-retrieval tool for agents. For teams
    with multi-repo architectures: this is the first built-in tool for cross-repository
    code search without a local clone requirement.

- **Chapter 04 (Context Engineering)**:
  - Semantic indexing universality (Claim 1): update any harness guidance that conditions
    on workspace type for semantic search availability. This is now unconditional.
  - Browser tab sharing (Claim 10) and terminal read/write (Claim 9) are new context
    sources in the agent session that change how agents can gather runtime evidence.
    Add as "live execution context sources" in contrast to the static code context sources
    (CLAUDE.md, skills, workspace files). These are highest-privilege context inputs and
    should be documented as requiring deliberate session scope management.
  - `/chronicle` (Claim 3): add as an experimental individual workflow-memory primitive.
    Distinguish from shared project context (CLAUDE.md) — `/chronicle` is personal and
    non-version-controlled. Do not recommend it for team-shared context yet.
  - Token reduction (Claim 4): note as a platform-level baseline improvement that reduces
    the cost of context-heavy agent sessions, without practitioner action required.

- **Chapter 03 (Safety and Verification)**:
  - Terminal write access to live sessions (Claim 9) and browser interaction (Claim 10)
    are the highest-risk new capabilities in this source. Add to the "agentic execution
    capabilities requiring human-in-the-loop gates" list. Recommend that teams review
    their VS Code Copilot auto-approve settings to determine whether terminal-write and
    browser-interact are gated behind human confirmation. These capabilities can modify
    runtime state in ways that are harder to undo than code-file changes.

## Extraction Notes

1. **Source covers VS Code specifically**: These features apply to the VS Code Copilot
   extension (releases v1.116–v1.119). The overlapping source `docs-github-copilot-vs-
   april-2026.md` covers the separate Visual Studio product — different editor, different
   feature set, same product family. Do not conflate.
2. **BYOK tier ambiguity is unresolved**: The source simultaneously describes BYOK as
   Business/Enterprise with admin policy and as available for Free/Pro users. Three
   fetches of the source produced slightly different renderings of this section. The
   ambiguity is documented as Claim 8 but the source note does not resolve it. Verify
   against current GitHub documentation.
3. **"Admins get new group policies for controlling which domains agents can reach"**:
   The source's overview summary mentions domain control policies for agents ("Admins get
   new group policies for controlling which domains agents can reach"), but this claim
   does not appear in the detailed feature sections. It may be covered under the BYOK
   admin policy or may be a separate feature not elaborated in this changelog. It is not
   extracted as a standalone claim because no detail is available to verify; practitioners
   should check GitHub's admin documentation for this feature.
4. **Token reduction claim is unquantified**: Claim 4 ("reduce token usage on every
   request") is stated without metrics. No percentage, benchmark, or example is provided.
   Treat as a directional claim pending practitioner verification.
5. **Experimental features**: `/chronicle` (Claim 3) and remote CLI monitoring (Claim 11)
   are explicitly marked experimental in the source. These should not anchor production
   harness designs.
6. **No contradictions filed**: Cross-referencing with all relevant Copilot and agent
   source notes found no opposing claims. BYOK is novel, terminal/browser access is
   novel, and the intra-source BYOK tier ambiguity is not actionable as a formal
   contradiction with another source note.
