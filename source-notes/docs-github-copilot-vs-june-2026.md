---
source_url: https://github.blog/changelog/2026-07-14-github-copilot-in-visual-studio-june-update
source_type: docs
title: "GitHub Copilot in Visual Studio — June 2026 Update"
author: GitHub (official changelog)
date_published: 2026-07-14
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: settled
issue: "#1917"
---

# GitHub Copilot in Visual Studio — June 2026 Update

> GitHub's July 14, 2026 changelog for Copilot in Visual Studio frames the release around
> "visibility and trust": a real-time, IDE-native usage/billing window; a two-stage
> configuration-and-fingerprint trust-validation system for MCP servers (explicitly designed
> to defeat "rug-pull" tool-redefinition attacks, per the companion Microsoft Learn docs); the
> first C++/MSVC scenarios for the modernization agent reaching general availability; and
> long-distance next-edit-suggestions, whose companion VS Code engineering deep-dive reveals a
> two-model (location + edit) architecture trained via supervised fine-tuning and then
> Reinforcement Learning with Verified Rewards, validated by a 23% A/B-tested increase in code
> written via NES.

## Source Context

- **Type**: docs (GitHub official product changelog, ~350 words, published July 14, 2026,
  covering the June 2026 Visual Studio release). Four companion pages were followed as
  substantive linked sub-pages per MINER.md §1: the devblogs.microsoft.com Visual Studio blog
  post (`visual-studio-june-update-track-your-usage-trust-your-tools`, the primary
  feature-by-feature companion), the Microsoft Learn "Use MCP servers in Visual Studio"
  reference doc (linked from the devblogs post, providing exact trust-dialog button labels,
  version gating, and rug-pull-prevention rationale), the VS Code engineering blog's
  "Building Long-Distance Next Edit Suggestions" deep-dive (linked from the devblogs post as
  "the back story," covering the ML architecture and training pipeline), and the GitHub
  company-news post announcing Copilot's transition to usage-based billing (linked as
  background for the Copilot Usage window, but already fully covered by an existing corpus
  note — see Extraction Notes).
- **Author credibility**: GitHub and Microsoft engineering teams (changelog, devblogs post,
  and Learn docs) plus the VS Code engineering team (NES deep-dive, byline: Vikram Duvvur,
  Gaurav Mittal, Benjamin Simmonds) announcing production features and, for NES, publishing
  actual model-training methodology and A/B results. Authoritative for feature existence,
  exact UI/settings paths, and the stated A/B metric. Not a credible source for MCP
  trust-dialog effectiveness against real attacks, C++ modernization-agent success rates, or
  independent verification of the 23% NES metric (self-reported, no confidence interval or
  methodology beyond "A/B test").
- **Scope**: Six named Visual Studio features (Copilot Usage window, MCP trust validation,
  C++ modernization agent GA, long-distance NES, PR-to-Copilot-Chat integration, in-IDE PR
  review) plus color-emoji rendering (devblogs post only, omitted from the changelog's
  headline list). Does NOT cover: adoption or usage data for any feature; whether the MCP
  trust model or NES architecture applies identically in VS Code (NES: yes, per the deep-dive,
  which is a VS Code post; MCP trust: not stated for VS Code); the JSON schema for `.mcp.json`
  precedence when multiple discovery locations conflict; or any timeline for the "what's next"
  teased broader usage-visibility investment.

## Extracted Claims

### Claim 1: The refreshed Copilot Usage window shows real-time, token-based usage against GitHub's usage-based billing model, with proactive alerts as a user approaches, hits, and exceeds their limit

- **Evidence**: Both the changelog and the devblogs companion post describe the window and
  alert behavior consistently across independent fetches. The devblogs post additionally
  states usage is "calculated based on token consumption rather than by request."
- **Confidence**: settled (product fact, worded consistently across the official changelog
  and companion blog post)
- **Quote**: "The refreshed Copilot Usage window reflects GitHub Copilot's usage-based billing
  model with real-time updates. In addition, proactive alerts let you know when you're
  approaching your limit, when you've hit it, and when overages activate. Open it from
  Copilot badge menu > Copilot Usage and tune the warning threshold in settings to decide how
  early you get the notification."
  (github.blog changelog, raw HTML, retrieved 2026-07-16)
- **Our assessment**: This is the first documented *individual, IDE-native, real-time* usage
  visibility surface in the corpus. Prior sources (`docs-github-copilot-usage-metrics-ai-credits-per-user.md`)
  document `ai_credits_used` as an enterprise-admin-facing REST API field for per-user
  reporting, queried after the fact by organization admins. This Copilot Usage window is the
  complementary developer-facing surface: the individual practitioner sees their own
  consumption live, in the tool they're using, with a configurable early-warning threshold —
  not an admin pulling a report. For Ch01 (Daily Workflows): document checking the Copilot
  Usage window as a routine habit for practitioners on usage-based plans, parallel to the
  context-window ring icon habit already documented from the May 2026 VS update
  (`docs-github-copilot-vs-may-2026.md` Claim 7).

### Claim 2: Visual Studio validates MCP server trust in two distinct stages at startup — pre-startup configuration comparison against a trusted baseline, and post-startup fingerprint comparison of tools, prompts, resources, and instructions

