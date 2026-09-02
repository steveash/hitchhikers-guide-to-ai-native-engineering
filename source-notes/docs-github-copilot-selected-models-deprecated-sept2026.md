---
source_url: https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated
source_type: docs
title: "Selected GitHub Copilot models deprecated"
author: GitHub (official changelog)
date_published: 2026-08-31
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: settled
issue: "#3156"
---

# Selected GitHub Copilot Models Deprecated (September 1, 2026 Confirmation)

> GitHub's August 31, 2026 changelog entry — the implementation-day
> confirmation of the six-model deprecation pre-announced on July 31, 2026 —
> confirms the same September 1, 2026 cutover but names different successor
> models for two of the six: Gemini 3.1 Pro now maps to Gemini 3.7 Flash
> (not the 3.6 Flash named a month earlier) and Raptor Mini now maps to
> MAI-Code-1.1-Flash (not MAI-Code-1-Flash), while all four Claude successor
> mappings are unchanged. Filed as contradiction #3170.

## Source Context

- **Type**: docs (GitHub official product changelog, August 31, 2026; ~110
  words of primary announcement text, "1 minute read," category-tagged
  "Retired" — confirmed via direct raw-HTML fetch with `curl --compressed`,
  not just a WebFetch summary)
- **Author credibility**: GitHub engineering team. Authoritative for which
  models were actually deprecated on the stated effective date, their
  successor designations as stated on this page, and the Sonnet 4.6
  annual-plan carve-out. Not a source for why the successor designations for
  Gemini 3.1 Pro and Raptor Mini differ from the July 31 pre-announcement —
  the page does not acknowledge or explain the change.
- **Scope**: Confirms deprecation of the same six named models covered in
  `docs-github-copilot-aug2026-model-deprecations.md`, effective September
  1, 2026, across "most GitHub Copilot experiences." Covers the successor
  model(s) named for each on this page, the Sonnet 4.6 carve-out, and the
  standard enable-then-verify admin procedure. Does NOT cover: why the
  Gemini and Raptor Mini successor names changed since the pre-announcement,
  capability differences between deprecated and replacement models, or cost
  implications of migration.

## Extracted Claims

### Claim 1: This changelog entry is GitHub's implementation-day confirmation of the same six-model deprecation pre-announced a month earlier, restated in the past/present tense rather than the future tense used in the pre-announcement

- **Evidence**: Direct textual comparison of the opening sentence in this
  source against the equivalent sentence in
  `docs-github-copilot-aug2026-model-deprecations.md` Concrete Artifacts
  (full article text).
- **Confidence**: settled (both texts are directly quotable and the tense
  shift is unambiguous)
- **Quote**: "As of today, September 1, 2026, we have deprecated the
  following models across most GitHub Copilot experiences (including
  Copilot Chat, inline edits, ask and agent modes, and code completions)."
- **Our assessment**: The July 31 notice used "We will deprecate the
  following models... on September 1st, 2026" (future tense, advance
  notice). This entry uses "we have deprecated" (perfect tense, action
  already taken). This is the first instance in the corpus's deprecation
  family of GitHub publishing two separate changelog entries for a single
  deprecation event — one pre-announcement, one implementation-day
  confirmation — rather than the single-notice pattern seen in every prior
  corpus deprecation (`docs-github-copilot-gpt52-deprecation.md`,
  `docs-github-copilot-gpt41-deprecation.md`,
  `docs-github-copilot-claude-sonnet4-deprecation.md`,
  `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`).

### Claim 2: The page's own publish-date metadata (August 31, 2026) does not match the "today" referenced in its own body text (September 1, 2026)

- **Evidence**: Page header timestamp versus the opening sentence of the
  article body, both extracted from the same raw-HTML fetch.
- **Confidence**: settled (both strings are directly observable on the same
  page; the significance we assign the mismatch is our interpretation)
- **Quote**: "August 31, 2026 •" (page header/byline); "As of today,
  September 1, 2026, we have deprecated the following models" (article
  body, first sentence)
