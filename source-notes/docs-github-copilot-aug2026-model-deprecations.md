---
source_url: https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot
source_type: docs
title: "Upcoming August 2026 model deprecations in GitHub Copilot"
author: GitHub (official changelog)
date_published: 2026-07-31
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: settled
issue: "#2471"
---

# Upcoming August 2026 Model Deprecations in GitHub Copilot

> GitHub's July 31, 2026 changelog retiring six models — Gemini 3.1 Pro, Claude
> Opus 4.5, Claude Opus 4.6, Claude Sonnet 4.5, Claude Sonnet 4.6, and Raptor
> Mini — from all Copilot experiences on September 1, 2026 (a 32-day notice
> window, the longest yet in the corpus), the first notice to span three
> providers simultaneously, the first to deprecate Opus-tier Claude models,
> the first to offer a three-way successor choice (Opus 4.7, 4.8, or 5) rather
> than a single replacement, and the first to carry a plan-based carve-out
> (Sonnet 4.6 stays available to individual annual-plan subscribers) rather
> than the surface-based carve-outs seen in earlier notices.

## Source Context

- **Type**: docs (GitHub official product changelog, July 31, 2026; ~150 words
  of primary announcement text, "1 minute read," category-tagged "Retired" —
  confirmed via direct raw-HTML fetch, not just a WebFetch summary)
- **Author credibility**: GitHub engineering team. Authoritative for the
  deprecation date, per-model successor designations, affected surfaces, the
  Sonnet 4.6 annual-plan carve-out, and enterprise admin requirements. Not a
  source for capability comparisons between deprecated and replacement
  models, migration effort, or cost implications of the migration.
- **Scope**: Deprecation of six named models from "all GitHub Copilot
  experiences (including Copilot Chat, inline edits, ask and agent modes, and
  code completions)," effective September 1, 2026. Covers the successor
  model(s) for each, the one stated carve-out, and the standard
  enable-then-verify admin procedure. Does NOT cover: why these six models
  (spanning three providers) are being retired together, capability
  differences between deprecated and replacement models, cost implications of
  the migration, or what happens to in-flight sessions using a deprecated
  model at the moment of cutover.

## Extracted Claims

### Claim 1: Six models are deprecated across all GitHub Copilot experiences effective September 1, 2026, each with a named successor: Gemini 3.1 Pro → Gemini 3.6 Flash; Claude Opus 4.5 → Opus 4.7/4.8/5; Claude Opus 4.6 → Opus 4.7/4.8/5; Claude Sonnet 4.5 → Sonnet 5; Claude Sonnet 4.6 → Sonnet 5; Raptor Mini → MAI-Code-1-Flash

