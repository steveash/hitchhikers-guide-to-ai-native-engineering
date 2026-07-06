---
source_url: https://github.blog/changelog/2026-07-02-upcoming-deprecation-of-gemini-2-5-pro-and-gemini-3-flash
source_type: docs
title: "Upcoming deprecation of Gemini 2.5 Pro and Gemini 3 Flash"
author: GitHub (official changelog)
date_published: 2026-07-02
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: settled
issue: "#1578"
---

# Upcoming Deprecation of Gemini 2.5 Pro and Gemini 3 Flash

> GitHub's July 2, 2026 changelog retiring Gemini 2.5 Pro and Gemini 3 Flash from all Copilot
> experiences on July 31, 2026 — with Gemini 3.1 Pro and Gemini 3.5 Flash as the named
> replacements, a 29-day advance notice window, and the same enterprise admin pre-migration
> requirement seen in the GPT-4.1/GPT-5.2/Claude Sonnet 4 notices — while also exposing that
> the "Retired" changelog category tag GitHub applies to this and to prior *advance-notice*
> deprecation posts is not, as an earlier corpus note assumed, a signal of retroactive timing.

## Source Context

- **Type**: docs (GitHub official product changelog, ~130 words of primary announcement
  text; July 2, 2026; category-tagged "Retired" on the page itself)
- **Author credibility**: GitHub engineering team. Authoritative for the deprecation date,
  successor model designations, affected surfaces, and enterprise admin requirements. Not a
  source for capability comparisons between Gemini 2.5 Pro/Gemini 3 Flash and their
  replacements, migration effort estimation, or cost implications.
- **Scope**: Deprecation of Gemini 2.5 Pro and Gemini 3 Flash from "all GitHub Copilot
  experiences (including Copilot Chat, inline edits, ask and agent modes, and code
  completions)," effective July 31, 2026. Covers the two replacement models and the admin
  action required for Enterprise teams. Does NOT cover: which specific Copilot surfaces
  (CLI, cloud agent, web, VS Code, app, SDK) actually exposed Gemini 2.5 Pro or Gemini 3
  Flash before this notice, capability differences between the deprecated and replacement
  models, cost/pricing implications, or why these two models are being retired together.

## Extracted Claims

### Claim 1: Gemini 2.5 Pro and Gemini 3 Flash are deprecated across all GitHub Copilot experiences effective July 31, 2026, with Gemini 3.1 Pro and Gemini 3.5 Flash as the respective suggested replacements

- **Evidence**: Official GitHub Copilot changelog. Deprecation date and per-model successor
  stated directly in a structured table.
- **Confidence**: settled (authoritative product fact — dates and successors stated directly)
- **Quote**: "We will deprecate Gemini 2.5 Pro and Gemini 3 Flash across all GitHub Copilot
  experiences (including Copilot Chat, inline edits, ask and agent modes, and code
  completions) on July 31st, 2026:" followed by a table pairing "Gemini 2.5 Pro | 7-31-2026 |
  Gemini 3.1 Pro" and "Gemini 3 Flash | 7-31-2026 | Gemini 3.5 Flash"
- **Our assessment**: This is the fourth Copilot model deprecation notice in the corpus
  (after `docs-github-copilot-gpt52-deprecation.md`, `docs-github-copilot-gpt41-deprecation.md`,
  and `docs-github-copilot-claude-sonnet4-deprecation.md`) and the **first involving
  Google/Gemini-family models**. Unlike the GPT-4.1/GPT-5.2 batch (both converging on the
  single replacement GPT-5.5), each deprecated Gemini model gets its own distinct successor —
  Gemini 2.5 Pro → Gemini 3.1 Pro (a same-tier Pro-to-Pro upgrade), Gemini 3 Flash → Gemini
  3.5 Flash (a same-tier Flash-to-Flash upgrade). Practitioners should map old-to-new by
  matching tier name, not assume a single universal successor as with the GPT batch.

