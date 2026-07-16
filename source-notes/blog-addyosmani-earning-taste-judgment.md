---
source_url: https://addyosmani.com/blog/earning-judgment/
source_type: blog-post
title: "Earning taste and judgment"
author: Addy Osmani
date_published: 2026-07-14
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1925"
---

# Earning taste and judgment

> Addy Osmani argues that taste and judgment used to emerge automatically as a byproduct
> of the reps junior developers performed (boilerplate, bug fixes, problem-solving), but
> agents have now automated those reps — so junior developers must deliberately cultivate
> taste rather than absorb it passively, at the same moment entry-level tech employment is
> measurably weakening. He grounds this in labor-market data (graduate unemployment,
> job-posting trends, Stanford/Indeed/Goldman Sachs figures) and closes with seven concrete
> practices for building judgment plus four principles for where durable career value
> concentrates in an agent-saturated market.

## Source Context

- **Type**: blog-post (addyosmani.com, published July 14, 2026; ~1,900-word essay with
  embedded hyperlinked citations to primary sources — Federal Reserve Bank of New York,
  Forbes/St. Louis Fed, Indeed Hiring Lab, Stanford Digital Economy Lab, MIT Technology
  Review, World Economic Forum, Fortune/Goldman Sachs, a Wharton podcast, and links to Kent
  Beck's newsletter and an InfoQ piece on Microsoft's Mark Russinovich and Scott Hanselman)
