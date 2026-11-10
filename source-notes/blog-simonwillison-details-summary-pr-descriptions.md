---
source_url: https://simonwillison.net/2026/Nov/9/details-summary/
source_type: blog-post
title: "Hide your slop PR descriptions behind <details><summary>"
author: Simon Willison
date_published: 2026-11-09
date_extracted: 2026-11-10
last_checked: 2026-11-10
status: current
confidence_overall: anecdotal
issue: "#4612"
---

# Hide your slop PR descriptions behind `<details><summary>`

> Willison proposes a low-effort convention for agent-authored PRs: a short human-curated opener, with the full agent-written description collapsed in a GitHub-rendered `<details><summary>` block labelled with model name and effort level.

## Source Context

- **Type**: blog-post (short practitioner tip, dated 9 Nov 2026)
- **Author credibility**: Simon Willison, Datasette/LLM maintainer, heavy daily user of Claude Code and Codex; reports from his own PR workflow.
- **Scope**: Covers the pattern, its rationale, five example PRs (datasette, datasette-agent, llm) and a mnemonic for tag order. No metrics, no data on whether reviewers behave differently. The datasette-specific examples are listed in Artifacts only briefly.

## Extracted Claims

### Claim 1: For this author the PR is the unit of work, and most changes arrive as agent-opened PRs
- **Evidence**: First-person workflow description.
- **Confidence**: anecdotal
- **Quote**: "Most of the changes I make to my projects these days come in the form of PRs opened for me by Claude Code or Codex."
- **Our assessment**: Consistent with PR-centric agent workflows; a self-report from one prolific maintainer, not a norm measurement.

### Claim 2: Agent PR descriptions are accurate and comprehensive, and that is exactly the problem: they read as slop and trigger skip-reading
- **Evidence**: Author's own reaction; no data.
- **Confidence**: anecdotal
- **Quote**: "It’s not necessarily slop, but it reads like slop!"
- **Our assessment**: Reframes the problem from accuracy to reader-cost. Different from Varda's complaint (descriptions were wrong-level) — here content is fine but volume and tone deter reading.

### Claim 3: The reader-cost asymmetry bothers even when the agent's driver is the author
- **Evidence**: Author's reaction.
- **Confidence**: anecdotal
- **Quote**: "I’m instantly put off by the thought that it will take me longer to read than it took the driving author to write... even when that driving author is me!"
- **Our assessment**: Names the core asymmetry (generation cost near zero, reading cost unchanged) that also underlies Ronacher's backpressure argument.

### Claim 4: What reviewers want is human editorial judgement in a short introduction that triages attention
- **Evidence**: Stated preference.
- **Confidence**: anecdotal
- **Quote**: "I want human editorial judgement."
- **Our assessment**: The opener is a triage signal ("does this deserve more of my attention"), not a summary of the diff. Useful framing for PR-template guidance.

### Claim 5: Collapse the full agent essay in `<details><summary>`, which GitHub Markdown renders natively
- **Evidence**: Pattern with HTML snippet; author uses it on his own PRs.
- **Confidence**: emerging (a simple mechanism that demonstrably works on GitHub; value for reviewers is self-reported)
- **Quote**: "Crucially, <details><summary> is supported in GitHub Markdown."
- **Our assessment**: Copy-pasteable and zero-tooling. Information is preserved rather than deleted, which is the main difference from banning agent descriptions.

### Claim 6: Label the collapsed block with model name and often effort level, to make provenance obvious
- **Evidence**: Author's practice; example "Claude Opus 5.5 Medium".
- **Confidence**: anecdotal
- **Quote**: "I use the model name and often the effort level as that summary, to make it abundantly clear what is going on"
- **Our assessment**: Doubles as lightweight AI-disclosure and provenance metadata. Not tied to any measured benefit.

### Claim 7: The opener is a promise from the human to the reader, and may be agent-derived
- **Evidence**: Author's stated practice.
- **Confidence**: anecdotal
- **Quote**: "My promise to the reader is that the short opener will represent my human judgement as to what is definitely worth their time."
- **Our assessment**: The accountability sits with the human regardless of who drafted the text; the agent may supply the opener, the human must vet it. This is the key condition separating the practice from rubber-stamping.

### Claim 8: Screenshots in the opener are often the fastest way to convey a UI change
- **Evidence**: Practice, with examples.
- **Confidence**: anecdotal
- **Quote**: "I’ll sometimes throw in a screenshot as well, since images are often the best way to quickly illustrate a new feature."
- **Our assessment**: Minor but practical; applies to UI-affecting agent PRs.

### Claim 9: Result: PRs feel less sloppy while all information remains available
- **Evidence**: Self-assessment only; no reviewer feedback or timing.
- **Confidence**: anecdotal
- **Quote**: "My PRs don’t feel nearly as sloppy now!"
- **Our assessment**: Unvalidated; the effect on actual review behaviour is not measured. Treat as a hypothesis.

## Concrete Artifacts

Snippet from the source (Willison, 2026-11-09):

```html
<details>
  <summary>Claude Opus 5.5</summary>
  <h2>The hook</h2>
  Plugins implement <code>register_agent_reference_types(datasette)</code>...
</details>
```

Opener examples cited (datasette #3052, #3043, #3042; datasette-agent #51; llm #1838) share a shape: one to two sentences stating the user-visible change and why, sometimes with a screenshot or `--help` output. Example from the source: "Adds commands for managing the records in extra-openai-models.yaml, so OpenAI-compatible endpoints can be saved from the command line instead of by hand-editing YAML."

Mnemonic: say "details-summary" (2+3 syllables) to remember tag order; `<summary>` is the clickable line, `<details>` wraps everything.

## Cross-References

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 11 (agent output as "energy vampire" draining recipients' attention) — Willison's reader-cost complaint is the same dynamic applied to PRs; and Claim 4 there (cheap generation vs. costly reading).
- **Contradicts**: None filed. `blog-simonwillison-kenton-varda-change-descriptions.md` (Claims 1–3) bans AI-written change descriptions outright whereas Willison keeps them but collapses them. This is a difference in remedy conditioned on whether a human-vetted opener exists, not a factual contradiction, so no contradiction issue was filed.
- **Extends**: `blog-simonwillison-kenton-varda-change-descriptions.md` Claim 2 (descriptions restate code-visible detail while omitting high-level framing): Willison's opener is a concrete remedy for the missing high-level framing. `blog-simonwillison-commit-rewriter.md` addresses the same cleanup concern for commit messages (see its Claim 1).
- **Novel**: A concrete formatting convention (human opener + collapsed agent body labelled with model/effort) for agent-authored PRs; no existing note covers PR-description formatting.

## Guide Impact

- **Chapter 03**: Where PR descriptions or review burden for agent output are discussed, add the "human opener + collapsed agent body" pattern as a lighter alternative to Varda's ban, flagged anecdotal and with the HTML snippet.
- **Chapter 05**: Candidate team norm: agent-authored PRs open with a human-vetted short paragraph; agent essay collapsed and labelled with model/effort. Anecdotal; one practitioner.

## Extraction Notes

- Read the full post; it is short and has no sub-pages worth following. Datasette-specific PR links were not followed (per triage guidance), only the opener quotes in the post were noted.
- Thin source: no metrics or review-outcome data. Confidence is anecdotal overall.
