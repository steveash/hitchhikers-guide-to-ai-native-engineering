---
source_url: https://simonwillison.net/2026/Jul/26/relay-market/
source_type: blog-post
title: "An Inside Look at the Relay Market Powering Token Resellers and Fraud"
author: Simon Willison (link-blog post relaying Matt Lenhard's investigation, published on Vectoral)
date_published: 2026-07-26
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2316"
---

# An Inside Look at the Relay Market Powering Token Resellers and Fraud

> Simon Willison relays — and the underlying Vectoral investigation by Matt
> Lenhard (a former AI-gateway engineer) documents in detail — a mature,
> four-layer Chinese gray-market ecosystem that pools stolen/leaked/abused
> API credentials behind open-source proxy software (`one-api`, `new-api`)
> to resell frontier-model access at 85-98% discounts; the first corpus
> source to document the attacker/reseller side of LLM API abuse (as
> opposed to the vendor/defender-side cost-control features already in the
> corpus).

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a "link-blog" entry
  published July 26, 2026 at 7:30pm, tagged `ai`, `generative-ai`, `llms`,
  `llm-pricing`, `ai-ethics`, `ai-in-china`). The entry links to, and is
  substantively about, a longer investigative article — "An Inside Look at
  the Relay Market Powering Token Resellers and Fraud" by Matt Lenhard,
  published on Vectoral (`vectoral.com/blog/token-relay-market`, June 28,
  2026, 9-minute read, tagged `threat-research` and `llm-security`) — which
  itself surfaced via a Hacker News discussion Willison also links to
  (`news.ycombinator.com/item?id=49058993`). Per MINER.md §1 ("follow up to
  5 linked pages that seem substantive"), the Lenhard/Vectoral article was
  fetched and read in full, since Willison's own post is five short
  paragraphs that summarize and react to it — the substantive claims and
  evidence live in the linked article, not in Willison's commentary alone.
- **Author credibility**: Simon Willison is the creator of Django and one
  of the highest-signal independent AI tooling commentators (already the
  most heavily cited author in this corpus). In this post he is curator and
  commentator, not the investigator. The investigator, Matt Lenhard, states
  in the article's "My Story" section that he "first stumbled upon [token
  fraud] while working as a software engineer on an AI gateway" and that he
  faced this abuse directly before researching the broader ecosystem — a
  first-hand operational vantage point, not a secondhand report. His primary
  source is a Chinese-language V2EX forum thread ("A comprehensive guide to
  AI transfer station jargon," started by user `v2exgo`, who by Lenhard's
  account operates a relay at `terminal.pub` — a self-interested party
  disclosing/bragging about the ecosystem, not a neutral informant) that ran
  March 5-June 23, 2026 with ~35,000 views and 190 replies.
