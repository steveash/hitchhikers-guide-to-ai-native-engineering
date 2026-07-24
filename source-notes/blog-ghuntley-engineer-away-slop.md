---
source_url: https://ghuntley.com/slop/
source_type: blog-post
title: "engineer away the slop"
author: Geoffrey Huntley
date_published: 2026-07-24
date_extracted: 2026-07-24
last_checked: 2026-07-24
status: current
confidence_overall: anecdotal
issue: "#2200"
---

# engineer away the slop

> A short personal-blog post in which Geoffrey Huntley announces he is joining
> Antithesis and lays out an unevidenced hypothesis that formal
> verification/deterministic system testing, adversarial LLM code review, and
> pre-commit-hook-driven language analyzers are about to combine into
> "software factories" that let people/agents ship reliable software without
> deep verification expertise — framed as personal prediction, not
> data-backed argument, and disclosed alongside a material conflict of
> interest (he is joining the vendor whose product category he is endorsing).

## Source Context

- **Type**: blog-post (personal blog, ghuntley.com, published 24 Jul 2026,
  the same day this issue was filed). Very short — roughly 230 words of body
  text plus an embedded bookmark-card link and a subscribe-newsletter
  footer. Framed as a first-person career announcement followed by a
  numbered-paragraph hypothesis, not an argued essay with citations or data.
- **Author credibility**: Geoffrey Huntley is the same author as
  `blog-ghuntley-miami-hot-takes.md` (already in this corpus). This post
  itself is the source of a disclosed conflict of interest: its central
  hypothesis is that formal verification and deterministic system testing
  are "about to cross the chasm," and in the same breath the author reveals
  he is "joining the folks over at antithesis.com" — Antithesis being a
  company that sells exactly this category of deterministic-testing
  tooling. No data, named customer, benchmark, or third party is cited
  anywhere in the post; every claim is a bare first-person assertion,
  explicitly framed by the author as "Here's my hypothesis."
- **Scope**: Covers (1) Huntley's own career move to Antithesis; (2) a claim
  that the software profession has changed more in the last six months than
  in the prior 30 years; (3) a specific one-line definition of "engineer" as
  a discipline where failures are unacceptable; (4) a callback to a named
  prior talk (AI Engineer World's Fair) about a coming "Eternal September";
  and (5) a four-part hypothesis — formal verification/deterministic testing
  + adversarial LLM code review + pre-commit-hook language analyzers as
  components of "software factories." Does NOT cover: any case study,
  benchmark, or named company besides the author's own new employer; a
  definition of "language analyzers" beyond the phrase itself; or any detail
  of what Antithesis's product actually does mechanically (that detail
  exists only in a separately-authored page this post links to — see
  Claim 12 and Extraction Notes).

## Extracted Claims

### Claim 1: Huntley predicted in November 2024 that the software profession would change, and asserts it has changed more in the last six months than in the preceding thirty years

- **Evidence**: Bare first-person assertion, no supporting data or named
  events beyond the timeframes themselves.
- **Confidence**: anecdotal
- **Quote**: "If I wind back time to November 2024, it was apparent to me back then that our profession would change. To be frank, in the last six months our profession has changed more than it has in the last 30 years."
- **Our assessment**: An unfalsifiable comparative claim — no metric is given for "how much a profession has changed," so the six-months-vs-thirty-years comparison cannot be checked against anything. Read as scene-setting for the post's real argument (Claims 6-10) rather than as a claim to carry weight on its own.

### Claim 2: Software authoring has been commoditized — everyone is now a software developer, but being a developer does not make someone an engineer

- **Evidence**: Bare first-person assertion.
- **Confidence**: anecdotal
- **Quote**: "Software authoring has been commoditised. Everyone is now a software developer, but being a software developer does not mean that they're an engineer."
- **Our assessment**: This restates the coder/engineer distinction already extracted from this same author's earlier post — see `blog-ghuntley-miami-hot-takes.md` Claim 2 ("Anyone can use Cursor or any other tool and generate code. Being a coder and being a software engineer are different.") and Claim 3 (the "gated vs. malleable" framing). This post adds no new argument for the distinction itself, but Claim 3 below gives it a sharper operational definition than either claim in the Miami post supplied.

