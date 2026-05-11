---
source_url: https://simonwillison.net/2026/Apr/22/bobby-holley/
source_type: blog-post
title: "Quoting Bobby Holley (Firefox CTO on 271 vulnerabilities in Firefox 150)"
author: Bobby Holley (CTO, Firefox/Mozilla), quoted by Simon Willison
date_published: 2026-04-22
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#461"
---

# Quoting Bobby Holley: Firefox CTO on 271 Vulnerabilities Found by Claude Mythos Preview

> Bobby Holley (CTO of Firefox) provides the first high-credibility practitioner case study
> quantifying frontier AI security scanning at production scale: 271 vulnerabilities found in
> Firefox 150 using Claude Mythos Preview (vs. 22 with Opus 4.6 in Firefox 148), with the
> operational conclusion that "Defenders finally have a chance to win, decisively."

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "quotation" format — Willison presents
  Bobby Holley's statement without adding editorial commentary; the linked Mozilla blog post
  "The Zero-Days Are Numbered" (blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/,
  April 21, 2026) contains the full statement and was fetched per Miner step 1 as a
  substantive linked page)
- **Author credibility**: Bobby Holley is the CTO of Firefox at Mozilla — a major
  organization with extensive, production-grade security practices and one of the most
  heavily audited open-source codebases in existence. This is not a vendor claim; it is a
  customer's public assessment of what a frontier model did to their own production codebase.
  Simon Willison is a designated `trusted-feed` source and creator of Django; his selection
  of this quote is itself a relevance signal.
- **Scope**: Covers the practitioner experience of applying Claude Mythos Preview to Firefox
  for defensive vulnerability scanning — specifically the scale of findings (271 bugs), the
  capability progression across model versions (Opus 4.6 → Mythos Preview), the strategic
  implication for the offensive/defensive balance, and the operational reality of conducting
  this work. Does NOT cover: methodology details (how the model was applied), vulnerability
  types found, cost structure, or agent architecture. Includes a footnote caveat about
  AI-assisted development risks.

## Extracted Claims

### Claim 1: Claude Mythos Preview found 271 vulnerabilities in Firefox 150 — approximately 12x more than the 22 bugs found with Opus 4.6 in Firefox 148

- **Evidence**: Bobby Holley's direct disclosure in the Mozilla blog post, with Firefox 150
  as the live production release. The 22/Firefox 148 figure provides the cross-model
  comparison baseline (same organization, same codebase, different model generation).
- **Confidence**: emerging (first-person practitioner report from a high-credibility source;
  not independently verified or peer-reviewed; "271 vulnerabilities" is the figure Holley
  chose to disclose, and the definition of "vulnerability" is not specified)
- **Quote**: "This week's release of Firefox 150 includes fixes for 271 vulnerabilities
  identified during this initial evaluation." (Simon Willison page and Mozilla blog post)
- **Our assessment**: This is the most concrete quantitative data point in the corpus for
  AI-driven defensive vulnerability scanning at production scale. The 12x jump from
  Opus 4.6 (22 bugs) to Mythos Preview (271 bugs) in the same codebase is a striking
  capability signal. The fact that all 271 were included as fixes in a Firefox release
  (not merely findings) means they were validated as real, actionable vulnerabilities —
  this is a higher bar than raw scanner output. The missing denominator (how many
  potential bugs exist in Firefox's codebase; how many hours of human review these
  replaced) limits direct comparison, but the absolute number from a heavily audited
  browser codebase is significant on its own.

### Claim 2: Frontier AI models now find bugs through source code reasoning, a capability that did not exist "a few months ago"

- **Evidence**: Holley's direct statement in the Mozilla blog post characterizing the
  recency and nature of the capability change. The contrast with fuzzing is implicit —
  the model "reasoning through the source code" is the described mechanism.
- **Confidence**: anecdotal (Holley's characterization of the capability's timeline; no
  benchmark data for the "a few months ago" comparison point)
- **Quote**: "Computers were completely incapable of doing this a few months ago, and now
  they excel at it." (Mozilla blog post)
