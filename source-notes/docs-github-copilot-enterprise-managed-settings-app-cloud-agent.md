---
source_url: https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app
source_type: docs
title: "Enterprise managed settings in the GitHub Copilot app and Copilot cloud agent"
author: GitHub (official changelog)
date_published: 2026-07-27
date_extracted: 2026-07-28
last_checked: 2026-07-28
status: current
confidence_overall: settled
issue: "#2268"
---

# Enterprise Managed Settings in the GitHub Copilot App and Copilot Cloud Agent

> GitHub's July 27, 2026 changelog extends enterprise-managed settings (`managed-settings.json`)
> to two client surfaces not previously covered in the corpus — the GitHub Copilot app and the
> Copilot cloud agent — joining Copilot CLI and VS Code, while explicitly scoping bypass-prompt
> controls to interactive clients only and stating for the first time an explicit precedence
> rule (managed values override anything a developer sets locally).

## Source Context

- **Type**: docs (GitHub official product changelog, July 27, 2026; ~250 words of primary
  announcement text). Followed three linked pages per MINER.md §1: the "Enterprise managed
  settings reference" page (full settings/client matrix), the "Configure enterprise managed
  settings" how-to page (precedence and propagation-timing language), and confirmed the
  "GitHub Community" discussion link (`orgs/community/discussions/199139`) is the same general
  enterprise-managed-settings thread already characterized as off-topic-for-changelog-specifics
  in `docs-github-copilot-enterprise-auto-model-default.md` (Claim 10), so it was not re-fetched.
- **Author credibility**: GitHub engineering team announcing a production governance-surface
  expansion to an existing enterprise feature. Authoritative for: which clients are now
  supported, which specific settings apply to the cloud agent versus interactive clients, the
  precedence rule between managed and local settings, and the propagation-timing model per
  client. Not a credible source for: adoption data, whether cloud agent task queues can be
  starved by a misconfigured marketplace restriction, or full backward-compatibility behavior
  for enterprises that have not yet migrated off the legacy `.github/copilot/settings.json` path.
- **Scope**: A client-surface expansion of the existing enterprise-managed-settings system
  (already documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
  `docs-github-copilot-enterprise-bypass-permissions.md`,
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`, and
  `docs-github-copilot-enterprise-auto-model-default.md`). Covers: which of the four settings
  categories (plugins, marketplaces, bypass-prompt, model-default) apply to the app and cloud
  agent, the precedence rule, and per-client propagation timing. Does NOT cover: a full schema
  reference (deferred to the linked reference page), whether cloud agent task assignment can be
  delayed by a marketplace-restriction misconfiguration, or any technical detail of how the
  cloud agent's non-interactive execution model interacts with policies designed for prompt-based
  clients.

## Extracted Claims

### Claim 1: The Copilot app and Copilot cloud agent now join Copilot CLI and VS Code as supported clients for enterprise managed settings
- **Evidence**: Official changelog, the announcement's central claim, stated as the lead
  technical fact after framing paragraphs.
- **Confidence**: settled (product fact in official first-party changelog, confirmed consistent
  across two independent WebFetch calls)
- **Quote**: "The Copilot app and cloud agent now join Copilot CLI and VS Code as supported
  clients for enterprise managed settings, so your guardrails follow your developers into the
  app and cloud agent tasks."
- **Our assessment**: This is the platform-expansion event the Prospector flagged as high
  novelty. All four prior corpus notes on enterprise-managed settings scope explicitly to "VS
  Code and Copilot CLI" (see `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2:
  "The baseline standards you set for your enterprise apply to every user's Copilot CLI and VS
  Code clients"). This is the first corpus source documenting the app and cloud agent as
  enterprise-managed-settings clients. For Ch02: the client list for `managed-settings.json`
  enforcement grows from two to four surfaces.

### Claim 2: Bypass-prompt controls apply only to interactive clients — the app, Copilot CLI, and VS Code — not to the cloud agent
- **Evidence**: Official changelog, stated as an explicit scope carve-out immediately after
  describing what the cloud agent enforces.
- **Confidence**: settled (explicit scope statement in official changelog)
- **Quote**: "Bypass-prompt controls only apply to the interactive clients (i.e., the app,
  Copilot CLI, and VS Code)."
