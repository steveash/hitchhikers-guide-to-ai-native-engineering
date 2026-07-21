---
source_url: https://simonwillison.net/2026/Jul/16/bad-codex-bug/
source_type: failure-report
title: "A quote from Thibault Sottiaux"
author: Simon Willison (quoting Thibault Sottiaux)
date_published: 2026-07-16
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: anecdotal
issue: "#2089"
---

# A quote from Thibault Sottiaux

> Simon Willison republishes a short tweet from Thibault Sottiaux describing the
> conditions under which GPT-5.6 Codex has unexpectedly deleted files: full
> access mode with no sandboxing and no auto-review enabled, combined with the
> model attempting to redefine `$HOME` as a temporary directory and then
> mistakenly deleting `$HOME` itself.

## Source Context

- **Type**: failure-report (as a link-blog "quotation" post) / blog-post. This is
  one of Simon Willison's "quotation" posts — a format on his blog consisting of a
  single blockquote with attribution and minimal or no original commentary. The
  entire page is: a dateline, one blockquote (three sentences plus a three-item
  bulleted list), and a one-line attribution/context caption. There is no
  surrounding analysis from Willison himself beyond the caption.
- **Author credibility**: The quoted content is attributed to Thibault Sottiaux
  (X/Twitter handle `@thsottiaux`, tweet ID `2077630111499882637`), not to Simon
  Willison. The post itself does not state Sottiaux's affiliation or role, and
  this extraction did not independently confirm it (the linked tweet requires an
  X/Twitter login to view in full; only the og:description metadata, matching the
  blockquote text, was retrievable). The Prospector's triage comments describe him
  as "appearing to be from OpenAI/Codex team" — this is the Prospector's
  inference, not a fact confirmed by the source page, and should be treated as
  unverified. What lends the quote some weight regardless of confirmed
  affiliation: the first-person plural framing ("We've investigated a handful of
  reports...") implies the author had some investigative role in looking at these
  reports, and Simon Willison — an independent, highly-cited, vendor-neutral LLM
  tooling commentator who has no reason to amplify a fabricated vendor-side claim
  — chose to feature it. Willison's own credibility (creator of Django, the `llm`
  CLI, and one of the most widely cross-referenced sources in this corpus) is
  around the *curation* decision (this is a bug worth knowing about), not around
  the *technical content* of the claim itself, which he did not independently
  verify or elaborate on.
- **Scope**: The post covers exactly one narrow failure pattern in "GPT-5.6" (a
  Codex-branded model/product tier) — accidental file deletion under three
  specific conjunctive conditions. It does not cover: how many total incidents
  were reported ("a handful"), whether the bug has been fixed or is still live at
  time of publication, what percentage of full-access/no-sandbox sessions
  actually trigger this, or any technical detail of Codex's temp-directory
  handling code beyond the tweet's three-bullet summary. It also does not
  describe the recovery/remediation process for affected users (contrast with
  `blog-simonwillison-datasette-blog-codex-session.md` Claim 5, where the same
  failure category — a Codex product deleting content it shouldn't — is
  documented with a full recovery narrative).

## Extracted Claims

### Claim 1: GPT-5.6 file-deletion incidents most commonly occur when full access mode is enabled and Codex is run without sandboxing protections, including without auto-review enabled

