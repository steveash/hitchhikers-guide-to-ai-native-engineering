---
source_url: https://simonwillison.net/2026/Nov/11/aws-emulator/
source_type: blog-post
title: "aws-emulator (link post) + AWS Emulator and the engineer's job when agents write the code"
author: Simon Willison (link post); Swaminathan Sivasubramanian, guest post on Werner Vogels' blog (primary source)
date_published: 2026-11-11
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: emerging
issue: "#4690"
---

# aws-emulator (and the AWS guest post it links to)

> AWS describes an agent-built local emulator of 200+ AWS services whose build loop is spec (Smithy API models) + oracle (real AWS) + fidelity tests + a merge gate with adversarial security-review agents, plus a first-person account of the engineer's job shifting to building specs, tests, and gates. All figures are vendor-stated.

## Source Context

- **Type**: blog-post. Simon Willison's link post (https://simonwillison.net/2026/Nov/11/aws-emulator/, ~3 short paragraphs) plus the primary source it links, the guest post https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html (1,671 words, 11 Nov 2026). Both were read in full.
- **Author credibility**: Willison is a high-signal independent commentator on LLM tooling; his post adds only the 29,684-commit figure and one usage caveat. Sivasubramanian is an AWS executive writing at the product launch, so the guest post is vendor marketing with first-hand engineering anecdotes. It links to a launch post by Matt Goldberg and a public GitHub repo, neither of which was fetched.
- **Scope**: Covers the emulator's build method, guardrails, and the author's framing of the engineer's role. It gives no quantitative quality data (no fidelity pass rates, defect counts, or review catch rates), no swarm topology, and no human-review process beyond "an engineer built the scaffolding".

## Extracted Claims

### Claim 1: AWS released an official local emulator of its services, written in Rust by a large agent swarm, with 29,684 commits in its first three weeks
- **Evidence**: Willison's statement; the commit count is not sourced in his post. The guest post says the full commit history is public in the GitHub repository (not checked by us).
- **Confidence**: anecdotal
- **Quote**: "It's written in Rust by a huge swarm of agents - 29,684 commits in the first three weeks of the project."
- **Our assessment**: Plausible but a volume metric, not a quality metric. The guest post itself never states the Rust language or the commit count, so those two facts rest on Willison alone. Cursor's swarm note shows commit volume can be dominated by conflict churn, so the number says little by itself.

### Claim 2: The build loop is spec + real-service oracle + fidelity tests: agents first make each test pass against real AWS, then build the emulator until it passes the same test
- **Evidence**: Description of method, with an SQS visibility-timeout example. Public Smithy API models serve as the written spec and the AWS cloud as the reference.
- **Confidence**: emerging
- **Quote**: "The agents correct each test until it passes against real AWS, so the test records how AWS behaves."
- **Our assessment**: This is the strongest transferable idea: differential testing against a ground-truth oracle turns "clone this system" into a verifiable task, which meets the "simple, verifiable success criterion" condition Cognition says most swarm demos rely on. It only works where a real oracle and a machine-readable spec exist.

### Claim 3: A single prompt to Kiro produced a passable first SQS emulator in about 15 minutes, and the prototype grew into the full emulator
- **Evidence**: Anecdote from the originator, Matt Goldberg (relayed second-hand).
- **Confidence**: anecdotal
- **Quote**: "when he gave Kiro one prompt describing this approach, it returned a passable first version of an SQS emulator in about 15 minutes."
- **Our assessment**: A believable prototype-speed data point, but "passable" is undefined. Note the guest post itself says turning the prototype into a robust solution "took much more work".

