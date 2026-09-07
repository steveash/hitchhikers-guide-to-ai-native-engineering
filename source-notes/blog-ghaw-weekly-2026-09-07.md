---
source_url: https://github.github.com/gh-aw/blog/2026-09-07-weekly-update/
source_type: blog-post
title: "Weekly Update – September 7, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-09-07
date_extracted: 2026-09-07
last_checked: 2026-09-07
status: current
confidence_overall: emerging
issue: "#3290"
---

# Weekly Update – September 7, 2026 (GitHub Agentic Workflows)

> v0.88.4 adds a new `trusted` enclave sensitivity level and fixes a DIFC
> policy-generation gap for GitHub App workflows, plus four other named bug
> fixes; the week's merge queue separately completed a 71-workflow migration
> off `gvisor`/`docker-sbx` onto Cloud Hypervisor, wired a dynamic enclave
> delegation controller that fails closed pending an unreleased mcpg
> release, and shipped a new `enclaves[].dynamic` repository-selector mode
> that extends the static, enumerated-`repos` enclave model already
> documented in `docs-ghaw-enclaves.md`.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; a short intro, a "Release: v0.88.4" section with
  "What's New" (4 bullets) and "Bug Fixes & Improvements" (4 bullets)
  subsections, a "Notable Pull Requests" section of five bullets, an "Agent
  of the Week: dead-code-remover" spotlight, and a "Try It Out" closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The on-page byline names the
  author as "Copilot" — the same non-human byline pattern documented in
  every prior weekly note in this corpus (e.g. `blog-ghaw-weekly-2026-08-24.md`).
  Every PR named in the post was independently fetched via `gh pr view
  <N> --repo github/gh-aw --json title,body,url` to corroborate the blog's
  one-line summaries against first-party PR descriptions — see Extraction
  Notes for the full list.
