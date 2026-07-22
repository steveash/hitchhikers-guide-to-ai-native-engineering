---
source_url: https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/
source_type: blog-post
title: "Firefox in WebAssembly"
author: Simon Willison (curating Puter's HeyPuter/firefox-wasm project and its Hacker News discussion)
date_published: 2026-07-16
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: anecdotal
issue: "#2124"
---

# Firefox in WebAssembly

> Puter compiled the Gecko/Firefox engine to WebAssembly and ran it inside another
> browser tab, reporting "over 25k in opus/fable tokens" of API-metered AI usage
> for the port — but the team's own follow-up comments reveal the actual
> out-of-pocket cost was closer to $100 via a single Claude Max 5x subscription
> plan, a sharper illustration of the subscription-vs-metered-billing gap than
> anything else currently in the corpus.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog / "blogmark," July 16, 2026,
  a short ~150-word curation piece with one embedded screenshot description,
  linking to Puter's live demo, the `HeyPuter/firefox-wasm` GitHub repository,
  the Wisp protocol spec, and the Hacker News discussion thread the post was
  filed "via"). Because the primary technical and cost claims live in the
  Hacker News thread (`news.ycombinator.com/item?id=48926939`) rather than in
  Willison's own prose, this note extracts directly from both: Willison's post
  for framing/summary, and first-hand comments from the project's own
  contributors (`coolelectronics`, `rlmineing_dead`, `ohonbob`) in the linked
  HN thread for the technical and cost specifics.
- **Author credibility**: Simon Willison is a trusted-feed source in this
  corpus (see author-credibility discussion in
  `blog-simonwillison-not-locked-in.md` and dozens of other notes) — but this
  post is pure secondary curation; Willison did not build the project or
  interview the team. The load-bearing claims come from `coolelectronics` and
  `rlmineing_dead`, who identify themselves in the HN thread as the people who
  built the project (they answer build/architecture/cost questions in first
  person and link their own supporting repos). Their HN handles are not
  independently verified identities, so these are self-reported practitioner
  claims, not audited figures — no AgentsView-style cost screenshot (contrast
  `blog-simonwillison-claude-fable-5.md`) or third-party token audit
  accompanies the $25k figure.
- **Scope**: Covers the Firefox-to-WebAssembly port's architecture (WISP
  protocol WebSocket proxying, single-process engine choice, experimental
  WASM→JS JIT), its AI-token cost and actual subscription billing, its
  development timeline, a mid-thread infrastructure scaling incident, and a
  technical disagreement over the "end-to-end encryption" framing. Does NOT
  cover: the actual Rust/C++ build toolchain internals beyond the public
  README's prerequisite list, any structured harness or review process (no
  mention of adversarial review, dynamic workflows, or multi-agent
  orchestration the way the Bun rewrite case study documents), or any
  post-launch maintenance plan.

## Extracted Claims

### Claim 1: Puter compiled the Gecko engine (including SpiderMonkey) to WebAssembly so that the full Firefox browser UI runs inside a `<canvas>` element in another browser
- **Evidence**: First-person description from `coolelectronics`, identified in the HN thread as the project's author, in the top-level project-announcement comment.
- **Confidence**: settled (the artifact is a public, runnable demo plus an open GitHub repository — independently checkable, not just an assertion)
- **Quote**: "This is the entire Firefox browser rendering to a <canvas> element. Gecko, all UI components, and the Spidermonkey JS engine are all compiled and running in WebAssembly." (comment by `coolelectronics`, news.ycombinator.com/item?id=48926939)
- **Our assessment**: This is the core, verifiable claim — a live demo and public repo back it up, unlike the cost figures below. It establishes that this isn't a partial or mocked port: the JS engine itself, not just UI chrome, is compiled to WASM.

