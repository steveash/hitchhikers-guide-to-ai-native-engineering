---
source_url: https://github.github.com/gh-aw/agent-factory-status
source_type: docs
title: "GitHub Agentic Workflows: Agent Factory Status"
author: GitHub Agentic Workflows team (GitHub Next)
date_published: null
date_extracted: 2026-04-21
last_checked: 2026-04-21
status: current
confidence_overall: emerging
issue: "#291"
---

# GitHub Agentic Workflows: Agent Factory Status

> Live production catalog of GitHub Next's agent factory — the most comprehensive
> public inventory of production agentic workflows in the corpus, listing 183+
> named workflows with AI engine assignments (copilot 65%, claude 28%, codex 5%),
> schedule cadences, and slash-command triggers; provides concrete evidence that
> a mature agent factory covers the full SDLC with intentional engine-to-domain
> assignment patterns.

## Source Context

- **Type**: docs (live status/catalog page — not a narrative post; a snapshot of
  the production agent factory. As a live page, contents change as workflows are
  added, retired, or reassigned. This note captures state as of 2026-04-21.)
- **Author credibility**: First-party from GitHub Next — the same team behind the
  "Peli's Agent Factory" blog series (Peli de Halleux, Don Syme, Mara Kiefer).
  This is the operational status dashboard for their own live production system.
  Factory counts and engine assignments are self-reported production data. High
  credibility for claims about their own system; does not automatically generalize
  to other teams or platforms.
