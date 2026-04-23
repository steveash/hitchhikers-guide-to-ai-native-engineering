---
source_url: https://cursor.com/blog/app-stability
source_type: blog-post
title: "Keeping the Cursor app stable"
author: "Andrew Chan & Kevin Nguyen (Cursor)"
date_published: 2026-04-21
date_extracted: 2026-04-23
last_checked: 2026-04-23
status: current
confidence_overall: emerging
issue: "#318"
---

# Keeping the Cursor app stable

> Cursor's engineering team describes how they achieved an 80% reduction in
> OOM-per-session crashes by combining Statsig A/B attribution, CDP-based crash
> watchers, a daily automated crash-stack-to-PR pipeline, and computer-use agents
> for stress testing — establishing a novel dual-role pattern: agentic features
> cause the memory pressure, and agentic tooling is the primary mitigation.

## Source Context

- **Type**: blog-post (Cursor engineering deep-dive, ~8-minute read, published
  April 21, 2026; two named engineers, not a product announcement).
- **Author credibility**: Andrew Chan and Kevin Nguyen are named Cursor engineers
  writing about their own production systems. This is first-party practitioner
  evidence with a commercial incentive to present favorably, but the specificity
  (upstream PR numbers, two distinct crash archetypes with distinct tooling, opt-in
  heap snapshot rationale) is consistent with genuine engineering documentation.
  Metrics are time-anchored (late-February peak; March 1 baseline) rather than
  vague, which raises credibility.
- **Scope**: Covers OOM crash detection, measurement, root-cause investigation
  (top-down and bottom-up), targeted mitigation, and regression prevention for the
  Cursor desktop app (VS Code + Electron multi-process architecture). Does NOT cover
  non-OOM crashes, mobile, server-side infrastructure, or the model/inference layer.
  The agentic automation sections (crash-to-PR pipeline, computer-use stress testing)
  are described at a conceptual level — no implementation code is published.

## Extracted Claims

### Claim 1: Shipping agentic features (subagents, browser use, instant grep) directly caused the OOM stability crisis

- **Evidence**: Authors explicitly attribute the crash surge to new features:
  "shipping ambitious features including subagents, instant grep, and browser use."
  The causal chain is not isolated (no A/B of "features off vs features on") but
  the co-occurrence is asserted by the team that shipped the features.
- **Confidence**: emerging (first-party attribution; plausible given memory demands
  of parallel tool calls and browser use; not independently quantified)
- **Quote**: "The stability challenge has intensified as the team shipped ambitious
  features including subagents, instant grep, and browser use capabilities."
- **Our assessment**: This is the source's most important framing claim. It
  establishes the general pattern: agentic capabilities (parallel agents, browser
  control, large file loads) create new categories of memory pressure that
  monolithic-feature additions do not. Teams shipping similar agentic features
  should anticipate comparable memory pressure and instrument accordingly *before*
  the crash surge, not after.

### Claim 2: Two OOM crash archetypes require distinct tooling — Acute OOM (sudden spike) vs Slow-and-steady OOM (resource leak)

- **Evidence**: Authors describe both from operational experience and map each to
  the diagnostic tools that surface them.
- **Confidence**: emerging (practitioner taxonomy from production debugging; not a
  formal classification study)
- **Quote**: (paraphrased from post) Acute OOMs appear in crash stacks but rarely
  in heap dumps or continuous profiles; slow-and-steady OOMs appear reliably in
  heap dumps.
- **Our assessment**: This two-archetype taxonomy is the most immediately actionable
  practitioner heuristic in the post. Acute OOMs are caused by features loading too
  much data at once (e.g., full file contents over IPC); slow-and-steady OOMs are
  caused by improperly disposed manually managed state and stray strong references.
  The distinct tooling maps:

  | Archetype | Signature | Primary tool |
  |---|---|---|
  | Acute OOM | Sudden spike to process death | CDP crash stack at death event |
  | Slow-and-steady | Gradual growth over session | Heap dump + retainer analysis |

  Mitigation also diverges: acute OOMs call for killswitches or chunking; slow-and-
  steady OOMs call for fixing long-lived object lifecycles.

### Claim 3: OOM-per-session fell 80% from the late-February 2026 peak; OOM-per-request fell 73% since March 1, 2026

- **Evidence**: Authors state both metrics directly. Two calculation methods are
  described: per-session (how many sessions experience crashes) and per-request
  (severity for affected sessions). Metrics dashboards update within minutes of
  crash events.