- **Our assessment**: The page's own metadata says it was published August
  31, but its lead sentence describes "today" as September 1. This is
  likely a scheduling/timezone artifact (the post may have been queued to
  publish at a UTC boundary that reads as August 31 in the changelog's
  timestamp system but was written to describe the day the cutover takes
  effect), but the source does not explain it. Combined with Claim 8 of
  `docs-github-copilot-aug2026-model-deprecations.md` (title-vs-date
  mismatch in the July 31 notice) and Claim 2 of
  `docs-github-copilot-claude-sonnet4-deprecation.md` (notice published one
  day after its own effective date), this is now a third instance across
  the corpus's deprecation family of a Copilot deprecation changelog
  entry's own internal dates not lining up cleanly — reinforcing the
  existing guide caution to trust only the per-model dates in the table,
  not surrounding prose or metadata.

### Claim 3: The affected-surface wording narrows from "all" to "most" GitHub Copilot experiences, compared to the July 31 pre-announcement and every other prior corpus deprecation notice

- **Evidence**: Direct textual comparison of the affected-surface clause in
  this source against the identical clause quoted in five prior corpus
  notices.
- **Confidence**: settled (the word-for-word text is directly quotable in
  both sources; whether this reflects an actual narrower scope or is
  incidental wording drift is not stated by the source)
- **Quote**: "across most GitHub Copilot experiences (including Copilot
  Chat, inline edits, ask and agent modes, and code completions)"
- **Our assessment**: Every prior corpus notice — including this same
  event's own July 31 pre-announcement (`docs-github-copilot-aug2026-model-deprecations.md`
  Claim 2) — used "all GitHub Copilot experiences" with the identical
  parenthetical surface list. This entry is the first to swap "all" for
  "most" while listing the exact same four example surfaces and stating no
  specific exclusion. The source does not identify which surface(s), if
  any, are now excluded, so we cannot confirm whether this is a substantive
  scope narrowing or an unannounced copy-editing variation. Flagged here
  rather than filed as a contradiction, since "most" is consistent with
  (a superset including) "all" and no specific surface is named as exempt
  — there is no concrete opposing claim to adjudicate.

### Claim 4: Gemini 3.1 Pro's suggested alternative is now stated as Gemini 3.7 Flash — one point release ahead of the Gemini 3.6 Flash named in the July 31 pre-announcement for the same model and the same September 1 cutover

- **Evidence**: Deprecation table row, extracted from raw HTML fetched
  directly via `curl --compressed` on 2026-09-02.
- **Confidence**: settled (directly stated in a structured table; the
  discrepancy with the prior notice is a directly observable textual
  comparison)
- **Quote**: "Gemini 3.1 Pro | 2026-09-01 | Gemini 3.7 Flash"
- **Our assessment**: This contradicts `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 1, which quotes the July 31 pre-announcement's table row as
  "Gemini 3.1 Pro | 9-1-2026 | Gemini 3.6 Flash" for the identical model and
  identical effective date. Filed as contradiction #3170. Neither source
  explains the successor-name change; the most plausible reading is that
  Gemini 3.7 Flash shipped in the 31-day gap between the two notices and
  GitHub updated the "suggested alternative" column without flagging the
  change, but that is our inference, not a stated fact.

### Claim 5: Raptor Mini's suggested alternative is now stated as MAI-Code-1.1-Flash — a minor-version increment ahead of the MAI-Code-1-Flash named in the July 31 pre-announcement for the same model and the same September 1 cutover

- **Evidence**: Deprecation table row, extracted from raw HTML fetched
  directly via `curl --compressed` on 2026-09-02.
- **Confidence**: settled (directly stated in a structured table; the
  discrepancy with the prior notice is a directly observable textual
  comparison)
- **Quote**: "Raptor Mini | 2026-09-01 | MAI-Code-1.1-Flash"
- **Our assessment**: This contradicts `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 1, which quotes the July 31 pre-announcement's table row as
  "Raptor Mini | 9-1-2026 | MAI-Code-1-Flash." Filed as contradiction #3170
  (same issue as Claim 4 — both successor changes were surfaced and filed
  together since they come from the same two source pages). Practitioners
  who read `docs-github-copilot-mai-code-1-flash-more-surfaces.md` and the
  July 31 notice and standardized on the identifier "MAI-Code-1-Flash" will
  find this confirmation notice instead pointing at "MAI-Code-1.1-Flash."
  The source does not state whether "MAI-Code-1-Flash" continues to work as
  an alias or was itself superseded.

### Claim 6: All four Claude successor mappings (Opus 4.5, Opus 4.6, Sonnet 4.5, Sonnet 4.6) are unchanged from the July 31 pre-announcement — only the two non-Claude models' successor names moved

