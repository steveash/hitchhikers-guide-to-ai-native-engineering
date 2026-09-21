---
source_url: https://simonwillison.net/2026/Sep/14/laurie-voss/
source_type: blog-post
title: "Quoting Laurie Voss (We are all Product Engineers now)"
author: Laurie Voss (quoted by Simon Willison); full essay published at seldo.com
date_published: 2026-09-14
date_extracted: 2026-09-21
last_checked: 2026-09-21
status: current
confidence_overall: emerging
issue: "#3590"
---

# Quoting Laurie Voss: We are all Product Engineers now

> A single-paragraph quotation post on Simon Willison's blog links to Laurie
> Voss's ~4,000-word essay "We are all Product Engineers now," which argues
> that the cost of writing code has already collapsed under LLMs, the cost
> of reviewing/fixing/operating code is collapsing next, and what remains —
> permanently, because it doesn't transfer between products — is extracting
> requirements from customers, defining "good," and making software
> pleasant to use. Voss names this recombined role "product engineer,"
> traces its lineage through "systems analyst" and "product manager," and
> documents its emergence in hiring data (job-posting growth, compensation)
> alongside a training-pipeline crisis for the judgment/taste skill it
> requires.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus a one-line citation, ~90 words total on Willison's own
  page). Auto-discovered via the `simon-willison` trusted feed. The quote's
  citation links directly to Voss's original essay at
  `seldo.com/posts/we-are-all-product-engineers-now/`, which this Miner
  fetched and read in full (per MINER.md §1) because the Willison page by
  itself is only the essay's closing summary paragraph and is not
  meaningful without the full argument behind it. Willison adds no
  editorial commentary of his own on this post.
- **Author credibility**: Laurie Voss is a co-founder of npm (the default
  JavaScript package registry) and has written about software-industry
  economics and labor markets on his personal blog across 2025–2026; the
  essay itself cites two of his own earlier posts (on AI creating "more
  programmers," on companies substituting compute for labor, and on junior
  labor-market data) as the foundation this piece builds on. He is a
  practitioner-analyst with direct industry standing (not an academic or
  journalist), and the essay is explicit about which parts are his own
  synthesis/forecast versus externally sourced data (Stanford Digital
  Economy Lab, SignalFire, GitHub, named benchmark studies). Simon
  Willison is a `trusted-feed` curator whose selection is itself a
  relevance signal, not an independent verifier of Voss's claims.
- **Scope**: Covers a 10-year forecast for how software engineering as a
  profession reshapes as AI compresses the cost of writing, then
  reviewing/fixing, then operating code, leaving "product engineering"
  (requirements extraction, defining quality, and design/delight) as the
  durable, un-transferable bottleneck. Draws on labor-market data (Stanford
  Digital Economy Lab, SignalFire, Indeed-style postings), agent-capability
  benchmark data (bug-fixing benchmarks, a Claude Code PR-merge study,
  GitHub-scale review statistics), and hiring data for "forward deployed
  engineer"-style roles. Does NOT cover: specific engineering practices,
  tooling, team-process recommendations, or company-level case studies of
  how any specific org has actually restructured around this thesis — it
  is a macro forecast and cost-taxonomy argument, not a how-to.

## Extracted Claims

### Claim 1: The cost of writing code has already collapsed under LLMs, having historically been the most expensive part of software development
- **Evidence**: Voss's own cost-taxonomy breakdown, placed first in a
  four-category list (Collapsed / Going soon / Next on the chopping block /
  Possibly safe) that structures the whole essay.
- **Confidence**: emerging (a qualitative claim from a practitioner-analyst,
  consistent with — though not independently measured against — other
  corpus cost-collapse claims; see Cross-References)
