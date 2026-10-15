---
source_url: https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside
source_type: blog-post
title: "Uber's AI infra, from the inside"
author: Gergely Orosz (The Pragmatic Engineer), interviewing Uday Kiran Medisetty (Uber Distinguished Engineer)
date_published: 2026-10-14
date_extracted: 2026-10-15
last_checked: 2026-10-15
status: current
confidence_overall: emerging
issue: "#4132"
---

# Uber's AI infra, from the inside

> A first-hand interview describing Uber's harness-agnostic Model Gateway, AIFX wrapper, tiered token spend, agent-run CI inner loop, and PR-type tagging; mechanisms are concrete, headline numbers are self-reported.

## Source Context

- **Type**: blog-post (podcast episode page with Orosz's written takeaways, timestamps, reference links, and an embedded ~93-minute episode transcript)
- **Author credibility**: Orosz is an ex-Uber engineering manager and author of The Pragmatic Engineer. The interviewee is an Uber Distinguished Engineer speaking first-hand about internal systems.
- **Scope**: Uber's pre-AI tooling, model gateway, harness wrapper, spend governance, code review, CI, productivity measurement, and the changing engineer role. No independent metrics.
- **Who is speaking**: The page's numbered takeaways are **Orosz's narration** summarizing the episode. Only text the page puts in quotation marks after "In Uday's words" / "As Uday reflects" is Uday's own wording. Transcript quotes below are labelled with timestamp and speaker (SPEAKER_00 = Uday, SPEAKER_01 = Orosz in the transcript's diarization).

## Extracted Claims

