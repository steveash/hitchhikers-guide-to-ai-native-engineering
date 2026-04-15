---
source_url: https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/
source_type: failure-report
platform: blog
title: "The Claude Code Source Leak: Fake Tools, Frustration Regexes, Undercover Mode"
author: Alex Kim (alex000kim)
date_published: 2026-03-31
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: emerging
issue: "#20"
---

# Failure Report: Claude Code Source Leak Reveals AutoCompact Runaway Loop, 14-Vector Cache Economics, and Prompt-Only Coordinator Orchestration

> An accidental source map leak in Anthropic's npm package exposed Claude Code's
> internal implementation, revealing a production autoCompact failure that wasted
> ~250K API calls per day globally (fixed by a 3-failure circuit breaker), a
> prompt-cache tracking system managing 14 distinct cache-break vectors with sticky
> latches, and a multi-agent coordinator that enforces quality standards entirely
> through system prompt instructions — plus 23 shell-security checks in bashSecurity.ts
> that define the attack surface practitioners should model in custom harnesses.

## Source Context

- **Platform**: Personal blog (alex000kim.com), 2026-03-31. The HN discussion thread
  (item id 47584540) corroborates the post with additional architectural observations;
  key details from both are incorporated here.
- **Author credibility**: Alex Kim is a practitioner-analyst who works through technical
  source code to extract actionable findings. The blog post is structured as a reverse
  engineering analysis of leaked source, not first-person practitioner experience — it
  draws on code-level evidence (file names, line numbers, comment text) rather than
  anecdote. Claims that cite specific file paths and line numbers are the highest-confidence
  category; claims about product roadmap implications are more speculative.
- **Community response**: The HN discussion (1,349 points, 555 comments) was large and
  broadly confirmatory of the findings. A key corroborating detail: HN commenters
  identified the April Fools' Buddy companion system (Tamagotchi-style creatures),
  confirming KAIROS and companion.ts are real features rather than noise artifacts. The
  regeneration philosophy ("there is no point in code-reviewing AI-generated code") was
  discussed and contested; most commenters acknowledged the tradeoff even if they
  disagreed with it. No commenter disputed the core autoCompact, cache, or security
  findings.
- **Scope**: Analysis covers eight major findings from the leaked codebase. Per the
  Prospector's triage, this note focuses on the four actionable-for-practitioners
  findings: autoCompact failure, prompt cache economics, coordinator orchestration,
  and bash security checks. Anti-distillation/fake tools, undercover mode, KAIROS,
  native client attestation, and the April Fools companion are documented briefly in
  Extraction Notes but not expanded into lessons.

## What Was Attempted

- **Goal**: Post-leak technical analysis of Claude Code's internal architecture, aimed
  at understanding production decisions and engineering quality.
- **Tool/approach**: Analysis of source maps accidentally shipped in Anthropic's npm
  package. The mechanism: Bun issue #28001 (source maps served in production despite
  documentation stating they should be disabled) is identified as the likely cause.
  Anthropic deprecated the package with message "Unpublished" rather than formally
  withdrawing it.
- **Setup**: The leak exposed the full JavaScript source of a commercial Claude Code
  release. The analysis was published March 31, 2026 — the day after the leak was
  publicly noted.

## What Went Wrong

The primary production failure revealed by the leak:

- **AutoCompact runaway loop**: The autoCompact mechanism had no circuit breaker.
  When compaction failed (e.g., due to API errors, context structure issues, or
  transient failures), the system would retry indefinitely within the same session.
  Internal Anthropic data cited in a source comment: **1,279 sessions had 50+ consecutive
  autoCompact failures in a single session, with the worst case reaching 3,272
  consecutive failures** — all in one session — **wasting approximately 250,000 API
  calls per day globally** at the time of the comment (2026-03-10).
- **The fix was a three-line circuit breaker**: Setting
  `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3` disabled compaction after three consecutive
  failures, preventing further waste. The simplicity of the fix underscores the severity
  of the omission: the entire $250K/day API burn was preventable with a single constant.

