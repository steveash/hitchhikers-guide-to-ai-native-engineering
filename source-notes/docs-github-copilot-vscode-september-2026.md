---
source_url: https://github.blog/changelog/2026-10-01-github-copilot-in-vs-code-september-2026-releases
source_type: docs
title: "GitHub Copilot in VS Code, September 2026 releases"
author: GitHub (official changelog)
date_published: 2026-10-01
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: settled
issue: "#3854"
---

# GitHub Copilot in VS Code, September 2026 Releases

> GitHub's October 1, 2026 monthly VS Code roundup (v1.136–v1.140) extends the Agents window from implementation through pull request merge: scheduled automations, an "agent merge" mode that handles review feedback, failed checks and conflicts, a model-orchestrating HydraFusion picker entry, Dev Container sessions, and session-hygiene features — most of them in preview.

## Source Context

- **Type**: docs (GitHub official product changelog, "2 minute read" monthly roundup covering VS Code v1.136 through v1.140, in three sections: Agents window, Workspaces and environments, Chat and integrations).
- **Author credibility**: GitHub's Copilot product team. Authoritative for the existence and naming of features and their preview status. Not a source for adoption, effectiveness, or quality data; the page has no metrics, code, or settings names.
- **Scope**: One-sentence-per-feature summaries; details are deferred to the linked VS Code 1.136–1.140 release notes, which this note did not read. Related-post links on the page (HydraFusion, Dynamic workflows in Copilot CLI and the Copilot app, computer use) were not followed.

## Extracted Claims

### Claim 1: HydraFusion lets Copilot choose models and workflows automatically for a coding task (research preview)
- **Evidence**: Vendor announcement; no benchmark or routing details on this page (a separate Sep 30 changelog post is linked).
- **Confidence**: anecdotal
- **Quote**: "If eligible, enable preview features and select HydraFusion in the model picker to choose models and workflows for your coding tasks automatically. This feature is in research preview."
- **Our assessment**: Notable because it picks workflows, not just models, so it goes beyond Auto model selection. Gated by eligibility and preview flags, with no evidence of quality yet. Treat as a direction, not a recommendation.

### Claim 2: Automations run agent tasks on an hourly, daily, or weekly schedule, or on demand
- **Evidence**: Vendor feature description; preview.
- **Confidence**: emerging
- **Quote**: "Use automations to run tasks on an hourly, daily, or weekly schedule or run them on demand. Start from a template or use your own prompt. This feature is in preview."
- **Our assessment**: Brings scheduled/recurring agent work into the editor. Scheduling is already a theme elsewhere in the corpus; the page says nothing about permissions, failure handling, or cost for unattended runs.

### Claim 3: "Agent merge" has the agent drive a PR to mergeable state (review feedback, failed checks, conflicts, workflow reruns)
- **Evidence**: Vendor feature description; preview.
- **Confidence**: emerging
- **Quote**: "Enable agent merge in an active session to let the agent handle review feedback, failed checks, merge conflicts, and workflow reruns."
- **Our assessment**: Extends the agent loop past code generation into the CI/review feedback loop. The page does not say whether human approval remains required to merge, which matters for guide advice on review gates.

### Claim 4: Pull requests can be created from Copilot, Claude, or Codex agent sessions via a form in the Agents window
- **Evidence**: Vendor feature description (general, non-preview wording).
- **Confidence**: settled
- **Quote**: "Open the pull request form from a Copilot, Claude, or Codex agent session in the Agents window to review and edit the title and description, choose draft and merge options, and create the pull request."
- **Our assessment**: A multi-vendor agent host with a uniform PR hand-off is a concrete example of agent-agnostic tooling. A human reviews the title and description before creation.

### Claim 5: Agents can now decide to create new chats or sessions, shown in a hierarchical session list
- **Evidence**: Vendor feature description.
- **Confidence**: emerging
- **Quote**: "Agents can now decide to create new chats or sessions."
- **Our assessment**: Agent-initiated spawning of sessions (not just subagents) is a shift in who controls session topology. Builds on user-initiated multi-chat sessions in the July release.

