---
source_url: https://developers.googleblog.com/catch-go-bugs-that-fuzzing-misses-with-gemini-and-a-constraint-solver/
source_type: blog-post
title: "Catch Go bugs that fuzzing misses with Gemini and a constraint solver"
author: Karl Weinmeister (Director, Developer Relations, Google)
date_published: 2026-11-12
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: emerging
issue: "#4701"
---

# Catch Go bugs that fuzzing misses with Gemini and a constraint solver

> An LLM (Gemini 4 Argon) translates the bounds-check traps that survive Go's optimizer into Z3 queries, and `go test` replays any `sat` input as a real crash; the post also documents a systematic fuzzing blind spot (slice capacity vs. length) with a one-line fix.

## Source Context

- **Type**: blog-post (Google Developers Blog, Nov. 12, 2026)
- **Author credibility**: Karl Weinmeister leads Google's agent skills program (175 skills) and wrote `skill-lint`, the Go CLI used as the real-world target. Single-author practitioner report with a vendor angle (Gemini 4 Argon); sample sizes are small (6 buggy functions, 3 planted bugs, 1 real project).
- **Scope**: Covers the pipeline (Go source + RISC-V disassembly -> Z3 script -> `go test` replay), a fuzzing baseline on planted bugs, and results on five functions from `skill-lint`. Does not cover races/deadlocks, whole-binary verification, or non-bounds bug classes.

## Extracted Claims

### Claim 1: An LLM can translate surviving `runtime.panicBounds` traps (from disassembly) into Z3 queries, and a `go test` replay makes every reported crash real even though the translation is unsound
- **Evidence**: Pipeline run on 3 planted-bug parsers and 5 `skill-lint` functions; author reports the first `sat` assignment for all six buggy functions triggered a real panic. Argon translation took ~a minute per function; Z3 finished in milliseconds.
- **Confidence**: emerging
- **Quote**: "An LLM-written solver model isn't a sound proof system, but it gives the agent an independent way to reason about control flow and synthesize concrete Go reproducers, and every crash it finds is real because go test runs the offending bytes directly."
- **Our assessment**: Strong design pattern: an unreliable generator (LLM) paired with a cheap, deterministic, ground-truth oracle (`go test` replay), so false positives are impossible by construction. The weakness is the false-negative side: `unsat` only means "maybe correct". Evidence is small-N and author-run.

### Claim 2: Passing both source and disassembly exposes information the source hides (eliminated bounds checks, 8-bit truncation)
- **Evidence**: Worked example `ParseTwoChunkFrame`: `total := hdrLen + bodyLen` wraps at uint8 (`MOVBU`), visible in RISC-V but easy to read past in source. Z3 produced a 59-byte counterexample (hdrLen=48, bodyLen=236; sum wraps 284 -> 28).
- **Confidence**: emerging
- **Quote**: "Looking at Go source alone, you can't see which bounds checks the compiler already removed or where a register gets truncated to 8 bits; in the disassembly, both show up."
- **Our assessment**: Plausible and demonstrated on one worked example. The author also notes a representation-change argument: an LLM reading source sees `int(total)+4 > len(buf)` as a "textbook bounds check".

### Claim 3: `go test -fuzz` has a systematic blind spot for slice-bounds bugs because Go checks slices against capacity, and fuzz inputs usually carry spare capacity
- **Evidence**: 10-second probe: 386,741 fuzz calls, 89% were views into a shared ~100 MB buffer, only 0.07% had `cap == len`. Unseeded fuzzing (Go 1.27.3, fresh cache each run) missed `ParseTwoChunkFrame` (a crash reachable by 19.4% of header pairs at 59 bytes) in one 3 s run and three 60 s runs; also missed `ExtractQuotedToken`.
- **Confidence**: emerging
- **Quote**: "Go checks a slice expression like buf[endHdr:endBody] against the slice's capacity, not its length, and Go's fuzzer rarely passes a slice without spare capacity."
- **Our assessment**: Mechanism is clearly stated and measured; independently checkable by anyone with Go 1.27. Note it is a property of Go's slice semantics and the fuzzing engine's buffer reuse, so it may not transfer to other languages.

### Claim 4: Clipping capacity to length in the fuzz harness fixes the blind spot
- **Evidence**: After the change the fuzzer crashed both overrun bugs in all three runs (median 0.28 s and 0.17 s). The third planted bug (signed int8 length, negative index) was found either way, acting as a control.
- **Confidence**: emerging
- **Quote**: "Clipping capacity to length with a full slice expression turns any slice past len into a panic:"
- **Our assessment**: Cheap, immediately actionable, and arguably the most transferable takeaway for agent-written fuzz harnesses. Three runs per condition is a thin sample, but the effect (never found vs. always found within <1 s) is large.