- **Scope**: Covers the reseller/relay ecosystem's market structure, the
  open-source software it runs on, named abuse/fraud methods, buyer
  motivations, and vendor/practitioner-side defensive recommendations —
  observed primarily through one forum thread plus the author's own
  prior first-hand experience running an AI gateway. Does NOT cover:
  independent corroboration of the forum's claims beyond the author's own
  cross-checking, any named enforcement action against a specific relay,
  or model-provider (Anthropic/OpenAI/Google) commentary on the article.
  All quantitative figures (discount percentages, "3.6 million visits a
  month," "258 people entered 401 tickets") originate from the forum thread
  or the author's own observation of relay-adjacent sites, not from
  provider-side telemetry.

## Extracted Claims

### Claim 1: A "relay" (a.k.a. "transfer station") is a service that proxies traffic to U.S. frontier models at a steep discount, with one documented package selling ~$3,333 of official Anthropic credit for 425 RMB — roughly a 97.8% discount
- **Evidence**: The article's "So What Is a Relay?" section, with the price
  derivation attributed in the "Sources" section to forum reply #50 by user
  `milkleeeeee`.
- **Confidence**: emerging (single forum-sourced pricing example, but a
  concrete and traceable one — the derivation is attributed to a specific
  named forum reply)
- **Quote**: "A relay — or "transfer station" — is essentially a service
  that proxies traffic to U.S. models, often at a deep discount. For
  example, one operator's price-comparison site listed a package that
  bought the equivalent of $3,333 worth of official Anthropic credit for
  425 RMB — roughly $0.13 of usage per $1 spent."
- **Our assessment**: The 97.8% figure (derived: $0.13 official-usage per
  $1 spent means the buyer pays about 2.2% of list price) is an extreme
  outlier discount, only possible if the underlying credentials themselves
  were obtained fraudulently (stolen cards, abused free trials) rather than
  purchased at any real cost by the relay operator — a legitimate reseller
  buying credits at list price could never sustain a 97.8% markdown. This
  number is the article's clearest single data point establishing that the
  supply side of this market is abuse-funded, not volume-discount-funded.

### Claim 2: A live-tracked table of named relay products shows a cluster of 20+ operators offering 85-98% discounts off official pricing, not just the one headline example
- **Evidence**: An embedded, apparently continuously-updated comparison
  table on the article page (a hydrated `ProviderPercentOffTable`
  component), ranked by discount.
- **Confidence**: emerging (author's own tracked/maintained data set;
  methodology for how "percent off" is computed per relay is not detailed
  in the prose)
- **Quote**: (no prose quote for the table itself; verbatim table data
  extracted in Concrete Artifacts below)
- **Our assessment**: This is the strongest evidence in the source that the
  market is not one anomalous listing but a competitive field of dozens of
  named operators (Now Coding, I Code Easy, Claude ZZ, Doro, UoCode,
  ZeroCode, AiYa, HongMaCC, and more) clustered tightly at the top of the
  discount range (97.8% down to ~91% within the top 18 entries alone). The
  tight clustering suggests a real, price-competitive secondary market with
  a going rate, not isolated fraud.

### Claim 3: The market has a four-layer structure — upstream card/account merchants, midstream account pools, downstream relays/transfer stations, and end-user buyers — though in practice operators often collapse the middle two layers
- **Evidence**: The article's "How the Market Works" section with dedicated
  subsections "Upstream," "Midstream," "Downstream," and "End users."
- **Confidence**: emerging (author's own synthesized taxonomy from forum
  observation, not an official industry classification)
- **Quote**: "The ecosystem runs four layers deep, from the merchants
  sourcing raw accounts down to the developers buying cheap tokens." /
  "In practice these layers blur. Many operators run both the pool and the
  relay, and the forum's own participants often use "pool" and "transfer
  station" interchangeably."
- **Our assessment**: The explicit acknowledgment that layers 2 and 3
  ("account pools" and "relays/transfer stations") blur in practice is an
  important caveat the article states itself — the four-layer model is a
  useful analytical frame but should not be presented in the guide as a
  rigid, universally-observed pipeline. The self-caveat also strengthens
  credibility: the author is not overselling the taxonomy's precision.

### Claim 4: Midstream account pools aggregate not just direct model-lab (OpenAI/Anthropic/Google) credentials but also accounts "reverse-engineered" from consumer coding-agent products like Kiro and antigravity — "anything that resells or exposes a model is a target"
- **Evidence**: The "Midstream" subsection, describing pool inventory
  composition.
- **Confidence**: emerging (author's own characterization of forum
  discussion content)
- **Quote**: "The inventory isn't only model-lab accounts. Alongside direct
  OpenAI, Anthropic, and Google credentials are accounts harvested from the
  application layer." / "Much of the forum's activity centers on
  "reverse-engineered" access to tools like Kiro and antigravity, which are
  consumer products, not lab APIs. To a pool, it makes no difference
  whether a token comes from a lab or from an app built on one; anything
  that resells or exposes a model is a target."
- **Our assessment**: This is a specific and previously-undocumented (in
  this corpus) escalation of the threat model: the abuse surface is not
  limited to direct provider API keys but extends to any consumer-facing
  coding-agent product whose backend model access can be reverse-engineered
  and re-exposed. Any team building an agentic product with an embedded
  model credential (not just teams issuing raw API keys) is a candidate
  target for this ecosystem.

### Claim 5: Almost every relay documented runs on one of two open-source, OpenAI-compatible gateway projects — `one-api` or its more actively developed fork `new-api` — used to pool provider API keys behind a single proxied endpoint with usage-based, multiplier-priced billing
- **Evidence**: The "The Software Behind the Relays" section, with direct
  links in Willison's post to the GitHub repos (`github.com/songquanpeng/one-api`
  and `github.com/QuantumNous/new-api`) and a detailed mechanism description
  in the Vectoral article.
- **Confidence**: settled (both sources — Willison's post and the underlying
  article — independently state this same fact, and it is a verifiable,
  named-software claim, not an interpretive one)
