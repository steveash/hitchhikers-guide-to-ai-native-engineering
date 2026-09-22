---
source_url: https://github.github.com/gh-aw/blog/2026-09-21-weekly-update/
source_type: blog-post
title: "Weekly Update – September 21, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-09-21
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: settled
issue: "#3608"
---

# Weekly Update – September 21, 2026 (GitHub Agentic Workflows)

> v0.89.17 is a stability release hardening AIC accounting, logs-audit
> efficiency, and the safe-outputs CLI transport, plus routine MCP
> Gateway/firewall version bumps and a model-catalog correction; the "Agent
> of the Week" spotlight, `deployment-incident-monitor`, ran a record 19
> times this week and correctly diagnosed a real Azure OpenAI provider-side
> failure via a triple-layered issue-deduplication design.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; a short intro, a "Release: v0.89.17" section with
  "What's New" (4 bullets) and "Bug Fixes & Improvements" (5 bullets)
  subsections, a "Notable Pull Requests" section of three bullets, an "Agent
  of the Week: deployment-incident-monitor" spotlight, and a "Try It Out"
  closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The on-page byline names the
  author as "Copilot" — the same non-human byline pattern documented in
  every prior weekly note in this corpus (e.g. `blog-ghaw-weekly-2026-09-07.md`).
  Every PR named or linked in the post was independently fetched via `gh pr
  view <N> --repo github/gh-aw --json title,body,url` to corroborate the
  blog's one-line summaries against first-party PR descriptions, and the
  "Agent of the Week" section's own claims were checked against the live
  `deployment-incident-monitor.md` workflow file and the actual filed
  issue (#61892) — see Extraction Notes for the full list.
- **Scope**: One "Release: v0.89.17" section naming nine PRs (four "What's
  New" bullets covering six PRs, five "Bug Fixes & Improvements" bullets
  covering five PRs — with one PR, `#61234`, counted once here for clarity),
  one "Notable Pull Requests" section naming two additional PRs beyond the
  one already named in "What's New" (`#61871`), and one "Agent of the Week"
  spotlight naming one filed issue (`#61892`). Does NOT cover: a full
  changelog/release-notes page for v0.89.17 beyond the linked GitHub
  Releases tag; the exact AWF config-schema diff introduced by PR #61527
  (the PR body links a schema refresh but the post itself does not surface
  schema details); or any workflow-configuration changes beyond
  `deployment-incident-monitor.md` itself.

## Extracted Claims

### Claim 1: v0.89.17, released September 19, 2026, is framed as focused on hardening the AIC accounting pipeline, AWF/firewall integration, and safe-outputs handling
- **Evidence**: Intro paragraph and the "Release: v0.89.17" section's lead sentence.
- **Confidence**: settled (first-party framing of the release's own scope)
- **Quote**: "We shipped a fresh release packed with reliability fixes, a smarter logs pipeline, and an updated model catalog — plus our usual dose of documentation polish." / "v0.89.17 landed on September 19th, focused on hardening the AIC accounting pipeline, AWF/firewall integration, and safe-outputs handling."
- **Our assessment**: This is scene-setting framing; the substance is in Claims 2–16 below. Unlike the September 7 update (`blog-ghaw-weekly-2026-09-07.md` Claim 1), which named architecturally new features (a third enclave sensitivity level, dynamic enclave delegation), this release's own framing names only hardening/reliability work — consistent with the Prospector's own low-novelty assessment of this issue. No new configuration surface is introduced anywhere in this post; every named PR is a bug fix, an efficiency improvement, or a version bump.

### Claim 2: PR #61871 stops `gh aw logs --cached-jsonl --audit` from redownloading artifacts for runs whose usage-only data is already cached, instead reusing matching cached records on a best-effort basis and falling back to partial audit generation when cached details are unavailable
- **Evidence**: PR #61871 description ("Avoid redownloading cached runs during logs audit"), fetched via `gh pr view 61871 --repo github/gh-aw`. The blog names this PR twice — once in "What's New" and again, with added framing, in "Notable Pull Requests."
- **Confidence**: settled (specific PR, specific prior bug, specific fix mechanism)
- **Quote**: "`logs --cached-jsonl --audit` bypassed cached runs and redownloaded their artifacts. Audit mode should instead use available cached data on a best-effort basis." / "Allow audit mode to reuse matching usage-only cached records." / "Fall back to partial audit generation when cached audit details are unavailable."
- **Our assessment**: The blog's own "Notable Pull Requests" framing — "a nice efficiency win that speeds up repeated `gh aw logs` invocations by skipping runs already cached locally" — is descriptive, not a technical claim; the technical substance is the specific bug (audit mode ignored its own cache) and the specific fix (best-effort reuse with a partial-generation fallback). This directly extends the two-tier `gh aw logs`/`gh aw audit` monitoring pattern documented in `docs-ghaw-cost-management.md` Claim 4 — a practitioner running repeated audits (e.g. a daily monitoring workflow, per `docs-ghaw-agentic-ops.md` Claim 8's `copilot-token-audit` reference implementation) previously paid a redundant download cost on every invocation; this fix removes that redundancy specifically for the `--audit` code path. For Ch06 (Agentic Operations): note that `gh aw logs --audit` cache-reuse behavior changed in v0.89.17 — teams running scheduled audit workflows should expect faster repeated invocations without a corresponding cache-flag change.

### Claim 3: PR #61027 fixes multi-target `gh aw logs` queries so that each active target is queried once per round in lock-step, rather than letting one target's requests exhaust shared API/count/timeout budgets before other targets receive any data
- **Evidence**: PR #61027 description ("Distribute multi-target logs queries fairly"), fetched via `gh pr view 61027 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description with the exact fairness failure and the round-based fix mechanism)
- **Quote**: "Multi-target `logs` requests could let one target consume multiple run batches before others received data. This biased shared API, count, and timeout budgets toward earlier targets." / "Query each active target once per round." / "Prevent any target from starting its next batch until all active targets complete the current round." / "Remove completed or failed targets from subsequent rounds."
- **Our assessment**: This is a narrow but concrete fairness bug in `gh aw logs`'s multi-target mode (querying several workflows or repositories in one invocation): without round-based scheduling, an operator monitoring multiple targets in one command could silently get complete data for the first-queried target and truncated or empty data for later ones once the shared count/timeout budget was exhausted — a data-completeness trap for anyone building fleet-wide dashboards from a single multi-target `gh aw logs` call. This is new to the corpus; no existing note documents multi-target query fairness. For Ch06: flag this as a fixed-in-v0.89.17 correctness bug for practitioners running multi-target `gh aw logs` invocations before this release — earlier-queried targets could have silently received disproportionate data.

### Claim 4: PR #60951 adds per-run artifact-download duration and size tracking to `gh aw logs`, surfaced in an end-of-run stats summary, with zero recorded for cache hits
- **Evidence**: PR #60951 description ("logs: track per-run download duration/size and render end-of-run stats summary"), fetched via `gh pr view 60951 --repo github/gh-aw`.
- **Confidence**: settled (first-party description naming the exact fields added and their population rule)
- **Quote**: "The `gh aw logs` command didn't capture how long artifact downloads took or how much data they transferred, making it hard to diagnose slow runs or estimate GitHub API usage." / "Added `DownloadDuration` / `DownloadSizeBytes` to `WorkflowRun`, populated by timing the download and measuring the resulting artifact directory size (zero for cache hits)." / "Extracted `downloadAndTimeRunArtifacts` from `processSingleRunDownload` to isolate the timing/sizing logic."
- **Our assessment**: This adds a new observability dimension to `gh aw logs` output — download duration/size — distinct from the cost/token metrics (AIC, ET) already tracked in `docs-ghaw-agentic-ops.md`'s audit schema and `blog-ghaw-ai-credits-migration.md`'s AIC metric. It is specifically an infrastructure-diagnostic signal (is `gh aw logs` itself slow because of large artifacts or API throttling?) rather than an agent-run-cost signal. Combined with Claim 2 and Claim 3, this week's three logs-related PRs form a coherent theme: `gh aw logs`/`gh aw audit` received efficiency (cache reuse), fairness (round-robin), and observability (download stats) improvements in the same release, none of which change the metrics' meaning — only the tooling around collecting them. For Ch06: note the new `DownloadDuration`/`DownloadSizeBytes` fields as available for diagnosing why a `gh aw logs` invocation is slow, separate from agent-run cost diagnostics.

### Claim 5: PR #61234 adds `gemini-3.8-flash` and `claude-fable-5.1` model aliases and corrects pricing for `gpt-6-astra` (previously stored roughly two orders of magnitude too high, at ~$1000/$5000 per 1M input/output tokens instead of ~$10/$50) and `gpt-5.6-sol` (GitHub Copilot section only), based on a daily model-inventory checker cross-referencing five live provider APIs
- **Evidence**: PR #61234 description ("model catalog: add gemini-3.8-flash/claude-fable-5.1 aliases, fix gpt-6-astra/gpt-5.6-sol pricing"), fetched via `gh pr view 61234 --repo github/gh-aw`.
- **Confidence**: settled (first-party description with exact before/after numeric pricing values and named cross-check sources)
- **Quote**: "The daily model inventory checker flagged a missing model alias, two stale/incorrect pricing entries, and a missing pricing entry after cross-checking `model_aliases.json` and the `models.json` pricing mirrors against live provider inventories (OpenAI, Anthropic, Gemini, Copilot SDK, Copilot reflect)." / "`gpt-6-astra` (openai and github-copilot sections): input/output were stored two orders of magnitude too high (`0.001`/`0.005`, i.e. ~$1000/$5000 per 1M tokens). Corrected to `1e-05`/`5e-05` (~$10/$50 per 1M), confirmed by agreement across Copilot SDK, Copilot reflect, and models.dev."
- **Our assessment**: The blog's own summary ("added `gemini-3.8-flash` and `claude-fable-5.1` aliases and corrected pricing for `gpt-6-astra`/`gpt-5.6-sol`") understates the severity of the `gpt-6-astra` bug: a two-orders-of-magnitude pricing error (~100x too high) in a cost-tracking system is not a minor correction — if any AIC-based guardrail, budget alert, or cost report used `gpt-6-astra` pricing before this fix, every derived dollar figure for that model would have been inflated ~100x. This is the first corpus documentation of a "daily model inventory checker" as a named, automated maintenance process (cross-referencing five live provider APIs against two local pricing mirrors), distinct from the one-off manual model-catalog fixes documented in prior weekly notes (`blog-ghaw-weekly-2026-08-24.md` Claim 4's `gh aw models` CLI is an on-demand audit tool; this PR implies a scheduled/automated inventory-checking process feeding it). For Ch06 (Agentic Operations): flag that gh-aw's model pricing catalog has previously carried a 100x pricing error for at least one model, and cite the existence of an automated daily inventory-check process as the detection mechanism — teams building their own cost dashboards on top of `models.json` should treat the catalog as generally reliable but not infallible, especially for newly added models.

