---
source_url: https://blog.jetbrains.com/ai/2026/06/github-copilot-now-an-integrated-agent/
source_type: blog-post
title: "GitHub Copilot now an Integrated Agent in JetBrains IDEs"
author: Dominique Rolink
date_published: 2026-06-30
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: emerging
issue: "#1495"
---

# GitHub Copilot now an Integrated Agent in JetBrains IDEs

> JetBrains' own vendor-perspective post on the June 30, 2026 launch of GitHub
> Copilot as a first-class, natively-picker-selectable agent in JetBrains AI
> Chat, adding setup, authentication, and slash-command detail that the
> same-day GitHub changelog (issue #1431) did not disclose.

## Source Context

- **Type**: blog-post (JetBrains AI blog, published Tue, 30 Jun 2026 13:15:31
  +0000; author Dominique Rolink; short product-announcement post, ~300 words
  of body content across three headed sections plus an intro sentence)
- **Author credibility**: JetBrains staff writer publishing on the official
  JetBrains AI blog, describing a feature JetBrains co-built with GitHub.
  Authoritative for: the JetBrains-side framing of the integration, the exact
  getting-started click path inside JetBrains IDEs, and the authentication
  requirements as JetBrains describes them to its own users. Not
  independently verified: no benchmark, screenshot, or technical
  architecture detail is given; this is a short marketing/announcement post,
  not a technical deep-dive, and it does not name which specific JetBrains
  IDEs or which Copilot models are supported.
- **Scope**: Covers the shift from ACP-Registry-based Copilot access to
  native agent-picker inclusion, the two slash commands (`/remote`,
  `/chronicle`) it says are now available in AI chat, OAuth-only
  authentication and the separate-subscription requirement, and the
  practitioner-facing getting-started steps. Does NOT cover: model
  selection/reasoning-depth details (documented instead in the same-day
  GitHub changelog, see Cross-References), the "run commands" agentic
  execution/permission model, a list of supported JetBrains IDEs, or any
  roadmap detail beyond a one-line reference to Microsoft Build.

## Extracted Claims

### Claim 1: The integration is framed by JetBrains as "born out of a deep partnership" that makes Copilot native in the agent picker, replacing the prior ACP-based access path
- **Evidence**: Opening summary sentence of the post, stated as the article's framing premise.
- **Confidence**: settled (direct statement of what the post is announcing)
- **Quote**: "Born out of a deep partnership between JetBrains and GitHub, this integration makes Copilot native in the agent picker and delivers a more stable agent experience directly in the IDE you already use every day."
- **Our assessment**: This is JetBrains' framing of the same launch documented from GitHub's side in `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 1 ("GitHub Copilot is a first-class option in the AI Assistant agent picker"). Both sources agree on the mechanical fact (Copilot is now natively selectable); this post adds the "deep partnership" framing and the explicit before/after contrast with ACP that the GitHub changelog states more tersely.

### Claim 2: Prior to this integration, Copilot was accessible in JetBrains via the "ACP Registry" — a named mechanism distinct from today's native agent-picker inclusion
- **Evidence**: Section heading "From ACP Registry to native experience" and its opening sentence, naming the prior access path explicitly.
- **Confidence**: settled (direct product-history statement from the vendor building the integration)
- **Quote**: "Copilot was previously accessible via the ACP Registry, but this integration takes things further."
- **Our assessment**: This is a more specific label than the GitHub changelog uses. `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` says Copilot "has also been available inside JetBrains AI Assistant through the Agent Client Protocol (ACP)" — naming the protocol but not an "ACP Registry" as a product surface. This post's related-posts footer links to a separate JetBrains post, "Cursor Joined the ACP Registry and Is Now Live in Your JetBrains IDE," confirming "ACP Registry" is JetBrains' name for a general-purpose, multi-vendor agent listing (Cursor is also a member), not a Copilot-specific integration path. For the guide: "ACP Registry" is the JetBrains-side product name for the pre-native integration mechanism; practitioners reading JetBrains documentation should expect this term rather than "Agent Client Protocol" alone.

### Claim 3: The new integration requires no setup or configuration via ACP — Copilot is described as available by default once the IDE is updated
- **Evidence**: Continuation of the same section, describing the practical effect of the "native" framing.
- **Confidence**: settled (direct product-behavior statement)
- **Quote**: "There's no need to set up or configure anything via ACP — Copilot is just there, ready to use."
- **Our assessment**: This directly fills a gap flagged in `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Extraction Note 3: "No setup/prerequisite information in the source [GitHub changelog]." This JetBrains post supplies the missing practitioner-facing detail — zero-configuration availability — that the GitHub changelog omitted. For the guide, this is the more actionable of the two sources for "what does a practitioner need to do to get this," even though it comes from the JetBrains side of the partnership rather than GitHub's.

### Claim 4: Copilot CLI slash commands `/remote` and `/chronicle` are available directly in JetBrains AI chat as part of this integration
- **Evidence**: Stated as part of the "core change" paragraph in the same section, naming two specific slash commands.
- **Confidence**: emerging (a specific, checkable product-behavior claim, but not corroborated by the same-day GitHub changelog, which only described the capability generically)
- **Quote**: "As part of the integration, Copilot CLI slash commands like /remote and /chronicle are also available directly in AI chat."
- **Our assessment**: This is genuinely novel detail relative to `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`, whose Claim 4 only says the integration supports "real coding tasks" ("Hand off multistep work and Copilot will reason through your project, propose changes, run commands, and iterate with you") without naming any slash command. `/remote` and `/chronicle` are the same commands already documented for the separate GitHub Copilot *plugin* surface in `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claims 2 and 4 respectively — remote session control and session-analysis/self-improvement subcommands). This post is the first source in the corpus to state that those same slash commands are reachable from the *AI Assistant* agent-picker surface, not just the Copilot plugin's own CLI agent surface. Practitioners should not assume the two surfaces have identical command availability without further confirmation — this claim covers only these two commands, not the full command set documented for the plugin surface (e.g., `/compact` is not mentioned here).

### Claim 5: JetBrains references a Microsoft Build announcement as the basis for a stated intent to continue delivering more GitHub Copilot × JetBrains experiences
- **Evidence**: Closing sentence of the "From ACP Registry to native experience" section.
- **Confidence**: anecdotal (forward-looking partnership statement, no specific roadmap items named)
- **Quote**: "As announced at Microsoft Build, we will continue to deliver more GitHub Copilot × JetBrains experiences through this partnership."
- **Our assessment**: This is vaguer than the GitHub changelog's roadmap, which named three concrete "What's next" items (NES support, Skills, deeper cross-tool orchestration — see `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claims 5–7). This post does not repeat those specifics; it only gestures at a Microsoft Build announcement as evidence of continued investment. Not independently actionable for the guide beyond corroborating that both companies frame this as an ongoing partnership rather than a one-off launch.

