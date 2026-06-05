---
source_url: https://simonwillison.net/2026/May/26/the-pressure/
source_type: blog-post
title: "The Pressure"
author: Simon Willison (link-blog curation); primary content by Daniel Stenberg (curl maintainer, daniel.haxx.se)
date_published: 2026-05-26
date_extracted: 2026-06-05
last_checked: 2026-06-05
status: current
confidence_overall: anecdotal
issue: "#1064"
---

# The Pressure

> Daniel Stenberg's first-person account (curated by Simon Willison) of how AI-assisted
> security research has flooded the curl project with a 4-5x surge in high-quality security
> reports, creating an unsustainable triage burden on volunteer maintainers who lack the
> infrastructure to process AI-amplified workloads at scale.

## Source Context

- **Type**: blog-post (Simon Willison link-blog curation, May 26, 2026). Willison's post
  is a short entry (~100 words) pointing to Daniel Stenberg's article "The Pressure"
  published the same day at daniel.haxx.se/blog/2026/05/26/the-pressure/. Stenberg's
  article (~2,100–2,300 words) is the substantive source; all quoted passages below are
  from Stenberg's original article. The Willison post frames it as "the unprecedented
  level of pressure the curl team are facing right now thanks to the deluge of (credible)
  AI-assisted security issues being reported."
- **Author credibility**: Daniel Stenberg is the creator and lead maintainer of curl —
  arguably the most widely deployed piece of C software in existence (~30 billion
  installations). He has led the project for nearly 30 years. This is first-person,
  operational testimony from the definitive authority on the curl project's security
  response processes. Simon Willison is the creator of Django and a trusted-feed source
  for LLM tooling commentary in this repo. Willison acts as curator here, not originator.
  Stenberg's observations are direct operational evidence, not theory or projection.
- **Scope**: Covers the period through mid-2026, documenting the evolution of AI-assisted
  security research as experienced on the receiving end by an open-source maintainer.
  Covers: volume and quality trends for AI-generated security reports, the work each
  report requires from the team, personal and family impact, funding gaps, and the
  resilience of curl's actual security posture despite the workload. Does NOT cover:
  which AI tools researchers are using, how to build AI triage infrastructure (see
  `blog-cursor-security-agents.md` for that), or how to stop receiving AI-generated
  reports. Does not represent the experience of corporate engineering teams, which
  typically have more resources to absorb volume surges.

## Extracted Claims

### Claim 1: AI-assisted security research has caused a 4-5x surge in security reports for curl relative to 2024 levels

- **Evidence**: Direct observation by Stenberg from the curl project's security inbox.
  Concrete comparative metrics across 2024, 2025, and mid-2026.
- **Confidence**: anecdotal (self-reported by the maintainer; the number is plausible
  and consistent with broader AI capability trends, but no independent audit of the
  curl security inbox is provided)
- **Quote**: "The rate of incoming security reports is 4-5 times higher than it was in
  2024 and double the speed of 2025 – meaning that on average we now get more than one
  report per day."
- **Our assessment**: This is the central quantitative anchor for the entire article.
  The cross-year comparison makes the trajectory clear: the surge is not a 2025 blip
  but an accelerating trend, with 2026 already doubling 2025's pace. For AI-native
  engineering teams: this is real-world evidence of the "order-of-magnitude increase in
  finding volume" that `blog-anthropic-ai-accelerated-offense.md` (Claim 5) predicted as
  a planning assumption. Curl is living that prediction. The >1/day rate also implies that
  each new report arrives before the previous one is resolved, creating a permanently
  accumulating queue.

### Claim 2: AI-generated security report quality has dramatically improved over time — from "stupid AI slop" to detailed, high-quality submissions

- **Evidence**: Stenberg's longitudinal observation across multiple years of curl security
  report history. He documents an explicit evolution in report quality over time.
- **Confidence**: anecdotal (maintainer's qualitative assessment over time; consistent
  with broader improvements in LLM capability documented in corpus sources)
- **Quote**: "Over the last years I have done numerous blog posts on the state of security
  reports submitted to curl. They have gradually switched over from complaints on stupid
  LLMs, to stupid AI slop reports, closing the bug bounty over to the current high quality
  chaos"