- **Quote** (Willison's post): "The software they are using for these
  proxies is open source - mostly one-api and its more actively developed
  fork new-api, both legitimate API proxy products which can be used to
  load balance requests across a pool of API credentials." **Quote**
  (Vectoral article): "Almost every relay I've looked at runs on one of two
  open-source projects: one-api or new-api." / "Both are OpenAI-compatible
  gateways. An operator deploys the panel and adds a set of channels (渠道).
  Each channel represents a provider plus a pool of API keys. The panel
  exposes a single endpoint that matches the OpenAI API, so buyers just
  point their existing SDK at the relay's URL. On every request it pulls a
  key from the pool, forwards it upstream, returns the response, and
  deducts quota priced by usage times a multiplier (倍率)."
- **Our assessment**: This is the single most concrete, actionable, and
  independently-corroborated claim in the source (stated near-identically
  by both Willison and Lenhard). Both authors are careful to note the
  software itself is legitimate and widely self-hosted by companies for
  benign purposes (team quota/spend tracking across their own accounts) —
  the abuse is in what credentials are loaded into the channel pool, not in
  the tool. The article states `one-api` turns up roughly four times as
  often as `new-api` among tracked relays, with `new-api` differentiated
  mainly by shipping self-service payment/recharge and additional media
  models — i.e., the fork more purpose-built for running a commercial
  reseller storefront.

### Claim 6: The article draws an explicit line between legitimate self-hosted use of this proxy software and criminal misuse — "a relay crosses the line when its channels are stocked with stolen, leaked, or pooled keys instead of the operator's own, and when it resells that access against the providers' terms"
- **Evidence**: Closing sentence of "The Software Behind the Relays" section.
- **Confidence**: settled (explicit, direct statement of the author's own
  distinguishing criterion)
- **Quote**: "There's nothing inherently illicit about the software. one-api
  and new-api are neutral, legitimate tools. Plenty of companies self-host
  them to put their own accounts behind a single gateway with team quotas
  and spend tracking. A relay crosses the line when its channels are
  stocked with stolen, leaked, or pooled keys instead of the operator's own,
  and when it resells that access against the providers' terms."
- **Our assessment**: This is a useful, precise framing for the guide: the
  risk is not "avoid this open-source software category" but "understand
  that a credential-pooling gateway is dual-use, and the same architecture
  that lets a company aggregate its own accounts safely is exactly the
  architecture a relay operator uses to launder stolen credentials." A
  guide reader evaluating or self-hosting `one-api`/`new-api` for
  legitimate internal use should not read this source as a condemnation of
  the tool itself.

### Claim 7: Five named abuse/fraud methods feed the relay supply chain: free-trial abuse (mass account creation to claim free credits), chargeback attacks (recouping spend after usage, or using stolen cards from the start), prepaid-card exploitation, "open inference" (proxying traffic through unprotected support chatbots), and "denial of wallet" (flooding concurrent requests purely to burn provider spend, with no resale/financial motive)
- **Evidence**: The article's "The Methods" section, a five-item list.
- **Confidence**: settled (explicit, itemized first-party taxonomy from the
  author, though the underlying prevalence of each method individually is
  not quantified)
- **Quote**: "Free-trial abuse. Abusers automate account creation en masse
  to claim free credits, then proxy that traffic back to their own end
  users." / "Chargeback attacks. Abusers charge back their spend after the
  usage period ends to recoup their costs — or use stolen cards from the
  start." / "Prepaid cards. Abusers fund accounts with prepaid cards capped
  at a set limit." / "Open inference. Any support chatbot without strict
  guardrails is ripe for having traffic proxied through it." / "Denial of
  wallet. Not strictly a relay technique, but an emerging form of abuse I've
  been tracking: attackers fire off a flood of concurrent requests purely to
  burn a provider's spend. It can be facilitated by any of the methods
  above. The difference is there's no financial motive."
- **Our assessment**: "Denial of wallet" as a named, motive-distinct attack
  (pure cost infliction, not resale profit) is new terminology to this
  corpus and a meaningfully different threat than the other four
  resale-motivated methods — it means cost-cap and rate-limiting defenses
  (already documented elsewhere in the corpus, see Cross-References) need
  to guard against attackers with no economic incentive to stay under any
  particular threshold, since they are not trying to preserve a resale
  margin.

### Claim 8: Buyers' three main stated motivations are cheap tokens, bypassing geo-restrictions, and acquiring output data for commercial model distillation — with forum commentary describing distillation-focused reselling as "a multi-billion RMB industry chain" where "many big players earn hundreds of thousands a day"
- **Evidence**: The "Who Are the Buyers?" section, including two directly
  quoted (and translated) forum replies attributed to user `@v2exgo`.
- **Confidence**: anecdotal (self-reported forum claims about distillation
  revenue, unverified by the author against any external financial data)
- **Quote**: "The three main use cases seem to be cheap tokens, getting
  around geo-restrictions and model distillation." Forum reply #38 (quoted
  and translated in the article): "Distillation uses Claude/CodeX models to
  train domestic models. There are intermediaries that specialize in
  distillation and can provide relevant evidence, but I can't name specific
  domestic companies. Anyway, companies with strong programming capabilities
  are all distilling Claude; it's a multi-billion RMB industry chain, and
  many big players earn hundreds of thousands a day." Forum reply #129: "It's
  not just true — many distillers in the industry have made millions."
