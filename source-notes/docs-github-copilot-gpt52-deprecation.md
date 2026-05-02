---
source_url: https://github.blog/changelog/2026-05-01-upcoming-deprecation-of-gpt-5-2-and-gpt-5-2-codex
source_type: docs
title: "Upcoming deprecation of GPT-5.2 and GPT-5.2-Codex"
author: GitHub (official changelog)
date_published: 2026-05-01
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: settled
issue: "#495"
---

# Upcoming Deprecation of GPT-5.2 and GPT-5.2-Codex

> GitHub's May 2026 deprecation notice removing GPT-5.2 and GPT-5.2-Codex from Copilot by June 1, 2026 — with GPT-5.5 and GPT-5.3-Codex as named replacements, a Copilot Code Review carve-out, and an enterprise admin pre-migration requirement that will silently break workflows if unaddressed.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words)
- **Author credibility**: GitHub engineering team. Authoritative for the deprecation timeline, successor model designations, and enterprise admin requirements. Not a source for model capability comparisons or migration effort estimation.
- **Scope**: Deprecation of GPT-5.2 and GPT-5.2-Codex from Copilot Chat, inline edits, ask and agent modes, and code completions, effective June 1, 2026. Covers the replacement models recommended by GitHub and the admin action required for Enterprise teams. Does NOT cover: capability differences between deprecated and replacement models, whether any model selection UI changes accompany the deprecation, cost implications for practitioners, or the deprecation timeline for other model generations.

## Extracted Claims

### Claim 1: GPT-5.2 is deprecated across Copilot experiences effective June 1, 2026, with GPT-5.5 as the suggested replacement

- **Evidence**: Official GitHub Copilot changelog. Deprecation date and successor model stated in a dedicated table in the announcement.
- **Confidence**: settled (authoritative product fact — date and successor are stated directly)
- **Quote**: "GPT-5.2 | 6-01-2026 | GPT-5.5" (from the deprecation table)
- **Our assessment**: The jump from GPT-5.2 to GPT-5.5 (skipping 5.3 and 5.4) routes GPT-5.2 users directly to the current premium tier. For practitioners who were using GPT-5.2 expecting a budget-tier model, GPT-5.5 carries materially higher API token costs (see `blog-simonwillison-gpt55-codex-plugin.md` Claim 4: GPT-5.5 is priced at $5/$30 per 1M tokens vs. GPT-5.4 at $2.5/$15). Whether GitHub's Copilot billing model exposes this cost difference to practitioners is not addressed in the changelog.

### Claim 2: GPT-5.2-Codex is deprecated across Copilot experiences effective June 1, 2026, with GPT-5.3-Codex as the suggested replacement

- **Evidence**: Official GitHub Copilot changelog. Deprecation date and successor model stated in the same deprecation table.
- **Confidence**: settled (authoritative product fact)
- **Quote**: "GPT-5.2-Codex | 6-01-2026 | GPT-5.3-Codex" (from the deprecation table)
- **Our assessment**: GPT-5.3-Codex is already in the Copilot CLI auto model pool (see `docs-github-copilot-cli-auto-model-selection.md` Claim 3) and in the web-agent model selection roster (see `docs-github-copilot-agent-model-selection.md` Claim 3). For practitioners who explicitly pinned GPT-5.2-Codex, the migration is a one-version step within the same Codex family. Teams already using auto-routing in the CLI receive GPT-5.3-Codex automatically and are unaffected by this deprecation.

### Claim 3: GPT-5.2-Codex in Copilot Code Review is explicitly excluded from the June 1, 2026 deprecation

- **Evidence**: Changelog states one explicit exception: GPT-5.2-Codex used within Copilot Code Review is not included in the June 1 deprecation.
- **Confidence**: settled (explicit carve-out stated in official changelog)
- **Quote**: "Note: GPT-5.2-Codex in Copilot Code Review is not included in this deprecation" (paraphrased; the carve-out is stated directly in the source)
- **Our assessment**: This is the most nuanced operational detail in the changelog. Enterprise teams using GPT-5.2-Codex specifically for Code Review workflows need not act before June 1. However, practitioners must not generalize this carve-out: GPT-5.2-Codex is still deprecated in all other surfaces (Chat, inline edits, ask and agent modes, completions). A future separate deprecation notice should be expected for the Code Review use case.

### Claim 4: The deprecation affects Copilot Chat, inline edits, ask and agent modes, and code completions

- **Evidence**: Changelog explicitly lists the affected surfaces.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Copilot Chat, inline edits, ask and agent modes, and code completions"
- **Our assessment**: This is a broad surface scope covering the primary AI-native engineering touchpoints: IDE completions, chat, and agentic task modes. Any practitioner using GitHub Copilot for any of these surfaces with an explicitly pinned GPT-5.2 or GPT-5.2-Codex model identifier will need to update their configuration before June 1.

