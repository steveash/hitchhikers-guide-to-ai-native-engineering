---
source_url: https://claude.com/blog/cowork-built-in-browser
source_type: blog-post
title: "Claude Cowork Gets a Built-In Browser"
author: Anthropic (Claude.com blog)
date_published: 2026-08-26
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: emerging
issue: "#2994"
---

# Claude Cowork Gets a Built-In Browser

> Anthropic's product announcement introducing a second, isolated browser built directly
> into the Claude Cowork desktop app — distinct from the existing Claude in Chrome
> extension — establishing an explicit division of labor between the two ("hand off a web
> task" vs. "the page you already have open") and reusing the Claude in Chrome safety
> architecture and safety-guide caveats for the new surface.

## Source Context

- **Type**: blog-post (first-party Anthropic product announcement, claude.com,
  August 26, 2026)
- **Author credibility**: Unbylined first-party Anthropic post on the official product
  blog. Authoritative on stated capabilities, plan availability, and intended safety
  architecture; as vendor communication, the risk-reduction claim ("meaningfully reduce
  the risk") is self-reported and directional, not independently verified — the post
  explicitly declines to claim the risk is eliminated. The article links out to the same
  Claude-in-Chrome safety guide already read and documented in
  `blog-anthropic-cowork-chrome-side-panel.md`
  (support.claude.com/en/articles/12902428-use-claude-in-chrome-safely); that guide was
  not re-extracted here since its claims are already captured in the existing note.
- **Scope**: Covers the built-in browser's architecture (isolated from the user's own
  browser), the login-import mechanism, the explicit division of labor between the
  built-in browser and Claude in Chrome, default browser selection logic, the safety
  architecture reused from Claude in Chrome, and rollout/plan availability including
  platform limits. Does NOT cover: pricing, token/cost characteristics of browser
  sessions, technical implementation detail on how the browser is sandboxed, a new
  quantified security metric specific to the built-in browser (it points to the existing
  Claude in Chrome safety guide instead), or comparison benchmarks between the two
  browser paths.

## Extracted Claims

### Claim 1: Claude Cowork now has a second browser — built directly into the desktop app — that opens in a side panel automatically whenever a task needs the web, as a separate mechanism from the Claude in Chrome extension

- **Evidence**: Direct product-architecture statement in the opening paragraph, describing
  the new capability and immediately contrasting it with how Cowork previously accessed
  the web (via the Claude in Chrome extension only).
- **Confidence**: settled (first-party statement of shipped architecture)
- **Quote**: "Claude now has a browser built into Claude Cowork on the desktop app. When a
  task needs to use a website, a browser opens in the side panel and Claude navigates
  webpages, reads them, clicks, and types."
- **Our assessment**: This is the core claim of the post. It is not a replacement for
  Claude in Chrome (documented in `blog-anthropic-cowork-chrome-side-panel.md`) but a
  second, parallel browser-access path within the same Cowork session model. For the
  guide, this means "browser automation in Cowork" is no longer a single mechanism —
  practitioners now choose between two distinct browser tools with different isolation
  properties (Claim 3, Claim 5).

### Claim 2: The built-in browser requires no extension install or setup, and shares nothing from the user's own browser unless explicitly chosen

- **Evidence**: Direct statement immediately following the architecture description,
  contrasting the new mechanism with the extension-based Claude in Chrome setup.
- **Confidence**: settled (first-party statement of product behavior)
- **Quote**: "No extension, no setup, and nothing shared from your own browser unless you
  choose to."
- **Our assessment**: This removes the installation friction associated with Claude in
  Chrome (a browser extension the user must add). Combined with Claim 8 (on by default
  once rolled out), this makes the built-in browser a zero-configuration capability —
  relevant for practitioners evaluating adoption friction between the two browser paths.

### Claim 3: The built-in browser is architecturally isolated from the user's personal browser — Claude cannot see the user's tabs, bookmarks, or passwords

- **Evidence**: Direct isolation claim in the "Which Browser, When" section, stated as
  the mechanism's defining property.
- **Confidence**: settled (first-party statement of a named isolation guarantee)
- **Quote**: "It's Claude's browser, not yours. The built-in browser is separate from your
  own. Claude never sees your tabs, bookmarks, or passwords."
- **Our assessment**: This is the key architectural differentiator from Claude in Chrome,
  which by design operates inside the user's actual browser session (side panel of the
  user's own Chrome, with access to whatever the user is signed into, per
  `blog-anthropic-cowork-chrome-side-panel.md`). The built-in browser inverts that model:
  it is a separate, Claude-controlled browser instance with no default access to the
  user's browsing state. This is a genuine isolation improvement for tasks that don't
  need the user's existing sessions, at the cost of not having those sessions available
  by default (mitigated by Claim 4).

