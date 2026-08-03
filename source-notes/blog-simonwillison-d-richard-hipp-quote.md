---
source_url: https://simonwillison.net/2026/Jul/29/d-richard-hipp/
source_type: blog-post
title: "A quote from D. Richard Hipp"
author: Simon Willison (quoting D. Richard Hipp)
date_published: 2026-07-29
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: anecdotal
issue: "#2443"
---

# A quote from D. Richard Hipp

> A single primary-source quotation — D. Richard Hipp, speaking in a YouTube
> appearance, uses the historical arrival of SQL (which displaced the need to
> pay "COBOL programmers" to hand-write data-query code) as a precedent for
> arguing that a new abstraction layer changes what a programmer's job
> involves rather than eliminating the job itself.

## Source Context

- **Type**: blog-post (Simon Willison's "quotation" post type — a single
  blockquote plus a one-line citation, no surrounding editorial commentary
  from Willison; ~110 words total including the quote). Auto-discovered via
  the `simon-willison` trusted feed. Filed under the tags `sql`, `careers`,
  `d-richard-hipp` on the source page itself.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo, but in this post he is purely a curator — he adds no
  original framing or analysis beyond the blockquote and its citation. The
  underlying speaker, D. Richard Hipp, is not identified or biographically
  framed anywhere in this post (no bio, no credential line, only the name and
  a citation link to the YouTube source video). Hipp is widely known outside
  this source as the creator of SQLite, Fossil, and TH3 — a veteran database
  and systems engineer with direct, decades-long personal experience of the
  COBOL-to-SQL transition he describes — but that identification is this
  Miner's own general knowledge, not a claim made in the source text itself,
  and is flagged as such rather than attributed to Willison's post.
- **Scope**: Covers exactly one thing — a three-paragraph spoken quotation
  from a YouTube video (cited as `https://www.youtube.com/watch?v=R57nUGzo7CA&t=848s`,
  i.e. timestamped to 14:08 into the video), reproduced by Willison as a
  blockquote with no additional commentary. Does not cover: the identity,
  title, channel, or broader topic of the source video (this Miner attempted
  to identify these via WebFetch against the YouTube URL and via `curl`, and
  neither returned usable video title/description/channel metadata — see
  Extraction Notes); any biographical detail about Hipp; or any argument
  beyond the single SQL/COBOL analogy quoted.

## Extracted Claims

### Claim 1: Before SQL existed, querying large data sets required custom-written software, and the job title for the specialists who wrote that software was "COBOL programmer"
- **Evidence**: Direct quote, first paragraph of the blockquote.
- **Confidence**: anecdotal (a single practitioner's spoken historical
  recollection/generalization, not a cited data source or study)
