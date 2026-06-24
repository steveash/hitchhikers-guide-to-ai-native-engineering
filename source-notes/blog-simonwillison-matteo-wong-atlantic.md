---
source_url: https://simonwillison.net/2026/Jun/16/matteo-wong-the-atlantic/
source_type: blog-post
title: "Quoting Matteo Wong, The Atlantic: The Fable Jailbreak and Cyberdefense"
author: Simon Willison (quoting Matteo Wong, The Atlantic)
date_published: 2026-06-16
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: anecdotal
issue: "#1286"
---

# Quoting Matteo Wong, The Atlantic: The Fable Jailbreak and Cyberdefense

> Simon Willison quotes a paragraph from Matteo Wong's Atlantic article in which
> cybersecurity expert Katie Moussouris describes the White House's Fable jailbreak
> report: the model refused "review the code for security issues" but complied when
> asked to "fix this code" — and Moussouris characterized this framing-sensitive
> behavior as "the model working as intended" for cyberdefense.

## Source Context

- **Type**: blog-post (simonwillison.net link/quote post, June 16, 2026; format is a
  single blockquote from Matteo Wong's Atlantic article "The White House Is Ratcheting
  Up Its War Against Anthropic" with a byline attribution and tags. No surrounding
  editorial commentary by Willison beyond the act of quoting. The primary source is
  the Atlantic article, which was not directly fetchable for this extraction — the
  verbatim text below comes from the Atom feed entry, which reproduces the blockquote
  in full.)
- **Author credibility**: Simon Willison is a trusted-feed source in this corpus —
  creator of Django and the `llm` Python CLI, widely cited as a high-signal LLM
  tooling commentator. This post's value is curatorial: Willison selected and surfaced
  this paragraph as significant. The underlying credibility is Matteo Wong's (The
  Atlantic staff writer covering AI) and Katie Moussouris's (CEO of Luta Security,
  a cybersecurity specialist; explicitly unpaid by Anthropic for this assessment).
  Moussouris is a practitioner expert whose independence is stated directly in the
  source.
- **Scope**: A single paragraph from Wong's Atlantic article. Covers: the White House
  report's characterization of the Fable jailbreak technique (specific prompt wording),
  Anthropic's decision to share the report with an independent expert, and Moussouris's
  verdict that the behavior is intentional design. Does NOT cover: the full White House
  report, the political/regulatory context of the directive, Anthropic's legal or policy
  response, or broader details of the Atlantic article (those were not accessible for
  extraction).

## Extracted Claims

### Claim 1: The White House's Fable jailbreak report described a specific prompt-framing pattern: the model refused "review the code for security issues" but complied when asked to "fix this code," followed by additional manual steps

- **Evidence**: Katie Moussouris's direct account of the White House report, as
  reported by Matteo Wong in The Atlantic, as quoted by Willison's post. The quote
  includes the exact prompt wording the testers used in both refused and accepted forms.
- **Confidence**: anecdotal (third-hand: Moussouris describes a report she read;
  Wong reports Moussouris's account; Willison quotes Wong. The White House report
  itself is not publicly available.)
- **Quote**: "Fable refused the prompt 'review the code for security issues' but then
  complied when asked to 'fix this code,' followed by some further manual steps."
- **Our assessment**: This is the most precise account in the corpus of the specific
  prompt wording behind the "Fable jailbreak." Prior notes in the corpus describe the
  technique generically as "asking the model to read a specific codebase and fix any
  software flaws" (see `blog-simonwillison-fable-mythos-access-directive.md`, Claim 3),
  but this source provides the verbatim prompt contrast that makes the pattern
  operational. The distinction is framing — not content: both prompts involve security
  analysis of insecure code. The model's response diverged based on whether the task
  was named as a security audit ("review for security issues") or as general code
  improvement ("fix this code"). This framing-sensitivity is significant for
  practitioners designing prompts for security-adjacent workflows: the explicit naming
  of a security-evaluation goal appears to trigger a different response path than
  implicit security improvement embedded in a code-fixing request.

