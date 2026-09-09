---
source_url: https://martinfowler.com/articles/never-send-slides/need-presentation.html
source_type: blog-post
title: "Do you even need a presentation?"
author: Sumeet Gayathri Moghe (Global Head of Culture and Organisational Design, Thoughtworks)
date_published: 2026-09-08
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: anecdotal
issue: "#3323"
---

# Do you even need a presentation? (Sumeet Gayathri Moghe)

> A martinfowler.com essay — first in Moghe's "Never Send The Slides" series
> — arguing that most corporate communication should default to a linear
> written document rather than a slide deck, with infodecks, interactive web
> apps, and recorded audio/video as escalating alternatives, and live
> presentations reserved for situations that specifically require
> synchronous influence. The content is general communication-design advice
> (not AI-native-specific), but it surfaces two AI-relevant claims: linear
> document structure reduces LLM hallucination when a reader has an LLM
> summarize the document, and vibe-coded interactive web apps built by
> non-engineers carry a maintainability/shelf-life risk tied to how well the
> author understands the app's "inner workings."

## Source Context

- **Type**: blog-post, first article in a multi-part martinfowler.com series
  titled "Never Send The Slides." Published 2026-09-08. The article states
  later articles in the series will cover "how to craft your story" and the
  three presentation formats (recorded, online, in-person) — those follow-on
  articles were not yet published at extraction time and are out of scope
  for this note.
- **Author credibility**: Sumeet Gayathri Moghe is Thoughtworks' global head
  of culture and organisational design. Per the article's own bio, he spent
  "over two decades" as "a business analyst, product manager and
  transformation consultant" before this role, and he is the author of *The
  Async-First Playbook*. Martin Fowler is credited only with "an overall
  editorial review," not authorship — this is Moghe's essay, hosted on
  Fowler's site (the same "Exploring Gen AI" / practitioner-memo publishing
  pattern seen in other Thoughtworks pieces on martinfowler.com, e.g.
  `blog-fowler-boeckeler-local-models-viability.md`, but this piece is not
  gen-AI-focused — it is a communication-design essay that happens to touch
  AI twice in passing).