### Claim 4: Users can selectively import site-specific logins into the built-in browser from Chrome, Edge, or Firefox (macOS) and Firefox (Windows/Linux), but banking, email, and SSO sites are excluded by default

- **Evidence**: Direct statement of the login-import mechanism and its default
  exclusions, in the "Which Browser, When" section.
- **Confidence**: settled (first-party statement of a named product control)
- **Quote**: "To stay signed in to your sites, you can bring your logins over site by
  site, from Chrome, Edge, or Firefox on macOS and from Firefox on Windows and Linux.
  Banking, email, and single sign-on sites are left out unless you choose to include
  them."
- **Our assessment**: This is a concrete, actionable governance detail: the default-deny
  posture on banking/email/SSO mirrors the "certain apps off-limits by default" pattern
  from computer use (`blog-anthropic-dispatch-computer-use.md` Claim 3) and the
  blocked-site list in the Claude in Chrome safety guide (cited in
  `blog-anthropic-cowork-chrome-side-panel.md` Concrete Artifacts, Layer 5). The
  site-by-site, opt-in import model is narrower than a blanket "sync my browser" feature
  — it requires deliberate per-site action rather than defaulting to broad access.

### Claim 5: Anthropic defines an explicit division of labor between the two browser tools — the built-in browser for handing off self-contained web tasks, Claude in Chrome for acting on a page the user already has open and is already signed into

- **Evidence**: Direct statement in the "Which Browser, When" section giving concrete
  examples for each tool.
- **Confidence**: settled (first-party statement of intended usage pattern)
- **Quote**: "The built-in browser is for handing web tasks to Claude while you keep
  working: gathering research for a report, or collecting this month's invoices from a
  vendor portal. Claude in Chrome is for the page you already have open, with the
  accounts you're already signed in to, such as updating your CRM, working through your
  inbox, or editing the doc in front of you."
- **Our assessment**: This is the most practically useful claim in the post for
  practitioners: it gives a decision rule between two tools that otherwise look similar
  (both let Claude control a browser). The distinguishing variable is *session state* —
  does the task need the user's existing logged-in context (Claude in Chrome) or can it
  run in a fresh, disposable browser (built-in browser)? This maps cleanly onto the
  connector-first/computer-use-fallback hierarchy already documented in
  `blog-anthropic-dispatch-computer-use.md` Claim 1: within the "no connector" tier,
  there is now a further split by whether the task needs the user's own browser identity.

### Claim 6: Claude in Chrome remains the default browser tool if the user already has it set up; otherwise the built-in browser is used by default, and users can switch the preference at any time

- **Evidence**: Direct statement of the default-selection logic and the settings location
  to override it.
- **Confidence**: settled (first-party statement of product defaults)
- **Quote**: "If you already use Claude in Chrome, it keeps working and stays your
  default; otherwise Claude uses the built-in browser. Switch anytime in Settings →
  Cowork → Preferred browser."
- **Our assessment**: This is a specific, actionable configuration detail for
  practitioners deploying Cowork: existing Claude in Chrome users see no default behavior
  change, while new/non-extension users get the built-in browser automatically. Worth
  documenting alongside the Enterprise admin toggle (Claim 9) as the two levers
  practitioners have over which browser tool activates.

### Claim 7: The built-in browser reuses the same safety architecture as Claude in Chrome, including the pre-action consistency check, and Anthropic repeats the same hedge that prompt-injection risk is reduced but not eliminated

- **Evidence**: Direct statement in the "Staying in Control" section, explicitly naming
  the shared safeguard and repeating language nearly identical to the Claude in Chrome
  announcement.
- **Confidence**: settled that the safeguards are reused (first-party architectural
  statement); the underlying risk-reduction effectiveness itself remains emerging/
  unverified, consistent with the source's own hedge.
