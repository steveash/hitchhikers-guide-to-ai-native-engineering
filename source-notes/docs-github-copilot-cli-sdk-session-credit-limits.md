---
source_url: https://github.blog/changelog/2026-07-01-set-ai-credit-session-limits-in-copilot-cli-and-sdk
source_type: docs
title: "Set AI credit session limits in Copilot CLI and SDK"
author: GitHub (official changelog)
date_published: 2026-07-01
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: settled
issue: "#1470"
---

# Set AI Credit Session Limits in Copilot CLI and SDK (GitHub Changelog, July 1, 2026)

> GitHub's July 1, 2026 changelog introduces a session-scoped AI credit spend cap for
> Copilot CLI and the Copilot SDK — a soft limit, set via `/limits` (interactive) or
> `--max-ai-credits` (noninteractive), that stops an agent cleanly when a per-session
> credit ceiling is reached, adding a new cost-control layer beneath org/user budgets
> and above per-request model-cost optimization.

## Source Context

- **Type**: docs (GitHub official product changelog, ~230 words, July 1, 2026). Two
  linked documentation pages were also read in full as substantive follow-on pages per
  MINER.md §1: "Setting an AI credit session limit in GitHub Copilot CLI"
  (docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit) and
  "Optimizing your AI usage to maximize efficiency and reduce cost"
  (docs.github.com/copilot/tutorials/optimize-ai-usage).
- **Author credibility**: GitHub engineering team announcing a production feature
  addition to Copilot CLI 1.0.66+ and Copilot SDK 1.0.5+. Authoritative for the
  feature's existence, its interactive/noninteractive interfaces, its soft-cap
  behavior, and its public-preview availability. Not a credible source for how
  effectively session limits reduce total organizational spend, whether teams have
  adopted the feature, or how it interacts with enterprise-level budget alerting
  systems beyond the one-line "complements" statement.
