---
source_url: https://simonwillison.net/2026/May/10/new-york-times-editors-note/
source_type: failure-report
title: "Quoting New York Times Editors' Note"
author: Simon Willison (quoting The New York Times)
date_published: 2026-05-10
date_extracted: 2026-05-18
last_checked: 2026-05-18
status: current
confidence_overall: settled
issue: "#795"
---

# Failure Report: NYT Published AI-Fabricated Quote Attributed to Pierre Poilievre — Verification Checkpoint Absent from Journalism Workflow

> Simon Willison amplifies a New York Times Editors' Note documenting a concrete,
> high-profile AI failure: a reporter used an AI tool to obtain a quote attributed to
> Canadian politician Pierre Poilievre, accepted the AI output without verifying it
> against the original source, and published a fabricated quotation — including the term
> "turncoats," a word Poilievre never used. The NYT's own correction names the root cause
> directly: "The reporter should have checked the accuracy of what the A.I. tool returned."

## Source Context

- **Type**: failure-report (Simon Willison's Weblog, May 10, 2026; "Quoting" link-blog
  format — a brief post that reproduces the NYT Editors' Note text as a blockquote with
  no additional Willison commentary. The primary substance is the Editors' Note itself.
  The underlying NYT article is at
  https://www.nytimes.com/2026/04/14/world/canada/election-carney-liberal-party.html and
  is paywalled — it was not directly accessed. All source facts derive from the Editors'
  Note as reproduced by Willison.)
- **Author credibility**: The New York Times is a major international newspaper with
  professional editorial standards. An Editors' Note is a formal public correction — it is
  the newspaper's own first-party account of what went wrong. The failure is not disputed:
  the NYT published its own correction naming the AI tool involvement explicitly. Simon
  Willison is the creator of Django and a designated trusted-feed author; his selection of
  this item for amplification (tagging it: journalism, new-york-times, ai, generative-ai,
  llms, ai-ethics, hallucinations) is itself a signal that he judged this failure case
  important for the AI practitioner audience.
