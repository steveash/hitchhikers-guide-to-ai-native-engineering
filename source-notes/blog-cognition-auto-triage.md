---
source_url: https://cognition.com/blog/auto-triage
source_type: blog-post
title: "Introducing Auto-Triage"
author: The Cognition Team
date_published: 2026-05-18
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1830"
---

# Introducing Auto-Triage

> Cognition product announcement: Devin's "Auto-Triage" feature monitors
> incoming alerts across Slack, Linear, GitHub, Sentry, Datadog, and custom
> webhooks, investigates autonomously (including spinning up parallel
> sub-Devins), maintains long-running memory across incidents to
> deduplicate and route them, and runs in a sandboxed environment designed
> to treat alert payloads as untrusted input — validated by one named
> customer (Modal) using it unprompted on production inference alerts.

## Source Context

- **Type**: blog-post (cognition.com/blog, published 05.18.26 per the
  page's own byline, i.e. 2026-05-18; company blog, no individual byline
  beyond "The Cognition Team")
- **Author credibility**: Published directly by Cognition, the company
  that builds Devin — this is a vendor product-announcement channel, not
  an independent account. The one specific practitioner validation is
  attributed by name and title: Hari Subbaraj, "Member of Technical Staff
  @ Modal." No independent, non-Cognition-hosted account of Modal's usage
  exists in this source.
- **Scope**: Covers what the Auto-Triage feature does (monitor, investigate,
  summarize/tag/PR), where it plugs in (Slack, Linear, GitHub, Sentry,
  Datadog, custom webhooks, schedules), the memory/context mechanism across
  investigations, the sandboxing/prompt-injection rationale, one customer
  quote, and a limited-time pricing offer ($200 in credits). Does NOT cover:
  triage accuracy, false-positive rate, investigation latency, cost per
  incident, incident volume at Modal, the underlying model version behind
  Devin at the time of this announcement, or any comparison to prior Devin
  behavior with numbers attached (the post asserts it "feels different"
  without quantifying how).

## Extracted Claims

