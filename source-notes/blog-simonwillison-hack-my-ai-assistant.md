---
source_url: https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/
source_type: blog-post
title: "What happened after 2,000 people tried to hack my AI assistant"
author: Simon Willison (link-post commentary on Fernando Irarrázaval's hackmyclaw.com challenge)
date_published: 2026-06-26
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1429"
---

# What happened after 2,000 people tried to hack my AI assistant

> A public red-team challenge — 2,000 people, 6,000 email-based prompt-injection attempts, $500 in token spend — failed to extract a protected secret from an Opus 4.6-powered OpenClaw instance defended by nothing more than a 10-20 line system-prompt instruction, which Willison reads as evidence that frontier-model anti-injection training is starting to work in practice, with an explicit caveat against relying on it alone.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog link-post, June 26, 2026, ~6:33pm; tagged `security`, `ai`, `prompt-injection`, `generative-ai`, `llms`). Willison's post is short editorial commentary that links to the primary source, Fernando Irarrázaval's challenge site hackmyclaw.com, which was independently fetched for this extraction and supplies most of the concrete factual detail (target, defense mechanism, prize, outcome).
- **Author credibility**: Simon Willison is a widely-followed independent commentator on LLM tooling and security, designated a `trusted-feed` source in this repo, and maintainer of the canonical prompt-injection incident index at simonwillison.net/tags/prompt-injection/. Fernando Irarrázaval (Twitter/X handle `@cucho`) is the challenge organizer and operator of the tested OpenClaw instance; he is a practitioner running a live, self-funded (plus sponsor-funded) public red-team exercise rather than a peer-reviewed researcher. The challenge had real financial stakes: a $1,000 sponsor-funded prize pool ($100 from Irarrázaval, $200 from Corgea, $200 from an anonymous donor, $500 from Abnormal AI).
- **Scope**: Covers one live, real-world adversarial test of a single frontier model's (Opus 4.6) resistance to human-driven prompt injection via email, defended only by a short natural-language system-prompt instruction. Does NOT cover: controlled/automated attack benchmarks, other attack channels (file upload, tool outputs, web content), other models, or a rigorous accounting of attacker skill distribution among the ~2,000 participants. The challenge's own site publishes no attempt-by-attempt data — only the final binary outcome (uncompromised) plus Willison's secondhand numeric estimates (2,000 people, 6,000 attempts, $500 spend).

## Extracted Claims

### Claim 1: Zero of roughly 6,000 prompt-injection attempts by ~2,000 participants succeeded in extracting the protected secret from the Opus 4.6-powered OpenClaw instance
- **Evidence**: hackmyclaw.com's own outcome statement, corroborated by Willison's participant/attempt counts.
- **Confidence**: emerging (single real-world test, not independently audited or peer-reviewed, but the outcome is stated directly by the challenge operator with no incentive to under-report a break given the sponsor-funded prize)
- **Quote**: "no one was able to extract `secrets.env` before the challenge ended." (hackmyclaw.com)
- **Our assessment**: This is the headline empirical result. A zero-success rate across 6,000 adversarial attempts by a broad, self-selected public population is a meaningfully large sample for a live security challenge — far larger than typical single-team red-team engagements. The result should be read as "held against this specific population and channel," not as a general robustness proof; see Claim 7 for Willison's own caveat.

### Claim 2: The AI assistant's only defense was a short natural-language system-prompt instruction — roughly 10-20 lines telling it never to reveal the protected file — with no additional technical safeguards
- **Evidence**: hackmyclaw.com's description of the assistant's ("Fiu") configuration.
- **Confidence**: emerging (stated directly by the challenge operator; not independently verified against the actual deployed system prompt)
- **Quote**: "10-20 lines in the prompt telling Fiu to never reveal `secrets.env`." (hackmyclaw.com)
- **Our assessment**: This is the single most important architectural detail in the source, and it sharpens Claim 1 considerably. The zero-success result was achieved with what amounts to a bare content-based instruction — exactly the class of defense that role-confusion research (see Cross-References) argues is structurally insufficient against a determined attacker who can mimic privileged-text style. That such a lightweight defense held against 6,000 attempts is either evidence that current frontier-model training has meaningfully raised the bar for content-based defenses, or evidence that the ~2,000-person attacker population did not include enough attackers using the most effective known technique (see Claim 8, contradiction filed).