- **Evidence**: Official GitHub Copilot changelog table, published July 31, 2026, fetched directly from the raw page HTML.
- **Confidence**: settled (authoritative product fact — dates and successors stated directly in a structured table)
- **Quote**: "We will deprecate the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions), on September 1st, 2026:" followed by the table rows "Gemini 3.1 Pro | 9-1-2026 | Gemini 3.6 Flash", "Claude Opus 4.5 | 9-1-2026 | Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5", "Claude Opus 4.6 | 9-1-2026 | Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5", "Claude Sonnet 4.5 | 9-1-2026 | Claude Sonnet 5", "Claude Sonnet 4.6* | 9-1-2026 | Claude Sonnet 5", "Raptor Mini | 9-1-2026 | MAI-Code-1-Flash"
- **Our assessment**: This is the fifth Copilot model deprecation notice in the corpus (after `docs-github-copilot-gpt52-deprecation.md`, `docs-github-copilot-gpt41-deprecation.md`, `docs-github-copilot-claude-sonnet4-deprecation.md`, and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`) and the first to bundle three providers' models (Google, Anthropic, Microsoft) into a single notice — prior notices each covered one or two providers at most. It is also the first notice to deprecate Opus-tier Claude models (`docs-github-copilot-claude-sonnet4-deprecation.md` only covered the Sonnet tier) and the first to give practitioners a *choice* of successor (Opus 4.7, 4.8, or 5) rather than a single designated replacement — every prior corpus notice mapped each deprecated model to exactly one successor.

### Claim 2: The deprecation covers the same broad surface set documented in every prior corpus deprecation notice, with no surface-based carve-out

- **Evidence**: Same sentence that announces the deprecation enumerates the affected surfaces; no surface exception is stated anywhere in the notice.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)"
- **Our assessment**: Word-for-word identical to the affected-surface boilerplate in `docs-github-copilot-gpt52-deprecation.md` Claim 4, `docs-github-copilot-gpt41-deprecation.md` Claim 2, `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 6, and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 2. Five consecutive notices now confirm this exact sentence is fixed boilerplate GitHub reuses regardless of provider or model count. Unlike the GPT-5.2-Codex/Copilot Code Review carve-out (`docs-github-copilot-gpt52-deprecation.md` Claim 3), this notice has no surface-specific exception — the only carve-out in this notice is plan-based (see Claim 4).

### Claim 3: The notice-to-cutoff window is 32 days (published July 31, 2026; effective September 1, 2026) — the longest advance-notice window documented in the corpus to date

- **Evidence**: Changelog publish date (July 31, 2026, per the page header) and the stated deprecation date (September 1, 2026) in the table.
- **Confidence**: settled (both dates stated directly in the official source; the day-count is a derived calculation)
- **Quote**: "July 31, 2026" (page publish date); "9-1-2026" (deprecation date, repeated six times in the table)
- **Our assessment**: Across five corpus deprecation notices the lead time is now 31, 25, -1, 29, and 32 days. This is the longest window yet, extending `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 3's conclusion that notice length is genuinely variable per-notice rather than following a fixed platform convention. Practitioners still cannot infer a specific lead time from any past pattern.

### Claim 4: Claude Sonnet 4.6 carries a plan-based carve-out — it remains available to individual GitHub Copilot subscribers on annual plans, unaffected by the September 1 deprecation

- **Evidence**: A footnote (marked by an asterisk on the "Claude Sonnet 4.6*" table row) stated as a standalone sentence directly beneath the deprecation table.
- **Confidence**: settled (stated directly and unambiguously in the official changelog)
- **Quote**: "Claude Sonnet 4.6 will remain available to individual GitHub Copilot subscribers on annual plans so they retain a Sonnet offering. The deprecation of Claude Sonnet 4.6 does not apply to these customers."
- **Our assessment**: This is the first *plan-based* carve-out documented in the corpus's deprecation-notice family. The only prior carve-out — GPT-5.2-Codex in Copilot Code Review (`docs-github-copilot-gpt52-deprecation.md` Claim 3) — was surface-based (a specific Copilot feature was exempted). Here the exemption instead depends on the subscriber's plan type and commitment length (individual + annual), not which Copilot surface they use. Practitioners on individual annual plans who are already using Claude Sonnet 4.6 do not need to migrate; individual monthly-plan subscribers and all Business/Enterprise users, by implication, are not covered by this carve-out and must migrate to Sonnet 5 by September 1. The changelog does not state whether this exemption is permanent or itself has a future expiration.

### Claim 5: Copilot Enterprise administrators must proactively enable the successor models via Copilot model policies — no automatic migration of admin policies occurs — using the same enable-then-verify procedure documented in every prior corpus notice

- **Evidence**: Changelog required-actions paragraph.
- **Confidence**: settled (required action stated directly in official changelog)
- **Quote**: "Please update your workflows and integrations to use the supported model before these dates. Copilot Enterprise administrators may need to enable access to the alternative model through their model policies in Copilot settings. As an administrator, you can verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model. Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com."
- **Our assessment**: Near-verbatim match to the equivalent paragraph in `docs-github-copilot-gpt52-deprecation.md` Claim 5, `docs-github-copilot-gpt41-deprecation.md` Claim 3, `docs-github-copilot-claude-sonnet4-deprecation.md` Claims 3-4, and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 4. Five consecutive notices across four providers (OpenAI, Anthropic, Google, and now Microsoft via Raptor Mini/MAI-Code-1-Flash) confirm this two-step enable-then-verify procedure is GitHub's fixed, standardized enterprise governance mechanism for Copilot model deprecations — not a provider-specific or notice-specific detail. Enterprise teams that do not enable the relevant successor models (Gemini 3.6 Flash, Opus 4.7/4.8/5, Sonnet 5, MAI-Code-1-Flash) before September 1 will find the deprecated models simply gone with no automatic replacement.

### Claim 6: After deprecation, the old models disappear automatically — no admin action is required for removal

- **Evidence**: Closing sentence of the required-actions paragraph.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "No action is required to remove the models once they have been deprecated."
- **Our assessment**: Near-identical wording to `docs-github-copilot-gpt41-deprecation.md` Claim 4 ("No action is required to remove the models once they have been deprecated") and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 5 ("No action is required to remove the older models once they have been deprecated"). This is now the fifth consecutive notice confirming auto-removal with no admin cleanup step as a fixed cross-provider pattern.

### Claim 7: GitHub Enterprise customers with questions are directed to their account manager — the same support channel named in every prior corpus notice

- **Evidence**: Closing sentence of the changelog body.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "GitHub Enterprise customers with questions or concerns are encouraged to reach out to their account manager for further assistance."
- **Our assessment**: Word-for-word identical to the equivalent sentence in `docs-github-copilot-gpt52-deprecation.md`, `docs-github-copilot-gpt41-deprecation.md`, and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`. No new support channel is offered beyond the general community-discussions link at the foot of the page.

### Claim 8: The changelog title names "August 2026" but every deprecation date in the table, and the publish date, place the event at the July 31 / September 1 boundary — no model in the table is actually deprecated during August

- **Evidence**: Page title "Upcoming August 2026 model deprecations in GitHub Copilot"; publish date "July 31, 2026"; every row in the deprecation table lists "9-1-2026" as the deprecation date.
- **Confidence**: emerging (the discrepancy is a directly observable fact from the page; the significance we assign it — that the title is a loose seasonal label rather than a precise date descriptor — is our interpretation)
- **Quote**: "Upcoming August 2026 model deprecations in GitHub Copilot" (title); "9-1-2026" (deprecation date, all six table rows)
- **Our assessment**: The title's "August 2026" appears to describe when the notice was surfaced/discussed (published the last day of July, with the cutover the day after August ends) rather than when any model is actually removed — all six removals take effect on September 1. Practitioners scanning changelog titles for a month label should not assume the title month matches the effective date; the table's explicit per-model dates are the only reliable signal, consistent with the broader "read the dates, not the label" caution already established for the "Retired" category tag in `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 7.

### Claim 9: This is the first corpus deprecation notice with no OpenAI/GPT-family model included — the affected models span Google (Gemini), Anthropic (Claude Opus and Sonnet), and Microsoft (Raptor Mini, an in-house model)

- **Evidence**: Cross-referencing the deprecation table in this source against the four prior corpus deprecation notices, all of which included at least one OpenAI GPT-family model (`docs-github-copilot-gpt52-deprecation.md`, `docs-github-copilot-gpt41-deprecation.md`) or were single-provider Claude/Gemini notices that followed GPT-inclusive notices earlier in the same season.
- **Confidence**: emerging (absence-of-GPT-models is a corpus-completeness observation derived by comparison, not a claim the source itself makes)
- **Quote**: (no direct quote; comparison across five dated sources)
- **Our assessment**: `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 8 and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 7's cross-notice tables show every deprecation cluster from May through July 2026 touching OpenAI models. This August notice is the first to omit OpenAI entirely, instead pairing a Gemini model with two Claude tiers and a Microsoft in-house model (Raptor Mini). This reinforces the guide's existing point that Copilot model lifecycle churn is provider-agnostic and does not follow a fixed per-provider cadence — any given notice can involve any subset of the providers Copilot supports.

### Claim 10: Raptor Mini was never separately documented in the corpus as being added to Copilot — like Gemini 2.5 Pro and Gemini 3 Flash before it, its existence in the Copilot model roster surfaces in the corpus only via this deprecation notice

- **Evidence**: A search of the existing corpus for "Raptor Mini" prior to this note returns no results — no prior source note documents Raptor Mini's addition to any Copilot surface.
- **Confidence**: emerging (absence-from-corpus is a corpus-completeness observation, not a claim the source itself makes)
- **Quote**: (no direct quote; corpus-search finding)
- **Our assessment**: This is a third instance of the "deprecation reveals prior undocumented availability" pattern first identified in `docs-github-copilot-web-model-consolidation.md` Claim 1 and repeated for Gemini 2.5 Pro/Gemini 3 Flash in `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 9. Models can enter and leave the Copilot roster without a corresponding "here's a new model" changelog entry ever surfacing in this corpus's source base — practitioners relying on the corpus as a complete model-availability timeline should treat this gap as expected, not exceptional.

### Claim 11: The designated Claude successors (Opus 5 and Sonnet 5) had both already reached GA/launch before this deprecation notice was published — Opus 5 seven days earlier, Sonnet 5 a month earlier

- **Evidence**: `blog-simonwillison-introducing-opus-5.md` documents Claude Opus 5's launch on July 24, 2026 (frontmatter `date_published`). `docs-github-copilot-sonnet5-ga.md` Claim 1 documents Claude Sonnet 5 reaching general availability in Copilot on June 30, 2026.
- **Confidence**: emerging (each underlying fact is settled individually; the "already available before deprecation" synthesis is our cross-reference, not stated in this changelog)
- **Quote**: (no direct quote; comparison across this source, `blog-simonwillison-introducing-opus-5.md`, and `docs-github-copilot-sonnet5-ga.md`)
- **Our assessment**: This mirrors the "successor rolled out ahead of predecessor's formal deprecation notice" pattern already established for GPT-5.5 (`docs-github-copilot-gpt41-deprecation.md` Cross-References) and Gemini 3.1 Pro/3.5 Flash (`docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 8). Practitioners who adopted Sonnet 5 or Opus 5 as soon as they became selectable were already migrated by the time this deprecation notice arrived; only practitioners still pinned to Opus 4.5/4.6 or Sonnet 4.5/4.6 identifiers face a required action before September 1.

