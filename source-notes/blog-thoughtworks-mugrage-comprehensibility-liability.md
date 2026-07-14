---
source_url: https://www.thoughtworks.com/insights/blog/security/code-you-don-t-understand-is-a-liability-you-can-t-defend
source_type: blog-post
title: "Code you don't understand is a liability you can't defend"
author: Ken Mugrage (Head of Insights, Thoughtworks)
date_published: 2026-06-25
date_extracted: 2026-07-14
last_checked: 2026-07-14
status: current
confidence_overall: emerging
issue: "#1854"
---

# Code you don't understand is a liability you can't defend

> Responding to the Five Eyes agencies' June 22, 2026 joint warning on
> AI-accelerated exploit timelines, Mugrage argues the "patch faster" framing
> is incomplete: the load-bearing security asset is *comprehensibility* — the
> degree to which system owners can reason about behavior, locate boundaries,
> and predict change impact — and proposes three enforcement instruments
> (executable specification, boundaries/contracts, observability) plus a
> starter set of comprehensibility metrics.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, security category; filed via the
  trusted `thoughtworks` RSS feed, published 2026-06-25, three days after the
  Five Eyes statement it responds to).
- **Author credibility**: Ken Mugrage, Head of Insights at Thoughtworks, is
  already an established corpus author via `blog-thoughtworks-mugrage-is-developer-experience-dead.md`
  (2026-06-23) and `blog-thoughtworks-mugrage-claude-outage-infrastructure.md`.
  This piece is editorial/argumentative, not a case study or controlled
  study: it cites the Five Eyes agencies' own statement as its evidentiary
  anchor but does not cite named client engagements, survey data, or
  benchmarked metrics for its own proposed instruments or metrics.
- **Scope**: Covers a response to the Five Eyes June 22, 2026 joint warning on
  AI-accelerated vulnerability-to-exploit compression; argues comprehensibility
  (not patch speed) is the asset that determines defensibility; defines
  comprehensibility; names three protective instruments (enforced
  specification, boundaries, observability); and proposes four starter
  metrics for measuring it. Does NOT cover: implementation mechanics for any
  of the three instruments (no code, no tool names, no config examples), a
  citation for the Five Eyes statement's original text beyond its own framing
  of "the headline," or any organizational rollout guidance for adopting the
  proposed metrics.

## Extracted Claims

### Claim 1: The Five Eyes agencies' June 22, 2026 joint warning framed the core problem as a speed problem — the shrinking gap between vulnerability discovery and working exploit — but even the agencies themselves acknowledge tools alone won't fix it
- **Evidence**: Author's characterization of the Five Eyes statement and his reading of its own self-qualification.
- **Confidence**: emerging
- **Quote**: "When the leaders of the Five Eyes cyber security agencies issued their joint warning on AI and cyber risk this week (June 22), the headline was about speed: frontier models are compressing the time between a vulnerability being discovered and a working exploit existing. If the gap is closing, the argument goes, close it faster. Patch sooner, scan more and buy the tool that promises to keep pace. While this may feel like the correct instinct given the urgency of Five Eyes warning, it's ultimately an incomplete one. Indeed, the agencies say as much themselves, noting that tools alone won't inevitably deliver security."
- **Our assessment**: This is the article's framing hook, not an independently verified claim — we have not separately verified that the Five Eyes statement itself says "tools alone won't inevitably deliver security" (Mugrage's paraphrase of the agencies' position, not a quote from them). Treat this claim as Mugrage's characterization of the Five Eyes statement, which is plausible given the widely-reported content of such joint advisories, but not independently confirmed against the primary Five Eyes text in this extraction pass.

### Claim 2: The harder, more important question than patch speed is whether you still understand what you're defending well enough to defend it at all
- **Evidence**: Author's thesis statement, immediately following Claim 1's framing of the incomplete "patch faster" instinct.
- **Confidence**: emerging
- **Quote**: "So, what _will_ deliver it? The key point that's all too often overlooked by missives that urge caution is that we need to tackle the harder question: understanding what you're defending in the first place and whether you still understand it well enough to defend it at all."
- **Our assessment**: This is the load-bearing reframe of the whole piece — from "how fast can you react" to "do you still understand the thing you're reacting for." It's an assertion, not a measured finding, but it is a clean, guide-usable thesis statement that sharpens the existing corpus comprehension-debt material into an explicit security claim rather than a productivity/quality claim.

