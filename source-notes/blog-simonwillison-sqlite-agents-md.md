---
source_url: https://simonwillison.net/2026/May/27/sqlite-agents/
source_type: blog-post
title: "sqlite AGENTS.md"
author: Simon Willison
date_published: 2026-05-27
date_extracted: 2026-06-06
last_checked: 2026-06-06
status: current
confidence_overall: emerging
issue: "#1073"
---

# sqlite AGENTS.md

> Simon Willison documents SQLite's AGENTS.md policy — a graduated approach that rejects
> agentic code outright but accepts agentic bug reports with reproducible test cases — and
> reports that the project recently hardened this stance and created a separate Bug Forum in
> response to AI-generated report volume.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a `trusted-feed` source; 27 May 2026)
- **Author credibility**: Simon Willison is among the most-cited LLM tooling commentators.
  He writes short-form annotations linking to primary sources with brief synthesis. The
  primary source he links — SQLite's AGENTS.md — was independently fetched and verified
  verbatim at https://sqlite.org/src/raw/AGENTS.md?ci=trunk. Claims about the project's
  policy therefore have primary-source backing. Claims about the commit removing "(currently)"
  and the Bug Forum creation are Willison's observations; the SQLite Bug Forum at
  https://sqlite.org/bugs/forum is publicly accessible for verification.
- **Scope**: The blog post covers SQLite's AGENTS.md governance policy (no agentic code; yes
  agentic bug reports with test cases), a recent commit strengthening that stance, and the
  creation of a separate Bug Forum due to AI-generated volume. The AGENTS.md file itself also
  contains detailed technical context for agents: build instructions, architecture walkthrough,
  coding conventions, and a table of generated files that must not be hand-edited. This note
  covers both the governance framing Willison discusses and the full technical context in the
  AGENTS.md primary source.

## Extracted Claims

### Claim 1: SQLite's AGENTS.md states that the project does not accept agentic code, but will accept agentic bug reports that include a reproducible test case

- **Evidence**: Verbatim text from SQLite's AGENTS.md at https://sqlite.org/src/raw/AGENTS.md?ci=trunk, fetched 2026-06-06.
- **Confidence**: settled (primary institutional document, publicly accessible)
- **Quote**: "SQLite does not accept agentic code.  However the project will accept agentic bug reports that include a reproducible test case. Patches or pull requests demonstrating a possible fix, for documentation purposes, are welcomed."
- **Our assessment**: This is a graduated policy, not a blanket ban. Three tiers: (1) agentic
  code — rejected outright, (2) agentic bug reports with reproducible test cases — accepted,
  (3) patches/PRs as documentation of a possible fix — accepted. The graduated structure
  distinguishes SQLite from Zig, which bans all AI contributions including bug reports
  (see `blog-simonwillison-zig-anti-ai.md` Claim 1). The qualifier "reproducible test case"
  is load-bearing: it requires machine-verifiable evidence, not just descriptive text. This
  constraint filters conjecture from evidence — agents that can reproduce bugs with runnable
  tests are welcomed; agents that generate descriptive analysis are not.

### Claim 2: SQLite's AGENTS.md requires prior agreement and/or legal paperwork for pull requests from humans as well — establishing that the project's default model is "we study contributions, then reimplement"

- **Evidence**: Verbatim text from SQLite's AGENTS.md
- **Confidence**: settled (primary institutional document)
- **Quote**: "SQLite does not accept pull requests without prior agreement and/or accompanying legal paperwork that places the pull request in the public domain. However, the human SQLite developers will review a concise and well-written pull request as a proof-of-concept prior to reimplementing the changes themselves."
- **Our assessment**: The pre-existing human PR policy establishes the baseline against which
  the agentic code restriction adds another layer. SQLite's upstream model has always been
  "study the contribution, reimplement it ourselves" — not direct merge. The agentic code
  restriction is therefore consistent with the project's philosophy: external contributors
  provide ideas and evidence; core developers implement. For agents, the expected path is:
  agent files bug report + test case → human developer reproduces and commits a fix.