- **Evidence**: Direct row-by-row comparison of this source's deprecation
  table against the July 31 table quoted in
  `docs-github-copilot-aug2026-model-deprecations.md` Concrete Artifacts.
- **Confidence**: settled (both tables are directly quotable and the
  comparison is mechanical)
- **Quote**: "Claude Opus 4.5 | 2026-09-01 | Claude Opus 4.7, Claude Opus
  4.8, or Claude Opus 5"; "Claude Opus 4.6 | 2026-09-01 | Claude Opus 4.7,
  Claude Opus 4.8, or Claude Opus 5"; "Claude Sonnet 4.5 | 2026-09-01 |
  Claude Sonnet 5"; "Claude Sonnet 4.6 | 2026-09-01 | Claude Sonnet 5"
- **Our assessment**: The successor drift documented in Claims 4-5 is
  specific to the Gemini and Microsoft in-house rows; the Anthropic
  successor guidance a practitioner would have acted on from the July 31
  notice (migrate Opus 4.5/4.6 to a choice of 4.7/4.8/5, migrate Sonnet
  4.5/4.6 to Sonnet 5) remains correct and unrevised a month later. This
  narrows the practical impact of the contradiction to Gemini-3.1-Pro and
  Raptor-Mini migrators specifically.

### Claim 7: Claude Sonnet 4.6 remains available to individual GitHub Copilot subscribers on annual plans, restated as a lead-paragraph sentence rather than a table footnote

- **Evidence**: Opening paragraph of the article body.
- **Confidence**: settled (stated directly and unambiguously)
- **Quote**: "Note that Claude Sonnet 4.6 is still available to individual
  GitHub Copilot subscribers on annual plans."
- **Our assessment**: Substantively identical to the carve-out documented in
  `docs-github-copilot-aug2026-model-deprecations.md` Claim 4, but delivered
  as a same-paragraph aside ("Note that...") rather than a separate
  asterisked footnote below the table. The table row itself for Claude
  Sonnet 4.6 in this source carries no asterisk, unlike the July 31 table's
  "Claude Sonnet 4.6*" row — the carve-out is stated once, in prose, instead
  of being cross-referenced from the table. This is a presentation change,
  not a substantive change to the carve-out's scope.

### Claim 8: Enterprise administrators must proactively enable alternative models via Copilot model policies, and no admin action is required to remove the deprecated models — the same enable-then-verify and auto-removal procedure documented in every prior corpus deprecation notice

- **Evidence**: Required-actions paragraph, closing the article body.
- **Confidence**: settled (stated directly in the official changelog)
- **Quote**: "Please update your workflows and integrations to use
  supported models. Copilot Enterprise administrators may need to enable
  access to alternative models through their model policies in Copilot
  settings. As an administrator, you can verify availability by checking
  your individual Copilot settings and confirming that the policy is
  enabled for the specific model. Once enabled, you'll see the model in the
  Copilot Chat model selector in VS Code and on github.com. No action is
  required to remove the deprecated models."
