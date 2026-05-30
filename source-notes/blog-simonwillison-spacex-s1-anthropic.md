---
source_url: https://simonwillison.net/2026/May/20/spacex-s1/
source_type: blog-post
title: "A quote from SpaceX S-1"
author: Simon Willison
date_published: 2026-05-20
date_extracted: 2026-05-30
last_checked: 2026-05-30
status: current
confidence_overall: settled
issue: "#998"
---

# A quote from SpaceX S-1

> Simon Willison quotes the SpaceX S-1 SEC filing's disclosure of the
> Anthropic compute deal: $1.25B/month through May 2029 for access to
> capacity across both COLOSSUS and COLOSSUS II — primary-source confirmation
> that updates and partially contradicts the May 7 analysis scope (Colossus 1
> only) and adds the shared-capacity context (SpaceX also trains Grok 5 at
> COLOSSUS II concurrently).

## Source Context

- **Type**: blog-post (minimal-commentary quotation post — Willison presents
  the S-1 passage with emphasis on key terms and a source attribution to the
  SEC filing; there is no extended analysis or editorial interpretation.
  Published May 20, 2026 — thirteen days after his own analysis post on the
  same deal.)
- **Author credibility**: Simon Willison is the creator of Django and a
  high-signal independent AI commentary source with no vendor affiliation.
  In this post, Willison is functioning primarily as a curator/signal-booster,
  not an analyst — the evidential weight rests entirely on the primary source
  he quotes (the SEC filing). His role here is to surface the document to his
  audience; the S-1 itself is the authoritative source.
- **Scope**: Covers the single paragraph from the SpaceX S-1 that discloses
  the Anthropic Cloud Services Agreement. Does NOT contain extended commentary,
  analysis of implications, or any environmental/governance discussion. Does
  NOT cover the full scope of the SpaceX S-1 filing — only this compute
  agreement excerpt.

## Extracted Claims

### Claim 1: The Cloud Services Agreements grant Anthropic access to compute capacity across both COLOSSUS and COLOSSUS II, not Colossus 1 alone

- **Evidence**: Verbatim language from the SpaceX S-1 SEC filing — the
  primary legal document governing the deal, cited by Willison directly. SEC
  filings are formal disclosures reviewed by legal counsel and filed under
  penalty for material misstatement. This is the most authoritative evidence
  available about the scope of the agreement.
- **Confidence**: settled
- **Quote**: "we entered into Cloud Services Agreements with Anthropic PBC ("Anthropic"), an AI research and development public benefit corporation, with respect to access to compute capacity across COLOSSUS and COLOSSUS II"
- **Our assessment**: This directly contradicts `blog-simonwillison-xai-anthropic-datacenter.md` Claim 2, which states "Anthropic are getting Colossus 1, but xAI are keeping their larger Colossus 2 data center for their own work." The S-1 is the primary source of record — it post-dates the May 7 analysis by 13 days and governs the legal terms of the deal. The May 7 characterization was Willison's analysis of the public announcement framing; the S-1 reflects the binding contractual scope. See **Contradicts** section and filed contradiction issue #1007.

### Claim 2: Anthropic agreed to pay $1.25 billion per month through May 2029

- **Evidence**: Direct S-1 disclosure of the financial term — a material
  fact required to be accurately reported in an SEC filing.