- **Our assessment**: This is the first documented case in the corpus of a per-client capability
  split within enterprise-managed settings — prior notes (e.g.
  `docs-github-copilot-enterprise-bypass-permissions.md` Claim 2) established that settings
  applied *uniformly* across all supported clients ("The baseline standards you set for your
  enterprise apply to every user's Copilot CLI and VS Code clients"). We read this as a
  structural consequence of the cloud agent's execution model rather than a governance gap:
  `disableBypassPermissionsMode` exists to prevent a human from clicking through an approval
  prompt without reading it, but the cloud agent has no interactive approval prompt to bypass in
  the first place — it is asynchronous and non-interactive by design. The control is scoped to
  where the underlying UI behavior (an approval prompt a human could rubber-stamp) exists. For
  Ch02/Ch06: document this as "not all managed-settings keys apply to all clients" rather than
  as an unpatched gap, and flag it as a caveat for anyone building an enterprise governance
  checklist off the flat client-support tables (see Extraction Notes on the docs page
  discrepancy below).

### Claim 3: The Copilot cloud agent enforces plugin and marketplace controls and only uses plugins/marketplaces the enterprise has approved
- **Evidence**: Official changelog, two adjacent sentences describing cloud agent enforcement
  scope.
- **Confidence**: settled (explicit statement in official changelog)
- **Quote**: "The Copilot cloud agent reads the applicable managed settings, including those for
  plugins and marketplace controls." / "It only uses the plugins and marketplaces you've
  approved."
- **Our assessment**: This extends the supply-chain framing established in
  `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 3 ("This is a direct way to
  enforce your client governance strategy prior to tool execution by removing the risk of users
  installing untrusted plugins") to an autonomous, non-interactive execution surface. Because the
  cloud agent runs unattended, install-time marketplace restriction is arguably *more* important
  there than for an interactive client — there is no human present who could notice and reject an
  unexpected plugin at runtime. For Ch06/07: recommend `strictKnownMarketplaces` as a
  higher-priority control specifically for cloud-agent-enabled enterprises, since the cloud
  agent's supply-chain exposure cannot be mitigated by human vigilance the way an interactive
  client's can.

### Claim 4: For each supported settings key, the enterprise-managed value takes precedence over anything a developer sets locally
- **Evidence**: Official changelog, stated as a general precedence rule covering all settings
  keys, not scoped to a specific key or client.
- **Confidence**: settled (explicit precedence rule stated in official changelog and
  independently corroborated, in closely matching wording, by the linked how-to documentation)
- **Quote**: "For each supported key, your managed value takes precedence over anything a
  developer sets locally."
- **Our assessment**: None of the four prior enterprise-managed-settings notes in the corpus
  documents an explicit precedence rule between the managed configuration and a developer's own
  local settings — they document what the managed setting *does*, not what happens when a
  developer's local configuration disagrees with it. This is the first corpus statement that
  managed settings are non-negotiable overrides rather than defaults a developer could shadow
  with a local file. The linked how-to page states the same rule in near-identical language for
  file-based configuration specifically: "For each supported key, the `managed-settings.json`
  value takes precedence over any file-based configuration a user sets in their client." (see
  Concrete Artifacts). For Ch02: document explicitly that `managed-settings.json` is an override,
  not a default — practitioners writing local Copilot configuration should not expect a local
  setting to win over an enterprise-managed one for any of the four documented capability
  categories.

### Claim 5: Enterprises that already deploy `managed-settings.json` for Copilot CLI and VS Code do not need any new setup for the app and cloud agent to pick up the same policy
- **Evidence**: Official changelog, stated as a direct reassurance to enterprises with existing
  deployments.
- **Confidence**: settled (explicit statement in official changelog)
- **Quote**: "If you already deploy `managed-settings.json` for Copilot CLI and VS Code, there's
  nothing new to set up."
- **Our assessment**: This confirms the single-configuration-file architecture already documented
  across all four prior notes (most recently `docs-github-copilot-enterprise-auto-model-default.md`
  Claim 3, reusing the same `.github-private` source-org repository across capabilities) extends
  automatically to new client surfaces without an administrator having to re-author or duplicate
  policy. For Ch02: the guide should frame `managed-settings.json` as forward-compatible with
  client-surface expansion — enterprises investing in this configuration surface now are not
  taking on migration risk as GitHub adds more clients.

### Claim 6: The app and cloud agent pick up managed settings on different triggers — the app on developer sign-in or restart, the cloud agent on the next task assignment
- **Evidence**: Official changelog, a single sentence naming both propagation triggers.
- **Confidence**: settled (explicit statement in official changelog)
- **Quote**: "The Copilot app automatically picks up your existing configuration the next time a
  developer signs in or restarts the app, and the cloud agent observes changes on the next task
  assignment."
- **Our assessment**: This is a new propagation-timing model not previously documented in the
  corpus. `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 6 documented
  "the next time they authenticate from a supported client" as the CLI/VS Code propagation
  trigger; this note adds a third trigger — "next task assignment" — specific to the cloud
  agent's queue-based, non-session execution model. Practically: a policy change targeting cloud
  agent behavior (e.g., tightening `strictKnownMarketplaces`) will not affect a cloud agent task
  that is already running or already queued before the change propagates — it takes effect on
  the *next* task the agent is assigned. For Ch02: add "next task assignment" as a third
  propagation trigger alongside "next authentication"/"sign-in or restart," and note it is
  specific to the cloud agent's asynchronous task model.

### Claim 7: GitHub frames incomplete cross-client governance coverage explicitly as a security gap, using the framing "your governance is only as strong as its least-covered surface"
- **Evidence**: Official changelog, framing paragraphs preceding the technical announcement.
- **Confidence**: settled (verbatim framing language in official changelog; a positioning
  statement, not a technical fact, but directly relevant to how GitHub wants enterprises to
  reason about multi-client governance)
- **Quote**: "Any client that sits outside your policy is a gap, a place where someone could
  install a plugin you haven't vetted or run a command you'd normally gate." / "Your governance
  is only as strong as its least-covered surface."
- **Our assessment**: This is the rhetorical framing the Prospector's triage comments quoted
  independently across all three triage passes, which suggests it is the changelog's clearest
  and most quotable sentence. We read it as GitHub retroactively characterizing the pre-July-27
  state (app and cloud agent outside managed-settings coverage) as having been a governance gap
  — a useful data point for Ch05 framing enterprise AI tooling adoption as an ongoing coverage
  problem rather than a one-time configuration task. For Ch05: use this framing to motivate an
  audit practice — "list every client surface where Copilot/Claude Code/etc. runs in your
  enterprise, and confirm each one is covered by policy" — since new client surfaces continue to
  appear over time (this is the fifth capability-surface expansion event in the corpus's
  enterprise-managed-settings notes since June 5, 2026).

### Claim 8: First-time setup for enterprise managed settings still follows the same three-step `.github-private` repository process documented since June 2026, with settings also deployable via MDM or a distributed file
- **Evidence**: Official changelog "Getting Started" section, numbered steps.
- **Confidence**: settled (matches, near-verbatim, the setup process already documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md`; this changelog restates it for
  readers new to the feature)
- **Quote**: "If you're setting up enterprise managed settings for the first time, the default
  approach is server-managed deployment: 1. Create and configure a `.github-private` repository
  in your enterprise. 2. In that repository, create or update `copilot/managed-settings.json`.
  3. Add your enterprise policy keys and values in JSON, then commit and push to the default
  branch." / "You can also deploy through MDM or a distributed file."
- **Our assessment**: This corroborates rather than extends the corpus — the `.github-private`
  repository and `copilot/managed-settings.json` path (the "new preferred path" per
  `docs-github-copilot-enterprise-bypass-permissions.md` Claim 4) are confirmed unchanged seven
  weeks after that migration was first documented. The "MDM or a distributed file" deployment
  option had not been explicitly named as an alternative in any prior corpus note (prior notes
  only documented the `.github-private` git-based path); this is the first explicit mention of
  MDM and distributed-file deployment as first-class alternatives, not just a fallback.

### Claim 9 (secondary source, lower confidence): The enterprise managed settings reference documents at least two settings keys — `enabledPlugins` and `extraKnownMarketplaces` — and one client-scoped setting, `telemetry`, not previously named in the corpus
- **Evidence**: Linked "Enterprise managed settings reference" page, fetched via WebFetch and
  returned as an AI-generated summary rather than raw verbatim text.
- **Confidence**: emerging (from a secondary documentation page processed through an
  AI-summarizing fetch, not independently verified against raw HTML; not stated in the July 27
  changelog itself)
- **Quote**: (no direct quote; the WebFetch response was already a synthesized summary table,
  not source prose — see Extraction Notes)
- **Our assessment**: If accurate, `enabledPlugins` (enable/disable specific plugins by key) and
  `extraKnownMarketplaces` (add marketplaces, as distinct from `strictKnownMarketplaces`
  restricting to a whitelist) would be two settings keys not documented anywhere in the corpus's
  four prior enterprise-managed-settings notes. `telemetry` (OpenTelemetry export configuration)
  would be entirely novel — a governance capability outside the plugin/permission/model-selection
  categories the corpus has documented so far. We flag these as plausible but unverified: the
  Assayer should independently confirm these key names against the live reference page before
  the guide cites them, since this claim rests on a single AI-summarized fetch rather than a
  verbatim excerpt.

### Claim 10 (secondary source, discrepancy noted): The reference page's client-support matrix and the how-to page's supported-clients list both omit the cloud agent, even though the July 27 changelog states the cloud agent is now supported
- **Evidence**: The "Enterprise managed settings reference" page's client-support matrix
  (fetched via WebFetch) lists only three client columns — Copilot CLI, VS Code, GitHub Copilot
  App — no cloud agent column. The separately linked "Configure enterprise managed settings"
  how-to page, fetched independently, states supported clients as "Copilot CLI, VS Code, The
  GitHub Copilot app" and does not mention the cloud agent at all.
- **Confidence**: anecdotal (an observation about documentation-page staleness, not a product
  fact; both supporting fetches are AI-summarized, not raw-HTML-verified)
- **Quote**: (no direct quote; both pages were returned as summaries by WebFetch rather than
  verbatim text — see Extraction Notes)
- **Our assessment**: This looks like ordinary documentation lag — the changelog is the
  first-party announcement of record and is unambiguous about cloud agent support (Claims 1–3
  above), while two secondary reference/how-to pages had apparently not yet been updated to add
  a cloud agent column or mention at the time of this extraction (2026-07-28, one day after the
  changelog's publication). We do not treat this as a contradiction requiring a filed
  contradiction issue (MINER.md §4a) because it is a staleness gap between a changelog and its
  supporting docs pages, not two sources making opposing claims about the same fact — the docs
  pages simply haven't caught up yet. Flagging it here so a future source note revisiting these
  reference pages can confirm whether the cloud agent column has since been added.

## Concrete Artifacts

### Client support summary (July 27, 2026 changelog)

```
Enterprise managed settings ("managed-settings.json") client coverage:

Client              | Plugins | Marketplaces | Bypass-prompt | Model-default
---------------------|---------|--------------|----------------|---------------
Copilot CLI          |   Y     |     Y        |       Y        |      Y
VS Code              |   Y     |     Y        |       Y        |      Y
Copilot app (NEW)    |   Y     |     Y        |       Y        |      Y
Copilot cloud agent  |   Y     |     Y        |       N        |   (not stated)
  (NEW)

"N" for cloud agent bypass-prompt: cloud agent is non-interactive, so there is
no approval prompt to bypass in the first place (our inference, not stated
explicitly as the reason in the source).

Source: github.blog changelog, 2026-07-27 (see Claims 1-3). Table structure is
this note's synthesis; the changelog itself states client coverage in prose,
not a table.
```

### Precedence and propagation rules (July 27, 2026 changelog + linked how-to page)

```
Precedence: managed-settings.json value > any developer/local-file setting,
            for every supported key.
  - Changelog wording: "For each supported key, your managed value takes
    precedence over anything a developer sets locally."
  - How-to page wording (independent fetch): "For each supported key, the
    managed-settings.json value takes precedence over any file-based
    configuration a user sets in their client."

Propagation triggers:
  - App:         next developer sign-in, or app restart
  - Cloud agent: next task assignment
  - CLI/VS Code (per prior notes, e.g. docs-github-copilot-enterprise-strict-
    known-marketplaces.md Claim 6): next authentication
  - General (server-managed deployment): ~1 hour, since clients periodically
    poll the server (how-to page: "users on a supported client see the
    specified settings within about an hour")

Source: github.blog changelog, 2026-07-27; docs.github.com "Configure
enterprise managed settings" how-to page, fetched 2026-07-28.
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2 and
    `docs-github-copilot-enterprise-bypass-permissions.md` Claim 2: both established that
    enterprise-managed settings apply "uniformly" across supported clients. This note
    corroborates the underlying architecture (one config, multiple clients) while adding the
    first documented exception (Claim 2 here) to full uniformity.
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 4 and
    `docs-github-copilot-enterprise-auto-model-default.md` Claim 6: both documented
    `copilot/managed-settings.json` as the current preferred configuration path with
    `.github/copilot/settings.json` as the backward-compatible legacy path. This note's Getting
    Started section (Claim 8) uses `copilot/managed-settings.json` directly, confirming the path
    is still current seven weeks later.
  - `docs-github-copilot-enterprise-auto-model-default.md` Claim 3: documented reuse of the
    same `.github-private` source-org repository across capability additions. Claim 5 here
    (no new setup needed for app/cloud agent) confirms that pattern continues to hold across a
    client-surface expansion, not just a settings-key addition.
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 3 (supply-chain framing,
    "prior to tool execution"): Claim 3 here extends the same framing to the cloud agent, an
    unattended execution surface where the supply-chain argument is arguably stronger.

- **Contradicts**: None identified requiring a filed contradiction issue. Claim 10 above notes a
  documentation-lag discrepancy (reference/how-to pages not yet reflecting cloud agent support),
  but this is staleness between a changelog and its own supporting docs, not an opposing claim
  from an independent source — per MINER.md §4a this does not meet the bar for filing a
  contradiction issue. No existing corpus source makes a claim that conflicts with the app/cloud
  agent expansion, the precedence rule, or the propagation-timing claims in this note.

- **Extends**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
    `docs-github-copilot-enterprise-bypass-permissions.md`,
    `docs-github-copilot-enterprise-strict-known-marketplaces.md`, and
    `docs-github-copilot-enterprise-auto-model-default.md`: this note is the fifth entry in a
    now five-part timeline (June 5 → June 17 → June 25 → July 1 → July 27) of enterprise-managed-
    settings capability and client-surface expansions, all sharing one configuration file and
    one source-org repository. This note extends the *client* axis (two clients → four clients)
    where the prior four notes extended the *capability* axis (plugins → hooks/MCP → bypass
    permissions → marketplace restriction → model default).

- **Novel**:
  - **Per-client capability differentiation**: Claim 2 (bypass-prompt controls excluded for the
    cloud agent) is the first documented case in the corpus where a `managed-settings.json`
    capability does *not* apply uniformly to every supported client. Prior notes documented
    uniform enforcement as an architectural given.
  - **Explicit precedence rule**: Claim 4 is the first corpus statement of a precedence
    relationship between managed settings and developer-local settings. No prior note states
    what happens when the two disagree.
  - **"Next task assignment" as a propagation trigger**: Claim 6 documents a propagation model
    tied to an asynchronous task queue rather than an authentication or session event — new to
    the corpus's propagation-timing vocabulary.
  - **MDM / distributed-file deployment named as a first-class alternative**: Claim 8's mention
    of MDM and distributed-file deployment, alongside the git-based `.github-private` path, is
    the first time these alternatives are named explicitly in a corpus source note (though
    `docs-github-copilot-enterprise-strict-known-marketplaces.md` implied broader deployment
    mechanisms existed via the "enforcement timing model").
  - **Possible new settings keys** (`enabledPlugins`, `extraKnownMarketplaces`, `telemetry`) per
    Claim 9 — unverified beyond a single AI-summarized fetch, flagged for Assayer confirmation
    rather than asserted as settled.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Update the enterprise-managed-settings client list from "VS Code and Copilot CLI" to four
    clients: VS Code, Copilot CLI, the Copilot app, and the Copilot cloud agent (Claim 1).
  - Add a caveat table (see Concrete Artifacts) noting that not every capability applies to
    every client — specifically, bypass-prompt control (`disableBypassPermissionsMode`) does not
    apply to the cloud agent (Claim 2). Practitioners building an enterprise governance checklist
    from the guide should not assume uniform coverage without checking per-key client support.
  - Document the explicit precedence rule (Claim 4): managed settings override local/developer
    settings for every supported key. This should be stated plainly wherever the guide currently
    describes `managed-settings.json` as a governance mechanism, since no prior guide-facing
    source made the override behavior explicit.
  - Add "next task assignment" as a third propagation trigger (alongside "next authentication"
    and "sign-in/restart") specific to the cloud agent's asynchronous execution model (Claim 6).

- **Chapter 05 (Team Adoption — Enterprise Governance)**:
  - Use the "your governance is only as strong as its least-covered surface" framing (Claim 7)
    to motivate a recurring audit practice: enumerate every AI-tooling client surface in use
    across the enterprise and confirm each is covered by the same managed policy. This is now
    the fifth capability/surface expansion documented in seven weeks — the guide should frame
    enterprise AI governance as an ongoing coverage exercise, not a one-time setup task.
  - Note that enterprises with an existing `.github-private`/`managed-settings.json` deployment
    get cloud agent and app coverage automatically (Claim 5) — this lowers the marginal cost of
    adopting the cloud agent for enterprises that have already invested in managed settings for
    CLI/VS Code.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Recommend `strictKnownMarketplaces` (documented in
    `docs-github-copilot-enterprise-strict-known-marketplaces.md`) as a higher-priority control
    specifically for cloud-agent-enabled enterprises (Claim 3): the cloud agent's unattended
    execution model means there is no human present to catch an unexpected plugin at runtime,
    making install-time restriction more load-bearing than for interactive clients.
  - Note the bypass-prompt exclusion for the cloud agent (Claim 2) as a structural fact to
    explain to auditors, not a governance gap to remediate — the control doesn't apply because
    the underlying interactive-approval-prompt behavior it targets doesn't exist on that client.

## Extraction Notes

1. **Two independent fetches of the primary changelog**: The first exploratory WebFetch and a
   second fetch explicitly requesting verbatim, sentence-by-sentence quoting returned consistent
   wording for every claim quoted directly from the changelog (Claims 1–8). The second fetch's
   output is used for all direct quotes in this note.

2. **Secondary docs pages returned as AI summaries, not verbatim text**: Two linked pages — the
   "Enterprise managed settings reference" and the "Configure enterprise managed settings"
   how-to page — were fetched via WebFetch, which processes HTML through an AI model before
   returning results. Both responses came back as synthesized summaries/tables rather than
   quotable prose (the reference page's response was explicitly framed as a "Reference Summary").
   No claim in this note treats those summaries as verbatim quotes; Claims 9 and 10 are marked
   `emerging`/`anecdotal` accordingly, and the Assayer should independently verify the specific
   key names (`enabledPlugins`, `extraKnownMarketplaces`, `telemetry`) and the client-matrix
   discrepancy against the live reference-page HTML before the guide cites them as settled facts.
   One exception: the how-to page's precedence-rule quote ("For each supported key, the
   `managed-settings.json` value takes precedence...") was returned in clearly quoted form
   distinct from the surrounding summary and closely matches the changelog's own wording on the
   same point, so it is treated as a corroborating quote in Claim 4/Concrete Artifacts rather
   than a paraphrase.

3. **Linked Community discussion not re-fetched**: The changelog links to
   `github.com/orgs/community/discussions/199139`, the same URL already characterized in
   `docs-github-copilot-enterprise-auto-model-default.md` (Claim 10, Extraction Note 3) as the
   general enterprise-managed-settings discussion thread, not scoped to any one changelog. Given
   that prior note's finding that the thread predates and is not specific to individual
   changelog entries, it was not re-fetched for this extraction.

4. **No contradiction issue filed**: See Cross-References → Contradicts. The only discrepancy
   found (Claim 10, reference/how-to pages not yet listing the cloud agent) is documentation
   staleness relative to the changelog's own announcement, not an opposing claim from an
   independent source, so it does not meet the MINER.md §4a bar for filing a contradiction issue.

5. **Short primary source, but rich linked material**: The changelog itself is ~250 words, but
   is the fifth in a series of increasingly specific corpus notes on the same configuration
   system, which makes the cross-referencing surface unusually deep. All prior four notes were
   re-read in full (not skimmed) to verify claim numbers before citing them, per MINER.md §4b.
