---
source_url: https://simonwillison.net/2026/Apr/14/cybersecurity-proof-of-work/
source_type: blog-post
title: "Cybersecurity Looks Like Proof of Work Now"
author: Simon Willison (synthesizing Drew Breunig analysis and UK AISI evaluation)
date_published: 2026-04-14
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#248"
---

# Cybersecurity Looks Like Proof of Work Now

> Willison's link-blog synthesis of Drew Breunig's economic analysis and the UK AI
> Safety Institute's independent evaluation of Claude Mythos Preview: AI transforms
> cybersecurity into a token-spend arms race where defenders must outspend attackers,
> and open-source libraries become *more* valuable under this model because their
> hardening costs are amortized across all users.

## Source Context

- **Type**: blog-post (Simon Willison link-blog style, ~200 words, April 14 2026).
  The post summarizes and quotes from two substantive sources it links to:
  (1) Drew Breunig's analysis "Cybersecurity Is Proof of Work Now"
  (dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html), and
  (2) the UK AI Safety Institute's independent evaluation of Claude Mythos Preview
  (aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities).
  Both linked sources were fetched and are the primary basis for this extraction;
  Willison's post provides the synthesis and the corpus entry point.
- **Author credibility**: Simon Willison is the creator of Django and one of the
  most widely-cited independent commentators on LLM tooling — designated a
  `trusted-feed` source in this repo. His link-blog posts are editorial synthesis, not
  original research; he is curating and contextualizing, not generating primary data.
  Drew Breunig writes on AI, data, and technology at dbreunig.com — an analytical
  commentary voice rather than a researcher or vendor. The UK AI Safety Institute (AISI)
  is an independent UK government body established specifically to evaluate advanced AI
  capabilities; their evaluation is the primary empirical anchor for all claims in this
  cluster of sources.
- **Scope**: Covers the economic implications of AI-assisted vulnerability discovery —
  specifically the token-budget framing for security hardening and the consequences for
  open-source library value. Does NOT cover: red-team methodology details, defensive
  agent architectures, operational security program design, or patch prioritization
  frameworks (see `blog-anthropic-ai-accelerated-offense.md` for those). The AISI
  evaluation it cites covers CTF performance and a 32-step corporate network attack
  simulation; it explicitly notes that the tested environments lacked active defenders
  and defensive tooling.

## Extracted Claims

### Claim 1: AI-assisted vulnerability discovery has become a token-budget problem: defenders must spend more tokens finding exploits than attackers will spend exploiting them

- **Evidence**: Drew Breunig's economic analysis, drawing on the AISI evaluation of
  Claude Mythos Preview which showed that model performance on the "Last Ones" (TLO)
  32-step corporate network attack simulation continued improving across all token budgets
  tested up to 100M tokens — with no saturation observed. The AISI report states:
  "Mythos Preview's performance continues to scale up to this limit," suggesting further
  investment would yield further results.