Secondary issues surfaced (not user-facing failures but engineering observations):

- `print.ts` spans 5,594 lines with a single function of 3,167 lines nested 12 levels
  deep — the entire agent run loop including SIGINT, rate-limits, AWS auth, MCP lifecycle,
  plugin install/refresh, worktree bridging, and more. HN commenters noted this is
  consistent with a "regeneration model" philosophy where the code is replaced wholesale
  rather than maintained incrementally.
- Inconsistent async/await patterns in `src/ink/termio/osc.ts:192-210`.

## Root Cause (if identified)

- **Author's diagnosis (autoCompact)**: The compaction subsystem lacked defensive
  programming around its own failure modes. A successful compaction is not guaranteed
  — if the compaction call fails, the session should fall back to proceeding without
  compaction, not retry indefinitely. The root cause is absence of a circuit breaker,
  not a flaw in the compaction algorithm itself.
- **Author's diagnosis (source exposure)**: Bun issue #28001 — source maps shipped
  in a production npm package despite documentation stating they should be disabled.
  Alex Kim notes: "Anthropic acquired Bun, and Claude Code builds atop it. A known
  bug that exposed their own product's source code."
- **Our assessment**: The autoCompact diagnosis is correct and well-evidenced by
  the code comment itself. The 250K calls/day figure is internally sourced (BQ data
  from 2026-03-10), making it unusually high-confidence for a production metric. The
  broader lesson is architectural: any retry loop in a harness that can fail needs
  a circuit breaker. The three-failure threshold chosen (not three failures total, but
  three *consecutive* failures) is also instructive — it allows transient errors to
  self-heal before the breaker trips.
- **Category**: genuine-bug (missing circuit breaker in production retry loop)

## Recovery Path

- **AutoCompact fix**: `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3` — disable compaction
  after three consecutive failures, allowing the session to continue without compaction
  rather than burning API budget on retries.
- **Harness engineering lesson**: The fix pattern generalizes: any retry mechanism in
  a harness (compaction retries, tool-call retries, agent loop retries) should count
  consecutive failures and trip to a safe degraded state. Three is a reasonable default;
  the key is that the constant exists at all.

## Extracted Lessons

### Lesson 1: AutoCompact runaway loops without a circuit breaker waste massive API budget

- **Evidence**: `autoCompact.ts` lines 68-70 comment: "BQ 2026-03-10: 1,279 sessions had
  50+ consecutive failures (up to 3,272) in a single session, wasting ~250K API calls/day
  globally." The BQ (BigQuery) annotation indicates this is internally measured production
  data, not an estimate. The fix — `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3` — shipped
  after the measurement.
- **Confidence**: emerging (code-level evidence from a production system is strong, but
  this is a snapshot of a specific point in time; the bug may be fixed in current releases)
- **Quote**: "BQ 2026-03-10: 1,279 sessions had 50+ consecutive failures (up to 3,272)
  in a single session, wasting ~250K API calls/day globally."
- **Our assessment**: This is the strongest production failure metric in our corpus.
  250K API calls/day is not a theoretical concern — it is a measured cost from Anthropic's
  own BigQuery telemetry. Harness authors building custom compaction or retry logic who
  skip circuit breakers are replicating this failure pattern. The "three consecutive
  failures" threshold is a reasonable default for any such circuit breaker.

### Lesson 2: Prompt cache management requires tracking 14 distinct break vectors — far more than practitioners typically model

- **Evidence**: `promptCacheBreakDetection.ts` tracks 14 cache-break vectors with sticky
  latches that prevent mode toggles from invalidating the cache. One internal function
  is annotated `DANGEROUS_uncachedSystemPromptSection()` — the uppercase `DANGEROUS`
  naming convention signals that calling it in the wrong context silently destroys cache
  hit rates for the session.
- **Confidence**: emerging (code-level evidence; the specific 14 vectors are not
  enumerated in the analysis, but the count and the latch architecture are cited)
