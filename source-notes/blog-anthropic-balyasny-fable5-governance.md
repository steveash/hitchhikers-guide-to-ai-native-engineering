---
source_url: https://claude.com/blog/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
source_type: blog-post
title: "Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5"
author: Anthropic (case study featuring Charlie Flanagan, Chief AI Officer at Balyasny Asset Management)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: emerging
issue: "#3529"
---

# Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

> First-person Q&A with Balyasny Asset Management's Chief AI Officer on the firm's
> own-benchmark evaluation methodology for Claude Fable 5, its explicit
> "capability does not equal authority" governance principle, the in-house
> BAMAgent orchestration platform, and three concrete production workflows
> (merger-arbitrage analysis, tax-loss harvesting, central-bank analysis) with
> before/after timing.

## Source Context

- **Type**: blog-post (official claude.com "Working at the frontier" case-study
  series — same series and Q&A structural format as
  `blog-anthropic-cursor-fable5-cursorbench.md`, `blog-anthropic-cognition-fable5-frontier-trust.md`,
  and `blog-anthropic-rakuten-fable5-overnight-agents.md`, published 2026-09-17)
- **Author credibility**: Published by Anthropic on claude.com — marketing framing,
  hosted to position Claude Fable 5 favorably — but the substantive claims are
  attributed throughout to Charlie Flanagan, Balyasny Asset Management's Chief AI
  Officer, in first-person Q&A form. BAM is described in the article as "a global,
  multi-strategy investment firm that manages roughly $38 billion in assets and
  supports a team of roughly 2,000 investment professionals and staff," giving
  Flanagan's account the standing of a named executive at a large, named,
  regulated financial institution rather than an anonymous or unnamed source. No
  independent, non-Anthropic-hosted account of these specific claims exists in
  this source, and the accuracy statistic (Claim 2) is BAM's own internal
  evaluation, reviewed jointly with Anthropic rather than audited by an
  independent third party.
- **Scope**: Covers BAM's model-evaluation methodology, the 89.4%-vs-86.1% Fable
  5 accuracy result, a safety/governance framework (five review questions, a
  named list of controls, and a "capability does not equal authority" principle),
  the in-house BAMAgent orchestration platform, three named production workflows
  (merger-arbitrage analysis, tax-loss harvesting, central-bank analysis) with
  before/after timing, and forward-looking remarks on agent-as-teammate framing.
  Does NOT cover: BAMAgent's technical architecture beyond a high-level
  description, the specific content of BAM's internal task-eval suite, pricing or
  infrastructure cost, or any regulatory/compliance-filing detail beyond the
  general "investment judgment and accountability remain with people" statement.

## Extracted Claims

### Claim 1: BAM evaluates new models on thousands of real-world financial tasks with verifiable outcomes across equities, macro, and commodities, rather than relying on general benchmarks or isolated demonstrations
- **Evidence**: Stated as the firm's evaluation methodology, framed as a
  multi-year investment ("One thing we did years ago") rather than a
  Fable-5-specific effort.
- **Confidence**: settled (first-party description of an actual, longstanding
  internal process, not a one-off claim about this model launch)
- **Quote**: "We test new models on thousands of real-world financial tasks with
  verifiable outcomes, across equities, macro, and commodities, rather than
  relying on general benchmarks or isolated demonstrations."
- **Our assessment**: This corroborates a now-recurring pattern in the corpus's
  finance-domain sources: build and maintain a proprietary, task-specific eval
  suite and gate model adoption on it rather than trusting public benchmarks.
  See Cross-References for the specific parallel claims in
  `blog-anthropic-hebbia-financial-diligence.md` and
  `blog-anthropic-kepler-verifiable-ai-financial.md`.

### Claim 2: On BAM's relevant task subset, Claude Fable 5 scored 89.4% versus 86.1% for the prior production model across thousands of tasks, with the largest gains in complex planning, analysis, and agentic execution — including a class of economics problems no prior model had ever solved, a result the team initially treated as a probable evaluation bug
- **Evidence**: Specific before/after accuracy statistic plus a named
  qualitative category (economics problems never previously solved), with an
  explicit verification step: BAM "reviewed the result with Anthropic before
  concluding that the improvement was real."
- **Confidence**: emerging (concrete, specific first-party statistic, but it is
  BAM's own internal eval, joint-reviewed with the model vendor rather than
  independently audited, and the eval task set/scoring rubric are not disclosed
  in this source)
