---
source_url: https://cursor.com/blog/security-incident-update
source_type: blog-post
title: "An update on our recent security incident"
author: Cursor Team (Cursor)
date_published: 2026-11-13
date_extracted: 2026-11-14
last_checked: 2026-11-14
status: current
confidence_overall: emerging
issue: "#4722"
---

# An update on our recent security incident (Cursor, 2026-11-13)

> A vendor post-mortem tracing the malicious Claude Code extension incident back to a leaked third-party vendor key, unredacted credentials inside stored coding-agent traces, and SaaS pivoting, with a list of containment controls.

## Source Context

- **Type**: blog-post (vendor incident update / post-mortem, first-party, 6 min read)
- **Author credibility**: Cursor Team, the operator of the affected systems, so first-party knowledge of its own data, credentials and response. Single-party account: external forensics experts are said to be engaged but no findings are published; the attacker is not named; no IOCs are included (the post points to the Oct 29/30 notice).
- **Scope**: Explains the causal chain behind the incident first disclosed on 2026-10-29, scope of exposure, what was not affected, and remediation. It gives no timeline of the key exposure at Fireworks, no explanation of how a "stolen credential" reached marketplace cache write access beyond the sequence given, and no root-cause analysis of why credentials were in traces.

## Extracted Claims

### Claim 1: The attack began with an access key Cursor issued to a vendor (Fireworks), which the vendor exposed
- **Evidence**: Vendor's own investigation narrative; no independent verification.
- **Confidence**: emerging
- **Quote**: "An attacker obtained an access key we had issued to Fireworks. The key was"
- **Our assessment**: The extension was the visible symptom; the entry point was a third-party vendor credential. The vendor-integration surface (keys issued to partners) is part of the threat model for any AI tool provider. Note the post attributes exposure to Fireworks ("exposed by Fireworks") but Fireworks' account is not given. The quote is a contiguous fragment; the following words ("exposed by Fireworks") are in the source as a separately formatted span.

### Claim 2: Coding-agent traces shared for model training sat in a read-only bucket and contained unredacted credentials
- **Evidence**: Cursor's account; numbers: "less than 0.01% of customers had API credentials exposed" and traces exposed for "fewer than 0.05%" of non-Privacy-Mode users.
- **Confidence**: emerging
- **Quote**: "A small number of those traces contained credentials that had not been redacted; less than 0.01% of customers had API credentials exposed."
- **Our assessment**: Strongest new lesson for the guide: agent session traces capture whatever the agent saw (env values, pasted keys, tool output), so stored traces become a credential store. Redaction before storage or sharing is a control, not an afterthought. The traces were "mostly from 2025", so old data retained for training kept its risk long after the sessions.

### Claim 3: Data retention scope was tied to Privacy Mode; Privacy Mode users were not exposed
- **Evidence**: Cursor's "What was not affected" list.
- **Confidence**: emerging
- **Quote**: "Your prompts and code if you use Privacy Mode."
- **Our assessment**: Supports the practical point that opting out of vendor training/retention reduces blast radius. Only the vendor's word; it is also a self-serving claim in a breach notice. The traces came from sessions "which we were permitted to use for model training", so retention policy was the determinant of exposure.

### Claim 4: Stolen credentials let the attacker pivot into SaaS tools and internal data
- **Evidence**: List of accessed data in the post.
- **Confidence**: emerging
- **Quote**: "Starting with those credentials, the attacker reached select SaaS tools used by Cursor."
- **Our assessment**: Shows credential chaining: one leaked secret class led to archived non-production repos, support email, usage metrics, "summaries of some coding agent conversations", and "some credentials users had sent to the Cursor support team". Support channels are a secondary credential-leak surface.

### Claim 5: A stolen internal credential was used to write a malicious extension into the marketplace cache
- **Evidence**: Cursor's account; ~11 hours availability; at most 5,000 users potentially received it.
- **Confidence**: emerging
- **Quote**: "At most 5,000 users who requested specific cached versions of the extension on October 29 potentially received the malicious build."
- **Our assessment**: Fills the "how was it published" gap in the Oct 29 notice (see Cross-References). The distribution cache, not upstream Open VSX ("never had the malware"), was the point of compromise, so verifying against the upstream source would have differed from the served artifact. Whether Cursor can know "at most 5,000" is unverified.

### Claim 6: Anthropic's product was not at fault
- **Evidence**: Vendor statement.
- **Confidence**: emerging
- **Quote**: "Anthropic did not publish this copy, and this was not a vulnerability in Anthropic's product."
- **Our assessment**: Consistent with the earlier notice. Attribution should stay with the distribution channel.

### Claim 7: Containment was over-broad on purpose, accepting feature disruption
- **Evidence**: Cursor's description of disabling services.
- **Confidence**: emerging
- **Quote**: "Out of an abundance of caution, we temporarily disabled internal and product services well beyond what the evidence required"
- **Our assessment**: Useful incident-response norm: when scope is uncertain, over-contain and restore service by service. It also means the post's "not affected" list reflects rebuilt and re-reviewed systems, not just absence of evidence.

### Claim 8: Remediation controls: vendor key revoked, blanket credential rotation, network egress restrictions, secret scanning
- **Evidence**: "What we've done" list.
- **Confidence**: emerging
- **Quote**: "Expanded network access restrictions across our service providers, where possible, so compromised credentials can't be used outside their intended location."
- **Our assessment**: The concrete controls are: rotate everything in use "even where we had no evidence of exposure"; bind credentials to origin (network restrictions); secret scanning "across all our code repositories, and expanded scanning to other internal data sources"; move traffic off the vendor and cut shared dataset access. Credential origin-binding is the generalizable one for agent environments.

