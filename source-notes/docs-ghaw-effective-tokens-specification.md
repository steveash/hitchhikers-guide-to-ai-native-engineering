---
source_url: https://github.github.com/gh-aw/reference/effective-tokens-specification
source_type: docs
title: "GitHub Agentic Workflows: Effective Tokens Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: 2026-04-02
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#451"
---

# GitHub Agentic Workflows: Effective Tokens Specification

> The formal normative specification for the Effective Tokens (ET) metric —
> defines the token-class weighting formula, model-specific Copilot Multiplier,
> multi-invocation execution graph aggregation, three conformance levels, overflow
> safeguards, and an embedded versioned multiplier registry; the first corpus source
> to give practitioners the normative specification underlying the `effective_tokens`
> field already visible in `gh aw logs --json` output.

## Source Context

- **Type**: docs (formal normative specification — Version 0.2.0, Draft, published
  2026-04-02. Uses W3C-style format with RFC 2119 requirement terminology (MUST, MUST NOT,
  SHALL, SHOULD, MAY). The page content includes material labeled for v0.3.0 in its own
  changelog — see Extraction Notes. This is the most formal specification document
  in the gh-aw reference section, alongside `docs-ghaw-safe-outputs-specification.md`.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team behind Peli de Halleux's "Agent Factory" blog
  series and the `gh aw` CLI). Normative requirements, formula definitions, and registry
  specifications are authoritative for the `gh aw` platform. The formal specification
  language makes this the highest-confidence source type for its claims: requirements
  phrased with MUST are platform mandates, not practitioner recommendations.
- **Scope**: The complete normative definition of Effective Tokens (ET) — token class
  definitions and default weights, per-invocation computation formula, multi-invocation
  aggregation across execution graphs, the Copilot Multiplier model, three conformance
  levels, implementation requirements (completeness, determinism, versioning, partial
  visibility, overflow safeguards), the `model_multipliers.json` registry specification,
  a compliance test suite (T-ET-001 through T-ET-031), and security considerations.
  Does NOT cover: how to query ET from `gh aw logs` (see `docs-ghaw-agentic-ops.md`),
  cost optimization patterns for reducing ET (see `blog-bswen-mcp-token-cost.md`),
  or concrete dollar conversion from ET values (ET explicitly carries no dependency
  on billing or pricing systems by design).

## Extracted Claims

### Claim 1: The core problem ET solves is that raw token counts are not directly comparable — different token classes carry different computational costs and different models have different relative costs

- **Evidence**: The specification's §1.1 (Purpose) opens with this problem statement
  as the foundational motivation. The design goal list further specifies that ET
  carries no dependency on billing or pricing systems — it is a computational intensity
  metric, not a cost metric.
- **Confidence**: settled (first-party formal specification; this is the normative
  motivation for the entire metric)
- **Quote**: "Token counts reported by LLM APIs are not directly comparable: different
  token classes (input, cached, output, reasoning) carry different computational costs,
  and different models have different relative costs."
- **Our assessment**: The framing is precise and important. ET is NOT a billing metric
  (it carries no billing dependency by explicit design goal). It is a normalized measure
  of computational intensity, allowing apples-to-apples comparison of: (a) runs using
  different token class mixes (e.g., a cache-heavy run vs. an output-heavy run); (b) runs
  using different models (e.g., a Copilot-powered run vs. a GPT-based run). For Ch02
  (Foundations): ET is the answer to "how do you measure what a multi-invocation agentic
  run actually cost in compute terms?" — distinct from what it cost in dollars.

### Claim 2: ET defines six explicit design goals, including one that explicitly excludes billing dependency

- **Evidence**: §1.3 (Design Goals) lists six requirements for a conforming ET
  implementation. Goals 5 and 6 are particularly significant: reproducibility from
  identical inputs, and independence from billing/pricing systems.
