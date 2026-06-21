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
| C-004 | Agentic workflow authentication: GITHUB_TOKEN sufficient vs PAT required | 2026-06-12 | resolved | accepted-A |

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

## C-004: Agentic workflow authentication: GITHUB_TOKEN sufficient (June 2026) vs. fine-grained PAT required (May 2026)

- **Filed**: 2026-06-12 by steveash
- **Issue**: #1161
- **Resolved**: 2026-06-21
- **Verdict**: accepted-A
- **Affected guide sections**: Ch02 §Harness Engineering, Ch03 §Safety and Verification, Ch05 §Team Adoption

### Side A
- **Source**: [docs-ghaw-assign-to-copilot](source-notes/docs-ghaw-assign-to-copilot.md)
- **Claim**: The `assign-to-agent` safe output requires a fine-grained PAT; the default GITHUB_TOKEN lacks the necessary permissions, and GitHub App tokens are explicitly not supported.
- **Evidence**: First-party GitHub reference documentation (May 2026), direct statement with verbatim quote: "This safe output requires a fine-grained PAT to authenticate the agent assignment operation. The default `GITHUB_TOKEN` lacks the necessary permissions." Confirmed by the Concrete Artifacts authentication table in the source note showing `DEFAULT GITHUB_TOKEN: ❌ Insufficient`, `FINE-GRAINED PAT: ✅ Required`.
- **Confidence**: settled (as of 2026-05-10 extraction, re-verified 2026-06-21 against live reference page)

### Side B
- **Source**: [docs-github-copilot-aw-github-token-auth](source-notes/docs-github-copilot-aw-github-token-auth.md)
- **Claim**: Agentic workflows can now authenticate using the built-in GITHUB_TOKEN; PATs are no longer required.
- **Evidence**: Official GitHub changelog (June 11, 2026) from the GitHub blog: "You can now use GitHub Agentic Workflows with GitHub Actions's built-in `GITHUB_TOKEN`. This means that you no longer need to create and store a personal access token (PAT)." The changelog discloses `copilot-requests: write` as the enabling mechanism in the workflow frontmatter, described as enabling Copilot AI inference billing.
- **Confidence**: settled (first-party official announcement)

### Resolution

These claims address different architectural layers and are not actually contradictory. The `assign-to-agent` reference page states the PAT requirement verbatim, as captured in [docs-ghaw-assign-to-copilot](source-notes/docs-ghaw-assign-to-copilot.md) Claim 7: "This safe output requires a fine-grained PAT to authenticate the agent assignment operation. The default `GITHUB_TOKEN` lacks the necessary permissions." The singular "This safe output" refers to `assign-to-agent` specifically; the source note's Concrete Artifacts authentication table confirms the required scope (Actions, Contents, Issues, Pull requests — all Write). Side A's requirement stands, scoped to `assign-to-agent`.

(Note on scope: an earlier draft of this entry quoted the page as "Both safe outputs require a fine-grained PAT." That plural wording does not match the source note's captured quote and could not be substantiated against the source note, so the verified singular quote above is authoritative. The PAT requirement documented in this entry applies to `assign-to-agent`; this entry makes no claim about any second safe output. If a future re-verification establishes that a second safe output — e.g. `assign-to-bot` — carries the same requirement, that should be filed as a separate, independently sourced claim.)

Side B's June 2026 changelog introduces GITHUB_TOKEN support for agentic workflows via the `copilot-requests: write` frontmatter permission — this is specifically for **Copilot AI inference billing** (authorizing and paying for LLM calls within a workflow run). This is a different credential layer from the `assign-to-agent` safe output, which requires write access to GitHub Issues and Pull Requests (the GitHub API write layer, routed through the Safe Outputs Processor). Side B's changelog never mentions `assign-to-agent` by name, nor does it address Safe Outputs write-credential requirements.

The guide should preserve the `assign-to-agent` PAT requirement (Side A holds) while clarifying that the June 2026 "no longer need a PAT" announcement refers to the Copilot inference billing layer (`copilot-requests: write`), a separate concern. Additionally, the filer noted a security distinction: PAT-based writes bypass the `github-actions[bot]` non-triggering loop-prevention mechanism (per `docs-ghaw-rate-limiting-controls.md` Claim 2), so workflows using PATs must explicitly guard against trigger loops — this is an important safety note regardless of authentication layering. (Note: this bypass implication is a first-principles inference from platform design, not directly stated in the rate-limiting controls reference — the source note's Extraction Note 4 flags it as "inferred from the platform design — not explicitly stated in the source." It should therefore be synthesized at the appropriate evidence level — inference, not settled platform documentation — rather than presented as a direct documentation statement.)

### Citation in the guide

Ch02 §Harness Engineering should state that `assign-to-agent` workflows require a fine-grained PAT (Actions/Contents/Issues/PRs Write; `GH_AW_AGENT_TOKEN` fallback chain; GitHub App tokens not supported), citing Side A as `[settled]`. Clarify that the June 2026 "no longer need a PAT" announcement covers Copilot AI inference billing only, not Safe Outputs write operations.

Ch03 §Safety and Verification should document the PAT-related loop-prevention bypass: workflows authenticating with a fine-grained PAT (rather than GITHUB_TOKEN) are not subject to the `github-actions[bot]` non-triggering protection, so they must implement explicit loop guards. Cite [docs-ghaw-rate-limiting-controls](source-notes/docs-ghaw-rate-limiting-controls.md) Claim 2 as the source for the bot non-triggering mechanism. Grade the *bypass* itself as an inference (e.g. `[emerging]` or an explicit `[editorial]` inference tag), not `[settled]`: per that note's Extraction Note 4 the bypass is inferred from platform design and is not a direct statement in the rate-limiting controls reference.

Ch05 §Team Adoption should note the June 2026 change as reducing PAT lifecycle management burden for Copilot AI inference billing, acknowledging this as an operational improvement for adoption — while preserving the note that `assign-to-agent` and certain other safe outputs still require PAT provisioning.

---

*This file is updated whenever a `contradiction` issue is resolved. New entries
are appended at the bottom; the index table at the top is updated to match.*
