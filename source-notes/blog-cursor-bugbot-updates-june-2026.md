---
source_url: https://cursor.com/blog/bugbot-updates-june-2026
source_type: blog-post
title: "Bugbot is now over 3x faster, 22% cheaper, and finds 10% more bugs"
author: Jason Smale, Yuri Volkov & Michael Zhao (Cursor)
date_published: 2026-06-10
date_extracted: 2026-06-11
last_checked: 2026-06-11
status: current
confidence_overall: emerging
issue: "#1147"
---

# Bugbot is now over 3x faster, 22% cheaper, and finds 10% more bugs (Cursor, June 2026)

> Cursor's June 2026 Bugbot update delivers three simultaneous improvements — 3x speed, 22% lower cost, 10% more bugs detected — powered by Composer 2.5 and harness upgrades, and introduces two new operational patterns: a pre-push `/review` command that integrates with GitHub/GitLab deduplication, and an incremental review mode that scopes feedback to genuinely new changes only.

## Source Context

- **Type**: blog-post (Cursor product announcement, ~4 min read, published June 10, 2026; bylined Jason Smale, Yuri Volkov & Michael Zhao — three named Cursor engineers, the most specific authorship of any Bugbot post in the corpus).
- **Author credibility**: Cursor/Anysphere is the vendor behind Bugbot; first-party product announcement with commercial incentive to present improvements favorably. All performance metrics (3x speed, 22% cost, 10% bug detection) are relative comparisons against prior Bugbot versions with no disclosed baseline absolute figures or measurement methodology. The Composer 2.5 attribution is coherent with the May 2026 model launch documented in `blog-cursor-composer-2-5.md`. The three named authors lend slightly more credibility than the anonymous "Cursor Team" byline used in prior Bugbot posts.
- **Scope**: Covers three performance metrics, the pre-push `/review` command (with deduplication behavior), incremental review mode, model attribution to Composer 2.5, and model block list fallback policy. Does NOT cover: absolute baseline runtime figures before the improvement, the specific methodology for computing "10% more bugs per review," the cost of high-effort runs under the new pricing, configuration syntax for incremental reviews, or what "next best available model" means in practice when Composer 2.5 is blocked.

## Extracted Claims

### Claim 1: Bugbot is now over 3x faster, 22% cheaper, and finds 10% more bugs per review as of June 2026

- **Evidence**: Direct product metrics stated in the announcement by three named Cursor engineers.
- **Confidence**: emerging (vendor-stated relative metrics; baselines are implicitly the prior Bugbot version and May 2026 pricing; no methodology, PR sample sizes, or absolute figures provided for any of the three dimensions)
- **Quote**: "Bugbot is now over 3x faster to run, 22% cheaper, and finds 10% more bugs per review."
- **Our assessment**: Three simultaneous improvements across speed, cost, and quality. All three are relative claims — "3x faster" implies a prior runtime that is never stated; "22% cheaper" implies a prior per-run cost; "10% more bugs" implies a prior bug-detection rate. Cross-referencing: the May 2026 billing post (`blog-cursor-bugbot-effort-billing.md` Claim 3) established the prior per-run cost at $1.00–$1.50 average, so 22% cheaper implies ~$0.78–$1.17/run average. The April 2026 benchmark (`blog-cursor-bugbot-learning.md` Claim 4) established an 80% resolution rate as the baseline — "10% more bugs per review" improves detection count, not resolution rate (a different metric). The 10% figure is additive on top of the May 2026 effort-level data: at default effort, 10% more bugs are now found; at high effort (per `blog-cursor-bugbot-effort-billing.md` Claim 6), Bugbot found 35% more bugs vs. default — those two multipliers operate on different axes (baseline improvement vs. effort tuning).

### Claim 2: 90% of Bugbot runs now finish in under three minutes

- **Evidence**: Specific P90 runtime distribution stated in the announcement.
- **Confidence**: emerging (vendor-stated; no prior published runtime distribution to compare against; no PR size segmentation provided)
- **Quote**: "In practice, 90% of Bugbot runs now finish in under three minutes."
- **Our assessment**: This is the first published runtime SLA-style metric for Bugbot. The P90 framing (90% under 3 minutes, not 100%) is honest about tail latency — large PRs or deep histories can still exceed 3 minutes. Practitioners setting workflow timeout budgets should use 5–10 minutes as a conservative upper bound. The "over 3x faster" headline claim combined with a P90 < 3 min suggests the median run before the June improvements was in the 3–5 minute range (rough inference only; baseline not stated).

### Claim 3: A new `/review` command allows running Bugbot and Security Review before pushing code, available in Cursor 3.7+