- **Scope**: One "Release: v0.88.4" section naming eight PRs (four "What's
  New," four "Bug Fixes & Improvements"), one "Notable Pull Requests"
  section naming seven more PRs (four named infrastructure PRs plus three
  workflow model-configuration fixes), and one "Agent of the Week"
  spotlight on `dead-code-remover` naming two additional PRs. Does NOT
  cover: a full changelog/release-notes page for v0.88.4 (no such page is
  linked; "Release Highlights" links directly to PRs, as in
  `blog-ghaw-weekly-2026-08-24.md`); the exact mcpg wire-protocol contract
  for dynamic enclave delegation (explicitly deferred by PR #59046 itself
  to "an unreleased compatible release"); or any of the individual 71
  workflow-configuration diffs behind the Cloud Hypervisor migration PR
  (#58726), which reports only aggregate counts.

## Extracted Claims

### Claim 1: v0.88.4 is framed as focused on three areas — hardening the agentic firewall/network layer, improving CI reliability, and expanding project tooling support
- **Evidence**: Opening intro paragraph and the "Release: v0.88.4" section's lead sentence.
- **Confidence**: settled (first-party framing of the release's own scope)
- **Quote**: "Another busy week for github/gh-aw! The team shipped a new release focused on hardening the agentic firewall and CI reliability, while dozens of pull requests tightened up sandboxing, model configuration, and safe-output handling across the fleet of agentic workflows." / "v0.88.4 landed this week, focused on hardening the agentic firewall/network layer, improving CI reliability, and expanding project tooling support."
- **Our assessment**: This is scene-setting framing, not itself a technical claim — the substance is in Claims 2–15 below. Note the framing names "CI reliability" as a headline focus, but none of the eight named Release-section PRs is a CI-pipeline fix specifically; the CI-reliability thread is carried instead by the Notable-PR-section model-configuration fixes (Claim 12) and the OTLP/PATH fixes (Claims 6–7), which are operational/tooling reliability fixes rather than CI-pipeline changes per se.

### Claim 2: PR #58328 adds a new `trusted` enclave sensitivity level that is unmetered and permits free-form string output only within strict structured response schemas, distinct from other sensitivities which remain finite-schema-only; it requires AWF `v0.28.13+` and treats trusted repositories as public-equivalent for `issues-read-v1` limits
- **Evidence**: PR #58328 description ("Add trusted enclave sensitivity support"), fetched via `gh pr view 58328 --repo github/gh-aw`. The blog post's own one-line summary is thinner: "adds finer-grained sensitivity controls for trusted enclave workflows."
- **Confidence**: settled (specific PR, specific new enum value, first-party description of validation and version-gating behavior)
- **Quote**: "Adds compiler and authoring support for AWF's `trusted` enclave sensitivity, which is unmetered and permits free-form strings only within strict structured response schemas. Other sensitivities remain finite-schema-only." / "Require AWF `v0.28.13+` for trusted repositories." / "Treat trusted repositories as public-equivalent for `issues-read-v1` limits."
- **Our assessment**: `docs-ghaw-enclaves.md` Claims 1, 3, 7, and 9 document exactly two sensitivity values in the enclave model — `confidential` (used in every configuration example in that note) and `public` (the ceiling `issues-read-v1` imposes on any repository beyond the first non-public one). This PR adds a third, named value, `trusted`, that sits in a different position in the model entirely: rather than gating *how much* is disclosed, it changes *what shape* of output is permitted (unmetered free-form strings inside a strict schema, vs. the implied metered/finite-schema constraint on `confidential`/`public` enclaves). This is new to the corpus — no existing note documents a sensitivity level that trades output-shape freedom for being "unmetered." The `v0.28.13+` version requirement is also new information: it is higher than the `v0.28.9` AWF floor `docs-ghaw-enclaves.md` Claim 12 recorded for the `issues-read-v1` profile, meaning the version floor for enclave features keeps climbing release over release. For Ch06 (Security and Threat Model): document `trusted` as a third enclave sensitivity tier with different output-shape rules, not merely a relabeling of `confidential`/`public`.

### Claim 3: PR #58302 fixes a bug where GitHub App authentication could suppress automatic DIFC guard-policy generation, leaving a guarded GitHub MCP source paired with an unguarded/noop `safeoutputs` sink — causing safe-output writes (dispatch, noop, incomplete reports) to be silently denied while the workflow still reported success
- **Evidence**: PR #58302 description ("Generate DIFC policies for GitHub App workflows"), fetched via `gh pr view 58302 --repo github/gh-aw`. The blog's own summary states only the fix's effect, not the bug: "automatically generates data-flow integrity/confidentiality policies for workflows authenticated via a GitHub App."
- **Confidence**: settled (first-party bug description with a stated failure mode and fix scope, plus an example of the corrected generated policy shape)
- **Quote**: "GitHub App authentication could suppress automatic DIFC policy generation, leaving guarded GitHub MCP sources paired with an unguarded/noop `safeoutputs` sink. That caused safe-output writes such as dispatch, noop, and incomplete reports to be denied while the workflow appeared successful." / "Generate automatic GitHub `allow-only` guard policies whenever no explicit policy is configured, including GitHub App workflows." / "GitHub App token minting and MCP authentication remain unchanged. Only DIFC source/sink policy generation changes."
- **Our assessment**: This directly extends the DIFC terminology and mechanism documented in `docs-ghaw-integrity-reference.md` Claim 2 (DIFC = Decentralized Information Flow Control; the MCP gateway logs filtered items as `DIFC_FILTERED` events) and `docs-ghaw-enclaves.md` Claim 9 (the `private:<owner>/<repo>` DIFC secrecy label) — this is the first corpus documentation of DIFC guard-policy *generation* being conditional on the authentication method used, and of a specific failure mode (a workflow reporting success while its safe outputs are silently denied by a mismatched source/sink guard pairing). "The workflow appeared successful" while writes were silently denied is a concrete instance of the "agent run completes without honestly reflecting what happened" failure class already tracked in `blog-ghaw-weekly-2026-08-24.md` Cross-References → Extends (there applied to the Aider engine and Copilot SDK startup crashes; here applied to DIFC policy generation itself). For Ch06 (Security and Threat Model): note that DIFC guard-policy coverage is authentication-method-dependent and that a coverage gap here does not surface as an error — it surfaces as denied safe-output writes with an otherwise-green run, which is a debugging trap for anyone relying on run status alone.

### Claim 4: PR #58267 makes `gh aw add` discover and deep-merge package-level `.github/workflows/aw.json` project settings into the target repository's `aw.json`, with added-package values taking precedence on conflicting scalars/arrays while preserving target-only settings
- **Evidence**: PR #58267 description ("Add aw.json project support to the add command"), fetched via `gh pr view 58267 --repo github/gh-aw`, including a worked before/after merge example.
- **Confidence**: settled (specific PR, first-party description of merge semantics with a concrete JSON example)
- **Quote**: "Package-level `.github/workflows/aw.json` settings were ignored by `gh aw add`. This change discovers and merges them into the target repository, with added package values taking precedence." / "Deep-merge nested objects while preserving unspecified target settings. Replace conflicting scalar and array values with package values. Validate the merged configuration before writing."
- **Our assessment**: This is the first corpus documentation of `aw.json` project-settings merge semantics specifically for the `add` command's package-import path. The worked example (target `{"utc":"-08:00","maintenance":{"runs_on":"self-hosted"}}` merged with package `{"utc":"+01:00","maintenance":{"label_triggers":true}}` yielding `{"utc":"+01:00","maintenance":{"runs_on":"self-hosted","label_triggers":true}}`) shows the merge is field-level for nested objects (deep-merge) but whole-value-replacing for scalars and arrays — a practitioner importing a package that sets `utc` will silently have their own `utc` setting overwritten, which is a concrete gotcha worth flagging. For Ch02 (Harness Engineering): document this deep-merge-nested/replace-scalar behavior explicitly when covering `gh aw add` package imports, since the precedence rule (package wins on conflicts) is not the only intuitive choice a practitioner might assume.

### Claim 5: PR #58320 adds a daily scheduled smoke-test workflow that creates matching haiku-generation issues in a named Linear project and a named Jira project through safe outputs, and fixes secret redaction so Linear API keys (`lin_api_...` format) are stripped from uploaded artifacts
- **Evidence**: PR #58320 description ("Add daily Linear and Jira smoke issues workflow"), fetched via `gh pr view 58320 --repo github/gh-aw`, including a YAML safe-output config snippet.
- **Confidence**: settled (specific PR, concrete workflow behavior, named project identifiers, named secret-redaction fix)
- **Quote**: "Adds a daily smoke workflow that generates a haiku and creates issues in the configured Linear and Jira projects through safe outputs. Linear API keys using the `lin_api_...` format are now redacted." / "Creates matching issues in Linear project `810f57a7e383` and Jira project `KAN`. Includes the workflow run URL in each issue."
- **Our assessment**: This bundles two distinct changes under one PR: a new integration-health smoke test (scheduled daily, cross-posting to two external issue trackers to verify the integrations still work end to end) and an unrelated but security-relevant secret-redaction fix (`lin_api_` keys previously could leak into uploaded artifacts). The smoke-test pattern — deliberately generating low-stakes synthetic content (a haiku) on a fixed daily schedule purely to exercise an integration path — is a concrete, named example of a "canary" or synthetic-monitoring pattern for third-party integrations, distinct from the corpus's existing user-facing safe-output examples. For Ch06 (Agentic Operations): add scheduled synthetic-content smoke tests as a pattern for verifying third-party integration health (Linear, Jira, or similar) independent of real workflow traffic.

### Claim 6: PR #58313 fixes Pi routing Anthropic models through OpenAI Chat Completions (producing invalid upstream paths and disabling prompt caching) by configuring firewall-backed Anthropic models to use native `anthropic-messages` routing to `/v1/messages`, and adds failure-propagation so an all-requests-failed inference session emits `report_incomplete` and exits nonzero instead of exiting successfully with no useful output
- **Evidence**: PR #58313 description ("Fix Pi Anthropic routing through the firewall"), fetched via `gh pr view 58313 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description with the exact prior failure mode and the fix's two independent halves — routing and failure-reporting)
- **Quote**: "Pi routed Anthropic models through OpenAI Chat Completions, producing invalid upstream paths and disabling prompt caching. Failed inference-only sessions could then exit successfully without reporting useful output." / "Configure firewall-backed Anthropic models with `anthropic-messages`. Target `/v1/messages`, restoring native prompt-cache accounting." / "Emit `report_incomplete` through the trusted safe-outputs CLI and exit nonzero when every request fails."
- **Our assessment**: This is a second, distinct instance of the "silently-successful-but-empty run" failure class already tracked in the corpus (`blog-ghaw-weekly-2026-08-17.md` Claim 9's Aider engine silently producing zero safe outputs, and `blog-ghaw-weekly-2026-08-24.md` Claim 5's Copilot SDK pre-ready crashes previously reporting only a bare exit signal) — here the mechanism is a wrong upstream API path for Anthropic models under the `pi` engine, which silently disabled prompt caching (a cost/latency regression, not just a correctness one) on top of the failure-reporting gap. The fix's `report_incomplete` + nonzero-exit behavior is a concrete, citable pattern for "when every request fails, fail loudly rather than exiting clean" — worth generalizing beyond this specific engine/provider pairing. For Ch06 (Agentic Operations): add "inference sessions that fail every request must emit an incomplete/failure signal and exit nonzero" as a general engine-reliability requirement, citing this fix alongside the two prior instances of the same failure class.

### Claim 7: PR #58312 fixes reusable-workflow OTLP telemetry export so endpoints with empty `Authorization` or `x-sentry-auth` headers are excluded (falling back to the next usable endpoint, or clearing exporter variables entirely if none remain), while endpoints intentionally configured with no authorization header are preserved
- **Evidence**: PR #58312 description ("Disable OTLP export when authorization secrets are empty"), fetched via `gh pr view 58312 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description with the exact failure condition — reusable workflows receiving empty OTLP secrets — and the fix's endpoint-filtering logic)
- **Quote**: "Reusable workflows may receive empty OTLP authorization secrets, causing telemetry exporters to target protected endpoints without credentials." / "Exclude endpoints with empty `Authorization` or `x-sentry-auth` headers. Preserve endpoints that intentionally use no authorization header." / "Promote the next usable endpoint when one is unavailable. Clear OTLP exporter variables when no usable endpoint remains."
- **Our assessment**: This is a narrow but concrete observability-plumbing fix specific to reusable-workflow secret propagation — a reusable workflow caller that doesn't pass through an OTLP secret would previously have caused noisy failed export attempts against an authenticated endpoint with no credentials, rather than silently (and correctly) skipping export. This is new to the corpus and distinct from the engine-level silent-failure class in Claim 6 — it's a telemetry-pipeline hygiene fix, not an agent-run correctness fix. For Ch06 (Agentic Operations): note this as a specific gotcha for teams wiring OTLP export through reusable workflow calls — an empty (not absent) secret value is the failure trigger, which is easy to produce accidentally via a reusable-workflow `secrets: inherit` misconfiguration.

### Claim 8: PR #58311 fixes `GetNpmBinPathSetup` prepending every cached runtime `bin` directory ahead of the host PATH (letting an older cached Ruby override the version `ruby/setup-ruby` selected) by appending discovered tool-cache directories after the existing host PATH instead, while explicitly retaining `GOROOT/bin` and `ERLANG_HOME/bin` precedence
- **Evidence**: PR #58311 description ("Preserve setup-ruby PATH precedence inside AWF"), fetched via `gh pr view 58311 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description naming the exact function, the exact override condition, and the fix's precedence rule, including named exceptions)
- **Quote**: "`GetNpmBinPathSetup` prepended every cached runtime `bin` directory, allowing an older cached Ruby to override the version selected by `ruby/setup-ruby`." / "Append discovered tool-cache directories after the existing host PATH. Retain explicit `GOROOT/bin` and `ERLANG_HOME/bin` precedence. Avoid introducing an empty PATH entry when no cached bins exist."
- **Our assessment**: This is a narrow PATH-ordering bug inside the Agentic Workflow Firewall's environment setup, notable mainly because it shows AWF's PATH construction treats different language toolchains inconsistently on purpose (Go and Erlang explicitly keep prepended/high precedence; npm-managed tool-cache bins are moved to append-only) rather than applying one uniform rule — a practitioner debugging "why is the wrong Ruby version running inside my AWF sandbox" would need to know this asymmetry exists. For Ch06: minor but concrete — cite as an example of an isolation-layer PATH-construction bug that could silently select the wrong toolchain version inside a sandboxed run.

### Claim 9: PR #58726 migrated 71 repository-managed agentic workflow runtime configurations off `docker-sbx`/`gvisor` onto Cloud Hypervisor, regenerating their lock files, replacing incompatible `gh-proxy` usage with local GitHub MCP access, migrating incompatible Pi and Crush-engine workflows to supported engines, and moving one self-hosted workflow to a GitHub-hosted runner required by Cloud Hypervisor — except `ci-doctor.md`, left unchanged because it is upstream-managed
- **Evidence**: PR #58726 description ("Migrate agentic workflows to Cloud Hypervisor"), fetched via `gh pr view 58726 --repo github/gh-aw`. The blog's own summary is one sentence: "a major infrastructure shift moving the workflow fleet onto Cloud Hypervisor-based microVMs for better isolation."
- **Confidence**: settled (specific PR, specific counts — 71 workflows — and a specific, named exclusion with a stated reason)
- **Quote**: "Migrates repository-managed agentic workflows from Docker sbx and gVisor to Cloud Hypervisor." / "Updated 71 workflow runtime configurations and regenerated their lock files. Replaced incompatible `gh-proxy` usage with local GitHub MCP access. Migrated incompatible Pi and Crush workflows to supported engines. Moved a self-hosted workflow to a GitHub-hosted runner required by Cloud Hypervisor." / "`ci-doctor.md` remains unchanged because it is upstream-managed and must be migrated at its source."
- **Our assessment**: This is gh-aw's own fleet migration executing the deprecation `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 1 announced two days earlier (2026-09-05) and Claims 6–7 gave migration guidance for — i.e., this PR is the platform team dogfooding its own migration instructions three concrete ways beyond the published guidance: (1) `gh-proxy` usage had to be replaced with local GitHub MCP access because it is *incompatible* with Cloud Hypervisor (a compatibility constraint not stated in the announcement post at all), (2) Pi and Crush-engine workflows also needed migration to "supported engines" (implying Cloud Hypervisor doesn't support every engine `docker-sbx`/`gvisor` did), and (3) at least one self-hosted-runner workflow had to move to GitHub-hosted, confirming this note's own inference in `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 5's "Our assessment" that Cloud Hypervisor "could mean... GitHub-hosted-runner-only." The `ci-doctor.md` carve-out (upstream-managed, must migrate at its source) is a concrete instance of a fleet migration being blocked by a workflow's own provenance, worth noting as an operational constraint for any large-scale runtime migration. For Ch04 (Safety and Constraints): update the Cloud Hypervisor migration guidance to include these three previously-undocumented compatibility constraints (gh-proxy incompatibility, engine restrictions, GitHub-hosted-runner requirement) sourced from the platform's own migration experience, not just the announcement post.

### Claim 10: PR #59046 fixes dynamic GitHub enclave delegation, which was completely non-functional because mcpg v0.4.16 rejects the provisional stdin config format the compiler emitted, by replacing it with an atomic env-var bootstrap (`MCP_GATEWAY_DELEGATION_ENVELOPE` and related vars) for mcpg's `github-repository-delegation-v1` controller, adding a `127.0.0.1`-only private control endpoint distinct from and excluded from the primary agent's environment, and fixing a gap where the GitHub MCP backend stayed in the primary agent's unrestricted routable server list whenever any dynamic enclave was configured even without top-level `tools.github`
- **Evidence**: PR #59046 description ("Wire dynamic enclave delegation controller into the workflow runtime"), fetched via `gh pr view 59046 --repo github/gh-aw`, including a YAML example of the primary-agent isolation fix.
- **Confidence**: settled for the bug and the fix mechanism (first-party, highly specific — named types, named env vars, named port-derivation rule); emerging for real-world availability, since the PR itself states the compatible mcpg release does not exist yet (see Claim 11)
- **Quote**: "mcpg v0.4.16 rejects the provisional `gateway.delegationControllers` stdin config the compiler emitted for dynamic GitHub enclaves, so AWF never received a control endpoint and dynamic policies were always rejected at runtime." / "Found and fixed a gap where the GitHub MCP backend stayed in the primary agent's unrestricted routable server list whenever a dynamic enclave was configured, even without top-level `tools.github`. The backend stays registered for delegated identities, but the primary agent no longer gets implicit GitHub tool access." / "Control port is derived from the job's data-plane gateway port (`port+10`) rather than a fixed literal, avoiding collisions on self-hosted runners running concurrent jobs."
- **Our assessment**: The primary-agent isolation gap this PR fixes is architecturally significant and directly extends `docs-ghaw-enclaves.md` Claim 10's credential-isolation architecture (PAT, mcpg address, root key, container identity, CA path, and repository catalog all withheld from both primary agent and enclave): here, the bug meant a *tool-routing* boundary (not a credential) leaked — the primary agent could reach the GitHub MCP backend registered for a dynamic enclave's delegated identity, even with no `tools.github` configured for the primary agent at all. This is a distinct isolation-failure class from the credential-exposure risks `docs-ghaw-enclaves.md` documents defenses against — it's an *access-routing* leak rather than a *secret* leak, and it was found and fixed by the same team building the feature, before (per Claim 11) the feature is even usable end to end. For Ch06 (Security and Threat Model): add this as a concrete example that enclave isolation has multiple independent failure surfaces (credentials, per `docs-ghaw-enclaves.md`; and tool-routing/backend registration, per this PR) that must each be independently verified, not assumed to be covered by a single isolation guarantee.

### Claim 11: PR #59046 explicitly leaves "exact mcpg wire-protocol validation against the unreleased compatible release" out of scope and bumps `MCPGDynamicRepositoryDelegationMinVersion` above `DefaultMCPGatewayVersion` so that dynamic enclave setup fails closed until a real post-mcpg-delegation-contract release is pinned
- **Evidence**: PR #59046 description, "Version gating" and "Out of scope" sections.
- **Confidence**: settled (first-party, explicit statement that the feature is gated to fail closed pending an unreleased dependency)
- **Quote**: "Bumped `MCPGDynamicRepositoryDelegationMinVersion` above `DefaultMCPGatewayVersion` so dynamic enclave setup fails closed until a real post-mcpg-delegation-contract release is pinned." / "Exact mcpg wire-protocol validation against the unreleased compatible release, raising `AWFDynamicRepositoryEnclaveMinVersion`/`DefaultFirewallVersion`, and DIFC isolation specifics — these depend on external releases not yet available."
- **Our assessment**: This is the same "fail closed on an unreleased upstream dependency" pattern `docs-ghaw-enclaves.md` Claim 6 documented for the base enclave feature (gated on `github/gh-aw-firewall#6992`) — here applied one layer up, to the dynamic-repository-selector extension of enclaves (Claim 12) specifically. The explicit mention that "DIFC isolation specifics" for dynamic enclaves are *also* not yet available is a direct signal that this feature's DIFC guarantees (the secrecy-labeling mechanism `docs-ghaw-enclaves.md` Claim 9 documents for static enclaves) have not yet been extended to, or verified for, the dynamic-selector case. For Ch06: flag dynamic enclave delegation as not yet safe to treat as having the same DIFC isolation guarantees as static, enumerated-repository enclaves — the PR's own author says this explicitly, not just "preview" boilerplate.

### Claim 12: PR #58880 adds `enclaves[].dynamic` for agent enclave entries — a mutually-exclusive alternative to the static, enumerated `repos` list — accepting bounded runtime repository selectors (`allowed-owners`, `sensitivity`, `github-policy`, `max-repositories`, per-invocation quotas, `audit-labels`, `expires-at`) so an agent enclave can admit repositories matching a selector at runtime rather than only a compile-time-enumerated set; dynamic mode is agent-only (script enclaves rejected) and requires mcpg `v0.4.16`
- **Evidence**: PR #58880 description ("Add compiler support for dynamic repository enclave policies"), fetched via `gh pr view 58880 --repo github/gh-aw`, including a full YAML configuration example.
- **Confidence**: settled for the configuration schema and stated constraints (first-party, exact field names and a worked example); emerging for real-world usability, since Claim 11 shows the underlying delegation controller this feature depends on is itself gated on an unreleased mcpg release
- **Quote**: "Dynamic repository admission lets agent enclaves accept bounded runtime repository selectors without enumerating every repo at compile time. Static `repos` support remains unchanged; dynamic mode is agent-only and fail-closed behind AWF/mcpg version gates." / "Enforce exactly one of `repos` or `dynamic` per entry. Reject dynamic script enclaves, unknown policy versions, unknown fields, and non-canonical selectors." / "Require AWF dynamic enclave support and mcpg `v0.4.16` for dynamic admission."
- **Our assessment**: This is the single largest architectural extension to the enclave model documented anywhere in the corpus. `docs-ghaw-enclaves.md` Claim 1 describes enclaves as scoping access to "approved private repositories" via a top-level `enclaves` array with *keyed, compile-time-enumerated* entries — every configuration example in that note lists exactly one hardcoded `repo:` per entry. This PR adds a second admission model entirely: an `allowed-owners`-scoped selector with a `max-repositories` cap, invocation/output/execution-time quotas, and an `expires-at` deadline, letting an agent enclave dynamically admit *any* repository under an allowed owner (up to the cap) rather than only a fixed, named set. This trades the "finite-disclosure" precision `docs-ghaw-enclaves.md` Claim 1 names as the feature's defining property (naming *exactly which* repositories are disclosable) for operational flexibility (not needing to recompile the workflow every time a new repository under an owner needs enclave access) — a real security/convenience tradeoff the PR body does not itself editorialize about. The `github-policy: github-repository-read-v1` field name in the example strongly suggests a versioned-profile pattern analogous to `issues-read-v1` (`docs-ghaw-enclaves.md` Claims 7–8), extended from the agent-enclave GitHub Issues surface to a broader per-repository read policy — but this PR's example does not show what operations that policy permits, so this note cannot confirm whether it matches the three-route `issues-read-v1` allowlist or is a distinct, broader surface. For Ch06 (Security and Threat Model): document dynamic enclave admission as a named, opt-in tradeoff against the static model's tighter disclosure guarantee, and flag (per Claim 11) that its DIFC isolation specifics are explicitly unverified as of this release.

### Claim 13: PR #58767 fixes `push_to_pull_request_branch` and `approve_workflow_run` safe outputs so that a policy-driven decline (an `allowed-files`/`protected-files` check blocking a change) is marked `skipped: true` with a `reasonCode` and logged as a warning, rather than returned as an indistinguishable-from-failure `success: false` result that triggered fail-fast cancellation of subsequent safe outputs and polluted failure-rate metrics
- **Evidence**: PR #58767 description ("Reclassify policy-driven safe-output declines as skipped, not hard failures"), fetched via `gh pr view 58767 --repo github/gh-aw`, including a before/after JSON example.
- **Confidence**: settled (first-party bug description with the exact prior behavior, the exact fix, and a concrete before/after payload example)
- **Quote**: "Policy-driven declines in `push_to_pull_request_branch` (allowed-files / protected-files checks) and `approve_workflow_run` (protected-files check) were returned as plain `success: false` results without `skipped: true`. The safe-outputs handler manager only treats `skipped: true` results as soft no-ops; without it, these declines are indistinguishable from genuine failures — triggering fail-fast cancellation of subsequent safe outputs and polluting failure-rate metrics, even though the workflow correctly enforced its configured policy." / "The post-apply parser-differential security check (potential patch-parser bypass) is intentionally left as a hard failure since it indicates a possible attack, not a normal policy decline."
- **Our assessment**: This is a precise, deliberate distinction worth preserving in the guide: a policy correctly blocking a change (a "the system worked as designed" event) was previously conflated with an actual failure, both in run-level fail-fast behavior and in aggregate failure-rate metrics — meaning a well-guarded workflow with many legitimate policy declines could have looked *less* reliable in metrics than a poorly-guarded one that never triggers its own protections. The explicit carve-out — a *different* check in the same handler (the post-apply parser-differential bypass check) is deliberately kept as a hard failure because it signals a possible attack, not a policy decline — shows the fix's authors distinguish "policy did its job" from "something is actively wrong" as two different signal classes requiring different handling, not just relaxing all failures uniformly. This is the same class of "spec/behavior mismatch in safe-output ingestion" already tracked in `blog-ghaw-weekly-2026-08-24.md` Claim 6 (`dismiss_pull_request_review` rejecting documented-valid values) — a third dated instance of gh-aw's own safe-output layer shipping a fix to how it classifies its own decisions. For Ch04/Ch06: when the guide discusses safe-output failure metrics or fail-fast behavior, distinguish "policy declined the action" (should be a skip) from "the action attempt itself errored or was attacked" (should be a hard failure) as a named design principle, citing this fix's explicit carve-out as the concrete boundary case.

### Claim 14: Three workflows — anchor-linked in the blog as "Daily Go Test Parallelizer" (#58826), "Auto-Triage Issues" (#58860), and "Linter Miner" (#58864) — needed model-configuration fixes this week because their previously configured models (`openai/gpt-5.4` for the first two under the Codex engine; `copilot/gpt-5.4` for the third) were rejected or unavailable, and were switched to `openai/gpt-5.3-codex`, `openai/gpt-5.3-codex`, and `copilot/mai-code-1-flash-picker` respectively
- **Evidence**: PR #58826, #58860, and #58864 descriptions, each fetched via `gh pr view <N> --repo github/gh-aw`. Notably, PR #58826's own title and body name the affected workflow as the "Daily CLI Performance Agent" / "daily CLI performance workflow," not "Daily Go Test Parallelizer" as the blog's anchor text states — see Extraction Notes for this discrepancy.
- **Confidence**: settled for the existence and specific model-swap details of each fix (first-party PR descriptions with exact before/after model strings); the blog's own workflow-name label for PR #58826 does not match that PR's own stated subject
- **Quote**: "The Daily CLI Performance Agent failed because `openai/gpt-5.4` rejected Codex's `custom` tool type." (PR #58826) / "Auto-Triage Issues configured the Codex engine with the generic `openai/gpt-5.4` model, causing model validation failure before issue triage could run." (PR #58860) / "Linter Miner failed because its configured `copilot/gpt-5.4` model was unavailable. This prevented the workflow engine and coding sub-agents from starting." (PR #58864)
- **Our assessment**: This is a third dated wave of the recurring "workflows pinned to a generic/unavailable `gpt-5.4` variant need a provider-specific or currently-supported model string" maintenance thread already tracked via the `gh-aw-detection` and general model-catalog notes in this corpus (e.g. `blog-ghaw-weekly-2026-08-24.md` Claim 4's `gh aw models` CLI, built specifically to audit this class of drift). Two of the three fixes are the identical root cause (`openai/gpt-5.4` incompatible with the Codex engine's `custom` tool type / failing Codex model validation) fixed the identical way (switch to `openai/gpt-5.3-codex`) — a strong signal that "generic model alias + Codex engine" is a specifically fragile combination worth calling out by name. For Ch06 (Agentic Operations): when documenting model-catalog/engine-compatibility maintenance, cite this as a concrete recurring pattern — Codex-engine workflows configured with a bare `gpt-5.4` alias rather than the `-codex`-suffixed variant are a known, repeated failure mode across this fleet, not a one-off.

### Claim 15: `dead-code-remover`, the Agent of the Week, ran three times this week, with two clean runs each producing a PR titled "[dead-code] chore: remove dead functions — 5 functions removed" (#58996, #58822) and a third run that hit a snag and returned empty-handed rather than force through a bad batch; the agent enforces a self-imposed cap of never removing more than five functions per run
- **Evidence**: "Agent of the Week" section prose; both named PR numbers independently fetched via `gh pr view 58996/58822 --repo github/gh-aw` and confirmed to carry that exact title and to each list exactly five removed functions in a table.
- **Confidence**: settled (specific, named, independently-verified PR numbers and titles; the "hit a snag and came back empty-handed" third run is asserted by the blog post only, with no corresponding PR to check, so that half of the claim is corroborated only by the post's own prose)
- **Quote**: "This week `dead-code-remover` ran three times and kept up its steady rhythm: two clean runs each produced a PR titled \"[dead-code] chore: remove dead functions — 5 functions removed\" (#58996, #58822), quietly trimming five functions each time, while one run hit a snag and came back empty-handed rather than force through a bad batch." / "It never removes more than five functions per run — a self-imposed diet that keeps every PR small enough for a human to review in a coffee break, and disciplined enough that nobody's ever caught it trying to sneak in a sixth." / "Usage tip: Cap batch size like this for any \"cleanup\" agent — small, reviewable PRs land far more often than one giant sweep."
- **Our assessment**: This is the same named agent profiled in `blog-ghaw-agent-of-the-day-2026-05-28.md` (there called "Dead Code Removal Agent," here "`dead-code-remover`" — same `github/gh-aw` Go-codebase dead-code cleanup workflow, consistent with that note's Concrete Artifacts PR-title format "chore: remove dead functions — N function(s) removed," here shown at N=5 instead of N=1). Two things are new here relative to that May 28 profile: (1) an explicit, named per-run cap ("never removes more than five functions per run") that the May 28 profile's single observed run (1 function removed) gave no evidence for one way or the other — this is the first corpus confirmation that 5 is a designed ceiling, not an emergent average; and (2) the third run's "hit a snag and came back empty-handed rather than force through a bad batch" is a second, independent instance of the "restraint is a feature, not a gap" design principle `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 named explicitly for this same agent's earlier failure/risky/in-progress run classifications — corroborating that the restraint behavior documented in May is still operative four months later. The post's own "Usage tip" generalizing the five-item cap to "any 'cleanup' agent" is editorial advice, not a measured claim, and should be cited as such. For Ch02/Ch04 (Harness Engineering / Operations): update the Dead Code Removal Agent / `dead-code-remover` profile to include the explicit five-function-per-run cap as a named, designed constraint, and add "cap batch size for cleanup/codemod agents" as a generalizable pattern citing this post's own framing.

## Concrete Artifacts

### DIFC guard-policy generation, expected shape after the fix (PR #58302, fetched via `gh pr view 58302 --repo github/gh-aw`)

```json
"github": {
  "guard-policies": {
    "allow-only": {
      "repos": "$GITHUB_MCP_GUARD_REPOS",
      "min-integrity": "$GITHUB_MCP_GUARD_MIN_INTEGRITY"
    }
  }
},
"safeoutputs": {
  "guard-policies": {
    "write-sink": {
      "accept": ["*"],
      "sink-visibility": "${GH_AW_SINK_VISIBILITY}"
    }
  }
}
```
*Source: PR #58302 body, "Expected generated policy shape."*

### `enclaves[].dynamic` configuration for agent enclaves (PR #58880, fetched via `gh pr view 58880 --repo github/gh-aw`)

```yaml
enclaves:
  - agent:
      model: gpt-5
      max-task-bytes: 4096
      max-model-requests: 8
      max-model-tokens: 1024
    dynamic:
      allowed-owners: [octo-org]
      sensitivity: confidential
      github-policy: github-repository-read-v1
      max-repositories: 4
      quotas:
        max-invocations: 8
        max-output-bytes: 32768
        max-execution-seconds: 900
      audit-labels: [dynamic-enclave]
      expires-at: "2999-01-01T00:00:00Z"
    timeout: 120
    memory-limit: 512m
    cpu-limit: "1"
    pids-limit: 128
    tmpfs-limit: 64m
    max-output-bytes: 8192
    max-invocations: 8
```
*Source: PR #58880 body, workflow syntax example. The placeholder `expires-at: "2999-01-01T00:00:00Z"` is the PR's own example value, not a real deadline.*

### Primary-agent GitHub-tool isolation fix for dynamic enclaves (PR #59046, fetched via `gh pr view 59046 --repo github/gh-aw`)

```yaml
enclaves:
  - dynamic:
      allowed-owners: [octo-org]
# primary agent: no tools.github -> "github" no longer in its routable servers
```
*Source: PR #59046 body, "Primary-agent isolation fix" section.*

### Policy-driven safe-output decline, before vs. after (PR #58767, fetched via `gh pr view 58767 --repo github/gh-aw`)

```js
// Before: indistinguishable from a hard failure, triggers fail-fast
{ success: false, error: "Cannot push to pull request branch: patch modifies files outside the allowed-files list (src/index.js). ..." }

// After: classified as a skip, subsequent safe outputs still processed
{ success: false, skipped: true, reasonCode: "POLICY_FILE_PROTECTION_DENIED", error: "..." }
```
*Source: PR #58767 body, "Example" section.*

### `aw.json` package-settings merge example (PR #58267, fetched via `gh pr view 58267 --repo github/gh-aw`)

```json
// Target
{"utc":"-08:00","maintenance":{"runs_on":"self-hosted"}}

// Added package
{"utc":"+01:00","maintenance":{"label_triggers":true}}

// Result
{"utc":"+01:00","maintenance":{"runs_on":"self-hosted","label_triggers":true}}
```
*Source: PR #58267 body, "Configuration merge" section.*

### Cloud Hypervisor fleet migration counts (PR #58726, fetched via `gh pr view 58726 --repo github/gh-aw`)

```
Workflow runtime configurations updated: 71
Excluded (upstream-managed, migrate at source): ci-doctor.md
Additional changes required:
  - gh-proxy usage replaced with local GitHub MCP access (incompatible with Cloud Hypervisor)
  - Pi and Crush-engine workflows migrated to supported engines
  - One self-hosted workflow moved to a GitHub-hosted runner (Cloud Hypervisor requirement)
```
*Source: PR #58726 body.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-integrity-reference.md` Claim 2 (DIFC = Decentralized
    Information Flow Control; `DIFC_FILTERED` event logging) and
    `docs-ghaw-enclaves.md` Claim 9 (the `private:<owner>/<repo>` DIFC
    secrecy label): Claim 3 here (the DIFC guard-policy generation fix for
    GitHub App workflows) is a new, dated instance of the same DIFC
    machinery, extended to a policy-*generation* gap rather than a
    filtering-*behavior* claim.
  - `blog-ghaw-cloud-hypervisor-consolidation.md` Claims 1, 5, and 7 (the
    `gvisor`/`docker-sbx` deprecation, `cloud-hypervisor`'s eligibility
    gate, and migration guidance, respectively): Claim 9 here is the
    platform team's own fleet migration acting on that exact guidance two
    days later, and surfaces three compatibility constraints (gh-proxy
    incompatibility, engine restrictions, GitHub-hosted-runner requirement)
    that post did not itself state.
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 ("restraint is a
    feature, not a gap" for the Dead Code Removal Agent's non-success run
    outcomes) and its Concrete Artifacts PR-title format: Claim 15 here is
    a second, independent, four-months-later instance of the same named
    agent exhibiting the same restraint behavior (a snagged run returning
    empty-handed) and the same PR-title convention (now at N=5 instead of
    N=1 functions removed).
  - `blog-ghaw-weekly-2026-08-24.md` Claim 4 (`gh aw models` CLI, built to
    audit fleet-wide model/catalog drift) and Claim 7 (the recurring
    `gh-aw-detection` schema/validator-mismatch class): Claim 14 here (three
    more workflows needing `gpt-5.4`-variant fixes) and Claim 13
    (policy-decline misclassification) are each a further dated instance of
    the drift/mismatch classes those notes already track.

- **Contradicts**: None found at the MINER.md §4a threshold. No claim in
  this post materially opposes an existing source note's claim in a way
  that would lead the guide toward different advice; the closest candidate
  (Claim 12's dynamic enclave admission trading disclosure precision for
  flexibility) is a new, additive configuration mode alongside the existing
  static model documented in `docs-ghaw-enclaves.md`, not a claim that
  contradicts anything stated there.

- **Extends**:
  - `docs-ghaw-enclaves.md` Claim 1 (the static, compile-time-enumerated
    `repos` admission model) and Claim 6 (the `github/gh-aw-firewall#6992`
    version-gate pattern): Claim 12 here (`enclaves[].dynamic`) is a second,
    parallel admission model for agent enclaves, and Claim 11 shows the same
    "fail closed on an unreleased upstream dependency" gating pattern
    applied one layer up, to the dynamic-selector extension specifically.
  - `docs-ghaw-enclaves.md` Claims 1, 3, 7, and 9 (the two known enclave
    sensitivity values, `confidential` and `public`): Claim 2 here
    (`trusted`) adds a third sensitivity value with different rules
    (unmetered, free-form-within-schema output) rather than a stricter or
    looser point on the same disclosure axis.
  - `docs-ghaw-enclaves.md` Claim 10 (the credential-isolation architecture
    withholding the PAT, mcpg address, root key, container identity, CA
    path, and repository catalog from both primary agent and enclave):
    Claim 10 here shows a *second*, independent isolation-failure surface
    for the same feature family — a tool-routing/backend-registration leak,
    not a credential leak — found and fixed by the same team.
  - `blog-ghaw-weekly-2026-06-29.md` Claim 4 (tracked `gh-aw-mcpg` and
    `gh-aw-firewall` version bumps, v0.3.31→v0.3.32 and v0.27.12→v0.27.13)
    and `docs-ghaw-enclaves.md` Claim 12 (minimum versions AWF v0.28.9,
    mcpg v0.4.13 for `issues-read-v1`): Claims 2 and 12 here name still
    higher version floors (AWF v0.28.13+ for `trusted` sensitivity, mcpg
    v0.4.16 for dynamic admission), continuing the same climbing-version-
    floor trend those two notes already documented.

- **Novel**:
  - **The `trusted` enclave sensitivity level** (Claim 2): first corpus
    documentation of a third enclave sensitivity value beyond
    `confidential`/`public`, and the first to trade output-shape freedom
    ("unmetered... free-form strings") for a stricter schema constraint
    rather than adjusting a disclosure quantity.
  - **DIFC guard-policy generation as authentication-method-dependent, with
    a silent-denial failure mode** (Claim 3): first corpus documentation
    that DIFC policy *generation* (not just filtering behavior) can have
    coverage gaps tied to how a workflow authenticates.
  - **`enclaves[].dynamic` runtime repository selectors** (Claim 12): the
    largest single extension to the enclave access model in the corpus —
    first documentation of owner-scoped, quota-bounded, expiring dynamic
    admission as an alternative to compile-time-enumerated `repos`.
  - **A second, distinct enclave isolation-failure class**: tool-routing/
    backend-registration leakage to the primary agent (Claim 10), as opposed
    to the credential-leakage risks `docs-ghaw-enclaves.md` already
    documents defenses against.
  - **The `dead-code-remover` five-function-per-run cap named explicitly as
    a designed ceiling** (Claim 15), not merely inferable from one prior
    single-function-removal example.
  - **The policy-decline-vs-hard-failure distinction with an explicit,
    named carve-out for a security-relevant check** (Claim 13): the
    `push_to_pull_request_branch` post-apply parser-differential bypass
    check is deliberately kept as a hard failure "since it indicates a
    possible attack" — the clearest first-party statement in the corpus of
    where gh-aw draws the line between "policy worked as intended" and
    "something is actively wrong."

## Guide Impact

- **Chapter 06 (Security and Threat Model)**:
  - Add the `trusted` enclave sensitivity level (Claim 2) as a third tier
    in the enclave sensitivity taxonomy alongside `confidential`/`public`
    already documented from `docs-ghaw-enclaves.md`, noting its distinct
    unmetered/schema-constrained tradeoff and its higher AWF version floor
    (v0.28.13+).
  - Add `enclaves[].dynamic` (Claim 12) as a named, opt-in alternative
    admission model to the static enumerated-`repos` model, with an
    explicit caution (Claim 11, first-party) that its DIFC isolation
    guarantees are not yet verified as of this release — do not present it
    as a drop-in equivalent to the static model's finite-disclosure
    guarantee.
  - Add the primary-agent GitHub-tool-routing isolation fix (Claim 10) as a
    second, distinct enclave isolation-failure class (routing/registration,
    not credential exposure) alongside the credential-isolation guarantees
    already documented from `docs-ghaw-enclaves.md` Claim 10.
  - Note the DIFC guard-policy generation gap for GitHub App workflows
    (Claim 3) as a concrete "green run, silently denied writes" debugging
    trap when documenting DIFC/guard-policy troubleshooting.
  - Cite the policy-decline-vs-attack distinction (Claim 13) — a policy
    correctly blocking a change should be a skip, not a hard failure; a
    check that could indicate an actual attack should stay a hard failure —
    as a named design principle for safe-output failure classification.

- **Chapter 04 (Safety and Constraints)**:
  - Update the Cloud Hypervisor migration guidance sourced from
    `blog-ghaw-cloud-hypervisor-consolidation.md` to add the three
    compatibility constraints this fleet migration (Claim 9) surfaced:
    `gh-proxy` incompatibility, engine restrictions (Pi/Crush needed
    migration), and the GitHub-hosted-runner requirement.

- **Chapter 02 (Harness Engineering)**:
  - Document `gh aw add`'s `aw.json` package-settings merge semantics
    (Claim 4): deep-merge for nested objects, whole-value replacement for
    conflicting scalars/arrays, package values winning on conflict.
  - Update the Dead Code Removal Agent / `dead-code-remover` profile
    (originally from `blog-ghaw-agent-of-the-day-2026-05-28.md`) to include
    the explicit five-function-per-run cap (Claim 15) as a named, designed
    constraint, and cite "cap batch size for cleanup/codemod agents" as a
    generalizable pattern.

- **Chapter 06 (Agentic Operations)**:
  - Add the scheduled synthetic-content smoke-test pattern (Claim 5) —
    generating deliberately low-stakes content on a fixed schedule purely
    to exercise a third-party integration path (here, Linear and Jira) —
    as a named integration-health-monitoring pattern.
  - Add "inference sessions that fail every request must emit an
    incomplete/failure signal and exit nonzero" (Claim 6) as a general
    engine-reliability requirement, citing this as a third dated instance
    of the "silently-successful-but-empty run" failure class alongside the
    Aider and Copilot SDK instances already in the corpus.
  - Cite the recurring "Codex engine + bare `gpt-5.4` alias" fragile
    combination (Claim 14) when discussing model-catalog/engine-
    compatibility maintenance as a fleet-operations task.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with a Python regex-based
   tag-stripping pass**, following the practice established in prior weekly
   notes (e.g. `blog-ghaw-weekly-2026-08-24.md` Extraction Note 1). An
   initial WebFetch pass was also run and cross-checked; it correctly
   captured the substance but rephrased several sentences into a
   restructured summary (e.g. it stated the DIFC PR number as part of its
   own prose reconstruction rather than the blog's actual anchor
   structure). All `Quote` fields above are copied character-for-character
   from the raw-HTML text extraction, not the WebFetch summary.

2. **All fifteen PRs named or linked in the post were independently
   fetched** via `gh pr view <N> --repo github/gh-aw --json
   title,body,url`, within (and beyond, given the post names more PRs than
   the "up to 5 linked pages" MINER.md §1 guidance contemplates for a
   single source) a thorough-extraction pass: #58328, #58302, #58267,
   #58320, #58317, #58313, #58312, #58311 (the eight "Release: v0.88.4"
   PRs), #58726, #59046, #58880, #58767, #58826, #58860, #58864 (the seven
   "Notable Pull Requests" PRs), and #58996, #58822 (the two dead-code-remover
   PRs). PR numbers for the "Notable Pull Requests" and "Agent of the Week"
   sections were recovered from the raw HTML's anchor `href` attributes
   (not printed as visible PR numbers in that section's prose), confirmed
   by locating the literal anchor text ("Migrate agentic workflows to Cloud
   Hypervisor," etc.) directly adjacent to each `pull/<N>` href in the raw
   HTML — see the next note for one resulting discrepancy this surfaced.

3. **Blog-anchor-text vs. PR-content discrepancy found and flagged, not
   filed as a contradiction**: the blog's "Notable Pull Requests" bullet
   links the anchor text "Daily Go Test Parallelizer" to PR #58826, but
   that PR's own title ("Use Codex-compatible model for daily CLI
   performance workflow") and body ("The Daily CLI Performance Agent
   failed...") both name a different workflow — "Daily CLI Performance
   Agent," not "Daily Go Test Parallelizer." This was confirmed by fetching
   PR #58826 directly and is recorded in Claim 14. Per the precedent set in
   `blog-ghaw-weekly-2026-08-24.md` Extraction Note 4 (a structurally
   identical blog-prose-vs-PR-schema imprecision), this is a blog-prose
   labeling imprecision against a first-party PR source, not a disagreement
   between two independently-argued claims, so it does not meet the
   MINER.md §4a bar for a contradiction issue.

4. **Cross-reference check performed** against `docs-ghaw-enclaves.md`,
   `docs-ghaw-integrity-reference.md`, `blog-ghaw-cloud-hypervisor-consolidation.md`,
   `blog-ghaw-weekly-2026-08-24.md`, `blog-ghaw-weekly-2026-08-17.md`,
   `blog-ghaw-weekly-2026-06-29.md`, and `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   all re-read in full (not skimmed) before writing Cross-References, plus
   `CONTRADICTIONS.md` and open `contradiction`-labeled issues (including
   the still-open #3285, filed from `blog-ghaw-cloud-hypervisor-consolidation.md`,
   which this note's Claim 9 provides corroborating-not-contradicting
   evidence for). No claim in this source meets the MINER.md §4a bar for a
   new contradiction filing. All `Claim N` citations above were verified
   against the actual numbered claims in the cited notes at the time of
   writing, per MINER.md §4b.

5. **Confidence rated `emerging` overall, not `settled`**: individual bug
   fixes (Claims 3, 6, 7, 8, 13) are settled, first-party, and shipped. But
   the release's most architecturally significant content — the `trusted`
   sensitivity level (Claim 2) and, especially, dynamic enclave delegation
   (Claims 10–12) — is explicitly stated by its own implementing PRs to be
   gated on unreleased upstream mcpg/AWF releases and to have unverified
   DIFC isolation specifics (Claim 11's own words: "these depend on
   external releases not yet available"). The overall grade reflects that
   mix rather than treating the whole release as uniformly settled.
