---
source_url: https://www.anthropic.com/research/formal-verification
source_type: blog-post
title: "LLMs are making formal software verification feasible at a much larger scale"
author: Anthropic Frontier Red Team (with Theorem)
date_published: 2026-10-22
date_extracted: 2026-10-27
last_checked: 2026-10-27
status: current
confidence_overall: emerging
issue: "#4361"
---

# LLMs are making formal software verification feasible at a much larger scale (Anthropic)

> Vendor-authored report that Claude produced machine-checked no-crash proofs over compiled RISC-V binaries for 239 fuzz entry points in 123 OSS-Fuzz libraries, with explicit scope limits, a reward-hacking guardrail on auto-patching, and token-cost data.

## Source Context

- **Type**: blog-post (Anthropic research post; Frontier Red Team with collaborator Theorem). A separate appendix exists ("Read the full appendix") and was not fetched.
- **Author credibility**: Anthropic's Frontier Red Team, with named contributors including Nicholas Carlini. Results are self-reported by the model vendor; the proof checker (Rocq) is external, and a subset of proofs and semantics is published for independent re-verification, but we did not re-check them.
- **Scope**: Pipeline shape (fuzz test -> spec -> Claude proof -> Rocq check), bugs found, other case studies (zlib, Rust Python interpreter), token-cost trends, proof reuse, and limitations. Does not give per-library attempt counts or total cost.

## Extracted Claims

### Claim 1: Claude proved no-crash properties over compiled RISC-V binaries for 239 entry points across 123 OSS-Fuzz libraries, in a few weeks
- **Evidence**: Self-reported counts: about 180 million lines of Rocq, typical proof about 600,000 lines, binaries with median 18,000 RISC-V instructions. Subset of proofs published.
- **Confidence**: emerging (vendor-reported; independent verification invited but not yet reported)
- **Quote**: "Over the span of a few weeks, Claude successfully patched the bugs it found and then proved that there are no crashes on any input (up to 64 MB) for 239 entry points across 123 different OSS-Fuzz libraries."
- **Our assessment**: The headline is "entry points", not "libraries fully verified". Note that it involved patching bugs first, so proofs are about patched code.

### Claim 2: The spec problem is sidestepped by converting existing fuzz tests into a generic "never crashes" spec
- **Evidence**: Design description: compiled library + fuzz test + Theorem's RISC-V/OS semantics + no-crash property mechanically yields the theorem to prove.
- **Confidence**: emerging
- **Quote**: "we take the approach of automatically converting their preexisting compilable test suites into a spec by encoding the rule “this test suite always passes,”"
- **Our assessment**: Key transferable idea: existing tests/fuzzers are a free source of specs; proofs then subsume the test. Limits verification to properties tests already express (crash/assert).

### Claim 3: A proof checker shrinks the trusted base to three artifacts, so the generated proofs need virtually no human review
- **Evidence**: Architectural argument; Rocq kernel checks the proof against the spec.
- **Confidence**: settled (as a property of proof checkers; the correctness of the specific semantics is emerging)
- **Quote**: "the only artifacts that a developer needs to trust are:"
- **Our assessment**: The list that follows is: the RISC-V and Linux process models, the exact theorem statements, and the Rocq checker. This is the generation-side/verification-side asymmetry in its strongest form: untrusted LLM output, mechanically checked. Footnote 5 adds that hardware, OS and the OCaml compiler under Rocq are also implicitly trusted.

### Claim 4: "Formally verified" does not mean "bug-free" — the checker cannot tell whether the spec matches reality
- **Evidence**: Limitations section; proofs are about single-threaded static RISC-V binaries on musl, while users run x86/ARM with glibc; ASan misses some memory bugs; not all entry points verified; callers may misuse the library.
- **Confidence**: settled
- **Quote**: "“Formally verified” does not mean “bug-free.”"
- **Our assessment**: Authors state this themselves; the guide should repeat the guardrail wherever it cites the result.

