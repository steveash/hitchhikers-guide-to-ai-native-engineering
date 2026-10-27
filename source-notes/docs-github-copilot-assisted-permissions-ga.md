---
source_url: https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available
source_type: docs
title: "GitHub Copilot assisted permissions generally available"
author: GitHub (official changelog; byline "Allison")
date_published: 2026-10-26
date_extracted: 2026-10-27
last_checked: 2026-10-27
status: current
confidence_overall: emerging
issue: "#4360"
---

# GitHub Copilot Assisted Permissions Generally Available

> GitHub ships an LLM-classifier-gated "Assisted" permission mode to GA across Copilot CLI, the Copilot app, and VS Code, with enterprise policy controls — a second vendor adopting the pattern described in Anthropic's Claude Code auto mode, though with no classifier details or metrics.

## Source Context

- **Type**: docs (GitHub changelog entry, ~1 minute read, GA announcement)
- **Author credibility**: GitHub's official changelog. Authoritative for the existence, surfaces, and enterprise policy behavior of the feature; not a source for classifier design, accuracy, or injection resistance.
- **Scope**: One-paragraph mechanism description, three UI paths (not extracted), and an "Enterprise controls" section. It defers the evaluation details to a docs page ("Allowing safe commands to run without manual approval"), which was not followed. No metrics, failure cases, config keys, or policy schema.

## Extracted Claims

### Claim 1: Assisted permissions uses an LLM to classify each permission request and auto-proceeds only on "clearly safe"
- **Evidence**: Official changelog mechanism description; no accuracy data.
- **Confidence**: emerging
- **Quote**: "Requests classified as clearly safe automatically proceed. Other requests require your approval."
- **Our assessment**: Same classify-then-approve split as Claude Code auto mode, but the default for anything not clearly safe is human approval (escalate), rather than Anthropic's deny-and-continue. The changelog does not say what the classifier sees (e.g. tool output, assistant reasoning), so the prompt-injection question raised in triage is unanswered here.

### Claim 2: The classified request types are commands, file system paths, and URLs
- **Evidence**: Changelog text.
- **Confidence**: emerging
- **Quote**: "When Copilot requests permission to run a command, access a file system path, or open a URL, a large language model evaluates the request."
- **Our assessment**: Mirrors the shell/file/network selector families in the managed deny/ask/allow rules (see `docs-github-copilot-enterprise-agent-operations-permissions.md`). Whether the classifier evaluates the same operations those rules govern, and how rules interact with Assisted, is not stated.

### Claim 3: It is GA on three surfaces
- **Evidence**: Changelog headline sentence.
- **Confidence**: settled
- **Quote**: "Assisted permissions are now generally available in GitHub Copilot CLI, GitHub Copilot app, and Visual Studio Code."
- **Our assessment**: Notably not JetBrains or the cloud agent, consistent with the client-support gaps in the managed-permissions note.

### Claim 4: Admins can block Allow All while keeping Assisted, or disable Assisted separately
- **Evidence**: Changelog "Enterprise controls" section.
- **Confidence**: settled
- **Quote**: "you can use enterprise-managed settings to block Allow All while keeping Assisted available or disable Assisted separately."
- **Our assessment**: This makes the classifier mode a policy-addressable middle tier between manual approval and full bypass — an explicit governance ladder. It extends the `disableBypassPermissionsMode` lever (`docs-github-copilot-enterprise-bypass-permissions.md` Claim 1). Setting key names are not given.

### Claim 5: Admins set the default mode for new sessions; prohibited defaults fall back to manual approval
- **Evidence**: Changelog text.
- **Confidence**: settled
- **Quote**: "If the default is unavailable or prohibited by policy, the session starts with manual approval."
- **Our assessment**: A fail-closed fallback — a sound policy-design detail. Developers retain choice within policy: "Developers can still select another mode permitted by policy."

## Concrete Artifacts

```
Enable (UI paths, per changelog):
  Copilot CLI:  /permissions  -> select "assisted"
  Copilot app:  mode picker -> Tool permissions -> Assisted
  VS Code:      permissions picker -> Assisted permissions
(Source: GitHub changelog, 2026-10-26)
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-code-auto-mode.md` — Claim 9 (three-tier permission structure with classifier-evaluated tier) and Claim 1 (manual approval prompts are low-value, motivating classifier gating); second vendor shipping the pattern to GA.
- **Contradicts**: None found.
- **Extends**: `docs-github-copilot-enterprise-bypass-permissions.md` Claim 1 (bypass control) and `docs-github-copilot-enterprise-agent-operations-permissions.md` Claim 1 (centrally managed permissions) with a classifier-based tier and default-mode policy.
- **Novel**: Default-permission-mode policy with fail-closed fallback to manual approval; independently disabling the classifier tier.

## Guide Impact

- **Chapter 02**: Where permission modes are discussed, add Copilot "Assisted" as a second shipped example of classifier-gated approval alongside Claude Code auto mode (cite this note and the auto-mode note).
- **Chapter 06**: In policy-managed agent permissions, note the admin ladder (manual / Assisted / Allow All) and fail-closed default; flag that vendor docs here disclose no classifier inputs or injection testing, unlike Anthropic's published numbers.

## Extraction Notes

- Read the full changelog (it is short). Did not follow the linked "Allowing safe commands to run without manual approval" docs page, which holds the evaluation details; a follow-up could mine it.
- Prospector asked to skip UI steps; only recorded as a brief artifact. Evidence is thin; confidence capped at emerging.
