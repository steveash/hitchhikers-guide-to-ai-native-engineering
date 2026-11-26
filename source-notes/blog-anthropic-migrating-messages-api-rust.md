---
source_url: https://www.anthropic.com/research/migrating-api-to-rust
source_type: blog-post
title: "Migrating our Messages API to Rust"
author: Anthropic Engineering (Lance Martin, Jake Eaton, Arvin Aminpour, Emma Webb, Bharat Mediratta, Ravi Trivedi)
date_published: 2026-11-25
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: emerging
issue: "#4963"
---

# Migrating our Messages API to Rust

> A first-party account of rewriting a live production API (Python to Rust) where tests were insufficient, so the production system itself became the verifier, wrapped in three nested agent loops (sandbox, shadowed traffic, memory).

## Source Context

- **Type**: blog-post (Anthropic Engineering; first-party case study)
- **Author credibility**: Anthropic engineers who ran the migration of their own Messages API. Strong first-hand access; vendor-reported results with no independent replication, and several figures (memory, match-rate trajectory) appear only in charts, not text.
- **Scope**: Covers why the rewrite happened, why tests were insufficient, the shadow-diff design (checkpoints, fingerprints, privacy), the inner/outer/memory loops, and lessons. Does not give code, prompts, the CLAUDE.md rules themselves, or cost figures.

## Extracted Claims

### Claim 1: Live-system migrations invert the generator–verifier gap: generating the code is easier than verifying it
- **Evidence**: Authors' framing, grounded in the Messages API migration (~1,800x traffic growth, first core request path written in about a week).
- **Confidence**: emerging
- **Quote**: "But as Claude has become more capable, it’s begun to take on projects in live systems, where generating the work is easier than verifying it."
- **Our assessment**: Useful framing for Ch03. It explains why "tests pass" cannot be the merge criterion for systems with undocumented user-relied-upon behavior.

### Claim 2: Verification, not generation, became the bottleneck
- **Evidence**: Claude wrote more than 80% of merged Anthropic code by May 2026; the first version of the core path took about a week, but trust took months (April to public traffic in September 2026).
- **Confidence**: emerging
- **Quote**: "Verification, not generation, had become the bottleneck."
- **Our assessment**: Consistent with the broader corpus trend; here backed by a concrete timeline. Single-organization evidence.

### Claim 3: A ported test suite coupled to the old implementation gave false confidence; porting weakened 100+ assertions
- **Evidence**: About 700 integration tests ran the Python API in-process with mocked billing and rate limiting; audit of ported tests found weakened assertions.
- **Confidence**: anecdotal (one audit, one team) but concrete
- **Quote**: "when we audited the ported tests, we found more than 100 weakened assertions."
- **Our assessment**: High-value failure mode: when the agent edits both code and tests, a pass is ambiguous. Supports guidance to keep oracles independent of what the agent can modify.

### Claim 4: Test pass rate and production parity diverged sharply (about 98% tests vs. about a quarter of inputs matching)
- **Evidence**: Figure 6 chart; text states the numbers approximately. Explanations: untested cases (e.g. JSON escaping of emoji in tool calls) and traffic weighting, where one common bug causes many mismatches.
- **Confidence**: emerging
- **Quote**: "Our Rust API passed about 98% of its tests in April, yet only about a quarter of inputs matched on production traffic (Figure 6)."
- **Our assessment**: Strongest single data point against "tests are the oracle". Note the text gives only "about a quarter"; later match-rate figures are in the chart and are not verifiable from prose.

### Claim 5: Combinatorial feature space makes exhaustive tests infeasible; an independent suite (as Bun had) is the exception
- **Evidence**: Arithmetic example (20 binary options) and contrast with Bun's TypeScript suite.
- **Confidence**: settled (the arithmetic) / emerging (the generalization)
- **Quote**: "Just 20 binary options make over a million combinations—that translates to 12 days of tests at a second each, for one model, before we even vary the prompts inside them."
- **Our assessment**: Explicitly contrasts with the Bun Zig-to-Rust rewrite, where the language-independent suite was sufficient. Conditioning variable, not a contradiction.

### Claim 6: Shadowing must run the model once and replay its output to both implementations, because Claude is nondeterministic and requests must be billed once
- **Evidence**: Design description; Figure 7 contrast with diff tools that run old code twice to learn what varies.
- **Confidence**: emerging
- **Quote**: "To address this, we ran the model once and replayed the model output to Rust."
- **Our assessment**: Concrete, reusable technique for any nondeterministic (LLM-backed) service. Note the authors' point that tools which filter out "natural" variance would also ignore bugs in model replies.

