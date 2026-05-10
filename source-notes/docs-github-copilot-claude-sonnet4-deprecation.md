---
source_url: https://github.blog/changelog/2026-05-07-claude-sonnet-4-deprecated
source_type: docs
title: "Claude Sonnet 4 deprecated"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#562"
---

# Claude Sonnet 4 Deprecated

> GitHub's May 7, 2026 retroactive deprecation notice — published one day after Claude Sonnet 4 was already removed from all Copilot experiences — with Claude Sonnet 4.6 as the named replacement; unlike the GPT-5.2 and GPT-4.1 notices (25–31 days advance), this notice provided zero advance warning, marking a new and riskier failure mode for enterprise model governance.

## Source Context

- **Type**: docs (GitHub official product changelog, ~150 words, labeled "Retired")
- **Author credibility**: GitHub engineering team. Authoritative for the deprecation date, successor model, affected surfaces, and enterprise admin requirements. Not a source for capability comparisons between Claude Sonnet 4 and Sonnet 4.6, or for cost implications of the migration.
- **Scope**: Deprecation of Claude Sonnet 4 (the base model, distinct from Sonnet 4.5 and 4.6) from all GitHub Copilot experiences, effective May 6, 2026. Covers the replacement model (Claude Sonnet 4.6) and the enterprise admin policy requirement. Does NOT cover: capability differences between Sonnet 4 and Sonnet 4.6, whether any Copilot surfaces have carve-outs, cost implications of the migration, or why this deprecation was announced retroactively rather than in advance.

## Extracted Claims

### Claim 1: Claude Sonnet 4 (the base model) is deprecated across all GitHub Copilot experiences effective May 6, 2026, with Claude Sonnet 4.6 as the suggested replacement

- **Evidence**: Official GitHub Copilot changelog, May 7, 2026. Deprecation date and successor model stated in a structured table.
- **Confidence**: settled (authoritative product fact — date and successor stated directly)
- **Quote**: "We have deprecated the following model across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on May 6, 2026."
- **Our assessment**: Claude Sonnet 4 (without a version suffix — i.e., the base generation) is the deprecated model, not Sonnet 4.5 or 4.6. The designated successor is Claude Sonnet 4.6, pointing practitioners toward the most recent Claude Sonnet generation. For Ch02: update any model selection guidance that referenced "Claude Sonnet 4" (bare name) to use "Claude Sonnet 4.6" explicitly. Note that "Claude Sonnet 4" as a bare identifier was already absent from the April 14 model selection roster (`docs-github-copilot-agent-model-selection.md` Claim 2, which listed only 4.5 and 4.6 variants), so this deprecation formalizes what was already implied by the roster.

### Claim 2: The deprecation notice was published on May 7, 2026 — one day AFTER the effective deprecation date of May 6, 2026 — providing zero advance notice

- **Evidence**: The changelog page is labeled "Retired" and dated May 7, 2026. The deprecation table states "2026-05-06" as the deprecation date. The word "Retired" distinguishes this post from GPT-5.2 and GPT-4.1 notices, which were labeled as upcoming and provided 31 and 25 days advance notice respectively.
- **Confidence**: settled (both dates stated directly in the official source)
- **Quote**: "Retired" (label on the changelog post); "Claude Sonnet 4 | 2026-05-06 | Claude Sonnet 4.6" (from the deprecation table)
- **Our assessment**: This is the most consequential finding in the source. Unlike the GPT-5.2 notice (31 days advance: May 1 → June 1) and the GPT-4.1 notice (25 days advance: May 7 → June 1), the Claude Sonnet 4 notice was published retroactively. When this changelog was posted on May 7, Claude Sonnet 4 had already been gone for one day. Enterprise teams monitoring the changelog as a governance trigger had zero time to act — the window had already closed. This breaks the advance-notice pattern the guide documented from the GPT deprecation series and represents a qualitatively new governance risk.

### Claim 3: Enterprise administrators may need to proactively enable Claude Sonnet 4.6 in model policies — no automatic migration of admin policies occurs

- **Evidence**: Changelog: "Copilot Enterprise administrators may need to enable access to alternative models through their model policies in Copilot settings."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Copilot Enterprise administrators may need to enable access to alternative models through their model policies in Copilot settings."
- **Our assessment**: The same governance failure mode as GPT-5.2 (`docs-github-copilot-gpt52-deprecation.md` Claim 5) and GPT-4.1 (`docs-github-copilot-gpt41-deprecation.md` Claim 3): admin policies are not automatically updated when models are deprecated. However, the retroactive announcement compounds this risk severely: enterprise teams had zero advance time to enable the replacement before the model disappeared. Any team that had not already enabled Claude Sonnet 4.6 in their model policies found the old model gone and the replacement potentially not yet enabled — with no warning window. For Ch05: the retroactive notice is a concrete escalation of the governance risk pattern that the guide should address explicitly.