### Claim 6: This week bundled three separate runtime-dependency version bumps — MCP Gateway (`gh-aw-mcpg`) from v0.4.23 to v0.4.25 (#61661), `gh-aw-firewall` (AWF) from v0.28.16 to v0.28.17 (#60945), and AWF again from v0.28.18 to v0.28.20 (#61527, which also refreshes the embedded AWF config schema and adds `AWFEnclaveAgentToolsMinVersion` for native `enclaves[].agent.tools.github` support)
- **Evidence**: PR #61661, #60945, and #61527 descriptions, each fetched via `gh pr view <N> --repo github/gh-aw`.
- **Confidence**: settled (first-party, exact before/after version strings for each bump)
- **Quote**: "Upgrades the pinned MCP Gateway (`gh-aw-mcpg`) Docker image from `v0.4.23` to `v0.4.25`." (#61661) / "Bumps the pinned `github/gh-aw-firewall` version from `v0.28.16` to `v0.28.17` and refreshes all generated artifacts to match." (#60945) / "Updates the default gh-aw-firewall/AWF release from `v0.28.18` to `v0.28.20` and reconciles the new AWF config schema surface introduced by the Cloud Hypervisor enclave configuration model." / "Added `AWFEnclaveAgentToolsMinVersion` for native `enclaves[].agent.tools.github` support." (#61527)
- **Our assessment**: This is a fourth dated instance of the recurring `gh-aw-mcpg`/`gh-aw-firewall` version-bump pattern already tracked in the corpus: `blog-ghaw-weekly-2026-06-29.md` Claim 4 recorded mcpg v0.3.31→v0.3.32 and AWF v0.27.12→v0.27.13 (June 29); `docs-ghaw-enclaves.md` Claim 12 recorded the `issues-read-v1` profile's floor at AWF v0.28.9/mcpg v0.4.13; `blog-ghaw-weekly-2026-09-07.md` Claims 2 and 12 recorded a further-raised floor of AWF v0.28.13+ for the new `trusted` enclave sensitivity and mcpg v0.4.16 for dynamic enclave admission. This week's bumps (AWF now at v0.28.20, mcpg now at v0.4.25) continue that same climbing-version-floor trend two weeks later, and the AWF bump is explicitly tied to reconciling a new config-schema surface from the Cloud Hypervisor enclave model — a direct dated follow-on to the Cloud Hypervisor migration this corpus already tracks (`blog-ghaw-cloud-hypervisor-consolidation.md`, `blog-ghaw-weekly-2026-09-07.md` Claim 9). The `AWFEnclaveAgentToolsMinVersion` addition is new: it names a fourth distinct minimum-version constant for a specific enclave capability (native `tools.github` support inside agent enclaves), alongside the `MCPGDynamicRepositoryDelegationMinVersion` and `AWFDynamicRepositoryEnclaveMinVersion` constants `blog-ghaw-weekly-2026-09-07.md` Claim 11 already documents as not-yet-satisfiable pending an unreleased mcpg release. For Ch06 (Security and Threat Model): update the running list of named minimum-version gate constants for enclave features to include `AWFEnclaveAgentToolsMinVersion`, and note that gh-aw's own runtime dependency versions (mcpg, AWF) are bumped on a near-weekly cadence — pinned-version drift for self-hosted or vendored deployments should be checked at least that often.

### Claim 7: PR #61426 fixes automatic grading so that native Copilot tool calls recorded in the staged agent session log — notably the built-in `skill` tool — are folded into the same preprocessing pass that builds the grader trace payload, which previously was built exclusively from MCP gateway logs
- **Evidence**: PR #61426 description ("Include native Copilot tool calls in the automatic grader trace payload"), fetched via `gh pr view 61426 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description naming the exact prior gap, the specific grader it affected, and the fix's mechanism)
- **Quote**: "`trace.toolCalls` was built exclusively from MCP gateway logs, so native Copilot tools recorded in the staged `events.jsonl` session log — notably the built-in `skill` tool — never reached graders." / "`skill-constraint-coverage` could therefore only report \"not applicable\" unless a repository supplied its own `agentOutput.toolCalls`, which is impossible to do before grading because the graders step is emitted ahead of user post-steps." / "`actions/setup/js/trace_graders.cjs` now folds native agent events into the same preprocessing pass."
- **Our assessment**: This directly extends `docs-ghaw-graders.md` Claim 9's description of grading as "one shared preprocessing pass over trace files that every enabled grader... reuses" — this fix is a concrete, dated instance of that shared preprocessing pass having had an actual coverage gap: any workflow using the `skill-constraint-coverage` grader (from `docs-ghaw-graders.md` Claim 3's ten reserved built-in grader IDs) against a workflow whose skill invocations went through Copilot's native tool-call path rather than the MCP gateway would have silently gotten an uninformative "not applicable" result rather than a real evaluation, with no workaround available to the repository (the fix notes a repository-supplied `agentOutput.toolCalls` override was "impossible... because the graders step is emitted ahead of user post-steps"). For Ch06 (Agentic Operations): when documenting grader reliability, note that grader trace completeness depends on which tool-invocation path an agent uses (MCP gateway vs. native engine tool calls), and that this specific gap for native Copilot `skill` tool calls was closed in v0.89.17 — teams grading skill usage on earlier versions may have seen false "not applicable" results.

