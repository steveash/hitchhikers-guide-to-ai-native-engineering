---
source_url: https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/
source_type: blog-post
title: "Quoting Prompting Claude Fable 5.2 (code-ownership framing)"
author: Simon Willison (quoting Anthropic documentation)
date_published: 2026-11-10
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: emerging
issue: "#4635"
---

# Quoting Prompting Claude Fable 5.2 (code-ownership framing)

> A one-sentence "this codebase is yours" instruction in the system prompt is reported by Anthropic to raise Fable 5.2's merging of repeated code from under 1 in 10 tries to about 1 in 2 on small coding tasks, at the cost of ~1.5x output tokens and unrequested changes.

## Source Context

- **Type**: blog-post (a short quotation post on simonwillison.net, tagged `prompt-engineering`, `claude-mythos-fable`). It quotes the "Say who owns the code" section of Anthropic's docs page *Prompting Claude Fable 5.2*.
- **Author credibility**: Simon Willison is a trusted-feed author in this corpus; he adds no commentary here. The substantive authority is Anthropic's documentation (vendor, first-party testing).
- **Scope**: The quote covers one effect and the one-sentence fix. The Willison post omits the caveats that appear in the original docs section (token cost, unrequested changes, scope-rule interaction). Per the triage request, I fetched the original page (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code) and extracted those too. Quotes below are from the Anthropic page unless marked.

## Extracted Claims

### Claim 1: Fable 5.2 is highly sensitive to what the prompt says about who owns the code
- **Evidence**: Anthropic's internal testing on small coding tasks; no sample sizes or task set published.
- **Confidence**: emerging
- **Quote**: "Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on."
- **Our assessment**: Plausible and consistent with the model following instructions literally. Vendor-only evidence.

### Claim 2: Without ownership framing (or with the code presented as someone else's), the model adds to existing structure even when that duplicates code, and reports nearby problems rather than fixing them
- **Evidence**: Same Anthropic small-task testing.
- **Confidence**: emerging
- **Quote**: "the model tended to add to the existing structure, even when that repeated existing code. It also tended to report nearby problems instead of fixing them."
- **Our assessment**: Describes a conservative default that suits large shared codebases but yields duplication in agent-owned repos.

### Claim 3: A single sentence flips behavior: merging of repeated code goes from under a tenth of tries to about half
- **Evidence**: Anthropic testing on small coding tasks; rate "varied by task"; feature worked "in nearly every try either way".
- **Confidence**: emerging
- **Quote**: "the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it."
- **Our assessment**: Large effect size, but no N, no task list, not independently replicated. The quote appears identically in Willison's post.

### Claim 4: The effect survives a long system prompt
- **Evidence**: Anthropic testing (unquantified).
- **Confidence**: emerging
- **Quote**: "The result held when the sentence stood inside a long system prompt."
- **Our assessment**: Useful for CLAUDE.md placement, though "long" is undefined.

### Claim 5: The ownership framing costs about 1.5x output tokens and causes unrequested changes (new tests, docs, and behavior changes in 1 in 6 to 10 tries)
- **Evidence**: Same testing; effects larger at higher effort.
- **Confidence**: emerging
- **Quote**: "the model also used about 1.5 times the output tokens with the sentence and made several changes that nobody had asked for, many of them new tests and documentation."
- **Our assessment**: Important trade-off omitted from Willison's quote. Scope creep is the price of the refactoring behavior.

### Claim 6: The closing summary under-reports small changes, so the diff must be reviewed
- **Evidence**: Anthropic testing.
- **Confidence**: emerging
- **Quote**: "Its closing summary named the larger changes but often left out small ones, so review the diff and not only the summary."
- **Our assessment**: Reinforces a standing review-the-diff rule; relevant to verification chapters.

### Claim 7: A scope-limiting rule elsewhere in the prompt does not fully cancel the ownership sentence
- **Evidence**: Test with "No drive-by refactors, renames or cleanups" earlier in the prompt.
- **Confidence**: emerging
- **Quote**: "A rule elsewhere in the prompt that limits scope doesn’t cancel the ownership sentence."
- **Our assessment**: Warns that instruction conflicts resolve unpredictably (merging still occurred in about a third of tries); don't combine contradictory framing.

### Claim 8: Omit the sentence where the user owns the code and wants minimal change
- **Evidence**: Anthropic recommendation.
- **Confidence**: emerging
- **Quote**: "Leave the ownership sentence out where the user owns the code and wants it changed as little as possible."
- **Our assessment**: Sensible; framing should be per-repo/per-task, not a global default.

### Claim 9 (adjacent, same page): Cautionary text carried in memory/notes/instruction files accumulates and Fable 5.2 follows it closely
- **Evidence**: Anthropic simulated-task testing (e.g., retries after a busy tool in about four in ten tries with a "never retry" note in context).
- **Confidence**: emerging
- **Quote**: "Cautious instructions build up wherever context carries over: memory, notes, instruction files, and messages between agents."
- **Our assessment**: Same underlying lesson as Claim 1: wording in persistent context steers behavior strongly. Outside the issue's core scope; noted for Ch04/Ch02.

## Concrete Artifacts

Prompt sentence (Anthropic docs, quoted by Willison):

```text
This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.
```

Reported figures (Anthropic small-task testing): merged repeated code ~1/2 with the sentence vs <1/10 without; ~1/3 with the sentence plus "No drive-by refactors, renames or cleanups"; ~1.5x output tokens; behavior-changing edits in 1 of 6-10 tries.

## Cross-References

- **Corroborates**: `blog-simonwillison-fable-judgement.md` (Claims 1-2): both show that framing Fable with autonomy/ownership ("use your own judgement") rather than fixed rules changes behavior. `blog-simonwillison-fable-relentlessly-proactive.md` also covers Fable's proactive tendencies.
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-anthropic-opus47-best-practices.md` (general prompting guidance) and `blog-anthropic-large-codebase-best-practices.md` (CLAUDE.md content) with a concrete, quantified framing sentence. Also complements `blog-anthropic-claude-fable-and-mythos-5-2.md` (release announcement) and `blog-anthropic-safely-scaling-multi-agent-teams-fable-5-2.md`.
- **Novel**: Ownership framing as a prompt lever with measured effect and measured side effects (token cost, scope creep, summary omissions); the interaction with explicit no-refactor rules.

## Guide Impact

- **Chapter 04 (context engineering)**: Add the ownership sentence as an example of a single-line framing instruction with a quantified effect, with the caveats (vendor testing, small tasks, no N).
- **Chapter 02 (harness engineering)**: In guidance on CLAUDE.md/AGENTS.md wording, note that ownership framing should be chosen per repo (agent-owned vs. human-owned/minimal-diff) and that it pairs with diff review because summaries omit small changes. Do not stack it with "no drive-by refactors" rules.
- **Verification/review material**: Cite Claim 6 for "review the diff, not the summary".

## Extraction Notes

- Willison's post is only the quotation; the original Anthropic page was fetched and read in full, and the caveats above come from it. Other sections of that page (effort calibration, finishing tasks, subagent expectations, progress updates, reports) are out of this issue's scope and not extracted, except Claim 9.
- All figures are Anthropic-internal, no sample sizes or methodology given; treated as emerging, not settled. Whether the sentence was tested alone or alongside other prompt changes is stated only as "the sentence", i.e. appears to be tested alone, but the docs do not say so explicitly.
