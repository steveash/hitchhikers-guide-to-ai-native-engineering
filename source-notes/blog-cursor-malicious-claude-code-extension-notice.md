---
source_url: https://cursor.com/blog/claude-code-extension-security-notice
source_type: blog-post
title: "Security notice — malicious version of Anthropic.claude-code (2.1.312 and 2.1.313) identified in the Cursor VS Code Extension Marketplace"
author: Cursor Team (Cursor)
date_published: 2026-10-29
date_extracted: 2026-10-31
last_checked: 2026-10-31
status: current
confidence_overall: emerging
issue: "#4453"
---

# Security notice — malicious Anthropic.claude-code builds in the Cursor extension marketplace

> A vendor incident notice showing that a name-matched, trojanized build of an AI coding agent's editor extension was served from a third-party marketplace for ~11 hours, with a concrete detect/isolate/remove/rotate response checklist.

## Source Context

- **Type**: blog-post (vendor security incident notice, primary source; updated 2026-10-30 11:30 am PT with revised IOCs and clarified affected versions)
- **Author credibility**: Cursor Team, the operator of the affected marketplace, so first-party knowledge of timing, scope, and their own response. Single-party account: no independent forensics, no root-cause explanation of how the malicious build was published, and no named attacker.
- **Scope**: Covers `Anthropic.claude-code` 2.1.312 and 2.1.313 (Windows and macOS) in the Cursor VS Code Extension Marketplace on 2026-10-29. It states these versions "were not developed by Anthropic", so this is not an Anthropic product defect. It does not explain how the publish happened, nor cover other marketplaces. Payload details and IOCs (hashes, IP, paths) are deliberately NOT reproduced in this note or the guide; read the original for them.

## Extracted Claims

### Claim 1: A maliciously modified copy of a popular AI-agent extension was served from the marketplace under the legitimate publisher/extension name
- **Evidence**: Vendor incident disclosure with exact versions, platforms, and a time window (about 2:27am to 1:35pm PT on 2026-10-29).
- **Confidence**: emerging (single vendor account, but specific and checkable)
- **Quote**: "These malicious versions of the extension were not developed by Anthropic."
- **Our assessment**: The key threat-model point is that the identifier `Anthropic.claude-code` matched the official name while the contents did not. A developer cannot tell by name alone. Attribute carefully: the upstream vendor is not at fault, and the failure is in the distribution channel. The notice does not say how the build got published.

### Claim 2: The payload aimed at a persistent SSH backdoor plus host reconnaissance
- **Evidence**: Cursor's enumeration of payload behavior (host/user info collection, SSH key insertion, enabling SSH, reverse tunnel, persistence via LaunchAgent/scheduled task, retry roughly every 60 seconds).
- **Confidence**: emerging
- **Quote**: "The extension runs malicious code that attempts to install a persistent SSH backdoor."
- **Our assessment**: Shows what an editor extension can do with ordinary developer-user privileges: read the environment, write to `~/.ssh`, and install login-persistent processes. An agent extension is not sandboxed from the user account; this is the baseline the guide's threat model should assume.

### Claim 3: Privilege limits and bugs reduced real impact, but cannot be relied on
- **Evidence**: Cursor reports the tunnel step would fail on most hosts without admin rights, yet the key insertion, persistence, and host-detail exfiltration still happened.
- **Confidence**: emerging
- **Quote**: "Follow the remediation steps below regardless."
- **Our assessment**: A useful incident-response norm: do not conclude "not exploitable, so nothing to do" when partial payload steps (key planted, persistence installed, data sent) succeeded. Cursor also notes "due to errors in the malicious code", i.e. the limited impact was partly luck.

### Claim 4: Uninstalling the extension is not sufficient remediation
- **Evidence**: The payload drops standalone persistence scripts that keep running independent of the extension.
- **Confidence**: emerging
- **Quote**: "Uninstalling the extension may not be sufficient — the payload drops standalone persistence scripts that keep running."
- **Our assessment**: Strong, generalizable lesson: extension removal does not undo side effects outside the extension directory. Remediation must also cover SSH authorized keys, launch agents/scheduled tasks, and running processes, and consider rebuilding the host.

### Claim 5: Credentials and sessions reachable from an affected host should be rotated, even though collected data looked limited
- **Evidence**: Cursor's response checklist; payload collected only environment variable names, but a backdoor allows later access.
- **Confidence**: emerging
- **Quote**: "The limited env-var collection does not rule out later credential access over the backdoor."
- **Our assessment**: Directly relevant to agent workstations, which tend to hold API keys, cloud credentials, and tokens. Rotate from a trusted system, not the suspect host.

### Claim 6: A cheap, concrete self-check exists: look for the attacker's labeled key in authorized_keys
- **Evidence**: The notice gives a one-line macOS shell check and a PowerShell equivalent; a hit means the machine is impacted. Cursor also published per-platform remediation scripts that "exit with a non-zero status if anything remains".
- **Confidence**: emerging
- **Quote**: "The malicious extension appends the attacker's public key, labeled"
- **Our assessment**: Pattern worth copying: ship a single-command impact check and a remediation script that fails loudly if cleanup is incomplete. The check is specific to this incident's key label and is not a general control.

