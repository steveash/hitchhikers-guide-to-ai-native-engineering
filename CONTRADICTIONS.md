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
| C-004 | slash_command trigger: recommended HITL mechanism vs. near-zero success rate | 2026-05-12 | resolved | debated |
| C-005 | Agentic workflow authentication: GITHUB_TOKEN sufficient vs PAT required | 2026-06-12 | resolved | accepted-A |
| C-006 | Context anxiety model version: Opus 4.5 eliminated it vs. Opus 4.5 still had it | 2026-04-20 | resolved | debated |
| C-007 | Human-attacker prompt-injection success: near-100% (role-confusion study) vs. 0/6,000 (hackmyclaw challenge) | 2026-06-29 | resolved | debated |
| C-008 | Copilot CLI auto routing: availability-only (April) vs. task-aware (July) | 2026-07-03 | resolved | superseded |

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

## C-004: slash_command trigger: recommended HITL mechanism vs. near-zero success rate

- **Filed**: 2026-05-12 by Miner agent (during extraction of issue #381)
- **Issue**: #681
- **Resolved**: 2026-06-21
- **Verdict**: debated
- **Affected guide sections**: Ch02 §Harness Engineering (trigger taxonomy, HITL interaction patterns); Ch03 §Safety and Verification (human-in-the-loop design)

### Side A
- **Source**: [docs-ghaw-chatops](source-notes/docs-ghaw-chatops.md)
- **Claim**: The `slash_command` trigger is a first-class, recommended mechanism for human-in-the-loop interactions in gh-aw workflows, with role-based access control, event filtering, and sanitized input handling.
- **Evidence**: First-party official gh-aw ChatOps documentation. Documents the full trigger schema, six `events:` filter values, roles-based runtime access control, and `steps.sanitized.outputs.text` sanitization pattern. Includes working production examples (Grumpy Code Reviewer, /review workflow).
- **Confidence**: settled (design intent and feature existence)

### Side B
- **Source**: [docs-ghaw-editors-reference](source-notes/docs-ghaw-editors-reference.md)
- **Claim**: The `slash_command` trigger has near-zero success rate across all configurations (n=204); practitioners should use `issues + workflow_dispatch` instead for user-initiated workflows.
- **Evidence**: Empirical analysis of 679 gh-aw workflows by the Agentic Prompt Generator (community tool by Ashley Wolf). n=204 for `slash_command`. Dataset composition and "success" definition not disclosed.
- **Confidence**: anecdotal (community tool's analysis; sample may be biased toward misconfigured or template-copied workflows)

### Resolution

This contradiction sits at the boundary between design documentation and empirical community outcome data. The `slash_command` trigger is unambiguously the platform's intended mechanism for human-initiated (ChatOps) workflows — the official docs describe its schema, access control model, and sanitization semantics in detail, with production examples. The community empirical data (n=204, near-zero success) is a meaningful signal that cannot be dismissed, but its methodology is undisclosed: the definition of "success," the sample composition, and whether failures reflect trigger defects or misconfiguration are all unknown.

The most plausible mediating variable is configuration complexity. The `slash_command` trigger requires correct specification across `name:`, `events:` (six values with non-obvious semantics), `roles:`, and the `steps.sanitized.outputs.text` access pattern. Template-copied or minimally-adapted workflows are likely to fail. The `docs-ghaw-dispatch-ops.md` note establishes `workflow_dispatch` as a simpler, fork-safe alternative with parameterization support — the Side B recommendation to use `issues + workflow_dispatch` may be sound advice for simpler HITL scenarios without implying the `slash_command` trigger is fundamentally broken.

The guide should present both sides, anchor on the mediating variable (configuration complexity), and withhold a definitive recommendation until the platform team confirms whether the community failure rate reflects a known limitation or a common misconfiguration pattern. Until then, the guide can honestly say: "The official mechanism is `slash_command`; community empirical data suggests near-zero success in practice, likely due to configuration complexity. If you use it, follow the official ChatOps documentation exactly; if you need a simpler alternative, `issues + workflow_dispatch` is the documented fallback."

### Citation in the guide

Ch02 §Harness Engineering trigger taxonomy and Ch03 §HITL interaction patterns should present this as a `**Debated:**` block:

- Cite `docs-ghaw-chatops.md` Claim 1 as `[settled]` for the assertion that `slash_command` exists and is designed for HITL use. Describe the full configuration (roles, events, sanitized input) from that note.
- Cite `docs-ghaw-editors-reference.md` Claim 5 as `[anecdotal]` for the near-zero community success rate (n=204). Note the undisclosed methodology.
- Present `workflow_dispatch` (`docs-ghaw-dispatch-ops.md`) as the documented simpler alternative for human-initiated invocation, with fork-safety and parameterization advantages.
- Do NOT present `slash_command` as settled guidance until the contradiction is resolved. Do NOT recommend avoiding it entirely without stronger evidence of a platform-level failure rather than a configuration complexity problem.

---

## C-005: Agentic workflow authentication: GITHUB_TOKEN sufficient (June 2026) vs. fine-grained PAT required (May 2026)

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

These claims address different architectural layers and are not actually contradictory. The human resolver re-fetched the live `assign-to-agent` reference page on 2026-06-21 and confirmed it still states verbatim: "Both safe outputs require a fine-grained PAT. The default `GITHUB_TOKEN` lacks the necessary permissions" (Actions, Contents, Issues, Pull requests — all Write). Side A's requirement stands.

Side B's June 2026 changelog introduces GITHUB_TOKEN support for agentic workflows via the `copilot-requests: write` frontmatter permission — this is specifically for **Copilot AI inference billing** (authorizing and paying for LLM calls within a workflow run). This is a different credential layer from the `assign-to-agent` safe output, which requires write access to GitHub Issues and Pull Requests (the GitHub API write layer, routed through the Safe Outputs Processor). Side B's changelog never mentions `assign-to-agent` by name, nor does it address Safe Outputs write-credential requirements.

The guide should preserve the `assign-to-agent` PAT requirement (Side A holds) while clarifying that the June 2026 "no longer need a PAT" announcement refers to the Copilot inference billing layer (`copilot-requests: write`), a separate concern. Additionally, the filer noted a security distinction: PAT-based writes bypass the `github-actions[bot]` non-triggering loop-prevention mechanism (per `docs-ghaw-rate-limiting-controls.md` Claim 2), so workflows using PATs must explicitly guard against trigger loops — this is an important safety note regardless of authentication layering.

### Citation in the guide

Ch02 §Harness Engineering should state that `assign-to-agent` workflows require a fine-grained PAT (Actions/Contents/Issues/PRs Write; `GH_AW_AGENT_TOKEN` fallback chain; GitHub App tokens not supported), citing Side A as `[settled]`. Clarify that the June 2026 "no longer need a PAT" announcement covers Copilot AI inference billing only, not Safe Outputs write operations.

Ch03 §Safety and Verification should document the PAT-related loop-prevention bypass: workflows authenticating with a fine-grained PAT (rather than GITHUB_TOKEN) are not subject to the `github-actions[bot]` non-triggering protection, so they must implement explicit loop guards.

Ch05 §Team Adoption should note the June 2026 change as reducing PAT lifecycle management burden for Copilot AI inference billing, acknowledging this as an operational improvement for adoption — while preserving the note that `assign-to-agent` and certain other safe outputs still require PAT provisioning.

---

## C-006: Context anxiety model version: Opus 4.5 eliminated it vs. Opus 4.5 still had it

- **Filed**: 2026-04-20 by Miner agent (during extraction of issue #192)
- **Issue**: #232
- **Resolved**: 2026-06-22
- **Verdict**: debated
- **Affected guide sections**: Ch04 §Context Engineering, Ch02 §Harness Engineering

### Side A
- **Source**: [blog-anthropic-harnessing-claude-intelligence](source-notes/blog-anthropic-harnessing-claude-intelligence.md)
- **Claim**: Opus 4.5 exhibited no context anxiety; context-reset harness components became dead weight by Opus 4.5.
- **Evidence**: Single illustrative sentence in a first-party Anthropic post (Lance Martin, April 2026). Corroborated by `blog-anthropic-scaling-managed-agents` Claim 1, which explicitly pairs Sonnet 4.5 (exhibited context anxiety) with Opus 4.5 (behavior gone).
- **Confidence**: emerging (two corroborating first-party Anthropic sources; claim is illustrative rather than primary; task profiles not specified)

### Side B
- **Source**: [blog-anthropic-harness-long-running](source-notes/blog-anthropic-harness-long-running.md)
- **Claim**: Opus 4.5 exhibited context anxiety in multi-hour production builds, requiring sprint decomposition; Opus 4.6 eliminated the behavior.
- **Evidence**: First-person production engineering retrospective (Prithvi Rajasekaran, Anthropic Labs, March 2026). Cost data, harness evolution tables across two domains, explicit "compaction alone wasn't sufficient" finding for Opus 4.5 on 3+ hour runs.
- **Confidence**: emerging (primary observation with production metrics; multi-hour continuous coding harness as the task profile)

### Resolution

This contradiction is most plausibly explained by a task-duration mediating variable. Two Anthropic engineering sources (Side A corroborated by managed-agents) document that Opus 4.5 eliminated context anxiety in their operational context. One Anthropic engineering source (Side B) documents Opus 4.5 still exhibiting context anxiety in multi-hour continuous coding builds. The behavior appears to be context-saturation-threshold-dependent: Opus 4.5 raised the threshold enough that typical tasks no longer trigger it, while genuinely extended runs (2+ hours of continuous context accumulation) still crossed it. Opus 4.6 appears to have eliminated the behavior across regimes. Neither post explicitly conditions on task duration, so both accounts are internally consistent with this explanation.

Practitioners should not treat "safe to remove context-reset logic" as universally true at Opus 4.5. The answer depends on whether your task profile resembles the managed-agents operational context (where Opus 4.5 was safe) or Prithvi's multi-hour continuous coding harness (where Opus 4.5 still required sprint decomposition). If you upgrade to Opus 4.5 and run primarily short sessions, Side A evidence suggests you may safely remove context resets. If you run extended multi-hour continuous builds, Side B documents that Opus 4.5 still required them, and only Opus 4.6 made them truly unnecessary.

### Citation in the guide

Ch04 §Context Engineering should present context anxiety as a real, named failure mode (premature task wrap-up as context window approaches saturation) documented by first-party Anthropic sources and third-party practitioners. Include a `**Debated:**` block on the model-version question:

- Cite `blog-anthropic-scaling-managed-agents` Claim 1 and `blog-anthropic-harnessing-claude-intelligence` Claim 15 as `[emerging]` for the claim that Opus 4.5 eliminated context anxiety relative to Sonnet 4.5 in typical operational contexts.
- Cite `blog-anthropic-harness-long-running` Claims 7–8 as `[emerging]` for the claim that Opus 4.5 still exhibited context anxiety in multi-hour continuous builds, with Opus 4.6 as the model where it was eliminated.
- State the conditioning variable explicitly: "The safe model version for removing context-reset logic is task-profile-dependent. For typical shorter sessions: Opus 4.5 evidence suggests context anxiety is eliminated. For extended multi-hour continuous builds: documented evidence shows Opus 4.5 still required sprint decomposition; Opus 4.6 is the safe floor."
- Do NOT cite either claim as `[settled]` for when context-reset components become unnecessary.
- Cite `blog-cursor-continual-harness-improvement` Claim 9 as `[anecdotal]` third-party corroboration that context anxiety is a real cross-vendor harness concern.

Ch02 §Harness Engineering should cite the meta-principle (prune harness components at each model upgrade) from both `blog-anthropic-harness-long-running` Claim 9 and `blog-anthropic-harnessing-claude-intelligence` Claim 15 as `[emerging]`. Tag the specific Opus 4.5 vs. Opus 4.6 trigger point as `**Debated:**` pending resolution, with the task-profile conditioning variable surfaced.

---

*This file is updated whenever a `contradiction` issue is resolved. New entries
are appended at the bottom; the index table at the top is updated to match.*

## C-007: Human-attacker prompt-injection success: near-100% (role-confusion study) vs. 0/6,000 (hackmyclaw challenge)

- **Filed**: 2026-06-29 by Miner agent (during extraction of issue #1429)
- **Issue**: #1443
- **Resolved**: 2026-07-02
- **Verdict**: debated
- **Affected guide sections**: Ch06 §Security and Threat Model (model-layer vs. environmental defenses against prompt injection)

### Side A
- **Source**: [blog-simonwillison-prompt-injection-role-confusion](source-notes/blog-simonwillison-prompt-injection-role-confusion.md)
- **Claim**: Human red-teamers deliberately exploiting role confusion achieve near-100% attack success against frontier models; automated attacks still succeed 11%/25% of the time against Opus 4.5/GPT-5.4 (May 2026); without genuine role perception, injection defense remains a "perpetual whack-a-mole game."
- **Evidence**: ICML 2026 peer-reviewed paper; human red-teaming evaluation plus controlled automated-attack measurement against named frontier models.
- **Confidence**: emerging

### Side B
- **Source**: blog-simonwillison-hack-my-ai-assistant (not yet mined — issue #1429)
- **Claim**: In a live public challenge, ~2,000 people made ~6,000 attempts to leak a secret from an Opus 4.6-powered, prompt-hardened OpenClaw instance via email injection. Zero succeeded. Willison reads this as evidence that labs' anti-injection training is "effective in making these attacks much harder to pull off," while explicitly cautioning that "6,000 failed attempts provides no guarantees that someone with a more sophisticated approach couldn't get through" and still recommending against relying on this for irreversible-damage production systems.
- **Evidence**: Real-world, large-N live public challenge against a specific model and deployment (verified directly against the source URL; corpus source note not yet written).
- **Confidence**: anecdotal (single deployment, single model, undisclosed attacker-skill distribution, no source note yet in corpus)

### Resolution

Both sides are credible but measure different things and are not as opposed as the raw headline figures (near-100% vs. 0%) suggest. Side A's near-100% figure specifically describes skilled red-teamers *deliberately* exploiting a named technique (CoT Forgery/role confusion); Side B's 6,000 attempts come from an open public audience with no evidence of comparable technique sophistication, against a deployment that included explicit system-prompt-level anti-injection rules (not a bare, undefended model). Model generation also differs (Opus 4.5/GPT-5.4, May 2026, vs. Opus 4.6, June 2026), consistent with Side A's own trendline that later model generations reduce automated-attack failure rates.

Willison's own text does not claim the 0/6,000 result refutes model-layer-defense skepticism — he explicitly cautions that a more sophisticated attacker could still succeed, which is consonant with, not contrary to, Side A's mechanism claim. The genuine open question is narrower than "does model-layer defense work": it is whether a *skilled, technique-aware* human attacker would still achieve a near-100% success rate against the same Opus 4.6 + prompt-hardened target that resisted 6,000 unscreened public attempts. The corpus cannot answer that yet.

This verdict should be revisited once the `blog-simonwillison-hack-my-ai-assistant` source note is formally extracted and merged — in particular, check whether Hacker News commenters or Fernando Irarrázaval's own writeup identify near-misses or technique-aware attempts, which would bear directly on whether Side B narrows or leaves untouched Side A's Claim 4.

### Citation in the guide

Ch06 §Security and Threat Model should present this as a `**Debated:**` block:
- Cite Side A's mechanism claims (Claims 1-3, 7-8: style-based role identification, CoT Forgery, destyling, "perpetual whack-a-mole") as `[emerging]` — these are not contradicted by Side B and should anchor the guide's recommendation that environmental/structural controls remain necessary regardless of model-layer training improvements.
- Cite Side A's automated-attack failure rates (Claim 5: 11%/25% for Opus 4.5/GPT-5.4, May 2026) as `[emerging]` and note the likely downward trend by model generation, corroborated qualitatively by Side B's Opus 4.6 result.
- Cite Side A's "near-100% human red-teamer success" figure (Claim 4) as `[emerging]` but flag it specifically as describing *technique-aware, deliberate* attackers — not a general population — and note it is the weaker-sourced part of Side A (no disclosed protocol).
- Cite the hackmyclaw result as `[anecdotal]` (pending the corpus source note) as encouraging real-world evidence that current-generation training resists a broad, unscreened attacker population, while explicitly carrying Willison's own caveat that this provides no guarantee against a more sophisticated, targeted attacker.
- Do NOT cite the hackmyclaw 0/6,000 result as evidence that model-layer training alone is a sufficient defense — the target used explicit prompt-level anti-injection rules, and Willison himself declines to draw that conclusion.
- Do NOT treat the human-attacker "near-100% vs. 0%" comparison as settled; flag it for re-assessment once `blog-simonwillison-hack-my-ai-assistant` is merged into the corpus.

## C-008: Copilot CLI auto routing: availability-only (April) vs. task-aware (July)

- **Filed**: 2026-07-03 by steveash (re-file of Miner-filed issue #1476, closed on a pre-screen technicality for a missing source URL)
- **Issue**: #1483
- **Resolved**: 2026-07-05
- **Verdict**: superseded
- **Affected guide sections**: Ch02 §Harness Engineering (CLI default model configuration, auto model selection surface map), Ch04 §Model Selection and Cost Management

### Side A
- **Source**: [docs-github-copilot-cli-auto-model-selection](source-notes/docs-github-copilot-cli-auto-model-selection.md)
- **Claim**: Copilot CLI auto (April 17, 2026) selects the most efficient model based on plan, applicable policies, and rate-limit pressure — not based on task type.
- **Evidence**: Official GitHub changelog, April 17, 2026: "Auto will select the most efficient model based on your plan and policies." No task-type or task-dimension language appears anywhere in the ~300-word source.
- **Confidence**: settled

### Side B
- **Source**: [docs-github-copilot-cli-auto-model-selection-task-based-routing](source-notes/docs-github-copilot-cli-auto-model-selection-task-based-routing.md)
- **Claim**: Copilot CLI auto (July 1, 2026) now evaluates the task across several dimensions (reasoning, code generation complexity, bug diagnosis difficulty, tool orchestration needs) alongside availability/reliability signals to select the optimal model.
- **Evidence**: Official GitHub changelog, July 1, 2026: "Auto weighs real-time model availability and reliability signals, then evaluates your task across several dimensions like reasoning, code generation complexity, bug diagnosis difficulty, and tool orchestration needs to select the optimal model." This sentence is verbatim identical to the May 20, 2026 VS Code auto announcement (issue #844, Claim 1).
- **Confidence**: settled

### Resolution

This is a genuine algorithm change to the CLI's "auto" feature between April and July 2026, not a description error in either source. The corpus already documents GitHub rolling task-aware routing out to three other Copilot surfaces before the CLI: Cloud Agent (May 14, issue #745), VS Code (May 20, issue #844), and Copilot Chat (June 17, issue #1218) — each launched or updated with task-complexity-aware routing already built in. The Chat auto note explicitly flagged, at time of its own extraction, that "only CLI auto remains purely availability-driven" and that this gap would need to be revisited. The July 1 CLI changelog closes exactly that gap, using routing-description and cache-boundary language that is verbatim identical to the VS Code announcement — strong evidence the CLI's routing implementation was brought into alignment with the already-shipped VS Code/Chat implementation, rather than the April source having simply omitted an existing capability.

The April source's "not task-aware" framing is inferred from the absence of any task-content language in a thin, ~300-word changelog, not a verbatim denial — this is a minor evidentiary weakness in Side A, but it is more consistent with "GitHub had not yet built task-aware routing for the CLI in April" than with "GitHub was suppressing an existing capability in April while announcing the same capability as new for sibling surfaces in May and June." No plan-tier, configuration, or credential-layer mediating variable explains the discrepancy (both changelogs describe the same "auto" toggle available on all Copilot plans) — this is a temporal supersession, not a context-dependent split.

The April source's other claims (billing discount, admin policy compliance, user override control, cost-bounded model pool) are independently reconfirmed as unchanged in the July source and remain valid; only the task-awareness dimension and the billing *unit* (premium requests → AI credits, with legacy-plan grandfathering) changed.

### Citation in the guide

Ch02 §Harness Engineering's auto-model-selection surface map should be updated to state that, as of July 2026, all four GitHub Copilot auto surfaces (CCA, VS Code, Chat, CLI) are task-aware, evaluating reasoning, code generation complexity, bug diagnosis difficulty, and tool orchestration needs alongside availability/reliability signals. Cite `docs-github-copilot-cli-auto-model-selection-task-based-routing` Claims 1–2 as `[settled]` for current CLI behavior. Retain `docs-github-copilot-cli-auto-model-selection` as `[settled]` historical context only — explicitly dated to April 2026 — for readers who need to reason about the feature's evolution or who may be on an older CLI version; do not cite its "not task-aware" claim as current guidance. Note the model-pool caveat: the July source does not name specific models (unlike April's four-model enumeration), so the guide should not assume the April pool list (GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, Haiku 4.5) is still accurate without checking GitHub's live supported-models documentation.

Ch04 §Model Selection and Cost Management should update CLI auto's cost-management guidance to the AI-credits billing default (10% credit discount vs. direct model cost) from the July source, while flagging the legacy-annual-plan exception (Copilot Pro/Pro+ on existing annual plans remain on premium-request billing with the 10% multiplier discount) as a plan-dependent branch practitioners must check before applying cost formulas. Do not cite the July source's "no quality regression" claim (Claim 9) as verified — it is vendor-asserted with no disclosed methodology, consistent with how the guide should already be treating the equivalent Chat auto "maintaining high quality results" claim (issue #1218).