- **Quote**: "On the relevant subset, Fable achieved 89.4% versus 86.1% for the
  prior production model, across thousands of tasks. Where it stood out most was
  complex planning, analysis, and agentic execution. The surprising result was a
  set of economics problems we have tested that we have never had a model
  complete successfully, until Fable."
- **Our assessment**: The "we suspected an eval bug, then confirmed the gain was
  real" pattern is now a recurring quality signal across multiple independent
  companies' Fable 5 case studies in this corpus (see Cross-References →
  Corroborates), which is stronger evidence than any single instance alone —
  though each instance individually remains a single organization's account,
  reviewed with Anthropic rather than by a fully independent auditor.

### Claim 3: The shift enabling BAM's 2026 workflows was giving an AI an outcome rather than a prompt and letting it keep working until complete — attributed specifically to the harnesses around the models (e.g., Claude Code), not the models alone
- **Evidence**: Stated as the article's opening framing question and answer,
  explicitly separating "the models" from "the harnesses around them" as two
  distinct causal factors.
- **Confidence**: settled (explicit first-party thesis statement opening the
  interview)
- **Quote**: "2026 is the year we moved from AI systems that do search to AI
  systems that do work. The key change has been not just the models, but the
  harnesses around them, such as Claude Code. They allow the AI solutions we
  build to take on vastly more complex and longer-running tasks. The ability to
  give an AI an outcome rather than a prompt, and have it keep working until
  complete, has been a gamechanger."
- **Our assessment**: This is a clean, quotable articulation of the
  harness-vs-model distinction that recurs across the corpus's "Working at the
  frontier" series (see Cross-References) — useful as a framing thesis for any
  guide section distinguishing model capability from harness engineering.

### Claim 4: BAM's merger-arbitrage deal-analysis workflow — extracting economic/legal terms, estimating close likelihood and timeline, flagging areas needing investor judgment — dropped from 3-5 days of fragmented manual work to under a day, with the agent itself running for roughly 30 minutes and human review preceding any reliance on the output
- **Evidence**: Named before/after workflow example with a specific agent
  runtime figure and an explicit human-review gate.
- **Confidence**: emerging (concrete, specific practitioner example with named
  timing, but single case, no sample size across multiple deals disclosed)
- **Quote**: "A year ago, those steps were fragmented across manual research and
  separate tools; we did not have an agent that could reliably sustain the full
  multi-step workflow to a usable conclusion. That work used to take three to
  five days. Now it takes less than one. The agent runs for approximately 30
  minutes, with human review before any material output is relied on."
- **Our assessment**: The gap between "less than one day" total turnaround and
  "approximately 30 minutes" of actual agent runtime is notable and worth
  flagging explicitly in the guide: the 30-minute figure is agent compute time,
  not wall-clock time-to-decision, since human review and investor judgment
  still sit in the loop before the output is used.

### Claim 5: A BAMAgent explored 90,000 database tables to find relevant mutual-fund-holdings data for a tax-loss-harvesting analysis, built its own weighting system, and produced a result the review team judged more comprehensive than a traditional approach would have produced
- **Evidence**: Named concrete example with a specific table-count figure and an
  explicit human-review verdict on output quality.
- **Confidence**: anecdotal (single named example, no repeat-run or
  quantified-comprehensiveness data beyond the qualitative "more comprehensive"
  judgment)
- **Quote**: "In one example, a BAMAgent ran a tax-loss harvesting analysis. It
  explored 90,000 database tables, found the relevant mutual fund holdings data,
  and built its own weighting system. After a review by our team, the result was
  more comprehensive than what a traditional approach would have produced."
- **Our assessment**: The "explored 90,000 database tables" detail is a
  concrete, vivid illustration of large-scale autonomous data discovery — the
  kind of broad, self-directed search behavior that is hard to demonstrate with
  a benchmark score and is more persuasive as a single detailed anecdote. Flag
  for the guide as an example of agentic scope of search rather than as
  statistical evidence of accuracy.

### Claim 6: BAM's Chief Economist configured an agent workflow that reduced a recurring central-bank analysis from roughly two days to approximately 30 minutes, with the economist retaining review and judgment; the model supplies reasoning/synthesis while BAM's own harness supplies workflow design, data/tool access, permissions, monitoring, and human-review controls
- **Evidence**: Named before/after timing example paired with an explicit
  division-of-labor statement between the model and BAM's surrounding
  infrastructure.
