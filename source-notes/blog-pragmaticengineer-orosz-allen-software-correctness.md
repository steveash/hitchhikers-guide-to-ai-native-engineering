---
source_url: https://newsletter.pragmaticengineer.com/p/software-correctness
source_type: blog-post
title: "Software correctness & supply chain security, with Sean Allen"
author: Gergely Orosz, interviewing Sean Allen (Antithesis, Pony language)
date_published: 2026-11-10
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: anecdotal
issue: "#4648"
---

# Software correctness & supply chain security, with Sean Allen (The Pragmatic Engineer)

> An interview in which Sean Allen argues that correctness should be pushed into types and checked with stateful "workloads" (e.g. the Bank Test) instead of leaning on late-stage testing; AI is only the framing motivation, and the supply-chain, tech-debt, and "quality is not a gate" arguments sit behind the paywall.

## Source Context

- **Type**: blog-post (paid Pragmatic Engineer "Deepdive", Q&A interview format).
- **Author credibility**: Sean Allen is a distinguished engineer at Antithesis (deterministic simulation testing), a core contributor to the Pony language, and previously worked on confidential computing at Microsoft. Orosz discloses: "Antithesis is a podcast sponsor, but this deepdive is not sponsored by them." Opinions are practitioner opinion; there is no code, config, or metrics in the readable portion.
- **Scope**: Only sections 1-3 and the first line of section 4 are readable. The article's own table of contents lists further sections (quality as a "gate", tech debt, supply chain security, garbage collection, "go slow to go fast"). Those are paywalled and were NOT read; the only content from them in this note comes from the free summary bullets at the top of the article, and is marked as such. The "without saying AI" premise means the AI link is indirect.

## Extracted Claims

### Claim 1: Correctness is best defined as invariants, and people often don't know what they expect upfront
- **Evidence**: Practitioner definition; no data.
- **Confidence**: anecdotal
- **Quote**: "An invariant is a guarantee that my software does what’s expected of it."
- **Our assessment**: Useful framing for agent work: an agent can only be verified against invariants somebody has written down. His observation that "in lots of cases, people don’t know what they expect their software to do upfront" supports spec-before-implementation steps. Pure opinion.

### Claim 2: Exhaustive matching on sum types turns "forgot to handle the new case" bugs into compile errors
- **Evidence**: Explanation of ML-family / Rust sum types and pattern matching; a Rust snippet is shown only as an image.
- **Confidence**: settled (well-known language-design property; the source only explains it)
- **Quote**: "exhaustive matching turns every “forgot to handle the new case” bug into a compilation error."
- **Our assessment**: Directly relevant to agent verification: compiler-enforced exhaustiveness gives agents a deterministic, zero-cost check on cross-file changes. The source does not make the agent connection; that is our inference.

### Claim 3: Verification should happen as early as possible; type systems can encode states and allowed transitions ("make illegal states unrepresentable")
- **Evidence**: Argument from experience; no measurements.
- **Confidence**: emerging
- **Quote**: "With ML languages, you can usually represent within the type system what the states are, and what the allowable transitions are."
- **Our assessment**: Plausible and widely held in the typed-FP community. Implication for agent-written code: choosing languages/types that make invalid states unrepresentable shrinks what tests and reviewers must catch. Untested against agents here.

### Claim 4: Manual testing is the worst verification, and automated tests remain a late-stage activity
- **Evidence**: Opinion; Allen frames Antithesis as "a software verification and correctness company", not a testing company.
- **Confidence**: anecdotal
- **Quote**: "You should do as much as possible before you get to testing."
- **Our assessment**: Rhetorical position from someone selling verification tooling (sponsor disclosure applies). Worth reading as "shift left", not "don't test".

### Claim 5: Literal-minded TDD katas (hard-coding answers to pass example tests) push you into property-based testing, and compilers eliminate many things examples would otherwise test
- **Evidence**: Personal anecdote from pairing katas; engineers paired with him said they'd be "much better at writing tests".
- **Confidence**: anecdotal
- **Quote**: "The moment you randomize inputs, you’re in the land of property-based testing because you’re generating inputs to cover more space than you’d come up with in examples."
- **Our assessment**: The "adversarially literal implementer" is an apt model of how an agent can game example-based tests (it can return hard-coded values). Relevant to reward-hacking worries; the source does not say this.

### Claim 6: A property-based "workload" is inputs plus validation, and purely random operation selection rarely reaches interesting states
- **Evidence**: Key-value store example (GET/PUT/DELETE) and reasoning about odds; no data.
- **Confidence**: emerging
- **Quote**: "Leaving all of this to chance is like walking when drunk: people don’t get very far from where they start."
- **Our assessment**: Strongest technique in the readable text: shaped (biased) generators plus an invariant checker. Applicable to verifying agent-written stateful code where example tests are weak. Adds specificity to the general advice for property-based testing in the Wayne note.