- **Quote**: "The system tracks '14 cache-break vectors' to preserve expensive token
  usage. Functions are annotated as `DANGEROUS_uncachedSystemPromptSection()` to
  highlight cache-invalidating operations. 'Sticky latches' prevent mode toggles from
  busting the cache."
- **Our assessment**: Practitioner guidance on prompt caching typically focuses on
  one or two obvious break vectors (e.g., "don't change the system prompt mid-session").
  Anthropic's own production implementation requires 14-vector tracking with explicit
  architecture around sticky latches. This gap between practitioner mental models and
  production reality is significant for Ch04. The `DANGEROUS_` prefix is a specific
  engineering convention worth recommending: when a function busts the cache, naming
  it explicitly prevents inadvertent calls from engineers who don't realize the cost.

### Lesson 3: Anthropic's production coordinator uses prompt-only orchestration with explicit anti-rubber-stamping directives

- **Evidence**: `coordinatorMode.ts` implements multi-agent orchestration entirely through
  system prompt instructions. The key directives revealed: "Do not rubber-stamp weak work"
  and "You must understand findings before directing follow-up work. Never hand off
  understanding to another worker."
- **Confidence**: emerging (code-level evidence; the full prompt is not quoted in the
  analysis, but these directives are explicitly cited as the mechanism)
- **Quote**: "The coordinator uses prompt-based instructions to manage worker agents,
  including directives like 'Do not rubber-stamp weak work' and 'You must understand
  findings before directing follow-up work. Never hand off understanding to another worker.'"
- **Our assessment**: This is the highest-signal orchestration finding in the note.
  Anthropic's own production coordinator does not rely on tool calls, structured schemas,
  or external state for quality enforcement — it uses prose instructions targeting the
  exact failure mode practitioners observe: a coordinator that waves through poor agent
  work without review. The "never hand off understanding to another worker" directive
  directly addresses a known multi-agent failure mode: shallow orchestration where the
  coordinator routes without synthesizing. This validates prompt-based orchestration
  as the production approach at Anthropic, and provides the specific language that
  makes it work.

### Lesson 4: Shell execution in a harness carries a 23-check attack surface — 18 Zsh builtins alone

- **Evidence**: `bashSecurity.ts` implements 23 numbered security checks: 18 blocked Zsh
  builtins, defense against Zsh equals expansion (`=curl` bypassing permission checks
  for `curl`), unicode zero-width space injection (ZWS in command tokens to slip past
  allow-list matching), IFS null-byte injection, and additional malformed token bypass
  mitigations discovered during security review.
- **Confidence**: emerging (code-level evidence; 23 is the count, specific check names
  are partially cited)
- **Quote**: "The system implements '23 numbered security checks' in `bashSecurity.ts`,
  including '18 blocked Zsh builtins, defense against Zsh equals expansion (`=curl`
  bypassing permission checks for `curl`), unicode zero-width space injection, IFS
  null-byte injection,' plus mitigations for malformed token bypasses discovered during
  security review."
- **Our assessment**: Practitioners building custom harnesses with shell execution
  rarely implement coverage at this depth. The Zsh equals expansion bypass
  (`=curl` executing `curl` even when `curl` is on a blocklist) and unicode ZWS
  injection are non-obvious attack vectors that would not appear in a typical security
  review. Three lessons:
  (1) If your harness allows shell execution, assume your allowlist matching will be
  bypassed unless hardened;
  (2) Zsh is meaningfully more dangerous than bash for harness tool use (18 extra
  blocked builtins is a strong signal);
  (3) The existence of 23 numbered, maintained checks suggests the attack surface is
  larger than most practitioners expect — and that new bypasses are discovered over time.

## Concrete Artifacts

The blog post cites source-level evidence rather than reproducing code verbatim. The
most useful artifacts for the guide:

```
# autoCompact.ts lines 68-70 (verbatim comment from source)
# BQ 2026-03-10: 1,279 sessions had 50+ consecutive failures
# (up to 3,272) in a single session, wasting ~250K API calls/day globally.
MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3
```