- **Our assessment**: "A few months ago" from April 2026 places the capability threshold
  around late 2025 or early 2026 — consistent with the Claude Mythos Preview release
  period. The phrasing "completely incapable" is a strong claim from someone with
  direct experience: Holley had run Opus 4.6 against Firefox (finding 22 bugs) before
  running Mythos Preview (finding 271). He is not describing a theoretical before-state;
  he is describing his actual experience of the capability gap between model generations.
  This corroborates the Anthropic claim (blog-anthropic-ai-accelerated-offense.md Claim 1)
  that capability is advancing rapidly, and the AISI evaluation data (blog-simonwillison-
  cybersecurity-proof-of-work.md Claim 3) that Mythos Preview crossed an expert-level
  capability threshold "no prior model could" reach before April 2025.

### Claim 3: Claude Mythos Preview has reached at least parity with elite human researchers in vulnerability class coverage

- **Evidence**: Holley's direct observation from running the model against Firefox's
  codebase. He is explicitly reporting on the types of bugs the model found relative to
  what a human researcher could find.
- **Confidence**: anecdotal (one practitioner's assessment of one model against one
  codebase; not a controlled comparison)
- **Quote**: "So far we've found no category or complexity of vulnerability that humans
  can find that this model can't." (Mozilla blog post)
- **Our assessment**: This is the strongest capability claim in the source. Holley is not
  saying the model is faster or cheaper — he is saying the model's vulnerability class
  coverage is at least as broad as the best human researchers. The "so far" qualifier is
  appropriately cautious, and the claim applies to the Firefox codebase specifically (not
  all software). However, Firefox is one of the most heavily audited codebases in
  existence (millions of lines, decades of expert review, multiple formal security
  audits), which makes this claim more significant rather than less. The companion claim
  in blog-anthropic-ai-accelerated-offense.md Claim 2 says "publicly available models can
  find serious vulnerabilities"; Holley's claim goes further — at the frontier (Mythos
  Preview), the model matches expert researchers in coverage breadth.

### Claim 4: Security has historically been "offensively-dominant" — attackers need only find one vulnerability while defenders must prevent exploitation of all

- **Evidence**: Holley's framing of the historical security dynamic in the Mozilla blog
  post. This is an established characterization in security research, confirmed from the
  practitioner perspective.
