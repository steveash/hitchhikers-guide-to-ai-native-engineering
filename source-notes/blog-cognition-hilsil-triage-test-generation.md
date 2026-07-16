---
source_url: https://cognition.com/blog/how-to-automate-failure-triages-and-10x-test-generation-what-weve-learned-deploying-ai-across-hilsil-workflows
source_type: blog-post
title: "How to Automate Failure Triages and 10x Test Generation: What We've Learned Deploying AI Across HIL/SIL Workflows"
author: The Cognition Team
date_published: 2026-05-11
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1930"
---

# How to Automate Failure Triages and 10x Test Generation: What We've Learned Deploying AI Across HIL/SIL Workflows

> Cognition's case-study account of deploying Devin across multiple automotive
> OEMs on hardware-in-the-loop/software-in-the-loop (HIL/SIL) workflows — the
> first source in this corpus documenting agentic patterns in embedded/
> automotive validation, with named customers (RV Tech, Mercedes), concrete
> dollar and time-savings figures, a three-stage AI-adoption maturity model,
> and an explicit admission of where the approach still fails (regulatory
> language mapping, proprietary HIL software integration).

## Source Context

- **Type**: blog-post (cognition.com/blog; company blog, byline "The
  Cognition Team," published 05.11.26 per the page's own byline format,
  i.e. 2026-05-11, consistent with the MM.DD.YY byline convention already
  documented for this domain in `blog-cognition-auto-triage.md`)
- **Author credibility**: Published directly by Cognition, the company that
  builds and sells Devin — this is a vendor case-study/marketing channel,
  not an independent account. The specific quantified claims are attributed
  to named customers (RV Tech, a "large US automotive company" left
  unnamed, and one further unnamed team), with one customer quote directly
  attributed by name and title (Wassym Bensaid, Co-CEO & CTO, RV Tech). No
  independent, non-Cognition-hosted verification of any figure exists in
  this source.
- **Scope**: Covers three workflow areas — automated failure-triage
  pipelines, test-generation/requirement-mapping acceleration, and
  HIL-to-SIL test conversion — plus a three-stage organizational
  AI-maturity model and a closing "what's still out of reach" section
  naming two concrete current limitations. Does NOT cover: the underlying
  model/version behind Devin at time of writing, methodology for any of
  the quoted metrics (baseline period, ticket-severity mix, headcount
  before/after), false-positive or triage-accuracy rates, cost of running
  the described automations, or any customer's full deployment timeline.

## Extracted Claims

### Claim 1: Cognition has deployed Devin across multiple automotive OEMs on HIL/SIL workflows over the past year, working with named customers including RV Tech and Mercedes
- **Evidence**: Opening framing paragraph naming the deployment history and
  two customers.
- **Confidence**: anecdotal (vendor-stated deployment history and customer
  list; no count of total OEMs, no deployment dates beyond "past year")
- **Quote**: "Over the past year, we've deployed Devin across multiple
  OEMs on HIL/SIL workflows."
- **Our assessment**: This is the source's scope-setting claim — it
  establishes automotive HIL/SIL as a real, multi-customer deployment
  vertical for Devin rather than a single pilot. Mercedes is named only
  once, in this framing sentence, and receives no further claims, quotes,
  or metrics elsewhere in the article — treat the Mercedes mention as an
  unelaborated customer-name drop, not as evidence of any specific
  Mercedes outcome.

### Claim 2: The persistent structural problem in this domain is that requirements and ticket volumes grow while engineering capacity stays flat, and adoption of AI across HIL/SIL workflows varies significantly with few effective examples to date
- **Evidence**: Direct problem-framing statement, presented as the
  motivating gap the rest of the post addresses.
- **Confidence**: anecdotal (industry-condition assertion, no data on
  ticket-volume growth rate or capacity-stagnation figures)
- **Quote**: "The problem remains - requirements and ticket volumes
  continue to grow, while engineering capacity hasn't kept up."
- **Our assessment**: A plausible but unverified industry-condition claim
  used to motivate the case study — read as a problem statement from the
  vendor selling the fix, not an independently surveyed industry finding.

### Claim 3: One team scheduled Devin to trigger daily after code-complete, running a GitLab pipeline that flashes tests onto the HIL bench, with Devin triaging outputs and sending reports to engineers before they arrive — reclaiming 2,000-4,000 engineering hours per month across roughly 4,000 tickets, equating to $1.7M-$3.5M in annual savings
- **Evidence**: Named workflow mechanism (schedule → GitLab pipeline → HIL
  bench flash → Devin triage → report) paired with a specific, quoted
  savings figure attributed to that one team.
