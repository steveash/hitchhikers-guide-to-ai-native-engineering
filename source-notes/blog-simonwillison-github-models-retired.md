---
source_url: https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/
source_type: blog-post
title: "GitHub Models is now retired"
author: Simon Willison
date_published: 2026-08-09
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: emerging
issue: "#2773"
---

# GitHub Models is now retired

> Simon Willison's short link-blog note on GitHub Models' full retirement
> (completed July 30, 2026, after a June 16 "no new customers" step and a
> July 1 wind-down announcement), speculating that "coding agent patterns"
> made free/subsidized inference too expensive to sustain — the first
> corpus source documenting a full unified-API platform shutdown rather
> than a single-model deprecation, with Willison's own concrete
> migration (GitHub Models → OpenAI API key with a monthly spending limit)
> as the recovery pattern.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "Link Blog" format — a short
  personal note built around a linked external announcement, not a
  long-form essay. Posted August 9, 2026, 10:48pm. Tagged: github, ai,
  github-actions, generative-ai, llms, llm-pricing. The primary text is
  ~180 words; verified via direct raw-HTML fetch of the page, not a
  WebFetch AI summary.)
- **Author credibility**: Simon Willison is a working practitioner (creator
  of Datasette, the `llm` CLI, and a prolific first-hand chronicler of LLM
  tooling and pricing changes) writing about his own GitHub Actions
  workflow breaking in production. He is a primary witness to the
  retirement's practical effect (a failed CI run), not a GitHub
  spokesperson — his claim about *why* GitHub retired the service is
  explicitly labeled as his own speculation, not an official explanation.
- **Scope**: Covers what GitHub Models was, how Willison discovered the
  retirement (a broken GitHub Actions run), his speculation about the
  cause, and his personal migration to the OpenAI API. Does NOT cover:
  GitHub's official rationale (GitHub did not publish one), usage/cost
  data behind the decision, or the experience of other GitHub Models
  users beyond Willison himself. To fill in the official timeline, this
  note also directly fetched and extracted GitHub's own changelog
  entries that Willison's post links to (see Claims 6-9 and Extraction
  Notes).

## Extracted Claims