- **Our assessment**: This is one of the most consequential claims for the guide: the
  quality trajectory matters as much as the volume trajectory. Early AI security reports
  were dismissible ("stupid LLM complaints"). Current AI-assisted reports are detailed
  and credible. The transition from ignorable noise to credible-but-overwhelming is what
  created the sustainability crisis — a maintainer can ignore slop, but cannot ignore
  high-quality credible vulnerability reports. The word "chaos" is Stenberg's own
  characterization: quality without proportionate triage capacity is chaos, not improvement.

### Claim 3: Each credible security report requires substantial, non-automatable human work to process

- **Evidence**: Stenberg's direct description of the per-report work sequence the curl
  security team follows.
- **Confidence**: anecdotal (first-person operational account of an established security
  response process)
- **Quote**: "Verify the claim, assess the importance, write a patch, figure out when
  the bug was introduced, understand the vulnerability, write a detailed advisory explaining
  the problem to the world and communicate all this with the security researcher"
- **Our assessment**: This itemized workflow clarifies why volume increase translates
  directly to human hours: each step requires expert judgment, not just pattern matching.
  Automated triage tools (e.g., the Anthropic-recommended AI at the front of the alert
  queue — `blog-anthropic-ai-accelerated-offense.md` Claim 7) could potentially handle
  the first step (verify the claim), but writing the patch, figuring out when the bug was
  introduced, and drafting the CVE advisory all require deep project expertise that cannot
  be easily automated for a project with curl's complexity and 30-year history. This
  explains why simply deploying an AI triage agent would not fully resolve the crisis
  for curl-scale projects.

### Claim 4: The volume surge has produced a never-before-experienced workload for a nearly 30-year-old project

- **Evidence**: Stenberg's own reflection on the project's history and current situation.
  At mid-2026, curl had already confirmed 12 vulnerabilities (a new project record for
  the period), with projections of 30+ CVEs by mid-year and potentially 60+ for 2026 total.
- **Confidence**: anecdotal (Stenberg's first-person account; the record-breaking nature
  is consistent with the quantitative data in Claim 1)
- **Quote**: "A thirty years old project could make you think you've seen most things
  already, but we have not been in this situation before."
- **Our assessment**: The historical framing is important: this is not a young project
  with an inexperienced team encountering its first surge. Stenberg has been running curl
  security response for decades. If a 30-year veteran calls something unprecedented, the
  claim deserves weight. The implication for the guide: even mature, experienced open-source
  projects with strong security track records are unprepared for AI-amplified report volumes.

### Claim 5: The triage burden is creating personal and family-level work-life balance crises for the lead maintainer

- **Evidence**: Stenberg's direct personal disclosure, including a notable first-time
  mention of his wife raising concerns.
- **Confidence**: anecdotal (personal account by the primary maintainer; documented
  publicly on his own blog)
- **Quote 1**: "I typically mean doing 50 hour work weeks, as I spend all days on it
  and then I top them off with a few more hours every late night"
- **Quote 2**: "For the first time in my life, my wife voiced concerns about my work
  hours and my imbalanced work/life situation."
- **Our assessment**: These are the most viscerally direct passages in the article.
  Stenberg's mention of his wife raising concerns — specifically noting it is a
  "first time in my life" event — signals that the situation has crossed a personal
  threshold that decades of intense open-source work did not previously cross. The
  50-hour baseline is itself high; the article implies additional hours on top during
  security response surges. For the guide: this is concrete evidence that AI-amplified
  workloads can create unsustainable conditions for human operators, even ones who have
  maintained exceptional output for 30 years. The human sustainability cost is real
  and documented.

### Claim 6: The maintainer is concerned about team members burning out, not just himself

- **Evidence**: Stenberg's direct expression of concern for teammates in the context
  of community members also expressing worry about the team.
- **Confidence**: anecdotal (first-person account)
- **Quote**: "People in my surrounding, I guess reading between the lines, have asked
  me how I and we cope with this deluge and want to make sure we don't burn in the
  process. I am concerned for my team mates."
- **Our assessment**: The plural scope ("my team mates") is significant: this is not
  a one-person burnout risk but a team-level sustainability threat. The community's
  awareness ("reading between the lines") signals that the strain is visible externally.
  For the guide: when AI tooling amplifies workload at the system level (not just for one
  person), the team-level resilience question becomes critical. The curl team is a canary
  for open-source security teams broadly.

