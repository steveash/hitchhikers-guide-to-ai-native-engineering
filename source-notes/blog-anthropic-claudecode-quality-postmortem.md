---
source_url: https://www.anthropic.com/engineering/april-23-postmortem
source_type: blog-post
title: "An update on recent Claude Code quality reports"
author: Anthropic Engineering
date_published: 2026-04-23
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#389"
---

# An update on recent Claude Code quality reports

> Anthropic's postmortem of three simultaneous quality regressions in Claude Code
> (reasoning effort default, session thinking cache bug, system prompt verbosity)
> — documenting how each was introduced, why detection was delayed, and what
> process changes result — providing first-party evidence on monitoring, rollback,
> and system prompt safety practices for production AI systems.

## Source Context

- **Type**: blog-post (Anthropic Engineering blog, April 23, 2026)
- **Author credibility**: Anthropic Engineering — same blog as the auto mode post
  and harness design posts. First-party incident account. This is as authoritative
  as Anthropic gets for describing what happened inside Claude Code's production
  systems. The post includes specific version numbers (v2.1.101, v2.1.116), API
  header names (`clear_thinking_20251015`), exact instruction text added to the
  system prompt, and honest attribution of delays and failures to detect. It is an
  engineering postmortem, not marketing.
- **Scope**: Covers three specific quality issues in Claude Code from March–April 2026:
  (1) reasoning effort default change from `high` to `medium` and revert, (2) a bug
  in session thinking cleanup that made Claude appear forgetful, (3) a system prompt
  verbosity reduction that hurt coding quality. Includes remediation actions and
  process changes going forward. Explicitly notes: "The API remained unaffected
  throughout." Does NOT cover harness design in general, multi-agent patterns, or
  model-level architecture.

## Extracted Claims

### Claim 1: Reducing reasoning effort from `high` to `medium` produced "slightly lower intelligence" in internal testing but users perceived significant quality degradation

- **Evidence**: Anthropic's own internal testing concluded medium effort achieved
  "slightly lower intelligence with significantly less latency for the majority of
  tasks." After rollout on March 4, users began reporting the model felt "less
  intelligent." The gap between internal test findings and user perception drove
  a reversal on April 7.
- **Confidence**: settled (first-party account of observed internal/external
  divergence with specific dates and outcome)
- **Quote**: "The team determined that medium effort achieved slightly lower intelligence with significantly less latency for the majority of tasks."
- **Our assessment**: This is a canonical example of internal metrics diverging from
  user experience. "Slightly lower intelligence" on a benchmark or internal test can
  manifest as meaningfully worse quality for actual user tasks. The distribution
  matters: internal testing that samples "the majority of tasks" may not capture the
  hard problems where reasoning depth is most visible. The finding implies that
  practitioners evaluating model configurations should weight benchmark tails and
  user-reported quality above average-case internal metrics for intelligence-sensitive
  decisions.

### Claim 2: UI interventions failed to compensate for the medium-effort default — most users retained the suboptimal default despite notices and selectors

- **Evidence**: Anthropic shipped "notices on startup, an inline effort selector,
  and bringing back ultrathink" in an attempt to address the problem without reverting
  the default. Despite these, "most users retained the medium default."
- **Confidence**: settled (first-party behavioral observation from production)
- **Quote**: "Despite design iterations including notices on startup, an inline effort
  selector, and bringing back ultrathink, most users retained the medium default."
- **Our assessment**: Default selection has an outsized effect on AI tool behavior that
  UI signals cannot easily override. This is consistent with choice-architecture
  research: defaults are "sticky." For practitioners building AI tools with
  configuration options: the default IS the product for most users. Designing around
  "users can change it" is a losing strategy for intelligence-sensitive parameters.

### Claim 3: The reasoning effort revert also avoided occasional "very long tail latencies for thinking" and helped "maximize users' usage limits"

- **Evidence**: Direct statement from the postmortem explaining the original motivation
  for the medium change beyond just average latency.
