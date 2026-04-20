---
source_url: https://www.deeplearning.ai/the-batch/issue-348/
source_type: blog-post
title: "The Batch Issue 348: Anthropic's Claude Mythos Problem, Dark DNA Unveiled, Pitfalls for Assistive Models, Simulating Fluid Dynamics"
author: Andrew Ng / DeepLearning.AI (editorial + reporting)
date_published: 2026-04-10
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#197"
---

# The Batch Issue 348: Andrew Ng on the Coding-Agent Era and Claude Mythos Security Findings

> Two extraction targets from this issue's five stories: (1) Andrew Ng's opening
> editorial letter — five named observations about how coding agents are reshaping
> software engineering roles and economics, with the "PM bottleneck" as a distinct
> new vocabulary item not previously in the corpus; (2) the Claude Mythos Preview —
> Anthropic's autonomous vulnerability-discovery system found thousands of high-
> severity bugs across production operating systems, with 99% unpatched at publication,
> raising a double-edged implication for AI-native verification practices.

## Source Context

- **Type**: blog-post (weekly news digest; DeepLearning.AI's flagship newsletter,
  Issue 348, April 10, 2026)
- **Author credibility**: Andrew Ng is the editorial author of the opening letter.
  He is a co-founder of Coursera, former Baidu Chief Scientist, former Google Brain
  head, founder of DeepLearning.AI and Landing AI — one of the highest-credibility
  voices in applied AI. His editorial reflects informed industry judgment, not
  empirical research. The Claude Mythos section is reported news, not first-party
  Anthropic engineering documentation.
- **Scope**: This issue covers five stories. Extraction targets two: Andrew Ng's
  editorial and the Claude Mythos Preview. Skipped per Prospector guidance:
  AlphaGenome (genomics ML, not AI-native engineering), Walrus physics simulation
  (fluid dynamics, not relevant), and "Pitfalls for Assistive Models" (about
  beauty-standard biases in vision-language models for blind users — not about AI
  coding assistants despite the section title).

## Extracted Claims

### Claim 1: Deciding what to build — not the building itself — is becoming the new bottleneck in software development

- **Evidence**: Andrew Ng's direct editorial observation in the opening letter.
  Framed as one of five trends reshaping software engineering.
- **Confidence**: anecdotal (authoritative editorial opinion; no quantitative data)
- **Quote**: "Deciding what to build, more than the actual building, is becoming a
  bottleneck."
- **Our assessment**: This is the most novel vocabulary item in the source and the
  one most directly actionable for the guide. Ng is naming a structural shift: when
  code generation is commoditized, the constraint on output moves upstream — from
  implementation capacity to specification and product judgment capacity. This
  matches the Zapier posting's "directing and reviewing agent-written code" framing
  (discussion-hn-agentic-coding-jobs) and Shopify's "AI-reflexive" performance
  review criterion (blog-bvp-shopify-ai-playbook), but from a higher vantage
  point: it names the organizational consequence, not just the engineer's new
  job description. The "PM bottleneck" framing implies that product management
  skills — requirements elicitation, stakeholder alignment, deciding what software
  is worth building — become the new rate-limiting resource in AI-assisted teams.

### Claim 2: Writing code by hand and even reading generated code is no longer the primary mode of software interaction

- **Evidence**: Ng's editorial.
- **Confidence**: anecdotal (editorial opinion, not empirical)
- **Quote**: "Writing code by hand and even reading (generated) code is not that
  important, because we can ask an LLM about the code and operate at a higher level."
- **Our assessment**: This is the most provocative claim in the editorial and the
  one that will meet the most resistance from practicing engineers. Ng is asserting
  that the interaction mode is shifting from "read the code" to "ask an LLM about
  the code." The Anthropic transformation study (research-anthropic-ai-transforming-work)
  shows that more than half of Anthropic engineers can only fully delegate 0–20% of
  their work — implying that reading code remains necessary for verification. Ng's
  claim may be forward-looking rather than descriptive of current practice.
  The guide should capture this as an emerging direction rather than a settled reality,
  and pair it with the verification evidence that contradicts its more extreme reading.

### Claim 3: AI is making it economically viable to build software for smaller and smaller audiences, increasing the total volume of custom software

