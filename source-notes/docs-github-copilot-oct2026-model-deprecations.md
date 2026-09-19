---
source_url: https://github.blog/changelog/2026-09-18-upcoming-deprecation-of-selected-github-copilot-models-in-mid-october
source_type: docs
title: "Upcoming deprecation of selected GitHub Copilot models in mid-October"
author: GitHub (official changelog)
date_published: 2026-09-18
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: settled
issue: "#3558"
---

# Upcoming Deprecation of Selected GitHub Copilot Models in Mid-October

> GitHub's September 18, 2026 changelog retiring six models — Gemini 3.7 Flash,
> GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5 mini, and Grok 4.5 — from all Copilot
> experiences on October 19, 2026, with two many-to-one successor convergences
> onto GPT-5.6 Sol and GPT-5.6 Luna, the first evidence anywhere in the corpus
> that Grok models were ever part of GitHub Copilot's roster, and the first
> deprecation notice in this corpus family to describe successor-model
> enablement as automatic-by-default rather than requiring proactive admin
> action — a direct downstream effect of the global default-enablement policy
> documented in `docs-github-copilot-global-model-policy-ga.md`.

## Source Context

- **Type**: docs (GitHub official product changelog, September 18, 2026; ~140
  words of primary announcement text, "1 minute read," category-tagged
  "Retired" — confirmed via direct raw-HTML fetch with `curl`, not just a
  WebFetch AI summary, which was run first and found to have under-reported
  the deprecation table by one row — see Extraction Notes)
- **Author credibility**: GitHub engineering team. Authoritative for the
  deprecation date, per-model successor designations, affected surfaces, and
  the enterprise admin default-enablement mechanism. Not a source for
  capability comparisons between deprecated and replacement models, cost
  implications of migration, or why these six models across three providers
  are being retired together.
- **Scope**: Deprecation of six named models — spanning Google (Gemini),
  OpenAI (GPT), and xAI (Grok) — from "all GitHub Copilot experiences
  (including Copilot Chat, inline edits, ask and agent modes, and code
  completions)," effective October 19, 2026. Covers the successor model(s)
  for each, the default-enablement mechanism for Enterprise/Business
  customers, and the auto-removal behavior. Does NOT cover: why these
  particular six models are being retired together, capability differences
  between deprecated and replacement models, cost implications of the
  GPT-5.4 → GPT-5.6 Sol and GPT-5.4 mini/GPT-5 mini → GPT-5.6 Luna
  migrations, or which specific Copilot surfaces (CLI, IDEs, cloud agent,
  Chat) previously exposed Grok 4.5 at all.

## Extracted Claims

### Claim 1: Six models are deprecated across all GitHub Copilot experiences effective October 19, 2026, with two many-to-one successor convergences: Gemini 3.7 Flash → Gemini 3.8 Flash; GPT-5.5 → GPT-5.6 Sol; GPT-5.4 → GPT-5.6 Sol; GPT-5.4 mini → GPT-5.6 Luna; GPT-5 mini → GPT-5.6 Luna; Grok 4.5 → Grok 4.6

- **Evidence**: Official GitHub Copilot changelog table, published September
  18, 2026, fetched directly from raw page HTML via `curl`.
- **Confidence**: settled (authoritative product fact — dates and successors
  stated directly in a structured table)
- **Quote**: "We will deprecate the following models across all GitHub
  Copilot experiences (including Copilot Chat, inline edits, ask and agent
  modes, and code completions) on October 19th, 2026:" followed by the table
  rows "Gemini 3.7 Flash | 2026-10-19 | Gemini 3.8 Flash", "GPT-5.5 |
  2026-10-19 | GPT-5.6 Sol", "GPT-5.4 | 2026-10-19 | GPT-5.6 Sol", "GPT-5.4
  mini | 2026-10-19 | GPT-5.6 Luna", "GPT-5 mini | 2026-10-19 | GPT-5.6
  Luna", "Grok 4.5 | 2026-10-19 | Grok 4.6"