- **Confidence**: anecdotal (single-team, self-reported, unaudited figure;
  no baseline headcount, no hourly-rate assumption disclosed for the
  dollar conversion, no time period specified beyond "per month")
- **Quote**: "This team 'reclaimed 2K–4K engineering hours per month
  across ~4,000 tickets, equating to $1.7M–$3.5M in annual savings.'"
- **Our assessment**: This is the single largest dollar figure in the
  source and the most quotable metric, but it is an unaudited,
  single-customer, vendor-hosted number with no disclosed hourly-rate
  basis for the dollar conversion or ticket-severity mix — cite as a
  self-reported existence proof of large potential savings from scheduled
  failure-triage automation, not as a generalizable ROI rate for the
  practice.

### Claim 4: A separate deployment used tens of parallel Devin agents (one agent per ticket) to triage 52 tickets in under 15 minutes, with engineers freed to work on other tasks while agents triage in parallel because Devin runs cloud-based
- **Evidence**: Direct quote giving a specific parallel-agent count range
  and a bounded time/ticket-count outcome.
- **Confidence**: anecdotal (single observed batch, no data on how
  representative 52 tickets in 15 minutes is versus typical throughput,
  no accuracy/correctness rate for the resulting triage reports)
- **Quote**: "tens of parallel agents triaged 52 tickets in less than 15
  minutes."
- **Our assessment**: This is a concrete, citable instance of one-agent-
  per-ticket parallel decomposition applied to triage specifically (as
  opposed to feature implementation or generic incident investigation),
  and it names cloud execution as the structural enabler of that
  parallelism — the same "you can't do this on a laptop" logic already
  documented for testing workloads (see Cross-References → Corroborates).
  No figure is given for triage correctness, so "52 tickets in 15 minutes"
  should be read as a throughput claim only, not a quality claim.

### Claim 5: At RV Tech, vehicle issues arriving in Slack auto-trigger Devin to pull logs, run diagnostics, and deliver structured triage reports
- **Evidence**: Direct workflow description naming the trigger surface
  (Slack) and the resulting agent actions (pull logs, run diagnostics,
  structured report).
- **Confidence**: emerging (named customer, named trigger mechanism and
  action sequence; no accuracy or adoption-rate figure for this specific
  workflow)
- **Quote**: "At RV Tech, when a vehicle issue arrives in Slack, Devin is
  auto-triggered to pull logs, run diagnostics, and deliver a structured
  triage report for teams to review."
- **Our assessment**: A concrete, named-customer instance of Slack-
  triggered autonomous triage in an automotive/embedded context — extends
  the general "Devin watches a Slack channel and triages" pattern already
  documented for software incidents (see Cross-References → Extends) into
  a hardware-adjacent domain (vehicle issue reports rather than software
  alerts).

### Claim 6: Separating a dedicated test-planning agent (mapping requirements to coverage gaps) from a test-implementation agent (generating code) improved both quality and speed for a large US automotive company, cutting test-development time from half a week to one day with roughly 80% of generated tests passing
- **Evidence**: Named architectural pattern (planning agent separated from
  implementation agent) paired with a specific before/after time figure
  and a pass-rate figure, both attributed to one unnamed customer.
- **Confidence**: anecdotal (single customer, self-reported, unaudited
  figures; "80% passing" has no denominator disclosed — passing on first
  generation? after human fixes? no baseline pass rate before the
  planning/implementation split is given either)
- **Quote**: "Their program 'test development took 1 day instead of half a
  week, with ~80% of generated tests passing.'"
- **Our assessment**: The planning/implementation separation is the more
  transferable technique here — a specific architectural claim (don't ask
  one agent to both decide what to test and write the test) that is more
  actionable than the raw time/pass-rate figures, which lack denominators
  and a disclosed baseline. This is a domain-specific instance of a
  task-decomposition pattern independent of automotive HIL/SIL
  specifically.

### Claim 7: Reusable, modular "Playbooks" encoding one engineer's framework/subsystem-specific test knowledge let a team immediately generate tests from that encoded knowledge, and in multiple cases Devin identified conflicting logic between requirements and flagged it to human reviewers for confirmation
- **Evidence**: Direct mechanism description (one engineer authors a
  Playbook, team reuses it) plus a named secondary behavior (flagging
  requirement conflicts for human confirmation).
