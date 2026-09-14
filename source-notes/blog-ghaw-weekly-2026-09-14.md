---
source_url: https://github.github.com/gh-aw/blog/2026-09-14-weekly-update/
source_type: blog-post
title: "Weekly Update – September 14, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-09-14
date_extracted: 2026-09-14
last_checked: 2026-09-14
status: current
confidence_overall: emerging
issue: "#3430"
---

# Weekly Update – September 14, 2026 (GitHub Agentic Workflows)

> Seventeen releases (v0.88.5→v0.89.12) shipped MCP-tool-call log identity,
> a `gh aw logs` cache-refresh and run-exclusion pair, a custom-engine
> threat-detection fix, and a week-long credential-persistence-reduction
> push across generated checkout steps — but the post's own "Agent of the
> Week" reliability narrative for `cli-version-checker` does not survive an
> independent check against the GitHub Actions API: the three most recent
> runs before publication contain one failure, not the two the post
> describes, and no run in that window lasted "5.6 minutes."

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; an intro paragraph, a "Release: v0.89.0" section
  with "What's New" (4 bullets) and "Bug Fixes & Improvements" (3 bullets)
  subsections, a "Release: v0.89.12" section (2 bullets), a "Notable Pull
  Requests" section (5 bullets), an "Agent of the Week: CLI Version Checker"
  spotlight, and a "Try It Out" closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The on-page byline names the
  author as "Copilot" — the same non-human byline pattern documented in
  every prior weekly note in this corpus (e.g. `blog-ghaw-weekly-2026-09-07.md`).
  Every PR named or linked in the post was independently fetched via `gh pr
  view <N> --repo github/gh-aw --json title,body,url,state,mergedAt` to
  corroborate the blog's one-line summaries against first-party PR
  descriptions, and the "Agent of the Week" workflow's own recent run
  history was independently pulled from the GitHub Actions API — see
  Extraction Notes for the full method and what it found.