- **Quote**: "Actually writing code: historically the most expensive part of the whole process, because getting it right was really tricky. The entire industry oriented itself around very expensive programmers as the center of gravity, with every other job more or less orbiting around them. The cost of this, with LLMs, has already collapsed."
- **Our assessment**: This is the load-bearing premise for the rest of the essay's argument, and it is asserted rather than measured with a specific statistic (contrast Claims 2–3, which do cite benchmark numbers). It directly corroborates Charity Majors' claim (see Cross-References) that code generation cost inverted from "very hard, time-consuming, and expensive" to "effectively free and instant" in 2025 — two independent practitioner-analysts naming the same collapse, though neither supplies a hard before/after metric.

### Claim 2: Code review and maintenance ("reviewing," "fixing bugs," "refactoring") are "going soon" but not yet automated — agent bug-fixing benchmark scores rose from ~50% to ~95% in two years on the main benchmark (now saturated), and sit around 59% on harder benchmarks designed to resist training-data leakage
- **Evidence**: Named benchmark trend, cited without naming the specific
  benchmark(s) by name in the essay text.
- **Confidence**: emerging (specific numeric trend cited, but the source
  benchmark is not named in the essay, so this Miner cannot independently
  verify the 50%→95%/59% figures against a primary benchmark report)
- **Quote**: "On benchmarks where agents fix real bugs in real repositories, frontier models went from roughly 50% to roughly 95% in the last two years, to the point where the main benchmark is effectively saturated and people have had to build harder ones. On the harder ones, which resist the models having seen the answers during training, the best models now score around 59%."
- **Our assessment**: The "benchmark saturation forces harder benchmarks" pattern is a useful methodological caveat: it means the raw percentage trend (50%→95%) partly reflects benchmark exhaustion, not unbounded capability growth, and the 59% figure on a harder, leakage-resistant benchmark is the more honest current-state number. Voss uses this to support his "going soon, not yet" placement for review/maintenance — the trend line is real but the current absolute capability is still well short of unsupervised reliability.

### Claim 3: A study of 567 Claude Code-opened pull requests across 157 open-source projects found an 84% eventual merge rate versus a 91% human baseline, with just over half merging without any human touching them
- **Evidence**: Named study statistics, cited without naming the study's
  author or publication venue in the essay text.
- **Confidence**: emerging (specific, falsifiable numbers cited, but source
  study not named/linked in the essay, so this Miner could not independently
  verify the primary study)
- **Quote**: "A study of 567 pull requests opened by Claude Code across 157 open source projects found 84% of them eventually got merged, a bit below the human rate of 91%, and just over half went in without a human touching them."
- **Our assessment**: This is the most concrete, quantified single data point in the essay for the "reviewing" category specifically. An 84%-vs-91% merge-rate gap is a narrower gap than the "agents are still bad at review-adjacent work" framing might suggest — but "just over half went in without a human touching them" is the more load-bearing number for Voss's larger argument: it means half of already-published, judged-mergeable agent PRs currently receive no human review step at all, which is the substrate for Claim 4's review-crisis-at-scale argument.

### Claim 4: At GitHub's current scale (36M new developers, +25% commits, PR volume up ~3.5x since 2023, an estimated 17M agent-opened PRs/month), most PRs — human or agent — receive no recorded review at all, and when agent PRs are reviewed, 58% of the time the only reviewer is another agent
- **Evidence**: GitHub platform-scale statistics plus a cited 33,000-agent-PR
  study, neither named/linked by author or venue in the essay text.
- **Confidence**: emerging (specific numeric claims from named-but-unlinked
  studies; internally consistent with Claim 3's smaller-scale finding, but
  not independently verifiable by this Miner without the primary sources)
- **Quote**: "GitHub added 36 million developers and a quarter more commits in a year, and the number of merged pull requests on the platform is up something like three and a half times since 2023, with one estimate having agents alone opening 17 million PRs a month. Something should review all of that, but one study of 33,000 agent PRs found that most PRs on GitHub, human or agent, get no recorded review at all, and when agent PRs are reviewed, 58% of the time the only reviewer is another agent."
- **Our assessment**: This is the essay's strongest evidence for "the ability to create code but not to review it is causing an enormous amount of pain" — the review bottleneck is not hypothetical, it is already visible at platform scale. The "58% agent-reviewing-agent" figure is a specific, guide-relevant data point: it suggests that where review is happening at all on agent PRs, it is disproportionately not human review, which complicates any guide claim that "code review" alone is a sufficient verification gate without specifying who or what is doing the reviewing.