- **Confidence**: emerging (specific, named mechanism and behavior; no
  count of how many conflicting-requirement flags were raised, no
  false-positive rate for the conflict detection)
- **Quote**: "One engineer works out the initial Playbook, and the rest of
  the team can immediately generate tests from that encoded knowledge."
- **Our assessment**: "Playbook" here names a specific artifact — codified,
  reusable domain/framework knowledge that amortizes one expert's setup
  cost across a team — conceptually adjacent to the deterministic "testing
  skill" artifact already documented for Devin's computer-use testing (see
  Cross-References → Extends), but applied to requirement-to-test mapping
  rather than UI setup steps. The requirement-conflict-flagging behavior is
  a specific instance of an agent surfacing an inconsistency for human
  judgment rather than silently resolving or ignoring it.

### Claim 8: Applying scheduled pipelines, parallel triage, and Playbook-based generation together, RV Tech achieved a 10x increase in test-generation throughput, from 1-2 tests/day manually to 10-15 tests/day with AI support
- **Evidence**: Direct before/after throughput figure attributed to RV
  Tech, presented as the cumulative result of the practices described in
  Claims 3-7.
- **Confidence**: anecdotal (single customer, self-reported, unaudited
  before/after rate; no data on whether test quality/coverage held
  constant at the higher throughput, and no time period over which the
  10-15/day rate was sustained)
- **Quote**: "For RV Tech, implementing these best practices led to a 10x
  increase in test-generation, from 1-2/day manually to 10-15 tests/day
  with AI-support."
- **Our assessment**: This is the figure named in the article's own title
  and the headline number of the source. It is a throughput claim only —
  the source does not report whether the 10-15/day tests are equivalent in
  scope, depth, or maintenance burden to the 1-2/day manually-written
  tests they're compared against, which matters for judging whether this
  is a genuine 10x productivity gain or a shift toward higher volume/lower
  average test quality.

### Claim 9: HIL tests are slow (often 1-8 hours per run) and constrained by bench availability; one team had only 150 SIL tests written against a target of 700-1,000 needed HIL-equivalent tests per program, motivating a push to convert bottlenecked HIL tests to SIL equivalents using Devin
- **Evidence**: Direct problem statement (HIL run-time range, one team's
  SIL-test coverage gap) followed by the stated mechanism (Devin converts
  HIL tests to SIL equivalents).
- **Confidence**: anecdotal (single team's coverage-gap figures; no data
  on how many HIL-to-SIL conversions Devin has actually completed, no
  accuracy/equivalence-verification rate for converted tests)
- **Quote**: "For one team we spoke to, only 150 SIL tests had been written
  against 700–1,000 HIL tests needed per program due to staffing capacity."
- **Our assessment**: This names a specific, checkable coverage gap (150
  vs. 700-1,000) that motivates HIL-to-SIL conversion as a capacity
  problem rather than a pure quality problem — a team isn't necessarily
  choosing SIL over HIL for accuracy reasons, but because bench-bound HIL
  testing cannot scale to the needed test count. No figure is given for
  how many of the needed tests Devin has actually converted, so the
  claim establishes motivation and mechanism, not a completed-conversion
  count.

### Claim 10: Cognition describes a three-stage organizational AI-maturity model for HIL/SIL adoption — Stage 1 "AI-Supported" (Devin reviews logs and documents root-cause hypotheses for engineer review), Stage 2 "Scheduled Automations" (time- and event-driven Devin agents proactively triage and open Jira issues with fix PRs attached before engineers arrive), and Stage 3 "Self-Improving Playbooks Shared Across the Organization" (parallel Devin agents diagnose issues and improve their own playbooks between runs, shared company-wide)
- **Evidence**: Three explicitly named and ordered stages, each with a
  "What Changes" summary and at least one concrete workflow example.
- **Confidence**: emerging (a named, ordered framework with concrete
  per-stage examples; no data on what fraction of Cognition's automotive
  customers sit at each stage, no time-to-progress figures between stages)
- **Quote**: "Stage 3: Self-Improving Playbooks Shared Across the
  Organization ... As Devin sees issues, it improves its own playbook
  between runs to increase its speed and accuracy."
