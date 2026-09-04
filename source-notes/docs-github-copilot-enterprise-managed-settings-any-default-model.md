---
source_url: https://github.blog/changelog/2026-09-02-enterprise-managed-settings-support-any-default-model
source_type: docs
title: "Enterprise-managed settings support any default model"
author: GitHub (official changelog)
date_published: 2026-09-02
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: settled
issue: "#3221"
---

# Enterprise-Managed Settings Support Any Default Model

> GitHub's September 2, 2026 changelog widens the enterprise `model` key in
> `managed-settings.json` from an `auto`-only value (established July 1, 2026)
> to any specific Copilot model identifier, and reconfirms the `overridable` /
> `team-mappings.json` team-specialization mechanism (established August 3,
> 2026) applies to this key — while a docs-page note clarifies that `model`
> supersedes the older, still-backward-compatible nested `permissions.model`
> key name.

## Source Context

- **Type**: docs (GitHub official product changelog, September 2, 2026; tagged
  `client-apps`, `copilot`, `enterprise-management-tools`). One linked
  documentation page followed per MINER.md §1: the `#model` anchor of the
  enterprise-managed-settings reference at
  `docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings#model`,
  fetched across two separate WebFetch calls that returned consistent wording
  for the setting description, valid values, `overridable` syntax, and the
  `permissions.model` deprecation note. The changelog itself was fetched
  across three separate WebFetch calls, all returning consistent wording for
  the opening paragraph, the `overridable`/`team-mappings.json` sentence, the
  GA/availability sentence, and the "all other users inherit" sentence — this
  cross-fetch consistency is the basis for rating changelog claims `settled`
  despite not raw-HTML-verifying via `curl` (see Extraction Notes). The linked
  Community discussion (`orgs/community/discussions/199139`) is the same
  general enterprise-managed-settings thread already characterized as
  off-topic-for-specific-features in
  `docs-github-copilot-enterprise-auto-model-default.md` (Extraction Note 3)
  and `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
  (Extraction Note 5); not re-fetched here for the same reason.
- **Author credibility**: GitHub engineering team announcing a production
  capability extension to a `managed-settings.json` key that has been the
  subject of two prior corpus source notes (July 1 and August 3, 2026 — see
  Cross-References). Authoritative for: the existence and accepted values of
  the `model` key, the `overridable`/`team-mappings.json` mechanism as applied
  to this specific key, the GA/client scope, and the `permissions.model` →
  `model` naming migration. Not a credible source for: which specific model
  identifiers are currently valid (the docs page gives exactly one example,
  `"kimi-k-3"`), what happens if an enterprise sets an invalid or
  since-deprecated model identifier as the default, or any client-version
  floor for this expanded capability (not stated in either the changelog or
  the linked docs excerpt obtained).
- **Scope**: A value-range expansion of the existing `model` key in
  `managed-settings.json` (previously `auto`-only, per
  `docs-github-copilot-enterprise-auto-model-default.md`) to accept any
  specific model identifier, plus confirmation that the key remains
  `overridable` at the enterprise-team level via `team-mappings.json`. Covers:
  the setting description, valid values, the `overridable` syntax, team-level
  override behavior, GA/client scope, and the top-level `model` vs. nested
  `permissions.model` naming history. Does NOT cover: a list of valid model
  identifiers beyond the one example given, invalid-model-identifier error
  handling, client version requirements, whether this changes anything about
  the `"unmanaged"` team-level opt-out sentinel already documented for this
  key, or interaction with the global default-availability policy
  (`docs-github-copilot-global-model-policy-ga.md`) that governs whether a
  named model is available to select at all.

## Extracted Claims

### Claim 1: Enterprise administrators can set their preferred Copilot model as the default for new conversations through enterprise-managed settings

- **Evidence**: Official GitHub changelog, opening paragraph. Consistent
  across three independent WebFetch fetches of the changelog page.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "You can now set your preferred GitHub Copilot model as the
  default for new conversations through enterprise-managed settings. This
  lets you choose the default model that best fits your workflows."
- **Our assessment**: This is the headline capability and the direct answer
  to the Prospector's repeated triage question about scope. It confirms the
  issue title's "any default model" framing at the level of the changelog's
  own opening statement — the enterprise default is no longer limited to a
  single mode (`auto`) but to "your preferred" model generally. For Ch02/Ch04:
  this is a value-range expansion of an existing governance lever
  (`docs-github-copilot-enterprise-auto-model-default.md`), not a new
  mechanism.

### Claim 2: The `model` key accepts either `"auto"` or a specific model identifier and version as its value, with a named example of setting a specific model as the enterprise default

- **Evidence**: Linked documentation page (`enterprise-managed-settings#model`
  anchor), setting description and valid-values section. Consistent across
  two independent WebFetch fetches.
