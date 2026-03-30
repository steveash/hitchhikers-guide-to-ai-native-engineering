# Editorial Constitution

This document defines the editorial standards for The Hitchhiker's Guide.
Every agent in the pipeline — discovery, extraction, review, synthesis — is
bound by these rules.

## Mission

Produce the fastest path from "I want to use AI coding agents effectively"
to "I am using them effectively" for working software engineers.

Not a survey. Not a taxonomy. Not an overview. A field guide that tells you
what to do, what not to do, and shows you exactly what it looks like.

## Editorial Tenets

### 1. Concrete beats abstract
Every recommendation must be actionable within a single coding session.
"Use progressive disclosure in your CLAUDE.md" is useless without an example.
Show the example. Always.

### 2. Cite everything
No unsourced claims. Every recommendation links to its source note.
Every source note links to the original material. The reader can always
trace a claim back to its origin and judge for themselves.

### 3. Evidence grades are mandatory
Every claim carries a confidence tag: `[settled]`, `[emerging]`, `[anecdotal]`,
`[editorial]`, or `[stale]`. The reader deserves to know how much weight
to put on a recommendation.

### 4. Show the counter-evidence
If sources disagree, say so. "Source A recommends X, but Source B found Y
when they tried it at scale." Suppressing contradictions is editorial malpractice.

### 5. Prescriptive over descriptive
Don't say "there are several approaches." Say "do X. Here's why. If your
situation is Y, do Z instead." The reader came for guidance, not a menu.

### 6. Point-in-time honesty
This guide describes what works *right now*. Tools change monthly.
Recommendations that were solid in January may be wrong in March.
Date your claims. Flag staleness. Never pretend stability.

### 7. Failure reports are first-class sources
"I tried X and it didn't work" is as valuable as "I tried X and it worked."
Often more valuable. Anti-patterns prevent more damage than best practices create.

### 8. Practitioner code over vendor docs
A real CLAUDE.md from a production repo is worth more than ten pages of
vendor documentation. Vendor docs say what's possible. Practitioner code
shows what actually works.

### 9. Small teams count
A 2-person startup's CLAUDE.md is as valid a data point as a Fortune 500's.
Don't filter by prestige. Filter by: did they actually use this in anger?

### 10. Deterministic tools for deterministic work
If a linter, formatter, type checker, or test suite can enforce a rule,
it should not be in a CLAUDE.md file or in this guide as "AI advice."
AI agents are for judgment calls, not mechanical enforcement.

## Anti-Patterns (in our own writing)

### Survey-itis
"There are several popular AI coding tools including..." — NO. The reader
doesn't need a market survey. Name the tool when relevant. Skip the panorama.

### Prompt cargo cults
"Always include 'think step by step' in your prompts" — NO. Cite evidence
or don't include it. "Everybody does it" is not evidence.

### Terminal fanfiction
Invented terminal sessions showing idealized AI interactions that never
happened. If you're showing an interaction, link to the source or say
it's a constructed example.

### Grandiose framing
"AI is transforming the very fabric of software engineering" — NO.
We're writing a practical guide, not a keynote.

### Stale confidence
Presenting 6-month-old claims as current truth. If the source is old
and the space moves fast, flag it as `[stale]` or re-verify.

### Unsourced prescriptions
"You should always restart your session after 20 turns" — says who?
Based on what? Every "should" needs a citation or an explicit `[editorial]` tag.

## Inclusion Bar

A source or claim earns inclusion if it meets ANY of:
- Concrete, reproducible pattern with evidence (code, config, metrics)
- Credible failure report with enough detail to learn from
- Contradiction of an existing guide recommendation (forces re-evaluation)
- Novel pattern not covered by existing source notes

## Exclusion Bar

Reject if ANY of:
- Pure opinion with no supporting evidence or experience report
- Vendor marketing disguised as guidance
- Duplicate of an existing source note (update the existing note instead)
- Theoretical/speculative — "this should work" with no evidence anyone tried it
- Older than 2025-12-01 (pre-agentic-era; the landscape was too different)

## Report Shape

The guide is organized by **practitioner need**, not by tool or vendor:
1. How should I think about this? (principles, mental models)
2. What does a good session look like? (workflows)
3. How do I configure my tools? (harness engineering)
4. How do I avoid disasters? (safety, verification)
5. How do I scale this to a team? (adoption)

Each chapter follows the pattern:
- Lead with the recommendation
- Show a concrete example (code, config, or workflow)
- Cite the source(s)
- Note the confidence level
- Acknowledge counter-evidence if it exists