### Claim 4: All code was agent-written and agent-tested, built from 400+ API models covering 200+ services, with teams of agents continuously testing against real AWS
- **Evidence**: Vendor assertion; the public repo is offered as verification.
- **Confidence**: emerging
- **Quote**: "All of AWS Emulator’s code was written and tested by agents, and it is built from more than 400 API models covering more than 200 AWS services."
- **Our assessment**: Scale claim is checkable via the public repo, which we did not inspect. The honest-gaps signal is useful: a "things-that-do-not-work" folder in the repo reportedly records behaviours that do not yet match real AWS (guest post's launch section).

### Claim 5: Every change passes a merge gate of automated checks including several adversarial security-review agents, alongside a general code reviewer and deterministic checks restricting what agents may touch
- **Evidence**: Description of the guardrail stack; no catch-rate metrics.
- **Confidence**: emerging
- **Quote**: "Every change goes through a merge gate, a deep bench of automated checks that every change must pass before it enters the codebase, including several security agents doing adversarial reviews."
- **Our assessment**: Consistent with the multi-lens review pattern elsewhere in the corpus. The mix of probabilistic agent review and deterministic path restrictions is worth recording as a design pattern; effectiveness is unquantified.

### Claim 6: The engineer's job when agents write code is to give agents room to work and to build the specs, tests, and merge gates that decide when work is correct
- **Evidence**: Author's synthesis from the emulator and a personal anecdote.
- **Confidence**: emerging
- **Quote**: "the engineer’s job is to give them room to work on their own and to build the specs, tests, and merge gates that decide when that work is correct."
- **Our assessment**: A clean statement of the "harness over code" thesis from a prominent practitioner, but it is opinion backed by one project and one anecdote.

### Claim 7: An agent supervised for four nights failed because it had no way to check its results; with a spec and test environment the same rebuild took about two hours (versus about four months by hand)
- **Evidence**: First-person anecdote (rebuilding the Alf replication engine with Kiro). Single case, no controls; the "four months" original and the two-hour rebuild are not like-for-like (the human had to invent the design).
- **Confidence**: anecdotal
- **Quote**: "I supervised the agent for four nights before I saw that it had no way to check its results."
- **Our assessment**: Memorable failure-then-fix story supporting "give the agent a feedback oracle first". Treat the 4 months → 2 hours ratio as marketing-grade, not a benchmark.

### Claim 8: Putting realistic infrastructure inside the agent's write-run-read loop lets agents check their own work and get code right on the first attempt more often
- **Evidence**: Reasoning only; no measurement given.
- **Confidence**: anecdotal
- **Quote**: "an agent can check its own work as it writes and produce correct code on its first attempt far more often, which improves software quality."
- **Our assessment**: Directionally sound (local, free, offline test targets also remove cost and credential friction, the point Willison highlights), but "far more often" is unquantified.

### Claim 9: The scaffolding that runs the agents was built quickly by one engineer, but hardening it was much harder
- **Evidence**: Brief statement.
- **Confidence**: anecdotal
- **Quote**: "An internal version came together over a weekend and started gaining adoption within a month."
- **Our assessment**: Suggests the harness, not the model, is where the engineering effort concentrates, but the guest post gives no detail on the orchestration (topology, parallelism, human review), so this is a gap rather than a finding.

### Claim 10: Practical limitation: the emulator currently needs Docker on macOS and Windows
- **Evidence**: Willison's observation.
- **Confidence**: settled (as of 11 Nov 2026)
- **Quote**: "It currently requires Docker to run on macOS or Windows."
- **Our assessment**: A concrete constraint for anyone planning to use it as a test dependency; Willison hopes for a single binary.

## Concrete Artifacts

```
Fidelity-test loop (paraphrased from the guest post; no code given):
1. Public Smithy API models  -> spec of operations, inputs, outputs, errors
2. Agent writes end-to-end customer-scenario test from the model
   (example: SQS received message hidden until visibility timeout expires)
3. Agent iterates the test until it PASSES against real AWS (oracle)
4. Agent builds emulator until it passes the same test
5. A still-failing test = gap in the emulator
```

```
Guardrails named in the guest post:
- fidelity tests verified against real AWS
- merge gate: multiple security agents (each reviewing a different attack angle) + a general code reviewer
- deterministic checks preventing agents from touching code they should not
Release: code under CC0; full commit history and agent-filed issues public;
"things-that-do-not-work" folder lists known behaviour gaps.
```

## Cross-References

- **Corroborates**: `blog-cursor-agent-swarm-model-economics.md` Claim 10 (stacked, varied review lenses catch more) matches the multi-agent security review in the merge gate. `blog-cognition-multi-agents-working.md` Claim 4 argues large swarm demos work because they share a simple, verifiable success criterion; the real-AWS fidelity-test oracle is such a criterion. `blog-cognition-multi-agents-working.md` Claim 5 (a separate reviewer agent catches bugs before humans) is a parallel pattern.
- **Contradicts**: None found; no contradiction issue filed.
- **Extends**: `blog-cursor-agent-swarm-model-economics.md` and `blog-cognition-multi-agents-working.md` with a non-Cursor, non-Cognition large-scale agent build, though with far less orchestration detail than the Cursor report.
- **Novel**: Spec-plus-live-oracle differential testing as the basis for an agent-built service clone; an official vendor emulator as agent test infrastructure; the "agent had no way to check its results" anecdote with its two-hour recovery.

## Guide Impact

- **Chapter 03 (verification)**: Add the fidelity-test pattern (tests validated against a real reference system, then used as the target for agent-built code) as an example of oracle-based verification, and note that local emulators give agents a free, offline test target. Flag as vendor-stated, emerging.
- **Chapter 02 (harness engineering)**: Cite the guardrail stack (oracle tests, adversarial multi-agent merge gate, deterministic path restrictions) as a concrete harness example; state that orchestration details are not disclosed.
- **Chapter 00 (principles)**: Optionally cite the quoted statement of the engineer's role (specs, tests, merge gates) as a practitioner articulation; do not use the commit count or the 4 months → 2 hours ratio as evidence of productivity.

## Extraction Notes

- Fetched raw HTML of both pages and read the text in full; quotes were copied from the extracted text. Curly apostrophes are preserved.
- Not followed: Goldberg's launch post and the GitHub repo (not linked with a URL in the extracted text). The commit count and Rust claim are unverified.
- The Prospector marked this low priority; the link post is thin, and the guest post carries the substance. All substantive claims are vendor-stated.