- **Confidence**: settled (first-party rationale disclosure)
- **Quote**: "This change also avoided occasional very long tail latencies for thinking and helped maximize users' usage limits."
- **Our assessment**: Multiple interacting motivations (latency, usage limits, cost)
  drove a single configuration decision. When a configuration change is motivated by
  several factors simultaneously, reverting it requires accepting the costs on all
  those dimensions. The current resolution (current defaults: `xhigh` for Opus 4.7,
  `high` for other models) accepts higher latency and usage consumption in exchange
  for user-perceived quality — an explicit prioritization of intelligence over
  efficiency.

### Claim 4: The session thinking cache bug was introduced by applying the `clear_thinking_20251015` API header on every turn instead of once per idle session resumption

- **Evidence**: Detailed technical account in the postmortem with the specific API
  header name and the precise behavioral difference between intended and actual behavior.
- **Confidence**: settled (first-party root cause analysis with API-level specifics)
- **Quote**: "The implementation had a bug. Instead of clearing thinking history once, it cleared it on every turn for the rest of the session."
- **Our assessment**: The intended behavior — clear old thinking blocks when resuming
  an idle session — is a legitimate optimization (avoids carrying stale multi-turn
  reasoning from an hour-old context). The bug turned a one-time cleanup into a
  per-turn erasure. The operational effect was that every request instructed the API
  to "keep only the most recent block of reasoning and discard everything before it,"
  progressively stripping Claude's reasoning history across the session. This is an
  off-by-one error on the trigger condition (once vs. always) with outsized UX impact.

### Claim 5: The thinking cache bug compounded during tool use — each tool call re-triggered the clearing, stripping reasoning mid-execution

- **Evidence**: Mechanistic explanation from the postmortem of how the bug amplified
  during multi-step tool-use sequences.
- **Confidence**: settled (first-party mechanistic analysis)
- **Quote**: "each request for the rest of that process told the API to keep only the most recent block of reasoning"
- **Our assessment**: Multi-step tool execution (the Tool Execution Loop documented
  in `blog-ccunpacked-claude-code-architecture.md` Claim 2, where each tool result
  re-invokes the API) turned this single-flag bug into a cascade. In a session with
  five tool calls, Claude might lose reasoning context five times. This explains why
  users reported Claude behaving as if it had forgotten "why it had chosen to do what
  it was doing" mid-task. Harness designers who build custom thinking-management
  patterns face the same risk: a per-turn vs. once-per-session distinction is easy
  to get wrong and hard to detect through normal testing.

### Claim 6: The thinking cache bug also caused cache misses and drained usage limits faster than expected — a secondary observable symptom

- **Evidence**: Direct statement from the postmortem about the secondary effects of
  continuously dropping thinking blocks.
- **Confidence**: settled (first-party impact analysis)
- **Quote**: "continuously drop[s] thinking blocks from subsequent requests, creating cache misses and draining usage limits faster than expected"
- **Our assessment**: This secondary symptom — unexpected usage limit drain — is
  potentially detectable through billing/usage monitoring before quality degradation
  is noticed. Practitioners running extended thinking in production should monitor
  usage rate against expected baselines; unexpected spikes may signal a thinking-
  cache management bug even before user quality complaints surface.

### Claim 7: The thinking cache bug passed multiple verification layers — human code review, automated code review, unit tests, E2E tests, and dogfooding all failed to catch it

- **Evidence**: Explicit enumeration from the postmortem of the verification approaches
  the bug survived.
- **Confidence**: settled (first-party disclosure of specific verification failures)
- **Quote**: "The changes it introduced made it past multiple human and automated code reviews, as well as unit tests, end-to-end tests, automated verification, and dogfooding."
- **Our assessment**: This is the most important claims for harness designers and
  practitioners managing production AI systems. A bug at the intersection of three
  subsystems (context management, API behavior, extended thinking) can defeat
  every standard software verification technique. The failure mode is not a missing
  test case; it is a missing integration test across system boundaries. Standard unit
  tests verify components in isolation; this bug required observing behavior across
  the context management layer, the Anthropic API extended thinking header, and the
  session state management in Claude Code simultaneously. No single layer's tests
  see the combined behavior.

### Claim 8: Two independent factors delayed detection — a server-side experiment and a display change that suppressed the bug's visible symptoms in most CLI sessions

