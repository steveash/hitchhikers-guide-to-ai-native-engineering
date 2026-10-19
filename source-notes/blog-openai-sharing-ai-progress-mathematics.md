---
source_url: https://openai.com/index/sharing-ai-progress-in-mathematics
source_type: blog-post
title: "Sharing AI progress in mathematics"
author: OpenAI
date_published: 2026-10-06
date_extracted: 2026-10-19
last_checked: 2026-10-19
status: current
confidence_overall: emerging
issue: "#4210"
---

# Sharing AI progress in mathematics

> OpenAI's disclosure post for a batch of AI-produced math results: it describes the release protocol (GitHub repo, Lean formalizations, compute and reasoning disclosures) rather than the results themselves, and is the first in-corpus OpenAI math post that ships a checkable artifact repository plus a per-result compute figure.

## Source Context

- **Type**: blog-post (OpenAI, Research / Publication category; updated 2026-10-15)
- **Author credibility**: First-party OpenAI announcement. Authoritative about what OpenAI released and how; all result counts, compute figures and "internal frontier model" capability claims are self-reported.
- **Scope**: Short post (~600 words). Covers release mechanics, verification artifacts, transparency disclosures and funding. It does NOT enumerate the problems, give a result count in the readable text, name the model, or describe the agent harness. The page body has an interactive/"Loading…" section and a "View on GitHub" link to `github.com/openai/math`; only the static text was readable.
- **Access note**: openai.com returned HTTP 403 to direct fetches; the text was read from a Wayback Machine snapshot (captured 2026-10-17). The GitHub repo itself was not read.

## Extracted Claims

### Claim 1: OpenAI released a broad set of new mathematical results produced by an internal, unreleased frontier model
- **Evidence**: Announcement only; the problems and results live in the linked GitHub repository, not in the post text.
- **Confidence**: anecdotal (self-reported; no independent verification in the post)
- **Quote**: "We’re releasing a broad range of new mathematical results produced by an internal frontier model."
- **Our assessment**: Consistent with the earlier notes. The post gives no count, so it neither confirms nor narrows the ">100 open problems" figure in the advisory-group note.

### Claim 2: The release was shaped by advice from the independent IAS Advisory Group on Mathematics and AI
- **Evidence**: Post cites consultation and public recommendations from the group.
- **Confidence**: emerging
- **Quote**: "we’ve been consulting with the independent Advisory Group on Mathematics and Artificial Intelligence at the Institute for Advanced Study⁠(opens in a new window) to develop best practices"
- **Our assessment**: This is the first observable output of the advisory-group process described in the Sept 21 note. Whether the group endorsed this release is not stated; "drawn on their advice" is OpenAI's characterisation.

### Claim 3: Results are published in a GitHub repository with protocols for paper revisions and citations, with community-hosted alternatives still being explored
- **Evidence**: Repo link (`github.com/openai/math`) in the page.
- **Confidence**: emerging
- **Quote**: "we’re publishing the results in a GitHub repository, with protocols for paper revisions and citations."
- **Our assessment**: Hosting results in a vendor-controlled repo (not arXiv or a journal) is a governance choice; the post concedes it is provisional ("We’re continuing to explore other community-hosted alternatives").

### Claim 4: Lean formalizations of "many" (not all) proofs are shared, with more to be added as obtained
- **Evidence**: Lean files in the repo (not inspected).
- **Confidence**: emerging
- **Quote**: "we are sharing formalizations of many of the proofs in Lean, a programming language that allows mathematical proofs to be checked by a computer."
- **Our assessment**: Key nuance: "many", not all, so some results ship informal proofs only. This is weaker than the Ten Advances release, where Willison's note reports Lean 4 formalizations of all ten results. Formal checking is the independent verification channel; the post does not say which results lack it.

### Claim 5: OpenAI publishes process-transparency material: reasoning summaries, compute estimates in ChatGPT Pro terms, and attempted-problem statistics
- **Evidence**: Repository contents per the post.
- **Confidence**: emerging
- **Quote**: "These include 10 summaries of the model’s reasoning, estimations of compute spent in terms of Pro usage on ChatGPT, and statistics about the number of attempted problems."
- **Our assessment**: Publishing attempted-problem statistics partly answers Willison's complaint (Ten Advances note, Claim 2) that the denominator of failures was missing. We have not seen the statistics; verify in the repo. Note these are "summaries" of reasoning, not raw traces.