### Claim 8: PR #61427 makes the `safeoutputs` CLI transport fail loudly with a real error instead of silently failing open, closing a bug where dropping the pipe character from the documented `printf '{...}' | safeoutputs noop .` invocation caused `printf` to silently consume the CLI arguments as format text, exit 0, and never invoke the CLI at all
- **Evidence**: PR #61427 description ("safeoutputs CLI: fail loudly instead of failing open"), fetched via `gh pr view 61427 --repo github/gh-aw`, including a terminal reproduction.
- **Confidence**: settled (first-party bug description with an exact reproducible failure mode and console transcript)
- **Quote**: "The documented `safeoutputs` CLI form puts the binary in the middle of the command line (`printf '{...}' | safeoutputs noop .`). Dropping the `|` makes `printf` consume `safeoutputs noop .` as format arguments — identical stdout, exit 0, CLI never invoked — so the agent believes it emitted a safe output and the run ends with none, reported as an undiagnosed \"produced no safe outputs\" issue." / "A single quoted JSON object argument is now a first-class transport: `safeoutputs noop '{\"message\":\"...\"}'`. The binary comes first, so every malformed variant still executes it." / "For the `safeoutputs` server, arguments that resolve to zero recognized tool arguments... now fail with guidance instead of printing help and exiting 0."
- **Our assessment**: This is a fifth dated instance of the "agent run completes without honestly reflecting what happened" failure class already tracked across this corpus (`blog-ghaw-weekly-2026-08-17.md` Claim 9's Aider engine, `blog-ghaw-weekly-2026-08-24.md` Claim 5's Copilot SDK crashes, `blog-ghaw-weekly-2026-09-07.md` Claim 3's DIFC guard-policy generation gap and Claim 6's Pi/Anthropic routing bug) — here the mechanism is a shell-syntax footgun (a missing pipe character) that produces byte-for-byte identical stdout and a zero exit code whether or not the CLI actually ran, making the failure invisible at every layer except "the run reported zero safe outputs." The fix's dual approach — a more robust inline-JSON transport that puts the binary first (so malformed piping variants still execute it) plus explicit failure instead of silent help-and-exit-0 for zero-argument invocations — is a concrete, generalizable pattern: CLI tools invoked by LLM-generated shell commands should be designed so that common malformed invocations fail loudly rather than degrading to a silent no-op. For Ch03 (Agent Design and Behavior) / Ch06: cite this as a concrete example of why safe-output CLI transports (or any tool interface an LLM is expected to invoke via generated shell commands) should treat "zero recognized arguments" as an error, not a silent success — the failure mode here was specifically dangerous because it was indistinguishable from a correct no-op call.