- **Our assessment**: This is the seventh Copilot model deprecation notice in
  the corpus's deprecation family (after `docs-github-copilot-gpt52-deprecation.md`,
  `docs-github-copilot-gpt41-deprecation.md`,
  `docs-github-copilot-claude-sonnet4-deprecation.md`,
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`,
  `docs-github-copilot-aug2026-model-deprecations.md`, and
  `docs-github-copilot-selected-models-deprecated-sept2026.md`) and the first
  to include an xAI/Grok model. It is also the first notice in the family to
  contain two separate many-to-one successor convergences within a single
  table: GPT-5.5 and GPT-5.4 both collapse onto GPT-5.6 Sol, and GPT-5.4 mini
  and GPT-5 mini both collapse onto GPT-5.6 Luna. The May 2026 GPT-5.5
  convergence (`docs-github-copilot-gpt41-deprecation.md` Claim 7) required
  two separate notices (GPT-5.2 on May 1, GPT-4.1 on May 7) to establish
  GPT-5.5 as a universal successor across two model lines; this notice
  achieves the same many-to-one shape twice, in one table, for GPT-5.6's two
  non-flagship tiers.

### Claim 2: The deprecation covers the same broad surface set documented in every prior corpus deprecation notice, with no surface-based carve-out

- **Evidence**: Same sentence that announces the deprecation enumerates the
  affected surfaces; no surface exception is stated anywhere in the notice.
- **Confidence**: settled (word-for-word identical boilerplate, directly
  quotable)
- **Quote**: "all GitHub Copilot experiences (including Copilot Chat, inline
  edits, ask and agent modes, and code completions)"
- **Our assessment**: Identical to the affected-surface clause in all six
  prior corpus deprecation notices. Seven consecutive notices across four
  providers (OpenAI, Anthropic, Google, and now xAI) confirm this exact
  sentence remains GitHub's fixed boilerplate for the deprecation-notice post
  type, unaffected by the "most" vs. "all" wording variation flagged as a
  one-off anomaly in `docs-github-copilot-selected-models-deprecated-sept2026.md`
  Claim 3 (that notice's "most" wording did not recur here).

### Claim 3: The notice-to-cutoff window is 31 days (published September 18, 2026; effective October 19, 2026)

- **Evidence**: Changelog publish date (September 18, 2026, per the page
  byline) and the stated deprecation date (October 19, 2026, repeated six
  times in the table).
- **Confidence**: settled (both dates stated directly in the official
  source; the day-count is a derived calculation)
- **Quote**: "September 18, 2026" (page byline); "2026-10-19" (deprecation
  date, all six table rows)
- **Our assessment**: Across the corpus's seven deprecation notices, the lead
  time is now 31, 25, -1, 29, 32, 0/1 (same-event confirmation), and 31 days.
  This ties the original May 1 GPT-5.2 notice's 31-day window as the second
  longest in the corpus after the July 31 batch notice's 32 days
  (`docs-github-copilot-aug2026-model-deprecations.md` Claim 3). Consistent
  with that note's conclusion, lead time remains genuinely variable
  per-notice with no fixed platform convention practitioners can rely on.

### Claim 4: Suggested alternative models are automatically enabled for Copilot Enterprise and Copilot Business customers by default, unless an administrator has turned off the global default or explicitly disabled the specific model — the first deprecation notice in the corpus to describe successor enablement as default-on rather than requiring proactive admin action

- **Evidence**: Changelog required-actions paragraph, extracted from raw page
  HTML.
- **Confidence**: settled (stated directly in the official changelog; the
  "first in this family" framing is a verified corpus cross-reference)
- **Quote**: "Please update your workflows and integrations to use the
  supported models before this date. Under default model enablement, the
  suggested alternatives are automatically enabled for Copilot Enterprise and
  Copilot Business customers unless an administrator has turned off the
  global default or explicitly disabled the model. If you've turned off the
  global default, you can enable access to the alternative models through
  their model policies in Copilot settings."
- **Our assessment**: Every one of the six prior corpus deprecation notices
  used enable-then-verify language requiring Enterprise administrators to
  proactively enable each successor model (e.g.,
  `docs-github-copilot-gpt52-deprecation.md` Claim 5: "Enterprise
  administrators should enable alternative models through Copilot settings");
  their Guide Impact sections warned that admins who did not act would find
  deprecated models "simply gone with no automatic replacement." This notice
  inverts that default: successor models (Gemini 3.8 Flash, GPT-5.6 Sol,
  GPT-5.6 Luna, Grok 4.6) are now enabled automatically for Business/Enterprise
  customers unless an admin has opted out. This is not a contradiction of the
  prior notices' claims — it is the direct, dated consequence of the global
  default-enablement policy documented in
  `docs-github-copilot-global-model-policy-ga.md` (GA and enforced August
  26-September 1, 2026) reaching this deprecation-notice template for the
  first time. Per MINER.md §4a, this is treated as product evolution, the
  same treatment `docs-github-copilot-gemini38flash-availability.md` Claim 6
  gave the identical default-enablement language appearing in a "new model
  available" notice two weeks earlier. For Ch05: the "silent failure" risk
  pattern emphasized in all six prior deprecation notices' Guide Impact
  sections — that an unenabled successor means the deprecated model simply
  disappears — is now materially reduced for Business/Enterprise customers
  who have not disabled the global default, though it is not eliminated for
  customers who have (or for any customer on a plan tier the global policy
  does not cover).

### Claim 5: After deprecation, the old models disappear automatically — no admin action is required for removal

- **Evidence**: Closing sentence of the required-actions paragraph, extracted
  from raw page HTML.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "No action is required to remove the models after they have
  been deprecated."
- **Our assessment**: Near-identical wording to five of the six prior corpus
  notices (e.g., `docs-github-copilot-aug2026-model-deprecations.md` Claim 6:
  "No action is required to remove the models once they have been
  deprecated"). The minor "after" vs. "once" wording swap is consistent with
  the boilerplate-drift pattern already observed across this notice family
  (`docs-github-copilot-selected-models-deprecated-sept2026.md` Claim 3) and
  does not change the substance: auto-removal with no admin cleanup step is
  now confirmed a seventh time.

### Claim 6: GitHub Enterprise customers with questions are directed to "their account team" — a support-channel phrasing change from "account manager" used in every one of the six prior corpus notices

- **Evidence**: Closing sentence of the changelog body, extracted from raw
  page HTML.
- **Confidence**: settled (directly quotable; the significance of the wording
  change is our interpretation)
- **Quote**: "GitHub Enterprise customers with questions or concerns are
  encouraged to contact their account team for assistance."
- **Our assessment**: Every prior corpus deprecation notice used "reach out
  to their account manager for further assistance" (e.g.,
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 6).
  This notice swaps "account manager" for "account team" and drops "further."
  This is the same kind of minor, non-substantive boilerplate drift already
  documented for the affected-surface clause
  (`docs-github-copilot-selected-models-deprecated-sept2026.md` Claim 3) and
  the auto-removal sentence (Claim 5 above) — worth tracking as evidence that
  none of this changelog template's prose, beyond the dated table itself, is
  perfectly stable wording, but not evidence of an actual support-channel
  change (a "team" is a reasonable paraphrase of an assigned "manager" and
  no new contact mechanism is introduced).

### Claim 7: This is the first evidence anywhere in the corpus that a Grok (xAI) model was ever part of GitHub Copilot's model roster — no prior `docs-github-copilot-*` source names any Grok model

- **Evidence**: A search of the existing corpus's `docs-github-copilot-*`
  source notes for "Grok" prior to this note returns no results; Grok 4.5 is
  documented elsewhere in the corpus only in non-Copilot contexts (e.g.,
  `blog-cursor-grok-4-5.md`, about Cursor's model router).
- **Confidence**: emerging (absence-from-corpus is a corpus-completeness
  observation, not a claim this changelog itself makes)
- **Quote**: (no direct quote; corpus-search finding)
- **Our assessment**: This is a fourth instance of the "deprecation reveals
  prior undocumented availability" pattern already established for Raptor
  Mini (`docs-github-copilot-aug2026-model-deprecations.md` Claim 10) and for
  Gemini 2.5 Pro/Gemini 3 Flash
  (`docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 9).
  Grok 4.5's addition to Copilot was never separately announced or captured
  in this corpus — practitioners relying on the corpus as a complete
  model-availability timeline should treat this as confirmation that
  cross-provider model additions (here, xAI alongside the already-documented
  OpenAI, Anthropic, Google, and Microsoft) can enter Copilot's roster
  without a dedicated "now available" changelog ever surfacing in this
  corpus.