### Claim 9: Release path was separated from the compromised systems
- **Evidence**: Vendor statement about separate code hosting and signing keys.
- **Confidence**: emerging
- **Quote**: "We ship Cursor from a separate code hosting system that the attacker never accessed, and no release signing keys were exposed."
- **Our assessment**: A segmentation lesson: separating release infrastructure limited the blast radius. Unverified externally. This also bears on the Oct 29 note's scope: the compromised surface was the extension marketplace cache, not the Cursor app's own update channel.

### Claim 10: Customers were notified with specific key lists, and uninstalling alone may not be enough
- **Evidence**: Notification description.
- **Confidence**: emerging
- **Quote**: "If credentials were exposed, we emailed team admins a list of the specific keys to rotate, and asked the third-party services that issued those credentials to revoke them."
- **Our assessment**: Good practice pattern: vendor-assisted revocation with the issuing services, not just telling customers. The post repeats "Uninstalling the extension alone may not be enough", corroborating the earlier note's Claim 4.

### Claim 11: The incident is declared contained, with the last attacker activity on November 1
- **Evidence**: Vendor monitoring.
- **Confidence**: anecdotal (single-party, timing-based claim)
- **Quote**: "We believe the incident is contained."
- **Our assessment**: Hedged ("believe"). Treat as the vendor's current belief; the post commits to updating if something changes.

## Concrete Artifacts

Attack chain as described by the post (attributed to Cursor, 2026-11-13; no IOCs):

```
1. Access key issued to vendor (Fireworks) exposed by the vendor
2. Key used to copy a read-only bucket of historical coding-agent traces
   (mostly 2025; non-Privacy-Mode sessions permitted for training)
3. A small number of traces held unredacted credentials
   (<0.01% of customers with API credentials exposed;
    traces exposed for <0.05% of non-Privacy-Mode users)
4. Credentials used to reach select SaaS tools -> archived non-prod repos,
   support data, usage metrics, agent conversation summaries,
   credentials users sent to support
5. 2026-10-29: stolen internal credential used to place malicious copies
   of Anthropic.claude-code in the marketplace cache (~11 h, <=5,000 users)
6. 2026-10-30: security notice; 2026-11-01: last attacker activity, blocked
```

Remediation list, condensed from "What we've done": moved inference off vendor; deactivated vendor key; rotated exposed and all in-use internal credentials; validated and rebuilt marketplace; network access restrictions across service providers; secret scanning across repos and other internal sources; redeployed production; external forensics.

## Cross-References

- **Corroborates**: `blog-cursor-malicious-claude-code-extension-notice` Claim 4 (uninstalling the extension is not sufficient remediation) and Claim 7 (the marketplace was treated as a compromised trust root: shutdown, audit, rebuild); this post repeats the first and confirms the marketplace rebuild.
- **Contradicts**: None found. The "what was not affected" list (app, release signing keys) narrows rather than conflicts with the Oct 29 note's scope, which covered only the marketplace extension. No contradiction issue filed.
- **Extends**: `blog-cursor-malicious-claude-code-extension-notice` Claim 1 and its Source Context gap: that note records "no root-cause explanation of how the malicious build was published". This post supplies a vendor-asserted chain. It also extends `blog-simonwillison-rust-targeted-attacks` Claim 9 (supply-chain window of opportunity under a week): this incident's ~11-hour window fits, though the root cause is credential theft, not a malicious dependency.
- **Novel**: Stored agent traces as a credential-leak surface; vendor/partner key as an entry point for an AI coding tool incident; support channels as a credential leak path; origin-binding of service-provider credentials. Nothing in the corpus covers agent-trace data retention as an attack surface. Related but distinct: `failure-railway-october-build-escape-to-kms-decrypt` (a different incident), `blog-simonwillison-stealing-reasoning-traces` (trace theft via model APIs, not credential exposure).

## Guide Impact

- **Chapter 06 (security threat model)**: Add this incident as a worked chain: vendor key -> trace bucket -> unredacted credentials -> SaaS -> marketplace cache write. Add "agent traces are sensitive data; redact secrets before storing or sharing" and "bind issued credentials to network origin" as controls. Cite as single-vendor account (confidence: emerging). Do not include IOCs.
- **Chapter 05 (team adoption)**: Add that data-retention settings (Privacy Mode or equivalent) and third-party vendor sharing determine exposure; teams should know whether sessions are retained for training and who the vendors are. Note this is our inference from the incident, not a Cursor recommendation.
- **Chapter 02 (harness engineering)**: Short note that session logs and traces produced by the harness inherit every secret the agent touched, so harness-level redaction belongs in the design.

## Extraction Notes

- Fetched the page HTML directly and read the whole article (What happened, What was not affected, What we've done, What's next). No sub-pages followed; the linked Oct 29 notice already has a source note.
- Quotes were copied from the extracted page text. Claim 1's quote is a fragment that stops where the source has a formatting break.
- No IOCs in the source, none reproduced.
- Numbers (0.01%, 0.05%, 5,000, ~11 hours) are the vendor's and not independently verified. Fireworks' side is not published.
- Triage comments reference "Open VSX never had the malware"; confirmed in the text.
