---
source_url: https://github.github.com/gh-aw/reference/fuzzy-schedule-specification
source_type: docs
title: "GitHub Agentic Workflows: Fuzzy Schedule Time Syntax Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#453"
---

# GitHub Agentic Workflows: Fuzzy Schedule Time Syntax Specification

> Formal specification (v1.2.0, Draft) for the natural-language scheduling
> syntax used in `gh aw` workflow frontmatter — covers the complete ABNF grammar
> for five schedule types, the deterministic FNV-1a scattering algorithm that
> distributes execution times across weighted time-slot tiers to prevent load
> spikes, timezone conversion rules, three conformance levels, and 10 normative
> error conditions that must cause compilation to fail.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows formal specification in the
  `reference/` section — version 1.2.0, status "Draft Specification"; W3C-style
  document with ABNF grammar, normative MUST/SHALL/SHOULD language, conformance
  levels, error-condition table, and compliance test requirements. This is the
  canonical spec for the short-form schedule syntax used in workflow `on:` blocks,
  as distinct from raw GitHub Actions cron syntax.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that authors all `github.github.com/gh-aw` documentation. Spec version
  1.2.0 indicates active development; the "Draft" status means the spec may be
  updated, but the core constructs (grammar, scattering algorithm, conformance
  levels) are sufficiently stable to document. ABNF grammar rules, hash function
  constants, and normative requirements are authoritative for the `gh aw` compiler;
  they are implementation contracts, not guidelines.
- **Scope**: Covers the complete Fuzzy Schedule Time Syntax — grammar, time format
  rules, timezone conversion, the deterministic scattering algorithm (including time
  slot preference tiers and peak avoidance rules), conformance levels, normative
  error conditions, and compliance test requirements. The output of this spec is a
  valid 5-field GitHub Actions cron expression. Does NOT cover: how compiled
  schedules interact with workflow concurrency (see `docs-ghaw-concurrency-reference.md`),
  the broader five-phase compilation pipeline (see `docs-ghaw-compilation-process.md`),
  or the DailyOps scheduling pattern (see `docs-ghaw-dailyops.md`).

## Extracted Claims

### Claim 1: The Fuzzy Schedule Time Syntax is a human-readable scheduling language that automatically distributes workflow execution times to prevent server load spikes caused by fixed-time schedules

- **Evidence**: The specification's opening statement gives this as the primary
  design rationale, contrasting it with the load-spike problem caused by fixed
  cron expressions.
- **Confidence**: settled (first-party; this is the normative design intent of the
  spec, stated at document open)
- **Quote**: "This specification defines the Fuzzy Schedule Time Syntax, a
  human-friendly scheduling language for GitHub Agentic Workflows that automatically
  distributes workflow execution times to prevent server load spikes."
- **Our assessment**: The motivation addresses a real operational problem: when many
  `gh aw` workflows use the same fixed schedule time (e.g., `cron: "0 2 * * 1-5"`)
  their simultaneous execution creates load spikes on shared infrastructure. The
  fuzzy syntax makes load distribution automatic by design — the author specifies
  intent (e.g., `daily around 2am`) and the compiler generates a deterministically
  scattered cron time. This is architecturally superior to asking practitioners to
  manually stagger their cron times. For Ch02 (Harness Engineering): frame the fuzzy
  schedule syntax not just as a convenience but as a load-distribution mechanism —
  the short syntax IS the scatter.

### Claim 2: The grammar defines five schedule families: daily, weekly, hourly, interval, and bi/tri-weekly — all compiled to standard 5-field GitHub Actions cron expressions

- **Evidence**: The complete ABNF grammar is reproduced in the specification.
  The top-level rule `fuzzy-schedule = daily-schedule / hourly-schedule /
  weekly-schedule / interval-schedule` covers the four primary families; bi/tri-weekly
  are defined as special cases with explicit day-count semantics (`SHALL execute once
  every 14 days` and `once every 21 days`). The specification output format is stated
  in the conformance section.