- **Evidence**: The devblogs companion post is the only source that names both stages
  explicitly; the changelog and Microsoft Learn doc both confirm the mechanism exists but
  compress it to one sentence.
- **Confidence**: settled (mechanism described in detail in the official companion blog post;
  corroborated at a higher level by the changelog and Learn docs)
- **Quote**: "Visual Studio now validates MCP server trust in two places during startup.
  Before the server process starts, the current configuration is compared against a
  previously trusted baseline. After it starts, the fingerprint of its tools, prompts,
  resources, and instructions is compared to the last-trusted fingerprint. If anything has
  diverged, a trust dialog asks you to review the changes before the server is allowed to
  run."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-07-16)
- **Our assessment**: The two-stage design closes two distinct attack windows: a server whose
  *configuration* (transport type, URL, command, arguments — per the Learn doc) was altered
  before Visual Studio even launches it, and a server whose *runtime-reported capabilities*
  (its tool/prompt/resource/instruction set) differ from what was previously approved, even
  if the configuration file itself is unchanged. The second stage is the more novel one: an
  MCP server can serve a different tool manifest at runtime than what a static config-file
  diff would catch. For Ch02 (Harness Engineering — MCP Configuration) and Ch07 (Security):
  document this as the first corpus example of runtime-capability fingerprinting for MCP
  servers, distinct from static config validation.

### Claim 3: The MCP trust dialog offers three explicit actions — Accept (run this updated version now), Always Trust (stop future prompts for this server), and Reject/Do not trust (abort startup and ask again next time) — and the mechanism is explicitly designed to prevent "rug-pull" attacks where a server's tools change after initial approval

- **Evidence**: The Microsoft Learn "Use MCP servers in Visual Studio" reference doc gives the
  exact button labels and reprompt behavior. The same doc states that when the MCP protocol's
  `notifications/tools/list_changed` event fires, "Visual Studio resets any prior acceptances
  or permissions on tools (to prevent rug-pull attacks), refetches the tool list, and updates
  the count and UI live" — in the general tool-lifecycle section, not the trust-dialog section
  specifically, but describing the same underlying threat model.
- **Confidence**: settled (exact UI labels and behavior from first-party Microsoft Learn
  documentation, a companion source with more implementation precision than the changelog or
  blog post)
- **Quote**: "When the trust dialog appears, review the change and choose the action that
  matches your intent: Accept to run this updated version now. Always Trust to stop future
  trust prompts for this server. Reject to stop startup because you don't want to run the
  updated server. If you choose Reject, Visual Studio doesn't start the server and asks again
  the next time you try to activate it."
  (learn.microsoft.com "Use MCP servers in Visual Studio," raw HTML, retrieved 2026-07-16)
- **Quote (rug-pull rationale, separate passage, same doc)**: "When that event fires, Visual
  Studio resets any prior acceptances or permissions on tools (to prevent rug-pull attacks),
  refetches the tool list, and updates the count and UI live."
- **Our assessment**: "Rug-pull attack" is a named, specific MCP threat model — a server that
  behaves benignly during initial review, gets approved, and later redefines its tools to do
  something the user never consented to. No prior corpus source uses this term or documents a
  concrete platform mitigation for it. This is the single most guide-relevant claim in this
  source for Ch07 (Security): the rug-pull threat model gives practitioners and teams a
  specific, nameable failure mode to check any MCP client (not just Visual Studio) against —
  "does this client re-validate tool definitions on every reconnect, or does it trust a server
  forever after first approval?"

### Claim 4: First-time MCP server connections are implicitly trusted and silently seed the initial baseline; built-in servers, servers under an organizational `RegistryOnly` policy, and any server explicitly marked "Always Trust" skip the trust dialog entirely

- **Evidence**: Stated directly in the Microsoft Learn reference doc's "When you won't see
  the trust dialog" section, and corroborated by the devblogs post's shorter mention of the
  same exceptions.
- **Confidence**: settled (documented behavior in first-party Microsoft Learn docs)
- **Quote**: "Visual Studio skips the prompt when: The server is built in and shipped with the
  extension. Organization policy is set to RegistryOnly. You already selected Always Trust for
  that server. It's the first time the server is seen. Visual Studio saves an initial trust
  baseline automatically."
  (learn.microsoft.com "Use MCP servers in Visual Studio," raw HTML, retrieved 2026-07-16)
- **Our assessment**: The "first-time connection is implicitly trusted" behavior is a
  meaningful limitation practitioners should understand: trust-on-first-use (TOFU) means the
  fingerprinting protects against *drift* after approval, not against a malicious server being
  approved in the first place. A server that is malicious from the very first connection
  establishes that malicious state as the trusted baseline with no prompt at all. This is
  consistent with TOFU models generally (e.g., SSH host keys) but is worth flagging explicitly:
  the trust dialog is a change-detection control, not a vetting control. For Ch07: document
  this TOFU caveat alongside the rug-pull mitigation (Claim 3) — teams should pair MCP trust
  validation with a separate vetting step (e.g., `RegistryOnly` policy restricting servers to a
  pre-approved registry) if they want protection against first-contact malice, not just
  post-approval drift.

### Claim 5: Tool invocation approval is managed separately from server trust, via Confirm/Allow dropdown scopes that can auto-approve a specific tool for the current session, the current solution, or all future invocations