- **Our assessment**: This three-stage model (human-reviewed AI assistance
  → proactive scheduled/event-driven automation → agents recursively
  improving shared playbooks across the org) is a reusable framework for
  describing organizational AI-adoption progression that is more
  structured than a simple "before/after" comparison — it gives the guide
  a named vocabulary for talking about where a team sits on an adoption
  curve. Stage 3's specific claim — agents improving their own playbook
  between runs without a human editing it — is the most novel and least
  substantiated part of the model; no example shows a specific playbook
  edit an agent made or how that edit was validated before being trusted
  company-wide.

### Claim 11: Two named limitations remain out of reach: mapping broad regulatory/compliance language (e.g. "limitations on braking torque") to the correct code sections is difficult because compliance standards are written for humans rather than machines, and understanding proprietary HIL software requires Cognition's own Forward Deployed Engineering team to build customer-specific integrations
- **Evidence**: Direct admission under an explicit "What's Still Out of
  Reach" heading, naming both limitations and, for the second, naming the
  internal team required to work around it.
- **Confidence**: settled (first-party admission of current, unresolved
  limitations — a vendor naming what its own product cannot yet do
  carries more weight than a positive capability claim, since it works
  against promotional interest)
- **Quote**: "What remains hard is mapping broad regulatory language such
  as 'limitations on braking torque' to the right sections of code.
  Compliance standards are written for humans, not machines, and bridging
  that gap is still a challenge."
- **Our assessment**: This is the most transferable negative-knowledge
  claim in the source: natural-language regulatory/compliance text does
  not map cleanly to code the way an engineering requirement does, because
  compliance language is written for human interpretation and judgment
  rather than as a specification. The second limitation (proprietary HIL
  software requiring a dedicated Forward Deployed Engineering team per
  customer) is a concrete admission that this deployment pattern is not
  self-service — a nontrivial amount of the described automation depends
  on Cognition's own custom integration work per customer stack, which
  the headline metrics (Claims 3, 6, 8) do not disclose as a cost.

## Concrete Artifacts

### Three-stage AI-maturity model (from the article, verbatim structure)

```
Source: cognition.com/blog/how-to-automate-failure-triages-and-10x-test-
generation-what-weve-learned-deploying-ai-across-hilsil-workflows

Stage 1: AI-Supported
- Engineers use Devin to review error logs for HIL failure investigation
- Devin iterates on root cause hypotheses, pulls data to validate/invalidate
- Root cause analysis documented and delivered for engineer review
- What Changes: investigations proceed faster with systematic evidence review

Stage 2: Scheduled Automations
- Example: Devin scheduled to run nightly, auto-triggering HIL tests,
  correlating failure logs against diagnostic protocols, posting root
  cause analysis to Slack before engineers arrive
- Example: Devin continuously polls for new crash reports, deduplicated
  against known issues, reviews codebase, drafts root cause analysis,
  creates Jira issues often with fix PRs attached
- What Changes: time-driven and event-driven Devin agents proactively
  respond to issues

Stage 3: Self-Improving Playbooks Shared Across the Organization
- Devin polls logs; parallel Devin agents diagnose each issue and create
  fix PRs
- Devin improves its own playbook between runs to increase speed/accuracy
- What Changes: teams set up agents to recursively improve playbooks for
  each V-model part across the company
```

### Named customer metrics (from the article, verbatim quotes)

```
Source: cognition.com/blog/how-to-automate-failure-triages-and-10x-test-
generation-what-weve-learned-deploying-ai-across-hilsil-workflows

- "reclaimed 2K–4K engineering hours per month across ~4,000 tickets,
  equating to $1.7M–$3.5M in annual savings" (one team, scheduled
  failure-triage pipeline)
- "tens of parallel agents triaged 52 tickets in less than 15 minutes"
  (separate deployment, parallel triage)
- "test development took 1 day instead of half a week, with ~80% of
  generated tests passing" (large US automotive company, planning/
  implementation agent separation)
- "a 10x increase in test-generation, from 1-2/day manually to 10-15
  tests/day with AI-support" (RV Tech)
- "For one team we spoke to, only 150 SIL tests had been written against
  700–1,000 HIL tests needed per program due to staffing capacity"
  (HIL-to-SIL motivation)
```

### Customer testimonial, full attribution

