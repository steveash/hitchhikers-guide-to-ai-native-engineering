---
source_url: https://martinfowler.com/rachels-ramblings/citizens-agents-experts.html
source_type: blog-post
title: "Citizens Build, Agents Execute, Experts Govern"
author: Rachel Laycock (CTO, Thoughtworks)
date_published: 2026-08-19
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: emerging
issue: "#2810"
---

# Citizens Build, Agents Execute, Experts Govern

> Thoughtworks CTO Rachel Laycock argues that the gap between "anyone can now
> build software" and "engineering teams aren't 10x faster" is conceptual, not
> technological — the industry conflated "writing software" with "software
> engineering" — and proposes a three-part model (citizens build, agents
> execute, experts govern) where expert engineers become more leveraged, not
> less necessary, as they shift from building every feature to designing the
> guardrails, platforms, and practices that let everyone else build safely at
> scale.

## Source Context

- **Type**: blog-post (personal essay column "Rachel's Ramblings" hosted on
  martinfowler.com, filed via the trusted `martin-fowler` feed; published
  2026-08-19; ~1,000-word opinion/reflection piece with a one-line TL;DR
  subtitle — "Why building an app over the weekend isn't the same as building
  enterprise software" — and no section headings, footnotes, citations, or
  embedded links to external data. It reads as a single continuous reflection,
  not a structured framework document.)
- **Author credibility**: Rachel Laycock is credited on the page itself as
  "CTO at Thoughtworks," with the column's own bio line stating she writes to
  "capture ideas before they're fully formed, challenge my own thinking and
  occasionally wander off on interesting tangents." This is an explicitly
  self-described work-in-progress reflection, not a peer-reviewed or
  data-backed report — no named study, survey, or client engagement is cited
  anywhere in the piece. The sole concrete evidence offered is one anonymized
  anecdote from an industry retreat ("FOSE"). This is her first appearance in
  this corpus.
- **Scope**: Covers the author's own recurring conversations with
  non-technical executives about why AI-assisted "weekend builds" don't
  translate into 10x faster enterprise engineering; a list of production-only
  questions (data protection, dependency failure, long-term maintainability,
  audit survival, scale, monitoring) that separate a demo from a production
  system; one retreat anecdote about a team's spec-by-day/agents-overnight/
  review-by-morning workflow; a reframing of scarcity from code-writing
  ability to engineering judgment; and the "Citizens build. Agents execute.
  Experts govern." model, explicitly clarified as being about where economic
  *value* is moving, not a fixed division of job roles. Does NOT cover: any
  named company, product, tool, metric, benchmark, or case study beyond the
  single unnamed retreat anecdote; no discussion of specific harness,
  verification, or governance tooling; no citation to external research.

## Extracted Claims

### Claim 1: The industry conflated "writing software" with "software engineering," which is why non-technical people building impressive weekend apps with AI creates a false expectation that professional engineering teams should now be delivering ten times faster
- **Evidence**: Author's own recurring conversation pattern with executives, presented as a composite/repeated scenario rather than one dated incident.
- **Confidence**: anecdotal (a generalized pattern from repeated informal conversations, not a documented survey or named set of incidents)
- **Quote**: "We've spent so many years banging on about how to write good software that everyone has assumed writing software is the same as software engineering."
- **Our assessment**: This is the article's diagnostic thesis — it locates the executive/engineer expectation gap in a category error (writing software vs. engineering software) rather than in AI capability limits or engineer resistance to change. It is a framing claim, not measured evidence, but it gives the guide a precise, quotable way to name a conversation pattern many teams likely already encounter with leadership.

