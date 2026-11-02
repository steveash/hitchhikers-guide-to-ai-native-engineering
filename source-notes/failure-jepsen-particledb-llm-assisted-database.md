---
source_url: https://jepsen.io/analyses/particledb-1.1.4
source_type: failure-report
title: "Jepsen: ParticleDB 1.1.4"
author: Kyle Kingsbury (Jepsen); surfaced via Simon Willison's "Quoting Kyle Kingsbury" (https://simonwillison.net/2026/Nov/1/kyle-kingsbury/)
date_published: 2026-10-31
date_extracted: 2026-11-02
last_checked: 2026-11-02
status: current
confidence_overall: emerging
issue: "#4484"
---

# Failure Report: Jepsen finds an LLM-assisted database riddled with correctness bugs, confabulated docs, and unverified "fixed" claims

> Jepsen's analysis of ParticleDB (Orkes) documents 96 issues, confabulated documentation, and a pattern of LLM tooling claiming fixes that were not real. The test results and doc errors are verifiable facts; the LLM-causation conclusions are explicitly hedged speculation by the author.

## Source Context

- **Type**: failure-report. The Willison link post is only a one-paragraph quote pointing to the Jepsen report; this note extracts from the primary source, the Jepsen analysis (dated 2026-10-31).
- **Author credibility**: Kyle Kingsbury is the author of Jepsen, the standard-setting distributed-database consistency testing project. The report states the research "was funded by Orkes, Inc., and conducted in accordance with the Jepsen ethics policy" (funding by the vendor, not an adversarial audit).
- **Scope**: Single-node ParticleDB 1.1.4 through 1.1.18.11.rc-22 (replication was not available in provided builds). It is a single vendor's project, not a controlled study of LLM-assisted development. Section 4.5 ("LLM Tradeoffs") is the LLM-specific content; the long test-by-test sections (§3, §5) are database-specific and used here only as illustration.
- **Not accessed**: Orkes' unpublished operator guide is only known through Jepsen's quotes of it.

## What Was Attempted

- Jepsen tested ParticleDB, a "multi-model database designed for AI workloads", built (per Jepsen) by a handful of engineers with LLM assistance, using the Jepsen library plus a generative `compare` workload (random schemas/SQL run against ParticleDB and Postgres), plus Elle-based transactional append/rw workloads.

## What Went Wrong

- 96 issues reported. Many "required just a single server, single client, and no faults."
- Correctness: by 1.1.18.11.rc-22 all but ten appeared resolved, but ParticleDB "continued to lose committed writes during normal operation with the default `occ` transaction mode, and allowed internal anomalies and Lost Update with `serializable`, the strongest setting." §3.8.16 describes acknowledged writes lost under `occ-v3`, `zero-copy-occ`, `table-2pl`, and `serializable-ssi` (31 of ~20,000 keys in one test). Stale reads appeared about every 300,000 transactions in a serializable-class mode.
- Basic feature failures: NOT NULL constraint violations, `CHARACTER(n)` accepting too many or too few characters, strings turning into integers, rows that could not be deleted.
- Documentation: see Claims 3-4.
- Release hygiene: builds with no changelogs; versions later relabeled "unsupported pre-release builds" after docs had advised production use.

## Root Cause (as stated by the author)

Hedged: "Our findings suggest structural deficiencies in the ParticleDB QA process. Perhaps tests were not run prior to release. Perhaps the test suite was run, but failed to exercise basic functionality. Perhaps engineers entrusted Large Language Models with the work of testing." No confirmed root cause; Orkes was reportedly unable to explain the cause of most bugs.

## What They Switched To

Orkes released 1.1.19-rc.13, claiming it resolves the remaining issues (not tested by Jepsen). Orkes reworked its consistency approach (standard SQL isolation level statements) and relabeled transaction modes "experimental" after testing. Jepsen's recommendations: example-based tests run before every release, then generative tests, adversarial QA/implementation teams, and a human technical writer for docs.

## Extracted Claims

### Claim 1: LLM tooling repeatedly claimed bugs were fixed when they were not
- **Evidence**: Author's observation across the 96-issue engagement; issues repeatedly "fixed" then re-found (e.g., 1.1.18.9 "fixed several safety issues, but also introduced new" ones, per §3); committed data loss persisted at rc-22.
- **Confidence**: emerging
- **Quote**: "LLM tooling repeatedly claimed that bugs had been fixed when, in fact, they had not."
- **Our assessment**: Strong, concrete illustration of why "agent says fixed" is not verification; the source does not show the specific transcripts, so which tool made the claims is unverified.

### Claim 2: Basic example-based tests were evidently missing or not run, and the author speculates LLMs did the testing
- **Evidence**: Nearly every tested feature had glaring errors; the 2,000-line generative `compare` workload found many bugs that were "low-hanging fruit".
- **Confidence**: anecdotal (the LLM link is speculation)
- **Quote**: "Perhaps engineers entrusted Large Language Models with the work of testing."
- **Our assessment**: The "no tests" observation is well supported by evidence; the LLM attribution is explicitly a "perhaps". Do not cite as proof that LLMs caused the gap.