- **Scope**: Provides per-workflow data (name, AI engine, schedule, slash command)
  for the GitHub Next agent factory at a point in time. Does NOT explain why
  specific engines were assigned to specific workflows, how workflows are developed
  or installed, cost or latency data per workflow, or the rationale for scheduling
  cadences. Explanatory depth lives in companion blog posts and the "How They Work"
  documentation (see `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: The GitHub Next agent factory runs 183+ distinct workflows covering the full SDLC

- **Evidence**: Extracted table lists 183 workflows by engine count (119 copilot +
  52 claude + 9 codex + 3 others), spanning security, documentation, CI/CD, code
  quality, repository management, observability, dependency management, and Go
  language analysis. The page states "500+" total entries; WebFetch extraction
  returned 198 numbered items with engine counts summing to 183, suggesting the
  full catalog may extend beyond what was captured. Triage notes from when this
  issue was filed cited "60+" and "~100+" workflows, implying the factory has grown
  significantly. This is the largest public catalog of production agentic workflows
  documented in the corpus.
- **Confidence**: emerging (self-reported; factory catalog reflects a live, changing
  system; exact counts are approximate due to extraction limits)
- **Quote**: (no direct narrative quote; evidence is the catalog table itself)
- **Our assessment**: The 183+ count is the most concrete public data point for
  "what does a mature agent factory look like at scale." It demonstrates that a
  team can build and operate a full-SDLC agentic automation layer — not just a
  handful of experimental workflows. For Ch05 (Team Adoption): this is the reference
  for what a mature factory eventually covers, useful for teams asking "what is the
  ceiling?" The domain breadth — from security red-teaming to poem-writing chatbots —
  also shows the factory includes both serious operational workflows and deliberate
  experimentation, coexisting in the same catalog.

### Claim 2: Engine assignment follows a cognitive-complexity gradient — Claude for investigation/analysis, Copilot for routine operations, Codex for code-intensive tasks

- **Evidence**: Engine-to-workflow mapping from catalog:
  - *Claude (52 workflows, 28%)*: Failure Investigator, CI Failure Doctor, Daily
    Security Red Team Agent, Copilot Session Insights, Daily Code Metrics and Trend
    Tracking, Blog Auditor, Developer Documentation Consolidator, DeepReport -
    Intelligence Gathering, Design Decision Gate, Agentic Workflow Audit Agent,
    Semantic Function Refactoring, six Go-specific language workflows (see Claim 7),
    platform self-monitoring (Daily AW Cross-Repo Compile Check, Safe Output Health
    Monitor, Schema Consistency Checker).
  - *Copilot (119 workflows, 65%)*: Auto-Triage Issues, Daily News, Daily Team
    Status, Dependabot Burner, Daily Workflow Updater, Code Refiner, Code
    Simplifier, Issue Monster, Organization Health Report, and the majority of
    scheduled daily reporting workflows.
  - *Codex (9 workflows, 5%)*: AI Moderator, Changeset Generator, Grumpy Code
    Reviewer (/grumpy), Duplicate Code Detector, Issue Arborist, Schema Feature
    Coverage Checker, Daily Fact About gh-aw.
  - Pattern: Claude clusters around tasks requiring investigation, multi-step
    reasoning, or domain expertise. Copilot handles high-volume, well-structured,
    routine tasks. Codex handles specifically code-centric tasks.
- **Confidence**: emerging (pattern is visible in the data; the team's selection
  criteria are not documented on this page)
- **Quote**: (inferred from catalog; not stated)
- **Our assessment**: This is the most actionable finding in the source for harness
  engineers. The pattern suggests an informal "complexity routing" heuristic: tasks
  requiring investigation, reasoning over complex states, or domain-specific expertise
  route to Claude; routine high-volume tasks go to Copilot; code-specialized tasks
  go to Codex. For Ch02 (Harness Engineering): recommend this as a starting heuristic
  for engine selection. The 65%/28%/5% split shows that routine automation dominates
  by volume; complex reasoning workflows are a minority but a critical one.

### Claim 3: The factory uses five distinct scheduling cadences mapping to task urgency and sensitivity

- **Evidence**: From the catalog:
  - Event-triggered (no schedule): majority of workflows (~120+); all slash-command
    workflows; most code-quality and triage workflows
  - `every 6h`: Failure Investigator (claude), Bot Detection (copilot) — reactive
    workflows where faster cycle time matters
  - Daily with specific times: ~30 workflows; Daily News (9:00), DeepReport (15:00
    weekdays), Repository Quality Improvement (13:00 weekdays), Copilot Token Usage
    Optimizer (14:00 weekdays), Super Linter Report (14:00 weekdays), Go Fan (7:00
    weekdays), Typist (11:00 weekdays)
  - Weekly: Copilot Opt (monday), Weekly Issue Summary (monday 15:00), Dictation
    Prompt Generator (sunday 6:00), Layout Specification Maintainer (monday 7:00)
  - Raw cron: Dependabot Dependency Checker (`20 9 * * 1,3,5`), Functional
    Pragmatist (`25 9 * * 2,4`) — compliance-style timing requirements
- **Confidence**: settled (catalog data is concrete)
- **Quote**: (from catalog; not narrative)
- **Our assessment**: The scheduling taxonomy maps directly to task urgency and
  cost sensitivity. `every 6h` is reserved for reactive workflows (failure
  investigation) where faster response time matters for CI health. Daily cadences
  cover cost-sensitive reporting and incremental code quality tasks where same-day
  feedback is sufficient. Weekly cadences cover broader periodic reviews. Raw cron
  format is used for tasks with precise timing requirements (e.g., 9:20 AM on
  Tue/Thu/Fri for dependency checks). For Ch01 (Daily Workflows): this five-tier
  taxonomy is a concrete framework practitioners can use to classify and schedule
  their own workflows.

### Claim 4: 15 slash commands provide user-initiated interaction points in an otherwise scheduled automation system — roughly 8% of total workflows

- **Evidence**: Slash commands extracted from catalog:
  `/ace` (ACE Editor Session, copilot), `/archie` (Archie, copilot), `/brave`
  (Brave Web Search, copilot), `/cloclo` (claude), `/craft` (Workflow Craft Agent,
  copilot), `/grumpy` (Grumpy Code Reviewer, codex), `/mergefest` (copilot),
  `/nit` (PR Nitpick Reviewer, copilot), `/plan` (Plan Command, copilot), `/poem`
  (Poem Bot, copilot), `/q` (copilot), `/scout` (Scout, claude), `/security`
  (Security Review Agent, copilot), `/summarize` (Resource Summarizer, copilot),
  `/unbloat` (Documentation Unbloat, claude). 15 of 183+ workflows are
  slash-command triggered.
- **Confidence**: settled (catalog data)
- **Quote**: (from catalog)
- **Our assessment**: The 8% ratio of command-triggered to total workflows suggests
  user-initiated interaction is intentionally a minority pattern in a mature factory.
  The command inventory covers code review (/nit, /grumpy, /security), documentation
  (/unbloat, /summarize), research (/brave, /scout), workflow creation (/craft),
  git operations (/mergefest), and creative/experimental (/poem, /q, /plan, /archie,
  /ace, /cloclo). Claude is assigned to 3 of the 15 slash commands (/cloclo, /scout,
  /unbloat), all of which require more reasoning-intensive output. For Ch01: the
  scheduled vs. slash-command distinction is a fundamental factory design decision —
  on-demand triggers are for tasks that benefit from human timing control; scheduled
  triggers are for tasks that should run regardless of human attention.

### Claim 5: The factory monitors itself — dedicated meta-workflows audit, profile, and test the factory's own workflows and infrastructure

- **Evidence**: Self-referential workflows identified in catalog:
  - Agentic Workflow Audit Agent (claude): audits other agents
  - Automated Portfolio Analyst (copilot): cost analysis across agents
  - Metrics Collector - Infrastructure Agent (copilot): factory-wide metrics
  - Agent Performance Analyzer - Meta-Orchestrator (copilot): meta-orchestration
  - Workflow Health Manager - Meta-Orchestrator (copilot): workflow health monitoring
  - Daily AW Cross-Repo Compile Check (claude): compilation verification across repos
  - Safe Output Health Monitor (claude): monitors Safe Outputs infrastructure
  - Agentic Observability Kit (copilot): observability tooling
  - 15+ Smoke* workflows: dedicated platform regression tests covering all engines
    (Smoke Claude, Smoke Copilot, Smoke Codex, Smoke Gemini, Smoke Crush, Smoke
    OpenCode, plus Smoke Agent variants, Smoke CI, Smoke Multi PR, etc.)
- **Confidence**: emerging (inferred from workflow names; specific behaviors
  documented in `blog-ghaw-agent-observability.md` for the observability cluster)
- **Quote**: (inferred from naming; details in companion blog posts)
- **Our assessment**: The self-monitoring layer is a non-trivial fraction of the
  factory. The Smoke* workflows specifically indicate the factory functions as
  its own regression suite — a meta-harness for the platform. For Ch04/Ch05: a
  production-scale factory needs dedicated infrastructure for its own health, and
  the pattern extends to smoke tests for every supported engine. Teams planning
  for scale should budget for this meta-layer from the start, not add it as an
  afterthought.

### Claim 6: The "Daily X" naming convention (38+ workflows) and task-oriented naming suggest an intentional taxonomy for human-navigable agent catalogs

- **Evidence**: 38 workflows identified with the "Daily X" prefix: Daily AstroStyleLite
  Markdown Spellcheck, Daily AW Cross-Repo Compile Check, Daily Choice Type Test,
  Daily CLI Performance Agent, Daily CLI Tools Exploratory Tester, Daily Code Metrics
  and Trend Tracking Agent, Daily Community Attribution Updater, Daily Compiler Quality
  Check, Daily Copilot PR Merged Report, Daily Copilot Token Usage Audit, Daily DIFC
  Integrity-Filtered Events Analyzer, Daily Documentation Healer, Daily Documentation
  Updater, Daily Fact About gh-aw, Daily File Diet, Daily Firewall Logs Collector and
  Reporter, Daily Go Function Namer, Daily Hippo Learn, Daily Issues Report Generator,
  Daily Malicious Code Scan Agent, Daily MCP Tool Concurrency Analysis, Daily News,
  Daily Observability Report for AWF Firewall and MCP Gateway, Daily OTel
  Instrumentation Advisor, Daily Project Performance Summary Generator, Daily Regulatory
  Report Generator, Daily Rendering Scripts Verifier, Daily Safe Output Integrator,
  Daily Safe Output Tool Optimizer, Daily Safe Outputs Conformance Checker, Daily
  Secrets Analysis Agent, Daily Security Red Team Agent, Daily Semgrep Scan, Daily
  Syntax Error Quality Check, Daily Team Evolution Insights, Daily Team Status, Daily
  Testify Uber Super Expert, Daily Workflow Updater. Task-oriented names include: CI
  Failure Doctor, Code Scanning Fixer, Bot Detection, Dead Code Removal Agent,
  Dependabot Burner, Duplicate Code Detector, Stale Repository Identifier.
- **Confidence**: anecdotal (naming patterns visible in catalog; explicit naming
  rationale not documented)
- **Quote**: (inferred from catalog structure)
- **Our assessment**: The "Daily X" prefix encodes cadence in the name — a human
  reading the catalog can instantly identify scheduled-daily workflows. Task-oriented
  names (Doctor, Fixer, Detector, Burner) describe what an agent *does* to the
  codebase, not what it *is*. Together these naming patterns constitute an implicit
  convention for human-navigable catalogs at scale. For Ch02 (Harness Engineering):
  recommend the "cadence prefix + task noun" naming convention as a practical standard
  for teams building catalogs that will grow past 10–20 workflows.

### Claim 7: A Go language specialization cluster using Claude exclusively (6+ dedicated workflows) demonstrates domain-specific agent specialization

- **Evidence**: Go-specific workflows, all using claude: Daily Go Function Namer,
  Go Fan (daily 7:00 weekdays), Go Logger Enhancement, Go Pattern Detector (daily
  14:00 weekdays), Typist - Go Type Analysis (daily 11:00 weekdays), Sergo - Serena
  Go Expert. None of these use Copilot or Codex.
- **Confidence**: anecdotal (pattern from catalog; rationale not documented on this
  page; plausible inference is that gh-aw repo is implemented in Go)
- **Quote**: (inferred from catalog)
- **Our assessment**: The Go cluster shows that at factory scale, domain-specific
  specialization emerges — dedicated agents for the team's primary codebase language,
  all assigned to the reasoning-intensive engine. The exclusive Claude assignment
  corroborates Claim 2's pattern (Go type analysis and pattern detection are more
  reasoning-intensive than routine cleanup). For Ch02: this is evidence for the
  "specialist workflow" pattern — dedicated agents for high-expertise domains rather
  than relying on a single generic code agent. A Go fan and a Go logger enhancer do
  different things; collapsing them into one "Go agent" would reduce specificity.

### Claim 8: Experimental engine smoke tests (crush, gemini, opencode) indicate the factory doubles as a platform sandbox for evaluating new AI engines

- **Evidence**: Three workflows each use a non-standard engine: Smoke Crush (crush),
  Smoke Gemini (gemini), Smoke OpenCode (opencode). All three use the "Smoke" prefix
  used for platform regression testing. "Crush" and "opencode" do not appear in the
  official gh-aw engine documentation (which lists copilot, claude, codex, gemini).
- **Confidence**: anecdotal (inferred from naming and context; explicit rationale not
  documented)
- **Quote**: (inferred from catalog structure)
- **Our assessment**: The factory explicitly includes smoke tests for engines not yet
  in official documentation, suggesting the factory is used as an evaluation harness
  before new engines reach production status. For harness engineers: this is an
  argument for building engine-agnostic workflow specs (using frontmatter-based engine
  configuration per `docs-ghaw-how-they-work.md` Claim 9), so new engines can be
  evaluated by swapping the frontmatter key rather than rewriting workflow logic. If
  the factory pattern holds, a team that maintains engine-agnostic specs can adopt
  new models as they mature with minimal rework.

### Claim 9: The Changeset Generator flagship workflow runs on Codex — providing the engine assignment the original blog post omitted

- **Evidence**: Changeset Generator appears in the catalog with engine=codex. The
  earlier source note `blog-gh-aw-operations-release-workflows.md` documented this
  workflow's 78% merge rate and behavior without specifying which AI engine it used
  (the Jan 2026 blog post was silent on engine choice). The status page (2026-04-21
  snapshot) shows codex as its assigned engine.
- **Confidence**: emerging (point-in-time snapshot; engine assignment may have
  changed since the blog post; the blog post's silence does not preclude prior engine
  assignments)
- **Quote**: (from catalog table)
- **Our assessment**: Codex for the Changeset Generator is consistent with Claim 2's
  pattern — version bumps and changelog generation are code-centric tasks. The
  blog post's silence on engine choice now has context. No contradiction with the prior
  note — the blog post described behavior and metrics; the status page adds the engine
  column. For the guide: when referencing the Changeset Generator's 78% merge rate,
  note that the workflow uses Codex and that this represents Codex's production
  performance on a code-centric release automation task.

## Concrete Artifacts

### Engine Distribution (2026-04-21 snapshot)

```
GitHub Next Agent Factory — Engine Distribution

Total workflows extracted: 183 by engine count (page may list more)

Engine     | Count | % of total | Apparent use pattern
-----------+-------+------------+-------------------------------------------
copilot    |   119 |    65%     | Routine ops, daily reporting, triage,
           |       |            | dependency mgmt, general code quality
claude     |    52 |    28%     | Investigation, analysis, security,
           |       |            | Go language cluster, platform audit
codex      |     9 |     5%     | Code-intensive tasks (changeset gen,
           |       |            | code review, deduplication, schema)
crush      |     1 |    <1%     | Smoke test only (experimental engine)
gemini     |     1 |    <1%     | Smoke test only (experimental engine)
opencode   |     1 |    <1%     | Smoke test only (experimental engine)

Note: "crush" and "opencode" are not in official gh-aw engine documentation.
Smoke-test-only engines should not be counted as production-grade assignments.
Excluding smoke tests: copilot ~68%, claude ~30%, codex ~5%.
```

### Scheduling Taxonomy (from catalog)

```
GitHub Next Agent Factory — Scheduling Patterns

Pattern           | Example workflows                          | Approx count
------------------+--------------------------------------------+--------------
Event-triggered   | CI Failure Doctor, Code Scanning Fixer,    | ~120+
  (no schedule)   | all slash-command workflows                |
                  |                                            |
every 6h          | [aw] Failure Investigator (claude)         | 2
                  | Bot Detection (copilot)                    |
                  |                                            |
daily (weekday,   | Daily News (9:00), DeepReport (15:00),     | ~30
  time-specific)  | Repository Quality Improvement (13:00),    |
                  | Go Fan (7:00), Typist (11:00)              |
                  |                                            |
weekly            | Weekly Issue Summary (Mon 15:00)           | ~5
                  | Copilot Opt (Mon)                         |
                  | Dictation Prompt Generator (Sun 6:00)      |
                  |                                            |
raw cron          | Dependabot: 20 9 * * 1,3,5                | 2
                  | Functional Pragmatist: 25 9 * * 2,4        |

Urgency mapping:
  every 6h  → reactive workflows where cycle time matters (failure investigation)
  daily     → same-day feedback sufficient (code quality, cost reporting)
  weekly    → broader periodic review (issue summary, health checks)
  event     → run only when triggered (code review, on-demand tools)
  raw cron  → compliance-style precise timing requirements
```

### Slash Commands Catalog (from catalog, 15 total)

```
GitHub Next Agent Factory — Slash Commands

Command      | Workflow                       | Engine  | Domain
-------------+--------------------------------+---------+------------------
/ace         | ACE Editor Session             | copilot | tooling/editor
/archie      | Archie                         | copilot | ?
/brave       | Brave Web Search Agent         | copilot | research
/cloclo      | /cloclo                        | claude  | ?
/craft       | Workflow Craft Agent           | copilot | meta / new workflows
/grumpy      | Grumpy Code Reviewer           | codex   | code review
/mergefest   | Mergefest                      | copilot | git ops
/nit         | PR Nitpick Reviewer            | copilot | code review
/plan        | Plan Command                   | copilot | planning
/poem        | Poem Bot                       | copilot | creative/experimental
/q           | Q                              | copilot | ?
/scout       | Scout                          | claude  | research/analysis
/security    | Security Review Agent          | copilot | security
/summarize   | Resource Summarizer Agent      | copilot | documentation
/unbloat     | Documentation Unbloat          | claude  | documentation

Claude slash commands (3/15): /cloclo, /scout, /unbloat — all reasoning-intensive
Codex slash commands (1/15): /grumpy — code-specific review task
Copilot slash commands (11/15): all remaining
```

### Domain Cluster Map (inferred from workflow names)

```
Domain              | Count  | Engines           | Representative workflows
--------------------+--------+-------------------+---------------------------------
Security &          |  ~8    | claude, copilot   | Daily Security Red Team (claude),
  Compliance        |        |                   | Code Scanning Fixer (copilot),
                   |        |                   | Daily Secrets Analysis (copilot),
                   |        |                   | Bot Detection (copilot, 6h)
                   |        |                   |
Documentation       |  ~8    | claude, copilot   | Daily Documentation Healer (claude),
                   |        |                   | Documentation Unbloat (claude),
                   |        |                   | Daily Documentation Updater (claude),
                   |        |                   | Glossary Maintainer (copilot, daily)
                   |        |                   |
CI/CD &             |  ~12   | claude, copilot,  | CI Failure Doctor (claude),
  Code Quality      |        | codex             | CI Optimization Coach (copilot, daily),
                   |        |                   | Changeset Generator (codex),
                   |        |                   | Code Simplifier (copilot)
                   |        |                   |
Observability /     |  ~8    | claude, copilot   | Metrics Collector (copilot),
  Meta-monitoring   |        |                   | Agentic Workflow Audit Agent (claude),
                   |        |                   | Automated Portfolio Analyst (copilot),
                   |        |                   | Workflow Health Manager (copilot)
                   |        |                   |
Dependency          |  ~4    | copilot           | Daily Workflow Updater (copilot),
  Management        |        |                   | Dependabot Burner (copilot),
                   |        |                   | Dependabot Dependency Checker (copilot)
                   |        |                   |
Go Language         |  6     | claude (all)      | Go Fan (daily 7:00), Typist (daily),
  Specialization    |        |                   | Sergo, Go Pattern Detector (daily),
                   |        |                   | Daily Go Function Namer, Go Logger
                   |        |                   |
Platform Smoke      |  ~15   | all engines       | Smoke Claude, Smoke Copilot,
  Tests             |        |                   | Smoke Codex, Smoke Gemini,
                   |        |                   | Smoke Crush, Smoke OpenCode,
                   |        |                   | Smoke Agent (5 variants), Smoke CI
                   |        |                   |
Reporting &         |  ~15   | copilot           | Daily News, Daily Team Status,
  Analytics         |        | (majority)        | Daily Copilot PR Merged Report,
                   |        |                   | Weekly Issue Summary
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support is first-class): That
    documentation describes multi-engine as a design option; this catalog confirms
    that in production three primary engines (copilot 65%, claude 28%, codex 5%) are
    actively used for distinct workflow types, plus experimental engines under smoke
    test. The theoretical claim is confirmed by the production distribution.
  - `blog-ghaw-agent-observability.md` Claim 3 (meta-agent pattern is viable in
    production): The catalog identifies at least seven dedicated meta/audit workflows
    (Agentic Workflow Audit Agent, Automated Portfolio Analyst, Metrics Collector,
    Workflow Health Manager, Agent Performance Analyzer, etc.) corresponding to the
    "observatory" layer documented in that blog post.
  - `blog-gh-aw-operations-release-workflows.md` (Changeset Generator and Daily
    Workflow Updater as production workflows): Both appear in this catalog (Changeset
    Generator under codex; Daily Workflow Updater under copilot). Confirms these are
    live production workflows at the time of extraction.
  - `discussion-hn-ttal-multiagent-factory.md` (multi-agent factory patterns): TTal's
    factory concept of a team-managed collection of specialized agents across the SDLC
    maps directly to what GitHub Next operates. The GitHub factory is the large-scale
    first-party reference for the concept TTal describes at small scale.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine as frontmatter config): Adds
    concrete production engine distribution and an observable engine-to-domain mapping
    pattern to the theoretical multi-engine claim.
  - `blog-ghaw-agent-observability.md` (three-tier observability decomposition): That
    note extracts the observability layer from a blog post; this catalog reveals the
    specific named workflows in that layer and their engine assignments (claude for
    audit, copilot for metrics/portfolio). Adds concrete identity to the abstraction.
  - `docs-ghaw-how-they-work.md` Claim 8 ("Continuous AI" — four canonical patterns):
    The four patterns (documentation currency, code quality, triage, code review) listed
    in the documentation all have multiple corresponding workflows in this catalog.
    "Continuous AI" is not aspirational — it is operational at 183+ workflow scale.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (Changeset Generator —
    behavior and metrics): This catalog adds the missing engine assignment (Codex) to
    the Changeset Generator entry first covered by that blog post.