### Claim 8: Gemini 3.7 Flash — named as the operative successor for Gemini 3.1 Pro's own deprecation only 18 days earlier — is itself scheduled for deprecation here, in favor of Gemini 3.8 Flash, a model that had only debuted in Copilot 15 days before this notice was published

- **Evidence**: `docs-github-copilot-selected-models-deprecated-sept2026.md`
  (published August 31, 2026) Claim 4 names Gemini 3.7 Flash as Gemini 3.1
  Pro's confirmed successor, effective September 1, 2026.
  `docs-github-copilot-gemini38flash-availability.md` (published September 3,
  2026) documents Gemini 3.8 Flash's debut across eight Copilot surfaces.
  This source, published September 18, 2026, deprecates Gemini 3.7 Flash
  effective October 19, 2026, with Gemini 3.8 Flash as its successor.
- **Confidence**: emerging (each underlying date is settled individually;
  the "rapid churn" synthesis connecting all three sources is our
  cross-reference, not stated by any one of them)
- **Quote**: (no direct quote; comparison across this source,
  `docs-github-copilot-selected-models-deprecated-sept2026.md`, and
  `docs-github-copilot-gemini38flash-availability.md`)
- **Our assessment**: This is the fastest successor-to-deprecation turnaround
  documented anywhere in the corpus's Gemini Flash lineage. Gemini 3.6 Flash
  and Gemini 3.7 Flash were each named as the Gemini 3.1 Pro successor in
  turn without ever receiving their own dedicated Copilot availability
  notice (`docs-github-copilot-gemini38flash-availability.md` Claim 7); now
  Gemini 3.7 Flash — a model whose own standalone Copilot arrival was never
  separately confirmed — is scheduled for removal a mere 18 days after being
  named the operative Gemini 3.1 Pro successor, in favor of a model
  (Gemini 3.8 Flash) that itself only reached Copilot 15 days before this
  notice. Practitioners who migrated to Gemini 3.7 Flash immediately upon
  reading the August 31 confirmation notice face a second required migration
  within seven weeks. This reinforces and sharpens the caution already
  recorded in `docs-github-copilot-selected-models-deprecated-sept2026.md`
  Guide Impact §Ch02 that pre-announcement successor names can drift before
  or shortly after the effective date — here the successor itself becomes
  the next deprecated model within weeks, not just its designated name.