### Claim 5: Enterprise administrators must proactively enable replacement models via Copilot model policies before June 1, 2026 — no automatic migration of admin policies occurs

- **Evidence**: Changelog states that users must "update your workflows and integrations to use supported models before these dates" and that Enterprise administrators should enable alternative models through Copilot settings and verify availability in the model selector.
- **Confidence**: settled (required action stated directly in official changelog)
- **Quote**: "update your workflows and integrations to use supported models before these dates" and "Enterprise administrators should enable alternative models through Copilot settings and verify availability in the model selector across VS Code and github.com"
- **Our assessment**: This is the highest-stakes operational claim in the source. On June 1, Enterprise teams whose admins have not enabled GPT-5.5 or GPT-5.3-Codex in model policies will find that the deprecated models simply disappear, with no automatic replacement. Engineering workflows that reference these models will fail silently or fall back to an unexpected default. This is a concrete example of why proactive model lifecycle management must be part of enterprise AI governance — not just a one-time setup step (see Guide Impact §Ch05).

### Claim 6: After deprecation, old models disappear automatically — no admin action is required for removal, only for adding replacements

- **Evidence**: Changelog frames required action entirely as enabling replacements before the deadline. No removal action by admins is described or implied.
- **Confidence**: settled (standard platform deprecation model; the required-action section addresses enablement only)
- **Quote**: (implied by the required-actions section focusing solely on enabling replacements and updating configurations, not removing old models)
- **Our assessment**: The failure mode here is passive: practitioners and admins who do nothing will discover the model is gone after June 1. The safe path is to enable replacements and update configurations before the deadline, then allow the deprecated models to disappear automatically. Admins who only remove old model references from policy without enabling replacements will still face workflow breaks.

### Claim 7: The GPT-5.2 generation is deprecated approximately 7 weeks after GPT-5.4 support was added to Copilot, demonstrating a rapid model lifecycle cadence on this platform

