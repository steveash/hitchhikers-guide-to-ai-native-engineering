---
source_url: https://martinfowler.com/rachels-ramblings/code-review.html
source_type: blog-post
title: "Maybe We Shouldn't Be Reviewing All This Code"
author: Rachel Laycock (CTO, Thoughtworks)
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: anecdotal
issue: "#3192"
---

# Maybe We Shouldn't Be Reviewing All This Code

> Rachel Laycock (CTO, Thoughtworks) argues, as a direct written response to a
> DX panelist's "what are code reviews even for?" position, that AI-generated
> code volume has exposed a deeper problem: teams have loaded too many
> unrelated responsibilities onto code review (quality gate, security check,
> architecture review, mentoring, knowledge-sharing, ownership model). Her
> fix is not to review faster but to move most of those responsibilities
> earlier — pairing, collaborative design sessions, trunk-based development,
> automated checks, fitness functions — and reserve human review for a
> narrow set of named exceptions.

## Source Context

- **Type**: blog-post (personal essay, `rachels-ramblings` series on
  martinfowler.com; ~900 words; published 2 September 2026). Framed
  explicitly as a written rebuttal to a specific interlocutor's public
  position, following an in-person panel disagreement, rather than a
  general-purpose explainer.
- **Author credibility**: Rachel Laycock is CTO at Thoughtworks. The
  `martinfowler.com` feed is designated `trusted-feed` in this repository.
  Laycock states the essay follows a panel at "Code Remix, hosted by
  Moderne" where she publicly disagreed with Brian Houck (DX), who had
  since published his own piece, "What are code reviews even for?" — Laycock
  states Houck "encouraged me to write this" response. The essay is a
  first-person argument and stated professional opinion, not a research
  report or a controlled study; the quantitative figures it cites (Meta,
  DX) are attributed to Houck's post, not independently measured by
  Laycock.
- **Scope**: Covers why AI-generated code volume broke the pull-request
  review model; a "shift the judgment left" framework mapping each named
  function of code review (exploring alternatives, knowledge transfer,
  junior mentoring, collective ownership, architectural alignment,
  deterministic quality checks) to an earlier-shifted practice that could
  substitute for it; a "review by exception" list of cases that still
  warrant a second human's inspection; an explicit rejection of "AI agent as
  human-reviewer substitute" as merely automating the ceremony rather than
  questioning it; and a closing reframe of code review as an
  over-responsibilized artifact. Does NOT include Laycock's own metrics,
  a description of a specific team or client engagement that implemented
  this model, or a rebuttal-by-rebuttal response to each of Houck's points
  (the essay references his piece but does not quote it).

## Extracted Claims

### Claim 1: The central disagreement is not whether AI is producing more code than humans can review, but whether the answer is to review it faster or to stop routing so much through review in the first place
- **Evidence**: Author's stated framing of her disagreement with Brian Houck, given as the essay's explicit thesis.
- **Confidence**: anecdotal
- **Quote**: "My question is: why are we waiting until code review to do all of those things?"
- **Our assessment**: This is the essay's organizing claim and the basis for filing [contradiction issue #3206](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3206) against `blog-addyosmani-agentic-code-review.md`, whose Claim 7 keeps the pull request as the central artifact and tiers its rigor by blast radius rather than questioning whether review should remain central at all. Laycock explicitly states a prior, independent distaste for PR-centric workflows ("I've never particularly liked pull requests as the centre of the software development process"), which predates and is not solely a reaction to AI-generated volume.