### Claim 3: SQLite recently strengthened its no-agentic-code policy by removing the word "(currently)" from the restriction, indicating the policy is now treated as permanent

- **Evidence**: Reported by Simon Willison in his blog post; the current AGENTS.md text reads
  "SQLite does not accept agentic code" with no temporal qualifier, consistent with the
  removal Willison describes.
- **Confidence**: emerging (Willison's report is consistent with the current AGENTS.md text;
  the specific commit was not independently accessed)
- **Quote**: (no direct quote from Willison's blog post prose available; the current AGENTS.md
  text is the evidence — it contains no "(currently)" qualifier)
- **Our assessment**: The removal of "currently" is a meaningful policy signal. "Currently
  does not accept" implies the policy might change; "does not accept" treats it as a permanent
  stance. The fact that this was an active commit — not a wording choice from day one — means
  the project started with a softer stance and hardened it in response to observed agent
  behavior. This is evidence of real-world policy evolution, not theoretical policy-setting.
  Projects that adopt soft AI policies in early 2025–2026 may harden them as agent volume grows.

### Claim 4: The SQLite forum created a separate Bug Forum due to the volume of AI-generated bug reports

- **Evidence**: Reported by Simon Willison in his blog post; the SQLite Bug Forum at
  https://sqlite.org/bugs/forum is publicly accessible and confirmed to exist.