### Claim 2: The deprecation affects Copilot Chat, inline edits, ask and agent modes, and code completions, with no stated carve-outs

- **Evidence**: The changelog explicitly enumerates the affected surfaces in the same
  sentence that announces the deprecation, and lists no exceptions.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and
  agent modes, and code completions)"
- **Our assessment**: Identical affected-surface phrasing to the GPT-5.2, GPT-4.1, and
  Claude Sonnet 4 notices (`docs-github-copilot-gpt52-deprecation.md` Claim 4,
  `docs-github-copilot-gpt41-deprecation.md` Claim 2, `docs-github-copilot-claude-sonnet4-deprecation.md`
  Claim 6) — confirming this exact sentence is boilerplate GitHub reuses across every model
  deprecation regardless of provider. No carve-out is stated, unlike the GPT-5.2-Codex/Copilot
  Code Review exception in the May 1 notice. Practitioners using Gemini 2.5 Pro or Gemini 3
  Flash anywhere in Copilot should treat July 31 as an unconditional cutoff.

### Claim 3: The notice-to-cutoff window is 29 days (published July 2, 2026; effective July 31, 2026)

- **Evidence**: Changelog publish date (July 2, 2026, per the page's `datetime="2026-07-02"`
  attribute and visible date) and the stated deprecation date (July 31, 2026) in the table.
- **Confidence**: settled (both dates stated directly in the official source)
- **Quote**: "Gemini 2.5 Pro | 7-31-2026 | Gemini 3.1 Pro" / "Gemini 3 Flash | 7-31-2026 |
  Gemini 3.5 Flash" (deprecation table); page dated "July 2, 2026"
- **Our assessment**: 29 days sits between the GPT-5.2 notice (31 days: May 1 → June 1) and
  the GPT-4.1 notice (25 days: May 7 → June 1), and far exceeds the Claude Sonnet 4 notice
  (-1 day, retroactive). Across four corpus deprecation notices the lead time is now 31, 25,
  -1, and 29 days — confirming `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 8's
  conclusion that notice length is genuinely variable per-model rather than following any
  fixed platform convention. Practitioners cannot assume a specific number of days' notice
  from any past pattern; each notice must be read individually for its own cutoff date.

### Claim 4: Copilot Enterprise administrators must proactively enable the replacement models via Copilot model policies — no automatic migration of admin policies occurs

- **Evidence**: Changelog states administrators "may need to enable access to the alternative
  models through their model policies in Copilot settings," with an explicit verification
  step described.
- **Confidence**: settled (required action stated directly in official changelog)
- **Quote**: "Copilot Enterprise administrators may need to enable access to the alternative
  models through their model policies in Copilot settings. As an administrator, you can
  verify availability by checking your individual Copilot settings and confirming that the
  policy is enabled for the specific model. Once enabled, you'll see the model in the
  Copilot Chat model selector in VS Code and on github.com."
- **Our assessment**: This is verbatim the same two-step pattern (enable in policy settings
  → verify in the model selector) documented in `docs-github-copilot-gpt52-deprecation.md`
  Claim 5, `docs-github-copilot-gpt41-deprecation.md` Claim 3, and
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claims 3–4. Four consecutive
  deprecation notices across three different model providers (OpenAI, Anthropic, Google) now
  confirm this is GitHub's standardized enterprise governance procedure for Copilot model
  deprecations, not a provider-specific quirk. Enterprise teams that have not enabled Gemini
  3.1 Pro and Gemini 3.5 Flash in their model policy before July 31 will find Gemini 2.5 Pro
  and Gemini 3 Flash simply disappear with no automatic replacement.

### Claim 5: After deprecation, the old models disappear automatically — no admin action is required for removal

- **Evidence**: Changelog states removal is automatic and requires no admin action.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "No action is required to remove the older models once they have been
  deprecated."
- **Our assessment**: Near-identical wording to `docs-github-copilot-gpt41-deprecation.md`
  Claim 4 ("No action is required to remove the models once they have been deprecated") and
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 5 ("No action is required to
  remove the deprecated models"). This confirms auto-removal, with no admin cleanup step, as
  a settled cross-provider pattern across all four corpus deprecation notices.

### Claim 6: GitHub Enterprise customers with questions are directed to their account manager — no other support channel is named for this deprecation

- **Evidence**: Closing sentence of the changelog's required-action guidance.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "GitHub Enterprise customers with questions or concerns are encouraged to reach
  out to their account manager for further assistance."
- **Our assessment**: Identical support-channel language to the GPT-5.2 and GPT-4.1 notices.
  No self-service escalation path (support ticket, community forum) is offered for
  deprecation-specific concerns beyond the general community discussions link at the foot of
  the page; Enterprise is the only tier given a named contact.

### Claim 7: The changelog page carries the "Retired" category tag despite being a 29-day advance notice, not a retroactive announcement — the same tag also appears on the GPT-5.2 and GPT-4.1 advance-notice pages, contradicting an earlier corpus note's use of that tag as a retroactive-timing signal

- **Evidence**: Direct inspection of this page's raw HTML shows `<span class="Tag
  Tag--type">Retired</span>` in the page header, alongside the July 2 publish date and the
  July 31 (future, 29-days-out) effective date. Cross-checking the raw HTML of
  `https://github.blog/changelog/2026-05-07-upcoming-deprecation-of-gpt-4-1/` and
  `https://github.blog/changelog/2026-05-01-upcoming-deprecation-of-gpt-5-2-and-gpt-5-2-codex/`
  — both confirmed by the existing corpus as genuine advance-notice deprecations (25 and 31
  days respectively) — shows the identical `Tag Tag--type">Retired` markup on those pages too.
