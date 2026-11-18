---
source_url: https://martinfowler.com/articles/deterministic-simulation-testing.html
source_type: blog-post
title: "Deterministic Simulation Testing"
author: Unmesh Joshi (Thoughtworks Distinguished Engineer), published on martinfowler.com
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: emerging
issue: "#4795"
---

# Deterministic Simulation Testing (Unmesh Joshi, martinfowler.com)

> Explains how a single-threaded tick-driven loop with simulated clock, network and disk makes every distributed-systems test run reproducible, lists the six coding rules and architectural fitness functions needed to keep the core deterministic, and briefly claims such a harness lets an LLM turn textbook anomaly diagrams into executable scenario tests.

## Source Context

- **Type**: blog-post (long-form article with Java code from Tickloom)
- **Author credibility**: Joshi is a Distinguished Engineer at Thoughtworks and author of *Patterns of Distributed Systems*. Tickloom is his own teaching library, modeled on FoundationDB and TigerBeetle. Reviewers credited include Will Wilson and Joran Dirk Greef.
- **Scope**: Technique, code, and trade-offs for application-level deterministic simulation. It does not cover agent-generated code in general. The LLM material is two short passages (log analysis, scenario generation) with no measurements. Tickloom is a teaching library; no production deployment is claimed.

## Extracted Claims

### Claim 1: Chaos engineering checks availability, not correctness; Jepsen-style checking of the client-visible history is what catches consistency violations
- **Evidence**: Worked three-node example (Athens, Byzantium, Cyrene): a partitioned node serves a stale local read after an acknowledged write, while every request still returns a response.
- **Confidence**: settled
- **Quote**: "But availability is not the same as correctness."
- **Our assessment**: Well established. Transferable framing for agent verification: "tests ran / service stayed up" is not evidence of semantic correctness.

### Claim 2: Live fault testing is hard to reproduce for two separate reasons: unseeded fault schedules and execution nondeterminism
- **Evidence**: Run 1 / Run 2 example with identical injected fault, where acknowledgment timing flips the outcome between success and timeout.
- **Confidence**: settled
- **Quote**: "Even with the exact same sequence of faults, the system is still not guaranteed to produce the same execution."
- **Our assessment**: The useful split is that seeding the PRNG fixes only the first problem. Seeded chaos tools alone do not give replayability.

### Claim 3: There are four environmental sources of nondeterminism (clock, thread scheduling, network timing, disk timing); in-program sources (random choices, collection iteration order) are handled by coding rules instead
- **Evidence**: Figures 5-8, one worked example per source, e.g. a crash before an fsync completes yields different recovery outcomes.
- **Confidence**: settled
- **Quote**: "There are four major sources of nondeterminism in a distributed system: the system clock, thread scheduling, network timing, and disk timing."
- **Our assessment**: A clean taxonomy; it explains what a harness must virtualize.

### Claim 4: Determinism comes from making progress explicit: run the whole cluster on one thread against simulated clock/network/disk, each advanced only by test-driven tick() calls
- **Evidence**: `Tickable` interface, `Cluster.tick()` ordering (advance clocks, tick networks, clients, servers), `tickUntil` replacing sleeps.
- **Confidence**: settled (the approach is that of FoundationDB and TigerBeetle, per the article)
- **Quote**: "Nothing progresses on its own. The test controls when each component executes and delivers its work."
- **Our assessment**: Core mechanism. The article's own contribution is a teachable Java rendering, not a new technique.

### Claim 5: Timeouts must be logical tick counts, not clock readings, so that pauses and wall-clock jumps do not affect behavior; etcd-raft does the same in production
- **Evidence**: `Timeout` class counting ticks; etcd `ElectionTick`/`HeartbeatTick` sidebar.
- **Confidence**: settled
- **Quote**: "A timeout of 10 expires after exactly 10 calls to tick()."
- **Our assessment**: Concrete and verifiable design rule.

### Claim 6: A seeded fault-injection runner makes a bug found in a long randomized run replayable from its seed, and tick-stamped fault/event logs make diagnosis easy, including by an LLM
- **Evidence**: `SimulationDecisions` / `FaultInjectingSimulationRunner` code; logs like "tick=12 isolate athens". No LLM evaluation given.
- **Confidence**: emerging (technique settled; LLM-log claim is an assertion)
- **Quote**: "If a bug shows up for seed 42, running seed 42 again reproduces it."
- **Our assessment**: Seed + fault schedule + event log is a compact, agent-friendly failure artifact. The LLM sentence ("particularly effective when handed to an LLM") is unsupported by data.

