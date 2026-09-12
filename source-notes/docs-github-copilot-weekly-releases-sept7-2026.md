---
source_url: https://github.blog/changelog/2026-09-10-github-copilot-weekly-releases-september-7
source_type: docs
title: "GitHub Copilot weekly releases — September 7"
author: GitHub (official changelog)
date_published: 2026-09-10
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: emerging
issue: "#3399"
---

# GitHub Copilot Weekly Releases — September 7

> GitHub's September 10, 2026 weekly digest covers four surfaces — the
> Copilot app, Copilot CLI, VS Code 1.137, and Copilot in JetBrains — and is
> the first corpus documentation of Jira issue integration in the Copilot
> app, of Project HydraFusion (an adaptive multi-model orchestration research
> preview for Copilot CLI that explicitly reuses the "Rubber Duck" review
> pattern for its critique workflow), of VS Code's public-preview scheduled
> agent-task automations and experimental voice mode, and of the
> repository-optional Agents-window issue/PR review experiment. It also
> restates, without new detail, the September 8, 2026 JetBrains
> enterprise-managed sandbox announcement (already fully mined in
> `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`,
> issue #3320). Because the digest's own text on HydraFusion is thin (one
> paragraph), the dedicated GitHub blog post it links to — "Project
> HydraFusion: Frontier quality via multi-model orchestration," published
> September 4, 2026 — was also fetched and mined in depth per MINER.md §1's
> instruction to follow substantive linked pages.

## Source Context