### Claim 5: Solver-based checking is worth the extra minute only after the compiler's prover and a clipped-capacity fuzz run have been tried
- **Evidence**: Author's recommended workflow; for helpers extracted from file I/O, a 3-second fuzz run also caught all three `skill-lint` bugs.
- **Confidence**: emerging
- **Quote**: "For most Go code, fuzzing pure helpers with slice capacity clipped to length will catch bounds bugs in seconds."
- **Our assessment**: Honest tiering of tools. It also quietly limits the novelty claim: on extracted helpers, plain fuzzing did equally well, so the solver's distinct value is the `unsat` signal and bugs fuzzing can't reach.

### Claim 6: Whole programs are too big for the solver; apply it to pure functions extracted per Functional Core, Imperative Shell
- **Evidence**: A 10-line parser links 1,559 runtime symbols; the 28 MB `skill-lint` binary has 32,321 symbols. I/O, CLI flags, and network were left to `go test -fuzz` and `-race`.
- **Confidence**: emerging
- **Quote**: "Following Functional Core, Imperative Shell, I left CLI flags, network calls, and file I/O to go test -fuzz and go test -race, and ran the solver only on pure functions and slice helpers extracted from file-reading code."
- **Our assessment**: A concrete architectural constraint that makes verification tractable; it also suggests agent-friendly code structure (pure cores) as a verification enabler.

### Claim 7: Modular checking requires the target to include its own entry-point guards, or Z3 invents out-of-precondition inputs
- **Evidence**: Author's explanation for zero false positives: each extracted helper included its entry guards.
- **Confidence**: anecdotal
- **Quote**: "If an internal helper assumes preconditions that are only enforced by its caller or stated in a doc comment, Z3 will happily invent inputs that violate them."
- **Our assessment**: Important operational caveat, but the replay oracle would not rescue this case (a replayed crash would be "real" yet out of contract). Worth noting for any "extract and verify" agent workflow.

### Claim 8: Real-project yield: three latent bugs in `skill-lint`, all "accounting errors" about slice state changing under edits
- **Evidence**: Of five functions, two scanners returned `unsat` (including a CRLF splitter with six surviving checks); three had bugs: overlapping chunks in `ApplyReplacementChunks` (sorting by StartLine does not prevent overlap), per-violation line checks invalidated by shrinking deletions in the local fixer, and a flat 100-byte reserve for a ~70-byte wrapper plus path in the prompt packer overshooting a 2 MB budget. One bug is latent (the fixer only returns one chunk today).
- **Confidence**: emerging
- **Quote**: "Z3 immediately returned sat because sorting by StartLine doesn't prevent two chunks from overlapping."
- **Our assessment**: The bug in the LLM-edit applier is notable: code that applies LLM-generated line edits is itself a bug surface. One caveat: the author found the bugs in their own code with their own method; no independent confirmation.

### Claim 9: The result is robust to the model leaning on source comments
- **Evidence**: Rerun with all comments stripped; same three bugs caught, `unsat` on the two scanners and all three patches.
- **Confidence**: anecdotal
- **Quote**: "To make sure Argon wasn't leaning on source comments in my test files, I also reran the skill-lint targets with all comments stripped; Argon and Z3 still caught all three bugs and returned unsat on the two scanners and all three patches."
- **Our assessment**: A reasonable leakage control, though the planted-bug tests were written by the same author who judges them.

### Claim 10: Constraint-solver `unsat` is a "maybe correct" signal, and the approach does not cover concurrency
- **Evidence**: Explicit limits stated by the author.
- **Confidence**: settled (as a statement of limits)
- **Quote**: "Like a Bloom filter for bugs, an unsat answer only means \"maybe correct.\""
- **Our assessment**: Correct and candid. Concurrency is explicitly deferred: "Single-threaded solver models don't see data races or deadlocks, so concurrent code still belongs with the race detector, deterministic concurrency testing, and Go 1.27's goroutine leak profiles."

### Claim 11: Changing representation helps an agent see bugs that staying in the target language hides
- **Evidence**: Argument from the worked examples (uint8 wrap; spare capacity hiding crashes), not measured independently.
- **Confidence**: anecdotal
- **Quote**: "Asking the agent to translate Go and assembly into a constraint solver forces a change of representation that strips away surface syntax and makes every bit width and slice bound explicit, while go test turns any solver hit back into a concrete Go reproducer."
- **Our assessment**: An interesting framing ("make the agent re-express the problem in a formalism") but a hypothesis here rather than a tested result.

## Concrete Artifacts

Attributed to Karl Weinmeister, Google Developers Blog, 2026-11-12.

Compile command to list surviving bounds checks:

```
GOOS=linux GOARCH=riscv64 go build -gcflags="-S -d=ssa/check_bce/debug=1"
```

Fuzz harness fix (capacity clipping):

```go
f.Fuzz(func(t *testing.T, data []byte) {
	data = data[:len(data):len(data)] // cap == len: slicing past the end now panics
	ParseTwoChunkFrame(data)
})
```

