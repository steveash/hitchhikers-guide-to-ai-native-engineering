---
source_url: https://github.blog/changelog/2026-06-02-github-copilot-in-eclipse-byok-skills-and-chat-updates
source_type: docs
title: "GitHub Copilot in Eclipse: BYOK, skills, and chat updates"
author: GitHub (official changelog)
date_published: 2026-06-02
date_extracted: 2026-06-03
last_checked: 2026-06-03
status: current
confidence_overall: emerging
issue: "#1034"
---

# GitHub Copilot in Eclipse: BYOK, skills, and chat updates

> GitHub's June 2, 2026 changelog documenting six new features in the Eclipse
> IDE Copilot plugin: a refreshed chat view with model/mode combo picker, context
> window usage indicator, BYOK for custom models, skills and prompt files via slash
> commands, thinking blocks (reasoning visibility), and selectable thinking effort
> — the first corpus documentation of IDE-level reasoning depth control and of
> Copilot's Eclipse integration.

## Source Context

- **Type**: docs (GitHub official product changelog, June 2, 2026; approximately
  600 words covering eight distinct feature areas)
- **Author credibility**: GitHub engineering team announcing a production feature
  release in the Eclipse Copilot plugin. Authoritative for the existence and
  described behavior of each feature, the file paths for skills and prompts, and
  the BYOK availability conditions. Not authoritative for: model performance with
  thinking enabled, how thinking effort affects output quality in practice, or
  whether Eclipse's BYOK scope differs from VS Code's documented B&E-only scope.
- **Scope**: Eight features in the June 2026 Eclipse Copilot update — refreshed
  chat view (combo picker), context window usage indicator, BYOK, ABAP support
  improvements, custom instructions loading preference, skills and prompt files,
  thinking blocks, and selectable thinking effort. Does NOT cover: which specific
  models support reasoning/thinking, cost implications of thinking effort levels,
  how Eclipse BYOK policies interact with enterprise governance, or how skills
  installed via `gh skill` CLI map to the `.github/skills/` path.

## Extracted Claims

### Claim 1: The Eclipse Copilot chat view has been refreshed with a new combo picker for selecting chat modes and models in a single UI control

- **Evidence**: Official GitHub product changelog.
- **Confidence**: settled (product fact — the UI update is announced in official changelog)
- **Quote**: "We've refreshed the chat view with a brand new combo picker for selecting chat modes and models."
- **Our assessment**: The combo picker consolidates mode selection (e.g., agent, ask) and
  model selection into a single control. The changelog notes it surfaces "more information
  for each model," indicating the picker includes metadata to help practitioners choose
  between available models in context. This is a UX change, not a capability change, but
  it affects how practitioners navigate model selection in Eclipse — comparable to the
  model picker improvements documented for VS Code and JetBrains IDEs.

### Claim 2: A context window size indicator shows token usage as a donut chart alongside the chat input, with a popup breaking down usage by category

- **Evidence**: Official GitHub product changelog describing a new UI element in the chat view.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "The chat view now shows a context size donut indicator alongside the input area, with a popup that breaks down token usage."
- **Our assessment**: This is the first IDE-level in-chat token usage visualization documented
  in our corpus for Eclipse. Practitioners who work in large codebases with long conversation
  histories can now see at a glance how close they are to context limits without inspecting
  API logs. The "popup that breaks down token usage" implies category-level visibility (e.g.,
  conversation history vs. file attachments vs. system context) — useful for diagnosing which
  context component is consuming the most tokens. For Ch04 (Context Engineering): the donut
  indicator is a practitioner tool for detecting context bloat in real time, complementing
  the guidance on managing context window size.

### Claim 3: BYOK (Bring Your Own Key) is now available in Eclipse for individual users and for Business and Enterprise users when enabled by their organization

- **Evidence**: Official GitHub product changelog.
- **Confidence**: settled (availability stated in official changelog)
- **Quote**: "Bring Your Own Key (BYOK) is now available to individual users as well as GitHub Copilot Business and Enterprise users when enabled by their organization."
- **Our assessment**: This is a notable scope statement. The VS Code BYOK announcement
  (April 22, 2026, `docs-github-copilot-byok-vscode.md`) explicitly scoped BYOK to
  "Copilot Business and Enterprise users" only. This Eclipse changelog includes "individual
  users" alongside Business and Enterprise — though the qualifier "when enabled by their
  organization" applies to the whole statement. Whether "individual users" here means
  Free/Pro plan users (expanding BYOK beyond B&E) or "individual accounts within an org"
  (consistent with the B&E scope) is ambiguous from the changelog text alone. The heading
  for this section on the changelog page reads "Custom models (BYOK) for Copilot Business
  and Enterprise" — suggesting the intended scope is still B&E. The body text's "individual
  users" likely refers to individual members of B&E organizations, not standalone individual
  Copilot plan subscribers. The administrative note confirms the org-dependency: "If you
  don't see custom models enabled, reach out to your organization's administrator to turn
  the feature on." For Ch02: document BYOK as now available in Eclipse IDE in addition to
  VS Code, with the same organization-enablement requirement.

