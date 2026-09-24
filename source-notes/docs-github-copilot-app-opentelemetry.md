---
source_url: https://github.blog/changelog/2026-09-22-opentelemetry-in-the-github-copilot-app
source_type: docs
title: "OpenTelemetry in the GitHub Copilot app"
author: GitHub (official changelog; byline "Allison")
date_published: 2026-09-22
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3656"
---

# OpenTelemetry in the GitHub Copilot App

> GitHub's September 22, 2026 changelog adds OpenTelemetry export to the
> GitHub Copilot app itself, configured centrally via the `telemetry`
> property in enterprise `managed-settings.json` — but the live enterprise
> managed-settings reference doc's own support table and prose both still
> say, as of two days later, that `telemetry` is not supported for the
> GitHub Copilot app client. Filed as contradiction issue #3682.

## Source Context

- **Type**: docs (GitHub official product changelog, September 22, 2026; ~1
  minute read, tagged `copilot`). Two linked documentation pages were
  followed per MINER.md §1: "OpenTelemetry for agent monitoring"
  (`docs.github.com/en/enterprise-cloud@latest/copilot/concepts/enterprise/opentelemetry`),
  which supplied the data-type and default-exclusion detail, and "Getting
  started with enterprise-managed settings"
  (`docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/get-started`),
  which supplied the `.github-private`/`managed-settings.json` deployment
  mechanics. A third page, the "Enterprise managed settings reference"
  (`docs.github.com/copilot/reference/enterprise-managed-settings-reference`),
  was also fetched — not because the changelog linked it, but because it is
  the page that already carries the `telemetry` key's full schema and
  per-client support matrix in this corpus (via
  `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`),
  and cross-checking it surfaced the contradiction this note documents.
- **Author credibility**: GitHub engineering team (changelog byline
  "Allison") announcing a production feature release for the GitHub Copilot
  app. Authoritative for: the existence of the announced capability, the
  named settings property (`telemetry`), the named configuration file
  (`managed-settings.json`), and the stated default content-exclusion
  behavior. Not yet corroborated by the platform's own reference-doc support
  matrix for this specific client — see Extraction Notes and issue #3682.
- **Scope**: A single new capability — OTel export configuration for the
  GitHub Copilot app, delivered via enterprise-managed settings. Covers:
  what OTel is for (session/trace analysis, behavior investigation,
  centralized policy management), where it's configured (`telemetry`
  property, `managed-settings.json`), and the default privacy posture
  (prompt/response content excluded by default). Does NOT cover: the full
  `telemetry` sub-property schema (endpoint, protocol, captureContent, etc.
  — that detail comes from the separately-fetched reference page, not this
  changelog), rollout/preview status (no preview or GA label is stated),
  which specific trace/span attributes the Copilot app emits (contrast with
  `docs-ghaw-open-telemetry-attributes.md`, which documents gh-aw's
  workflow-level OTel attribute schema in detail — this changelog names no
  attributes at all for the Copilot app), or how this interacts with the
  Copilot app's existing usage-metrics telemetry
  (`docs-github-copilot-usage-metrics-server-side-telemetry.md`,
  `docs-github-copilot-app-usage-metrics-report-rollups.md`), which is a
  separate, pre-existing reporting pipeline.

## Extracted Claims

### Claim 1: The GitHub Copilot app now supports OpenTelemetry configuration through enterprise-managed settings, letting administrators export agent session data to their organization's monitoring tools

- **Evidence**: Official changelog opening paragraph, the single-sentence
  summary of the entire release.
- **Confidence**: settled as a product announcement (see Claim 6 for the
  discrepancy over whether this is yet reflected in the platform's own
  reference-doc support matrix)
- **Quote**: "Understand how Copilot agents perform and interact with models
  and tools. The GitHub Copilot app now supports OpenTelemetry (OTel)
  configuration through enterprise-managed settings."
