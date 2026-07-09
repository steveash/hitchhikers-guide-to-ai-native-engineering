---
source_url: https://vercel.com/blog/how-fern-runs-multi-tenant-docs-for-webflow-and-elevenlabs-on-vercel
source_type: blog-post
title: "How Fern runs multi-tenant docs for Webflow and ElevenLabs on Vercel"
author: Eric Dodds (Vercel)
date_published: 2026-06-09
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: anecdotal
issue: "#1680"
---

# How Fern runs multi-tenant docs for Webflow and ElevenLabs on Vercel

> A short Vercel customer-story page (built around a 3-minute video, with no
> transcript available) reporting that Fern serves multi-tenant developer
> documentation for Webflow, ElevenLabs, and other customers from a single
> Next.js app on Vercel, and that a partial Pages Router → App Router
> migration (65% of the platform in 7 days) preceded self-reported gains in
> TTFB, page load time, and deploy speed — all self-reported, single-source
> vendor metrics with no methodology disclosed.

## Source Context

- **Type**: blog-post (Vercel Blog, "Customers" category customer-story
  page). The page is built around an embedded 3-minute Mux-hosted video
  (`mux.com/00F402Vtat2hrJpX55lu02oDJAwmF9V4XrVZNGFpmGDz84`) — the page's own
  read-time label is "3 min watch," not a reading-time estimate for prose.
  The accompanying text is a single descriptive paragraph plus a four-item
  stat-highlight list; there is no separate written case-study body.
- **Author credibility**: Byline is Eric Dodds, listed as "Content Engineer"
  at Vercel. Dodds is also a co-listed author (alongside Jerilyn Zheng and
  Harpreet Arora) on Vercel's AI Gateway production index, corroborated
  directly in this corpus by `blog-vercel-ai-gateway-production-index-may2026.md`
  frontmatter (`author: Jerilyn Zheng, Harpreet Arora, Eric Dodds (Vercel)`).
  This is first-party Vercel marketing content about a Vercel customer
  (Fern); the performance and migration figures are self-reported by Vercel
  on Fern's behalf, with no named Fern engineer quoted in the text, no
  methodology, no baseline definition (e.g., what "80%" is measured against,
  over what time window), and no link to an independent or Fern-authored
  account of the same numbers.
- **Scope**: Covers only four things, all asserted without elaboration: (1)
  Fern's business (developer docs/SDK hosting for other companies), (2) that
  it serves multiple named customers from one multi-tenant Next.js app via
  custom domains, (3) a partial Pages Router → App Router migration
  completed in 7 days, and (4) four aggregate performance/scale metrics.
  Does NOT cover: how multi-tenancy is implemented (routing, tenant
  isolation, custom-domain provisioning mechanism), why or how the App
  Router migration was executed, what blocked the remaining 35% of the
  migration, what caused the performance improvements mechanically (ISR,
  caching, edge config, etc.), any AI-specific tooling or AI-native
  engineering practice, or any direct quote from a Fern employee.

## Extracted Claims