- **Author credibility**: Addy Osmani is a Google Chrome engineering lead and the author of
  *Beyond Vibe Coding* (O'Reilly); he is an existing top-cited corpus source via the
  `addy-osmani` trusted feed, with several prior notes already in this corpus
  (`blog-addyosmani-loop-engineering.md`, `blog-addyosmani-intent-debt.md`,
  `blog-addyosmani-new-software-lifecycle.md`, `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-agentic-code-review.md`). This piece is denser with external citation
  than his typical practice-pattern posts — roughly half the essay leans on named
  third-party data sources rather than his own practitioner observation. The post ends with
  a note that "Pangram scored this article as 100% human authored."
- **Scope**: Covers labor-market data on entry-level tech employment (graduate
  unemployment/underemployment, job-posting demand shifts, age-cohort employment decline),
  a synthesis of contradictory macro-employment forecasts, a diagnosis of "cognitive
  surrender" (over-trusting AI output) backed by a cited psychology study, an
  inner-loop/outer-loop framing for human-agent responsibility division, seven concrete
  practices for building taste, three named practitioners' AI-era career advice, and four
  principles for where durable career value concentrates. Does NOT cover: specific harness
  or CLAUDE.md configuration, team-adoption rollout mechanics, or code/tooling artifacts —
  this is a career-and-labor-market essay, not a technical-practice post.

## Extracted Claims

### Claim 1: Taste and judgment used to be an automatic byproduct of the reps junior developers performed, but agents have now automated those reps, so junior developers must deliberately acquire taste rather than absorb it passively
- **Evidence**: Author's own career narrative — his stated personal experience that his taste and judgment came from "thousands of reps," contrasted with the claim that agents now automate those same reps.
- **Confidence**: anecdotal (a single practitioner's generalized career narrative, not a measured claim)
- **Quote**: "Taste used to be a byproduct of the reps. Agents took the reps. So if you're junior you now have to go get the taste (and judgment) on purpose."
- **Our assessment**: This is the essay's organizing thesis and its most portable one-line formulation. It is a framing claim rather than evidence, but it names a specific mechanism (reps → taste, now interrupted) more precisely than a generic "AI erodes junior learning" statement. Directly corroborates the "job split" thesis already documented from Kent Beck and Jessica Kerr's conversation (see Cross-References).

### Claim 2: Recent college graduates faced 5.6% unemployment and 41.5% underemployment as of March 2026, with recent graduates now more likely to be unemployed than the workforce as a whole — an inversion of the historical norm
- **Evidence**: Cited to the Federal Reserve Bank of New York's college labor market research page.
- **Confidence**: settled (a named, dated statistic from a primary government-adjacent research source)
- **Quote**: "As of March 2026, unemployment among recent college graduates sat at a staggering 5.6%, with underemployment at 41.5% - and recent graduates are now more likely to be unemployed than the workforce as a whole, an inversion of the historical norm"
- **Our assessment**: The "inversion of the historical norm" clause is the load-bearing part — this isn't just "graduate unemployment is elevated," it's that the traditional relationship (new graduates historically employed at rates comparable to or better than the general workforce) has flipped. Computer science and engineering graduates specifically show even higher elevated rates (Claim 3), meaning this is not a generic liberal-arts-major story.

### Claim 3: Recent computer-engineering graduates had a 7.5% unemployment rate and computer-science graduates 6.1%, both elevated above many non-technical majors
- **Evidence**: Cited to Forbes, itself citing the St. Louis Federal Reserve.
- **Confidence**: settled (named statistic from a cited Federal Reserve-sourced report)
- **Quote**: "recent computer-engineering graduates had an unemployment rate of 7.5% and computer-science graduates 6.1%, both elevated above many non-technical majors"
- **Our assessment**: This directly undercuts any assumption that a technical degree currently insulates new graduates from the entry-level employment weakness — CS/CE graduates are cited as doing *worse* than "many non-technical majors," which is the specific, checkable claim that makes this relevant to a software-engineering career guide rather than a general labor-market observation.

### Claim 4: Junior and standard tech job postings are down 34% since early 2020 versus 19% for senior/manager roles, while postings demanding five-plus years of experience rose from 37% to 42%, and the most AI-exposed early-career workers (ages 22-25) showed a 16% relative employment decline through October 2025 (revised up from an initial 13% estimate)
- **Evidence**: Cited to the Indeed Hiring Lab (posting-mix data) and the Stanford Digital Economy Lab (Brynjolfsson, Chandar & Chen; original study plus a February 2026 follow-up revision).
- **Confidence**: emerging (multiple independent, named, quantified sources converging on the same directional pattern, though the age-cohort figure was itself revised once already, which the author discloses rather than hides)
- **Quote**: "the Indeed Hiring Lab found junior and standard tech titles down 34% since early 2020 against just 19% for senior and manager roles, while the share of tech postings demanding five or more years of experience climbed from 37% to 42% - even as the number of computer-science graduates kept growing. The most AI-exposed early-career workers (ages 22–25) showed a 13% relative employment decline in the original Stanford Digital Economy Lab study; a February 2026 follow-up revised that to 16% through October 2025"
- **Our assessment**: Notable for its methodological transparency: the author explicitly flags that the Stanford figure was revised from 13% to 16% between studies, rather than citing only the more dramatic current number. This is stronger evidentiary practice than most single-figure labor-market claims in this corpus.

### Claim 5: Entry-level developer jobs function as training infrastructure, not just employment — Microsoft's Mark Russinovich and Scott Hanselman argue agents help senior developers while "robbing juniors of theirs and narrowing the pyramid," illustrated by a race-condition example where a senior catches an agent's sleep()-based bug fix but a junior ships it straight to production
- **Evidence**: Cited to an InfoQ report on Russinovich and Hanselman's public remarks.
- **Confidence**: emerging (a named, specific illustrative anecdote from two credible named Microsoft engineers, cited via a secondary report rather than a primary transcript)
- **Quote**: "far from taking the bread of all software developers, agents actually help senior developers while robbing juniors of theirs and narrowing the pyramid"
- **Quote (illustrative anecdote)**: "Hanselman's telling example: inserting a sleep() to paper over a race condition. The senior developer spots the error and helps you learn from it. The junior developer skips the code review, pushes it to production, and the race later crashes the site - then does it again."
- **Our assessment**: The article is careful to note the mechanism is behavioral, not purely technological: "Their real point is that the agents aren't doing this on their own; it's less an AI story than a story about how people choose to use the products." This nuance matters — it frames the risk as a process-discipline failure (skipping review) rather than an inherent agent limitation, which is consistent with this corpus's broader verification-before-autonomy theme (see Cross-References).

### Claim 6: Two seemingly contradictory macro-employment forecasts are both true simultaneously — the World Economic Forum projects a net gain of 78 million jobs by 2030 (170 million created vs. 92 million displaced), while Goldman Sachs estimated roughly 16,000 net US job losses per month in 2026 with Gen Z and entry-level roles hit hardest — because "the net and the entry level are two different questions"
- **Evidence**: Cited to the WEF's Future of Jobs 2025 report (published January 2025) and a Fortune report on Goldman Sachs' 2026 payroll analysis.
- **Confidence**: emerging (both cited figures are from named, credible institutional sources; the reconciliation ["both true at once"] is the author's own analytical synthesis)
- **Quote**: "The World Economic Forum's Future of Jobs 2025, published in January 2025, projects that by 2030 some 170 million new roles will emerge against just 92 million displaced - a net gain of 78 million."
- **Quote**: "Goldman Sachs, looking at 2026 payrolls, estimated a net loss of about 16,000 US jobs a month with Gen Z and entry-level roles hit hardest - the empirical answer to 'zero evidence.'"
- **Quote**: "Aggregate growth and a vanishing first rung are both true at once - and if you're the one trying to climb onto that rung, the net number is cold comfort."
- **Our assessment**: This reconciliation is the essay's most useful analytical move for a guide audience: it explicitly refuses to pick one narrative (optimistic aggregate vs. pessimistic entry-level) and instead names the exact axis along which both can be simultaneously accurate. This is consistent with, and adds sharper numbers to, the same "aggregate demand stable, individual careers rocky" distinction already documented in `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` (see Cross-References).

### Claim 7: A cited psychology study found that people accept incorrect AI output roughly 80% of the time, with accuracy dropping about 15 points below the no-AI baseline while confidence in their own answers rose about 12%, illustrating a "cognitive surrender" debt the article says engineers now owe alongside genuine comprehension
- **Evidence**: Cited to a Wharton Knowledge podcast episode featuring Gideon Nave and Steven Shaw, describing a study surveying 1,372 participants over roughly 10,000 trials.
- **Confidence**: emerging (a named academic study with a specific participant count and trial count, cited via a secondary podcast reference rather than the primary paper)
- **Quote**: "Shaw and Nave surveyed 1,372 participants over ~10,000 trials and found that they tended to accept incorrect AI output nearly 80% of the time. Their accuracy dropped ~15 points below the no-AI baseline, while confidence rose ~12%."
- **Our assessment**: The confidence-rising-while-accuracy-falls pairing is the most guide-relevant part of this claim — it describes a specific, measurable failure mode (rising unwarranted confidence alongside declining accuracy) rather than a vague "people over-trust AI" warning. This is a concrete empirical anchor for any guide section on why verification discipline can't be assumed to emerge naturally from experience with a tool.

### Claim 8: The human's role in agent-driven work is to own an "outer loop" — deciding whether a result deserves attention, verifying it against diffs/test results/logs, approving or blocking, and carrying the consequence — while the agent's "inner loop" cycles through investigate, implement, test, and report
- **Evidence**: Author's own framing, presented as a distillation of his own operating principle ("my psalm").
- **Confidence**: emerging (a named framework from a credible practitioner-author, not independently measured, but a specific and actionable division of responsibility)
- **Quote**: "The agent runs a loop of activities (investigate, implement, test, report)."
- **Quote**: "You, the human, own the outer loop of deciding whether the result is worth your attention; verifying that the result is worthy of approval (diffs, test results, logs, and a short why); approving or blocking; carrying the consequence. The boundary is evidence (my psalm)."
- **Our assessment**: "The boundary is evidence" is a sharp, quotable rule: the outer-loop/inner-loop split isn't drawn by task type or seniority, it's drawn by who supplies and checks evidence for the result. This gives the guide a compact test for where human review must sit in any agent workflow — the human's job is specifically to demand and evaluate evidence, not merely to "review the code."

### Claim 9: Seven concrete practices build taste and judgment when reps are automated: read far more code than you generate; keep a "wrong log" of agent mistakes; do some things manually on purpose to protect fundamentals; go deep on one system end-to-end; learn to specify and verify separately; build a rubric-based eval against real AI-generated pull requests; and calibrate autonomy per task by cost and reversibility
- **Evidence**: Author's own prescriptive list, presented as concrete practices following the diagnostic sections of the essay.
- **Confidence**: anecdotal (prescriptive practitioner advice, not validated against outcome data)
- **Quote**: "Read far more code than you generate. Hunt for logic errors, security holes, simple or subtle edge cases. On a regular basis, ask yourself about the code you read: Did I consider the right things?"
- **Quote**: "Keep a wrong log. Every mistake an agent makes gets one sentence. After thirty days you get a sense of patterns."
- **Quote**: "Calibrate autonomy per task. Turn it way up on cheap, reversible tasks. Down on expensive failures. Learning to calibrate is a senior developer instinct worth exercising daily."
- **Our assessment**: These are specific enough to be directly actionable (a "wrong log," a 50-PR rubric eval, an explicit cost/reversibility autonomy dial) rather than generic "practice good judgment" advice. The "specify and verify separately" practice ("Spec-writing is clear thinking. Verification is evidence. Specification quality is the biggest lever.") is the most guide-relevant single practice, since it names specification quality as "the biggest lever" — consistent with, and a practitioner-actionable instantiation of, the "decide-execute-deliver sandwich" model's finding that the deciding layer is where engineering time and risk concentrate (see Cross-References).

### Claim 10: Claude Code's Boris Cherny states engineers still need to know the craft underlying software engineering — languages, compilers, runtimes, system design — and his "coding is largely solved" remark describes his own productive workflow, not a license to skip fundamentals
- **Evidence**: A quote attributed to Boris Cherny via a linked article (rogerwong.me), with the author's own gloss distinguishing Cherny's personal-workflow claim from a general "fundamentals no longer matter" claim.
- **Confidence**: anecdotal (a single named practitioner's public statement, relayed via a secondary source, with the essay author's own interpretive gloss attached)
- **Quote**: "People are still going to need to know the craft underlying software engineering, including languages, compilers, runtimes, and system design"
- **Our assessment**: The gloss matters more than the quote itself here: the author is pre-empting a likely misreading of Cherny's separately-known "coding is largely solved" line by explicitly distinguishing "this is the workflow I personally find productive" from "fundamentals no longer matter." This is a useful corrective for any guide section that might otherwise cite "coding is solved" out of context as license to skip underlying systems knowledge.

### Claim 11: Anthropic's own internal report states its engineers only use AI to help when they already know the answer, warning of a "paradox of supervision" — that supervising an agent requires exactly the skills that atrophy when you over-rely on the agent
- **Evidence**: Cited to "A report from Anthropic" — the essay's link resolves to Anthropic's "How AI Is Transforming Work at Anthropic" research report, which this corpus already has a source note for.
- **Confidence**: emerging (directly sourced from a mixed-methods internal study already documented elsewhere in this corpus at higher extraction depth)
- **Quote**: "Beware the paradox of supervision."
- **Quote**: "A report from Anthropic says they only use AI to help when they already know the answer, and warn that supervising an agent requires exactly the skills that atrophy when you over-rely on one."
- **Our assessment**: This paraphrases, rather than directly quotes, the underlying Anthropic report. The report itself (`research-anthropic-ai-transforming-work.md` Claim 8) documents the same underlying concern via direct interview quotes from Anthropic engineers ("When producing output is so easy and fast, it gets harder to actually take time to learn something") — this essay's "paradox of supervision" phrase is Osmani's own naming of that finding, not a phrase used in the original report. Treat the naming as Osmani's framing, and the underlying finding as sourced to the Anthropic report directly (see Cross-References).

## Concrete Artifacts

### The seven taste-building practices (verbatim from the article)

```
Source: Addy Osmani, "Earning taste and judgment", addyosmani.com, 2026-07-14

- Read far more code than you generate. Hunt for logic errors, security holes,
  simple or subtle edge cases. On a regular basis, ask yourself about the code
  you read: Did I consider the right things?
- Keep a wrong log. Every mistake an agent makes gets one sentence. After
  thirty days you get a sense of patterns.
- Do a few things the hard way on purpose. Build a parser manually, or a CRM,
  or something meaningful from scratch. Protect your collateral learning.
  Karpathy emphasizes fundamentals like memory, views (how the world appears
  to the system), and storage that agents get wrong.
- Go deep on one system end to end. Push it all the way to failure. Then
  learn what real depth feels like.
- Learn to specify and verify separately. Spec-writing is clear thinking.
  Verification is evidence. Specification quality is the biggest lever.
- Build an eval, a test framework around a rubric of correctness,
  maintainability, efficiency, security, style. Run it on fifty real PRs
  generated by AI agents. Note surprising test failures and fixes. Calibrate
  to make your internal quality function explicit.
- Calibrate autonomy per task. Turn it way up on cheap, reversible tasks.
  Down on expensive failures. Learning to calibrate is a senior developer
  instinct worth exercising daily.
```

### The four principles of durable value (verbatim from the article)

```
Source: Addy Osmani, "Earning taste and judgment", addyosmani.com, 2026-07-14

1. Finish the last mile. Automation covers the easy 80-90% of software
   engineering. The last mile - edge cases, architecture, taste - is the
   whole game. As first drafts become free, the finish is the product, and
   it's where people distinguish themselves.
2. Solve the hard version. Richard Sutton's famed bitter lesson of the last
   three decades is not just career advice: The easy version is already
   solved; durable value comes from solving the hard one.
3. Build in public near hard problems. [...] Think of it like expected goals
   in soccer: your reputation and public work decide how many chances you get
   in front of goal, and judgment is whether you convert them. [...] almost
   every real opportunity I've had came from work I did in public, never from
   a job I applied for.
4. Be a T-shaped generalist. Developers with the deepest knowledge in one or
   two areas while maintaining broad literacy tend to deliver the best
   results. A good dose of AI assistance means developers will be able to
   accomplish more as single contributors working on fewer different areas
   than they could before.
```

### Closing thesis (verbatim from the article)

```
Source: Addy Osmani, "Earning taste and judgment", addyosmani.com, 2026-07-14

"To put it plainly: the world isn't short on opportunity; it's short on
people who can find the right problem, tell whether the machine solved it,
and finish past where the machine stopped."

"Anything gradeable by someone else is getting automated."

"The career is the ungradeable part: choosing what matters, judging honestly
when you've got it, and answering for it. Do that. In public. Near the hard
problems. The rest tends to follow."
```

## Cross-References

- **Corroborates**:
  - `blog-kentbeck-jessicakerr-learning-system.md` Claim 1 ("AI didn't eliminate the
    programmer's job, it split it in two — hand-crafted code-writing is commoditized...
    while understanding what to build, proving it works, and stewarding the... system is
    the harder, more human remainder"): this source's Claim 1 (taste no longer a byproduct
    of automated reps) and Claim 8 (the human's outer-loop role: deciding, verifying,
    approving, carrying consequence) independently arrive at the same "durable value moved
    to judgment/verification, not code-crafting" conclusion from a career-advice angle
    rather than a conversational one.
  - `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 1 (Kent Beck: coding is only a
    small, and shrinking, part of the job — durable value is confidence-building, human
    connection, domain understanding) and Claim 11 (Beck's "cosmic, practical joke": success
    is gated by human skills, not computer skills): this source's four durable-value
    principles (Claim 9's list plus the "ungradeable career" closing) restate the same
    "coding recedes, judgment/human skill persists" thesis with concrete practices attached,
    rather than as autobiography.
  - `research-anthropic-ai-transforming-work.md` Claim 8 (Anthropic engineers report skill
    atrophy and supervision-paradox concerns in their own words: "When producing output is
    so easy and fast, it gets harder to actually take time to learn something"): this
    source's Claim 11 cites the same underlying Anthropic report and names the same finding
    "the paradox of supervision" — Osmani's phrase is his own naming of the report's
    finding, not a quote from the report itself; see Claim 11's assessment for the
    distinction.
  - `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 10 (software engineer
    employment still growing but slowed ~3pp/year vs. counterfactual) and Claim 11
    (aggregate labor demand likely remains healthy even as individual careers get rockier):
    this source's Claim 6 (WEF's optimistic net-78-million forecast vs. Goldman Sachs'
    pessimistic entry-level-focused monthly loss estimate, "both true at once") is a second,
    independent source making the identical aggregate-vs-individual distinction with
    different named data (WEF/Goldman here vs. Federal Reserve/WARN Act there).

- **Extends**: `blog-pragmaticengineer-ai-hiring-market-2026.md` Claim 11 (a Los Angeles
  tech lead: "I'd rather hire someone who is 'behind' on AI, but has great taste/judgment
  than someone with complex agent setups and prompt libraries") — that note documents one
  hiring manager's stated preference for taste over demonstrated AI-tooling sophistication;
  this source supplies the labor-market data (Claims 2-4) and the prescriptive practices
  (Claim 9) that would explain *why* that preference exists and *how* an engineer could
  actually go about building the taste that hiring manager says he values.

- **Novel**:
  - The specific March 2026 graduate unemployment/underemployment figures (5.6% / 41.5%
    overall, 6.1% / 7.5% for CS/CE graduates specifically) and the Indeed Hiring Lab
    posting-mix data (34% vs. 19% decline, 37%→42% experience-requirement shift) — not
    present in any existing corpus source note.
  - The Russinovich/Hanselman "narrowing the pyramid" framing and the specific
    sleep()-race-condition illustrative anecdote of a senior catching an agent's bug versus
    a junior shipping it straight to production — new to the corpus.
  - The WEF Future of Jobs 2025 (170M created / 92M displaced / net +78M) figure paired
    explicitly against the Goldman Sachs 16,000/month 2026 net-loss estimate as two
    simultaneously-true framings of the same labor market — the specific pairing and the
    "net and entry level are two different questions" reconciliation is new to the corpus.
  - The Shaw & Nave cognitive-surrender study (1,372 participants, ~10,000 trials, ~80%
    acceptance of incorrect AI output, ~15-point accuracy drop, ~12-point confidence rise) —
    not present elsewhere in the corpus; this is a specific, quantified empirical anchor for
    over-trust-in-AI-output risk.
  - The "inner loop / outer loop" framing for agent-vs-human responsibility (agent:
    investigate/implement/test/report; human: decide/verify/approve-or-block/carry
    consequence), explicitly anchored on evidence as the boundary condition — a distinct
    naming from this corpus's other loop taxonomies (e.g. `blog-thoughtworks-gall-
    supervisory-engineering.md`'s inner/middle/outer-loop framing, which divides by pipeline
    stage rather than by who owns evidence-based approval).
  - The seven concrete taste-building practices (wrong log, manual-build-on-purpose,
    fifty-PR rubric eval, cost/reversibility autonomy calibration) as a named, ordered list —
    new to the corpus as a single practitioner checklist, though individual elements echo
    scattered guidance elsewhere (e.g. this corpus's existing verification-discipline and
    spec-quality themes).
  - Richard Sutton's "bitter lesson" applied explicitly to individual career strategy
    ("durable value comes from solving the hard [version], not the easy one") rather than
    to ML research methodology (its original context) — a novel application of an existing
    concept to this corpus's career-guidance material.

- **Contradicts**: None found requiring a filed contradiction issue per MINER.md §4a. One
  soft tension worth flagging for the Smith's awareness without escalating: this source's
  Claim 1 treats the loss of automatic, reps-derived taste-building as a straightforwardly
  bad outcome requiring deliberate compensation, while `blog-thoughtworks-gall-supervisory-
  engineering.md` Claim 11 raises (as an explicitly unresolved, self-hedged question) whether
  junior engineers might productively skip traditional syntax-mastery reps entirely and
  develop evaluation skill directly. The two are not in direct opposition — this source
  argues taste must still be earned through some deliberate practice (just not the old
  reps-based path), while the Gall piece speculates junior evaluation skill might not need
  the old reps-based path *at all* — but both address the same open question (how do juniors
  build judgment once reps are automated) with different degrees of optimism about shortcuts,
  and neither source treats its own position as settled.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the "inner loop / outer loop" framing (Claim 8) as a
  concrete rule for where human review must sit in any agent-assisted workflow: the human's
  job is specifically to supply and evaluate evidence (diffs, test results, logs) before
  approving, not merely to "look over" agent output. Pair with the seven practices (Claim 9)
  as a named checklist practitioners can adopt directly, particularly "keep a wrong log" and
  "calibrate autonomy per task," which are concrete enough to become guide-recommended habits
  rather than abstract advice.

- **Chapter 03 (Verification)**: Cite the Shaw & Nave cognitive-surrender statistics (Claim
  7 — ~80% acceptance of incorrect AI output, ~15-point accuracy drop, ~12-point confidence
  rise) as the empirical justification for why verification discipline requires deliberate
  practice and cannot be assumed to emerge naturally from tool familiarity. Currently the
  guide's verification sections lack a quantified psychological mechanism for *why*
  engineers under-scrutinize AI output; this fills that gap.

- **Chapter 05 (Team Adoption / Hiring, or a new career-guidance section)**: The labor-market
  data (Claims 2-6) should ground any guide discussion of the entry-level pipeline with
  current (March 2026-dated), multiply-sourced figures rather than an impressionistic "junior
  hiring is harder now" statement. Recommend pairing the WEF-vs-Goldman reconciliation (Claim
  6) explicitly, so the guide neither over-claims mass displacement nor dismisses the
  entry-level-specific weakening as noise. The Russinovich/Hanselman "narrowing the pyramid"
  anecdote (Claim 5) is a concrete, quotable illustration for why teams should treat junior
  code review as a training obligation, not just a quality gate.

- **Chapter 00 (Principles) or Chapter 05**: The four durable-value principles (Claim 9's
  companion "Concrete Artifacts" list — finish the last mile, solve the hard version, build
  in public near hard problems, be T-shaped) give the guide a structured, named framework for
  career-positioning advice under AI-native conditions, complementing the more autobiographical
  Kent Beck material already in the corpus with a more prescriptive, checklist-style
  companion.

## Extraction Notes

- WebFetch's summarizing model produced a paraphrased digest on first pass rather than the
  article's literal text (its own output described "concerning trend" and other clearly
  summarized language, and merged the "13% original / 16% revised" Stanford figures into a
  single "16%" number). Per MINER.md §2a, that summarized pass was not used as a quote
  source. The raw HTML was fetched directly via `curl` with a browser user agent, and the
  article body was located in the page's `<section id="post-body">` element; every quote in
  this note was copied verbatim from that raw HTML, not from the WebFetch summary.
- The article's full text was read in its entirety (it is a single page with no
  linked sub-pages presented as substantive continuations — its outbound links are all to
  external primary sources for citations, which is why this note treats those citations as
  Osmani's evidence rather than as separate "linked pages" to independently mine). Two of
  the cited external sources (the Anthropic "How AI Is Transforming Work" report and the
  general "job split" thesis) are already independently mined in this corpus at greater
  depth; this note cites them rather than re-extracting them.
- The article links to a prior Pragmatic Engineer piece ("TDD, AI agents and coding with
  Kent Beck") for Kent Beck's claim that "it's unlikely AI agents will ever possess taste, by
  which he means judgment" — that specific episode is referenced but not yet present as its
  own source note in this corpus (the existing `blog-pragmaticengineer-orosz-kentbeck-
  career.md` note explicitly documents that it did *not* fetch or extract that separate,
  earlier episode). This note therefore does not cite a claim number for that Kent Beck
  reference, since doing so would require fabricating a citation to an unextracted source;
  if that episode is separately submitted and mined, it should cross-reference this note.
- Cross-references verified before writing: `blog-kentbeck-jessicakerr-learning-system.md`
  Claim 1 (confirmed at that note's Claim 1 heading); `blog-pragmaticengineer-orosz-kentbeck-
  career.md` Claim 1 and Claim 11 (both confirmed); `research-anthropic-ai-transforming-
  work.md` Claim 8 (confirmed — the skill-atrophy/supervision-paradox interview quotes);
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 10 and Claim 11 (both
  confirmed); `blog-pragmaticengineer-ai-hiring-market-2026.md` Claim 11 (confirmed — the LA
  tech lead's taste-over-tooling hiring preference); `blog-thoughtworks-gall-supervisory-
  engineering.md` Claim 11 (confirmed — the open question on juniors bypassing syntax
  mastery).
- No contradiction issue filed — see Cross-References/Contradicts above for the reasoning
  (an open, self-hedged question in both sources, not a material contradiction).
