---
source_url: https://vercel.com/changelog/simplified-onboarding-for-deepsec
source_type: blog-post
title: "Simplified onboarding for deepsec"
author: Malte Ubl (Vercel)
date_published: 2026-08-10
date_extracted: 2026-09-08
last_checked: 2026-09-08
status: current
confidence_overall: emerging
issue: "#3308"
---

# Simplified onboarding for deepsec

> Vercel changelog announcing single-command onboarding (`npx deepsec init`) for
> deepsec, Vercel's open-source AI-driven security review tool — a checkpointed,
> resumable setup that scaffolds an isolated `.deepsec/` workspace, wires up model
> access via Vercel AI Gateway or a bring-your-own-key provider, and immediately
> runs a codebase-description + pattern-scan + AI-review pipeline. The linked
> getting-started, architecture, PR-mode, configuration, and models docs reveal a
> much more fully-specified tool than the ~120-word changelog itself shows:
> explicit cost/duration governors, a scan→process→revalidate→enrich pipeline with
> a stated 50%+ false-positive reduction from revalidation, a two-job GitHub
> Actions pattern for safe CI use, and named per-model cost/false-positive
> tradeoffs.

## Source Context

- **Type**: blog-post (Vercel official changelog, `vercel.com/changelog`,
  published August 10, 2026; byline Malte Ubl). Per MINER.md §1, five linked docs
  pages were followed since the changelog itself is a short (~120-word) feature
  announcement that compresses mechanics documented in much greater depth on
  deepsec's own docs site (`deepsec.sh/docs`, not a Vercel-hosted docs path):
  the getting-started guide, the docs index/overview, the architecture page, the
  PR-mode ("reviewing changes") page, the configuration reference, and the models
  page. Six pages were fetched in total (docs index plus five content pages),
  slightly over the "up to 5" guidance in MINER.md §1, because the docs index
  itself is a one-paragraph link list rather than a substantive content page, and
  each subsequent page was directly load-bearing for a distinct claim (setup,
  pipeline architecture, PR/CI usage, configuration surface, model economics).
  Not followed: `supported-tech`, `writing-matchers`, `vercel-setup`,
  `data-layout` (partially covered via the architecture page), `plugins`, and
  `faq` — these either duplicate detail already captured or fall outside this
  issue's scope (onboarding and core pipeline mechanics, not matcher-authoring or
  plugin-extension mechanics).
- **Author credibility**: First-party Vercel product changelog for a Vercel
  open-source tool, byline Malte Ubl (publicly known as a Vercel
  CTO/principal-engineer-level figure in the corpus's existing Vercel coverage).
  Authoritative for the tool's existence, CLI surface, configuration schema, and
  stated architecture, since all of it is drawn from the vendor's own docs site
  for a shipping open-source project. Not a credible source for independent
  detection-quality data (precision/recall against a labeled vulnerability
  corpus), real-world adoption figures, or comparative benchmarking against
  competing AI security-review tools — none of the fetched pages cite a named
  customer, a third-party evaluation, or a reproducible benchmark; the stated
  false-positive-reduction figure (Claim 5) and refusal-rate figure (Claim 7) are
  vendor-stated numbers with no described methodology.
- **Scope**: Covers deepsec's one-command onboarding flow, its steady-state
  scan/process/revalidate/enrich/export pipeline, its CI/PR-diff mode, its
  configuration and environment-variable surface, and its model
  recommendations/cost tradeoffs. Does NOT cover: independent security
  evaluation of detection quality, pricing for Vercel AI Gateway usage incurred
  by running deepsec at scale, the matcher-authoring workflow in
  `writing-matchers`, the plugin-extension API in `plugins`, or multi-repo
  workspace mechanics beyond the single `init-project --id` command named in the
  getting-started page.

## Extracted Claims

### Claim 1: A single command, `npx deepsec init`, both bootstraps a new deepsec workspace and runs the tool's first end-to-end review, scaffolding an isolated `.deepsec/` directory rather than touching the target repository's own files
- **Evidence**: The changelog's lead sentence and the getting-started page's "Key Setup Command" section both state the same single entry point.
- **Confidence**: settled (first-party description of a shipping CLI entry point, consistent across the changelog and the docs page)
- **Quote**: "Users can now initialize a repository and execute an initial security review using: `npx deepsec init`" (changelog, as fetched)
- **Our assessment**: Collapsing "set up the tool" and "run the first scan" into one command is a specific onboarding-friction reduction, not just a marketing restatement of "the tool has a CLI" — it means a developer's first interaction with deepsec produces a real result (a codebase description plus initial findings) rather than an empty scaffold requiring a second command to see any value. Scoping all generated state to a dedicated `.deepsec/` directory (confirmed in the architecture page's on-disk layout, Claim 8) is the concrete mechanism that keeps this "just run one command" flow from mutating the target repository's own source tree.