### Claim 4: Administrators can verify replacement model availability through individual Copilot settings and the model selector in VS Code and github.com

- **Evidence**: Changelog: "As an administrator, you can verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model. Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com."
- **Our assessment**: This verification step is identical to what was documented in `docs-github-copilot-gpt52-deprecation.md` Claim 5 and `docs-github-copilot-gpt41-deprecation.md` Claim 3. The two-step pattern (enable in policy settings → verify in model selector) is now confirmed as GitHub's standard post-deprecation verification procedure. For harness engineering: after enabling a replacement model in admin policy, the validation step is a functional check in the model selector — not just a settings-page confirmation.

### Claim 5: After deprecation, the model disappears automatically — no admin action is required for removal

- **Evidence**: Changelog: "No action is required to remove the deprecated models."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "No action is required to remove the deprecated models."
- **Our assessment**: Identical language to `docs-github-copilot-gpt41-deprecation.md` Claim 4 and consistent with `docs-github-copilot-gpt52-deprecation.md` Claim 6. Auto-removal is a consistent pattern across all three deprecation notices in the corpus. The passive failure mode (do nothing, discover the model is gone) is now confirmed as applying to Claude model deprecations as well as GPT model deprecations.

### Claim 6: The deprecation has no stated carve-outs — all affected Copilot surfaces are covered unconditionally

- **Evidence**: Changelog states the model is deprecated across "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)" with no noted exceptions.
- **Confidence**: settled (absence of carve-out language in official changelog)
- **Quote**: "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)"
- **Our assessment**: Unlike the GPT-5.2 deprecation, which carried an explicit carve-out for GPT-5.2-Codex in Copilot Code Review (`docs-github-copilot-gpt52-deprecation.md` Claim 3), this notice contains no exceptions. The Claude Sonnet 4 deprecation is unconditional across all surfaces — consistent with the GPT-4.1 notice (also no carve-outs) and in contrast to the GPT-5.2 notice. The absence of a carve-out simplifies the practitioner's action: there are no surface-specific edge cases to track.

### Claim 7: Claude Sonnet 4 (base) was already absent from the active model roster as of April 14, 2026 — the formal deprecation ratifies a de facto removal that preceded the announcement by at least three weeks

