---
source_url: https://cognition.com/blog/introducing-devin-security-swarm
source_type: blog-post
title: "Introducing Devin Security Swarm"
author: The Cognition Team
date_published: 2026-07-01
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2428"
---

# Introducing Devin Security Swarm

> Cognition's technical product-launch post for Devin Security Swarm, backed
> by two linked deep-dive posts (the "Agentic MapReduce" architecture and the
> "Evaluating Security Swarm" methodology page) that together supply the
> quantified benchmark (72% recall / $90.23 per run, beating three named
> competitors), three specific vulnerability examples, and — critically — the
> runtime-validation mechanism that two prior, thinner Cognition sources in
> this corpus explicitly flagged as an unanswered gap.

## Source Context

- **Type**: blog-post (Cognition's own product blog, cognition.com, byline
  "By The Cognition Team," dated "07.01.26" per the page's own byline and
  confirmed via the page's embedded JSON-LD `datePublished`:
  `2026-07-01T10:00:00-07:00`). This note also draws on two pages the launch
  post links to directly as "the full technical breakdown" and "our
  evaluation methodology": `devin.ai/blog/agentic-map-reduce` ("Agentic
  MapReduce," ~2,000 words, 9-minute read, dated July 1, 2026) and
  `devin.ai/blog/security-swarm-eval` ("Evaluating Security Swarm," ~1,600
  words, 8-minute read, also dated July 1, 2026). All three pages were
  published the same day and are treated here as one extraction per MINER.md
  §1's instruction to follow substantive linked pages.
- **Author credibility**: First-party Cognition product/technical content,
  unsigned by an individual (unlike `blog-cognition-multi-agents-working.md`'s
  named Walden Yan byline). Unlike this corpus's other two Devin Security
  Swarm sources — `blog-cognition-devin-federal-security-swarm.md` (a
  pre-event webinar page with zero technical detail) and
  `blog-cognition-devin-security-vulnerability-remediation-program.md` (a
  service-offering announcement with a timeline but no product mechanism) —
  this launch post and its two linked pages disclose an actual benchmark
  dataset, a named competitor comparison, a specific architecture (with a
  named prior-art borrowing: MapReduce), and a stated grading methodology.
  It remains vendor-published, unaudited, first-party content: no
  third-party reproduction of the 72%-recall figure exists anywhere in this
  corpus, and Cognition names its own tool as "Security Swarm" for
  comparison against products it labels "Claude Security," "Codex Security,"
  and "Cursor Security" — it is not stated whether these labels reflect the
  competitors' own product names or Cognition's own harness built atop
  those models.
- **Scope**: Covers the product pitch, the "how it works" architecture
  summary, the benchmark table, scan-profile/scheduling mechanics, and a
  pointer to the Remediation Program (launch post); the deterministic
  selector/Map/Reduce pattern, its motivating research on why single-agent
  search fails at whole-codebase tasks, and the five-stage security-scan
  pipeline (Agentic MapReduce post); and the eval dataset construction,
  grading rules, and a named failure mode ("Right Area, Different Defect")
  (Evaluating Security Swarm post). Does **not** cover: pricing beyond the
  benchmark's per-run cost figures, the six-week Remediation Program's
  internal timeline (already covered in
  `blog-cognition-devin-security-vulnerability-remediation-program.md`), any
  named customer identity behind "major companies" or the Fortune 500 pilot
  figure mentioned in a different corpus source, or independent third-party
  validation of the benchmark.

## Extracted Claims

### Claim 1: Cognition frames the problem as a volume crisis — security teams "seeing 10–100x more security findings" than before, with scanners unable to reason about business logic or chained exploits, and AI security tools unable to validate exploitability or write a fix
- **Evidence**: Opening two paragraphs of the launch post, stated as
  diagnostic premise before the product pitch; no named scanner, statistic
  source, or customer backs the "10–100x" figure.
- **Confidence**: anecdotal (unsourced vendor problem-framing; no named
  tool, customer, or measurement behind the multiplier)
