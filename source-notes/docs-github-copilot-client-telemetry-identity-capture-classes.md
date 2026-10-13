---
source_url: https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture
source_type: docs
title: "Client telemetry user attribution and configurable capture"
author: GitHub (official changelog; no byline shown)
date_published: 2026-10-12
date_extracted: 2026-10-13
last_checked: 2026-10-13
status: current
confidence_overall: emerging
issue: "#4080"
---

# Client telemetry user attribution and configurable capture

> GitHub's Oct 12, 2026 changelog splits the managed-settings `telemetry` content-capture switch into an opt-in identity setting (`telemetry.capture.identity`) plus five independently controlled content classes, all default-off, so enterprises can attribute Copilot activity to a user without collecting prompts or tool content.

## Source Context

- **Type**: docs (GitHub official changelog, label "Improvement", ~1 minute read, tagged `client apps`, `copilot`, `enterprise management tools`). One linked page was followed per MINER.md §1: the "Enterprise managed settings reference" (`docs.github.com/en/copilot/reference/enterprise-managed-settings-reference`), which carries the schema detail the changelog omits. The second link (VS Code "monitor agent usage with OpenTelemetry") was not fetched.
- **Author credibility**: First-party product team announcing a shipped feature; authoritative for setting names, defaults and precedence. Short (~200 words), no schema, examples or rollout/GA label.
- **Scope**: Identity attributes, five capture classes, defaults, precedence, legacy `captureContent` relationship, and a security warning. Does NOT cover endpoint/protocol schema, per-surface support matrix, or retention/privacy-law implications of attributing activity to named users.

## Extracted Claims

### Claim 1: `telemetry.capture.identity` lets enterprise admins attribute Copilot activity to a user without collecting prompts, responses, or tool content
- **Evidence**: Official changelog; the reference page gives a minimal config that does exactly this.
- **Confidence**: emerging (single vendor announcement, corroborated by vendor reference page)
- **Quote**: "Enterprise administrators can now use"  … "in managed settings to attribute GitHub Copilot activity to a user without collecting their prompts, responses, or tool content."
- **Our assessment**: Real new capability: attribution is decoupled from content capture, which removes the main reason audit teams previously had to turn on content capture. Quote note: the `telemetry` code span falls between the two fragments in the page rendering; both fragments are verbatim.

### Claim 2: Identity capture adds three OTel attributes: `user.name`, `process.user.name`, `host.name`
- **Evidence**: Changelog list; reference page repeats it and adds that it does not affect the pseudonymous `enduser.pseudo.id` attribute.
- **Confidence**: emerging
- **Quote**: "The authenticated Copilot account name, currently the GitHub login."
- **Our assessment**: `user.name` is the Copilot (GitHub) login, `process.user.name` the local OS account, `host.name` the machine name. This is personally identifying telemetry, so enabling it likely triggers employee-monitoring/works-council/privacy review that the changelog does not mention.

### Claim 3: Identity capture is off by default and separate from the existing pseudonymous user identifier
- **Evidence**: Changelog statement.
- **Confidence**: emerging
- **Quote**: "Identity capture is off by default and remains separate from the existing pseudonymous user identifier."
- **Our assessment**: Implies pseudonymous per-user telemetry already existed (`enduser.pseudo.id` per the reference page), so admins get usage-per-person analytics without names unless they opt in.

### Claim 4: Five content classes (`prompts`, `responses`, `toolArguments`, `toolOutput`, `policyDetail`) are independently controllable, and every capture class is off by default
- **Evidence**: Changelog definitions; reference page gives longer definitions (e.g. prompts include attachments, compaction summaries, skill content, workspace context; policyDetail is "unbounded policy details", with bounded posture/counts/outcomes still emitted when false).
- **Confidence**: emerging
- **Quote**: "Every capture class is off by default."
- **Our assessment**: Granularity matters: an org can capture `toolArguments` (commands) for security audit while never capturing `prompts`/`responses`. Note `toolArguments` also covers "identifiers for tools, MCP servers, plugins, and hooks", so it doubles as an inventory of what agents actually used.

### Claim 5: Explicit managed values take precedence over local settings, SDK configuration, and environment variables
- **Evidence**: Changelog; reference page repeats and adds that if multiple managed sources define `telemetry`, the highest-precedence source supplies the complete object with no merging.
- **Confidence**: emerging
- **Quote**: "Explicit managed values take precedence over local settings, SDK configuration, and environment variables."
- **Our assessment**: Developers cannot override via env vars (e.g. OTel env vars) once managed. The no-merge rule (reference page only) is a gotcha for admins layering MDM/server/file sources; compare precedence order in the JetBrains managed-settings note, Claim 8.

