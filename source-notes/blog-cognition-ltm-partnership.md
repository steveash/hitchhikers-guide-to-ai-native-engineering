---
source_url: https://cognition.com/blog/ltm-cognition-partnership
source_type: blog-post
title: "LTM Partners with Cognition To Reduce Cyber Risk in Financial Services"
author: The Cognition Team
date_published: 2026-07-28
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: anecdotal
issue: "#2429"
---

# LTM Partners with Cognition To Reduce Cyber Risk in Financial Services

> A Cognition partnership-announcement post: LTM (a systems integrator with
> 260+ clients including 26 Fortune 500 companies and the top 5 global banks)
> is deploying Devin Security Swarm inside BlueVerse RightLogic, a managed,
> outcome-based vulnerability-remediation service targeting an 80% CVE
> backlog clearance rate (up from 60%) and "30% lower cost" per verified
> vulnerability than the nearest alternative — the first Cognition
> SI-partnership post in this corpus to name a security/compliance vertical
> rather than engineering-productivity/legacy-migration, and the first to
> quote named individuals from both companies rather than being entirely
> unattributed corporate narration.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-07-28; a partnership/announcement post, not a technical article or
  first-person practitioner account).
- **Author credibility**: Byline is "By The Cognition Team" — the same
  unattributed-byline convention as `blog-cognition-infosys-partnership.md`
  and `blog-cognition-cognizant-partnership.md`. Unlike those two posts,
  however, this one *does* quote two named individuals mid-body: Gardner
  Johnson (VP Global Partnerships, Cognition) and Harsh Naidu (Chief
  Business Officer – Banking & Financial Services, LTM). This breaks the
  "zero named spokesperson on either side" pattern both prior partnership
  notes flagged as notable by omission.
