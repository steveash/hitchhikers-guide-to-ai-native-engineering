# Sticky Notes: 03 — Safety and Verification

Editorial guidance notes for [guide/03-safety-and-verification.md](../guide/03-safety-and-verification.md).

Sticky notes capture prescriptive or conditional editorial guidance that the
synthesis agents must respect when updating a chapter. Each note has a unique
ID that is never reused, even after the note is resolved.

## Note Format

```
## SN-03-NNN: Short title
- **Created**: YYYY-MM-DD
- **Type**: prescriptive | conditional
- **Status**: active | resolved | stale
- **Section**: §section-name (what part of the chapter this applies to)
- **Condition**: (conditional notes only) the condition under which the note applies
- **Note**: the editorial guidance
- **Resolved**: (resolved notes only) YYYY-MM-DD — one-line reason
```

## Index

| ID | Title | Type | Status | Section |
|----|-------|------|--------|---------|
| SN-03-001 | Benchmark data without a practitioner rule belongs in source notes, not the guide | prescriptive | active | any section presenting benchmark results |

---

## SN-03-001: Benchmark data without a practitioner rule belongs in source notes, not the guide
- **Created**: 2026-04-16
- **Type**: prescriptive
- **Status**: active
- **Section**: any section presenting benchmark results
- **Note**: Do not include a benchmark table or dataset in the guide unless it produces a generalizable rule that practitioners can act on. Presenting data + caveats alone ("here are the numbers, but the vendor ran the study, results may vary") is not useful — the lesson "don't trust benchmarks" is obvious to the target audience. Reviewer said "i find this section useless; there is no clear lesson other than to not trust benchmarks which is obvious."

**Why:** The guide's job is practitioner-actionable synthesis, not data presentation. A benchmark that only supports "be skeptical" should stay in the source note. If the data does produce a rule (e.g., "LLM-only review misses >50% of vulnerabilities; anchor it with static analysis"), lead with the rule and trim the data to one supporting sentence.
**How to apply:** Before including any benchmark or study result, ask: "What is the practitioner rule this data justifies?" If the answer is only "be skeptical of benchmarks," cut the section. If there is a concrete rule, state the rule first, then cite the data in one sentence.
