---
source_url: https://github.blog/changelog/2026-07-14-github-copilot-for-jetbrains-expands-byok-capabilities
source_type: docs
title: "GitHub Copilot for JetBrains expands BYOK capabilities"
author: GitHub (official changelog)
date_published: 2026-07-14
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: settled
issue: "#1880"
---

# GitHub Copilot for JetBrains Expands BYOK Capabilities

> GitHub's July 14, 2026 JetBrains changelog adds custom OpenAI-compatible BYOK endpoints,
> a public-preview local sandboxing mode, an integrated plugin marketplace browser, Claude
> agent provider customizations support (Pro and higher, public preview), a built-in CLI
> debugger skill, and a policy carve-out so that disabling Copilot CLI by policy no longer
> disables the Copilot CLI provider inside JetBrains IDEs.

## Source Context

- **Type**: docs (GitHub official product changelog, July 14, 2026; a short "What's new"
  changelog entry of roughly 250-300 words spanning six named feature sections plus UX and
  reliability notes)
- **Author credibility**: GitHub engineering team announcing production feature releases in
  the JetBrains Copilot plugin. Authoritative for the existence and stated behavior of each
  feature, the named plan-tier restriction on Claude agent provider customizations, and the
  public-preview labels applied to local sandboxing and the CLI debugger skill. Not
  authoritative for: how local sandboxing isolation differs technically from cloud sandboxing
  (the page links out to a separate docs page for that), performance or reliability of the new
  OpenAI-compatible custom endpoint path, or why no plan-tier restriction is stated for the
  BYOK custom-endpoint and local-sandboxing features specifically.
- **Scope**: Six named feature areas in the July 14, 2026 JetBrains Copilot update — BYOK
  custom endpoint support, expanded plugin management, Claude agent provider customizations
  support, local sandboxing support, a built-in Copilot CLI debugger skill, and a Copilot CLI
  policy behavior change for CLI-as-default scenarios — plus a UX-enhancements section and a
  quality/reliability section. Does NOT cover: plan-tier eligibility for BYOK custom endpoints
  or local sandboxing (not stated in the page), the mechanics of the new custom endpoint
  configuration UI, what "more complete" plugin management means beyond marketplace/source-repo
  browsing, or the difference between local and cloud sandbox isolation models (deferred to a
  linked docs page not fetched as part of this extraction).

## Extracted Claims

### Claim 1: BYOK now supports custom, OpenAI-compatible endpoints with API keys, not just named providers

- **Evidence**: Official changelog "What's new" section, first bullet.
- **Confidence**: settled (product fact stated definitively; no preview qualifier attached)
- **Quote**: "We've expanded bring your own key support with custom endpoints. You can now configure OpenAI-compatible custom endpoints with API keys to use your own models."
- **Our assessment**: This is a materially different BYOK mechanism from the named-provider lists documented for VS Code (`docs-github-copilot-byok-vscode.md`, Claim 2: Anthropic, Gemini, OpenAI, OpenRouter, Azure, Ollama, Foundry Local) and JetBrains itself as of June 2 (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 10, which only documented the removal of the Editor Preview flag requirement — not a custom-endpoint capability). "Custom endpoints" means any model server that speaks the OpenAI-compatible API shape can be wired in without GitHub naming it as a supported provider, which is the same pattern the Copilot app used for "any OpenAI-compatible endpoint" (`docs-github-copilot-byok-app.md`, Claim 1). This closes a gap that existed in JetBrains: previously JetBrains BYOK was scoped to named providers (per the June 2 note); now self-hosted or niche OpenAI-compatible model servers are addressable directly.
- **Our assessment**: The changelog does not state a plan-tier restriction for this feature, unlike the neighboring Claude agent provider customizations feature (Claim 3 below), which is explicitly scoped to "GitHub Copilot Pro and higher." That asymmetry is notable but should not be read as "available on all tiers" — it is simply unstated in this source.

### Claim 2: JetBrains now includes a more complete plugin management experience, letting practitioners browse and install plugins through the marketplace or from the source repository

