---
source_url: https://github.blog/changelog/2026-10-07-discover-local-models-in-github-copilot-cli
source_type: docs
title: "Discover local models in GitHub Copilot CLI"
author: GitHub (official changelog)
date_published: 2026-10-07
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: settled
issue: "#3978"
---

# Discover Local Models in GitHub Copilot CLI

> GitHub's Oct 7, 2026 changelog adds `/model` discovery of local Ollama models in Copilot CLI (1.0.94-0+) and explicitly states that a local model is not offline mode and does not disable telemetry — a data-egress caveat for the threat model.

## Source Context

- **Type**: docs (GitHub product changelog, ~1 minute read, labeled "Improvement")
- **Author credibility**: GitHub's own announcement of a shipped CLI feature. Authoritative for the discovery flow, prerequisites, and the offline/telemetry statement. Not authoritative for: which Ollama models qualify, what telemetry is collected, or how routing with local models will work.
- **Scope**: Ollama discovery in the CLI `/model` picker, prerequisites, error surfacing, the offline-mode caveat, and a pointer to an announced-but-unreleased routing feature. Does NOT cover LM Studio or other runtimes, enterprise policy interaction, or performance/quality of local models.

## Extracted Claims

### Claim 1: `/model` in Copilot CLI (1.0.94-0+) lists models from a running local Ollama instance next to configured and cloud models
- **Evidence**: Official changelog describing a shipped feature with a minimum CLI version.
- **Confidence**: settled
- **Quote**: "supported models from a running local Ollama instance"
- **Our assessment**: Moves local models from manual BYOK configuration (see `docs-github-copilot-byok-app.md` Claim 2, Settings → Model Providers) to zero-config discovery in the CLI picker. Only Ollama is named; other runtimes are not mentioned in this entry. The version floor (1.0.94-0) is a concrete detail practitioners can check.

### Claim 2: Discovery never auto-adds a model; the user reviews provider/endpoint and chooses to use it for the session or add it without switching
- **Evidence**: Described flow in the changelog (pick discovered model → review provider and endpoint → confirm).
- **Confidence**: settled
- **Quote**: "Discovery doesn’t automatically add models."
- **Our assessment**: A sensible human-in-the-loop gate: a local port that answers like Ollama cannot silently become the model receiving code context. The review of endpoint matters because the endpoint could be a non-local host. The two confirm options ("Add and use for this session" / "Add without switching") are as reported by the Prospector triage; the fetch tool summarized rather than reproduced them, so they are not quoted here.

