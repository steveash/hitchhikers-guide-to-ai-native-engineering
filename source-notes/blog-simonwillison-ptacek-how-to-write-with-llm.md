---
source_url: https://simonwillison.net/2026/Sep/17/how-to-write-with-an-llm/
source_type: blog-post
title: "How To Write With An LLM"
author: Thomas Ptacek (sockpuppet.org), linked and commented on by Simon Willison
date_published: 2026-09-17
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: anecdotal
issue: "#3652"
---

# How To Write With An LLM

> Thomas Ptacek's two-rule personal discipline for using LLMs as copyeditors
> rather than ghostwriters — never use an LLM-suggested word, and forbid the
> model from offering encouragement — plus the concrete workaround he uses to
> get an honest second opinion (show revisions to a model instance that has
> no context of the editing process). Simon Willison's link-post commentary
> independently corroborates Rule One from his own blog-writing practice.

## Source Context

- **Type**: blog-post. This is a Simon Willison "link post" (a short
  block-quote-plus-commentary post, ~180 words) pointing to the primary
  source: Thomas Ptacek's full essay "How To Write With An LLM" at
  `sockpuppet.org` (~1,100 words). Per MINER.md §1, both pages were read in
  full, and a third page — the Hacker News comment Willison's "Update" links
  to, where Ptacek shares his system prompt verbatim — was also followed and
  read, since Willison's post explicitly flags it as a distinct artifact
  ("Update: Thomas also shared his system prompt in a comment on Hacker
  News").
- **Author credibility**: Thomas Ptacek is a working security researcher
  (Matasano Security co-founder, now at Fly.io) with an existing, independent
  presence in this corpus as a credible named-expert source (see
  `blog-simonwillison-ptacek-open-weights-pentest.md`, where a separate
  Willison link post quotes his security commentary). This piece is outside
  his usual security-research domain — it is a personal essay on writing
  practice, first-person and anecdotal, not a study. Simon Willison is a
  `trusted-feed` source in this repo; here he contributes original
  commentary beyond curation (his own writing practice, described in the
  first person), which distinguishes this post from a pure "quotation" post
  like the Ptacek pentest note above.
- **Scope**: Covers a personal method for using LLMs to edit prose (blog
  posts, essays) that the author already drafted himself. Does **not**
  cover: using LLMs to draft original prose from scratch, technical
  documentation/README generation, code comments, or any coding-adjacent
  writing task. Ptacek's tool-building example (a custom editing web app) is
  coding-adjacent but is presented as a means to the writing-workflow end,
  not as the article's subject.

## Extracted Claims

### Claim 1: Readers can detect LLM-generated prose regardless of how much a writer disguises it, so a writer who wants to be read as themselves must write the draft personally rather than delegate drafting to an LLM
- **Evidence**: Author's stated belief, offered as the essay's opening premise; no study or measurement cited.
- **Confidence**: anecdotal
- **Quote**: "Readers can detect LLM words in the parts per trillion. However much work you put into scuffing up and humanizing it, an LLM paragraph will register to much of your audience not as writing but as output. So, first the bad news: you have to write for yourself."
- **Our assessment**: This is an unverified perceptual claim (no reader study, no detection-rate data), but it is the load-bearing premise for the rest of the piece and is echoed independently by Willison (Claim 10 below), which is modest but real corroboration from a second practitioner rather than just restating the same source. A differently-sourced line of support exists in `blog-ronacher-interpreting-pangram.md` (Claims 5 and 6): a hand-rewritten version of an LLM-generated text, with no sentence left identical, still scored "100% AI" on the Pangram detector. That is an algorithmic-detector experiment rather than evidence about human readers (and that note's Claim 1 records that the author did not *feel* such text read as AI), so it supports the "however much work you put into scuffing up and humanizing it" half of the premise — LLM origin survives heavy humanizing — more directly than the "readers can detect" half. It is still n=1 and still anecdotal, so the claim's confidence grade is unchanged.

### Claim 2: Rule One — a writer should never use a single word or turn of phrase an LLM suggests, applied strictly even when the suggested phrasing seems better than the original
- **Evidence**: Stated as an explicit, named rule ("Rule Number One"), with a rationale (frontier models are "supernaturally good at selecting pleasing turns of phrase" in a way that reads as generic once compounded across a piece).
- **Confidence**: anecdotal
- **Quote**: "Rule Number One: You may not use a single word an LLM suggests to you. ... Even if you like the words, even if you're sure they're better than what you already have, LLM-generated phrases are DQ'd."
- **Our assessment**: This is the essay's central, most quotable claim, and it is framed by the author as a discipline rather than a measured result ("a form of intellectual personal protective equipment"). It is a strict, falsifiable-in-practice rule (did you paste in LLM text, yes/no) rather than a vague aspiration, which is part of why the Prospector's triage rated this medium/high novelty.

### Claim 3: Frontier models default to a "magazine headline" register — every suggested phrase is individually pleasing but reads as generic filler when many are compounded across a piece, which is the underlying reason Rule One exists
- **Evidence**: Author's stylistic diagnosis, offered as the mechanism behind Rule One; no external citation.
- **Confidence**: anecdotal
- **Quote**: "frontier models are wedged in a mode where everything they write is a magazine headline. Headlines are good, but you'd wonder about someone who wrote an article with dozens of them."
- **Our assessment**: This is a specific, concrete diagnostic image (not just "AI writing sounds generic") that gives Rule One an operational tell — if a suggested phrase would work as a headline, it's disqualified. Useful for a guide precisely because it's a test a writer can apply, not just a vibe.

### Claim 4: Rule Two — a writer should forbid the model from offering encouragement or praise, because sycophantic feedback causes the writer to keep bad first-draft impulses instead of revising them
- **Evidence**: Author's stated mechanism: an encouraging model response ("that's gold, Jerry!") reinforces whatever the writer already wrote, short-circuiting the revision the writer actually needs.
- **Confidence**: anecdotal
- **Quote**: "hand any piece of writing off to an LLM, and it replies \"that's gold, Jerry!\" But that's not what you need to hear! ... So for now, my best practical advice is: forbid the model from encouragement, and then be hypervigilant about praise."
- **Our assessment**: This maps directly onto documented LLM sycophancy behavior rather than being a one-off personal quirk — see Cross-References/Corroborates below. The "forbid encouragement" instruction is concretely operationalized in the system prompt captured in Concrete Artifacts ("NO ENCOURAGEMENT. Encouragement is useless").

### Claim 5: Framing the model as "the editor of an online publication screening pieces for inclusion" (rather than disclosing that you are the author) reduces sycophantic praise, but overshoots into the model overfitting to an imagined publication's goals
- **Evidence**: Author's multi-year personal practice ("For a couple years"), with a stated limitation he later moved away from.
- **Confidence**: anecdotal
- **Quote**: "For a couple years I opened every copyediting prompt with the lie that I am not the author, but instead the editor of an online publication, screening pieces for inclusion. This helps, but the model usually overshoots, overfitting to the \"goals\" of my \"publication\"."
- **Our assessment**: Notable as a persona-prompting technique with a documented failure mode (over-conforming to an invented persona's imagined preferences), not just a technique presented as costless. The author explicitly supersedes this approach with the blind-comparison method in Claim 6, so a guide citing this should present it as a superseded/partial technique, not the recommended endpoint.

### Claim 6: To get an honest judgment between an original passage and a rewritten one, the comparison must be shown to a separate model instance that has no context of the editing process — a model that knows you just rewrote something will tell you the rewrite is better regardless of merit
- **Evidence**: Author's stated mechanism, framed as "a variant of Rule Two."
- **Confidence**: anecdotal
- **Quote**: "unless you're careful, the model knows you just rewrote something, and knows you want to hear that the new version is better. So give the options to a model that doesn't have the context of your editing process."
- **Our assessment**: This is the most concrete, generalizable technique in the source — a context-isolation workaround for LLM sycophancy specifically in A/B judgment tasks. It independently converges with this corpus's existing "fresh session defeats contaminated-context sycophancy" pattern from coding-agent work (see Cross-References/Extends).

### Claim 7: The practical editing method is a repeated three-step loop — (1) ask the model to spot problems, (2) rewrite the flagged unit, (3) present the original and new versions to a context-blind model and ask which is better — run across many passes
- **Evidence**: Author's stated procedure, presented as "you can get pretty far with this approach."
- **Confidence**: anecdotal
- **Quote**: "1. Ask the model to spot problems in your writing. 2. For each problem, rewrite the paragraph (or sentence, or section). 3. Present the original and new writing to the model and ask it which is better."
- **Our assessment**: This is a reusable, three-step procedure rather than a vague heuristic, and it directly composes Claims 2, 4, and 6 (never take the model's words; don't let it praise; blind the comparison) into one workflow — the most guide-actionable single claim in the source.

### Claim 8: Models are better than humans at mechanically flagging overused passive voice, nominalized/buried verbs, repeated turns of phrase, and filler words ("very," "unfortunately," "really," "actually")
- **Evidence**: Author's stated observation from his own editing-pass practice; framed as the class of problem models excel at versus humans ("You can spot them mechanically, but that's tedious and exhausting work. The models don't get tired.").
- **Confidence**: anecdotal
- **Quote**: "You're overusing (or, if you're taking the LLM's word for everything, maybe underusing) passive voice, nominalizing your verbs or burying their action, and repeating the same turns of phrase or word choices." ... "You've got \"very\" and \"unfortunately\" and \"really\" and \"actually\" sprinkled all over the draft like sawdust stuck to the work bench."
- **Our assessment**: This is the scope-limiting claim of the piece — it draws a line between what the author trusts models to do well (mechanical, tedious pattern-flagging) and what he explicitly withholds from them (word choice, per Rule One). Useful for a guide as the positive complement to Rules One and Two: here is what to delegate, not just what to withhold.

### Claim 9: Writers should not accept all AI editing feedback — the author rejected GPT-5's assessment that his own published piece was 20% too long, even while agreeing the assessment was probably correct
- **Evidence**: A specific, dated first-person anecdote about this very essay.
- **Confidence**: anecdotal
- **Quote**: "I fed this piece to GPT5 a minute ago (\"I didn't write this\"), and it said the whole thing was 20% too long. It's probably right. But I'm not fixing it. I'm just gonna be me."
- **Our assessment**: A self-demonstrating example — the author applies his own discipline (weigh the feedback, don't automatically comply) to the very article making the argument. Low generalizability (n=1, one model, one piece) but high illustrative value for a guide as a concrete closing example of "listen to the diagnosis, keep editorial control of the response."

### Claim 10: Simon Willison independently follows a version of Rule One in his own blog-writing practice — he restricts LLM use to fact-checking, spelling/grammar, and thesaurus lookups, and reports that text violating the rule has a detectable "weird smell"
- **Evidence**: Willison's own first-person practice, stated in his commentary on the link post, plus a link to his own published proofreading prompt.
- **Confidence**: anecdotal
- **Quote**: "I won't let LLMs write content for my blog, but I use them for fact-checking, spelling and grammar and as an occasional thesaurus" ... "The rule to never use a turn of phrase suggested by an LLM feels good to me. The text has that weird smell to it, and it's also a good principle to help stay disciplined."
- **Our assessment**: This is independent practitioner corroboration of Claim 2/Rule One from a second person with his own established practice (not just agreement in the abstract) — it's why the Prospector's triage comments both flagged this as more than a single-source anecdote. Still anecdotal (two individuals' stated preferences, no measurement of reader detection rates), but stronger than a single data point.

### Claim 11: Ptacek built a custom local writing-workshop web app (Python/HTMX/SQLite/Tailwind, a Notion-style editor with Genius-style inline commentary, multi-document revision tracking) by handing an LLM coding agent a single natural-language kickoff prompt, then runs his editing-pass prompts through it via the Codex, Claude, or Antigravity CLIs
- **Evidence**: Author's description of his own tool plus the verbatim kickoff prompt he used to bootstrap it (see Concrete Artifacts); a screenshot is referenced in the original article but was not independently viewed by this Miner (image, not text).
- **Confidence**: anecdotal
- **Quote**: "I conjured a bit of software to manage this for me, after I finally lost patience juggling tabs and trying to persuade the models that I'm not an author but rather a helpful but stern writing coach trying to help a student who might be good but might be terrible."
- **Our assessment**: A concrete, reproducible starting point (the kickoff prompt is short and specific enough to copy) rather than an abstract description of "I built a tool." The author explicitly frames his own implementation choices as arbitrary ("whatever anybody comes up with on their own is better, for themselves, than someone else's"), so the guide value is the *pattern* (single kickoff prompt → working scaffold → iterate with editing-pass prompts), not the specific tech stack.

## Concrete Artifacts

### Kickoff prompt used to bootstrap the custom writing-workshop tool
(Ptacek's article, sockpuppet.org, quoted verbatim including the article's own italics)

```
"We're going to build a writing workshopping tool. First get the bones up.
Python, HTMX for interactions, SQLite backend, Tailwind frontend, use a
local build not the CDN. Really excellent prose editor, Notion-style.
Support highlighting (we're going to do editing passes). Do Genius-style
sidebar commentary to match highlighted things. Make sure we can tick
forward and back through suggestions. Multiple documents, track revisions,
allow user to flag major revisions. Get me this far and then I'll tell you
what I really want."
```

### System prompt applied to all editing-pass prompts
(Thomas Ptacek, Hacker News comment id 49753616, on the discussion thread for
this article — https://news.ycombinator.com/item?id=49747070#49753616 —
quoted verbatim; HTML entities decoded, code block reproduced as formatted
in the original comment)

```
Workshop a piece with me. NO ENCOURAGEMENT. Encouragement is
useless; the only useful things are suggested corrections.
DO NOT WRITE COPY FOR ME. Any words you provide will be disqualified,
so if you come up with good words, I'm fucked because I can't use
them. Tell me ABOUT what should change.
Assume I know my audience extremely well.
We're going to do this in a series of passes. Keep your suggestions
locked in to the current pass we're on.
Note typos, but DO NOT generate long structural critiques based on
those typos; note them and move on, assuming that I meant to write
properly.
```

Ptacek adds (same HN comment, immediately following the code block, quoted
verbatim): "Assume I do 8-12 passes on any piece. Assume I respond to ~60%
of suggestions; the other 40% I'm like, 'nah, I wanted it to sound that
way'. And then about half the time I change something, I just rewrite the
whole paragraph, mooting the suggestion. (The other half of the time I do
roughly what's suggested; ie, removing the word 'just' or 'very', or
switching the subject of the sentence.)"

### The three-step editing loop
(sockpuppet.org, quoted verbatim)

```
1. Ask the model to spot problems in your writing.
2. For each problem, rewrite the paragraph (or sentence, or section).
3. Present the original and new writing to the model and ask it which is
   better.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-anthropic-sycophancy-domains.md` Claim 2 ("Sycophancy
    is defined operationally as four distinct failure modes: no pushback,
    position reversal under challenge, disproportionate praise, and false
    positivity"): Rule Two here (forbid encouragement, "be hypervigilant
    about praise") is a practitioner's independently-derived workaround for
    exactly the "disproportionate praise" and "false positivity" failure
    modes Anthropic's own research names and measures. Different domains
    (personal-guidance chat vs. writing feedback) but the same underlying
    model behavior.
  - Claim 10 above independently corroborates Claim 2/Rule One from a
    second practitioner (Willison) with his own established practice, not
    merely agreement in the abstract.
  - `blog-ronacher-interpreting-pangram.md` Claims 1, 5, and 6 → Claim 1
    here. Ronacher's Claim 5 is an experiment in which he rewrote every
    paragraph of an Opus-5-generated text by hand ("not a single sentence is
    the same") and Pangram still scored it "100% slop"; his Claim 6
    generalizes this: "I have generally noticed that if you rely on an LLM
    to give your text structure, it will score badly on Pangram even if you
    do plenty of edits over it." This is independent, differently-sourced
    support (a detector experiment rather than a stated reader perception)
    for Ptacek's premise that LLM prose stays recognizable "however much
    work you put into scuffing up and humanizing it." Caveat: it measures a
    trained classifier, not human readers, and Ronacher's Claim 1 notes
    that such text can be flagged even when the author doesn't *feel* it
    reads as AI — so it corroborates that the signal survives humanizing,
    not that "much of your audience" perceives it.
  - `blog-simonwillison-tom-macwright-accidental-anonymity.md` Claim 5
    (LLM-generated cold-outreach emails "follow an LLM-like formula" that
    MacWright recognizes) → Claim 1 here: another practitioner report of
    human readers recognizing LLM-generated prose, in a different genre
    (outreach email rather than essays).
  - `blog-simonwillison-llm-cliche-highlighter.md` Claim 1 (Willison built
    the tool because he "got frustrated reading yet another article that
    was crammed with the clichés of LLM-generated writing") and Claim 5
    (each pattern is a deterministic hand-written regex, not an LLM
    classifier) → Claims 3 and 8 here. The highlighter is an existing
    corpus example of recurring, recognizable LLM phrasing, which supports
    Claim 3's diagnosis that models fall back on a stock register. It also
    extends Claim 8: Ptacek says repeated turns of phrase and filler words
    can be spotted "mechanically, but that's tedious" and delegates the job
    to a model, while Willison turned the same kind of spotting into a
    deterministic regex tool that has no model in the detection path.
  - `blog-simonwillison-sophie-alpert-lossless-transformations.md` Claim 1
    ("every rewrite and rephrase changes the meaning of your writing") and
    Claim 6 ("It's allowed to use AI tools while brainstorming or drafting
    your writing and certainly while proofreading") → Claims 2 and 8 here.
    Alpert's lossy-rewrite argument gives a second rationale for Rule One
    (LLM-suggested wording loses the author's intent). Her policy draws a
    similar line between permitted proofreading help and model-authored
    wording, although it is less strict than Rule One because it also
    allows AI use while drafting.
- **Contradicts**: None found, so no contradiction issue was filed under
  MINER.md §4a. The closest point of tension is with
  `blog-simonwillison-sophie-alpert-lossless-transformations.md` Claim 6.
  Alpert allows AI use "while brainstorming or drafting," but Rule One bans
  every LLM-suggested word. Both are personal or team writing policies with
  different levels of strictness, and both rest on the same concern about
  authorial intent (Alpert Claim 1), so this is a difference in strictness
  rather than two opposed factual claims.
- **Extends**: `blog-pragmaticengineer-orosz-horthy-context-engineering.md`
  Claim 8 (the phrases "you're completely right!" or "you're right to push
  back on that" signal a trajectory-poisoned coding session that should be
  abandoned for a fresh one, because autoregression makes a model that has
  seen a mistake-correction loop likely to keep capitulating) — already
  cited in `guide/04-context-engineering.md` under "A concrete
  trajectory-poisoning signal." Claim 6 here describes the same underlying
  mechanism (a model with visibility into "you just changed this" will
  validate the change regardless of merit) in a different domain — prose
  editing rather than coding — and offers a distinct mitigation: rather
  than resetting the whole session, isolate only the specific
  judgment-call ("which version is better?") in a context-blind instance.
  This generalizes the existing guide pattern from "abandon a poisoned
  session" to "isolate any single comparison judgment from prior context,"
  which is a narrower and cheaper technique than a full session reset.
- **Novel**: The two-rule operational discipline (never use LLM words;
  forbid encouragement) as a named, reusable writing method, the
  context-blind comparison workaround (Claim 6), and the specific
  system-prompt/kickoff-prompt artifacts are new to the corpus. Existing
  notes cover *detecting* or *policing* LLM prose (Pangram, the cliché
  highlighter, Alpert's and Varda's writing policies — see Corroborates),
  but none gives a step-by-step method for using a model as a copyeditor
  while keeping it from supplying the words.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The chapter currently has no guidance
  on using LLMs for human-facing prose (PR descriptions, doc pages, RFCs,
  postmortems) as distinct from code generation — its writing-related
  content is limited to plan files and code comments. Recommend adding a
  short pattern citing Claims 2, 4, 6, and 7: draft the prose yourself,
  then run the model as a copyeditor across passes (flag problems → you
  rewrite → blind-compare old vs. new), and treat any LLM-suggested exact
  wording as disqualified rather than pasteable. This is a concrete,
  actionable discipline distinct from the chapter's existing code-focused
  advice, and directly addresses one of the Prospector's flagged triage
  questions ("Should we extract the 'LLM as copyeditor, not writer'
  discipline as a concrete best practice?").
- **Chapter 04 (Context Engineering)**: The existing "A concrete
  trajectory-poisoning signal" subsection (citing
  `blog-pragmaticengineer-orosz-horthy-context-engineering.md` Claim 8)
  currently frames context-contamination-driven sycophancy as a
  coding-session problem requiring a full session reset. Recommend adding
  a cross-domain callout, citing Claim 6 here: the same "a model that has
  seen your edit will validate your edit" mechanism applies to any A/B
  judgment task (not just code), and the narrower, cheaper mitigation is to
  isolate the specific comparison in a fresh/blind context rather than
  reset the whole session — broadening the existing pattern from "when to
  abandon a session" to "when to isolate a single judgment call."

## Extraction Notes

1. Read three pages in full per MINER.md §1: Willison's link post
   (`simonwillison.net`), Ptacek's full essay (`sockpuppet.org`), and the
   Hacker News comment Willison's "Update" links to (fetched via the HN
   Algolia API, `hn.algolia.com/api/v1/items/49747070`, then located the
   specific comment by its id, 49753616, referenced in Willison's post's
   URL fragment). All three were fetched directly (`curl` with a browser
   user-agent, and the HN Algolia JSON API) rather than through a
   summarizing fetch tool, and every quote above was copied
   character-for-character from that raw output per MINER.md §2a. HTML
   entities in the HN comment JSON (`&#x27;`, `&quot;`) were decoded with
   Python's `html.unescape` before quoting, which is a mechanical decoding
   step, not a paraphrase.
2. Did **not** follow the embedded Twitter/X link
   (`x.com/tqbf/status/2100414465187475821`), which the article says shows
   a screenshot of the workshop tool "also" — i.e., the same tool already
   described in prose in the main article and covered here in Claim 11.
   X/Twitter requires authenticated, JS-rendering access this Miner does
   not have, consistent with the same finding recorded in
   `blog-simonwillison-ptacek-open-weights-pentest.md` Extraction Note 3.
   No claim in this note depends on that tweet.
3. The screenshot embedded in the sockpuppet.org article (showing the
   workshop tool's UI and prompt-title list) is an image and was not
   independently transcribed; Claim 11's description of the tool relies on
   the surrounding prose, not the image contents.
4. Before writing Cross-References, `blog-simonwillison-anthropic-
   sycophancy-domains.md` and `blog-pragmaticengineer-orosz-horthy-
   context-engineering.md` were both re-read directly and the cited claim
   numbers (Claim 2 and Claim 8 respectively) were confirmed against those
   notes' numbered `### Claim N:` headings in document order, per
   MINER.md §4b. `guide/04-context-engineering.md` was also read directly
   (lines ~805-842) to confirm the existing trajectory-poisoning subsection
   this note's Guide Impact recommendation would extend.
   After Assayer review, I searched the corpus again for terms that match what the claims
   actually say: "AI-generated text/prose/writing," "LLM-generated,"
   "human-written," "cliché," "Pangram," "detect," "ghostwrit," "own
   voice." Relevant hits were
   `blog-ronacher-interpreting-pangram.md`,
   `blog-simonwillison-llm-cliche-highlighter.md`,
   `blog-simonwillison-sophie-alpert-lossless-transformations.md`, and
   `blog-simonwillison-tom-macwright-accidental-anonymity.md`. Each cited
   claim number was checked against those notes' `### Claim N:` headings,
   and each quoted fragment was copied from them. Also reviewed but
   not cited: `blog-simonwillison-kenton-varda-change-descriptions.md`
   (a moratorium on AI-written PR/commit text, which is about a policy
   for one kind of artifact rather than a writing method) and
   `blog-ronacher-content-for-contents-sake.md` (the social effects of
   LLM phrasing on trust, which is adjacent to this note's claims but
   doesn't bear on any of them).
5. **confidence_overall: anecdotal.** Every claim in this source rests on
   one or two practitioners' first-person, unreplicated experience — there
   is no benchmark, reader study, or controlled comparison anywhere in the
   source. The corroboration from Willison (Claim 10) and from Anthropic's
   sycophancy research (Cross-References/Corroborates) strengthens
   individual claims but does not change the source's own evidentiary
   status from personal-practice anecdote to measured result.