### Claim 2: AI-generated code volume has grown sharply by two independent measures Laycock attributes to Houck's post — Meta's lines of code per human-landed diff up 106% in a year, and DX's median pull request size up 64%
- **Evidence**: Figures attributed to Brian Houck's own piece, cited by Laycock as shared, undisputed context for the disagreement rather than something she measured herself.
- **Confidence**: anecdotal (secondhand citation of another author's figures, not independently verified by Laycock or by this note against Houck's original piece)
- **Quote**: "Brian cites some pretty striking numbers: at Meta, significant lines of code per human-landed diff reportedly increased 106% in a year, while DX's own data shows median pull request size increasing 64%."
- **Our assessment**: These are the same class of secondhand, vendor/practitioner-cited volume statistics already present in this corpus via `blog-addyosmani-agentic-code-review.md` Claims 1-2 (GitClear's ~4x raw-output figure, Faros AI's 861% code-churn and 441.5% review-duration increases). This note's figures are not identical numbers, but they corroborate the same underlying trend from a third, independent attribution chain (Meta, DX) — worth citing alongside, not instead of, the Osmani post's four datasets as further evidence the review-volume problem is measured and industry-wide, not anecdotal to a single team.

### Claim 3: Code review is credited with several distinct functions beyond bug-finding — exploring alternative solutions, knowledge transfer, teaching junior engineers how experienced engineers think, building collective ownership, and architectural alignment — and Laycock proposes a specific earlier-shifted practice for each
- **Evidence**: Author's structural argument, stated as a direct point-by-point mapping ("Take the things we say code review gives us").
- **Confidence**: anecdotal
- **Quote**: "If we want to explore alternative solutions, I'd rather do that before implementing one of them." / "If we want knowledge transfer, pair. Sitting next to someone, physically or virtually, while they reason through a problem teaches you far more than reading their completed solution afterwards." / "If we want junior engineers to learn how experienced engineers think, let them work with experienced engineers while they're thinking." / "If we want collective ownership, organise teams so people actually build and operate software collectively rather than relying on a pull request to tell everyone what somebody else has already built." / "If we want architectural alignment, design together ... and then encode the important constraints as fitness functions."
- **Our assessment**: This is the most concrete, actionable content in the essay — a named substitution for each function review is asked to perform, rather than a general "shift left" slogan. It is the mechanism underlying Claim 1's thesis and is the specific content a guide section would cite if recommending this model. Note that "encode constraints as fitness functions" is asserted without a worked example or named tool in this essay (unlike, e.g., the Thoughtworks retreat report's named constraint-test/scenario-test vocabulary in `blog-fowler-fragments-2026-07-21.md` Claim 2), so it should be treated as a directional recommendation, not a documented technique.

### Claim 4: Deterministic review concerns — formatting, linting, known security problems, anything that can be deterministically tested — should be automated rather than reviewed by a human at all
- **Evidence**: Author's stated position, offered as the final item in the same point-by-point mapping as Claim 3.
- **Confidence**: anecdotal
- **Quote**: "And if we're reviewing code for formatting, linting, known security problems or things that can be deterministically tested, automate them. We really shouldn't still be arguing about whitespace in 2026."
- **Our assessment**: This is a narrow, uncontroversial claim relative to the rest of the essay and corroborates already-settled practice elsewhere in the corpus rather than adding new evidence; its value here is that Laycock treats it as the baseline everyone should already agree on before the more contested claims (Claims 1, 3, 5) are argued.

### Claim 5: Human review should be reserved for a named set of exceptions — a fundamental architectural change, a change crossing a sensitive security boundary, a change with a huge blast radius, an unfamiliar part of a critical system, or any case where the team itself says "I'm not confident about this" — rather than being required for every change
- **Evidence**: Author's stated policy, given as a specific list under the essay's "Review by exception" section heading.
- **Confidence**: anecdotal
- **Quote**: "There are absolutely changes where I want another experienced human looking. An example would be a fundamental architectural change. ... Other examples could be something crossing a sensitive security boundary, a change with a huge blast radius, an unfamiliar part of a critical system or simply something where the team says, 'I'm not confident about this.'"
- **Our assessment**: This list overlaps substantially with the "full stack" end of `blog-addyosmani-agentic-code-review.md` Claim 7's blast-radius tiering (that post's own example: "a payments path earns the full stack"). The practical convergence between the two frameworks — both would flag a payments/security-boundary change for full human scrutiny — is the basis for recommending a `debated` (not `accepted-A`/`accepted-B`) verdict in contradiction issue #3206: the disagreement is less about which changes deserve review than about whether PR review remains the default mechanism (Osmani, tiered-but-central) or the rare exception after most judgment has already happened earlier (Laycock).