### Claim 3: "Engineer" specifically means a discipline in which failures are unacceptable, a standard borrowed from other engineering professions but used only loosely in software

- **Evidence**: Bare first-person assertion, contrasting software's trivial use of the word "engineer" against other engineering disciplines' stricter usage.
- **Confidence**: anecdotal
- **Quote**: "The word engineer is used trivially in our profession, but in other industries the word engineer means failures are unacceptable."
- **Our assessment**: This is the most operationally specific content in the post's engineer/developer distinction — more concrete than the Miami post's Claim 4 ("If you cannot demonstrate how a coding agent works, you are just a consumer..."), which gates on *understanding a mechanism* rather than on *an outcome standard*. The two are compatible (understanding-of-mechanism could be one path to achieving zero-defect outcomes) but this post names the bar as an outcome ("failures are unacceptable"), not a competency test. Neither post operationalizes how "failures are unacceptable" would be measured for software specifically, so this remains an aspirational definition, not a testable one.

### Claim 4: Huntley is concerned the industry is entering another "Eternal September" because too few software engineers were trained after the dot-com implosion to sustain an apprenticeship model of learning

- **Evidence**: First-person assertion referencing a named prior talk (AI Engineer World's Fair) where the author says he raised the same concern.
- **Confidence**: anecdotal
- **Quote**: "If you caught my talk at the AI Engineer World Fair, one of the things I shared was some deep concerns that we are entering into another Eternal September. You see, we didn't create enough software engineers after the 2000s dot-com implosion to properly support an apprenticeship model of learning in our industry."
- **Our assessment**: No data is given for "we didn't create enough software engineers after the dot-com implosion" — it is a historical claim asserted without a source. It is, however, a distinct causal mechanism from the "apprenticeship crisis" already documented with much stronger, multi-session corroboration in `blog-fowler-fragments-2026-07-21.md` Claim 6 (Thoughtworks retreat report: "Independently, in at least six different sessions, senior practitioners..." raised an apprenticeship/skills-transmission crisis). That report's mechanism is *current*: juniors losing hands-on exposure because agents (or seniors pairing exclusively with agents) absorb the work. Huntley's mechanism here is *historical*: a shortage of senior mentors left over from a prior industry contraction, now compounding as everyone can "create software" per Claim 2. The two claims point at the same named phenomenon (apprenticeship breakdown) via different, non-contradictory causal stories — worth citing together, not treating as duplicates.

### Claim 5: Despite the changes described in Claims 1-4, the core job of a software engineer remains producing experiences without defects

- **Evidence**: Bare first-person assertion, presented as the stable premise the rest of the post's hypothesis is built on.
- **Confidence**: anecdotal
- **Quote**: "It's now twenty-six years since that event, and now that everyone can create software, we've got some hard questions to solve. But whilst many things have changed, the job of software engineers is to produce experiences without defects."
- **Our assessment**: This restates Claim 3's "failures are unacceptable" standard as a job description rather than a definition of the word "engineer." Taken together, Claims 3 and 5 are the premise that makes the rest of the post's hypothesis (Claims 6-10) matter to the author: if the standard for "engineer" is zero defects, and everyone can now produce code, then verification capacity — not authoring capacity — is the thing that must scale.

### Claim 6: Formal verification and deterministic system testing are "about to cross the chasm" because a large volume of brownfield software is being hit all at once by an "infinite software crisis" of unmanageable code-review volume

- **Evidence**: Bare first-person hypothesis, explicitly labeled as such by the author ("Here's my hypothesis").
- **Confidence**: anecdotal (self-labeled hypothesis; no data, case study, or named company given)
- **Quote**: "The discipline/techniques of formal verification and deterministic system testing are about to cross the chasm. There's a whole lot of brownfield software out there that's been written over the last 30 years that is being affected by the infinite software crisis (“how do we do code review now?” / “the volume of code/change is too high”) all at once."
- **Our assessment**: The specific phrase "infinite software crisis" is new to this corpus, but the underlying claim — that verification, not code generation, is now the binding constraint — is independently and much more strongly corroborated elsewhere: `blog-fowler-fragments-2026-07-21.md` Claim 1 ("Code generation is no longer the bottleneck — verification is," a Thoughtworks retreat headline finding) and `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("The bottleneck is no longer generation. It's verification.") both state the identical thesis with more institutional backing (a named multi-session industry retreat; a separate practitioner's independent synthesis) than this post supplies on its own. This post's contribution is not new evidence for the thesis — it's a compact, named framing ("crossing the chasm," "infinite software crisis") applied specifically to formal verification/deterministic testing as the proposed remedy.

### Claim 7: Not enough skilled practitioners exist in the disciplines of formal verification and deterministic system testing

- **Evidence**: Bare first-person assertion, no data (e.g., no headcount estimate, survey, or job-market figure).
- **Confidence**: anecdotal
- **Quote**: "Not enough skilled practitioners in the discipline/techniques of formal verification and deterministic system testing exist."
- **Our assessment**: This is the stated reason the post's hypothesis (Claim 9) frames Antithesis-style tooling as valuable specifically because it lets "people/agents" work without acquiring this specialized knowledge themselves — the claim functions as a premise for Claim 9, not as an independently supported fact. No corpus source currently quantifies the supply of formal-verification practitioners, so this remains an unverified premise.

### Claim 8: Building a deterministic simulator for a project is now significantly cheaper than before, and doing so surfaces whole categories of bugs that will not otherwise appear

- **Evidence**: Bare first-person assertion.
- **Confidence**: anecdotal
- **Quote**: "Whilst the costs of building a simulator for a project (new or retrofitting an existing project) are significantly cheaper now, there are entire categories and classes of problems that will not surface unless you emulate a deterministic computer (which provides a forceful way to make anything deterministic)."
- **Our assessment**: No mechanism is given for *why* simulator-building costs have dropped (the implicit link is that AI coding tools make building the simulator itself cheaper, but this is not stated explicitly). The claim that some bug classes require deterministic emulation to surface at all is corroborated with far more mechanism-level detail by `blog-anthropic-datadog-temper-machine-tool.md` Claim 9, which documents a live, named four-layer verification cascade (symbolic reasoning, exhaustive state exploration, deterministic fault-injected simulation, randomized property testing) built specifically because "there is no drift between what was verified and what is running" (Claim 8 of that same note). That note supplies the production case study this post asserts only in the abstract.

### Claim 9: Antithesis, adversarial LLM code review, and pre-commit-hook-driven language analyzers together will be a key component of "software factories" that let people/agents deliver reliable software without needing specialized formal-verification knowledge

- **Evidence**: Bare first-person hypothesis, naming a specific product (Antithesis, the company the author is joining) alongside two general techniques (LLM code review, language analyzers).
- **Confidence**: anecdotal (a named-vendor hypothesis with a disclosed conflict of interest; no case study or measurement given in this post)
- **Quote**: "Antithesis, when used in conjunction with adversarial code reviews by an LLM and with language analyzers driven by pre-commit hooks, will be a key component in software factories that enables people/agents to deliver reliable software without the burden of having to learn this specialized knowledge."
- **Our assessment**: Each of the three named components already has stronger, independent corpus evidence than this post supplies for the combination: adversarial LLM code review has a concrete, measured production case in `blog-simonwillison-rewriting-bun-rust.md` Claim 3 (Sumner's own summary: "a language-independent test suite with a million assertions, adversarial code review and when something does go wrong, fixing the process that generates the code") and `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7 (the specific harness: "one Claude instance implements, two independent Claude instances... try to find bugs, and a fourth applies the accepted feedback"). Pre-commit-hook-driven language analyzers have a concrete, sustained production case in `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 1 (35+ custom Go analyzers maintained via a three-workflow discover/challenge/apply loop). What is genuinely new here is not any individual component but the *named triad* — formal/deterministic verification tooling + LLM adversarial review + automated language analyzers — proposed as one integrated "software factory" component in a single sentence, from a source with a direct financial stake in one of the three named things succeeding. The guide should treat this compact framing as a hypothesis worth testing against the corpus's more detailed individual case studies, not as an independent data point for the combination itself.

### Claim 10: The central thesis of the post — creation is now near-free, but verification and understanding are not yet — is offered as the reason to "engineer away the slop"

- **Evidence**: Bare first-person assertion, presented as the post's closing thesis statement.
- **Confidence**: anecdotal
- **Quote**: "Creation is now near-free. Verification/understanding is not, yet. It's time to engineer away the slop."
- **Our assessment**: This is a compact, quotable restatement of the same verification-bottleneck thesis already well established in the corpus (see Claim 6's assessment). Its "not, yet" qualifier is notable: it frames verification cost as a temporary state expected to fall (consistent with Claim 9's hypothesis that tooling like Antithesis will close the gap), rather than as a permanent structural constraint — a more optimistic framing than, e.g., `blog-addyosmani-software-factories-light-dark.md` Claim 5's "back pressure" rule, which treats the verification bottleneck as a durable autonomy-budgeting constraint rather than a temporary gap tooling will close.

### Claim 11: Huntley discloses he is joining Antithesis, the company whose product category (deterministic system testing / formal verification) is the centerpiece of this post's hypothesis

- **Evidence**: First-person disclosure, stated as the post's opening line.
- **Confidence**: anecdotal (self-disclosed fact about the author, not a claim about the industry)
- **Quote**: "I'm not going to bury the lede here; the short TLDR is I'm joining the folks over at https://antithesis.com/."
- **Our assessment**: This is a material conflict of interest the author discloses transparently rather than hides, which is to the post's credit, but it means Claims 6-10 (all of which endorse formal verification/deterministic testing, and Claim 9 specifically names Antithesis) should be read as a new hire's account of why he joined the company, not as an independent industry assessment. The guide should attribute this post's endorsement of Antithesis specifically as disclosed-COI opinion if cited at all.

### Claim 12: Antithesis's deterministic hypervisor does not just make bugs reproducible — it is also the mechanism that helps the system find bugs in the first place, demonstrated by an unassisted platform autonomously beating Super Mario Bros. in about 45 minutes

- **Evidence**: This claim is authored by Will Wilson, Antithesis co-founder & CEO, in a separately-authored Antithesis company blog post ("How Antithesis finds bugs (with help from the Super Mario Bros.)," April 17, 2024) that Huntley's post links to as an embedded bookmark card, immediately following the paragraph that introduces Antithesis by name. Followed per MINER.md §1 as a substantive linked page, not part of Huntley's own claims.
- **Confidence**: anecdotal (single-vendor self-description of its own product, no independent benchmark or third-party verification found in this extraction)
- **Quote**: "our deterministic hypervisor isn't just about getting perfect reproducibility of the bugs we find, it also helps us find the bugs in the first place." Also: "Antithesis can find this solution in about forty-five minutes on a 2018-era workstation CPU. The only hints our platform received were the locations in memory that hold Mario's X and Y coordinates in a level, and which level he's on."
- **Our assessment**: This is useful mechanism-level context for what "deterministic system testing" (Claim 6) and "emulate a deterministic computer" (Claim 8) actually mean in Antithesis's own telling: a hypervisor that makes a system's execution fully reproducible, which in turn enables autonomous, efficient exploration of that system's state space to find bugs (not just replay them). It is vendor self-description, attributed here to Wilson/Antithesis rather than to Huntley, and should not be conflated with Huntley's own claims in this note.

## Concrete Artifacts

### Full body text, verbatim (`ghuntley.com/slop/`, by Geoffrey Huntley, 24 Jul 2026)

```
Source: Geoffrey Huntley, "engineer away the slop", ghuntley.com, 24 Jul 2026.

It's been a busy six months, that's for sure. I'm not going to bury the
lede here; the short TLDR is I'm joining the folks over at
https://antithesis.com/.

If I wind back time to November 2024, it was apparent to me back then that
our profession would change. To be frank, in the last six months our
profession has changed more than it has in the last 30 years. Software
authoring has been commoditised. Everyone is now a software developer, but
being a software developer does not mean that they're an engineer.

The word engineer is used trivially in our profession, but in other
industries the word engineer means failures are unacceptable.

Now I'm a little bit old and crusty these days; I turn 44 next week, and
I've seen some absolutely horrible codebases, but if I'm to be honest, I
can remember some of the first code that I wrote, and I have regrets. If
you caught my talk at the AI Engineer World Fair, one of the things I
shared was some deep concerns that we are entering into another Eternal
September. You see, we didn't create enough software engineers after the
2000s dot-com implosion to properly support an apprenticeship model of
learning in our industry.

It's now twenty-six years since that event, and now that everyone can
create software, we've got some hard questions to solve. But whilst many
things have changed, the job of software engineers is to produce
experiences without defects.

So I've been pondering how we are going to fix this predicament.

Here's my hypothesis:

The discipline/techniques of formal verification and deterministic system
testing are about to cross the chasm. There's a whole lot of brownfield
software out there that's been written over the last 30 years that is
being affected by the infinite software crisis ("how do we do code review
now?" / "the volume of code/change is too high") all at once.

Not enough skilled practitioners in the discipline/techniques of formal
verification and deterministic system testing exist.

Whilst the costs of building a simulator for a project (new or
retrofitting an existing project) are significantly cheaper now, there are
entire categories and classes of problems that will not surface unless you
emulate a deterministic computer (which provides a forceful way to make
anything deterministic).

Antithesis, when used in conjunction with adversarial code reviews by an
LLM and with language analyzers driven by pre-commit hooks, will be a key
component in software factories that enables people/agents to deliver
reliable software without the burden of having to learn this specialized
knowledge.

Creation is now near-free. Verification/understanding is not, yet. It's
time to engineer away the slop.

[Embedded bookmark-card link: "How Antithesis finds bugs (with help from
the Super Mario Bros.) | Antithesis" -- Will Wilson, Co-founder & CEO]
```

(Fetched via `curl` with a browser user-agent and converted from raw HTML
with a Python stdlib tag-stripping pass, not a summarizing fetch tool, so
the above is verified character-for-character against the live page as of
2026-07-24, including the exact quotation marks used around the two
"infinite software crisis" sub-phrases.)

### Excerpt from the linked Antithesis post, verbatim (`antithesis.com/blog/sdtalk/`, by Will Wilson, 17 Apr 2024)

```
Source: Will Wilson, Co-founder & CEO, "How Antithesis finds bugs (with
help from the Super Mario Bros.)", antithesis.com, 17 Apr 2024. Linked
directly from ghuntley.com/slop/ as an embedded bookmark card.

"We're publishing it now because it answers one of the most common
questions we get: how exactly does Antithesis explore the state spaces of
complex systems, and how does it find bugs so quickly? It also explains
something Alex alluded to in his post: our deterministic hypervisor isn't
just about getting perfect reproducibility of the bugs we find, it also
helps us find the bugs in the first place."

"Antithesis can find this solution in about forty-five minutes on a
2018-era workstation CPU. The only hints our platform received were the
locations in memory that hold Mario's X and Y coordinates in a level, and
which level he's on."

"Super Mario Bros. is a simple game, but its state space is inconceivably
vast. As far as we know, we're the first autonomous system to explore that
state space efficiently enough to beat the game (albeit with one or two
hints)."
```

## Cross-References

- **Corroborates**:
  - `blog-fowler-fragments-2026-07-21.md` Claim 1 ("Code generation is no
    longer the bottleneck — verification is," a Thoughtworks retreat
    headline finding) — independently corroborates the core premise behind
    Claims 6 and 10 here, with far more institutional weight (a named
    multi-session industry retreat report) than this post supplies on its
    own.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("The bottleneck is
    no longer generation. It's verification.") — a second, independent
    practitioner stating the identical thesis Claim 6/10 here rest on.
  - `blog-addyosmani-software-factories-light-dark.md` Claim 5 ("Back
    pressure... Verification, not generation, is the real constraint on a
    factory") and Claim 1 (the loop/harness/factory stack, "software
    factory" as a named term) — Huntley's post uses the identical term
    "software factories" (Claim 9) for the same underlying pattern,
    independently of Osmani, though Huntley's usage is a single unglossed
    noun phrase while Osmani's post supplies the full structural definition
    Huntley's does not.
  - `blog-simonwillison-rewriting-bun-rust.md` Claim 3 and
    `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7 — a concrete,
    already-shipped production case of exactly the "adversarial code
    reviews by an LLM" component named in Claim 9 here, including the
    specific harness mechanism (one implementer instance, two adversarial
    reviewer instances, one integrator instance) this post only names in
    the abstract.
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 1 — a concrete,
    already-shipped production case of "language analyzers driven by
    pre-commit hooks" (Claim 9 here), documenting 35+ custom analyzers
    maintained via a continuous discover/challenge/apply loop.
  - `blog-anthropic-datadog-temper-machine-tool.md` Claim 9 (a four-layer
    verification cascade: symbolic reasoning, exhaustive state exploration,
    deterministic fault-injected simulation, randomized property testing) —
    the most detailed existing corpus example of "formal verification and
    deterministic system testing" (Claim 6/8 here) actually running in
    production, supplying mechanism detail this post asserts only in the
    abstract.
  - `blog-fowler-fragments-2026-07-21.md` Claim 6 (an "apprenticeship
    crisis" independently raised in at least six Thoughtworks retreat
    sessions) — corroborates the *phenomenon* named in Claim 4 here (an
    apprenticeship/mentorship breakdown), though via a different causal
    mechanism; see Claim 4's assessment for why these are complementary
    rather than duplicate claims.
  - `blog-ghuntley-miami-hot-takes.md` Claims 2-4 (same author's earlier
    post on the coder/engineer distinction) — Claim 2 and Claim 3 here
    restate and sharpen that distinction with an outcome-based definition
    of "engineer" ("failures are unacceptable") that the Miami post did not
    supply.

- **Contradicts**: None found requiring a contradiction filing under
  MINER.md §4a. The post's claims are broad, self-labeled hypotheses from a
  single practitioner with a disclosed financial stake in one of the named
  components (Antithesis), rather than specific, falsifiable positions that
  clash with an existing source note's specific claim. The closest tension
  is between Claim 10's "not, yet" framing (implying the verification gap
  is temporary and closing) and `blog-addyosmani-software-factories-light-dark.md`
  Claim 5's "back pressure" rule, which treats the generation/verification
  gap as a durable, structural autonomy-budgeting constraint rather than a
  gap that tooling will simply close over time. This is a difference in
  outlook/emphasis between two practitioners, not a specific factual claim
  in one that a specific factual claim in the other directly refutes, so it
  does not meet the MINER.md §4a filing bar.