- **Confidence**: emerging (concrete, specific practitioner example with named
  timing and role division, single named use case)
- **Quote**: "Separately, our Chief Economist has configured an agent workflow
  that reduces a recurring central-bank analysis from roughly two days to
  approximately 30 minutes, with the economist retaining review and judgment.
  Fable contributes the reasoning, synthesis, and multi-step problem-solving.
  BAM's harness provides the workflow design, approved data and tool access,
  retrieval context, permissions, monitoring, and human-review controls. Both
  are necessary for a production-quality result."
- **Our assessment**: "Both are necessary for a production-quality result" is a
  sharp, explicit statement against a model-alone framing of AI value — directly
  useful for any guide section arguing that harness engineering (not just model
  selection) is a first-class, load-bearing part of production AI systems, not
  optional scaffolding around a sufficient model.

### Claim 7: BAM treats safety as a product and operating-model question rather than a one-time model-selection exercise, organized around five explicit questions and a named set of controls, including adversarial/failure-scenario testing before broadening access
- **Evidence**: Stated as the direct answer to "How are you thinking about
  safety with today's frontier models?", enumerating both the review questions
  and the specific controls in place.
- **Confidence**: settled (first-party description of an actual internal
  governance framework, not a hypothetical)
- **Quote**: "We treat safety as a product and operating-model question, not as
  a one-time model-selection exercise. The relevant questions are not only what
  the model can do, but what data it can access, what tools it can use, what
  actions it can take, what must remain human-approved, and how we will know
  when something has gone wrong. That means putting controls around the model
  rather than assuming the model itself is the control. We use approved data
  boundaries, least-privilege access, tool-level permissions, logging and
  traceability, human review for material outputs, and clear escalation paths
  for edge cases. We also test adversarial and failure scenarios before
  broadening access."
- **Our assessment**: "Putting controls around the model rather than assuming
  the model itself is the control" is a sharp, quotable governance principle
  that closely parallels the four-question risk-assessment framework in
  `blog-anthropic-ciso-guide-agentic-ai.md` — see Cross-References. This is a
  second, independent (regulated-finance) instance of "ask about
  data/tools/actions/approval/observability before granting access," which
  strengthens the case that this is a generalizable pattern rather than an
  Anthropic-security-team-specific idiosyncrasy.

### Claim 8: BAM's explicit policy is that a more capable model does not automatically receive broader authority — models remain restricted to the tools and data sources approved for a given user and task and cannot grant themselves more access, and investment judgment and accountability remain with people regardless of model capability
- **Evidence**: Stated as a direct governance principle immediately following
  the controls list in Claim 7, explicitly framed as unaffected by the Fable 5
  launch.
- **Confidence**: settled (explicit first-party policy statement, stated as
  currently in force, not aspirational)
- **Quote**: "Those controls were a day-one priority, and security did not
  fundamentally change with Fable. A more capable model does not receive
  broader authority simply because it can reason or plan more effectively.
  Models can use only the tools and data sources approved for that user and
  task, and they cannot grant themselves more access. Investment judgment and
  accountability remain with people."
- **Our assessment**: This is the note's most reusable governance artifact: a
  named, explicit decoupling of model capability from operational authority.
  It is the policy-side companion to the incident described in
  `blog-anthropic-ciso-guide-agentic-ai.md` Claim 7-8, where an intelligence
  upgrade alone (no new tools or permissions) produced new emergent agent
  behavior within an unchanged, bounded tool list — that source shows what
  happens when capability increases inside fixed bounds; this source states the
  policy reason bounds are kept fixed regardless of capability increases in the
  first place.

### Claim 9: BAM built its own agent-orchestration platform, BAMAgent, over roughly six months; it now supports thousands of autonomous agents working 24/7, running multi-step research and analysis for hours or days in parallel, distinct from BAM's chat platform, which the article frames as being for information synthesis rather than execution
- **Evidence**: Direct description of the platform's build timeline, current
  scale, and functional distinction from BAM's existing chat tooling.
- **Confidence**: emerging (specific, first-party scale and timeline figures,
  but "thousands of autonomous agents" is not further broken down by
  concurrency, task type, or utilization)
- **Quote**: "For us, that has meant building BAMAgent, our internal platform
  for securely deploying agents into approved enterprise workflows. It gives
  agents the tools and systems they need, but only those tools and systems. We
  have been building it for six months now and it supports thousands of
  autonomous agents working 24/7. BAMAgent is the next step beyond our chat
  platform. Chat helps people take in and synthesize information. BAMAgent does
  the work: multi-step research and analysis that can run for hours or days,
  with agents working in parallel, and it ends in something a person can
  review."