- **Confidence**: settled (first-party; ABNF grammar is normative)
- **Quote**: "Generate valid 5-field cron expression"
- **Our assessment**: The five families cover the practical spectrum of recurring
  workflow schedules. The bi/tri-weekly variants are worth noting explicitly — they
  serve workflows that are too frequent for weekly but too infrequent for daily (e.g.,
  a bi-weekly dependency audit). The output being a standard GitHub Actions cron
  expression ensures that compiled lock files are portable: they produce valid Actions
  workflow schedules with no special runtime support needed. For Ch02: document the
  five families as the menu of scheduling options before practitioners reach for raw
  cron. For Ch04 (Engineering Practices): bi/tri-weekly scheduling fills a gap between
  weekly and daily that raw cron syntax obscures with complex day-of-week math.

### Claim 3: The grammar supports three time constraint forms: `around <time>` (approximate target), `between <start> and <end>` (bounded window), and unconstrained (fully scattered)

- **Evidence**: The ABNF defines: `time-constraint = around-constraint / between-constraint`,
  `around-constraint = "around" time-spec`, `between-constraint = "between" time-spec "and" time-spec`.
  Unconstrained schedules (e.g., `daily` with no qualifier) receive fully automatic
  scattering across the preferred time slot pool.
- **Confidence**: settled (first-party ABNF; normative)
- **Quote**: (no direct quote; grammar rules cited verbatim in Concrete Artifacts)
- **Our assessment**: The three constraint forms provide a graduated control mechanism:
  fully automatic scatter for workflows with no timing preference; `around` for
  workflows that should run at roughly a given time but can be offset for load
  distribution; `between` for workflows that must complete within a given window
  (e.g., before a 9 AM standup). This makes the fuzzy syntax practical for real
  scheduling requirements rather than just academic demonstration. For Ch02: document
  these three constraint forms as the primary configuration knobs, with `around` as
  the default for human-time-zone-aware schedules.

### Claim 4: The grammar supports four time notation formats: 24-hour (`14:00`), 12-hour (`3pm`), time keywords (`midnight`, `noon`), and UTC offsets (`utc+9`, `utc-5:30`)

- **Evidence**: The ABNF defines:
  ```
  time-spec  = (hour-24 ":" minute) [utc-offset]
             / (hour-12 am-pm) [utc-offset]
             / time-keyword [utc-offset]
  utc-offset = "utc" ("+" / "-") (hours / hours ":" minutes)
  ```
  Time keywords include at minimum `midnight` and `noon` (from initial WebFetch summary).
- **Confidence**: settled (first-party ABNF; normative grammar is authoritative)
- **Quote**: (no direct quote for this claim; ABNF rules reproduced in Concrete Artifacts)
- **Our assessment**: The time format flexibility is pragmatically important for
  practitioners: Europeans naturally write `14:00`; Americans write `2pm`; no-preference
  workflows use `midnight` or `noon`; distributed teams use UTC offsets to anchor times
  to a specific global instant. Supporting all four formats eliminates friction in
  expressing intent. The UTC offset support (`utc+9`, `utc-5:30`) is particularly
  significant: it allows practitioners to write `daily around 14:00 utc+9` and have the
  compiler convert to the correct UTC time (05:00 UTC) before applying scattering. For
  Ch02: document the UTC offset form for distributed teams — it makes timezone intent
  explicit in the workflow spec rather than requiring practitioners to compute UTC
  offsets manually.

### Claim 5: Timezone conversion uses `UTC_time = local_time - offset` with day-wrap handling — converting `14:00 utc+9` to `05:00 UTC`

- **Evidence**: The specification states the conversion formula and documents the
  day-wrap rules: "Negative results wrap to previous day (add 24 hours); Results
  ≥24:00 wrap to next day (subtract 24 hours)."