### Claim 2: The port was reported to cost "over 25k" in Claude Opus/Fable tokens at API-metered pricing, but the team's actual out-of-pocket spend was closer to $100 because it ran under a single Claude Max 5x subscription plan
- **Evidence**: Two first-hand comments from the project's own contributors clarifying an initial ambiguity in the announcement (readers first assumed "25k" meant literal dollars, then literal token count, before the team clarified both the token-cost estimate and the real billing mechanism).
- **Confidence**: anecdotal (self-reported by HN accounts with no independent audit or billing screenshot; internally consistent across two different commenters, which raises credibility somewhat)
- **Quote**: "This port cost over 25k in opus/fable tokens for debugging and JIT research" (`coolelectronics`, top-level comment) — later clarified: "$25k of tokens, closer to 30 billion I believe." (`coolelectronics`, reply to `sangeeth96`) — and separately: "it was 25k WORTH of API billed tokens, but only actually 1 claude max 5x plan, so it was more like 100 dollars" (`rlmineing_dead`)
- **Our assessment**: This is the single most guide-relevant claim in the source. A ~250x gap between the API-metered valuation of tokens consumed ($25,000) and the actual cash outlay (~$100, one Claude Max 5x subscription) is a starker version of the pattern already documented in `blog-simonwillison-claude-fable-5.md` Claim 10 ($110.42 of token usage absorbed by a $100/month Max subscription in a single day). Unlike that note, there is no first-party billing dashboard evidence here (no AgentsView-style screenshot) — this is an unaudited practitioner claim from an anonymous-ish HN account, so it should be cited as illustrative rather than as a verified cost benchmark.

### Claim 3: Firefox/Gecko was chosen over Chromium/Blink specifically because Gecko's single-process support is more mature, making it a better fit for WASM's execution model
- **Evidence**: First-hand technical rationale from the project author, given directly in response to a question about why Firefox was picked.
- **Confidence**: emerging (a specific, falsifiable technical rationale from the person who made the choice, though not independently verified against Gecko/Blink internals)
- **Quote**: "Firefox was chosen because its single-process support was in a better place than chromium/blink." (`coolelectronics`, reply to `sangeeth96`)
- **Our assessment**: This is a concrete, checkable engineering rationale (not just "we picked Firefox because we like it") and it corroborates a pattern already in the corpus — see Cross-References below.

### Claim 4: The bulk of the ~25k-token-equivalent effort went into squeezing out performance and stability and attempting a JIT, not the initial bring-up, which took only a few days
- **Evidence**: First-hand timeline breakdown from the project author.
- **Confidence**: anecdotal (single self-reported timeline, no commit-history or calendar evidence provided in the thread)
- **Quote**: "It only took a few days to actually get the engine up, the hard parts where most of the effort was spent was squeezing out performance and increasing stability, as well as attempting the JIT." (`coolelectronics`, reply to `sangeeth96`)
- **Our assessment**: This reframes "how long did the AI-assisted port take" — the headline capability (get a browser engine to boot in WASM) was fast; the expensive, token-hungry work was performance/stability polish and an experimental JIT, which is a different cost profile than e.g. the Bun rewrite's structured 11-day migration-to-production timeline (`blog-pragmaticengineer-bun-rust-rewrite.md`).

### Claim 5: The project routes all guest-browser network traffic over a WebSocket connection using the Wisp protocol through a Puter-operated proxy server, because browser sandboxes don't allow arbitrary outbound TCP connections
- **Evidence**: Direct architectural description from Willison's post, corroborated by a contributor's more detailed technical comment about the TCP-over-WebSocket mechanism and the TLS-in-WASM implementation.
- **Confidence**: settled (matches the publicly linked Wisp protocol spec and is corroborated by multiple independent comments in the thread)
- **Quote**: "The demo funnels all traffic over a WebSocket protocol (using the Wisp protocol) through Puter's server - a requirement to get this kind of thing to work because code running in browsers can't open arbitrary network connections." (Willison, source post)
- **Quote (contributor detail)**: "The TCP proxy exit node we're using is running on Cloudflare, you can check that your traffic is still TLS encrypted by OpenSSL (also compiled to webassembly). The browser does not have a native API to send raw TCP so the proxying is done by the [wisp-protocol]." (`rlmineing_dead`)
- **Our assessment**: The architecture is a "dumb TCP pipe" proxy plus in-WASM TLS termination (OpenSSL compiled to WASM), not a decrypting man-in-the-middle proxy — this is the technical basis for the encryption claim examined in Claim 7.