- **Evidence**: Direct product feature description with specific version requirement and command syntax.
- **Confidence**: settled (stated as an available product feature with version and platform requirements; verifiable in product)
- **Quote**: "You can now run Bugbot and Security Review with `/review` before pushing code."
- **Our assessment**: Pre-push review is the most operationally significant feature in this update. Previously, Bugbot triggered post-push via GitHub/GitLab PR review hooks — catching issues only after code is visible to teammates. Pre-push via `/review` shifts the feedback point earlier in the developer workflow, before the code is shared. The two targeted commands (`/review-bugbot` and `/review-security`) allow selective invocation rather than running both agents every time. The "Available in Cursor 3.7+ and on cursor.com/agents" availability note means CLI users must wait (see Claim 4 below).

### Claim 4: The `/review` command syncs with GitHub/GitLab Bugbot and skips already-reviewed diffs to prevent duplicate reviews

- **Evidence**: Direct product behavior description.
- **Confidence**: settled (stated product behavior with specific deduplication semantics; verifiable in product)
- **Quote**: "Bugbot recognizes it, skips the review, and leaves a comment noting it has already reviewed that diff."
- **Our assessment**: The deduplication behavior prevents double-review when a developer runs `/review` pre-push and the same diff later triggers a post-push Bugbot review on GitHub/GitLab. Without this, teams using both pathways would receive duplicate review comments on the same code. The "leaves a comment noting it has already reviewed that diff" behavior provides an audit trail — the PR record shows that Bugbot ran pre-push, even though it does not run again post-push. This is good harness UX: silence would be ambiguous (did Bugbot fail? was it skipped?); a note confirms intentional deduplication.

### Claim 5: Organizations can configure Bugbot to review only changes since the last review, keeping feedback focused on new updates

- **Evidence**: Direct product feature description.
- **Confidence**: emerging (stated as an available configuration option; the mechanism for what "since the last review" tracks — by commit SHA, by prior Bugbot run timestamp, by push event — is not described in this post)
- **Quote**: "You can now configure Bugbot to only review what's new since the last review, keeping feedback focused on your latest updates."
- **Our assessment**: Incremental review addresses a real pain point: when a PR author pushes a minor fix in response to a Bugbot comment, a full re-review re-surfaces all previously flagged findings plus any new ones. This creates review noise and trains developers to ignore Bugbot re-reviews. Incremental mode limits the re-review to genuinely new changes. The tradeoff: if a developer's fix introduces a regression in an area previously flagged, incremental mode may not catch it (depending on how granularly "new since last review" is defined). This is an org-level configuration, suggesting all PRs in the org share the same incremental-vs-full behavior.

### Claim 6: The June 2026 performance improvements are powered by Composer 2.5 training advances and separate harness improvements

- **Evidence**: Direct attribution in the "How we got here" section of the post.
- **Confidence**: emerging (vendor attribution; specific technical changes enabling the 3x speed and 22% cost reduction are not detailed; "harness improvements" is vague)
- **Quote**: "These performance gains are made possible by harness improvements and progress we've made training Composer 2.5, which now powers Bugbot."
- **Our assessment**: The attribution has two components: (1) Composer 2.5 model improvements, and (2) harness infrastructure improvements, stated as separate contributors. The "harness improvements" component is distinct from model quality — it likely refers to inference infrastructure, request routing, caching, or batching changes that reduce latency and cost independently of model capability. The cost improvement (22%) plausibly comes mostly from harness/inference efficiency; the quality improvement (10% more bugs) plausibly comes mostly from Composer 2.5's improved capabilities. The speed improvement (3x) likely combines both. None of this breakdown is disclosed. Cross-reference: `blog-cursor-composer-2-5.md` Claim 1 established that Composer 2.5 "is better at sustained work on long-running tasks, follows complex instructions more reliably" — the quality improvement in Bugbot is consistent with these capabilities applied to code review analysis.

### Claim 7: Bugbot automatically falls back to the next best available model if an organization has opted out of Composer 2.5

- **Evidence**: Direct product policy statement.
- **Confidence**: settled (stated product policy; verifiable in org settings behavior)
- **Quote**: "Bugbot respects model block lists. If your organization has opted out of Composer 2.5, Bugbot will automatically fall back to the next best available model."
- **Our assessment**: This is an important enterprise caveat. The 3x speed, 22% cost, and 10% quality figures quoted in this announcement are Composer 2.5 numbers. Organizations that have opted out of Composer 2.5 — for compliance, data residency, legal, or security reasons — will receive Bugbot reviews from a different model with different (likely lower) performance characteristics. Practitioners at organizations using model block lists should verify empirically what model Bugbot falls back to and what performance differential to expect, rather than assuming the June 2026 headline numbers apply to their environment.

