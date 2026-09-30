---
source_url: https://openai.com/index/building-standards-next-phase-ai
source_type: blog-post
title: "Building standards for the next phase of AI"
author: OpenAI (Global Affairs; no individual byline)
date_published: 2026-09-21
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: anecdotal
issue: "#3806"
---

# Building standards for the next phase of AI

> OpenAI's institutional policy proposal that the United States lead development of international technical standards for frontier AI (evaluation, human oversight of automated AI research, incident reporting), framed around the risks of recursive self-improvement (RSI); it is a position statement with no empirical data.

## Source Context

- **Type**: blog-post (OpenAI Global Affairs policy statement, published 2026-09-21 per the openai-news RSS feed).
- **Author credibility**: Institutional voice of a frontier lab and a party with a direct interest in how standards are written. It states positions and proposals, not measurements. The post itself says "any AI lab that pursues automated AI research or other advanced capabilities must take accountability for doing so safely".
- **Scope**: Covers the RSI framing, the case for international standards (three problems), and a two-part proposal (a standard-setting mechanism; common measurements and incident-reporting protocols), plus a geopolitical argument for US leadership. It does not give concrete thresholds, evaluation designs, or a timeline, and says the concept is expected to "evolve substantially over time". It says little about coding agents or SDLC practice.

## Extracted Claims

### Claim 1: Fully autonomous RSI is not happening today and should not be pursued until it can be done safely, while automated AI research with human supervision is presented as beneficial.
- **Evidence**: Assertion by OpenAI; no data in this post (it links to a separate research-acceleration report).
- **Confidence**: anecdotal
- **Quote**: "Fully autonomous RSI is not happening today, and we should not pursue it unless and until it can be done safely."
- **Our assessment**: Consistent with the lab's other statements. The guide should treat this as a stated norm, not a verified state of the world.

### Claim 2: RSI risk is that humans lose practical oversight of research processes they no longer understand.
- **Evidence**: Reasoned argument; cites the Hugging Face incident as a "preview" of the risks, while noting it was not a direct result of RSI.
- **Confidence**: anecdotal
- **Quote**: "Done without appropriate care and caution, RSI could result in humans losing practical control over AI development, unable to provide oversight on research processes they no longer understand."
- **Our assessment**: The oversight-comprehension framing is the useful part: it parallels the guide's verification themes (reviewers must keep pace with agent output). The incident linkage is only illustrative.

### Claim 3: Standards define what good evidence and safeguard rigor look like for catastrophic-risk mitigation.
- **Evidence**: Argument by analogy to aviation and financial stability.
- **Confidence**: anecdotal
- **Quote**: "Standards can create shared definitions of high-quality evidence and agreed-upon baselines for the rigor of technical safeguards."
- **Our assessment**: Reasonable, but the post specifies no standard content. Useful only as a signal of which standard-setting axes a major lab wants.

### Claim 4: Three problems justify international (rather than purely national) standards: fragmentation, collective action, and uneven capacity.
- **Evidence**: Argument only.
- **Confidence**: anecdotal
- **Quote**: "Fragmentation—Evaluations, reporting requirements, and incident definitions by different nations could conflict, making it harder to compare evidence, understand emerging capabilities, and respond to risks that cross borders."
- **Our assessment**: The fragmentation point (incompatible incident definitions and evaluations) is concrete and plausible. Our assessment of the other two: they are standard collective-action arguments without evidence.

### Claim 5: Proposed mechanism: leverage the network of AI safety institutes, via CAISI and national industry bodies, focused on frontier models (defined by capability benchmarks) and benefit-risk management of automated AI research.
- **Evidence**: Proposal listing existing institutes (Australia, Canada, Germany, France, Kenya, Japan, Korea, Singapore, India, UK) and the International Network for Advanced AI Measurement, Evaluation, and Science.
- **Confidence**: anecdotal
- **Quote**: "One way of accomplishing this would be to leverage the emerging network of AI safety institutes"
- **Our assessment**: A proposal by an interested party; no commitments from those institutes are cited.

### Claim 6: The standards are explicitly not licensing, prerelease review, or approval regimes; national governments decide whether to adopt them.
- **Evidence**: Stated design constraint.
- **Confidence**: anecdotal
- **Quote**: "These technical standards would not be licenses, mandatory prerelease review, or approval requirements for AI models."
- **Our assessment**: Notable contrast with the "mandatory, capability-based national AI safety regulation" OpenAI describes in blog-openai-ai-policy-window (Claim 2). It is not a contradiction: this concerns international technical standards while the other concerns national regulation. It is worth noting the layering.

### Claim 7: Standards should avoid disadvantaging new entrants and open-weight developers, and challenges apply to both open and closed models.
- **Evidence**: Stated principle; no mechanism.
- **Confidence**: anecdotal
- **Quote**: "Common standards should be developed transparently and designed so that they do not advantage particular companies, countries, or business models, including by making it harder for new entrants or open-weight developers to compete."
- **Our assessment**: Relevant to the standards-capture risk. Unverifiable as a commitment.