## Concrete Artifacts

### Deprecation Table (from changelog, July 31, 2026 — effective September 1, 2026)

```
GitHub Copilot Model Deprecation — Effective September 1, 2026

| Model             | Deprecation Date | Suggested Alternative                          |
|--------------------|-------------------|------------------------------------------------|
| Gemini 3.1 Pro     | 9-1-2026          | Gemini 3.6 Flash                                |
| Claude Opus 4.5    | 9-1-2026          | Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5 |
| Claude Opus 4.6    | 9-1-2026          | Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5 |
| Claude Sonnet 4.5  | 9-1-2026          | Claude Sonnet 5                                 |
| Claude Sonnet 4.6* | 9-1-2026          | Claude Sonnet 5                                 |
| Raptor Mini        | 9-1-2026          | MAI-Code-1-Flash                                |

* Claude Sonnet 4.6 remains available to individual subscribers on annual
  plans; the deprecation does not apply to those customers.

No surface-based exceptions or carve-outs stated.
Affected surfaces: all GitHub Copilot experiences (Copilot Chat, inline edits,
                   ask and agent modes, code completions).
Page category tag: "Retired"
```

*Source: GitHub Copilot official changelog, July 31, 2026*

### Full Article Text (verbatim, extracted from raw page HTML via direct curl fetch)

