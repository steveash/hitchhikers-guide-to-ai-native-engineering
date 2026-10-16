---
source_url: https://simonwillison.net/2026/Oct/9/built-using-my-voice/
source_type: blog-post
title: "A new feature for my blog, built using my voice"
author: Simon Willison
date_published: 2026-10-09
date_extracted: 2026-10-16
last_checked: 2026-10-16
status: current
confidence_overall: anecdotal
issue: "#4146"
---

# A new feature for my blog, built using my voice

> A single-practitioner account of building a Django feature via Codex voice mode against a live local preview, then finishing by typed review of an agent-opened PR; voice suits multi-tasking, typing wins for detail.

## Source Context

- **Type**: blog-post (first-person experience report)
- **Author credibility**: Simon Willison is a long-running Django co-creator and prolific LLM tooling commentator; claims here are his own session observations, not measurements.
- **Scope**: One feature (a Newsletters page) on his own blog, ~30 min voice + ~30 min typed review. No metrics, no code in the post (a voice transcript is in a linked Gist). Model name "GPT-6 Astra High" is vendor-reported and not verified here. Feature details (newsletter page design) are not guide-relevant and are not extracted.

## Extracted Claims

### Claim 1: Voice mode paired with a live local preview of the app makes a coding agent more powerful than voice alone
- **Evidence**: He started the session by typing "Start dev server and open in browser", then gave visual feedback from across the kitchen; the agent designed the page and revised it from his spoken reactions.
- **Confidence**: anecdotal
- **Quote**: "The addition of the visual preview, plus being able to type or paste things in via the keyboard when I need to communicate something that doesn’t work vocally, makes this a much more powerful way of interacting with a coding agent."
- **Our assessment**: Plausible and consistent with general feedback-loop arguments; it is one user's impression. The useful harness point is that a running preview gives the agent and human a shared visual channel.

### Claim 2: A substantial multi-part feature was built almost entirely by voice in about half an hour
- **Evidence**: Model, migration, admin config, four importers, archive pages, search integration; transcript in a Gist; model "would reply and occasionally ask clarifying questions, then get to work".
- **Confidence**: anecdotal
- **Quote**: "We went on like this for about half an hour (the time it took to cook dinner)."
- **Our assessment**: Credible but unmeasured; the task was a well-understood Django feature he was "certain" the model could do, so it is a favourable case.

### Claim 3: Spoken, disfluent requirements were sufficient for the agent to infer intent
- **Evidence**: Transcript excerpt full of false starts about which pages newsletters should/shouldn't appear on and which should be searchable.
- **Confidence**: anecdotal
- **Quote**: "Apparently this was clear enough that the model knew what I wanted to build!"
- **Our assessment**: Suggests spec quality tolerates messy phrasing when the human has a clear mental model; one data point.

### Claim 4: Final review happened in the GitHub PR UI, and the human corrected an agent design choice (git subprocess vs API import)
- **Evidence**: Agent used Git in a subprocess for an import; because one source was a private repo, he had it swapped for an API-based import. Extra commits on the PR show the changes.
- **Confidence**: anecdotal
- **Quote**: "It was nearly what I needed, except it had chosen to use Git in a subprocess for one of the import scripts."
- **Our assessment**: A concrete example of PR-as-review-gate catching a design choice the agent could not know the constraints of (private repo / credential setup). Worth a supporting citation for human review of agent PRs.

### Claim 5: Review and fine-tuning cost roughly as much time again, done by typing
- **Evidence**: Authors' own account of the second phase.
- **Confidence**: anecdotal
- **Quote**: "It took an additional half hour of typing-based prompting to get to the point where I was happy to deploy it to production by landing the PR."
- **Our assessment**: Indicates voice produced a ~"mostly done" draft, not a shippable result; total effort about 1 hour, though unmeasured against a baseline.

### Claim 6: Detail work (errors, pointing at code) stays more efficient by typing
- **Evidence**: Author's stated working practice.
- **Confidence**: anecdotal
- **Quote**: "Being able to paste in examples and error messages, or directly highlight the code or feature that needs changing, remains more efficient than trying to describe it in words."
- **Our assessment**: Believable; reflects a modality split (voice for intent/direction, text for precise references).

### Claim 7: Voice is better for multi-tasking than as a daily driver
- **Evidence**: Author's verdict; contrasts with prior phone voice-mode use for research/brainstorming while walking the dog; notes privacy/shared-workspace limits.
- **Confidence**: anecdotal
- **Quote**: "The killer feature for me is the ability to multi-task."
- **Our assessment**: Single-user opinion; do not generalise to productivity. The non-obvious value is making otherwise-dead time usable.

### Claim 8: The agent knew of an undocumented API and researched pagination itself
- **Evidence**: Agent tried `/api/v1/archive` directly, then searched and found a third-party article.
- **Confidence**: anecdotal
- **Quote**: "which GPT-6 Astra knew about (it tried /api/v1/archive directly) and then ran a search to figure out how to paginate it"
- **Our assessment**: Minor; shows agents combining training knowledge with web search. Minor corroboration only.

## Concrete Artifacts

```
Opening typed prompt (Willison, post):
Start dev server and open in browser

Workflow (post): type prompt to start dev server -> "Start new voice chat" (Codex tab, ChatGPT desktop app)
 -> ~30 min voice dialogue with clarifying questions + visual preview checks
 -> Codex creates branch and opens PR -> human review in GitHub PR UI
 -> switch to typed prompts for fixes (~30 min) -> land PR.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-gptlive-voice-delegation.md` (voice used hands-free during other activity; Claim 7 there, hour-long walking conversation).
- **Contradicts**: none found.
- **Extends**: `blog-simonwillison-voice-mode-weaker.md` (Claim 2 there contrasts weak voice mode with strong Codex models); this note shows the Codex-based voice mode closing that gap for coding.
- **Novel**: Voice-driven coding agent session with live preview, followed by typed PR review; no existing note covers this.

## Guide Impact

- **Chapter 01**: Optional supporting citation in any interaction-mode discussion: voice for drafting/multi-tasking, typing for errors and code pointers (Claims 1, 6, 7), flagged as a single-user observation.
- **Chapter 02**: Optional example for human-in-the-loop PR review catching a design choice (Claim 4). Low priority; no new section warranted.

## Extraction Notes

- Read the full post (fetched raw HTML, extracted text). Did not read the linked Gist transcript or the Karen Spinner article. Quotes copied verbatim from the page text. Cross-references verified against claim numbering in the cited notes (gptlive Claim 7 is the hour-long hands-free conversation; voice-mode-weaker Claim 2 is the Karpathy contrast).
