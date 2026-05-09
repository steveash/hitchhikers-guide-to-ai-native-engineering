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
| SN-03-002 | Inline citation grade must match the per-claim grade in the source note | prescriptive | active | any inline `[source: <slug>, Claim N] [grade]` citation |

---

## SN-03-001: Benchmark data without a practitioner rule belongs in source notes, not the guide
- **Created**: 2026-04-16
- **Type**: prescriptive
- **Status**: active
- **Section**: any section presenting benchmark results
- **Note**: Do not include a benchmark table or dataset in the guide unless it produces a generalizable rule that practitioners can act on. Presenting data + caveats alone ("here are the numbers, but the vendor ran the study, results may vary") is not useful — the lesson "don't trust benchmarks" is obvious to the target audience. Reviewer said "i find this section useless; there is no clear lesson other than to not trust benchmarks which is obvious."

**Why:** The guide's job is practitioner-actionable synthesis, not data presentation. A benchmark that only supports "be skeptical" should stay in the source note. If the data does produce a rule (e.g., "LLM-only review misses >50% of vulnerabilities; anchor it with static analysis"), lead with the rule and trim the data to one supporting sentence.
**How to apply:** Before including any benchmark or study result, ask: "What is the practitioner rule this data justifies?" If the answer is only "be skeptical of benchmarks," cut the section. If there is a concrete rule, state the rule first, then cite the data in one sentence.

## SN-03-002: Inline citation grade must match the per-claim grade in the source note
- **Created**: 2026-05-09
- **Type**: prescriptive
- **Status**: active
- **Section**: any inline `[source: <slug>, Claim N] [grade]` citation
- **Note**: When a source note assigns different confidence grades to different claims (e.g., Claim 1 = emerging, Claim 2 = anecdotal), the inline citation in the guide must use the per-claim grade, not the source's `confidence_overall`, not a default, and not a heuristic downgrade. Open the source note, find the specific claim, and copy its `Confidence:` field verbatim.

**Why:** The confidence ladder in §7 of agents/SMITH.md depends on each citation accurately reflecting how strongly that specific claim is supported. Defaulting to `[anecdotal]` for first-party Anthropic research that the source note grades `emerging` understates the evidence and misleads the reader. Reviewer caught two such mismatches on blog-anthropic-ai-accelerated-offense (Claims 1 and 7 both graded emerging in the note, but cited as anecdotal in the guide).
**How to apply:** Whenever you write or revise a `[source: <slug>, Claim N] [grade]` citation, open `source-notes/<slug>.md`, locate the matching `### Claim N:` block, and use the grade from its `**Confidence**:` field. If a single citation references multiple claims with different grades, either split the citation or use the lower of the two grades and explain in prose.