### Claim 5: curl shut down its bug bounty program in January (2026, implied) after the share of submitted reports that were real bugs fell from over 15% to under 5%, symptomatic of open-source projects being overwhelmed by AI-generated low-quality submissions
- **Evidence**: Named, specific incident (curl bug bounty shutdown) cited as
  an illustrative example of the review-crisis argument.
- **Confidence**: emerging (specific, checkable claim about a well-known
  open-source project; not independently verified against curl's own
  announcement by this Miner, but curl's bug-bounty struggles with
  AI-generated low-quality reports are independently well-documented in
  security-community discussion generally)
- **Quote**: "curl shut down its bug bounty in January after the share of submitted reports that were real bugs fell from better than 15% to under 5%."
- **Our assessment**: This is the essay's sharpest concrete anecdote for "AI slop overwhelming review capacity" — a named project, a named mechanism (bug bounty), and a specific before/after ratio. It is the kind of failure-mode data point the guide can cite directly when arguing that generation-without-verification-capacity is a real, already-materialized organizational risk, not a hypothetical one.

### Claim 6: Product discovery — finding out what a customer actually wants — cannot be done mechanically, because the relevant knowledge exists only in the customer's head and was never written down anywhere a model could train on
- **Evidence**: Author's own analytical argument, illustrated with a
  hypothetical ("I need to keep track of my orders" meaning different
  things for a bakery versus a car-parts factory).
- **Confidence**: emerging (a reasoned argument from a practitioner-analyst,
  not an empirical measurement — but the underlying mechanism it describes,
  that requirements knowledge is tacit and uncodified, is independently
  corroborated; see Cross-References)
- **Quote**: "You cannot do product discovery mechanically short of reading people's thoughts. You can't train it into a model, because it isn't in the training data, because it's in the head of one specific baker who's never written it down and wouldn't know how to if you asked them."
- **Our assessment**: This is the essay's central causal mechanism, and it is a genuinely different framing from most "requirements are the bottleneck" claims elsewhere in the corpus: Voss's argument is not that requirements-gathering is slow or effortful, but that the relevant knowledge is structurally absent from any possible training corpus, which makes the bottleneck permanent rather than merely currently-unsolved. This distinction matters for the guide: it implies better models will not shrink this bottleneck, only better *elicitation* processes and people will.

### Claim 7: The cost of defining "what good looks like" for a piece of software does not transfer between products — two superficially similar problems (a calendar app vs. a scheduling app, or two different bakeries) have almost nothing in common in their specific requirements — so as software demand rises without bound, this per-product cost becomes the entire remaining job
- **Evidence**: Author's own analytical argument, generalized from the
  bakery/car-parts example in Claim 6.
- **Confidence**: emerging (a structural/economic argument, not an empirical
  measurement)
- **Quote**: "As the cost of software creation falls to zero, the bottleneck moves to the description of the problem, and my thesis is that's where it's going to stay."
- **Our assessment**: This is the essay's core economic claim and the one most directly load-bearing for its title ("we are all product engineers now"). "Doesn't transfer" is the specific mechanism that distinguishes this from ordinary economies-of-scale arguments: most engineering costs (infrastructure, tooling, even code itself under Voss's own Claim 1) get cheaper as they're reused across products, but per-product requirements-definition cost does not amortize, so it becomes proportionally larger as the volume of software rises. This is a sharper, more mechanistic version of the "bottleneck shifts upstream" claim found elsewhere in the corpus (see Cross-References).

### Claim 8: The "product engineer" role is not a speculative new invention — it is the systems-analyst/product-manager function (previously split into two professions for ~25 years) recombining into one job, driven by cheap code production shortening the distance between customer insight and shipped product
- **Evidence**: Author's own historical narrative, tracing "systems analyst"
  (a 1963 Miami University memo) through Intuit/Microsoft's "program
  manager" role (Jabe Blumenthal, late 1980s, for Excel for the Mac) to the
  present.