### Claim 9: PR #61424 fixes a bug where a workflow that imports a shared `engine:` block (including `engine.auth` for OIDC/WIF federation) and also declares a root-level `model:` field would silently lose the entire imported engine config and fall back to API-key auth with no warning, because `ExtractEngineConfig` returns a non-nil config for top-level-only keys and the import-resolution logic only merged in the imported config when that returned config was nil
- **Evidence**: PR #61424 description ("Preserve imported engine config (including auth) when a workflow sets top-level model"), fetched via `gh pr view 61424 --repo github/gh-aw`, including a before/after YAML example.
- **Confidence**: settled (first-party bug description with named function, exact root cause, and a worked YAML example)
- **Quote**: "A workflow that imports a shared `engine:` block and also declares a root-level `model:` silently lost the entire imported engine config — notably `engine.auth` (OIDC/WIF) — and fell back to API-key auth with no warning." / "`ExtractEngineConfig` returns a non-nil `EngineConfig` for top-level-only keys (`model`, `max-turns`, budgets). `resolveEngineFromIncludesAndImports` extracted the imported engine config only when that c[onfig was nil]"
- **Our assessment**: This is a security-relevant silent-failure bug distinct from the classes tracked in Claim 8: rather than a missing safe output, the failure mode here is silently falling back from federated OIDC/WIF authentication to API-key authentication — a downgrade in authentication mechanism that produces no error and no warning, only a workflow that continues to run (now with a different, weaker credential source). A team relying on `engine.auth` OIDC federation specifically to avoid provisioning long-lived API keys would have had that protection silently removed by adding an unrelated top-level `model:` override. This is new to the corpus; no existing note documents an engine-config-import/top-level-override interaction bug. For Ch06 (Security and Threat Model): flag this as a concrete example of a configuration-merge bug causing a silent authentication-method downgrade (OIDC → API key) — worth a general caution that engine/auth configuration inherited via `imports:` should be verified as actually applied whenever a workflow also sets any top-level engine-adjacent field, not assumed safe by default.

