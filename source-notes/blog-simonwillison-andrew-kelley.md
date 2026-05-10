---
source_url: https://simonwillison.net/2026/Apr/30/andrew-kelley/
source_type: blog-post
title: "A quote from Andrew Kelley"
author: Andrew Kelley (Zig creator), quoted by Simon Willison
date_published: 2026-04-30
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: anecdotal
issue: "#571"
---

# A Quote from Andrew Kelley: LLM Detection and "Digital Smell"

> Andrew Kelley (creator of Zig) asserts from his experience as an active OSS
> maintainer that experienced reviewers can detect LLM-assisted contributions
> through a distinctive "digital smell" — a perceptual asymmetry where non-users
> identify agentic patterns that users themselves cannot see — and frames Zig's AI
> ban as a project-scope house rule, not a prohibition on personal use.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, "quotation" format — Willison
  collected and posted the quote without adding his own commentary; the analytical
  payload is entirely in Kelley's 96-word statement)
- **Author credibility**: Andrew Kelley is the creator of the Zig programming
  language and a prominent figure in systems programming. He speaks from direct
  experience reviewing PRs submitted to a major open-source project. This is a
  first-person practitioner account from someone in the maintainer role, not a
  researcher or vendor. Simon Willison is one of the highest-signal LLM tooling
  commentators; his selection of this quote is itself a signal of relevance.
- **Scope**: Covers three distinct claims: (1) experienced maintainers can detect
  LLM-assisted contributions; (2) LLM hallucinations and human mistakes have
  fundamentally different signatures; (3) agentic practitioners exhibit a "digital
  smell" that is obvious to non-users but invisible to themselves. Does NOT cover
  detection methodology in detail, the Zig project's AI policy rationale (covered
  in `blog-simonwillison-zig-anti-ai.md`), or quantitative measurements. This is a
  brief, high-density quotation, not a technical analysis.

## Extracted Claims

### Claim 1: The belief that LLM use in open-source contributions is undetectable is a misconception — experienced maintainers can and do identify LLM-assisted PRs

- **Evidence**: First-person account from Andrew Kelley, speaking as a Zig project
  maintainer who has been actively reviewing LLM-assisted PRs "over the past few
  months." The claim is grounded in direct experience, not theory.
- **Confidence**: anecdotal (one practitioner, no measurements, no inter-rater
  reliability data)
- **Quote**: "It's a common misconception that we can't tell who is using LLM and
  who is not."
- **Our assessment**: Kelley is not speculating about whether detection is
  theoretically possible — he is reporting that he has been doing it. The claim
  does not assert perfect accuracy ("I'm sure we didn't catch 100%"), only that
  the "can't tell at all" belief is wrong. The guide should present this as
  practitioner evidence that detection capability exists, while noting it is not
  infallible.

### Claim 2: LLM hallucinations and human mistakes have fundamentally different signatures, making them distinguishable

- **Evidence**: Kelley's direct statement from his maintainer experience. Human
  errors tend to be consistent with the author's knowledge gaps; LLM hallucinations
  are confident assertions about things that don't exist, exhibiting a qualitatively
  different pattern.
- **Confidence**: anecdotal (one practitioner's characterization; no empirical
  studies cited)
- **Quote**: "the kind of mistakes humans make are fundamentally different than LLM
  hallucinations, making them easy to spot"
- **Our assessment**: The "easy to spot" claim is stronger than the evidence
  supports — it reflects Kelley's subjective experience, not a calibrated precision/
  recall measurement. But the directional claim (the signatures differ) is credible
  and consistent with what is known about LLM failure modes. This has direct
  implications for code review practice: reviewers can develop pattern recognition
  for LLM error signatures in the same way they develop pattern recognition for
  common human error types.

### Claim 3: Practitioners of agentic coding exhibit a "digital smell" — a recognizable perceptual pattern in their work

- **Evidence**: Kelley's assertion from his maintainer experience; the cigarette
  smoke analogy provides the illustrative support.
- **Confidence**: anecdotal
- **Quote**: "people who come from the world of agentic coding have a certain
  digital smell that is not obvious to them but is obvious to those who abstain"
- **Our assessment**: The "digital smell" concept is specific: it is not that
  LLM-generated code is always lower quality, but that it has a recognizable
  pattern — a style, a structure, a distribution of decisions — that trained
  reviewers can identify. The "code smell" term in software engineering refers to
  surface-level indicators of deeper design problems; Kelley's "digital smell"
  extends this to mean a surface-level indicator of *process* (agentic generation).
  This is more than quality assessment — it is a claim about process inference from
  artifact examination.

### Claim 4: The "digital smell" is an asymmetric signal — observable to non-users, invisible to the practitioners who exhibit it