- **Confidence**: emerging (a historical argument constructed by the author
  from named sources — a 1963 memo, a named individual and role — not
  independently verified by this Miner, but specific and falsifiable rather
  than vague)
- **Quote**: "The function moved into Product, and Product got separated from engineering as a career, and for the last twenty-five years we've had two professions where there used to be one and a half... My speculation is that it's about to collapse back into one job."
- **Our assessment**: This historical framing is genuinely novel to the corpus (no other source note traces "product manager" lineage back to a 1963 "systems analyst" memo). It reframes "product engineer" as a return to an older equilibrium rather than a genuinely new category — useful for the guide if it wants to argue this role shift is structurally durable rather than a temporary buzzword.

### Claim 9: Job postings for "forward deployed engineer"-style roles grew roughly 800% in nine months during 2025, with a census counting almost 1,000 live postings across 462 companies (including OpenAI, Anthropic, Databricks, Stripe, and Google Cloud) at average total compensation around $240,000 and senior compensation clearing $600,000 — and in these postings, code-writing is "the smallest part" of the job
- **Evidence**: Named census statistics (source/methodology not linked in
  the essay text) plus the author's own reading of job-posting
  responsibilities language.
- **Confidence**: emerging (specific, falsifiable hiring-market numbers, not
  independently verified by this Miner against a primary source, but
  directly corroborated in kind — if not in exact figures — by an
  independent corpus source; see Cross-References)
- **Quote**: "Then in 2025 postings for it grew by something like eight hundred percent in nine months, and by this month a census counted almost a thousand live postings across 462 companies, including OpenAI, Anthropic, Databricks, Stripe and Google Cloud, with Salesforce saying it wants a thousand of them to roll out its agent products. The average total comp is around $240,000 and senior ones clear $600,000, which is to say it pays like a senior engineer, because it is one."
- **Our assessment**: The compensation-parity framing ("it pays like a senior engineer, because it is one") is a sharp, quotable synthesis of the underlying claim: the market is already pricing this role at senior-engineer levels, which is itself evidence that hiring managers already believe writing code is no longer the scarce, expensive skill. The companion sentence — "The code-writing is in there, but it's the smallest part, and it's the part the agent does" — is the essay's most concrete statement of what actually differentiates the role day to day.

### Claim 10: The junior-engineer training pipeline that historically produced senior judgment ("type code somebody else reviews," repeated for a decade) is broken, because agents now do both the typing and the reviewing that used to teach that judgment — and no comparably-scaled replacement pipeline exists (Google's APM program admits ~50 people/year from ~12,000 applicants)
- **Evidence**: Author's own causal argument connecting the broken
  junior-developer ladder (from his own earlier, linked post) to a named,
  specific statistic about product-manager training-program scale.
- **Confidence**: emerging (the "loop is broken" causal claim is the
  author's own synthesis; the Google APM admission statistic is a specific,
  named, checkable figure)
- **Quote**: "That's how every senior engineer I know got their taste, and it's the loop I said in July is now broken, and it's broken because the first rung on the ladder was "type code somebody else reviews" and the agents are going to do both of those things."
- **Quote**: "Google's APM program, which Marissa Mayer started in 2002 and which is the template everyone copies, takes about fifty people a year out of something like twelve thousand applicants."
- **Our assessment**: This is the essay's most actionable claim for organizations, and it converges tightly with an existing corpus finding about *what* the broken pipeline used to transmit (see Cross-References): Voss's "taste" is functionally the same construct as Kamelman's "transmissibility," and both sources independently argue that the traditional junior-engineer ladder — not classroom training — was the delivery mechanism for it, and that mechanism is what agents have disrupted by doing both ends of the loop (writing and reviewing) themselves.