- **Extends**:
  - `blog-ghuntley-miami-hot-takes.md` — extends the coder/engineer
    distinction from that post with an operational, outcome-based
    definition of "engineer" (Claim 3 here) and a proposed technical
    remedy (Claims 6-9) that the Miami post, being a list of unelaborated
    hot takes, did not attempt.
  - The linked Antithesis post (Will Wilson, `antithesis.com/blog/sdtalk/`)
    — supplies the mechanism-level detail (a deterministic hypervisor
    enabling both reproducibility and efficient state-space exploration)
    behind the phrase "emulate a deterministic computer" that Huntley's
    post uses without elaboration (Claim 8/12).

- **Novel**:
  - The specific phrase "infinite software crisis" for the volume/velocity
    mismatch between code-change volume and available code-review capacity
    (Claim 6) is not present elsewhere in the corpus under this name,
    though the underlying phenomenon is well documented (see Corroborates).
  - The named triad — formal/deterministic verification tooling +
    adversarial LLM code review + pre-commit-hook language analyzers — as
    three components proposed to combine into one "software factory"
    component in a single sentence (Claim 9) is new; each component
    individually already has stronger corpus evidence than this post
    supplies for the combination.
  - The outcome-based one-line definition of "engineer" as "failures are
    unacceptable" (Claim 3), contrasted explicitly against software's
    "trivial" use of the word, is a new, quotable formulation not present
    elsewhere in the corpus.
  - The historical "post-dot-com under-hiring caused an apprenticeship gap"
    causal story (Claim 4) is a distinct mechanism from the corpus's
    existing, more current-focused apprenticeship-crisis material (see
    Corroborates).
  - The disclosed conflict of interest itself — a practitioner publicly
    endorsing a technology category in the same post where he discloses
    joining its leading vendor — is a novel piece of context for how the
    guide should weight this specific post's advocacy, distinct from the
    more institutionally-sourced verification-bottleneck claims elsewhere
    in the corpus.

