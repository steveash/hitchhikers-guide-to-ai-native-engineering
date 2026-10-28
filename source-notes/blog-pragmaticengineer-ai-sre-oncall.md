---
source_url: https://newsletter.pragmaticengineer.com/p/ai-sre
source_type: blog-post
title: "AI SRE: what is it, how could it change on-call – and does it work?"
author: Gergely Orosz (with Jessica), The Pragmatic Engineer
date_published: 2026-10-27
date_extracted: 2026-10-28
last_checked: 2026-10-28
status: current
confidence_overall: anecdotal
issue: "#4385"
---

# AI SRE: what is it, how could it change on-call – and does it work?

> Vendor- and company-interview survey of "AI SRE" tooling: more AI-driven deploys mean more incidents and pages, current tools accelerate investigation (not autonomous remediation), and investigation agents need verifier agents, a context layer and memory.

## Source Context

- **Type**: blog-post (paid newsletter; industry analysis built on interviews with Rootly, incident.io and ResolveAI)
- **Author credibility**: Gergely Orosz, ex-Uber engineering manager and author of The Pragmatic Engineer. He discloses he is an investor in incident.io and says he was not paid to mention any company.
- **Scope**: Sections 1-3 are fully readable, and the article text breaks off at the start of section 4 ("Making agents accurate") at the paywall. The section 4-7 headings and one-line summaries appear in the free intro. Their detail (adversarial verification, evals/backtesting, model routing, cache-hit tracking, autonomy timeline, on-call deskilling, simulation training) is NOT extracted here. Vendor figures are vendor-supplied.

## Extracted Claims

### Claim 1: Incident rate scales with change rate, and AI agents have roughly doubled change rate, so pages are rising
- **Evidence**: A back-of-envelope formula (i = c x p), the assertion that PR frequency doubled at almost all tech companies, and a Rootly chart (not reproduced) showing pages up year over year and outside-business-hours pages nearly doubled. The chart is vendor data.
- **Confidence**: emerging
- **Quote**: "Almost all tech companies have seen their"
- **Our assessment**: The "Almost all tech companies have seen their PR frequency double in a year" sentence is split across a link in the source, so only the contiguous fragment is quoted. The math is a tautology; the empirical content is the doubling of C and the unreported size of P. No independent data is given on whether P is flat. Rootly's data is a vendor sample and is not a measure of the industry.

### Claim 2: Two levers lower P: better pre-deploy verification, and learning from incidents
- **Evidence**: Author framing; Rootly's strategy diagram (not reproduced).
- **Confidence**: anecdotal
- **Quote**: "Better pre-deploy verification: more testing & verification loops"
- **Our assessment**: Useful framing that links verification (Ch03) to on-call load. The article says vendors are "well placed to learn from incidents", which is a commercial interest.

### Claim 3: "AI SRE" mostly means faster incident investigation, performed inside Slack/Teams, with engineers keeping the key decisions
- **Evidence**: Description of all three vendors' products; the pre-AI investigation steps (alert details, dashboards, runbooks, logs/observability) that the tools now automate.
- **Confidence**: emerging
- **Quote**: "AI SRE tools mostly help with the investigation phase of incidents."
- **Our assessment**: Plausible and consistent with the Anthropic CI on-call note. The author reports that vendors dislike the name; "automated incident investigation agents" is the more accurate label.

### Claim 4: Vendors fan out investigation to parallel subagents, like an engineer opening eight tabs
- **Evidence**: Description of incident.io's agent orchestrator: main agent kicks off, fans out to subagents that report progress, uses heuristics to decide where to go deeper.
- **Confidence**: anecdotal
- **Quote**: "Subagents: it fans out investigation work to subagents which report on progress"
- **Our assessment**: Same orchestrator-plus-executors shape as the Anthropic on-call note. Two independent implementations converging is mild corroboration, though both are descriptions, not measured outcomes.

### Claim 5: A human arriving ~5 minutes after the alert to find an AI summary removes "shovel work"
- **Evidence**: Author assertion; no timing data.
- **Confidence**: anecdotal
- **Quote**: "It gives the oncall dev a sense of what might be happening, instead of having to do all the “shovel work.”"
- **Our assessment**: Compare to Anthropic's reported median of 14 minutes to a first triage analysis. Neither is a controlled measurement.