- **Quote**: "It runs the same safeguards as Claude in Chrome, including the checks that
  review Claude's actions against what you asked for. Those measures meaningfully reduce
  the risk but can't eliminate it, so we recommend starting on sites you trust."
- **Our assessment**: This confirms the built-in browser does not introduce a separate
  safety model — it inherits the pre-action consistency check already documented as novel
  in `blog-anthropic-cowork-chrome-side-panel.md` Claim 4, plus (implicitly, via the
  linked safety guide) the model-level classifier and injection scanning documented in
  that note's Concrete Artifacts. No new quantified attack-success-rate figure is given
  for the built-in browser specifically; the post links to the same safety guide rather
  than publishing a browser-specific number. The guide should not treat the built-in
  browser as safer or riskier than Claude in Chrome based on this post alone — the
  vendor's own framing is that the safety layer is identical.

### Claim 8: The built-in browser rolls out over "the coming week" to Pro, Max, and Team plans in the desktop app on macOS, Windows, and Linux (Linux in beta), is on by default once it arrives, and Enterprise admins can enable it immediately via Organization settings

- **Evidence**: Explicit rollout, platform, and default-state statements, given twice
  (once in the lede, once in "Getting Started").
- **Confidence**: settled (first-party statement of shipped/rolling-out availability as
  of publication date)
- **Quote**: "The built-in browser is rolling out over the coming week to Pro, Max, and
  Team plans in the Claude desktop app on macOS, Windows, and Linux (in beta). Once it
  reaches you, it's on by default: give Claude a task that involves a website and the
  browser opens on its own. On Enterprise plans, it's available now and admins can manage
  it in Organization settings → Cowork → Built-in browser."
- **Our assessment**: Two details matter for deployment planning: (1) this is an
  on-by-default rollout for Pro/Max/Team, unlike Claude in Chrome's opt-in extension
  install — practitioners on those plans should expect the behavior change to arrive
  automatically without user action; (2) Linux desktop support is explicitly beta-labeled,
  a platform maturity signal worth flagging for teams standardized on Linux desktops.
  Enterprise gets immediate availability plus an explicit admin management surface
  (Organization settings → Cowork → Built-in browser), which is the governance lever
  parallel to the domain-allowlist control Anthropic ships for Claude in Chrome
  (`blog-anthropic-cowork-chrome-side-panel.md` Claim 9), though this post does not state
  whether the built-in browser has an equivalent domain-restriction control — it only
  confirms an on/off admin toggle.

### Claim 9: The built-in browser lives in the desktop app only; Claude can still drive it from a web or mobile session as long as the desktop app stays open and online, and on the web without a desktop app, Claude in Chrome is the only way to give Claude a browser

- **Evidence**: Explicit platform-dependency statement in "Getting Started," describing
  what happens when the user is not on the desktop app.
- **Confidence**: settled (first-party statement of a technical requirement)
- **Quote**: "The built-in browser lives in the desktop app. From the web or your phone,
  Claude can still drive it as long as your desktop app is open and online. On the web
  without the desktop app, Claude in Chrome remains the way to give Claude a browser."