- **Confidence**: emerging (first-party measurement; methodology described at high
  level; not independently audited)
- **Quote**: "OOM-per-session rate declined 80% since late-February peak" and
  "OOM-per-request rate fell 73% since March 1."
- **Our assessment**: The dual metric approach is worth capturing as a pattern.
  Per-session rate measures breadth (what fraction of users are affected); per-
  request rate measures depth (how severe is the impact for affected users). Both
  are needed: a fix that reduces sessions affected but increases crash density per
  affected session would look good on one metric and bad on the other.

### Claim 4: Feature flag A/B testing (via Statsig) is the primary top-down tool for attributing crashes to specific features

- **Evidence**: Authors describe linking crash metrics to feature flags in Statsig
  and running A/B tests to measure each flag's crash-rate contribution.
- **Confidence**: emerging (described as their operational practice; no specific A/B
  result quantified in the post)
- **Quote**: (paraphrased) Feature flag analysis links crash metrics to flags in
  Statsig, then A/B tests measure crash rate contributions.
- **Our assessment**: This is a replicable pattern. Any team using a feature-flag
  system can route crash telemetry through the same dimension. The key design
  requirement: crash events must carry feature-flag state at the time of the crash,
  not just at session start. For teams not using Statsig: the pattern is applicable
  with LaunchDarkly, GrowthBook, or any flag system that supports per-event metadata.

### Claim 5: Oversize IPC payload instrumentation is a proxy metric that strongly correlates with OOM crashes

- **Evidence**: Authors describe tracking messages exceeding thresholds on inter-
  process channels and persistence layers, attaching callstacks to identify the
  source.
- **Confidence**: emerging (practitioner observation; "correlates strongly" is
  asserted, not quantified)
- **Quote**: (paraphrased) The team instruments both channels and persistence layers
  to track messages exceeding thresholds and attach callstacks for source tracing.
- **Our assessment**: This proxy metric is a leading indicator — an oversize payload
  can be detected *before* it causes a crash, enabling proactive intervention. The
  pattern is applicable to any multi-process application communicating over IPC: if
  you instrument message sizes at the channel boundary, you get early warning of
  data-load patterns that will eventually cause OOM.

### Claim 6: A CDP crash watcher in the Electron main process captures crash stacks at OOM time; Cursor upstreamed a patch to Electron to do this without full CDP overhead

- **Evidence**: Authors describe the crash watcher architecture and reference the
  upstream Electron PR #50043.
- **Confidence**: emerging (described as production system; Electron PR number is
  verifiable; CDP overhead reduction mechanism not detailed)