- **Scope**: Covers the fact and shape of the partnership: the product
  being deployed (Devin Security Swarm only — no other Devin capability or
  Windsurf is mentioned), the specific managed service it powers
  (BlueVerse RightLogic), LTM's client scale (260+ clients, 26 Fortune 500,
  top 5 global banks), the three operating pillars of RightLogic, two
  quantified metrics (30% lower cost per verified vulnerability; 80% vs.
  60% CVE backlog clearance), the initial target vertical (banking,
  financial services, insurance) and planned expansion (application
  modernization, SDLC transformation, "and more" across "additional
  industries"), and two named-individual quotes. Does NOT cover: how many
  of LTM's 260+ clients are currently live on RightLogic (vs. planned), any
  named client deployment or case study, the "five joint offerings"
  contents beyond RightLogic itself, how the 30%-lower-cost and 60%/80%
  figures were measured or against what baseline/sample, any discussion of
  challenges or failure modes, or technical detail on how Devin Security
  Swarm's runtime-exploitability validation actually works.

## Extracted Claims

### Claim 1: LTM has partnered with Cognition to deploy Devin across its global client base and cybersecurity practice, which serves over 260 clients including 26 of the Fortune 500 and the top 5 global banks
- **Evidence**: Opening sentence of the announcement, giving three distinct scale figures (260+ clients, 26 Fortune 500, top 5 global banks) rather than a qualitative superlative.
- **Confidence**: anecdotal (single unattributed corporate announcement; the figures describe LTM's existing client base generally, not how many of those clients are actually using Devin or RightLogic)
- **Quote**: "LTM has partnered with Cognition to deploy Devin, the AI software engineer, across its global client base and cybersecurity practice serving over 260 clients, including 26 of the Fortune 500 and the top 5 global banks."
- **Our assessment**: This is more specific than the scale language in the corpus's other two Cognition SI-partnership posts — `blog-cognition-infosys-partnership.md` Claim 1 uses an unquantified superlative ("one of the largest global deployments... to date") and `blog-cognition-cognizant-partnership.md` Claim 1 uses vague scope language ("many of the world's largest companies") — but the figures still describe LTM's *existing client roster*, not a measured count of clients actually running Devin/RightLogic today. Should be cited as LTM's addressable client base, not as adoption evidence.

### Claim 2: The partnership brings Devin into BlueVerse RightLogic, a managed, outcome-based service that clears a customer's vulnerability backlog by pairing Devin's autonomous engineering capacity with LTM's enterprise-grade security practice, and is the first of five joint offerings the two companies are bringing to market together
- **Evidence**: Second paragraph, naming the specific product (RightLogic), its parent ecosystem (LTM BlueVerse), its operating model ("managed, outcome-based"), and its position within a larger five-offering roadmap.
- **Confidence**: anecdotal (stated product scope and roadmap; no description of what the other four joint offerings are or when they will ship)
- **Quote**: "The partnership brings Devin into BlueVerse RightLogic, a managed, outcome-based service that clears a customer's vulnerability backlog by pairing Devin's autonomous engineering capacity with LTM's enterprise-grade security practice and delivery expertise. RightLogic is an extension of LTM BlueVerse, LTM's AI-native ecosystem that embeds intelligent agents directly into core business processes, and is the first of five joint offerings the two companies are bringing to market together."
- **Our assessment**: "Outcome-based" (as opposed to a seat-license or hourly-services model) is a specific commercial framing not previously named in this corpus's SI-partnership material — it implies LTM is pricing RightLogic against a measurable result (backlog clearance) rather than against Devin usage or engineer hours, which is a different commercial shape than the internal-productivity/services-delivery/MSP taxonomy documented in `blog-cognition-infosys-partnership.md` Claim 4.

### Claim 3: AI-powered cyberattacks have tripled while security teams face 10-100x more security findings than before, with a large share being false positives, and existing tools "stop at detection," missing chained exploits that require deep reasoning about business logic and leaving validation/remediation to humans
- **Evidence**: Third paragraph's problem-framing statement, preceding the Devin Security Swarm pitch; gives two specific multipliers (tripled attacks, 10-100x findings) rather than a purely qualitative claim.
- **Confidence**: anecdotal (unsourced vendor statistics — no citation, dataset, or methodology given for either the "tripled" attack-volume figure or the "10-100x" findings-volume figure; no named benchmark or third-party study referenced)
- **Quote**: "As AI accelerates code production, AI-powered cyberattacks have tripled — swarms of low-cost attacks now probe every possible vulnerability, leaving enterprises of all sizes exposed. Meanwhile, security teams are drowning: many face 10–100x more security findings, with a large share being false positives. The tools most enterprises rely on offer coverage but stop at detection: they miss the chained exploits that require deep reasoning about business logic, and leave validation and remediation up to humans."
- **Our assessment**: This is the same "traditional tooling cannot keep up" diagnostic framing documented in `blog-cognition-devin-federal-security-swarm.md` Claim 4 and `blog-cognition-doe-genesis-mission.md` Claim 7, restated here with two specific (but unsourced) multipliers. Should be treated as restated sales framing, not new supporting data, consistent with how those two notes assess the same underlying rhetorical pattern.

### Claim 4: Cognition built Devin Security Swarm to give security teams the engineering capabilities to ship fixes themselves, and major enterprises are already using it to detect critical vulnerabilities, validate their exploitability at runtime, and ship remediation PRs — finding more verified vulnerabilities at 30% lower cost than the nearest comparable alternative
- **Evidence**: Direct capability and outcome claim, immediately following the problem framing in Claim 3; the only quantified cost/outcome metric in the post.
- **Confidence**: anecdotal (vendor's own comparative cost claim, restated without attribution from Cognition's earlier product post; "nearest comparable alternative" is unnamed *in this post*, though the linked source post names it — see assessment)
- **Quote**: "At Cognition, we built Devin Security Swarm in order to give security teams the engineering capabilities to ship fixes themselves. Major enterprises are already using Devin Security Swarm to detect critical vulnerabilities across the codebase, validate their exploitability at runtime, and ship remediation PRs, finding more verified vulnerabilities at 30% lower cost than the nearest comparable alternative."
- **Our assessment**: The three-step mechanism described here (detect vulnerabilities → validate exploitability at runtime → ship remediation PRs) matches the same three-stage architecture documented independently in `blog-cognition-devin-federal-security-swarm.md` Claim 1 ("tracing data flows, validating what's actually exploitable at runtime, and shipping reviewed remediation PRs") and `blog-cognition-doe-genesis-mission.md` Claim 8 ("find vulnerabilities... verify whether they're actually exploitable in a safe sandbox, and open remediation pull requests") — a third independent Cognition post converging on the identical detect/verify/remediate shape, which strengthens confidence that this is Cognition's settled product description rather than a one-off framing (though, per those notes, still not independently benchmarked by any of the three posts). On the "30% lower cost" figure: the phrase "Devin Security Swarm" in this sentence is an inline hyperlink to Cognition's own earlier product post, `/blog/introducing-devin-security-swarm` (published 07.01.26, four weeks before this one), which was fetched during this extraction. That post is the origin of the figure — it states, in near-identical wording, "Security Swarm finds more verified vulnerabilities at 30% lower cost than the nearest comparable alternative," and publishes the benchmark behind it (see Concrete Artifacts → Linked sub-page). The two figures therefore *do* reconcile: on Cognition's 50-vulnerability GHSA benchmark, Devin Security scores 72% recall at $90.23/run against Claude Security's 68% at $131.87/run — the "nearest comparable alternative" by recall — which is 31.6% lower cost at higher recall, i.e. exactly the "more verified vulnerabilities at 30% lower cost" claim restated here without its baseline. This also identifies the benchmark flagged as unmined in `blog-cognition-doe-genesis-mission.md`'s Extraction Notes as the *same* measurement underlying this post's cost claim, not a separate unreconciled metric. Two caveats survive the reconciliation: the benchmark is Cognition's own, run by Cognition on a benchmark of Cognition's construction with no third-party audit, and this post drops both the baseline competitor and the benchmark's existence, so a reader of the LTM post alone cannot tell what "nearest comparable alternative" means.

### Claim 5: RightLogic's "Managed remediation" pillar ingests findings from the scanners enterprises already run, prioritizes them against business criticality and regulatory exposure, and routes high-confidence fixes to Devin for end-to-end remediation while LTM engineers handle complex tasks requiring human judgment — with every fix reviewed by a person before it merges
- **Evidence**: First of three named operating pillars, each given its own bolded sub-heading in the post body.
- **Confidence**: anecdotal (stated operating process; no data on what share of findings are "high-confidence" vs. routed to human LTM engineers, or what the human-review turnaround looks like)
- **Quote**: "Managed remediation: RightLogic ingests findings from the scanners enterprises already run, prioritizes them against business criticality and regulatory exposure, and routes high-confidence fixes to Devin for end-to-end remediation while LTM engineers handle the complex tasks that need human judgment. Every fix is reviewed by a person before it merges."
- **Our assessment**: The explicit human-review-before-merge guarantee is a concrete governance detail not present in the corpus's other two SI-partnership posts (Infosys, Cognizant), which describe deployment models but no merge-gating policy. This is a specific, checkable operational claim (every fix reviewed by a person) that meaningfully bounds Devin's autonomy in this deployment — it is not "Devin merges fixes autonomously," but "Devin proposes fixes that a human gates."

### Claim 6: RightLogic's "Enterprise Scale and Governance" pillar combines Devin's capacity to work across tens of thousands of findings with LTM's existing remediation playbooks, compliance rules, and coding standards, delivered by engineers already trained on Devin — and is designed to clear 80 percent of an enterprise's CVE backlog, up from the 60 percent previously delivered, a figure jointly backed by LTM and Cognition
- **Evidence**: Second named pillar, giving both a specific scale figure (tens of thousands of findings) and a specific before/after outcome figure (60% → 80% CVE backlog clearance).
- **Confidence**: anecdotal (a joint LTM/Cognition-backed target figure, not an independently measured or audited outcome; no baseline period, client sample, or CVE severity mix is disclosed for either the 60% "previously delivered" figure or the 80% target)
- **Quote**: "Devin supplies the autonomous capacity to work across tens of thousands of findings while LTM applies the remediation playbooks, compliance rules, coding standards, and regulated-industry expertise it already runs, delivered by engineers trained on Devin and productive from day one. RightLogic is designed to clear 80 percent of an enterprise's CVE backlog, up from the 60 percent previously delivered, an improvement jointly backed by LTM and Cognition."
- **Our assessment**: This is the most specific quantified outcome claim in the post — a named before/after percentage pair — and is meaningfully more concrete than the qualitative "material productivity gains" language in `blog-cognition-infosys-partnership.md` Claim 3 or the entirely unquantified `blog-cognition-cognizant-partnership.md`. However, "the 60 percent previously delivered" is ambiguous as written: it is not clear whether this refers to LTM's pre-Devin CVE clearance rate, an industry baseline, or some other reference point, and no source citation is given for either number. Should be cited as a stated joint target, not a verified measured outcome.

### Claim 7: RightLogic's "Continuous improvement at scale" pillar states that every engagement sharpens LTM's remediation playbooks by encoding each customer's compliance rules and coding standards, so that remediation runs faster and more autonomously over time
- **Evidence**: Third named pillar, describing a claimed compounding/learning effect across engagements.
- **Confidence**: anecdotal (stated mechanism with no evidence of a measured improvement curve across engagements — no before/after comparison across multiple named clients)
- **Quote**: "Continuous improvement at scale: Every engagement sharpens LTM's remediation playbooks, encoding each customer's compliance rules and coding standards so remediation runs faster and more autonomously over time."
- **Our assessment**: This is a claimed compounding-returns mechanism (each new client engagement improves the playbook for the next) rather than a per-client one, distinct from within-organization "continuous improvement" claims elsewhere in the corpus — but as with Claim 6, no data is given to substantiate that the playbooks actually do improve measurably over time, only that this is the intended mechanism.

### Claim 8: Gardner Johnson, VP Global Partnerships at Cognition, is quoted directly: "Security has become a volume problem that no human team can staff its way out of. Devin lets security teams move from reporting issues to resolving them, and LTM brings the expertise and customer relationships to deliver that outcome at enterprise scale."
- **Evidence**: A named, titled individual quote attributed to Cognition — the first such attribution in this corpus's Cognition SI-partnership-post cluster.
- **Confidence**: anecdotal (a single named spokesperson's characterization of the partnership's value proposition, not an independently measured claim)
- **Quote**: "Security has become a volume problem that no human team can staff its way out of. Devin lets security teams move from reporting issues to resolving them, and LTM brings the expertise and customer relationships to deliver that outcome at enterprise scale."
- **Our assessment**: Both `blog-cognition-infosys-partnership.md` Claim 6 and `blog-cognition-cognizant-partnership.md` Claim 6 explicitly flagged, as a notable omission, that neither prior SI-partnership post quotes any named individual from either company — "every sentence is unattributed corporate narration." This post breaks that pattern with two named, titled quotes (this one and Claim 9). That is itself a structural observation worth recording: Cognition's SI-partnership template is not fixed, and at least one later post in the series (this one, 2026-07-28, six-plus months after the Infosys and Cognizant posts) adds named-spokesperson attribution the earlier two lacked.

### Claim 9: Harsh Naidu, Chief Business Officer – Banking & Financial Services at LTM, is quoted directly: "The Financial Services sector is under constant pressure to strengthen security while accelerating AI adoption. Through BlueVerse RightLogic and Devin, we are helping clients reduce vulnerability backlogs, automate remediation, and improve cyber resilience across financial services, empowering them to innovate faster without compromising security."
- **Evidence**: A named, titled individual quote attributed to LTM, paired with Claim 8's Cognition-side quote.
- **Confidence**: anecdotal (a single named spokesperson's characterization; no data or metric beyond what's already stated elsewhere in the post)
- **Quote**: "The Financial Services sector is under constant pressure to strengthen security while accelerating AI adoption. Through BlueVerse RightLogic and Devin, we are helping clients reduce vulnerability backlogs, automate remediation, and improve cyber resilience across financial services, empowering them to innovate faster without compromising security."
- **Our assessment**: Notably, Naidu's title is specific to Banking & Financial Services rather than a general LTM executive title, reinforcing Claim 10's point that this partnership is being led from a named, financial-services-specific business unit rather than a general corporate-partnerships function — a more vertical-specific organizational signal than either the Infosys or Cognizant posts give for their respective partner-side spokespeople (neither of which quotes anyone by name at all).

### Claim 10: BlueVerse RightLogic will focus first on banking, financial services, and insurance — where Devin has been "thoroughly proven" and where LTM brings deep institutional expertise — before scaling RightLogic and the broader joint-offering portfolio (spanning application modernization and SDLC transformation) to additional industries
- **Evidence**: Section header ("Starting with banking, built to scale") and its accompanying paragraph, naming the initial vertical and the two named categories of planned future joint offerings.
- **Confidence**: anecdotal (stated sequencing and plan; no timeline given for when expansion to "additional industries" begins, and "thoroughly proven" is asserted without a specific proof point beyond what's already stated in Claims 1, 4, and 6)
- **Quote**: "BlueVerse RightLogic will focus first on banking, financial services, and insurance, where Devin has been thoroughly proven and where LTM brings deep institutional expertise. The partnership will then scale RightLogic and the broader portfolio of joint offerings, spanning application modernization, SDLC transformation, and more, across additional industries."
- **Our assessment**: This matches the "lead with the most regulated, highest-stakes vertical rather than a lower-stakes pilot" sequencing choice `blog-cognition-infosys-partnership.md` Claim 2 flagged as notable for Infosys's Financial Services-first rollout — a second, independent instance of a Cognition SI partner choosing regulated banking/financial-services as the *first* deployment target for an autonomous or semi-autonomous coding/security agent, here specifically for a security-remediation (not general engineering-productivity) use case. The mention that RightLogic sits alongside planned "application modernization, SDLC transformation" joint offerings confirms Claim 2's five-offerings figure includes non-security work, meaning the LTM partnership is not exclusively a security play even though this announcement leads with security.

## Concrete Artifacts

```
Full body text of the announcement (cognition.com/blog/ltm-cognition-partnership,
published 07.28.26, byline "By The Cognition Team"), reproduced in full from
raw fetched page text — this is the entire substantive content of the post:

"LTM Partners with Cognition To Reduce Cyber Risk in Financial Services

By The Cognition Team | 07.28.26

LTM has partnered with Cognition to deploy Devin, the AI software engineer,
across its global client base and cybersecurity practice serving over 260
clients, including 26 of the Fortune 500 and the top 5 global banks.

The partnership brings Devin into BlueVerse RightLogic, a managed,
outcome-based service that clears a customer's vulnerability backlog by
pairing Devin's autonomous engineering capacity with LTM's enterprise-grade
security practice and delivery expertise. RightLogic is an extension of LTM
BlueVerse, LTM's AI-native ecosystem that embeds intelligent agents directly
into core business processes, and is the first of five joint offerings the
two companies are bringing to market together.

As AI accelerates code production, AI-powered cyberattacks have tripled —
swarms of low-cost attacks now probe every possible vulnerability, leaving
enterprises of all sizes exposed. Meanwhile, security teams are drowning:
many face 10–100x more security findings, with a large share being false
positives. The tools most enterprises rely on offer coverage but stop at
detection: they miss the chained exploits that require deep reasoning about
business logic, and leave validation and remediation up to humans. At
Cognition, we built Devin Security Swarm in order to give security teams the
engineering capabilities to ship fixes themselves. Major enterprises are
already using Devin Security Swarm to detect critical vulnerabilities across
the codebase, validate their exploitability at runtime, and ship remediation
PRs, finding more verified vulnerabilities at 30% lower cost than the
nearest comparable alternative.

RightLogic operationalizes Devin's Security capabilities as a managed
service, built on three pillars:

Managed remediation: RightLogic ingests findings from the scanners
enterprises already run, prioritizes them against business criticality and
regulatory exposure, and routes high-confidence fixes to Devin for
end-to-end remediation while LTM engineers handle the complex tasks that
need human judgment. Every fix is reviewed by a person before it merges.

Enterprise Scale and Governance: Devin supplies the autonomous capacity to
work across tens of thousands of findings while LTM applies the remediation
playbooks, compliance rules, coding standards, and regulated-industry
expertise it already runs, delivered by engineers trained on Devin and
productive from day one. RightLogic is designed to clear 80 percent of an
enterprise's CVE backlog, up from the 60 percent previously delivered, an
improvement jointly backed by LTM and Cognition.

Continuous improvement at scale: Every engagement sharpens LTM's
remediation playbooks, encoding each customer's compliance rules and coding
standards so remediation runs faster and more autonomously over time.

"Security has become a volume problem that no human team can staff its way
out of. Devin lets security teams move from reporting issues to resolving
them, and LTM brings the expertise and customer relationships to deliver
that outcome at enterprise scale." — Gardner Johnson, VP Global
Partnerships, Cognition.

Starting with banking, built to scale

BlueVerse RightLogic will focus first on banking, financial services, and
insurance, where Devin has been thoroughly proven and where LTM brings deep
institutional expertise. The partnership will then scale RightLogic and the
broader portfolio of joint offerings, spanning application modernization,
SDLC transformation, and more, across additional industries.

"The Financial Services sector is under constant pressure to strengthen
security while accelerating AI adoption. Through BlueVerse RightLogic and
Devin, we are helping clients reduce vulnerability backlogs, automate
remediation, and improve cyber resilience across financial services,
empowering them to innovate faster without compromising security." — Harsh
Naidu, Chief Business Officer – Banking & Financial Services, LTM.

This partnership builds on real momentum inside LTM: a large pool of LTM
engineers has already been trained on Devin, so customers engage teams that
are productive on day one. LTM customers can learn more about deploying
Devin at scale here."
```

### Linked sub-page: the benchmark behind the "30% lower cost" claim

The phrase "Devin Security Swarm" in the third paragraph above is an inline
hyperlink to `https://cognition.com/blog/introducing-devin-security-swarm`
("Introducing Devin Security Swarm," By The Cognition Team, 07.01.26). That
page is the origin of this post's cost claim and publishes the benchmark
this post omits. Reproduced verbatim from that page's raw HTML:

```
"Devin Security Swarm brings engineering capabilities to security teams so
they can ship fixes themselves. It finds vulnerabilities across the codebase,
validates that they are exploitable at runtime, and ships remediation PRs.
Security Swarm finds more verified vulnerabilities at 30% lower cost than the
nearest comparable alternative."

Performance

"We evaluated Devin Security Swarm on a benchmark of 50 real-world
vulnerabilities, each tied to a published GitHub Security Advisory (GHSA)
across repositories in Go, Python, JavaScript, Rust, Ruby, C#, Java, Swift,
PHP, Elixir, Erlang, C, Kotlin, and Dart."

  Harness            Recall    $/Run
  Devin Security     72%       $90.23
  Claude Security    68%       $131.87
  Codex Security     48%       $118.20
  Cursor Security    26%       $4.60

"Only Devin found three critical vulnerabilities that other tools missed: a
PHP sandbox bypass via template injection, an argument injection through
metadata value parsing, and an overly broad deserialization surface in Spring
Kafka."
```

Arithmetic check: $90.23 vs. $131.87 is 31.6% lower cost, against the
highest-recall competitor in the table (Claude Security, 68% vs. Devin's
72%) — consistent with "more verified vulnerabilities at 30% lower cost than
the nearest comparable alternative." Note that Cursor Security is ~19x
cheaper per run ($4.60) at 26% recall, so "nearest comparable alternative"
must be read as nearest-by-recall, not nearest-by-price.

This sub-page has substantive content not covered by this note (an "Agentic
MapReduce" parallel-agent architecture description, configurable scan
profiles with incremental post-baseline scanning, and a six-week
"Devin Security Vulnerability Remediation Program" forward-deployed
engagement) and links onward to two devin.ai posts — `/blog/agentic-map-reduce`
and `/blog/security-swarm-eval` (evaluation methodology). It warrants its own
source note; only the material bearing on this post's Claim 4 is extracted
here. See Extraction Notes.

## Cross-References

- **Corroborates**: `blog-cognition-devin-federal-security-swarm.md` Claim 1
  and `blog-cognition-doe-genesis-mission.md` Claim 8 — this source's Claim 4
  (detect vulnerabilities → validate exploitability at runtime → ship
  remediation PRs) independently restates the identical three-stage Devin
  Security Swarm mechanism described in both of those posts, in a third,
  differently-worded Cognition source, which strengthens confidence that
  this is Cognition's settled product description rather than a one-off
  framing for a single audience (though none of the three posts benchmarks
  the mechanism independently). This source's Claim 3 ("traditional"
  tooling "stop[ping] at detection") also corroborates the same
  tooling-inadequacy framing documented in `blog-cognition-devin-federal-security-swarm.md`
  Claim 4 and `blog-cognition-doe-genesis-mission.md` Claim 7.
- **Corroborates**: `blog-cognition-infosys-partnership.md` Claim 2 — this
  source's Claim 10 (leading with banking/financial services/insurance as
  the *first* deployment vertical, ahead of a broader multi-industry
  rollout) is a second, independent instance of a Cognition SI partner
  choosing the most heavily regulated vertical as the initial target rather
  than a lower-stakes pilot, here for a security-remediation use case rather
  than Infosys's general engineering-productivity/legacy-migration use case.
- **Contradicts**: None identified. This source's cost/outcome claims (30%
  lower cost per verified vulnerability; 80% vs. 60% CVE backlog clearance)
  do not oppose any existing source note's claims about Devin Security Swarm
  or comparable vulnerability-remediation tooling. The 30%-lower-cost figure
  is not a *separate* metric from the "72% recall at $90.23/run... versus
  named competitors at 26-68% recall" benchmark flagged as unmined in
  `blog-cognition-doe-genesis-mission.md`'s Extraction Notes — following
  this post's inline link to `/blog/introducing-devin-security-swarm`
  (see Concrete Artifacts → Linked sub-page) shows it is *derived from* that
  same benchmark ($90.23 vs. Claude Security's $131.87 = 31.6% lower, at 72%
  vs. 68% recall). The two figures agree; this post simply restates the
  conclusion without its baseline. The 80%/60% CVE-clearance pair is a
  distinct LTM-service-level metric with no corpus counterpart to contradict.
