---
source_url: https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez
source_type: blog-post
title: "CI/CD with Robert Erez"
author: Gergely Orosz (host); Robert Erez (guest, principal engineer at Octopus Deploy)
date_published: 2026-06-17
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: anecdotal
issue: "#1454"
---

# CI/CD with Robert Erez

> A podcast companion post in which Robert Erez (principal engineer at Octopus Deploy) lays out
> ten practitioner positions on modern software delivery — roll-forward over rollback, GitOps
> without the Git dogma, delivery over deployment, feature toggles as an incident safety net,
> Git-repo scalability limits for pull-based GitOps at Kubernetes scale, and a closing claim that
> AI code generation shifts CI/CD's central optimization target from build speed to shipped-bug risk.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack; published June 17, 2026. The
  post is a written companion summary to a podcast episode — Gergely Orosz interviewing Robert
  Erez — available on YouTube, Spotify, and Apple Podcasts, run time ~1 hour 14 minutes. Format:
  ten numbered "key observations," each with a heading (Orosz's summary language) and a body
  paragraph beneath it. No paywall notice was found on the page; the ten observations and their
  body paragraphs appear to be fully accessible without a subscription.)
- **Author credibility**: Robert Erez is described in the post as "a principal engineer at
  Octopus Deploy, and a longtime expert in CI/CD, deployment systems, and software delivery."
  Octopus Deploy is a widely used enterprise CD/release-management platform, giving Erez direct
  operational exposure to how a large number of customer organizations actually run deployment
  pipelines — this is deployment-platform-vendor practitioner expertise, not academic or
  first-party AI-lab research. Gergely Orosz is the author of The Pragmatic Engineer, a
  high-signal engineering newsletter already represented multiple times in this corpus (e.g.
  `blog-pragmaticengineer-hightower-infrastructure-ai.md`).
- **Scope**: Covers rollback vs. roll-forward strategy, GitOps's four pillars vs. its Git-centric
  reputation, continuous delivery vs. continuous deployment, feature-toggle incident response and
  hygiene, Git-repo scalability under pull-based GitOps at large Kubernetes fleet scale, on-prem
  persistence in regulated industries, platform-team value at scale, ephemeral per-branch
  environments, and — in the single AI-specific observation (#10) — a claim about how AI code
  generation changes CI/CD's optimization priorities. Does NOT cover: specific AI coding tools,
  named case studies of AI-in-CI/CD deployments, concrete metrics on AI-generated-code bug rates,
  or any implementation detail for the "extra, more thorough tests" the AI observation calls for.
  The AI content is one of ten observations and is asserted as a prediction, not backed by data
  from Erez's own customer base.

## Extracted Claims

### Claim 1: Systems with database state should be fixed by rolling forward to a new version, not rolled back to a prior one, because rollback can desync code from schema
- **Evidence**: Erez's stated operational principle, attributed by Orosz as "Rob's advice."
- **Confidence**: anecdotal (single practitioner's operational heuristic, though grounded in a
  concrete, verifiable failure mode — schema/code desync — rather than pure opinion)
- **Quote**: "When a system has state – which typically means it uses databases – then doing a
  rollback can leave the code talking to a schema that's no longer in sync. Rob's advice is to
  not treat a failure in v2 as a trip back to v1, but rather as a push to v3 with the fix in it."
- **Our assessment**: This is a specific, checkable failure mode, not a vague preference for
  "forward fixes." A rollback that reverts code but not a since-migrated schema (or vice versa)
  produces a code/schema mismatch that a same-version rollback wouldn't have. The advice — treat
  a failed v2 as a reason to ship v3, not to revert to v1 — is directly relevant to any
  AI-agent-driven deploy pipeline that includes database migrations: an agent's "fix a bad
  deploy" playbook should default to forward-fix, not blind rollback, whenever migrations are
  involved.

### Claim 2: None of GitOps's four defining pillars actually require Git, yet the industry has become dogmatic about storing everything — including secrets — in a repo
- **Evidence**: Erez's definitional breakdown of GitOps into four pillars, contrasted with
  observed industry practice.
- **Confidence**: anecdotal (definitional/critical observation from a CD-platform practitioner;
  not a data-backed claim, but the four-pillar breakdown is a specific, checkable taxonomy)
- **Quote**: "None of the four pillars of GitOps – 1) declarative, 2) versioned and immutable, 3)
  pulled, not pushed, 4) continuously reconciled – require Git, although Git can work under these
  constraints. Yet, the term 'GitOps' has made the industry dogmatic about cramming everything
  into a repo – even things like secrets that absolutely shouldn't be there!"
