---
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_type: blog-post
title: "The components of agent memory"
author: Lance Martin (Anthropic Engineering)
date_published: 2026-11-06
date_extracted: 2026-11-07
last_checked: 2026-11-07
status: current
confidence_overall: emerging
issue: "#4570"
---

# The components of agent memory

> Anthropic's eval-backed account of what agents should write to memory (salience judgment beats fixed rules for frontier models) and how "dreaming" (offline replay of transcripts) corrects notes, builds wikis, and manages the injected top layer of memory.

## Source Context

- **Type**: blog-post (first-party Anthropic Engineering post, published 2026-11-06, tagged Agents / Context engineering / Agent memory)
- **Author credibility**: Written by Lance Martin with editorial guidance from Anthropic staff; first-party, with direct access to internal evals. Authoritative on Claude's behavior; all results are Anthropic-internal and vendor-favorable, and several are single runs.
- **Scope**: Defines "agent memory" narrowly (cross-session, saved as readable context; excludes weights, in-context learning, compaction). Covers CL-Bench 1.0, Pokémon Red, a Stainless corpus wiki eval, Harvey LAB, and Claude Code auto memory. Does not give raw numbers for most figures (charts only) and does not compare vendors.

## Extracted Claims

### Claim 1: "Agent memory" is defined as cross-session knowledge saved as readable context, explicitly excluding weights, in-context learning, and compaction
- **Evidence**: Definitional framing by the authors; no measurement.
- **Confidence**: settled (as a definition; useful scoping)
- **Quote**: "By “agent memory,” we mean knowledge that Claude gains from experience—including interactions with users and tasks it’s been assigned—and that it retains between sessions, saved as context it can read later."
- **Our assessment**: Clean taxonomy that separates memory from compaction (Ch04's compaction material) and from in-context learning. Adopt when citing this source; do not generalize its eval results to compaction.

### Claim 2: Writing a memory is a prediction about future relevance, so salience is hard to judge in the moment
- **Evidence**: Conceptual framing, illustrated by CL-Bench and Pokémon results. The authors' model, not a measured result.
- **Confidence**: emerging
- **Quote**: "By writing down a rule, an agent predicts that the pattern it’s describing will be relevant again."
- **Our assessment**: Useful mental model: a "verified fact" note is a bet that a future session may rely on it without re-checking, which is exactly why wrong notes are costly (Claim 7).

### Claim 3: On CL-Bench's database task, models differ in how far they close a test-and-record learning loop; Opus 5 and later were the first to close it
- **Evidence**: Claude Managed Agents run, fresh session per question, persistent memory directory. Qualitative description of memory contents per model (Sonnet 4.6: untested guesses; Opus 4.7: consolidated reference marking checked vs unconfirmed; Sonnet 5: confirmed after grader check plus corrections; Opus 5: rule + how it knew + answers + trap warnings). Scores shown only in a figure.
- **Confidence**: emerging
- **Quote**: "Claude Opus 5 was the first of these models to close the loop."
- **Our assessment**: Plausible and concretely described, but internal benchmark; no numeric scores in text. Opus 5.5 and Sonnet 5.5 "scored about the same as Opus 5" with memory, per the post.

### Claim 4: In Pokémon Red, indiscriminate memory writing (Sonnet 3.7: 413 files) underperformed a small, selective memory (Fable 5: 9 files) that stores only what the game does not show
- **Evidence**: One run each, compared about 10,000 steps in. Sonnet 3.7: 413 files across 225 folders, 1 badge; Fable 5: nine files in two folders plus `global.md`, 4 badges. Sonnet 3.7 spent steps reorganizing: over 17 steps it "created six files, deleted nine others, and took no actions in the game itself." Opus 5.5 also kept a small goal/next-steps folder and beat the game.
- **Confidence**: anecdotal (single run per model, different model generations)
- **Quote**: "Fable 5’s approach used memory for things the game didn’t explicitly tell it."
- **Our assessment**: Vivid illustration of a real failure mode (memory bloat and staleness of observable state), but confounded by model generation and n=1. Treat as illustration, not proof that small memory is better.

### Claim 5: A fixed write rule ("record only failures") removed much of the memory gain for Opus 5 and Opus 4.7; for stronger models, freedom to judge salience beat fixed rules
- **Evidence**: CL-Bench ablation, one rule per test, compared gain from memory with vs without the rule (Figure 5, right; no numbers in text).
- **Confidence**: emerging
- **Quote**: "For stronger models, giving them freedom to judge salience was more effective than setting fixed rules in advance, and those rules could end up weakening performance."
- **Our assessment**: Directly relevant to prescriptive CLAUDE.md/memory instructions. Tested only one rule type on one task; generalize cautiously.

### Claim 6: Steering matters most for older models: telling Sonnet 4.6 to read memory and test theories nearly doubled its score; Sonnet 5 reads memory unprompted 9 of 10 times
- **Evidence**: CL-Bench with/without prompting (Figure 5, left). Sonnet 5 read memory before answering 9/10 times vs fewer than half for Sonnet 4.6.
- **Confidence**: emerging
- **Quote**: "We’ve found that it helps to tell Claude what memory is for, but not  how  to use it."
- **Our assessment**: Consistent with the broader "scaffolding shrinks as models improve" theme. Practical rule: say what memory is for; keep guidance simple, and expect to add steering only for weaker models. (Quote contains a double space from the source's italic markup.)

### Claim 7: Wrong or drifted notes are trusted by later sessions; dreaming can validate notes against the transcript as ground truth
- **Evidence**: Pokémon Mt. Moon case: Claude wrote the PokéCenter was on the east side, declared "Mt Moon DONE," and fell off a one-way ledge repeatedly. After dreaming rewrote the note, the run re-entered the cave and reached Cerulean City; the uncorrected run dropped back three times and never got past the mountain; the no-memory run also did not pass it.
- **Confidence**: anecdotal (single run per condition)
- **Quote**: "The transcript gave Claude a ground truth to validate its memory against."
- **Our assessment**: Strongest concrete evidence of dreaming as error correction, but one scenario. Note the structural point: correction works because an independent record (transcript) exists to check against.

### Claim 8: Wikis built by repeated dreaming improve with more sessions, help most combined with search, and help on cross-document tasks but not single-document ones
- **Evidence**: ~350,000 files / ~420M tokens of Stainless internal docs; 25 questions; Opus 5 agents over 128 sessions with a shared coordination log. Wiki-only score rose from 13% to 48% (2 to 128 sessions); search+wiki rose from 54% to 61% vs 53% search alone; saved about 20,000 tokens per question. Harvey LAB merger set (24 questions): 87% with wiki vs 73% search alone on multi-document items; one LAB task showed no clear wiki gain; another produced a wiki larger than the source documents.
- **Confidence**: emerging (internal evals; small question sets: 25 and 24)
- **Quote**: "When it used both search and the wiki, Claude’s aggregate score rose from 54% to 61% as that wiki grew, compared with 53% when it had access to the search tool alone."
- **Our assessment**: Gain over search alone is modest (53 to 61) and on a 25-question set; wiki-only (48%) is below search-only. The Borges "map as large as the empire" failure is a useful caution about detail without abstraction.

### Claim 9: The injected top layer of memory must stay small; dreaming's job includes demoting details and leaving links
- **Evidence**: Authors' reasoning (tokens, wrong notes propagate to every session, longer instruction files reduce adherence per Claude Code docs); Claude Code auto memory loads only the first 200 lines or 25 KB of `MEMORY.md`.
- **Confidence**: emerging
- **Quote**: "It loads only the first 200 lines or 25 KB of  MEMORY.md ."
- **Our assessment**: Concrete, checkable limit. Reinforces the index-plus-links pattern for memory files. (Quote contains source markup spacing.)

### Claim 10: Dreaming instructions should be goal-specific, and a reflect-and-rewrite loop can find the right instructions; one writer per page avoided overwrite losses
- **Evidence**: LAB acquisition-contracts task: several agents writing one shared table kept 41 of 57 graded facts (72%); after Claude reflected on failures and rewrote the instructions, one agent per contract page quoting terms word for word kept 57 of 57 (100%).
- **Confidence**: anecdotal (one task)
- **Quote**: "Each contract got its own page in the wiki, written by a single agent, which quoted the terms word for word rather than summarizing them into a shared table."
- **Our assessment**: Good concrete multi-agent shared-state lesson (partition writes; preserve exact terms). One task, so the numbers are illustrative.

### Claim 11: Dreaming across sessions can fix gaps single sessions leave, such as dangling links and missing index pages
- **Evidence**: Second dreaming pass on a LAB wiki found nine links to a missing page and repointed them, and added three pages including an index.
- **Confidence**: anecdotal
- **Quote**: "A second dreaming pass closed many of these gaps."
- **Our assessment**: Plausible; a single example, no aggregate stats.

### Claim 12: Open questions: write in the moment vs in the background, keeping memory current, and compute cost of maintenance
- **Evidence**: Authors' discussion; they note in-moment logging "draws Claude’s attention away from its main task," while dreaming outputs are not immediately accessible, and suggest tuning dreaming cadence or focusing on likely-to-change info.
- **Confidence**: emerging
- **Quote**: "Even though Claude’s judgment about salience has improved, no model can really know what will happen in future turns."
- **Our assessment**: Honest framing; the post does not resolve the tradeoffs and gives no data on dreaming cost.

## Concrete Artifacts

Memory-structure comparison (Pokémon Red, ~10,000 steps, source Claim 4 section):

```
Sonnet 3.7: 413 memory files across 225 folders, 1 badge
            (a file per battle, item, and NPC; fourth "master" folder started around step 10,000)
Fable 5:    9 files in 2 folders + global.md, 4 badges
            global.md = dashboard: current goal, prewritten gym plan, model's own rules for using memory
            locations/ = route navigation plans
            gameplay/  = strategies learned about how the game works
```

Example memory note written by Fable 5 (attributed in source):

```
"If 3+ balls fail in a row, VARY the timing (insert extra ‘wait’ presses between menu steps) - the catch landed right after doing this."
```

Wiki eval numbers (source):

```
Stainless corpus (~350,000 files, ~420M tokens), 25 questions, 128 Opus 5 dreaming sessions
  wiki only:      13% (2 sessions) -> 48% (128 sessions)
  search only:    53%
  search + wiki:  54% -> 61% as wiki grew; ~20,000 tokens saved per question
Harvey LAB merger set, 24 questions (multi-document items): wiki 87% vs search 73%
Contract-terms wiki: 41/57 facts (72%) shared table -> 57/57 (100%) one page per contract
```

## Cross-References

- **Corroborates**: `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 1 and Claim 3 (dreaming as an asynchronous between-session process refining what in-session memory captured); this post supplies the mechanism and eval evidence the product announcement lacks. `blog-anthropic-claude-managed-agents-memory.md` Claim 9 (Opus 4.7 "more discerning about what to remember") is consistent with Claims 3-5 here.
- **Contradicts**: None filed. Claim 5 (fixed write rules hurt strong models) is in tension with guidance elsewhere in the corpus that prescribes explicit memory-write instructions, but I did not find a note that makes the opposing claim for the same models and conditions, so no contradiction issue was filed.
- **Extends**: `blog-anthropic-claude-managed-agents-memory.md` Claim 2 (filesystem-mounted memory) and Claim 6 (concurrent agents on one store): this post shows the overwrite failure mode (41/57 facts) and the one-page-per-writer fix. `blog-openai-chatgpt-memory-dreaming.md` Claim 3 and Claim 7 (background curation; revising time-sensitive facts): same pattern from a different vendor, here with ground-truth correction from transcripts. `blog-langchain-harness-memory.md` Claim 5 (context management as foundation for memory): this post adds the explicit boundary between memory and compaction.
- **Novel**: Salience ablation ("record only failures"); the 413-vs-9 file comparison; transcript-grounded correction of a wrong note; wiki scaling curve with session count; the 200-line / 25 KB injected-index limit; the memory-vs-compaction-vs-in-context-learning definition.

## Guide Impact

- **Chapter 04**: Add a short section separating agent memory from compaction and in-context learning (Claim 1) and covering memory layers (transcripts, notes, representations, injected context). Cite Claim 5/6 for "state what memory is for, don't script how"; cite Claim 9 for keeping the injected index small.
- **Chapter 02**: Add dreaming as an offline harness process with transcript-as-ground-truth correction (Claim 7), and the one-writer-per-page rule for multi-agent memory (Claim 10).
- **Chapter 03**: Mention that memory notes marked "verified" should be checkable against a record of what happened (Claims 3, 7).
- Caveat for the Smith: every result is Anthropic-internal; label Pokémon items as single-run anecdotes.

## Extraction Notes

- Read the full article via raw HTML text extraction (no paywall). Figures are charts and were not readable; numbers are taken only from the article text. The post mentions cookbooks for dreaming and knowledge wikis; those were not followed.
- Quotes copied verbatim from the page text; two contain double spaces from italic markup in the original.
- Cross-referenced claim numbers were verified against the headings of the cited notes.
