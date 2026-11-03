---
source_url: https://latent.space/p/ainews-openais-patch-the-planet-program/
source_type: blog-post
title: "[AINews] OpenAI's Patch the Planet program is 1 of 2 parties to discover PHP2Shell vulnerabilities in core PHP affecting 70% of the web, using GPT-5.6 Sol; coordinated response over 2 months"
author: Latent Space / AINews (daily digest; aggregates tweets and Reddit for 10/20/2026-10/21/2026)
date_published: 2026-10-22
date_extracted: 2026-11-03
last_checked: 2026-11-03
status: current
confidence_overall: anecdotal
issue: "#4503"
---

# [AINews] OpenAI's Patch the Planet program ... PHP2Shell

> A secondary digest of the PHP2Shell incident (two PHP-engine memory-corruption CVEs, multi-party AI-assisted discovery, ~2-month coordinated remediation, Cloudflare stopgap WAF rules) that is unusually explicit about which claims are researcher-reported or tweet-sourced and which evidence gaps remain open.

## Source Context

- **Type**: blog-post (Latent Space "AINews" daily digest, 37-minute read; only the "Top Story" concerns PHP2Shell, the rest covers unrelated items such as Flint, DeepInfer, and subreddit recaps).
- **Author credibility**: Automated/editorial aggregation with no individual byline. Every PHP2Shell claim is sourced to tweets (@sagitz_, @OpenAI, @dok2001, @NSACyber, @TheRundownAI, etc.). The digest itself repeatedly flags "supplied material" limits, so it is useful as a map of what is and is not established, not as primary evidence.
- **Scope**: Chronology, AI attribution, operational complications, public reactions. It does NOT supply a PHP Foundation advisory, fixed-version matrix, CVSS, or patch commit. The digest's headline "affecting 70% of the web" is a title-level figure; the body does not substantiate it and says the severity is "up to some debate".

## Extracted Claims

### Claim 1: Two PHP-engine memory-corruption bugs (CVE-2026-109618 / CVE-2026-109619) were disclosed, with researcher-reported pre-auth RCE against WordPress, Drupal, and Joomla
- **Evidence**: Researcher announcement thread (@sagitz_) as relayed by the digest; no primary advisory in the digest's record.
- **Confidence**: anecdotal
- **Quote**: "Their technical description places the defects in PHP’s internal handling of out-of-memory conditions and fatal errors—not in a WordPress plugin or an application’s authentication logic."
- **Our assessment**: Record as researcher claims. The digest explicitly warns these "should not be silently expanded into a claim that every deployment has an identical, immediately exploitable RCE path." We should not generalize to "every PHP deployment is trivially exploitable."

### Claim 2: Discovery credit is disputed/multi-party: OpenAI credits Calif with GPT-5.6 Sol; a Wiz-affiliated account credits Gemini 4 Argon
- **Evidence**: Posts from @OpenAI, @TheRundownAI, @steipete, @ralucaadapopa. The intro adds that Wiz used "Gemini 4 Argon and GPT-5.6 Sol, as well as their own tool, Wiz Atlas".
- **Confidence**: anecdotal
- **Quote**: "This is a multi-party discovery story, not evidence that one vendor alone found and fixed the issue."
- **Our assessment**: Causality/attribution between the two discovery tracks stays open; the independent discovery timeline is listed as an unresolved gap. Do not cite this as "GPT-5.6 Sol found PHP2Shell" without the Wiz counter-claim.

### Claim 3: Remediation involved ~2 months of private, coalition-led coordination including governments before disclosure
- **Evidence**: Participant accounts (OpenAI, Eric Wallace, Greg Brockman, @itszn13); the patch reportedly required a major PHP-engine change with PHP Foundation involvement.
- **Confidence**: anecdotal
- **Quote**: "These are participant accounts, not an independently audited incident timeline."
- **Our assessment**: A useful data point for AI-era coordinated disclosure (long embargo, patch + detection built in parallel), but self-reported by the parties who benefit from the narrative.