### Claim 6: Giving an AI SRE the access it needs requires high trust, which pushes mid-size and larger companies to build in-house, though vendors may out-improve home-grown tools
- **Evidence**: Quote from Sam Newman's book; author reasoning about ZDR and compromise risk; author's opinion on vendor focus.
- **Confidence**: anecdotal
- **Quote**: "The trust issue is a major driver in why many mid-size-and-above companies build their own AI SRE tools."
- **Our assessment**: A real security trade-off (telemetry, logs, source, maybe a sanitized prod DB copy). The author also predicts that "AI SRE vendors are likely to become more capable than home-grown solutions", so the build-versus-buy conclusion is left open.

### Claim 7: Whether AI SREs should remediate (write code), not only mitigate, is contested; the three vendors differ
- **Evidence**: incident.io builds autonomous PR creation but customers prefer their own coding agents; ResolveAI writes simple PRs and hands off larger changes; Rootly's stated vision is a drafting agent plus a judging agent that auto-merges safe PRs. Rootly says all PRs raised so far follow human approval.
- **Confidence**: emerging
- **Quote**: "As yet, all PRs raised happen after a human has approved them."
- **Our assessment**: This is the key Ch03/Ch06 data point: vendor roadmaps outrun practice. Rootly's AI-judges-AI-merge idea runs into the verifier-independence problem (Claim 9). Treat as a vendor vision.

### Claim 8: ResolveAI rebuilt its investigation agent three times (scripted workflow, single agent with knowledge graph, multi-agent), each failing for specific reasons
- **Evidence**: Vendor account. 2024 scripted pipeline did poorly on incidents not fitting the script; 2025 single agent hit context rot, self-confirmation and no memory; 2026 multi-agent is called most reliable.
- **Confidence**: anecdotal
- **Quote**: "Context rot"
- **Our assessment**: A rare failure-mode taxonomy with architecture progression. It is a vendor self-report with no accuracy numbers. The "context rot" item cites Dex Horthy's "dumb zone" framing.

### Claim 9: A verifier agent that is structurally independent from the investigator avoids self-confirmation
- **Evidence**: ResolveAI's three roles (Investigator, Verifier, Communicator); the single-agent failure where it "almost always confirmed its first suspicion".
- **Confidence**: anecdotal
- **Quote**: "It’s structurally independent of investigators to avoid self-confirmation"
- **Our assessment**: Directly applicable to any verify-your-own-output design: the grader should not be the generator. No quantified improvement is given.

### Claim 10: Typical investigation is a 7-step loop (trigger, orient, fan out, verify, report, steer, hand off), with per-step latency/accuracy/cost trade-offs
- **Evidence**: Synthesized by the authors across the three vendors.
- **Confidence**: emerging
- **Quote**: "You’ll want to decide on tradeoffs between latency, accuracy, and cost."
- **Our assessment**: Good checklist, see Concrete Artifacts. Open design questions listed include fixed alert buckets versus hypothesis-before-paging and fan-out by hypothesis versus unbounded.

### Claim 11: A "context layer" (knowledge graph + memory + tools) is common to all three vendors and replicable in-house
- **Evidence**: Rootly Atlas, incident.io Nexus, Resolve HiveMind; Uber's Context Graph as an in-house example.
- **Confidence**: emerging
- **Quote**: "Generalizing a bit, all three of these context layers are made up of a knowledge graph, memory, and tools."
- **Our assessment**: Consistent across vendors, but the article gives no evidence on how much the layer improves outcomes (the triage question asked for this; the readable portion has none).

### Claim 12: Memory needs lifecycle management: Rootly "activates" useful notes and "quarantines" contradicted ones
- **Evidence**: Description of Rootly's memory design.
- **Confidence**: anecdotal
- **Quote**: "Systems keep changing, and this is one way to not feed stale information to the agent"
- **Our assessment**: Concrete stale-memory mitigation that maps onto lessons.md-style logs (Anthropic note Claim 11), which have no expiry mechanism.

### Claim 13: Pooling anonymized incident data across customers is offered as opt-in by Rootly only, and is contentious
- **Evidence**: Rootly cofounder JJ Tang quote; scrubbing code not open-sourced yet; author urges scrubbing confidential data first.
- **Confidence**: anecdotal
- **Quote**: "Most vendors in our space promise your data stays siloed forever. We think that’s the wrong default for operational data."
- **Our assessment**: A vendor's commercial position. Data-governance risk for Ch06.

