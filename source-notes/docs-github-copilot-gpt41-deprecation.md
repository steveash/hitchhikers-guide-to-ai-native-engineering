---
source_url: https://github.blog/changelog/2026-05-07-upcoming-deprecation-of-gpt-4-1
source_type: docs
title: "Upcoming deprecation of GPT-4.1"
author: GitHub (official changelog)
date_published: 2026-05-07
date_extracted: 2026-05-08
last_checked: 2026-05-08
status: current
confidence_overall: settled
issue: "#563"
---

# Upcoming Deprecation of GPT-4.1

> GitHub's May 7, 2026 deprecation notice retiring GPT-4.1 from all Copilot experiences on June 1, 2026 — with GPT-5.5 as the named replacement, no carve-outs, and the same enterprise admin pre-migration requirement established by the May 1 GPT-5.2 notice; together these two notices confirm a June 2026 batch retirement across multiple Copilot model generations with a compressed 25-day notice window.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words)
- **Author credibility**: GitHub engineering team. Authoritative for the deprecation timeline, successor model designation, and enterprise admin requirements. Not a source for capability comparisons between GPT-4.1 and GPT-5.5, migration effort estimation, or cost implications.
- **Scope**: Deprecation of GPT-4.1 from Copilot Chat, inline edits, ask and agent modes, and code completions, effective June 1, 2026. Covers the replacement model (GPT-5.5) and the admin action required for Enterprise teams. Does NOT cover: capability differences between GPT-4.1 and GPT-5.5, whether GPT-4.1 was available in Copilot Code Review, cost implications of migrating to GPT-5.5, or why GPT-4.1 is being retired alongside GPT-5.2 in the same batch.

## Extracted Claims

### Claim 1: GPT-4.1 is deprecated across all GitHub Copilot experiences effective June 1, 2026, with GPT-5.5 as the suggested replacement

- **Evidence**: Official GitHub Copilot changelog. Deprecation date and successor model stated directly in a structured table.
- **Confidence**: settled (authoritative product fact — date and successor stated directly)
- **Quote**: "We will deprecate the following model across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on 6/1/2026"
- **Our assessment**: GPT-5.5 was already designated as the replacement for GPT-5.2 in the May 1 deprecation notice (see `docs-github-copilot-gpt52-deprecation.md` Claim 1). Routing both GPT-4.1 (older generation) and GPT-5.2 (more recent generation) to GPT-5.5 as the single replacement confirms GPT-5.5 is GitHub's current-generation default — practitioners on any older model identifier converge on GPT-5.5 as the upgrade path regardless of which legacy model they were using.

### Claim 2: The deprecation affects the same broad set of Copilot surfaces as GPT-5.2 — with no stated carve-outs

- **Evidence**: Changelog lists affected surfaces as "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)" and mentions no exceptions.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)"
- **Our assessment**: The GPT-5.2 deprecation notice included an explicit carve-out for GPT-5.2-Codex in Copilot Code Review. No equivalent carve-out exists in the GPT-4.1 notice, either because GPT-4.1 was not used in Code Review or because GitHub chose a clean deprecation with no exceptions. Practitioners who used GPT-4.1 in any Copilot surface should treat June 1 as a hard unconditional cutoff.

### Claim 3: Enterprise administrators must proactively enable replacement models via Copilot model policies before June 1 — no automatic migration of admin policies occurs

- **Evidence**: Changelog states administrators "may need to enable access to alternative models through their model policies." Verification step is described: administrators can "verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model."
- **Confidence**: settled (required action stated directly in official changelog)
- **Quote**: "Copilot Enterprise administrators may need to enable access to alternative models through their model policies."
- **Our assessment**: Identical governance failure mode to GPT-5.2 (`docs-github-copilot-gpt52-deprecation.md` Claim 5): Enterprise teams whose admins have not enabled GPT-5.5 before June 1 will find GPT-4.1 disappears with no automatic replacement. For teams that already enabled GPT-5.5 for the GPT-5.2 migration, no additional admin action is required — GPT-5.5 coverage handles both deprecations. Teams that missed the May 1 GPT-5.2 migration notice now face a compound risk: two model identifiers retiring on the same date.