### Claim 3: AI-generated code volume is growing faster than the trust and understanding needed to safely rely on it
- **Evidence**: Author's economic framing of the code-generation/comprehension gap.
- **Confidence**: emerging
- **Quote**: "We're accumulating code faster than we accumulate the trust to rely on it. When a model can produce a plausible module in seconds, the volume of software grows far quicker than the understanding that should accompany it."
- **Our assessment**: This restates the corpus's now-familiar "generation is cheap, understanding is not" convergence (see Cross-References) in security-specific language: the risk framed here isn't wasted review time or stale documentation, it's an unassessed and growing attack surface. The claim is directionally consistent with everything else in the corpus on this topic but, like those other sources, offers no measurement of the growth-rate gap itself.

### Claim 4: Comprehensibility is a specific, definable property — the degree to which system owners can reason about behavior, locate boundaries, and predict the effect of a change
- **Evidence**: Author's explicit definition, offered as the article's central term.
- **Confidence**: emerging
- **Quote**: "_Comprehensibility_ is the degree to which the people who own a system can reason about its behaviour, locate its boundaries and predict what a change will do."
- **Our assessment**: This is a usable, three-part operational definition (reason about behavior / locate boundaries / predict change impact) rather than a vague appeal to "understanding." It gives the guide a concrete definition to cite when discussing comprehension debt in a security context, distinct from the more general "comprehension debt" framing already in the corpus (see Cross-References).

### Claim 5: Comprehensibility is what actually enables the three things security response depends on — containment, prioritization, and safe patching — not raw response speed
- **Evidence**: Author's direct statement connecting the definition of comprehensibility to concrete security outcomes.
- **Confidence**: emerging
- **Quote**: "Defence at machine speed is built on comprehension at every step: Containing a breach means knowing what a compromised component can reach. Prioritizing means knowing which flaws matter to your particular system. Patching safely means knowing what a change will break before it breaks it."
- **Our assessment**: This is the article's clearest mechanistic argument: it doesn't just assert comprehensibility matters, it names the three specific security activities (containment, prioritization, safe patching) that comprehensibility is a precondition for, and argues each fails silently without it. This is the strongest single passage to cite if the guide wants to justify *why* comprehensibility, not speed, is the security-relevant metric.

### Claim 6: Executable specification — tests and specs that gate what a system must and must not do — is one of the instruments that protects comprehensibility, in contrast to prose documentation nobody reads
- **Evidence**: Author's first named protective instrument.
- **Confidence**: emerging
- **Quote**: "Tests and specs should be executable, gating definitions of what the system must and must not do, rather than prose that no one reads after the first sprint."
- **Our assessment**: This draws an explicit enforcement/exhortation distinction — a spec that gates (fails a build, blocks a merge) versus a spec that only documents. This is a specific, actionable claim that goes beyond "write good docs" and instead argues documentation should be executable, i.e., a control, not a courtesy.

### Claim 7: Boundaries and strict encapsulation are a second instrument — they keep comprehension local, so no single change requires holding the entire system in your head
- **Evidence**: Author's second named protective instrument.
- **Confidence**: emerging
- **Quote**: "Contracts and strict encapsulation keep comprehension local, so that changing or containing one part does not require holding the whole system in your head."
- **Our assessment**: This connects architectural boundary discipline directly to the security claim rather than treating it as a separate "good architecture" concern — the argument is that encapsulation is what makes Claim 5's "containing a breach" tractable at all, because it scopes what a compromised component can reach.

### Claim 8: Observability built for real-time decisions (not compliance reporting) is a third instrument — it keeps a running system legible while it's running
- **Evidence**: Author's third named protective instrument.
- **Confidence**: emerging
- **Quote**: "Instrumentation built for real-time decisions, rather than for compliance reporting, keeps the running system legible while it runs."
- **Our assessment**: The distinction drawn here — instrumentation for real-time decision-making versus instrumentation for after-the-fact compliance reporting — is a specific and useful design criterion. It implies observability tooling should be evaluated by whether an operator can use it to make a decision *during* an incident, not just whether it produces an auditable log afterward.

### Claim 9: Comprehensibility needs rough instrumentation even before precise metrics exist, and the article proposes four specific starting metrics
- **Evidence**: Author's explicit call for measurement, followed by a concrete starter list.
- **Confidence**: anecdotal (the metrics are proposed, not validated or benchmarked against any organization)
- **Quote**: "An asset you cannot measure is one you will not protect. That's why comprehensibility needs rough instrumentation even before it has precise metrics." The four proposed starting points: "The proportion of a running system any single engineer can reason about without help." / "The mean time to localize a fault." / "How much of the codebase has no current owner who understands it." / "Specification and observability coverage as proxies for how much intent is encoded and how much of the system is visible."
- **Our assessment**: These four metrics map directly onto Claims 4, 6, 7, and 8 (respectively: the definition itself, fault localization as a proxy for boundary clarity, ownership as a proxy for who can reason about the system, and spec/observability coverage as proxies for the two named instruments). None are benchmarked or given target thresholds in the article — they are offered explicitly as a starting point, not a validated measurement framework, which is why we rate this claim anecdotal despite the emerging-confidence claims around it.