### Claim 6: Automating code review by having an AI agent act as the human reviewer, in order to preserve the existing review process at higher speed, treats the symptom rather than the cause
- **Evidence**: Author's stated objection to a specific alternative approach (AI-as-reviewer), presented as a rejected option distinct from her own proposal.
- **Confidence**: anecdotal
- **Quote**: "I don't think the answer is an AI agent pretending to be the human reviewer so we can preserve exactly the same process at higher speed. That's automating the ceremony rather than questioning why the ceremony exists."
- **Our assessment**: This is a direct, named objection to the general category of AI-code-review tooling that much of this corpus's existing review coverage documents favorably (e.g., `blog-addyosmani-agentic-code-review.md` Claim 4's 60M+ Copilot reviews, Claim 5's tool-comparison benchmarks, and the broader CodeRabbit/Anthropic Code Review material). Laycock does not name or critique any specific AI-review tool or vendor, so this should be read as a structural critique of the category ("ceremony automated rather than questioned"), not a claim that any specific tool underperforms — it is compatible with those tools existing and being useful for the narrower "review by exception" cases (Claim 5), just not as a wholesale substitute for reviewing everything.

### Claim 7: If an agent can produce ten times the code but every line still queues for a senior engineer to inspect, the result is not a ten-times engineering organization but a larger backlog and a new bottleneck
- **Evidence**: Author's stated argument, following directly from the "review by exception" framing.
- **Confidence**: anecdotal
- **Quote**: "If an agent can produce ten times the code but every line eventually queues up waiting for a senior engineer to inspect it, we haven't created a ten-times engineering organisation, we've created a big backlog and a new bottleneck."
- **Our assessment**: This is a sharp, quotable framing of the same "generation sped up, verification didn't" dynamic already well-established in this corpus (e.g., `blog-fowler-fragments-2026-07-21.md` Claim 1's "code generation is no longer the bottleneck — verification is," and `blog-addyosmani-agentic-code-review.md` Claim 1's 4x-output-vs-12%-value gap). It restates rather than extends that thesis, but is a useful, memorable one-line citation for a guide section introducing the bottleneck-shift problem.

### Claim 8: Laycock agrees that AI-generated code creates a real risk of teams accumulating cognitive and intent debt, but does not believe mandatory pull requests are a particularly strong defense against it, and instead argues human understanding must be maintained deliberately through collaborative design, pairing, good boundaries, executable architecture, and shared operational responsibility
- **Evidence**: Author's direct response to a specific concern she attributes to Brian Houck's piece.
- **Confidence**: anecdotal
- **Quote**: "He talks about teams accumulating cognitive and intent debt: software grows while the humans responsible for it understand less and less about why it works the way it does. I think that's a very real problem. I just don't think mandatory pull requests are a particularly strong defence against it." / "If agents are going to produce substantially more of the implementation, we need to be much more deliberate about maintaining human understanding through collaborative design, pairing, good boundaries, executable architecture, shared operational responsibility and probably some practices we haven't invented yet." / "We need engineers to understand systems, not diffs."
- **Our assessment**: This directly engages the same comprehension/intent-debt cluster already present in this corpus via `blog-addyosmani-intent-debt.md` (whose Claim 8, per that note, treats lightweight decision logs — typically attached to the PR — as "pure intent-debt paydown"). There is a real tension worth flagging for the Smith even though it does not rise to a separate filed contradiction under MINER.md §4a's "materially opposes, leads to different guide advice" bar on its own: Laycock explicitly denies that the mandatory-PR mechanism itself is a strong defense against intent debt, while the Osmani decision-log practice is a lightweight addition *to* that same PR mechanism. The two are not strictly incompatible (a team could adopt Laycock's earlier-shifted practices as the primary defense and still attach decision logs to whatever PRs remain), but a guide section should not cite the Osmani decision-log claim as if it settles the question Laycock raises about PRs generally being an effective intent-debt defense.