### Claim 7: Fast-forward execution lets simulation explore far more fault combinations than live testing because ticks run as fast as the CPU allows
- **Evidence**: Argument by arithmetic (100 protocol ticks = 100 loop iterations, "hours" of cluster time in seconds); no benchmark.
- **Confidence**: emerging
- **Quote**: "Replay helps after a bug is found. Fast-forward helps find it in the first place."
- **Our assessment**: Plausible and consistent with FoundationDB/TigerBeetle practice, but no numbers here.

### Claim 8: Correctness checking records the client-visible history (invoke/ok/fail) and feeds it to a consistency checker such as a linearizability checker; a violation plus its seed fully reproduces the failure
- **Evidence**: Jepsen EDN history excerpt; `ConsistencyChecker.check(history, LINEARIZABILITY, REGISTER)` test.
- **Confidence**: settled
- **Quote**: "If the checker finds a violation, the seed that produced it is enough to reproduce the exact execution."
- **Our assessment**: The oracle is a spec-level invariant on observable behavior, the same shape as agent-verification oracles in other notes.

### Claim 9: Deterministic simulation cannot be retrofitted cheaply; it needs upfront architecture (single-threaded core, async I/O interfaces, no thread-heavy libraries), but the constraints apply only on the deterministic side of a seam
- **Evidence**: Argument via the custom `TickCompletableFuture` (no blocking get, no executors); production adapters (`NioNetwork`, `SingleThreadedFileIO`, `SystemClock`) may use threads if they hand results back via tick().
- **Confidence**: emerging
- **Quote**: "Deterministic simulation testing cannot be added as an afterthought; it requires upfront architectural investment."
- **Our assessment**: Important cost caveat. The article names hypervisor-level simulation (Antithesis) as the alternative when re-architecture is infeasible, which is relevant to legacy code that agents would modify.

### Claim 10: Six strict coding rules keep the core deterministic, and they cannot be enforced by review; they must be enforced by automated fitness functions (ArchUnit static rules for five, a runtime thread-confinement check for the sixth)
- **Evidence**: Rule list (no system clock, no unseeded randomness, no threads/standard futures, no direct I/O, no iteration over unordered collections, no cross-thread callbacks); `DeterminismRulesTest`; `checkOnOwnerThread()` code.
- **Confidence**: emerging (reasoned from experience; no defect data)
- **Quote**: "relying on developer discipline or code reviews to enforce these rules does not scale."
- **Our assessment**: Directly relevant to agents: this is a concrete, mechanically enforceable constraint set an agent can be held to, and it explains why one stray `HashMap` iteration silently breaks replay. The article does not mention agents here; applying it to them is our inference.

### Claim 11: Single-threaded, async, batched I/O designs usually cost little or nothing in production and may be faster
- **Evidence**: Appeal to Redis, FoundationDB, TigerBeetle; no measurements.
- **Confidence**: anecdotal
- **Quote**: "In practice, the opposite is often true."
- **Our assessment**: Reasonable for I/O-bound systems; the article itself concedes handlers must never block and multi-core scaling means multiple processes. Not evidence for CPU-bound workloads.

### Claim 12: Once a simulation harness exists, an LLM can translate a textbook anomaly diagram (DDIA quorum linearizability) into an executable scenario test, giving a learning interface
- **Evidence**: A single named example, `DDIA_LinearizabilityScenarioTest`. No prompt, no transcript, no success rate, no code shown in the article.
- **Confidence**: anecdotal
- **Quote**: "an LLM can translate the book's diagram directly into an executable Tickloom scenario"
- **Our assessment**: Credible in direction (a small deterministic API with link-delay/partition primitives is a good generation target, consistent with the DSL claim in the Fowler fragments note), but unvalidated here. The value is that outputs are checkable by running them deterministically. Treat as a hypothesis, not a result.

### Claim 13: Message-level simulation is simpler but never exercises byte-to-message framing code; byte-level simulation (FoundationDB) catches those bugs
- **Evidence**: Sidebar comparing Tickloom/TigerBeetle (whole messages) with FoundationDB's `Sim2Conn`.
- **Confidence**: settled
- **Quote**: "A bug in handling a frame that arrives split across two reads, or a connection that dies halfway through a frame, cannot show up in simulation."
- **Our assessment**: A reminder that a simulation only verifies the code that runs under it; the choice of seam sets coverage.

