---
source_url: https://github.blog/changelog/2026-05-07-claude-sonnet-4-deprecated
source_type: docs
title: "Claude Sonnet 4 deprecated"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-08
last_checked: 2026-05-08
status: current
confidence_overall: settled
issue: "#562"
---

# Claude Sonnet 4 Deprecated

> GitHub's May 2026 deprecation notice removing Claude Sonnet 4 (the base, non-versioned model) from all Copilot experiences effective May 6, 2026 — with Claude Sonnet 4.6 as the named replacement, an enterprise admin enablement requirement, and automatic removal of the deprecated model with no cleanup action required from practitioners.

## Source Context

- **Type**: docs (GitHub official product changelog, ~150 words)
- **Author credibility**: GitHub engineering team. Authoritative for the deprecation timeline, successor model designation, and enterprise admin requirements. Not a source for capability comparisons between deprecated and replacement models, cost implications, or migration effort estimation.
- **Scope**: Deprecation of Claude Sonnet 4 (the original, unversioned Sonnet 4 model — distinct from Sonnet 4.5 and Sonnet 4.6) from all GitHub Copilot experiences, effective May 6, 2026. Covers affected surfaces, the replacement model, and the enterprise admin action required. Does NOT cover: capability differences between Claude Sonnet 4 and Sonnet 4.6, whether any UI changes accompany the deprecation, cost implications for practitioners, or the deprecation timeline for other Claude model generations (Sonnet 4.5, Opus variants).

## Extracted Claims

### Claim 1: Claude Sonnet 4 is deprecated across all GitHub Copilot experiences effective May 6, 2026, with Claude Sonnet 4.6 as the suggested replacement

- **Evidence**: Official GitHub Copilot changelog. Deprecation date and successor model stated in the announcement.
- **Confidence**: settled (authoritative product fact — date and successor stated directly)
- **Quote**: "We have deprecated the following model across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on May 6, 2026."
- **Our assessment**: The deprecated model is Claude Sonnet 4 — the original base model from the Claude 4 generation, not the subsequent 4.5 or 4.6 variants. The replacement is Claude Sonnet 4.6, the current standard tier. This deprecation completes the retirement of the initial Claude 4 baseline from Copilot's active roster. Practitioners who had explicitly pinned "claude-sonnet-4" (the base identifier) must update to "claude-sonnet-4-6". Teams using Sonnet 4.5 or any Opus variant are unaffected.

### Claim 2: The deprecation affects Copilot Chat, inline edits, ask and agent modes, and code completions — the full set of primary Copilot surfaces

- **Evidence**: Official changelog explicitly lists all affected surfaces within the deprecation statement.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "including Copilot Chat, inline edits, ask and agent modes, and code completions"
- **Our assessment**: This surface scope is identical to the GPT-5.2 deprecation (see `docs-github-copilot-gpt52-deprecation.md` Claim 4). GitHub applies deprecations uniformly across all AI interaction surfaces simultaneously rather than phasing by surface — a consistent deprecation pattern across both the OpenAI and Anthropic model families. Any practitioner using GitHub Copilot for any of these surfaces with an explicitly pinned Claude Sonnet 4 identifier needs to update before the deadline.

### Claim 3: Practitioners must update workflows and integrations to use supported models; no action is required to remove deprecated models

- **Evidence**: Required-actions section of the official changelog, stating both the positive obligation (update integrations) and the absence of a cleanup obligation (models auto-removed).
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Please update your workflows and integrations to use supported models."
- **Quote**: "No action is required to remove the deprecated models."
- **Our assessment**: The failure mode is passive: practitioners who do nothing will find that Claude Sonnet 4 simply disappears from Copilot after the deprecation date. Any integration that references this model identifier will break silently. The "no action required" for removal means the burden is entirely on the update side — practitioners must replace deprecated model references proactively, but can ignore cleanup (the platform handles removal automatically). This mirrors the GPT-5.2 deprecation behavior (see `docs-github-copilot-gpt52-deprecation.md` Claim 6).

### Claim 4: Copilot Enterprise administrators may need to proactively enable access to alternative models through model policies in Copilot settings