- **Scope**: One "Release: v0.89.0" section naming seven PRs (four "What's
  New," three "Bug Fixes & Improvements"), one "Release: v0.89.12" section
  naming two more PRs, one "Notable Pull Requests" section naming six more
  PRs, and one "Agent of the Week" spotlight on `cli-version-checker`
  (linking to the live workflow file but naming no PRs). Does NOT cover: a
  full v0.89.x changelog page (none is linked; PR links are the only
  citations, consistent with every prior weekly note in this corpus); the
  other ~15 releases between v0.88.5 and v0.89.0 not named in either
  "Release" section; or any log/transcript data for `cli-version-checker`'s
  cited "~40K tokens" / "26 GitHub API calls" figures, which this note could
  not independently verify (see Claim 15).

## Extracted Claims

### Claim 1: PR #59579 makes `gh aw logs --json` record a timestamp, server name, and tool name for every MCP tool call, mapped into a new `mcp_tool_usage.tool_calls` field, without exposing call arguments, results, or gateway identifiers
- **Evidence**: PR #59579 description ("Expose identifiable MCP tool calls in logs JSON"), fetched via `gh pr view 59579 --repo github/gh-aw`, including a JSON example.
- **Confidence**: settled (specific PR, specific new field path, first-party description of what is and is not captured)
- **Quote**: "Compact usage artifacts omitted MCP call identity, leaving `gh aw logs --json` consumers unable to determine which server and tool produced each call." / "Record timestamp, server name, and tool name for each MCP call. Retain synthetic call IDs without exposing arguments, results, or gateway identifiers." / "Map the new fields into `mcp_tool_usage.tool_calls`."
- **Our assessment**: This directly extends `docs-ghaw-audit-reference.md` Claim 6, which documents `gh aw logs` as the cross-run aggregate report command (domain inventory, metrics trends, MCP server health) but does not describe per-call identity within that output — before this fix, a `gh aw logs --json` consumer could see that an MCP call happened but not which server or tool produced it. The explicit exclusion of arguments/results/gateway identifiers from the new fields is a deliberate privacy/security boundary: identity is now traceable, but call payloads and internal gateway addressing are not. For Ch04 (Agentic Operations): update `gh aw logs` observability documentation to note that `--json` output now carries per-MCP-call server/tool identity, enabling per-tool usage audits that were previously only inferable from aggregate counts.

### Claim 2: PR #59697 adds `--ignore-workflow-runs` to `gh aw logs`, accepting comma-separated or repeated numeric run IDs or qualified `slug/ID` values, to exclude specific runs from log collection without reducing the requested result count
- **Evidence**: PR #59697 description ("Add workflow run ignore list to logs"), fetched via `gh pr view 59697 --repo github/gh-aw`, including a CLI usage example.
- **Confidence**: settled (specific PR, specific flag syntax and input formats, first-party description)
- **Quote**: "`gh aw logs` could not exclude known workflow runs from collection. Add `--ignore-workflow-runs` to omit specific runs without reducing the requested result count." / "Accept numeric IDs and qualified `slug/ID` values. Support comma-separated and repeated entries. Reject invalid or non-positive IDs." / "Filter ignored runs before artifact processing. Preserve ignored IDs in pagination continuations."
- **Our assessment**: The "without reducing the requested result count" behavior is the operationally significant detail: a practitioner who wants "the last 10 healthy runs" for a trend report (the pattern `docs-ghaw-monitoring-patterns.md` Claim 9 documents for `gh aw logs --format markdown`) previously had no way to skip a known-bad or known-irrelevant run (e.g., a manual `workflow_dispatch` test run) without the count silently shrinking by one for each excluded run. This flag makes exclusion additive rather than count-reducing — the collector keeps pulling until it has the requested count of non-ignored runs. For Ch04 (Agentic Operations): document `--ignore-workflow-runs` as the mechanism for excluding known-noise runs (manual test dispatches, known-broken runs under active investigation) from trend/aggregate reports without skewing the sample size.

### Claim 3: PR #59690 makes `gh aw logs --cached-json` overwrite the supplied cache file with the combined cached-and-newly-processed response after every successful collection, instead of leaving the cache file stale once written
- **Evidence**: PR #59690 description ("Refresh cached logs JSON in place"), fetched via `gh pr view 59690 --repo github/gh-aw`, including a shell usage example.
- **Confidence**: settled (specific PR, first-party description of prior vs. fixed cache-write behavior)
- **Quote**: "`gh aw logs --cached-json` reused compatible run records but left the cache file stale. The command now replaces it with the updated logs response after each successful collection." / "Reuse only completed runs with matching repository, attempt, conclusion, and update timestamp. Fall back to artifact processing when cached data cannot satisfy requested filters." / "Overwrite the supplied cache with the combined cached and newly processed response."
- **Our assessment**: Before this fix, `--cached-json` was read-mostly: it consumed the cache to avoid redundant artifact fetches but never wrote fresh results back, so the cache would drift further out of date with each run until manually regenerated. This is the same class of fix as PR #60702 (Claim 11, wildcard cached-logs files, shipped the same week) — both are cache-hygiene fixes to the `gh aw logs` caching subsystem, landing in the same release cycle. For Ch04: when documenting `gh aw logs` caching flags, note that `--cached-json` is now both the cache input and the refreshed output — a single flag serves both roles, which was not true before this fix.

### Claim 4: PR #59711 adds `gpt-6-astra` to gh-aw's model alias resolution and pricing catalogs for GitHub Copilot and OpenAI, including it in the `large` and `agent` alias-resolution chains, in response to the model already being live in both providers' inventories
- **Evidence**: PR #59711 description ("Add GPT-6 Astra model inventory support"), fetched via `gh pr view 59711 --repo github/gh-aw`, including a JSON alias snippet. The PR closes issue #59709.
- **Confidence**: settled (specific PR, specific alias-chain and catalog changes, first-party description)
- **Quote**: "`gpt-6-astra` is live in Copilot and OpenAI inventories but was absent from model aliases and pricing metadata. This adds it to flagship fallback selection and cost accounting." / "Add `gpt-6` provider patterns. Include it in `large` and `agent` resolution chains." / "Add `gpt-6-astra` costs to GitHub Copilot and OpenAI catalogs. Keep `actions/setup/js/models.json` synchronized with the CLI catalog."
- **Our assessment**: This is the same recurring "gh-aw's own model catalog trails live provider releases" maintenance pattern already tracked in the corpus for `gpt-5.4`-variant drift (`blog-ghaw-weekly-2026-09-07.md` Claim 14; `blog-ghaw-weekly-2026-08-24.md` Claim 4's `gh aw models` CLI, built to audit exactly this class of drift) — here one generation newer (GPT-6 Astra rather than a GPT-5.x variant), and this time the fix is proactive catalog registration rather than a reactive per-workflow model-string swap. The dual catalog sync (`actions/setup/js/models.json` kept in lockstep with the CLI's own pricing catalog) is a previously undocumented detail: gh-aw's model/pricing metadata exists in at least two places that must stay synchronized by hand (or by this kind of PR) rather than a single source of truth. For Ch06 (Cost Management): note that gh-aw's model catalog requires a dedicated PR per newly-available flagship model, and that the catalog is duplicated between the CLI and the `actions/setup/js` package rather than centralized.

### Claim 5: PR #59636 fixes threat detection reporting `config_error` for every custom-engine workflow with safe outputs by generalizing engine-ID normalization to any non-built-in engine, and adds a new `detection-engine` frontmatter key so an engine definition can declare its own working detection default
- **Evidence**: PR #59636 description ("Fix threat detection config_error for workflows using custom engines"), fetched via `gh pr view 59636 --repo github/gh-aw`, including a YAML frontmatter example and a compiler warning message.
- **Confidence**: settled (first-party bug description with the exact prior failure mode, the exact fix, and a stated precedence order)
- **Quote**: "Threat detection passed the workflow's own engine ID to `threat-detect --engine`, which only accepts built-in engines. Every run of a custom-engine workflow with safe outputs ended with `THREAT_DETECTION_STATUS: reason=config_error`, and because the detection job is `continue-on-error`, the run stayed green with safe outputs applied and no analysis performed." / "Precedence: `safe-outputs.threat-detection.engine` > engine definition `detection-engine` > `copilot`." / "warning: Threat detection does not support the custom engine \"pydantic-ai\", so it runs on the built-in \"copilot\" engine instead, which requires that engine's credentials."
- **Our assessment**: This is a direct, concrete extension of `docs-ghaw-threat-detection.md` Claim 8, which documents the `engine` field's string/object/`false` type signature but records (as `emerging` confidence) that "the specific model names accepted as strings... are not elaborated." This PR reveals the actual failure surface that documentation didn't cover: an engine ID that isn't one of threat detection's built-in engines was previously passed through unnormalized, causing every custom-engine workflow with safe outputs to silently skip AI threat analysis while still reporting a green run — because the detection job is `continue-on-error`, exactly the same "green run, but the safety gate didn't actually run" failure shape as `blog-ghaw-weekly-2026-09-07.md` Claim 3 documented for DIFC guard-policy generation gaps (there: safe-output writes silently denied on a green run; here: threat detection silently skipped on a green run). The fix's own compile-time warning ("requires that engine's credentials") is a second, distinct issue this PR fixes: normalizing to `copilot` for detection could fail if the workflow doesn't hold Copilot credentials, so the compiler now surfaces this dependency at compile time rather than letting it fail at runtime. For Ch06 (Security and Threat Model): add `detection-engine` as a required frontmatter field for custom-engine authors, and flag that prior to this fix, custom-engine workflows with safe outputs configured were running with NO threat detection at all despite appearing to pass — a second dated instance of the "fail-secure gate that was actually silently fail-open due to a configuration gap" failure class.

### Claim 6: PR #59703 fixes the daily model-inventory job by pinning `@github/copilot-sdk` to 1.0.13 (up from 1.0.11), after 1.0.11 resolved an incompatible CLI platform package that prevented `CopilotClient` initialization entirely
- **Evidence**: PR #59703 description ("Fix Copilot SDK model inventory collection"), fetched via `gh pr view 59703 --repo github/gh-aw`.
- **Confidence**: settled (first-party bug description naming the exact dependency versions and the exact failure — client initialization, not a downstream call failure)
- **Quote**: "The daily model inventory job failed because Copilot SDK 1.0.11 resolved an incompatible CLI platform package, preventing `CopilotClient` initialization." / "Update `@github/copilot-sdk` from 1.0.11 to 1.0.13. Regenerate the compiled workflow lock file."
- **Our assessment**: This is a narrow but concrete instance of an npm dependency's own transitive resolution breaking an internal gh-aw automation job — the model-inventory job (the same general category of fleet-maintenance workflow that produces the `gh aw models` catalog referenced in Claim 4's cross-reference) failed at the client-construction step, before any model-inventory logic could run at all, due to a version of a first-party SDK dependency resolving an incompatible platform package. This is new to the corpus: no existing note documents a gh-aw internal tooling failure caused by the Copilot SDK's own dependency resolution rather than by gh-aw's own code. For Ch06 (Agentic Operations): note this as a concrete example that gh-aw's own maintenance/audit tooling (not just user-facing agentic workflows) is itself subject to upstream SDK dependency breakage, and requires the same kind of pinned-version discipline.