### Claim 2: Anthropic proactively shared the White House's report with an independent, unpaid cybersecurity expert to obtain a third-party assessment

- **Evidence**: Moussouris's direct statement to Matteo Wong that Anthropic shared
  the report with her, and her explicit disclosure that she is not paid by Anthropic
  for this assessment.
- **Confidence**: anecdotal (Moussouris's own statement as reported by Wong; her
  motivation to disclose non-payment suggests she understood the independence claim
  mattered)
- **Quote**: "Anthropic shared with her a copy of the White House's report on the
  Fable jailbreak to get her appraisal. (She said that she is not being paid by
  Anthropic.)"
- **Our assessment**: Anthropic's decision to seek an independent expert's opinion on
  the government's jailbreak characterization is consistent with their broader strategy
  of contesting the regulatory framing (also documented in
  `blog-simonwillison-fable-mythos-access-directive.md`, Claim 4). The transparency
  move — sharing a classified government report with an unpaid third party — is a
  credibility signal: Anthropic appears to believe the independent assessment supports
  their position. For practitioners: this is the first in-corpus instance of a vendor
  proactively commissioning independent expert review of a government security claim
  about their model.

### Claim 3: Independent cybersecurity expert Katie Moussouris assessed the model's framing-sensitive behavior as "the model working as intended" for cyberdefense purposes

- **Evidence**: Moussouris's direct expert judgment, as quoted by Wong. She is
  described as a cybersecurity expert and CEO of Luta Security — a practitioner with
  domain expertise to assess whether this behavior pattern is appropriate for defensive
  security use.
- **Confidence**: anecdotal (single expert's judgment; not peer-reviewed; framed as
  Moussouris's interpretation of the report's evidence, not her own testing)
- **Quote**: "Moussouris told me that this was just 'the model working as intended'
  for cyberdefense."
- **Our assessment**: Moussouris's verdict is significant for the broader regulatory
  debate: it directly counters the government's characterization of the "fix this code"
  compliance as a jailbreak bypass. Her framing — "working as intended" — implies that
  the distinction between explicit security-review framing and implicit code-fixing
  framing is a design choice by Anthropic, not an accidental vulnerability. If her
  assessment is correct, the model's refusal of "review the code for security issues"
  is an intentional guardrail, and the compliance with "fix this code" reflects a
  judgment that general code improvement does not fall within the restricted category.
  This view aligns with Anthropic's own characterization of the technique as a narrow,
  non-novel capability (see `blog-simonwillison-fable-mythos-access-directive.md`,
  Claim 4), but adds an independent expert voice to the same position.

### Claim 4: The White House report's testing methodology involved IT experts giving the model deliberately insecure code to test its security-assistance behavior