- **Evidence**: Microsoft Learn reference doc, "Management of tool approvals" section.
- **Confidence**: settled (documented UI mechanism in first-party Microsoft Learn docs)
- **Quote**: "When you invoke a tool, Copilot requests confirmation to run the tool. The
  reason is that tools might run locally on your machine and perform actions that modify
  files or data. After a tool invocation, on the chat pane, use the Confirm dropdown options.
  You can automatically confirm the specific tool for the current session, the current
  solution, or all future invocations."
  (learn.microsoft.com "Use MCP servers in Visual Studio," raw HTML, retrieved 2026-07-16)
- **Our assessment**: This is a second, distinct permission layer from the server-level trust
  dialog (Claims 2–4): trust validation governs *whether the server is allowed to run at all*;
  tool-invocation approval governs *whether a specific tool call is allowed to execute*, with
  three widening scopes of persistence (session → solution → all future). A practitioner could
  trust a server's integrity (no rug-pull) while still wanting per-invocation confirmation for
  a specific destructive tool (e.g., a file-delete tool) — the two layers are independently
  configurable. For Ch02: document both layers side by side as the complete MCP permission
  model for Visual Studio — server-trust (identity/integrity) and tool-approval (execution
  consent), each with their own settings surface and reset path (`Tools > Options > GitHub >
  Copilot > Copilot Chat` for trust; `All Settings > GitHub > Copilot > Tools` for approval
  resets).

### Claim 6: MCP server configuration in Visual Studio is discovered from up to five file-based locations, in a defined precedence order, including paths shared with other editors (`.vscode/mcp.json`, `.cursor/mcp.json`)

- **Evidence**: Microsoft Learn reference doc lists the five paths with descriptions in
  discovery order.
- **Confidence**: settled (documented file paths and discovery order in first-party docs)
- **Quote**: "Visual Studio also checks for MCP configurations that other development
  environments set up. It reads MCP server configurations from the following directories, in
  the following order: %USERPROFILE%\.mcp.json ... <SOLUTIONDIR>\.vs\mcp.json ...
  <SOLUTIONDIR>\.mcp.json ... <SOLUTIONDIR>\.vscode\mcp.json ... <SOLUTIONDIR>\.cursor\mcp.json"
  (learn.microsoft.com "Use MCP servers in Visual Studio," raw HTML, retrieved 2026-07-16)
- **Our assessment**: Visual Studio explicitly reading `.vscode/mcp.json` and `.cursor/mcp.json`
  means a repository's MCP server configuration, once defined for one editor, is
  automatically picked up by Visual Studio without duplication — a cross-editor configuration
  portability pattern. This parallels the multi-path skill discovery documented for VS Code/VS
  in `docs-github-copilot-vs-april-2026.md` (`.github/skills/`, `.claude/skills/`,
  `.agents/skills/`), extending the "one config file, many tools read it" pattern from skills
  to MCP server definitions. For Ch02: document the five-location discovery order (with
  `%USERPROFILE%\.mcp.json` as global/user-scope and the four `<SOLUTIONDIR>` variants as
  progressively narrower/editor-specific scope) as the current MCP configuration surface for
  Visual Studio, and note that teams standardizing on a single `.mcp.json` at the solution
  root get automatic Visual Studio + Cursor + VS Code compatibility without per-editor
  duplication.

### Claim 7: The GitHub Copilot modernization agent's MSVC/C++ upgrade scenarios have graduated from preview to general availability, offering an Automated mode for end-to-end execution and a Guided mode requiring review/approval of the assessment, plan, and each execution step

- **Evidence**: Stated consistently across the changelog and devblogs companion post, with the
  devblogs post adding that the agent "analyzes your project, identifies compatibility issues,
  and lays out an upgrade plan" before either mode begins.
- **Confidence**: settled (GA product fact, worded consistently across two official sources)
- **Quote**: "The first C++ scenarios for the GitHub Copilot modernization agent are now
  generally available. These are the flows that upgrade your C++ projects to the latest
  version of the Microsoft C++ (MSVC) Build Tools... The agent analyzes your project,
  identifies compatibility issues, and lays out an upgrade plan. Run it in Automated mode to
  let it carry out the upgrade end to end, or in Guided mode to review and approve the
  assessment, plan, and execution steps before each one runs. Right-click a solution or
  project in Solution Explorer and pick Modernize, or open Copilot Chat and type @Modernize
  followed by your upgrade request."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-07-16)
- **Our assessment**: This is the first corpus source documenting a GitHub Copilot
  "modernization agent" as a named, GA product surface with an explicit Automated-vs-Guided
  mode split. The mode split is structurally the same plan-then-approve-then-execute pattern
  already documented for the general-purpose Plan agent (`docs-github-copilot-vs-may-2026.md`
  Claims 1–4), but applied to a domain-specific migration task (MSVC toolset upgrades) with a
  narrower, more mechanically verifiable scope (compiler compatibility) than open-ended
  feature work. For Ch04 (Agentic Workflows — Domain-Specific Agents): document the
  modernization agent as a second instance of the plan-review-execute pattern, and note that
  Guided mode's per-step approval granularity (assessment → plan → each execution step) is
  finer-grained than the Plan agent's single approval gate (approve the whole plan, then hand
  off to Agent mode) — appropriate for a task where an intermediate step failure (e.g., a
  compiler flag change breaking a downstream build target) is more consequential and easier to
  isolate than in general feature implementation.