```
# promptCacheBreakDetection.ts — architectural summary
# - 14 cache-break vectors tracked
# - Sticky latches: prevent mode toggles from invalidating cache
# - DANGEROUS_uncachedSystemPromptSection() — naming convention for
#   functions that silently destroy cache hit rate if called incorrectly
```

```
# coordinatorMode.ts — sample directives (verbatim from article)
"Do not rubber-stamp weak work"
"You must understand findings before directing follow-up work.
 Never hand off understanding to another worker."
```

```
# bashSecurity.ts — security check inventory (partial, from article)
# Total: 23 numbered checks
# Includes:
#   - 18 blocked Zsh builtins
#   - Zsh equals expansion: =curl bypasses permission checks for curl
#   - Unicode zero-width space injection in command tokens
#   - IFS null-byte injection
#   - Malformed token bypass (additional, discovered in security review)
```

## Cross-References

- **Corroborates**: `failure-claudemd-ignored-compaction.md` — that note documents
  CLAUDE.md instruction loss after compaction (a failure of what compaction produces);
  this source documents a failure of the compaction mechanism itself (runaway retry loops).
  These are complementary: the first failure degrades session quality gradually; the
  second burns API budget in a tight loop. Both argue for defensive harness design
  around compaction. The 250K calls/day figure in this source is distinct from any metric
  in the CLAUDE.md note — it covers wasted API calls, not instruction loss.

- **Extends**: `research-wasnotwas-context-compaction.md` — wasnotwas provides compaction
  trigger thresholds and dollar-cost measurements for successful compaction. This source
  adds the production failure case: when compaction itself fails repeatedly, the cost is
  not $0.40/call (the cost of successful compaction) but $0.40 × N for each failing
  attempt. The two notes together cover both the success path and the failure path for
  compaction economics.

- **Corroborates**: `failure-cursor-ultra-billing-cache-explosion.md` — Cursor's cache
  billing explosion (4k user tokens billed as 21M cache reads, costing $12/call) is
  another manifestation of cache economics that practitioners do not adequately model.
  The 14-vector cache tracking revealed by this source is evidence that cache management
  at production scale is architecturally complex — supporting the guide's argument that
  cache economics require explicit attention, not ad-hoc management.

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's Claim 5
  ("The bottleneck has shifted from code generation to verification") and the anti-sycophancy
  stance in orchestration find concrete implementation support here. The coordinator's
  "Do not rubber-stamp weak work" directive is Anthropic operationalizing Osmani's claim
  at the orchestrator layer. The two sources agree: quality enforcement must be built into
  the orchestrator, not assumed.

- **Extends**: `blog-addyosmani-code-agent-orchestra.md` — Osmani describes subagent
  patterns and the Ralph loop but treats orchestration as primarily a workflow design
  problem. This source reveals that at the code level, Anthropic's coordinator relies on
  system prompt instructions for quality control, not structured schemas or tool-call
  mechanisms. This is useful grounding: practitioners do not need exotic orchestration
  infrastructure to achieve coordinator-level quality control — the mechanism is prose.

