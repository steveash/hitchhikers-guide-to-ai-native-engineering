---
source_url: https://mattwood.blog/essays/2026/08/how-this-was-made/
source_type: blog-post
title: "How This Was Made"
author: Matt Wood (Chief AI & Technology Officer, AWS)
date_published: 2026-08-04
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: anecdotal
issue: "#2528"
---

# How This Was Made

> Matt Wood (AWS Chief AI & Technology Officer) argues that organizational AI
> momentum stalls not at the tool-access or use-case-discovery layer but at
> the *spreading* layer — early adopters become isolated champions because
> organizations share finished outputs but never share process — and
> proposes a concrete leadership practice, a short "How This Was Made" note
> appended to shared work describing how AI, judgment, source material, and
> revision combined to produce it, as the mechanism for changing norms
> through observed behavior rather than policy.

## Source Context

- **Type**: blog-post (personal essay site, `mattwood.blog`, "essays"
  collection; short-form, single-author, no comments or citation
  infrastructure; ~1,300 words including a postscript; no images, tables, or
  outbound hyperlinks in the article body — confirmed by inspecting the raw
  HTML's `<a>` tags, which contain only navigation links to the site root).
- **Author credibility**: Matt Wood is AWS's Chief AI & Technology Officer,
  having returned to AWS in 2026 after nearly 15 years there earlier in his
  career and, most recently, leading commercial technology and innovation at
  PwC (per the site's About page, fetched directly). He holds a PhD in
  machine learning and did a postdoctoral fellowship in NLP/bioinformatics at
  Weill Cornell Medicine. This is the same author and site as
  `blog-mattwood-field-and-frontier.md`, `blog-mattwood-half-life-assumption.md`,
  and `blog-mattwood-barcode-bargain.md`; the bio and credibility assessment
  in those notes applies unchanged here (re-verified by re-fetching the About
  page for this extraction — text is identical). As with those essays, this
  is a `trusted-feed` source that has already passed an
  author-worth-listening-to bar, but the piece itself is a
  personal-essay/prescriptive-practice piece, not a data report: it contains
  zero named customer examples, zero benchmarks, zero surveys, and zero
  third-party citations of any kind — every claim is the author's own
  argument, historical analogy, or personal example, not third-party
  evidence.
- **Scope**: Covers the "early adoption concentrates among self-motivated
  champions" diagnosis, the mechanism by which process invisibility blocks
  organizational knowledge transfer, the claim that norms change through
  observed behavior rather than declared policy, the authorship/
  responsibility reframing ("the work is the author's... because they shaped
  it, revised it, and remain responsible for it"), the concrete "How This
  Was Made" note practice (what it should and shouldn't contain, three
  example formats), the requirement that the practice stay informal and
  consistent rather than becoming a measured policy, the Benjamin Franklin
  Junto historical analogy, and a first-person meta-example of the author
  using his own "Writing Room" app with multiple agents to produce the essay
  itself. Does NOT cover: any named company, team, or organization that has
  adopted this practice; any measurement of whether "How This Was Made"
  notes actually change adoption rates or spread speed; any tooling,
  template enforcement, or workflow for collecting these notes at scale; or
  any counter-perspective/rebuttal (single-voice essay, no named
  disagreement addressed).

## Extracted Claims

### Claim 1: Early AI adoption inside organizations concentrates among a small, self-motivated group who become informal champions, and the organizational challenge has shifted from tool access or use-case discovery to spreading what that group already knows through the rest of the organization
- **Evidence**: Author's own diagnosis, presented as an observed pattern across organizations "a year" into AI adoption; no named organization, survey, or count is cited.
- **Confidence**: anecdotal (asserted organizational pattern from an AWS customer-facing executive's vantage point, not backed by a named case or dataset)
- **Quote**: "The challenge isn't getting started, and it isn't tool access or finding use cases, because the champions have already found plenty of those. It is taking what's working in the early group and spreading it through the rest of the organization."
- **Our assessment**: This is the essay's diagnostic starting point and the Prospector's flagged key question. It names a specific, plausible failure mode (momentum concentrating rather than spreading) that the guide's existing Chapter 05 material does not currently address directly — the guide covers *who to pilot with* (seniors first) but not *how the pilot group's knowledge is supposed to reach everyone else*.

### Claim 2: Organizations routinely share finished outputs (decks, memos, reports) but almost never share the process behind them, so how AI contributed to a piece of work stays invisible even as the work itself circulates widely
- **Evidence**: Author's own mechanism argument, no external citation.
- **Confidence**: anecdotal (asserted mechanism, no survey of what organizations actually share)
- **Quote**: "Organizations share outputs constantly: decks, memos, reports, analysis. They almost never share process. The finished document moves from inbox to inbox. How it was made stays invisible."
- **Our assessment**: This is the essay's load-bearing mechanism claim — it locates the spreading failure specifically at the process-visibility layer, not at output quality or tool availability. It is a clean, quotable diagnosis but remains an assertion; the essay gives no example of an organization auditing what fraction of shared work includes any process information.

### Claim 3: Invisible AI involvement in shared work has a specific cost — either people don't realize AI was involved and so don't update their sense of what's possible, or they suspect it was involved but nobody confirms it, which normalizes quiet, unstated use rather than openly shared use
- **Evidence**: Author's own two-branch mechanism, extending Claim 2; no external citation.
- **Confidence**: anecdotal (asserted causal mechanism, no measurement of either branch)
- **Quote**: "Other people see a good piece of work and have no idea that AI contributed to it, so they don't update their sense of what's possible. Or they suspect AI was involved but nobody says so, so the norm becomes quiet use rather than shared use."
- **Our assessment**: This sharpens Claim 2 into a specific failure mode — "quiet use" as the default equilibrium when nobody discloses process — which is a useful, nameable anti-pattern for a guide section on adoption. It is asserted rather than observed in a named organization, but it is internally consistent with Claim 1's champion-concentration diagnosis (the champions have the knowledge; nothing in the shared artifact transmits it).

### Claim 4: Organizational norms change when people observe a change in behavior, not when a policy is announced — a policy encouraging AI use doesn't shift what people do because it doesn't change what they see colleagues and leaders actually doing
- **Evidence**: Author's own definitional/mechanism claim about organizational norm formation; no external citation, study, or named example.
- **Confidence**: anecdotal (asserted mechanism; the underlying idea — norms form from observed behavior, not stated policy — echoes broader social-proof/descriptive-norm concepts in organizational-behavior literature generally, but the essay itself cites no research and offers no measurement)
- **Quote**: "Norms inside organizations change when behavior changes, not when policy changes. A policy that says "AI use is encouraged" doesn't shift what people do because it doesn't shift what they see. People watch what respected colleagues and leaders actually do, and they form their sense of what's normal from those observations."
- **Our assessment**: This is the essay's central causal claim and the reason the recommended practice is behavioral (leaders modeling AI use openly) rather than administrative (writing a policy). It is plausible and consistent with general organizational-change intuition, but the essay presents it as self-evident rather than citing any study of policy-vs-behavior adoption gaps — the guide should treat it as the author's framing device, not a settled finding.

### Claim 5: Authorship and responsibility for AI-assisted work are resolved by who shaped, revised, and remains accountable for the result — not by how many sentences a person personally typed — and making the process visible answers the "does it count as mine?" question with evidence instead of leaving it as an unstated anxiety
- **Evidence**: Author's own definitional argument, framed around a question he says "many people are sitting with quietly."
- **Confidence**: anecdotal (definitional/philosophical claim, not tested against any named organization's authorship dispute or survey of how people actually resolve the question)
- **Quote**: "The work is the author's not because they typed every sentence, but because they shaped it, revised it, and remain responsible for it."
- **Our assessment**: This directly parallels the guide's existing Directly Responsible Individual (DRI) framing in Chapter 05 (`blog-simonwillison-directly-responsible-individuals.md`) — both locate ownership in accountability for the outcome rather than in who executed the mechanical steps — but Wood applies the logic at the level of individual authorship of a single artifact rather than project-level accountability. It strengthens the case that "responsibility doesn't transfer to the tool" is a load-bearing idea at multiple organizational scales, though this essay offers no case where an authorship dispute was actually resolved this way.

### Claim 6: The concrete practice is a short, honest note appended to substantive shared work describing how judgment, tools, source material, and revisions combined to produce it — not a legal disclaimer and not a measurement of how much AI was used
- **Evidence**: Author's own prescriptive definition of the practice, illustrated with three example note formats (heavy AI involvement, no AI involvement, AI-pulled-data-with-human-analysis).
- **Confidence**: anecdotal (prescriptive practice, not evaluated against any organization that has actually adopted it)
- **Quote**: "It is not a legal disclaimer or a measure of how much AI you used. It is a plain description of how your judgment, the tools, your source material, and your revisions combined to produce the work."
- **Our assessment**: This is the essay's single most actionable artifact — a lightweight, specific practice a team could start immediately without new tooling or process. Its weakest point is that the essay provides zero evidence it has actually accelerated adoption anywhere; it is a proposal, not a documented outcome.

### Claim 7: The practice only works if applied consistently, including on work where no AI was used at all — a "no AI" note is just as valuable as a heavy-AI-involvement note, because consistency is what establishes the note as a description of process rather than a signal of how much AI adoption is happening
- **Evidence**: Author's own argument about what makes the practice trustworthy over time.
- **Confidence**: anecdotal (prescriptive design constraint, not tested)
- **Quote**: "The discipline is doing it consistently, not just when AI played a large role. A note that says "I wrote this the traditional way" is just as valuable as one that describes heavy AI involvement. It establishes that How This Was Made is a description of process, not a signal of AI adoption."
- **Our assessment**: This is a sharp, specific design detail that distinguishes the proposal from a simple "disclose when you use AI" norm — it explicitly guards against the practice becoming a de facto AI-usage scoreboard, which connects directly to Claim 9's warning about measurement corrupting the practice.

### Claim 8: Writing a "How This Was Made" note is itself a reflective practice that sharpens the author's own judgment about when AI helps and when it doesn't — the note-writing is part of the learning, not just a record of it
- **Evidence**: Author's own argument about the practice's side effect on the note-writer, independent of its organizational-spreading purpose.
- **Confidence**: anecdotal (asserted personal-development claim, no before/after comparison of practitioners who do vs. don't write these notes)
- **Quote**: "To write a good How This Was Made note, you have to think clearly about what you actually did. Which parts did AI handle well? Where did it fall short? What did you have to fix, and why? That reflection, done regularly, builds a clearer picture of your own practice than almost anything else."
- **Our assessment**: This adds an individual-benefit case for the practice (better personal calibration of when to use AI) that is separate from, and would justify the practice even absent, the organizational-spreading argument — a useful angle for a guide that wants to sell the practice to individual practitioners, not just to leaders trying to change org-wide norms.

### Claim 9: The practice must remain an informal norm rather than a formal policy or performance metric — the moment people believe the notes will be used to evaluate whether they used AI "enough," honesty and useful detail disappear
- **Evidence**: Author's own warning about how measurement would corrupt the practice.
- **Confidence**: anecdotal (asserted risk, no example of an organization that formalized a similar practice and saw honesty degrade)
- **Quote**: "How This Was Made should begin as a practice, not a policy. The purpose is to make learning transferable, not to measure adoption or evaluate whether someone used AI enough. The moment people believe the notes will be used to score their performance, honesty disappears and the useful detail disappears with it."
- **Our assessment**: This is a Goodhart's-law-shaped warning (measuring a behavior changes the behavior being measured) applied specifically to AI-use disclosure. It is a real risk worth flagging in the guide if this practice is recommended, but it also means the practice resists exactly the kind of quantitative adoption tracking the guide's existing "Measuring Impact" section (Chapter 05) is built around — see Guide Impact below.

### Claim 10: Benjamin Franklin's Junto (a weekly Philadelphia discussion club founded 1727, running nearly forty years) worked not because of the quality of its members but because inquiry was made visible — members brought questions as well as conclusions and learned by watching one another learn, a discipline the essay explicitly names "How This Was Made" as updating
- **Evidence**: Historical description of the Junto's rules and outcomes (the Library Company of Philadelphia, the Union Fire Company), presented as established history but not cited to a specific historical source within the essay.
- **Confidence**: anecdotal (historical claim, unsourced beyond the author's own telling — consistent with how this note's sibling extractions, e.g. `blog-mattwood-barcode-bargain.md` Claim 3 and `blog-mattwood-half-life-assumption.md` Claim 2, treat this author's unsourced historical analogies)
- **Quote**: "What made it work was not simply the quality of the people in the room. It was that inquiry was visible. Members brought questions as well as conclusions. They exposed their reasoning and learned by watching one another learn."
- **Additional quote (essay's closing synthesis, same essay)**: "Franklin understood that mutual improvement required people to see one another in the act of learning. Leaders trying to build momentum with AI can begin the same way: do real work with it, take responsibility for the result, and show how it was made."
- **Our assessment**: This is the essay's framing device and title justification — it gives the practice a 300-year historical precedent for "visible learning creates organizational momentum," which is rhetorically effective but, like this author's other historical analogies (Notices to Mariners, barcode scanning), not independently verified against a primary historical source in this extraction.

### Claim 11: Vendor-produced examples of AI use don't help spread adoption within an organization — what actually creates reference points people can act on is seeing a known colleague, inside their own organization, do real work and explain how
- **Evidence**: Author's own claim, contrasting vendor examples with in-organization examples.
- **Confidence**: anecdotal (asserted, no comparison of vendor-example-exposed vs. colleague-example-exposed groups)
- **Quote**: "Vendor examples don't fill that gap. What fills it is seeing someone they know, in their organization, doing real work and explaining how."
- **Our assessment**: This is a specific, checkable-sounding claim that argues against a common enablement-team default (share vendor case studies, run vendor-led demos) in favor of internal, named-colleague examples. It is asserted rather than tested, but it is a sharp enough claim to be worth flagging as a concrete recommendation distinct from generic "share success stories" advice.

### Claim 12: The author used his own custom "Writing Room" app with multiple AI agents across several revision rounds to draft this essay, directing structure and argument while writing and editing sections by hand, and explicitly takes responsibility for the final piece — offered as the essay's own worked example of the practice it recommends
- **Evidence**: First-person self-report in the essay's postscript, applying the essay's own recommended practice to itself.
- **Confidence**: anecdotal (single first-person self-report, unverifiable beyond the author's own account)
- **Quote**: "I used my own custom 'Writing Room' app to develop and draft this essay. I directed the structure and argument across multiple rounds from multiple agents: pushing on historical accuracy, tightening the language, and cutting anything that announced what the writing was about to do rather than just doing it. I wrote sections and edited by hand, shaped the direction, reviewed and revised each round, and take responsibility for the argument and the final piece."
- **Our assessment**: This is a genuine, if singular, demonstration of the practice — the essay itself carries a "How This Was Made" note, which is stronger evidence of the author's own commitment to the idea than a purely theoretical argument would be. It confirms "Writing Room" as a named, custom (non-off-the-shelf) tool this author has built, though the essay gives no further description of what the app does beyond this one mention — not enough detail to extract as a distinct tooling artifact.

## Concrete Artifacts

### The three example "How This Was Made" note formats (verbatim)

```
Source: Matt Wood, "How This Was Made," mattwood.blog, 2026-08-04
(https://mattwood.blog/essays/2026/08/how-this-was-made/)

1. "I started with rough notes and used AI to draft this. I rewrote the
   first section, adjusted the structure, and added the third example.
   Total time was about an hour."

2. "I wrote this without AI. The recommendation depended on recent customer
   conversations and organizational context that weren't available to the
   model."

3. "An agent pulled the data. I wrote the analysis and the recommendation."
```

### The essay's own postscript "How This Was Made" note (verbatim, in full — the essay's self-demonstration of its own recommended practice)

```
Source: Matt Wood, "How This Was Made," mattwood.blog, 2026-08-04,
postscript ("PS: How this was made")

"I began with the core idea: that AI momentum stalls inside organizations
because people see finished work but not the process behind it, and that
leaders can change this by describing how their own work was made. I wanted
the argument to feel inevitable rather than prescriptive, and asked for
precision and clarity over rhetorical polish.

I used my own custom 'Writing Room' app to develop and draft this essay. I
directed the structure and argument across multiple rounds from multiple
agents: pushing on historical accuracy, tightening the language, and cutting
anything that announced what the writing was about to do rather than just
doing it. I wrote sections and edited by hand, shaped the direction,
reviewed and revised each round, and take responsibility for the argument
and the final piece."
```

### Historical references (as stated in prose; no citation or link in the original)

```
Source: Matt Wood, "How This Was Made," mattwood.blog, 2026-08-04

- 1727: Benjamin Franklin founds the Junto, a weekly discussion club in
  Philadelphia (members: a printer, a surveyor, a shoemaker, a joiner)
- Club rules: direct contradiction and declarations of certainty
  "discouraged under threat of a small fine"; questions circulated before
  each meeting
- Ran "for almost forty years"
- Outcomes attributed to the Junto: the Library Company of Philadelphia
  ("America's first successful lending library") and the Union Fire Company
  ("the nation's first volunteer fire company")
```

### Author bio (from the site's About page, `https://mattwood.blog/about/`, fetched directly)

```
"I returned to AWS as Chief AI & Technology Officer in 2026, after almost 15
years here earlier in my career and most recently leading commercial
technology and innovation at PwC."

"Earlier: a PhD in machine learning, medical school at the University of
Nottingham, and a postdoctoral fellowship at Weill Cornell Medicine, where I
worked on natural language processing and bioinformatics back when that was
still a niche."

Source: https://mattwood.blog/about/ (re-fetched 2026-08-06; text unchanged
from the versions quoted in blog-mattwood-field-and-frontier.md,
blog-mattwood-half-life-assumption.md, and blog-mattwood-barcode-bargain.md)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-directly-responsible-individuals.md` Claim 1 (DRI:
    "ultimately accountable for the success or failure of a specific
    project") and Claim 2 (accountability "is something that feels uniquely
    human... because humans can take accountability for their actions where
    machines cannot"): this essay's Claim 5 (authorship is resolved by who
    shaped, revised, and remains responsible for a piece of work, not by who
    typed it) is the same "responsibility does not transfer to the tool"
    logic, applied to individual authorship of a single artifact rather than
    project-level accountability — a second, independent voice locating
    ownership in accountability rather than mechanical execution.
  - `blog-kentbeck-bethandresbeck-how-do-you-know-that.md` Claim 5 (a
    first-time manager builds a team testing culture by repeatedly asserting
    the norm and then reinforcing it visibly in code review, creating a
    self-reinforcing "dopamine loop"): both sources describe norm formation
    as something built through repeated, visible, reinforced behavior over
    time rather than a one-time declaration — though Beck/Andres-Beck's
    example starts with a manager's verbal assertion of the norm before it's
    true, while this essay's Claim 4 argues policy/verbal statements
    specifically do *not* shift behavior on their own. The two are
    complementary (both end in sustained visible behavior as the actual
    mechanism), not identical, and not treated as a MINER.md §4a
    contradiction — see below.
  - `blog-thoughtworks-lad-platform-business-value.md` Claim 5 and
    `blog-mattwood-barcode-bargain.md` Claim 9 (visible tool deployment can
    be "finished" while the surrounding trust/adoption work is nowhere near
    finished): this essay's Claim 1 (champions have already found the use
    cases; the unsolved problem is spreading, not deploying) is the same
    "rollout completion ≠ value realization" diagnosis, specifically located
    at the knowledge-transfer stage rather than the trust-earning stage.

- **Contradicts**: None identified as a MINER.md §4a contradiction. The
  closest candidate — this essay's Claim 4 ("policy doesn't shift behavior")
  versus `blog-kentbeck-bethandresbeck-how-do-you-know-that.md` Claim 5 (a
  manager verbally asserting a norm as a starting move) — was evaluated and
  judged not to qualify: Andres-Beck's technique pairs the verbal assertion
  with sustained visible reinforcement in code review, which is consistent
  with, not opposed to, this essay's claim that observed behavior (not the
  policy statement alone) is what actually shifts norms. This is a
  conditioning-variable difference (a manager's own repeated declaration-plus-modeling
  in a small team, vs. an organization-wide "AI use is encouraged" policy
  memo with no attached behavior), not two claims about the same mechanism
  that disagree. No contradiction issue filed.

- **Extends**:
  - Chapter 05's existing "Senior engineers should be the early adopters"
    guidance (`survey-pragmaticengineer-ai-tooling-2026.md` Claim 3): that
    material argues seniors should pilot first because they verify fastest
    and "produce the patterns that become the second-wave rollout's
    documentation." This essay supplies the missing mechanism for *how*
    those patterns are supposed to actually reach the second wave — not
    through a documentation deliverable, but through champions habitually
    attaching short process notes to real shared work.
  - `blog-mattwood-barcode-bargain.md` (same author): that essay's Claim 6
    (trust is a judgment about the whole arrangement, not a reaction to the
    technology) and Claim 9 (visible deployment can be finished while the
    surrounding "operating system" of adoption is not) supply an
    organization-wide historical frame; this essay narrows to a specific,
    immediately actionable mechanism (a shared-work process note) for
    closing exactly the gap the barcode essay describes only abstractly.
  - `blog-mattwood-half-life-assumption.md` (same author): that essay
    recommends recording *why* a decision was made as testable conditions;
    this essay recommends recording *how* a piece of work was made as a
    process note. Both are the same underlying move — externalizing tacit
    reasoning that would otherwise stay locked in one person's head — applied
    to decisions in one essay and to day-to-day work artifacts in this one.

- **Novel**:
  - The specific "How This Was Made" note practice itself (Claim 6) — a
    named, concrete, low-overhead artifact for AI-use process disclosure —
    is new to the corpus. No existing source note proposes appending a
    short, honest process note to shared work as an adoption-spreading
    mechanism.
  - The "champions concentrate momentum; the unsolved problem is spreading,
    not starting" diagnosis (Claim 1) and the "process invisibility" failure
    mechanism (Claims 2-3) are new, explicit framings not previously named
    this precisely in the corpus's Chapter 05 material.
  - The "norms change through observed behavior, not policy" mechanism
    (Claim 4) as an explicit, named principle for AI-adoption norm-setting is
    new to the corpus, though it echoes general organizational-behavior
    intuition rather than introducing new data.
  - The "practice, not policy" design constraint — that turning the note
    into a measured/scored artifact destroys its usefulness (Claim 9) — is a
    new, specific warning not previously articulated in the corpus for this
    kind of disclosure practice.
  - The Junto historical analogy (Claim 10) is a new historical framing
    device for the corpus, distinct from this author's other analogies
    (nautical charts, barcode scanning) already extracted in sibling notes.

## Guide Impact

- **Chapter 05 (Team Adoption) — "Senior engineers should be the early
  adopters" section**: This section currently stops at "seniors pilot first
  because they verify fastest," leaving the mechanism for spreading their
  patterns to the rest of the org unspecified beyond "documentation." Add
  this essay's "How This Was Made" note practice (Claim 6: a short, honest
  note on judgment/tools/source material/revisions appended to real shared
  work) as the specific, low-overhead mechanism recommended for that
  spreading step, paired with Claim 1's diagnosis (the unsolved problem
  after year one is spreading, not starting) as the reason a documentation
  deliverable alone is insufficient. Add Claim 11 (vendor examples don't
  spread adoption; in-organization, named-colleague examples do) as a
  specific argument against defaulting to vendor case studies for internal
  enablement.

- **Chapter 05 (Team Adoption) — "Measuring Impact" section**: Add Claim 9
  (the practice must stay an informal norm, not a scored metric, or honesty
  and useful detail disappear) as an explicit caution against folding
  "How This Was Made" notes into the chapter's existing adoption-metrics
  framework — this is a specific tension worth naming: the guide's
  measurement apparatus and this essay's recommended disclosure practice
  pull in opposite directions, and Chapter 05 should flag that turning the
  note into a tracked KPI would defeat its own purpose per this source.

- **Chapter 05 (Team Adoption) — "Name a human accountable for the outcome,
  not just the work" section**: Add Claim 5 (the work is the author's
  because they shaped, revised, and remain responsible for it, not because
  they typed every sentence) as a complementary, individual-authorship-level
  statement of the same accountability-doesn't-transfer-to-the-tool logic
  already anchored there via the DRI framing
  (`blog-simonwillison-directly-responsible-individuals.md`) — this essay
  extends that logic from "who is accountable for a project" to "who gets
  authorship credit for a specific piece of AI-assisted work," which the
  guide does not currently address at the individual-artifact level.

## Extraction Notes

1. The full article was retrieved directly via `curl` with a browser
   user-agent (HTTP 200) and parsed to plain text by stripping script/style
   tags and HTML markup, per the same method documented in
   `blog-mattwood-field-and-frontier.md` and
   `blog-mattwood-half-life-assumption.md`. This was necessary because an
   initial WebFetch attempt with a "reproduce the article verbatim" prompt
   was refused by WebFetch's summarizing model on copyright grounds, and a
   follow-up targeted-quote WebFetch prompt returned quotes that could not
   be trusted as character-for-character without independent verification.
   Per MINER.md §2a, this note relies only on the directly-parsed `curl`
   text for all quotes; the WebFetch-derived text was used only to identify
   which passages to look for, then verified word-for-word against the
   locally-parsed HTML.
2. The article contains no outbound hyperlinks in its body (confirmed by
   inspecting the raw HTML's `<a>` tags — only navigation links to the site
   root). No sub-pages were followed beyond the About page, per MINER.md
   §1's "up to 5 linked pages" guidance — there were none in the essay
   itself to follow.
3. The site's About page (`https://mattwood.blog/about/`) was fetched
   directly via `curl` to confirm the bio text had not changed since the
   three prior mattwood.blog extractions; it is identical to all three.
4. One candidate contradiction (this essay's "policy doesn't change
   behavior" claim vs. `blog-kentbeck-bethandresbeck-how-do-you-know-that.md`'s
   "manager asserts the norm" technique) was evaluated against MINER.md §4a
   and judged to be a conditioning-variable difference, not a genuine
   contradiction — see Cross-References → Contradicts for the full
   reasoning. No contradiction issue filed.
5. `confidence_overall` is rated `anecdotal`, consistent with this author's
   other two most recent sibling notes (`blog-mattwood-half-life-assumption.md`,
   `blog-mattwood-barcode-bargain.md`): every claim in this essay is either
   the author's own argument/mechanism claim, an unsourced historical
   analogy, or a single first-person self-report — there is no named
   customer example, survey, benchmark, or third-party citation anywhere in
   the source.
