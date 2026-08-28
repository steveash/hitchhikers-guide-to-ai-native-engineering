---
source_url: https://github.github.com/gh-aw/reference/open-telemetry-attributes
source_type: docs
title: "GitHub Agentic Workflows: OpenTelemetry Attribute Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: settled
issue: "#3003"
---

# GitHub Agentic Workflows: OpenTelemetry Attribute Reference

> The exhaustive attribute-name inventory for gh-aw's OpenTelemetry integration —
> enumerates the resource, span, GenAI, episode, outcome, and experiment attributes
> emitted on built-in spans, and (via the companion `reference/open-telemetry` guide)
> the workflow-frontmatter configuration for writing spans out to a backend and
> reading existing telemetry back in through an MCP server. This is the concrete
> attribute schema that practitioners need to write dashboards, alerts, and
> queries against gh-aw telemetry — a gap the existing observability notes in the
> corpus (architecture and config patterns) do not fill.

## Source Context

- **Type**: docs (GitHub Agentic Workflows `reference/open-telemetry-attributes`
  page — a pure attribute-inventory reference page in the `reference/` section,
  distinct from the `patterns/` section covered by `docs-ghaw-monitoring-patterns.md`
  and from the conceptual blog series covered by `blog-ghaw-agent-observability.md`.
  The page explicitly defers setup/usage instructions to a companion page,
  `reference/open-telemetry`, which this note also extracts as a substantive
  linked page per MINER.md §1.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and the `mcp-gateway` and
  `outcomes` reference specifications already in the corpus). Attribute names
  and their descriptions are authoritative for the `gh aw` platform; they are
  the literal OTel span keys emitted by the platform's own instrumentation code,
  not a third-party interpretation.
- **Scope**: Covers the complete attribute inventory across seven categories
  (resource, workflow/job span, agent/GenAI, workflow-call/episode, outcome
  summary, outcome per-item, experiment) plus a short note on trace-artifact
  mirroring (`otel.jsonl`). The companion `reference/open-telemetry` page adds
  the configuration surface: write-side OTLP export config, an MCP-based
  read-side telemetry-query mechanism, custom span/resource attributes, and a
  `otlp.cjs` helper API for emitting custom spans from shared imports. Does NOT
  cover: the OpenTelemetry configuration at the MCP Gateway layer (that is
  `docs-ghaw-mcp-gateway-reference.md`), the outcome *concept* definitions
  (state taxonomy, efficiency formula — that is `docs-ghaw-outcomes-reference.md`),
  or GitHub Projects-based monitoring (`docs-ghaw-monitoring-patterns.md`). Does
  not include sample trace/span JSON payloads or exporter-specific backend setup
  beyond the Sentry and Google WIF examples shown.

## Extracted Claims

### Claim 1: Resource attributes identify the workflow run, repository, runner, and gh-aw environment, and custom resource attributes must never carry secret values because they are exported to external backends

- **Evidence**: A 24-row attribute table lists resource-level identifiers
  (`service.name`, `gh-aw.workflow.name`, `gh-aw.repository`, `gh-aw.run.id`,
  `github.run_id`, `github.repository`, `runner.os`, `runner.arch`,
  `deployment.environment`, etc.) alongside an explicit warning about the
  `observability.otlp.resource-attributes` config field.
- **Confidence**: settled (first-party reference table; the secrets warning
  uses direct prescriptive language)
- **Quote**: "Do **not** use `secrets.*` or `vars.*` values for this field
  because resource attributes are exported to external observability backends
  and are not treated as secret values."
- **Our assessment**: This is a concrete, actionable security guardrail that
  is easy to violate by accident — a practitioner adding a custom resource
  attribute for, say, a team identifier or cost-center tag might reach for
  `${{ secrets.TEAM_ID }}` without realizing resource attributes are shipped
  to whatever OTLP backend is configured (Sentry, a Google Cloud collector,
  etc.) unencrypted and un-redacted. The `github.run_id` / `gh-aw.run.id` and
  `github.repository` / `gh-aw.repository` pairs also show a deliberate
  dual-namespace design: `gh-aw.*` attributes are the platform's own namespace,
  while `github.*` attributes exist purely for "compatibility" with dashboards
  built against standard GitHub Actions OTel conventions. For Ch02 (Harness
  Engineering): document the secrets-in-resource-attributes anti-pattern
  explicitly — it is a data-exfiltration-adjacent misconfiguration, not just a
  style nit.

### Claim 2: Workflow/job span attributes expose AI Credits budget tracking directly as span fields — consumed, budget, exceeded flag, and rate-limit-error flag are all separate attributes