### Claim 8: Long-distance next edit suggestions extend Copilot's NES capability to predict and propose edits anywhere in the active file, not just near the cursor, and ship off by default

- **Evidence**: Consistently stated across the changelog, devblogs companion post, and the VS
  Code engineering deep-dive (which frames the feature's motivation: "until now they were
  limited to the area immediately around your cursor. That's often not where the related
  edits actually are.").
- **Confidence**: settled (product fact, worded consistently across three independent sources)
- **Quote**: "Copilot's next edit suggestions can now predict and propose follow-up edits
  anywhere in the active file, not just near your cursor. Turn it on under Tools > Options >
  Text Editor > Inline Suggestions by selecting Enable extended range suggestions."
  (github.blog changelog, raw HTML, retrieved 2026-07-16)
- **Quote (off-by-default, devblogs post)**: "The feature is off by default for now. Turn it
  on under Tools > Options > Text Editor > Inline Suggestions by checking Enable extended
  range suggestions."
- **Our assessment**: This is the Visual Studio-side rollout of a capability whose underlying
  engineering work (Claims 9–10 below) was done and published separately by the VS Code team,
  five months earlier (February 2026) — indicating GitHub ships a model/capability improvement
  to VS Code first, then rolls the same capability into Visual Studio as a later, off-by-default
  opt-in. For Ch02: document `github.copilot.nextEditSuggestions.extendedRange` (VS Code
  setting name, from the deep-dive) and "Enable extended range suggestions" (Visual Studio
  setting label) as the same underlying feature exposed with different settings surfaces per
  IDE, both currently opt-in.

### Claim 9: Long-distance NES uses a two-model architecture — a dedicated "location model" trained to predict only where the next edit should occur, followed by the original NES model generating the edit content at that predicted location — rather than modifying the existing single edit-generation model

- **Evidence**: VS Code engineering blog "Building Long-Distance Next Edit Suggestions"
  (February 26, 2026, by Vikram Duvvur, Gaurav Mittal, Benjamin Simmonds), linked from the
  devblogs companion post as "the back story" on long-distance NES.
- **Confidence**: settled (first-party engineering account of the architecture, with explicit
  rationale for the design choice)
- **Quote**: "Rather than modifying the existing edit-generation model, we decided to use a
  multi-model approach. We trained a dedicated location model whose sole responsibility is to
  predict where the next edit should happen. Once a valid location is selected, the original
  NES model then generates the edit suggestion. This separation has two benefits. First, each
  model can specialize on one task: one model learns spatial intent (where to jump), the other
  model produces high-quality edits within a local window. In addition, it enables us to
  iterate independently on location prediction without disrupting ongoing improvements to the
  core NES model."
  (code.visualstudio.com/blogs, "Building Long-Distance Next Edit Suggestions," raw HTML,
  retrieved 2026-07-16)
- **Our assessment**: This is the first corpus source to document the internal model
  architecture behind a shipped Copilot IDE feature at this level of technical specificity
  (a two-stage location→content pipeline, explicitly chosen over single-model retraining to
  allow independent iteration). Most prior VS/VS Code changelog sources describe *what* a
  feature does and its UI surface, not *how* the underlying model is structured. For Ch02
  (Harness Engineering) or a "Behind the Model" sidebar: this is a concrete, citable example of
  a two-stage location-then-content prediction pattern for editor-integrated suggestion
  features, worth cross-referencing if the guide ever discusses how vendors structure
  multi-step agentic predictions internally (decompose "where" from "what").

### Claim 10: The long-distance NES team validated the model with a structured evaluation framework measuring both "jump" and "no-jump" accuracy, then used A/B testing to find a 23% increase in code written via NES — alongside a higher rejection rate for far-away suggestions that required a subsequent reinforcement-learning stage (RLVR) to correct

- **Evidence**: The same VS Code engineering deep-dive describes the evaluation methodology,
  the initial dogfooding failure mode (model "too eager to jump"), the A/B test result, and the
  RLVR fix in sequence.
- **Confidence**: emerging (the 23% figure and RLVR fix are self-reported by the team that
  built the feature, with no external replication, confidence interval, or sample-size
  disclosure — but the qualitative narrative of failure-then-fix is unusually transparent for a
  vendor engineering post)
- **Quote (evaluation framework)**: "We designed a structured three-step evaluation process:
  Identify common multi-edit workflows[,] Construct representative cursor-jump examples[,]
  Measure both jump and no-jump accuracy... Crucially, we measured both jump and no-jump
  accuracy. While many examples required predicting a new location, a meaningful subset
  required staying on the current line. A model that jumps too often can be just as disruptive
  as one that misses important transitions."
- **Quote (A/B result and tradeoff)**: "To validate at scale, we ran A/B tests comparing
  long-distance NES against standard NES. The results were encouraging: a 23% increase in code
  written via NES, along with improvements across other engagement metrics. But the experiment
  also surfaced a tradeoff. Far-away suggestions were rejected more often than standard NES."
- **Quote (RLVR fix)**: "To address this, we introduced a reinforcement learning stage using
  Reinforcement Learning with Verified Rewards (RLVR). Instead of relying solely on supervised
  labels, we added a grading signal based on how closely the model's predicted jump location
  matched the eventual cursor movement... The result was a better balance between initiative
  and restraint. The updated model improved offline metrics and translated those gains into
  online performance, increasing code written via NES while reducing rejection rates."
  (code.visualstudio.com/blogs, "Building Long-Distance Next Edit Suggestions," raw HTML,
  retrieved 2026-07-16)
- **Our assessment**: The "jump too eagerly, causing higher rejection of far suggestions,
  fixed via an RLVR stage with a reward based on matching actual subsequent cursor movement"
  narrative is a specific, falsifiable engineering story, not marketing language — the team
  explicitly reports a shipped model's known weakness (over-eager jumping) and names the
  concrete fix. This is a rare level of methodological transparency in this corpus for an IDE
  vendor feature. For Ch04/Ch08 (if the guide has an evaluation-methodology chapter): cite this
  as a worked example of "measure the failure mode you expect (unwanted jumps), not just the
  success case," and of using RLVR with a behavioral proxy reward (does the model's prediction
  match what the user actually did next) when explicit human labels for "was this jump good"
  are expensive to collect at scale. Caveat per confidence rating: no external verification of
  the 23% figure exists, and "along with improvements across other engagement metrics" is
  vague — the guide should cite the number as vendor-reported, not as an independently
  verified benchmark.

