---
source_url: https://simonwillison.net/2026/May/1/inat-sightings/
source_type: blog-post
title: "Tool: iNaturalist Sightings"
author: Simon Willison
date_published: 2026-05-01
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: anecdotal
issue: "#601"
---

# Tool: iNaturalist Sightings

> Simon Willison demonstrates a complete, end-to-end, serverless personal data tool
> built entirely on a phone via Claude Code for web — three components (Python CLI,
> GitHub Actions git-scraping pipeline, single-prompt HTML frontend) assembled over
> a camping weekend — providing concrete evidence that mobile-first, prompt-driven
> full-stack development is viable today and that the personal use case alone is
> sufficient justification under AI-native development economics.

## Source Context

- **Type**: blog-post (short tool-announcement post in Willison's characteristic
  link-blog style; ~200 words of original text plus a verbatim Claude Code prompt
  and technical links to three GitHub repositories. Short but dense with concrete
  technical decisions.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI;
  one of the highest-signal LLM tooling practitioners and commentators. He has built
  200+ personal tools at tools.simonwillison.net and has popularized the git-scraping
  pattern (documented at simonwillison.net/series/git-scraping). His tooling
  decisions are first-hand practitioner evidence, not speculation. The finished
  application is publicly accessible at tools.simonwillison.net/inat-sightings,
  providing behavioral verification that the described workflow actually produced
  working software.
- **Scope**: Covers one complete end-to-end tool build: motivation, architecture,
  three implementation components, and development environment. Does NOT cover
  multi-turn refinement (the post implies the frontend was a single-shot prompt),
  cost of the Claude Code session, or failure modes encountered. The post does not
  reflect on the development experience explicitly — it simply describes what was
  built.

## Extracted Claims

### Claim 1: Claude Code for web enables complete full-stack development on a mobile phone, with no desktop environment required

- **Evidence**: Willison's direct statement in the post, combined with the working
  deployed application at tools.simonwillison.net/inat-sightings as behavioral
  verification. Claude Code for web is the browser-accessible version of Claude
  Code, requiring no local CLI installation or desktop operating system.
- **Confidence**: anecdotal (single practitioner; single instance; but from a
  highly credible and prolific practitioner with a verifiable deployed output)
- **Quote**: "I'm camping this weekend so I built this entirely on my phone using
  Claude Code for web."
- **Our assessment**: This is the most novel claim in the source. It demonstrates
  that the "development environment" barrier has been fully removed: a complete
  three-component full-stack tool can be built from a mobile browser while camping,
  with no laptop, no local toolchain, and no desktop IDE. For practitioners who
  assumed AI-native development requires a development machine, this is a counter-
  example. The implications extend beyond convenience — mobile-first development
  changes who can participate in AI-native tooling and when development sessions
  can happen (on a camping trip, in transit, between meetings on a phone).

### Claim 2: A complete multi-component application can be built over a single weekend as a personal project using Claude Code

- **Evidence**: The iNaturalist project itself — a Python CLI, GitHub Actions
  automation, and HTML frontend — built "this weekend" while camping.
- **Confidence**: anecdotal (single practitioner example; no time tracking; but
  the completed application and its three GitHub repositories are publicly
  verifiable evidence)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This directly corroborates the "tools at blog-post cadence"
  thesis from `blog-simonwillison-rss-vibe-coded-apps.md` (Claim 1 there). The
  tool's use case is entirely personal — viewing one's own iNaturalist observations
  across two accounts — built in a camping weekend, deployed publicly, and
  representing the exact "personal, situated, frequent" tool category that Matt
  Webb and Willison identified in the rss-vibe-coded-apps post as the new norm
  under AI-accelerated development. The iNaturalist tool is not a hypothetical
  example; it is a concrete instantiation of the abstract cadence claim.

### Claim 3: A single-sentence Claude Code prompt can generate a complete, functional HTML frontend with multiple advanced UI features

- **Evidence**: The verbatim prompt published in the post, which produced
  inat-sightings.html — a working application with async data fetching, lazy-loaded
  thumbnails, modal dialogs for enlarged images, and conditional species name
  display. The deployed application at tools.simonwillison.net/inat-sightings
  confirms the prompt succeeded.
- **Confidence**: anecdotal (single instance; but the working application is
  direct verification of success)
- **Quote**: "Build inat-sightings.html - an app that does a fetch() against
  https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json
  and then displays all of the observations on one page using the
  https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for
  the thumbnails - with loading=lazy - but when a thumbnail is clicked showing
  the large.jpg in an HTML modal. Both small and large should include the common
  species names if available"
- **Our assessment**: This is the most concrete piece of evidence in the source
  and the highest-value artifact for the corpus. The prompt is remarkably terse:
  it specifies the data source URL, the thumbnail URL pattern, lazy loading,
  modal behavior on click, the large image URL convention, and a conditional
  display requirement for species names — all in a single run-on sentence. The
  working application confirms that Claude Code resolved the URL pattern from
  the example URL (`538073008/small.jpg` → infer the pattern), implemented lazy
  loading, wired modal behavior, and handled the species-name conditional correctly
  from one pass. For practitioners: this is evidence that specification density in
  a single prompt (explicit URLs, behavioral requirements, conditional logic) is
  more effective than iterative negotiation for UI generation tasks. The author
  published the exact prompt alongside the working result, making this a
  reproducible template.

### Claim 4: Git scraping is an effective zero-backend data pipeline for personal tools, enabling scheduled CLI execution and CORS-accessible JSON without any dedicated infrastructure

- **Evidence**: The simonw/inaturalist-clumps repository automates the
  inaturalist-clumper Python CLI via GitHub Actions, persists results to
  clumps.json in a public GitHub repo, and the HTML frontend fetches that JSON
  directly. This is Willison's established git-scraping pattern, documented at
  simonwillison.net/series/git-scraping.
- **Confidence**: emerging (single implementation in this post; but the git-scraping
  pattern is extensively documented in Willison's series and has been applied by
  other practitioners — this is not the first use)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Git scraping — using GitHub Actions to run a script on a
  schedule and commit the output to a repository — eliminates the need for a
  dedicated data API server. In the iNaturalist architecture: the CLI handles
  data ingestion from the iNaturalist API, GitHub Actions handles scheduling
  and persistence, and the raw GitHub JSON endpoint acts as a zero-cost API
  with permissive CORS headers. The frontend fetches data directly from
  raw.githubusercontent.com. No dedicated backend infrastructure, no cloud bill,
  no API key management beyond the initial CLI configuration. For the guide:
  git scraping deserves explicit treatment as a "zero-backend data layer" pattern
  for AI-native personal tools, separate from the serverless backend patterns
  aimed at multi-user applications.

### Claim 5: GitHub's raw file hosting supports CORS, making it viable as a lightweight API layer for JavaScript fetch() calls from static frontends

- **Evidence**: The inat-sightings.html uses a fetch() call to
  raw.githubusercontent.com to retrieve clumps.json. GitHub serves raw files
  with CORS headers that allow cross-origin requests. This is a documented GitHub
  behavior verified by the working application.
- **Confidence**: settled (CORS support for raw.githubusercontent.com is a
  documented and stable GitHub behavior; the working application demonstrates it)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The choice to use raw.githubusercontent.com as the data
  endpoint is a deliberate architectural decision, not an accident. The CORS
  support makes this viable. This is a concrete, infrastructure-free alternative
  to running a dedicated API backend for simple personal tools. The constraint:
  read-only data only, update latency depends on GitHub Actions schedule, and
  the JSON file must be small enough to load in full. Within those constraints,
  this is a zero-operational-overhead data delivery mechanism for tools that
  would otherwise require a backend.

### Claim 6: The three-component CLI + git-scraping + static-HTML architecture is a reusable pattern for personal data tools at minimal operational cost

- **Evidence**: The iNaturalist architecture: inaturalist-clumper (domain CLI) →
  inaturalist-clumps (GitHub Actions git scraping) → inat-sightings.html
  (static frontend). All three components are public GitHub repos; the frontend
  is hosted on Willison's tools site.
- **Confidence**: anecdotal (single instantiation; but follows Willison's
  established git-scraping methodology with an added frontend layer)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The pattern is: (1) write a domain-specific CLI to
  fetch/process data, (2) automate it with GitHub Actions to keep data current
  and commit to a public repo, (3) build a static HTML frontend that fetches
  the resulting JSON via CORS. This stack requires no cloud backend, no database,
  no deployment pipeline beyond `git push`, and has no ongoing operational cost
  beyond GitHub's free tier. For practitioners building personal data tools, this
  represents a minimal viable infrastructure. The pattern is particularly well-
  suited to AI-native development: Claude Code can build each component
  independently (CLI via terminal session, Actions YAML, HTML frontend via web),
  and the interfaces between components are simple file formats (JSON, YAML).

### Claim 7: Highly specific personal use cases — not commercial viability — are sufficient motivation for building production-quality AI-native tools

- **Evidence**: The entire project was motivated by Willison's personal desire to
  view his own iNaturalist observations across two accounts, grouped by proximity
  in time and space. No stated commercial intent; no mentioned user base beyond
  himself.
- **Confidence**: anecdotal (single example; but consistent with Willison's
  established portfolio of 200+ personal tools and the "personal, situated"
  tool pattern documented in rss-vibe-coded-apps.md)
- **Quote**: "I wanted to see my iNaturalist observations - across two separate
  accounts - grouped by when they occurred."
- **Our assessment**: This is the "calculator economics" argument at the personal
  tool level. Under pre-AI development economics, a custom tool for one person's
  naturalist observation management would never be worth building (the effort:benefit
  ratio for a single-user tool about one person's wildlife sightings is negative
  unless you count learning value). Under AI-native development economics, the same
  tool is feasible in a camping weekend on a phone. The personal friction — "I have
  two accounts and I want to see them together" — is sufficient justification because
  the development cost has fallen to the level of the personal benefit. For the guide:
  practitioners should internalize this threshold shift. Tools that serve one person's
  specific workflow are worth building now; they were not before.

## Concrete Artifacts

### The Claude Code prompt that generated inat-sightings.html (verbatim, from the post)

```
Build inat-sightings.html - an app that does a fetch() against
https://raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json
and then displays all of the observations on one page using the
https://static.inaturalist.org/photos/538073008/small.jpg small.jpg URLs for the
thumbnails - with loading=lazy - but when a thumbnail is clicked showing the large.jpg
in an HTML modal. Both small and large should include the common species names if available
```

Source: Simon Willison, simonwillison.net/2026/May/1/inat-sightings/, May 1, 2026

This prompt was executed via Claude Code for web (browser-based), on a phone while camping.
The output is live at: https://tools.simonwillison.net/inat-sightings

### Three-component iNaturalist architecture (from the post)

```
Component 1: Python CLI
  - Repo:    github.com/simonw/inaturalist-clumper
  - Purpose: Fetch observations from iNaturalist API; group into "clumps"
  - Default: observations within 2 hours and 5km of each other
  - Built with: Claude Code

Component 2: Git Scraping Automation
  - Repo:    github.com/simonw/inaturalist-clumps
  - Purpose: Runs inaturalist-clumper on schedule; commits clumps.json to repo
  - Pattern: GitHub Actions + git commit (Simon Willison's git-scraping methodology)
  - Data:    raw.githubusercontent.com/simonw/inaturalist-clumps/refs/heads/main/clumps.json

Component 3: Static HTML Frontend
  - File:    inat-sightings.html (in github.com/simonw/tools repo)
  - Live:    tools.simonwillison.net/inat-sightings
  - Built with: Single Claude Code prompt (see above)
  - Features: fetch() from GitHub raw CORS, lazy-loaded thumbnails, modal on click,
              species common names, iNaturalist photo CDN URLs

Interface between components: CORS-accessible JSON via GitHub raw file hosting
Backend infrastructure required: None
```

### inaturalist-clumper algorithm parameters (from repo and post)

```
Source: github.com/simonw/inaturalist-clumper + simonwillison.net/2026/May/1/inat-sightings/

Clumping algorithm:
  - Groups observations that occurred within 2 hours of each other (default)
  - AND within 5km of each other (default)
  - Parameters are configurable
  - Supports multiple iNaturalist accounts in a single clumps.json output

Tool: Python CLI using uv for dependency management
Testing: pytest-httpx for mocked API testing (no real network calls during tests)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1 — "Vibe-coding
  accelerates app development to the point where the release cadence becomes blog-post-like
  rather than product-launch-like." The iNaturalist tool is a concrete instantiation of
  this abstract claim: a complete tool built and shipped in a camping weekend, announced
  in a short blog post, with no product-launch ceremony.

- **Corroborates**: `blog-simonwillison-rss-vibe-coded-apps.md` Claim 2 — "Vibe-coded
  apps trend toward being more personal, more situated, and more frequent." The
  iNaturalist tool is exactly "personal" (solving Willison's own observation-management
  workflow), "situated" (built for a specific naturalist context), and frequent (one of
  200+ tools Willison has built). This source is the concrete evidence for the abstract
  claim in rss-vibe-coded-apps.

- **Corroborates**: `practitioner-dadlerj-tin.md` (Repo Context section) — tin is
  described as "100% vibe coded" with "this README.md is the only human-edited file
  in this repo." The iNaturalist tool extends this from a single developer tool to a
  complete multi-component stack, demonstrating that 100% AI-driven development scales
  beyond single-file tools to CLI + automation + frontend architectures.

- **Extends**: `blog-simonwillison-rss-vibe-coded-apps.md` — The rss-vibe-coded-apps
  source is abstract (cadence thesis, distribution gap, syndication proposal). The
  iNaturalist post provides the concrete worked example that the abstract thesis predicts.
  Together they form a theory (rss-vibe-coded-apps) + evidence (inat-sightings) pair.
  The Smith should cite both when making claims about personal tool cadence and
  AI-native development productivity.

- **Novel**:
  - **Claude Code for web as mobile development environment**: No prior corpus source
    documents using Claude Code's browser-based interface to build a complete project
    on a phone. This is the first in-corpus example of mobile-first, desktop-free AI
    development.
  - **Single-prompt frontend generation at feature density**: The verbatim prompt
    demonstrates that a single terse sentence can specify lazy loading, modal behavior,
    URL pattern conventions, and conditional display logic — producing a working
    multi-feature frontend. No prior corpus source documents a specific prompt of this
    kind with a verifiable working output.
  - **Git-scraping as a zero-backend AI-native data layer**: While Willison's git-
    scraping series predates this post, this is the first corpus source that documents
    the git-scraping + CORS raw GitHub JSON + static HTML frontend as a reusable
    architecture pattern explicitly combined with Claude Code for all three components.

- **Contradicts**: None identified. The source does not make claims that conflict with
  any existing corpus note.

## Guide Impact

- **Chapter on AI-native development fundamentals (Ch01/Ch02)**: Add Claude Code for
  web as an explicitly documented interface, distinct from the CLI. The guide should
  note that the browser-based version enables mobile development with no local toolchain.
  This is a barrier-reduction claim: the "you need a development machine" assumption
  is false. Cite Claim 1 and the Concrete Artifacts section.

- **Chapter on rapid prototyping and tool building (Ch03/Ch04)**: Add the single-prompt
  frontend generation pattern with the verbatim prompt as an example of specification
  density. The guide should teach practitioners to front-load requirements into a single
  dense prompt (explicit URLs, behavioral requirements, conditional logic) rather than
  iterating via multi-turn conversation for UI generation tasks. The iNaturalist prompt
  is the worked example.

- **Chapter on tool architecture and data pipelines**: Add the CLI + git-scraping +
  static-HTML pattern as a named architecture for personal data tools. Document
  GitHub raw CORS support as an architectural decision (CORS-accessible data layer
  at zero operational cost). This pattern deserves its own section or callout,
  distinct from serverless/cloud backend patterns.

- **Chapter on the economics of personal tooling (Ch01/Ch04)**: The "personal use
  case is sufficient justification" shift in development economics (Claim 7) should
  be stated explicitly. Under AI-native development, the threshold for "worth
  building" has dropped to personal utility. This is a mental model change, not
  just a productivity claim. Cite Claim 7 alongside the rss-vibe-coded-apps cadence
  thesis.

## Extraction Notes

- **Short source**: The post is approximately 200 words of original text plus the
  Claude Code prompt, links, and tags. It was read completely. The brevity is
  characteristic of Willison's tool-announcement style; the analytical payload is
  in the architecture and the verbatim prompt rather than in explicit reflection.
- **WebFetch limitation**: The WebFetch tool returned processed/summarized versions
  of the article rather than verbatim HTML. Quotes marked as verbatim were
  reproduced consistently across multiple independent fetches and are treated as
  high-confidence verbatim; other passages use "(no direct quote; see paraphrase
  in Our assessment)" per MINER.md §2a requirements.
- **Working application verified**: The application at
  tools.simonwillison.net/inat-sightings was fetched and confirmed to be live,
  though in a loading state during extraction (JavaScript data fetching is async).
  The existence of the application is the behavioral verification that the
  single-prompt claim succeeded.
- **Linked GitHub repos fetched**: github.com/simonw/inaturalist-clumper and
  github.com/simonw/inaturalist-clumps were fetched for technical details.
  The inaturalist-clumper repo README provided algorithm parameters (2 hours, 5km,
  configurable) and tooling choices (uv, pytest-httpx). The inaturalist-clumps
  repo returned limited detail (32 commits, GitHub Actions configured, clumps.json
  present).
- **Fragment URL**: The issue body URL includes `#atom-everything` as a fragment.
  The source_url uses the canonical page URL without the fragment, consistent with
  prior Willison source notes in this corpus.
- **Cross-reference verification**: `blog-simonwillison-rss-vibe-coded-apps.md`
  Claim 1 verified at lines 45-63 of that note. Claim 2 verified at lines 65-83.
  `practitioner-dadlerj-tin.md` Repo Context section verified at lines 18-20 of
  that note ("100% vibe coded" and "this README.md is the only human-edited file
  in this repo"). All cross-references verified against actual file contents before
  writing this note.