- **Contradicts**: None found. `docs-ghaw-how-they-work.md` Claim 9 lists supported
  engines as "Copilot, Claude, Codex, Gemini" — the catalog adds "crush" and
  "opencode" as undocumented experimental engines in smoke tests. This is an extension
  of the engine inventory, not a contradiction (documentation lists production-grade
  engines; smoke tests may cover pre-production candidates).

- **Novel**:
  - **Aggregate factory scale** (Claim 1): No existing note documents the total
    workflow count or SDLC breadth of the GitHub Next factory. First corpus entry
    answering "how big is a mature agent factory?"
  - **Engine-to-domain assignment pattern** (Claim 2): First concrete production
    evidence for a cognitive-complexity gradient in engine assignment at scale.
    65%/28%/5% split provides a calibration baseline.
  - **Full slash command catalog** (Claim 4): No existing note catalogs the complete
    set of user-facing slash commands in the factory or their engine distribution.
  - **Go language specialization cluster** (Claim 7): First note identifying
    domain-specific agent specialization (a dedicated cluster of same-engine,
    same-domain workflows) as a factory-scale pattern.
  - **Experimental engine sandbox pattern** (Claim 8): The use of the factory as an
    engine evaluation sandbox (crush, opencode smoke tests not in official docs) is not
    described anywhere in the corpus.
  - **"Daily X" naming convention as catalog taxonomy** (Claim 6): Explicitly naming
    cadence in the workflow name (38+ "Daily X" workflows) as a navigability mechanism
    for large catalogs is not described in any existing source note.