- **Evidence**: Ng's editorial.
- **Confidence**: anecdotal (logic-based claim; no market data cited)
- **Quote**: "There will be a lot more custom applications, because now it's
  economical to write software for smaller and smaller audiences."
- **Our assessment**: The underlying logic is sound: if the cost to build and
  maintain software falls, the minimum viable audience size for a software product
  also falls. This changes team-structure economics — smaller teams can produce
  and maintain more applications in parallel. For the guide's team adoption chapter,
  this is relevant: the AI-native team is not just "faster at the same work" but
  capable of expanding the scope of what software is worth building for internal
  or niche external audiences. The implication for engineering practice is an
  increase in the breadth of maintained codebases per engineer.

### Claim 4: As AI makes coding easier, more people will do it — the developer population will expand rather than contract

- **Evidence**: Ng's editorial, framed as a counter to the "AI will take all
  coding jobs" narrative.
- **Confidence**: anecdotal (historical analogy, no empirical projection)
- **Quote**: "As AI makes coding easier, a lot more people will be doing it."
- **Our assessment**: Ng is invoking the standard "tools democratize access and
  expand the total market" argument. The parallel is to how spreadsheets didn't
  eliminate accountants but expanded financial modeling to non-accountants. This
  is a reasonable directional prediction but speculative over any short-to-medium
  time horizon. The Pragmatic Engineer survey (survey-pragmaticengineer-ai-tooling-2026)
  shows rising adoption among existing engineers; the claim here is specifically
  about expanding the coding population, which the survey does not address.
  Treat as plausible but unvalidated.

### Claim 5: The cost of paying down technical debt is decreasing because AI can handle refactoring

- **Evidence**: Ng's editorial.
- **Confidence**: anecdotal (editorial claim; no case study data)
- **Quote**: "The cost of paying down technical debt is decreasing (since AI can
  refactor for you)."
- **Our assessment**: This is the most directly testable claim in the editorial
  and the one with the most immediate workflow implications. If refactoring cost
  falls, the threshold for "is this debt worth paying down now" shifts. Teams that
  previously deferred cleanup because the cost exceeded the benefit may find that
  threshold reverses. The guide's daily workflows chapter should address this:
  AI-assisted refactoring changes the calculus for technical debt maintenance,
  not just feature development. The risk is over-delegation: the Miller et al.
  study (paper-miller-speed-cost-quality) shows AI-assisted code increases
  complexity and static-analysis warnings — unchecked refactoring via AI could
  introduce new debt while appearing to remove old debt.

### Claim 6: Anthropic's Claude Mythos Preview discovered thousands of high-severity vulnerabilities autonomously across production operating systems

- **Evidence**: Reported facts in the Claude Mythos Preview section. Specific
  systems named: OpenBSD (a flaw undetected for 27 years; enables TCP crash on
  responsive hosts; now patched), Linux kernel (a chain of multiple bugs enabling
  root access and system takeover; now patched). Total: "thousands" of high-severity
  bugs across operating systems and browsers.
- **Confidence**: emerging (Anthropic-reported; specific bugs with patch confirmation
  provide partial independent verification, but "thousands" total is Anthropic's
  own claim without third-party audit)
- **Quote**: "thousands of high-severity bugs autonomously identified across operating
  systems and browsers; 99% remain unpatched"
- **Our assessment**: The specific named bugs — a 27-year-old OpenBSD flaw and a
  Linux kernel privilege escalation chain — are independently verifiable through
  patch tracking. The "thousands" total is Anthropic's claim at pre-launch; the
  99% unpatched rate reflects the gap between discovery and remediation at scale.
  For the guide: this is the most concrete evidence in the corpus that coding-agent
  capability at the frontier can find security-critical bugs at a scale and speed
  that no human team could match. This has two implications: (a) AI-native teams
  should treat autonomous security scanning as a viable production practice, and
  (b) the same capability level that finds subtle bugs can also be expected to
  introduce them. The double-edged nature is the key guide insight.

### Claim 7: 99% of the vulnerabilities found by Claude Mythos remained unpatched at the time of writing

- **Evidence**: Reported statistic from the Claude Mythos Preview section.
- **Confidence**: anecdotal (stated as fact; the "at time of writing" qualifier
  makes this a snapshot, not a stable metric)