- **Evidence**: `docs-github-copilot-agent-model-selection.md` (issue #171, April 14, 2026) listed the available Claude models as Sonnet 4.5, Sonnet 4.6, Opus 4.5, and Opus 4.6 — no "Claude Sonnet 4" (base) entry. The Copilot CLI auto model pool (`docs-github-copilot-cli-auto-model-selection.md`, April 17, 2026) similarly listed Sonnet 4.6 and Haiku 4.5, not Sonnet 4.
- **Confidence**: emerging (the absence from the roster is factual; the inference that de facto removal preceded the formal notice is analytical)
- **Quote**: (no direct quote; inferred from cross-referencing dated roster sources)
- **Our assessment**: The absence of "Claude Sonnet 4" (base) from the April 14 model roster and the April 17 auto pool means the formal deprecation notice on May 7 announced a removal that had already been functionally complete. Practitioners following the model roster as their authoritative source for available models would not have been actively using "Claude Sonnet 4" (base) for new configurations since at least April 14. The zero-notice retroactive announcement had lower operational impact than it appears, because the model had already been out of the active roster for weeks.

### Claim 8: Three Copilot model deprecation notices across two AI providers were published within a 7-day window (May 1–7, 2026), with cutoff dates spanning two days (May 6 and June 1)

- **Evidence**: GPT-5.2 + GPT-5.2-Codex deprecated (notice May 1, cutoff June 1); GPT-4.1 deprecated (notice May 7, cutoff June 1); Claude Sonnet 4 deprecated (notice May 7, effective May 6 — already done). Derived from cross-referencing three dated official changelogs.
- **Confidence**: settled (all dates stated in official changelogs; the 7-day window is derived, not directly stated)
- **Quote**: (no direct quote; comparison across three dated sources)
- **Our assessment**: The density of deprecation notices in early May 2026 confirms that GitHub's Copilot model roster is turning over rapidly and non-uniformly: some deprecations carry advance notice windows, others do not; some are coordinated batch events targeting the same date, others are immediate; some affect only GPT models, others affect Claude. For Ch05: the unpredictability of notice cadence (31 days, 25 days, and zero days all within the same week) is the central governance signal. Teams cannot rely on a "we'll get notified and have time to act" assumption for Copilot model governance. Proactive posture — always maintaining policy coverage of the successor model before the deprecated model is retired — is the only safe strategy.

## Concrete Artifacts

### Deprecation Table (from changelog, May 7, 2026 — effective May 6, 2026)

```
GitHub Copilot Model Deprecation — Effective May 6, 2026

| Model            | Deprecation Date | Suggested Alternative |
|------------------|------------------|-----------------------|
| Claude Sonnet 4  | 2026-05-06       | Claude Sonnet 4.6     |

Notice type: RETROACTIVE ("Retired" — announced after deprecation already effective)
No exceptions or carve-outs stated.
Affected surfaces: all GitHub Copilot experiences (Copilot Chat, inline edits,
                   ask and agent modes, code completions).
```

*Source: GitHub Copilot official changelog, May 7, 2026*

### Deprecation Notice Timeline Across Corpus (May 2026)

```
GitHub Copilot Model Deprecations — May 2026

Notice  | Model(s)                   | Notice Date | Effective Date | Lead Time
--------|----------------------------|-------------|----------------|----------
May 1   | GPT-5.2                    | 2026-05-01  | 2026-06-01     | 31 days
        | GPT-5.2-Codex (most sfc)  | 2026-05-01  | 2026-06-01     | 31 days
        | GPT-5.2-Codex (Code Review)| CARVE-OUT  | TBD            | N/A
May 7   | GPT-4.1                    | 2026-05-07  | 2026-06-01     | 25 days
May 7   | Claude Sonnet 4            | 2026-05-07  | 2026-05-06     | -1 day (retroactive)

Successor model designations:
  GPT-5.2        → GPT-5.5
  GPT-5.2-Codex  → GPT-5.3-Codex
  GPT-4.1        → GPT-5.5
  Claude Sonnet 4 → Claude Sonnet 4.6
```

*Derived from this source, `docs-github-copilot-gpt52-deprecation.md`, and `docs-github-copilot-gpt41-deprecation.md`*

### Enterprise Migration Checklist (derived from changelog required-actions section)

```
After May 6, 2026 — Enterprise Copilot Administrators
(Note: cutover already occurred — model already deprecated):

[ ] Audit workflows, scripts, and integrations that reference "Claude Sonnet 4"
    as a model identifier (bare name, not suffixed with 4.5 or 4.6)
[ ] Enable Claude Sonnet 4.6 in Copilot model policy settings:
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
[ ] Verify Claude Sonnet 4.6 availability in model selector:
    Check individual Copilot settings → confirm policy is enabled →
    verify model appears in Copilot Chat model selector in VS Code and github.com
[ ] Update integration configurations to reference "claude-sonnet-4-6"

Post-May 6:
  - Claude Sonnet 4 has already been automatically removed.
  - "No action is required to remove the deprecated models."

Support: "GitHub Enterprise customers with questions or concerns are encouraged
          to reach out to their account manager for further assistance."
```

*Source: Required actions section of GitHub Copilot changelog, May 7, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claims 4, 5, and 6 (affected surface list, enterprise admin pre-migration requirement, auto-removal behavior): all three patterns recur verbatim in this Claude Sonnet 4 notice, confirming they are settled patterns in GitHub's model deprecation playbook that apply across providers, not just to GPT models.

- **Corroborates** `docs-github-copilot-gpt41-deprecation.md` Claim 4 ("No action is required to remove the models once they have been deprecated") and Claims 3 (enterprise admin policy enablement requirement): the language is nearly identical across all three notices, confirming standardized deprecation procedure language.

- **Extends** `docs-github-copilot-gpt41-deprecation.md` Claim 5 (model lifecycle cadence) and Claim 6 (coordinated batch retirement): that note identified a compressed notice window (25 days for GPT-4.1 vs. 31 days for GPT-5.2) and a coordinated June 1 batch cutoff. This source adds a third data point — a retroactive notice with zero advance warning — showing the notice-window variability extends beyond compression to full elimination. The pattern is now: advance notices can be zero or negative, and multiple providers can be affected simultaneously.

- **Extends** `docs-github-copilot-agent-model-selection.md` Extraction Notes (point 5): that note warned "model lists for cloud AI services change frequently." The Claude Sonnet 4 retroactive deprecation is the most extreme illustration of that warning — the model was removed before the notice was published.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3 (auto pool as of April 17 contained Sonnet 4.6 and Haiku 4.5, not Sonnet 4): the auto pool had already excluded Claude Sonnet 4 (base) before either the April 14 roster or this deprecation notice. Auto-routing was ahead of the formal deprecation by weeks, consistent with the pattern observed for GPT-5.2 in `docs-github-copilot-gpt41-deprecation.md` Cross-References.

- **Contradicts**: None. The retroactive notice pattern is not contradicted by existing corpus claims — prior notes documented GPT deprecations with advance windows but did not claim all future deprecations would follow that pattern. The existing notes even warned that model lists change frequently. No contradiction issue required.

- **Novel**:
  - First in-corpus documentation of a **retroactive** Copilot model deprecation notice — announced after the model was already removed, providing zero advance warning. Prior corpus deprecation notes (GPT-5.2, GPT-4.1) both provided advance notice windows.
  - First Claude-family (Anthropic) model deprecation notice in the corpus; prior deprecation notes covered only GPT-family (OpenAI) models.
  - First evidence that GitHub's advance-notice convention is not universal: the same changelog that published a 25-day GPT-4.1 notice (on May 7) simultaneously published a -1-day Claude Sonnet 4 notice (also on May 7). Notice length is model-specific, not a platform-wide policy.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: Claude Sonnet 4 (bare name, no version suffix) should be marked as deprecated as of May 6, 2026. Claude Sonnet 4.6 is the confirmed current-generation replacement. The model roster from `docs-github-copilot-agent-model-selection.md` did not list "Claude Sonnet 4" (base) as of April 14 — the entry was already absent, so the guide's roster table is likely already correct. Verify that no existing roster entry references the bare "Sonnet 4" identifier and update any that do to "Sonnet 4.6."
- **Retroactive deprecation as a design signal**: The zero-advance-notice deprecation of Claude Sonnet 4 is concrete evidence that hardcoding bare model identifiers in configurations can result in immediate, unannounced failure rather than the 25–31 day migration window practitioners have seen from GPT deprecations. Strengthen the existing recommendation (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02) to prefer auto-routing or admin-policy-managed model selection: configurations that reference bare model names can break without warning.

### Chapter 05: Team Adoption / Enterprise Governance

- **Retroactive notice as a new governance risk tier**: The guide should explicitly distinguish two failure modes in Copilot model governance: (a) advance-notice deprecations, where teams have 25–31 days to act; and (b) retroactive deprecations, where the model is already gone when the notice is published. Governance processes designed only for (a) — monitoring changelogs and scheduling migrations — will not protect against (b). For retroactive deprecations, the only effective mitigation is maintaining proactive policy coverage: always enable the successor model in admin policy before the predecessor is retired, based on the model roadmap, not the deprecation notice.
- **Cross-provider deprecation simultaneity**: The May 7, 2026 date carried both a 25-day advance notice for GPT-4.1 (June 1 cutoff) and a retroactive notice for Claude Sonnet 4 (already gone). Enterprise teams monitoring the changelog must now process notices from multiple AI providers simultaneously and recognize that notice characteristics (advance vs. retroactive, with vs. without carve-outs) differ by model, not by provider or date. Recommend governance processes explicitly categorize notice type on intake rather than assuming a uniform lead time.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 150 words. All extractable facts are captured in the eight claims above. The source provides no explanation of why Claude Sonnet 4 was deprecated retroactively rather than in advance, no capability comparison between Sonnet 4 and Sonnet 4.6, and no information on what occurs to in-flight Copilot sessions that were using Sonnet 4 at the moment of deprecation.
2. **WebFetch returned structured content closely matching source**: The page content was returned in detail. Direct quotes in the claims above match the fetched page text; the Assayer should spot-check key quotes against the live source URL.
3. **"Claude Sonnet 4" identity**: The deprecated model is identified only as "Claude Sonnet 4" with no version suffix. This is distinct from "Claude Sonnet 4.5" and "Claude Sonnet 4.6," both of which remain active. The guide should not conflate these identifiers.
4. **Already-absent from active roster**: Cross-referencing `docs-github-copilot-agent-model-selection.md` confirms that "Claude Sonnet 4" (base) was not in the April 14, 2026 active model roster. The deprecation formally ratifies a model that had already been phased out from the selectable lineup weeks earlier.
5. **No contradictions filed**: No existing corpus claim asserts that all Copilot deprecations will carry advance notice, or that Claude models are exempt from Copilot deprecation. The retroactive pattern is novel but does not contradict any existing claim. No contradiction issue required.
