---
source_url: https://martinfowler.com/articles/never-send-slides/slide-principles.html
source_type: blog-post
title: "Principles for effective slides"
author: Sumeet Gayathri Moghe (Global Head of Culture and Organisational Design, Thoughtworks)
date_published: 2026-09-30
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: anecdotal
issue: "#3832"
---

# Principles for effective slides (Sumeet Gayathri Moghe)

> Part of Moghe's "Never Send The Slides" series on martinfowler.com: when a live presentation is justified, slides should be a visual channel that complements the speaker, so they are minimalist, tightly coupled to the talk, and never sent out in advance. General communication craft; its one AI-specific passage is a short sidebar arguing that delegating slide construction to AI costs more effort than it saves.

## Source Context

- **Type**: blog-post, second substantive article in the "Never Send The Slides" series (published 2026-09-30). The article's own navigation lists "Nail your narrative" as the previous post; the first article is covered by `blog-fowler-moghe-need-presentation.md`. The article promises later posts on colours/typography/layouts and on helping colleagues present your slides; those were not yet published.
- **Author credibility**: Moghe is Thoughtworks' global head of culture and organisational design, and per the article's bio "a software technologist for over two decades, working as a business analyst, product manager and transformation consultant." He credits Martin Fowler with helping "frame the evidence that justifies using slides as a complementary visual channel." Evidence is practitioner experience plus citations to Clark & Mayer's multimedia principle, Nancy Duarte, Neal Ford, Dan Roam and Don Norman.
- **Scope**: Craft principles for slides used in live presentations. Not AI-native engineering; there is no discussion of agents, code, or docs for LLMs. Only the sidebar "The AI slide design challenge" touches AI (plus AI as example talk topics).

## Extracted Claims

### Claim 1: The defining difference between a presentation and an infodeck is the presenter's control over the rate of knowledge exposition, via builds and transitions
- **Evidence**: Attributed to Neal Ford; the author's own practice (a single slide split into 31 visuals; 14 snapshots delivered in two minutes to a C-suite audience).
- **Confidence**: anecdotal
- **Quote**: "Unlike static infodecks, the builds (animations) and transitions in your presentation slides allow you to control that rate of knowledge exposition."
- **Our assessment**: A clean criterion for separating "deck to be read" from "deck to be presented". It is the same cognitive-load-pacing idea that the guide applies to feeding agents context incrementally, but here it is only about human audiences.

### Claim 2: Slides should be a "complementary visual channel", and learning is better with words plus graphics than words alone (dual encoding)
- **Evidence**: Appeal to Clark and Mayer's "multimedia principle" (E-Learning and the Science of Instruction, 2016); Martin Fowler's "complementary visual channel" framing. No new data.
- **Confidence**: emerging (the multimedia principle has research behind it; the application to corporate slides is asserted)
- **Quote**: "When you provide the words and your slides provide the visuals, your audience benefits from dual encoding."
- **Our assessment**: The only external-research hook in the article. Reasonable, and consistent with the claim of Part 1 that a presentation is more than its visuals, but we have not verified the Clark and Mayer citation.

### Claim 3: Slides must couple tightly with the speaker without repeating the speaker; wordy slides "steal the narrative" because audiences read faster than you speak
- **Evidence**: Worked example of a standard infodeck slide ("passable" as a reading artefact, "a disaster" as a presentation slide); term "stealing the narrative" attributed to Martin Fowler.
- **Confidence**: anecdotal
- **Quote**: "By the time you start with the first point, your audience will have already speed-read the entire page."
- **Our assessment**: Intuitive and widely held. The wider implication is that the same artifact cannot serve both a reading and a presenting purpose, which sharpens Part 1's document/infodeck/live-presentation split.

### Claim 4: Effective slides are speaker-specific, so they are hard to hand to someone else to present, and this is why slide makers over-stuff slides
- **Evidence**: Author's observation (sidebar "When your job is to present someone else's slides").
- **Confidence**: anecdotal
- **Quote**: "Even when we design these slides well, the knowledge of how to present the materials remains tacit."
- **Our assessment**: An interesting tacit-knowledge point: the slides alone do not encode the presenting knowledge. It parallels the guide's concern that prompts and specs lose meaning without their surrounding context, but the author does not make that link and defers the fix to a future post.

### Claim 5: Be minimalist by default, and the number of slides does not matter, so discard the "one slide per two minutes" and "six bullets, six words" rulebook
- **Evidence**: Example of 14 snapshots of one diagram covered in two minutes; Nancy Duarte's "glance media" / billboard analogy; Saint-Exupéry quote.
- **Confidence**: anecdotal
- **Quote**: "Those are the death-by-PowerPoint rules. Our principles are different."
- **Our assessment**: Contrarian but coherent: the unit to optimise is the cognitive load per reveal, not slide count. Not AI-specific.

### Claim 6: Delegating slide construction to AI may cost more effort than building from scratch when slides are many fine-grained snapshots tied to a narrative
- **Evidence**: The author's own reasoning from the 14-snapshot developer-relations example. No experiment, tool, or model named; the claim rests on introspection about describing-and-iterating effort.
- **Confidence**: anecdotal
- **Quote**: "The effort it’ll take me to describe these slides to AI, and then iterate with it, is much higher than the effort I’ll have to put in to build everything from scratch."
- **Our assessment**: The only AI-native claim in the article, and an honest "AI isn't worth it here" data point: when the intent is largely tacit and highly sequenced, specifying it costs more than doing it. This is consistent with a broader theme that delegation pays off only when the spec is cheaper than the work. The author doesn't say which tools he tried, so treat it as an opinion rather than a failure report.