### Claim 3: Participants were given essentially unconstrained attack freedom — any prompt-injection technique or social-engineering approach was permitted, delivered via ordinary email body or subject line
- **Evidence**: hackmyclaw.com's description of the attack mechanism and allowed techniques.
- **Confidence**: emerging (self-reported challenge rules)
- **Quote**: "any prompt injection technique" or "creative social engineering within the email" (hackmyclaw.com)
- **Our assessment**: The breadth of permitted technique matters for how much weight Claim 1's result should carry. This was not a narrow test of one injection pattern — participants could combine social engineering with arbitrary injection framing, sent through a single unconstrained channel (email). That the defense held under an open-ended attack scope, not just a fixed test suite, strengthens the result somewhat, though it does not establish that any *specific* known high-efficacy technique (e.g., CoT Forgery per the role-confusion research) was actually attempted by a meaningful fraction of the 2,000 participants.

### Claim 4: Sustained attacker effort was substantial and had real-world side effects: participants spent roughly $500 in token costs collectively, and email volume was high enough to trigger a Google account suspension
- **Evidence**: Willison's numeric summary of the challenge, obtained via WebFetch of the source post.
- **Confidence**: anecdotal (secondhand figures relayed by Willison, not independently sourced to a published accounting from Irarrázaval)
- **Quote**: (no direct quote; see paraphrase in Our assessment — WebFetch-mediated summary reports "$500 spent on token costs" and "Google account suspension triggered by excessive inbound emails")
- **Our assessment**: These two data points are useful as effort proxies even without a formal methodology: token spend is a rough measure of how much LLM-assisted attack generation participants used against the target, and the account suspension indicates the volume of email traffic was large enough to trip standard anti-abuse infrastructure at Google — i.e., this was not a token effort by a handful of casual testers but a sustained, high-volume campaign.