- **Confidence**: settled (value range stated directly on the linked docs
  page; the two independent fetches returned matching wording for the
  specific-model example, though this is a secondary docs page rather than
  the changelog itself)
- **Quote**: "Set `model` to a specific model and version to make that model
  the default for new conversations, for example `\"kimi-k-3\"`."
- **Our assessment**: This is the concrete mechanism behind Claim 1 and the
  central novelty of this source relative to
  `docs-github-copilot-enterprise-auto-model-default.md`, whose Claim 1
  documented `model` accepting only the literal value `auto` as of July 1,
  2026. This source shows the same key's accepted-value set has since grown
  to include arbitrary model identifiers. For Ch02: the guide's
  `managed-settings.json` schema reference should update the `model` key's
  documented value type from "the literal string `auto`" to "either `auto` or
  a specific model identifier," and flag that the only confirmed example
  identifier in the corpus is `"kimi-k-3"` — the guide should not assume a
  specific enumerated list of valid models without checking GitHub's live
  supported-models documentation, consistent with the caution already applied
  to CLI auto's model pool in `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`.

### Claim 3: The `model` key can be marked `overridable` in `managed-settings.json`, and teams can be given their own preferred default model via `team-mappings.json`

- **Evidence**: Official changelog, second body sentence. Consistent across
  three independent WebFetch fetches.
- **Confidence**: settled (mechanism stated directly in official changelog)
- **Quote**: "Set the `model` key as `overridable` and update team
  configuration files in `team-mappings.json` so that enterprise teams can
  choose their own preferred default model."
