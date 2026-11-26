---
source_url: https://newsletter.pragmaticengineer.com/p/how-anthropic-builds-software-in
source_type: blog-post
title: "How Anthropic builds software in 2026 with Katelyn Lesse"
author: Gergely Orosz (The Pragmatic Engineer), interviewing Katelyn Lesse (Anthropic)
date_published: 2026-11-25
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: emerging
issue: "#4968"
---

# How Anthropic builds software in 2026 with Katelyn Lesse

> Podcast-episode write-up in which Anthropic's platform engineering lead describes the Python-to-Rust Messages API rewrite verified by shadowing, a Claude review-routing classifier, an oncall-triage agent, and team/hiring/promotion changes, all as self-reported practice.

## Source Context

- **Type**: blog-post (newsletter page for a ~1h50m podcast episode; the page contains Orosz's 12 written takeaways plus the episode blurb. The full transcript was not available in the fetched text.)
- **Author credibility**: Orosz is a well-known engineering writer; Lesse leads platform engineering at Anthropic (owns the Claude API and infrastructure for Claude Code / Claude Desktop), previously led engineering teams at Stripe. First-hand but self-reported by the vendor; no metrics beyond one estimate (~20%).
- **Scope**: Rust rewrite verification, code-review classifier, oncall agent, onboarding, team structure, interviews, promotion. Does NOT give implementation detail of the migration (see the primary source in `blog-anthropic-migrating-messages-api-rust.md`).

## Extracted Claims

### Claim 1: The Messages API was rewritten from a Python monolith to Rust in about five months by a few engineers, none Rust experts
- **Evidence**: Lesse's account as summarized by Orosz; corroborated by Anthropic's own write-up (published the same day).
- **Confidence**: emerging
- **Quote**: "It took a few engineers and a few months in total; all without anyone being expert in Rust!"
- **Our assessment**: Plausible and consistent with the primary source. Orosz's heading says "around five months"; the quote gives "a few months". Vendor-reported.

### Claim 2: A year earlier the team chose Go because engineers could read it; by 2026 Claude's Rust ability changed that calculus
- **Evidence**: Lesse's account of language choice; no data.
- **Confidence**: anecdotal
- **Quote**: "A year earlier, the same team picked Go for their new services because it was a language that team members knew how to read and write."
- **Our assessment**: Notable shift: language choice no longer bounded by what humans can read. Related: Lesse says "Knowing a programming language well is starting to not matter" (Orosz's heading for takeaway 10). One engineer's view; not measured.

### Claim 3: The old Python API served as a "perfect test harness"; Rust shadowed it until responses were identical, replacing strict code review
- **Evidence**: Description of the shadowing design; details in the primary source (replay model output to both, fingerprint diffs).
- **Confidence**: emerging
- **Quote**: "They set up the new Rust API to shadow the current API, and iterated until all responses were identical."
- **Our assessment**: Corroborates the primary source's thesis that production parity, not tests, was the oracle. Note the tension in the primary source: it also reports human review at the seam and a reward-hacking incident, so "did not do strict code reviews" should be read as "no line-by-line review", not "no review".

### Claim 4: Engineers closely read only ~20% of the generated Rust, because the work was made verifiable
- **Evidence**: Lesse's estimate ("Katelyn estimates"), no measurement.
- **Confidence**: anecdotal
- **Quote**: "As long as you can really boil something down to make it verifiable in some way, then you don’t have to look at every single line of Rust code that’s getting written."
- **Our assessment**: Strong statement of the verification-substitutes-for-review principle, but the 20% is an estimate and the conditional ("as long as...verifiable") carries the weight. Applies where a behavioral oracle exists.

### Claim 5: A Claude classifier runs on all PRs and decides whether human review is needed, how many reviewers, and which team
- **Evidence**: Description of the system; no accuracy or volume data.
- **Confidence**: emerging
- **Quote**: "The company has a Claude code review classifier running for all pull requests."
- **Our assessment**: Concrete three-output design (need / count / routing). Risk scoring plus "additional rules" decides count; the rules are not disclosed.

### Claim 6: Mechanical, low-risk changes (SDK bump, newer model) can skip human review; flaky-test fixes are reviewed, merged and deployed by another Claude
- **Evidence**: Examples given by Lesse via Orosz.
- **Confidence**: anecdotal
- **Quote**: "This is also the case for fixing flaky tests, in which case, another Claude does the review, then merges and deploys it."
- **Our assessment**: Goes further than `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 7, which says a human still manually merged even low-risk AI-approved changes. Likely a temporal/scope difference (different team or later date), not filed as a contradiction; flagged for the Smith.

### Claim 7: A Claude agent now categorizes incoming API oncall alerts as "real" or "noise" before a human is paged; autonomous incident handling is a goal, not reality
- **Evidence**: Agent shadowed the rotation "for months" for training before being given first-look triage.
- **Confidence**: emerging
- **Quote**: "The long-term goal is for Claude to handle actual incidents without waking up a human – but they’re not there yet."
- **Our assessment**: Shows a shadow-then-promote rollout pattern (run in shadow mode, build confidence, then grant a role), echoing the shadow-traffic idea in the rewrite. Consistent with `blog-pragmaticengineer-ai-sre-oncall.md` Claims 3 and 5 (investigation and triage, humans keep decisions).

### Claim 8: New engineers onboard by asking Claude, which is connected to the codebase and internal systems, instead of onboarding buddies
- **Evidence**: Description only.
- **Confidence**: anecdotal
- **Quote**: "Not so at Anthropic, where Claude is connected to the codebase and internal systems, and engineers just ask it to explain how things work."
- **Our assessment**: Plausible; Orosz notes OpenAI engineers use Codex similarly. Loss of mentorship/social effects is not discussed.

### Claim 9: Planning and cross-team alignment time has not shrunk; engineers spend more time coordinating than implementing
- **Evidence**: Lesse's statement; team interacts with Inference, Research, Safety, App.
- **Confidence**: anecdotal
- **Quote**: "The average engineer actually spends more time coordinating than on implementation!"
- **Our assessment**: Supports the view that coding speed-ups do not remove coordination bottlenecks; matches `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 2 (PRD still used for coordination).

### Claim 10: Teams remain two-pizza (5-8 people) and own, and are paged for, their systems; a team, not an individual, owns each system
- **Evidence**: Lesse's rationale: right size for understanding a complex system and staffing an oncall rotation.
- **Confidence**: anecdotal
- **Quote**: "Teams at Anthropic are still two-pizza teams of around 5-8 people."
- **Our assessment**: Useful counterweight to "one-engineer" narratives (compare the Bun rewrite's one-engineer framing in `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 9). Conditioning variable: production services with oncall vs. single-project rewrites. The article's wording "5-8" conflicts mildly with the "maximum of two engineers" teaser in `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 15, which refers to per-project staffing, not team size.

### Claim 11: Engineers spend much more time building tooling to accelerate their own work
- **Evidence**: One example: an engineer set up a Slack channel running a multi-agent team toward a single goal, not an assigned task.
- **Confidence**: anecdotal
- **Quote**: "Even on product teams, engineers are spending a lot more time building tools that help them to accelerate their own work."
- **Our assessment**: Consistent with the "harness building" theme; single example.

### Claim 12: The coding interview was phased out because strong candidates failed it; agent-assisted interviews are being trialed; design and project deep-dive interviews unchanged
- **Evidence**: Lesse's team's experience; no replacement finalized.
- **Confidence**: anecdotal
- **Quote**: "Candidates who crushed other interviews were starting to fail the coding one because they no longer write code by hand."
- **Our assessment**: Contrasts with `blog-pragmaticengineer-neetcode-interview.md` Claim 2 (Google reinstating in-person coding interviews to counter AI cheating). Different responses to the same problem (signal loss); a conditioning difference, not filed as a contradiction.

### Claim 13: Promotion no longer weighs "time to complete a project"; impact (CPU saved, latency reduced, incidents avoided) is used instead
- **Evidence**: Lesse's description; levels and promotion process remain.
- **Confidence**: anecdotal
- **Quote**: "But the time taken to completion is pretty meaningless when a year-long project can now be done in days or weeks with AI!"
- **Our assessment**: Interesting for Ch05 performance-evaluation guidance; impact examples are infra-centric and may not generalize to product roles.

### Claim 14: Engineers anxious about their skills have plenty of agent-infrastructure work to solve
- **Evidence**: Lesse's message, written up in her blog post.
- **Confidence**: anecdotal
- **Quote**: "It’s an incredibly exciting time to put your skills to work."
- **Our assessment**: Motivational, low evidentiary value; included for completeness.

## Concrete Artifacts

Classifier outputs (Orosz's summary of Lesse, "Anthropic has its own code review agent running at all times"):

```
Claude code review classifier, per PR:
1. Does it need a human review?   (mechanical / low-risk -> no; flaky-test fix -> another Claude reviews, merges, deploys)
2. How many human reviews?        (Claude scores risk + additional rules)
3. Which team reviews?            (Claude routes the PR)
```

Episode timestamps (page text, selected): Rust rewrite 10:21, shadow traffic verification 23:40, onboarding with Claude 31:11, oncall with Claude 1:06:41, coding interviews 1:24:13. No code, config, or metrics beyond the "~20%" estimate.

## Cross-References

- **Corroborates**: `blog-anthropic-migrating-messages-api-rust.md` (same migration; Claim 6 replay-once shadowing and Claim 13 on human judgment defining "correct"). This note adds the practitioner view and the ~20% estimate. `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 6 (blast-radius tiering at Anthropic). `blog-pragmaticengineer-ai-sre-oncall.md` Claim 5 (AI summary before human arrives).
- **Contradicts**: None filed. Mild tension: Claim 6 above vs. `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 7 (human manually merges low-risk changes); likely temporal. Claim 12 vs. `blog-pragmaticengineer-neetcode-interview.md` Claim 2 is a differing response rather than a factual conflict.
- **Extends**: `blog-pragmaticengineer-orosz-inside-anthropic.md` (same guest, July 2026): adds review-routing classifier, oncall agent, interview and promotion changes, and Rust rewrite. `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 8 (tests as merge criterion): here the oracle is production, not a test suite.
- **Novel**: Three-output review classifier (need/count/team); oncall agent in shadow-then-triage rollout; Anthropic dropping the hand-written coding interview; promotion based on impact not time-to-complete; ~20% human-read estimate for a verifiable rewrite.

## Guide Impact

- **Chapter 03 (verification)**: Cite the "~20% read closely when verifiable" statement as a practitioner data point alongside the primary source's shadow-traffic design; stress that it is an estimate and conditional on a behavioral oracle.
- **Chapter 01 (daily workflows)**: Add the three-output review classifier (need / count / team) and agent-first onboarding as examples.
- **Chapter 05 (team adoption)**: Add the interview redesign, impact-based promotion, and unchanged two-pizza team sizing as one organization's reported changes, with the Google counterexample noted.

## Extraction Notes

- Fetched the page HTML and extracted text; read the whole article body (blurb, 12 takeaways, closing quote). The page is a summary; the full transcript was not in the text, so claims are Orosz's rendering of Lesse, and quotes are from Orosz's prose except where attributed to Lesse (Claim 4, Claim 14).
- Did not follow the linked Anthropic migration post here (already mined in `blog-anthropic-migrating-messages-api-rust.md`, issue #4963).
- Triage mentioned "response-identity as the acceptance test"; the page says responses were "identical".
- No contradiction issue filed.