```
Source: cognition.com/blog/how-to-automate-failure-triages-and-10x-test-
generation-what-weve-learned-deploying-ai-across-hilsil-workflows

"This will help us be way more predictable in our execution, deliver
software with way higher quality, and dramatically increase the velocity
of our engineering team."
— Wassym Bensaid, Co-CEO & CTO, RV Tech
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-auto-triage.md` Claim 3 (Devin "spin[s] up sub-Devins
    to investigate in parallel") and Claim 9 (named trigger surfaces
    including Slack, schedules, webhooks, applicable to "investigating
    production alerts" and "looking into failed CI runs"). This source's
    Claim 4 (tens of parallel agents, one per ticket, 52 tickets in <15
    minutes) and Claim 3/Claim 10's scheduled-nightly-triage examples are
    the same parallel-decomposition and scheduled-trigger mechanisms
    documented in `blog-cognition-auto-triage.md`, instantiated with named
    customers and concrete throughput numbers in a hardware/automotive
    domain rather than a general software-incident domain. Together they
    move the proactive-triage pattern from a feature description (Auto-
    Triage) toward disclosed, if unaudited, customer outcomes in a second
    vertical.
  - `blog-cursor-amplitude-autonomous-pipeline.md` Claim 1 (event-driven
    Slack→Linear→PR pipeline fully delegating customer-facing bug triage
    to cloud agents) and Claim 3 (hourly cron automations for continuous
    migration work) — this source's Stage 2 "Scheduled Automations"
    examples (nightly HIL-triggered triage, continuous crash-report
    polling with Jira issue + fix PR creation) are the same scheduled/
    event-driven agent automation pattern, independently reported by a
    different vendor (Cognition/Devin vs. Cursor/Amplitude) in a
    different domain (automotive hardware validation vs. SaaS product
    engineering) — evidence the pattern generalizes across vendors and
    verticals, not evidence of a shared mechanism.
  - `blog-cognition-verifying-agentic-development.md` Claim 3 (engineers
    observed running 10-20 Devins in parallel on cloud infrastructure,
    "something you simply can't do on a single laptop") — this source's
    Claim 4 (tens of parallel triage agents, cloud-based, explicitly
    framed as freeing engineers to do other work while agents triage in
    parallel) corroborates that cloud execution, not local execution, is
    what the described parallel-agent scale depends on, in a different
    task category (test-generation/self-verification vs. failure triage).

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under matching conditions.

- **Extends**:
  - `blog-cognition-auto-triage.md` Claim 5 (Modal's single named-customer
    validation quote for unprompted, autonomous incident triage) — this
    source extends that single-anecdote validation model to three named/
    unnamed automotive customers (RV Tech named throughout with a named
    executive quote; a "large US automotive company" and other teams left
    unnamed) with attached dollar and throughput figures, moving the
    evidentiary base from one qualitative quote toward multiple
    quantified (if unaudited) customer outcomes.
  - `blog-cognition-verifying-agentic-development.md` Claim 7 (repeated
    setup steps extracted into a deterministic "testing skill" stored in
    the repo, which Devin can propose extending via a one-click PR when it
    learns a new step) — this source's Claim 7 ("Playbooks" encoding one
    engineer's framework/subsystem test knowledge, reused by the rest of
    the team to generate tests) is the same underlying idea — codify a
    domain expert's operational knowledge once, reuse it broadly — applied
    to requirement-to-test-code mapping rather than UI setup automation.
    This source's Claim 10 (Stage 3: Devin "improves its own playbook
    between runs to increase speed and accuracy") goes one step further
    than the testing-skill mechanism in the cited note by describing the
    agent editing the shared knowledge artifact itself rather than only
    proposing an addition for human approval — a meaningfully higher-
    autonomy variant of the same compounding-knowledge pattern, and one
    the source gives no validation mechanism for (no example of a
    specific playbook edit, or how a bad edit would be caught).

- **Novel**: This is the first source in this corpus documenting agentic
  deployment in automotive hardware-in-the-loop/software-in-the-loop
  (HIL/SIL) validation workflows — a regulated, safety-adjacent embedded
  domain distinct from the general software engineering and SaaS contexts
  that dominate the rest of the corpus. Specifically new: the HIL-to-SIL
  test conversion pattern (Claim 9); the three-stage organizational
  AI-maturity model (Claim 10), which is a more structured adoption-
  progression framework than anything else currently in the corpus; the
  planning-agent/implementation-agent separation for test generation
  (Claim 6); and the explicit admission that regulatory/compliance
  language resists code-mapping because it is "written for humans, not
  machines" (Claim 11) — a specific, named boundary condition for
  requirement-to-code automation that no existing source note documents.

## Guide Impact

