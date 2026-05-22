---
source_url: https://github.blog/changelog/2026-05-20-updates-to-available-models-in-copilot-on-web
source_type: docs
title: "Updates to available models in Copilot on web"
author: GitHub (official changelog)
date_published: 2026-05-20
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: settled
issue: "#845"
---

# Updates to Available Models in Copilot on Web

> GitHub's May 20, 2026 changelog announcing a deliberate contraction of the web Copilot
> model roster — all Gemini models and select OpenAI variants (GPT-5.2-Codex, GPT-5.4 nano)
> removed from Copilot Chat on the web, with OpenAI and Claude models retained — framed as
> a consistency and reliability strategy rather than a deprecation, establishing that the web
> chat surface is now actively managed toward a narrower recommended set.

## Source Context

- **Type**: docs (GitHub official product changelog, May 20, 2026; approximately 150 words
  of primary announcement text)
- **Author credibility**: GitHub engineering team announcing a production product change.
  Authoritative for the existence of the removals, which models were removed, which remain,
  and the stated rationale. Not a credible source for: which specific Claude or OpenAI models
  remain in the web picker, the full current model list, whether the web roster will expand
  again in the future, plan-tier differences in what remains available, or comparative
  quality evidence for the "more consistent responses" claim.
- **Scope**: Model roster changes specific to Copilot Chat on the web (github.com). Covers:
  which models were removed (all Gemini models; GPT-5.2-Codex; GPT-5.4 nano), which model
  families remain (OpenAI and Claude across price points), the stated rationale (reliable,
  consistent responses), and the forward strategy (more limited new model rollouts). Does
  NOT cover: the full current model list post-removal, plan-tier availability differences
  within the remaining roster, whether the removed models remain available in the CLI or
  cloud agent surfaces, cost implications for practitioners, or any evidence base for the
  "more consistent response quality" benefit claim.

## Extracted Claims

### Claim 1: All Gemini models have been removed from Copilot Chat on the web

- **Evidence**: Official GitHub product changelog stating the removal as a completed action.
  The phrasing "have been removed" indicates this is an already-implemented change, not
  a scheduled future removal.
- **Confidence**: settled (product fact — removal stated in official changelog as complete)
- **Quote**: "All Gemini models and several other models (e.g., GPT-5.2 Codex and GPT-5.4
  nano) have been removed from Copilot Chat on the web."
- **Our assessment**: This is the most novel claim in the source. No prior corpus source
  documented Gemini models being available in Copilot web chat — so their removal reveals
  retroactively that Google Gemini was part of the Copilot web model roster. The removal
  signals that GitHub's web chat is now exclusively OpenAI and Anthropic territory for AI
  providers. For Ch02: practitioners who depended on Gemini models in web Copilot chat must
  switch to OpenAI or Claude models; there is no Gemini substitute in the web interface.
  The broader implication is that the web surface's multi-provider strategy is being rolled
  back — the web picker is contracting toward a curated OpenAI/Anthropic set.

### Claim 2: GPT-5.2-Codex and GPT-5.4 nano have been removed from Copilot Chat on the web

- **Evidence**: Both model names are cited as examples of "several other models" removed
  alongside all Gemini models. The removal is presented as already complete.
- **Confidence**: settled (model names stated in official changelog as removed)
- **Quote**: "All Gemini models and several other models (e.g., GPT-5.2 Codex and GPT-5.4
  nano) have been removed from Copilot Chat on the web."
- **Our assessment**: GPT-5.2-Codex removal from web chat is consistent with (and may be
  an early implementation of) GitHub's broader May 1 deprecation notice
  (`docs-github-copilot-gpt52-deprecation.md` Claim 2), which scheduled GPT-5.2-Codex
  deprecation across all Copilot surfaces by June 1, 2026. The web chat removal may have
  been the first surface-specific implementation of that deprecation, 11 days before the
  June 1 cutoff. GPT-5.4 nano is a distinct finding: no prior corpus source documented
  GPT-5.4 nano as a Copilot web model — its removal reveals retroactively that a nano
  (likely lower-cost, lower-capability) variant of GPT-5.4 was available in web chat.
  For Ch02: GPT-5.2-Codex users on web chat should already have migrated to GPT-5.3-Codex
  per the deprecation notice. GPT-5.4 nano had no prior corpus documentation, so the
  removal affects practitioners who may have been using it without the guide covering it.