- **Confidence**: settled (verified directly against raw page HTML for three separate
  changelog URLs, not inferred from a WebFetch summary)
- **Quote**: `<span class="Tag Tag--type">Retired</span>` (identical markup on this page and
  on the GPT-4.1 and GPT-5.2 deprecation pages)
- **Our assessment**: `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 2 asserted
  that "the word 'Retired' distinguishes this post from GPT-5.2 and GPT-4.1 notices, which
  were labeled as upcoming" — treating the tag as evidence that the Claude Sonnet 4 notice
  was uniquely retroactive. That is not correct: "Retired" is GitHub's standing changelog
  *category* tag for the deprecation/retirement post type, applied uniformly whether the
  post is an advance notice (this source, GPT-4.1, GPT-5.2) or a retroactive one (Claude
  Sonnet 4). The tag carries no timing information; only the dates in the post body and
  table do. **This contradicts a specific evidentiary claim in
  `docs-github-copilot-claude-sonnet4-deprecation.md` — contradiction issue #1595 filed.**
  The broader, separately-supported conclusion in that note (Claude Sonnet 4's notice really
  was published one day after its effective date, i.e., genuinely retroactive) is not
  affected, since that rests on the dated table, not the tag.

### Claim 8: The designated replacement models (Gemini 3.1 Pro and Gemini 3.5 Flash) had already been rolled out to Copilot CLI, cloud agent, the Copilot app, and the Copilot SDK a full month before this deprecation notice

- **Evidence**: `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 1 documents a June
  2, 2026 changelog announcing "Gemini 3.1 Pro (Preview) and Gemini 3.5 Flash can now be
  used in" Copilot CLI, cloud agent, the Copilot app, and the Copilot SDK.
- **Confidence**: emerging (the two facts are each settled individually; the inference that
  the June 2 rollout was preparation for this July 2 deprecation is our synthesis, not
  stated in either source)
- **Quote**: (no direct quote; comparison across this source and
  `docs-github-copilot-gemini-cli-cloud-agent-app.md`)