- **Evidence**: The workflow/job span attribute table includes `gh-aw.aic`
  ("AI credits consumed for the run when available"), `gh-aw.max_ai_credits`
  ("Configured max AI credits budget for the run when available"),
  `gh-aw.max_ai_credits_exceeded` ("Whether the run exceeded the max AI
  credits budget"), and `gh-aw.ai_credits_rate_limit_error` ("Whether an
  AI-credits rate-limit or budget-exhaustion signal was detected").
- **Confidence**: settled (first-party attribute table; four distinct,
  named fields)
- **Quote**: `gh-aw.max_ai_credits_exceeded` — "Whether the run exceeded the
  max AI credits budget."
- **Our assessment**: This confirms that AI Credits (AIC) — which
  `blog-ghaw-ai-credits-migration.md` Claim 1 documents as having replaced
  Effective Tokens as the platform's primary spend metric — is fully wired
  into the OTel span schema, not just `gh aw logs`/`gh aw audit` CLI output.
  The separate `exceeded` boolean and `rate_limit_error` boolean are notable:
  they let a dashboard or alert distinguish "this run went over budget but
  finished" from "this run hit a hard rate-limit wall," which are different
  operational conditions requiring different responses (the first is a
  budget-tuning problem, the second may indicate the workflow needs backoff
  or scheduling changes). For Ch04/Ch07 (Cost and Observability): recommend
  alerting on `gh-aw.max_ai_credits_exceeded` and
  `gh-aw.ai_credits_rate_limit_error` as first-class signals, distinct from
  raw `gh-aw.aic` cost tracking.

### Claim 3: The "working-set rebuild factor" metric measures cumulative context reconstruction relative to peak invocation context, and the platform explicitly disclaims it as a predictor of task success or semantic coherence

- **Evidence**: Five related attributes —
  `gh-aw.working_set.measurement_state` (values: `measured`, `partial`,
  `unavailable`), `gh-aw.working_set.rebuild_factor` ("Cumulative canonical
  input tokens divided by peak invocation input tokens"),
  `gh-aw.working_set.cumulative_input_tokens`,
  `gh-aw.working_set.peak_input_tokens`, and
  `gh-aw.working_set.rebuild_excess_tokens` — plus an explicit closing
  disclaimer on the page.
- **Confidence**: settled (first-party attribute table plus an explicit
  scope-limiting disclaimer in the page's own prose, mirroring the pattern
  in `docs-ghaw-outcomes-reference.md` Claim 11 where the platform team
  names what a metric does NOT measure)
- **Quote**: "Working-Set Rebuild Factor measures cumulative context
  reconstruction relative to peak invocation context. It is an
  efficiency/trajectory metric, not a measurement of semantic coherence debt
  and not a predictor of task success."
- **Our assessment**: This is a genuinely new metric to the corpus: a numeric
  ratio (cumulative input tokens ÷ peak input tokens) that quantifies how much
  a multi-invocation agent run "re-sends" context across invocations rather
  than building incrementally. A rebuild factor near 1.0 suggests each
  invocation mostly reused prior context economically; a high rebuild factor
  suggests the harness is repeatedly reconstructing large context windows
  from scratch across invocations — a token-efficiency anti-pattern distinct
  from (but related to) the "chatty" LLM-calling pattern that
  `blog-ghaw-agent-observability.md` Claim 4 describes. The explicit
  disclaimer — this is NOT a task-success predictor — is important
  editorial guidance: teams should not conflate a low rebuild factor with
  "the agent did a good job," only with "the agent didn't waste tokens
  reconstructing context." For Ch04/Ch07: document rebuild factor as a
  context-engineering efficiency signal, paired with the explicit disclaimer
  to prevent practitioners from over-interpreting it as a quality metric.

### Claim 4: Agent/GenAI span attributes follow OpenTelemetry's GenAI semantic-convention naming (`gen_ai.*`) specifically for compatibility with existing dashboards and backends, separate from the platform's own `gh-aw.*` namespace

- **Evidence**: A 12-row table of `gen_ai.*` attributes (`gen_ai.system`,
  `gen_ai.request.model`, `gen_ai.operation.name`, `gen_ai.usage.input_tokens`,
  `gen_ai.usage.cache_read.input_tokens`, `gen_ai.usage.cache_creation.input_tokens`,
  `gen_ai.usage.total_tokens`, etc.), with `gen_ai.system` explicitly annotated
  as a "compatibility" field.
- **Confidence**: settled (first-party attribute table; the compatibility
  framing is explicit for `gen_ai.system`, and the guide page confirms the
  broader pattern: "gh-aw emits built-in spans for setup, conclusion, and
  outcome events using OpenTelemetry GenAI semantic conventions")
- **Quote**: `gen_ai.system` — "Compatibility GenAI system/provider name used
  by existing gh-aw dashboards and backends."
- **Our assessment**: Standardizing on the OTel GenAI semantic conventions
  (rather than an all-custom `gh-aw.*` schema) means practitioners with
  existing GenAI-aware observability tooling (dashboards built for
  OpenTelemetry's `gen_ai.*` conventions generally, not gh-aw-specific ones)
  can plug gh-aw spans into that tooling with minimal adaptation — cache-read
  and cache-creation token attributes in particular mirror what
  Anthropic/OpenAI SDK instrumentation typically emits. For Ch04
  (Observability and Cost): document the split — `gen_ai.*` for
  cross-platform-compatible model/token data, `gh-aw.*` for
  platform-specific execution and outcome data — as the mental model for
  writing gh-aw-aware dashboards without vendor lock-in to gh-aw's own schema.

### Claim 5: Episode and hop attributes support tracking nested, multi-run execution structures — an episode groups related runs, and hops track parent/child relationships within workflow-call chains

- **Evidence**: Nine attributes cover episode/hop tracking:
  `gh-aw.episode.id`, `gh-aw.episode.kind` (values include `run` or
  `workflow_call`), `gh-aw.hop.id`, `gh-aw.hop.parent_id`,
  `gh-aw.workflow_call.id`, `gh-aw.workflow_call.parent_id`,
  `gh-aw.origin.event`, `gh-aw.root.repo`, `gh-aw.root.workflow_id`.
- **Confidence**: settled (first-party attribute table; introductory framing
  is explicit)
- **Quote**: `gh-aw.episode.kind` — "Episode kind such as `run` or
  `workflow_call`."
- **Our assessment**: This is the OTel-schema-level implementation of the
  episode concept that `docs-ghaw-outcomes-reference.md` Claim 9 defines
  conceptually ("For orchestrated workflows, multiple runs can belong to one
  logical execution. In that case, the more meaningful unit is the
  episode.") — that note describes rolling up outcome/cost totals from runs
  into episodes but does not enumerate the attribute names that carry episode
  membership on spans. This page fills that gap: `gh-aw.episode.id` is the
  join key, `gh-aw.hop.id`/`gh-aw.hop.parent_id` and
  `gh-aw.workflow_call.id`/`gh-aw.workflow_call.parent_id` provide the
  parent/child structure within an episode, and `gh-aw.root.repo` /
  `gh-aw.root.workflow_id` anchor the whole chain back to its origin. For
  Ch04 (Multi-agent orchestration): document this attribute set as the
  concrete mechanism for building episode-level rollup dashboards/queries
  against raw OTel data, directly implementing the abstract episode rollup
  `docs-ghaw-outcomes-reference.md` Claim 9 describes.

### Claim 6: Outcome summary attributes enumerate the exact OTel field names for acceptance rate, waste rate, and zero-touch rate that the outcomes framework describes only conceptually elsewhere in the corpus

- **Evidence**: A 22-row table of `gh-aw.outcome.*` summary attributes
  includes `gh-aw.outcome.accepted`, `gh-aw.outcome.rejected`,
  `gh-aw.outcome.ignored`, `gh-aw.outcome.pending`, `gh-aw.outcome.noop`,
  `gh-aw.outcome.acceptance_rate` ("Accepted fraction"),
  `gh-aw.outcome.waste_rate` ("Rejected fraction"),
  `gh-aw.outcome.noop_rate` ("No-op fraction"),
  `gh-aw.outcome.zero_touch_count`, `gh-aw.outcome.zero_touch_rate`, and
  `gh-aw.outcome.median_resolution_sec`.
- **Confidence**: settled (first-party attribute table; names map directly
  onto the six outcome states and the zero-touch concept already documented
  conceptually in `docs-ghaw-outcomes-reference.md`)
- **Quote**: `gh-aw.outcome.waste_rate` — "Rejected fraction."
- **Our assessment**: This is the single most valuable claim in the source
  for closing a documented corpus gap.
  `docs-ghaw-outcomes-reference.md` Claim 7 states, in general terms:
  "Workflow-level rollups such as accepted counts and acceptance rate are
  emitted on outcome summary or conclusion spans" — but that note's own
  Extraction Notes (item 4) explicitly says the telemetry reference page
  "was not followed" during that extraction and "would warrant a separate
  source note." This page is that separate source note. It confirms the
  outcomes reference's general claim and supplies the literal attribute
  names a practitioner would query: `gh-aw.outcome.acceptance_rate` and
  `gh-aw.outcome.waste_rate` are the two headline metrics; `waste_rate` is
  notably named "waste" rather than "rejection," echoing the "failures or
  waste" phrasing `docs-ghaw-monitor-ops.md` Claim 6 documents as the
  MonitorOps pattern's dual detection dimension. The presence of both
  `gh-aw.outcome.zero_touch_count` and `_rate` as summary-level rollups
  (distinct from the per-item `zero_touch` boolean in Claim 7 below) means
  fleet-wide zero-touch-acceptance trending is queryable without per-item
  aggregation. For Ch04/Ch07: this attribute list is the direct
  implementation reference for the "five-metric basic dashboard" that
  `docs-ghaw-outcomes-reference.md` Claim 10 recommends — map
  `total accepted outcomes` → `gh-aw.outcome.accepted`,
  `effective tokens per accepted outcome` → derived from `gh-aw.aic` (or
  legacy ET) ÷ `gh-aw.outcome.accepted`, etc.

### Claim 7: Outcome per-item attributes include a `zero_touch` boolean plus PR-shape metrics (changed files, additions, deletions, review comments), giving per-output audit-trail granularity beyond the summary rollups

- **Evidence**: A 23-row table of `gh-aw.outcome.*` per-item attributes
  includes `gh-aw.outcome.result`, `gh-aw.outcome.evidence_strength`,
  `gh-aw.outcome.url`, `gh-aw.outcome.changed_files`,
  `gh-aw.outcome.additions`, `gh-aw.outcome.deletions`,
  `gh-aw.outcome.review_comments`, `gh-aw.outcome.reactions_total`,
  `gh-aw.outcome.reactions_positive`, `gh-aw.outcome.reactions_negative`, and
  `gh-aw.outcome.zero_touch` ("Boolean zero-touch flag").
  `gh-aw.outcome.pending_age_sec` measures how long a pending item has been
  unresolved.
- **Confidence**: settled (first-party attribute table)
- **Quote**: `gh-aw.outcome.zero_touch` — "Boolean zero-touch flag."
- **Our assessment**: This directly instantiates
  `docs-ghaw-outcomes-reference.md` Claim 7's description of per-item spans
  carrying "object type, URL, comments, review activity, and zero-touch
  acceptance" — every field named in that prose description has a
  corresponding attribute here (`gh-aw.outcome.type`, `gh-aw.outcome.url`,
  `gh-aw.outcome.comments`, `gh-aw.outcome.review_comments`,
  `gh-aw.outcome.zero_touch`). The PR-shape metrics (`changed_files`,
  `additions`, `deletions`) are new to the corpus and enable a practitioner
  to correlate outcome (accepted/rejected) with PR size — e.g., querying
  whether large PRs are rejected at a higher rate than small ones, a
  question the outcomes reference's conceptual description does not surface
  a mechanism for answering. `gh-aw.outcome.pending_age_sec` is the field
  that operationalizes `docs-ghaw-outcomes-reference.md` Claim 4's
  guidance to "monitor `ignored` and `pending` rates" — it gives a numeric
  age rather than just a state, enabling an alert like "flag any pending
  item older than N days." For Ch03 (Safety and Verification): document
  per-item outcome spans as the audit-trail data source for reviewing
  exactly which outputs were accepted/rejected and why (via
  `gh-aw.outcome.detail` and `gh-aw.outcome.signal`).

### Claim 8: Experiment attributes support A/B-testing gh-aw workflows by recording per-experiment variant assignments as span attributes

- **Evidence**: Two attributes: `gh-aw.experiment.<name>` ("Variant assigned
  for a named experiment") and `gh-aw.experiments` ("Serialized map of valid
  experiment assignments").
- **Confidence**: emerging (attribute names and one-line descriptions are
  explicit and settled as platform fields, but no worked example of an
  experiment configuration or use case is shown on this page, so how
  experiments are declared/randomized is not verifiable from this source)
- **Quote**: `gh-aw.experiments` — "Serialized map of valid experiment
  assignments."
- **Our assessment**: This is a wholly new concept to the corpus: no existing
  gh-aw source note documents an A/B-testing or experimentation framework
  for agentic workflows. The templated attribute name
  (`gh-aw.experiment.<name>`) suggests a workflow can be enrolled in
  multiple named experiments simultaneously (e.g., testing two different
  prompt variants, or two different models), with each variant assignment
  recorded as its own span attribute for later cohort analysis against
  outcome data. Because the page gives no configuration syntax for
  *declaring* an experiment, this claim is marked emerging rather than
  settled — the attribute schema is confirmed, but the authoring workflow is
  not. For Ch04 (Scaling): flag as a candidate technique for teams that want
  to compare workflow variants (prompt changes, model changes) using outcome
  efficiency as the comparison metric, pending a follow-up source that
  documents experiment declaration syntax.

### Claim 9: Attributes are emitted conditionally — only when the underlying value is available — and different span types carry different subsets of the full schema

- **Evidence**: An explicit scoping statement appears on the page, positioned
  as a caveat governing interpretation of every table on the page.
- **Confidence**: settled (first-party, direct quote)
- **Quote**: "Unless stated otherwise, attributes are emitted only when the
  underlying value is available. Different spans carry different subsets of
  these fields."
- **Our assessment**: This is a necessary caveat for anyone building
  dashboards or alerts off this schema: the absence of an attribute on a
  given span is not necessarily an error condition — it may simply mean the
  value was not computable for that run (e.g., `working_set.rebuild_factor`
  is explicitly "omitted when unavailable" per Claim 3, and several
  workflow-call/episode attributes only apply to runs that participate in
  nested execution). For Ch04: document this as a query-writing gotcha —
  dashboards/alerts built against gh-aw OTel data must treat missing
  attributes as "not applicable to this span type," not "instrumentation
  bug," and should not assume every attribute in this reference appears on
  every span.

### Claim 10: Trace data is mirrored to local JSONL files and uploaded as a workflow artifact, with `otel.jsonl` specifically covering spans emitted by gh-aw's JavaScript helper code

- **Evidence**: Both the attribute-reference page and its companion guide
  page describe the same artifact mechanism.
- **Confidence**: settled (first-party, consistent description across both
  the reference page and the companion guide page)
- **Quote**: "When observability is enabled, trace data is also mirrored to
  local JSONL files and uploaded in the `agent` artifact: `otel.jsonl` for
  spans emitted by gh-aw JavaScript helpers"
- **Our assessment**: This gives practitioners a debugging path that does
  not require a live OTLP backend: even without configuring
  `observability.otlp`, trace data lands in the workflow run's `agent`
  artifact as `otel.jsonl`, downloadable and inspectable per-run. This
  complements the CLI-based inspection tools (`gh aw audit`, `gh aw logs`)
  documented in `docs-ghaw-monitoring-patterns.md` Claims 7-9 — those are
  live commands against the platform's own log store, while `otel.jsonl` is
  a raw per-run artifact a practitioner can pull into their own tooling. For
  Ch02 (Harness Engineering): document `otel.jsonl` in the `agent` artifact
  as the zero-configuration entry point for inspecting span data before
  investing in a full OTLP backend integration.

### Claim 11: Workflow-level OTLP span export is configured entirely in workflow frontmatter (`observability.otlp.endpoint`), separate from and complementary to the MCP Gateway's own `gateway.opentelemetry` config already documented in the corpus

- **Evidence**: The companion `reference/open-telemetry` guide page shows a
  complete Sentry export configuration requiring both a `network.allowed`
  entry and an `observability.otlp.endpoint` block with a secret-sourced
  `Authorization` header.
- **Confidence**: settled (first-party YAML configuration example, cross-
  validated against the attribute reference page's own description of
  `observability.otlp.resource-attributes`)
- **Quote**: (no single prose quote; see Concrete Artifacts for the YAML)
- **Our assessment**: This is a distinct configuration surface from
  `docs-ghaw-mcp-gateway-reference.md` Claim 9's `gateway.opentelemetry`
  field. That claim documents OTel configuration for the MCP Gateway's own
  proxy-layer tracing (tool invocations passing through the gateway); this
  claim documents OTel configuration for the *workflow's* own span export
  (setup/conclusion/outcome spans, GenAI spans, etc.) at the frontmatter
  level. The two are not in conflict — they are two independent
  instrumentation points in the same platform, each configured separately
  and potentially pointed at different backends. Practitioners wanting
  end-to-end tracing across both the workflow execution and the MCP tool
  calls it makes would need to configure both. For Ch02/Ch04: document the
  two-config-surface model explicitly so practitioners do not assume
  configuring one automatically enables the other.

### Claim 12: Organizations can enable OTLP export across all workflows without editing individual workflow files, via two repository/org-level settings — an unencrypted endpoint variable and a secret headers value

- **Evidence**: The guide page documents `GH_AW_DEFAULT_OTLP_ENDPOINT` (typed
  as a Variable) and `GH_AW_DEFAULT_OTLP_HEADERS` (typed as a Secret,
  described as "comma-separated key=value pairs"), with frontmatter
  configuration explicitly stated to override these defaults.
- **Confidence**: settled (first-party; the Variable/Secret type distinction
  is explicit)
- **Quote**: (no single prose quote; see Concrete Artifacts)
- **Our assessment**: The Variable/Secret split mirrors the resource-
  attributes-must-not-be-secret guidance in Claim 1 — the endpoint URL is
  not sensitive and is stored as a plain repository Variable, while
  authorization headers are credentials and correctly go in a Secret. This
  two-tier default mechanism is operationally significant for org-wide
  observability rollout: a platform team can turn on tracing for every
  gh-aw workflow in an organization by setting two org-level values once,
  rather than editing every workflow's frontmatter individually — and
  individual workflows retain an escape hatch to override the org default
  via their own `observability.otlp` block. For Ch05 (Team Adoption):
  document the org-default env vars as the recommended rollout mechanism
  for observability at scale, versus per-workflow configuration for
  one-off or backend-specific needs.

### Claim 13: gh-aw supports reading existing telemetry back into a workflow via an MCP server (demonstrated with Sentry's MCP server), making observability data queryable by the agent itself, not just exported for human dashboards

- **Evidence**: The guide page's "Read Telemetry Through MCP" section shows a
  complete `mcp-servers` configuration for the Sentry MCP server, with an
  explicit allowlist of read-only Sentry operations
  (`whoami`, `find_organizations`, `get_trace_details`, `search_events`).
- **Confidence**: emerging (the mechanism and one worked example — Sentry —
  are settled/documented, but whether other OTel backends have equivalent
  MCP servers, or whether this pattern is broadly used in production, is
  not established by this source alone)
- **Quote**: (no single prose quote; see Concrete Artifacts for the YAML)
- **Our assessment**: This is a genuinely novel bidirectional-observability
  pattern not documented anywhere else in the corpus: `blog-ghaw-agent-
  observability.md` Claim 7 speculates, with only emerging confidence, that
  "metrics data should feed upward to higher-level orchestrators" but
  describes the mechanism as unclear from that source. This page provides a
  concrete mechanism — an agent workflow that includes `mcp-servers.sentry`
  in its tools can call `get_trace_details` or `search_events` directly
  during its own run, meaning a workflow could, for example, inspect its own
  or a sibling workflow's recent trace history as part of its reasoning,
  closing the loop between "telemetry was emitted" and "an agent consumed
  that telemetry to make a decision" without a human or a separate
  dashboard in between. For Ch04 (Multi-agent orchestration): document
  read-side MCP telemetry access as a concrete implementation of the
  "metrics as orchestration input" pattern that
  `blog-ghaw-agent-observability.md` Claim 7 named but could not describe
  mechanistically; this closes that gap with worked YAML.

### Claim 14: Custom span attributes can be attached via `observability.otlp.attributes` using template expressions that resolve from computed span attributes (e.g., `{{ gh-aw.episode.id }}`), enabling integration with session/user-tracking backends like Langfuse

- **Evidence**: The guide page shows a YAML example setting
  `langfuse.session.id: "{{ gh-aw.episode.id }}"` and
  `langfuse.user.id: "{{ github.actor }}"` under
  `observability.otlp.attributes`, with an explicit note that empty values
  are omitted and non-empty values are masked in logs.
- **Confidence**: settled (first-party YAML example with explicit templating
  and masking-behavior documentation)
- **Quote**: "Template expressions resolve from computed span attributes.
  Empty values are omitted and non-empty values are masked in logs."
- **Our assessment**: The ability to reference `gh-aw.episode.id` (a
  platform-computed attribute from Claim 5) as a template source for a
  *custom* attribute is a composability detail: it means custom attributes
  are not limited to static strings or raw GitHub Actions expressions — they
  can incorporate the platform's own computed telemetry values, enabling
  direct mapping onto third-party observability platforms' own session/user
  conventions (Langfuse's `session.id`/`user.id` here) without needing the
  third-party backend to understand gh-aw's `gh-aw.*` namespace at all. The
  masking-in-logs behavior is a security-adjacent detail worth noting
  alongside Claim 1's secrets warning, though it is a distinct
  mechanism (log masking vs. a hard prohibition on secret values in
  resource attributes). For Ch02: document custom span attributes with
  template expressions as the integration mechanism for third-party
  observability platforms with their own semantic conventions.

## Concrete Artifacts

### Resource Attributes (selected rows, verbatim from `reference/open-telemetry-attributes`)

```
service.name              — OTel service name for the emitting component or workflow.
service.version            — Version of the emitting gh-aw helper when available.
gh-aw.workflow.name         — Workflow name.
gh-aw.repository            — GitHub repository in `owner/repo` form.
gh-aw.run.id                — GitHub Actions run ID.
github.run_id               — GitHub run ID compatibility resource attribute.
github.repository           — GitHub repository compatibility resource attribute.
runner.os / runner.arch / runner.name / runner.environment
gh-aw.awf.version            — Workflow compiler version when available.
gh-aw.awmg.version           — MCP gateway version when available.
deployment.environment       — `staging` or `production` depending on staged mode.
```

### AI Credits Span Attributes (verbatim)

```
gh-aw.aic                          — AI credits consumed for the run when available.
gh-aw.max_ai_credits                — Configured max AI credits budget for the run when available.
gh-aw.max_ai_credits_exceeded       — Whether the run exceeded the max AI credits budget.
gh-aw.ai_credits_rate_limit_error   — Whether an AI-credits rate-limit or budget-exhaustion signal was detected.
gh-aw.turns                         — Total agent turns recorded for the run.
```

### Working-Set Attributes (verbatim)

```
gh-aw.working_set.measurement_state        — measured | partial | unavailable
gh-aw.working_set.rebuild_factor            — Cumulative canonical input tokens ÷ peak invocation input tokens. Omitted when unavailable.
gh-aw.working_set.cumulative_input_tokens   — Sum of canonical logical input tokens across measured agent invocations.
gh-aw.working_set.peak_input_tokens         — Largest canonical logical input-token count among measured agent invocations.
gh-aw.working_set.rebuild_excess_tokens     — Cumulative input tokens minus peak input tokens, clamped to zero.
gh-aw.working_set.invocations               — Valid invocation records contributing to the working-set measurement.
```

### Outcome Summary Attributes (verbatim, full table)

```
gh-aw.outcome.runs_checked              — Number of runs checked while computing the summary.
gh-aw.outcome.total                     — Total evaluated outcomes.
gh-aw.outcome.accepted                  — Accepted outcome count.
gh-aw.outcome.rejected                  — Rejected outcome count.
gh-aw.outcome.ignored                   — Ignored outcome count.
gh-aw.outcome.pending                   — Pending outcome count.
gh-aw.outcome.noop                      — No-op outcome count.
gh-aw.outcome.accepted_strong           — Strongly accepted outcome count.
gh-aw.outcome.accepted_medium           — Medium-strength accepted outcome count.
gh-aw.outcome.accepted_weak             — Weakly accepted outcome count.
gh-aw.outcome.fallback_exists_only_count — Fallback exists-only acceptance count.
gh-aw.outcome.acceptance_rate           — Accepted fraction.
gh-aw.outcome.waste_rate                — Rejected fraction.
gh-aw.outcome.noop_rate                 — No-op fraction.
gh-aw.outcome.zero_touch_count          — Zero-touch accepted count.
gh-aw.outcome.zero_touch_rate           — Zero-touch acceptance fraction.
gh-aw.outcome.item_count                — Number of evaluated items in the summary payload.
gh-aw.outcome.date                      — Summary date when present.
gh-aw.outcome.median_resolution_sec     — Median resolution time in seconds.
gh-aw.outcome.events                    — Comma-separated event names represented in the summary.
gh-aw.outcome.workflows                 — Comma-separated workflow names represented in the summary.
gh-aw.outcome.types                     — Comma-separated outcome object types represented in the summary.
```

*Source: `reference/open-telemetry-attributes`, "Outcome Summary Attributes" section*

### Outcome Per-Item Attributes (verbatim, full table)

```
gh-aw.outcome.type              — Object type being evaluated.
gh-aw.outcome.result            — Observed result classification.
gh-aw.outcome.outcome_status    — Normalized outcome status.
gh-aw.outcome.evidence_strength — Evidence strength classification.
gh-aw.outcome.workflow          — Source workflow name.
gh-aw.outcome.run_id            — Source run ID.
gh-aw.outcome.repo              — Repository associated with the item.
gh-aw.outcome.url               — Primary URL for the evaluated object.
gh-aw.outcome.detail            — Additional detail string.
gh-aw.outcome.signal            — Signal that triggered evaluation.
gh-aw.outcome.created_at        — Creation timestamp.
gh-aw.outcome.event             — Outcome event label.
gh-aw.outcome.resolution_sec    — Resolution time in seconds.
gh-aw.outcome.pending_age_sec   — Age of a pending item in seconds.
gh-aw.outcome.review_comments   — Review comment count.
gh-aw.outcome.changed_files     — Changed file count.
gh-aw.outcome.additions         — Added line count.
gh-aw.outcome.deletions         — Deleted line count.
gh-aw.outcome.reactions_total   — Total reaction count.
gh-aw.outcome.reactions_positive — Positive reaction count.
gh-aw.outcome.reactions_negative — Negative reaction count.
gh-aw.outcome.comments          — Comment count.
gh-aw.outcome.zero_touch        — Boolean zero-touch flag.
```

*Source: `reference/open-telemetry-attributes`, "Outcome Per-item Attributes" section*

### Episode/Hop/Workflow-Call Attributes (verbatim)

```
gh-aw.episode.id              — Episode identifier used to roll up related runs.
gh-aw.episode.kind            — Episode kind such as `run` or `workflow_call`.
gh-aw.hop.id                  — Current hop identifier within an episode.
gh-aw.hop.parent_id           — Parent hop identifier when nested.
gh-aw.workflow_call.id        — Current workflow-call hop identifier.
gh-aw.workflow_call.parent_id — Parent workflow-call hop identifier.
gh-aw.origin.event            — Original triggering event for the root execution.
gh-aw.root.repo               — Root repository for the episode.
gh-aw.root.workflow_id        — Root workflow identifier.
```

### Experiment Attributes (verbatim, full table)

```
gh-aw.experiment.<name> — Variant assigned for a named experiment.
gh-aw.experiments       — Serialized map of valid experiment assignments.
```

### Write-Side OTLP Export Config — Sentry Example

From the companion `reference/open-telemetry` guide page:

```yaml
---
network:
  allowed:
    - "*.sentry.io"
observability:
  otlp:
    endpoint:
      - url: ${{ secrets.GH_AW_OTEL_SENTRY_ENDPOINT }}
        headers:
          Authorization: ${{ secrets.GH_AW_OTEL_SENTRY_AUTHORIZATION }}
---
```

### Organization-Wide OTLP Defaults

```
GH_AW_DEFAULT_OTLP_ENDPOINT   (Variable) — OTLP endpoint URL
GH_AW_DEFAULT_OTLP_HEADERS    (Secret)   — Exporter headers as comma-separated key=value pairs

Frontmatter configuration overrides these defaults entirely.
```

### Google Workload Identity Federation for OTLP

```yaml
observability:
  otlp:
    endpoint:
      - url: https://telemetry.googleapis.com
        headers:
          x-goog-user-project: ${{ vars.GCP_PROJECT_ID }}
    workload-identity:
      provider: google
      audience: ${{ vars.GCP_WIF_PROVIDER }}
      service-account: ${{ vars.GCP_SA_EMAIL }}
```

### Read-Side MCP Telemetry Query — Sentry Example

```yaml
---
mcp-servers:
  sentry:
    command: "npx"
    args: ["@sentry/mcp-server@0.33.0"]
    allowed:
      - whoami
      - find_organizations
      - get_trace_details
      - search_events
    env:
      SENTRY_ACCESS_TOKEN: ${{ secrets.SENTRY_ACCESS_TOKEN }}
      SENTRY_HOST: ${{ env.SENTRY_HOST || 'sentry.io' }}
---
```

### Custom Span/Resource Attributes

```yaml
observability:
  otlp:
    attributes:
      deployment.environment: production
      langfuse.session.id: "{{ gh-aw.episode.id }}"
      langfuse.user.id: "{{ github.actor }}"

observability:
  otlp:
    resource-attributes:
      service.namespace: platform-automation
      deployment.environment: ${{ github.ref_name }}
```

### Custom Spans from Shared Imports (`otlp.cjs` helper)

```javascript
const otlp = require('/tmp/gh-aw/actions/otlp.cjs');

const startMs = Date.now();
// ... do work ...
const endMs = Date.now();

await otlp.logSpan('my-tool', {
  'my-tool.version': '1.2.3',
  'my-tool.items_processed': 42,
  'my-tool.result': 'success',
}, { startMs, endMs });
```

Environment variables set automatically for use with `otlp.cjs` and manual
span emission:

```
GITHUB_AW_OTEL_TRACE_ID          — 32-character hex trace ID
GITHUB_AW_OTEL_PARENT_SPAN_ID    — 16-character hex parent span ID
OTEL_EXPORTER_OTLP_ENDPOINT      — Collector base URL
OTEL_EXPORTER_OTLP_HEADERS       — Authentication headers
```

*Source: `reference/open-telemetry`, "Custom Spans from Shared Imports" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-outcomes-reference.md` Claim 7 (workflow-level rollups on
    summary/conclusion spans; per-item spans carry object type, URL,
    comments, review activity, zero-touch acceptance): Claims 6 and 7 of
    this note supply the exact attribute names for every field that claim
    describes in prose, without naming a single attribute.
  - `docs-ghaw-outcomes-reference.md` Claim 9 (episode as the rollup unit
    for orchestrated workflows): Claim 5 of this note supplies the
    attribute names (`gh-aw.episode.id`, `gh-aw.hop.id`,
    `gh-aw.workflow_call.id`) that implement episode membership at the
    span level.
  - `blog-ghaw-ai-credits-migration.md` Claim 1 (AI Credits replaced
    Effective Tokens as the primary spend metric): Claim 2 of this note
    confirms AIC is fully represented in the OTel span schema
    (`gh-aw.aic`, `gh-aw.max_ai_credits`, and two boolean flags), not just
    in CLI output.
  - `docs-ghaw-mcp-gateway-reference.md` Claim 9 (gateway-level OTel via
    `gateway.opentelemetry.endpoint`/`serviceName`, with T-OTEL-001 through
    T-OTEL-010 compliance tests): Claim 11 of this note documents the
    complementary workflow-level OTLP config surface
    (`observability.otlp.endpoint`). Both sources agree OpenTelemetry is a
    first-class, tested integration point in gh-aw; they document two
    different layers of the same platform (gateway proxy traffic vs.
    workflow execution spans), not conflicting claims.
  - `docs-ghaw-monitor-ops.md` Claim 6 ("failures or waste" as the
    co-equal dual dimension MonitorOps surfaces across teams): Claim 6 of
    this note shows `gh-aw.outcome.waste_rate` is the literal OTel field
    name for "waste," confirming the terminology is consistent from
    pattern-page prose down to the attribute schema.
  - `docs-ghaw-monitoring-patterns.md` Claims 7-9 (`gh aw audit`,
    `gh aw logs` as CLI-level operational inspection): Claim 10 of this
    note documents `otel.jsonl` in the `agent` artifact as a complementary,
    file-based inspection path that does not require the OTLP backend or
    CLI to be configured.

- **Extends**:
  - `docs-ghaw-outcomes-reference.md`: that note's own Extraction Notes
    (item 4) explicitly flags the telemetry reference as not-yet-followed
    and names it as a candidate for a dedicated source note "if the guide's
    observability chapters need that level of instrumentation detail." This
    note is that follow-up extraction.
  - `blog-ghaw-agent-observability.md` Claim 7 ("metrics data should feed
    upward to higher-level orchestrators," marked emerging because "the
    post does not describe the mechanism in detail"): Claim 13 of this note
    (read-side MCP telemetry query via the Sentry MCP server) is a concrete,
    worked mechanism for exactly this pattern — an agent workflow querying
    its own or another workflow's trace history as an input to its own
    reasoning. This raises confidence on the underlying architectural claim
    even though it does not itself confirm GitHub's production Portfolio
    Analyst uses this specific mechanism.
  - `docs-ghaw-mcp-gateway-reference.md`: extends the gateway-level OTel
    picture with the workflow-level configuration surface, the full
    attribute schema for what actually gets traced, and (novel to the
    corpus) the read-side MCP query mechanism the gateway spec does not
    mention.

- **Contradicts**: None identified. The workflow-level `observability.otlp`
  config and the gateway-level `gateway.opentelemetry` config
  (`docs-ghaw-mcp-gateway-reference.md` Claim 9) could be mistaken for
  overlapping/competing configuration surfaces, but on close reading they
  configure different span-emission points in the same platform and are
  additive, not conflicting. No contradiction issue filed.

- **Novel**:
  - **The working-set rebuild factor metric and its explicit
    non-task-success disclaimer** (Claim 3): not documented anywhere else
    in the corpus.
  - **The complete outcome summary and per-item attribute vocabulary**
    (Claims 6-7): fills the gap `docs-ghaw-outcomes-reference.md`
    explicitly left open.
  - **Read-side MCP telemetry querying** (Claim 13): the first source in
    the corpus documenting that a gh-aw workflow can query its own OTel
    trace history via an MCP server as part of its own execution, rather
    than telemetry being purely a write-out-for-humans mechanism.
  - **Experiment/A-B-testing attributes** (Claim 8): no existing corpus
    source documents any experimentation framework for gh-aw workflows.
  - **`otlp.cjs` custom span helper and its auto-set environment variables**
    (Concrete Artifacts): not documented elsewhere; gives shared-import
    authors a documented way to emit their own spans correlated to the
    parent workflow's trace.
  - **Org-wide OTLP default env vars** (Claim 12): the
    Variable/Secret-typed default mechanism for org-wide observability
    rollout is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the secrets-in-resource-
  attributes anti-pattern (Claim 1) as an explicit warning alongside any
  guidance about `observability.otlp` configuration. Add `otel.jsonl` in
  the `agent` artifact (Claim 10) as the zero-configuration first step for
  inspecting trace data. Add custom span attributes with template
  expressions (Claim 14) as the integration mechanism for third-party
  observability platforms with their own conventions (Langfuse session/user
  IDs as the worked example).

- **Chapter 04 (Multi-agent orchestration / Observability and Cost)**: Add
  the episode/hop attribute set (Claim 5) as the concrete implementation
  reference for episode-level rollup dashboards, directly extending
  `docs-ghaw-outcomes-reference.md` Claim 9. Add the outcome summary and
  per-item attribute vocabulary (Claims 6-7) as the field-name reference
  for the five-metric dashboard `docs-ghaw-outcomes-reference.md` Claim 10
  recommends. Add read-side MCP telemetry querying (Claim 13) as a concrete
  pattern for building the "closed-loop agent governance" that
  `blog-ghaw-agent-observability.md` Claim 7 speculated about but could not
  describe mechanistically.

- **Chapter 07 (Cost and Observability, if distinct from Ch04 in the
  guide's final structure)**: Add AI Credits span-level budget tracking
  (Claim 2) — recommend alerting on `gh-aw.max_ai_credits_exceeded` and
  `gh-aw.ai_credits_rate_limit_error` as distinct signals from raw cost.
  Add the working-set rebuild factor (Claim 3) as a context-engineering
  efficiency metric, with the platform's own disclaimer preserved verbatim
  to prevent over-interpretation as a task-success signal.

- **Chapter 05 (Team Adoption)**: Add the org-wide OTLP default environment
  variables (Claim 12) as the recommended rollout mechanism for enabling
  observability across many workflows without per-file edits.

## Extraction Notes

1. **Two pages extracted, one issue**: The `reference/open-telemetry-attributes`
   page (the page filed in this issue) explicitly defers all configuration
   and setup guidance to a companion page, `reference/open-telemetry`. Per
   MINER.md §1 ("follow up to 5 linked pages that seem substantive"), the
   companion page was fetched and extracted as well (Claims 11-14 and
   several Concrete Artifacts derive from it), since the attribute
   inventory alone is not actionable without the configuration surface that
   populates it. Both pages are attributed by name throughout this note and
   in each artifact's source line.

2. **WebFetch returns AI-summarized content**: Both pages are served from
   the gh-aw Astro/Starlight documentation site. WebFetch renders and
   summarizes HTML through an intermediate model rather than returning raw
   markdown source. Five separate targeted fetches were made across the two
   pages (resource/workflow-span tables; GenAI/episode tables; outcome/
   experiment tables; trace-artifact and emission-condition text; the full
   companion guide page) to maximize verbatim coverage and cross-validate
   attribute names and descriptions. All attribute names and their
   one-line descriptions were returned consistently as table rows across
   passes; prose quotes were retained only where fetch results marked them
   as direct quotations from the page.

3. **No "type" or "example" table columns exist on the page**: The prompt
   used in the first fetch pass asked for type/example columns, and the
   fetch result explicitly clarified the source tables are two-column
   (attribute name, description) only — there is no separate type or
   example-value column on this reference page. This note reflects that
   the source itself does not provide per-attribute type/example data
   beyond what is embedded in the description text (e.g., enumerated
   values like `measured`/`partial`/`unavailable`).

4. **No sample trace/span JSON on the page**: A dedicated fetch pass
   confirmed the attribute-reference page contains no sample trace/span
   JSON payloads and no code blocks; it is a pure attribute-name inventory.
   Sample configuration YAML exists only on the companion
   `reference/open-telemetry` guide page and is reproduced in Concrete
   Artifacts above.

5. **Publication date not available**: Neither page carries an explicit
   publication date in the fetched content. `date_published` is left null,
   consistent with the convention used in sibling `reference/` and
   `patterns/` notes in this corpus (e.g., `docs-ghaw-monitoring-patterns.md`,
   `docs-ghaw-monitor-ops.md`) where the gh-aw docs site does not surface
   per-page publish dates.

6. **No contradictions filed**: Reviewed `docs-ghaw-mcp-gateway-reference.md`,
   `docs-ghaw-outcomes-reference.md`, `docs-ghaw-monitoring-patterns.md`,
   `docs-ghaw-monitor-ops.md`, `blog-ghaw-agent-observability.md`, and
   `blog-ghaw-ai-credits-migration.md`. No claim in this source materially
   opposes any existing source note. The two OTel configuration surfaces
   (workflow-level `observability.otlp` here vs. gateway-level
   `gateway.opentelemetry` in the MCP Gateway spec) were the one place a
   contradiction seemed plausible on first read; closer comparison shows
   they configure distinct span-emission points and are additive, not
   conflicting. No contradiction issue filed.

7. **`confidence_overall` set to settled**: Twelve of fourteen claims are
   individually rated settled, reflecting that this is a first-party,
   literal attribute-name reference (the highest-confidence source type in
   this corpus, alongside the RFC-style specifications). The two
   `emerging`-rated claims (Claim 8, experiment attributes; Claim 13,
   read-side MCP telemetry) are emerging specifically because the *usage
   mechanism* around those attributes/patterns is thinner than the
   attribute/config evidence itself — not because the underlying platform
   facts are in doubt.