### Claim 10: This week's daily AIC accounting hardening covered three distinct ambiguous-evidence cases — legacy runs with validated same-attempt agent artifacts but empty usage accounting (#61313), pre-harness AWF-startup failures with no accounting file and no engine-harness marker (#61232), and jobs that failed before being assigned a runner and so produced no usage artifact at all (#61222) — each now counted as zero AIC rather than blocking the guardrail, while explicitly preserving fail-closed behavior for any evidence that remains ambiguous
- **Evidence**: PR #61313, #61232, and #61222 descriptions, each fetched via `gh pr view <N> --repo github/gh-aw`.
- **Confidence**: settled (first-party bug descriptions each naming the exact evidence condition treated as zero AIC and the exact condition still treated as fail-closed)
- **Quote**: "Treat failed agent jobs with no accounting file as zero only when there is no contradictory execution or agent-log evidence. Recognize successful deterministic sample replays from the validated same-attempt agent artifact when legacy usage accounting is empty. Preserve fail-closed behavior for malformed execution evidence, harness-started jobs, unreadable accounting, and ordinary successful runs." (#61313) / "Inspect the run's agent artifact when accounting is missing. Count zero usage only when logs show an AWF startup failure and no engine harness marker. ... Continue failing closed for ambiguous or post-harness failures." (#61232) / "Treat failed jobs with no assigned runner or executed steps as zero AIC. Preserve fail-closed behavior when execution metadata is incomplete or a runner was assigned." (#61222)
- **Our assessment**: All three fixes share an identical structural pattern: the daily AIC guardrail (introduced per `blog-ghaw-ai-credits-migration.md` Claim 1's AIC metric) defaults to fail-closed (blocking/flagging) whenever usage accounting is missing, and each of these PRs carves out one specific, narrowly-evidenced legacy/edge condition — a validated replay artifact, a confirmed pre-harness startup failure, or a confirmed unassigned-runner failure — as safe to count as zero rather than block on, while explicitly re-affirming fail-closed for every other ambiguous case. This is a concrete, repeatable engineering pattern for hardening a cost/usage guardrail without weakening its default safety posture: each carve-out requires positive evidence of the specific benign condition, not merely the absence of the expected evidence. For Ch06 (Agentic Operations): cite this three-PR sequence as a worked example of safely relaxing a fail-closed guardrail — narrow, evidence-gated exceptions rather than a blanket loosening of the default.

### Claim 11: PR #61605 raises the `Code Scanning Fixer` workflow's timeout from 40 to 50 minutes and adds a focused set of allowed shell helpers (`cat:*`, `git diff:*`, `git restore:*`, `git status:*`, `grep`, `head:*`, `jq`, `ls`, `sed:*`, `tail`, `wc`) for large-output triage, fixing repeated tool denials and timeouts the agent hit while inspecting oversized MCP/tool outputs
- **Evidence**: PR #61605 description ("Fix Code Scanning Fixer timeout and tool denials"), fetched via `gh pr view 61605 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description with exact prior/new timeout values and the exact allowlist added)
- **Quote**: "Code Scanning Fixer exceeded its 40-minute agent execution window after repeated denied shell attempts while inspecting large tool outputs. The workflow needed more headroom and clearer allowed parsing paths for oversized MCP/tool responses." / "Raises the workflow timeout from `40` to `50` minutes." / "Adds focused shell helpers used for large-output triage... Directs the agent to inspect saved large outputs with allowed shell readers (`grep`, `head`, `jq`, `sed`, `tail`)."
- **Our assessment**: This is a concrete, named example of a workflow-tuning fix where the root problem was a mismatch between the agent's granted tool permissions and the actual inspection work it needed to do — the agent was repeatedly denied the exact read-only shell commands (`grep`, `head`, `jq`, `sed`, `tail`) it needed to triage large outputs without loading them entirely into context, so it burned its execution budget on denied attempts and retries rather than on productive work. This is a specific, practitioner-actionable pattern: if a workflow's agent repeatedly needs to inspect large saved outputs, granting a narrow, explicitly read-only shell allowlist (rather than a broader or absent one) both reduces tool-denial churn and keeps large content out of the context window. For Ch02 (Harness Engineering): cite this as a concrete before/after example of right-sizing a `bash:` tool allowlist for large-output triage tasks — the fix's specific allowlist is a reusable template for similar "inspect large tool output without loading it all into context" workflows.

### Claim 12: PR #61602 fixes slash-command activation silently failing when a GitHub-web-editor comment uses CRLF line endings, because the compiled `activation` job's `if:` condition — generated by `buildMultiCommandCheck` in `pkg/workflow/command.go` — only recognized three match shapes (`body == '/cmd'`, `startsWith(body, '/cmd ')`, `startsWith(body, '/cmd\n')`), none of which match a body starting with `/cmd\r\n`
- **Evidence**: PR #61602 description ("Fix slash command activation on CRLF line endings"), fetched via `gh pr view 61602 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description naming the exact function, the exact three prior match shapes, and the exact CRLF gap)
- **Quote**: "A slash command on its own line (e.g. `/qa-agent-android`) followed by more text was not activating the workflow when the comment body used CRLF line endings, as produced by the GitHub web editor. `pre_activation` correctly matched the command, but the compiled `activation` job's `if:` condition rejected it, silently skipping the run." / "`buildMultiCommandCheck` in `pkg/workflow/command.go` only generated three match shapes for the compiled condition: exact match (`body == '/cmd'`), `startsWith(body, '/cmd ')`, `startsWith(body, '/cmd\\n')`. None of these match a body starting with `/cmd\\r\\n`, while the JS-side `check_command_position.cjs` tolerates `\\r`"
- **Our assessment**: This is a specific, source-attributable trigger of the bug: comments authored through the GitHub web editor (as opposed to, e.g., the GitHub API or most local git clients) produce CRLF line endings, so any `slash_command`-triggered workflow was silently non-functional for exactly that authoring path — a "silently skipped, not failed" outcome, consistent with the same debugging-trap shape as Claim 8 and Claim 9 above (the run produces no visible error; it simply never starts). The PR notes an inconsistency worth preserving: the JS-side activation-position checker (`check_command_position.cjs`) already tolerated `\r`, while the compiled GitHub Actions `if:` condition (generated separately, in Go) did not — meaning the two activation-check implementations had drifted out of sync for this input class. This corroborates and extends the existing corpus finding (`docs-ghaw-triggers-reference.md`, `blog-ghaw-chatops.md`-adjacent notes not individually re-verified here) that `slash_command` activation reliability has been an ongoing source of silent-failure bugs. For Ch06: note CRLF-authored comments (notably from the GitHub web editor) as a specific, now-fixed-in-v0.89.17 trigger for silent `slash_command` activation failures — teams on pre-v0.89.17 builds using web-editor-authored slash commands should verify their commands actually activated.

### Claim 13: PR #61430 fixes two Copilot SDK driver bugs — auto-granted git subcommand permissions (e.g. `shell(git checkout:*)`) being rejected because the permission matcher relied on unreliable SDK-provided command identifiers rather than the actual command text, and the tool-denial guard hanging indefinitely once tripped if `session.disconnect()` or an in-flight SDK request never settled
- **Evidence**: PR #61430 description ("Fix Copilot SDK multiword shell prefix matching and denial-guard hang"), fetched via `gh pr view 61430 --repo github/gh-aw`. This PR is named only in the "Notable Pull Requests" section, with no PR number printed in the visible bullet text; the number was recovered from the anchor `href` in the raw HTML.
- **Confidence**: settled (first-party bug description naming the exact matcher field relied on and the exact hang condition)
- **Quote**: "Git subcommands auto-granted by `safe-outputs.create-pull-request` (e.g. `shell(git checkout:*)`, `shell(git branch:*)`) were rejected by the Copilot SDK driver because the permission matcher relied on unreliable SDK-provided command identifiers. Additionally, once the tool-denial guard tripped, the process could stall indefinitely if `session.disconnect()` or the in-flight SDK request never settled." / "The matcher previously compared rule prefixes against `commands[].identifier`, which the SDK may populate with just the executable name (`\"git\"`), the full command text, or nothing at all — none of which reliably exposes the s[ubcommand]"
- **Our assessment**: This is a two-in-one fix worth separating: (1) a false-negative permission-matching bug specific to the Copilot SDK engine, where commands that gh-aw itself auto-grants (for the `create-pull-request` safe output specifically) were being denied by the engine's own permission layer due to an unreliable upstream field, and (2) an availability bug where the *consequence* of a denial (the denial guard) could hang the whole run rather than fail fast. The combination is notable: a workflow using the Copilot SDK engine with git-subcommand safe outputs could previously have experienced not just an incorrect denial but an indefinite hang triggered by that denial — turning a permission bug into an availability bug. For Ch06: flag pre-v0.89.17 Copilot SDK engine runs using auto-granted git subcommands as a specific combination that could hang rather than fail cleanly.

### Claim 14: PR #61599 fixes `${{ experiments.<name> }}` references inside `engine.model` (or the split top-level `model:` field) being rewritten correctly for prompt-body text but left as the literal, GitHub-Actions-invalid `experiments.model` context reference in three specific generated environment variables (`ANTHROPIC_MODEL`, `GH_AW_INFO_MODEL`, `GH_AW_ENGINE_MODEL`), by adding regex-based rewrite helpers that convert `experiments.<name>` into valid job-scoped expressions such as `needs.activation.outputs.<name>`
- **Evidence**: PR #61599 description ("Rewrite `experiments.<name>` in engine.model to valid job-scoped expressions"), fetched via `gh pr view 61599 --repo github/gh-aw`, including the invalid pre-fix YAML.
- **Confidence**: settled (first-party bug description naming the exact three affected env vars and the exact rewrite mechanism)
- **Quote**: "`${{ experiments.model }}` used in `engine.model` (or the split top-level `model:` field) was rewritten for prompt-body text but not for `ANTHROPIC_MODEL`, `GH_AW_INFO_MODEL`, or `GH_AW_ENGINE_MODEL`. The compiled lock file kept the literal `experiments.model` reference, which GitHub Actions rejects at run time since `experiments` is not a valid context" / "Added regex-based rewrite helpers (`pkg/workflow/compiler_experiments.go`) that convert `experiments.<name>` into a valid, job-scoped reference: `RewriteExperimentsReferenceForDownstreamJobs` → `needs.activation.outputs.<name>`, for j[obs downstream of activation]"
- **Our assessment**: This is a compile-time correctness bug specific to gh-aw's `experiments` feature (documented at the specification level in `docs-ghaw-practices-experiments-specification.md`, not independently re-verified here): a workflow author referencing an experiment variant inside `engine.model` would get a compiled lock file that GitHub Actions rejects outright at run time, because `experiments` is a gh-aw-internal templating concept with no corresponding GitHub Actions expression context — the rewrite step existed for prompt text but had a specific, narrow gap for three named environment variables tied to model configuration. For Ch06: note this as a fixed compile-time gap for teams combining the `experiments` feature with per-experiment model overrides — pre-v0.89.17 compiled workflows using this combination would fail at GitHub Actions runtime, not at `gh aw compile` time, since the invalid reference only surfaces when the Action actually evaluates the expression.

### Claim 15: `deployment-incident-monitor`, the Agent of the Week, watches `deployment_status` events for `error`/`failure` states and layers three independent deduplication mechanisms — a trigger-level `skip-if-match: "is:issue is:open label:incident label:deployment-failure"` condition that cancels the run before the agent job starts, an explicit prompt instruction to check for an existing open incident issue before creating a new one, and `close-older-issues: true` combined with `expires: 7d` on the `create-issue` safe output
- **Evidence**: Blog post prose plus the live workflow file, fetched via `gh api repos/github/gh-aw/contents/.github/workflows/deployment-incident-monitor.md`.
- **Confidence**: settled (blog framing corroborated directly against the live, first-party workflow YAML frontmatter)
- **Quote**: "Meet `deployment-incident-monitor`, the on-call responder of the gh-aw fleet — it watches every `deployment_status` event and automatically files a deduplicated incident issue with root-cause analysis whenever something breaks." / "Usage tip: Pair `deployment_status`-triggered monitors like this one with `skip-if-match` on your incident label so repeated failures from the same root cause collapse into a single, evolving issue instead of flooding your tracker." From the workflow file itself: `on: deployment_status: state: [error, failure]` / `skip-if-match: "is:issue is:open label:incident label:deployment-failure"` / `safe-outputs: create-issue: expires: 7d, title-prefix: "[Incident] ", labels: [incident, deployment-failure], close-older-issues: true` / step 1 of the prompt: "Check for an existing open incident issue: Look for open issues with both `incident` and `deployment-failure` labels. If one already exists for this environment and recent timeframe, call `noop` with a brief explanation."
- **Our assessment**: This is a distinct third dedup mechanism beyond the two the corpus already documents: `docs-ghaw-monitoring-patterns.md` Claim 5 covers `group-reports: true` (aggregating many failure reports as sub-issues under one shared parent, capped at 64), while `docs-ghaw-agentic-ops.md` Claim 8 and `docs-ghaw-cost-management.md` Claim 5 cover `close-older-issues: true` paired with a short `expires` window (there, for periodic audit/optimizer reports) and `skip-if-match` as a pre-activation cost-avoidance filter (there, framed purely as a cost control), respectively. `deployment-incident-monitor` combines all three techniques — trigger-level `skip-if-match` (which `docs-ghaw-cost-management.md` Claim 5 already names as "the highest-leverage cost-reduction strategy" because it avoids inference cost entirely), an in-prompt LLM-instructed duplicate check (a semantic check the deterministic `skip-if-match` label query cannot fully replace, since it also reasons about "this environment and recent timeframe"), and `close-older-issues`/`expires` at the safe-output layer — into one workflow, which is new to the corpus as a worked example of defense-in-depth deduplication rather than relying on any single mechanism. For Ch06 (Agentic Operations): document this three-layer dedup design (trigger-level skip, in-prompt semantic check, safe-output-layer close-older-issues) as the recommended pattern for any event-triggered incident/alerting workflow, citing `docs-ghaw-cost-management.md` Claim 5 for the `skip-if-match` cost rationale and `docs-ghaw-monitoring-patterns.md` Claim 5 for the alternative `group-reports` aggregation approach used by fleet-wide failure reporters — and note these are different tools for different shapes of duplicate-suppression problem (one evolving incident thread vs. many aggregated failure reports).

### Claim 16: On September 19, 2026, `deployment-incident-monitor` correctly diagnosed a `Smoke Copilot - AOAI (Entra)` workflow failure as a provider-side Azure OpenAI organization-verification requirement rather than a code regression, by tracing the failure to the most recent commit and confirming that commit did not touch the failing path, then filing issue #61892 with a full evidence trail
- **Evidence**: Blog post prose plus the live filed issue, fetched via `gh issue view 61892 --repo github/gh-aw --json body,state`.
- **Confidence**: settled (blog framing corroborated directly against the live, first-party incident issue body)
- **Quote**: "This was its busiest week yet, firing 19 times — more runs than any other workflow in the repo... on September 19th it caught a real one: the `Smoke Copilot - AOAI (Entra)` workflow started failing with a `400` error because Azure OpenAI required organization verification for reasoning summaries. The agent didn't just flag the failure — it traced it back to the exact commit, confirmed the change wasn't the culprit, and filed issue #61892 with a full evidence trail linking the failing run and deployment." From the filed issue itself: "The Copilot CLI harness (`copilot-harness`) exhausted all 3 retries (4 total attempts) invoking the model backend, and every attempt returned the same upstream `400` error... `400 Your organization must be verified to generate reasoning summaries...`" / "This is a provider/account configuration issue on the model backend side... not a regression introduced by a recent code change in this repository. The most recent commit on `main` prior to the failure (`9894316e`,... #61774) does not touch inference routing, Copilot harness, or AOAI/Entra configuration."
- **Our assessment**: This is a concrete, verified example of an LLM-driven monitoring agent performing negative diagnosis correctly — actively ruling out "our own recent change caused this" by naming the specific preceding commit and stating what it did and did not touch, rather than either assuming code-side blame by default or vaguely attributing the failure to "unknown causes." The agent's evidence trail (retry count, exact upstream error message, failing run link, deployment link, and the ruled-out commit) is exactly the kind of structured incident triage a human on-call engineer would be expected to produce, and it was produced automatically within the workflow's 10-minute timeout. This is the single most concrete, independently-verifiable "agent did real diagnostic work correctly" example in this week's post, as opposed to the mostly-infrastructure/tooling fixes in Claims 2–14. For Ch04/Ch06 (Agentic Operations): cite this specific, dated, independently-verified incident (issue #61892) as a worked example of automated root-cause triage that includes active exculpation of recent code changes — not just failure detection, but a documented reasoning chain for why the failure is *not* attributable to the repository's own recent history.

## Concrete Artifacts

### `printf`-pipe safe-output failure reproduction (PR #61427, fetched via `gh pr view 61427 --repo github/gh-aw`)

```console
$ printf '{"message":"no action needed"}' safeoutputs noop .   # CLI never runs
{"message":"no action needed"}
$ echo $?
0
```
*Source: PR #61427 body, reproduction of the pre-fix bug.*

### Imported-engine-config-loss example (PR #61424, fetched via `gh pr view 61424 --repo github/gh-aw`)

```yaml
# shared/engine.md
engine:
  id: claude
  auth:
    type: github-oidc
    provider: anthropic
    federation-rule-id: fr_01ABC
---
# workflow.md — adding `model:` dropped AWF_AUTH_* entirely
imports:
  - shared/engine.md
model: claude-sonnet-4-5
```
*Source: PR #61424 body, pre-fix reproduction.*

### `experiments.<name>` invalid GitHub Actions expression (PR #61599, fetched via `gh pr view 61599 --repo github/gh-aw`)

```yaml
ANTHROPIC_MODEL: ${{ experiments.model }}   # invalid — not a GH Actions context
```
*Source: PR #61599 body, pre-fix reproduction.*

### `deployment-incident-monitor.md` frontmatter (live workflow file, fetched via `gh api repos/github/gh-aw/contents/.github/workflows/deployment-incident-monitor.md`)

```yaml
private: true
emoji: "🚨"
description: Monitors deployment failures and automatically creates deduplicated incident issues with root cause analysis.
on:
  deployment_status:
    state: [error, failure]
  skip-if-match: "is:issue is:open label:incident label:deployment-failure"
permissions:
  contents: read
  actions: read
  deployments: read
engine:
  id: copilot
  copilot-sdk: true
max-tool-denials: 3
imports:
  - shared/mcp-pagination.md
  - shared/reporting.md
  - shared/otlp.md
features:
  gh-aw-detection: true
tools:
  cli-proxy: true
  github:
    mode: gh-proxy
    toolsets: [repos, actions]
safe-outputs:
  create-issue:
    expires: 7d
    title-prefix: "[Incident] "
    labels: [incident, deployment-failure]
    close-older-issues: true
  noop:
timeout-minutes: 10

evals:
  - id: incident-or-noop
    question: Did the agent either create an incident issue or call noop?
  - id: root-cause-included
    question: Does the agent output include a root cause analysis or a reason for the noop decision?
  - id: dedup-respected
    question: Does the agent output show that it checked for an existing open incident issue before creating a new one?
```
*Source: `.github/workflows/deployment-incident-monitor.md` in `github/gh-aw` at the current default branch. Note the `evals:` frontmatter key — a list of natural-language grading questions with `id`/`question` fields — is a distinct mechanism from the deterministic built-in `graders:` block `docs-ghaw-graders.md` documents; no existing source note in this corpus covers `evals:` blocks, so this is flagged as new-to-corpus rather than cross-referenced.*

### `Code Scanning Fixer` allowed shell helpers (PR #61605, fetched via `gh pr view 61605 --repo github/gh-aw`)

```yaml
bash: ["cat:*", "git diff:*", "git restore:*", "git status:*", grep, "head:*", jq, ls, "sed:*", tail, wc]
```
*Source: PR #61605 body, "Allowed local inspection tools."*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claim 8 (`create-issue` with `expires: 3d`/`7d` plus `close-older-issues: true` for `copilot-token-audit`/`copilot-token-optimizer`): Claim 15 here shows `deployment-incident-monitor` using the identical `expires: 7d` + `close-older-issues: true` combination, a third corpus instance of this exact `create-issue` configuration for a monitoring workflow.
  - `blog-ghaw-weekly-2026-06-29.md` Claim 4 (named `gh-aw-mcpg`/`gh-aw-firewall` version bumps, v0.3.31→v0.3.32 and v0.27.12→v0.27.13) and `docs-ghaw-enclaves.md` Claim 12 (minimum versions AWF v0.28.9, mcpg v0.4.13 for `issues-read-v1`) and `blog-ghaw-weekly-2026-09-07.md` Claims 2 and 12 (AWF v0.28.13+, mcpg v0.4.16 floors): Claim 6 here (mcpg v0.4.23→v0.4.25, AWF v0.28.16→v0.28.17→v0.28.20) is a further, later instance of the same recurring dependency-version-bump pattern and continues the climbing-version-floor trend those notes already document.
  - `docs-ghaw-graders.md` Claim 9 (grading as one shared preprocessing pass every enabled grader reuses): Claim 7 here is a concrete, dated bug report confirming that shared pass previously had a real coverage gap for native Copilot tool calls.

- **Contradicts**: None found at the MINER.md §4a threshold. This release is exclusively bug fixes, efficiency improvements, and version bumps; no claim here opposes an existing source note's claim in a way that would lead the guide toward different advice.

- **Extends**:
  - `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` as "the highest-leverage cost-reduction strategy," framed around avoiding inference cost) and `docs-ghaw-monitoring-patterns.md` Claim 5 (`group-reports: true` failure aggregation, capped at 64 sub-issues): Claim 15 here shows a third, distinct deduplication mechanism (trigger-level `skip-if-match` + in-prompt semantic check + `close-older-issues`) applied together for an incident-monitoring use case, extending both notes' single-mechanism framings into a documented defense-in-depth combination.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 9, `blog-ghaw-weekly-2026-08-24.md` Claim 5, and `blog-ghaw-weekly-2026-09-07.md` Claims 3 and 6 (the recurring "agent run completes without honestly reflecting what happened" failure class): Claim 8 here (the `safeoutputs` CLI's `printf`-pipe silent-no-op bug) is a fifth dated instance of the same failure class, and Claim 12 here (CRLF slash-command silent activation failure) and Claim 9 here (silent OIDC→API-key auth downgrade) are two further, distinct instances of the same "silently wrong, not visibly broken" shape applied to different subsystems (trigger activation, authentication resolution).
  - `blog-ghaw-weekly-2026-08-24.md` Claim 4 (`gh aw models` CLI for auditing fleet-wide model/catalog drift): Claim 5 here (the daily model-inventory checker finding a ~100x pricing error) is a further, automated instance of the same catalog-drift-detection theme, naming a scheduled/automated process rather than an on-demand CLI audit.
  - `blog-ghaw-ai-credits-migration.md` Claim 1 (AIC as the primary gh-aw spend metric, 1 AIC = $0.01 USD): Claim 10 here (the three AIC accounting gap fixes) is a dated instance of hardening the guardrail infrastructure built on top of that metric, five months after its introduction.