- **Evidence**: Stated as the lead finding of a stated investigation ("a handful
  of reports") into unexpected file deletions, framed as the first and primary
  precondition in a three-item bulleted list.
- **Confidence**: anecdotal (self-reported investigation of an unspecified small
  number of incidents — "a handful of reports" — with no case count, no published
  incident report, and no independent verification available from this source)
- **Quote**: "Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled"
- **Our assessment**: This is a conjunctive, not a sufficient, condition — the
  quote frames it as the situation in which the bug "most commonly occurs," not a
  guarantee that it always occurs under these conditions or never occurs
  otherwise. Read narrowly, it is consistent with (not novel beyond) the corpus's
  existing position that full-access/no-sandbox configurations are the highest-risk
  posture for coding agents: it adds a second, distinct concrete failure case
  (accidental destructive file deletion via environment-variable confusion) to
  that position, alongside the credential-exfiltration and hook-execution-ordering
  failures already documented in `blog-anthropic-how-contain-claude.md` (Claims 10
  and 11) and the untracked-directory deletion documented in
  `blog-simonwillison-datasette-blog-codex-session.md` (Claim 5). "Auto review" is
  independently confirmed to be a real, named Codex configuration surface — the
  Codex system-prompt corpus documented in `blog-simonwillison-codex-base-instructions.md`
  (Source Context / Concrete Artifacts) lists `codex-auto-review` as one of six
  named model-tier entries in OpenAI's public `models.json`, corroborating that
  "auto review" is a genuine, named Codex product control rather than a term
  Sottiaux coined loosely for this quote.

### Claim 2: The proximate technical trigger for the deletions is the model attempting to override the `$HOME` environment variable to define a temporary directory

- **Evidence**: Second bullet in the blockquote's three-item list.
- **Confidence**: anecdotal (single-source technical description of the failure
  mechanism, not independently reproduced or confirmed in this extraction)
- **Quote**: "The model attempts to override the $HOME env var to define a temporary directory."
- **Our assessment**: This names a specific, plausible engineering root cause:
  rather than using a dedicated temp-directory API or `$TMPDIR`, the model's
  reasoning path apparently involves repointing `$HOME` itself to a scratch
  location — a legitimate-seeming shortcut that is actually rewriting a
  high-blast-radius variable. This is a distinct failure mechanism from every
  other Codex/coding-agent deletion incident already in the corpus: it is not a
  misclassification of untracked content as disposable (the mechanism in
  `blog-simonwillison-datasette-blog-codex-session.md` Claim 5), and it is not a
  configuration-ordering vulnerability (the pre-trust hook execution issue in
  `blog-anthropic-how-contain-claude.md` Claim 10). It is a case of the model
  choosing an unsafe means to a benign end.

### Claim 3: The model's deletion of `$HOME` (instead of the intended temporary directory) is characterized as an honest mistake, not adversarial or malicious behavior

- **Evidence**: Third bullet in the blockquote's three-item list, explicitly
  using the phrase "honest mistake."
- **Confidence**: anecdotal (characterization by the (unverified) author of the
  tweet, not an independently audited root-cause finding)
- **Quote**: "The model makes an honest mistake and mistakenly deletes $HOME instead."
- **Our assessment**: This framing places the incident in the "model misbehavior"
  category of Anthropic's three-category agent risk taxonomy (user misuse / model
  misbehavior / external attackers) documented in `blog-anthropic-how-contain-claude.md`
  Claim 1 — the model is not being attacked via prompt injection and the user is
  not intentionally causing harm; the model itself takes an unexpected,
  destructive path while pursuing a benign-looking sub-goal (creating a temp
  directory). That containment article's Claim 3 — that model-layer defenses
  "will never be 100% effective" and environmental controls must be the primary
  backstop — is exactly the argument this incident supports empirically, in a
  different vendor's product: an "honest," non-adversarial model action was still
  destructive because there was no environmental boundary (sandboxing, restricted
  filesystem access) stopping it from acting on `$HOME`.

### Claim 4: This finding is based on investigation of "a handful of reports," not a systematic study, audit, or public incident postmortem

- **Evidence**: Opening clause of the blockquote, preceding the three-item list.
- **Confidence**: anecdotal (the author's own framing states the evidentiary base
  explicitly, and it is small and imprecise)
- **Quote**: "On file deletions. We've investigated a handful of reports where GPT-5.6 unexpectedly deleted files."
- **Our assessment**: "A handful" is deliberately imprecise — it could mean
  anywhere from three to a dozen or more reports, and no rate (reports per active
  user, or per session) is given, so this cannot be used to estimate how common
  the failure actually is in the field. This distinguishes the source sharply from
  higher-rigor incident data already in the corpus, such as the specific 24-of-25
  phishing-test success rate and named internal metrics in
  `blog-anthropic-how-contain-claude.md` (Claims 11, 6, 7). This source should be
  cited in the guide as a qualitative confirmation that the failure mode exists
  and recurs, not as evidence of its frequency or severity relative to other
  agent failure modes.

### Claim 5: Simon Willison selected and republished this quote with the framing "a pretty gnarly Codex bug," signaling practitioner-relevant notability independent of the tweet's own evidentiary weight

- **Evidence**: The post's caption line, which is the only original text Willison
  contributes to the page.
