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

---

## SN-05-001: Don't repeat billing details from ch04
- **Created**: 2026-04-15
- **Type**: prescriptive
- **Status**: stale
- **Section**: §adoption-playbook (team rollout checklist)
- **Note**: Billing risk details (inference vs. cache billing, billing CSV exports, session-state caching costs) belong in ch04-context-engineering and must not be repeated in the adoption playbook checklist. Reviewer flagged the billing pilot bullet as "a relatively unimportant comment that you didn't need to repeat in this section" — the word "again" signals they'd already objected to billing overexplanation in ch04.

**Why:** Repeating ch04 content here adds noise to the adoption checklist and signals the Smith is padding rather than synthesizing. Cross-chapter repetition also creates maintenance burden when the billing section changes.
**How to apply:** The Months 1-3 and Months 3-6 checklists should reference billing concerns at most with a one-line pointer ("see §billing-window in ch04") — do not expand into multi-sentence explanations of cache token mechanics.
