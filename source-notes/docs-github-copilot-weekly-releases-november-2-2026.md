---
source_url: https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2
source_type: docs
title: "GitHub Copilot weekly releases — November 2"
author: GitHub (official changelog)
date_published: 2026-11-06
date_extracted: 2026-11-07
last_checked: 2026-11-07
status: current
confidence_overall: emerging
issue: "#4568"
---

# GitHub Copilot weekly releases — November 2

> A thin vendor digest that records Agent Merge staying armed while checks are pending, opt-in personal instructions for assisted approval, cron-scheduled local automations in VS Code 1.145, and two new Copilot surfaces (JetBrains Air, Xcode).

## Source Context

- **Type**: docs (official changelog weekly digest, 2-minute read)
- **Author credibility**: GitHub's own changelog; authoritative on what shipped, but it gives no evidence on effectiveness.
- **Scope**: Five sections (Copilot app, CLI, JetBrains, Xcode, VS Code 1.145), one to five one-line bullets each. No metrics, config examples, or design rationale. Followed the two linked changelog pages (Xcode, JetBrains Air) for detail; the VS Code 1.145 release notes were not fetched.

## Extracted Claims

### Claim 1: Agent Merge now stays enabled while required checks or rules are pending
- **Evidence**: Vendor release statement; no demo or metrics.
- **Confidence**: anecdotal
- **Quote**: "It now stays enabled while required checks or rules are pending."
- **Our assessment**: A verification gate: the merge is conditional on repository checks, not on the agent's own judgment. Behavior on check failure isn't described here. Fits existing coverage of Agent Merge; adds only the persistence behavior.

### Claim 2: Users can write personal instructions that guide which tool requests the agent approves without asking
- **Evidence**: One-line release note.
- **Confidence**: anecdotal
- **Quote**: "Personal instructions for assisted approval are opt-in and apply to local sessions."
- **Our assessment**: Extends LLM-classified assisted permissions with a user-authored policy layer (natural-language rules for the approver). Whether instructions can loosen the built-in "clearly safe" threshold is not stated; that is the key security question.

### Claim 3: Copilot app sessions that hit the context limit can be compacted or inspected from the error itself
- **Evidence**: Release note only.
- **Confidence**: anecdotal
- **Quote**: "Compact the conversation or review what’s using the available space directly from the error."
- **Our assessment**: Surfacing context-consumption breakdown at the failure point is a small but useful context-management UX. No detail on what is shown.

### Claim 4: VS Code 1.145 local automations support cron expressions and workspace custom agents
- **Evidence**: Release note; links to VS Code 1.145 notes.
- **Confidence**: anecdotal
- **Quote**: "Local automations now support cron expressions and custom agents from your workspace."
- **Our assessment**: Scheduled agent runs with a workspace-defined agent move from fixed hourly/daily/weekly schedules to arbitrary schedules. Note "local": it runs on the developer's machine, unlike shared repo-level automations.

### Claim 5: Copilot in Xcode's built-in coding assistant is in public preview from Xcode 27.3 beta
- **Evidence**: Digest plus the linked Nov 4 changelog: requires macOS Tahoe 26.6+, set up via Xcode > Settings > Intelligence, all Copilot plans supported.
- **Confidence**: settled (that it shipped); the capabilities are undocumented.
- **Quote**: "The integration is now in public preview, available starting with Xcode 27.3 beta."
- **Our assessment**: Surface expansion. The linked page doesn't say whether it runs agent sessions or only inline assistance, so don't claim agentic capability. It states the existing extension "remains a separate option".

### Claim 6: Copilot in JetBrains Air supports local and cloud tasks on an existing Copilot subscription
- **Evidence**: Digest plus the linked Nov 3 changelog (ACP-based; cloud tasks run in a Docker container on a fresh VM, traffic through a proxy, no state carried between tasks).
- **Confidence**: emerging
- **Quote**: "Track multiple agent sessions and run tasks locally in your JetBrains IDE or in the cloud through Air Teams, using your existing Copilot subscription."
- **Our assessment**: Confirms the pattern that IDEs act as conduits for agents users already pay for (ACP), and gives a concrete cloud-sandbox description (ephemeral VM, proxied traffic).

### Claim 7: Copilot CLI `/settings` is now a unified dashboard for plugins, MCP servers, and more, with search
- **Evidence**: Release note.
- **Confidence**: anecdotal
- **Quote**: "/settings now opens a unified dashboard for your plugins, MCP servers, and more, and you can search across all of your settings."
- **Our assessment**: Extends the earlier `/settings` consolidation to harness components (plugins, MCP). Harness configuration is being centralized into one inspectable surface.

### Claim 8: VS Code adds experimental chat view modes and remote-app previews for checking agent work
- **Evidence**: Release notes.
- **Confidence**: anecdotal
- **Quote**: "Experimental chat view modes let you collapse or expand reasoning and tool calls without starting a new conversation."
- **Our assessment**: Reflects the observability trade-off between clutter and step-by-step inspection. Also "Preview remote apps and use interactive canvases in the Agents window, now in preview": verifying agent work on another machine.

## Concrete Artifacts

No code or config. Key fragments:

```
Agent Merge: "stays enabled while required checks or rules are pending"
Assisted approval: personal instructions, opt-in, local sessions only
VS Code 1.145: local automations = cron expressions + workspace custom agents
Xcode: public preview, Xcode 27.3 beta, macOS Tahoe 26.6+, Settings > Intelligence
Air cloud task: Docker container on fresh VM, proxy for all traffic, no state between tasks
(Source: digest and linked Nov 3 / Nov 4 changelog pages)
```

## Cross-References

- **Corroborates**: `docs-github-copilot-vscode-september-2026.md` Claim 3 (Agent Merge) and Claim 2 (scheduled automations); `blog-jetbrains-air-in-ides-eap.md` Claim 5 (Air plugin as conduit for existing subscriptions).
- **Contradicts**: None found.
- **Extends**: `docs-github-copilot-assisted-permissions-ga.md` Claim 1 (LLM-classified approvals; this adds a user-authored instruction layer); `docs-github-copilot-cli-settings-command.md` Claim 1 (`/settings`); `docs-github-copilot-shared-automations.md` (shared repo-level automations; this is the local, cron-scheduled counterpart); `docs-github-copilot-weekly-releases-sept21-2026.md` (prior digest in the series).
- **Novel**: Copilot in Xcode's coding assistant; cron expressions for local automations; Agent Merge persistence while checks are pending; Copilot-in-Air cloud sandbox description.

## Guide Impact

- **Chapter 02**: Assisted-approval guidance can note that Copilot now allows opt-in user-written approval instructions (local sessions only); flag as unverified how they interact with the safety classifier.
- **Chapter 03**: Agent Merge persisting while required checks/rules are pending is an example of delegating the merge decision to repository gates; cite as vendor-stated only.
- **Chapter 01 / surface landscape**: Add Xcode (public preview) and JetBrains Air to the list of Copilot surfaces; state that agentic capability in Xcode is undocumented.
- **Scheduled automations**: cite cron support in VS Code 1.145 local automations as an example of schedule-driven agents.

## Extraction Notes

Read the full digest and followed the two linked changelog pages (Xcode, JetBrains Air). Did not read VS Code 1.145 release notes; the cron/custom-agent detail is from the digest only. The digest is thin and the claims are mostly vendor release statements, hence low evidence grades. Skipped generic UX items (CSV/TSV viewer, My Work views) per triage guidance. No contradictions found, so none filed.