### Claim 9: Code review has, over time, been loaded with an unusually large number of distinct organizational responsibilities — quality gate, security check, architecture review, mentoring mechanism, knowledge-sharing system, and ownership model — and this overload, not AI specifically, is the underlying problem AI-generated volume has exposed
- **Evidence**: Author's closing reframe, presented as the essay's summary thesis.
- **Confidence**: anecdotal
- **Quote**: "We've spent years loading an extraordinary number of responsibilities onto the humble code review: quality gate, security check, architecture review, mentoring mechanism, knowledge-sharing system, ownership model." / "It worked, sort of, while humans could only produce code so quickly. That constraint is disappearing. So perhaps the question isn't how we get the code reviewed faster. Perhaps it's why we're waiting until code review to have all the important conversations in the first place."
- **Our assessment**: This is the essay's title-level thesis, restating Claim 1 as the closing argument. Its guide value is as a compact, six-item checklist (quality gate / security check / architecture review / mentoring / knowledge-sharing / ownership model) that a guide section could use to structure a discussion of *which* of review's traditional responsibilities a given team should shift earlier versus keep in review — since Laycock's essay argues all six should move, but a team adopting this model piecemeal would need to decide per-responsibility, which the essay does not itself walk through beyond the mapping in Claim 3.

### Claim 10: Agents can participate in the earlier-shifted feedback loops themselves — challenging designs, testing assumptions, continuously verifying what is being built — but the substantive thinking driving those loops should still come from experienced humans, and that experience only benefits the whole team if the team acts collectively much earlier than code review
- **Evidence**: Author's stated qualification, appended directly to the list of shifted practices (pairing, trunk-based development, automated testing, static analysis, fitness functions, security scanning).
- **Confidence**: anecdotal
- **Quote**: "Increasingly, agents can participate in those loops too, challenging designs, testing assumptions and continuously verifying what is being built, but the real thinking is coming from experienced humans and if we want that experience to benefit the whole team then we have to act like one much earlier than code review."
- **Our assessment**: This is a narrower, more qualified claim than it might first appear — Laycock is not proposing agents replace pairing or design sessions, only that they can participate alongside humans within those earlier loops. It is compatible with, and a lighter-weight version of, the "human judgment relocates rather than disappears" thesis already well-represented in this corpus via `blog-addyosmani-human-judgment-relocates.md` Claim 15 ("The best software factories will not be defined by how completely they eliminate human involvement. They will be defined by how intelligently they place it.") — both authors argue for relocating rather than removing human judgment, though Laycock's relocation target is earlier-in-the-SDLC collaborative practices specifically, while Osmani's is spread across a factory's multiple human-intervention points (shape, steer, handoff, stop-shipping).

## Concrete Artifacts

```
Source: Rachel Laycock, "Maybe We Shouldn't Be Reviewing All This Code"
(martinfowler.com/rachels-ramblings/code-review.html, 2 September 2026)

"SHIFT THE JUDGMENT LEFT" — what review is credited with, and Laycock's
proposed earlier-shifted substitute for each:

  Review function                  Proposed substitute
  --------------------------------  --------------------------------------
  Exploring alternative solutions   Explore before implementing (design
                                     conversation, not post-hoc review)
  Knowledge transfer                Pairing (physically or virtually)
  Junior engineers learning how     Pairing with experienced engineers,
    experienced engineers think     or collective whiteboard design
                                     sessions, before code is written
  Collective ownership              Organize teams to build/operate
                                     collectively (pairing, mob
                                     programming, team design sessions)
                                     rather than a PR announcing what one
                                     person already built
  Architectural alignment           Design together; encode constraints
                                     as fitness functions
  Formatting / linting / known      Automate (deterministic checks, not
    security problems / anything    human review)
    deterministically testable

"REVIEW BY EXCEPTION" — cases that still warrant a second human's review:
  - A fundamental architectural change
  - Something crossing a sensitive security boundary
  - A change with a huge blast radius
  - An unfamiliar part of a critical system
  - Any case where the team says "I'm not confident about this"

CODE REVIEW'S ACCUMULATED RESPONSIBILITIES (closing argument):
  quality gate, security check, architecture review, mentoring mechanism,
  knowledge-sharing system, ownership model
```

