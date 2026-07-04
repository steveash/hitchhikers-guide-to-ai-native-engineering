---
source_url: https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available
source_type: docs
title: "Copilot vision is generally available"
author: GitHub (official changelog)
date_published: 2026-07-01
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: settled
issue: "#1506"
---

# Copilot vision is generally available

> GitHub's July 1, 2026 changelog announcing general availability of Copilot
> vision — direct image (JPEG, PNG, GIF, WebP) and PDF attachment to chat
> prompts across VS Code, github.com, and the Copilot CLI, for all Copilot
> plan tiers including Free, with the Business/Enterprise "Editor Preview
> Features" admin gate removed and a ~24-hour attachment retention window
> disclosed for Business/Enterprise.

## Source Context

- **Type**: docs (GitHub official product changelog, July 1, 2026; approximately
  100 words of primary announcement text, "1 minute read")
- **Author credibility**: GitHub engineering team announcing a production GA
  release. Authoritative for: the fact that Copilot vision is GA, the
  supported file types, the three named surfaces it works on, plan-tier
  availability, the removal of the prior admin policy gate, and the stated
  attachment retention window for Business/Enterprise. Not a credible source
  for: model/architecture detail on how images or PDFs are processed,
  benchmark or accuracy data for visual reasoning, retention behavior for
  Free/Pro/Pro+ tiers (only Business/Enterprise retention is stated), or
  whether this GA follows a documented preview period (no prior "Copilot
  vision" preview announcement was found elsewhere in the corpus).
- **Scope**: Covers file-type support, the three interaction surfaces (VS
  Code Copilot Chat, github.com Copilot Chat, Copilot CLI), plan-tier
  availability, the admin-policy-gate removal, and Business/Enterprise
  attachment retention. Does NOT cover: which Copilot models process the
  images/PDFs, accuracy or reliability of visual reasoning, file size or
  page-count limits, whether vision works in the Copilot cloud agent (CCA) or
  JetBrains/other IDE surfaces, or retention terms for non-Business/Enterprise
  plans.

## Extracted Claims

### Claim 1: Copilot vision — attaching images and PDFs to chat prompts so Copilot can reason about them alongside code — is now generally available

- **Evidence**: Opening statement of the changelog announcing GA status for the
  capability.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Copilot vision is now generally available. You can attach images
  and PDFs directly to your chat prompts so Copilot can reason about what it
  sees alongside your code."
- **Our assessment**: This is the first corpus documentation of GitHub
  Copilot's multimodal image/PDF input capability as a named, generally
  available feature. No prior corpus source (including the Prospector's
  cross-check) documents an earlier "Copilot vision" preview, so the GA
  announcement is the corpus's introduction to this capability, not a
  promotion the corpus can trace from a prior state. For practitioners, the
  framing "alongside your code" signals the intended use case is combining a
  visual artifact (screenshot, diagram, scanned doc) with the existing code
  context already available to Copilot chat — not vision as a standalone
  capability.

### Claim 2: Copilot vision accepts four image formats (JPEG, PNG, GIF, WebP) and PDF documents as attachable file types

- **Evidence**: "Supported file types" table in the changelog, listing exact
  file extensions grouped under "Images" and "Documents."
- **Confidence**: settled (explicit file-type table in official changelog)
- **Quote**: "JPEG (.jpg, .jpeg), PNG (.png), GIF (.gif), WebP (.webp)" (Images
  row); "PDF (.pdf)" (Documents row)
- **Our assessment**: The four-format image list plus PDF is a fairly broad
  but not exhaustive set — notably it does not include SVG, HEIC, or BMP.
  Practitioners with screenshots or diagrams in unsupported formats (e.g.,
  SVG diagrams exported from design tools) would need to convert before
  attaching. The inclusion of PDF alongside raster images is notable: it
  extends the use case beyond screenshots to scanned documents, design specs,
  or exported reports being reasoned about directly in a chat prompt.

### Claim 3: Copilot vision works across three surfaces — VS Code Copilot Chat, github.com Copilot Chat, and the Copilot CLI — with VS Code explicitly supporting all three chat modes (ask, plan, agent)

- **Evidence**: "Where it works" table in the changelog, with a distinct
  attachment mechanism and mode-scope note per surface.
- **Confidence**: settled (explicit surface table in official changelog)
- **Quote**: "Paste, drag-and-drop, or right-click to attach images in the
  chat panel; works in ask, plan, and agent modes" (VS Code row)
- **Our assessment**: The explicit statement that vision "works in ask, plan,
  and agent modes" in VS Code is the most operationally significant detail
  in the table — it means an autonomous or semi-autonomous agent-mode session
  can receive an attached image or PDF as part of its working context, not
  just interactive Q&A. This is directly relevant to visual verification and
  screenshot-based debugging workflows: a practitioner running Copilot in
  agent mode could, in principle, attach a screenshot of a UI bug or a failed
  test's rendered output as part of the task instruction. The changelog does
  not describe *how* an agent-mode session would attach an image mid-run
  (e.g., whether the agent itself can request or capture a screenshot, versus
  only the human attaching one at prompt time) — this remains an open
  question for harness design.

### Claim 4: Copilot vision is available to all Copilot subscription tiers — Free, Pro, Pro+, Business, and Enterprise — with no policy changes or admin action required

- **Evidence**: "Available on all Copilot plans" section of the changelog,
  naming all five plan tiers explicitly.
- **Confidence**: settled (plan availability stated explicitly in official
  changelog)
- **Quote**: "Copilot vision is now available to all Copilot subscribers:
  Free, Pro, Pro+, Business, and Enterprise. No policy changes or admin
  actions are required to turn it on."
- **Our assessment**: Universal, non-gated availability (including the Free
  tier) is notable given how many other Copilot feature GA announcements in
  the corpus are Business/Enterprise-gated or require explicit admin
  enablement even at GA (e.g., Sonnet 5 GA still requires Business/Enterprise
  admins to enable the model via policy settings, per
  `docs-github-copilot-sonnet5-ga.md` Claim 8). Vision's zero-friction rollout
  suggests GitHub is treating it as a low-risk UI/input-modality feature
  rather than a compute- or model-access feature requiring governance
  controls.

### Claim 5: Vision was previously gated behind the "Editor Preview Features" policy for Business and Enterprise users at the org or enterprise level; that gate has now been removed and vision is on by default for everyone

- **Evidence**: "Available on all Copilot plans" section, describing the
  prior admin-gated state and its removal.
- **Confidence**: settled (policy-removal stated definitively in official
  changelog)
- **Quote**: "Previously, users on Copilot Business and Copilot Enterprise
  needed the Editor Preview Features policy enabled at the org or enterprise
  level. Vision is now on by default for everyone."
- **Our assessment**: This is the same "Editor Preview Features" admin gate
  documented repeatedly elsewhere in the corpus for other Copilot features
  reaching GA (see Cross-References) — removing that gate at GA time is a
  recurring GitHub release pattern, not unique to vision. For teams that
  previously had an administrator explicitly enable Editor Preview Features
  specifically to unlock vision (or another gated feature bundled under the
  same policy), this GA promotion means the policy toggle is no longer the
  operative control for vision access — though the policy may still gate
  other still-preview features bundled under the same name, a nuance this
  changelog does not address.

### Claim 6: For Copilot Business and Enterprise users, GitHub retains image and PDF attachments for approximately 24 hours to provide the vision service

- **Evidence**: Final sentence of the "Available on all Copilot plans"
  section, a standalone data-handling disclosure scoped explicitly to
  Business and Enterprise.
- **Confidence**: settled (explicit retention window stated in official
  changelog)
- **Quote**: "For users on GitHub Copilot Business and GitHub Copilot
  Enterprise, GitHub retains image and PDF attachments for approximately 24
  hours to provide the service."
- **Our assessment**: This is a concrete, compliance-relevant detail for
  Business/Enterprise teams evaluating vision for use with sensitive visual
  content (e.g., screenshots containing customer data, internal architecture
  diagrams, or scanned confidential documents). The changelog scopes this
  disclosure only to Business/Enterprise — it does not state a retention
  policy for Free, Pro, or Pro+ attachments, leaving an open question for
  individual-tier practitioners about how long their attached images/PDFs are
  stored. This is a distinct data-handling disclosure from the Zero Data
  Retention (ZDR) claim documented for Claude Sonnet 5 in Copilot
  (`docs-github-copilot-sonnet5-ga.md` Claim 9) — ZDR concerns whether a
  model provider retains conversation data for training, while this 24-hour
  window concerns how long GitHub itself stores the uploaded attachment
  blobs to serve the feature. The two are complementary, not overlapping,
  data-handling disclosures for Copilot practitioners assembling a full data
  governance picture.

## Concrete Artifacts

### Verbatim Text of Source Changelog (July 1, 2026)

```
Title: Copilot vision is generally available
Release: July 1, 2026 · 1 minute read
Label: copilot

Copilot vision is now generally available. You can attach images and PDFs
directly to your chat prompts so Copilot can reason about what it sees
alongside your code.

Supported file types
  Type       | Formats
  Images     | JPEG (.jpg, .jpeg), PNG (.png), GIF (.gif), WebP (.webp)
  Documents  | PDF (.pdf)

Where it works
  Copilot vision is available across the following surfaces:
  Surface                       | Notes
  GitHub Copilot Chat in VS Code| Paste, drag-and-drop, or right-click to
                                 | attach images in the chat panel; works in
                                 | ask, plan, and agent modes
  github.com Copilot Chat       | Attach images and PDFs directly in chat on
                                 | github.com
  GitHub Copilot CLI            | Attach image paths when using Copilot in
                                 | the terminal

Available on all Copilot plans
  Copilot vision is now available to all Copilot subscribers: Free, Pro,
  Pro+, Business, and Enterprise. No policy changes or admin actions are
  required to turn it on.

  Previously, users on Copilot Business and Copilot Enterprise needed the
  Editor Preview Features policy enabled at the org or enterprise level.
  Vision is now on by default for everyone.

  For users on GitHub Copilot Business and GitHub Copilot Enterprise, GitHub
  retains image and PDF attachments for approximately 24 hours to provide
  the service.
```

Source: https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available
Retrieved: 2026-07-04, via direct `curl` fetch of the raw article HTML
(cross-checked against two independent WebFetch passes; all three fetches
agreed on content).

### Feature Summary: Copilot Vision GA (July 1, 2026)

```
Feature: Copilot vision (image/PDF attachment + reasoning)
Published: 2026-07-01
Availability: All Copilot plans (Free, Pro, Pro+, Business, Enterprise) —
              no admin action required

Supported inputs:
  Images:    JPEG, PNG, GIF, WebP
  Documents: PDF

Surfaces:
  VS Code Copilot Chat  — paste / drag-drop / right-click; ask, plan, agent modes
  github.com Copilot Chat — attach directly in chat
  Copilot CLI            — attach image paths in the terminal

Admin gate history:
  Before: Business/Enterprise required "Editor Preview Features" policy
          enabled at org/enterprise level
  After:  On by default for everyone, no policy action required

Data retention (Business/Enterprise only):
  Image and PDF attachments retained ~24 hours to provide the service
  (Free/Pro/Pro+ retention not stated)
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`,
`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`,
`docs-github-copilot-jetbrains-cli-agent-sessions.md`, and
`docs-github-copilot-sonnet5-ga.md` were re-read directly in those notes
before citing (per MINER.md §4b); claim numbers are counted top-to-bottom in
document order as they appear in each cited note.

- **Corroborates**: None found for the vision capability itself — the
  Prospector's triage confirmed no existing source note documents Copilot
  vision, and no other corpus note independently corroborates image/PDF
  input for Copilot chat.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Copilot vision, image/PDF attachment, or contradicts the stated
  plan-tier availability, surface list, or retention window. No contradiction
  issue filed.

- **Extends**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim
    8 ("Cloud agent has reached general availability, no longer requiring
    the Editor Preview feature flag in JetBrains"): both sources document
    the same recurring GitHub release pattern — a feature ships gated behind
    the "Editor Preview Features" policy for Business/Enterprise, then has
    that gate removed at GA. This note's Claim 5 is a second, independent
    instance of the same pattern applied to vision rather than cloud agent.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 10
    ("BYOK ... is now available without the Editor Preview feature flag in
    JetBrains, with Business and Enterprise availability controlled by
    GitHub policy"): a third independent instance of the same gate-removal-
    at-GA pattern, this time for BYOK. Together with this note's Claim 5 and
    the cloud-agent instance above, the corpus now documents three separate
    features (cloud agent, BYOK, vision) following the identical GA-promotion
    shape of removing the "Editor Preview Features" bundled policy gate —
    strong evidence this is a standing GitHub release convention rather than
    a one-off decision for any single feature.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 4 ("Copilot
    Business and Enterprise users must have the 'Editor preview features'
    policy enabled by an administrator before they can use the CLI agent in
    JetBrains"): documents the *pre-GA* gated state for a different feature
    (CLI agent in JetBrains), which is the same shape of restriction this
    note's Claim 5 describes vision as having had before its own GA.
  - `docs-github-copilot-sonnet5-ga.md` Claim 9 ("Claude Sonnet 5 operates
    under Zero Data Retention (ZDR) in GitHub Copilot"): both this note's
    Claim 6 and that claim are Copilot data-handling disclosures, but for
    different layers — ZDR is a model-provider training-data guarantee,
    while this note's ~24-hour attachment retention is GitHub's own storage
    window for uploaded files. Practitioners assembling a full Copilot data
    governance picture need both: which models retain conversation data
    (ZDR, per-model) and how long GitHub stores uploaded artifacts
    (attachment retention, per-feature).

- **Novel**:
  - **Copilot vision as a named, generally available multimodal input
    capability**: no prior corpus source documents image or PDF attachment
    to GitHub Copilot chat prompts on any surface.
  - **Vision support in VS Code agent mode specifically**: the explicit
    statement that vision "works in ask, plan, and agent modes" is the first
    corpus documentation of an attached visual artifact being available to
    an agentic (not just interactive Q&A) Copilot session — directly
    relevant to visual verification / screenshot-based debugging workflow
    design.
  - **Free-tier inclusion for a GA multimodal feature**: unlike several other
    Copilot GA announcements in the corpus that remain Business/Enterprise-
    gated or admin-enabled even at GA (e.g., Sonnet 5 model policy
    enablement), vision ships to Free-tier users with zero admin friction.
  - **Attachment-specific data retention window (~24 hours, Business/
    Enterprise)**: distinct from, and not previously documented alongside,
    the model-level ZDR disclosures elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — visual verification / screenshot-based
  workflows)**: Add Copilot vision as a documented capability practitioners
  can use for screenshot-based debugging and visual QA within VS Code and
  the CLI. Flag the open question this source leaves unanswered: the
  changelog does not specify how an agent-mode session acquires an image
  mid-task (human-attached at prompt time vs. agent-captured), which matters
  for designing an automated visual-verification loop versus a human-in-
  the-loop screenshot review step.

- **Chapter 02 (Harness Engineering — admin governance patterns)**: Add this
  as a third corroborating instance (alongside cloud agent GA and BYOK GA in
  the JetBrains notes) of GitHub's recurring "ship gated behind Editor
  Preview Features, remove the gate at GA" release pattern. Practitioners
  building internal rollout playbooks for GitHub Copilot features can expect
  this shape by default and should track the Editor Preview Features policy
  as a temporary, not permanent, gate.

- **Chapter 03 (Verification — visual QA)**: Add Copilot vision (image/PDF
  attachment across VS Code, github.com, and CLI) as a candidate mechanism
  for incorporating visual evidence (rendered UI screenshots, diagrams,
  scanned specs) directly into a Copilot-driven verification workflow. Note
  the format limitation (no SVG, HEIC, or BMP) as a practical constraint for
  teams whose screenshot tooling defaults to an unsupported format.

- **Chapter 05 (Team Adoption — data governance)**: Add the ~24-hour
  Business/Enterprise attachment retention disclosure (Claim 6) to any team
  adoption checklist covering Copilot data-handling review, alongside the
  existing Sonnet-5 ZDR disclosure — flagging that the retention window is
  documented only for Business/Enterprise, not Free/Pro/Pro+.

## Extraction Notes

1. **Source is very short (~100 words, "1 minute read")**: this is among the
   shortest sources in the corpus. Six claims were extracted, representing
   essentially all substantive content in the announcement (opening GA
   statement, file-type table, surface table, plan availability, gate
   removal, and retention disclosure). This is consistent with the corpus's
   established pattern for brief changelog entries (compare
   `docs-github-copilot-web-contextual-chat.md`, ~150 words → 7 claims).
2. **Verbatim quotes verified via raw HTML, not WebFetch alone**: two
   independent WebFetch passes were run first and returned mutually
   consistent paraphrases, but per MINER.md §2a a WebFetch summary is not
   treated as quote-safe on its own. The raw article HTML was fetched
   directly via `curl` (following the redirect from the bare changelog slug
   to its trailing-slash canonical URL) and the `<article>` element was
   parsed by hand to recover exact table cell text and paragraph wording.
   All `Quote` fields above are copied character-for-character from that raw
   extraction, not from either WebFetch pass.
3. **No linked sub-pages to follow**: the article body contains no outbound
   links other than same-page anchor links (table of contents), the
   `copilot` label-filtered changelog listing, and generic site-navigation
   links (docs.github.com homepage, other unrelated changelog entries, site
   footer). None of these are substantive sub-pages specific to Copilot
   vision, so no follow-up pages were fetched.
4. **No prior "Copilot vision" preview found in the corpus**: this changelog
   announces GA directly; it does not reference an earlier preview
   announcement, and a corpus search for "vision" combined with Copilot
   context found no earlier source note describing a preview stage. If a
   preview announcement exists and is later submitted as its own source, it
   would predate this note chronologically despite being mined afterward.
5. **No contradictions found**: checked the corpus broadly for prior claims
   about Copilot image/PDF input, admin gating of vision specifically, or
   attachment retention: none exist. No contradiction issue filed.
