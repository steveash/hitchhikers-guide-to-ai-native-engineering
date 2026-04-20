---
source_url: https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense
source_type: blog-post
title: "Preparing your security program for AI-accelerated offense"
author: Anthropic (security team; Project Glasswing / Claude Mythos Preview)
date_published: 2026-04-10
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#243"
---

# Preparing your security program for AI-accelerated offense

> Anthropic's first-party disclosure from their internal security research (Project
> Glasswing) establishing a 24-month countdown to AI-driven mass exploitation of
> known bugs, paired with seven concrete program-level recommendations including
> AI agent patterns for triage, autonomous red-teaming, patch generation, and
> detection coverage.

## Source Context

- **Type**: blog-post (Anthropic / Claude official blog, April 10, 2026)
- **Author credibility**: Published on the Anthropic/Claude blog and attributed to
  Anthropic's internal security team using frontier Claude models (Project Glasswing,
  Claude Mythos Preview) against real codebases. This is the model-maker reporting what
  their own models do when pointed at production systems. Maximum authority for claims
  about AI offensive capability timelines — Anthropic has direct access to capability
  curves that external researchers do not. The prescriptive recommendations are from
  practitioners who have run these experiments, not from analysts modeling threats
  theoretically.
- **Scope**: Covers the full security program lifecycle (vulnerability prioritization,
  code review, codebase audit, breach containment, exposure inventory, incident
  response) through an AI-acceleration lens. The seven recommendations range from
  basic hygiene to AI-native defensive patterns. Includes a sub-section for small
  organizations and one for AI-assisted vulnerability disclosure etiquette. Does NOT
  cover: red-team methodology details, agent architecture specifics beyond brief
  descriptions, or evidence that the defensive AI patterns have been independently
  benchmarked.

## Extracted Claims

### Claim 1: Within 24 months, widely available AI models will chain previously unnoticed bugs into working exploits at scale

- **Evidence**: Anthropic's internal findings from Project Glasswing and Claude Mythos
  Preview running against real codebases. First-party capability research, not a
  projection based on extrapolation.
- **Confidence**: emerging (first-party Anthropic research, not peer-reviewed; the
  24-month window is a prediction from the maker of the models in question)
- **Quote**: "Within the next 24 months, vast numbers of bugs that sat unnoticed in
  code, possibly for years, will be found by AI models and chained into working exploits."
- **Our assessment**: This is the central threat framing claim and it deserves weight
  because it comes from the source most likely to have accurate capability data —
  Anthropic. "Chained" is the operative word: AI doesn't just find individual bugs,
  it connects them. The implication for AI-native engineering teams (which produce
  significantly more code per developer) is that their expanded attack surface is
  especially exposed. The 24-month window sets an urgency threshold: security programs
  that have not yet shifted their posture have approximately 2 years before this
  becomes an active crisis, not a theoretical one.

### Claim 2: Sub-frontier publicly available models already find serious vulnerabilities that traditional code review missed for extended periods

- **Evidence**: Anthropic's direct observation from their own codebase audit work
  (Project Glasswing). Not a controlled benchmark but first-person operational
  evidence.
- **Confidence**: anecdotal (reported as internal observation; no public benchmark
  methodology or reproducibility details provided)
- **Quote**: "Today, publicly available models can find serious vulnerabilities that
  traditional reviews have missed for long periods."
- **Our assessment**: This claim is significant because it is not about frontier
  models — it explicitly says "publicly available." The implication: an attacker
  does not need access to Claude Opus or GPT-4 to find exploitable bugs in a
  production codebase. This directly changes the threat model for any team that
  assumed "only nation-state actors have these capabilities." The companion defensive
  claim (Recommendation 4) follows logically: if publicly available models can find
  historical bugs, teams should run those same models against their own code first.

### Claim 3: The patch window between publication and working exploit is shrinking due to AI-assisted reverse engineering

- **Evidence**: Anthropic's position as the developer of models being used for
  vulnerability research; no specific CVE timeline data cited.
- **Confidence**: emerging (logical inference from capability trends; first-party
  authority on what their models can do, but no empirical patch-to-exploit timeline
  data provided)
- **Quote**: "The window between a patch being published and an exploit becoming
  available is shrinking."
- **Our assessment**: This is the urgency multiplier for the patching recommendations.
  If traditional patch-to-exploit timelines were weeks-to-months, AI-assisted reverse
  engineering of patch diffs can compress this to days or hours. The 24-hour patching
  target for internet-facing systems (Recommendation 1) is calibrated to this reality.