- **Our assessment**: This mirrors the tethering constraint already documented for
  computer use in `blog-anthropic-dispatch-computer-use.md` Claim 7 ("Claude's desktop
  app must be awake and running") — the built-in browser is not a headless or
  cloud-hosted capability; it requires an always-on or attended desktop machine as the
  execution host, even when the triggering session is mobile or web. This is a real
  architectural limitation for practitioners who want browser automation as a background,
  server-side process: neither Claude in Chrome nor the built-in browser is deployable
  without a live desktop app instance somewhere.

## Concrete Artifacts

```
Claude Cowork — Two Browser Tools, Division of Labor
(from claude.com/blog/cowork-built-in-browser, Aug 26, 2026)

                        Built-in browser              Claude in Chrome
Isolation               Separate from user's browser  Runs inside user's own browser
Session/login access    None by default; site-by-site Full access to whatever the
                         opt-in import (no banking/    user is already signed into
                         email/SSO by default)
Setup                    None (built into desktop app) Chrome extension install
Best for                 Self-contained handoff tasks  Tasks on a page/account the
                         (research, portal data pulls) user already has open
Default selection        Used if Claude in Chrome not  Stays default if already set up
                         already set up
Platform                 Desktop app only (macOS,      Desktop app extension +
                         Windows, Linux beta);         "Cowork session" surfaces
                         drivable remotely only while   (per blog-anthropic-cowork-
                         desktop app is open/online     chrome-side-panel.md)
Plan availability        Pro/Max/Team (rolling out     Max/Team (per prior note);
                         this week); Enterprise now     Pro rolling out (per prior note)
Safety architecture      Same as Claude in Chrome (pre-action consistency check,
                         injection classifier, "meaningfully reduce, can't eliminate")

Admin control (built-in browser): Organization settings → Cowork → Built-in browser
User control (browser choice):    Settings → Cowork → Preferred browser
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-chrome-side-panel.md` Claim 4 (pre-action consistency check)
    and Claim 6 (risk "meaningfully reduced... cannot eliminate" hedge): this post
    restates both almost verbatim for the built-in browser, confirming the safety
    architecture is shared rather than reinvented per surface.
  - `blog-anthropic-dispatch-computer-use.md` Claim 3 (default app/site denylist as a
    safety layer): the built-in browser's default exclusion of banking, email, and SSO
    sites from login import is the same categorical-risk-exclusion pattern applied to a
    new surface.
  - `blog-anthropic-dispatch-computer-use.md` Claim 7 (computer use requires the desktop
    app "awake and running"): Claim 9 above shows the same tethering constraint applies
    to the built-in browser — no headless/server deployment path exists for either
    capability as of this post.

- **Contradicts**: None identified. This post does not conflict with any claim in
  `blog-anthropic-cowork-chrome-side-panel.md` or `blog-anthropic-dispatch-computer-use.md`;
  it adds a second, parallel browser mechanism rather than revising or replacing the
  existing one. Checked CONTRADICTIONS.md — no open entries relate to Cowork browser
  tooling. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-cowork-chrome-side-panel.md`: that note documents Claude in Chrome as
    a Cowork-integrated, extension-based, user's-own-browser access surface. This post
    adds a second access surface with an inverted isolation model (Claim 3) and
    documents, for the first time in the corpus, an explicit vendor-stated decision rule
    for choosing between two browser tools (Claim 5) rather than one browser tool with a
    single behavior.
  - `blog-anthropic-dispatch-computer-use.md`: extends the connector-first →
    computer-use-fallback hierarchy (Claim 1 of that note) with a further split inside
    the "no connector" tier: session-dependent tasks route to Claude in Chrome,
    session-independent tasks route to the built-in browser.
  - `blog-anthropic-cowork-deploy-guide.md`: the Chat/Cowork/Code decision framework in
    that note (Claim 1) operates one level above this post's browser-tool decision rule
    (Claim 5) — once a task is routed to Cowork, this post supplies the next-level
    decision (which browser) for web-touching Cowork tasks.

- **Novel** (not in prior corpus):
  - **A second, isolated, Claude-controlled browser as a Cowork surface**, distinct in
    architecture from the extension-based Claude in Chrome (Claim 1, Claim 3): no prior
    source note documents Anthropic shipping two separate browser-access mechanisms with
    different isolation properties for the same product.
  - **Explicit vendor-stated decision rule between two browser tools** (Claim 5): prior
    corpus sources document only single-tool selection hierarchies (connector vs.
    computer use). This is the first source with a two-way split inside the
    "give Claude a browser" category itself.
  - **Site-by-site opt-in login import with categorical exclusions** (Claim 4): a new,
    more granular access-control mechanism than the binary "off by default, admin
    enables" Enterprise control previously documented for Claude in Chrome.

## Guide Impact

- **Chapter on Cowork / multi-surface agent work**: Add the two-browser-tool model
  (Claim 1, Claim 5, Concrete Artifacts table) as an update to any existing guidance that
  treats "give Claude a browser in Cowork" as a single mechanism. Practitioners now choose
  between the built-in browser (isolated, zero-setup, for handoff tasks) and Claude in
  Chrome (session-aware, extension-based, for tasks on an already-open/signed-in page).
  The decision rule from Claim 5 is concrete enough to state directly in the guide as a
  rule of thumb.

- **Chapter on browser automation / agentic browser risk (risk management)**: Note that
  the built-in browser's isolation (Claim 3) is a genuine risk-reduction property distinct
  from the safety-classifier layer — even before any prompt-injection defense activates,
  the built-in browser has nothing to leak (no tabs, bookmarks, passwords) unless the user
  opts a specific site in. This is an architectural mitigation, not just a behavioral one,
  and is a stronger default posture than Claude in Chrome's model (which starts with full
  access to whatever the user is signed into). The guide's risk-management section should
  present the built-in browser as the lower-blast-radius default choice when a task does
  not require the user's own logged-in sessions.

- **Chapter on enterprise deployment / admin governance of Cowork**: Add the built-in
  browser's Enterprise admin toggle (Organization settings → Cowork → Built-in browser,
  Claim 8) alongside the domain-allowlist control already documented for Claude in Chrome
  in `blog-anthropic-cowork-chrome-side-panel.md`. Flag that this post does not state
  whether the built-in browser supports the same domain-restriction granularity — only an
  on/off toggle is confirmed; the guide should not assume feature parity between the two
  admin controls without further evidence.

- **Chapter on tool/plan selection and deployment timing**: Add the rollout detail
  (Claim 8) — on-by-default for Pro/Max/Team once it arrives, Linux still in beta — as a
  practical adoption-timing note distinct from Claude in Chrome's opt-in extension model.

## Extraction Notes

- Read the full announcement post via two WebFetch passes (claude.com/blog/cowork-built-in-browser):
  a first summarizing pass, then a second explicitly requesting full verbatim paragraph-by-paragraph
  text with linked URLs, to ensure all quotes in this note are copied character-for-character
  from the source rather than reconstructed from the first, summarized pass.
  The post is short (~5 min read per its own metadata) and was read in full.
- The post links to the same Claude-in-Chrome safety guide
  (support.claude.com/en/articles/12902428-use-claude-in-chrome-safely) already fetched and
  extracted in full for `blog-anthropic-cowork-chrome-side-panel.md`. Did not re-fetch or
  re-extract it here since its claims (the six-layer safety architecture, the <0.08% attack-success
  figure, the blocked-site/activity lists) are already captured in that note and apply unchanged to
  this post's "same safeguards" claim (Claim 7).
- Also fetched one related linked post published the same day, "Claude in Chrome is generally
  available" (claude.com/blog/claude-in-chrome-generally-available), for background context only —
  it is not the assigned source for this issue and no claims from it are extracted into this note.
  For the record: that companion post states Claude in Chrome exited its pilot/research-preview
  phase into general availability on the same day (Aug 26, 2026) as this built-in-browser post, and
  reports newer per-model attack-success-rate figures (0% for Sonnet 5/Opus 5/Mythos 5, 0.3% for
  Fable 5 against stronger red-team attacks) that appear to supersede the single <0.08% blended
  figure in the safety guide cited by `blog-anthropic-cowork-chrome-side-panel.md`. This is flagged
  here as a pointer for a future Miner run on that post, not asserted as a claim of this note — the
  figures were read via a summarizing WebFetch pass, not verified against verbatim source text, so
  they should not be quoted from this note.
- Checked `source-notes/` for existing Cowork and browser-automation coverage before writing
  (16 Cowork-related notes, plus `blog-anthropic-dispatch-computer-use.md` and
  `blog-anthropic-computer-use-best-practices.md` for computer-use safety architecture).
  Cross-referenced against the three notes with direct topical overlap.
- Reviewed CONTRADICTIONS.md — no existing entries relate to Cowork or browser tooling. No
  contradiction found between this source and any existing note; none filed.
- **Confidence calibration**: Overall **emerging**. Product architecture, availability, and default-
  behavior claims (Claims 1, 2, 4, 6, 8, 9) are settled first-party descriptions of shipped/rolling-out
  features. The isolation claim (Claim 3) is a settled architectural statement. The safety-effectiveness
  claim (Claim 7) explicitly self-hedges ("meaningfully reduce... can't eliminate") and reuses an
  unverified risk-reduction framing already flagged as emerging in the sibling Claude-in-Chrome note —
  this pulls the overall confidence down from "settled," consistent with how
  `blog-anthropic-cowork-chrome-side-panel.md` was calibrated.