- **Confidence**: settled (first-party formal specification; design goals are normative)
- **Quote**: "An ET implementation: 1. Preserves raw token counts per invocation
  2. Normalizes across token classes using disclosed weights 3. Normalizes across models
  using per-model multipliers 4. Supports aggregation across any number of invocations
  5. Produces a single reproducible metric from identical inputs 6. Carries no dependency
  on billing or pricing systems"
- **Our assessment**: Goal 6 (no billing dependency) is the most architecturally
  important. ET is designed to be a stable computational metric that teams can use in
  dashboards and comparisons without the metric shifting every time provider pricing
  changes. This separation of concerns (compute intensity ≠ cost) is the right
  engineering design for observability tooling. For Ch04 (Patterns): ET-based
  dashboards remain valid after price changes; dollar-cost dashboards require recalibration
  after every pricing update.

### Claim 3: Four token classes with dramatically different default weights — output and reasoning tokens are 4× more expensive than input, cached input is 0.1×

- **Evidence**: §4.2 (Token Class Weights) provides the normative weight table.
  Implementations MAY override these weights but MUST disclose the weights used
  in any reported output.
- **Confidence**: settled (first-party formal specification; the default weights are
  the normative baseline)
- **Quote** (table from §4.2):

  | Token Class  | Symbol  | Default Weight |
  |--------------|---------|----------------|
  | Input        | w_in    | 1.0            |
  | Cached Input | w_cache | 0.1            |
  | Output       | w_out   | 4.0            |
  | Reasoning    | w_reason| 4.0            |

  "Implementations MAY override these values but MUST disclose the weights used
  in any reported output."
- **Our assessment**: The 4× weight for output tokens formalizes the widely-cited
  practitioner observation that output tokens are significantly more expensive than
  input tokens. The 0.1× weight for cached input formalizes the Anthropic-published
  cache-read pricing (see `blog-bswen-mcp-token-cost.md` Claim 8 and
  `failure-cursor-ultra-billing-cache-explosion.md`). The equal weighting of reasoning
  tokens and output tokens (both 4.0) is notable — this positions reasoning tokens
  as computationally equivalent to generation tokens, not as "free" internal steps.
  For Ch02 (Foundations): a run that generates 1,000 output tokens consumes 40× more
  ET than a run that reads 1,000 cached tokens — this explains why cache utilization
  is so impactful on effective cost.

### Claim 4: The core ET formula applies a model-specific Copilot Multiplier on top of class-weighted token totals

- **Evidence**: §4.3 and §4.4 define the computation in two steps:
  (1) base_weighted_tokens applies the class weights; (2) effective_tokens applies
  the model multiplier. §5.1 extends this to multi-invocation aggregation.
  Appendix B provides the canonical collapsed formula.
- **Confidence**: settled (first-party formal specification; the formulas are normative)
- **Quote** (§4.3): "Per invocation: `base_weighted_tokens = (w_in × I) + (w_cache × C) + (w_out × O) + (w_reason × R)`"
- **Quote** (§4.4): "`effective_tokens = m × base_weighted_tokens`"
- **Quote** (§5.1): "For a request involving N invocations: `ET_total = Σ (m_i × base_weighted_tokens_i)`. Each invocation MAY use a different model and multiplier."
- **Quote** (Appendix B): "`ET_total = Σ [ m_i × (w_in × I_i + w_cache × C_i + w_out × O_i + w_reason × R_i) ]`. With default weights: `ET_total = Σ [ m_i × (I_i + 0.1 C_i + 4 O_i + 4 R_i) ]`"
- **Our assessment**: The two-step design (class weighting → model multiplier) is
  clean. The first step normalizes across token classes within a model; the second
  normalizes across models. The additive aggregation over N invocations (ET_total = Σ)
  enables direct comparison of runs with different numbers of sub-agent invocations.
  For Ch04 (Multi-Agent Orchestration): ET_total is the cost unit for comparing
  different orchestration strategies — a fan-out with 5 workers each making 3 LLM calls
  produces an ET_total that is directly comparable to a single-agent run with 15 LLM calls.

### Claim 5: The Copilot Multiplier is a per-model scalar sourced from an embedded versioned registry — unrecognized models default to 1.0 with a warning

