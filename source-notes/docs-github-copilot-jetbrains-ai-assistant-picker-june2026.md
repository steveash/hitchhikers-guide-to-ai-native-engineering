---
source_url: https://github.blog/changelog/2026-06-30-copilot-agent-is-now-available-in-jetbrains-ai-assistant
source_type: docs
title: "Copilot Agent is now available in JetBrains AI Assistant"
author: GitHub (official changelog)
date_published: 2026-06-30
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1431"
---

# Copilot Agent is now available in JetBrains AI Assistant

> GitHub's June 30, 2026 changelog announces GitHub Copilot as a first-class,
> natively selectable agent option inside **JetBrains AI Assistant** (JetBrains'
> own standalone AI product) via the Agent Client Protocol, upgrading Copilot
> from an ACP-connected option to a picker-level entry with model choice and
> reasoning-depth control — the mirror image of the June 22 announcement that
> made Claude selectable inside the *GitHub Copilot plugin's* own agent picker.

## Source Context

- **Type**: docs (GitHub official product changelog, June 30, 2026; a short
  "Release" entry, self-tagged "1 minute read," roughly 230 words across three
  sections: "What's new," "What's next," and "Share your feedback")
- **Author credibility**: GitHub engineering team announcing a production
  integration co-developed with JetBrains. Authoritative for: the existence and
  described behavior of the integration, which product surface it lives in
  (JetBrains AI Assistant's agent picker, not the GitHub Copilot plugin), and
  the stated roadmap items. Not authoritative for: how Copilot's agent
  performance compares to JetBrains' own native agents inside AI Assistant,
  pricing/credit metering for this integration, or whether any admin
  policy/feature-flag gate applies (the changelog does not mention one, unlike
  several JetBrains Copilot-plugin changelogs in this corpus that explicitly
  require the "Editor preview features" policy).
- **Scope**: Covers the single feature launch (Copilot as a native agent-picker
  option in JetBrains AI Assistant) plus three named roadmap items (NES
  support, Skills, deeper cross-tool orchestration). Does NOT cover: setup
  steps or prerequisites (no settings path or install instructions are given,
  unlike peer JetBrains changelogs in this corpus), permission/approval
  behavior for Copilot-initiated file edits or commands in this surface,
  pricing/credit consumption, or a GA/preview status label for the feature.

## Extracted Claims

### Claim 1: GitHub Copilot is now a first-class, natively selectable agent option in the JetBrains AI Assistant agent picker — upgraded from its prior status as an ACP-connected option

- **Evidence**: Official GitHub changelog explicitly distinguishes two prior
  states (the separate GitHub Copilot plugin used as a JetBrains IDE pair
  programmer, and Copilot already reachable inside JetBrains AI Assistant via
  the Agent Client Protocol) from the new state announced here (Copilot as "a
  first-class option in the AI Assistant agent picker").
- **Confidence**: emerging (freshly announced integration; no GA/preview label
  given by the source, and no independent behavioral verification exists yet)
- **Quote**: "Today, JetBrains and GitHub are announcing a deeper integration
  between JetBrains AI Assistant and GitHub Copilot. Millions of developers
  already rely on the GitHub Copilot plugin as their AI pair programmer in
  JetBrains IDEs, and Copilot has also been available inside JetBrains AI
  Assistant through the Agent Client Protocol (ACP). Now we are taking the
  next step: GitHub Copilot is a first-class option in the AI Assistant agent
  picker, so you can choose the entry point that best fits your workflow."
- **Our assessment**: This is the headline fact and it names three distinct
  JetBrains-facing Copilot surfaces in one paragraph: (1) the GitHub Copilot
  *plugin* (covered by `docs-github-copilot-jetbrains-cli-agent-sessions.md`,
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, and
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` in this
  corpus), (2) Copilot reachable inside JetBrains' own **AI Assistant** product
  via ACP (a pre-existing but previously undocumented-in-corpus integration),
  and (3) the new first-class agent-picker status announced today. None of the
  three existing JetBrains source notes in this corpus mention "AI Assistant"
  as a product name or "Agent Client Protocol" — they are all scoped to the
  GitHub Copilot plugin's own agent picker (where Claude and the Copilot CLI
  agent are selectable). This claim establishes that JetBrains AI Assistant is
  a genuinely separate integration surface from the Copilot plugin, and the
  two are now symmetric: the Copilot plugin lets you pick Claude as your
  agent; JetBrains AI Assistant lets you pick Copilot as your agent. For Ch02:
  document this as a distinct, third JetBrains AI surface (alongside the
  Copilot plugin and the Copilot CLI) so practitioners don't conflate "Copilot
  in JetBrains" as a single integration.

### Claim 2: Selecting GitHub Copilot from the AI Assistant agent picker makes it the active agent for the current chat conversation

- **Evidence**: Official changelog, listed under "What's new" as the first
  bullet, describing the mechanical selection step.
- **Confidence**: settled (direct, mechanical product-behavior statement)
- **Quote**: "GitHub Copilot as a native agent picker: Open the agent picker
  in the AI chat and select GitHub Copilot to make it the active agent for the
  conversation."
- **Our assessment**: This confirms the integration is picker-scoped per
  conversation (not a global default switch) — consistent with how the
  Copilot plugin's own agent picker works for Claude/CLI-agent selection in
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1
  and `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 1.
  The per-conversation scoping pattern (pick an agent provider at the start of
  a chat, not as a persistent IDE-wide setting) now appears to be JetBrains'
  standard UX convention across both the AI Assistant and Copilot-plugin
  agent pickers.

### Claim 3: Practitioners can choose between supported Copilot models and tune reasoning depth directly in the AI Assistant chat, to balance speed, depth, and cost

- **Evidence**: Official changelog, second "What's new" bullet.
- **Confidence**: settled (direct product-capability statement)
- **Quote**: "Pick your Copilot model: Choose between supported Copilot models
  and tune reasoning depth right in the AI chat to balance speed, depth, and
  cost."
- **Our assessment**: This mirrors the reasoning/thinking-effort control
  documented for the Copilot plugin's own JetBrains model picker in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 7 ("For
  reasoning models that support configurable thinking effort, you can now
  control how much reasoning the model applies to each request, directly from
  the model picker"). The new source does not specify which Copilot models
  are "supported" in the AI Assistant surface, nor whether the effort-level
  granularity matches the Copilot plugin's implementation — this is a gap the
  source leaves open. For Ch02: note that both JetBrains Copilot surfaces
  (plugin and AI Assistant) now expose per-request reasoning-depth control,
  but do not assume feature parity between them without further confirmation.

### Claim 4: The integration supports handing off multistep coding tasks, where Copilot reasons through the project, proposes changes, runs commands, and iterates with the practitioner

- **Evidence**: Official changelog, third "What's new" bullet, describing the
  agentic task-execution capability.
- **Confidence**: emerging (vendor-authored capability description; no
  independent verification of actual agentic behavior quality in this specific
  surface, and no isolation-mode, permission-approval, or safety mechanism is
  mentioned for it — contrast with the Copilot-plugin CLI agent's documented
  worktree/workspace isolation modes)
- **Quote**: "Real coding tasks: Hand off multistep work and Copilot will
  reason through your project, propose changes, run commands, and iterate
  with you."
- **Our assessment**: The phrase "run commands" implies tool/shell execution
  access, but the source gives no detail on approval gating, sandboxing, or
  isolation for this surface — unlike `docs-github-copilot-jetbrains-cli-agent-sessions.md`
  Claim 2/3, which explicitly document worktree vs. workspace isolation modes
  for the Copilot-plugin CLI agent, and unlike
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 2,
  which explicitly discloses that the JetBrains Claude agent integration runs
  in bypass-permissions mode. This changelog is silent on the equivalent
  question for Copilot-in-AI-Assistant. For Ch02/Ch05 (governance): flag this
  as an open question rather than assume either safe-by-default or
  bypass-by-default behavior — practitioners evaluating this surface for
  team use should verify the approval/sandboxing model directly in the
  product before relying on it for unattended multistep work.

### Claim 5: GitHub and JetBrains plan to add Next Edit Suggestions (NES) support to this integration, to guide practitioners through multistep code changes by surfacing the next likely edit

- **Evidence**: Official changelog, "What's next" section, listed as the
  first of three roadmap items.
- **Confidence**: anecdotal (explicitly a forward-looking roadmap statement,
  not a shipped capability; no timeline given)
- **Quote**: "NES support: Next Edit Suggestions will guide you through
  multistep code changes by surfacing your next likely edit."
- **Our assessment**: Roadmap-only; do not represent this as available in the
  guide. Worth tracking as a "coming soon" item since NES is a distinct
  capability from the agentic hand-off described in Claim 4 — it's a
  suggestion/autocomplete-style aid rather than autonomous execution.

### Claim 6: GitHub and JetBrains plan to add "Skills" to this integration, to help developers invoke reusable, specialized capabilities more quickly

- **Evidence**: Official changelog, "What's next" section, second roadmap
  item.
- **Confidence**: anecdotal (roadmap statement, no timeline or scope detail)
- **Quote**: "Skills: Helping developers invoke reusable, specialized
  capabilities more quickly, making common workflows more efficient and
  consistent."
- **Our assessment**: The source does not clarify whether these "Skills" would
  be the same Copilot Agent Skills documented elsewhere in this corpus (e.g.,
  `docs-github-copilot-agent-skills-cli.md`, and confirmed GA for the
  Copilot plugin in JetBrains by `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
  Claim 9) or a JetBrains-AI-Assistant-native skills concept. This is a
  genuine ambiguity in the source, not an inference — flag it as an open
  question for future mining once GitHub ships and documents this roadmap
  item concretely.

### Claim 7: GitHub and JetBrains plan "deeper orchestration across tools," further improving how Copilot plans, executes, and iterates on complex development tasks directly within the IDE

- **Evidence**: Official changelog, "What's next" section, third roadmap item.
- **Confidence**: anecdotal (roadmap statement, no concrete mechanism
  described)
- **Quote**: "Deeper orchestration across tools: Further improving how
  Copilot plans, executes, and iterates on complex development tasks directly
  within the IDE."
- **Our assessment**: Too vague to act on for the guide beyond noting
  direction of travel: GitHub is signaling continued investment in
  Copilot-as-agent inside JetBrains AI Assistant specifically (not just the
  Copilot plugin), reinforcing Claim 1's point that this is a maturing,
  independently-invested-in integration surface rather than a one-off
  announcement.

## Concrete Artifacts

### JetBrains Copilot Surfaces — Product Map (as of June 30, 2026, per this source and corpus cross-reference)

```
Surface 1: GitHub Copilot plugin (JetBrains IDEs)
  - Copilot's own agent picker, selectable agents include:
    Copilot's native agent, Copilot CLI agent, Claude (via Claude Code CLI,
    public preview as of June 22, 2026)
  - Covered by: docs-github-copilot-jetbrains-cli-agent-sessions.md,
    docs-github-copilot-jetbrains-cli-enhancements-june2026.md,
    docs-github-copilot-jetbrains-claude-agent-provider-june2026.md

Surface 2: JetBrains AI Assistant (JetBrains' own standalone AI product)
  - Copilot previously reachable via Agent Client Protocol (ACP)
  - As of June 30, 2026: Copilot is a first-class option in AI Assistant's
    own agent picker, with model selection + reasoning-depth tuning
  - Covered by: this source note (docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md)

No settings path, prerequisite, or admin policy gate is given in this
source for Surface 2 — contrast with Surface 1 sources, which consistently
document an "Editor preview features" policy requirement for Business/
Enterprise admins.
```

*Source: this changelog entry, cross-referenced against the three existing
JetBrains-scoped source notes in this corpus.*

### What's New / What's Next (verbatim, GitHub changelog, June 30, 2026)

```
What's new:
- GitHub Copilot as a native agent picker: Open the agent picker in the AI
  chat and select GitHub Copilot to make it the active agent for the
  conversation.
- Pick your Copilot model: Choose between supported Copilot models and tune
  reasoning depth right in the AI chat to balance speed, depth, and cost.
- Real coding tasks: Hand off multistep work and Copilot will reason through
  your project, propose changes, run commands, and iterate with you.

What's next:
- NES support: Next Edit Suggestions will guide you through multistep code
  changes by surfacing your next likely edit.
- Skills: Helping developers invoke reusable, specialized capabilities more
  quickly, making common workflows more efficient and consistent.
- Deeper orchestration across tools: Further improving how Copilot plans,
  executes, and iterates on complex development tasks directly within the
  IDE.
```

*Source: "Copilot Agent is now available in JetBrains AI Assistant," GitHub
changelog, June 30, 2026.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 7):
    That note documents per-request thinking-effort/reasoning-depth control
    added to the Copilot-plugin's own JetBrains model picker on June 2, 2026.
    Claim 3 here corroborates that reasoning-depth tuning is now a
    cross-surface convention for GitHub Copilot in JetBrains — appearing in
    both the Copilot plugin's model picker and (per this source) the AI
    Assistant agent picker.
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`
    (Claim 1): That note documents Claude becoming selectable inside the
    Copilot plugin's own agent picker on June 22, 2026, with the framing
    "giving you more flexibility to pick the agent that best fits your
    task." Claim 1 here documents the mirror-image move — Copilot becoming
    selectable inside JetBrains' own AI Assistant agent picker — corroborating
    a broader pattern of cross-vendor agent-picker reciprocity in JetBrains
    tooling (each vendor's chat surface now offers the other's agent as an
    option).

- **Contradicts**: None identified. No existing corpus source makes a
  conflicting claim about Copilot's availability or behavior inside JetBrains
  AI Assistant specifically — this is the first corpus source to name that
  product surface at all. No contradiction issue filed.

- **Extends**: None directly — this source does not build on a prior
  in-corpus JetBrains AI Assistant note (none existed before this one). It is
  topically adjacent to (but does not extend) the three Copilot-plugin
  JetBrains notes listed above, since those cover a different integration
  surface.

- **Novel**:
  - **JetBrains AI Assistant as a distinct, previously-undocumented-in-corpus
    Copilot integration surface** (Claim 1): No prior source note in this
    corpus mentions "JetBrains AI Assistant" as a product name or the "Agent
    Client Protocol (ACP)" as an integration mechanism. All three existing
    JetBrains-scoped notes are exclusively about the GitHub Copilot plugin.
    This is the first documentation of the reverse integration direction:
    Copilot as a guest agent inside a JetBrains-native AI product, rather
    than JetBrains agents (Claude, CLI agent) as guests inside the Copilot
    plugin.
  - **Absence of a stated permission/approval model for agentic actions in
    this surface** (Claim 4): Every other corpus source documenting a
    JetBrains agentic-execution capability (worktree/workspace isolation for
    the CLI agent; bypass-permissions mode for the Claude agent provider)
    explicitly states how file edits and commands are approved. This source
    is silent on that question for Copilot-in-AI-Assistant, which is itself
    a notable gap worth flagging rather than assuming.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tool/Surface Selection)**: Add JetBrains
  AI Assistant as a third documented JetBrains-facing Copilot surface,
  distinct from the GitHub Copilot plugin and the standalone Copilot CLI.
  Update any guide language that treats "Copilot in JetBrains" as a single
  integration — it is now at least two separately evolving surfaces (Copilot
  plugin's own picker vs. AI Assistant's picker), each with different
  disclosed feature sets (e.g., isolation modes and bypass-permissions status
  are documented for the Copilot-plugin surfaces but not for AI Assistant).

- **Chapter 02 (Harness Engineering — Governance/Permissions)**: Flag the
  undocumented approval model for Copilot's "run commands" capability inside
  JetBrains AI Assistant (Claim 4) as an open question. Recommend
  practitioners/teams verify the actual approval/sandboxing behavior directly
  before using this surface for unattended multistep work, rather than
  assuming parity with the Copilot-plugin CLI agent's worktree isolation or
  the Claude-agent-provider's (disclosed) bypass-permissions mode.

- **Chapter 01 (Daily Workflows — Tool Selection)**: Note the reciprocal
  agent-picker pattern now visible across JetBrains tooling: the Copilot
  plugin lets you pick Claude as your execution agent; JetBrains AI Assistant
  lets you pick Copilot as your execution agent. Practitioners choosing a
  JetBrains entry point should be aware they are choosing both a chat surface
  *and* an available-agent set, which differs between the two products.

## Extraction Notes

1. **Source is very short** (~230 words, self-tagged "1 minute read" by
   GitHub). This limits the claim count below the 5-15 target suggested in
   `agents/MINER.md`; 7 claims were extracted and represent essentially all
   of the substantive content in the article. No sub-pages were linked from
   the changelog entry itself to follow.
2. **Two-source verification for quotes**: An initial WebFetch call returned
   an AI-summarized/paraphrased version of the page (not usable for direct
   quotes per MINER.md §2a). A second pass fetched the raw HTML directly via
   `curl` and stripped markup by hand to recover the verbatim text used for
   every `Quote` field in this note. All quotes above were copied
   character-for-character from that raw-text extraction.
3. **No setup/prerequisite information in the source**: Unlike the three
   existing JetBrains Copilot-plugin changelogs in this corpus, this entry
   gives no settings path, install prerequisite, or admin policy gate for the
   AI Assistant integration. This is noted as a gap in Claim 4 and the
   Concrete Artifacts product map, not filled in by inference.
4. **Related same-day post not extracted**: The page's "Related Posts" footer
   links to a separate June 30, 2026 changelog entry, "Claude Sonnet 5 is
   generally available for GitHub Copilot." That is a distinct URL/article
   and was not fetched or extracted here — it is a candidate for a separate
   source-submission issue if not already in the pipeline.
5. **No contradictions found**: This source does not conflict with any
   existing corpus note; it documents a previously-undocumented product
   surface. No contradiction issue filed.