### Claim 5: Willison frames the result as evidence that frontier-lab investment in anti-injection training is producing real, practical improvements in attack resistance
- **Evidence**: Willison's own editorial synthesis, connecting this result to a broader pattern he says he has observed.
- **Confidence**: anecdotal (editorial judgment from one practitioner, based on one data point plus unspecified personal observation — "something I've been seeing myself")
- **Quote**: "the effort the labs have been putting in to training their frontier models not to fall for injection attacks do appear effective in making these attacks much harder to pull off." (Simon Willison's blog, via WebFetch)
- **Our assessment**: This is the post's central interpretive claim, and it is explicitly hedged ("appear effective," "much harder to pull off" — not "solved" or "immune"). It should be read as a directional signal from a credible, experienced observer rather than as a quantified capability claim. It is the piece of this source most in tension with the corpus's existing theoretical account of why content-based defenses fail (see Cross-References, Contradicts).

### Claim 6: Willison cites OpenAI's GPT-5.6 system card as independent, cross-vendor corroboration that labs are actively training against injection attacks
- **Evidence**: Willison's reference to a specific section of OpenAI's GPT-5.6 system card (deploymentsafety.openai.com/gpt-5-6-preview/prompt-injection), obtained via WebFetch of the source post.
- **Confidence**: anecdotal (Willison's characterization of the system card's content; the system card itself was not independently fetched for this extraction)
- **Quote**: "a short section about that in today's GPT-5.6 system card" (Simon Willison's blog, via WebFetch, paraphrased reference — see Extraction Notes on quote confidence)
- **Our assessment**: The cross-vendor pattern (Anthropic's Opus 4.6 resisting the hackmyclaw challenge; OpenAI documenting its own anti-injection training investment in the same week) is the kind of corroboration that elevates a single anecdote toward an industry trend, though this extraction did not independently verify the GPT-5.6 system card's content — the Assayer should treat this claim as pointing to a citable primary source rather than as a verified fact in its own right.

### Claim 7: Willison explicitly declines to generalize the result to production safety guidance, still recommending against deploying irreversible-damage systems that rely on prompt-injection resistance alone
- **Evidence**: Willison's own stated caveat, directly following his positive framing of the result.
- **Confidence**: settled (this is Willison's own stated position, not an empirical claim requiring external validation — it is a direct quote of his recommendation)
- **Quote**: "I still wouldn't recommend deploying a production system where a prompt injection attack could cause irreversible damage though!" (Simon Willison's blog, via WebFetch)
- **Our assessment**: This caveat is load-bearing for how the guide should use this source. Willison is not arguing that model-layer resistance obviates architectural/environmental controls — he is arguing that model-layer resistance has measurably improved while still maintaining that irreversible-consequence systems need defense-in-depth. This aligns with, rather than contradicts, the corpus's existing "environmental controls first" guidance (see Cross-References, Corroborates) even though Claim 5's headline framing is in tension with the role-confusion paper's structural claim.

### Claim 8: The Hacker News discussion of this result is characterized by Willison as high-quality, skeptical, good-faith scrutiny rather than uncritical celebration
- **Evidence**: Willison's own characterization of the linked HN thread (news.ycombinator.com/item?id=48681687); this extraction attempted to independently fetch the HN thread but received an HTTP 429 (rate-limited) response and could not verify specific comment content.
- **Confidence**: anecdotal (Willison's characterization only; individual HN comments not independently verified for this extraction)
- **Quote**: "excellent, full of well-founded skepticism and good faith replies" (Simon Willison's blog, via WebFetch)
- **Our assessment**: That Willison — who is himself skeptical by habit about overclaiming AI capability results — flags the community response as appropriately skeptical is a mild secondary signal that the result was received as credible-but-limited by informed practitioners, not dismissed as flawed methodology nor treated as a definitive proof of injection immunity. The Assayer should independently re-fetch the HN thread if a more granular account of specific objections is needed for guide-writing.

### Claim 9: The challenge ended due to operational cost to the organizer, not because the defense was eventually broken
- **Evidence**: hackmyclaw.com's stated reason for closing the challenge.
- **Confidence**: emerging (stated directly by the challenge operator)
- **Quote**: "closed due to operational costs, with Fiu remaining uncompromised." (hackmyclaw.com, via WebFetch paraphrase — see Extraction Notes)
- **Our assessment**: This detail matters for interpreting Claim 1's zero-success result: the test was not run to a natural saturation point (e.g., attacker population exhaustion or a fixed time limit reached with declining attack rate) but was terminated for cost reasons while still receiving attack traffic. This means the true asymptotic success probability against a sufficiently large or persistent attacker population is unknown — the challenge demonstrates resistance to 6,000 attempts, not resistance to unbounded attempts.

## Concrete Artifacts

### Challenge Configuration (hackmyclaw.com)

```
HackMyClaw Challenge — Source: hackmyclaw.com (via Simon Willison,
simonwillison.net/2026/Jun/26/hack-my-ai-assistant/)

Organizer:        Fernando Irarrázaval (@cucho)
Target:            AI assistant "Fiu," built on OpenClaw framework,
                   running Claude Opus 4.6
Protected asset:   contents of `secrets.env` (described as "sensitive
                   credentials")
Defense:           10-20 lines of natural-language system-prompt
                   instruction telling Fiu never to reveal secrets.env
                   — no other technical safeguards disclosed
Attack channel:    email only (body or subject line)
Attack scope:      "any prompt injection technique" or "creative
                   social engineering within the email" — unrestricted
Prize pool:        $1,000 total
                     - $100 from Irarrázaval
                     - $200 from Corgea
                     - $200 from an anonymous donor
                     - $500 from Abnormal AI
Leaderboard:       none — competitive but unranked

RESULT (per Willison's summary):
  Participants:      ~2,000
  Attempts:          ~6,000
  Token spend:       ~$500 (collective, across participants)
  Side effect:       email volume triggered a Google account suspension
  Outcome:           0 successful extractions of secrets.env
  Closure reason:    operational cost to organizer, not a compromise
```

### Willison's Verbatim Framing (short excerpts, via WebFetch)

```
Source: simonwillison.net/2026/Jun/26/hack-my-ai-assistant/
Posted: 26th June 2026 at 6:33 pm
Tags: security, ai, prompt-injection, generative-ai, llms

Opening: "Fernando Irarrázaval ran a challenge on hackmyclaw.com to see
if anyone could leak secrets held by his OpenClaw test instance by
sending it email."

"This matches something I've been seeing myself: the effort the labs
have been putting in to training their frontier models not to fall for
injection attacks do appear effective in making these attacks much
harder to pull off."

"I still wouldn't recommend deploying a production system where a
prompt injection attack could cause irreversible damage though!"

References OpenAI's GPT-5.6 system card
(deploymentsafety.openai.com/gpt-5-6-preview/prompt-injection) as
same-week corroborating evidence of cross-vendor anti-injection
training investment.

Links to Hacker News discussion (news.ycombinator.com/item?id=48681687),
characterized as "excellent, full of well-founded skepticism and good
faith replies."
```

## Cross-References

- **Contradicts**: `blog-simonwillison-prompt-injection-role-confusion.md` (Claims 4, 5, 8) — filed as contradiction issue [#1443](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1443). That source's ICML 2026 research claims human red-teamers achieve "near-100%" attack success against frontier models by deliberately exploiting role confusion, and that Opus 4.5/GPT-5.4 still fail 11%/25% of the time against *automated* attacks as of May 2026 — concluding that content-based, model-layer injection defense is a "perpetual whack-a-mole game" absent genuine role perception. This source's 0/6,000 result against Opus 4.6, defended by nothing more than a short content-based system-prompt instruction (Claim 2), sits in direct tension with that structural pessimism. The gap could be explained by conditioning variables (newer model generation, a general public attacker population vs. red-teamers using a specifically-named technique, or a narrower success criterion — leaking one literal secret vs. a broader "attack success" metric) but the magnitude and opposing guide-relevant conclusions warrant the filed contradiction rather than a silent resolution here. Do not treat either source as settling the question until the contradiction is resolved.

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` (Claim 1, Claim 4) — that source documents AISI's finding that frontier-model *offensive* capability (Claude Mythos Preview) shows no saturation with increased token budget, implying attackers can keep buying more capability. This source is the mirror-image *defensive* data point: increased lab investment in anti-injection *training* (a fixed, non-token-budget-dependent defense) appears to be raising the bar in practice. Together they sketch both sides of the proof-of-work framing: attacker capability scales with attacker token spend, while defender resistance to a specific attack class (email-based injection) scales with lab training investment rather than per-deployment token spend.

- **Contrasts with** (not a formal contradiction — different attack surface, illustrative for guide framing): `failure-copilot-cowork-file-exfiltration.md` and `failure-meta-ai-instagram-account-takeover.md` document production failures where prompt injection or trivial social engineering succeeded completely (5/5 and effectively 1/1 respectively) against systems with architectural weaknesses — an unapproved email-send capability chained with pre-authenticated links (Copilot Cowork), and a support bot with unauthenticated account-recovery capability (Meta AI). This source's result is the inverse case: the *same class* of attack (email-based, social-engineering-assisted) failed completely against a system whose only defense was a system-prompt instruction, because the target had no analogous dangerous capability to abuse — Fiu could not be tricked into taking a harmful *action*, only (unsuccessfully) tricked into disclosing text it was told to protect. The guide should draw the distinction sharply: model-layer resistance to disclosing a secret is a different (and per this source, more tractable) problem than architectural resistance to an agent being induced into taking an irreversible or exfiltration-enabling *action*. This source provides no evidence about the latter.

- **Extends**: `blog-simonwillison-prompt-injection-role-confusion.md` — beyond the direct numerical tension (filed as a contradiction), this source adds a real-world, large-N field data point to a corpus that has so far relied primarily on controlled academic evaluation (ICML paper) and vendor-reported/third-party lab benchmarks (AISI) for prompt-injection resistance figures. It is the first source in the corpus reporting a live, crowd-sourced, non-institutional red-team result.

- **Novel**:
  - **First live crowd-sourced prompt-injection challenge result in the corpus.** Prior injection-resistance figures come from controlled academic studies (role-confusion paper) or lab/third-party benchmarks (AISI); this is the first "wisdom of an adversarial crowd" data point.
  - **First documented case in the corpus of a bare system-prompt instruction (10-20 lines, no other technical safeguard) surviving a large-scale (6,000-attempt), technique-unrestricted attack campaign.** This is a specific, falsifiable claim about the current practical floor for content-based defenses that no other corpus source quantifies at this attempt volume.
  - **First corpus reference to OpenAI's GPT-5.6 system card's prompt-injection section**, though not independently verified in this extraction (see Claim 6, Extraction Notes).
  - **First corpus data point on operational cost as a practical limiter on adversarial red-team challenge duration** (Claim 9) — a minor but real consideration for anyone designing a similar internal bug-bounty-style test.

## Guide Impact

- **Chapter 06 (Security and Threat Model)**: Add this source as a real-world counterpoint to the corpus's existing "model-layer defenses are structurally insufficient" framing (from the role-confusion research). The guide should present both results together, flagged via the filed contradiction (#1443), rather than citing either in isolation: current frontier-model training appears to substantially raise the practical bar for content-based injection defenses against broad, unstructured attacker populations (this source), while a research-driven, technique-specific attack approach may still achieve near-total success against the same model class (role-confusion paper). Guide text should avoid the false takeaway "prompt injection is basically solved for frontier models" — Willison's own caveat (Claim 7) should be quoted directly as the recommended framing: don't rely on model-layer resistance alone for irreversible-damage systems.

- **Chapter 06 (Security — defense-in-depth rationale)**: Use the sharp contrast between this source and the Copilot Cowork / Meta AI Instagram failure reports (see Cross-References) to make a specific, actionable point: the guide's existing recommendation for architectural/environmental controls (approval gates, capability restriction) is really about constraining what an agent can *do*, not primarily about preventing it from being fooled about what to *say*. This source suggests disclosure-resistance may be a more tractable model-layer problem than action-resistance — a distinction the guide does not currently draw explicitly.

- **Chapter 04 (Testing & Validation)**: Add the hackmyclaw.com challenge design (open-ended technique scope, single unrestricted channel, real financial stakes via a sponsor-funded prize pool, public crowd-sourced participation) as a candidate pattern for teams wanting a low-cost adversarial validation exercise for a specific narrow-scope defense (e.g., "does this agent ever reveal this specific piece of information"), while noting Claim 9's caveat that a challenge ending without a break is not proof of unlimited robustness — it proves robustness against the tested population and duration only.

## Extraction Notes

- **Willison post is thin (~200 words); hackmyclaw.com supplies the load-bearing detail.** The Willison post alone would not support a source note meeting the quality bar — most of the concrete, falsifiable detail in this note (defense mechanism, prize structure, attack channel, closure reason) comes from independently fetching hackmyclaw.com, per the Prospector's expectation that the Miner follow substantive linked pages.
- **WebFetch intermediary caveat**: Both simonwillison.net and hackmyclaw.com were fetched through WebFetch, which uses an AI summarization intermediary and — per its own stated policy — declines to reproduce full article text verbatim, instead returning short quoted fragments in response to targeted factual questions. All quotes in this note were obtained by asking WebFetch for short (under ~40-word), specifically-bounded quotations and cross-checking consistency across multiple fetch calls with different prompts; the short quotes returned were consistent across calls. The Assayer should spot-check the exact wording of the quotes marked "via WebFetch" against the live source URLs, particularly Claims 6 and 9 where the underlying text was paraphrased by the intermediary rather than returned as a clean verbatim excerpt (flagged accordingly in those claims).
- **Hacker News thread not independently verified**: The linked HN thread (news.ycombinator.com/item?id=48681687) returned an HTTP 429 (rate-limited) on fetch attempt and was not independently read. Claim 8 relies solely on Willison's characterization of the thread's tone; no specific HN comment content is quoted or attributed in this note.
- **GPT-5.6 system card not independently fetched**: Claim 6 relies on Willison's reference to the system card's existence and general content; the system card itself (deploymentsafety.openai.com/gpt-5-6-preview/prompt-injection) was not fetched for this extraction. Flagged as a citable-but-unverified pointer for future mining if a dedicated GPT-5.6 system card source is triaged separately.
- **Contradiction filed**: See Cross-References → Contradicts. Issue [#1443](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1443) filed against `blog-simonwillison-prompt-injection-role-confusion.md` per MINER.md §4a; no verdict is asserted in this note.
- **No other sub-pages followed**: hackmyclaw.com did not appear to link to further substantive sub-pages (e.g., a detailed writeup or leaderboard); the GPT-5.6 system card and HN thread were the only two additional links surfaced, and both are noted above as not independently fetched.
