---
source_url: https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
source_type: research-report
title: "How AI Is Transforming Work at Anthropic"
author: Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern, Deep Ganguli (Anthropic Societal Impacts)
date_published: 2025-12-02
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.4 — Ch 05 Team Adoption discovery"
---

# How AI Is Transforming Work at Anthropic

> A mixed-methods internal study of Anthropic employees combining a 132-respondent survey, 53 in-depth interviews, and Clio analysis of 200,000 internal Claude Code transcripts across two six-month-apart snapshots (Feb 2025 → Aug 2025). Provides the most rigorous "company-wide AI adoption" dataset publicly available, with the load-bearing finding that senior engineers at the most AI-enthusiastic company in the world still cannot fully delegate the majority of their work — even with unlimited model access, no procurement friction, and a culture that rewards AI use.

## Source Context

- **Type**: research-report (vendor-internal study, mixed methods, with explicit methodology and limitations sections — this is unusually rigorous for a vendor publication)
- **Author credibility**: All seven authors are on Anthropic's Societal Impacts team, which has a track record of publishing methodologically transparent work (the same team built Clio, the privacy-preserving analysis tool used here, and has published on it at academic venues). Deep Ganguli is the team lead and has prior peer-reviewed publications. This is a vendor publication, but the methodology is closer to a research paper than a marketing piece.
- **Scope**: Internal Anthropic employees only. Covers both engineering and non-engineering teams. Combines self-report (survey + interviews) with behavioral data (Claude Code logs). Does NOT include external comparison groups, does NOT measure code quality outcomes (no static analysis, no incident data), does NOT compare against pre-AI baselines (only Feb 2025 vs. Aug 2025 snapshots).

## Methodology