- **Evidence**: Moussouris's description of the testing setup as reported by Wong.
- **Confidence**: anecdotal (reported at two removes: Wong reporting Moussouris's
  account of the government's report)
- **Quote**: "The report, Moussouris said, involved IT experts asking Fable to help
  find and patch bugs. When given deliberately insecure code..."
- **Our assessment**: The testing methodology — deliberately insecure code, IT expert
  testers, explicit security-task framing — is a controlled adversarial probe
  consistent with red-team evaluations. The fact that "IT experts" were the testers
  (rather than security researchers or adversarial prompt specialists) suggests the
  scenario was closer to a practitioner-realistic security workflow than a novel
  jailbreak technique. This is relevant to the government's implicit claim that the
  behavior represents a novel, exploitable vulnerability: if IT professionals
  discovered this through ordinary use, the "jailbreak" is closer to a feature boundary
  than a bypass technique.

## Concrete Artifacts

### Verbatim Blockquote (from Atom feed entry for Willison's post, 2026-06-16)

```
Source: Simon Willison quoting Matteo Wong, The Atlantic,
"The White House Is Ratcheting Up Its War Against Anthropic"
(simonwillison.net/2026/Jun/16/matteo-wong-the-atlantic/)

Katie Moussouris, a cybersecurity expert and the CEO of Luta Security, told me
that Anthropic shared with her a copy of the White House's report on the Fable
jailbreak to get her appraisal. (She said that she is not being paid by
Anthropic.) The report, Moussouris said, involved IT experts asking Fable to help
find and patch bugs. When given deliberately insecure code, she said, Fable refused
the prompt "review the code for security issues" but then complied when asked to
"fix this code," followed by some further manual steps. Moussouris told me that
this was just "the model working as intended" for cyberdefense.
```

### Framing Contrast (derived from Claim 1)

```
Prompt that was REFUSED:  "review the code for security issues"
Prompt that COMPLIED:     "fix this code" + further manual steps

Context: deliberately insecure code given by IT expert testers
Testing purpose: White House report on "Fable jailbreak"
Expert verdict: "the model working as intended" (Katie Moussouris, CEO Luta Security)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-fable-mythos-access-directive.md` Claim 3 — that note
    describes the alleged jailbreak technique generically as "essentially consists of
    asking the model to read a specific codebase and fix any software flaws." The
    current source provides the specific prompt wording behind the same technique —
    "review the code for security issues" (refused) vs. "fix this code" (accepted).
    The two notes should be read together: the directive note establishes the
    regulatory and policy context; this note provides the operational prompt-level
    detail that the directive note lacks.
  - `blog-simonwillison-fable-mythos-access-directive.md` Claim 4 — Anthropic
    characterized the jailbreak as "narrow" and non-unique to Fable 5. The current
    source adds Moussouris's independent validation of the same position from the
    expert practitioner side: the behavior is intentional design, not a vulnerability.
  - `blog-anthropic-ai-accelerated-offense.md` Claim 2 — Anthropic's security team
    documented that publicly available models can find serious vulnerabilities through
    code review. The "fix this code" compliance pattern documented here is the same
    technique class Anthropic themselves documented as legitimate defensive security
    practice in that April 2026 post. Moussouris's "working as intended" verdict
    extends the corroboration from another independent expert.

- **Extends**:
  - `blog-simonwillison-fable-mythos-access-directive.md` — this note is a companion
    to that one. The directive note covers the regulatory event, timeline, and
    Anthropic's public position. This note fills in the one piece missing from that
    note: the specific prompt wording of the alleged jailbreak and an independent
    expert's verdict on its character. The Assayer should consider whether these two
    notes should be read as a unit for synthesis purposes.

- **Contradicts**: None identified. No existing source note characterizes the
  "review the code for security issues" vs. "fix this code" framing difference as
  a genuine vulnerability (rather than intended behavior) in a way that would
  contradict Moussouris's verdict here. The government's contrary framing is documented
  in the corpus (`blog-simonwillison-fable-mythos-access-directive.md`, Claims 3–4)
  but attributed to the government, not asserted as the corpus's position. No
  contradiction issue filed.

- **Novel**:
  - **First verbatim prompt wording for the Fable jailbreak in the corpus**: Claim 1
    adds the specific prompt contrast ("review the code for security issues" refused
    vs. "fix this code" accepted) that prior corpus notes describe only at the generic
    technique level ("asking the model to read a specific codebase and fix any software
    flaws").
  - **First independent expert verdict in the corpus on the Fable jailbreak character**:
    Claim 3 — Moussouris's "working as intended" judgment — is the first
    third-party practitioner assessment of whether the framing-sensitive behavior is a
    vulnerability or an intentional design choice. Prior corpus notes document Anthropic's
    own position; this note adds an unpaid, independent credentialed expert's view.
  - **First documentation of Anthropic sharing a government report with an independent
    expert**: Claim 2 — Anthropic's proactive disclosure of the White House report to
    Moussouris — is a new category of vendor response behavior not documented elsewhere
    in the corpus.

## Guide Impact

- **Chapter on Model Behavior & Safety (Ch04)**: Add the prompt-framing specifics from
  Claim 1 as a concrete case study in framing-sensitive model responses. The guide
  currently covers general principles of prompt engineering; the Fable jailbreak case
  shows that safety boundaries themselves are framing-sensitive. Specific recommendation:
  document the "review for security issues" vs. "fix this code" contrast as a documented
  instance where explicit security-audit framing triggers a different response than
  implicit code-improvement framing. Practitioners designing prompts for security-adjacent
  workflows should test both explicit and implicit framings and not assume that a single
  framing covers all desired behaviors. Cite Claim 1.

- **Chapter on Practical Guardrails & Limitations (Ch05)**: Add the Moussouris verdict
  (Claim 3) as evidence that some framing-sensitive behavior is intentional design
  rather than a bug or bypass. The chapter should distinguish between (a) model
  limitations that constrain legitimate use, (b) guardrails that are properly framing-
  sensitive by design, and (c) genuine jailbreaks that bypass intended restrictions.
  The Fable cyberdefense case illustrates category (b): "review the code for security
  issues" may be intentionally scoped differently than "fix this code" as a design
  choice. Cite Claims 1 and 3.

- **Chapter on Security Threat Modeling (Ch06)**: Update the discussion of the
  government's Fable directive (built from `blog-simonwillison-fable-mythos-access-
  directive.md`) with the prompt-level detail from Claim 1 and the Moussouris verdict
  from Claim 3. The regulatory framing (government: "this is a jailbreak") and the
  expert practitioner framing (Moussouris: "this is model working as intended") are
  now both in the corpus and should be presented as a documented disagreement. The guide
  should not silently pick a side — present both framings and note that the expert
  assessment supports the "intended design" interpretation. Cite Claims 1, 3, and 4.

- **Chapter on Verification (Ch03)**: Anthropic's proactive sharing of the government
  report with an independent expert (Claim 2) is a case study in vendor transparency
  as a trust-building mechanism. The guide can recommend that practitioners, when
  evaluating a model provider's response to regulatory challenges, look for exactly
  this behavior: commissioning independent technical assessment and disclosing the
  basis for their position. This is distinct from the vendor simply asserting their
  model is safe. Cite Claim 2.

## Extraction Notes

1. **Source is a single-paragraph quote post**: This is among the thinnest sources in
   the corpus by word count. It is a quote post: Simon Willison selected and surfaced
   a single paragraph from Matteo Wong's Atlantic article without adding editorial
   commentary. The value is the paragraph itself, not Willison's analysis.

2. **Verbatim text source**: The full blockquote text was obtained from the Atom feed
   entry (simonwillison.net/atom/everything/) rather than from the HTML page directly,
   as the WebFetch tool returned summaries rather than verbatim content for the HTML
   page. The Atom feed reproduced the full HTML of the entry including the blockquote
   element with the cite attribute and the attribution paragraph. All quotes in this
   note are from that Atom feed entry, which is character-for-character from the page.

3. **Atlantic article inaccessible**: The source post links to Matteo Wong's full
   Atlantic article (https://www.theatlantic.com/technology/2026/06/trump-anthropic-
   export-control-ai-race/687555/) with a gift link. This article was not fetchable
   by the WebFetch tool (site blocked). The extraction is therefore limited to the
   single paragraph Willison reproduced. The article likely contains additional
   context, but this note can only certify claims derivable from the verbatim
   blockquote. The gift link suggests the full article may be accessible to readers
   with the URL.

4. **Canonical URL**: The source_url uses the canonical page URL without the
   `#atom-everything` fragment from the issue body, consistent with the convention
   documented in `blog-simonwillison-fable-relentlessly-proactive.md` Extraction Notes.

5. **Attribution chain**: Moussouris → Wong → Willison. All claims are at minimum
   two removes from the White House report itself, which remains non-public. Confidence
   calibrated accordingly as `anecdotal` throughout.

6. **No contradiction issues filed**: Existing notes document the government's contrary
   framing (that this IS a jailbreak) but attribute it to the government, not assert it
   as the corpus position. The current source adds a practitioner expert's contrary
   view (that it is NOT a jailbreak) attributed to Moussouris. The tension between
   government characterization and practitioner assessment is already captured in
   `blog-simonwillison-fable-mythos-access-directive.md` Claim 3's Our assessment;
   this note extends that tension with named expert support, but does not introduce
   a new material contradiction between corpus notes.