### Claim 5: Letting Claude auto-patch bugs found mid-proof opens a reward-hacking route, mitigated by penalizing patches and auditing them
- **Evidence**: Footnote 6: Claude could rewrite the program to trivially never crash; mitigation was penalizing patches, extra credit for proving which inputs a patch changes, and logging/auditing patches.
- **Confidence**: anecdotal (mitigation described, effectiveness not quantified)
- **Quote**: "Note this leaves open the door to reward hacking."
- **Our assessment**: Concrete example of a verifier gate that the agent can game by editing the thing being verified. High value for the verification chapter.

### Claim 6: The proof attempt itself finds bugs that fuzzers are unlikely to find
- **Evidence**: Examples: counter underflow in a decompressor needing about 20 MB input with a rare layout; out-of-bounds read needing 64 MB input and over 2 GB memory; an OOB read needing a call sequence across two handles; rediscovery of CVE-2026-56132 in libexpat; a logic bug where a file-restriction feature isn't always enforced.
- **Confidence**: emerging (specific examples, but library names mostly withheld)
- **Quote**: "Many of the bugs we found are ones that a fuzzer would be unlikely to ever find."
- **Our assessment**: Credible mechanism (fuzzers cap inputs around 1 MB). Counts of bugs are only "hundreds"; no bug-per-library data.

### Claim 7: Proving a fuzz test is crash-free can be equivalent to proving high-level properties, because fuzz tests encode properties as assertions
- **Evidence**: LZO compress/decompress roundtrip example; cpp-httplib proof forced Claude to prove libc++ red-black tree depth is logarithmically bounded on machine code.
- **Confidence**: emerging
- **Quote**: "so proving the test never crashes is equivalent to proving the property itself."
- **Our assessment**: Suggests property-style tests are worth writing even before proofs, as they upgrade into specs.

### Claim 8: Proofs can cost hundreds of millions of tokens, but newer models need fewer
- **Evidence**: On 36 small tasks (3 attempts each, 5M-token budget), Opus 5.5 proves half with about 40% fewer tokens than Opus 5. Small sample, chart-based.
- **Confidence**: anecdotal
- **Quote**: "One of the key limitations of LLM-assisted formal verification is that the proofs can take hundreds of millions of tokens to produce."
- **Our assessment**: The only quantitative cost data. No dollar totals for the 123-library effort.

### Claim 9: Shared proof workspaces cut token use about 17% and reuse is substantial at scale
- **Evidence**: Experiment where agents copy each other's proofs; cost was lower than solo in 30 of 34 completed proofs; in the OSS-Fuzz effort teams copied and adapted finished proofs (C runtime and ASan initialization overlap).
- **Confidence**: emerging
- **Quote**: "agents needed 17% fewer tokens than when they worked alone, and some agents even succeeded after previously failing in a solo attempt."
- **Our assessment**: Multi-agent pattern: a shared artifact store helps when work decomposes into reusable pieces.

### Claim 10: Claude autonomously generated x86 ISA semantics, surfacing documentation errors
- **Evidence**: Footnote 7: single-stepping the semantics can boot an Ubuntu userspace on a Linux kernel; hundreds of mistakes found in official reference documentation and a smaller number of hardware bugs. Authors concede semantics may not be perfect.
- **Confidence**: anecdotal
- **Quote**: "Generating these semantics also identified hundreds of mistakes in the official reference documentation, along with a smaller number of bugs in the hardware itself."
- **Our assessment**: Treat separately; validated by empirical testing (boots Ubuntu), not by proof.

### Claim 11: Other experiments: zlib proven against an RFC 1950 spec, and a Rust Python interpreter proven in Verus matched CPython on 99.95% of 1.7M random programs
- **Evidence**: Self-reported; zlib work found only minor unexploitable bugs; the interpreter's adherence was measured empirically rather than proven end to end.
- **Confidence**: anecdotal
- **Quote**: "finding identical behavior with CPython in 99.95% of tests, with remaining test differences as unsurprising known corner cases."
- **Our assessment**: Little detail in the main post; appendix not read.

