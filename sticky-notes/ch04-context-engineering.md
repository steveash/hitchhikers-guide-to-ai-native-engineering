# Sticky Notes: 04 — Context Engineering

Editorial guidance notes for [guide/04-context-engineering.md](../guide/04-context-engineering.md).

Sticky notes capture prescriptive or conditional editorial guidance that the
synthesis agents must respect when updating a chapter. Each note has a unique
ID that is never reused, even after the note is resolved.

## Note Format

```
## SN-04-NNN: Short title
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
| SN-04-001 | §billing-window stays rule-only | prescriptive | active | §billing-window |
| SN-04-002 | Cache breakpoints are harness-controlled in Claude Code | prescriptive | active | §billing-window |
| SN-04-003 | Replace internal implementation jargon with plain language | prescriptive | active | any section citing internal source code |

---

## SN-04-001: §billing-window stays rule-only
- **Created**: 2026-04-15
- **Type**: prescriptive
- **Status**: stale
- **Section**: §billing-window (The billing window is not the inference window)
- **Note**: The billing section must contain only the rule — no failure-case narratives, no token arithmetic, no "cheap per token" cross-references. Reviewer explicitly said "the whole section could just be this rule; all of the above is a waste of time to read" and flagged the section as overly explicit about a secondary concern.

**Why:** Billing details are not the core topic of a context-engineering chapter. Lengthy narratives distract from the primary evidence and inflate read time for a point that can be made in one rule.
**How to apply:** When synthesizing §billing-window, write the **Rule** block only. Do not add supporting failure cases, code blocks with token counts, or cross-references to MCP cost framing.

---

## SN-04-002: Cache breakpoints are harness-controlled in Claude Code
- **Created**: 2026-04-15
- **Type**: prescriptive
- **Status**: stale
- **Section**: §billing-window (The billing window is not the inference window)
- **Note**: In Claude Code specifically, cache breakpoints are set by the harness — not by the frontier model vendor (Anthropic). Do not write "cache breakpoints are determined by the vendor" without qualifying that in Claude Code the harness controls this. The distinction matters because it affects whether users can influence caching behavior through harness configuration.

**Why:** Reviewer corrected a factual error: "cache breakpoints are picked by the harness, not the frontier model vendor (at least in the case of claude code)."
**How to apply:** If §billing-window or any caching section discusses who controls cache breakpoints, attribute that control to the harness (for Claude Code) rather than the vendor in blanket statements.

---

## SN-04-003: Replace internal implementation jargon with plain language
- **Created**: 2026-04-16
- **Type**: prescriptive
- **Status**: active
- **Section**: any section citing internal source code (e.g., from the Claude Code source map leak)
- **Note**: When referencing internal implementation details derived from source code leaks or architecture maps, translate jargon into plain language before including it in the guide. Terms like "cache-break vector with sticky latches" are not meaningful to practitioners without definition; replace with plain equivalents (e.g., "14 distinct ways a cache can be invalidated — with internal guards to prevent accidental busting"). Reviewer said "no clue what that means concretely."

**Why:** The guide audience is practitioners, not Anthropic engineers. Internal naming conventions carry no shared meaning outside their original context.
**How to apply:** After quoting or paraphrasing from leaked source code, read the sentence aloud and ask: "Would a senior engineer who has never seen this codebase understand this in one pass?" If not, replace or define the jargon before publishing.