- **Evidence**: `docs-github-copilot-agent-model-selection.md` (issue #171, dated April 14, 2026) listed GPT-5.2-Codex as a current model option; this deprecation notice is dated May 1, 2026 with a June 1 effective date. The gap between adding GPT-5.4 support and announcing GPT-5.2 retirement is approximately 17 days; the actual retirement is 48 days after the GPT-5.4 announcement.
- **Confidence**: emerging (the timeline is derived from dated source notes; the inference about "lifecycle cadence as a design signal" is our interpretation, not a stated claim in the changelog)
- **Quote**: (inferred from source dates, not directly stated in changelog)
- **Our assessment**: As the Prospector triage note identified: "GitHub is already retiring GPT-5.2 less than two months after publishing GPT-5.4 support." For practitioners, this is evidence that hardcoded model identifiers in Copilot workflows have a shelf life measurable in weeks, not months or years. This strengthens the design recommendation to prefer auto-routing or admin-policy-managed model selection over pinning specific model version strings in scripts, harness configurations, or CI jobs.

## Concrete Artifacts

### Deprecation Table (from changelog, May 1, 2026)

```
GitHub Copilot Model Deprecation — Effective June 1, 2026

| Model          | Deprecation Date | Suggested Alternative |
|----------------|------------------|----------------------|
| GPT-5.2        | June 1, 2026     | GPT-5.5              |
| GPT-5.2-Codex  | June 1, 2026     | GPT-5.3-Codex        |

EXCEPTION: GPT-5.2-Codex in Copilot Code Review is NOT included in this deprecation.

Affected surfaces: Copilot Chat, inline edits, ask and agent modes, code completions.
```

*Source: GitHub Copilot official changelog, May 1, 2026*

### Enterprise Migration Checklist (derived from required actions in changelog)

```
Before June 1, 2026 — Enterprise Copilot Administrators:

[ ] Audit workflows, scripts, and integrations that explicitly pin "gpt-5.2"
    or "gpt-5.2-codex" as model identifiers.
[ ] Enable GPT-5.5 in Copilot model policy settings (replacement for GPT-5.2):
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
[ ] Enable GPT-5.3-Codex in model policy settings (replacement for GPT-5.2-Codex):
    Navigate: org/enterprise Settings > Copilot > Policies > [Model access]
[ ] Verify replacement model availability in VS Code model selector and github.com.
[ ] Update integration configurations to reference replacement model names.
[ ] If using GPT-5.2-Codex for Code Review only: no action required before June 1
    (carve-out confirmed; watch for a future deprecation notice for this surface).

Post-June 1:
  - GPT-5.2 and GPT-5.2-Codex (except Code Review) disappear automatically.
  - No explicit removal action required from admins.

Support: GitHub Enterprise customers can reach out to their account manager
for further assistance.
```

*Source: Required actions section of GitHub Copilot changelog, May 1, 2026*

## Cross-References

- **Corroborates** `docs-github-copilot-agent-model-selection.md` Extraction Notes (point 5): That note warned "model lists for cloud AI services change frequently (new versions added, older versions deprecated)... Check the changelog for updates before citing specific version names." This deprecation announcement is precisely the kind of update that note anticipated. The model roster in `docs-github-copilot-agent-model-selection.md` Concrete Artifacts → Model Roster section (which listed `gpt-5.2-codex` as an active Codex option as of April 14) is now superseded — GPT-5.2-Codex exits the web-agent selection roster on June 1.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3: The CLI auto model pool (GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, Haiku 4.5 as of April 17) already excluded GPT-5.2 and GPT-5.2-Codex. This deprecation is consistent with that forward-looking pool design — auto-routing was already routing around the soon-to-be-retired GPT-5.2 generation before the deprecation was announced.

- **Corroborates** `blog-simonwillison-gpt55-codex-plugin.md` Claim 4 (GPT-5.5 pricing and positioning as the premium-tier successor): Willison documented GPT-5.5 as the natural successor tier to GPT-5.4, priced at 2× GPT-5.4. This deprecation changelog designates GPT-5.5 as the explicit replacement for GPT-5.2, positioning GPT-5.5 as the definitive current-generation upgrade path for GPT-5.2 users.

- **Extends** `docs-github-copilot-agent-model-selection.md` Claim 5 (two-layer admin governance model for model access): That source documented org admin policy + repo-level enablement as a one-time governance setup. This deprecation adds a lifecycle management dimension: admin governance requires a recurring review cadence aligned with model deprecation notices — it is not a set-once configuration.

- **Contradicts**: None. The deprecation updates model availability facts that existing notes explicitly anticipated would change. No claim in the existing corpus directly contradicts this announcement.

- **Novel**: First source in corpus to document a model *deprecation* event in GitHub Copilot (as opposed to model additions). Establishes a concrete data point on model lifecycle cadence: the GPT-5.2 generation is retired approximately 7 weeks after GPT-5.4 support was announced. This is the first in-corpus evidence of the speed at which Copilot's model roster turns over — a design constraint for practitioners building configurations that reference specific model version strings.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: GPT-5.2 and GPT-5.2-Codex should be marked as deprecated (effective June 1, 2026) in any model selection table or roster the guide maintains. The roster from `docs-github-copilot-agent-model-selection.md` listed GPT-5.2-Codex — annotate or remove it. GPT-5.5 should be added as the base-model replacement; GPT-5.3-Codex was already listed as current.
- **Design principle — avoid hardcoded model identifiers**: This deprecation is direct evidence that specific model version strings (e.g., `"gpt-5.2-codex"`) have a shelf life measurable in weeks in Copilot configurations. Add an explicit recommendation: prefer auto-routing (Copilot CLI auto mode, per `docs-github-copilot-cli-auto-model-selection.md`) or admin-policy-managed model selection over hardcoding model names in scripts, CI harnesses, and integrations. Tie model selection to the policy layer, not the innermost configuration layer, so that future model transitions require only an admin policy update, not a code change.

### Chapter 05: Team Adoption / Enterprise Governance

- **Model lifecycle management as an ongoing governance responsibility**: This deprecation is a concrete example that enterprise Copilot governance is not a one-time setup. Enterprise teams whose admins do not act before June 1 will experience silent workflow failures at the cutover. Recommend teams add "Copilot changelog review" as a recurring entry in their AI governance checklist, specifically watching for deprecation notices that carry admin-action requirements.
- **Silent failure mode as a governance risk pattern**: Deprecated models disappear automatically — no warning at the moment of failure. Workflows that reference deprecated model identifiers will break silently after June 1. This is a broader pattern: governance policies that are correct at setup time can become incorrect when the platform evolves. Enterprise AI governance must include mechanisms to detect and respond to upstream platform changes, not just enforce internal policies.

## Extraction Notes

1. **Source is very thin by design**: The changelog is approximately 200 words. All extractable facts are captured in the seven claims above. The source provides no capability comparison between deprecated and replacement models, no migration tooling, and no specification of post-cutover error behavior (silent failure vs. explicit error message).
2. **WebFetch returned structured summary**: The page content was returned as a structured markdown summary rather than verbatim HTML. Quotes from the deprecation table and required-actions section appear accurate; some claims are paraphrased rather than directly quoted where verbatim reproduction was not possible from the structured summary.
3. **GPT-5.2-Codex Code Review carve-out**: The carve-out is clearly stated in the source. This note does not speculate about when a separate deprecation for that surface will be announced.
4. **No contradictions filed**: The deprecation updates model availability facts that prior notes explicitly anticipated would change. No claim in the existing corpus is materially contradicted. No contradiction issue required.
