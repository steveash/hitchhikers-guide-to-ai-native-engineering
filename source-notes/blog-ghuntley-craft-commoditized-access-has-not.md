---
source_url: https://ghuntley.com/access/
source_type: blog-post
title: "the craft has been commoditized, but access has not"
author: Geoffrey Huntley
date_published: 2026-10-02
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: anecdotal
issue: "#3861"
---

# the craft has been commoditized, but access has not

> A short opinion post arguing that AI has made everyone a potential software developer, that corporate role gatekeeping and agile process (built for scarce authorship) now lag that reality, and that the engineer's job becomes building safety systems that let anyone ship.

## Source Context

- **Type**: blog-post (personal blog, ghuntley.com, 2 Oct 2026). Short essay with an embedded video clip (credited to an X post), an embedded tweet by Ivan Burazin, and a "ps." on quality.
- **Author credibility**: Geoffrey Huntley is tracked in this corpus's trusted feeds for agentic coding technique (Ralph loops, spec-driven autonomy). That characterization comes from feed metadata, not the post. The post contains no data; claims are first-person opinion ("one of my hottest takes").
- **Scope**: Personalization of computers, game-dev democratization, corporate role gating, agile's assumptions, career risk for AI-rejecting engineers, hiring juniors, quality, and the redefined engineer job. It does not give any implementation guidance on how to build the "safety controls" or how to open access.

## Extracted Claims

### Claim 1: For ~40 years only programmers could make a computer truly personal; AI is only now delivering on that promise
- **Evidence**: Historical framing; no data.
- **Confidence**: anecdotal
- **Quote**: "If you didn't have these skills, you were given an interface, and your ability to personalize the computer or software was limited to what the interface could do."
- **Our assessment**: Compelling framing of the "access" thesis (capability gated by interface vs. by skill). Rhetorical rather than evidenced, but consistent with the democratization claims in other Huntley notes.

### Claim 2: In game development, anyone can now be a game developer by expressing intent and iterating through loops
- **Evidence**: Embedded ~1-minute video from an X post (not independently reviewed in the text; shown as a credit link). No metrics.
- **Confidence**: anecdotal
- **Quote**: "With AI, everyone is a game developer."
- **Our assessment**: Single-domain illustration. Plausible, but no evidence about quality, maintainability, or production readiness of the outcomes.

### Claim 3: At most corporates, building software is still a named role or job function, which is the access barrier
- **Evidence**: Author's observation; no examples named.
- **Confidence**: anecdotal
- **Quote**: "Yet, why is it that at most corporates right now, the responsibility to develop software is a named role or job function?"
- **Our assessment**: The central novel contribution: distinguishes an *organizational access* barrier from a *capability* barrier. Worth noting but asserted, not demonstrated. Rhetorical question rather than documented finding.

### Claim 4: 2026–2027 should be about enabling others in the organization to develop software; ignoring this is career self-sabotage
- **Evidence**: Opinion ("hottest takes").
- **Confidence**: anecdotal
- **Quote**: "One of my hottest takes right now is that 2026 and 2027 are all about enabling others in your organization to contribute to and develop software, and if your corporate roadmap doesn't have this on the agenda, you're missing the mark."
- **Our assessment**: A prescriptive prediction. Pair with caution: no cost/risk analysis of widening commit access (governance, security, maintenance burden).

### Claim 5: Corporate roles, processes and responsibility assignments must be rethought from first principles
- **Evidence**: Assertion.
- **Confidence**: anecdotal
- **Quote**: "This needs to be completely rethought from first principles, including who is responsible for these activities and what that entails."
- **Our assessment**: Directionally matches the Anthropic org note's role-blurring (PMs coding), which is better evidenced. Huntley supplies no concrete redesign.

### Claim 6: Agile optimized the delivery loop around scarce, expensive human authorship by a select few
- **Evidence**: Argument by assumption-breaking; no data.
- **Confidence**: anecdotal
- **Quote**: "Agile assumed writing software was the costly, scarce activity, so it optimized the loop around human authorship by a select few."
- **Our assessment**: Interesting, testable thesis (process assumptions encode a cost structure). Historical accuracy of agile's motivation is debatable; treat as a framing, not a finding.

### Claim 7: Engineers still hand-coding and rejecting AI should expect tough career conversations within six months — they have "failed the curiosity test"
- **Evidence**: Opinion, bolstered by an embedded tweet from Ivan Burazin about 28–30 year olds refusing AI tools (also anecdote).
- **Confidence**: anecdotal
- **Quote**: "you should be setting the stage for tough career conversations with that person within the next six months, because they have failed the curiosity test."
- **Our assessment**: Corroborates the "curiosity" theme in the Miami note, with a specific (unsupported) six-month timeline. Management-facing and somewhat coercive in tone; no evidence about outcomes.