- **Our assessment**: This directly reconfirms
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`'s
  Claim 6, which named `model` (alongside `disableBypassPermissionsMode`) as
  the flagship worked example of the `overridable`/`team-mappings.json`
  mechanism on August 3, 2026 — but that note's example showed teams setting
  `"model": "unmanaged"` to opt out of the enterprise default entirely. This
  changelog is the first to state explicitly that the team-level override
  value itself can now be a specific preferred model (not just the enterprise
  auto-only default, and not just the `"unmanaged"` opt-out sentinel), which
  follows directly from Claim 2's value-range expansion applying to the
  team-level override just as much as the enterprise-level default.

### Claim 4: Model defaults in managed settings are generally available with Copilot Business and Copilot Enterprise across the GitHub Copilot app, Copilot CLI, and Visual Studio Code

- **Evidence**: Official changelog, availability statement. Consistent across
  three independent WebFetch fetches.
- **Confidence**: settled (GA scope stated directly in official changelog)
- **Quote**: "Model defaults in managed settings are generally available with
  Copilot Business and Copilot Enterprise in the GitHub Copilot app, Copilot
  CLI, and Visual Studio Code."
- **Our assessment**: This client list (Copilot app, CLI, VS Code) matches the
  dual/triple-client enforcement pattern already established for prior
  `managed-settings.json` capabilities, though it explicitly states "the
  GitHub Copilot app" as a named client — a broader list than the VS
  Code+CLI pairing documented for the July 1 `model: auto` note, and
  consistent with (though not identical in wording to) the four-client list
  ("VS Code, Copilot CLI, the Copilot App, and Copilot cloud agent") stated
  for team specialization generally in the August 3 note's Claim 11. This
  changelog does not mention "Copilot cloud agent" for the model-default
  capability specifically — an open scope question, not a contradiction (see
  Cross-References).

### Claim 5: Users not covered by a team-specific override inherit the enterprise-wide default model

- **Evidence**: Official changelog, final body sentence. Consistent across
  three independent WebFetch fetches.
- **Confidence**: settled (fallback behavior stated directly in official
  changelog)
- **Quote**: "All other users inherit your enterprise default."
- **Our assessment**: This restates the same fallback semantics already
  documented generically for `overridable` keys in
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
  Claim 4 ("An overridable key uses the team's value when set or falls back
  to your enterprise default when the team leaves it unset") — applied here
  specifically to `model`. No new fallback mechanism; this is confirmation
  that `model`'s override behavior follows the general `overridable` rule
  rather than a key-specific exception.

### Claim 6: This key is overridable by enterprise team mapping; the docs page shows the marker syntax as `{ "overridable": "auto" }` in `managed-settings.json`

- **Evidence**: Linked documentation page, "Overridable Flag" section.
  Consistent across two independent WebFetch fetches.
- **Confidence**: settled (syntax stated directly on the linked docs page,
  cross-fetch consistent, though not raw-HTML-verified — see Extraction
  Notes)
- **Quote**: "This key is overridable by enterprise team mapping. In your
  `managed-settings.json`, use the `{ \"overridable\": \"auto\" }` syntax to
  specialize the key's configuration on a per-team basis."
- **Our assessment**: The example uses `"auto"` as the overridable marker
  value specifically (i.e., the enterprise default being marked overridable
  in this example is `auto`, not a named model) — consistent with the
  general `{ "overridable": <enterprise-default-value> }` syntax documented
  in `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
  Claim 4, where `<value>` is whatever the enterprise default currently is.
  This does not indicate the marker syntax is restricted to `"auto"`; per
  Claim 2, a specific model identifier could equally be the marked
  enterprise-default value.

### Claim 7: `model` was originally documented as the nested key `permissions.model`; clients still read the nested value when the top-level key is absent, but new configurations should use the top-level `model` key

- **Evidence**: Linked documentation page, note callout. Consistent across
  two independent WebFetch fetches.
- **Confidence**: settled (naming-migration note stated directly on the
  linked docs page)
- **Quote**: "`model` was originally documented as `permissions.model`.
  Clients still read the nested `permissions.model` value when the top-level
  `model` key is absent, but you should use the top-level `model` key in new
  configurations."
- **Our assessment**: This resolves an open naming ambiguity in the corpus.
  `docs-github-copilot-enterprise-auto-model-default.md` (Claim 8, `emerging`
  confidence) documented `model` nested under a `permissions` object based on
  a July 1 linked-docs fetch, and
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
  (Claim 12, `emerging` confidence) independently documented the `overridable`
  mechanism as applying to `permissions.model` specifically, based on an
  August 3 linked-docs fetch. This September 2 docs page explicitly confirms
  those two `emerging`-rated claims were accurate for their time — but also
  states the schema has since moved the canonical key to the top level
  (`model`, not `permissions.model`), with the nested form retained only for
  backward compatibility. This is presented as the docs page's own
  explanation of an intentional naming migration, not a disagreement between
  sources describing the same point in time — no contradiction issue filed
  (see Cross-References). For Ch02: the guide's `managed-settings.json`
  schema reference should cite the top-level `model` key as canonical going
  forward, with a note that `permissions.model` remains a supported legacy
  form and that clients read the nested value only when the top-level key is
  absent (not merged or preferred — the top-level key wins if both are
  present, per the "when absent" phrasing).

## Concrete Artifacts

### Changelog body (reconstructed from three consistent WebFetch fetches, September 2, 2026)

```
Title: Enterprise-managed settings support any default model
Published: September 2, 2026
Tags: client-apps, copilot, enterprise-management-tools

You can now set your preferred GitHub Copilot model as the default for new
conversations through enterprise-managed settings. This lets you choose the
default model that best fits your workflows.

Set the `model` key as `overridable` and update team configuration files in
`team-mappings.json` so that enterprise teams can choose their own preferred
default model.

Model defaults in managed settings are generally available with Copilot
Business and Copilot Enterprise in the GitHub Copilot app, Copilot CLI, and
Visual Studio Code.

All other users inherit your enterprise default.

Learn more in our docs about enterprise managed settings
  -> https://docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings#model
or join the discussion in the GitHub Community
  -> https://github.com/orgs/community/discussions/199139
```
Source: three independent WebFetch (AI-summarizing) fetches of
https://github.blog/changelog/2026-09-02-enterprise-managed-settings-support-any-default-model,
all returning consistent wording for every sentence above. Not raw-HTML
`curl`-verified — see Extraction Notes.

### `managed-settings.json` — `model` key reference (from linked docs page, `#model` anchor)

```json
{
  "model": "auto"
}
```

Setting description: "Sets your preferred model as the default for new
conversations"

Valid values:
- `"auto"` — auto model selection as the default for new sessions
- A specific model identifier, e.g. `"kimi-k-3"` — that model becomes the
  default for new conversations

Overridable syntax:
  { "overridable": "auto" }
  (per-team specialization marker; the marked value is whatever the
  enterprise default currently is — "auto" in the docs page's own example)

Team-level override (per changelog):
  Teams set their own value in team-mappings.json-routed team files,
  including a specific model identifier per Claim 2/3, or "unmanaged" to
  opt out entirely (per the August 3 team-specialization note's Claim 6).

Legacy key note:
  Top-level `model` supersedes the originally-documented nested
  `permissions.model`. Clients read `permissions.model` only when the
  top-level `model` key is absent. Use the top-level key in new configs.
```
Source: two independent WebFetch (AI-summarizing) fetches of
https://docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings#model,
consistent across both fetches. Not raw-HTML `curl`-verified — see
Extraction Notes.

### Enterprise-Managed Settings Capability Map (updated to September 2, 2026)

```
Configuration surface: .github-private source-org repository
Enterprise file:  copilot/managed-settings.json  (legacy compat: .github/copilot/settings.json)
Team files:       copilot/teams/*.json
Team routing:     team-mappings.json
License required: Copilot Business or Copilot Enterprise

Capabilities announced to date (chronological):
1. Plugin distribution (June 5, 2026) — VS Code 1.122+
2. Hooks/MCP "always enabled" governance (June 5, 2026) — VS Code 1.122+
3. disableBypassPermissionsMode (June 17, 2026) — VS Code 1.122+
4. strictKnownMarketplaces (June 25, 2026, public preview)
5. model: auto default only (July 1, 2026) — VS Code 1.126+
   Source: docs-github-copilot-enterprise-auto-model-default.md
6. Team-level specialization / overridable / team-mappings.json
   (August 3, 2026) — VS Code, CLI, Copilot App, Copilot cloud agent
   Source: docs-github-copilot-enterprise-team-specialization-managed-settings.md
7. Global default-availability policy for GA models, 4-state taxonomy
   (announced July 2026, enforcement rolled out through Sept 1, 2026)
   Source: docs-github-copilot-global-model-policy-ga.md
8. model: any specific identifier (not just auto) as enterprise/team
   default (September 2, 2026) — GitHub Copilot app, CLI, VS Code
   ← THIS NOTE
   Source: docs-github-copilot-enterprise-managed-settings-any-default-model.md

Verification path (prior capabilities): Agents page -> AI controls ->
  GitHub Enterprise settings (not independently reconfirmed in this
  changelog; presumed same surface, not verified)
```
Source: synthesis across corpus source notes for this family, listed in
chronological order of changelog publication.

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-auto-model-default.md` (issue #1542,
    Claim 1): both sources agree the `model` key in `managed-settings.json`
    sets the enterprise-wide default model-selection starting point for new
    conversations; this source extends the value range that key accepts.
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    (issue #2473, Claims 4, 6): both sources agree `model` is one of the
    named `overridable` keys with team-level specialization via
    `team-mappings.json`; this source reconfirms the mechanism six weeks
    later, extended to specific-model (not just `"unmanaged"` or `"auto"`)
    team-level values.

- **Extends**:
  - `docs-github-copilot-enterprise-auto-model-default.md` (issue #1542,
    Claim 1): that source documented `model` accepting only the literal
    value `auto` as of July 1, 2026 ("Enterprise administrators can now set
    `model` to `auto`..."). This source shows the same key now accepts any
    specific model identifier as of September 2, 2026 — a value-range
    expansion of an existing capability, not a new key or mechanism. This is
    read as product evolution over two months, not a disagreement about the
    same point in time; no contradiction issue filed.
  - `docs-github-copilot-enterprise-auto-model-default.md` (issue #1542,
    Claim 8, `emerging`) and
    `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    (issue #2473, Claim 12, `emerging`): both notes tentatively documented
    `model` as nested under a `permissions` object (`permissions.model`)
    based on AI-summarized secondary docs-page fetches, explicitly flagged
    as unverified/emerging at the time. This source's Claim 7 resolves that
    ambiguity with an explicit docs-page note: `permissions.model` was the
    original (now legacy, backward-compatible) location, and the current
    canonical key is top-level `model`. Both earlier `emerging` claims are
    confirmed accurate for their respective extraction dates, not
    contradicted — the schema location changed between documentation
    revisions, which the docs page itself narrates.
  - `docs-github-copilot-global-model-policy-ga.md` (issue #2992): that
    source documents an upstream governance layer — whether a given model is
    *available* to select at all, via the global default-availability policy
    and its four-state taxonomy. This source's expanded `model` default
    setting is a downstream layer: which *available* model a new conversation
    starts with. An enterprise setting `model` to a specific identifier under
    this source's mechanism should first confirm that identifier is not
    excluded by the global policy's exclusion list (pre-GA models, named
    open-weight models, models outside GitHub's data retention agreement, or
    data-residency/FedRAMP-restricted models) — neither source states this
    interaction explicitly, so it is a gap for the guide to flag rather than
    a documented dependency.

- **Contradicts**: None. This is a strictly additive value-range expansion of
  an existing `managed-settings.json` key, consistent with the established
  pattern in this source family (see `docs-github-copilot-global-model-policy-ga.md`
  Cross-References for the same "product evolution, not contradiction"
  reasoning applied to the two-state → four-state model-availability
  taxonomy). No contradiction issue required per MINER.md §4a.

- **Novel**:
  - First corpus source to document the `model` key accepting a specific
    model identifier (not just `"auto"`) as an enterprise or team default.
  - First corpus source to explicitly resolve the `model` vs.
    `permissions.model` naming ambiguity left `emerging` in two prior source
    notes, via the docs page's own backward-compatibility note.
  - First corpus source to name a specific model identifier
    (`"kimi-k-3"`) as a valid `model` default value.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Update the
  documented `managed-settings.json` `model` key's value type from
  "the literal string `auto`" to "either `auto` or a specific model
  identifier and version." Cite the top-level `model` key as canonical, note
  `permissions.model` as a backward-compatible legacy form read only when the
  top-level key is absent, and flag that the corpus has exactly one confirmed
  example model identifier (`"kimi-k-3"`) — do not present a broader list of
  valid identifiers without checking GitHub's live supported-models
  documentation.
- **Chapter 04/05 (Model Selection and Cost Management / Enterprise
  Governance)**: Add the specific-model enterprise/team default as a
  governance lever distinct from (and composable with) the global
  default-availability policy (`docs-github-copilot-global-model-policy-ga.md`):
  enterprises can now pre-select a specific cost- or capability-appropriate
  model as the starting point for new conversations at the enterprise level,
  with team-level exceptions via `overridable`/`team-mappings.json`, so long
  as the chosen model is not excluded by the global availability policy's
  exclusion list. Flag the unresolved interaction between these two layers
  (this note's "Extends" entry) as an open question worth a future source or
  Smith synthesis pass if GitHub documents an explicit precedence rule.

## Extraction Notes

1. **No raw-HTML `curl` verification performed**: unlike
   `docs-github-copilot-global-model-policy-ga.md`, this note relies entirely
   on WebFetch's AI-summarizing fetch (the sandboxed environment's `curl` to
   github.blog and docs.github.com returned no output when attempted). Cross-fetch
   consistency was used as the confidence signal instead: the changelog was
   fetched three separate times with three differently-scoped prompts, and
   the linked docs page was fetched twice, with all overlapping sentences
   returned identically each time. This is a weaker verification method than
   raw HTML but stronger than a single AI-summarized fetch (the basis for
   `emerging` ratings in the two prior notes in this family). The Assayer
   should spot-check the quotes in Claims 1–7 directly against the live URLs.
2. **Community discussion not fetched**: the linked discussion
   (`orgs/community/discussions/199139`) was previously characterized as the
   general enterprise-managed-settings thread, off-topic for any single
   feature in this family, by two prior source notes. Not re-fetched here for
   the same reason; a future miner covering a subsequent changelog in this
   family should check whether any discussion specific to the any-model
   expansion has since appeared there.
3. **Docs page did not surface GA/preview status, error handling for invalid
   model identifiers, or client version requirements** despite being asked
   directly for these in a follow-up WebFetch prompt — treated as an honest
   "not stated" rather than inferred from the GA language in the changelog
   body (Claim 4), which covers the `model` default capability generally but
   was not cross-checked against a version-requirements table the way the
   July 1 note's VS Code 1.126+ floor was.
4. **No contradictions found**: this source is additive to the existing
   `managed-settings.json`/`model` corpus and explicitly self-resolves a
   naming ambiguity two prior notes had flagged as `emerging`. See
   Cross-References for the full reasoning.