- **Evidence**: Kelley's statement; the smoker analogy provides the intuitive
  support (smokers habituate to the smell and lose the ability to detect it
  themselves).
- **Confidence**: anecdotal
- **Quote**: "not obvious to them but is obvious to those who abstain"
- **Our assessment**: This asymmetry is the sharpest part of the observation. If
  true, it means practitioners using agentic tools are in a systematically worse
  position to self-assess whether their work is detectable. Just as a smoker cannot
  smell themselves, an agentic coder may review their own work and see it as clean
  while still leaving markers others can perceive. For the guide, this has direct
  implications for self-review practices and peer review protocols in AI-native
  teams: engineers cannot rely solely on their own judgment about whether their
  agentic-generated output is distinguishable.

### Claim 5: LLM-assisted PR detection at the Zig project was active but imperfect — not all LLM-assisted PRs were caught

- **Evidence**: Kelley's explicit qualifier, framed as epistemic humility about a
  capability he is otherwise asserting.
- **Confidence**: anecdotal
- **Quote**: "I'm sure we didn't catch 100% of LLM-assisted PRs over the past few
  months"
- **Our assessment**: This qualifier is important for calibration. Kelley is not
  claiming that experienced reviewers can perfectly identify all LLM-assisted
  contributions. The actual operating point is somewhere between "can never detect"
  (the misconception he is correcting) and "always detect." For the guide: the
  correct framing is "detection is real but imperfect" rather than "you can always
  tell." This also has enforcement implications: projects with AI bans should
  expect that the ban will be imperfectly enforced through detection alone.

### Claim 6: Kelley frames Zig's AI contribution policy as a project-scope house rule, not a prohibition on personal use

- **Evidence**: The closing statement of the quote, and the structure of the analogy.
- **Confidence**: anecdotal (one person's framing of one project's policy)
- **Quote**: "I'm not telling you not to smoke, but I am telling you not to smoke
  in my house."
- **Our assessment**: This framing is softer than the Zig Code of Conduct language
  ("No LLMs for issues. No LLMs for pull requests."), which is stated as a flat
  ban. Kelley's personal framing preserves individual agency while establishing a
  project-level boundary. This may be Kelley's diplomatic characterization rather
  than a nuance in the policy itself. For the guide: this formulation — "don't
  bring it here, use it how you like elsewhere" — is a useful template for how
  project-level AI governance can be presented to avoid unnecessary conflict. It
  frames the policy as a project-scope commitment, not a personal moral judgment.

## Concrete Artifacts

### Full verbatim quote from Andrew Kelley, Creator of Zig

```
It's a common misconception that we can't tell who is using LLM and who is not.
I'm sure we didn't catch 100% of LLM-assisted PRs over the past few months, but
the kind of mistakes humans make are fundamentally different than LLM hallucinations,
making them easy to spot. Furthermore, people who come from the world of agentic
coding have a certain digital smell that is not obvious to them but is obvious to
those who abstain. It's like when a smoker walks into the room, everybody who
doesn't smoke instantly knows it.

I'm not telling you not to smoke, but I am telling you not to smoke in my house.
```

*Source: Andrew Kelley, Creator of Zig, as quoted by Simon Willison.
URL: https://simonwillison.net/2026/Apr/30/andrew-kelley/ — posted April 30, 2026.*

## Cross-References

- **Corroborates**: `blog-simonwillison-zig-anti-ai.md` Claim 9 — "Practical
  LLM-assisted OSS contributions caused concrete operational harm to the Zig project
  before the ban." That Claim 9 is supported by Loris Cro's account of "worthless
  drive-by PRs full of hallucinations" and "sneakily consulting an LLM" in follow-
  up discussions. Kelley's quote confirms the detection side: the team was actively
  identifying LLM-assisted PRs ("over the past few months") — which is a prerequisite
  for the operational harm account to be credible. Both sources were published the
  same day (April 30, 2026) and together tell the complete story: LLM-assisted PRs
  were arriving, being detected, causing harm, and motivating the formalized ban.

- **Corroborates**: `blog-simonwillison-zig-anti-ai.md` Claim 4 — "LLM assistance
  breaks that completely" (the contributor-development investment loop). Kelley's
  claim that LLM-assisted contributions are detectable is a prerequisite for Cro's
  policy to be operationally enforceable: if the team could not distinguish LLM PRs
  from human PRs, the contributor-poker investment model would still apply regardless.
  Kelley's detection capability is what makes the policy workable in practice.