Planted bug `ParseTwoChunkFrame` (uint8 sum wraps before the length guard):

```go
func ParseTwoChunkFrame(buf []byte) ([]byte, []byte) {
	if len(buf) < 4 || buf[0] != 0xA5 || buf[1] != 0x5A {
		return nil, nil
	}
	hdrLen, bodyLen := buf[2], buf[3]
	total := hdrLen + bodyLen
	if int(total)+4 > len(buf) {
		return nil, nil
	}
	endHdr := 4 + int(hdrLen)
	endBody := endHdr + int(bodyLen)
	return buf[4:endHdr], buf[endHdr:endBody]
}
```

Z3 query generated by Argon for that trap (excerpt):

```python
s = z3.Solver()
length, capacity = z3.BitVecs("length capacity", 64)
b0, b1, hdrLen8, bodyLen8 = z3.BitVecs("b0 b1 hdrLen8 bodyLen8", 8)
wrapped_sum64 = z3.ZeroExt(56, hdrLen8 + bodyLen8) + z3.BitVecVal(4, 64)
end_hdr64 = z3.BitVecVal(4, 64) + z3.ZeroExt(56, hdrLen8)
end_body64 = end_hdr64 + z3.ZeroExt(56, bodyLen8)
s.add(z3.UGE(length, 4), z3.ULE(length, 64), capacity == length)
s.add(z3.UGT(end_body64, capacity))  # panic at 0x0092
```

Key numbers: 386,741 fuzz calls in the probe; 89% views of a shared ~100 MB buffer; 0.07% with `cap == len`; 19.4% of (hdrLen, bodyLen) pairs crash at 59 bytes; median time-to-crash after the fix 0.28 s and 0.17 s; ~1 min per function for the LLM translation, milliseconds for Z3; 3 planted + 3 latent bugs found; 1,559 runtime symbols linked by a 10-line parser.

## Cross-References

- **Corroborates**: `blog-anthropic-llm-formal-software-verification-at-scale` (Claim 6: the proof attempt finds bugs fuzzers are unlikely to find) – this post supplies a concrete mechanism (capacity-vs-length) for one such class of miss. Also consistent with that note's Claim 2 (fuzz-test harnesses reused as the "never crashes" spec) since this post's harness-level fix is a fuzz-harness change.
- **Contradicts**: None filed. The post contrasts itself with Anthropic's approach (lighter, unsound SMT vs. checked Rocq proofs), but that is a trade-off of rigor vs. cost, not an opposing claim; compare Anthropic Claim 3 (proof checker shrinks the trusted base) and Claim 4 ("formally verified" is not "bug-free"), where this post trades the former for a replay oracle.
- **Extends**: `blog-anthropic-llm-formal-software-verification-at-scale` (Claim 1: RISC-V binary-level no-crash properties) by scaling the idea down to single functions with SMT, ~1 minute each, and by targeting Go.
- **Related**: `blog-google-go-ai-assisted-engineering` (Claim 11: Go native fuzzing as an agent self-hardening tool) – this post shows a limit of that default: unclipped fuzz harnesses miss slice-overrun bugs. `blog-google-adk-gemini-4-argon-overnight-optimization` uses the same model (Gemini 4 Argon) with a different, non-verification use; no overlapping claims.
- **Novel**: The capacity-vs-length fuzzing blind spot and its one-line fix; the LLM-as-translator-to-Z3 plus test-replay oracle pattern; the "entry-point guards" requirement for modular solver checks.

## Guide Impact

- **Chapter 03 (verification)**: Add the pattern "unreliable generator + deterministic replay oracle" with this post as an example where false positives are eliminated by construction, with the stated limit that `unsat` is not a proof. Add the fuzz-harness tip (clip `cap` to `len` in Go) as a concrete caveat to recommendations that agents rely on fuzzing for self-hardening (cf. `blog-google-go-ai-assisted-engineering` Claim 11).
- **Chapter 03**: In any discussion of formal verification at scale (citing `blog-anthropic-llm-formal-software-verification-at-scale`), add this as a lighter-weight, lower-assurance alternative, noting the trade (no proof, minute-scale per function).
- **Chapter 02 (harness engineering)**: Secondary: agent drives external tools (compiler flags, disassembler, Z3, `go test`) and relies on extracted pure functions for tractability.

## Extraction Notes

- Read the full post from the raw page (HTML stripped to text) so quotes are verbatim from the source. No sub-pages followed; the post links to Anthropic's article (already in the corpus) and `theorem-labs/oss-verify`, which were not fetched.
- The post's date is Nov. 12, 2026. Results are author-reported and not independently reproduced; the Gemini 4 Argon translation step is non-deterministic and was not reported across repeated runs.
- Cross-referenced claim numbers were checked against the headings in the cited notes.