### Claim 1: Auto-Triage lets Devin monitor incoming alerts, investigate them automatically, and return with an investigation, next steps, or a PR
- **Evidence**: The article's own summary sentence, restated in the closing
  "Try Auto-Triage" section as a call to action ("give Devin an ongoing
  responsibility").
- **Confidence**: emerging (vendor product description of a shipped,
  purchasable feature — not an anecdote, but no independent measurement)
- **Quote**: "Devin can now monitor incoming alerts, investigate them automatically, and come back with an investigation, next steps, and even a PR."
- **Our assessment**: This is the headline capability claim and reads as a
  straightforward feature description rather than a stretch claim — the
  rest of the post backs it with specifics (integrations, memory,
  sandboxing) rather than just repeating the summary. Treat as an existence
  claim for a shipped, paid feature, not as evidence of accuracy or
  reliability at any particular rate.

### Claim 2: Existing alerting systems (Slack, Linear, GitHub, Sentry, Datadog, custom webhooks) stop at detection, leaving a human to reconstruct context before acting
- **Evidence**: Problem-framing paragraph that opens the post, naming the
  specific systems Auto-Triage later claims to integrate with.
- **Confidence**: emerging (a structural observation about existing tooling,
  not a measured claim, but plausible on its face and used to motivate the
  rest of the feature)
- **Quote**: "Engineering teams already have systems that tell them when something might be wrong: Slack channels, Linear issues, GitHub checks, Sentry alerts, Datadog dashboards, customer escalations, and custom webhooks. Most of these systems usually stop at detection: they create a message, ticket, or alert, and then a human has to reconstruct the context around it."
- **Our assessment**: This is the marketing frame for the feature (detection
  vs. investigation gap), and it is directionally reasonable — most
  alerting tools genuinely don't investigate — but it is also the exact
  gap the vendor is selling a fix for, so it should be read as a problem
  statement rather than an independently verified pain-point survey.

### Claim 3: During an investigation, Devin inspects the codebase, checks observability tools, reads related tickets/threads, asks for missing context, and spins up parallel sub-Devins to investigate simultaneously
- **Evidence**: Direct feature-mechanics quote describing the investigation
  loop, including explicit sub-agent parallelization.
- **Confidence**: emerging (specific mechanism description for a shipped
  feature, not a single anecdote, but no example investigation is walked
  through step-by-step the way Willison's session log is)
- **Quote**: "Devin can inspect the codebase, check observability tools, look through related tickets or threads, ask for missing context, and spin up sub-Devins to investigate in parallel."
- **Our assessment**: "Spin up sub-Devins to investigate in parallel" is the
  most concrete mechanism claim in the post — it names parallel sub-agent
  decomposition as the specific technique for incident investigation,
  analogous to the subagent/parallel-decomposition pattern documented
  elsewhere in this corpus for coding tasks (see Cross-References →
  Extends) but applied here to triage rather than feature implementation.
  No detail is given on how many sub-Devins, how their findings are
  merged, or what happens on disagreement between sub-Devins.

### Claim 4: Devin routes outcomes based on investigation confidence — posting a summary if it finds a likely cause, tagging a human owner when one is needed, or opening a PR if the fix is clear
- **Evidence**: Direct quote describing the three-way outcome branching
  logic of the feature.
- **Confidence**: emerging (feature description with named decision
  branches, not a single measured outcome distribution)
- **Quote**: "If it finds the likely cause, it can post a summary. When the issue needs a human, Devin can tag the right owner. If the fix is clear, Devin can open a PR."
- **Our assessment**: The three-tier outcome model (summary / human tag /
  PR) is a specific and useful design pattern for describing what
  "autonomous triage" concretely produces, distinct from a vaguer claim
  like "Devin helps with incidents." No data is given on what fraction of
  incidents land in each tier, which is the missing number that would let
  a reader judge how often Devin actually resolves vs. merely narrates.

### Claim 5: Modal uses Auto-Triage to triage production inference-team incidents with no prompting, and reports the experience as qualitatively different from prompted Devin usage
- **Evidence**: Named customer quote, attributed to Hari Subbaraj, Member
  of Technical Staff at Modal.
- **Confidence**: anecdotal (single named practitioner at a single
  customer, vendor-hosted quote, no incident count, accuracy rate, or
  time-saved figure given)
- **Quote**: "We've been using Devin Automations to automatically triage incidents for Modal's inference team. It monitors our channel, so we don't have to prompt Devin at all. Because it has context across our codebase and observability stack, it can investigate quickly and come back with fixes or next steps. It feels different from using Devin traditionally: Devin works on its own, and we can wake up to really good investigation without prompting it."
- **Our assessment**: This is the post's only piece of independent-ish
  validation, and it is a single named quote from one customer with no
  quantification ("really good investigation" is not a measured rate).
  It should be cited as an existence proof that at least one production
  team is using unprompted, autonomous incident triage — not as evidence
  that this is reliable or common practice. "We can wake up to really
  good investigation" implies overnight/unattended operation, which
  parallels the unattended-session theme already in this corpus (see
  Cross-References → Corroborates) but from an operator describing
  incident response specifically, rather than a general coding session.

### Claim 6: Devin builds and maintains long-running context across investigations — learning recurring issues and a team's preferred routing conventions
- **Evidence**: Direct quote describing the memory mechanism as distinct
  from a single-shot investigation.
- **Confidence**: emerging (mechanism description for a shipped feature; no
  before/after measurement of routing accuracy or learning curve given)
- **Quote**: "In Auto-Triage, Devin builds and maintains long-running context of prior investigations, recurring issues, and how your team prefers issues to be routed."
- **Our assessment**: This is a specific claim about cross-session memory
  applied to a concrete task (incident routing), which is more actionable
  than a general "Devin has memory" statement — it names three things
  being remembered (prior investigations, recurring issues, routing
  preference). No detail is given on the memory's underlying mechanism
  (embeddings, structured store, or context stuffed into future prompts)
  or on how far back the context reaches.

### Claim 7: Devin's memory lets it de-duplicate incidents by connecting new alerts to earlier threads on the same known issue, saving triage time
- **Evidence**: Direct quote describing the deduplication behavior as a
  consequence of the memory mechanism in Claim 6.
- **Confidence**: emerging (specific behavioral claim, no measured time
  savings or dedup accuracy given — "significant triage time" is
  unquantified)
- **Quote**: "Devin's memory makes each future investigation more useful: Devin will learn to tag the correct owner or reference the right part of the codebase for related issues. If a known issue fires new alerts, Devin can connect that to the earlier thread, de-duplicating incidents and saving significant triage time."
- **Our assessment**: Incident deduplication via connecting a new alert to
  a prior thread is a specific, checkable claim (in principle a team could
  measure dedup precision/recall), but no such measurement is offered here
  — "significant triage time" is asserted, not sized. This is the most
  novel mechanism claim in the post relative to this corpus's existing
  proactive-agent coverage, which has not previously documented
  incident-level deduplication as a named agent behavior.

### Claim 8: Auto-Triage explicitly treats alert payloads, Slack messages, tickets, logs, and webhooks as untrusted input, and runs Devin in a network-sandboxed environment with added protections against prompt injection and data exfiltration
- **Evidence**: Direct quote naming the threat model (arbitrary text in
  external inputs) and the mitigation (sandboxing plus additional
  protections).
- **Confidence**: emerging (specific security design claim for a shipped
  feature; no red-team results, penetration-test data, or named protection
  mechanisms beyond "additional protections" are given)
- **Quote**: "Auto-Triage operates on messy inputs: Slack messages, alert payloads, tickets, logs, and webhooks. Those inputs can contain arbitrary text and should not be treated as trusted instructions." / "So Devin runs in secure, network-sandboxed environments. Auto-Triage also includes additional protections against prompt injection and data exfiltration, so Devin can investigate real external inputs while keeping its execution environment and your code and data safe."
- **Our assessment**: This is a clear, explicit statement that external
  alert content is an untrusted-instruction attack surface, and that
  Cognition's mitigation is environmental (network-sandboxed execution)
  rather than purely model-layer. The claim is stated as a design
  principle, not backed by any disclosed test results (no phishing-style
  test, no named exfiltration attempt count) — contrast with
  `blog-anthropic-how-contain-claude.md` Claim 11, which discloses a
  specific test count (24/25 exfiltration completions blocked only by
  environmental controls). This post asserts the same environmental-first
  philosophy without equivalent disclosed evidence.

### Claim 9: Auto-Triage integrates at the point alerts originate — Slack messages, Linear events, GitHub activity, schedules, and incoming webhooks — making it applicable to production alerts, new bug reports, failed CI runs, recurring health issues, and fix PRs
- **Evidence**: Direct quote listing the integration surface and the
  resulting workflow types.
- **Confidence**: emerging (integration/workflow list for a shipped
  feature, not a measured claim)
- **Quote**: "Devin can respond to Slack messages, Linear events, GitHub activity, schedules, and incoming webhooks, - right where reports first happen." / "That makes it useful for a range of triage workflows: investigating production alerts, routing new bug reports, looking into failed CI runs, summarizing recurring health issues, and opening fixes."
- **Our assessment**: This is a concrete integration surface list (useful
  for the guide as a "what does self-triggering actually plug into"
  reference), distinct from the higher-level "monitor production" framing
  in prior Cognition-adjacent sources in this corpus. Notably it explicitly
  includes failed CI runs as a triage target, which is a workflow not named
  in the Anthropic/Alberti case study already in this corpus.

## Concrete Artifacts

### Integration and workflow surface (from the article, verbatim)

```
Source: cognition.com/blog/auto-triage

Trigger surfaces:
- Slack messages
- Linear events
- GitHub activity
- schedules
- incoming webhooks

Applicable workflows:
- investigating production alerts
- routing new bug reports
- looking into failed CI runs
- summarizing recurring health issues
- opening fixes
```

### Outcome/routing model (from the article, verbatim)

```
Source: cognition.com/blog/auto-triage

If it finds the likely cause -> post a summary
When the issue needs a human -> tag the right owner
If the fix is clear -> open a PR
```

### Customer validation quote, full attribution

```
Source: cognition.com/blog/auto-triage

"We've been using Devin Automations to automatically triage incidents
for Modal's inference team. It monitors our channel, so we don't have
to prompt Devin at all. Because it has context across our codebase and
observability stack, it can investigate quickly and come back with
fixes or next steps. It feels different from using Devin traditionally:
Devin works on its own, and we can wake up to really good investigation
without prompting it."
— Hari Subbaraj, Member of Technical Staff @ Modal
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 12 ("Devin
    can watch a Slack channel and jump into an issue without being tagged,
    or monitor production and triage a spike on its own... 'like a real
    engineer on the team'") and Claim 13 (Alberti's forecast that 90% of
    agent sessions will be proactive within one to two years). This source
    is Cognition's own product blog describing the shipped mechanics behind
    those Alberti quotes — it names the specific integrations (Slack,
    Linear, GitHub, Sentry, Datadog, webhooks), the sub-Devin parallel
    investigation mechanism (Claim 3 here), and the memory/dedup layer
    (Claims 6-7 here) that the Alberti case study only gestured at without
    naming a mechanism. Together they move the proactive-triage claim from
    a single practitioner's forecast/anecdote toward a named, purchasable
    product feature with one customer quote — still not toward any
    accuracy or reliability measurement.
  - `blog-simonwillison-fable-relentlessly-proactive.md` Claim 8
    (Willison: unsandboxed coding agents are his "top contender for a
    Challenger disaster incident," and "Running coding agents outside of a
    sandbox has always been a bad idea") and Claim 9 (agents can do
    anything a shell user can do). This source's Claim 8 (network-sandboxed
    execution plus explicit prompt-injection/exfiltration protections for
    untrusted alert payloads) is the vendor-side design response to exactly
    the risk class Willison names — agents that autonomously act on
    external, potentially adversarial input need environmental containment,
    not just model-layer judgment. Notably this post treats sandboxing as
    a stated design principle without offering the kind of disclosed
    penetration-test evidence found in `blog-anthropic-how-contain-claude.md`.

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under the same conditions.

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md` Claim 3 ("Subagents via the
    Task tool are cost-neutral at ~220k tokens and enable parallel
    decomposition"; parent spawns Data Layer and Business Logic subagents
    in parallel). This source's Claim 3 ("spin up sub-Devins to investigate
    in parallel") is the same parallel-subagent-decomposition pattern
    instantiated in a different product (Devin rather than Claude Code's
    Task tool) and applied to a different task category (incident
    investigation rather than feature implementation) — evidence that
    parallel sub-agent decomposition is a recurring architectural pattern
    across vendors and task types, not specific to one tool.

- **Novel**: The explicit incident-memory deduplication mechanism (Claim 7
  — connecting a new alert to an earlier thread on a known issue to save
  triage time) is new to this corpus; no existing source note documents
  agent-level incident deduplication as a named behavior. The specific
  named integration surface for self-triggered triage (Slack, Linear,
  GitHub, Sentry, Datadog, custom webhooks, schedules — Claim 9) is also
  more granular than any prior source in this corpus, which previously
  only had "watch a Slack channel" and "monitor production" as named
  triggers (via the Alberti case study). The explicit three-tier outcome
  model (summary / human tag / PR — Claim 4) is a new, reusable framework
  for describing autonomous-triage output that this corpus lacked.

## Guide Impact

- **Chapter 04/05 (Proactive / Self-Triggered Agents)**: Add this source as
  the concrete product-mechanics citation for the proactive-agent pattern
  currently anchored by `blog-anthropic-cognition-fable5-frontier-trust.md`
  Claims 12-13 and `blog-simonwillison-fable-relentlessly-proactive.md`.
  Specifically add: the named integration surface (Claim 9), the
  three-tier outcome model — summary / tag owner / open PR (Claim 4), and
  the sub-agent parallel investigation mechanism (Claim 3). Flag clearly
  that no accuracy, false-positive, or resolution-rate figures are
  disclosed anywhere in this source — the guide should not imply this
  pattern is measured-reliable, only that it is shipped and in at least
  one production use (Claim 5).
- **Chapter 03 (Long-running context / memory)**: Add Claims 6-7 (memory
  across investigations; incident deduplication by connecting new alerts
  to earlier threads) as a concrete example of cross-session memory
  applied to a specific operational task, distinct from the general
  session-memory discussions already in the corpus. Flag that the
  underlying memory mechanism (embeddings vs. structured store vs. prompt
  stuffing) is not disclosed.
- **Chapter 02/05 (Safety / Sandboxing untrusted input)**: Add Claim 8
  (explicit "should not be treated as trusted instructions" framing for
  Slack/webhook/ticket content, mitigated via network-sandboxed execution)
  as a second vendor's articulation of the same environmental-containment
  principle already sourced from Anthropic
  (`blog-anthropic-how-contain-claude.md`) and argued from the practitioner
  side by Willison. Note in the guide that this source, unlike
  `blog-anthropic-how-contain-claude.md`, discloses no test count or
  red-team result — cite it as a second data point on principle, not on
  measured effectiveness.

## Extraction Notes

- The full article was fetched via `curl` (WebFetch's summarizing pass was
  also run first and cross-checked, but the verbatim HTML-to-text
  extraction was used as the authoritative source for all quotes above,
  since MINER.md §2a requires character-for-character quoting). The full
  post is short (~500 words across seven short sections: intro, "Customers
  are using Auto-Triage today," "Devin gets smarter with every incident,"
  "Auto-Triage works where issues pop up," "Built for untrusted inputs,"
  and "Try Auto-Triage"). No sub-pages or footnotes were linked from the
  article body worth following — the only other links on the page are
  site navigation (Careers, Research, other blog posts) and a related-
  articles list of unrelated Cognition posts, none of which elaborate on
  Auto-Triage specifically.
- The publish date is read from the page's own byline format ("05.18.26"),
  interpreted as MM.DD.YY per the site's other post bylines (e.g.
  "06.04.26," "02.27.26"), i.e. 2026-05-18.
- No quantitative metric (accuracy, latency, cost, incident volume, or
  false-positive rate) appears anywhere in the source — this is flagged
  throughout the Extracted Claims and is the basis for the
  `confidence_overall: emerging` rating (a shipped feature with one named
  customer quote, but zero measured outcomes).
- Cross-references verified before writing: re-read
  `blog-anthropic-cognition-fable5-frontier-trust.md` in full and confirmed
  Claim 12 and Claim 13 by number and content; re-read
  `blog-simonwillison-fable-relentlessly-proactive.md` in full and
  confirmed Claim 8 and Claim 9 by number and content; re-read
  `blog-addyosmani-code-agent-orchestra.md` in full and confirmed Claim 3
  by number and content. No claim numbers were guessed.
- No contradiction meeting MINER.md §4a's filing bar was found — this
  source corroborates and extends existing claims about proactive/
  self-triggered agents and sandboxing, but does not oppose any existing
  source note's claim under matching conditions. No contradiction issue
  filed.