- **Quote**: "Years ago, we didn’t have SQL. There were people whose job was to generate software that would query large data sets. Their job title was COBOL programmer."
- **Our assessment**: This is scene-setting for the analogy rather than a
  claim requiring independent verification — it is an accurate, unremarkable
  characterization of pre-SQL data querying practice (COBOL was the dominant
  business-data-processing language before SQL's standardization), stated
  as a shared premise Hipp expects the audience to recognize rather than a
  contested assertion.

### Claim 2: SQL replaced the need to pay for custom COBOL query code by letting people accomplish the same outcome through a simple declarative specification
- **Evidence**: Direct quote, second paragraph of the blockquote, describing
  the mechanism of the SQL transition.
- **Confidence**: anecdotal (Hipp's own simplified characterization of the
  transition — he explicitly flags it as a simplification)
- **Quote**: "Then SQL comes along—I’m simplifying this only a little bit—and it gives you this convenient way so people could just specify. With a very simple specification, you can generate all of that code that you had to pay the expensive COBOL programmer to do before."
- **Our assessment**: The self-flagged "I'm simplifying this only a little
  bit" hedge is notable — Hipp is presenting this as a considered, not
  glib, historical account, which is relevant to how much interpretive
  weight the guide should put on the analogy. The specific mechanism named
  (declarative specification replacing hand-written procedural code to
  produce the same output) is structurally identical to how the guide
  already frames AI agents as a specification-driven abstraction layer over
  hand-written code (see Cross-References).

### Claim 3: The arrival of SQL did not eliminate programmers — it changed what their job involved
- **Evidence**: Direct quote, third and final paragraph of the blockquote,
  presented as the conclusion Hipp draws from the SQL/COBOL analogy.
- **Confidence**: anecdotal (a single practitioner's interpretive conclusion
  drawn from his own historical account, not a measured or externally
  verified claim)
- **Quote**: "That didn’t mean programmers went away. It just meant the job changed a little bit."
- **Our assessment**: This is the load-bearing sentence of the source and
  the reason the Prospector flagged it — it is a historical precedent (not
  an AI-era prediction) for the "abstraction compresses part of the job
  without eliminating the role" pattern the guide's other sources argue is
  happening again with AI agents (see Cross-References — Corroborates). Its
  value is precedent, not new evidence: it offers a concrete, named prior
  instance of the same structural pattern, from a speaker with direct
  personal experience of that earlier transition, rather than additional
  data about the current AI transition itself.

## Concrete Artifacts

```
Full text of the quoted blockquote, D. Richard Hipp, as reproduced verbatim
in the page HTML at simonwillison.net/2026/Jul/29/d-richard-hipp/:

"Years ago, we didn't have SQL. There were people whose job was to generate
software that would query large data sets. Their job title was COBOL
programmer.

Then SQL comes along—I'm simplifying this only a little bit—and it gives
you this convenient way so people could just specify. With a very simple
specification, you can generate all of that code that you had to pay the
expensive COBOL programmer to do before.

That didn't mean programmers went away. It just meant the job changed a
little bit."

Citation line: "— D. Richard Hipp"
Blockquote cite attribute (video source, not independently explored beyond
the timestamp): https://www.youtube.com/watch?v=R57nUGzo7CA&t=848s (14:08)

Post metadata: tags "sql", "careers", "d-richard-hipp"; posted 29th July
2026 at 9:15 pm; page type "quotation collected by Simon Willison".
```

## Cross-References

- **Corroborates**: `blog-kentbeck-jessicakerr-learning-system.md` Claim 1
  ("AI didn't eliminate the programmer's job, it split it in two —
  hand-crafted code-writing is commoditized 'IKEA furniture,' while
  understanding what to build, proving it works, and stewarding the
  human/code/agent system is the harder, more human remainder"). Hipp's
  Claim 3 here ("that didn't mean programmers went away... the job changed")
  is the same structural pattern — job-splits/changes rather than
  disappears — stated about a prior, non-AI abstraction transition (SQL
  over hand-written COBOL query code) rather than the current AI transition.
  This source adds historical precedent to a claim the corpus otherwise
  only documents for the present AI moment.
- **Corroborates**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`
  Claim 8 ("even making the execution layer instant and perfect will only
  be a small change from the status quo" — AI has already largely
  compressed the execution/coding layer without eliminating the role) and
  Claim 4 (the "decide-execute-deliver sandwich" — AI compresses the
  execution middle, leaving the outer layers unchanged). Hipp's Claim 2
  (SQL as a "convenient way so people could just specify," replacing
  hand-written procedural code for the same output) describes the same
  compression-of-execution mechanism Narayanan and Kapoor formalize for the
  AI case; Hipp's Claim 3 draws the same "role persists, job changes"
  conclusion Narayanan and Kapoor argue from WARN Act and task-survey data.
  The value of pairing them: Narayanan/Kapoor supply present-day empirical
  grounding for the pattern, Hipp supplies an independent, non-AI historical
  instance of the identical structural pattern recurring.
- **Corroborates**: `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 1
  (Kent Beck "rebuts the claim that coding – and eventually the whole
  software engineering craft – will vanish... coding is only part of what
  we do, and a small part of it, too"). Both sources converge on programming
  roles surviving abstraction/automation of the coding layer specifically,
  though Beck's claim addresses the present AI moment directly while Hipp's
  is a historical analogy offered as precedent for the same conclusion.
- **Extends**: The corpus's existing "abstraction doesn't eliminate the job"
  evidence (`blog-simonwillison-why-ai-hasnt-replaced-engineers.md`,
  `blog-kentbeck-jessicakerr-learning-system.md`,
  `blog-pragmaticengineer-orosz-kentbeck-career.md`) is drawn entirely from
  the current AI transition (WARN Act filings, task-time surveys,
  practitioner interviews about present-day agentic coding). This source
  extends that body of evidence with a named, dated, pre-AI historical
  instance (SQL displacing hand-written COBOL query code) of the same
  pattern, offered by a speaker with firsthand experience of that earlier
  transition.
- **Novel**: A historical (pre-AI, SQL-vs-COBOL) precedent for the
  "abstraction compresses execution without eliminating the role" pattern is
  new to this corpus. Every other corpus source making this argument reasons
  from AI-era evidence or AI-era practitioner testimony; this is the first
  source to ground the same structural claim in an earlier, already-settled
  technology transition, which gives the guide a rhetorical option (citing
  precedent rather than only current-moment data) when addressing
  career-anxiety framing.

## Guide Impact

- **Chapter 00 (Principles) or Chapter 05 (Team Adoption)**, wherever the
  guide addresses "will AI eliminate programming jobs?" career anxiety:
  recommend citing Claim 3 as a short, quotable historical precedent
  alongside the AI-era evidence already cited from
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` and
  `blog-kentbeck-jessicakerr-learning-system.md`. Concretely: the guide can
  now say "this isn't the first time an abstraction layer absorbed a
  category of hand-written code — SQL did the same to COBOL query
  programming, and the job didn't vanish, it changed," citing Hipp by name,
  before presenting the current AI-era data. This gives the anxiety-framing
  section a specific historical anchor rather than relying solely on
  present-tense arguments about a still-unfolding transition.
- **No other chapter should cite this source for anything beyond the single
  precedent claim** — the source contains no data, no methodology, and no
  discussion of AI, agentic coding, or any contemporary tooling; its entire
  guide value is the historical-analogy framing in Claim 3, supported by
  the mechanism described in Claims 1–2.

## Extraction Notes

1. **Source is unusually thin, deliberately**: this is Simon Willison's
   "quotation" post type — a single three-paragraph blockquote and a
   one-line citation, with zero surrounding editorial commentary, matching
   the format of `blog-simonwillison-sam-altman-quote.md` (also a bare
   quotation post). Per MINER.md's "aim for 5-15 claims... if you only
   found 1-2, you probably didn't read deeply enough" guidance: this note
   extracts 3 claims, one per paragraph of the quote, which is the full
   substantive content of the source. Padding further would require
   splitting single sentences into artificially finer sub-claims or
   inventing biographical/contextual claims not present in the source text;
   neither was done.
2. **Verbatim text obtained via direct `curl`, not the WebFetch tool**: a
   first WebFetch pass against the source URL returned only a 125-character
   truncated paraphrase citing "guidelines limiting quotes to 125
   characters"; a second WebFetch pass requesting the full verbatim text was
   refused outright by the fetch tool's underlying model on copyright
   grounds (consistent with the same behavior documented in
   `blog-simonwillison-sam-altman-quote.md`'s and
   `blog-pragmaticengineer-orosz-kentbeck-career.md`'s extraction notes for
   this same publisher/tooling combination). Per MINER.md §2a, the raw HTML
   was instead fetched directly with `curl` (browser user-agent) against
   `simonwillison.net`, and every quote in this note was copied
   character-for-character from the `<blockquote>` element in that HTML —
   none were constructed from the earlier summarized/truncated WebFetch
   passes.
3. **Video source not independently explored**: the blockquote's `cite`
   attribute points to a YouTube video
   (`https://www.youtube.com/watch?v=R57nUGzo7CA&t=848s`). Both a WebFetch
   attempt and a direct `curl` fetch against the YouTube watch page failed to
   return usable title, description, or channel metadata (YouTube's watch
   page requires JavaScript execution to render this information; the raw
   HTML/JSON returned only UI chrome strings). This Miner did not have a
   method to reliably extract the video's title, channel, or broader
   conversational context beyond what Willison's citation already states
   (speaker name and timestamp). The claims extracted above are therefore
   based solely on the blockquote text as reproduced by Willison, not on
   independently verified video context.
4. **No sub-pages followed**: beyond the one attempted (and unsuccessful)
   fetch of the cited YouTube video, the source page contains no other
   substantive inline links — only standard site navigation, tag links, and
   a "Recent articles" list of unrelated posts (a stateless-MCP post, an
   OpenAI/Hugging Face incident post, and a Claude Code team fireside-chat
   post), none of which relate to this quote's topic. Per MINER.md §1, none
   were followed.
5. **Cross-reference verification**: before writing citations above, this
   Miner re-read `blog-kentbeck-jessicakerr-learning-system.md` (Claim 1,
   confirmed at that note's `### Claim 1:` heading),
   `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` (Claim 4 and
   Claim 8, both confirmed at their respective headings), and
   `blog-pragmaticengineer-orosz-kentbeck-career.md` (Claim 1, confirmed at
   that note's heading) directly, and confirmed each cited claim's number and
   content matches what is cited above.
6. **No contradiction identified**: this source's sole substantive claim
   (abstraction compresses the job without eliminating the role) corroborates
   rather than opposes every existing corpus note found on this topic; no
   contradiction issue was filed per MINER.md §4a.
7. **Confidence rated `anecdotal` overall**: all three claims rest on a
   single practitioner's self-described simplified, spoken historical
   recollection and interpretive conclusion, delivered in a video appearance
   with no data, citation, or study behind it. This is weaker than the
   `emerging` rating given to `blog-simonwillison-sam-altman-quote.md` (which
   quotes a specific, dated primary document — an email — with checkable
   text) because Hipp's quote is a generalized recollection and analogy
   rather than a specific, checkable factual record; it is stronger than
   nothing because Hipp is a first-party account from someone with (per
   external, non-source-text knowledge) direct professional experience of
   the transition he describes.