### Claim 2: Software built over a weekend by a non-engineer is real, sometimes genuinely impressive software, and AI dramatically increasing the number of people who can turn ideas into working software is one of the most exciting things AI has done
- **Evidence**: Author's direct assessment, presented as a deliberate concession before pivoting to the production-readiness distinction.
- **Confidence**: anecdotal (author's own value judgment, not measured)
- **Quote**: "I don't want to diminish that because I think one of the most exciting things AI has done is dramatically increase the number of people who can turn ideas into working software."
- **Our assessment**: This concession matters for how the guide should frame the "citizens build" leg of the model — Laycock is explicit that this is not a dismissal of non-engineer-built software as fake or worthless, which shapes the tone the guide should use if it cites the framework (celebratory about access, not gatekeeping).

### Claim 3: The set of questions that separate a demo from a production system — data protection, dependency failure, long-term comprehensibility, audit survival, scale, and early problem detection — only surface once an experienced engineer is in the room, and do not show up during a weekend build or a demo
- **Evidence**: Author's own list of six illustrative questions, contrasted with her own admitted lack of these instincts when she was building her first apps.
- **Confidence**: anecdotal (an illustrative list and a personal admission, not a study of what questions actually get asked in practice)
- **Quote**: "Is customer data protected? What happens when a dependency fails? Can someone else understand this system in two years' time? Will it survive an audit? Can it cope with a thousand times more users than it has today, what about millions in one day? How will we know something is wrong before our customers do? Those questions don't show up in a demo or in the build phase at all unless an experienced engineer is in the room."
- **Our assessment**: This is the article's most concrete, checklist-like content — a specific, guide-usable list of production-readiness questions framed as the operational definition of what "software engineering" adds beyond "writing software." It is asserted rather than tested against a case where the questions were or weren't asked, but the list itself is specific enough to be directly actionable.

### Claim 4: Experienced engineers become more important, not less, as AI increases the volume of software being written — not because they remain the only people who can produce code, but because they hold the judgment needed to determine whether the resulting software can be trusted in production
- **Evidence**: Author's direct argumentative claim, following from Claim 3.
- **Confidence**: emerging (a coherent, specific reframing of engineer value — trust/judgment rather than code-production — consistent with, though not independently tested against, the author's own retreat anecdote in Claim 5)
- **Quote**: "This is where experienced engineers become more important, not less. Not because they're the only people who can build the software anymore, but because they have the judgement to know whether we can trust it: whether the design is good, the risks are understood, and the thing that works today won't become somebody else's nightmare six months from now."
- **Our assessment**: This is the article's central normative claim about engineer value and directly corroborates the "judgment over execution" convergence already present across several corpus sources from different angles (Osmani's transmissibility/taste framing, Kamelman's know/reason/transmit decomposition, Gall's "human judgment managing machine velocity") — see Cross-References.

### Claim 5: At the "FOSE" industry retreat, a team described a workflow of designing a specification during the day, letting agents work on it overnight, and reviewing the results the next morning — and what mattered to Laycock was not the overnight execution but the human activity of deciding what "good" looked like and judging whether the output matched intent
- **Evidence**: A single anonymized anecdote from an unnamed team at an unnamed retreat ("FOSE"), reported secondhand by the author without further detail on the team, company, or task.
- **Confidence**: anecdotal (one unnamed team, one unnamed event, no detail on the actual task, outcome, or whether the overnight run succeeded)
- **Quote**: "One team described spending the day designing a specification, letting agents work overnight and reviewing the results the next morning. The interesting bit for me wasn't the overnight pipeline, cool as that was. It was what the humans were doing: deciding what good looked like, making trade-offs and judging whether what came back was actually what they wanted."
- **Our assessment**: This is the article's only concrete evidentiary anchor, and it is thin — a single secondhand anecdote with no company, outcome, or verification detail. It should be cited as illustrative color for the "experts govern" leg of the model, not as demonstrated proof that spec-by-day/agents-overnight/review-by-morning is a reliable or widely adopted pattern.

### Claim 6: When agents can generate code very quickly, good design matters more, not less
- **Evidence**: Author's own generalization drawn from the FOSE retreat conversations described in Claim 5.
- **Confidence**: anecdotal (a generalization from the same single retreat anecdote in Claim 5, not independently evidenced)
- **Quote**: "We also kept coming back to good design, because it turns out that when agents can generate lots of code very quickly, good design matters more, not less."
- **Our assessment**: This is a compact, quotable counter to the intuitive-but-wrong assumption that faster code generation reduces the need for upfront design discipline. It is directly consistent with, though adds no new evidence beyond, the corpus's existing convergence on upfront specification/design mattering more as generation speed increases (see Cross-References — Corroborates).

### Claim 7: The historical scarcity the software industry optimized around was never really "people who can write code" — what is scarce now is good engineering judgment: knowing what good looks like, understanding the risks, and knowing when something that works is actually safe to trust in production
- **Evidence**: Author's own reflective reframing, presented as an open question she herself hedges ("I'm not convinced that was ever the real scarcity, but that's probably another ramble").
- **Confidence**: anecdotal (a self-hedged reflective claim, explicitly flagged by the author as underdeveloped and reserved for a future piece)
- **Quote**: "That made me wonder whether we've been thinking about scarcity in the wrong way. We've spent decades optimising around people who can write code because they were scarce and expensive. I'm not convinced that was ever the real scarcity... What feels scarce now is good engineering judgement: knowing what good looks like, understanding the risks and knowing when something that works is actually safe to trust in production."
- **Our assessment**: Should be cited as an explicitly tentative, self-acknowledged-as-underdeveloped claim rather than a settled position — the author herself flags it as something she has not fully worked out. Its value for the guide is as a provocative framing question, not as evidence.

### Claim 8: Software doesn't exist to be built — it exists to run in production and safely solve the problem it was created for; organizations run on trust, not on code
- **Evidence**: Author's closing statement of the scarcity-reframing paragraph, presented as a direct assertion.
- **Confidence**: anecdotal (a values statement, not a measured or testable claim)
- **Quote**: "Because software doesn't exist to be built. It exists to run in production and safely solve the problem it was created for."
- **Quote**: "Organisations don't run on code. They run on trust."
- **Our assessment**: This is the article's most quotable single line and functions as the value proposition underlying the entire "experts govern" argument — production fitness and trust, not code volume, are the actual unit of value. Useful as a section epigraph if the guide cites this framework, but it is an assertion, not a demonstrated finding.

### Claim 9: The "Citizens build. Agents execute. Experts govern." model is not primarily about dividing people into three fixed roles — it is about where economic value is moving: AI gives everyone a way to express ideas, agents increasingly handle execution (writing, refactoring, testing, fixing), and neither of those developments reduces the need for expertise
- **Evidence**: Author's own explicit correction of her first interpretation of her own coined phrase, presented as a reflection she arrived at only after "letting it bounce around" and testing it on trusted senior engineers at Thoughtworks.
- **Confidence**: emerging (the author explicitly revises her own initial, more literal role-based reading of the phrase into a value-flow reading — this self-correction is itself evidence the claim was deliberated, not a first-draft slogan, though it remains the author's own interpretation with no external validation)
- **Quote**: "Citizens build. Agents execute. Experts govern."
- **Quote** (the reframing): "At first I thought I was talking about roles... But I don't actually think that's what I meant. I think I was talking about where value is moving. AI has given everyone a new way to express their ideas. The execution is increasingly handled by agents... But neither of those things reduces the need for expertise."
- **Our assessment**: This is the article's headline framework and its most citable naming contribution. The explicit "not fixed roles, but where value is moving" clarification is important and easy to lose if the slogan is quoted in isolation — the guide should preserve this distinction if it cites the model, since the bare three-clause slogan alone invites a literal (and, per the author, incorrect) role-mapping reading.

### Claim 10: Experienced engineers become dramatically more leveraged, not less important, as their job shifts from building every feature themselves to designing the guardrails, platforms, engineering practices, and feedback loops that let everyone else — both non-engineers and agents — build safely at scale, because somebody still has to decide whether software deserves to exist in production (architecture, security, resilience, operability, compliance, cost)
- **Evidence**: Author's direct argumentative claim extending Claim 9.
- **Confidence**: emerging (a specific, actionable reframing of what senior-engineer leverage means under AI-assisted development, consistent with but not independently tested beyond the author's own reasoning)
- **Quote**: "Somebody still has to decide whether that software deserves to exist inside an enterprise system in PRODUCTION. Somebody still has to think about architecture. Security. Resilience. Operability. Compliance. Cost. The boring stuff that nobody gets excited about in a demo but that becomes painfully important the first time a customer can't log in or an auditor comes knocking."
- **Quote**: "I think they become dramatically more leveraged. Their job shifts from building every feature themselves to creating the environment in which thousands of features can be built safely by other people and by agents. They become the people who design the guardrails, the platforms, the engineering practices and the feedback loops that allow everyone else to move quickly without creating chaos."
- **Our assessment**: This is the article's core organizational-leverage claim and the most directly actionable content for a guide chapter on how senior engineering roles change under AI-native development — it names four concrete work products (guardrails, platforms, engineering practices, feedback loops) that constitute the "governing" leg of the model, rather than leaving "experts govern" as an abstract label.

### Claim 11: The model explicitly excludes an antipattern where non-engineers build software and simply hand it off to engineers to fix — that is not what "citizens build, agents execute, experts govern" is meant to describe
- **Evidence**: Author's explicit, direct disclaimer inserted immediately after stating the "future software organisation" vision.
- **Confidence**: anecdotal (a definitional clarification/caveat, not itself a claim requiring evidence)
- **Quote**: "And to be clear I do not mean people build stuff and throw it to engineers to fix, that is a total antipattern for another ramble."
- **Our assessment**: This is a small but important guardrail on how the guide should present the model — Laycock is explicitly pre-empting a "citizens build recklessly, experts clean up the mess" misreading. If the guide adopts this framework, it should carry this caveat forward, since without it "citizens build" could be misread as license for unreviewed handoff.

### Claim 12: Executives and engineers often sound as though they're describing completely different futures because they are looking at different parts of the same system — the executive sees that anyone can now build software, the engineer sees that somebody still has to live with what gets built — and both perspectives are correct
- **Evidence**: Author's closing synthesis, generalized from the recurring executive/engineer conversations described in Claim 1.
- **Confidence**: anecdotal (a generalized observation from repeated informal conversations, not a survey or documented set of exchanges)
- **Quote**: "The executive sees that anyone can now build software. The engineer sees that somebody still has to live with it. Both are right. They're simply looking at different parts of the same system we have to solve to create whatever the future actually ends up being."
- **Our assessment**: This closing line reframes the article's opening tension (executive asks "why aren't we 10x faster?") not as a disagreement to resolve but as two true, partial views of one system — useful as a rhetorical tool for the guide's team-adoption content when addressing skeptical or frustrated non-engineering stakeholders, since it validates the executive's observation rather than dismissing it.

## Concrete Artifacts

```
Source: Rachel Laycock, "Citizens Build, Agents Execute, Experts Govern",
martinfowler.com ("Rachel's Ramblings"), published 2026-08-19

The core slogan (Claim 9):
  "Citizens build. Agents execute. Experts govern."

The six production-readiness questions (Claim 3), as listed in the source:
  1. Is customer data protected?
  2. What happens when a dependency fails?
  3. Can someone else understand this system in two years' time?
  4. Will it survive an audit?
  5. Can it cope with a thousand times more users than it has today,
     what about millions in one day?
  6. How will we know something is wrong before our customers do?

The four named work products of a "more leveraged" senior engineer (Claim 10):
  - Guardrails
  - Platforms
  - Engineering practices
  - Feedback loops

The FOSE retreat workflow anecdote (Claim 5), as described (no company,
team, or task named):
  Day: team designs a specification
  Overnight: agents work against the specification
  Next morning: humans review the results — deciding what "good" looked
  like, making trade-offs, judging whether the output matched intent
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-kamelman-unbundling-expertise.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-addyosmani-earning-taste-judgment.md`,
`blog-thoughtworks-harmellaw-nfr-guardrail.md`,
`blog-addyosmani-new-software-lifecycle.md`, and
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` were re-read
directly (MINER.md §4b) and claim numbers below were confirmed against those
notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 2 (the "exec in the
    driving seat" dynamic: executives personally vibe-code impressive
    prototypes and draw incorrect conclusions about how easy production-ready
    systems are to build, leaving their teams to manage the gap): this is a
    near-identical scenario to this article's opening anecdote (a non-technical
    executive builds something impressive over the weekend, then asks why
    engineering teams aren't 10x faster). Both sources, independently
    published roughly six weeks apart on the same trusted Thoughtworks-affiliated
    feed, converge on naming this exact executive/engineering-team dynamic —
    Harmel-Law frames it as a governance failure (missing NFRs), Laycock frames
    it as a category-confusion failure (writing software vs. software
    engineering). The two framings are complementary diagnoses of the same
    observed pattern, not competing ones.
  - `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 6 ("Expertise
    isn't the multiplier; transmissibility is... An organization that has
    systematically rewarded execution over explicability... may find it has
    underinvested in the layer AI actually rewards") and Claim 12 ("Expertise
    isn't disappearing, but it may be getting repriced"): both corroborate
    this article's Claim 4 and Claim 10 — Kamelman and Laycock independently
    argue that AI-assisted development does not reduce the value of expert
    engineers, but reprices what part of their expertise is valuable (judgment/
    articulation over raw code-production), from different starting angles
    (Kamelman: individual skill decomposition; Laycock: organizational role
    and leverage).
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("In the middle
    loop, the human engineer evaluates whether the agent actually solved the
    right problem") and Claim 12 ("The future of software engineering isn't
    human vs. machine; it's human judgment managing machine velocity"): both
    corroborate this article's Claim 5 (the FOSE anecdote: humans deciding
    what good looks like, judging whether output matched intent) and Claim 4
    (engineers valued for judgment, not code production) — three independent
    Thoughtworks-affiliated authors converge on human judgment, not code
    authorship, as the persistent human contribution.
  - `blog-addyosmani-earning-taste-judgment.md` Claim 8 ("You, the human, own
    the outer loop of deciding whether the result is worth your attention;
    verifying that the result is worthy of approval... approving or blocking;
    carrying the consequence"): corroborates this article's Claim 5 and
    Claim 10 with a more granular, named division of responsibility (Osmani's
    inner-loop/outer-loop split) for the same underlying "humans supply
    judgment, agents supply execution" pattern this article states more
    loosely.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (every deployed agent must have a "designated principal" — a specific
    human executive legally and operationally accountable for the agent's
    outcomes; "AI cannot define its own legal and operational purpose"):
    corroborates the accountability dimension of this article's "experts
    govern" leg — both sources independently argue a named, accountable human
    layer is required above agent execution, though Gordon/Kamelman specify
    this as a legal/governance mechanism while Laycock states it as an
    organizational-leverage argument without mechanism detail.

- **Contradicts**: None identified requiring a filed contradiction issue per
  MINER.md §4a. The closest candidate tension is with
  `blog-thoughtworks-gall-supervisory-engineering.md` Claim 11 (the industry
  no longer requires syntax mastery and this shift "may particularly favor
  experienced engineers," while it's an open question whether juniors can skip
  syntax mastery to develop evaluation skill directly) — this article does not
  address junior engineers or entry-level career paths at all, so it neither
  supports nor contradicts that open question; it is silent on it, not opposed
  to it. No conditioning-variable or opposing-claim relationship was found on
  the same question.

- **Extends**:
  - `blog-addyosmani-new-software-lifecycle.md` Claim 7 ("AI compresses the
    lifecycle, but unevenly... Implementation drops from weeks to hours.
    Requirements, architecture and verification stay slow, because they're
    judgment work"): this article's Claim 10 (engineers shift from building
    features to designing guardrails/platforms/practices/feedback loops) gives
    an organizational-role vocabulary to the same underlying phenomenon Osmani
    describes as a lifecycle-phase compression pattern — where Osmani names
    *which phases* stay slow, Laycock names *what the humans in those phases
    are now responsible for producing* (guardrails and platforms, not just
    decisions).
  - `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 9 ("stop treating NFRs
    as a QA concern... specify them as entry criteria for any AI-assisted
    development initiative"): this article's Claim 3 (the six production-
    readiness questions) supplies a complementary, less formal checklist for
    the same underlying "production-readiness must be established before/
    alongside building, not after" argument — Harmel-Law's is a specific
    technical-practice checklist (NFRs as testable specs); Laycock's is a
    broader, less technical set of questions aimed at explaining the gap to
    non-engineers specifically.

- **Novel**:
  - **The "Citizens build. Agents execute. Experts govern." three-clause
    model itself** (Claim 9), including the author's explicit clarification
    that it names a shift in where value concentrates rather than a fixed
    division of job roles — no existing corpus source uses this specific
    three-part framing.
  - **The FOSE retreat spec-by-day/agents-overnight/review-by-morning
    anecdote** (Claim 5) — a new, if thin, illustrative example not present
    elsewhere in the corpus.
  - **The explicit "not a build-and-throw-to-engineers-to-fix antipattern"
    disclaimer** (Claim 11) — a specific, quotable guardrail against a likely
    misreading of role-shift models under AI-assisted development; not stated
    this way in any existing corpus source.
  - **The "executives and engineers describing different futures, both
    correct" reframe** (Claim 12) — a distinct rhetorical move for validating
    both sides of a stakeholder disagreement rather than adjudicating between
    them; not present elsewhere in the corpus in this form.

## Guide Impact

- **Chapter 00 (Principles) or Chapter 05 (Team Structure & Roles)**: Add the
  "Citizens build. Agents execute. Experts govern." model (Claim 9) as named
  vocabulary for how engineering roles reshape under AI-assisted development,
  paired explicitly with the author's own correction (this is about where
  value moves, not a literal three-way job split) and the antipattern
  disclaimer (Claim 11) — without both caveats attached, the bare slogan
  invites exactly the misreading the author warns against. Pair with
  `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 12 ("expertise...
  may be getting repriced") as a compatible framing from an independent
  author.

- **Chapter 05 (Team Adoption — Executive Expectations)**: Add Claim 1 and
  Claim 3 (the category-error diagnosis and the six production-readiness
  questions) as a specific, reusable explanation for the "why can't the whole
  team move as fast as my weekend prototype" conversation — recommend citing
  alongside `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 2's "exec in
  the driving seat" pattern, since the two sources describe the identical
  executive scenario from complementary angles (governance-gap diagnosis vs.
  category-confusion diagnosis) and together give a fuller account of both
  what's happening and why it happens.

- **Chapter 05 (Team Structure & Roles — Senior Engineer Leverage)**: Add
  Claim 10's four named work products (guardrails, platforms, engineering
  practices, feedback loops) as a concrete answer to "what does a senior
  engineer actually produce now" — currently the guide's discussion of
  engineer leverage under AI-assisted development lacks this specific a list
  of deliverables; this source's contribution is naming them, not new
  evidence that they matter (which is already established via the corpus's
  broader judgment/verification convergence).

## Extraction Notes

- **Verbatim quoting verified against raw HTML, not the WebFetch summary
  alone.** WebFetch's first pass returned what it presented as the complete
  article text; to satisfy MINER.md §2a, this was independently cross-checked
  by fetching the raw page via `curl` (browser user agent, HTTP 200),
  stripping HTML tags, and unescaping entities. Every quote used in this note
  was located and confirmed character-for-character (accounting for the
  page's typographic curly quotes/apostrophes) in that raw extraction before
  being included above.
- **The full article was read in its entirety.** It is short (~1,000 words),
  self-contained, and contains no inline links to external studies, data, or
  sub-pages — it is a personal reflective essay, not a page with substantive
  linked continuations, so no further pages were fetched per MINER.md §1.
- **Confidence rated "emerging" overall**, consistent with this corpus's
  treatment of comparable senior-practitioner framework/reflection pieces
  without supporting data (e.g. `blog-thoughtworks-gall-supervisory-engineering.md`,
  `blog-thoughtworks-kamelman-unbundling-expertise.md`, both rated
  "emerging"). Individual claims are graded lower (mostly anecdotal) since
  nearly every claim rests on the author's own composite conversations or a
  single unnamed retreat anecdote rather than named data, a study, or a
  verifiable case — but the author's seniority (Thoughtworks CTO), the
  internal coherence of the argument, and its independent convergence with
  several other corpus sources on the same underlying "judgment persists,
  code-authorship recedes" thesis justify rating the source as a whole above
  purely anecdotal.
- **No contradiction issue filed.** See Cross-References → Contradicts above
  — no opposing claim on the same question was found in the existing corpus.
- All cross-reference claim numbers cited above were verified by re-reading
  the cited notes' actual claim numbering (MINER.md §4b) before this note was
  written; none were guessed or approximated.