### Claim 6: The proxying infrastructure saturated the NICs on the original two servers once the project reached the front page of Hacker News, forcing the team to add servers mid-thread
- **Evidence**: First-hand infrastructure post-mortem from a project contributor, posted during the same thread as the traffic spike was happening.
- **Confidence**: anecdotal (real-time, first-person operational account; not independently measured)
- **Quote**: "So funny story, supporting web codecs may have been a bad idea because it led to people using more traffic per session than we assumed at first. We had to add more servers mid HN post" (`rlmineing_dead`) — "We had completely saturated NICs on like the two original servers" (`rlmineing_dead`, same comment thread)
- **Our assessment**: This is a concrete operational cost of the proxy-everything architecture in Claim 5 that Willison's own post only gestures at ("(That proxying sounds expensive!..."). Bandwidth from routing full webcodec-heavy browser sessions through a central proxy, not compute, was the scaling bottleneck — worth noting for anyone building similar "cloud browser" demos.

### Claim 7: The project's "end-to-end encryption" claim was directly disputed in the thread — a commenter argued the proxy operator ultimately controls the WASM code the browser runs, so true end-to-end encryption is definitionally impossible in this architecture
- **Evidence**: A direct technical exchange between a skeptical commenter and the project's contributor, both quoted, representing a genuine unresolved disagreement rather than a settled claim.
- **Confidence**: anecdotal (an in-thread technical dispute, not resolved by either party changing position)
- **Quote (challenge)**: "By definition, i dont think you can be end2end encrypted in a web browser, since your server controls what code is run by the web browser. Puter would fully be able to spy on you if they were so inclined because they control what wasm you load." (`bawolff`)
- **Quote (defense)**: "End to end Encrypted is valid here because both peers of the request (client and server) have their information being exchanged through TLS and they both manage their own keys. We can't look inside the TLS tunnel, we only transport the TCP side. It's end to end encrypted in the same sense that when you go to hackernews your ISP can't see your password because of TLS." (`rlmineing_dead`)
- **Quote (rebuttal)**: "But its not like that. I do not have to trust my isp to not be evil. There is nothing my isp can do to read the password. I do have to trust you, you could easily modify the software in a way to read my password." (`bawolff`)
- **Our assessment**: `bawolff`'s rebuttal is the stronger technical argument — an ISP is a fixed, non-adversarial intermediary by construction, whereas Puter controls and can silently change the WASM binary the client trusts, which is not a property TLS-between-two-parties normally assumes away. Willison's own post ("Puter claim this supports end-to-end encryption and that looks to be true") only verified that HTTPS-vs-HTTP traffic is distinguishable in the WebSocket stream — that confirms TLS is being carried opaquely through the tunnel, not that the trust model is actually end-to-end in the security sense `bawolff` is using. The guide should not repeat "end-to-end encrypted" as an unqualified claim about this architecture.