- **Our assessment**: The "multi-billion RMB industry chain" and
  "hundreds of thousands a day" figures are a single anonymous forum
  participant's unverified claims, not measured data — the author himself
  frames this section as "a few relevant quotes from the forum," signaling
  he is presenting testimony, not confirmed fact. Treat this as directional
  color on motive (distillation is a real, discussed use case) rather than
  a quantitative claim the guide should cite as settled.

### Claim 9: The market is mature and commercially normalized — price-comparison sites, affiliate programs, and gateway products exist, and the ten highest-traffic relays the author tracks pull a combined 3.6 million visits a month
- **Evidence**: The "A Growing and Maturing Market" section.
- **Confidence**: emerging (author's own tracked traffic data across
  relays; methodology for the traffic measurement is not disclosed)
- **Quote**: "I was surprised by how mature the market already is. There
  are price-comparison sites for the relays, affiliate programs, and even
  gateway products. On the forums, consumer demand looks just as strong.
  And these aren't fringe operations: the ten highest-traffic relays we
  track pull a combined 3.6 million visits a month between them." / "My
  hunch is that things get worse for the application layer from here. As
  Anthropic and others roll out KYC controls and identity verification, the
  abuse won't disappear, it will just move somewhere else."
- **Our assessment**: The forward-looking claim ("things get worse for the
  application layer... abuse won't disappear, it will just move somewhere
  else") is explicitly labeled "my hunch" by the author — an opinion, not a
  finding. It is nonetheless a relevant framing for the guide's threat
  model: provider-side identity verification is presented here as a
  displacement, not elimination, of the abuse surface, pushing pressure
  toward whatever layer (application-level credentials, consumer product
  reverse-engineering per Claim 4) is least protected next.

### Claim 10: One relay-adjacent site (hvoy.ai) runs a daily provably-fair lottery giving away fifty $100 API keys, using a cryptographic fairness scheme (Bitcoin-block-hash seed, Partial Fisher-Yates shuffle, published entry snapshot) borrowed from crypto-gambling sites
- **Evidence**: The "They're Raffling Off Keys Now" section, with specific
  observed participation numbers from one draw.
- **Confidence**: emerging (author's direct observation of one specific
  site and one specific day's draw)
- **Quote**: "The site — hvoy.ai, which otherwise bills itself as a relay
  authenticity checker and price-comparison tool, gives away fifty $100 API
  keys every single day. You earn entry credits from a daily check-in, spend
  20 credits per ticket, and can buy up to three tickets a round. On the day
  I looked, 258 people had entered 401 tickets for the fifty keys." / "The
  part that got me is the fairness theater. The draw is provably fair — the
  same cryptographic scheme legitimate crypto-gambling sites use to prove
  they didn't rig the result. The random seed is the hash of the latest
  Bitcoin block, winners are picked with a Partial Fisher-Yates shuffle, and
  the full list of entries is published as a snapshot before the draw."
- **Our assessment**: This is the article's clearest illustration of Claim
  9's "maturity" argument in concrete, verifiable-in-principle form (a
  named site, a specific mechanism, a specific day's participation count) —
  it is qualitatively different from the more anecdotal forum-quote
  evidence elsewhere in the piece. The detail is colorful but has limited
  direct guide relevance beyond reinforcing that this ecosystem has
  develop real consumer-facing product polish, not just ad hoc reselling.

### Claim 11: The author's recommended defenses are layered across three stages matching how abuse travels — account creation (raise cost of entry, watch payment signals, watch behavioral signals, cluster accounts, monitor for spend anomalies), and damage control (enforce spend caps/locks/concurrency limits per account, reserve budget for in-flight requests, start new accounts with low caps that grow with age/verification, add step-up friction like CAPTCHA when risk rises mid-session, and throttle caught abusers quietly rather than with a clean error)
- **Evidence**: The "How Providers Can Defend Themselves" section, with two
  bulleted lists.
- **Confidence**: emerging (practitioner recommendations from the author's
  own experience fighting this abuse at an AI gateway company, not a
  vendor's documented feature set or independently validated best-practice
  standard)
- **Quote**: "I've talked to many companies facing this, and the truth is
  that there's no clean fix. Fraud is a constant cat-and-mouse game." /
  "Raise the cost of entry. Make accounts hard to create in bulk and cap
  what a fresh one can spend. Check for browser-based automation signals.
  Any client-side detection can be bypassed, but every bit of friction
  raises the attacker's cost." / "Reserve budget for every in-flight
  request, so concurrent calls can't blow past your limit." / "And when you
  do catch someone, throttle quietly. A clean error just tells the attacker
  which signal to fix before they come back." / "None of this stops the
  abuse for good. But if you make attacking your own service expensive
  enough that the numbers stop working, they'll try to find an easier
  target."
- **Our assessment**: "Reserve budget for every in-flight request, so
  concurrent calls can't blow past your limit" is a materially stronger
  recommendation than the "soft cap" (check-at-request-start, in-flight
  requests can overshoot) design documented as the cross-vendor norm
  elsewhere in this corpus (see Cross-References) — Lenhard is
  recommending reservation/hold-based accounting specifically to close the
  overshoot gap that Vercel's and GitHub Copilot's shipped products do not
  close. "Throttle quietly" (vs. a clean rejection error) is a distinct,
  previously undocumented-in-corpus adversarial-response tactic: it treats
  the error message itself as information leakage that helps an attacker
  iterate faster.

### Claim 12: The V2EX forum thread that is the article's primary source ran March 5-June 23, 2026, drew roughly 35,000 views and 190 replies, and was started by a user (`v2exgo`) who, per the author, operates a relay at `terminal.pub` — i.e., the primary source is a self-interested market participant, not a neutral or adversarial informant
- **Evidence**: The "Sources" section.
- **Confidence**: settled (explicit sourcing disclosure by the author)
- **Quote**: "All quotes are translated from a V2EX thread in the site's
  Programmers section, "A comprehensive guide to AI transfer station
  jargon," started by the user v2exgo (who operates the relay at
  terminal.pub). The thread ran from March 5 to June 23, 2026 and drew
  roughly 35,000 views and 190 replies."
- **Our assessment**: This sourcing disclosure is a meaningful caveat the
  Assayer and Smith should weigh: the primary informant for pricing,
  buyer-motivation, and revenue claims (Claims 1, 2, 8) is a relay operator
  with a plausible incentive to either inflate the market's scale (marketing
  for demand) or normalize the practice (reputational cover) rather than a
  disinterested researcher or a victim/enforcement source. This does not
  invalidate the claims, but it downgrades appropriate confidence from
  "settled" to "emerging"/"anecdotal" for anything traceable specifically
  to forum testimony rather than the author's own direct observation
  (e.g., the hvoy.ai lottery in Claim 10, which the author observed
  directly, warrants higher confidence than the distillation-revenue
  forum quotes in Claim 8).

