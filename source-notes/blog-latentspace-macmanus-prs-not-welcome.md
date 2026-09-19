---
source_url: https://www.latent.space/p/pr-not-welcome
source_type: blog-post
title: "PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of Contributors"
author: Richard MacManus (Latent Space)
date_published: 2026-09-01
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: emerging
issue: "#3564"
---

# PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of Contributors

> Reports, with named on-record quotes from the creators/maintainers of four
> high-traffic AI-native open source projects (Vercel AI SDK, Astro, Flue,
> tldraw), a specific organizational pattern: replacing external
> community pull requests with an internal "software factory" of specialized
> agents that triage, reproduce, fix, and review issues — with concrete
> adoption metrics from Vercel (25-35% of merged PRs, 70-80% of closed
> issues within four weeks) and an open, unresolved debate among the
> maintainers themselves about what happens to community-building and
> future-maintainer pipelines once code contribution is closed off.

## Source Context

- **Type**: blog-post (Latent Space, published September 1, 2026, byline
  Richard MacManus). Reporting/synthesis piece built from a Vercel company
  blog post plus a Vercel engineer's YouTube explainer, a direct interview
  with Astro/Flue creator Fred Schott, a public policy post + a public reply
  tweet from tldraw creator Steve Ruiz, and a public reply from Mitchell
  Hashimoto (HashiCorp co-founder, Ghostty creator, now co-founder of
  Superlogical). Not paywalled; full article (~900 words) retrieved directly.
- **Author credibility**: Richard MacManus is a working technology journalist
  (also the byline behind `blog-latentspace-aiewf-loops-software-factories-dispatch.md`
  in this corpus, an AIEWF conference dispatch). This piece is synthesis
  reporting drawing on primary sources (a company blog post, a video, a
  direct interview, and public social posts) rather than first-hand
  on-site observation of the systems described — MacManus did not
  independently verify Vercel's claimed metrics or observe the software
  factory operating.
- **Scope**: Covers four named projects' policies on external PRs (Vercel AI
  SDK, Astro, Flue, tldraw) and the specific mechanics and metrics of
  Vercel's "software factory," Astro's auto-triage system, and Flue's/
  tldraw's outright PR-closing policies. Also covers a short community-impact
  debate (Schott's stated risk concern, Hashimoto's prediction, Ruiz's
  reframing of what community contribution is "for" going forward). Does
  NOT cover: any technical detail of how Vercel's agents are prompted or
  evaluated beyond one architecture diagram description; any quantified
  data from Astro, Flue, or tldraw comparable to Vercel's percentages;
  or any project that has tried this and reverted/failed.

## Extracted Claims

### Claim 1: Several top AI-native open source projects (named: Flue, tldraw) now refuse to accept pull requests from external contributors at all, converting them instead to issues or discussions, and prefer to use their own agents to create and manage PRs
- **Evidence**: Author's framing claim, opening the article, backed by the
  specific project policies documented in Claims 6 and 9-10 below.
- **Confidence**: emerging (a named, verifiable policy at two specific
  projects, not a survey of the broader ecosystem)
- **Quote**: "These projects, which include Flue and tldraw, refuse to accept PRs from external contributors — in part because they're usually AI-generated. Instead, the maintainers prefer to use their own agents to create and manage PRs."
- **Our assessment**: This is a specific, checkable claim (project contribution policies are public) rather than an industry-wide generalization, and the article backs it with two concrete, named examples plus direct quotes from both projects' creators (Claims 6, 9-10). The stated reason — that external PRs are "usually AI-generated" and therefore lower-trust — is a distinct rationale from Vercel's stated reason (Claim 3: trust in a specific, tuned agent configuration over an unknown community agent), worth preserving as two related but separate justifications for the same policy shift.

### Claim 2: The "software factory" pattern for managing community contributions typically involves a team of agents triaging a PR or issue, reproducing the bug (if applicable), implementing a fix or feature, reviewing it, and then handing the result back to a human for the final merge decision
- **Evidence**: Author's synthesized definition, presented as the general
  pattern the four case studies below instantiate.
- **Confidence**: emerging (a synthesized pattern description drawn from the
  article's own four case studies, not a single named source's definition)