- **Our assessment**: Near-verbatim match to the equivalent paragraph in
  `docs-github-copilot-aug2026-model-deprecations.md` Claim 5, itself a
  match to four earlier notices. The closing sentence is slightly
  reworded ("No action is required to remove the deprecated models" versus
  the July 31 notice's "No action is required to remove the models once
  they have been deprecated") but states the identical policy. This is now
  the sixth corpus notice — and the first same-event confirmation notice —
  to restate this fixed enable-then-verify/auto-removal playbook, further
  reinforcing it as GitHub's standardized (not notice-specific) governance
  mechanism.

### Claim 9: GitHub Enterprise customers with questions are directed to their account manager — the same support channel named in every prior corpus notice, including this event's own July 31 pre-announcement

- **Evidence**: Closing sentence of the changelog body.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "GitHub Enterprise customers with questions or concerns are
  encouraged to reach out to their account manager for further
  assistance."
- **Our assessment**: Word-for-word identical to the equivalent sentence in
  `docs-github-copilot-aug2026-model-deprecations.md` Claim 7 and the three
  notices that claim cites. No new support channel is introduced for the
  confirmation notice.

## Concrete Artifacts

### Full Article Text (verbatim, extracted from raw page HTML via direct curl fetch)

```
Selected GitHub Copilot models deprecated

As of today, September 1, 2026, we have deprecated the following models
across most GitHub Copilot experiences (including Copilot Chat, inline
edits, ask and agent modes, and code completions). Note that Claude Sonnet
4.6 is still available to individual GitHub Copilot subscribers on annual
plans.

Model               Deprecation date    Suggested alternative
Gemini 3.1 Pro       2026-09-01          Gemini 3.7 Flash
Claude Opus 4.5      2026-09-01          Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5
Claude Opus 4.6      2026-09-01          Claude Opus 4.7, Claude Opus 4.8, or Claude Opus 5
Claude Sonnet 4.5    2026-09-01          Claude Sonnet 5
Claude Sonnet 4.6    2026-09-01          Claude Sonnet 5
Raptor Mini          2026-09-01          MAI-Code-1.1-Flash

Please update your workflows and integrations to use supported models.
Copilot Enterprise administrators may need to enable access to alternative
models through their model policies in Copilot settings. As an
administrator, you can verify availability by checking your individual
Copilot settings and confirming that the policy is enabled for the specific
model. Once enabled, you'll see the model in the Copilot Chat model
selector in VS Code and on github.com. No action is required to remove the
deprecated models.

GitHub Enterprise customers with questions or concerns are encouraged to
reach out to their account manager for further assistance.

To learn more about the models available in Copilot, see our documentation
on models and get started with Copilot today.
```

*Source: raw HTML of
https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated/,
fetched directly via `curl --compressed` (not WebFetch summarization) on
2026-09-02. Page metadata: category tag "Retired," byline "August 31, 2026,"
"1 minute read."*

### Successor-Mapping Diff: July 31 Pre-Announcement vs. August 31 Confirmation

```
Model              | July 31 successor (pre-announcement)    | Aug 31 successor (confirmation)  | Changed?
-------------------|------------------------------------------|-----------------------------------|----------
Gemini 3.1 Pro     | Gemini 3.6 Flash                          | Gemini 3.7 Flash                   | YES
Claude Opus 4.5    | Opus 4.7, 4.8, or 5                       | Opus 4.7, 4.8, or 5                 | no
Claude Opus 4.6    | Opus 4.7, 4.8, or 5                       | Opus 4.7, 4.8, or 5                 | no
Claude Sonnet 4.5  | Claude Sonnet 5                            | Claude Sonnet 5                     | no
Claude Sonnet 4.6  | Claude Sonnet 5 (annual-plan carve-out)   | Claude Sonnet 5 (annual-plan carve-out) | no
Raptor Mini        | MAI-Code-1-Flash                          | MAI-Code-1.1-Flash                  | YES
```

*Derived by comparing this source's table against
`docs-github-copilot-aug2026-model-deprecations.md` Concrete Artifacts
(Deprecation Table). Filed as contradiction issue #3170.*

## Cross-References

- **Corroborates** `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 5 (enable-then-verify admin procedure, auto-removal, no admin
  action for removal) and Claim 7 (account-manager support channel): both
  restated near-verbatim in this confirmation notice.

- **Corroborates** `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 4 (Claude Sonnet 4.6's individual-annual-plan carve-out): restated
  in this source, in prose rather than a table footnote, with identical
  substance.

- **Contradicts** `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 1: the successor models named for Gemini 3.1 Pro (Gemini 3.6 Flash
  → Gemini 3.7 Flash) and Raptor Mini (MAI-Code-1-Flash → MAI-Code-1.1-Flash)
  differ between the July 31 pre-announcement and this August 31
  confirmation, for the identical deprecation event and cutover date. Filed
  as **contradiction issue #3170**. See Claims 4-5 above and the
  Successor-Mapping Diff artifact.

- **Extends** `docs-github-copilot-mai-code-1-flash-more-surfaces.md`
  (MAI-Code-1-Flash surface expansion, June 18, 2026): that note documents
  the "MAI-Code-1-Flash" identifier reaching broad availability; this
  source's confirmation table now points migrators at "MAI-Code-1.1-Flash"
  instead, meaning the surface-expansion note's identifier is no longer the
  one named in the operative deprecation guidance.

- **Novel**:
  - **First same-event confirmation notice in the corpus's deprecation
    family**: GitHub published two separate changelog entries — a July 31
    pre-announcement and this August 31 implementation-day confirmation —
    for a single deprecation event, rather than the single-notice pattern
    in all four prior corpus deprecation notices.
  - **First documented case of a Copilot deprecation notice's own successor
    guidance changing between pre-announcement and confirmation** for the
    same model and cutover date (Gemini 3.1 Pro, Raptor Mini).
  - **First "most" (rather than "all") GitHub Copilot experiences** phrasing
    in the affected-surface boilerplate, with no stated exclusion (Claim 3).

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update — use this note's successor names, not the July 31
  note's, for Gemini 3.1 Pro and Raptor Mini**: Any guide-maintained Copilot
  model roster should record Gemini 3.1 Pro's replacement as Gemini 3.7
  Flash and Raptor Mini's replacement as MAI-Code-1.1-Flash, per this
  implementation-day source — not the Gemini 3.6 Flash / MAI-Code-1-Flash
  values from `docs-github-copilot-aug2026-model-deprecations.md`. The four
  Claude successor mappings from the July 31 note remain correct.
- **New caution — pre-announcement successor names can drift by the
  effective date**: This is the first corpus evidence that a Copilot
  deprecation notice's stated successor model can change between its
  advance notice and its implementation-day confirmation. The guide should
  add a caution alongside the existing "avoid hardcoded model identifiers"
  recommendation (`docs-github-copilot-gpt52-deprecation.md` Guide Impact
  §Ch02): practitioners who migrate immediately upon reading a
  pre-announcement should re-check the changelog on or after the effective
  date in case the specific successor point-release has moved.
- **Trust dates over prose, extended to publish-date metadata**: Building on
  the "read the dates, not the label" caution from
  `docs-github-copilot-aug2026-model-deprecations.md` Guide Impact §Ch02,
  this note's own publish-date/body-text mismatch (Claim 2) shows the
  caution should extend to the page's own byline timestamp, not just the
  title and category tag.

### Chapter 05: Team Adoption / Enterprise Governance

- **Governance checklists should re-verify successor identifiers at the
  effective date, not just at pre-announcement time**: Extending
  `docs-github-copilot-aug2026-model-deprecations.md` Guide Impact §Ch05's
  enterprise-governance recommendations, an admin who enabled
  "Gemini 3.6 Flash" or "MAI-Code-1-Flash" in model policy settings upon
  reading the July 31 notice should re-check policy settings against this
  confirmation notice's table, since the officially suggested identifiers
  changed for those two models before the cutover took effect.

## Extraction Notes

1. **Raw HTML fetched directly, not relied on WebFetch summary alone**:
   WebFetch was used first and returned a consistent structured summary
   (matching successor changes); it was then verified against the live
   page's raw HTML (`curl --compressed` against the trailing-slash URL) to
   extract the exact article text programmatically. All quotes above are
   taken from that raw-HTML extraction and are character-for-character
   verbatim from the source page as of 2026-09-02.
2. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-aug2026-model-deprecations.md`,
   `docs-github-copilot-gpt52-deprecation.md`,
   `docs-github-copilot-claude-sonnet4-deprecation.md`,
   `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md`, and
   `docs-github-copilot-mai-code-1-flash-more-surfaces.md` were checked
   against those notes' actual claim numbering (each note re-read in full
   before citing); none were guessed.
3. **Contradiction filed before this PR was opened**: Issue #3170
   documents the Gemini 3.1 Pro and Raptor Mini successor-name discrepancy
   between this source and `docs-github-copilot-aug2026-model-deprecations.md`,
   per MINER.md §4a. No verdict is asserted in this note; the filer's
   recommended verdict (accepted-B, favoring this confirmation notice as
   operative for current migrations) is recorded only in issue #3170 for
   human resolution.
4. **Source is thin by design**: The changelog is approximately 110 words
   of primary text, shorter than the July 31 pre-announcement it confirms.
   All extractable facts are captured in the nine claims above. The source
   does not link to or acknowledge the July 31 pre-announcement, and does
   not explain why two of the six successor names changed.
5. **Prospector's triage framing**: Three separate triage comments were
   left on issue #3156, each independently flagging the Gemini/Raptor Mini
   successor discrepancy with the July 31 notice and asking the Miner to
   verify it. This note's Claims 4-5 and the filed contradiction (#3170)
   directly answer that question with a verbatim side-by-side comparison.