### Claim 6: Copilot in this integration authenticates exclusively via OAuth through the user's GitHub account
- **Evidence**: Opening sentence of the "Authentication: What you need to know" section.
- **Confidence**: settled (direct statement of authentication mechanism)
- **Quote**: "Copilot authenticates exclusively via OAuth through your GitHub account."
- **Our assessment**: This is authentication-model detail entirely absent from `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`, which does not mention authentication at all. This fills a real gap for practitioners evaluating the integration — it confirms Copilot access in this surface is tied to a GitHub identity, not a separate JetBrains-managed credential.

### Claim 7: A separate, active GitHub Copilot subscription is required to use this integration, and it is not included with a JetBrains AI subscription
- **Evidence**: "Separate subscription required" callout within the authentication section.
- **Confidence**: settled (explicit, unambiguous commercial-requirement statement)
- **Quote**: "Separate subscription required: JetBrains AI users will need an active GitHub Copilot subscription to use this integration. It is not included with your JetBrains AI subscription."
- **Our assessment**: This is a concrete, practitioner-relevant cost/entitlement detail with no equivalent in the GitHub changelog note. Teams already paying for JetBrains AI should not assume this integration is bundled — it requires a distinct, separately-billed GitHub Copilot subscription. For the guide, this is the kind of "who pays for what" detail that belongs in any tool-comparison table covering JetBrains AI Chat's agent options.