- **Our assessment**: This is the headline claim and the first corpus
  source documenting OTel export specifically for the GitHub Copilot app
  client, as distinct from JetBrains
  (`docs-github-copilot-jetbrains-otel-model-management-july2026.md`,
  `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`)
  or the workflow/gateway layer of GitHub Agentic Workflows
  (`docs-ghaw-open-telemetry-attributes.md`,
  `docs-ghaw-mcp-gateway-reference.md`). It extends the corpus's picture of
  OpenTelemetry as GitHub's standard observability integration point across
  an increasing number of distinct Copilot surfaces.

### Claim 2: OTel export lets administrators follow the flow of a Copilot agent session, including requests to AI models and the tools an agent uses

- **Evidence**: Changelog body, first bullet of the "helps teams" list.
- **Confidence**: settled (stated directly in the official changelog)
- **Quote**: "Analyze agent sessions: Follow the flow of a session, including
  requests to AI models and the tools an agent uses."
- **Our assessment**: This "session flow" framing is a session/trace-level
  capability, not a metrics-only one — consistent with the trace concept
  the linked "OpenTelemetry for agent monitoring" doc formalizes (see Claim
  4). It is functionally the same session-flow value proposition that
  `docs-ghaw-open-telemetry-attributes.md` Claim 5 documents for gh-aw's
  episode/hop span attributes, though at a coarser level of description —
  this changelog names no specific span or attribute, only the capability.

### Claim 3: OTel export lets administrators review step-by-step traces of agent execution in their existing monitoring tools to investigate unexpected behavior, and apply telemetry settings centrally across teams instead of requiring per-developer configuration

- **Evidence**: Changelog body, second and third bullets of the "helps
  teams" list.
- **Confidence**: settled (stated directly in the official changelog)
- **Quote**: "Investigate unexpected behavior: Review step-by-step traces of
  agent execution in their existing monitoring tools." / "Manage monitoring
  centrally: Apply telemetry settings across teams instead of requiring
  each developer to individually configure them."
- **Our assessment**: The "centrally... instead of requiring each developer
  to individually configure them" framing positions this explicitly as an
  enterprise-managed-settings capability from the outset, not an
  individually-configurable one — a different framing than
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` Claim 1,
  which documented JetBrains OTel (as of July 27, 2026) as a
  practitioner-facing settings-UI toggle before enterprise management was
  layered on top a month later
  (`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  Claim 4). This changelog gives no indication the GitHub Copilot app ever
  had an individually-configurable OTel toggle prior to this
  enterprise-managed release — it appears to have shipped centrally-managed
  from day one for this client.

### Claim 4: OpenTelemetry data sent by Copilot clients is categorized into three types — traces (session flow, including model calls and tool use), metrics (numeric measurements like token usage over time), and events (individual actions at a point in time, like edit-feedback)

- **Evidence**: Linked docs page, "OpenTelemetry for agent monitoring"
  (`docs.github.com/en/enterprise-cloud@latest/copilot/concepts/enterprise/opentelemetry`),
  "What data does Copilot send?" section, fetched as raw HTML.
- **Confidence**: settled (first-party docs page, direct quote)
- **Quote**: "Traces show the flow of an agent session and connect each
  step, including model calls and tool use. For example, a trace can show
  an agent calling a model, using the readFile tool, and calling the model
  again to produce a response." / "Metrics are numeric measurements that
  help you identify patterns over time. For example, token usage metrics
  track the number of input and output tokens used in model calls." /
  "Events record individual actions at a specific point in time. For
  example, an edit feedback event records whether a user accepted or
  rejected an agent edit."
- **Our assessment**: This three-way taxonomy (traces / metrics / events)
  is standard OpenTelemetry vocabulary, but the worked examples are
  Copilot-specific and genuinely useful: the "edit feedback event" example
  is the first corpus mention of accept/reject feedback being emitted as an
  OTel event (as opposed to being captured only in product usage-metrics
  reporting, per `docs-github-copilot-app-usage-metrics-report-rollups.md`).
  This gives a practitioner three distinct query surfaces (traces for
  causal flow, metrics for trend dashboards, events for discrete
  moments) rather than one undifferentiated telemetry stream.

