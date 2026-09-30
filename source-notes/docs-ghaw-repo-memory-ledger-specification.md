---
source_url: https://github.github.com/gh-aw/specs/repo-memory-ledger-specification
source_type: docs
title: "GitHub Agentic Workflows: Repository Memory Ledger Specification (Working Draft v1.0)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: emerging
issue: "#3812"
---

# GitHub Agentic Workflows: Repository Memory Ledger Specification

> A normative RFC 2119-style working draft defining agent memory as a bounded, append-only, hash-chained JSONL ledger with a disposable query projection, a three-job trust split, declarative-only compaction, and a 14-row adversarial threat table for a prompt-injected agent.

## Source Context

- **Type**: docs (formal normative specification from the `specs/` section of the gh-aw site; Version 1.0, Status: Working Draft, Editor: GitHub Agentic Workflows Team)
- **Author credibility**: First-party GitHub Agentic Workflows team. Authoritative for how `gh aw` implements the ledger; it is a working draft, so requirements may change, and it is a design/threat-model document rather than field evidence of how it performs.
- **Scope**: Data model and integrity, job responsibilities, script extension points, lifecycle (restore, append, compaction, retirement, save), concurrency guarantees, configuration limits, security considerations, adversarial review, conformance tests. Does NOT cover: workflow-author-facing configuration syntax (see `docs-ghaw-repo-memory-reference.md`), usage patterns (see `docs-ghaw-memory-ops.md`), or any measured performance/adoption data.

## Extracted Claims

### Claim 1: Agent memory is modelled as an append-only, content-hashed record log; the queryable database is disposable and never required for recovery
- **Evidence**: Normative text in Abstract, §2 and §5.1; no empirical evidence (specification).
- **Confidence**: emerging
- **Quote**: "The projection is not durable ledger state and MUST NOT be required for recovery."
- **Our assessment**: Sound event-sourcing design applied to agent memory: durable truth is immutable shards, and SQLite is rebuilt on demand. Practitioners get deterministic reconstruction and tamper-evidence per record. Unproven at scale; it is a spec, not a reported deployment.

### Claim 2: Each record has a fixed, exact schema with a SHA-256 self-hash and parent hashes, forming a DAG
- **Evidence**: §2 Data Model and Integrity.
- **Confidence**: emerging
- **Quote**: "A record MUST contain exactly `version`, `id`, `type`, `timestamp`, `parents`, `payload`, and `sha`."
- **Our assessment**: The parent-hash DAG is what lets concurrent runs coexist without locks (Claim 8). Malformed lines are skipped without losing valid records, which is a robustness choice appropriate for untrusted writers.

### Claim 3: Ledger duties are split across three jobs with different privileges, and responsibilities must never move to a less trusted job
- **Evidence**: §3 table: agent job (untrusted, no memory-branch write token), safe-outputs job (log-only, no ledger storage access), persistence job (only holder of memory-branch `contents: write`).
- **Confidence**: emerging
- **Quote**: "An implementation MUST NOT move a responsibility to a less trusted job."
- **Our assessment**: Applies the safe-outputs least-privilege pattern to memory: the agent can request appends but only a trusted job pushes. Portable principle: the process that reasons over untrusted input should not hold the credential that persists state.

### Claim 4: Everything restored from the memory branch, including shards, coverage declarations and audit entries, is treated as untrusted input by the persistence job
- **Evidence**: §3 and §8.
- **Confidence**: emerging
- **Quote**: "The persistence job MUST treat everything under the restored memory directory, including shards, coverage declarations, and audit entries, as untrusted input."
- **Our assessment**: Important because memory written by a prior (possibly injected) run is a persistence vector. Agent-supplied ledger shards and coverage files are excluded from the trusted copy set (§5.5), and files matching an already-trusted shard ID are rejected (§9).

### Claim 5: Scripted compaction policy is deliberately unsupported because Node `vm` is not a security boundary
- **Evidence**: §4.2 reasoning about host functions reaching the host realm through their constructors; configuring `ledger.compactor.script` is a compile-time error. Policy is declarative (`min-segments`, `max-segments`).
- **Confidence**: emerging
- **Quote**: "An in-process Node `vm` context is not a security boundary"
- **Our assessment**: A concrete, generalizable design lesson: do not run user "policy hooks" in-process next to a push token. By contrast, `repo-memory.validation.script` IS allowed, but only in a separate Node process with bounded timeout and sanitized environment, and it fails closed. The spec also pre-registers the conditions under which scripted compaction could return (separate least-privilege process, serialized data only, may declare coverage but never delete, fails open).