### Claim 7: The Bank Test checks isolation by transferring money between accounts while a checker asserts the total never changes
- **Evidence**: Worked example: $10,000 over 10 accounts of $1,000; transfers in transactions; a concurrent reader should only ever see 10,000. Allen says bugs appear "like crazy" under fault injection (Jepsen/Antithesis-style).
- **Confidence**: settled for the test design (a long-standing Jepsen-style technique); anecdotal for the effectiveness claim as stated here
- **Quote**: "If the isolation guarantees hold, the only value it should ever see is 10,000."
- **Our assessment**: A clean template of "simple workload + one global invariant". Could be proposed as a pattern for validating agent-built transactional code. Note the article is not about agents.

### Claim 8 (free summary only, paywalled body not read): Quality checks as late CI/CD "gates" are less effective than building validation and feedback in from the start
- **Evidence**: None readable; this is the article's own teaser bullet.
- **Confidence**: anecdotal
- **Quote**: "He prefers this to adding CI/CD quality “gates” late in the development process."
- **Our assessment**: Cannot be assessed without the paywalled argument. Note "gate" here means late CI/CD checks, which differs from Ch03's Quality Gates Framework (plan approval, test-on-complete, AGENTS.md), which are in-loop checkpoints; the tension may be mostly terminological. Do not cite as guidance.

### Claim 9 (free summary only, paywalled body not read): Supply-chain attacks have no single or simple fix
- **Evidence**: None readable beyond the teaser.
- **Confidence**: anecdotal
- **Quote**: "There’s no single or simple fix, says Sean."
- **Our assessment**: The teaser attributes this to popular languages assuming a trustworthy ecosystem; the reasoning and any recommendations are behind the paywall. Not usable as guidance.

## Concrete Artifacts

```
Bank Test (Sean Allen, in the article, section 3):
- $10,000 in the system, split across 10 accounts of $1,000
- Workload: transfer money from one account to another inside a transaction
- A separate component constantly queries the total amount of money
- Invariant: the observed total is always 10,000 (isolation holds)
- Run with injected faults (network partitions, killed nodes) to expose bugs
```

```
Workload = Inputs + Validation (key-value store example):
Inputs: GET, PUT, DELETE operations
Validation: how many keys, the key range, how big keys and values can be
```

The Rust sum-type snippet in the article is an image and was not extractable.

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-wayne-formal-methods.md` Claim 7 (property-based testing as the practical lightweight formal technique); `failure-jepsen-particledb-llm-assisted-database.md` Claim 9 (generative testing found many bugs in LLM-assisted database code; same Jepsen-style lineage).
- **Contradicts**: None filed. The "quality is not a gate" teaser (Claim 8) may conflict with `guide/03-verification.md` "Quality Gates Framework", but the argument is paywalled and the term likely differs in meaning (late CI/CD gates vs. in-loop checkpoints), so no contradiction issue was filed.
- **Extends**: `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` (TDD with agents; this adds the point that example-based tests are weaker than randomized/property-based ones); `blog-pragmaticengineer-orosz-mattis-distributed-databases.md` (same publication, distributed-database correctness).
- **Related, not corroborating**: `blog-anthropic-zero-trust-ai-agents.md` for the supply-chain topic; this note does not read that section.
- **Novel**: Type-system-as-verification (exhaustive matching, illegal states unrepresentable), the "workload = inputs + validation" model, and the Bank Test as a concrete invariant template are not covered elsewhere in the corpus.

## Guide Impact

- **Chapter 03**: Consider adding, in Layer 1 (deterministic tools), compiler-enforced exhaustiveness and "illegal states unrepresentable" as checks that cost agents nothing, and, next to property-based testing (see Wayne note Claim 7), the "workload = inputs + validation" pattern with the Bank Test as an example. Evidence is a single interview opinion, so mark as emerging at most.
- **Chapter 03 (gates)**: Do not change the Quality Gates Framework on the strength of this source; revisit only if the paywalled "gate" argument becomes available.
- **Chapter 06**: No change; the supply-chain section is unread.

## Extraction Notes

- The page is paid; the free preview ends mid-section 4. Fetched the page HTML and read all accessible text (sections 1-3, intro, summary bullets). No sub-pages followed (none substantive in the free text).
- The article contains no AI-specific evidence; AI appears only as Orosz's motivation ("AI agents producing more code than ever"), which is the author's framing, not evidence.
- Claims 8 and 9 rest only on the free summary bullets and are labelled as such. Confidence overall is anecdotal: interview opinion, no metrics, sponsor-adjacent guest.
