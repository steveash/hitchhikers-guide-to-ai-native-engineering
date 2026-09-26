---
source_url: https://github.github.com/gh-aw/blog/2026-09-25-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 25, 2026: Daily VulnHunter Scan"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-25
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: settled
issue: "#3725"
---

# Agent of the Day – September 25, 2026: Daily VulnHunter Scan

> Profiles Daily VulnHunter Scan, a gh-aw workflow that runs Capital One's
> open-sourced `vulnhunt` injection-bug methodology as a single Claude Code
> agent against a deterministically pre-scoped, risk-ranked slice of gh-aw's
> own codebase, and treats a falsification-backed "no findings" as a
> legitimate, load-bearing output rather than an absence of detection. This
> note substantially extends the ~600-word blog post by fetching the live
> workflow source (`.github/workflows/daily-vulnhunter-scan.md`), the target
> file it names (`actions/setup/js/apply_samples.cjs`), and the complete
> first-party GitHub Actions artifacts (`agent_output.json`,
> `agent_usage.json`, `agent-stdio.log`, `evals.jsonl`,
> `activity/summary.json`) for the exact run the blog describes as reviewing
> "all 40 ranked candidates" (`github/gh-aw/actions/runs/36099855973`) —
> which corroborate the blog's headline claims (turn count, noop outcome,
> zero blocked network requests) while showing the blog's "1.94M tokens"
> figure does not cleanly reproduce from the run's own token-usage
> breakdown, and that the blog's terse description of the codebase's
> defensive patterns compresses a much more specific, file-and-function-
> attributed self-assessment the agent actually wrote.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  convention documented across this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-24.md` and
  `blog-ghaw-agent-of-the-day-2026-08-28.md`. One agent profiled per post,
  distinct from the weekly changelog format.)
- **Author credibility**: Official gh-aw platform team blog, auto-published
  by the same scheduled "Agent of the Day" pipeline as the rest of the
  series. The post cites two specific, independently-checkable GitHub
  Actions run IDs (35961274043 for September 24, 36099855973 for September
  25) and a named target file (`actions/setup/js/apply_samples.cjs`) — all
  fetched directly and cross-checked by this note (see Concrete Artifacts).
  This note additionally fetched the live workflow definition
  (`.github/workflows/daily-vulnhunter-scan.md`), the September 25 run's
  own agent output, usage, and eval artifacts, and the actual source of the
  file named in the September 24 finding.
- **Scope**: Covers one workflow (Daily VulnHunter Scan) and two of its
  daily runs (Sept 24 and Sept 25, 2026) in gh-aw's own repository. Does not
  cover VulnHunter's original multi-agent design as Capital One built it
  (this workflow deliberately runs only a subset of it as a single agent),
  nor does it cover any run before or after the two it names. This note
  independently verified the Sept 25 run's artifacts but did not fetch the
  Sept 22 baseline run the blog compares against, so that comparison is
  corroborated only at the conceptual level, not re-derived from raw data.

## Extracted Claims

### Claim 1: VulnHunter treats a falsification-backed "no findings" as a real, load-bearing output rather than an absence of detection — the opposite incentive from scanners optimized to always report something.
- **Evidence**: Blog framing plus the workflow's own Reporting Rules
  ("Only report findings that survive VulnHunter's falsification/disproof
  process... If there are no verified exploitable findings, call `noop`
  with a short explanation") and the actual Sept 25 run output, which called
  `noop` with a itemized, code-attributed explanation rather than a bare
  "nothing found."
- **Confidence**: settled
- **Quote**: "What makes VulnHunter interesting isn't that it never finds anything — it's that "nothing to report" is a real, load-bearing output, backed by explicit falsification logic instead of a shrug."
- **Our assessment**: Confirmed against primary run data, not just the
  blog's framing — the actual `agent_output.json` for run 36099855973
  contains a multi-paragraph `noop` message with specific function and file
  names as evidence (see Concrete Artifacts), which is a materially
  stronger form of "load-bearing no-finding" than the blog post alone
  demonstrates.

### Claim 2: On September 24 (run 35961274043), the agent flagged an unsanitized `branch` argument passed into `git checkout -b` inside `actions/setup/js/apply_samples.cjs` as a textbook CWE-88 flag-injection candidate, then falsified it by tracing the argument's origin to a compile-time deterministic-replay fixture rather than live/external input.
- **Evidence**: Blog narrative, independently verified by fetching
  `actions/setup/js/apply_samples.cjs` directly from `github/gh-aw`. The
  file's own header comment describes it as "Deterministic replay driver
  for `gh aw compile --use-samples`" that "Reads `GH_AW_SAMPLES` (a JSON
  array of `{tool, arguments, sidecars}` entries produced by the compiler)."
  Its `branch` variable is set from `entry.arguments.branch` (falling back
  to a synthetic `gh-aw-sample-${index+1}` name) and passed to
  `runGit(["checkout", "-b", branch], repoCwd)`.
- **Confidence**: settled
- **Quote**: "It found the input comes from GH_AW_SAMPLES, a compile-time deterministic-replay fixture produced by gh aw compile --use-samples and authored by the workflow developer, never by live agent output or an external actor at runtime."
- **Our assessment**: This is a rare case where a Miner can independently
  re-derive a security agent's own falsification conclusion from the actual
  source code rather than trusting the agent's (or the blog's)
  characterization of it — and it checks out exactly. Strong evidence for
  the guide's "verification, not just generation" theme.

### Claim 3: The workflow's pre-agent bundling job deterministically ranks candidate files by security-risk signal (weighted regex hits for exec calls, network calls, secrets, path construction, and templating) so the agent never has to explore the repository tree itself.
- **Evidence**: Fetched directly from `.github/workflows/daily-vulnhunter-scan.md`'s `vulnhunter_bundle` job — a pure-bash step that greps the repo for five weighted pattern classes (`exec.Command`/`child_process`/etc. at weight 5, HTTP/network calls at weight 4, credential-shaped strings at weight 4, path-construction calls at weight 3, templating/regex/JSON calls at weight 2), sums per-file scores, and writes a ranked `scope/candidates.txt`.
- **Confidence**: settled
- **Quote**: "Rank files by security-risk signal so the agent never has to explore the tree." (from the workflow's bash comments, not the blog post)
- **Our assessment**: The blog's "ranked candidate list" phrase undersells a
  fairly specific, auditable mechanism. This is directly useful for the
  guide as a concrete example of moving reconnaissance out of the LLM and
  into deterministic pre-processing.

### Claim 4: Each run's scan scope is bounded to a fixed 20-file "core" (the highest-ranked files, rescanned every run) plus a 20-file "rotating" window that shifts daily by day-of-year, so full-repository coverage accumulates across runs without any single run scanning everything.
- **Evidence**: Fetched directly from the workflow's bundling script:
  `CORE=20`, `ROTATING=20`, and an offset computed as
  `(DAY * ROTATING) % TAIL_COUNT` where `DAY` is the day-of-year, applied to
  the non-core tail of the ranked file list.
- **Confidence**: settled
- **Quote**: "Bounded per-run scope: the highest-risk core plus a window that rotates daily through the remainder, so coverage accumulates across runs." (from the workflow's bash comments, not the blog post)
- **Our assessment**: This exactly explains why the Sept 24 run reviewed
  "25 of 41 candidates" while the Sept 25 run reviewed "all 40" — 40 is
  CORE(20)+ROTATING(20), and the total candidate pool size drifts run to
  run as the underlying ranked-file count changes with the codebase. Novel,
  reusable pattern for "budget-bounded but eventually-complete" scanning.

### Claim 5: The workflow deliberately runs only a subset of Capital One's externally-authored, multi-agent `vulnhunt` methodology, as a single agent, explicitly stripping out its orchestrator/sub-agent dispatch machinery and its Phase 1 recon step (which the deterministic bundling job already replaced).
- **Evidence**: Fetched directly from the workflow's agent prompt body,
  which instructs the agent to read the skill's `SKILL.md` and exactly two
  phase files (`phase2_class_inj.md`, `phase2b_verify.md`) and no others.
- **Confidence**: settled
- **Quote**: "Apply it as a **single agent**: ignore its orchestrator/sub-agent dispatch machinery and its Phase 1 recon instructions, which the bundle job already replaced." (from the workflow prompt, not the blog post)
- **Our assessment**: A concrete pattern for adapting a heavier, externally-
  designed multi-agent methodology into a cheaper CI-scale single-agent
  workflow by relocating one phase (recon) into deterministic pre-agent
  bash and keeping only the analysis/verification phases for the LLM.

### Claim 6: On September 25 (run 36099855973), the agent reviewed all 40 ranked candidates and none survived even the initial vulnerability-construction step, so the deeper Phase 2b falsification pass was never invoked at all.
- **Evidence**: Blog text, confirmed by the run's own `agent_output.json`
  noop message: "Zero findings survived initial construction, so no
  candidates required Phase 2b falsification."
- **Confidence**: settled
- **Quote**: "all 40 ranked candidates reviewed, zero surviving even initial construction, so nothing needed the deeper Phase 2b falsification pass at all."
- **Our assessment**: Matches the run's own primary output almost exactly
  in substance. This is a stronger "no finding" tier than September 24's
  single-candidate-falsified outcome — worth distinguishing in the guide
  as "nothing looked suspicious" vs. "something looked suspicious and was
  disproven."

### Claim 7: The September 25 run's reasoning enumerates specific, file-and-function-attributed defensive patterns across the scanned codebase (array-based exec arguments, named path validators, Docker image-reference validation, escaped/config-sourced YAML interpolation) rather than a generic "looks safe" verdict.
- **Evidence**: Blog text compresses this; the run's actual
  `agent_output.json` noop message names specific functions and files:
  `isSafeGitRevisionArg`, `validateRelPathForGit`,
  `fileutil.ValidatePathWithinBase`, `gitutil.ValidateGitPath`,
  `validateDockerImageRef`, `validateContainerMountPath` in
  `grant.go`/`grype.go`/`poutine.go`/`runner_guard.go`, and
  `shellEscapeArg`/`%q` escaping in `pi_engine.go`,
  `universal_llm_consumer_engine.go`, and `safe_outputs_env.go`.
- **Confidence**: settled
- **Quote**: "every os/exec call across the codebase uses array-based arguments rather than shell-string concatenation, path-construction sinks are guarded by explicit validators like isSafeGitRevisionArg and fileutil.ValidatePathWithinBase, Docker-based scanners validate image references before building argv, and values interpolated into generated YAML are consistently escaped or sourced from trusted workflow-author configuration."
- **Our assessment**: The blog's version of this claim is a fair paraphrase
  of the agent's actual output, but anyone wanting to check the underlying
  evidence should go to the run's own `agent_output.json` (reproduced in
  Concrete Artifacts below), not the blog post, which omits the specific
  file/function names entirely.

### Claim 8: The September 25 run cost 50 turns and 1.94M tokens, was flagged "resource heavy" for its task domain, and roughly half its turns were spent on data-gathering that could in principle move to deterministic pre-agent steps.
- **Evidence**: Blog text. Independently checked against the run's own
  artifacts: `agent-stdio.log` contains an exact `"num_turns":50` field,
  matching the blog precisely. `agent_usage.json` reports
  `input_tokens:126354`, `output_tokens:59884`, `cache_read_tokens:1826540`,
  `cache_write_tokens:481893` — no single sum of these fields lands on
  exactly 1.94M (input+cache_read ≈ 1.95M is the closest match; the full
  sum of all four fields is ≈2.49M). The "resource heavy" flag and the
  "roughly half the turns" data-gathering estimate are not present verbatim
  in any artifact this note fetched, so they could not be independently
  re-derived.
- **Confidence**: emerging
- **Quote**: "50 turns and 1.94M tokens for a single-agent scan, flagged as a "resource heavy" profile for its task domain, with roughly half the turns doing data-gathering that could in principle move to deterministic pre-agent steps."
- **Our assessment**: Turn count is exactly verified against the run's own
  Claude Code JSON output. The token total is close in order of magnitude
  but does not cleanly reproduce from the token-usage artifact this note
  fetched — likely a different aggregation method (e.g., a rounded or
  differently-computed "effective tokens" figure used by gh-aw's own audit
  tooling, per `docs-ghaw-effective-tokens-specification.md`) rather than a
  fabricated number, but readers should treat "1.94M" as the platform's own
  reported figure rather than a number this note re-derived from raw usage
  data.

### Claim 9: Comparing the September 25 run against a September 22 baseline shows turn count climbing from 44 to 50 while blocked network requests dropped from 3 to 0, surfaced automatically by gh-aw's audit tooling rather than by manually diffing two log files.
- **Evidence**: Blog text. Partially corroborated: the Sept 25 run's own
  firewall summary (`activity/summary.json`) shows `blocked_requests: 0`,
  consistent with the "0" side of the claimed drop. This note did not fetch
  the September 22 baseline run, so the "44" turn count and "3" blocked-
  request figures for that run are not independently re-verified here.
- **Confidence**: emerging
- **Quote**: "Comparing it against a matched September 22 baseline showed turn count climbing from 44 to 50 while blocked network requests dropped from 3 to 0 — a small but visible behavioral drift that the audit surfaced automatically, without anyone having to eyeball two log files side by side."
- **Our assessment**: The mechanism this describes (automatic baseline-drift
  detection via regression thresholds against a rolling baseline, rather
  than manual log comparison) matches the pattern already documented in
  `docs-ghaw-audit-with-agents.md`'s cache-memory 30-day rolling-baseline
  and numeric regression thresholds (cost >20%, tokens >50%, MCP
  error_rate >0.10) — strong conceptual corroboration even without
  re-deriving the raw Sept 22 numbers.

### Claim 10: The workflow's system prompt explicitly tells the agent its scan scope is fixed and non-widenable, and frames staying within it as a cost constraint, not just a correctness one.
- **Evidence**: Fetched directly from the workflow prompt body.
- **Confidence**: settled
- **Quote**: "Work inside that scope — you must finish within the run's AI credit budget, so spend it on analysis, not on exploring the repository." (from the workflow prompt, not the blog post)
- **Our assessment**: Direct, novel-to-corpus evidence of an explicit
  cost-boundary instruction embedded directly in a production agent's
  system prompt, phrased in terms of the run's AI-credit budget rather than
  generic "be efficient" framing.

### Claim 11: The workflow restricts its write surface to at most one GitHub issue per run (with automatic closure of older VulnHunter issues) or a `noop`, rather than a general-purpose comment/write channel.
- **Evidence**: Fetched directly from the workflow frontmatter's
  `safe-outputs` block.
- **Confidence**: settled
- **Quote**: (no direct quote; see the literal YAML reproduced in Concrete Artifacts)
- **Our assessment**: Reinforces a recurring gh-aw platform pattern (also
  seen in `docs-ghaw-safe-outputs-specification.md` and
  `docs-ghaw-gallery-security-review.md`) of constraining an agent's
  possible actions to a narrow, typed safe-output surface rather than
  general write access — here specifically capped at one issue per run with
  `close-older-issues: true` so stale VulnHunter issues don't accumulate.

## Concrete Artifacts

Live workflow definition, `.github/workflows/daily-vulnhunter-scan.md`
(fetched from `github/gh-aw` at HEAD, not from the blog post) — bundling
job's risk-ranking logic:

```bash
add_hits 5 'exec\.Command|exec\.CommandContext|child_process|execSync|spawnSync'
add_hits 4 'http\.NewRequest|http\.Get|http\.Post|url\.Parse|fetch\('
add_hits 4 'Authorization|GITHUB_TOKEN|[Bb]earer |_API_KEY|\.Token'
add_hits 3 'filepath\.Join|os\.ReadFile|os\.WriteFile|os\.Create|os\.OpenFile'
add_hits 2 'template\.(New|Must|HTML)|regexp\.MustCompile|json\.Unmarshal'