### Claim 4: After deprecation, the model disappears automatically — no admin action is required for removal

- **Evidence**: Changelog states "No action is required to remove the models once they have been deprecated."
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "No action is required to remove the models once they have been deprecated."
- **Our assessment**: The passive failure path is to do nothing and discover GPT-4.1 is gone after June 1. The active path is to enable GPT-5.5 before June 1. Unlike the GPT-5.2 case, there is no secondary complexity (no Code Review carve-out, no Codex sub-variant distinction) — GPT-4.1 is a clean, unconditional removal.

### Claim 5: The GPT-4.1 notice-to-cutoff window is 25 days — 6 days shorter than the 31-day window for GPT-5.2

- **Evidence**: GPT-5.2 deprecation notice published May 1, 2026 → June 1, 2026 cutoff = 31 days. GPT-4.1 deprecation notice published May 7, 2026 → June 1, 2026 cutoff = 25 days. Both cutoffs land on the same date.
- **Confidence**: emerging (timeline derived from dated sources; inference about cadence is analytical interpretation, not a stated claim in either changelog)
- **Quote**: (no direct quote; inferred from publication dates across two sources)
- **Our assessment**: The Prospector triage asked whether the notice-to-cutoff window was shorter than for GPT-5.2. The answer is yes: 25 days vs. 31 days. The more significant signal is that both cutoffs land on June 1 — GitHub is executing a coordinated batch retirement of multiple legacy generations simultaneously, with staggered notice dates. Practitioners monitoring the changelog cannot assume a later notice means a later cutoff. Any new deprecation notice should be checked for its specific cutoff date, not assumed to follow a fixed lead-time convention.

### Claim 6: June 1, 2026 is a batch retirement cutoff — two separate deprecation notices (GPT-5.2 on May 1, GPT-4.1 on May 7) both target the same date

- **Evidence**: `docs-github-copilot-gpt52-deprecation.md` documents the May 1 notice with June 1 cutoff; this source documents the May 7 notice also with June 1 cutoff.
- **Confidence**: settled (both cutoff dates are stated in official changelogs)
- **Quote**: (no direct quote; comparison across two authoritative sources)
- **Our assessment**: The coincidence of the same June 1 cutoff across two notices from different dates confirms this is a coordinated batch retirement rather than two independent lifecycle events. Practitioners who saw and acted on the May 1 notice and enabled GPT-5.5 are already covered for the GPT-4.1 transition — the same replacement model handles both. Practitioners who missed both notices face simultaneous loss of access to multiple model identifiers. This pattern strengthens the guide recommendation to treat Copilot changelog review as a recurring governance task that looks for new notices targeting already-announced cutoff dates.

### Claim 7: GPT-5.5 is the designated replacement for both GPT-4.1 and GPT-5.2, making it the universal single successor across multiple Copilot model generations