### Claim 3: OpenAI and Claude models remain available in Copilot on web across Copilot plans

- **Evidence**: Changelog explicitly confirms continued availability for both OpenAI and
  Claude model families, framing it as "still available across Copilot plans" after the
  removals.
- **Confidence**: settled (continued availability stated in official changelog)
- **Quote**: "OpenAI and Claude models across price points are still available across
  Copilot plans."
- **Our assessment**: The "across price points" phrasing implies that multiple tiers within
  both OpenAI and Claude families remain (i.e., not just a single model per provider). The
  "across Copilot plans" phrasing implies these are available to all plan tiers, not just
  Business/Enterprise. However, the changelog does not enumerate which specific OpenAI and
  Claude models remain — practitioners cannot determine from this source alone which exact
  models are currently in the web picker. For Ch02: the web picker is now a two-provider
  roster (OpenAI and Anthropic), with Gemini entirely absent. Teams that relied on a
  three-provider model comparison workflow in web chat must revise that workflow.

### Claim 4: GitHub's stated rationale for the reduction is ensuring consistent, reliable responses by limiting the model list

- **Evidence**: Changelog provides an explicit rationale statement that directly names model
  list limitation as the reliability mechanism.
- **Confidence**: settled (rationale stated in official changelog; the causal link between
  "fewer models" and "more reliable responses" is GitHub's claim, not independently verified)
- **Quote**: "While model choice is valuable, we are limiting the list of available models
  on github.com so that we can consistently ensure reliable responses."
- **Our assessment**: This is a notable strategic admission — GitHub is explicitly
  acknowledging that broader model choice trades off against response reliability on the
  web surface. The rationale implies that managing a large multi-provider model roster
  creates operational challenges (likely: inconsistent quality assurance across providers,
  different response characteristics, harder to ensure consistent UX). The "while model
  choice is valuable" clause concedes the user value of breadth before explaining the
  constraint. For Ch03 (model selection): practitioners should understand that web Copilot
  is now a curated experience, not a comprehensive model comparison tool. If they want
  access to Gemini models alongside Claude and OpenAI, they must use alternative tooling
  rather than GitHub Copilot web chat.

### Claim 5: The change is framed as producing a "simplified experience focused on recommended models" and "more consistent response quality"

- **Evidence**: Changelog cites two user-facing benefits: simplified experience and more
  consistent response quality. These are presented as the positive outcomes of the
  roster reduction.
- **Confidence**: settled (benefits stated in official changelog); the underlying quality
  claim is vendor assertion without supporting evidence
- **Quote**: "Simplified experience focused on our recommended models" and "More consistent
  response quality across all interactions"
- **Our assessment**: Both are marketing framings. "Simplified experience" acknowledges
  that fewer choices reduce cognitive load for practitioners who were uncertain which of
  many models to select. "More consistent response quality" is an assertion without data —
  the changelog provides no evidence that the removed models produced worse or more
  variable responses. For the guide: these benefit claims should be presented as vendor
  rationale, not as empirically verified outcomes. Whether practitioners actually experience
  more consistent quality after the removal is unknowable from this source.

### Claim 6: GitHub's forward strategy for the web surface is a more limited set of new model rollouts

- **Evidence**: Changelog explicitly states the future direction for the web surface model
  management approach.
- **Confidence**: settled (stated in official changelog as a forward-looking platform
  commitment)
- **Quote**: "a more limited set of new model rollouts as we work to ensure optimal
  performance"
- **Our assessment**: This is the most strategically significant claim for practitioners
  planning their web Copilot workflows. GitHub is committing to a consolidation strategy
  going forward — future model releases will not automatically appear in the web picker.
  The "as we work to ensure optimal performance" qualifier suggests the constraint is
  operational (not enough QA bandwidth to support all new models) rather than a permanent
  two-provider philosophy. For Ch01 (Daily Workflows): practitioners who rely on accessing
  the latest models via Copilot web chat should expect that the web picker will lag behind
  model availability in other surfaces (CLI, VS Code) going forward. The web surface is
  optimizing for reliability, not for frontier access.

### Claim 7: The web surface model roster is now managed distinctly from the CLI auto pool and cloud agent model selection

- **Evidence**: Derived from comparing this source with `docs-github-copilot-cli-auto-model-selection.md`
  (Claim 3, April 17 pool: GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, Haiku 4.5) and
  `docs-github-copilot-agent-model-selection.md` (Claim 2, April 14 roster including Opus tiers).
  The web removal of Gemini models, GPT-5.4 nano, and GPT-5.2-Codex does not imply those
  models were removed from the CLI or agent surfaces.
- **Confidence**: emerging (the surface-specific management is inferred from comparing
  announcements; no single source explicitly states that surfaces have independent model
  policies)
- **Quote**: (no direct quote; see Our assessment)
- **Our assessment**: The corpus now shows three distinct GitHub Copilot model surfaces
  with independently managed model rosters: (1) web chat (narrowed by this source to
  OpenAI + Claude only), (2) CLI auto pool (GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, Haiku 4.5
  as of April 17), and (3) cloud agent model selection (Sonnet/Opus 4.5/4.6 and Codex
  variants as of April 14). The fact that Gemini was in web chat but never in CLI or agent
  surfaces confirms surface-specific policies. Practitioners should not assume that model
  availability in one surface implies availability in another. For Ch02: document the
  web-vs-CLI-vs-agent roster divergence as a practical knowledge requirement for
  multi-surface Copilot users.

## Concrete Artifacts

### Web Copilot Model Roster Change (May 20, 2026)

```
GitHub Copilot Chat on Web — Model Roster Change (May 20, 2026)

REMOVED:
  All Gemini models             (Google)    — all variants removed
  GPT-5.2-Codex                (OpenAI)    — removed (earlier than June 1 broad deprecation)
  GPT-5.4 nano                 (OpenAI)    — removed (not previously documented in corpus)

RETAINED:
  OpenAI models "across price points"      — specific models not enumerated
  Claude models "across price points"      — specific models not enumerated

RATIONALE (official statement):
  "While model choice is valuable, we are limiting the list of available models
  on github.com so that we can consistently ensure reliable responses."

FORWARD STRATEGY:
  "a more limited set of new model rollouts as we work to ensure optimal performance"

Effective date: May 20, 2026 (presented as already implemented at announcement)
```

*Source: GitHub Copilot official changelog, May 20, 2026*

### Cross-Surface Model Availability Comparison (as of May 20, 2026)

```
Model                  Web Chat   CLI Auto Pool   Cloud Agents
──────────────────────────────────────────────────────────────
Gemini models          REMOVED    never listed    never listed
GPT-5.4 nano           REMOVED    never listed    never listed
GPT-5.2-Codex          REMOVED    never listed    listed Apr 14*
GPT-5.4                unknown    ✓               unknown
GPT-5.3-Codex          unknown    ✓               listed Apr 14
Claude Sonnet 4.6      ✓ (retained) ✓             ✓
Claude Opus 4.6        ✓ (retained) NOT in pool   ✓
Claude Haiku 4.5       ✓ (retained) ✓             not listed
Claude Sonnet/Opus 4.5 ✓ (retained) NOT in pool   ✓

* GPT-5.2-Codex was in cloud agent selection as of Apr 14, 2026 but is subject to
  broader June 1 deprecation per docs-github-copilot-gpt52-deprecation.md.

Caveats:
  - Web Chat: "Retained" means the model family is retained; specific model names
    within each family are not listed in this source.
  - CLI Auto Pool: data from April 17, 2026 announcement.
  - Cloud Agents: data from April 14, 2026 announcement; subject to June 1 deprecations.
  - "unknown" = not documented in the corpus for that surface.
```

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 2 ("GPT-5.2-Codex
  is deprecated across Copilot experiences effective June 1, 2026, with GPT-5.3-Codex as
  the suggested replacement"): The May 20 web chat removal of GPT-5.2-Codex is an early
  surface-specific implementation of the broader June 1 deprecation that source documented.
  The June 1 cutoff applies globally; the web chat removal occurred 11 days earlier. This
  corroborates the trend in that note's Extraction Notes (point 1): the deprecation is
  rolling out surface by surface. Practitioners who read the June 1 deprecation notice as
  the universal cutoff should be aware the web removal already occurred.

- **Extends** `docs-github-copilot-web-contextual-chat.md` (issue #817): That May 18
  changelog redesigned the web Copilot UX (in-page contextual panel, automatic context
  attachment). Two days later, this source narrows the model roster available in that
  same redesigned interface. Together the two announcements characterize the web Copilot
  trajectory in May 2026: UX improvement (panel model, zero-effort context) + model
  simplification (Gemini removed, narrower roster). The web surface is being refined
  toward reliability and consistency, not toward frontier model breadth.

- **Complements** `docs-github-copilot-vscode-auto-model-selection.md` (issue #844):
  Published the same day (May 20, 2026). While the web source contracts the model roster
  for consistency, the VS Code source expands routing sophistication with task-aware model
  selection. The two same-day announcements reveal a surface differentiation strategy:
  web Copilot → curated, consistent, reliability-optimized; VS Code Copilot → sophisticated,
  task-aware, capability-optimized within a cost-bounded pool. For Ch02: practitioners
  choosing between web and VS Code for Copilot interaction should understand these distinct
  design philosophies. Web is simpler and more predictable; VS Code is more capable and
  adaptive.

- **Extends** `docs-github-copilot-agent-model-selection.md` Extraction Notes (point 5):
  That source warned "model lists for cloud AI services change frequently (new versions
  added, older versions deprecated). Check the changelog for updates before citing
  specific version names." This source is a direct instance of exactly that — not a
  deprecation but a surface-specific contraction removing models from the web chat
  interface. The warning to check the changelog before citing specific version names
  applies with equal force to surface availability (which surface a model appears on)
  as it does to model version currency.

- **Extends** `docs-github-copilot-student-gpt53codex-picker-removal.md` Claim 1
  ("first source in corpus documenting a model being removed from the manual picker on
  a specific plan tier"): That note documented a plan-tier-specific picker removal
  (Student plan, GPT-5.3-Codex). This source documents a surface-specific roster
  reduction (web chat surface, all Gemini models + two OpenAI variants) affecting all
  plans. The two notes together reveal that GitHub is managing model access on at least
  two independent axes: plan-tier restriction (Student picker) and surface-level
  restriction (web chat roster). A model can be available on a given surface for some
  plan tiers but not others, and available via one surface but not another.

- **Contradicts**: None identified. The removal of GPT-5.2-Codex from web chat is
  consistent with the broader deprecation. The removal of Gemini models is not
  contradicted by any prior corpus source (no prior source documented Gemini availability
  in web chat). The retention of OpenAI and Claude models is consistent with their
  documented presence in CLI and agent surfaces. No contradiction issue filed.

- **Novel**:
  - **Gemini model availability in Copilot web (revealed by removal)**: No prior corpus
    source documented Google Gemini models as part of the GitHub Copilot model roster
    on any surface. Their removal reveals retroactively that Gemini was part of the web
    picker — the first corpus evidence that Copilot web offered a Google model family
    alongside OpenAI and Anthropic. No existing notes need to be updated for this (the
    models are already removed), but future references to the Copilot web roster as
    "two-provider" (OpenAI + Anthropic) are now accurate.
  - **GPT-5.4 nano in Copilot web (revealed by removal)**: No prior corpus source
    documented GPT-5.4 nano as a distinct model variant in any Copilot surface. Its
    removal is the only evidence it existed in web chat.
  - **Consolidation as a strategy vs. deprecation**: All prior corpus sources about model
    removals framed them as deprecations (model lifecycle events) or plan-tier restrictions.
    This source is the first to frame removal as a proactive consolidation strategy —
    "limiting the list" for operational reliability rather than retiring an outdated model.
    This is a distinct rationale that changes how practitioners should interpret future web
    model roster changes.
  - **Web-specific model policy as a distinct governance layer**: This is the first corpus
    source to make evident that the web chat surface has an independent model roster policy
    from CLI and cloud agent surfaces. Prior sources each documented their surface's model
    set without establishing cross-surface comparison. This source, read alongside existing
    CLI and agent notes, reveals the web surface as an independently managed layer.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a note for practitioners using web Copilot chat:
  the model roster is now narrowed to OpenAI and Claude families only, with Gemini removed
  and a forward commitment to limit new model rollouts. Practitioners who want access to
  Gemini models or the latest frontier models must use CLI or VS Code Copilot, not the
  web interface. The web surface is optimized for reliable responses over broad model
  variety.

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Document the surface-specific
  model roster as a practical knowledge requirement for multi-surface Copilot users. Copilot
  web chat, CLI auto mode, and cloud agent model selection each have independent model
  availability governed by different policies. Teams building workflows that span multiple
  GitHub Copilot surfaces must verify model availability per surface, not assume cross-surface
  consistency. Update any model roster tables to reflect that Gemini is not available in
  web chat. Mark GPT-5.4 nano as removed from web chat (it may not have been previously
  documented). Note that OpenAI and Claude models remain available on web, but the specific
  current list must be verified at github.com/copilot.

- **Chapter 03 (Model Selection and Capabilities)**: Add the web surface as a case study
  in vendor-curated model selection: GitHub explicitly chose to reduce the web picker to
  improve consistency, trading model variety for operational reliability. This is a useful
  data point for practitioners thinking about which model selection surfaces to use for
  their workflows. If "access to many models" is the goal, VS Code or CLI is the better
  surface; if "reliable, consistent responses from recommended models" is the goal, web
  is now explicitly designed for that.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Note the forward consolidation
  strategy for web model rollouts. Teams planning AI tooling roadmaps should not assume
  that new frontier models will appear in the web Copilot picker — GitHub has explicitly
  committed to limiting new web model rollouts for operational reasons. Teams that need
  leading-edge model access should plan their workflows around VS Code or CLI surfaces,
  with web serving as the stable, curated interaction point.

## Extraction Notes

1. **WebFetch returned structured summaries rather than raw HTML**: Two separate WebFetch
   calls to the source URL returned structured markdown summaries consistent with each
   other. Verbatim quotes in Claims 1, 3, 4, and 6 are reproduced as they appeared in
   the WebFetch output, enclosed in quotation marks in the tool's output. Claims 5's quotes
   ("Simplified experience focused on our recommended models" and "More consistent response
   quality across all interactions") appeared in a "Benefits Cited" section of the WebFetch
   summary — these are presented as verbatim but the Assayer should verify them directly
   against the source URL, as the structured format of the WebFetch output creates some
   uncertainty about whether the tool quoted or paraphrased these short phrases.

2. **Source is brief by design**: This is a short changelog entry (~150 words of primary
   content). All seven claims exhaust the substantive content. The source is thin — it
   announces the roster change and rationale without listing the full current model set,
   providing evidence for quality claims, or specifying plan-tier differences within the
   retained roster.

3. **Gemini availability prior to removal is undocumented**: The corpus has no prior source
   documenting which specific Gemini models were in the web picker, at what plan tiers, or
   since when. The removal reveals only that Gemini models were available; no further detail
   is available from this source.

4. **Current web model list not enumerated**: The changelog does not provide a complete list
   of models currently available in the web Copilot picker after the removals. "OpenAI and
   Claude models across price points" is the only descriptor. Practitioners who need the
   current complete list should visit github.com/copilot or GitHub's documentation on
   supported AI models.

5. **No contradictions filed**: The removal of GPT-5.2-Codex from web chat is consistent
   with the broader June 1 deprecation notice. No corpus source claims Gemini availability
   on any other Copilot surface (so there is no surface-consistency claim to contradict).
   No contradiction issue required.