- **Evidence**: §3.2 defines the Copilot Multiplier conceptually. The Registry
  section specifies the normative registry source file and nine registry requirements
  (R-REG-001 through R-REG-009).
- **Confidence**: settled (first-party formal specification; the registry definition
  and default behavior are normative)
- **Quote** (§3.2): "The **Copilot Multiplier** (`m`) is a scalar representing the
  relative computational intensity of a model versus a defined baseline. Its value
  is model-specific and MUST be disclosed by the implementation."
- **Quote** (Registry section): "The authoritative registry for `copilot_multiplier`
  values in this implementation is the file: `pkg/cli/data/model_multipliers.json`.
  This file is embedded at compile time into the `gh-aw` binary using a Go
  `//go:embed` directive in `pkg/cli/effective_tokens.go`."
- **Our assessment**: The compile-time embedding via `//go:embed` means the multiplier
  values are pinned to the binary version — a run's ET is reproducible from the binary
  version alone, without consulting a live registry. The R-REG-005 default (1.0 for
  unrecognized models) is safety-conscious: unknown models are not silently excluded
  from ET aggregation; they contribute at base rate with a warning. For Ch02: when a
  new model is added to the gh-aw ecosystem before its registry entry exists, its
  ET contribution will be understated (multiplied by 1.0 rather than its true
  multiplier) — teams should check for registry update lag when introducing new models.

### Claim 6: R-REG-009 requires deprecated models to remain in the registry with a deprecation marker for at least one minor version before removal

- **Evidence**: R-REG-009 in the Registry Requirements section specifies the
  deprecation lifecycle for multiplier entries.
- **Confidence**: settled (first-party formal specification; R-REG-009 is a normative
  requirement)
- **Quote**: "When a model is scheduled for removal from the registry, it MUST remain
  in `pkg/cli/data/model_multipliers.json` with a `deprecated` marker in a comment or
  companion metadata field for at least one minor version before it is deleted."
- **Our assessment**: The one-version deprecation window is the minimum required for
  historical report integrity. Without it, ET reports from an older binary run using
  a now-deleted model would fail validation because the multiplier no longer exists.
  The `deprecated` marker (not deletion) preserves the entry for one version so that
  historical reconstruction remains possible. For Ch05 (Team Adoption): when teams
  track ET over time, model deprecations in the registry are a potential data quality
  event — a binary upgrade that removes a model entry could silently change historical
  ET calculations if reports are recomputed.

### Claim 7: The spec defines three conformance levels — Basic covers single-invocation, Standard adds multi-invocation graph, Complete adds reporting and extensibility

- **Evidence**: §2.3 (Compliance Levels) specifies three levels with section references
  for each level's required content.
- **Confidence**: settled (first-party formal specification; conformance levels are
  normative)
- **Quote**: "**Level 1 – Basic**: Single-invocation ET computation (Section 4)"
- **Quote**: "**Level 2 – Standard**: Multi-invocation aggregation and execution graph
  (Sections 5–6)"
- **Quote**: "**Level 3 – Complete**: Full reporting and extensibility support
  (Sections 7–9)"
- **Our assessment**: The three-level progression is well-designed for incremental
  adoption. A simple tool that instruments a single LLM call can conform at Level 1.
  A multi-agent orchestrator needs Level 2 to attribute costs across the invocation
  graph. An enterprise observability platform would implement Level 3 for structured
  reporting. For Ch04 (Patterns): when evaluating or building ET-compatible tooling,
  ask which conformance level it claims — Level 1 is insufficient for multi-agent
  systems where sub-agent costs are the dominant cost driver.

### Claim 8: Execution graphs represent all invocations as a directed parent-child structure — root has parent_id=null, all sub-agents reference a valid parent

- **Evidence**: §6 (Execution Graph Requirements) with §6.2 (Root Invocation) and
  §6.3 (Sub-Agent Invocations).
- **Confidence**: settled (first-party formal specification; graph structure is normative)
- **Quote** (§6.2): "The root invocation MUST have `parent_id = null`. It represents
  the user-facing request that initiates the execution graph."