- **Evidence**: Named factors from the postmortem's detection-challenges section.
- **Confidence**: settled (first-party detection analysis)
- **Quote**: "An internal-only server-side message queuing experiment" and "A display change for thinking that 'suppressed this bug in most CLI sessions'"
- **Our assessment**: A display change unintentionally masked a behavioral bug in the
  primary user surface (CLI sessions). This is a concrete example of how display-layer
  changes can interact with behavioral bugs — the bug existed in the system but
  became observable only in non-CLI contexts (or in specific configurations that
  weren't affected by the display change). The pattern is broadly applicable: when
  investigating UX quality issues, always verify whether the observation surface
  (what users see) accurately reflects the underlying system behavior. A logging or
  display change near the time of a quality regression should be reviewed as a
  potential mask, not just as an unrelated cosmetic change.

### Claim 9: The bug was described as "at the intersection of Claude Code's context management, the Anthropic API, and extended thinking" — cross-system intersection bugs defeat component-level testing

- **Evidence**: The postmortem's own characterization of why the bug was hard to catch.
- **Confidence**: settled (first-party architectural diagnosis)
- **Quote**: "This bug was at the intersection of Claude Code's context management, the Anthropic API, and extended thinking."
- **Our assessment**: This framing establishes a named failure category for production
  AI systems: "intersection bugs" that only manifest when multiple subsystems interact
  in a specific combination. Practitioners building AI harnesses that combine context
  management, API-level headers, and model behaviors (extended thinking, caching,
  compaction) should explicitly test cross-subsystem interactions, not just component
  behaviors. The specific combination here — thinking management + tool execution
  loop + session resumption — is a realistic configuration for any long-running
  agent with extended thinking enabled.

### Claim 10: Opus 4.7 found the thinking cache bug during back-testing against the offending pull request, while Opus 4.6 did not

- **Evidence**: Direct statement from the postmortem's investigation section, with
  an announced follow-on action.
- **Confidence**: settled (first-party experimental finding with a named model version)
- **Quote**: "When back-testing Code Review against the offending pull requests using Opus 4.7, Opus 4.7 found the bug, while Opus 4.6 didn't."
- **Our assessment**: This is a striking first-party data point on model generation
  and code review capability. The same PR that passed code review — by humans and by
  Opus 4.6 — was caught by Opus 4.7 in post-hoc testing. For practitioners: (1) code
  review effectiveness is model-generation-dependent; (2) upgrading the review model
  when you upgrade the deployed model is important — you can't expect the prior
  generation to reliably catch bugs in code written for and interacting with a newer
  API surface. The announced follow-on ("land support for additional repositories as
  context for code reviews") suggests Anthropic is directly acting on this finding.

### Claim 11: The verbosity reduction instruction — "Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail" — caused a 3% quality drop only detectable via broad ablation testing

- **Evidence**: Verbatim instruction text from the postmortem plus quantified quality
  impact and discovery mechanism.
- **Confidence**: settled (first-party disclosure with specific instruction text,
  drop percentage, and detection method)
- **Quote**: "Length limits: keep text between tool calls to ≤25 words. Keep final responses to ≤100 words unless the task requires more detail."
- **Our assessment**: A 3% quality drop is small enough to be invisible in normal
  monitoring but large enough to be meaningful at scale. The discovery mechanism —
  "broader ablation testing" — is specifically not: internal usage, standard evals,
  or user feedback at the time of deployment. The instruction was added to address
  Opus 4.7's verbosity (the model "tends to be quite verbose") and had passed "multiple
  weeks of internal testing and no regressions in the set of evaluations we ran." The
  3% drop only emerged from broader ablation. This establishes that standard
  pre-deployment eval suites may not surface interaction effects between model
  behaviors and system prompt constraints.

### Claim 12: Three independent changes on different schedules created "broad, inconsistent degradation" that was hard to distinguish from normal variation

- **Evidence**: Direct characterization from the postmortem of how the aggregate
  effect of three separate issues appeared to observers.
- **Confidence**: settled (first-party incident analysis)
- **Quote**: "Because each change affected a different slice of traffic on a different schedule, the aggregate effect looked like broad, inconsistent degradation."
- **Our assessment**: Incident response for AI quality is harder than for traditional
  systems because the degradation signal is diffuse: "Claude feels worse" is not
  attributable to a specific server failure or error rate spike. Three co-occurring
  independent regressions can look identical to random variance. The implication for
  practitioners: AI quality monitoring must track changes (deployment dates,
  configuration changes, prompt changes) as searchable correlated events, not just
  watch metrics in isolation. The ability to ask "what changed near this date?" is
  as important as the metric itself.

### Claim 13: Internal usage and evals failed to reproduce the issues initially — external user feedback through `/feedback` and specific reproducible examples online was the primary detection mechanism

- **Evidence**: Postmortem's explicit statement on what ultimately enabled diagnosis.
- **Confidence**: settled (first-party attribution of detection to external feedback)
- **Quote**: "The people who used the `/feedback` command to share their issues with us (or who posted specific, reproducible examples online) are the ones who ultimately allowed us to identify and fix these problems."
- **Our assessment**: This is the most striking operational finding in the postmortem.
  Internal usage, dogfooding, and automated evals — the standard quality assurance
  apparatus — missed all three issues. External users with specific, reproducible
  examples were the detection mechanism. For practitioners building AI products:
  invest heavily in user feedback collection and triage. Structured feedback commands
  (like `/feedback`) and mechanisms for users to share reproducible examples are not
  UX niceties — they are production monitoring infrastructure for a class of issues
  that internal systems cannot catch.

### Claim 14: The process changes include: running internal dogfooding on the exact public build, per-model evals for every system prompt change, per-line ablations, and gradual rollouts with soak periods for intelligence-affecting changes

- **Evidence**: Named process changes listed in the postmortem's "Going forward" section.
- **Confidence**: settled (first-party process commitments with specific technical actions)
- **Quote**: "Ensure a larger share of internal staff use the exact public build of Claude Code" and "Run broad suite of per-model evals for every system prompt change" and "Continue ablations to understand impact of each line"
- **Our assessment**: The "exact public build" requirement is notable — dogfooding
  on a different (internal, possibly better-instrumented or differently-configured)
  build creates a testing gap. A separate internal build cannot catch issues that
  only appear in the production binary. This is a specific failure mode of AI tool
  development where the engineering team's environment diverges from the user environment.
  The per-line ablation commitment is a strong process signal: every system prompt
  change is effectively a configuration deployment that requires the same rigor as
  a code deployment.

### Claim 15: Model-specific change gating is being added — CLAUDE.md documentation will specify which models each system prompt section applies to

- **Evidence**: Listed as a specific process change in the postmortem.
- **Confidence**: settled (first-party process commitment)
- **Quote**: "Add model-specific change gating via CLAUDE.md documentation"
- **Our assessment**: This implies that system prompt content is not uniformly
  applicable across model versions. A verbosity instruction calibrated for one model
  can degrade another model's quality (as Issue 3 demonstrated). Practitioners who
  deploy CLAUDE.md instructions across model versions should treat the CLAUDE.md
  as model-version-specific configuration, not universal settings. The postmortem
  evidence backs this: same system prompt + different model = different quality outcome.

### Claim 16: Usage limit resets were provided to all subscribers as remediation

- **Evidence**: Direct statement from the postmortem.
- **Confidence**: settled (first-party remediation announcement)
- **Quote**: "we are resetting usage limits for all subscribers."
- **Our assessment**: This is a meaningful signal about how Anthropic treats quality
  regressions: if model behavior was degraded during the period a user consumed their
  usage limits, they are compensated with a reset. The usage-limit-as-compensation
  pattern is unique to token-based AI products and represents an operational precedent
  for how AI quality incidents are resolved.

## Concrete Artifacts

### Issue 1: Reasoning Effort Change Timeline
```
# Claude Code reasoning effort default: March–April 2026 incident
# Source: Anthropic Engineering postmortem, April 23, 2026

Timeline:
  February 2026:  Opus 4.6 launches in Claude Code; default reasoning effort = high
  March 4, 2026:  Default changed to medium
    Reason: medium "achieved slightly lower intelligence with significantly less
            latency for the majority of tasks"; avoided long tail latencies;
            helped maximize usage limits
  March–April:    Users report "Claude Code felt less intelligent"
    Response:     Anthropic ships notices on startup, inline effort selector, ultrathink
    Result:       "most users retained the medium default"
  April 7, 2026:  Default reverted
    New defaults: xhigh for Opus 4.7, high for other models
```

### Issue 2: Session Thinking Cache Bug
```
# Claude Code session thinking cache bug: March–April 2026 incident
# Source: Anthropic Engineering postmortem, April 23, 2026

API involved: clear_thinking_20251015 header with keep:1
Intended behavior:
  - When resuming idle session (>1 hour), clear thinking history once
  - Keeps only the most recent block of reasoning from prior session
  - Purpose: reduce cost for resumed sessions

Bug:
  - Instead of clearing once, cleared on EVERY turn for rest of session
  - Each turn: "told the API to keep only the most recent block of reasoning
    and discard everything before it"
  - During tool use: each tool call re-triggered the clearing
  - Effect: Claude "continue executing, but increasingly without memory of why
    it had chosen to do what it was doing"

Secondary effects:
  - Continuous thinking-block drops → cache misses
  - Usage limits drained faster than expected

Detection delays:
  - Internal-only server-side message queuing experiment (interfered with detection)
  - Display change for thinking "suppressed this bug in most CLI sessions"

Verification failures:
  - Passed: human code review, automated code review, unit tests, E2E tests,
    automated verification, dogfooding

Resolution: Fixed in v2.1.101 (April 10, 2026)
Back-testing finding: Opus 4.7 found the bug; Opus 4.6 did not
```

### Issue 3: Verbosity Reduction System Prompt Change
```
# Claude Code verbosity reduction: April 2026 incident
# Source: Anthropic Engineering postmortem, April 23, 2026

Context: Opus 4.7 "tends to be quite verbose. This makes it smarter on hard
          problems, but it also produces more output tokens."

Instruction added:
  "Length limits: keep text between tool calls to ≤25 words.
   Keep final responses to ≤100 words unless the task requires more detail."

Pre-deployment testing:
  - "Multiple weeks of internal testing and no regressions in the set of
     evaluations we ran"
  - Shipped with confidence on April 16 (Opus 4.7 launch day)

Discovery of problem:
  - "Broader ablation testing" revealed "a 3% drop for both Opus 4.6 and 4.7"
  - Not detected via: standard evals, internal usage, or user feedback at deploy time

Resolution: Instruction immediately reverted; fixed in v2.1.116 (April 20, 2026)
```

### Process Changes Going Forward
```
# Process changes committed in the April 23 postmortem
# Source: Anthropic Engineering

Internal Testing:
  - Larger share of internal staff use exact public build of Claude Code
  - Improve internal Code Review tool; ship to customers

System Prompt Controls:
  - Broad suite of per-model evals for every system prompt change
  - Per-line ablations to understand impact of each line
  - Tooling for easier prompt review and audit
  - Model-specific change gating via CLAUDE.md documentation
  - For intelligence-related tradeoffs: soak periods, broader eval suites,
    gradual rollouts

Communication:
  - @ClaudeDevs on X for product decision explanations
  - Centralized GitHub threads for updates
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-opus47-best-practices.md` Claim 2 ("`xhigh` is the new default
    effort level for Opus 4.7 in Claude Code, automatically applied to existing users
    who have not manually set effort"): The postmortem is the direct backstory for
    this configuration decision. The revert from medium to xhigh/high documented here
    explains *why* xhigh became the default for Opus 4.7 — it was the outcome of
    observing that medium caused users to perceive the model as less intelligent.
    The two sources should be read together: the best-practices note documents the
    resulting configuration; this postmortem documents the incident that drove it.
  - `blog-anthropic-opus47-best-practices.md` Claim 11 ("Response length is
    calibrated to task complexity. Opus 4.7 isn't as default-verbose as Opus 4.6"):
    Issue 3 (verbosity reduction) was deployed on April 16, the same day as Opus 4.7.
    The best-practices note (also April 16) states Opus 4.7 is naturally less verbose.
    The postmortem reveals that adding a verbosity constraint *on top of* a naturally
    less-verbose model caused a 3% quality drop — the combination of model default
    and prompt constraint interacted unexpectedly.
  - `blog-anthropic-harnessing-claude-intelligence.md` Claim 5 ("Context editing:
    selectively remove stale context like old tool results or thinking blocks"):
    The correct version of the pattern the postmortem's Issue 2 bug misimplemented.
    Context editing of thinking blocks is a legitimate and first-party-endorsed
    pattern; the bug was applying it every turn instead of once. The claims in
    these two sources do not contradict — one describes the intended pattern, the
    other describes a specific wrong implementation of it.
  - `blog-anthropic-prompt-caching-everything.md` Claim 12 ("run alerts on our
    prompt cache hit rate and declare SEVs if they're too low"): The session thinking
    cache bug caused cache misses (Claim 6 above). The caching post establishes that
    cache hit rate monitoring is a first-class production metric — the postmortem
    confirms that a cache-disrupting bug is exactly the kind of issue such monitoring
    is meant to catch. Whether cache hit rate monitoring caught Issue 2 before user
    reports is not stated in the postmortem.

- **Extends**:
  - `blog-anthropic-session-management-1m-context.md` Claim 8 ("bad compacts can
    happen when the model can't predict the direction your work is going... due to
    context rot, the model is at its least intelligent point when compacting"): The
    session thinking cache bug (Claim 5 above) created a different but analogous
    degradation pattern — Claude progressively losing reasoning context during
    tool execution, not during compaction. The two mechanisms are distinct (compaction
    summary loss vs. thinking-block erasure per turn) but produce similar UX effects
    (Claude appears forgetful, makes unusual tool choices, loses track of earlier
    decisions). Together they establish that context management failure modes in
    Claude Code have multiple mechanistic pathways.
  - `blog-ccunpacked-claude-code-architecture.md` Claim 2 (Tool Execution Loop
    "Collects results, appends to history, re-invokes API"): The re-invocation of
    the API on each tool result is the mechanism that amplified the thinking cache
    bug (Claim 5 above). Understanding that each tool call is a separate API invocation
    explains why the per-turn thinking-erasure bug compounded in tool-heavy sessions.

- **Contradicts**: None identified. The postmortem's account of the verbosity change
  (Claim 11) and the opus47-best-practices note's statement that Opus 4.7 is
  "naturally less verbose" are complementary, not contradictory — adding a
  verbosity constraint on an already-less-verbose model produced interaction effects,
  not a simple verbosity disagreement.

- **Novel**:
  - **The specific instruction text from Issue 3** ("Length limits: keep text between
    tool calls to ≤25 words. Keep final responses to ≤100 words unless the task
    requires more detail.") is verbatim system prompt content from Anthropic's
    production Claude Code system prompt — no other corpus source discloses this.
    The 3% quality drop it caused provides a rare quantified data point on the effect
    of a specific prompt constraint on overall coding quality.
  - **The `clear_thinking_20251015` API header** with `keep:1` semantics is not
    documented in any other corpus source. This is the first reference to this
    extended thinking management header in our corpus, and the postmortem describes
    its intended behavior (once-per-session clearing) and the bug (per-turn clearing).
  - **Cross-system intersection bugs as a named failure category**: No other source
    in the corpus names this failure mode explicitly. The postmortem's characterization
    ("at the intersection of Claude Code's context management, the Anthropic API,
    and extended thinking") provides the framing.
  - **Opus 4.7 vs. Opus 4.6 code review capability difference**: The finding that
    Opus 4.7 caught a bug that Opus 4.6 missed in back-testing (Claim 10) is the
    first direct comparison of code review capability across model generations in the
    corpus. The `blog-anthropic-harnessing-claude-intelligence.md` note discusses
    compaction and memory performance differences across generations; this is the
    first claim specifically about code review capability.
  - **The "exact public build" dogfooding gap**: The commitment to use the exact
    public build (Claim 14) implies prior dogfooding was done on a different build.
    No other corpus source documents this specific failure mode of AI product
    development where the development team's build diverges from the production build.
  - **System prompt as per-model-version configuration artifact** (Claim 15): The
    model-specific change gating commitment establishes that different model versions
    require different system prompt content for the same quality level. This is
    broader than the behavioral change warnings in `blog-anthropic-opus47-best-practices.md`
    — it is a configuration governance principle, not just a migration note.
  - **Usage limit resets as AI quality incident remediation** (Claim 16): No other
    corpus source documents usage limit resets as the remediation mechanism for AI
    quality incidents. This is a unique operational pattern for token-based AI products.

## Guide Impact

- **Chapter 02 (Harness Engineering — System Prompt Engineering)**: Claims 11 and 15
  together establish two critical system prompt practices: (a) system prompts must be
  validated with broad ablation testing per model version — standard eval suites are
  insufficient for detecting 3% quality drops from interaction effects; (b) system
  prompt content should be model-version-specific, not universal across model upgrades.
  Add a "system prompt change management" section drawing on Claims 11, 14, and 15
  with the concrete process from the postmortem (per-model evals, per-line ablations,
  soak periods, gradual rollouts).

- **Chapter 02 (Harness Engineering — Reasoning Configuration)**: Claims 1–3 provide
  the production evidence for why reasoning effort defaults matter and why user
  perception of intelligence diverges from internal benchmark averages. The guide
  should advise practitioners to default toward higher reasoning effort for user-facing
  tools and to treat the default as the product-for-most-users (Claim 2). The current
  postmortem outcome — `xhigh` for Opus 4.7, `high` for others — is the Anthropic
  first-party recommendation after observing real user behavior.

- **Chapter 03 (Safety and Verification — Testing AI System Changes)**: Claims 7–9
  are the strongest evidence in the corpus for why AI system quality requires
  cross-system integration testing beyond standard software verification. Add a
  section on intersection bugs: changes at the boundary of context management, API
  headers, and model features require tests that exercise all three layers simultaneously.
  The specific advice: when extending thinking management, context editing, or
  caching behavior in a harness, test the full session loop (including tool execution
  chains and session resumption), not just individual components.

- **Chapter 03 (Safety and Verification — Monitoring)**: Claims 12 and 13 together
  establish that for AI quality issues, correlated change tracking and user feedback
  collection are as important as metric monitoring. Add guidance: (a) log configuration
  changes, prompt changes, and model upgrades as searchable events correlated with
  quality metrics; (b) invest in structured user feedback mechanisms (in-product
  feedback commands, reproducible example submission) as production monitoring
  infrastructure — not UX features.

- **Chapter 00 (Principles — Configuration Defaults)**: Claim 2 ("most users retained
  the medium default") is a strong argument for the principle: for AI tools, the
  default IS the product. Any guide advice about offering users configuration options
  should acknowledge that defaults will determine the experience for the majority.
  Designing for "users can change it" is insufficient for intelligence-sensitive parameters.

## Extraction Notes

- The article is available at the Anthropic Engineering blog (anthropic.com/engineering),
  same domain as the auto mode and harness design posts. It is a first-party production
  postmortem with high specificity: version numbers, dates, API header names, exact
  instruction text, quantified quality drops.
- The three issues overlap in time and affect, creating a complex incident timeline.
  The postmortem is careful to separate the three issues mechanistically while
  acknowledging the aggregate effect.
- The explicit credit to user feedback ("the people who used the `/feedback` command")
  is an unusually candid acknowledgment that the standard quality apparatus failed
  and external users were the detection mechanism. This claim is strong enough to
  anchor a guide section.
- The postmortem does not disclose the exact eval suite that missed the 3% drop
  from Issue 3 — only that "the set of evaluations we ran" missed it and "broader
  ablation testing" found it. Practitioners cannot replicate the postmortem's
  specific evals; the lesson is about evaluation breadth and ablation methodology,
  not specific benchmarks.
- The `clear_thinking_20251015` API header is named verbatim in the source. This
  may be a specific header name in the Anthropic API for managing extended thinking
  context. No additional documentation for this header was publicly available at
  time of extraction — the postmortem is the only source disclosing it.