### Claim 10: The right question for a security posture isn't "how fast can you patch" but "how much of what you run could you still explain"
- **Evidence**: Author's closing restatement of the thesis.
- **Confidence**: emerging
- **Quote**: "The window will keep shrinking; no tool you buy will change that. What you can change is whether the systems on the other side of the alarm are ones your people still understand. Defend comprehensibility as the asset and use architecture, contracts, specifications and observability as the instruments that keep it solvent." / "The question to put to your own estate is not how fast you can patch; it's how much of what you run you could still explain."
- **Our assessment**: This closing line is the single most quotable sentence in the piece and directly extends the guide's existing principle that "AI makes code cheap to generate. It does not make understanding cheap to skip." (see Guide Impact) into an explicit security-liability framing rather than a quality/maintainability framing.

## Concrete Artifacts

```
Three protective instruments for comprehensibility
(Ken Mugrage, Thoughtworks, "Code you don't understand is a liability
you can't defend," 2026-06-25)

1. Enforced specification
   "Tests and specs should be executable, gating definitions of what the
   system must and must not do, rather than prose that no one reads after
   the first sprint."

2. Boundaries
   "Contracts and strict encapsulation keep comprehension local, so that
   changing or containing one part does not require holding the whole
   system in your head."

3. Observability
   "Instrumentation built for real-time decisions, rather than for
   compliance reporting, keeps the running system legible while it runs."

Starter metrics for comprehensibility (same source):
   - The proportion of a running system any single engineer can reason
     about without help.
   - The mean time to localize a fault.
   - How much of the codebase has no current owner who understands it.
   - Specification and observability coverage as proxies for how much
     intent is encoded and how much of the system is visible.
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-intent-debt.md` (Claim 9: "software's scarce resource
    shifted from the ability to produce correct implementation... to intent,
    the one input that must still originate with a human"): both sources
    converge on the same underlying shape — generation is cheap, the human
    contribution that matters is the one AI cannot supply (intent for
    Osmani, comprehension for Mugrage) — applied here specifically to
    security liability rather than to engineering economics.
  - `blog-simonwillison-litt-understand-to-participate.md` (Claim 1: "the
    need to avoid taking on cognitive debt as your understanding drifts from
    how the code actually works"): Litt's cognitive-debt-from-drift mechanism
    is the same phenomenon Claim 3 here describes at the level of an entire
    codebase/system rather than a single collaborative session.
  - `blog-thoughtworks-mugrage-is-developer-experience-dead.md`: same author,
    published two days earlier (2026-06-23); that piece argues agentic
    coding relocated cognitive cost from mechanical typing friction to
    verification fatigue and architectural decision-making load. This piece
    is a direct continuation of that argument applied specifically to
    security rather than developer experience — both pieces treat "who still
    understands the system" as the scarce resource, just with different
    framing (DevEx vs. security liability).

- **Contradicts**: None identified. This piece does not dispute the Five
  Eyes agencies' urgency claim (compressed exploit timelines are real); it
  argues the *response* the urgency implies (patch faster) is incomplete
  without comprehensibility. `blog-anthropic-zero-trust-ai-agents.md` also
  argues that friction/speed-only controls are insufficient (its "impossible
  vs. tedious" test, Claim 3 of that note) and instead prescribes structural
  controls (identity, boundaries, sandboxing) — the same anti-speed-only
  argument, from a controls vocabulary rather than a comprehensibility
  vocabulary. These are complementary framings of the same position, not a
  disagreement, so no contradiction issue was filed.

- **Extends**:
  - `blog-anthropic-zero-trust-ai-agents.md` (Claim 3, the "impossible vs.
    tedious" test, and Claim 19, identity-based isolation as the primary
    boundary control): that note's architecture answers "what controls
    should exist"; this piece answers a prior question — "can the people
    running those controls actually reason about the system those controls
    protect." Claim 7 here (boundaries keep comprehension local) gives an
    explicit *comprehension* rationale for the same encapsulation/boundary
    discipline that note frames purely as an attack-surface-reduction
    control.
  - `blog-anthropic-zero-trust-ai-agents.md` (Claim 20, dwell time and
    coverage as the two metrics that matter most): Claim 9 here proposes a
    parallel, non-overlapping metrics set specifically for comprehensibility
    (proportion of system reasoned-about, MTTR-to-localize, ownership
    coverage, spec/observability coverage) rather than incident response
    speed — the guide could present both metric sets together as covering
    different security dimensions (response operations vs. underlying
    system legibility).

- **Novel**:
  - The explicit definition of "comprehensibility" as a named security asset
    (Claim 4), distinct from the corpus's existing "comprehension debt" /
    "cognitive debt" framings, which describe an eroding liability rather
    than defining the positive asset being eroded.
  - The direct causal claim (Claim 5) that comprehensibility specifically
    enables containment, prioritization, and safe patching — no existing
    corpus note connects architectural/documentation practices to these
    three named incident-response capabilities this explicitly.
  - The four-metric starter list for measuring comprehensibility (Claim 9)
    is new to the corpus; the closest existing metrics (Zero Trust's dwell
    time/coverage) measure incident response speed, not system legibility.

## Guide Impact

- **Chapter 00 (Principles)**: The existing "Comprehension Work Is the Job"
  section (citing `blog-addyosmani-code-agent-orchestra`, Linked Source 6)
  currently frames comprehension loss as a quality/maintainability risk.
  Add Claim 2 and Claim 10 from this source alongside it to extend that
  principle with an explicit security-liability framing: understanding is
  not just what makes code maintainable, it's what makes a system
  defensible. The closing line ("the question to put to your own estate is
  not how fast you can patch; it's how much of what you run you could still
  explain") is a citable, guide-ready restatement of the existing principle
  in security terms.

- **Chapter 06 (Security & Threat Model)**: This chapter currently has no
  content connecting architecture/documentation practices to security
  outcomes via a comprehensibility lens (confirmed: no existing mention of
  "comprehensibility," specifications, or boundaries-as-security-control in
  `guide/06-security-threat-model.md`). Add a new subsection introducing
  comprehensibility (Claim 4) as a named security asset, citing Claim 5 for
  *why* it matters (containment, prioritization, safe patching) and Claims
  6-8 for the three enforcement instruments (executable specs, boundaries/
  contracts, observability). Pair with `blog-anthropic-zero-trust-ai-agents.md`
  Claim 3 (the "impossible vs. tedious" test) as a parallel evaluation
  heuristic — both sources argue friction/speed-only measures are
  insufficient, this source's angle is "can you still reason about it,"
  Zero Trust's is "does the control remove the capability or just slow it
  down."

- **Chapter 06 (Security & Threat Model) — Metrics**: Add Claim 9's four
  starter metrics (proportion of system any engineer can reason about
  unaided, MTTR-to-localize-fault, unowned-codebase proportion, spec/
  observability coverage) as a comprehensibility-specific complement to
  `blog-anthropic-zero-trust-ai-agents.md` Claim 20's dwell-time/coverage
  metrics — the guide should present these as two different measurement
  axes (incident response speed vs. underlying system legibility) rather
  than competing metric sets.

## Extraction Notes

- The article was fetched via WebFetch across four targeted passes (opening/
  Five Eyes framing; three instruments + metrics + closing; comprehensibility
  definition + transition paragraph; verbatim metrics list confirmation) to
  cross-check that quoted passages were stable and consistent across
  independent fetches, since WebFetch summarizes through a small model rather
  than returning raw HTML. The four-item metrics list (Claim 9) was
  requested twice, independently, with different prompt wording, and returned
  identical wording both times, which is the basis for treating it as a
  verbatim quote rather than a paraphrase.
- No sub-pages were followed: the article does not link out to other
  substantive pages (its outbound link is to the Five Eyes agencies'
  statement itself, referenced only by description — "issued their joint
  warning on AI and cyber risk" — not quoted from directly in this note; we
  did not independently fetch and verify the primary Five Eyes text against
  Claim 1's characterization of it).
- The article has no named case studies, client engagements, or benchmark
  data of its own — its confidence is rated "emerging" overall because it is
  a coherent, first-party editorial argument from an established corpus
  author (Ken Mugrage) responding to a real, dated external event (the Five
  Eyes June 22, 2026 statement), but the three instruments and four metrics
  it proposes are presented as reasoned recommendations, not validated
  practices.
- Did not find a contradiction warranting a filed contradiction issue (see
  Cross-References → Contradicts) — the closest candidate
  (`blog-anthropic-zero-trust-ai-agents.md`'s speed/urgency framing vs. this
  source's "speed framing is incomplete" argument) resolves as two
  complementary anti-speed-only arguments from different vocabularies, not
  opposing positions.