- **Chapter 04/05 (Proactive / Self-Triggered Agents)**: Add Claims 3, 4,
  5, and the Stage 2 examples in Claim 10 as a second-vertical case study
  (automotive HIL/SIL, alongside the existing software-incident examples
  from `blog-cognition-auto-triage.md`) for scheduled and event-triggered
  autonomous triage, with named customer throughput figures. Flag clearly,
  as with the sibling Cognition sources already in the corpus, that all
  dollar/hour figures are single-customer, self-reported, and unaudited —
  cite as existence proof of large potential value, not as a
  generalizable savings rate.
- **Chapter 05 (Testing & Verification / Test Generation)**: Add Claim 6
  (separate planning agent from implementation agent for test generation)
  and Claim 7 (reusable "Playbooks" encoding one engineer's test-authoring
  knowledge per framework/subsystem) as concrete, transferable techniques
  for scaling test generation beyond headcount — distinct from the
  self-testing/computer-use verification techniques already sourced from
  `blog-cognition-verifying-agentic-development.md`, since this source is
  about generating new tests from requirements rather than an agent
  verifying its own code changes.
- **Chapter 02 (Harness Engineering / Organizational Adoption)**: Propose
  the three-stage AI-maturity model (Claim 10: AI-Supported → Scheduled
  Automations → Self-Improving Playbooks Shared Across the Organization)
  as a named framework for describing where a team sits on an
  agentic-adoption curve, if the guide has or adds a section on
  organizational rollout maturity. Flag Stage 3's "agents edit their own
  shared playbook between runs" claim as the least substantiated part of
  the model — no validation mechanism is described for agent-made edits
  to a knowledge artifact other agents and humans will subsequently rely
  on.
- **Chapter 05 (Limitations)**: Add Claim 11 (regulatory/compliance
  language resists code-mapping; proprietary HIL software integration
  requires vendor-side custom engineering per customer) as a concrete,
  vendor-admitted boundary condition — useful as a counterweight to the
  headline throughput/savings metrics elsewhere in this source, and as a
  specific instance of the general "natural-language requirements don't
  map cleanly to code" problem in a regulated domain.

## Extraction Notes

- The article was fetched via WebFetch requesting full verbatim section-
  by-section text; the returned content covered the complete article
  (title, byline/date, all six subsections under "What We've Learned," all
  three maturity-model stages under "What We've Seen," the "What's Still
  Out of Reach" section, and the closing testimonial/call-to-action) with
  no indication of truncation or missing sections. No sub-pages were
  linked from the article body worth following — the only outbound links
  visible are site navigation and a closing invitation to contact
  Cognition, neither of which elaborates on the case-study content itself.
- The publish date is read from the page's own byline ("05.11.26"),
  interpreted as MM.DD.YY consistent with the byline format already
  documented for this domain in `blog-cognition-auto-triage.md` and
  `blog-cognition-verifying-agentic-development.md`, i.e. 2026-05-11.
- Two customers are named explicitly (RV Tech, referenced throughout with
  a named-executive testimonial; Mercedes, named once in the opening
  sentence with no further elaboration anywhere in the article). Two
  further customers/teams are described but left unnamed ("a large US
  automotive company," and additional unattributed "one team"/"another
  team" examples in the maturity-model section) — this note does not
  invent identities for them and flags each instance's anonymity in the
  relevant claim.
- No quantitative claim in the source discloses a measurement methodology,
  baseline period, or audit — every dollar, hour, and pass-rate figure is
  a single-customer, vendor-hosted, self-reported number. This is the
  basis for the `confidence_overall: emerging` rating (a vendor case study
  with multiple named-customer, specific, checkable-in-principle metrics,
  but zero independently audited figures) — consistent with the
  confidence rating already applied to the two sibling Cognition source
  notes in this corpus.
- Cross-references verified before writing: re-read `blog-cognition-
  auto-triage.md` in full and confirmed Claims 3, 5, and 9 by number and
  content; re-read `blog-cognition-verifying-agentic-development.md` in
  full and confirmed Claims 3 and 7 by number and content; re-read
  `blog-cursor-amplitude-autonomous-pipeline.md` in full and confirmed
  Claims 1 and 3 by number and content. No claim number was guessed or
  approximated.
- No contradiction meeting MINER.md §4a's filing bar was found — this
  source corroborates and extends existing claims about proactive/
  scheduled agents and compounding operational knowledge, applied to a new
  vertical, but does not oppose any existing source note's claim under
  matching conditions. No contradiction issue filed.