## Cross-References

### Cross-reference verification notes
`blog-addyosmani-agentic-code-review.md`, `blog-addyosmani-human-judgment-relocates.md`,
`blog-addyosmani-intent-debt.md`, and `blog-fowler-fragments-2026-07-21.md` were
each re-read directly and claim numbers below were confirmed against those
notes' numbered `### Claim N:` headings in document order (MINER.md §4b).
`blog-fowler-fragments-2026-09-01.md` (the same trusted feed's adjacent
entry) was checked and found to cover unrelated topics (LLM-writing
detection, long-horizon agent architecture, CI, biosecurity, scholarly-paper
contamination) — no overlap with this source.

- **Corroborates**:
  - `blog-fowler-fragments-2026-07-21.md` Claim 3 (the Thoughtworks retreat
    report: "no one in the room could cite data on how many defects manual
    review actually catches" — a "status quo illusion") — Laycock's Claim 8
    skepticism that mandatory PRs are "a particularly strong defence"
    against cognitive/intent debt is consistent with, and independently
    arrived at alongside, that report's finding that review's actual
    defect-catch effectiveness has never been measured. Both sources
    challenge the same unstated assumption (that mandatory review is a
    known-effective safeguard) from different angles — one via missing
    data, the other via a structural argument about what review can
    realistically defend against.
  - `blog-addyosmani-agentic-code-review.md` Claims 1-2 (GitClear's ~4x
    output/12% value gap; Faros AI's 861% churn, 441.5% review-duration
    increase) — this note's Claim 2 (Meta's 106% LOC/diff increase, DX's
    64% PR-size increase) adds a third, independently attributed data
    source corroborating the same industry-wide volume trend.
  - `blog-addyosmani-human-judgment-relocates.md` Claim 15 ("human judgment
    is being relocated," not eliminated) — this note's Claim 10 (agents
    participate in earlier loops, but substantive thinking still comes from
    experienced humans) is a compatible, narrower application of the same
    relocation thesis to Laycock's specific earlier-shifted practices.

