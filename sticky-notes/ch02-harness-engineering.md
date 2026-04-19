# Sticky Notes: 02 — Harness Engineering

Editorial guidance notes for [guide/02-harness-engineering.md](../guide/02-harness-engineering.md).

Sticky notes capture prescriptive or conditional editorial guidance that the
synthesis agents must respect when updating a chapter. Each note has a unique
ID that is never reused, even after the note is resolved.

## Note Format

```
## SN-02-NNN: Short title
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
| SN-02-001 | Permission tiers must include concrete examples | prescriptive | active | §permission-architecture |
| SN-02-002 | Context tier hierarchy references settings.json only, not CLAUDE.md | prescriptive | active | §permission-architecture |

---

## SN-02-001: Permission tiers must include concrete examples
- **Created**: 2026-04-16
- **Type**: prescriptive
- **Status**: stale
- **Section**: §permission-architecture (the .claude/settings.json section)
- **Note**: When introducing the three permission levels (deny / check / prompt), define each with a concrete description of what happens at runtime — not just an abstract label. The `check` tier in particular must describe that a PreToolUse hook script runs, can block on non-zero exit, and that Claude Code uses this internally. Reviewer asked "what does this mean, 'check'? is there an example where claude does this today?"

**Why:** Abstract tier names without concrete runtime descriptions leave practitioners unable to decide whether or how to use them.
**How to apply:** For each permission level in the code block, write a description that describes the actual runtime behavior (what fires, who decides, what happens on rejection). Add a sentence after the block that gives a concrete example of the `check` tier in use.

---

## SN-02-002: Context tier hierarchy references settings.json only, not CLAUDE.md
- **Created**: 2026-04-16
- **Type**: prescriptive
- **Status**: stale
- **Section**: §permission-architecture (the .claude/settings.json section)
- **Note**: The context tier hierarchy in the permission architecture section must reference only deterministic settings files (`.claude/settings.json`, `~/.claude/settings.json`). Do not list `CLAUDE.md` as an alternative for the project tier. `CLAUDE.md` is a system-instruction file, not a deterministic permission settings file. Reviewer flagged "project → .claude/settings.json (or CLAUDE.md)" as a category error.

**Why:** Conflating settings.json (deterministic permission enforcement) with CLAUDE.md (instructional prose for the model) confuses practitioners about where permissions are actually enforced.
**How to apply:** In the context tier hierarchy code block, write `project → .claude/settings.json` with no parenthetical. If CLAUDE.md is mentioned elsewhere in the chapter in a different context, that is fine — just not inside the permission tier diagram.