- **Our assessment**: The naming-versus-substance distinction is useful: GitOps is a set of
  properties (declarative, versioned/immutable, pull-based, continuously reconciled), and Git is
  one possible substrate, not a requirement. The secrets-in-repo anti-pattern this dogma produces
  is a concrete operational risk worth naming directly in any guide section that discusses
  storing agent-managed configuration or credentials — an AI agent following "put config in Git
  because that's GitOps" literally, without understanding the four pillars, could be steered
  toward committing secrets to a repo.

### Claim 3: Continuous deployment (auto-shipping every change) is often unnecessary overkill; continuous delivery (validated, gated shipping) is more practical for most teams
- **Evidence**: Erez's stated preference, framed as a corrective to a common assumption that
  full continuous deployment is the goal to aim for.
- **Confidence**: anecdotal (practitioner opinion; consistent with long-standing CD literature
  distinguishing delivery from deployment, not a novel empirical finding)
- **Quote**: "Shipping every single change to prod (continuous deployment) is not as necessary as
  many people think, Rob says, and there's often more value in continuous delivery, where changes
  flow through testing and the deployment process itself is validated. With continuous delivery,
  you can decide whether to push to production automatically, or click a button once a week."
- **Our assessment**: This distinction matters directly for AI-agent-authored changes: an
  AI-native pipeline does not need full continuous deployment (auto-ship every agent commit) to
  get the throughput benefit of agents — continuous delivery (every change validated and
  deploy-ready, with a human or policy gate on the final push) preserves a control point without
  giving up pipeline validation. This is a useful vocabulary distinction for any guide section
  that currently conflates "agents can ship fast" with "agents should auto-deploy every change."

### Claim 4: Feature toggles are a faster, calmer incident-response mechanism than rolling back a deployment
- **Evidence**: Erez's operational comparison of toggle-based mitigation vs. deployment rollback
  during a production incident.
- **Confidence**: anecdotal (practitioner operational preference, widely echoed in the feature-flag
  literature but presented here without incident data)
- **Quote**: "When something breaks in production, reaching for a toggle to switch a feature off
  enables you to 'stop the bleeding' and then calmly diagnose an issue. Rolling back a feature
  flag is less nerve-jangling than scrambling to force a redeployment in the middle of the night!"
- **Our assessment**: This complements Claim 1 rather than conflicting with it — the "roll
  forward, not back" advice is about deployment/schema state, while this claim is specifically
  about *toggling a feature flag off*, which is a config change, not a code/deployment rollback.
  Read together, Erez's position is: don't roll back deployments (risk of schema desync); do roll
  back feature flags (cheap, fast, no schema risk). For AI-native pipelines, this argues for
  agents having toggle-off authority (a narrow, low-risk action) separate from and prior to any
  redeploy/rollback authority (a broader, higher-risk action).

### Claim 5: The ease of adding feature flags creates a hygiene problem — flags accumulate faster than they get removed, and cleanup must be treated as ongoing maintenance
- **Evidence**: Erez's stated maintenance concern, with a specific remediation framing ("weed" as
  gardening metaphor).
- **Confidence**: anecdotal (widely observed pattern in the industry; presented as an assertion,
  not backed by a specific count or case study in this source)
- **Quote**: "On the other hand, the ease with which feature flags are added can create a hygiene
  crisis if they're continuously added, but not removed. Treat feature-toggle cleanups like a form
  of gardening and 'weed' rolled-out toggles from the codebase."