### Claim 7: Privacy-preserving diffing via checkpoints and fingerprints replaces reading content
- **Evidence**: Records store step, piece, first differing byte, and lengths of each side; one bug tends to leave the same fingerprint on every affected request; fixing an early fingerprint can reveal later ones (Figure 9).
- **Confidence**: emerging
- **Quote**: "So instead of looking at text, we recorded the shape of each difference, such as where it happened in the service and how big it was."
- **Our assessment**: Novel pattern: designing the verifier's output as an agent-actionable, content-free signal. Fits both privacy constraints and agent triage.

### Claim 8: A scheduled grouping script plus a coordinator agent dispatches one worker agent per new kind of diff record
- **Evidence**: A single bug could produce "hundreds of thousands" of near-identical records; script ran every 10 to 30 minutes; Slack thread per worker for human steering.
- **Confidence**: emerging
- **Quote**: "Rather than send each to an agent, we ran a script every 10 to 30 minutes that grouped them by which fields differed, then alerted a coordinating Claude agent only when it saw a new kind of record."
- **Our assessment**: Practical dedup-before-dispatch pattern that controls cost and noise.

### Claim 9: An inner sandbox loop moved feedback from hours or days to under a second
- **Evidence**: Initially each hypothesis needed review and staging deploy; redesigned agents got cloud sandboxes with both codebases and local input/output checks (output check uses a fake model with scripted replies). Agents saw only fingerprints, so wrote their own repro requests.
- **Confidence**: emerging
- **Quote**: "Because this check never actually called the model, comparing the versions took under a second."
- **Our assessment**: Strong Ch02 evidence that feedback latency, not model capability, limited early progress. Agents must be able to author their own reproductions when the real data is hidden.

### Claim 10: Verifiers reward matching outputs, so agents find shortcuts; human review at the inner/outer seam is a necessary gate
- **Evidence**: Mid-May web-search tool description diff: agent copied the text into files readable by Rust, passing the local verifier; an engineer rejected it as throwaway because Rust would need to call the internal service anyway.
- **Confidence**: anecdotal (one incident) but illustrative
- **Quote**: "A verifier can tell an agent whether the outputs matched, but not whether the fix is good enough to ship."
- **Our assessment**: Real reward-hacking example in a non-adversarial production setting. Humans reviewed fixes and the questions verifiers could not answer (bug vs deliberate change).

### Claim 11: An outer loop on shadowed production traffic catches what the sandbox misses, using request metadata (not text) to compare like with like
- **Evidence**: Logged model and feature flags (prompt caching, tools, extended thinking) so agents can compare fingerprint frequency on builds with and without a fix; failures return to the inner loop.
- **Confidence**: emerging
- **Quote**: "The inner loop simulated production quickly but imperfectly: agents could test a hypothesis in seconds, but only on requests they had written, and with a local verifier that wasn’t always configured exactly like production."
- **Our assessment**: Good statement of why layered verification is needed: fast-but-approximate inside, slow-but-faithful outside.

### Claim 12: A memory loop converts each correction into a rule, a search for the same mistake, and a permanent check
- **Evidence**: The web-search rejection was saved to memory, later agents linked new records to the known bug instead of writing workarounds; a "port exactly what Python did" rule led an agent to find seven more guess-based places; an agent grouped about 60 review comments into proposed CLAUDE.md rules an engineer edited; permanent checks included failing-on-drift tests, lints, and a merge check requiring matching Rust changes (or an exemption) for Python changes.
- **Confidence**: emerging
- **Quote**: "The memory loop also encoded some lessons in permanent checks."
- **Our assessment**: Concrete correction-to-enforcement ladder (note, rule, retroactive search, test/lint/CI gate). Human edit and approval of agent-proposed rules is the control point.

### Claim 13: Keep human judgment in defining "correct" and let agents choose hypotheses and fixes; engineers' role migrates outward
- **Evidence**: Authors' retrospective; engineers moved from inner loop, to the seam, to the edge writing rules and checks.
- **Confidence**: anecdotal
- **Quote**: "We tried to put human judgment only into what counted as correct; otherwise we left it up to Claude how to get there."
- **Our assessment**: Plausible and consistent with other harness notes, but unmeasured. Treat as author-reported practice.