### Claim 7: Despite report volume surge, curl's actual security posture remains strong — all recent vulnerabilities are LOW or MEDIUM severity

- **Evidence**: Stenberg's direct statement about CVE severity history, with a specific
  date anchor for the last HIGH severity issue.
- **Confidence**: anecdotal (self-reported; severity ratings are assigned by security
  researchers and the curl team collaboratively, with CVE severity scores externally
  verifiable)
- **Quote 1**: "all vulnerabilities found the last few years in curl have all been deemed
  severity LOW or MEDIUM"
- **Quote 2**: "The most recent severity high curl CVE was published in October 2023."
- **Our assessment**: This is the "good news" claim that provides crucial context. The
  crisis is a workload crisis, not a code quality crisis. Curl's underlying security
  posture — the result of "relentless work and attention to details through decades" —
  is strong. The AI-assisted researchers are finding bugs, but the bugs being found are
  at the margins. This has two implications: (1) AI-assisted security tooling is effective
  enough to find real vulnerabilities even in mature, hardened code; (2) the volume of
  marginal-severity findings may exceed the value they provide relative to the cost they
  impose on the maintenance team. This is the "volume without commensurate severity"
  paradox — a new class of problem for open-source security governance.

### Claim 8: Open-source projects handling AI-amplified security report volumes receive no corresponding increase in funding or infrastructure support

- **Evidence**: Stenberg's explicit description of curl's organizational structure: no
  corporate backing, no umbrella organization, existing contracts funding a limited number
  of team members.
- **Confidence**: anecdotal (Stenberg's direct account of curl's funding situation)
- **Quote**: "I wish more companies that use and depend upon curl or libcurl in commercial
  software and services would chime in their part to fund us...Get your employer to pay
  for a support contract!"
- **Our assessment**: This is the structural claim that makes the situation a systemic
  problem, not just a personal one. The companies using AI security research tools to
  find vulnerabilities in open-source code (and generating the report volume Stenberg
  describes) are not the same as the companies funding curl's security response capacity.
  The funding gap is not new, but AI-assisted tooling has dramatically widened the
  mismatch between report volume and response capacity. For the guide: teams that use
  AI security research tools to scan open-source dependencies should consider whether
  they are contributing to the maintainer burden — and whether their contracts or
  contributions to the projects they depend on reflect that cost.

### Claim 9: The team's operational resilience rests on self-reliance rather than external support, which is itself a risk factor

- **Evidence**: Stenberg's closing framing of how the curl team plans to respond to
  the situation.
