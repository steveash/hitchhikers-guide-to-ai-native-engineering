---
source_url: https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases
source_type: docs
title: "GitHub Copilot in VS Code, Universe releases"
author: GitHub (official changelog)
date_published: 2026-10-28
date_extracted: 2026-10-30
last_checked: 2026-10-30
status: current
confidence_overall: settled
issue: "#4431"
---

# GitHub Copilot in VS Code, Universe releases

> GitHub's Universe 2026 VS Code roundup turns the Agent Host and Agent Host Protocol into shipped cross-client session continuity (cloud, remote, phone), makes the Copilot SDK-based harness the default, and adds preview connectors and marketplace controls.

## Source Context

- **Type**: docs (vendor changelog roundup; 4-minute read)
- **Author credibility**: GitHub's official changelog; first-party statements about its own product. No independent measurements.
- **Scope**: Feature announcements only: cloud sessions, Agent Host, phone control, default harness, Copilot CLI install, model comparison, computer use, AHP, marketplace, plugin controls, connectors. No metrics, no failure data, no configuration beyond a few settings/commands. Maturity labels (preview/experimental) matter and are recorded per claim.

## Extracted Claims

### Claim 1: Cloud agent sessions run on GitHub infrastructure and can be continued across VS Code, the Copilot app, GitHub Mobile, github.com, and Copilot CLI
- **Evidence**: Vendor feature description; no demo or metrics.
- **Confidence**: settled (product fact; GA status not explicitly stated)
- **Quote**: "The work runs on GitHub’s infrastructure, so closing your laptop doesn’t stop it."
- **Our assessment**: Session continuity across clients is the headline. Also stated: "Sessions started in a Slack or Microsoft Teams DM can also be continued in these clients." This makes the session, not the client, the unit of work, a shift for Ch01 workflows.

### Claim 2: The Agent Host decouples Copilot sessions from individual VS Code windows
- **Evidence**: Vendor feature description.
- **Confidence**: settled
- **Quote**: "The new Agent Host isolates your Copilot sessions from individual VS Code windows, so work continues in the background after you close the project folder or window."
- **Our assessment**: Moves the agent process lifecycle out of the editor. Follows the August "connect windows to the same session" feature (see Cross-References). Practitioners should treat sessions as long-lived background processes.

### Claim 3: Agents can run on a separate machine via Remote SSH and dev tunnels, but the remote machine and its Agent Host must stay running
- **Evidence**: Vendor description.
- **Confidence**: settled
- **Quote**: "The remote machine and its Agent Host must remain running."
- **Our assessment**: An honest durability caveat: the remote agent survives client disconnect ("can keep running when you disconnect or quit VS Code locally") but not host shutdown. Persistence is a property of the host, not the cloud.

### Claim 4: A phone (GitHub Mobile) can control an agent running on your own development machine
- **Evidence**: A single command is given; no security discussion on the page.
- **Confidence**: settled (feature), emerging (practical maturity)
- **Quote**: "Your phone provides the controls, and the agent does the work on your development machine."
- **Our assessment**: Distinct from cloud sessions (Claim 1): execution stays local with local tools and credentials. The remote-control surface needs governance; see `docs-github-copilot-cli-remote-control-managed-devices.md`, which covers the `remoteControl` managed setting. This page does not mention it.

### Claim 5: The Copilot harness, built on the Microsoft Copilot SDK, is now the default for new sessions in the editor and Agents window
- **Evidence**: Vendor statement; motivation is consistency across VS Code, Copilot CLI, and the Copilot app.
- **Confidence**: settled
- **Quote**: "The Copilot harness, built on the Microsoft Copilot SDK, is now the default for new sessions in both the editor and the Agents window."
- **Our assessment**: Names a shared SDK underneath the clients as the mechanism for behavioral consistency, a harness-engineering point for Ch02. The consistency claim is unmeasured.

### Claim 6: The Agent Host Protocol (AHP) is open and lets third-party clients attach to the same live sessions, with catch-up after reconnect
- **Evidence**: Description plus a list of client libraries.
- **Confidence**: settled (exists); emerging (adoption)
- **Quote**: "The open Agent Host Protocol (AHP) lets connected clients stay in sync and catch up after reconnecting."
- **Our assessment**: Realizes the cross-client interoperability layer the May note described as in progress. Libraries are listed for "TypeScript, Rust, Go, Kotlin, or Swift"; connection starts with `code agent host`. No spec link or third-party adopters are named here.

### Claim 7: Computer use is experimental, enabled by a setting plus `/computer on`, requires per-application approval, and can be disabled by organization policy
- **Evidence**: Setting name and command given.
- **Confidence**: settled (product facts)
- **Quote**: "Each application requires your approval."
- **Our assessment**: Consistent with `docs-github-copilot-computer-use-desktop-apps.md`; this adds the VS Code entry point (`chat.agentHost.computerUse.enabled`, macOS/Windows) and that the setup is shared with CLI and the app so macOS permissions are granted once. The page labels it "an experimental feature", whereas the earlier note says public preview in CLI and app.