## Concrete Artifacts

Test pinning an outcome to chosen numbers (Joshi, "Testing with a Simulated Cluster"):

```java
try (Cluster cluster = new Cluster()
        .withProcessIds(List.of(ATHENS, BYZANTIUM, CYRENE))
        .withRequestTimeoutTicks(10)
        .useSimulatedNetwork()
        .build(QuorumReplica::new)) {
    cluster.start();
    cluster.isolateProcess(CYRENE);
    cluster.setNetworkDelay(BYZANTIUM, ATHENS, 20);
    ...
    cluster.tickUntil(() -> !write.isPending());
    assertTrue(write.isFailed());
}
```

Seeded run plus linearizability check (Joshi, "Correctness Checking"):

```java
long seed = 123L;
long runForTicks = 500;
var runner = new FaultInjectingQuorumKVScenarioRunner(seed);
History history = runner.runAndGetHistory(runForTicks);
assertTrue(ConsistencyChecker.check(history, LINEARIZABILITY, REGISTER));
```

Default fault parameters (Joshi, `SimulationDecisions`): request probability 0.4, fault probability 0.08, heal interval 40 ticks; fault types ISOLATE_NODE, PARTITION_PAIR, DELAY_LINK, DROP_LINK.

Six strict coding rules (Joshi, "Strict Coding Rules"): no system clock calls; no unseeded randomness; no threads or standard futures; no direct network or disk I/O; no iteration over unordered collections; no cross-thread callbacks across the seam. Enforced by ArchUnit `DeterminismRulesTest` (rules 1-5) and `TickCompletableFuture.checkOnOwnerThread()` (rule 6).

Durability model (Joshi, `SimulatedFile`): two byte arrays, `visible` and `durable`; `sync()` copies visible to durable; `crash()` resets visible to durable.

## Cross-References

- **Corroborates**: `blog-anthropic-datadog-temper-machine-tool.md` (Claim 9) lists "deterministic simulation with seeded fault injection" as one verification layer for agent-generated specs and says "failures reproduce exactly under the same seed"; this article supplies the mechanism behind that sentence. `blog-pragmaticengineer-orosz-allen-software-correctness.md` (Claim 7, Bank Test under fault injection; author is from Antithesis) is practitioner opinion on the same family of techniques; this article's sidebar names Antithesis as the hypervisor-level alternative.
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-fowler-fragments-2026-07-21.md` (Claim 14, DSLs and LLM reliability; line ~587 flags this Joshi article as a candidate for its own note). Claim 12 here is a second Joshi data point on a small constrained API as an LLM generation target. `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` frames agent-loop verification; this adds a deterministic, replayable oracle option.
- **Novel**: The nondeterminism taxonomy, the tick-based harness design, the six enforceable determinism rules with fitness functions, the "seam" idea, and the explicit retrofit cost caveat are new to the corpus.

## Guide Impact

- **Chapter 03**: Add deterministic simulation as a verification layer for concurrent/distributed code that agents write, positioned between CI and live chaos testing, with the replay artifact (seed + fault schedule + tick log). Cite this note with Temper Claim 9 as the agent-context corroboration. Mark emerging: no agent-specific evidence in this source.
- **Chapter 03**: Use the six-rule list as an example of constraints enforced mechanically (ArchUnit) rather than by review, applicable to agent-authored code.
- **Chapter 02**: Note that a harness can require architectural groundwork (seam and interfaces) before agents can be verified this way; legacy code may need hypervisor-level tools.
- **Chapter 04**: Optionally mention the LLM-scenario-generation claim as an unvalidated idea (anecdotal), not as a recommendation.

## Extraction Notes

- Read the full article (about 65k characters of rendered text) including sidebars and code. Linked GitHub/Tickloom sources and the DDIA scenario test were not followed, so Claim 12 rests on the article's one-sentence description.
- No agent-specific claims appear outside the Learning and the Use of LLMs section and one sentence about tick-stamped logs; applications to agents above are marked as our inference.
- Cross-reference claim numbers (Temper 9, Orosz-Allen 7, Fragments 14) were checked against the cited notes.