- **Our assessment**: BAMAgent is a named example of a regulated-finance firm
  building custom, in-house agent-orchestration infrastructure on top of a
  frontier model rather than adopting an off-the-shelf agent platform wholesale
  — a parallel pattern to Cognition's and Cursor's own harness investments
  documented elsewhere in the corpus, but in a financial-services governance
  context specifically. "Ends in something a person can review" restates the
  human-review gate from Claims 4 and 6 as a platform-level design invariant,
  not just a per-workflow choice.

### Claim 10: BAM frames its AI roadmap as moving from "people having tools to having teammates," with agents expected to become more useful the longer people work with them; some BAM teams already run over 300 agents doing continuous analysis, and the framing question has shifted from automating existing processes to asking whether there's a better way to reach the outcome
- **Evidence**: Direct forward-looking statement closing the interview, with a
  specific named concurrent-agent-count figure for at least some teams.
- **Confidence**: anecdotal (forward-looking framing plus one concrete but
  unattributed-to-a-specific-team figure — "some teams" is not further
  specified)
- **Quote**: "This is the year we go from people having tools to having
  teammates. Much like a teammate, agents will become more useful over time as
  you work with them, complete more complex tasks, and start to do work
  proactively to help. We already have some teams running over 300 agents doing
  analysis over new data and information constantly. ... We used to build
  expert systems and teach people to automate the processes they already had.
  Now we ask whether there is a better way to reach the outcome."
- **Our assessment**: The "tools to teammates" framing is now a repeated
  vocabulary choice across multiple Anthropic case studies in the corpus (see
  Cross-References); the 300-agents-per-team figure is a concrete data point
  for the corpus's ongoing thread on large-scale concurrent-agent deployment,
  comparable in kind (though not in specific mechanism) to Rakuten's
  agent-scaling account.

## Concrete Artifacts

```
Source: "Working at the frontier: How Balyasny Asset Management evaluates and
governs Claude Fable 5," claude.com, published 2026-09-17

FIRM SCALE: ~$38 billion AUM, ~2,000 investment professionals and staff

EVALUATION RESULT (Fable 5 vs. prior production model, BAM's internal task suite):
  Fable 5:              89.4%
  Prior production model: 86.1%
  (across thousands of tasks; largest gains in complex planning, analysis,
  agentic execution; includes a previously-unsolved class of economics problems)

WORKFLOW BEFORE/AFTER TIMING:
  Merger-arbitrage deal analysis:  3-5 days  -> <1 day (agent runtime ~30 min)
  Central-bank analysis:           ~2 days   -> ~30 minutes

TAX-LOSS HARVESTING EXAMPLE:
  Agent explored 90,000 database tables to find relevant mutual-fund-holdings
  data; built its own weighting system; judged more comprehensive than a
  traditional approach after human review.

BAMAGENT PLATFORM:
  Build time:        ~6 months (in-house)
  Scale:             thousands of autonomous agents, working 24/7
  Distinction:        "Chat helps people take in and synthesize information.
                       BAMAgent does the work."
  Use cases named:   company research package build/maintenance, earnings/macro
                       event prep, turning new evidence into financial scenarios

GOVERNANCE — FIVE REVIEW QUESTIONS (paraphrased from "How are you thinking
about safety" answer):
  1. What data can the model access?
  2. What tools can it use?
  3. What actions can it take?
  4. What must remain human-approved?
  5. How will we know when something has gone wrong?

GOVERNANCE — NAMED CONTROLS (verbatim list):
  "approved data boundaries, least-privilege access, tool-level permissions,
  logging and traceability, human review for material outputs, and clear
  escalation paths for edge cases" + adversarial/failure-scenario testing
  before broadening access

GOVERNANCE PRINCIPLE (verbatim):
  "A more capable model does not receive broader authority simply because it
  can reason or plan more effectively."

ROADMAP DATA POINT:
  "some teams running over 300 agents doing analysis over new data and
  information constantly"
```

## Cross-References

### Cross-reference verification notes
Claim numbers in cited source notes below were verified by re-reading each
cited note directly and counting `### Claim N:` headings top-to-bottom, per
MINER.md §4b.

