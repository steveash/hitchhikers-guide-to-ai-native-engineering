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

- **Type**: blog-post (podcast episode page with takeaways, timestamps and reference links)
- **Author credibility**: Orosz is an ex-Uber engineering manager and author of The Pragmatic Engineer. The interviewee is a Uber Distinguished Engineer speaking first-hand about internal systems.
- **Scope**: Uber's pre-AI tooling, model gateway, harness wrapper, spend governance, code review, CI, productivity measurement, and the changing engineer role. No independent metrics.

## Extracted Claims

### Claim 1: A single model- and harness-agnostic gateway (since 2023) has been a durable platform decision
- **Evidence**: Interview statement; the gateway reportedly supports multiple vendors and open models and hosts AI Guard (security), spend tracking and audit visibility.
- **Confidence**: emerging
- **Quote**: "A single AI model gateway has paid lots of dividends."
- **Our assessment**: Credible and consistent with common platform practice. First-hand but unquantified; the dividends are not measured in the page.

### Claim 2: AIFX lets engineers switch between Claude Code, Codex and OpenCode without losing settings, skills and plugins
- **Evidence**: Interview description of an internal wrapper CLI.
- **Confidence**: emerging
- **Quote**: "AIFX allows engineers to switch harnesses without losing settings."
- **Our assessment**: A concrete harness-portability pattern. The page gives no adoption data or implementation detail.

### Claim 3: Per-engineer spend is governed by tiers, with manager approval to exceed and a CostCheck plugin for cost tips
- **Evidence**: Interview description of policy and tooling.
- **Confidence**: emerging
- **Quote**: "engineers get allocated a spend tier."
- **Our assessment**: Gives the internal mechanism behind the Bloomberg-reported caps. Exact tier values are not given in the portions we could read.

### Claim 4: CostCheck gives cross-session cost-improvement tips
- **Evidence**: Interview description.
- **Confidence**: anecdotal
- **Quote**: "A plugin called CostCheck works across sessions and gives tips on how to improve an engineer’s cost profile."
- **Our assessment**: Feedback-to-the-engineer is a distinct lever from hard caps. No effect size is reported.

### Claim 5: Uber says token costs fell about 50% over recent months
- **Evidence**: Self-reported; no baseline, method or published metric.
- **Confidence**: anecdotal
- **Quote**: "Uber has reduced token costs by about 50% the last few months"
- **Our assessment**: Treat as a claim, not a measurement. Cause (routing, tiers, CostCheck, cheaper models) is not attributed in what we read.

### Claim 6: CI load forced an internal "code red"; simple checks moved to an agent-run inner loop
- **Evidence**: Interview statement that CI jobs more than doubled in 12 months (per the page takeaways); no further numbers found.
- **Confidence**: emerging
- **Quote**: "Uber had to declare an internal “code red” for its CI system earlier this year."
- **Our assessment**: Plausible downstream effect of agent-generated PR volume. Useful pattern: shift cheap checks left to the agent.

### Claim 7: Agents run `afx validate` before opening a PR
- **Evidence**: Description of the mechanism for lint, build and template rules.
- **Confidence**: emerging
- **Quote**: "agents run these commands with the _afx validate_ command before opening a PR."
- **Our assessment**: Concrete example of a pre-PR validation command as a harness feature.

### Claim 8: Uber tags every PR by type to replace raw PR velocity
- **Evidence**: Interview statement; feature share reportedly rising and maintenance share falling, with no numbers.
- **Confidence**: emerging
- **Quote**: "So Uber now tags all PRs by type: feature, bugfix, maintenance, testing, or docs."
- **Our assessment**: Sensible response to PR-count inflation. The trend is unquantified.

### Claim 9: Code review is now a major bottleneck, even with AI review, screenshots/videos and risk scores
- **Evidence**: Interviewee's own admission.
- **Confidence**: emerging
- **Quote**: "Uday admits that code review has become a big bottleneck inside the company,"
- **Our assessment**: Corroborates the wider review-bottleneck theme. Note this is Orosz's paraphrase, not Uday's words.

### Claim 10: The engineer's job is building context for agents
- **Evidence**: Opinion of the interviewee, supported by the Uber workflow described.
- **Confidence**: anecdotal
- **Quote**: "The job of a software engineer inside a place like Uber is to build context."
- **Our assessment**: Strong framing, weak evidence beyond testimony.

### Claim 11: Prior decade of internal tooling (e.g., DevPods, 2017) made agent tooling fast to build
- **Evidence**: Interview summary on the page.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Platform foundations compound; plausible survivorship-flavored claim from one large firm.

## Concrete Artifacts

```
Uber internal tools named in the source (Orosz page):
- Model Gateway (since 2023) + AI Guard, spend tracking, audit visibility
- AIFX (wrapper across Claude Code, Codex, OpenCode)
- CostCheck plugin
- `afx validate` (agent pre-PR check)
PR type tags: feature, bugfix, maintenance, testing, docs
```

## Cross-References

- **Corroborates**: `blog-simonwillison-uber-caps-usage.md` Claims 1–2 (Uber spending pressure and caps); `blog-pragmaticengineer-orosz-state-of-tech-industry-2026.md` Claim 9 (Uber AI cost reduction); `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 5 (Uber uReview) on the review burden.
- **Contradicts**: None found. (Caps in Bloomberg reporting are per-tool dollar limits; here tiers with manager override. Different mechanism descriptions, not opposing claims.)
- **Extends**: `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 13 (Uber tool inventory incl. AIFX, which cited this deep dive without fetching it) — this note adds the gateway, CostCheck, `afx validate`, and PR tagging.
- **Novel**: Harness-agnostic gateway plus wrapper, agent-run CI inner loop, PR-type tagging replacing PR velocity.

## Guide Impact

- **Chapter 02**: Add the Model Gateway + AIFX as an example of harness portability (settings/skills/plugins carried across harnesses).
- **Chapter 04**: Cite "context is the job" framing and the pre-PR `afx validate` inner loop as a pattern for moving cheap CI checks to the agent.
- **Chapter 05**: Cite PR-type tagging as an alternative to PR velocity, and spend tiers with manager sign-off as a cost-governance mechanism; flag the 50% figure as unverified.

## Extraction Notes

- The fetch tool returned the page's takeaways/description, not a full transcript; the page references a transcript but its text was not available to us. Quotes are from the page's takeaway text (several are Orosz's narration, not Uday's direct words).
- Quotes were retrieved via a summarizing fetch tool and should be spot-checked by the Assayer against the page.
- The claim that CI jobs "more than doubled in 12 months" is taken from the page summary and the triage; not independently quoted.
- Chapter mapping is approximate (triage comments disagreed on numbering).