- **Quote** (§6.3): "Each sub-agent invocation MUST reference a valid `parent_id`.
  Sub-agent invocations MAY recursively spawn further invocations."
- **Quote** (§5.3): "`total_invocations = N`. This count MUST include the root call,
  all sub-agent calls, and all tool-triggered LLM calls."
- **Our assessment**: The directed graph model with parent_id attribution makes ET
  attributable — not just "what was the total?" but "which sub-agent incurred what
  share?" The MUST requirement on `total_invocations` including tool-triggered calls
  is significant: if a sub-agent calls a tool that internally makes an LLM call (e.g.,
  a summarization tool), that nested call must be counted. Invisibility to the
  orchestrator is not an excuse for omission (see Claim 9, §8.1 Completeness). For
  Ch04: the execution graph structure is the data model that enables the
  Portfolio-Analyst-style pattern in `blog-ghaw-agent-observability.md` Claim 4
  ("some agents were way too chatty") — you can only diagnose over-calling by
  attributing calls to their originating sub-agent in the graph.

### Claim 9: §8.1 Completeness requires all LLM calls to be counted including hidden or system-triggered calls — partial visibility must be flagged, not silently dropped

- **Evidence**: §8.1 (Completeness) and §8.4 (Partial Visibility) are normative
  implementation requirements.
- **Confidence**: settled (first-party formal specification; MUST requirements are
  normative)
- **Quote** (§8.1): "All LLM calls MUST be included in the execution graph. Hidden
  or system-triggered calls MUST be counted."
- **Quote** (§8.4): "When sub-agents are not fully observable, implementations MUST
  still report aggregate totals. Invocation nodes with incomplete data SHOULD be
  flagged to indicate missing information."
- **Our assessment**: The completeness requirement is the hardest to satisfy in
  practice. In a deeply nested multi-agent system, the orchestrator may not have
  visibility into all LLM calls made by sub-agents (especially if sub-agents run in
  separate processes or on different platforms). The §8.4 guidance (report aggregates,
  flag incomplete nodes) is the pragmatic fallback: incomplete ET is better than no
  ET, but incompleteness must be disclosed. For Ch04: this requirement implies that
  ET-compliant instrumentation must be end-to-end, not just instrumented at the
  orchestrator level. An orchestrator that instruments itself but not its workers
  produces a Level 1 report masquerading as Level 2.

### Claim 10: Four safeguard requirements protect against overflow — including a hard ceiling of 2^53 - 1 for JavaScript-safe integer interoperability and mandatory overflow warnings

- **Evidence**: §8.5 (Safeguards) contains four normative requirements (R-SAFE-001
  through R-SAFE-004).
- **Confidence**: settled (first-party formal specification; R-SAFE requirements are
  normative)
- **Quote** (R-SAFE-002): "Implementations **MUST** enforce a maximum ET ceiling of
  `9007199254740991` (`2^53 - 1`) for serialized numeric fields to preserve
  JavaScript-safe integer interoperability in cross-language pipelines."
- **Quote** (R-SAFE-003): "When computed ET exceeds the ceiling, implementations
  **MUST** clamp the reported `summary.effective_tokens` value to the ceiling and
  **MUST** emit a warning indicating that capping occurred."
- **Quote** (R-SAFE-004): "For long multi-agent chains, implementations **SHOULD**
  aggregate ET in a streaming manner (incremental updates per invocation) and
  **SHOULD** emit an early warning when running totals exceed 80% of the ceiling."
- **Our assessment**: The 2^53 - 1 ceiling is a JavaScript Number limit — this design
  choice reflects the cross-language pipeline reality (gh-aw reports likely pass
  through Node.js tooling, GitHub Actions JSON, and browser-based dashboards). The
  80% early-warning threshold (§R-SAFE-004) is operationally valuable: a long-running
  multi-agent chain that will eventually overflow should raise a warning before it
  hits the ceiling, giving operators time to investigate rather than discovering the
  clamped value in post-processing. In practice, reaching 2^53 ET would require
  an astronomically large run; the safeguard matters more as a correctness guarantee
  for edge cases than as a routine operational concern.