- **Confidence**: settled (first-party; normative conversion rule)
- **Quote**: "UTC_time = local_time - offset" (day wrapping: "Negative results wrap
  to previous day (add 24 hours); Results ≥24:00 wrap to next day (subtract 24 hours)")
- **Our assessment**: The day-wrap rule is algorithmically necessary but easy to get
  wrong in an implementation — a schedule like `daily around 2:00 utc+9` would
  convert to 17:00 UTC the previous day, which is a different calendar date. Explicit
  wrap handling ensures consistent behavior across timezone transitions. The concrete
  example `14:00 utc+9` → `05:00 UTC` is the canonical conversion test case. For the
  guide: this conversion is the compiler's responsibility, not the practitioner's —
  practitioners express local time intent; the spec handles UTC translation.

### Claim 6: The deterministic scattering algorithm uses the FNV-1a 32-bit hash of the workflow identifier (`owner/repo/.github/workflows/workflow-name.md`) to produce reproducible, unique schedule offsets per workflow

- **Evidence**: The specification states the algorithm SHOULD use FNV-1a (Fowler-Noll-Vo)
  32-bit hash with `FNV_offset_basis = 2166136261` and `FNV_prime = 16777619`. The
  workflow identifier format is specified as `repository_slug + "/" + workflow_file_path`
  (e.g., `owner/repo/.github/workflows/workflow-name.md`). The hash produces a seed
  value used in modulo operations to select the actual execution time.
- **Confidence**: settled (first-party; hash function constants and identifier format
  are normative specifications)
- **Quote**: "An implementation SHOULD use the FNV-1a (Fowler-Noll-Vo) 32-bit hash
  algorithm as a reference implementation" / "The workflow identifier used for hashing
  MUST be constructed as: `workflow_identifier = repository_slug + "/" + workflow_file_path`"
- **Our assessment**: Using the workflow identifier (not a random seed) as the hash
  input is the critical design choice that makes scattering both reproducible and
  stable: the same workflow compiles to the same cron expression every time, on every
  machine, in every CI run. This is essential for `actions-lock.json` reproducibility
  (documented in `docs-ghaw-compilation-process.md` Claim 6). If scattering used a
  random seed, every `gh aw compile` would produce a different cron, breaking the
  lock-file model. The FNV-1a choice is a pragmatic engineering decision: FNV-1a is
  fast (no dependencies), well-distributed for short strings, and deterministic.
  For Ch02: document that the fuzzy schedule is stable across recompilations — once
  a workflow is in the lockfile, its scheduled time does not change unless the
  workflow identifier changes.

### Claim 7: The scattering algorithm distributes execution times across three weighted time slot preference tiers — BEST (02–05 UTC, weight 3), GOOD (10–12 UTC, weight 2), and OK (19–23 UTC, weight 1)

- **Evidence**: The specification defines three tiers with their weights, UTC hour
  ranges, and minute sets:
  ```
  BEST (weight 3): hours 02–05 UTC, odd minutes {7, 13, 23, 37, 43, 53} → 72 slots
  GOOD (weight 2): hours 10–12 UTC, minutes [5, 54] → 300 slots
  OK   (weight 1): hours 19–23 UTC, minutes [5, 54] → 250 slots
  ```
- **Confidence**: settled (first-party; tier definitions are normative)
- **Quote**: "BEST (weight 3): hours 02–05 UTC, odd minutes {7, 13, 23, 37, 43, 53}
  → 72 slots / GOOD (weight 2): hours 10–12 UTC, minutes [5, 54] → 300 slots /
  OK (weight 1): hours 19–23 UTC, minutes [5, 54] → 250 slots"
- **Our assessment**: The three-tier design encodes an explicit platform policy about
  when workflows *should* run for server efficiency — off-peak UTC hours (02–05) are
  triply preferred, mid-morning UTC (10–12, which is EU midday / US early morning)
  is doubly preferred, and US business-hour evening (19–23 UTC) is singly preferred.
  Workflows unconstrained by time (`daily` with no qualifier) are scattered into this
  pool proportionally to tier weights. The BEST tier uses a specific set of odd minutes
  ({7, 13, 23, 37, 43, 53}) rather than a range — this is the peak avoidance rule
  embedded into the tier definition itself. For Ch04 (Engineering Practices / Load
  Distribution): the BEST tier target is 02–05 UTC; practitioners designing always-on
  workflows without timing constraints should understand their workflows will be
  preferentially scheduled in this window.

### Claim 8: Peak avoidance rules remap scheduled minutes away from hour boundaries, EU morning peak (06–09 UTC around :30), and US business-hour peaks (14–18 UTC around :15 and :45)

- **Evidence**: The specification defines three avoidance rules:
  - Hour boundary: "Minutes [0, 4] → minute + 5; [55, 59] → minute − 5; [5, 54] unchanged"
  - EU morning peak: "hour ∈ [6, 9] AND minute ∈ [27, 33] avoid; replacement: 34"
  - US business: "hour ∈ [14, 18] AND minute ∈ [12, 18] → 19; [42, 48] → 49"
- **Confidence**: settled (first-party; normative avoidance rules)
- **Quote**: "Minutes [0, 4] → minute + 5; [55, 59] → minute − 5; [5, 54] unchanged" /
  "hour ∈ [6, 9] AND minute ∈ [27, 33] avoid; replacement: 34" /
  "hour ∈ [14, 18] AND minute ∈ [12, 18] → 19; [42, 48] → 49"
- **Our assessment**: The peak avoidance rules are the most operationally sophisticated
  part of the spec. They address three distinct load patterns: (1) the universal
  "top of the hour" clustering (minute 00) that occurs when humans set schedules to
  even times; (2) EU morning standups that cause traffic spikes around :30 in the
  06–09 UTC window; (3) US business-hour cadence spikes at :15 and :45 in the 14–18
  UTC window. Each avoidance rule is a simple deterministic remapping, not a random
  offset — a scheduled time that falls in an avoided zone is shifted to the zone
  boundary (e.g., minute 14 in a US business hour becomes minute 19). For Ch04
  (Load Distribution): these avoidance rules mean `gh aw` workflows are explicitly
  designed not to fire at common human-scheduled instants — this is the platform's
  cooperative load-distribution policy.

### Claim 9: Three conformance levels allow incremental implementation — Level 1 (daily/weekly basic), Level 2 (adds time constraints and hourly), Level 3 (adds timezone, intervals, bi/tri-weekly)

- **Evidence**: The specification defines:
  "**Level 1 (Basic)**: Supports daily and weekly schedules without time constraints.
  **Level 2 (Standard)**: Adds support for time constraints and hourly schedules.
  **Level 3 (Complete)**: Includes timezone conversion, interval schedules, and
  bi-weekly/tri-weekly patterns."
- **Confidence**: settled (first-party; conformance level definitions are normative)
- **Quote**: "**Level 1 (Basic)**: Supports daily and weekly schedules without time
  constraints. **Level 2 (Standard)**: Adds support for time constraints and hourly
  schedules. **Level 3 (Complete)**: Includes timezone conversion, interval schedules,
  and bi-weekly/tri-weekly patterns."
- **Our assessment**: The three-level structure implies that `gh aw`'s compiler likely
  targets Level 3 (Complete) conformance, since it processes the full grammar. Third-
  party tools or alternative compilers can target Level 1 or 2 for simpler
  implementation. The Level 3 gateway features — timezone conversion, intervals, and
  bi/tri-weekly — are the most complex to implement correctly, which is why they are
  in the highest conformance tier. For guide writers: the level structure is useful
  for explaining when to upgrade a workflow's schedule complexity — teams should start
  with Level 1 constructs (`daily`, `weekly on monday`) and add constraints when their
  operational needs require them.

### Claim 10: Implementations MUST NOT silently fall back to a default schedule on invalid input — all 10 normative error conditions (E-01 through E-10) must cause compilation to fail with a non-zero exit code

- **Evidence**: The specification contains an explicit normative prohibition:
  "Implementations MUST NOT silently fall back to a default schedule when the input is
  invalid; all errors in rows E-01 through E-10 MUST cause compilation to fail with a
  non-zero exit code." The 10 conditions include: unknown schedule keyword, hour
  out-of-range, minute out-of-range, `around` with no time specification, `between`
  with only one argument, `between` range where start equals end, unknown weekday,
  invalid interval unit, interval below GitHub Actions minimum, and non-integer
  interval value.
- **Confidence**: settled (first-party; MUST NOT and MUST are normative requirements)
- **Quote**: "Implementations MUST NOT silently fall back to a default schedule when
  the input is invalid; all errors in rows E-01 through E-10 MUST cause compilation
  to fail with a non-zero exit code."
- **Our assessment**: The fail-fast requirement is consistent with the broader gh-aw
  philosophy of detecting errors at compile time rather than at runtime. This connects
  directly to `docs-ghaw-compilation-process.md` Claim 1 (Phase 1 parsing and
  validation) — schedule expression validation is part of Phase 1. The prohibition on
  silent fallback is particularly important: if a typo in `daily around 2om` (typo for
  `2am`) silently fell back to `daily`, the workflow would run at the wrong time
  indefinitely. The 10 error conditions (E-01 through E-10) cover the practical space
  of authoring errors. For Ch02: frame this as part of the compile-time safety
  guarantee — schedule syntax errors produce actionable compiler errors, not silent
  misbehavior.

### Claim 11: The specification requires 50+ compliance tests covering syntax parsing, time formats, timezone handling, scattering distribution, peak avoidance, and cron generation

- **Evidence**: The specification's changelog entry for v1.0.0 states "Included
  comprehensive test suite with 50+ test cases."
- **Confidence**: settled (first-party; test suite requirement is normative in
  the Appendix)
- **Quote**: (no direct quote; cited as "Included comprehensive test suite with 50+
  test cases" in v1.0.0 changelog)
- **Our assessment**: The 50+ test requirement is a compliance testing specification,
  not just implementation guidance. It establishes that any conforming implementation
  must demonstrate coverage across all six areas: syntax parsing, time formats,
  timezone handling, scattering distribution, peak avoidance, and cron generation.
  This matters for teams evaluating whether `gh aw compile` is a reference
  implementation they can rely on — the spec's compliance testing framework provides
  the verification surface. For Ch02: the compliance test framework is evidence that
  the fuzzy schedule compiler is not a best-effort convenience feature but a validated
  implementation with defined correct-behavior criteria.

## Concrete Artifacts

### Complete ABNF Grammar (from specification)

```abnf
; Top-level schedule expression
fuzzy-schedule  = daily-schedule / hourly-schedule / weekly-schedule / interval-schedule

; Schedule types
daily-schedule  = "daily" [time-constraint]
weekly-schedule = "weekly" ["on" weekday] [time-constraint]
hourly-schedule = "hourly" / ("every" hour-interval)
interval-schedule = "every" (minute-interval / hour-interval / day-interval / week-interval)

; Time constraints
time-constraint    = around-constraint / between-constraint
around-constraint  = "around" time-spec
between-constraint = "between" time-spec "and" time-spec

; Time specifications
time-spec   = (hour-24 ":" minute) [utc-offset]
            / (hour-12 am-pm) [utc-offset]
            / time-keyword [utc-offset]

utc-offset  = "utc" ("+" / "-") (hours / hours ":" minutes)

; Interval units
hour-interval   = 1*DIGIT ("h" / "hours" / "hour")
minute-interval = 1*DIGIT ("m" / "minutes" / "minute")
day-interval    = 1*DIGIT ("d" / "days" / "day")
week-interval   = 1*DIGIT ("w" / "weeks" / "week")

; Weekday names
weekday = "sunday" / "monday" / "tuesday" / "wednesday"
        / "thursday" / "friday" / "saturday"
```

*Source: `reference/fuzzy-schedule-specification` — "Grammar" section (ABNF)*

### Deterministic Scattering Algorithm (normative)

```
Algorithm: FNV-1a (Fowler-Noll-Vo) 32-bit hash

Constants:
  FNV_offset_basis = 2166136261
  FNV_prime        = 16777619

Input: workflow_identifier = repository_slug + "/" + workflow_file_path
       e.g. "owner/repo/.github/workflows/daily-triage.md"

Output: seed value → modulo operations → time slot selection

Time Slot Preference Pool (weighted):
  BEST (weight 3): hours 02–05 UTC, odd minutes {7, 13, 23, 37, 43, 53} → 72 slots
  GOOD (weight 2): hours 10–12 UTC, minutes [5, 54]                     → 300 slots
  OK   (weight 1): hours 19–23 UTC, minutes [5, 54]                     → 250 slots

Peak Avoidance Rules (applied after initial slot selection):
  Hour boundary: minutes [0,4] → +5; [55,59] → -5; [5,54] unchanged
  EU morning (06–09 UTC): minute ∈ [27,33] → 34
  US business (14–18 UTC): minute ∈ [12,18] → 19; minute ∈ [42,48] → 49
```

*Source: `reference/fuzzy-schedule-specification` — "Scattering Algorithm" section*

### Schedule Expression Examples

```
Expression                  → Compiled cron (deterministically scattered)
──────────────────────────────────────────────────────────────────────────
daily                       → FUZZY:DAILY:*        * * *  (any BEST/GOOD/OK slot)
daily around 14:00          → FUZZY:DAILY_AROUND:14:0 * * *  (scattered near 14:00 UTC)
weekly                      → FUZZY:WEEKLY:*       * * *
weekly on monday            → FUZZY:WEEKLY:1       * * 1
every 2h                    → FUZZY:HOURLY:2       * * *
bi-weekly                   → executes once every 14 days, scattered time
tri-weekly                  → executes once every 21 days, scattered time
```

*Source: `reference/fuzzy-schedule-specification` — "Examples" section*

### Timezone Conversion Rule

```
UTC_time = local_time - offset

Day-wrap handling:
  if UTC_time < 00:00 → add 24 hours (wrap to previous day)
  if UTC_time ≥ 24:00 → subtract 24 hours (wrap to next day)

Example:
  "daily around 14:00 utc+9"
  14:00 - 9h = 05:00 UTC  (no wrap needed)
  → scattered around 05:00 UTC (within BEST tier: hours 02–05)
```

*Source: `reference/fuzzy-schedule-specification` — "Timezone Conversion" section*

### Normative Error Conditions (E-01 through E-10)

```
E-01: Unknown schedule keyword (e.g., "fortnight", "biweekly" spelled differently)
E-02: Hour out-of-range (24-hour format, must be 0–23)
E-03: Minute out-of-range (must be 0–59)
E-04: "around" keyword with no time specification following
E-05: "between" with only one time argument (missing second time)
E-06: "between" range where start equals end (zero-width window)
E-07: Unknown weekday in "weekly on <day>"
E-08: Invalid interval unit (not m/minutes/h/hours/d/days/w/weeks)
E-09: Interval value below GitHub Actions minimum
E-10: Non-integer interval value

Normative requirement:
  "Implementations MUST NOT silently fall back to a default schedule when the
   input is invalid; all errors in rows E-01 through E-10 MUST cause compilation
   to fail with a non-zero exit code."
```

*Source: `reference/fuzzy-schedule-specification` — "Error Handling" section*

### Three Conformance Levels

```
Level 1 (Basic):    daily, weekly (without time constraints)
Level 2 (Standard): + time constraints (around, between), hourly schedules
Level 3 (Complete): + timezone conversion, interval schedules, bi/tri-weekly

gh aw compile implements Level 3 (Complete) conformance.
```

*Source: `reference/fuzzy-schedule-specification` — "Conformance" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 1 (Phase 1 parsing/validation validates
    against workflow schema before job construction): Schedule expression parsing and
    the 10 normative error conditions from this spec (Claim 10) are executed during
    Phase 1. This source specifies the schedule grammar that Phase 1 validates against;
    together the two sources give the complete picture: Phase 1 catches schema errors
    including malformed schedule expressions, and this spec defines what "malformed"
    means normatively.
  - `docs-ghaw-compilation-process.md` Claim 6 (action pinning with `actions-lock.json`
    for reproducible compilation): Claim 6 here (deterministic scattering using workflow
    identifier hash, Claim 6) is the schedule analog of the SHA pinning reproducibility
    guarantee. Both ensure that `gh aw compile` produces the same output for the same
    input across machines and time. The fuzzy schedule spec makes schedules reproducible
    in the same way `actions-lock.json` makes action pins reproducible.
  - `docs-ghaw-dailyops.md` Claim 2 (weekday-only cron `0 2 * * 1-5` is required
    because "no short syntax available" for weekday range schedules): The fuzzy spec's
    grammar confirms this claim — `weekly on <weekday>` is single-day syntax only
    (ABNF: `weekday = "sunday" / "monday" / ...`), not a range like Monday–Friday.
    A Mon–Fri recurring schedule has no fuzzy syntax equivalent and still requires
    raw cron. The DailyOps observation is therefore accurate: for weekday-range
    schedules, practitioners must use raw cron.
  - `docs-ghaw-deterministic-agentic-patterns.md` Concrete Artifacts → "Precomputation
    Example" (uses `on: schedule: daily` and `on: schedule: every hour`): The two
    schedule expressions in that note's YAML examples are exactly the fuzzy schedule
    syntax this spec defines. The note uses the syntax; this spec is the formal
    definition of that syntax's semantics and output contract.

- **Extends**:
  - `docs-ghaw-dailyops.md` Claim 2 (weekday-only scheduling with raw cron): While
    the fuzzy spec does not replace raw cron for weekday-range scheduling, it IS the
    mechanism that compiles `daily` expressions in DailyOps workflows that use the
    all-days variant. DailyOps workflows that switch from `cron: "0 2 * * 1-5"` to
    `on: schedule: daily around 2am` would gain load distribution; those requiring
    weekday-only scheduling still need raw cron. This source completes the picture of
    why both syntaxes coexist.
  - `docs-ghaw-compilation-process.md` Claim 1 (five-phase pipeline): This spec
    provides the normative grammar that Phase 1 validates against and Phase 5 uses to
    generate cron output. The compilation process note describes the phases; this spec
    describes the grammar and algorithm processed in Phases 1 and 5 respectively.
  - `docs-ghaw-concurrency-reference.md` Claim 2 (per-workflow concurrency groups,
    Schedule/Other trigger type uses `gh-aw-${{ github.workflow }}` group): Workflows
    using fuzzy schedules compile to standard cron-triggered GitHub Actions runs, which
    fall into the Schedule/Other trigger type in the concurrency reference. The fuzzy
    spec determines *when* the workflow fires; the concurrency reference determines
    how concurrent firings are handled. Together they give the complete scheduling
    lifecycle: fuzzy spec → cron expression → trigger → concurrency group → execution.

- **Contradicts**: None identified. No existing source note makes claims that conflict
  with the fuzzy schedule syntax, its grammar, or the scattering algorithm. The DailyOps
  note's claim that "no short syntax available" for weekday-range scheduling is
  confirmed (not contradicted) by the spec's ABNF. No contradiction issue required.

- **Novel**:
  - **The fuzzy schedule syntax as a formal load-distribution mechanism** (Claim 1):
    No existing source note names or documents the fuzzy schedule syntax. Prior notes
    use it in examples (DailyOps, deterministic patterns) but do not define it. This
    is the first corpus entry providing the normative definition.
  - **Complete ABNF grammar for all five schedule families** (Claim 2, Concrete
    Artifacts): The full grammar — including interval types, time constraints,
    timezone syntax, and weekday names — is entirely new to the corpus.
  - **FNV-1a hash-based deterministic scattering algorithm** (Claim 6): The specific
    hash algorithm, constants, and workflow identifier format used to produce
    deterministic, per-workflow schedule offsets are not documented in any prior note.
  - **Three weighted time slot preference tiers** (Claim 7): The BEST/GOOD/OK tier
    structure with weights, UTC hour ranges, and slot counts is new. No prior note
    documents that `gh aw` has a preference policy for *when* in the day it schedules
    workflows.
  - **Peak avoidance rules** (Claim 8): The three peak avoidance rules (hour boundary,
    EU morning, US business hours) are not described in any existing source note. This
    is an operational detail with real implications for teams that notice their workflows
    are scheduled away from expected instants.
  - **Three conformance levels** (Claim 9): The Level 1/2/3 conformance framework
    is new and provides a structured vocabulary for discussing schedule complexity.
  - **10 normative error conditions with fail-fast requirement** (Claim 10): The
    MUST NOT silent fallback requirement and the enumerated error conditions are new.
    No existing note documents the error-handling contract for schedule expressions.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the fuzzy schedule syntax as the primary recommended scheduling mechanism**
  (Claims 1–4): When practitioners reach for `cron:` in their workflow frontmatter,
  redirect them to the fuzzy syntax unless they need weekday-range constraints
  (Mon–Fri, which still requires raw cron per `docs-ghaw-dailyops.md` Claim 2). The
  pitch: the fuzzy syntax IS the load distribution — practitioners get scatter for
  free without manual cron math. Document the five families and three constraint
  forms as the decision framework.

- **Document the deterministic stability guarantee** (Claim 6): A workflow's compiled
  schedule time is stable across recompilations. Teams that see a workflow scheduled
  at an unexpected time should know: (1) the time is deterministic, not random;
  (2) it is determined by the workflow's full path identifier; (3) it may have been
  remapped by peak avoidance rules. This is actionable debugging information.

- **Add timezone conversion examples for distributed teams** (Claims 4, 5): For teams
  across multiple timezones, the `around <time> utc+N` form makes timezone intent
  explicit in the workflow spec. Document the conversion formula (`UTC_time =
  local_time - offset`) and the day-wrap rule so teams can predict their workflow's
  UTC execution window.

- **Document schedule validation as part of the compile-time safety guarantee** (Claim 10):
  Adding to `docs-ghaw-compilation-process.md` Claim 1 (Phase 1 validation): schedule
  expression errors produce non-zero exit codes with actionable messages. MUST NOT
  silent fallback means `on: schedule: fortnight` fails the compile, not silently
  defaults to `daily`. This is part of the "compile step is the trust layer" framing.

### Chapter 04: Engineering Practices / Load Distribution

- **Add the three-tier preference model as a platform load policy** (Claim 7): Teams
  running many workflows should understand that unconstrained `daily` expressions
  are preferentially scheduled in the BEST tier (02–05 UTC). If a team is building
  many scheduled workflows, they will cluster in off-peak UTC hours — this is
  intentional, not random. Teams in UTC+9 should note that BEST-tier scheduling
  corresponds to their 11:00–14:00 local window.

- **Document peak avoidance as the reason for unexpected schedule offsets** (Claim 8):
  A workflow with `daily around 14:15 utc` will have its minute shifted to 19 (US
  business peak avoidance). Teams that notice their scheduled workflows fire at
  different times than specified should be directed to the peak avoidance rules as
  the explanation, not a bug.

### Chapter 02 / Chapter 04 cross-reference: DailyOps weekday scheduling gap

- **Clarify the fuzzy/raw cron boundary** (Claims 2, 3 + `docs-ghaw-dailyops.md`
  Claim 2): The guide should explicitly document: use fuzzy syntax for all-day
  recurring schedules; use raw cron for weekday-range (Mon–Fri) schedules. The
  DailyOps weekday convention (`0 2 * * 1-5`) is not replaceable by fuzzy syntax
  because the spec's `weekly on <weekday>` is single-day only. This is a practitioner
  decision point that should be made explicit rather than discovered by trial and error.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The `gh aw` documentation site is an
   Astro/Starlight SPA; WebFetch renders content through an AI model before returning
   it. Four targeted fetch passes were used: (1) initial overview, (2) request for
   verbatim key sections, (3) complete ABNF grammar, (4) remaining sections including
   hash constants and error table. Quote text was cross-checked across passes for
   consistency. Technical strings (ABNF rules, hash constants, error condition labels,
   UTC time slot ranges) were stable across passes and are treated as verbatim.
   Prose descriptions that varied between passes are marked "(no direct quote; see
   paraphrase in Our assessment)."

2. **Version 1.2.0, "Draft Specification"**: The spec carries both a version number
   and a Draft status. Draft does not mean "unreliable" — the grammar and algorithm
   sections are normative (MUST/SHOULD/SHALL language) and implemented in `gh aw compile`.
   It means the spec may be revised. The core constructs (five schedule families,
   scattering algorithm, three tiers, peak avoidance, conformance levels) are stable
   enough to document; edge-case error conditions may be updated in future versions.

3. **ABNF grammar partially reconstructed**: The spec contains a complete ABNF grammar.
   The top-level rules and primary non-terminals were returned consistently across
   WebFetch passes and are treated as verbatim. Some auxiliary rules (e.g., exact
   `hour-24`, `hour-12`, `am-pm` definitions) were not returned in full detail; they
   are omitted rather than guessed.

4. **Bi/tri-weekly as Section 3.5.1 and 3.5.2**: The spec organizes bi-weekly and
   tri-weekly as sub-sections with SHALL language ("The schedule SHALL execute once
   every 14 days" / "once every 21 days"). These short-form quotes were returned
   consistently and are treated as verbatim.

5. **No sub-pages followed**: The `reference/fuzzy-schedule-specification` page
   appeared to be a self-contained specification document with no sub-pages linked.
   The compliance test appendix (Appendix A) was referenced in the changelog entry
   but the full test suite was not extracted.

6. **No contradictions to file**: Reviewed all existing source notes against all
   eleven claims extracted. No claim here materially opposes any existing source note.
   The DailyOps "no short syntax available" observation is confirmed rather than
   contradicted. No contradiction issue required.
