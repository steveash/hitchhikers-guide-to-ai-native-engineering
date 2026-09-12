---
source_url: https://simonwillison.net/2026/Sep/7/creepy-crawlies/
source_type: blog-post
title: "Creepy crawlies"
author: Simon Willison (link-blog curation); quoted/primary subject Konstantin Ryabitsev (Linux Foundation IT infrastructure lead, maintainer of git.kernel.org)
date_published: 2026-09-07
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: settled
issue: "#3398"
---

# Creepy crawlies

> Simon Willison links to Konstantin Ryabitsev's operational report on AI-training
> web crawlers hitting git.kernel.org: legitimate traffic is now roughly 2% of all
> requests, 14-16 of the fleet's 90 CPU cores are permanently consumed rendering
> git commits as HTML for scrapers, and a proof-of-work challenge system (Anubis)
> that once stopped bots outright is now being solved by them at increasing
> difficulty levels — a quantified, first-party account of AI training-data
> acquisition as an infrastructure-cost externality.

## Source Context

- **Type**: blog-post — Willison's post is a ~50-word link-blog entry (his
  standard "quotation" format: one framing sentence, a blockquote excerpt, one
  sentence of his own reaction) that excerpts the TL;DR of a much longer,
  substantive primary source: Konstantin Ryabitsev's own post "Creepy crawlies"
  at `https://people.kernel.org/monsieuricon/creepy-crawlies`. Per MINER.md §1
  ("follow substantive linked pages"), Ryabitsev's full post was fetched
  directly and read in full; it is the primary basis for this extraction.
  Willison's post was independently verified via direct HTML fetch (not
  WebFetch's summarized pass) to confirm his blockquote is a verbatim, unedited
  excerpt of Ryabitsev's TL;DR paragraph.
- **Author credibility**: Konstantin Ryabitsev is the Linux Foundation's IT
  infrastructure lead and the maintainer of `git.kernel.org`, `lore.kernel.org`,
  and related kernel.org services — he is the first-party operator reporting
  metrics from his own production systems, not a third-party analyst. Simon
  Willison (creator of Django and Datasette, a `trusted-feed` source in this
  repo) contributes only curation and one sentence of his own reaction; the
  substantive authority and all data in this note originate with Ryabitsev.
  Ryabitsev's post is dated August 29, 2026 on kernel.org (`datetime="2026-08-29T05:33:07Z"`
  in the page's `<time>` element) — nine days before Willison linked to it on
  September 7, 2026.
- **Scope**: Covers git.kernel.org's own crawler-traffic problem specifically —
  request volume, CPU allocation, the Anubis proof-of-work challenge system's
  effectiveness over time, and the mitigation path Ryabitsev's team is taking
  (removing crawlable functionality). Does NOT cover: crawler behavior on other
  kernel.org services (e.g., `lore.kernel.org`'s separate anti-bot measures,
  documented elsewhere in this corpus), the training-data quality or legal
  status of scraped kernel commits, or any defensive tooling beyond Anubis and
  IP/ASN banning. Ryabitsev explicitly declines to offer a solution: "there are
  no simple solutions to the problem."

## Extracted Claims