- **Contradicts**:
  - `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review by
    blast radius, keeping PR review as the central, scaled mechanism) —
    **filed as [contradiction issue #3206](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3206)**.
    Both sources agree review shouldn't apply uniform rigor to every
    change, and their "which changes deserve full scrutiny" lists converge
    substantially (this note's Claim 5 vs. Osmani's "a payments path earns
    the full stack" example), but they disagree on the structural
    question: whether pull-request review, tiered, remains the SDLC's
    default mechanism (Osmani) or is demoted to a rare exception after
    most judgment has already happened earlier via pairing and design
    sessions (Laycock, this note's Claims 1, 3, 5). Per MINER.md §4a, no
    verdict is picked in this note — see the issue and, once resolved,
    CONTRADICTIONS.md.
  - A narrower, related tension (not separately filed — see Claim 8's Our
    assessment) with `blog-addyosmani-intent-debt.md`'s decision-log
    recommendation: that note treats lightweight decision logs attached to
    PRs as "pure intent-debt paydown," while this source's Claim 8
    explicitly denies that mandatory pull requests generally are "a
    particularly strong defence" against intent/cognitive debt. The two
    are not strictly incompatible (decision logs could be attached to
    whichever PRs survive under Laycock's review-by-exception model), but
    a guide section should not cite the decision-log claim as settling the
    broader question Laycock raises.

- **Extends**:
  - `blog-fowler-fragments-2026-07-21.md` Claim 5 (the retreat report's
    "two clocks" diagnostic — production-clock vs. decision-clock — and its
    PM/designer "superpowers" cautionary case study about eroded pairing
    culture) — this note's emphasis on pairing and collective design
    sessions as review's replacement gives a specific, prescriptive
    practice for closing exactly the "decision-clock" gap that report
    names as the sharper, harder-to-see bottleneck once code-production
    throughput stops being the constraint.

- **Novel**:
  - The first source note in this corpus authored directly by a named
    Thoughtworks CTO (Rachel Laycock) rather than curated/paraphrased by
    Martin Fowler or cited secondhand through another practitioner's post.
  - The explicit, six-item "what review has been asked to do" checklist
    (quality gate, security check, architecture review, mentoring,
    knowledge-sharing, ownership model) as a structuring device for
    per-responsibility guide discussion (Claim 9).
  - The specific "review by exception" criteria list (Claim 5) as a named,
    citable alternative to blast-radius tiering.
  - The explicit, named objection to "AI agent as human-reviewer
    substitute" as ceremony-automation rather than ceremony-questioning
    (Claim 6) — no existing corpus source frames AI code-review tooling
    this critically at the structural level (as opposed to critiquing
    individual tools' precision/recall).

## Guide Impact

- **Chapter 02 (Core Patterns / agentic workflows, review policy)**: Present
  this source alongside `blog-addyosmani-agentic-code-review.md` as a
  `**Debated:**` block per contradiction issue #3206, once resolved. Add the
  "shift the judgment left" mapping (Claim 3, Concrete Artifacts) as a named
  alternative framework to blast-radius tiering — a team choosing between
  the two models should understand that Osmani's keeps PR review central
  and scales its rigor, while Laycock's demotes PR review to a rare
  exception after pairing/design sessions absorb most of what review used
  to do. Add the "review by exception" criteria list (Claim 5) as a
  concrete alternative decision rule, noting its practical overlap with
  Osmani's "full stack" tier.

- **Chapter 05 (Team Adoption / Team Organization & Culture)**: Add Claim 3's
  specific substitutions (pairing for knowledge transfer and junior
  mentoring, mob/whiteboard design sessions for collective ownership and
  architectural alignment, trunk-based development) as concrete practices a
  team could adopt to shift review's functions earlier, citing this source.
  Cross-reference with `blog-fowler-fragments-2026-07-21.md` Claim 5's "two
  clocks" diagnostic and its PM/designer cautionary case study, since both
  sources treat pairing/collective design as load-bearing for organizational
  cohesion, not just individual productivity.

- **Chapter 03 (Verification)**: Add Claim 7's "ten-times code, still a
  bottleneck" framing as a memorable one-line citation for a section
  introducing the generation/verification bottleneck shift, alongside the
  existing `blog-fowler-fragments-2026-07-21.md` Claim 1 anchor citation.
  Add Claim 4 (automate deterministic checks) as uncontroversial baseline
  guidance.

## Extraction Notes

- The article's full text was recovered via `curl` with a browser
  user-agent, followed by a Python stdlib HTML-tag-stripping pass (block
  tags converted to newlines, tags stripped, entities unescaped) rather
  than relying on WebFetch's summarization mode — consistent with the
  pattern independently noted in several other Fowler-fragments and Osmani
  source notes in this corpus. Every `Quote` field above was located
  character-for-character in that raw-text capture. The full recovered
  article body is short (≈33 lines of substantive prose after boilerplate
  navigation/footer removal), so it was read in its entirety, not sampled.
- No linked sub-pages were followed: the essay references Brian Houck's
  "What are code reviews even for?" piece by name but does not link it in
  the extracted HTML, and no other substantive external link appears in the
  article body. This is a self-contained essay.
- A contradiction was identified during extraction (Claim 1 vs.
  `blog-addyosmani-agentic-code-review.md` Claim 7) and filed per MINER.md
  §4a as [issue #3206](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3206)
  before this note was written. No verdict is asserted here; see the issue
  and, once resolved, CONTRADICTIONS.md.
- Confidence rated `anecdotal` overall: this is a single practitioner's
  stated opinion and argument (albeit from a high-credibility, trusted-feed
  author explicitly responding to a named interlocutor), with no original
  measurement, case study, or client engagement data of Laycock's own — the
  only quantitative figures in the piece (Claim 2) are attributed secondhand
  to Brian Houck's post and were not independently verified against that
  source.