### Claim 8: Copilot connectors bring Slack, Notion, and Microsoft Learn context into sessions without an MCP server (preview)
- **Evidence**: Vendor description.
- **Confidence**: emerging (preview)
- **Quote**: "Bring context from services such as Slack, Notion, and Microsoft Learn into agent sessions without installing or managing an MCP server."
- **Our assessment**: A vendor-managed alternative to MCP for context integrations. Connections are reusable "across supported Copilot clients signed in with the same account" and work only "with the Copilot harness". Business and Enterprise admins must allow Editor preview features. Tradeoffs versus MCP (portability, auditability) are not discussed.

### Claim 9: Plugin and marketplace controls are policy-enforceable, while repo-level `.github/copilot/settings.json` only sets defaults
- **Evidence**: Vendor description.
- **Confidence**: settled
- **Quote**: "These are defaults, not enforcement: contributors can turn plugins off unless enterprise policy requires them."
- **Our assessment**: A clear enforcement/default split for Ch05/Ch06. Admins can "require or block named plugins, add marketplaces, and restrict installation to approved sources". Repo files recommend and org policy enforces.

### Claim 10: A Customization Marketplace (preview, on by default) unifies skills, MCP servers, plugins, and other customizations in a "Browse" page
- **Evidence**: Vendor description.
- **Confidence**: emerging (preview)
- **Quote**: "The Customization Marketplace is in preview and enabled by default."
- **Our assessment**: On by default for a supply-chain-relevant surface; Business/Enterprise admins must still allow Editor preview features. Pair with Claim 9.

### Claim 11: Models and harnesses can be run in parallel and compared side by side, with a Judge model and a Synthesize option (preview)
- **Evidence**: Vendor description.
- **Confidence**: emerging (preview)
- **Quote**: "You can ask a Judge model to recommend a solution and choose Synthesize to combine ideas from the other attempts."
- **Our assessment**: Continues the Judge/Synthesize pattern from the May note. No evidence on quality.

### Claim 12: Copilot CLI installs via the VS Code installer
- **Evidence**: Vendor description.
- **Confidence**: settled
- **Quote**: "Install GitHub Copilot CLI through the VS Code installer on Windows, when adding VS Code to your path on macOS, or by running copilot on Linux."
- **Our assessment**: Minor onboarding change; supports the "one harness, several surfaces" theme.

## Concrete Artifacts

```
# Source: GitHub changelog, 2026-10-28
code agent host --github-environment   # run in project folder; enables GitHub Mobile control
code agent host                        # run, then connect an AHP client library
chat.agentHost.computerUse.enabled     # VS Code setting (macOS/Windows), restart, then:
/computer on                           # in a Copilot session on your computer
.github/copilot/settings.json          # repo-level plugin marketplaces and default plugins (defaults only)
Chat: Open Customizations              # command palette entry for the Customizations editor
```

## Cross-References

- **Corroborates**: `docs-github-copilot-vscode-may-2026.md` Claim 2 (remote agents over SSH/Dev Tunnels that continue when the client disconnects) and Claim 3 (AHP). `docs-github-copilot-computer-use-desktop-apps.md` Claim 4 (approval before control) and Claim 6 (org disable).
- **Contradicts**: None found. (Minor labeling difference on computer use: "experimental" here versus "public preview" in the earlier note's CLI/app context.)
- **Extends**: `docs-github-copilot-vscode-august-2026.md` Claim 6 (Agent Host connects multiple windows) to cloud, remote, mobile, and third-party clients. `docs-github-copilot-vscode-september-2026.md` Claim 7 (agent sessions on Dev Containers over SSH/Tunnel/WSL). `docs-github-copilot-cli-remote-control-managed-devices.md` (governance for the remote control this page enables).
- **Novel**: Copilot connectors as a non-MCP integration path; Copilot SDK-based harness as the default; AHP client libraries in five languages; Slack/Teams-originated cloud sessions; the `code agent host --github-environment` phone flow.

## Guide Impact

- **Chapter 02**: Add the Agent Host/AHP architecture (session decoupled from window; cross-client attach) and the Copilot-SDK default harness as a harness-consistency example, citing this note with May Claim 3.
- **Chapter 01**: Note the three continuity modes (cloud, remote host, local host driven by phone) and their durability caveats (Claim 3).
- **Chapter 06**: Add the computer-use approval/policy-disable controls and the phone-to-local-machine control surface as attack surface; link to the managed-devices note.
- **Chapter 05**: Use Claim 9's defaults-versus-enforcement split for team plugin adoption.

## Extraction Notes

Read the full changelog page (all 12 sections). The page links to the VS Code release notes, an Agent Host deep dive, and a computer-use doc; these were not followed, so details such as AHP's spec and security model are absent. Preview/experimental status is recorded per claim. Cross-reference claim numbers were verified against the cited notes' headings.