- **Confidence**: emerging (Willison's report; forum existence confirmed; causal attribution to
  AI-generated volume is Willison's characterization, not stated in the AGENTS.md itself)
- **Quote**: (no direct quote from Willison's blog post prose available; see paraphrase in Our assessment)
- **Our assessment**: Creating a separate infrastructure channel for bug reports is a concrete
  organizational response to agent activity — not a policy change on paper but a system
  architecture change in practice. This parallels Pi's auto-close mechanism
  (`blog-ronacher-pi-oss.md` Claim 8: 79% auto-close rate for external issues) and Zig's
  triage burden before the ban (`blog-simonwillison-zig-anti-ai.md` Claim 9). The routing
  approach is notable: unlike Pi's auto-close (same queue, filtered out) SQLite routes
  AI-generated bug reports to a separate queue — acknowledging they may have value while
  handling them differently from human-initiated reports.

### Claim 5: D. Richard Hipp, SQLite's creator and lead developer, has been actively addressing agent-generated bug reports with code commits in the Bug Forum

- **Evidence**: Simon Willison's observation in his blog post.
- **Confidence**: anecdotal (Willison's characterization; not independently verified)
- **Quote**: (no direct quote from Willison's blog post prose available; see paraphrase in Our assessment)
- **Our assessment**: If accurate, the graduated policy (accept agentic bug reports with
  reproducible tests, reject agentic code) is not merely a deflection — the project founder
  is personally acting on accepted reports. This validates the policy design: the accepted
  tier generates actionable signal the project actually uses. The rejected tier (code) would
  require maintainers to review, evaluate, and reimplement at scale, which is unsustainable.
  The distinction is between actionable information (reproduce → fix yourself) vs. work
  product (review + reimplement or reject). D. Richard Hipp's active engagement in the Bug
  Forum is the clearest evidence that the graduated model is designed to work, not to deflect.

### Claim 6: SQLite's AGENTS.md serves a dual purpose — governance of what agents may contribute, and technical context for how agents should operate in the codebase

- **Evidence**: The full AGENTS.md includes sections on Project Nature, Build, Testing,
  Architecture, Do Not Edit Generated Files, Coding Conventions, Extensions, and Useful
  References. The governance content is roughly three paragraphs; the technical context is
  the remaining ~80% of the document.
- **Confidence**: settled (the file structure itself demonstrates this dual purpose)
- **Quote**: "Guidance for AI coding agents working in this repository." (opening line of AGENTS.md)
- **Our assessment**: Most policy discussion around AGENTS.md focuses on governance (what
  agents may or may not do). The SQLite AGENTS.md demonstrates that the format is also a
  technical onboarding document. An agent that reads only the governance section and skips
  the rest is missing concrete operational constraints: wrong VCS (Fossil, not Git), wrong
  build system (autosetup, not GNU Autoconf), generated files that must not be touched,
  memory allocation conventions. The dual-purpose structure means that "AGENTS.md as
  governance" and "AGENTS.md as context" are not separate concerns — they are the same
  document serving both needs simultaneously.

### Claim 7: SQLite uses Fossil for version control and autosetup for configuration — not Git and not GNU Autoconf — making common agent assumptions incorrect without AGENTS.md context

- **Evidence**: Verbatim text from AGENTS.md
- **Confidence**: settled (stated directly in AGENTS.md; consistent with SQLite's publicly
  known infrastructure)
- **Quote**: "SQLite uses the [Fossil](https://fossil-scm.org/) for version control, not Git.  The canonical repository is at <https://sqlite.org/src>."
- **Our assessment**: Without reading AGENTS.md, a coding agent would default to git commands,
  which would fail immediately. The "not X" framing ("not Git", "not GNU Autoconf") is
  effective context engineering: it anticipates the agent's likely prior assumption and
  explicitly corrects it. Stating what something is NOT, in addition to what it is, prevents
  the high-confidence wrong action more reliably than just stating what it is. This pattern
  is generalizable to any AGENTS.md author who anticipates that an agent's training bias
  will cause it to reach for the wrong tool.

### Claim 8: The AGENTS.md explicitly lists seven generated files that must never be edited by hand, with the script to regenerate each

- **Evidence**: Verbatim table from AGENTS.md (see Concrete Artifacts)
- **Confidence**: settled (verbatim from primary document)
- **Quote**: "These files are produced by scripts and must not be edited by hand"
- **Our assessment**: This is a concrete example of "invariant documentation" — the document
  states what the agent must never do and provides the correct alternative. `blog-ronacher-pi-oss.md`
  Claim 7 argues that AI agents default to adding permissive handling rather than enforcing
  invariants ("The clanker's present-day behavior is to just assume that no such invariants
  exist, and instead to make the system work with all kinds of malformedness"). The
  generated-files table is the structural response: explicit documentation of files-off-limits
  with correct alternatives. An agent without this context will generate patches touching
  generated files; such patches will be rejected. The table makes the constraint
  machine-actionable: the agent doesn't need to infer which files are generated — they are listed.

### Claim 9: The AGENTS.md specifies that all memory allocation must go through sqlite3Malloc, never raw malloc — a semantic invariant that an agent would violate by default

- **Evidence**: Verbatim text from AGENTS.md coding conventions section
- **Confidence**: settled (verbatim from primary document)
- **Quote**: "All memory allocation goes through `sqlite3Malloc` / `sqlite3_malloc64` (never raw `malloc`). The `sqlite3MallocZero` variant zero-initializes."
- **Our assessment**: This is a semantic invariant that a competent C programmer (human or AI)
  would naturally violate, because C code defaults to malloc(). The AGENTS.md explicitly names
  the pattern and forbids the default. This represents a category of constraint that requires
  explicit documentation: not a structural constraint (file permissions, wrong VCS) but a
  semantic one (which function to call for a common operation). The fact that the document
  names this suggests it was written by someone who reasoned about what mistakes an
  agent would make — including correct-looking mistakes that pass a code review by a human
  unfamiliar with SQLite's conventions.

### Claim 10: The 2026 pattern of major OSS projects adding AI-contribution policies represents a new governance layer that practitioners operating agentic systems must discover before interacting with a project

- **Evidence**: Simon Willison's tagging of the post (sqlite, ai, d-richard-hipp,
  generative-ai, llms, coding-agents, ai-security-research) frames it as a general-interest
  policy development. At minimum three documented cases exist (Zig, SQLite, Pi) with
  materially different policy models.
- **Confidence**: emerging (three documented independent cases; extrapolation)
- **Quote**: (no direct quote available; see paraphrase in Our assessment)
- **Our assessment**: The three documented cases (Zig: blanket ban; SQLite: graduated policy;
  Pi: auto-close + separate infrastructure) form a taxonomy of OSS responses to agent
  activity. The implication for practitioners: before deploying an agent that interacts with
  an external OSS project, the agent should discover and read that project's AGENTS.md or
  equivalent policy document. The policies are not static — SQLite's hardening demonstrates
  they evolve. Checking for AGENTS.md is a standard pre-flight check, not a one-time
  configuration.

## Concrete Artifacts

### SQLite AGENTS.md — Full Governance Section (Project Nature)

Source: https://sqlite.org/src/raw/AGENTS.md?ci=trunk (fetched 2026-06-06, verbatim)

```
Guidance for AI coding agents working in this repository.

## Project nature

SQLite is a self-contained, serverless SQL database engine written in C. The
source is **public domain** — no copyright or license header should ever be
added to any file. The blessing comment that appears at the top of each source
file is intentional and should be preserved unchanged.

SQLite does not accept pull requests without prior agreement and/or
accompanying legal paperwork that places the pull request in the public domain.
However, the human SQLite developers will review a concise and well-written
pull request as a proof-of-concept prior to reimplementing the changes
themselves.

SQLite does not accept agentic code.  However the project
will accept agentic bug reports that include a reproducible test case.
Patches or pull requests demonstrating a possible fix, for documentation
purposes, are welcomed.

SQLite uses the [Fossil](https://fossil-scm.org/) for version control,
not Git.  The canonical repository is at <https://sqlite.org/src>.
```

### SQLite AGENTS.md — Build Commands

Source: https://sqlite.org/src/raw/AGENTS.md?ci=trunk (fetched 2026-06-06, verbatim)

```bash
apt install gcc make tcl-dev   # prerequisites (Debian/Ubuntu)

./configure --dev              # debug build
make sqlite3                   # CLI shell
make sqlite3d                  # Debugging variant of the CLI shell
make sqlite3.c                 # amalgamation (single-file distribution form)
make testfixture               # test runner binary (requires tcl-dev)
make tclextension-install      # install TCL extension before running tests
```

### SQLite AGENTS.md — Test Execution and the "always run devtest" requirement

Source: https://sqlite.org/src/raw/AGENTS.md?ci=trunk (fetched 2026-06-06, verbatim)

```bash
# From the build directory:
./testfixture test/main.test   # single test file
test/testrunner.tcl            # quick suite
test/testrunner.tcl full       # full suite
test/testrunner.tcl fts5%      # pattern match

# Check for failures:
grep '!' testrunner.log
```

`make devtest` is the fastest way to run a representative subset. Always run
at least `devtest` after any change to `src/`.

### SQLite AGENTS.md — Generated Files Table (must not be edited by hand)

Source: https://sqlite.org/src/raw/AGENTS.md?ci=trunk (fetched 2026-06-06, verbatim)

```
## Do not edit generated files

These files are produced by scripts and must not be edited by hand:

| File | Regenerate with |
|---|---|
| `sqlite3.h` | `tool/mksqlite3h.tcl` |
| `parse.c`, `parse.h` | build lemon (`tool/lemon.c`) then run on `src/parse.y` |
| `opcodes.h` | `tool/mkopcodeh.tcl` (reads `src/vdbe.c`) |
| `opcodes.c` | `tool/mkopcodec.tcl` (reads `opcodes.h`) |
| `keywordhash.h` | `tool/mkkeywordhash.c` |
| `pragma.h` | `tool/mkpragmatab.tcl` |
| `sqlite3.c` | `tool/mksqlite3c.tcl` (the amalgamation) |

Editing rules:
- To add a PRAGMA: edit `tool/mkpragmatab.tcl`, then regenerate `pragma.h`.
- To add a VDBE opcode: add the `case OP_Xxx:` handler in `src/vdbe.c`; the
  opcode number and name are extracted automatically by `mkopcodeh.tcl`.
- To change the SQL grammar: edit `src/parse.y`, not `parse.c`.
```

### SQLite AGENTS.md — Coding Conventions

Source: https://sqlite.org/src/raw/AGENTS.md?ci=trunk (fetched 2026-06-06, verbatim)

```
- C89/C99 compatible C only. No C++, no STL, no exceptions, no VLAs.
- All memory allocation goes through `sqlite3Malloc` / `sqlite3_malloc64`
  (never raw `malloc`). The `sqlite3MallocZero` variant zero-initializes.
- Integer widths: use `i64` (`sqlite3_int64`) for 64-bit values, `u32`/`u64`
  for unsigned. Avoid bare `long` or `int` for values that could exceed 2G.
- Error propagation: functions return `SQLITE_OK` (0) on success and a
  `SQLITE_*` error code on failure. Many routines also set `db->mallocFailed`
  on OOM, allowing deferred error checking.
- Assert liberally for invariants that must hold in correct code; use
  `ALWAYS(x)` / `NEVER(x)` for conditions that are logically always
  true/false but that the compiler cannot prove.
```

### Policy Comparison: OSS AI-Contribution Policies (2026)

```
Zig (ziglang.org)    — BLANKET BAN
  Rule:   "No LLMs for issues. No LLMs for pull requests. No LLMs for
           comments on the bug tracker, including translation."
  Reason: Contributor-poker philosophy — reviewer time invests in people,
          not code; LLM-assisted PRs break that investment loop.
  Infra:  No separate channel; blanket prohibition.
  Source: blog-simonwillison-zig-anti-ai.md Claim 1

SQLite (sqlite.org)  — GRADUATED POLICY
  Tier 1: Agentic code                                  → NOT ACCEPTED
  Tier 2: Agentic bug reports + reproducible test case  → ACCEPTED
  Tier 3: Patches/PRs as documentation of a possible fix → ACCEPTED
  Reason: Implied — accepts signal + verification, rejects work product.
  Infra:  Separate Bug Forum created for AI-generated reports.
  Source: This note (blog-simonwillison-sqlite-agents-md.md) Claim 1

Pi (github.com/earendilair/pi) — VOLUME MANAGEMENT
  Approach: Auto-close all contributions from non-approved individuals;
            ~79% auto-close rate on external issues/PRs (3,145 in 90 days).
  Reason:  Volume pressure; separate triage workflow with /is command.
  Infra:   Auto-close + separate investigation workflow, not separate channel.
  Source: blog-ronacher-pi-oss.md Claim 8
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-zig-anti-ai.md` Claim 9: "Practical LLM-assisted OSS contributions
    caused concrete operational harm to the Zig project before the ban" — the Zig post quotes
    "from an increase in background noise due to worthless drive-by PRs full of hallucinations
    (that wouldn't even compile, let alone pass CI), to insane 10 thousand line long first time
    PRs." SQLite's Bug Forum creation and policy hardening (this source, Claims 3 and 4) document
    the same phenomenon independently: AI-generated contributions created sufficient volume to
    require organizational response. Two independent major OSS projects converging on the same
    operational problem.
  - `blog-ronacher-pi-oss.md` Claim 8: "Pi's public GitHub tracker received 3,145 external
    issues/PRs in 90 days; 2,504 were auto-closed" — the same volume-driven infrastructure
    response. Pi created auto-close infrastructure; SQLite created a separate Bug Forum. Both
    are operational responses to AI-generated contribution volume.
  - `paper-gloaguen-agentsmd-effectiveness.md` Claim 4: "Agents faithfully follow instructions
    in context files, including tool-specific directives" with measured compliance rates (tool
    mentions increase usage 1.6–2.5x per instance). SQLite's governance constraints and
    technical invariants in AGENTS.md (Claims 1, 7, 8, 9) are meaningful precisely because
    agents comply with explicit file instructions at high rates. An AGENTS.md that says "do
    not accept agentic code" doesn't prevent a human from submitting AI-generated code, but
    it does prevent a compliant agent that reads it from operating in forbidden ways.

- **Contradicts**:
  - `blog-simonwillison-zig-anti-ai.md` Claim 1 (Zig's blanket ban on all AI contributions
    including bug reports) vs. this source Claim 1 (SQLite's acceptance of agentic bug reports
    with reproducible test cases): these represent materially different policy choices that
    would lead to different practitioner advice. Zig says no AI contributions at all; SQLite
    says AI contributions are acceptable if they provide reproducible test cases. No
    contradiction issue filed because both claims accurately describe the respective projects'
    actual policies — this is a divergence in design philosophy between independent projects,
    not a factual contradiction. The guide should present both models and note that the "right"
    policy depends on project philosophy (contributor development vs. operational efficiency).

- **Extends**:
  - `blog-simonwillison-zig-anti-ai.md` overall: That note established the OSS AI-policy
    pattern with one data point (blanket ban). This source adds a second data point (graduated
    policy) and provides the full AGENTS.md text as a primary source artifact. Together, the
    two sources define the policy-space options available to OSS maintainers.
  - `blog-ronacher-pi-oss.md` Claim 7: "The clanker's present-day behavior is to just assume
    that no such invariants exist, and instead to make the system work with all kinds of
    malformedness." The SQLite AGENTS.md addresses exactly this failure mode through explicit
    invariant documentation: the generated-files table (Claim 8) and memory allocation
    conventions (Claim 9). Ronacher names the problem; SQLite's AGENTS.md demonstrates
    the structural countermeasure.
  - `paper-gloaguen-agentsmd-effectiveness.md` overall: The paper studies how AGENTS.md
    affects agent task-success rates in benchmark settings. This source adds the governance
    use case — AGENTS.md as an external-agent constraint mechanism — which the paper does not
    study. Together they describe AGENTS.md's dual role: technical context file (paper) and
    governance policy for external agents (this source).

- **Novel**:
  - **Graduated OSS AI-contribution policy as a documented pattern**: No existing corpus
    source documents a major project adopting a tiered (graduated) AI-contribution policy
    rather than a blanket ban. SQLite's three-tier structure (no code / yes bug reports with
    tests / yes documentation patches) is the first corpus example of this policy design.
  - **Policy hardening as active response to observed agent behavior**: The removal of
    "(currently)" from an existing policy statement — tracked as a specific commit — is the
    first corpus documentation of a project actively strengthening an AI policy in response
    to observed agent activity, rather than setting policy preemptively. Other corpus sources
    document policies at a point in time; this source documents policy evolution.
  - **AGENTS.md as governance mechanism for external agents**: Prior corpus coverage of
    AGENTS.md (`paper-gloaguen-agentsmd-effectiveness.md`) focuses on agents working inside
    the project on assigned tasks. This source documents AGENTS.md as a governance mechanism
    aimed at external agents — agents not affiliated with the project that might attempt to
    contribute. This is a different use case requiring a different design perspective.
  - **Infrastructure routing as organizational response**: Creating a separate channel for
    AI-generated contributions (rather than policy-level rejection alone) is not documented
    in prior corpus sources. The routing approach implicitly acknowledges that AI-generated
    reports may have value — they are handled differently, not discarded wholesale.
  - **"Not X" framing in AGENTS.md**: Explicitly stating what the project does NOT use
    ("not Git", "not GNU Autoconf") to counteract default agent assumptions is a concrete
    context-engineering pattern not articulated in prior corpus notes.

## Guide Impact

- **Chapter 01 (Agent Engineering and Governance)**: Add the OSS AI-contribution policy
  taxonomy as a new pattern. Three documented models exist: (1) blanket ban (Zig — all AI
  contributions prohibited, contributor-poker rationale), (2) graduated policy (SQLite — no
  code, yes bug reports with tests, yes documentation patches), (3) volume management
  infrastructure (Pi — auto-close + separate routing). Each is a defensible choice with
  different trade-offs. The guide should not prescribe one; it should help practitioners
  understand the design space. Cite this source for Claims 1–5 on the graduated model.

- **Chapter 02 (Harness Engineering)**: Recommend that agentic systems interacting with
  external OSS projects should discover and read AGENTS.md before operating. The SQLite
  case provides concrete evidence: a coding agent that doesn't read AGENTS.md will try
  to use git (wrong VCS), touch generated files (forbidden), use raw malloc (convention
  violation), and may submit agentic code (policy violation). Reading AGENTS.md first
  prevents all four failures. Add the "not X" framing observation (Claim 7) as a concrete
  AGENTS.md authoring pattern: when a project uses atypical tooling, explicitly stating
  what it does NOT use prevents high-confidence wrong actions.

- **Chapter 03 (Safety and Verification)**: Add the "reproducible test case" requirement
  (Claim 1) as a model for agent-generated verification. The SQLite policy does not say
  "AI bug reports are acceptable" — it says "AI bug reports with reproducible test cases
  are acceptable." The reproducibility requirement is a verification gate that filters
  conjecture from evidence. For teams designing agent workflows that output bug reports,
  tickets, or issues, this is an actionable model: require the agent to include
  machine-verifiable evidence (a test that reproduces the bug), not just descriptive text.

- **Chapter 04 (Deployment Patterns and Project Governance)**: Add policy hardening (Claim 3)
  as evidence that AI-contribution policies are living governance artifacts. The removal of
  "(currently)" is an observable policy evolution event driven by real-world agent behavior.
  Teams building agents that interact with external projects should not assume policies are
  static — checking for recent AGENTS.md changes is part of responsible agentic deployment.

- **Chapter 05 (Team Adoption)**: Add the dual-purpose AGENTS.md recommendation (Claim 6).
  A well-written AGENTS.md serves two audiences simultaneously: agents working inside the
  project (technical context: build, test, conventions) and external agents attempting to
  contribute (governance: what is and is not accepted). Teams that have written AGENTS.md
  only for internal use should audit it for external-agent governance completeness.

## Extraction Notes

- **Primary source access**: The Simon Willison blog post at
  https://simonwillison.net/2026/May/27/sqlite-agents/ was fetched twice; both fetches
  returned AI-summarized rather than verbatim text (tool processing behavior). The SQLite
  AGENTS.md was fetched verbatim from https://sqlite.org/src/raw/AGENTS.md?ci=trunk — all
  AGENTS.md quotes in this note are from the primary document, not Willison's reproduction.
  The SQLite Bug Forum at https://sqlite.org/bugs/forum was fetched and confirmed to exist.
- **Verbatim constraint**: Due to summarization of the Willison blog post, no verbatim quotes
  from the post's prose were extracted. All Claims with Quote fields referencing Willison's
  commentary are marked "(no direct quote from Willison's blog post prose available; see
  paraphrase in Our assessment)" per MINER.md §2a. All AGENTS.md quotes are verbatim.
- **The "(currently)" commit**: Willison reports a specific commit removing "(currently)" from
  the agentic code restriction. The current AGENTS.md text confirms the qualifier is absent.
  The commit itself was not independently accessed. Claims 3 rated `emerging` accordingly.
- **Contradiction assessment**: Zig's blanket ban vs. SQLite's graduated policy creates a
  policy contrast, but both claims are accurate descriptions of different projects' actual
  policies. No material contradiction requiring a contradiction issue exists — these are
  different projects making different design choices.
- **Cross-reference verification** (per MINER.md §4b):
  - `blog-simonwillison-zig-anti-ai.md` Claim 9 verified at lines 169–184 of that note:
    "Practical LLM-assisted OSS contributions caused concrete operational harm to the Zig
    project before the ban." Content matches citation.
  - `blog-ronacher-pi-oss.md` Claim 8 verified at lines 167–185: "Pi's public GitHub tracker
    received 3,145 external issues/PRs in 90 days; 2,504 were auto-closed." Content matches.
  - `blog-ronacher-pi-oss.md` Claim 7 verified at lines 146–164: "The correct response to
    bad persisted data is to make bad state impossible, not to handle it — but AI agents
    default to the opposite." Content matches citation.
  - `paper-gloaguen-agentsmd-effectiveness.md` Claim 4 verified at lines 87–90: "Agents
    faithfully follow instructions in context files, including tool-specific directives."
    Content matches citation.
- **SQLite AGENTS.md URL**: The SQLite AGENTS.md file accessible via
  https://sqlite.org/src/raw/AGENTS.md?ci=trunk returns verbatim raw content. The primary
  source for all governance and technical claims is this file, not Willison's reproduction.
  The file is substantially larger than the governance section — the Build, Testing,
  Architecture, Coding Conventions, and Extensions sections were all read and are reproduced
  in Concrete Artifacts.
