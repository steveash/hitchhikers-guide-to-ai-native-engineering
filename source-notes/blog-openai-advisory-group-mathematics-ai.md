---
source_url: https://openai.com/index/advisory-group-on-mathematics-and-ai
source_type: blog-post
title: "Advisory Group on Mathematics and Artificial Intelligence"
author: OpenAI
date_published: 2026-09-21
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: emerging
issue: "#3833"
---

# Advisory Group on Mathematics and Artificial Intelligence

> OpenAI announces an independent, unpaid, publicly-voiced external advisory group of nine senior mathematicians (hosted at the Institute for Advanced Study) to advise on reviewing and communicating its AI-produced math results, while explicitly carving out advice on how fast OpenAI paces its own internal progress; it also adds new headline figures (100+ open problems resolved by a model whose training began August 28).

## Source Context

- **Type**: blog-post (openai.com/index, "Company" category, September 21, 2026, author "OpenAI"). A short announcement (~450 words plus a member list).
- **Author credibility**: First-party announcement from OpenAI. It is the primary source for the group's charter, but it is self-reported: the group's independence and any advice it gives cannot be verified from this post alone.
- **Scope**: Covers the motivation (rapid math progress, a mathematicians' open letter), the group's remit, its independence terms, and initial membership. It does not give the problem list, methodology, charter document, meeting cadence, or any concrete advice yet issued.

## Extracted Claims

### Claim 1: The internal model whose training began August 28 has now resolved more than 100 long-standing open problems across most areas of mathematics, in addition to Navier–Stokes
- **Evidence**: Self-reported by OpenAI; no list, paper, or Lean artifacts are linked in the text of this post (only a link labelled "pace of its progress").
- **Confidence**: anecdotal
- **Quote**: "On August 28, we began training a new internal model. In addition to resolving the Navier–Stokes Millennium Prize problem"
- **Our assessment**: Notable as a quantity update: the corpus's earlier notes cover 10 problems (Willison note) plus Navier–Stokes. The ">100" figure is unverified here and we should not treat it as established until problems are enumerated and formalizations are published. The same post says the model "has now resolved more than 100 long-standing open problems across most areas of mathematics."

### Claim 2: OpenAI says the pace surprised even its own in-house mathematicians, which prompted internal discussion about how to inform the community and "prepare and adapt the field"
- **Evidence**: Authority/self-report only.
- **Confidence**: anecdotal
- **Quote**: "The pace of its progress"
- **Our assessment**: The quote above is only the fragment visible as link text; the fuller sentence in the post is "The pace of its progress in mathematics has surprised the mathematicians within OpenAI." A capability-surprise-then-communication-planning sequence is a process pattern worth tracking: the lab's response to rapid capability gain is a communication/stakeholder structure, not a slowdown.

### Claim 3: OpenAI treats external criticism (an open letter by mathematicians, "A Severe Misalignment of AI in Mathematics") as the trigger for creating the group
- **Evidence**: The post cites the letter as raising "concerns about the negative externalities of solving open problems as a benchmark for new AI systems"; the letter's contents are not reproduced and we did not read it.
- **Confidence**: emerging
- **Quote**: "Their criticisms highlight the need for thoughtful engagement of AI companies with the math community."
- **Our assessment**: Useful as a concrete example of using open problems as a capability benchmark drawing domain-community pushback, and a lab responding with institutional structure. We have not verified the letter; a follow-up source on it would be high value.

### Claim 4: The group's remit is review and communication of emerging results, assessing significance, coordinating dissemination, professional/academic standards, and how tools can support math research and learning
- **Evidence**: Stated charter in the post; no formal charter document linked.
- **Confidence**: emerging
- **Quote**: "The group will advise on the review and communication of emerging results: they will help OpenAI assess their significance, advise on how to coordinate their dissemination, and advise on academic and professional standards of mathematical research."
- **Our assessment**: This is external expert review of AI-generated results *before/at* publication, in a domain (math) where results are formally checkable. It complements the formal-verification emphasis in existing notes (Lean, Comparator) by adding a human-community legitimacy layer.

### Claim 5: Independence is operationalized through specific terms: freedom to give unsolicited advice, comment publicly on OpenAI's impact, publish its advice, no payment from OpenAI, and self-determined membership
- **Evidence**: Terms stated in the post; unverifiable externally. Hosting at the Institute for Advanced Study is stated in the member-list heading.
- **Confidence**: emerging
- **Quote**: "The group will have the freedom to offer advice we have not requested, comment on OpenAI’s impact on mathematics, and make its advice public."
- **Our assessment**: A reasonably specific independence checklist (unsolicited advice, public voice, unpaid, self-selecting membership) that can be reused as a rubric for evaluating any lab's "external advisory" claims. Note the structural limit: OpenAI chose/convened the initial members.

### Claim 6: The group is explicitly excluded from advising on the pace of OpenAI's internal progress in mathematics
- **Evidence**: Stated limitation.
- **Confidence**: settled (as a statement of what the post says)
- **Quote**: "Importantly, the group will not be responsible for advising us on how to pace our internal progress on mathematics."
- **Our assessment**: The most analytically important sentence. Oversight is scoped to downstream communication and community impact, not to whether/how fast to push capability. This contrasts with the "pacing" language in OpenAI's other recent posts (see Cross-References), where pacing is treated as an internal safety/alignment matter.

### Claim 7: OpenAI frames responsible broader deployment of math-related capabilities as still being worked out, and describes the advisory group as "a first step"
- **Evidence**: Self-report; no deployment plan given.
- **Confidence**: anecdotal
- **Quote**: "We recognize this and are working through how broader deployment of math-related AI capabilities can be done responsibly."
- **Our assessment**: Signals that math capabilities are not yet broadly deployed and that no policy exists yet. Low evidentiary value; useful as a dated marker of OpenAI's stated position.

### Claim 8: OpenAI states a goal of putting capable tools in mathematicians' hands so they can pursue questions of their choosing
- **Evidence**: Stated aspiration only.
- **Confidence**: anecdotal
- **Quote**: "We want to put capable tools in mathematicians’ hands so they can pursue the questions they know best and develop new ideas."
- **Our assessment**: Consistent with the human-AI "big mathematics" framing in the Willison/Tao note, but here it is a one-sentence intent with no product, access, or pricing details.

## Concrete Artifacts

Initial members as listed in the post (hosted at the Institute for Advanced Study); affiliations as given:

```
François Charles (ENS-PSL)
Camillo De Lellis (IAS, GSSI)
Timothy Gowers (Collège de France, Cambridge)
Martin Hairer (EPFL, Imperial College London)
Nikhil Srivastava (Berkeley, Simons [Institute])
Ulrike Tillmann (Oxford, INI)
Ravi Vakil (Stanford)
Edward Witten (IAS)
Melanie Matchett Wood (Harvard)
-- Source: openai.com/index/advisory-group-on-mathematics-and-ai (the post's own spelling of the Simons affiliation contains a typo; corrected in brackets here)
```

Independence terms (condensed from the post): unsolicited advice permitted; may comment publicly on OpenAI's impact; may publish its advice; members unpaid by OpenAI; membership self-determined; excluded from advising on internal pacing.

## Cross-References

- **Corroborates**: `blog-openai-navier-stokes-solution.md` Claim 2 (internal model training began August 28, 2026) — this post repeats the August 28 date and Navier–Stokes resolution. `blog-openai-work-now-within-reach.md` Claim 6 (Navier–Stokes cited as evidence of scientific-discovery capability).
- **Contradicts**: None filed. Not a contradiction, but a scoping contrast: `blog-openai-pacing-model-development-cyber-capabilities.md` Claim 1 describes OpenAI slowing frontier scaling for cyber-capability reasons, whereas this post excludes pace-setting from the math advisory group's remit. These are different domains and different mechanisms, so we treat it as conditioning, not a contradiction.
- **Extends**: `blog-simonwillison-ten-advances-mathematics.md` (Claims 1, 5–7: ten problems, Comparator proof checking, Tao's "big mathematics" and formal verification) — adds a community-governance layer and the ">100 problems" update. `blog-openai-building-standards-next-phase-ai.md` Claim 3 (standards define what good evidence looks like) — this is a domain-specific, community-run analogue at the lab level rather than the international-standards level.
- **Novel**: The first source in the corpus describing a named, unpaid, publicly-voiced external domain-expert advisory body for a lab's AI-discovery results; the "not responsible for pacing" scope carve-out; and the existence of the mathematicians' open letter "A Severe Misalignment of AI in Mathematics" (not yet in corpus).

## Guide Impact

- **Chapter 05 (Team Adoption) / governance material**: Add the independence-terms checklist (unsolicited advice, public voice, unpaid, self-selecting membership, explicit scope exclusions) as an example for evaluating external review bodies. Cite Claims 5 and 6; flag as self-reported.
- **Chapter 03 (verification)**: Where Lean/Comparator formal verification is discussed (via the Willison note), note that OpenAI is pairing machine verification with human-community review for significance and dissemination (Claim 4). Low-to-moderate priority.
- **No change recommended** to Chapter 04 context-engineering content; the triage's suggestion of relevance there was not borne out by the text.

## Extraction Notes

- The openai.com URL returns HTTP 403 (Cloudflare) to direct fetches, so the full text was read from a Wayback Machine copy of the same URL; the RSS feed entry confirms the publication date. The article is short and was read in full; no sub-pages were followed. The linked open letter and the advisory group page were not fetched.
- The page shows "Loading…" in place of an embedded element beneath the title, so some page media may be missing. Claim 2's quote is a link-text fragment; the fuller sentence is provided in the assessment.
- Several quotes use the curly apostrophe as published.
