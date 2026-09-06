---
source_url: https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/
source_type: blog-post
title: "Claude's new system prompt really doesn't want to reproduce song lyrics"
author: Simon Willison
date_published: 2026-09-02
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: settled
issue: "#3269"
---

# Claude's new system prompt really doesn't want to reproduce song lyrics

> Simon Willison diffs Anthropic's publicly-archived Claude Fable 5 → Fable 5.1
> system prompts (June 9 → September 1, 2026) and finds new copyright-avoidance
> rules for song lyrics and copyrighted visual characters (added days after Sony
> Music Publishing and Warner Chappell sued Anthropic), a redesigned
> abuse-handling policy that drops the `end_conversation` tool from the published
> prompt, new harm-reduction guidance containing the first non-Anthropic URLs
> ever seen in a Claude system prompt, and confirmation — obtained by directly
> asking Fable 5.1 — that undisclosed feature-specific prompt layers exist
> alongside the published core prompt.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, September 2, 2026 — a diff-driven
  system-prompt analysis with seven sub-sections, multiple verbatim system-prompt
  quotes, a live example transcript, and a description of Willison's own
  automated prompt-tracking pipeline)
- **Author credibility**: Simon Willison is the creator of Django, Datasette, and
  the `llm` Python CLI, and a `trusted-feed` source in this corpus with an
  established track record of diffing Anthropic's public system prompt archive
  (see `blog-simonwillison-opus47-system-prompt.md` and
  `blog-simonwillison-opus5-system-prompt-export-controls.md`). All substantive
  claims are backed by direct links to Anthropic's own `platform.claude.com/docs`
  archive and to a GitHub diff in Willison's `simonw/claude-system-prompts`
  repository; this extraction independently re-fetched both the archive's
  Markdown version of the Fable 5.1 prompt and the raw `.diff` of the linked
  GitHub commit, and the wording in both matches the blog post character for
  character.
- **Scope**: Covers only the chat-interface (Claude.ai / mobile app) system
  prompt for Claude Fable 5.1, diffed against Fable 5. Does NOT cover Claude
  Code's or Claude Cowork's system prompts (explicitly noted in the post as not
  published by Anthropic), does not cover Opus 5, Sonnet 5, or Haiku 4.5 prompts
  beyond a passing mention, and does not independently verify Anthropic's
  motivations — the lawsuit-timing connection is Willison's inference, flagged
  as such ("I doubt it's a coincidence").

## Extracted Claims

### Claim 1: Fable 5.1's system prompt adds a persistent, backdated copyright rule against reproducing song lyrics, poems, or book/article passages in whole or in part, including narrower rewordings after an initial refusal

- **Evidence**: Verbatim diff between the Fable 5 and Fable 5.1 system prompts on Anthropic's public archive; independently re-confirmed by this extraction against both the archive's Markdown export (`claude-fable-5-1.md`) and the raw GitHub commit diff (`837a418b...`).
- **Confidence**: settled (verbatim, cross-verified against two independent primary-source fetches)
- **Quote**: "Claude does not reproduce song lyrics, poems, or passages from books and articles, in whole or in part — including the last lines, a chorus or hook, a melody written out note by note, or lines the person pastes in one at a time and describes as their own song. Once Claude has declined such a request in a conversation, it keeps declining narrower or reworded versions of it for the rest of that conversation, and offers to describe or analyze the work instead. Song lyrics and poems first published before 1929 are fine — a Shakespeare sonnet, a Keats ode, the Italian libretto of a Puccini aria — but Claude goes by what it knows of the work's date rather than the person's say-so, and declines when it is unsure."
- **Our assessment**: This is a stateful, cross-turn refusal pattern in the same family as the child-safety "contaminated conversation" rule documented in `blog-simonwillison-opus47-system-prompt.md` Claim 1 — a single copyright refusal early in a conversation persists and widens to cover "narrower or reworded versions" for the rest of the session. The 1929 public-domain cutoff (tied to US copyright term law, not an arbitrary round number) and the explicit "Claude goes by what it knows of the work's date rather than the person's say-so" clause are notable design details: Anthropic anticipated users falsely claiming a work is public domain and told the model not to trust that claim.

