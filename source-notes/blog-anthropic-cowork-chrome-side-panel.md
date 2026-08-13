---
source_url: https://claude.com/blog/cowork-chrome-side-panel
source_type: blog-post
title: "The Claude in Chrome side panel is now Claude Cowork"
author: Anthropic (Claude.com blog)
date_published: 2026-08-12
date_extracted: 2026-08-13
last_checked: 2026-08-13
status: current
confidence_overall: emerging
issue: "#2669"
---

# The Claude in Chrome side panel is now Claude Cowork

> Anthropic's product announcement merging the Claude in Chrome browser extension's
> side panel into the same Cowork session used on desktop, web, and mobile —
> making browser-driven work (vendor portals, legacy systems, internal dashboards)
> a portable, resumable Cowork surface rather than an isolated one, alongside an
> updated prompt-injection mitigation ("automatically approve" plus a pre-action
> consistency check) and admin domain-restriction controls for Enterprise.

## Source Context

- **Type**: blog-post (first-party Anthropic product announcement, claude.com,
  August 12, 2026)
- **Author credibility**: Unbylined first-party Anthropic post on the official
  product blog. Authoritative on stated capabilities, plan availability, and
  the intended safety architecture; as vendor communication, self-reported
  claims about risk reduction ("meaningfully reduce the risk") should be read
  as directional rather than independently verified. The article links out to
  a separate Anthropic support-site safety guide
  (support.claude.com/en/articles/12902428-use-claude-in-chrome-safely), which
  was also read for this note and provides more specific, testable claims
  (e.g., a numeric attack-success-rate figure).
- **Scope**: Covers the merge of the Claude in Chrome side panel into Claude
  Cowork sessions, cross-surface session continuity (browser → desktop/web/
  mobile), plan availability (Max/Team now, Pro rolling out), the "automatically
  approve" vs. per-step permission model, a pre-action consistency check against
  the original request, admin controls (off by default on Enterprise, domain
  allow-listing), and product limitations (no local file access from the
  browser, no other Chromium browsers, no mobile). Does NOT cover: pricing,
  token/cost characteristics of the merged session, technical detail on how
  the "action against what you originally asked for" check is implemented,
  or a quantified before/after security metric in the blog post itself (the
  0.08% figure comes from the linked safety guide, not the announcement).

## Extracted Claims

### Claim 1: The Chrome side panel now runs the same Claude Cowork session used on desktop, web, and mobile, rather than an isolated browser-only session

- **Evidence**: Direct product-architecture statement in the opening paragraph,
  contrasted explicitly with the prior (pilot-era) behavior where the side
  panel was a separate session.
- **Confidence**: settled (first-party statement of shipped architecture change)
- **Quote**: "Until now, a session in the side panel was separate from those in
  the Claude apps, so context and conversations didn't carry between them. Now,
  the side panel runs the same Claude Cowork session you use on desktop, web,
  and mobile for longer, multi-step work."
- **Our assessment**: This is the core claim of the post and a meaningful
  architecture change, not just a UI update. It converts the browser extension
  from a standalone tool into one more entry point into a single persistent
  Cowork session tied to the user's account rather than a device. For the
  guide, this reframes "Claude in Chrome" from a separate capability
  (documented alongside computer use in `blog-anthropic-dispatch-computer-use.md`)
  into a Cowork access surface — practitioners already using Cowork on desktop
  gain browser automation "for free" rather than needing to learn a separate tool.

### Claim 2: A task started in the browser side panel can be resumed and extended on another Claude surface, including adding local files unavailable to the browser

- **Evidence**: Concrete worked example: collecting vendor-portal invoice data
  in Chrome, then continuing the same session in the desktop app to add local
  files or import a budget file.
- **Confidence**: emerging (single illustrative example in a marketing post, not
  a measured workflow benchmark)
- **Quote**: "Then, you can pick the session up in the desktop app to add files
  from your computer, or import last month's budget and ask what's changed,
  allowing you to maintain context across surfaces as you work."
- **Our assessment**: This example directly demonstrates why cross-surface
  continuity matters: the browser and desktop app have non-overlapping
  capabilities (browser can act inside web-only vendor portals; desktop can
  access local files), so the practical value is combining both within one
  session rather than either surface alone. This is the clearest illustration
  in the post of the "start anywhere, finish anywhere" pattern and is concrete
  enough to cite directly in the guide as a canonical Cowork example.