### Claim 4: CISA KEV catalog + EPSS scoring is the correct two-tier prioritization framework for finite patching capacity

- **Evidence**: Anthropic's operational recommendation; references to established
  frameworks (CISA KEV maintained by US CISA; FIRST EPSS model updated daily based
  on observed exploitation data).
- **Confidence**: settled (both frameworks are well-established; the combination as
  a prioritization strategy is operationally sound and independently corroborated by
  practitioner guidance)
- **Quote**: "Patch everything on the CISA Known Exploited Vulnerabilities catalog
  first. For the remaining CVEs, use FIRST's Exploit Prediction Scoring System (EPSS)
  to prioritize based on the probability of exploitation within 30 days."
- **Our assessment**: This is the most immediately actionable concrete recommendation
  in the article. The KEV catalog is the emergency queue (known active exploitation);
  EPSS is the risk-ranked backlog (predicted exploitation probability). The two-tier
  structure handles the "too many CVEs to patch everything" problem without requiring
  custom scoring. For AI-native teams: the same AI triage agent that processes alerts
  can use EPSS scores as a structured input for patch prioritization, removing human
  judgment from the routine queue.

### Claim 5: Teams should plan for an order-of-magnitude increase in vulnerability finding volume

- **Evidence**: Logical projection from AI scanning capability; Anthropic frames this
  as necessary planning posture, not a measured observation.
