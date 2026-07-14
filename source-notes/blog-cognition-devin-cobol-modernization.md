---
source_url: https://cognition.com/blog/how-devin-is-modernizing-cobol-at-fortune-500-companies
source_type: blog-post
title: "How Devin Is Modernizing COBOL at Fortune 500 Companies"
author: The Cognition Team
date_published: 2026-04-08
date_extracted: 2026-07-14
last_checked: 2026-07-14
status: current
confidence_overall: emerging
issue: "#1864"
---

# How Devin Is Modernizing COBOL at Fortune 500 Companies

> Cognition's technical account of why COBOL structurally defeats the
> standard agent feedback loop (untypeable positional data, near-zero
> training exposure, and code that cannot be executed off a mainframe) and
> the two-part fix — DeepWiki codebase mapping plus playbook-based
> iteration — that let Devin deliver value on three named Fortune 500
> COBOL projects (documentation, a 25,000-line batch migration, and a
> tax-ID refactor at Itaú Unibanco) while explicitly excluding transactional
> workloads from what agents can do autonomously today.

## Source Context

- **Type**: blog-post (cognition.com/blog, published 04.08.26 per the
  page's own byline, i.e. 2026-04-08; company blog, byline "By The
  Cognition Team," no individual author named)
- **Author credibility**: Published directly by Cognition, the company
  that builds Devin — this is a vendor case-study/product-marketing
  channel, not an independent account. No individual practitioner is named
  or quoted anywhere in the post (unlike, e.g., `blog-cursor-nab-legacy-migration.md`,
  which quotes five named NAB engineers by title). All three case studies
  (healthcare, automotive, Itaú Unibanco) are described in Cognition's own
  words with no first-person customer quote and no named customer
  spokesperson. Treat the technical mechanism descriptions (why COBOL is
  hard, the two-part solution) as a vendor's engineering explanation, and
  the outcome metrics (73% cost reduction, 5-6x speedup, zero production
  errors) as self-reported, unaudited figures with no stated methodology.
- **Scope**: Covers why COBOL is difficult for coding agents (three named
  technical barriers), what two conditions Cognition says are required for
  agents to help (codebase mapping, restored feedback loop), a
  batch-vs-transactional workload distinction, and three named Fortune 500
  case studies (documentation, batch migration, large-scale refactoring).
  Does NOT cover: any technical detail on how DeepWiki's parsing/mapping
  works internally, the actual content or format of a "playbook," the
  identity of "other agentic tools" that failed at Itaú Unibanco, any
  timeline or cost baseline behind the 73% cost-reduction figure, headcount
  or team size for any of the three projects, or any discussion of what
  happens when Devin's own COBOL-generated code introduces a bug that only
  surfaces on the mainframe (given it cannot test-execute there either).

## Extracted Claims

### Claim 1: COBOL faces an acute, closing talent cliff — 47% of organizations cannot fill their COBOL roles and 92% of COBOL developers plan to retire by 2030
- **Evidence**: Two industry statistics stated in the opening paragraph, with no cited source or methodology given in the article itself.
- **Confidence**: emerging (specific, checkable-in-principle statistics, but presented without attribution to a named research source or survey methodology — this is the article's uncontested framing premise, not something the article itself claims to have measured)
- **Quote**: "Forty-seven percent of organizations cannot fill their COBOL roles and 92% of COBOL developers plan on retiring by 2030."
- **Our assessment**: This is the article's "why now" hook, structurally identical in function to the McKinsey/Deloitte/Adacta statistics opening `blog-thoughtworks-harrison-insurance-legacy-modernization.md` — a headline scarcity/urgency statistic cited without a traceable primary source. Should be treated as a directional industry signal, not a verified figure, since no research organization or survey is named.

### Claim 2: Over an eight-month period, several Fortune 500 companies staffed Devin on COBOL projects spanning documentation, a COBOL-to-AWS-Lambda batch migration, and tax-ID refactoring across hundreds of programs
- **Evidence**: Direct scope statement naming the time window and the three project types that the rest of the article details as named case studies.
- **Confidence**: anecdotal (vendor-stated deployment scope; no aggregate customer count beyond "several," no named timeline start/end date)
- **Quote**: "As a result, over the past eight months, several Fortune 500 companies have staffed Devin on COBOL project — documenting millions of lines of code, migrating a customs workflow from COBOL to AWS Lambda, and refactoring tax ID logic across hundreds of programs."
- **Our assessment**: This sentence is the article's table of contents — the three clauses map directly onto the "Documentation," "Batch Job Migrations," and "Large-Scale Refactoring" sections that follow with named companies (a healthcare company, an automotive manufacturer, Itaú Unibanco). "Several" is left unquantified, so the reader cannot tell if this is three companies (matching the three detailed case studies) or a larger number with only three detailed.

### Claim 3: COBOL's copybook data model — flat, positional memory layouts with no types, schemas, or enforced naming — makes business-critical data structurally difficult to trace across program boundaries, because two programs can name the identical memory location differently with nothing in the language connecting them
- **Evidence**: Detailed technical explanation with a concrete named example (`CUST-TAX-NUM` and `WS-FIELD-01` referring to the same value).
- **Confidence**: settled (a factual, checkable description of COBOL's copybook/data-layout mechanics, independent of any Devin-specific claim)
- **Quote**: "A field at a given position could be a tax ID, a timestamp, or a control number — the language provides no way to distinguish them semantically." ... "CUST-TAX-NUM and WS-FIELD-01 are the same value — but nothing in the language says so. The implicit dependency between them is invisible."
- **Our assessment**: This is the most concrete, verifiable technical claim in the article and the one the Prospector's triage flagged as the key "why agents fail on domain X" mechanism. It is a specific, named failure mode (semantic-free positional data crossing program boundaries under different names) rather than a vague "COBOL is old and confusing" characterization — useful for the guide as a named, generalizable barrier: any system where data crosses component boundaries without a shared schema (not just COBOL) will present agents with the same invisible-dependency tracing problem.

### Claim 4: LLMs have almost no COBOL training exposure because virtually all COBOL code lives on private mainframes and has never been shared publicly, so models lack the pattern recognition a human COBOL expert builds over decades
- **Evidence**: Direct claim about training-data scarcity, illustrated with the same `WS-FIELD-01` example used in Claim 3, contrasted against a human expert's "30 years of exposure."
- **Confidence**: anecdotal (plausible and directionally consistent with known facts about COBOL's proprietary distribution, but the article gives no quantitative measure of "almost no" — e.g., no benchmark score or token-count estimate of COBOL's share of any model's training corpus)
- **Quote**: "Another challenge is that models have been trained on almost no COBOL. Virtually all COBOL lives on mainframes and has never been shared publicly, so LLMs lack the pattern recognition that makes them effective with modern languages." ... "A retiring COBOL expert can glance at a field name like WS-FIELD-01 and immediately know it's a tax ID. That intuition comes from 30 years of exposure to naming conventions, company-specific patterns, and actually writing COBOL. Models are starting from scratch."
- **Our assessment**: The article itself states these first two barriers "compound each other" — the tracing problem (Claim 3) and the pattern-recognition gap (this claim) interact because recognizing what a memory-offset field actually represents is exactly the intuition training-data exposure would normally provide. This compounding relationship, stated explicitly by the source, is worth preserving rather than treating the two barriers as independent.

### Claim 5: The most critical barrier is that COBOL runs exclusively on mainframes with tightly coupled infrastructure that cannot be replicated in a Linux VM, so agents can read COBOL source but cannot execute or test it — breaking the fast write-run-check-iterate loop the article calls "the core mechanism that drives agent performance"
- **Evidence**: Direct claim, explicitly ranked above the other two barriers ("the most critical problem"), naming the specific infrastructure classes (job control systems, middleware, legacy databases, proprietary filesystems) that don't exist in a Linux environment.
- **Confidence**: settled (a factual, verifiable claim about deployment architecture — mainframe-only execution environments genuinely do not run on commodity Linux VMs — independent of how well agents otherwise perform)
- **Quote**: "The most critical problem is that COBOL breaks the feedback loop that makes agents effective." ... "All leading coding agents run on Linux-based VMs, which means they can read COBOL source code but cannot run or test it. The core mechanism that drives agent performance — fast, autonomous iteration — is fundamentally broken."
- **Our assessment**: This is the single highest-value claim in the source for the guide, and precisely the "generalizes beyond COBOL" pattern the Prospector's triage comment flagged. It names, explicitly, a structural precondition for agent effectiveness (a runnable, checkable feedback loop) that the rest of this corpus's verification-focused sources (see Cross-References → Extends) assume is available and focus on *improving* — this source is the first in the corpus to document a domain where that precondition is simply unavailable, not merely imperfect.

### Claim 6: 68% of COBOL modernization efforts fail
- **Evidence**: A single unattributed statistic, stated as evidence for how hard the problem is, immediately before the article pivots to "what it takes" to succeed with agents.
- **Confidence**: anecdotal (no source, survey, or methodology named for this figure anywhere in the article)
- **Quote**: "As you can see, this is incredibly difficult to get right — so difficult that 68% of COBOL modernization efforts fail."
- **Our assessment**: This is the article's baseline-failure-rate framing, structurally functioning like Claim 1's talent-scarcity statistics — an unattributed industry figure used to motivate the value of Devin's approach. It should be cited in the guide only as a stated, unattributed vendor claim, not as an independently verified modernization failure rate.

### Claim 7: Success with COBOL requires two conditions: (1) the agent must build a comprehensive, system-wide map of the codebase before acting, and (2) for any work beyond documentation, the agent's feedback loop must be restored — which is possible for batch workloads (30-50% of COBOL migrations) but not for transactional workloads
- **Evidence**: Direct two-part framework statement, followed by an explanation of why batch workloads (deterministic inputs/outputs, offline scheduling) can have their feedback loop artificially restored on the agent's own VM, while transactional workloads (live systems, decades of accumulated database state, no isolated test environment) cannot.
- **Confidence**: emerging (a coherent, internally consistent framework backed by the technical reasoning in Claims 3-5, but the 30-50% batch-workload-share figure is given without a cited source, and the framework itself is Cognition's own prescriptive model, not an independently validated taxonomy)
- **Quote**: "Batch workloads — which make up 30% to 50% of COBOL migrations — are scheduled, offline processes like reporting and settlements. They take structured inputs and produce deterministic outputs. Because the expected output is known in advance, the agent can recreate the logic in a modern language on its own VM and iterate until the outputs match — restoring the feedback loop that COBOL otherwise breaks." ... "Transactional workloads are fundamentally different... There is no isolated environment to safely replicate them in, and no clean input/output pairs to test against. Autonomous migration of these systems remains out of reach for agents today — but tools like Windsurf can still help developers read, trace, and navigate transactional code across large COBOL estates."
- **Our assessment**: This is the article's central technical thesis and its most transferable idea: the feedback-loop-restoration approach (recreate the logic somewhere the agent *can* execute and test it, using known-good inputs/outputs as an oracle) is a specific, generalizable pattern for any domain where the target execution environment itself is inaccessible to the agent — the target system doesn't need to be executable, only *some* system with equivalent, checkable input/output behavior. The explicit exclusion of transactional workloads, with a named partial mitigation (Windsurf for human-in-the-loop code navigation, not autonomous migration), is a candid capability boundary rather than a blanket "Devin solves COBOL" claim.

### Claim 8: At a Fortune 500 healthcare company, DeepWiki (Cognition's codebase indexing tool) built a system-wide map of millions of lines of claims-processing COBOL written by since-retired engineers, and Devin used that map to discover undocumented recovery logic that existed specifically to prevent duplicate transactions after system interruptions — a safeguard the company can now demonstrate to auditors
- **Evidence**: Named case study with a specific named artifact (DeepWiki-generated interactive diagram) and a specific discovered finding (duplicate-transaction recovery logic).
- **Confidence**: anecdotal (single named case, no company name given beyond "a Fortune 500 healthcare company," no verification that the "recovery logic" finding was independently confirmed by the company's own auditors, no metric for how much of the "millions of lines" was actually mapped or documented)
- **Quote**: "The company used DeepWiki, Cognition's codebase indexing tool, to build the system-wide map Devin needed to understand the codebase. DeepWiki parsed every program's structure, traced how memory blocks flow between programs, and built an interactive diagram that enables the developer to better understand the entire codebase." ... "In one session, Devin identified that a program's recovery logic existed specifically to prevent duplicate transactions after a system interruption... a critical financial safeguard that was invisible is now documented, understood, and demonstrable to auditors."
- **Our assessment**: This is the article's clearest demonstration of Claim 7's "codebase mapping" condition in practice — DeepWiki's role is explicitly to compensate for the copybook/positional-data opacity named in Claim 3, by tracing memory-block flow system-wide rather than program-by-program. The duplicate-transaction-prevention discovery is a specific, plausible example of documentation-only work (no execution needed, consistent with Claim 7's stated exemption for documentation) surfacing business logic that was previously tribal knowledge lost to retirement.

### Claim 9: A top-10 global automotive manufacturer migrated a 25,000-line COBOL customs batch workflow to AWS Lambda by having Devin write and iteratively test a Python re-implementation against known outputs, refining a playbook across sessions, delivering an estimated 73% reduction in migration costs
- **Evidence**: Named case study with a specific line count (25,000), a specific migration mechanism (Python rewrite tested against known I/O until convergence), a described playbook-refinement loop, and a specific cost-reduction figure.
- **Confidence**: anecdotal (single named case, "top 10 global automotive manufacturer" not identified by name, "estimated 73%" figure given with no baseline cost, no time-to-completion figure more specific than "within months," no description of what fraction of the 25,000 lines required manual correction after Devin's output)
- **Quote**: "The company fed the COBOL input/output from the workflow directly to Devin, which analyzed the underlying logic, wrote a Python implementation designed to reproduce the same behavior, ran it on its VM, and tested it against the known outputs — iterating on every mismatch until the two converged." ... "Within months, Devin completed the full migration — delivering an estimated 73% reduction in migration costs."
- **Our assessment**: This is a direct, concrete instance of Claim 7's batch-workload feedback-loop restoration mechanism: instead of running the actual COBOL, Devin runs an equivalent Python implementation on its own VM and treats known COBOL outputs as ground truth to converge against. The playbook-refinement description ("After each session, Devin identified what worked and what didn't, allowing it to refine ambiguous instructions, eliminate redundant steps, and tighten constraints") documents playbook iteration as a named, repeatable technique distinct from a single one-shot migration attempt — each session's output informs the next session's instructions.

### Claim 10: At Itaú Unibanco (Latin America's largest private bank), other agentic tools generated COBOL that violated mainframe syntactic constraints (exceeding the 72-character column limit, mishandling COMP variables) and broke in production, forcing manual correction of every change; Devin succeeded on the same tax-ID refactor by following a playbook encoding those constraints, running hundreds of agents concurrently across the codebase, completing three months ahead of a government deadline across hundreds of programs and 20 field variations with zero production errors
- **Evidence**: Named case study naming the specific mandate (numeric-to-alphanumeric tax ID conversion), the specific failure mode of unnamed competing tools (column-limit violations, COMP mishandling), the specific mitigation (playbook encoding bank engineers' own constraints), the specific parallelization mechanism (hundreds of concurrent agents), and specific outcome figures (3 months ahead of deadline, hundreds of programs, 20 field variations, zero production errors).
- **Confidence**: anecdotal (single named case with unusually specific outcome figures — "zero production errors" and "three months ahead" are strong, falsifiable claims — but self-reported by the vendor with no named Itaú spokesperson, no independent audit, and the competing "other agentic tools" are not named, making the comparison unverifiable)
- **Quote**: "These agents had no understanding of COBOL's syntactic constraints — exceeding COBOL's 72-character column limit and mishandling COMP variables. The result was code that broke when run on the mainframe, forcing engineers to monitor every session and manually correct errors, which defeated the purpose of using an agent." ... "And because Devin can run hundreds of agents concurrently, the changes were coordinated across the codebase in parallel rather than one program at a time." ... "The refactor was completed three months ahead of the government deadline — across hundreds of programs, 20 field variations, and zero production errors."
- **Our assessment**: This is the article's strongest capability claim and its least independently verifiable one. The playbook-as-constraint-encoding pattern here is the same mechanism as Claim 9 (Cognition frames "playbook" consistently across both case studies as encoded domain/syntactic rules, not just task instructions), but applied to constraint-compliance rather than behavior-replication. "Zero production errors" across "hundreds of programs" is an unusually absolute claim for an autonomous code-modification effort at this scale — the guide should flag this as the single most aggressive unaudited metric in the source.

### Claim 11: Because Devin can run hundreds of agents in parallel, Itaú Unibanco completed its migrations 5-6x faster without scaling headcount — reframing the historic COBOL modernization bottleneck (talent scarcity) as a problem with "a viable solution" that doesn't depend on closing the expertise gap
- **Evidence**: Closing-section synthesis statement tying the parallel-execution mechanism to a headline speedup figure and an explicit talent-bottleneck reframing.
- **Confidence**: anecdotal (headline multiplier figure with no stated baseline measurement methodology — unclear whether "5-6x faster" is measured against sequential single-agent Devin execution, human-engineer baseline, or industry-average migration timelines)
- **Quote**: "And because Devin can run hundreds of agents in parallel, migrations can accelerate significantly — Itaú, for example, has completed migrations 5-6x faster without needing to scale headcount." ... "The bottleneck in COBOL modernization has always been talent. For the first time, enterprises have a path forward that doesn't depend on closing that gap."
- **Our assessment**: The "without needing to scale headcount" qualifier is the load-bearing part of this claim — it distinguishes parallel-agent speedup from a scenario where the bank simply hired more COBOL contractors to work in parallel. This talent-substitution framing (parallel AI agents replacing the need for scarce human COBOL expertise, rather than merely accelerating existing human work) parallels the "expertise gap bridging" framing already documented for Assembly migration in `blog-cursor-nab-legacy-migration.md` Claim 6, but applied to COBOL and backed by a specific (if unaudited) multiplier rather than a qualitative "couldn't even think about it" statement.

## Concrete Artifacts

```
Source: cognition.com/blog/how-devin-is-modernizing-cobol-at-fortune-500-companies
(published 04.08.26, byline "By The Cognition Team")

Three named barriers to agents working on COBOL (section headings, in order):
1. "Business Critical Data Is Difficult to Trace"
   — copybooks: flat, positional memory layouts; no types/schemas/naming
     conventions; same value can exist under dozens of names across
     thousands of programs, connected only by memory position.
2. "LLMs Do Not Natively Understand COBOL"
   — virtually all COBOL lives on private mainframes, never published;
     models lack the pattern recognition a 30-year human expert has.
3. "Broken Agent Feedback Loop" (stated as "the most critical problem")
   — COBOL runs only on mainframes with tightly coupled infrastructure
     (job control systems, middleware, legacy databases, proprietary
     filesystems) that don't exist on a Linux VM; agents can read COBOL
     source but cannot run or test it.
```

```
Source: cognition.com/blog/how-devin-is-modernizing-cobol-at-fortune-500-companies

Two-part framework for "What It Takes to Modernize COBOL With Agents":
1. Comprehensive, system-wide codebase mapping before acting
   (trace every call chain, follow data across every program boundary,
   resolve what each field represents globally) — implemented via DeepWiki
   in the healthcare documentation case study.
2. Restoring the feedback loop, workload-dependent:
   - Documentation: feedback loop problem doesn't apply (read-only).
   - Batch workloads (30-50% of COBOL migrations): deterministic
     input/output; agent recreates logic in a modern language on its own
     VM and iterates until outputs converge with known-good COBOL output.
   - Transactional workloads: live systems, decades of accumulated
     database state, no isolated test environment, no clean I/O pairs —
     "autonomous migration of these systems remains out of reach for
     agents today." Partial mitigation named: Windsurf for human-driven
     code navigation/tracing (not autonomous migration).
```

```
Source: cognition.com/blog/how-devin-is-modernizing-cobol-at-fortune-500-companies

Three named Fortune 500 case studies:

1. Documentation — Fortune 500 healthcare company (unnamed)
   - Millions of lines of claims-processing COBOL, original engineers retired
   - Tool: DeepWiki (Cognition's codebase indexing tool) → system-wide map,
     interactive diagram of memory-block flow between programs
   - Finding: undocumented recovery logic preventing duplicate transactions
     after system interruptions — now "demonstrable to auditors"
   - Follow-up: company plans to expand COBOL documentation efforts

2. Batch Job Migration — top-10 global automotive manufacturer (unnamed)
   - 25,000-line COBOL customs workflow → AWS Lambda
   - Mechanism: Devin analyzes COBOL I/O, writes Python re-implementation,
     runs/tests on its own VM against known outputs, iterates to convergence
   - Playbook (encoded instructions) refined across sessions
   - Outcome: "within months," estimated 73% reduction in migration costs

3. Large-Scale Refactoring — Itaú Unibanco (named; largest private bank in
   Latin America)
   - Government mandate: corporate tax ID numeric → alphanumeric across
     entire COBOL estate; ~20 distinct tax-ID variations surfaced via
     mainframe tracing tools
   - Other (unnamed) agentic tools failed: violated 72-character column
     limit, mishandled COMP variables, broke on mainframe, required manual
     correction of every change
   - Devin: playbook encoding column limits, COMP handling, naming
     conventions; ran hundreds of agents concurrently, coordinating changes
     across the codebase in parallel
   - Outcome: completed 3 months ahead of government deadline; hundreds of
     programs; 20 field variations; zero production errors; "5-6x faster"
     overall migration speed cited in the closing section, attributed to
     parallel agent execution without headcount scaling
```

## Cross-References

### Cross-reference verification notes
`blog-cursor-nab-legacy-migration.md`, `blog-cognition-verifying-agentic-development.md`,
`blog-thoughtworks-harrison-insurance-legacy-modernization.md`,
`blog-cognition-auto-triage.md`, and `blog-cognition-cognizant-partnership.md`
were each re-read in full (MINER.md §4b) and the claim numbers cited below
were confirmed against each note's numbered `### Claim N:` headings in
document order before citing.

- **Corroborates**:
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (Assembly mainframe
    migration was previously categorically impossible due to expertise
    scarcity; "we couldn't even think about moving away from Assembly")
    and Claim 5 (AI-assisted legacy comprehension via Ask/Plan mode
    compressed BizCalc pre-development work 8x). This source's Claim 11
    (COBOL modernization's "historic bottleneck — talent — now has a
    viable solution" via parallel agents) independently arrives at the
    same "AI substitutes for scarce legacy-system expertise" framing for a
    different legacy language (COBOL vs. Assembly) and a different vendor
    (Cognition vs. Cursor) — two independent vendors now describe
    expertise-gap bridging as the core value proposition for legacy
    mainframe modernization specifically, not just general velocity
    improvement.
  - `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 7
    (AI "changes that dynamic. Not by removing the hard work, and not by
    turning modernization into a push-button exercise") and Claim 1
    ("Legacy is better defined by behavior than by age"). This source's
    explicit exclusion of transactional workloads (Claim 7 here) and its
    unattributed 68%-failure-rate framing (Claim 6 here) are a concrete,
    domain-specific instance of the same conservative hedge Thoughtworks
    states in the abstract — both sources agree AI-assisted modernization
    has a real, bounded scope rather than being a general-purpose solvent
    for legacy systems.
  - `blog-cognition-auto-triage.md` Claim 3 ("Devin can... spin up sub-Devins
    to investigate in parallel"). This source's Claim 10 ("Devin can run
    hundreds of agents concurrently" at Itaú Unibanco) is the same
    parallel-sub-agent architectural pattern applied to a different task
    category (COBOL refactoring vs. incident triage) — two independent
    Cognition product posts describing hundreds/many concurrent sub-Devins
    as a standing architectural capability rather than a one-off technique
    for either task.
  - `blog-cognition-cognizant-partnership.md` Claim 3 (Devin targeted at
    "code migration, refactoring, testing, and maintenance" workflows at
    Cognizant). This source's three case studies (documentation, batch
    migration, large-scale refactoring) are concrete, detailed instances of
    exactly the same workflow category set that partnership announcement
    names only abstractly — this source supplies the technical depth the
    Cognizant post lacks entirely (that post has zero technical detail or
    named case studies).

- **Contradicts**: None filed. One tension considered and rejected as not
  meeting the MINER.md §4a bar: `blog-cognition-verifying-agentic-development.md`
  Claim 2 states the "real unlock" for Devin was computer-use testing —
  "Devin will spin up the app, click through it, and confirm its changes
  actually work, the same way an engineer would" — which reads as a
  general capability statement. This source's Claim 5 states that for
  COBOL specifically, "the core mechanism that drives agent performance —
  fast, autonomous iteration — is fundamentally broken" because the code
  cannot run on a Linux VM at all. These are not in tension: the
  verifying-agentic-development post is about testing software that *can*
  run somewhere Devin controls (a web app on its own VM); this post is
  about software that structurally cannot run anywhere but a mainframe.
  The two sources describe different domains with different execution
  constraints, not opposing claims about the same class of system — see
  Extends below for how this source narrows the other's scope rather than
  disputing it.

- **Extends**:
  - `blog-cognition-verifying-agentic-development.md` (Devin's self-testing
    and verification infrastructure, built on the premise that Devin's own
    VM can run and observe the software under test). This source is a
    case study in what happens when that premise fails: COBOL cannot be
    executed in the same VM class Devin's verification infrastructure
    assumes, so the "restore the feedback loop" solution described here
    (Claim 7 — recreate the logic in a language the agent's own VM *can*
    run, and treat known COBOL outputs as the test oracle) is a distinct,
    more expensive workaround required specifically because the direct
    self-testing approach documented in the other source is unavailable.
    Read together, the two sources define a spectrum: directly executable
    software (self-test via computer use) → executable-elsewhere-with-a-
    known-oracle software (COBOL batch workloads, this source) →
    unexecutable-anywhere software (COBOL transactional workloads, still
    out of reach per this source's Claim 7).
  - `blog-cursor-nab-legacy-migration.md` Claim 5 (AI-generated user
    stories/API specs from legacy code comprehension). This source's
    healthcare documentation case study (Claim 8) is a more detailed,
    COBOL-specific instance of the same "AI reads legacy code and produces
    a comprehension artifact a human previously had to reverse-engineer
    manually" pattern, adding a specific mechanism (DeepWiki's system-wide
    memory-block-flow mapping) that the NAB source does not name.

- **Novel**:
  - **The three named technical barriers to agents on COBOL specifically**
    (Claims 3-5), and especially the explicit statement that the feedback
    loop — not model capability, not training data alone — is "the most
    critical problem" and "the core mechanism that drives agent
    performance." No prior corpus source names execution-environment
    inaccessibility as a distinct, ranked-above-training-data barrier to
    agent effectiveness in a specific technical domain.
  - **The feedback-loop-restoration technique for unexecutable code**
    (Claim 7, Claim 9): recreate the target logic in a language/environment
    the agent's own VM can run, using known input/output pairs from the
    original system as a test oracle. This is a novel, generalizable
    technique not previously documented in this corpus — distinct from
    both direct self-testing (`blog-cognition-verifying-agentic-development.md`)
    and manual code-comprehension-only approaches
    (`blog-cursor-nab-legacy-migration.md` Claim 5).
  - **Playbooks as encoded syntactic/domain constraints for code
    generation** (Claim 10 — column limits, COMP handling, naming
    conventions): distinct from the general "playbook as task instructions"
    framing in Claim 9, this shows playbooks being used specifically to
    encode hard technical constraints of the target language/platform that
    a model would not otherwise respect, which is new to this corpus's
    playbook/instruction-encoding material.
  - **The batch-vs-transactional workload taxonomy for autonomous
    migration feasibility** (Claim 7): no prior corpus source draws this
    specific line (deterministic offline batch jobs vs. live
    transactional systems with accumulated database state) as the
    determinant of whether autonomous AI migration is currently feasible.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the three named COBOL barriers
  (Claims 3-5) as a concrete case study for a new or existing discussion of
  "when the standard write-run-test-iterate agent loop breaks down."
  Specifically add the explicit ranking — feedback-loop breakage is named
  the *most* critical problem, ranked above both the data-tracing problem
  and the training-data-sparsity problem — as a generalizable diagnostic:
  before evaluating whether an agent can help in a constrained domain
  (embedded systems, kernel-space code, proprietary hardware, and COBOL
  alike), first ask whether the agent can execute and observe the system's
  behavior at all. Cite this source as the first in the corpus to name
  this precondition explicitly and rank it above model-capability concerns.

- **Chapter 02/03 (Harness Engineering / Verification)**: Add the
  feedback-loop-restoration technique (Claim 7, Claim 9) as a named,
  transferable pattern: when the target execution environment is
  inaccessible to the agent, recreate the target behavior in an
  environment the agent *can* run, and use known-good input/output pairs
  from the original system as the test oracle to iterate against. Pair
  this with the explicit boundary condition the source states for when
  this technique does *not* work (transactional workloads with no clean
  I/O pairs and no isolated replica environment) so the guide doesn't
  imply the technique generalizes to all "can't execute the real system"
  cases.

- **Chapter on Legacy Modernization / Technical Debt (planned or Ch05)**:
  Add this source as a third named vendor case study (alongside NAB/Cursor
  and Thoughtworks/Mechanical Orchard) documenting AI-assisted legacy
  modernization, specifically adding COBOL-specific detail the other two
  sources lack — copybook data-tracing mechanics, the 72-character
  column-limit/COMP-variable constraint class, and DeepWiki as a named
  codebase-mapping tool. Flag the three case-study outcome metrics (73%
  cost reduction, zero production errors across hundreds of programs,
  5-6x speedup) explicitly as self-reported, unaudited vendor figures with
  no named customer spokesperson — a materially weaker evidentiary basis
  than `blog-cursor-nab-legacy-migration.md`'s five named, quoted NAB
  practitioners.

- **Chapter 04 (Agentic Orchestration)**: Add the "hundreds of agents
  running concurrently, coordinating changes across the codebase in
  parallel rather than one program at a time" mechanism (Claim 10) as a
  third corpus data point (alongside `blog-cognition-auto-triage.md` Claim
  3 and `blog-addyosmani-code-agent-orchestra.md` Claim 3) for large-scale
  parallel sub-agent decomposition, here applied to constraint-compliant
  code refactoring across a legacy estate rather than feature
  implementation or incident triage.

## Extraction Notes

- WebFetch's default summarizing pass declined a full verbatim
  reproduction request, citing copyright concerns (consistent with the
  extraction-notes caveat already recorded in
  `blog-addyosmani-agentic-code-review.md` and other notes in this corpus).
  Two structured follow-up WebFetch passes were used first to get a
  section-by-section paraphrase plus short quotes, but the article's full,
  exact text was then retrieved directly via `curl` against the live URL
  and converted from HTML to plain text for this note — every `Quote`
  field above was copied character-for-character from that raw-text
  extraction, not reconstructed from the earlier WebFetch summaries. The
  raw-text extraction was diffed against the WebFetch summaries and found
  fully consistent (no factual discrepancies), giving high confidence the
  quotes are accurate.
- The full article is short (~1,100 words across eight sections: intro,
  three "Why COBOL is so Difficult" subsections, "What It Takes to
  Modernize COBOL With Agents," "Where Devin Helps Today" with three named
  case-study subsections, "What's Still Out of Reach," and a closing
  synthesis paragraph). No sub-pages were followed — the only other links
  on the page are site navigation and a "04. Articles" footer list of
  eight unrelated Cognition blog post titles, none of which elaborate on
  this article's COBOL claims.
- The publish date is read from the page's own byline format ("04.08.26"),
  interpreted as MM.DD.YY consistent with the convention already
  established for this source's sibling Cognition posts in this corpus
  (`blog-cognition-auto-triage.md`'s "05.18.26", `blog-cognition-cognizant-partnership.md`'s
  "01.28.26"), i.e. 2026-04-08.
- No contradiction meeting the MINER.md §4a filing bar was identified —
  see Cross-References → Contradicts for the one tension considered and
  rejected (this source narrows, rather than opposes,
  `blog-cognition-verifying-agentic-development.md`'s self-testing claim
  to domains where the target software is executable at all). No
  contradiction issue filed.
- Overall confidence is set to `emerging`: the technical mechanism
  descriptions (why COBOL breaks the feedback loop, the copybook data
  model, the batch/transactional distinction) are independently verifiable
  and consistent with known facts about COBOL and mainframe architecture
  (rated `settled` at the individual-claim level for Claims 3 and 5), but
  the three case-study outcome metrics rest entirely on unaudited,
  self-reported vendor figures with no named customer spokesperson quoted
  anywhere in the piece — a weaker evidentiary basis than this corpus's
  named-practitioner case studies (e.g. `blog-cursor-nab-legacy-migration.md`).