### Claim 8: A parallel, independently-built project ports WebKit to WebAssembly using a mix of Fable, Opus, and GLM 5.2
- **Evidence**: A comment from a different contributor (`ohonbob`) posting their own related project in the same thread, explicitly noting the multi-model tool mix used to build it.
- **Confidence**: anecdotal (single self-reported project, no further detail on how the three models' work was divided)
- **Quote**: "Not as polished as the firefox port but is a fully working port of webkit ported with fable, opus and some glm 5.2." (`ohonbob`)
- **Our assessment**: This is a small but notable data point for multi-model tool use: rather than picking one frontier model, this contributor mixed Anthropic's Fable and Opus with Zhipu's GLM 5.2 for the same class of problem (browser-engine-to-WASM porting), which the corpus has limited direct evidence of at this scale/domain elsewhere.

### Claim 9: The public build requires a Linux host, `emscripten`, Node+pnpm, `emsdk` 6.0.1, and a `rustup` toolchain targeting `wasm32-unknown-emscripten`, invoked via a single `make web` command; an experimental JS-to-WASM JIT can be disabled with a `GECKO_NOWASMJIT=1` environment variable
- **Evidence**: The project's public README/build documentation.
- **Confidence**: settled (published, checkable build instructions) — but see Extraction Notes: this note paraphrases the README rather than quoting it verbatim, because the fetch tooling summarized rather than returned raw README text and MINER.md prohibits reconstructing quotes.
- **Quote**: (no direct quote; see paraphrase above — README text could not be retrieved raw)
- **Our assessment**: The `GECKO_NOWASMJIT=1` escape hatch confirms Claim 8-adjacent concerns from `coolelectronics`'s own framing ("a novel WASM→JS JIT for experimental site speedup") — the team shipped the JIT as opt-out rather than default-on, consistent with it being an experimental, stability-risk feature rather than a core dependency.

## Concrete Artifacts

### Full text of Willison's blogmark (verbatim, simonwillison.net/2026/Jul/16/firefox-in-webassembly/)

```
This is absurdly cool: Puter compiled Firefox to WebAssembly such that the
whole browser runs in another browser.

Here's my blog, running in Firefox, running in WebAssembly, running in Chrome:

[screenshot: Chrome network panel showing a 233MB gecko.wasm and an 18MB
chrome-assets.tar.zst]

They chose Firefox/Gecko because it has strong single-process support. The
project used an estimated $25,000 worth of Claude Opus and Fable tokens, but
took advantage of a Claude Max subscription plan so cost much less in actual
dollars.

The demo funnels all traffic over a WebSocket protocol (using the Wisp
protocol) through Puter's server - a requirement to get this kind of thing to
work because code running in browsers can't open arbitrary network
connections.

(That proxying sounds expensive! The team had to scale the servers up to
handle the traffic during the Hacker News conversation about the project.)

Puter claim this supports end-to-end encryption and that looks to be true - I
inspected the WebSocket messages and traffic to my own HTTPS site was
encrypted whereas requests and responses to `http://www.example.com/` were in
cleartext.

Tags: browsers, firefox, ai, webassembly, generative-ai, llms,
ai-assisted-programming, claude, claude-mythos-fable
```

### Linked artifacts (from the post and thread)

```
Live demo:      https://developer.puter.com/labs/firefox-wasm/
Source repo:    https://github.com/HeyPuter/firefox-wasm
HN discussion:  https://news.ycombinator.com/item?id=48926939
Wisp protocol:  https://github.com/MercuryWorkshop/wisp-protocol
Related demo:   https://github.com/theogbob/WebkitWasm (WebKit-to-WASM, "fable, opus and some glm 5.2")
Puter follow-up tool: https://github.com/HeyPuter/browser.js ("eats a bit less RAM")
```

### HN cost-clarification exchange (verbatim, news.ycombinator.com/item?id=48926939)

```
sangeeth96: "edit: I misunderstood, that's $25k not 25k tokens :/ time to
  log off." [initial reader misreading of the "25k" figure, corrected by
  the same commenter]

coolelectronics: "$25k of tokens, closer to 30 billion I believe. It only
  took a few days to actually get the engine up, the hard parts where most
  of the effort was spent was squeezing out performance and increasing
  stability, as well as attempting the JIT."

rlmineing_dead: "it was 25k WORTH of API billed tokens, but only actually
  1 claude max 5x plan, so it was more like 100 dollars"
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-servo-crate-exploration.md` Claim 2 (Claude Code
    correctly assessed WASM-compiling the Servo browser engine as infeasible
    "citing the specific constraints (threading and SpiderMonkey dependency)").
    This source's Claim 3 — Gecko was chosen over Chromium/Blink specifically
    for its *single-process* maturity — is the positive-case mirror of that
    same constraint: browser engines built around heavy OS-thread reliance
    are the hard case for WASM compilation, and single-process design is
    what made this port tractable at all. The two notes describe the same
    underlying technical constraint from opposite sides (a project that hit
    it and pivoted away, and a project that specifically routed around it).
  - `blog-simonwillison-claude-fable-5.md` Claim 10 (Willison's own $110.42
    of Fable token usage absorbed by a $100/month Max subscription). This
    source's Claim 2 is a more extreme version of the identical pattern:
    large API-metered token valuations becoming small real-dollar costs
    under a Claude Max subscription.
- **Contradicts**: None identified. The "end-to-end encryption" dispute in
  Claim 7 is an in-thread disagreement between two HN commenters, not a
  disagreement with an existing corpus source-note — it does not rise to a
  `[[CONTRADICTIONS.md]]`-worthy cross-source contradiction, so no
  contradiction issue was filed. It is flagged here as a claim the guide
  should not repeat unqualified.
- **Extends**: `blog-pragmaticengineer-bun-rust-rewrite.md` (Claims 1 and 5:
  the Bun Zig-to-Rust rewrite's $165,000 API-metered token cost over an
  11-day structured migration with a formal adversarial-review harness) and
  `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 6: the same Bun
  rewrite used dynamic workflows). This source is a much smaller, less
  structured data point on the same "AI ports a large existing codebase"
  spectrum — no mention of adversarial review, dynamic workflows, or a
  formal merge bar; the author's own framing ("This was just a fun
  experiment to push the boundaries of WebAssembly") and timeline ("a few
  days" for initial bring-up) contrasts with Bun's disciplined 11-day
  production migration. Useful for the guide as the informal/exploratory end
  of that spectrum, next to Bun's disciplined/production end.