- **Type**: docs (GitHub official product changelog, September 10, 2026;
  self-tagged "Release," "1 minute read"; four sections — "GitHub Copilot
  app," "GitHub Copilot CLI," "VS Code 1.137 release updates," and "GitHub
  Copilot in JetBrains"). Fetched via `curl` with a browser user-agent
  (rather than relying solely on WebFetch AI summarization), following the
  precedent set in `docs-github-copilot-weekly-releases-aug31-2026.md`
  Extraction Note 1, which found WebFetch prone to inventing headings not
  present in the source. One linked page was followed in full: the Project
  HydraFusion announcement blog post at
  `github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/`
  (September 4, 2026, ~1,800 words, tagged "9 minutes" read, by "GitHub
  Staff"). The JetBrains sandbox link
  (`github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains/`)
  was not re-fetched because it is already the subject of a dedicated,
  fully-mined source note (`docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`,
  issue #3320). The general VS Code 1.137 release notes link
  (`aka.ms/VSCode/137`) was not fetched, consistent with this family's
  established treatment of non-Copilot-specific VS Code release notes as out
  of scope (e.g. `docs-github-copilot-weekly-releases-aug31-2026.md`
  Extraction Note 2).
- **Author credibility**: GitHub engineering team (changelog) and "GitHub
  Staff" with a named "Meet the Team" credit block (HydraFusion post: Aashna
  Garg, Shengyu Fu, Carlos Castro, Siddharth Singha Roy, Andy Salerno —
  Principal Applied Scientist, Partner Applied Science Manager, Partner
  Architect, Research Scientist II, and Principal Software Engineer
  respectively, all Code AI / GitHub Copilot). Authoritative for: the
  existence of each named feature, its availability tier/status, and the
  HydraFusion benchmark numbers as GitHub's own offline evaluation results.
  Not authoritative for: independent verification of the HydraFusion
  benchmark methodology (no third party audited "the best tuned HydraFusion
  configuration" claim), how HydraFusion's routing decision is exposed for
  the developer's own evaluation/observability, or real-world production
  behavior of any of the four preview/experimental features (Jira
  integration's status is not stated as GA or preview in the digest text
  itself).
- **Scope**: A weekly digest covering the period since the prior weekly
  release (week of September 7, 2026), plus the fully-followed HydraFusion
  announcement post it links to. Does NOT cover: Visual Studio, Eclipse,
  Xcode, GitHub Mobile, configuration/admin-policy detail for Jira
  integration, HydraFusion's training data or model-pool composition beyond
  "models across multiple providers," or the JetBrains sandbox feature
  beyond what is already covered in the dedicated note for issue #3320.

## Extracted Claims

### Claim 1: The Copilot app now lets developers bring Jira issues into a shared canvas, choose what moves forward, and have Copilot carry the context into investigation, implementation, and pull request preparation

- **Evidence**: "GitHub Copilot app" section, sole bullet, changelog.
- **Confidence**: emerging (no GA/preview status stated in the digest text
  itself, unlike every other item in this digest, which explicitly states
  "public preview," "experimental," or "/experimental")
- **Quote**: "Turn Jira issues into action. Bring Jira issues into a shared canvas, choose what moves forward, and let Copilot carry the context into investigation, implementation, and pull request preparation."
- **Our assessment**: This is the first corpus documentation of a
  third-party issue-tracker (Jira) integration in the standalone Copilot
  app, as distinct from GitHub's own Issues/Projects surface (documented in
  `docs-github-copilot-issues-projects-sessions.md`). The phrase "choose
  what moves forward" implies a human-in-the-loop triage step before Copilot
  acts, consistent with the guide's general "verify before execute" pattern,
  but the digest gives no mechanism detail — how Jira issues sync into the
  canvas, whether this requires a Jira admin-side app install, or which
  Copilot plans include it. For Ch05 (Team Adoption): flag as relevant for
  organizations using Jira alongside GitHub, but treat as unconfirmed for
  rollout planning until a dedicated Jira-integration changelog (in the
  style of the dedicated Gemini 3.8 Flash or HydraFusion announcements)
  provides plan-tier and configuration detail.

### Claim 2: Project HydraFusion, now in Copilot CLI's `/experimental`, delivers automated semantic routing between local, cloud, and compound models — selectable like any other model, choosing a workflow that balances performance, cost, and latency per task

- **Evidence**: Changelog "GitHub Copilot CLI" section; corroborated in far
  greater depth by the dedicated HydraFusion blog post.
- **Confidence**: emerging (explicitly a "research preview," per the
  HydraFusion post's own framing, not GA)
- **Quote**: "Project HydraFusion is now in /experimental. HydraFusion delivers automated semantic routing between local, cloud, and compound models. You select HydraFusion like any other model, and it chooses a workflow that balances performance, cost, and latency for each task."
- **Our assessment**: This extends the CLI's existing "auto" model-selection
  routing (`docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
  Claim 2, which already evaluates "reasoning, code generation complexity,
  bug diagnosis difficulty, tool orchestration needs" to pick *one* model)
  into something categorically different: HydraFusion doesn't just pick a
  model, it constructs a multi-step *workflow* — potentially invoking
  several models in sequence for a single task (see Claim 3). The HydraFusion
  post itself frames this lineage explicitly: "Earlier this year, we made
  that easier by launching Auto model selection... Today, we're introducing
  Project HydraFusion... runtime orchestration." For Ch02 (Model Selection &
  Routing): document HydraFusion as the next step beyond single-model auto
  routing — from "pick the best model" to "construct the best workflow,"
  still opt-in and CLI-only as of this preview.

### Claim 3: HydraFusion chooses one of three execution patterns per request — Single (one model solves directly), Cascade (an efficient model drafts, a quality gate decides whether to accept or escalate to a stronger model), or Critique (one model drafts, an independent read-only critic from a different model family reviews it "following the same review pattern as Rubber Duck," and the drafting model revises once)

- **Evidence**: HydraFusion blog post, bulleted list under "For each request,
  HydraFusion currently chooses one of three execution patterns."
- **Confidence**: emerging (research preview; the post states these are the
  patterns "currently" available, implying the set may change)
- **Quote**: "Single. One selected model solves the task directly." / "Cascade. An efficient model drafts a solution and a quality gate decides whether to accept it or escalate to a stronger model." / "Critique. One model drafts a result, an independent read-only critic from a different model family reviews it (following the same review pattern as Rubber Duck), and the drafting model revises once."
- **Our assessment**: This is a direct, source-stated link to an existing
  corpus feature: `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`
  Claim 1 documents Rubber Duck as a GA, manually-invoked (`/rubber-duck`)
  CLI peer-review agent. HydraFusion's Critique pattern automates that same
  review shape (draft → independent critic → revise) as one *automatically
  selected* leg of a routing decision, rather than a practitioner-invoked
  command — the practitioner no longer decides when to get a second opinion;
  HydraFusion decides for them, per-request. The "different model family"
  detail is new: unlike a practitioner manually invoking `/rubber-duck`
  (where the reviewing model is whatever the session is configured to
  use), HydraFusion's Critique pattern deliberately picks a *different*
  model family for the critic, presumably to reduce correlated blind spots
  between drafter and reviewer. For Ch02 (Harness Engineering) and Ch04
  (Agentic Workflows — Multi-Agent Patterns): document HydraFusion's
  Cascade and Critique patterns as production-adjacent, automated instances
  of the "efficient-model-first, escalate-on-failure" and
  "draft-then-independent-critique" patterns the guide already covers
  conceptually, now implemented as a single selectable CLI "model."

### Claim 4: In offline evaluations across three agentic coding benchmarks, HydraFusion matched or exceeded Claude Opus 5's verified task quality at substantially lower estimated cost — improving quality by 4.9 percentage points at 67% lower cost on TerminalBench 2.1, coming within 1.5 points at 36% lower cost on DeepSWE, and within 0.1 points at 65% lower cost on CheckpointBench (GitHub's internal benchmark)

- **Evidence**: HydraFusion blog post, "Benchmarking results" section and
  per-benchmark subsections; a results table; comparison baseline is Claude
  Opus 5 (and GPT-5.6 Sol, though GPT-5.6 Sol's specific numbers are not
  broken out in the prose, only "used ... as comparison baselines").
- **Confidence**: emerging (GitHub's own offline evaluation, explicitly
  scoped as "specific to the evaluated benchmark revisions, workflow
  configurations, model pool, and pricing assumptions"; no third-party
  reproduction)
- **Quote**: "On TerminalBench 2.1, it improved verified task quality by 4.9 percentage points at 67% lower estimated cost compared with Claude Opus 5." / "On this benchmark, HydraFusion comes within 1.5 percentage points of Opus 5 while reducing cost by 36%, demonstrating a compelling quality-cost tradeoff for complex real-world engineering tasks." / "On this benchmark, HydraFusion comes within 0.1 percentage points of Opus 5 at 65% lower cost."
- **Our assessment**: The one benchmark where HydraFusion *exceeds* the Opus
  5 baseline (TerminalBench 2.1, +4.9 points) is also the one GitHub's own
  "Hill-climbing HydraFusion" section attaches a caveat to. That section
  says of it: "TerminalBench 2.1 was one of several benchmarks used during
  development." It then adds, in the next sentence: "Its relative saturation
  makes broader validation important, so the three-benchmark evaluation also
  includes DeepSWE's more demanding repository-level tasks." The post does
  *not* claim TerminalBench was weighted more heavily than the others during
  tuning — on intent it says the reverse, that the team optimized "across
  the evaluation sets rather than for any single benchmark" (Claim 8). What
  it does volunteer is that the benchmark carrying the strongest headline
  number is the one whose saturation GitHub itself treats as a reason to
  validate elsewhere, and that the two benchmarks it positions as that
  broader validation (DeepSWE, CheckpointBench) show HydraFusion trailing
  Opus 5 slightly on quality rather than exceeding it. This is
  a self-disclosed caveat, not an external critique, and it means the
  practitioner-relevant takeaway is closer to "comparable quality at
  meaningfully lower cost" than "better quality at lower cost," despite the
  post's "matched or exceeded" framing. For Ch02: cite the cost reduction
  (36–67% depending on task type) as the more robust claim than the
  TerminalBench quality delta.

### Claim 5: HydraFusion is built around five operating principles — complete accounting, bounded execution, isolated review, fail-safe application, and validated routing — with review steps run in isolated, tool-less contexts and no patch applied if a workflow is cancelled or fails validation

- **Evidence**: HydraFusion blog post, "Building HydraFusion" section,
  five-item bulleted list with one-sentence elaborations.
- **Confidence**: emerging (architectural description of a research-preview
  system; no external audit of whether these principles hold under load)
- **Quote**: "Complete accounting. Aggregate cost and usage across every workflow leg, including drafting, critique, revision, escalation, retry, and fallback." / "Isolated review. Run review steps in isolated, tool-less contexts, while solver steps use the shared workspace and normal permission-aware agent loop. This allows models to assess the work independently without modifying the repository." / "Fail-safe application. Apply no patch when the workflow is cancelled or fails validation, preventing incomplete changes from reaching the repository."
- **Our assessment**: "Isolated review" is the architectural detail that
  makes HydraFusion's Critique pattern (Claim 3) safe to automate: the critic
  model runs without tool/write access, so an adversarial or buggy critique
  cannot itself modify the repository — a materially different trust
  boundary than a solver-role model, which "use[s] the shared workspace and
  normal permission-aware agent loop." "Fail-safe application" is the
  guarantee that an interrupted multi-leg workflow cannot leave a
  partially-applied patch. Neither principle is new to the corpus in
  concept (isolation-of-review and fail-safe-apply are established harness
  patterns), but this is the first corpus documentation of GitHub stating
  them as explicit, named design principles for a production-directed
  multi-model orchestration system. For Ch02 (Harness Engineering):
  document these five principles as a reference checklist for teams
  designing their own multi-model or multi-agent orchestration harnesses,
  independent of whether they use HydraFusion itself.

### Claim 6: HydraFusion deliberately withholds intermediate drafts from view during a multi-step workflow, showing only workflow stages until it returns one coherent result — a design trade-off GitHub is still evaluating, not a limitation being hidden

- **Evidence**: HydraFusion blog post, "Showing progress without showing
  unfinished work" subsection, structured as Today/Why/What we're
  learning/Next.
- **Confidence**: anecdotal (self-reported design rationale and an
  explicitly open, unresolved UX question — "we're actively exploring
  better progress updates")
- **Quote**: "Today: HydraFusion shows workflow stages but holds intermediate drafts until it returns one coherent result." / "Why: Those drafts may be reviewed, revised, or discarded, so showing them live could make unfinished work appear final." / "What we're learning: Waiting without enough visibility is a real trade-off for developers."
- **Our assessment**: This is a candid, first-party acknowledgment of a
  concrete UX cost of the Cascade/Critique patterns: a practitioner watching
  a HydraFusion session sees less real-time signal than they would watching
  a single model work, because a draft that might be discarded (rejected by
  the Cascade quality gate, or revised after Critique) is deliberately not
  surfaced. GitHub frames this as an active, unresolved trade-off rather
  than a settled design decision. For Ch01 (Daily Workflows): note that
  HydraFusion sessions may feel less transparent moment-to-moment than a
  direct single-model session, even though the final result may be higher
  quality or lower cost — set practitioner expectations accordingly during
  the research preview.

### Claim 7: HydraFusion usage is billed by the tokens consumed by the underlying models it invokes, at each model's standard rate, and is available to users on all GitHub Copilot plans through Copilot CLI's `/experimental`

- **Evidence**: HydraFusion blog post, "Now available as a research preview"
  section.
- **Confidence**: settled (direct first-party statement of pricing
  mechanics and plan availability)
- **Quote**: "HydraFusion is available to users on all GitHub Copilot plans through /experimental in GitHub Copilot CLI. Usage is based on the tokens consumed by the models HydraFusion uses, priced at each model's standard rate."
- **Our assessment**: "All GitHub Copilot plans" is broader access than
  several other CLI experimental features documented elsewhere in this
  corpus, which are sometimes plan-gated even at preview (e.g., the
  free/student tier restriction documented in
  `docs-github-copilot-free-student-auto-only-model-selection.md`). Because
  a multi-leg Cascade or Critique workflow invokes more than one model call
  per task, and billing aggregates "every workflow leg" (per Claim 5's
  "complete accounting" principle), practitioners on usage-capped plans
  should expect a single HydraFusion request to consume more of their
  budget than an equivalent single-model request — the post does not state
  an average or worst-case multiplier. For Ch05 (Team Adoption — Cost
  Governance): flag this as an open cost-forecasting question for teams
  piloting HydraFusion under a fixed AI-credit budget.

### Claim 8: HydraFusion's routing policies were tuned using beam search against a frozen baseline on quality, cost, and failure modes, evaluated across three benchmarks (CheckpointBench, DeepSWE, TerminalBench 2.1) rather than optimized for any single one, using CheckpointBench specifically because it was curated from real GitHub Copilot agentic coding session trajectories

- **Evidence**: HydraFusion blog post, "Hill-climbing HydraFusion" section.
- **Confidence**: emerging (methodology disclosure for a research-preview
  system; the post also discloses that two operational evaluation-harness
  failures between August 11–25, 2026 produced invalid runs that were
  excluded and corrected)
- **Quote**: "We refined HydraFusion repeatedly across CheckpointBench, DeepSWE, and TerminalBench 2.1, optimizing across the evaluation sets rather than for any single benchmark." / "Instead of manually tuning thresholds, we used beam search to build the optimal decision policy. Each candidate was measured against a frozen baseline on quality, cost, and failure modes, so improvements were evaluated on stable ground."
- **Our assessment**: The disclosure of "two operational failures in the
  evaluation harness" producing "invalid runs" between August 11–25, 2026 —
  volunteered rather than prompted — is a notable transparency practice: it
  means the TerminalBench 2.1 "hill-climbing" chart (Figure 2, not
  independently reproducible from the post's text) has a documented gap
  and correction, rather than presenting a clean monotonic improvement
  curve. This level of methodology transparency (frozen-baseline beam
  search, disclosed harness failures) is more detailed than typical
  vendor-benchmark disclosures elsewhere in the corpus. No specific guide
  action follows from this claim beyond noting it as a data point on
  GitHub's benchmark-disclosure practices.

### Claim 9: VS Code 1.137 adds public-preview support for scheduling recurring agent tasks to run hourly, daily, or weekly, or on demand, via "automations"

- **Evidence**: Changelog "VS Code 1.137 release updates" section, first
  bullet.
- **Confidence**: emerging (explicitly public preview)
- **Quote**: "Schedule recurring agent tasks to run hourly, daily, or weekly, or run them on demand with automations, now in public preview."
- **Our assessment**: "Automations" is an established term in this corpus —
  `docs-github-copilot-automations-comment-trigger.md` Claim 4 documents
  Copilot cloud agent automations as configured via the GitHub.com "Agents
  tab → Automations" sidebar entry, with (per that note's Claim 6) four
  pre-existing trigger types (schedule, issue-created, PR-opened,
  PR-synchronized) plus a fifth comment trigger added in August 2026 — all
  configured on GitHub.com, not from inside an IDE. This VS Code 1.137 item
  does not state whether it is a new *configuration surface* for that same
  underlying cloud-agent automations system (i.e., VS Code now lets you
  create/manage the same automations without leaving the editor) or a
  separate, VS Code-local scheduling primitive. The phrasing "schedule
  recurring agent tasks... with automations" reads as the former (using the
  existing automations system from a new surface) rather than introducing a
  new trigger taxonomy, but the digest does not confirm this explicitly.
  For Ch02 (Harness Engineering — Workspace Management): if VS Code is
  indeed a new automations configuration surface, document it as removing
  the GitHub.com round-trip previously required to set up a scheduled or
  on-demand cloud-agent task; flag the surface-vs-taxonomy ambiguity as
  unresolved pending a dedicated changelog entry (the pattern this family of
  sources typically produces for major individual features, e.g. the
  HydraFusion or Gemini 3.8 Flash dedicated posts).

### Claim 10: VS Code 1.137 adds an experimental voice mode letting developers talk to, interrupt, or redirect Copilot while it works on their code

- **Evidence**: Changelog "VS Code 1.137 release updates" section, second
  bullet.
- **Confidence**: emerging (explicitly experimental)
- **Quote**: "Voice mode is now in experimental so you can talk to, interrupt, or redirect Copilot while it works on your code."
- **Our assessment**: This is a distinct capability from the CLI's existing
  GA voice input, documented in
  `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` Claim 4 and
  Claim 5 — that feature is one-shot dictation ("Hold the space bar... and
  talk to input a prompt"), confirmed to run entirely on-device with no
  interruption/redirection capability described. This VS Code feature
  explicitly supports *interrupting and redirecting* an in-progress agent
  by voice — a live, bidirectional interaction pattern, not a
  speech-to-text input method for composing a prompt before sending it. It
  is also a different feature from Anthropic's own "voice mode" for hard
  reasoning problems (`blog-anthropic-voice-mode-tools-multilingual.md`)
  and from the ChatGPT voice-mode critiques in
  `blog-simonwillison-voice-mode-weaker.md` and
  `blog-simonwillison-gptlive-voice-delegation.md`, none of which cover an
  in-progress coding-agent interruption pattern. The digest does not state
  whether voice mode processes audio locally (as the CLI's GA voice input
  does) or in the cloud — an open privacy/enterprise-adoption question
  distinct from, but analogous to, the one the CLI feature already
  resolved. For Ch01 (Daily Workflows): document as a new interaction
  pattern — hands-free mid-task steering — distinct from the CLI's
  dictation-only voice input, and flag the on-device-vs-cloud processing
  question as unconfirmed.

### Claim 11: VS Code 1.137 adds an experimental option to review issue and pull request details directly in the Agents window, even when the repository is not open

- **Evidence**: Changelog "VS Code 1.137 release updates" section, third
  bullet.
- **Confidence**: emerging (explicitly experimental)
- **Quote**: "New in experimental, review issue and pull request details directly in the Agents window, even when the repository is not open."
- **Our assessment**: "Even when the repository is not open" is the notable
  detail — it decouples GitHub issue/PR review from having a local
  workspace open at all, which is a different repository-optionality
  pattern from the ones already in the corpus: the June 2026 CLI
  experimental terminal's Issues/PR tabs
  (`docs-github-copilot-cli-rubber-duck-scheduling-voice.md` Claim 7)
  require an active CLI session (implicitly repository-scoped), and
  `docs-github-copilot-chat-agent-sessions.md` covers searching *past
  sessions*, not browsing GitHub issues/PRs independent of a repository
  context. No prior corpus source documents a VS Code surface for reading
  GitHub issue/PR content with no repository open at all. For Ch01: note as
  a lightweight triage pattern — a developer can review incoming issues/PRs
  from VS Code's Agents window without first opening (or having previously
  cloned) the relevant repository.

### Claim 12: GitHub Copilot in JetBrains now offers enterprise-managed sandbox policies in public preview, letting administrators centrally control sandbox enablement, filesystem and network access, proxy settings, developer-tool access, and macOS Keychain access

- **Evidence**: Changelog "GitHub Copilot in JetBrains" section, sole
  bullet, linking to "the previous Copilot in JetBrains changelog"
  (`github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains/`).
- **Confidence**: emerging (explicitly public preview; also see
  Cross-References for a same-day contradiction already filed against the
  dedicated source)
- **Quote**: "Now in public preview, enterprise administrators can centrally configure sandbox behavior for GitHub Copilot in JetBrains IDEs. Managed policies can control sandbox enablement, filesystem and network access, proxy settings, developer-tool access, macOS Keychain access, and more."
- **Our assessment**: This is a verbatim-equivalent restatement, two days
  later, of `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`
  Claim 1, which already extracted this same announcement in full depth —
  including the notable finding that the changelog's managed-sandbox claim
  conflicts with the "Enterprise managed settings reference" page's own
  "Supported keys" table (filed as **issue #3334**, not resolved in either
  note). This weekly digest adds no new detail beyond that dedicated note;
  no additional guide action follows from this restatement.

## Concrete Artifacts

### Full weekly digest — September 7, 2026 (published September 10, 2026), verbatim transcript

Extracted from raw HTML via `curl` with a browser user-agent (not WebFetch
summarization alone), per MINER.md §2a and this family's established
precedent.

```
GitHub Copilot weekly releases — September 7
Source: github.blog/changelog, published 2026-09-10, retrieved 2026-09-12
Release, 1 minute read

INTRO
  This week, GitHub Copilot introduces Jira integration in Copilot app and
  adaptive model orchestration with Project HydraFusion in Copilot CLI. We
  also introduced new agent automation in Visual Studio Code and expanded
  enterprise controls for Copilot in JetBrains.

GITHUB COPILOT APP
  [Claim 1]
  Turn Jira issues into action. Bring Jira issues into a shared canvas,
  choose what moves forward, and let Copilot carry the context into
  investigation, implementation, and pull request preparation.
  (Link: "Download the Copilot app" — github.com/features/ai/github-app)

GITHUB COPILOT CLI
  [Claim 2]
  Project HydraFusion is now in /experimental. HydraFusion delivers
  automated semantic routing between local, cloud, and compound models.
  You select HydraFusion like any other model, and it chooses a workflow
  that balances performance, cost, and latency for each task.
  (Link: "read the Project HydraFusion blog post" —
   github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/
   — followed in full, see Claims 2-8 detail above and separate transcript
   below)
  (Link: "Install Copilot CLI" — github.com/features/copilot/cli)

VS CODE 1.137 RELEASE UPDATES
  [Claim 9]
  - Schedule recurring agent tasks to run hourly, daily, or weekly, or run
    them on demand with automations, now in public preview.
  [Claim 10]
  - Voice mode is now in experimental so you can talk to, interrupt, or
    redirect Copilot while it works on your code.
  [Claim 11]
  - New in experimental, review issue and pull request details directly in
    the Agents window, even when the repository is not open.
  (Link: "full release notes" — aka.ms/VSCode/137, not fetched, general
   non-Copilot-specific release notes)

GITHUB COPILOT IN JETBRAINS
  [Claim 12]
  Now in public preview, enterprise administrators can centrally configure
  sandbox behavior for GitHub Copilot in JetBrains IDEs. Managed policies
  can control sandbox enablement, filesystem and network access, proxy
  settings, developer-tool access, macOS Keychain access, and more.
  (Link: "Learn more in the previous Copilot in JetBrains changelog" —
   github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains/
   — already fully mined as
   docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md,
   issue #3320; not re-fetched)
```

### Project HydraFusion announcement post — verbatim excerpts (September 4, 2026)

```
Title: "Project HydraFusion: Frontier quality via multi-model orchestration"
Byline: GitHub Staff · @github, September 4, 2026, 9 minutes

Summary line:
  "In controlled offline evaluations, HydraFusion's selective coding
  workflows matched or exceeded the evaluated Opus 5 baseline while
  reducing estimated workflow cost. Now available as a research preview
  in GitHub Copilot."

Availability [Claim 7]:
  "HydraFusion is available to users on all GitHub Copilot plans through
  /experimental in GitHub Copilot CLI. Usage is based on the tokens
  consumed by the models HydraFusion uses, priced at each model's
  standard rate."

To try HydraFusion in Copilot CLI:
  - Run /update to install the latest version
  - Run /experimental on
  - Run /model, then select HydraFusion (Research Preview)

Execution patterns [Claim 3]:
  - Single. One selected model solves the task directly.
  - Cascade. An efficient model drafts a solution and a quality gate
    decides whether to accept it or escalate to a stronger model.
  - Critique. One model drafts a result, an independent read-only critic
    from a different model family reviews it (following the same review
    pattern as Rubber Duck), and the drafting model revises once.

Five operating principles [Claim 5]:
  - Complete accounting: aggregate cost/usage across every workflow leg
    (drafting, critique, revision, escalation, retry, fallback)
  - Bounded execution: explicit timeout/cancellation behavior per leg
  - Isolated review: review steps run in isolated, tool-less contexts;
    solver steps use the shared workspace and normal permission-aware
    agent loop
  - Fail-safe application: no patch applied if workflow is cancelled or
    fails validation
  - Validated routing: workflow definitions, model bindings, fallback
    behavior, and model availability verified before execution begins

Benchmark table (Table 1, relative to Claude Opus 5) [Claim 4]:
  Benchmark          Cost vs. Opus 5   Quality vs. Opus 5
  TerminalBench 2.1  67% lower         +4.9 points
  DeepSWE            36% lower         -1.5 points
  CheckpointBench    65% lower         -0.1 points

Practitioner quote:
  "So far, the reasoning and task solving capability [of HydraFusion] is
  at or better than Opus."
  — Principal Software Engineer at Microsoft

Progress-visibility trade-off [Claim 6]:
  Today: HydraFusion shows workflow stages but holds intermediate drafts
    until it returns one coherent result.
  Why: Those drafts may be reviewed, revised, or discarded, so showing
    them live could make unfinished work appear final.
  What we're learning: Waiting without enough visibility is a real
    trade-off for developers.
  Next: Actively exploring better progress updates, guided by research
    preview feedback.

Development methodology [Claim 8]:
  "We refined HydraFusion repeatedly across CheckpointBench, DeepSWE, and
  TerminalBench 2.1, optimizing across the evaluation sets rather than
  for any single benchmark."
  "Instead of manually tuning thresholds, we used beam search to build
  the optimal decision policy. Each candidate was measured against a
  frozen baseline on quality, cost, and failure modes."
  Disclosed harness issue: "Between August 11 and August 25, two
  operational failures in the evaluation harness produced invalid runs.
  Those failures were excluded from the performance trend, corrected."

Scope guidance for the preview:
  "For this preview, first-turn, single-prompt coding tasks are the best
  place to start. We'll be focusing on strong multi-turn performance with
  longer, iterative sessions next."

Team credited: Aashna Garg (Principal Applied Scientist, Code AI),
  Shengyu Fu (Partner Applied Science Manager, Code AI), Carlos Castro
  (Partner Architect, GitHub Copilot), Siddharth Singha Roy (Research
  Scientist II, Code AI), Andy Salerno (Principal Software Engineer,
  GitHub Copilot)
```

*Sources: raw HTML of
https://github.blog/changelog/2026-09-10-github-copilot-weekly-releases-september-7
and
https://github.blog/ai-and-ml/github-copilot/project-hydrafusion-frontier-quality-via-multi-model-orchestration/,
both fetched directly via `curl` with a browser user-agent on 2026-09-12,
block-level tags converted to line breaks, remaining markup stripped. All
`Quote` fields above were checked by exact substring match against these
transcripts.*

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`,
`docs-github-copilot-cli-auto-model-selection-task-based-routing.md`,
`docs-github-copilot-automations-comment-trigger.md`,
`docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`,
`docs-github-copilot-free-student-auto-only-model-selection.md`,
`docs-github-copilot-issues-projects-sessions.md`,
`docs-github-copilot-chat-agent-sessions.md`, and
`blog-thoughtworks-omahony-fugu-model-routing-critique.md` were re-read
directly in those notes (via `### Claim N:` headings, counted top-to-bottom
in document order) before citing, per MINER.md §4b.

- **Corroborates** `docs-github-copilot-jetbrains-enterprise-managed-sandbox-sept2026.md`
  (Claim 1, enterprise-managed sandbox policies for JetBrains): Claim 12 of
  this note restates the identical public-preview announcement two days
  later, with no new detail.

- **Extends** `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
  (Claim 2, task-aware single-model routing across reasoning/code-gen/bug-
  diagnosis/tool-orchestration dimensions): Claim 2 of this note documents
  HydraFusion as the next step beyond single-model selection — constructing
  a multi-step *workflow* (Single/Cascade/Critique, Claim 3) rather than
  picking one model per request.

- **Extends** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`
  (Claim 1, GA manually-invoked `/rubber-duck` peer-review agent): Claim 3
  of this note documents HydraFusion's Critique execution pattern as an
  automated, per-request application of the same draft-then-independent-
  critique shape, explicitly self-described by GitHub as "following the
  same review pattern as Rubber Duck" — the first corpus case of a vendor
  changelog directly naming the reuse of one of its own previously-shipped
  patterns inside a new orchestration feature.

- **Contrasts with** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`
  (Claim 4 and Claim 5, GA voice *input* — one-shot dictation, confirmed
  on-device processing): Claim 10 of this note (VS Code experimental voice
  *mode* — interrupt/redirect an in-progress agent) is a different
  interaction shape (bidirectional, mid-task steering vs. one-shot
  dictation) on a different surface (VS Code vs. CLI), with on-device vs.
  cloud processing left unstated for the new feature. Not a contradiction —
  distinct features on distinct surfaces — but flagged because the CLI
  precedent set a specific privacy expectation (local-only audio) that this
  digest does not confirm or deny for VS Code's voice mode.

- **Extends** `docs-github-copilot-automations-comment-trigger.md` (Claim 4,
  Copilot cloud agent automations configured via GitHub.com's "Agents tab →
  Automations," and Claim 6, four-plus-one existing trigger types): Claim 9
  of this note (VS Code 1.137 scheduling recurring/on-demand agent tasks
  "with automations") appears to reference the same underlying automations
  system from a new IDE-native configuration surface, though the digest
  does not confirm whether VS Code is a new configuration surface for the
  existing system or introduces a separate scheduling primitive — flagged
  as an open question, not resolved here.

- **Distinct from** `docs-github-copilot-issues-projects-sessions.md`
  (GitHub-native Issues/Projects integration) and
  `docs-github-copilot-chat-agent-sessions.md` (searching past chat
  sessions): Claim 1 of this note (Jira issues into a shared canvas) is a
  third-party issue-tracker integration, distinct from both GitHub-native
  issue handling and session search/retrieval.

- **Extends and contrasts with** `blog-thoughtworks-omahony-fugu-model-routing-critique.md`
  (Claim 7 and Claim 8: the argument that opaque, platform-layer model
  routing is a design flaw because the application team cannot observe or
  evaluate the routing decision, and that Fugu's own FAQ confirms engineers
  cannot see which model answered a given query): HydraFusion (Claims 2-5
  of this note) is architecturally similar to the pattern that source
  critiques — an opaque platform-layer router the developer selects "like
  any other model" without configuring or inspecting its internal routing
  logic — but is not treated here as a direct contradiction. The two
  sources address different contexts: the Fugu critique is about routing
  logic for an application team's *own* product capabilities (where the
  author argues the team needs its own evals and observability over
  routing), while HydraFusion is a routing layer *internal to a
  third-party coding assistant* the developer is using as a consumer of
  the tool, not building on top of as an application platform. HydraFusion
  does retain internal accounting and diagnostics per workflow leg (Claim
  5's "complete accounting" principle), which is a partial answer to the
  Fugu critique's observability concern, though that accounting is not
  described as exposed to the end developer for their own evaluation
  purposes. This is a genuine tension worth a chapter callout but does not
  meet MINER.md §4a's bar for a formal contradiction issue — the two
  sources are not making opposing claims about the same fact, they differ
  in whether the "opacity" concern applies to build-your-own-application
  routing versus use-a-vendor's-built-in coding-agent routing (a
  conditioning variable, not a contradiction).

- **Contradicts**: None filed as a new contradiction issue from this note's
  own extraction. Claim 12 (JetBrains sandbox) restates an announcement
  whose underlying contradiction (managed-sandbox capability vs. the
  "Supported keys" reference page marking `sandbox` "Not supported" for
  JetBrains) was already filed as **issue #3334** by the dedicated source
  note; this note does not add new information to that question.

- **Novel**:
  - First corpus documentation of Jira issue-tracker integration in the
    standalone Copilot app (Claim 1).
  - First corpus documentation of Project HydraFusion — adaptive
    multi-model workflow orchestration (Single/Cascade/Critique patterns),
    its five operating principles, its three-benchmark evaluation results,
    its self-disclosed progress-visibility trade-off, and its
    beam-search/frozen-baseline tuning methodology (Claims 2-8).
  - First corpus documentation of a vendor changelog explicitly naming its
    own reuse of a previously-shipped feature (Rubber Duck) as the design
    basis for a new feature's review step (Claim 3).
  - First corpus documentation of VS Code-native scheduling for recurring
    or on-demand agent tasks via "automations" (Claim 9).
  - First corpus documentation of an interruptible, bidirectional
    "voice mode" for steering an in-progress coding agent, as distinct from
    one-shot voice dictation (Claim 10).
  - First corpus documentation of reviewing GitHub issue/PR details in a
    VS Code surface with no repository open at all (Claim 11).

## Guide Impact

### Chapter 02: Model Selection & Routing / Harness Engineering

- **HydraFusion as workflow-level orchestration beyond single-model
  routing**: Document HydraFusion (Claims 2-3) as the corpus's first
  vendor-shipped example of routing that constructs a multi-step workflow
  (Single/Cascade/Critique) rather than selecting a single model per
  request, extending the existing "auto model selection" pattern family.
- **Five-principle checklist for multi-model orchestration harnesses**:
  Add HydraFusion's stated design principles (Claim 5 — complete
  accounting, bounded execution, isolated review, fail-safe application,
  validated routing) as a reference checklist for teams building their own
  multi-agent or multi-model harnesses, independent of whether they adopt
  HydraFusion itself. "Isolated review" (tool-less critic contexts) is
  the most actionable detail — it is what makes automated critique safe to
  run without human gating.
- **Rubber Duck reuse as a named design lineage**: Note that GitHub itself
  frames HydraFusion's Critique pattern as reusing the Rubber Duck review
  pattern (Claim 3) — a concrete example of a vendor building automated
  orchestration on top of a previously-manual verification primitive,
  worth citing as a model for teams evolving their own manual
  review-agent patterns toward automatic invocation.
- **Cost-quality tradeoff nuance for benchmark claims**: When citing
  HydraFusion's benchmark results (Claim 4), lead with the cost reduction
  (36-67%) rather than the quality claim, since the one benchmark showing
  a quality *improvement* over Opus 5 is also the one GitHub's own text
  says received the most tuning attention during development.

### Chapter 01: Daily Workflows

- **Progress-visibility trade-off in orchestrated sessions**: Document
  HydraFusion's deliberate withholding of intermediate drafts (Claim 6) as
  a UX cost practitioners should expect from multi-model orchestration
  tools generally, not just HydraFusion specifically — set expectations
  that "less visible progress" can accompany "higher quality or lower
  cost" results.
- **Voice mode as mid-task steering, distinct from dictation**: Add VS
  Code's experimental voice mode (Claim 10) as a new interaction pattern —
  interrupting/redirecting an in-progress agent by voice — distinct from
  the CLI's existing GA voice input (one-shot dictation). Flag the
  on-device-vs-cloud processing question as unconfirmed pending a
  dedicated changelog.
- **Repository-optional issue/PR triage in VS Code**: Note the new
  Agents-window issue/PR review option (Claim 11) as a lightweight triage
  workflow that does not require the repository to be open or cloned.

### Chapter 05: Team Adoption — Cost Governance / Enterprise Integration

- **HydraFusion cost-forecasting caveat**: Flag for teams piloting
  HydraFusion (Claim 7) that per-leg billing across a multi-model workflow
  means a single HydraFusion request likely consumes more of a fixed
  AI-credit or usage budget than an equivalent single-model request — no
  average multiplier is disclosed, so teams should measure their own usage
  before broad rollout.
- **Jira integration as a third-party issue-tracker bridge**: Add Copilot
  app's Jira integration (Claim 1) to the guide's coverage of third-party
  tool integrations, flagged as unconfirmed for plan-tier and
  configuration requirements pending a dedicated changelog.
- **Automations configuration surface expansion, pending confirmation**:
  If VS Code's new scheduling option (Claim 9) proves to be a new
  configuration surface for the existing GitHub.com-based automations
  system, update the automations deployment guidance
  (from `docs-github-copilot-automations-comment-trigger.md`) to note that
  automations can now potentially be created without leaving the IDE.

## Extraction Notes

1. **HydraFusion blog post followed per MINER.md §1**: The weekly digest's
   own HydraFusion paragraph is one sentence; the linked dedicated blog post
   (~1,800 words) was fetched and mined in full, since it is clearly the
   more substantive and novel source and matches the Prospector's
   triage-comment emphasis on HydraFusion as the highest-signal item. The
   JetBrains sandbox link was deliberately *not* re-fetched because it
   already has a dedicated, fully-mined source note (issue #3320) with no
   new information in this digest's one-paragraph restatement.
2. **Raw HTML fetched via `curl`, not WebFetch summarization**: Both pages
   were fetched directly with a browser user-agent and parsed by stripping
   markup from the relevant content region, per the precedent in
   `docs-github-copilot-weekly-releases-aug31-2026.md` Extraction Note 1
   (which found WebFetch prone to inventing headings). For the HydraFusion
   post specifically, the page's `<article>` tags at the end of the HTML
   turned out to be unrelated "related posts" widgets; the actual post body
   was located by finding the first occurrence of a known heading anchor
   (`h-adaptive-multi-model-orchestration`) and extracting outward from
   there. All `Quote` fields above were checked by exact substring match
   against the raw HTML (including confirming the curly-apostrophe
   character `'` used in "HydraFusion's" and "each model's standard rate").
3. **Jira integration status is genuinely unconfirmed, not an extraction
   gap**: Every other item in this digest and the HydraFusion post states
   an explicit availability tier (public preview, experimental,
   /experimental, or GA). The Jira integration bullet states none — this
   is reported as-is in Claim 1 rather than assumed to be GA.
4. **VS Code "automations" surface question left open, not resolved by
   inference**: Claim 9's relationship to the pre-existing GitHub.com
   automations system (documented in
   `docs-github-copilot-automations-comment-trigger.md`) is plausible but
   not confirmed by this source; Cross-References and Guide Impact both
   flag this explicitly as open rather than presenting an inference as
   fact.
5. **Fugu contrast considered for a contradiction filing and declined**:
   See Cross-References → "Extends and contrasts with" entry for
   `blog-thoughtworks-omahony-fugu-model-routing-critique.md`. This was
   weighed against MINER.md §4a's filing bar and judged to be a
   conditioning-variable difference (build-your-own-application routing
   vs. use-a-vendor's-built-in-tool routing) rather than two sources making
   opposing claims about the same fact, so no contradiction issue was
   filed.
6. **Cross-reference verification performed**: All `Claim N` citations above
   were checked against each cited note's actual claim numbering by
   re-reading the note in full before citing, per MINER.md §4b.
7. **Apostrophe normalization**: The source HTML uses typographic curly
   apostrophes (e.g. "HydraFusion’s," "model’s standard rate," "we’re
   learning"). Consistent with existing notes in this corpus (verified
   against `docs-github-copilot-weekly-releases-aug31-2026.md`, which
   contains zero curly apostrophes despite its source using them), all
   quotes in this note are normalized to straight ASCII apostrophes. This
   is a typographic substitution only — no wording, word order, or
   punctuation was altered.