### Claim 9: GPT-5.4's designated successor is GPT-5.6 Sol, the flagship tier — not a same-tier GPT-5.6 mid-range model — meaning migrators inherit Sol's pricing rather than a mid-tier equivalent

- **Evidence**: This source's deprecation table pairs "GPT-5.4" with
  "GPT-5.6 Sol." `blog-simonwillison-gpt55-codex-plugin.md` Claim 4
  documents GPT-5.4's own (April 2026) API pricing as $2.50/$15.00 per
  million input/output tokens, "2× cheaper than GPT-5.5." `blog-simonwillison-gpt56-sol-launch.md`
  Concrete Artifacts documents GPT-5.6 Sol's pricing as $5.00/$30.00 —
  unchanged through the July 30, 2026 price cut per
  `blog-simonwillison-gpt56-luna-price-drop.md` Concrete Artifacts (only
  Terra and Luna were cut; "Sol pricing remains unchanged").
- **Confidence**: emerging (the per-token API prices are settled individually
  from independent corpus sources; whether GitHub Copilot's own internal
  billing/premium-request multipliers track raw API pricing this closely is
  not confirmed by any source in this note)
- **Quote**: "GPT-5.4 | 2026-10-19 | GPT-5.6 Sol" (from this source's
  deprecation table)
- **Our assessment**: Unlike GPT-5.5 → GPT-5.6 Sol (a same-tier flagship
  migration matching the $5/$30 Sol price this GPT-5.5 already paid), GPT-5.4
  → GPT-5.6 Sol is a tier bump: GPT-5.4 sat one rung below GPT-5.5 on
  pricing, but its designated GPT-5.6-generation successor is Sol, not a
  Terra/Luna-tier model. If Copilot's cost model tracks these API-list
  prices even loosely, GPT-5.4 migrators face roughly a 2x cost increase per
  request, not a same-tier refresh. This is a materially different migration
  shape from the Gemini and Grok rows in the same table (Claim 1), which are
  both same-tier point-release bumps (Flash→Flash, Grok→Grok). The changelog
  itself states no pricing information and does not flag this as a tier
  change — practitioners auditing cost impact from this table alone would
  miss it.

### Claim 10: Users see the replacement model in "the Copilot Chat model selector in supported GitHub Copilot experiences" once enabled — a more generic surface reference than the "VS Code and github.com" wording used in five of the six prior corpus notices

- **Evidence**: Changelog body, sentence following the default-enablement
  paragraph, extracted from raw page HTML.
- **Confidence**: settled (directly quotable; the significance of the
  wording is our interpretation)