```
Upcoming August 2026 model deprecations in GitHub Copilot

We will deprecate the following models across all GitHub Copilot experiences
(including Copilot Chat, inline edits, ask and agent modes, and code
completions), on September 1st, 2026:

Model               Deprecation date    Suggested alternative
Gemini 3.1 Pro       9-1-2026            Gemini 3.6 Flash
Claude Opus 4.5      9-1-2026            Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5
Claude Opus 4.6      9-1-2026            Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5
Claude Sonnet 4.5    9-1-2026            Claude Sonnet 5
Claude Sonnet 4.6*   9-1-2026            Claude Sonnet 5
Raptor Mini          9-1-2026            MAI-Code-1-Flash

Claude Sonnet 4.6 will remain available to individual GitHub Copilot
subscribers on annual plans so they retain a Sonnet offering. The
deprecation of Claude Sonnet 4.6 does not apply to these customers.

Please update your workflows and integrations to use the supported model
before these dates. Copilot Enterprise administrators may need to enable
access to the alternative model through their model policies in Copilot
settings. As an administrator, you can verify availability by checking your
individual Copilot settings and confirming that the policy is enabled for
the specific model. Once enabled, you'll see the model in the Copilot Chat
model selector in VS Code and on github.com. No action is required to
remove the models once they have been deprecated.

GitHub Enterprise customers with questions or concerns are encouraged to
reach out to their account manager for further assistance.

To learn more about the models available in Copilot, see our documentation
on models and get started with Copilot today.
```

*Source: raw HTML of
https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot/,
fetched directly via curl (not WebFetch summarization) on 2026-08-04. Tag:
"Retired". Published: July 31, 2026. Read time: "1 minute read." Links out to
docs.github.com/copilot/reference/ai-models/supported-models (models
documentation) and github.com/orgs/community/discussions/categories/copilot-conversations
(community feedback) — same two link targets as the Gemini 2.5 Pro/Gemini 3
Flash notice.*