# Bounded per-run scope: the highest-risk core plus a window that rotates
# daily through the remainder, so coverage accumulates across runs.
CORE=20
ROTATING=20
DAY=$((10#$(date -u +%j)))
```

Same file, `safe-outputs` frontmatter block:

```yaml
safe-outputs:
  create-issue:
    title-prefix: "[vulnhunter] "
    labels: [security, vulnhunter, cookie]
    close-older-issues: true
    max: 1
  noop:
timeout-minutes: 45
max-turns: 80
strict: true
```

Same file, agent task instructions:

```
2. Read `/tmp/gh-aw/agent/vulnhunter/vulnhunt/SKILL.md` for the methodology. Apply it as a
   **single agent**: ignore its orchestrator/sub-agent dispatch machinery and its Phase 1
   recon instructions, which the bundle job already replaced.
3. Read exactly these two phase files and no others:
   - `/tmp/gh-aw/agent/vulnhunter/vulnhunt/phases/phase2_class_inj.md`
   - `/tmp/gh-aw/agent/vulnhunter/vulnhunt/phases/phase2b_verify.md`
```

`actions/setup/js/apply_samples.cjs` (fetched from `github/gh-aw` at HEAD)
— the code behind the September 24 falsified finding:

```js
branch = typeof entry.arguments.branch === "string" && entry.arguments.branch.trim()
  ? entry.arguments.branch.trim()
  : `gh-aw-sample-${index + 1}`;
entry.arguments.branch = branch;
...
try {
  runGit(["checkout", "-b", branch], repoCwd);
} catch {
  runGit(["checkout", branch], repoCwd);
}
```

`agent_output.json` for run `36099855973` (downloaded via
`gh run download 36099855973 --repo github/gh-aw -n agent`), full `noop`
message the agent produced — the primary source behind Claim 6 and Claim 7:

```
VulnHunter (single-agent, injection-class methodology) reviewed all 40 ranked candidates in scope/candidates.txt against phase2_class_inj.md's dangerous-sink reference (SQL, command execution, path traversal, SSRF/URL construction, XXE, file upload, XSS/navigation sinks, open redirect, LDAP, code injection/SSTI). Zero findings survived initial construction, so no candidates required Phase 2b falsification.

Key observations across the codebase (pkg/cli, pkg/parser, pkg/workflow, actions/setup/js):
- Every os/exec invocation (git, docker, gh) uses array-based arguments, never shell-string concatenation, eliminating command injection even where inputs (PR titles/bodies, image refs) are attacker/remote-influenced.
- Path-construction sinks are guarded by explicit validators (isSafeGitRevisionArg, validateRelPathForGit, fileutil.ValidatePathWithinBase, gitutil.ValidateGitPath, IsValidOperationalValueEvaluatorRunPath) that reject `..`, absolute paths, and control characters before use.
- Docker-based scanners (grant.go, grype.go, poutine.go, runner_guard.go) validate image refs and mount paths (validateDockerImageRef, validateContainerMountPath) before building argv.
- Values interpolated into generated shell/YAML in pkg/workflow (pi_engine.go, universal_llm_consumer_engine.go, safe_outputs_env.go) are consistently either escaped (shellEscapeArg, %q) or sourced from workflow-author frontmatter config (engine.driver, engine.extensions, safe-outputs.env) rather than external-attacker-controlled runtime data — outside the INJ threat model's trust boundary.
- GitHub-Actions-script-injection is deliberately avoided: untrusted values are passed via env: blocks rather than interpolated into ${{ }} expressions inside run: blocks (documented design choice in threat_detection_external.go).
- Validation-only files (permissions*.go, safe_outputs_validation.go, schema_validation.go, strict_mode_env_validation.go, graders_config.go, tools_validation_github.go) contain no dangerous sinks at all — pure struct/config logic with input-format checks (grader script forbidden-pattern denylist, repo pattern regex, target value validation).

Conclusion: no exploitable, falsification-surviving vulnerability found in this scope. No issue created per reporting rules (zero verified findings → noop).
```

`agent_usage.json` for run `36099855973`:

```json
{"input_tokens":126354,"output_tokens":59884,"cache_read_tokens":1826540,"cache_write_tokens":481893,"ambient_context":6095,"ai_credits":363.238275,"primary_model":"claude-sonnet-5"}
```

`evals.jsonl` for run `36099855973` (the run's own automated eval grading):

```json
{"id":"scan_completed","question":"Did the agent download the prepared VulnHunter bundle artifact, load the vulnhunt skill instructions, and scan the pre-ranked candidate files?","answer":"UNKNOWN","model":"claude-sonnet-5","timestamp":"2026-09-25T05:59:42.048Z","runid":"36099855973"}
{"id":"issue_created_or_noop","question":"Was a security issue created for verified exploitable findings, or was noop used when VulnHunter found nothing actionable?","answer":"YES","model":"claude-sonnet-5","timestamp":"2026-09-25T05:59:42.048Z","runid":"36099855973"}
```

`agent-stdio.log` for run `36099855973`, final Claude Code result line
(excerpt) — confirms turn count and duration:

```
..."num_turns":50,"ttft_ms":1608,"type":"result","duration_ms":564454,...
[claude-harness] attempt 1: process closed exitCode=0 duration=9m 24s stdout=1904591B stderr=0B hasOutput=true
```

`activity/summary.json` for run `36099855973`, firewall section — confirms
zero blocked network requests:

```json
"firewall": {
  "total_requests": 123,
  "allowed_requests": 123,
  "blocked_requests": 0,
  "allowed_domains": ["api.anthropic.com:443", "o205451.ingest.us.sentry.io:443", "otlp-gateway-prod-eu-west-2.grafana.net:443"]
}
```

## Cross-References

- **Corroborates**: `blog-anthropic-datadog-temper-machine-tool.md` (its
  four-layer verification cascade closing the gap between "generated" and
  "proven" is the same underlying idea as VulnHunter's Phase 2 →
  Phase 2b construction/falsification gate, at CI-workflow scale instead of
  runtime-kernel scale). `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
  (its "sensors vs. guides" / deterministic-vs-probabilistic 2×2 taxonomy
  maps directly onto this workflow's split: the deterministic bash bundling
  job is the "sensor" layer, the LLM's falsification reasoning is the
  probabilistic-judgment layer). `docs-ghaw-audit-with-agents.md` (the
  Sept 22→25 baseline-drift comparison the blog describes is exactly the
  cache-memory rolling-baseline / regression-threshold pattern that note
  documents). `docs-ghaw-measuring-impact.md` (turn count and token usage
  are the "operational layer" metrics that note's four-layer model
  predicts would be reported alongside a qualitative "resource heavy"
  cost-efficiency flag). Other `blog-ghaw-agent-of-the-day-*.md` notes
  (same recurring byline/format, and the same practice — established in
  `blog-ghaw-agent-of-the-day-2026-09-24.md` and
  `blog-ghaw-agent-of-the-day-2026-08-28.md` — of independently fetching
  run artifacts rather than trusting the blog's summary at face value).
- **Contradicts**: None identified. Unlike the September 24 post covered in
  `blog-ghaw-agent-of-the-day-2026-09-24.md` (where fetched run data flatly
  contradicted the blog's central claim), this post's claims about the
  Sept 25 run's outcome and turn count check out against primary data; only
  the exact token total (Claim 8) and the unfetched Sept 22 baseline
  (Claim 9) could not be fully reproduced, which is a verification gap, not
  a contradiction.
- **Extends**: `docs-ghaw-gallery-security-review.md` (that note's "Daily
  Malicious Code Scan" workflow reports leads via SARIF code-scanning
  alerts with an explicit "leads, not proof" framing — a design that
  surfaces low-confidence findings for a human to triage. VulnHunter takes
  the opposite design stance: falsify aggressively pre-report so that
  almost nothing reaches a human at all, and cap the write surface at one
  issue with `close-older-issues: true`. Same platform, two deliberately
  different philosophies for communicating agent security findings — worth
  citing both if the guide discusses agent-driven security scanning).
  `docs-ghaw-threat-detection.md` (this workflow's own frontmatter sets
  `features: gh-aw-detection: true`, meaning the VulnHunter *workflow
  itself* is protected by gh-aw's separate AI-powered threat-detection
  pipeline — a different mechanism analyzing the agent's own behavior for
  compromise, layered on top of what VulnHunter analyzes in the target
  code).
- **Novel**: The specific two-phase falsification pipeline (construction →
  verify) adapted from an externally-authored multi-agent methodology into
  a single-agent CI workflow by relocating its recon phase into
  deterministic pre-agent bash (Claim 5) is new to the corpus. The exact
  bounded-scope rotation mechanism — a fixed 20-file "core" plus a 20-file
  window that rotates daily by day-of-year (Claim 4) — is a concrete,
  reusable pattern for "budget-bounded but eventually-complete" scanning
  not documented elsewhere in this corpus.

## Guide Impact

- **Chapter 03 (Agent patterns & reasoning)**: Add the construction→
  falsification two-gate pattern (Claim 1, Claim 2, Claim 6) as a named
  example of an agent design that treats "no finding" as a first-class,
  evidence-backed output rather than a null result — contrast with
  `docs-ghaw-gallery-security-review.md`'s "leads, not proof" SARIF
  approach (see Extends) to show the guide two legitimate but opposite
  philosophies for agent-driven security review, so readers can choose
  based on their tolerance for false positives vs. missed leads.
- **Chapter 05 (Building agents for domain tasks / observability)**: Add
  the deterministic pre-agent bundling/ranking job (Claim 3, Claim 4) as a
  concrete example of moving reconnaissance out of the LLM loop entirely —
  cite the exact CORE=20/ROTATING=20 day-of-year rotation as a reusable
  "budget-bounded but eventually-complete" scanning pattern, and the
  explicit "you must finish within the run's AI credit budget" prompt
  language (Claim 10) as an example of stating cost constraints directly
  in an agent's system prompt rather than only enforcing them out-of-band.
- **Chapter 05 (resource tracking / observability)**: If the guide covers
  cross-run drift detection, cite Claim 9 alongside
  `docs-ghaw-audit-with-agents.md`'s regression thresholds as a live
  example of the pattern in production — but flag for the Assayer that
  this note could only corroborate it conceptually, not re-derive the raw
  Sept 22 numbers.

## Extraction Notes

- Followed the source's only in-body link (`github/gh-aw`) by fetching the
  live workflow definition, the run artifacts for the run the blog
  describes reviewing "all 40 ranked candidates" (36099855973), and the
  specific file named in the September 24 finding
  (`actions/setup/js/apply_samples.cjs`) — none of these are hyperlinked
  directly in the post's prose, but all are precisely enough named
  (workflow name, run IDs, file path) to locate unambiguously in
  `github/gh-aw`.
- Did not fetch the September 22 baseline run (Claim 9) or the September 24
  run's own artifacts beyond the file lookup for Claim 2 — flagged as
  emerging/partially-corroborated rather than fully re-verified.
- All blog-post quotes were copied verbatim from the rendered page (fetched
  via `curl` with HTML tags stripped, not via a summarizing fetch tool) to
  avoid paraphrase drift; quotes attributed to the workflow source, run
  artifacts, or `apply_samples.cjs` are marked as such and were copied
  verbatim from those files, not from the blog post.
- The `aic-usage-scan-v2` artifact for this run was empty; the "resource
  heavy" / baseline-drift figures in Claim 8 and Claim 9 could not be
  traced to a specific artifact file this note could open, only to the
  blog's own prose describing "gh aw's own audit tooling."