### Claim 5: By default, OTel data sent by Copilot clients does not include prompts, responses, or tool arguments; organizations can opt into capturing this content but doing so may expose sensitive information such as code, file contents, and user prompts

- **Evidence**: Changelog "Important Security Note" plus the linked
  "OpenTelemetry for agent monitoring" docs page, "What data does Copilot
  send?" section (both sources state the same fact, cross-checked).
- **Confidence**: settled (stated identically, near-verbatim, in both the
  changelog and the linked concept doc)
- **Quote (changelog)**: "Prompt and response content is excluded by
  default—review your content-capture settings before enabling it."
- **Quote (linked docs page)**: "By default, the data does not include
  prompts, responses, or tool arguments. You can choose to capture this
  content, but it may contain sensitive information, such as code, file
  contents, and user prompts."
- **Our assessment**: This "excluded by default, opt-in for content" design
  matches the pattern the reference page shows for the underlying
  `telemetry` schema's `captureContent` / `lockCaptureContent` sub-properties
  (see Concrete Artifacts) — `lockCaptureContent` lets an enterprise
  administrator prevent developers from ever flipping `captureContent` to
  `true` locally, which is the concrete enforcement mechanism behind this
  "review before enabling" warning. This is a sensible default for an
  enterprise-wide telemetry pipeline: code and prompt content routed
  unredacted to an arbitrary OTLP collector is a real data-exposure surface,
  and the corpus already documents an analogous secrets-in-telemetry
  anti-pattern for a different product (`docs-ghaw-open-telemetry-attributes.md`
  Claim 1: custom resource attributes must never carry secret values because
  "resource attributes are exported to external observability backends and
  are not treated as secret values").

### Claim 6 (novel corpus finding via cross-check, not from the source itself): As of two days after this changelog's publication, the platform's own "Enterprise managed settings reference" page's support matrix and prose both state that the `telemetry` key is NOT supported for the GitHub Copilot app — directly contradicting this changelog's central claim

- **Evidence**: `docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
  fetched as raw HTML on 2026-09-24 (two days after this changelog's
  2026-09-22 publication date). The "Supported keys" table's `telemetry`
  row renders an "Not supported" icon (`<svg ... aria-label="Not
  supported">`) in the "GitHub Copilot app" column, and the page's own
  prose subsection for the `telemetry` key states the client scope
  explicitly.
- **Confidence**: emerging — this is a live, dated observation about two
  GitHub-owned pages disagreeing with each other on the filing date; it may
  resolve on its own once GitHub's docs team updates the reference page,
  which is exactly the pattern already logged for the same reference page
  in issue #3334 (JetBrains `sandbox` key: changelog says supported,
  reference table says not) and issue #2802 (JetBrains `telemetry` key:
  reference table and reference prose disagree with each other).
- **Quote (reference page prose, `telemetry` key subsection)**: "This
  property is supported for Copilot CLI and VS Code."
- **Our assessment**: **Contradicts issue #3682** (filed by this
  extraction). Unlike the JetBrains case in #2802, where the reference
  page's table and its own prose disagreed with *each other*, here the
  table and the prose *agree with each other* — both say the GitHub
  Copilot app does not support `telemetry` — but both disagree with this
  changelog, which is a dedicated, single-purpose announcement of exactly
  that capability, including a "Get started" section that names the
  `telemetry` property and `managed-settings.json` file directly (see
  Concrete Artifacts). This extraction does not pick a winner: it is
  plausible the changelog is accurate and the reference doc simply has not
  caught up yet (the changelog is only two days old as of the reference-doc
  fetch), or that the changelog describes a capability that shipped to a
  subset of users/plans not yet reflected as "Supported" in the general
  reference. See issue #3682 for the full Side A/Side B framing.

## Concrete Artifacts