### Cross-Notice Deprecation Timeline (derived from five corpus sources)

```
GitHub Copilot Model Deprecations — Corpus Timeline (as of August 2026)

Notice   | Model(s)                       | Notice Date | Effective Date | Lead Time | Providers
---------|----------------------------------|-------------|-----------------|-----------|---------------------
May 1    | GPT-5.2 / GPT-5.2-Codex*        | 2026-05-01  | 2026-06-01      | 31 days   | OpenAI
May 7    | GPT-4.1                         | 2026-05-07  | 2026-06-01      | 25 days   | OpenAI
May 7    | Claude Sonnet 4                 | 2026-05-07  | 2026-05-06      | -1 day    | Anthropic
Jul 2    | Gemini 2.5 Pro / Gemini 3 Flash | 2026-07-02  | 2026-07-31      | 29 days   | Google
Jul 31   | Gemini 3.1 Pro / Opus 4.5 /     | 2026-07-31  | 2026-09-01      | 32 days   | Google, Anthropic,
         | Opus 4.6 / Sonnet 4.5 /         |             |                 |           | Microsoft
         | Sonnet 4.6 / Raptor Mini        |             |                 |           |

* GPT-5.2-Codex in Copilot Code Review carved out (see docs-github-copilot-gpt52-deprecation.md)

Successor model designations (this notice):
  Gemini 3.1 Pro    → Gemini 3.6 Flash
  Claude Opus 4.5   → Claude Opus 4.7, 4.8, or 5 (practitioner's choice)
  Claude Opus 4.6   → Claude Opus 4.7, 4.8, or 5 (practitioner's choice)
  Claude Sonnet 4.5 → Claude Sonnet 5
  Claude Sonnet 4.6 → Claude Sonnet 5 (except individual annual-plan subscribers)
  Raptor Mini       → MAI-Code-1-Flash
```

*Derived from this source, `docs-github-copilot-gpt52-deprecation.md`,
`docs-github-copilot-gpt41-deprecation.md`,
`docs-github-copilot-claude-sonnet4-deprecation.md`, and
`docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`*

### Enterprise Migration Checklist for the September 1, 2026 Cutover

```
Before September 1, 2026 — Enterprise Copilot Administrators:

[ ] Audit workflows, scripts, and integrations referencing "gemini-3.1-pro",
    "claude-opus-4.5", "claude-opus-4.6", "claude-sonnet-4.5",
    "claude-sonnet-4.6", or "raptor-mini" as model identifiers.
[ ] Enable Gemini 3.6 Flash in Copilot model policy settings
    (replacement for Gemini 3.1 Pro).
[ ] Enable at least one of Claude Opus 4.7 / 4.8 / 5 in model policy settings
    (replacement for Opus 4.5 and Opus 4.6) — practitioner/org choice among
    three successors, unlike prior single-successor notices.
[ ] Enable Claude Sonnet 5 in model policy settings (replacement for Sonnet
    4.5 and Sonnet 4.6) — UNLESS all affected users are individual
    subscribers on annual plans, in which case Sonnet 4.6 remains usable
    without migration.
[ ] Enable MAI-Code-1-Flash in model policy settings (replacement for
    Raptor Mini).
[ ] Verify availability by checking individual Copilot settings and
    confirming the policy is enabled for each specific model.
[ ] Confirm each replacement model appears in the Copilot Chat model
    selector in VS Code and on github.com.
[ ] Update integration configurations to reference the new model identifiers.

Post-September 1:
  - Gemini 3.1 Pro, Opus 4.5, Opus 4.6, Sonnet 4.5, and Raptor Mini disappear
    automatically. Sonnet 4.6 disappears automatically EXCEPT for individual
    annual-plan subscribers.
  - "No action is required to remove the models once they have been
    deprecated."

Support: "GitHub Enterprise customers with questions or concerns are
          encouraged to reach out to their account manager for further
          assistance."
```