### Claim 8: Hiring is a market, not a moral issue — juniors are cheaper and more AI-native, and there was never a market for "free-range organic software"
- **Evidence**: Argument; the section header is "don't hire left of the line". The header is stylistic and not elaborated in text.
- **Confidence**: anecdotal
- **Quote**: "There's never been a market for free-range organic software; it's always been about more, cheaper and sooner."
- **Our assessment**: Contrasts with Addy Osmani's skill-decay note, which stresses that junior reps must be deliberate. Huntley doesn't address how AI-native juniors build judgment. Dismisses IP/ethics objections ("it's been two years now...") without engaging them.

### Claim 9: There is no reason software quality should dip from AI adoption, since LLMs generate better code than 99% of companies could hire for
- **Evidence**: Assertion; no measurement.
- **Confidence**: anecdotal
- **Quote**: "These LLMs generate better code than 99% of companies could hire for."
- **Our assessment**: Unsupported quantitative claim (the 99% figure has no source) and in tension with notes on verification bottlenecks (e.g., Anthropic org Claim 1, Huntley's own engineer-away-slop). Treat with skepticism; use only as a stated position.

### Claim 10: The engineer's job becomes engineering systems and safety controls that let everyone ship to production safely
- **Evidence**: Concluding assertion.
- **Confidence**: anecdotal
- **Quote**: "Our job as software engineers now is to engineer systems, including safety controls, that let everyone ship to production — safely."
- **Our assessment**: The most actionable line: it reframes the role from authorship to guardrail/platform engineering. Consistent with engineer-away-slop (verification over creation). No specifics on which controls.

## Concrete Artifacts

No code, configs, or metrics. Embedded media only:

```
Embedded tweet (quoted in post): Ivan Burazin, 5 Mar 2026:
"I've never seen this before in my career: 28-30 year olds who refuse to use AI coding tools."
Embedded video credit: https://x.com/chasmmmmmmmmmmm/status/2105707774646562818 (game-dev example, 0:59)
```

## Cross-References

- **Corroborates**: `blog-ghuntley-miami-hot-takes.md` Claim 5 (curiosity as the determinant of career survival) and Claim 3 (computers gated to specialists, now malleable); `blog-ghuntley-engineer-away-slop.md` Claim 2 (authoring commoditized, everyone a developer) and Claim 5 (engineer's core job remains defect-free experiences); `blog-ghuntley-eighteen-month-recap.md` Claim 7 (non-engineers shipping software) and Claim 2 (democratization analogy); `blog-anthropic-ai-native-engineering-org.md` Claim 8 (role blurring).
- **Contradicts**: None filed. Tension (not a clean contradiction, so no issue filed): the "99% better code" quality claim vs. `blog-anthropic-ai-native-engineering-org.md` Claim 1 (verification and review became the bottleneck) — the latter is evidence-based, this is assertion. Also `blog-addyosmani-agentic-skill-decay.md` Claim 9 (expertise returns rising) vs. the "hire AI-native juniors" framing, which differ in context rather than directly oppose.
- **Extends**: `blog-ghuntley-miami-hot-takes.md` Claim 3 from individual capability to organizational gatekeeping; adds the agile-obsolescence argument.
- **Novel**: (a) "access vs. craft" framing — corporate role/job-function gating as the binding constraint; (b) the claim that agile encodes an authorship-scarcity assumption; (c) an explicit six-month career-conversation timeline for AI-rejecting engineers; (d) the explicit engineer-as-safety-system-builder job redefinition aimed at letting non-engineers ship.

## Guide Impact

- **Chapter 03 (teams/roles)**: Candidate text that "who may author software" is an organizational policy choice, not only a skill question; cite this post as a single, anecdotal position, paired with Anthropic org Claim 8 for evidence.
- **Chapter 04 (careers)**: Could add the "curiosity test" and six-month-timeline claim as a labeled opinion corroborating Miami Claim 5; flag it as unsupported by data.
- **Chapter 05 (quality/safety)**: Quote the "systems, including safety controls, that let everyone ship to production" framing as a role definition; do NOT cite the 99% quality claim as fact.
- **Chapter 02**: Optionally note the "agile assumed scarce authorship" hypothesis as something to test against process evidence from stronger sources.

## Extraction Notes

- Fetched the full page HTML and read the whole article (short; ~600 words). No sub-pages followed; the embedded X video and tweet were not independently opened, so claims about them rest on the post's captions only.
- Prospector comments disagreed on relevant chapters; this note lists impacts per the post's actual content.
- Source is thin on evidence; confidence is anecdotal throughout. Quotes copied verbatim from the page text.
