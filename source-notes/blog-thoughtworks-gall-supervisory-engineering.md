---
source_url: https://www.thoughtworks.com/insights/blog/agile-engineering-practices/supervisory-engineering-orchestrating-software-middle-loop
source_type: blog-post
title: "Supervisory engineering: Orchestrating software's 'middle loop'"
author: Richard Gall
date_published: 2026-06-03
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1422"
---

# Supervisory Engineering: Orchestrating Software's 'Middle Loop'

> Thoughtworks argues that AI coding agents have inserted a new architectural
> layer between the traditional inner loop (writing code in the IDE) and outer
> loop (CI/CD and deployment) — the "middle loop" — and proposes "supervisory
> engineering," organized around three pillars (directing, evaluating,
> correcting), as the discipline for working in it.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published 2026-06-03; conceptual/
  framework-style essay, not a case study or empirical report; five H2 sections:
  "Supervisory engineering" (intro), "What is the 'middle loop'?", "The middle
  loop in practice: Supervisory engineering" (with four H3 subsections —
  "Aligning intent and setting constrains", "Multi-agent synthesis",
  "Differential and behavioral review", "Gatekeeping and guardrails"), "The
  three pillars of supervisory engineering", and "The skill that scales")
- **Author credibility**: Richard Gall, published under Thoughtworks Insights
  (Thoughtworks is a well-known vendor-neutral software consultancy; this blog
  is a designated `trusted-feed` source in this repo per the Prospector's
  triage). The page gives no further bio for Gall beyond a profile link — no
  title, no stated hands-on agent-orchestration experience is cited in the
  article itself. The piece reads as editorial/conceptual synthesis rather
  than first-person practitioner reporting: it contains no named companies,
  no case studies, no metrics, and no code or config artifacts.
- **Scope**: Covers a conceptual reframing of the software development loop
  (inner/outer → inner/middle/outer) and a taxonomy of supervisory activities
  (four practical areas, restated as three "pillars"). Does NOT cover: specific
  tooling, named orchestration frameworks, CLAUDE.md/AGENTS.md-style
  configuration, quantitative outcomes, or any concrete engineering
  organization's experience implementing this. It is a thought-leadership
  framing piece, not a report of applied practice.

## Extracted Claims

### Claim 1: The traditional software development mental model had two loops — an inner loop (IDE-level coding) and an outer loop (post-push CI/CD and deployment) — and AI coding agents have broken that two-loop model by inserting a new layer between them
- **Evidence**: Author's conceptual argument; no external citation or data.
- **Confidence**: emerging (novel framing, no empirical backing, but a plausible
  and well-articulated restructuring of a widely-used mental model)
- **Quote**: "This change is nothing less than a brand-new layer in software development: the middle loop."
- **Our assessment**: This is the article's foundational move and its main
  novel contribution to our corpus: no existing source note names an
  "inner/middle/outer loop" taxonomy. It is a naming/framing claim, not an
  empirical one — its value is as vocabulary, not evidence.

### Claim 2: In the middle loop, the human engineer's job is to evaluate whether the agent actually solved the right problem, not to write the code
- **Evidence**: Author's conceptual argument extending Claim 1.
- **Confidence**: emerging
- **Quote**: "In the middle loop, the human engineer evaluates whether the agent actually solved the right problem."
- **Our assessment**: This is the definitional core of "supervisory
  engineering" — evaluation-of-output replaces authorship-of-code as the
  primary human activity at this layer. It is consistent with, and gives a
  name to, the general "review > write" shift already present piecemeal in
  our corpus (see Cross-References).

### Claim 3: Supervisory engineering requires aligning intent and setting constraints before an agent builds — breaking a system down into "agent-sized" chunks, managing context windows, and codifying engineering standards explicitly so the agent doesn't invent its own design patterns
- **Evidence**: Author's conceptual argument (H3: "Aligning intent and setting
  constrains").