- **Scope**: Session-level AI credit spend limits for Copilot CLI and Copilot SDK:
  what they cap, how they are set interactively and noninteractively, their soft-cap
  behavior, and availability/version requirements. Does NOT cover: the underlying
  AI-credit-to-dollar conversion mechanics beyond the "$0.01 per credit" definition
  in the linked docs page; enterprise-level policy controls over whether developers
  can raise their own limits; how `--max-ai-credits` interacts with CI/CD pipelines
  specifically; or a deprecation/GA timeline (feature is public preview, "subject to
  change").

## Extracted Claims

### Claim 1: Copilot CLI and the Copilot SDK now support AI credit session limits that cap the amount an agent can spend in a single session

- **Evidence**: Opening sentence of the changelog, confirmed verbatim via direct HTML
  fetch of the changelog page (not the AI-summarizing WebFetch tool, which returned a
  paraphrased version on a first pass — a direct `curl` of the page was used for exact
  text on the second pass).
- **Confidence**: settled (product fact — the feature exists as described)
- **Quote**: "You can now set AI credit session limits in Copilot CLI and the GitHub
  Copilot SDK to cap the amount an agent spends in a session."
- **Our assessment**: This is the first session-scoped (as opposed to per-user or
  per-organization) AI credit control documented in the corpus. Prior corpus sources
  cover per-user consumption visibility (`docs-github-copilot-usage-metrics-ai-credits-per-user.md`)
  and workflow-level cost-reduction levers for gh-aw (`docs-ghaw-cost-management.md`),
  but neither documents a hard ceiling that an individual CLI or SDK session enforces
  on itself in real time.

### Claim 2: The stated purpose of session limits is automation contexts where no one is actively monitoring the agent's work

- **Evidence**: Explicit rationale stated in the changelog's opening paragraph.
- **Confidence**: settled (stated motivation in official changelog)
- **Quote**: "This is especially useful for automation, where no one is actively
  monitoring the agent's work."
- **Our assessment**: This framing positions session limits as a guardrail for
  unattended/long-running agent sessions specifically — the same class of workload
  gh-aw's cost-management reference addresses with `skip-if-match`, cheaper models,
  and rate limiting (`docs-ghaw-cost-management.md` Claims 5–8). Session limits are a
  runtime backstop that applies regardless of which of those upstream levers is used,
  rather than a substitute for them.

### Claim 3: Session tracking covers the entire session, including model calls, subagents, and background work like compaction

- **Evidence**: Explicit scope statement in the changelog.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Copilot tracks AI credit usage across the entire session, including model
  calls, subagents, and background work like compaction."
- **Our assessment**: The explicit inclusion of subagents and compaction is significant
  for multi-agent harnesses: a session limit set on a top-level Copilot CLI session
  will account for credit spend by any subagents it spawns, not just the top-level
  model calls. This closes a potential loophole where a runaway subagent could exceed
  spend expectations invisibly to a session-level cap. Compaction (context summarization)
  is itself billed against the limit, meaning long sessions that repeatedly compact
  will consume part of their budget on housekeeping, not just task work.

### Claim 4: When the limit is reached, the agent stops cleanly and notifies the user rather than continuing until the task is finished or the user manually intervenes

- **Evidence**: Explicit behavior statement in the changelog.
- **Confidence**: settled (stated behavior in official changelog)
- **Quote**: "When the limit is reached, the agent wraps up and lets you know instead
  of running until the task is finished or until you manually stop it."
- **Our assessment**: This changes the default failure mode for unattended agent runs
  from "runs until done or until someone notices and kills it" to "runs until done or
  until the credit ceiling, whichever comes first, with an explicit notification." For
  Ch02 harness engineering: this is a concrete example of a resource-bounded stopping
  condition being built into the platform itself, rather than something practitioners
  must implement via external monitoring or wrapper scripts.

### Claim 5: In an interactive session, the `/limits` command views, sets, or removes the session limit; when the limit is reached, Copilot prompts the user to raise or adjust it and continues from where it stopped without restarting the task

- **Evidence**: Explicit description in both the changelog and the linked "Setting an
  AI credit session limit" docs page, with the exact command syntax given on the docs
  page.
- **Confidence**: settled (documented CLI command with exact syntax)
- **Quote**: "In an interactive session, use /limits to view, set, or remove your
  limit. When it's reached, Copilot prompts you to raise or adjust it and then
  continues from where it stopped. There's no need to restart the task."
- **Our assessment**: The "continues from where it stopped" behavior is operationally
  important: hitting the limit does not discard session state or force a fresh context
  rebuild. This distinguishes the credit limit from a hard kill switch — it is a
  checkpoint the user can choose to extend past, not an unconditional cutoff. For
  practitioners: interactive sessions can treat the limit as a deliberate "check in with
  me before you keep spending" gate rather than a risk of losing work in progress.

### Claim 6: In noninteractive runs, passing `--max-ai-credits` bounds a single run and the run ends when the limit is reached, making it usable in scripts

- **Evidence**: Explicit description in the changelog and the linked docs page, with
  exact flag syntax given on the docs page.
- **Confidence**: settled (documented CLI flag with exact syntax)
- **Quote**: "For noninteractive runs, pass --max-ai-credits to bound a single run. The
  run ends when the limit is reached, so it's easy to use in scripts."
- **Our assessment**: Unlike the interactive mode's "pause and prompt" behavior, the
  noninteractive mode's run simply ends when the limit is hit — there is no one present
  to respond to a prompt. This is the correct default for CI/CD or scheduled contexts:
  a script-driven Copilot CLI invocation with `--max-ai-credits` becomes a bounded-cost
  operation that will not silently exceed a budget ceiling even if the task is larger
  than expected.

### Claim 7: Session limits are soft caps — because usage is only known after a response returns, a response already underway finishes before the session stops, so actual usage may slightly exceed the configured number

- **Evidence**: Explicit "Important Considerations" statement in the changelog, echoed
  in the linked docs page.
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "Session limits are a soft cap. Since usage is only known after a response
  returns, a response that's already underway finishes before Copilot stops, so actual
  usage may slightly exceed the number you set."
- **Our assessment**: This is a precise, honest disclosure of the mechanism's
  limitation: a limit of N credits does not guarantee spend caps at exactly N — a
  response in flight when the threshold is crossed will complete and push actual usage
  above N. For teams treating `--max-ai-credits` as a hard budget enforcement
  mechanism (e.g., to guarantee a CI job never exceeds $X), this soft-cap behavior
  means the configured number should be treated as a target with margin, not an
  absolute ceiling — consistent with how gh-aw's cost-management reference frames
  `estimated_cost` figures as estimates rather than guarantees
  (`docs-ghaw-cost-management.md` Claim 12).

### Claim 8: A session limit governs spend for a single session only; it complements but does not replace broader user- or organization-level AI credit budgets and spending controls

- **Evidence**: Explicit statement in the changelog's "Important Considerations"
  section.
- **Confidence**: settled (explicitly documented scope boundary)
- **Quote**: "A session limit controls spend for one session—it complements, but
  doesn't replace, your overall budgets and spending limits."
- **Our assessment**: This places session limits as one tier in a multi-tier cost
  governance stack, alongside the per-user `ai_credits_used` metrics field
  (`docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 1) and whatever
  org-level monthly budget controls exist in GitHub billing. A team could set generous
  per-session limits to prevent any single unattended run from spiraling, while
  separately tracking aggregate per-user or per-org consumption against a monthly
  budget — the two mechanisms operate at different time horizons and do not need to
  agree numerically.

### Claim 9: Session limits are available in public preview for Copilot Individuals, Business, and Enterprise, are subject to change, and require Copilot CLI 1.0.66+ and Copilot SDK 1.0.5+

- **Evidence**: Explicit "Availability" statement in the changelog.
- **Confidence**: settled (explicit version and plan-tier statement in official
  changelog)
- **Quote**: "Session limits are available in public preview for Copilot for
  Individuals, Business, and Enterprise, and are subject to change. They're supported
  in Copilot CLI 1.0.66 and later, and in Copilot SDK 1.0.5 and later."
- **Our assessment**: Broad plan-tier availability (including Individuals, not gated
  to Business/Enterprise) mirrors the CLI auto model selection feature's "across all
  Copilot plans" availability (`docs-github-copilot-cli-auto-model-selection.md`
  Claim 1) rather than the Business/Enterprise-only gating seen on some web-agent
  features. "Public preview" and "subject to change" mean the `/limits` syntax and
  `--max-ai-credits` flag behavior documented here should be treated as current-as-of-
  July-2026, not guaranteed stable.

### Claim 10: An AI credit is a $0.01 USD unit used to track the cost of AI model interactions, and usage per credit depends on the model and number of tokens consumed

- **Evidence**: Explicit definition on the linked "Setting an AI credit session limit"
  docs page.
- **Confidence**: settled (explicit unit definition on official docs page)
- **Quote**: "AI credits are the unit Copilot uses to track the cost of AI model
  interactions: each credit equals $0.01 USD, and usage depends on the model and the
  number of tokens consumed."
- **Our assessment**: The $0.01-per-credit conversion rate matches the AI Credits
  (AIC) unit documented for GitHub Agentic Workflows in `blog-ghaw-ai-credits-migration.md`
  Claim 7 ("AI Credits (AIC): primary spend metric (1 AIC = $0.01 USD)"). This
  confirms "AI credit" is a single GitHub-wide billing unit shared across gh-aw,
  Copilot CLI, Copilot SDK, and the usage-metrics API's `ai_credits_used` field
  (`docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 1) — not a
  product-specific metric reinvented per surface.

### Claim 11: GitHub's own guidance recommends setting session limits above 30 AI credits, because most model calls cost more than 20 AI credits

- **Evidence**: Explicit "Tip" callout on the linked "Setting an AI credit session
  limit" docs page.
- **Confidence**: settled (explicit numeric guidance on official docs page)
- **Quote**: "AI credit session limits work best when set to > 30 AI credits as most
  model calls will cost more than 20 AI credits."
- **Our assessment**: This is the first concrete per-model-call cost magnitude
  disclosed for Copilot CLI/SDK sessions in the corpus: a single model call
  frequently costs more than 20 credits (more than $0.20). This is a useful anchor for
  practitioners setting limits — a limit at or below 20 credits risks tripping after a
  single model call, defeating the purpose of allowing the agent to do meaningful work
  before stopping. The guidance to stay above 30 credits implies a working margin of at
  least one full model call beyond the typical single-call cost.

### Claim 12: The interactive session limit depletes as each message is processed for the life of the session, independent of message count, while the noninteractive limit applies for the duration of Copilot's work on a task and remains active until Copilot finishes responding

- **Evidence**: Explicit distinction on the linked "Setting an AI credit session
  limit" docs page, under "Setting a limit within an interactive session" and "Setting
  a limit in non-interactive mode" subsections.
- **Confidence**: settled (explicit behavioral distinction on official docs page)
- **Quote**: "In an interactive CLI session, the limit applies for the entire session
  and depletes as each message is processed, independent of how many messages you
  send." / "When you run Copilot CLI programmatically from the command line, the limit
  applies for the duration of Copilot's work on the task and remains active until
  Copilot finishes responding."
- **Our assessment**: The two modes have different "unit of accounting": interactive
  mode accumulates spend across an open-ended number of user messages within one
  session, while noninteractive mode accumulates spend across the bounded lifetime of
  a single invoked task. A practitioner scripting many short noninteractive
  `copilot -p ... --max-ai-credits N` invocations is setting a per-invocation ceiling
  each time, whereas a practitioner setting `/limits set max-ai-credits N` once in an
  interactive session is setting a ceiling for that entire multi-turn conversation
  until it is reset or the session ends.

### Claim 13: Session limits are presented by GitHub as one of eight distinct strategies (specifically strategy 5) for optimizing AI usage and reducing cost, alongside model selection, prompt clarity, context management, caching, phased research/plan/implement workflows, `/chronicle`-driven learning, and deterministic guardrails

- **Evidence**: The "Optimize AI usage" tutorial page lists "5. Set AI credit session
  limits" as one of eight numbered strategies, with session limits framed around two
  specific use cases.
- **Confidence**: settled (explicit structural placement and stated use cases in
  official docs page)
- **Quote**: "AI credit session limits are most useful when: You want to cap AI
  credits usage on a single session to avoid unexpected costs. You're tuning agent
  efficiency and want to find the minimum AI credits that still produces a good
  result."
- **Our assessment**: The second use case — using session limits as an experimentation
  tool to find the minimum credit budget that still produces a good result — is a
  distinct framing from the "safety net for unattended automation" framing in Claim 2.
  It positions `--max-ai-credits`/`/limits` not just as a guardrail but as a deliberate
  tuning instrument: a practitioner can iteratively lower the limit on a repeated task
  to find the smallest budget that still succeeds, then adopt that number as a standing
  ceiling. This is a novel cost-optimization technique not described in the
  gh-aw cost-management reference's five strategies (`docs-ghaw-cost-management.md`
  Claims 5–8), which are all workflow-configuration levers rather than an
  interactive tuning loop.