- **Evidence**: Official changelog "What's new" section, "Expanded customizations with plugin management" heading.
- **Confidence**: settled (product fact stated definitively)
- **Quote**: "GitHub Copilot for JetBrains now includes a more complete plugin management experience in customizations."
- **Quote**: "browse and install plugins through the marketplace or from the source repository"
- **Our assessment**: This adds a discovery/installation UI layer inside the customizations surface, similar in spirit to the Agent Customizations editor introduced June 2 (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 8: "a centralized UI for creating and managing all your agent customizations in one place"). The July 14 change specifically targets *plugin* discovery and installation (marketplace browsing, source-repository installation) rather than the agent/skill/instruction editing that Claim 8 covered. The two features are complementary parts of the same "customizations" panel rather than the same capability restated.

### Claim 3: Customizations now support Claude as an agent provider for setting up custom agents, skills, and instructions, available to GitHub Copilot Pro and higher plans in public preview

- **Evidence**: Official changelog "What's new" section, "Claude agent provider customizations support" heading, with an explicit plan-tier and preview-status qualifier.
- **Confidence**: emerging (explicitly labeled public preview)
- **Quote**: "Customizations now support Claude agent provider, allowing you to set up custom agents, skills, and instructions."
- **Quote**: "GitHub Copilot Pro and higher plans in public preview"
- **Our assessment**: This is distinct from — and builds on — Claude becoming a *selectable agent provider* in the JetBrains agent picker, which reached public preview on June 22, 2026 (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, Claim 1: "Claude as agent provider is now available in public preview... all without leaving your JetBrains IDE," requiring the Claude Code CLI to be installed and its path configured). The June 22 source covered *selecting* Claude as the agent backend for a session; this July 14 source covers *customizing* that Claude-backed agent — configuring custom agents, skills, and instructions specifically for the Claude provider, via the customizations UI (Claim 2's marketplace-adjacent panel). The plan-tier detail is new information: the June 22 note did not state an individual-plan restriction (it discussed Business/Enterprise "Editor preview features" policy gating), while this note explicitly scopes Claude customizations to "Pro and higher" — implying Free-tier users are excluded from this specific capability, though this note does not clarify how the Pro-and-higher gate interacts with the Business/Enterprise Editor Preview policy documented for Claude-as-provider itself.

### Claim 4: JetBrains now supports local sandboxing, including new sandbox settings and configuration flows in the plugin, available in public preview

- **Evidence**: Official changelog "What's new" section, "Local sandboxing support" heading, explicitly labeled public preview, with a link to a separate docs page describing cloud vs. local sandboxes.
- **Confidence**: emerging (explicitly labeled public preview)
- **Quote**: "This release adds support for local sandboxing, including new sandbox settings and configuration flows in the JetBrains plugin."
- **Quote**: "This feature is in public preview."
- **Our assessment**: This is the first source in our corpus documenting sandbox *isolation mode selection* as a JetBrains-configurable dimension. The June 2 JetBrains note (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 11) mentioned "multiple isolation modes" only as one of three differentiators justifying the phased rollout of Copilot CLI agent as the JetBrains default — it did not name "local" vs. "cloud" sandboxing as the two modes or describe any configuration flow. This July 14 note gives that isolation-mode claim concrete shape: practitioners can now choose a local sandbox (via new settings in the plugin) as an alternative to whatever the prior default was. The page links to "About cloud and local sandboxes" (`docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes`) for the technical distinction, which this extraction did not follow — the mechanics of what a "local sandbox" isolates against (filesystem scope, network access, process boundaries) are not established by this source and should be verified against that docs page before the guide states specifics.

### Claim 5: A built-in debugger skill for Copilot CLI sessions is now available in public preview, enabling agent-driven debugging workflows directly in the development environment

- **Evidence**: Official changelog "What's new" section, "Built-in debugger skill for Copilot CLI" heading, explicitly labeled public preview.
- **Confidence**: emerging (explicitly labeled public preview)
- **Quote**: "agent-driven debugging workflows directly in your development environment"
- **Our assessment**: This is a first-party skill shipped with the plugin rather than a `.github/skills/`-based custom skill installed via `gh skill` (documented in `docs-github-copilot-agent-skills-cli.md`). It is a different capability from the Agent Debug Panel (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 5, enhanced further in `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, Claim 5): the Agent Debug Panel is an observability surface for watching what an agent did during a session; this debugger skill is a tool the agent itself can invoke to debug the practitioner's code (e.g., set breakpoints, inspect state) as part of an agentic workflow. The changelog does not specify which debuggers or languages are supported, or how the skill differs from a practitioner manually driving the JetBrains debugger.

### Claim 6: Disabling Copilot CLI by policy no longer affects the Copilot CLI provider inside JetBrains IDEs

- **Evidence**: Official changelog "What's new" section, framed as an adjustment to "Copilot CLI provider policy handling for CLI-as-default scenarios."
- **Confidence**: settled (policy-behavior fact stated definitively)
- **Quote**: "We've adjusted Copilot CLI provider policy handling for CLI-as-default scenarios."
- **Quote**: "Disabling Copilot CLI by policy no longer affects Copilot CLI provider in JetBrains IDEs."
- **Our assessment**: This decouples two things that were previously coupled: the organization-level "Copilot CLI" policy (which gates standalone terminal CLI access, and per `docs-github-copilot-byok-app.md` Claim 7 also gates access to the standalone Copilot app) and the *in-IDE* Copilot CLI provider that JetBrains is phasing in as its default agent experience (per `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 11: "a phased transition to make Copilot CLI agent... the default"). Before this change, an admin disabling the standalone Copilot CLI policy would presumably also have removed the CLI-as-default agent experience inside JetBrains — undermining the phased default rollout for any org that had disabled standalone CLI access for other reasons (e.g., to keep terminal-level file access restricted while still wanting the in-IDE agentic experience). This carve-out lets GitHub proceed with CLI-as-default in JetBrains independent of the standalone CLI policy toggle. The changelog does not state whether a *new*, separate policy now controls the JetBrains-embedded CLI provider, or whether it is simply no longer policy-gated at all.

## Concrete Artifacts

### JetBrains BYOK and Sandboxing Update — Feature Inventory (July 14, 2026)

```
GitHub Copilot for JetBrains — July 14, 2026 Changelog

WHAT'S NEW:
  1. Bring your own key custom endpoint support
     "We've expanded bring your own key support with custom endpoints.
     You can now configure OpenAI-compatible custom endpoints with API
     keys to use your own models."
     Plan tier: not stated. Preview status: not stated.

  2. Expanded customizations with plugin management
     "GitHub Copilot for JetBrains now includes a more complete plugin
     management experience in customizations."
     "browse and install plugins through the marketplace or from the
     source repository"

  3. Claude agent provider customizations support
     "Customizations now support Claude agent provider, allowing you to
     set up custom agents, skills, and instructions."
     Plan tier: "GitHub Copilot Pro and higher plans"
     Status: public preview

  4. Local sandboxing support
     "This release adds support for local sandboxing, including new
     sandbox settings and configuration flows in the JetBrains plugin."
     Status: public preview
     See also: docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes

  5. Built-in debugger skill for Copilot CLI
     "agent-driven debugging workflows directly in your development
     environment"
     Status: public preview

CHANGED:
  6. Copilot CLI provider policy for CLI-as-default scenarios
     "We've adjusted Copilot CLI provider policy handling for
     CLI-as-default scenarios. Disabling Copilot CLI by policy no
     longer affects Copilot CLI provider in JetBrains IDEs."

USER EXPERIENCE ENHANCEMENTS (not extracted as standalone claims):
  - Improved model picker controls and authentication UX
  - "message re-edit support in inline and CLI experiences for faster
    prompt iteration"

QUALITY IMPROVEMENTS (not extracted as standalone claims):
  - "reliability and stability across authentication recovery, account
    switching, provider and session persistence, and editor interaction
    paths"
```

*Source: GitHub Copilot for JetBrains expands BYOK capabilities, GitHub changelog, July 14, 2026*

### Page Section Structure (as fetched)

```
GitHub Copilot for JetBrains expands BYOK capabilities
├── What's new
│   ├── Bring your own key custom endpoint support
│   ├── Expanded customizations with plugin management
│   ├── Claude agent provider customizations support
│   ├── Local sandboxing support
│   └── Built-in debugger skill for Copilot CLI
├── User experience enhancements
├── Quality improvements
├── Changed
├── Try it out
└── Share your feedback
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 11): The June 2 note
    named "multiple isolation modes" as one of three differentiators for CLI-as-default in
    JetBrains, without naming the modes. This note's Claim 4 (local sandboxing, public preview)
    corroborates and gives concrete shape to that isolation-mode claim by naming "local" as one
    of the modes and linking to a docs page that contrasts it with "cloud" sandboxing.
  - `docs-github-copilot-byok-app.md` (Claim 1): That source documented "any OpenAI-compatible
    endpoint" as a catch-all BYOK provider category for the standalone Copilot app. This note's
    Claim 1 confirms the same OpenAI-compatible-endpoint pattern is now available in JetBrains,
    corroborating that GitHub is standardizing "custom OpenAI-compatible endpoint" as a BYOK
    mechanism across surfaces (app and now JetBrains) rather than only naming specific providers.

- **Extends**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` (Claim 1): That June 22
    source made Claude *selectable* as a JetBrains agent provider (public preview, requiring a
    local Claude Code CLI installation). This note's Claim 3 extends that by adding a
    *customizations* layer specifically for the Claude provider — custom agents, skills, and
    instructions — scoped to Pro-and-higher plans. This is the first source to attach a named
    individual-plan-tier restriction ("Pro and higher") to any part of the Claude-in-JetBrains
    integration; the June 22 source only discussed Business/Enterprise Editor Preview policy
    gating, not individual-plan tiers.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 8): The June 2 Agent
    Customizations editor gave JetBrains a centralized UI for agents/skills/instructions/prompts.
    This note's Claim 2 extends that same customizations surface with plugin discovery and
    installation (marketplace browsing, source-repo installation) — a new customizations
    dimension (plugins) alongside the existing agent-configuration dimension.
  - `docs-github-copilot-byok-vscode.md` (Claim 2) and `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
    (Claim 10): Prior JetBrains and VS Code BYOK documentation covered named-provider lists and
    policy-flag removal, respectively. This note's Claim 1 extends JetBrains BYOK from
    named-provider-only to include arbitrary OpenAI-compatible custom endpoints.
  - `docs-github-copilot-byok-app.md` (Concrete Artifacts "BYOK Governance Comparison" table):
    That table listed JetBrains BYOK as "DEDICATED POLICY... controlled via own policy at
    github.com/settings/copilot/features" with no mention of a custom-endpoint path. This note
    adds the custom-endpoint capability to that governance picture without stating whether the
    same dedicated policy also gates custom endpoints specifically — an open question for the
    Assayer or a future source to resolve.

- **Contradicts**: None identified against existing source notes. This note's own internal
  asymmetry — Claim 3 (Claude customizations) carries an explicit "Pro and higher" plan-tier
  restriction while Claims 1 and 4 (BYOK custom endpoints, local sandboxing) state no plan-tier
  restriction at all — is not a contradiction between two claims about the same feature; it is
  three different features documented with different levels of specificity in the same
  changelog. Not filed as a contradiction per MINER.md §4a (conditioning-variable / differing
  scope, not opposing claims about the same fact).

- **Novel**:
  - **OpenAI-compatible custom endpoint BYOK in JetBrains** (Claim 1): No prior JetBrains source
    documents a custom-endpoint (as opposed to named-provider) BYOK path.
  - **Local sandboxing as a JetBrains-configurable isolation mode** (Claim 4): First source to
    name and describe a concrete "local sandbox" setting in JetBrains, moving the "multiple
    isolation modes" claim from `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
    (Claim 11) from an abstract differentiator to a configurable feature.
  - **Integrated plugin marketplace/source-repo browser inside Copilot customizations** (Claim 2):
    No prior source documents plugin discovery/installation happening from within the Copilot
    customizations panel itself.
  - **A first-party, built-in CLI debugger skill** (Claim 5): No prior source documents a
    GitHub-shipped (not `.github/skills/`-installed) debugging skill for Copilot CLI.
  - **Decoupling the standalone Copilot CLI policy from the in-IDE JetBrains CLI provider**
    (Claim 6): First source documenting that these two were previously coupled and are now
    independently controllable.
  - **A named individual-plan-tier gate ("Pro and higher") on a Claude-in-JetBrains capability**
    (Claim 3): Prior Claude-in-JetBrains documentation discussed only Business/Enterprise policy
    gating, not an individual-plan floor.