- **Extends**: `blog-simonwillison-zig-anti-ai.md` — The Zig anti-AI source covers
  *why* Zig has a ban (contributor poker, operational harm) and the formal *policy*
  (CoC language). This source provides the detection evidence: the team has active,
  real-world experience identifying LLM-assisted contributions, and the detection
  mechanism is a recognizable error-signature difference. Together these two sources
  provide a complete practitioner account from the Zig project: detection is real
  (Kelley), policy is justified (Cro/Willison), policy is enforceable (Kelley's
  detection experience).

- **Extends**: `discussion-hn-agentic-coding-jobs.md` Claim 8 — that claim notes
  "The failure modes of agent-written code are still poorly understood." Kelley's
  account adds the maintainer-detection perspective: practitioners on the receiving
  end of LLM-assisted code ARE developing pattern recognition for its error
  signatures ("easy to spot"), even if systematic documentation and mitigations
  remain underdeveloped. Detection-by-pattern and formal characterization of failure
  modes are different capabilities; Kelley is describing the former.

- **Novel**:
  - **"Digital smell" as a named concept**: No other source in our corpus names or
    describes the perceptual marker that non-agentic reviewers use to identify
    agentic-generated contributions. This is the first explicit named concept for
    this phenomenon in our corpus.
  - **Asymmetry of perception (Claim 4)**: No existing note characterizes the "not
    obvious to them but obvious to those who abstain" asymmetry — that agentic
    practitioners are worse positioned to assess the detectability of their own work
    than external observers. This has direct implications for self-review and peer
    review design.
  - **First-person maintainer detection testimony**: Our corpus has no other source
    where a named, active open-source maintainer states from direct experience that
    they have been successfully (if imperfectly) detecting LLM-assisted contributions.
    This fills a gap in the evidence base.

## Guide Impact

- **Chapter 02 or Chapter 03 (Code Review Practices in AI-Native Teams)**: Claim 4
  (the asymmetry of "digital smell") should be surfaced as a calibration principle
  for AI-native engineers: practitioners who generate code with agentic tools may be
  systematically unable to assess how that code appears to non-agentic reviewers.
  Practical implication: AI-native teams whose code will be reviewed by non-agentic
  reviewers (open-source maintainers, clients, mixed teams) should build in an
  explicit "outside perspective" review step — the agentic practitioner cannot be
  the sole judge of whether their output is distinguishable.

- **Chapter 02 (Organizational Context — Open-Source Specifically)**: Claims 1–5
  together should anchor any guidance about contributing AI-generated code to
  open-source projects. If a practitioner believes "no one can tell," Kelley's
  first-person refutation is directly relevant. If a project has an AI ban, Claims
  5 and 6 clarify that enforcement is imperfect but real. Pair with
  `blog-simonwillison-zig-anti-ai.md` for the complete picture of why the policy
  exists and how it is operationally sustained.

- **Chapter 03 or Chapter 05 (AI Adoption Perception — Outside Observers)**: Claim
  3 (the "digital smell" concept) should appear in any discussion of how AI-native
  work is perceived outside AI-native teams. The perception is real, it is already
  happening, and it may affect team dynamics in mixed (agentic/non-agentic) contexts.

- **Any section on code review under agentic workflows**: The detection-is-real-but-
  imperfect framing (Claims 1 and 5 together) is the correct calibration for setting
  expectations. Neither "you can always tell" nor "you can never tell" is right.
  Kelley's evidence puts the operating point in between, with the error-signature
  difference as the key discriminator.

## Extraction Notes

The source is Simon Willison's "quotation" format — a very brief post (the page
content is approximately 200 words including navigation) that presents a single
quote from Andrew Kelley. Willison added no commentary of his own; the page tags
only (ai, zig, generative-ai, llms). The analytical payload is entirely in Kelley's
96-word statement.

The page was fetched via `curl` to get raw HTML, then text-extracted with an HTML
parser. The verbatim quote in the Concrete Artifacts section was verified
character-for-character against the extracted text. All claim quotes are substrings
of the verbatim quote above; no reconstruction or paraphrase is used in any Quote
field.

The original channel where Kelley made this statement is not cited on the Willison
page. It may have originated from the Ziggit forum or another channel during the
April 30, 2026 Zig AI ban discussions. No upstream source was reachable from the
Willison page.

This source was published the same day as `blog-simonwillison-zig-anti-ai.md`
(April 30, 2026). The Prospector correctly noted these as complementary: the Zig
anti-AI source covers the *why* of the ban; this source covers the *how* of
detection enforcement. No contradiction issue was filed. The closest potential
tension — Kelley's "easy to spot" claim vs. `discussion-hn-agentic-coding-jobs.md`
Claim 8 ("failure modes poorly understood") — was assessed as a non-contradiction:
detection by pattern recognition and formal characterization of failure modes are
different capabilities; both claims can be simultaneously true.