### Claim 4: Cloudflare shipped stopgap WAF rules to all tiers ahead of the patch release and told operators to patch at 14:00 UTC
- **Evidence**: Cloudflare CTO post (@dok2001); the digest calls it "the strongest firsthand operational evidence in the supplied record".
- **Confidence**: emerging
- **Quote**: "He explicitly called the rules a"  (digest text continues: "stopgap and directed operators to patch at 14:00 UTC")
- **Our assessment**: The quote is truncated at the formatting boundary; the substantive point is that WAF rules were framed as temporary. Cloudflare did not disclose compromise counts, victim counts, or payload provenance (digest says so), so "early attacks" evidence is thin. Overlaps with open issue #4499.

### Claim 5: OpenAI frames this as a "Defender's Window", but only "to our knowledge"
- **Evidence**: OpenAI messaging via the digest.
- **Confidence**: anecdotal
- **Quote**: "Importantly, its wording is"  (digest text continues: "“to our knowledge”—not proof that no attacker previously knew the vulnerabilities.")
- **Our assessment**: Good caution for Ch06: "found first by defenders" is unfalsifiable from the outside. Compare the Defender's Window framing in `blog-openai-defenders-window.md`.

### Claim 6: Many headline claims (early leak, ~1.5M unpatched servers per Censys, widespread shutdowns, 1.5M figure, Japan PM warning) are uncorroborated in the digest's record
- **Evidence**: The Rundown and a viral compilation (@fiveoutofnine); SemiAnalysis for the Japan PM warning.
- **Confidence**: anecdotal
- **Quote**: "None of those individual claims is corroborated by its underlying advisory, measurement, or status page in the supplied material."
- **Our assessment**: Do not carry forward breach/shutdown/exposure counts as fact. The digest also notes SemiAnalysis frames the Japan response against an existing breach wave, not as caused by PHP2Shell.

### Claim 7: Google's Gemini 4 Argon "found more than twice as many vulnerabilities as baseline models" is promotional, not an independent evaluation
- **Evidence**: Google promotional post via @Google.
- **Confidence**: anecdotal
- **Quote**: "but the supplied promotional post does not expose the dataset, baselines, budgets, or false-positive accounting."
- **Our assessment**: Consistent with our corpus's treatment of vendor-reported cyber benchmarks as unverified.

### Claim 8: A burst of disclosures is not evidence of a burst of AI-caused compromises
- **Evidence**: Editorial analysis; the feed mixes defensive discovery, supply-chain attacks, credential theft, and unrelated vulnerabilities.
- **Confidence**: emerging
- **Quote**: "A burst of disclosures is not, by itself, evidence of a burst of AI-caused compromises."
- **Our assessment**: Sound epistemics; the CVE-volume claim (~4,000 to 15,000/month per Sarah Guo) is flagged by the digest as unverified.

### Claim 9: The emergency is as much about distribution and ownership as discovery
- **Evidence**: Operator anecdotes (@ostrisai, @jd_pressman).
- **Confidence**: anecdotal
- **Quote**: "The emergency is as much distribution and ownership as discovery."
- **Our assessment**: Strong, practical point for Ch06: AI-accelerated discovery shifts the bottleneck to inventory, packaging, deploy, and verification of running builds.

### Claim 10: WAF coverage can create false confidence; shutdown guidance is conditional
- **Evidence**: Digest analysis of Cloudflare and NSA statements.
- **Confidence**: emerging
- **Quote**: "Proxied coverage, alternate ingress paths, and the origin’s exposure must be checked rather than assumed."
- **Our assessment**: Reasonable operator guidance; digest's own synthesis rather than a primary-source finding.

### Claim 11: Using the RCE to "auto-patch every server" is a proposal, not an authorized remediation plan
- **Evidence**: Proposal by Marc Köhlbrugge; pardon suggestion by J. D. Pressman; digest rebuttal.
- **Confidence**: anecdotal
- **Quote**: "“Use the RCE to auto-patch every server” is a proposal, not an authorized remediation plan."
- **Our assessment**: Relevant to agent-authorization boundaries: capability to act does not equal authorization.

