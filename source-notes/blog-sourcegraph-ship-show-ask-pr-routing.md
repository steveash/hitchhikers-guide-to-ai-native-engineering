---
source_url: https://sourcegraph.com/blog/what-we-learned-building-a-pr-approval-bot
source_type: blog-post
title: "Keeping code moving with clearer review expectations"
author: Constantin Nicolae (Sourcegraph)
date_published: 2026-11-10
date_extracted: 2026-11-10
last_checked: 2026-11-10
status: current
confidence_overall: anecdotal
issue: "#4621"
---

# Keeping code moving with clearer review expectations

> Sourcegraph describes an internal experiment that routes each PR into Ship / Show / Ask using an agent-assessed diff plus a per-component author-familiarity rule, rolled out recommendations-only first; it reports no outcome metrics on review quality.

## Source Context

- **Type**: blog-post (experience report on an early internal experiment; no code or metrics)
- **Author credibility**: Sourcegraph engineer writing about their own team's workflow; Sourcegraph builds code search and agentic coding tools, so the post also promotes their Compare page. First-hand but self-reported.
- **Scope**: Covers the motivation (review bottleneck, stamp group, single approval gate), the Ship/Show/Ask policy, the familiarity rule, the hard override, the rollout method, and open questions. Does not give quantified results, false-positive rates, or the actual prompts/rules. A follow-up post on post-merge review and bot interruptions is promised.
- **Note**: The URL slug ("what-we-learned-building-a-pr-approval-bot") differs from the page title.

## Extracted Claims

### Claim 1: Agent-accelerated writing shifts the bottleneck to review, and a single approval gate fits routine and discussion-worthy changes badly
- **Evidence**: Description of Sourcegraph's own setup: a "stamp group" for small PRs and a GitHub rule requiring one approval for every merge.
- **Confidence**: emerging
- **Quote**: "We had different expectations for review, but we were fitting them into one approval requirement."
- **Our assessment**: Plausible and consistent with other sources, but anecdotal and not measured here. The useful detail is the stamp-group pattern ("Can someone stamp this?") as a concrete cost of uniform approval.

### Claim 2: Review paths can be made explicit with Ship / Show / Ask definitions applied to PRs
- **Evidence**: Policy definitions adopted from a 2021 Ship/Show/Ask article; used in the bot.
- **Confidence**: emerging
- **Quote**: "Show: someone should see the change, but their review can happen after merge."
- **Our assessment**: Gives a concrete three-tier vocabulary. Ship = no additional review under policy; Ask = review before merge. Tiering is by policy outcome rather than by author type.

### Claim 3: An agent inspects the diff and surrounding code and returns findings with evidence, while deterministic application code applies the rules and selects the path
- **Evidence**: Architectural description; the workflow runs in GitHub Actions.
- **Confidence**: emerging
- **Quote**: "It returns findings with supporting evidence, and application code applies our rules to select a review path and post the result on the PR."
- **Our assessment**: Worth highlighting: the LLM produces evidence, not the decision. Separating assessment from policy application makes decisions auditable and the rules editable without retuning a prompt.

### Claim 4: Familiarity is operationalised as two merged PRs reviewed by another person plus a relevant contribution in the past 30 days, per component
- **Evidence**: Stated as the "current policy"; later refined through feedback ("the evidence required to establish familiarity").
- **Confidence**: anecdotal
- **Quote**: "our current policy looks for two merged PRs reviewed by another person, plus a relevant contribution of code, tests, or technical documentation in the past 30 days."
- **Our assessment**: Concrete, copyable thresholds, but no justification for 2 PRs / 30 days is given. Treat as one team's starting point.

### Claim 5: Some change categories always require review regardless of author experience
- **Evidence**: Stated policy rule.
- **Confidence**: emerging
- **Quote**: "Changes to authentication checks or to how sensitive data is exposed require review regardless of experience."
- **Our assessment**: A sensible hard override that bounds the risk of familiarity-based auto-approval. Matches blast-radius tiering in other sources.

### Claim 6: Rollout began recommendations-only, with human review unchanged, before enabling approvals
- **Evidence**: Process description; feedback was used to refine rules and re-check affected recommendations.
- **Confidence**: emerging
- **Quote**: "We started with recommendations only, while human review continued as usual."
- **Our assessment**: A transferable shadow-mode rollout for any approval automation. Note the post does not report how long shadow mode lasted or the disagreement rate, and does not clearly state that approvals have since been enabled.