- **Quote**: "Once enabled, users will see the model in the Copilot Chat
  model selector in supported GitHub Copilot experiences."
- **Our assessment**: Every prior corpus deprecation notice that described
  verification named two specific surfaces — "you'll see the model in the
  Copilot Chat model selector in VS Code and on github.com" (e.g.,
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 4). This notice
  replaces that two-surface enumeration with the generic "supported GitHub
  Copilot experiences." Given that Copilot's model picker now spans at least
  eight surfaces for some models (VS Code, Visual Studio, CLI, cloud agent,
  app, JetBrains, Xcode, Eclipse, per
  `docs-github-copilot-gemini38flash-availability.md` Claim 1), this reads as
  the changelog template catching up to a surface count too large to
  enumerate concisely, rather than a narrowing of scope. No surface is stated
  to be excluded.

## Concrete Artifacts

### Deprecation Table (from changelog, September 18, 2026 — effective October 19, 2026)

```
GitHub Copilot Model Deprecation — Effective October 19, 2026

| Model          | Deprecation Date | Suggested Alternative |
|----------------|-------------------|------------------------|
| Gemini 3.7 Flash | 2026-10-19      | Gemini 3.8 Flash       |
| GPT-5.5        | 2026-10-19        | GPT-5.6 Sol            |
| GPT-5.4        | 2026-10-19        | GPT-5.6 Sol            |
| GPT-5.4 mini   | 2026-10-19        | GPT-5.6 Luna           |
| GPT-5 mini     | 2026-10-19        | GPT-5.6 Luna           |
| Grok 4.5       | 2026-10-19        | Grok 4.6               |

No exceptions or carve-outs stated.
Affected surfaces: all GitHub Copilot experiences (Copilot Chat, inline edits,
                   ask and agent modes, code completions).
Page category tag: "Retired"
```

*Source: GitHub Copilot official changelog, September 18, 2026*

### Full Article Text (verbatim, extracted from raw page HTML via direct curl fetch)

```
Upcoming deprecation of selected GitHub Copilot models in mid-October

Retired
September 18, 2026 • 1 minute read

We will deprecate the following models across all GitHub Copilot experiences
(including Copilot Chat, inline edits, ask and agent modes, and code
completions) on October 19th, 2026:

Model              Deprecation date    Suggested alternative
Gemini 3.7 Flash   2026-10-19          Gemini 3.8 Flash
GPT-5.5            2026-10-19          GPT-5.6 Sol
GPT-5.4            2026-10-19          GPT-5.6 Sol
GPT-5.4 mini       2026-10-19          GPT-5.6 Luna
GPT-5 mini         2026-10-19          GPT-5.6 Luna
Grok 4.5           2026-10-19          Grok 4.6

Please update your workflows and integrations to use the supported models
before this date. Under default model enablement, the suggested alternatives
are automatically enabled for Copilot Enterprise and Copilot Business
customers unless an administrator has turned off the global default or
explicitly disabled the model. If you've turned off the global default, you
can enable access to the alternative models through their model policies in
Copilot settings.

Once enabled, users will see the model in the Copilot Chat model selector in
supported GitHub Copilot experiences.

No action is required to remove the models after they have been deprecated.

GitHub Enterprise customers with questions or concerns are encouraged to
contact their account team for assistance.

To learn more about the models available in Copilot, see our documentation
on supported models. Join the GitHub Community to share your feedback.
```

*Source: raw HTML of
https://github.blog/changelog/2026-09-18-upcoming-deprecation-of-selected-github-copilot-models-in-mid-october,
fetched directly via `curl` (not WebFetch summarization alone) on
2026-09-19. Page category tag: "Retired." Published: September 18, 2026.
Read time: "1 minute read." Links out to a general "documentation on
supported models" page and the GitHub Community discussions category — the
same two link-target types as every prior notice in this family.*

### Cross-Notice Deprecation Timeline (derived from seven corpus sources)

