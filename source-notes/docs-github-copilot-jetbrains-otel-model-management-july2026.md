---
source_url: https://github.blog/changelog/2026-07-27-github-copilot-for-jetbrains-adds-improvved-opentelemetry-configuration-and-model-management
source_type: docs
title: "GitHub Copilot for JetBrains adds improved OpenTelemetry configuration and model management"
author: GitHub (official changelog)
date_published: 2026-07-27
date_extracted: 2026-07-28
last_checked: 2026-07-28
status: current
confidence_overall: settled
issue: "#2270"
---

# GitHub Copilot for JetBrains Adds Improved OpenTelemetry Configuration and Model Management

> GitHub's July 27, 2026 JetBrains changelog adds practitioner-configurable OpenTelemetry
> export for agent workflows, default token-limit controls (`maxInputToken`/`maxOutputToken`)
> and a built-in-model kill switch for cost/model governance, MCP server and custom-agent
> support inside Claude agent flows (a capability not previously documented for the JetBrains
> Claude integration), and three new Copilot CLI session capabilities (forks, `/rubber-duck`,
> and an in-harness todo list) — plus AI-credit visibility for enterprises that haven't
> configured a user-level budget.

## Source Context

- **Type**: docs (GitHub official product changelog, July 27, 2026; ~300 words across a "What's
  new" section with four named feature groups, a "User experience enhancements" section with
  six polish items, and a one-line "Quality improvements" note)
- **Author credibility**: GitHub engineering team announcing production feature releases for the
  JetBrains Copilot plugin. Authoritative for: the existence and stated behavior of each feature,
  the exact settings path for OpenTelemetry configuration, the token-limit field names, and which
  session capabilities are new. Not authoritative for: what OTLP fields or exporters the
  OpenTelemetry export actually supports (the changelog names only the settings location, not the
  configuration schema), how `maxInputToken`/`maxOutputToken` interact with server-side model
  context limits, or how MCP servers are wired into Claude agent flows technically (transport,
  auth, discovery).
- **Scope**: Four "What's new" feature groups (OpenTelemetry export, model behavior controls, MCP
  servers/custom agents in Claude agent flows, CLI session capabilities), one cost-visibility
  item, six UX polish items, and one quality/reliability fix — all in the July 27, 2026 JetBrains
  Copilot update. Does NOT cover: the OpenTelemetry configuration schema (endpoint, exporter
  protocol, sampling), the mechanics of MCP server registration for Claude agent flows, whether
  the token-limit controls are enforced client-side or server-side, or plan-tier/preview-status
  gating for any of these features (none of the "What's new" items in this changelog carry an
  explicit preview or plan-tier qualifier, unlike the July 14 JetBrains changelog's Claude
  customizations feature).

## Extracted Claims

### Claim 1: JetBrains Copilot users can now configure OpenTelemetry export settings for agent workflows, under Settings > Tools > GitHub Copilot > Chat, to align plugin behavior with organizational observability requirements

- **Evidence**: Official changelog "What's new" section, "OpenTelemetry export for agent
  workflows" heading, with an explicit settings path.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "You can now configure OpenTelemetry export settings for agent workflows. This
  makes it easier to align plugin behavior with your organization's requirements for
  observability. You can configure this under Settings > Tools > GitHub Copilot > Chat."
- **Our assessment**: This is the first corpus source documenting OpenTelemetry as a
  practitioner-configurable, settings-UI-level capability of a GitHub Copilot IDE plugin itself
  (as opposed to OpenTelemetry appearing at the MCP-gateway/workflow-infrastructure layer, per
  `docs-ghaw-mcp-gateway-reference.md` Claim 9, which documents `gateway.opentelemetry.endpoint`
  and `gateway.opentelemetry.serviceName` for GitHub Agentic Workflows' MCP gateway). The
  changelog names only the settings location, not the underlying schema (OTLP endpoint,
  protocol, sampling, service name) — the same category of gap the Assayer flagged for the
  July 14 local-sandboxing feature in `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`
  (Claim 4), where the mechanics were deferred to a separate docs page. No equivalent "learn
  more" link is present in this changelog for OpenTelemetry, so the configuration schema is
  presently undocumented outside the plugin's own settings UI. For Ch02 (harness engineering —
  observability): document this as the settings-UI entry point for agent-workflow tracing/export
  in JetBrains; flag the schema as unverified pending direct inspection of the settings panel.