## Guide Impact

- **Chapter 01: Daily Workflows** — The scheduling taxonomy (Claim 3) provides a
  five-tier framework (event-triggered, every-6h, daily, weekly, raw-cron) teams can
  use to classify their own workflows before building them. The scheduled vs.
  slash-command distinction (Claim 4) frames a fundamental design question: does this
  workflow run regardless of human attention, or should it run when a human decides?
  The "Daily X" naming convention (Claim 6) is immediately adoptable. Recommend
  these three patterns as a workflow design checklist for Ch01.

- **Chapter 02: Harness Engineering** — Engine assignment heuristic (Claim 2): add
  the copilot-for-routine / claude-for-analysis / codex-for-code gradient as a
  production-backed starting point for engine selection. Reference this catalog as
  the production evidence (65/28/5 distribution). The Go specialization cluster
  (Claim 7) provides evidence for the "specialist workflow" pattern. The factory-as-
  engine-sandbox pattern (Claim 8) is an argument for frontmatter-based engine
  configuration — swapping engines without rewriting logic.

- **Chapter 04: Multi-Agent Orchestration** — Factory scale (Claim 1) is the
  production reference for "what a mature agent factory looks like." Self-monitoring
  layer (Claim 5) demonstrates that meta-workflows are not optional at scale — the
  Smoke* infrastructure and observatory cluster together represent a dedicated
  platform health layer. Cross-reference with `blog-ghaw-agent-observability.md`
  for the named "observatory" pattern.

