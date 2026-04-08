# Contradictions Log

A public ledger of contradictions found between sources in the Hitchhiker's
Guide corpus, and how each was resolved.

This file exists because **suppressing contradictions is editorial malpractice**
(see [Editorial Constitution](EDITORIAL-CONSTITUTION.md), Tenet 4). When two
sources disagree, the reader deserves to know. When the guide picks a side, the
reader deserves to know which side won and why.

## How Contradictions Get Here

1. The **Miner** spots a contradiction during extraction (a new source disagrees
   with an existing source note, or a source disagrees with itself).
2. The Miner files a `contradiction` issue using the
   [contradiction issue template](.github/ISSUE_TEMPLATE/contradiction.yml).
3. A human (or the Smith, working with a human) resolves the contradiction:
   accept side A, accept side B, present as debated, or mark unresolved.
4. The resolved entry is appended to this file with full provenance.
5. The Smith uses this file when synthesizing chapters — debated points get
   the `**Debated:**` treatment described in [SMITH.md](agents/SMITH.md#5-handle-contradictions-explicitly).

A contradiction without a CONTRADICTIONS.md entry is not resolved. It is just
an open issue.

## Resolution Verdicts

| Verdict | Meaning |
|---------|---------|
| `accepted-A` | Side A's claim is the guide's position. Side B is documented as counter-evidence. |
| `accepted-B` | Side B's claim is the guide's position. Side A is documented as counter-evidence. |
| `debated` | Evidence is too thin or context-dependent to pick a winner. The guide presents both sides. |
| `superseded` | One side's evidence has been overtaken by newer or stronger evidence. |
| `unresolved` | Filed and acknowledged, awaiting more evidence or human decision. Do NOT cite either side as settled until resolved. |

## Entry Format

Every entry follows this shape:

```markdown
## C-NNN: [Short title of the contradiction]

- **Filed**: YYYY-MM-DD by [agent or human]
- **Issue**: #NNN
- **Resolved**: YYYY-MM-DD (or `unresolved`)
- **Verdict**: accepted-A / accepted-B / debated / superseded / unresolved
- **Affected guide sections**: ChNN §Topic (or `none yet`)

### Side A
- **Source**: [source-note-name](source-notes/source-note-name.md)
- **Claim**: [one-sentence statement of the claim]
- **Evidence**: [what backs it up]
- **Confidence**: settled / emerging / anecdotal

### Side B
- **Source**: [source-note-name](source-notes/source-note-name.md)
- **Claim**: [one-sentence statement of the claim]
- **Evidence**: [what backs it up]
- **Confidence**: settled / emerging / anecdotal

### Resolution
[1–3 paragraphs explaining the verdict. Why did one side win? Or why is this
debated? What did the resolver weigh? If `superseded`, what's the newer evidence?
If `unresolved`, what would it take to resolve?]

### Citation in the guide
[How the guide should cite this going forward. Example:
"Cite Side A as [emerging] in Ch02 §CLAUDE.md sizing. Note Side B as
counter-evidence in the same section."]
```

Every field is mandatory except `Affected guide sections` (which may legitimately
be `none yet` if the contradiction is filed before any chapter touches the topic).

## Contradiction IDs

IDs are sequential: `C-001`, `C-002`, ... Assigned at filing time. Once assigned,
an ID is permanent — never reused, never renumbered. Closed/superseded entries
stay in this file with their original ID.

## Index

| ID | Title | Filed | Status | Verdict |
|----|-------|-------|--------|---------|
| C-001 | CLAUDE.md sizing: brief vs verbose | 2026-04-08 | resolved | debated |
| C-002 | AGENTS.md role: redirect target vs identical mirror | 2026-04-08 | resolved | accepted-A |
| C-003 | AI productivity at the org level: individual vs organizational gains | 2026-04-08 | resolved | debated |

---

## C-001: CLAUDE.md sizing: brief vs verbose

- **Filed**: 2026-04-08 by hitchhiker/polecats/rust (seed entry)
- **Issue**: N/A (seed — pre-dates contradiction issue template)
- **Resolved**: 2026-04-08
- **Verdict**: debated
- **Affected guide sections**: Ch02 §Harness Engineering

### Side A
- **Source**: [practitioner-nikolays-postgres-dba](source-notes/practitioner-nikolays-postgres-dba.md)
- **Claim**: Concise CLAUDE.md files (≈30 lines) work well; brevity prevents
  agents from skipping sections they deem irrelevant.
- **Evidence**: A working SQL repo with a ~30-line CLAUDE.md governing a
  cross-version PostgreSQL CI matrix.
- **Confidence**: anecdotal

### Side B
- **Source**: [practitioner-supabase-supabase-js](source-notes/practitioner-supabase-supabase-js.md)
- **Claim**: A 931-line CLAUDE.md is the primary entry point; verbosity is
  warranted when the repo spans multiple tools (Claude, Cursor, Warp) and
  needs documentation-constellation linking.
- **Evidence**: Production TypeScript SDK with a 931-line CLAUDE.md plus 5
  supporting docs.
- **Confidence**: anecdotal

### Resolution

Both repos are real, both work, both authors are credible practitioners. The
brevity vs verbosity choice appears to track repo type: a single-language,
single-purpose repo can survive on 30 lines; a multi-tool, multi-doc SDK needs
more. The
[failure-claudemd-ignored-compaction](source-notes/failure-claudemd-ignored-compaction.md)
report adds pressure on the verbose side — long CLAUDE.md files degrade harder
under context compaction — but does not invalidate Supabase's choice, since the
failure mode is *prose-rule reliability*, not *file length per se*.

This is a context-dependent judgment call, not a settled rule. The guide
should present both, anchored to repo characteristics rather than a line count.

### Citation in the guide

Ch02 §CLAUDE.md sizing should present this as a `**Debated:**` block citing
both sources with `[anecdotal]` confidence. Add the compaction failure as
counter-evidence against the verbose side, with the caveat that the failure
mechanism is prose enforcement, not file size. Do not prescribe a number.

---

## C-002: AGENTS.md role: redirect target vs identical mirror

- **Filed**: 2026-04-08 by hitchhiker/polecats/rust (seed entry)
- **Issue**: N/A (seed — pre-dates contradiction issue template)
- **Resolved**: 2026-04-08
- **Verdict**: accepted-A
- **Affected guide sections**: Ch02 §Harness Engineering

### Side A
- **Source**: [practitioner-getsentry-sentry](source-notes/practitioner-getsentry-sentry.md)
- **Claim**: AGENTS.md should be the single source of truth, with CLAUDE.md
  as a thin `@AGENTS.md` redirect.
- **Evidence**: Sentry's production setup: thin CLAUDE.md → AGENTS.md redirect,
  context-aware subdirectory guides, 16 domain skills, `agents.toml` for
  cross-tool sharing.
- **Confidence**: emerging (Sentry-scale practitioner repo)

### Side B
- **Source**: [practitioner-dadlerj-tin](source-notes/practitioner-dadlerj-tin.md)
- **Claim**: CLAUDE.md and AGENTS.md should be identical copies of one another.
- **Evidence**: tin's repo keeps both files in sync as duplicates.
- **Confidence**: anecdotal

### Resolution

Side A wins on maintainability grounds. The duplicate-mirror approach (Side B)
forces every edit to be applied twice; the redirect approach (Side A) has a
single source of truth and lets each tool resolve the redirect itself. Side B's
own source note flags the duplication as "simpler but less maintainable."
[paper-gloaguen-agentsmd-effectiveness](source-notes/paper-gloaguen-agentsmd-effectiveness.md)
weakly supports Side A by showing that LLM-generated context files hurt
performance — manual maintenance of two copies is the failure mode that paper
implicitly warns against.

The guide should recommend the redirect pattern. The mirror pattern is not
*wrong* in small repos, but it does not generalize and should not be
prescribed.

### Citation in the guide

Ch02 §Multi-tool config should recommend the AGENTS.md-as-source-of-truth +
CLAUDE.md-as-redirect pattern as `[emerging]`, citing
`practitioner-getsentry-sentry`. Note the mirror pattern as a simpler
alternative for small repos with `[anecdotal]` confidence, citing
`practitioner-dadlerj-tin`, but flag the maintenance cost.

---

## C-003: AI productivity at the org level: individual vs organizational gains

- **Filed**: 2026-04-08 by hitchhiker/polecats/rust (seed entry)
- **Issue**: N/A (seed — pre-dates contradiction issue template)
- **Resolved**: 2026-04-08
- **Verdict**: debated
- **Affected guide sections**: Ch05 §Team Adoption

### Side A
- **Source**: [research-anthropic-ai-transforming-work](source-notes/research-anthropic-ai-transforming-work.md)
- **Claim**: Both individual and organizational productivity rise with heavy
  AI adoption (60% of work uses Claude at Anthropic; autonomous tool calls
  doubled Feb→Aug 2025).
- **Evidence**: Mixed-methods study at Anthropic — 132 surveys, 53 interviews,
  200k Clio-analyzed transcripts.
- **Confidence**: emerging

### Side B
- **Source**: [blog-faros-claude-code-roi](source-notes/blog-faros-claude-code-roi.md)
- **Claim**: Individual output increases dramatically but organizational
  delivery stays flat — the productivity paradox.
- **Evidence**: Faros's measurement framework + a "Team A 5% vs Team B 60%:
  47% more PRs daily but 35% longer review times" case.
- **Confidence**: emerging

### Resolution

This is genuinely debated and the resolution is "it depends on organizational
structure." Anthropic's anomaly is its environment: small teams, fast deploys,
an internal release loop running 60–100 deployments/day. That's exactly the
kind of structure where individual productivity converts cleanly to
organizational throughput (no review-time bottleneck, no PR-queue depth, no
cross-team coordination tax). Faros's case study shows the opposite structure:
PR queue depth grows because review capacity does not scale with author
output. The two findings are not contradictory once you condition on
organizational shape.

The guide should present this as debated and surface the *mediating variable*
(organizational structure) so readers can predict which regime they're in.

### Citation in the guide

Ch05 §Measuring AI ROI should present this as a `**Debated:**` block. Cite
both sources at `[emerging]`. Lead with the conditioning variable — review
capacity and deploy cadence — rather than picking a winner. Reference
[paper-miller-speed-cost-quality](source-notes/paper-miller-speed-cost-quality.md)
as additional evidence that the organizational picture is more pessimistic
than the individual one.

---

*This file is updated whenever a `contradiction` issue is resolved. New entries
are appended at the bottom; the index table at the top is updated to match.*