### Claim 8: A dedicated login flow and model picker are available for this integration, giving users control over which Copilot model to use, but this requires updating the IDE first
- **Evidence**: "Login and model picker" callout within the authentication section.
- **Confidence**: settled (direct statement of feature availability and its IDE-version precondition)
- **Quote**: "Login and model picker: A dedicated login flow and model picker will be available, giving you control over which Copilot model you use. Note you need to update your IDE to access this functionality."
- **Our assessment**: This corroborates `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 3 ("Choose between supported Copilot models and tune reasoning depth right in the AI chat") — both sources agree a model picker exists — but this post adds the practical precondition (IDE update required) that the GitHub changelog does not mention. Neither source names which specific Copilot models are selectable in this surface; that remains an open gap across both notes.

### Claim 9: Getting started requires opening AI chat, navigating to the agent picker menu, selecting GitHub Copilot, and completing an OAuth login prompt to connect a GitHub account
- **Evidence**: "Get started with Copilot in your IDE" section, describing the exact click path.
- **Confidence**: settled (direct step-by-step product instructions)
- **Quote**: "Open AI chat in your JetBrains IDE, navigate to the agent picker menu, and select GitHub Copilot. From there, follow the OAuth login prompt to connect your GitHub account."
- **Our assessment**: This is the concrete "how do I actually do this" detail entirely missing from `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`, whose Claim 2 only describes the mechanical result of selection ("Open the agent picker in the AI chat and select GitHub Copilot to make it the active agent for the conversation") without the OAuth step. This post's version is the more complete practitioner-facing setup path between the two sources.

### Claim 10: For users new to AI chat, the recommended entry point is the JetBrains AI widget in the IDE's top-right corner, which prompts installation of the AI Assistant plugin
- **Evidence**: Final sentence of the "Get started" section, describing the onboarding path for first-time users.
- **Confidence**: settled (direct onboarding instructions)
- **Quote**: "If you're new to the AI chat, open the JetBrains AI widget in the top-right corner of your IDE, click Let's Go, and follow the instructions to install the AI Assistant plugin."
- **Our assessment**: This confirms that "AI chat" in this post refers to the JetBrains AI Assistant product's chat surface, consistent with `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`'s framing of "JetBrains AI Assistant (JetBrains' own standalone AI product)" as the integration surface — not the separate GitHub Copilot plugin. This is useful confirmation for the guide that both sources are describing the same product surface, not two different ones.

## Concrete Artifacts

### Getting-started click path (JetBrains blog, June 30, 2026)

```
New to AI chat:
  1. Open the "JetBrains AI" widget (top-right corner of the IDE)
  2. Click "Let's Go"
  3. Follow instructions to install the AI Assistant plugin

Already using AI chat:
  1. Open AI chat
  2. Navigate to the agent picker menu
  3. Select "GitHub Copilot"
  4. Follow the OAuth login prompt to connect your GitHub account

Requirements:
  - Active GitHub Copilot subscription (separate from JetBrains AI subscription)
  - Updated IDE (required for dedicated login flow + model picker)
  - Authentication: OAuth via GitHub account only

Slash commands available directly in AI chat: /remote, /chronicle
```

*Source: "GitHub Copilot now an Integrated Agent in JetBrains IDEs," JetBrains AI blog, June 30, 2026 (Dominique Rolink).*

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`,
`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`,
`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, and
`blog-jetbrains-codex-recommended-agent.md` were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 1:
    both sources describe the same June 30, 2026 launch of GitHub Copilot as
    a native, first-class agent-picker option inside JetBrains AI Assistant's
    chat surface, upgrading it from a prior ACP-based integration.
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 2:
    both sources agree that selecting GitHub Copilot from the agent picker
    makes it the active agent for the chat/conversation.
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 3:
    both sources confirm a model picker/model-selection capability exists in
    this integration (this post's Claim 8 adds the IDE-update precondition).

- **Contradicts**: None identified. This post and
  `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` describe
  the same feature launch from two vendor perspectives (JetBrains and
  GitHub respectively) and agree on every point of factual overlap. No
  contradiction issue filed.

- **Extends**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`: this
    post fills three gaps that note's own Extraction Notes and Scope
    explicitly flagged as missing — setup/prerequisite steps (Claim 3, 9,
    10), an authentication model (Claims 6, 7, 8), and named slash commands
    reachable from this surface (Claim 4). The GitHub note's Concrete
    Artifacts "Product Map" explicitly stated "No settings path,
    prerequisite, or admin policy gate is given in this source for Surface
    2 [JetBrains AI Assistant]" — this post's Claims 3, 9, and 10 directly
    close that gap with concrete steps, though it still does not address
    the admin-policy-gate question for Business/Enterprise users that the
    GitHub note also left open.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claims 2,
    4): that note documents `/remote` and `/chronicle` as slash commands
    available within the separate GitHub Copilot *plugin's* own CLI agent
    sessions. This post's Claim 4 extends the reach of those same two
    commands to the JetBrains AI Assistant surface as well — the first
    corpus evidence that CLI-agent slash commands cross over into the
    AI-Assistant agent-picker surface.
  - `blog-jetbrains-codex-recommended-agent.md` (Claim 9): that note
    (published June 25, 2026, five days before this post, on the same
    JetBrains AI blog) documents the same JetBrains AI Chat agent-picker
    surface this post's Claims 9–10 describe, including a "recommended
    agent" default-selection feature that names Codex as the default while
    stating users "can switch to Junie, Claude Agent, or other ACP-compatible
    agents at any time" (that note's Claim 9). This post's Claim 2 establishes
    that Copilot was reachable through the general-purpose "ACP Registry"
    mechanism *before* this native launch — so Copilot was very plausibly
    already one of the "other ACP-compatible agents" that recommended-agent
    note refers to. Today's native, first-class picker inclusion (Claim 1)
    changes that relationship. Open questions this post does not answer, but
    that the connection surfaces for the guide: does the "recommended agent"
    default (Codex) still apply when a user selects GitHub Copilot, or does
    picking Copilot bypass the recommendation entirely? Does Copilot's new
    first-class status change whether it appears among, or ahead of, the
    ACP-Registry-reached agents in that picker? Neither is answerable from
    this source alone.