- **Chapter 05: Team Adoption** — This catalog is the concrete answer to "what
  should our agent factory eventually look like?" The 183+ workflow count, domain
  coverage, and engine distribution together constitute the most complete public
  description of a production-scale agent factory available in the corpus. Teams
  can use the domain cluster map as a roadmap, the engine distribution as a
  calibration target, and the naming conventions as an adoptable standard.

## Extraction Notes

1. **Live catalog — point-in-time snapshot**: The page is a live status dashboard.
   Workflow counts, engine assignments, and schedules change as GitHub Next iterates.
   This note captures state as of 2026-04-21. Patterns (engine gradient, naming
   conventions, domain clusters) are more durable than exact counts.

2. **Count discrepancy**: The page claims "500+" workflows; WebFetch returned 198
   numbered items; engine totals sum to 183. The discrepancy likely reflects
   rendering/extraction limits (the tool may not have captured all table rows) or
   the model's overcounting of items. Treat 183 as the minimum confirmed count; the
   actual total may be higher. Triage notes cited 60+ and ~100+, so the factory has
   grown, but the absolute ceiling is uncertain from this extraction.

3. **No rationale for engine assignment**: The catalog shows what but not why. The
   engine-to-domain gradient (Claim 2) is inferred from the visible pattern, not
   stated policy. A companion blog post or documentation page explaining selection
   criteria would upgrade this from emerging to settled.

4. **Smoke workflows are infrastructure, not production automation**: The 15+ Smoke*
   workflows are platform regression tests. Excluding them shifts the engine
   distribution slightly (copilot ~68%, claude ~30%, codex ~5%). The SDLC breadth
   claim (Claim 1) holds regardless, as all non-smoke domain clusters are represented.

5. **Experimental engines not documented**: "Crush" and "opencode" appear in the
   catalog (each as a single smoke test) but are not documented in official gh-aw
   documentation or any existing source note. No further information is available
   about these engines from this source.

6. **No sub-pages followed**: The agent-factory-status page is a catalog table with
   no linked per-workflow detail pages. Per-workflow depth lives in the "Meet the
   Workflows" blog series (tracked as separate issues in this corpus). This note
   captures only what the catalog table itself provides.

7. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose existing claims at the MINER.md §4a filing threshold. The
   undocumented engines (crush, opencode) extend the engine list in
   `docs-ghaw-how-they-work.md` Claim 9 without contradicting it.