## Guide Impact

- **Chapter 03 (Verification)**: If the guide cites this post at all for
  the verification-bottleneck thesis (Claims 6, 10), it should route
  primary attribution to the stronger, less conflicted sources already in
  the corpus — `blog-fowler-fragments-2026-07-21.md` Claim 1 and
  `blog-addyosmani-code-agent-orchestra.md` Claim 5 — and cite this post
  only for its specific, quotable "infinite software crisis" framing and
  its named-triad hypothesis (Claim 9), explicitly flagged as one
  practitioner's disclosed-COI opinion (Claim 11) rather than independent
  evidence. The guide should pair Claim 9's abstract triad with the
  corpus's concrete case studies for each component: adversarial LLM
  review (`blog-pragmaticengineer-bun-rust-rewrite.md` Claim 7), pre-commit
  language analyzers (`blog-ghaw-custom-linters-three-workflow-loop.md`
  Claim 1), and formal/deterministic verification cascades
  (`blog-anthropic-datadog-temper-machine-tool.md` Claim 9) — so that the
  guide's verification-strategy section rests on the shipped examples, not
  on Huntley's unelaborated abstraction of them.

- **Chapter 05 (Team Adoption — career framing)**: Add Claim 3's
  outcome-based definition of "engineer" ("failures are unacceptable") as a
  sharper companion citation alongside this same author's Miami-post
  coder/engineer distinction (`blog-ghuntley-miami-hot-takes.md` Claims 2
  and 4) — note for the guide that neither post from this author
  operationalizes how "failures are unacceptable" would actually be
  measured for a specific team or codebase.

