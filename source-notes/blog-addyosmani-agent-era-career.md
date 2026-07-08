---
source_url: https://addyosmani.com/blog/career-advice-age-of-agents/
source_type: blog-post
title: "The Agent-Era Career"
author: Addy Osmani
date_published: 2026-07-06
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: anecdotal
issue: "#1643"
---

# The Agent-Era Career

> Osmani argues that as agents commoditize anything with an "answer key"
> (solving well-posed problems), the durable, ungradeable career skill
> becomes choosing which problems to work on and judging whether the
> machine solved them well — and offers a set of concrete personal
> practices (deliberate practice without agents, a private mistake log,
> per-task autonomy dialing, periodic from-scratch rebuilds) for building
> that judgment deliberately rather than letting it atrophy.

## Source Context

- **Type**: blog-post (personal essay / career advice, explicitly framed as
  a response to and extension of another author's piece)
- **Author credibility**: Addy Osmani — "an engineering and evangelism
  leader who spent over 14 years at Google leading developer experience
  across Chrome and, in recent years, AI (Gemini, coding agents, and
  agentic engineering), most recently as a Director at Google Cloud AI." He
  is already the corpus's most-cited single author
  (`blog-addyosmani-agentic-code-review.md`, `blog-addyosmani-intent-debt.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-new-software-lifecycle.md`, `blog-osmani-good-spec.md`).
  Unlike those posts, this one is not a technical synthesis of third-party
  data — it is first-person career advice, explicitly built on his own
  biography ("I was at Google for over 14 years... I've turned down offers
  from frontier labs and FAANG companies when the fit wasn't right") and,
  by his own statement, on someone else's original idea (see below).
- **Scope**: Covers career-level advice for engineers in an agent-heavy
  environment: what's scarce (reputation, judgment, attention), what
  practices build judgment (deliberate practice, a private error log,
  periodic from-scratch rebuilds), how to delegate to agents (autonomy as a
  per-task setting, specification vs. verification as distinct skills,
  personal accountability for shipped agent output), and how to think about
  opportunity (the "xG and finishing" framing, betting on team over demo).
  Does NOT provide any data, benchmark, or third-party citation beyond one
  attributed concept (Rich Sutton's "bitter lesson") and one attributed
  origin ("This piece grew out of Phil Chen's original", linked to a single
  X/Twitter post, not fetched — see Extraction Notes). This is a pure
  opinion/advice piece; treat every claim below as the author's personal
  position, not as measured or independently verified.

## Extracted Claims

### Claim 1: The scarce resource in an agent-native career is reputation and relationships built through good work, not capital or time, both of which are now abundant
- **Evidence**: Author's personal narrative (years spent in open source with "almost zero direct payoff" that nonetheless compounded into later opportunities) contrasted with an explicit claim about what is and isn't abundant.
- **Confidence**: anecdotal
- **Quote**: "Many resources are abundant. Capital is abundant. Time is abundant. Real relationships, and especially track record of doing good work, are still scarce."
- **Our assessment**: This is a personal-experience claim with no measurement behind it, but it is a clean, quotable framing of "optimize for the resource that doesn't get cheaper as AI improves." It sets up the rest of the post's individual claims (judgment, taste, verification) as instances of the same underlying resource-scarcity argument rather than unrelated tips.

### Claim 2: As agents absorbed problem-solving, the valuable skill shifted from solving problems to selecting which ones matter
- **Evidence**: Author's own origin story (noticing dial-up was slow, inventing chunked multi-connection fetching, then moving to the next hard problem) plus a direct classroom observation (students with identical agents and problem sets produce "wildly different" results).
- **Confidence**: anecdotal
- **Quote**: "solving problems went cheap while selecting them became scarce."
- **Our assessment**: This is the post's central reframing claim and the thesis the rest of the piece elaborates. It is consistent with, and gives an individual-career gloss to, the corpus's existing organizational-level "verification/judgment is the bottleneck" convergence (see Cross-References), but here it is asserted from personal anecdote (one classroom observation, one origin story), not measured — we rate it anecdotal despite its directional alignment with better-evidenced corpus claims.

### Claim 3: Taste (judgment/pattern-matching) is earned by grinding through real code, and the real risk of agent use is not bad output but losing the ability to recognize bad output
- **Evidence**: Author's account of building judgment by "grinding out boilerplate and fixing bugs" and "seeing the worst abstractions humans could devise."
- **Confidence**: anecdotal
- **Quote**: "The real risk isn't agents writing bad code. We've been there before. It's losing the ability to tell." / "Taste is pattern-matching, but all that pattern-matching has to be earned by doing the work."
- **Our assessment**: This names a specific failure mode — judgment atrophy from disuse — that is distinct from "agents produce bad code." It's a plausible mechanism (skills that aren't exercised regularly degrade) but is asserted rather than measured; no timeframe, no before/after comparison of engineers who did vs. didn't practice this way. Useful as a named risk for a guide chapter, not as evidence of prevalence.

### Claim 4: A concrete deliberate-practice routine builds judgment: solve some problems manually without the agent, read far more code than you write, treat every agent diff like a review that must be justified, and keep a daily private log of agent mistakes
- **Evidence**: Author's own prescribed routine, offered as a numbered set of habits.
- **Confidence**: anecdotal
- **Quote**: "Pick a few problems that really matter. Do them the hard way, without the agent, building deep mental models of how systems and languages work. Read a thousand times more code than you ever write. Treat every diff from an agent like a human review you need to carefully justify. Go deep on at least one system end to end, from intake to output. On a daily basis, keep a private log of every time you see an agent suggest something that looks wrong and confidently flag it."
- **Our assessment**: This is the single most concrete, actionable artifact in the post — a specific daily/recurring practice rather than a general exhortation to "stay sharp." It directly corroborates `blog-ghuntley-miami-hot-takes.md` Claim 13 (deliberate, intentional practice with AI tools, framed via the same "instrument, not a tool" metaphor) from an independent author within roughly two weeks of each other, which is a meaningful convergence signal for a genuinely new-to-2026 piece of career advice.

### Claim 5: Delegating to an agent should mirror delegating to a person — scope the task, define done, calibrate trust, verify the result — with autonomy set per task rather than fixed by rank
- **Evidence**: Author's prescriptive framing, given as a direct analogy to human delegation.
- **Confidence**: anecdotal
- **Quote**: "Autonomy is a setting, not a rank; it's a per-task switch." / "Turn it up to the maximum on something small and reversible and cheap to check. Turn it down on anything where mistakes will be hard to undo."
- **Our assessment**: This corroborates `blog-cursor-agent-autonomy-auto-review.md` Claim 1 ("Auto-review, which makes decisions around agent autonomy behave more like a dial than a switch") — the two sources use opposite words for the mechanism (Osmani: "a per-task switch"; Cursor: "more like a dial than a switch") but describe the same underlying idea: autonomy should vary continuously with the task's risk/reversibility rather than being fixed once (by a person's rank, in Osmani's framing, or by a single global permission setting, in Cursor's). This is a terminology difference, not a substantive disagreement, so it is not filed as a contradiction per MINER.md 4a — both sources argue against a static, all-or-nothing autonomy setting.

### Claim 6: Specification and verification are distinct engineering skills, and verification specifically means not trusting an agent's own self-report as evidence
- **Evidence**: Author's structural claim distinguishing the two skills.
- **Confidence**: anecdotal
- **Quote**: "Specification and verification are two distinct, complementary skills. The agent isn't as good as the intent you hand it. The best engineers are those who know how to write precise specs; clear thinking made legible." / "It's verification, not evidence. Not evidence in the form of an agent grading its own homework."
- **Our assessment**: The "agent grading its own homework" framing is a sharp, specific articulation of the self-evaluation-bias risk this corpus already documents with first-party data in `blog-anthropic-harness-long-running.md` (models "confidently praising the work — even when, to a human observer, the quality is obviously mediocre"). Osmani's contribution here is naming it as a career/individual-skill distinction (specify vs. verify) rather than a harness-architecture problem (generator vs. evaluator), which is a useful individual-practice complement to that more mechanistic corpus finding.

### Claim 7: Accountability for shipped code stays with the human who shipped it, regardless of whether an agent wrote it
- **Evidence**: Author's direct normative statement.
- **Confidence**: anecdotal
- **Quote**: "“the AI did it” is not a defense." / "Your name is on the change."
- **Our assessment**: This is a bare assertion with no supporting incident or example, but it is independently and more rigorously corroborated by `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 7, which cites Narayanan & Kapoor's structural argument that "human teams need to be accountable for what they deliver" as one of three durable bottlenecks resisting AI automation. Osmani's version is the individual-career framing of the same structural claim; Narayanan & Kapoor's is the organizational-accountability framing. Together they make a stronger case than either alone that accountability, not just verification capability, is a durable (not merely current-state) constraint.

### Claim 8: Career value concentrates in attempting the hardest version of a problem, following the same logic as Rich Sutton's "bitter lesson" that general, scalable methods beat hand-tuned ones
- **Evidence**: Author's analogical argument, explicitly borrowing Sutton's framework and applying it to career strategy rather than ML methods.
- **Confidence**: anecdotal
- **Quote**: "Rich Sutton's bitter lesson: in almost every field general methods that scale with additional compute beat out hand-tuned equivalents. As a career lesson, there's no point in solving an easy version of the problem, it's worth almost nothing."
- **Our assessment**: This is an analogy transplanted from ML research methodology to individual career choice, which is a rhetorical move, not an empirical claim about careers — Sutton's original observation was about compute-scaled general methods outperforming hand-engineered ones in AI research, and Osmani is using it as a metaphor for "attempt hard problems, not easy ones." We buy the underlying career advice (harder problems differentiate more) but flag that the Sutton citation lends borrowed authority rather than direct evidentiary support for the career claim itself.

### Claim 9: Agents reliably deliver about 70% of a feature quickly, but the remaining 30% — edge cases, architecture, taste — is where all differentiated value now lives, making "finishing" the actual deliverable
- **Evidence**: Author's stated rule of thumb, framed against a description of "median" agent output from a "lazy prompt."
- **Confidence**: anecdotal
- **Quote**: "No turnkey agent writes a whole system from end to end. As a rule, you'll get 70% of a feature quickly from an agent, and the last 30%—debugging the gnarly edge cases, figuring out the right architecture, cultivating the right taste—will be the whole game." / "When first drafts come free, finish is the product."
- **Our assessment**: The 70/30 split is presented "as a rule" with no measurement methodology (no sample of features, no definition of "done") — it should be read as an illustrative heuristic from personal experience, not a benchmark figure, unlike (for contrast) the specific attributed third-party statistics in `blog-addyosmani-agentic-code-review.md` (e.g. GitClear's 4x/12% figures, which are at least named-dataset citations). The qualitative point — that agent output clusters around a "median" that itself keeps rising, so differentiation moves to finishing — is a reasonable and now-common framing (see `blog-anthropic-ai-native-engineering-org.md` Claim 1 on the bottleneck shifting to verification), but the specific 70/30 number is Osmani's own unaudited estimate.

### Claim 10: A concrete personal practice for staying sharp at "finishing": periodically rebuild a project entirely from scratch using the newest frontier model rather than incrementally patching old code
- **Evidence**: Author's own stated habit.
- **Confidence**: anecdotal
- **Quote**: "every few months I completely rebuild from scratch using the latest, sharp-end-of-the-sword model. It's less exhausting than nursing half-hearted old code to health."
- **Our assessment**: This is a novel, concrete, easily-adoptable practice not previously captured in this corpus's Osmani notes (which document orchestration, review, and intent-debt practices, but not a periodic-rebuild habit). No cadence detail beyond "every few months," no cost/token data, and no comparison against the incremental-patching alternative beyond the author's subjective "less exhausting" — treat as a single practitioner's habit, not a validated technique.

### Claim 11: Career opportunity has two separable levers, analogous to a soccer player's expected goals (xG) and finishing rate — generating chances (via public work and reputation) and converting them (via judgment) — and only the latter is something you fully control
- **Evidence**: Author's extended sports metaphor, paired with a personal claim about the source of his own opportunities.
- **Confidence**: anecdotal
- **Quote**: "xG measures the number of chances your play should produce. Finishing measures whether you convert them." / "I've only ever had big opportunities as a result of work I've done in public, never from a job I've applied for. You can't script which chances arrive, only whether you're standing where they land."
- **Our assessment**: This is a memorable framing device but is built entirely on the author's own single-case experience ("I've only ever had..."), with no comparison to engineers whose opportunities came through applications rather than public work. Useful as a mental model for a guide section on career strategy, but should be presented as a metaphor/heuristic, not a demonstrated career-outcomes finding.

### Claim 12: Engineers should evaluate opportunities based on team trajectory and market position rather than the current product, since a good team routinely reinvents its product into something unrecognizable
- **Evidence**: Author's direct prescriptive statement.
- **Confidence**: anecdotal
- **Quote**: "bet on the team and the market opportunity, not the demo." / "It's true that your work has to exist somewhere, but a good team quickly mutates their current offering into something unrecognizable."
- **Our assessment**: Standard startup/career advice reframed for an agent-native context (the "demo" specifically evokes AI-product prototypes, which are cheap and fast to produce now, per the post's own "vibe-coding makes earning a quick buck trivial" line in Claim 1's paragraph). No new evidence offered; it's an assertion consistent with general pre-AI startup-evaluation wisdom, applied here to argue that AI-era demos are even less predictive of a team's eventual product than before.

### Claim 13: Because agents can scale output infinitely while human attention cannot, attention (not time or effort) is the individual's most precious and non-renewable career asset
- **Evidence**: Author's closing structural argument, contrasting agent output scaling with human attention.
- **Confidence**: anecdotal
- **Quote**: "the last few feet are infinite (agents scale output infinitely; you don't)." / "Your attention is your most precious asset, and it doesn't refill."
- **Our assessment**: This closing claim reframes the whole post's advice (judgment, verification, deliberate practice, accountability) as different applications of one scarce resource — attention — rather than a list of unrelated tips. It's a rhetorical synthesis, not new evidence, but it's a useful one-line takeaway for summarizing the piece if the guide only has room to cite one claim from this source.

## Concrete Artifacts

```
Source: Addy Osmani, "The Agent-Era Career," https://addyosmani.com/blog/career-advice-age-of-agents/ (July 6, 2026)

Closing synthesis line (verbatim):
"the world isn't short on opportunity; it's short on people who can find
the right problem, tell whether the machine solved it, and finish past
where the machine stopped."

Author bio (verbatim, used for Source Context credibility assessment):
"Addy Osmani is an engineering and evangelism leader who spent over 14
years at Google leading developer experience across Chrome and, in recent
years, AI (Gemini, coding agents, and agentic engineering), most recently
as a Director at Google Cloud AI."

Explicit attribution of the piece's origin (verbatim, footer note):
"This piece grew out of Phil Chen's original, which is well worth reading
in full." [links to https://x.com/philhchen/status/2072793818945167475 --
a single X/Twitter post, not an article; not independently fetched, see
Extraction Notes]
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 7
    ("Verifying and being accountable for delivery" resists AI automation,
    quoting Narayanan & Kapoor: "human teams need to be accountable for
    what they deliver") — independently and more rigorously supports this
    post's Claim 7 ("Your name is on the change"). Claim 6 of that same note
    ("Deciding and specifying what to build" resists automation because
    "requirements specification takes surprisingly long") likewise
    corroborates this post's Claim 6 (specification as a distinct,
    high-value skill).
  - `blog-anthropic-ai-native-engineering-org.md` Claim 1 ("Verification,
    code review, and security replaced code-writing as the primary
    bottlenecks") — a first-party, better-evidenced version of this post's
    Claim 2/Claim 9 thesis that value shifted from generation to judgment.
  - `blog-ghuntley-miami-hot-takes.md` Claim 13 ("AI tools are better
    understood as an instrument to be played through deliberate,
    intentional practice") and Claim 5 ("Curiosity... is now the primary
    determinant of career survival") — an independent author making closely
    related deliberate-practice and career-durability claims within about
    two weeks of this post.
  - `blog-cursor-agent-autonomy-auto-review.md` Claim 1 ("dial rather than
    a switch") — corroborates this post's Claim 5 on per-task autonomy
    calibration, despite the surface-level opposite terminology (see Claim
    5's assessment above for why this is not a contradiction).
  - `blog-anthropic-harness-long-running.md` (self-evaluation bias: agents
    "confidently praising the work" on their own output) — corroborates the
    mechanism behind this post's "agent grading its own homework" framing
    in Claim 6, applied there at the harness-architecture level and here at
    the individual-practice level.

- **Contradicts**: None identified. This post does not directly oppose any
  existing corpus source note on a claim that would drive different guide
  advice; the closest surface-level tension (autonomy as "a switch" here
  vs. "more like a dial than a switch" in `blog-cursor-agent-autonomy-auto-review.md`)
  is a terminology difference describing the same underlying mechanism, not
  a factual disagreement — see Claim 5's assessment. No contradiction issue
  filed.

- **Extends**:
  - `blog-addyosmani-intent-debt.md` Claim 9 ("Software's scarce resource
    shifted from... correct implementation... to intent, the one input
    that still has to originate with a human") — this post extends that
    claim from a system/artifact-level framing to an individual career/
    reputation-level framing (Claim 1, Claim 2 here).
  - `blog-addyosmani-agentic-code-review.md` (the "human on the loop"
    reviewer-posture shift, Claim 11 of that note) — this post's Claim 7
    ("Your name is on the change") is the individual-accountability
    corollary to that note's team/process-level review-posture argument.

- **Novel**:
  - The periodic from-scratch project rebuild as a personal
    finishing-practice (Claim 10) is not covered by any existing corpus
    Osmani note.
  - The "xG and finishing" sports metaphor for separating opportunity
    generation from opportunity conversion (Claim 11) is a new framing
    device not present elsewhere in the corpus.
  - The explicit "this piece grew out of [another author's] original"
    framing is unusual for this corpus's Osmani notes — prior Osmani source
    notes in this corpus are original synthesis pieces; this one is
    self-described as a derivative/extension of a third party's idea (see
    Extraction Notes).

## Guide Impact

- **Chapter 00 (Principles)**: Add "choosing what to build and judging if
  it's good" as a named durable-skill principle, citing this source's
  Claim 2 and Claim 13, and cross-reference it as the individual-career
  extension of the existing intent-debt principle already sourced from
  `blog-addyosmani-intent-debt.md` — both argue the scarce input is
  now human judgment/intent rather than implementation ability.

- **Chapter 01 (Daily Workflows)**: Add the deliberate-practice routine
  (Claim 4: solve some problems manually, read far more than you write,
  treat every diff like a review, keep a daily private log of agent
  mistakes) as a concrete, adoptable habit, citing this source and
  cross-referencing `blog-ghuntley-miami-hot-takes.md` Claim 13 for
  independent corroboration of the same underlying practice from a
  different author.

- **Chapter 02 (Harness Engineering)**: Add "autonomy as a per-task
  setting, not a fixed rank" (Claim 5) as a human-side delegation principle
  to pair with the existing tooling-level autonomy-dial content already
  sourced from `blog-cursor-agent-autonomy-auto-review.md` — note for the
  Smith that these two sources use opposite words ("switch" vs. "dial") for
  compatible ideas, so guide text should pick one term and note the
  synonymy rather than presenting them as competing frameworks.

- **Chapter 03 (Verification)**: Add the "verification, not evidence...
  not an agent grading its own homework" framing (Claim 6) as an
  individual-practice complement to the existing generator/evaluator
  harness-architecture content from `blog-anthropic-harness-long-running.md`,
  and add "your name is on the change" (Claim 7) as the accountability
  framing for why verification is not optional, citing this source
  alongside the independently-sourced `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`
  Claim 7 for a stronger, dual-sourced citation.

- **Chapter 05 (Team Adoption)**: Add the 70/30 "sprint the last mile"
  framing (Claim 9) as a talking point for how teams should set
  expectations and evaluate individual contribution once agents handle the
  median case, citing this source while flagging (per Claim 9's assessment)
  that the specific 70/30 split is an unaudited personal estimate, not a
  benchmark figure, unlike the named third-party datasets already cited via
  `blog-addyosmani-agentic-code-review.md`.

## Extraction Notes

- WebFetch's summarization mode initially declined to reproduce article
  text verbatim (citing copyright) and only offered short quotes plus
  paraphrase. To get exact, verifiable quotes, the full page was fetched
  directly with `curl` and stripped of HTML tags with a small Python
  script (regex tag-strip + `html.unescape`), following the same approach
  documented in this corpus's `blog-addyosmani-intent-debt.md` and
  `blog-addyosmani-loop-engineering.md` extraction notes. All quotes above
  were copied from that raw-text extraction, not from the WebFetch summary.
- This is a short (~1,500 word), single-page post with no internal
  sub-pages of its own. It ends with two outbound links: one to Phil
  Chen's original post (a single X/Twitter status URL, not a substantive
  article page — not independently fetched, consistent with MINER.md's
  guidance to follow "substantive linked pages," which a single tweet is
  not) and one promotional link to the author's own O'Reilly book ("Beyond
  Vibe Coding"), which was not fetched as it is a book advertisement, not a
  linked source, consistent with the pattern already established in
  `blog-addyosmani-intent-debt.md`'s extraction notes for the same book
  link.
- Every claim in this note is anecdotal personal advice/opinion rather than
  measured or third-party-cited evidence (the one exception — the Rich
  Sutton "bitter lesson" attribution in Claim 8 — is itself used as an
  analogy, not as direct evidentiary support). `confidence_overall` is set
  to `anecdotal` accordingly, distinct from this corpus's other Osmani
  notes (mostly rated `emerging`), which synthesize named third-party
  datasets or first-party practitioner accounts.
- Cross-references to `blog-cursor-agent-autonomy-auto-review.md`,
  `blog-ghuntley-miami-hot-takes.md`, `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`,
  `blog-anthropic-ai-native-engineering-org.md`, `blog-addyosmani-intent-debt.md`,
  and `blog-addyosmani-agentic-code-review.md` were all verified by reading
  the cited claim numbers directly in those source-note files before
  writing this note; no claim numbers were guessed.
- No contradiction with an existing corpus note was found that would
  warrant filing a contradiction issue per MINER.md 4a (see Cross-References
  → Contradicts for the one surface-level terminology difference
  considered and ruled out).
