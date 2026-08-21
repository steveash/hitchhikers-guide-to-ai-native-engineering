---
source_url: https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/
source_type: blog-post
title: "There are no lossless transformations of natural-language text"
author: Sophie Alpert (via Simon Willison)
date_published: 2026-08-11
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2833"
---

# There are no lossless transformations of natural-language text

> Sophie Alpert shares an internal policy she wrote at Clay on acceptable use of
> AI writing by engineers: authors must stand behind every sentence in their
> documents because AI rewrites are never lossless — an entity without the
> author's full mental model of intent will lose or distort information every
> time it rephrases, so review, brevity, and personal ownership of meaning are
> the load-bearing safeguards, not AI "polish."

## Source Context

- **Type**: blog-post (Simon Willison "link blog" entry — a short commentary
  post that quotes and links a primary source, on simonwillison.net, a
  designated `trusted-feed` source in this corpus) linking to a full essay by
  Sophie Alpert on her personal blog, sophiebits.com.
- **Author credibility**: Sophie Alpert is the primary author of the linked
  material; the essay states she wrote this "in my work at Clay" as "an
  internal policy on acceptable use of AI writing by engineers" and is sharing
  it externally. This is a first-person practitioner policy document — a
  working engineer describing a rule she authored and applies to her own team
  — not third-party commentary or academic research. Simon Willison, an
  established high-signal corpus source, independently selected and endorsed
  it: "It's a short read (supporting its own recommendations) and really
  good," and singled out the accountability principle (Claim 1 below) as "the
  following rule seems crucial to me." Willison's endorsement is a secondary
  relevance signal on top of Alpert's own first-person authority over her
  team's policy.