- **Chapter 05 (Team Adoption — apprenticeship/workforce risk)**: Add
  Claim 4's historical framing (post-dot-com under-hiring reduced the pool
  of senior mentors available now) as a second, distinct causal
  contribution to the apprenticeship-crisis material already documented
  with much stronger multi-session corroboration in
  `blog-fowler-fragments-2026-07-21.md` Claim 6 — cite both together as
  complementary mechanisms (a historical mentor shortage colliding with a
  current agentic-adoption skills-transmission gap), not as duplicate
  evidence for the same claim.

- **Not recommended for inclusion without a conflict-of-interest caveat**:
  Claim 9 (the named Antithesis + LLM review + language-analyzer triad) and
  Claim 10 (the "creation is free, verification is not, yet" tagline)
  should not be cited in the guide as independent industry assessment
  without noting Claim 11's disclosure — the author announces joining
  Antithesis in the same post that argues Antithesis's product category is
  "about to cross the chasm."

## Extraction Notes

- The main post was fetched via `curl` with a browser user-agent and
  converted from raw HTML to plain text with a Python stdlib tag-stripping
  pass, not a summarizing fetch tool, so that every quote above (including
  the exact nested-quotation-mark phrasing around "how do we do code
  review now?" / "the volume of code/change is too high") is checked
  against the live page as of 2026-07-24, rather than reconstructed from a
  paraphrase.
- Per MINER.md §1, one substantively linked page was followed: the
  embedded bookmark-card link to Will Wilson's April 2024 Antithesis blog
  post, "How Antithesis finds bugs (with help from the Super Mario
  Bros.)," which is the only non-navigational, non-newsletter link in the
  post and directly follows the paragraph introducing Antithesis by name.
  That page was likewise fetched via `curl` and stripped to plain text;
  the quotes attributed to Will Wilson above are verified against that
  fetch. The post's other links are site navigation (Home, Lately, Media,
  Workshops, Speaking, Disclosures, Contact), a subscribe/newsletter
  footer, and a "Previous" post link to `ghuntley.com/miami/`, which is
  already covered in depth by the existing `blog-ghuntley-miami-hot-takes.md`
  and was not re-extracted here.
