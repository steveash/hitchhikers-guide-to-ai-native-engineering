---
source_url: https://martinfowler.com/bliki/ParacelsusMaxim.html
source_type: blog-post
title: "Bliki: Paracelsus Maxim"
author: Martin Fowler
date_published: 2026-09-02
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: anecdotal
issue: "#3225"
---

# Bliki: Paracelsus Maxim

> Fowler's short "bliki" dictionary entry naming a general heuristic — "the
> difference between a medicine and a poison is dosage" — for habits and
> design choices that are neither universally good nor bad but become
> harmful past some threshold of amount, illustrated with a single
> programming example (global data).

## Source Context

- **Type**: blog-post (martinfowler.com "bliki" — Fowler's short,
  dictionary-style entry format, explicitly tagged `dictionary` on the
  page itself)
- **Author credibility**: Martin Fowler, Thoughtworks Chief Scientist —
  the trusted-feed author this repository already draws on for multiple
  harness-engineering and context-engineering source notes (e.g.
  `blog-fowler-garg-orchestrator-tax.md`,
  `blog-fowler-bayer-prince-agentic-rag.md`). This particular entry is not
  an evidence-driven article; it is a short personal-opinion definitional
  post in Fowler's long-running "bliki" (blog + wiki) series, a format he
  uses for compact, recurring-vocabulary concepts rather than researched
  argument.
- **Scope**: The entire entry is approximately 250 words: one framing
  sentence, the etymology of the Paracelsus quote, one contrasting example
  about context-dependence (reading a book in a garden vs. while driving),
  one dosage example (a painkiller vs. an overdose), one programming
  example (global data), and a closing two-question heuristic. It does
  NOT cover any AI-specific, agentic, or AI-native-engineering example —
  the only concrete domain example given is a general software-engineering
  one (global data), predating and unrelated to LLM-based tooling. It does
  not cite any data, study, or named practitioner incident; it is an
  assertion of a general framing principle, illustrated rather than
  evidenced.

## Extracted Claims

### Claim 1: The distinction between something being beneficial or harmful is often a matter of dosage, not an inherent binary property
- **Evidence**: Stated as the article's opening thesis and framing device
  for everything that follows.
- **Confidence**: anecdotal
- **Quote**: "The difference between a medicine and a poison is dosage."
- **Our assessment**: This is a restatement of a well-established
  toxicological/folk-wisdom principle (see Claim 2) applied as a framing
  device for engineering habits. As a *meta*-principle it is broadly
  credible and hard to dispute in the abstract, but the article itself
  offers no AI-native-engineering evidence for it — it is a lens the guide
  would need to apply to specific practices (model size, context volume,
  tool count, configuration surface) using evidence from other sources,
  not from this one.

### Claim 2: The dosage principle traces to Paracelsus, a 16th-century Swiss physician, in the original German "Alle Dinge sind Gift, und nichts ist ohne Gift; allein die Dosis macht, dass ein Ding kein Gift ist"
- **Evidence**: Historical/etymological attribution, sourced by Fowler to
  Wikipedia (not a primary historical source).
- **Confidence**: settled (as a widely-attested historical attribution;
  Fowler himself cites it secondhand via Wikipedia rather than a primary
  source)
- **Quote**: "The importance of dosage was noticed by a 16th century Swiss physician called Paracelsus. His quote was originally in German \"Alle Dinge sind Gift, und nichts ist ohne Gift; allein die Dosis macht, dass ein Ding kein Gift ist.\" which (according to Wikipedia) translates as \"All things are poison, and nothing is without poison; the dosage alone makes it so a thing is not a poison.\""
- **Our assessment**: Background/provenance only — useful for correctly
  naming and attributing the heuristic if the guide adopts "Paracelsus
  Maxim" as a named term, not itself an AI-engineering claim.

### Claim 3: Context is a separate variable from dosage — some things are good or bad depending on the situation they occur in, independent of how much of them there is
- **Evidence**: A single illustrative contrast (reading while sitting in a
  garden vs. reading while driving a car), offered before the dosage point
  is introduced.
- **Confidence**: anecdotal
- **Quote**: "Some vary with context: reading a book is a good thing sitting in my garden, but not while driving my car."
- **Our assessment**: Fowler explicitly separates "context" from "dosage"
  as two distinct reasons a habit's value can vary — the guide should not
  collapse these into one idea. For AI-native-engineering purposes this
  maps to two different design questions: "is this appropriate *here*"
  (context) versus "is this appropriate *at this amount*" (dosage) — e.g.
  a large context window may be contextually appropriate for one task type
  and inappropriate for another, which is a separate question from how
  much context volume is too much for a given task.

