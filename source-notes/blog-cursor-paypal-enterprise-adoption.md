---
source_url: https://cursor.com/blog/paypal
source_type: blog-post
title: "Beyond efficiency: PayPal expands what's possible to build with AI"
author: Cursor Team (vendor case study; named practitioners from PayPal: Michelle Chance — Head of Developer Platforms; Prakhar Mehrotra — SVP and Global Head of AI)
date_published: 2026-05-11
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#696"
---

# Beyond Efficiency: PayPal Expands What's Possible to Build with AI

> The first enterprise-scale customer case study in the corpus from a major fintech (8,000 engineers, 400M+ customers) documenting organic AI adoption rollout, SDLC transformation from linear to iterative prototyping, role-boundary blur between engineers and product managers, disciplined metric selection (deployment frequency over % AI code), and a talent-retention signal absent from technical-pattern sources.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's commercial blog, May 11, 2026; approximately 600–800 words with four thematic sections and multiple attributed executive quotes)
- **Author credibility**: Two named PayPal executives provide direct quotes throughout: Michelle Chance (Head of Developer Platforms) and Prakhar Mehrotra (SVP and Global Head of AI). PayPal is a global payments platform responsible for over 400 million customers — a Fortune-100 scale regulated fintech. The organizational details (8,000 engineers, specific projects like the 3,000-app Java upgrade) are specific and attributable; the metrics (40% throughput, 6x speedup, daily deployment) are headline-level claims consistent with the named project. Published on Cursor's commercial blog — vendor-sourced marketing. Treat as practitioner evidence at emerging confidence.
- **Scope**: Covers PayPal's Cursor adoption rollout strategy, SDLC transformation patterns, role-boundary changes, metric discipline, and a talent-retention signal. Does NOT cover: specific tooling architecture (how Cursor is configured at PayPal), any competing tools evaluated or used alongside Cursor, technical details of the Java upgrade pipeline, how "change failure rate" is measured, or whether PayPal uses autonomous agent commits vs. purely AI-assisted human development.

## Extracted Claims

### Claim 1: PayPal's adoption rollout started with highest-impact teams building critical products requiring rapid market entry, then spread organically as engineers witnessed peer accomplishments

- **Evidence**: Vendor case study describes the rollout strategy explicitly: high-impact teams first, organic peer-to-peer spread afterward. Named metric: "Teams exceeding 90% Cursor adoption demonstrated dramatic improvements in deployment frequency and lead time."
- **Confidence**: emerging (vendor-sourced; the rollout description is specific and plausible; no independent validation)
- **Quote**: (no single direct quote summarizing the rollout strategy; see paraphrase in Our assessment)
- **Our assessment**: The organic-spread adoption strategy is explicitly described in the source rather than being inferred. PayPal did not force adoption org-wide from day one — they seeded it in the teams most likely to demonstrate value fastest, then relied on peer observation to generate pull. The 90% adoption threshold for "high-impact teams" is the first corpus datum on what adoption saturation looks like in a large enterprise context. This rollout pattern differs from NAB's intentional enablement approach (`blog-cursor-nab-legacy-migration.md` Claim 4) which used sprint days and structured training. Both patterns produced high adoption — the PayPal approach relied on organic social proof; the NAB approach relied on structured training on real production projects. These are context-conditioned strategies, not contradictions.

### Claim 2: High-impact teams shifted from weekly/biweekly deployment cadence to daily deployment within two weeks of Cursor adoption

- **Evidence**: Named metric with specific timeframe: "Within two weeks, these teams achieved daily deployments instead of weekly or biweekly cycles." This is the fastest individual-team adoption-to-outcome timeline in the corpus.
- **Confidence**: emerging (vendor case study; specific timeline; no cohort comparison or baseline definition)
- **Quote**: (no direct quote for this specific claim; described in the article narrative)
- **Our assessment**: A two-week timeline to deployment-cadence change is unusually fast. It implies the deployment bottleneck was code-production throughput (which AI addressed immediately), not infrastructure, review process, or release management friction. This is consistent with the source's framing of Cursor as accelerating from four sprints to one sprint (`blog-cursor-paypal-enterprise-adoption.md`, Claim 5 quote) — if development cycles compress 4x, deployment can become daily without any CI/CD changes. The two-week figure is memorable but should be read as "fastest teams reporting fastest changes" rather than a median enterprise outcome.