### Full changelog body (verbatim, GitHub Copilot app changelog, September 22, 2026)

```
Understand how Copilot agents perform and interact with models and tools.
The GitHub Copilot app now supports OpenTelemetry (OTel) configuration
through enterprise-managed settings.
OTel is an open source observability framework. Administrators can use it
to send agent activity data to their organization's compatible monitoring
tools. This helps teams:

- Analyze agent sessions: Follow the flow of a session, including
  requests to AI models and the tools an agent uses.
- Investigate unexpected behavior: Review step-by-step traces of agent
  execution in their existing monitoring tools.
- Manage monitoring centrally: Apply telemetry settings across teams
  instead of requiring each developer to individually configure them.

## Get started

Configure the `telemetry` property in your enterprise's
`managed-settings.json` file to enable export and specify the endpoint
that will receive the data. Prompt and response content is excluded by
default—review your content-capture settings before enabling it.

Learn more about OpenTelemetry for agent monitoring and configuring
enterprise-managed settings.
```

*Source: OpenTelemetry in the GitHub Copilot app, GitHub changelog,
September 22, 2026. Fetched via raw HTML from the `<article>` element, not
an AI-summarized WebFetch pass, to preserve verbatim quoting per MINER.md
§2a.*

### `telemetry` key full schema (verbatim, from the enterprise managed settings reference page — NOT from the changelog itself)

```
"telemetry": {
    "enabled": true,
    "endpoint": "https://otel-collector.example.com",
    "protocol": "http/protobuf",
    "captureContent": false,
    "lockCaptureContent": true,
    "serviceName": "copilot",
    "resourceAttributes": {
      "deployment.environment": "production"
    },
    "headers": {
      "Authorization": "Bearer TOKEN"
    }
  }
```

Sub-property descriptions (verbatim, reference page prose):
```
enabled             — Set to true to turn on telemetry export, or false to turn it off.
endpoint             — The URL of your OTLP collector (for example, https://otel-collector.example.com).
protocol             — The transport protocol for telemetry export. Accepted values are "http/json" and "http/protobuf".
captureContent       — Set to true to include prompt and response content in the telemetry payload, or false to exclude it.
lockCaptureContent   — Set to true to prevent users from changing the captureContent setting.
serviceName          — A label for the telemetry service name (for example, "copilot").
resourceAttributes   — An object of OpenTelemetry resource attributes to attach to all exported telemetry (for example, {"deployment.environment": "production"}).
headers              — An object of HTTP headers to include with each telemetry request (for example, an Authorization header for your collector).
```

*Source: `docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
"telemetry" subsection, fetched as raw HTML 2026-09-24. Included here
because this changelog names only the `telemetry` property, not its
sub-schema — this artifact is the schema detail a practitioner would need
to actually act on the changelog's "Get started" instruction. Note the
support-matrix discrepancy in Claim 6 / issue #3682: this same reference
page's own table and prose say this key is not supported for the GitHub
Copilot app that the changelog announces it for.*

### `telemetry` key "Supported keys" table row (verbatim client support, as fetched 2026-09-24)

```
Key: telemetry
Purpose: Configures OpenTelemetry export, routing Copilot usage data to a
         collector of your choice