## Concrete Artifacts

### Changelog full text (verbatim, via direct fetch of the live page)

```
Set AI credit session limits in Copilot CLI and SDK
Release: July 1, 2026 | 1 minute read

You can now set AI credit session limits in Copilot CLI and the GitHub Copilot
SDK to cap the amount an agent spends in a session. This is especially useful
for automation, where no one is actively monitoring the agent's work.

Set a limit before you start work or kick off jobs, and Copilot tracks AI
credit usage across the entire session, including model calls, subagents, and
background work like compaction. When the limit is reached, the agent wraps up
and lets you know instead of running until the task is finished or until you
manually stop it.

In an interactive session, use /limits to view, set, or remove your limit.
When it's reached, Copilot prompts you to raise or adjust it and then
continues from where it stopped. There's no need to restart the task.

For noninteractive runs, pass --max-ai-credits to bound a single run. The run
ends when the limit is reached, so it's easy to use in scripts.

Session limits are a soft cap. Since usage is only known after a response
returns, a response that's already underway finishes before Copilot stops, so
actual usage may slightly exceed the number you set. A session limit controls
spend for one session—it complements, but doesn't replace, your overall
budgets and spending limits.

Session limits are available in public preview for Copilot for Individuals,
Business, and Enterprise, and are subject to change. They're supported in
Copilot CLI 1.0.66 and later, and in Copilot SDK 1.0.5 and later.

To get started, update GitHub Copilot CLI by running copilot update in your
terminal. To learn more, see Setting a session limit in Copilot CLI and
Optimize AI usage.

Share feedback with the /feedback command in a CLI session or open an issue
in our public repository.
```

