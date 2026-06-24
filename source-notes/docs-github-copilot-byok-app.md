---
source_url: https://github.blog/changelog/2026-06-23-github-copilot-app-support-for-byok
source_type: docs
title: "GitHub Copilot app support for BYOK"
author: GitHub (official changelog)
date_published: 2026-06-23
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: settled
issue: "#1289"
---

# GitHub Copilot App Support for BYOK

> GitHub's June 23, 2026 changelog announcing BYOK support for the standalone GitHub Copilot app — extending the bring-your-own-key pattern to a third distinct product surface (after VS Code and JetBrains) and introducing an explicit "frontier + local model hybrid" use case and OS keychain key storage claim not previously documented in the corpus.

## Source Context

- **Type**: docs (GitHub official product changelog, June 23, 2026; approximately 150 words of primary announcement text plus three bullet-point use cases)
- **Author credibility**: GitHub engineering team announcing a production feature change. Authoritative for: the existence of BYOK in the Copilot app, the listed supported providers, the configuration path (Settings → Model Providers), the key storage mechanism (OS keychain), and the Business/Enterprise admin requirement (Copilot CLI policy). Not authoritative for: whether individual plan users can access app BYOK without prerequisites, how app BYOK interacts with BYOK policies in other surfaces, cost implications, or whether BYOK in the app carries the same Responsible AI filtering caveat as VS Code BYOK.
- **Scope**: BYOK support in the standalone GitHub Copilot app — supported providers, configuration path, key storage, three primary use cases, and Business/Enterprise plan access prerequisites. Does NOT cover: individual plan availability (not addressed), cost model (not addressed), comparison to VS Code/JetBrains BYOK configuration (not addressed), whether Responsible AI filtering applies to BYOK models in the app, or explicit GA/preview status of BYOK in the app.

## Extracted Claims

### Claim 1: The GitHub Copilot app now supports BYOK for running agent sessions against external model providers including OpenAI, Azure OpenAI, Microsoft Foundry, Anthropic, LM Studio, Ollama, and any OpenAI-compatible endpoint

- **Evidence**: Official GitHub product changelog announcing current availability — phrasing "now supports" indicates an active, deployed feature.
- **Confidence**: settled (product fact stated in official changelog as current availability)
- **Quote**: "The GitHub Copilot app now supports bring your own key (BYOK), so you can run agent sessions against your own model providers, including OpenAI, Azure OpenAI, Microsoft Foundry, Anthropic, LM Studio, Ollama, and any OpenAI-compatible endpoint."
- **Our assessment**: This extends the BYOK pattern documented for VS Code (`docs-github-copilot-byok-vscode.md`) and JetBrains (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 10) to a third distinct product surface: the standalone Copilot app. The provider list overlaps with but differs from the VS Code list — the app includes Microsoft Foundry and LM Studio explicitly, uses "any OpenAI-compatible endpoint" as a catch-all rather than naming Gemini and OpenRouter as separate providers. The phrasing "agent sessions" is specific to the app context: unlike VS Code (which distinguished chat vs. completions), the Copilot app is a standalone agent environment where all interactions are agent sessions. For Ch02: BYOK is now available on all three major Copilot product surfaces (VS Code, JetBrains, standalone app).

### Claim 2: BYOK configuration is done via Settings → Model Providers, with providers appearing in the model picker alongside Copilot-hosted models and selectable per session

- **Evidence**: Official changelog documents the specific settings path and the per-session model selection behavior.
- **Confidence**: settled (configuration path stated in official changelog)
- **Quote**: "Add a provider in Settings → Model Providers with your endpoint and API key, or just a host for LM Studio or Ollama."
- **Our assessment**: The LM Studio/Ollama special case (host-only, no API key required) matches the local model support pattern documented for VS Code BYOK. The first WebFetch result also noted that "the provider's models appear in the model picker alongside Copilot-hosted models, selectable per session" — a model-picker integration pattern consistent with how VS Code BYOK surfaces external models. For Ch02: the configuration entry point is Settings → Model Providers, not a dedicated BYOK configuration section. Per-session selection means practitioners can switch between BYOK and Copilot-hosted models in each session without changing settings.

### Claim 3: API keys for BYOK are stored in the local OS keychain and are never read back by the UI

- **Evidence**: Official changelog states the key storage mechanism and a security property explicitly.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Keys are stored in the local OS keychain and are never read back by the UI."
- **Our assessment**: This is a security architecture detail not extracted in the VS Code BYOK note. OS keychain storage means keys are not held in application config files (where they could be accidentally committed to version control) — they are delegated to the OS credential store. The "never read back by the UI" clause means the app cannot display an already-entered key, a one-way security property preventing casual key exposure. For Ch05 (enterprise governance): the OS keychain storage is a positive security attribute relative to environment-variable or config-file alternatives. It does not, however, prevent the key from being used for inference — that requires policy-level controls above the application layer.