```
GitHub Copilot Model Deprecations — Corpus Timeline (as of September 2026)

Notice   | Model(s)                          | Notice Date | Effective Date | Lead Time
---------|-------------------------------------|-------------|-----------------|----------
May 1    | GPT-5.2 / GPT-5.2-Codex*            | 2026-05-01  | 2026-06-01      | 31 days
May 7    | GPT-4.1                              | 2026-05-07  | 2026-06-01      | 25 days
May 7    | Claude Sonnet 4                      | 2026-05-07  | 2026-05-06      | -1 day
Jul 2    | Gemini 2.5 Pro / Gemini 3 Flash       | 2026-07-02  | 2026-07-31      | 29 days
Jul 31   | Gemini 3.1 Pro / Opus 4.5 / Opus 4.6 /| 2026-07-31  | 2026-09-01      | 32 days
         | Sonnet 4.5 / Sonnet 4.6 / Raptor Mini |             |                 |
Aug 31   | Same event, confirmed (successor      | 2026-08-31  | 2026-09-01      | 0/1 day
         | names for Gemini 3.1 Pro & Raptor     |             |                 | (confirmation)
         | Mini revised — contradiction #3170)   |             |                 |
Sep 18   | Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 /| 2026-09-18  | 2026-10-19      | 31 days
         | GPT-5.4 mini / GPT-5 mini / Grok 4.5  |             |                 |  ← THIS NOTE

* GPT-5.2-Codex in Copilot Code Review carved out (see docs-github-copilot-gpt52-deprecation.md)

Successor model designations (this notice, Sept 18):
  Gemini 3.7 Flash → Gemini 3.8 Flash
  GPT-5.5          → GPT-5.6 Sol
  GPT-5.4          → GPT-5.6 Sol       (tier bump: mid-tier → flagship pricing)
  GPT-5.4 mini     → GPT-5.6 Luna
  GPT-5 mini       → GPT-5.6 Luna
  Grok 4.5         → Grok 4.6          (first Grok/xAI model in the corpus's Copilot roster)
```

*Derived from this source and the six prior corpus deprecation notices listed
in Claim 1.*

### Enterprise Migration Checklist for the October 19, 2026 Cutover

```
Before October 19, 2026 — Enterprise Copilot Administrators:

[ ] Audit workflows, scripts, and integrations referencing "gemini-3.7-flash",
    "gpt-5.5", "gpt-5.4", "gpt-5.4-mini", "gpt-5-mini", or "grok-4.5" as
    model identifiers.
[ ] Confirm the global default-enablement policy's current state (enabled or
    disabled) — if enabled and none of the six successor models have been
    explicitly disabled, no admin action is required; the successors
    (Gemini 3.8 Flash, GPT-5.6 Sol, GPT-5.6 Luna, Grok 4.6) become available
    automatically per Claim 4.
[ ] If the global default has been turned off, explicitly enable Gemini 3.8
    Flash, GPT-5.6 Sol, and GPT-5.6 Luna (and Grok 4.6, if xAI models are in
    use) through Copilot model policy settings.
[ ] Flag GPT-5.4 migrators for a potential cost review: GPT-5.4's designated
    successor (GPT-5.6 Sol) is the GPT-5.6 flagship tier, not a same-tier
    mid-range model (see Claim 9) — unlike the Gemini and Grok rows, which
    are same-tier point-release bumps.
[ ] Update integration configurations to reference the new model identifiers.

Post-October 19:
  - Gemini 3.7 Flash, GPT-5.5, GPT-5.4, GPT-5.4 mini, GPT-5 mini, and Grok 4.5
    disappear automatically.
  - "No action is required to remove the models after they have been
    deprecated."

Support: "GitHub Enterprise customers with questions or concerns are
          encouraged to contact their account team for assistance."
```

*Source: Required actions section of GitHub Copilot changelog, September 18,
2026, combined with `docs-github-copilot-global-model-policy-ga.md`.*

## Cross-References

- **Corroborates** `docs-github-copilot-global-model-policy-ga.md` Claims 2
  and 10, and `docs-github-copilot-gemini38flash-availability.md` Claim 6:
  all three sources describe the same default-enablement mechanism (models
  not explicitly configured follow the global policy, which defaults to
  enabled for Business/Enterprise). This is the first deprecation-notice
  instance of that mechanism in the corpus, following the "new model
  available" instance in `docs-github-copilot-gemini38flash-availability.md`
  by two weeks.

- **Corroborates** `docs-github-copilot-selected-models-deprecated-sept2026.md`
  Claim 3, `docs-github-copilot-aug2026-model-deprecations.md` Claim 2, and
  four earlier notices (identical affected-surface boilerplate): this notice
  repeats the exact phrase verbatim, confirming it as stable across seven
  consecutive deprecation notices.