### Claim 3: The new model is usable immediately, without restarting the CLI
- **Evidence**: Changelog statement.
- **Confidence**: settled
- **Quote**: "You can use the model in your current session without restarting the CLI."
- **Our assessment**: Minor UX point, but it supports mid-session model switching (cf. `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 3 on `/model` switching).

### Claim 4: The flow installs nothing — Ollama and the model must already be present
- **Evidence**: Changelog prerequisite statement.
- **Confidence**: settled
- **Quote**: "Ollama and the model must already be installed—this flow doesn’t install a runtime or download models."
- **Our assessment**: Setup remains the practitioner's job. Discovery is a pointer, not a provisioner.

### Claim 5: Local models must support tool calling and streaming
- **Evidence**: Changelog requirement; reflects the agent loop's dependence on tool use.
- **Confidence**: settled
- **Quote**: "Models must support tool calling and streaming."
- **Our assessment**: A practical filter: many small or older local models lack reliable tool calling and won't appear or won't work as agents. Consistent with the local-model viability concerns in `blog-fowler-boeckeler-local-models-viability.md` and `blog-ronacher-local-models-focus-polish.md` (cited by topic; no claim numbers asserted).

### Claim 6: Provider connection failures are surfaced in the picker with an explanation
- **Evidence**: Changelog statement.
- **Confidence**: settled
- **Quote**: "Provider connection failures appear in the picker with an explanation, helping you identify what needs attention."
- **Our assessment**: Minor; failure diagnosis is in-band rather than a silent missing entry.

### Claim 7: Choosing a local model does not enable offline mode or disable GitHub telemetry
- **Evidence**: Explicit caveat in the changelog.
- **Confidence**: settled
- **Quote**: "Choosing a local model doesn’t turn on offline mode or disable GitHub telemetry."
- **Our assessment**: The key contribution. "Local inference" and "no egress" are separate properties. Corroborates the VS Code finding in `docs-github-copilot-byok-vscode.md` Claim 7 (local models still need the Copilot service) for a different surface, the CLI. Teams adopting local models for privacy must configure offline behavior separately.

### Claim 8: Offline mode is an explicit `COPILOT_OFFLINE=true` setting, and remote providers can still receive prompts and code context even then
- **Evidence**: Changelog statement per the fetched summary (not verbatim-quotable; the fetch tool paraphrased this part).
- **Confidence**: settled
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The changelog says offline mode requires setting `COPILOT_OFFLINE=true` and that a remote provider configured in the CLI still receives prompts and code context over the network. So offline mode governs GitHub-side connectivity, not where a configured provider lives. A threat-model check should therefore list every configured provider endpoint, not just whether a local model is selected. Verify exact wording against the live page before the Smith quotes it.

### Claim 9: Intelligent routing with local models is announced but not yet available here
- **Evidence**: One-line announcement; details deferred to the Microsoft Command Line blog.
- **Confidence**: anecdotal (announcement only, no mechanism)
- **Quote**: "We’re also announcing intelligent routing with local models."
- **Our assessment**: Would extend the frontier+local hybrid idea in `docs-github-copilot-byok-app.md` Claim 5 and Auto routing in `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 1. Nothing to act on until details exist.

## Concrete Artifacts

```
Source: changelog entry, 2026-10-07 (fetched summary; only the quoted strings above are verbatim)
Minimum CLI version: 1.0.94-0
Command: /model
Env var for offline mode: COPILOT_OFFLINE=true
Confirm options (per Prospector triage): "Add and use for this session" | "Add without switching"
Requirements: Ollama running; model pre-installed; tool calling + streaming support
```

## Cross-References

- **Corroborates**: `docs-github-copilot-byok-vscode.md` Claim 7 (local models still involve the Copilot service); `docs-github-copilot-byok-app.md` Claim 1 (Ollama among supported providers).
- **Contradicts**: None found. (The "Copilot service still required" statements in VS Code docs and this entry's "not offline by default" are consistent, though this entry shows an explicit `COPILOT_OFFLINE` option exists in the CLI.)
- **Extends**: `docs-github-copilot-byok-app.md` Claim 2 and Claim 5 (manual provider config and frontier+local hybrid → CLI auto-discovery); `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` Claim 3 (`/model` switching).
- **Novel**: CLI `/model` Ollama discovery flow; the `COPILOT_OFFLINE=true` setting; the explicit statement that local model ≠ offline ≠ telemetry-off.

## Guide Impact

- **Chapter 02**: When describing local/BYOK model options for Copilot CLI, add `/model` Ollama discovery (CLI 1.0.94-0+) and its prerequisites (pre-installed, tool calling, streaming).
- **Chapter 06**: Add a threat-model caveat: selecting a local model does not stop telemetry or prompt egress; offline mode is a separate explicit setting and does not stop a configured remote provider from receiving code context. Audit configured provider endpoints.

## Extraction Notes

- Read the single changelog page; linked docs (CLI provider setup, offline mode) and the Microsoft Command Line blog were not followed. The offline-mode docs would be the best follow-up for exact telemetry semantics.
- The fetch tool returned summaries; quotes were obtained via a second targeted fetch for exact sentences. Claim 8 has no verbatim quote for that reason.
- Entry is short; 9 claims is near the ceiling of what it supports.
