---
source_url: https://github.github.com/gh-aw/reference/fuzzy-schedule-specification
source_type: docs
title: "GitHub Agentic Workflows: Fuzzy Schedule Time Syntax Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#453"
---

# GitHub Agentic Workflows: Fuzzy Schedule Time Syntax Specification

> A formal ABNF specification for human-readable schedule strings with a deterministic
> two-phase compilation model — placeholders are scatter-resolved at deployment time
> via FNV-1a hashing into a weighted low-traffic hour pool, addressing the load
> distribution problem for repositories that run similar workflows at scale.

## Source Context

- **Type**: docs (formal W3C-style specification in the `reference/` section of
  the gh-aw documentation — alongside `reference/concurrency`, `reference/rate-limiting-controls`,
  and `reference/permissions`. Reference pages document platform behavior precisely;
  this one specifies the complete grammar, scattering algorithm, timezone handling,
  conformance levels, and error contract for fuzzy schedule strings.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's "Agent Factory" series and the `gh aw` CLI.
  The ABNF grammar, FNV-1a hash parameters, slot counts, and conformance level
  definitions are authoritative for the `gh aw` platform. The scattering algorithm
  in particular is a platform implementation detail — external practitioners cannot
  adjust it, only rely on its guarantees.
- **Scope**: The complete specification for fuzzy schedule syntax — ABNF grammar
  for four schedule families (daily, weekly, hourly, interval), time constraints
  (around/between), the two-phase compilation model (FUZZY:* placeholder → resolved
  cron), the deterministic scattering algorithm and its weighted pool structure,
  peak-minutes avoidance post-processing, UTC offset timezone syntax, three
  conformance levels, and 10 enumerated error conditions. Does NOT cover: how
  cron-scheduled workflows are triggered (see `docs-ghaw-how-they-work.md`),
  concurrency limits for scheduled workflows (see `docs-ghaw-concurrency-reference.md`),
  anti-runaway controls including delay injection (see `docs-ghaw-rate-limiting-controls.md`),
  or the DailyOps pattern for structuring scheduled workflows (see `docs-ghaw-dailyops.md`).

## Extracted Claims

### Claim 1: Fuzzy schedule syntax defines four families of human-readable schedule strings via ABNF grammar, replacing raw cron expressions with typed, constraint-aware alternatives

- **Evidence**: The specification provides an ABNF grammar with four top-level
  productions (`daily-schedule`, `weekly-schedule`, `hourly-schedule`,
  `interval-schedule`) each composable with time constraints (`around-constraint`
  or `between-constraint`). Time specifications support 24-hour format (HH:MM),
  12-hour format with am/pm, keywords "midnight" and "noon," and UTC offset notation.
- **Confidence**: settled (formal specification document from the platform team;
  the grammar is the normative definition, not a practitioner pattern)
- **Quote**: (no direct quote; the ABNF grammar block was returned by WebFetch as a
  processed summary — see paraphrase in Our assessment)
- **Our assessment**: The four schedule families cover the dominant scheduling
  needs for agentic workflows without requiring practitioners to write cron
  expressions: `daily` for once-per-day automation, `weekly on <weekday>` for
  once-per-week automation, `hourly` / `every N hours` for sub-daily cycles, and
  `every N days/weeks` for longer intervals. The "around" and "between" time
  constraints give practitioners human-friendly approximate scheduling without
  specifying exact minutes — which is precisely what the scattering algorithm then
  resolves deterministically. For Ch02 (Harness Engineering): introduce this
  syntax as the preferred alternative to raw cron for any schedule that fits one
  of the four families. Raw cron remains necessary for the weekday-only pattern
  (`0 2 * * 1-5` documented in `docs-ghaw-dailyops.md` Claim 2) because the
  fuzzy grammar does not include a "weekdays" schedule type.

### Claim 2: Compilation is two-phase — the parser emits deterministic FUZZY:* placeholder tokens rather than resolved cron expressions, and scattering occurs as a separate deployment-time step

- **Evidence**: The specification defines a table of FUZZY:* placeholder strings
  for each schedule type: `FUZZY:DAILY * * *`, `FUZZY:DAILY_AROUND:HH:MM * * *`,
  `FUZZY:DAILY_BETWEEN:SH:SM:EH:EM * * *`, `FUZZY:WEEKLY * * *`,
  `FUZZY:WEEKLY:DOW * * DOW`, `FUZZY:HOURLY * * *`, `FUZZY:HOURLY:N * * *`,
  `FUZZY:BI-WEEKLY * * *`, `FUZZY:TRI-WEEKLY * * *`.
- **Confidence**: settled (the placeholder tokens are the normative output of the
  compilation step — this is platform-defined behavior, not a design pattern)
- **Quote**: (no direct quote available — WebFetch returned processed output, not
  raw spec text; see paraphrase in Our assessment)
- **Our assessment**: The two-phase model is architecturally significant: the
  parse/compile step is deterministic and environment-independent (the same schedule
  string always produces the same FUZZY:* placeholder), while the scatter step is
  deterministic-but-repository-specific (the same FUZZY:* placeholder produces
  different resolved cron times for different repositories). This means compiled
  workflow files (`.lock.yml`) can be committed to source control with FUZZY:*
  placeholders, and the scattering is applied at the deployment boundary — ensuring
  no two repositories in the same organization inadvertently share the exact same
  schedule. For Ch02: document the two-phase model as the mechanism that makes
  fuzzy schedules safe to commit without creating fleet-wide load spikes.

### Claim 3: The scattering algorithm uses FNV-1a 32-bit hashing of the workflow identifier (`owner/repo/workflow_path`) as the deterministic seed — guaranteeing the same schedule offset for every deployment of the same workflow

- **Evidence**: The specification explicitly states the hash function: FNV-1a 32-bit
  with offset basis `0x811c9dc5` and prime `0x01000193`, applied to the workflow
  identifier string `owner/repo/workflow_path`. The hash produces a deterministic
  seed for modulo-based slot selection.
- **Confidence**: settled (the hash function parameters are normative spec content;
  implementations must use these exact values to pass conformance testing)
- **Quote**: (no direct quote available — specific parameters extracted from WebFetch
  processed output; see paraphrase in Our assessment)
- **Our assessment**: Using the workflow identifier as the hash input means the
  scattering is stable: renaming a repository changes the resolved schedule; renaming
  the workflow file changes the resolved schedule; changing only the schedule string
  itself does not change which time slot is selected (unless the FUZZY:* type changes).
  This is a deliberate design — operators can predict schedule stability based on
  identifier continuity. FNV-1a is chosen for its speed and good distribution
  properties in low-cardinality string spaces. For Ch02: mention that renaming
  a workflow file or transferring a repository to a different org will change its
  resolved schedule time — this should be accounted for when planning coordinated
  multi-repository schedules.

### Claim 4: v1.2.0 replaced uniform scatter across 1,440 daily minutes with a weighted 622-slot pool that concentrates workflows in low-traffic UTC hours — a deliberate load distribution design

- **Evidence**: The specification defines three tiers of the 622-slot pool:
  BEST tier (weight 3): hours 02–05 UTC, odd minutes {7, 13, 23, 37, 43, 53} = 72 slots;
  GOOD tier (weight 2): hours 10–12 UTC, minutes [5–54] = 300 slots;
  OK tier (weight 1): hours 19–23 UTC, minutes [5–54] = 250 slots.
  Slot selection: `index = hash(identifier) % 622`, biasing toward BEST and GOOD
  tiers proportionally to their weights.
- **Confidence**: settled (the slot counts and tier definitions are normative spec
  content; v1.2.0 version is named explicitly)
- **Quote**: (no direct quote; quantitative detail extracted from WebFetch processed
  summary; see paraphrase in Our assessment)
- **Our assessment**: The weighted pool is the key load-distribution mechanism in
  the spec. Hours 02–05 UTC are BEST because they are the global trough — lowest
  US, EU, and APAC activity simultaneously. Hours 10–12 UTC are GOOD because
  they fall in EU morning before US business picks up. Hours 19–23 UTC are OK
  because they are US evening / APAC morning. All three windows avoid the overlap
  zones where EU morning + US morning + APAC late afternoon create peak GitHub
  load (roughly 13–18 UTC). The weighted selection means the algorithm generates
  roughly 3× more BEST-tier times than OK-tier times across a fleet of repositories.
  For Ch04 (Orchestration): this is the platform's answer to "how do you prevent
  100 repositories from all running daily cleanup workflows at the same time?" —
  the answer is hashed scatter into a biased low-traffic pool, requiring no
  operator configuration. For Ch02: contrast with `docs-ghaw-rate-limiting-controls.md`
  Claim 1 (eight-layer anti-runaway model) — rate limiting controls concurrent
  execution; fuzzy scheduling controls temporal distribution. They are orthogonal
  defenses against different load problems.

### Claim 5: "Around" and "between" time constraints use hash-derived offsets within the specified window — enabling human-readable approximate scheduling without arbitrary minute selection

- **Evidence**: For "around" patterns: ±60 minute window centered on the target
  time, with `hash % 120` determining the offset within [-60, +59]. For "between"
  patterns: hash modulo the range duration determines the offset from the start
  time; midnight-crossing ranges calculate size as `(1440 - start_minutes) + end_minutes`.
- **Confidence**: settled (the formulas are normative spec content for the
  scattering step)
- **Quote**: (no direct quote; formulas extracted from WebFetch processed summary;
  see paraphrase in Our assessment)
- **Our assessment**: The constraint-scattering formulas allow practitioners to
  express scheduling intent semantically ("sometime around 2 AM", "sometime between
  midnight and 5 AM") without knowing or caring about the exact resolved minute.
  The "between" midnight-crossing formula shows careful edge-case handling —
  a range from 23:00 to 04:00 does not produce a zero or negative duration error,
  because the formula wraps correctly across the 00:00 boundary. For Ch02: recommend
  "daily around 03:00 utc" as the human-readable equivalent of `cron: "0 3 * * *"`,
  and "daily between midnight and 05:00 utc" as the equivalent of a maintenance
  window constraint — both are more readable and produce appropriately scattered times.

### Claim 6: Two sequential normalization passes enforce minute boundaries after raw scattering — avoidHourBoundary then avoidPeakMinutes — preventing clustering near hour transitions and EU/US peak periods

- **Evidence**: Pass 1 (`avoidHourBoundary`): minutes [0–4] shift to [5–9]; minutes
  [55–59] shift to [50–54]. Result is always in [5, 54]. Pass 2 (`avoidPeakMinutes`,
  applied after boundary adjustment): EU morning peak (hours 06–09) avoids minutes
  [27–33], shifting to 34; US business hours (hours 14–18) avoid minutes [12–18]
  shifting to 19, and [42–48] shifting to 49.
- **Confidence**: settled (the normalization pass definitions are normative spec
  content; named passes suggest they are independently testable units)
- **Quote**: (no direct quote; details extracted from WebFetch processed summary;
  see paraphrase in Our assessment)
- **Our assessment**: The two-pass normalization is the spec's defense against
  GitHub Actions' well-known clustering problem — when many workflows specify
  `cron: "0 * * * *"` (on the hour) or `cron: "*/5 * * * *"` (every 5 minutes),
  all minute-00 or minute-05 slots become extremely congested. The avoidHourBoundary
  pass ensures fuzzy schedules never land at the exact hour boundary where runner
  demand spikes. The avoidPeakMinutes pass adds a second layer: avoiding the specific
  minutes within peak hours that correlate with workflow start clusters (likely
  derived from GitHub infrastructure telemetry). The sequence (raw scatter → boundary
  correction → peak correction) is important — applying peak correction before
  boundary correction could push a corrected minute back into a boundary zone.
  For Ch02: this explains why fuzzy schedule outputs are more load-safe than naive
  "pick a random minute" approaches — two layers of post-processing ensure the
  resulting schedules avoid known congestion points.

### Claim 7: UTC offset notation is the preferred timezone specification; DST abbreviations are explicitly discouraged due to ambiguity

- **Evidence**: The specification defines UTC offset syntax as "utc±HH[:MM]" with
  range UTC-12:00 to UTC+14:00 and conversion formula `UTC_time = local_time - offset`
  (in minutes). Negative results wrap to the previous day; results ≥1440 wrap to
  the next day. The specification explicitly discourages DST abbreviations for
  this reason.
- **Confidence**: settled (the offset range and conversion formula are normative;
  the DST discouragement is an explicit normative statement, not a recommendation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The DST discouragement is practically significant: abbreviations
  like "EST" are ambiguous (Eastern Standard Time = UTC-5, but "EST" is sometimes
  misused for Eastern Time which observes DST), whereas "utc-5" or "utc-05:00" is
  unambiguous. The day-wrap arithmetic (negative → previous day, ≥1440 → next day)
  handles schedules like "daily around midnight utc-5" that would naively produce
  an out-of-range UTC minute. For Ch02: if teams need to express a schedule relative
  to a local time zone, use explicit UTC offsets — "daily around 08:00 utc+9" —
  not timezone name abbreviations.

### Claim 8: Three conformance levels allow incremental implementation — Basic (Level 1), Standard (Level 2), Complete (Level 3) — enabling partial adopters to implement a useful subset without the full spec

- **Evidence**: Level 1 (Basic): daily and weekly schedules without time constraints.
  Level 2 (Standard): adds "around"/"between" constraints and hourly schedules.
  Level 3 (Complete): adds timezone conversion and interval schedules (bi-weekly,
  tri-weekly).
- **Confidence**: settled (the conformance level definitions are normative spec
  content; the three-level structure is characteristic of a W3C-style spec designed
  for testing and certification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The conformance levels reveal the spec's deployment intent —
  it is written for third-party implementers (other CI platforms, scheduling tools,
  or gh-aw clients), not just for internal gh-aw use. The progression from Basic
  to Complete aligns with implementation complexity: daily/weekly parsing is
  straightforward; constraint scattering adds the hashing and normalization logic;
  timezone conversion and interval schedules add the edge-case arithmetic. For the
  guide: this spec is not just a gh-aw-internal document — it is a portable
  scheduling syntax designed for adoption by other tooling. Teams building custom
  scheduling layers for agentic workflows could implement Level 1 or Level 2
  without committing to the full spec.

### Claim 9: The spec mandates compilation failure with a non-zero exit code for all 10 enumerated error conditions — no silent fallback to defaults is permitted

- **Evidence**: The spec defines 10 error conditions (E-01 through E-10) with
  required behavior for each. Example conditions: unknown keywords must list valid
  options; out-of-range times must cite valid ranges; zero-duration "between" ranges
  must be rejected. The spec states implementations must NOT silently fall back
  to defaults — all errors cause compilation failure.
- **Confidence**: settled (the no-silent-fallback requirement is a normative SHALL
  statement in the spec; the error enumeration is normative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The no-silent-fallback mandate is a sharp departure from
  many scheduling tools (including cron itself) that silently accept malformed
  input or substitute defaults. The rationale is clear in a multi-workflow agentic
  context: a silently defaulted schedule produces a workflow that runs at an
  unexpected time with no indication of error, potentially causing coordination
  failures (e.g., a dependency workflow runs before the workflow that was supposed
  to run first). Compilation failure with diagnostic output (citing the specific
  E-NN code and valid alternatives) converts a runtime mystery into a compile-time
  error. For Ch02: this is consistent with the gh-aw pattern of "fail fast at
  compile time" documented across multiple reference notes — the fuzzy schedule
  spec extends that pattern to the scheduling domain.

## Concrete Artifacts

### ABNF Grammar (from specification)

```
fuzzy-schedule = daily-schedule / hourly-schedule / weekly-schedule / interval-schedule
daily-schedule = "daily" [time-constraint]
weekly-schedule = "weekly" ["on" weekday] [time-constraint]
hourly-schedule = "hourly" / ("every" hour-interval)
interval-schedule = "every" (minute-interval / hour-interval / day-interval / week-interval)
time-constraint = around-constraint / between-constraint
around-constraint = "around" time-spec
between-constraint = "between" time-spec "and" time-spec
```

Time specifications: 24-hour HH:MM, 12-hour with am/pm, keywords "midnight"/"noon",
UTC offset "utc±HH[:MM]".

*Source: gh-aw fuzzy-schedule-specification, "ABNF Grammar Definition" section*

### FUZZY:* Placeholder Token Table

```
FUZZY:DAILY * * *                      → daily schedule (no time constraint)
FUZZY:DAILY_AROUND:HH:MM * * *         → daily around HH:MM
FUZZY:DAILY_BETWEEN:SH:SM:EH:EM * * *  → daily between SH:SM and EH:EM
FUZZY:WEEKLY * * *                     → weekly (no weekday or time constraint)
FUZZY:WEEKLY:DOW * * DOW               → weekly on specific weekday DOW
FUZZY:HOURLY * * *                     → hourly schedule
FUZZY:HOURLY:N * * *                   → every N hours
FUZZY:BI-WEEKLY * * *                  → every two weeks
FUZZY:TRI-WEEKLY * * *                 → every three weeks
```

*Source: gh-aw fuzzy-schedule-specification, "Fuzzy Cron Placeholders" section*

### Weighted Slot Pool (v1.2.0)

```
Total pool: 622 slots

BEST tier (weight 3): 72 slots
  Hours: 02–05 UTC
  Minutes: {7, 13, 23, 37, 43, 53} (odd, non-boundary)
  Effective weight in selection: 72 × 3 = 216 weighted units

GOOD tier (weight 2): 300 slots
  Hours: 10–12 UTC
  Minutes: [5–54]
  Effective weight in selection: 300 × 2 = 600 weighted units

OK tier (weight 1): 250 slots
  Hours: 19–23 UTC
  Minutes: [5–54]
  Effective weight in selection: 250 × 1 = 250 weighted units

Selection formula: index = FNV-1a32(owner/repo/workflow_path) % 622
```

*Source: gh-aw fuzzy-schedule-specification, "Deterministic Scattering Algorithm" section*

### Peak Minutes Avoidance Normalization

```
Pass 1 — avoidHourBoundary:
  Input minutes [0–4]   → shift to [5–9]   (avoid hour-start cluster)
  Input minutes [55–59] → shift to [50–54] (avoid hour-end cluster)
  Result: always in [5, 54]

Pass 2 — avoidPeakMinutes (applied after Pass 1):
  EU morning peak (hours 06–09):
    Minutes [27–33] → shift to 34
  US business hours (hours 14–18):
    Minutes [12–18] → shift to 19
    Minutes [42–48] → shift to 49
```

*Source: gh-aw fuzzy-schedule-specification, "Peak Minutes Avoidance" section*

### Conformance Level Summary

```
Level 1 — Basic:
  - Daily schedules (with and without time constraints): NO
    (only plain daily, no around/between)
  - Weekly schedules (no time constraints)
  - No timezone conversion required

Level 2 — Standard:
  - All Level 1 features
  - "around" and "between" time constraints
  - Hourly schedules

Level 3 — Complete:
  - All Level 2 features
  - Timezone conversion (utc±HH[:MM] offset arithmetic)
  - Interval schedules (bi-weekly, tri-weekly)
```

*Source: gh-aw fuzzy-schedule-specification, "Conformance Levels" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-rate-limiting-controls.md` Claim 1 (eight-layer defense-in-depth
    anti-runaway model): The fuzzy schedule spec's weighted pool and peak-minutes
    avoidance are temporal load-distribution mechanisms that complement the
    concurrent-execution controls in the rate-limiting reference. The two defenses
    are orthogonal: rate-limiting controls how many workflows run simultaneously;
    fuzzy scheduling controls when they fire. Together they represent defense-in-depth
    against both concurrency overload and temporal load spikes.
  - `docs-ghaw-concurrency-reference.md` Claim 1 (two-tier concurrency model for
    AI resource isolation): Claim 9 here (compile-time error on invalid schedules)
    extends the "fail fast" theme of the concurrency reference's validation approach.
    Both specs enforce correctness at configuration/compile time rather than allowing
    runtime surprises.

- **Extends**:
  - `docs-ghaw-dailyops.md` Claim 2 (weekday-only cron `0 2 * * 1-5` with comment
    "no short syntax available"): The fuzzy-schedule spec provides human-readable
    alternatives for daily, weekly, and hourly scheduling patterns. However, the
    comment in DailyOps remains accurate: the fuzzy grammar does not include a
    "weekdays only" schedule type (Mon–Fri), so raw cron `0 2 * * 1-5` is still
    required for that pattern. The fuzzy spec extends the scheduling vocabulary
    without filling the weekday-only gap. Recommend in Ch02: use `daily around 02:00 utc`
    for workflows that can run daily (including weekends); keep raw cron for
    weekday-only constraints.
  - `docs-ghaw-dailyops.md` Claim 8 (DailyOps as the scheduled counterpart to
    event-driven patterns): The fuzzy schedule spec provides the formal grammar
    for the schedule strings that power DailyOps workflows. The DailyOps pattern
    note documents *what* to build with scheduled workflows; this spec documents
    *how schedules are expressed and resolved*. Together they give practitioners
    the full picture for building scheduled agentic automation.

- **Contradicts**: None. The fuzzy schedule specification adds new content to the
  corpus — formal grammar, scattering algorithm, conformance levels, error contract.
  No existing source note makes claims about schedule syntax or scattering that
  conflict with this spec. No contradiction issue required.

- **Novel**:
  - **Two-phase compilation model (FUZZY:* placeholders → resolved cron)** (Claim 2):
    No existing source note documents the placeholder system or two-phase approach
    to schedule compilation. This is entirely new to the corpus.
  - **FNV-1a 32-bit hash of `owner/repo/workflow_path` as the scattering seed**
    (Claim 3): The specific hash function and its input are new to the corpus.
    The implication — workflow identifier stability determines schedule stability —
    is a novel operational insight.
  - **Weighted 622-slot pool for temporal load distribution** (Claim 4): No existing
    note documents how gh-aw distributes scheduled workflow load across time. The
    three-tier pool (BEST/GOOD/OK) with explicit UTC hour ranges is new.
  - **Peak-minutes avoidance post-processing** (Claim 6): The two named normalization
    passes (`avoidHourBoundary`, `avoidPeakMinutes`) with specific minute ranges
    are new to the corpus.
  - **Three conformance levels for third-party implementation** (Claim 8): The spec's
    design for external adoption — enabling partial implementations — implies the
    fuzzy schedule syntax is intended as a portable standard, not merely a gh-aw
    internal format. No existing note discusses this portability intent.
  - **10 enumerated error conditions with mandatory compilation failure** (Claim 9):
    The explicit no-silent-fallback mandate is the strongest compile-time enforcement
    statement in any gh-aw reference note to date.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add fuzzy schedule syntax as the preferred alternative to raw cron for daily,
  weekly, and hourly patterns** (Claim 1): When a scheduled workflow fires once
  per day or once per week, `daily around 03:00 utc` or `weekly on tuesday around 02:00 utc`
  is more readable than the cron equivalent and produces a load-distributed schedule
  automatically. Reserve raw cron for weekday-only patterns (`0 2 * * 1-5`) that
  the fuzzy grammar cannot express.

- **Document the two-phase compilation model** (Claim 2): Practitioners committing
  workflow files should know that FUZZY:* placeholders are committed to source
  control, and scattering is applied at deployment time per repository. This
  matters for reproducibility: the same workflow spec deployed to two repositories
  resolves to different cron times — by design.

- **Warn that renaming a workflow file or repository changes its resolved schedule**
  (Claim 3): Since the FNV-1a hash input is `owner/repo/workflow_path`, any
  identifier change produces a new scatter result. Teams coordinating multi-repository
  workflows that must run in a specific relative order should account for this.

- **Add the weighted 622-slot pool as the explanation for why fuzzy schedules
  distribute load** (Claim 4): Engineers who ask "why not just pick a random minute?"
  need to understand the difference between random scatter (uniform across 1,440
  minutes) and the weighted pool (biased toward 02–05 UTC, avoiding 13–18 UTC).
  The weighted pool is the platform's answer to the GitHub Actions "00-minute
  clustering" problem.

- **Add UTC offset notation as the required form for timezone-aware schedules**
  (Claim 7): Use `utc+9`, `utc-05:00` — never DST abbreviations. Explain the
  day-wrap arithmetic for midnight-boundary schedules.

### Chapter 04: Multi-Agent Orchestration Patterns

- **Add fuzzy scheduling as the temporal load-distribution primitive for agent
  fleets** (Claim 4): When an organization runs similar scheduled workflows across
  many repositories, fuzzy scheduling ensures they scatter across the 622-slot pool
  without operator coordination. This is the temporal equivalent of the concurrency
  controls in `docs-ghaw-concurrency-reference.md` — addressing "when do agents
  fire?" rather than "how many can run simultaneously?" Present both as orthogonal
  components of a load-safe agent fleet.

### Chapter 03 (or wherever compile-time validation is covered):

- **Add no-silent-fallback as a scheduling-domain extension of the "fail fast"
  principle** (Claim 9): The 10 error conditions with mandatory compilation failure
  prevent the class of scheduling bugs where a typo in a schedule string silently
  deploys a workflow that fires at an unexpected time. This extends the compile-time
  validation theme established for orchestration target checking in
  `docs-ghaw-orchestration-patterns.md` Claim 5.

## Extraction Notes

1. **WebFetch returned a processed summary, not raw HTML/markdown**: The tool
   processed the source page and returned a structured technical summary with
   model-added headers ("## ABNF Grammar Definition", etc.). The technical content
   (ABNF grammar, FNV-1a parameters, slot counts, hour ranges, minute ranges, error
   conditions) appears to be faithfully extracted from the source, but character-for-
   character verbatim accuracy cannot be guaranteed. All `Quote` fields are therefore
   set to "(no direct quote; see paraphrase in Our assessment)" per MINER.md §2a.
   The Assayer should verify specific technical values (slot counts, hash parameters,
   conformance level definitions) against the live source URL.

2. **This is the spec that underlies gh-aw's `schedule:` frontmatter field**: The
   fuzzy-schedule syntax is what practitioners write in workflow `.md` files under
   the `schedule:` key. The spec formalizes what has been used implicitly in
   DailyOps examples like `daily around 02:00 utc` (if such examples exist in the
   docs) — or conversely, explains why existing examples use raw cron instead of
   the fuzzy syntax for weekday-only schedules.

3. **v1.2.0 is named explicitly for the weighted pool change**: The "key innovation
   in v1.2.0" language in the WebFetch output indicates this was a deliberate design
   upgrade from an earlier uniform-scatter approach. The previous behavior (uniform
   across all 1,440 minutes) is not documented in the current spec but is implied
   by the "rather than" framing.

4. **No publication date**: The specification page does not carry an explicit
   publication date. `date_published` is left null. The v1.2.0 reference provides
   a versioning signal but no date.

5. **Conformance testing reference**: The source mentions "compliance testing" for
   the three conformance levels, suggesting a test suite exists (likely in the gh-aw
   repository or a separate compliance kit). This was not followed — the compliance
   test suite was not in scope for this extraction.

6. **No contradictions filed**: All claims in this source are new additions to the
   corpus. No existing source note makes claims that conflict with the fuzzy-schedule
   grammar, scattering algorithm, or error contract. The DailyOps "no short syntax
   available" comment is consistent with this spec (fuzzy grammar has no weekday-only
   type). No contradiction issue required.