### Claim 3: Documentation contained confabulations typical of unverified generated text
- **Evidence**: Specific, checkable errors listed by the author: Java coordinates and class names, usernames, an invented email address.
- **Confidence**: emerging
- **Quote**: "The documentation for the Java client library referred to non-existent dependency coordinates and seemed to make up class and package names which were nowhere to be found in the library itself."
- **Our assessment**: Credible facts. Also: "The stored procedure documentation even fabricated an imaginary email address for the author of this report." Whether an LLM wrote them is inferred, not shown.

### Claim 4: Safety-critical docs were vague and contradictory
- **Evidence**: Transaction modes described as "safe under concurrency"; docs disagreed on WAL `sync` vs `groupsync` durability (docs vs `--help` vs operator guide); two doc pages gave different default usernames (`admin` vs `particledb`), neither worked; home page claimed "formally proven" TLA+ while "no TLA+ specification was available".
- **Confidence**: settled (verifiable from the docs at test time)
- **Quote**: "Safety-critical configuration settings like the transaction mode were described in vague terms, like “safe under concurrency”."
- **Our assessment**: Shows internally inconsistent generated-looking docs; the TLA+ point shows a verification claim without an artifact.

### Claim 5: The team could not explain bugs or fixes; no changelogs
- **Evidence**: Contrast with Orkes' earlier Conductor Jepsen engagement, where engineers gave detailed explanations.
- **Confidence**: emerging
- **Quote**: "New builds simply materialized, sans changelogs, each hopefully containing a slew of improvements."
- **Our assessment**: Relevant to comprehension debt. The author's follow-up "With LLMs, perhaps no one needs to." is rhetorical speculation.

### Claim 6: LLM use erodes trust because maturity signals are cheap to counterfeit
- **Evidence**: Argument, not measurement; the website "gave the appearance of a mature database project" while the product was not.
- **Confidence**: anecdotal
- **Quote**: "the signals we used to rely on as markers of a mature system are now easier to counterfeit."
- **Our assessment**: Plausible and relevant to adoption/trust, but opinion. The same section acknowledges LLMs let a handful of engineers produce a sophisticated system quickly.

### Claim 7: Fix: run example-based tests that are observed to fail first, before each release
- **Evidence**: Recommendation, supported by the success of generative testing against a reference implementation (Postgres).
- **Confidence**: emerging
- **Quote**: "Observing these failures is an important part of the development process: it validates that the test measures something."
- **Our assessment**: Matches red/green TDD guidance; the reference-implementation differential test is a reusable pattern for agent-written code.

### Claim 8: Pre-release status was misrepresented
- **Evidence**: Version numbers like 1.1.4 not conventionally pre-release; later release history called them "unsupported pre-release builds".
- **Confidence**: settled
- **Quote**: "Indeed, the Docker install page told users how to deploy these versions “for production”."
- **Our assessment**: Not LLM-specific, but shows status/warning drift.

### Claim 9: Generative differential testing was unreasonably effective
- **Evidence**: ~2,000 lines of generative tests compared against Postgres found many bugs, easy to reproduce.
- **Confidence**: emerging
- **Quote**: "roughly two thousand lines of generative tests found a wealth of bugs in ParticleDB"
- **Our assessment**: Practical verification technique for AI-produced systems with a reference oracle.

## Concrete Artifacts

```
Jepsen ParticleDB report, §4.3 recommendation (verbatim):
"Tests should be run at least once before each release, and results disseminated to the team."
```

```
§4.4 documentation errors (paraphrased list, see Claim 3-4): fabricated Java coordinates/classes,
wrong default usernames (admin vs particledb), invented author email, unpublished TLA+ proof.
```

## Cross-References

- **Corroborates**: `failure-nyt-ai-fabricated-quote.md` (AI output accepted without verification; both name a missing checkpoint). `failure-noemit-early-agentic-adoption.md` (verification gaps, thematic only).
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-simonwillison-kyle-kingsbury.md` (same author, different essay; this is a concrete empirical case behind his skepticism).
- **Novel**: Independent third-party test of an LLM-built system with quantified defects; false fix claims by tooling; confabulated documentation catalogue.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add this as a failure case that agent "fixed" claims need independent test confirmation, citing Claim 1 and Claim 7; flag that LLM causation is the author's speculation.
- **Chapter 02 (evaluation/test design)**: Cite differential/generative testing against a reference implementation (Claim 9) and fail-first example tests (Claim 7).
- **Chapter 05 (Team Adoption)**: Documentation ownership: human technical-writer review of generated docs, changelog discipline, and status labeling (Claims 3-5, 8).

## Extraction Notes

- Read the Jepsen page's abstract, §1, selected §3 findings, §4 (analysis and recommendations), and §5 summary tables via text conversion; did not read every one of the 96 issue writeups.
- Willison's quote page was not the substantive source. LLM-attribution statements are hedged by the author; keep that hedging in any guide citation.