- **Novel**:
  - **The `deployment-incident-monitor` three-layer deduplication design** (Claim 15): the first corpus example combining trigger-level `skip-if-match`, an in-prompt LLM-instructed duplicate check, and safe-output-layer `close-older-issues` in a single workflow, rather than relying on any one mechanism alone.
  - **A verified, independently-checked example of correct automated negative diagnosis** (Claim 16): the agent actively ruled out a specific named commit as the cause of a failure, rather than merely detecting and reporting the failure — the first corpus instance of this specific "exculpation" reasoning pattern being independently confirmed against the actual filed issue body.
  - **A ~100x model-pricing error in the gh-aw cost catalog, caught by an automated daily inventory checker** (Claim 5): first corpus documentation both of a concrete pricing-catalog error of this magnitude and of a named automated (not just on-demand CLI) catalog-drift-detection process.
  - **A silent OIDC-to-API-key authentication downgrade caused by a configuration-merge bug** (Claim 9): first corpus documentation of this specific failure interaction between `imports:`-inherited engine auth and a top-level `model:` override.
  - **The `evals:` frontmatter block** (Concrete Artifacts): a natural-language grading-question mechanism distinct from the deterministic `graders:` spec `docs-ghaw-graders.md` documents in detail — flagged as new-to-corpus and unverified beyond this one workflow file, not yet corroborated by any dedicated documentation source.