*Source: Required actions section of GitHub Copilot changelog, July 31, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 4,
  `docs-github-copilot-gpt41-deprecation.md` Claim 2,
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 6, and
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 2
  (identical affected-surface boilerplate): this notice repeats the exact
  phrase verbatim, confirming five-for-five that it is fixed boilerplate
  across every provider's deprecation notice.

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 5,
  `docs-github-copilot-gpt41-deprecation.md` Claim 3,
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claims 3-4, and
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 4
  (enterprise admin enable-then-verify procedure), and `docs-github-copilot-gpt41-deprecation.md`
  Claim 4 / `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`
  Claim 5 (automatic removal, no admin action required): both recur
  near-verbatim in this notice, extending the confirmed cross-provider
  standardized playbook to a fifth notice and a fourth provider (Microsoft).

- **Extends** `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`
  Claim 3 (notice-length variability: 31, 25, -1, 29 days across four prior
  notices): this source adds a fifth data point (32 days) — the longest
  advance window in the corpus — further reinforcing that lead time has no
  fixed platform convention.

- **Extends** `docs-github-copilot-claude-sonnet4-deprecation.md` (which
  established the Sonnet-tier deprecation pattern for Claude Sonnet 4 →
  Sonnet 4.6) to the Opus tier for the first time, and extends it again to
  Sonnet 4.5/4.6 → Sonnet 5. Also extends `docs-github-copilot-sonnet5-ga.md`
  Claim 1 (Sonnet 5 reaching GA June 30, 2026) — that note flagged Sonnet
  4.6's continued availability as "not confirmed" pending a future
  deprecation notice; this source is that notice, and resolves the open
  question with a partial answer: Sonnet 4.6 is deprecated for
  Business/Enterprise and individual monthly-plan users, but explicitly
  preserved for individual annual-plan subscribers.

- **Extends** `blog-simonwillison-introducing-opus-5.md` (Opus 5 launch, July
  24, 2026) and `docs-github-copilot-opus48-fast-mode-preview.md` (Opus 4.8
  fast mode preview, June 29, 2026): both named successor models were already
  available in some form before this deprecation notice, consistent with the
  "successor rolled out ahead of predecessor's deprecation" pattern
  documented in `docs-github-copilot-gpt41-deprecation.md` Cross-References
  and `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 8.

- **Extends** `docs-github-copilot-mai-code-1-flash-more-surfaces.md` (MAI-Code-1-Flash
  surface expansion, June 18, 2026): that note documented MAI-Code-1-Flash
  reaching eight additional Copilot surfaces for individual plan tiers about
  six weeks before this notice designates it as Raptor Mini's replacement —
  the model was already broadly available before being named a migration
  target.

- **Extends** `docs-github-copilot-web-model-consolidation.md` Claim 1 and
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Claim 9
  ("deprecation reveals prior undocumented availability" pattern): Raptor
  Mini is a third instance of a model whose Copilot-roster existence the
  corpus learns about only through its removal notice, not its addition.

- **Contradicts**: None identified. The plan-based Sonnet 4.6 carve-out is a
  new carve-out *shape* (plan-based rather than surface-based) but does not
  contradict any existing corpus claim — no prior note asserted that all
  Copilot carve-outs must be surface-based. No contradiction issue required.

- **Novel**:
  - **First deprecation notice spanning three providers simultaneously**
    (Google, Anthropic, Microsoft) — all four prior notices covered at most
    two providers.
  - **First deprecation of Opus-tier Claude models** — prior Claude
    deprecations covered only the Sonnet tier.
  - **First multi-option successor mapping**: Opus 4.5 and Opus 4.6 both map
    to a practitioner's choice of three successors (Opus 4.7, 4.8, or 5)
    rather than one designated replacement, unlike every prior notice's
    single-successor-per-model pattern (including this same notice's other
    five rows, which are all single-successor).
  - **First plan-based (rather than surface-based) carve-out**: Claude
    Sonnet 4.6 remains available specifically to individual annual-plan
    subscribers, contrasting with the GPT-5.2-Codex/Copilot-Code-Review
    surface-based carve-out in `docs-github-copilot-gpt52-deprecation.md`
    Claim 3.
  - **Longest advance-notice window in the corpus**: 32 days, surpassing the
    prior maximum of 31 days (GPT-5.2).
  - **First deprecation notice with no OpenAI/GPT-family model included.**

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: Gemini 3.1 Pro, Claude Opus 4.5, Claude Opus 4.6,
  Claude Sonnet 4.5, and Raptor Mini should be marked deprecated (effective
  September 1, 2026) in any model roster the guide maintains for GitHub
  Copilot; Claude Sonnet 4.6 should be marked deprecated with the annual-plan
  exception noted explicitly, not omitted. Gemini 3.6 Flash, Claude Opus
  4.7/4.8/5, Claude Sonnet 5, and MAI-Code-1-Flash are the confirmed
  replacements.
- **Design principle reinforcement — avoid hardcoded model identifiers**:
  This is the fifth data point (after GPT-5.2, GPT-4.1, Claude Sonnet 4,
  Gemini 2.5 Pro/Gemini 3 Flash) supporting the existing recommendation to
  prefer auto-routing or admin-policy-managed model selection over
  hardcoding model names in Copilot configurations
  (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02). The
  three-way Opus successor choice (4.7, 4.8, or 5) adds a new wrinkle: even
  practitioners who do migrate off a hardcoded identifier now face a
  selection decision among successors rather than a single obvious target —
  the guide should note that "update the model name" is not always a
  mechanical one-to-one substitution.
- **Title-vs-date discrepancy as a changelog-reading caution**: Per Claim 8,
  this notice's title ("August 2026") does not match its effective date
  (September 1). Combined with the "Retired" tag carrying no timing
  information (`docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`
  Claim 7), the guide should state plainly: when reading a Copilot
  deprecation changelog, trust only the explicit dates in the table, not the
  post title or category tag.

### Chapter 05: Team Adoption / Enterprise Governance

- **Plan-based carve-outs as a new governance dimension**: Governance
  checklists that only track *surface*-based carve-outs (e.g., "is this
  model still available in Code Review?") will miss *plan*-based carve-outs
  like the Sonnet 4.6 annual-plan exception. Recommend governance intake
  processes explicitly check both dimensions — surface and plan/subscription
  type — when parsing a new deprecation notice.
  (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch05 already
  covers batch-retirement and recurring-review recommendations; add this
  carve-out-dimension check as a refinement.)
- **Cross-provider deprecation cadence, now four providers deep**: Five
  deprecation notices across OpenAI, Anthropic, Google, and Microsoft within
  roughly three months (May-July 2026) confirm Copilot model-lifecycle
  monitoring is an ongoing, cross-provider governance responsibility
  regardless of which provider(s) a given organization currently uses
  (`docs-github-copilot-claude-sonnet4-deprecation.md` Guide Impact §Ch05;
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` Guide Impact
  §Ch05). This notice extends that conclusion to a fourth provider.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 150
   words of primary text. All extractable facts are captured in the eleven
   claims above. The source provides no explanation for why these six models
   across three providers are being retired together, no capability
   comparison between deprecated and replacement models, and no guidance on
   choosing among the three Opus successor options.