- **Extends**: `blog-cognition-infosys-partnership.md` and
  `blog-cognition-cognizant-partnership.md` — this source follows the same
  unattributed-byline, internal-momentum-then-client-expansion narrative
  template documented in those two notes' Claim 7 (Infosys) and Corroborates
  section (Cognizant), but extends it in three ways: (1) it is the first
  Cognition SI-partnership post in this corpus to lead with a
  security/compliance vertical (Devin Security Swarm + RightLogic) rather
  than general engineering-productivity or legacy-migration work; (2) it is
  the first to break the "zero named spokesperson" pattern both prior notes
  flagged, quoting two named, titled individuals (Claims 8-9); (3) it is the
  first to give quantified before/after outcome and comparative-cost figures
  (80% vs. 60% CVE clearance; 30% lower cost) rather than the purely
  qualitative "material productivity gains" language in the Infosys post or
  the zero-metric Cognizant post. Also extends
  `blog-cognition-devin-federal-security-swarm.md` and
  `blog-cognition-doe-genesis-mission.md` by providing a third, commercial
  (non-federal, non-webinar) context for Devin Security Swarm — an
  outcome-based managed service sold through a systems-integrator partner
  to enterprise financial-services clients, rather than a direct federal
  sales motion.
- **Novel**: The "outcome-based" managed-service commercial model (Claim 2)
  is new to this corpus's SI-partnership material — neither the Infosys nor
  Cognizant posts describe pricing or commercial structure at all. The
  explicit "every fix is reviewed by a person before it merges" governance
  guarantee (Claim 5) is also new — no prior SI-partnership or Security Swarm
  post in this corpus states a merge-gating policy this concretely. The
  named before/after CVE-clearance percentage pair (60% → 80%, Claim 6) is
  the first quantified backlog-clearance outcome figure for Devin Security
  Swarm in this corpus's partnership-post material (distinct from, and not
  reconcilable with, the unmined recall/cost-per-run benchmark noted in
  `blog-cognition-doe-genesis-mission.md`). Two named, titled spokespeople
  quoted on the record (Claims 8-9) is also a first for this corpus's
  Cognition SI-partnership-post cluster specifically.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add this source alongside
  `blog-cognition-infosys-partnership.md` and `blog-cognition-cognizant-partnership.md`
  as a third instance of the Cognition SI-partnership pattern, but flag it
  as the first to target a security/compliance vertical rather than general
  engineering productivity or legacy migration — if the guide's Chapter 05
  coverage of SI partnerships is vertical-agnostic, note that this source
  demonstrates the pattern extending into regulated-industry security
  operations specifically, not just software delivery capacity.