## Concrete Artifacts

### Willison's full commentary (verbatim, from direct HTML fetch of simonwillison.net/2026/Jul/26/relay-market/)

```
"An Inside Look at the Relay Market Powering Token Resellers and Fraud (via)
Fascinating investigation by Matt Lenhard into the market that has grown up
around reselling LLM tokens at a discount by pooling API keys from various
sources.

This looks to be mostly a thing in China. Resellers sell access to an LLM
proxy that offers significant discounts on regular API pricing, which they
achieve by abusing free trials, proxying through unprotected support bots,
or sometimes through stolen credit cards or chargeback attacks.

The software they are using for these proxies is open source - mostly
one-api and its more actively developed fork new-api, both legitimate API
proxy products which can be used to load balance requests across a pool of
API credentials.

The buyers are seeking cheap tokens, avoiding geo-restrictions, and in some
cases collecting data for model distillation.

I've been cautious about exposing my own LLM-driven applications publicly
out of fear of abuse leading to big token bills. The existence of this
marketplace makes me even more cautious: there's now an entire ecosystem
that can profit from finding a new unprotected endpoint to exploit.

LLM vendors really need to get better at offering strict caps for their API
keys. I want my LLM apps to stop working the moment they hit a dollar
threshold I've set for a period of time.

Here's the (Chinese language) forum thread that served as the principal
source for Matt's article."

Tags: ai, generative-ai, llms, llm-pricing, ai-ethics, ai-in-china
Posted: 26th July 2026 at 7:30pm
Linked article: https://vectoral.com/blog/token-relay-market
Linked forum thread: https://www.v2ex.com/t/1196011
Linked HN discussion: https://news.ycombinator.com/item?id=49058993
```