- **Confidence**: emerging (the token-scaling observation is independently confirmed by
  AISI data; the economic inference — that this creates an arms-race equilibrium — is
  Breunig's analytical extrapolation, not a tested prediction)
- **Quote**: "to harden a system you need to spend more tokens discovering exploits than
  attackers will spend exploiting them." — Drew Breunig, as quoted by Simon Willison
- **Our assessment**: This is the central novel framing in the Willison/Breunig cluster.
  It operationalizes AI security in economic rather than capability terms. Prior corpus
  sources (especially `blog-anthropic-ai-accelerated-offense.md`) frame AI security as a
  threat timeline ("24 months to mass exploitation"); this source adds the equilibrium
  condition: the game is won by whoever can outspend the other in compute. For AI-native
  engineering teams, this has a concrete implication: security review budgets are now
  denominated in tokens, not engineering hours. The AISI data provides the key empirical
  support — the continued-scaling observation means there is no known saturation point at
  the current frontier, so spending more genuinely yields more security.

### Claim 2: Claude Mythos Preview completed 3 of 10 runs of a 32-step corporate network attack simulation that no other tested frontier model completed

- **Evidence**: AISI's "The Last Ones" (TLO) evaluation — an independent third-party
  benchmark. Mythos completed 3/10 attempts; average across all attempts was 22/32 steps.
  Claude Opus 4.6 (next best) averaged 16/32 steps. GPT-5.4 and other tested models did
  not complete the simulation. AISI estimates a human expert would require ~20 hours to
  complete all 32 steps.
- **Confidence**: emerging (third-party evaluation by a credible independent body;
  methodology — absent active defenders — limits generalization to real-world hardened
  environments)
- **Quote**: (AISI report) "Mythos Preview's performance continues to scale up to this
  limit" [100M token budget]. Average: "22 of 32 steps completed." Breunig: "Mythos
  completed the task in 3 out of 10 attempts; other models (Opus 4.6, GPT-5.4) did
  not complete it."
- **Our assessment**: This is the most concrete evidence underpinning the proof-of-work
  thesis. The 3/10 completion rate shows AI-level autonomous attack capability is real
  but not trivial — it requires significant compute per attempt. The cost figures
  (Claim 5 below) make this economically legible. The AISI caveat — environments
  lacked active defenders and defensive tooling — is important: the simulation reflects
  weakly defended network conditions; real-world hardened infrastructure was not tested.
  Claude Opus 4.6 at 16/32 average is still a significant capability even without
  full completion.

### Claim 3: Mythos Preview succeeds on 73% of expert-level CTF challenges that no prior model could complete before April 2025

- **Evidence**: AISI evaluation data. The evaluation tracked AI cyber capabilities since
  2023, progressively increasing difficulty as models improved; the 73% success rate is
  on the expert-level tier that prior models could not reach.
- **Confidence**: emerging (third-party benchmark; CTF challenges are stylized security
  exercises that may not fully represent real-world production environments, but
  expert-level CTFs are accepted as strong proxies for vulnerability discovery skills)
- **Quote**: (AISI) "Mythos Preview succeeds 73% of the time" on expert-level CTF
  challenges "which no prior model could complete before April 2025."
- **Our assessment**: The historical comparison ("which no prior model could complete
  before April 2025") contextualizes the pace of capability development more than the
  absolute number. If 0% → 73% happened in approximately one year (April 2025 to April
  2026), the rate of advance supports Anthropic's "24-month window" claim in
  `blog-anthropic-ai-accelerated-offense.md`. For the guide: this is the empirical
  grounding for the general claim that AI security capabilities are advancing rapidly.

### Claim 4: The token-performance correlation shows no saturation at 100M tokens per run — "models continue making progress with increased token budgets across all token budgets tested"

- **Evidence**: AISI evaluation specifically notes this as an observation across all
  tested budgets up to 100M tokens. The implication — that performance would continue
  improving beyond 100M — is an extrapolation, but the observed absence of saturation
  within tested ranges is a direct empirical finding.
- **Confidence**: emerging (direct AISI observation within tested range; extrapolation
  beyond 100M tokens is inference)
- **Quote**: (AISI) "Models continue making progress with increased token budgets across
  the token budgets tested."
- **Our assessment**: This is the technical foundation for the arms-race framing. If
  there were a saturation point (a token budget above which more spending yields no more
  security gain), the proof-of-work model would break down — defenders could cap
  investment. The absence of observed saturation at 100M tokens means the arms race is
  live: both attackers and defenders can keep spending for better results, at least within
  current frontier model ranges. For AI-native engineering teams: this means there is no
  "good enough" token budget for security hardening given the current capability curves —
  the target is always the attacker's likely budget, not a fixed bar.

### Claim 5: The cost per security hardening run is legible and significant: ~$12,500 per Mythos attempt at 100M tokens; a full 10-run campaign costs ~$125,000

- **Evidence**: Breunig's cost calculation based on the AISI token budget and published
  Anthropic API pricing.
- **Confidence**: anecdotal (cost figure is Breunig's calculation; pricing changes over
  time; this is a point-in-time estimate)
- **Quote**: (Breunig) "$12,500 per Mythos attempt; $125,000 for ten runs."
- **Our assessment**: This is the most practically legible number in the cluster. A
  $125,000 security hardening campaign (10 full-scale autonomous attack simulations) is
  within the budget of large enterprise security programs — comparable to a brief external
  penetration test or a portion of a senior security engineer's salary. For smaller
  organizations: even a single $12,500 run is comparable to a bug bounty payout for a
  critical finding. The cost figure denominalizes the proof-of-work equation: teams can
  now ask "how much should we spend per release on autonomous security review?" with a
  concrete order-of-magnitude anchor. Caveat: pricing will change as inference
  optimizations improve; the cost per token has historically dropped.

### Claim 6: Open-source libraries become *more* valuable under the token-economy security model because shared security hardening costs amortize across all users

- **Evidence**: Breunig's analytical argument extending from the proof-of-work framing.
  A token budget spent hardening a widely-used open-source library benefits every user of
  that library — the cost is shared, not incurred by each user independently. Willison
  quotes this as a notable implication: "open source libraries become more valuable, since
  the tokens spent securing them can be shared across all of their users."
- **Confidence**: anecdotal (logical argument from the economic model; no empirical data
  on actual shared security spending across OSS communities)
- **Quote**: "open source libraries become more valuable, since the tokens spent securing
  them can be shared across all of their users. This directly counters the idea that the
  low cost of vibe-coding up a replacement for an open source library makes those open
  source projects less attractive." — Simon Willison's synthesis
- **Our assessment**: This is the most counterintuitive claim in the cluster and the most
  novel to the corpus. The "vibe-coding makes open source less attractive" assumption
  (referenced in Willison and attributed to Karpathy's view on dependencies) predicts that
  cheap AI-generated bespoke code undermines the appeal of shared libraries. Breunig
  inverts this: under the proof-of-work security model, cost-of-security is the dominant
  term, and it favors shared infrastructure over bespoke. A well-used OSS library that
  gets $125,000 in autonomous security hardening amortizes that cost across 100,000 users
  at $1.25 per user; a bespoke replacement requires each user to spend the full amount.
  Note: this argument assumes the OSS library's maintainers or community actually perform
  the hardening; unmaintained libraries do not benefit from this logic (see the
  tension with `blog-anthropic-ai-accelerated-offense.md` Claim 10 in Cross-References).

### Claim 7: Breunig's three-phase development cycle positions "hardening" as a distinct, budgeted phase separate from code review

- **Evidence**: Breunig's explicit three-phase framework: (1) Development — quick
  iteration guided by human intuition; (2) Review — documentation and refactoring
  (~$15–20 per review via Anthropic's code review product); (3) Hardening — autonomous
  exploit identification with budgeted token spending.
- **Confidence**: anecdotal (Breunig's proposed framework; no practitioner reports of
  this specific three-phase cycle as an adopted workflow)
- **Quote**: (Breunig, paraphrased) Development → Review (~$15–20 per review) →
  Hardening (budgeted autonomous exploit-finding).
- **Our assessment**: The separation of "hardening" as a third phase distinct from
  standard code review is the operational implication of the proof-of-work thesis. Code
  review (Phase 2) is about correctness and maintainability; hardening (Phase 3) is
  adversarial — it requires a different agent, a different prompt, and a different budget
  authorization. This framing maps cleanly onto the Cursor four-agent fleet
  (`blog-cursor-security-agents.md`): their Agentic Security Review operates at the
  boundary of Phase 2/3 (pre-merge), while Vuln Hunter and Invariant Sentinel are
  pure Phase 3 (adversarial scanning, ongoing compliance). The $15–20 code review cost
  vs. $12,500 hardening run cost illustrates the order-of-magnitude budget difference
  between the two phases.

### Claim 8: Security vulnerability finding is an inherently verifiable task that suits AI capability evaluation

- **Evidence**: Breunig's characterization: "Finding exploits is a clearly defined,
  verifiable search problem." The AISI CTF/TLO benchmarks are structured exactly this
  way — success is binary and measurable.
- **Confidence**: settled (this is a structural property of the problem domain — CTFs
  and attack simulations have defined success conditions, unlike code quality or UX review)
- **Quote**: "Finding exploits is a clearly defined, verifiable search problem."
  — Breunig
- **Our assessment**: This is why security is the leading edge of AI-assisted software
  engineering verification. The binary success condition (found the exploit / didn't find
  it) enables clean benchmarking, which enables fast capability measurement, which is why
  AISI can publish precise numbers (73%, 3/10, 22/32 steps) that other AI capability
  domains cannot match. For the guide: security verification is the canary for AI
  capability in software engineering broadly — if AI can do security review at high
  reliability, code correctness verification is likely the next frontier.

### Claim 9: Code cost stays cheap; secure code cost rises unless AI reaches a point of diminishing security returns

- **Evidence**: Breunig's cost dynamics argument: as inference optimizations reduce
  per-token cost, the proof-of-work equilibrium adjusts — but only diminishing returns
  (not lower per-token prices) would break the arms race.
- **Confidence**: anecdotal (economic inference; no empirical data on attacker spend
  patterns or price elasticity of exploit discovery)
- **Quote**: "Code remains cheap, unless it needs to be secure. Even if costs go down
  as inference optimizations [improve], unless models reach the point of diminishing
  security returns, you still need to buy more tokens than attackers do." — Breunig
- **Our assessment**: This is the long-run economic projection. Declining inference costs
  (a historical trend) do not resolve the arms race because both defenders and attackers
  benefit equally from lower prices. Only capability saturation — where more tokens yield
  no more security insight — would break the equilibrium. Given that AISI observed no
  saturation at 100M tokens (Claim 4), that point is not yet reached. For AI-native
  engineering teams: infrastructure cost savings from inference optimization should be
  partially reinvested in token-based security hardening, not fully captured as margin —
  because attacker token budgets will also fall at the same rate.

## Concrete Artifacts

### The Three-Phase AI-Native Development Cycle

```
Breunig's Development Cycle (dbreunig.com, April 14, 2026)

Phase 1: Development
  — Quick iteration guided by human intuition
  — AI-assisted code generation, pair programming
  — Low token spend per action; high velocity

Phase 2: Code Review
  — Documentation + refactoring pass
  — Cost anchor: ~$15–20 per review (Anthropic code review product)
  — AI-assisted quality review
  — Gate: correctness, maintainability, style

Phase 3: Hardening
  — Autonomous exploit identification
  — Budgeted token spending (adversarial posture)
  — Cost anchor: $12,500 per full Mythos-scale attempt; $125,000 for 10-run campaign
  — Gate: security — must outspend likely attacker token budget
  — Distinct authorization: separate budget line from code review
```

### AISI "The Last Ones" (TLO) Benchmark Results

```
AISI Evaluation of Claude Mythos Preview — "The Last Ones" Corporate Network Attack Simulation
Source: aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
Published: approx. April 2026

Simulation parameters:
  — 32-step corporate network attack sequence
  — Estimated human expert completion time: ~20 hours
  — Token budget tested up to: 100M tokens per run
  — Cost per run (Mythos): ~$12,500 at 100M tokens

Results:
  Model                 | Completion rate | Avg steps completed
  ---------------------|-----------------|--------------------
  Claude Mythos Preview | 3/10 (30%)      | 22/32 steps
  Claude Opus 4.6       | 0/10 (0%)       | 16/32 steps
  GPT-5.4               | 0/10 (0%)       | not reported
  Other frontier models | 0/10 (0%)       | not reported

Key finding: "Mythos Preview's performance continues to scale up to this limit"
  — no saturation observed at 100M tokens

Caveat: environments "lacked active defenders and defensive tooling" — applies
primarily to weakly defended networks; real-world hardened environments not evaluated.
```

### AISI CTF Performance

```
AISI Expert-Level CTF Results (same evaluation)

Mythos Preview: 73% success on expert-level CTF challenges
Historical baseline: 0% — "no prior model could complete" these challenges before April 2025

Methodology: AISI has tracked AI cyber abilities since 2023, progressively increasing
difficulty as models improved. Expert-level tier newly unlocked by Mythos.
```

### Proof-of-Work Security Economics Model

```
Economic Equilibrium (Breunig formulation, April 2026)

Defenders: spend T_d tokens on autonomous hardening (finding exploits in own system)
Attackers: spend T_a tokens on autonomous exploitation (finding exploits in target)

Security condition: T_d > T_a

Characteristics:
  — Incumbent advantage: defenders run first and can set baseline
  — Scale advantage: open-source libraries amortize T_d across N users → T_d/N per user
  — No saturation point (as of April 2026, 100M token budget): more spend → more security
  — Price-symmetric: per-token cost reductions benefit attacker and defender equally

Implication for open source:
  Cost to harden widely-used library: T_d (one-time per release, shared)
  Cost to harden bespoke vibe-coded replacement: T_d (full cost, not shared)
  → OSS hardening cost per user << bespoke hardening cost per user
```

## Cross-References

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` — Anthropic's 24-month
  countdown claim (Claim 1) and the assertion that sub-frontier public models already find
  historical bugs (Claim 2) are grounded in the same capability landscape that this source
  documents with AISI data. The AISI finding (73% CTF success, 3/10 TLO completion)
  provides independent third-party evidence for the Anthropic threat-framing claims.
  Willison's post links to Willison's own April 7 post about Claude Mythos, which is the
  same Project Glasswing capability described in the Anthropic source.

- **Corroborates**: `blog-cursor-security-agents.md` — Cursor's investment in a four-agent
  security fleet at 3,000+ PRs/week is economically justified by the proof-of-work framing.
  Cursor is effectively operationalizing Phase 3 (hardening) of Breunig's development cycle
  at PR-level granularity. The Cursor note explains what the fleet does architecturally; this
  source provides the economic rationale for why the investment is necessary regardless of
  scale.

- **Extends**: `blog-anthropic-ai-accelerated-offense.md` — The Anthropic source provides
  the threat framing and the defensive program recommendations (seven recommendations);
  this source adds the missing economic layer: how to budget AI security spend, the
  equilibrium condition (outspend attackers), and the open-source cost-sharing advantage.
  The Anthropic source recommends "scan your code for vulnerabilities using AI before it
  ships" without a cost model; Breunig's framework provides the cost model.

- **Novel**:
  - The **tokens-as-security-budget framing** (proof-of-work equilibrium, T_d > T_a)
    is the first explicit economic model for AI security review spend in the corpus.
    All prior sources frame AI security in capability terms ("it finds bugs") or threat
    terms ("attackers will use it"); this is the first source to frame it in budget terms.
  - **AISI independent evaluation data** (73% CTF, 3/10 TLO, 22/32 avg steps, no
    saturation at 100M tokens, $12,500/run cost) is the first third-party quantitative
    benchmark data for frontier AI offensive capability in the corpus.
  - The **three-phase development cycle** (Development → Review ~$15–20 → Hardening
    ~$12,500+) is a novel workflow framework for AI-native engineering not present in
    any other corpus source.
  - The **open-source amortization argument** (shared token hardening costs make OSS
    more valuable under the proof-of-work model, not less) is new to the corpus and
    directly inverts the "vibe-code a cheap replacement" assumption.

- **Tension** (not a formal contradiction): `blog-anthropic-ai-accelerated-offense.md`
  Claim 10 recommends "AI vendoring" — using LLMs to reimplement unmaintained open-source
  dependencies to reduce supply chain risk. Breunig's open-source amortization argument
  runs in the opposite direction: replacing an OSS library with a bespoke implementation
  requires bearing the full Phase 3 hardening cost alone rather than sharing it. These
  claims address partially different scenarios (Anthropic targets *unmaintained* libraries;
  Breunig's argument applies most strongly to *well-maintained, widely-used* libraries),
  but both recommend actions that affect the same decision: "should I take a dependency
  on library X or reimplement it?" Teams should consider both arguments when making that
  call: unmaintained = supply chain risk → AI-vendor; well-maintained, widely-used =
  shared hardening cost → prefer OSS. If a material contradiction is later identified
  (e.g., if one source explicitly applies to maintained libraries as well), this should
  be filed using the contradiction template.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add the proof-of-work economic framing as the
  core budget model for AI security review. Specific addition: "Token-based security
  hardening is not a one-time cost — it is a recurring budget line calibrated against
  the attacker's likely token spend. The equilibrium condition (Breunig 2026): T_d > T_a.
  The AISI evaluation provides the cost anchor: ~$12,500 per full autonomous attack
  simulation at frontier capability, with no observed saturation at 100M tokens." Pair
  with Anthropic's threat framing for the complete picture.

- **Chapter 03 (Safety and Verification — Open Source Dependencies)**: Add the
  amortization argument as the economic rationale for preferring well-maintained OSS
  over bespoke AI-generated replacements for security-critical dependencies. Frame it
  explicitly as a counter to the "vibe-code a replacement" narrative: under the proof-
  of-work model, replacing widely-used OSS with bespoke code multiplies the defender's
  Phase 3 hardening cost by N (no sharing), which may exceed the replacement's
  development cost savings many times over for high-security contexts.

- **Chapter 02 (Harness Engineering — Security Workflow)**: Add Breunig's three-phase
  development cycle (Development → Review → Hardening) as a named workflow framework.
  The key addition is naming "hardening" as a distinct, separately-authorized phase
  rather than treating security review as a subset of code review. The cost differential
  (~$15–20 for review vs. ~$12,500+ for a hardening run) makes the budget distinction
  operationally real. Teams should treat Phase 3 hardening as a periodic release
  investment, not a per-PR action.

- **Chapter 03 or Introduction to Security section**: Cite the AISI benchmark data
  (73% CTF, 3/10 TLO, no saturation at 100M tokens) as the empirical grounding for
  why AI-native teams face a materially different threat environment. This is
  third-party validation — not vendor claims — of the AI offensive capability level.
  It belongs in any section that establishes why AI-accelerated security matters.

## Extraction Notes

1. **Willison post is thin; linked sources are substantive**: The Willison entry is
   ~200 words of synthesis. Both linked sources (Breunig's article and the AISI
   evaluation) were successfully fetched and are the primary basis for this extraction.
   Per the Prospector's guidance, the Breunig and AISI material is extracted directly.

2. **AISI evaluation environment caveat**: The TLO simulation lacked active defenders
   and defensive tooling. All quantitative capability numbers (73%, 3/10, 22/32 steps)
   apply to weakly-defended environments. Real-world organizations with mature security
   tooling should treat these as upper-bound attack-capability estimates, not expected
   real-world performance.

3. **Cost figures are point-in-time**: The $12,500/run figure is Breunig's calculation
   based on April 2026 pricing. Inference costs have historically declined; this number
   will likely decrease but the economic structure (attacker:defender budget ratio) is
   what matters, not the absolute cost.

4. **Karpathy anti-dependency reference**: Breunig cites Karpathy's view that
   "classical software engineering's belief that dependencies are good has to be
   re-evaluated" as the foil for the open-source amortization argument. The Karpathy
   quote is treated as context, not a corpus source, since no Karpathy source note
   exists in this repo.

5. **No sub-pages of Willison post followed beyond the two linked sources**: The post
   also links to Willison's own April 7 post about Claude Mythos (`/2026/Apr/7/
   project-glasswing/`) and a Honeycomb sponsor link; neither was followed as they
   are not substantive to the economic argument being extracted.