### Claim 11: Per-invocation token data should be treated as potentially sensitive and separated from aggregate ET values in access-controlled reporting systems

- **Evidence**: Appendix C (Security Considerations) is labeled as a security
  requirement section added in the v0.3.0 draft (per changelog).
- **Confidence**: emerging (the security consideration is framed with SHOULD, not
  MUST — it is a recommendation, not a mandate)
- **Quote**: "ET values are derived from token usage metadata. Implementations
  SHOULD treat per-invocation token data as potentially sensitive since usage patterns
  may reveal information about system prompts, model configurations, or user behavior.
  Aggregate ET values suitable for observability dashboards SHOULD be separated from
  detailed per-invocation data in access-controlled reporting systems."
- **Our assessment**: The sensitivity concern is real. Per-invocation token counts
  can reveal the relative complexity of different sub-agent calls — which can in turn
  reveal which parts of a workflow are computationally expensive, which may be
  sensitive competitive information. Aggregate ET (total for a workflow run) is
  typically safe to expose broadly; per-invocation ET breakdown is more sensitive.
  For Ch03 (Safety and Verification): when building ET dashboards, publish aggregate
  ET in team-wide visibility and restrict per-invocation data to workflow owners or
  audit roles. Corroborates the principle in `docs-ghaw-safe-outputs-specification.md`
  (privilege separation between observability layers).

## Concrete Artifacts

### Core ET Formula (from Appendix B)

```
ET_total = Σ [ m_i × (w_in × I_i + w_cache × C_i + w_out × O_i + w_reason × R_i) ]

With default weights:
ET_total = Σ [ m_i × (I_i + 0.1 C_i + 4 O_i + 4 R_i) ]

Per-invocation:
  base_weighted_tokens = (w_in × I) + (w_cache × C) + (w_out × O) + (w_reason × R)
  effective_tokens = m × base_weighted_tokens
```

### Default Token Class Weights (from §4.2)

```
Token Class  | Symbol   | Default Weight
-------------|----------|---------------
Input        | w_in     | 1.0
Cached Input | w_cache  | 0.1
Output       | w_out    | 4.0
Reasoning    | w_reason | 4.0
```

### Conformance Levels (from §2.3)

```
Level 1 – Basic:    Single-invocation ET computation (Section 4)
Level 2 – Standard: Multi-invocation aggregation and execution graph (Sections 5–6)
Level 3 – Complete: Full reporting and extensibility support (Sections 7–9)
```

### Worked Example — Three-Invocation Run (from Appendix A)

Scenario: root call, retrieval sub-agent, synthesis call — three different models.

```
root:       base = 1120, ET = 2240   (model multiplier m = 2.0)
retrieval:  base = 700,  ET = 700    (model multiplier m = 1.0)
synthesis:  base = 1210, ET = 2420   (model multiplier m = 2.0)
```

```json
{
  "summary": {
    "total_invocations": 3,
    "raw_total_tokens": 1800,
    "base_weighted_tokens": 3030,
    "effective_tokens": 5360
  }
}
```

### Registry Source Location (from Registry section)

```
File:       pkg/cli/data/model_multipliers.json
Embedding:  //go:embed directive in pkg/cli/effective_tokens.go
Versioning: registry version field ≠ gh-aw binary version
Default:    unrecognized model → multiplier treated as 1.0 (with warning)
Deprecation: deprecated models must remain for ≥ 1 minor version (R-REG-009)
```

### Compliance Test IDs (from §10)

```
Token Accounting:   T-ET-001 through T-ET-004
Aggregation:        T-ET-010 through T-ET-012
Execution Graph:    T-ET-020 through T-ET-022
Reporting:          T-ET-030 through T-ET-031
```

### Overflow Safeguards (from §8.5)