## Concrete Artifacts

### Pre-push Review Command Reference

```
# Bugbot pre-push review commands (Cursor, June 2026)
# Source: https://cursor.com/blog/bugbot-updates-june-2026

AVAILABILITY:
  - Cursor 3.7+
  - cursor.com/agents
  - CLI: coming soon (not available at publication)

COMMANDS:
  /review              → prompts to choose which agents to run
  /review-bugbot       → runs Bugbot directly
  /review-security     → runs Security Review directly

GITHUB/GITLAB SYNC:
  - /review syncs with Bugbot on GitHub and GitLab
  - If identical diff already reviewed pre-push:
    Bugbot skips the review and leaves a comment noting
    it has already reviewed that diff (deduplication)
```

### June 2026 Performance Metrics

```
# Bugbot June 2026 performance improvements
# Source: https://cursor.com/blog/bugbot-updates-june-2026
# All figures are relative to prior version (baselines not stated)

Speed:     over 3x faster to run
Runtime:   90% of runs complete in under three minutes (P90 < 3 min)
Cost:      22% cheaper (implies ~$0.78-$1.17/run avg, down from $1.00-$1.50)
Quality:   10% more bugs per review

Powered by: Composer 2.5 + harness infrastructure improvements (two separate
            contributors; breakdown by dimension not disclosed)

Model fallback: If org has opted out of Composer 2.5 →
                automatic fallback to "next best available model"
                (specific fallback model not named)

EVIDENCE BASIS: Vendor-stated relative metrics; no methodology disclosed
```

### Incremental Review Mode

```
# Bugbot incremental review configuration (Cursor, June 2026)
# Source: https://cursor.com/blog/bugbot-updates-june-2026

BEHAVIOR:
  Default:     Review the entire PR diff on each Bugbot run
  Incremental: Review only changes since the last review

SETTING LEVEL: Organization-wide configuration option
MECHANISM:     "Since the last review" — tracking mechanism not specified
               (by commit SHA? by prior Bugbot run timestamp? not disclosed)

USE CASE: Prevents re-surfacing already-reviewed findings when PR is
          updated with minor fixes
TRADEOFF: May miss regressions introduced in previously-reviewed areas
          (depends on granularity of change tracking)
```

## Cross-References

- **Corroborates**: `blog-cursor-bugbot-effort-billing.md` Claim 3 — May 2026 established the baseline per-run cost at "$1.00-$1.50, depending on PR size and complexity." June's "22% cheaper" maps that baseline to ~$0.78–$1.17/run average. Consistent progression; no contradiction.

- **Corroborates**: `blog-cursor-bugbot-effort-billing.md` Claim 5 — May 2026 stated the default effort resolution rate at 80%. This June post improves bug detection count by 10% without stating a new resolution rate; the two metrics (bugs found vs. resolution rate) are compatible with each other — finding more bugs does not necessarily change what fraction developers act on. No contradiction.

- **Extends**: `blog-cursor-bugbot-effort-billing.md` (entire note) — May introduced configurable effort levels (default/high/custom), with high effort finding 35% more bugs vs. default at constant 80% resolution. June adds a cross-cutting baseline improvement (+10% bugs, 3x speed, 22% cost) that applies on top of the May effort-level system. Together these notes establish the full parameter space: the June note changes the floor (better baseline across all effort levels); the May note changes the ceiling (high effort finds 35% more bugs on top of the new baseline). Teams designing effort routing should account for both axes.

- **Extends**: `blog-cursor-bugbot-learning.md` (entire note) — April 2026 documented the learned-rules mechanism and the trajectory from 52% (July 2025 launch) to ~80% (April 2026). The June improvement (+10% more bugs detected) continues the improvement trajectory via a different mechanism: model upgrade rather than online learning. The two improvement vectors (learned rules + model quality) are additive — Bugbot now benefits from both a stronger underlying model and a learned-rules layer that adapts to team patterns. Neither mechanism is sufficient alone; the combination is the current production state.

- **Extends**: `blog-cursor-composer-2-5.md` Claim 1 — May 2026 established Composer 2.5 as "a substantial improvement in intelligence and behavior over Composer 2" for "sustained work on long-running tasks." This June post reveals a concrete downstream application: Bugbot running on Composer 2.5 achieves 10% more bug detection and 3x speed improvement. This is the first specific performance delta attributed to the Composer 2.5 upgrade in a production workflow.