### Claim 6: Legacy `captureContent` remains as shorthand for the five content classes and never enables identity
- **Evidence**: Changelog; reference page adds that an explicitly configured `capture` sub-property wins over `captureContent` for that class, and `lockCaptureContent` does not govern identity.
- **Confidence**: emerging
- **Quote**: "The existing"  … "setting remains available as a legacy shorthand for the five content classes, but it never enables identity."
- **Our assessment**: Existing configs keep working and cannot silently begin collecting identity. Both previously noted notes describe `captureContent` as a single boolean; that is now incomplete (see Cross-References).

### Claim 7: Prompt, tool, and policy capture can include sensitive material; enable only needed classes and send to an approved endpoint
- **Evidence**: Changelog warning; reference page "Warning" is similar and adds MCP identifiers and "paths to workspaces, user profiles, or files that may contain secrets".
- **Confidence**: settled (vendor's own explicit warning)
- **Quote**: "Prompt, tool, and policy capture can include source code, file contents, commands, tool results, and workspace or user-profile paths."
- **Our assessment**: Sound least-privilege guidance. Tool output and commands in particular can contain secrets the agent read; the OTel collector becomes a sensitive data store needing its own access control and retention.

### Claim 8: Fine-grained capture controls apply in Copilot CLI, the GitHub Copilot app, and VS Code sessions using Agent Host
- **Evidence**: Changelog; reference page qualifies it for VS Code.
- **Confidence**: emerging
- **Quote**: "Fine-grained capture controls are available in Copilot CLI, the GitHub Copilot app, and VS Code sessions using Agent Host."
- **Our assessment**: Reference page adds: "VS Code's local agent harness supports capture.identity and the legacy captureContent setting, but does not independently apply prompts, responses, toolArguments, toolOutput, or policyDetail." So a VS Code deployment outside Agent Host gets only identity and the all-or-nothing shorthand. JetBrains and cloud agent are not listed.

## Concrete Artifacts

Minimal identity-only config (from the Enterprise managed settings reference page, "Capture controls"; fetched 2026-10-13):

```json
{ "telemetry" : { "capture" : { "identity" : true } } }
```

Reference-page description of the sub-properties (paraphrased structure, names verbatim): `enabled`, `endpoint`, `protocol` (`"http/json"` | `"http/protobuf"`), `capture` (`identity`, `prompts`, `responses`, `toolArguments`, `toolOutput`, `policyDetail`), `captureContent` (legacy), `lockCaptureContent`, `serviceName`, `resourceAttributes`, `headers`.

## Cross-References

- **Corroborates**: `docs-github-copilot-app-opentelemetry.md` Claim 5 (content excluded by default, opt-in with sensitivity warning); this entry keeps that default and extends it per class.
- **Contradicts**: No new contradiction filed. Open issues #3682 (does `telemetry` support the GitHub Copilot app) and #2802 (JetBrains) concern the support matrix. This changelog names the GitHub Copilot app as supporting fine-grained capture, and the reference page's `telemetry` prose points to the support table, so it adds weight to the "supported for the app" side of #3682, but the table's per-client marks are not legible in text extraction, so it does NOT resolve either issue. JetBrains is not mentioned here, so #2802 is unaffected. A mild internal tension (changelog says VS Code "Agent Host" sessions; reference limits the local VS Code harness) is a conditioning variable, not a contradiction.
- **Extends**: `docs-github-copilot-app-opentelemetry.md` (Claims 1 and 5; its `captureContent`/`lockCaptureContent` description is now the legacy shorthand layered over per-class controls); `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md` Claim 4 (content-capture policy) and Claim 8 (precedence among managed sources).
- **Novel**: Identity attributes (`user.name`, `process.user.name`, `host.name`); five named capture classes; the rule that `captureContent` never enables identity; no-merge across managed sources (reference page).

## Guide Impact

- **Chapter 05**: Where managed-settings telemetry is discussed, recommend identity-only attribution (`capture.identity: true`) for per-person adoption/audit measurement, with content classes left off; flag privacy/HR review before enabling named attribution.
- **Chapter 06**: Add a threat-model note that `toolArguments`/`toolOutput`/`prompts` telemetry can carry secrets and source; treat the collector as sensitive storage, enable per class, approved endpoint only.
- **Chapter 02**: When listing managed settings as a harness control surface, update the `telemetry` description from single `captureContent` boolean to per-class `capture` object, noting managed-over-env-var precedence.

## Extraction Notes

- Fetched raw HTML of the changelog (curl) to obtain verbatim text; WebFetch alone returns summaries. Quotes were copied from that text; quotes with an inline code span elided (`telemetry`, `captureContent`) are given as separate fragments.
- Reference-page content is cited as secondary and was read on 2026-10-13; it may change.
- Triage comments suggested checking whether #3682/#2802 are resolved; answer above: not resolved.
- The linked VS Code OpenTelemetry guide was not followed.