```
R-SAFE-001: Detect NaN, +Inf, -Inf before serializing
R-SAFE-002: Enforce ceiling 9007199254740991 (2^53 - 1) — JS-safe integer
R-SAFE-003: Clamp and warn when ceiling exceeded
R-SAFE-004: Aggregate incrementally; warn at 80% of ceiling for long chains
```

## Cross-References

- **Corroborates**:
  - `blog-bswen-mcp-token-cost.md` Claim 8 ("Cache read costs 0.1x compared to
    base input"): The ET spec's w_cache = 0.1 default weight formalizes the same
    0.1× cache-read pricing that Bswen observed empirically. The ET spec makes this
    normative rather than anecdotal.
  - `failure-cursor-ultra-billing-cache-explosion.md` (cache reads at 0.1× base
    input price): Same corroboration as Bswen — the ET spec's w_cache = 0.1 is
    consistent with the Anthropic-published cache pricing that both notes reference.
  - `docs-ghaw-agentic-ops.md` Concrete Artifacts → "Audit Workflow Run Data Schema"
    section: The `effective_tokens int` field described there as "Cost-normalized
    tokens" is the observable output of the ET specification. The spec provides the
    normative definition; the agentic-ops note shows the field in the `gh aw logs
    --json` schema where practitioners will encounter it.

- **Extends**:
  - `blog-ghaw-agent-observability.md` Claim 4 ("some agents were way too chatty
    with their LLM calls"): The Portfolio Analyst pattern diagnosed this by comparing
    token consumption across agents. ET_total is the formal normalized metric that
    makes such cross-agent comparison meaningful — raw token counts are incomparable
    across models, but ET values are directly comparable. The specification provides
    the formal basis for what the Portfolio Analyst is computing.
  - `docs-ghaw-orchestration-patterns.md` Claim 1 (orchestrator/worker fan-out
    model) and Claim 2 (`dispatch-workflow` for async worker runs): ET_total's
    multi-invocation aggregation (ET_total = Σ per-invocation ET) is the cost model
    for evaluating fan-out orchestration strategies. The specification's execution
    graph with parent-child attribution (root → sub-agents) maps directly to the
    orchestrator → worker structure in the orchestration patterns note.
  - `docs-ghaw-safe-outputs-specification.md`: The ET specification uses the same
    W3C-style normative format (RFC 2119, conformance levels, appendices) as the
    Safe Outputs specification — both are from the same team and the formal
    specification style is the same. Together they form the two main formal specs
    in the gh-aw reference section.

- **Contradicts**: None identified. The ET spec's w_cache = 0.1 is consistent with
  all existing corpus sources that reference cache pricing. No existing source note
  makes claims about ET normalization or Copilot Multiplier values that oppose this
  specification. No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Formal normative definition of Effective Tokens**: No prior corpus note
    defines ET formally. The agentic-ops note shows the field name; this spec
    provides the definition, formula, and requirements.
  - **Output and reasoning token weight (4.0×)**: No prior note explicitly states
    that output and reasoning tokens are weighted 4× input tokens in ET computation.
    Practitioners who see only raw token counts underestimate the impact of
    output-heavy runs vs. input-heavy runs.
  - **Model Copilot Multiplier mechanics**: The existence of per-model multipliers
    embedded from `pkg/cli/data/model_multipliers.json`, their compile-time embedding,
    and the 1.0 default for unrecognized models are entirely new to the corpus.
  - **Three conformance levels with section-level precision**: The Level 1/2/3
    progression for ET implementation is novel — practitioners can now assess tool
    compliance claims against the normative levels.
  - **Overflow safeguards with JavaScript-safe integer rationale**: The 2^53 - 1
    ceiling and its cross-language pipeline rationale are not documented anywhere
    else in the corpus.
  - **Security sensitivity of per-invocation ET data**: The recommendation to
    separate aggregate ET (broadly shareable) from per-invocation breakdown
    (access-controlled) is novel.

## Guide Impact

- **Chapter 02 (Foundations — LLM Cost Measurement)**: ET is the formal answer to
  "how do you measure what an agentic run cost computationally?" Add as the normative
  unit. Lead with Claim 1 (the problem: raw counts are incomparable), Claim 3 (the
  four token classes with their 1.0 / 0.1 / 4.0 / 4.0 weights), and Claim 4 (the
  formula). Use the worked example (Concrete Artifacts) to make the formula concrete.
  Pair with `blog-bswen-mcp-token-cost.md` Claim 8 — the ET spec formalizes what
  Bswen measured empirically.

- **Chapter 04 (Multi-Agent Patterns — Cost Attribution)**: ET_total with the
  execution graph (Claim 8) enables per-sub-agent cost attribution. Add as the
  recommended cost model for multi-invocation workflows. Cross-reference the
  `docs-ghaw-orchestration-patterns.md` fan-out model: ET_total is what practitioners
  should use to compare fan-out strategies. Currently Ch04 has no normalized cost
  metric — ET fills that gap.

- **Chapter 04 (Multi-Agent Patterns — Observability)**: Pair Claim 9 (completeness
  requirement: all LLM calls MUST be counted) with `blog-ghaw-agent-observability.md`
  Claim 4 (Portfolio Analyst finding chatty agents). The completeness requirement
  is what makes cross-agent cost comparison valid — an orchestrator that instruments
  itself but not its workers produces misleading ET figures.

- **Chapter 05 (Team Adoption — Cost Tracking)**: Claim 11 (security: aggregate ET
  shareable, per-invocation data access-controlled) is a concrete privacy recommendation
  for teams deploying ET-based dashboards. Add to the "what to make visible to whom"
  guidance.

- **Chapter 05 (Team Adoption — Tooling Versions)**: Claim 6 (R-REG-009 deprecation
  lifecycle) and Claim 5 (1.0 default for unrecognized models) are operational
  caveats for teams tracking ET over time. A gh-aw binary upgrade that changes
  multiplier values or removes deprecated entries will silently change ET values
  for future runs — teams should version-pin registry states when comparing
  historical ET trends.

## Extraction Notes

1. **Source access via WebFetch AI model**: The WebFetch tool processes page content
   through an AI model before returning results. Three fetch passes were made:
   - First pass: overview with tables and formulas (returned structured summary)
   - Second pass: section-by-section content with verbatim text for formulas,
     tables, and requirements (used for most quotes)
   - Third pass: confirmation of overview and formulas (consistent with second pass)
   Quotes in §4, §5, §8.5, Registry, Appendix B, and Design Goals are verbatim from
   the second and third fetches, which returned specific text consistently across passes.
   Prose summaries for sections where the AI model paraphrased rather than quoted are
   marked "(no direct quote; see paraphrase in Our assessment)."

2. **Version ambiguity**: The page header shows "Version 0.2.0 | Status: Draft |
   Publication Date: 2026-04-02." However, the page's own changelog lists a
   "Version 0.3.0 (Draft)" entry that adds the Model Multiplier Registry section,
   R-REG-009, compliance test skeleton, and security audit findings — all of which
   are present in the current page content. The most likely interpretation: the page
   is a living draft that already includes v0.3.0 content but the header version
   has not been formally bumped. The publication date (2026-04-02) is treated as
   the date of the base v0.2.0 publication. Content attributed to v0.3.0 per the
   changelog (Registry section, Appendix C, T-ET test IDs) is noted as such.

3. **No contradictions filed**: All existing corpus notes are consistent with the
   ET specification's claims. The 0.1× cache weight corroborates multiple prior
   notes rather than contradicting them. No contradiction issue required.

4. **Worked example computation note**: The worked example in Appendix A shows
   `root: ET = 2240` for `base = 1120`. This implies the root model's Copilot
   Multiplier is 2.0. Similarly `synthesis: ET = 2420` for `base = 1210` is also
   m=2.0. The `retrieval` sub-agent has ET=700 = base=700, implying m=1.0 (the
   reference model). The JSON summary shows `effective_tokens: 5360` = 2240 + 700
   + 2420 = 5360 ✓. The math is internally consistent. We have not reverse-engineered
   model identities from these multipliers.