### Claim 11: Stanford Digital Economy Lab data shows the employment gap for 22-to-25-year-olds in AI-exposed jobs is now 19% below where it would be absent AI exposure, up from 15% a year earlier, driven by reduced hiring rather than layoffs — with the "codified vs. tacit knowledge" distinction explaining why young/AI-exposed workers lose ground while experienced workers in tacit-knowledge occupations gain it
- **Evidence**: Named research institution (Stanford), with a specific
  young/old comparison and a codified/tacit knowledge framework attributed
  to "the Stanford authors."
- **Confidence**: emerging (specific, named-institution statistic with a
  year-over-year comparison, consistent with — and extending — the same
  underlying research program cited elsewhere in the corpus at earlier
  snapshots; see Cross-References for the numeric progression)
- **Quote**: "The employment gap for 22-to-25-year-olds in AI-exposed jobs is now 19% below where it would be if they'd tracked their less exposed peers, up from 15% a year ago, and it's happening through reduced hiring rather than layoffs."
- **Quote**: "young workers lost ground in occupations built on knowledge that's been written down somewhere, and experienced workers gained ground in occupations built on knowledge you get by doing the job. The Stanford authors call these codified and tacit knowledge"
- **Our assessment**: The codified/tacit framing is a precise, useful vocabulary the guide could adopt: it gives a mechanistic reason (rather than just an outcome statistic) for *why* the age/seniority split in AI's labor impact exists — codified knowledge is by definition what training data contains, tacit knowledge by definition is not. This maps cleanly onto Voss's own broader thesis (Claim 6: tacit customer knowledge resists automation) applied to worker skill rather than product requirements.