- **Confidence**: emerging
- **Quote**: "Prompting an agent to build something is easy; getting it to build the right thing in the right way is another matter"
- **Our assessment**: This restates, under new vocabulary ("aligning intent
  and setting constraints"), a practice this corpus already documents at the
  concrete level — decomposing work into agent-sized tasks and codifying
  standards in CLAUDE.md/AGENTS.md-style configuration. The value-add here is
  framing it as a distinct upstream *pillar* of a supervisory discipline
  rather than a one-off harness-configuration tip.

### Claim 4: Modern AI workflows increasingly involve multiple agents working in parallel, and the middle loop is where the engineer must synthesize these parallel work streams into a coherent system
- **Evidence**: Author's conceptual argument (H3: "Multi-agent synthesis").
- **Confidence**: emerging
- **Quote**: "The middle loop is where the engineer must synthesize these parallel work streams."
- **Our assessment**: Directly corroborates the orchestrator-subagent pattern
  already documented with concrete practitioner detail in
  `blog-anthropic-vlasenko-pm-agent-orchestration.md` (Claim 2: 15+ named
  parallel subagents) and `blog-anthropic-multi-agent-coordination-patterns.md`.
  This article adds no new mechanism, but frames "stitching together
  parallel-agent output" as a named supervisory responsibility rather than an
  incidental orchestration detail.

### Claim 5: Code review in the middle loop shifts from checking *how* the code was written to verifying *what* the code does — differential and behavioral review rather than style/authorship review
- **Evidence**: Author's conceptual argument (H3: "Differential and behavioral
  review").
- **Confidence**: emerging
- **Quote**: "Your review shifts from checking how the code was written to verifying what the code does."
- **Our assessment**: This is a specific, actionable reframing of code review
  practice for agent-generated code, distinct from human-authored-PR review.
  It implies reviewers should prioritize behavioral/differential testing
  (does the diff change observable behavior correctly?) over line-by-line
  style review — relevant to Ch03 (Verification), which already covers
  automated verification but not this specific human-review posture shift.

### Claim 6: The middle loop should function as a filter/gate that machine-generated code must pass before it reaches the CI/CD pipeline
- **Evidence**: Author's conceptual argument (H3: "Gatekeeping and
  guardrails").
- **Confidence**: emerging
- **Quote**: "The middle loop should be treated as a kind of filter stage, one that needs to be passed before anything touches your CI/CD pipeline."
- **Our assessment**: This positions supervisory review as a required gate
  rather than an optional or parallel activity, ahead of automated CI/CD
  checks — an architectural point about *where* human judgment should sit
  in the pipeline, not just *that* it should exist somewhere.

### Claim 7: Supervisory engineering can be understood through three pillars: directing, evaluating, and correcting
- **Evidence**: Author's conceptual argument (H2: "The three pillars of
  supervisory engineering") — presented as "another way to understand"
  the same practices described in Claims 3-6, not as new content.
- **Confidence**: emerging
- **Quote**: "Another way to understand supervisory engineering is through the prism of three key pillars: directing, evaluating and correcting."
- **Our assessment**: This is a restatement/relabeling of the four practical
  areas above (Claims 3-6) into a three-part rhetorical frame, not an
  independently evidenced taxonomy. Useful as a mnemonic for the guide, but
  should be cited as framing, not as a validated model.

### Claim 8: "Directing" means breaking a large system architecture into agent-sized chunks, managing context windows, and explicitly codifying engineering standards so an agent doesn't invent its own design patterns
- **Evidence**: Author's conceptual argument (pillar 1 of 3).
- **Confidence**: emerging
- **Quote**: "It involves breaking a massive system architecture down into 'agent-sized' chunks, managing context windows and explicitly codifying engineering standards so an agent doesn't hallucinate its own design patterns."
- **Our assessment**: "Hallucinate its own design patterns" is a memorable,
  specific failure mode — an agent inventing architectural conventions absent
  explicit constraints. This corroborates the guide's existing emphasis
  (guide/02-harness-engineering.md, "What to Put in CLAUDE.md") on codifying
  engineering standards explicitly rather than assuming an agent will infer
  house style.

### Claim 9: "Evaluating" requires deep system context to look at plausible, well-formatted agent-generated code and judge whether it actually handles real-world conditions (e.g., edge cases under load) — not just whether it looks correct
- **Evidence**: Author's conceptual argument (pillar 2 of 3).
- **Confidence**: emerging
- **Quote**: "It requires deep system context to read highly plausible, beautifully indented code and instantly ask: 'Did this catch the edge cases under heavy load?'"
- **Our assessment**: This names a specific risk already implicit in this
  corpus's verification discussions: LLM-generated code is often
  syntactically clean and "plausible-looking," which can lull reviewers into
  under-scrutinizing it. The claim that this evaluation requires "deep system
  context" is an argument for experienced-engineer involvement at this
  pillar specifically (see Claim 11 tension below).

### Claim 10: "Correcting" means stitching together codebases generated by multiple agents working in parallel, maintaining architectural coherence and ensuring the systems mesh seamlessly
- **Evidence**: Author's conceptual argument (pillar 3 of 3).
- **Confidence**: emerging
- **Quote**: "Stitching together three different codebases generated by three different agents working in parallel, maintaining architectural coherence and ensuring the systems mesh seamlessly."
- **Our assessment**: This is the same underlying activity as Claim 4
  ("Multi-agent synthesis") restated as a pillar — the article uses two
  different vocabularies (four practical areas vs. three pillars) to describe
  overlapping ground, and this is the clearest case of duplication between
  the two framings.

### Claim 11: The industry no longer requires engineers to be syntax experts; instead it now values strong mental models of system architecture, an intuitive grasp of real-world software behavior, and the ability to coordinate complex work rather than manually code it — and this shift may particularly favor experienced engineers, while it is an open question whether junior engineers can skip traditional syntax mastery to develop evaluation skill directly
- **Evidence**: Author's conceptual argument (H2: "The skill that scales").
  No data, survey, or named examples are given for either the "favors
  experienced engineers" claim or the "open question" about juniors.
- **Confidence**: anecdotal (pure editorial speculation, explicitly hedged by
  the author as unresolved for juniors)
- **Quote**: "The industry no longer requires you to be a walking syntax dictionary. Instead, it values: Strong mental models of system architecture."
- **Quote**: "Junior developers may need to adapt and even bypass the traditional 'syntax-mastery' phase to learn the art of rigorous evaluation."
- **Our assessment**: This is the article's most speculative claim and the
  one in tension with practitioner evidence elsewhere in the corpus (see
  Cross-References — Extends/tension with
  `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 6). It should be
  cited as an open question the author raises, not as a settled position —
  the article itself frames it as unresolved ("open to question" per the
  author's own hedge).

### Claim 12: The future of software engineering is framed as "human judgment managing machine velocity," not "human vs. machine" — the surface area of engineering responsibility has expanded, not shrunk, under AI-assisted development
- **Evidence**: Author's closing conceptual argument (H2: "The skill that
  scales").
- **Confidence**: emerging
- **Quote**: "The future of software engineering isn't human vs. machine; it's human judgment managing machine velocity."
- **Quote**: "The surface area of engineering responsibility hasn't shrunk; it has expanded."
- **Our assessment**: This is the article's thesis-level takeaway and directly
  corroborates Ronacher's normative conclusion in
  `blog-ronacher-the-coming-loop.md` (Claim 13: the question is not whether
  to loop but how to retain human judgment within an inevitable looping
  future) — both sources converge on "human judgment persists as the
  scarce, valuable input" even as machine execution speed increases,
  despite reaching that conclusion from different starting critiques (this
  article from a positive/prescriptive framing, Ronacher from a
  quality-degradation critique).

## Concrete Artifacts

```
Source: Richard Gall, "Supervisory engineering: Orchestrating software's
'middle loop'", Thoughtworks Insights, 2026-06-03

Document structure (H2/H3 headings, in order):
  H2 Supervisory engineering (intro)
  H2 What is the 'middle loop'?
  H2 The middle loop in practice: Supervisory engineering
    H3 Aligning intent and setting constrains
    H3 Multi-agent synthesis
    H3 Differential and behavioral review
    H3 Gatekeeping and guardrails
  H2 The three pillars of supervisory engineering
    (Directing / Evaluating / Correcting — no further H3 subdivision)
  H2 The skill that scales

Two parallel taxonomies for the same underlying practices:
  Four practical areas          <-->  Three pillars
  Aligning intent & constraints        Directing
  Multi-agent synthesis                Directing / Correcting (overlaps both)
  Differential & behavioral review     Evaluating
  Gatekeeping & guardrails             Evaluating / Correcting (overlaps both)

Note: the mapping is the Miner's inference from content overlap; the article
does not itself provide an explicit crosswalk between the four areas and the
three pillars.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 2 (15+ named
    specialized subagents run in parallel by a single orchestrator) and
    `blog-anthropic-multi-agent-coordination-patterns.md`'s orchestrator-
    subagent pattern: this article's Claim 4/Claim 10 ("multi-agent
    synthesis"/"correcting") names, at the conceptual level, exactly the
    activity Vlasenko performed concretely — stitching together outputs from
    parallel specialized agents into one coherent system.
  - `blog-ronacher-the-coming-loop.md` Claim 13 (the question is not whether
    to loop, but how to retain human judgment within a looping future) and
    Claim 12 (harness-operated loops risk reducing the human to a
    "messenger" when the "done" signal is delegated to another machine
    judge): this article's Claim 6 ("gatekeeping" — the middle loop as a
    required filter stage before CI/CD) and Claim 2 (the human evaluates
    whether the agent solved the right problem) together argue for exactly
    the human-retained-in-the-loop architecture that Ronacher's Claim 12
    warns is lost when a harness delegates its "done" signal to another
    machine. The two sources are not in tension here: Ronacher critiques the
    failure mode (human reduced to messenger when review is automated away);
    this article prescribes the mitigation (treat the middle loop as a
    mandatory human gate). Read together, they reinforce the same
    architectural recommendation from opposite directions — one as warning,
    one as design principle.

- **Contradicts**: No contradiction issue filed. One tension is worth flagging
  explicitly without escalating to a contradiction: this article's Claim 11
  speculates that experienced engineers are advantaged at supervisory
  evaluation because it "requires deep system context" (Claim 9), while
  `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 6 reports that a
  non-technical practitioner found full delegation *easier* precisely because
  he lacked the instinct to "control every line of code." These are not
  strictly opposed — Vlasenko's claim is about ease of *delegation*
  (willingness to hand off), while this article's claim is about quality of
  *evaluation* (skill at judging output) — different axes, and this
  article's own claim about juniors is self-described as an open question,
  not a settled position. Per MINER.md §4a, this reads as a conditioning
  variable (different question being asked) rather than a material
  contradiction warranting a filed issue; flagging here for the Smith's
  awareness.

- **Extends**: `blog-ronacher-the-coming-loop.md` — Ronacher names and
  defines the "agent loop" (inside the model, tool-calling) vs. "harness
  loop" (outside the agent, orchestrator-level) distinction. This article's
  "middle loop" is a third, complementary axis: not inside-agent vs.
  outside-agent, but inner-loop (IDE) vs. middle-loop (human evaluation of
  agent output) vs. outer-loop (CI/CD and deployment). The two taxonomies
  describe different dimensions of the same overall system (Ronacher: who's
  driving the iteration; this article: which stage of the pipeline the human
  is engaged at) and could be combined in a Ch02 discussion of loop
  architecture.

- **Novel**:
  - **The inner-loop/middle-loop/outer-loop taxonomy**: no existing corpus
    source names a three-part loop structure with an explicit "middle loop"
    sitting between IDE-level coding and CI/CD-level deployment. This is the
    first corpus source to name this layer.
  - **"Supervisory engineering" as a named discipline**: the term itself,
    and its three-pillar (directing/evaluating/correcting) framing, is not
    used in any existing corpus source. The closest existing corpus term is
    Ronacher's "supervisory capacity" (`blog-ronacher-the-coming-loop.md`
    Claim 13), which is used in passing to mean an engineer's bandwidth to
    supervise, not a named discipline with sub-practices.
  - **"Hallucinate its own design patterns" as a named failure mode**
    (Claim 8): a specific, quotable description of what happens absent
    explicit constraints — agents inventing unconstrained architectural
    conventions — that is not phrased this way elsewhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The guide currently discusses harness
  configuration (CLAUDE.md, agent boundaries, multi-agent coordination
  patterns) without a named vocabulary for the human-review layer that sits
  between agent output and CI/CD. Recommend adding a short "middle loop"
  framing (citing this source, Claim 1-2) to introduce where human
  supervisory review fits relative to the harness's own agent/tool loop —
  this is a naming/organizing contribution, not a new practice, since the
  underlying activities (context-window management, standards codification,
  multi-agent stitching) are already covered under "What to Put in
  CLAUDE.md" and "Multi-Agent Coordination Patterns."
- **Chapter 03 (Verification)**: Add the "differential and behavioral review"
  framing (Claim 5) as a named posture for reviewing agent-generated diffs —
  explicitly recommend that reviewers check *what changed in behavior*
  rather than *how the code reads*, since agent output is often
  syntactically clean but may not handle real-world conditions correctly
  (Claim 9). This is a specific, citable addition to any section on human
  review of agent output.
- **Chapter 05 (Team Adoption)**: Cite Claim 11 (open question on whether
  junior engineers can bypass syntax mastery to develop evaluation skill
  directly) as an unresolved question for onboarding/leveling discussions —
  explicitly flag it as speculative and in tension with the practitioner
  evidence in `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 6
  (see Cross-References), rather than presenting either claim as settled.

## Extraction Notes

- WebFetch (the underlying model powering this tool) declined to reproduce
  the article's full text verbatim in a single pass, citing copyright
  concerns, and instead offered summaries. To satisfy the verbatim-quote
  requirement in MINER.md §2a, the article was fetched multiple times with
  narrowly scoped prompts (per-section, per-heading, short-quote-only), and
  every quote above was independently returned by at least one of these
  targeted fetches as an exact excerpt under ~40 words. No quote was
  constructed by splicing across fetches or by paraphrasing a longer
  summary.
- The article contains no named companies, no case studies, no metrics, and
  no code/config artifacts — this is reflected in the "Concrete Artifacts"
  section being limited to the document's own structure rather than any
  external evidence the article cites. Confidence is rated **emerging**
  overall: the core taxonomy (inner/middle/outer loop, three pillars) is a
  plausible and well-articulated conceptual framework from a credible
  trusted-feed publisher, but it is entirely editorial/conceptual — no data,
  no named practitioner experience, and no external validation is offered
  anywhere in the piece. Claim 11 specifically is downgraded to anecdotal
  since it is speculative even by the author's own admission.
- All three Prospector triage comments (issue #1422 has three, apparently
  from repeated auto-triage runs) were reviewed. Two of the three
  independently converged on the three-pillars framing and the
  Ch02/Ch03/Ch05 relevance, which this note follows. The third comment's
  claimed overlap with `docs-github-copilot-web-contextual-chat.md` was
  checked and found unsupported: that note documents GitHub Copilot's web UI
  context-accumulation feature and contains no discussion of supervisory
  review, the middle loop, or human-oversight architecture. No cross-
  reference to that note is included above, since none of its content
  actually overlaps with this source.
- Cross-references verified: `blog-ronacher-the-coming-loop.md` Claims 12
  and 13, and `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claims 2
  and 6, were re-read in full and confirmed to match the content cited above
  before this note was written.
- No contradiction issue filed — see Cross-References/Contradicts above for
  reasoning (conditioning variable, not a material contradiction).
