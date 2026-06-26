# Sticky Notes: 05 — Team Adoption

Editorial guidance notes for [guide/05-team-adoption.md](../guide/05-team-adoption.md).

Sticky notes capture prescriptive or conditional editorial guidance that the
synthesis agents must respect when updating a chapter. Each note has a unique
ID that is never reused, even after the note is resolved.

## Note Format

```
## SN-05-NNN: Short title
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
| SN-05-001 | Don't repeat billing details from ch04 | prescriptive | active | §adoption-playbook |
| SN-05-002 | Every Rule block must carry an inline [source:] citation | prescriptive | active | any |
| SN-05-003 | Tag Smith synthesis and prescriptive directives [editorial] | prescriptive | active | any |

---

## SN-05-001: Don't repeat billing details from ch04
- **Created**: 2026-04-15
- **Type**: prescriptive
- **Status**: stale
- **Section**: §adoption-playbook (team rollout checklist)
- **Note**: Billing risk details (inference vs. cache billing, billing CSV exports, session-state caching costs) belong in ch04-context-engineering and must not be repeated in the adoption playbook checklist. Reviewer flagged the billing pilot bullet as "a relatively unimportant comment that you didn't need to repeat in this section" — the word "again" signals they'd already objected to billing overexplanation in ch04.

**Why:** Repeating ch04 content here adds noise to the adoption checklist and signals the Smith is padding rather than synthesizing. Cross-chapter repetition also creates maintenance burden when the billing section changes.
**How to apply:** The Months 1-3 and Months 3-6 checklists should reference billing concerns at most with a one-line pointer ("see §billing-window in ch04") — do not expand into multi-sentence explanations of cache token mechanics.

---

## SN-05-002: Every Rule block must carry an inline [source:] citation
- **Created**: 2026-06-21
- **Type**: prescriptive
- **Status**: active
- **Section**: any
- **Note**: Every **Rule** block must be followed immediately, on its own line, by an inline `[source: <slug>, ...] [grade]` citation — even when the Rule restates a point already cited earlier in the same section. A Rule is a recommendation, and the guide convention is that every recommendation carries its own inline citation.

**Why:** The Rule is the most actionable line in each section; an uncited Rule reads as bare editorial assertion rather than evidence-backed synthesis. Reviewers flagged four Rule blocks across ch02/03/05 in a single PR for missing their inline citations ("the guide convention seen elsewhere in these chapters").
**How to apply:** After writing any `**Rule**:` block, add a citation line on the next line pointing at the source(s) the rule is drawn from, at the appropriate confidence grade. The cited slug must already back the rule's content — do not invent a citation to satisfy the convention; if no source backs the rule, it is `[editorial]`, not a Rule.

---

## SN-05-003: Tag Smith synthesis and prescriptive directives [editorial]
- **Created**: 2026-06-26
- **Type**: prescriptive
- **Status**: active
- **Section**: any
- **Note**: Any sentence or block that is the Smith's own synthesis — a conclusion drawn *across* multiple sources rather than extracted from one — must carry an `[editorial]` tag, even when the underlying sources are cited inline. The same applies to any prescriptive instruction the Smith addresses to the reader (e.g. "Treat it as a hypothesis", "do not drop review depth"): a directive the Smith is asserting, not lifting from a source, is `[editorial]`. Reviewers flagged two such untagged blocks in a single PR — a cross-source synthesis combining Faros + Coinbase, and a prescriptive "treat it as a hypothesis" instruction.

**Why:** Inline `[source:]` cites tell the reader where evidence came from; the confidence grade tells the reader how much to trust it. A synthesis or directive that carries source cites but no grade reads as a directly-extracted, fully-corroborated claim when it is actually the Smith's own reasoning. `[editorial]` is the honest grade for synthesis and authorial directives.
**How to apply:** Before opening the PR, scan for sentences that (a) draw a conclusion the cited sources don't each state on their own, or (b) instruct the reader to do/believe something. If the conclusion or instruction is the Smith's, end the block with `[editorial]`. This is distinct from [[ch05-team-adoption]] SN-05-002: that note is about Rule blocks needing a `[source:]` cite; this one is about synthesis/directive prose needing the `[editorial]` grade.
