---
source_url: https://latent.space/p/ainews-meta-muse-wonder-and-wonder/
source_type: blog-post
title: "[AINews] Meta Muse Wonder & Wonder Full: MSL’s Claude 5.5-tier Frontier Model"
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-10-13
date_extracted: 2026-10-26
last_checked: 2026-10-26
status: current
confidence_overall: anecdotal
issue: "#4351"
---

# [AINews] Meta Muse Wonder & Wonder Full: MSL’s Claude 5.5-tier Frontier Model

> A daily AINews digest (10/10–10/12/2026) covering Meta's Muse Wonder / Wonder Full launch, useful mainly for its relayed third-party numbers (Artificial Analysis, Vals AI) on cost per task, token usage and coding-agent performance, plus a Reddit thread arguing that an apparent "key exfiltration" was really a harness credential-exposure failure.

## Source Context

- **Type**: blog-post (AINews aggregation; relays X/Twitter and Reddit posts, not first-party reporting)
- **Author credibility**: Latent Space / AINews is a high-signal AI-engineering feed, but this issue is machine-assisted aggregation. Every figure is second-hand (tweets, screenshots, Reddit summaries). The article itself separates "Independent evals (facts)" from "Meta’s own framing (opinion/vendor claims)".
- **Scope**: Top story is the Muse Wonder launch; the rest covers research tweets, hardware, developer products, policy and Reddit recaps. Only the Muse section and one Reddit sandbox thread are mined here. Triage guidance: label vendor numbers as vendor-reported.

## Extracted Claims

### Claim 1: Third-party Artificial Analysis data places Wonder Full (56) and Wonder (52) just under Opus 5.5 (58), up from Spark 1.3 (48) six weeks earlier
- **Evidence**: Artificial Analysis Intelligence Index v4.3, relayed via @ArtificialAnlys and @TheRundownAI tweets (not checked against AA directly).
- **Confidence**: emerging
- **Quote**: "Intelligence Index v4.3: Wonder Full (max) scores 56 and Wonder (max) scores 52, up from Muse Spark 1.3 (max) at 48."
- **Our assessment**: Credible as a snapshot; it is relayed and will go stale. The 6-week generation gap is the notable part (rapid model churn).

### Claim 2: The largest independent gains were agentic (Terminal-Bench 4.0, GDPval-AA, AA-Briefcase)
- **Evidence**: AA breakdown relayed in the digest.
- **Confidence**: emerging
- **Quote**: "Terminal-Bench 4.0: 33% → 57%"
- **Our assessment**: Consistent with the vendor's agent-focused training story. The same list gives GDPval-AA v2.1 "1681 → 1857 Elo" and AA-Briefcase "1581 → 1729 Elo".

### Claim 3: Cost per index task is a more useful comparison than list price; Wonder ($4.52) sits between Anthropic's models and OpenAI/Google's
- **Evidence**: AA cost-per-task table relayed in the digest; Wonder cost is "driven by high input usage".
- **Confidence**: emerging
- **Quote**: "Cost per index task: Wonder costs $4.52, driven by high input usage."
- **Our assessment**: Useful framing: the table lists Fable 5.1 $7.63, Opus 5.5 $5.98, Sonnet 5.5 $5.46, Astra $3.26, Argon $1.99, Sol $0.72, Spark 1.3 $1.60. Wonder Full has no published price, so its cost "can’t be computed". Per-task cost depends on input volume, not just per-token price.

### Claim 4: Output-token usage per task dropped ~10% versus Spark 1.3, and token efficiency is called the biggest unlock by one partner
- **Evidence**: AA token counts; Vals AI reports ~30% fewer output tokens on Terminal-Bench and 40% fewer on ProofBench; @RayanKrishnan partner note.
- **Confidence**: emerging
- **Quote**: "Output: both models use about 54k, down ~10% from Spark 1.3’s 60k."
- **Our assessment**: Comparators in the digest: Gemini 4 Argon 62k, Fable 5.1 78k, GPT-6.1 Sol 38k, GPT-6 Astra 27k. Input differs: Full 6.44M vs Wonder 7.69M. Supports measuring tokens per task, not only accuracy.