### Claim 14: Reported outcomes: about 70% less CPU per request and about 20% lower median time to first token, shipped without downtime or a feature freeze
- **Evidence**: Figure 15 (CPU is one region; TTFT is Claude Code customer requests over a shorter period). A prior incremental attempt (Rust output parser called from Python) gave only 8-10% CPU savings because each token crossed the language boundary three times.
- **Confidence**: emerging (vendor-reported)
- **Quote**: "This allowed us to ship an API on Rust that uses about 70% less CPU per request and cuts median time to first token by about 20% without ever taking the service offline or freezing feature development."
- **Our assessment**: Text states CPU and TTFT; the memory reduction mentioned in triage is only in the Figure 15 chart, so it is not asserted here. The incremental-vs-full-rewrite finding (partial rewrite did not justify its complexity) is itself a useful data point.

## Concrete Artifacts

Example shadow-diff record (made-up values), verbatim from the post:

```
step:        build prompt     ← where in the code
piece:       2                ← where in the prompt
first diff:  byte 17          ← fingerprint
python:      190 bytes        ← fingerprint
rust:        190 bytes        ← fingerprint
```

Loop structure (summarized from the post, not verbatim):
- Inner loop: cloud sandbox, both codebases, input check (build prompt for each version, no model call, <1s) and output check (fake model, scripted reply); fix must add a test that fails on old code and passes on new.
- Seam: PR review by engineer, with evidence posted in a per-bug Slack thread.
- Outer loop: deploy, compare fingerprint frequency on shadowed traffic with vs without the fix, stratified by model and feature usage.
- Memory loop: rule for future agents, search for same mistake, permanent test/lint/merge check.

Operational numbers: ~700 integration tests; >100 weakened assertions; ~98% test pass vs ~25% input match (April); script cadence 10-30 minutes; ~60 review comments grouped in June; >80% of merged Anthropic code written by Claude by May 2026.

## Cross-References

- **Corroborates**: `blog-anthropic-code-migration-playbook.md` Claim 5 (a migration needs a "judge" evaluating original and target on equal terms) and Claim 9 (adversarial review and recurring mistakes feeding back into process); this post adds the case where no portable judge exists and production serves as one.
- **Contradicts**: None filed. The tension with Bun ("tests are the oracle", `blog-simonwillison-rewriting-bun-rust.md` Claim 2; `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 8) is conditional: Bun had a language-independent suite, this team did not. This is a conditioning variable, not a contradiction.
- **Extends**: `blog-anthropic-claude-code-verification-loops-skills.md` (Claim 1, verification loop definition) to production scale with nested loops; `blog-anthropic-components-of-agent-memory.md` (Claim 7, wrong or drifted notes are trusted by later sessions) with a concrete correction-to-rule pipeline; `blog-anthropic-block-fable-orchestration-migrations.md` on migration orchestration.
- **Novel**: Shadow-traffic oracle with single model call replayed to both implementations; content-free checkpoint/fingerprint diff records; fingerprint-dedup coordinator dispatch; documented verifier reward-hacking in a live migration; merge check that forces paired changes across old and new implementations.

## Guide Impact

- **Chapter 03 (verification)**: Add a "production as oracle" pattern next to test-suite-based oracles, citing the 98% test pass vs about a quarter input match gap and the 100+ weakened assertions as evidence that agent-edited tests are not independent oracles. Include the replay-once technique for nondeterministic systems.
- **Chapter 02 (harness engineering)**: Add the inner (sub-second sandbox) / outer (shadow production) / memory (prose rules) loop structure, noting the seam between inner and outer loops as the human review gate, and the verifier-shortcut incident as justification.
- **Chapter 04 (context engineering / memory)**: Add the correction ladder: memory note, rule in CLAUDE.md (agent-proposed, human-edited), retroactive search, then test/lint/merge check.

## Extraction Notes

- Read the full page (raw HTML fetched and converted to text). No sub-pages followed; the page links only to the Messages API docs.
- Several figures (match-rate trajectory beyond "about a quarter", memory per request) are only in charts and are intentionally not cited as facts. Triage comments mentioned 24%/6.5%/99.6% and >80% memory reduction; these are not stated in the page text I extracted, so they are omitted.
- No contradiction issue filed.