*Source: https://github.blog/changelog/2026-07-01-set-ai-credit-session-limits-in-copilot-cli-and-sdk*

### CLI command syntax (from linked "Setting an AI credit session limit" docs page)

```
# Interactive session — set, view, or remove a limit
/limits set max-ai-credits NUMBER
/limits unset

# Noninteractive / scripted run — bound a single run
copilot -p "YOUR PROMPT" --max-ai-credits NUMBER
```

*Source: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit*

### Sizing guidance (from the same docs page)

```
Tip: AI credit session limits work best when set to > 30 AI credits as most
model calls will cost more than 20 AI credits.

Definition: AI credits are the unit Copilot uses to track the cost of AI model
interactions: each credit equals $0.01 USD, and usage depends on the model and
the number of tokens consumed.
```

*Source: https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit*

### Position within GitHub's eight-strategy AI-usage optimization framework

```
"Optimizing your AI usage to maximize efficiency and reduce cost" — strategy list:
1. Choose the right model for the right task
2. Provide clear guidance in your prompts
3. Keep your context lean
4. Preserve the cache
5. Set AI credit session limits          <- this source's feature
6. Research, plan, then implement
7. Utilize learnings to be more efficient at every turn
8. Add deterministic guardrails
```

*Source: https://docs.github.com/copilot/tutorials/optimize-ai-usage*