- **Our assessment**: This is a direct counterpoint to Claim 4 within the same source: toggles are
  the recommended safety net, but they are also a known maintenance liability if not actively
  pruned. For an AI-native pipeline where agents can create feature flags cheaply (and may create
  more of them than a human team would, given lower friction to adding one), this argues for
  pairing agent flag-creation with an equally automatable flag-removal/audit process — an
  "agent that adds toggles" needs a corresponding "agent (or scheduled job) that weeds them."

### Claim 6: Pull-based GitOps does not scale infinitely for free — companies running thousands of independent Kubernetes clusters pulling from a single Git repo can get throttled by the repo itself
- **Evidence**: Erez's observation about large-scale GitOps deployments, describing the repo as
  a bottleneck rather than the orchestration layer.
- **Confidence**: anecdotal (practitioner observation from CD-platform vantage point; no specific
  company named, no throughput numbers given)
- **Quote**: "Rob mentions that some companies run thousands of independent Kubernetes clusters
  that pull state from a Git repository. But such clusters can get throttled by the repo, forcing
  them into workarounds. Pull-based GitOps doesn't scale infinitely for free."
- **Our assessment**: This is a specific, checkable scaling limit rather than a general caution
  about GitOps. It's relevant to any AI-native org running many agent-driven deployment targets
  (e.g., per-feature ephemeral clusters, per-tenant clusters) that all pull from the same
  Git-backed config source — the repo itself, not the reconciliation logic, becomes the
  bottleneck at fleet scale. No specifics are given on what the "workarounds" are, which limits
  how directly actionable this claim is on its own.

### Claim 7: Banks, other financial institutions, and governments will keep significant on-prem infrastructure and will not move fully to cloud SaaS, driven by hardware/downtime control requirements
- **Evidence**: Erez's stated expectation about a market segment's infrastructure trajectory.
- **Confidence**: anecdotal (practitioner prediction about a market segment, not backed by
  adoption data in this source)
- **Quote**: "Banks, other financial bodies, and governments, demand full control over their
  hardware, upgrades, and downtime. That's why Rob expects this segment won't move to cloud-based
  SaaS."
- **Our assessment**: This is a scoping claim relevant to any guide discussion of AI-agent-driven
  deployment automation that assumes cloud-hosted infrastructure and SaaS control planes — a
  meaningful fraction of regulated-industry deployments will remain on-prem, meaning AI-native
  CI/CD patterns built around cloud APIs (cloud agent runners, hosted GitOps controllers) need an
  on-prem-compatible equivalent for these segments, not just a cloud-first assumption.

### Claim 8: Platform engineering teams justify their organizational cost primarily at larger companies with multiple teams and projects, not at smaller scale
- **Evidence**: Erez's stated view on when a dedicated platform team pays for itself.
- **Confidence**: anecdotal (practitioner opinion; no headcount or company-size threshold given)
- **Quote**: "These teams earn their keep in big organizations with multiple teams and projects
  because they offer ways of bringing sanity and focus."
- **Our assessment**: Directionally consistent with general platform-engineering literature (a
  platform team amortizes its cost over many consuming teams), but Erez gives no concrete
  threshold (team count, org size) at which this becomes true, so it's a scoping heuristic rather
  than an actionable rule. Relevant to any guide discussion of when to stand up a dedicated
  AI-harness or agent-platform team vs. leaving harness maintenance to individual teams.

### Claim 9: Ephemeral, per-feature-branch, pre-merge environments are replacing static shared test/staging environments as the default verification pattern
- **Evidence**: Erez's observation contrasting older static test-environment contention with
  current per-branch ephemeral environment practice.
- **Confidence**: anecdotal (practitioner observation of an industry trend; no adoption
  percentage or company examples given in this source)