### Claim 3: PayPal's overall deployment cadence changed from monthly release cycles to daily releases as part of the AI-driven SDLC transformation

- **Evidence**: Stated as a before/after organizational metric. "High-adoption teams deploy multiple times daily versus once weekly previously." The monthly → daily shift represents a 20-30x deployment frequency increase for the highest-adoption teams.
- **Confidence**: emerging (vendor-sourced headline metric; no time window specified; vendor reports this as a current outcome)
- **Quote**: "Teams with high adoption are deploying faster and shipping with shorter lead times." — Michelle Chance, Head of Developer Platforms
- **Our assessment**: The deployment frequency change (monthly → daily at organizational level) is one of the three headline metrics in the source. Unlike the NAB case study (`blog-cursor-nab-legacy-migration.md` Claim 5) where the primary metric was timeline compression on a specific project, this is an operational cadence metric measuring ongoing delivery rhythm. It is consistent with `blog-cursor-amplitude-autonomous-pipeline.md` Claim 5's finding of 3x production commit growth at Amplitude. The mechanism at PayPal appears to be development acceleration (four sprints → one sprint) rather than autonomous agent commits — the source does not mention automated PR merging.

### Claim 4: PayPal projects a 40% increase in roadmap throughput for 2026 attributable to AI tool adoption

- **Evidence**: Headline metric in the article. Presented as a 2026 projection, not a realized figure.
- **Confidence**: anecdotal (self-reported projection from a vendor case study; no methodology for how "roadmap throughput" is defined or measured; vendor-sourced)
- **Quote**: (no direct quote attributing this metric to a named person; presented as an organizational headline)
- **Our assessment**: The 40% figure is the weakest evidentially of the three headline metrics. It is a projection rather than a realized measurement, and "roadmap throughput" is not defined. However, it is in the same order of magnitude as the NAB 3x project-compression metrics and consistent with the `blog-cursor-better-models-ambitious-work.md` behavioral study's +44% usage growth finding. The convergence of independently-arrived-at percentages in the 40–50% range across multiple enterprise cases is worth noting even if none of them is settled evidence.

### Claim 5: PayPal completed a 3,000-application Java upgrade in 2 months, compared to an 8-12 month original estimate — a 4-6x speedup on a large-scale migration

- **Evidence**: Specific project with before/after timeline: 3,000 applications, 2 months actual vs. 8-12 months estimated. This is the most concrete single data point in the source and the largest-scale legacy migration metric in the corpus.
- **Confidence**: emerging (named project with specific timelines; vendor-sourced; no independent validation; no description of what "complete" means in this context)
- **Quote**: (no direct quote about this specific project; described in the article as a key outcome)
- **Our assessment**: The 3,000-app Java upgrade is the corpus's first named enterprise-scale legacy migration metric at this magnitude. NAB's BizCalc migration (`blog-cursor-nab-legacy-migration.md` Claim 5) compressed 2-month pre-development to 1 week (8x) and expected 2-month full migration vs. 6-month estimate (3x). PayPal's 4-6x speedup across 3,000 apps is lower per-app velocity but the scope (3,000 apps vs. a single monolith) is dramatically larger. The mechanism is not described in detail — it is plausible that AI was used for automated code transformation rather than developer-assisted coding on each app individually. The guide should present these two migration cases together as enterprise-scale evidence that AI-assisted migration is empirically achievable, while noting that the PayPal case does not describe the technical approach.

### Claim 6: Traditional linear development (design → code → build → deploy) has shifted at PayPal toward rapid iterative prototyping — from idea to working prototype in hours

- **Evidence**: Article explicitly contrasts traditional linear SDLC with the new pattern. Attributed to team-level practice changes observed after Cursor adoption.
- **Confidence**: emerging (named practitioners; specific process description; vendor-sourced; no measurement of how widespread this pattern is within the 8,000-person org)
- **Quote**: "from idea to working prototype in hours, then iterate from there"
- **Our assessment**: The shift from waterfall-style linear SDLC to rapid iterative prototyping is consistent with the broader corpus narrative but this is the first explicit corporate-level statement that a major enterprise has documented this change as an outcome of AI tool adoption. The "hours" timeline for idea-to-prototype is also consistent with the `blog-cursor-better-models-ambitious-work.md` behavioral study's finding that developers shift toward higher-complexity and more expansive work after model upgrades — prototyping is a higher-complexity, more creative task than incremental feature work. The guide currently lacks an enterprise-scale validation that this SDLC shift is occurring beyond small teams.