### Claim 12: SignalFire's 2026 talent report found entry-level hiring at big tech companies down 65% since 2019 and down 75% at early-stage startups, while engineering's share of overall hiring simultaneously rose from 46% to 55% — meaning companies are hiring fewer people overall but a larger fraction of those they do hire are engineers, "just not the kind whose primary job is typing code"
- **Evidence**: Named research source (SignalFire's 2026 talent report),
  cited with four specific percentage figures.
- **Confidence**: emerging (specific, named-source statistics; internally
  consistent with the broader "junior pipeline collapsing while senior/
  specialized engineering demand holds or grows" pattern documented
  elsewhere in the corpus)
- **Quote**: "SignalFire's 2026 talent report has the corporate side: entry-level hiring at the big tech companies is down 65% since 2019, at early-stage startups it's down 75%, and yet engineering as a share of hiring went up, from 46% to 55%."
- **Our assessment**: The "46%→55%" figure is the more novel half of this claim for the corpus — most existing sources document the junior-hiring collapse but fewer document that engineering's *share* of hiring rose at the same time. Read together, these two facts support Voss's specific thesis (not just "AI is bad for junior hiring," but "AI is bad for junior hiring while being good for engineering-shaped hiring generally") more precisely than either figure alone.

### Claim 13: The craft of writing code as paid work is "mostly over" outside of narrowing niches — a genuine professional loss, not offset by aggregate employment statistics — but people who loved "the moment before the typing, when a vague mess of a problem resolved into a precise shape in their head" will find that moment is now the entire job, and will likely do well
- **Evidence**: Author's own stated opinion and forecast, explicitly framed
  as non-consolatory.
- **Confidence**: anecdotal (a personal, non-empirical value judgment and
  forecast about which individuals will thrive)
- **Quote**: "The craft of writing code as a thing somebody pays you to do is, I think, mostly over, outside of niches that will get narrower every year."
- **Quote**: "the part they actually loved was the moment before the typing, when a vague mess of a problem resolved into a precise shape in their head. That moment is the job now."
- **Our assessment**: This is the essay's most emotionally direct claim, and Voss is explicit that he does not intend it as reassurance ("I don't have a consolation prize"). It's useful for the guide primarily as a candid counterweight to purely economic framings elsewhere in the corpus: a structural argument for why "product engineering" is the growth path does not erase that it represents a real loss of craft-as-paid-work for people whose satisfaction was specifically in typing, not specifying.

<!-- 13 claims extracted; see Extraction Notes for why the essay's explicit
     "two assumptions" framing (agents eat the whole SDLC; software demand
     has no ceiling) was folded into Source Context/assessments rather than
     given its own claim number. -->

## Concrete Artifacts

```
Voss's four-category cost taxonomy for software development
(source: seldo.com/posts/we-are-all-product-engineers-now/,
section "The job of making software will become what the agents can't do"):

Collapsed:
  - Actually writing code

Going soon:
  - Reviewing code
  - Maintaining code (finding bugs, fixing bugs, refactoring)

Next on the chopping block:
  - Shipping code to production
  - Scaling up

Possibly safe:
  - Deciding what to build in the first place
  - Deciding the definition of "good"
  - Making it delightful
```

```
Closing summary paragraph, reproduced by Simon Willison as the full quote
on his own page (simonwillison.net/2026/Sep/14/laurie-voss/), confirmed
character-for-character by this Miner via direct curl fetch of both pages:

"The cost of writing code collapsed, and the cost of reviewing, fixing and
operating it is following, and I'm assuming it gets there. What's left of
making software is finding out what people actually want, defining it
precisely, and making it pleasant to use. That cost is per piece of
software and doesn't transfer, so as the amount of software goes to
infinity, which it will because there's no ceiling on demand, that cost
becomes the whole job."

— Laurie Voss, "We are all Product Engineers now"
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-charity-majors-code-economics.md` Claim 1 (Charity
    Majors: code generation economics "turned upside down" in 2025, from
    "very hard, time-consuming, and expensive" to "effectively free and
    instant") — two independent practitioner-analysts naming the same
    cost-collapse event for code writing specifically, corroborating this
    note's Claim 1.
  - `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claims 4–7
    (Narayanan & Kapoor's "decide-execute-deliver sandwich": AI has
    compressed only the execution middle, leaving "deciding and specifying
    what to build" and "verifying and being accountable for delivery"
    resistant for structural, not capability, reasons) — this is the
    closest independent match to this note's overall thesis. Voss's
    four-category taxonomy (Claims 1–2, 6–7) maps onto their three-layer
    sandwich: Voss's "collapsed" (writing) = their "execute"; Voss's
    "going soon/next" (reviewing, fixing, shipping, scaling) = part of
    their "deliver"/accountability layer; Voss's "possibly safe" (deciding
    what to build, defining good) = their "decide" layer. Two independent
    analyses reach structurally identical conclusions via different
    evidence bases (benchmark/hiring data for Voss; task-time-allocation
    surveys for Narayanan & Kapoor).
  - `blog-addyosmani-new-software-lifecycle.md` Claim 7 ("AI compresses the
    lifecycle... unevenly... implementation drops from weeks to hours.
    Requirements, architecture and verification stay slow, because they're
    judgment work") — the same "compression is uneven, bottleneck
    relocates rather than disappears" thesis, framed as SDLC phases rather
    than Voss's cost-category taxonomy.
  - `blog-thoughtworks-kamelman-unbundling-expertise.md` Claims 2–6 (the
    ability to "transmit a coherent internal model" to an AI, not domain
    knowledge itself, is what an Anthropic study of ~400,000 Claude Code
    sessions found actually predicts effective AI-assisted work) — Voss's
    "taste" (Claim 10) and Kamelman's "transmissibility" describe the same
    underlying construct: the skill that used to be a side effect of the
    junior-review loop and is now the scarce, unpriced-separately input.
    Kamelman's article supplies the mechanism-level study Voss's essay
    lacks; Voss supplies labor-market and training-pipeline-scale evidence
    Kamelman's article lacks.
  - `blog-latentspace-meurer-agent-engineer-fde.md` Claim 7 ("product
    engineering and forward deployed engineering are... converging, at
    least among the best people in each role") and Claim 10 ("when code
    becomes cheap to author, it also becomes easier to translate customer
    insights directly into a product") — an independent practitioner (Devi
    Meurer, on the FDE/agent-engineering side) reaches the same
    convergence conclusion as Voss's Claim 8, via the same mechanism
    (cheap code shortens the distance between customer insight and shipped
    product).
  - `blog-pragmaticengineer-ai-hiring-market-2026.md` Claim 9 (AI/ML/FDE
    roles described as a historically exceptional sellers' market, with
    unsolicited inbound and candidates rejecting offers they'd previously
    have "killed" for) and Claim 11 (a hiring manager explicitly stating
    they would rather hire for design/product taste than sophisticated
    agent tooling for a "product engineer" role) — independent, ground-
    level hiring-manager and candidate testimony corroborating both the
    hiring boom in Voss's Claim 9 and the "taste is the scarce input" claim
    in Voss's Claim 10.
  - `blog-addyosmani-earning-taste-judgment.md` Claim 4 (Indeed Hiring Lab:
    junior/standard tech postings down 34% since 2020 vs. 19% for senior
    roles; Stanford Digital Economy Lab age-cohort employment gap figure,
    revised from 13% to 16% through October 2025 per a February 2026
    follow-up) — see **Extends** below for the specific numeric
    relationship to this note's Claim 11.

- **Contradicts**: No contradiction identified rising to the MINER.md §4a
  bar. One tension worth flagging for the Assayer: this note's Claim 13
  ("the craft of writing code as paid work is mostly over... outside of
  niches that will get narrower every year") sits in some tension with
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 10
  ("software engineer employment is still growing post-ChatGPT, but the
  growth rate has slowed... relative to a no-AI counterfactual") — but
  these are not actually opposed: Voss's claim is about the *craft* of
  typing code as the differentiating, paid skill, while the
  why-ai-hasnt-replaced-engineers claim is about aggregate *employment*
  under the title "software engineer," which (per both sources) is
  increasingly defined by product/requirements work rather than typing.
  Not filed as a contradiction because both sources' own text explicitly
  reconciles this (Voss: "the industry [will be] larger than today's...
  and is mostly shaped like product engineering" — growth in headcount,
  not in the craft of typing).

- **Extends**: `blog-addyosmani-earning-taste-judgment.md` Claim 4's
  Stanford Digital Economy Lab figure (13% original → 16% per a February
  2026 follow-up, through October 2025) is extended by this note's Claim
  11 (19% now, "up from 15% a year ago," as of this essay's September 2026
  publication). Read together across three source notes, this traces the
  same ongoing Stanford tracking metric worsening over roughly a year:
  13% (original study) → ~15% (year-ago baseline implied by Voss) → 16%
  (February 2026 revision) → 19% (September 2026, per this essay). This is
  a genuine numeric progression of the same underlying research program,
  not a contradiction — flagged here so the Assayer/Smith can see the
  chain rather than treat the differing percentages as inconsistent
  reporting.

- **Novel**:
  - The historical lineage argument (Claim 8: "systems analyst" (1963) →
    "product manager" (Jabe Blumenthal, Microsoft, late 1980s) → "product
    engineer" as a recombination, not a new invention) is new to the
    corpus — no other source note traces this specific institutional
    history.
  - The "doesn't transfer" economic mechanism (Claim 7) as the specific
    reason product-definition cost doesn't shrink with scale, distinct
    from ordinary "requirements are hard" framings elsewhere in the
    corpus, is a sharper and more novel articulation of *why* this
    bottleneck is durable rather than merely currently unsolved.
  - The curl bug-bounty statistic (Claim 5: 15%→under 5% real-bug rate,
    leading to a January bounty shutdown) is a new, concrete, named
    incident not previously present in the corpus as evidence for
    AI-generated submission volume overwhelming review capacity.
  - The GitHub platform-scale review statistics (Claim 4: 58% of reviewed
    agent PRs reviewed only by another agent) are new, specific figures
    not previously in the corpus quantifying agent-reviewing-agent
    prevalence at platform scale.

## Guide Impact

- **Chapter 02 (Economics & team structure)**: Add Voss's four-category
  cost taxonomy (Concrete Artifacts, above) as a structuring device for
  discussing which parts of the SDLC are actually durable versus
  transitional — it's more actionable than a single "bottleneck shifts
  upstream" sentence because it names four distinct maturity states
  (collapsed / going soon / next / possibly safe) rather than a binary
  before/after. Pair with Claim 9's compensation data ($240k average /
  $600k senior for FDE-style "product engineer" roles) as concrete
  evidence that this shift is already being priced by the labor market,
  not just forecast.

- **Chapter 05 (Team Adoption)**: Add Claim 10 (the junior-review loop that
  used to transmit "taste" is broken because agents now do both ends of
  it) as a named risk for any team-adoption plan that assumes junior
  engineers will develop senior judgment the traditional way. Cite
  alongside `blog-thoughtworks-kamelman-unbundling-expertise.md`'s
  "transmissibility" framing and `blog-addyosmani-earning-taste-judgment.md`'s
  seven concrete practices for building taste when reps are automated —
  this essay documents *why* the problem exists at a training-pipeline-
  scale level (Google APM: ~50/12,000 applicants) that the guide currently
  lacks.

- **Chapter 06 (Product engineering as core skill)**: Add Claim 6's
  "product discovery cannot be done mechanically" argument and Claim 7's
  "doesn't transfer" economic mechanism as the sharpest available
  articulation in the corpus of *why* product/requirements skill remains
  the durable bottleneck as code generation gets cheaper — not just that
  it currently is one. Recommend citing the historical lineage (Claim 8)
  when the guide wants to argue this is a structural recombination of
  existing professions rather than a speculative new role.

## Extraction Notes

1. **Two-page source: Willison's quotation post plus the full linked
   essay.** Per MINER.md §1, this Miner followed the citation link on
   Willison's page to Voss's full essay at
   `seldo.com/posts/we-are-all-product-engineers-now/` and read it in
   full (fetched via direct `curl`, then stripped of HTML markup to
   confirm exact wording; Willison's own page was independently confirmed
   the same way). Willison's page alone reproduces only the essay's
   closing summary paragraph (Concrete Artifacts, second block); all other
   quotes in this note are drawn from the full essay, which is
   ~4,000 words (stated in the essay itself: "It's been a long 4000
   words").
2. **Several cited statistics have no named/linked primary source in the
   essay text** (Claims 2–4: the bug-fixing benchmark trend, the 567-PR
   Claude Code study, the 33,000-agent-PR study). The essay refers to
   these as "a study" or "one estimate" without naming the author,
   institution, or publication. This Miner could not independently verify
   these figures against primary sources within the scope of this
   extraction and has flagged each as `emerging` rather than `settled`
   accordingly. A future miner may wish to search for and separately mine
   the underlying studies if they can be identified.
3. **`confidence_overall` set to `emerging`**: most individual claims are
   specific, named, and falsifiable (Claims 2–5, 9, 11–12 all cite
   quantified statistics from named institutions or studies), which is
   stronger than a purely anecdotal single-author opinion piece. But this
   Miner could not independently verify most of the underlying primary
   sources (see note 2, above), and several of the essay's most central
   claims (Claims 1, 6–8, 10, 13) are the author's own analytical
   synthesis rather than externally measured findings. `emerging` reflects
   a well-evidenced, internally consistent, cross-corroborated argument
   that has not yet been independently fact-checked by this Miner against
   every cited primary source.
4. **Did not treat the essay's own stated "two assumptions" as a separate
   claim.** Voss opens by naming two explicit assumptions his forecast
   depends on (agents eventually get good at the entire SDLC, not just
   writing code; there is no upper bound on software demand). These are
   folded into the Source Context and into individual claim assessments
   (particularly Claim 7) rather than given a standalone claim number,
   since they are stated by the author as assumptions/preconditions for
   the argument rather than as claims he is asserting are independently
   true — the Assayer should weigh every other claim in this note against
   the fact that the whole essay depends on these two assumptions holding.