### Four-layer market structure (verbatim excerpts, from vectoral.com/blog/token-relay-market, "How the Market Works")

```
Upstream: "Sitting at the top are the card merchants (卡商) and account
merchants (号商). They sell virtual credit cards designed to pass U.S. and
European billing checks, along with bulk-registered accounts."

Midstream: "In the middle sit the account pools (账号池). A pool aggregates
dozens or hundreds of upstream accounts, manages their authentication
tokens and rate limits, handles failover when accounts get flagged, and
exposes a single API surface that downstream relays can consume."

Downstream: "Downstream sit the relay / transfer stations themselves — the
consumer-facing layer. They wrap the pool's API in a clean Chinese-language
product, handle billing and invoicing, run customer-support WeChat groups,
and compete on price."

End users: "At the bottom are individual Chinese developers, small
startups, and mid-sized SaaS companies hunting for cheap inference — as
well as some larger commercial buyers using the infrastructure for model
distillation."
```

### Named relay discount table (verbatim data extracted from the article's embedded `ProviderPercentOffTable` component, top 18 of the tracked list, ranked by percent off official pricing)

```
Now Coding:    97.8%
I Code Easy:   97.1%
Claude ZZ:     96.6%
Doro:          96.4%
UoCode:        96.3%
ZeroCode:      94.9%
AiYa:          94.9%
HongMaCC:      94.2%
Right Code:    94.1%
BUZZ:          94.1%
OneDayAI:      94.1%
17NAS:         93.4%
TiMi CC:       92.7%
Xcode Best:    92.3%
Spark Code:    92.2%
Fox Code:      92.2%
BMAI:          91.2%
Claude API:    91.2%

Source: vectoral.com/blog/token-relay-market, embedded price-comparison
table under "So What Is a Relay?" (component name ProviderPercentOffTable
in the page's client-side JSON payload; table continues beyond the top 18
extracted here).
```

### Abuse methods (verbatim, from "The Methods" section)

```
- Free-trial abuse. Abusers automate account creation en masse to claim
  free credits, then proxy that traffic back to their own end users.
- Chargeback attacks. Abusers charge back their spend after the usage
  period ends to recoup their costs — or use stolen cards from the start.
- Prepaid cards. Abusers fund accounts with prepaid cards capped at a set
  limit.
- Open inference. Any support chatbot without strict guardrails is ripe
  for having traffic proxied through it.
- Denial of wallet. Not strictly a relay technique, but an emerging form
  of abuse I've been tracking: attackers fire off a flood of concurrent
  requests purely to burn a provider's spend. It can be facilitated by any
  of the methods above. The difference is there's no financial motive.

Source: vectoral.com/blog/token-relay-market, "The Methods" section
```

### Defense recommendations (verbatim, from "How Providers Can Defend Themselves")

```
Account-creation stage:
- Raise the cost of entry. Make accounts hard to create in bulk and cap
  what a fresh one can spend. Check for browser-based automation signals.
  Any client-side detection can be bypassed, but every bit of friction
  raises the attacker's cost.
- Watch the money. Flag prepaid cards, virtual cards, mismatched billing
  info, and small card-testing charges.
- Watch the behavior. Look for patterns no real user produces: time from
  registration to first token, the model selected, prompt relevance (where
  you can measure it), account age, and IP signals (proxy, VPN, country).
- Cluster the accounts. Watch for IP sybils and shared device fingerprints
  that tie supposedly-separate accounts back to one operator.
- Monitor for cost anomalies. Setup monitors and alerts on AI spend as a
  failsafe, so that you can flip things off if abuse does start.

Damage-control stage (assume some abuse gets through anyway):
- Enforce spend caps, spend locks, and concurrency limits per account.
- Reserve budget for every in-flight request, so concurrent calls can't
  blow past your limit.
- Start new accounts with low caps; let them earn higher limits with age
  and a verified card.
- If an account's risk rises mid-session, add friction like a CAPTCHA or an
  additional form of identity verification.
- And when you do catch someone, throttle quietly. A clean error just
  tells the attacker which signal to fix before they come back.

Source: vectoral.com/blog/token-relay-market, "How Providers Can Defend
Themselves" section
```