### Claim 14: Slack agent UX is a design problem: update length affects trust, and Rootly keeps its agent quiet unless specific triggers occur
- **Evidence**: incident.io learned too-concise updates erode trust and too-long ones annoy; Rootly's four speak-up triggers.
- **Confidence**: anecdotal
- **Quote**: "a risky action is announced with no rollback plan"
- **Our assessment**: Specific, reusable "when should an agent interrupt" rules (see artifacts).

### Claim 15: In-house AI SREs from Monzo, OpenAI, Stripe and Google restrict write actions; Google's ProdAgent favours scripts over LLM determinism
- **Evidence**: Sevbot never executes mitigations on its own but applies them when instructed; Stripe runs an investigation on every outage, averaging three minutes for simple and 14 minutes for deep; ProdAgent suggests MCP tools (e.g. borg_task_restart) with policy enforcement and audit trails.
- **Confidence**: anecdotal
- **Quote**: "more scripts, less LLM determinism!"
- **Our assessment**: Four named companies converge on investigate-and-suggest with human or policy gating, supporting Claim 7's conservatism. The numbers come from Stripe's own writeup via secondhand linking, so unverified here.

## Concrete Artifacts

```
Reliability math (Pragmatic Engineer, section 1):
i = c x p
Incident rate = [Change rate] x [Probability]
C = number of changes per unit time
P = probability a single change introduces failure
```

```
Typical AI SRE investigation steps (Pragmatic Engineer, section 3):
Trigger -> Orientation -> Fan out -> Verify -> Report -> Steer -> Hand off
```

```
Rootly agent speaks up only when (Pragmatic Engineer, section 3):
- a question in the channel goes unanswered
- a stakeholder joins without context
- someone declares "mitigated" without proof
- a risky action is announced with no rollback plan
```

```
ResolveAI architecture history (Pragmatic Engineer, section 3):
2024 scripted workflow -> 2025 single agent + knowledge graph (context rot, self-confirmation, no memory) -> 2026 Investigator / Verifier / Communicator
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-oncall-cicd` (Claim 9: orchestration agent plus parallel executor subagents; Claim 11: running lessons log). The article's fan-out pattern and memory layer match that implementation. Also `blog-pragmaticengineer-orosz-horthy-context-engineering` (Claim 4: "dumb zone"), which the article cites for context rot.
- **Contradicts**: none found. Rootly's auto-merge vision is a roadmap, not a conflicting claim, and no existing note asserts the opposite.
- **Extends**: `blog-pragmaticengineer-newman-resilient-ai-powered-software` (Claim 9, review AI vendors; the article quotes Newman on the vendor-trust requirement); `blog-ghaw-fault-investigation` (Claim 2: deep investigation) by adding the on-call and page-volume side; `blog-pragmaticengineer-orosz-ubers-ai-infra-from-the-inside` (Uber's context graph is cited as an in-house knowledge graph).
- **Novel**: the i = c x p framing of AI-driven incident growth; Rootly page data; ResolveAI's three-architecture failure taxonomy; independent verifier role for investigations; memory activation/quarantine; Rootly's quiet-agent triggers; Stripe/Google/OpenAI/Monzo in-house AI SRE descriptions.

## Guide Impact

- **Chapter 03**: Add the independent Verifier pattern (Claim 9) as evidence that self-grading agents self-confirm, and note that the article ties verification to production reliability via i = c x p.
- **Chapter 05**: Note rising page volume as a team-level cost of faster shipping. The deskilling and simulation-training material is in the paywalled part and is not yet usable.
- **Chapter 06**: Cite the access-trust trade-off (Claim 6) and the restraint of OpenAI, Google and Rootly (Claims 7, 15) for autonomous production changes.

## Extraction Notes

- Fetched raw HTML and extracted the public article body. Text ends at the paywall at the start of section 4, "Making agents accurate", so claims on accuracy measurement, evals, model routing, cache hit rate, autonomy timeline, on-call deskilling and Uptime Labs simulations are unverified and not extracted.
- Quotes were copied from the extracted text; Claim 1's quote is only a fragment because the source splits the sentence around a link.
- Rootly figures and all vendor architecture descriptions are vendor-reported; the author is an incident.io investor (disclosed).
- Sub-articles linked (Stripe, Monzo, Sevbot, Google ProdAgent) were not followed.