### Claim 6: Completed-session housekeeping and attention signals are now product features
- **Evidence**: Vendor feature descriptions; both preview.
- **Confidence**: anecdotal
- **Quote**: "Use Mark as Done suggestions after a session’s pull requests merge, or configure automatic cleanup to keep your session list manageable."
- **Our assessment**: Session sprawl is an implicit admission of the cost of running many parallel agents. The companion application badge ("surface new results, input requests, and pull request checks on your dock, launcher, or taskbar") is the notification side of the same problem.

### Claim 7: Agent sessions can run in Dev Containers, including over SSH, Tunnel, and WSL
- **Evidence**: Vendor feature description.
- **Confidence**: settled
- **Quote**: "Select Use Dev Container from a local or remote folder’s menu to run an agent session with your project’s configured tools and dependencies, including on SSH, Tunnel, and WSL hosts."
- **Our assessment**: Reuses the repo's existing environment definition as the agent's execution environment, so tools and dependencies come from the project rather than the developer's host.

### Claim 8: Chats can start without a workspace and attach a folder later; Codex conversations can be continued from the ChatGPT app
- **Evidence**: Vendor feature descriptions.
- **Confidence**: emerging
- **Quote**: "Start a general Copilot chat without a workspace, then attach a local folder when you want to make the conversation specific to that project."
- **Our assessment**: The second feature ("Pick up a Codex conversation from the ChatGPT app in VS Code and start working on your codebase without copying and pasting context or files") continues the cross-application session continuity seen in August.

### Claim 9: Messages from an agent no longer interrupt the active turn of an ongoing chat
- **Evidence**: Vendor feature description; a UX fix related to claim 5.
- **Confidence**: anecdotal
- **Quote**: "When an agent sends a message to an ongoing chat, it no longer interrupts the active turn."
- **Our assessment**: Implies agent-to-chat messaging is common enough to need an interruption policy. Minor on its own.

### Claim 10: GitHub issues and PRs can be attached as context to any chat
- **Evidence**: Vendor feature description.
- **Confidence**: settled
- **Quote**: "Add a GitHub issue or pull request from Add Context, or paste its URL into the new-session input."
- **Our assessment**: Tickets become first-class context inputs, supporting the practice of well-specified issues as the unit of agent work.

## Concrete Artifacts

```
Release scope (source): "This changelog covers VS Code v1.136 through v1.140, shipped throughout September 2026."
Preview-labelled features: HydraFusion (research preview), automations, agent merge, Mark as Done / auto cleanup, application badge.
Theme line (source): "September’s releases streamline agent-driven development from implementation through pull request merge."
```

## Cross-References

- **Corroborates**: `docs-github-copilot-vscode-august-2026.md` Claim 5 (continuing sessions started in other applications) — Codex continuation from the ChatGPT app is the same direction.
- **Contradicts**: none found.
- **Extends**: `docs-github-copilot-vscode-july-2026.md` Claim 3 (multiple related chats in one session) and Claim 5 (quick chat without a workspace) — September lets agents create chats/sessions and attach a workspace to a quick chat later. Also Claim 6 of the July note (CI failures/review comments surfaced in the Agents window), which agent merge now acts on automatically.
- **Related**: `docs-github-copilot-vscode-auto-model-selection.md` (HydraFusion is a more ambitious routing layer); `docs-github-copilot-computer-use-desktop-apps.md` and `blog-anthropic-dynamic-workflows-claude-code.md` (same-week adjacent announcements, not read for this note); `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (scheduling in the CLI).
- **Novel**: Agent merge, in-editor automations, agent-initiated sessions, and Dev Container agent sessions are not covered by existing VS Code notes.

## Guide Impact

- **Chapter 06 (tooling & agents)**: Update the Copilot VS Code timeline with the September entry: the Agents window now spans implementation → PR creation → agent-driven merge, with automations for recurring work. Mark most items as preview.
- **Chapter 04 (patterns & practices)**: Candidate example for "close the CI/review feedback loop with the agent" (agent merge), with the caveat that the source does not state human approval gates.
- **Chapter 06**: Note that HydraFusion is a research-preview workflow/model router; revisit when an evidence-bearing source appears.

## Extraction Notes

- Read the full changelog page (short, ~2 minutes). Did not follow the linked VS Code 1.136–1.140 release notes, so setting names, defaults, and limits are not captured.
- Triage comments assigned inconsistent chapter numbers; chapters above reflect the content.
- Confidence "settled" applies to the existence of the announced features, not their effectiveness.