- **Quote**: "As AI code production accelerates, security teams are facing a growing pile of findings they can't act on. Some teams are seeing 10–100x more security findings—and many are false positives." / "Scanners offer coverage at scale but miss critical exploits because they can't reason about business logic and discover chained vulnerability attacks. AI security tools often struggle to reason effectively about the whole codebase. None of them can validate which findings are actually exploitable or write a fix."
- **Our assessment**: This is generic vendor problem-framing with no
  independent evidentiary weight of its own, structurally identical to the
  unsourced premises already catalogued in
  `blog-cognition-devin-security-vulnerability-remediation-program.md` Claim
  1 ("attackers are using AI to discover, chain, and exploit vulnerabilities
  faster than traditional remediation programs can respond") — the same
  volume-crisis narrative restated for a different product-launch post one
  day later. Treat as restated sales framing, not new supporting data.

### Claim 2: Devin Security Swarm's core pitch is that it finds vulnerabilities across a codebase, validates their exploitability at runtime, ships remediation PRs, and does so at "30% lower cost than the nearest comparable alternative"
- **Evidence**: The launch post's central positioning sentence, immediately
  following the problem statement; the 30% figure is directly checkable
  against the benchmark table in Claim 3 below ($90.23 vs. Claude Security's
  $131.87 is a ~31.6% cost reduction).
- **Confidence**: emerging (a specific, quantified competitive claim that is
  internally consistent with the source's own disclosed benchmark data,
  though not independently reproduced by a third party)
- **Quote**: "Devin Security Swarm brings engineering capabilities to security teams so they can ship fixes themselves. It finds vulnerabilities across the codebase, validates that they are exploitable at runtime, and ships remediation PRs. Security Swarm finds more verified vulnerabilities at 30% lower cost than the nearest comparable alternative."
- **Our assessment**: Unlike the generic capability claims in
  `blog-cognition-devin-federal-security-swarm.md` Claim 1 and
  `blog-cognition-devin-security-vulnerability-remediation-program.md`
  Claim 4 — both of which this Miner flagged for asserting "validating what's
  actually exploitable at runtime" with **no disclosed mechanism** — this
  claim is now backed by a specific benchmark (Claim 3) and, critically, an
  explicit runtime-validation mechanism (Claim 10's sandboxed Verify stage).
  This source closes the gap those two earlier, thinner sources left open.

### Claim 3: On a 50-vulnerability benchmark spanning 14 languages, Devin Security scored 72% recall at $90.23 per run — the highest recall and, among tools scoring above 50% recall, the lowest cost of the four tools tested (Claude Security: 68% / $131.87; Codex Security: 48% / $118.20; Cursor Security: 26% / $4.60)
- **Evidence**: A four-row comparison table in the launch post's
  "Performance" section, with each competitor's product name, recall
  percentage, and cost-per-run figure given individually.
- **Confidence**: emerging (specific, quantified, named-competitor benchmark
  data with a disclosed dataset size and methodology — see Claims 11-13 —
  but self-reported by the vendor whose product wins the comparison, and not
  independently reproduced by this Miner or any third party in this corpus)
- **Quote**: "We evaluated Devin Security Swarm on a benchmark of 50 real-world vulnerabilities, each tied to a published GitHub Security Advisory (GHSA) across repositories in Go, Python, JavaScript, Rust, Ruby, C#, Java, Swift, PHP, Elixir, Erlang, C, Kotlin, and Dart." — followed by the table: "Devin Security / 72% / $90.23", "Claude Security / 68% / $131.87", "Codex Security / 48% / $118.20", "Cursor Security / 26% / $4.60"
- **Our assessment**: Note that Cursor Security is far cheaper ($4.60) but
  scores far lower recall (26%) — a genuinely different point on a
  cost/recall tradeoff curve, not a strictly dominated data point. Cognition's
  "30% lower cost" claim (Claim 2) and "leads on both detection and
  economics at once" claim (Claim 14) implicitly restrict the comparison to
  tools in a similar recall range (68%+), which is a defensible framing but
  worth stating explicitly when citing this table in the guide, since a
  naive reading of "lower cost AND higher recall" could be misapplied against
  Cursor Security specifically.

### Claim 4: Devin Security Swarm uniquely found three critical vulnerabilities the other three tested tools missed — a PHP sandbox bypass via template injection, an argument injection through metadata value parsing, and an overly broad deserialization surface in Spring Kafka
- **Evidence**: A single sentence in the launch post's "Performance"
  section, immediately following the benchmark table.
- **Confidence**: anecdotal (three specific, named vulnerability classes are
  given, but no CVE/GHSA identifier, affected repository name, or
  independent confirmation is provided for any of the three — unlike the
  eval page's worked facil.io example in Claim 13, which does name the
  specific project)
- **Quote**: "Only Devin found three critical vulnerabilities that other tools missed: a PHP sandbox bypass via template injection, an argument injection through metadata value parsing, and an overly broad deserialization surface in Spring Kafka."
- **Our assessment**: These are specific, checkable vulnerability-class
  descriptions rather than a vague "found more bugs" claim, which gives the
  guide concrete language for the kind of business-logic/chained
  vulnerability class this product line claims to target — but the lack of
  a GHSA ID or repo name (contrast the eval page's aws/amazon-redshift-
  python-driver example, GHSA-29h4-r29x-hchv, in Claim 12's Concrete
  Artifacts) means this specific claim cannot be independently verified
  from the source alone.

### Claim 5: Scan profiles can be generated directly from a customer's existing threat-model documentation, tailored to specific attacker personas, applied org-wide without per-repo configuration, with configurable batch size trading off depth against cost, and scheduled scans process only changed code after an initial full baseline
- **Evidence**: Two paragraphs under the launch post's "Scan profiles"
  heading, describing the feature mechanically rather than as a performance
  claim.
- **Confidence**: settled (first-party description of the product's own
  configuration surface, not a capability or outcome claim)
- **Quote**: "Devin can generate scan profiles directly from your existing threat model documentation, tailor them to specific attacker personas, and apply them across your entire organization without per-repo configuration or CI setup. Batch size is configurable per profile, giving you direct control over depth and cost." / "Scans run on a daily, weekly, or custom schedule. The first full scan establishes a baseline across your codebase. Subsequent scans process only code that changed since the last run, so cost decreases over time."
- **Our assessment**: The "process only code that changed since the last
  run" mechanic is directly corroborated and given technical grounding by
  the Agentic MapReduce post's Claim 9 below ("the entire pipeline runs only
  on files that changed since the last commit scanned"), so this is not
  just a scheduling-UI feature but a direct consequence of the underlying
  deterministic-selector architecture.

### Claim 6: Devin Security Swarm is already in production use by unnamed "major companies" for regular scanning and generally available as of the post's July 1, 2026 publication date, with the Vulnerability Remediation Program (a six-week forward-deployed engagement) offered as an optional, more guided on-ramp
- **Evidence**: The launch post's closing "How to get started" section.
- **Confidence**: anecdotal for the "major companies" adoption claim (no
  customer named or countable); settled for the availability date and the
  program's existence, which is corroborated in detail by an already-mined
  corpus source (see Cross-References)
- **Quote**: "Devin Security Swarm is already used by major companies for regular security scanning, and it's available starting today." / "For enterprises that want more guidance, the Devin Security Vulnerability Remediation Program is a six-week engagement to help organizations reduce their vulnerability backlog and set up ongoing remediation. Cognition's forward-deployed engineering team embeds with yours. First, Devin burns down your CVE backlog. After that, Security Swarm is set up to continuously find and fix vulnerabilities."
- **Our assessment**: This paragraph is a condensed restatement of the
  two-pillar structure already fully extracted in
  `blog-cognition-devin-security-vulnerability-remediation-program.md`
  Claims 3-5 (backlog-clearing pillar, then continuous-discovery pillar, six
  weeks, three two-week stages) — no new detail on the program itself, only
  confirmation that this launch post and that program-announcement post
  (published one day apart, July 1 vs. July 2, 2026) describe the same
  offering consistently.

### Claim 7: Whole-codebase reasoning tasks (security scanning, code-quality enforcement, breaking-change detection) share a defining property — a result is only trustworthy if the entire codebase was considered — and this breaks the "local-task toolkit" of a single search-driven agent (shell, grep, read) in three specific ways: it spends most of its budget finding the work rather than doing it, context becomes a shared bottleneck as unrelated discoveries compete for attention, and it has no explicit coverage boundary because it stops when it "decides" it's done rather than when a finite queue is exhausted
- **Evidence**: The Agentic MapReduce post's opening argument, naming three
  distinct failure modes as sub-headed points before introducing the
  MapReduce-derived solution.
- **Confidence**: emerging (a first-party architectural argument, but backed
  by three cited external studies for each failure mode — see Claim 8 — that
  this Miner did not independently re-verify)
- **Quote**: "These tasks share a defining property: the result is only trustworthy if the entire codebase was considered." / "The agent spends most of its budget finding the work rather than doing it. The agent greps, opens the wrong files, backtracks, and re-decides what to inspect next. On a large repo, selection can dominate analysis." / "Context becomes a shared bottleneck. A long-running agent carries discoveries from one part of the repo while reasoning about the next. As the run grows, unrelated evidence competes for attention and context budget." / "No explicit coverage boundary. A search-driven agent stops when it decides it's done - not when a finite work queue has been exhausted."
- **Our assessment**: This is a clean, specific articulation of *why*
  single-agent search architectures don't scale to completeness-required
  tasks, distinct from this corpus's existing context-rot coverage (see
  Cross-References) in that it targets a different failure axis: not "the
  model gets dumber at long context" but "the agent doesn't know when it has
  covered everything," a distinction directly relevant to any guide section
  on evaluating agentic architectures for audit/compliance-style tasks where
  completeness (not just quality) is the requirement.

### Claim 8: Cognition backs its three named failure modes with three external, non-Cognition research citations: Zhang et al. (FastContext, 2026) found reading/searching consumed 56.2% of tool-use turns and 46.5% of main-agent tokens across 300 SWE-bench Multilingual trajectories; Zeng et al. (LOCA-bench, ICML 2026) found agent success fell from 96.0% to 34.0% (Claude Opus 4.5), 72.0% to 38.7% (GPT-5.2 Medium), and 64.0% to 21.3% (Gemini 3 Flash) as environment description length grew from 8K to 128K tokens with task semantics held fixed; and Ko et al. (2026) found even the best-performing search agent (TongyiDR) terminated with an underverified answer on 52.1% of 215 multi-constraint search tasks
- **Evidence**: Three named academic/industry studies, each cited with
  author, paper title (two of three), and a specific figure or chart in the
  Agentic MapReduce post, presented as evidence for the "finding the work,"
  "context bottleneck," and "coverage boundary" failure modes respectively.
- **Confidence**: emerging (specific, named, dated external citations with
  quantified figures; this Miner did not independently fetch or verify any
  of the three cited papers, so the citations are reported as Cognition's
  characterization of them, not independently confirmed)
- **Quote**: "Zhang et al. analyzed 300 coding-agent runs and found that reading and searching consumed more than half of all tool-use turns and nearly half of the main agent's tokens. The study classifies both activities as repository exploration; it does not claim that every read was unnecessary." (Source: Zhang et al., FastContext (2026)) / "Zeng et al. held task semantics fixed while increasing the amount of information agents had to navigate. From 8K to 128K tokens, success fell from 96.0% to 34.0% for Claude Opus 4.5, 72.0% to 38.7% for GPT-5.2 Medium, and 64.0% to 21.3% for Gemini 3 Flash." (Source: Zeng et al., LOCA-bench (ICML 2026)) / "Ko et al. evaluated search agents on questions requiring at least three independent constraints. Even the strongest trained system terminated with an underverified answer on 52.1% of tasks; an answer was underverified when at least one constraint remained unresolved or violated." (Source: Ko et al., When Is Enough Not Enough? Illusory Completion in Search Agents (2026))
- **Our assessment**: The Zeng et al. LOCA-bench figures are a third,
  independent quantified data point for context-length-driven performance
  degradation, alongside this corpus's existing Chroma "context rot"
  citations (see Cross-References) — but it measures a related, distinct
  variable (environment/navigable-information length at fixed task
  semantics, i.e., a "how much do you have to search through" axis) rather
  than raw conversational context length, so it should be cited as a
  complementary, not duplicate, data point. None of the three papers is
  independently corroborated elsewhere in this corpus; a future Miner could
  usefully mine FastContext, LOCA-bench, or the Ko et al. paper directly if
  any is discoverable as a primary source.

### Claim 9: Agentic MapReduce adapts the two-decade-old MapReduce pattern to agents with one inversion — a Plan stage lets an agent author a deterministic "selector" (a relevance test) once, which then runs with no model in the loop over every file to produce a bounded, finite set of candidates that are Sharded into batches, Mapped by parallel focused-context workers, and Reduced by a synthesis agent — and because re-runs execute the same pipeline only on files changed since the last scan, ongoing cost tracks the size of the diff, not the size of the repository
- **Evidence**: A four-row "Stage / What happens / Agentic?" table (Plan:
  yes, Shard: no, Map: yes, Reduce: yes) plus explicit statements on cost
  behavior for initial and incremental runs.
- **Confidence**: emerging (detailed, internally consistent first-party
  architecture description, corroborated across all three pages of this
  source — launch post, Agentic MapReduce post, and eval post all describe
  the same five-stage security-specific pipeline consistently — but with no
  third-party technical audit)
- **Quote**: "We borrowed a two-decade-old idea from distributed systems - MapReduce, and adapted it for agents." / "First, an agent synthesizes a deterministic relevance test. That test runs over every source file and produces a finite set of candidates. The candidates are then divided into bounded batches, investigated in parallel, and reduced into a single result." / "Coverage is guaranteed by construction: the deterministic pass produces a finite work queue, every shard is assigned to an investigation agent, and the scan is complete only when that queue is exhausted." / "The principle: put agents where reasoning is required - synthesizing the decomposition function, inspecting the shards, and the reduction. Everything else is deterministic." / "as a codebase evolves, re-runs of Agentic MapReduce remain cheap. The entire pipeline runs only on files that changed since the last commit scanned, so you pay for the diff and not a full pass."
- **Our assessment**: The "put agents where reasoning is required, make
  everything else deterministic" principle is a specific, transferable
  design heuristic distinct from a generic "use agents for hard parts"
  platitude — it names exactly which three sub-steps get agent reasoning
  (author the selector, inspect each shard, reduce/synthesize) and which one
  does not (running the selector itself). This directly extends this
  corpus's existing "Agentic MapReduce" mention (see Cross-References) from
  a name and a one-sentence gloss into a fully specified four-stage pipeline
  with an explicit agentic/deterministic split.

### Claim 10: Completeness in this architecture rests on selector recall (a file matching no selector never reaches a worker), which Cognition frames as a deliberate, favorable trade because selectors are inspectable, version-controlled, testable artifacts — unlike a search agent's unfalsifiable claim to have "looked everywhere"
- **Evidence**: A direct architectural justification in the "The Planner"
  section of the Agentic MapReduce post, framed as an explicit trade-off
  the team chose rather than an incidental property.
- **Confidence**: emerging (a specific, falsifiable epistemic argument about
  auditability, though asserted rather than empirically demonstrated against
  an actual audit)
- **Quote**: "Completeness now rests on selector recall: a file that matches no selector never reaches a worker. We take this trade deliberately. The selectors are an inspectable, version-controlled artifact. You can read them, test them against known examples, and tune their recall to the task at hand, whereas a search agent's 'I've looked everywhere' is unfalsifiable."
- **Our assessment**: This is a specific, quotable epistemic argument for
  why a deterministic-selector architecture is preferable for
  audit/compliance contexts even if it introduces its own recall ceiling
  (a poorly-authored selector silently drops files) — the trade is honestly
  named rather than hidden, and the mitigation offered (selectors are
  testable, version-controlled artifacts a human can inspect) is a concrete,
  actionable design principle the guide can state directly for any
  "coverage-required" agentic task, not just security scanning.

### Claim 11: A production security scan runs as five explicit stages — Plan (an agent writes rules/selectors for the specific repo's routes, auth wrappers, and deserialization sinks, surfaced as an editable threat model a human can adjust before the swarm fans out), Shard (the rules run deterministically, non-matching files are dropped), Map (one child Devin session per batch investigates in parallel, clears a false-positive gate, and reports findings with severity/confidence/preconditions), Reduce (a reducer session deduplicates, attributes ownership, triages into P0/P1/P2, and composes attack chains across shards — e.g., an unauthenticated ID leak plus an ID-gated RCE become one P0 unauthenticated RCE), and Verify (a sandboxed session per serious finding reproduces it against a running build and records Confirmed / False Positive / Inconclusive)
- **Evidence**: A named five-stage breakdown ("A scan runs as five stages")
  in the Agentic MapReduce post's "Security Swarm" section, with one
  paragraph per stage.
- **Confidence**: emerging (the most technically detailed first-party
  description of the product's actual mechanism in this corpus, internally
  consistent with the launch post's shorter "how it works" summary, but
  still an unaudited vendor architecture description)
- **Quote**: "Plan: the threat model. A Devin session studies the repository and writes the rules for this codebase: patterns for its routes, data layer, auth wrappers, and deserialization sinks. Swarm surfaces these as an editable threat model. You can read every rule, and on an interactive scan, adjust it before the swarm fans out." / "Map: the swarm. One child Devin session per batch, in parallel, each from a fresh, focused context: its batch's signals and the rule provenance behind them. A worker reads the real code, clears a false-positive gate, and reports findings with severity, confidence, and preconditions, accounting for every file it was handed." / "Reduce: triage and chains. A reducer session consumes the workers' findings...deduplicates them, attributes ownership, and triages each into P0/P1/P2. With the global view no single worker had, it composes attack chains across shards: an unauthenticated ID leak plus an ID-gated RCE become one P0 unauthenticated RCE." / "Verify: runtime proof. The orchestrator Devin session fans out once more; this time over findings. One sandboxed session per serious finding reproduces it against a running build and records it as Confirmed, False Positive, or Inconclusive, so the report reflects what was actually executed."
- **Our assessment**: This is the single highest-value claim in the source
  for this corpus, because it directly resolves an open question flagged
  in two prior, thinner corpus sources: `blog-cognition-devin-federal-
  security-swarm.md` Claim 1 explicitly noted "zero supporting detail on
  *how* runtime exploitability is validated (sandboxed execution? symbolic
  tracing? an LLM's own reasoning?)," and `blog-cognition-devin-security-
  vulnerability-remediation-program.md` Claim 4 flagged the identical gap
  ("validating each one" is asserted with no description of the validation
  mechanism"). This source answers both: the Verify stage is sandboxed
  dynamic reproduction against a running build, with an explicit
  three-way Confirmed/False Positive/Inconclusive outcome — a specific,
  checkable mechanism, not a black-box "AI validates it" assertion.

### Claim 12: The eval dataset consists of 50 real vulnerabilities across 14 languages, each pinned to the commit immediately preceding its published fix and selected from advisories published after the tested models' training cutoffs, specifically so a correct finding reflects code reasoning rather than recall of a memorized advisory — and the team additionally reviewed agent trajectories to confirm models did not look up the CVE mid-run
- **Evidence**: The "The Dataset" section of the Evaluating Security Swarm
  post, naming the specific selection criteria and a worked example (the
  aws/amazon-redshift-python-driver case, CVSS 9.8, GHSA-29h4-r29x-hchv,
  RCE via `eval()` on server-supplied data).
- **Confidence**: emerging (a specific, well-articulated
  contamination-avoidance methodology — pinning to pre-patch commits and
  filtering by advisory-publication date relative to model training cutoffs
  is a standard, defensible technique for this kind of eval — but self-
  administered and not independently audited)
- **Quote**: "So we built our own eval, consisting of real, published vulnerabilities in real repositories. Each repo is pinned to the commit where the bug still shipped and drawn from after the models' training cutoffs. So a hit means Devin reasoned about the code, not that it recalled the advisory." / "Every advisory we use was published after the training cutoffs of the models we test, so the patch, the CVE, and the write-ups explaining the bug were never in their training data...We also reviewed harness trajectories to verify that agents did not look up CVEs in their own investigations."
- **Our assessment**: This is a meaningfully more rigorous eval-construction
  methodology than a bare "we tested on N vulnerabilities" claim — the
  explicit acknowledgment that "off-the-shelf security benchmarks use
  synthetic bugs that look nothing like the code real software ships with,
  and vendor benchmarks quote recall numbers we can't audit for false
  positives or reproduce independently" (a direct, named criticism of
  *other* vendor benchmarks, implicitly including competitors in Claim 3's
  table) raises the credibility of this specific eval relative to an
  unspecified benchmark claim, though it remains Cognition grading its own
  product on Cognition's own dataset against Cognition's own definition of
  a "hit."

### Claim 13: Recall is graded per-case as a strict semantic match to a single labeled target vulnerability (not any real bug in the right file), which the team acknowledges undercounts real findings — illustrated by a facil.io case where the swarm found two genuine, different vulnerabilities (a depth-counter underflow and a number-parsing over-read) in the exact file containing the graded target (a bare i/I infinity-token infinite loop) but scored zero because neither matched the labeled bug — leading the team to characterize the reported recall figures as "a floor on what a run finds, not a ceiling"
- **Evidence**: The "Grading" and "Right Area, Different Defect" sections of
  the Evaluating Security Swarm post, with one named, specific example case.
- **Confidence**: emerging (a specific, self-critical methodological
  disclosure with a concrete named example — a rare instance of a vendor
  explaining a way its own headline metric *understates* its product's
  actual performance, rather than only a way the metric could be inflated)
- **Quote**: "Recall is the fraction of the 50 cases in which at least one of the run's findings describes the target vulnerability; everything else, including false positives, is ignored." / "One example case was facil.io. The target defect is an infinite loop in its JSON parser triggered by a bare i/I (Infinity) token. Runs discovered the right file and flagged real defects in it: a depth-counter underflow and an over-read in number parsing, just not the bare-token loop we were grading for. Both were genuine flaws; neither was the one on the answer key." / "Counting that as a miss is correct for our benchmark, but it means recall understates detection: the needle we grade is one of several in the haystack, and surfacing a different real needle still scores zero. So one can read the recall numbers as a floor on what a run finds, not a ceiling."
- **Our assessment**: This is a genuinely useful methodological nuance for
  the guide to carry alongside the 72% headline figure (Claim 3): the
  benchmark's strict-match grading rule means the true "found a real,
  actionable vulnerability" rate for all four tools tested is very likely
  higher than the reported recall numbers for each, not just for Devin
  Security specifically — a caveat that should travel with the benchmark
  table whenever it's cited, so 72% is not misread as an upper bound on
  real-world vulnerability-finding capability.

### Claim 14: Cost and recall are typically in tension (buying more findings costs more compute), but Cognition claims Security Swarm does not sit on that tradeoff curve — it reports both the highest recall (72%) and, among tools clearing 50%+ recall, the lowest cost of the tools tested, achieved under an identical-conditions methodology (same repository, same pre-patch commit, no custom prompts or benchmark-specific tuning for any tool)
- **Evidence**: The "Results" section of the Evaluating Security Swarm
  post, explicit about both the tradeoff framing and the controlled-
  comparison methodology.
- **Confidence**: emerging (a specific claim to have broken an assumed
  tradeoff, backed by a stated methodology of holding conditions constant
  across tools — the strongest procedural detail in the source for ruling
  out an unfair comparison, though "no custom prompts or... tuning" cannot
  be verified from the source text alone, e.g., whether competitor tools
  were run via their own default interface or a harness Cognition built)
- **Quote**: "For each case in the dataset, we ran every security tool, including Security Swarm, against the same repository, checked out at the same pre-patch commit. We did not add custom prompts, configuration, or benchmark-specific tuning." / "Cost and recall usually pull against each other: you can buy more findings by spending more compute. Security Swarm doesn't sit on that tradeoff curve. It returns the most needles and costs less than the alternative closest to it, which is the result the Agentic MapReduce architecture was built to produce."
- **Our assessment**: "The alternative closest to it" language quietly
  narrows the "doesn't sit on the tradeoff curve" claim to a comparison
  against Claude Security specifically (68%/$131.87, the next-highest
  recall tool) — this is consistent with Claim 3's assessment that the
  "beats on both axes" framing implicitly excludes Cursor Security's very
  different, much-cheaper/lower-recall point on the same curve. The guide
  should cite this claim with that scope explicitly stated, not as an
  unqualified "Security Swarm dominates all alternatives on every axis."

## Concrete Artifacts

### Benchmark comparison table, verbatim (launch post, "Performance" section)
```
Source: cognition.com/blog/introducing-devin-security-swarm

Harness           Recall    $/Run
Devin Security    72%       $90.23
Claude Security   68%       $131.87
Codex Security    48%       $118.20
Cursor Security   26%       $4.60

(Benchmark: 50 real-world vulnerabilities tied to published GitHub
Security Advisories, across Go, Python, JavaScript, Rust, Ruby, C#, Java,
Swift, PHP, Elixir, Erlang, C, Kotlin, and Dart.)
```

### Agentic MapReduce stage table, verbatim (devin.ai/blog/agentic-map-reduce, "The Architecture")
```
Source: devin.ai/blog/agentic-map-reduce

Stage    What happens                                                Agentic?
Plan     An agent studies the repo and authors selectors, patterns   Yes
         that identify which code is relevant
Shard    The selector runs deterministically over the entire repo;   No
         matches are bucketed into bounded batches
Map      One agent per batch, in parallel, does the real per-shard   Yes
         reasoning
Reduce   An agent groups, dedupes, and synthesizes the per-shard     Yes
         outputs into a final answer
```

### Example selector table, verbatim (devin.ai/blog/agentic-map-reduce, "The Planner")
```
Source: devin.ai/blog/agentic-map-reduce

Task                        Example Selectors
Security Scanning           Select route declarations, auth boundaries,
                             deserialization entry points, and calls to
                             dangerous APIs
Breaking-Change Detection   Compare exported symbols or generated API
                             schemas, then select affected consumers
Code-Quality Enforcement    Query syntax trees for deprecated APIs or
                             project-specific anti-patterns
Large-Scale Migration       Traverse imports and references to find
                             every caller of the interface being replaced
```

### Security-scan five-stage pipeline, verbatim (devin.ai/blog/agentic-map-reduce, "Security Swarm")
```
Source: devin.ai/blog/agentic-map-reduce

1. Plan    — Devin session writes rules/selectors for this repo's
             routes, data layer, auth wrappers, deserialization sinks;
             surfaced as an editable threat model.
2. Shard   — Rules run deterministically over the entire repo; every
             match emits a signal; non-matching files are dropped;
             matches bucketed into bounded batches.
3. Map     — One child Devin session per batch, in parallel, fresh
             focused context (batch's signals + rule provenance);
             clears a false-positive gate; reports findings with
             severity, confidence, preconditions.
4. Reduce  — Reducer session dedupes findings, attributes ownership,
             triages into P0/P1/P2, composes attack chains across
             shards (e.g., unauthenticated ID leak + ID-gated RCE =
             one P0 unauthenticated RCE).
5. Verify  — Orchestrator fans out one sandboxed session per serious
             finding; reproduces against a running build; records
             Confirmed / False Positive / Inconclusive.
```

### Cited external research on single-agent whole-codebase reasoning failure, verbatim (devin.ai/blog/agentic-map-reduce)
```
Source: devin.ai/blog/agentic-map-reduce

1. Zhang et al., FastContext (2026) — 300 SWE-bench Multilingual
   trajectories, GPT-5.4-high with Mini-SWE-Agent:
   Tool-use turns spent reading/searching: 56.2%
   Main-agent tokens spent reading/searching: 46.5%

2. Zeng et al., LOCA-bench (ICML 2026) — 75 runs per context length,
   ReAct scaffold, fixed task semantics, environment description
   length varied 8K -> 128K tokens:
   Claude Opus 4.5:   96.0% -> 34.0% success
   GPT-5.2 Medium:    72.0% -> 38.7% success
   Gemini 3 Flash:    64.0% -> 21.3% success

3. Ko et al., "When Is Enough Not Enough? Illusory Completion in
   Search Agents" (2026) — 215 multi-constraint search tasks, up to
   100 turns/task, underverified-answer rate (lower is better):
   DR-Tulu:     90.2%
   WebExplorer: 72.6%
   TongyiDR:    52.1% (best of the three tested)
```

### Eval dataset construction and grading rule, verbatim (devin.ai/blog/security-swarm-eval)
```
Source: devin.ai/blog/security-swarm-eval

Dataset: 50 vulnerabilities, 14 languages (Go, Rust, Python, Ruby, Java,
C#, JavaScript, C, Swift, Dart, Elixir, and others), repo sizes from
smallbitvec (60 KB, 10 files) to libcrux (92 MB, 1,754 files).

Worked example case:
  Repo: aws/amazon-redshift-python-driver
  CVSS: 9.8 | Language: Python | Size: 2.0 MB, 179 files
  Class: RCE | CWE: CWE-94 | GHSA ID: GHSA-29h4-r29x-hchv
  Commit: 2c1dd5b9aca1945a1b8e01b2359075d9e8b0e77c
  Vulnerability: "A column-type parser runs eval() on data the server
  sends back, so a malicious server executes code on the client."

Grading rule: "Recall is the fraction of the 50 cases in which at least
one of the run's findings describes the target vulnerability... A
finding matches if it lands on the same root cause in the same place,
with the CWE and file path as hints. We don't require matching wording
or line numbers."
```

## Cross-References

- **Corroborates**: `blog-cognition-devin-security-vulnerability-remediation-program.md`
  Claims 1, 3, 4 — this source's Claim 1 (volume-crisis problem framing) and
  Claim 6 (six-week Remediation Program, two-pillar structure) restate,
  without adding new data to, that source's already-extracted claims about
  the same problem framing and the same program, published one day apart
  (2026-07-01 vs. 2026-07-02).
- **Extends** (high value): `blog-cognition-devin-federal-security-swarm.md`
  Claim 1 and `blog-cognition-devin-security-vulnerability-remediation-program.md`
  Claim 4 — both of those sources explicitly flagged, at extraction time,
  that Cognition's "validates what's actually exploitable at runtime" /
  "validating each one" language was asserted with **zero disclosed
  mechanism**. This source's Claim 11 (the five-stage pipeline's Verify
  stage: sandboxed reproduction against a running build, graded Confirmed /
  False Positive / Inconclusive) directly answers that open question with a
  specific, checkable mechanism. Any future guide citation of the federal or
  remediation-program sources' runtime-validation language should be updated
  to point here for the actual mechanism.
- **Extends**: `blog-latentspace-ainews-fable-relaunch-orchestration.md`
  Claim 11 — that source's paraphrased, one-sentence description of "Agentic
  MapReduce" ("fan out bounded agents across a codebase, aggregate findings,
  and validate exploitability before surfacing confirmed vulnerabilities")
  and its Fortune 500 pilot figure ("found and fixed over a thousand
  vulnerabilities in production repos") is the only other corpus mention of
  this architecture by name. This source supplies the full four-stage
  general pattern (Claim 9) and five-stage security-specific pipeline (Claim
  11) that one-sentence gloss was standing in for, but does not mention or
  corroborate the Fortune 500 pilot figure — that figure remains sourced
  only to the AINews digest and is not independently confirmed here.
- **Extends**: This source's Claim 8 (Zeng et al., LOCA-bench, ICML 2026 —
  agent success falling from 96.0% to 34.0% for Claude Opus 4.5 as
  navigable-environment length grows from 8K to 128K tokens) is a third,
  independent quantified citation for context-length-driven performance
  degradation, alongside this corpus's existing "context rot" coverage in
  `blog-cognition-multi-agents-working.md` Claim 6 (citing Chroma's
  context-rot research) and `blog-anthropic-session-management-1m-context.md`
  Claim 8. It measures a related but distinct variable — searchable/
  navigable information volume at fixed task semantics, not raw
  conversational context length — so should be cited as a complementary
  data point, not a duplicate of the Chroma citation.
- **Contradicts**: None identified. No existing corpus source claims that
  scanner-based tooling adequately covers business-logic or chained
  vulnerabilities without agent-based discovery, that Devin Security Swarm's
  benchmark methodology is flawed, or that a deterministic-selector /
  bounded-parallel-worker architecture is inferior to unstructured
  single-agent search for whole-codebase completeness tasks — so no
  contradiction is filed. (This source's Claim 9's "put agents where
  reasoning is required, make everything else deterministic" principle and
  `blog-cognition-multi-agents-working.md` Claim 13's "map-reduce-and-manage"
  verdict against "unstructured swarms" are consistent, not contradictory —
  both are Cognition sources converging on a bounded, orchestrator-driven
  shape over free-form multi-agent negotiation.)
- **Novel**: The full Agentic MapReduce pipeline specification (Plan/Shard/
  Map/Reduce general pattern, Claim 9; the security-specific five-stage
  variant with an explicit Verify stage, Claim 11) is the first corpus
  source to specify this architecture beyond a one-sentence gloss. The
  three cited external studies (FastContext, LOCA-bench, the Ko et al.
  "Illusory Completion" paper — Claim 8) are new to this corpus. The
  eval-construction methodology (pre-patch-commit pinning + post-training-
  cutoff advisory selection to prevent memorization, Claim 12) and the
  "Right Area, Different Defect" recall-as-floor-not-ceiling finding (Claim
  13) are both new, transferable methodological points for how to build and
  interpret any AI-tool security benchmark, not specific to Devin.

## Guide Impact

- **Chapter 06 (Security & Threat Model)**: Add the benchmark table (Claim
  3) as a citable, quantified data point for AI-driven vulnerability
  scanning tool comparison — with the explicit caveat from Claim 13 that the
  underlying grading methodology (strict single-target semantic match) means
  reported recall figures are a floor, not a ceiling, on real detection
  capability, and the caveat from Claim 3/14 that the "wins on cost and
  recall" framing implicitly compares only tools in a similar recall range
  (excludes Cursor Security's much-cheaper, much-lower-recall point).
- **Chapter 06 (Security & Threat Model)**: Update any existing guide
  language that cites `blog-cognition-devin-federal-security-swarm.md` or
  `blog-cognition-devin-security-vulnerability-remediation-program.md` for
  "how does Devin validate exploitability" — cite this source's Claim 11
  (the five-stage pipeline, specifically the sandboxed Verify stage) as the
  actual disclosed mechanism instead of the earlier sources' unmechanized
  assertions.
- **Chapter 02 (Harness Engineering)**: Add Claim 9's design principle ("put
  agents where reasoning is required — synthesizing the decomposition
  function, inspecting the shards, and the reduction — make everything else
  deterministic") and Claim 10's inspectability argument (deterministic
  selectors as version-controlled, testable artifacts vs. an unfalsifiable
  "I've looked everywhere") as a general-purpose design pattern for any
  agentic task requiring provable completeness over a large corpus, not
  limited to security scanning — cite the four named example task types
  (security scanning, breaking-change detection, code-quality enforcement,
  large-scale migration) from the selector table.
- **Chapter 04 (Evaluation & Metrics)**: Add Claim 12's eval-construction
  methodology (pin to pre-patch commit, select advisories published after
  model training cutoffs, review trajectories to confirm no CVE lookup) as a
  concrete, reusable technique for building any benchmark intended to
  measure code reasoning rather than memorized-answer recall. Add Claim 13's
  "Right Area, Different Defect" finding as a caveat template for any
  single-target-match benchmark: recall figures built this way should be
  read as a floor, not a ceiling, on true capability.

## Extraction Notes

- **Fetch method**: An initial WebFetch call against the launch post URL
  returned a short, restructured ~250-word summary consistent with the
  paraphrasing problem already documented in this corpus's other Cognition
  source notes (e.g., `blog-cognition-multi-agents-working.md`,
  `blog-cognition-devin-federal-security-swarm.md` Extraction Notes) —
  notably, that summary reported benchmark figures (72%/$90.23 etc.) that
  turned out to be accurate once verified against the raw page, but per
  MINER.md §2a no `Quote` field in this note is drawn from that WebFetch
  output. All quotes were instead pulled from the raw page HTML fetched
  directly via `curl` with a browser user-agent: for the launch post, the
  page's Next.js `__next_f` streaming payload was located and its JSON
  `"children"` text fields extracted, cross-checked against the
  server-rendered HTML directly (including the benchmark table, which lives
  in a client-rendered `<div>` grid outside the streamed payload's text
  nodes and was recovered by locating and stripping the table's HTML markup
  directly). For the two linked Agentic MapReduce and Evaluating Security
  Swarm pages (an Astro-based site, `devin.ai`, distinct from the Next.js
  `cognition.com`), the server-rendered HTML was stripped of script/style
  tags and block-level tags converted to newlines to recover full body text.
- **Sub-pages followed**: Both links the launch post identifies as "the
  full technical breakdown" (Agentic MapReduce) and "our evaluation
  methodology" (Evaluating Security Swarm) were fetched and deep-read in
  full per MINER.md §1, since both are explicitly pointed to by the primary
  source as containing the substantive technical detail the launch post
  itself only summarizes. No other in-body links were followed (a Vimeo
  embed titled "Introducing Devin Security Swarm: Powered by Agentic
  MapReduce" was not transcribed — it is a video, out of scope for a
  text-source Miner pass).
- **Cross-references verified before writing**: re-read
  `blog-cognition-devin-federal-security-swarm.md` in full and confirmed
  Claim 1 by number and content; re-read
  `blog-cognition-devin-security-vulnerability-remediation-program.md` in
  full and confirmed Claims 1, 3, 4, 5, 6 by number and content; re-read
  `blog-cognition-multi-agents-working.md` in full and confirmed Claims 6
  and 13 by number and content; re-read
  `blog-latentspace-ainews-fable-relaunch-orchestration.md` in full and
  confirmed Claim 11 by number and content; re-read
  `blog-anthropic-session-management-1m-context.md` and confirmed Claim 8 by
  number and content. No claim number was guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References -> Contradicts. No contradiction issue filed.
- **Confidence rated `emerging` overall**: this source is meaningfully more
  rigorous than the two prior, thinner Cognition Security Swarm sources
  already in this corpus (both rated `anecdotal`) — it discloses an actual
  benchmark dataset, a stated contamination-avoidance methodology, a named
  competitor comparison under claimed identical conditions, a specific
  runtime-validation mechanism, and a self-critical methodological caveat
  (recall as a floor, not a ceiling) rather than only unfalsifiable
  capability assertions. It does not reach `settled` because it remains
  entirely vendor-self-reported: no third party has reproduced the 72%
  recall figure, no named customer or independent case study backs the
  "already used by major companies" claim, and the "Claude Security" /
  "Codex Security" / "Cursor Security" comparison points are Cognition's own
  characterization of competitor tools' performance, not something those
  vendors have confirmed.
