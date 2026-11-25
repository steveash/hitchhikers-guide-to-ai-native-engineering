---
source_url: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-essay-challenge
source_type: blog-post
title: "The Pragmatic Engineer Essay Challenge: Category Winners (Part 1)"
author: Gergely Orosz, Jessica Salmon, Ivan Klaric (excerpting reader essays by Anton Zaides, David Veszelovszki, Jacob Bartlett and others)
date_published: 2026-11-24
date_extracted: 2026-11-25
last_checked: 2026-11-25
status: current
confidence_overall: anecdotal
issue: "#4945"
---

# The Pragmatic Engineer Essay Challenge: Category Winners (Part 1)

> Excerpts from three category-winning reader essays (HoneyBook EM, a solo Claude Code builder, a Granola iOS engineer) plus runner-up snippets, giving self-reported accounts of review collapse (two reviewers to zero), extreme solo throughput with "no code reviews", and parallel-agent workflows.

## Source Context

- **Type**: blog-post (secondary roundup: edited excerpts of reader essays from The Pragmatic Engineer's 5th-anniversary essay contest; grand prize went to Neil Kakkar, already covered in `blog-pragmaticengineer-kakkar-two-eras-of-shipping.md`)
- **Author credibility**: Orosz is a long-running, trusted industry analyst. The essay authors are practitioners writing about their own experience: Anton Zaides (EM at HoneyBook), David Veszelovszki (solo creator of Cmdr, ex-Sourcegraph), Jacob Bartlett (engineer at Granola).
- **Scope**: Three categories: "What happens when AI writes all the code?", "Essays by solo builders and tiny teams", "Reflections on AI". Only excerpts are included; most essays are linked, not reproduced, so detail beyond the excerpts (e.g., Veszelovszki's "automated checks and balances", PostHog's deep review agents) is not available here. All metrics are self-reported; several come from a vendor dashboard (Weave) or LoC counts, which the author concedes are imperfect.

## Extracted Claims

### Claim 1: Optional code review decayed from two reviewers per PR to zero within a couple of months at HoneyBook, followed by a buggy, duplicated codebase
- **Evidence**: First-hand account by an EM across three repos with different review regimes (ai-workflows: two reviewers; atlas-vibe: barely any PRs; backend: optional review). Author-reported; no defect metrics given.
- **Confidence**: anecdotal
- **Quote**: "So, in the span of a couple of months, we dropped from two people reviewing and understanding the code, to zero!"
- **Our assessment**: A rare first-hand description of review erosion happening by drift rather than policy. The stated outcome ("a buggy codebase full of duplications and non-optimal patterns") is qualitative only. Contrast with Kakkar's team, where human review was removed deliberately and replaced with an agent reviewer.

### Claim 2: Optional review is quickly abandoned because shipping immediately is addictive
- **Evidence**: Author's observation of his own team's behaviour in the backend repo.
- **Confidence**: anecdotal
- **Quote**: "Slowly, it became more and more tempting to just not ask for reviews. It’s addicting to just develop a feature and immediately have it in production."
- **Our assessment**: Plausible behavioural mechanism. Implication: "review optional" is not a stable policy; if review is wanted for some change classes it needs enforcement (risk tiers, required checks).

### Claim 3: Review creates peer pressure that drives the author's own understanding; without it, authors cut corners on comprehension
- **Evidence**: Author's reflection; no measurement.
- **Confidence**: anecdotal
- **Quote**: "It took me a while to understand that the code review stage contains a lot of peer pressure."
- **Our assessment**: Useful reframing: a hidden function of review is accountability for comprehension, not just defect-finding. He also states a norm that "it’s still your responsibility to read and understand it" and that "You can’t let Claude make the decisions and ‘drive’ the work", yet reports that norm eroded anyway. Suggests individual-responsibility norms alone are weak.

### Claim 4: One EM's personal PR throughput rose from ~1/week to 20+/week and parallel sessions from 2-3 to 6-8
- **Evidence**: Self-reported; charts sourced to Weave (a vendor "normalized units of work for an expert engineer" metric). PR count is gameable; the author notes the PRs also grew in seriousness (small side features in March-June, more serious work later).
- **Confidence**: anecdotal
- **Quote**: "From last October until March this year, I averaged one PR a week. Currently, it’s 20+."
- **Our assessment**: Data point for the upper range of individual PR counts, similar in spirit to Kakkar's 11x. The EM-returns-to-hands-on claim ("to be a good EM there is absolutely no other way than to join the building activity") is opinion.

### Claim 5: Non-engineers shipping production code creates review and quality burden (10k-line PR with dummy data)
- **Evidence**: Single anecdote opening the essay: a designer's 10k-line production PR with "dummy data where backend calls were supposed to be". Runner-up Ygor Cardoso's essay is described as covering "the extra work created for devs when non-engineers start to contribute code".
- **Confidence**: anecdotal
- **Quote**: "Not only is it full of hacky solutions (not even talking about criminal useEffect abuses), it also has dummy data where backend calls were supposed to be."
- **Our assessment**: Concrete failure symptom: placeholder/mock data surviving into a PR meant for production. Supports gating non-engineer contributions behind checks.

### Claim 6: A solo builder reports ~1.4M LoC and 12,003 commits in 10 months with Claude Code, and estimates 80-100x speedup over no-AI
- **Evidence**: Author's own repo statistics: "1.4M LoC", 1,674 changelog entries, 12,003 commits (~15/workday in Jan to ~160/workday in Oct), 67 releases. Baseline: 194 LoC/active day at Sourcegraph (2022-2025). The author concedes "Lines of code is far from a perfect metric" and applies a 33% "AI bloat" discount himself.
- **Confidence**: anecdotal
- **Quote**: "12,003 commits (avg. ~55/workday, but increased from ~15/workday in Jan to ~160/workday in Oct, so about 10x!)."
- **Our assessment**: Do not cite the 60-100x as a productivity effect: LoC is a poor proxy, the baseline is a different (reviewed, multi-person) context, and nobody independent verified the output. The commits/workday growth within a single project is the less-confounded signal, but it is also commit-granularity dependent.

### Claim 7: The solo workflow is no specs, no skills, no code review, and manual QA at the end, grasping the product but not the code
- **Evidence**: The author's own bullet list of his workflow (Claude Code with Opus 5.5 medium, single 20x Max plan).
- **Confidence**: anecdotal
- **Quote**: "Grasping 100% of the product level, 0% of the code level"
- **Our assessment**: Extreme end of the spectrum, and explicitly conditioned by the author on being solo. Minimal-ceremony prompting works for him in a codebase he owns alone, but the essay excerpt gives no defect/incident data. The author separately says he uses "automated checks and balances architecture work to keep the code in order" (per Orosz's summary), so "no review" does not mean "no verification"; those details are only in the unreproduced full essay.

### Claim 8: Batching many small tickets to subagents in rounds closed 42 GitHub issues in one day
- **Evidence**: Description of the 2026-10-01 session; author gave Claude ~10 tickets at a time, to be done "with subagents, then merge and push it at the end, make CI happy", repeated in four rounds; a human made initial decisions and edited UI copy strings (about five minutes) before shipping.
- **Confidence**: anecdotal
- **Quote**: "On 2026-10-01, I closed these 42 GitHub issues total."
- **Our assessment**: Concrete, reproducible-looking batching pattern (ticket batch -> subagents -> merge -> CI green). Human-in-loop points: initial decisions and user-facing copy. Note the scope disclaimer that this "didn’t directly touch humans".

### Claim 9: The solo advantage is the absence of coordination overhead, so the speed does not generalise to teams
- **Evidence**: Author's own caveat.
- **Confidence**: anecdotal
- **Quote**: "My advantage as a solo eng is that I don’t have any of that overhead."
- **Our assessment**: Important self-conditioning. Agrees with Kakkar's decomposition (removed coordination/review overhead matters as much as AI) and should travel with any quotation of the 100x figure. Also flags a human cost: "building at crazy speeds can be addictive" and "makes sleep relatively costly".

### Claim 10: Bartlett's parallel workflow rests on three learned skills: designing verification steps, planning alongside agents, and context switching; parallel git checkouts enable multiple concurrent agent projects
- **Evidence**: First-person account of building the Meeting Bar feature in "20% time" while doing a standard job, in an 11-month-old iOS codebase, with a relaxed token-spend attitude and alignment with the mobile lead on the architectural destination.
- **Confidence**: anecdotal
- **Quote**: "I’d just learned to parallelise my work across multiple git checkouts, and I’d been honing my ability to define iOS verification steps."
- **Our assessment**: Corroborates parallel-checkout practice and verification-as-skill. Success was conditioned on stated enablers (small codebase, spend tolerance, agreed architecture), which the author lists himself. The essay's full month-by-month breakdown is not in the excerpt.

### Claim 11: The engineer's role is shifting from "rowing" to "steering", and from hand-crafting to machining (tooling and sampling)
- **Evidence**: Opinion essays by runner-ups Bruno Felix (CTO, XEO360, 8 people) and Paul D'Ambra (PostHog); D'Ambra explicitly limits scope: "things have changed less for folks working on systems with critical safety requirements, or high performance systems".
- **Confidence**: anecdotal
- **Quote**: "the main activity of a software engineer is shifting from rowing (focusing on one thing at a time and producing good code) to steering (managing multiple workstreams, context switching all day, and exercising sound judgment throughout)."
- **Our assessment**: Framing, not evidence. Useful vocabulary; D'Ambra's prediction that "continuous integration and review will change next" matches the bottleneck-migration thesis in Kakkar's note. The XEO360 excerpt also admits the shift is "mentally taxing".

### Claim 12: Runner-up data points: a migration estimated at ~3 years per platform finished in under one; internal hackathon yielded ~60 skills; AI spend reached $2M/year; one sole developer deploys 50+ times/day
- **Evidence**: Orosz's one-line summaries of Moreau (Devolutions, 250 people, 1,500-screen app) and Warren (Blend Supply). The underlying numbers are in linked essays not reproduced here.
- **Confidence**: anecdotal
- **Quote**: "A migration that should have taken ~3 years, per platform, was completed in less than one for Windows and Linux. Other platforms look promising"
- **Our assessment**: Headline figures with no method visible; treat as leads. Moreau's context includes company-mandated AI-native transition (voluntary departure package offered), which is a confounder. Spend figure is useful alongside `blog-pragmaticengineer-orosz-roi-of-ai-spend.md`.

### Claim 13: The "80/20 rule": 80% of the work is easy to get done alone with AI, but people are needed for the final 20%
- **Evidence**: One bullet in Orosz's summary of Carlo Beschi's 16-item list (Treatwell, 700 staff).
- **Confidence**: anecdotal
- **Quote**: "This says that 80% of the work is easy to get done alone with AI, but people are needed for the final 20%."
- **Our assessment**: A widely repeated heuristic; no data here. Minor value.

## Concrete Artifacts

```
Veszelovszki's self-described workflow (from ‘I’m a 100x engineer now!’ excerpt):
Claude Code with Opus 5.5 medium in a terminal, a single 20x Max plan
Few-liner prompts and no specs
No skills
Almost no rule files now
No reading specs/plans. Manual QA at the end
No code reviews
Claude-maintained dev&prod infra
Grasping 100% of the product level, 0% of the code level
```

```
Veszelovszki's ticket-batching prompt (paraphrase quoted by author, 2026-10-01):
"Hey, I’m painting a room today. Could you find 10 smaller tickets to do on your own, with subagents, then merge and push it at the end, make CI happy."
Rounds: 10 tickets, 10 more, 8-12 UI bugs as a category, a fourth round. Total 42 issues closed that day.
```

```
Zaides' three-repo review regimes (HoneyBook):
ai-workflows: every PR reviewed by at least two people including the author
atlas-vibe (thin frontend): barely any PRs, vibe-coded, improving repo skills
backend: optional code reviews -> zero reviewers within a couple of months
Parallel sessions: 2-3 -> 6-8. PRs: ~1/week (Oct-Mar) -> 20+/week
```

```
Veszelovszki's metrics (self-reported): Cmdr 1.4M LoC (+800k lines translations/docs) in 10 months;
1,674 changelog entries (~40/month Jan-Feb -> 230-350/month Aug-Oct);
12,003 commits; 67 releases (~2/week). Baseline: 194 LoC per active day at Sourcegraph 2022-2025.
```

## Cross-References

- **Corroborates:**
  - `blog-pragmaticengineer-kakkar-two-eras-of-shipping.md` Claim 2 (human PR review absent in practice) and Claim 7 (removing review and communication overhead matters as much as AI): Zaides reaches zero reviewers by drift, Veszelovszki by solo-ness. Same publisher, same contest; Kakkar is the grand-prize essay.
  - `blog-pragmaticengineer-orosz-gill-software-factories-code-review.md` Claim 2 (review-exempt list with strike system): shows what a governed version of reduced review looks like versus HoneyBook's ungoverned drift.
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 6 (blast-radius risk tiering): HoneyBook's per-repo regimes (strict review for shared ai-workflows, none for the thin frontend) are an informal tiering; the backend's optional-review tier is the one that collapsed.
  - `blog-addyosmani-agentic-code-review.md` Claim 2 (31.3% rise in PRs merging with zero review, per Faros data cited there): Zaides is a first-hand instance of that trend.
- **Contradicts:** None filed. Veszelovszki's "no code reviews, manual QA at the end" is a different context (solo, owned product) from sources recommending review tiers, so it is a conditioning variable rather than a contradiction. The author's own Claim 9 caveat supports this reading.
- **Extends:**
  - `blog-pragmaticengineer-orosz-roi-of-ai-spend.md` Claim 2 (PR-frequency tiers): adds named individual data points (20+ PRs/week for an EM; Heartbeat, Blend Supply anecdotes).
  - `blog-pragmaticengineer-orosz-roi-of-ai-spend.md` Claim 12 (story-level metrics are a more credible velocity signal than PR counts): these essays mostly use PR/commit/LoC counts, which that note warns against; Veszelovszki's changelog-entry count is closer to a value-based metric.
- **Novel:** (a) The mechanism claim that review supplies peer pressure for comprehension, so removing it lowers authors' own understanding; (b) the observed drift from optional review to no review; (c) the 42-issue subagent batching session with its human-in-loop points; (d) the non-engineer 10k-line PR failure symptom (dummy data left in).

## Guide Impact

- **Chapter 03 (Verification / review)**: Add HoneyBook as a cautionary example: "optional review" is unstable and decayed to zero reviewers in a couple of months, with duplication and non-optimal patterns reported. Recommend explicit risk tiers or required checks over optional review (cite alongside code-review-approaches Claim 6). Add the "review as accountability for comprehension" framing, attributed as experience, not finding.
- **Chapter 01 (Daily workflows)**: Add the ticket-batching-to-subagents pattern (Veszelovszki) and the parallel-git-checkout plus verification-step design (Bartlett) as attributed practitioner examples. Mention parallel session growth 2-3 -> 6-8 (Zaides) as one self-reported data point, not a target.
- **Chapter 05 (Team adoption)**: Warn that solo-builder speedups (60-100x claims) do not transfer to teams, citing the author's own caveat that the advantage is zero coordination overhead; add the non-engineer-contributor risk (10k-line PR with dummy data) and the sleep/addiction cost noted by two authors.
- **Chapter 00 (Principles)**: Optional low-priority: the "rowing to steering" vocabulary and PostHog's "machinist" framing. Do not use the LoC/commit multipliers as evidence.

## Extraction Notes

- Fetched the full article HTML and read all of it (approx. 39k characters of text). Quotes were copied from the extracted text of the page; curly apostrophes are preserved as in the source. Cited essays are linked from the article but were not followed: the triage comments note that most are linked, not included, and the Miner brief limits extraction to what is in the article body.
- Part 2 (the other three category winners) is announced but not published in this article; it will need a separate issue.
- The triage comments listed Bartlett as lower priority, and the 2 reviewer-to-0 claim as primary; the note follows that weighting.
- Orosz's Takeaways section ("everyone recalled the massive change in pace with Opus 4.5 or 4.6") is an editorial generalisation across self-selected contest entries, not a measured result.