- **Novel**: The following patterns are not documented in any other source note in the corpus:
  - **Pre-push AI code review with post-push deduplication**: The `/review` command pattern — run before push, deduplicate against post-push trigger, leave audit trail comment — is a new harness integration pattern for AI code review. No prior source documents this pre-push + deduplication architecture for a production AI code review tool.
  - **P90 runtime SLA for AI code review**: The "90% of runs finish in under three minutes" metric is the first published runtime SLA-style figure for any AI code review tool in the corpus. Prior sources discuss review quality (resolution rate, bug detection), not runtime distribution.
  - **Incremental review mode**: Limiting AI review to only genuinely new changes within a PR update cycle is a new configuration pattern for reducing review noise. No prior source documents this as a production option.
  - **Model block list fallback for AI code review**: The pattern of respecting org-level model block lists with automatic fallback is a new enterprise governance pattern for AI review tools. Enterprise practitioners with compliance constraints should note this.

## Guide Impact

- **Chapter on AI-Assisted Code Review (Ch07 or equivalent)**: 
  - Add P90 < 3 minute runtime figure as the current Bugbot performance baseline — the first published runtime SLA for an AI code review tool. Teams setting CI timeout budgets can use this as a starting point.
  - Update the cost baseline from $1.00–$1.50/run (May 2026, `blog-cursor-bugbot-effort-billing.md` Claim 3) to ~$0.78–$1.17/run (June 2026 implied, 22% reduction). Note the reduction is specifically for orgs using Composer 2.5 (see model block list caveat, Claim 7).
  - Add the pre-push `/review` pattern as a new integration point alongside the existing post-push GitHub/GitLab trigger pattern.

- **Chapter on Harness Engineering (Ch02)**:
  - Add the pre-push + post-push deduplication pattern as a design reference. The `/review` → GitHub/GitLab sync → skip-if-already-reviewed flow is a reusable architecture for any AI review agent that can be invoked at multiple workflow points.
  - Add incremental review mode as a "review scope" configuration dimension. Teams with high PR-update frequency (many small pushes to a single PR) should evaluate whether incremental mode reduces reviewer fatigue from re-surfaced findings.

- **Chapter on Team Adoption (Ch05)**:
  - Update cost modeling from the May 2026 figures to the June 2026 figures (22% reduction). Teams that evaluated Bugbot economics against the May baseline should recalculate.
  - Add the model block list caveat: orgs with Composer 2.5 opt-out may not realize the headline performance improvements. Teams with compliance-driven model restrictions should validate actual performance in their environment.

- **Chapter on Agent Execution and Control (Ch04)**:
  - The P90 < 3 min runtime distribution is directly actionable for agents that orchestrate Bugbot as a step in a pipeline. Agents should set timeouts at the P99 (likely 5–10 min) rather than P90 to handle tail cases.
  - The model block list + fallback pattern is a generalizable design principle: AI agents operating in enterprise environments should declare what model they run on and expose their fallback behavior — not silently degrade.

## Extraction Notes

1. **Source is intentionally concise**: The post is a 4-minute read structured around four sections ("Run Bugbot before you push," "Only review what's new in your PR," "How we got here," "Learn more"). Full content was read. The brevity is a deliberate product announcement format — technical details of the Composer 2.5 training improvements that drive the quality gains are in `blog-cursor-composer-2-5.md`, not reprised here.

2. **All metrics are relative, baselines unstated**: "3x faster," "22% cheaper," and "10% more bugs" are all relative to an implicit prior version. The May 2026 billing post provides the only published absolute baseline (cost: $1.00–$1.50/run; resolution rate: 80%). The prior absolute runtime figure has never been published. Treat all three relative metrics as directional rather than precisely calculable.

3. **"10% more bugs" vs. resolution rate**: "10% more bugs per review" (detection count improvement) is distinct from "resolution rate" (fraction of flagged bugs acted on before merge). The April and May posts focused on resolution rate (78.13% → 80%). This June post uses a different metric. The two metrics are independently meaningful — finding more bugs is good even if the fraction resolved stays at 80%, because more bugs found × 80% resolved = more bugs fixed. No contradiction, but readers should not conflate the metrics.

4. **CLI support pending**: Pre-push `/review` is available in Cursor 3.7+ and cursor.com/agents only. CLI support is "coming soon" — teams using Claude Code or other CLI-based workflows will need to wait. The practical implication: pre-push review requires the Cursor IDE or web interface at present.

5. **No contradictions filed**: The June improvements extend the May and April data without opposing any prior claims. The 22% cost reduction is additive to the May billing model change. The 10% bug detection improvement is additive to the April 78.13% baseline and May 80% resolution rate. No contradiction issue needed.