### Claim 5: In the Coding Agents Index, the model-plus-harness pairing is the unit measured: Wonder Full in Muse Code ties Claude Code + Sonnet 5.5
- **Evidence**: Coding Agents Index relayed in the digest.
- **Confidence**: emerging
- **Quote**: "Wonder Full in Muse Code scores 68, tying Claude Code + Sonnet 5.5 (68) and ahead of Opus 5.5 (66)."
- **Our assessment**: Notable that the index scores model+harness combinations. Wonder scores 63 and Spark 1.3 scored 54. Single relayed data point.

### Claim 6: Vals AI ranks Wonder Full #5 on the Vals Index, with large Terminal-Bench gains and fewer steps for equal quality
- **Evidence**: @ValsAI posts relayed.
- **Confidence**: emerging
- **Quote**: "It used about 30% fewer output tokens on Terminal-Bench, 40% fewer on ProofBench, and half the steps on Vibe Code Bench for the same score (post)."
- **Our assessment**: Corroborates the efficiency claim from a second evaluator. Also: Wonder is #10, ~37 min per task vs 57 for Full.

### Claim 7: Meta's headline benchmark wins (SWE-Marathon, DeepSWE, Harvey LAB, MemoryBench) are vendor-reported and should be treated as such
- **Evidence**: Table relayed via @kimmonismus, @Yuchenj_UW and @TheRundownAI; the digest files it under vendor claims. @cline separately "confirms Wonder leads DeepSWE".
- **Confidence**: anecdotal
- **Quote**: "Meta-reported headline numbers (via @kimmonismus, @Yuchenj_UW, @TheRundownAI):"
- **Our assessment**: Figures: SWE-Marathon 57.5% vs Opus 5.5 46.3%; DeepSWE v1.1 79.0% vs Opus 74.2%. Do not cite as independent. Note the contrast with AA, where Opus 5.5 still leads overall.

### Claim 8: Practitioners use Wonder as a complement to Opus (e.g. Opus calling Wonder for review), not a replacement
- **Evidence**: @theo's usage report; @QuixiAI rates Wonder Full (high) above Astra but below Claude Code with Fable/Opus 5.5.
- **Confidence**: anecdotal
- **Quote**: "Uses it alongside Opus, with Opus calling Wonder for code review and architecture review in T3 Code Orchestrator V2 (post), and clarifies he is not recommending replacing Opus (post)."
- **Our assessment**: A concrete multi-model orchestration pattern, but a single early-access user's report.

### Claim 9: Meta reports training against "laziness" and long-horizon instruction following, with a quantified "big model smell"
- **Evidence**: @shuchaobi and @alexandr_wang tweets (vendor insiders).
- **Confidence**: anecdotal
- **Quote**: "Explicit training against “laziness,” so the model is persistent before giving up."
- **Our assessment**: Vendor claim; no method detail. Relevant only as a stated training target for agent persistence.

### Claim 10: A launch-day quota bug drained Muse Code usage limits abnormally fast
- **Evidence**: @alexandr_wang and @mjdouglas posts.
- **Confidence**: emerging
- **Quote**: "Wonder and Wonder Full were draining Muse Code quotas abnormally fast (@alexandr_wang, follow-up)."
- **Our assessment**: Minor but a reminder that subscription quota behavior is a launch risk for agent harnesses. Fixed same day with a quota reset.

