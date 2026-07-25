---
source_url: https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/
source_type: blog-post
title: "AI Mania Is Eviscerating Global Decision-Making"
author: Nikhil Suresh (Ludicity); curated by Simon Willison
date_published: 2026-07-18
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: anecdotal
issue: "#2212"
---

# AI Mania Is Eviscerating Global Decision-Making

> A consultant's first-person account of organizational AI-adoption dysfunction —
> "0% success" across every AI project his team has observed in eighteen months,
> a career-risk coordination problem that makes honest reporting of AI outcomes
> nearly impossible at scale, and a structural explanation for why non-AI projects
> get relabeled "AI-driven" and demo-driven buying frenzies override rational
> procurement.

## Source Context

- **Type**: blog-post (Ludicity, Nikhil Suresh's personal/company blog, published
  July 18, 2026; long-form essay, ~3,200 words, cross-posted to the author's
  consultancy's own blog at hermit-tech.com). Surfaced via Simon Willison's
  link-blog (simonwillison.net/2026/Jul/19/ai-mania/), which frames it as an essay
  "examining AI hype at major corporations" discovered via Hacker News. Willison's
  own commentary is minimal (a short framing paragraph plus tags `ai`,
  `ai-ethics`, `ai-misuse`); the substantive content is entirely Suresh's. This
  note extracts from the original Ludicity essay, fetched and parsed from raw
  HTML to recover verbatim quotes (see Extraction Notes).
- **Author credibility**: Nikhil Suresh ("Nik Suresh") is, per his own "About Me"
  page (ludic.mataroa.blog/about-me/), based in Melbourne, Australia, and is
  "the executive director of a consultancy" — a small operation ("just myself and
  five friends") that does data/software engineering consulting work, including
  Snowflake deployments referenced in this essay. His claims are drawn from
  running his firm's sales process, leading "all but two" of the firm's technical
  engagements over the past year, and roughly 300 informal professional
  conversations with people ranging from niche-service-industry workers to
  Fortune 500 executives. This is first-person practitioner testimony from
  someone with direct commercial exposure to how enterprises buy and run AI
  projects — not a survey, academic study, or investigative report. He is not
  a disinterested observer: his firm has explicitly "rejected all AI implementation
  work" and markets itself in opposition to "grifters," which is a plausible source
  of selection bias (see Extraction Notes).
- **Scope**: Covers organizational-level dynamics of AI adoption at large
  companies (500+ employees) and their vendors: reported vs. actual project
  success rates, why honest reporting is suppressed, executive/board incentive
  structures, AI-demo-driven buying behavior, and practical survival tactics for
  employees and consultants navigating this environment. Grounded in the author's
  direct engagements (data/analytics consulting, Snowflake deployments) and
  secondhand accounts from his professional network. Does NOT cover: AI model
  capability evaluation, technical benchmarking, or engineering-practice guidance
  (CLAUDE.md design, agent harness architecture, etc.) — this is an
  organizational-sociology piece, not a technical one. Does not represent
  small companies, startups building AI-native products from scratch (the
  essay explicitly notes his firm avoids those engagements), or successful
  AI adoption cases, since the author states his team has "quickly learned...
  not to ask anything about ongoing AI projects" once one starts (i.e., the
  sample is skewed toward troubled/failing projects that surface organically).

## Extracted Claims

### Claim 1: The author's team has observed a 0% success rate across all AI projects they have encountered in eighteen months, whether as direct participants or bystanders on unrelated work
- **Evidence**: Direct first-person claim, stated as the load-bearing empirical
  anchor for the whole essay.
- **Confidence**: anecdotal (one consultancy's observational sample, not a
  survey or controlled study; the author does not define "success" numerically
  or disclose the total number of projects observed)
- **Quote**: "All of the AI projects we have observed as a team are failing. Every single one – we have seen 0% success in a year and a half, not only amongst projects we have been asked to participate in, but even within projects that we have observed in passing while doing totally unrelated work."
- **Our assessment**: This is the essay's central, most falsifiable-sounding claim,
  and also its weakest empirically — "success" is undefined, the sample size and
  selection process are undisclosed, and the author's own footnote states his firm
  has "rejected all AI implementation work," which likely biases his network
  toward people dealing with failures (successful, quiet AI deployments have less
  reason to surface in his conversations). Treat as a strong directional signal
  from an unusually well-networked observer, not a measured failure rate. See
  filed contradiction (Cross-References) against a vendor's own claimed
  productivity-measurement rigor.

### Claim 2: Companies systematically avoid tracking basic AI-adoption metrics, or track metrics that are easily gamed, rather than measuring actual usage or outcomes
- **Evidence**: Direct observation from consulting engagements involving both
  internal and customer-facing AI chatbots.
- **Confidence**: anecdotal
- **Quote**: "In both cases, project leaders are very careful to avoid tracking basic metrics, such as whether the tools are being used at all, or they track metrics that are easily gamed."
- **Our assessment**: This is a structural claim about measurement avoidance as a
  deliberate (if not fully conscious) organizational behavior, not just a
  competence gap. Pairs directly with the "token leaderboard" anecdote (Claim 5)
  as a concrete example of "metrics that are easily gamed."

### Claim 3: Internal AI chatbots see minimal employee adoption because they can only surface information that is already well-documented, and most companies have low-quality internal documentation
- **Evidence**: Direct first-person observation across the author's consulting
  engagements.
- **Confidence**: anecdotal
- **Quote**: "Employees don't use internal chatbots because companies tend to have low-quality documentation and an LLM is not psychic – it can only know things that have been written down and made accessible."
- **Our assessment**: A concrete, falsifiable causal mechanism (not just "adoption
  is low") — the bottleneck is pre-existing documentation quality, not the LLM
  itself. This is a specific, actionable diagnostic for any team evaluating why
  an internal knowledge chatbot is underperforming: check documentation coverage
  before blaming the model or the tool.

### Claim 4: Continued career advancement and employment at large companies increasingly requires public professions of belief in AI's transformative power, independent of actual technical understanding or usage
- **Evidence**: Repeated first-person observations across many organizations
  (500+ employees), including a specific anecdote about an executive who had
  never used any AI tool personally while authoring an AI-centered technical
  strategy for a $2B+-revenue organization.
- **Confidence**: anecdotal
- **Quote**: "In every sufficiently large business we have observed (say, with 500+ employees), we have noted that continued advancement, and increasingly continued employment, has started to require repeated professions of belief in the transformative power of AI for said business. I am not talking about providing ideas about how to use AI in the business – I mean religious profession, declarations of faith."
- **Quote 2 (the executive anecdote)**: "In one extreme case, I have seen an executive confess that they had never even used ChatGPT or any AI tool in their life, immediately after producing a technical strategy for an organisation with $2B+ in revenue which was entirely centered around AI."
- **Our assessment**: The "religious profession" framing is the essay's central
  metaphor (reinforced by section headers like "Heretics Will Be Shot" and a
  mock confession format later in the piece). The executive anecdote is the
  single most concrete, quotable data point in the source and directly supports
  the Prospector's triage note about "executives with zero AI experience
  producing AI technical strategy for $2B+ revenue organizations."

### Claim 5: Engineers are gaming AI-usage metrics (e.g., "token leaderboards") by running self-prompting loops that consume tokens without producing usable work, undetected by management
- **Evidence**: Direct observation plus a verbatim quote attributed to "an actual
  software engineer" (anonymized source, per the author's stated practice of
  filing off identifying details).
- **Confidence**: anecdotal
- **Quote**: "Others are being measured on their AI bills with 'token leaderboards', where higher is better... the people hired for their freakish ability to perform system optimisation do the obvious thing. They set the LLMs prompting themselves in a semi-plausible loop in case someone inspects the token consumption and then they watch Netflix. Not a single one has been caught, even when their own assessment of the output is that it isn't suitable for deployment."
- **Quote 2 (engineer's own words)**: "Checking out a parallel copy of our Go repository and telling the AI to rewrite the whole thing in Zig while I work on something else just so I can keep my job. I hate this shit so much. My job has usage tracking and quotas. I don't use it for actual work, I just spin it up and disregard the output."
- **Our assessment**: This is the single most concrete, mechanism-level
  "gamed metric" example in the corpus so far — engineers running unfaithful
  self-prompting loops specifically to defeat token-consumption dashboards.
  It directly extends the corpus's existing token-budget/token-crisis material
  (see Cross-References) with a bad-faith-gaming failure mode those sources
  don't cover: the budget/spend metrics themselves become adversarial targets
  once they're used as individual performance measures.

### Claim 6: Engineers are secretly rewriting production codebases in unfamiliar languages using AI tools, driven by fear of AI-related job loss rather than any technical requirement
- **Evidence**: The same anonymized engineer quote as Claim 5 (Go-to-Zig
  rewrite), presented by the author as representative of a broader pattern he
  has observed.
- **Confidence**: anecdotal (single quoted individual, though the author frames
  it as illustrative of a pattern, not an isolated incident)
- **Quote**: "Checking out a parallel copy of our Go repository and telling the AI to rewrite the whole thing in Zig while I work on something else just so I can keep my job."
  — an actual software engineer, quoted by Nikhil Suresh
- **Our assessment**: This corroborates the Prospector's triage note ("Engineers
  rewriting major codebases in unfamiliar languages to preserve employment
  against perceived AI replacement risk"). Notably the engineer explicitly
  states the rewritten output is disregarded ("I don't use it for actual
  work") — the activity is pure performance for management visibility, not a
  genuine technical migration. This is a distinct phenomenon from legitimate
  AI-assisted rewrites and should not be conflated with them in the guide.

### Claim 7: Vendors are structurally unable to contradict customers' inflated AI productivity claims (e.g., "100x productivity") without risking contract cancellation and personal career consequences
- **Evidence**: A private, off-the-record conversation the author had with a
  Fortune 500 executive (one of the executives referenced elsewhere in the
  essay), conducted specifically "without any microphones around."
- **Confidence**: anecdotal (single off-the-record source, though the author
  frames it as explaining a widely observed pattern of "extremely strange"
  hesitancy that he sets out specifically to investigate)
- **Quote**: "Executives at their customers were saying absurd things about achieving 100x productivity, and this meant that if any executive at the vendor said that these gains were not plausible, it would undermine the credibility of the customer's executive, be perceived as an attack (or heresy), and possibly result in an enterprise contract cancellation. And getting enterprise contracts cancelled because you wanted to opine on something that doesn't really matter to your organisation's mission is a great way to get fired."
- **Our assessment**: This is the essay's most structurally interesting claim —
  it's not "vendors lie because they're incentivized to oversell," it's
  "vendors cannot correct customer executives' own lies without punishing
  themselves," which is a genuinely different (and more corrosive) mechanism:
  dishonesty compounds bidirectionally between customer and vendor rather than
  originating one-sidedly from either side.

### Claim 8: Executive dishonesty about AI gains is sustained by a multi-party coordination problem — no individual executive can admit uncertainty without appearing to accuse peers of lying, incompetence, or cowardice, and there is no mechanism to coordinate simultaneous honesty
- **Evidence**: The author's synthesis, following directly from the Claim 7
  anecdote, extended to describe a market-wide dynamic among executives who
  are simultaneously vendors and customers of each other's services.
- **Confidence**: anecdotal (author's interpretive synthesis of the pattern
  described in Claim 7, not a separate independently-sourced data point)
- **Quote**: "This is to say that we're facing a coordination problem around executives being honest around the AI gains they've witnessed – if they co-operate, they keep their jobs. If they defect, they will possibly be fired by their embarrassed peers (who have now been implicitly called liars, cowards, or incompetents) and then replaced with someone that will toe the line anyway. If they could all admit the truth at once there might be some hope, but there is no way to coordinate that event."
- **Our assessment**: Framed explicitly (by the author's own vocabulary — "coordination problem," "co-operate," "defect") as a game-theoretic / prisoner's-dilemma-style structure. This is the essay's clearest candidate for a durable analytical framework, independent of the specific 2026 AI cycle: it predicts that public claims about any hyped technology will systematically over-state benefits for as long as the coordination problem persists, and that the failure mode resolves only through external shock (e.g., a market correction), not through any individual actor choosing honesty.

### Claim 9: Even skeptical board members at large public companies privately acknowledge doubts about AI investment ROI but feel unable to act on that skepticism due to positional risk
- **Evidence**: The author's own direct experience presenting to S&P 500 board
  members on "navigating AI hype," including a specific quoted comment from a
  board member.
- **Confidence**: anecdotal
- **Quote**: "the main comments I remember from the session were board members admitting they were skeptical, but expressing anxiety that their positions were contingent on demanding AI investment. One of them commented 'investing this early seems like risk without much upside'."
- **Our assessment**: Extends the executive-level coordination problem (Claim 8)
  up to the board level, suggesting the dynamic is not confined to operational
  management but present at the highest oversight layer of large public
  companies — undermining the assumption that board governance would function
  as a check on executive AI-hype excess.

### Claim 10: Non-AI projects are frequently relabeled as "AI-driven" after the fact to satisfy organizational mandates, with the actual AI component often minimal, cosmetic, or a failed pilot that was quietly replaced by manual work
- **Evidence**: A specific, detailed anecdote about an Oracle-to-Snowflake
  database migration where an LLM-based SQL translation phase failed (for
  permissions reasons, not model capability) and was silently replaced by
  manual translation, while still being reported internally as an AI-driven
  success.
- **Confidence**: anecdotal
- **Quote**: "When the project failed (due to issues getting enough permissions to automate the work, not because an LLM can't do something that easy), the vendor simply started handling the translation by hand but the company billed it as an AI-driven success because some inconsequential portion of the SQL had been translated by AI before being pasted over."
- **Quote 2 (author's summary framing)**: "My assessment of the market so far is that a substantial component of the outburst of AI projects are actually non-AI projects with an AI element slapped on after the fact to pass the purity test."
- **Our assessment**: This is a concrete, mechanistic example of "AI-washing"
  at the project-reporting level (distinct from Claim 4's individual-belief
  "AI-washing," where engineers claim AI did work they did manually). Directly
  relevant to any guide section on evaluating vendor or internal AI-project
  success claims: a reported "AI-driven" label does not reliably indicate the
  AI component was load-bearing, or even functional.

### Claim 11: Even lukewarm, skeptical prospective clients exhibit an immediate, overwhelming buying urge upon seeing a flashy AI demo, overriding prior rational cost-benefit consideration — even when told explicitly that the demoed capability would not meet their actual needs
- **Evidence**: A specific, detailed first-person account of the author's firm
  demonstrating Snowflake's "Cortex" natural-language-query feature (which the
  author states reaches only ~92% accuracy on complex enterprise data per a
  Snowflake staff presentation) to several "lukewarm" prospects, all of whom
  attempted to buy immediately despite explicit caveats.
- **Confidence**: anecdotal
- **Quote**: "every lukewarm client that saw the chatbot in action, even with us telling them that it was not going to accomplish what they wanted, wanted to buy it immediately. Every other consideration, including millions of dollars that we could plausibly help them achieve by non-AI means, was swept aside."
- **Our assessment**: The author's firm responded by removing the demo from
  their sales process entirely and declining the resulting sales — a notable
  self-restraint data point that lends some credibility to the account (it is
  not in the author's commercial interest to describe a technique that reliably
  closes deals and then discard it). The ~92% accuracy figure is attributed to
  "actual Snowflake staff" in a presentation the author recalls "from memory"
  — treat that specific number as weakly sourced (secondhand, unverified,
  memory-based) even though the buying-frenzy anecdote itself is a direct
  first-person account.

### Claim 12: Practical mitigation tactics exist for individuals trying to raise concerns about AI projects without triggering retaliation: one-on-one conversations (not group settings), anonymous 1-10 success-rating polls to surface hidden bimodal disagreement, and involving frontline users directly
- **Evidence**: The author's own consulting practice, presented as accumulated
  technique ("an effective trick that I believe I picked up from Secrets of
  Consulting").
- **Confidence**: anecdotal
- **Quote**: "an effective trick... is the anonymous poll, where you can ask individuals to rate their opinion of an AI project's success chances on a scale of 1 to 10. The typical split I have observed is half of those involved rating the project at a 3/10 and others at around an 8/10 – a clear bimodal split on a project that was already three years late."
- **Our assessment**: This is the essay's most directly actionable, guide-relevant
  material — a concrete diagnostic technique (anonymous bimodal-rating polls)
  for surfacing suppressed disagreement about a project's real status, distinct
  from the essay's mostly-diagnostic (not prescriptive) tone elsewhere.

## Concrete Artifacts

### The "AI Mania" mechanism chain, as the author frames it (synthesized from the essay's section structure)

```
Source: Nikhil Suresh, "AI Mania Is Eviscerating Global Decision-Making"
        (ludic.mataroa.blog, July 18, 2026)

I.   AI Investments Are Generally Total Failures
     -> 0% observed success rate; metrics avoided or gamed

II.  Heretics Will Be Shot
     -> Career risk for skepticism; "religious profession" required for advancement;
        AI-washing of individual work ("say Claude did it"); token-leaderboard gaming

III. AI Demos Are The Mind-Killer
     -> Flashy demos trigger irrational buying urges even in skeptical prospects,
        overriding rational cost-benefit evaluation

IV.  Executives, Game Theory, and The Emperor's Clothes
     -> Vendor-customer contract pressure suppresses honest vendor pushback;
        multi-party coordination problem prevents simultaneous honest disclosure
        among executives and boards

V.   You Must Be This AI-Native To Ride
     -> Non-AI projects relabeled "AI-driven" post hoc to pass organizational
        purity tests; headcount requests require demonstrating prior AI attempts
```

### Practical survival/mitigation tactics (verbatim excerpts, attributed)

```
Source: Nikhil Suresh, "AI Mania Is Eviscerating Global Decision-Making"

For people trying to fix a project or raise concerns:
- "Where possible, when raising issues, do not have conversations about the
   state of AI projects in group settings... Arrange for one-on-one settings."
- Anonymous 1-10 success-rating polls to surface bimodal hidden disagreement.
- "Always involve people on the ground. The only source of data on whether
   projects are succeeding or the investment is going anywhere are the people
   that use it for their day-to-day activity."
- "Do not question the broadest claims about AI... The challenge can only come
   after you have gained the trust of the most senior person involved."

For people just trying to personally survive the environment:
- "If you feel like you're going absolutely nuts, consider switching over to
   contracting."
- "I do my best to limit my uptake of AI-related news, as it is pretty
   crazy-making and unproductive to consume."
- "If you're being asked to review huge volumes of terrible AI code, just
   assume that the organisation is going to burn you out and fire you...
   Start looking for a new job as if you have already been fired."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md` — Hashimoto's claim
    that technical decision makers are "motivated primarily by NOT GETTING
    FIRED" and follow analyst/peer consensus rather than technical merit is the
    same underlying mechanism Suresh describes at the executive/board level
    (Claims 4, 8, 9): career-risk-driven conformity overriding honest technical
    assessment. Suresh adds the vendor-side half of the picture (Claim 7) that
    Hashimoto's Redis-focused account does not cover — vendors are locked into
    the same dishonesty by customer executives' own public claims.
  - `blog-thoughtworks-omahony-feature-token-budgets.md` and
    `blog-thoughtworks-kamelman-token-crisis.md` — both document token-spend as
    an organizational governance problem; Suresh's "token leaderboard" gaming
    anecdote (Claim 5) is a concrete individual-level failure mode of exactly
    the kind of spend-based metric these sources discuss architecting budgets
    around. Neither Thoughtworks source anticipates that spend metrics used as
    *performance* measures (not just cost controls) can be adversarially gamed
    by the people being measured.
  - `blog-simonwillison-uber-caps-usage.md` — Uber's per-tool spending cap is a
    cost-control response to token spend; Suresh's token-leaderboard anecdote
    (an incentive to spend *more*, not less, to look productive) is the
    inverse failure mode, illustrating that both under- and over-consumption
    can be organizationally rewarded depending on what's being measured and how.

- **Extends**:
  - `blog-simonwillison-the-pressure.md` — Stenberg's curl account documents
    workload strain from AI-amplified *external* pressure (inbound security
    reports); Suresh documents workload/integrity strain from AI-amplified
    *internal* organizational pressure (career risk, forced AI-washing,
    forced pointless rewrites). Together they sketch two distinct but
    compounding categories of AI-adoption-era burden on engineers and
    maintainers: external volume surge and internal performative-compliance
    pressure.

- **Contradicts**: Filed as
  [issue #2232](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2232)
  (**verdict: unresolved as of this note's extraction**). Suresh's Claim 1/2
  (reported AI productivity gains are almost universally false; project
  leaders avoid tracking metrics or track gameable ones) is in direct tension
  with `blog-cognition-devin-productivity-estimation.md`'s claim that
  Cognition has built and validated a rigorous, falsifiable, disclosed-limitations
  system for measuring genuine Devin-driven productivity gains. See the filed
  issue for full framing; do not cite either source's productivity-honesty
  claim as settled in the guide until this resolves.

- **Novel**:
  - **The vendor-customer bidirectional dishonesty-lock mechanism** (Claim 7):
    no existing corpus source documents *why* vendors cannot correct inflated
    customer AI claims — only that hype exists. This gives a causal, structural
    explanation (contract-cancellation risk) rather than a generic "vendors
    oversell" framing.
  - **The executive/board coordination-problem framing** (Claims 8-9), stated
    explicitly in game-theoretic vocabulary ("co-operate," "defect"). No other
    corpus source models AI-hype persistence as a multi-party coordination
    failure with no mechanism for simultaneous honest disclosure.
  - **Post-hoc AI relabeling of non-AI projects to satisfy organizational
    mandates** (Claim 10), with a specific mechanistic anecdote (Oracle-to-
    Snowflake migration where a failed AI phase was quietly replaced by manual
    work but still reported as an AI success). No other corpus source documents
    this specific "AI-washing at the project level" pattern with this level of
    mechanistic detail.
  - **Anonymous bimodal-rating polls as a diagnostic technique** (Claim 12) for
    surfacing suppressed project-status disagreement — a concrete, reusable
    practitioner tool not present elsewhere in the corpus.

## Guide Impact

- **Ch05 (Team Adoption)**: Add a subsection on organizational dishonesty
  dynamics around AI project reporting, distinct from the existing
  TDM-procurement material (Hashimoto). Specific recommendation: cite Claim 8
  (the executive coordination problem) as the mechanism explaining why public
  AI-success claims should be discounted independent of any individual
  executive's honesty, and cite Claim 12 (anonymous bimodal polling) as a
  concrete technique teams can use internally to surface real project status
  before committing further investment. Flag the filed contradiction
  (issue #2232) rather than stating "vendor productivity claims are unreliable"
  as settled — the guide should note both that structural incentives favor
  inflated claims (Suresh) and that some vendors publish falsifiable,
  limitations-disclosed methodology (Cognition) without picking a winner yet.

- **Ch05 (Team Adoption — Metric Design)**: Add Claim 5 (token-leaderboard
  gaming) as a concrete cautionary example when discussing token-budget or
  AI-usage-metric design (extending `blog-thoughtworks-omahony-feature-token-budgets.md`
  and `blog-thoughtworks-kamelman-token-crisis.md`): any metric used to evaluate
  individual performance rather than pure cost control creates an incentive to
  game the metric, not the underlying outcome. Recommend outcome-based
  validation (e.g., Cognition's self-reported-ground-truth approach, flagged
  with the same caveats raised in the filed contradiction) over raw
  spend/token-count metrics as individual KPIs.

- **Ch00 (Principles) or Ch05**: Consider citing Claim 10 (post-hoc AI
  relabeling of non-AI projects) as a specific pattern to watch for when
  evaluating internal or vendor claims of "AI-driven" project success —
  readers should ask what the AI component specifically did, not just whether
  one was present in the project's billing or reporting.

## Extraction Notes

- **WebFetch returned summaries, not full text, on the first several attempts**:
  Both the Simon Willison curation page and the original Ludicity essay were
  initially fetched via WebFetch, which returned condensed AI-generated
  summaries rather than verbatim text regardless of prompt phrasing. To recover
  verbatim quotes, the raw HTML of the Ludicity essay
  (ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/)
  was downloaded directly via `curl` and parsed with Python's stdlib
  `html.parser` to extract the `posts-item-body` article content as plain text.
  All quotes in this note are taken from that raw-HTML extraction, cross-checked
  against the rendered text, not from the WebFetch summaries.
- **Author identity confirmed via the site's About page**: The essay itself
  does not carry an explicit byline in its HTML; author identity (Nikhil
  Suresh) and biographical details were confirmed by separately fetching
  ludic.mataroa.blog/about-me/.
- **Full essay read, including footnotes**: All six footnotes were read; footnote
  2 ("We have rejected all AI implementation work... every single one of our
  current contracts would be totally unaffected by OpenAI collapsing") is the
  basis for the selection-bias caveat noted in Source Context and Claim 1's
  assessment. No linked sub-pages were followed beyond the essay itself and the
  author's About page — the essay links to a Mitchell Hashimoto tweet (already
  covered by an existing corpus note), a prior Suresh essay ("Contra Ptacek's
  Terrible Article On AI") responding to Thomas Ptacek's "My AI Skeptic Friends
  Are All Nuts" (neither Ptacek's essay nor Suresh's response essay currently
  has a corpus source note — worth flagging as a future mining candidate but
  out of scope for this extraction, which is limited to the AI Mania essay
  itself), and the author's consultancy website (hermit-tech.com), none of
  which added claims beyond what's already captured here.
- **The essay is long-form opinion/testimony, not empirical research**: All
  twelve claims are anecdotal by nature — first-person or secondhand accounts
  from the author's professional network, not survey or measured data. The
  `confidence_overall: anecdotal` rating reflects this consistently across the
  source, not a judgment that the author is unreliable; his stated basis (sales
  leadership + ~300 professional conversations across a wide range of
  organizations) is broader than most single-practitioner corpus sources, but
  still self-selected and unverifiable from the outside.