## Guide Impact

- **Chapter 06 (Agentic Operations)**:
  - Document the `deployment-incident-monitor` three-layer deduplication design (Claim 15) as the recommended pattern for event-triggered incident/alerting workflows, contrasted with `docs-ghaw-monitoring-patterns.md`'s `group-reports` aggregation pattern for a different duplicate-suppression shape (many failures under one parent vs. one evolving incident thread).
  - Cite issue #61892 (Claim 16) as a concrete, verified example of automated root-cause triage that actively rules out recent code changes as the cause — a reasoning pattern worth naming explicitly when documenting what "good" automated incident response looks like.
  - Add the fifth-through-seventh dated instances of the "silently wrong, not visibly broken" failure class (Claims 8, 9, 12) to the running list already tracked from prior weekly notes, now spanning safe-output CLI invocation, engine-config/auth resolution, and trigger activation.
  - Cite the three-PR AIC accounting hardening sequence (Claim 10) as a worked example of safely relaxing a fail-closed guardrail via narrow, evidence-gated exceptions.
  - Note the ~100x `gpt-6-astra` pricing catalog error (Claim 5) as a caution that AIC/cost dashboards built on `models.json` are not infallible, and cite the automated daily inventory-checker as the detection mechanism.

- **Chapter 06 (Security and Threat Model)**:
  - Flag the silent OIDC→API-key authentication downgrade bug (Claim 9) as a caution: engine/auth configuration inherited via `imports:` should be verified as actually applied whenever a workflow also sets any top-level engine-adjacent field.
  - Update the running list of named enclave minimum-version gate constants to include `AWFEnclaveAgentToolsMinVersion` (Claim 6), alongside the already-tracked `MCPGDynamicRepositoryDelegationMinVersion`/`AWFDynamicRepositoryEnclaveMinVersion`.