### Claim 7: Review serves distinct purposes (catch problems, share context, check customer-facing claims), and naming them helps decide when a second person is needed
- **Evidence**: Lesson from the feedback phase; anecdotal.
- **Confidence**: anecdotal
- **Quote**: "It can catch a problem, share context, or check what we tell customers."
- **Our assessment**: Useful framing: Show tier mainly sacrifices the "catch" purpose before merge while keeping context-sharing. Not elaborated further in the post.

### Claim 8: Familiarity must be scoped to the component actually changed; contribution history is evidence, not proof
- **Evidence**: Lesson from feedback; no examples given.
- **Confidence**: anecdotal
- **Quote**: "Working in one part of a system doesn't imply familiarity with all of it."
- **Our assessment**: Real weakness of any history-based trust heuristic; the post doesn't say how component boundaries are defined.

### Claim 9: Exposing the bot's reasoning made decisions challengeable and fed policy improvement
- **Evidence**: Anecdotal team experience.
- **Confidence**: anecdotal
- **Quote**: "We could challenge the assumptions behind a recommendation and work out whether the rule or the assessment needed to change."
- **Our assessment**: Good practice: distinguishing "rule wrong" from "assessment wrong" gives a debugging split.

### Claim 10: The bot's own comments are an attention cost; deciding when it speaks, updates, or stays quiet is part of the design
- **Evidence**: Stated as a lesson; no measurements.
- **Confidence**: anecdotal
- **Quote**: "Comments and repeated assessments can become interruptions of their own."
- **Our assessment**: Consistent with other automated-review sources; the follow-up post is meant to quantify this.

### Claim 11: Fewer stamp requests are not evidence of better review; Show's post-merge attention is unverified
- **Evidence**: The authors' own caveat.
- **Confidence**: settled (as an authors' admission of what is not shown)
- **Quote**: "Fewer stamp requests tell us little about review quality."
- **Our assessment**: The only reported outcome is reduced stamp requests, which the authors themselves discount. The guide should cite this as policy design, not demonstrated results. Open risk: "With Show, removing the wait means relying on someone to return after merge."

## Concrete Artifacts

Policy as described in the post (paraphrased summary of the quoted definitions; Sourcegraph blog, "Ship, Show, or Ask" and "How the agent works"):

```
Ship: "no additional review is needed under our policy."
Show: "someone should see the change, but their review can happen after merge."
Ask:  "someone needs to review the change before it merges."

Familiarity (per component):
  two merged PRs reviewed by another person
  + a relevant contribution of code, tests, or technical documentation
  in the past 30 days

Override: changes to authentication checks or to how sensitive data is
exposed require review regardless of experience.

Pipeline: agent examines PR diff, relevant code, author's previous
contributions -> findings + evidence -> application code applies rules
-> review path posted on the PR (runs in GitHub Actions).
```

## Cross-References

- **Corroborates**: `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review effort by blast radius) and Claim 11 (human-on-the-loop sampling rather than reading every diff): the auth/sensitive-data override and Show tier are concrete implementations of these ideas. `blog-cursor-agent-autonomy-auto-review.md` Claim 1 (autonomy as a "dial rather than a switch"): Ship/Show/Ask is a three-position dial for PR review.
- **Contradicts**: None found; no contradiction issue filed.
- **Extends**: `blog-cursor-bugbot-learning.md` (feedback-driven refinement of automated review rules); here the feedback loop applies to routing rules, not bug findings. Adjacent: `docs-github-copilot-pr-review-stage-metrics.md`, `blog-cognition-what-we-learned-building-cloud-agents.md` (loosely related).
- **Novel**: Ship/Show/Ask PR routing; author-familiarity-based review gating with explicit thresholds; recommendations-only shadow rollout for approval automation; LLM-for-evidence plus deterministic-code-for-decision split in review routing.

## Guide Impact

- **Chapter 05** (Code Review When AI Wrote It / review-as-bottleneck): add Ship/Show/Ask as a worked example of tiered review paths, with the familiarity rule and auth/sensitive-data override, flagged as an early, unmeasured internal experiment.
- **Chapter 03** (Layer 4 Human Review): note that automated approval routing needs hard overrides for security-sensitive changes and a shadow-mode phase before enabling approvals.
- **Chapter 01** (rubber-stamp guidance): mention explicit review expectations as an alternative to ad-hoc "can someone stamp this" requests, with the caveat that fewer stamp requests do not show review quality.

## Extraction Notes

- Read the full page (fetched raw HTML and stripped markup; quotes copied from that text). Page is short and contains no code or metrics. The post cites a 2021 Ship/Show/Ask article, a simulation study on pre/post-commit review, and a 2026 preprint on Meta's RADAR; those links were not followed (not substantive within this post).
- Confidence is anecdotal: single team, early experiment, no outcome data.