## Guide Impact

- **Chapter 02 (Harness Engineering — BYOK / Model Configuration)**:
  - Update the BYOK surface inventory to note that JetBrains BYOK now supports arbitrary
    OpenAI-compatible custom endpoints (Claim 1), not just the named-provider list documented
    for VS Code and the app. Flag that this note does not state a plan-tier restriction for this
    path, in contrast to the neighboring Claude customizations feature (Claim 3), and that this
    should be verified before the guide states "available on all tiers."
  - Add Claude agent provider *customizations* (Claim 3) as distinct from Claude agent provider
    *selection* (already documented from the June 22 source): customizing a Claude-backed agent
    with custom agents/skills/instructions requires Copilot Pro or higher, in public preview.

- **Chapter 03 (Infrastructure — Sandbox / Isolation Models)**:
  - Add local sandboxing (Claim 4) as a JetBrains-configurable isolation mode, public preview.
    Recommend following up on `docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes`
    (not fetched in this extraction) before writing guide-level guidance on when to choose local
    vs. cloud sandboxing — this note establishes only that the choice now exists and is
    configurable, not the isolation guarantees of either mode.

- **Chapter 04 (Agentic Workflows — Debugging)**:
  - Add the built-in Copilot CLI debugger skill (Claim 5) as a first-party alternative to
    custom-installed debugging skills, public preview. Note it is distinct from the Agent Debug
    Panel (which observes agent activity) — this skill lets the agent itself perform debugging.