- Confidence is set to `anecdotal` overall: every claim original to this
  post is a first-person, self-labeled hypothesis ("Here's my hypothesis")
  from a single practitioner, with no data, named customer, or benchmark
  behind any individual point, and a disclosed material conflict of
  interest (Claim 11) bearing directly on the post's central technical
  recommendation (Claim 9). This is consistent with the Prospector's own
  triage assessment describing the post's core content as "Huntley's
  perspective" and "hypothesized role of formal verification." Where this
  note cites corpus claims that independently corroborate the underlying
  verification-bottleneck thesis at `emerging` confidence, those citations
  point to the stronger source, not to this post, per the citations in
  Cross-References and Guide Impact above.
- Cross-reference verification: all cited claim numbers were confirmed by
  re-reading the actual source notes before writing this note —
  `blog-fowler-fragments-2026-07-21.md` Claim 1 (line 76: "The Thoughtworks
  retreat report names five headline findings...") and Claim 6 (line 232:
  "The report documents an apprenticeship crisis independently raised in
  at least six sessions...") — verified; `blog-addyosmani-code-agent-orchestra.md`
  Claim 5 (line 53: "The bottleneck has shifted from code generation to
  verification") — verified; `blog-addyosmani-software-factories-light-dark.md`
  Claim 1 (line 59) and Claim 5 (line 143: "Back pressure is the rule that
  a loop can only be granted as much autonomy as can be cheaply and
  reliably verified...") — verified; `blog-simonwillison-rewriting-bun-rust.md`
  Claim 3 (line 101) — verified; `blog-pragmaticengineer-bun-rust-rewrite.md`
  Claim 7 (line 195: "The rewrite's core safety mechanism was an
  adversarial-review harness...") — verified; `blog-ghaw-custom-linters-three-workflow-loop.md`
  Claim 1 (line 27: "Three interconnected workflows—Linter Miner, Sergo,
  and LintMonster—manage 35+ custom Go analyzers...") — verified;
  `blog-anthropic-datadog-temper-machine-tool.md` Claim 9 (line 126:
  "Every Temper specification passes four independent verification
  layers...") — verified; `blog-ghuntley-miami-hot-takes.md` Claims 2-4
  (lines 54, 61, 68) — verified by re-reading the full note (already read
  in full during this extraction).
