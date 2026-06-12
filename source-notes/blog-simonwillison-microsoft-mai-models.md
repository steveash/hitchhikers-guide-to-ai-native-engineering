---
source_url: https://simonwillison.net/2026/Jun/2/microsofts-new-models/
source_type: blog-post
title: "Microsoft's new MAI models"
author: Simon Willison
date_published: 2026-06-02
date_extracted: 2026-06-12
last_checked: 2026-06-12
status: current
confidence_overall: emerging
issue: "#1154"
---

# Microsoft's new MAI models

> Simon Willison's analysis of Microsoft's June 2026 announcement of MAI-Thinking-1 and MAI-Code-1-Flash provides the corpus's first documentation of Microsoft as an independent LLM developer and demonstrates, via self-corrections in two updates, how vendor marketing language ("enterprise grade, commercially licensed data") can diverge from what the technical paper actually describes (web crawl training on 1.2 trillion pages).

## Source Context

- **Type**: blog-post (Willison link-blog + notes format with two published corrections; includes quoted model card language, technical paper excerpts, and Willison's commentary on his own reporting failures. Published June 2, 2026.)
- **Author credibility**: Simon Willison is creator of Django and the `llm` CLI, one of the most widely-cited practitioner commentators on LLM tooling. This post is notable for its self-corrections: Willison published two updates within hours, first correcting his own misreading of MoE parameter counts, then retracting his initial acceptance of Microsoft's "commercially licensed data" claims. His public acknowledgment "I did not cover this one at all well [...] I'm sorry for not digging deeper before publishing my initial notes" adds credibility to the corrected analysis. No disclosed affiliation with Microsoft.
- **Scope**: Covers MAI-Thinking-1 and MAI-Code-1-Flash model specifications, GitHub Copilot deployment plans, Microsoft's performance claims, training data details revealed in the technical paper, and Willison's commentary on vendor claim accuracy. Does NOT cover independent benchmark evaluations, pricing, API specifications, deployment infrastructure, or fine-tuning capabilities.

## Extracted Claims

### Claim 1: Microsoft announced two new MoE text LLMs — MAI-Thinking-1 (1T total/35B active, reasoning) and MAI-Code-1-Flash (137B total/5B active, code) — marking Microsoft's debut as an independent LLM developer separate from its OpenAI partnership

- **Evidence**: Direct product announcement by Microsoft on June 2, 2026. Model specs sourced from Microsoft's model cards and technical paper as cited by Willison. Both models use Mixture-of-Experts architecture.
- **Confidence**: settled (announced product specifications from official model cards)
- **Quote**: "Microsoft announced two new text LLMs this morning - MAI-Thinking-1 (reasoning, 1T parameters, 35B active, available to "select early partners") and MAI-Code-1-Flash (137B Parameters, 5B active, "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost […] rolling out to GitHub Copilot individual users in Visual Studio Code")."
- **Our assessment**: This is the first corpus documentation of Microsoft developing LLMs independently (as distinct from hosting OpenAI models through Azure or the Microsoft/OpenAI partnership). The MoE architecture with low active-parameter ratios (35B/1T ≈ 3.5% for MAI-Thinking-1; 5B/137B ≈ 3.6% for MAI-Code-1-Flash) mirrors the DeepSeek V4 architectural approach documented in `blog-simonwillison-deepseek-v4.md`. At 35B active parameters, MAI-Thinking-1 sits in the same active-parameter range as Kimi K2.5 (32B active, see `blog-cursor-composer2-technical-report.md` Claim 1) — strong reasoning capability at a fraction of total-parameter inference cost.

### Claim 2: MAI-Code-1-Flash is being deployed directly into GitHub Copilot for individual VS Code users — Microsoft's first purpose-built coding model integrated into its own IDE tooling

- **Evidence**: Willison's quotation of Microsoft's product announcement; the explicit "individual users" framing distinguishes this from enterprise-only rollouts.
- **Confidence**: settled (official Microsoft product announcement, June 2026)
- **Quote**: "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost […] rolling out to GitHub Copilot individual users in Visual Studio Code"
- **Our assessment**: Microsoft integrating its own LLM (rather than a third-party model) into GitHub Copilot is a competitive positioning move. The "lower cost" framing for a 5B active parameter model implies Microsoft intends MAI-Code-1-Flash as a cost-optimization path for Copilot, potentially replacing or supplementing existing OpenAI/Anthropic models in the product. This has direct implications for practitioners using Copilot who assume model stability — the ongoing model substitution pattern documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4 applies here.

### Claim 3: Microsoft claims MAI-Thinking-1 "is preferred to Sonnet 4.6 in our blind human side-by-side evaluations" — the only performance comparison cited in the announcement

- **Evidence**: Direct quote from Microsoft's model card as reproduced by Willison. This is a human-preference evaluation, not a capability benchmark.
- **Confidence**: anecdotal (self-reported vendor preference evaluation; no methodology disclosed, no independent verification possible given "select early partners" access restriction)
- **Quote**: "[MAI-Thinking-1] is preferred to Sonnet 4.6 in our blind human side-by-side evaluations"
- **Our assessment**: The performance claim is notable for what it omits: no ARC-AGI, no coding benchmarks, no hallucination rates, no methodology disclosure. A single human-preference comparison against one competitor (Sonnet 4.6, not GPT-5.5 or Gemini 3.1 Pro) is the weakest possible form of performance evidence. The choice of Sonnet 4.6 as the comparison target may reflect selective favorable comparison. Practitioners evaluating MAI-Thinking-1 cannot independently verify this claim until access expands beyond "select early partners."

### Claim 4: Microsoft marketed MAI-Thinking-1 as trained on "enterprise grade, clean and commercially licensed data, without distillation from third-party models" — a claim Willison initially accepted and then retracted in Update 2

- **Evidence**: Direct quote from Microsoft's model card/announcement as reproduced by Willison. Willison acknowledged in Update 2 that he did not investigate this claim before initial publication.
- **Confidence**: anecdotal (vendor marketing claim; explicitly contradicted by technical paper details documented in Claim 5)
- **Quote**: "We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean and commercially licensed data, without distillation from third-party models."
- **Our assessment**: This claim represents vendor marketing language that did not survive technical scrutiny. Willison's Update 2 (see Claim 5) directly contradicts it by revealing the models trained on a proprietary web crawl of public internet content — the standard approach that raises the same licensing questions as every major LLM. MAI-Code-1-Flash carries a similar claim: "It is built end-to-end by Microsoft using clean and appropriately licensed data." The phrase "commercially licensed" for web crawl data is ambiguous and potentially misleading — web crawl data is generally scraped under limited crawl licenses, not licensed directly from content creators.

### Claim 5: Update 2 reveals MAI training actually used a proprietary web crawl of ~1.2 trillion pages (filtered to ~794 billion) plus ~24.2 billion Common Crawl pages — "the same licensing problems as all of the other major LLMs"

- **Evidence**: Willison quotes from Microsoft's technical paper starting at page 80. The page crawl counts and Common Crawl volume are cited directly from the paper. Willison's characterization ("same licensing problems as all of the other major LLMs") is his editorial interpretation.
- **Confidence**: emerging (technical paper citations are settled; "licensing problems" characterization is Willison's editorial judgment, not legal finding)
- **Quote**: "That technical paper describes the training data in some detail from page 80 onwards. It has the same licensing problems as all of the other major LLMs: it's trained on a crawl of the public web"
- **Our assessment**: This is the most important finding in the post for practitioners evaluating models under compliance or data-sourcing requirements. "The same licensing problems as all of the other major LLMs" is the key framing: Microsoft's training pipeline is categorically identical to industry norms despite the marketing claims. The technical paper makes this explicit: "The majority of our web HTML corpus comes from a proprietary crawl. After initial page discovery and selection, approximately 1.2 trillion pages are crawled and parsed." For compliance-focused practitioners: vendor "commercially licensed" or "appropriately licensed" training data claims require independent technical paper verification before making deployment decisions.

### Claim 6: Willison expressed preemptive skepticism about "appropriately licensed" training data before Update 2 confirmed the web crawl source

- **Evidence**: Willison's direct editorial commentary published before he obtained the technical paper details.
- **Confidence**: anecdotal (editorial skepticism that proved warranted)
- **Quote**: "I would _very much_ like to learn more about this 'appropriately licensed' data!"
- **Our assessment**: The skepticism was calibrated and warranted — Willison questioned the licensing claim without being able to refute it at time of writing, and Update 2 vindicated the skepticism. This is a useful practitioner heuristic: when vendor training data claims use vague language ("appropriately licensed," "commercially licensed," "enterprise grade"), the correct response is to consult the technical paper directly rather than accepting the marketing framing. The instinct that led Willison to question the claim before finding the technical paper is the right instinct.

### Claim 7: Willison initially misread MoE active parameter counts as total parameter counts — a common pitfall documented in a public self-correction (Update 1)

- **Evidence**: Willison's self-correction in Update 1, explicitly stating the error and its cause.
- **Confidence**: settled (Willison's own admission)
- **Quote**: "My initial published notes got the size of the models wrong. I misread Microsoft's announcements and interpreted the MoE active parameter count as the total parameter count."
- **Our assessment**: This is a practitioner warning documented by public example: MoE model announcements commonly lead with total parameter counts (for marketing impact) while active parameter counts are the inference-relevant metric. MAI-Thinking-1 has 1T total parameters but 35B active — comparable to a dense 35B model for inference cost. Practitioners evaluating model capability and cost from announcements should always distinguish total vs. active parameter counts. Willison making this mistake publicly illustrates that it is easy to miss even for experienced analysts — the distinction deserves explicit attention in any model selection framework.

### Claim 8: Willison's post provides the observation that MoE models with low active parameters are interesting given current inference costs — reframing "low parameter count" as an efficiency signal, not a limitation

- **Evidence**: Willison's editorial commentary on the 35B/5B active parameter counts.
- **Confidence**: anecdotal (practitioner editorial observation)
- **Quote**: "It's very interesting to see Microsoft releasing models with such low parameter counts, especially given how expensive larger models are to access right now."
- **Our assessment**: Willison uses "low parameter counts" to mean low *active* parameter counts after Update 1 — the 35B/5B active figures vs. the 1T/137B total. The observation is that deploying MoE models with ~35B active parameters for reasoning tasks positions MAI-Thinking-1 as cost-efficient at inference compared to dense frontier models of similar capability. This is consistent with the DeepSeek V4 architectural trend (`blog-simonwillison-deepseek-v4.md` Claims 4–5): MoE models at massive total scale with low active parameter ratios are emerging as the dominant approach for cost-effective frontier-class inference.

## Concrete Artifacts

### Model Specifications — Microsoft MAI Models (June 2, 2026)

```
MAI-Thinking-1:
  Architecture:       Mixture of Experts (MoE)
  Total parameters:   1 trillion
  Active parameters:  35 billion (~3.5% active ratio)
  Focus:              Reasoning
  Availability:       Select early partners only (not generally available at announcement)

MAI-Code-1-Flash:
  Architecture:       Mixture of Experts (MoE)
  Total parameters:   137 billion
  Active parameters:  5 billion (~3.6% active ratio)
  Focus:              Code generation (GitHub Copilot, VS Code)
  Deployment:         Rolling out to GitHub Copilot individual users in VS Code

Source: Simon Willison (citing Microsoft model cards), simonwillison.net/2026/Jun/2/microsofts-new-models/
Note: Initial reports incorrectly stated 35B/5B as total parameters; corrected in Willison's Update 1
```

### Training Data — MAI Models (from Microsoft technical paper, p. 80+, via Willison Update 2)

```
Proprietary web crawl:
  Initial crawl:    ~1.2 trillion pages
  After filtering:  ~794 billion pages

Common Crawl (after filtering and deduplication):
  ~24.2 billion pages

Filtering applied:
  - Adult content filtering
  - Piracy filtering
  - AI-generated content detection (using detection models)

Paper quote:
  "The majority of our web HTML corpus comes from a proprietary crawl.
   After initial page discovery and selection, approximately 1.2 trillion
   pages are crawled and parsed."

  "After filtering, deduplication, merging with the proprietary web corpus,
   and a final round of exact-URL and content-level fuzzy deduplication,
   the Common Crawl portion contains 24.2 billion pages."

Source: Microsoft technical paper (p. 80 onward), quoted by Simon Willison,
        simonwillison.net/2026/Jun/2/microsofts-new-models/, June 2, 2026
```

### Vendor Claims vs. Technical Paper Reality

```
Microsoft model card marketing claim (MAI-Thinking-1):
  "We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean
   and commercially licensed data, without distillation from third-party models."

Microsoft model card marketing claim (MAI-Code-1-Flash):
  "It is built end-to-end by Microsoft using clean and appropriately licensed data."

What the technical paper (p. 80+) actually describes:
  — Proprietary web crawl of ~1.2 trillion pages
  — Common Crawl contributions of ~24.2 billion pages after filtering
  — AI-generated content filtering via detection models

Willison's summary assessment:
  "It has the same licensing problems as all of the other major LLMs: it's
   trained on a crawl of the public web"

Source: Simon Willison, simonwillison.net/2026/Jun/2/microsofts-new-models/,
        June 2, 2026 (Update 2)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4.md` Claim 1: DeepSeek V4-Pro (1.6T/49B active) and MAI-Thinking-1 (1T/35B active) are both large-scale MoE models with active-parameter ratios of 3–5%. These two models together confirm a mid-2026 architectural trend: frontier-class capability at 30–50B active parameters inside 1T+ total parameter MoE architectures. Willison's observation that "low active parameter counts" are interesting given inference costs (`blog-simonwillison-deepseek-v4.md` Claim 7: "what's really notable here is the cost") applies equally to both.
  - `blog-cursor-composer2-technical-report.md` Claim 1: Kimi K2.5 (1.04T total/32B active MoE) was selected by Cursor as their Composer 2 base model over DeepSeek V3.2 and GLM-5. MAI-Thinking-1's 35B active parameter count is directly comparable to Kimi K2.5's 32B active. The convergence of three independent models (Kimi K2.5, DeepSeek V4-Pro, MAI-Thinking-1) around the 30–50B active parameter range suggests this is the current capability-efficiency sweet spot for frontier-class reasoning.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4: "Developers should design their software stacks to swap models as easily as bumping a dependency." MAI-Code-1-Flash rolling into GitHub Copilot extends this recommendation to practitioners who use Copilot as a coding tool — the underlying model in Copilot can change without notice, reinforcing the need for model-agnostic harness design.

- **Contradicts**: None identified with other source notes. The internal contradiction (vendor marketing claim vs. technical paper) is within this single source and documented in Claims 4–5 above. No prior corpus note made positive claims about Microsoft MAI training data.

- **Extends**:
  - `blog-simonwillison-gemini35-flash-pricing.md` Claims 5–6: That note documented three major labs simultaneously probing price tolerance (GPT-5.5, Opus 4.7, Gemini 3.5 Flash) in May 2026. This source adds Microsoft as a fourth LLM developer entering in June 2026. Microsoft's strategy differs: rather than pricing a premium general-purpose flagship, they deploy two purpose-built specialized models (reasoning vs. code) into owned distribution channels (GitHub Copilot/VS Code).
  - `blog-simonwillison-deepseek-v4.md` (Concrete Artifacts — Model Specifications): The DeepSeek V4 note established an MoE specification pattern (total params, active params, context length, HuggingFace size). This source adds MAI-Thinking-1 and MAI-Code-1-Flash to the growing corpus of large MoE model specifications.

- **Novel**:
  - **First corpus documentation of Microsoft as independent LLM developer**: No prior note documents Microsoft developing foundation models separate from the OpenAI partnership. MAI-Thinking-1 and MAI-Code-1-Flash are the first Microsoft-trained LLMs in the corpus.
  - **Specialized model strategy at the architecture level**: Microsoft's two-model strategy (reasoning-focused vs. code-focused) is the first documented case of a major lab releasing purpose-built specialized models rather than a single general-purpose flagship. Prior corpus model releases (GPT-5.5, Gemini 3.5 Flash, Claude Opus 4.7) are all positioned as general-purpose.
  - **Vendor "commercially licensed data" claim directly contradicted by technical paper in same announcement cycle**: This is the first corpus case where a specific vendor training data marketing claim is directly contradicted by the vendor's own technical paper, discovered within hours of initial publication. Willison's self-correction pattern (marketing claim → skeptical question → technical paper verification) is a documented practitioner research workflow.
  - **MoE total-vs-active parameter count confusion as public cautionary tale**: Willison's Update 1 self-correction documents a specific reading error (interpreting MoE active parameters as total parameters) made by an expert analyst. This is the first corpus documentation of this error type by name.

## Guide Impact

- **Chapter 05 (Model Selection and Capabilities)**: Claims 3 and 7 together establish a concrete negative example for model announcement evaluation standards. The guide should add MAI-Thinking-1 as a case study of insufficient performance evidence: a single human-preference comparison against one competitor, no benchmark methodology, and no independent verification possible due to limited access. Recommend adding: "When evaluating new model releases, require at minimum: multi-benchmark capability data (not just human preference), disclosed evaluation methodology, and comparison against the full peer set (not just one selected competitor). MAI-Thinking-1's announcement (June 2026) demonstrates what insufficient evidence looks like."

- **Chapter 10 (Responsible AI and Licensing Concerns)**: Claims 4–6 provide the clearest corpus example of vendor training data marketing language diverging from technical paper reality. Recommend adding a specific rule: "Do not rely on marketing claims like 'commercially licensed data,' 'enterprise grade data,' or 'appropriately licensed data' when evaluating a model for compliance or data-sourcing requirements. Read the technical paper directly. In the Microsoft MAI case (June 2026), marketing claimed 'commercially licensed' training while the technical paper described a proprietary web crawl of 1.2 trillion pages — categorically the same approach as every other major LLM." Cite Willison's assessment: "the same licensing problems as all of the other major LLMs."

- **Chapter 03–04 (Reasoning Models / Model Evaluation)**: Claim 1 establishes MAI-Thinking-1's architecture (1T/35B active MoE) as a new entry in the purpose-built reasoning model category alongside GPT-5.5, Claude Opus reasoning modes, and Gemini 3.1 Thinking. The 35B active parameter count at 1T total is now the third independent confirmation that the ~30–35B active parameter range is the current MoE design sweet spot for reasoning-class models. Recommend updating any model selection table to note MAI-Thinking-1 is in limited early access as of June 2026.

- **Chapter 07 (Data Practices)**: The training data metrics from the technical paper (1.2T pages crawled, 794B after filtering, 24.2B Common Crawl) document Microsoft's training data pipeline for the first time in the corpus. Notably: AI-generated content detection and filtering is now a standard preprocessing step at this scale. This is worth documenting as an emerging training data quality practice — major labs are explicitly filtering synthetic content, not just adult and piracy content.

## Extraction Notes

- Source is a link-blog-style post in Willison's standard format. The post has three distinct layers: (1) original publication, (2) Update 1 (parameter count correction), and (3) Update 2 (training data revelation + reporting acknowledgment). All three layers were read and extracted.
- WebFetch produced targeted responses rather than full verbatim reproduction; multiple targeted fetches were used to verify quotes. All `Quote` fields were confirmed via at least one targeted fetch returning identical text.
- The `#atom-everything` fragment in the original issue URL is a feed anchor; `source_url` in this note uses the canonical page URL without the fragment (consistent with other Willison source notes in this corpus, e.g., `blog-simonwillison-deepseek-v4.md` Extraction Notes).
- The Microsoft technical paper is cited by Willison (from page 80 onward) but the paper URL is not provided in the post. The training data quotes are from the paper as mediated through Willison's reporting — not independently verified against the original paper.
- No contradiction issues filed. The internal contradiction (marketing claims vs. technical paper) is within this single source, documented in Claims 4–5.
- Three Prospector triage comments were present. Comment 1 focuses on Ch03/Ch04 (architecture/model selection). Comment 2 focuses on Ch05/Ch10 (capabilities, responsible AI). Comment 3 provides the most detailed analysis and identifies Ch01, Ch02, Ch03-04, Ch05, Ch07. This extraction addresses all of these, with primary emphasis on Ch05 and Ch10 per the Prospector's second comment identifying the "key question" as vendor claims vs. reality.