### Claim 1: GitHub Models has been fully retired, and Willison discovered this only when a GitHub Actions workflow in his own repository started failing
- **Evidence**: Opening two sentences of the post, describing a failed CI run in `simonw/research`.
- **Confidence**: settled (first-hand account of the author's own workflow breaking)
- **Quote**: "GitHub Models is now retired. I missed this news until today, when the GitHub Actions run for my simonw/research repository failed with this error message:"
- **Our assessment**: This is a concrete, first-hand illustration of what "platform retirement" looks like from the consumer side — not a graceful deprecation notice landing in an inbox, but a production workflow silently failing until someone investigates. It underscores that even a well-known, plugged-in practitioner like Willison missed the announcement until it broke something he depended on.

### Claim 2: The GitHub Actions failure surfaced as a "scheduled retirement brownout" error message before the retirement was fully complete
- **Evidence**: Blockquoted error text reproduced directly from Willison's failed CI run.
- **Confidence**: settled (direct quote of an observed system error message)
- **Quote**: "GitHub Models is temporarily unavailable as part of a scheduled retirement brownout."
- **Our assessment**: This is a concrete artifact of GitHub's own deprecation mechanics — scheduled "brownouts" (temporary, intermittent outages) ahead of a hard cutoff, rather than a single instant on/off switch. Cross-referencing GitHub's own July 1 changelog (Claim 7 below) confirms this was a deliberate two-brownout warning schedule, not an ad hoc error.

### Claim 3: GitHub Models was a unified API and playground spanning multiple LLM providers, whose main practical advantage was that GitHub Actions workflows could call it using the GitHub token already present in that environment, with no separate API key needed
- **Evidence**: Willison's own description of the service, drawn from his experience using it in his `simonw/research` workflow.
- **Confidence**: settled (author's direct description of a service he used)
- **Quote**: "GitHub Models was an odd-shaped duck. GitHub provided a model playground tool and a unified API across a bunch of different LLM providers, with the biggest benefit being that code running in GitHub Actions could use the GitHub API key already present in that environment to execute prompts."
- **Our assessment**: This "ambient credential" pattern — using a token that's already present in the CI environment rather than provisioning and storing a separate LLM API key as a repo secret — is the specific ergonomic advantage that's now gone. Anyone who built CI-integrated LLM steps on this assumption (zero-secrets-management inference) now has to add real secret management (an API key + spending limit, per Claim 5) to their workflows.

### Claim 4: Willison speculates, without confirmation from GitHub, that the retirement fits a pattern where coding-agent usage patterns made offering free or subsidized inference tokens prohibitively expensive
- **Evidence**: Willison's own stated reasoning, explicitly framed as a bet/guess rather than a confirmed cause.
- **Confidence**: anecdotal (explicitly labeled by the author as speculation — "my bet is" — not a sourced or confirmed explanation; GitHub did not publish a reason)
- **Quote**: "GitHub didn't share the reason behind the shutdown, but my bet is that it fits the pattern where coding agent patterns made it prohibitively expensive to offer free or subsidized tokens."
- **Our assessment**: This is the single most guide-relevant claim in the post, and it is the weakest-evidenced one — pure speculation from a well-informed but non-authoritative observer, with GitHub itself declining to state a reason (confirmed by reading GitHub's own changelog entries directly: none of the three official posts state a cause). We should present this as a plausible practitioner hypothesis, not an established fact. It is consistent with the broader corpus pattern of agentic/coding-agent usage driving unexpectedly high inference costs (see Cross-References), but this specific source provides no usage or cost data to substantiate it for GitHub Models specifically.

### Claim 5: Willison's own recovery was to replace GitHub Models with a direct OpenAI API key carrying a monthly spending limit, and to switch his README folder-summary generation to GPT-5.6 Luna
- **Evidence**: Closing paragraph describing his own migration, with a link to the actual code in his `simonw/research` repository.
- **Confidence**: settled (first-hand account of the author's own remediation, with a link to the actual workflow code)
- **Quote**: "My workflow uses an LLM call to create folder summaries for the README, using this code here. I swapped GitHub Models out for an OpenAI API key with a monthly spending limit, and I'm now generating my summaries using GPT-5.6 Luna."
- **Our assessment**: This is the concrete, actionable pattern the post offers: when a free/subsidized unified-API platform disappears, the fallback is a direct provider API key with an explicit spending cap set by the practitioner, not an open-ended pay-as-you-go key. Setting a spending limit as a first-class part of the migration (not an afterthought) mirrors the cost-governance pattern already documented for Uber's org-wide caps (`blog-simonwillison-uber-caps-usage.md`) and Willison's own `datasette-llm-limits` plugin (`blog-simonwillison-datasette-llm-limits.md`) — capping spend by policy is his consistent personal and professional practice, now applied at the individual-API-key level too.

### Claim 6: GitHub Models' retirement was staged over roughly six weeks in three announced steps: closed to new customers (June 16, 2026), full-retirement timeline announced with two brownout dates (July 1, 2026), and completed retirement (July 30, 2026)
- **Evidence**: Directly fetched and read GitHub's own changelog entries, linked from Willison's post: "GitHub Models is no longer available to new customers" (June 16, 2026), "GitHub Models is being fully retired on July 30, 2026" (July 1, 2026), and "GitHub Models is now retired" (July 30, 2026).
- **Confidence**: settled (three dated, first-party GitHub changelog posts, each fetched directly via raw HTML)
- **Quote**: "We are retiring GitHub Models. As a first step, new customers can no longer use it." (June 16 post); "GitHub Models will be fully retired on July 30, 2026. After this date, the playground, model catalog, inference API, and BYOK endpoints will no longer be available, and the related UI will be removed. This affects all customers." (July 1 post); "As of July 30, 2026, GitHub Models is now retired. The playground, model catalog, inference API, and bring your own key (BYOK) are no longer available to any customer, including existing customers with active usage." (July 30 post)
- **Our assessment**: This staged-retirement structure — cut off new signups first, then announce a hard date with scheduled brownouts as a warning mechanism, then execute — is a materially different shutdown pattern from the single-notice, single-cutoff model deprecations already well-documented in the corpus (e.g. `docs-github-copilot-aug2026-model-deprecations.md`). It gave existing customers roughly six weeks from the "fully retiring" announcement to the actual cutoff, plus about seven weeks from the initial new-customer freeze. None of the three official posts state a reason for the shutdown, which corroborates Willison's own observation (Claim 4) that GitHub did not share its rationale.

### Claim 7: GitHub's official retirement announcements explicitly named two brownout dates (July 16 and July 23, 2026) as advance warnings before the final cutoff
- **Evidence**: "What's changing" section of the July 1, 2026 changelog post.
- **Confidence**: settled (stated directly in the official changelog)
- **Quote**: "Brief brownouts ahead of retirement. To help you prepare, we will run short, scheduled service interruptions (brownouts) on July 16 and July 23, 2026. During a brownout, GitHub Models requests will temporarily return errors before service is restored."
- **Our assessment**: This directly explains the error Willison saw (Claim 2) — though his own encounter came after full retirement, when the brownout message text was technically stale ("That message is already stale, because the retirement has been completed," per his post). It's a reusable pattern worth noting for the guide: a platform that wants to warn dependents of an impending shutdown can inject deliberate, scheduled, intermittent failures beforehand as a forcing function — a technique distinct from just publishing a deprecation date and hoping people read it.

### Claim 8: GitHub's official guidance for displaced GitHub Models users points them to Microsoft Foundry (for general model catalog access) or GitHub Copilot (for AI-powered workflows built directly on GitHub)
- **Evidence**: "What you can do" section, present in near-identical form across all three official changelog posts (using "Azure AI Foundry" in the June 16 post and "Microsoft Foundry" in the July 1 and July 30 posts).
- **Confidence**: settled (stated directly in the official changelog, consistent across three posts)
- **Quote**: "For new and existing projects that need AI model access, Microsoft Foundry offers a broad model catalog. To build AI-powered workflows directly on GitHub, GitHub Copilot gives you access to a range of models." (July 30 post)
- **Our assessment**: GitHub is explicitly not offering a free-tier successor to GitHub Models — both named alternatives (Microsoft Foundry, GitHub Copilot) are paid products, not another unified free API. This corroborates the "free tier withdrawn, no free replacement" framing rather than a mere migration to a differently-branded free service. Note the internal rename between posts: "Azure AI Foundry" (June 16) became "Microsoft Foundry" (July 1 and July 30) — a naming change within GitHub's own six-week announcement sequence that this note flags but does not further investigate.

### Claim 9: GitHub's official retirement notices give no usage, cost, or adoption data — the rationale for the shutdown is never stated in any of the three changelog posts
- **Evidence**: Full-text reading of all three GitHub changelog posts (June 16, July 1, July 30, 2026); none contains a "why" section, cost figure, or usage statistic.
- **Confidence**: settled (absence-of-content observation from direct reading of all three primary source documents)
- **Quote**: (no direct quote — this is an absence, not a stated claim; confirmed by reading all three posts' full text)
- **Our assessment**: This absence is itself informative for the guide: official platform-retirement announcements in this corpus tend to state *what* is changing and *what to do next* in comprehensive detail, but not *why* — cost and usage rationale for shutting down free/subsidized infrastructure is not something vendors publish. Practitioners are left to speculate (as Willison does in Claim 4), and the guide should not treat vendor silence on cost rationale as evidence that cost wasn't the driver — it's simply not disclosed either way.

## Concrete Artifacts

### GitHub Actions failure message (from Willison's `simonw/research` workflow, as quoted in his post)
```
GitHub Models is temporarily unavailable as part of a scheduled retirement brownout.
```

### Willison's migration (described in his post, code linked but not reproduced here)
```
Before: GitHub Models unified API, authenticated via ambient GitHub Actions token
After:  OpenAI API key (with a monthly spending limit), model = GPT-5.6 Luna
Use case: generating folder summaries for a repository README from within a
          GitHub Actions workflow
```
*Source: simonwillison.net, "GitHub Models is now retired," August 9, 2026.
The actual workflow code Willison links to (in `simonw/research`) was not
separately fetched or reproduced here — only his prose description of the
change.*

### GitHub Models retirement timeline (assembled from three official GitHub changelog posts, all fetched directly via raw HTML)
```
2026-06-16  "GitHub Models is no longer available to new customers"
            - New orgs/enterprises without prior usage lose access (free and paid plans).
            - Existing customers with active usage: unaffected "today."

2026-07-01  "GitHub Models is being fully retired on July 30, 2026"
            - Full retirement date announced: July 30, 2026.
            - Applies to ALL customers this time, including existing active usage.
            - Two scheduled brownout dates announced: July 16 and July 23, 2026.
            - Playground, model catalog, inference API, and BYOK endpoints all named
              as going away; related UI to be removed.

2026-07-30  "GitHub Models is now retired"
            - Retirement completed as of this date.
            - Playground, model catalog, inference API, and BYOK confirmed unavailable
              to any customer, including existing customers with active usage.
            - "This completes the retirement we announced on July 1."

All three posts: same "What you can do" guidance — Microsoft/Azure AI Foundry
for general model access, GitHub Copilot for AI workflows built on GitHub —
and no stated reason for the retirement.
```
*Source: github.blog/changelog, three posts dated 2026-06-16, 2026-07-01, and
2026-07-30, all fetched directly via curl against the raw page HTML (not
WebFetch summarization).*

## Cross-References

- **Extends** `docs-github-copilot-aug2026-model-deprecations.md` and the
  broader Copilot model-deprecation family in the corpus (GPT-5.2, GPT-4.1,
  Claude Sonnet 4, Gemini 2.5 Pro/Gemini 3 Flash notices): those notices all
  document a single model being swapped for a named successor within a
  platform that continues to exist. This source documents a materially
  different, more severe failure mode — an entire unified-API *platform*
  being withdrawn with no in-kind free replacement, only paid alternatives
  (Claim 8). The guide's existing "avoid hardcoded model identifiers"
  recommendation (built from the Copilot deprecation family) should be
  extended to "avoid hard-dependency on a single free/subsidized inference
  platform for CI or production workflows" — a broader architectural
  concern than model-name hardcoding alone.
- **Corroborates** `blog-simonwillison-uber-caps-usage.md` (Uber's
  $1,500/month per-tool per-employee cap introduced to manage an AI budget
  overrun) and `blog-simonwillison-datasette-llm-limits.md` (Willison's own
  plugin for per-user/global USD spending limits): all three sources
  converge on explicit, policy-level spending caps — whether org-wide,
  per-user, or per-API-key — as the practitioner and enterprise response to
  agentic-workload cost unpredictability. Claim 5's "OpenAI API key with a
  monthly spending limit" is the same governance instinct applied at the
  smallest possible scale (a single personal CI workflow).
- **Corroborates** (directionally, not on specifics) the general
  cost-pressure theme already present in `blog-ghaw-ai-credits-migration.md`
  (GitHub's own Agentic Workflows team replacing a billing-independent cost
  metric, Effective Tokens, with a directly dollar-denominated one, AI
  Credits) — both sources show GitHub-adjacent infrastructure moving toward
  tighter, more direct cost accounting for agentic/LLM workloads within
  roughly the same mid-2026 window, though `blog-ghaw-ai-credits-migration.md`
  is about a metric change within a still-operating product (gh-aw) and this
  source is about a platform's outright discontinuation — they are related
  by theme, not by shared claim.
- **Contradicts**: None identified. No existing source note makes a claim
  about GitHub Models specifically that this source disagrees with.
- **Novel**:
  - First corpus source documenting GitHub Models' existence and full
    retirement at all — no prior note mentions GitHub Models.
  - First corpus example of a full unified-API *platform* shutdown (not a
    single-model deprecation) with a staged, multi-announcement retirement
    process (new-customer freeze → dated full-retirement notice with
    scheduled brownouts → completion).
  - The "ambient CI credential" ergonomic pattern (Claim 3) — using a token
    already present in the CI environment instead of a separately
    provisioned API key — is a novel architectural detail not covered
    elsewhere in the corpus's CI/CD or secrets-management notes reviewed
    during this extraction.
  - The "scheduled brownout" as a deliberate pre-shutdown warning mechanism
    (Claim 7) is a novel deprecation-communication technique not seen in the
    corpus's existing (single-notice, no-brownout) Copilot model-deprecation
    family.

## Guide Impact

- **Chapter 02 (Foundations — Economics/Constraints)**: Add GitHub Models as
  a concrete case study of a free/subsidized unified-LLM-API platform being
  discontinued outright, not just individual models rotating. Present
  Willison's cost-driven-by-agent-usage hypothesis (Claim 4) explicitly as
  speculation, not confirmed cause — pair it with the observation (Claim 9)
  that the vendor never states a rationale for these shutdowns, so
  practitioners should plan for silent cost-driven withdrawal as a real risk
  category even when it can't be confirmed in advance.
- **Chapter 03 (Deployment patterns & platform dependencies)**: Use the
  "ambient CI credential" pattern (Claim 3) as a specific example of a
  convenience dependency worth flagging: workflows that lean on a
  platform-provided token for LLM calls (rather than a portable, independently
  managed API key) save setup effort but create a harder migration when that
  platform's LLM offering disappears — the practitioner has to add secrets
  management at the same moment they're scrambling to replace the underlying
  capability. Recommend provisioning a spending-limited API key up front even
  when a free ambient-credential option is available, precisely so migration
  is a config change rather than an emergency.
- **Chapter 04 (Tool selection / vendor risk)**: Add the staged-retirement
  pattern (Claim 6) — new-customer freeze, then a dated full-retirement
  notice with scheduled brownouts, then completion — as a template for what
  a full platform deprecation (as opposed to a model swap) looks like in
  practice, distinct from the Copilot model-deprecation notices already
  documented. Recommend treating "free or heavily subsidized unified LLM API
  tied to a single platform vendor" as a higher-risk dependency category than
  "named model available from a specific provider," since the former can
  disappear as a whole product line with no free successor.

## Extraction Notes

1. **WebFetch summarized rather than quoted verbatim on first pass**: The
   initial WebFetch call against the source URL returned an AI-generated
   summary, not exact source text, and was not used for any quote in this
   note. All quotes above were taken from a direct `curl` fetch of the raw
   page HTML (`simonwillison.net/2026/Aug/9/github-models-is-now-retired/`),
   located inside the `<div class="entry entryPage">` block, and are
   character-for-character verbatim as of the 2026-08-19 fetch.
2. **Followed the primary linked source, plus one level further**: Per
   MINER.md's "follow up to 5 linked pages that seem substantive" guidance,
   this note directly fetched and read all three GitHub changelog posts in
   the retirement sequence: the post Willison links to directly (July 30,
   "GitHub Models is now retired"), the post it in turn links to (July 1,
   "GitHub Models is being fully retired on July 30, 2026"), and the post
   that one links to (June 16, "GitHub Models is no longer available to new
   customers"). All three were fetched via raw HTML `curl`, not WebFetch
   summarization, and are quoted verbatim in Claims 6-9. The two other
   links in Willison's post (his `simonw/research` repository and its
   README/workflow code, and GitHub Next's Continuous AI page) were not
   fetched — they support Claim 3's context but are not needed for a direct
   quote, and the repository code itself is not a text source in scope for
   this note.
3. **Confidence rated "emerging" overall, not "settled"**: The factual
   retirement timeline (Claims 1, 2, 3, 5, 6, 7, 8) is settled — directly
   observed and corroborated by three official GitHub sources. But the
   claim most relevant to the guide (Claim 4, the cost-driven-by-agents
   causal hypothesis) is explicitly labeled speculation by its own author
   and is unconfirmed by GitHub. The overall confidence rating reflects
   that the source's most guide-relevant contribution is anecdotal, even
   though its factual timeline is settled.
4. **No contradiction found; none filed.** This source does not conflict
   with any existing source note's claims — it introduces a new topic
   (GitHub Models) not previously covered in the corpus.