### Claim 6: The average result used roughly three hours of ChatGPT Pro thinking
- **Evidence**: Self-reported average; no distribution, variance or hardware detail.
- **Confidence**: anecdotal
- **Quote**: "The average result used the equivalent compute of roughly three hours of ChatGPT Pro thinking."
- **Our assessment**: A useful unit of account for agentic work but it is an average over successes, and is hard to reconcile with the 10,000-agent, ~88-hour Navier–Stokes effort (Navier–Stokes note, Claims 3 and 7), which was clearly an outlier. Treat as unverified.

### Claim 7: OpenAI plans to release the model that produced the results and to fund community workshops
- **Evidence**: Stated intent; plus an Oct 15 update committing $5 million to a Simons Foundation initiative, with model and compute access for supported researchers.
- **Confidence**: anecdotal (commitment, no timeline)
- **Quote**: "are working to responsibly release the model that produced these results."
- **Our assessment**: No date or capability gating is given. The Oct 15 update ("we are contributing $5 million to a new Simons Foundation initiative") is a funding commitment, not a result.

### Claim 8: OpenAI commits to updating its disclosure standards based on community feedback
- **Evidence**: Stated commitment only.
- **Confidence**: anecdotal
- **Quote**: "We will continue to act on feedback from the community and update our standards for future disclosures of major scientific advancements."
- **Our assessment**: Signals that the format (repo + Lean + compute disclosure) is a draft norm. Nothing about pacing, which the advisory-group note (Claim 6) says is outside the group's remit.

## Concrete Artifacts

```
Release package (OpenAI, "Sharing AI progress in mathematics", 2026-10-06):
- GitHub repository (github.com/openai/math) containing:
  - results/papers with "protocols for paper revisions and citations"
  - Lean formalizations of "many of the proofs" (to be extended)
  - "10 summaries of the model's reasoning"
  - "estimations of compute spent in terms of Pro usage on ChatGPT"
  - "statistics about the number of attempted problems"
- Reported average cost: "roughly three hours of ChatGPT Pro thinking" per result
- Update 2026-10-15: $5 million to a Simons Foundation initiative (workshops, conferences, special programs)
```

## Cross-References

- **Corroborates**: `blog-openai-advisory-group-mathematics-ai.md` (Claim 1) — same program; this post is the release the group's formation anticipated. `blog-simonwillison-ten-advances-mathematics.md` (Claim 3) — same pattern of shipping Lean formalizations alongside results.
- **Contradicts**: None filed. Mild tension only: "many of the proofs" in Lean versus all ten formalized in the Ten Advances release is a difference in scope, not a conflicting claim.
- **Extends**: `blog-simonwillison-ten-advances-mathematics.md` (Claim 2) — this post says attempted-problem statistics are published, addressing the missing denominator. `blog-openai-navier-stokes-solution.md` (Claim 8) — adds a per-result average compute figure alongside that note's aggregate message/token counts.
- **Novel**: Release protocol (citation/revision protocols in a repo), the "three hours of ChatGPT Pro" unit, the Simons Foundation $5M commitment, and the explicit plan to release the underlying model.

## Guide Impact

- **Ch03 (verification)**: Add this as an example of formal proof checking as an independent verification channel, with the caveat that coverage is partial ("many") and the artifacts are vendor-hosted. Cite alongside the Ten Advances note.
- **Ch04 (evidence handling)**: Example of disclosing denominators (attempted-problem statistics) and compute alongside successes; recommend readers demand these when evaluating AI-result announcements.
- **Ch02 (optional sidebar)**: The "~3 hours of Pro thinking per average result" figure is one concrete datapoint for cost of long-horizon agent runs, flagged as self-reported.

## Extraction Notes

- Source was short; extraction is complete for the static text. Read via Wayback snapshot because of HTTP 403 on openai.com. An interactive section ("Loading…") was not rendered, so any embedded result list/count is not captured here.
- GitHub repo `openai/math` was not read; claims about its contents are as described by the post. A follow-up could mine the repo (problem list, Lean coverage, attempted-problem statistics).
- The post says "10 summaries of the model’s reasoning" (quoted as written); the number may be a typo or a literal count.
- Related aggregator issue #4213 (AINews "722 math papers") is not cited because it was not read; the post text contains no "722" figure.