- **Evidence**: `docs-github-copilot-gpt52-deprecation.md` Claim 1 designates GPT-5.5 as replacement for GPT-5.2; this source designates GPT-5.5 as replacement for GPT-4.1.
- **Confidence**: settled (both designations stated in official changelogs)
- **Quote**: (from this source's deprecation table: "GPT-4.1" → suggested alternative "GPT-5.5")
- **Our assessment**: For practitioners with configurations referencing either GPT-4.1 or GPT-5.2, the migration target is the same: GPT-5.5. The convergence on a single successor simplifies the migration (one model to enable, one identifier to update) but amplifies the risk of a missed migration: anyone who has not enabled GPT-5.5 simultaneously loses access to both legacy model lines on June 1.

## Concrete Artifacts

### Deprecation Table (from changelog, May 7, 2026)

```
GitHub Copilot Model Deprecation — Effective June 1, 2026

| Model    | Deprecation Date | Suggested Alternative |
|----------|------------------|-----------------------|
| GPT-4.1  | June 1, 2026     | GPT-5.5               |

No exceptions or carve-outs stated.
Affected surfaces: all GitHub Copilot experiences (Copilot Chat, inline edits,
                   ask and agent modes, code completions).
```

*Source: GitHub Copilot official changelog, May 7, 2026*

### Combined June 2026 Batch Retirement Picture (derived from two changelogs)

```
Simultaneous June 1, 2026 Deprecations:

Notice May 1 → docs-github-copilot-gpt52-deprecation.md:
  GPT-5.2        → GPT-5.5          (31 days notice)
  GPT-5.2-Codex  → GPT-5.3-Codex   (31 days notice)
    EXCEPTION: GPT-5.2-Codex in Copilot Code Review (carve-out, watch for
               a future separate deprecation notice for that surface)

Notice May 7 → this source:
  GPT-4.1        → GPT-5.5          (25 days notice)
    No exceptions.

Single required admin action covers both notices:
  [ ] Enable GPT-5.5 in Copilot model policy before June 1, 2026
  [ ] Enable GPT-5.3-Codex in Copilot model policy before June 1, 2026
      (for teams that explicitly pinned GPT-5.2-Codex outside Code Review)
```

*Derived from this source and `docs-github-copilot-gpt52-deprecation.md`*

### Enterprise Migration Checklist for June 2026 Batch Cutover

```
Before June 1, 2026 — Enterprise Copilot Administrators:

[ ] Audit workflows, scripts, and integrations referencing "gpt-4.1"
[ ] Enable GPT-5.5 in Copilot model policy settings (covers both GPT-4.1
    and GPT-5.2 migration targets):
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
[ ] Verify GPT-5.5 availability in VS Code model selector and github.com:
    "verify availability by checking your individual Copilot settings and
     confirming that the policy is enabled for the specific model"
[ ] Update integration configurations to reference "gpt-5.5"

Note: If GPT-5.5 was already enabled for the May 1 GPT-5.2 migration,
no additional admin action is required for the GPT-4.1 migration.

Post-June 1:
  - GPT-4.1 disappears automatically.
  - "No action is required to remove the models once they have been deprecated."

Support: "GitHub Enterprise customers with questions or concerns are
          encouraged to reach out to their account manager for further
          assistance."
```

*Source: Required actions section of GitHub Copilot changelog, May 7, 2026,
 combined with `docs-github-copilot-gpt52-deprecation.md` enterprise checklist*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claims 4, 5, and 6: the same affected surface list, the same enterprise admin pre-migration requirement (proactively enable replacement models; no auto-migration of policies), and the same post-deprecation auto-removal behavior all recur verbatim in this notice, confirming these as settled patterns in GitHub's model deprecation playbook rather than one-off behaviors for GPT-5.2.

- **Extends** `docs-github-copilot-gpt52-deprecation.md` Claim 7 (model lifecycle cadence): that claim derived a lifecycle inference from a single data point. This source provides the second data point, adding new evidence: (a) the June 2026 retirement is a **coordinated batch event** rather than a sequence of independent lifecycle decisions, and (b) the notice window is **compressed** for later notices targeting the same cutoff (25 days vs. 31 days). Both observations strengthen the design recommendation to avoid hardcoded model identifiers in Copilot configurations.

- **Corroborates** `docs-github-copilot-agent-model-selection.md` Extraction Notes (point 5): that note warned "model lists for cloud AI services change frequently (new versions added, older versions deprecated)... Check the changelog for updates before citing specific version names." GPT-4.1 did not appear in the April 14 model roster (it was already older than the listed models), but its simultaneous deprecation with GPT-5.2 shows that turnover applies to all generations tracked or untracked in that roster, not just the most recent.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3: the CLI auto model pool (GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, and Haiku 4.5 as of April 17) already excluded both GPT-5.2 and GPT-4.1 before either deprecation notice was published. The auto router was ahead of the formal deprecation, having already shed the legacy generations before the notices arrived.

- **Contradicts**: None. This source repeats and reinforces patterns established by `docs-github-copilot-gpt52-deprecation.md`. No material contradictions with existing corpus claims. No contradiction issue required.

- **Novel**: Second in-corpus documentation of a GitHub Copilot model deprecation event (first was `docs-github-copilot-gpt52-deprecation.md`). Novel aspects:
  - First evidence of a **coordinated batch retirement**: two model generations retired on the same date via staggered notices, rather than two independent lifecycle events.
  - **Compressed notice window confirmed**: 25 days for GPT-4.1 (legacy generation) vs. 31 days for GPT-5.2 (recent generation) — practitioners cannot assume a generous or consistent notice lead time.
  - **GPT-5.5 as universal successor** across multiple generations: first confirmation that a single replacement model covers multiple retiring model identifiers simultaneously.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: GPT-4.1 should be marked as deprecated (effective June 1, 2026). GPT-5.5 is now confirmed as the replacement for multiple legacy Copilot model lines (GPT-4.1 and GPT-5.2). Any guide model roster table should note this convergence.
- **Design principle — avoid hardcoded model identifiers**: The batch nature of this retirement (two model lines, same date, staggered notices) is direct evidence that configurations referencing specific model version strings can become invalid simultaneously. Strengthen the recommendation from `docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02: prefer auto-routing (Copilot CLI auto mode, per `docs-github-copilot-cli-auto-model-selection.md`) or admin-policy-managed model selection over hardcoding model names. Practitioners who adopted auto-routing after the GPT-5.2 notice were already covered for GPT-4.1 without any additional action — a concrete demonstration of the design principle's value.

### Chapter 05: Team Adoption / Enterprise Governance

- **Batch deprecation as a governance pattern requiring adjusted monitoring**: The June 2026 batch retirement changes the governance calculus. Practitioners who monitor the changelog and act on each individual notice may still be caught: two notices, same cutoff date, but the second notice arrives with 6 fewer days of lead time. A governance process that triggers action only on first notice of a given cutoff date may miss subsequent notices. Recommend governance processes explicitly check whether new deprecation notices target an already-announced cutoff date when one is in flight.
- **Compound risk for missed migrations**: Teams that missed both the May 1 GPT-5.2 notice and the May 7 GPT-4.1 notice simultaneously lose access to multiple model identifiers on June 1 with no fallback. Unlike sequential retirements, a batch retirement amplifies the consequence of a single governance process gap.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 200 words. All extractable facts are captured in the seven claims above. The source provides no capability comparison between GPT-4.1 and GPT-5.5, no migration tooling, and no specification of post-cutover error behavior.
2. **WebFetch returned structured summary, not verbatim HTML**: Page content was returned as a structured markdown summary rather than verbatim HTML. Quotes in the claims above appeared in the WebFetch output and are likely accurate, but the Assayer should spot-check key quotes against the live source URL before treating them as character-for-character verbatim.
3. **GPT-4.1 generation context**: As of the April 14, 2026 model selection roster (`docs-github-copilot-agent-model-selection.md`), GPT-4.1 did not appear as a current model option for GitHub agents on github.com — it was already legacy. Its retirement alongside GPT-5.2 on the same date suggests GitHub is clearing multiple deprecated generations in a single June 2026 housekeeping event.
4. **No contradictions filed**: This source repeats and extends patterns from `docs-github-copilot-gpt52-deprecation.md`. No material contradictions with existing corpus claims.
5. **No carve-out complexity**: Unlike GPT-5.2-Codex (which had an explicit Code Review carve-out), GPT-4.1 has no stated exceptions. The deprecation is unconditional.
