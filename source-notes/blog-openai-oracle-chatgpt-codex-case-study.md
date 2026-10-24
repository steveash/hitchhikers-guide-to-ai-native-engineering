---
source_url: https://openai.com/index/oracle
source_type: blog-post
title: "How Oracle turns days of work into minutes with ChatGPT and Codex"
author: OpenAI (customer story; named Oracle quotes from Jan Ackerman, Richard Lam, Barry Shilmover)
date_published: 2026-10-08
date_extracted: 2026-10-24
last_checked: 2026-10-24
status: current
confidence_overall: anecdotal
issue: "#4298"
---

# How Oracle turns days of work into minutes with ChatGPT and Codex

> An OpenAI customer story with three named Oracle executives describing a recruiting research tool, an ontology-backed natural-language-to-SQL layer, and SRE incident triage built with ChatGPT Work and Codex; all outcome figures are vendor-reported and unmethodologised, but the "leadership lessons" are specific and usable.

## Source Context

- **Type**: blog-post (OpenAI "Customer Stories" page, published October 8, 2026; auto-discovered via the `openai-news` trusted feed).
- **Author credibility**: Vendor-authored marketing. Credibility is partly offset by three named Oracle leaders quoted by title: Jan Ackerman (SVP and Global Head of Talent Acquisition), Richard Lam (Group VP, Oracle Applications Lab), Barry Shilmover (VP and Technical Advisor to the CIO). No independent measurement.
- **Scope**: Covers three use cases (talent market intelligence tool, Applications Lab ontology + Codex for business questions, SRE incident context) and three leadership lessons. Does NOT cover: how the 98% figure was measured, model/config details, rollout timeline, cost, security architecture, or failures.

## Extracted Claims

### Claim 1: Oracle's talent acquisition team built a talent market intelligence tool in ChatGPT Work that cut multi-day research to a 15–20 minute prep
- **Evidence**: Workflow description (job description in; comparable-role research, compensation benchmarking, talent-pool assessment by location out); a named executive quote; headline stat card "98% Decrease in the time it takes for talent acquisition research" (no method given). The text says the prep previously took 2–4 days.
- **Confidence**: anecdotal
- **Quote**: "Now we’re able to sit down and prep for about 15 to 20 minutes using the tool that we’ve built using [ChatGPT] Work."
- **Our assessment**: The 2–4 days → 15–20 minutes is consistent with a ~98% reduction arithmetically, so the card is internally coherent, but it is a self-reported estimate with no baseline study, no output-quality check, and it compares compiled research against a prep session. The user is a non-engineer building their own tool, which is the interesting part.

### Claim 2: A standardized tool made recruiting intake consistent across recruiters
- **Evidence**: Author assertion in the article; no measure of consistency.
- **Confidence**: anecdotal
- **Quote**: "Recruiters used to run the intake process differently from one search to the next, but with the talent market intelligence tool, the process is consistent"
- **Our assessment**: Plausible and a real second-order benefit (encoded procedure vs. per-person variation), but unquantified.

### Claim 3: An ontology of company objects, relationships, and rules lets Codex turn plain-language business questions into reliable SQL and decide which systems to call
- **Evidence**: Architecture description from the Applications Lab; one user anecdote in which the result matched the old manual process "exactly."
- **Confidence**: anecdotal
- **Quote**: "built an ontology of the company’s objects, relationships, and rules, so a plain-language business question can be turned into a reliable SQL query with Codex."
- **Our assessment**: The most technically substantive claim: grounding the agent in an explicit domain model, not raw schema. The validation is n=1 and told second-hand. No info on ontology format, maintenance, or error rates.

### Claim 4: SREs use Codex to gather incident context and pull the right playbook; simple incidents drop from an hour to minutes
- **Evidence**: Quote from Richard Lam; no incident data.
- **Confidence**: anecdotal
- **Quote**: "A typical simple incident that used to take an hour to resolve can now be handled in minutes,"
- **Our assessment**: Scoped to "simple" incidents, which limits the claim. Compare the NTT DATA incident-analysis story linked in the page's "keep reading" (not mined here).

### Claim 5: Adoption scale is 130K active ChatGPT users and 95K+ active Codex users at Oracle
- **Evidence**: Stat cards on the page; the body text says "Over a hundred thousand employees."
- **Confidence**: anecdotal
- **Quote**: "Over a hundred thousand employees across Oracle are using ChatGPT Work and Codex"
- **Our assessment**: "Active" is undefined. The closing section's "thousands of ChatGPT and Codex users" conflicts loosely with the 130K/95K cards (internal inconsistency in scale wording; not a substantive contradiction).

### Claim 6: Leadership lesson — humans remain responsible for system design, architecture, and security; give Codex guardrails
- **Evidence**: Lam's experience statement.
- **Confidence**: anecdotal
- **Quote**: "You have to still be very responsible about your system design, your architecture, your security, and how you would like Codex to structure the code for you,"
- **Our assessment**: Standard but corroborated advice; the article explicitly states "none of this runs on autopilot."

### Claim 7: Leadership lesson — prototypes replace written specs
- **Evidence**: Shilmover's quote.
- **Confidence**: anecdotal
- **Quote**: "Normally, I put [my idea] down on paper, but now I put it down in a prototype,"
- **Our assessment**: A concrete workflow shift (prototype-as-spec) from a CIO-office technical advisor; fits spec-vs-prototype discussions.

### Claim 8: Leadership lesson — own the code or face unmaintainable output
- **Evidence**: Lam's quote; no maintainability data.
- **Confidence**: anecdotal
- **Quote**: "If you don’t work alongside Codex, you’re going to get into a situation of having lots of code that is not going to be maintainable,"
- **Our assessment**: A rare cautionary note in a marketing piece; directionally matches the maintainability-debt theme elsewhere in the corpus.

## Concrete Artifacts

```
Stat cards (source: openai.com/index/oracle, header):
98%   Decrease in the time it takes for talent acquisition research
130K  Active ChatGPT users at Oracle
95K+  Active Codex users at Oracle

Talent market intelligence tool workflow (source text paraphrase of described pipeline):
job description -> research comparable roles -> benchmark compensation
-> assess talent pool across relevant locations -> recruiter prep brief
```

## Cross-References

- **Corroborates**: `blog-openai-codex-knowledge-work.md` (Codex used by non-engineers for non-coding work); `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` (ontology/domain-model grounding for LLM data work).
- **Contradicts**: None found; no contradiction issue filed.
- **Extends**: `blog-openai-samsung-chatgpt-codex-deployment.md` (same vendor enterprise rollout genre, but Oracle supplies named-executive workflow detail Samsung lacked).
- **Novel**: Same genre as `blog-openai-atv-big-air-tour-case-study.md`, `blog-openai-1password-codex-case-study.md`, `blog-openai-asana-codex-case-study.md`, `blog-openai-bbva-banking-transformation.md`, `blog-openai-endava-frontiers.md`. New here: ontology-backed NL→SQL with Codex choosing systems to call, SRE playbook retrieval, and a "prototype instead of spec" practice.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Could cite this as another vendor-reported enterprise case study (anecdotal), mainly for the three leadership lessons (guardrails, prototypes over specs, own the code). Do not use the 98% figure as evidence of productivity gains.
- No other chapter changes recommended; evidence is too thin.

## Extraction Notes

- openai.com returns a bot challenge/403 to curl and WebFetch; the article text was read from a Wayback Machine snapshot of the same URL (full body, including quotes, was available). Quotes were copied from that snapshot.
- Page is short (~600 words); extraction covers all substantive content. No sub-pages followed.