### Claim 7: Role boundaries between product managers and engineers are blurring productively — PMs now bring functioning prototypes to engineers rather than documents, and engineers bring their own prototypes and design variations

- **Evidence**: Named quote from Michelle Chance describing a specific behavioral change in cross-functional collaboration.
- **Confidence**: anecdotal (single executive's characterization; not a measurement)
- **Quote**: "Roles that used to be very finite are blurring and we're seeing better product ideas come out of it." — Michelle Chance, Head of Developer Platforms
- **Our assessment**: This is the clearest statement in the corpus of AI-driven role-boundary change being beneficial rather than threatening. The mechanism is described explicitly: AI tools lower the cost of producing a working prototype enough that product managers can build one themselves rather than writing documents, and engineers can build design variations to show PMs rather than waiting for a spec. The "better product ideas" outcome is attributed to the collaboration itself — the claim is that cross-functional prototyping produces better ideas than sequential handoffs. This corroborates `blog-cursor-nab-legacy-migration.md` Claim 8 (Cursor brings engineers, architects, product, and security into the same workflow), but extends it from "same workflow" to "role boundary dissolution and better outcomes."

### Claim 8: PayPal deliberately tracks deployment frequency, lead time, and change failure rate as AI success metrics — and explicitly avoids % of AI-generated code as a metric because it incentivizes gaming

- **Evidence**: Named quote from Michelle Chance with an explicit anti-metric rationale. This is the most specific metric-discipline statement in the corpus.
- **Confidence**: emerging (named executive with direct quote; the rationale is specific and logically coherent)
- **Quote**: "If you measure it, you impact it. If you tell a developer their success is based on what percentage of code was generated by AI, they'll just ask AI to write verbose functions." — Michelle Chance, Head of Developer Platforms
- **Our assessment**: This is the most quotable and actionable single claim in the source. The anti-metric argument is specific and falsifiable: % AI-generated code is a gaming-susceptible metric because developers can optimize for the metric (ask AI to write verbose functions) without improving actual outcomes. The alternative metrics PayPal chose (deployment frequency, lead time, change failure rate) are the DORA core metrics — well-established DevOps outcome measures. This is the first corpus source to explicitly reject % AI code as a success metric with a named executive quote and a specific gaming mechanism. For the guide: this is the answer to "how do we measure AI adoption success?" — cite PayPal's choice and the specific reason % AI code fails.

### Claim 9: Prakhar Mehrotra frames AI as a fundamental paradigm shift from information distribution to intelligence — "AI is about intelligence, not information. It's a fundamentally different technology stack."

- **Evidence**: Named executive quote from SVP and Global Head of AI.
- **Confidence**: anecdotal (executive framing/philosophy statement; not an operational measurement)
- **Quote**: "AI is about intelligence, not information. It's a fundamentally different technology stack." — Prakhar Mehrotra, SVP and Global Head of AI
- **Our assessment**: This framing positions the PayPal transformation not as "productivity improvement" but as a fundamental technology layer shift — from distributing information to providing intelligence. The distinction is consequential: information distribution tools (documentation systems, wikis, search) are passive; intelligence tools (AI coding assistants, agents) are active and can produce novel outputs. For the guide: this is a useful leadership framing for the "what is AI-native engineering" chapter — it contrasts with pure velocity framing and positions AI as a new capability layer, not just a speed multiplier. It also aligns with the corpus-wide narrative that the right frame is "what becomes possible" (the source title) rather than "how much faster."

### Claim 10: Talent retention and recruiting has become a business outcome of AI tool adoption — developers want to work at PayPal specifically because it supports effective AI tools

- **Evidence**: Named executive quote from SVP and Global Head of AI.
- **Confidence**: anecdotal (executive characterization; no measurement of turnover or recruiting conversion rates)
- **Quote**: "The most important thing is our developers are participating in the AI journey. They want to come work for us because PayPal supports tools like Cursor." — Prakhar Mehrotra, SVP and Global Head of AI
- **Our assessment**: This is the first corpus source to explicitly name talent attraction and retention as a measurable business outcome of AI tool adoption. The implication: at PayPal's scale, developer experience (including AI tooling) has become a competitive differentiator in the talent market. This is distinct from productivity claims — it's a workforce strategy claim. For the guide: the talent-retention signal should appear in any section on justifying AI tool investment to leadership. The argument is not just "your engineers will be more productive" but "your engineers will choose to stay and new engineers will choose to join." This framing may be particularly useful for large enterprises competing with startups for developer talent.

### Claim 11: Michelle Chance uses "scrappy as a startup, but with all the funding and maturity of a large enterprise" as the desired outcome of AI tool adoption — enterprise AI enables startup-speed without startup-scale constraints

- **Evidence**: Named quote from Head of Developer Platforms.
- **Confidence**: anecdotal (aspirational framing; no measurement of how "scrappy" is defined or achieved)
- **Quote**: "For the first time we're able to see a real path to being as scrappy as a startup, but with all the funding and maturity of a large enterprise." — Michelle Chance, Head of Developer Platforms
- **Our assessment**: This is the clearest articulation in the corpus of the enterprise AI value proposition as experienced by a practitioner: the goal is not to move at startup speed and lose enterprise capabilities, but to access startup-style iteration velocity while retaining enterprise-grade resources and institutional maturity. The "for the first time" qualifier is significant — Chance is attributing this capability specifically to AI tooling adoption, not to other organizational changes. For the guide: this framing is useful for enterprise adoption chapters as a leadership narrative. It addresses the common objection "we're too large and regulated to move fast" by repositioning speed and agility as compatible with enterprise scale under AI tooling.

## Concrete Artifacts

### Key Metrics Summary

```
PayPal AI Tool Adoption Outcomes (Cursor blog, May 11, 2026)

ORGANIZATIONAL SCALE
  Engineering organization: 8,000 developers
  Customer responsibility: 400M+ customers globally

HEADLINE METRICS
  Roadmap throughput:    +40% projected for 2026
  Java upgrade (3,000 apps): 2 months actual vs. 8-12 months estimated (4-6x faster)
  Deployment cadence:    Daily (up from monthly release cycle)

HIGH-ADOPTION TEAM OUTCOMES (teams with 90%+ adoption)
  Deployment frequency:  Multiple times daily vs. once weekly (approx. 7x increase)
  Lead time:             Shortened (no specific measurement given)
  Change failure rate:   Decreased (no specific measurement given)

INDIVIDUAL VELOCITY CLAIM
  Sprint compression:    "Four sprints to one" — 4x throughput for high-impact work
  Adoption ramp:         Daily deployments within two weeks of tool adoption

ROLLOUT PATTERN
  Phase 1:  High-impact teams building critical products requiring rapid market entry
  Trigger:  Organic spread as engineers witnessed peer accomplishments
  Threshold: 90%+ adoption in high-impact teams
```

### Executive Quote Collection

```
Michelle Chance, Head of Developer Platforms — PayPal:

  On velocity: "Cursor has been critical in accelerating our timelines from doing
  something in four sprints to getting it done in one."

  On outcomes: "Teams with high adoption are deploying faster and shipping with
  shorter lead times."

  On role changes: "Roles that used to be very finite are blurring and we're
  seeing better product ideas come out of it."

  On metrics: "If you measure it, you impact it. If you tell a developer their
  success is based on what percentage of code was generated by AI, they'll just
  ask AI to write verbose functions."

  On the enterprise aspiration: "For the first time we're able to see a real
  path to being as scrappy as a startup, but with all the funding and maturity
  of a large enterprise."

Prakhar Mehrotra, SVP and Global Head of AI — PayPal:

  On AI as technology: "AI is about intelligence, not information. It's a
  fundamentally different technology stack."

  On developer agency: "Engineers still have to decide what problem to solve.
  But you're getting there much faster."

  On talent: "The most important thing is our developers are participating in
  the AI journey. They want to come work for us because PayPal supports tools
  like Cursor."
```

### SDLC Transformation Pattern

```
PayPal SDLC Before/After (described in Cursor blog, May 2026)

BEFORE (traditional linear SDLC):
  Design → Code → Build → Deploy
  Release cadence: Monthly
  Prototype delivery: Multiple sprints

AFTER (AI-accelerated iterative):
  Idea → Working prototype (hours) → Iterate
  Release cadence: Daily (high-adoption teams: multiple times daily)
  Sprint compression: 4 sprints → 1 sprint for critical product work

CROSS-FUNCTIONAL CHANGE:
  Before: PMs deliver documents; engineers implement
  After:  PMs bring functioning prototypes; engineers bring design variations
  Outcome: "Better product ideas come out of it" (Chance)

METRICS DISCIPLINE:
  Track:   Deployment frequency, lead time, change failure rate (DORA core metrics)
  Avoid:   % of AI-generated code (gaming vector: verbose functions on demand)
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (Assembly mainframe migration — "Before Cursor, we couldn't even think about moving away from Assembly") and Claim 5 (BizCalc 3x migration compression): PayPal's 6x Java upgrade across 3,000 apps is the corpus's second named large-scale AI-assisted migration, now at a different scale (3,000 apps vs. single monolith, 4-6x vs. 3x). Together they establish that AI-accelerated large-scale migration is reproducible across different enterprises, tech stacks, and project shapes.
  - `blog-cursor-nab-legacy-migration.md` Claim 8 (Cursor "brings engineers, architects, product, and security into the same workflow"): PayPal's role-blurring claim (Claim 7 above) provides independent validation from a different practitioner at a different company. NAB's De Lorenzo describes cross-discipline workflow unification; PayPal's Chance describes PMs and engineers co-creating prototypes. Both converge on the same structural change.
  - `blog-cursor-amplitude-autonomous-pipeline.md` Claim 5 (3x increase in production commits): Amplitude's commit-volume metric and PayPal's deployment-frequency metric are measuring the same phenomenon from different angles. Convergence across two enterprise case studies strengthens confidence that AI tool adoption produces measurable delivery acceleration.
  - `blog-cursor-better-models-ambitious-work.md` Claim 6 ("A central question around AI adoption is whether it merely facilitates existing work, or also opens up new productive opportunities. Our study indicates that it does both, but that expansion may eventually be the bigger story."): PayPal's source title — "Beyond efficiency: PayPal expands what's possible to build" — is a practitioner confirmation of this hypothesis. The blog post explicitly frames the outcome as expansion of capability, not just efficiency. The study's behavioral data and PayPal's executive framing converge independently.

- **Extends**:
  - `blog-cursor-nab-legacy-migration.md` Claim 4 (NAB's intentional enablement strategy — sprint days on real production projects): PayPal's organic-spread approach (Claim 1 above) extends the adoption-strategy corpus by documenting a successful alternative. NAB: intentional training → rapid scale. PayPal: seed high-impact teams → organic viral spread. Both reached high adoption. For the guide: neither is universally superior; both are documented strategies with different org-culture assumptions.
  - `blog-cursor-better-models-ambitious-work.md` Claim 5 (Finance/fintech sector shows +45% AI adoption growth rate): PayPal provides named practitioner evidence for why — the arms-race dynamic described in that study is visible in PayPal's framing (competitive advantage, talent market). The behavioral study explains the macro pattern; PayPal explains the firm-level experience of the same dynamic.

- **Contradicts**: None filed. No existing corpus source makes claims that materially oppose the PayPal claims. The organic adoption strategy (PayPal) vs. intentional enablement (NAB) difference is context-conditioned, not contradictory — both succeeded in different organizational contexts.

- **Novel**:
  - **Metric discipline: explicit rejection of % AI-generated code with specific gaming mechanism** (Claim 8): No prior corpus source names % AI-generated code as a specific anti-metric with an explicit gaming explanation ("they'll just ask AI to write verbose functions"). This is the most actionable negative metric recommendation in the corpus.
  - **Talent retention as AI adoption business outcome** (Claim 10): No prior corpus source documents talent attraction and retention as a measurable consequence of AI tool adoption. PayPal is the first to frame developer experience (including AI tooling) as a recruiting and retention differentiator.
  - **"Startup scrappiness within enterprise scale" as desired outcome** (Claim 11): The "scrappy as a startup but with enterprise resources" framing is the clearest articulation in the corpus of what enterprise AI adoption is trying to achieve as a business goal. Prior sources focus on productivity, velocity, or capability — none frame it as achieving startup agility without startup constraints.
  - **Role-blurring as quality improvement** (Claim 7): Prior sources (NAB Claim 8) note that AI brings cross-functional roles into the same workflow. PayPal adds: "we're seeing better product ideas come out of it" — a quality claim, not just a process claim. The blurring of PM/engineer boundaries produces better outcomes, not just faster ones.
  - **8,000-developer enterprise organic adoption arc** (Claim 1): This is the largest-scale AI coding tool adoption trajectory in the corpus documented at 90%+ team adoption rates with named org size. No prior source documents adoption saturation dynamics at this scale.

## Guide Impact

- **Chapter on Enterprise AI Adoption (planned, or Ch05)**: Add PayPal's organic rollout strategy (Claim 1) alongside NAB's intentional enablement (NAB Claim 4) as two validated enterprise adoption archetypes. The guide should present both, noting that organic spread requires seeding high-visibility high-impact teams first, while intentional enablement requires sprint days on real production projects. Both succeeded; the choice depends on organizational culture. PayPal's 90% adoption threshold for "high-impact teams" is a concrete milestone to aim for.

- **Chapter on Measurement (planned, or Ch04)**: Add Claim 8 (metric discipline) as the primary corpus reference for AI adoption measurement. Three-part recommendation: (1) track DORA core metrics — deployment frequency, lead time, change failure rate; (2) explicitly do not track % AI-generated code; (3) cite Chance's explanation of the gaming mechanism as the reason. This is more specific and actionable than any prior source on this topic.

- **Chapter on SDLC Transformation (planned, or Ch02/Ch03)**: Add Claim 6 (linear → iterative prototyping) and Claim 7 (role-boundary blur) as enterprise-scale validation of patterns the guide may describe from smaller-scale or individual-practitioner sources. The fact that an 8,000-person fintech has documented this SDLC shift as an organizational outcome strengthens the guide's credibility when making SDLC transformation claims.

- **Chapter on Team Adoption / Leadership Framing**: Add Claims 9, 10, and 11 as a leadership-narrative toolkit. For tech leaders pitching AI adoption internally: (9) position AI as intelligence not information (paradigm shift, not efficiency tool); (10) frame developer experience as a talent market differentiator; (11) use "startup scrappiness at enterprise scale" as the aspirational outcome. These three quotes together give a complete executive communication framework.

- **Chapter on Legacy Modernization**: Add Claim 5 (3,000-app Java upgrade in 2 months) as the second large-scale migration data point (alongside NAB's Assembly migration). The corpus now has two named enterprises with measurable large-scale migration outcomes. The guide can frame AI-assisted large-scale migration as empirically validated at Fortune-100 scale.

## Extraction Notes

1. **Source is vendor marketing**: Published on Cursor's commercial blog. All claims are filtered through Cursor's commercial interest in showcasing strong customer outcomes. Named executives and specific metrics provide credibility above typical vendor copy, but no independent validation exists. Treat all quantitative claims as emerging confidence.

2. **Quotes extracted via WebFetch tool**: All direct quotes in this note were extracted via the WebFetch tool which converts HTML to markdown. The Assayer should verify each attributed quote against the source URL (https://cursor.com/blog/paypal) before treating them as confirmed verbatim. The quotes are consistent across multiple WebFetch requests (same quotes appear in both fetches), which increases confidence, but character-level accuracy has not been independently verified.

3. **Deployment cadence claim requires careful reading**: The source describes both a per-team outcome (some teams: weekly/biweekly → daily within 2 weeks) and an organizational-level outcome (monthly → daily). These may be different claims about different team populations within the same 8,000-person org. The Assayer should verify whether "daily" applies to all teams or only the highest-adoption cohort.

4. **Java upgrade mechanism not described**: The 3,000-app Java upgrade claim (6x speedup) does not describe how AI was applied. It could involve automated code transformation agents, AI-assisted manual development, or a hybrid. The mechanism matters for reproducibility — the guide should present this as an outcome without prescribing the exact technical approach.

5. **No sub-pages followed**: The Cursor blog post is self-contained. No linked sub-pages were identified.

6. **No contradictions filed**: No existing corpus source makes claims that materially oppose the PayPal claims. The organic (PayPal) vs. intentional (NAB) adoption strategy difference is context-conditioned, not contradictory.