### Claim 4: ABAP development in Eclipse now receives more accurate context-aware chat responses and directory-reading capability within locally cached files

- **Evidence**: Official GitHub product changelog describing expanded language support.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "Copilot now provides more accurate and context-aware chat responses for ABAP projects. It can also read directories and search within the locally cached files."
- **Our assessment**: ABAP (Advanced Business Application Programming) is a language used
  primarily for SAP enterprise development. Eclipse is the canonical IDE for ABAP development
  (via the ABAP Development Tools plugin). This is the first corpus mention of ABAP-specific
  Copilot support. The "locally cached files" qualifier is significant: ABAP projects in
  Eclipse ADT use a local cache of server-side repository objects rather than a traditional
  local file system. Copilot now reads this cache for directory and file content, enabling
  context-aware completions for enterprise SAP developers. This is a niche but high-value
  addition for organizations running SAP workloads.

### Claim 5: Custom instructions in Eclipse can be loaded from all workspace projects (default) or scoped to only referenced projects to reduce irrelevant context

- **Evidence**: Official GitHub product changelog documenting two loading preference options.
- **Confidence**: settled (two options and default stated in official changelog)
- **Quote**: "All projects (default): Load custom instructions from every project in your Eclipse workspace"
- **Quote** (second option): "Referenced projects: Only load instructions from projects whose files or folders are referenced in the current chat"
- **Our assessment**: Eclipse workspaces often contain multiple projects simultaneously (unlike
  VS Code workspaces, which tend to be single-root). Loading custom instructions from all
  workspace projects by default means a developer with 10 projects in their workspace injects
  all 10 projects' custom instruction files into every chat context. The "Referenced projects"
  option provides a relevance filter: only inject instructions from the projects whose files
  are actually part of the current conversation. For Ch04 (Context Engineering): the
  "Referenced projects" mode is the better default for large multi-project workspaces —
  loading all projects' custom instructions regardless of relevance dilutes context with
  irrelevant directives and consumes tokens for instructions that don't apply to the current
  task. Recommend "Referenced projects" mode for practitioners with more than 2–3 projects
  in their Eclipse workspace.

### Claim 6: Skills and prompt files are stored at `.github/skills/` and `.github/prompts/` and triggered via the `/` slash command picker in Eclipse chat

- **Evidence**: Official GitHub product changelog documenting the file paths and invocation
  mechanism for skills and prompt files in Eclipse.
- **Confidence**: settled (paths and invocation mechanism stated in official changelog)
- **Quote**: "To trigger a skill or prompt in chat, type `/` in the chat input box to open the slash command picker"
- **Our assessment**: This confirms that the `.github/skills/` and `.github/prompts/` paths
  — previously documented as part of the `gh skill` CLI ecosystem
  (`docs-github-copilot-agent-skills-cli.md`) — are natively supported in the Eclipse
  Copilot plugin. The slash command picker provides in-chat discovery: practitioners type
  `/` and see available skills and prompts without needing to remember file names. This is
  the IDE-native invocation mechanism that complements the `gh skill install` CLI management
  pattern. For Ch02: document `.github/skills/` and `.github/prompts/` as the project-level
  storage paths for reusable AI instructions, now supported in Eclipse alongside VS Code and
  JetBrains, with the slash command picker as the invocation surface.

### Claim 7: For models that support reasoning, the Eclipse chat view displays thinking blocks showing the AI's reasoning process as expandable sections

- **Evidence**: Official GitHub product changelog.
- **Confidence**: settled (feature described in official changelog; "settled" for the feature
  existing; the broader reasoning model integration is "emerging" as a pattern)