- **Chapter 06 (Security & Threat Model)**: This is the corpus's third
  independent Cognition source describing Devin Security Swarm's
  detect/validate-exploitability/remediate mechanism (alongside
  `blog-cognition-devin-federal-security-swarm.md` Claim 1 and
  `blog-cognition-doe-genesis-mission.md` Claim 8) and the first to attach a
  named commercial outcome-based service (RightLogic) and quantified
  before/after backlog-clearance figures (80% vs. 60%, Claim 6) plus a
  comparative cost claim (30% lower cost per verified vulnerability, Claim
  4) to it. If Chapter 06 discusses AI-driven vulnerability remediation at
  enterprise scale, this source adds the first named commercial-deployment
  metrics for the pattern in this corpus — but every metric here is a
  vendor/partner-jointly-stated figure with no disclosed methodology,
  baseline, or independent audit, so it should be cited as a stated target
  or claim, not a verified measured outcome, consistent with how the two
  companion Security Swarm sources are already weighted.
- **Chapter 05 (Team Adoption) — governance detail**: Claim 5's explicit
  "every fix is reviewed by a person before it merges" policy is a concrete,
  citable human-in-the-loop governance guarantee for an otherwise
  autonomous-remediation product — useful if the guide discusses where
  human review gates are placed in agentic security-remediation workflows,
  since neither the Infosys nor Cognizant partnership posts, nor the two
  companion Security Swarm posts, state an equivalent merge-gating policy
  this explicitly.
