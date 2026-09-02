---
source_url: https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/
source_type: blog-post
title: "Just a rumour of a bug is enough to find a security exploit these days"
author: Simon Willison (link-post), quoting/summarizing Anil Madhavapeddy and Nick Craig-Wood
date_published: 2026-08-28
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: emerging
issue: "#3155"
---

# Just a rumour of a bug is enough to find a security exploit these days

> Willison's link-post pointing to Anil Madhavapeddy's (Cambridge professor,
> OCaml core maintainer) first-person account of a cohttp security patch that
> drew automated exploit probes within ten minutes of the fix PR going public,
> plus a Hacker News comment from rclone's maintainer documenting a 20x jump
> in monthly security disclosures. Together they argue that traditional OSS
> security embargoes no longer buy meaningful time once an AI agent only
> needs "a rumour" of a bug to go find the exploit itself.

## Source Context

- **Type**: blog-post. This is a Simon Willison "link blog" post (~250
  words: a framing paragraph, two block-quoted excerpts, and a closing
  editorial note) that points to the primary source — Anil Madhavapeddy's
  long-form post "Just a rumour of a bug is enough to find a security
  exploit these days" at `anil.recoil.org/notes/rumour-is-the-exploit`
  (published 22 August 2026, six days before Willison's link post). Per
  MINER.md §1, this Miner followed that primary source in full — it is the
  substantive basis for most of the claims below — rather than treating
  Willison's excerpt as the complete text. Willison also quotes a Hacker
  News comment from Nick Craig-Wood (rclone's maintainer) that is not
  present in Madhavapeddy's original article; that quote is only available
  via Willison's post, which is the reason `source_url` is the Willison URL
  rather than the primary article's URL.
- **Author credibility**: Anil Madhavapeddy is a professor of computer
  science at Cambridge and a core maintainer of the OCaml compiler and the
  `cohttp` HTTP library — he is describing a security incident on his own
  project, in his own infrastructure, with his own webserver logs as
  evidence. This is first-person practitioner testimony, not secondhand
  reporting. Nick Craig-Wood is rclone's maintainer, commenting on his own
  project's GitHub security-disclosure volume. Simon Willison is a
  designated `trusted-feed` source in this repo; for this post he is a
  curator adding a short framing paragraph, not original analysis. The
  article also cites two arXiv papers by name (Fang et al. 2024 on
  automated one-day exploitation; Pesoli et al. 2026 on "bugonomics") and
  a Vulncheck-sourced chart, giving several of the more general claims
  academic/third-party backing beyond Madhavapeddy's own anecdote.
- **Scope**: Covers one maintainer's real-time experience of a single
  security patch (path-traversal fix in `cohttp` 6.3.0), generalized with
  a handful of cited statistics (Fang et al.'s exploit-rate benchmark,
  Vulncheck's mean-time-to-exploit trend, two other named 2026 CVEs) and
  rclone's disclosure-volume data point. Does NOT cover: any systematic,
  cross-project survey of exploit timelines (the "quick search finds lots
  of other similar cases" claim rests on two named examples, not a
  dataset); the technical internals of Project Glasswing's access-gating
  criteria; or independent verification of the Fang et al./Pesoli et al.
  papers' methodology (this Miner read Madhavapeddy's characterization of
  them, not the papers themselves).

## Extracted Claims

### Claim 1: A path-traversal patch for OCaml's cohttp drew exploit probes matching the exact bug pattern within minutes of the fix PR being opened publicly

- **Evidence**: First-person account from Madhavapeddy's own webserver logs, for a `cohttp` 6.3.0 patch he personally authored and shipped.
- **Confidence**: anecdotal (single incident, self-reported, though the observer is also the codebase owner with direct log access — not a secondhand or reconstructed account)
- **Quote**: "I noticed probes in my live webserver logs with the exact bug pattern just minutes after opening the PR to fix the issue."
- **Our assessment**: This is the anchoring incident for the whole post. "The exact bug pattern" is the load-bearing detail — it distinguishes targeted exploitation of this specific bug class from generic background internet scanning noise, which is a much weaker signal. A single incident from one maintainer doesn't establish a base rate, but it is the kind of first-person, log-backed anecdote that is hard to dismiss as speculation.

### Claim 2: Madhavapeddy's own coding agent found and built a working exploit for the same bug just by being pointed at "roughly what it was about," without seeing the disclosed patch

- **Evidence**: First-person account of the author's own experiment, run in parallel with the public disclosure process.
- **Confidence**: anecdotal (single self-reported experiment, no independent reproduction)
- **Quote**: "I found I could use my own agents to find the exploit just by knowing roughly what it was about and so could have been exploiting it well before the public patch was available!"
- **Our assessment**: This is the concrete demonstration behind the post's title — a rumour, not a patch or a CVE description, was sufficient input. It directly narrows the gap between "an agent given a CVE description can exploit it" (the Fang et al. finding, Claim 4 below) and "an agent given nothing but a vague hint can exploit it," which is a meaningfully lower bar for what counts as a leaked signal that needs protecting.

### Claim 3: Claude Fable refused to help investigate related path-normalization issues in the codebase due to a security block, while DeepSeek V4 Pro complied and independently surfaced several related issues; the same non-frontier-gated agent then built a working exploit against a local live server in under a minute

- **Evidence**: First-person account of the author testing two named models against the same task.
- **Confidence**: anecdotal (single self-reported comparison, two named models, no controlled benchmark)
- **Quote**: "Fable frustratingly refused outright due to its security block since I don't have access to Glasswing, but DeepSeek V4 Pro obliged me and independently turned up several related issues. My agent also trivially created an exploit to probe a local live server in under a minute."
- **Our assessment**: This is a concrete, named-model illustration of a threat-model asymmetry that this corpus has previously only seen argued in the abstract: a frontier model with safety gating (Claude Fable, gated behind Anthropic's Project Glasswing access program) refused, while a less-gated model (DeepSeek V4 Pro) did the task anyway. The defender (Madhavapeddy, an OCaml maintainer) doesn't have Glasswing access and had to fall back to the less-restricted model to audit his own code — meaning the safety gate blocked the defensive use case here, not just a hypothetical offensive one. This directly corroborates Thomas Ptacek's claim in `blog-simonwillison-ptacek-open-weights-pentest.md` (Claim 2: "doesn't think this even needs a frontier model") with a specific named-model data point that source lacked.

### Claim 4: Fang et al.'s benchmark found that a GPT-4 agent exploited 87% of a 15-vulnerability benchmark when given a CVE description, versus just 7% without one

- **Evidence**: Cited academic source — Fang et al. (2024), "LLM Agents can Autonomously Exploit One-day Vulnerabilities," arXiv:2404.08144 — named and linked in the reference list of Madhavapeddy's article.
- **Confidence**: emerging (a specific, named, citable peer-reviewed-adjacent (arXiv) benchmark result; this Miner read Madhavapeddy's characterization of the paper, not the paper itself, so the 87%/7% figures are a secondhand citation of a primary academic source rather than independently verified)
- **Quote**: "Fang et al. found that when given a CVE description, their GPT-4 agent exploited 87% of a 15-vulnerability benchmark, and without the description, just 7%."
- **Our assessment**: This is the clearest quantitative evidence in the article for the "just a rumour is enough" thesis — an 80-point swing in exploit success rate from a text description alone, with no code access beyond what a CVE advisory typically contains. It's also the baseline the rest of the article extrapolates from: if a *description* produces an 87% success rate, the article's argument is that today's agents need even less than that (a rumour, a Slack message, a mailing-list question).

### Claim 5: The mean time to exploit new vulnerabilities is now -7 days (exploitation precedes the patch), down from roughly 63 days in 2018-19, crossing zero in 2024

- **Evidence**: Cited third-party trend data attributed to Vulncheck (referenced via an embedded chart captioned "The state of LLM exploitation in 2026 (source: Vulncheck)").
- **Confidence**: emerging (a specific, named, third-party-sourced statistic; this Miner did not independently fetch Vulncheck's underlying report, so the figure is a secondhand citation, not independently verified against the primary source)
- **Quote**: "Two years on, the mean time to exploit is -7 days. In other words, exploitation now precedes the patch! That same metric looks to be around 63 days in 2018-19, and crossed zero in 2024."
- **Our assessment**: The "-7 days" framing is the single most quotable statistic in the article: it means, on average, working exploits are now already circulating before the fix ships, which inverts the entire premise of a responsible-disclosure embargo (which assumes the patch is the starting gun, not something attackers cross before it fires). The 2018-19 → 2024 → 2026 trend line (63 days → 0 → -7) gives this a trajectory, not just a snapshot, which is useful for guide purposes: it lets readers reason about where the number goes next rather than treating -7 as a plateau.

### Claim 6: Two named 2026 CVEs (marimo's CVE-2026-39987 and Langflow's CVE-2026-33017) went from advisory publication to first exploitation attempt in 9 hours and 20 hours respectively, with marimo's case having no public proof-of-concept in existence at the time of the first attempt

- **Evidence**: Two specific, named CVE identifiers with stated timelines, presented as corroborating examples following the Vulncheck chart.
- **Confidence**: anecdotal (two named data points, not a systematic sample; the underlying source for these specific timelines is not cited beyond "a quick search finds lots of other similar cases")
- **Quote**: "marimo's CVE-2026-39987 went from advisory to first exploitation attempt in 9 hours, even with no public proof-of-concept in existence. Langflow's CVE-2026-33017 took 20 hours."
- **Our assessment**: The marimo case is the more striking of the two because it explicitly rules out the "someone published a working PoC and that's what got copied" explanation — the first attempt came before any public exploit code existed, which is consistent with Claim 4's finding that an agent can go from description to exploit without a PoC to copy from. These are illustrative examples rather than a dataset, so they should be cited as named incidents, not generalized into an average.

### Claim 7: rclone's maintainer reports roughly 20 security disclosures through GitHub across the project's first 10 years, versus over 40 in the most recent single month, with a security-triage hit rate of about 75%

- **Evidence**: Direct Hacker News comment from rclone maintainer Nick Craig-Wood, quoted by Willison (this quote does not appear in Madhavapeddy's original article — it is only in the Willison link post).
- **Confidence**: anecdotal (single maintainer's own count, from a third-party comment thread, not an audited figure — but it is a first-person report from the person doing the triage, with a concrete before/after comparison)
- **Quote**: "In the first 10 years of the rclone project we received about 20 security disclosures through GitHub. We had to deal with over 40 in the last month! That has taken a huge amount of my time, even using AI tools to triage and come up with fixes for review."
- **Quote** (hit rate): "The hit rate for those security disclosures is pretty good - about 75% of them have a nugget of something which needs looking at."
- **Our assessment**: This is the strongest volume-side evidence in the source cluster — a ~2/year baseline exploding to 40+/month is roughly a 240x jump in monthly disclosure rate for one project, and the 75% hit rate rules out the alternative explanation that the flood is mostly noise/false positives that AI made cheap to generate. Note that Craig-Wood explicitly says he is "even using AI tools to triage" the incoming volume — the disclosures are AI-accelerated on the attacker/researcher side, and the maintainer is already using AI defensively just to keep pace, not choosing to.

### Claim 8: GitHub's CVE assignment turnaround grew from 2-3 days to 3-4 weeks, forcing rclone to ship point releases marked "CVE-PENDING"

- **Evidence**: Same Nick Craig-Wood Hacker News comment, quoted by Willison.
- **Confidence**: anecdotal (single maintainer's first-person account of GitHub's CVE assignment process for his project specifically; no GitHub-side confirmation of the aggregate backlog cited in this source)
- **Quote**: "GitHub assigns CVEs for the advisories. Before the AI apocalypse they took 2-3 days for an assignment but now it they are running at 3-4 weeks so I have to send the point releases out with CVE-PENDING in the changelog which isn't ideal."
- **Our assessment**: This is a concrete downstream operational consequence of Claim 7's volume increase: the disclosure pipeline's bottleneck has moved from "finding the bug" to "processing the paperwork," and the visible symptom is maintainers shipping fixes without a CVE identifier attached yet. For a guide audience, this is a useful, verifiable-in-principle claim (rclone's own changelog would show "CVE-PENDING" entries) even though this Miner did not independently check rclone's changelog to confirm it.

### Claim 9: A May 2026 paper coined the term "bugonomics," arguing the bottleneck in AI-accelerated vulnerability discovery has shifted to "defender remediation throughput" — LLMs generate exploits faster than maintainer validation, triage, and release rates improve

- **Evidence**: Cited academic source — Pesoli et al. (2026), "Demystifying the Mythos or Disrupting Bugonomics? From Zero-Day Asymmetry to Defender Remediation Throughput," arXiv:2605.24632 — named, linked, and directly quoted in Madhavapeddy's article.
- **Confidence**: emerging (a named, citable 2026 arXiv paper, directly quoted at length by the article; this Miner read the passage as reproduced in Madhavapeddy's post, not the paper itself)
- **Quote**: "The question is not whether frontier models, open-weight models, or program analysis 'win'. The question is how to orchestrate them so that scarce validation, prioritization, and release capacity goes toward durable fixes rather than mechanical search and report drafting."
- **Our assessment**: This reframes the entire article's evidence (Claims 1-8) into a named economic concept: the constraint isn't how fast AI can find or exploit bugs (that capability is already fast and getting faster per Claim 5), it's how fast humans — or human-supervised systems — can validate, prioritize, and ship a durable fix. This is the same underlying bottleneck that `blog-sourcegraph-tanner-vulnerability-remediation-scale.md` Claim 8 names independently from an enterprise-remediation angle ("the work isn't hard... what doesn't scale is the coordination"), giving the "remediation throughput is the real constraint" thesis two independent namings from different communities (OSS maintainer / academic paper here, enterprise vendor there) in the same month-window of the corpus.

### Claim 10: Security embargoes no longer function as designed because an agent only needs a broad search direction — not the specific bug details — to conduct its own research and reach a working exploit

- **Evidence**: Author's own analysis, stated as the article's central thesis and restated in its "no embargoes" prescriptive section.
- **Confidence**: emerging (a reasoned conclusion drawn directly from the author's own first-hand incident, Claim 4's cited benchmark, and Claim 5's trend data — not itself an independent empirical measurement, but well-grounded in the evidence presented alongside it)
- **Quote**: "Conventional security process involves embargoing the bug, and assumes that secrecy of the details protects users. However, all an agent needs today is a broad direction to search in, and it can do its own research."
- **Our assessment**: This is the article's core normative claim, and it's the one most directly relevant to guide advice: it argues that the specific mechanism embargoes rely on (attackers lack the specific technical details) is broken, because agents can now supply the missing specificity themselves from a vague pointer. The companion claim — "just one person searching for the issue class... is sufficient to alert someone else's agent and let them get exploit code" — extends this to argue that embargo *leakage* now has a much lower bar too: an innocuous mailing-list question or an orphan-branch commit can be enough of a "rumour" to trigger the same effect.

### Claim 11: The author proposes three concrete adaptations for OSS maintainers: (a) better-trusted, web-of-trust-gated private discussion infrastructure instead of relying on secrecy of the patch itself, (b) shipping fixes continuously and publicly rather than embargoing (citing Chrome's twice-weekly security releases and the Linux kernel's 7-14 day fix deferral ceiling), and (c) proactive, protocol-layer "virtual patching" deployable before the full code fix completes review

- **Evidence**: Author's own prescriptive recommendations, each illustrated with a named comparison case (Chrome's release cadence, the Linux kernel's patch-deferral policy, Cloudflare's 2021 Log4shell virtual-patching response).
- **Confidence**: anecdotal (the author's own proposed responses, explicitly framed as still being worked out — "I think we'll need some combination of all three options in the short-term" — not a validated or adopted practice)
- **Quote** (discussion infra): "We don't have robust discussion infrastructure available within OSS as it's spread through various end-to-end encrypted ones (we use Matrix) but also shared infrastructure like Discord or Slack which are extremely leaky. We do need some sort of web-of-trust to distinguish the good guys from the bad in a particular project context."
- **Quote** (continuous shipping): "Bigger projects like Chrome show this is possible via weekly security updates, two releases per week (!), and dynamic patching that swaps background processes for updated binaries without a restart."
- **Quote** (protocol-layer protection): "For example, this cohttp bug fixed today has a simple mitigation: just normalise percent-encoded path separators in the request URL. This rule was implementable the minute the report arrived, and also deployable while the full fix went through review, testing and packaging. Virtual patching is routine on cloud infrastructure these days; Cloudflare deployed managed rules to plug Log4shell back in 2021."
- **Our assessment**: These three proposals are the most guide-actionable content in the source, but they're explicitly framed by the author as unsettled and resource-dependent — he immediately notes that smaller projects like OCaml lack Chrome's single-binary distribution model and lack frontier-model access to build the tooling for (a) or (c). For a guide audience, the honest framing is "an active practitioner's working hypotheses for a genuinely unsolved problem," not "here are the three fixes."

### Claim 12: Access to frontier AI models with security guardrails removed is itself gated and unevenly distributed — Project Glasswing covers 150 organizations across 15 countries including critical infrastructure, cloud, and financial providers, but individual open-source ("mom and pop") maintainers still lack access

- **Evidence**: Author's own account of his access status as an OCaml maintainer, contrasted with the stated scope of Project Glasswing's access program.
- **Confidence**: anecdotal (author's first-person account of his own access status; the "150 organisations across 15 countries" figure is stated without a citation to Project Glasswing's own disclosure of that number)
- **Quote**: "For smaller projects like OCaml, just gaining access to the frontier models is a struggle. The Western models have security guards in place which mean that we can't use the commercially available ones. Project Glasswing has expanded to 150 organisations across 15 countries including critical infrastructure operators, cloud and financial providers, the Linux Foundation, but 'mom and pop' maintainers still don't have access."
- **Our assessment**: This is the sharpest illustration in the article of a defensive capability gap that mirrors Claim 3's offensive one: the maintainers who most need frontier-model-assisted defense (small OSS projects with limited engineering time) are exactly the ones locked out of the gated frontier tooling, while an ungated model (DeepSeek V4 Pro, Claim 3) was available to both the defender in this anecdote and, by the same logic, to any attacker. The author's own closing line — "if anyone from Project Glasswing is listening, team OCaml could use access now" — underscores that this is a live, unresolved access gap from the perspective of a working maintainer, not a hypothetical one.

## Concrete Artifacts

### Timeline of the cohttp incident (Madhavapeddy's own account, `anil.recoil.org/notes/rumour-is-the-exploit`)

```
1. Bug reported privately via a Slack channel (via Jane Street), itself
   found using Claude Fable.
2. Author points his own Claude agent at the affected code to look for
   related issues. Claude Fable refuses (security block, no Glasswing
   access). DeepSeek V4 Pro complies, finds several related issues.
3. Author's agent builds a working exploit against a local live server
   in under a minute.
4. Author opens cohttp#1145 publicly to get more eyes on the fix
   ("This normally takes a few days and a release within a week or two
   is reasonable.")
5. ~10 minutes later: live webserver logs show probes matching the
   exact bug pattern (percent-encoded path traversal sequences).
```

### Vulncheck mean-time-to-exploit trend (as cited in the article, chart captioned "The state of LLM exploitation in 2026")

```
~2018-19:  mean time to exploit ≈ 63 days
2024:      mean time to exploit crosses zero
2026:      mean time to exploit ≈ -7 days (exploitation precedes patch)
```

### rclone security-disclosure volume (Nick Craig-Wood, via Hacker News comment quoted by Willison)

```
First 10 years of rclone:  ~20 security disclosures via GitHub
Most recent single month:  40+ security disclosures
Hit rate (real issue found): ~75%
GitHub CVE assignment turnaround: 2-3 days (before) → 3-4 weeks (now)
Operational consequence: point releases shipped with "CVE-PENDING"
  in the changelog
```

## Cross-References

- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 3
  ("The patch window between publication and working exploit is shrinking
  due to AI-assisted reverse engineering" — quote: "The window between a
  patch being published and an exploit becoming available is shrinking.")
  — that April 2026 claim was graded `emerging` in its own note because
  Anthropic cited "no specific CVE timeline data." This source supplies
  exactly that missing empirical grounding four months later: the
  Vulncheck mean-time-to-exploit trend (Claim 5 here) and two named 2026
  CVE timelines (Claim 6: 9 hours, 20 hours) are concrete timeline data
  points that did not exist in the corpus when that Anthropic claim was
  extracted.
- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 5
  ("Teams should plan for an order-of-magnitude increase in vulnerability
  finding volume") — rclone's jump from ~20 disclosures/decade to 40+/month
  (Claim 7 here) is a concrete practitioner data point far exceeding
  "order of magnitude" for monthly rate, corroborating the direction of
  Anthropic's claim with a specific, named project's real counts rather
  than a projection.
- **Corroborates**: `blog-anthropic-ai-accelerated-offense.md` Claim 2
  ("Sub-frontier publicly available models already find serious
  vulnerabilities that traditional code review missed for extended
  periods") and `blog-simonwillison-ptacek-open-weights-pentest.md`
  Claim 2 ("The specific capability Ptacek describes does not require a
  frontier-tier model") — Claim 3 in this note (DeepSeek V4 Pro succeeding
  where Claude Fable refused) is a named, dated, first-person incident
  supporting both: it shows a non-frontier-gated model performing
  vulnerability-relevant work a gated frontier model declined to do, for
  the person who most needed the defensive capability.
- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md`
  Claim 3 (Mythos Preview's 73% expert-level CTF success rate, "which no
  prior model could complete before April 2025") — Claim 4 in this note
  (Fang et al.'s 87%/7% exploit-rate benchmark) is a different benchmark
  measuring a related capability (exploitation given a description, rather
  than CTF-solving), and both point the same direction: agent-driven
  vulnerability exploitation crossing thresholds that held only a year or
  two earlier.
- **Extends**: `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`
  Claim 8 ("No current remediation process scales to thousands of
  repositories... the work isn't hard; it's the same fix applied hundreds
  of times. What doesn't scale is the coordination") — that source names
  the bottleneck as *cross-repo coordination* at enterprise scale; Claim 9
  in this note (the "bugonomics" / "defender remediation throughput"
  framing from Pesoli et al. 2026) names the same underlying bottleneck —
  human validation/triage/release capacity, not discovery speed — from an
  academic and single-maintainer perspective rather than an enterprise
  cross-repo one. Two independent framings of "the constraint has moved
  from finding bugs to fixing them" arriving in the corpus within the
  same few months.
- **Extends**: `blog-anthropic-ai-accelerated-offense.md` Claim 1 ("Within
  24 months, widely available AI models will chain previously unnoticed
  bugs into working exploits at scale" — published April 2026). This
  source's evidence is about a *different* threat surface — rapid
  weaponization of newly-disclosed/patched (n-day) bugs, not mass discovery
  of previously-unnoticed (zero-day) bugs — so this Miner did not treat it
  as contradicting Anthropic's 24-month timeline claim. But the two claims
  are close enough in framing (both about AI compressing exploit timelines)
  that a reader could conflate them; the guide should keep these as two
  distinct causal threads: (1) zero-day mass discovery timeline (Anthropic,
  24-month projection, not yet realized at scale per that source) and
  (2) n-day exploit weaponization speed (this source, already observed
  in the wild as of August 2026, with a negative mean-time-to-exploit).
- **Novel**:
  - The specific **-7 days mean-time-to-exploit** figure (Claim 5) and its
    2018-19→2024→2026 trajectory is the first mean-time-to-exploit trend
    line in the corpus; prior sources report point-in-time capability
    percentages (CTF success rates, exploitation percentages) rather than
    a timeline metric.
  - The **named model-refusal-vs-compliance incident** (Claim 3: Claude
    Fable refuses, DeepSeek V4 Pro complies, on the *defensive* side of a
    real maintainer's own audit) is new — prior corpus sources
    (`blog-simonwillison-ptacek-open-weights-pentest.md`) argued this
    asymmetry existed but had no named-model incident to point to.
  - **"Bugonomics" and "defender remediation throughput"** as named terms
    (Claim 9) are new to the corpus, sourced to a specific 2026 arXiv
    paper (Pesoli et al.) not previously cited in any source note.
  - The **rclone before/after disclosure-volume comparison with an exact
    hit rate** (Claim 7) is a new, specific, named-project data point; no
    prior corpus source gives both a "before" baseline and an "after"
    count for the same project.
  - The three **maintainer-proposed adaptations** (Claim 11) — web-of-trust
    discussion infrastructure, continuous-shipping-instead-of-embargo, and
    protocol-layer virtual patching — are the first set of concrete,
    OSS-maintainer-authored (rather than vendor- or model-maker-authored)
    proposed responses to AI-accelerated exploitation in the corpus.

## Guide Impact

- **Chapter 06 (Security & Threat Model)**: Add Claim 5 (-7 days mean time
  to exploit, trending from +63 days in 2018-19) as the single sharpest
  timeline statistic for framing why patch-then-disclose embargo practices
  need reconsideration — it should sit alongside, not replace, the existing
  24-month mass-exploitation timeline citation from
  `blog-anthropic-ai-accelerated-offense.md` Claim 1, with the two framed
  as separate threat surfaces (n-day weaponization speed vs. zero-day mass
  discovery) per the Cross-References note above. Claim 10's core argument
  (embargoes assume secrecy protects users, but agents only need a broad
  search direction) is the mechanism-level explanation the guide should
  pair with the timeline statistic — the number alone doesn't explain why
  embargoes specifically are the affected practice.
- **Chapter 06 (Security & Threat Model) — remediation bottleneck framing**:
  Add Claim 9's "bugonomics"/"defender remediation throughput" framing as a
  named concept the guide can use to distinguish two different problems
  practitioners might otherwise conflate: AI making bugs easier to *find*
  (already true, well-covered elsewhere in the corpus) versus AI making
  bugs easier to *fix durably* (not true — human validation/release
  capacity is the flat constraint). Pair with
  `blog-sourcegraph-tanner-vulnerability-remediation-scale.md` Claim 8 as
  the enterprise-scale version of the same argument.
- **Chapter 06 (Security & Threat Model) — model-access asymmetry**: Add
  Claim 3 and Claim 12 together as a concrete case study for a threat-model
  point the guide has previously only argued abstractly (via the Ptacek
  quote): gating frontier models behind programs like Project Glasswing can
  leave the maintainers of widely-depended-on infrastructure (here, OCaml's
  `cohttp`) without access to the same defensive tooling that ungated models
  already provide attackers. This is a specific, dated, named-model
  counter-example to any guide framing that treats frontier-model access
  gating as a settled, sufficient defensive measure.
- **Chapter 02 (Harness Engineering)**: The Claim 3 incident (Claude Fable's
  security-block refusal on a legitimate defensive-audit task, for a
  maintainer without Glasswing access) is a concrete example of a coding
  agent's safety guardrails producing a false negative for a benign use
  case, which is relevant to any guide discussion of how model-level safety
  gating interacts with real engineering workflows — the refusal did not
  stop the work, it just redirected it to a different, less-gated tool.

## Extraction Notes

1. **WebFetch summarization risk avoided for the primary source**: An
   initial WebFetch call against `anil.recoil.org/notes/rumour-is-the-exploit`
   returned a paraphrased summary and explicitly declined to reproduce the
   article verbatim, citing copyright. Per MINER.md §2a, no `Quote` field
   in this note is drawn from that summarized output. Instead, this Miner
   fetched the raw page HTML directly via `curl` (browser user-agent),
   stripped markup with a Python script, and read the full resulting plain
   text (all sections: incident narrative, "bugonomics" discussion, three
   proposed adaptations, references list, and author's closing note). All
   quotes above are copied character-for-character from that verbatim
   extraction. The same direct-`curl` approach was used for the Willison
   link-post page for the rclone/Craig-Wood quotes, which do not appear in
   Madhavapeddy's original article.
2. **Fang et al. and Pesoli et al. papers not independently fetched**: This
   note quotes Madhavapeddy's own characterization and direct quotation of
   both arXiv papers (2404.08144 and 2605.24632 respectively), not the
   papers themselves. Confidence for Claims 4 and 9 is graded `emerging`
   rather than `settled` accordingly.
3. **Vulncheck chart data not independently fetched**: The -7 days /
   63 days / crossed-zero-in-2024 figures (Claim 5) are read off
   Madhavapeddy's prose description of an embedded chart credited to
   Vulncheck; this Miner did not locate or fetch a separate Vulncheck
   report to verify the underlying data. Graded `emerging`.
4. **The two named CVEs in Claim 6 (marimo, Langflow) are presented in the
   source as illustrative examples ("a quick search finds lots of other
   similar cases"), not a systematic sample** — this Miner did not attempt
   to independently verify the 9-hour/20-hour timelines against the
   respective projects' own advisories or a CVE database.
5. **No contradiction filed**: This Miner considered whether Claim 5/6
   (exploitation now routinely precedes or immediately follows patches)
   materially contradicts `blog-anthropic-ai-accelerated-offense.md`
   Claim 1 (24-month timeline to *mass* zero-day exploitation) but
   concluded these describe different threat surfaces — n-day weaponization
   speed vs. zero-day discovery-at-scale — rather than opposing claims
   about the same question, so no contradiction issue was filed. See the
   "Extends" entry above for how the guide should keep these separated.
6. **Cross-reference verification**: Before writing the citations above,
   `blog-anthropic-ai-accelerated-offense.md`,
   `blog-simonwillison-cybersecurity-proof-of-work.md`,
   `blog-simonwillison-ptacek-open-weights-pentest.md`, and
   `blog-sourcegraph-tanner-vulnerability-remediation-scale.md` were
   re-read in full and every cited claim number confirmed against that
   note's own numbered `### Claim N:` headings in document order, per
   MINER.md §4b.
7. **Confidence set to `emerging` overall**: The core incident (Claims 1-3,
   10-12) is a single first-person maintainer account, which alone would
   be `anecdotal`. But it is corroborated by an independent third-party
   account in the same source cluster (Craig-Wood/rclone, Claims 7-8) and
   grounded in two named academic papers (Fang et al., Pesoli et al.) plus
   a named third-party trend dataset (Vulncheck) — none independently
   re-verified by this Miner, but collectively enough named, checkable,
   multi-source backing to place this above `anecdotal` and below
   `settled`.