- **Confidence**: emerging (directionally corroborated by Miller et al.'s 30.3%
  increase in static analysis warnings from AI-assisted development; the "order of
  magnitude" claim for AI-driven discovery is a projection)
- **Quote**: "Plan for an order-of-magnitude increase in finding volume."
- **Our assessment**: The "order of magnitude" framing is strong and potentially
  understated. Current security tooling (SAST, DAST, human review) is calibrated to
  a finding rate that human teams can triage. If AI scanning saturates that pipeline,
  the bottleneck shifts immediately to triage capacity. The automated triage agent
  recommendation (Recommendation 7) is the direct response: you cannot add human
  reviewers 10x faster than you add findings.

### Claim 6: AI vulnerability scanning of your own code before shipping is the single highest-ROI defensive action

- **Evidence**: Anthropic's prescriptive ranking of their seven recommendations.
- **Confidence**: anecdotal (editorial judgment by Anthropic's security team, not
  benchmarked)
- **Quote**: "If you implement one thing from this section, implement this: scan your
  code for vulnerabilities using AI before it ships."
- **Our assessment**: This is the asymmetric-advantage claim: attackers will use AI
  to find your bugs, so the first mover who uses AI to find their own bugs first wins.
  The recommendation is also the easiest for AI-native engineering teams to implement —
  they already have AI coding tooling in place. Adding a dedicated security scan pass
  (not general code review, but threat-model-focused scanning per the Cursor model)
  extends existing tooling to this use case.

### Claim 7: Placing a model at the front of the alert queue enables 100% alert coverage — a coverage level impossible with human-only triage

- **Evidence**: Anthropic's operational recommendation; framed as a known defensive
  pattern, not described as a benchmark result.
- **Confidence**: emerging (logically sound; consistent with Cursor's 3,000+ PR/week
  agent review at scale; no alert-queue baseline comparison provided)
- **Quote**: "Place a model at the front of your alert queue, so that every alert
  gets at least some investigation."
- **Our assessment**: The key word is "every." Human-only SOC teams operate under
  alert fatigue and statistical sampling; 100% alert coverage is not achievable at
  scale. An AI triage agent that processes every alert (even at low depth) ensures
  no alert goes completely uninvestigated. The design principle: human investigators
  get pre-triaged, de-duplicated, contextualized alerts rather than raw signal. This
  is architecturally parallel to Cursor's Agentic Security Review — the same triage-
  first pattern applied to runtime alerts instead of code PRs.

### Claim 8: Autonomous external red-teaming agents should test the network perimeter from outside

- **Evidence**: Anthropic's operational recommendation; no specific agent architecture
  details or results provided.
- **Confidence**: anecdotal (recommended practice; no benchmark comparison vs.
  human red-team or prior-generation automated scanners)
- **Quote**: "Deploy autonomous agents to conduct external red-teaming, probing your
  network perimeter as an attacker would."
- **Our assessment**: This is the mirror of the offensive acceleration claim applied
  defensively: if adversaries use autonomous agents to probe perimeters, the most
  effective defense is to probe your own perimeter with the same tool class first.
  The recommendation is consistent with the "find bugs before attackers do" asymmetric
  logic. The gap: no implementation details provided — what tool, what agent
  architecture, what scope constraints. The Cursor source provides the architectural
  pattern (autonomous agent fleet); this source provides the strategic rationale.

### Claim 9: The AI-driven detection flywheel (threat intel → candidate detections → hunt → tune) automates the historically manual detection engineering process

- **Evidence**: Anthropic's recommended defensive pattern; described as a workflow
  rather than a benchmarked implementation.
- **Confidence**: anecdotal (conceptual pattern with no implementation evidence or
  measured detection coverage improvement)
- **Quote**: (paraphrased from the detection engineering section — no direct verbatim
  quote available in the extracted summary)
- **Our assessment**: This is the most architecturally novel pattern in the article
  for detection engineering. The flywheel structure closes the loop: threat intel
  informs what to look for, AI generates candidate SIEM/EDR detections, automated
  hunting validates them against real data, and the results tune both the detection
  library and the AI's future generation. Mapping this against MITRE ATT&CK provides
  structured coverage tracking. Teams currently doing detection engineering manually
  (write rule → test → deploy → tune) can use this pattern to parallelize the
  write-and-test phases.

### Claim 10: "AI vendoring" — having an LLM reimplement an unmaintained dependency — reduces supply chain risk from abandoned packages

- **Evidence**: Anthropic's recommendation; described as a defensive strategy for
  reducing open-source supply chain exposure.
- **Confidence**: anecdotal (novel strategy with no published adoption data or
  failure-mode analysis)
- **Quote**: "Use LLMs to reimplement unmaintained dependencies ('AI vendoring')
  rather than pulling in untrusted open-source packages."
- **Our assessment**: This is the most novel tactical recommendation in the article
  and the most relevant to AI-native engineering specifically. If AI can generate a
  functionally equivalent replacement for a small unmaintained library, teams can
  eliminate the dependency without manual rewrite cost. The risks (correctness of the
  reimplementation, hidden behavioral divergence, responsibility shift from upstream
  maintainer to internal team) are significant and unaddressed. For the guide: this
  warrants a dedicated "emerging practice with open risks" treatment rather than a
  direct recommendation. The signal-to-noise ratio is high but the failure modes
  need mapping before this becomes guide advice.

### Claim 11: Zero-trust architecture with identity-based service isolation and short-lived tokens limits blast radius when AI-assisted attacks succeed

- **Evidence**: Anthropic's architectural recommendation; references industry best
  practices (zero-trust, hardware-bound credentials, service isolation).
- **Confidence**: settled (zero-trust architecture is independently established best
  practice; AI acceleration makes it more urgent, not novel)
- **Quote**: "Replace long-lived secrets with short-lived tokens. Tie access to
  verified hardware rather than credentials alone. Enforce identity-based isolation
  between services."
- **Our assessment**: This is not an AI-specific recommendation, but it is AI-urgency-
  elevated. AI-assisted attacks will break credentials faster (credential stuffing,
  phishing automation, secret scanning of repos at scale). Short-lived tokens with
  hardware binding reduce the blast radius when any single credential is compromised.
  For AI-native engineering teams: the increased code and repository volume creates
  more opportunities for accidental secret exposure, amplifying the importance of
  token rotation.

### Claim 12: Human decision-speed should never rate-limit evidence collection during incident response — AI handles collection, humans handle containment

- **Evidence**: Anthropic's operational framing of the human/AI division of labor
  during incident response.
- **Confidence**: emerging (sound operational principle; consistent with Cursor's
  human-in-control-of-containment pattern)
- **Quote**: "Human decision-speed should never be rate-limited on aspects that would
  be better handed to an AI, like evidence collection or write-ups."
- **Our assessment**: This is the clearest articulation in the article of AI's role
  in the human/AI work split during incidents. The principle is: AI handles the
  time-insensitive but high-volume work (evidence collection, log correlation,
  timeline construction, write-ups); humans handle the time-sensitive and
  consequential work (containment decisions, communications, escalation). This is
  architecturally the same division as Cursor's gradual trust rollout: AI operates
  in informational mode (evidence collection) before being trusted with action
  mode (containment).

## Concrete Artifacts

### Seven-Recommendation Security Program Framework

```
Anthropic AI-Accelerated Defense Framework (claude.com/blog, April 2026)
Based on Project Glasswing internal research.

Priority order from the article:

1. CLOSE YOUR PATCH GAP
   — Emergency queue: CISA Known Exploited Vulnerabilities (KEV) catalog
   — Prioritized backlog: FIRST EPSS (exploit probability within 30 days)
   — Timeline: internet-facing systems within 24 hours of exploit availability;
               other systems within days
   — AI assistance: automate triage, deduplication, patch generation

2. PREPARE FOR HIGHER VULNERABILITY VOLUME
   — Plan for order-of-magnitude increase in finding volume
   — OpenSSF Scorecard to assess open-source dependency security signals
   — Extend security expectations to third-party vendors
   — AI assistance: automated triage of the incoming finding flood

3. FIND BUGS BEFORE SHIPPING
   — Static analysis + AI-assisted code review in CI/CD (most critical single action)
   — Automated penetration testing in continuous delivery pipeline
   — CISA Secure by Design pledge commitments
   — Prefer memory-safe languages (Rust, Go, managed runtimes) for new code
   — OWASP ASVS for security requirements baseline

4. AUDIT EXISTING CODEBASES
   — "Most long-running production code has never been examined by a frontier model"
   — Prioritize: code parsing untrusted input, authentication handlers, legacy code
   — AI assistance: frontier model scanning for bugs humans missed for years

5. DESIGN FOR BREACH
   — Zero-trust: authentication on every request
   — Replace long-lived secrets with short-lived tokens
   — Tie access to verified hardware (not credentials alone)
   — Identity-based isolation between services
   — SLSA framework for build provenance and integrity

6. REDUCE AND INVENTORY EXPOSURE
   — Current inventory: every internet-facing host, service, and API endpoint
   — Decommission unused systems
   — AI assistance: autonomous external red-teaming agents

7. SHORTEN INCIDENT RESPONSE TIME
   — AI model at front of alert queue (100% alert coverage)
   — Primary metrics: dwell time and coverage (not alert count)
   — AI handles: evidence collection, timeline construction, write-ups
   — Humans handle: containment decisions (kept in control)
   — MITRE ATT&CK mapping for structured detection coverage tracking
   — Establish emergency change procedures in advance
```

### AI-Driven Detection Flywheel

```
Detection Engineering Flywheel (Anthropic recommendation, April 2026)

Threat intelligence feed
  ↓
AI generates candidate detections
  ↓
Automated hunting validates against real data
  ↓
Results tune detection library + AI generation
  ↓
Coverage mapped against MITRE ATT&CK framework

Design note: closes the loop between what attackers do (threat intel)
and what defenders detect (SIEM/EDR rules). Currently manual in most
SOC workflows — AI generation parallelizes the write/test phases.
```

### Small Organization Priority List

```
Four actions for resource-constrained organizations:

1. Enable automatic updates across all systems
2. Prefer managed services over self-hosting
   (security responsibility transfers to vendor)
3. Use passkeys / hardware security keys (phishing-resistant)
4. Enable free security tooling:
   - GitHub Dependabot (dependency vulnerability alerts)
   - GitHub CodeQL (code scanning)
   - GitHub secret scanning (accidental credential exposure)
```

### AI-Assisted Vulnerability Disclosure Requirements

```
When submitting AI-assisted vulnerability reports, include:

1. Plain-language bug description and impact
2. Detailed code path analysis (where the vulnerability lives)
3. Working reproduction / proof-of-concept
4. Proposed patch
5. Explicit disclosure: "This report was AI-assisted"
6. Deference to maintainer judgment (do not demand timeline)

Note: AI-assisted disclosure is now expected, not exceptional.
Maintainers need the AI disclosure to calibrate report quality.
```

## Cross-References

- **Corroborates**: `source-notes/blog-cursor-security-agents.md` — Cursor's defensive
  agent fleet (3,000+ PRs/week, 200+ vulnerabilities/week) is a production implementation
  of the same patterns Anthropic recommends here: triage agents at scale, autonomous
  scanning, patch generation. The Cursor note provides architecture; this Anthropic note
  provides the strategic threat model that makes those investments necessary. Together they
  form the complete picture: threat accelerates (Anthropic) → agent fleet responds (Cursor).

- **Corroborates**: `source-notes/discussion-hn-autofix-hybrid-review.md` — DeepSource's
  benchmark showing Claude Code recall at 48.78% for security on full diffs directly
  supports Anthropic's Recommendation 3: general-purpose AI code review is insufficient
  for security; dedicated, threat-model-focused AI scanning is required. This is the
  empirical evidence behind the "if you implement one thing, implement AI security
  scanning" recommendation.

- **Corroborates**: `source-notes/paper-miller-speed-cost-quality.md` — Miller et al.'s
  finding of a 30.3% increase in static analysis warnings from AI-assisted development
  partially validates Anthropic's "order-of-magnitude finding volume increase" claim
  (Claim 5). Miller's data is for static analysis warnings from AI-generated code; this
  article's claim extends to the additional signal from AI-powered security scanners.
  Both point to the same conclusion: the finding-to-reviewer ratio breaks without
  automated triage.

- **Extends**: `source-notes/blog-cursor-security-agents.md` — Anthropic's threat framing
  provides the missing "why" for Cursor's agent fleet investment. The Cursor note
  documents what the fleet does; this note establishes why a 5x PR velocity increase
  alone doesn't explain the urgency. The AI-accelerated offense timeline (24 months) is
  the deeper motivation: even if PR velocity were constant, the threat environment is
  accelerating independently.

- **Novel**:
  - The **24-month countdown to mass AI-driven exploit chaining** is the first explicit
    timeline claim in the corpus. No other source names a specific window.
  - **CISA KEV + EPSS as a structured two-tier patching prioritization framework** is not
    documented in any other corpus source. This is a concrete, immediately actionable
    protocol.
  - The **AI detection flywheel** (threat intel → AI-generated detections → hunt →
    tune → MITRE ATT&CK coverage) is a novel agent workflow pattern not described
    in the Cursor or other agent fleet sources.
  - **"AI vendoring"** (LLM reimplementation of unmaintained dependencies) is a novel
    supply chain risk reduction strategy with no prior corpus coverage. High-risk claim
    requiring more evidence before guide adoption.
  - The **human/AI work split during incident response** (AI = evidence collection and
    write-ups; humans = containment decisions) is articulated more clearly here than
    in any other corpus source.
  - **AI-assisted vulnerability disclosure etiquette** (explicit AI disclosure to
    maintainers) is a new professional norm documented here for the first time in the
    corpus.

## Guide Impact

- **Chapter on Security / Threat Model**: Add the 24-month timeline claim as the opening
  framing for why AI-native engineering teams face a different security environment.
  Cite this source for the claim that sub-frontier publicly available models already
  find historical bugs — this directly changes the "only nation-state actors" threat model
  assumption that prior chapters may implicitly carry.

- **Chapter on Security / Defensive Patterns**: The seven-recommendation framework should
  anchor the defensive practices section. Specifically: (1) CISA KEV + EPSS as the
  named vulnerability prioritization framework; (2) AI security scan before shipping as
  the single highest-ROI action; (3) 100% alert coverage via AI triage agent as the
  incident response design principle. Each maps to a concrete AI-native pattern already
  documented in `blog-cursor-security-agents.md`.

- **Chapter on Agentic Workflows / Security Agents**: The detection flywheel is a new
  named agent workflow pattern to add alongside Cursor's four-agent fleet. The flywheel
  applies to a different part of the security lifecycle (detection engineering, not code
  review or dependency patching) and completes the agent coverage of the full security
  program.

- **Chapter on Harness Engineering / Tool Selection**: The "AI vendoring" recommendation
  is high enough novelty and low enough evidence that it warrants an "emerging practice
  with open risks" call-out rather than a direct recommendation. Document the concept,
  flag the correctness and ownership risks, and recommend validating with a controlled
  pilot before adopting as a policy.

- **Chapter on Team Adoption / Risk Surface**: The claim that AI-native teams producing
  more code per developer also produce more attack surface connects the velocity benefits
  documented in multiple sources to a concrete security cost. This provides the missing
  security risk dimension in any chapter section on team adoption ROI.

## Extraction Notes

1. **Source required JavaScript rendering**: The source URL is `claude.com/blog/...` which
   required JS rendering for full content access. The WebFetch tool returned a well-
   structured summary with direct quotes. The extraction is based on this rendering;
   no paywall was encountered.

2. **Project Glasswing / Claude Mythos Preview**: The triage comments reference these
   internal Anthropic project names as the basis for the empirical claims. Neither is
   elaborated in the public article; they establish that the claims are based on
   first-party red-team research, not market analysis.

3. **No architecture specifications for AI defensive agents**: While Anthropic recommends
   triage agents, autonomous red-teaming, and the detection flywheel, they do not provide
   implementation details. The Cursor note fills this gap architecturally. For guide
   purposes, this source provides the strategic rationale; the Cursor note provides the
   implementation patterns.

4. **Confidence calibration**: The core threat claims (24-month window, patch gap
   shrinking) are rated emerging rather than settled because they are first-party
   predictions from a model builder, not peer-reviewed longitudinal studies. Their
   authority is high; their independent verifiability is currently low.