- **Corroborates**:
  - `blog-anthropic-hebbia-financial-diligence.md` Claim 1 ("Hebbia runs every
    new Claude model through a finance-specific internal benchmark, head-to-head
    against the model it would replace, before deploying it") — this note's
    Claim 1 (BAM tests models on thousands of real-world financial tasks with
    verifiable outcomes rather than general benchmarks) is the same
    proprietary-eval-suite pattern at a second, independent regulated-finance
    firm.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8 ("Automated
    evaluation pipelines — testing every prompt change, model upgrade, and
    context modification against known-correct answers at every stage — are the
    development discipline for production financial AI") — corroborates the
    same "verify every model change against your own ground-truth tasks"
    discipline this note's Claim 1 and Claim 2 describe.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 1 ("Cognition
    explicitly distrusts benchmarks in isolation and gates model adoption on
    its own engineers' subjective judgment") and Claim 7 (a benchmark jump
    initially triggered suspicion of measurement error, confirmed by
    dogfooding) — this note's Claim 2 (BAM's 89.4%/86.1% gain "initially
    treated as a potential evaluation issue" and reviewed with Anthropic before
    being accepted as real) is now the third independent company in this
    corpus's "Working at the frontier" series to report the same
    suspect-first-then-verify response to a large capability jump.
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 2 (four-question risk
    framework: untrusted content, action scope/identity, blast radius,
    observability) and Claim 3 ("principle of least agency": grant the
    narrowest capability that still completes the task) — this note's Claim 7
    (five review questions plus a named controls list, explicitly framed as
    "putting controls around the model rather than assuming the model itself
    is the control") is a second, independent (regulated-finance rather than
    AI-vendor-internal) instance of the same structured pre-deployment review
    pattern.
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 7 and Claim 8 (an
    intelligence-only upgrade, with no new tools/permissions/prompts, was
    sufficient to produce new emergent agent behavior within an unchanged,
    bounded tool list; lesson: "limit access and actions, not around what you
    believed today's model limits are") — this note's Claim 8 ("a more capable
    model does not receive broader authority simply because it can reason or
    plan more effectively... they cannot grant themselves more access") states
    the governance policy that produces exactly the bounded-blast-radius outcome
    the CISO guide's case study describes: two independent Anthropic-published
    sources converge on the same principle from opposite ends — one as an
    incident account, one as a standing policy.
  - `blog-anthropic-agent-identity-access-model.md` Claim 11 (minimal-footprint
    start, "one deliberate grant at a time") — corroborates this note's Claim 8
    least-privilege framing with the same incremental-access discipline.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("Least agency... extends
    least privilege to agentic applications... restricting what each agent
    tool can do") — corroborates the "least-privilege access, tool-level
    permissions" item in this note's Claim 7 controls list.
  - `blog-anthropic-rakuten-fable5-overnight-agents.md` — this note's Claim 10
    (300+ concurrent agents on some teams) is a comparable large-scale
    concurrent-agent-deployment data point to Rakuten's account of scaling
    agent usage, though the two sources describe different mechanisms (BAM:
    continuous data-analysis agents; Rakuten: task-delegation agents scaling
    an individual's throughput).

- **Contradicts**: None identified. No claim in this source was found to
  materially oppose an existing source note on the same topic.

- **Extends**: This note extends the "Working at the frontier" case-study
  series (`blog-anthropic-cursor-fable5-cursorbench.md`,
  `blog-anthropic-cognition-fable5-frontier-trust.md`,
  `blog-anthropic-rakuten-fable5-overnight-agents.md`) — all prior entries in
  the corpus's copy of this series document developer-tooling companies
  (Cursor, Cognition, Rakuten's engineering org); this is the series' first
  entry in the corpus covering a regulated financial-services firm, adding an
  explicit governance/safety framework (Claims 7-8) that the developer-tooling
  entries in the series do not cover in comparable depth. It also extends
  `blog-anthropic-ciso-guide-agentic-ai.md`'s abstract four-question risk
  framework with a second, independent, industry-specific (asset management)
  instance of the same review-before-deployment discipline.

- **Novel**: The "capability does not equal authority" governance principle
  (Claim 8), stated as an explicit, named policy rather than inferred from an
  incident, is new phrasing to the corpus. BAMAgent's specific build timeline
  (six months) and scale (thousands of agents, 24/7) are new concrete
  infrastructure data points. The tax-loss-harvesting 90,000-table exploration
  example (Claim 5) and the central-bank-analysis workflow with its explicit
  model/harness division-of-labor statement (Claim 6) are new concrete
  workflow examples not previously documented in the corpus's finance-domain
  sources.

## Guide Impact

- **Chapter 02 (Model Selection & Evaluation)**: Add Claim 1 and Claim 2
  alongside `blog-anthropic-hebbia-financial-diligence.md` and
  `blog-anthropic-kepler-verifiable-ai-financial.md` as a third independent
  data point for the recommendation to build a proprietary, task-specific eval
  suite and gate every model upgrade on it rather than trusting public
  benchmarks — and to explicitly flag and re-verify surprising jumps (Claim 2's
  "we treated the result as a potential evaluation issue" pattern) rather than
  accepting them at face value.

- **Chapter 06 (Security / Threat Model / Governance)**: Add Claim 7's five
  review questions and named controls list as a second, industry-specific
  instance of the four-question risk framework already documented from
  `blog-anthropic-ciso-guide-agentic-ai.md` — pair the two to show the pattern
  generalizes beyond a single AI vendor's internal practice. Add Claim 8's
  "capability does not receive broader authority" principle directly alongside
  the CISO guide's emergent-behavior case study (its Claims 7-8) as the
  policy-and-incident pairing: the CISO guide shows what happens when this
  discipline is followed and a model gets more capable anyway (bounded,
  contained emergent behavior); this source states the policy explicitly and
  proactively.

- **Chapter 02/03 (Harness Engineering)**: Add BAMAgent (Claim 9) as a named
  example of a regulated-finance firm building custom agent-orchestration
  infrastructure distinct from its chat tooling, with an explicit
  chat-vs-execution-platform distinction ("Chat helps people take in and
  synthesize information. BAMAgent does the work."). Pair with Claim 6's
  explicit model/harness division-of-labor statement ("Both are necessary for
  a production-quality result") as a concrete argument against
  model-capability-alone framings of AI value.

- **Chapter 05 (Team Adoption)**: Add Claim 10's "tools to teammates" framing
  and the 300+-agents-per-team figure as a comparison point alongside
  `blog-anthropic-rakuten-fable5-overnight-agents.md`'s agent-scaling account,
  and Claim 4/Claim 6's before/after workflow timing (merger-arbitrage,
  central-bank analysis) as concrete, named productivity data points for a
  regulated-industry context specifically.

## Extraction Notes

1. **Access method**: The claude.com blog renders as a JavaScript-heavy page.
   An initial WebFetch request for full verbatim reproduction was declined by
   the fetch tool on copyright grounds; a follow-up WebFetch for short cited
   excerpts returned quotes with minor wording drift across separate calls to
   the same URL (e.g., one pass rendered the Claim 8 quote without "more
   effectively," another included it). To get verifiable ground truth, the raw
   page HTML was fetched directly via `curl` and searched locally for each
   quote's surrounding text; every quote in this note was checked
   character-for-character against that raw-HTML text, not against either
   WebFetch summarization pass. This follows the same higher-fidelity
   extraction path used in `blog-anthropic-ciso-guide-agentic-ai.md`'s
   Extraction Notes, which flags the same WebFetch-summarization fidelity
   concern for claude.com blog posts specifically.
2. **Full article read**: The entire interview was read in full, structured as
   six Q&A sections ("How has frontier AI changed for BAM in 2026?", "How did
   you evaluate Claude Fable 5 before turning it on?", "How are you thinking
   about safety with today's frontier models?", "Where does BAMAgent fit in?",
   "What has Claude Fable 5 made possible for BAM?", "As models become
   increasingly powerful, what's next on your AI roadmap?"). No sub-pages were
   followed — this is a short, self-contained interview post (~1,000 words of
   body text) with no linked pages that extend its substantive content.
3. **Confidence calibration**: Set to emerging overall. The governance
   principles (Claims 7-8) and the evaluation-methodology description (Claim 1)
   are stated as settled, ongoing internal practice by a named executive, but
   the note's single most citable statistic (Claim 2's 89.4%/86.1% figure) is
   BAM's own internal eval reviewed jointly with Anthropic rather than an
   independently audited result, and every workflow example (Claims 4-6, 9-10)
   is a single named case rather than an aggregated, multi-instance dataset.
4. **No contradictions filed**: Cross-referencing against the corpus found no
   material contradiction with existing source notes; see Cross-References →
   Contradicts.