### Claim 7: Treat slides as integrated visuals; the audience should not notice transitions, and someone else controlling your slides ("Next slide, please") distracts from the message
- **Evidence**: Author's practice and a three-minute embedded video example.
- **Confidence**: anecdotal
- **Quote**: "“Next slide, please” is the easiest way to distract your audience from the message and have them think about your slides."
- **Our assessment**: Narrow craft advice; no AI relevance.

### Claim 8: Visuals can carry the message with minimal text; text should reinforce or label, but must not substitute for the presenter
- **Evidence**: A "perpetual beta" talk with 13 photographs and about a minute of narration (camera eye-detect autofocus failing on a leopard, used to illustrate that mature AI is fallible); Dan Roam quote.
- **Confidence**: anecdotal
- **Quote**: "The trap to avoid is letting the text substitute for you, the presenter."
- **Our assessment**: Fine craft guidance. The example is incidentally about AI fallibility but is a rhetorical device, not evidence about AI engineering.

### Claim 9: Never send slides in advance; replace them with purpose-specific artefacts (prep notes, a dress rehearsal or recorded run-through, reference materials, a takeaway handout)
- **Evidence**: The author's practice; a remote-work research talk used a handout and a data dashboard but no prep notes; "Greek chorus" pattern from Ford, McCollough and Schutta.
- **Confidence**: anecdotal
- **Quote**: "If your slides serve as a visual channel that reinforces what you say, they can’t stand alone."
- **Our assessment**: The substantive new idea: match the artefact to its purpose (prepare, align, reference, take away) rather than sending one multipurpose artifact. This extends Part 1's artefact-selection table from "which format" to "which supporting artefacts around a live session". The author concedes exceptions ("Never say never, right?").

### Claim 10: Slides are cue cards for the audience, not for the presenter; needing on-slide notes signals poor preparation
- **Evidence**: Author's assertion.
- **Confidence**: anecdotal
- **Quote**: "If you're using your slides to prompt you, that signals poor preparation."
- **Our assessment**: Opinionated and untested; a useful heuristic for who an artifact is written for. A similar "who is the reader?" question applies when writing agent-facing docs, but that is our extrapolation.

## Concrete Artifacts

The article's summary of its principles (verbatim, "Rewrite the rulebook" section):

```
As presenters, we seek to control the rate of knowledge exposition.
Slides serve as a visual channel to complement the speaker.
Slides and speakers are tightly coupled.
The number of slides doesn’t matter.
Be minimalist by default.
Treat slides as integrated visuals, not a collection of components.
Never send the slides.
```

The four substitutes for sending slides (paraphrased from the "Never send the slides" section):
- Prep notes (one page, short email, or structured message) to prepare the audience.
- Dress rehearsal, or a recorded run-through for high-stakes talks, to align colleagues and seed a "Greek chorus".
- Reference materials (prints, online resource, chat links) for use during the talk.
- Handout (e.g. a PDF of slides with presenter notes, or a one-page takeaway).

AI use disclosed by the author: "I have used Grammarly to proof read and copy-edit this essay." (Acknowledgments.)

## Cross-References

- **Corroborates**:
  - `blog-fowler-moghe-need-presentation.md` (Claim 10: live presentations reserved for situations that merit "the scheduling overhead"; Claim 2: slideware is a poor format for well-structured writing) — this article takes the same position from the other side: slides stand alone poorly, so do not send them, and a reading artefact should be a document or infodeck.
- **Contradicts**: None identified.
- **Extends**:
  - `blog-fowler-moghe-need-presentation.md` (Claim 4, infodeck as a distinct "light reading" artefact; the cheat-sheet table in its Concrete Artifacts section). This article gives the criterion separating infodecks from presentation slides (control over rate of exposition) and the set of supporting artefacts around a live session.
- **Novel**: The presenter-vs-audience "cue card" framing, the "never send the slides" principle with its four substitute artefacts, and the author's first-person judgment that AI-assisted construction of fine-grained, narrative-coupled slides costs more than it saves (Claim 6). None appear elsewhere in the corpus.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Marginal. If a communication-formats subsection is ever added (see the Impact section of `blog-fowler-moghe-need-presentation.md`), this article could be a secondary citation for "match the artefact to its purpose rather than circulating one deck". On its own it does not justify a new section; it is general communication craft with weak, practitioner-only evidence.
- **Chapter 01 (Daily Workflows)**: Claim 6 could be cited, with the caveat that it is a single unnamed-tool opinion, as an example of a task where delegating to AI is not worth it because the intent is tacit and the iteration cost exceeds the build cost. Recommend not changing the guide without corroborating sources.

## Extraction Notes

- Fetched the raw HTML with curl, stripped markup, and read the full article text; quotes were copied from that text (line-wrap whitespace collapsed to single spaces).
- Embedded media (iframes of slide builds, YouTube videos) could not be inspected; claims about the example decks rely on the author's prose descriptions.
- Followed no sub-pages: the article's links point to external books/talks, and the series' later posts were unpublished.
- Per the triage comments, novelty is low-to-medium and the overlap with the Part 1 note is the main one; a separate note was written because this article contains distinct claims (notably Claim 6) rather than merging into the Part 1 note.