### Claim 6: Compaction fails open; validation fails closed
- **Evidence**: §4.1, §5.3, §9 (compaction failure and shard-ID collision rows).
- **Confidence**: emerging
- **Quote**: "Compaction MUST fail open: a failed compaction MUST leave the ledger readable and MUST NOT block persistence."
- **Our assessment**: Availability-vs-safety is assigned per step: an optimization (compaction) must not block work; a policy gate (validation script) must block on non-zero exit. The spec flags the trap in the other direction: "a misparsed limit that disables compaction through fail-open handling is a defect", i.e. fail-open hides misconfiguration.

### Claim 7: Retirement (deletion of source shards) requires proof of coverage and is owned by the runtime
- **Evidence**: §5.4; verification that every source record SHA is present in the replacement; only declarations created by the current run are honoured (§9).
- **Confidence**: emerging
- **Quote**: "Invalid, incomplete, current-run, or forged declarations MUST be ignored."
- **Our assessment**: Deletion is the dangerous operation for memory; this verify-then-delete with directory `fsync` is a sensible template. The spec reads "current-run" both as excluded from retirement (here) and as the only trusted source (§9 table says "created by the current runtime run"); presumably it means shards created by the current persistence run are not "stable" and cannot be retired. The wording is ambiguous and could be a draft defect.

### Claim 8: Concurrency is handled by retaining multiple DAG heads and converging by identity, not by locking; the guarantees are explicitly limited
- **Evidence**: §6.
- **Confidence**: emerging
- **Quote**: "It does not provide distributed locking, serializable transactions across branches, or confidentiality of repository-memory contents."
- **Our assessment**: Honest scope statement. Guarantees are integrity, boundedness, deterministic reconstruction, best-effort convergence. Workflows needing exactly-once or serialized semantics must layer that themselves.

### Claim 9: `ledger_query` pagination is cursor-based, deterministic, and explicitly not snapshot-consistent
- **Evidence**: §5.2: ascending record-SHA order, exclusive `after` cursor, `hasMore`/`nextCursor`.
- **Confidence**: emerging
- **Quote**: "Pagination is not a snapshot: concurrent writes may add matches between requests."
- **Our assessment**: A tool-design detail worth copying for any agent-facing memory MCP server: truncated results must be visibly truncated so the agent does not treat a partial page as complete.

### Claim 10: The audit trail is a dedicated, hash-only, best-effort log and is never authoritative
- **Evidence**: §5.2, §8, §9. Transaction log is separate from the safe-output manifest; entries carry identifiers and payload hash only; `ledger_mutation` handler is log-only.
- **Confidence**: emerging
- **Quote**: "an audit event is evidence of an attempted or completed mutation, not authorization for that mutation."
- **Our assessment**: Good separation of provenance from authority. Audit failure after a durable append does not fail the append, leaving gaps in the log; the authoritative state is the validated shards.

### Claim 11: Stored memory payloads are a durable prompt-injection channel and must be treated as data, not instructions
- **Evidence**: §9 threat table row "Durable prompt injection through stored payloads".
- **Confidence**: emerging
- **Quote**: "Ledger payloads are untrusted content; consumers MUST treat `ledger_get` and `ledger_query` results as data, never as instructions"
- **Our assessment**: Names a threat many memory features gloss over. Note the countermeasure is a consumer-side obligation the spec cannot enforce; it depends on the agent's prompt discipline and threat detection.

### Claim 12: Integrity is not authenticity: residual risks are accepted, notably semantically false but well-formed records
- **Evidence**: §9 closing paragraph.
- **Confidence**: emerging
- **Quote**: "records are integrity-checked but not authenticated, so a well-formed record proves only that its content hashes correctly, never who authored it"
- **Our assessment**: Candid. A hash chain prevents silent corruption, not a poisoned agent writing plausible lies. Anyone treating ledger contents as ground truth should add provenance and review.

