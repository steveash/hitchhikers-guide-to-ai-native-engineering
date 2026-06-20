---
source_url: https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements
source_type: docs
title: "Copilot code review: AGENTS.md support and UI improvements"
author: GitHub (official changelog)
date_published: 2026-06-18
date_extracted: 2026-06-20
last_checked: 2026-06-20
status: current
confidence_overall: settled
issue: "#1236"
---

# Copilot Code Review: AGENTS.md Support and UI Improvements

> GitHub's June 18, 2026 changelog announcing that Copilot code review now reads
> repository-root AGENTS.md files automatically — adding a cross-agent standard
> configuration surface to the code review customization stack — plus two UI
> improvements that reduce friction for draft PR reviews and declutter the
> conversation timeline.

## Source Context

- **Type**: docs (GitHub official product changelog, June 18, 2026; short feature
  announcement covering one primary feature and two secondary UI changes)
- **Author credibility**: GitHub engineering team announcing a production generally-available
  feature. Authoritative for the existence of the feature, that AGENTS.md is read
  automatically, and the availability status. Not authoritative for: how AGENTS.md content
  interacts with SKILL.md skills or MCP context when both are present during the same review;
  how much AGENTS.md content is incorporated vs. truncated for large files; or whether the
  "generally available" status applies equally to all Copilot plan tiers.
- **Scope**: AGENTS.md support for code review (feature announcement with no configuration
  steps), two UI changes (draft PR request button placement, timeline event collapsing). Does
  NOT cover: how AGENTS.md interacts with or takes precedence over `.github/copilot-instructions.md`,
  SKILL.md files, or MCP server context already documented in the June 2 and June 12 changelogs;
  how to structure AGENTS.md content specifically for code review feedback quality; or whether
  AGENTS.md is read in full or partially.

## Extracted Claims

### Claim 1: Repository-root AGENTS.md files can now be used to shape Copilot code review feedback

- **Evidence**: Official GitHub product changelog announcing the feature as generally available.
- **Confidence**: settled (product fact — stated in official changelog as GA)
- **Quote**: "You can now add an `AGENTS.md` file at the root of your repository to help shape
  Copilot code review feedback."
- **Our assessment**: This introduces AGENTS.md as a code review configuration surface, alongside
  the existing surfaces documented in the June 2 and June 12 changelogs (SKILL.md, MCP servers,
  `.github/copilot-instructions.md`, content exclusions, runner configuration, review tier). Unlike
  SKILL.md — which defines agentic tool invocations — AGENTS.md is a repository-level context file
  encoding project conventions, environment setup, and patterns for AI agents generally. The
  June 2 source note (`docs-github-copilot-code-review-skills-mcp-tier.md`) explicitly flagged
  "how agent skills differ from AGENTS.md or CLAUDE.md for code review purposes" as out of scope.
  This June 18 changelog directly addresses that gap. For Ch02 (Harness Engineering): AGENTS.md is
  now the eighth configuration surface for Copilot code review (adding to the seven-layer surface
  documented in Claim 6 of `docs-github-copilot-code-review-config-controls.md`).

### Claim 2: Copilot code review reads AGENTS.md automatically as part of its review workflow — no manual configuration or invocation required

- **Evidence**: Official GitHub product changelog stating automatic utilization.
- **Confidence**: settled (product behavior stated in official changelog)
- **Quote**: "Copilot code review will now utilize that context automatically as part of its
  workflow."
- **Our assessment**: The "automatically" framing is significant: AGENTS.md is not a skill the
  practitioner must invoke or a setting the admin must enable — it is read implicitly whenever a
  review runs and the file exists at the repository root. This is consistent with how Claude Code
  reads CLAUDE.md files (automatically at session start, per
  `blog-anthropic-steering-claude-code-mechanisms.md` Claim 2). The automatic behavior means
  teams that already have an AGENTS.md in their repository get code review customization with no
  additional configuration step. For Ch05 (Team Adoption): AGENTS.md is a zero-friction activation
  path for teams that already author this file for Claude Code or other AI agents — their existing
  file begins shaping Copilot code reviews immediately.

### Claim 3: AGENTS.md support and the UI improvements are generally available — not in preview

- **Evidence**: Official GitHub product changelog describing availability status.
- **Confidence**: settled (availability status stated in official changelog)
- **Quote**: (no direct quote; both WebFetch attempts confirmed 'generally available' status but
  verbatim text of the availability section was not recoverable — see Extraction Notes)