- **Quote**: "For models that support reasoning, the chat view now displays thinking blocks so you can follow Copilot's reasoning process."
- **Our assessment**: This is the first IDE-level in-chat reasoning visibility feature
  documented in our corpus for Eclipse. Thinking blocks (expandable reasoning traces showing
  how the model arrived at an answer before producing its final response) have been documented
  in Claude Code (`blog-anthropic-claudecode-quality-postmortem.md`) and in computer use
  contexts, but this is the first documentation of thinking blocks appearing natively in
  GitHub Copilot chat within an IDE. The "models that support reasoning" qualifier means this
  is model-gated — the feature is only visible when using a reasoning-capable model (likely
  Claude claude-sonnet-4-6 with extended thinking, or similar). For Ch04: thinking blocks provide
  a reasoning audit trail — practitioners can inspect whether the model's reasoning path was
  sound before accepting its output, a form of in-context verification not available with
  non-reasoning models.

### Claim 8: Users can select the thinking effort level for reasoning-capable models, trading reasoning depth for speed

- **Evidence**: Official GitHub product changelog.
- **Confidence**: settled (feature described in official changelog)
- **Quote**: "You can now choose the thinking effort level for supported models. Dial the reasoning depth up for complex problems or keep it light for quick tasks."
- **Our assessment**: This is the first documented user-facing thinking effort control in
  an IDE in our corpus. The framing "dial the reasoning depth up for complex problems or keep
  it light for quick tasks" positions thinking effort as a practitioner decision point:
  high effort for tasks requiring careful multi-step reasoning (debugging complex issues,
  architectural analysis), low effort for simple queries (syntax lookup, quick doc questions).
  This mirrors the thinking effort API parameters available in Anthropic's API (budget_tokens
  parameter for extended thinking), now surfaced as a UI control in Eclipse. For Ch04: add
  thinking effort selection as an IDE-level cost/quality knob: high effort produces more
  thorough reasoning but takes longer and may consume more tokens; low effort is faster but
  produces less extensive reasoning traces. Document as a practitioner-controlled latency/
  quality tradeoff in Copilot chat with reasoning models.

## Concrete Artifacts

### Feature Inventory — Eclipse Copilot Plugin (June 2, 2026)

```
GitHub Copilot in Eclipse — June 2, 2026 Updates

CHAT UI:
  - New combo picker: mode + model selection in single control
    ("a brand new combo picker for selecting chat modes and models")
  - Context size donut indicator: token usage visualization
    ("a popup that breaks down token usage")

BYOK (CUSTOM MODELS):
  Section heading: "Custom models (BYOK) for Copilot Business and Enterprise"
  Availability: individual users + Business + Enterprise, "when enabled by their organization"
  Admin action: "reach out to your organization's administrator to turn the feature on"

LANGUAGE SUPPORT:
  - ABAP: context-aware responses + directory reading in locally cached files

CUSTOM INSTRUCTIONS:
  Two loading preference options:
    "All projects (default): Load custom instructions from every project in your Eclipse workspace"
    "Referenced projects: Only load instructions from projects whose files or folders are referenced in the current chat"

SKILLS AND PROMPT FILES:
  Storage paths:
    Skills:  /.github/skills/my-skill/SKILL.md
    Prompts: /.github/prompts/my-prompt.prompt.md
  Invocation: type `/` in chat input → slash command picker
  ("To trigger a skill or prompt in chat, type `/` in the chat input box to open the slash command picker")

REASONING FEATURES:
  Thinking blocks: expandable reasoning traces in chat view
    "For models that support reasoning, the chat view now displays thinking blocks so you can follow Copilot's reasoning process."
  Selectable thinking effort:
    "You can now choose the thinking effort level for supported models."
    "Dial the reasoning depth up for complex problems or keep it light for quick tasks."
```

### Skills and Prompts File Paths (Eclipse)

```
GitHub Copilot Eclipse — Skills and Prompt Files Storage

SKILLS:
  Path:   .github/skills/<skill-name>/SKILL.md
  Example: .github/skills/my-skill/SKILL.md

PROMPTS:
  Path:   .github/prompts/<prompt-name>.prompt.md
  Example: .github/prompts/my-prompt.prompt.md

INVOCATION:
  In Eclipse chat input:  type "/"  → slash command picker opens
  Shows all available skills and prompts from repository

MANAGEMENT (via gh CLI, separate feature):
  gh skill install <owner>/<repo> <skill-name>
  → installs to .github/skills/ (and other agent-host-specific paths)
```

### Custom Instructions Loading Modes (Eclipse)

```
Eclipse Copilot — Custom Instructions Loading Preference

Option 1: "All projects" (DEFAULT)
  → Loads custom instructions from every project in Eclipse workspace
  → Risk: all projects' instructions injected regardless of relevance
  → Best for: small workspaces (1-2 projects)

Option 2: "Referenced projects"
  → Loads instructions only from projects referenced in current chat
  → Reduces irrelevant context for large multi-project workspaces
  → Best for: workspaces with 3+ projects
```

