---
source_url: https://github.blog/changelog/2026-07-01-enterprise-managed-settings-json-is-generally-available
source_type: docs
title: "Enterprise managed-settings.json is generally available"
author: GitHub (official changelog)
date_published: 2026-07-01
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: settled
issue: "#1541"
---

# Enterprise managed-settings.json is Generally Available

> GitHub's July 1, 2026 changelog moves the enterprise-managed settings system (previewed
> across three June 2026 changelogs) to general availability under the file name
> `managed-settings.json`, and for the first time enumerates the complete set of five
> supported configuration keys together — revealing two previously undocumented keys,
> `extraKnownMarketplaces` and `enabledPlugins`, plus confirmation that `model` is an
> enterprise-managed key, alongside the already-documented `strictKnownMarketplaces` and
> `disableBypassPermissionsMode`.

## Source Context

- **Type**: docs (GitHub official product changelog, July 1, 2026; approximately 150 words,
  "2 minute read" per the page's own estimate)
- **Author credibility**: GitHub engineering team announcing a GA status change for a system
  previously in public preview. Authoritative for: the GA status itself, the complete list of
  supported configuration keys, the file location and path, the enforcement/refresh mechanism,
  and client/license scope. Not a credible source for: the JSON schema of each individual key
  (only named, not defined, in this entry), migration mechanics for existing preview
  configurations, or adoption data.
- **Scope**: Covers the GA transition of the enterprise-managed settings system, the complete
  key list, enforcement timing (hourly refresh), client/license scope, and the configuration
  path with its backward-compatibility note. Does NOT cover: the schema for `extraKnownMarketplaces`,
  `enabledPlugins`, or `model` individually (only `strictKnownMarketplaces`'s schema has been
  documented in a prior source note); whether GA introduces any breaking changes for existing
  preview configurations; or whether the three earlier preview features
  (`disableBypassPermissionsMode`, `strictKnownMarketplaces`, plugin distribution) changed
  behavior between preview and GA.

## Extracted Claims

### Claim 1: GitHub Enterprise Cloud customers configure AI standards through a `managed-settings.json` file maintained in a `.github-private` repository in a selected organization
- **Evidence**: Lead sentence of the changelog body, consistent across two independent WebFetch
  retrievals of the source.
- **Confidence**: settled (product fact in official changelog; consistent across two
  independent fetches)
- **Quote**: "GitHub Enterprise Cloud customers can configure AI standards through a `managed-settings.json` file maintained in a `.github-private` repository in a selected organization."
- **Our assessment**: This confirms `.github-private` as the settled repository convention
  first documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3
  (`.github-private/.github/copilot/settings.json`). The GA entry's phrasing — "a selected
  organization" — clarifies that the private repository is scoped per-organization within the
  enterprise, not a single enterprise-wide repository, which was implicit but not stated this
  plainly in the June notes.

### Claim 2: The `managed-settings.json` configuration is additive to, not a replacement for, the policies configured in the AI Controls tab of enterprise settings
- **Evidence**: Explicit statement in the changelog body, consistent across both WebFetch
  retrievals.
- **Confidence**: settled (verbatim official statement)
- **Quote**: "The configuration in `managed-settings.json` is in addition to the policies available in the **AI Controls** tab in enterprise settings."
- **Our assessment**: This is the first source in the corpus to explicitly state the
  relationship between the file-based `managed-settings.json` mechanism and the GUI-based AI
  Controls tab: they are complementary layers, not alternatives. Enterprises should treat AI
  Controls as the console-configured policy baseline and `managed-settings.json` as the
  source-controlled, PR-reviewable extension layer on top of it. Prior notes documented the
  file-based mechanism in isolation without clarifying this relationship to the console UI.

### Claim 3: The complete GA schema of `managed-settings.json` supports five optional keys: `extraKnownMarketplaces`, `enabledPlugins`, `strictKnownMarketplaces`, `disableBypassPermissionsMode`, and `model`
- **Evidence**: Both independent WebFetch retrievals list the identical five keys together as
  "optional configuration keys."
- **Confidence**: settled (technical identifiers listed identically across two independent
  fetches; treated as authoritative)
- **Quote**: (no direct verbatim quote of the enumerating sentence recovered — WebFetch
  paraphrased the list intro differently across the two fetches, though the five key names
  themselves were identical in both; see paraphrase above and Extraction Notes)
- **Our assessment**: This is the highest-value claim in this source. Prior corpus notes
  documented `disableBypassPermissionsMode` (`docs-github-copilot-enterprise-bypass-permissions.md`)
  and `strictKnownMarketplaces` (`docs-github-copilot-enterprise-strict-known-marketplaces.md`)
  as if they were the only two named controls added to the system. This GA announcement reveals
  three more keys exist that were never separately announced in a changelog the corpus has
  captured: `extraKnownMarketplaces`, `enabledPlugins`, and `model`. Two of these
  (`extraKnownMarketplaces`, `model`) are genuinely novel to the corpus — no prior source note
  documents an enterprise-enforced Copilot model selection control, despite one prior note
  (`docs-github-copilot-enterprise-bypass-permissions.md`, Guide Impact section) speculating
  about "enterprise-level model selection controls" as a hypothetical future capability. That
  speculation is now confirmed as a real, named, shipping key.

### Claim 4: `extraKnownMarketplaces` is a distinct key from `strictKnownMarketplaces`, implying an additive-allowlist mechanism separate from the restrictive-allowlist mechanism already documented
- **Evidence**: The key appears alongside, and textually distinct from, `strictKnownMarketplaces`
  in the five-key list; no further schema or behavioral description is given in this changelog
  entry.
- **Confidence**: anecdotal (key name and existence are settled facts; the *inferred* semantic
  distinction from `strictKnownMarketplaces` is our interpretation, not stated by the source)
- **Quote**: (no direct quote describing `extraKnownMarketplaces` behavior; the source only
  lists the key name — see Our assessment for our inference)
- **Our assessment**: We infer from the naming pattern (`extra` vs. `strict`) that
  `extraKnownMarketplaces` adds marketplaces to a known-good list (supplementing GitHub's own
  default marketplace set) while `strictKnownMarketplaces` restricts installation to only the
  listed marketplaces (documented in `docs-github-copilot-enterprise-strict-known-marketplaces.md`
  Claim 2 as whitelist semantics: "Copilot will only allow plugins to be installed from the
  marketplaces you've explicitly defined"). This is an inference, not a confirmed fact — the
  changelog does not describe `extraKnownMarketplaces`'s schema or semantics at all. The Assayer
  and Smith should treat this distinction as unconfirmed until a dedicated changelog entry or
  documentation page for `extraKnownMarketplaces` is found.

### Claim 5: `enabledPlugins` is a key that did not appear in any of the three prior enterprise-managed settings changelogs captured in the corpus
- **Evidence**: Absent from the June 5, June 17, and June 25 changelog entries as documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md`, `docs-github-copilot-enterprise-bypass-permissions.md`,
  and `docs-github-copilot-enterprise-strict-known-marketplaces.md` respectively; first appears
  in this July 1 GA entry's key list.
- **Confidence**: emerging (key existence is settled; its behavior/schema is undocumented in
  any source the corpus has captured)
- **Quote**: (no direct quote describing `enabledPlugins` behavior beyond its name appearing in
  the key list)
- **Our assessment**: The June 5 note (`docs-github-copilot-enterprise-managed-plugins-vscode.md`
  Claim 4) documented auto-*install* of plugins/skills, and Claim 5 documented hooks/MCP
  configurations that are "always enabled." `enabledPlugins` may be the plugin-specific analogue
  of that "always enabled" governance pattern — a list of plugins enterprise-enforced as active,
  distinct from auto-install (which pushes plugins to users) or marketplace restriction (which
  gates install sources). This is speculative; no changelog entry documenting `enabledPlugins`
  specifically has been found. Flag for a future source-note pass if GitHub publishes a
  dedicated changelog or docs page for this key.

### Claim 6: The `model` key allows enterprise-managed settings to control which AI model Copilot clients use — the first confirmed enterprise-level model selection control in the corpus
- **Evidence**: Appears in the five-key list alongside the other four documented controls; no
  further schema or behavioral detail given in this changelog entry.
- **Confidence**: emerging (key existence and name are settled facts from the official
  changelog; the exact mechanism — e.g., whether it pins a single model, provides an allowlist,
  or sets a default — is undocumented)
- **Quote**: (no direct quote describing `model` key behavior; only the key name is given)
- **Our assessment**: This is significant new ground. `docs-github-copilot-enterprise-bypass-permissions.md`
  (Guide Impact, Chapter 05) previously speculated about "enterprise-level model selection
  controls" as a governance lever organizations might want, listing it as a hypothetical
  alongside CCA custom properties — but no source had confirmed such a control existed. This
  changelog confirms a `model` key ships in `managed-settings.json`, but does not describe its
  values or semantics (single model pin? allowlist of models? default with user override?).
  For Ch02/Ch05: flag this as a newly confirmed but under-documented enterprise control —
  practitioners should consult the linked configuration documentation directly for the `model`
  key's schema before relying on guide coverage, since this changelog entry does not provide it.

### Claim 7: Configuration in `managed-settings.json` takes precedence over user-level client configuration and is fetched server-side, cached in memory, and refreshed hourly
- **Evidence**: WebFetch retrieval #1 states this behavior; not fully corroborated verbatim by
  retrieval #2, which focused on other sections.
- **Confidence**: emerging (behavior described in one of two independent fetches; not
  contradicted by the second fetch, but also not independently confirmed by it)
- **Quote**: (no direct verbatim quote recovered for the precedence/refresh mechanism; see
  Extraction Notes)
- **Our assessment**: If accurate, the hourly refresh cadence is a new operational detail not
  present in any prior enterprise-managed settings note — the June 25 note
  (`docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 6) documented an
  authentication-cycle enforcement model ("the next time they authenticate from a supported
  client") for `strictKnownMarketplaces` specifically. An hourly refresh is a materially
  different (and faster) propagation model than "next authentication." This may mean GA
  introduced a faster refresh mechanism than the preview-era authentication-cycle model, or it
  may mean the two mechanisms coexist (hourly refresh for an authenticated session, full
  re-fetch at next authentication). This is not resolved by the available fetches and should be
  verified against the live source and linked documentation before the guide asserts a specific
  refresh cadence.

### Claim 8: The primary configuration path is `copilot/managed-settings.json`, in the `.github-private` repository, with backward compatibility for the older `.github/copilot/settings.json` path
- **Evidence**: Stated identically in both independent WebFetch retrievals.
- **Confidence**: settled (path and backward-compatibility relationship consistent across two
  fetches and consistent with the June 17 note's Claim 4 forward announcement of this same path
  change)
- **Quote**: "The path `copilot/managed-settings.json` maintains backward compatibility with `.github/copilot/settings.json`."
- **Our assessment**: This confirms, at GA, the path migration that `docs-github-copilot-enterprise-bypass-permissions.md`
  Claim 4 announced during preview (June 17): "A new preferred configuration path
  `copilot/managed-settings.json` has been introduced, with backward compatibility maintained
  for `.github/copilot/settings.json`." The GA entry settles what was an in-flux preview
  behavior — `copilot/managed-settings.json` is now the stable, GA-supported primary path, and
  `.github-private/.github/copilot/settings.json` (the original June 5 path) is the
  backward-compatible fallback. Ch02 documentation should now present
  `copilot/managed-settings.json` as the primary path without hedging language about "preview,"
  since GA confirms it.

### Claim 9: As of GA, enforcement applies to VS Code and Copilot CLI clients for users with a Copilot Business or Copilot Enterprise license issued from the enterprise or one of its organizations
- **Evidence**: Stated in both retrievals, closely matching wording.
- **Confidence**: settled (license/client scope consistent with all three prior preview notes
  and confirmed at GA)
- **Quote**: "Today the configuration defined in `managed-settings.json` is enforced in VS Code and Copilot CLI whenever a user has a Copilot Business or Copilot Enterprise license issued from the enterprise or one of its organizations."
- **Our assessment**: The word "Today" in the source's own phrasing is notable — it signals
  GitHub is flagging VS Code/CLI as the *current* client scope, implying more clients (e.g.,
  JetBrains, where `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` already
  references enterprise-managed bypass-permissions framing) may be added later. This is our
  inference from the word choice, not a stated roadmap item in the source. License scope
  (Business/Enterprise) is unchanged from all three June preview notes.

## Concrete Artifacts

### Complete `managed-settings.json` Key List (GA, July 1, 2026)

```
File:        managed-settings.json
Location:    copilot/managed-settings.json (primary, GA path)
             .github-private repository, selected organization
Fallback:    .github/copilot/settings.json (backward-compatible legacy path)
Status:      Generally Available (as of 2026-07-01)

Supported keys (all optional):
  1. extraKnownMarketplaces        — NEW to corpus; schema/semantics undocumented
  2. enabledPlugins                — NEW to corpus; schema/semantics undocumented
  3. strictKnownMarketplaces       — documented: docs-github-copilot-enterprise-strict-known-marketplaces.md
  4. disableBypassPermissionsMode — documented: docs-github-copilot-enterprise-bypass-permissions.md
  5. model                         — NEW to corpus; schema/semantics undocumented

Enforcement:  VS Code and Copilot CLI clients
License:      Copilot Business or Copilot Enterprise (enterprise or org-issued)
Relationship: Additive to AI Controls tab policies (not a replacement)

Getting started (per changelog):
  1. Select an organization in enterprise settings' AI Controls tab
  2. Create copilot/managed-settings.json in that org's .github-private repo
  3. Add supported keys, commit to the default branch
```

*Source: GitHub Copilot changelog, July 1, 2026, cross-referenced against
`docs-github-copilot-enterprise-managed-plugins-vscode.md`,
`docs-github-copilot-enterprise-bypass-permissions.md`, and
`docs-github-copilot-enterprise-strict-known-marketplaces.md` for which of the
five keys already have corpus documentation.*

### Enterprise-Managed Settings Timeline (updated through GA)

```
May 2026:     Copilot CLI enterprise plugin distribution, public preview
              (referenced in June 5 changelog; no dedicated corpus note)
June 5, 2026: VS Code enterprise-managed plugins, public preview
              Keys revealed: plugin marketplace definition, hooks/MCP "always enabled"
              Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
June 17, 2026: disableBypassPermissionsMode added; new preferred path
              copilot/managed-settings.json announced (preview)
              Source: docs-github-copilot-enterprise-bypass-permissions.md
June 25, 2026: strictKnownMarketplaces added (whitelist marketplace restriction)
              Source: docs-github-copilot-enterprise-strict-known-marketplaces.md
July 1, 2026: GA. File renamed/settled as managed-settings.json at
              copilot/managed-settings.json. Full 5-key schema disclosed for the
              first time, revealing extraKnownMarketplaces, enabledPlugins, and
              model as previously undocumented keys.
              Source: THIS NOTE (docs-github-copilot-enterprise-managed-settings-ga.md)
```

*Source: synthesis across the four enterprise-managed-settings source notes in the corpus.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3: The `.github-private`
    repository convention for enterprise Copilot configuration is reaffirmed at GA (Claim 1 of
    this note).
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 4: The preview-era announcement
    of `copilot/managed-settings.json` as a new preferred path, with `.github/copilot/settings.json`
    backward compatibility, is confirmed as the settled GA path (Claim 8 of this note).
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 5: License scope
    (Copilot Business or Enterprise) and automatic client application are reaffirmed at GA
    (Claim 9 of this note).

- **Contradicts**: Possible tension, not a full contradiction, with
  `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 6, which documents
  settings taking effect "the next time they authenticate from a supported client." This GA
  note's Claim 7 describes an hourly-refresh, in-memory caching model, which is a different
  propagation cadence than "next authentication." The two claims describe what could be the
  same underlying mechanism worded differently, or two genuinely different propagation models
  for different keys. Given the low confidence of Claim 7 (only one of two WebFetch retrievals
  surfaced this detail) and the plausible reading that these are non-conflicting (hourly refresh
  of an already-authenticated session vs. full settings re-fetch at next login), this does not
  clear the bar in MINER.md §4a for filing a contradiction issue — the evidence for Claim 7 is
  too thin to constitute a "real claim" in tension with the June 25 note's authentication-cycle
  claim. Flagging here per the cross-reference requirement; no contradiction issue filed. A
  future source note with stronger verbatim sourcing on the refresh mechanism should resolve this.

- **Extends**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
    `docs-github-copilot-enterprise-bypass-permissions.md`, and
    `docs-github-copilot-enterprise-strict-known-marketplaces.md`: This note extends all three
    by disclosing the complete GA key schema (5 keys) where each prior note only documented one
    key in isolation as it was announced. This is the first source that lets the corpus see the
    full shape of the `managed-settings.json` schema at once.

- **Novel**:
  - `extraKnownMarketplaces` key: not documented in any prior corpus source (Claim 3, Claim 4).
  - `enabledPlugins` key: not documented in any prior corpus source (Claim 3, Claim 5).
  - `model` key as a confirmed enterprise-managed control: previously only speculated as a
    hypothetical in `docs-github-copilot-enterprise-bypass-permissions.md`'s Guide Impact
    section; now confirmed to exist as a named, shipping key (Claim 3, Claim 6).
  - GA status itself: the enterprise-managed settings system transitions from public preview
    (all three June notes) to generally available (Claim 1, Claim 8, Claim 9) — the first GA
    confirmation in the corpus for this system.
  - Explicit relationship between `managed-settings.json` and the AI Controls tab (Claim 2):
    not previously stated in any prior note.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Update the enterprise-managed settings coverage to reflect GA status: drop "public preview"
    hedging language for `disableBypassPermissionsMode`, `strictKnownMarketplaces`, and plugin
    distribution/hooks/MCP — these are now GA as of 2026-07-01.
  - Add the complete 5-key schema (see Concrete Artifacts → Complete `managed-settings.json` Key
    List) as the canonical reference table, explicitly marking `extraKnownMarketplaces`,
    `enabledPlugins`, and `model` as newly disclosed keys whose detailed schema/semantics are
    not yet documented in this corpus — flag these for a follow-up source-mining pass rather
    than asserting behavior the guide cannot back with evidence.
  - Update the primary configuration path guidance to `copilot/managed-settings.json` (GA,
    unhedged) with `.github/copilot/settings.json` as the legacy backward-compatible fallback.
  - Document the stated relationship between `managed-settings.json` and the AI Controls tab
    (additive, not a replacement) — this clarifies a relationship the guide has not previously
    had a source for.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Retire the "hypothetical enterprise-level model selection controls" framing used in
    `docs-github-copilot-enterprise-bypass-permissions.md`'s prior Guide Impact section — the
    `model` key confirms this is real, not hypothetical. Frame it as a fifth concrete enterprise
    governance lever (alongside CCA custom properties, hooks/MCP enforcement, bypass permissions,
    and marketplace restriction), while being explicit that the guide does not yet know the
    key's exact schema or semantics.

## Extraction Notes

1. **WebFetch AI-summarization limitation, mitigated by two independent fetches**: As with all
   prior enterprise-managed-settings notes in this corpus, WebFetch processes the source HTML
   through an AI model before returning text, so no returned text can be verified as
   character-for-character verbatim without independent access to the raw HTML. Two independent
   WebFetch calls were made with different prompts (one summary-oriented, one verbatim-oriented).
   Quotes used in Claims 1, 2, 8, and 9 appeared with matching or near-matching wording across
   both retrievals and are used as quotes on that basis. Claims 3 (key list), 4, 5, 6, and 7
   either lacked a verbatim sentence to quote or were only surfaced by one of the two fetches,
   and are marked accordingly with no fabricated quote.
2. **Key list is the highest-confidence, highest-value extraction**: The five-key list
   (`extraKnownMarketplaces`, `enabledPlugins`, `strictKnownMarketplaces`,
   `disableBypassPermissionsMode`, `model`) appeared identically in both independent WebFetch
   retrievals, which is why it is rated settled despite lacking a single verbatim quoted
   sentence — the key names themselves are technical identifiers unlikely to be
   hallucinated identically by two separate summarization passes.
3. **No dedicated documentation for the three new keys found**: A linked documentation page
   (`docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings`)
   is referenced in the changelog itself but was not separately fetched for this note, since the
   Prospector's triage flagged this as low/medium priority incremental coverage. A future Miner
   pass fetching that documentation page directly would likely resolve the open questions in
   Claims 4, 5, and 6 (schema for `extraKnownMarketplaces`, `enabledPlugins`, and `model`).
4. **Short changelog (~150 words per the page's own "2 minute read" estimate)**: Consistent with
   the brevity of the three prior enterprise-managed-settings changelog entries in the corpus.
   Nine claims were extracted, which is more than the roughly 150 words would suggest for a
   single linear reading — this is because several claims (4, 5, 6, 7) are explicitly flagged
   as inferences or partially-corroborated details rather than direct restatements of settled
   sentences, in keeping with MINER.md §2a's instruction to separate quote from inference.
5. **No contradiction issue filed**: See Cross-References → Contradicts above. The tension
   between this note's hourly-refresh claim (Claim 7, low confidence) and the June 25 note's
   authentication-cycle claim is flagged in-note per MINER.md §4, but does not meet the bar in
   §4a for a formal contradiction issue given how thin the evidence for Claim 7 is.