### Three data sources
1. **Survey**: 132 engineers and researchers (31% response rate from targeted Slack outreach)
2. **Interviews**: 53 in-depth qualitative interviews with first-respondent survey participants
3. **Usage logs**: 200,000 internal Claude Code transcripts, sampled proportionally from February 2025 and August 2025
4. **Analysis tool**: Clio (Anthropic's privacy-preserving conversation analysis tool)
5. **Task taxonomy**: Eight categories — debugging, code understanding, refactoring, data science, front-end development, feature implementation, design/planning, "papercut fixes"
6. **Complexity scale**: 1–5 ("1 = basic edits, 5 = expert-level tasks")

### Time window
- Survey/interviews: August 2025
- Log comparison: February 2025 vs. August 2025 (6-month delta)
- Self-reported productivity recall: extended back 12 months

### Limitations explicitly acknowledged by authors
- **Selection bias**: engaged employees more likely to respond
- **Social desirability bias**: non-anonymous responses to one's own employer
- **Recency bias**: 12-month productivity recall
- **Self-report validity**: productivity claims difficult to validate independently
- **Proportional sampling**: cannot measure absolute changes in work volume, only relative shifts in mix

## Extracted Claims

### Claim 1: Anthropic engineers use Claude in 60% of their work, up from 28% one year prior
- **Evidence**: Self-report from 132-engineer survey, August 2025.
- **Confidence**: emerging (self-reported, internal sample, social-desirability bias)
- **Quote**: N/A (statistic stated directly in summary)
- **Our assessment**: This is the upper-bound number for what is possible inside the most aggressive AI-adopting engineering culture. Two implications for the team-adoption chapter: (1) The doubling year-over-year tells you the trajectory is real, not a fad. (2) The 60% ceiling — at the *most* AI-friendly company on Earth — tells you that 100% AI work is not the target, even aspirationally. A team that aims for "all code through AI" is aiming past the empirical ceiling. The honest framing: 60% is what looks like "transformation," not 100%.

### Claim 2: Engineers self-report a 50% productivity boost (up from 20% baseline a year prior)
- **Evidence**: Survey self-report, recall window 12 months.
- **Confidence**: anecdotal (self-report only, no instrumented validation, recall bias)
- **Quote**: N/A
- **Our assessment**: Take this with a grain of salt comparable in size to the claim itself. The METR study (pre-cutoff) found that experienced developers self-reported a 24% productivity gain while objective measurement showed a 19% *slowdown* on the same tasks. Self-reported productivity is the least reliable evidence we have. Cite this number only paired with the methodology limitation, never as a standalone metric. The directional finding ("self-reported productivity is up") is more reliable than the magnitude.

### Claim 3: 27% of Claude-assisted work consists of tasks that wouldn't have been done otherwise
- **Evidence**: Survey self-report.
- **Confidence**: emerging
- **Quote**: "27% of Claude-assisted work consists of tasks that wouldn't have been done otherwise"
- **Our assessment**: This is the most interesting metric in the report and the most under-discussed. It implies that a significant fraction of "AI productivity" is not "doing the same work faster" but "doing additional work that wasn't worth doing before." For the chapter's "Measuring impact" section, this is critical: a team that measures only "lines of code per engineer per week" or "PRs merged" will miss the entire 27%. The right metric is whether *new categories of work* are being done — quality-of-life improvements, exploratory prototypes, internal tools — not whether the existing backlog is moving faster. Connects directly to the "papercuts" finding (8.6% of tasks address quality-of-life improvements previously deprioritized).

### Claim 4: More than half of engineers report they can only "fully delegate" 0–20% of their work
- **Evidence**: Survey self-report.
- **Confidence**: emerging
- **Quote**: N/A
- **Our assessment**: This is the *single most important finding for the verification-before-autonomy section of the chapter*. At Anthropic, with the best models, the best harness, and the most experienced users, the majority of engineers say only 0–20% of their work is fully delegable. The remaining 80%+ requires human verification at some point in the loop. Any team-adoption playbook that promises "you can hand work off to agents" should set expectations against this number: even for the most AI-fluent engineers, full delegation is the exception, not the norm. Recommend leading the verification section with this stat verbatim.

### Claim 5: Claude Code autonomous tool calls doubled from ~10 to ~20 actions per task between Feb 2025 and Aug 2025
- **Evidence**: 200,000-transcript log analysis via Clio.
- **Confidence**: emerging (behavioral data, not self-report; but no external benchmark)
- **Quote**: N/A
- **Our assessment**: This is the strongest piece of behavioral evidence in the report — it is instrumented, not self-reported. The doubling of consecutive tool calls before human turns is a real signal that autonomy is increasing, not just confidence in autonomy. Pair this with the human-turn decrease (6.2 → 4.1 per task, -33%) for a coherent story: tasks are getting longer-horizon, with fewer human interruptions per task. The implication for team adoption is that the "right" review checkpoint is *not* fixed — it should slide outward as the team's harness and trust mature. A team rolling out agents in early 2026 should not adopt the verification cadence of Feb 2025 (turn-by-turn review) nor the Aug 2025 cadence (~20 actions per turn) without measuring their own harness's reliability first.

### Claim 6: Feature implementation grew from 14% to 37% of Claude Code usage; code design/planning grew from 1% to 10%
- **Evidence**: 200,000-transcript log analysis, two snapshots six months apart.
- **Confidence**: emerging
- **Quote**: N/A
- **Our assessment**: The shift from "Claude as autocomplete and explainer" to "Claude as feature-builder and designer" is the most significant qualitative change in the dataset. For the chapter's "Start with the harness" section: the harness needed for code-design tasks is fundamentally different from the harness needed for autocomplete. A team that starts with autocomplete-grade CLAUDE.md will hit a wall when their engineers try to use the same harness for feature implementation. Recommend the chapter explicitly stage the harness rollout to match this trajectory: start with refactoring/explanation harness, expand to feature harness, then add design/planning harness.

### Claim 7: Pre-training team uses Claude for 54.6% feature implementation; Security uses it for 48.9% code understanding; Non-technical staff uses it for 51.5% debugging
- **Evidence**: Log analysis broken down by team.
- **Confidence**: emerging
- **Quote**: N/A
- **Our assessment**: The team-by-team breakdown is the strongest support in the dataset for the chapter's central thesis that team adoption is not uniform — different teams use AI for different work. The pre-training team's 54.6% feature implementation is a researcher-engineer hybrid pattern that won't transfer to most product teams. The security team's 48.9% code understanding is the "use AI to read, not write" pattern. The non-technical staff's 51.5% debugging shows that "debugging" includes things like fixing broken Excel formulas or SQL queries, not just code defects. Use these as concrete examples in the chapter, not as targets.

### Claim 8: Engineers explicitly identify skill atrophy and supervision-paradox risks
- **Evidence**: Qualitative interview quotes.
- **Confidence**: emerging
- **Quote (skill atrophy)**: "When producing output is so easy and fast, it gets harder to actually take time to learn something."
- **Quote (collaboration loss)**: "I like working with people and it's sad that I need them less now."
- **Quote (career uncertainty)**: "I feel optimistic short-term but long-term AI will make me irrelevant."
- **Our assessment**: These are *Anthropic engineers* — the people building the agents — voicing concerns that are usually dismissed as outsider Luddism. For the "Common objections" section of the chapter, the key move is to re-frame these as legitimate concerns held by AI insiders, not as resistance from skeptics. The supervision-paradox concern (atrophied coding skills undermine ability to oversee AI output) is the most load-bearing — it directly contradicts the "AI lets juniors operate at senior level" framing. If senior engineers atrophy, the verification capacity that the staff+ adoption rate (Pragmatic Engineer survey) depends on will erode over time. The chapter should address this not as a future risk but as a present concern raised by the current heaviest users.

## Notable Omissions and Gaps

### What this report does NOT cover

1. **Code quality outcomes** — no static analysis data, no bug rate data, no incident data. The report measures *what* people are using AI for, not whether the AI output is good. Pair with Speed at the Cost of Quality (Miller et al.) for the quality side.
2. **Comparison to non-Anthropic teams** — the entire study is internal. Generalizability to teams that aren't building the model is unknown. Anthropic engineers have unique advantages: direct model access, internal slack channels with the model team, no procurement friction, no security review delays.
3. **Specific harness patterns** — the report mentions Claude Code usage but does not enumerate CLAUDE.md patterns, slash commands, or hooks. For harness specifics, use the Sentry profile and the older "How Anthropic teams use Claude Code" piece.
4. **Failure modes** — the report does not document tasks where Claude failed and engineers had to redo the work. The Faros paradox report and the CMU study cover the failure side.
5. **Adoption resistance** — the 31% survey response rate means 69% of targeted employees did not respond. The report does not analyze the non-respondent population. Skeptics may be in the long tail.

### Methodological caveats from the authors

- Cannot distinguish absolute work-volume changes from relative work-mix shifts
- Selection bias toward engaged employees
- Social desirability bias: respondents work for the company that makes the tool
- 12-month recall on productivity claims
- Two snapshots only (Feb + Aug 2025); no continuous longitudinal data

## Cross-References

- **Reinforces** the Pragmatic Engineer survey's 56% "≥70% of work with AI" figure. Anthropic's 60% internal figure is consistent with the broader senior-engineer audience, suggesting the ceiling is real and not Anthropic-specific.
- **Reinforces** the Sentry profile's verification-first stance (`gh-review.md` skeptical review command) — the >50% finding that engineers can only fully delegate 0–20% of work is the empirical justification for Sentry's "do not assume feedback is valid" stance.
- **Tension with** the Faros productivity-paradox claim that "individual output increases dramatically but organizational delivery stays flat." Anthropic reports both individual and organizational gains, but Anthropic's organizational structure (small teams, fast deploys, internal release loop ~60-100/day) is unusual. The contradiction may be a case of organizational structure mediating the AI productivity effect.
- **Complements** the Bessemer Shopify piece — Anthropic's Clio-based log analysis is more rigorous than Shopify's reversion-rate-and-demos approach, but Shopify's external-facing constraints are more typical.

## Guide Impact

### Chapter 05: Team Adoption

- **Section "Start with the harness"**: Use Claim 6 (feature implementation 14% → 37%) as evidence that harness needs evolve as usage matures. Recommend staging the harness rollout: explanation/refactoring first, feature implementation second, design/planning third.
- **Section "Verification before autonomy"**: Lead with Claim 4 verbatim ("more than half of Anthropic engineers can only fully delegate 0–20% of their work"). This is the empirical anchor for the entire section. Pair with Claim 5 (autonomy growing over time) to argue that verification cadence should be a sliding window calibrated to harness maturity, not a fixed checkpoint.
- **Section "Measuring impact"**: Use Claim 3 (27% of work wouldn't have been done otherwise) to push for "new categories of work" as a primary metric, not "lines per engineer." Critique the Faros approach as necessary but insufficient if it only measures backlog velocity.
- **Section "Common objections"**: Use Claim 8 quotes verbatim to neutralize the "objections come from skeptics who don't understand AI" framing. These objections come from Anthropic engineers. Treat them as load-bearing concerns, not noise.

### Chapter 04: Context Engineering

- The shift from autocomplete to feature implementation (Claim 6) implies that context budgets are now load-bearing for senior workflows, not optional for power users.

### Chapter 03: Safety and Verification

- Claim 4 (only 0–20% fully delegable) is the empirical floor for "what verification looks like at the most permissive end of the spectrum."

## Extraction Notes

1. **Date verification**: Multiple sources confirm publication on December 2, 2025. This is past the editorial cutoff (2025-12-01) by one day. Treat the data window (Feb–Aug 2025) as current-relevant since the trajectory it documents continues into the agentic era.
2. **Mixed methods strengthens the report**: Most vendor publications rely on a single data source (typically self-report). This report uses three (survey + interviews + behavioral logs) and explicitly cross-checks them. The rare cases where logs and self-report diverge are noted in the original.
3. **Clio analysis is reproducible-in-principle but not in practice**: Clio is described in a separate Anthropic paper. The 200k-transcript dataset is internal and not released. Replication is impossible from outside Anthropic.
4. **The "papercuts" finding is original**: 8.6% of tasks addressed previously deprioritized quality-of-life improvements. This is a novel category in the AI-impact literature and worth highlighting as a metric that doesn't exist in the standard developer-productivity playbook.
5. **Vendor caveat**: Anthropic published this. The findings flatter Anthropic's product. The methodology is rigorous enough to take the directional claims seriously, but treat magnitude claims (50% productivity boost) with the same caution as any vendor-published metric.