## Cross-References

Cross-reference verification notes: `blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-simonwillison-uber-caps-usage.md`, and `docs-ghaw-rate-limiting-controls.md`
were re-read in full during this extraction (MINER.md §4b); every claim
number cited below was located and confirmed against that note's own
numbered `### Claim N:` headings in document order before writing this
section.

- **Corroborates**:
  - `blog-simonwillison-uber-caps-usage.md` Claim 4: Willison's own
    commentary here — "LLM vendors really need to get better at offering
    strict caps for their API keys. I want my LLM apps to stop working the
    moment they hit a dollar threshold I've set for a period of time" —
    expresses the exact same cost-governance preference (a hard,
    provider-enforced dollar ceiling) that he separately praised as
    "a rational policy response to over-spending" when Uber implemented it
    organizationally. This source shows Willison wants the same discipline
    applied one level down: at the API-key/vendor level, not just the
    org-policy level.
  - `blog-vercel-ai-gateway-api-key-budgets.md` Claim 1 and Claim 4: this
    source's naming of "an entire ecosystem that can profit from finding a
    new unprotected endpoint to exploit" is a concrete, attacker-side
    instantiation of exactly the risk category Vercel's own changelog names
    as motivation for shipping API-key budgets ("Autonomous workflows that
    can loop or fan out without supervision," "Demos and prototypes that
    could catch unexpected traffic if shared or shipped"). Willison's
    explicit wish ("I want my LLM apps to stop working the moment they hit
    a dollar threshold") is, in substance, already a shipping feature per
    that note's Claim 1 ("Set a spend cap on any key, and AI Gateway
    rejects further requests on that key once the limit is exceeded") —
    though that note's Claim 2 documents this as a soft cap (checked at
    request start, so an in-flight request can still overshoot), which is
    a meaningful gap against Claim 11 here's stronger recommendation to
    "reserve budget for every in-flight request."

- **Extends**:
  - `docs-ghaw-rate-limiting-controls.md` Claim 8 (per-user `rate-limit`
    frontmatter field for GitHub Agentic Workflows): that source documents
    rate-limiting as a defense against internal/authenticated-user trigger
    abuse inside one platform's workflow system. This source extends the
    same "unprotected endpoint gets exploited" threat model to the broader,
    adversarial, profit-motivated external ecosystem — an organized market
    of relay operators specifically hunting for exposed LLM credentials
    and endpoints, rather than a single over-eager internal user. The
    defenses in Claim 11 here (behavioral/IP clustering, spend-anomaly
    monitoring, step-up friction) are a materially more adversarial-grade
    playbook than a simple per-user request-count throttle.
  - `blog-vercel-ai-gateway-api-key-budgets.md`: that note documents the
    shipped, vendor-side spend-cap *mechanism*; this source documents the
    attacker-side *motivation and method* that makes such a mechanism
    necessary in the first place — together they give the guide both the
    "why you need this control" (this source's threat actors and their
    economics) and the "here is a control you can turn on today" (Vercel's
    feature).

- **Contradicts**: None identified and no MINER.md §4a contradiction issue
  filed. No existing source note makes a claim about LLM API abuse
  economics, relay software, or reseller markets that this source
  materially opposes — this is a new threat-model topic for the corpus
  (see Novel, below), not a disagreement with existing coverage.

- **Novel**:
  - **First attacker/reseller-side documentation of LLM API abuse in the
    corpus**: every existing corpus source touching cost caps or rate
    limiting (`blog-vercel-ai-gateway-api-key-budgets.md`,
    `blog-simonwillison-uber-caps-usage.md`, `docs-ghaw-rate-limiting-controls.md`,
    `docs-github-copilot-cli-sdk-session-credit-limits.md`) documents the
    vendor or organizational defensive side. This is the first source
    documenting the organized, profit-motivated attacker/reseller side —
    a four-layer market with named products, tracked pricing, and
    documented recruitment/participation mechanics (Claims 1-3, 9-10).
  - **Named open-source relay software (`one-api`, `new-api`) as a
    dual-use credential-pooling gateway being repurposed for resale
    fraud** (Claims 5-6): not documented in any existing corpus source.
  - **"Denial of wallet" as a named, motive-distinct attack category**
    (Claim 7): no-financial-motive cost-infliction attacks are not named
    or discussed in any existing corpus source on cost controls or rate
    limiting.
  - **Consumer coding-agent products (not just raw provider API keys) as
    a credential-harvesting target** (Claim 4): the Kiro/antigravity
    reverse-engineering detail extends the abuse surface beyond what any
    existing corpus cost-control source addresses (those all assume the
    credential being protected is a provider API key or gateway key, not
    a consumer product's embedded backend access).
  - **"Reserve budget for in-flight requests" and "throttle quietly rather
    than reject cleanly" as named countermeasures** (Claim 11): both are
    more specific and more adversarially-aware than the soft-cap,
    reject-with-error designs documented in the corpus's existing
    vendor-feature sources.

## Guide Impact

- **Chapter 06 (Security Threat Model)**: Add this source as the corpus's
  first documented attacker-side threat actor profile for deployed LLM
  applications — an organized, price-competitive resale market (not just
  opportunistic individual abuse) that actively hunts for unprotected
  endpoints and pooled/leaked credentials, extending to consumer
  coding-agent products (Claim 4), not only raw API keys. Pair with the
  existing vendor-side cost-cap coverage (`blog-vercel-ai-gateway-api-key-budgets.md`,
  `blog-simonwillison-uber-caps-usage.md`) to give the guide both "why this
  matters" (this source) and "here's the shipped control" (Vercel).

- **Chapter 06 (Security Threat Model) — layered defenses**: Add Claim 11's
  three-stage playbook (raise cost of entry at account creation; watch
  payment/behavioral signals; damage-control via per-account spend
  caps/locks/concurrency limits, in-flight budget reservation, and quiet
  throttling on detection) as a concrete practitioner checklist,
  explicitly noting the gap this source identifies against currently
  shipped vendor soft-caps: "reserve budget for every in-flight request"
  goes further than the check-at-request-start soft-cap design documented
  in `blog-vercel-ai-gateway-api-key-budgets.md` Claim 2.

- **Chapter 04 (Cost Management)**: Add "denial of wallet" (Claim 7) as a
  named risk category distinct from resale-motivated abuse — cost-control
  guidance should note that some attackers have no profit motive to stay
  under any particular spend threshold, so rate limits and spend caps must
  be sized assuming adversarial intent to maximize cost, not assuming
  attackers will self-limit for their own margin.

## Extraction Notes

1. **WebFetch's initial summarized output was cross-checked against
   directly-fetched raw HTML.** An initial WebFetch pass on both the
   Willison post and the Vectoral article produced paraphrased summaries
   consistent in substance with the underlying text, but per MINER.md §2a
   this note does not rely on that AI-intermediated output for any `Quote`
   field. Both pages were re-fetched via direct `curl` (Willison's post:
   `https://simonwillison.net/2026/Jul/26/relay-market/`; the Vectoral
   article: `https://vectoral.com/blog/token-relay-market`), and every
   quote above was copied character-for-character from that raw HTML
   (including the embedded discount-table JSON payload for Claim 2/Concrete
   Artifacts). The two independent WebFetch passes and the raw HTML were
   consistent with each other in every case checked.
2. **One linked page followed, per MINER.md §1.** Willison's post's
   primary substantive link — Matt Lenhard's Vectoral article — was
   followed and read in full, since it is where nearly all of the specific
   claims, quotes, and data in this note originate; Willison's own post is
   five short paragraphs of summary and reaction. The article's own primary
   source (the V2EX forum thread) was not independently fetched or
   translated — this note relies on the article's own translated
   quotations of that thread (Claim 8) and its own sourcing disclosure
   about the thread (Claim 12). The linked Hacker News discussion
   (`news.ycombinator.com/item?id=49058993`) was not followed; it is a
   discussion-of-the-article, not a distinct primary source.
3. **Confidence calibration: emerging, not settled.** While Claims 5, 6,
   and 12 are settled first-party statements (software identity, the
   author's own distinguishing criterion, and the author's own sourcing
   disclosure), the overall confidence is capped at "emerging" because the
   article's central quantitative claims (pricing, traffic, revenue) trace
   back either to the author's own limited direct observation (one day's
   lottery participation count, a self-tracked discount table with
   undisclosed methodology) or to unverified testimony from a single,
   self-interested forum thread whose primary poster is himself a relay
   operator (Claim 12). No claim in this note should be treated as
   independently verified market-research data.
4. **No contradiction issue filed.** This is a new topic area for the
   corpus (see Cross-References → Novel) with no existing source making an
   opposing claim about relay economics, reseller software, or this
   specific abuse taxonomy.