- **Novel**: The specific ~250x gap between API-metered token valuation
  ($25k) and actual subscription cost (~$100) is the sharpest single data
  point of that gap currently in the corpus. The WISP-protocol WebSocket-TCP
  proxy architecture (with TLS terminated inside the WASM guest rather than
  by the proxy) is a novel concrete architecture pattern not previously
  documented. The multi-model (Fable + Opus + GLM 5.2) WebKit-to-WASM side
  project mentioned in Claim 8 is also new to the corpus.

## Guide Impact

- **Chapter 02 (Cost-Benefit Analysis)**: Add this source's Claim 2 as a
  second, more extreme illustration — alongside the existing
  `blog-simonwillison-claude-fable-5.md` Claim 10 citation — of why raw
  "tokens consumed" or "API-list-price-equivalent" figures are not a
  reliable stand-in for actual project cost. Recommend the guide explicitly
  state the billing-model caveat: metered API cost and subscription-plan
  cost can diverge by two orders of magnitude for the same token volume, so
  any "$X of tokens" claim in a case study should be read alongside how it
  was billed, not treated as a dollar figure on its own.
- **Chapter 02 (Harness Engineering)**: Recommend citing this source next to
  `blog-pragmaticengineer-bun-rust-rewrite.md` as the informal/low-harness
  end of a spectrum the guide already documents at the high-structure end
  (adversarial review, dynamic workflows, formal merge criteria). This
  source shows a large systems-port task (browser engine → WASM) completed
  with apparently no formal review harness, at a fraction of the cost and
  time of the Bun rewrite — worth a caveat that lower-stakes/exploratory
  ports may not need Bun-level process, but the guide should note the
  tradeoff explicitly (no mention here of test-suite conformance checking,
  unlike Bun's "100% of test suite passing" merge bar).
- **Chapter 01 or wherever encryption/trust claims about AI-built systems are
  discussed**: If the guide ever cites vendor or project claims of
  "end-to-end encryption" for browser-proxy architectures, this source's
  Claim 7 is a concrete example of why such claims should be scrutinized —
  the proxy operator's control over the client-side code (even if that code
  is WASM) undermines the trust model in a way distinct from a passive
  network intermediary like an ISP.

## Extraction Notes

- Followed the "via" link from Willison's post to the Hacker News discussion
  thread (`news.ycombinator.com/item?id=48926939`) and pulled it via the
  Algolia HN API (`hn.algolia.com/api/v1/items/48926939`) to get raw,
  unprocessed comment text rather than an LLM-summarized rendering — the
  cost-clarification and encryption-dispute quotes in this note come from
  that raw JSON and are high-confidence verbatim.
  Also visited the live demo page (`developer.puter.com/labs/firefox-wasm/`)
  and the GitHub repo (`github.com/HeyPuter/firefox-wasm`) README, but the
  fetch tooling available in this environment returned summarized/paraphrased
  content for both rather than raw page text, so Claim 9's build
  requirements are presented as paraphrase, not verbatim quote, per MINER.md
  §2a's guidance to prefer a missing quote over a reconstructed one.
- Did not follow the `theogbob/WebkitWasm` repo link in depth — it is
  mentioned in Claim 8 only as reported by other commenters, not
  independently verified beyond confirming the link resolves.
- No contradiction issue was filed. The in-thread "end-to-end encryption"
  dispute (Claim 7) is a disagreement between two HN commenters, not a
  disagreement with any existing corpus source-note, so it does not meet the
  MINER.md §4a bar for filing a contradiction issue.