### Claim 1: Fern serves customer documentation for multiple named companies, including Webflow and ElevenLabs, across custom domains from a single multi-tenant Next.js application on Vercel
- **Evidence**: Direct descriptive statement in the page's sole body paragraph; no architectural detail (tenant isolation, routing mechanism, custom-domain provisioning) is given beyond this sentence.
- **Confidence**: anecdotal (single-source, vendor-authored description of a customer's architecture; no independent corroboration or technical elaboration)
- **Quote**: "Fern helps companies ship developer documentation and SDKs, running customer docs for Webflow, ElevenLabs, and others across custom domains from a single Next.js app on Vercel."
- **Our assessment**: This establishes the "what" (multi-tenant doc hosting via one codebase, per-customer custom domains) but supplies none of the "how" that would make it useful as an implementation pattern for the guide — there is no detail on how tenant routing, per-customer theming, or domain-to-tenant mapping actually works in Fern's Next.js app. As a data point it only confirms that this architecture (one app, many customer-facing domains) is viable at the scale described in Claim 4, not how to build it.

### Claim 2: Fern migrated 65% of its platform from the Pages Router to the App Router in seven days, avoiding what the source characterizes as a months-long engineering project
- **Evidence**: Stated both in the stat-highlight list and restated with added framing in the body paragraph.
- **Confidence**: anecdotal (self-reported percentage and timeframe; no definition of how "65% of the platform" is measured — by route count, page count, traffic share, or engineering effort — and no account of what was migrated first or why)
- **Quote**: "65% of the platform migrated from Pages Router to App Router in 7 days" / "Mid-migration from the Pages Router to the App Router, the team moved 65% of the platform in seven days instead of taking on a months-long engineering project."
- **Our assessment**: The claim is explicitly framed as a comparison against a counterfactual ("instead of taking on a months-long engineering project") that the source never substantiates — there is no baseline estimate, prior planning document, or other team's comparable migration cited to justify what a "months-long" migration would otherwise have looked like. Fern is still "mid-migration" (35% remaining, unquantified in time), so this is a report of a favorable in-progress trend, not a completed, verifiable outcome. The source gives no method (codemod, incremental route-by-route conversion, AI-assisted refactor, or otherwise) for how the 65% was achieved.

### Claim 3: Fern's documentation platform serves 6 million or more page views per month from 1 million or more unique visitors
- **Evidence**: Stat-highlight list item; not repeated or elaborated elsewhere in the page.
- **Confidence**: anecdotal (self-reported scale figure with no time window specified precisely — "per month" is given, but no specific month or date range, and no distinction between total-platform traffic vs. per-customer breakdown for Webflow, ElevenLabs, or others)
- **Quote**: "6 million+ page views per month from 1 million+ unique visitors"
- **Our assessment**: This is a scale indicator (roughly 6 page views per unique visitor per month, aggregated across all of Fern's customer docs), useful only as context for how large a "multi-tenant docs on Vercel" deployment can get, not as evidence for any specific technical or AI-native practice.

### Claim 4: Fern deploys multiple times per day, with individual deploys taking as little as five minutes
- **Evidence**: Body paragraph statement; not elaborated with any detail on CI/CD pipeline, build caching, or what changed to reach this deploy time (i.e., no before/after comparison is given for deploy time, unlike the explicit before/after framing given for TTFB and page load).
- **Confidence**: anecdotal (self-reported; "down to five minutes" implies an improvement from some earlier, unstated deploy time, but no prior figure is given)
- **Quote**: "Today Fern deploys multiple times a day, with deploys down to five minutes and page load times cut by up to 80%."
- **Our assessment**: The phrase "down to five minutes" implies this is an improvement, but — unlike the TTFB and page-load stats, which are given as explicit multipliers/percentages — no baseline deploy time is stated anywhere on the page, so the actual magnitude of improvement cannot be assessed from this source alone.

### Claim 5: Fern's documentation pages now load 3x faster in time-to-first-byte (TTFB) and have page load times reduced by up to 80%, attributed in context to the App Router migration
- **Evidence**: Two separate stat-highlight list items, restated together in the body paragraph's closing sentence ("page load times cut by up to 80%").
- **Confidence**: anecdotal (self-reported performance multiplier and percentage; no baseline measurement methodology, no specification of which pages/routes were measured, no distinction between the already-migrated 65% and the still-Pages-Router 35%, and no third-party or Fern-published corroborating benchmark)
- **Quote**: "3x faster time to first byte" / "Page load times reduced by 80%"
- **Our assessment**: These are the source's most concrete-sounding numbers, but the causal link to the App Router migration is implied by proximity and framing (the stats sit directly under the migration story) rather than stated explicitly as cause-and-effect anywhere in the text — the source never writes a sentence directly attributing the TTFB/page-load gains to the router migration specifically, as opposed to other unstated infrastructure changes made in the same period. Without a stated methodology, these numbers should be treated as a vendor-published marketing claim, not a benchmarked result a practitioner could expect to reproduce.

## Concrete Artifacts

### Full page text (verbatim, excluding site navigation/footer chrome)

```
How Fern runs multi-tenant docs for Webflow and ElevenLabs on Vercel
Eric Dodds
Content Engineer
Blog / Customers
9 Jun 2026
3 min watch

Fern on Vercel
- 3x faster time to first byte
- Page load times reduced by 80%
- 6 million+ page views per month from 1 million+ unique visitors
- 65% of the platform migrated from Pages Router to App Router in 7 days

Fern helps companies ship developer documentation and SDKs, running
customer docs for Webflow, ElevenLabs, and others across custom domains
from a single Next.js app on Vercel. Mid-migration from the Pages Router
to the App Router, the team moved 65% of the platform in seven days
instead of taking on a months-long engineering project. Today Fern
deploys multiple times a day, with deploys down to five minutes and page
load times cut by up to 80%.

Source: https://vercel.com/blog/how-fern-runs-multi-tenant-docs-for-webflow-and-elevenlabs-on-vercel
```

This is the complete body content of the page — there is no additional
prose section, pull quote, named-engineer testimonial, or written case
study beyond what is reproduced above. The page's primary content is an
embedded video (Mux asset ID
`00F402Vtat2hrJpX55lu02oDJAwmF9V4XrVZNGFpmGDz84`); no transcript, captions
track, or `.vtt` file was found in the page's HTML, so the video's content
could not be extracted or included in this note.

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-production-index-may2026.md` and
`blog-vercel-ai-gateway-api-key-budgets.md` were re-read in full during this
extraction (MINER.md §4b); no `### Claim N:` heading in either note concerns
Next.js routing, multi-tenant documentation hosting, or framework migration,
so no `Claim N` citation is made against either — both are cited below only
by frontmatter/author-identity fact (Eric Dodds' co-authorship) and by
scope contrast (both cover the AI Gateway product, not application
deployment architecture). A corpus-wide search for "App Router," "Pages
Router," "multi-tenant," and "custom domain" surfaced no existing source
note covering a Next.js Pages Router → App Router migration or a
multi-tenant documentation-hosting architecture; the closest matches
(`docs-ghaw-guides-network-configuration.md`, `docs-ghaw-network-reference.md`)
concern gh-aw workflow network egress allowlisting for custom domains, an
unrelated meaning of "custom domain," and are not cited as overlapping.

- **Corroborates**: None found. No existing source note documents Next.js
  App Router migration timelines, multi-tenant documentation platform
  architecture, or Vercel deploy-time benchmarks for a customer application
  (as opposed to Vercel's own AI Gateway product, covered by
  `blog-vercel-ai-gateway-production-index-may2026.md` and
  `blog-vercel-ai-gateway-api-key-budgets.md`).

- **Contradicts**: None identified.

- **Extends**: `blog-vercel-ai-gateway-production-index-may2026.md` and
  `blog-vercel-ai-gateway-api-key-budgets.md` — both existing Vercel-sourced
  notes in the corpus cover Vercel's own AI Gateway product (usage telemetry
  and API-key spend controls, respectively). This note is the corpus's first
  Vercel source concerning a customer's *application deployment
  architecture* on the platform, rather than the AI Gateway product itself;
  it does not extend either note's specific claims, only the corpus's
  coverage of what Vercel publishes about customers.

- **Novel**: The entire subject — Next.js Pages Router → App Router
  migration timelines/scope, multi-tenant documentation hosting for
  multiple customer-facing custom domains from one codebase, and Vercel
  deploy-time figures for a customer (non-Vercel-product) application — is
  new to this corpus. No existing note addresses framework-migration
  strategy, multi-tenant SaaS routing architecture on Next.js, or
  comparative deploy-time benchmarks for docs platforms.

## Guide Impact

This source has minimal guide impact and no direct AI-native engineering
content; it is a general SaaS infrastructure/deployment case study, not an
AI-native engineering source, despite Fern's own customers (Webflow,
ElevenLabs) being AI-native-adjacent companies. Recommend against adding
it as a cited data point to any chapter:

- **Chapter 02 (Harness Engineering)**: No specific recommendation. The
  95%-confidence-lacking migration and performance figures (Claims 2 and 5)
  are exactly the kind of self-reported, methodology-free vendor metric the
  guide should avoid citing as evidence for a "framework migrations can be
  done incrementally and quickly" claim — there is no reproducible detail
  (approach, tooling, team size, before/after baseline) a practitioner could
  act on. If the guide later needs an example of incremental Pages Router →
  App Router migration, this source should not be the citation; a source
  with named engineers, a described methodology, or code-level detail would
  be needed instead.
- **Chapter 05 (Team Adoption)**: No specific recommendation — the source
  contains no team-process, adoption, or organizational detail beyond a
  single unelaborated sentence about migration timing.

## Extraction Notes

1. **WebFetch (the AI-summarizing tool) undercounted the page's own content
   on three separate passes**, each returning a slightly different partial
   summary of the same short paragraph and stat list, none flagging that
   this was the *entire* body text rather than an excerpt. To confirm
   nothing was being missed (e.g., hidden by client-side hydration or
   JS-rendered content not captured by the summarizer), this note instead
   fetched the raw page HTML directly via `curl` (425,741 bytes,
   `/tmp/fern.html`), stripped script/style/markup with a Python script, and
   read the full resulting plain text (227 lines, `/tmp/fern_text.txt`) in
   its entirety, including all navigation chrome, to verify no article body
   content was being missed. The result confirmed WebFetch's summaries were
   accurate as far as they went — the page genuinely contains only the one
   paragraph and four-item stat list reproduced in Concrete Artifacts above,
   framing an embedded 3-minute video as the primary content.
2. **No sub-pages followed.** Per MINER.md §1's "follow up to 5 linked
   pages that seem substantive," the page's only in-content links are
   generic CTAs ("Start Deploying," "Talk to an Expert") pointing to
   Vercel's own signup/sales pages, not to any Fern-authored or
   third-party page with more detail. No substantive linked page was found
   to follow.
3. **Video content could not be extracted.** The page is built around an
   embedded Mux-hosted video (`00F402Vtat2hrJpX55lu02oDJAwmF9V4XrVZNGFpmGDz84`,
   confirmed via direct HTML inspection); this is very likely where most of
   the substantive information about Fern's actual migration process and
   architecture lives (the page explicitly labels itself "3 min watch"
   rather than giving a reading-time estimate). No caption track, transcript
   endpoint, or `.vtt` file reference was found in the page HTML, so the
   video's content is not reflected in this note. This is the primary
   reason the extraction is thin relative to typical source notes in this
   corpus (contrast e.g. `blog-vercel-ai-gateway-api-key-budgets.md`, ~9
   claims from a changelog plus a linked reference page) — it is a limit of
   the source's format (video-first customer testimonial with a short
   text stub), not a shortfall in extraction effort.
4. **Confidence calibration: anecdotal.** All three prior Prospector triage
   passes on this issue independently flagged the same concern (thin
   content, self-reported metrics, tangential AI-native relevance); this
   extraction confirms that assessment directly. Every numeric claim in the
   source (Claims 2-5) is self-reported by Vercel on behalf of a customer,
   with no stated methodology, baseline, or measurement window, and no
   independent or Fern-authored corroboration was found. The descriptive
   claim (Claim 1) is plausible and uncontroversial but similarly
   unelaborated. `confidence_overall: anecdotal` reflects that the source's
   evidentiary weight rests entirely on unverified vendor-marketing
   self-report, not that the claims are believed to be false.
5. **No contradiction issues filed.** No existing source note makes a
   claim that materially opposes anything in this source.