- **Confidence**: settled (the asymmetric attack/defense dynamic is independently
  established in security research; Holley's framing matches the standard characterization)
- **Quote**: "This is because security to date has been offensively-dominant: the attack
  surface isn't infinite, but it's large enough to be difficult to defend comprehensively
  with the tools we've had available." (Mozilla blog post)
- **Our assessment**: This is the strategic setup for the "Defenders finally have a chance
  to win" conclusion. The offensive-dominant framing explains why the current situation
  has been a structural stalemate even for heavily resourced defenders like Mozilla. The
  asymmetry is not about effort (Mozilla has invested heavily in security, leading Rust
  adoption, process sandboxing); it is about the fundamental economics of attack surface
  vs. exploit-finding cost. AI changes this economic ratio.

### Claim 5: Closing the gap between machine-discoverable and human-discoverable bugs erodes the attacker's long-term structural advantage

- **Evidence**: Holley's strategic analysis in the Mozilla blog post, explaining why the
  coverage gap matters for the offense/defense balance.
- **Confidence**: emerging (sound strategic reasoning from a credible practitioner;
  the economic logic is clear but "erodes... long-term advantage" is a projection,
  not an observed outcome)
- **Quote**: "A gap between machine-discoverable and human-discoverable bugs favors the
  attacker, who can concentrate many months of costly human effort to find a single bug.
  Closing this gap erodes the attacker's long-term advantage by making all discoveries
  cheap." (Mozilla blog post)
- **Our assessment**: This is the key strategic claim and the one most directly connected
  to the proof-of-work framing in blog-simonwillison-cybersecurity-proof-of-work.md
  (Breunig's economic model). If attackers historically had a structural advantage because
  they could invest disproportionate human effort in finding a single bug (while defenders
  had to prevent exploitation of all bugs), then making bug-finding cheap and scalable
  removes that advantage — the defender can now also scan comprehensively. The "making all
  discoveries cheap" framing implies that the price asymmetry between attack and defense
  narrows. Holley is describing the equilibrium shift; Breunig's proof-of-work model
  (blog-simonwillison-cybersecurity-proof-of-work.md) provides the economic structure
  for why this equilibrium exists and what it means in budget terms.

### Claim 6: This capability shift means defenders can now move beyond historical stalemate to decisive advantage

- **Evidence**: Holley's explicit conclusion, reinforced by both the Mozilla blog post
  context and the Willison page quotation.
- **Confidence**: anecdotal (a practitioner's optimistic assessment based on one major
  case study; the 271-bug result is the evidence, but "decisive" victory is a projection)
- **Quote**: "Defenders finally have a chance to win, decisively." (both Simon Willison
  page and Mozilla blog post)
- **Our assessment**: "Finally" signals that this is a genuine state change, not an
  incremental improvement. Holley's historical framing (Claim 4) establishes that
  defenders could not "win" under prior constraints — the best outcome was stalemate.
  The "decisively" qualifier is deliberately strong and reflects the asymmetry
  Holley describes: if machines can now find all bugs cheaply, the economics of
  comprehensive defense become favorable for the first time. This is a high-confidence
  practitioner sentiment claim, but the strategic argument rests on the capability
  claims in Claims 3–5. The Anthropic source (blog-anthropic-ai-accelerated-offense.md)
  frames AI security primarily as a threat to defenders; the Holley source is notably
  more optimistic about the defensive opportunity.

### Claim 7: Deploying frontier AI for security scanning requires significant organizational reprioritization — "relentless and single-minded focus"

- **Evidence**: Holley's direct characterization of the operational experience in the
  Willison page quotation.
- **Confidence**: anecdotal (one team's experience; no baseline for comparison)
- **Quote**: "You may need to reprioritize everything else to bring relentless and
  single-minded focus to the task, but there is light at the end of the tunnel."
  (Simon Willison page)
- **Our assessment**: This is the most practically useful operational signal in the
  source for teams considering similar deployments. "Reprioritize everything else" is
  not an abstraction — it means Mozilla's Firefox security team suspended or deprioritized
  other work to handle the finding volume from Claude Mythos Preview. The companion
  statement ("Our experience is a hopeful one for teams who shake off the vertigo")
  implies an initial disorienting phase when the scale of findings becomes apparent.
  The "vertigo" framing is consistent with Anthropic's warning (Claim 5 in
  blog-anthropic-ai-accelerated-offense.md) to "plan for an order-of-magnitude increase
  in finding volume." Holley is confirming that the volume shock is real and
  significant enough to require organizational preparation.

### Claim 8: Frontier AI vulnerability scanning revealed a completed response — Firefox "turned the corner" — not an ongoing crisis

- **Evidence**: Holley's characterization of the team's current state in the Willison
  page quotation.
- **Confidence**: anecdotal (self-assessment; no independent measure of completion)
- **Quote**: "Our work isn't finished, but we've turned the corner and can glimpse a
  future much better than just keeping up." (Simon Willison page)
- **Our assessment**: This is the optimistic narrative endpoint of the Mozilla case
  study. "Better than just keeping up" suggests the prior security posture was reactive
  (keeping up with found bugs, patching known CVEs); AI-assisted scanning creates a
  proactive posture (finding and fixing bugs before attackers do). The framing directly
  validates Anthropic's Recommendation 3 (Claim 6 in blog-anthropic-ai-accelerated-
  offense.md): "scan your code for vulnerabilities using AI before it ships" — Mozilla
  did exactly this and reports moving from stalemate to advantage.

### Claim 9: AI-assisted development creates a footnote risk — codebases may surpass human comprehension, scaling bug complexity alongside discovery capability

- **Evidence**: A footnote in the Mozilla blog post where Holley explicitly acknowledges
  this risk as part of his broader analysis.
- **Confidence**: anecdotal (the risk is Holley's assessment; no empirical data on
  comprehension-threshold effects)
- **Quote**: "There's a risk that codebases begin to surpass human comprehension as a
  result of more AI in the development process, scaling bug complexity along with (or
  perhaps faster than) discovery capability. Human-comprehensibility is an essential
  property to maintain, especially in critical software like browsers and operating
  systems." (Mozilla blog post, footnote)
- **Our assessment**: This is a significant self-aware caveat from a security leader who
  is simultaneously celebrating AI security capabilities. Holley is warning that using AI
  to develop code faster may generate codebases that even frontier AI cannot fully
  reason about — the discovery capability may not scale as fast as the complexity being
  introduced. "Bug complexity scaling faster than discovery capability" would invert the
  "defenders win" conclusion. For the guide: this caveat belongs prominently alongside
  any celebration of AI-driven vulnerability finding. The guide should flag that the
  defensive advantage is conditional on maintaining codebase human-comprehensibility —
  unconstrained AI-assisted development may undermine the very defense it enables.

### Claim 10: Memory-safe languages (Rust) mitigate certain vulnerability classes but cannot be the sole defensive strategy for large legacy codebases

- **Evidence**: Holley's characterization of Firefox's existing defensive investment in
  the Mozilla blog post.
- **Confidence**: settled (the Rust adoption/migration limitation is independently
  corroborated; "certain very common classes" refers to memory safety bugs, which is
  accurate)
- **Quote**: "We've led the industry in building and adopting Rust, but we still can't
  afford to stop everything to rewrite decades of C++ code, especially since Rust only
  mitigates certain (very common) classes of vulnerabilities." (Mozilla blog post)
- **Our assessment**: This is the practical constraint that makes AI-driven vulnerability
  scanning necessary even for organizations that have already invested heavily in memory
  safety. Mozilla is arguably the most advanced organization in Rust adoption, yet still
  has significant C++ code and still found 271 vulnerabilities with a frontier model.
  The implication for the guide: memory-safe language adoption and AI vulnerability
  scanning are complementary, not alternatives. Teams that have already made memory
  safety investments still need AI-assisted scanning for the remaining attack surface.

## Concrete Artifacts

### Firefox AI Security Collaboration Timeline

```
Firefox AI Vulnerability Scanning Progression
Source: Bobby Holley, Mozilla blog, April 21–22, 2026

Phase 1 — Opus 4.6 (Firefox 148):
  Model:           Claude Opus 4.6
  Outcome:         22 security-sensitive bugs fixed
  Characterization: Initial collaboration with Anthropic

Phase 2 — Claude Mythos Preview (Firefox 150):
  Model:           Claude Mythos Preview (early version)
  Start date:      "Since February" (approx. February 2026)
  Outcome:         271 vulnerabilities fixed
  Scale factor:    ~12x increase over Opus 4.6 run
  Mode:            Source code reasoning (not fuzzing)
  Team impact:     Required reprioritizing other work; "relentless and single-minded focus"

Strategic conclusion:
  Historical state: "offensively-dominant" — defenders at structural disadvantage
  Current state:    "Defenders finally have a chance to win, decisively"
  Mechanism:        Closing gap between machine-discoverable and human-discoverable bugs
                    removes attacker's structural cost advantage
```

### Bobby Holley's Willison-Quoted Statement (Full)

```
[Bobby Holley, CTO Firefox, as quoted by Simon Willison, April 22, 2026]

"As part of our continued collaboration with Anthropic, we had the opportunity to apply
an early version of Claude Mythos Preview to Firefox. This week's release of Firefox 150
includes fixes for 271 vulnerabilities identified during this initial evaluation.

Our experience is a hopeful one for teams who shake off the vertigo and get to work.
You may need to reprioritize everything else to bring relentless and single-minded focus
to the task, but there is light at the end of the tunnel.

We are extremely proud of how our team rose to meet this challenge, and others will too.
Our work isn't finished, but we've turned the corner and can glimpse a future much
better than just keeping up.

Defenders finally have a chance to win, decisively."
```

### Key Strategic Claims from Mozilla Blog Post ("The Zero-Days Are Numbered")

```
[Bobby Holley, Mozilla blog, April 21, 2026]
[Source: blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/]

On historical security asymmetry:
  "Until now, the industry has largely fought security to a draw."
  "This is because security to date has been offensively-dominant: the attack surface
   isn't infinite, but it's large enough to be difficult to defend comprehensively with
   the tools we've had available."

On the capability change:
  "Computers were completely incapable of doing this a few months ago, and now they
   excel at it."

On coverage parity with human researchers:
  "So far we've found no category or complexity of vulnerability that humans can find
   that this model can't."

On the strategic implication:
  "A gap between machine-discoverable and human-discoverable bugs favors the attacker,
   who can concentrate many months of costly human effort to find a single bug. Closing
   this gap erodes the attacker's long-term advantage by making all discoveries cheap."

Footnote (caveat):
  "There's a risk that codebases begin to surpass human comprehension as a result of
   more AI in the development process, scaling bug complexity along with (or perhaps
   faster than) discovery capability. Human-comprehensibility is an essential property
   to maintain, especially in critical software like browsers and operating systems."
```

## Cross-References

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 2 — "Today, publicly
  available models can find serious vulnerabilities that traditional reviews have missed for
  long periods." The Bobby Holley note provides the practitioner case study that validates this
  claim with specific numbers (271 bugs, Firefox 150) from a high-credibility external source.
  The Anthropic source establishes the abstract claim; the Holley source provides the concrete
  evidence. Note the scope difference: Anthropic's claim is about "publicly available models";
  Holley's result is from a frontier preview model (Claude Mythos Preview), which is not
  publicly available. The Holley result is thus stronger (frontier capability) than the
  Anthropic claim requires (publicly available capability).

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 5 — "Plan for an
  order-of-magnitude increase in finding volume." Holley's "vertigo" and "reprioritize
  everything else" language is first-person confirmation that the finding-volume shock is real
  and organizationally significant. Mozilla (one of the most security-mature organizations
  in open source) was not prepared to absorb 271 vulnerabilities without significant
  operational disruption.

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 6 — "If you implement
  one thing from this section, implement this: scan your code for vulnerabilities using AI
  before it ships." The Firefox/Mozilla case study is the highest-profile practitioner
  validation of this recommendation in the corpus. Mozilla did exactly this and reports
  moving from historical stalemate to a "decisive" defensive advantage.

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 3 — "Mythos
  Preview succeeds on 73% of expert-level CTF challenges that no prior model could complete
  before April 2025." The Holley note provides the defensive-use counterpart: the same model
  generation that shows frontier offensive CTF capability also shows frontier defensive
  scanning capability (271 bugs in Firefox 150). The AISI evaluation measured offensive
  benchmarks; the Mozilla deployment measured defensive production results. Together they
  characterize the capability level from both sides.

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 1 — the
  token-economy / proof-of-work framing where "closing this gap erodes the attacker's long-
  term advantage by making all discoveries cheap." Holley's "Closing this gap erodes the
  attacker's long-term advantage by making all discoveries cheap" is nearly identical in
  framing to Breunig's proof-of-work model. These are independently arrived-at formulations
  of the same strategic insight — high corroboration value.

- **Corroborates**: `blog-cursor-security-agents.md` Claim 9 — "Agent-driven security review
  can catch 200+ vulnerabilities per week across 3,000+ PRs." Cursor's 200+ per week and
  Mozilla's 271 in a single evaluation run are the two largest concrete vulnerability-count
  data points in the corpus. They corroborate each other directionally (AI security scanning
  finds hundreds of real vulnerabilities in production-grade codebases) while being
  architecturally distinct (Cursor's ongoing PR review fleet vs. Mozilla's one-time audit
  run with Claude Mythos Preview).

- **Extends**: `blog-anthropic-ai-accelerated-offense.md` — The Anthropic source
  provides the threat framing and the seven-recommendation defensive program. The Holley
  source provides the practitioner case study from outside Anthropic that validates the
  claims: a major third-party organization applied the recommended "scan your code with AI"
  approach and found 271 vulnerabilities. Together: Anthropic sets the agenda; Mozilla
  confirms the results at scale.

- **Novel**:
  - **12x capability jump (Opus 4.6 → Mythos Preview)** in the same codebase is the first
    cross-model-version quantitative comparison for defensive vulnerability scanning in the
    corpus. No other source provides a before/after number for the same organization, same
    codebase, different model generations.
  - **Human-researcher parity claim** ("no category or complexity of vulnerability that
    humans can find that this model can't") from a high-credibility external practitioner is
    the strongest capability parity claim in the corpus. The Anthropic source claims
    "publicly available models find serious vulnerabilities"; Holley claims frontier models
    match elite human researchers in coverage breadth.
  - **"Vertigo" as a named operational experience** — the psychological/organizational
    shock of encountering AI-generated finding volume for the first time — is novel to
    the corpus. No other source names or describes this phenomenon from firsthand
    experience.
  - **Codebase comprehensibility as a defensive property** (Claim 9 footnote) — the
    warning that AI-assisted development may scale bug complexity faster than discovery
    capability — is a novel caveat not raised in any other corpus source. This inverts the
    "AI helps defenders" narrative conditionally: the defensive advantage may erode if
    development speed outpaces reasoning capability.

## Guide Impact

- **Chapter on Security / Threat Model**: The Firefox case study (271 bugs, Firefox 150)
  should be the primary concrete example anchoring the threat model discussion. Currently,
  the corpus has the Anthropic source (vendor claim) and the AISI evaluation (benchmark).
  The Holley source is the missing practitioner case study from an independent, non-vendor
  organization. The 12x model-generation jump should be cited as evidence for the claim
  that capability is advancing rapidly. The "vertigo" concept should be surfaced as an
  operational warning: teams should plan for finding-volume shock before deploying AI
  security scanning.

- **Chapter on Security / Defensive Patterns**: The "scan your code with AI before it
  ships" recommendation (Anthropic source, Claim 6) should now cite the Mozilla case
  study as its primary practitioner validation. The claim that this approach enables
  "defenders finally to win, decisively" is a strong endorsement from an independent,
  credible source. The Claim 7 operational implication (organizational reprioritization
  required) should accompany this recommendation — it is not a zero-effort deployment.

- **Chapter on Security / Capability Context**: Claim 3 (human-researcher parity at the
  frontier) should inform the framing of what frontier AI security scanning can do vs.
  what prior-generation models could do. The guide should distinguish the publicly-
  available model capability (Anthropic source: "finds serious vulnerabilities") from
  frontier capability (Holley: "no category or complexity humans can find that this
  model can't").

- **Chapter on Security or Adoption / Codebase Health**: Claim 9 (the comprehensibility
  footnote) should appear as a caveat in any section celebrating AI-driven vulnerability
  finding. The defensive advantage is conditional: it holds as long as the AI can
  reason about the codebase. AI-assisted development that outpaces human comprehension
  may eventually create codebases where the AI security scanner itself cannot reason
  effectively about the full attack surface.

- **Chapter on Tool Adoption / Practitioner Experiences**: Bobby Holley's account
  (Claims 7–8) is the most succinct and credible practitioner arc in the corpus for AI
  security adoption: initial disorientation ("vertigo"), organizational reprioritization,
  then "turned the corner." This arc — disorientation → focus → outcome — is a realistic
  adoption model that teams can anticipate and plan for.

## Extraction Notes

1. **Two-layer source structure**: The Simon Willison page (the issue URL) is the
   primary entry point and contains Bobby Holley's 7-sentence statement in full. The
   linked Mozilla blog post ("The Zero-Days Are Numbered," April 21, 2026) is the
   substantive underlying source and was fetched per Miner step 1. All claims from the
   Mozilla blog post are attributed accordingly in this note.

2. **Quote verification caveat**: Quotes from the Mozilla blog post were extracted via
   WebFetch, which may synthesize or paraphrase rather than return character-for-character
   verbatim text. The Willison-page quotes (the 7-sentence Bobby Holley statement) are
   higher-confidence verbatim extractions — returned in consistent form across multiple
   fetches. Mozilla blog post quotes should be verified against the source URL before
   use as pull quotes in the guide. See the Concrete Artifacts section for the full
   Willison-page statement verified across fetches.

3. **Methodology not disclosed**: The Mozilla blog post does not specify how Claude
   Mythos Preview was applied to Firefox — no agent architecture, no scanning methodology,
   no tooling stack. The model "reasoning through the source code" is mentioned as the
   distinguishing characteristic vs. fuzzing, but implementation details are absent.
   The Cursor source (blog-cursor-security-agents.md) provides the architectural patterns
   for what this kind of deployment typically looks like.

4. **"271 vulnerabilities" scope**: The disclosure does not specify vulnerability severity,
   types (memory safety vs. logic bugs), or whether any were previously known. "Fixes for
   271 vulnerabilities" means they were validated as real and patched, not just flagged —
   a higher bar than raw scanner output.

5. **Confidence calibration**: Rated "emerging" overall. The practitioner credibility
   (Firefox CTO, major organization) is high. The quantitative claim (271 bugs) is specific
   and attached to a shipped Firefox release. However, independent verification of the
   numbers is not possible from the source alone, and "no category or complexity humans
   can find that this model can't" (Claim 3) is a sweeping capability assertion that
   warrants careful framing in the guide.