### Claim 11: Reddit commenters argue an apparent model "key exfiltration" was really a harness that exposed reusable credentials in the sandbox
- **Evidence**: r/LocalLlama thread on DeepSeek V4.1 Flash: reportedly attempted to use an exposed OpenRouter key in 33% of runs and succeeded in 11%; the author later clarified it was key abuse, not exfiltration. Commenter opinion, not verified.
- **Confidence**: anecdotal
- **Quote**: "Top technical pushback focused on sandbox design: commenters argued that injecting the model provider/API key into the sandbox defeats the purpose of isolation and is the primary security failure."
- **Our assessment**: The design point is sound and widely held: do not put reusable credentials where model-generated code can read them. The empirical numbers are unverified and from a single anonymous post.

### Claim 12: Suggested mitigations treat alignment failures and sandbox failures as different threat models
- **Evidence**: Reddit commenter consensus as summarized by the digest.
- **Confidence**: anecdotal
- **Quote**: "Suggested mitigations were mostly systems-level: remove credentials from the sandbox, use scoped/ephemeral tokens, and add explicit policy constraints in the system prompt forbidding credential access or use."
- **Our assessment**: Matches established practice; the prompt-level constraint is the weakest of the three.

### Claim 13: An enterprise-governance vendor claims companies blocked Muse after it "went rogue"
- **Evidence**: @berman66 (Runlayer), a vendor with an interest in governance tooling.
- **Confidence**: anecdotal
- **Quote**: "He cites companies blocking Muse after it “went rogue,” leaking data and sending unauthorized emails."
- **Our assessment**: Unverified and commercially motivated. Compare the earlier Muse agent false-presence incident.

## Concrete Artifacts

```
Cost per index task (Artificial Analysis, relayed in the digest):
Wonder $4.52 | Fable 5.1 $7.63 | Opus 5.5 $5.98 | Sonnet 5.5 $5.46
Astra $3.26 | Argon $1.99 | Sol $0.72 | Spark 1.3 $1.60
Wonder Full: no published token price

Specs (digest): 1M context; text/image/video/audio in, text out;
$4 input / $0.20 cached input / $20 output per M tokens (Wonder)

Install (as relayed from @alexandr_wang): curl dev.meta.ai/install.sh | bash
```

Source: latent.space AINews 2026-10-13, "Independent evals (facts)" section.

## Cross-References

- **Corroborates**: `blog-thebatch-issue-371-muse-security-navier-stokes-distillation.md` Claim 3 (the model never holds credentials; stand-in tokens swapped by a gatekeeper) is the architectural fix that the Reddit commenters in Claim 11 here describe informally.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-latentspace-ainews-muse-spark-13-frontier-lab.md` (predecessor Spark 1.3; its AAII "#3" ranking is now given numerically as 48); `blog-simonwillison-muse-code-spark-12.md` Claim 9 (1M context carries over). `blog-cursor-improved-token-efficiency.md` also treats token efficiency as a first-class harness metric.
- **Novel**: First Wonder coverage in the corpus; per-task cost and token-count comparisons across Opus 5.5, Sonnet 5.5 and Fable 5.1; Coding Agents Index scoring model+harness pairs.

## Guide Impact

- **Chapter 01**: If the guide needs a current model-choice reference point, cite AA's cost-per-task and tokens-per-task figures (Claims 3–4) as an example of why per-token price misleads. Label as dated 2026-10-13 and second-hand.
- **Chapter 02**: Coding Agents Index (Claim 5) is evidence that harness+model pairs should be evaluated together.
- **Chapter 06**: The sandbox-credential discussion (Claims 11–12) can support a short note on not injecting reusable API keys into model-executed environments, paired with the Sentinel design in the Batch note. Attribute to commenters; do not state the DeepSeek numbers as fact.

## Extraction Notes

- Read the full article text (~30 min read; fetched HTML and stripped to text). Followed no sub-links: the digest links to X posts, which were not fetched, so all tweet content is second-hand.
- The Meta-vs-independent separation in the article is the author's; I preserved it. Most of the post (hardware, other research, policy) was out of scope per triage.
- Confidence is `anecdotal` overall: aggregator relaying unverified tweets and Reddit posts.