- **Evidence**: Required-actions section of official changelog, addressing the enterprise admin layer separately from individual practitioners.
- **Confidence**: settled (stated directly in official changelog; note "may need to" phrasing)
- **Quote**: "Copilot Enterprise administrators may need to enable access to alternative models through their model policies in Copilot settings."
- **Our assessment**: The "may need to" phrasing implies that whether admin action is required depends on the organization's existing policy configuration. Enterprises that have already enabled Claude Sonnet 4.6 in their model policies are unaffected; those that permitted only Claude Sonnet 4 (base) must update their policies to include the replacement. This is the same governance risk pattern as the GPT-5.2 deprecation (see `docs-github-copilot-gpt52-deprecation.md` Claim 5): enterprises whose admins have not pre-enabled replacement models will find their users blocked when the deprecated model disappears. This is a concrete example of why model lifecycle management must be part of recurring enterprise AI governance, not a one-time setup.

### Claim 5: Claude Sonnet 4 was already absent from GitHub's April 2026 model selection roster for Claude agents, indicating the base model had been effectively de-emphasized before formal deprecation

- **Evidence**: `docs-github-copilot-agent-model-selection.md` (issue #171, dated April 14, 2026) listed only Sonnet 4.5, Opus 4.5, Sonnet 4.6, and Opus 4.6 as available Claude models for github.com cloud agents — the base "Claude Sonnet 4" (unversioned) was not in that roster. Similarly, the Copilot CLI auto model pool (`docs-github-copilot-cli-auto-model-selection.md` Claim 3) included Sonnet 4.6 but not base Sonnet 4 as of April 17, 2026.
- **Confidence**: emerging (inferred from absence in prior source notes — the April 14 note does not explain why base Sonnet 4 was not listed)
- **Quote**: (no direct quote; see Our assessment)
- **Our assessment**: The formal deprecation notice (May 7, announcing May 6 effective date) appears to be a trailing acknowledgment of a model that had already been effectively retired from the primary selection UI. Practitioners building on GitHub Copilot agent model selection as of mid-April would not have encountered base Sonnet 4 as an active option. This suggests GitHub may have soft-deprecated the base model earlier and used the formal changelog to document the cutoff date. The lesson for practitioners: follow the official changelog for deprecation dates, but the model selection UI may provide earlier signal that a model generation is being wound down.

### Claim 6: Two model deprecation events (GPT-5.2 and Claude Sonnet 4) occurred within one week of each other in May 2026, reinforcing that GitHub Copilot's model roster turns over at a rapid cadence

- **Evidence**: `docs-github-copilot-gpt52-deprecation.md` was published May 1, 2026 (GPT-5.2 and GPT-5.2-Codex deprecated effective June 1, 2026). This changelog was published May 7, 2026 (Claude Sonnet 4 deprecated effective May 6, 2026 — retroactive announcement). Two deprecations across two model families (OpenAI and Anthropic) in a single week.
- **Confidence**: emerging (the co-occurrence is factual; the "design signal" interpretation is our assessment)
- **Quote**: (no direct quote; date comparison across two source notes)
- **Our assessment**: The GPT-5.2 deprecation note (`docs-github-copilot-gpt52-deprecation.md` Claim 7) introduced the observation that GitHub's model lifecycle runs in weeks-to-months, not years. This deprecation is a second data point in the same week. Practitioners who treat specific model version identifiers as stable long-term references in scripts, CI harnesses, or documentation should expect to revisit those references on a quarterly basis at minimum. The safe design is to prefer auto-routing (see `docs-github-copilot-cli-auto-model-selection.md`) or admin-policy-managed model selection over hardcoded model version strings at the innermost configuration layer.

### Claim 7: GitHub Enterprise customers can reach out to their account manager for assistance with the migration

- **Evidence**: Support guidance at end of changelog.
- **Confidence**: settled (standard support channel statement)
- **Quote**: "GitHub Enterprise customers with questions or concerns are encouraged to reach out to their account manager for further assistance."
- **Our assessment**: This is the same escalation path offered in the GPT-5.2 deprecation. GitHub consistently directs enterprise migration questions to account managers rather than to community forums or generic support. For teams with dedicated account managers, this is the appropriate channel for timeline or policy questions outside the changelog's scope.

## Concrete Artifacts

### Deprecation Summary (from changelog, May 7, 2026)

```
GitHub Copilot Model Deprecation — Effective May 6, 2026

| Model              | Deprecation Date | Suggested Alternative |
|--------------------|------------------|-----------------------|
| Claude Sonnet 4    | May 6, 2026      | Claude Sonnet 4.6     |

Affected surfaces: Copilot Chat, inline edits, ask and agent modes, code completions.
No carve-outs stated (contrast: GPT-5.2-Codex had a Code Review carve-out).
```

*Source: GitHub Copilot official changelog, May 7, 2026*

### Claude Model Roster in GitHub Copilot (post-deprecation, as of May 8, 2026)

```
Active Claude models (from docs.github.com/copilot/reference/ai-models/supported-models):

  GA:
    Claude Haiku 4.5
    Claude Sonnet 4.5
    Claude Sonnet 4.6     ← replacement for deprecated Claude Sonnet 4
    Claude Opus 4.5
    Claude Opus 4.6
    Claude Opus 4.7

  Preview:
    Claude Opus 4.6 (fast mode)

Retired:
    Claude Opus 4.1   — retired February 17, 2026; replaced by Claude Opus 4.6
    Claude Sonnet 4   — retired May 6, 2026; replaced by Claude Sonnet 4.6
```

*Source: GitHub docs supported-models page, accessed May 8, 2026*

### Enterprise Migration Checklist (derived from required actions in changelog)

```
Following Claude Sonnet 4 deprecation (effective May 6, 2026):

Enterprise Copilot Administrators:
[ ] Audit workflows, scripts, and integrations for "claude-sonnet-4" model identifiers.
[ ] If model policy does NOT already include Claude Sonnet 4.6:
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
    Enable Claude Sonnet 4.6 as an available model.
[ ] Verify Claude Sonnet 4.6 appears in the Copilot Chat model selector
    in VS Code and on github.com.
[ ] Update any integration configurations to reference "claude-sonnet-4-6".

Post-May 6:
  - Claude Sonnet 4 has already been removed automatically.
  - No explicit removal action required from admins.
  - Contact your GitHub account manager with migration questions.

Not affected by this deprecation:
  - Claude Sonnet 4.5, Sonnet 4.6 (current)
  - Claude Opus 4.5, 4.6, 4.7 (current)
  - Claude Haiku 4.5 (current)
  - Any Copilot Code Review configurations (no Code Review carve-out stated,
    but Code Review is not listed as a primary affected surface; verify separately)
```

*Source: Required actions section of GitHub Copilot changelog, May 7, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 4: The GPT-5.2 deprecation identified the same four affected surfaces (Copilot Chat, inline edits, ask and agent modes, code completions). GitHub is applying a uniform surface scope to deprecations regardless of model family (OpenAI or Anthropic). The pattern is consistent.

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 5 and Claim 6: Both deprecations share the same behavioral semantics — practitioners must enable replacements proactively (admin action for Enterprise), and deprecated models disappear automatically with no cleanup obligation. The governance risk pattern (enterprise admins who do nothing will find workflows broken) is identical.

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 7 (rapid model lifecycle cadence): That note identified the GPT-5.2 generation as retired approximately 7 weeks after GPT-5.4 support was added. This Claude Sonnet 4 deprecation — also in May 2026, one week after the GPT-5.2 notice — is a second data point confirming that GitHub's model roster turns over on a weeks-to-months cadence across both model families.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3: The CLI auto model pool already excluded Claude Sonnet 4 (listing Sonnet 4.6 instead) as of April 17, 2026. This deprecation formalizes what the auto pool's composition already implied: base Sonnet 4 had been superseded by Sonnet 4.6 in GitHub's preferred routing configuration before the deprecation was announced.

- **Extends** `docs-github-copilot-agent-model-selection.md` Claim 5 (two-layer admin governance model): The April 14 note documented org admin policy + repo-level enablement as a governance setup. This deprecation adds a recurring lifecycle dimension: admin policies set up for the deprecated model generation may need to be updated. Enterprise governance is not a one-time configuration — model deprecations require a recurring review cycle.

- **Extends** `docs-github-copilot-agent-model-selection.md` Extraction Notes (point 5), which anticipated exactly this type of change: "Model lists for cloud AI services change frequently (new versions added, older versions deprecated). Check the changelog for updates before citing specific version names." This deprecation is a second instance (after GPT-5.2) confirming the urgency of that caveat.

- **Contradicts**: None. This deprecation updates model availability facts that prior notes explicitly anticipated would change. The base Claude Sonnet 4 was not an actively promoted model in the April 2026 roster notes; no claim in the existing corpus is materially contradicted.

- **Novel**: Second model deprecation event in the corpus (first was `docs-github-copilot-gpt52-deprecation.md`), and the first Claude-specific deprecation. Establishes that both the OpenAI and Anthropic model families hosted in Copilot operate on the same rapid deprecation cadence. Also introduces the pattern of a *retroactive* deprecation announcement: the changelog was published May 7 but announced an effective date of May 6 — the model was already removed before practitioners received the formal notice.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Claude model roster update**: Any model table or roster in the guide that listed Claude Sonnet 4 (the base, unversioned Sonnet 4) should mark it as deprecated (effective May 6, 2026). The April 14 model roster in `docs-github-copilot-agent-model-selection.md` did not list base Sonnet 4, so no existing corpus-derived table likely needs this update — but verify before publishing.
- **Design principle — avoid hardcoded model identifiers**: Together with `docs-github-copilot-gpt52-deprecation.md`, this is the second concrete evidence within one week that specific model version strings have a short shelf life in Copilot configurations. Strengthen the existing recommendation (introduced in the GPT-5.2 note): prefer auto-routing or admin-policy-managed model selection over pinning specific model version strings in scripts, CI harnesses, and integrations.
- **Retroactive deprecation as a risk pattern**: The deprecation was effective May 6 but announced May 7. Practitioners relying solely on changelog monitoring would have experienced a one-day window where Claude Sonnet 4 was already removed without formal notice. This strengthens the case for the proactive monitoring pattern: use the model selection UI (not just the changelog) to detect de-emphasis of a model before formal deprecation.

### Chapter 05: Team Adoption / Enterprise Governance

- **Model lifecycle management as a recurring governance obligation**: Two deprecation events in May 2026 (GPT-5.2 and Claude Sonnet 4) establish that enterprise Copilot governance requires a recurring review cadence. Recommend teams add "Copilot changelog review" as a monthly governance checkpoint, specifically watching for deprecation notices with admin-action requirements. Reference this note and `docs-github-copilot-gpt52-deprecation.md` together as evidence.
- **Retroactive notice as a governance risk**: The one-day gap between the May 6 effective date and the May 7 changelog publication is a concrete example that Copilot deprecations may not always provide advance notice. Enterprise governance policies should not assume adequate warning time for model transitions. Proactive monitoring of the model selection UI and supported-models documentation page is preferable to reactive changelog monitoring.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 150 words. All extractable facts are captured in the seven claims above. The source provides no capability comparison between Claude Sonnet 4 and Sonnet 4.6, no migration tooling, and no post-cutover error behavior specification.
2. **Retroactive effective date**: The changelog is dated May 7, 2026, but states the deprecation was effective May 6, 2026. This means the model was already removed when the notice was published. The one-day gap is noted in Claim 6 and Guide Impact; the Assayer should be aware this is not an extraction error.
3. **Base Sonnet 4 vs. 4.5/4.6**: The deprecated model is "Claude Sonnet 4" — the original, unversioned Sonnet 4, not the subsequent 4.5 or 4.6 variants. Claim 5 discusses that this model was already absent from the April 2026 GitHub UI. This distinction is operationally important — practitioners using Sonnet 4.5 or 4.6 are completely unaffected.
4. **Supported-models page used as secondary source**: The docs page (docs.github.com/copilot/reference/ai-models/supported-models) was fetched to verify the current roster and confirm the retirement entry. That page listed "Claude Sonnet 4 (retiring May 1, 2026)" — a slight date discrepancy vs. the changelog's May 6. The official changelog date (May 6) is used as authoritative; the docs page discrepancy is likely rounding or pre-announcement draft text.
5. **No contradictions filed**: No claim in the existing corpus is materially contradicted by this deprecation. No contradiction issue required.