- **Novel**:
  - **"ACP Registry" as JetBrains' named term for the prior integration
    mechanism** (Claim 2): not previously named in the corpus; the GitHub
    changelog note only used "Agent Client Protocol (ACP)" without the
    "Registry" product name. The related-posts link confirming Cursor is
    also an "ACP Registry" member (per the post's own footer link title,
    "Cursor Joined the ACP Registry and Is Now Live in Your JetBrains IDE")
    establishes ACP Registry as a shared, multi-vendor listing mechanism,
    not a Copilot-specific one.
  - **Zero-configuration availability framing** (Claim 3): first corpus
    source to state explicitly that no ACP setup/configuration is needed for
    this integration.
  - **OAuth-exclusive authentication and separate-subscription requirement**
    (Claims 6, 7): first corpus documentation of the authentication and
    billing model for Copilot inside JetBrains AI Assistant specifically.
  - **Concrete getting-started click path** (Claims 9, 10): first corpus
    source with step-by-step onboarding instructions for this specific
    integration surface.

## Guide Impact

- **Chapter 01 (Daily Workflows — Tool Setup)**: Add the concrete
  getting-started path from Claims 9 and 10 (open AI chat → agent picker →
  select GitHub Copilot → OAuth login; or, for new users, JetBrains AI
  widget → "Let's Go" → install AI Assistant plugin) as the practitioner
  setup sequence for this integration. This is more actionable than the
  guide's current sourcing (`docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`),
  which has no setup steps at all.

- **Chapter 02 (Harness Engineering — Tool/Surface Selection, Cost)**: Add
  Claim 7 (separate, non-bundled GitHub Copilot subscription required,
  distinct from JetBrains AI subscription) to any cost/entitlement
  comparison table covering JetBrains AI Chat's agent options. Practitioners
  or teams already paying for JetBrains AI should not assume Copilot access
  is included.

- **Chapter 02 (Harness Engineering — Command/Feature Surface Parity)**: Add
  Claim 4 (`/remote` and `/chronicle` available directly in AI chat) as
  evidence that at least some Copilot-plugin CLI slash commands now cross
  over into the JetBrains AI Assistant agent-picker surface. Flag as an open
  question which other Copilot-plugin commands (e.g., `/compact`,
  documented for the plugin surface in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 3) are
  or are not available in AI Assistant — this post names only two commands,
  not a complete list.

## Extraction Notes

1. **WebFetch returned inconsistent quotes across two calls; raw HTML was
   fetched directly to resolve this**: a first WebFetch call returned an
   AI-summarized paraphrase (not quote-safe per MINER.md §2a). A second,
   more targeted WebFetch call returned quotes that did not fully match the
   first pass and could not be trusted as verbatim without independent
   verification. To resolve this, the raw HTML was fetched directly via
   `curl` and stripped of markup by hand; the resulting plain text (source
   body is short, ~300 words across three sections) was used as the sole
   basis for every `Quote` field in this note. All quotes above were copied
   character-for-character from that raw-text extraction, not from either
   WebFetch pass.
2. **Source is short**: the entire article body is approximately 300 words
   across an intro sentence and three headed sections ("From ACP Registry to
   native experience," "Authentication: What you need to know," "Get started
   with Copilot in your IDE"). Ten claims were extracted, representing
   essentially all substantive content in the post. No sub-pages were
   followed from the article itself; the related-posts footer link to
   "Cursor Joined the ACP Registry and Is Now Live in Your JetBrains IDE"
   was read only for its title/one-line description (used in Claim 2 and the
   Novel section) and was not separately mined as a full source — it is a
   candidate for its own source-submission issue if not already queued.
3. **No admin/policy-gate information given**: like the GitHub changelog
   covering the same launch, this post does not state whether a
   Business/Enterprise admin policy gate (e.g., "Editor preview features,"
   documented for the separate Copilot-plugin surface in multiple other
   corpus notes) applies to this AI Assistant integration. This gap persists
   across both sources describing this launch.
4. **No contradictions found**: this post agrees with
   `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` on every
   point of factual overlap; it only adds detail the GitHub changelog
   omitted. No contradiction issue filed.