### Claim 11: Practitioners can add a pull request to Copilot Chat by right-clicking it in the Git Repository window (or referencing it inline by typing `#` followed by the PR ID), gated behind a "View pull requests for a Git repository" Preview Feature flag, and a new in-IDE PR review experience allows browsing, commenting, approving, and completing PRs from GitHub or Azure DevOps without leaving Visual Studio

- **Evidence**: Stated in the github.blog changelog; the devblogs companion post does not
  mention either feature at all (confirmed by direct inspection of the companion post's raw
  HTML — see Extraction Notes), meaning the changelog is the sole source for these two
  features.
- **Confidence**: settled (product fact, from the official changelog); the Azure DevOps
  cross-platform scope is explicitly named but not elaborated
- **Quote**: "Right-click a pull request in the Git Repository window and select Add to
  Copilot Chat. Copilot will then pick up the pull request description, changed files, and
  comments as context. You can also reference a pull request inline by typing # followed by
  the pull request ID. This functionality requires View pull requests for a Git repository
  under Preview Features." / "The new in-IDE pull request review experience pairs naturally
  with Add to Copilot Chat. Browse, comment, approve, and complete pull requests from GitHub
  or Azure DevOps without leaving Visual Studio, then pull any pull request into Copilot Chat
  when you want help triaging or summarizing."
  (github.blog changelog, raw HTML, retrieved 2026-07-16)