### Claim 4: A little global data (especially immutable) is a useful way to propagate information a program needs everywhere, but it becomes dangerous once there is a lot of it
- **Evidence**: The article's single concrete domain example, offered as
  the illustration of the maxim applied to programming, with no supporting
  data or citation beyond Fowler's own stated view.
- **Confidence**: anecdotal
- **Quote**: "In programming, global data is a good example of the Paracelsus Maxim (as I like to call it). A little global data, especially when immutable, can be a handy way of propagating information that may needed anywhere in a program, but it quickly becomes dangerous if there is a lot of it about."
- **Our assessment**: This is a general software-engineering example (and
  contains an apparent typo in the source itself — "may needed" — copied
  here verbatim as it appears on the page), not an AI-native-engineering
  one. It is useful only as the template for the *kind* of claim the
  guide would need to construct for AI-specific practices (e.g. "a little
  shared/global state in a multi-agent system may be fine, more becomes
  dangerous") — that specific extension is the guide's inference, not
  something this article states.

### Claim 5: When evaluating whether a habit or practice is good or bad, one should ask both "in what contexts?" and "in what doses?" rather than treating it as a universal binary
- **Evidence**: Stated as the article's closing generalization/heuristic.
- **Confidence**: anecdotal
- **Quote**: "This kind of thing crops up in lots of places. So when thinking about when things are good or bad, we should always ask \"in what contexts\" and \"in what doses\"?"
- **Our assessment**: This is the most directly reusable output of the
  piece — a two-question checklist ("what context, what dose") rather than
  a single-axis judgment. It is a useful framing tool for the guide's
  Principles chapter when discussing practices that are neither uniformly
  recommended nor uniformly discouraged (e.g. tool enablement, context
  volume, model size, configuration surface), but the article supplies the
  question, not the answer, for any AI-native-engineering practice.

## Concrete Artifacts

```
Source: martinfowler.com/bliki/ParacelsusMaxim.html (full entry, ~250 words)

The difference between a medicine and a poison is dosage.

Often we talk about certain habits, in programming or life, are good or
bad. But few things are simple binaries. Some vary with context: reading
a book is a good thing sitting in my garden, but not while driving my
car. But another variable is dosage: a little pain-killer salves my
headache, but too much will kill me.

The importance of dosage was noticed by a 16th century Swiss physician
called Paracelsus. His quote was originally in German "Alle Dinge sind
Gift, und nichts ist ohne Gift; allein die Dosis macht, dass ein Ding
kein Gift ist." which (according to Wikipedia) translates as "All things
are poison, and nothing is without poison; the dosage alone makes it so
a thing is not a poison." It's also known as "The dose makes the poison"
or if you prefer your sayings in Latin "dosis sola facit venenum".

In programming, global data is a good example of the Paracelsus Maxim
(as I like to call it). A little global data, especially when immutable,
can be a handy way of propagating information that may needed anywhere
in a program, but it quickly becomes dangerous if there is a lot of it
about.

This kind of thing crops up in lots of places. So when thinking about
when things are good or bad, we should always ask "in what contexts" and
"in what doses"?
```

## Cross-References

- **Corroborates**: None found as a direct empirical corroboration — this
  is a framing/naming piece, not an evidence claim, so there is nothing in
  the corpus that "agrees" with it in the evidentiary sense. See Extends
  below for the closest matches.
- **Contradicts**: None identified. Checked against the other Fowler notes
  in the corpus (`blog-fowler-garg-orchestrator-tax.md`,
  `blog-fowler-bayer-prince-agentic-rag.md`,
  `blog-fowler-boeckeler-local-models-viability.md`,
  `blog-fowler-boeckeler-tdd-in-the-agent-loop.md`,
  `blog-fowler-edwards-alexander-accidental-blackboard.md`,
  `blog-fowler-edwardsalexander-refactoring-token-economics.md`,
  `blog-fowler-malykhin-archaeologist-copilot.md`,
  `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md`, and the
  `blog-fowler-fragments-*.md` link-roundup notes) and found nothing that
  argues a binary always-good/always-bad framing for a practice this
  article would classify as dosage-dependent. No contradiction issue
  filed per MINER.md §4a.
- **Extends**: This general "amount matters, not just presence/absence"
  framing is a plausible naming device for several *already-evidenced*
  AI-native-engineering claims elsewhere in the corpus that describe the
  same shape of trade-off without using this vocabulary:
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 5
    ("Connecting too many MCP tools fills the context window with tool
    descriptions, degrading agent performance... every irrelevant tool
    description costs reasoning tokens even without being used") — a
    concrete, evidenced instance of the dosage pattern applied to tool
    count: a few tools are useful, too many degrade performance, mirroring
    this article's global-data example structurally.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 3
    ("HumanLayer's CLAUDE.md is kept under 60 lines") and Claim 9 (LLM-
    generated AGENTS.md files hurt performance while costing more; agents
    spend 14-22% more reasoning tokens processing context-file
    instructions) — both are evidenced examples of configuration/context
    volume behaving as a dosage variable (small and curated helps, large
    and unmanaged hurts) rather than a simple "more context is always
    better" binary.
  - `blog-fowler-garg-orchestrator-tax.md` Claim 7 ("A larger context
    window does not fix the attention-competition problem... a bigger
    context window doesn't fix that. It just gives the noise more room to
    pile up before anyone notices.") — an independent Fowler-published
    piece making the same "more capacity is not the same as more benefit"
    point about context volume specifically, without naming or citing this
    dosage framing.
  These are offered as candidate applications the guide could name using
  this article's vocabulary; the article itself does not make any of
  these connections — they are absent from its text, which stops at the
  global-data example.
- **Novel**: The "Paracelsus Maxim" name and its two-question checklist
  ("in what contexts, in what doses") are new to this corpus as an
  explicit, citable framing device — no existing source note uses this
  vocabulary, even though several (see Extends above) evidence the
  underlying pattern independently.

## Guide Impact

- **Chapter 00 (Principles)**: The single clearest use of this source is
  as a *named framing device*, not as new evidence: if the guide already
  has or plans a section on "practices that are neither universally
  recommended nor discouraged" (context volume, tool count, model size,
  configuration surface, abstraction layers), it could adopt "the
  Paracelsus Maxim" / "dose makes the poison" as the citable vocabulary
  for that section, with this article as the citation for the term, and
  the actual evidence drawn from the Extends sources above (e.g.
  `blog-humanlayer-skill-issue-harness-engineering.md` Claim 5 for tool
  count, Claim 9 for AGENTS.md length; `blog-fowler-garg-orchestrator-tax.md`
  Claim 7 for context window size). Do not cite this source alone as
  evidence for any specific AI-native-engineering dosage threshold — it
  supplies the name and the question, not a measurement.
- **Chapter 02 (Harness Engineering) / Chapter 04 (Context Engineering)**:
  If the guide adds "ask what dose, not just what type" as a design
  checklist item for tool enablement, context budget, or configuration
  scope, this article is the correct citation for the checklist's origin
  and phrasing ("in what contexts... in what doses"), paired with the
  already-evidenced sources above for the actual thresholds/data.

## Extraction Notes

- The full entry was fetched directly (not paywalled, not truncated) and
  is reproduced in full above under Concrete Artifacts, since the entire
  post is short enough to quote in its entirety without exceeding fair-use
  extraction norms for a source note.
- This is Fowler's shortest content format ("bliki," tagged `dictionary`
  on the page) — a ~250-word definitional entry, not a researched article.
  Per MINER.md's "5-15 claims per source" guidance, this note extracts 5
  claims; the source genuinely does not contain more distinct, extractable
  claims without inventing content that is not in the text. Padding beyond
  the 5 identified claims (thesis, etymology, context-vs-dosage
  distinction, the global-data example, the closing heuristic) would
  require fabricating claims the article does not make — three Prospector
  triage passes on this issue independently converged on "low"/"medium"
  novelty and flagged the source as thin/conceptual, which this extraction
  confirms.
- No sub-pages were followed: the only outbound link on the page is an
  internal tag link (`/tags/dictionary.html`), a category index page with
  no substantive content of its own to extract.
- The apparent grammatical error in the source's global-data sentence
  ("information that may needed anywhere") is reproduced verbatim in the
  Claim 4 quote and in Concrete Artifacts, per the verbatim-quoting rule —
  not corrected or flagged as [sic] beyond this note.