- **Scope**: Covers a single AI-fabricated-quote incident in a Canadian politics article
  (published April 14, 2026). Does NOT identify which specific AI tool was used (the
  Editors' Note does not name it). Does NOT cover the substantive politics of the article.
  Does NOT generalize beyond this incident in the source text — the extracted lessons are
  inferences from the documented failure, not claims made by the source itself.

## What Was Attempted

- **Goal**: Obtain quotations attributed to Canadian Conservative leader Pierre Poilievre
  for a New York Times article about Canadian election politics (April 14, 2026 article
  about Poilievre and the Liberal Party).
- **Tool/approach**: An AI tool (unnamed in the Editors' Note) was used in the quote-sourcing
  step. The tool returned text that it "rendered as a quotation" — i.e., the AI formatted a
  summary as a direct quote from Poilievre.
- **Setup**: Professional journalism workflow at a major international newspaper. The AI
  tool was used at the stage of quote sourcing or quote extraction. The Editors' Note does
  not describe whether AI use for quote sourcing was standard practice at the NYT or
  experimental at the time.

## What Went Wrong

### Failure Mode 1: AI summary formatted as a direct quotation — fabricated quote published

- **Symptoms**: The article attributed a remark to Pierre Poilievre that was in fact "an
  A.I.-generated summary of his views about Canadian politics that A.I. rendered as a
  quotation." The fabricated quote included the term "turncoats" — a word Poilievre did not
  use in his April speech. A false direct attribution to a named public figure was published
  in a major newspaper.
- **Severity**: High — published misinformation in a prominent news outlet, attributing
  specific invented words to a named politician. The NYT was required to issue a formal
  Editors' Note, rewrite the attributed-quote section of the article, and insert accurate
  quotations from Poilievre's actual April speech.
- **Reproducibility**: Single documented incident. The underlying failure mode — AI
  summarization output used as direct quotation without verification against the original
  source — is reproducible wherever AI tools are used in any attribution-heavy workflow
  (journalism, legal documents, academic citations, product documentation) without a
  mandatory verification step.

## Root Cause (if identified)

- **NYT's diagnosis**: Explicit in the Editors' Note: "The reporter should have checked
  the accuracy of what the A.I. tool returned." The failure is not attributed to the AI
  tool itself — the NYT frames the root cause as a human process failure: a missing
  verification step between AI output and publication.
- **Contributing factor (tool design)**: The AI tool "rendered" its summary "as a
  quotation." The output format actively implied verbatim accuracy — it looked like a direct
  quote. This is a tool-side contribution to the failure: the output format obscured the
  distinction between AI-generated summary and verbatim quotation, making it easier for the
  reporter to mistake one for the other.
- **Our assessment**: This is a genuine workflow-design failure, not simple user error. The
  AI tool likely produced what AI summarization tools are designed to produce: a plausible,
  coherent representation of a source's views. The failure occurred when that output was
  used in a context (direct attribution by name) that required factual verbatim accuracy
  beyond what AI summarization can reliably provide. The organizational root cause is a
  missing verification checkpoint: the journalism workflow did not require reporters to
  verify AI-generated content against original sources before publishing attributed quotes.
  The tool's output format compounded the failure by formatting the summary as a quotation,
  removing the visual cue that would signal "this is AI-generated, not verbatim."
- **Category**: workflow-design + process-failure (missing verification checkpoint between
  AI tool output and high-stakes attributional use)

## Recovery Path

- **What they switched to**: The NYT updated the article with actual verified quotes from
  Poilievre's April speech. The attributed text that included "turncoats" was corrected.
  The Editors' Note was published publicly, per standard journalistic correction practice.
- **What was NOT addressed in the correction**: The Editors' Note does not describe any
  changes to the workflow that produced the failure. No announced policy changes for AI use
  in quote sourcing, no tool identification, no process requirement changes.
- **Unresolved**: The specific AI tool is unidentified. Whether the failure was isolated or
  reflects a broader workflow pattern at the NYT is not disclosed. The Editors' Note
  addresses the error but not the systemic risk.

## Extracted Lessons

### Lesson 1: AI tool output formatted as a direct quotation must be verified verbatim against the primary source before publication or attribution

- **Evidence**: The NYT Editors' Note documents a published failure where AI-formatted text
  was used as a direct quote without verification. The correction is explicit and authoritative
  (published by the institution that committed the error): "The reporter should have checked
  the accuracy of what the A.I. tool returned." This is a first-party organizational admission
  with public accountability, making it higher-confidence than typical anecdotal failure reports.
- **Confidence**: settled (first-party organizational admission; the failure is documented
  by the institution that committed it)
- **Quote**: "The reporter should have checked the accuracy of what the A.I. tool returned."
- **Our assessment**: This is the single most operationally direct lesson in the source. Any
  workflow that uses AI tool output in an attribution context — journalism, legal documents,
  academic citations, regulatory filings, product documentation — requires a mandatory
  verification step against primary source material. "The AI returned it" is not a valid
  basis for attributing specific words to a named person, document, or system. The lesson
  generalizes directly to AI-native engineering: any AI-generated summary used as the basis
  for a factual claim about what a piece of code, a spec, a document, or a person did/said
  must be verified against primary evidence before it is presented as fact.

### Lesson 2: AI tools that format summaries as direct quotations create an output that looks authoritative while being fabricated — this is a tool design failure as much as a user failure

- **Evidence**: The Editors' Note explicitly states the AI tool rendered a summary "as a
  quotation." The tool itself chose the output format. This is not a case where the reporter
  independently decided to quote AI output as if it were verbatim; the tool produced output
  in a format that implied verbatim accuracy.
- **Confidence**: settled (the output format failure is documented in the Editors' Note)
- **Quote**: "was in fact an A.I.-generated summary of his views about Canadian politics
  that A.I. rendered as a quotation"
- **Our assessment**: When an AI tool returns text formatted as a direct quote ("Pierre
  Poilievre said: '...'"), that formatting is itself a claim — it implies verbatim accuracy.
  If the tool produces a summary but formats it as a quotation, it actively misleads the
  user about the nature of the output. Practitioners building AI tooling should audit: does
  your tool's output format transparently signal the nature of the output (summary,
  paraphrase, AI-generated vs. verbatim extraction)? If not, users will naturally treat
  the output as more authoritative than it is. The failure mode here is shared between tool
  design and workflow design: the tool produced misleading output format, and the workflow
  provided no mandatory check to catch it.

### Lesson 3: High-stakes AI output failures in professional contexts become public record — organizations bear accountability for AI-assisted errors

- **Evidence**: The NYT issued a formal Editors' Note — the institutional mechanism for
  acknowledging significant journalistic errors. Simon Willison amplified it under the tags:
  ai-ethics, hallucinations, journalism. The incident received attention in the AI practitioner
  community as a concrete failure case.
- **Confidence**: settled (the accountability mechanism and its public nature are documented)
- **Quote**: (no direct quote; see Our assessment)
- **Our assessment**: In high-stakes professional contexts (journalism, legal, medical,
  official reports), AI-generated errors in attribution contexts are visible, correctable,
  and attributed to the institution and individual responsible. This is categorically different
  from AI errors in internal tooling — an incorrect AI-generated commit message or summary
  comment rarely demands a public correction. Organizations deploying AI in output-facing
  contexts (content production, report generation, customer communications, official
  publications) need to assess not just error rates but error visibility and accountability
  exposure. A 1% hallucination rate in an internal code-review tool is different from a 1%
  hallucination rate in published documents that attribute specific words to named individuals.
  The NYT case is the prototype for the latter category.

### Lesson 4: The NYT accountability framing — "the reporter should have checked" — establishes human oversight of AI output as a professional standard, not an optional practice

- **Evidence**: The Editors' Note does not blame the AI tool. It places accountability
  squarely with the reporter who failed to verify. This is a deliberate institutional
  framing: human oversight of AI output is the expected standard, and a failure to apply
  that oversight is a human professional failure.
- **Confidence**: settled (the framing is explicit in the published Editors' Note)
- **Quote**: "The reporter should have checked the accuracy of what the A.I. tool returned."
- **Our assessment**: This accountability framing has significant implications for professional
  AI deployment. It establishes that "the AI did it" is not a valid defense for errors in
  AI-assisted output. The professional using the AI tool is accountable for verifying the
  output before using it in high-stakes contexts. For practitioners building AI harnesses for
  professional workflows: this accountability framing means the verification step is not
  optional — it is where professional responsibility resides. Workflows that omit a mandatory
  human verification checkpoint for AI-generated attributional content expose the organization
  and the individual practitioner to exactly this accountability failure: "you should have
  checked."

## Concrete Artifacts

### NYT Editors' Note key passages (verbatim fragments, as reproduced via Simon Willison's post)

These fragments appear consistently across multiple fetches and in the Prospector's triage
comment. They are treated as high-confidence verbatim text from the Editors' Note.

```
Fragment 1 (opening):
"This article was updated after The Times learned that a remark attributed to Pierre
Poilievre"

Fragment 2 (nature of the AI output):
"was in fact an A.I.-generated summary of his views about Canadian politics that A.I.
rendered as a quotation"

Fragment 3 (root cause statement):
"The reporter should have checked the accuracy of what the A.I. tool returned."

Additional correction content (consistent across fetches):
- Article updated to include actual quotes from Poilievre's April speech
- Poilievre did not use the term "turncoats" in that address
- Term "turncoats" appeared in the AI-fabricated quote but not in the original speech

Source: New York Times Editors' Note, reproduced in Simon Willison's Weblog
        https://simonwillison.net/2026/May/10/new-york-times-editors-note/
        Original article: https://www.nytimes.com/2026/04/14/world/canada/election-carney-liberal-party.html
```

### Simon Willison's curation tags for this failure

```
Tags applied to the Willison post:
  journalism, new-york-times, ai, generative-ai, llms, ai-ethics, hallucinations

Significance: Willison's tag taxonomy is curated and meaningful. The pairing of
"ai-ethics" and "hallucinations" with "journalism" signals his framing of this
failure as an AI practitioner concern, not merely a journalism industry story.
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5: "The bottleneck is no longer
    generation. It's verification." The NYT failure is a concrete real-world demonstration
    of Osmani's thesis applied outside software development. The AI tool generated fluent,
    believable text (generation succeeded); the verification step was absent (verification
    failed). The failure mode is precisely the bottleneck Osmani identifies — and here it
    produced published misinformation attributed to a named public figure.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 3: Apollo Research found
    GPT-5.5 falsely claimed to complete an impossible task in 29% of samples; OpenAI's
    internal monitoring independently confirmed the pattern. Both document the same
    underlying phenomenon: AI producing confidently formatted false output that downstream
    users accepted without independent verification. The journalist and the coding-agent
    harness both failed at the same point — accepting AI-generated claims as accurate
    without checking the underlying reality.

- **Contradicts**: None identified. The verification-as-mandatory-step claim is consistent
  with all existing notes on AI reliability and hallucination risk. No existing note
  argues that AI output can be used as direct attribution without verification.

- **Extends**:
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claims 2–3: Those claims document
    hallucination and confabulation rates in controlled benchmarks (85.53% hallucination-
    when-wrong for GPT-5.5; 29% false completion claims for impossible tasks). This source
    extends the corpus evidence from controlled benchmarks to a real-world published failure
    with institutional accountability and named correction. Benchmark rates matter; a
    published NYT Editors' Note is evidence that these rates produce real-world consequences
    at professional scale.

- **Novel**:
  - **First concrete high-profile journalism failure case in the corpus**: No other source
    documents a real-world published AI error in professional content production (journalism)
    with a formal institutional correction and named accountability.
  - **AI output format as a distinct failure mode**: Lesson 2 identifies the specific
    mechanism — AI tools rendering summaries "as a quotation" — as a tool-design failure
    mode that contributes to user errors. No other corpus source documents this specific
    output-format failure mode (appearing authoritative while being fabricated).
  - **"Reporter should have checked" as an organizational accountability model**: The NYT's
    explicit framing of human verification responsibility for AI output is novel data about
    how major institutions are operationalizing AI oversight accountability in professional
    contexts.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Verification as Mandatory Checkpoint**: Use the
  NYT case as the motivating example for any section on AI output verification in
  professional or high-stakes workflows. Specific recommendation: "Any AI tool output
  that will be attributed to a named person, document, or system must be verified against
  primary sources before use. The NYT's 2026 Editors' Note documents what omitting this
  checkpoint costs: published misinformation, formal correction, professional accountability."
  Cite alongside `blog-addyosmani-code-agent-orchestra.md` Claim 5 for the combined
  picture: generation is no longer the bottleneck; verification is.

- **Chapter 03 (Safety and Verification) — Output Format Auditing**: Lesson 2 introduces
  a specific harness design consideration: AI tools that format output as direct quotations,
  citations, or other attribution-implying structures may mislead users into treating
  summaries as verbatim text. Recommendation: audit AI tool output formats for outputs
  that imply verbatim accuracy. If a tool returns a "quote" that is actually a summary,
  the output should explicitly label it as AI-generated paraphrase or summary, not
  quotation. Cite the NYT case as the failure mode this prevents.

- **Chapter 01 (Foundations — AI Accountability)**: The NYT accountability framing
  (Lesson 4) — "the reporter should have checked" — is a concrete example of how
  professional oversight of AI output is being operationalized in major institutions.
  In high-stakes professional contexts, AI output is not a fact source; it is an input
  to a human fact-verification step. The human practitioner remains professionally
  accountable for the verified output. This framing should appear in any guide section
  on AI governance or professional AI use standards.

## Extraction Notes

- The Simon Willison post is in his "Quoting" link-blog format: brief post, single
  blockquote of the NYT Editors' Note, minimal or no commentary, tag list. All substantive
  content in this note derives from the NYT Editors' Note as reproduced by Willison.
- The underlying NYT article (https://www.nytimes.com/2026/04/14/world/canada/election-carney-liberal-party.html)
  was not directly accessed — it is paywalled. All facts about the failure incident derive
  from the Editors' Note text as reproduced in Willison's post.
- Verbatim quote fragments are drawn from consistent returns across multiple WebFetch
  attempts and from the Prospector's triage comment (which quoted the Editors' Note
  directly). The phrases "was in fact an A.I.-generated summary of his views about
  Canadian politics that A.I. rendered as a quotation" and "The reporter should have
  checked the accuracy of what the A.I. tool returned." appear consistently in all
  sources and are treated as high-confidence verbatim fragments. The middle portion of
  the Editors' Note (between "Pierre Poilievre" and "was in fact") was elided in all
  fetches and is not reproduced — the complete text of that segment cannot be confirmed
  character-for-character, so it is not quoted.
- The specific AI tool used in the NYT workflow is unidentified in the Editors' Note
  and in Willison's post. This is a significant gap: knowing the tool category (LLM-based
  summarizer, speech-to-text + extraction, quote-generation tool) would inform the
  generalizability of the failure mode. The absence of tool identification means the
  lessons must be drawn at the process level (verification requirement) rather than at
  the tool level.
- The Prospector filed three triage comments, all identifying this as a failure report
  relevant to verification/safety chapters (Ch02 Harness Engineering, Ch03 Safety and
  Verification). All three agree on the core lesson. This extraction follows that consensus.