- **Chapter 05 (Governance — Policy Scoping)**:
  - Update any guide language that assumes disabling the org-level "Copilot CLI" policy also
    disables the in-IDE JetBrains CLI provider (Claim 6) — as of July 14, 2026 these are
    decoupled. Organizations that disabled standalone Copilot CLI access for other reasons should
    re-verify whether the JetBrains CLI-as-default agent experience is still active for their
    members.

## Extraction Notes

1. **Source is short (~250-300 words) but dense**: six distinct "What's new" feature items plus
   a "Changed" policy note were extracted as six claims. Two lower-signal sections (user
   experience enhancements, quality improvements) were captured verbatim in Concrete Artifacts
   but not expanded into standalone claims — they are generic UX/reliability polish without a
   specific, guide-relevant mechanism to assess.
2. **Two triage comments exist on the source issue** (#1880), both authored by the repo owner
   with near-identical timestamps (14 seconds apart). They appear to be a duplicate triage run
   rather than sequential revisions. Both list overlapping existing notes and largely agree; this
   extraction treated the union of both as guidance and independently verified every claim against
   the live source rather than trusting either comment's characterization (e.g., the second
   comment's "all-tier support" framing for the policy change was not corroborated by the source
   text and was not carried into the claims above).
3. **One linked page not followed**: the "About cloud and local sandboxes" docs page
   (`docs.github.com/copilot/concepts/about-cloud-and-local-sandboxes`) was identified via the
   page's outbound links but not fetched. Per MINER.md §1 guidance to follow up to 5 substantive
   linked pages, this one is a strong candidate for a future extraction or Assayer follow-up,
   since it likely contains the technical detail (isolation guarantees, what's sandboxed) that
   this changelog explicitly defers to it. Flagged rather than speculated on.
4. **Multiple WebFetch passes**: three WebFetch calls were made with progressively narrower
   prompts to cross-check verbatim quote consistency (a general extraction, a full-verbatim
   request, and a targeted request for plan-tier/status/heading-structure details). All quotes
   used in this note were consistent across at least two of the three fetches.
5. **No contradictions filed**: see Cross-References → Contradicts above; the internal
   plan-tier-disclosure asymmetry between claims does not rise to a MINER.md §4a contradiction.