- Do NOT cite the 30%-lower-cost or 80%/60% CVE-clearance figures (Claims 4,
  6) as independently verified performance data — both are vendor/partner
  self-reported, and should be attributed explicitly to LTM and Cognition's
  own joint statement if used in guide prose. The two differ in how much
  backing exists behind them, and the guide should treat them differently:
  the 30%-lower-cost figure *does* have a disclosed baseline and methodology,
  but only on the linked sub-page, not in this post (Cognition's own
  50-vulnerability GHSA benchmark, $90.23 vs. Claude Security's $131.87 —
  see Concrete Artifacts → Linked sub-page); it is a self-run, self-designed,
  unaudited vendor benchmark, so it is citable as "Cognition's own published
  benchmark" with the competitor and sample named, not as a neutral result.
  The 80%/60% CVE-clearance pair has no disclosed baseline, sample, or
  methodology anywhere and remains a stated joint target only.

## Extraction Notes

- **Fetch method**: The page is Next.js-rendered, so it was fetched as raw
  HTML via `curl` with a browser user-agent and stripped of script/style/markup
  with a Python script — the same method used by
  `blog-cognition-infosys-partnership.md` and
  `blog-cognition-cognizant-partnership.md`. Every `Quote` field above was
  copied character-for-character from that raw-HTML extraction, per
  MINER.md §2a, and all ten were re-verified against a fresh fetch. This
  matters: a plain WebFetch of the same URL paraphrases at least one sentence
  (rendering Claim 4's "At Cognition, we built Devin Security Swarm in order
  to give security teams the engineering capabilities to ship fixes
  themselves" as "Devin Security Swarm was built to give..."), so WebFetch
  output alone is not a safe basis for verbatim quotes on this domain. An
  earlier revision of this note described the fetch method as WebFetch-only;
  that description was wrong and is corrected here.
- **Sub-pages followed**: The post body contains three inline hyperlinks, not
  one (an earlier revision of this note incorrectly stated there was one, and
  specifically that there were "no links to related technical documentation
  about Devin Security Swarm's internals" — that was false):
  1. "LTM BlueVerse" → `https://www.ltm.com/services/blueverse` (LTM vendor
     marketing page; not fetched — partner-side product marketing, below the
     MINER.md §1 substantive bar for this note's subject).
  2. "Devin Security Swarm" → `/blog/introducing-devin-security-swarm`
     (Cognition's own technical product post, 07.01.26). **Fetched and
     extracted** — see Concrete Artifacts → Linked sub-page. This is the
     page `blog-cognition-doe-genesis-mission.md`'s Extraction Notes flagged
     as a candidate future Miner target for containing the only quantified
     Security Swarm performance figure in the corpus, and it turns out to be
     the direct source of this post's "30% lower cost" claim, which
     materially changed Claim 4's assessment and the Contradicts entry above.
  3. "here" (in "learn more about deploying Devin at scale here") →
     `https://www.ltm.com/about-us/partners/cognition-devinAI` — an LTM
     partner page for Cognition/Devin, not a Cognition enterprise-contact
     page as an earlier revision of this note stated; not fetched (partner
     marketing).
- **Still a candidate Miner target**: `/blog/introducing-devin-security-swarm`
  should get its own source note. Only the material bearing on this post's
  Claim 4 (the cost claim and its benchmark) was extracted here; that page
  additionally describes an "Agentic MapReduce" parallel-agent architecture,
  configurable scan profiles with incremental post-baseline scanning, and a
  six-week forward-deployed "Devin Security Vulnerability Remediation
  Program," and links onward to two further devin.ai posts
  (`/blog/agentic-map-reduce`, `/blog/security-swarm-eval`) that would
  document the architecture and evaluation methodology in full.
- Existing source notes under `source-notes/` were searched for prior
  Cognition SI-partnership posts (`infosys`, `cognizant`) and prior Devin
  Security Swarm coverage (`federal-security-swarm`, `doe-genesis-mission`,
  and the Security Swarm passage in `blog-latentspace-ainews-fable-relaunch-orchestration.md`
  Claim 11) before writing the Cross-References section above; all claim
  numbers cited from those four notes were verified by re-reading each
  note's actual numbered claims (or, for the AINews digest, its exact Claim
  11 text) before citing — none were guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified. After
  following the linked Security Swarm post, this source's 30%-lower-cost
  claim resolves to the *same* measurement as the recall/cost-per-run
  benchmark flagged in `blog-cognition-doe-genesis-mission.md`'s Extraction
  Notes, and the two agree ($90.23 vs. $131.87 = 31.6% lower, at higher
  recall) — agreement, not opposition, so no contradiction issue was filed.
  The 80%/60% CVE-clearance figures have no corpus counterpart to oppose.
- Overall confidence is set to `anecdotal`, matching both
  `blog-cognition-infosys-partnership.md` and
  `blog-cognition-cognizant-partnership.md`: every substantive claim in this
  source is a vendor/partner joint statement of intent, plan, or outcome,
  with no independent audit, named client case study, or disclosed
  methodology behind either quantified figure (30% lower cost; 80%/60% CVE
  clearance). The two named-spokesperson quotes (Claims 8-9) raise this
  source's attribution quality above its two SI-partnership-post
  predecessors, but do not change the underlying evidentiary weight of the
  claims themselves, which remains self-reported and unaudited.