- **Our assessment**: Both prior June changelogs (June 2 and June 12) launched their features in
  "public preview" status. The June 18 GA status means no feature flags, no opt-in requirements,
  and no preview-tier restrictions. For Ch05: teams evaluating these features no longer need to
  account for preview-related limitations (stability, support, documentation gaps) when planning
  adoption. GA status also implies that these features are part of the product's supported surface
  and will be maintained forward-compatibly.

### Claim 4: The "Request" button now appears next to Copilot on draft pull requests, eliminating the need to search for it when requesting a review before a PR is published

- **Evidence**: Official changelog describing the UI placement change for draft PR review requests.
- **Confidence**: settled (UI behavior stated in official changelog)
- **Quote**: "The **Request** button shows up next to Copilot on draft pull requests"
- **Our assessment**: Prior to this change, requesting a Copilot code review on a draft PR
  apparently required extra navigation steps. The new placement reduces friction at an important
  moment in the review workflow: teams that want AI feedback during active development (before
  marking a PR ready for review) can now request it without leaving the PR conversation UI. For
  Ch05 (Team Adoption): the placement change makes draft-PR-as-feedback-loop more visible and
  accessible, which may increase review adoption earlier in the development cycle when feedback
  is most actionable.

### Claim 5: Copilot code review events on the pull request conversation tab are now collapsed together to reduce timeline clutter

- **Evidence**: Official changelog describing the timeline collapsing behavior.
- **Confidence**: settled (UI behavior stated in official changelog)
- **Quote**: "collapsed together to help declutter your conversation tab, allowing you to find
  what matters, quickly."
- **Our assessment**: As Copilot code review is used more actively — especially in repositories
  with the June 2 Medium tier enabled (which triggers richer, more iterative reviews) — the
  number of Copilot events on the conversation tab grows. Collapsing them addresses a signal-to-
  noise problem where Copilot review events visually compete with human reviewer comments and PR
  discussion. This pairs with the severity label and comment grouping from
  `docs-github-copilot-code-review-comment-ux.md` (May 12, 2026): that note reduced comment-level
  noise; this note reduces event-level noise on the timeline. For Ch01 (Daily Workflows): the
  conversation tab now presents Copilot events as a collapsed group, so practitioners can choose
  to expand them rather than scroll past them linearly.

## Concrete Artifacts

### Source Changelog Summary (June 18, 2026)

```
Title: Copilot code review: AGENTS.md support and UI improvements
Published: 2026-06-18
Source: https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements
Status: Generally Available

--- FEATURE: AGENTS.md Support ---

"You can now add an `AGENTS.md` file at the root of your repository to help
shape Copilot code review feedback."
"Copilot code review will now utilize that context automatically as part of
its workflow."

--- UI IMPROVEMENT 1: Draft PR Review Request ---

"The **Request** button shows up next to Copilot on draft pull requests"
[Eliminates need to search for the button when requesting review before publishing]

--- UI IMPROVEMENT 2: Timeline Decluttering ---

"collapsed together to help declutter your conversation tab, allowing you
to find what matters, quickly."
[Copilot code review events now collapse on the conversation tab]

Availability: Generally available
```

### Updated Code Review Configuration Surface (as of June 18, 2026)

```
# Complete configuration surface for Copilot code review
# Compiled from June 2 + June 12 + June 18 2026 changelogs

AGENT CONTEXT (what the agent reads during review):
  AGENTS.md                             → cross-agent project conventions (June 18 — NEW)
  .github/skills/code-review/SKILL.md   → agent skill context (June 2)
  MCP servers (repo settings → Copilot → MCP servers) → external context (June 2)
  .github/copilot-instructions.md       → general instructions (now unlimited — June 12)
  *.instructions.md                     → additional instructions (now unlimited — June 12)

CONTENT GOVERNANCE (what the agent can access):
  Content exclusion settings            → repo / org / enterprise levels (June 12)

COMPUTE CONFIGURATION (where the agent runs):
  Org-level runner default              → org settings → Copilot → Runner type (June 12)
  Runner lock                           → org setting overrides repo-level config (June 12)
  Per-repo Actions workflow             → configurable compute environment (June 2)

ANALYSIS DEPTH (how thoroughly the agent reviews):
  Review tier (Low / Medium)            → repo settings → Copilot → Code review (June 2)

TOTAL LAYERS AS OF JUNE 18, 2026: 8 agent-context items, plus 6 governance/compute/depth items
```