## Cross-References

- **Corroborates** `blog-ghaw-ai-credits-migration.md` Claim 7 ("AI Credits (AIC):
  primary spend metric (1 AIC = $0.01 USD)"): the $0.01-per-credit definition on the
  Copilot CLI session-limit docs page matches the gh-aw AIC conversion rate exactly,
  confirming "AI credit" is one GitHub-wide billing unit rather than a per-product
  metric reinvented for the CLI.

- **Corroborates** `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 1
  (the `ai_credits_used` per-user metrics field) and Claim 5 (metrics-signal vs.
  billed-total distinction): both sources use "AI credits" as the unit of account for
  Copilot spend. Together they show the same underlying credit ledger being surfaced
  in two different ways — as a retrospective per-user/per-org metric (June 19 source)
  and as a prospective, session-enforced spend ceiling (this source, July 1).

- **Extends** `docs-github-copilot-cli-auto-model-selection.md` Claim 3 (the CLI auto
  model pool is bounded to 0x–1x premium multiplier models) and Claim 6 (auto mode
  gives a 10% multiplier discount): auto model selection and session credit limits are
  complementary, non-overlapping cost controls operating at different levels — auto
  selection controls which model (and therefore the per-request multiplier) handles a
  given request, while a session limit caps cumulative spend across an entire session
  regardless of which models were used. A practitioner could combine both: use auto
  mode to keep per-request cost down, and set a session limit as a backstop against
  unexpectedly long sessions.

- **Extends** `docs-ghaw-cost-management.md` Claims 5–8 (gh-aw's five workflow-level
  cost-reduction strategies: `skip-if-match`, cheaper models, context limiting,
  per-user rate limiting) and Claim 1 (the two-component cost model of Actions minutes
  + inference cost): this source documents an analogous but distinct cost-control
  primitive for interactive/scripted Copilot CLI and SDK sessions rather than for
  gh-aw's GitHub Actions-triggered workflows. Where gh-aw's levers operate at
  workflow-configuration time (frontmatter fields evaluated before or during a run),
  the CLI/SDK session limit is a live, in-session enforcement mechanism that halts
  an already-running session when a threshold is crossed — closer in spirit to gh-aw's
  `skip-if-match` (a cost-avoidance gate) than to model selection, but applied mid-session
  rather than pre-run.

- **Extends** `docs-github-copilot-cli-settings-command.md` Claim 2 (the `/settings`
  command's three invocation modes: interactive dialog, inline key-value assignment,
  reset to defaults) and Claim 8 (keyboard shortcuts and self-service configuration
  design): `/limits` is another Copilot CLI slash command following the same
  self-service, in-session configuration pattern documented for `/settings` — both
  commands let practitioners configure session behavior without leaving the CLI or
  consulting external documentation. Neither source states whether `/limits` state is
  itself exposed through the `/settings` schema or is a fully separate subsystem.

- **Novel**:
  - **First session-scoped (as opposed to per-user, per-org, or per-workflow) AI
    credit spend cap documented in the corpus.** Prior corpus sources cover
    aggregate metrics visibility (`docs-github-copilot-usage-metrics-ai-credits-per-user.md`)
    and workflow-configuration-time cost levers for gh-aw
    (`docs-ghaw-cost-management.md`); none document a live, self-enforcing ceiling
    inside a single running CLI/SDK session.
  - **First corpus source to name a concrete per-model-call cost magnitude** ("most
    model calls will cost more than 20 AI credits," i.e., more than $0.20 per call)
    as sizing guidance for a spend control.
  - **First corpus source to document Copilot SDK (1.0.5+) as carrying its own cost
    controls**, distinct from the `gh aw` CLI/SDK covered elsewhere in the corpus and
    from the Copilot CLI itself — establishing that GitHub's agent SDK surface has
    matured to the point of shipping first-party spend-limiting primitives.
  - **First explicit statement that subagents and background compaction are billed
    against the same session-level cap as top-level model calls** — closing a
    potential blind spot where nested agent work could otherwise be invisible to a
    session-level budget.
  - **First corpus source to frame a cost control as a deliberate tuning instrument**
    (Claim 13's "find the minimum AI credits that still produces a good result"), not
    just a safety guardrail.

## Guide Impact

- **Chapter 02 (Harness Engineering — Tooling Landscape / Cost Management)**:
  Add `/limits` (interactive) and `--max-ai-credits` (noninteractive) as concrete,
  first-party stopping conditions for unattended Copilot CLI/SDK sessions. Update any
  existing guidance that frames "runaway unattended agent spend" as a problem requiring
  external wrapper scripts or monitoring — GitHub CLI 1.0.66+/SDK 1.0.5+ now provide a
  native (if soft) ceiling. Document the soft-cap caveat explicitly: a configured limit
  is a target with margin, not a hard guarantee, because an in-flight response
  completes before the session stops. Recommend the >30-credit sizing floor from
  Claim 11 so practitioners don't set limits that trip after a single model call.

- **Chapter 04 (Model Selection and Cost Management, per Prospector triage)**: Add
  session credit limits as a distinct cost-control tier alongside auto model selection
  (`docs-github-copilot-cli-auto-model-selection.md`) and per-user/per-org metrics
  visibility (`docs-github-copilot-usage-metrics-ai-credits-per-user.md`). Frame the
  three mechanisms as operating at different levels: auto selection controls
  per-request model cost; session limits cap cumulative session spend; usage metrics
  provide retrospective per-user/per-org visibility. Cite the $0.01-per-credit
  conversion (Claim 10) as the shared unit across all three, and Claim 13's
  "tuning instrument" use case as a technique for finding a minimal viable credit
  budget for a recurring task type.

- **Chapter 05 (Team Adoption — Cost Governance)**: Recommend teams running unattended
  or scheduled Copilot CLI/SDK automation set `--max-ai-credits` as a standing default
  in their scripts, the same way `docs-ghaw-cost-management.md` recommends `schedule`
  triggers and `skip-if-match` for gh-aw workflows. Note this is a public-preview
  feature ("subject to change") as of July 2026 — teams building automation on
  `--max-ai-credits` should expect the flag's behavior or availability to evolve.

## Extraction Notes

1. **WebFetch returned a paraphrased version on the first pass.** The WebFetch tool's
   AI-summarization step reworded the changelog substantially (e.g., "GitHub
   introduced the ability to cap AI credit spending..." instead of the source's actual
   opening sentence). Per MINER.md §2a, a direct `curl` fetch of the live changelog
   page and the two linked docs pages was performed and the HTML was parsed directly
   to extract character-for-character text. All quotes in this note are taken from
   the direct HTML fetch, not the WebFetch-summarized pass.
2. **Both linked "Further reading" pages were followed in full**, per MINER.md §1's
   instruction to follow substantive linked pages: "Setting an AI credit session limit
   in GitHub Copilot CLI" and "Optimizing your AI usage to maximize efficiency and
   reduce cost." A third link, "What are GitHub AI Credits" (linked from the
   session-limit docs page's "Further reading" section), was not followed — it appears
   to be a billing-concepts reference page rather than a page with additional
   session-limit-specific claims, and the $0.01/credit definition it would likely
   restate was already captured verbatim from the session-limit page itself (Claim 10).
3. **No contradictions found.** This announcement is additive to the existing cost-
   governance corpus — it introduces a new control tier rather than disputing any
   claim in `docs-github-copilot-usage-metrics-ai-credits-per-user.md`,
   `docs-github-copilot-cli-auto-model-selection.md`, or `docs-ghaw-cost-management.md`.
   No contradiction issue was filed.
4. **The three duplicate Prospector triage comments on the source issue** (all posted
   within the same minute, apparently from repeated triage runs) were treated as one
   triage assessment; their guidance was consistent (Ch02/Ch04/Ch05 relevance, overlap
   with the auto-model-selection and per-user AI-credits notes) and did not require
   reconciliation.