- **Extends** six prior corpus deprecation notices' enable-then-verify
  governance pattern (most recently
  `docs-github-copilot-selected-models-deprecated-sept2026.md` Claim 8): this
  notice is the first to describe automatic default enablement rather than
  required proactive admin action, per Claim 4. Per MINER.md §4a, this is
  treated as product evolution (explained by the intervening global
  default-enablement policy GA, `docs-github-copilot-global-model-policy-ga.md`)
  rather than a contradiction — no contradiction issue filed.

- **Extends** `docs-github-copilot-selected-models-deprecated-sept2026.md`
  Claim 4 and contradiction #3170 (Gemini 3.1 Pro's successor renamed from
  Gemini 3.6 Flash to Gemini 3.7 Flash between pre-announcement and
  confirmation): this source shows Gemini 3.7 Flash itself scheduled for
  deprecation only 18 days after being confirmed as the operative successor,
  sharpening that note's caution about successor-name churn into a caution
  about successor-model churn (Claim 8).

- **Extends** `docs-github-copilot-gemini38flash-availability.md` (Gemini
  3.8 Flash's September 3, 2026 Copilot debut across eight surfaces): this
  source confirms Gemini 3.8 Flash as an operative deprecation successor
  just 15 days after its own Copilot debut — the shortest gap between a
  model's Copilot arrival and its designation as another model's replacement
  documented anywhere in this corpus's Gemini lineage.

- **Extends** `docs-github-copilot-gpt41-deprecation.md` Claim 7 (GPT-5.5 as
  a universal successor across GPT-5.2 and GPT-4.1) and
  `blog-simonwillison-gpt56-sol-launch.md` / `blog-simonwillison-gpt56-luna-price-drop.md`
  (GPT-5.6 Sol/Terra/Luna pricing): this source shows GPT-5.5 itself — the
  model that absorbed two prior deprecated model lines four months earlier —
  is now deprecated in turn, and cross-references the GPT-5.6 pricing corpus
  to surface the GPT-5.4 → Sol tier-bump cost implication (Claim 9) that the
  changelog itself does not flag.

- **Extends** `docs-github-copilot-aug2026-model-deprecations.md` Claim 10
  and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 9
  ("deprecation reveals prior undocumented availability" pattern): Grok 4.5
  is a fourth instance, and the first to introduce an entirely new provider
  (xAI) to the corpus's documented Copilot-provider roster (OpenAI,
  Anthropic, Google, Microsoft, now xAI).

- **Contradicts**: None filed. The default-enablement language shift (Claim
  4) is resolved as product evolution via the intervening global
  default-enablement policy, following the exact precedent set by
  `docs-github-copilot-gemini38flash-availability.md` for the same wording
  in a different notice type. No other claim in this source conflicts with
  an existing corpus claim about the same point in time.

- **Novel**:
  - **First Grok/xAI model in the corpus's documented GitHub Copilot
    roster** (Claim 7), surfaced only via its deprecation.
  - **First deprecation notice to describe successor enablement as
    automatic-by-default** rather than requiring proactive admin action
    (Claim 4).
  - **First notice with two many-to-one successor convergences within a
    single deprecation table** (Claim 1).
  - **Fastest successor-to-next-deprecation turnaround documented in the
    corpus**: Gemini 3.7 Flash deprecated 18 days after being named an
    operative successor; Gemini 3.8 Flash named a successor 15 days after
    its own Copilot debut (Claim 8).
  - **First documented tier-bump migration within this deprecation family**:
    GPT-5.4 (mid-tier pricing) is routed to GPT-5.6 Sol (flagship pricing),
    not a same-tier GPT-5.6 model (Claim 9).

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: Gemini 3.7 Flash, GPT-5.5, GPT-5.4, GPT-5.4 mini,
  GPT-5 mini, and Grok 4.5 should be marked deprecated (effective October 19,
  2026) in any Copilot model roster the guide maintains. Gemini 3.8 Flash,
  GPT-5.6 Sol, GPT-5.6 Luna, and Grok 4.6 are the confirmed replacements.
  This is also the first documented instance of a Grok/xAI model in the
  guide's Copilot roster context — if the guide currently has no xAI entries
  for Copilot, this notice is the evidence base for adding one (with the
  caveat, per Claim 7, that Grok 4.5's actual Copilot debut is otherwise
  undocumented in this corpus).