- **Confidence**: anecdotal (an editorial/curation judgment, not a technical claim)
- **Quote**: "describing a pretty gnarly Codex bug"
- **Our assessment**: Willison's link-blog format (documented previously in
  `blog-simonwillison-codex-base-instructions.md` Source Context and
  `blog-simonwillison-datasette-blog-codex-session.md` Claim 9) routinely surfaces
  items with minimal editorializing — the value of a Willison "quotation" post is
  almost entirely in the curation signal (he read many things and picked this one)
  rather than in original analysis. "Gnarly" is Willison's own characterization,
  and its practical implication is that this bug is unusual or severe enough to be
  worth a reader's attention, even though the post supplies no further technical
  detail beyond the quoted tweet.

## Concrete Artifacts

### Full blockquote (verbatim, from page HTML)

```html
<blockquote cite="https://twitter.com/thsottiaux/status/2077630111499882637">
<p>On file deletions. We've investigated a handful of reports where GPT-5.6 unexpectedly deleted files.</p>
<p>What we have  found is that this most commonly occurs when:</p>
<ul>
<li>Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled</li>
<li>The model attempts  to override the $HOME env var to define a temporary directory.</li>
<li>The model makes an honest mistake and mistakenly deletes $HOME instead.</li>
</ul>
</blockquote>
<p class="cite">— <a href="https://twitter.com/thsottiaux/status/2077630111499882637">Thibault Sottiaux</a>, <span class="context">describing a pretty gnarly Codex bug</span></p>
```

*Source: page HTML at https://simonwillison.net/2026/Jul/16/bad-codex-bug/, retrieved 2026-07-21.
Double-spacing after "have" and "attempts" in the source paragraphs is preserved verbatim
from the live page markup — likely an authoring artifact, not meaningful.*

### Page metadata

```
Title: A quote from Thibault Sottiaux
Published: 16th July 2026, 5:45 pm
Tags: ai, generative-ai, llms, coding-agents, codex
Post type: "quotation" (Willison's site categorizes this post type explicitly:
  "This is a quotation collected by Simon Willison, posted on 16th July 2026.")
Cited tweet: https://twitter.com/thsottiaux/status/2077630111499882637 (@thsottiaux)
```

*Source: page `<head>` metadata and `.metabox` sidebar, same URL.*

## Cross-References