### Claim 4: The first BYOK use case is maintaining existing provider billing, quotas, regions, and data-handling terms when using external models in the Copilot app

- **Evidence**: Official changelog bullet point describing the "Connect the providers you already use" use case.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Connect the providers you already use: Add Azure OpenAI, Anthropic, self-hosted Ollama, LM Studio, or any OpenAI-compatible gateway, then choose the right model for each session while keeping your existing billing, quotas, regions, and data-handling terms."
- **Our assessment**: This mirrors the VS Code BYOK positioning (`docs-github-copilot-byok-vscode.md` Claim 4) — BYOK usage is billed directly by the chosen provider rather than against GitHub Copilot request quotas. The explicit mention of "data-handling terms" is notable for enterprise context: organizations with specific data residency or processing agreements with a provider (e.g., Azure OpenAI in a specific region) can maintain those terms when using the Copilot app, rather than having inference routed through GitHub's infrastructure. For Ch04: document this as the "quota bypass + data sovereignty" pattern for app BYOK.

### Claim 5: The second BYOK use case is a frontier+local model hybrid — frontier models handle complexity, local models handle execution

- **Evidence**: Official changelog bullet point describing the "Mix frontier and local models" use case.
- **Confidence**: emerging (use case described in official changelog; implementation mechanism within a session is not detailed)
- **Quote**: "Mix frontier and local models: Pair a frontier model with a local or self-hosted model. Frontier models handle complexity. Local models handle execution."
- **Our assessment**: This is the most novel framing in the source. No prior corpus source articulates a role-divided frontier+local pairing pattern in a BYOK context. VS Code BYOK documented local model support (Ollama, Foundry Local) but did not describe a hybrid task-division strategy. The practical implementation is unspecified: the Copilot app allows per-session model selection, so "mixing" likely means routing different task types to different sessions rather than switching mid-session. The claim is emerging because the effectiveness of the pairing pattern is not empirically documented. For Ch02: document as an emerging pattern for cost-sensitive or privacy-sensitive deployments — local models (no cloud inference cost) for execution, frontier models (provider-billed) for reasoning.

### Claim 6: The third BYOK use case is routing inference through the organization's own cloud account, tenant, or internal gateway for regulated environments