### Claim 12: Update velocity carries a supply-chain trade-off
- **Evidence**: Widely shared post (@xeophon) and Pressman commentary.
- **Confidence**: anecdotal
- **Quote**: "Update velocity has a supply-chain trade-off."
- **Our assessment**: A genuine tension (fast patching vs compromised packages); no data offered.

### Claim 13: OpenAI published a Codex skill to help operators check PHP2Shell exposure
- **Evidence**: OpenAI repository (via @OpenAI).
- **Confidence**: anecdotal
- **Quote**: "That is an assistance workflow, not a substitute for a vendor advisory, package verification, or evidence that every vulnerable runtime has been replaced."
- **Our assessment**: A concrete example of shipping an agent skill as an incident-response aid; we have not inspected the repository itself.

## Concrete Artifacts

Digest's recommended incident sequence (Operational complications section):

```
For an incident team, the defensible sequence is to obtain the authoritative PHP and distribution advisories, inventory exposed runtimes, apply temporary protections where justified, deploy authenticated fixed packages, verify running processes, and investigate evidence of exploitation separately. Updating closes a vulnerability; it does not establish that credentials or data were never exposed.
```

Unresolved evidence gaps listed by the digest: exact affected and fixed versions; CVSS vectors; deployment prerequisites; the independent discovery timeline; what leaked before release; successful exploitation versus scanning; validated exposure counts; the cause and duration of each reported shutdown.

Timeline (as reported, unaudited): ~2 months private coordination -> 23:00 JST Oct 21 / 14:00 UTC patch window -> Cloudflare WAF stopgap -> NSA warning -> OpenAI says upgrades available -> Codex exposure-check skill.

## Cross-References

- **Corroborates**: `blog-openai-patch-the-planet.md` (program context: Claim 11 there, human review of AI findings; Claim 13, maintainers control disclosure); `blog-latentspace-ainews-cybersecurity-top-of-mind.md` (same digest's pattern of mixing vendor claims with commentary, e.g. its Claim 5 on vendor-reported cyber benchmark counts).
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-openai-patch-the-planet.md` (adds first major incident under the program); `blog-simonwillison-calif-weworm.md` (Calif again appears as an AI-assisted vuln-discovery party; there, Claim 3 and Claim 9 describe fast AI-assisted exploit development and coordinated disclosure); `blog-ghuntley-patch-the-planet.md` and `blog-openai-defenders-window.md` (Defender's Window framing; not re-read claim-by-claim here).
- **Novel**: PHP2Shell incident itself; explicit competing-credit (Calif/GPT-5.6 Sol vs Wiz/Gemini 4 Argon) attribution; the digest's evidence-gap checklist; operator-side bottlenecks (inventory, verify running build); WAF false-confidence caution.

## Guide Impact

- **Chapter 06 (Security / threat model)**: If the guide cites the Defender's Window or Patch the Planet, add PHP2Shell as an *example with caveats*: researcher-reported, multi-party discovery, "to our knowledge" wording, and no primary advisory in this source. Add the "discovery is not the bottleneck; inventory/patch/verify is" point (Claim 9) and the unauthorized-auto-patch caution (Claim 11).
- **Chapter 03 (Verification)**: Optional illustration of separating researcher-reported from verified claims; the evidence-gap list is a reusable template.
- Recommend waiting for a primary source (PHP Foundation advisory, Cloudflare post, OpenAI post) before stating any version, severity, or exposure figure in the guide.

## Extraction Notes

- Read the full Top Story section from the fetched page (raw HTML text), plus the intro and the start of "Other News"; the remainder of the issue is unrelated and was skipped.
- Followed no linked primary sources (tweets are not retrievable); all claims are therefore second-hand.
- Some Quote fields end at a formatting boundary where the digest bolds a phrase; those are noted inline and the fragments are contiguous source text.
- Title's "70% of the web" is unsupported by the body; do not repeat.