### Claim 3: Claude in Chrome exists specifically to bridge tools that don't have direct Claude integrations — internal dashboards, legacy systems, and vendor portals

- **Evidence**: Direct statement of the extension's purpose, contrasted with
  tools that already "connect directly to Claude."
- **Confidence**: settled (first-party statement of product rationale)
- **Quote**: "Many of the tools you use every day connect directly to Claude,
  but others don't, such as internal dashboards, legacy systems, and vendor
  portals. With Claude in Chrome, Claude can work in these apps through the
  browser."
- **Our assessment**: This confirms the connector-first, browser-as-fallback
  hierarchy already documented from the March 2026 computer-use announcement
  (`blog-anthropic-dispatch-computer-use.md` Claim 1: "Claude will reach for
  the most precise tool first, starting with connectors... When there isn't a
  connector, Claude can directly control your browser"). The Chrome side panel
  is the concrete product surface for that fallback tier when the target is a
  web application specifically (as opposed to a native desktop app, which
  computer use handles separately). No new hierarchy claim here — this is
  corroboration, not novelty.

### Claim 4: Anthropic has added a pre-action consistency check that blocks any consequential action not matching the user's original request, layered on top of the existing "automatically approve" permission mode

- **Evidence**: Direct description of a safety mechanism added "since the
  pilot" — distinct from and in addition to the permission-mode toggle.
- **Confidence**: emerging (first-party description of an internal safety
  mechanism; no technical detail on implementation, no independently measured
  false-negative/false-positive rate given in the announcement itself)
- **Quote**: "Before anything consequential, like submitting a form, sending a
  message, or downloading a file, a separate check reviews the action against
  what you originally asked for and blocks anything that doesn't match. That
  creates fewer interruptions while maintaining oversight."
- **Our assessment**: This is the most novel security claim in the post and is
  a specific, checkable mechanism distinct from the two previously documented
  layers: (1) the activation-level prompt-injection classifier described in
  `blog-anthropic-dispatch-computer-use.md` Claim 3 and confirmed in
  `blog-anthropic-computer-use-best-practices.md` Claim 7 (`computer_20251124`
  tool type), and (2) the permission-mode toggle. This "intent consistency
  check" is a third, narrower layer that runs specifically before consequential
  actions and compares the proposed action to the stated goal — a defense
  against prompt injection that redirects Claude toward an action a user
  would not have asked for, even if that action isn't independently
  classified as malicious. The framing ("fewer interruptions while maintaining
  oversight") suggests this check is partly a UX lever to make "automatically
  approve" safer to use as a default, not purely a security hardening. Because
  no benchmark accompanies this specific check, we treat the risk-reduction
  claim as directional pending independent testing.

### Claim 5: Claude still requires explicit approval for certain irreversible or high-stakes actions regardless of permission mode, such as making a purchase or sharing personal data

- **Evidence**: Direct statement of a hard-coded approval gate that is not
  overridden by "automatically approve."
- **Confidence**: settled (first-party statement of a named restriction)
- **Quote**: "Claude still asks before certain irreversible or costly actions,
  like making a purchase or sharing personal data."
- **Our assessment**: This corroborates the "four behavioral best practices"
  from `blog-anthropic-computer-use-best-practices.md` Claim 8, specifically
  "pause and request user confirmation before performing irreversible actions."
  The Chrome-specific detail (purchases, personal-data sharing named explicitly)
  is more concrete than the general best-practices post and is worth citing
  directly when discussing what "automatically approve" does and does not cover.

### Claim 6: Prompt injection risk cannot be eliminated, only reduced, and Anthropic frames its mitigation as an ongoing arms race rather than a solved problem

- **Evidence**: Explicit hedge immediately following the description of the
  safety mechanisms.
- **Confidence**: settled (first-party admission of a limitation, which
  increases rather than decreases credibility of the surrounding safety claims)
- **Quote**: "While these measures meaningfully reduce the risk, they cannot
  eliminate it. Prompt injection is a moving target, so Anthropic continues
  hunting for new attacks and building what they learn into each model they
  release."
- **Our assessment**: This is a candid first-party admission that browser-agent
  prompt injection remains unsolved as of August 2026, consistent with the
  broader corpus position (see `blog-simonwillison-prompt-injection-role-confusion.md`
  and the file-exfiltration failure report below). The guide should not present
  Claude in Chrome's safety measures as eliminating browser-agent risk — the
  source itself declines to make that claim.

### Claim 7: Anthropic's explicit safety recommendation is to start Claude in Chrome usage on trusted sites, deferring detailed practices to a separate safety guide

- **Evidence**: Direct recommendation quoted in the "Understanding the Risks"
  section, with a link to a dedicated safety guide.
- **Confidence**: settled (first-party recommendation)
- **Quote**: "We recommend starting on sites you trust, and our safety guide has
  more best practices."
- **Our assessment**: The linked safety guide (support.claude.com/en/articles/
  12902428) is substantially more specific than the announcement post and was
  read in full for this note (see Concrete Artifacts). It names a measured
  attack-success rate, explicit blocked-activity and blocked-site lists, and
  concrete best practices (separate browser profiles for sensitive accounts,
  avoiding financial/legal/medical data). The guide is a distinct, citable
  document, not just a link — the guide chapter on browser-agent risk should
  cite it directly rather than only the announcement post.

### Claim 8: Testing shows the current Claude in Chrome configuration reduces prompt-injection attack success to under 0.08% against a combined set of known effective attack techniques

- **Evidence**: Specific numeric claim from the linked safety guide (not the
  announcement post itself).
- **Confidence**: emerging (first-party benchmark; methodology — "internal
  testing combining known effective techniques" — is not published in enough
  detail to assess technique coverage or reproducibility, and the figure
  is against known techniques, explicitly not novel/future attacks)
- **Quote**: "Testing indicates current configuration reduces prompt injection
  attack success rates to less than 0.08% against internal testing combining
  known effective techniques."
- **Our assessment**: This is the single most citable, specific security metric
  in this note. It should be attributed carefully: it is an internal Anthropic
  benchmark against known attack techniques, not an independent red-team result,
  and it explicitly does not cover novel attacks (Claim 6 above already concedes
  this). Still, a quantified figure is more useful to practitioners than the
  qualitative "meaningfully reduce the risk" language in the announcement post,
  and it is new to the corpus — no existing source note has a specific
  attack-success-rate number for Claude's browser agent.

### Claim 9: Claude in Chrome is off by default on Enterprise plans, and admins can enable it restricted to an approved-domain allowlist

- **Evidence**: Direct statement of the default Enterprise configuration and
  the specific admin control available.
- **Confidence**: settled (first-party statement of a named admin control)
- **Quote**: "On Enterprise plans, Claude in Chrome is off by default. Admins
  can turn it on and limit it to approved domains."
- **Our assessment**: This is a concrete, actionable governance control for
  admins deploying Cowork/Claude in Chrome in an organization — domain
  allow-listing is a coarser but simpler control than the per-user "automatically
  approve" toggle, and it operates at the account/org level rather than the
  session level. For a guide chapter on enterprise governance of agentic
  browser tools, this is a specific control to name alongside the plan-tier
  gating (Claim 10).

### Claim 10: Claude in Chrome's new Cowork-integrated side panel is available today on Max and Team plans, rolling out to Pro over "the coming weeks," and is not available on other Chromium browsers or on mobile

- **Evidence**: Explicit plan-availability and platform-limitation statements,
  stated twice in the post (once in the lede, once in "Getting Started").
- **Confidence**: settled (first-party statement of shipped availability as of
  publication date)
- **Quote**: "It's available on Max and Team plans today, and is rolling out to
  Pro users over the coming weeks."; "Claude in Chrome doesn't run on other
  Chromium browsers or on mobile yet."
- **Our assessment**: Practical detail for practitioners deciding when to
  adopt: this is a partial, tiered rollout as of August 12, 2026, not a
  universal release. The Chromium-only, no-mobile limitation is also a real
  constraint worth naming — teams standardized on Edge, Brave, or Arc (all
  Chromium-based but not Chrome) cannot currently use this, despite being
  technically Chromium browsers.

## Concrete Artifacts

```
Claude in Chrome — safety architecture summary
(from the announcement post, claude.com/blog/cowork-chrome-side-panel,
and the linked safety guide, support.claude.com/en/articles/12902428)

Layer 1 — Model-level: RL training to recognize malicious instructions +
          content classifiers scanning untrusted material (per safety guide)
Layer 2 — Action-level: "automatically approve" mode screens Claude's own
          actions automatically; users can switch to "Manually approve"
          for step-by-step oversight (per safety guide)
Layer 3 — Consequential-action check: before submitting a form, sending a
          message, or downloading a file, a check compares the proposed
          action against the user's original request and blocks mismatches
          (per announcement post)
Layer 4 — Hard-coded approval gate: certain irreversible/costly actions
          (purchases, sharing personal data) always require explicit
          approval regardless of mode (per announcement post)
Layer 5 — Site/activity restrictions: blocked from stock trading, captcha
          bypass, sensitive data entry, facial image gathering; blocked
          from adult content and pirated-material sites (per safety guide)
Layer 6 — Admin/org-level: off by default on Enterprise; admins can enable
          and restrict to an approved-domain allowlist (per announcement post)

Measured result (per safety guide, not the announcement post):
  <0.08% attack success rate in internal testing combining known
  effective prompt-injection techniques.
```

```
Claude in Chrome — plan availability and platform limits
(from the announcement post)

- Max plan: available now
- Team plan: available now
- Pro plan: rolling out "over the coming weeks" (as of Aug 12, 2026)
- Enterprise: off by default; admin-enabled, domain-restrictable
- Platform: Chrome only — "doesn't run on other Chromium browsers"
- Device: desktop browser only — "doesn't run on... mobile yet"
- Local files: side panel cannot access files on your computer;
  desktop app still required for that
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-dispatch-computer-use.md` Claim 1 (connector-first,
    computer-use-as-fallback hierarchy): this post's framing of Claude in
    Chrome as filling the gap for "internal dashboards, legacy systems, and
    vendor portals" (Claim 3 above) is the browser-specific instance of the
    same hierarchy — connectors first, browser automation for tools without one.
  - `blog-anthropic-dispatch-computer-use.md` Claim 3 (three-safeguard safety
    model: consent gating, injection scanning, denylist) and
    `blog-anthropic-computer-use-best-practices.md` Claim 7 (`computer_20251124`
    tool type ships an automatic injection classifier) and Claim 8 (pause
    before irreversible actions is a named best practice): this post confirms
    those layers are still active for Claude in Chrome specifically and adds
    a new layer on top (Claim 4, the pre-action consistency check) not
    previously documented for any Claude surface.
  - `blog-simonwillison-prompt-injection-role-confusion.md` (general position
    that prompt injection defenses are probabilistic, not a solved problem):
    corroborated directly by this post's own hedge in Claim 6 ("cannot
    eliminate it... a moving target").

- **Contradicts**: None identified. No existing source note claims Claude's
  browser-agent prompt injection defenses are complete or that Claude in
  Chrome was previously part of a unified Cowork session — this post's claims
  extend rather than conflict with the corpus.

- **Extends**:
  - `blog-anthropic-cowork-getting-started.md` (individual practitioner
    onboarding guidance for Cowork on desktop/web): this post extends that
    guidance to a new access surface (Chrome side panel) without changing the
    underlying task-selection heuristics (the five-ingredient checklist still
    applies; only the entry point changes).
  - `blog-anthropic-cowork-deploy-guide.md` and `blog-anthropic-cowork-enterprise.md`
    (enterprise deployment and governance framework for Cowork): this post
    adds a concrete new governance lever specific to the browser surface —
    domain allow-listing (Claim 9) — that deployment-planning chapters should
    include alongside whatever controls those notes already document.
  - `failure-copilot-cowork-file-exfiltration.md` (Microsoft Copilot Cowork
    file-exfiltration failure via unapproved agent email + external image
    rendering + pre-authenticated links): that failure report is a concrete
    demonstration of exactly the risk category this post's safety
    architecture (Claim 4, Claim 5) is designed to prevent — an agent taking
    a consequential, data-exposing action (sending an email, generating a
    download link) that a user did not ask for. The guide's risk-management
    chapter should pair these two notes: the failure report shows what goes
    wrong when a competing product lacks an equivalent to Anthropic's
    pre-action consistency check (no approval gate on agent→inbox email in
    the Copilot Cowork case); this post shows Anthropic's stated mitigation
    for the same class of failure. This is not a contradiction (different
    products, no direct claim conflict) but a directly relevant risk/mitigation
    pairing worth citing together.

- **Novel** (not in prior corpus):
  - **Cross-surface Cowork session continuity via the browser** (Claim 1,
    Claim 2): no existing source note documents that a Claude Cowork session
    can start in a browser extension and be resumed in the desktop/web/mobile
    apps with shared context. Previously, Claude in Chrome was documented
    (in `blog-anthropic-dispatch-computer-use.md`) as a computer-use-adjacent,
    session-isolated capability.
  - **Pre-action consistency check against original intent** (Claim 4): this
    specific "does the action match what the user originally asked for" gate,
    distinct from the injection classifier and from the permission-mode
    toggle, is a new safety-architecture detail not present in any prior
    computer-use or Cowork source note.
  - **Numeric attack-success-rate figure** (Claim 8, <0.08%): the first
    quantified prompt-injection defense metric for a Claude browser/computer-use
    surface in the corpus.
  - **Domain-allowlist admin control for Claude in Chrome** (Claim 9): new
    enterprise governance detail specific to the browser extension, distinct
    from the app-denylist mechanism previously documented for general
    computer use.

## Guide Impact

- **Chapter on Cowork / multi-surface agent work**: Add Claim 1 and Claim 2 —
  the Chrome side panel is now a first-class Cowork entry point with full
  session continuity, not a separate tool. Update any existing guidance that
  frames "Claude in Chrome" and "Claude Cowork" as distinct capabilities;
  as of August 2026 the browser extension is one access surface into the same
  session model documented in `blog-anthropic-cowork-getting-started.md` and
  `blog-anthropic-cowork-deploy-guide.md`.

- **Chapter on browser automation / agentic browser risk (risk management)**:
  Add the six-layer safety architecture summary (Concrete Artifacts) as the
  current state of Claude's browser-agent defense-in-depth, specifically
  citing the pre-action consistency check (Claim 4) as a newer layer beyond
  the injection classifier and permission toggle already documented from
  `blog-anthropic-dispatch-computer-use.md` and
  `blog-anthropic-computer-use-best-practices.md`. Cite the <0.08% figure
  (Claim 8) with its caveat (internal testing, known techniques only, not a
  claim about novel attacks) rather than presenting it as an unqualified
  security guarantee. Pair with `failure-copilot-cowork-file-exfiltration.md`
  to show a concrete real-world consequence when an equivalent safeguard is
  absent in a competing product.

- **Chapter on enterprise deployment / admin governance of Cowork**: Add the
  Enterprise default-off + domain-allowlist control (Claim 9) as a specific,
  actionable governance lever, alongside whatever deployment guidance already
  exists in `blog-anthropic-cowork-enterprise.md` and
  `blog-anthropic-cowork-deploy-guide.md`.

- **Chapter on tool/plan selection**: Add the plan-availability and platform
  limitation detail (Claim 10) as a practical adoption-timing note — Pro-plan
  and Chromium-alternative-browser users cannot yet use this capability as of
  the source's publication date.

## Extraction Notes

- Read the full announcement post via WebFetch (claude.com/blog/cowork-chrome-side-panel).
  The post is short (~5 min read, per its own metadata) and was read in full;
  no sub-sections were truncated.
- Followed one linked page beyond the primary source, per MINER.md §1's
  allowance to follow substantive linked pages: the safety guide at
  support.claude.com/en/articles/12902428-use-claude-in-chrome-safely, linked
  directly from the "Understanding the Risks" section and explicitly pointed
  to by the post's own safety recommendation (Claim 7). This page provided
  the numeric attack-success-rate figure (Claim 8) and the specific
  blocked-activity/blocked-site lists (Concrete Artifacts) that the
  announcement post itself only gestures at. Did not follow the Chrome Web
  Store listing or the admin-setup guide link, as those are product/install
  pages without additional claims relevant to this note's scope.
  All quotes in this note were copied verbatim from the WebFetch tool output
  for each respective page; none were reconstructed or paraphrased into quote
  form.
- Checked `source-notes/` for existing Cowork and Claude-in-Chrome coverage
  before writing (grepped for "Claude in Chrome", "chrome extension",
  "browser agent", "prompt injection", "automatically approve"). Found ten
  existing Cowork-related notes and two computer-use notes
  (`blog-anthropic-dispatch-computer-use.md`,
  `blog-anthropic-computer-use-best-practices.md`) with direct relevance;
  cross-referenced against both.
- Reviewed CONTRADICTIONS.md — no existing entries relate to Cowork or
  Claude in Chrome. No contradiction found between this source and any
  existing note; none filed.
- **Confidence calibration**: Overall **emerging**. This is a first-party
  product announcement describing a shipped feature (settled claims about
  what exists and is available), but several of the most guide-relevant
  claims — the pre-action consistency check's real-world effectiveness
  (Claim 4) and the attack-success-rate figure's generalizability beyond
  internal testing (Claim 8) — are self-reported and not independently
  verified, which pulls the overall confidence down from "settled."