Copilot CLI:         Supported
VS Code:              Supported
GitHub Copilot app:   Not supported   <-- contradicts this changelog; see Claim 6 / issue #3682
Copilot cloud agent:  Not supported
JetBrains IDEs:       Supported   (itself contested by reference-page prose; see issue #2802)
```

*Source: `docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
"Supported keys" table, `telemetry` row, icon `aria-label` attributes read
directly from raw HTML SVG markup (`aria-label="Supported"` /
`aria-label="Not supported"`), fetched 2026-09-24.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-open-telemetry-attributes.md` (Claims 1, 4, 10): that source
    documents OpenTelemetry as GitHub Agentic Workflows' standard tracing
    integration, including a secrets-must-not-go-in-telemetry warning
    (Claim 1) that parallels this changelog's default content-exclusion
    stance (Claim 5). Both sources independently confirm GitHub treats
    "exported telemetry" as a distinct trust boundary requiring explicit
    opt-in for sensitive content, across two unrelated product surfaces
    (gh-aw workflows vs. the Copilot app).
  - `docs-github-copilot-jetbrains-otel-model-management-july2026.md`
    (Claim 1) and `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
    (Claim 4): both confirm OpenTelemetry as a recurring, actively-expanding
    observability integration point across Copilot's IDE/client surfaces.
    This changelog extends that pattern to a client (the GitHub Copilot
    app) that had no prior corpus documentation of any OTel capability.

- **Contradicts**: **Issue #3682** (filed by this extraction). This
  changelog's central claim — that the GitHub Copilot app now supports the
  `telemetry` property in `managed-settings.json` — directly opposes the
  live "Enterprise managed settings reference" page's own support table and
  prose, both of which mark `telemetry` as "Not supported" for the GitHub
  Copilot app as of two days after this changelog's publication (Claim 6).
  No verdict is picked here; see issue #3682 for the full Side A/Side B
  framing and CONTRADICTIONS.md once resolved. This is the same
  changelog-vs-reference-doc lag pattern already logged for the same
  reference page in issue #3334 (JetBrains `sandbox` key) and issue #2802
  (JetBrains `telemetry` key, a table-vs-prose self-contradiction rather
  than a changelog-vs-doc one).

- **Extends**:
  - `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`:
    that note's Concrete Artifacts section listed the Aug 18, 2026 snapshot
    of the `telemetry` row as `CLI=Y, VSCode=Y, Copilot app=N, cloud
    agent=N, JetBrains=Y`. This changelog, dated a month later, is GitHub
    announcing a change to exactly the "Copilot app=N" cell that note
    recorded — but as of this extraction's fetch, the live reference table
    still shows "N" for that cell (Claim 6). A future source or Assayer
    re-check should verify whether the reference page has been updated to
    "Y" by the time this contradiction is resolved.
  - `docs-github-copilot-usage-metrics-server-side-telemetry.md` and
    `docs-github-copilot-app-usage-metrics-report-rollups.md`: both
    document a separate, pre-existing telemetry pipeline for the Copilot
    app — aggregate/per-user usage-metrics reporting via the REST API, not
    OTel trace/span export. This changelog adds a second, independent
    telemetry pipeline (OTel export to an admin-configured OTLP collector)
    for the same client. The guide should distinguish these explicitly:
    usage-metrics reporting answers "how many users, how much activity,"
    while OTel export answers "what did this specific session actually do,
    step by step."

- **Novel**:
  - **OpenTelemetry export as a GitHub Copilot app capability**: no prior
    corpus source documents any OTel integration for this specific client
    (as opposed to JetBrains, VS Code/CLI, or the gh-aw workflow/gateway
    layer).
  - **Edit-feedback as an OTel event example**: the linked concept doc's
    example of an "edit feedback event" recording whether a user
    accepted/rejected an agent edit is the first corpus mention of
    accept/reject signal being framed as OTel event data specifically
    (distinct from its prior framing purely as usage-metrics/outcome data).
  - **A dated, filed contradiction between a changelog and the live
    reference-doc support matrix for this exact key/client pair** (Claim 6,
    issue #3682): novel as a specific instance, though it fits an
    already-recurring pattern (issues #3334, #2802) for this same
    reference page.

## Guide Impact

- **Chapter 02 (Harness Engineering — Observability)**: Add the GitHub
  Copilot app to the guide's inventory of Copilot clients with
  enterprise-managed OTel export, alongside VS Code/CLI and JetBrains —
  but explicitly flag the currency caveat from issue #3682: as of this
  extraction, the platform's own reference doc does not yet confirm this
  client in its support matrix, so the guide should hedge ("GitHub
  announced this capability on Sept 22, 2026; verify current support status
  against the live reference doc before citing as settled") rather than
  state it as a confirmed, schema-verified capability the way JetBrains VS
  Code/CLI support can be stated.

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**: Add the
  full `telemetry` sub-property schema (`enabled`, `endpoint`, `protocol`,
  `captureContent`, `lockCaptureContent`, `serviceName`,
  `resourceAttributes`, `headers`) to the guide's `managed-settings.json`
  reference material, since this changelog names only the top-level
  property and the schema detail comes from the separately-fetched
  reference page (see Concrete Artifacts).

- **Chapter 02/07 (Observability — Data Governance)**: Add the
  default-excludes-prompts-and-responses stance (Claim 5) and the
  `lockCaptureContent` administrator-lock mechanism as a specific,
  actionable governance recommendation: enterprises exporting Copilot app
  telemetry to a third-party OTLP collector should leave `captureContent`
  false and set `lockCaptureContent: true` unless there is a specific,
  reviewed reason to capture prompt/response content, given that content
  is "not treated as secret" once exported (per the parallel warning in
  `docs-ghaw-open-telemetry-attributes.md` Claim 1).

## Extraction Notes

1. **WebFetch returned an AI-summarized version first**: An initial
   WebFetch call against the changelog URL returned a plausible-looking but
   summarized rendering. Per MINER.md §2a, this extraction instead fetched
   the raw HTML directly via `curl`, isolated the `<article>` element, and
   read the verbatim body text before writing any Quote field. All quotes
   in Claims 1-3 and 5 (changelog side) and the Concrete Artifacts
   changelog block were copied from that raw-HTML extraction, not the
   WebFetch summary.
2. **Two linked pages followed, one non-linked page fetched for
   cross-checking**: Per MINER.md §1, the two pages the changelog itself
   links ("OpenTelemetry for agent monitoring" and "Getting started with
   enterprise-managed settings") were both fetched as raw HTML and used for
   Claims 4-5 and the deployment-mechanics context in Source Context. A
   third page — the "Enterprise managed settings reference" — was not
   linked from this changelog, but was fetched because it is the page this
   corpus already relies on for the `telemetry` key's full schema and
   per-client support matrix (via the JetBrains notes). Cross-checking it
   against this changelog is what surfaced the contradiction in Claim 6.
3. **Contradiction filed before this note, per MINER.md §4a**: Issue #3682
   was filed prior to writing this note, once the reference-page fetch
   confirmed the "GitHub Copilot app: Not supported" table cell and the
   matching prose sentence. This note does not pick a verdict — see Claim 6
   and Cross-References → Contradicts.
4. **`confidence_overall` set to emerging, not settled**: Although each
   individual claim about what the changelog *says* is settled (verbatim,
   first-party text), the central capability the source announces is
   actively contradicted by the platform's own live reference
   documentation as of the extraction date (Claim 6). Rating the note
   `emerging` overall reflects that the underlying product fact — does the
   GitHub Copilot app actually support `telemetry` today — is not yet
   settled across GitHub's own properties, even though the changelog's
   wording itself is unambiguous.
5. **No sample OTel trace/span JSON or attribute names in this source**:
   Unlike `docs-ghaw-open-telemetry-attributes.md`, neither the changelog
   nor its two linked pages provide any concrete span/trace/attribute
   schema for what the GitHub Copilot app actually emits — only the
   three-way trace/metric/event taxonomy (Claim 4) and the
   `managed-settings.json` configuration schema (Concrete Artifacts, from
   the third, non-linked reference page). A future source documenting the
   Copilot app's actual OTel attribute names (analogous to the gh-aw
   attribute reference) would close this gap.
6. **Two prior triage comments on the source issue**: The Prospector left
   two independent triage comments on issue #3656 (both rating novelty
   "high"), one emphasizing enterprise governance/Ch02, the other
   emphasizing the client-side-instrumentation angle relative to the gh-aw
   server-side OTel reference. Both angles are reflected in this note's
   Guide Impact section.