- **Confidence**: anecdotal (first-person statement about the team's approach)
- **Quote**: "I totally expect us to ride out this storm by ourselves. Like we are used
  to. We will survive. We will endure."
- **Our assessment**: The stoic framing is revealing: Stenberg does not expect
  meaningful external support to materialize. The team's resilience strategy is
  self-reliance, not systemic change. For the guide: self-reliance as a resilience
  strategy is brittle at AI-amplified workload levels. When a 30-year maintainer with a
  strong team and decades of hardening calls a situation a "storm" they must "endure,"
  the implied risk is maintainer attrition if the intensity is sustained. The guide should
  address this as a real team adoption risk: AI tooling that amplifies security research
  without proportionate triage infrastructure can burn out the human reviewers the whole
  system depends on.

## Concrete Artifacts

### Security Report Volume Trend (curl project, mid-2026)

```
Data from: Daniel Stenberg's "The Pressure" (daniel.haxx.se, May 26, 2026)

Security report rate comparison:
  2024 baseline:    1x (reference)
  2025 rate:        2x baseline (roughly)
  2026 mid-year:    4-5x 2024 baseline; 2x 2025 pace
  Average rate:     >1 security report per day (2026)

Vulnerability severity (recent years):
  Severity level:   ALL LOW or MEDIUM
  Last HIGH CVE:    October 2023
  Pending CVEs at time of writing: 12 (new record for project)

Stenberg's workload estimate:
  Typical work week:  50+ hours
  Nature of work:     majority on security response during surge periods
```

### Per-Report Security Response Workflow (curl team)

```
From: Daniel Stenberg's "The Pressure" (daniel.haxx.se, May 26, 2026)
Sequence for each credible security report:

1. Verify the claim
2. Assess the importance / severity
3. Write a patch
4. Figure out when the bug was introduced (git archaeology)
5. Understand the vulnerability fully
6. Write a detailed advisory explaining the problem to the world
7. Communicate all this with the security researcher

Typical output: a CVE advisory with patch, severity rating, timeline
Human expertise required at every step for a 30-year, ~30B-installation project
```

### Evolution of AI Security Report Quality (Stenberg's observation)

```
From: Daniel Stenberg's "The Pressure" (daniel.haxx.se, May 26, 2026)

Phase 1 (early LLM era):
  — "complaints on stupid LLMs"
  — Reports based on hallucinated or misunderstood vulnerabilities
  — Dismissible as noise

Phase 2 (LLM slop era):
  — "stupid AI slop reports"
  — Low-quality AI-generated submissions
  — curl closed bug bounty to reduce slop volume

Phase 3 (current, mid-2026):
  — "current high quality chaos"
  — "The quality is way higher than ever before."
  — "The reports are typically very detailed and long."
  — High enough quality to require full security response per report
  — Volume: >1/day, 4-5x 2024 rate
```

## Cross-References

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 5 — Anthropic
  forecast "plan for an order-of-magnitude increase in finding volume." The Stenberg
  article is a live empirical data point: curl is experiencing a 4-5x surge, which is
  within the lower range of "order of magnitude" as a real, observed outcome, not a
  projection. The forecast and the observation align. Claim 7 in that note recommends
  placing a model at the front of the alert queue — curl's situation illustrates exactly
  why: without automated triage, the human queue becomes unsustainable.

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 1 — the
  token-budget framing. The Stenberg article documents the maintainer-side consequence of
  that arms race: when AI-assisted researchers (spending tokens) flood an open-source
  project with high-quality reports, the defenders (maintainers) face a triage burden that
  does not scale at the same rate as token spending. The proof-of-work framing assumes
  defenders will also invest in AI triage; curl demonstrates what happens when they cannot.

- **Extends**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 6 — that note
  argues "open-source libraries become more valuable" under the token-economy model because
  shared hardening costs amortize across users. The Stenberg article adds a critical missing
  term: more security value flowing to users of well-maintained OSS does not automatically
  translate to more resources for the maintainers handling the resulting triage burden.
  The amortization argument (Breunig/Willison) is about cost-sharing for defenders who run
  hardening scans; it does not address the cost imposed on maintainers by the corresponding
  increase in inbound researcher findings. The full picture requires both notes.

- **Extends**: `blog-cursor-security-agents.md` — Cursor's four-agent security fleet
  (3,000+ PRs/week, AI-assisted triage, shared MCP infrastructure) represents the
  corporate-scale infrastructure response to the same AI-amplified finding volume problem.
  Cursor solves the problem for a well-resourced team by deploying AI triage. The Stenberg
  article shows what the problem looks like for a volunteer-led open-source project that
  cannot deploy equivalent infrastructure. Together the two notes bracket the problem space:
  corporate teams can build the Cursor pattern; open-source maintainers typically cannot,
  and the gap creates a systemic sustainability risk.

- **Novel**:
  - The **maintainer-side view of AI-amplified security research volume** is the first
    primary-source account in the corpus from the *receiving end* of AI-assisted security
    research. All prior corpus sources (Cursor, Anthropic, AISI) document this from the
    generator/defender perspective. Stenberg documents the third position: the open-source
    maintainer who receives the output of AI-assisted security tools without the resources
    to process it.
  - The **quality evolution timeline** (stupid LLM → slop → high-quality chaos) is a
    novel longitudinal observation about how AI security report quality has changed over
    time. No other corpus source documents this trajectory.
  - The **"volume without commensurate severity" paradox** — 4-5x more reports, but
    all LOW/MEDIUM severity — is a new pattern to the corpus. The flood is real; the
    urgency per report is not proportionately elevated. This is a novel finding about
    the *composition* of AI-assisted security research output: volume scales faster than
    critical-severity discovery.
  - The **funding gap as a structural amplifier** is novel: companies benefiting from
    AI-assisted discovery of open-source vulnerabilities are not correspondingly funding
    the maintainers who must process those reports. This is a systemic externality not
    addressed in any other corpus source.
  - The **human sustainability cost at family level** (spouse raising concerns for the
    first time in 30 years of open-source work) is the first corpus source to document
    AI-amplified workload reaching personally-disclosed family impact. This is a concrete
    marker of sustainability threshold being crossed.

## Guide Impact

- **Ch05 (Team Adoption)**: Add a section on second-order workload effects: AI tooling
  that amplifies output in one context (security research velocity) generates corresponding
  workload in another (open-source maintainer triage). Teams that deploy AI-assisted
  security scanning against open-source dependencies should account for the maintainer
  cost of the reports they generate. The guide should recommend responsible disclosure
  practices (already in `blog-anthropic-ai-accelerated-offense.md` Concrete Artifacts)
  AND contributing funding to the open-source projects being scanned. This is an adoption
  ethics consideration, not just a technical one.

- **Ch03 (Safety and Verification) or dedicated Security chapter**: Add the curl case
  as a concrete example of the predicted AI-amplified finding volume surge. Currently
  `blog-anthropic-ai-accelerated-offense.md` Claim 5 is a forward-looking projection;
  the Stenberg article is a backward-looking empirical data point confirming it. The guide
  should cite both: prediction (Anthropic) and observation (Stenberg/curl). The claim to
  add: "The projected order-of-magnitude finding volume increase is already observable.
  The curl project is experiencing 4-5x more security reports in 2026 than 2024, driven
  by AI-assisted research tools. All are credible; most are LOW or MEDIUM severity."

- **Ch01 (Daily Workflows)**: The AI-amplified workload pattern documented here applies
  to any team running AI-assisted security scanning. Teams should build AI triage
  infrastructure before enabling high-volume AI security research — the alternative is
  the Stenberg scenario: a permanent queue of credible, detailed reports that exceeds
  human capacity to process. The guide should specify that deploying AI security research
  without AI triage is an incomplete workflow.

- **Ch05 (Team Adoption) — open-source sustainability**: Add explicit guidance for
  organizations using open-source libraries at scale: if your security tooling generates
  reports against those libraries, budget for supporting the maintainers who handle the
  responses. This is a novel adoption responsibility created by AI-amplified security
  research that did not previously exist at current report volumes.

## Extraction Notes

1. **Simon Willison's post is a link-blog entry**. The substantive content is from
   Daniel Stenberg's article at daniel.haxx.se/blog/2026/05/26/the-pressure/. All
   quoted passages are from Stenberg's original; Willison's post contributes the
   curation signal (trusted-feed tagging, his characterization of the situation) and
   serves as the issue entry point. Both URLs were fetched; Stenberg's article is the
   primary extraction source.

2. **Projection statistics are from the WebFetch summary, not direct quotes**: The
   figures of 12 confirmed pending vulnerabilities (new record) and 60+ projected full-year
   CVEs for 2026 come from the WebFetch content summary of Stenberg's article. They are
   reported as approximate values in the Concrete Artifacts section without being placed
   in Quote fields, since verbatim source text for these specific numbers was not confirmed.

3. **Source quality is high for a personal account**: Stenberg is an unusually credible
   first-person source. He has led curl's security response for nearly three decades,
   and his observations about report volume and quality are based on direct operational
   experience, not survey data or extrapolation. The confidence rating of `anecdotal`
   reflects the source type (first-person account, not peer-reviewed study), not the
   author's credibility.

4. **No sub-pages followed beyond the primary article**: The Willison post links to
   Stenberg's article and attributes discovery to Lobste.rs. The Lobste.rs discussion
   thread was not followed (likely discussion commentary, not primary evidence). Stenberg's
   article itself does not contain substantive linked sub-pages that were followed.

5. **No contradictions filed**: The claims in this source are corroborative or
   additive relative to existing corpus notes. The closest tension is with the
   "open-source amortization" argument in `blog-simonwillison-cybersecurity-proof-of-work.md`
   (Claim 6), but the two claims address different aspects of the same system (who captures
   the security value vs. who bears the triage cost) rather than opposing positions on
   the same question.