- **Quote**: "99% remain unpatched; validation status incomplete"
- **Our assessment**: The 99% unpatched rate is a measure of the scale mismatch
  between AI-enabled discovery and human-capacity remediation — not a measure
  of severity or exploitability. It illustrates that autonomous vulnerability
  discovery can outrun the patch pipeline. For AI-native teams: this is relevant
  when deploying security scanning agents (see blog-cursor-security-agents for
  the Cursor production pattern at 200+ vulnerabilities/week). The ability to find
  bugs at scale is not useful if the remediation pipeline cannot absorb the
  throughput. Reachability analysis and triage automation become prerequisites,
  not options, at this discovery rate.

### Claim 8: Project Glasswing is a defensive consortium — Anthropic + AWS, Apple, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, Nvidia, and 40+ others — organized around AI-enabled vulnerability disclosure

- **Evidence**: Named in the Claude Mythos Preview section with consortium member
  list and financial commitment details.
- **Confidence**: emerging (announced consortium; independent verification of
  membership requires cross-checking with each named organization's public statements)
- **Quote**: N/A (factual reporting; no direct quote)
- **Our assessment**: Project Glasswing represents the industry's first large-scale
  organized response to AI-enabled autonomous vulnerability discovery. The $100M
  in Anthropic API credits (at $25/$125 per million tokens input/output) plus $4M
  in donations to open-source maintainers signals that the remediation problem
  is recognized at organizational scale. The consortium composition — cloud
  providers, security vendors, OS maintainers, financial institutions, hardware
  makers — spans the full stack from kernel to cloud. For AI-native engineering
  teams: Project Glasswing is the institutional signal that autonomous security
  scanning is shifting from research to operational infrastructure. Teams building
  security practices should expect this capability to become standard tooling within
  18–24 months.

### Claim 9: Senior engineer skills are shifting away from syntax and implementation toward judgment — deciding what to build and how to verify it

- **Evidence**: Implicit in Ng's full editorial frame (combining Claims 1–5);
  explicitly framed as an "open question about senior engineer skills" in the
  source.
- **Confidence**: anecdotal (named as an open question, not a settled claim)
- **Quote**: N/A (paraphrased from Ng's editorial framing of open questions)
- **Our assessment**: Ng explicitly flags senior engineer skills as an open question
  rather than a settled claim — credit to him for intellectual honesty about the
  uncertainty. The directional argument is: if building is commoditized, the scarce
  skill becomes judgment about what to build, how to specify it, and how to verify
  the output. This is consistent with Shopify's "comprehension debt" warning (blog-
  bvp-shopify-ai-playbook: "engineers must understand systems two or three layers
  below") and Anthropic's own engineers' skill-atrophy concern (research-anthropic-
  ai-transforming-work: "when producing output is so easy and fast, it gets harder
  to actually take time to learn something"). The guide should present this as an
  open question with directional evidence rather than a settled prediction.

## Concrete Artifacts

### Andrew Ng's Five Observations on the Coding-Agent Era

```
Andrew Ng, "The Batch Issue 348" editorial (April 10, 2026):

Five trends reshaping software engineering:

1. Accessibility of coding
   "As AI makes coding easier, a lot more people will be doing it."

2. Code interaction shift
   "Writing code by hand and even reading (generated) code is not that important,
   because we can ask an LLM about the code and operate at a higher level."

3. Economics of custom software
   "There will be a lot more custom applications, because now it's economical to
   write software for smaller and smaller audiences."

4. The PM Bottleneck
   "Deciding what to build, more than the actual building, is becoming a bottleneck."

5. Technical debt cost reduction
   "The cost of paying down technical debt is decreasing (since AI can refactor
   for you)."

Open questions Ng names: senior engineer skills, competitive advantages for
individuals and companies, new development paradigms, team structure changes,
how AI agents reshape ML engineering workflows.
```

### Claude Mythos Preview: Key Facts

```
Claude Mythos Preview (reported in The Batch Issue 348, April 10, 2026):

SCOPE OF DISCOVERY
  Total:       Thousands of high-severity bugs autonomously identified
  Systems:     Production operating systems and browsers
  Patch status: 99% unpatched at time of writing; validation status incomplete

NAMED VULNERABILITIES (both patched at time of publication)
  OpenBSD flaw:
    Undetected: 27 years
    Impact:     TCP crash on responsive hosts
    Status:     Now patched

  Linux kernel chain:
    Impact:     Multiple bugs enabling root access and system takeover
    Status:     Now patched

PROJECT GLASSWING DEFENSIVE CONSORTIUM
  Lead:         Anthropic
  Members:      AWS, Apple, CrowdStrike, Google, JPMorganChase, Linux Foundation,
                Microsoft, Nvidia, and 40+ others
  Commitment:   $100M in Anthropic API credits
  Pricing:      $25/$125 per million input/output tokens
  Donations:    $4M to open-source maintainers for vulnerability remediation
```

## Cross-References

- **Corroborates**: `discussion-hn-agentic-coding-jobs.md` — Ng's PM bottleneck claim
  (Claim 1) is the editorial-level articulation of what the Zapier posting expressed
  at the job-description level ("directing and reviewing agent-written code, not
  writing it by hand"). The Zapier posting names the new competency profile; Ng names
  the structural reason it is emerging. Together they make a stronger case than either
  alone. Ng's "senior engineer judgment" framing (Claim 9) also extends Claim 8 of
  the HN discussion ("failure modes are poorly understood; 'built mitigations' is
  doing heavy lifting in job descriptions").

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` — Claim 9 (senior engineer
  skills shifting toward judgment) directly echoes Shopify's "comprehension debt"
  warning: Farhan Thawar's "the brain is a muscle" quote and Ng's framing of
  judgment as the scarce resource are making the same claim from two different
  vantage points (operational executive vs. editorial synthesis). Ng's PM bottleneck
  (Claim 1) also aligns with Shopify's code review bottleneck (review becoming
  the constraint as generation volume grows) — different manifestations of the
  same shift.

- **Corroborates**: `research-anthropic-ai-transforming-work.md` — The skill-atrophy
  concern in the Anthropic transformation study ("when producing output is so easy
  and fast, it gets harder to actually take time to learn something") converges with
  Ng's Claim 9 framing of senior engineer skills as an open question. Two of the
  most AI-optimistic voices in the field (Anthropic engineers, Andrew Ng) are
  independently flagging the judgment/skill question as unresolved. That convergence
  is more significant than either source alone.

- **Corroborates**: `blog-cursor-security-agents.md` — The Claude Mythos findings
  (thousands of vulnerabilities found autonomously; Claim 6) and Cursor's production
  security fleet (200+ vulnerabilities caught per week; Claim 9 in that note) are
  corroborating data points at very different scales. Cursor demonstrates autonomous
  vulnerability discovery is viable at production PR-review scale. Mythos extends
  the claim to OS-level autonomous discovery at much greater depth. Both point toward
  the same conclusion: AI-native security scanning at scale is feasible and is moving
  from research to operational infrastructure.

- **Extends**: `discussion-hn-agentic-coding-jobs.md` — Ng's PM bottleneck framing
  (Claim 1) is vocabulary not previously in the corpus. "PM bottleneck" names the
  upstream constraint that the Zapier posting implied but did not explicitly label.
  The HN discussion captures "what the job description looks like"; Ng captures
  "why that job description is structured that way."

- **Contradicts**: None filed. Ng's Claim 2 ("reading generated code is not that
  important") is in tension with the verification evidence across multiple notes
  (research-anthropic-ai-transforming-work, paper-miller-speed-cost-quality,
  blog-bvp-shopify-ai-playbook) — but Ng frames this as a forward-looking trend
  and names it an open question, so it does not rise to a materially opposing claim
  that would require a contradiction issue. The tension is captured in the Claim 2
  assessment above.

- **Novel**:
  - **PM bottleneck** as a named concept: no other source in the corpus uses this
    vocabulary item or explicitly frames product management judgment as the
    rate-limiting resource in AI-assisted engineering.
  - **Claude Mythos / Project Glasswing** details: the specific vulnerability
    findings (27-year OpenBSD flaw, Linux kernel privilege escalation chain, 99%
    unpatched rate) and the Glasswing consortium composition are not documented
    elsewhere in the corpus.
  - **Economics of small-audience custom software** (Claim 3): the argument that
    falling development cost expands the viable audience size threshold for custom
    software — and thus the total breadth of codebases per team — is not explicitly
    made in any other corpus source.
  - **Technical debt cost reduction** (Claim 5): while AI-assisted refactoring is
    mentioned in other sources, Ng's framing of this as a structural change in the
    technical debt calculus (not just a productivity improvement) is new vocabulary.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Ng's PM bottleneck (Claim 1) should anchor any
  section on how senior engineers' daily work is shifting. The claim is: the bottleneck
  is no longer "can we write the code?" but "can we decide what code to write?" This
  reframes the guide's daily workflow advice: the highest-value practice is not faster
  code generation but better specification and product judgment upstream of generation.
  Pair with the Zapier posting (discussion-hn-agentic-coding-jobs) as a complementary
  signal — editorial synthesis (Ng) plus job-market evidence (Zapier) make a stronger
  case than either alone.

- **Chapter 01 (Daily Workflows)**: Claim 5 (technical debt cost decreasing) changes
  the maintenance decision calculus. The guide should explicitly state: the threshold
  for "is this refactoring worth doing now?" has shifted downward — teams should
  revisit their debt triage criteria. Caveat with the Miller et al. finding
  (paper-miller-speed-cost-quality) that unchecked AI refactoring increases complexity
  — AI-assisted refactoring requires the same verification discipline as AI-assisted
  feature development.

- **Chapter 03 (Safety and Verification)**: The Claude Mythos findings (Claims 6–7)
  are the most concrete evidence in the corpus that coding-agent capability is
  sufficient to discover OS-level security vulnerabilities at scale. The guide
  implication is double-edged: (a) autonomous security scanning is a viable practice
  for AI-native teams; (b) models capable of finding subtle multi-step vulnerability
  chains are also capable of introducing them. Any chapter section on verification
  should name this dynamic explicitly — the same capability that makes AI-assisted
  development productive is the capability that makes AI-generated code require
  more rigorous security review, not less. Pair with blog-cursor-security-agents
  for the production implementation pattern.

- **Chapter 03 (Safety and Verification)**: Claim 7 (99% unpatched rate) illustrates
  the discovery-vs-remediation throughput gap. The guide should advise teams deploying
  security scanning agents to plan for triage volume, not just discovery. Reachability
  analysis (blog-cursor-security-agents, Claim 6) and structured output formatting
  are prerequisites for managing the remediation pipeline at scale.

- **Chapter 05 (Team Adoption)**: Claim 3 (economics of small-audience custom software)
  implies that AI-native teams should expect to maintain a broader portfolio of
  applications per engineer than pre-AI teams. This changes team structure planning:
  more surfaces to maintain, more context to track, more harness configurations to
  manage. Teams planning AI adoption should factor in the increased breadth of
  maintained software, not just the increased depth of any single application.

- **Chapter 05 (Team Adoption)**: Claim 8 (Project Glasswing) is the institutional
  signal that autonomous security scanning is becoming standard tooling. Teams building
  AI-native security practices should watch Project Glasswing as the leading indicator
  of what "table stakes" looks like within 18–24 months.

## Extraction Notes

- This is a weekly news digest, not a practitioner deep-dive. Andrew Ng's editorial
  is informed opinion at the level of industry synthesis, not empirical research.
  Claims carry authority from Ng's credibility and position, not from data. Confidence
  grades reflect this: "anecdotal" throughout the editorial section, "emerging" for
  the Mythos claims where named vulnerabilities provide partial independent verification.
- The Claude Mythos Preview section is secondary reporting on Anthropic's pre-launch
  announcement, not primary Anthropic documentation. The "thousands" total is Anthropic's
  own claim; independent verification of the full scope would require the Glasswing
  disclosure pipeline.
- Three Prospector triage comments were on this issue with slightly different guidance.
  The third comment (most detailed) was used as the primary guide: skip "Pitfalls for
  Assistive Models" (blind users + beauty biases, not coding), skip AlphaGenome and
  Walrus. The second comment suggested extracting the Assistive Models section for
  the trust-verification angle; this was not extracted because the source content
  specifically concerns bias in vision models for blind users — the mapping to AI-native
  engineering trust/verification is too indirect to justify inclusion.
- No sub-pages followed; the newsletter is a self-contained HTML page. Full text
  retrieved in one WebFetch pass.