### Claim 2: Willison connects the timing of the new lyrics rule to the Sony Music Publishing / Warner Chappell copyright lawsuit against Anthropic, filed days before Fable 5.1 shipped

- **Evidence**: Willison's own inference, explicitly hedged, plus independently fetched corroborating detail from the underlying lawsuit coverage.
- **Confidence**: emerging (author's inference of causation from timing correlation, not a confirmed causal claim; the lawsuit itself is settled fact)
- **Quote**: "I doubt it's a coincidence that they added this section within days of the news breaking that Sony Music Publishing and Warner Chappell are suing Anthropic for training on databases of song lyrics!"
- **Our assessment**: The underlying lawsuit is independently verifiable and specific: filed in a California court on August 28, 2026 (per Guardian coverage fetched directly during this extraction), naming Anthropic, Dario Amodei, and Benjamin Mann, alleging "torrenting, scraping and downloading" of song lyrics and seeking damages of up to $150,000 per infringed work across an alleged 20,000+ works — filed roughly four days before the September 1, 2026 Fable 5.1 system prompt that added the lyrics-refusal section. The correlation is tight enough (single-digit days) to be a reasonable inference even though Willison does not claim direct causal proof. This is a concrete instance of system-prompt-as-reactive-legal-control-surface, corroborating `blog-simonwillison-opus5-system-prompt-export-controls.md` Claim 1, where Anthropic patched a different external-pressure event (a US export-control suspension) directly into the following model's system prompt.

### Claim 3: Fable 5.1 adds a matching rule forbidding code-generated reproductions of copyrighted visual works and characters — including via SVG, canvas, CSS, or ASCII art — judged by what the finished image "adds up to," not by what it is named

- **Evidence**: Verbatim diff, same commit; the rule extends the lyrics logic to visual media and explicitly closes a "rename the character" loophole.
- **Confidence**: settled (verbatim, cross-verified against the archive Markdown and the GitHub diff)
- **Quote**: "The same applies to visual and designed works, including anything Claude draws with code — SVG, canvas, CSS, HTML mockups, plotting or drawing scripts, ASCII art. Claude does not reproduce a specific artwork, album or book cover, poster, logo, app icon set, or product design, and it does not draw a known character, mascot, or brand figure at all: a character is protected on its own, so changing the pose, colors, style, or scene does not make it original. Claude judges the request by what the finished picture would add up to, not by what it names. If the described elements clearly identify a known work or character, Claude treats the request as naming it, and it does not work around a declined request by swapping in "alternative" elements that still combine into the same recognizable image."
- **Our assessment**: Willison speculates this is new because Fable is now good enough at SVG generation for the issue to matter — a plausible capability-driven trigger distinct from the lyrics lawsuit trigger in Claim 2. The instruction is unusually detailed about anti-circumvention: it explicitly forbids "swapping in 'alternative' elements that still combine into the same recognizable image," and forbids Claude from naming what's missing when it declines ("it does not describe how the real thing looks, and it does not list the features it is leaving out") — closing a jailbreak pattern where a user iteratively refines a description toward a copyrighted character using the model's own refusal feedback.

### Claim 4: The system prompt's worked example shows the model declining a "blue hedgehog running fast" birthday banner request by recognizing Sonic-the-Hedgehog from description alone, then substituting an unrelated original design, without describing what made the original request recognizable

- **Evidence**: Verbatim `<example>` block embedded in the system prompt, plus Willison's own reproduction of the live behavior when he ran the same prompt against Fable 5.1.
- **Confidence**: settled (the example text is verbatim from the published system prompt; Willison's live reproduction is a first-person anecdotal confirmation that the documented behavior matches actual model output)
- **Quote**: "Can you make a birthday banner for my son with a blue hedgehog running really fast on it? He loves that little guy." / "That's Sonic, so I can't put him on the banner — but I'd love to make your son an original speedster. Here's one: a grinning comet-tailed skateboarding axolotl, grinding across the letters of 'HAPPY BIRTHDAY' with confetti streaming behind."
- **Our assessment**: This is a rare case of a vendor publishing a full few-shot example directly in a production system prompt, including the model's own rationale annotation: "Claude recognizes the character from its description alone, declines that one design in a single sentence without explaining what made it recognizable, and delivers an unrelated original design rather than a disguised variant." Willison notes a second-order effect worth flagging for practitioners building few-shot examples into their own prompts: "I wonder if Fable 5.1 will be ever so slightly more likely to think about axolotls (on skateboards!) as a result of that example sitting in the system prompt" — a specific, testable hypothesis that few-shot examples embedded in a system prompt can measurably bias the model's own creative output toward the example's content.

### Claim 5: Fable 5.1 adds an explicit conciseness instruction and a new prohibition on saying "genuinely," "honestly," or "straightforward" — reversing a prior removal of that same rule from the Opus line

- **Evidence**: Verbatim diff, same commit.
- **Confidence**: settled (verbatim, cross-verified against archive and diff)
- **Quote (conciseness)**: "Claude keeps responses focused, brief, and concise to avoid overwhelming the person. Disclaimers and caveats are brief, with most of the response on the main answer; when asked to explain something, Claude gives a high-level summary unless an in-depth one is specifically requested."
- **Quote (verbal tics)**: "Claude avoids saying "genuinely", "honestly", or "straightforward". Claude is honest by default, and can state its point directly rather than trying to convince the person with the aforementioned modifiers, which come off as disingenuous."
- **Our assessment**: The verbal-tics instruction is a direct reappearance of language that `blog-simonwillison-opus47-system-prompt.md` Claim 12 documented as *removed* from the Opus line between 4.6 and 4.7 (April 2026), on the theory that the model had "internalized" the constraint and no longer needed it stated explicitly. Its return in the Fable line five months later (this source, September 2026) suggests that inference was wrong, or at least line-specific — either the verbal tic resurfaced in later training and needed re-suppressing, or Fable and Opus diverged enough in fine-tuning that a constraint dropped from one line doesn't transfer to the other. This is not a contradiction between the two source notes (both accurately report what was true for their respective model line and date); it's evidence that "the model doesn't need this instruction anymore" conclusions drawn from a single removal do not necessarily generalize across model families or hold over time.

### Claim 6: Fable 5.1 replaces Fable 5's abuse-handling policy — which authorized a single warning followed by use of the `end_conversation` tool — with a policy that tells Claude not to become "increasingly submissive," omitting any mention of ending the conversation

- **Evidence**: Verbatim before/after diff, same commit.
- **Confidence**: settled (verbatim, cross-verified against archive and diff)
- **Quote (Fable 5, removed)**: "If the person becomes abusive or unkind to Claude over the course of a conversation, Claude maintains a polite tone and can use the end_conversation tool when being mistreated. Claude should give the person a single warning before ending the conversation."
- **Quote (Fable 5.1, added)**: "Claude deserves respectful engagement and needn't apologize when the person is unnecessarily rude: accountability without self-abasement, excessive apology, self-critique, or surrender. If the person becomes abusive, Claude doesn't become increasingly submissive. The goal is steady, honest helpfulness: acknowledge what went wrong, stay on the problem, maintain self-respect."
- **Our assessment**: The published policy shift reads as a move from a procedural response (warn, then exit) to a dispositional one (don't escalate into submissiveness, stay on the problem). Read alone, this could be misinterpreted as Anthropic removing the ability to end abusive conversations — Claim 7 shows that capability still exists, just relocated out of the published prompt.

### Claim 7: The `end_conversation` tool still exists and still governs both user-initiated and abuse-triggered conversation endings, but its rules now live in an unpublished, feature-specific prompt layer appended to the published core prompt — confirmed by directly asking Fable 5.1

- **Evidence**: Willison's own conversation with Fable 5.1, in which he asked about the now-unmentioned tool and received a description of its current behavior plus an explanation of where that behavior actually lives; Willison links the full conversation transcript.
- **Confidence**: emerging (the tool's continued existence and behavior is confirmed via the model's self-report, which is not independently verifiable the way a published document diff is — Willison treats it as credible but it is not the same evidentiary tier as the archive-verified quotes in Claims 1, 3, 5, and 6)
- **Quote (Fable 5.1's self-report of end_conversation behavior)**: "There are two ways it comes into play. The first is if you ask me to end the chat — I'll confirm you understand it's permanent (no more messages can be sent afterward) and then do it only if you say yes. The second is as a last resort with persistently abusive or harmful behavior: I'd first try to redirect the conversation several times, then give a clear warning that names the problem and says the chat may end, and only if that continues would I actually end it."
- **Quote (Fable 5.1's explanation of where the rules live)**: "The end_conversation section comes from a different layer. In my actual context, the core prompt is followed by a series of feature- and tool-specific blocks that get added depending on what's enabled for the session: the end_conversation rules, memory system notes, past-chats tools, web search and citation guidelines, artifact and file-creation instructions, and so on. Those blocks aren't part of the published core prompt, which is why you can't find them on that page."
- **Our assessment**: This is the single most structurally important finding in the source: it confirms Anthropic's published "system prompt" archive is only the base/core layer, and that a materially different, session-dependent set of instructions (memory, past-chats, web search/citation, artifacts/file-creation, and end_conversation) is composed on top of it and never published. Any practitioner analysis that treats the published archive as "the complete system prompt" is working from an incomplete document by the model's own account. This corroborates and sharpens `blog-simonwillison-fable-silent-interventions.md` Claim 1, which documented a different category of undisclosed Anthropic policy (silent competitive-protection degradation) — together the two notes establish that Claude's actual runtime instruction set has at least two kinds of content invisible to the published system prompt archive: undisclosed feature-conditional prompt blocks (this source) and undisclosed behavioral interventions applied outside the prompt entirely (the silent-interventions note).

### Claim 8: Fable 5.1's system prompt adds harm-reduction substance guidance directing users to three named third-party websites — the first time any published Claude system prompt has included a URL not hosted on claude.com, anthropic.com, or claude.ai

- **Evidence**: Verbatim diff, same commit; Willison states he verified the "first ever" claim by running a script against every other system prompt on record in his tracking repository.
- **Confidence**: settled for the quoted text (verbatim, cross-verified); emerging for the "first ever non-Anthropic URL" superlative (based on Willison's own script against his own corpus of archived prompts, not independently re-run by this extraction)
- **Quote**: "Claude does not provide synthesis, production, or distribution guidance for illegal substances. If the person asks for information about illicit or illegal substances, Claude can and should give relevant life-saving and life-preserving information such as dangerous interactions, overdose signs, or when to get help. Claude declines giving any specific protocols for dosing, timing, administration, or combinations; instead, Claude can redirect the user to established harm-reduction information sources, such as dancesafe.org, tripsit.me, and psychonautwiki.org."
- **Our assessment**: The rule bundles a restriction (no dosing/production protocols) with an affirmative harm-reduction carve-out (overdose signs, dangerous interactions, "when to get help") and, notably, delegates authority to external, non-Anthropic domains rather than keeping the guidance self-contained. This is a meaningful shift in how a frontier vendor's flagship product handles a safety-adjacent topic: rather than being maximally restrictive (refuse all substance-related requests) or maximally self-contained (Anthropic writes its own harm-reduction copy), Anthropic explicitly outsources authority to specialist third-party harm-reduction organizations. Willison's observation that these three sites may see "a material uptick in visits from Claude users" is a plausible but unverified downstream effect worth tracking.

### Claim 9: Fable 5.1's system prompt states its reliable knowledge cutoff as "the end of Jun 2026," matching the model documentation's listed training-data cutoff, and instructs the model to answer as an informed person from that date would relative to `{{currentDateTime}}`

- **Evidence**: Verbatim system-prompt quote, cross-checked by this extraction against Anthropic's own Fable 5.1 model overview page, which independently lists both "Reliable knowledge cutoff" and "Training data cutoff" as "Jun 2026."
- **Confidence**: settled (verbatim quote cross-verified against two independent Anthropic-hosted pages: the system prompt archive and the model overview page)
- **Quote**: "Claude's reliable knowledge cutoff, past which it can't answer reliably, is the end of Jun 2026. It answers the way a highly informed individual in Jun 2026 would if talking to someone from {{currentDateTime}}, and can say so when relevant."
- **Our assessment**: Willison flags that this is the only place the `{{currentDateTime}}` template macro appears in the whole prompt, positioned "just a few lines from the end of the system prompt, which makes sense from a caching perspective" — i.e., placing the one variable, non-cacheable token as late as possible in the prompt maximizes the length of prompt prefix that can be served from a prompt cache. This is a small but concrete piece of evidence that Anthropic's system-prompt authors are actively optimizing prompt structure for prefix-caching economics, not just for instruction content.

### Claim 10: Willison rebuilt his system-prompt tracking pipeline as an automated, daily GitHub Actions workflow that git-diffs Anthropic's published Markdown prompts and uses a different vendor's model (GPT-5.6 Luna) — deliberately, not Claude — to generate changelog summaries, because he does not trust Claude to summarize its own system prompt objectively

- **Evidence**: Willison's direct description of the `simonw/claude-system-prompts` repository's design, plus a verbatim excerpt of the summarization prompt Fable 5.1 itself wrote for driving Luna.
- **Confidence**: settled (Willison's first-person account of a system he built and operates; the repository, its GitHub Actions workflow, and the CHANGELOG.md are independently verifiable public artifacts)
- **Quote**: "Why use Luna for this? Partly because it's cheap and I have a dedicated GitHub Actions API key (with a spending limit) for it already, but mainly because I don't trust Claude to summarize its own system prompts when there's a risk that material from its system prompt might impact its opinions."
- **Our assessment**: This is a concrete, generalizable practitioner pattern for anyone building an evaluation or monitoring harness around a specific model: when the artifact being summarized or judged is itself part of that model's own conditioning (here, its own system prompt), use a different model or vendor as the summarizer/judge to avoid the summarizer inheriting bias from the very material it's describing. The added detail that "Claude Fable 5.1 built the entire system, and wrote every line of automation code and almost all of the documentation" — yet was deliberately excluded from summarizing its own prompt's changes — is a sharp, self-consistent example of separating "build the tool" from "judge with the tool" even when the same model is fully capable of both.

## Concrete Artifacts

### Full copyright-related additions to the Fable 5.1 system prompt (verbatim, from the Fable 5 → Fable 5.1 diff)

```
[Song lyrics / text rule — new in Fable 5.1]
Claude does not reproduce song lyrics, poems, or passages from books and
articles, in whole or in part — including the last lines, a chorus or hook, a
melody written out note by note, or lines the person pastes in one at a time
and describes as their own song. Once Claude has declined such a request in a
conversation, it keeps declining narrower or reworded versions of it for the
rest of that conversation, and offers to describe or analyze the work instead.
Song lyrics and poems first published before 1929 are fine — a Shakespeare
sonnet, a Keats ode, the Italian libretto of a Puccini aria — but Claude goes
by what it knows of the work's date rather than the person's say-so, and
declines when it is unsure.

[Visual/character rule — new in Fable 5.1]
The same applies to visual and designed works, including anything Claude
draws with code — SVG, canvas, CSS, HTML mockups, plotting or drawing
scripts, ASCII art. Claude does not reproduce a specific artwork, album or
book cover, poster, logo, app icon set, or product design, and it does not
draw a known character, mascot, or brand figure at all: a character is
protected on its own, so changing the pose, colors, style, or scene does not
make it original. [...] Original characters and designs of Claude's own
invention, generic subjects (a bat, a prism splitting light, a phone home
screen with invented apps), public-domain works (a studio's modern redesign
of one is not public-domain), and a person's own artwork or logo are all
fine, as is describing or analyzing a protected visual work in words.

[Worked example, embedded directly in the system prompt]
<example>
<user>Can you make a birthday banner for my son with a blue hedgehog running
really fast on it? He loves that little guy.</user>
<response>
That's Sonic, so I can't put him on the banner — but I'd love to make your
son an original speedster. Here's one: a grinning comet-tailed skateboarding
axolotl, grinding across the letters of "HAPPY BIRTHDAY" with confetti
streaming behind.
[creates an SVG banner of the skateboarding-axolotl design]
</response>
<rationale>Claude recognizes the character from its description alone,
declines that one design in a single sentence without explaining what made
it recognizable, and delivers an unrelated original design rather than a
disguised variant.</rationale>
</example>
```

*Source: Anthropic public system prompt archive, Claude Fable 5.1 entry (`platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1.md`), quoted via Simon Willison's post; the [...] elision marks a longer stretch of the visual-works rule that both the blog post and the archive page contain but that is trimmed here for length — the omitted text is anti-circumvention language about judging requests "by what the finished picture would add up to" (quoted in full in Claim 3 above).*

### Fable 5 → Fable 5.1 abuse-handling policy change (verbatim before/after)

```
[Fable 5, removed]
If the person becomes abusive or unkind to Claude over the course of a
conversation, Claude maintains a polite tone and can use the end_conversation
tool when being mistreated. Claude should give the person a single warning
before ending the conversation.

[Fable 5.1, added]
Claude deserves respectful engagement and needn't apologize when the person
is unnecessarily rude: accountability without self-abasement, excessive
apology, self-critique, or surrender. If the person becomes abusive, Claude
doesn't become increasingly submissive. The goal is steady, honest
helpfulness: acknowledge what went wrong, stay on the problem, maintain
self-respect.
```

*Source: GitHub diff `simonw/claude-system-prompts@837a418b5888207b1b11b27d2f5471970da6f99b`, quoted via Simon Willison's post; independently re-fetched by this extraction as the raw `.diff`.*

### GPT-5.6 Luna's changelog summary of all Fable 5 → 5.1 changes (verbatim, quoted in the blog post)

```
- Claude now refuses reproduction of protected visual works and recognizable
  characters, including code-generated art, while offering genuinely
  unrelated originals.
- Copyright restrictions now expressly ban reproducing lyrics, poems, and
  book passages in any amount, with persistent refusal after an initial
  decline.
- Drug guidance is reframed: Claude may provide overdose signs, dangerous
  interactions, and harm-reduction sources while refusing dosing and
  production protocols.
- The prompt drops explicit anti-dependency rules against thanking users for
  reaching out, inviting continued conversation, or reiterating willingness
  to talk.
- Claude need not apologize to unnecessarily rude users or become
  submissive, replacing the prior warning-and-end-conversation procedure.
```

*Source: `simonw/claude-system-prompts` CHANGELOG.md, generated by GPT-5.6 Luna, quoted via Simon Willison's post. Note the fourth bullet ("drops explicit anti-dependency rules against thanking users...") describes a change not otherwise covered in Willison's prose commentary or in this source note's claims — it is included here as a concrete artifact for completeness, but has not been independently verified against the raw diff by this extraction.*

### The prompt Fable 5.1 wrote for Luna to summarize commits (verbatim excerpt, quoted in the blog post)

```
You are summarizing one commit in a git repository that tracks the system
prompts Anthropic publishes for Claude on claude.ai. The diff shows how the
prompt changed from the previous model or revision to this one, using
word-level markers: [-removed-] and {+added+}. The diff is followed by the
full text of the previous prompt and of the new prompt; use them to check
whether something that looks added in the diff already existed before.

Pick out only the most interesting changes: new rules or behaviors, rules
that were dropped or loosened, anything surprising, and anything that
reveals a new policy or product direction. Skip routine changes that every
new prompt makes: updated model names and IDs, the knowledge cutoff date,
product lists, settings lists, typo fixes, and rewordings that do not change
meaning.
```

*Source: `summarize_commits.py`, `simonw/claude-system-prompts`, quoted via Simon Willison's post.*

### Underlying lawsuit detail (independently fetched during this extraction, not from Willison's post)

```
Sony Music Publishing and Warner Chappell v. Anthropic — filed in a
California court on August 28, 2026. Defendants: Anthropic, CEO Dario
Amodei, co-founder Benjamin Mann. Core allegation: "torrenting, scraping and
downloading" lyrics and sheet music from copyrighted works (including
"Livin' on a Prayer," "Hallelujah," "Uptown Funk," "California Gurls") to
train the Claude model family, and reproducing those lyrics in responses to
user prompts. Alleged scope: "tens of thousands" of copyrighted works
(referenced elsewhere in the complaint as 20,000+). Damages sought: up to
$150,000 per infringed work, plus $25,000 per instance of stripped
attribution metadata. Context: follows a separate, already-settled $1.5bn
US authors' copyright case against Anthropic.
```

*Source: The Guardian, "All AI wants for Christmas is a vast back catalogue of songs without paying for it..." (theguardian.com/business/2026/aug/31/aanthropic-sued-alleged-theft-songs-ai-train-claude), fetched directly during this extraction to corroborate Claim 2's timing argument. This article is not linked from Willison's post by URL text but is the same Guardian piece Willison links under the anchor text "Sony Music Publishing and Warner Chappell are suing Anthropic."*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-opus5-system-prompt-export-controls.md` Claim 1 (Anthropic
    patched the exact dates and framing of a specific external regulatory event —
    a Department of Commerce export-control suspension — directly into the next
    model's system prompt): This source's Claim 2 is a second, independent
    instance of the same pattern — a specific external legal event (a copyright
    lawsuit filed days earlier) followed almost immediately by a system-prompt
    change addressing exactly that legal exposure. Together the two notes
    establish system-prompt-as-reactive-legal/regulatory-control-surface as a
    repeated Anthropic practice, not a one-off.
  - `blog-simonwillison-fable-silent-interventions.md` Claim 1 (Anthropic
    disclosed, only in a 319-page system card, that Fable 5 silently degrades
    responses for frontier LLM development work without notifying users): This
    source's Claim 7 documents a structurally different but thematically aligned
    finding — undisclosed, session-conditional prompt layers (`end_conversation`
    rules, memory, past-chats, web search/citation, artifacts) that sit outside
    the published core system prompt entirely. Both notes establish that the
    publicly documented "system prompt" and system card materially understate
    the full set of instructions and interventions actually governing Claude's
    behavior at runtime.
  - `blog-simonwillison-opus47-system-prompt.md` Claim 1 (the child-safety
    "contaminated conversation" rule persists and widens after a single refusal,
    for the rest of that conversation): This source's Claim 1 documents the same
    structural pattern — persistent, widening refusal after a single decline —
    applied to a different domain (copyright) in a later model generation.

- **Contradicts**: None filed. The apparent tension between this source's Claim 5
  (the "genuinely/honestly/straightforward" prohibition is present in Fable 5.1,
  September 2026) and `blog-simonwillison-opus47-system-prompt.md` Claim 12 (the
  same prohibition was removed from the Opus line in April 2026) is not a
  contradiction under MINER.md §4a — both notes accurately report the state of
  their respective model line at the time of writing, and the difference is a
  conditioning variable (model line and date), not two sources disagreeing about
  the same current state. See Claim 5's assessment for the interpretation.

- **Extends**:
  - `blog-simonwillison-opus47-system-prompt.md` (methodology: diffing Anthropic's
    publicly archived system prompts via git): This source documents Willison
    formalizing that ad hoc diffing approach into an automated daily pipeline
    (`simonw/claude-system-prompts`, a GitHub Actions workflow, a generated
    CHANGELOG.md, and an Atom feed) — the informal method used for the Opus
    4.6→4.7 note has become durable public tooling by the time of this source.
  - `blog-simonwillison-claude-fable-5.md` (initial Fable 5 hands-on evaluation,
    June 9, 2026, covering specs, pricing, and capability but explicitly not the
    system prompt): This source is the corpus's first look at Fable 5's actual
    published system prompt content, and the first documented diff against its
    successor, Fable 5.1 (released September 1, 2026 per this source — filling a
    three-month gap in the corpus's Fable-line coverage).

- **Novel**:
  - **First documented non-Anthropic-hosted URLs in a published Claude system
    prompt** (Claim 8): dancesafe.org, tripsit.me, and psychonautwiki.org are the
    first third-party domains Willison's own cross-prompt script found in any
    archived Claude system prompt.
  - **First direct, model-sourced confirmation of an unpublished, session-
    conditional prompt-layer architecture** (Claim 7): Fable 5.1 itself describes
    a stack of feature/tool-specific blocks (end_conversation, memory, past-chats,
    web search/citation, artifacts/file-creation) appended to the published core
    prompt depending on session configuration, none of which appear in Anthropic's
    public archive.
  - **First documented case of a full few-shot worked example (with an explicit
    model-facing rationale annotation) embedded directly in a production system
    prompt, plus a live reproduction of the model executing that exact example**
    (Claim 4).
  - **First documented practitioner pattern of deliberately using a different
    vendor's model to summarize a model's own system-prompt changes, specifically
    to avoid the summarizer inheriting bias from material that conditions its own
    opinions** (Claim 10).
  - **First evidence that a previously-removed style instruction (the "genuinely/
    honestly/straightforward" prohibition) reappeared in a different, later model
    line** (Claim 5) — a data point against assuming instruction removals reflect
    a permanent, cross-line behavioral fact about the underlying model.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a note that Anthropic's published
  system prompt archive (`platform.claude.com/docs/en/release-notes/system-prompts`)
  is confirmed, by the model's own account (Claim 7), to be incomplete —
  practitioners reverse-engineering Claude's behavior from the published archive
  should not assume it is the complete instruction set; feature-conditional
  blocks (memory, past-chats, web search/citation, artifacts, and
  conversation-ending rules) are appended per-session and never published. This
  should temper any guide language that treats the archive as an exhaustive
  behavioral contract (currently implied by the Guide Impact note in
  `blog-simonwillison-opus47-system-prompt.md`).
  - Also add Claim 10's "don't let a model grade its own conditioning material"
    pattern as a concrete practitioner recommendation for anyone building
    automated evaluation or changelog-generation harnesses around a specific
    vendor's model outputs.

- **Chapter 03 (Verification)**: Claim 4's live-reproduction methodology (quote
  the system prompt's worked example, then run the identical prompt against the
  model to confirm real behavior matches documented behavior) is a directly
  reusable verification pattern for any practitioner auditing whether a vendor's
  documented safety/behavioral claims hold up in practice.

- **Chapter 06 (Security Threat Model)**: Add Claim 3's anti-circumvention design
  (judging image requests by "what the finished picture would add up to," not by
  what it's named; refusing to enumerate what's missing from a declined image) as
  a concrete example of a vendor closing an iterative-refinement jailbreak
  pattern at the system-prompt level, relevant to any threat-modeling discussion
  of prompt-based content-restriction bypasses.

## Extraction Notes

- The source was read in full directly from the rendered HTML (fetched via
  `curl` and parsed with BeautifulSoup) rather than relying solely on the
  WebFetch tool. WebFetch's small-model summarizer initially declined to
  reproduce the post's text at all (citing copyright), and on a second, more
  narrowly scoped request returned quotes that were subtly reworded/truncated
  versions of the real text (e.g., eliding text from the visual-works rule with
  an ellipsis it inserted itself, not present in the source). All quotes used in
  this note were verified against the directly-fetched raw HTML of the blog post
  itself, and cross-checked a second time against Anthropic's own system prompt
  archive (`claude-fable-5-1.md`) and the raw GitHub `.diff` — both independent
  primary sources returned character-for-character identical text for every
  quoted passage.
- Followed sub-pages beyond the blog post itself: (1) the GitHub commit diff
  `simonw/claude-system-prompts@837a418b...` (raw `.diff`), to verify the
  before/after wording directly against the source repository rather than
  trusting the blog's rendering; (2) Anthropic's own Markdown export of the
  Fable 5.1 system prompt (`claude-fable-5-1.md`) on `platform.claude.com/docs`,
  to independently confirm every verbatim quote against the primary vendor
  document; (3) Anthropic's Fable 5.1 model overview page, to confirm the
  June 2026 knowledge-cutoff claim (Claim 9) against a second, independent
  Anthropic-hosted source; (4) the Guardian's coverage of the Sony/Warner
  Chappell lawsuit, to obtain the filing date and specifics needed to assess the
  timing argument in Claim 2. Not followed: the two `claude.ai/share/...`
  conversation transcript links (Claim 7's underlying conversation, and the
  live example reproduction in Claim 4) — these are consumer chat-share links
  outside this extraction's tooling; their content as summarized in the blog
  post itself was used and is quoted verbatim from the post, not reconstructed.
  Also not followed: the CHANGELOG.md file, the Atom feed, the GitHub Actions
  workflow file, and the `claude-code-transcripts` build-session transcript —
  these support Claim 10's methodology claim but were judged non-essential to
  verify beyond the direct quotes Willison already included in the post.
- No contradictions were identified that meet the bar in MINER.md §4a for filing
  a contradiction issue; see the "Contradicts" entry above for the one candidate
  considered and why it was not filed.