### Copilot Code Review Feature Evolution Arc (updated to June 18, 2026)

```
Date        Source Note                                          What Changed
----------  ---------------------------------------------------  ------------------------------------
2026-04-08  docs-github-copilot-pr-review-metrics               Measurement: code review API fields
2026-04-27  docs-github-copilot-code-review-actions-billing     Billing: AI Credits + Actions mins
2026-05-12  docs-github-copilot-code-review-comment-ux          UX: severity labels + grouping
2026-05-19  docs-github-copilot-cca-apply-review-feedback       Action: Fix with Copilot dialog
2026-06-02  docs-github-copilot-code-review-skills-mcp-tier     Customization: skills + MCP + tier
2026-06-12  docs-github-copilot-code-review-config-controls     Governance: org runner defaults +
                                                                 content exclusion + unlimited
                                                                 instruction files
2026-06-18  THIS NOTE (code-review-agents-md-ui)                Cross-agent: AGENTS.md support GA;
                                                                 draft PR button; timeline collapse
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  - That source's Scope section explicitly stated: "Does NOT cover: how agent skills differ from
    AGENTS.md or CLAUDE.md for code review purposes." This June 18 source directly fills that gap —
    AGENTS.md is now a documented code review configuration surface. The distinction: SKILL.md
    (Claim 12 of that note) defines agentic tool invocations that Copilot calls during review;
    AGENTS.md defines project-level conventions and context that the model reads as background
    knowledge. Both are configuration surfaces for the review agent, but AGENTS.md is cross-tool
    (read by Claude Code, other AI agents, and now Copilot code review), while SKILL.md is a
    GitHub-specific mechanism. For Ch02: document both in the configuration surface matrix with
    clear role distinction.
  - That source's Claim 5 noted "Shared configuration across review and cloud agent means platform
    teams invest once and get consistent behavior across both agents." This June 18 AGENTS.md
    announcement extends the shared-configuration principle: AGENTS.md written for Claude Code or
    other AI agents now also shapes Copilot code review, extending the cross-agent investment
    payoff further.

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue #1168):
  - That source's Claim 6 described "a seven-layer configuration surface for Copilot code review"
    as of June 12, 2026. AGENTS.md support (this note's Claim 1) adds an eighth layer to the
    agent-context category. The concrete artifact "Updated Code Review Configuration Surface" above
    revises that seven-layer surface to eight by adding AGENTS.md at the top of the agent-context
    section.
  - That source's Claim 5 distinguishes `.github/copilot-instructions.md` and `*.instructions.md`
    from SKILL.md: instruction files provide general guidelines; SKILL.md defines agentic skill
    invocations. AGENTS.md now adds a third type in the agent-context category: project-level
    AI-agent conventions. Platform teams need to understand all three and their different roles
    to avoid redundancy (encoding the same information in multiple files wastes context budget).

- **Extends** `docs-github-copilot-code-review-comment-ux.md` (issue #723):
  - That source (May 12) documented comment-level noise reduction via severity labels and comment
    grouping. This source's timeline event collapsing (Claim 5) adds a complementary event-level
    noise reduction: Copilot review events on the conversation tab are now collapsed. The two form
    a coherent noise-reduction pair: May 12 reduced noise within Copilot's comment surface; June 18
    reduces noise at the timeline level where Copilot events appear alongside human reviewer activity.

- **Corroborates** `paper-gloaguen-agentsmd-effectiveness.md` (issue N/A):
  - That ETH Zurich paper (Claim 2) found developer-written AGENTS.md files improve AI coding
    agent success rates by ~4% on average. The fact that Copilot code review now reads AGENTS.md
    makes that finding directly applicable to code review configuration quality: a well-authored
    AGENTS.md may improve the relevance and accuracy of code review feedback, while a poorly-
    authored or LLM-generated AGENTS.md may degrade it (Claim 1 of that paper: LLM-generated
    context files reduce task success rates). That paper's Claim 4 (agents follow AGENTS.md
    instructions with high compliance, including tool-specific directives) supports our confidence
    that AGENTS.md content will materially shape Copilot code review output.
  - For Ch02: teams authoring AGENTS.md for code review customization should write it manually
    (not auto-generate with `/init`), per the paper's findings. The same quality bar applies here
    as for AGENTS.md written for coding agents.

- **Corroborates** `blog-anthropic-steering-claude-code-mechanisms.md` (issue #1222):
  - That Anthropic blog (Claim 2) documented that CLAUDE.md files "load into context at session
    start and stay there for the entire session" and are "memoized" through compaction. The
    analogous behavior for AGENTS.md in Copilot code review (read automatically per Claim 2 of
    this note) appears to follow a similar automatic-load pattern. However: Anthropic's taxonomy
    covers Claude Code only, not Copilot. The extent to which AGENTS.md in Copilot behaves like
    CLAUDE.md in Claude Code (full file, partial, memoized, etc.) is not stated in this source.
  - The Anthropic post's taxonomy of seven instruction mechanisms for Claude Code does not include
    AGENTS.md — AGENTS.md is a cross-tool community standard rather than a first-party Anthropic
    mechanism. That distinction matters for Ch04: AGENTS.md is an ecosystem convention that
    multiple vendors now support (Copilot, others), while CLAUDE.md is Anthropic-specific.

- **Contradicts**: None found. No existing corpus source makes claims that conflict with AGENTS.md
  support for Copilot code review. The June 2 source explicitly noted AGENTS.md as out of scope
  (not addressed, not denied). No contradiction issue to file.

- **Novel**:
  - **AGENTS.md as a Copilot code review configuration surface**: No prior corpus source documents
    AGENTS.md being read by Copilot code review. Prior code review sources cover SKILL.md, MCP,
    copilot-instructions.md, and content exclusions — AGENTS.md was absent from all.
  - **Cross-agent portability of AGENTS.md**: This is the first corpus source to document that a
    single AGENTS.md file can shape both Claude Code (per `blog-anthropic-steering-claude-code-mechanisms`
    context on CLAUDE.md and ecosystem standards) and Copilot code review. The cross-tool
    portability creates an investment multiplier: one well-authored AGENTS.md shapes multiple AI
    agents' behavior.
  - **GA (not preview) status for these features**: Prior June 2026 code review features launched
    as public preview. This is the first set of code review features announced as generally available
    in June 2026, implying production-ready stability.
  - **Timeline event collapsing**: No prior corpus source documents Copilot review events being
    collapsed on the conversation tab. The May 12 note covered comment-level UX; this is event-level.

## Guide Impact

### Chapter 02: Harness Engineering

- **Update the complete code review configuration surface**: As of June 18, 2026, the surface
  now has eight agent-context entries. Add AGENTS.md at the top of the agent-context section
  (it loads automatically at the root level, making it the baseline context; SKILL.md and MCP
  layers add on top of it). Reference the "Updated Code Review Configuration Surface" artifact
  in this note to replace the seven-layer table in `docs-github-copilot-code-review-config-controls.md`
  Claim 6.
- **Distinguish the three agent-context file types**: AGENTS.md (project conventions, cross-agent),
  `.github/copilot-instructions.md` (Copilot-specific review guidelines, unlimited since June 12),
  and SKILL.md (agentic tool invocations). All three are now code review configuration surfaces,
  but they serve different purposes and load via different mechanisms. The guide should explain
  when to use each and warn against encoding the same information in multiple files (context
  budget waste).
- **AGENTS.md quality guidance**: Cross-reference `paper-gloaguen-agentsmd-effectiveness.md`
  Claim 2 for the finding that developer-written AGENTS.md files outperform auto-generated ones.
  The same principle applies to AGENTS.md written for code review: write it by hand, focused on
  repository-specific conventions that the model cannot discover from the diff alone.

### Chapter 04: Agents

- **AGENTS.md as a cross-agent standard configuration mechanism**: Add AGENTS.md to the discussion
  of how teams shape AI agent behavior. The June 18 changelog demonstrates the investment multiplier:
  a well-authored AGENTS.md shapes Claude Code (reads CLAUDE.md and AGENTS.md natively), Copilot
  code review (reads AGENTS.md automatically per this source), and potentially other AI agents that
  respect the standard. This is the first corpus-documented case of a single file shaping both a
  code generation agent and a code review agent.
- **Auto-read context files vs. explicitly configured skills**: The code review agent layer now
  includes both auto-read files (AGENTS.md, copilot-instructions.md) and explicitly configured
  capabilities (SKILL.md, MCP servers). For agentic architecture discussion: distinguish passive
  context injection (auto-read files) from active context injection (skill invocations, MCP calls).
  AGENTS.md is passive — it shapes the agent's baseline knowledge; SKILL.md is active — it enables
  the agent to call tools during the review pass.

### Chapter 05: Team Adoption

- **AGENTS.md as a zero-friction Copilot code review activation path**: Teams that have already
  authored an AGENTS.md for Claude Code or other AI agents get Copilot code review customization
  with no additional configuration. This lowers the adoption bar significantly for teams in
  mixed-tool environments. The guide should highlight this as the recommended first customization
  step: "If your team already maintains AGENTS.md, your code review is already partially
  customized."
- **Draft PR review friction reduction**: The Request button placement (Claim 4) enables teams
  to establish earlier-cycle AI review as a workflow pattern. Recommend: request Copilot review
  when opening a draft PR, not just when marking it ready. Earlier AI feedback → fewer late-stage
  rework cycles.
- **Updated code review deployment checklist (as of June 18, 2026)**: Seven deployment layers:
  (1) Billing model — `docs-github-copilot-code-review-actions-billing.md`
  (2) Triage UX — `docs-github-copilot-code-review-comment-ux.md`
  (3) Suggestion application — `docs-github-copilot-cca-apply-review-feedback.md`
  (4) Org context injection (skills + MCP) — `docs-github-copilot-code-review-skills-mcp-tier.md`
  (5) Analysis depth (Low/Medium tier) — same note
  (6) Governance controls — `docs-github-copilot-code-review-config-controls.md`
  (7) Cross-agent AGENTS.md + UI improvements — this source
  Teams that evaluated before June 18, 2026 are missing AGENTS.md as a configuration surface and
  may have unintentional customization from an existing AGENTS.md that was not authored with code
  review in mind.

### Chapter 01: Daily Workflows

- **Existing AGENTS.md content now shapes Copilot code review**: Practitioners whose repositories
  already have AGENTS.md should review the file's content and consider whether it encodes
  conventions they want Copilot to apply during code review. Content written for coding agent
  workflows (e.g., "always use pytest fixtures" or "check for async safety in all database calls")
  will also influence review comments. Teams should audit for content that might produce unwanted
  review behavior.

## Extraction Notes

1. **WebFetch returned AI-processed summaries, not verbatim text**: Both WebFetch attempts
   returned content processed through a small model rather than raw source text. Quotes shown
   in this note are those that appeared in double-quotes in the WebFetch output and are likely
   verbatim or close to verbatim. The Assayer should verify all quotes against the source URL
   directly. The availability-section quote (Claim 3) could not be recovered verbatim from
   either WebFetch response and is marked accordingly.

2. **Source is very short**: The June 18 changelog is a brief feature announcement (estimated
   100-200 words based on the WebFetch summary depth). The five claims above are likely
   exhaustive — this is a thin changelog that announces the feature without providing setup steps,
   configuration details, or interaction guidance between AGENTS.md and the other configuration
   surfaces (SKILL.md, copilot-instructions.md, MCP). Those details presumably live in linked
   documentation pages that were not fetched.

3. **No setup steps documented**: Unlike the June 2 and June 12 changelogs (which included step-
   by-step setup paths), this source provides no configuration steps for AGENTS.md. The file must
   be at the repository root — that is the only structural requirement stated. No settings to enable,
   no admin action required.

4. **Interaction with other surfaces not addressed**: The source does not explain how AGENTS.md
   interacts with `.github/copilot-instructions.md`, SKILL.md, or MCP context when all are present.
   Precedence, merging, or override behavior is not documented. This is an open question for a
   future source or documentation follow-up.

5. **No contradictions to file**: All claims in this source either extend or corroborate existing
   corpus notes. No existing source makes claims this source would refute. No contradiction issue
   required.

6. **"Generally available" confirmation**: Both WebFetch responses independently confirmed GA status
   (not preview). This is notable because prior June 2026 code review features (June 2, June 12)
   launched as "public preview." The GA status was consistent across both retrieval attempts, giving
   higher confidence in this fact despite the verbatim-text caveat.