- **Quote**: "Typically this involves a 'team' of agents triaging a PR, reproducing the issue (if it's a bug), implementing a fix or a new feature, reviewing it, and then handing it back to a human to merge it."
- **Our assessment**: This keeps a human in the loop at the merge decision specifically, even in projects that have otherwise automated triage, reproduction, fix, and review — consistent with the "review gate as the one non-scaling box" framing already established in `blog-addyosmani-software-factories-light-dark.md` Claim 1. None of the four case studies in this article describe fully unattended ("dark factory," in that note's terminology) merging.

### Claim 3: Vercel deployed multiple specialized agents (one to reproduce a bug, another to apply a fix, another to review the fix) for its AI SDK project because it trusts a specific, tuned agent configuration with a proven track record on a category of bugs more than it trusts agents run by unknown community members
- **Evidence**: Direct quote from Vercel engineer Lars Grammel, explaining
  the reasoning in a YouTube video the article cites.
- **Confidence**: emerging (a named engineer's stated rationale for a shipped
  internal system, not independently audited)
- **Quote**: "If we have a very specific agent with a very specific prompt that we optimized — and we know that, over history, it was very successful in fixing a certain category of bugs — then we develop trust in that particular agent configuration," Vercel engineer Lars Grammel explained in a YouTube video.
- **Our assessment**: This is a specific trust mechanism — accumulated track record of a fixed, tuned agent configuration against a known bug category — distinct from a generic "AI review catches more bugs" claim. It gives a concrete reason projects would prefer their own narrow, tested agents over accepting arbitrary community-submitted AI-generated code: the trust is in the specific configuration's history, not in "AI" as a category. Grammel's companion line, cited in the same video per the article — "not necessarily trusting the community, because it can actually cut down your time to review" — makes explicit that the community's own agent use (not just human contributions) is the thing being distrusted.

### Claim 4: Vercel's AI SDK project, which receives over 20 million npm downloads per week, had accumulated over 1,000 open issues and almost 800 open pull requests by late June 2026 before deploying its software factory
- **Evidence**: Figures the article attributes to Vercel's own company blog
  post, "Building a software factory for AI SDK."
- **Confidence**: emerging (first-party vendor-reported backlog figures,
  relayed by an independent reporter, not independently re-counted)
- **Quote**: "deployed agents to get control over its PR and issue backlog — which had reached 'over 1,000 open issues and almost 800 pull requests' by late June."
- **Our assessment**: This is the concrete before-state that Claim 5's metrics are measured against — useful for the guide as evidence of the scale of backlog (not a small side project) at which a maintainer team judged agent-driven triage/fix automation worth building, for a project with genuinely high external usage (20M weekly downloads).

### Claim 5: Within four weeks of deploying its software factory, Vercel's AI SDK project reports the factory authors between 25% and 35% of the PRs the team merges, and closes 70-80% of issues
- **Evidence**: Figures the article attributes directly to Vercel's own
  claim (blog post and/or Grammel's video).
- **Confidence**: emerging (a single vendor's self-reported metric over a
  short (four-week) measurement window, not independently audited or
  compared against a longer-term baseline)
- **Quote**: "Just four weeks after this software factory was implemented, Vercel claims the factory now 'authors between 25 and 35% of PRs we merge and closes 70-80% of issues.'"
- **Our assessment**: This is the most concrete, quotable adoption metric in the article, and a meaningful data point for a guide section on agentic OSS maintenance — but it should be flagged clearly as (a) self-reported by the vendor, (b) measured only four weeks in, with no reported one-quarter or one-year follow-up, and (c) not broken out by bug severity/complexity, so it does not indicate what fraction of *hard* issues the factory resolves versus low-hanging-fruit triage and closure.

### Claim 6: Astro (62,000 GitHub stars) adopted an agent-driven auto-triage system after creator Fred Schott's team spent roughly five years with issues arriving faster than the team could handle them; Schott says the situation has "totally shifted in the last six months" because agents now handle triage, reproduction, and get the user to verify a suggested fix before a maintainer even looks at it
- **Evidence**: Direct quotes from Fred Schott, given to Latent Space
  (MacManus) directly, describing the before/after state.
- **Confidence**: emerging (a single named maintainer's first-person account
  of his own project's operational history, no metrics given comparable to
  Vercel's Claim 5)
- **Quote**: "For five years, we were in this place where issues came in faster than we could handle them," Schott told Latent Space. "It's totally shifted in the last six months," he said. "We can now solve these issues with these automations — handling triage, reproduction, getting the user to actually verify the fix that the bot is suggesting before we even look at it."
- **Our assessment**: The specific ordering — automated triage, automated reproduction, and automated user-verification of a proposed fix, all occurring *before* a human maintainer looks at the issue — is a concrete workflow sequence worth extracting as a named pattern distinct from Vercel's parallel multi-agent-role description (Claim 3): here the human's first exposure to an issue can be a fix already verified by the reporter, not a raw bug report. Schott separately called this "a five-year problem" solved in six months, and stated: "I've never seen that in my entire decade-plus experience with open source," and "Being able to essentially treat issues as a thing that every week, you prioritize — no matter what — versus a backlog that you're constantly trimming" — a specific before/after framing (perpetual backlog trimming vs. weekly-prioritizable queue) worth citing as the qualitative payoff distinct from the raw resolution-rate metrics Vercel reports.

### Claim 7: Astro's auto-triage system directly led Fred Schott to build a new, separate agent framework, Flue, and Flue's contributor guide states an explicit intent to prevent "Drive-by AI slop PRs"
- **Evidence**: Author's causal framing plus a direct quote from Flue's
  published contributor guide.
- **Confidence**: emerging (a stated causal link from the project's own
  creator, and a directly quoted phrase from a public contributor-guide
  document)
- **Quote**: "Furthermore, the Astro 'auto-triage' system directly led to Schott creating a brand new agent framework, called Flue." Flue's contributor guide "states that 'we're going to try to reimagine things' — partly to prevent what it calls 'Drive-by AI slop PRs.'"
- **Our assessment**: This traces a specific lineage — an internal triage-automation tool built to manage one project's backlog became the seed for a general-purpose agent framework (Flue) whose stated design goal includes preventing low-effort, AI-generated external PRs specifically. This corroborates, from the project-management-motivation side, `blog-latentspace-flue-2-react-agents.md` Claim 9's separate account (from the same interview subject, a different article) that Flue began as "just automation in a repo" before generalizing — the two articles describe the same origin story from two different angles (contribution-policy motivation here; technical architecture evolution there).

### Claim 8: Under Flue's policy, every external pull request submitted to the project is automatically closed and converted into an issue (for bug reports/fix proposals) or a discussion (for feature requests); Schott frames this as treating incoming requests as "leads" rather than as work a maintainer is obliged to review, using a combination of the team's own expertise and "the best available SOTA [State-of-the-Art] LLMs" to decide what to work on next, after which agents are deployed for "research, design, implementation, and initial review"
- **Evidence**: Direct quotes attributed to Schott and to Flue's contributor
  guide.
- **Confidence**: emerging (a specific, stated, currently-live policy at one
  project, directly attributed to its creator and public documentation)
- **Quote**: "If you submit a PR, no hard feelings, we're just going to go and represent it for you as issues and discussions. And from there, trying to figure out the right way to bring people on." The contributor guide states it uses "the best available SOTA [State-of-the-Art] LLMs that we have access to" to help decide what to work on next, after which agents are deployed for "research, design, implementation, and initial review."
- **Our assessment**: This is the most granular, publicly-documented example in the article of a project stating precisely which stages of the SDLC (research, design, implementation, initial review) are delegated to agents versus which remain with a human maintainer (the final "what to work on next" decision, and — per Claim 2's general pattern — the merge decision). The "leads, not obligations" reframing of incoming external requests is a distinct psychological/process shift from Vercel's approach (Claim 5): Vercel is quantifying how much of an existing PR/issue stream its agents resolve, while Flue is redefining what an external PR *is* (no longer reviewable code, only a signal).

### Claim 9: tldraw (50,000 GitHub stars, described by the article as "source available") automatically closes all external pull requests; creator Steve Ruiz announced this policy in January 2026 and reiterated it five months later, framing it as a response to "changes in how we're coding (more discussion, more agents), the social practices around public contribution, and the changing landscape around code security"
- **Evidence**: Direct quote from Steve Ruiz, cited by the article as a
  public restatement of a January 2026 policy announcement.
- **Confidence**: emerging (a named maintainer's public, dated policy
  statement, directly quoted)
- **Quote**: Ruiz's reiterated policy was "an opinionated decision made in response to changes in how we're coding (more discussion, more agents), the social practices around public contribution, and the changing landscape around code security."
- **Our assessment**: Ruiz's three named reasons (coding-practice change, social-practice change, code-security landscape change) are broader than either Vercel's or Flue's stated rationale — he explicitly names *security* as a distinct driver, a consideration neither Vercel's nor Astro/Flue's quotes in this article mention. This is worth flagging separately in the guide: the "close external PRs" policy shift is not motivated by a single shared reason across projects, but by at least three distinguishable concerns (review-capacity/trust, security, and social/process norms) that happen to converge on the same policy.

### Claim 10: Mitchell Hashimoto (HashiCorp co-founder, Ghostty creator, now co-founder of Superlogical) predicts that large open source projects will close contributions completely, to which Steve Ruiz responded that it makes less sense to accept human-submitted code once an issue is well-specified enough that an agent can write the code directly
- **Evidence**: A direct quote from Hashimoto (attributed by the article, not
  block-quoted from a linked primary source in the extracted text) and a
  direct quote from Ruiz responding to it.
- **Confidence**: anecdotal (two named practitioners' predictive/normative
  opinions in a public exchange, not a measured trend or a policy either
  has actually implemented at the scale predicted)
- **Quote**: Hashimoto: "the future is that large open source projects will close contributions completely." Ruiz, in response: "It just makes less sense to have people contributing code if the issue is decently well-specified and the code can be written by agents."
- **Our assessment**: This is the article's most extreme, unhedged prediction — full closure of contributions at "large" projects generally, not just the four case studies discussed — and it comes from a named, credible open-source figure (Hashimoto) but is explicitly a forward-looking prediction, not a described current policy anywhere in the article. Ruiz's response reframes the underlying logic as contingent on spec quality ("if the issue is decently well-specified"), which is a narrower, more conditional claim than Hashimoto's blanket prediction — the guide should preserve that distinction rather than treating the two quotes as making the identical claim.

### Claim 11: Fred Schott explicitly acknowledges a community/maintainer-pipeline risk in the software-factory approach: narrowing who does the code work does not solve the problem of what happens to a project when its core maintainers eventually step away, since traditionally PR review has also served to teach and evaluate future maintainers
- **Evidence**: Author's framing of the traditional PR-review-as-mentorship
  function, followed by a direct quote from Schott acknowledging the risk.
- **Confidence**: emerging (a named maintainer's own stated concern about his
  own project's approach — a self-critical admission rather than an outside
  critique, though not a resolved or measured problem)
- **Quote**: "It still leaves this open hole of, well, if you just keep narrowing the project, at a certain point, you and I go on vacation — what happens? It doesn't really solve every problem."
- **Our assessment**: This is a notable self-critical admission from a source whose own project (Flue) is one of the two most aggressive examples of PR-closing in the article — Schott does not present the software-factory/PR-closing pattern as a solved problem, only as a solution to the immediate triage/backlog crisis (Claim 6). The traditional function being lost — PR review as a mechanism to "teach contributors and assess them as future maintainers" (author's framing) — is a specific, named cost of the pattern that none of the article's four case studies claim to have replaced with an equivalent mechanism.

### Claim 12: Both Flue and tldraw, despite closing external PRs, continue to accept new issues and discussions; the article and Ruiz frame ongoing discussion-based (not code-based) engagement as a path for community members to build trust with maintainers and potentially prove themselves as future maintainer candidates, with Ruiz stating community contribution should be limited "to the places it still matters: reporting, discussion, perspective, and care"
- **Evidence**: Author's synthesis plus a closing direct quote from Ruiz.
- **Confidence**: anecdotal (a proposed, not measured, alternative
  community-engagement pathway — no project in the article reports data on
  whether discussion-based engagement actually produces new maintainers at
  a comparable rate to the prior PR-review pathway)
- **Quote**: "it's better to limit community contribution to the places it still matters: reporting, discussion, perspective, and care," as tldraw founder Steve Ruiz put it.
- **Our assessment**: This is the article's proposed answer to the risk named in Claim 11, but it is explicitly speculative ("perhaps points to a solution") rather than evidenced — no project quantifies how many contributors have transitioned from discussion participant to trusted maintainer under the new model, so the guide should present this as an open, untested hypothesis about what replaces code-contribution-based community-building, not a demonstrated replacement mechanism.

## Concrete Artifacts

### Vercel AI SDK software factory — stated architecture (as described in the article)
```
Source: https://www.latent.space/p/pr-not-welcome, attributed to Vercel
engineer Lars Grammel's YouTube explainer and Vercel's own blog post
"Building a software factory for AI SDK"

- Multiple specialized agents, each focused on a different task:
  one reproduces a bug, another applies a fix, another reviews the fix.
- Deployment architecture (per Grammel): "there is a UI, there's a web
  app, there's an underlying API, there's an execution space, and there
  are sandboxes." Synchronized with GitHub, which automatically triggers
  further actions. The UI was custom-built by Vercel.
- Backlog before deployment (late June 2026): 1,000+ open issues,
  ~800 open pull requests.
- Results after 4 weeks: authors 25-35% of merged PRs; closes 70-80%
  of issues.
```

### Named project policies on external PRs (as reported in the article)
```
Source: https://www.latent.space/p/pr-not-welcome

Vercel AI SDK  — accepts PRs, but agent-authored PRs now form a large
                 share (25-35%) of what gets merged; agents handle
                 reproduction/fix/review before human merge decision.
Astro          — accepts PRs; agents handle triage, bug reproduction,
                 and get the reporter to verify a suggested fix before
                 a human maintainer looks at the issue.
Flue           — closes ALL external PRs automatically, converts to
                 issue (bugs/fixes) or discussion (features).
tldraw         — closes ALL external PRs automatically (policy
                 announced January 2026, reiterated ~June 2026).
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-software-factories-light-dark.md` Claim 1 (the loop →
    harness → factory stack, with the review gate as the sole non-scaling
    box) and Claim 6 (a "lit" factory moves human judgment upstream rather
    than eliminating it): Claim 2 here — every case study in this article
    keeps a human at the final merge decision, even at Flue and tldraw where
    the *review of external submissions* is eliminated entirely by closing
    them outright — is a concrete, named-project instantiation of Osmani's
    abstract "review gate never fully disappears" claim, applied to the OSS
    contribution-management context specifically rather than internal
    engineering pipelines.
  - `blog-pragmaticengineer-orosz-openai-software-factory.md` Claim 11-12
    (OpenAI's risk-tiered agentic code review and auto-approval for
    low-risk PRs) and Claim 14 (the named, multi-step "agentic software
    factory" pipeline): this article's Vercel case study (Claims 3-5) is an
    independent, second named company ("software factory" terminology used
    identically) building a comparable multi-agent PR pipeline, applied to
    an open-source project's *external* contribution stream rather than
    OpenAI's internal engineering pipeline — extending the "software
    factory" pattern's documented reach from internal engineering
    (OpenAI) to open-source community management (Vercel, Astro, Flue,
    tldraw).
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md` Claim 6
    (Tereza Tížková's definition of "software factory": "the whole
    lifecycle of developing software with autonomy... collecting all the
    signals, reacting to user feedback [and] to logs, prioritizing what's
    important, then orchestrating it all") and Claim 8 (Zach Lloyd's
    framing of "factory" as a per-organization configuration choice over
    which lifecycle stages to automate): this article's four case studies
    are concrete, named instances of exactly that per-organization dial —
    Vercel automates reproduce/fix/review but keeps merge human; Astro
    automates triage/reproduction/verification but keeps the final look
    human; Flue and tldraw automate (via closure) the entire external-PR
    review stage itself. This article supplies the missing "here is what
    the dial actually looks like set to different positions, at named
    companies" evidence that dispatch's more abstract, conference-stage
    framing did not have.
  - `blog-latentspace-flue-2-react-agents.md` Claim 9 (Flue's origin as an
    internal Astro-repo issue-triage script that grew into a general
    framework, from the same interview subject Fred Schott in a different
    article): this article's Claim 7 independently corroborates that origin
    story from the contribution-policy-motivation angle (the triage
    automation's success directly motivated generalizing it into Flue),
    complementing that note's technical-architecture-evolution angle.

- **Contradicts**: None filed. No claim in this article materially opposes
  a specific claim in an existing source note in a way that would change
  guide advice. The closest tension is internal to this article itself,
  not against the corpus: Ruiz's own two quotes (Claim 9's process/security/
  social rationale for tldraw's policy vs. Claim 12's "reporting,
  discussion, perspective, and care" framing of what remains valuable about
  community contribution) sit in mild tension with Hashimoto's blanket
  "close contributions completely" prediction (Claim 10) — Ruiz's own
  practice (still accepting issues/discussions) is more moderate than
  Hashimoto's stated prediction, even though Ruiz agrees with Hashimoto's
  underlying logic in his reply. This is a difference in degree between two
  practitioners in the same conversation, not a fileable contradiction
  between sources.

- **Extends**:
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 1 (the
    invent/challenge/apply three-workflow separation of concerns for
    self-sustaining quality automation): Vercel's role-specialized agent
    pipeline (Claim 3 here — one agent reproduces, one fixes, one reviews)
    is a structurally similar pattern — partitioning a traditionally
    conflated human workflow (triage a bug, fix it, review the fix) into
    independent, specialized agent roles — applied to external-contribution
    management rather than internal linter maintenance. Worth citing
    together as two independent instances of the same "partition a
    traditionally single-person workflow into specialized agent roles"
    design principle.
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md` Claim 10
    (Cursor's Pauline Brunet positioning Forward Deployed Engineering within
    the software-factory shift) and Claim 2 (Allie Howe citing Huntley's
    "ralph loop" as the conceptual seed for AIEWF's Software Factories
    track): this article adds a new dimension to the corpus's "software
    factory" coverage — the *external-facing*, community-management use of
    the pattern — that neither the AIEWF dispatch (internal vendor
    positioning) nor the OpenAI/Vercel-internal-engineering sources cover.

- **Novel**:
  - **Named projects that fully close external code contributions and
    convert them to issues/discussions** (Flue, tldraw — Claims 1, 8-9):
    not documented anywhere else in the corpus. Prior corpus "software
    factory" sources (Vercel eve/AI SDK internals, OpenAI, Cursor's
    maintenance factory, the AIEWF dispatch) all describe factories
    processing an organization's *own* internal engineering work, not
    filtering *external, public* code contributions.
  - **Concrete, dated adoption metrics for an OSS-contribution software
    factory** (Vercel: 25-35% of merged PRs authored, 70-80% of issues
    closed, within 4 weeks — Claim 5): the most specific quantified
    before/after metric in the corpus for this specific use case.
  - **The explicit community/maintainer-pipeline risk, self-named by a
    practicing maintainer** (Schott's "you and I go on vacation — what
    happens?" — Claim 11): a named, first-party acknowledgment that
    closing/automating external contribution may sever a traditional
    future-maintainer pipeline, without a demonstrated replacement.
  - **A named security rationale for closing external PRs, distinct from
    the trust/velocity rationale given by other projects** (Ruiz's "the
    changing landscape around code security" — Claim 9): not previously
    documented in the corpus as a distinct driver of PR-closing policies.
  - **A named practitioner's unhedged prediction that "large open source
    projects will close contributions completely"** (Hashimoto — Claim 10):
    the most extreme, generalized version of this claim in the corpus;
    existing corpus material describes specific companies' internal
    practices, not a blanket prediction about the OSS ecosystem broadly.

## Guide Impact

- **Chapter 01 (Daily Workflows) / Chapter 05 (Team Adoption)**: Add the
  four named case studies (Vercel AI SDK, Astro, Flue, tldraw — Claims 1,
  3-9) as concrete examples of the "software factory" pattern applied
  specifically to *external, public* contribution management, distinct from
  the corpus's existing internal-engineering-focused software factory
  material (OpenAI, Cursor). This is a genuinely new axis for the guide:
  teams maintaining public repositories, not just internal codebases, now
  have named precedent for agent-mediated (or agent-replaced) contribution
  review, at four different points on the automation spectrum (Vercel:
  agents assist, human merges; Astro: agents pre-verify, human glances;
  Flue/tldraw: agents replace review of code entirely, human engages only
  via issues/discussions).
- **Chapter 05 (Team Adoption — community/organizational risk)**: Add
  Claim 11 (Schott's explicit "you and I go on vacation" concern) and
  Claim 12 (the untested "discussion-based trust-building replaces
  PR-review-based trust-building" hypothesis) as a concrete, named
  practitioner caution: the guide should not present agent-mediated
  contribution management as a solved problem for long-term project
  sustainability/maintainer succession — the sources in this very article
  who have gone furthest with the pattern (Flue, tldraw) do not claim to
  have solved it, only to have solved the immediate backlog/trust problem.
- **Chapter 02 (Harness Engineering)**: Add Vercel's role-specialized
  multi-agent PR pipeline (Claim 3, Concrete Artifacts) as a named,
  quantified example of the "partition a workflow into specialized agent
  roles" pattern already documented via `blog-ghaw-custom-linters-three-workflow-loop.md`,
  applied here to external-contribution triage/fix/review rather than
  internal linter maintenance — useful as a second, independent case study
  of the same design principle.

## Extraction Notes

- The article was fetched via `curl` with a browser user-agent (HTTP 200,
  no paywall encountered) and converted from raw HTML to plain text with a
  Python stdlib tag-stripping pass, after an initial `WebFetch` summarizing
  pass returned a condensed rewrite that did not preserve exact wording —
  consistent with the pattern documented in several other Latent
  Space/Substack source notes in this corpus. All `Quote` fields above were
  checked against the raw-text extraction, not the summarized rendering.
  Quotes are kept intentionally short (sentence-length, matching the
  template's citation purpose) rather than reproducing the article's full
  body text as a verbatim block.
- No sub-pages were followed. The article references, but this note does
  not separately fetch: Vercel's own blog post "Building a software factory
  for AI SDK," Lars Grammel's YouTube video, Flue's public contributor
  guide, and Steve Ruiz's original January 2026 policy announcement — the
  article's own reporting of quotes and figures from these primary sources
  is treated as the citable content for this note, consistent with
  MINER.md's guidance to follow substantive *linked* pages; the article as
  served did not contain inline hyperlinks to these primary sources in the
  extracted text (embedded as styled spans/cards without resolvable href
  text in the plain-text extraction), so they were not independently
  re-fetched. A future Miner could treat Vercel's own "Building a software
  factory for AI SDK" post as a lead for a deeper, first-party mining pass
  on the same system this article only reports secondhand.
- Confidence set to `emerging` overall: the article combines one
  first-party, quantified vendor claim (Vercel, self-reported, 4-week
  window, Claim 5), two named-maintainer first-person interview/public-post
  accounts (Astro/Flue's Schott, tldraw's Ruiz) with qualitative but
  unquantified claims, and one unhedged practitioner prediction (Hashimoto,
  Claim 10) with no supporting data. No claim in the article is
  independently audited or corroborated by a third party beyond the
  reporter's own relaying of primary-source quotes and figures.
- Cross-references to `blog-addyosmani-software-factories-light-dark.md`,
  `blog-pragmaticengineer-orosz-openai-software-factory.md`,
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md`,
  `blog-latentspace-flue-2-react-agents.md`, and
  `blog-ghaw-custom-linters-three-workflow-loop.md` were each re-read in
  full before citing; all cited claim numbers were located and confirmed
  in document order before writing this note, per MINER.md §4b.
- No contradiction meeting the MINER.md §4a filing bar was found; the one
  candidate tension (Ruiz's moderate practice vs. Hashimoto's blanket
  prediction) is documented under Cross-References → Contradicts above
  with reasoning for why it was not filed as a formal contradiction issue.