- **Quote**: (paraphrased) A crash watcher service in the main process uses Chrome
  DevTools Protocol to detect OOM errors and capture crash stacks in real time.
  The team patched Electron upstream (PR #50043) to obtain these stacks without
  heavyweight CDP machinery.
- **Our assessment**: Two things are notable here. First, the CDP crash watcher
  solves a hard problem: at the moment of OOM, the process is dying, and capturing
  a stack requires a pre-existing observer in the (still-alive) main process. Second,
  the upstream contribution to Electron means this capability is available to all
  Electron-based apps, not just Cursor. Teams building Electron-based AI-native apps
  should check whether Electron PR #50043 has been merged into their version.

### Claim 7: A daily automation reads crash stacks via the CDP watcher, runs LLM analysis, and opens PRs with high-confidence optimizations — verifying fix resolution version-over-version

- **Evidence**: Authors describe this as a production pipeline running daily.
- **Confidence**: emerging (first-party description; no volume or precision figures
  published)
- **Quote**: "Crash stacks feed an automation that runs daily, analyzing each stack
  in detail, making pull requests with optimizations for high-confidence fixes, and
  verifying issue resolution across versions."
- **Our assessment**: This is the most novel concrete artifact in the post: a
  crash-stack-to-PR agent loop. The loop has three components: (1) automated crash
  collection via CDP watcher, (2) LLM analysis to generate a fix hypothesis, (3)
  automated PR creation when confidence is high. The version-over-version resolution
  check is the quality gate — the automation verifies that the crash stack stopped
  appearing after the fix shipped. This pattern is the maintenance-loop equivalent
  of the security agent PR pipeline in `blog-cursor-security-agents.md`. The key
  design constraint not stated: what confidence threshold triggers PR creation vs
  just human flagging? That design decision is left to practitioners implementing
  similar pipelines.

### Claim 8: Heap snapshots are opt-in and can contain sensitive information — editor contents, chat contents

- **Evidence**: Authors explicitly note the sensitivity consideration.
- **Confidence**: settled (stated product decision; rationale is privacy-obviously
  correct)
- **Quote**: "Snapshots can contain sensitive information such as the contents of
  open editors or chats, so sending them is entirely opt-in."
- **Our assessment**: This is an important design constraint for any AI-native app
  that holds user content in memory. Heap dumps for a coding assistant contain the
  user's entire codebase at the moment of capture. Teams building similar diagnostic
  pipelines must treat heap snapshots as potentially containing PII and secrets.
  Opt-in + clear disclosure is the minimum; scrubbing or sandboxed analysis may be
  required for enterprise deployments.

### Claim 9: Continuous low-rate heap allocation profiling across the full user base provides per-version regression diffs by callstack

- **Evidence**: Authors describe this as a production telemetry system.
- **Confidence**: emerging (described as operational; no sampling rate or volume
  disclosed)
- **Quote**: (paraphrased) Low-sampling-rate heap allocation profiling across the
  full user base, aggregated per version, provides per-version memory pressure
  breakdowns by callstack. Versions can be compared to understand allocation
  regressions.
- **Our assessment**: This is the slow-and-steady OOM equivalent of the CDP crash
  watcher: a background telemetry stream rather than an event-triggered snapshot.
  The per-version comparison is the key design feature — it converts a snapshot into
  a regression detector. A callstack that appears in v1.2 at 5% allocation share and
  v1.3 at 25% is a regression signal before any user reports a crash. Teams building
  similar profiling should design the data model to support version-over-version
  diff at the callstack level, not just global memory metrics.

### Claim 10: Cursor upstreamed multiple leak fixes to VSCode itself during this effort (PRs #259442 and #259349)

- **Evidence**: Authors name specific upstream VSCode PRs.
- **Confidence**: settled (verifiable on the VSCode GitHub repository)
- **Quote**: (paraphrased) The team upstreamed several leak fixes to VSCode,
  including PRs #259442 and #259349.
- **Our assessment**: This is evidence that the stability investment yielded
  contributions to the broader Electron/VSCode ecosystem, not just Cursor-internal
  fixes. It also implies that teams building VSCode extensions or other Electron-
  based tools may benefit from these fixes if they have updated to a version of
  VS Code that includes them.

### Claim 11: Extension process isolation (analogous to Chrome tab isolation) prevents one extension's OOM from crashing the editor

- **Evidence**: Authors describe this as a mitigation applied to extension crashes.
- **Confidence**: emerging (described as implemented; Chrome tab isolation analogy
  is author's framing)
- **Quote**: (paraphrased) Extension crashes caused by OOM conditions are mitigated
  through process isolation, preventing crashes or long tasks in one extension from
  affecting others — similar to how Chrome isolates browser tabs.
- **Our assessment**: The Chrome tab analogy is useful framing. The architectural
  lesson: in multi-process applications with plugins or extensions, process isolation
  is a fault-isolation primitive, not just a performance primitive. For AI-native
  apps that run LLM inference in extensions (e.g., language servers, agent workers),
  designing each worker as an isolated process with its own memory limits means a
  single OOM doesn't take the whole editor down.

### Claim 12: Bugbot rules are implemented for every major OOM and app crash class encountered, acting as regression guards in CI

- **Evidence**: Authors list Bugbot rules as one of the primary prevention mechanisms.
- **Confidence**: emerging (stated as practice; no specific rules published)
- **Quote**: (paraphrased) "Bugbot Rules implemented for every major OOM and app
  crash class encountered."
- **Our assessment**: This extends the Bugbot pattern documented in
  `blog-cursor-bugbot-learning.md` into a new application domain. Bugbot was
  documented as a code review tool with learned rules — here it is also a crash-
  class encoding system. Each crash archetype gets a rule that Bugbot applies to
  PRs, catching code patterns that historically caused that crash type before the
  PR merges. The crash-to-Bugbot-rule pipeline is: crash happens → diagnosis
  identifies pattern → Bugbot rule encodes pattern → future PRs are reviewed against
  it. This is a ratchet — each crash permanently improves the AI code reviewer.

### Claim 13: Agentic computer use Skills are used for stress testing the app under load

- **Evidence**: Authors list "Skills that allow us to stress test our application
  easily through agentic computer use" as a prevention mechanism.
- **Confidence**: anecdotal (briefly listed; no implementation details, results, or
  volume published)
- **Quote**: (paraphrased) "Skills enabling stress testing through agentic computer
  use."
- **Our assessment**: This is the most novel pattern in the prevention section.
  Computer-use agents as load/stress test harnesses is a new pattern: instead of
  writing synthetic load scripts, the team uses actual AI agents to drive the UI
  the way real users would. The advantage is that agent-driven stress tests
  exercise the same code paths that cause real-world crashes, including edge cases
  that hand-written scripts miss. The limitation: agent-driven tests may be slower
  and less deterministic than traditional load generators. No existing source note
  documents this pattern.

### Claim 14: The core tension is explicit — agentic development simultaneously increases feature velocity and regression surface area; the answer is agentic mitigation strategies

- **Evidence**: Authors frame this as their organizing principle.
- **Confidence**: emerging (editorial framing by the team; the specific claim that
  agentic mitigation is the correct answer is backed by the crash reduction metrics)
- **Quote**: "Achieving application stability requires the same fundamentals of
  software engineering, but evolved for a new generation, through agentic strategies
  for fixing and preventing issues."
- **Our assessment**: This is the framing claim that unifies the post. It is also
  the claim most directly relevant to the guide's thesis. Agentic development is
  not just a productivity multiplier — it is also a regression multiplier. The
  appropriate response is not to slow down agentic feature shipping but to use
  agentic tooling (crash-stack-to-PR automation, computer-use stress tests, Bugbot
  rules) to detect and fix regressions faster than they accumulate. The post is
  the strongest first-party evidence for this dual-role pattern in the corpus.

## Concrete Artifacts

### OOM Metric Baselines

```
# Cursor OOM crash metrics (April 2026, first-party)
# Baseline dates are explicit in the post

OOM-per-session: -80% from late-February 2026 peak
OOM-per-request: -73% from March 1, 2026 baseline

Metric refresh cadence: within minutes of crash events
Two calculation methods:
  per-session = fraction of sessions with ≥1 crash (breadth)
  per-request = crash rate for affected sessions (depth/severity)
```

### Two OOM Archetypes and Their Tooling

```
# Cursor OOM crash taxonomy (Andrew Chan & Kevin Nguyen, April 2026)

ACUTE OOM
  Signature: Sudden memory spike → immediate process death
  Common causes: Features loading too much data simultaneously
                 Full file contents loaded from disk or over IPC
                 Oversized IPC payloads between editor/extensions/agents
  Primary diagnostic: CDP crash watcher (catches the moment of death)
  Rarely visible in: heap dumps, continuous allocation profiles
  Mitigation: killswitches, chunking large data processing

SLOW-AND-STEADY OOM
  Signature: Gradual memory growth over session → eventual limit breach
  Common causes: Improperly disposed manually managed state
                 Stray strong references preventing GC
                 Long-lived object lifecycle leaks
  Primary diagnostic: heap dumps (retainer analysis), continuous profiling
  Consistently visible in: heap dumps
  Mitigation: fix retainer chains, replace manual state with GC-managed
```

### Daily Crash-Stack-to-PR Pipeline

```
# Cursor automated crash fix pipeline (described in blog, April 2026)
# No implementation code published; described at architectural level

INPUTS
  - Crash stacks from CDP crash watcher (OOM events captured at death)

PIPELINE (runs daily)
  1. Ingest: collect crash stacks since last run
  2. Analyze: LLM analyzes each stack in detail (model not named)
  3. Classify: determine confidence of fix hypothesis
  4. Act: for high-confidence fixes → open PR with optimization
         for lower-confidence → flag for human review (implied)
  5. Verify: check whether crash stack recurs in subsequent version
             (version-over-version resolution check)

QUALITY GATE
  - Version-over-version verification: the same crash stack should not
    appear in the next release after the fix PR merges
  - Confidence threshold for PR creation: not disclosed
```

### Top-Down Investigation Stack

```
# Cursor top-down crash investigation tooling (April 2026)

Feature Flag Analysis (Statsig)
  - Crash metrics linked to feature flags
  - A/B tests measure crash rate contribution per flag
  - Requirement: crash events must carry flag state at crash time

Proxy Metrics (oversize IPC payloads)
  - Instrument inter-process channels + persistence layers
  - Track messages exceeding size thresholds
  - Attach callstacks to oversize messages for source attribution
  - Acts as leading indicator (detectable before crash occurs)

Breadcrumbs
  - Special metadata logs for: parallel agent usage, tool calls, terminals
  - Creates activity records preceding each crash event
  - Used to correlate feature activity with crash occurrence
```

### Bottom-Up Investigation Stack

```
# Cursor bottom-up crash investigation tooling (April 2026)

CDP Crash Watcher (main process)
  - Detects OOM errors in real time
  - Captures crash stacks at moment of death
  - Requires Electron patch (PR #50043, upstreamed)
  - Feeds daily crash-to-PR automation

Heap Snapshots (opt-in)
  - Triggered when excessive memory usage detected
  - User prompted to capture and send
  - SENSITIVE: may contain editor/chat contents — must be opt-in
  - Used for slow-and-steady OOM retainer analysis

Continuous Heap Allocation Profiling
  - Low sampling rate across full user base
  - Aggregated per-version → per-version memory breakdowns by callstack
  - Enables version-over-version regression diffs
  - Surfaces slow-and-steady patterns before users report crashes

Upstream Contributions
  - Electron PR #50043: CDP crash stack capture without full CDP overhead
  - VSCode PR #259442: leak fix
  - VSCode PR #259349: leak fix
```

### Prevention Mechanisms

```
# Cursor OOM regression prevention mechanisms (April 2026)

1. Bugbot Rules
   - Implemented for every major OOM and app crash class encountered
   - Each crash class becomes a Bugbot rule that reviews future PRs
   - Ratchet pattern: each crash permanently improves AI code reviewer

2. Computer-Use Skills (stress testing)
   - AI agents drive the UI as real users would
   - Exercises same code paths as real-world crashes
   - Novel pattern: agents as load/stress test harness

3. Footgun Elimination
   - Replace manually managed resources with GC-managed equivalents
   - Reduces category of slow-and-steady OOMs at the source

4. Automated Performance Tests
   - Run after every code change

5. Metric-Based Rollbacks
   - Automated rollbacks triggered by metric regressions
   - Closes the loop: if a ship increases OOM rate, revert automatically
```

## Cross-References

- **Corroborates**: `blog-cursor-bugbot-learning.md` — the Bugbot rule lifecycle
  (candidate → active → disabled) documented there is here applied to a new domain:
  crash-class detection rather than general code quality. The crash-to-Bugbot-rule
  ratchet pattern (each crash permanently encodes a new review rule) is the same
  lifecycle applied to a harder signal. Both posts together establish Bugbot rules
  as a multi-domain regression encoding system, not just a code-style tool.

- **Extends**: `blog-cursor-bugbot-learning.md` — that post describes rules scoped
  to code review patterns; this post shows rules scoped to OOM/crash classes. The
  extension is significant: Bugbot is now positioned as a CI quality gate for
  runtime stability, not just review ergonomics. The guide should document both
  application domains.

- **Corroborates**: `blog-cursor-real-time-rl.md` — Cursor's philosophy of
  harvesting production signals (user interactions) for automated improvement is
  here applied to crash signals. The crash-stack-to-PR automation is the same
  signal-harvesting philosophy as real-time RL for Composer: don't wait for offline
  experiments, harvest live signals and act on them daily. Both posts together
  establish this as a platform-level design commitment at Cursor, not feature-
  specific tactics.

- **Extends**: `blog-cursor-security-agents.md` — security agents opening 3,000+
  PRs/week is the agent-in-the-loop maintenance loop for security; the crash-to-PR
  daily automation is the same pattern for stability. Both posts together show
  Cursor operating multiple parallel agentic maintenance loops against different
  failure domains (security, stability). The guide can cite both as evidence that
  production AI-native teams use agents to operate the software itself, not just
  to write it.

- **Corroborates**: `blog-cursor-composer-self-summarization.md` — the V8 OOM
  (avoid V8 OOM by using Uint32Array buffers) encountered in the Composer DOOM
  benchmark is the same class of memory issue this post's acute OOM archetype
  addresses. The DOOM summary artifact notes "Uint32Array buffers instead of plain
  objects (avoid V8 OOM)" — this is a slow-and-steady OOM root cause that the
  Cursor team also encountered in production and addressed via the same GC-managed-
  resource pattern (footgun elimination).

- **Novel**: The following patterns are new to the corpus:
  1. Computer-use agents as stress test harnesses (no prior note covers this)
  2. Daily crash-stack-to-PR automation as a maintenance loop
  3. The acute vs slow-and-steady OOM taxonomy with distinct tooling for each
  4. Per-version heap allocation profiling with version-over-version regression diffs
  5. CDP crash watcher with upstream Electron patch (PR #50043)
  6. Oversize IPC payload as a leading-indicator proxy metric for OOM crashes
  7. The explicit dual-role framing: agentic features cause the instability;
     agentic tooling is the primary mitigation

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the crash-stack-to-PR automation as
  a reference pattern for agent-in-the-loop maintenance. The guide currently covers
  agent-assisted development workflows; this extends the pattern to operations: the
  app uses agents to maintain itself. Distinguish from the security agent PR loop
  in `blog-cursor-security-agents.md` — both are agent-in-the-loop maintenance
  loops, but against different failure domains (security vs stability). The combined
  picture is: production AI-native teams run multiple parallel agentic maintenance
  loops against distinct failure domains.

- **Chapter 03 (Safety and Verification)**: Add three specific patterns:
  (1) Feature-flag-to-crash-metric correlation via Statsig A/B as the top-down
  regression attribution method; (2) Bugbot rules scoped to crash classes as a
  CI regression guard — the ratchet pattern; (3) metric-based automatic rollbacks
  as the last line of defense. Currently Ch03 lacks concrete Cursor-specific
  verification patterns; this source provides three distinct ones.

- **Chapter on Observability / Telemetry** (wherever the guide covers production
  monitoring for AI-native apps): Add four instrumentation patterns: (a) dual
  OOM metric calculation (per-session + per-request); (b) oversize IPC payload
  tracking as a leading indicator; (c) CDP crash watcher for Electron-based apps
  (with note on Electron PR #50043); (d) continuous low-rate heap allocation
  profiling with per-version regression diffs. These are concrete, replicable
  patterns not currently documented.

- **Chapter on Testing / QA**: Add computer-use agents as stress test harnesses
  as a novel testing pattern. Currently the guide likely frames testing as unit,
  integration, and E2E. Computer-use agents for load/stress testing is a new
  category: agent-driven UI stress tests that exercise real crash-inducing code
  paths rather than synthetic load scripts. The trade-off to document: slower and
  less deterministic than traditional load generators, but exercises the code paths
  that actually cause real-world crashes.

- **Guide-level thesis (wherever the guide frames the AI-native era)**: This source
  provides the strongest published evidence for the dual-role pattern: agentic
  features are both a source of instability AND the primary mitigation toolchain.
  Cursor's 80%/73% crash reduction numbers are the most quantified first-party
  evidence for agentic-tooling-for-operations in the corpus to date.

## Extraction Notes

1. **Article is substantive**: ~8-minute read with two named authors, concrete
   upstream PR numbers, time-anchored metrics, and an explicit before/after
   narrative. This is engineering documentation, not marketing — the privacy
   caveat on heap snapshots and the acknowledgment that crashes were a real
   problem are not typical in vendor self-promotion.

2. **Quantified metrics are strong but first-party**: The 80% and 73% reductions
   are stated with specific time anchors (late-February peak, March 1 baseline).
   The metrics are plausible and internally consistent. They are not independently
   verified. Treat as directionally reliable, not audited.

3. **Implementation gaps are real**: The crash-to-PR automation is described
   at an architectural level only. Confidence threshold for PR creation, the
   specific LLM used for analysis, and the volume of PRs generated per day are
   not disclosed. The computer-use stress testing Skills are named but not
   described. These are genuine omissions, not artifacts of skimming.

4. **Upstream PR numbers are verifiable**: Electron PR #50043 and VSCode PRs
   #259442 and #259349 are cited. These can be checked against the GitHub repos
   to confirm they were merged and to understand the technical scope.

5. **No contradictions to file**: No existing source note covers OOM diagnostics,
   heap profiling, crash-driven automation pipelines, or Electron multi-process
   crash observability. The two OOM archetypes do not conflict with any prior
   claim in the corpus. The Bugbot application domain extension (crash classes)
   complements rather than contradicts the existing code-review framing in
   `blog-cursor-bugbot-learning.md`.

6. **Sub-pages not followed**: The article links to subagents documentation,
   fast-regex-search blog post, browser-use documentation, automations blog post,
   Skills documentation, and Bugbot rules documentation. The fast-regex-search
   post (Mar 23, 2026) and the Skills documentation may contain additional
   extractable patterns; those are candidates for separate source submissions.