- **Quote**: "Companies used to have a few testers fighting over a handful of static test
  environments, but today, it's trivial to spin up a full environment, per-feature branch,
  pre-merge. This is an 'ephemeral' environment for evaluating that things work, which is then
  torn down once something is merged. It helps speed up the feedback process."
- **Our assessment**: This is directly relevant to AI-agent-driven development: if agents are
  producing many more concurrent branches/PRs than a human-only team would (as documented
  elsewhere in the corpus, e.g. Amplitude's 1,000+ automated agent runs/week in
  `blog-cursor-amplitude-autonomous-pipeline.md` Claim 8), then static shared test environments
  become a contention bottleneck faster, making per-branch ephemeral environments less a nice-to-have
  and more a structural requirement for high-volume agent output. This source doesn't discuss AI
  agents in connection with this trend, but the scaling logic (more concurrent changes needing
  independent verification) applies directly.

### Claim 10: AI agents writing most code will shift CI/CD's central optimization target from build/pipeline speed to reducing the risk of shipping an agent-introduced bug, favoring more and slower tests
- **Evidence**: Erez's forward-looking claim about how AI code generation changes the cost-benefit
  calculus of CI pipeline design, contrasting current motivations (avoid blocking a human dev) with
  a projected future motivation (avoid an agent shipping a bug).
- **Confidence**: emerging (this is the source's single most guide-relevant claim, framed as
  Erez's own prediction rather than an observed data point — no metrics, no named team already
  running this way, but it's a specific and directly testable prediction about pipeline design
  priorities, not vague futurism)
- **Quote**: "Today, shaving ten minutes off the CI build-time matters because a long-running
  build blocks human devs. But this time saving will be insignificant when an AI agent writes
  most of the code and 'babysits' a slow pipeline without context switching. Then, the new
  priority will be to reduce the risk of an AI agent shipping a bug to production, so it will
  make much more sense to run extra, more thorough tests – and also even slower ones."
- **Our assessment**: This is the highest-value claim in the source for the guide. The mechanism
  is specific: today's CI speed pressure exists because a slow build blocks a *human*, who
  context-switches while waiting; an agent doesn't context-switch the same way, so the human cost
  of a slow pipeline drops, freeing budget to spend on more (and slower) verification instead.
  This reframes "make CI faster" as a human-ergonomics optimization that becomes less load-bearing
  as agents do more of the waiting, while "make CI more thorough" becomes the optimization that
  matters more as agents do more of the code-writing. This directly corroborates the corpus's
  existing testing-rigor arguments (see Cross-References) but adds a distinct causal argument —
  the shift isn't just "AI writes more code so we need more tests," it's "AI agents remove the
  human-blocking cost of slow pipelines, which removes the reason CI needed to be fast in the
  first place." No data or named team backs this; it is Erez's stated prediction.

## Concrete Artifacts

### The 10 Observations (verbatim headings, from the article)
```
Episode: "CI/CD with Robert Erez"
The Pragmatic Engineer (Gergely Orosz, host), June 17, 2026
Guest: Robert Erez, principal engineer at Octopus Deploy

1.  Roll forward, never backwards
2.  GitOps isn't actually about Git
3.  Continuous deployment can be overkill; continuous delivery is more practical
4.  Feature toggles are a better safety net than rollbacks
5.  One problem with feature flags is that they're addictive
6.  A Git repo can be a bottleneck at scale
7.  A sizable number of major institutions remain on-prem – and this won't change
8.  Platform teams work at larger companies
9.  There's a trend of ephemeral environments replacing test/staging environments
10. AI shifts the CI/CD calculus from speed to risk
```