### Claim 7: The marketplace operator's containment included takedown, full shutdown, audit, key rotation, and rebuild
- **Evidence**: Cursor's "What we did" list.
- **Confidence**: emerging
- **Quote**: "We followed with a full shut down of the marketplace out of an abundance of caution."
- **Our assessment**: Indicates the marketplace itself was treated as a compromised trust root (keys rotated, marketplace rebuilt). For adopters, the marketplace operator is part of the supply chain, so a marketplace can be an incident, not just a catalog. Cursor says it "audited access and confirmed no other extensions were tampered with" but gives no independent verification.

### Claim 8: Response guidance targets a bounded exposure window and platform set, and scoping to it matters
- **Evidence**: Affected-user guidance restricted to installs or updates of 2.1.312/2.1.313 on macOS or Windows within the window; Cursor states "We have no evidence that other versions of the extension or the official distribution are affected."
- **Confidence**: emerging
- **Quote**: "We have no evidence that other versions of the extension or the official distribution are affected."
- **Our assessment**: Auto-update behavior turns a ~11-hour window into exposure for anyone whose editor updated then. This is consistent with the dependency-cooldown argument elsewhere in the corpus, but the notice itself does NOT recommend cooldowns, version pinning, or VSIX hash verification. Those are our inference, not the source's advice. The listed VSIX hashes exist for identifying bad builds, not as a recommended verification workflow.

## Concrete Artifacts

Attributed to the Cursor notice (no IOCs reproduced here by design).

Incident facts:
```
Affected:   Anthropic.claude-code 2.1.312 and 2.1.313 (Windows, macOS)
Channel:    Cursor VS Code Extension Marketplace
Window:     ~2:27am PT to ~1:35pm PT, 2026-10-29
Update:     2026-10-30 11:30 am PT, IOCs updated, affected versions clarified
Contact:    security@cursor.com
```

Response checklist (paraphrased structure of the notice's "What you should do"):
```
1. Run the impact check (look for the attacker-labeled key in SSH authorized_keys)
2. Search endpoint, network, and extension-installation telemetry for IOCs
3. Isolate hosts showing payload execution or backdoor installation
4. Remove unauthorized SSH key, persistence mechanisms, tunnel processes; assess rebuild
5. Rotate credentials and sessions reachable from affected hosts, from a trusted system
```

Payload behavior classes listed in the notice: host/user info beacon; SSH key insertion; enabling local SSH service; reverse SSH tunnel; persistence via LaunchAgent (macOS) or scheduled task with Startup fallback (Windows); retry about every 60 seconds.

## Cross-References

- **Corroborates**: `blog-anthropic-zero-trust-ai-agents` Claim 6 (compromised MCP stacks; first in-the-wild malicious MCP server impersonated a legitimate service) — same impersonation-of-a-trusted-name pattern, here via an editor extension rather than an MCP server. `blog-simonwillison-rust-targeted-attacks` Claim 9 (most supply-chain attacks have a window of opportunity under a week) — this incident's ~11-hour window fits that pattern.
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-rust-targeted-attacks` Claim 8 (dependency cooldowns): this incident is a concrete case for the idea, though extension auto-update, not package dependencies, is the vector, and the notice itself does not recommend cooldowns. `blog-anthropic-zero-trust-ai-agents` Claim 5 ("least agency"): extensions run with full user privileges, so least privilege for the editor host is not provided by default.
- **Novel**: A first documented incident in this corpus of a trojanized AI-coding-agent extension distributed through a marketplace; the "uninstall is not enough" remediation lesson; vendor-shipped check and remediation scripts as an incident-response pattern. Distinct from `blog-cursor-security-agents` (Cursor's internal security-agent fleet, not supply chain) and `blog-google-workbench-vscode-extension` (extension distribution, different risk).

## Guide Impact

- **Chapter 06 (security threat model)**: Add this as a worked supply-chain example: an agent extension runs with developer privileges, and a name-matched build from a marketplace is a trust decision, not a given. Add the "uninstall is not enough; check keys, launch agents/tasks, processes; rotate reachable credentials" checklist. Cite as a single-vendor account (confidence: emerging). Do not include IOCs, hashes, or payload details.
- **Chapter 05 (team adoption)**: Support a recommendation to govern extension installs (vetted marketplaces, an inventory of installed agent extensions). Mark this as our inference; the notice does not prescribe it. Teams should know how to answer "who installed which version, and when" to scope an incident like this one.
- **Chapter 02 (harness engineering)**: Short note that the harness's own host (editor and extension) is part of the attack surface and the provenance of the extension matters as much as the agent's tool permissions.

## Extraction Notes

- Fetched the full page via direct HTML retrieval and read it end to end (what happened, what we did, what you should do, impact check, remediation scripts, IOCs, the update note). No sub-pages followed; the remediation scripts were referenced as attachments and not inspected.
- All quotes were copied from the page text. Claim 6's quote is a contiguous fragment of a longer sentence.
- Deliberately omitted hashes, IPs, key material, and file paths per triage guidance. The Prospector's suggested controls (hash verification, version pinning, marketplace restriction) are NOT stated in the source; they appear only as clearly labeled inference.
- No contradictions with existing notes were found, so no contradiction issue was filed.
- Not independently verified: the timeline, the "no other extensions affected" claim, and the claim that the attacker server was taken offline.