- **Scope**: The essay is a short (~600-word), self-contained policy document
  with an italicized framing paragraph, two paragraphs of setup, four bulleted
  principles (each with elaboration), and two closing paragraphs on exceptions
  and future revision. It covers acceptable-use guidance for engineers using
  AI to brainstorm, draft, or proofread written documents (tech specs, status
  updates, incident retrospectives, and general internal docs are named
  explicitly). It does NOT cover AI-generated code (the essay explicitly
  contrasts AI's coding ability against its writing ability), does not name a
  specific enforcement mechanism, and does not define how the policy applies
  to external-facing writing (marketing copy, customer communications) versus
  internal engineering docs — the named examples are all internal
  engineering/product artifacts.

## Extracted Claims

### Claim 1: There are no lossless transformations of natural-language text — every rewrite or rephrase changes meaning, and if the rewriting entity lacks the author's detailed mental model of intent, information is lost
- **Evidence**: Author's central thesis, stated as the title claim and
  elaborated in the "Longer is not better" section as the direct consequence
  of using AI (an entity without the author's mental model) to rewrite text.
- **Confidence**: emerging (a stated first-principles argument from a
  practitioner, not an empirical measurement, but it is the load-bearing,
  most-quoted claim of the piece and is the one Willison highlights)
- **Quote**: "There are no lossless transformations of natural-language text — every rewrite and rephrase changes the meaning of your writing, and if this is done by an entity that doesn't have the most detailed mental representation of what you personally were trying to communicate, information will be lost."
- **Our assessment**: This is a clean, generalizable mechanism (not just an
  assertion that "AI writing is bad") — it locates the failure specifically
  in the gap between the rewriting entity's model of intent and the author's
  actual intent, which is the same underlying mechanism `blog-addyosmani-intent-debt.md`
  (Claim 2) names for code: an agent can only infer a plausible rationale, not
  reproduce the actual one. Alpert applies the identical structural argument
  one layer up, to the *wording itself* rather than to code behavior.

### Claim 2: You must stand behind every idea and every sentence in your docs — it is not acceptable to disclaim AI-authored content when a reviewer questions it
- **Evidence**: Author's first and headline policy principle, with a
  concrete dialogue example of the unacceptable response.
- **Confidence**: emerging (normative policy statement from a practitioner
  who states she enforces it on her own team, not a measured outcome)
- **Quote**: "You must stand behind every idea and every sentence in your docs. It is your responsibility to make sure that the entire document is representative of your own thoughts before you share it. If a reviewer asks, "What did you mean by this line?", it's not acceptable to reply with "Oh sorry, AI wrote that, just ignore it.""
- **Our assessment**: This is the specific, actionable rule the guide should
  quote directly — it converts the abstract "no lossless transformations"
  thesis into a concrete review-time test: can the author defend every line
  as their own thought, on demand? This mirrors — but for prose specifically,
  rather than for project/agent outcomes generally — the human-accountability
  argument in `blog-simonwillison-directly-responsible-individuals.md`
  (Claim 2: an agent should never be the DRI because accountability is
  uniquely human). Alpert's rule is the prose-authorship analogue: authorship
  accountability, like DRI accountability, cannot be outsourced to the model
  that helped produce the artifact.

### Claim 3: Writing is thinking — spending time on the writing process teaches the author more about the topic, and skipping that process (by outsourcing document creation to AI) produces a poorer understanding of the subject matter
- **Evidence**: Author's second policy principle, framing documents as
  "proof of thought" whose value is the thinking process, not just the
  artifact.
- **Confidence**: emerging
- **Quote**: "Writing is thinking. Spending time on the writing process — on deciding what to emphasize and how to structure your ideas clearly — teaches you more about your topic. If you circumvent this process, you will probably walk away with a poorer understanding of the subject matter. In many cases, written artifacts like tech specs, project status updates, and incident retrospectives serve as a "proof of thought". The artifact itself is not the only goal; instead, detailed thinking about the problem is the goal."
- **Our assessment**: This directly parallels `blog-simonwillison-litt-understand-to-participate.md`
  (Claim 3: "you need a rich set of concepts in your mind to think creatively
  and fluently about how to move something forward... your ability to
  participate in the project is meaningfully limited" without that fluency).
  Litt's claim is about reading/reviewing agent-written code; Alpert's is
  about writing prose — both argue that skipping the cognitive labor (via AI)
  degrades the human's own understanding, not just the artifact's quality.
  Together they support a guide principle that applies across both code and
  prose: the process of engaging with material builds understanding that
  cannot be recovered later by reading a finished AI-produced artifact.

### Claim 4: More time should be spent authoring a document than consuming it — generating a long document from a short prompt and asking readers to process the longer output disrespects their time, because the one-to-many ratio of authors to readers makes clarity investment pay multiplicative dividends
- **Evidence**: Author's third policy principle, with an explicit
  time-asymmetry argument (one author's extra editing time vs. every
  reader's saved time).
- **Confidence**: emerging
- **Quote**: "More time should be spent authoring a document than consuming it. If you generate a document from a short prompt then ask your readers to go through the longer output, you are disrespecting their time. They can always talk to ChatGPT themselves if they want to. Most docs are written by one person but are read by many people, so any extra time that readers need to spend to understand what you meant incurs a multiplicative cost on the team's time. Conversely, if you spend extra time to make your document clear and concise before sending it, you are paying a one-time cost that every reader will benefit from."
- **Our assessment**: This is a specific, checkable economic argument (author
  time is a one-time cost, reader confusion is a per-reader recurring cost)
  rather than a vague appeal to conciseness. It is the same generate/evaluate
  cost asymmetry that `blog-ronacher-content-for-contents-sake.md` documents
  independently (Claim 10: "The fact that it was cheap for you to produce
  does not make it cheap for someone else to receive") — Ronacher frames it
  as a platform-flooding problem across many senders/readers; Alpert frames
  the identical mechanism as a one-team, one-document authorship discipline.
  The two sources corroborate each other from different angles (external
  content platforms vs. internal team documents).

### Claim 5: Longer is not better — AI makes it easy to generate long documents, and one of its characteristic failure modes is including sentences that don't say much and detract from the actual content
- **Evidence**: Author's fourth policy principle, opening statement before
  the lossless-transformations argument (Claim 1) and a quoted aphorism from
  Pascal.
- **Confidence**: emerging
- **Quote**: "Longer is not better. Pascal once wrote, "I have made this [letter] longer than usual because I have not had time to make it shorter." AI makes it much easier to generate a long doc, and one of its strategies is to include many sentences that don't say much at all and detract from the actual content."
- **Our assessment**: This is a specific, actionable diagnostic for reviewers
  and authors: verbosity in AI-assisted writing should be treated as a
  content-quality warning sign, not a neutral byproduct of thoroughness. The
  practical recommendation that follows — "if you are producing a longer
  piece of writing from a shorter prompt, consider instead just sharing the
  prompt itself" — is a concretely actionable alternative to publishing
  AI-expanded prose, worth citing directly in any guide section on
  AI-assisted documentation practices.

### Claim 6: It is allowed to use AI tools while brainstorming, drafting, or proofreading writing, provided the author applies the accountability, thinking, time-asymmetry, and length principles above while doing so
- **Evidence**: Author's explicit statement of what AI use is permitted under
  the policy, positioned directly before the four bulleted principles.
- **Confidence**: emerging
- **Quote**: "It's allowed to use AI tools while brainstorming or drafting your writing and certainly while proofreading, but make sure to consider the following principles while doing so"
- **Our assessment**: This establishes the policy is not an AI-writing ban —
  it is a conditional-use policy scoped to specific stages (brainstorm,
  draft, proofread) with the four principles (Claims 2–5) as the compliance
  conditions. This distinguishes Alpert's policy from
  `blog-simonwillison-kenton-varda-change-descriptions.md` (Claim 1: Kenton
  Varda's team fully banned AI-written change descriptions after finding them
  "worse than useless"). Alpert's policy is more permissive in structure
  (conditional use with review obligations) than Varda's team's response
  (outright moratorium on a specific artifact type), though both are reactions
  to the same underlying risk — AI-generated text failing to carry the
  author's actual intent.

### Claim 7: It is acceptable to quote AI generations verbatim, even ones that don't meet the accountability standard, as long as they are clearly marked as AI-originated rather than presented as the author's own thoughts
- **Evidence**: Author's explicit carve-out, stated immediately after the
  four bulleted principles, with a worked example phrase.
- **Confidence**: emerging
- **Quote**: "It's also OK to quote AI generations verbatim that don't meet the above standards if you mark them clearly as such. Sometimes it's useful to say like "Claude offered this idea, do you think it's worth looking more into?", and this is allowed."
- **Our assessment**: This is the disclosure mechanism that resolves the
  apparent tension between Claim 2 (you must stand behind every sentence) and
  wanting to surface an AI-generated idea that the author isn't ready to
  personally endorse: label it explicitly as the AI's contribution rather
  than presenting it as the author's own thought. This is the same mechanism
  `blog-ronacher-content-for-contents-sake.md` recommends independently
  (Claim 8: "Transparency in either direction, when there is ambiguity, can
  help great lengths") — both sources converge on disclosure/labeling as the
  practical safeguard, rather than a blanket prohibition on ever showing raw
  AI output to a reader.

### Claim 8: The policy is explicitly framed as provisional to current (2026) AI capability — as AI tools improve at theory of mind and writing quality, it may make sense to rely on them more heavily, but the stated principles will remain important
- **Evidence**: Author's closing sentence, immediately following the essay's
  substantive policy content.
- **Confidence**: emerging
- **Quote**: "As AI tools improve over time at theory of mind and get better at writing, it may make sense to lean more heavily on them, but the principles above will remain important."
- **Our assessment**: This is a notable self-limiting claim: Alpert
  distinguishes between the *degree* of AI reliance (which she expects to
  change as capability improves) and the *principles themselves*
  (accountability, writing-as-thinking, reader-time respect, and concision),
  which she frames as durable regardless of model capability. For the guide,
  this argues the practices extracted here should be framed as durable
  authorship-accountability norms, not as a stopgap that will become obsolete
  once models improve — the essay itself pre-empts that reading.

### Claim 9: As of 2026, AI models — despite their coding ability — are not yet able to produce unedited writing output that reliably conveys the author's actual intended ideas, structure, and emphasis
- **Evidence**: Author's framing statement in the second paragraph of the
  essay, explicitly contrasting AI coding ability against AI writing ability.
- **Confidence**: emerging
- **Quote**: "As of 2026, AI models — despite their coding ability — are not yet at a point where their unedited output will achieve this goal; you as an author need to take the time to make sure that all of the ideas in the writing are the ideas that you personally intend to convey (including the structure and wording that determines which ideas are emphasized) and that the documents are a good use of your readers' time."
- **Our assessment**: This is a specific, time-bound capability claim (a
  practitioner's assessment as of 2026, not a permanent one) that explicitly
  separates two AI capability domains — code generation and natural-language
  writing — and asserts they are not at parity. This is a useful caveat for
  the guide: this source's evidence is about AI writing quality specifically,
  and should not be read as extending to (or contradicting) the corpus's
  separate body of evidence on AI coding capability.

## Concrete Artifacts

### Full verbatim policy text (Sophie Alpert, sophiebits.com, June 25, 2026)

```
Source: https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text
Fetched directly via raw HTML (not summarized) to verify verbatim quotes.

In my work at Clay I recently wrote an internal policy on acceptable use of
AI writing by engineers, and I'm sharing it here. It's my hope that one day
better AI tools might be able to help us think, but until then I fear that
using AI to write does the exact opposite.

Good writing is a tool to clearly communicate ideas from your brain into
someone else's.

As of 2026, AI models — despite their coding ability — are not yet at a
point where their unedited output will achieve this goal; you as an author
need to take the time to make sure that all of the ideas in the writing are
the ideas that you personally intend to convey (including the structure and
wording that determines which ideas are emphasized) and that the documents
are a good use of your readers' time.

It's allowed to use AI tools while brainstorming or drafting your writing
and certainly while proofreading, but make sure to consider the following
principles while doing so:

  - You must stand behind every idea and every sentence in your docs. [...]
  - Writing is thinking. [...]
  - More time should be spent authoring a document than consuming it. [...]
  - Longer is not better. [...] There are no lossless transformations of
    natural-language text — every rewrite and rephrase changes the meaning
    of your writing [...]

It's also OK to quote AI generations verbatim that don't meet the above
standards if you mark them clearly as such. Sometimes it's useful to say
like "Claude offered this idea, do you think it's worth looking more into?",
and this is allowed.

As AI tools improve over time at theory of mind and get better at writing,
it may make sense to lean more heavily on them, but the principles above
will remain important.

(Full text of the four bulleted principles reproduced verbatim in the
Extracted Claims section above — elided here to avoid duplication.)
```

### Simon Willison's link-post framing (simonwillison.net, August 11, 2026)

```
Source: https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/

Sophie Alpert shares her "internal policy on acceptable use of AI writing by
engineers". It's a short read (supporting its own recommendations) and
really good.

If you chose to have LLMs help massage your writing the following rule
seems crucial to me:

  "You must stand behind every idea and every sentence in your docs. It is
  your responsibility to make sure that the entire document is
  representative of your own thoughts before you share it."

The "no lossless transformations" idea from the post title is expanded on
here:

  "There are no lossless transformations of natural-language text — every
  rewrite and rephrase changes the meaning of your writing"

Tags: writing, ai, generative-ai, llms, ai-misuse
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-directly-responsible-individuals.md` (Claim 2:
    "an agent should never be considered the DRI for a project... because
    humans can take accountability for their actions where machines
    cannot"). Alpert's Claim 2 (you must stand behind every sentence,
    disclaiming AI authorship to a reviewer is not acceptable) is the
    prose-authorship instance of the same human-only-accountability
    principle Willison argues at the project-outcome level.
  - `blog-addyosmani-intent-debt.md` (Claim 2: "An agent can't generate
    intent... A model can infer a plausible rationale from the code... A
    guess about intent isn't the intent"). Alpert's Claim 1 (the lossless-
    transformations thesis) is the identical structural argument applied to
    prose rewriting rather than code: an entity without the author's actual
    mental model can only approximate intent, and that approximation loses
    information.
  - `blog-simonwillison-litt-understand-to-participate.md` (Claim 3: a
    developer needs a "rich set of concepts" in mind to think creatively
    about a project, or their ability to participate is "meaningfully
    limited"). Alpert's Claim 3 (writing is thinking; circumventing the
    writing process leaves you with a poorer understanding) makes the
    parallel argument for prose authorship: skipping the cognitive labor via
    AI degrades the human's own understanding, independent of code vs. prose
    domain.
  - `blog-ronacher-content-for-contents-sake.md` (Claim 10: "The fact that
    it was cheap for you to produce does not make it cheap for someone else
    to receive"; Claim 8: "Transparency in either direction, when there is
    ambiguity, can help great lengths"). Alpert's Claim 4 (reader-time
    asymmetry favors author-side effort) and Claim 7 (mark AI-verbatim
    content clearly) independently converge on the same two mechanisms —
    generate/evaluate cost asymmetry and disclosure-as-safeguard — from a
    different context (internal team docs vs. public platform content).
- **Contradicts**: None identified. No existing corpus note argues that
  unedited or lightly-reviewed AI-generated prose reliably preserves an
  author's intended meaning, or that authorship accountability for written
  content can be delegated to the AI tool that helped produce it.
- **Extends**:
  - `blog-simonwillison-kenton-varda-change-descriptions.md` (Claim 2:
    Varda's team found AI-written change descriptions "outlining details of
    the code that could easily be seen by looking at the code, but omitting
    the higher-level framing needed to understand broadly what the code is
    doing"). Varda's report is a concrete, named-practitioner failure
    instance of exactly the mechanism Alpert's Claim 1 predicts in the
    abstract (an AI rewriting/summarizing without the author's actual intent
    loses the information that mattered) — but for a narrower artifact type
    (PR/commit/issue text) than Alpert's broader policy (tech specs, status
    updates, incident retrospectives, general internal docs).
- **Novel**: This is the first corpus source to state a general,
  first-principles argument for *why* AI-assisted rewriting of prose loses
  information (the "no lossless transformations" mechanism, Claim 1), and
  the first to propose a complete, adoptable team policy specifically for
  AI-assisted *writing* (as distinct from AI-assisted *coding*), including a
  concrete disclosure mechanism (Claim 7) and an explicit self-limiting
  scope statement tied to current model capability (Claim 8).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The guide's documentation-writing
  guidance (tech specs, status updates, incident retrospectives, PR/design
  docs) currently lacks an explicit AI-assisted-writing policy. Recommend
  adding Alpert's four-principle structure (Claims 2–5) as a concrete,
  adoptable team policy: (1) authors must be able to defend every sentence
  on demand, (2) AI-assisted drafting doesn't excuse skipping the
  understanding-building work of writing, (3) author effort should exceed
  reader effort, (4) verbosity from AI-assisted drafting is a warning sign,
  not a neutral byproduct. Pair with Claim 7's disclosure mechanism ("Claude
  offered this idea...") as the practical way to surface AI-generated ideas
  without violating the ownership principle.
- **Chapter 02 (Harness Engineering)**: Claim 9's explicit split between AI
  coding capability and AI writing capability is a useful scoping caveat:
  guide sections that recommend trusting AI output more readily for code
  (given the corpus's extensive verification-of-code material) should not be
  read as extending the same trust level to AI-assisted prose without the
  additional review discipline this source describes.
- **Chapter 05 (Team Adoption)**: Recommend citing this source alongside
  `blog-simonwillison-kenton-varda-change-descriptions.md` as two concrete,
  adoptable team-level responses to the same underlying risk (AI-rewritten
  text losing the author's actual intent) — one a conditional-use policy
  with review principles (Alpert), the other an outright ban on a specific
  artifact type after the conditional approach apparently wasn't tried or
  didn't hold (Varda). The guide should frame Alpert's policy as the
  proactive, adoptable middle path between "no restrictions on AI writing"
  and "ban AI from writing tasks entirely."

## Extraction Notes

- The issue's given source URL is Simon Willison's link-blog post, which is
  brief (a short framing paragraph plus two short quotes). Per MINER.md §1
  ("follow up to 5 linked pages that seem substantive"), I followed the
  single substantive link in the post — Sophie Alpert's full essay at
  sophiebits.com — and treated it as the primary content source, since
  nearly all of the guide-relevant material lives there rather than in
  Willison's short commentary. The frontmatter `source_url` is kept as the
  originally-triaged simonwillison.net URL (consistent with how this corpus
  treats other Willison link-blog entries, e.g.
  `blog-simonwillison-kenton-varda-change-descriptions.md` and
  `blog-simonwillison-litt-understand-to-participate.md`); Alpert's essay
  URL and its full text are captured in Concrete Artifacts and cited
  directly in every claim drawn from it.
- Both pages were fetched twice: once via WebFetch (which returned
  paraphrased/summarized text for both the Willison post and Alpert's essay
  — the Alpert-essay WebFetch summary in particular restructured the content
  into invented section headings not present in the source and would have
  produced fabricated quotes if used directly) and once via direct `curl`
  against the raw HTML, with the actual article markup parsed by hand. All
  quotes in this note are taken from the raw-HTML extraction of each page,
  not from either WebFetch summary, per MINER.md §2a's quote-verification
  requirement.
- All four cross-referenced source notes (`blog-simonwillison-directly-responsible-individuals.md`,
  `blog-addyosmani-intent-debt.md`, `blog-simonwillison-litt-understand-to-participate.md`,
  `blog-ronacher-content-for-contents-sake.md`, `blog-simonwillison-kenton-varda-change-descriptions.md`)
  were read in full and claim numbers verified directly against their
  `### Claim N:` headings before citing, per MINER.md §4b.
  `blog-anthropic-ciso-guide-agentic-ai.md`, flagged by one Prospector triage
  pass as a possible overlap, was not cited: on review it addresses agent
  security governance, not documentation/writing authorship, and no specific
  claim in it matches this source's content closely enough to cite without
  overreaching.
- No contradiction with any existing corpus note was found (see
  Cross-References → Contradicts), so no contradiction issue was filed.
- Confidence is set to `emerging` for the note overall: the essay is a
  first-person, practitioner-authored policy document (not third-party
  research or a controlled study), and every claim is a stated position
  Alpert applies to her own team, not a measured or independently verified
  outcome — but it is a complete, self-consistent, adoptable policy from a
  named practitioner describing a live internal decision, which is stronger
  evidentiary footing than a one-off anecdote or unelaborated opinion.