- **Our assessment**: This mirrors the pattern already established for the GPT-5.5 rollout
  ahead of the GPT-5.2/GPT-4.1 cutover (`docs-github-copilot-gpt41-deprecation.md`
  Cross-References): the successor model becomes selectable in at least some Copilot
  surfaces well before the predecessor's formal deprecation notice, giving practitioners who
  proactively adopt new models a head start on migration. One open question this raises but
  does not resolve: the June 2 note documented Gemini 3.1 Pro as "(Preview)"-qualified, while
  this July 2 deprecation table lists it simply as "Gemini 3.1 Pro" with no Preview
  qualifier — suggesting it may have exited preview status between June 2 and July 2, though
  neither source states this explicitly.

### Claim 9: This notice is the first corpus confirmation that Gemini 2.5 Pro and Gemini 3 Flash were part of GitHub Copilot's model roster at all — no prior corpus source documented either model's addition to any Copilot surface

- **Evidence**: A search of the existing corpus for "Gemini 2.5 Pro" and "Gemini 3 Flash"
  turns up only capability/benchmark and third-party pricing references
  (`blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 10, `blog-jetbrains-codex-recommended-agent.md`
  Claim 6, `blog-simonwillison-deepseek-v4.md`, `blog-simonwillison-gemini35-flash-pricing.md`
  Claim 2, `blog-thebatch-fde-agents-aiact-issue355.md` Claim 6) — none of which document
  either model being available specifically within GitHub Copilot.
- **Confidence**: emerging (absence-from-corpus is a corpus-completeness observation, not a
  claim the source itself makes)
- **Quote**: (no direct quote; corpus-search finding)
- **Our assessment**: This is the same "deprecation reveals prior existence" pattern seen in
  `docs-github-copilot-web-model-consolidation.md` Claim 1 (which revealed, via removal, that
  unspecified Gemini models had been in Copilot web chat). Here, the two specific models
  (Gemini 2.5 Pro, Gemini 3 Flash) are named for the first time in the corpus, but only
  because they are being retired — their addition to Copilot was never separately announced
  or captured. Practitioners relying on the corpus as a complete model-availability timeline
  should treat this as a reminder that gaps exist: models can enter and leave Copilot's
  roster without a "here's a new model" changelog entry ever surfacing in this corpus.

## Concrete Artifacts

### Deprecation Table (from changelog, July 2, 2026)

```
GitHub Copilot Model Deprecation — Effective July 31, 2026

| Model          | Deprecation Date | Suggested Alternative |
|----------------|-------------------|------------------------|
| Gemini 2.5 Pro | 7-31-2026         | Gemini 3.1 Pro         |
| Gemini 3 Flash | 7-31-2026         | Gemini 3.5 Flash       |

No exceptions or carve-outs stated.
Affected surfaces: all GitHub Copilot experiences (Copilot Chat, inline edits,
                   ask and agent modes, code completions).
Page category tag: "Retired"
```

*Source: GitHub Copilot official changelog, July 2, 2026*

### Full Article Text (verbatim, extracted from raw page HTML)

```
Upcoming deprecation of Gemini 2.5 Pro and Gemini 3 Flash

We will deprecate Gemini 2.5 Pro and Gemini 3 Flash across all GitHub Copilot
experiences (including Copilot Chat, inline edits, ask and agent modes, and code
completions) on July 31st, 2026:

Model            Deprecation date    Suggested alternative
Gemini 2.5 Pro   7-31-2026           Gemini 3.1 Pro
Gemini 3 Flash   7-31-2026           Gemini 3.5 Flash

Please update your workflows and integrations to use the supported models before
these dates. Copilot Enterprise administrators may need to enable access to the
alternative models through their model policies in Copilot settings. As an
administrator, you can verify availability by checking your individual Copilot
settings and confirming that the policy is enabled for the specific model. Once
enabled, you'll see the model in the Copilot Chat model selector in VS Code and
on github.com. No action is required to remove the older models once they have
been deprecated.

GitHub Enterprise customers with questions or concerns are encouraged to reach
out to their account manager for further assistance.

To learn more about the models available in Copilot, see our documentation on
models and get started with Copilot today.
```

*Source: raw HTML of https://github.blog/changelog/2026-07-02-upcoming-deprecation-of-gemini-2-5-pro-and-gemini-3-flash/,
fetched directly via curl (not WebFetch summarization) on 2026-07-06. Tag: "Retired".
Published: July 2, 2026. Read time: "1 minute read." Links out to
docs.github.com/copilot/reference/ai-models/supported-models (models documentation) and
github.com/orgs/community/discussions/categories/copilot-conversations (community feedback).*

### Cross-Notice Deprecation Timeline (derived from four corpus sources)

```
GitHub Copilot Model Deprecations — Corpus Timeline (as of July 2026)

Notice   | Model(s)                    | Notice Date | Effective Date | Lead Time | Tag
---------|------------------------------|-------------|-----------------|-----------|--------
May 1    | GPT-5.2 / GPT-5.2-Codex*    | 2026-05-01  | 2026-06-01      | 31 days   | Retired
May 7    | GPT-4.1                     | 2026-05-07  | 2026-06-01      | 25 days   | Retired
May 7    | Claude Sonnet 4              | 2026-05-07  | 2026-05-06      | -1 day    | Retired
Jul 2    | Gemini 2.5 Pro / Gemini 3    | 2026-07-02  | 2026-07-31      | 29 days   | Retired
         | Flash

* GPT-5.2-Codex in Copilot Code Review carved out (see docs-github-copilot-gpt52-deprecation.md)

Successor model designations:
  GPT-5.2         → GPT-5.5
  GPT-5.2-Codex   → GPT-5.3-Codex
  GPT-4.1         → GPT-5.5
  Claude Sonnet 4 → Claude Sonnet 4.6
  Gemini 2.5 Pro  → Gemini 3.1 Pro
  Gemini 3 Flash  → Gemini 3.5 Flash

Note: the "Retired" tag is identical across all four notices regardless of lead time
(31, 25, -1, and 29 days) — it is a post-type category, not a timing signal.
```

*Derived from this source, `docs-github-copilot-gpt52-deprecation.md`,
`docs-github-copilot-gpt41-deprecation.md`, and `docs-github-copilot-claude-sonnet4-deprecation.md`*

### Enterprise Migration Checklist for the July 31, 2026 Gemini Cutover

```
Before July 31, 2026 — Enterprise Copilot Administrators:

[ ] Audit workflows, scripts, and integrations referencing "gemini-2.5-pro" or
    "gemini-3-flash" as model identifiers.
[ ] Enable Gemini 3.1 Pro in Copilot model policy settings (replacement for
    Gemini 2.5 Pro):
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
[ ] Enable Gemini 3.5 Flash in Copilot model policy settings (replacement for
    Gemini 3 Flash) — note this was already available for opt-in as of the
    June 2, 2026 Gemini CLI/cloud-agent/app/SDK rollout
    (docs-github-copilot-gemini-cli-cloud-agent-app.md).
[ ] Verify availability by checking individual Copilot settings and confirming
    the policy is enabled for each specific model.
[ ] Confirm the models appear in the Copilot Chat model selector in VS Code and
    on github.com.
[ ] Update integration configurations to reference the new model identifiers.

Post-July 31:
  - Gemini 2.5 Pro and Gemini 3 Flash disappear automatically.
  - "No action is required to remove the older models once they have been deprecated."

Support: "GitHub Enterprise customers with questions or concerns are encouraged
          to reach out to their account manager for further assistance."
```

*Source: Required actions section of GitHub Copilot changelog, July 2, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 4,
  `docs-github-copilot-gpt41-deprecation.md` Claim 2, and
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 6 (identical affected-surface
  boilerplate — "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask
  and agent modes, and code completions)"): this notice repeats the exact phrase verbatim,
  confirming it as fixed boilerplate across every provider's deprecation notice, not
  model- or provider-specific wording.

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 5,
  `docs-github-copilot-gpt41-deprecation.md` Claim 3, and
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claims 3–4 (enterprise admin
  enable-then-verify procedure) and Claim 5 / `docs-github-copilot-gpt41-deprecation.md`
  Claim 4 (automatic removal, no admin action required): all recur nearly verbatim in this
  notice. Four consecutive notices across three providers (OpenAI, Anthropic, Google) now
  confirm these as GitHub's standardized, cross-provider Copilot deprecation playbook.

- **Extends** `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 8 (notice-length
  variability: 31, 25, -1 days across three prior notices): this source adds a fourth data
  point (29 days), reinforcing that lead time varies per notice with no fixed convention.

- **Extends** `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 1 (Gemini 3.1 Pro
  (Preview) and Gemini 3.5 Flash added to Copilot CLI, cloud agent, app, and SDK on June 2,
  2026): this source shows those same two models, one month later, are the designated
  replacements for a formal deprecation — confirming the "successor already rolled out
  before predecessor's deprecation notice" pattern first seen with GPT-5.5
  (`docs-github-copilot-gpt41-deprecation.md` Cross-References).

- **Extends** `docs-github-copilot-web-model-consolidation.md` Claim 1 (Gemini models'
  presence in Copilot web chat only became known to the corpus when they were removed): this
  source is a second instance of the same "deprecation reveals prior undocumented
  availability" pattern, this time naming the specific models (Gemini 2.5 Pro, Gemini 3
  Flash) for the first time.

- **Contradicts** `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 2 and its Novel
  section: that note used the changelog's "Retired" category tag as evidence that the
  Claude Sonnet 4 notice was uniquely retroactive, contrasting it with GPT-5.2/GPT-4.1
  notices it described as "labeled as upcoming." Direct inspection of the raw HTML for this
  source and for the GPT-4.1 and GPT-5.2 changelog pages shows all three carry the identical
  "Retired" tag, regardless of whether the notice is advance (this source: 29 days; GPT-4.1:
  25 days; GPT-5.2: 31 days) or retroactive (Claude Sonnet 4: -1 day). **Contradiction issue
  filed: #1595.** See Claim 7 above for full detail. The narrower factual finding in that
  note (Claude Sonnet 4 was genuinely deprecated one day before its notice was published) is
  unaffected, since it rests on the dated table, not the tag.

- **Novel**:
  - **First Gemini/Google-family Copilot model deprecation notice in the corpus.** Prior
    deprecation notices covered only OpenAI (GPT-5.2, GPT-5.2-Codex, GPT-4.1) and Anthropic
    (Claude Sonnet 4) models. This extends the deprecation-playbook pattern to a third
    provider, confirming it is provider-agnostic.
  - **Per-model (not universal) successor mapping.** Unlike the GPT-4.1/GPT-5.2 batch, which
    both routed to a single successor (GPT-5.5), this notice pairs each deprecated model with
    its own same-tier successor (Pro→Pro, Flash→Flash) — a distinct migration-mapping shape
    not previously seen in the corpus's deprecation notes.
  - **"Retired" tag exposed as a non-timing category label** (Claim 7 / contradiction #1595)
    — the first corpus evidence obtained by directly inspecting raw changelog HTML rather
    than relying on a WebFetch summary, and the first correction of a prior note's
    tag-based inference.
  - **Confirmation that Gemini 2.5 Pro and Gemini 3 Flash were part of the Copilot roster**,
    named here for the first time in the corpus (Claim 9).

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: Gemini 2.5 Pro and Gemini 3 Flash should be marked deprecated
  (effective July 31, 2026) in any model roster the guide maintains; Gemini 3.1 Pro and
  Gemini 3.5 Flash are the confirmed same-tier replacements. This is the first documented
  instance of Gemini models in the guide's Copilot roster context at all — if the guide
  currently has no Gemini entries for Copilot, this notice (plus
  `docs-github-copilot-gemini-cli-cloud-agent-app.md`) is the evidence base for adding them.
- **Correction to changelog-reading guidance**: If any prior guide draft advised readers to
  use the "Retired" tag on a GitHub changelog post as a signal that a deprecation is
  retroactive/zero-notice, that guidance is wrong and should be removed or corrected per
  Claim 7 and contradiction #1595 — the tag marks post *type* only. The reliable signal is
  the explicit date(s) stated in the post body/table, not any category label.
- **Design principle reinforcement**: This is the fourth data point (after GPT-5.2, GPT-4.1,
  Claude Sonnet 4) supporting the existing recommendation to avoid hardcoded model
  identifiers in Copilot configurations and prefer auto-routing or admin-policy-managed
  model selection (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02).

### Chapter 05: Team Adoption / Enterprise Governance

- **Cross-provider deprecation cadence as a recurring governance task**: Four deprecation
  notices across OpenAI, Anthropic, and now Google within roughly three months (May–July
  2026) reinforce that Copilot model-lifecycle monitoring is an ongoing, cross-provider
  governance responsibility, not a one-time or single-vendor concern
  (`docs-github-copilot-claude-sonnet4-deprecation.md` Guide Impact §Ch05). Recommend
  governance checklists explicitly track all three providers' Copilot changelog entries, not
  just the vendor(s) currently in active use.
- **Do not use the "Retired" tag as a triage signal**: Enterprise governance processes that
  might otherwise scan GitHub's changelog feed and prioritize action based on a "Retired"
  category tag should instead parse the explicit dates in each post — the tag alone does not
  distinguish urgent (retroactive/imminent) from routine (weeks-out) deprecations.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 130 words of primary
   text. All extractable facts are captured in the nine claims above.
2. **Raw HTML fetched directly, not via WebFetch summary alone**: WebFetch was used first
   and returned two independent structured summaries; both were then verified by fetching
   the live page's raw HTML directly (`curl --compressed` against the trailing-slash URL,
   since the bare URL 301-redirects) and extracting the article text and the `Tag
   Tag--type` markup programmatically. All quotes above are taken from that raw-HTML
   extraction, not from the WebFetch summaries, and are character-for-character verbatim
   from the source page as of 2026-07-06.
3. **Contradiction filed and cited**: Claim 7 required filing contradiction issue #1595
   against `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 2's use of the "Retired"
   tag as a retroactive-notice signal. No verdict is asserted in this note; that is for the
   issue's resolver. This note only documents the raw-HTML evidence that surfaced the
   discrepancy.
4. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-gpt52-deprecation.md`, `docs-github-copilot-gpt41-deprecation.md`,
   `docs-github-copilot-claude-sonnet4-deprecation.md`, and
   `docs-github-copilot-gemini-cli-cloud-agent-app.md` were checked against those notes'
   actual claim numbering (re-read in full) before citing; none were guessed.
5. **Chapter numbering**: The Prospector's three triage comments on issue #1578 referenced
   inconsistent chapter numbers/topics for this source (variously Ch01/Ch02/Ch03/Ch04/Ch05
   under different topic labels not all matching the guide's actual structure). This note
   instead cites the guide's real chapter structure as it exists in `guide/` (00 Principles,
   01 Daily Workflows, 02 Harness Engineering, 03 Verification, 04 Context Engineering, 05
   Team Adoption, 06 Security and Threat Model) — the same Ch02/Ch05 mapping used by the
   three prior deprecation notes in this family.
6. **Gemini 3.1 Pro naming discrepancy noted, not resolved**: See Claim 8's assessment — the
   June 2, 2026 rollout note calls it "Gemini 3.1 Pro (Preview)" while this July 2 notice
   drops the "(Preview)" qualifier. Neither source explains the change; flagged for a future
   source note if a GA announcement for Gemini 3.1 Pro turns up.