2. **Raw HTML fetched directly, not relied on WebFetch summary alone**:
   WebFetch was used first (two passes) and returned consistent structured
   summaries; both were then verified against the live page's raw HTML
   (`curl --compressed` against the trailing-slash URL) to extract the exact
   article text programmatically. All quotes above are taken from that
   raw-HTML extraction and are character-for-character verbatim from the
   source page as of 2026-08-04. The linked
   `docs.github.com/copilot/reference/ai-models/supported-models` page was
   also fetched (per MINER.md §1's "follow substantive linked pages"
   guidance) to confirm current model availability context, but nothing from
   that page was extracted as a numbered claim here since it documents the
   general current roster rather than anything specific to this deprecation
   event.
3. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-gpt52-deprecation.md`,
   `docs-github-copilot-gpt41-deprecation.md`,
   `docs-github-copilot-claude-sonnet4-deprecation.md`,
   `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`,
   `docs-github-copilot-sonnet5-ga.md`, and
   `docs-github-copilot-mai-code-1-flash-more-surfaces.md` were checked
   against those notes' actual claim numbering (each note re-read in full
   before citing); none were guessed.
4. **No contradictions filed**: The plan-based Sonnet 4.6 carve-out is a new
   carve-out shape but does not conflict with any existing corpus claim. No
   contradiction issue required.
5. **Prospector's triage framing**: The triage comment on issue #2471 asked
   what "transient model availability and forced vendor-driven migrations"
   tell us about abstraction and resilience patterns, and flagged Ch02/Ch04/Ch05
   as relevant. This note follows the existing deprecation-family notes in
   addressing Ch02 and Ch05 specifically (harness/tooling roster hygiene and
   enterprise governance), since those are the two chapters the four prior
   notices in this family have consistently updated; no Ch04-specific claim
   emerged from this source's content beyond what Ch02/Ch05 already cover.