### Claim 8: Part 2 lists three standardization targets: RSI-relevant evaluation, human oversight triggers, and incident classification/reporting.
- **Evidence**: Cites two OpenAI artifacts as "initial contributions": the research-acceleration report and the misalignment reporting framework.
- **Confidence**: anecdotal
- **Quote**: "Human oversight over automated AI research, including what kinds of automated AI research processes should trigger immediate human review."
- **Our assessment**: The most concrete portion. "What should trigger immediate human review" is an unsolved design question relevant to agent harness approval gates. The same list includes "common incident severity levels and reporting thresholds".

### Claim 9: The post argues the US should lead, so it shapes the global framework rather than facing a fragmented system.
- **Evidence**: Geopolitical argument (US position in finance, trade, defense, technology).
- **Confidence**: anecdotal
- **Quote**: "That is why we believe the United States should lead an effort to work together with countries around the world to develop global technical standards for frontier AI, including for RSI."
- **Our assessment**: Advocacy. Low relevance to engineering practice; useful context for how the lab positions itself.

### Claim 10: Pacing is defined as keeping alignment research and its deployment ahead of capabilities, not a fixed speed.
- **Evidence**: Definition offered by the post.
- **Confidence**: anecdotal
- **Quote**: "Pacing AI development is not about maintaining a predetermined speed. Technically, it is about ensuring that alignment research and deployment of that research stay ahead of capabilities."
- **Our assessment**: A clarifying definition that complements the earlier "pacing" posts.

## Concrete Artifacts

No code, configs, or metrics are in the source. The proposal's structure, quoted from the post's headings and list:

```
Source: OpenAI, "Building standards for the next phase of AI" (2026-09-21)

Problems: Fragmentation / Collective action / Uneven capacity
(1) A mechanism that facilitates complementary national and international frontier standards
(2) Common measurements and incident reporting protocols for better collective action
    - Evaluation of RSI-relevant AI progress ...
    - Human oversight over automated AI research ...
    - Incident classification, tracking, reporting, and responding ...
Named partner bodies: CAISI, ISO, Frontier Model Forum, Agentic AI Foundation,
Open Secure AI Alliance, Appia Foundation
```

## Cross-References

- **Corroborates**: blog-openai-ai-policy-window (Claim 10, RSI "is not happening today"; Claim 9, framework for reporting consequential misalignment incidents); blog-openai-built-to-benefit-everyone (Claim 5, long-held belief in an international coordinating organization; Claim 3, the three main goals reused here); blog-openai-model-misalignment-reporting-framework (Claim 7, the reporting-mechanism framing, which this post cites as an "early contribution").
- **Contradicts**: None found. Standards being non-mandatory (Claim 6 here) differs in scope from the national "mandatory, capability-based" regulation ask in blog-openai-ai-policy-window (Claim 2); this is a difference of layer, not a contradiction, so no issue was filed.
- **Extends**: blog-latentspace-ainews-aef1-third-party-evaluators (Claims 1 and 3 cover AEF-1 and embedded evaluators; this post is a different, government-facing standards route, and does not mention AEF-1 in the readable text); blog-openai-hf-incident-road-ahead (cited here as a "preview" of risk); blog-openai-pacing-model-development-cyber-capabilities; blog-simonwillison-research-acceleration-view-inside-openai (the report this post cites as an initial contribution, Claim 3).
- **Novel**: The three-part case for international standards (fragmentation, collective action, uneven capacity); the explicit "not licenses" framing; the proposal to standardize oversight-trigger criteria and cross-lab incident severity levels.

## Guide Impact

- **Chapter 03 (Verification)**: Optional note that a lab is publicly calling for standard incident severity levels, reporting thresholds, and human-review triggers for automated research; use as context, not as a practice. No specific evidence to change existing advice.
- **Chapter 06 (Organizational challenges)**: Could cite this as an example of the governance direction (standards bodies, incident taxonomies) that organizations adopting agents may eventually be measured against. Label as an anecdotal, interested-party position.
- **Chapters 01, 02**: No change recommended; the source has no engineering-practice content.

## Extraction Notes

- The OpenAI page returned HTTP 403 to direct fetch and WebFetch. The full article text was retrieved through the r.jina.ai reader proxy (about 1,650 words, complete through the final paragraph); the quotes were copied from that text. The Assayer may see a 403 if spot-checking directly.
- Linked posts (Altman, Pachocki, HF incident, misalignment framework, research acceleration) were not re-fetched; existing source notes cover them.
- The triage comment suggested comparing with AEF-1; the readable text does not mention AEF-1.
- Source is thin on engineering content; a short claim count reflects a short policy essay, not shallow reading.