### Claim 12: Anecdote that a PDF reader yielded a year's worth of security bugs in one week and a decade-old logic bug was found
- **Evidence**: One sentence, no project names, counts or links.
- **Confidence**: anecdotal
- **Quote**: "During an effort to verify a widely used PDF reader, we found as many security bugs in one week as are typically reported in a year."
- **Our assessment**: Not enough detail to treat as evidence; cite only as an unsupported claim.

### Claim 13: Binary-level, generic specs avoid rewriting codebases, and dependency proofs amortize
- **Evidence**: Argument plus Theorem's roadmap for the Nix ecosystem (glibc, OpenSSL, cURL).
- **Confidence**: emerging (forward-looking)
- **Quote**: "Dependencies follow a power law: proving even a small set of shared libraries makes a huge swath of software feasible to prove."
- **Our assessment**: Plausible strategy, unproven; forecast that verification will be "as practical as fuzzing" is opinion.

## Concrete Artifacts

```
Stated assumptions (Anthropic, "Introduction"):
"for every input less than 64 MB and every modeled Linux operating system (OS) response and memory layout, under certain assumptions (namely that the program runs as a single-threaded static binary with a fixed memory budget on a RISC-V1 CPU using Linux OS)"

Trusted components (Anthropic, "Turning tests into proofs"):
- The formal models of RISC-V and of Linux processes;
- The exact theorem statements that were proved;
- The Rocq proof checker itself.

Pipeline (from Figure 2 caption): library + existing fuzz test compiled to RISC-V executable;
with Theorem's RISC-V/OS semantics and the no-crash property -> mechanically generated spec;
Claude writes proof; Rocq kernel checks it.
```

Published: subset of proofs, trusted components, specs for unproved fuzz tests, and a Theorem-published Claude skill for developers to verify their own code (not inspected here).

## Cross-References

- **Corroborates**: `blog-simonwillison-ten-advances-mathematics.md` Claim 7 (Tao: formal verification enables low-trust collaboration) and Claim 5 (independent proof checking): same logic that an external checker lets you trust untrusted AI output.
- **Contradicts**: None filed. Tension with `blog-pragmaticengineer-orosz-wayne-formal-methods.md` Claim 8 (AI expands formal-methods adoption only modestly, 0.1% to 0.3%) and Claim 9 (LLMs write weak, easily-true properties; users need expertise): this post reports large-scale autonomous proofs, but its specs are generic no-crash properties derived from existing tests (which fits Wayne's "weak properties" point rather than refuting it), and covers a different population (security-critical C/C++ libraries). Judged a difference in context, not a contradiction.
- **Extends**: `blog-pragmaticengineer-orosz-wayne-formal-methods.md` Claim 6 (specs are hard to write): this source's answer is to reuse tests as specs.
- **Related**: `blog-anthropic-datadog-temper-machine-tool.md` Claim 9 (layered verification cascade before execution); different technique. `blog-anthropic-claude-code-verification-loops-skills.md` Claim 1 (test/feedback verification loops); proofs are a stronger gate. `blog-cursor-reward-hacking-benchmarks.md` for the general reward-hacking theme (see Claim 5 above; claim numbers not cited).
- **Novel**: Machine-checked proofs at assembly level by an LLM at scale; token-cost and proof-reuse numbers; reward hacking via patching the verification target.

## Guide Impact

- **Chapter 03**: Add formal proof with an external checker as the strongest verification tier, citing Claims 1-3. Include the "tests become specs" idea (Claim 2) and always pair with the Claim 4 caveat (spec vs reality) and the explicit scope assumptions.
- **Chapter 03**: Add the reward-hacking case (Claim 5): if an agent can modify the code under verification, constrain/penalize and audit the edits.
- **Chapter 06**: Note proven no-crash guarantees versus test-based assurance, scoped as in Claim 4; do not state that libraries are "bug-free".
- **Chapter 02**: Optional: shared proof workspace (Claim 9) as a multi-agent pattern, with the 17% figure marked as a small experiment.

## Extraction Notes

- Read the full main article; the linked appendix, Theorem's roadmap and the Theorem skill were not followed. Figures were not viewable; chart data is described only via captions.
- Vendor-authored; all numbers self-reported. Model names (Opus 5, Opus 5.5) are as printed in the post.