- **Design principle reinforcement, with a new nuance — successor identity
  can churn as fast as successor naming**: The existing recommendation to
  avoid hardcoded model identifiers
  (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02) should now
  add: even a model adopted specifically as a migration target (Gemini 3.7
  Flash, per the August 31 confirmation) can itself be deprecated within
  weeks (Claim 8). Practitioners who treat "migrated to the suggested
  alternative" as a durable end state should instead treat it as a recurring
  task.
- **Cost-review nuance for tier-bump migrations**: Add a caution, based on
  Claim 9, that a deprecation table's "suggested alternative" column does
  not guarantee a same-tier (and therefore same-cost) replacement — GPT-5.4
  migrators here inherit GPT-5.6 Sol's flagship pricing, not a mid-tier
  equivalent, with no cost information stated in the changelog itself.

### Chapter 05: Team Adoption / Enterprise Governance

- **The "enable proactively or lose access silently" governance risk is now
  weakened for Business/Enterprise customers with the global default
  enabled**: Update any governance checklist built from the six prior
  deprecation notices' Guide Impact sections (all of which emphasized
  proactive admin enablement as the only defense against silent model loss)
  to reflect Claim 4: as of this notice, successor models are enabled
  automatically by default. The residual risk shifts to customers who have
  turned off the global default or explicitly disabled a specific successor
  model — governance audits should confirm which state applies before
  assuming either the old (manual) or new (automatic) risk model.
- **Cross-provider deprecation cadence now spans five providers**: Seven
  deprecation notices across OpenAI, Anthropic, Google, Microsoft, and now
  xAI within roughly five months (May-September 2026) reinforce that Copilot
  model-lifecycle monitoring is an ongoing, cross-provider governance
  responsibility (`docs-github-copilot-claude-sonnet4-deprecation.md` Guide
  Impact §Ch05), regardless of which provider(s) an organization currently
  uses — a fifth provider appearing without warning here.

## Extraction Notes

1. **WebFetch under-reported the deprecation table by one row**: An initial
   WebFetch pass returned a five-model summary that omitted "GPT-5 mini"
   entirely and mischaracterized the table structure. The page's raw HTML was
   then fetched directly via `curl` and the article text extracted
   programmatically (tags stripped, HTML entities decoded). All six claims
   quoting the deprecation table, the required-actions paragraph, and the
   closing sentences above are taken from that raw-HTML extraction and are
   character-for-character verbatim from the source page as of 2026-09-19,
   not from the WebFetch summary. This is the same AI-summarization risk
   flagged in every prior deprecation note in this family
   (e.g., `docs-github-copilot-aug2026-model-deprecations.md` Extraction
   Notes item 2).
2. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-gpt52-deprecation.md`,
   `docs-github-copilot-gpt41-deprecation.md`,
   `docs-github-copilot-claude-sonnet4-deprecation.md`,
   `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`,
   `docs-github-copilot-aug2026-model-deprecations.md`,
   `docs-github-copilot-selected-models-deprecated-sept2026.md`,
   `docs-github-copilot-global-model-policy-ga.md`,
   `docs-github-copilot-gemini38flash-availability.md`,
   `blog-simonwillison-gpt55-codex-plugin.md`,
   `blog-simonwillison-gpt56-sol-launch.md`, and
   `blog-simonwillison-gpt56-luna-price-drop.md` were checked against those
   notes' actual claim numbering (each note re-read in full before citing);
   none were guessed.
3. **No contradiction issue filed**: The only candidate contradiction — the
   default-enablement language shift documented in Claim 4 — is resolved as
   product evolution via the intervening, independently documented global
   default-enablement policy GA
   (`docs-github-copilot-global-model-policy-ga.md`), following the exact
   precedent already set for the same wording in
   `docs-github-copilot-gemini38flash-availability.md` Claim 6. No new
   contradiction issue was warranted per MINER.md §4a.
4. **Source is thin by design**: The changelog is approximately 140 words of
   primary text. All extractable facts are captured in the ten claims above;
   Claims 7, 8, and 9 are corpus cross-reference findings built on this
   source's table entries rather than facts the changelog itself states, and
   are labeled `emerging` accordingly. The changelog does not explain why
   these six models across three providers are being retired together, nor
   does it disclose pricing for any of the four successor models.
5. **Grok 4.5's prior Copilot availability could not be independently
   confirmed**: A search of this corpus's `docs-github-copilot-*` notes for
   any prior mention of Grok models returned nothing (Claim 7). This note
   does not speculate about when or how Grok 4.5 was added to Copilot's
   roster — only that its addition was never separately documented in this
   corpus.
