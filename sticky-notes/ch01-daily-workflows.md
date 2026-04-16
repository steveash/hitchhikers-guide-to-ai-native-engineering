# Sticky Notes: 01 — Daily Workflows

Editorial guidance notes for [guide/01-daily-workflows.md](../guide/01-daily-workflows.md).

Sticky notes capture prescriptive or conditional editorial guidance that the
synthesis agents must respect when updating a chapter. Each note has a unique
ID that is never reused, even after the note is resolved.

## Note Format

```
## SN-01-NNN: Short title
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
| SN-01-001 | Keep obvious recommendations concise | prescriptive | active | §task-size-threshold |

---

## SN-01-001: Keep obvious recommendations concise
- **Created**: 2026-04-15
- **Type**: prescriptive
- **Status**: active
- **Section**: §task-size-threshold
- **Note**: When a recommendation is self-evident to the target audience (e.g. "skip the agent for micro-tasks you can execute in 10 seconds"), state it in one tight paragraph — not multiple paragraphs with a supporting quote and editorial wrap-up. Reviewer flagged three paragraphs on an obvious task-sizing point as a waste of the reader's time.

**Why:** Belaboring obvious points erodes the chapter's signal-to-noise ratio and signals the Smith is padding.
**How to apply:** Before finalizing any subsection, ask: "Would an experienced engineer find this obvious?" If yes, cap at 3-4 sentences and drop supporting quotes unless they add nuance not in the prose.