### Claim 2: Practitioners can now set default `maxInputToken` and `maxOutputToken` limits for BYOK and custom endpoints, and can globally disable or enable all built-in Copilot models, for cost control and model governance

- **Evidence**: Official changelog "What's new" section, "More control over model behavior"
  heading, naming both token-limit fields and the model on/off toggle explicitly.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "You can now set default token limits, including maxInputToken and maxOutputToken,
  for BYOK and custom endpoints. You can also disable or enable all built-in Copilot models from
  model-management controls. These options make it easier to align plugin behavior with your
  organization's requirements for cost control and model governance."
- **Our assessment**: This extends the BYOK custom-endpoint capability added July 14
  (`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`, Claim 1: "You can now configure
  OpenAI-compatible custom endpoints with API keys to use your own models") with governance
  controls that were absent from that source: the July 14 note documented *how to add* a custom
  endpoint but not how to bound its token usage. `maxInputToken`/`maxOutputToken` as named,
  per-endpoint default limits is new to the corpus — no prior source names these exact field
  names for JetBrains. This is a different cost-control layer than the session-scoped AI-credit
  spend cap documented in `docs-github-copilot-cli-sdk-session-credit-limits.md` (a soft
  `/limits`/`--max-ai-credits` cap on total credit spend per session): `maxInputToken`/
  `maxOutputToken` cap token counts per request/model configuration, not credits per session.
  The blanket enable/disable-all-built-in-models toggle is coarser than the per-model policy
  rules documented in `docs-github-copilot-org-targeted-model-rules.md` (not independently
  re-verified in this extraction) — worth flagging to the Assayer as a possible overlap to
  reconcile. For Ch02 (harness engineering — model governance): document `maxInputToken`/
  `maxOutputToken` as the new default-limit fields for BYOK/custom endpoints in JetBrains, and
  the built-in-model kill switch as a coarse, plugin-wide governance control distinct from
  session credit caps and org-level model policy rules.

### Claim 3: MCP servers and custom agents can now be used directly within Claude agent flows in JetBrains, for specialized tools, custom instructions, or team-specific workflows

- **Evidence**: Official changelog "What's new" section, "MCP servers and custom agents in
  Claude agent flows" heading.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "You can now use MCP servers and custom agents directly in Claude agent flows. This
  gives you more flexibility when you need specialized tools, custom instructions, or
  team-specific workflows in your IDE. If you rely on shared agent setups across projects, this
  update helps you keep your flow consistent while still adapting to repository-specific needs."
- **Our assessment**: This is genuinely new to the corpus's coverage of the JetBrains Claude
  integration. Neither prior JetBrains-Claude source mentions MCP: the June 22 introduction of
  Claude as an agent provider (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`,
  Claim 1) covered only provider selection and noted the agent "currently runs in bypass
  permissions mode" (Claim 2); the July 14 note's Claude customizations feature
  (`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`, Claim 3) covered "custom agents,
  skills, and instructions" scoped to Pro-and-higher plans but did not mention MCP servers as
  part of that customization surface. This July 27 entry is therefore the first documented
  connection between MCP tooling and the Claude-as-agent-provider integration in JetBrains — it
  implies MCP servers configured for the native Copilot agent are now also reachable when Claude
  is the selected agent backend, though the changelog does not state whether this is the same MCP
  configuration surface used by the native Copilot agent or a Claude-specific one. For Ch02
  (harness engineering — MCP configuration): note that MCP servers are now usable inside
  Claude-backed JetBrains sessions, extending the "shared agent setups across projects" pattern
  to the Claude provider; flag the configuration-surface question (shared vs. Claude-specific MCP
  config) as unresolved and worth a follow-up source.

### Claim 4: Copilot CLI sessions in JetBrains now support forking a session, invoking the `/rubber-duck` command, and showing a todo list in the harness, to help break down work and keep progress visible

- **Evidence**: Official changelog "What's new" section, "More Copilot CLI session capabilities"
  heading, naming all three capabilities together.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "Copilot CLI sessions now support forks, include the /rubber-duck command, and show
  a todo list in the harness. These additions help you break down work, reason through
  implementation ideas, and keep progress visible while you iterate."
- **Our assessment**: This bundles one genuinely new capability with two that extend prior
  corpus coverage. Session forking is new: no prior JetBrains source (checked
  `docs-github-copilot-jetbrains-cli-agent-sessions.md`, worktree/workspace isolation modes, and
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, session management commands)
  documents a fork operation on a running CLI session. `/rubber-duck` is not new as a
  capability — it reached GA in the standalone Copilot CLI on June 2, 2026
  (`docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, Claim 1: "Rubber duck is a
  built-in CLI agent that acts as a constructive critic") — but this is the first source
  documenting it as available specifically inside JetBrains-embedded CLI sessions, i.e., the
  standalone-CLI feature has now propagated into the IDE-embedded CLI surface. The todo list
  in the harness is also new to the corpus: no prior source documents an in-CLI task-list
  display (distinct from the Agent Debug Panel's chronological event log documented in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 5, which logs agent
  activity rather than tracking a practitioner-facing task breakdown). The changelog does not
  say whether forking creates an independent worktree/workspace (per the May 13 isolation-mode
  model) or a lighter-weight session-state branch, or whether the todo list is agent-generated,
  practitioner-editable, or both. For Ch01 (daily workflows) and Ch02 (harness engineering):
  document session forking and the in-harness todo list as new JetBrains CLI primitives, and
  update the `/rubber-duck` guide entry to note that JetBrains-embedded CLI sessions now carry
  this GA standalone-CLI capability — flag the fork mechanics and todo-list authorship model as
  open questions pending a docs page or hands-on verification.

### Claim 5: For enterprise organizations that have not configured a user-level budget, JetBrains Copilot now displays the number of AI credits consumed

- **Evidence**: Official changelog "What's new" section, "Cost efficiency" heading, with a link
  to a separate docs page ("our docs about user-level budgets") defining what a user-level
  budget is. That linked page (`docs.github.com/copilot/concepts/billing/budgets-for-usage-based-billing#user-level-budget`)
  was followed as part of this extraction.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "For enterprise users, we now display the number of AI credits consumed when their
  organization has not configured a user-level budget."
- **Quote (linked docs page, for context on what a user-level budget is)**: "The user-level
  budget (ULB) caps how many AI credits a single user can consume in a billing cycle—both from
  the shared pool and from additional (metered) usage." (source: linked "user-level budgets"
  docs page, not the changelog itself)
- **Our assessment**: This closes a visibility gap specifically for the no-ULB-configured case —
  previously, enterprises without a configured user-level budget apparently had no in-plugin
  signal of per-user AI credit consumption inside JetBrains. This complements, but is narrower
  than, `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 7, which
  documented a per-turn AI credits indicator shown inline "for local, CLI, and Claude agent
  sessions" as of June 22, 2026 — that earlier feature did not condition on ULB configuration
  status. It's unclear from this changelog whether the new July 27 display is the same per-turn
  indicator now extended to a wider condition, or a separate/aggregate display; the phrasing
  ("the number of AI credits consumed," not "per-turn") suggests an aggregate or session-total
  figure rather than the per-turn indicator. For Ch01 (daily workflows — cost awareness):
  document this as a narrower cost-visibility improvement — enterprises without a configured
  user-level budget now see AI credit consumption directly in JetBrains — and flag the open
  question of whether it duplicates or extends the June 22 per-turn indicator.

### Claim 6: Session prompts (ask-user questions) are now rendered as Markdown with explicit user-attention notifications, for improved clarity

- **Evidence**: Official changelog "User experience enhancements" section, "Session prompts"
  bullet.
- **Confidence**: settled (product fact stated definitively)
- **Quote**: "Session prompts: Improved clarity by rendering ask-user questions as Markdown and
  adding explicit user-attention notifications."
- **Our assessment**: Two distinct improvements bundled in one bullet: (1) ask-user questions
  (the agent's mid-task clarifying questions to the practitioner) now render as formatted
  Markdown rather than plain text, which matters for questions containing code snippets, lists,
  or options that benefit from structure; (2) "explicit user-attention notifications" implies a
  new UI signal (e.g., a badge or highlight) that surfaces when the agent is blocked waiting on
  practitioner input — addressing the failure mode where a practitioner starts a long agent task,
  switches away, and doesn't notice the agent has stalled awaiting a response. No prior corpus
  source documents an explicit attention/notification mechanism for agent-blocked-on-user-input
  states in JetBrains. For Ch01 (daily workflows): note the attention-notification mechanism as
  relevant to practitioners who run agent sessions in the background while multitasking — it
  reduces the risk of an agent session idling unnoticed on a clarifying question.

### Claim 7: Copilot CLI now preserves path capitalization more reliably in working sets and snapshots on macOS and Linux

- **Evidence**: Official changelog "Quality improvements" section, the sole "Quality
  improvements" sentence.
- **Confidence**: settled (product fact stated definitively, framed as a reliability fix)
- **Quote**: "This release also improves path handling and session recording. Copilot CLI now
  preserves path capitalization more reliably in working sets and snapshots on macOS and Linux."
- **Our assessment**: This is a narrow but concrete correctness fix: on case-insensitive-but-
  case-preserving filesystems (macOS default, and some Linux configurations), a CLI that
  normalizes or loses path-capitalization information when recording "working sets" or
  "snapshots" could cause file-identity mismatches — e.g., treating `Foo.ts` and `foo.ts` as the
  same file, or failing to reopen a snapshot's referenced file if capitalization was mangled.
  The changelog does not name the prior failure mode explicitly, only the fix. For Ch03
  (verification — environment reliability): a minor but worth-noting item for teams that have
  hit path-casing bugs with Copilot CLI's session snapshot/restore feature on macOS; this
  changelog entry is evidence GitHub has addressed at least one class of that bug, but does not
  establish the fix is complete for all path-capitalization scenarios.

## Concrete Artifacts

### Full "What's New" Section (verbatim, JetBrains Copilot changelog, July 27, 2026)

```
Lead sentence:
"This update brings more control and clarity to your GitHub Copilot for
JetBrains workflows. You can now connect MCP servers and custom agents in
Claude agent flows, tune telemetry and token settings for advanced
scenarios, and work with a cleaner chat and model-selection experience."

What's new:

1. OpenTelemetry export for agent workflows
   "You can now configure OpenTelemetry export settings for agent
   workflows. This makes it easier to align plugin behavior with your
   organization's requirements for observability. You can configure this
   under Settings > Tools > GitHub Copilot > Chat."

2. More control over model behavior
   "You can now set default token limits, including maxInputToken and
   maxOutputToken, for BYOK and custom endpoints. You can also disable
   or enable all built-in Copilot models from model-management controls.
   These options make it easier to align plugin behavior with your
   organization's requirements for cost control and model governance."

3. MCP servers and custom agents in Claude agent flows
   "You can now use MCP servers and custom agents directly in Claude
   agent flows. This gives you more flexibility when you need specialized
   tools, custom instructions, or team-specific workflows in your IDE.
   If you rely on shared agent setups across projects, this update helps
   you keep your flow consistent while still adapting to
   repository-specific needs."

4. More Copilot CLI session capabilities
   "Copilot CLI sessions now support forks, include the /rubber-duck
   command, and show a todo list in the harness. These additions help
   you break down work, reason through implementation ideas, and keep
   progress visible while you iterate."

5. Cost efficiency
   "For enterprise users, we now display the number of AI credits
   consumed when their organization has not configured a user-level
   budget. For more information, see our docs about user-level budgets."
```

*Source: GitHub Copilot for JetBrains adds improved OpenTelemetry configuration and model
management, GitHub changelog, July 27, 2026*

### User Experience Enhancements and Quality Improvements (verbatim)

```
User experience enhancements:
"We are also enhancing day-to-day experience across chat, inline chat,
and model selection."

- Model and action picker: "Improved consistency so controls are easier
  to predict and use."
- Customization flows: "Improved usability so creating and managing
  setup details takes less effort."
- Session prompts: "Improved clarity by rendering ask-user questions as
  Markdown and adding explicit user-attention notifications."
- Inline chat and model picker layout: "Improved layout behavior for
  cleaner interactions."
- MCP diagnostics: "Improved diagnostics to help you understand
  configuration and runtime issues faster."
- URL rendering in Copilot CLI harness: "Improved bare URL display for
  better readability in chat output."

Quality improvements:
"This release also improves path handling and session recording. Copilot
CLI now preserves path capitalization more reliably in working sets and
snapshots on macOS and Linux."
```

*Source: GitHub Copilot for JetBrains adds improved OpenTelemetry configuration and model
management, GitHub changelog, July 27, 2026*

### Page Section Structure (as fetched)

```
GitHub Copilot for JetBrains adds improved OpenTelemetry configuration
and model management (Release, July 27, 2026, 2 minute read)
├── What's new
│   ├── OpenTelemetry export for agent workflows
│   ├── More control over model behavior
│   ├── MCP servers and custom agents in Claude agent flows
│   ├── More Copilot CLI session capabilities
│   └── Cost efficiency
├── User experience enhancements (6 bullets)
├── Quality improvements (1 sentence)
├── Try it out
└── Share your feedback
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcp-gateway-reference.md` (Claim 9): That source documents OpenTelemetry as the
    observability primitive for GitHub Agentic Workflows' MCP gateway
    (`gateway.opentelemetry.endpoint`, `gateway.opentelemetry.serviceName`, 10 T-OTEL compliance
    test cases). This note's Claim 1 corroborates that OpenTelemetry is GitHub's standard
    observability integration point for agent tooling, now confirmed at a second, distinct layer
    (JetBrains IDE plugin settings) in addition to the MCP gateway layer — the two sources
    describe different products (Copilot plugin vs. gh-aw MCP gateway) converging on the same
    tracing standard.
  - `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 1): That source established
    `/rubber-duck` as a GA, constructive-critic CLI agent in the standalone Copilot CLI (June 2,
    2026). This note's Claim 4 corroborates that `/rubber-duck` exists as described and confirms
    it is now reachable from JetBrains-embedded CLI sessions as well.
  - `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 1): That source documented
    OpenAI-compatible custom-endpoint BYOK support added to JetBrains on July 14, 2026. This
    note's Claim 2 corroborates that custom endpoints are a live JetBrains BYOK mechanism and
    extends it with token-limit governance controls not present in the July 14 note.

- **Contradicts**: None identified. No existing corpus source makes a claim that opposes any
  claim in this note. No contradiction issue filed.

- **Extends**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claims 1, 2, 7): The
    June 22 note established Claude as a selectable JetBrains agent provider, running in bypass
    permissions mode, with a per-turn AI credits indicator. This note's Claim 3 extends that
    integration with MCP server and custom-agent support inside Claude agent flows — a
    capability neither the June 22 note nor the July 14 customizations note documented. This
    note's Claim 5 (cost efficiency for no-ULB enterprises) sits alongside, and may overlap with,
    the June 22 per-turn credits indicator (Claim 7) — the relationship between the two is not
    stated in either source (see Claim 5 assessment).
  - `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 1, Claim 3): This note's
    Claim 2 extends the July 14 BYOK custom-endpoint capability with `maxInputToken`/
    `maxOutputToken` default limits and a built-in-model kill switch — governance controls that
    did not exist in the July 14 feature set. This note's Claim 3 (MCP in Claude flows) extends
    Claim 3 of the July 14 note (Claude customizations: "custom agents, skills, and
    instructions," Pro-and-higher, public preview) by adding MCP servers to what can be wired
    into a Claude-backed agent — the July 14 note's customization scope did not mention MCP.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 2, worktree/workspace isolation)
    and `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (session-management slash
    commands): This note's Claim 4 (session forking, todo list) extends the JetBrains CLI
    session model established by these two sources with a new fork operation and an in-harness
    todo list, neither of which either prior source documents.
  - `docs-github-copilot-cli-sdk-session-credit-limits.md`: That source documented a
    session-scoped AI-credit spend cap (`/limits`, `--max-ai-credits`) as a cost-control layer
    "beneath org/user budgets and above per-request model-cost optimization." This note's Claim 2
    (`maxInputToken`/`maxOutputToken`) adds a token-count-based control at the per-request/
    per-endpoint level, distinct from both the credit-based session cap and the org/user budget
    layer described in that note.

- **Novel**:
  - **OpenTelemetry export as a JetBrains plugin-settings-level, practitioner-configurable
    capability** (Claim 1): First corpus source documenting OTel configuration inside a GitHub
    Copilot IDE plugin's own settings UI (as opposed to workflow/gateway infrastructure).
  - **Named `maxInputToken`/`maxOutputToken` default-limit fields for BYOK/custom endpoints in
    JetBrains, plus a blanket built-in-model enable/disable toggle** (Claim 2): No prior corpus
    source names these exact fields or this toggle for JetBrains.
  - **MCP servers usable inside Claude agent flows in JetBrains** (Claim 3): First corpus source
    connecting MCP tooling to the Claude-as-agent-provider integration in any surface.
  - **CLI session forking in JetBrains** (Claim 4): First corpus source documenting a fork
    operation on a running Copilot CLI session (JetBrains or standalone).
  - **In-harness todo list for Copilot CLI sessions** (Claim 4): First corpus source documenting
    a practitioner-facing task-list display distinct from the Agent Debug Panel's event log.
  - **Explicit user-attention notifications for agent-blocked-on-input states** (Claim 6): First
    corpus source documenting a dedicated UI signal for when an agent session is stalled awaiting
    practitioner input.

## Guide Impact

- **Chapter 02 (Harness Engineering — Observability)**: Add JetBrains's OpenTelemetry export
  setting (Settings > Tools > GitHub Copilot > Chat) as a practitioner-facing observability
  configuration point (Claim 1), alongside the existing MCP-gateway-level OTel coverage from
  `docs-ghaw-mcp-gateway-reference.md`. Flag that the export schema (endpoint, protocol,
  sampling) is not documented in the changelog and should be verified directly in the settings
  panel before the guide states specifics.

- **Chapter 02 (Harness Engineering — Model/Cost Governance)**: Add `maxInputToken`/
  `maxOutputToken` default limits and the built-in-model enable/disable toggle (Claim 2) to the
  guide's inventory of JetBrains model-governance controls, distinguishing this token-count-based
  control from the session-scoped AI-credit cap (`docs-github-copilot-cli-sdk-session-credit-limits.md`)
  and org-level model policy rules.

- **Chapter 02 (Harness Engineering — MCP Configuration)**: Note that MCP servers and custom
  agents are now usable inside Claude-backed agent flows in JetBrains (Claim 3) — update any
  guide language that scoped MCP availability to the native Copilot agent only. Flag the open
  question of whether this is a shared or Claude-specific MCP configuration surface.

- **Chapter 01 (Daily Workflows)**: Document CLI session forking and the in-harness todo list
  (Claim 4) as new JetBrains CLI primitives for breaking down and tracking work. Update the
  existing `/rubber-duck` guidance to note it is now available inside JetBrains-embedded CLI
  sessions, not just the standalone CLI. Add the session-prompt Markdown rendering and
  user-attention notification (Claim 6) as a mitigation for the "agent stalled awaiting input,
  unnoticed" failure mode during multitasking.

- **Chapter 01 (Daily Workflows — Cost Awareness)**: Add the no-ULB-configured AI-credit-consumed
  display (Claim 5) as a narrower cost-visibility improvement for enterprises, while flagging
  that its relationship to the existing per-turn AI credits indicator
  (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, Claim 7) is unresolved.

- **Chapter 03 (Verification — Environment Reliability)**: Note the path-capitalization fix for
  Copilot CLI working sets/snapshots on macOS and Linux (Claim 7) as a minor but concrete
  reliability improvement relevant to teams that have encountered path-casing issues with
  session snapshot/restore.

## Extraction Notes

1. **WebFetch vs. raw HTML**: An initial WebFetch call returned a plausible-looking but
   AI-summarized version of the page. Per MINER.md §2a, this extraction instead fetched the raw
   HTML directly via `curl`, stripped tags, and HTML-entity-decoded the result (`&rsquo;` → `’`,
   `&gt;` → `>`, etc.) to obtain verbatim text before writing any Quote field. All quotes above
   were copied from that decoded raw-text extraction, not from the WebFetch summary.
2. **One linked page followed**: the "our docs about user-level budgets" link
   (`docs.github.com/copilot/concepts/billing/budgets-for-usage-based-billing#user-level-budget`)
   was fetched to clarify what "has not configured a user-level budget" means for Claim 5. Three
   other links on the page (JetBrains plugin marketplace listing, feedback survey, feedback issue
   repository) are navigational/feedback-channel links, not substantive content, and were not
   followed. A fourth link to a July 23 "Agent automation controls in GitHub Issues" related post
   is unrelated to this changelog's content and was not followed.
3. **No preview/plan-tier qualifiers found**: unlike the July 14 JetBrains changelog (which
   explicitly scoped Claude customizations to "GitHub Copilot Pro and higher plans" in "public
   preview"), none of the five "What's new" items in this July 27 changelog carry an explicit
   preview or plan-tier label. This extraction treats them as generally available product facts
   (`confidence: settled`) on that basis, but flags for the Assayer that the absence of a stated
   qualifier is not the same as an explicit "generally available" statement — the changelog simply
   doesn't address rollout status for these five items.
4. **URL typo in source**: the changelog's own URL contains a typo ("improvved" instead of
   "improved") while the page `<title>` and headings use the correct spelling. This is presumably
   a publishing artifact on GitHub's end, not an extraction error — the URL was used exactly as
   provided in the issue body and resolves with HTTP 200.
5. **No contradictions filed**: no existing corpus source makes a claim that opposes any claim in
   this note. See Cross-References → Contradicts.