- **Chapter 02 (Harness Engineering)**:
  - Cite the `Code Scanning Fixer` allowed-shell-helpers fix (Claim 11) as a reusable template for right-sizing a `bash:` tool allowlist for large-output triage tasks, reducing tool-denial churn without loading large content into context.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with BeautifulSoup**, following the
   practice established in prior weekly notes (e.g. `blog-ghaw-weekly-2026-09-07.md`
   Extraction Note 1). An initial WebFetch pass was attempted first and refused to
   reproduce verbatim text, citing a copyright-driven per-quote character limit;
   the raw-HTML extraction was used instead for all `Quote` fields, and all quotes
   above are copied character-for-character from that extraction, not from any
   WebFetch summary.

2. **All PRs named or linked in the post were independently fetched** via
   `gh pr view <N> --repo github/gh-aw --json title,body,url`: #61871, #61027,
   #60951 (the three "Faster, smarter logs auditing" PRs), #61234 (model
   catalog), #61661, #61527, #60945 (the three "MCP Gateway and firewall
   bumped" PRs), #61426 (grading), #61605, #61602, #61427, #61424, #61313,
   #61232, #61222 (the five "Bug Fixes & Improvements" bullets, covering
   seven PRs total), and #61430, #61599 (the two "Notable Pull Requests" not
   already named in "What's New"). PR numbers for the "Notable Pull Requests"
   section were recovered from the raw HTML's anchor `href` attributes, since
   that section's visible prose does not print PR numbers — confirmed by
   locating the anchor text ("Fix Copilot SDK multiword shell prefix matching
   and denial-guard hang," "Rewrite `experiments.<name>`...") directly
   adjacent to each `pull/<N>` href.

3. **Agent of the Week claims independently verified against live, non-blog
   sources**: the `deployment-incident-monitor.md` workflow file was fetched
   directly via `gh api repos/github/gh-aw/contents/...` (Claim 15's
   Concrete Artifact), and the filed incident issue #61892 was fetched via
   `gh issue view 61892 --repo github/gh-aw --json body,state` (Claim 16).
   Both confirmed the blog's prose framing without contradiction. This is a
   deeper verification pass than prior weekly notes typically apply to the
   Agent of the Week section, undertaken because the Prospector's triage
   comments flagged this release as otherwise low-novelty — the Agent of the
   Week section turned out to be the most independently verifiable and
   substantive part of the post.

4. **Cross-reference check performed** against `docs-ghaw-cost-management.md`,
   `docs-ghaw-monitoring-patterns.md`, `docs-ghaw-agentic-ops.md`,
   `docs-ghaw-graders.md`, `docs-ghaw-enclaves.md`, `blog-ghaw-ai-credits-migration.md`,
   `blog-ghaw-weekly-2026-09-07.md`, and `blog-ghaw-weekly-2026-06-29.md`, all
   re-read in full (not skimmed) before writing Cross-References, plus
   `CONTRADICTIONS.md` for existing entries. No claim in this source meets the
   MINER.md §4a bar for a new contradiction filing — this release is
   exclusively hardening/maintenance work consistent with the corpus's
   existing documentation of the same subsystems. All `Claim N` citations
   above were verified against the actual numbered claims in the cited notes
   at the time of writing, per MINER.md §4b.

5. **Three triage comments were left on the source issue** by the Prospector,
   with somewhat different novelty assessments (two rated "high," one rated
   "low," the "low" comment being the most recent and most specific about
   this release being "primarily maintenance and incremental improvements
   rather than novel patterns"). This note's `confidence_overall: settled`
   reflects that every individual claim is a settled, shipped, first-party
   bug fix or version bump — there is no "emerging" architectural feature in
   this release comparable to the September 7 update's dynamic enclave
   delegation. Novelty (how new the *pattern* is to the corpus) and
   confidence (how well-supported each *claim* is) are graded independently
   here: several claims (5, 8, 9, 15, 16) are novel to the corpus despite the
   release's overall low architectural novelty.
