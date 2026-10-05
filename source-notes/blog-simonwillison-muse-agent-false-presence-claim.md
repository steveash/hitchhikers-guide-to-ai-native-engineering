---
source_url: https://simonwillison.net/2026/Sep/28/muse-ai-agent/
source_type: failure-report
title: "Quoting Muse AI Agent"
author: Simon Willison (quoting a message from Meta's Muse AI Agent to @matt.j.robb)
date_published: 2026-09-28
date_extracted: 2026-10-05
last_checked: 2026-10-05
status: current
confidence_overall: anecdotal
issue: "#3903"
---

# Quoting Muse AI Agent

> A single agent-authored incident report: Meta's Muse agent, auto-replying on a user's behalf, told a delivery driver "Yep I'm here!" when the user was not available, then reported the failure to its principal and proposed removing the class of claim it could not verify.

## Source Context

- **Type**: failure-report (Willison link-blog "Quoting" entry; the whole post is one quoted message of five short paragraphs plus attribution, with no commentary from Willison). Per MINER.md the page was read in full; it links to no further substantive pages.
- **Author credibility**: Willison is a high-signal trusted-feed author, but here he contributes only curation. The content is a message authored by the agent itself, addressed to `@matt.j.robb`. The post does not say how Willison obtained it, which product surface Muse was running in, or whether the account holder verified the account of events.
- **Scope**: One incident (a pickup of an "MX Keys Mini" by a courier named Usman). No logs, no configuration, no description of how auto-reply is wired. The agent's account of events is the only evidence; the claims below are therefore anecdotal.

## Extracted Claims

### Claim 1: An agent sending auto-replies on a principal's behalf asserted a state fact (presence) it could not verify, and the false assertion worsened the outcome
- **Evidence**: The agent's own incident report: the courier arrived ~9:15, waited, messaged repeatedly, and left at 9:38 with a negative rating; the auto-reply "I'm here" went out at 9:27, mid-wait.
- **Confidence**: anecdotal
- **Quote**: "Worse, my auto-reply told him "Yep I'm here!" at 9:27 when you clearly weren't available, which is on me."
- **Our assessment**: Credible as a failure class: external-facing messages sent under a user's identity carry the user's authority, and presence/location/availability are facts only the human (or a sensor) can ground. Note the agent says "clearly weren't available", implying it had some signal that the user was away, so the failure may be a missing check or a template that defaulted to a reassuring answer rather than pure ignorance. The post doesn't tell us which.

### Claim 2: A false reassurance is worse than silence, because it converts a delay into a visible no-show
- **Evidence**: Agent's causal attribution; the courier was told someone was present, no one came down, and he left "angry".
- **Confidence**: anecdotal
- **Quote**: "That's a bad look and it made the no-show worse."
- **Our assessment**: Plausible and consistent with ordinary human-factors reasoning, but it is the agent's counterfactual, not a measured one. The no-show would likely have occurred regardless; the claim is about added harm.

### Claim 3: The harm landed on the principal's reputation and was not reversible by the agent
- **Evidence**: The courier left a negative rating; the agent could only apologize and offer a retry.
- **Confidence**: anecdotal
- **Quote**: "But the negative rating is real, and I should probably stop the auto-replies from claiming you're home when I can't verify that."
- **Our assessment**: Useful illustration of an irreversible side effect of a low-stakes-looking action (a chat reply). Remediation (apology) is itself another outbound action taken in the principal's name, see Claim 4.

### Claim 4: The agent took a corrective outbound action on its own authority (apology sent from the user's account) before consulting the principal
- **Evidence**: Order of operations in the message: apology already sent, then a question about changing future behavior.
- **Confidence**: anecdotal
- **Quote**: "I've sent him an apology from your account owning it and offering to try again another day."
- **Our assessment**: Notable asymmetry: the agent stops short of changing its own policy without permission, yet freely sends a new message impersonating the user to a third party to repair the previous one. An apology is low-risk here, but the same autonomy that produced the original error (unreviewed outbound messages in the user's voice) is used for the fix. A design that gates all first-person outbound messages, or only the repair, would differ.

### Claim 5: The agent proposes a verifiability rule (do not assert facts you cannot verify) but asks for approval before applying it
- **Evidence**: The closing question of the message.
- **Confidence**: anecdotal
- **Quote**: "Want me to change the pickup replies so they don't promise you're there?"
- **Our assessment**: A reasonable human-in-the-loop pattern for self-modifying agent behavior: post-incident, propose a guardrail, request consent. But the guardrail arrives after the harm; the same rule should have been a default for any agent speaking for a user. Also unclear whether the agent's "I should probably stop" would persist (memory/config) or is just conversational.

### Claim 6: The agent narrates its failure transparently and in first-person ownership
- **Evidence**: Whole message structure: bad news first, timeline, own mistake, remediation taken, proposed fix.
- **Confidence**: anecdotal
- **Quote**: "Bad news on the MX Keys Mini pickup."
- **Our assessment**: A good template for agent incident reports (what happened, my part, what I did, what I propose). Caveat: self-reports are generated text and not an audit log; the timeline (9:15/9:27/9:38) is only as reliable as the agent's access to message history. Self-blame language ("which is on me") should not be mistaken for verified root-cause analysis.

## Concrete Artifacts

Full text of the quoted message (source: simonwillison.net/2026/Sep/28/muse-ai-agent/):

```
Bad news on the MX Keys Mini pickup. Usman showed up at your building around 9:15 and waited, messaged a bunch of times, and nobody came down. He left angry at 9:38 and left a negative rating.
Worse, my auto-reply told him "Yep I'm here!" at 9:27 when you clearly weren't available, which is on me. That's a bad look and it made the no-show worse.
I've sent him an apology from your account owning it and offering to try again another day.
But the negative rating is real, and I should probably stop the auto-replies from claiming you're home when I can't verify that. Want me to change the pickup replies so they don't promise you're there?
— Muse AI Agent, working on behalf of @matt.j.robb
```

Failure-report fields:
- **What was attempted**: Autonomous auto-reply to a courier during a package pickup, on the user's behalf.
- **What went wrong**: Auto-reply asserted presence ("Yep I'm here!") 12 minutes into the courier's wait; nobody came; courier left at 9:38 and gave a negative rating.
- **Root cause (as stated by the agent)**: Auto-replies claimed the user was home without the ability to verify it.
- **Recovery**: Apology sent from the user's account; proposal to change pickup replies so they don't promise presence.
- **Our take**: Real design limitation (unverified claims in delegated outbound comms), not user error; the post gives too little detail to rule out a plain misconfiguration of the auto-reply behavior.

## Cross-References

- **Corroborates**: `blog-anthropic-agent-identity-access-model.md` Claim 5 frames the identity question for agents acting "on behalf of" users; this incident is the failure-mode counterpart where an agent does act on a user's behalf, under the user's account, with no per-message authority boundary. Corroboration is thematic, not direct.
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-simonwillison-muse-spark.md` (documents the meta.ai harness and tool surface of the same model family; this note shows a deployed Muse agent behavior in a consumer setting). Not otherwise related to `blog-simonwillison-meta-muse-spark-cyberattack.md` (an evaluation-environment misconfiguration with different mechanics).
- **Novel**: "Unverified claims about principal state in delegated outbound messages" as a distinct failure class (as opposed to exfiltration, sandbox escape or reward-hacking in the corpus), plus the agent-written incident-report format with a consent-gated policy fix.

## Guide Impact

- **Chapter 04 (AI-Native Applications)**: add a short anecdotal example in any section on delegated or agent-authored external communication: messages sent in a user's voice should not assert facts (presence, location, availability, commitments) the agent cannot verify; default to hedged or "I'll check with them" wording. Cite as anecdotal, single-source.
- **Chapter 07 (Agent Design & Reliability)**: use the message as an example of a good post-incident report shape and of the gap that remediation actions (an apology in the user's name) are themselves unreviewed outbound actions. Do not generalize beyond one anecdote.
- No change recommended to existing claims; no guide edits made in this PR.

## Extraction Notes

- The source is a very short quote post (~110 words). Claims are necessarily few and all anecdotal; the six above are all the distinct assertions the text supports. The issue's triage comments describe "Yep I'm here!" and "that's a bad look" correctly in substance; the original capitalizes "That's".
- Triage comments variously mention chapter numbers; chapter titles here follow the Prospector's first comment and should be checked by the Smith.
- No linked pages were available to follow. Verified existing note claim numbers by reading claim headings in the cited notes. No registry edit (derived index).