- **Novel**: The 250K API calls/day autoCompact waste figure is the only measured
  production failure cost in our corpus from Anthropic's own telemetry. The 14-vector
  cache tracking count is unique to this source. The coordinator's specific anti-rubber-
  stamping language ("Do not rubber-stamp weak work", "Never hand off understanding to
  another worker") is unique to this source and directly usable in guide recommendations.
  The 23-check bash security inventory is the only source in our corpus that quantifies
  the shell execution attack surface.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "Circuit Breakers for Retry Loops" pattern
  with the autoCompact failure as the motivating example. The 250K API calls/day waste
  is the cost of omitting one. Specific recommendation: any retry loop in a harness
  (compaction retries, tool-call retries, agent loop retries) needs a consecutive-failure
  counter and a trip to a safe degraded state. Cite `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3`
  as the reference implementation: it took Anthropic a measured production failure before
  they added one; practitioners should add it by default.

- **Chapter 03 (Safety and Verification)**: Add `bashSecurity.ts`'s 23-check inventory
  as the reference for what production shell execution security looks like. Specific
  additions warranted: (a) Zsh is riskier than bash for harness tool use — the equals
  expansion bypass alone justifies defaulting to bash; (b) unicode ZWS injection against
  allowlist matching is a non-obvious but real attack vector; (c) 23 checks is a floor,
  not a ceiling — the comment history implies new bypasses are discovered during audits.
  Frame as: "If your harness allows shell execution and you have fewer than 23 documented
  security checks, you have unknown exposure."

- **Chapter 04 (Context Engineering / Cache-Aware Design)**: Update the prompt cache
  guidance to reflect that production cache management involves 14 distinct break vectors.
  Two specific additions: (a) Adopt the `DANGEROUS_` naming convention for any function
  that invalidates the prompt cache — this prevents inadvertent calls and documents
  intent; (b) "Sticky latches" as a design pattern: if a mode toggle (e.g., switching
  tool configurations mid-session) would bust the cache, gate the toggle behind a latch
  that only fires at session boundaries rather than immediately.

- **Chapter 04 (Multi-Agent Orchestration)**: The coordinator's prompt-only orchestration
  with specific quality-control directives is the strongest production evidence for
  prompt-based coordination as the viable approach. Specific guide additions: (a) Cite
  "Do not rubber-stamp weak work" and "You must understand findings before directing
  follow-up work" as reference language for coordinator prompts — practitioners can
  adapt this directly; (b) The "never hand off understanding to another worker" directive
  is a concrete operationalization of Osmani's Claim 5 (verification bottleneck). This
  language belongs in the coordinator prompt design section, not just as philosophy.

## Extraction Notes

- **Confidence caveat**: This is a code snapshot from a leaked version. Current Claude
  Code may have addressed the autoCompact bug, changed the cache tracking architecture,
  or modified the coordinator prompt. Before citing specific numbers (250K calls/day,
  14 vectors, 23 checks) in the published guide, an editor should verify against current
  behavior where possible. The autoCompact fix (MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3)
  is the most verifiable — it would be reflected in changed session behavior for users
  who previously experienced runaway compaction.

- **Out of scope per Prospector**: Anti-distillation mechanisms (fake tool injection
  via `ANTI_DISTILLATION_CC` flag and connector-text summarization), undercover mode
  (`undercover.ts`, 90 lines, strips internal Anthropic references), KAIROS autonomous
  agent (unreleased: `/dream` skill, daily append-only logs, GitHub webhook subscriptions,
  5-minute cron refresh), native client attestation (`cch=00000` placeholder rewritten
  by Bun's Zig HTTP stack below JS runtime), and the April Fools Buddy companion system
  (18 species, rarity tiers, 1% shiny chance, RPG stats via Mulberry32 PRNG from user ID)
  are real findings but do not directly intersect with guide practitioner recommendations.
  Document here for completeness; do not expand into lessons unless a future source
  connects them to actionable practitioner patterns.

- **Terminal rendering optimization** (`ink/screen.ts`, `ink/optimizer.ts`): Int32Array-
  backed ASCII pools with bitmask-encoded styles achieving ~50x reduction in stringWidth
  calls during token streaming. Interesting engineering but not guide-impacting.

- **Code quality findings** (print.ts 3,167-line single function, 12 nesting levels):
  The HN discussion noted this is consistent with a regeneration philosophy ("there is
  no point in code-reviewing AI-generated code — simply update your spec(s) and
  regenerate"). This is relevant to the guide's claims about AI code quality but the
  evidence is anecdotal (one file, one codebase snapshot).

- **The HN discussion thread** (47584540) was the source of the Buddy companion system
  confirmation and the regeneration philosophy observation. These corroborate the blog
  post rather than contradicting it. A commenter confirmed the native client attestation
  is the enforcement mechanism behind Anthropic's legal action against OpenCode (a
  third-party Claude Code client that bypassed attribution headers).

- The blog post was published March 31, 2026 — one day after the leak was widely noted.
  The speed of publication and the code-citation depth suggest Kim had access to the
  source for at least a day before publishing. The analysis reads as a genuine technical
  walkthrough, not a clickbait summary.