### Claim 1: A single model- and harness-agnostic gateway (since 2023) has been a durable platform decision
- **Evidence**: Orosz's takeaway #4, backed by Uday's transcript description: the gateway exposes one OpenAI-compatible or Anthropic-compatible API over open- and closed-weight models, and hosts AI Guard (security middleware), per-user/per-caller attribution, spend tracking, audit logging and session traces.
- **Confidence**: emerging
- **Quote**: "A single AI model gateway has paid lots of dividends." (Orosz narration, takeaway #4). Uday, transcript [0:23:32]: "Every model request at Uber goes through this."
- **Our assessment**: Credible and consistent with common platform practice. First-hand but unquantified; the dividends are not measured.

### Claim 2: AIFX lets engineers switch between Claude Code, Codex and OpenCode without losing settings, skills and plugins
- **Evidence**: Orosz's takeaway #5; Uday's transcript description adds that AIFX is pre-installed on DevPods, uses "personas" that ship default plugins and skills, syncs central and user-specific settings across environments, and adds a status line with spend tracking across harnesses.
- **Confidence**: emerging
- **Quote**: "AIFX allows engineers to switch harnesses without losing settings." (Orosz narration, takeaway #5)
- **Our assessment**: A concrete harness-portability pattern. No adoption data or implementation detail beyond the description.

### Claim 3: Per-engineer spend is governed by multiple tiers, with lightweight manager approval to move up
- **Evidence**: Orosz's takeaway #6 plus Uday in the transcript. Uday describes a default tier, "many levels of tiers", a request plus manager approval framed as an ROI conversation, and a separate tier for background coding agents distinct from interactive harnesses.
- **Confidence**: emerging
- **Quote**: "engineers get allocated a spend tier." and "When they hit the limit, their manager can sign off to spend more in that month." (Orosz narration, takeaway #6). Uday, transcript [0:25:57]: "So by default, you get certain, certain tier." Transcript [0:27:08]: "We have a separate independent tier."
- **Our assessment**: This is the internal mechanism behind the Bloomberg-reported caps. **Tier dollar values are not stated anywhere in the episode.** We checked the full transcript, and Uday only says "certain tier", so the absence is in the source, not in our read.

### Claim 4: CostCheck gives personalized, cross-session cost-improvement tips
- **Evidence**: Orosz's takeaway #6 plus Uday's transcript. CostCheck runs across all of an engineer's sessions and gives personalized tips based on usage and per-project spend. Uday ties it to "real-time coaching" on context and model sizing.
- **Confidence**: anecdotal
- **Quote**: "A plugin called CostCheck works across sessions and gives tips on how to improve an engineer’s cost profile." (Orosz narration, takeaway #6). Uday, transcript [0:27:41]: "a plugin called cost check that will run across all of your sessions"
- **Our assessment**: Feedback to the engineer is a lever distinct from the hard tiers in Claim 3. No effect size is reported, and the episode gives no further detail on how CostCheck works.

### Claim 5: Uber says token costs fell about 50% over recent months
- **Evidence**: Self-reported in Orosz's narration, which links back to his earlier coverage ("as we previously covered"). The figure is **not** stated by Uday anywhere in the transcript. No baseline or method is given.
- **Confidence**: anecdotal
- **Quote**: "Uber has reduced token costs by about 50% the last few months" (Orosz narration, takeaway #6)
- **Our assessment**: Treat this as a claim, not a measurement. It restates `blog-pragmaticengineer-orosz-state-of-tech-industry-2026.md` Claim 9, which attributes Uber's 50%+ cut to model routing and lower-cost models. It is not independent corroboration, because both come from Orosz.

### Claim 6: CI load forced an internal "code red"; simple checks moved to an agent-run inner loop
- **Evidence**: Orosz's takeaway #8 states that CI jobs more than doubled in 12 months. Uday confirms it in the transcript [0:57:39–0:57:43] (the ASR renders "code red" as "code read"). Uday ties the increase to rising year-over-year PR volume.
- **Confidence**: emerging
- **Quote**: "Uber had to declare an internal “code red” for its CI system earlier this year." and "This was because CI jobs more than doubled in a 12-month timeframe" (Orosz narration, takeaway #8). Uday, transcript [0:57:43]: "the number of CI jobs also doubled or more than doubled."
- **Our assessment**: A plausible downstream effect of agent-generated PR volume, consistent with `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 5 (Linear: 5x PRs). The pattern is useful: shift cheap checks left to the agent. The doubling figure is self-reported, with no absolute numbers.

### Claim 7: Agents run `afx validate` before opening a PR
- **Evidence**: Orosz's takeaway #8; Uday in the transcript lists linter, coverage rules, build rules and template rules behind one command, followed by visual and staging validation and a "self-healing CI" for failures after PR creation.
- **Confidence**: emerging
- **Quote**: "so agents run these commands with the afx validate command before opening a PR." (Orosz narration, takeaway #8). Uday, transcript [0:55:21]: "and we kept all of this behind one single command like AI FX validate."
- **Our assessment**: A concrete example of a pre-PR validation command built into the harness.

### Claim 8: Uber tags every PR by type, moving from "diff velocity" toward feature velocity
- **Evidence**: Orosz's takeaway #9 plus Uday in the transcript [1:23:07–1:24:05]. Uday says PRs are also tagged by complexity, that the feature-PR share is rising and the maintenance share is falling, and that AI now auto-clusters PRs and tags missing ones to compute P50 feature velocity per half. The trend has no numbers.
- **Confidence**: emerging
- **Quote**: "So Uber now tags all PRs by type: feature, bugfix, maintenance, testing, or docs." (Orosz narration, takeaway #9). Uday, transcript [1:23:07]: "we are internally talking about not necessarily just diff velocity,"
- **Our assessment**: A sensible response to PR-count inflation (see `slow-down-speed-up` Claim 5). The trend is unquantified.

### Claim 9: Code review is a major bottleneck even with AI review, screenshots/videos and risk scores; a human still reviews every PR
- **Evidence**: Orosz's takeaway #7 and Uday's direct statement in the transcript. Uday adds that "green lane" auto-landing for low-risk PRs is a future possibility, not current practice.
- **Confidence**: anecdotal (one company's self-report; the "bottleneck" framing is common but unmeasured here)
- **Quote**: "Uday admits that code review has become a big bottleneck inside the company," (Orosz narration, takeaway #7). Uday, transcript [0:54:56]: "I think reviews become a big bottleneck, same as like any other company."
- **Our assessment**: Corroborates the wider review-bottleneck theme. It ties to the PR-volume inflation in `slow-down-speed-up` Claim 5.

### Claim 10: The engineer's job is building context for agents, plus multitasking and verification
- **Evidence**: Uday's opinion (quoted directly on the page), framed by Orosz's takeaway #10 heading.
- **Confidence**: anecdotal
- **Quote**: "The job of a software engineer inside a place like Uber is to build context." (Orosz narration, takeaway #10 heading). Uday, as quoted on the page: "The job of engineering is, in some sense: ‘how do you build the right context for the agents to produce reliable output?’" and "You need to get really good at context engineering."
- **Our assessment**: A strong framing with weak evidence beyond testimony.

### Claim 11: Uber's AI tooling built quickly on a decade of prior dev-tooling investment (e.g., DevPods from 2017 powering Minion)
- **Evidence**: Orosz's takeaway #11 gives examples: Minion (2025) runs on DevPods (2017), MCP Gateway reused the Thrift/Protobuf registries, and Jaeger tracing helped Slate routing and the Context graph. Uday is quoted directly. In the outro, Orosz says companies with pre-AI developer-platform teams seem to benefit most.
- **Confidence**: anecdotal
- **Quote**: "Uber’s AI tooling was seemingly built in a year: in reality, it was built on top of a decade worth of dev tooling investment." (Orosz narration, takeaway #11). Uday, as quoted on the page: "All the things that we built to make life easier for engineers: it makes it easier for our agents as well!"
- **Our assessment**: Platform foundations compound. The claim is plausible but survivorship-flavored, drawn from one large firm with unusual platform investment.

## Concrete Artifacts

```
Uber internal tools named in the source (Orosz page + transcript):
- Model Gateway (late 2023, built on Michelangelo) + AI Guard, per-user spend tracking, audit logs, session traces
- AIFX / "AI Foundations" (wrapper across Claude Code, Codex, OpenCode; personas with default skills/plugins; synced settings; spend status line)
- Spend tiers: default tier -> request + manager approval for next tier; separate tier for background coding agents
- CostCheck plugin (cross-session, personalized cost tips)
- `afx validate` (agent pre-PR check: linter, coverage, build, template rules)
- Self-healing CI; Code Inbox (risk score, blast radius)
PR type tags: feature, bugfix, maintenance, testing, docs (+ complexity level)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-uber-caps-usage.md` Claims 1–2 (Uber spending pressure and caps) → Claims 3–4 here. `blog-pragmaticengineer-orosz-state-of-tech-industry-2026.md` Claim 9 (Uber cuts per-token cost by 50%+ through model routing and open models) → Claim 5 here. It has the same author, so it is not independent. `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 5 (Uber uReview) → Claim 9 here (review burden). `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 5 (Linear: teams using agents ship 5x as many PRs) → the PR-volume inflation behind Claims 6, 8 and 9 here.
- **Contradicts**: None found. Bloomberg describes the caps as per-tool dollar limits; this source describes tiers with manager override. These are different descriptions of the mechanism, not opposing claims.
- **Extends**: `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 13 (Uber tool inventory, including AIFX). This note adds the gateway, spend tiers, CostCheck, `afx validate`, and PR tagging.
- **Novel**: A harness-agnostic gateway plus wrapper, an agent-run CI inner loop, and PR-type tagging in place of PR velocity.

## Guide Impact

Chapter numbers were checked against `guide/`:

- **Chapter 02 (Harness Engineering) → "Multi-Tool Configuration"**: Add the Model Gateway + AIFX as an org-scale example of harness portability (settings, skills and plugins carried across Claude Code, Codex and OpenCode).
- **Chapter 03 (Verification) → "CI"**: Cite `afx validate` as a pattern for moving cheap CI checks into the agent's pre-PR inner loop, and cite the CI "code red" as the pressure that motivated it.
- **Chapter 04 (Context Engineering)**: Cite Uday's "build the right context for the agents" framing as practitioner testimony.
- **Chapter 05 (Team Adoption) → "Measuring Impact"**: Cite PR-type tagging and feature velocity as an alternative to PR or diff velocity. Under **"Code Review When AI Wrote It"**, cite Uber's human-reviews-every-PR stance with risk signals. Cite spend tiers with manager sign-off and CostCheck as a cost-governance mechanism, and flag the 50% figure as unverified.

## Extraction Notes

- Quotes were verified verbatim against the raw page HTML and against the episode's transcript JSON, which is linked from the page (`transcription.json` on substackcdn). The full transcript was read for the gateway, AIFX, spend, CI, code-review, measurement and outro sections.
- The transcript is machine-generated ASR with diarization. Transcript quotes are copied exactly, including ASR errors (e.g., "AI FX validate", "cost check"), and each is labelled with its timestamp.
- Tier values and CostCheck internals are not given anywhere in the episode, so they cannot be extracted.
- The "Pragmatic Engineer deepdives" reference links on the page were not followed. They are earlier Orosz articles, and the Uber-relevant ones are already covered by the cross-referenced notes.