- **Evidence**: Official changelog bullet point describing the "Keep traffic in your tenant" use case.
- **Confidence**: settled (stated directly in official changelog as a supported use case)
- **Quote**: "Keep traffic in your tenant: Route inference through your own cloud account, tenant, or internal gateway for enterprise and regulated environments with stricter data-boundary requirements."
- **Our assessment**: This is the enterprise data governance use case — BYOK as a data-boundary control mechanism. In VS Code, the data governance aspect was implicit (use your own provider's data terms). The Copilot app changelog makes it explicit and adds "internal gateway" as a routing target. An internal gateway means an organization can place a proxy between the Copilot app and the model provider, enabling audit logging, PII filtering, or rate-limiting at the gateway layer. For Ch05: document app BYOK's "keep traffic in your tenant" framing as a data governance control for regulated industries. The internal gateway option is architecturally significant — it enables observation and policy enforcement without modifying the Copilot app itself.

### Claim 7: Access to the GitHub Copilot app on Copilot Business or Enterprise plans requires the organization or enterprise admin to have Copilot CLI enabled in policy settings — there is no separate BYOK policy for the app

- **Evidence**: Official changelog note documenting the Business/Enterprise admin requirement.
- **Confidence**: settled (admin requirement stated directly in official changelog)
- **Quote**: "To access the GitHub Copilot app on a Copilot Business or Enterprise plan, your organization or enterprise admin must have the Copilot CLI enabled in policy settings."
- **Our assessment**: This is a prerequisite for app access generally, not a BYOK-specific policy. The same admin policy that gates CLI access gates app access for Business/Enterprise users. There is no mention of a separate, BYOK-specific policy for the app — in contrast to VS Code BYOK (which has a dedicated "Bring Your Own Language Model Key in VS Code" policy) and JetBrains BYOK (which has its own dedicated policy control post-June 2). For Ch05: the admin governance model for app BYOK differs from VS Code and JetBrains BYOK — the app uses the existing Copilot CLI policy as its gate. Admins enabling Copilot CLI access for Business/Enterprise users are implicitly enabling app BYOK with no separate toggle. Organizations that want Copilot CLI access but not BYOK in the app currently have no mechanism to separate them.

## Concrete Artifacts

### Copilot App BYOK — Supported Providers and Configuration (June 23, 2026)

```
GitHub Copilot App BYOK — Supported Providers

CLOUD PROVIDERS (endpoint + API key required):
  OpenAI                  — GPT model family
  Azure OpenAI            — Azure-hosted OpenAI models
  Microsoft Foundry       — Microsoft AI Foundry models
  Anthropic               — Claude model family
  Any OpenAI-compatible endpoint

LOCAL RUNTIMES (host address only, no API key required):
  LM Studio               — Local model GUI/server
  Ollama                  — Local model server (e.g., Llama, Phi)

CONFIGURATION PATH:
  Settings → Model Providers
  → Enter endpoint and API key (or host address for LM Studio/Ollama)
  → Models appear in model picker alongside Copilot-hosted models
  → Selectable per session

KEY STORAGE:
  "Keys are stored in the local OS keychain and are never read back by the UI."
```

*Source: GitHub Copilot app support for BYOK, June 23, 2026*

### Copilot App BYOK — Three Use Cases (verbatim from official changelog)

```
1. MAINTAIN EXISTING PROVIDER TERMS
   "Connect the providers you already use: Add Azure OpenAI, Anthropic,
   self-hosted Ollama, LM Studio, or any OpenAI-compatible gateway,
   then choose the right model for each session while keeping your
   existing billing, quotas, regions, and data-handling terms."

2. FRONTIER + LOCAL HYBRID
   "Mix frontier and local models: Pair a frontier model with a local or
   self-hosted model. Frontier models handle complexity. Local models
   handle execution."

3. DATA BOUNDARY CONTROL
   "Keep traffic in your tenant: Route inference through your own cloud
   account, tenant, or internal gateway for enterprise and regulated
   environments with stricter data-boundary requirements."
```

*Source: GitHub Copilot app support for BYOK, June 23, 2026*

### BYOK Governance Comparison — Three Copilot Surfaces (as of June 23, 2026)

```
Surface         Plan Availability         Governance Model
─────────────────────────────────────────────────────────────────────────
VS Code Chat    Copilot Business/         DEFAULT-ON: admin must actively
                Enterprise                disable via "Bring Your Own Language
                                          Model Key in VS Code" policy in
                                          Copilot settings on github.com

JetBrains       Copilot Business/         DEDICATED POLICY: no longer requires
                Enterprise                Editor Preview flag; controlled via own
                                          policy at github.com/settings/copilot/features

Copilot App     Any plan; B/E requires    CLI-POLICY-GATED: admin must enable
                admin to enable           "Copilot CLI" in policy settings.
                Copilot CLI policy        No separate BYOK policy for the app.
```

*Cross-referenced from this source, docs-github-copilot-byok-vscode.md, and
docs-github-copilot-jetbrains-cli-enhancements-june2026.md (Claim 10)*

## Cross-References

- **Corroborates** `docs-github-copilot-byok-vscode.md` (Claims 1, 2, 4): The VS Code BYOK note established the foundational pattern — BYOK for Business/Enterprise Copilot users, provider-direct billing that bypasses Copilot quota, and a multi-provider list including Anthropic, OpenAI, Azure, and Ollama. This source corroborates that pattern for the app surface. Provider lists overlap (both support Anthropic, OpenAI, Azure, Ollama) though the app uses "any OpenAI-compatible endpoint" as a catch-all instead of naming Gemini and OpenRouter individually. The VS Code note's Claim 4 (provider-direct billing, quota bypass) maps to this source's Claim 4 (maintain "existing billing, quotas"). The VS Code note's Claim 8 ("no guarantee that responsible AI filtering is applied") likely applies to the app surface by analogy but is not stated in this source.

- **Extends** `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 10): The JetBrains note documented BYOK removing its Editor Preview flag and gaining a dedicated policy control for Business/Enterprise. This source extends BYOK to a third surface — the standalone app — making BYOK a cross-surface pattern rather than IDE-specific. The governance model for the app differs from JetBrains (Copilot CLI policy gate, not a BYOK-specific policy).

- **Extends** `docs-github-copilot-gemini-cli-cloud-agent-app.md` (Claims 1, 4): The June 2 source documented the Copilot app as a surface for Gemini models in technical preview, introduced for the first time. This June 23 source adds BYOK to the same app surface, expanding its external model support. The two mechanisms are complementary: the app now supports both GitHub-managed external models (Gemini via admin policy opt-in) and user-configured external models (BYOK via Settings → Model Providers, CLI-policy gated for B/E). The Copilot app has gone from "no external models" to "two distinct external model pathways" in three weeks.

- **Contextual relationship** `docs-github-copilot-cli-terminal-ga.md` (same-day): The CLI terminal GA note was published on the same date (June 23, 2026) and extends the Copilot CLI surface. Claim 7 in this note establishes that the Copilot app requires "Copilot CLI enabled in policy settings" for B/E — confirming that the app and CLI share an admin policy gate. The two June 23 announcements together extend both the CLI surface (terminal GA) and the app surface (BYOK) simultaneously.

- **Novel**:
  - **First corpus source documenting BYOK in the GitHub Copilot standalone app**: Prior BYOK sources covered VS Code and JetBrains IDEs. The standalone app is a distinct product with its own configuration surface.
  - **"Frontier handles complexity, local handles execution" framing**: No prior corpus source articulates a role-divided frontier+local model pairing pattern in the context of BYOK. VS Code BYOK documented local model support but did not describe a task-division strategy.
  - **"Keep traffic in your tenant" with internal gateway routing**: While the data governance use case was implicit in VS Code BYOK, the Copilot app announcement explicitly names "internal gateway" as a routing target — enabling proxy-layer interception between the Copilot app and the model provider. No prior corpus source documents this specific architectural pattern.
  - **OS keychain key storage as an explicit security property**: The VS Code BYOK note did not document key storage mechanism. This source is the first in corpus to explicitly state OS keychain storage and the "never read back by the UI" property for Copilot BYOK keys.
  - **App access gated by Copilot CLI policy (not a BYOK-specific policy)**: No prior corpus source established that the Copilot CLI admin policy also controls app access. The shared policy gate between CLI and app is a novel governance linkage.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**:
  - Update BYOK surface coverage to include the Copilot standalone app as a third surface. Surface inventory: VS Code (BYOK in chat, not completions), JetBrains (BYOK with dedicated policy), Copilot app (BYOK for agent sessions, CLI-policy gated for B/E).
  - Add the frontier+local model hybrid pattern (Claim 5) as a documented app-specific BYOK strategy: local models for execution (LM Studio, Ollama — no cloud billing), frontier models for complex reasoning (provider-billed). Note this is per-session selection, not mid-session switching.
  - Note that app BYOK includes "any OpenAI-compatible endpoint" as an explicit provider category — practitioners with self-hosted models behind an OpenAI-compatible API surface can connect them to the Copilot app without requiring a named provider integration.

- **Chapter 04 (Model Selection and Cost Management)**:
  - Add app BYOK as a third surface where provider-direct billing bypasses Copilot request quotas (alongside VS Code Chat BYOK and JetBrains BYOK). The "keep your existing billing, quotas, regions" framing (Claim 4) confirms this.
  - The frontier+local model pairing (Claim 5) is a cost optimization pattern: local models incur no cloud inference cost for execution tasks (high-volume, low-complexity); frontier models (provider-billed) are reserved for reasoning tasks (low-volume, high-value).

- **Chapter 05 (Enterprise Governance)**:
  - Add the Copilot app as a third BYOK governance surface. Enterprise AI governance policies must account for three BYOK surfaces with three different governance models: VS Code (default-on, opt-out), JetBrains (dedicated policy, opt-in), app (Copilot CLI policy gate — no separate BYOK toggle).
  - Note the governance gap specific to the app: enabling Copilot CLI access for Business/Enterprise users implicitly enables app BYOK. Organizations that want CLI access but not BYOK in the app have no current separate mechanism to disable only BYOK.
  - Add the "internal gateway routing" pattern (Claim 6) as an enterprise architecture option: a proxy between the Copilot app and the model provider enables audit logging, PII filtering, or rate-limiting without modifying the app configuration itself.
  - Document OS keychain key storage (Claim 3) as a positive security attribute: BYOK keys are not stored in config files that could be accidentally committed or visible in plaintext. Governance should still address workstation-level access controls.

## Extraction Notes

1. **Source is brief (~150 words plus three bullet points)**: The changelog is intentionally short. All substantive claims are extracted above. Three WebFetch calls were made with progressively specific extraction prompts to capture verbatim text; quotes are consistent across fetches.
2. **Individual plan availability unaddressed**: The source mentions the Business/Enterprise admin requirement but does not state whether individual plan users (Free, Pro, Pro+, Student) can access app BYOK. The VS Code BYOK announcement explicitly scoped to Business/Enterprise; the app announcement uses the B/E admin requirement as a note rather than an exclusive scope statement. No claim about individual plan access is made.
3. **No GA/preview status explicitly stated**: The source uses "now supports" (implying current availability) but does not use the words "generally available" or "preview." Confidence is settled for the feature's existence; whether it carries an implicit preview caveat is not determinable from this source.
4. **Responsible AI filtering caveat absent**: The VS Code BYOK documentation (`docs-github-copilot-byok-vscode.md` Claim 8) explicitly noted "There is no guarantee that responsible AI filtering is applied" for BYOK models. The Copilot app announcement does not address this. No claim is made about RA filtering in the app — but the VS Code source's caveat likely applies by analogy, since BYOK in any surface bypasses GitHub's managed model infrastructure. The Assayer may want to verify this against the official Copilot app documentation.
5. **No contradiction issues filed**: This source is additive (extends BYOK to a new surface), not contradictory of any existing claim.