- **Our assessment**: This is the first corpus source documenting PR review as a native,
  in-IDE Visual Studio surface (rather than a browser-based GitHub/Azure DevOps workflow), and
  the first to document `#`-style inline PR referencing in Copilot Chat specifically for
  Visual Studio (a different IDE and mechanism from the PR-context-attachment-via-right-click
  pattern documented for Git History/Blame in the May 2026 VS update,
  `docs-github-copilot-vs-may-2026.md` Claim 10 — that claim covers *commits*, this covers
  *pull requests* as a chat-context object, and adds inline `#PR-ID` referencing which the May
  note's commit-attachment mechanism did not have). The dual GitHub/Azure DevOps support
  parallels the Azure Repos code-review technical preview
  (`docs-github-copilot-code-review-azure-repos.md`), continuing a pattern of GitHub extending
  Copilot review/PR surfaces beyond github.com-hosted repositories. The Preview Features gate
  means this is not yet a default-on capability — teams evaluating it should expect it to be
  opt-in and potentially unstable. For Ch01 (Daily Workflows): document `#PR-ID` referencing
  and right-click "Add to Copilot Chat" as the new in-IDE path for PR-review-assisted chat,
  once the Preview Feature flag is enabled, alongside the existing commit-attachment workflow
  from the May 2026 update.

## Concrete Artifacts

### MCP Server Trust Model (Visual Studio 2026 v18.7+)

```
Source: github.blog changelog (2026-07-14) + devblogs.microsoft.com companion post
         + learn.microsoft.com "Use MCP servers in Visual Studio," all retrieved 2026-07-16

VERSION GATE: Visual Studio 2026 version 18.7 and later

STAGE 1 — Pre-startup (before the server process starts):
  Current server configuration compared against previously trusted baseline
  Triggers on changes to: transport type, URL, command, or arguments

STAGE 2 — Post-startup (after the server process starts):
  Fingerprint of tools, prompts, resources, resource templates, instructions
  compared against last-trusted fingerprint
  Triggers on changes to: server capabilities (tools/prompts/resources/instructions)

IF DIVERGENCE DETECTED → Trust dialog:
  Accept       — run this updated version now (updates the baseline)
  Always Trust — stop future trust prompts for this server
  Reject / Do not trust — abort startup; re-prompt next activation attempt

SKIP CONDITIONS (no dialog shown):
  - Server is built-in / shipped with the extension
  - Organization policy = RegistryOnly
  - User already selected "Always Trust" for this server
  - First-time connection (implicitly trusted; seeds initial baseline — TOFU)

SETTING: Tools > Options > GitHub > Copilot > Copilot Chat >
         "Show trust dialog before running tools from an updated MCP server"
         (on by default)

RUG-PULL MITIGATION (separate from trust dialog, same underlying threat model):
  On MCP protocol event `notifications/tools/list_changed`:
    Visual Studio resets all prior tool acceptances/permissions
    Refetches the tool list
    Updates count/UI live
  Explicit stated purpose: "to prevent rug-pull attacks"

TOOL-INVOCATION APPROVAL (separate permission layer from server trust):
  Confirm dropdown scopes: current session | current solution | all future invocations
  Allow dropdown: same three scopes
  Reset path: Tools > Options > All Settings > GitHub > Copilot > Tools

MCP CONFIG DISCOVERY ORDER (file-based, cross-editor-compatible):
  1. %USERPROFILE%\.mcp.json          — global, all VS solutions for this user
  2. <SOLUTIONDIR>\.vs\mcp.json       — VS-specific, this user + this solution
  3. <SOLUTIONDIR>\.mcp.json          — solution-scoped, source-controllable
  4. <SOLUTIONDIR>\.vscode\mcp.json   — solution-scoped, typically not source-controlled
  5. <SOLUTIONDIR>\.cursor\mcp.json   — solution-scoped, typically not source-controlled
```

### C++ Modernization Agent (GA, Visual Studio, June 2026)

```
Source: github.blog changelog + devblogs.microsoft.com companion post,
        both retrieved 2026-07-16

Scope: MSVC (Microsoft C++ Build Tools) upgrade scenarios — first C++ scenarios
       for the modernization agent to reach GA (graduated from preview)

Flow:
  1. Agent analyzes project
  2. Agent identifies compatibility/compile-blocker issues
  3. Agent lays out an upgrade plan (assessment document)
  4a. Automated mode → executes upgrade end-to-end, no per-step gate
  4b. Guided mode → review/approve assessment, plan, AND each execution step individually

Invocation:
  - Right-click solution/project in Solution Explorer → "Modernize"
  - Copilot Chat: "@Modernize" + upgrade request text
```

### Long-Distance Next Edit Suggestions — Architecture and Validation (VS Code engineering, Feb 2026; rolled into Visual Studio, June 2026)

```
Source: code.visualstudio.com/blogs, "Building Long-Distance Next Edit Suggestions"
        (Feb 26, 2026, Vikram Duvvur / Gaurav Mittal / Benjamin Simmonds),
        retrieved 2026-07-16; Visual Studio rollout per github.blog changelog
        + devblogs.microsoft.com, retrieved 2026-07-16

ARCHITECTURE:
  Model 1 ("location model") — predicts WHERE the next edit should occur
  Model 2 (original NES model) — generates the edit content at that location
  Design rationale: specialization + independent iteration (vs. retraining
  one combined model)

TRAINING:
  Base: same trajectory dataset used for the core NES model (developer cursor
        movement + edit history)
  Method: Supervised Fine-Tuning (SFT), grid search around known-good NES
          hyperparameters (Bayesian Optimization tried, did not outperform)
  Refinement stage: Reinforcement Learning with Verified Rewards (RLVR) —
        reward = how closely predicted jump location matches actual
        subsequent cursor movement

EVALUATION:
  Three-step framework: (1) identify common multi-edit workflows (rename,
  signature change, doc update) (2) construct cursor-jump examples from them
  (3) measure BOTH jump accuracy and no-jump accuracy (staying put when
  correct is also scored)

VALIDATION TIMELINE:
  Dogfooding → found model "too eager to jump" (root cause: training-set
    imbalance, too few no-jump examples)
  → dataset rebalanced, both jump/no-jump accuracy improved
  → A/B test vs. standard NES: +23% code written via NES; but far-away
    suggestions rejected more often than standard NES
  → RLVR stage added to add "restraint" → reduced rejection rate while
    preserving the code-written gain
  → shipped the following month

VISUAL STUDIO ROLLOUT (June 2026):
  Off by default
  Setting: Tools > Options > Text Editor > Inline Suggestions >
           "Enable extended range suggestions"
  (VS Code equivalent setting: github.copilot.nextEditSuggestions.extendedRange)

FUTURE WORK (stated, not yet shipped): cross-file suggestions; unified
  location+content model
```

### Pull Request Integration and Color Emoji (Visual Studio, June 2026, changelog-only unless noted)

```
Source: github.blog changelog (2026-07-14), retrieved 2026-07-16
        [Color emoji section: also in devblogs.microsoft.com companion post]

Add to Copilot Chat:
  Right-click PR in Git Repository window → "Add to Copilot Chat"
  → picks up PR description, changed files, comments as context
  Inline reference: type "#" + PR ID
  Gate: requires "View pull requests for a Git repository" (Preview Features)

In-IDE PR review:
  Browse, comment, approve, complete PRs
  Sources: GitHub OR Azure DevOps
  No need to leave Visual Studio

Color emoji rendering:
  Full-color emoji now render in: editor, markdown previews, Copilot Chat,
  build output, Solution Explorer
  Uses "modern font technologies" — consistent rendering regardless of
  Windows version
  NOT in the changelog's own "Highlights" list; documented only in the
  devblogs companion post

Availability (all features in this note): Copilot Free, Student, Pro, Pro+,
  Max, Business, Enterprise
```

## Cross-References

- **Extends**:
  - `docs-github-copilot-vs-may-2026.md` (Claim 7, context-window ring icon): The Copilot
    Usage window (Claim 1) is a second instance of the same "make a normally-invisible resource
    budget visible in real time, in the IDE" pattern — context tokens in May, billing tokens in
    June. For Ch01: group both as "budget visibility habits" practitioners should form.
  - `docs-github-copilot-usage-metrics-ai-credits-per-user.md` (whole note): That source
    documents `ai_credits_used` as an admin-facing, per-user REST API field, queried
    after-the-fact at the org/enterprise level. This note's Copilot Usage window (Claim 1) is
    the individual-developer-facing, real-time complement to that same underlying
    usage-based-billing system — same billing model, opposite audience and latency.
  - `docs-github-copilot-vs-may-2026.md` (Claims 1–4, Plan agent plan-review-execute pattern):
    The C++ modernization agent's Automated/Guided split (Claim 7) is a second, domain-specific
    instance of the plan-then-approve-then-execute workflow shape, with finer-grained per-step
    approval in Guided mode than the Plan agent's single plan-approval gate.
  - `docs-github-copilot-vs-may-2026.md` (Claim 10, commit-history context attachment): Claim
    11 (PR-to-Copilot-Chat) extends the same "attach a Git object as chat context via
    right-click" gesture from commits (May) to pull requests (June), and adds a new `#PR-ID`
    inline-reference mechanism the May commit-attachment feature does not have.
  - `docs-github-copilot-vs-april-2026.md` (Claim 1, multi-path skill discovery): The MCP
    config discovery order (Claim 6) extends the "one shared config file read by multiple
    tools/editors" pattern from skills directories to MCP server definitions, explicitly
    including `.vscode/mcp.json` and `.cursor/mcp.json` paths.
  - `docs-github-copilot-code-review-azure-repos.md`: That note documents Azure Repos code
    review reaching technical preview in June 2026. This note's in-IDE PR review (Claim 11)
    explicitly supporting "GitHub or Azure DevOps" continues the same platform-expansion
    pattern — Copilot surfaces increasingly treat Azure DevOps-hosted repositories as
    first-class, not GitHub-exclusive.

- **Corroborates**:
  - `docs-github-copilot-security-validation-third-party-agents.md` and
    `blog-anthropic-zero-trust-ai-agents.md`: both document platform/vendor-level automated
    security controls (CodeQL/secret-scanning parity, Zero Trust Foundation-tier controls) as
    a "the platform provides this by default" pattern. MCP server trust validation (Claims
    2–4) is a further instance of the same pattern, specific to the MCP supply chain rather
    than agent-generated code.

- **Contradicts**: None identified. No existing corpus source claims MCP servers in any
  GitHub Copilot surface were previously trust-validated at startup, or that Visual Studio
  lacked in-IDE PR review before this release. The rug-pull terminology and TOFU caveat
  (Claims 3–4) refine the corpus's understanding of MCP security controls without opposing any
  existing claim. No contradiction issue filed.

- **Novel**:
  - **"Rug-pull attack" as a named MCP threat model with a documented platform mitigation**
    (Claim 3): first appearance of this specific term and threat model in the corpus.
  - **Two-stage (config + runtime-fingerprint) MCP trust validation** (Claim 2): first
    corpus documentation of fingerprinting a server's *runtime-reported* tool/prompt/resource
    manifest, distinct from static config-file validation.
  - **TOFU limitation explicitly surfaced for an MCP trust system** (Claim 4): first corpus
    source to note that first-contact trust is implicit and unvetted — the mitigation covers
    drift-after-approval, not initial vetting.
  - **Published two-model (location + content) architecture with SFT→RLVR training pipeline
    and a self-reported A/B result for a shipped Copilot IDE feature** (Claims 9–10): the
    corpus's first example of this level of ML-engineering transparency for a Copilot feature;
    prior VS/VS Code changelog notes describe feature behavior, not model architecture or
    training methodology.
  - **In-IDE, cross-platform (GitHub + Azure DevOps) pull request review inside Visual
    Studio** (Claim 11): first corpus documentation of full PR review (not just code review
    comments) as a native non-browser IDE surface.
  - **Individual/IDE-native real-time usage-billing visibility** (Claim 1): first
    developer-facing (as opposed to admin-facing API) usage-billing surface in the corpus.

## Guide Impact

- **Chapter 07 (Security) / Chapter 02 (Harness Engineering — MCP Configuration)**:
  - Add the "rug-pull attack" threat model (Claim 3) as a named risk practitioners should
    check any MCP client against, not just Visual Studio: does the client re-validate a
    server's tool/prompt/resource manifest on every reconnect, or trust it indefinitely after
    first approval? Cite Visual Studio's `notifications/tools/list_changed`-triggered
    permission reset as a concrete example of a client that does the former.
  - Document the TOFU caveat (Claim 4) explicitly: MCP trust-on-first-use protects against
    drift, not initial vetting. Recommend pairing trust validation with an allowlist/registry
    policy (`RegistryOnly`) for teams that need protection against malicious servers from
    first contact, not just malicious changes to previously-approved servers.
  - Add the two-layer permission model (server trust vs. tool-invocation approval, Claims 2–5)
    as the reference MCP permission architecture, and the five-location config discovery order
    (Claim 6) — including cross-editor paths (`.vscode/mcp.json`, `.cursor/mcp.json`) — as the
    current state of MCP configuration portability across IDEs.

- **Chapter 01 (Daily Workflows)**:
  - Add the Copilot Usage window (Claim 1) alongside the existing context-window ring icon
    (May 2026 update) as a "budget visibility" habit: check both regularly on usage-based
    plans, not just at billing-cycle end.
  - Add right-click "Add to Copilot Chat" for pull requests and inline `#PR-ID` referencing
    (Claim 11) as the new in-IDE path for PR-review-assisted chat, gated behind the "View pull
    requests for a Git repository" Preview Feature — note this is not yet default-on.

- **Chapter 04 (Agentic Workflows — Domain-Specific Agents)**:
  - Add the C++ modernization agent's Automated/Guided mode split (Claim 7) as a second
    instance of the plan-review-execute workflow shape from the May 2026 Plan agent, with
    finer per-step approval granularity appropriate to a more mechanically-verifiable task
    (compiler/toolset migration) than open-ended feature work.

- **Chapter 02 or an "Evaluation Methodology" sidebar**:
  - Cite the long-distance NES validation story (Claims 9–10) as a worked example of (a)
    explicitly measuring the failure mode you expect, not just the success case (jump AND
    no-jump accuracy), and (b) using RLVR with a behavioral proxy reward (does the prediction
    match the user's actual subsequent action) when direct human labels for suggestion quality
    are expensive to collect at scale. Flag the 23% figure as vendor-self-reported with no
    disclosed methodology or confidence interval.

## Extraction Notes

1. **Five sources fetched, within MINER.md's "up to 5 linked pages" guidance**: (1) the
   primary github.blog changelog, (2) the devblogs.microsoft.com companion Visual Studio blog
   post (linked from the changelog), (3) the Microsoft Learn "Use MCP servers in Visual
   Studio" reference doc (linked from the devblogs post), (4) the VS Code engineering blog's
   NES architecture deep-dive (linked from the devblogs post as "the back story"), and (5) the
   GitHub company-news post announcing the usage-based-billing transition (linked from the
   devblogs post as background). Source (5) was read but not deeply extracted — its content
   is already fully covered by the existing corpus note
   `docs-github-copilot-usage-metrics-ai-credits-per-user.md` and an earlier billing
   announcement; it is cited only as background context for Claim 1.

2. **Raw HTML fetched via `curl`, not WebFetch's AI-summarized output**: Following the
   precedent set in `docs-github-copilot-vscode-june-2026.md` (Extraction Notes §1–2), an
   initial WebFetch call to the primary changelog returned two internally-inconsistent
   paraphrases across two separate prompts (e.g., "Key Features" vs. "Key Highlights" as a
   section title, and differing exact wording for the same sentences). To avoid citing
   paraphrased text as a direct quote (MINER.md §2a), all five pages were re-fetched via
   `curl` with a browser user-agent, and body text was extracted from the raw HTML with a
   Python script (strip `<script>`/`<style>`, convert block-level closing tags to newlines,
   strip remaining tags, unescape entities). All quotes in this note are taken from that
   raw-HTML-derived plain text, not from any WebFetch summary.

3. **Companion post confirmed NOT to cover pull request features**: An initial WebFetch pass
   over the devblogs companion post asserted "the article does not contain information about
   pull request integration, in-IDE pull request review experience, or PR referencing." This
   was independently confirmed by inspecting the raw-HTML-derived text (`/tmp/vs-june-devblog-clean.txt`
   at extraction time) section by section — the companion post covers Copilot usage tracking,
   MCP trust validation, C++ modernization, long-distance NES, and color emoji only. Claim 11
   (pull request features) is sourced exclusively from the github.blog changelog; no companion
   corroboration exists for it.

4. **NES deep-dive is a VS Code post, not a Visual Studio post**: `code.visualstudio.com/blogs`
   is the VS Code product blog. The architecture, training, and A/B-test content in Claims
   9–10 describes work done for VS Code's NES feature (published February 26, 2026); the June
   2026 Visual Studio changelog documents Visual Studio *receiving* the same long-distance NES
   capability roughly five months later, off by default. This note treats the deep-dive's
   technical claims as applicable to the underlying model/capability (which Visual Studio now
   also uses), not as Visual-Studio-specific product documentation — flagged explicitly in
   Claim 8's assessment.

5. **No contradictions identified**: Cross-referenced against all existing VS/VS Code Copilot
   notes, the MCP-related docs/discussion notes, the security-validation and Zero Trust notes,
   and the Azure Repos code-review note. No claim in this source opposes an existing corpus
   position. The "rug-pull attack" and TOFU-limitation claims (3–4) refine rather than
   contradict the corpus's existing (sparse) MCP-security coverage. No contradiction issue
   filed.

6. **Two Prospector triage comments, both used**: The issue carries two triage comments from
   the same day (2026-07-16), the second rated "high" novelty and more specific than the
   first ("medium," listing only Ch02–Ch04). This extraction follows the second, more detailed
   comment's guidance (usage tracking, MCP trust/fingerprinting, C++ GA, long-distance NES) and
   additionally surfaces the PR-integration and color-emoji features neither comment
   mentioned, since MINER.md's extraction process calls for reading the entire source, not
   only the features a triage comment flagged in advance.