### Guest bio (verbatim, from the article)
```
"Robert Erez is a principal engineer at Octopus Deploy, and a longtime expert
in CI/CD, deployment systems, and software delivery."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claudecode-quality-postmortem.md` (Claims 7–9): that source documents a
    real incident where a bug passed "multiple human and automated code reviews, as well as unit
    tests, end-to-end tests, automated verification, and dogfooding" — a concrete case for why
    more/slower verification layers matter for AI-affected changes. Erez's Claim 10 here (run
    "extra, more thorough tests – and also even slower ones" as AI writes more code) gives the
    forward-looking design principle that the postmortem's incident illustrates the cost of
    skipping. The postmortem is evidence of what happens without enough rigor; Erez's claim is
    the prescriptive response.
  - `blog-cursor-app-stability.md` (Concrete Artifacts → item 5, "Metric-Based Rollbacks":
    "Automated rollbacks triggered by metric regressions... if a ship increases OOM rate, revert
    automatically"): this reads as consistent with, not contradicting, Erez's Claim 1 and Claim 4
    here — Cursor's described mechanism reverts a *ship* (a change/config) automatically on a
    metric regression, which is closer to Erez's endorsed "toggle off, stop the bleeding" pattern
    (Claim 4) than to the deployment/schema rollback Erez warns against (Claim 1). Both sources
    converge on: automated/fast reversion of a discrete change is good; reverting a full
    deployment with migrated schema state is risky.
  - `blog-cursor-amplitude-autonomous-pipeline.md` (Claim 8: 1,000+ automated agent runs per week
    at Amplitude; Claim 2: 60–70% of PRs auto-merge via risk-stratified Bugbot review): Erez's
    Claim 9 here (ephemeral per-branch environments replacing static test environments) and
    Claim 10 (risk-focused testing as agents write more code) describe the infrastructure and
    testing-philosophy changes that a deployment volume like Amplitude's would require in
    practice. Amplitude is the named-company evidence; Erez's claims are the general operational
    principles that would explain why such volume needs ephemeral environments and heavier
    automated risk review rather than static staging and human-paced review.
  - `docs-ghaw-safe-rollout.md` (four-rung autonomy-promotion ladder: report-only → staged →
    shadow evaluation → production writes): this is a different domain (rolling out AI agent
    *workflow* autonomy, not application deployments), but shares Erez's underlying logic in
    Claim 3 (continuous delivery — validated, gated progression — over continuous deployment —
    auto-ship everything). Both sources independently favor staged, validated promotion over
    all-at-once automation, applied to two different objects (application code vs. agentic
    workflow permissions).

- **Contradicts**: None identified. No existing source note stakes out an opposing position on
  roll-forward-vs-rollback, GitOps substrate requirements, feature-flag hygiene, or the specific
  CI-speed-to-test-rigor tradeoff in Claim 10.

- **Extends**:
  - `blog-pragmaticengineer-hightower-infrastructure-ai.md` (Claim 1: the imperative-to-declarative
    infrastructure paradigm shift as an analogy for AI's effect on software development): that
    source frames a high-level historical analogy from a Kubernetes-era infrastructure engineer;
    this source, from a CD-platform practitioner, provides the concrete pipeline-design mechanism
    (Claim 10) for one specific instance of that shift — CI/CD priorities moving from
    human-blocking speed to agent-shipped-bug risk.

- **Novel**:
  - **The specific causal chain in Claim 10** — CI speed matters today because slow builds block
    *humans who context-switch*; agents don't context-switch the same way, so that cost drops,
    freeing pipeline budget for more/slower verification — is new to the corpus. Existing sources
    argue for more testing rigor around AI-generated code (e.g. the quality postmortem) but do not
    articulate *why the traditional counter-pressure (build speed) weakens* as agents take over
    more of the waiting.
  - **Roll-forward vs. feature-toggle-rollback as two different risk classes** (Claims 1 and 4
    together): no existing source in the corpus draws this specific distinction between
    "reverting a deployment with migrated schema state" (risky) and "reverting a feature flag"
    (safe, recommended) as two categorically different classes of automated remediation action —
    relevant to scoping what an incident-response agent should be allowed to revert autonomously.
  - **Pull-based GitOps repo-throttling at thousand-cluster scale** (Claim 6) is a specific
    infrastructure-scaling limit not otherwise documented in the corpus.

## Guide Impact

- **Chapter 05 (Systems & Operations) — incident response and rollback authority for agents**:
  Add the roll-forward/toggle-rollback distinction (Claims 1 and 4) as a scoping rule for what an
  automated or agent-driven incident-response system should be allowed to do: toggle a feature
  flag off autonomously (low risk, no schema concerns) vs. trigger a full deployment rollback
  (higher risk when database migrations are involved — prefer forward-fix). Currently the corpus's
  automated-remediation examples (e.g. `blog-cursor-app-stability.md`'s metric-based rollback) do
  not draw this distinction explicitly; this source gives the guide language to separate the two
  remediation classes and recommend the lower-risk one as the default autonomous action.

- **Chapter 05 (Systems & Operations) — feature-flag hygiene as an agent-adjacent maintenance task**:
  Add Claim 5 (flags accumulate faster than they're removed) as a concrete argument for pairing any
  agent or process that creates feature flags with an equally automated flag-audit/removal job —
  otherwise the same low-friction-creation property that makes flags a good incident safety net
  (Claim 4) also makes them a compounding maintenance liability when agents create them at higher
  volume than human teams would.

- **Chapter 02/Chapter 03 (Harness Engineering / Verification) — the build-speed-to-test-rigor
  tradeoff**: Add Claim 10 as the concrete rationale for why AI-native pipelines should deliberately
  spend more wall-clock time on verification than human-paced pipelines did, rather than treating
  agent-driven development as a reason to optimize pipelines the same way (for speed). Pair with
  the quality postmortem's incident (`blog-anthropic-claudecode-quality-postmortem.md`) as the
  concrete cost of under-investing in this rigor, and with Amplitude's risk-stratified auto-merge
  rate (`blog-cursor-amplitude-autonomous-pipeline.md` Claim 2) as an example of a team already
  acting on a version of this tradeoff.

- **Chapter 03 (Verification) — ephemeral per-branch environments as a scaling response to agent
  output volume**: Add Claim 9 (ephemeral environments replacing static staging) as the
  infrastructure pattern that becomes necessary, not optional, once agent-driven PR/branch volume
  exceeds what a shared static test environment can support without queueing/contention. Cite
  alongside Amplitude's 1,000+ weekly automated runs as the volume regime where this applies.

- **Chapter 05 (Systems & Operations) — cloud-first assumptions and on-prem/regulated segments**:
  Add Claim 7 as a caution against guide recommendations that implicitly assume cloud-hosted
  control planes for AI-driven deployment automation — banks, financial institutions, and
  governments are a persistent on-prem segment that needs an equivalent pattern, not just a
  cloud-first one.

## Extraction Notes

- The full source was read via WebFetch across five separate targeted passes (article metadata
  and paywall check; full ten-point summary; deep-dive on observation #10 and all AI mentions;
  full body paragraphs for observations 1, 3, 4, 5, 6, 9; full body paragraphs for observations
  2, 7, 8, plus the guest bio). No paywall notice was encountered at any point — the ten
  observations and their body paragraphs, plus the guest bio, all appear to be freely accessible
  free-tier newsletter content. The underlying podcast audio/video (referenced via YouTube,
  Spotify, Apple Podcasts links) was not independently reviewed; this note is based on the
  written companion post only.
- The source is genuinely light on AI content: only observation #10 of ten addresses AI directly.
  The other nine observations are general CI/CD, GitOps, and deployment practices with no AI
  framing in the source itself — the AI-relevance connections drawn in Claims 1, 2, 5, 6, 7, 8,
  and 9's "Our assessment" fields are this note's own analytical extension, not claims Erez or
  Orosz make in the source. This is flagged so the Assayer and Smith can distinguish
  source-asserted claims from miner-drawn connections.
- No contradiction with an existing source note was found; none was filed.
- All cross-referenced claim numbers (quality-postmortem Claims 7–9 and 10; amplitude-pipeline
  Claims 2 and 8; hightower-infrastructure-ai Claim 1) and the app-stability "Metric-Based
  Rollbacks" artifact were verified by re-reading the cited notes before inclusion.