### Claim 2: The setup process is checkpointed and resumable — re-running the exact same `npx deepsec init` command after an interruption continues from the last completed step rather than restarting the pipeline
- **Evidence**: The changelog's closing sentence and the getting-started page's "Resuming Interrupted Runs" section state this as the same recovery mechanism.
- **Confidence**: settled (first-party description of a specific, named recovery behavior)
- **Quote**: "Just run the same command again: `npx deepsec init`. Deepsec remembers how far it got." (getting-started page, as fetched)
- **Our assessment**: This is the same "idempotent, checkpointed setup" pattern already valuable elsewhere in the corpus for long-running or resource-constrained agent processes: a setup flow that can be interrupted by a closed terminal, a hit rate limit, or a crash without forcing the user to redo already-completed (and, for the AI-review phase, already-paid-for) work. Combined with the per-run cost/duration governors (Claim 4), this suggests the tool's authors specifically designed for the case of a review run being deliberately or accidentally cut short partway through a paid AI pass.

### Claim 3: At setup, the user chooses both a model (from a recommended list or a custom specification) and a payment path — routing model calls through Vercel AI Gateway by default, or authenticating with a separate provider directly
- **Evidence**: The getting-started page's "Initial Configuration" section, corroborated by the configuration reference's environment-variable table (`AI_GATEWAY_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `OPENAI_API_KEY`) and the models page's per-backend defaults.
- **Confidence**: settled (first-party specification of the exact setup prompts and the underlying credential options)
- **Quote**: "During setup, users are prompted for two things: Model selection - Choose from recommended options or specify a custom model. Payment method - Either route through Vercel AI Gateway (default) or use your own API key." (getting-started page, as fetched)
- **Our assessment**: Vercel AI Gateway as the *default* payment path — rather than requiring the user to first obtain and configure a provider API key before deepsec can run at all — is the same "reduce time-to-first-successful-run" design goal as Claim 1, applied to the credentials step specifically. The bring-your-own-key escape hatch (direct OpenAI key with `--agent codex`, Anthropic with `--agent claude`, or local machine subscriptions via `--model-auth local`, per the configuration reference) means a team that already has its own model spend/governance in place is not forced through Vercel's gateway.

### Claim 4: Runs can be bounded by explicit cost and duration ceilings — `--max-cost-usd` and `--max-duration` flags stop the AI-review pass once either limit is reached
- **Evidence**: The getting-started page's "Cost and Time Controls" section, listing both flags with their accepted formats.
- **Confidence**: settled (first-party specification of exact flag names and accepted units)
- **Quote**: "Users can limit runs with flags: `--max-cost-usd 100`, `--max-duration 2h` (supports ms, s, m, h units)" (getting-started page, as fetched)
- **Our assessment**: This is a directly relevant, concrete instance of the "autonomous agent workflows that loop or fan out unsupervised" cost-risk scenario that Vercel's own AI Gateway team names as a reason to add key-level budgets (`blog-vercel-ai-gateway-api-key-budgets.md`, Claim 4) — here the cost governor is built into the consuming tool itself rather than (or likely in addition to) an upstream gateway-level budget. A team running deepsec's paid AI-review pass across a large codebase or in CI on every PR has a first-party, tool-level cost ceiling available without needing to separately configure an AI Gateway key budget, though the two mechanisms are not shown to be mutually aware of each other in any fetched page.

### Claim 5: The steady-state pipeline runs five named stages in sequence — scan (free, pattern-based), process (paid, AI-driven), revalidate (re-checks findings for false positives, reported to reduce false-positive rates by more than 50%), enrich (attaches git committer/ownership data), and export/report
- **Evidence**: The architecture page's "Initialization and Steady-State Phases" and "Key Processing Stages" sections, which name and describe each stage.
- **Confidence**: emerging (the pipeline stage names, order, and mechanism are settled first-party documentation; the specific "50%+" false-positive reduction figure is a vendor-stated number with no disclosed methodology, dataset, or comparison baseline)
- **Quote**: "Revalidate: Re-checking findings for false positives, yielding verdicts like true-positive or fixed, reportedly reducing false positive rates by 50%+" (architecture page, as fetched)
- **Our assessment**: Splitting "find candidate issues" (scan, process) from "re-check whether they're real" (revalidate) as a distinct, separately-invokable pipeline stage is the same design goal as the confidence-scoring and false-positive-suppression mechanisms already documented for competing AI security-review tools in this corpus (see Cross-References) — the specific mechanism here (a dedicated re-verification pass with its own verdicts, rather than a single-pass confidence score attached at finding-creation time) is new to the corpus, but the stated 50%+ figure should be treated as a vendor claim pending any independent measurement, consistent with how this note treats Claim 7's refusal-rate figure.

### Claim 6: The `scan` stage is a fast, free, non-AI pattern-matching pass — glob/pattern matching over the codebase with no model cost, completing in roughly 15 seconds for a 2,000-file codebase
- **Evidence**: The architecture page's "Key Processing Stages" section and the getting-started page's daily-commands list, which both describe `scan` as the cost-free stage distinct from the paid `process` stage.
- **Confidence**: settled (first-party description of the stage's mechanism and a specific, named performance figure)
- **Quote**: "Scan: Glob matching without AI cost, producing candidate findings (~15 seconds for 2k files)" (architecture page, as fetched)
- **Our assessment**: Separating a free, fast, deterministic pattern pass from the expensive AI pass is the concrete architectural reason the cost governors in Claim 4 only need to bound the AI stage — a team can re-run `scan` as often as it likes (e.g., on every commit) at zero marginal AI cost, and only pay for `process` when it actually wants the AI review to advance. This is the same two-tier "cheap deterministic filter narrows what the expensive model has to look at" pattern documented for a security-scanning agent elsewhere in the corpus (`docs-ghaw-gallery-security-review.md`, Claim 7: bash-scripted grep/regex heuristics as a first pass before agent reasoning) — deepsec's split is a pipeline-stage-level version of the same idea rather than instructions embedded in one agent's prompt.

### Claim 7: Vendor-stated per-model performance figures include a sub-1% batch-refusal rate for the two default/best-scoring models (Claude Opus and `gpt-5.5`), and an explicit ~3x cost reduction with a 10–20 percentage-point false-positive-rate increase when dropping from Claude Opus to Claude Sonnet for the same prompt
- **Evidence**: The models page's "Performance Claims" and per-backend model tables.
- **Confidence**: anecdotal (specific numeric figures — refusal rate, cost multiplier, false-positive delta — stated by the vendor with no disclosed test set, methodology, or sample size)
- **Quote**: "Claude Opus and `gpt-5.5` refuse less than 1% of batches in practice." / "Drop to `claude-sonnet-4-6`. Same prompt, ~3× cheaper, ~10–20% higher FP rate." (models page, as fetched)
- **Our assessment**: This is a named, quantified cost/quality tradeoff for choosing a review model — more specific than a general "bigger models are more accurate" claim — but it is a single vendor's internal figure with no stated evaluation methodology, so it should be treated as directional guidance ("expect meaningfully more false positives on the cheaper model, not zero-cost accuracy") rather than a benchmark result a practitioner could reproduce or cite externally.

### Claim 8: The tool exposes three named cost/quality selection profiles at setup — `best` (highest score regardless of cost), `value` (best score within 2.5x the cheapest option's cost), and `budget` (cheapest option) — and displays each model's cost relative to the cheapest recommendation
- **Evidence**: The models page's "Cost Information" section.
- **Confidence**: settled (first-party specification of the exact profile names and the `value` profile's stated cost multiplier)
- **Quote**: "recommends selecting based on profiles: `best` (highest score), `value` (best score within 2.5× cheapest cost), or `budget` (cheapest option)" (models page, as fetched)
- **Our assessment**: Naming three fixed profiles rather than leaving the cost/quality tradeoff as a single opaque model-name choice is a specific UX decision worth extracting on its own: it converts "which model should I use" into a small, labeled decision (optimize for score, optimize for a bounded cost premium, or optimize for price) rather than requiring the user to already know each candidate model's relative accuracy and price before choosing.

### Claim 9: `deepsec process` supports a dedicated PR/diff review mode restricted to changed files, using one of five mutually exclusive file-selection flags, and its exit code counts only net-new findings — pre-existing findings in unchanged code do not fail the run
- **Evidence**: The reviewing-changes page's "Core Purpose," "Main Flags," and "Exit Codes" sections.
- **Confidence**: settled (first-party specification of exact flag names and exit-code semantics)
- **Quote**: "Use PR mode to investigate only changed files and fail CI when new findings appear." / "Net-new findings only count toward the exit code." (reviewing-changes page, as fetched)
- **Our assessment**: The "net-new findings only" exit-code rule is the specific design choice that makes this usable as a CI gate on an existing codebase with known, unfixed findings: a repository does not have to reach zero total findings before it can adopt deepsec as a required check — it only needs to avoid introducing *new* ones. Without this distinction, any codebase with pre-existing findings would fail every PR check regardless of what the PR itself changed, which is a common adoption blocker for retrofitting a strict static/AI analysis gate onto a large existing codebase.

### Claim 10: The documented CI pattern for PR review explicitly separates code execution from repository write permissions into two GitHub Actions jobs, framed as preventing a malicious PR from combining "execute arbitrary code" with repo write access
- **Evidence**: The reviewing-changes page's "Security Approach" section.
- **Confidence**: settled (first-party statement of the specific threat model and the specific mitigating architecture)
- **Quote**: "The recommended workflow uses a two-job GitHub Actions pattern separating code execution from repository write permissions, preventing malicious PRs from combining \"execute arbitrary code\" with repo access." (reviewing-changes page, as fetched)
- **Our assessment**: This is the same "privilege separation between the job that runs untrusted PR content and the job that has write access" pattern already documented as a named architectural requirement for GitHub Agentic Workflows' Safe Outputs design (see Cross-References) — deepsec's own CI recipe independently arrives at the identical two-job split for the identical reason (a fork PR's contents are untrusted code that must not run with write-scoped credentials). This is corroborating evidence that "separate the execution sandbox from the write-capable job" is close to an industry-converged pattern for any CI-triggered AI review of PR content, not one vendor's idiosyncratic design.

### Claim 11: PR-comment output is truncated to specific character limits (600/400 characters) specifically to stay under GitHub's per-comment size cap
- **Evidence**: The reviewing-changes page's "PR Comments" section, describing the `--comment-out` flag's output formatting.
- **Confidence**: settled (first-party statement of exact truncation lengths and their stated rationale)
- **Quote**: descriptions are truncated at 600/400 characters to avoid exceeding "GitHub's 65 KiB comment limit" (reviewing-changes page, as fetched; the 65 KiB figure is a direct quote, the 600/400-character figures are stated directly by the fetched summary rather than quoted verbatim — see Extraction Notes)
- **Our assessment**: This is a small but concrete example of a tool author designing output format around a specific downstream platform constraint (GitHub's documented 65 KiB comment body limit) rather than emitting unbounded findings text and letting the PR-comment API call fail on a large batch of findings — a reusable detail for any harness that posts AI-generated findings as GitHub PR comments in bulk.

### Claim 12: The configuration schema centers on a typed config file (`deepsec.config.{ts,mjs,js,cjs}`) declaring one or more `ProjectDeclaration` entries, each with a required `id` and `root` and optional fields for GitHub links, repo-context markdown injected into AI prompts, free-form system-prompt append text, and priority path ordering
- **Evidence**: The configuration reference's "Top-Level Configuration Fields" and "ProjectDeclaration Fields" tables.
- **Confidence**: settled (first-party specification of exact field names, types, and descriptions)
- **Quote**: "`infoMarkdown` | `string` | no | \"Repo context injected into AI prompts\"" / "`promptAppend` | `string` | no | \"Free-form text appended to the system prompt\"" / "`priorityPaths` | `string[]` | no | \"Path prefixes to process first.\"" (configuration reference, as fetched)
- **Our assessment**: `infoMarkdown` and `promptAppend` are named, structured hooks for injecting project-specific context into every AI review call — the same "give the model durable, repo-specific context rather than relying on it to infer everything from raw file contents" pattern documented elsewhere in the corpus for CLAUDE.md-style context files, but here exposed as explicit typed configuration fields for a single-purpose review tool rather than a general-purpose coding-agent memory file. `priorityPaths` lets a team front-load review of its highest-risk directories (e.g., auth, payments) rather than reviewing files in an arbitrary or purely alphabetical order.

### Claim 13: Generated pipeline state is deliberately excluded from version control while a durable summary file is kept trackable — `files/`, `runs/`, `reports/`, `project.json`, and `setup/` under `data/<projectId>/` are gitignored by the scaffold, but `INFO.md` remains trackable — and the architecture is described as file-level-atomic and append-only, so records are never destructively overwritten
- **Evidence**: The architecture page's "On-Disk Data Structure" and "Design Principles" sections.
- **Confidence**: settled (first-party statement of the exact gitignore boundary and the two named design principles)
- **Quote**: "Generated `files/`, `runs/`, `reports/`, `project.json`, and `setup/` are gitignored by the scaffold; `INFO.md` remains trackable." (architecture page, as fetched)
- **Our assessment**: This draws a specific, checkable line between "state a team should commit and review" (a human-readable `INFO.md` codebase description) and "state that is regenerable tool output" (per-file records, run history, reports) — a team adopting deepsec does not need to decide for itself what belongs in version control, since the scaffold's own `.gitignore` already encodes that decision. The append-only, file-level-atomic design principle is the stated mechanism behind the checkpointed resumability in Claim 2: if records are never destructively overwritten, a resumed run can safely pick up from the last completed atomic write without risking a corrupted half-written record from the interrupted attempt.

### Claim 14: In CI or other non-interactive environments, deepsec automatically switches to a headless mode that never prompts for input or opens a browser window, and this can additionally be forced with explicit flags
- **Evidence**: The getting-started page's "CI/Headless Mode" section.
- **Confidence**: settled (first-party statement of the specific automatic-detection behavior and the explicit override flags)
- **Quote**: "In CI environments without terminals: \"deepsec automatically runs in headless mode: it never prompts or opens a browser\"" (getting-started page, as fetched; inner quotation marks as returned)
- **Our assessment**: Automatic environment detection (rather than requiring every CI caller to remember to pass a `--headless` flag) reduces the chance that a CI run silently hangs waiting on a prompt or browser-based auth step that can never be answered in that environment — the explicit `--headless`, `--yes`, and `--model-profile` flags remain available for a caller that wants to force non-interactive behavior even when the environment might otherwise appear interactive, or to pin a specific model profile rather than relying on auto-detection.

## Concrete Artifacts

### Onboarding and daily-use commands (verbatim, from the changelog and getting-started page)

```
# One-command bootstrap and first review
npx deepsec init

# Cost/time-bounded run
npx deepsec init --max-cost-usd 100
npx deepsec init --max-duration 2h

# Resume an interrupted run (same command)
npx deepsec init

# Daily commands (run from the .deepsec/ directory)
pnpm deepsec status        # check progress
pnpm deepsec scan          # pattern matching (free)
pnpm deepsec process       # AI review (paid)
pnpm deepsec revalidate    # reduce false positives

# Export findings
pnpm deepsec export --format md-dir --out ./findings

# Bring-your-own-provider auth
MY_OPENAI_KEY=... npx deepsec init --agent codex
npx deepsec init --agent claude
npx deepsec init --model-auth local

# Multi-repo workspace
pnpm deepsec init-project --id <project-id>

# CI / headless
npx deepsec init --headless --yes --model-profile <profile>
```
Source: https://vercel.com/changelog/simplified-onboarding-for-deepsec and
https://deepsec.sh/docs/getting-started

### PR/diff mode commands and exit codes (verbatim, from the reviewing-changes page)

```
deepsec process --diff origin/main
deepsec process --diff-staged
deepsec process --diff-working
deepsec process --files <csv>
deepsec process --files-from <path>
deepsec process --comment-out <path>

# Exit codes:
#   0   — no findings
#   1   — findings detected (net-new findings only count toward this)
#   nonzero (other) — runtime error
```
Source: https://deepsec.sh/docs/reviewing-changes

### Configuration file fields (verbatim table contents, from the configuration reference)

```
Top-level (deepsec.config.{ts,mjs,js,cjs}):
  projects            ProjectDeclaration[]   "The codebases deepsec knows about."
  plugins             DeepsecPlugin[]        "Loaded in order; later plugins override single-slot capabilities."
  matchers            { only?, exclude? }    "Filter the matcher set used by `scan`."
  defaultAgent        string                 codex | claude | pi
  defaultModel        string                 "Default `--model` value selected during setup."
  defaultThinkingLevel string                "Default reasoning effort (`minimal` through `xhigh`)"
  ai                  ModelRoute             "Non-secret model credential route"
  dataDir             string                 "Override the `data/` directory. Defaults to `./data`."

ProjectDeclaration:
  id             string    required  "Used as `--project-id` and the data directory name"
  root           string    required  "Absolute or relative path to the codebase."
  githubUrl      string    optional  "used in exports for clickable links"
  infoMarkdown   string    optional  "Repo context injected into AI prompts"
  promptAppend   string    optional  "Free-form text appended to the system prompt"
  priorityPaths  string[]  optional  "Path prefixes to process first."
```
Source: https://deepsec.sh/docs/configuration

### Environment variables (verbatim, from the configuration reference)

```
Platform auth:
  VERCEL_OIDC_TOKEN   "Interactive linked-project credential used by Gateway and Sandbox"
  VERCEL_TOKEN        "Non-interactive Vercel access token"
  VERCEL_TEAM_ID      "Non-interactive team paired with `VERCEL_TOKEN`"
  VERCEL_PROJECT_ID   "Non-interactive project paired with `VERCEL_TOKEN`"

Model auth:
  AI_GATEWAY_API_KEY   "Optional long-lived alternative to linked-project OIDC"
  ANTHROPIC_AUTH_TOKEN "API token for the Claude Agent SDK"
  ANTHROPIC_BASE_URL   default: https://ai-gateway.vercel.sh
  <ai.apiKeyEnv>       user-chosen variable for provider credentials

Optional:
  OPENAI_API_KEY       used by codex and Pi agents
  OPENAI_BASE_URL      default: https://ai-gateway.vercel.sh/v1
  PI_CODING_AGENT_DIR  "Optional Pi config/auth directory. Defaults to `~/.pi/agent`"
  DEEPSEC_AGENT_DEBUG  "Set to `1` to enable verbose agent logging"
  DEEPSEC_DATA_ROOT    "Override the data directory location"
```
Source: https://deepsec.sh/docs/configuration

### Pipeline architecture and on-disk layout (as summarized from the architecture page)

```
Init phase:   scaffold -> install -> link/model/Sandbox -> INFO + inventory
                -> baseline scan -> coverage policy evaluation
Steady state: scan -> process -> revalidate -> enrich -> export/report

On disk: data/<projectId>/{files/, runs/, reports/, project.json, setup/}  [gitignored]
         data/<projectId>/INFO.md                                          [trackable]

Design principles: file-level atomicity; append-only history (no destructive
overwrites); plugin-mediated integrations.
```
Source: https://deepsec.sh/docs/architecture

### Model recommendations and cost/quality profiles (verbatim, from the models page)

```
Codex (default):   gpt-5.5           (alt: gpt-5.5-pro, "most careful ... at
                                       significantly higher cost")
Claude:            claude-opus-4-8   (process/revalidate)
                   claude-sonnet-4-6 (triage; "~1¢/finding")
                   -> dropping Opus to Sonnet: "Same prompt, ~3x cheaper,
                      ~10-20% higher FP rate"
Pi:                zai/glm-5.2       (via Vercel AI Gateway)

Selection profiles: best (highest score) | value (best score within 2.5x
cheapest cost) | budget (cheapest option)
```
Source: https://deepsec.sh/docs/models

## Cross-References

- **Corroborates**:
  - `blog-vercel-ai-gateway-api-key-budgets.md` Claim 4 (Vercel frames AI Gateway
    key budgets as a response to "autonomous agent workflows that loop or fan
    out unsupervised" among other cost risks): this source's Claim 4
    (`--max-cost-usd` / `--max-duration` flags on deepsec's own AI-review pass)
    is a concrete instance of a tool author building the same cost-risk
    mitigation directly into an autonomous, potentially-long-running AI review
    loop, at the consuming-tool layer rather than (or in addition to) the
    gateway-key layer that note documents.
  - `docs-ghaw-gallery-security-review.md` Claim 7 (a security-scanning agent
    combining deterministic bash/grep heuristics as a first pass with agent
    reasoning layered on top, rather than relying on LLM judgment alone): this
    source's Claim 6 (a free, fast, non-AI `scan` pattern-matching stage that
    runs before the paid AI `process` stage) is the same "cheap deterministic
    filter narrows the expensive model's workload" design, expressed as a
    distinct pipeline stage rather than instructions inside one agent's prompt.
  - `docs-ghaw-safe-outputs-specification.md` (the corpus's existing coverage of
    GitHub Agentic Workflows' privilege-separation requirement that agents
    execute without repository write permissions, with writes mediated through
    a separate, constrained channel): this source's Claim 10 (deepsec's
    documented two-job CI pattern separating code execution from
    repository-write permissions, explicitly to stop a malicious PR from
    combining "execute arbitrary code" with repo access) is an independently
    arrived-at instance of the same execution/write privilege-separation
    pattern, for a different tool and platform.
  - `practitioner-getsentry-sentry.md` (Notable Skills → `sentry-security`: "a
    security review framework based on 37 historical security patches...
    requires HIGH/MEDIUM confidence threshold and traces a 7-layer enforcement
    chain before flagging issues"): this source's Claim 5 (a dedicated
    `revalidate` pipeline stage that re-checks findings and is reported to cut
    false positives by 50%+) is the same underlying goal — suppressing
    low-confidence or false-positive AI security findings before they reach a
    human — implemented as a distinct re-verification pipeline stage rather
    than an inline confidence-threshold rule evaluated once at finding-creation
    time.
  - `docs-github-copilot-cli-security-review.md` Claim 2 and
    `docs-github-copilot-app-security-review.md` Claim 2 (both describe
    GitHub Copilot's `/security-review` command output as "high-confidence
    security findings, scored by severity and confidence"): this is the same
    general industry pattern of attaching a confidence/severity signal to
    AI-generated security findings to support triage, that deepsec implements
    differently (a separate `revalidate` stage with true-positive/fixed
    verdicts, rather than a per-finding confidence score attached inline).

- **Contradicts**: No contradiction issue filed. No existing corpus source
  makes a claim about AI-driven security-review tooling that this source's
  claims materially oppose — the differences noted above (dedicated
  re-verification stage vs. inline confidence scoring; tool-level cost flags vs.
  gateway-level key budgets) are different implementations of compatible goals
  for different tools, not conflicting claims about the same mechanism.

- **Extends**:
  - `docs-github-copilot-cli-security-review.md` and
    `docs-github-copilot-app-security-review.md`: those notes document GitHub's
    developer-invoked, closed-source `/security-review` command (five named
    vulnerability categories, severity/confidence-scored output, no disclosed
    architecture beyond the changelog copy). This source documents a
    structurally different, open-source competitor with a fully disclosed
    pipeline (scan/process/revalidate/enrich/export), an explicit multi-agent
    backend choice (Codex, Claude, or Pi), named per-model cost/FP tradeoffs,
    and a documented CI/PR-diff integration mode — none of which the GitHub
    Copilot notes' sources disclose for the closed-source command.
  - `blog-vercel-ai-gateway-api-key-budgets.md`: that note documents
    gateway-level, per-API-key dollar budgets as a general cost-governance
    primitive across any AI Gateway consumer. This source documents a specific,
    named consumer (deepsec) that layers its own tool-level cost/duration
    governors (Claim 4) on top of whatever gateway-level budget may also be
    configured — a worked example of "defense in depth" cost governance for an
    autonomous AI workload, going beyond that note's single-layer gateway
    budget coverage.

- **Novel** (what this note adds that no prior source covers):
  - **A five-stage, separately-invokable security-review pipeline
    (scan/process/revalidate/enrich/export) with a dedicated false-positive
    re-verification stage** (Claim 5): no prior corpus source documents an
    AI security-review tool splitting "find issues" from "re-check whether
    they're real" into a distinct, independently runnable pipeline stage with
    its own named verdicts.
  - **Checkpointed, resumable tool *setup* (not just resumable task execution)
    via re-invoking the identical setup command** (Claim 2): the specific
    pattern of a setup wizard itself being safely re-runnable after
    interruption, rather than only the tool's ongoing task execution being
    resumable, is new to the corpus.
  - **Tool-level per-run cost and duration ceilings on an AI review pass**
    (Claim 4, `--max-cost-usd` / `--max-duration`): a concrete, named example of
    cost governance built into the consuming application itself, distinct from
    the gateway/platform-level budget mechanisms already documented.
  - **Named cost/quality selection profiles (`best`/`value`/`budget`) with an
    explicit cost-multiplier definition for the middle tier** (Claim 8): no
    prior corpus source documents a tool converting model selection into three
    labeled tradeoff profiles with a stated multiplier (2.5x cheapest cost) for
    the "balanced" option.
  - **"Net-new findings only" as the CI exit-code rule for a security-review
    gate** (Claim 9): a specific, reusable mechanism for retrofitting a strict
    AI review gate onto an existing codebase with known findings, not
    previously documented in the corpus's security-review coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the scan (free, deterministic) →
  process (paid, AI) → revalidate (re-verification) → enrich → export pipeline
  (Claim 5, Claim 6) as a named reference architecture for any team building or
  evaluating an AI-driven code-analysis tool: split cheap deterministic
  filtering from expensive model calls, and treat "did we double-check this
  finding" as its own pipeline stage rather than a one-shot confidence score.
  Cite Claim 9's "net-new findings only" exit-code rule as a specific,
  reusable technique for adopting a strict analysis gate on an existing,
  imperfect codebase without requiring a full backlog cleanup first.

- **Chapter 03 (Safety and Verification) / Chapter 06 (Security Threat Model)**:
  Add deepsec (Claims 1, 5, 9, 10) alongside the existing GitHub Copilot
  `/security-review` coverage (`docs-github-copilot-cli-security-review.md`,
  `docs-github-copilot-app-security-review.md`) and the gh-aw malicious-code-scan
  workflow (`docs-ghaw-gallery-security-review.md`) as a third, open-source,
  self-hostable point in the AI-driven security-review landscape — distinguish
  it from those by its multi-backend model choice (Codex/Claude/Pi), its fully
  disclosed pipeline, and its CI-native PR-diff mode. Add the two-job
  execution/write privilege-separation CI pattern (Claim 10) as a named,
  cross-vendor-corroborated pattern (alongside `docs-ghaw-safe-outputs-specification.md`)
  for safely running any AI review tool against untrusted fork-PR content in CI.

- **Chapter 04 (Cost Engineering at Scale)**: Add the tool-level
  `--max-cost-usd`/`--max-duration` governors (Claim 4) and the named
  `best`/`value`/`budget` model-selection profiles (Claim 8) as concrete,
  reusable patterns for bounding spend on an autonomous, potentially
  long-running AI workload — complementary to, and layerable with, the
  gateway-level per-key budget mechanism already documented in
  `blog-vercel-ai-gateway-api-key-budgets.md`. Flag the vendor-stated
  ~3x cost / 10-20 percentage-point FP-rate tradeoff between Claude Opus and
  Claude Sonnet (Claim 7) as directional guidance only, given the lack of
  disclosed methodology.

- **Chapter 05 (Team Adoption)**: Add the single-command, checkpointed
  onboarding flow (Claims 1, 2, 3) as a case study in reducing time-to-first-
  successful-run for a new AI tool — defaulting to a managed credential path
  (Vercel AI Gateway) while preserving a bring-your-own-key escape hatch, and
  making the same setup command safely re-runnable after any interruption.

## Extraction Notes

1. **Access method and verbatim-quote confidence.** All six pages (the
   changelog and five `deepsec.sh/docs` pages) were fetched via WebFetch with
   prompts explicitly requesting verbatim, non-summarized reproduction of
   quoted text, per MINER.md §2a's caution that WebFetch runs content through a
   summarizing model. Every `Quote` field in this note reproduces text that
   WebFetch's own output returned inside quotation marks, on the premise
   (consistent with this corpus's prior practice, e.g.
   `blog-vercel-herdr-agent-sandboxes.md` Extraction Note 1) that a fetch tool
   asked to quote verbatim and returning text in quotation marks is reproducing
   the source's own wording rather than paraphrasing it. One exception is
   flagged directly in Claim 11: the fetched summary of the PR-comment
   truncation limits (600/400 characters) stated those numbers outside of
   quotation marks, so only the "GitHub's 65 KiB comment limit" fragment is
   presented as a direct quote there; the character-count figures are reported
   as stated fact, not as a verbatim quotation.
2. **Six pages fetched, one over the "up to 5" guidance.** The changelog links
   to `deepsec.sh/docs/getting-started`; from that page's parent docs index,
   five further pages were identified and four were fetched in full
   (architecture, reviewing-changes, configuration, models) alongside the
   index page itself and getting-started — six total. This slightly exceeds
   MINER.md §1's "up to 5 linked pages" guidance because the docs index is a
   thin link list rather than a content page, and each of the four content
   pages fetched afterward was the sole source for a distinct, substantive
   claim cluster (setup/CI mechanics, pipeline architecture, PR-mode/CI
   security, configuration schema, model economics) rather than duplicating
   material already captured.
3. **No customer or independent evaluation evidence.** None of the six fetched
   pages names a customer, cites an independent security evaluation, or
   discloses a benchmark methodology for the stated false-positive-reduction
   (Claim 5) or refusal-rate (Claim 7) figures. `confidence_overall` is set to
   `emerging`: the tool's existence, CLI surface, and architecture are settled
   first-party facts about a shipping open-source project, but the numeric
   quality claims are unverified vendor figures, consistent with how this note
   individually marks Claim 7 as `anecdotal`.
4. **No contradictions filed.** Reviewed
   `docs-github-copilot-cli-security-review.md`,
   `docs-github-copilot-app-security-review.md`,
   `docs-ghaw-gallery-security-review.md`, `practitioner-getsentry-sentry.md`,
   and `blog-vercel-ai-gateway-api-key-budgets.md` in full during
   cross-reference verification (MINER.md §4b). No claim in this source
   materially opposes a claim in any of those notes — see Cross-References →
   Contradicts.
5. **Prospector's triage comments.** The issue carries three separate triage
   comments across what appear to be different triage passes (novelty rated
   medium, medium, then high; the first two comments' "existing notes that
   overlap" reference generic Vercel-ecosystem notes rather than
   security-review-specific ones). This note follows the third, most specific
   comment's framing (deepsec as a novel, first-in-corpus AI security-review
   tool) and independently verified the technical summary in that comment
   against the actual fetched pages rather than trusting the triage summary at
   face value — the comment's description of the `npx deepsec init` flow and
   checkpointed setup matched the fetched getting-started page closely.