- **Confidence**: settled
- **Quote**: "the customer has agreed to pay us $1.25 billion per month through May 2029"
- **Our assessment**: The financial scale ($1.25B/month) and duration (through
  May 2029 — approximately 3 years from the filing date) establishes this as
  one of the largest known AI infrastructure agreements. For practitioners, the
  total committed spend (roughly $15B over the deal period before ramping
  reductions) provides context for understanding why Anthropic would accept the
  governance terms (Musk's reclaim clause) documented in
  `blog-simonwillison-xai-anthropic-datacenter.md` Claim 8. The financial
  commitment also validates the compute-constraint framing (Claim 1 in the
  May 7 note): this is not an opportunistic purchase of overflow capacity.

### Claim 3: Capacity is ramping in May and June 2026 at a reduced fee, not at full rate from day one

- **Evidence**: S-1 disclosure of commercial terms — legally binding,
  accuracy required for SEC compliance.
- **Confidence**: settled
- **Quote**: "with capacity ramping in May and June 2026 at a reduced fee"
- **Our assessment**: The ramp period (May–June 2026) aligns with the timing
  of the announcement (May 6, 2026 Code w/ Claude event) and the S-1 filing
  (May 20, 2026). The reduced-fee ramp structure is a standard commercial
  arrangement for infrastructure contracts where capacity cannot be delivered
  at full scale immediately. For practitioners reasoning about Anthropic's
  rate limits and API capacity in mid-2026: the ramp clause explains why the
  full compute benefit of the deal would not be available at announcement time.

### Claim 4: Either party may terminate the agreements with 90 days' notice — a relatively short window for a $1.25B/month infrastructure commitment

- **Evidence**: S-1 disclosure of termination terms.
- **Confidence**: settled
- **Quote**: "The agreements may be terminated by either party upon 90 days' notice."
- **Our assessment**: 90 days is notable as a termination clause for a
  deal at this scale and duration. Standard large-scale infrastructure
  contracts often carry much longer notice periods or lock-in terms. The
  bilateral termination right — either party, not just SpaceX — means
  Anthropic can also exit with 90 days' notice, providing some optionality.
  However, this same clause means SpaceX can terminate (or, in the context of
  Musk's reclaim threat documented in `blog-simonwillison-xai-anthropic-datacenter.md`
  Claim 8, execute the reclaim) with only 90 days' notice. The 90-day window
  provides limited operational runway for Anthropic to source alternative
  compute if the agreement is terminated.

### Claim 5: SpaceX is simultaneously using COLOSSUS II for Grok 5 training while providing Anthropic access to capacity across both facilities — this is a shared-capacity arrangement, not exclusive access

- **Evidence**: S-1 explicitly states Grok 5 "is currently being trained at
  COLOSSUS II" in the same passage that describes providing Anthropic access
  to compute "across COLOSSUS and COLOSSUS II."
- **Confidence**: settled
- **Quote**: "We have the ability to use compute resources to support our proprietary AI applications (such as Grok 5, which is currently being trained at COLOSSUS II), while also providing access to select compute capacity to third-party customers."
- **Our assessment**: The "select compute capacity" framing is significant: SpaceX is not handing over COLOSSUS II to Anthropic; they are monetizing available capacity beyond what their own Grok 5 training requires. This means Anthropic's effective compute access at COLOSSUS II is bounded by SpaceX's own utilization. The governance risk is therefore more nuanced than a simple "Colossus 1 only" picture: Anthropic gets capacity across both facilities, but COLOSSUS II is not dedicated — it is shared with SpaceX's own priority workloads. This shared nature may partially reconcile the May 7 note's claim that xAI "keeps" Colossus 2 for their own work: xAI/SpaceX does retain priority use, while also monetizing available capacity to Anthropic.

### Claim 6: The S-1 describes Anthropic PBC formally as "an AI research and development public benefit corporation"

- **Evidence**: S-1 legal characterization of Anthropic's corporate structure.
- **Confidence**: settled
- **Quote**: "Anthropic PBC (\"Anthropic\"), an AI research and development public benefit corporation"
- **Our assessment**: The public benefit corporation (PBC) framing is
  embedded in the contractual documentation. For practitioners evaluating
  Anthropic's corporate governance and how it relates to their AI safety
  mission, the PBC structure being named in the SEC filing signals that
  Anthropic's unusual governance model is explicitly acknowledged in major
  commercial agreements. This connects to the Musk reclaim clause risk: the
  compute access is formally associated with an entity whose stated mission
  (public benefit AI development) is referenced in the agreement.

### Claim 7: Willison presents the S-1 passage with minimal commentary — the post is a signal-amplification act, not an analysis

- **Evidence**: Willison's post structure as described by the source: he
  presents the excerpt with emphasis on key terms and source attribution, but
  provides no extended editorial analysis or interpretation.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This source's value is primary-source amplification, not
  independent analysis. Willison's judgment in surfacing it is itself a signal
  (he found it notable enough to post), but the evidentiary weight rests on the
  S-1, not on Willison's commentary. Contrast with his May 7 post, which was a
  substantial analysis with editorial judgments about governance risk,
  environmental record, and supply chain implications. Practitioners reading
  this source should understand they're reading the SEC filing through
  Willison's curation lens, not his analytical frame.

## Concrete Artifacts

### SpaceX S-1 Filing — Anthropic Cloud Services Agreement Disclosure (May 20, 2026)

```
Source: SpaceX S-1 SEC filing, quoted verbatim by Simon Willison
(https://simonwillison.net/2026/May/20/spacex-s1/)

"We have the ability to use compute resources to support our proprietary AI
applications (such as Grok 5, which is currently being trained at COLOSSUS II),
while also providing access to select compute capacity to third-party customers.
For example, in May 2026, we entered into Cloud Services Agreements with
Anthropic PBC ("Anthropic"), an AI research and development public benefit
corporation, with respect to access to compute capacity across COLOSSUS and
COLOSSUS II. Pursuant to these agreements, the customer has agreed to pay us
$1.25 billion per month through May 2029, with capacity ramping in May and
June 2026 at a reduced fee. The agreements may be terminated by either party
upon 90 days' notice."
```

### Financial and Commercial Terms Summary

```
Source: Derived from SpaceX S-1 passage quoted above

Deal structure:
  Party A: SpaceX (infrastructure provider)
  Party B: Anthropic PBC ("an AI research and development public benefit corporation")

Infrastructure scope:
  - Access to compute capacity across COLOSSUS and COLOSSUS II
  - "Select compute capacity" (shared, not dedicated — SpaceX also trains Grok 5 at COLOSSUS II)

Financial terms:
  - $1.25 billion per month
  - Duration: through May 2029 (~3 years from S-1 filing)
  - Estimated committed spend: ~$45B total (at full rate; excludes ramp discounts)
  - May–June 2026: capacity ramp period at a reduced fee

Exit terms:
  - Either party may terminate with 90 days' notice
  - No lock-in past notice period documented

Filing date: May 20, 2026 (SpaceX S-1)
```

## Cross-References

- **Contradicts**: `blog-simonwillison-xai-anthropic-datacenter.md` Claim 2
  ("Anthropic are getting Colossus 1, but xAI are keeping their larger Colossus
  2 data center for their own work.") — the S-1 says access spans both COLOSSUS
  and COLOSSUS II, not Colossus 1 alone. The May 7 note characterized the scope
  as Colossus 1 only; the SEC filing is the authoritative primary document and
  states both facilities are covered. **See contradiction issue #1007.** The
  Miner does not pick a verdict; the contradiction is filed for human resolution.

- **Corroborates**:
  - `blog-simonwillison-xai-anthropic-datacenter.md` Claim 9 (supply chain risk
    framing): the S-1 provides financial specificity ($1.25B/month, 90-day
    termination) that makes the supply chain risk pattern more concrete and
    quantifiable. The deal's scale and short termination notice now have primary-
    source confirmation.
  - `blog-simonwillison-xai-anthropic-datacenter.md` Claim 8 (Musk reclaim
    clause): the S-1's 90-day termination window is the contractual mechanism
    through which that governance risk could be exercised — the two claims
    together complete the picture of how governance risk and termination
    mechanics interact.
  - `blog-simonwillison-xai-anthropic-datacenter.md` Claim 1 (Anthropic is
    "severely compute-constrained"): the $1.25B/month commitment is consistent
    with extreme compute constraint — this is not an exploratory purchase.

- **Extends**:
  - `blog-simonwillison-xai-anthropic-datacenter.md`: The May 7 analysis built
    the governance/environmental risk framework around this deal. This S-1
    source adds primary-source financial specificity, confirms the
    infrastructure scope (updating Claim 2), and provides the 90-day
    termination clause that quantifies the governance risk window. The two notes
    should be read together.
  - `blog-simonwillison-code-w-claude-2026.md` Claim 5 (original Colossus
    announcement: "We're partnering with SpaceX to use all of the capacity of
    their Colossus data center"): the S-1 is the primary-source confirmation of
    this announcement, with added financial specificity and infrastructure scope
    clarification (both COLOSSUS and COLOSSUS II, not "Colossus data center"
    as an undifferentiated whole).

- **Novel**:
  - **Primary-source financial disclosure**: $1.25B/month is now confirmed in
    an SEC filing. Prior corpus references to this figure were from news
    coverage and Willison's analysis; this is the authoritative primary
    source.
  - **90-day bilateral termination**: The specific termination clause (either
    party, 90 days) is new to the corpus. Prior notes discussed governance risk
    but did not have the formal termination mechanics.
  - **Shared-capacity framing**: The S-1's "select compute capacity" language
    and simultaneous Grok 5 training at COLOSSUS II establishes that Anthropic
    gets shared capacity, not dedicated infrastructure. Prior notes discussed
    the deal as a data center lease; the S-1 characterizes it as a cloud
    services agreement with capacity sharing.
  - **Duration through May 2029**: The end date is primary-source confirmed.
    Prior notes noted the duration but the S-1 is the authoritative source.

## Guide Impact

- **Chapter 03 (Economics, Governance, Supply Chain)**: The existing supply
  chain risk analysis (drawn from `blog-simonwillison-xai-anthropic-datacenter.md`)
  should be updated to reflect: (1) the financial scale now has primary-source
  confirmation ($1.25B/month, S-1); (2) the 90-day termination window is the
  formal mechanism for the governance risk, making it concrete and time-bounded;
  (3) the infrastructure scope should be updated pending resolution of
  contradiction #1007 — whether practitioners should understand the deal as
  Colossus 1 or both COLOSSUS and COLOSSUS II changes the risk surface analysis.
  Hold on updating Claim 2's scope framing until #1007 is resolved.

- **Chapter 03 (Infrastructure Scope)**: Once contradiction #1007 is resolved,
  update the infrastructure scope description to match the authoritative
  primary-source claim. If the verdict is `superseded` (S-1 controls), the
  guide should describe Anthropic's compute access as spanning both COLOSSUS
  and COLOSSUS II at shared capacity, not as exclusive Colossus 1 access.

- **Chapter 05 (Commercial Dynamics of AI Infrastructure)**: The $1.25B/month
  figure, now confirmed by an SEC filing, is the strongest available primary-
  source evidence for the scale at which AI model providers are investing in
  compute infrastructure. The guide can cite this as `[settled]` evidence for
  the cost structure of frontier AI capability.

- **Chapter 03 (Termination Risk)**: The 90-day bilateral termination clause
  is concrete new evidence for the "supply chain optionality" discussion. Anthropic
  can exit with 90 days' notice — but so can SpaceX. Practitioners building on
  Anthropic's APIs should understand that their supply chain's infrastructure
  layer can be renegotiated or terminated with a 90-day window, which limits
  the operational runway for finding alternative compute if SpaceX exercises
  its termination right.

## Extraction Notes

- Source is a minimal-commentary quotation post. The full evidentiary content
  is in the single S-1 passage. Willison provides source attribution to the
  SEC filing but no extended analysis.
- The verbatim block quote from the S-1 was extracted via two targeted WebFetch
  calls, with the second call explicitly requesting the exact block quote text.
  The quote beginning "We have the ability to use compute resources..." through
  "...upon 90 days' notice." was returned with the note that it matched the
  exact page content.
- A contradiction was identified between this source's Claim 1 and
  `blog-simonwillison-xai-anthropic-datacenter.md` Claim 2 regarding the
  facility scope (Colossus 1 only vs. both COLOSSUS and COLOSSUS II).
  Contradiction issue #1007 was filed before this PR was opened, per
  MINER.md §4a. The source note does not pick a verdict — it presents both
  claims and references the open issue.
- The estimated $45B total commitment is the Miner's arithmetic
  ($1.25B/month × ~36 months), not a figure stated in the source. It is
  presented as a derived calculation in the artifacts section, not as a
  direct quote.
- No sub-pages were followed; the post is a single-excerpt quotation post
  with no substantive linked pages.
- Confidence overall is `settled` because the core factual claims (facility
  scope, financial terms, duration, termination clause) derive from a primary
  SEC filing. The shared-capacity interpretation (Claim 5) involves some
  inference from the S-1 language, but the underlying facts are directly stated.