### Claim 1: git.kernel.org spends more CPU cycles rendering commits for scrapers than on all legitimate access combined, including git clones, with 14 CPU cores across 5 geo-distributed nodes permanently dedicated to this
- **Evidence**: Ryabitsev's own TL;DR summary, opening the post, backed by an accompanying graph ("fig6-cpu-crawl-vs-clone.png") comparing CPU spent on crawler-driven HTML rendering versus legitimate `git clone` traffic.
- **Confidence**: settled (first-party operator report of the operator's own production metrics, not a third-party estimate)
- **Quote**: "TL;DR: we spend more CPU cycles rendering commits for scrapers than we spend on all other kinds of legitimate access, including git clones. At any one time, across 5 geo-distributed nodes, there are 14 CPU cores doing nothing but rendering git commits as html."
- **Our assessment**: This is the single most citable number in the post: a majority-of-load claim from the infrastructure owner, not an outside observer's inference. It establishes the core externality — AI training-data acquisition imposing a permanent, non-negotiated compute cost on a public good the acquirer does not pay for or maintain.

### Claim 2: Out of git.kernel.org's total capacity of 90 CPU cores across 5 geo-distributed nodes, 14-16 cores (on average ~20% of total capacity) are constantly consumed rendering commits for scrapers, in a spiky rather than flat pattern
- **Evidence**: Ryabitsev's own capacity accounting, given in the "How bad is it?" section, alongside a graph ("fig5-hits-vs-bytes.png") of hits versus bytes served.
- **Confidence**: settled (first-party capacity/utilization figures for the operator's own fleet)
- **Quote**: "you should know that out of the total of the 90 cores across 5 geo-distributed nodes, there are 14-16 cores that are constantly doing nothing but rendering commits for scrapers. On average, that's 20% of our entire capacity — except the swarms descend in waves and the actual graph is a lot more spiky than a 20% flatline."
- **Our assessment**: This is the fleet-wide denominator for Claim 1's absolute core count, and it adds an important nuance — the load is not smooth. A steady-state "20% overhead" framing would understate the operational risk; Ryabitsev is explicit that scraper traffic arrives in bursts ("swarms") that can push utilization well above the 20% average at any given moment, which is consistent with his separate observation that the system is not yet "overwhelmed" but is under a variable, adversarial load pattern.

### Claim 3: git.kernel.org receives about 6 million daily requests for individual commits, of which 66% are blocked by the Anubis proof-of-work challenge and 33% now solve the challenge and get through
- **Evidence**: Ryabitsev's own traffic-funnel data, illustrated with a graph ("fig8-funnel.png", "Anatomy of git.kernel.org requests").
- **Confidence**: settled (first-party traffic-funnel measurement from server logs)
- **Quote**: "Today, git.kernel.org receives about 6M daily requests demanding to see random commits. Of these, 66% are still immediately batted away with the Anubis challenge, but 33% are now solving the math and getting through to the main site — because apparently what we have to offer is worth spending a ton of cycles to calculate the Anubis challenge."
- **Our assessment**: This is direct evidence that a compute-cost anti-bot mechanism (proof-of-work) does not stop determined, well-resourced scrapers — it merely raises their cost, and a third of requests are still willing to pay it. This complicates any guide claim that positions proof-of-work challenges as a durable solution rather than a cost-raising delay tactic.

### Claim 4: With generous assumptions favoring legitimate traffic, only about 2% of git.kernel.org's total traffic is legitimate human/developer use — the remaining ~98% is scraper activity
- **Evidence**: Ryabitsev's own estimate, stated immediately after the traffic-funnel numbers in Claim 3, and explicitly caveated as uncertain in classification but generous toward the legitimate-traffic side.
- **Confidence**: emerging (Ryabitsev himself frames this as an estimate under "generous assumptions," not a hard measurement — he states directly beforehand that "it's impossible to tell with certainty which of these are bots and which are real humans")
- **Quote**: "With a bunch of generous assumptions, legitimate requests are only about 2% of git.kernel.org traffic — everything else are scrapers."
- **Our assessment**: The 2% figure is the most dramatic number in the post and the one most likely to be quoted out of context, so the caveat matters: Ryabitsev explicitly flags the classification uncertainty and states the assumptions are generous *toward* legitimate traffic (i.e., 2% is likely an upper bound on the legitimate share, not a precise measurement). This should be cited as "Ryabitsev's own generous-case estimate," not as an audited figure, distinct from the settled-confidence Claims 1-3 above which are direct log/capacity measurements.

### Claim 5: A proof-of-work challenge system (Anubis) that initially stopped bots completely has been progressively defeated as bots learned to solve increasingly difficult computational challenges, in an escalating arms race
- **Evidence**: Ryabitsev's own timeline: Anubis deployed roughly a year prior to the post; initially fully effective; bots began solving difficulty-4 challenges after a few months, prompting an increase to difficulty 5; bots are now solving difficulty 5 as well. Illustrated with a graph ("fig1-difficulty.png", "Anubis painfulness graph").
- **Confidence**: settled (first-party account of the operator's own deployed mitigation and its documented decay in effectiveness over roughly a year)
- **Quote**: "It was immediately extremely effective — the bots just gave up. [...] A few months later, the bots were back, solving difficulty 4. No problem, we said, let's raise difficulty to 5. [...] Then... the bots started solving difficulty 5."
- **Our assessment**: This is a concrete, dated case study of a specific proof-of-work anti-scraping mechanism losing effectiveness over time as the adversary's economics (or capability) improved enough to absorb higher compute costs. It directly corroborates the "arms race" framing already in the corpus (`blog-simonwillison-cybersecurity-proof-of-work.md`) but from the defender-cost side rather than the attacker-capability side: raising the difficulty also raises the cost paid by legitimate users ("Difficulty 5 takes a few seconds to solve on a mobile device, and the phone gets uncomfortably warm"), so the escalation is not free for the defender either.

### Claim 6: Web scrapers switched from crawling via efficient `git clone` to the least efficient method possible — rendering every commit as an individual HTML page and parsing it — because doing so lets them treat kernel commit history as "guaranteed LLM-free" training data with maximum URL-space coverage
- **Evidence**: Ryabitsev's own explanation in the "Why is git.kernel.org 'interesting' to crawlers" and "The stupidest way of doing it" sections, contrasting the trivial availability of `git clone` with the scrapers' actual behavior of requesting rendered HTML, diffs, and patches for every commit across every one of the 922 forks of linux.git.
- **Confidence**: settled (Ryabitsev's direct technical description of the scraping method actually observed against his own servers, though his characterization of the *motive* — training-data purity — is his own inference about the scrapers' goals, not something he can directly observe)
- **Quote**: "But no, let's in fact choose the stupidest possible way of doing it — by rendering everything as HTML commit by commit and then parsing it. [...] Unless, of course, you're a scraper, in which case you have, oh, several BILLION valid URLs you can scrape, only to get 922 duplicates of the same 1.48 million commits — which is exactly what the scrapers are doing."
- **Our assessment**: This is the most novel and specific technical claim in the post — it directly contradicts the Prospector's second triage comment's framing that this is a "naive HTML scraping ... when efficient alternatives exist" pattern driven by inefficiency, and instead attributes it to a rational-but-costly choice: `cgit`'s HTML rendering exposes derived views (diffs between arbitrary commits, patches, per-fork duplicates) that a raw `git clone` does not, generating what Ryabitsev estimates at "1.2 METRIC BAJILLION valid URLs just for a single fork of linux.git." From the scraper's perspective this may not be "stupid" so much as it is externalizing the rendering cost onto the server rather than doing the equivalent computation locally after a clone.

### Claim 7: Training an LLM on LLM-generated content is harmful to the resulting model ("digital prion disease"), which is why pre-AI-era public archives like kernel commit history are unusually valuable training targets
- **Evidence**: Ryabitsev's own stated rationale for why git.kernel.org specifically is targeted, presented as background/motive rather than a technical measurement.
- **Confidence**: anecdotal (Ryabitsev's own inference about scraper motive and a colloquial characterization of a training dynamic, not a cited study or measurement — no paper or benchmark is referenced)
- **Quote**: "Training an LLM on content produced by the LLM gives it the equivalent of a digital prion disease, so when a source is guaranteed to be LLM-free, like the entire history of kernel commits, it's worth its weight in gold as a source of training data."
- **Our assessment**: This names a mechanism (recursive-generation degradation, colloquially "model collapse") without citing evidence for it — it is stated as an accepted premise, not argued or sourced. This corpus does not otherwise contain a source note that examines model-collapse/synthetic-data-degradation claims directly, so this should be flagged as an assumed-true premise in Ryabitsev's argument rather than an independently verified fact if cited in the guide.

### Claim 8: Crawler evasion has escalated from user-agent spoofing, to IP-based blocking evasion, to ASN-level subnet fanning, to residential/mobile IP swarms via commercial "proxy SDK monetization" services (e.g., embedded in smart TV apps), each phase defeating the prior generation of defense
- **Evidence**: Ryabitsev's own chronological account of his team's defensive escalation and the crawlers' counter-escalation, across the "Block them" and "Enter... your TV?" sections, with an external link corroborating the smart-TV-proxy-SDK claim.
- **Confidence**: emerging (Ryabitsev's first-party defensive history is a settled account of what his team observed and tried; the "proxy SDK monetization... your TV is probably doing it" claim is corroborated by an external source he links to, but that source was not independently fetched as part of this extraction)
- **Quote**: "Suddenly, the crawlers were coming from millions of random residential or mobile IPs, all pretending to be random modern browsers. An IP like that would make 4-5 requests and then never show up in the logs again. [...] They descended like swarms of locust, hit hard and fast until the system fell over and then moved on to the next target until you recovered. Then, they returned. Rinse. Repeat."
- **Our assessment**: This is a specific, escalating threat-model narrative useful for a security/infrastructure chapter: each defensive tier (user-agent filtering → IP banning → ASN banning → proof-of-work challenges) was defeated by a corresponding evasion tier, and the current tier (residential/mobile proxy swarms making 4-5 requests each before disappearing) makes IP-based blocking specifically ineffective because individual source IPs are used too briefly and too few times each to justify the cost of banning them ("You just needlessly ballooned your firewall ruleset by adding IPs that would never be back").

### Claim 9: git.kernel.org is not yet at the point of user-visible service degradation from scraper load — the actual outages it experiences come from poorly designed CI systems performing simultaneous shallow-clones, not from scrapers
- **Evidence**: Ryabitsev's own operational assessment in the "How bad is it?" section, explicitly distinguishing scraper load (currently absorbed) from a separate, unrelated failure mode (CI misconfiguration).
- **Confidence**: settled (first-party operational assessment of the system's current failure modes)
- **Quote**: "At this point, we're not quite overwhelmed — if you visit git.kernel.org, it will likely be snappy and responsive. The thing that usually takes us down are not scraper bots, but poorly designed CI systems that try to do something stupid like shallow-clone stable.git from 20 different nodes, all at the same time."
- **Our assessment**: This is an important qualifier against over-dramatizing the scraper problem: Ryabitsev is careful to say the site currently remains responsive to real users, and that the actual incident-causing load pattern he's observed is a *different*, non-AI-related problem (CI misconfiguration doing redundant shallow clones). This distinction matters for a guide chapter drawing on this source — the "20% of capacity" figure (Claim 2) is a standing cost, not (yet) an outage cause, and conflating the two would overstate the claim.

### Claim 10: git.kernel.org's chosen mitigation is to remove crawlable functionality and gate expensive-to-run actions, at the cost of reduced functionality for anonymous users, while still promising downloadable access to all data for anyone who asks
- **Evidence**: Ryabitsev's own stated forward plan in the "Where does that leave us?" closing section.
- **Confidence**: settled (first-party statement of the operator's own planned/ongoing response)
- **Quote**: "In terms of what we're doing, we're turning off features to reduce the number of crawlable URLs and to gate off actions that are expensive for us to run. Expect to lose some functionality, at least when accessing our resources anonymously. [...] That said, we promise to still offer all of our data for download to anyone who asks. You just may have to jump through more hoops to get it."
- **Our assessment**: This is the concrete mitigation strategy, and it is notable that it is capitulation rather than a technical defeat of the scrapers: rather than finding a way to block bad actors while preserving full anonymous functionality, the operator is reducing the surface area available to *everyone*, including legitimate anonymous users, because distinguishing good from bad traffic at the edge has become infeasible. This is a real-world cost of the externality named in Claim 1 — legitimate users lose functionality because of scraper load they did not cause.

## Concrete Artifacts

### Full traffic and capacity figures (verbatim, from Ryabitsev's post, fetched directly via curl and parsed from the page's `e-content` HTML block)

```
Source: Konstantin Ryabitsev, "Creepy crawlies," people.kernel.org/monsieuricon/creepy-crawlies
(published 2026-08-29T05:33:07Z per the page's <time datetime> attribute)

Repository scale:
  - linux.git: ~1.48 million commits
  - ~922 forks of linux.git hosted on git.kernel.org
  - Estimated valid URL space: "1.2 METRIC BAJILLION valid URLs just for
    a single fork of linux.git" (author's own hyperbolic order-of-magnitude
    framing, not a literal count)

Fleet capacity:
  - Total: 90 CPU cores across 5 geo-distributed nodes
  - Consumed by scraper HTML rendering: 14-16 cores constantly (~20% average,
    spiky rather than flat)

Daily request funnel:
  - ~6,000,000 daily requests demanding to see random commits
  - 66% blocked immediately by the Anubis proof-of-work challenge
  - 33% solve the challenge and get through
  - ~2% of total traffic estimated as legitimate (generous assumptions)

Anubis difficulty escalation timeline (approximate, as narrated):
  - Deployment: ~1 year before the August 2026 post
  - Initial effectiveness: bots "just gave up" at default difficulty
  - ~"a few months later": bots solving difficulty 4 → raised to difficulty 5
  - Difficulty 5: "takes a few seconds to solve on a mobile device, and the
    phone gets uncomfortably warm" for legitimate users
  - Current state (as of the post): bots solving difficulty 5 as well

Crawler evasion escalation (chronological, as narrated):
  1. User-agent-based identification and fail2ban (bots spoofed UA)
  2. Per-IP banning (bots fanned out across subnets)
  3. ASN-level banning (bots moved to residential/mobile proxy swarms)
  4. Anubis proof-of-work challenge (bots learned to solve it; see above)
```

### Referenced external links (from Ryabitsev's post)

```
- Anubis proof-of-work challenge system: https://anubis.techaro.lol
- Smart-TV residential-proxy-SDK background: https://spur.us/blog/smart-tv-apps-residential-proxy-sdks
- WriteFreely (mentioned as the platform note for a different context on the site, not independently fetched)
```

### Willison's link-blog post (verbatim, fetched directly via curl, confirms the excerpt is unedited)

```
Source: https://simonwillison.net/2026/Sep/7/creepy-crawlies/, posted
7th September 2026 at 11:08 pm

"Creepy crawlies (via) Konstantin Ryabitsev discusses how bad the
"background radiation" of abusive crawlers has become from the
perspective of git.kernel.org, the official Git repository for the
Linux kernel:

  TL;DR: we spend more CPU cycles rendering commits for scrapers than
  we spend on all other kinds of legitimate access, including git
  clones. At any one time, across 5 geo-distributed nodes, there are
  14 CPU cores doing nothing but rendering git commits as html.

I worry about this a lot from the perspective of Datasette, which
serves a huge number of crawlable web pages."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 9 (Drew
  Breunig, quoted by Willison: "unless models reach the point of diminishing security
  returns, you still need to buy more tokens than attackers do" — i.e., symmetric
  cost declines don't resolve an adversarial allocation problem). This source's Claim 5
  (Anubis difficulty escalation being progressively defeated) is a concrete, dated,
  real-world instance of exactly that dynamic applied to anti-scraping proof-of-work
  rather than security hardening: raising the compute cost of the challenge did not
  create a durable advantage, because the adversary's resources scaled to absorb it.
- **Corroborates**: `blog-simonwillison-cloudflare-mcp-api-fallback.md` Claim
  (Concrete Artifacts → Final WAF Rule Expression section; that note documents
  Willison's own Cloudflare CAPTCHA rule narrowly targeting "the faceted search
  crawler pattern" on his own site). Both sources document the same practitioner
  (Willison, as site operator in that note; Ryabitsev, as infrastructure lead here)
  independently reaching for edge-level challenge/friction mechanisms (Cloudflare
  Managed Challenge; Anubis proof-of-work) as the practical response to abusive
  crawler traffic, at very different scales (a single WAF rule on a personal search
  endpoint vs. fleet-wide proof-of-work on a major open-source infrastructure
  project) — this source provides the larger-scale, longer-timeline case showing
  that such challenges are a cost-raising delay tactic, not a permanent fix.
- **Extends**: `blog-ronacher-content-for-contents-sake.md` Claim 10 (Armin
  Ronacher's argument that text-intake platforms need friction/"backpressure"
  mechanisms against AI-generated content flooding: "The fact that it was cheap
  for you to produce does not make it cheap for someone else to receive"). Ronacher's
  claim concerns AI-*generated* content flooding human-facing intake systems (issue
  trackers, comment sections); this source documents the mirror-image externality —
  AI *training-data acquisition* flooding infrastructure with request traffic. Both
  describe the same underlying asymmetry (cheap for the AI-side actor to impose cost,
  expensive for the human-run system to absorb it), applied to different layers
  (content moderation vs. server infrastructure).
- **Novel**: This is the first source in the corpus with first-party, operator-reported
  quantitative infrastructure-cost data for AI-training-data web scraping (CPU core
  counts, daily request volume, percentage of traffic that is scraper vs. legitimate,
  and a proof-of-work challenge's effectiveness decaying over a measured ~1-year
  timeline). Prior corpus sources touch on crawler/anti-bot topics only as a single
  WAF rule (`blog-simonwillison-cloudflare-mcp-api-fallback.md`) or a blocked-access
  aside (`blog-simonwillison-linus-torvalds-ai-debug-session.md`, where a `lore.kernel.org`
  page was inaccessible due to an anti-bot challenge, but the note does not explore the
  underlying cause). This source is also the first in the corpus to name the
  "digital prion disease" / recursive-training-degradation rationale (Claim 7) as a
  stated motive for scrapers preferentially targeting pre-AI-era public archives.

## Guide Impact

- **Chapter 06 (Security Threat Model)**: Ch06 currently has no coverage of
  infrastructure-level resource-exhaustion from AI-training-data scraping as a
  threat category distinct from traditional DoS (a targeted search for "crawl",
  "scrap", "bot", "DoS", "infrastructure" in `guide/06-security-threat-model.md`
  returned no matches). Recommend adding a specific subsection on "scraper load as
  an ambient infrastructure tax": cite Claims 1-2 (14-16 of 90 cores, ~20% average
  capacity, permanently consumed) as a concrete order-of-magnitude case study for
  teams that run or depend on publicly-crawlable infrastructure (docs sites, public
  git hosting, package registries), and Claim 5 (Anubis difficulty escalation being
  progressively defeated over ~1 year) as evidence that proof-of-work/CAPTCHA-style
  defenses raise attacker cost but do not provide durable blocking against
  well-resourced scraping operations — teams should budget for continuous defensive
  investment, not a one-time challenge deployment.
- **Chapter 06 (Security Threat Model)**: Add Claim 8's evasion-escalation timeline
  (user-agent spoofing → IP banning → ASN banning → residential/mobile proxy swarms)
  as a named case study of adversary adaptation outpacing a specific defensive
  measure at each tier, relevant to any guide discussion of defense-in-depth against
  automated/bot traffic generally, not just AI-training scrapers specifically.
- **Chapter 02 (Harness Engineering) or Chapter 03 (Verification) — data
  provenance**: Claim 7 (the "digital prion disease" premise — that LLM-free
  historical archives are unusually valuable training data because training on
  LLM-generated content degrades models) is relevant context for any guide passage
  that discusses training-data quality or provenance for AI systems teams might
  build, but should be cited as a stated, unproven premise in Ryabitsev's argument
  (per Claim 7's confidence rating), not as an established fact — this corpus does
  not yet contain a source note that independently evaluates model-collapse/
  synthetic-data-degradation claims.

## Extraction Notes

- Both the Willison link-blog post and Ryabitsev's primary source post were fetched
  directly via `curl` with a standard browser user-agent and parsed locally from the
  raw HTML (`<div class="entryContent">` for Willison's post; `<div class="e-content">`
  for Ryabitsev's post), rather than relying solely on WebFetch's summarized output —
  WebFetch's initial pass on Ryabitsev's post correctly surfaced the key figures but
  did not preserve exact punctuation/emphasis (e.g., the ALL-CAPS "AWFUL" and "METRIC
  BAJILLION" emphasis in the original), so all quotes in this note were verified
  against the locally-parsed HTML.
- Note the date discrepancy: Ryabitsev's post carries a kernel.org page timestamp of
  2026-08-29 (per its `<time datetime="2026-08-29T05:33:07Z">` element), while
  Willison linked to it on 2026-09-07 — a roughly nine-day gap. `date_published` in
  this note's frontmatter is set to Willison's link date (matching the issue's
  `source_url`), since that is the actual `source_url` of this note per the Miner
  task instructions; Ryabitsev's earlier publication date on the primary source is
  documented here and in Source Context for anyone tracing the underlying report.
- Did not follow the `spur.us` smart-TV-proxy-SDK link or the Anubis project site
  (`anubis.techaro.lol`) as full sub-page fetches — both are cited by Ryabitsev as
  supporting context for claims already extracted from his own text (Claim 8), and
  neither contains git.kernel.org-specific data that would add a new claim.
- No contradiction with any existing source note was identified. The Prospector's
  three triage comments on this issue characterize the scraping method as either
  "inefficient"/"stupidest way" (second comment) or don't address the mechanism at
  all (first and third comments); this note's Claim 6 provides the more complete
  picture directly from Ryabitsev's own text — the HTML-rendering approach exposes
  URL-space (diffs, per-fork duplicates) that a raw clone does not, which is a
  rational-if-costly choice given the "guaranteed LLM-free" motive of Claim 7, not
  simply "stupid" as Ryabitsev's own rhetorical framing suggests at a glance. This
  is a nuance within a single source, not a cross-source contradiction, so no
  contradiction issue was filed per MINER.md §4a.
- Confidence rated `settled` overall: the great majority of the post's substantive
  content (Claims 1, 2, 3, 5, 6, 9, 10) is first-party operator-reported metrics and
  operational history from the person who runs the affected infrastructure, which is
  about as strong an evidentiary basis as a single blog post can carry. The two
  claims resting on the author's own inference about scraper motive and cause
  (Claims 4 and 7) are individually rated `emerging`/`anecdotal` in their own
  entries; Claim 8's evasion history is rated `emerging` since its final element
  (proxy SDK monetization) relies on an unfetched external corroborating source.