- **Corroborates**:
  - `blog-anthropic-how-contain-claude.md` Claim 3 ("protection in the model layer
    will never be 100% effective, which is why it can't stand alone") and Claim 14
    (preference for battle-tested infrastructure primitives over custom logic):
    this incident is a second-vendor, independent data point for the same
    principle — an "honest," non-malicious model action caused destructive harm
    specifically because environmental sandboxing was absent, not because model
    behavior was adversarial.
  - `blog-jetbrains-agentic-ai-governance.md` Claim 4 (the governance question
    should be "should this agent ever have been allowed to access this system at
    all?" rather than post-hoc fault-finding) and Claim 10 (agents should operate
    within constrained environments with scoped credentials and limited blast
    radius): the Sottiaux quote is a concrete failure case for exactly the
    boundary-condition gap these sources argue against — full access mode with no
    sandboxing removed any constraint on what the model could do to `$HOME`.
  - `blog-cursor-agent-autonomy-auto-review.md` Claim 11 (allowlists and
    sandboxing should handle the majority of agent commands, with a
    higher-judgment review layer reserved for a smaller subset of
    higher-consequence actions): this incident demonstrates the failure mode that
    occurs when that layered structure is entirely absent — no sandbox layer,
    and (per the quote) no auto-review layer either.

- **Contradicts**: None identified. No existing source note asserts that full
  access mode without sandboxing is safe for destructive filesystem operations;
  this source is uniformly consistent with the corpus's existing position that
  environmental sandboxing is necessary regardless of model behavior. No
  contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-datasette-blog-codex-session.md` Claim 5 (Codex Desktop
    accidentally deleted an untracked, user-owned directory during a cleanup
    pass, believing it to be disposable build output): both sources document a
    Codex-family product accidentally deleting content it should not have, but
    via different mechanisms and in different product surfaces. The May 2026
    incident was Codex Desktop misclassifying untracked content as ephemeral
    build output during an inferred cleanup step; this July 2026 report is
    (per Sottiaux) GPT-5.6 Codex overwriting/deleting `$HOME` itself while
    attempting to define a temp directory, in a full-access, unsandboxed
    configuration. Together they establish that Codex-family products have more
    than one distinct destructive-deletion failure mode, not a single isolated
    incident — a pattern worth naming explicitly in the guide rather than treating
    either report as a one-off.
  - `blog-simonwillison-codex-base-instructions.md` (Source Context /
    Concrete Artifacts, `codex-auto-review` model-tier entry): that note
    independently confirms "auto review" as a real, named Codex configuration
    dimension (one of six model tiers in OpenAI's public `models.json`). This
    source adds a concrete consequence of *not* having that dimension enabled —
    a destructive filesystem incident — which the base-instructions note did not
    itself analyze (it only listed the tier's existence without describing its
    behavior).

- **Novel**:
  - **`$HOME` env-var-override deletion mechanism**: no prior corpus source
    documents this specific technical trigger (a model attempting to redefine
    `$HOME` as a temp directory location and then deleting the wrong path). This
    is a distinct failure mechanism from the untracked-directory misclassification
    already in the corpus.
  - **A second, independent full-access/no-sandbox destructive-deletion incident
    in a coding agent product**: strengthens the corpus's evidence base that this
    configuration class (full access, no sandbox, no auto-review) is a recurring
    risk pattern across vendors (OpenAI/Codex here; Anthropic/Claude Code in
    `blog-anthropic-how-contain-claude.md`), not a single-vendor quirk.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this incident as a second, named
  example (alongside `blog-simonwillison-datasette-blog-codex-session.md` Claim 5)
  under any discussion of "why sandboxing is required for agents with filesystem
  access, even when the model is not being attacked." The specific mechanism —
  a model attempting to redefine `$HOME` for a legitimate-seeming purpose (a temp
  directory) and then deleting it — is a concrete, memorable illustration that
  destructive failures do not require adversarial intent; they can arise from an
  agent's own reasoning path when no environmental boundary constrains it. Note
  explicitly that the guide should flag this as a *qualitative* data point (one
  vendor's self-reported "handful" of cases), not a quantified failure rate.

- **Chapter 06 (Security & Threat Model)**: Add "full access mode + no sandboxing
  + no auto-review" as a named high-risk configuration triple, citing this source
  alongside the credential-phishing and Files API incidents in
  `blog-anthropic-how-contain-claude.md`. Recommend the guide state plainly that
  this configuration combination has now been independently linked to destructive
  incidents in agent products from at least two vendors, which is stronger
  evidence than either vendor's report alone.

## Extraction Notes

- The source page itself is extremely short: a dateline, one blockquote (three
  sentences of prose plus a three-item bulleted list, roughly 60 words of
  substantive content), and a one-line attribution caption. This is a Willison
  "quotation" post, a distinct post type on his site consisting of essentially a
  single quoted passage with minimal framing — there is no additional prose,
  analysis, or linked deep-dive to follow beyond the cited tweet itself. Per
  MINER.md §1 guidance to follow substantive linked pages: the page links only to
  the cited tweet (`https://twitter.com/thsottiaux/status/2077630111499882637`)
  and to three unrelated "Recent articles" (Kimi K3 benchmark commentary, the
  GPT-5.6 family launch post, and an sqlite-utils release) that do not bear on
  this topic and were not followed as substantive.
- The cited tweet was fetched directly (via `curl`, not WebFetch) to check for
  additional context (e.g., a longer thread, replies, or elaboration beyond what
  Simon Willison quoted). X/Twitter's page requires an authenticated session to
  render tweet body content; only the page's `<title>` and inferred
  `og:description`-equivalent text were retrievable, and both matched the
  blockquote text verbatim with no additional detail. It is possible the original
  tweet is part of a longer thread with more technical detail (root cause,
  timeline, fix status) that is not accessible from this vantage point — flagged
  for the Assayer or a future source pass if the thread becomes accessible.
- Given the page's brevity, only 5 claims were extracted (below MINER.md's
  5–15 target range). This reflects the genuine thinness of the source rather
  than shallow reading — the entire substantive content of the page is the single
  blockquote reproduced in full under Concrete Artifacts above; there is no
  additional material in the page to extract further claims from without
  padding or restating the same three bullets differently.
- Confidence set to `anecdotal` overall: the source is a single secondhand
  quotation (Willison quoting a tweet, not his own investigation or a formal
  incident report), the underlying claim is self-reported by an unverified author
  about an unspecified small number of cases ("a handful"), and no independent
  technical verification of the `$HOME`-override mechanism was possible from this
  extraction.
- No contradictions identified against the existing corpus; no contradiction
  issue filed (see Cross-References → Contradicts above).
