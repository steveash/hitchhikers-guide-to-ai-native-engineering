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
| SN-02-003 | Split citations when settled facts and emerging inferences share a paragraph | prescriptive | active | any |
| SN-02-004 | Rules with vendor-restricted scope must carry a scope qualifier | prescriptive | active | any |
| SN-02-005 | Every Rule block must carry an inline [source:] citation | prescriptive | active | any |

---

## SN-02-003: Split citations when settled facts and emerging inferences share a paragraph
- **Created**: 2026-05-02
- **Type**: prescriptive
- **Status**: active
- **Section**: any
- **Note**: When a paragraph mixes a `[settled]` factual claim with an `[emerging]` inference derived from that same source, each must carry its own citation line. Do not roll both under a single `[settled]` tag — this overstates the confidence of the inferential sentence.

**Why:** A single `[settled]` citation covering a paragraph that ends with an interpretation (e.g., "this means X is a neutral landing zone") implies the interpretation is as firmly established as the underlying fact. Reviewers caught this pattern twice on the skill-path addition.
**How to apply:** Wherever a paragraph concludes with an inference ("this means...", "this suggests...", "this makes X a..."), give the inferential sentence its own citation line at the appropriate grade. The factual sentence keeps its grade separately.

---

## SN-02-004: Rules with vendor-restricted scope must carry a scope qualifier
- **Created**: 2026-05-02
- **Type**: prescriptive
- **Status**: active
- **Section**: any
- **Note**: When a Rule's applicability is restricted to a specific tool, IDE, or platform (as indicated by Extraction Notes in the source), include a parenthetical qualifier in the Rule text stating the current scope and the unknown. The Rule's confidence tag should reflect the weakest supporting claim.

**Why:** A Rule stated without scope qualification implies broad adoption. The skill-path Rule said "for cross-tool compatibility" when multi-path discovery was confirmed for Visual Studio Copilot only; reviewers flagged this as implying broader adoption than the evidence supports.
**How to apply:** Check the source note's Extraction Notes for scope caveats. If the evidence is IDE/vendor-specific, add "(currently confirmed for X; whether Y adopts the same pattern is not yet documented)" to the Rule text and downgrade to the weakest cited claim's confidence grade.

---

## SN-02-005: Every Rule block must carry an inline [source:] citation
- **Created**: 2026-06-21
- **Type**: prescriptive
- **Status**: active
- **Section**: any
- **Note**: Every **Rule** block must be followed immediately, on its own line, by an inline `[source: <slug>, ...] [grade]` citation — even when the Rule restates a point already cited earlier in the same section. A Rule is a recommendation, and the guide convention is that every recommendation carries its own inline citation.

**Why:** The Rule is the most actionable line in each section; an uncited Rule reads as bare editorial assertion rather than evidence-backed synthesis. Reviewers flagged four Rule blocks across ch02/03/05 in a single PR for missing their inline citations ("the guide convention seen elsewhere in these chapters").
**How to apply:** After writing any `**Rule**:` block, add a citation line on the next line pointing at the source(s) the rule is drawn from, at the appropriate confidence grade. The cited slug must already back the rule's content — do not invent a citation to satisfy the convention; if no source backs the rule, it is `[editorial]`, not a Rule.

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
