---
source_url: https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude
source_type: blog-post
title: "How Outtake built a cyber investigator on Claude"
author: Anthropic (no individual byline; quotes Jack Hayford, engineering lead for Outtake's agent platform, and Alex Dhillon, founder/CEO of Outtake)
date_published: 2026-07-22
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2164"
---

# How Outtake built a cyber investigator on Claude

> Anthropic's "How startups build with Claude" case study on Outtake's Recon
> Agent — a cybersecurity investigator that runs autonomously for up to two
> hours against live adversarial infrastructure — documenting a four-stage
> build path (manual expertise → Claude Code prototype → Agent SDK
> production → eval-driven iteration) and four production lessons: filesystem
> + bash as a minimal-but-sufficient toolset, prompts as unreliable long-run
> constraints that should be hardcoded into the harness instead, evals valued
> for development speed rather than just reliability, and a "blastbox"
> containment model for agents operating in adversarial environments.

## Source Context

- **Type**: blog-post (official Anthropic/Claude blog, "How startups build with
  Claude" series, published July 22, 2026)
- **Author credibility**: Anthropic-authored case study (no individual Anthropic
  byline), built around direct quotes from Jack Hayford (engineering lead for
  Outtake's agent platform) and Alex Dhillon (Outtake founder/CEO, formerly of
  Palantir's "moonshot team"). This is vendor-published customer-story content —
  Anthropic has an obvious interest in showcasing Claude favorably — but the
  practitioner quotes describe specific engineering decisions and trade-offs
  (four build stages, specific failure-recovery anecdotes, an explicit design
  principle for where to constrain vs. where to leave freedom) rather than
  generic praise. Business growth figures (6x ARR, 10x customer base, 20M+ scans)
  are Outtake-reported and unaudited.
- **Scope**: Covers Outtake's Recon Agent — an autonomous investigator that
  traces phishing/impersonation infrastructure into full threat-actor networks.
  Covers: the four-stage build process, tool design (filesystem + bash),
  prompt-vs-harness guardrail philosophy, an eval-driven iteration loop, and a
  security/containment model for agents operating in adversarial environments
  ("blastbox," network-boundary trust checkpoint). Does NOT cover: specific
  Agent SDK API calls or code, the eval suite's actual test cases or scoring
  rubric, quantified before/after metrics for the eval-driven iteration claim
  (no numbers given beyond qualitative "faster" and "safer"), or the mechanics
  of the network-boundary trust-scoring checkpoint beyond the three example
  questions it asks.

## Extracted Claims

### Claim 1: Recon Agent sessions run a median of 16 minutes but routinely stretch to an hour or more, with the longest observed run lasting two hours of autonomous work

- **Evidence**: Direct production metric reported in the article, describing
  actual session-length distribution for a live cybersecurity investigation
  agent.
- **Confidence**: emerging (single first-party production metric; no
  distribution/percentile detail beyond median and a stated maximum)
- **Quote**: "Agent sessions run a median of 16 minutes, but routinely stretch
  to an hour and beyond; the longest run thus far lasted two hours of agentic
  work before returning results."
- **Our assessment**: This is a concrete data point for "how long can an
  autonomous agent run unsupervised in production today" — most published
  case studies describe agent turns in minutes, not hours. The median (16 min)
  vs. tail (2 hr) gap suggests investigation length is highly
  workload-dependent (simple impersonation takedown vs. tracing a full
  adversarial network), which is a useful caveat: "long-running agent" design
  needs to handle both the common short case and the rare multi-hour case
  without assuming a fixed session length.

### Claim 2: The build process had four stages — become the domain expert first, prototype in Claude Code, graduate to the Agent SDK for lower-level control, then build an eval-driven iteration loop

- **Evidence**: The article's own structuring of Outtake's build history,
  attributed to the team's actual development sequence rather than a
  retrospective framework imposed after the fact.
- **Confidence**: emerging (first-party retrospective account, not a
  contemporaneous engineering log)
- **Quote**: "Outtake built the Recon Agent in roughly four stages. Each stage
  was about understanding what a good investigation looked like, then
  progressively handing that judgment to the agent."
- **Our assessment**: The sequencing is notable: domain expertise came before
  any tooling decision, and the harness graduation (Claude Code → Agent SDK)
  came before eval investment, not after. This matches a "validate cheaply,
  then invest in control, then invest in measurement" ordering that other
  practitioner accounts describe differently (some invest in evals from day
  one). Here, evals were explicitly the *last* of the four stages, not the
  first — worth flagging as a specific, possibly debatable, sequencing choice.

### Claim 3: Claude Code was used specifically to validate that the agent could write code, build tools on the fly, and interact directly with malicious domains, before any production harness was built

- **Evidence**: Direct quote describing why Claude Code (not a traditional
  agent framework) was chosen as the prototyping tool.
- **Confidence**: emerging (first-party practitioner account of tool choice)
- **Quote**: "The agent needed coding muscle and capability, and Claude Code
  was a strong initial harness for us to actually validate those assumptions
  and start experimenting more and more."
- **Our assessment**: The prior sentence in the source is also notable: "They
  quickly realized, however, that the Recon Agent couldn't just be a simple
  investigator. It needed to write, run code, build tools on the fly, and
  actually interact with malicious domains" — implying an initial attempt with
  "traditional agent frameworks" (unnamed) was abandoned because it couldn't
  support this. This is an anecdotal data point that generic multi-step agent
  frameworks were insufficient for a workload requiring live code generation
  and direct interaction with adversarial infrastructure, and that a coding
  agent (Claude Code) was a better starting harness even for a non-coding
  (cybersecurity investigation) task.

### Claim 4: The team constrains the agent tightly at the orchestration level, but leaves it free to improvise wherever judgment is required

- **Evidence**: Stated as the "core design principle" the team arrived at
  during the Claude Code prototyping phase.
- **Confidence**: emerging (first-party design principle, restated later in
  the article's "best practices" summary)
- **Quote**: "constrain the agent tightly at the orchestration level ('always
  do X, Y, Z when investigating a domain'), but leave it free to improvise
  whenever judgement was required."
- **Our assessment**: This is the article's central design thesis and it
  recurs in two other forms later: the "prompts are suggestions" claim (Claim
  5) locates *where* the tight constraints should live (the harness, not the
  prompt), and the closing best-practices list restates it as "hardcode
  guardrails at the orchestration layer, but don't let those constraints reach
  into low-level judgment calls." The pattern — deterministic scaffolding
  around a zone of genuine model discretion — is consistent with how other
  corpus sources describe harness design, but this source states it as an
  explicit, named trade-off rather than an implicit architecture choice.

### Claim 5: Prompts degrade as guardrails over long agent runs; behaviors that must always happen should be moved out of the system prompt and into the harness

- **Evidence**: Direct practitioner claim with a stated failure mode (prompt
  instructions "probably will be ignored eventually" as agent runs get longer
  and more complex) and a stated remedy (move the behavior into guardrails
  instead of the prompt).
- **Confidence**: emerging (first-party practitioner claim; no quantified
  measurement of *how much* prompt-instruction compliance degrades or over
  what run length)
- **Quote**: "When you're building these long-running agents that get
  complicated over time, prompts are suggestions... Slipping 'when X happens,
  make sure you do Y' into the system prompt may work initially, but as this
  agent runs longer, every single word in that prompt will probably be
  ignored eventually."
- **Our assessment**: The remedy is stated just as directly: "Pull these
  things out of the prompt and put them into the harness... Now the agent
  doesn't have to think about it anymore and it has more context space and
  attention to put towards areas where it can really thrive." This gives a
  concrete two-part decision rule: (1) if a behavior must *always* happen,
  it belongs in deterministic harness logic, not prompt text; (2) doing so is
  framed not just as a reliability fix but as a context-budget optimization —
  every hardcoded rule is one fewer thing competing for the model's attention
  in a long context. This directly corroborates the general framing in
  `blog-anthropic-steering-claude-code-mechanisms.md`, which the source
  article itself links to ("Read more on best practices for directing Claude,
  and the context cost and authority of each method") — that note's seven-method
  taxonomy for instructing Claude Code ranks mechanisms partly by how durable
  each is against being "ignored" over a long session, which is exactly the
  failure mode described here.

### Claim 6: Filesystem access plus the ability to write, read, and run code is presented as a minimal-but-sufficient tool design that lets agents improvise around obstacles like tool or network failures

- **Evidence**: Direct practitioner claim with a specific anecdote (a tool
  failing due to a network hiccup, and the agent finding its own workaround).
- **Confidence**: emerging (first-party practitioner account; single named
  anecdote, not a systematic study of recovery rate)
- **Quote**: "We've observed plenty of cases where an agent had a tool that
  was failing due to a network hiccup or whatever, and it would just find the
  right workaround and continue... Because the rest of the harness that we
  had built was strong enough, and because it left the agent with opportunity
  for improvisation with these powerful, open-ended tools, it was still able
  to get to a successful outcome."
- **Our assessment**: The article frames this explicitly against giving
  agents "very specific and nuanced tools" — the claim is that narrow,
  purpose-built tools are more brittle in the face of unexpected failure
  modes than a general filesystem + bash capability, because the agent can
  route around a broken narrow tool but can't easily route around a missing
  general capability. The caveat embedded in the quote itself ("because the
  rest of the harness that we had built was strong enough") matters: the team
  is not claiming filesystem + bash alone is sufficient — it's sufficient
  *given* a harness that already constrains and structures the agent's
  behavior (Claim 4). Filesystem-as-memory-substrate is separately
  corroborated by `blog-anthropic-claude-managed-agents-memory.md` Claim 2,
  though that note is about the Managed Agents platform's memory feature
  specifically, not general-purpose tool design — the "filesystem enables
  memory that survives compaction" line in this article is the more general
  claim of the two.

### Claim 7: Evals are valuable primarily for development speed, not just as a reliability/quality gate — replacing manual transcript review with automated, graded scoring

- **Evidence**: Direct practitioner claim contrasting the "conventional view"
  of evals (quality gate) against Outtake's stated primary motivation (speed),
  paired with a description of the manual process evals replaced (reading a
  30-minute agent transcript by hand).
- **Confidence**: emerging (first-party practitioner claim; no quantified
  before/after iteration-speed number given — "faster" is qualitative)
- **Quote**: "The conventional view is that evals are a quality gate for
  reliability. For long-running agents, though, the bigger payoff is
  speed... An eval is just a structured, graded, automatable version of that
  reflection. Once you've codified what good looks like into a repeatable
  check, you can put an agent in the judge's seat to read the 30-minute
  transcript and score the run."
- **Our assessment**: The stated progression — manual reflection first, then
  codify the reflection into a repeatable check, then hand transcript-grading
  to an LLM judge — is a concrete, generalizable path from "we review agent
  runs by hand" to "we have an eval suite," and it's pitched at teams who feel
  the eval-suite bar is too high to start: "Building some version of evals
  from the very beginning will make you build that agent faster regardless of
  how official or 'perfect' they are." This is a useful counter to a common
  hesitation (waiting for a "proper" eval framework before investing in evals
  at all).

### Claim 8: The eval-driven iteration loop let the team make large changes — model upgrades and full memory-system refactors — with confidence, and let humans review only final results instead of every run

- **Evidence**: Direct practitioner claim describing the operational effect
  of the eval suite once built (enabling sweeping changes; removing humans
  from the per-run review loop).
- **Confidence**: emerging (first-party practitioner claim; no quantified
  metric for how much confidence increased or how much human review time was
  saved)
- **Quote**: "This let them make sweeping changes, like model upgrades and
  full memory-system refactors, safely and with confidence... It also let the
  team pull themselves out of the agentic loop... Only at the very end does a
  human step in to look at the result."
- **Our assessment**: The described workflow is specific: when the Recon
  Agent finishes an investigation and reports it could have done better with
  a tool it lacked, "a separate coding agent then reads those suggestions,
  writes the new tool, and builds a test scenario to try it out" — and only
  then does a human evaluate whether the new tool actually helped. This is a
  concrete instance of an agent-improves-agent development loop gated by
  automated eval rather than continuous human review, with the explicit
  framing "We are the bottleneck, and when you build these long, complex
  agents, it's very important that the feedback loop be automated."

### Claim 9: Security for the Recon Agent centers on a "blastbox" model — assuming the agent might get hijacked and engineering the surrounding system to contain the damage rather than prevent compromise outright

- **Evidence**: Direct practitioner quote naming the specific security
  problem (an agent with filesystem + bash access being sent into adversarial
  environments) and the containment approach adopted.
- **Confidence**: emerging (first-party practitioner account of a security
  design choice; no incident data or effectiveness metric given, unlike
  `blog-anthropic-how-contain-claude.md`'s documented incidents)
- **Quote**: "We gave it a file system and bash and we're sending it to
  adversarial environments, so the most important problem we had to solve was
  building a sort of blastbox where you could try to hide your agent from
  sensitive internals without actually hindering it."
- **Our assessment**: "Blastbox" here names the same underlying strategy that
  `blog-anthropic-how-contain-claude.md` documents in much greater
  architectural and incident-level detail (environmental containment sized to
  blast radius, assumed-compromise design). This article adds an explicit
  caveat the containment note doesn't emphasize as strongly: "not all agents
  are blastbox candidates" — security design has to match the agent's purpose,
  not be applied uniformly. It does not describe *how* the blastbox is
  implemented (no sandbox technology, egress control, or isolation mechanism
  named), so this claim is directional/conceptual rather than a reusable
  architectural spec — for implementation detail, `blog-anthropic-how-contain-claude.md`
  remains the authoritative source.

### Claim 10: Outtake scores trust at the point the agent reaches out to the internet, checkpointing every outbound request against questions like whether the target page is an impersonation, malware, or an active prompt-injection attempt

- **Evidence**: Direct practitioner description of a specific security
  control implemented at the network boundary.
- **Confidence**: emerging (first-party description of a security control;
  no detail on how the trust score is computed, what model or classifier
  performs the check, or measured effectiveness)
- **Quote**: "Outtake is now scoring the level of trust at the exact point
  where the agent reaches out to the internet, implementing a checkpoint that
  evaluates whatever the agent is about to touch: 'Is this page an
  impersonation? Is it malware? Is it trying to prompt-inject the agent right
  now?'"
- **Our assessment**: This is a network-boundary content-inspection
  checkpoint conceptually similar to the "server-side prompt-injection probe
  that screens tool outputs" described in
  `blog-anthropic-claude-code-auto-mode.md` (per that note's cross-references
  in `blog-anthropic-how-contain-claude.md`), but applied here to *outbound*
  requests before the agent touches a page, rather than to *inbound* tool
  output after the fact. The explicit inclusion of "is it trying to
  prompt-inject the agent right now" as one of three checkpoint questions is
  notable: it treats the malicious infrastructure the agent investigates as
  an active adversary specifically targeting the agent, not merely as inert
  data the agent analyzes — a natural framing for a cybersecurity investigator
  but a sharper adversarial-content framing than most non-security agent
  deployments would need.

### Claim 11: Claude was chosen in part because of its resistance to prompt injection, given that the Recon Agent is deliberately sent into environments built by adversaries to attack it

- **Evidence**: Direct attribution of a model-selection rationale to
  prompt-injection robustness specifically (not general capability).
- **Confidence**: anecdotal (single-sentence vendor/customer attribution; no
  comparative data against other models, no benchmark cited)
- **Quote**: "The Outtake team chose Claude in part because of its strength
  against prompt injection."
- **Our assessment**: This is a thin claim on its own — no benchmark, no
  comparison, no methodology — but it is the kind of practitioner-adoption
  signal that corroborates the more rigorously measured injection-resistance
  claims elsewhere in the corpus (e.g., the phishing-test data in
  `blog-anthropic-how-contain-claude.md`, which reports a 96% *successful*
  injection rate in a realistic social-engineering scenario despite
  "best-in-class model defenses" — a useful tension: Claude's injection
  resistance is good enough to be a stated reason for model choice in an
  adversarial-by-design product, while the same corpus's own incident data
  shows model-layer injection defenses are still far from sufficient alone).
  This source does not resolve that tension; it's consistent with, not
  contradictory to, the "environmental controls must be the real backstop"
  position of the containment note.

### Claim 12: Outtake grew annual recurring revenue 6x and its customer base more than 10x year-over-year, scanning more than 20 million potential cyberattacks in 2025

- **Evidence**: Company-reported growth figures presented in the article's
  "quick pitch" summary box.
- **Confidence**: anecdotal (single-company, self-reported business metrics;
  no methodology, no baseline, no independent audit)
- **Quote**: "Grew annual recurring revenue 6x and its customer base more than
  10x year-over-year, scanning 20M+ potential cyberattacks in 2025 alone."
- **Our assessment**: These are business-outcome metrics, not agent-performance
  metrics — useful only as evidence that the underlying product is
  commercially viable at scale, not as evidence for any specific engineering
  claim in the rest of the article. Should be cited only as company-scale
  context, not as validation of the technical claims (tool design, prompt
  philosophy, eval approach) made elsewhere in the source.

## Concrete Artifacts

### Four-stage build process (from the article's structure)

```
Step 1: Become the expert first
  - Engineers ran real cyber investigations themselves
  - Pulled domain expertise from customers and design partners
  - Output: a fixed reference standard for "what good looks like"

Step 2: Prototype in Claude Code
  - Started with traditional agent frameworks; found them insufficient
  - Needed: write/run code, build tools on the fly, interact with malicious domains
  - Output: core design principle — tight orchestration constraints, free
    improvisation where judgment is required

Step 3: Graduate to a production-grade harness (Claude Agent SDK)
  - Motivation: needed lower-level control over memory, context, sessions
  - Explicitly did not want to rebuild the agent loop / session handling themselves
  - Carried over patterns from Claude Code prototyping without losing velocity

Step 4: Build a tight iteration loop driven by evals
  - Manual transcript review ("brutal, doesn't scale") -> codified reflection
    -> automated eval suite running many scenarios at once
  - Enabled: model upgrades, full memory-system refactors, "safely and with confidence"
  - Removed humans from per-run review; humans review only final results

Source: "How Outtake built a cyber investigator on Claude" (Anthropic, 2026-07-22)
```

### Best-practices checklist (from the article's closing section)

```
- Do you know what "good" looks like?
  -> Be the agent first; run the real task yourself before automating it.
- Is each piece of complexity earned?
  -> Find the simplest working version, automate piece by piece, add
     complexity only when results justify it.
- Is your harness matched to the workload?
  -> Validate fast in Claude Code, graduate to Agent SDK for lower-level
     control; don't rebuild the agent loop yourself.
- Where should the agent be constrained?
  -> Hardcode guardrails at the orchestration layer; leave low-level
     judgment calls to the agent's improvisation.

Source: "How Outtake built a cyber investigator on Claude" (Anthropic, 2026-07-22)
```

### Attack-chain framing used to motivate the Recon Agent's scope

```
Attacker process (per the article): weaponize public data -> build
impersonations as lures -> exploit internal systems.

Legacy tooling gap called out: each stage is guarded by a different,
disconnected tool category:
  - Threat intelligence tools -> monitor public-data stage only
  - Brand protection tools -> watch for impersonations only
  - Endpoint tools -> guard internal systems only
None trace the connected infrastructure across all three stages.

Recon Agent's stated difference: instead of taking down one artifact (e.g.
a cloned login page), it follows leads to connected infrastructure (e.g. a
fake "Customer Support" Telegram account), maps the adversarial network in
a graph, and produces a report with threat-actor profile + timeline.

Source: "How Outtake built a cyber investigator on Claude" (Anthropic, 2026-07-22)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` (Claim 3, Claim 4): This article's
    "blastbox" concept (Claim 9 here) restates that note's core principle —
    environmental containment sized to blast radius, designed to hold even if
    the model is compromised — using different vocabulary but the same
    underlying strategy. Also corroborates that note's Claim 11 (96% prompt
    injection success rate in a realistic attack) by independently treating
    prompt injection as a real, assumed-successful threat requiring
    environmental (not just model-layer) defense (Claim 10 here).
  - `blog-anthropic-steering-claude-code-mechanisms.md`: This article's
    "prompts are suggestions, pull hardcoded behavior into the harness" claim
    (Claim 5) corroborates and is explicitly linked from within the source
    article itself to that note's seven-method taxonomy for instructing
    Claude Code, which ranks mechanisms partly on durability against being
    "ignored" over a long session.
  - `blog-anthropic-claude-managed-agents-memory.md` (Claim 2): That note's
    filesystem-as-memory-substrate design for Managed Agents corroborates
    this article's more general claim (Claim 6) that filesystem access is
    what "enables memory that survives compaction" for long-running agents —
    though this article is about a Claude Code/Agent SDK deployment, not the
    Managed Agents platform specifically.

- **Contradicts**: None found. The prompt-injection tension noted under Claim
  11 (Claude chosen partly for injection resistance, vs. the containment
  note's 96% successful-injection incident) is a difference in emphasis, not
  a factual contradiction — both sources agree model-layer defenses are
  necessary but insufficient alone, and this article's own "blastbox"/network
  checkpoint claims (9, 10) show Outtake building environmental defenses on
  top of, not instead of, model-layer injection resistance. No contradiction
  issue filed.

- **Extends**:
  - `blog-anthropic-how-contain-claude.md`: Extends the general containment
    architecture (gVisor containers / OS-level sandboxes / full VMs, matched
    to user population) with a fourth deployment context that note doesn't
    cover: an autonomous agent operating against externally-controlled,
    actively adversarial infrastructure (live malicious domains) rather than
    a user's own filesystem or a knowledge worker's documents. The
    network-boundary trust checkpoint (Claim 10) is a concrete control this
    article adds that the containment note does not describe.
  - `blog-anthropic-ai-accelerated-offense.md`: That note's thesis (AI
    accelerates attacker capability, motivating AI-native defense) is given a
    concrete production instance here — Outtake explicitly frames its product
    as answering "agentic offense needs agentic defense," with Alex Dhillon's
    quote ("The average attack is not only executed faster because of AI, but
    it also captures deeper access due to AI") echoing that note's premise
    from the defender-vendor side rather than the security-research side.

- **Novel**:
  - **Long-running session metrics for a live, unsupervised agent**: 16-minute
    median, 1-2 hour routine, 2-hour observed maximum, for a single
    autonomous investigation. No other corpus source gives this specific a
    session-length distribution for an agent operating without a human in
    the loop for the duration of the run.
  - **"Evals for speed, not just reliability" framing**: The explicit
    reframing of automated evals as a development-velocity tool first and a
    quality gate second, plus the concrete "manual reflection -> codified
    check -> automated judge" progression, is a specific articulation not
    found elsewhere in the corpus in this form.
  - **"Blastbox" terminology and the "not all agents are blastbox candidates"
    caveat**: A named term for assumed-compromise containment, plus the
    explicit statement that this containment strategy is agent-purpose-
    dependent rather than universal.
  - **Network-boundary trust-scoring checkpoint for outbound agent requests**:
    Checking "is this an impersonation / malware / active prompt injection"
    at the moment the agent is about to reach out to a URL is a specific
    control pattern not previously documented in the corpus.
  - **Agent-improves-agent tool-authoring loop**: A separate coding agent
    reading the Recon Agent's self-reported tooling gaps, writing a new tool,
    and building a test scenario for it — with humans reviewing only the
    final before/after result — is a concrete instance of automated
    tool-gap-driven development not described elsewhere in the corpus in this
    specific loop shape.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 5 ("prompts are suggestions")
  as supporting production evidence for the existing steering-mechanism
  guidance sourced from `blog-anthropic-steering-claude-code-mechanisms.md`.
  Specifically: this source gives a concrete failure mode ("every single word
  in that prompt will probably be ignored eventually" over a long run) and a
  concrete remedy (move must-always-happen behaviors into harness/guardrail
  logic) that the guide can cite as a second, independent practitioner account
  reaching the same conclusion as Anthropic's own first-party steering post.

- **Chapter 03 (Verification)**: Add Claim 7 and Claim 8 (evals as a speed
  tool, and the manual-reflection-to-automated-judge progression) as a
  concrete on-ramp recommendation for teams that feel they need a "proper"
  eval framework before starting. The guide should state the progression
  explicitly: start with manual review of agent transcripts, codify what you
  look for into a repeatable check, then hand transcript grading to an LLM
  judge — and frame the payoff as iteration speed (safely making sweeping
  changes like model upgrades), not only defect-catching.

- **Chapter 06 (Security and Threat Model)**: Add Claim 9 and Claim 10 (the
  "blastbox" containment model and the network-boundary trust checkpoint) as
  a case study for agents operating against actively adversarial,
  externally-controlled infrastructure — a scenario the existing containment
  material (`blog-anthropic-how-contain-claude.md`) covers for user-controlled
  environments (a developer's machine, a knowledge worker's VM) but not for
  an agent deliberately sent to interact with infrastructure built by an
  attacker to target it. The explicit caveat "not all agents are blastbox
  candidates" should be preserved — this is a targeted pattern for
  adversarial-environment agents, not a universal containment recommendation.

- **Chapter 04 (Context Engineering)**: Add the tool-design argument from
  Claim 6 (filesystem + bash as a minimal-but-sufficient toolset that
  survives compaction and supports improvisation around tool/network
  failures) as a counterpoint to guidance favoring narrow, purpose-built
  tools — with the explicit caveat from the source itself that this only
  works "because the rest of the harness... was strong enough." The guide
  should present this as conditional: general-purpose tools plus a strong
  harness, not general-purpose tools alone.

## Extraction Notes

- WebFetch on the source URL returned only a high-level AI-generated summary
  rather than the article's actual text (a known limitation of that tool for
  this kind of content). To get verbatim quotes, the raw HTML was fetched
  directly via `curl` and stripped of markup with a Python script to recover
  the article's actual paragraph text. All quotes in this note were copied
  character-for-character from that recovered text, not from the WebFetch
  summary.
- The article is short (~5 minute read, roughly 20 substantive paragraphs) —
  all of its content was read and extracted; there were no linked sub-pages
  with additional substantive text (the "View the full webinar" and "Get a
  free Recon Agent assessment" links at the end point to gated/marketing
  destinations, not additional readable source material, and were not
  followed).
- No paywall or access issue. The article is fully public on claude.com/blog.
- The article is thinner on quantified evidence than some other Anthropic
  first-party engineering posts in the corpus (e.g.
  `blog-anthropic-how-contain-claude.md`'s specific incident counts and
  percentages) — most claims here are qualitative practitioner statements
  ("faster," "safely," "strong enough") rather than measured before/after
  numbers, which is reflected in the `emerging`/`anecdotal` confidence ratings
  throughout rather than `settled`.
- No contradictions with existing source notes were found; the one notable
  tension (Claim 11, model choice for injection resistance vs. the 96%
  successful-injection incident in the containment note) was assessed as a
  difference in framing/emphasis, not a factual contradiction, per the
  discussion under Claim 11 and Cross-References → Contradicts. No
  contradiction issue was filed.
