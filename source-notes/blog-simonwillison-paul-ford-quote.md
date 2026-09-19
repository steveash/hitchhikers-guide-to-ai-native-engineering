---
source_url: https://simonwillison.net/2026/Sep/12/paul-ford/
source_type: blog-post
title: "A quote from Paul Ford"
author: Simon Willison (quoting Paul Ford, New York Times opinion piece)
date_published: 2026-09-12
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: anecdotal
issue: "#3557"
---

# A quote from Paul Ford

> A single-paragraph quotation post — Simon Willison reproducing four sentences
> from Paul Ford's *New York Times* opinion piece "A.I. Was Supposed to Give Us
> New Killer Apps. What Happened?" — arguing that the software industry is
> discovering cutting-edge work still requires humans thinking and working
> together, that AI's ease of "doing someone else's job badly" is part of why
> AI-driven software projects fail, and closing with the aphorism "now that
> everyone can code, it's become clearer why many shouldn't."

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus a one-line citation, ~90 words total including the quote).
  Auto-discovered via the `simon-willison` trusted feed. The blockquote's
  `cite` attribute points directly to the original NYT opinion piece
  (`https://www.nytimes.com/2026/09/12/opinion/ai-software-coding-apps.html`).
  Willison adds no original commentary of his own — the entire page is the
  quote, its citation line, and standard site chrome (tags, date, "Recent
  articles").
- **Author credibility**: Paul Ford is a technology writer and programmer,
  co-founder of the product studio Postlight and best known for the widely
  read 2015 Bloomberg Businessweek cover story "What Is Code?" — an
  established, credentialed voice writing a paid opinion piece for a major
  outlet (the *New York Times*), not an anonymous or unknown commentator.
  This piece is explicitly first-person testimony about his own trade
  ("software developer roles like mine") rather than outside punditry.
  Willison is a `trusted-feed` curator here, not an independent verifier of
  Ford's underlying claims — this note's confidence reflects that Ford's
  statements are stated as personal, experience-grounded opinion in an
  opinion-section essay, not as measured or sourced findings within the
  quoted text itself.
- **Scope**: The quoted excerpt states a personal before/after arc (developer
  roles seemed threatened, then the industry realized something durable about
  human craft), one causal claim about why "projects fail," and a closing
  aphorism about coding capability vs. coding judgment. It does NOT include
  any data, named incident, specific failed project, or methodology — the
  quote is argumentative aphorism, not evidence. This Miner could not access
  the full NYT article (paywalled/bot-blocked; see Extraction Notes), so this
  note is scoped strictly to the four sentences Willison reproduced, not to
  whatever fuller argument or evidence the original 1,000+-word op-ed may
  contain.

## Extracted Claims

### Claim 1: Ford states it once looked like AI ("tireless robots") would end software developer roles like his own
- **Evidence**: Ford's own first-person framing, opening sentence of the quote.
- **Confidence**: anecdotal (a single practitioner's stated personal fear, not a measured claim)
- **Quote**: "For a while, I must admit, it looked as if software developer roles like mine were done for. How could we fight against tireless robots?"
- **Our assessment**: This is scene-setting for the claims that follow, not itself a substantive claim about AI-native engineering — but it establishes Ford writes as a practitioner reflecting on his own trade's trajectory, not as an outside observer, which matters for weighing the credibility of Claims 2–5.

### Claim 2: Ford argues the software industry is "slowly realizing" that making cutting-edge software still requires humans to think and work together, maximizing their skill sets and practicing their respective crafts
- **Evidence**: Ford's own stated observation, directly following the "done for" framing in Claim 1.
- **Confidence**: anecdotal (a stated industry-level observation from an experienced practitioner, with no data or named example attached in the quoted text)
- **Quote**: "But our industry is slowly realizing that making truly cutting-edge software still requires humans to think and work together, to maximize their skill sets and to practice their respective crafts."
- **Our assessment**: This directly corroborates the corpus's existing "developer roles persist, judgment relocates rather than disappears" thesis (see Cross-References), but adds no new mechanism beyond what those more detailed sources already establish — its value is as a concise, quotable restatement from a credentialed outside voice (NYT opinion, not an AI-industry blog), not as new evidence.

### Claim 3: AI can write very good software, but it also makes it easy to do someone else's job badly
- **Evidence**: Ford's own stated claim, third sentence of the quote.
- **Confidence**: anecdotal (an assertion with no supporting example, metric, or named incident in the quoted text)
- **Quote**: "A.I. can write very good software, but it also makes it easy to do someone else's job badly,"
- **Our assessment**: This is the quote's sharpest, most specific claim — it distinguishes AI's raw code-generation capability from the separate question of whether the person directing it is qualified to do the job the code is standing in for. This is conceptually adjacent to the corpus's existing "vibe coding is not agentic engineering" definition (Narayanan & Kapoor, via `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 9), which similarly separates capability-to-generate from capability-to-evaluate — but Ford's framing is about displacing *someone else's job*, not about an individual's own supervision practice.

### Claim 4: Ford attributes the failure of "all those projects" partly to AI making it easy to do someone else's job badly
- **Evidence**: Ford's own stated causal claim, continuing directly from Claim 3 in the same sentence.
- **Confidence**: anecdotal (a bare causal assertion — "all those projects fail" — with no named project, count, timeframe, or failure-mode detail given in the quoted excerpt)
- **Quote**: "which is part of why all those projects fail."
- **Our assessment**: "All those projects" implies a referent (presumably discussed earlier in Ford's full NYT piece, which this Miner could not access — see Extraction Notes) that is not recoverable from the quoted excerpt alone. As extracted, this is an unsupported causal claim: it names a plausible failure mechanism (unqualified people producing plausible-looking but unsound work) without any case detail. The guide should not cite this as evidence of a specific failure pattern — only as a named hypothesis from a credible outside voice, pending the fuller argument in Ford's original piece.

### Claim 5: "Now that everyone can code, it's become clearer why many shouldn't" — Ford frames AI's democratization of coding ability as having revealed, rather than resolved, a judgment gap
- **Evidence**: Ford's own closing aphorism, the quote's final sentence.
- **Confidence**: anecdotal (an aphoristic closing line, not a measured or evidenced claim)
- **Quote**: "Now that everyone can code, it's become clearer why many shouldn't."
- **Our assessment**: This is the quote's most citable line and the reason the Prospector flagged it as high-novelty phrasing — it names the "capability ≠ judgment" tension as a *revelation* caused specifically by removing the coding-skill barrier, rather than as a pre-existing concern AI happens to intersect with. This is the same underlying tension the corpus already documents in more operational detail (e.g., `blog-addyosmani-earning-taste-judgment.md`'s thesis that taste/judgment no longer accrue automatically from reps once agents absorb the reps), but Ford's framing is about *access* to coding (who can now produce code at all) rather than about *skill development* (how existing developers build judgment) — a distinct angle: this is about gatekeeping removed, not about a training pipeline disrupted.

## Concrete Artifacts

```
Source: simonwillison.net/2026/Sep/12/paul-ford/, quoting Paul Ford,
"A.I. Was Supposed to Give Us New Killer Apps. What Happened?",
New York Times, September 12, 2026
(cite attribute: https://www.nytimes.com/2026/09/12/opinion/ai-software-coding-apps.html)

Full quoted text (verified character-for-character against the raw HTML
<blockquote> element via direct curl fetch of the Willison page):

"For a while, I must admit, it looked as if software developer roles like
mine were done for. How could we fight against tireless robots? But our
industry is slowly realizing that making truly cutting-edge software still
requires humans to think and work together, to maximize their skill sets
and to practice their respective crafts. A.I. can write very good software,
but it also makes it easy to do someone else's job badly, which is part of
why all those projects fail. Now that everyone can code, it's become
clearer why many shouldn't."

Citation line: "— Paul Ford, A.I. Was Supposed to Give Us New Killer Apps.
What Happened?"
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-human-judgment-relocates.md` Claim 15 ("human ownership
    does not need to shrink even as the percentage of code physically typed
    by humans falls... the future of software engineering is better described
    as human judgment being relocated than as humans leaving the loop") and
    `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 5 (the
    "decide-execute-deliver" outer layers resist AI automation for structural,
    not capability, reasons): this source's Claim 2 (cutting-edge software
    still requires humans thinking and working together) restates the same
    "roles persist, work relocates" thesis in a single credentialed-outsider
    aphorism, with no independent evidence of its own.
  - `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 9
    (Narayanan & Kapoor's definition: "in true vibe coding the user simply
    tells the agent what to do, doesn't supervise it... might not even have
    the skills to do so"): this source's Claim 3 (AI "makes it easy to do
    someone else's job badly") names the same underlying capability/judgment
    gap from a different angle — Narayanan and Kapoor define the *behavior*
    that constitutes the gap (no supervision, no review, no skill to review);
    Ford's line names the *consequence* (displacing someone qualified with
    someone merely AI-enabled).
  - `blog-addyosmani-earning-taste-judgment.md` Claim 1 ("taste used to be a
    byproduct of the reps. Agents took the reps. So if you're junior you now
    have to go get the taste... on purpose") and its closing thesis ("the
    world isn't short on opportunity; it's short on people who can find the
    right problem, tell whether the machine solved it, and finish past where
    the machine stopped"): this source's Claim 5 ("everyone can code... many
    shouldn't") is a shorter, more aphoristic restatement of the same
    capability-vs-judgment gap, from a non-technologist outlet (NYT opinion
    page) rather than a practitioner blog — useful as evidence the concern
    has reached general-audience discourse, not as new mechanism detail.

- **Contradicts**: None found requiring a filed contradiction issue per
  MINER.md §4a. No existing corpus source note asserts the inverse of any of
  Claims 1–5 (e.g., no source claims coding-skill democratization has *not*
  revealed a judgment gap, or that "all those projects" succeeded).

- **Extends**: No existing corpus note is extended with new mechanism detail
  by this source — see Guide Impact and Extraction Notes for why: the quote
  is aphoristic assertion, not case detail, so it restates rather than
  deepens the corpus's existing, more evidenced treatments of the same
  capability-vs-judgment theme.

- **Novel**: The specific phrasing "now that everyone can code, it's become
  clearer why many shouldn't" is new to the corpus as a compact, quotable
  aphorism for the capability-vs-judgment gap, and its source — a *New York
  Times* opinion page, rather than an AI-industry or engineering-practitioner
  blog — is itself a novel signal that this framing has reached
  general-audience discourse. No other data point, mechanism, or named
  incident in this excerpt is new; Claim 4's "why all those projects fail"
  claim gestures at unnamed evidence this Miner could not access (see
  Extraction Notes).

## Guide Impact

- **No chapter should cite Claim 4 ("part of why all those projects fail")
  as evidence of a specific or quantified failure pattern** — as extracted,
  it is a bare, unsupported causal assertion referring to an unrecoverable
  antecedent ("all those projects") from a piece this Miner could not read
  in full. If a future Miner obtains full access to the NYT piece and finds
  the referenced projects/evidence, that should supersede this note's Claim 4
  treatment.
- **Chapter 00/01 (Principles / framing), if the guide wants a short,
  general-audience-credible pull-quote for the capability-vs-judgment
  theme**: Claim 5 ("now that everyone can code, it's become clearer why many
  shouldn't") is a strong candidate epigraph or section-opener — it is more
  citable as rhetoric than as evidence, and should be paired with, not
  substituted for, the corpus's more detailed treatments of the same theme
  (`blog-addyosmani-earning-taste-judgment.md`,
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 9) for any
  section making an actual argument rather than setting a tone.

## Extraction Notes

1. **Source is a single ~90-word quotation post with no companion links to
   follow**: per MINER.md §1, this Miner attempted to follow the blockquote's
   `cite` link to the underlying NYT article
   (`https://www.nytimes.com/2026/09/12/opinion/ai-software-coding-apps.html`)
   to read Ford's full argument and locate the antecedent for "all those
   projects" in Claim 4. The NYT URL returned a bot-detection/CAPTCHA
   challenge page (DataDome) to an unauthenticated `curl` fetch, not article
   content, and the NYT is a subscription-paywalled outlet this Miner has no
   authenticated access to. This note is therefore scoped strictly to the
   four sentences Willison reproduced, not to the fuller op-ed; this is
   flagged explicitly in Claim 4's assessment and in Guide Impact.
2. **Verbatim text obtained via direct `curl`, not an AI-summarizing fetch
   tool**: a first WebFetch pass against the Willison page returned close but
   not confirmed-verbatim text; per MINER.md §2a, the quote in this note was
   independently verified character-for-character against the raw HTML
   `<blockquote>` element via a direct `curl` fetch (browser user-agent) of
   `simonwillison.net`, including exact curly-quote punctuation.
3. **Three redundant Prospector triage comments on the source issue**: the
   issue carries three separate triage comments from the same author, with
   differing (high/medium/low) novelty assessments and differing chapter/
   overlap lists, rather than one settled assessment. These are redundant
   triage passes on the same source, not conflicting claims within the
   source itself, so this was not treated as a MINER.md §4a contradiction.
   This note's extraction and Cross-References draw on and reconcile the
   union of chapters and overlaps flagged across all three comments,
   including the third (lowest-novelty) comment's assessment that the
   source's "substance" is "thin" — an assessment this note's extraction
   confirms: the source is genuinely a single four-sentence aphoristic
   quotation with no supporting data, case detail, or extended argument
   accessible to this Miner.
4. **Claim count below MINER.md's "5-15" guideline, deliberately**: this note
   extracts 5 claims from a 4-sentence, ~90-word quotation, matching the
   precedent set by `blog-simonwillison-sam-altman-quote.md` (4 claims from a
   comparably short quotation) and `blog-simonwillison-boris-cherny-quote.md`
   (7 claims from a longer single-paragraph quotation). Further subdivision
   would not add information; the quote's scene-setting and causal-claim
   sentences (Claims 1 and 4) are already close to the floor of what
   constitutes a distinct, citable statement.
5. **Cross-reference verification**: before writing citations above,
   `blog-addyosmani-human-judgment-relocates.md`,
   `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`, and
   `blog-addyosmani-earning-taste-judgment.md` were each re-read directly
   (MINER.md §4b) and all claim numbers above were confirmed against those
   notes' numbered `### Claim N:` headings in document order.
6. **`confidence_overall` set to `anecdotal`**: every claim in this note
   rests on a single unelaborated opinion-piece excerpt with no data,
   methodology, or named incident in the accessible text — this is weaker
   evidentially than the `emerging` rating given to the Boris Cherny and
   Sam Altman quotation notes, both of which involve first-party
   organizational/primary-document testimony about verifiable practices or
   events. Ford's quote is credentialed personal opinion and aphorism, which
   this note grades `anecdotal` throughout.