### Claim 7: PR #59602 bumps the bundled MCP gateway (`gh-aw-mcpg`) from a prior pinned version to v0.4.20 — which includes a safe-outputs sink-visibility exemption fix — and refreshes pinned container image digests in `actions-lock.json` and two generated `action_pins.json` files so compiled workflows stop referencing the previous gateway tag/digest
- **Evidence**: PR #59602 description ("Bump bundled MCP gateway to v0.4.20 and refresh pinned workflow image references"), fetched via `gh pr view 59602 --repo github/gh-aw`, including a Go constant snippet.
- **Confidence**: settled (specific PR, specific version bump, first-party description of the constant, pinned-metadata, and lock-file changes)
- **Quote**: "This updates `gh-aw` to use `gh-aw-mcpg v0.4.20`, which includes the safe-outputs sink-visibility exemption fix. It also refreshes pinned image metadata so compiled workflows stop carrying the previous gateway tag/digest." / "Updated `DefaultMCPGatewayVersion` to `v0.4.20` in `pkg/constants/version_constants.go`." / "Replaced the `ghcr.io/github/gh-aw-mcpg:v0.4.18` entry with `v0.4.20` in `.github/aw/actions-lock.json`."
- **Our assessment**: The PR body itself confirms the prior pinned version was v0.4.18. This continues the climbing-mcpg-version-floor trend `blog-ghaw-weekly-2026-09-07.md` Cross-References → Extends already tracked (that note's Claim 2 and Claim 12 cited AWF v0.28.13+ and mcpg v0.4.16 as newly-introduced minimums that week) — v0.4.20 is now the default for every newly-compiled workflow, a further step up from the v0.4.16 minimum for dynamic-enclave admission documented one week earlier. The "safe-outputs sink-visibility exemption fix" bundled into this version bump is named but not detailed in this PR's own body; this note cannot confirm what specific sink-visibility bug it addresses without fetching the `gh-aw-mcpg` v0.4.20 release notes directly (not done here — out of scope for a `github/gh-aw` PR-level fetch). For Ch06 (Security and Threat Model): update any documented minimum/default mcpg version references to v0.4.20 as of this release, and flag that the specific sink-visibility fix bundled in this bump is not yet documented in this corpus at the mechanism level.

### Claim 8: PR #60685 and PR #60650 are two distinct instances, shipped the same week, of gh-aw disabling `persist-credentials` on `actions/checkout` steps inside its own generated workflows — the central slash-command router (`.github/workflows/agentic_commands.yml`) and the auto-upgrade workflow (`agentic-auto-upgrade.yml`) — specifically because those generated jobs only need the working tree, not a persisted `GITHUB_TOKEN` in local git config
- **Evidence**: PR #60685 description ("Disable credential persistence on the agentic_commands router checkout") and PR #60650 description ("Disable persisted credentials in auto-upgrade checkout"), both fetched via `gh pr view <N> --repo github/gh-aw`, including a generated-YAML example and a named regression test for #60685.
- **Confidence**: settled (two specific PRs, first-party descriptions of the exact generated file, the exact `with:` field added, and — for #60685 — a named test asserting the full checkout block and that `persist-credentials: true` never appears in generated output)
- **Quote**: "The generated central slash-command router workflow (`.github/workflows/agentic_commands.yml`) checked out the repo without `persist-credentials: false`, leaving `GITHUB_TOKEN` in the local git config for the lifetime of the routing job. The router only needs the tree (it loads `actions/setup` scripts and dispatches), so persisted credentials are pure blast radius." (#60685) / "The generated auto-upgrade workflow should not retain repository credentials after checkout." (#60650) / "`TestGenerateCentralSlashCommandWorkflow_CheckoutDoesNotPersistCredentials` asserts the full checkout block (step name + pinned `uses` + `with`) and that `persist-credentials: true` never appears in the generated output." (#60685)
- **Our assessment**: This is new to the corpus — no existing source note documents `persist-credentials` as a gh-aw hardening dimension at all; `docs-ghaw-checkout-reference.md` documents the `checkout:` frontmatter field's shallow-fetch and PR-head-ref defaults (Claim 2) but says nothing about credential persistence. Two independent generated-workflow checkout steps got the identical fix in the same week — a router workflow and an auto-upgrade workflow, both first-party gh-aw-generated automation rather than user-authored agentic workflows — which the "Notable Pull Requests" section frames as "two more steps in a week-long push to shrink `GITHUB_TOKEN` exposure across generated automation checkouts," implying more than these two instances exist. The `#60685` regression test explicitly asserts the negative ("`persist-credentials: true` never appears") in addition to the positive, which is a stronger correctness bar than only testing the intended new behavior. For Ch06 (Security and Threat Model): add `persist-credentials: false` on generated-workflow checkout steps as a named, currently-in-progress hardening initiative — the blast-radius rationale ("the router only needs the tree... persisted credentials are pure blast radius") is a reusable principle for any CI job that checks out code but does not itself need to push, tag, or otherwise use git with the checked-out token.

### Claim 9: PR #60683, titled "[WIP] Fix failing GitHub Actions job Integration: CMD Tests" and credited by the blog with "restoring a green CI signal," was merged on 2026-09-13 with its title still literally reading "[WIP]" and its body still the original unedited auto-generated task-acceptance placeholder — despite that placeholder's own text promising to "keep this PR's description up to date" — and the actual merged change was a one-line, one-file diff
- **Evidence**: PR #60683 fetched via `gh pr view 60683 --repo github/gh-aw --json number,title,state,mergedAt,url,body`, showing `state: MERGED`, `mergedAt: 2026-09-13T20:07:29Z`, and a body unchanged from the initial task-acceptance template; `gh pr view 60683 --repo github/gh-aw --json additions,deletions,changedFiles` shows exactly 1 file changed, 1 addition, 1 deletion, in `cmd/gh-aw/argument_syntax_test.go`.
- **Confidence**: settled (state, merge timestamp, body content, and diff stats are all read directly from the GitHub API, not paraphrased from the blog)
- **Quote**: "Thanks for asking me to work on this. I will get started on it and keep this PR's description up to date as I form a plan and make progress." / "Fix the failing GitHub Actions job \"Integration: CMD Tests\" ... Check run ID: 103779641453"
- **Our assessment**: The blog's one-line summary ("Fixed the 'Integration: CMD Tests' CI job (#60683), restoring a green CI signal") is accurate as far as it goes — the PR did merge, and the diff (a one-line change to a test file) is consistent with a genuine, narrow test fix — but it is currently the *only* human-readable account of what changed and why anywhere in the corpus, since the PR's own title and body never progressed past the initial "I will get started" placeholder despite that placeholder explicitly promising an update. This is a new, concrete instance of the "agent-authored PR ships with a stale or non-descriptive title/body even after merge" pattern; unlike the blog-anchor-vs-PR-title discrepancy `blog-ghaw-weekly-2026-09-07.md` Extraction Note 3 found (a labeling mismatch between two different first-party texts), this is a single PR's own text failing to keep its own stated promise to itself. Per MINER.md §4a, this is not filed as a contradiction — it is one source's content being thin/stale against its own later state, not two independently-argued claims disagreeing. For Ch02 (Harness Engineering): when citing a merged PR as evidence for a specific technical claim, check whether the PR body actually describes the fix (as most PRs fetched for this note's other claims do) or is a stale auto-generated placeholder (as this one is) before treating the PR body as corroborating detail — here, only the diff itself, not the PR text, confirms what changed.

### Claim 10: PR #60702 adds trailing-prefix wildcard support to `gh aw logs --cached-logs` (e.g. `logs-*`), which loads all matching `*.jsonl` shards as the starting cache, writes new records to a uniquely-named new shard (Unix time plus random bytes), and in wildcard mode additionally prunes source cache files that contain only out-of-range dated run records
- **Evidence**: PR #60702 description ("Support wildcard cached logs files"), fetched via `gh pr view 60702 --repo github/gh-aw`, including a CLI usage example with read/write path annotations.
- **Confidence**: settled (specific PR, specific wildcard syntax constraint — trailing-prefix only — and specific file-naming/pruning rules, first-party description)
- **Quote**: "`gh aw logs --cached-logs` now supports prefix wildcard cache inputs, allowing runs to reuse all matching JSONL cache shards and write fresh data to a collision-resistant new shard." / "Accepts trailing prefix wildcards such as `logs-*`. Loads all matching `*.jsonl` files as the starting cache. Rejects non-trailing wildcard patterns." / "In wildcard mode, removes source cache files that contain only dated run records outside the requested range. Preserves files with metadata-only or otherwise non-prunable records."
- **Our assessment**: This is the third `gh aw logs` caching-subsystem fix in this same release window alongside Claims 2 and 3 (`--ignore-workflow-runs`, in-place `--cached-json` refresh) — together these three PRs form a coherent theme of hardening the logs-caching layer for practitioners who run `gh aw logs` repeatedly against a growing fleet (sharded cache files accumulating over time, needing merge/prune/refresh support rather than a single monolithic cache file). The "collision-resistant new shard" naming (Unix time plus random crypto bytes) implies concurrent or frequent invocations against the same cache prefix are an anticipated usage pattern, not an edge case. For Ch04 (Agentic Operations): document the sharded-cache-file pattern (`--cached-logs prefix-*`) as the recommended approach for teams running `gh aw logs` on a recurring schedule against a large or growing workflow fleet, replacing a single ever-growing cache file with periodically-pruned shards.

### Claim 11: PR #60663 configures Git's union merge driver for `*.jsonl` files in repo-memory checkouts (as a checkout-local, uncommitted Git attribute) so that concurrent workflow runs pushing to the same repo-memory branch no longer resolve conflicts by discarding the other side's added rows
- **Evidence**: PR #60663 description ("Preserve JSONL rows during repo-memory merge conflicts"), fetched via `gh pr view 60663 --repo github/gh-aw`, including a `.gitattributes` snippet.
- **Confidence**: settled (first-party bug description with the exact prior behavior — local-wins conflict resolution discarding remote rows — and the exact fix mechanism)
- **Quote**: "Concurrent repo-memory pushes previously resolved every conflict with the local version, potentially discarding remotely added `.jsonl` rows." / "Configure Git's union merge driver for `*.jsonl`. Preserve rows added by both concurrent workflow runs." / "Store the policy in checkout-local Git attributes so it is not committed. Retain local-wins resolution for non-JSONL files."
- **Our assessment**: This is a concrete, previously-undocumented data-loss bug in gh-aw's repo-memory mechanism: two workflow runs appending different rows to the same `.jsonl` memory file concurrently would previously have one run's additions silently discarded by local-wins conflict resolution — a form of lost-update race condition specific to the repo-memory persistence layer. The fix is scoped precisely (only `*.jsonl`, only as an uncommitted checkout-local attribute, non-JSONL files keep local-wins) rather than broadening union-merge to all files, which would risk different kinds of merge corruption for non-append-only file types. For Ch04 (Agentic Operations): when documenting the repo-memory feature, note that concurrent-write row loss was a real, fixed bug — teams running multiple workflows that write to a shared repo-memory `.jsonl` file concurrently should confirm they are on a `gh-aw` version that includes this fix (or later).

### Claim 12: PR #60452 lets `gh aw update` reapply an installed package (not just a named workflow) when given the package's identifier or GitHub URL, matching against `.github/aw/packages` ownership records, restoring missing package workflows and reporting package-like targets that are not installed, while preserving custom workflow directories and engine-specific skill/agent locations
- **Evidence**: PR #60452 description ("Add package-aware targets to `gh aw update`"), fetched via `gh pr view 60452 --repo github/gh-aw`, including two CLI usage examples.
- **Confidence**: settled (specific PR, first-party description of the prior every-argument-is-a-workflow-name limitation and the new package-resolution behavior)
- **Quote**: "`gh aw update` previously treated every argument as a workflow name. It can now reapply an installed package when given its package identifier or GitHub URL." / "Match package identifiers and GitHub URLs against `.github/aw/packages` ownership records. Report package-like targets that are not installed." / "Update all workflows and assets owned by the selected package. Restore missing package workflows. Preserve custom workflow directories and engine-specific skill and agent locations. Exclude non-workflow Markdown assets from workflow reconciliation."
- **Our assessment**: This is a companion fix to `blog-ghaw-weekly-2026-09-07.md` Claim 4 (`gh aw add`'s `aw.json` package-settings deep-merge behavior) — both PRs extend package-level operations beyond the individual-workflow model the `gh aw` CLI originally assumed, here for `update` specifically rather than `add`. The "restore missing package workflows" behavior is notable: it implies `gh aw update <package>` can recover from a practitioner having manually deleted one of a package's workflow files, re-materializing it from the package definition rather than only refreshing files that still exist locally. For Ch02 (Harness Engineering): document `gh aw update <package-id-or-url>` as the package-level reconciliation command, distinct from `gh aw update <workflow-name>`, and note it can restore accidentally-deleted package-owned workflow files.

### Claim 13: PR #60061 pinned three mutable-tag `uses:` references (two `actions/checkout`, one `actions/setup-go`) in `github/gh-aw`'s own hand-authored CI workflow files to immutable commit SHAs, and separately added a `github-actions` Dependabot ecosystem entry with weekly updates and a 7-day cooldown before newly-published action releases are applied
- **Evidence**: PR #60061 description ("Pin GitHub Actions to commit SHAs"), fetched via `gh pr view 60061 --repo github/gh-aw`, including a summary metrics table and a before/after pinned-refs table.
- **Confidence**: settled (specific PR, specific file:line locations, specific before/after `uses:` values, first-party description of the Dependabot cooldown addition)
- **Quote**: "Pins GitHub Actions `uses:` references in `github/gh-aw` to immutable commit SHAs." / "Pinning actions to full commit SHAs prevents future tag or branch retargeting from changing workflow behavior without review." / "Added a `github-actions` entry (weekly updates, 7-day cooldown) to the existing Dependabot configuration. The cooldown delays applying a newly published action release for 7 days, reducing exposure to a compromised or broken release while keeping you SHA-pinned." / "Branch refs were allowed and pinned to their current HEAD; review mutable-branch pins carefully."
- **Our assessment**: `docs-ghaw-compilation-process.md` Claim 6 documents that gh-aw's *compiler* automatically pins every action reference inside *compiled agentic workflows* to a commit SHA ("tags can be moved, SHAs cannot"), caching resolutions in `actions-lock.json`. This PR applies the identical rationale to a different surface entirely: `github/gh-aw`'s own three hand-authored CI workflow files (`error-message-lint.yml`, `publish-safe-outputs-node.yml`), which are not compiler output and were not covered by the compiler's automatic pinning at all — meaning the project's own build/lint CI had mutable tag references (`actions/checkout@v4`, `actions/setup-go@v5`, `actions/checkout@v7.0.0`) even while every agentic workflow it generates for others has been SHA-pinned by the compiler since that documented feature shipped. The added 7-day Dependabot cooldown is new to the corpus: it is a distinct supply-chain control from SHA pinning itself — pinning stops a tag from silently moving under you, while the cooldown adds a time buffer before *accepting* a newly-published release's SHA in the first place, giving a compromised-or-broken release a week to be caught and yanked upstream before this repo's Dependabot would propose adopting it. For Ch06 (Security and Threat Model): document the Dependabot release-cooldown pattern (delay adopting a newly-published dependency/action release by N days) as a complementary control to SHA pinning, distinct from and additive to it, and note that gh-aw's own hand-authored CI files were a gap in the project's otherwise-automatic SHA-pinning coverage until this PR.

### Claim 14: The "Agent of the Week" post accurately frames `cli-version-checker`'s terminal action as filing a `"[ca]"`-prefixed issue (not opening a pull request directly), and independently confirms the workflow's `expires: 2d` issue-expiry configuration and its broad tool/image coverage (Claude Code, GitHub Copilot CLI, MCP Gateway, and other tools, plus container-scanning utilities) against the live workflow source
- **Evidence**: Blog post "Agent of the Week" section prose, cross-checked against the live workflow source fetched today via `curl` from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/cli-version-checker.md`, which shows `safe-outputs: create-issue: {expires: 2d, title-prefix: "[ca] ", labels: [automation, dependencies, cookie], close-older-issues: true}` and no `create-pull-request` key anywhere in the file — identical to the configuration `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2 and Concrete Artifacts independently fetched from the same file five days earlier (2026-09-09).
- **Confidence**: settled for the mechanism (the `safe-outputs:` block was independently re-fetched today and matches both the blog's framing and the prior note's fetch); settled for the "2-day issue expiry" detail specifically
- **Quote**: "one clean 6.6-minute pass that filed its usual \"[ca]\"-prefixed update issue" / "Its self-imposed 2-day issue expiry is a nice touch: if nobody acts on a version bump quickly, the checker doesn't let stale \"you should upgrade\" nags pile up in the issue tracker forever."
- **Our assessment**: This is a notable, favorable contrast within the corpus's own coverage of this exact workflow: `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2 found that an *earlier* gh-aw blog post (the 2026-09-08 "Agent of the Day" profile of this same workflow) stated "when it finds one, it opens a pull request" — a claim that note showed does not survive a check against the live `safe-outputs:` configuration, which contains only `create-issue`. This week's post gets the mechanism right: it describes the terminal action as filing an issue, not opening a PR, and correctly names the 2-day expiry. Whether this is a deliberate correction (the Sep 8 note's finding informing later posts) or simply a different post using more careful language cannot be determined from either post's text alone. For Ch04 (Operations): when citing gh-aw "Agent of the [Day/Week]" framing for a workflow's terminal action, prefer the most recent post's framing and cross-check against the live `safe-outputs:` block, since accuracy has varied across posts about the identical workflow within the same two-week span.

### Claim 15: The post's claim that `cli-version-checker`'s "last three scheduled runs" this week showed "a genuinely mixed week" — one 6.6-minute success, one 49-second failure, and one additional 5.6-minute failure — does not match the three most recent runs verified via the GitHub Actions API, which contain only one failure, not two, and no run of either duration combination in that window
- **Evidence**: Independently fetched via `gh api repos/github/gh-aw/actions/workflows/195931538/runs` (workflow ID established in `blog-ghaw-agent-of-the-day-2026-09-08.md` Concrete Artifacts) and `gh api repos/github/gh-aw/actions/runs/<id>/jobs` for the specific runs, 2026-09-14. The three runs immediately preceding this post's publication date are: #557 (2026-09-13, success, 393s = 6.55 min — matches the post's "6.6-minute pass"), #556 (2026-09-12, failure, 49s — matches the post's "49 seconds," but job-level data shows the failure was in the `activation` job, 33 seconds, with `agent`/`detection`/`safe_outputs`/etc. all `skipped`, meaning the agent itself never ran rather than running and then failing), and #555 (2026-09-11, **success**, 584s = 9.73 min). No run with both a failure conclusion and a ~5.6-minute duration appears within the week preceding publication; the two runs matching "failure + ~5.6 minutes" by duration are #549 (2026-09-05, failure, 338s = 5.63 min) and #548 (2026-09-04, failure, 333s = 5.55 min) — 8–9 days before this post's publication date, and already the tail end of the seven-run losing streak `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 and Concrete Artifacts documented for this same workflow.
- **Confidence**: settled (run numbers, dates, conclusions, and durations are computed directly from GitHub Actions API `created_at`/`run_started_at`/`updated_at` and job-level `started_at`/`completed_at` timestamps, not paraphrased from the blog)
- **Quote**: "Over its last three scheduled runs this agent had a genuinely mixed week: one clean 6.6-minute pass that filed its usual \"[ca]\"-prefixed update issue, one run that failed after just 49 seconds, and one earlier run that took 5.6 minutes before also hitting trouble."
- **Our assessment**: This is a new instance of the same general failure class `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 first documented for this exact workflow — a gh-aw blog post's "last N runs" reliability framing not surviving an Actions-API check — but in the opposite direction from that prior finding. There, the blog's "two failed runs" *understated* a longer seven-run losing streak (the true picture was worse than stated). Here, the post's "genuinely mixed week... two runs hitting trouble" *overstates* the failure rate of the workflow's actual three most recent runs (only one of #555–#557 failed), and the specific "5.6 minutes" duration/failure combination it cites only matches runs from more than a week earlier — well outside any reasonable reading of "last three scheduled runs" as of a 2026-09-14 publication date. Two explanations are plausible and this note cannot distinguish between them from the available evidence: either the post's underlying data source queried a stale or differently-windowed run sample (e.g., three runs sampled by some criterion other than "three most recent," or fetched at an earlier point before #557 completed and never refreshed), or the "5.6 minutes" and second-failure figures were fabricated/hallucinated rather than sourced from a real run. Per MINER.md §4a, this is not filed as a contradiction — it is this source's own claim about its own subject's live artifact, the same category of gap established for this exact workflow by the immediately preceding note, not two independently-argued sources disagreeing. For Ch04 (Operations): when citing any gh-aw "Agent of the Day/Week" post's specific run-count, duration, or failure-rate figures for a spotlighted workflow, independently verify against `gh api repos/<owner>/<repo>/actions/workflows/<id>/runs` before repeating them — this is now the second documented instance, for the same specific workflow, of the blog's own reliability narrative not matching the Actions API, once understating and once (here) apparently overstating recent failures.

## Concrete Artifacts

### MCP tool call usage entry, new fields (PR #59579, fetched via `gh pr view 59579 --repo github/gh-aw`)

```json
{
  "timestamp": "2026-09-09T00:00:00Z",
  "server_name": "github",
  "tool_name": "issue_read",
  "status": "success"
}
```
*Source: PR #59579 body.*

### `gh aw logs --ignore-workflow-runs` usage (PR #59697 body)

```bash
gh aw logs --ignore-workflow-runs 123,github/gh-aw/456
```

### `gh aw logs --cached-logs` wildcard usage and shard naming (PR #60702 body)

```bash
gh aw logs --cached-logs .github/aw/logs/runs-*
# reads:  .github/aw/logs/runs-*.jsonl
# writes: .github/aw/logs/runs-<unix>-<random>.jsonl
```

### `detection-engine` frontmatter key and compiler warning (PR #59636 body)

```yaml
engine:
  id: pydantic-ai
  detection-engine: copilot   # copilot | claude | codex
  behaviors:
    # ...
```

```
warning: Threat detection does not support the custom engine "pydantic-ai", so it runs on the
built-in "copilot" engine instead, which requires that engine's credentials. Set
safe-outputs.threat-detection.engine to a built-in engine (or false to skip AI analysis), or
declare detection-engine in the engine definition.
```

### `persist-credentials: false` on the generated slash-command router checkout (PR #60685 body)

```yaml
    steps:
      - name: Checkout repository
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
```

### Repo-memory `.jsonl` union-merge Git attribute (PR #60663 body)

```gitattributes
*.jsonl merge=union
```

### `gh aw update` package-target usage (PR #60452 body)

```shell
gh aw update owner/package
gh aw update https://github.com/owner/package
```

### GitHub Actions SHA-pinning summary and pinned refs (PR #60061 body)

```
Files changed: 3 | Files scanned: 2 | Refs found: 3 | Refs pinned: 3 | Skipped: 0 | Warnings: 0 | Errors: 0

.github/workflows/error-message-lint.yml:23      actions/checkout@v4        -> actions/checkout@11d5960a326750d5838078e36cf38b85af677262
.github/workflows/error-message-lint.yml:28      actions/setup-go@v5        -> actions/setup-go@40f1582b2485089dde7abd97c1529aa768e1baff
.github/workflows/publish-safe-outputs-node.yml:32  actions/checkout@v7.0.0 -> actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0
```
*Source: PR #60061 body. Dependabot addition: `github-actions` ecosystem, weekly schedule, 7-day cooldown.*

### `cli-version-checker` run-history verification (independently fetched, `gh api repos/github/gh-aw/actions/workflows/195931538/runs` and `.../actions/runs/<id>/jobs`, 2026-09-14)

```
Run #  Date (2026)   Conclusion   Run duration      Notes
558    Sep 14        success      531s = 8.85min    (published same day as this post)
557    Sep 13        success      393s = 6.55min    matches post's "6.6-minute pass"
556    Sep 12        failure       49s = 0.82min    matches post's "49 seconds"; activation
                                                     job failed in 33s, agent job SKIPPED
555    Sep 11        success      584s = 9.73min    post implies this slot was a failure
549    Sep 05        failure      338s = 5.63min    matches post's "5.6 minutes" by duration,
                                                     but 9 days before publication
548    Sep 04        failure      333s = 5.55min    also close to "5.6 minutes," 10 days prior
```
*Source: GitHub Actions API, workflow ID 195931538 (established in `blog-ghaw-agent-of-the-day-2026-09-08.md`), fetched 2026-09-14.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-audit-reference.md` Claim 6 (`gh aw logs` as the cross-run
    aggregate report command): Claims 1–3 and 10 here are four dated
    improvements to that exact command's observability and caching surface,
    landing in the same release window.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2 and Concrete Artifacts
    (the `cli-version-checker` `safe-outputs: create-issue` configuration
    with `expires: 2d`, `title-prefix: "[ca] "`, `cookie` label — independently
    re-fetched today with an identical result): Claim 14 here confirms the
    same configuration five days later and notes this week's post frames the
    mechanism accurately (issue, not PR) where an earlier post about the same
    workflow did not.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 and its Concrete
    Artifacts run-history table (the same `cli-version-checker` workflow's
    prior seven-run losing streak, Aug 30–Sep 5, also found via independent
    Actions-API verification rather than trusting the blog's own framing):
    Claim 15 here is a second, independently-conducted Actions-API
    verification of a gh-aw blog post's reliability narrative for this exact
    workflow, using the identical methodology (`gh api
    .../actions/workflows/<id>/runs` and `.../runs/<id>/jobs`).
  - `blog-ghaw-weekly-2026-09-07.md` Claim 3 (the DIFC guard-policy
    generation gap causing safe-output writes to be silently denied on an
    apparently-green run): Claim 5 here (custom-engine threat detection
    silently skipped, also on a green run, due to `continue-on-error`) is a
    second, independent instance of the "fail-secure gate that was actually
    silently fail-open" failure shape, one week later.

- **Contradicts**: None found at the MINER.md §4a threshold. Claim 9 (the
  stale `[WIP]` PR body) and Claim 15 (the run-history mismatch) are both
  cases of this source's own claims not surviving a check against its own
  subject's live artifacts — the same precedent already established for this
  exact family of posts by `blog-ghaw-agent-of-the-day-2026-09-08.md`
  (Claims 2–4) and `blog-ghaw-weekly-2026-09-07.md` Extraction Note 3 — not
  two independently-argued sources disagreeing with each other.
  `CONTRADICTIONS.md` and open `contradiction`-labeled issues were checked
  (including #3285, unrelated to this post's content); no new filing meets
  the bar.

- **Extends**:
  - `docs-ghaw-threat-detection.md` Claim 8 (the `engine` field's
    string/object/`false` type signature, rated `emerging` confidence for
    lack of detail on specific engine-name handling): Claim 5 here provides
    exactly the missing detail — a specific failure mode (custom engine IDs
    passed unnormalized to `threat-detect --engine`) and the fix (a new
    `detection-engine` frontmatter key plus generalized normalization).
  - `docs-ghaw-compilation-process.md` Claim 6 (the gh-aw *compiler*
    automatically SHA-pins every action reference inside compiled agentic
    workflows): Claim 13 here shows the identical SHA-pinning rationale
    applied to a surface the compiler does not touch — `github/gh-aw`'s own
    hand-authored CI workflow files — closing a gap in what was otherwise
    automatic, fleet-wide coverage.
  - `blog-ghaw-weekly-2026-09-07.md` Claim 4 (`gh aw add`'s `aw.json`
    package-settings deep-merge behavior) and Cross-References → Extends
    (the climbing mcpg/AWF version-floor trend): Claim 12 here (`gh aw
    update`'s new package-aware targets) is a companion package-level
    operation for a different CLI subcommand, and Claim 7 here (mcpg bumped
    to v0.4.20, up from v0.4.18) is a further step in the same climbing-
    version-floor trend that note's Cross-References already tracked.
  - `blog-ghaw-weekly-2026-08-24.md` Claim 4 (`gh aw models`, built to audit
    fleet-wide model-catalog drift) and `blog-ghaw-weekly-2026-09-07.md`
    Claim 14 (three workflows needing `gpt-5.4`-variant model-string fixes):
    Claim 4 here (proactive GPT-6 Astra catalog registration) is the same
    drift-prevention theme one generation newer, this time addressed before
    any workflow broke rather than after.

- **Novel**:
  - **`persist-credentials: false` as an active, named gh-aw hardening
    initiative across its own generated-workflow checkout steps** (Claim 8):
    first corpus documentation of credential-persistence reduction as a
    security dimension gh-aw tracks at all; the Notable-PR section's own
    "week-long push" framing implies a broader in-progress effort beyond the
    two named instances.
  - **A second, opposite-direction Actions-API verification failure for the
    same spotlighted workflow within a two-week span** (Claim 15): the first
    instance (`blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3) found the
    blog understating a failure streak; this instance finds the blog
    apparently overstating recent failures using data that matches a run
    over a week stale — together these are evidence that this blog series'
    "recent run" framing for spotlighted agents should not be trusted without
    independent verification, in either direction.
  - **A merged, blog-cited PR whose title and body never progress past an
    unedited "I will get started" placeholder** (Claim 9): a new,
    independently-confirmed instance of agent-authored-PR documentation debt
    surviving all the way through merge.
  - **The Dependabot release-cooldown pattern** (Claim 13): a 7-day delay
    before adopting a newly-published action release, distinct from and
    additive to SHA pinning — not previously documented in this corpus as a
    supply-chain control.
  - **Repo-memory concurrent-write row loss and its union-merge-driver fix**
    (Claim 11): a previously undocumented data-loss bug class specific to
    the repo-memory persistence mechanism.

## Guide Impact

- **Chapter 06 (Security and Threat Model)**:
  - Add `detection-engine` as a required/recommended frontmatter field for
    custom-engine authors (Claim 5), and note that prior to this fix,
    custom-engine workflows with safe outputs configured ran with threat
    detection silently skipped while still reporting green — a second dated
    instance (after the Sep 7 DIFC gap) of a fail-secure gate being silently
    fail-open due to a configuration mismatch.
  - Add `persist-credentials: false` on checkout steps as a named hardening
    practice for any generated or hand-authored CI job that checks out code
    but does not need to push/tag with the checked-out token (Claim 8), citing
    this as an active, multi-PR gh-aw initiative.
  - Add the Dependabot release-cooldown pattern (Claim 13) as a control
    complementary to SHA pinning — delaying adoption of a newly-published
    action/dependency release by a fixed window (here, 7 days) to give a
    compromised or broken release time to be caught upstream.
  - Note that gh-aw's own hand-authored CI files (not compiler output) had
    unpinned action tags until this release (Claim 13) — a reminder that
    automatic compiler-level SHA pinning (`docs-ghaw-compilation-process.md`
    Claim 6) does not cover a project's own meta-CI.

- **Chapter 04 (Agentic Operations)**:
  - Document the three `gh aw logs` caching/observability fixes this release
    (Claims 1–3, 10) as a coherent hardening pass on the logs-caching
    subsystem: per-MCP-call identity, run exclusion without count reduction,
    in-place cache refresh, and wildcard-sharded cache files.
  - Add the repo-memory concurrent-write row-loss bug and its union-merge
    fix (Claim 11) as an operational gotcha for teams writing to a shared
    repo-memory `.jsonl` file from multiple concurrently-scheduled workflows.
  - When citing this blog series' "Agent of the Day/Week" run-count or
    failure-rate figures for a spotlighted workflow, independently verify
    against the Actions API first (Claim 15) — this is now a two-for-two
    pattern of unverified figures not matching the live artifact, for the
    same specific workflow, in opposite directions.
  - When citing a PR body as corroborating detail, confirm it isn't a stale
    auto-generated placeholder that never got updated post-merge (Claim 9).

- **Chapter 06 (Cost Management)**:
  - Note that gh-aw's model/pricing catalog is duplicated between the CLI
    and `actions/setup/js/models.json` and must be kept in sync by dedicated
    PRs per newly-available flagship model (Claim 4), continuing the
    `gpt-5.4`-drift theme already tracked in the corpus one generation newer.

- **Chapter 02 (Harness Engineering)**:
  - Document `gh aw update <package-id-or-url>` as a package-level
    reconciliation command that can restore accidentally-deleted
    package-owned workflow files (Claim 12), distinct from
    `gh aw update <workflow-name>`.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with a Python regex-based
   tag-stripping pass**, following the practice established in every prior
   weekly note (e.g. `blog-ghaw-weekly-2026-09-07.md` Extraction Note 1). An
   initial WebFetch pass was also run and cross-checked; it correctly
   captured the substance but restructured the post into its own
   "Opening Paragraph" / headed-bullet summary and, on comparison, invented
   run-duration figures for the Agent of the Week section that do not match
   either the raw HTML or (per Claim 15) the Actions API — none of the
   `Quote` fields above are drawn from the WebFetch pass; all are copied
   character-for-character from the raw-HTML extraction.

2. **All fifteen PRs named or linked in the post were independently
   fetched** via `gh pr view <N> --repo github/gh-aw --json
   title,body,url[,state,mergedAt,additions,deletions,changedFiles]`:
   #59579, #59697, #59690, #59711 (the four "What's New" PRs), #59636,
   #59703, #59602 (the three "Bug Fixes & Improvements" PRs), #60685, #60683
   (the two "Release: v0.89.12" PRs), #60702, #60663, #60452, #60650, #60061
   (the "Notable Pull Requests" PRs — #60685 is named in both the v0.89.12
   and Notable-PR sections). PR numbers not printed as visible text in the
   "Notable Pull Requests" section were recovered from the raw HTML's
   anchor `href` attributes and confirmed against each PR's own title/body.

3. **`cli-version-checker`'s run history was independently re-verified**
   against the GitHub Actions API beyond the "up to 5 linked pages" MINER.md
   §1 guidance, following the identical precedent and workflow-ID lookup
   already established in `blog-ghaw-agent-of-the-day-2026-09-08.md`
   Extraction Note 2 for this exact workflow (workflow ID 195931538, no
   re-lookup needed). This surfaced Claim 15's run-history mismatch; job-level
   detail (`gh api .../actions/runs/<id>/jobs`) for runs #555, #556, #557,
   and #549 was additionally fetched to confirm which specific job failed in
   run #556 (the pre-agent `activation` gate, not the agent itself) and to
   compute #549's agent-job-level duration (2.2 min) separately from its
   run-level duration (5.6 min), since the blog's "5.6 minutes" figure only
   matches at the run level, not the job level, for any run this note
   checked.

4. **The live `cli-version-checker.md` workflow source was re-fetched today**
   via `curl` from `raw.githubusercontent.com/github/gh-aw/main/...` to
   confirm the `safe-outputs:` block (Claim 14) still matches the state
   `blog-ghaw-agent-of-the-day-2026-09-08.md` documented on 2026-09-09; no
   change was found in the relevant frontmatter block between the two fetch
   dates.

5. **No contradictions filed**: Claim 9 (stale WIP PR body) and Claim 15
   (run-history mismatch) were each evaluated against the MINER.md §4a bar
   and do not meet it, for the reasons given in each claim's "Our assessment"
   and in Cross-References → Contradicts. Both are this source's own text
   (or an earlier post about the same subject) not surviving a check against
   live first-party artifacts, consistent with precedent already established
   twice for this exact blog series. `CONTRADICTIONS.md` and open
   `contradiction`-labeled issues were checked before reaching this
   conclusion.

6. **Cross-reference check performed** against `docs-ghaw-audit-reference.md`,
   `docs-ghaw-threat-detection.md`, `docs-ghaw-compilation-process.md`,
   `docs-ghaw-checkout-reference.md`, `docs-ghaw-monitoring-patterns.md`,
   `docs-ghaw-dependabot.md`, `blog-ghaw-weekly-2026-09-07.md`,
   `blog-ghaw-weekly-2026-08-24.md`, and both `blog-ghaw-agent-of-the-day-`
   notes for `cli-version-checker` and other September 2026 entries, all
   re-read in full (not skimmed) before writing Cross-References. All
   `Claim N` citations above were verified against the actual numbered
   claims in the cited notes at the time of writing, per MINER.md §4b.

7. **Confidence rated `emerging` overall, not `settled`**: the individual
   PR-level fixes (Claims 1–4, 6–8, 10–13) are settled, first-party, and
   independently verified via `gh pr view`. But the post's own flagship
   "Agent of the Week" narrative section — the only section with genuine
   editorial framing rather than PR-summary bullets — contains a
   run-history claim (Claim 15) this note could not reconcile with the
   Actions API at all, and a token/API-call figure ("~40K tokens... 26
   GitHub API calls") this note could not verify or falsify from available
   artifacts (no execution log or artifact URL was fetched for the specific
   runs in question; this is noted as an open gap, not claimed as false).
   The overall grade reflects that the release-notes content is solid while
   the editorial spotlight section is not reliable without independent
   verification.