## Cross-References

- **Corroborates** `docs-github-copilot-byok-vscode.md` (issue #346):
  VS Code BYOK (April 22, 2026) established the core BYOK pattern — provider API keys
  enabling custom model access within Copilot chat, billed directly by the provider and
  not against Copilot quotas. This Eclipse source documents BYOK reaching the Eclipse IDE
  as a second host. The fundamental BYOK mechanics (configure API keys, access custom models
  in chat, billing via provider) are consistent across both sources.

- **Corroborates** `docs-github-copilot-agent-skills-cli.md` (issue #189, Claim 5):
  That source documented the `.github/skills/` path as the standard storage location
  for skills that work across agent hosts via the `gh skill` CLI. This Eclipse source
  confirms that Eclipse is a supported host for the `.github/skills/` path, with the
  slash command picker as the in-IDE invocation mechanism. Together these two sources
  confirm `.github/skills/` and `.github/prompts/` as cross-IDE standard paths.

- **Corroborates** `docs-github-copilot-jetbrains-cli-agent-sessions.md` (issue #744):
  The JetBrains source documented a unified sessions view and the pattern of extending
  Copilot agent capabilities into IDEs beyond VS Code. This Eclipse source is a further
  extension of the same pattern to another non-VS Code IDE. Together they show GitHub
  executing a cross-IDE feature parity rollout: VS Code → JetBrains → Eclipse.

- **Extends** `docs-github-copilot-byok-vscode.md` (issue #346, Claim 1):
  The VS Code BYOK source documented BYOK as "Copilot Business and Enterprise users" only.
  This Eclipse source's "individual users as well as" phrasing introduces an ambiguity
  about plan scope (see Claim 3 and Extraction Notes). The section heading "Custom models
  (BYOK) for Copilot Business and Enterprise" and the org-admin enablement requirement
  suggest the intended scope remains B&E, but the exact wording differs from VS Code's
  announcement. This scope question warrants tracking as Eclipse BYOK documentation matures.

- **Extends** `docs-github-copilot-agent-skills-cli.md` (issue #189):
  The CLI skills source documented the `gh skill` distribution and management model. This
  Eclipse source adds the in-IDE consumption layer: skills stored at `.github/skills/` are
  surfaced via the slash command picker. Together: `gh skill install` manages skills;
  `/` in chat invokes them. The distribution and invocation layers now both have documented
  implementations.

- **Novel**:
  - **Eclipse IDE Copilot support documented for first time**: No prior source in corpus
    covers GitHub Copilot features in Eclipse. VS Code, JetBrains, and Visual Studio have
    prior notes; Eclipse is new to the corpus.
  - **Thinking blocks in IDE chat**: First documentation of thinking blocks (expandable
    reasoning traces) appearing natively in GitHub Copilot chat within any IDE. Prior
    thinking block references in corpus (`blog-anthropic-claudecode-quality-postmortem.md`)
    cover Claude Code context management, not IDE chat display.
  - **Selectable thinking effort as IDE UI control**: First corpus documentation of a
    user-facing thinking effort selector in an IDE. Prior corpus sources document thinking
    effort as an API parameter (budget_tokens in Anthropic SDK) or as a product-level
    feature (`blog-anthropic-computer-use-best-practices.md`), not as an in-chat IDE control.
  - **Context window usage donut indicator**: First corpus documentation of in-chat visual
    token usage feedback in any IDE. Context window management guidance in Ch04 has no prior
    source documenting an IDE tool for this.
  - **Custom instructions scope control (all projects vs. referenced)**: First corpus
    documentation of user-configurable custom instruction loading scope. Prior custom
    instruction sources treat loading as automatic or uniform.
  - **ABAP support via locally cached files**: First and only corpus mention of ABAP support
    in any Copilot IDE integration.
  - **Slash command picker for skills/prompts invocation**: First corpus documentation of
    in-IDE slash command discovery for skills and prompt files.

## Guide Impact

### Chapter 02: Harness Engineering

- **Eclipse as a third supported IDE**: Add Eclipse to the IDE support matrix alongside VS
  Code and JetBrains. Document that skills (`.github/skills/`) and prompts (`.github/prompts/`)
  work across all three IDEs, with slash command invocation available in Eclipse. BYOK is
  available in Eclipse with organization enablement requirement.
- **Slash command invocation for skills**: Ch02 should document the in-IDE invocation pattern:
  type `/` in chat to access installed skills and prompts from `.github/skills/` and
  `.github/prompts/`. This complements the `gh skill install` CLI management pattern from
  `docs-github-copilot-agent-skills-cli.md` with the in-IDE usage layer.
- **Custom instructions scope control**: Add guidance that Eclipse practitioners with large
  multi-project workspaces should use "Referenced projects" mode for custom instructions
  loading to avoid injecting irrelevant project-specific instructions into every chat session.
  This is the first harness configuration surface that addresses custom instruction relevance
  filtering at the workspace level.

### Chapter 04: Context Engineering

- **Thinking effort as a quality/latency knob**: Add thinking effort selection to the model
  selection guidance. For Eclipse users with reasoning-capable models: high thinking effort
  for complex multi-step problems (architecture decisions, complex debugging), low thinking
  effort for quick lookups (syntax, API signatures). Document as an IDE-level control with
  latency and token-consumption implications.
- **Thinking blocks for in-context verification**: Thinking blocks display the model's
  reasoning process before the final answer. Add this to context verification patterns:
  practitioners can inspect whether the model's reasoning path reached the right intermediate
  conclusions before accepting its output — especially useful for debugging where incorrect
  reasoning may be visible in the thinking block before the wrong answer appears.
- **Context window donut indicator**: Add the donut indicator as an IDE tool for context
  management in Eclipse. The popup breakdown by category enables practitioners to identify
  which context component (conversation history, attached files, project instructions) is
  consuming the most tokens, enabling targeted context reduction before hitting limits.
- **Custom instructions scope as context control**: The "Referenced projects" vs. "All
  projects" loading choice directly affects token consumption and instruction relevance.
  Frame this as a context engineering decision: load fewer, more relevant instructions for
  focused tasks; load all instructions only when the task genuinely spans multiple projects.

### Chapter 05: Team Adoption

- **Cross-IDE skills strategy**: With VS Code, JetBrains, and now Eclipse all supporting
  `.github/skills/` and `.github/prompts/`, teams can maintain a single shared skill/prompt
  library in their repository's `.github/` directory and have it available consistently
  across all three IDEs. Document this as the recommended team-level skills organization
  pattern for multi-IDE shops.
- **ABAP/SAP teams**: Organizations running SAP workloads with ABAP development in Eclipse
  can now leverage Copilot's ABAP support including directory reading in the local cache.
  For teams considering Copilot adoption across a mixed-language shop that includes SAP
  development, Eclipse BYOK and ABAP support reduce the tooling gap that previously
  required separate AI coding tools for ABAP vs. other languages.

## Extraction Notes

1. **Source is a changelog (~600 words)**: All eight feature sections were read and extracted.
   All claims above are exhausted from the available content. No sub-pages were followed
   (the changelog is self-contained).

2. **BYOK scope ambiguity**: The Eclipse BYOK announcement uses "individual users as well as
   GitHub Copilot Business and Enterprise users when enabled by their organization." The VS
   Code BYOK source (April 2026) said "Copilot Business and Enterprise users" only. The
   Eclipse changelog's section heading says "Custom models (BYOK) for Copilot Business and
   Enterprise" — suggesting the body text's "individual users" refers to individual org
   members, not Free/Pro plan holders. However, this ambiguity was not resolved by the
   changelog text. A potential semantic expansion between April and June 2026 is also
   possible. No contradiction issue filed (the difference is ambiguous and may be terminology
   rather than a substantive policy difference), but this should be verified against GitHub
   documentation.

3. **Specific reasoning models not named**: The changelog says "models that support reasoning"
   without naming which models qualify. Based on the Copilot model roster (Claude claude-sonnet-4-6,
   Claude Opus 4.8), reasoning models with thinking capability are likely Claude models with
   extended thinking enabled. No inference was drawn beyond what the source states.

4. **Thinking effort levels not enumerated**: The changelog does not name specific thinking
   effort levels (e.g., "low / medium / high") — only the capability to select them is
   documented. The exact UI options are not specified in this source.

5. **Two WebFetch calls made**: Content was fetched twice with different prompts. The second
   fetch returned fuller verbatim quote coverage. Results were consistent between fetches.
   Per MINER.md §2a, all quotes were verified against the second fetch result.

6. **No contradictions to file**: The BYOK scope ambiguity (Extraction Note 2) is a
   terminology uncertainty rather than a material contradiction — both sources could be
   simultaneously true (B&E only, with "individual users" meaning individual org members).
   No existing source note makes a claim that would be directly refuted by this source. No
   contradiction issue filed.