### Claim 13: All limits must be enforced before a mutation is acknowledged, with units converted exactly once
- **Evidence**: §2, §7, §9 (unbounded growth row; silent limit misconfiguration row).
- **Confidence**: emerging
- **Quote**: "Size fields are expressed in KiB in workflow configuration and MUST be converted to bytes exactly once."
- **Our assessment**: Bounded memory is a first-class requirement (record, segment, patch, shard-count). The unit-conversion rule reflects a real bug class (KiB/bytes confusion silently disabling compaction).

## Concrete Artifacts

Job responsibility split (source: §3 table, condensed):

```
Agent job          untrusted  ledger MCP server: ledger_append/get/query/status; no memory-branch write token
Agent post-steps   trusted    merge transaction log into safe-output file (revalidate, redact, dedupe, bound)
Safe-outputs job   trusted    ledger_mutation handler is log-only; no ledger storage access
Persistence job    trusted    restore, DAG reconstruct, compact, retire, normalize, commit+push (contents: write)
```

Record format (source: §2): canonical JSON + newline, fields `version, id, type, timestamp, parents, payload, sha`; `sha` = SHA-256 of canonical record with `sha` omitted; IDs UUIDv4; timestamps canonical UTC ISO 8601.

Threat table (source: §9), representative rows: forged replacement shard to delete history; forged coverage file; truncated-copy overwrite of an existing shard; compacting the run's own writer shard; identity forgery; unbounded growth; path traversal/symlinks; escaping via scripted policy; forged audit entries; agent lines mixed into trusted output; durable prompt injection; pre-creating a replacement shard ID to block compaction; payload/credential leakage via logs; compaction blocking persistence; silent limit misconfiguration.

Conformance test list (source: §10): canonical serialization, hash verification, malformed-line isolation, concurrent-head convergence, configured limits, deterministic compaction, forged/current-run coverage, safe retirement, transaction-log redaction, audit-merge validation, log-only audit handling, limit unit parsing, projection rebuilds.

## Cross-References

- **Corroborates**: `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents execute without write permissions) and Claim 5 (normative security invariants): the ledger applies the same permission separation to memory. `docs-ghaw-threat-detection.md` Claim 1 (detection job between agent and safe outputs): the ledger's §5.5 requires ledger files in the threat-detection artifacts. `docs-ghaw-memory-ops.md` Claim 10 (append-only JSON Lines with rotation) and Claim 11 (no secrets in memory) and `docs-ghaw-repo-memory-reference.md` Claim 11 (repo memory follows repository permissions): the spec states "It MUST NOT be used for secrets" more strongly.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `docs-ghaw-repo-memory-reference.md` Claim 3 ("your changes win" conflict resolution) with the DAG multi-head model and Claim 6 (configuration parameters) with ledger-specific limits; `docs-ghaw-memory-ops.md` patterns 4/5 by supplying the formal guarantees beneath JSONL storage.
- **Novel**: Three-job trust split for memory; declarative-only compaction with the `vm`-is-not-a-boundary rationale; coverage-verified retirement; the durable-prompt-injection-via-memory threat with countermeasures; explicit "integrity is not authenticity" residual risk statement.

## Guide Impact

- **Chapter 04 (Agent State & Memory)**: Add the ledger design as a reference architecture for bounded agent memory: append-only content-hashed records, disposable projection, deterministic compaction, explicit non-guarantees (Claims 1, 2, 8). Cite Claim 12 as a caution that hashed memory is not trusted memory.
- **Chapter 07 / security sections**: Add "memory is an injection and persistence channel" guidance (Claims 4, 11) and the rule that the process consuming untrusted input must not hold the memory-write credential (Claim 3). Cite Claim 5 for not running policy scripts in-process beside privileged credentials.
- **Chapter 02 (Harness Engineering)**: Use Claim 6 as a worked example of assigning fail-open vs fail-closed per pipeline step.
- **Chapter 05 (Coordination)**: Note Claim 8: concurrent agents writing shared memory get convergence, not locking.

## Extraction Notes

- Read the full spec page (single page; no sub-pages followed). Fetched via a summarizing fetch tool asked for verbatim text; quotes were taken from that reproduction and are short contiguous fragments, but the Assayer should verify against the live page.
- The page is a Working Draft; requirements may change.
- The wording of "current-run" in §5.4 vs §9 is ambiguous (see Claim 7).