- **Scope**: Covers how to choose among five communication artifacts —
  document, infodeck, interactive web app, recorded audio/video, live
  presentation — for **corporate information-transfer scenarios**. It does
  not cover engineering-specific documentation formats (READMEs, ADRs,
  CLAUDE.md, PR descriptions) at all; every example given is drawn from
  general corporate/consulting communication (Thoughtworks playbooks, a
  personal video about brainstorming, a video series on "cultural
  identity"). The AI-native relevance has to be inferred by the reader; the
  article does not itself frame its advice in terms of AI-assisted
  engineering teams.

## Extracted Claims

### Claim 1: A "presentation" is specifically an act of live storytelling — narrative, timing, and emotion orchestrated by a presenter — and the slide deck itself is not the presentation
- **Evidence**: Author's own definitional framework, stated as a pull-quote/callout in the article, used to structure the entire piece.
- **Confidence**: anecdotal (a personal definitional framing, not an empirically validated claim)
- **Quote**: "A presentation is an act of storytelling in which a presenter orchestrates narrative, timing, and emotion to create meaning that neither visuals nor documents can achieve on their own."
- **Our assessment**: This is a useful conceptual wedge — it separates "the deck" from "the presentation" and lets the rest of the article argue that most of what people call "sending a presentation" is actually a document (or infodeck) mislabeled as a presentation. It's a framing device more than an evidenced claim; we treat it as the article's premise rather than an independently verifiable finding.

### Claim 2: Slideware is a poor format for well-structured writing because it forces readers to consume information in fragmented, disconnected bursts rather than building understanding progressively
- **Evidence**: Author's own practitioner observation/argument, no external citation or study.
- **Confidence**: anecdotal
- **Quote**: "Most of the time, though, slideware is a poor tool for well-structured writing. When we start using slides as a document format, we force readers to consume information in fragmented, disconnected bursts."
- **Our assessment**: Plausible and consistent with general writing-craft advice (documents allow readers to backtrack, scan headings, and see argument structure that slide-per-slide delivery obscures). Not novel to the AI-native corpus, but it is a clean articulation of "why default to docs."

### Claim 3: Linear document structure reduces the probability of hallucination when an LLM is used to summarize the document, because the writer is forced to explicitly bridge between sections
- **Evidence**: Author's own reasoning chain (documents force explicit bridging between sections → explicit writing gives an LLM summarizer less to infer/fabricate), no benchmark or study cited.
- **Confidence**: anecdotal
- **Quote**: "When you write, the linear structure of documents forces you to bridge different sections of your writing. From the reader's perspective, if they even use an LLM to summarise your document, the explicit nature of linear writing reduces the probability of hallucinations."
- **Our assessment**: This is the article's single most AI-specific claim, and it is asserted, not tested — there's no comparison of hallucination rates on slide-derived text versus linear-document text. Directionally plausible (less-elliptical source text should give a summarizer fewer gaps to fill), but we'd weight this as a hypothesis worth citing, not a settled result. It does connect to a live theme in the corpus: writing for machine consumption, not just human consumption, as a documentation-quality driver (see Cross-References).

### Claim 4: Infodecks (Fowler's term) are a distinct artifact from both slideuments and live-presentation decks — a "light reading" format that juxtaposes text and visuals for one-time or async consumption, not for presenting
- **Evidence**: Definitional distinction plus named real-world examples (Thoughtworks playbooks, Fowler's own site).
- **Confidence**: anecdotal
- **Quote**: "Infodecks aren't slideuments and don't double as presentation devices. They're only for what I'd call \"light reading\". They juxtapose text with visuals and communicate information in a concise and approachable manner."
- **Our assessment**: Useful terminology if the guide ever wants to distinguish "a slide-formatted document meant to be read, not presented" from both plain docs and presentation decks. Low novelty as a concept (slidedocs/"Slidedoc" from Duarte Design is cited by the author as prior art), but the term itself is a handy label.

### Claim 5: Infodecks mostly fail because of a scarcity of design skill among knowledge workers, not because of the format itself; the highest cost of a good infodeck is the information-design labor, not the authoring tool
- **Evidence**: Author's own practitioner assertion, no data cited.
- **Confidence**: anecdotal
- **Quote**: "Design makes an infodeck succeed or fail. The scarcity of design sense among knowledge workers is one reason most infodecks are ineffective. Indeed, the highest cost in producing infodecks comes from leveraging skilful information designers who can collaborate with subject matter experts to produce the final artefact."
- **Our assessment**: This is a caution against recommending infodecks as a low-cost default — the article itself concedes it's a high-skill, high-cost format when done well, which cuts against treating it as a lightweight communication upgrade over plain docs.

### Claim 6: A recent wave of coding harnesses lets non-developers build small interactive web apps (embedding content, adding filter/hover interactivity) to manage an audience's cognitive load, as an alternative to a static document or spreadsheet
- **Evidence**: Author's own practitioner example — a filterable/hoverable word-cloud web page (full HTML/CSS/JS embedded in the article as a live demo) built by the author, who identifies as "not a software engineer," to compare company-values claims across consulting firms.
- **Confidence**: anecdotal
- **Quote**: "In the last year or so, we've seen an explosion of coding harnesses that allow non-developers to spin up simple applications. Using HTML, CSS, and JavaScript, you can embed content from external sources and use interactivity to manage your readers' cognitive load."
- **Our assessment**: This is the article's clearest "AI-native engineering touches my job now" moment — a non-engineer builds and ships small interactive artifacts via a coding harness rather than commissioning developer time. It corroborates the broader corpus theme of vibe-coding by non-engineers for narrow, low-blast-radius purposes (see Cross-References), though this article does not name which harness/tool was used.

### Claim 7: Interactive web apps built this way have real trade-offs — they lack the built-in inline commenting of wikis/docs, and are "stateless" one-way information transfer unless that functionality is deliberately added
- **Evidence**: Author's own practitioner observation, drawn from having built such apps.
- **Confidence**: anecdotal
- **Quote**: "Wiki pages and collaborative documents have built-in commenting functionality, so people can offer you feedback and reactions inline with your content. Adding this functionality to every app or interaction you build creates overhead. So, be aware of this trade-off. Interactive, but stateless applications have limited utility beyond one-way information transfer."
- **Our assessment**: A concrete, specific downside (no inline feedback loop) rather than a vague "interactivity is complex" caveat — useful as a checklist item when deciding whether a quick vibe-coded artifact is the right format for something that needs collaborative iteration.

### Claim 8: A non-engineer author estimates the maintainability/shelf-life of a vibe-coded interactive app by how well they personally understand its inner workings, not by any formal engineering assessment
- **Evidence**: First-person admission from the author.
- **Confidence**: anecdotal
- **Quote**: "Since I'm not a software engineer, I estimate the shelf life of such applications based on how well I understand their inner workings."
- **Our assessment**: This is a candid and somewhat alarming admission — the author's *comprehension*, not code quality, tests, or review, is the proxy for whether a shipped artifact will keep working. It's an honest data point on how non-engineers reason about the durability of AI-generated code they can't fully evaluate, and it complements (see Cross-References) the corpus's existing "keep blast radius small for vibe-coded artifacts" guidance — Moghe's version of risk mitigation is "only ship what I can still explain," which is a weaker but real-world-practiced substitute for code review.

### Claim 9: Recorded audio/video is a substitute for live presentation and, per the author, "most presentations are better off as recordings" because the audience controls pace and gets closed captions/chapter markers
- **Evidence**: Author's own argument plus two personal production examples with concrete build/transition counts (an 8-minute video with 129 builds/transitions; a 24-minute on-screen recording with 141 builds/transitions), cited as evidence that even heavily-produced recordings don't need a rigid "right number" of slide builds.
- **Confidence**: anecdotal
- **Quote**: "Recording a talk forces you to be brief and cut the fluff from your narrative. Your audience can consume your content on their own time, slow it down, speed it up, or play it multiple times if they wish. Closed captions help others understand your accent, and chapter markers help viewers and listeners speed to or revisit topics of interest. With all these benefits, it's fair to say that most presentations are better off as recordings."
- **Our assessment**: Reasonable async-communication argument (self-paced, replayable, captioned beats synchronous and un-replayable), consistent with general async-first-team advice, though asserted rather than measured (no data on completion rates or comprehension for recorded vs. live).

### Claim 10: Live presentations should be reserved for situations that specifically require synchronous presence — influencing people or addressing objections in real time — because that overhead is only justified when it can't be achieved async
- **Evidence**: Author's own recommendation, plus a cheat-sheet table mapping five artifact types to trigger conditions (see Concrete Artifacts).
- **Confidence**: anecdotal
- **Quote**: "I suggest reserving live presentations for situations that merit the scheduling overhead. If you're bringing people together in the same physical or virtual space to share something with them, it should be well worth everyone's time."
- **Our assessment**: This is the article's central thesis restated as a decision rule. It's a clean, actionable framing ("what does this synchronous meeting actually need that an async artifact couldn't provide?") even though it's general workplace-communication advice rather than anything specific to AI-assisted engineering work.

## Concrete Artifacts

Cheat-sheet decision table from the article (verbatim, reformatted as Markdown from the source's two-column layout):

```
Artefact                    | Use it when…
-----------------------------|--------------------------------------------------------------------------------
Document                    | You want to convey information and don't need synchronous communication.
Infodeck                    | The content will have a long shelf life and deserves visual polish.
Web apps                    | You want to manage your audience's cognitive load by using web interactions
                             | that allow them to explore your content.
Recorded audio and video    | Your voice matters, but you don't need live audience interaction.
Live presentation           | Synchronous presence matters, so you can influence people or address
                             | objections in real time.
```

Author's acknowledgment of AI tool use in producing the article itself (attribution
verbatim from the "Acknowledgments" section):

```
I have used Grammarly to proof read and copy-edit this essay.
Claude helped me double-check whether I had addressed all feedback
I'd received for this article, either as edits to the original or as
ideas for future articles in this series.
```

The article embeds two full working HTML/CSS/JS demos inline (a filterable/hoverable
word-cloud comparing consulting-firm values, and a tabbed video-series player) as
live illustrations of the "web interactions" artifact type. Both are functioning,
self-contained single-file web apps of the kind the author describes non-developers
building via "coding harnesses" — consistent with Claim 6, though the article does
not name which harness produced them.

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-liteparse-browser.md` (Claim 12: browser-native static
    apps with no server/data-transfer have "almost non-existent" blast radius
    that justifies vibe coding by less-technical builders) — Claim 6/8 here
    describe the same practice (a self-identified non-engineer shipping a
    small interactive web artifact via a coding harness) from the builder's
    side, adding a maintainability angle (shelf-life estimated by personal
    comprehension, not blast-radius analysis) that Willison's note doesn't
    cover.
- **Contradicts**: None identified.
- **Extends**: None identified — this is the first source note in the corpus
  focused specifically on choosing among document/infodeck/web-app/video/
  live-presentation formats for team communication; there is no existing
  note to extend on this specific topic.
- **Novel**: The "infodeck" terminology and decision framework (Claims 4-5,
  10) and the cheat-sheet artifact-selection table are new to the corpus.
  Claim 3's specific mechanism (linear-document structure reduces LLM
  hallucination on summarization) and Claim 8's "I estimate shelf life by
  how well I understand the code" admission are also novel angles not
  previously captured, though both are asserted rather than evidenced in the
  source itself.

## Guide Impact

- **Chapter 05 (Team Adoption)**: The guide does not currently have a
  section on choosing communication media for team knowledge-sharing (async
  docs vs. live meetings vs. recorded video). This source is *weak-to-
  moderate* supporting evidence, not primary evidence, for the guide's
  existing implicit bias toward persistent written artifacts (PRs, CLAUDE.md,
  plan files) over synchronous handoffs — but the article itself is general
  corporate-communication advice, not engineering- or AI-specific, so it
  should be cited (if at all) as a secondary reference for "why async-first
  documentation works," not as a basis for a new standalone section. Given
  low-to-medium novelty (per triage) and the general-audience framing, we'd
  recommend citing Claim 10's decision rule only if the guide adds a
  communication-format subsection to Ch05; it does not on its own justify
  adding one.
- **Chapter 01 (Daily Workflows) / Chapter 04 (Context Engineering)**: No
  direct change recommended. Claim 3 (linear docs reduce LLM hallucination on
  summarization) is thematically adjacent to context-engineering's concern
  with how document structure affects LLM comprehension, but the claim here
  is asserted without evidence and is about a *reader's* LLM summarizing a
  *human-facing* document, not about how an agent consumes a repo's own
  documentation — the fit is loose enough that we would not cite this source
  for that claim without independent corroboration.

## Extraction Notes

- Read the full article via direct HTTP fetch (not the WebFetch summarizer)
  specifically so that all quotes above could be copied character-for-character
  from the raw HTML rather than reconstructed from an AI-generated summary.
  Every quote in this note was verified against the raw HTML source before
  being included.
- The article is the first in a stated multi-part series ("Never Send The
  Slides"); per MINER.md guidance to follow substantive linked pages, I
  checked for already-published follow-on articles in the series and found
  none — the series' table-of-contents/next-article links point to content
  not yet published as of extraction (2026-09-09). No sub-pages were
  available to follow.
- Two large embedded code blocks (the word-cloud demo and the video-series
  player, each 100+ lines of HTML/CSS/JS) were skimmed for structure rather
  than reproduced in full in Concrete Artifacts — they are functioning demos
  illustrative of Claim 6 rather than a technique with independent
  guide-relevant content; reproducing them in full would not add extraction
  value beyond what Claim 6/7's quotes already capture.
- Three separate Prospector triage comments on the source issue gave
  differing novelty assessments (medium, low, medium) and disagreed on
  which existing notes overlap. I independently verified the two notes
  named in the third comment (`blog-cursor-better-models-ambitious-work.md`
  Claim 6, `blog-simonwillison-liteparse-browser.md` Claim 5) and found
  neither to be a strong content match for this article's claims — Claim 5
  of the liteparse note (notes.md → plan.md handoff) is about persisting an
  agent's own working context between sessions, not about choosing a
  communication medium for human audiences, so I did not cite it. I instead
  found a genuine corroboration point via `blog-simonwillison-liteparse-browser.md`
  Claim 12 (vibe-coded low-blast-radius apps), cited above under
  Cross-References.
