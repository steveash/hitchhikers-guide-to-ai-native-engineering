---
source_url: https://openai.com/index/daybreak-securing-the-world
source_type: blog-post
title: "Daybreak: Tools for securing every organization in the world"
author: OpenAI (no individual byline)
date_published: 2026-06-22
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1920"
---

# Daybreak: Tools for securing every organization in the world

> OpenAI's first-party announcement expanding Daybreak — its cybersecurity initiative — with an updated Codex Security plugin (30M+ commits scanned, 500K+ findings auto-fixed), a more permissive/capable GPT‑5.5‑Cyber model (85.6% on CyberGym), a 28-partner Cyber Partner Program, and "Patch the Planet," a Trail of Bits collaboration that found production vulnerabilities (including a 23-year-old OpenBSD use-after-free) across nine open-source projects.

## Source Context

- **Type**: blog-post (official OpenAI blog, `openai.com/index/...`, June 22, 2026;
  product/initiative announcement with embedded stat graphics, a partner logo
  cloud, and links to four sub-pages: the Daybreak overview page, the Codex
  Security plugin page, the Daybreak Cyber Partner Program page, and the "Patch
  the Planet" initiative page)
- **Author credibility**: First-party OpenAI communication — no individual
  byline, published under the OpenAI brand. This is the model vendor describing
  its own product and its own benchmark results (CyberGym, ExploitGym, SEC-bench
  Pro), so the capability numbers are unaudited self-report. The vulnerability
  counts attributed to Patch the Planet are described as reviewed by Trail of
  Bits security researchers (a named third-party firm) before reaching
  maintainers, which is a meaningful independent-review step, though the raw
  counts themselves are still OpenAI's own disclosure. The Cloudflare CTO quote
  on the linked Daybreak overview page is the only outside-voice corroboration
  in the source cluster.
- **Scope**: Covers OpenAI's Daybreak cybersecurity initiative as of June 2026:
  the Codex Security plugin (scan/patch workflow, production usage stats), the
  GPT‑5.5‑Cyber model update (benchmark scores, access tiering), the Daybreak
  Cyber Partner Program (product and GSI partners), Patch the Planet
  (open-source vulnerability remediation with Trail of Bits/HackerOne/Calif),
  and government/critical-infrastructure partnerships (Trusted Access for Cyber
  agreements with several national governments). Does NOT cover: agent
  architecture internals for Codex Security (no MCP/tool-call design detail
  comparable to Cursor's security agent fleet), false-positive/false-negative
  rates for Codex Security findings, pricing for GPT‑5.5‑Cyber or Trusted
  Access, or a methodology description for how the 500,000+ "automatically
  determined to be fixed" findings were verified.

## Extracted Claims

### Claim 1: The security bottleneck has shifted from finding vulnerabilities to patching them, because AI has made vulnerability discovery cheap relative to remediation capacity

- **Evidence**: OpenAI's framing statement contrasting the historical
  vulnerability-discovery bottleneck with the current post-AI environment.
- **Confidence**: emerging (directional framing from the model vendor; consistent
  with, but not identical to, the corpus's existing "finding-to-fixing gap"
  framing)
- **Quote**: "The bottleneck historically has been _finding_ vulnerabilities, but now defenders are overwhelmed with the number of vulnerabilities found. Instead, the bottleneck is now _patching_ vulnerabilities."
- **Our assessment**: This is a slightly different emphasis than Anthropic's
  "order-of-magnitude increase in finding volume" framing
  (`blog-anthropic-ai-accelerated-offense.md` Claim 5) and Bobby Holley's
  "vertigo" account of Firefox's 271-bug finding shock
  (`blog-simonwillison-bobby-holley.md` Claim 7) — those sources frame the shock
  as "too many findings to triage"; OpenAI frames it as "too many findings to
  fix." Both are compatible: triage and remediation are sequential stages of the
  same overloaded pipeline. OpenAI's framing most closely mirrors Deloitte's "the
  gap helps determine whether attackers or defenders win the window"
  (`blog-anthropic-opus-cybersecurity-partners.md` Claim 7) — both name
  remediation speed, not discovery, as the decisive variable.

### Claim 2: Codex Security has scanned over 30 million commits across more than 30,000 codebases since its March 2026 research preview, with human reviewers manually confirming 70,000+ fixed findings and 500,000+ findings automatically determined to be fixed

- **Evidence**: Production usage statistics presented with an inline stat
  graphic ("30K Repos scanned," "30M+ Commits scanned," "500K+ Fixed findings").
- **Confidence**: anecdotal (vendor-reported aggregate usage metrics; no
  methodology given for how "automatically determined to be fixed" is verified,
  and no false-positive or precision/recall figures are provided)
- **Quote**: "Since launching Codex Security cloud in research preview in March, it has scanned over 30 million commits across more than 30,000 codebases; human reviewers have manually marked more than 70,000 findings as fixed, and over 500,000 findings have automatically been determined to be fixed."
- **Our assessment**: The 500,000-to-70,000 ratio (automatically-determined vs.
  manually-confirmed fixes) is notable: roughly seven automated determinations
  for every one a human reviewer manually marked. This scale claim is the OpenAI
  analog to Cursor's "3,000+ PRs/week, 200+ vulnerabilities/week"
  (`blog-cursor-security-agents.md` Claim 9) and Wiz's "150,000+ production
  assets a week, zero false positives"
  (`blog-anthropic-opus-cybersecurity-partners.md` Claim 2) — all three vendors
  report large-scale automated security scanning numbers without independent
  audit. The corpus pattern is now: every major AI vendor/partner ecosystem
  (Anthropic partners, Cursor, OpenAI) reports six-figure-or-higher scan/finding
  volumes with no shared measurement standard, which limits cross-vendor
  comparison but strengthens the directional claim that AI-assisted security
  scanning now operates at a scale no manual process could match.

### Claim 3: Codex Security is designed to put "the equivalent of a security engineer next to every software developer" by generating a codebase-specific threat model, validating reachability, and producing a verified patch — not just emitting alerts

- **Evidence**: OpenAI's description of the plugin's design premise and workflow
  steps.
- **Confidence**: emerging (vendor design description; the "generate one if it
  doesn't exist" threat-model claim and reachability validation are specific
  enough to indicate a real workflow rather than marketing abstraction, but no
  benchmark of threat-model quality or reachability-analysis accuracy is given)
- **Quote**: "Rather than just generating alerts, Codex Security will understand your team's code and its threat model (or generate one if it doesn't exist), identify plausible vulnerabilities, determine whether affected code is reachable, gather evidence to provide validation steps, develop a targeted patch, and verify the result."
- **Our assessment**: The reachability-validation step is architecturally
  identical to Cursor's Anybump workflow, which "narrows findings to those that
  are actually impactful, then traces through the relevant code paths"
  (`blog-cursor-security-agents.md` Claim 6). This corroborates reachability
  analysis as a convergent design pattern across two independent vendors for
  filtering AI-generated vulnerability findings down to exploitable ones before
  presenting them to humans. The "generate a threat model if it doesn't exist"
  capability is more novel — it implies Codex Security can bootstrap threat
  modeling for codebases that never had one, which is a lower floor than Cursor's
  or Wiz's descriptions (which presuppose an existing scanning target).
  "Humans remain in control of which findings to investigate, which changes to
  apply, and what information to share" is an explicit human-in-the-loop
  commitment, consistent with the gradual-trust patterns documented across the
  corpus (Cursor's shadow→inform→gate rollout).

### Claim 4: GPT‑5.5‑Cyber reached 85.6% on CyberGym, versus 81.8% for GPT‑5.5, described as "the highest CyberGym score we have measured from a single model"

- **Evidence**: OpenAI's reported benchmark comparison between GPT‑5.5‑Cyber and
  the base GPT‑5.5 model on CyberGym, a benchmark OpenAI describes as measuring
  "whether an agent can reproduce known vulnerabilities in software
  environments."
- **Confidence**: emerging (first-party benchmark; OpenAI's own benchmark suite,
  not independently run; no comparison to non-OpenAI frontier models such as
  Claude Mythos Preview is provided in this source)
- **Quote**: "On CyberGym, which measures whether an agent can reproduce known vulnerabilities in software environments, the updated GPT‑5.5‑Cyber reached 85.6% in single-model evaluations, compared with 81.8% for GPT‑5.5. This is the highest CyberGym score we have measured from a single model."
- **Our assessment**: CyberGym, ExploitGym, and SEC-bench Pro (Claim 5) are all
  OpenAI-named benchmarks not previously documented anywhere in the corpus,
  which otherwise relies on the UK AI Security Institute's (AISI) independent
  benchmark suite (Expert-level CTF tasks, "The Last Ones" corporate-network
  simulation) for cross-model cyber-capability comparison
  (`blog-simonwillison-cybersecurity-proof-of-work.md`,
  `blog-simonwillison-aisi-gpt55-cyber.md`). Because CyberGym/ExploitGym/SEC-bench
  Pro are OpenAI's own benchmarks, the 85.6% figure cannot be directly compared
  to the AISI figures already in the corpus (GPT‑5.5: 71.4% ±8.0% on AISI
  Expert-level tasks). The guide should not conflate these two evaluation
  families when citing capability numbers.

### Claim 5: GPT‑5.5‑Cyber outperformed GPT‑5.5 on ExploitGym (39.5% vs. 25.95%) and SEC-bench Pro (69.8% vs. 63.1%)

- **Evidence**: OpenAI's reported benchmark comparisons. ExploitGym is described
  as testing "whether agents can turn known vulnerabilities into working
  exploits that achieve unauthorized code execution." SEC-bench Pro is described
  as evaluating "long-horizon vulnerability discovery and proof-of-concept
  generation across complex software targets."
- **Confidence**: anecdotal (first-party benchmarks with no external
  validation, no confidence intervals, and no description of task counts or
  sample sizes, unlike the AISI evaluations elsewhere in the corpus which report
  confidence intervals and task counts)
- **Quote**: "GPT‑5.5‑Cyber also outperformed GPT‑5.5 on two demanding real-world security benchmarks: 39.5% versus 25.95% on ExploitGym, which tests whether agents can turn known vulnerabilities into working exploits that achieve unauthorized code execution. On SEC-bench Pro, which evaluates long-horizon vulnerability discovery and proof-of-concept generation across complex software targets, GPT‑5.5‑Cyber reached 69.8%, compared with 63.1% for GPT‑5.5."
- **Our assessment**: The ExploitGym task (turning a known vulnerability into a
  working exploit with unauthorized code execution) is explicitly an offensive
  capability benchmark. Naming and publishing an offensive-exploit-generation
  benchmark score is more direct dual-use disclosure than most of the corpus's
  defensive-framed claims (Codex Security, CLUE, Cursor's agent fleet). OpenAI
  pairs this disclosure with the access-tiering description in Claim 6, which is
  the intended mitigation — but the benchmark existing at all confirms that
  frontier models are now explicitly evaluated and marketed on offensive
  exploit-generation ability, not only defensive scanning ability.

### Claim 6: OpenAI operates a three-tier access model for cyber capability — GPT‑5.5 available by default, GPT‑5.5 with "Trusted Access for Cyber" for advanced defensive workflows, and GPT‑5.5‑Cyber restricted to verified defenders conducting authorized red-teaming/exploit validation

- **Evidence**: A comparison table on the linked Daybreak overview page
  (`openai.com/daybreak`) describing what each access tier unlocks, its intended
  use cases, and its designed audience.
- **Confidence**: settled (this is a stated first-party product/policy
  structure, not a capability projection — verifiable by checking OpenAI's
  current access documentation)
- **Quote**: "Some advanced cyber capabilities require a controlled access process. Through Trusted Access, approved teams can use these models in scoped environments with authorization, logging, verification, and stronger controls for higher-risk defensive workflows." (from the Daybreak overview page, `openai.com/daybreak`)
- **Our assessment**: This is OpenAI's analog to the model-safety-control
  concern raised in the AISI evaluation of GPT‑5.5, where "AISI expert
  red-teamers found a universal jailbreak effective across all malicious cyber
  queries in approximately 6 hours" and OpenAI's fix could not be independently
  verified before publication (`blog-simonwillison-aisi-gpt55-cyber.md` Claim
  6). The tiered-access model is the intended structural safeguard for exactly
  that risk: rather than relying solely on the model refusing malicious
  requests, OpenAI gates the more permissive GPT‑5.5‑Cyber behind an
  authorization/logging/verification process for vetted defenders. Whether this
  access-control layer is more robust than model-level refusal (which AISI
  showed was breakable) is not established in this source or elsewhere in the
  corpus — it is a claim about process controls, not a benchmarked outcome.

### Claim 7: The Daybreak Cyber Partner Program lets 20 named product-security vendors and 8 named Global Systems Integrators embed GPT‑5.5 (via Trusted Access) into their own products, keeping direct model access with the partners rather than their end customers

- **Evidence**: OpenAI's description of the partner program plus the partner
  list on the linked partner page (`openai.com/daybreak/partners/`): product
  partners include Akamai, Cato Networks, Check Point, Cisco, Cloudflare,
  CrowdStrike, Darktrace, Elastic, Fortinet, IBM, Okta, Palo Alto Networks,
  Proofpoint, Red Hat, Trend/TrendAI, SentinelOne, SpecterOps, Sophos, Tenable,
  and Zscaler; GSI partners include IBM, Accenture, EY, KPMG, PwC, Cognizant,
  GuidePoint Security, and NCC Group.
- **Confidence**: settled (named partner list is a verifiable factual claim
  about business relationships, not a capability projection)
- **Quote**: "Through the program, participating partners can use GPT‑5.5 with Trusted Access for Cyber—our primary model for most defensive cybersecurity workflows—in the security products and services they provide to customers. This allows their customers to benefit from the model's defensive capabilities and make their software more resilient, but keeps direct model access in the hands of participating partners."
- **Our assessment**: This is a near-identical structural pattern to Anthropic's
  security partner ecosystem documented in
  `blog-anthropic-opus-cybersecurity-partners.md` — both vendors route frontier
  cyber capability to enterprises through named security-industry partners
  rather than direct API access, and both name CrowdStrike, Accenture, and PwC
  specifically as partners. This is the strongest single data point in the
  corpus that "route capability through trusted security-industry
  intermediaries rather than direct API access" is now the standard
  go-to-market pattern for frontier labs selling cyber capability to
  enterprises, not an Anthropic-specific choice. Notably, CrowdStrike, Accenture,
  and PwC appear as named partners in *both* OpenAI's and Anthropic's
  cybersecurity partner ecosystems — the same major consultancies and security
  vendors are integrating multiple frontier labs' models simultaneously, which
  the guide should flag as evidence that enterprise security buyers are
  multi-sourcing frontier model capability rather than standardizing on one lab.

### Claim 8: Patch the Planet, run with Trail of Bits in collaboration with HackerOne and Calif, filters and deduplicates AI-generated vulnerability findings through expert human security review before they reach open-source maintainers

- **Evidence**: OpenAI's description of the initiative's operating model: an
  initial consultation phase where maintainers set priorities and disclosure
  preferences, followed by Patch the Planet researchers managing "the work end
  to end—validating and deduplicating both vulnerabilities and patches before
  they reach maintainers."
- **Confidence**: emerging (described process with a named third-party
  reviewing organization, Trail of Bits, which adds independent-review
  credibility beyond a pure vendor self-report; no data on review time,
  reviewer headcount, or rejection rate for AI-generated findings that did not
  pass review)
- **Quote**: "Maintainers define their priorities, preferences, and established disclosure processes. Patch the Planet security researchers then manage the work end to end–validating and deduplicating both vulnerabilities and patches before they reach maintainers, significantly reducing the burden on maintainers and speeding up remediation."
- **Our assessment**: This human-review-before-maintainer-contact design directly
  addresses the "maintainer report deluge" problem that Anthropic's own
  disclosure-etiquette recommendation targets (`blog-anthropic-ai-accelerated-offense.md`
  Claim 10's disclosure section: "Explicit disclosure: 'This report was
  AI-assisted'... Deference to maintainer judgment"). Patch the Planet goes
  further than a disclosure-etiquette norm — it interposes a funded human
  review layer between the AI-generated findings and the maintainer, rather
  than relying on the AI submitter to self-regulate report quality. The source
  explicitly frames this as a response to concentrated maintainer risk: citing
  a Linux Foundation/Harvard study that "94 percent of the widely used projects
  it studied had fewer than ten developers responsible for more than 90 percent
  of the code."

### Claim 9: Patch the Planet's initial engagement found a 23-year-old use-after-free vulnerability in OpenBSD, confirmed 34 vulnerabilities in FreeBSD (7 with local-privilege-escalation proofs-of-concept), and produced 8 kernel-pointer-leak proofs-of-concept plus 24 local-privilege-escalation exploits against the Linux kernel

- **Evidence**: Concrete vulnerability-finding results reported on the linked
  "Patch the Planet" sub-page (`openai.com/index/patch-the-planet/`), broken out
  by target: operating systems (Linux kernel, OpenBSD, FreeBSD), network
  software (dnsmasq — matching CVE-2026-4890, -4891, -4892, -5172; an "HTTP/2
  Bomb" denial-of-service technique affecting NGINX, Apache, IIS, and Pingora),
  and browsers (5 exploitable Chrome/V8 vulnerabilities, 10+ exploitable
  Safari/WebKit vulnerabilities, 1 Firefox WebAssembly vulnerability,
  CVE-2026-8390).
- **Confidence**: emerging (specific CVE numbers and named targets make this a
  verifiable claim in principle; Trail of Bits' involvement as reviewer adds
  credibility beyond raw vendor disclosure; however, no independent third-party
  confirmation of these specific counts was found during this extraction)
- **Quote**: "OpenBSD: Identified a 23-year-old use-after-free vulnerability." (Patch the Planet sub-page, Key Findings Across Software Stack — Operating Systems section)
- **Our assessment**: A 23-year-old use-after-free bug surviving in OpenBSD —
  a project with an unusually strong security-audit culture and BSD's smaller,
  more heavily-scrutinized codebase relative to Linux — is a striking concrete
  data point for the corpus's recurring claim that frontier models find bugs
  human review missed for extended periods (`blog-anthropic-ai-accelerated-offense.md`
  Claim 2; `blog-simonwillison-bobby-holley.md` Claim 1's 271 Firefox bugs). This
  is a second, independently-sourced set of named-target production
  vulnerability disclosures in the corpus, this time from OpenAI rather than
  Anthropic, and spanning multiple operating systems (Linux, OpenBSD, FreeBSD)
  rather than a single browser codebase. Note that OpenAI's Patch the Planet
  findings list separately includes a Firefox WebAssembly vulnerability
  (CVE-2026-8390) — this source does not state whether that finding is related
  to, or independent of, Anthropic's Firefox 150 collaboration documented in
  `blog-simonwillison-bobby-holley.md`; no shared-attribution claim should be
  inferred without further evidence.

### Claim 10: The Daybreak sub-page reports nine open-source projects joined Patch the Planet's "first round" (cURL, NATS Server, pyca/cryptography, Sigstore, aiohttp, the Go project, freenginx, Python, and python.org), while the main Daybreak announcement describes "more than 30 open-source projects" as having "committed to participate"

- **Evidence**: Two different participant counts appear across OpenAI's own
  Daybreak content: the main announcement states "More than 30 open-source
  projects have committed to participate, with initial participants including
  cURL, Go, Python, Sigstore, and pyca/cryptography," while the linked Patch the
  Planet sub-page states "Nine projects joined the first round" and names nine
  specific projects.
- **Confidence**: anecdotal (both figures come from the same OpenAI-controlled
  source cluster published the same day; this is an internal scope/framing
  difference within one vendor's own materials, not a claim vs. claim
  disagreement between independent sources)
- **Quote**: "More than 30 open-source projects have committed to participate, with initial participants including cURL, Go, Python, Sigstore, and pyca/cryptography." (main Daybreak announcement) vs. "Nine projects joined the first round: cURL, NATS Server, pyca/cryptography, Sigstore, aiohttp, the Go project, freenginx, Python, and python.org." (Patch the Planet sub-page)
- **Our assessment**: This is not treated as a corpus-worthy contradiction per
  MINER.md §4a — it reads as "more than 30 have committed overall" (a broader,
  ongoing-commitment figure) versus "nine joined the first round" (the initial
  cohort actually engaged so far), i.e., a conditioning-variable difference
  (total commitment vs. first-cohort scope) rather than two sources disagreeing
  on the same fact. Flagged here as an extraction note rather than a filed
  contradiction: if the guide cites a Patch the Planet participant count, it
  should specify which figure (30+ committed vs. 9 in the first round) and not
  present them interchangeably, since OpenAI itself does not reconcile them
  within the source cluster.

### Claim 11: OpenAI has established Trusted Access for Cyber partnerships with the governments of Australia, Canada, France, Germany, Japan, and the Republic of Korea, plus EU institutions including ENISA, in the month preceding this announcement

- **Evidence**: OpenAI's direct statement in the "Protecting critical
  infrastructure and sensitive systems" section, plus references to ongoing
  work with the U.S. government (CAISI, ONCD, OSTP) on a June 2026 U.S.
  Executive Order on AI innovation and security.
- **Confidence**: settled (named government partnerships are a verifiable
  factual claim about institutional relationships)
- **Quote**: "In the past month we have already established Trusted Access for Cyber partnerships with Australia, Canada, France, Germany, Japan, Republic of Korea, and EU institutions like ENISA."
- **Our assessment**: This is the first corpus source to document a frontier
  lab's cyber-capability access program extending to multiple national
  governments as named institutional partners (rather than to enterprises).
  This is a materially different category of stakeholder from the corpus's
  existing enterprise-focused security partner coverage (Anthropic's Wiz/Palo
  Alto/Accenture/CrowdStrike/PwC roster in
  `blog-anthropic-opus-cybersecurity-partners.md`, and OpenAI's own product/GSI
  partner list in Claim 7 above). The scope — "eligible operators of critical
  infrastructure, including government networks" — signals that frontier
  cyber-capability governance is now explicitly a matter of international
  government-to-vendor negotiation, not solely enterprise procurement.

## Concrete Artifacts

### Codex Security Setup Workflow (from `openai.com/daybreak/codex-security-plugin/`)

```
Codex Security Plugin — Setup Guide
Source: openai.com/daybreak/codex-security-plugin/ (linked sub-page)

Two entry points: "Use Desktop Codex for a guided flow, or Codex CLI for a
one-command scan from a folder of code."

1. Install Codex (skip if already installed and signed in)
2. Add the Codex Security plugin (button becomes "Try in chat" once installed)
3. Click "Try in chat" — opens a new chat with a pre-loaded security scan prompt
4. Choose a folder containing the code to review
5. Press "Send" to initiate the security analysis
```

### Codex Security Production Usage Stats (main Daybreak post)

```
Since research preview launch (March 2026):
  30,000+   codebases scanned
  30M+      commits scanned
  70,000+   findings manually marked "fixed" by human reviewers
  500,000+  findings automatically determined to be fixed
```

### GPT‑5.5‑Cyber Benchmark Comparison (main Daybreak post)

```
Benchmark        | GPT-5.5-Cyber | GPT-5.5 | What it measures
-----------------|----------------|---------|----------------------------------
CyberGym         | 85.6%          | 81.8%   | Reproducing known vulnerabilities
ExploitGym       | 39.5%          | 25.95%  | Turning known vulns into working
                 |                |         | exploits (unauthorized code exec)
SEC-bench Pro    | 69.8%          | 63.1%   | Long-horizon vuln discovery + PoC
                 |                |         | generation, complex targets

Note: these are OpenAI-named, first-party benchmarks, distinct from the UK
AI Security Institute's (AISI) independent benchmark suite used elsewhere in
the corpus (Expert-level CTF tasks, "The Last Ones" cyber range). Do not
directly compare these percentages to AISI figures for other models.
```

### Trusted Access Tiering Table (from `openai.com/daybreak`)

```
Access                          | Intended use cases                        | Designed for
---------------------------------|--------------------------------------------|------------------------------------
GPT-5.5 (default)               | Secure coding, secure code review,          | All developers and application
                                 | vulnerability discovery/triage,             | security teams
                                 | remediation guidance, dependency risk
                                 | analysis, patch validation
GPT-5.5 + Trusted Access Cyber  | Advanced vulnerability triage, malware      | Cyber teams doing advanced defensive
                                 | analysis, detection engineering,            | work; cyber product vendors; system
                                 | security investigations, incident           | integrators; consultancies; DevSecOps
                                 | analysis, complex defensive validation
GPT-5.5-Cyber                   | Authorized red teaming, penetration         | Cyber teams/vendors conducting
                                 | testing, exploit validation, controlled     | authorized red teaming, pen testing,
                                 | security testing                            | exploit validation, controlled testing
```

### Daybreak Cyber Partner Program Roster (from `openai.com/daybreak/partners/`)

```
Product Partners (20): Akamai, Cato Networks, Check Point, Cisco, Cloudflare,
  CrowdStrike, Darktrace, Elastic, Fortinet, IBM, Okta, Palo Alto Networks,
  Proofpoint, Red Hat, Trend/TrendAI, SentinelOne, SpecterOps, Sophos,
  Tenable, Zscaler

GSI Partners (8): IBM, Accenture, EY, KPMG, PwC, Cognizant,
  GuidePoint Security, NCC Group

Model: partners embed GPT-5.5 (Trusted Access) into their own products;
end customers do not get direct model access — access stays with the partner.
```

### Patch the Planet — Vulnerability Findings by Target (from linked sub-page)

```
Operating Systems:
  Linux Kernel:  8 kernel-pointer information-leak PoCs; 24 local
                 privilege-escalation exploits
  OpenBSD:       1 use-after-free vulnerability, 23 years old
  FreeBSD:       34 vulnerabilities confirmed; 7 with local
                 privilege-escalation PoCs

Network:
  dnsmasq:       patterns matching CVE-2026-4890, -4891, -4892, -5172
  HTTP/2 Bomb:   denial-of-service technique affecting NGINX, Apache,
                 IIS, and Pingora

Browsers:
  Chrome/V8:     5 exploitable vulnerabilities
  Safari/WebKit: 10+ exploitable vulnerabilities
  Firefox/Wasm:  1 vulnerability, CVE-2026-8390

Initial participants (per Patch the Planet sub-page, "first round," 9 total):
  cURL, NATS Server, pyca/cryptography, Sigstore, aiohttp, the Go project,
  freenginx, Python, python.org

(Main Daybreak announcement separately states "more than 30 open-source
projects have committed to participate" — see Claim 10 for the scope
discrepancy between these two OpenAI-published figures.)
```

## Cross-References

- **Corroborates** `blog-cursor-security-agents.md` Claim 6 (Anybump's
  reachability-analysis filter for autonomous dependency patching): Codex
  Security's "determine whether affected code is reachable" step (Claim 3
  above) is the same design pattern independently implemented by a different
  vendor for a different product. Two independent implementations of
  reachability filtering as the mechanism for converting raw AI-generated
  findings into actionable ones strengthens this as a general pattern, not a
  single-vendor idiosyncrasy.

- **Corroborates** `blog-anthropic-opus-cybersecurity-partners.md` Claim 1 and
  the partner roster in that note's Concrete Artifacts: OpenAI's Daybreak Cyber
  Partner Program (Claim 7 above) is structurally identical to Anthropic's
  security partner ecosystem — both frontier labs route cyber capability to
  enterprises through named security vendors and consultancies rather than
  direct API access, and CrowdStrike, Accenture, and PwC appear as named
  partners in *both* rosters. This is the strongest evidence in the corpus that
  major enterprise security vendors are integrating multiple frontier labs'
  models in parallel, not choosing one.

- **Corroborates** `blog-anthropic-ai-accelerated-offense.md` Claim 2 ("Today,
  publicly available models can find serious vulnerabilities that traditional
  reviews have missed for long periods") and `blog-simonwillison-bobby-holley.md`
  Claim 1 (271 Firefox vulnerabilities): Patch the Planet's 23-year-old OpenBSD
  use-after-free and 34 confirmed FreeBSD vulnerabilities (Claim 9 above) are
  further concrete, named-target evidence for the same claim, from a second
  frontier lab (OpenAI) applying the pattern to a different set of operating
  systems.

- **Corroborates** `blog-anthropic-opus-cybersecurity-partners.md` Claim 7
  (Deloitte: "the gap helps determine whether attackers or defenders win the
  window") and Claim 6 (TrendAI's 96-day virtual-patching lead time): OpenAI's
  "the bottleneck is now patching" framing (Claim 1 above) is the same
  finding-to-fixing-gap thesis, now stated by a second frontier lab as the
  central premise of its entire cybersecurity product line, rather than as one
  claim among several partner case studies.

- **Extends** `blog-anthropic-ai-accelerated-offense.md` Claim 10 ("AI
  vendoring" — reimplementing unmaintained dependencies) and the Linux
  Foundation/Harvard maintainer-concentration statistic cited in Patch the
  Planet (Claim 8 above, "94 percent of the widely used projects... had fewer
  than ten developers"): both sources independently identify small-maintainer-team
  capacity as the binding constraint on open-source security, but propose
  different responses — Anthropic recommends replacing unmaintained
  dependencies with AI-generated equivalents; OpenAI/Patch the Planet instead
  funds expert human review capacity to support existing maintainers. The guide
  should present these as two different remedies for the same
  maintainer-capacity problem, not as competing claims about the problem's
  existence.

- **Extends** `blog-simonwillison-aisi-gpt55-cyber.md` Claim 6 (AISI's
  universal-jailbreak finding on GPT‑5.5, with OpenAI's fix unverifiable by
  AISI at publication time): this source's three-tier Trusted Access structure
  (Claim 6 above) is OpenAI's process-control response to exactly the kind of
  model-safety-control gap AISI identified. The guide should note that this
  source does not resolve whether the access-tiering process is itself robust
  against circumvention — it is a claim about controls, not an independently
  verified outcome.

- **Novel**:
  - **CyberGym, ExploitGym, and SEC-bench Pro** are OpenAI-named benchmarks not
    previously documented in the corpus, distinct from the AISI benchmark suite
    used for all prior cross-model cyber-capability comparisons.
  - **Government-to-vendor Trusted Access for Cyber partnerships** with named
    national governments (Australia, Canada, France, Germany, Japan, Republic of
    Korea, EU/ENISA) is a new stakeholder category for the corpus — prior
    sources document only enterprise and open-source partnerships.
  - **A dual-vendor security partner ecosystem** (CrowdStrike, Accenture, and
    PwC integrating both Anthropic's and OpenAI's models) is a novel corpus
    observation about enterprise multi-sourcing of frontier cyber capability.
  - **Named CVE-level findings from a second frontier lab against operating
    system codebases** (OpenBSD, FreeBSD, Linux kernel) extends the corpus's
    production-vulnerability evidence beyond Anthropic/Firefox to an
    OpenAI/multi-OS case, with Trail of Bits as an independent reviewing party.
  - **An explicit offensive exploit-generation benchmark (ExploitGym)** publicly
    disclosed alongside a defensive product launch is a more direct form of
    dual-use benchmark disclosure than other corpus sources, which frame
    capability disclosures primarily in defensive terms.

## Guide Impact

- **Chapter 06 (Security and Threat Model)**: Add Codex Security's reachability-
  validation step and Patch the Planet's human-review-before-maintainer-contact
  model as two additional, independently-arrived-at implementations of patterns
  already documented from Anthropic and Cursor sources (reachability filtering,
  gradual human-in-the-loop trust). Specifically recommend citing this source
  alongside `blog-cursor-security-agents.md` Claim 6 to show reachability
  analysis is now a convergent, cross-vendor design pattern for autonomous
  vulnerability remediation, not one company's idiosyncratic choice.

- **Chapter 06 (Security and Threat Model) — Benchmark citation hygiene**: Add
  an explicit caution that OpenAI's CyberGym/ExploitGym/SEC-bench Pro scores and
  the AISI Expert-level CTF/TLO scores documented elsewhere in the corpus are
  different benchmark families and must not be presented as directly
  comparable numbers for the same capability axis.

- **Chapter 06 (Security and Threat Model) — Enterprise security ecosystem**:
  Update any section describing the AI security vendor landscape to note that
  CrowdStrike, Accenture, and PwC appear as named partners in both Anthropic's
  and OpenAI's cybersecurity partner programs. Recommend framing this as
  evidence that enterprise security buyers are integrating multiple frontier
  labs' capabilities in parallel rather than standardizing on a single vendor —
  a relevant consideration for any chapter section on vendor lock-in or
  model-selection strategy for security tooling.

- **Chapter 06 (Security and Threat Model) — Governance and access control**:
  Add the three-tier Trusted Access model (default / Trusted Access for Cyber /
  GPT‑5.5‑Cyber) as a concrete example of a frontier lab's access-control
  response to the AISI-documented jailbreak risk on the same model family
  (`blog-simonwillison-aisi-gpt55-cyber.md` Claim 6). Pair the two sources so
  the guide presents both the risk (AISI's jailbreak finding) and the vendor's
  structural mitigation (this source's tiering), while noting that no source in
  the corpus independently verifies the mitigation's robustness.

## Extraction Notes

1. **Source required a fetch workaround**: Direct `WebFetch` on
   `openai.com/index/daybreak-securing-the-world` returned HTTP 403. The full
   article text was retrieved via the `r.jina.ai` text-extraction proxy
   (`https://r.jina.ai/<original-url>`), which returned what appears to be a
   faithful, unsummarized rendering of the page (headings, bullet structure,
   and paragraph text intact). The four linked sub-pages (Daybreak overview,
   Codex Security plugin, Patch the Planet, Cyber Partner Program) were fetched
   the same way, but returned as WebFetch-summarized content rather than raw
   verbatim HTML-to-text, since the fetch tool applies a prompt-driven pass over
   sub-page content. Quotes drawn from the four sub-pages should be treated as
   slightly lower-confidence verbatim extractions than quotes drawn from the
   main article (which came through as continuous prose in the proxy fetch).
   Where a sub-page quote could not be confirmed as exact, it was either
   omitted or flagged in the relevant claim.

2. **Trail of Bits blog post not fetched**: The main article links to a Trail
   of Bits blog post ("Introducing Patch the Planet,"
   `blog.trailofbits.com/2026/06/22/introducing-patch-the-planet`) as further
   detail on the initial five-day sprint. This was not fetched for this
   extraction (five sub-pages were already followed: Daybreak overview, Codex
   Security plugin, Patch the Planet, Cyber Partner Program, plus the RSS feed
   entry). A follow-up extraction of the Trail of Bits post — an independent
   third-party account rather than OpenAI's own description — would add
   valuable outside verification of the Patch the Planet vulnerability counts
   and should be considered for a separate source-note pass if that post is
   filed as its own issue.

3. **No contradiction filed**: The only internal inconsistency found (Claim 10,
   9-projects-vs-30+-projects) is scored as a scope/framing difference within
   OpenAI's own materials, not a claim-vs-claim disagreement per MINER.md §4a's
   filing criteria, so no contradiction issue was opened. Flagged prominently
   in Claim 10 and the Concrete Artifacts section instead.

4. **Benchmark methodology gaps**: CyberGym, ExploitGym, and SEC-bench Pro are
   named but not described in detail (task counts, sample sizes, confidence
   intervals) in this source, unlike the AISI benchmarks used elsewhere in the
   corpus. Guide citations of these benchmark scores should note this
   limitation rather than presenting them with AISI-level rigor.
